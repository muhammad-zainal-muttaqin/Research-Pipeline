"""Per-kelas AP50 & AP50-95 SEMUA model lewat SATU protokol (pycocotools).

Menghapus caveat evaluator campur: YOLO26m, RT-DETR-L, YOLO26l, RF-DETR-L
semua dievaluasi dengan pipeline identik — predict (threshold rendah) lalu
COCOeval pada GT yang sama (dibangun sekali dari label YOLO). Setiap model di
resolusi latihannya sendiri. Hasil -> results/perkelas_pycoco.json.
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

NAMES = ["B1", "B2", "B3", "B4"]
DS = Path("rfdetr_ds")
SPLIT_DIR = {"val": "valid", "test": "test"}
OUT = Path("results/perkelas_pycoco.json")
CHUNK = 8

# (kunci, tipe, bobot, imgsz, param_juta). tipe: yolo | rtdetr | rfdetr
MODELS = [
    ("YOLO26m",   "yolo",   "runs/rgb_e60_i640_s42/weights/best.pt",     640,  21.9),
    ("RT-DETR-L", "rtdetr", "runs/rtdetr_l_e60_i1280/weights/best.pt",   1280, 33.0),
    ("YOLO26l",   "yolo",   "runs/yolo26l_e60_i1280/weights/best.pt",    1280, 26.3),
    ("RF-DETR-L", "rfdetr", "runs/rfdetr_l_e60_i1280/checkpoint_best_ema.pth", 1280, 35.7),
]


def build_gt(split_dir):
    images, anns, ann_id = [], [], 1
    idir, ldir = DS / split_dir / "images", DS / split_dir / "labels"
    paths = sorted(idir.iterdir())
    for img_id, p in enumerate(paths, 1):
        w, h = Image.open(p).size
        images.append({"id": img_id, "file_name": p.name, "width": w, "height": h})
        lf = ldir / (p.stem + ".txt")
        if lf.is_file():
            for line in lf.read_text().splitlines():
                if not line.strip():
                    continue
                c, cx, cy, bw, bh = map(float, line.split())
                x, y, aw, ah = (cx - bw / 2) * w, (cy - bh / 2) * h, bw * w, bh * h
                anns.append({"id": ann_id, "image_id": img_id, "category_id": int(c) + 1,
                             "bbox": [x, y, aw, ah], "area": aw * ah, "iscrowd": 0})
                ann_id += 1
    gt = COCO()
    gt.dataset = {"images": images, "annotations": anns,
                  "categories": [{"id": i + 1, "name": n} for i, n in enumerate(NAMES)]}
    gt.createIndex()
    return gt, paths


def predict_ultra(model, paths, imgsz):
    res = []
    for i, p in enumerate(paths, 1):
        r = model.predict(str(p), imgsz=imgsz, conf=0.001, verbose=False)[0]
        b = r.boxes
        if b is None:
            continue
        xyxy = b.xyxy.cpu().numpy(); conf = b.conf.cpu().numpy(); cls = b.cls.cpu().numpy()
        for k in range(len(xyxy)):
            x1, y1, x2, y2 = xyxy[k]
            res.append({"image_id": i, "category_id": int(cls[k]) + 1,
                        "bbox": [float(x1), float(y1), float(x2 - x1), float(y2 - y1)],
                        "score": float(conf[k])})
    return res


def predict_rfdetr(model, paths):
    res = []
    for i in range(0, len(paths), CHUNK):
        chunk = [str(p) for p in paths[i:i + CHUNK]]
        dl = model.predict(chunk, threshold=0.001)
        if not isinstance(dl, list):
            dl = [dl]
        for j, d in enumerate(dl):
            img_id = i + j + 1
            for k in range(len(d.xyxy)):
                x1, y1, x2, y2 = d.xyxy[k]
                res.append({"image_id": img_id, "category_id": int(d.class_id[k]) + 1,
                            "bbox": [float(x1), float(y1), float(x2 - x1), float(y2 - y1)],
                            "score": float(d.confidence[k])})
    return res


def per_class_ap(ev):
    p = ev.eval["precision"]  # [T,R,K,A,M]
    ap50, ap95 = {}, {}
    for k, n in enumerate(NAMES):
        s95, s50 = p[:, :, k, 0, 2], p[0, :, k, 0, 2]
        ap95[n] = round(float(s95[s95 > -1].mean()) if (s95 > -1).any() else 0.0, 4)
        ap50[n] = round(float(s50[s50 > -1].mean()) if (s50 > -1).any() else 0.0, 4)
    return ap50, ap95


def load(kind, weights, imgsz):
    if kind == "yolo":
        from ultralytics import YOLO
        return YOLO(weights)
    if kind == "rtdetr":
        from ultralytics import RTDETR
        return RTDETR(weights)
    from rfdetr import RFDETRLarge
    return RFDETRLarge(pretrain_weights=weights, resolution=imgsz)


def main():
    gts = {s: build_gt(sd) for s, sd in SPLIT_DIR.items()}
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for key, kind, weights, imgsz, params in MODELS:
        if not Path(weights).exists():
            print(f"SKIP {key}: bobot belum ada ({weights})"); continue
        print(f"\n===== {key} ({params}jt, imgsz {imgsz}, {kind}) =====")
        model = load(kind, weights, imgsz)
        entry = {"params_juta": params, "imgsz": imgsz, "evaluator": "pycocotools"}
        for split, (gt, paths) in gts.items():
            dt_list = predict_rfdetr(model, paths) if kind == "rfdetr" else predict_ultra(model, paths, imgsz)
            ev = COCOeval(gt, gt.loadRes(dt_list), "bbox")
            ev.evaluate(); ev.accumulate(); ev.summarize()
            ap50, ap95 = per_class_ap(ev)
            entry[split] = {"mAP50": round(float(ev.stats[1]), 4),
                            "mAP50_95": round(float(ev.stats[0]), 4),
                            "per_kelas_AP50": ap50, "per_kelas_AP50_95": ap95}
            print(f"  {split}: mAP50={entry[split]['mAP50']} mAP50-95={entry[split]['mAP50_95']}")
        data[key] = entry
        OUT.parent.mkdir(exist_ok=True)
        OUT.write_text(json.dumps(data, indent=2))  # simpan progresif tiap model
        del model
    print(f"\n-> {OUT}")


if __name__ == "__main__":
    main()
