"""Per-kelas AP50 & AP50-95 RF-DETR-L (checkpoint terbaik ep9) via COCO eval.

evaluation.json rf-detr hanya menyimpan per-kelas AP50-95; di sini keduanya
diambil (AP50 + AP50-95, val+test) lewat pycocotools agar konsisten dengan
model lain. Overall di-print sebagai sanity check terhadap angka resmi
(val 0.5699/0.2604 EMA, test 0.5837/0.2653). Hasil di-merge ke
results/perkelas_fair.json.
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

from rfdetr import RFDETRLarge

NAMES = ["B1", "B2", "B3", "B4"]
CKPT = "runs/rfdetr_l_e60_i1280/checkpoint_best_ema.pth"
DS = Path("rfdetr_ds")
SPLIT_DIR = {"val": "valid", "test": "test"}
OUT = Path("results/perkelas_fair.json")
CHUNK = 8


def build_gt(split_dir):
    """COCO GT dari label YOLO. Kategori 1..4 (B1..B4)."""
    images, anns = [], []
    ann_id = 1
    idir = DS / split_dir / "images"
    ldir = DS / split_dir / "labels"
    paths = sorted(idir.iterdir())
    for img_id, p in enumerate(paths, 1):
        w, h = Image.open(p).size
        images.append({"id": img_id, "file_name": p.name, "width": w, "height": h})
        lf = ldir / (p.stem + ".txt")
        if not lf.is_file():
            continue
        for line in lf.read_text().splitlines():
            if not line.strip():
                continue
            c, cx, cy, bw, bh = map(float, line.split())
            x = (cx - bw / 2) * w
            y = (cy - bh / 2) * h
            aw, ah = bw * w, bh * h
            anns.append({"id": ann_id, "image_id": img_id, "category_id": int(c) + 1,
                         "bbox": [x, y, aw, ah], "area": aw * ah, "iscrowd": 0})
            ann_id += 1
    gt = COCO()
    gt.dataset = {"images": images, "annotations": anns,
                  "categories": [{"id": i + 1, "name": n} for i, n in enumerate(NAMES)]}
    gt.createIndex()
    return gt, paths


def predict_split(model, paths):
    results = []
    for i in range(0, len(paths), CHUNK):
        chunk = [str(p) for p in paths[i:i + CHUNK]]
        dets_list = model.predict(chunk, threshold=0.001)
        if not isinstance(dets_list, list):
            dets_list = [dets_list]
        for j, dets in enumerate(dets_list):
            img_id = i + j + 1
            xyxy = dets.xyxy
            conf = dets.confidence
            cls = dets.class_id
            for k in range(len(xyxy)):
                x1, y1, x2, y2 = xyxy[k]
                results.append({"image_id": img_id, "category_id": int(cls[k]) + 1,
                                "bbox": [float(x1), float(y1), float(x2 - x1), float(y2 - y1)],
                                "score": float(conf[k])})
    return results


def per_class_ap(coco_eval):
    """precision: [T(iou), R(recall), K(cat), A(area), M(maxdet)]."""
    p = coco_eval.eval["precision"]
    ap50, ap5095 = {}, {}
    for k, n in enumerate(NAMES):
        s95 = p[:, :, k, 0, 2]
        s50 = p[0, :, k, 0, 2]
        ap5095[n] = round(float(s95[s95 > -1].mean()) if (s95 > -1).any() else 0.0, 4)
        ap50[n] = round(float(s50[s50 > -1].mean()) if (s50 > -1).any() else 0.0, 4)
    return ap50, ap5095


def main():
    print(f"Load checkpoint: {CKPT}")
    model = RFDETRLarge(pretrain_weights=CKPT, resolution=1280)
    result = {"params_juta": 35.7, "imgsz": 1280}
    for split, sdir in SPLIT_DIR.items():
        print(f"== {split} ({sdir}) ==")
        gt, paths = build_gt(sdir)
        dt_list = predict_split(model, paths)
        dt = gt.loadRes(dt_list)
        ev = COCOeval(gt, dt, "bbox")
        ev.evaluate(); ev.accumulate(); ev.summarize()
        ap50, ap5095 = per_class_ap(ev)
        overall_5095 = round(float(ev.stats[0]), 4)   # AP@[.5:.95]
        overall_50 = round(float(ev.stats[1]), 4)     # AP@.5
        result[split] = {"mAP50": overall_50, "mAP50_95": overall_5095,
                         "per_kelas_AP50": ap50, "per_kelas_AP50_95": ap5095}
        print(f"  overall mAP50={overall_50} mAP50-95={overall_5095}")
        for n in NAMES:
            print(f"    {n}: AP50={ap50[n]:.4f}  AP50-95={ap5095[n]:.4f}")
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    data["RF-DETR-L"] = result
    OUT.write_text(json.dumps(data, indent=2))
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
