#!/usr/bin/env python3
"""I-11 — Evaluasi terstratifikasi untuk semua varian model.

Satu angka mAP menyembunyikan justru hal yang ingin kita ketahui. Naskah
(Tabel hierarki metrik, §234-262) menuntut deteksi dilaporkan per strata ukuran
dan oklusi; diagnosis SR-007 menambahkan strata yang lebih relevan lagi untuk
dataset ini: **kontras**, karena di situlah B4 gagal.

Skrip ini mengevaluasi model apa pun (RGB, RGB+D, RGB+tekstur) dengan alat yang
PERSIS SAMA, lalu memecah hasilnya menurut:
  - kelas (B1-B4)
  - ukuran kotak (tercile: kecil / sedang / besar)
  - kontras kotak terhadap sekelilingnya (tercile: rendah / sedang / tinggi)

Strata dihitung dari kotak kebenaran-dasar, jadi identik untuk semua model --
perbandingannya adil.

Pemakaian:
  python stratified_eval.py --weights runs/rgb_.../weights/best.pt --mode rgb
  python stratified_eval.py --weights runs/rgbt_.../weights/best.pt --mode rgbt
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
DEPTH = Path("/workspace/experiments/depth_da3/depth")
OUT = Path("/workspace/experiments/results/strat")
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


def texture_channel(bgr):
    g = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lap = np.abs(cv2.Laplacian(g, cv2.CV_32F, ksize=3))
    lap = cv2.GaussianBlur(lap, (0, 0), 2)
    hi = np.percentile(lap, 99.5)
    return np.clip(lap / max(hi, 1e-6) * 255, 0, 255).astype(np.uint8)


def depth_channel(stem, shape):
    dp = DEPTH / f"{stem}.png"
    d = cv2.imread(str(dp), cv2.IMREAD_UNCHANGED)
    if d is None:
        return np.zeros(shape, np.uint8)
    if d.dtype != np.uint8:
        d = (d.astype(np.float32) / 65535.0 * 255).astype(np.uint8)
    if d.shape[:2] != shape:
        d = cv2.resize(d, (shape[1], shape[0]))
    return d


def box_contrast(bgr, box) -> float:
    """dE CIELAB isi kotak vs cincin -- dipakai untuk membagi strata kontras."""
    H, W = bgr.shape[:2]
    x0, y0, x1, y1 = box
    if x1 - x0 < 4 or y1 - y0 < 4:
        return 0.0
    inner = bgr[y0:y1, x0:x1]
    bw, bh = x1 - x0, y1 - y0
    ex, ey = bw // 2, bh // 2
    X0, Y0 = max(0, x0 - ex), max(0, y0 - ey)
    X1, Y1 = min(W, x1 + ex), min(H, y1 + ey)
    outer = bgr[Y0:Y1, X0:X1]
    mask = np.ones(outer.shape[:2], bool)
    mask[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = False
    if mask.sum() < 10 or inner.size == 0:
        return 0.0
    li = cv2.cvtColor(inner, cv2.COLOR_BGR2LAB).reshape(-1, 3).astype(np.float32).mean(0)
    lo = cv2.cvtColor(outer, cv2.COLOR_BGR2LAB)[mask].astype(np.float32).mean(0)
    return float(np.linalg.norm(li - lo))


def ap50(preds, gts, keep) -> float:
    """AP50 gaya VOC atas himpunan kotak kebenaran-dasar terpilih (`keep`).

    Prediksi yang mencocoki kotak GT di luar `keep` tidak dihitung sebagai
    positif palsu -- kalau tidak, AP tiap strata akan dihukum oleh objek yang
    memang bukan bagian strata itu.
    """
    recs = []
    npos = sum(len(v) for v in keep.values())
    if npos == 0:
        return float("nan")
    for im, ps in preds.items():
        for cls, sc, *b in ps:
            recs.append((sc, im, b, cls))
    recs.sort(key=lambda r: -r[0])
    matched = defaultdict(set)
    tp, fp = [], []
    for sc, im, b, cls in recs:
        cand = keep.get(im, [])
        other = gts.get(im, [])
        best, bj = 0.0, -1
        for j, g in enumerate(cand):
            if g[0] != cls:
                continue
            ix0, iy0 = max(b[0], g[1]), max(b[1], g[2])
            ix1, iy1 = min(b[2], g[3]), min(b[3], g[4])
            inter = max(0, ix1-ix0) * max(0, iy1-iy0)
            u = (b[2]-b[0])*(b[3]-b[1]) + (g[3]-g[1])*(g[4]-g[2]) - inter
            iou = inter / (u + 1e-9)
            if iou > best:
                best, bj = iou, j
        if best >= 0.5 and bj not in matched[im]:
            tp.append(1); fp.append(0); matched[im].add(bj)
        else:
            # abaikan bila mencocoki GT di luar strata
            hit_other = False
            for g in other:
                if g[0] != cls:
                    continue
                ix0, iy0 = max(b[0], g[1]), max(b[1], g[2])
                ix1, iy1 = min(b[2], g[3]), min(b[3], g[4])
                inter = max(0, ix1-ix0) * max(0, iy1-iy0)
                u = (b[2]-b[0])*(b[3]-b[1]) + (g[3]-g[1])*(g[4]-g[2]) - inter
                if inter / (u + 1e-9) >= 0.5:
                    hit_other = True
                    break
            if hit_other:
                continue
            tp.append(0); fp.append(1)
    if not tp:
        return 0.0
    tp, fp = np.array(tp), np.array(fp)
    ctp, cfp = tp.cumsum(), fp.cumsum()
    rec = ctp / npos
    prec = ctp / np.maximum(ctp + cfp, 1e-9)
    mrec = np.r_[0, rec, 1]; mpre = np.r_[0, prec, 0]
    for i in range(len(mpre) - 2, -1, -1):
        mpre[i] = max(mpre[i], mpre[i + 1])
    idx = np.where(mrec[1:] != mrec[:-1])[0]
    return float(((mrec[idx + 1] - mrec[idx]) * mpre[idx + 1]).sum())


def main() -> int:
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("--weights", required=True)
    ap_.add_argument("--mode", choices=["rgb", "rgbd", "rgbt"], default="rgb")
    ap_.add_argument("--imgsz", type=int, default=640)
    ap_.add_argument("--conf", type=float, default=0.001)
    ap_.add_argument("--tag", default=None)
    ap_.add_argument("--limit", type=int, default=None)
    ap_.add_argument("--device", default=None)
    args = ap_.parse_args()

    from ultralytics import YOLO
    model = YOLO(args.weights)

    names = [Path(l).stem for l in (SRC / "test.txt").read_text().split() if l.strip()]
    if args.limit:
        names = names[: args.limit]
    preds, gts = {}, {}
    meta = []          # (stem, idx, cls, area, contrast)

    for n, stem in enumerate(names):
        bgr = cv2.imread(str(SRC / "images" / f"{stem}.jpg"))
        if bgr is None:
            continue
        H, W = bgr.shape[:2]
        g = []
        for i, (c, cx, cy, bw, bh) in enumerate(load_boxes(stem)):
            box = (int((cx-bw/2)*W), int((cy-bh/2)*H), int((cx+bw/2)*W), int((cy+bh/2)*H))
            g.append([c, *box])
            meta.append((stem, i, c, (box[2]-box[0])*(box[3]-box[1]),
                         box_contrast(bgr, box)))
        gts[stem] = g

        if args.mode == "rgbt":
            inp = np.dstack([bgr, texture_channel(bgr)])
        elif args.mode == "rgbd":
            inp = np.dstack([bgr, depth_channel(stem, bgr.shape[:2])])
        else:
            inp = bgr

        r = model.predict(inp, imgsz=args.imgsz, conf=args.conf, verbose=False,
                          device=args.device)[0]
        preds[stem] = [[int(c), float(s), *b] for b, s, c in zip(
            r.boxes.xyxy.cpu().numpy(), r.boxes.conf.cpu().numpy(),
            r.boxes.cls.cpu().numpy())]
        if (n + 1) % 150 == 0:
            print(f"  {n+1}/{len(names)}")

    areas = np.array([m[3] for m in meta])
    cons = np.array([m[4] for m in meta])
    a_t = np.percentile(areas, [33, 66])
    c_t = np.percentile(cons, [33, 66])

    def subset(pred_fn):
        keep = defaultdict(list)
        for (stem, i, c, a, ct) in meta:
            if pred_fn(c, a, ct):
                keep[stem].append(gts[stem][i])
        return dict(keep)

    tag = args.tag or Path(args.weights).parts[-3]
    W_ = 72
    print("\n" + "=" * W_)
    print(f"EVALUASI TERSTRATIFIKASI — {tag} (mode {args.mode})")
    print("=" * W_)

    res = {"tag": tag, "mode": args.mode}
    all_ap = ap50(preds, gts, subset(lambda c, a, ct: True))
    print(f"  AP50 keseluruhan : {all_ap:.4f}")
    res["overall"] = all_ap

    print("\n  per KELAS")
    res["per_class"] = {}
    for ci, cn in enumerate(CLASSES):
        v = ap50(preds, gts, subset(lambda c, a, ct, ci=ci: c == ci))
        print(f"    {cn:4s} {v:.4f}")
        res["per_class"][cn] = v

    print(f"\n  per UKURAN (tercile: <{a_t[0]:.0f}, <{a_t[1]:.0f}, >=)")
    res["per_size"] = {}
    for lbl, fn in (("kecil", lambda c, a, ct: a < a_t[0]),
                    ("sedang", lambda c, a, ct: a_t[0] <= a < a_t[1]),
                    ("besar", lambda c, a, ct: a >= a_t[1])):
        v = ap50(preds, gts, subset(fn))
        print(f"    {lbl:7s} {v:.4f}")
        res["per_size"][lbl] = v

    print(f"\n  per KONTRAS (tercile: <{c_t[0]:.1f}, <{c_t[1]:.1f}, >=)")
    res["per_contrast"] = {}
    for lbl, fn in (("rendah", lambda c, a, ct: ct < c_t[0]),
                    ("sedang", lambda c, a, ct: c_t[0] <= ct < c_t[1]),
                    ("tinggi", lambda c, a, ct: ct >= c_t[1])):
        v = ap50(preds, gts, subset(fn))
        print(f"    {lbl:7s} {v:.4f}")
        res["per_contrast"][lbl] = v

    print("\n  B4 pada KONTRAS RENDAH (kasus tersulit menurut SR-007)")
    v = ap50(preds, gts, subset(lambda c, a, ct: c == 3 and ct < c_t[0]))
    print(f"    {v:.4f}")
    res["b4_low_contrast"] = v

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{tag}_{args.mode}.json").write_text(json.dumps(res, indent=1))
    print(f"\nlaporan -> {OUT / f'{tag}_{args.mode}.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
