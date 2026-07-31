#!/usr/bin/env python3
"""E-022 G1: melacak selisih evaluator `hasil.json` vs pycocotools.

AUDIT-E022 mencatat selisih sampai 0,028 yang **tidak simetris antar lengan** —
`hasil.json` merugikan lengan RGB+D secara sistematis, sehingga rerata delta
YOLO26n berubah tanda: -0,0060 (hasil.json) versus +0,0059 (pycocotools).
Selama penyebabnya belum diketahui, tidak ada angka E-022 yang berstatus final.

Audit mendaftar empat kandidat: pemilihan checkpoint (best vs last), ambang
confidence, `max_det`, dan perbedaan daftar citra. Pembacaan kode 31 Juli 2026
sudah menggugurkan dua di antaranya secara statis:

  - Daftar citra: `data_rgb.yaml` dan `data_rgbd4.yaml` menunjuk `test.txt`
    yang SAMA; satu-satunya beda adalah `channels: 3` vs `4`.
  - Checkpoint: kedua jalur memuat `weights/best.pt`
    (`eval_e022_pycoco.py` eksplisit; trainer memanggil `model.val()` setelah
    `model.train()`, dan ultralytics memuat ulang `best` ke `self.model` di
    akhir `train()`). Skrip ini tetap MEMVERIFIKASI itu, tidak mengasumsikannya.

Dan menambahkan satu kandidat yang TIDAK ada di daftar audit:

  - `maxDets`. Tidak satu pun skrip menyetel `ev.params.maxDets`, jadi COCOeval
    memakai default `[1, 10, 100]` dan AP dihitung pada 100 deteksi teratas,
    sementara prediksi dibuat dengan `max_det=300`. Efeknya tidak netral antar
    lengan bila kedua lengan menghasilkan jumlah deteksi berbeda.

Rancangan: satu himpunan deteksi dipakai untuk SEMUA pengukuran, sehingga
tiap sumber selisih terisolasi satu per satu. Kalau ultralytics dan pycocotools
berbeda pada deteksi yang identik, sisa selisih adalah murni implementasi AP.

Pemakaian (dijalankan di mesin yang punya `runs_e022/`):

  python eval/diag_evaluator_gap.py \
      --run runs/detect/runs_e022/yolo26n_rgbd_seed42 --modal rgbd \
      --keluaran ../../evidence/experiments/results/E-022/diag_evaluator_gap.json

Jalankan untuk KEDUA lengan satu pasangan (rgb dan rgbd); asimetrilah yang
menjadi bukti, bukan angka satu lengan.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from eval.eval_e022_pycoco import bangun_gt, prediksi  # noqa: E402


def ap_pycoco(gt, dets: list[dict], img_ids: list[int], max_dets: int) -> dict:
    """AP lewat pycocotools pada `max_dets` deteksi teratas per citra."""
    from pycocotools.cocoeval import COCOeval

    ev = COCOeval(gt, gt.loadRes(dets), "bbox")
    ev.params.imgIds = img_ids
    ev.params.maxDets = [1, 10, max_dets]
    ev.evaluate()
    ev.accumulate()
    ev.summarize()
    return {"mAP50": float(ev.stats[1]), "mAP50_95": float(ev.stats[0])}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="folder run (berisi weights/best.pt, hasil.json)")
    ap.add_argument("--modal", default="rgb", choices=["rgb", "rgbd", "derau", "tukar"])
    ap.add_argument("--split", default="test", choices=["val", "test"])
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--keluaran", default=None)
    args = ap.parse_args()

    rd = Path(args.run)
    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    gt, peta = bangun_gt(paths)
    img_ids = sorted(peta.values())

    lap: dict = {"run": str(rd), "modal": args.modal, "split": args.split,
                 "n_citra": len(paths), "n_kotak_gt": len(gt.dataset["annotations"])}

    # --- kandidat A: checkpoint yang sebenarnya dinilai --------------------
    hasil_json = rd / "hasil.json"
    lap["hasil_json"] = json.loads(hasil_json.read_text())["test"] if hasil_json.exists() else None
    bobot = rd / "weights" / "best.pt"
    lap["checkpoint"] = {
        "best_ada": bobot.exists(),
        "last_ada": (rd / "weights" / "last.pt").exists(),
        "bobot_tercatat_di_hasil_json": (
            json.loads(hasil_json.read_text()).get("bobot") if hasil_json.exists() else None),
        "bobot_dipakai_skrip_ini": str(bobot),
    }

    # --- satu himpunan deteksi untuk semua pengukuran ----------------------
    dets = prediksi(str(bobot), paths, peta, args.imgsz, args.modal, seed=args.seed)
    per_citra: dict[int, int] = {}
    for d in dets:
        per_citra[d["image_id"]] = per_citra.get(d["image_id"], 0) + 1
    jumlah = sorted(per_citra.values(), reverse=True)
    lap["deteksi"] = {
        "total": len(dets),
        "rerata_per_citra": round(len(dets) / max(1, len(paths)), 2),
        "maks_per_citra": jumlah[0] if jumlah else 0,
        "citra_lebih_dari_100_deteksi": sum(1 for v in jumlah if v > 100),
        "citra_lebih_dari_300_deteksi": sum(1 for v in jumlah if v > 300),
    }

    # --- kandidat B: maxDets 100 (default COCOeval) vs 300 (max_det predict)
    lap["pycoco_maxdets_100"] = ap_pycoco(gt, dets, img_ids, 100)
    lap["pycoco_maxdets_300"] = ap_pycoco(gt, dets, img_ids, 300)
    lap["efek_maxdets"] = {
        k: round(lap["pycoco_maxdets_300"][k] - lap["pycoco_maxdets_100"][k], 6)
        for k in ("mAP50", "mAP50_95")}

    # --- kandidat C: implementasi AP, pada deteksi yang IDENTIK ------------
    # Selisih yang tersisa setelah B dijelaskan adalah murni beda implementasi
    # (ultralytics menghitung AP-nya sendiri; pycocotools memakai COCOeval).
    if lap["hasil_json"]:
        lap["selisih_pycoco_minus_hasiljson"] = {
            "vs_maxdets_100": round(
                lap["pycoco_maxdets_100"]["mAP50"] - lap["hasil_json"]["mAP50"], 6),
            "vs_maxdets_300": round(
                lap["pycoco_maxdets_300"]["mAP50"] - lap["hasil_json"]["mAP50"], 6),
        }

    print(json.dumps(lap, indent=2))
    if args.keluaran:
        Path(args.keluaran).parent.mkdir(parents=True, exist_ok=True)
        Path(args.keluaran).write_text(json.dumps(lap, indent=2))
        print(f"-> {args.keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
