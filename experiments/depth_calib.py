#!/usr/bin/env python3
"""Parser kalibrasi sidecar SawitMVC-Depth + reproyeksi depth -> bidang color.

Dipakai oleh reproject_depth.py dan verify_depth_align.py (E-022).

TEMUAN YANG MELANDASI MODUL INI (E-022, 2026-07-29): label sidecar
`"alignedTo": "color"` MENYESATKAN — buffer 848x480 masih berada di grid kamera
depth pabrikan, belum di-D2C ke bidang color. Bukti: (1) intrinsik depth
piksel-persegi (fx=fy=416,55) bukan versi terskala intrinsik color
(610,87*848/1280=404,7 pada x tetapi 610,87*480/800=366,5 pada y); (2) tidak ada
baris/kolom yang selalu-invalid di tepi, padahal FOV vertikal color (66,4 deg)
lebih lebar daripada depth (59,9 deg); (3) estimasi skala empiris lewat mutual
information memberi s_y ~ 1,455, sedangkan resize langsung mengharuskan 1,667.

Konsekuensi: resize naif meleset median ~29 px (maks ~61 px) pada bidang
1280x800 — seukuran tandan B4 itu sendiri. Modul ini melakukan reproyeksi
per-piksel penuh: depth -> titik 3D (intrinsik depth) -> ekstrinsik ->
proyeksi intrinsik color + distorsi Brown-Conrady K6.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np

DEPTH_W, DEPTH_H = 848, 480
RGB_W, RGB_H = 1280, 800

# Nilai di atas ini diperlakukan tidak valid: 1,171% piksel >15 m dan 0,061%
# tepat 65535 (saturasi uint16) — hampir pasti langit / derau ToF, bukan pohon.
MAX_VALID_MM = 15000.0


@dataclass(frozen=True)
class Kalibrasi:
    fx_d: float
    fy_d: float
    cx_d: float
    cy_d: float
    fx_c: float
    fy_c: float
    cx_c: float
    cy_c: float
    k: tuple[float, ...]  # k1..k6 color
    p1: float
    p2: float
    rot: tuple[float, ...]  # 9 elemen, row-major
    trans: tuple[float, ...]  # mm

    @property
    def kunci(self) -> str:
        """ID unit kamera — dataset ini memuat DUA unit dengan intrinsik berbeda."""
        return f"{self.fx_d:.3f}_{self.cx_d:.3f}"


def _angka(teks: str, nama: str) -> float:
    m = re.search(rf"{nama}=(-?[\d.]+(?:[eE]-?\d+)?)", teks)
    if not m:
        raise ValueError(f"{nama} tidak ditemukan")
    return float(m.group(1))


def _blok(dump: str, nama: str) -> str:
    m = re.search(rf"{nama}=\w+\{{([^}}]*)\}}", dump)
    if not m:
        raise ValueError(f"blok {nama} tidak ditemukan")
    return m.group(1)


def _vektor(dump: str, nama: str) -> tuple[float, ...]:
    m = re.search(rf"{nama}=\[([^\]]*)\]", dump)
    if not m:
        raise ValueError(f"vektor {nama} tidak ditemukan")
    return tuple(float(x) for x in m.group(1).split(","))


@lru_cache(maxsize=8)
def _parse_dump(dump: str) -> Kalibrasi:
    di = _blok(dump, "mDepthIntrinsic")
    ci = _blok(dump, "mColorIntrinsic")
    cd = _blok(dump, "mColorDistortion")
    return Kalibrasi(
        fx_d=_angka(di, "mFx"), fy_d=_angka(di, "mFy"),
        cx_d=_angka(di, "mCx"), cy_d=_angka(di, "mCy"),
        fx_c=_angka(ci, "mFx"), fy_c=_angka(ci, "mFy"),
        cx_c=_angka(ci, "mCx"), cy_c=_angka(ci, "mCy"),
        k=tuple(_angka(cd, f"mK{i}") for i in range(1, 7)),
        p1=_angka(cd, "mP1"), p2=_angka(cd, "mP2"),
        rot=_vektor(dump, "mRot"), trans=_vektor(dump, "mTrans"),
    )


def baca_kalibrasi(sidecar: Path) -> Kalibrasi:
    """Kalibrasi PER BERKAS — jangan hardcode, dataset memuat dua unit kamera."""
    return _parse_dump(json.loads(sidecar.read_text())["calibrationDump"])


def baca_depth_mm(raw: Path) -> np.ndarray:
    """.raw uint16le 848x480 -> float32 milimeter; invalid (0 dan >15 m) = 0."""
    z = np.fromfile(raw, dtype="<u2").astype(np.float32)
    if z.size != DEPTH_W * DEPTH_H:
        raise ValueError(f"{raw}: {z.size} sampel, harusnya {DEPTH_W * DEPTH_H}")
    z = z.reshape(DEPTH_H, DEPTH_W)
    z[z > MAX_VALID_MM] = 0.0
    return z


def _distorsi_color(x: np.ndarray, y: np.ndarray, kal: Kalibrasi) -> tuple[np.ndarray, np.ndarray]:
    """Brown-Conrady K6 (rasional) pada koordinat ternormalisasi kamera color."""
    k1, k2, k3, k4, k5, k6 = kal.k
    r2 = x * x + y * y
    r4 = r2 * r2
    r6 = r4 * r2
    radial = (1 + k1 * r2 + k2 * r4 + k3 * r6) / (1 + k4 * r2 + k5 * r4 + k6 * r6)
    xd = x * radial + 2 * kal.p1 * x * y + kal.p2 * (r2 + 2 * x * x)
    yd = y * radial + kal.p1 * (r2 + 2 * y * y) + 2 * kal.p2 * x * y
    return xd, yd


def reproyeksi(z_mm: np.ndarray, kal: Kalibrasi, *, distorsi: bool = True,
               ekstrinsik: bool = True) -> np.ndarray:
    """Depth di grid kamera depth -> peta depth (mm) di grid RGB 1280x800.

    Forward-warp dengan Z-BUFFER: bila beberapa piksel depth jatuh ke piksel
    tujuan yang sama, yang DIAMBIL adalah yang paling dekat. Tanpa ini, piksel
    latar (jauh) menimpa piksel objek (dekat) di tepi oklusi — justru tepi
    oklusi itulah sinyal yang dicari untuk B4 yang tertanam di pelepah.

    Piksel tujuan tanpa sumber bernilai 0 = "tidak ada data".
    """
    v, u = np.nonzero(z_mm)
    if u.size == 0:
        return np.zeros((RGB_H, RGB_W), np.float32)
    z = z_mm[v, u]

    # piksel depth -> titik 3D di kerangka kamera depth (mm)
    X = (u - kal.cx_d) * z / kal.fx_d
    Y = (v - kal.cy_d) * z / kal.fy_d

    if ekstrinsik:
        r = kal.rot
        t = kal.trans
        Xc = r[0] * X + r[1] * Y + r[2] * z + t[0]
        Yc = r[3] * X + r[4] * Y + r[5] * z + t[1]
        Zc = r[6] * X + r[7] * Y + r[8] * z + t[2]
    else:
        Xc, Yc, Zc = X, Y, z

    baik = Zc > 1.0
    Xc, Yc, Zc = Xc[baik], Yc[baik], Zc[baik]

    xn = Xc / Zc
    yn = Yc / Zc
    if distorsi:
        xn, yn = _distorsi_color(xn, yn, kal)

    uc = np.rint(kal.fx_c * xn + kal.cx_c).astype(np.int32)
    vc = np.rint(kal.fy_c * yn + kal.cy_c).astype(np.int32)

    di_dalam = (uc >= 0) & (uc < RGB_W) & (vc >= 0) & (vc < RGB_H)
    uc, vc, Zc = uc[di_dalam], vc[di_dalam], Zc[di_dalam]

    kanvas = np.full(RGB_H * RGB_W, np.inf, np.float32)
    np.minimum.at(kanvas, vc * RGB_W + uc, Zc)  # z-buffer: ambil yang terdekat
    kanvas[np.isinf(kanvas)] = 0.0
    return kanvas.reshape(RGB_H, RGB_W)


def tambal_lubang(peta: np.ndarray, iterasi: int = 2) -> np.ndarray:
    """Isi piksel kosong hasil forward-warp dengan MEDIAN tetangga yang valid.

    Skala reproyeksi ~1,47 meninggalkan sebagian besar piksel tujuan kosong
    sebagai kisi. Operator RANKING (median) dipakai, bukan blur/bilinear:
    operator rata-rata menghasilkan kedalaman "hantu" yang melintasi batas
    objek dan menghapus tepi oklusi.
    """
    import cv2

    keluar = peta.copy()
    for _ in range(iterasi):
        kosong = keluar == 0
        if not kosong.any():
            break
        # median 3x3 hanya atas tetangga valid: median dari nilai bukan-nol
        med = _median_valid_3x3(keluar)
        keluar[kosong] = med[kosong]
    return keluar


def _median_valid_3x3(peta: np.ndarray) -> np.ndarray:
    """Median 3x3 yang MENGABAIKAN piksel nol (tidak ada data)."""
    h, w = peta.shape
    pad = np.pad(peta, 1, constant_values=0)
    tumpuk = np.empty((9, h, w), np.float32)
    i = 0
    for dy in range(3):
        for dx in range(3):
            tumpuk[i] = pad[dy:dy + h, dx:dx + w]
            i += 1
    tumpuk[tumpuk == 0] = np.nan
    with np.errstate(invalid="ignore"):
        med = np.nanmedian(tumpuk, axis=0)
    return np.nan_to_num(med, nan=0.0).astype(np.float32)


def encode_inverse(z_mm: np.ndarray, z_near_m: float, z_far_m: float) -> np.ndarray:
    """Peta depth (mm, 0=invalid) -> kanal kanonik uint8 (kontrak fourch.py).

    0 = tidak ada data; 1..255 = inverse depth pada rentang metrik TETAP
    [z_near, z_far]: dekat -> 255, jauh -> 1. Tanpa normalisasi per-citra —
    normalisasi per-citra membuang jarak absolut dan membuat nilai piksel tidak
    sebanding antar-frame.
    """
    z = z_mm / 1000.0
    valid = z > 0
    zc = np.clip(z, z_near_m, z_far_m)
    inv = (1.0 / zc - 1.0 / z_far_m) / (1.0 / z_near_m - 1.0 / z_far_m)
    keluar = np.rint(1 + inv * 254).astype(np.uint8)
    keluar[~valid] = 0
    return keluar
