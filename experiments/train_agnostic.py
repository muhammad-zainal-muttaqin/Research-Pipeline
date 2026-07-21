"""Tahap 1 dari detektor dua-tahap: deteksi tandan KELAS-AGNOSTIK.

Dasar (E-014): pada bobot 4-kelas yang sama, mAP50 agnostik 0,7191 vs 4-kelas
0,5218. Deteksi bukan hambatannya — klasifikasi kematangan yang menghancurkan
skor. Maka tahap 1 dilepaskan dari beban kematangan (single_cls) dan dilatih
pada resolusi lebih tinggi (960, native SawitMVC 960x1280) supaya lokalisasi
— yang menentukan mAP50-95 — ikut membaik.

Inisialisasi dari bobot RGB baseline yang sudah konvergen, bukan dari COCO:
backbone-nya sudah beradaptasi ke citra sawit, jadi cukup epoch pendek.
"""
import argparse
from ultralytics import YOLO

ap = argparse.ArgumentParser()
ap.add_argument("--weights", default="runs/rgb_e60_i640_s42/weights/best.pt")
ap.add_argument("--imgsz", type=int, default=960)
ap.add_argument("--epochs", type=int, default=25)
ap.add_argument("--batch", type=int, default=12)
ap.add_argument("--name", default="agn_e25_i960_s42")
a = ap.parse_args()

m = YOLO(a.weights)
m.train(data="data_rgb.yaml", single_cls=True, epochs=a.epochs, imgsz=a.imgsz,
        batch=a.batch, seed=42, name=a.name, project="/workspace/experiments/runs",
        exist_ok=True, lr0=0.004, cos_lr=True, close_mosaic=5, plots=False,
        patience=25, val=True)
r = m.val(data="data_rgb.yaml", split="val", imgsz=a.imgsz, batch=8,
          single_cls=True, plots=False, verbose=False)
print(f"AGNOSTIK val mAP50={float(r.box.map50):.4f} mAP50-95={float(r.box.map):.4f}")
