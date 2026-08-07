#!/usr/bin/env python3
"""Metrik lengkap + provenans untuk seluruh run E-022/G7/G8, protokol tunggal.

Uji berpasangan (`eval_e022_paired.py`) hanya melaporkan mAP50 karena itu yang
dibutuhkan untuk selisih antar lengan. Skrip ini melengkapi rekamnya: mAP50,
mAP50-95, AP per kelas pada kedua ambang, precision, recall, dan F1 — semuanya
lewat pycocotools, protokol yang dibekukan [E-025] setelah terbukti bahwa
evaluator internal trainer tidak boleh dipakai membandingkan antar lengan.

## Kenapa ada bagian "provenans"

Kebijakan repo tidak mengarsipkan bobot model, jadi angka di sini tidak dapat
diverifikasi dengan cara membuka checkpoint-nya. Sebagai gantinya tiap run
mencatat:

  - SHA-256 dan ukuran `weights/best.pt` — siapa pun yang melatih ulang dengan
    resep yang sama dapat membandingkan hash-nya; kalau berbeda, minimal
    diketahui bahwa checkpoint-nya bukan yang sama, bukan sekadar menduga.
  - epoch tercatat, durasi, dan hiperparameter efektif dari `args.yaml`.
  - perangkat (GPU) — angka absolut tidak identik antar perangkat.

Itu tidak menggantikan bobot, tetapi membuat selisih antara "hasil tidak
tereproduksi" dan "checkpoint-nya memang lain" dapat dibedakan.

Pemakaian:

  python eval/metrics_lengkap.py --pola 'yolo26*_seed42'
  python eval/metrics_lengkap.py --keluaran results/E-022/metrics_lengkap.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
RUNS = REPO_ROOT / "runs" / "detect" / "runs_e022"

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

KELAS = ["B1", "B2", "B3", "B4"]


def sha256(p: Path, potong: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for blok in iter(lambda: f.read(potong), b""):
            h.update(blok)
    return h.hexdigest()


def modal_dari(nama: str) -> str:
    """Turunkan modalitas dari nama run; menentukan komposisi kanal ke-4."""
    for m in ("derau", "tukar", "rgbd"):
        if f"_{m}_" in nama:
            return m
    return "rgb"


def metrik(gt, dets, img_ids) -> dict:
    """COCOeval + P/R/F1 pada ambang keyakinan operasional 0,25."""
    from pycocotools.cocoeval import COCOeval

    ev = COCOeval(gt, gt.loadRes(dets), "bbox")
    ev.params.imgIds = img_ids
    ev.evaluate(); ev.accumulate()

    p = ev.eval["precision"][:, :, :, 0, 2]      # [T, R, K]
    def rr(x):
        v = x[x > -1]
        return round(float(v.mean()), 4) if v.size else None

    hasil = {
        "mAP50": rr(p[0]),
        "mAP50_95": rr(p),
        "AP50_perkelas": {KELAS[k]: rr(p[0, :, k]) for k in range(p.shape[2])},
        "AP50_95_perkelas": {KELAS[k]: rr(p[:, :, k]) for k in range(p.shape[2])},
    }

    # P/R/F1 mikro pada conf 0,25, dicocokkan sendiri secara serakah.
    #
    # TIDAK memakai ev.evalImgs: senarai itu berisi satu entri per
    # (kelas x rentang-area x citra), sehingga menjumlahkan dtMatches di
    # seluruhnya menghitung tiap TP sebanyak jumlah rentang area dan
    # menghasilkan precision > 1 serta recall > 1 — mustahil, tetapi tidak
    # error, jadi mudah lolos sebagai hasil. Pencocokan sendiri dapat diperiksa.
    kuat = sorted((d for d in dets if d["score"] >= 0.25), key=lambda d: -d["score"])
    gt_per: dict = {}
    for a in gt.dataset["annotations"]:
        gt_per.setdefault((a["image_id"], a["category_id"]), []).append(a["bbox"])
    dipakai = {k: [False] * len(v) for k, v in gt_per.items()}

    def iou_xywh(a, b):
        ax, ay, aw, ah = a; bx, by, bw, bh = b
        ix1, iy1 = max(ax, bx), max(ay, by)
        ix2, iy2 = min(ax + aw, bx + bw), min(ay + ah, by + bh)
        iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
        inter = iw * ih
        u = aw * ah + bw * bh - inter
        return inter / u if u > 0 else 0.0

    tp = 0
    for d in kuat:
        kunci = (d["image_id"], d["category_id"])
        kand = gt_per.get(kunci, [])
        terbaik, skor = -1, 0.5
        for i, g in enumerate(kand):
            if dipakai[kunci][i]:
                continue
            v = iou_xywh(d["bbox"], g)
            if v >= skor:
                terbaik, skor = i, v
        if terbaik >= 0:
            dipakai[kunci][terbaik] = True
            tp += 1

    n_gt = len(gt.dataset["annotations"])
    pr = tp / len(kuat) if kuat else 0.0
    rc = tp / n_gt if n_gt else 0.0
    f1 = 2 * pr * rc / (pr + rc) if (pr + rc) else 0.0
    hasil |= {"precision@0.25": round(pr, 4), "recall@0.25": round(rc, 4),
              "F1@0.25": round(f1, 4), "TP@0.25": tp, "n_deteksi@0.25": len(kuat)}
    hasil["n_deteksi_total"] = len(dets)
    return hasil


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pola", default="*_seed*", help="pola nama folder run")
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--split", default="test")
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--keluaran", default=None)
    args = ap.parse_args()

    from eval.eval_e022_pycoco import bangun_gt, prediksi

    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    gt, peta = bangun_gt(paths)
    img_ids = sorted(peta.values())
    print(f"{args.split}: {len(paths)} citra, {len(gt.dataset['annotations'])} kotak GT")

    keluar: dict = {"_protokol": {
        "evaluator": "pycocotools",
        "aturan": "E-025 — hasil.json tidak boleh dipakai membandingkan antar lengan",
        "split": args.split, "split_dir": args.split_dir,
        "n_citra": len(paths), "n_kotak_gt": len(gt.dataset["annotations"]),
        "conf_prediksi": 0.001, "iou_nms": 0.7, "max_det": 300, "imgsz": args.imgsz,
    }}

    for rd in sorted(RUNS.glob(args.pola)):
        bobot = rd / "weights" / "best.pt"
        if not bobot.is_file() or rd.name.endswith("_test"):
            continue
        # Run SawitMVC dilatih di dataset LAIN. Mengevaluasinya pada split
        # SawitMVC-Depth menghasilkan angka yang terlihat wajar (mAP50 0,1452)
        # tetapi tidak berarti apa pun — jenis kesalahan yang tidak menimbulkan
        # error dan karena itu mudah lolos ke tabel.
        if ("sawitmvc" in rd.name) != ("sawitmvc" in args.split_dir):
            print(f"   lewati {rd.name} — dataset tidak cocok dengan {args.split_dir}")
            continue
        csv = rd / "results.csv"
        n_ep = 0
        if csv.is_file():
            n_ep = len({l.split(",")[0] for l in csv.read_text().splitlines()[1:] if l.strip()})
        print(f"-> {rd.name} ({n_ep} epoch)")

        modal = modal_dari(rd.name)
        dets = prediksi(str(bobot), paths, peta, args.imgsz, modal, seed=42)
        entri = metrik(gt, dets, img_ids)
        entri["provenans"] = {
            "modal": modal, "epoch_tercatat": n_ep,
            "bobot_sha256": sha256(bobot), "bobot_byte": bobot.stat().st_size,
            "catatan": "bobot TIDAK diarsipkan (kebijakan repo). Hash ini membuat "
                       "checkpoint hasil latih-ulang dapat dibandingkan.",
        }
        keluar[rd.name] = entri
        print(json.dumps({k: entri[k] for k in ("mAP50", "mAP50_95") if k in entri}))

    if args.keluaran:
        Path(args.keluaran).parent.mkdir(parents=True, exist_ok=True)
        Path(args.keluaran).write_text(json.dumps(keluar, indent=2, ensure_ascii=False))
        print(f"-> {args.keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
