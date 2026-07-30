"""Jalur yang belum pernah diuji: detektor 4-KELAS pada resolusi asli dengan
augmentasi aman-warna.

Dua koreksi, keduanya menyerang tepat di tempat kerugian mAP berada (E-014:
38% mAP50 hilang di klasifikasi kematangan, bukan di deteksi):

1. AUGMENTASI AMAN-WARNA. Baseline memakai bawaan ultralytics hsv_s=0.7,
   hsv_v=0.4 — saturasi diacak sampai ±70% tiap batch. Kematangan sawit ADALAH
   warna: B1 MATANG (jingga-merah) → B4 MENTAH (gelap kehijauan). Resep bawaan
   itu mengacak persis bukti yang harus dipelajari, dan pengklasifikasi
   potongan di E-016 dilatih aman-warna sedangkan head YOLO tidak — jadi
   perbandingan plafon sebelumnya memang belum adil bagi head. Geometri tetap
   diacak bebas.

2. RESOLUSI 1280 = ASLI (SawitMVC 960×1280), jadi tidak ada piksel yang dibuang
   sama sekali. Pada 640 tandan bermedian 46–63 px; pada 1280 dua kali lipat.
   Deteksi agnostik sudah naik 0,7191 → 0,7730 hanya dengan 640→960, dan
   mAP50-95 — sasaran yang lebih berat — ditentukan oleh ketepatan lokalisasi,
   yang paling langsung dibayar oleh resolusi.

Diinisialisasi dari baseline yang sudah konvergen; jadwal penuh dengan kosinus.
"""
import argparse
from ultralytics import YOLO

ap = argparse.ArgumentParser()
ap.add_argument("--weights", default="runs/rgb_e60_i640_s42/weights/best.pt")
ap.add_argument("--imgsz", type=int, default=1280)
ap.add_argument("--epochs", type=int, default=50)
ap.add_argument("--batch", type=int, default=8)
ap.add_argument("--hsv-s", type=float, default=0.15)
ap.add_argument("--hsv-v", type=float, default=0.25)
ap.add_argument("--hsv-h", type=float, default=0.005)
ap.add_argument("--name", default="c4_e50_i1280_warna")
a = ap.parse_args()

m = YOLO(a.weights)
m.train(data="data_rgb.yaml", epochs=a.epochs, imgsz=a.imgsz, batch=a.batch,
        seed=42, name=a.name, project="/workspace/experiments/runs",
        exist_ok=True, lr0=0.006, cos_lr=True, close_mosaic=15,
        hsv_h=a.hsv_h, hsv_s=a.hsv_s, hsv_v=a.hsv_v,
        plots=False, patience=50, val=True)
r = m.val(data="data_rgb.yaml", split="val", imgsz=a.imgsz, batch=4,
          plots=False, verbose=False)
print(f"4KELAS val mAP50={float(r.box.map50):.4f} mAP50-95={float(r.box.map):.4f}")
