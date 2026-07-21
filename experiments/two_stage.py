"""I-23 — rakit dan nilai detektor dua tahap.

Tahap 1  deteksi kelas-agnostik (satu kelas "tandan").
Tahap 2  potong tiap kotak pada resolusi ASLI citra, klasifikasikan
         kematangannya, lalu skor tiap kelas = skor_objek x peluang_kelas.

Skor gabungan itu bukan pilihan gaya: mAP menilai peringkat, jadi tiap kotak
menyumbang ke keempat kelas dengan bobot peluangnya — persis cara detektor
dua-tahap klasik menilai. Menyimpan hanya argmax akan membuang informasi
peringkat dan menurunkan AP.

Evaluasi memakai pycocotools (definisi mAP standar COCO), bukan implementasi
sendiri, supaya angkanya bisa dibandingkan lurus dengan hasil ultralytics.
"""
import argparse, json, contextlib, io
from pathlib import Path

import cv2, numpy as np, torch, torch.nn as nn
from torchvision import transforms as T, models
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from ultralytics import YOLO

NAMES = ["B1", "B2", "B3", "B4"]
PAD = 0.25  # sama dengan build_crops.py — WAJIB sama, ini kontrak


def build_gt(img_paths):
    """Kebenaran dasar COCO dari label YOLO."""
    imgs, anns, aid = [], [], 1
    for i, p in enumerate(img_paths):
        im = cv2.imread(str(p))
        H, W = im.shape[:2]
        imgs.append({"id": i, "file_name": Path(p).name, "width": W, "height": H})
        lab = Path(str(p).replace("/images/", "/labels/")).with_suffix(".txt")
        if not lab.exists():
            continue
        for line in lab.read_text().split("\n"):
            f = line.split()
            if len(f) < 5:
                continue
            c = int(f[0]); cx, cy, bw, bh = (float(v) for v in f[1:5])
            x, y, w, h = (cx - bw / 2) * W, (cy - bh / 2) * H, bw * W, bh * H
            anns.append({"id": aid, "image_id": i, "category_id": c,
                         "bbox": [x, y, w, h], "area": w * h, "iscrowd": 0})
            aid += 1
    return {"images": imgs, "annotations": anns,
            "categories": [{"id": i, "name": n} for i, n in enumerate(NAMES)]}


_RAWMAP = None


def raw_image_for(mvc_path):
    """Citra master 3024x4032 yang sepadan, lewat peta isi dari E-015."""
    global _RAWMAP
    if _RAWMAP is None:
        _RAWMAP = json.load(open("results/raw_map.json"))["peta"]
    e = _RAWMAP.get(Path(mvc_path).name)
    if e is None:
        return None
    im = cv2.imread(str(Path("/workspace/Sawit/data") / e["raw"]))
    if im is not None and im.shape[0] < im.shape[1]:
        im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
    return im


def load_classifier(path, size, dev):
    m = models.convnext_tiny(weights=None)
    m.classifier[2] = nn.Linear(768, 4)
    m.load_state_dict(torch.load(path, map_location="cpu"))
    m.to(dev).eval()
    tf = T.Compose([T.ToTensor(),
                    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    return m, tf


def crops_from(im, boxes, size):
    """Potongan dengan konteks 25%, ditata persis seperti transformasi eval
    pengklasifikasi (Resize sisi pendek -> CenterCrop)."""
    H, W = im.shape[:2]
    out = []
    for x0, y0, x1, y1 in boxes:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        w, h = (x1 - x0) * (1 + 2 * PAD), (y1 - y0) * (1 + 2 * PAD)
        a = max(0, int(cx - w / 2)); b = max(0, int(cy - h / 2))
        c = min(W, int(cx + w / 2)); d = min(H, int(cy + h / 2))
        cr = im[b:max(d, b + 2), a:max(c, a + 2)]
        ch, cw = cr.shape[:2]
        s = int(size * 1.14) / min(ch, cw)
        cr = cv2.resize(cr, (max(1, int(round(cw * s))), max(1, int(round(ch * s)))),
                        interpolation=cv2.INTER_LINEAR)
        ch, cw = cr.shape[:2]
        y = max(0, (ch - size) // 2); x = max(0, (cw - size) // 2)
        cr = cr[y:y + size, x:x + size]
        if cr.shape[0] != size or cr.shape[1] != size:
            cr = cv2.resize(cr, (size, size))
        out.append(cv2.cvtColor(cr, cv2.COLOR_BGR2RGB))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--det", default="runs/agn_e25_i960_s42/weights/best.pt")
    ap.add_argument("--cls", default="runs/maturity/best.pt")
    ap.add_argument("--split", default="val")
    ap.add_argument("--imgsz", type=int, default=960)
    ap.add_argument("--size", type=int, default=224)
    ap.add_argument("--conf", type=float, default=0.01)
    ap.add_argument("--pmin", type=float, default=0.02)
    ap.add_argument("--max-det", type=int, default=300)
    ap.add_argument("--tag", default="")
    ap.add_argument("--tta", action="store_true")
    ap.add_argument("--crop-source", choices=["mvc", "raw"], default="mvc")
    a = ap.parse_args()

    dev = "cuda"
    paths = [l.strip() for l in open(f"splits_rgb/{a.split}.txt") if l.strip()]
    gt = build_gt(paths)
    det_model = YOLO(a.det)
    clfs, tf = [], None
    for w in a.cls.split(","):
        m, tf = load_classifier(w.strip(), a.size, dev)
        clfs.append(m)
    print(f"{len(clfs)} pengklasifikasi | TTA={a.tta} | potongan dari "
          f"{'master mentah' if a.crop_source == 'raw' else 'MVC'}", flush=True)

    dets = []
    for i, p in enumerate(paths):
        im = cv2.imread(str(p))
        r = det_model.predict(im, imgsz=a.imgsz, conf=a.conf, iou=0.7,
                              max_det=a.max_det, verbose=False, device=0)[0]
        if r.boxes is None or len(r.boxes) == 0:
            continue
        xyxy = r.boxes.xyxy.cpu().numpy()
        sc = r.boxes.conf.cpu().numpy()
        src, bx = im, xyxy
        if a.crop_source == "raw":
            rim = raw_image_for(p)
            if rim is not None:
                sx, sy = rim.shape[1] / im.shape[1], rim.shape[0] / im.shape[0]
                src = rim
                bx = xyxy * np.array([sx, sy, sx, sy], np.float32)
        cr = crops_from(src, bx, a.size)
        with torch.no_grad():
            batch = torch.stack([tf(c) for c in cr]).to(dev)
            views = [batch]
            if a.tta:
                views += [torch.flip(batch, [3]), torch.flip(batch, [2])]
            acc = 0
            for model in clfs:
                for v in views:
                    ps = []
                    for k in range(0, len(v), 128):
                        with torch.autocast("cuda", torch.bfloat16):
                            ps.append(model(v[k:k + 128]).float().softmax(1).cpu())
                    acc = acc + torch.cat(ps)
            probs = (acc / (len(clfs) * len(views))).numpy()
        for (x0, y0, x1, y1), s, pr in zip(xyxy, sc, probs):
            for c in range(4):
                if pr[c] < a.pmin:
                    continue
                dets.append({"image_id": i, "category_id": c,
                             "bbox": [float(x0), float(y0), float(x1 - x0), float(y1 - y0)],
                             "score": float(s * pr[c])})
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(paths)}", flush=True)

    with contextlib.redirect_stdout(io.StringIO()):
        coco = COCO(); coco.dataset = gt; coco.createIndex()
        dt = coco.loadRes(dets)
        e = COCOeval(coco, dt, "bbox"); e.evaluate(); e.accumulate(); e.summarize()
    res = {"split": a.split, "n_citra": len(paths), "n_deteksi": len(dets),
           "mAP50-95": round(float(e.stats[0]), 4), "mAP50": round(float(e.stats[1]), 4),
           "mAP75": round(float(e.stats[2]), 4)}
    per = {}
    for c in range(4):
        e2 = COCOeval(coco, dt, "bbox"); e2.params.catIds = [c]
        with contextlib.redirect_stdout(io.StringIO()):
            e2.evaluate(); e2.accumulate(); e2.summarize()
        per[NAMES[c]] = {"AP50": round(float(e2.stats[1]), 4),
                         "AP50-95": round(float(e2.stats[0]), 4)}
    res["per_kelas"] = per
    print(json.dumps(res, indent=1))
    Path("results").mkdir(exist_ok=True)
    json.dump(res, open(f"results/two_stage_{a.split}{a.tag}.json", "w"), indent=1)


if __name__ == "__main__":
    main()
