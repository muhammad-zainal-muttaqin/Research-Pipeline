#!/usr/bin/env python3
"""E-022 gerbang wajib: buktikan pemetaan depth->RGB mana yang benar.

Hipotesis yang diuji (H-022c): "buffer depth SawitMVC-Depth sudah tersejajar ke
bidang color" sebagaimana klaim sidecar `alignedTo: "color"`.

Uji dilakukan dengan ANOTASI, bukan korelasi tepi — korelasi tepi (NCC gradien)
sudah terbukti tidak konklusif pada kanopi sawit (semua kandidat NCC ~ -0,07).
Gagasannya: tandan adalah objek padat yang menonjol ke arah kamera, jadi pada
pemetaan yang BENAR, depth di dalam kotak anotasi harus lebih dekat dan lebih
rapat daripada cincin latar di sekelilingnya. Pemetaan yang meleset 30-60 px
akan mencampur tandan dengan latar dan memperkecil separasi itu.

Kandidat:
  H1 = resize langsung 848x480 -> 1280x800 (yang diasumsikan sidecar & prepare_depth.py)
  H2 = affine dari intrinsik saja (abaikan ekstrinsik + distorsi)
  H3 = reproyeksi penuh (intrinsik + ekstrinsik + distorsi Brown-Conrady K6)

Uji tambahan: sapuan pergeseran global (dx,dy) pada H3. Kalau H3 benar,
skor harus memuncak di (0,0); kalau depth sebenarnya sudah D2C, puncaknya akan
bergeser ke arah selisih H1-H3.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np

from depth_calib import (RGB_H, RGB_W, Kalibrasi, baca_depth_mm, baca_kalibrasi,
                         reproyeksi, tambal_lubang)

DATA = Path("/workspace/SawitMVC-Depth/data")


def peta_h1(z_mm: np.ndarray, kal: Kalibrasi) -> np.ndarray:
    """Resize langsung — NEAREST supaya piksel invalid 0 tidak tercampur."""
    return cv2.resize(z_mm, (RGB_W, RGB_H), interpolation=cv2.INTER_NEAREST)


def peta_h2(z_mm: np.ndarray, kal: Kalibrasi) -> np.ndarray:
    """Affine dari intrinsik saja: skala seragam fx_c/fx_d, tanpa parallax/distorsi."""
    return reproyeksi(z_mm, kal, distorsi=False, ekstrinsik=False)


def peta_h3(z_mm: np.ndarray, kal: Kalibrasi) -> np.ndarray:
    return reproyeksi(z_mm, kal, distorsi=True, ekstrinsik=True)


KANDIDAT = {"H1_resize": peta_h1, "H2_affine": peta_h2, "H3_reproyeksi": peta_h3}


def kotak_piksel(label: Path) -> list[tuple[int, int, int, int]]:
    kotak = []
    for baris in label.read_text().split("\n"):
        if not baris.strip():
            continue
        _, xc, yc, w, h = (float(x) for x in baris.split())
        x1 = int((xc - w / 2) * RGB_W)
        x2 = int((xc + w / 2) * RGB_W)
        y1 = int((yc - h / 2) * RGB_H)
        y2 = int((yc + h / 2) * RGB_H)
        kotak.append((max(0, x1), max(0, y1), min(RGB_W, x2), min(RGB_H, y2)))
    return kotak


def skor_peta(peta: np.ndarray, kotak: list[tuple[int, int, int, int]],
              geser: tuple[int, int] = (0, 0)) -> list[dict]:
    """Untuk tiap kotak: bandingkan depth di dalam kotak vs cincin di sekitarnya."""
    dx, dy = geser
    hasil = []
    for x1, y1, x2, y2 in kotak:
        x1, x2 = x1 + dx, x2 + dx
        y1, y2 = y1 + dy, y2 + dy
        if x1 < 0 or y1 < 0 or x2 > RGB_W or y2 > RGB_H or x2 <= x1 or y2 <= y1:
            continue
        w, h = x2 - x1, y2 - y1
        m = max(8, int(0.5 * min(w, h)))
        rx1, ry1 = max(0, x1 - m), max(0, y1 - m)
        rx2, ry2 = min(RGB_W, x2 + m), min(RGB_H, y2 + m)

        dalam = peta[y1:y2, x1:x2]
        dalam = dalam[dalam > 0]
        luar_kotak = peta[ry1:ry2, rx1:rx2].copy()
        luar_kotak[y1 - ry1:y2 - ry1, x1 - rx1:x2 - rx1] = 0
        cincin = luar_kotak[luar_kotak > 0]

        if dalam.size < 30 or cincin.size < 30:
            continue
        hasil.append({
            "med_dalam": float(np.median(dalam)),
            "med_cincin": float(np.median(cincin)),
            "iqr_dalam": float(np.subtract(*np.percentile(dalam, [75, 25]))),
            "valid_dalam": float(dalam.size / (w * h)),
        })
    return hasil


def ringkas(catatan: list[dict]) -> dict:
    if not catatan:
        return {}
    d = np.array([c["med_dalam"] for c in catatan])
    r = np.array([c["med_cincin"] for c in catatan])
    return {
        "n_kotak": len(catatan),
        # separasi relatif: cincin lebih jauh daripada tandan -> positif
        "separasi_rel": float(np.median((r - d) / np.maximum(r, 1.0))),
        "frac_tandan_lebih_dekat": float(np.mean(d < r)),
        "med_iqr_dalam_mm": float(np.median([c["iqr_dalam"] for c in catatan])),
        "med_valid_dalam": float(np.median([c["valid_dalam"] for c in catatan])),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200, help="jumlah citra bersampel")
    ap.add_argument("--geser", action="store_true", help="jalankan sapuan pergeseran pada H3")
    ap.add_argument("--keluaran", default="results/e022_align.json")
    args = ap.parse_args()

    label_ada = sorted(p for p in (DATA / "labels").glob("*.txt") if p.stat().st_size > 0)
    rng = np.random.default_rng(42)
    pilih = [label_ada[i] for i in rng.choice(len(label_ada), min(args.n, len(label_ada)), replace=False)]

    catatan: dict[str, list[dict]] = {k: [] for k in KANDIDAT}
    geser_skor: dict[str, list[dict]] = {}

    for i, lab in enumerate(pilih):
        stem = lab.stem
        raw = DATA / "depth" / f"{stem}.raw"
        side = DATA / "depth" / f"{stem}.json"
        if not raw.is_file():
            continue
        z = baca_depth_mm(raw)
        kal = baca_kalibrasi(side)
        kotak = kotak_piksel(lab)
        if not kotak:
            continue
        for nama, fn in KANDIDAT.items():
            peta = fn(z, kal)
            if nama != "H1_resize":
                peta = tambal_lubang(peta)
            catatan[nama].extend(skor_peta(peta, kotak))
            if args.geser and nama == "H3_reproyeksi":
                for dx in (-40, -20, -10, 0, 10, 20, 40):
                    for dy in (-40, -20, -10, 0, 10, 20, 40):
                        geser_skor.setdefault(f"{dx},{dy}", []).extend(
                            skor_peta(peta, kotak, (dx, dy)))
        if (i + 1) % 25 == 0:
            print(f"  {i + 1}/{len(pilih)} citra")

    hasil = {"n_citra": len(pilih), "kandidat": {k: ringkas(v) for k, v in catatan.items()}}
    if geser_skor:
        hasil["sapuan_geser_h3"] = {k: ringkas(v) for k, v in geser_skor.items()}

    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hasil, indent=2))

    print(f"\n{'kandidat':16s} {'n':>6s} {'separasi_rel':>13s} {'tandan<cincin':>14s} {'IQR dalam (mm)':>15s} {'valid dalam':>12s}")
    for k, v in hasil["kandidat"].items():
        if v:
            print(f"{k:16s} {v['n_kotak']:6d} {v['separasi_rel']:13.4f} "
                  f"{v['frac_tandan_lebih_dekat']:14.3f} {v['med_iqr_dalam_mm']:15.1f} {v['med_valid_dalam']:12.3f}")
    if geser_skor:
        urut = sorted(hasil["sapuan_geser_h3"].items(),
                      key=lambda kv: -kv[1].get("separasi_rel", -9))
        print("\n5 pergeseran terbaik pada H3 (dx,dy -> separasi_rel):")
        for k, v in urut[:5]:
            print(f"  ({k}) {v['separasi_rel']:.4f}  n={v['n_kotak']}")
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
