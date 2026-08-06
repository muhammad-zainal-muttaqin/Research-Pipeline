#!/usr/bin/env python3
"""E-022: evaluasi 1-protokol pycocotools untuk seluruh lengan RGB / RGB-D.

Menghapus caveat evaluator campur — semua model (ultralytics YOLO/RT-DETR dan
nanti RF-DETR) diprediksi pada daftar citra split yang SAMA, lalu dinilai oleh
COCOeval atas GT yang dibangun sekali dari label YOLO. Ini protokol yang sama
seperti E-021 (`eval_all_pycoco.py`), diadaptasi ke split per-pohon dataset
SawitMVC-Depth dan ke masukan 4-kanal.

Untuk lengan RGB-D, kanal ke-4 disusun di memori dari PNG depth kanonik
(`fourch.compose`) — tidak ada penyalinan dataset, dan urutan kanal [B,G,R,D]
persis sama dengan jalur latih.

Tambahan yang tidak ada di E-021: CI bootstrap 2000x yang di-resample per
POHON (bukan per citra), karena 4 sisi satu pohon tidak independen — resample
per citra membuat CI terlalu sempit.
"""
from __future__ import annotations

import argparse
import json
import sys
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
PIPELINE_ROOT = REPO_ROOT / "reproduce" / "pipeline"

import numpy as np
from PIL import Image
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

sys.path.insert(0, str(PIPELINE_ROOT))
import fourch  # noqa: E402

NAMES = ["B1", "B2", "B3", "B4"]
DEPTH_DIR = EVIDENCE_ROOT / "depth_png"


def pohon_dari(nama: str) -> str:
    return nama.rsplit("_", 1)[0]


def bangun_gt(paths: list[Path]) -> tuple[COCO, dict[str, int]]:
    images, anns, ann_id = [], [], 1
    peta = {}
    for img_id, p in enumerate(paths, 1):
        w, h = Image.open(p).size
        images.append({"id": img_id, "file_name": p.name, "width": w, "height": h})
        peta[p.stem] = img_id
        lf = Path(str(p).replace("/images/", "/labels/")).with_suffix(".txt")
        if lf.is_file():
            for baris in lf.read_text().splitlines():
                if not baris.strip():
                    continue
                c, cx, cy, bw, bh = map(float, baris.split())
                x, y, aw, ah = (cx - bw / 2) * w, (cy - bh / 2) * h, bw * w, bh * h
                anns.append({"id": ann_id, "image_id": img_id, "category_id": int(c) + 1,
                             "bbox": [x, y, aw, ah], "area": aw * ah, "iscrowd": 0})
                ann_id += 1
    gt = COCO()
    gt.dataset = {"images": images, "annotations": anns,
                  "categories": [{"id": i + 1, "name": n} for i, n in enumerate(NAMES)]}
    gt.createIndex()
    return gt, peta


def prediksi(bobot: str, paths: list[Path], peta: dict[str, int], imgsz: int,
             modal: str, chunk: int = 8, seed: int = 42) -> list[dict]:
    from ultralytics import RTDETR, YOLO
    import cv2

    Model = RTDETR if "rtdetr" in Path(bobot).parts[-3] else YOLO
    model = Model(bobot)
    dets = []
    for i in range(0, len(paths), chunk):
        potong = paths[i:i + chunk]
        if modal in ("rgbd", "derau", "tukar"):
            masukan = []
            for p in potong:
                bgr = cv2.imread(str(p), cv2.IMREAD_COLOR)
                if modal == "derau":
                    # kontrol negatif: kanal ke-4 derau, seed tetap agar
                    # evaluasi dapat direproduksi
                    # zlib.crc32, bukan hash(): hash() Python diacak per proses
                    # (PYTHONHASHSEED) sehingga deraunya tidak dapat direproduksi
                    # Harus identik dengan _patch_depth_acak saat training:
                    # pola tetap per berkas, tetapi berbeda antar-seed.
                    rng = np.random.default_rng(zlib.crc32(p.stem.encode()) ^ seed)
                    d8 = rng.integers(0, 256, bgr.shape[:2], dtype=np.uint8)
                elif modal == "tukar":
                    # Donor hanya dari split evaluasi yang sama dan pohon lain,
                    # identik dengan _patch_depth_tukar saat training.
                    urut = sorted(q.stem for q in paths)
                    i2 = urut.index(p.stem)
                    geser = max(4, len(urut) // 2)
                    lain = urut[(i2 + geser) % len(urut)]
                    for j in range(len(urut)):
                        if pohon_dari(lain) != pohon_dari(p.stem):
                            break
                        lain = urut[(i2 + geser + j + 1) % len(urut)]
                    if pohon_dari(lain) == pohon_dari(p.stem):
                        raise RuntimeError(f"donor tukar pohon lain tidak ditemukan untuk {p.stem}")
                    d8 = cv2.imread(str(DEPTH_DIR / f"{lain}.png"), cv2.IMREAD_GRAYSCALE)
                else:
                    d8 = fourch.load_depth_for(p, DEPTH_DIR)
                masukan.append(fourch.compose(bgr, d8))
        else:
            masukan = [str(p) for p in potong]
        hasil = model.predict(masukan, imgsz=imgsz, conf=0.001, iou=0.7,
                              max_det=300, verbose=False)
        for p, r in zip(potong, hasil):
            img_id = peta[p.stem]
            b = r.boxes
            if b is None or len(b) == 0:
                continue
            for kotak, skor, kelas in zip(b.xyxy.cpu().numpy(), b.conf.cpu().numpy(),
                                          b.cls.cpu().numpy()):
                x1, y1, x2, y2 = kotak
                dets.append({"image_id": img_id, "category_id": int(kelas) + 1,
                             "bbox": [float(x1), float(y1), float(x2 - x1), float(y2 - y1)],
                             "score": float(skor)})
    return dets


def coco_eval(gt: COCO, dets: list[dict], img_ids: list[int]) -> dict:
    if not dets:
        return {"mAP50": 0.0, "mAP50_95": 0.0, "AP50_perkelas": {n: 0.0 for n in NAMES}}
    dt = gt.loadRes(dets)
    ev = COCOeval(gt, dt, "bbox")
    ev.params.imgIds = img_ids
    ev.evaluate(); ev.accumulate(); ev.summarize()
    hasil = {"mAP50": float(ev.stats[1]), "mAP50_95": float(ev.stats[0])}
    perkelas = {}
    for i, n in enumerate(NAMES):
        e = COCOeval(gt, dt, "bbox")
        e.params.imgIds = img_ids
        e.params.catIds = [i + 1]
        e.evaluate(); e.accumulate(); e.summarize()
        perkelas[n] = float(e.stats[1])
    hasil["AP50_perkelas"] = perkelas
    return hasil


def bootstrap_pohon(gt: COCO, dets: list[dict], paths: list[Path], peta: dict[str, int],
                    B: int = 2000, seed: int = 42) -> dict:
    """CI bootstrap dengan resample per POHON — 4 sisi satu pohon tidak independen."""
    pohon = sorted({pohon_dari(p.stem) for p in paths})
    per_pohon = {t: [peta[p.stem] for p in paths if pohon_dari(p.stem) == t] for t in pohon}
    rng = np.random.default_rng(seed)
    nilai = []
    for _ in range(B):
        contoh = rng.choice(len(pohon), len(pohon), replace=True)
        ids = [i for k in contoh for i in per_pohon[pohon[k]]]
        try:
            nilai.append(coco_eval_diam(gt, dets, ids))
        except Exception:
            continue
    a = np.array(nilai)
    return {"mAP50_ci95": [float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5))],
            "mAP50_rerata_boot": float(a.mean()), "B": len(nilai)}


def coco_eval_diam(gt: COCO, dets: list[dict], img_ids: list[int]) -> float:
    import contextlib
    import io
    dt = gt.loadRes(dets)
    ev = COCOeval(gt, dt, "bbox")
    ev.params.imgIds = img_ids
    with contextlib.redirect_stdout(io.StringIO()):
        ev.evaluate(); ev.accumulate(); ev.summarize()
    return float(ev.stats[1])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True,
                    help="path folder run (berisi weights/best.pt dan hasil.json)")
    ap.add_argument("--split", default="test", choices=["val", "test"])
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--bootstrap", action="store_true")
    ap.add_argument("--keluaran", default="results/e022_pycoco.json")
    args = ap.parse_args()

    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    gt, peta = bangun_gt(paths)
    img_ids = [peta[p.stem] for p in paths]
    print(f"{args.split}: {len(paths)} citra, {len(gt.dataset['annotations'])} kotak GT, "
          f"{len({pohon_dari(p.stem) for p in paths})} pohon")

    keluaran = {}
    for run in args.runs:
        rd = Path(run)
        meta = json.loads((rd / "hasil.json").read_text()) if (rd / "hasil.json").is_file() else {}
        modal = meta.get("modal", "rgbd" if "rgbd" in rd.name else "rgb")
        bobot = str(rd / "weights" / "best.pt")
        print(f"\n=== {rd.name} (modal={modal}) ===")
        dets = prediksi(bobot, paths, peta, args.imgsz, modal,
                        seed=int(meta.get("seed", 42)))
        skor = coco_eval(gt, dets, img_ids)
        skor["modal"] = modal
        skor["n_deteksi"] = len(dets)
        if args.bootstrap:
            skor.update(bootstrap_pohon(gt, dets, paths, peta))
        keluaran[rd.name] = skor

    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(keluaran, indent=2))

    print(f"\n{'run':34s} {'mAP50':>8s} {'mAP50-95':>9s} " + " ".join(f"{n:>7s}" for n in NAMES))
    for k, v in keluaran.items():
        print(f"{k:34s} {v['mAP50']:8.4f} {v['mAP50_95']:9.4f} " +
              " ".join(f"{v['AP50_perkelas'][n]:7.4f}" for n in NAMES))
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
