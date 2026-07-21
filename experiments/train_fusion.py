#!/usr/bin/env python3
"""I-4 — YOLO 4-kanal (early fusion RGB+D) vs baseline RGB, kondisi identik.

PREDIKSI YANG DICATAT SEBELUM DIJALANKAN (lihat SR-005): fusi ini **diperkirakan
tidak menolong**, karena E-006 menunjukkan tandan tidak menonjol dalam kedalaman
(kontras 0,26x kotak acak, AUC 0,60 vs 0,60). Ophoff dkk. (naskah §174) juga
memperkirakan early fusion berkinerja lebih rendah daripada middle/late fusion.
Eksperimen ini tetap dijalankan sebagai **kontrol**: tanpa angkanya, klaim
"depth tidak menolong lewat early fusion" hanyalah dugaan.

Kejujuran perbandingan dijaga dengan menyamakan segalanya kecuali satu variabel:
split, resolusi, epoch, batch, seed, augmentasi, dan bobot awal identik. Satu-
satunya beda adalah ada/tidaknya kanal kedalaman.

Bobot pratlatih 3-kanal diadaptasi ke 4-kanal dengan menyalin bobot RGB apa
adanya dan menginisialisasi kanal keempat dari rata-rata ketiganya (praktik
standar inflasi kanal). Kalau kanal keempat diinisialisasi nol, model memulai
dari titik yang persis sama dengan RGB -- itu justru membuat perbandingan tidak
sensitif terhadap kontribusi depth di awal pelatihan.

Pemakaian:
  python train_fusion.py --build          # rakit dataset RGBD saja
  python train_fusion.py --mode rgb       # latih baseline
  python train_fusion.py --mode rgbd      # latih 4-kanal
  python train_fusion.py --mode both --epochs 40
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
DEPTH = Path("/workspace/experiments/depth_da3/depth")
RGBD = Path("/workspace/experiments/data_rgbd")
RUNS = Path("/workspace/experiments/runs")


# --------------------------------------------------------------------------
def build_rgbd(limit: int | None = None) -> int:
    """Rakit citra 4-kanal: BGR + kedalaman sebagai kanal ke-4."""
    (RGBD / "images").mkdir(parents=True, exist_ok=True)
    (RGBD / "labels").mkdir(parents=True, exist_ok=True)

    n, miss = 0, 0
    imgs = sorted((SRC / "images").glob("*.jpg"))
    if limit:
        imgs = imgs[:limit]
    for p in imgs:
        dp = DEPTH / f"{p.stem}.png"
        if not dp.exists():
            miss += 1
            continue
        out = RGBD / "images" / f"{p.stem}.png"
        if not out.exists():
            bgr = cv2.imread(str(p))
            d16 = cv2.imread(str(dp), cv2.IMREAD_UNCHANGED)
            if bgr is None or d16 is None:
                miss += 1
                continue
            if d16.shape[:2] != bgr.shape[:2]:
                d16 = cv2.resize(d16, (bgr.shape[1], bgr.shape[0]))
            d8 = (d16.astype(np.float32) / 65535.0 * 255).astype(np.uint8)
            cv2.imwrite(str(out), np.dstack([bgr, d8]))
        lb = SRC / "labels" / f"{p.stem}.txt"
        tgt = RGBD / "labels" / f"{p.stem}.txt"
        if lb.exists() and not tgt.exists():
            shutil.copy(lb, tgt)
        n += 1
    print(f"RGBD dirakit: {n} citra ({miss} dilewati karena depth belum ada)")

    # daftar split, memakai keanggotaan split asli
    for split in ("train", "val", "test"):
        names = [Path(l).stem for l in
                 (SRC / f"{split}.txt").read_text().split() if l.strip()]
        lines = [str(RGBD / "images" / f"{s}.png") for s in names
                 if (RGBD / "images" / f"{s}.png").exists()]
        (RGBD / f"{split}.txt").write_text("\n".join(lines) + "\n")
        print(f"  {split}: {len(lines)} citra")

    (RGBD / "data.yaml").write_text(
        f"path: {RGBD}\ntrain: train.txt\nval: val.txt\ntest: test.txt\n"
        f"channels: 4\nnc: 4\nnames:\n  0: B1\n  1: B2\n  2: B3\n  3: B4\n")
    return n


RGBD_FLAG = -999  # penanda internal untuk pemuatan 4-kanal (RGB + kedalaman)
RGBT_FLAG = -998  # penanda internal untuk pemuatan 4-kanal (RGB + tekstur)


def texture_channel(bgr):
    """Kanal tekstur Laplacian.

    E-011 menunjukkan ini satu-satunya transformasi yang menaikkan keterpisahan
    B4 (AUC 0,6153 vs kendali 0,5695), sementara kedalaman (E-006), warna
    (E-010), dan penajam kontras (E-011) semuanya gagal. Dihitung saat pemuatan
    sehingga tidak memakan disk sama sekali.
    """
    g = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lap = np.abs(cv2.Laplacian(g, cv2.CV_32F, ksize=3))
    lap = cv2.GaussianBlur(lap, (0, 0), 2)
    hi = np.percentile(lap, 99.5)
    return np.clip(lap / max(hi, 1e-6) * 255, 0, 255).astype(np.uint8)


_FLAG = [RGBD_FLAG]


def patch_loader_for_4ch(mode: str = "rgbd") -> None:
    """Susun RGB+depth SAAT PEMUATAN, bukan disimpan ganda di disk.

    Versi awal skrip ini menulis 3.992 PNG 4-kanal lossless (14 GB) padahal
    JPEG aslinya sudah ada -- pemborosan yang menghabiskan kuota disk. Di sini
    citra dibaca dari JPEG asli dan peta kedalaman ditempel sebagai kanal ke-4
    di memori, sehingga tidak ada byte tambahan yang ditulis ke disk.
    """
    _FLAG[0] = RGBT_FLAG if mode == "rgbt" else RGBD_FLAG
    import ultralytics.data.base as base
    from ultralytics.data.base import BaseDataset

    orig_init = BaseDataset.__init__

    def patched_init(self, *a, **kw):
        orig_init(self, *a, **kw)
        if getattr(self, "channels", 3) == 4:
            self.cv2_flag = _FLAG[0]

    BaseDataset.__init__ = patched_init

    orig_imread = base.imread

    def imread_rgbd(filename, flags=cv2.IMREAD_COLOR):
        if flags not in (RGBD_FLAG, RGBT_FLAG):
            return orig_imread(filename, flags)
        bgr = cv2.imread(str(filename), cv2.IMREAD_COLOR)
        if bgr is None:
            return None
        if flags == RGBT_FLAG:
            return np.dstack([bgr, texture_channel(bgr)])
        dp = DEPTH / f"{Path(filename).stem}.png"
        d16 = cv2.imread(str(dp), cv2.IMREAD_UNCHANGED)
        if d16 is None:
            # depth hilang -> kanal nol, dan ini TIDAK disembunyikan
            d8 = np.zeros(bgr.shape[:2], np.uint8)
        else:
            if d16.shape[:2] != bgr.shape[:2]:
                d16 = cv2.resize(d16, (bgr.shape[1], bgr.shape[0]))
            d8 = (d16.astype(np.float32) / 65535.0 * 255).astype(np.uint8)
        return np.dstack([bgr, d8])

    base.imread = imread_rgbd


def write_rgbd_yaml() -> str:
    """data.yaml 4-kanal yang menunjuk ke JPEG ASLI (bukan salinan)."""
    p = Path("/workspace/experiments/data_rgbd4.yaml")
    p.write_text("path: /workspace/experiments/splits_rgb\n"
                 "train: train.txt\nval: val.txt\ntest: test.txt\n"
                 "channels: 4\nnc: 4\nnames:\n"
                 "  0: B1\n  1: B2\n  2: B3\n  3: B4\n")
    return str(p)


def inflate_first_conv(model, in_ch: int = 4) -> bool:
    """Salin bobot conv pertama 3-kanal ke 4-kanal; kanal ke-4 = rata-rata RGB."""
    import torch
    import torch.nn as nn
    for m in model.modules():
        if isinstance(m, nn.Conv2d) and m.in_channels == 3:
            w = m.weight.data
            new = nn.Conv2d(in_ch, m.out_channels, m.kernel_size, m.stride,
                            m.padding, bias=m.bias is not None)
            with torch.no_grad():
                new.weight[:, :3] = w
                new.weight[:, 3:] = w.mean(dim=1, keepdim=True)
                if m.bias is not None:
                    new.bias.copy_(m.bias)
            return new
    return False


# --------------------------------------------------------------------------
def train(mode: str, args) -> None:
    from ultralytics import YOLO

    if mode in ("rgbd", "rgbt"):
        patch_loader_for_4ch(mode)
        data = write_rgbd_yaml()
    else:
        data = "/workspace/experiments/data_rgb.yaml"

    name = f"{mode}_e{args.epochs}_i{args.imgsz}_s{args.seed}"
    print(f"\n{'='*70}\nLATIH {mode.upper()}  ->  {name}\n{'='*70}")

    model = YOLO(args.weights)
    model.train(
        data=data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch,
        seed=args.seed, project=str(RUNS), name=name, exist_ok=True,
        patience=args.epochs, val=True, plots=False, verbose=True,
        workers=args.workers, deterministic=True,
    )
    m = model.val(data=data, split="test", imgsz=args.imgsz, batch=args.batch,
                  project=str(RUNS), name=f"{name}_test", exist_ok=True)
    print(f"\nHASIL UJI {mode.upper()}")
    print(f"  mAP50    : {m.box.map50:.4f}")
    print(f"  mAP50-95 : {m.box.map:.4f}")
    for i, c in enumerate(["B1", "B2", "B3", "B4"]):
        try:
            print(f"  {c} AP50  : {m.box.ap50[i]:.4f}  "
                  f"P={m.box.p[i]:.4f}  R={m.box.r[i]:.4f}")
        except Exception:
            pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["rgb", "rgbd", "rgbt", "both"], default="both")
    ap.add_argument("--build", action="store_true", help="rakit dataset RGBD lalu keluar")
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--weights", default="yolo26m.pt")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    if args.build:
        build_rgbd(args.limit)
        return 0
    for m in (["rgb", "rgbd"] if args.mode == "both" else [args.mode]):
        train(m, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
