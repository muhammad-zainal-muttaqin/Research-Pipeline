"""Apakah mAP50-95 0,30 secara geometris mungkin?

mAP50-95 merata-ratakan AP pada ambang IoU 0,50 sampai 0,95. Untuk mendapat
angka tinggi, sebagian besar deteksi harus cocok dengan kotak GT pada IoU >0,8.
Kalau kotak anotasi sendiri digambar longgar atau tidak konsisten, tidak ada
model yang bisa mencapainya — plafonnya ada pada labelnya, bukan pada modelnya.

Yang diukur: untuk tiap kotak GT, IoU tertinggi dengan deteksi mana pun (kelas
diabaikan, ambang keyakinan rendah). Ini plafon lokalisasi empiris detektor
sekarang. Distribusinya menunjukkan di mana mAP50-95 kehabisan napas:

  - Kalau banyak GT punya IoU terbaik 0,9+, lokalisasi bukan hambatan.
  - Kalau menumpuk di 0,7-0,85, mAP50-95 dijatah oleh ketepatan kotak.
"""
import json
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO


def iou_mat(a, b):
    if len(a) == 0 or len(b) == 0:
        return np.zeros((len(a), len(b)), np.float32)
    x0 = np.maximum(a[:, None, 0], b[None, :, 0]); y0 = np.maximum(a[:, None, 1], b[None, :, 1])
    x1 = np.minimum(a[:, None, 2], b[None, :, 2]); y1 = np.minimum(a[:, None, 3], b[None, :, 3])
    inter = np.clip(x1 - x0, 0, None) * np.clip(y1 - y0, 0, None)
    ar = lambda z: (z[:, 2] - z[:, 0]) * (z[:, 3] - z[:, 1])
    return inter / (ar(a)[:, None] + ar(b)[None, :] - inter + 1e-9)


paths = [l.strip() for l in open("splits_rgb/val.txt") if l.strip()]
runs = {
    "baseline_640": ("runs/rgb_e60_i640_s42/weights/best.pt", 640),
    "agnostik_960": ("runs/agn_e25_i960_s42/weights/best.pt", 960),
}
out = {}
for tag, (w, sz) in runs.items():
    det = YOLO(w)
    best = []
    for p in paths:
        im = cv2.imread(p)
        H, W = im.shape[:2]
        g = []
        for line in Path(p.replace("/images/", "/labels/")).with_suffix(".txt").read_text().split("\n"):
            f = line.split()
            if len(f) < 5:
                continue
            cx, cy, bw, bh = (float(v) for v in f[1:5])
            g.append([(cx-bw/2)*W, (cy-bh/2)*H, (cx+bw/2)*W, (cy+bh/2)*H])
        if not g:
            continue
        g = np.array(g, np.float32)
        r = det.predict(im, imgsz=sz, conf=0.05, max_det=300, verbose=False, device=0)[0]
        if r.boxes is None or not len(r.boxes):
            best += [0.0] * len(g)
            continue
        M = iou_mat(g, r.boxes.xyxy.cpu().numpy().astype(np.float32))
        best += list(M.max(1))
    b = np.array(best)
    out[tag] = {
        "n_gt": int(len(b)),
        "tak_terdeteksi_iou0": round(float((b < 0.01).mean()), 4),
        "median_iou_terbaik": round(float(np.median(b)), 4),
        "median_iou_yang_terdeteksi": round(float(np.median(b[b > 0.5])), 4) if (b > 0.5).any() else None,
        "pecahan_iou>=0.5": round(float((b >= 0.5).mean()), 4),
        "pecahan_iou>=0.75": round(float((b >= 0.75).mean()), 4),
        "pecahan_iou>=0.90": round(float((b >= 0.90).mean()), 4),
        # plafon mAP50-95 kalau SETIAP kotak yang ditemukan diberi kelas benar
        # dan skor sempurna: rerata pecahan-terdeteksi pada 10 ambang COCO
        "plafon_mAP50-95_kelas_sempurna": round(float(
            np.mean([(b >= t).mean() for t in np.arange(0.50, 0.96, 0.05)])), 4),
        "plafon_mAP50_kelas_sempurna": round(float((b >= 0.5).mean()), 4),
    }
    print(tag, json.dumps(out[tag], indent=1), flush=True)

Path("results").mkdir(exist_ok=True)
json.dump(out, open("results/loc_ceiling.json", "w"), indent=1)
