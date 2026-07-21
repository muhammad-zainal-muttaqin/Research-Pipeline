"""Kenaikan kapasitas: yolo26x (59,0 juta parameter) pada resolusi asli 1280
dengan augmentasi aman-warna.

Baseline memakai yolo26m (21,9 juta) pada 640 dengan hsv_s=0.7. Tiga hal
diubah sekaligus dan itu disengaja — sasarannya angka, bukan ablasi; ablasi
dua faktornya sudah dijalankan terpisah (E-019: 1280 + aman-warna pada
yolo26m).

Dilatih dari bobot COCO, bukan dari baseline kita: arsitekturnya berbeda,
jadi transfer bobot tidak berlaku. Karena itu jadwalnya penuh.
"""
import argparse
from ultralytics import YOLO

ap = argparse.ArgumentParser()
ap.add_argument("--weights", default="yolo26x.pt")
ap.add_argument("--imgsz", type=int, default=1280)
ap.add_argument("--epochs", type=int, default=60)
ap.add_argument("--batch", type=int, default=4)
ap.add_argument("--name", default="x_e60_i1280_warna")
a = ap.parse_args()

m = YOLO(a.weights)
m.train(data="data_rgb.yaml", epochs=a.epochs, imgsz=a.imgsz, batch=a.batch,
        seed=42, name=a.name, project="/workspace/experiments/runs",
        exist_ok=True, lr0=0.01, cos_lr=True, close_mosaic=15,
        hsv_h=0.005, hsv_s=0.15, hsv_v=0.25,
        plots=False, patience=60, val=True)
r = m.val(data="data_rgb.yaml", split="val", imgsz=a.imgsz, batch=2,
          plots=False, verbose=False)
print(f"YOLO26X val mAP50={float(r.box.map50):.4f} mAP50-95={float(r.box.map):.4f}")
