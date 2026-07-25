"""Ide I-14 — RT-DETR sebagai detektor NMS-free.

Alasan dari korpus (deep-research-report.md, prioritas 1): NMS sering menjadi
plafon STRUKTURAL pada objek rapat/bertumpuk. Tandan sawit di mahkota persis
kondisi itu — banyak tandan berdekatan, saling menutup sebagian. YOLO memakai
NMS greedy yang, saat dua tandan tumpang tindih, dapat menekan salah satu kotak
benar. RT-DETR memakai pencocokan Hungarian satu-ke-satu (tanpa NMS), jadi
kalau plafon deteksi kita sebagian berasal dari NMS, RT-DETR mengangkatnya.

Ini BUKAN varian YOLO yang lebih besar — arsitektur decoder transformer yang
berbeda kelas. Karena itu ia menguji hipotesis yang berbeda dari yolo26x
(kapasitas): apakah MEKANISME penindasan kotak yang membatasi, bukan kapasitas.

Augmentasi tetap aman-warna (kematangan = warna, lihat E-019). Resolusi 1280
asli. Dilatih dari bobot COCO RT-DETR.
"""
import argparse
from ultralytics import RTDETR

ap = argparse.ArgumentParser()
ap.add_argument("--weights", default="rtdetr-l.pt")
ap.add_argument("--imgsz", type=int, default=1280)
ap.add_argument("--epochs", type=int, default=60)
ap.add_argument("--batch", type=int, default=4)
ap.add_argument("--name", default="rtdetr_l_e60_i1280")
a = ap.parse_args()

m = RTDETR(a.weights)
m.train(data="data_rgb.yaml", epochs=a.epochs, imgsz=a.imgsz, batch=a.batch,
        seed=42, name=a.name, project="/workspace/experiments/runs",
        exist_ok=True, cos_lr=True,
        hsv_h=0.005, hsv_s=0.15, hsv_v=0.25,
        plots=False, patience=60, val=True)
r = m.val(data="data_rgb.yaml", split="val", imgsz=a.imgsz, batch=2,
          plots=False, verbose=False)
print(f"RTDETR-L val mAP50={float(r.box.map50):.4f} mAP50-95={float(r.box.map):.4f}")
for i, n in enumerate(["B1", "B2", "B3", "B4"]):
    print(f"  {n} AP50={float(r.box.ap50[i]):.4f}")
