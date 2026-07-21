"""mAP di bawah beberapa perumusan tugas, dari SATU set prediksi yang sama.

Alasan: tiga pengukuran bebas (head YOLO, CNN potongan master, voting
multi-sisi) sama-sama berhenti di ~68% akurasi kematangan, dan 100% kesalahan
head YOLO hanya meleset satu tingkat. Kalau begitu, sebagian dari yang dihukum
oleh mAP 4-kelas adalah ambiguitas yang melekat pada labelnya — bukan
kekurangan model. Yang perlu diketahui: BERAPA bagiannya.

Varian yang dihitung:
  4kelas     apa adanya (definisi sekarang)
  agnostik   semua kotak satu kelas "tandan" (deteksi murni)
  B2B3       B2 dan B3 digabung (SR-009: kebingungannya ordinal & terbesar
             justru di pasangan ini)
  pm1        toleransi satu tingkat — mencerminkan metrik deployment DiB
             `Class +-1 Acc`, yang MEMANG sudah memaafkan geser satu kelas
"""
import contextlib, io, json
from pathlib import Path
import numpy as np, cv2
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from ultralytics import YOLO

NAMES = ["B1", "B2", "B3", "B4"]
paths = [l.strip() for l in open("splits_rgb/val.txt") if l.strip()]
det = YOLO("runs/rgb_e60_i640_s42/weights/best.pt")

imgs, anns, dets, aid = [], [], [], 1
for i, p in enumerate(paths):
    im = cv2.imread(p); H, W = im.shape[:2]
    imgs.append({"id": i, "file_name": Path(p).name, "width": W, "height": H})
    lab = Path(p.replace("/images/", "/labels/")).with_suffix(".txt")
    for line in lab.read_text().split("\n"):
        f = line.split()
        if len(f) < 5:
            continue
        c = int(f[0]); cx, cy, bw, bh = (float(v) for v in f[1:5])
        anns.append({"id": aid, "image_id": i, "category_id": c,
                     "bbox": [(cx-bw/2)*W, (cy-bh/2)*H, bw*W, bh*H],
                     "area": bw*W*bh*H, "iscrowd": 0}); aid += 1
    r = det.predict(im, imgsz=640, conf=0.01, max_det=300, verbose=False, device=0)[0]
    if r.boxes is None or not len(r.boxes):
        continue
    for b, s, c in zip(r.boxes.xyxy.cpu().numpy(), r.boxes.conf.cpu().numpy(),
                       r.boxes.cls.cpu().numpy()):
        dets.append({"image_id": i, "category_id": int(c),
                     "bbox": [float(b[0]), float(b[1]), float(b[2]-b[0]), float(b[3]-b[1])],
                     "score": float(s)})
print(f"{len(anns)} kotak GT, {len(dets)} deteksi", flush=True)


def run(remap, ncat, tag):
    A = [dict(a, category_id=remap[a["category_id"]]) for a in anns]
    D = [dict(d, category_id=remap[d["category_id"]]) for d in dets]
    with contextlib.redirect_stdout(io.StringIO()):
        c = COCO(); c.dataset = {"images": imgs, "annotations":
                                 [dict(a, id=k+1) for k, a in enumerate(A)],
                                 "categories": [{"id": i, "name": str(i)} for i in range(ncat)]}
        c.createIndex(); dt = c.loadRes(D)
        e = COCOeval(c, dt, "bbox"); e.evaluate(); e.accumulate(); e.summarize()
    return {"mAP50": round(float(e.stats[1]), 4), "mAP50-95": round(float(e.stats[0]), 4)}


res = {
    "4kelas":   run({0: 0, 1: 1, 2: 2, 3: 3}, 4, "4kelas"),
    "agnostik": run({0: 0, 1: 0, 2: 0, 3: 0}, 1, "agnostik"),
    "B2B3":     run({0: 0, 1: 1, 2: 1, 3: 2}, 3, "B2+B3 digabung"),
}
# pm1: kotak GT diduplikasi ke kelas tetangga, meniru toleransi satu tingkat
A2, k = [], 1
for a in anns:
    for c in {max(0, a["category_id"]-1), a["category_id"], min(3, a["category_id"]+1)}:
        A2.append(dict(a, category_id=c, id=k)); k += 1
with contextlib.redirect_stdout(io.StringIO()):
    c = COCO(); c.dataset = {"images": imgs, "annotations": A2,
                             "categories": [{"id": i, "name": NAMES[i]} for i in range(4)]}
    c.createIndex(); dt = c.loadRes(dets)
    e = COCOeval(c, dt, "bbox"); e.evaluate(); e.accumulate(); e.summarize()
res["pm1_toleransi"] = {"mAP50": round(float(e.stats[1]), 4),
                        "mAP50-95": round(float(e.stats[0]), 4)}
print(json.dumps(res, indent=1))
json.dump(res, open("results/metric_variants.json", "w"), indent=1)
