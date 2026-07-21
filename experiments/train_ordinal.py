#!/usr/bin/env python3
"""I-22 — Loss ordinal untuk kelas kematangan (E-013).

Dasar bukti: SR-009 (E-012) menunjukkan kebingungan kematangan bersifat
ORDINAL. Enam kebingungan terbesar seluruhnya berjarak satu langkah pada rantai
B1->B2->B3->B4 (B3->B4 32,5%, B2->B3 28,3%), sementara lompatan dua langkah
nyaris tidak terjadi (B3->B1 hanya 7 dari 375). Kematangan adalah variabel
kontinu yang dipotong menjadi empat kotak.

Ketidakcocokan yang diserang:

                          B2 -> B3        B1 -> B4
  Pelatihan (kategoris)   salah total     salah total
  Metrik DiB (Class +-1)  DIANGGAP BENAR  salah

Metrik evaluasi DiB sudah mengakui ordinalitas lewat toleransi +-1, tetapi
objektif pelatihan belum: klasifikasi kategoris menghukum kesalahan ke tetangga
sama beratnya dengan lompatan jauh. Model menghabiskan kapasitas memisahkan
sesuatu yang metriknya sendiri tidak pedulikan -- persis "mismatch
objective-ke-deployment" pada docs/deep-research-report.md.

Cara kerja: sebelum BCE, massa target disebar sebagian ke kelas TETANGGA saja
(bukan seluruh kelas seperti label smoothing biasa). Dengan alpha=0,2, sebuah
tandan B3 memberi target 0,8 pada B3 dan 0,1 pada masing-masing B2 dan B4,
tetapi 0 pada B1.

Ini perubahan pada APA yang dioptimalkan, bukan penyetelan hyperparameter.

Pemakaian:
  python train_ordinal.py --alpha 0.2 --epochs 60
"""
from __future__ import annotations

import argparse
from pathlib import Path

import torch
import torch.nn as nn

RUNS = Path("/workspace/experiments/runs")
DATA = "/workspace/experiments/data_rgb.yaml"


def ordinal_smooth(t: torch.Tensor, alpha: float) -> torch.Tensor:
    """Sebar massa target ke kelas tetangga pada dimensi terakhir.

    t : (..., nc) skor target, massa pada kelas yang ditugaskan
    """
    if alpha <= 0:
        return t
    left = torch.zeros_like(t)
    right = torch.zeros_like(t)
    left[..., :-1] = t[..., 1:]     # massa dari kelas di kanan menetes ke kiri
    right[..., 1:] = t[..., :-1]    # massa dari kelas di kiri menetes ke kanan
    return (1.0 - alpha) * t + (alpha / 2.0) * (left + right)


class OrdinalBCE(nn.Module):
    """BCE yang melunakkan target secara ordinal lebih dulu."""

    def __init__(self, alpha: float):
        super().__init__()
        self.alpha = alpha
        self.bce = nn.BCEWithLogitsLoss(reduction="none")

    def forward(self, pred, target):
        return self.bce(pred, ordinal_smooth(target, self.alpha))


def patch_loss(alpha: float) -> None:
    """Sisipkan OrdinalBCE ke dalam kriteria deteksi ultralytics."""
    from ultralytics.utils import loss as L

    targets = [n for n in dir(L) if n.endswith("DetectionLoss")]
    if not targets:
        raise RuntimeError("kelas DetectionLoss tidak ditemukan di ultralytics.utils.loss")
    patched = []
    for name in targets:
        cls = getattr(L, name)
        orig_init = cls.__init__

        def new_init(self, *a, _orig=orig_init, **kw):
            _orig(self, *a, **kw)
            if hasattr(self, "bce"):
                self.bce = OrdinalBCE(alpha)

        cls.__init__ = new_init
        patched.append(name)
    print(f"loss ditambal (alpha={alpha}): {', '.join(patched)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpha", type=float, default=0.2,
                    help="proporsi massa target yang disebar ke tetangga")
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--weights", default="yolo26m.pt")
    ap.add_argument("--data", default=DATA)
    args = ap.parse_args()

    patch_loss(args.alpha)

    from ultralytics import YOLO
    name = f"ordinal_a{args.alpha}_e{args.epochs}_s{args.seed}"
    print(f"melatih -> {name}")
    model = YOLO(args.weights)
    model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz,
                batch=args.batch, seed=args.seed, project=str(RUNS), name=name,
                exist_ok=True, patience=args.epochs, plots=False,
                deterministic=True, val=True)
    m = model.val(data=args.data, split="test", imgsz=args.imgsz,
                  batch=args.batch, project=str(RUNS), name=f"{name}_test",
                  exist_ok=True)
    print(f"\nHASIL UJI ORDINAL (alpha={args.alpha})")
    print(f"  mAP50    : {m.box.map50:.4f}")
    print(f"  mAP50-95 : {m.box.map:.4f}")
    for i, c in enumerate(["B1", "B2", "B3", "B4"]):
        try:
            print(f"  {c} AP50  : {m.box.ap50[i]:.4f}")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
