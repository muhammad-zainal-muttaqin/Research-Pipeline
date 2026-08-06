#!/usr/bin/env python3
"""Diagnostik cacat audit #1: nilai padding letterbox pada kanal ke-4.

ultralytics 8.4.103 data/augment.py LetterBox.apply_image cabang "multispectral"
mengisi SELURUH kanal dengan padding_value (114), termasuk kanal depth. Padahal
konvensi encoding kita adalah 0 = "tidak ada data" (lihat depth_calib.encode_inverse).
Citra 1280x800 -> 640x640 memberi skala 0,5, jadi tinggi terpakai 400 px dan
padding 120 px di atas + 120 px di bawah = 240/640 = 37,5% tinggi citra berisi
depth palsu bernilai 114.

Skrip ini TIDAK melatih ulang. Ia mengevaluasi checkpoint 4-kanal yang SUDAH ADA
dua kali pada split test: (a) apa adanya, (b) dengan padding kanal ke-4 dipaksa 0.
Selisihnya = besaran cacat. Kalau selisihnya kecil, angka E-022 yang sudah
dilaporkan tetap sah dan matriks P0 boleh lanjut apa adanya.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
PIPELINE_ROOT = REPO_ROOT / "reproduce" / "pipeline"

import numpy as np


def patch_pad_kanal4_nol() -> None:
    """Paksa padding kanal ke-4 menjadi 0 (= 'tidak ada data'), kanal RGB tetap 114."""
    from ultralytics.data.augment import LetterBox

    asli = LetterBox.apply_image

    def apply_image(self, labels, params):
        keluar = asli(self, labels, params)
        img = keluar["img"]
        if img.ndim == 3 and img.shape[2] == 4:
            top, bottom = params["top"], params["bottom"]
            left, right = params["left"], params["right"]
            h, w = img.shape[:2]
            d = img[..., 3]
            # nolkan hanya bingkai padding, jangan sentuh area citra asli
            if top:
                d[:top, :] = 0
            if bottom:
                d[h - bottom:, :] = 0
            if left:
                d[:, :left] = 0
            if right:
                d[:, w - right:] = 0
        return keluar

    LetterBox.apply_image = apply_image
    print("patch aktif: padding kanal ke-4 = 0")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="runs/detect/runs_e022/yolo26n_rgbd_seed42")
    ap.add_argument("--data", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42" / "data_rgbd4.yaml"))
    ap.add_argument("--keluaran", default="results/diag_letterbox_pad.json")
    args = ap.parse_args()

    import sys
    sys.path.insert(0, str(PIPELINE_ROOT))
    import fourch  # memasang pemuat 4-kanal, sama seperti train_depth4ch.py
    fourch.patch_loader(str(EVIDENCE_ROOT / "depth_png"), dropout=0.0)

    from ultralytics import YOLO

    hasil = {}
    for label in ("pad114_apaadanya", "pad0_kanal4"):
        if label == "pad0_kanal4":
            patch_pad_kanal4_nol()
        m = YOLO(f"{args.run}/weights/best.pt")
        r = m.val(data=args.data, split="test", imgsz=640, batch=16, verbose=False,
                  plots=False, save_json=False)
        hasil[label] = {
            "mAP50": float(r.box.map50), "mAP50-95": float(r.box.map),
            "perkelas_AP50": {n: float(v) for n, v in
                              zip(["B1", "B2", "B3", "B4"], r.box.ap50)},
        }
        print(f"{label}: mAP50={r.box.map50:.4f} mAP50-95={r.box.map:.4f}")

    a, b = hasil["pad114_apaadanya"], hasil["pad0_kanal4"]
    hasil["selisih"] = {k: b[k] - a[k] for k in ("mAP50", "mAP50-95")}
    hasil["fraksi_tinggi_padding"] = 240 / 640

    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hasil, indent=2))
    print(f"\nselisih mAP50    {hasil['selisih']['mAP50']:+.4f}")
    print(f"selisih mAP50-95 {hasil['selisih']['mAP50-95']:+.4f}")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
