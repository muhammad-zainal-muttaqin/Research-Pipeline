#!/usr/bin/env python3
"""I-6 — Penautan tandan lintas-sisi secara GEOMETRIS (E-007).

Masalah yang diserang: bottleneck counting bukan penghitungnya, melainkan
duplikasi lintas-sisi. Saat ini duplikasi ditangani secara statistik -- dibagi
k = 1,8905, atau ditaksir SVR. Keduanya menebak rata-rata; keduanya tidak tahu
tandan mana yang sama dengan tandan mana.

Ide (naskah §208): kalau pose kamera tersedia, dua deteksi dapat diuji
kesesuaian spasialnya di kerangka koordinat bersama. Tandan fisik yang sama
harus menempati titik 3D yang sama dari sisi mana pun ia dilihat. SR-004 sudah
membuktikan DA3 memulihkan pose 4/8 sisi dengan benar (urutan benar 50/50),
jadi bahan bakunya ada.

Yang dibandingkan -- tangga ablasi §208:
  A. hanya penampilan  : cocokkan berdasarkan kelas + ukuran kotak saja
  B. depth tanpa pose  : cocokkan berdasarkan kedalaman + posisi citra
  C. sadar-pose        : proyeksikan ke 3D memakai pose DA3, lalu cocokkan
  D. koreksi global k  : pembanding publikasi (bagi 1,8905)

Kebenaran acuan: graf `_confirmedLinks` (komponen terhubung = tandan unik).

Yang akan memalsukan ide ini: C tidak lebih baik daripada A/B/D pada galat
hitung maupun mutu penautan.

Pemakaian:
  python geometric_linking.py --trees 141 --split test
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
DEPTH = Path("/workspace/experiments/depth_da3/depth")
CAMS = Path("/workspace/experiments/depth_da3/cameras_all.json")
OUT = Path("/workspace/experiments/results/e007")
CLASSES = ["B1", "B2", "B3", "B4"]
K_GLOBAL = 1.8905


# --------------------------------------------------------------------------
def load_tree_gt(tree: str) -> dict | None:
    f = SRC / "json" / f"{tree}.json"
    if not f.exists():
        return None
    return json.loads(f.read_text(encoding="utf-8-sig"))


def load_boxes(stem: str):
    f = SRC / "labels" / f"{stem}.txt"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().strip().splitlines():
        p = line.split()
        if len(p) >= 5:
            out.append((int(p[0]), float(p[1]), float(p[2]), float(p[3]), float(p[4])))
    return out


def backproject(cx, cy, depth_val, K, E):
    """Piksel + kedalaman -> titik 3D di kerangka dunia.

    E adalah world-to-camera (3,4). Titik kamera Xc = d * K^-1 [u,v,1],
    lalu Xw = R^T (Xc - t).
    """
    uv1 = np.array([cx, cy, 1.0])
    Xc = depth_val * (np.linalg.inv(K) @ uv1)
    R, t = E[:3, :3], E[:3, 3]
    return R.T @ (Xc - t)


def components(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """Komponen terhubung lewat union-find (transitive closure, sama seperti
    cara dataset menurunkan identitas tandan)."""
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            par[ra] = rb
    lab, out = {}, []
    for i in range(n):
        r = find(i)
        if r not in lab:
            lab[r] = len(lab)
        out.append(lab[r])
    return out


# --------------------------------------------------------------------------
def link_tree(tree: str, paths: list[Path], cams: dict, mode: str, thr: float):
    """Kembalikan (jumlah unik per kelas, jumlah deteksi mentah per kelas)."""
    dets = []           # (side, class, cx, cy, w, h, X3d atau None, depth)
    for si, p in enumerate(paths):
        boxes = load_boxes(p.stem)
        if not boxes:
            continue
        dmap = None
        if mode in ("depth", "pose"):
            dp = DEPTH / f"{p.stem}.png"
            if dp.exists():
                dmap = cv2.imread(str(dp), cv2.IMREAD_UNCHANGED).astype(np.float32) / 65535.0

        for (c, cx, cy, w, h) in boxes:
            dv = None
            if dmap is not None:
                H, W = dmap.shape
                x, y = int(cx * W), int(cy * H)
                r = max(2, int(min(w * W, h * H) * 0.25))
                patch = dmap[max(0, y - r):y + r, max(0, x - r):x + r]
                dv = float(np.median(patch)) if patch.size else float(dmap[y, x])
            dets.append({"side": si, "cls": c, "cx": cx, "cy": cy,
                         "w": w, "h": h, "d": dv, "X": None})

    if not dets:
        return np.zeros(4, int), np.zeros(4, int)

    # --- proyeksi 3D untuk mode sadar-pose
    if mode == "pose" and tree in cams:
        cam = cams[tree]
        ext = np.asarray(cam["extrinsics"], dtype=np.float64)
        itr = np.asarray(cam["intrinsics"], dtype=np.float64)
        for d in dets:
            si = d["side"]
            if si >= len(ext) or d["d"] is None:
                continue
            K = itr[si].copy()
            # intrinsik DA3 dinyatakan pada resolusi pemrosesannya; koordinat
            # kotak ternormalisasi sehingga cukup diskalakan ke resolusi itu
            W = K[0, 2] * 2
            H = K[1, 2] * 2
            d["X"] = backproject(d["cx"] * W, d["cy"] * H, d["d"], K, ext[si])

    # --- bangun sisi graf antar-sisi berbeda
    edges = []
    n = len(dets)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = dets[i], dets[j]
            if a["side"] == b["side"]:
                continue                      # satu sisi tidak menaut ke dirinya
            if a["cls"] != b["cls"]:
                continue                      # tandan sama = kelas sama
            if mode == "appearance":
                sim = abs(a["w"] * a["h"] - b["w"] * b["h"]) / max(
                    a["w"] * a["h"], b["w"] * b["h"])
                if sim < thr:
                    edges.append((i, j))
            elif mode == "depth":
                if a["d"] is None or b["d"] is None:
                    continue
                if abs(a["d"] - b["d"]) < thr and abs(a["cy"] - b["cy"]) < 0.15:
                    edges.append((i, j))
            elif mode == "pose":
                if a["X"] is None or b["X"] is None:
                    continue
                if np.linalg.norm(a["X"] - b["X"]) < thr:
                    edges.append((i, j))

    comp = components(n, edges)
    uniq = np.zeros(4, int)
    seen = {}
    for d, c in zip(dets, comp):
        if c not in seen:
            seen[c] = d["cls"]
            uniq[d["cls"]] += 1
    raw = np.zeros(4, int)
    for d in dets:
        raw[d["cls"]] += 1
    return uniq, raw


def metrics(pred: np.ndarray, gt: np.ndarray) -> dict:
    """Metrik yang sama dengan Tabel 4 DiB."""
    diff = pred - gt
    return {
        "class_within1": float((np.abs(diff) <= 1).mean()),
        "tree_within1": float(np.all(np.abs(diff) <= 1, axis=1).mean()),
        "macro_mae": float(np.abs(diff).mean(axis=0).mean()),
        "mean_bias": float(diff.mean(axis=0).mean()),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="test")
    ap.add_argument("--trees", type=int, default=None)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--sweep", action="store_true",
                    help="sapu ambang tiap mode; wajib sebelum memvonis ide ini")
    args = ap.parse_args()

    cams = json.loads(CAMS.read_text())
    by_tree = defaultdict(list)
    for p in sorted((SRC / "images").glob("*.jpg")):
        m = re.match(r"^(.*)_(\d+)$", p.stem)
        by_tree[m.group(1)].append(p)
    for t in by_tree:
        by_tree[t].sort(key=lambda q: int(re.match(r"^.*_(\d+)$", q.stem).group(1)))

    trees = []
    for t in sorted(by_tree):
        g = load_tree_gt(t)
        if g and g.get("split") == args.split:
            trees.append(t)
    if args.trees:
        trees = trees[: args.trees]
    print(f"split={args.split}  pohon={len(trees)}  pohon berpose={sum(t in cams for t in trees)}\n")

    gt_counts, raw_counts = [], []
    preds = {m: [] for m in ("appearance", "depth", "pose")}
    THR = {"appearance": 0.35, "depth": 0.05, "pose": 0.30}

    if args.sweep:
        grids = {
            "appearance": [0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9],
            "depth": [0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8],
            "pose": [0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0],
        }
        gtl = []
        for t in trees:
            g = load_tree_gt(t)
            gtl.append([g["summary"]["by_class"].get(c, 0) for c in CLASSES])
        gt = np.array(gtl)
        print("SAPUAN AMBANG (acuan: koreksi global k = 95,57% Class±1)\n")
        best = {}
        for mode, grid in grids.items():
            print(f"  {mode}:")
            for thr in grid:
                P = np.array([link_tree(t, by_tree[t], cams, mode, thr)[0]
                              for t in trees])
                m = metrics(P, gt)
                star = ""
                if mode not in best or m["class_within1"] > best[mode][1]["class_within1"]:
                    best[mode] = (thr, m)
                    star = "  <-- terbaik sejauh ini"
                print(f"    thr={thr:<6} Class±1={m['class_within1']*100:6.2f}%  "
                      f"Tree±1={m['tree_within1']*100:6.2f}%  MAE={m['macro_mae']:.3f}  "
                      f"Bias={m['mean_bias']:+.3f}{star}")
        print("\n  RINGKASAN TERBAIK PER MODE:")
        for mode, (thr, m) in best.items():
            print(f"    {mode:12s} thr={thr:<6} Class±1={m['class_within1']*100:6.2f}%  "
                  f"MAE={m['macro_mae']:.3f}")
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "sweep.json").write_text(json.dumps(
            {k: {"thr": v[0], **v[1]} for k, v in best.items()}, indent=1))
        return 0

    for t in trees:
        g = load_tree_gt(t)
        bc = g["summary"]["by_class"]
        gt_counts.append([bc.get(c, 0) for c in CLASSES])
        raw = None
        for mode in preds:
            u, r = link_tree(t, by_tree[t], cams, mode, THR[mode])
            preds[mode].append(u)
            raw = r
        raw_counts.append(raw)

    gt = np.array(gt_counts)
    raw = np.array(raw_counts)
    k_pred = np.rint(raw / K_GLOBAL).astype(int)

    W = 74
    print("=" * W)
    print(f"E-007 — PENAUTAN LINTAS-SISI ({len(trees)} pohon, split {args.split})")
    print("=" * W)
    print(f"  {'metode':26s} {'Class±1':>9s} {'Tree±1':>8s} {'MAE':>8s} {'Bias':>8s}")

    rows = {}
    m = metrics(raw, gt); rows["Jumlah mentah (naif)"] = m
    m = metrics(k_pred, gt); rows[f"Koreksi global k={K_GLOBAL}"] = m
    for mode, label in (("appearance", "A. hanya penampilan"),
                        ("depth", "B. depth tanpa pose"),
                        ("pose", "C. sadar-pose (3D)")):
        rows[label] = metrics(np.array(preds[mode]), gt)

    for label, v in rows.items():
        print(f"  {label:26s} {v['class_within1']*100:8.2f}% {v['tree_within1']*100:7.2f}% "
              f"{v['macro_mae']:8.3f} {v['mean_bias']:+8.3f}")

    print(f"\n  acuan publikasi (GT+SVR)   :    96.81%   88.65%    0.303   -0.048")
    print(f"  acuan publikasi (YOLO+SVR) :    75.35%   33.33%    1.027   +0.158")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / f"report_{args.split}.json").write_text(
        json.dumps({"split": args.split, "n_trees": len(trees),
                    "thresholds": THR, "results": rows}, indent=1), encoding="utf-8")
    print(f"\nlaporan -> {args.out / f'report_{args.split}.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
