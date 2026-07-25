"""Perbandingan setara: pada KOTAK YANG SAMA, siapa yang lebih baik menilai
kematangan — head klasifikasi YOLO, atau pengklasifikasi potongan?

Rasio mAP bukan perbandingan yang adil (mAP mencampur deteksi, peringkat, dan
ambang). Di sini keduanya dinilai pada tugas identik: diberi kotak kebenaran
dasar, tebak kelasnya.

  - Head YOLO   : jalankan detektor, pasangkan deteksi ke kotak GT (IoU>=0.5),
                  ambil kelas yang diprediksi pada pasangan itu.
  - Pengklasifikasi potongan : klasifikasikan potongan GT yang sama.
"""
import json
from collections import defaultdict
from pathlib import Path
import numpy as np, cv2, torch, torch.nn as nn
from torchvision import transforms as T, models
from ultralytics import YOLO

NAMES = ["B1", "B2", "B3", "B4"]


def iou_mat(a, b):
    if len(a) == 0 or len(b) == 0:
        return np.zeros((len(a), len(b)))
    x0 = np.maximum(a[:, None, 0], b[None, :, 0]); y0 = np.maximum(a[:, None, 1], b[None, :, 1])
    x1 = np.minimum(a[:, None, 2], b[None, :, 2]); y1 = np.minimum(a[:, None, 3], b[None, :, 3])
    inter = np.clip(x1 - x0, 0, None) * np.clip(y1 - y0, 0, None)
    ar = lambda z: (z[:, 2] - z[:, 0]) * (z[:, 3] - z[:, 1])
    return inter / (ar(a)[:, None] + ar(b)[None, :] - inter + 1e-9)


def stats(pairs, tag):
    p = np.array(pairs)
    acc = float((p[:, 0] == p[:, 1]).mean())
    pm1 = float((np.abs(p[:, 0] - p[:, 1]) <= 1).mean())
    rec = {}
    for c in range(4):
        m = p[:, 1] == c
        rec[NAMES[c]] = round(float((p[m, 0] == c).mean()), 4) if m.sum() else None
    bal = float(np.mean([v for v in rec.values() if v is not None]))
    print(f"{tag}: n={len(p)} akurasi={acc:.4f} seimbang={bal:.4f} pm1={pm1:.4f} {rec}")
    return {"n": len(p), "akurasi": round(acc, 4), "seimbang": round(bal, 4),
            "pm1": round(pm1, 4), "recall": rec}


paths = [l.strip() for l in open("splits_rgb/val.txt") if l.strip()]
det = YOLO("runs/rgb_e60_i640_s42/weights/best.pt")

dev = "cuda"
clf = models.convnext_tiny(weights=None); clf.classifier[2] = nn.Linear(768, 4)
clf.load_state_dict(torch.load("runs/maturity/best.pt", map_location="cpu"))
clf.to(dev).eval()
tf = T.Compose([T.ToTensor(), T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
PAD = 0.25

head_pairs, crop_pairs = [], []
for p in paths:
    im = cv2.imread(p); H, W = im.shape[:2]
    lab = Path(p.replace("/images/", "/labels/")).with_suffix(".txt")
    g, gc = [], []
    for line in lab.read_text().split("\n"):
        f = line.split()
        if len(f) < 5:
            continue
        c = int(f[0]); cx, cy, bw, bh = (float(v) for v in f[1:5])
        g.append([(cx - bw/2)*W, (cy - bh/2)*H, (cx + bw/2)*W, (cy + bh/2)*H]); gc.append(c)
    if not g:
        continue
    g = np.array(g); gc = np.array(gc)

    r = det.predict(im, imgsz=640, conf=0.25, verbose=False, device=0)[0]
    if r.boxes is not None and len(r.boxes):
        db = r.boxes.xyxy.cpu().numpy(); dc = r.boxes.cls.cpu().numpy().astype(int)
        M = iou_mat(db, g)
        for i in range(len(db)):
            j = int(M[i].argmax())
            if M[i, j] >= 0.5:
                head_pairs.append((dc[i], gc[j]))

    crops = []
    for (x0, y0, x1, y1) in g:
        cx, cy = (x0+x1)/2, (y0+y1)/2; w, h = (x1-x0)*(1+2*PAD), (y1-y0)*(1+2*PAD)
        a_ = max(0, int(cx-w/2)); b_ = max(0, int(cy-h/2))
        c_ = min(W, int(cx+w/2)); d_ = min(H, int(cy+h/2))
        cr = im[b_:max(d_, b_+2), a_:max(c_, a_+2)]
        cr = cv2.resize(cr, (224, 224), interpolation=cv2.INTER_AREA)
        crops.append(tf(cv2.cvtColor(cr, cv2.COLOR_BGR2RGB)))
    with torch.no_grad(), torch.autocast("cuda", torch.bfloat16):
        pr = clf(torch.stack(crops).to(dev)).float().softmax(1).cpu().numpy()
    for k in range(len(g)):
        crop_pairs.append((int(pr[k].argmax()), int(gc[k])))

out = {"head_yolo": stats(head_pairs, "head YOLO (deteksi cocok IoU>=0.5)"),
       "potongan": stats(crop_pairs, "pengklasifikasi potongan (kotak GT)")}
json.dump(out, open("results/head_vs_crop.json", "w"), indent=1)
