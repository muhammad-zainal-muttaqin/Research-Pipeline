#!/usr/bin/env python3
"""Konversi peta kedalaman mentah -> PNG kanonik uint8 untuk pipeline 4-kanal.

Dua sumber yang didukung:

  --mode gemini   : PNG/berkas uint16 dalam MILIMETER dari sensor (Orbbec
                    Gemini dan sejenisnya). Dipetakan ke inverse-depth pada
                    rentang metrik tetap [0,3 m, 8 m]; piksel 0 (lubang
                    sensor) tetap 0 = tidak valid. INI MODE PRODUKSI.

  --mode relative : peta relatif (Depth Anything dsb., uint8/uint16 apa pun).
                    Disebar per-citra ke 1..255. HANYA untuk pralatihan dengan
                    pseudo-depth — skala absolutnya tidak berarti, jadi model
                    yang dilatih dengannya perlu dilatih ulang / disetel-halus
                    begitu data sensor asli tersedia.

Syarat: peta kedalaman sudah SEJAJAR (registered) ke RGB — pakai fitur
alignment SDK sensor (depth-to-color). Ukuran boleh beda; pipeline akan
me-resize nearest-neighbor saat memuat.

Contoh:
  python prepare_depth.py --src depth_mentah/ --dst depth_kanonik/ --mode gemini
"""
from __future__ import annotations

import argparse
from pathlib import Path

import cv2

import fourch


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="folder peta kedalaman mentah")
    ap.add_argument("--dst", required=True, help="folder keluaran PNG kanonik")
    ap.add_argument("--mode", choices=["gemini", "relative"], required=True)
    args = ap.parse_args()

    src, dst = Path(args.src), Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in src.iterdir()
                   if p.suffix.lower() in (".png", ".tif", ".tiff"))
    n = bad = 0
    for p in files:
        d = cv2.imread(str(p), cv2.IMREAD_UNCHANGED)
        if d is None:
            bad += 1
            continue
        if d.ndim == 3:
            d = d[:, :, 0]
        if args.mode == "gemini":
            out = fourch.encode_metric_depth(d)
        else:
            out = fourch.encode_relative_depth(d)
        cv2.imwrite(str(dst / f"{p.stem}.png"), out)
        n += 1
    print(f"selesai: {n} dikonversi, {bad} gagal dibaca -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
