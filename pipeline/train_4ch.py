#!/usr/bin/env python3
"""Pelatihan YOLO 4-kanal (RGB + kedalaman) — satu bobot untuk dua mode uji.

Prasyarat:
  1. data.yaml dengan `channels: 4` (lihat pipeline/README.md untuk templat).
  2. Folder PNG kedalaman kanonik senama dengan citranya
     (hasil prepare_depth.py). Citra tanpa PNG kedalaman tetap ikut dilatih —
     kanal ke-4-nya nol, sama seperti mode RGB di lapangan.

Contoh:
  python train_4ch.py --data data_4ch.yaml --depth-dir depth_kanonik \
      --epochs 60 --batch 32 --name gemini_v1
"""
from __future__ import annotations

import argparse
from pathlib import Path

import fourch


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="data.yaml dengan channels: 4")
    ap.add_argument("--depth-dir", default=None,
                    help="folder PNG kedalaman kanonik (tanpa ini semua kanal-4 nol)")
    ap.add_argument("--dropout", type=float, default=0.25,
                    help="peluang kanal depth dikosongkan saat latih (modality dropout)")
    ap.add_argument("--weights", default="yolo26m.pt", help="bobot pratlatih 3-kanal")
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--device", default=None)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--project", default="runs4ch")
    ap.add_argument("--name", default="fourch")
    ap.add_argument("--no-inflate", action="store_true",
                    help="jangan salin bobot pratlatih ke conv pertama")
    args = ap.parse_args()

    fourch.patch_loader(args.depth_dir, dropout=args.dropout)

    from ultralytics import YOLO
    model = YOLO(args.weights)
    if not args.no_inflate:
        model.add_callback("on_pretrain_routine_end",
                           fourch.make_inflate_callback(args.weights))

    model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz,
                batch=args.batch, seed=args.seed, device=args.device,
                workers=args.workers, project=args.project, name=args.name,
                exist_ok=True, patience=args.epochs, plots=False,
                deterministic=True, val=True)

    best = Path(args.project) / args.name / "weights" / "best.pt"
    print(f"\nbobot final : {best}")

    m = model.val(data=args.data, split="test", imgsz=args.imgsz,
                  batch=args.batch, device=args.device,
                  project=args.project, name=f"{args.name}_test", exist_ok=True)
    print(f"\nHASIL UJI (split test, DENGAN depth)")
    print(f"  mAP50    : {m.box.map50:.4f}")
    print(f"  mAP50-95 : {m.box.map:.4f}")
    for i, c in enumerate(fourch.CLASSES):
        try:
            print(f"  {c} AP50  : {m.box.ap50[i]:.4f}")
        except Exception:
            pass
    print("\nUntuk mengukur mode RGB-saja, jalankan infer_4ch.py tanpa --depth-dir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
