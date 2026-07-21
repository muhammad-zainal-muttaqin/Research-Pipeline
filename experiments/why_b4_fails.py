#!/usr/bin/env python3
"""E-010 — Kenapa B4 gagal? Diagnosis penyebab, bukan tebakan. (ide I-11)

E-009 menunjukkan ukuran hanya sebagian penjelasan (B4 median 46x46 px, 81%
masih "sedang"). Uji ini mengukur tiga tersangka lain secara langsung pada
kotak kebenaran-dasar, tanpa melibatkan model:

  1. KONTRAS FOTOMETRIK  -- seberapa beda tandan dari sekelilingnya secara
     warna/terang? Hipotesis: B4 gelap di latar pelepah yang juga gelap.
  2. KEPADATAN (crowding) -- berapa banyak tandan lain berdekatan? Objek rapat
     memicu penggabungan/pemecahan instans.
  3. TUMPANG TINDIH       -- berapa besar IoU dengan kotak tetangga terdekat?

Sama seperti E-006, dipakai KENDALI kotak acak berukuran sama, karena kotak apa
pun pada citra kanopi akan menunjukkan kontras tertentu.

Pemakaian:  python why_b4_fails.py --images 400
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
CLASSES = ["B1", "B2", "B3", "B4"]


def load_boxes(stem: str):
    f = SRC / "labels" / f"{stem}.txt"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().strip().splitlines():
        p = line.split()
        if len(p) >= 5:
            out.append([int(p[0])] + [float(v) for v in p[1:5]])
    return out


def ring_stats(img: np.ndarray, box, ring_scale=2.0):
    """Kontras isi kotak vs cincin sekelilingnya, pada kanal terang dan warna."""
    H, W = img.shape[:2]
    x0, y0, x1, y1 = box
    if x1 - x0 < 4 or y1 - y0 < 4:
        return None
    inner = img[y0:y1, x0:x1]
    bw, bh = x1 - x0, y1 - y0
    ex, ey = int(bw * (ring_scale - 1) / 2), int(bh * (ring_scale - 1) / 2)
    X0, Y0 = max(0, x0 - ex), max(0, y0 - ey)
    X1, Y1 = min(W, x1 + ex), min(H, y1 + ey)
    outer = img[Y0:Y1, X0:X1]
    mask = np.ones(outer.shape[:2], bool)
    mask[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = False
    if mask.sum() < 20 or inner.size == 0:
        return None
    lab_i = cv2.cvtColor(inner, cv2.COLOR_BGR2LAB).reshape(-1, 3).astype(np.float32)
    lab_o = cv2.cvtColor(outer, cv2.COLOR_BGR2LAB)[mask].astype(np.float32)
    dL = abs(lab_i[:, 0].mean() - lab_o[:, 0].mean())
    dab = float(np.linalg.norm(lab_i[:, 1:].mean(0) - lab_o[:, 1:].mean(0)))
    de = float(np.linalg.norm(lab_i.mean(0) - lab_o.mean(0)))
    return {"dL": float(dL), "dab": dab, "deltaE": de,
            "L_in": float(lab_i[:, 0].mean()),
            "texture": float(cv2.Laplacian(
                cv2.cvtColor(inner, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var())}


def iou(a, b):
    ix0, iy0 = max(a[0], b[0]), max(a[1], b[1])
    ix1, iy1 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix1 - ix0) * max(0, iy1 - iy0)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / (ua + 1e-9)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=int, default=400)
    args = ap.parse_args()

    names = [Path(l).stem for l in (SRC / "test.txt").read_text().split() if l.strip()]
    names = names[: args.images]
    rng = np.random.default_rng(42)

    real = defaultdict(lambda: defaultdict(list))
    ctrl = defaultdict(list)

    for stem in names:
        im = cv2.imread(str(SRC / "images" / f"{stem}.jpg"))
        if im is None:
            continue
        H, W = im.shape[:2]
        boxes = load_boxes(stem)
        px = [[c, int((cx-bw/2)*W), int((cy-bh/2)*H), int((cx+bw/2)*W), int((cy+bh/2)*H)]
              for c, cx, cy, bw, bh in boxes]

        for i, (c, x0, y0, x1, y1) in enumerate(px):
            s = ring_stats(im, (x0, y0, x1, y1))
            if s is None:
                continue
            cn = CLASSES[c]
            for k, v in s.items():
                real[cn][k].append(v)

            # kepadatan: jumlah kotak lain yang pusatnya dalam radius 1,5x diagonal
            cxp, cyp = (x0+x1)/2, (y0+y1)/2
            diag = np.hypot(x1-x0, y1-y0)
            near = sum(1 for j, (c2, a0, b0, a1, b1) in enumerate(px) if j != i and
                       np.hypot((a0+a1)/2 - cxp, (b0+b1)/2 - cyp) < 1.5 * diag)
            real[cn]["neighbours"].append(near)
            best_iou = max([iou((x0, y0, x1, y1), (a0, b0, a1, b1))
                            for j, (c2, a0, b0, a1, b1) in enumerate(px) if j != i] or [0])
            real[cn]["max_iou"].append(best_iou)

            bw2, bh2 = x1-x0, y1-y0
            for _ in range(1):
                rx = int(rng.integers(0, max(1, W-bw2))); ry = int(rng.integers(0, max(1, H-bh2)))
                sc = ring_stats(im, (rx, ry, rx+bw2, ry+bh2))
                if sc:
                    for k, v in sc.items():
                        ctrl[k].append(v)

    W = 78
    print("=" * W)
    print(f"E-010 — DIAGNOSIS KEGAGALAN B4 ({len(names)} citra uji)")
    print("=" * W)
    print("\n1. KONTRAS FOTOMETRIK (kotak vs cincin sekeliling)")
    print(f"  {'kelas':6s} {'dLuminans':>10s} {'dWarna':>9s} {'deltaE':>8s} "
          f"{'terang dlm':>11s} {'tekstur':>9s} {'n':>6s}")
    out = {}
    for c in CLASSES:
        if not real[c]["deltaE"]:
            continue
        r = real[c]
        print(f"  {c:6s} {np.mean(r['dL']):10.2f} {np.mean(r['dab']):9.2f} "
              f"{np.mean(r['deltaE']):8.2f} {np.mean(r['L_in']):11.1f} "
              f"{np.mean(r['texture']):9.1f} {len(r['deltaE']):6d}")
        out[c] = {k: float(np.mean(v)) for k, v in r.items()}
    print(f"  {'acak':6s} {np.mean(ctrl['dL']):10.2f} {np.mean(ctrl['dab']):9.2f} "
          f"{np.mean(ctrl['deltaE']):8.2f} {np.mean(ctrl['L_in']):11.1f} "
          f"{np.mean(ctrl['texture']):9.1f} {len(ctrl['deltaE']):6d}")

    print("\n2. KEPADATAN & TUMPANG TINDIH")
    print(f"  {'kelas':6s} {'tetangga':>9s} {'%>=1 tetangga':>14s} "
          f"{'IoU maks':>9s} {'%IoU>0,1':>10s}")
    for c in CLASSES:
        if not real[c]["neighbours"]:
            continue
        nb = np.array(real[c]["neighbours"]); mi = np.array(real[c]["max_iou"])
        print(f"  {c:6s} {nb.mean():9.2f} {(nb>=1).mean()*100:13.1f}% "
              f"{mi.mean():9.3f} {(mi>0.1).mean()*100:9.1f}%")
        out[c]["pct_with_neighbour"] = float((nb >= 1).mean() * 100)
        out[c]["pct_iou_gt_01"] = float((mi > 0.1).mean() * 100)

    p = Path("/workspace/experiments/results/e010")
    p.mkdir(parents=True, exist_ok=True)
    (p / "why_b4.json").write_text(json.dumps(
        {"per_class": out, "control": {k: float(np.mean(v)) for k, v in ctrl.items()}},
        indent=1))
    print(f"\nlaporan -> {p / 'why_b4.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
