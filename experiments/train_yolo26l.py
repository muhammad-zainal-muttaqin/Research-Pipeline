"""Baseline YOLO adil sekelas DETR-L: YOLO26l (26,3 jt param) @1280.

Motivasi: YOLO26m (21,9 jt, 640) tidak setara dengan RT-DETR-L (33,0 jt) dan
RF-DETR-L (35,7 jt) yang dibandingkan pada 1280. YOLO26l adalah varian YOLO26
dengan parameter TERDEKAT ke DETR-L, dilatih di sini dengan konfigurasi IDENTIK
RT-DETR (imgsz 1280, 60 epoch, cos_lr, augmentasi aman-warna hsv kecil E-019,
seed 42, dari bobot COCO) agar perbandingan benar-benar apple-to-apple.

Menulis per-kelas AP50 DAN AP50-95 (val+test) ke results/yolo26l_eval.json.
"""
import argparse
import json
from pathlib import Path

from ultralytics import YOLO

NAMES = ["B1", "B2", "B3", "B4"]


def evaluate(model, imgsz):
    out = {}
    for split in ["val", "test"]:
        r = model.val(data="data_rgb.yaml", split=split, imgsz=imgsz, batch=2,
                      plots=False, verbose=False)
        out[split] = {
            "mAP50": round(float(r.box.map50), 4),
            "mAP50_95": round(float(r.box.map), 4),
            "precision": round(float(r.box.mp), 4),
            "recall": round(float(r.box.mr), 4),
            "per_kelas_AP50": {NAMES[i]: round(float(r.box.ap50[i]), 4) for i in range(4)},
            "per_kelas_AP50_95": {NAMES[i]: round(float(r.box.ap[i]), 4) for i in range(4)},
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights", default="yolo26l.pt")
    ap.add_argument("--imgsz", type=int, default=1280)
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--batch", type=int, default=4)
    ap.add_argument("--name", default="yolo26l_e60_i1280")
    ap.add_argument("--resume", action="store_true",
                    help="Lanjut dari runs/<name>/weights/last.pt (recovery).")
    a = ap.parse_args()

    if a.resume:
        # Ultralytics memuat argumen train dari args.yaml saat resume=True.
        m = YOLO(f"/workspace/experiments/runs/{a.name}/weights/last.pt")
        m.train(resume=True)
    else:
        m = YOLO(a.weights)
        m.train(data="data_rgb.yaml", epochs=a.epochs, imgsz=a.imgsz, batch=a.batch,
                seed=42, name=a.name, project="/workspace/experiments/runs",
                exist_ok=True, cos_lr=True,
                hsv_h=0.005, hsv_s=0.15, hsv_v=0.25,
                plots=False, patience=60, val=True)

    result = {"model": "YOLO26l", "params_juta": 26.3, "config": vars(a),
              **evaluate(m, a.imgsz)}
    Path("results").mkdir(exist_ok=True)
    Path("results/yolo26l_eval.json").write_text(json.dumps(result, indent=2))
    v, t = result["val"], result["test"]
    print(f"YOLO26l val mAP50={v['mAP50']} mAP50-95={v['mAP50_95']} | "
          f"test mAP50={t['mAP50']} mAP50-95={t['mAP50_95']}")
    print("-> results/yolo26l_eval.json")


if __name__ == "__main__":
    main()
