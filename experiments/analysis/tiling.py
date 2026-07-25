#!/usr/bin/env python3
"""I-12 — Pelatihan berbasis ubin (tiling) untuk tandan kecil (E-008).

Masalah: B4 adalah kelas terburuk (AP50 0,354) dan kotaknya paling kecil. Pada
`imgsz=640` dari sumber 960x1280, seluruh citra diperkecil ~2x, sehingga tandan
B4 tinggal segelintir piksel. Detektor tidak bisa menemukan apa yang sudah
hilang sebelum masuk ke jaringan.

Ini BUKAN penyetelan hyperparameter. Menaikkan `imgsz` hanya memperbesar piksel
yang sudah kabur; memotong citra menjadi ubin lalu melatih pada skala aslinya
memberi jaringan piksel yang benar-benar lebih banyak per tandan. Regime
pelatihan yang berbeda, bukan angka yang berbeda.

Rancangan:
  1. Potong tiap citra menjadi ubin bertumpang tindih, sesuaikan labelnya.
  2. Latih detektor pada ubin.
  3. Saat inferensi, potong citra uji dengan cara sama, deteksi per ubin,
     kembalikan koordinat ke citra penuh, lalu gabungkan dengan NMS.
  4. Evaluasi pada CITRA PENUH memakai label asli -- supaya angkanya sebanding
     dengan baseline dan dengan DiB. Mengevaluasi per-ubin akan menghasilkan
     angka yang terlihat bagus tetapi tidak sebanding.

Pemakaian:
  python tiling.py --build
  python tiling.py --train --epochs 40
  python tiling.py --eval --weights runs/tile_.../weights/best.pt
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
TILE = Path("/workspace/experiments/data_tiles")
RUNS = Path("/workspace/experiments/runs")
CLASSES = ["B1", "B2", "B3", "B4"]


# --------------------------------------------------------------------------
def tile_grid(W: int, H: int, nx: int, ny: int, overlap: float):
    """Kotak ubin bertumpang tindih. Tumpang tindih perlu supaya tandan yang
    kebetulan jatuh di garis potong tidak hilang dari kedua ubin."""
    tw, th = W / nx, H / ny
    ox, oy = tw * overlap, th * overlap
    out = []
    for j in range(ny):
        for i in range(nx):
            x0 = max(0, int(i * tw - ox)); x1 = min(W, int((i + 1) * tw + ox))
            y0 = max(0, int(j * th - oy)); y1 = min(H, int((j + 1) * th + oy))
            out.append((x0, y0, x1, y1))
    return out


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


def build(nx: int, ny: int, overlap: float, min_visible: float = 0.35) -> None:
    """Rakit dataset ubin. Kotak yang terpotong dipertahankan hanya bila
    bagian yang tersisa >= min_visible dari luas aslinya; kalau tidak, ia
    menjadi label palsu yang mengajarkan model mendeteksi potongan."""
    (TILE / "images").mkdir(parents=True, exist_ok=True)
    (TILE / "labels").mkdir(parents=True, exist_ok=True)

    counts = defaultdict(int)
    for split in ("train", "val"):
        names = [Path(l).stem for l in (SRC / f"{split}.txt").read_text().split() if l.strip()]
        lines = []
        for stem in names:
            ip = SRC / "images" / f"{stem}.jpg"
            im = cv2.imread(str(ip))
            if im is None:
                continue
            H, W = im.shape[:2]
            boxes = load_boxes(stem)
            for ti, (x0, y0, x1, y1) in enumerate(tile_grid(W, H, nx, ny, overlap)):
                tw, th = x1 - x0, y1 - y0
                keep = []
                for c, cx, cy, bw, bh in boxes:
                    bx0, by0 = (cx - bw / 2) * W, (cy - bh / 2) * H
                    bx1, by1 = (cx + bw / 2) * W, (cy + bh / 2) * H
                    ix0, iy0 = max(bx0, x0), max(by0, y0)
                    ix1, iy1 = min(bx1, x1), min(by1, y1)
                    if ix1 <= ix0 or iy1 <= iy0:
                        continue
                    area_o = (bx1 - bx0) * (by1 - by0)
                    if area_o <= 0 or ((ix1 - ix0) * (iy1 - iy0)) / area_o < min_visible:
                        continue
                    ncx = ((ix0 + ix1) / 2 - x0) / tw
                    ncy = ((iy0 + iy1) / 2 - y0) / th
                    nbw = (ix1 - ix0) / tw
                    nbh = (iy1 - iy0) / th
                    keep.append(f"{c} {ncx:.6f} {ncy:.6f} {nbw:.6f} {nbh:.6f}")
                    counts[CLASSES[c]] += 1
                # ubin tanpa objek tetap disimpan sebagian sebagai latar negatif
                if not keep and (ti % 3):
                    continue
                name = f"{stem}_t{ti}"
                op = TILE / "images" / f"{name}.jpg"
                if not op.exists():
                    cv2.imwrite(str(op), im[y0:y1, x0:x1], [cv2.IMWRITE_JPEG_QUALITY, 92])
                (TILE / "labels" / f"{name}.txt").write_text("\n".join(keep) + ("\n" if keep else ""))
                lines.append(str(op))
        (TILE / f"{split}.txt").write_text("\n".join(lines) + "\n")
        print(f"  {split}: {len(lines)} ubin")
    print("  objek per kelas pada ubin:", dict(counts))

    (TILE / "data.yaml").write_text(
        f"path: {TILE}\ntrain: train.txt\nval: val.txt\n"
        f"channels: 3\nnc: 4\nnames:\n" +
        "".join(f"  {i}: {c}\n" for i, c in enumerate(CLASSES)))
    (TILE / "grid.json").write_text(json.dumps({"nx": nx, "ny": ny, "overlap": overlap}))


# --------------------------------------------------------------------------
def nms(boxes: np.ndarray, scores: np.ndarray, iou_thr: float = 0.55) -> list[int]:
    idx = scores.argsort()[::-1]
    keep = []
    while len(idx):
        i = idx[0]
        keep.append(i)
        if len(idx) == 1:
            break
        xx0 = np.maximum(boxes[i, 0], boxes[idx[1:], 0])
        yy0 = np.maximum(boxes[i, 1], boxes[idx[1:], 1])
        xx1 = np.minimum(boxes[i, 2], boxes[idx[1:], 2])
        yy1 = np.minimum(boxes[i, 3], boxes[idx[1:], 3])
        inter = np.clip(xx1 - xx0, 0, None) * np.clip(yy1 - yy0, 0, None)
        a1 = (boxes[i, 2] - boxes[i, 0]) * (boxes[i, 3] - boxes[i, 1])
        a2 = ((boxes[idx[1:], 2] - boxes[idx[1:], 0]) *
              (boxes[idx[1:], 3] - boxes[idx[1:], 1]))
        iou = inter / (a1 + a2 - inter + 1e-9)
        idx = idx[1:][iou < iou_thr]
    return keep


def ap50_per_class(preds: dict, gts: dict, n_cls: int = 4, iou_thr: float = 0.5):
    """AP50 gaya VOC dengan interpolasi seluruh titik, dihitung sendiri agar
    baseline dan varian ubin diukur dengan alat yang persis sama."""
    aps, ps, rs = [], [], []
    for c in range(n_cls):
        recs = []
        npos = 0
        for im, g in gts.items():
            gb = np.array([b[1:] for b in g if b[0] == c], dtype=np.float64).reshape(-1, 4)
            npos += len(gb)
        for im, p in preds.items():
            for cls, sc, *box in p:
                if cls == c:
                    recs.append((sc, im, box))
        recs.sort(key=lambda r: -r[0])
        matched = defaultdict(set)
        tp = np.zeros(len(recs)); fp = np.zeros(len(recs))
        for k, (sc, im, box) in enumerate(recs):
            gb = [b[1:] for b in gts.get(im, []) if b[0] == c]
            best_iou, best_j = 0.0, -1
            for j, g in enumerate(gb):
                ix0, iy0 = max(box[0], g[0]), max(box[1], g[1])
                ix1, iy1 = min(box[2], g[2]), min(box[3], g[3])
                inter = max(0, ix1 - ix0) * max(0, iy1 - iy0)
                u = ((box[2]-box[0])*(box[3]-box[1]) + (g[2]-g[0])*(g[3]-g[1]) - inter)
                iou = inter / (u + 1e-9)
                if iou > best_iou:
                    best_iou, best_j = iou, j
            if best_iou >= iou_thr and best_j not in matched[im]:
                tp[k] = 1; matched[im].add(best_j)
            else:
                fp[k] = 1
        if npos == 0:
            aps.append(float("nan")); ps.append(float("nan")); rs.append(float("nan"))
            continue
        ctp, cfp = tp.cumsum(), fp.cumsum()
        rec = ctp / npos
        prec = ctp / np.maximum(ctp + cfp, 1e-9)
        mrec = np.r_[0, rec, 1]; mpre = np.r_[0, prec, 0]
        for i in range(len(mpre) - 2, -1, -1):
            mpre[i] = max(mpre[i], mpre[i + 1])
        idx = np.where(mrec[1:] != mrec[:-1])[0]
        aps.append(float(((mrec[idx + 1] - mrec[idx]) * mpre[idx + 1]).sum()))
        ps.append(float(prec[-1]) if len(prec) else 0.0)
        rs.append(float(rec[-1]) if len(rec) else 0.0)
    return aps, ps, rs


def evaluate(weights: str, tiled: bool, conf: float = 0.001, imgsz: int = 640):
    from ultralytics import YOLO
    model = YOLO(weights)
    grid = json.loads((TILE / "grid.json").read_text()) if tiled else None

    names = [Path(l).stem for l in (SRC / "test.txt").read_text().split() if l.strip()]
    preds, gts = {}, {}
    for n, stem in enumerate(names):
        ip = SRC / "images" / f"{stem}.jpg"
        im = cv2.imread(str(ip))
        H, W = im.shape[:2]
        gts[stem] = [[c, (cx-bw/2)*W, (cy-bh/2)*H, (cx+bw/2)*W, (cy+bh/2)*H]
                     for c, cx, cy, bw, bh in load_boxes(stem)]

        out = []
        if tiled:
            for (x0, y0, x1, y1) in tile_grid(W, H, grid["nx"], grid["ny"], grid["overlap"]):
                r = model.predict(im[y0:y1, x0:x1], imgsz=imgsz, conf=conf,
                                  verbose=False)[0]
                for b, s, c in zip(r.boxes.xyxy.cpu().numpy(),
                                   r.boxes.conf.cpu().numpy(),
                                   r.boxes.cls.cpu().numpy().astype(int)):
                    out.append([c, float(s), b[0]+x0, b[1]+y0, b[2]+x0, b[3]+y0])
        else:
            r = model.predict(im, imgsz=imgsz, conf=conf, verbose=False)[0]
            for b, s, c in zip(r.boxes.xyxy.cpu().numpy(),
                               r.boxes.conf.cpu().numpy(),
                               r.boxes.cls.cpu().numpy().astype(int)):
                out.append([c, float(s), *b])

        if out:
            arr = np.array([o[2:] for o in out], dtype=np.float64)
            sc = np.array([o[1] for o in out])
            cl = np.array([o[0] for o in out], dtype=int)
            kept = []
            for c in range(4):
                m = np.where(cl == c)[0]
                if len(m):
                    for k in nms(arr[m], sc[m]):
                        kept.append(out[m[k]])
            out = kept
        preds[stem] = out
        if (n + 1) % 100 == 0:
            print(f"    {n+1}/{len(names)} citra")

    aps, ps, rs = ap50_per_class(preds, gts)
    print(f"\n  {'kelas':6s} {'AP50':>8s} {'P':>8s} {'R':>8s}")
    for i, c in enumerate(CLASSES):
        print(f"  {c:6s} {aps[i]:8.4f} {ps[i]:8.4f} {rs[i]:8.4f}")
    print(f"  {'mAP50':6s} {np.nanmean(aps):8.4f}")
    return {"ap50": aps, "p": ps, "r": rs, "map50": float(np.nanmean(aps))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--train", action="store_true")
    ap.add_argument("--eval", action="store_true")
    ap.add_argument("--nx", type=int, default=2)
    ap.add_argument("--ny", type=int, default=3)
    ap.add_argument("--overlap", type=float, default=0.15)
    ap.add_argument("--epochs", type=int, default=40)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--weights", default="yolo26m.pt")
    ap.add_argument("--tiled-eval", action="store_true", default=False)
    args = ap.parse_args()

    if args.build:
        build(args.nx, args.ny, args.overlap)
    if args.train:
        from ultralytics import YOLO
        name = f"tile{args.nx}x{args.ny}_e{args.epochs}_s{args.seed}"
        YOLO(args.weights).train(
            data=str(TILE / "data.yaml"), epochs=args.epochs, imgsz=args.imgsz,
            batch=args.batch, seed=args.seed, project=str(RUNS), name=name,
            exist_ok=True, patience=args.epochs, plots=False, deterministic=True)
        print(f"bobot -> {RUNS / name / 'weights' / 'best.pt'}")
    if args.eval:
        r = evaluate(args.weights, tiled=args.tiled_eval, imgsz=args.imgsz)
        out = Path("/workspace/experiments/results/e008")
        out.mkdir(parents=True, exist_ok=True)
        tag = "tiled" if args.tiled_eval else "full"
        (out / f"eval_{tag}.json").write_text(json.dumps(r, indent=1))
        print(f"\nlaporan -> {out / f'eval_{tag}.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
