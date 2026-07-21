#!/usr/bin/env python3
"""E-006 — Apakah kedalaman membawa sinyal di tingkat TANDAN? (ide I-9)

Ini penentu. E-005 membuktikan DA3 memulihkan geometri tingkat-pohon, tetapi
inspeksi visual menunjukkan area mahkota tampak menyatu. Kalau kedalaman tidak
membedakan tandan dari sekitarnya, maka fusi depth tidak akan menolong B4
berapa pun arsitekturnya -- dan itu harus diketahui SEBELUM jam GPU dibakar
untuk pelatihan.

Rancangan: untuk setiap kotak tandan kebenaran-dasar, bandingkan statistik
kedalaman di DALAM kotak terhadap CINCIN di sekelilingnya. Sebagai kendali,
lakukan hal yang sama pada kotak acak berukuran sama di posisi acak pada citra
yang sama. Kalau kotak tandan asli menunjukkan kontras kedalaman yang lebih
besar daripada kotak acak, kedalaman membawa sinyal tandan.

Kendali ini penting: peta kedalaman apa pun punya gradien (atas jauh, bawah
dekat), sehingga kotak mana pun akan menunjukkan "kontras" tertentu. Yang
bermakna adalah SELISIH terhadap kendali, bukan angka mentahnya.

Metrik:
  contrast   = |median_dalam - median_cincin| / rentang kedalaman citra
  cohen_d    = beda rata-rata dibagi simpangan baku gabungan (ukuran efek)
  auc        = peluang piksel dalam-kotak acak lebih dekat daripada piksel cincin
               (0,5 = tidak informatif)

Pemakaian:
  python depth_bunch_signal.py --trees 40
  python depth_bunch_signal.py --trees 40 --process-res 1008
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

IMAGES = Path("/workspace/SawitMVC/data/images")
LABELS = Path("/workspace/SawitMVC/data/labels")
OUT_DIR = Path("/workspace/experiments/results/e006")
CLASS_NAMES = ["B1", "B2", "B3", "B4"]


def group_by_tree(images: Path) -> dict[str, list[Path]]:
    by = defaultdict(list)
    for p in sorted(images.glob("*.jpg")):
        m = re.match(r"^(.*)_(\d+)$", p.stem)
        if m:
            by[m.group(1)].append(p)
    for t in by:
        by[t].sort(key=lambda q: int(re.match(r"^.*_(\d+)$", q.stem).group(1)))
    return by


def load_boxes(stem: str) -> list[tuple[int, float, float, float, float]]:
    f = LABELS / f"{stem}.txt"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().strip().splitlines():
        parts = line.split()
        if len(parts) >= 5:
            out.append((int(parts[0]), *map(float, parts[1:5])))
    return out


def box_to_pixels(b, W, H, pad=0.0):
    _, cx, cy, w, h = b
    w2, h2 = w * (1 + pad) / 2, h * (1 + pad) / 2
    x0 = int(max(0, (cx - w2) * W)); x1 = int(min(W, (cx + w2) * W))
    y0 = int(max(0, (cy - h2) * H)); y1 = int(min(H, (cy + h2) * H))
    return x0, y0, x1, y1


def analyse_box(depth: np.ndarray, box_px, ring_scale: float) -> dict | None:
    """Kontras kedalaman antara isi kotak dan cincin di sekelilingnya."""
    H, W = depth.shape
    x0, y0, x1, y1 = box_px
    if x1 - x0 < 3 or y1 - y0 < 3:
        return None
    inner = depth[y0:y1, x0:x1].ravel()

    bw, bh = x1 - x0, y1 - y0
    ex, ey = int(bw * (ring_scale - 1) / 2), int(bh * (ring_scale - 1) / 2)
    X0, Y0 = max(0, x0 - ex), max(0, y0 - ey)
    X1, Y1 = min(W, x1 + ex), min(H, y1 + ey)
    outer = depth[Y0:Y1, X0:X1]
    mask = np.ones(outer.shape, bool)
    mask[y0 - Y0: y1 - Y0, x0 - X0: x1 - X0] = False
    ring = outer[mask].ravel()

    inner = inner[np.isfinite(inner)]
    ring = ring[np.isfinite(ring)]
    if inner.size < 9 or ring.size < 9:
        return None

    rng_img = float(np.nanpercentile(depth, 99) - np.nanpercentile(depth, 1))
    if rng_img <= 0:
        return None

    mi, mr = float(np.median(inner)), float(np.median(ring))
    si, sr = float(inner.std()), float(ring.std())
    pooled = np.sqrt((si ** 2 + sr ** 2) / 2) or 1e-9

    # AUC lewat statistik-U Mann-Whitney (disubsampel agar murah)
    a = inner if inner.size <= 4000 else np.random.default_rng(0).choice(inner, 4000, replace=False)
    b = ring if ring.size <= 4000 else np.random.default_rng(1).choice(ring, 4000, replace=False)
    conc = np.concatenate([a, b])
    ranks = conc.argsort().argsort().astype(np.float64) + 1
    ra = ranks[: len(a)].sum()
    auc = (ra - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))

    return {
        "contrast": abs(mi - mr) / rng_img,
        "signed_contrast": (mi - mr) / rng_img,
        "cohen_d": (mi - mr) / pooled,
        "auc": float(max(auc, 1 - auc)),
        "px": int(bw * bh),
        "inner_std_rel": si / rng_img,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trees", type=int, default=40)
    ap.add_argument("--ckpt", default="depth-anything/da3-large")
    ap.add_argument("--process-res", type=int, default=504)
    ap.add_argument("--ring-scale", type=float, default=2.0)
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    by_tree = group_by_tree(IMAGES)
    trees = [t for t, ps in by_tree.items() if len(ps) == 4]
    random.Random(args.seed).shuffle(trees)
    trees = trees[: args.trees]

    import torch
    from depth_anything_3.api import DepthAnything3
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = DepthAnything3.from_pretrained(args.ckpt).to(device=dev).eval()

    import cv2
    rng = np.random.default_rng(args.seed)
    real = defaultdict(list)
    ctrl = defaultdict(list)
    per_class = defaultdict(lambda: defaultdict(list))
    n_boxes = 0

    print(f"pohon diuji: {len(trees)}  process_res={args.process_res}\n")
    for i, t in enumerate(trees):
        paths = by_tree[t]
        with torch.inference_mode():
            pred = model.inference([str(p) for p in paths], process_res=args.process_res)
        depths = np.asarray(pred.depth)

        for k, p in enumerate(paths):
            boxes = load_boxes(p.stem)
            if not boxes:
                continue
            im = cv2.imread(str(p))
            H0, W0 = im.shape[:2]
            d = depths[k]
            # peta kedalaman beresolusi lebih rendah: skala kotak ke ukuran peta
            Hd, Wd = d.shape
            for b in boxes:
                bp = box_to_pixels(b, Wd, Hd)
                r = analyse_box(d, bp, args.ring_scale)
                if r is None:
                    continue
                n_boxes += 1
                for key in ("contrast", "cohen_d", "auc"):
                    real[key].append(r[key])
                    per_class[CLASS_NAMES[b[0]]][key].append(r[key])
                per_class[CLASS_NAMES[b[0]]]["px"].append(r["px"])

                # kendali: kotak berukuran sama di posisi acak
                bw, bh = bp[2] - bp[0], bp[3] - bp[1]
                for _ in range(2):
                    x0 = int(rng.integers(0, max(1, Wd - bw)))
                    y0 = int(rng.integers(0, max(1, Hd - bh)))
                    rc = analyse_box(d, (x0, y0, x0 + bw, y0 + bh), args.ring_scale)
                    if rc:
                        for key in ("contrast", "cohen_d", "auc"):
                            ctrl[key].append(rc[key])

        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(trees)} pohon, {n_boxes} kotak")

    W = 74
    print("\n" + "=" * W)
    print(f"E-006 — SINYAL KEDALAMAN TINGKAT TANDAN ({n_boxes} kotak, "
          f"process_res={args.process_res})")
    print("=" * W)

    def summ(name, dct):
        c = np.array(dct["contrast"]); a = np.array(dct["auc"]); cd = np.abs(dct["cohen_d"])
        print(f"  {name:22s} kontras={c.mean():.4f}  AUC={a.mean():.4f}  |d|={cd.mean():.3f}  n={len(c)}")
        return c, a

    cr, ar = summ("kotak tandan asli", real)
    cc, ac = summ("kotak acak (kendali)", ctrl)

    print("\n  SELISIH terhadap kendali (inilah yang bermakna):")
    print(f"    kontras : {cr.mean() - cc.mean():+.4f}  "
          f"(rasio {cr.mean()/cc.mean():.2f}x)")
    print(f"    AUC     : {ar.mean() - ac.mean():+.4f}")

    # uji permutasi sederhana pada selisih rata-rata AUC
    both = np.concatenate([ar, ac])
    n1 = len(ar)
    obs = ar.mean() - ac.mean()
    perm = np.array([
        (lambda s: s[:n1].mean() - s[n1:].mean())(rng.permutation(both))
        for _ in range(2000)
    ])
    p = float((np.abs(perm) >= abs(obs)).mean())
    print(f"    uji permutasi AUC: p = {p:.4f} ({2000} permutasi)")

    print("\n  PER KELAS (kotak tandan asli):")
    print(f"    {'kelas':6s} {'kontras':>9s} {'AUC':>8s} {'|d|':>7s} {'piksel median':>14s} {'n':>6s}")
    for c in CLASS_NAMES:
        if not per_class[c]["contrast"]:
            continue
        v = per_class[c]
        print(f"    {c:6s} {np.mean(v['contrast']):9.4f} {np.mean(v['auc']):8.4f} "
              f"{np.mean(np.abs(v['cohen_d'])):7.3f} {np.median(v['px']):14.0f} "
              f"{len(v['contrast']):6d}")

    args.out.mkdir(parents=True, exist_ok=True)
    out = {
        "process_res": args.process_res, "trees": len(trees), "boxes": n_boxes,
        "real": {k: float(np.mean(v)) for k, v in real.items()},
        "control": {k: float(np.mean(v)) for k, v in ctrl.items()},
        "auc_perm_p": p,
        "per_class": {c: {k: float(np.mean(v)) for k, v in d.items()}
                      for c, d in per_class.items()},
    }
    fp = args.out / f"report_res{args.process_res}.json"
    fp.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nlaporan -> {fp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
