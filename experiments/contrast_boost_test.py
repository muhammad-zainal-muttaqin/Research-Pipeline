#!/usr/bin/env python3
"""E-011 — Bisakah praproses menaikkan keterpisahan B4? (ide I-20)

SR-007 menemukan B4 tersamar: kontras dE 11,55, DI BAWAH kendali kotak acak
(12,92). Satu-satunya sinyal tersisa adalah tekstur, di mana B4 justru
tertinggi (7.780).

Kalau begitu, praproses yang memperkuat kontras lokal atau tekstur seharusnya
menaikkan keterpisahan B4. Uji ini mengukurnya LANGSUNG pada kotak
kebenaran-dasar, sebelum satu jam GPU pun dibakar -- disiplin yang sama seperti
E-006 dan E-010.

Kandidat praproses:
  asli      : tanpa perlakuan (acuan)
  clahe     : CLAHE pada kanal L (kontras lokal adaptif)
  unsharp   : unsharp mask (menonjolkan frekuensi tinggi)
  gradmag   : besar gradien Sobel (kanal tekstur murni)
  laplacian : respons Laplacian (frekuensi tinggi murni)

Metrik: AUC pemisahan piksel isi-kotak vs cincin (0,5 = tidak informatif),
dihitung per kelas, plus kendali kotak acak untuk tiap praproses. Yang bermakna
adalah SELISIH terhadap kendali, bukan AUC mentahnya.

Pemakaian:  python contrast_boost_test.py --images 250
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


# --------------------------------------------------------------------------
def prep_variants(bgr: np.ndarray) -> dict[str, np.ndarray]:
    """Hasilkan peta skalar (1 kanal) yang akan diuji keterpisahannya."""
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    L_cl = clahe.apply(lab[:, :, 0])

    blur = cv2.GaussianBlur(gray, (0, 0), 3)
    unsharp = cv2.addWeighted(gray, 1.8, blur, -0.8, 0)

    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    grad = cv2.magnitude(gx, gy)
    # haluskan sedikit supaya yang diukur adalah energi tekstur lokal,
    # bukan derau piksel tunggal
    grad = cv2.GaussianBlur(grad, (0, 0), 2)

    lap = np.abs(cv2.Laplacian(gray, cv2.CV_32F, ksize=3))
    lap = cv2.GaussianBlur(lap, (0, 0), 2)

    return {
        "asli": lab[:, :, 0].astype(np.float32),
        "clahe": L_cl.astype(np.float32),
        "unsharp": unsharp.astype(np.float32),
        "gradmag": grad,
        "laplacian": lap,
    }


def auc_inner_vs_ring(m: np.ndarray, box, ring_scale=2.0) -> float | None:
    H, W = m.shape
    x0, y0, x1, y1 = box
    if x1 - x0 < 4 or y1 - y0 < 4:
        return None
    inner = m[y0:y1, x0:x1].ravel()
    bw, bh = x1 - x0, y1 - y0
    ex, ey = int(bw * (ring_scale - 1) / 2), int(bh * (ring_scale - 1) / 2)
    X0, Y0 = max(0, x0 - ex), max(0, y0 - ey)
    X1, Y1 = min(W, x1 + ex), min(H, y1 + ey)
    outer = m[Y0:Y1, X0:X1]
    mask = np.ones(outer.shape, bool)
    mask[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = False
    ring = outer[mask].ravel()
    if inner.size < 9 or ring.size < 9:
        return None
    rng = np.random.default_rng(0)
    a = inner if inner.size <= 3000 else rng.choice(inner, 3000, replace=False)
    b = ring if ring.size <= 3000 else rng.choice(ring, 3000, replace=False)
    conc = np.concatenate([a, b])
    ranks = conc.argsort().argsort().astype(np.float64) + 1
    ra = ranks[: len(a)].sum()
    auc = (ra - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))
    return float(max(auc, 1 - auc))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=int, default=250)
    args = ap.parse_args()

    names = [Path(l).stem for l in (SRC / "test.txt").read_text().split() if l.strip()]
    names = names[: args.images]
    rng = np.random.default_rng(42)

    real = defaultdict(lambda: defaultdict(list))   # [varian][kelas]
    ctrl = defaultdict(list)                        # [varian]

    for stem in names:
        bgr = cv2.imread(str(SRC / "images" / f"{stem}.jpg"))
        if bgr is None:
            continue
        H, W = bgr.shape[:2]
        maps = prep_variants(bgr)
        boxes = load_boxes(stem)
        for c, cx, cy, bw, bh in boxes:
            box = (int((cx-bw/2)*W), int((cy-bh/2)*H),
                   int((cx+bw/2)*W), int((cy+bh/2)*H))
            for name, m in maps.items():
                a = auc_inner_vs_ring(m, box)
                if a is not None:
                    real[name][CLASSES[c]].append(a)
            pw, ph = box[2]-box[0], box[3]-box[1]
            rx = int(rng.integers(0, max(1, W-pw))); ry = int(rng.integers(0, max(1, H-ph)))
            for name, m in maps.items():
                a = auc_inner_vs_ring(m, (rx, ry, rx+pw, ry+ph))
                if a is not None:
                    ctrl[name].append(a)

    W_ = 80
    print("=" * W_)
    print(f"E-011 — KETERPISAHAN SETELAH PRAPROSES ({len(names)} citra)")
    print("=" * W_)
    print("AUC isi-kotak vs cincin; 0,5 = tidak informatif")
    print("Yang bermakna: selisih terhadap kendali kotak acak\n")
    hdr = f"  {'praproses':11s}" + "".join(f"{c:>9s}" for c in CLASSES) + f"{'kendali':>10s}{'B4-kendali':>12s}"
    print(hdr)
    out = {}
    rows = []
    for name in ("asli", "clahe", "unsharp", "gradmag", "laplacian"):
        vals = [np.mean(real[name][c]) if real[name][c] else float("nan") for c in CLASSES]
        cv_ = np.mean(ctrl[name]) if ctrl[name] else float("nan")
        d = vals[3] - cv_
        print(f"  {name:11s}" + "".join(f"{v:9.4f}" for v in vals) +
              f"{cv_:10.4f}{d:+12.4f}")
        out[name] = {"per_class": {c: float(v) for c, v in zip(CLASSES, vals)},
                     "control": float(cv_), "b4_minus_control": float(d)}
        rows.append((name, d))

    best = max(rows, key=lambda r: r[1])
    base = dict(rows)["asli"]
    print(f"\n  Acuan 'asli' (B4 - kendali) : {base:+.4f}")
    print(f"  Praproses terbaik untuk B4  : {best[0]} ({best[1]:+.4f}, "
          f"perbaikan {best[1]-base:+.4f})")
    if best[1] - base < 0.02:
        print("\n  CATATAN: perbaikan di bawah 0,02 AUC tergolong dapat diabaikan.")
        print("  Praproses semacam ini kemungkinan TIDAK akan menolong B4.")

    p = Path("/workspace/experiments/results/e011")
    p.mkdir(parents=True, exist_ok=True)
    (p / "contrast_boost.json").write_text(json.dumps(out, indent=1))
    print(f"\nlaporan -> {p / 'contrast_boost.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
