#!/usr/bin/env python3
"""E-009 — Seberapa kecil tandan setelah citra diperkecil? (ide I-11/I-12)

Alasan: B4 adalah kelas terburuk (AP50 0,354). Hipotesis I-12 mengatakan
penyebabnya sebagian adalah resolusi -- pada `imgsz=640`, citra 960x1280
diperkecil 2x, sehingga tandan kecil kehilangan piksel sebelum masuk jaringan.

Uji ini tidak melibatkan model sama sekali; ia hanya mengukur geometri kotak
kebenaran-dasar. Kalau B4 ternyata tidak lebih kecil daripada kelas lain,
dasar pemikiran I-12 runtuh sebelum satu jam GPU pun dibakar.

Konvensi COCO dipakai sebagai acuan yang dikenal luas:
  kecil   : luas < 32^2 px   (32x32)
  sedang  : 32^2 .. 96^2 px
  besar   : > 96^2 px

Pemakaian:  python box_size_analysis.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np

SRC = Path("/workspace/SawitMVC/data")
CLASSES = ["B1", "B2", "B3", "B4"]
W0, H0 = 960, 1280
IMGSZ = 640


def main() -> int:
    # skala ultralytics: sisi terpanjang -> imgsz
    scale = IMGSZ / max(W0, H0)
    Ws, Hs = W0 * scale, H0 * scale

    per_cls = defaultdict(list)
    names = [Path(l).stem for l in (SRC / "test.txt").read_text().split() if l.strip()]
    names += [Path(l).stem for l in (SRC / "train.txt").read_text().split() if l.strip()]

    for stem in names:
        f = SRC / "labels" / f"{stem}.txt"
        if not f.exists():
            continue
        for line in f.read_text().strip().splitlines():
            p = line.split()
            if len(p) < 5:
                continue
            c = int(p[0]); w = float(p[3]); h = float(p[4])
            per_cls[CLASSES[c]].append((w * Ws, h * Hs))

    W = 76
    print("=" * W)
    print(f"E-009 — UKURAN KOTAK PADA imgsz={IMGSZ} (sumber {W0}x{H0}, skala {scale:.2f})")
    print("=" * W)
    print(f"  {'kelas':6s} {'n':>7s} {'lebar':>8s} {'tinggi':>8s} {'luas px':>10s} "
          f"{'%kecil':>8s} {'%sedang':>8s} {'%besar':>7s}")

    out = {}
    for c in CLASSES:
        a = np.array(per_cls[c])
        if not len(a):
            continue
        area = a[:, 0] * a[:, 1]
        small = float((area < 32 ** 2).mean() * 100)
        med = float(((area >= 32 ** 2) & (area < 96 ** 2)).mean() * 100)
        large = float((area >= 96 ** 2).mean() * 100)
        print(f"  {c:6s} {len(a):7d} {np.median(a[:,0]):8.1f} {np.median(a[:,1]):8.1f} "
              f"{np.median(area):10.0f} {small:7.1f}% {med:7.1f}% {large:6.1f}%")
        out[c] = {"n": len(a), "median_w": float(np.median(a[:, 0])),
                  "median_h": float(np.median(a[:, 1])),
                  "median_area": float(np.median(area)),
                  "pct_small": small, "pct_medium": med, "pct_large": large,
                  "p10_area": float(np.percentile(area, 10))}

    print(f"\n  Ambang COCO: kecil < 32x32=1024 px, sedang < 96x96=9216 px")
    print("\n  Efek ubin 2x2 (setiap sisi ubin ~2x lebih besar pada imgsz sama):")
    print(f"  {'kelas':6s} {'luas kini':>11s} {'luas ubin':>11s} {'%kecil kini':>12s} {'%kecil ubin':>12s}")
    for c in CLASSES:
        a = np.array(per_cls[c])
        if not len(a):
            continue
        area = a[:, 0] * a[:, 1]
        area_t = area * 4.0            # 2x per sisi -> 4x luas
        print(f"  {c:6s} {np.median(area):11.0f} {np.median(area_t):11.0f} "
              f"{(area < 32**2).mean()*100:11.1f}% {(area_t < 32**2).mean()*100:11.1f}%")
        out[c]["pct_small_tiled"] = float((area_t < 32 ** 2).mean() * 100)

    p = Path("/workspace/experiments/results/e009")
    p.mkdir(parents=True, exist_ok=True)
    (p / "box_sizes.json").write_text(json.dumps(out, indent=1))
    print(f"\nlaporan -> {p / 'box_sizes.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
