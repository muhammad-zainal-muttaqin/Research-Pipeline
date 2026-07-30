#!/usr/bin/env python3
"""E-022 gerbang: pilih pemetaan depth->RGB lewat mutual information agregat.

Uji berbasis kotak anotasi (verify_depth_align.py) terbukti terlalu lemah:
tandan tidak cukup menonjol dari kanopi dalam ruang kedalaman (separasi relatif
hanya -0,007 s.d. +0,002 untuk ketiga kandidat). Uji ini memakai sinyal yang
jauh lebih kuat: seluruh struktur citra.

Gagasan: pemetaan yang BENAR membuat peta depth sejajar dengan struktur RGB,
sehingga mutual information I(depth; abu-abu RGB) maksimum. Salah registrasi
30-60 px mencampur permukaan berbeda dan menurunkan MI. MI dijumlahkan lintas
banyak citra sebelum dibandingkan (SNR naik ~sqrt(N)).

Kontrol: pergeseran buatan +-24 px pada kandidat terbaik HARUS menurunkan MI.
Kalau tidak turun, metriknya yang gagal — bukan hipotesisnya yang seri.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np

from depth_calib import (RGB_H, RGB_W, baca_depth_mm, baca_kalibrasi,
                         reproyeksi, tambal_lubang)

DATA = Path("/workspace/SawitMVC-Depth/data")
NBIN = 32


def mi(a: np.ndarray, b: np.ndarray, valid: np.ndarray) -> float:
    """Mutual information (bit) antara dua kanal terkuantisasi, piksel valid saja."""
    if valid.sum() < 5000:
        return float("nan")
    x = a[valid].astype(np.int32)
    y = b[valid].astype(np.int32)
    h = np.bincount(x * NBIN + y, minlength=NBIN * NBIN).reshape(NBIN, NBIN).astype(np.float64)
    h /= h.sum()
    px = h.sum(1, keepdims=True)
    py = h.sum(0, keepdims=True)
    nz = h > 0
    return float((h[nz] * np.log2(h[nz] / (px @ py)[nz])).sum())


def kuantisasi(x: np.ndarray, valid: np.ndarray) -> np.ndarray:
    """Kuantisasi ke NBIN level lewat peringkat (tahan outlier)."""
    keluar = np.zeros(x.shape, np.int32)
    v = x[valid]
    if v.size == 0:
        return keluar
    tepi = np.quantile(v, np.linspace(0, 1, NBIN + 1)[1:-1])
    keluar[valid] = np.searchsorted(tepi, v)
    return keluar


def geser(peta: np.ndarray, dx: int, dy: int) -> np.ndarray:
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(peta, M, (RGB_W, RGB_H), flags=cv2.INTER_NEAREST,
                          borderMode=cv2.BORDER_CONSTANT, borderValue=0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=120)
    ap.add_argument("--keluaran", default="results/e022_mi.json")
    args = ap.parse_args()

    semua = sorted((DATA / "depth").glob("*.raw"))
    rng = np.random.default_rng(42)
    pilih = [semua[i] for i in rng.choice(len(semua), min(args.n, len(semua)), replace=False)]

    kandidat = ["H1_resize", "H2_affine", "H3_reproyeksi",
                "H3_geser_x+24", "H3_geser_x-24", "H3_geser_y+24", "H3_geser_y-24"]
    skor: dict[str, list[float]] = {k: [] for k in kandidat}

    for i, raw in enumerate(pilih):
        stem = raw.stem
        jpg = DATA / "images" / f"{stem}.jpg"
        if not jpg.is_file():
            continue
        abu = cv2.imread(str(jpg), cv2.IMREAD_GRAYSCALE)
        z = baca_depth_mm(raw)
        kal = baca_kalibrasi(DATA / "depth" / f"{stem}.json")

        peta = {
            "H1_resize": cv2.resize(z, (RGB_W, RGB_H), interpolation=cv2.INTER_NEAREST),
            "H2_affine": tambal_lubang(reproyeksi(z, kal, distorsi=False, ekstrinsik=False)),
            "H3_reproyeksi": tambal_lubang(reproyeksi(z, kal)),
        }
        p3 = peta["H3_reproyeksi"]
        peta["H3_geser_x+24"] = geser(p3, 24, 0)
        peta["H3_geser_x-24"] = geser(p3, -24, 0)
        peta["H3_geser_y+24"] = geser(p3, 0, 24)
        peta["H3_geser_y-24"] = geser(p3, 0, -24)

        for nama, p in peta.items():
            valid = p > 0
            qd = kuantisasi(p, valid)
            qa = kuantisasi(abu.astype(np.float32), valid)
            skor[nama].append(mi(qd, qa, valid))

        if (i + 1) % 20 == 0:
            print(f"  {i + 1}/{len(pilih)}")

    hasil = {"n_citra": len(pilih), "nbin": NBIN,
             "mi_rerata_bit": {k: float(np.nanmean(v)) for k, v in skor.items()},
             "mi_sd": {k: float(np.nanstd(v)) for k, v in skor.items()},
             "n_valid": {k: int(np.sum(~np.isnan(v))) for k, v in skor.items()},
             "per_citra": {k: [float(x) for x in v] for k, v in skor.items()}}

    # uji berpasangan H3 vs H1 (bootstrap per citra, B=2000, seed 42) — pasangan
    # per citra, bukan antar sampel bebas, karena keduanya diukur pada citra sama
    a = np.array(skor["H3_reproyeksi"])
    b = np.array(skor["H1_resize"])
    ok = ~(np.isnan(a) | np.isnan(b))
    d = a[ok] - b[ok]
    rng_b = np.random.default_rng(42)
    boot = np.array([rng_b.choice(d, d.size, replace=True).mean() for _ in range(2000)])
    hasil["h3_minus_h1"] = {
        "delta_rerata_bit": float(d.mean()),
        "ci95": [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
        "frac_citra_h3_menang": float(np.mean(d > 0)),
        "n_pasangan": int(d.size),
    }

    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hasil, indent=2))

    print(f"\n{'kandidat':16s} {'MI rerata (bit)':>16s} {'sd':>8s}")
    for k in kandidat:
        print(f"{k:16s} {hasil['mi_rerata_bit'][k]:16.4f} {hasil['mi_sd'][k]:8.4f}")
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
