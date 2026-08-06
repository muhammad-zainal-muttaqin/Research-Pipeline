#!/usr/bin/env python3
"""F-004 — Simpan logit MENTAH per query dari checkpoint RF-DETR.

E-021 hanya mengarsipkan JSON agregat (`pr_curves.json`, `confusion.json`,
`bootstrap_ci.json`); tidak ada satu pun deteksi mentah per objek. Akibatnya P1
(F-005) tidak dapat dihitung tanpa inferensi ulang — dan setelah bobotnya hilang,
tanpa latihan ulang. Berkas ini menutup lubang itu untuk seterusnya.

## Kenapa perlu logit, bukan hasil `predict()`

Skor deteksi RF-DETR = `sigmoid(pred_logits)` per kelas INDEPENDEN, lalu top-k
`num_select=300` atas grid datar (Q x C) = 300 x 4 = 1.200 pasangan
(`rfdetr/models/postprocess.py:106`). Artinya `predict()` hanya mengembalikan
seperempat pasangan, dipilih menurut skor.

P1 menanyakan selisih logit ANTAR KELAS DI DALAM query yang sama:

    delta = z[q, c_benar] - z[q, c_salah]

Untuk itu keempat logit tiap query harus utuh, termasuk yang tidak lolos top-k.
Karena itu `PostProcess.forward` ditambal untuk menyimpan `pred_logits` mentah
(B, Q, C) plus kotak SELURUH query yang sudah diskalakan ke piksel — bukan hanya
yang terpilih.

## Kenapa menambal, bukan menulis ulang inferensi

Menyalin jalur pra-proses rf-detr (letterbox, normalisasi, resolusi) berarti dua
sumber kebenaran yang bisa menyimpang diam-diam saat paket naik versi. Pola yang
sama dipakai `train_rfdetr_4ch.py` dan `train_rfdetr_fusion_late.py`. Di sini
`forward` asli tetap dipanggil dan hasilnya tetap dikembalikan apa adanya,
sehingga `predict()` berperilaku persis seperti biasa.

Keluaran: satu `.npz` per split berisi
  logits  float16 (N, Q, C)  -- logit MENTAH, sebelum sigmoid
  boxes   float32 (N, Q, 4)  -- xyxy piksel, SELURUH query
  ukuran  int32   (N, 2)     -- (tinggi, lebar) citra asli
  nama    daftar stem citra, urut

Pemakaian:
  python eval/dump_logits_rfdetr.py --ckpt <checkpoint_best_ema.pth> \
      --split test --keluaran results/F-004/logits_test_seed42.npz
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

import numpy as np
import torch
from PIL import Image

DS = Path(__file__).resolve().parents[1] / "rfdetr_ds"
SPLIT_DIR = {"val": "valid", "test": "test"}
NAMES = ["B1", "B2", "B3", "B4"]

# Tempat singgah hasil tambalan. Diisi satu entri per citra, urut panggilan.
_STASH: list[dict] = []


def pasang_tambalan() -> None:
    """Tambal `PostProcess.forward` supaya menyimpan logit mentah semua query."""
    from rfdetr.models.postprocess import PostProcess
    from rfdetr.utilities import box_ops

    asli = PostProcess.forward

    def forward_rekam(self, outputs, target_sizes):
        logits = outputs["pred_logits"]            # (B, Q, C)
        bbox = outputs["pred_boxes"]               # (B, Q, 4) cxcywh ternormalisasi
        # Skala kotak SELURUH query ke piksel, meniru `_gather_and_scale_boxes`
        # persis (termasuk clamp) tetapi tanpa penyaringan top-k.
        boxes = box_ops.box_cxcywh_to_xyxy(bbox)
        img_h, img_w = target_sizes.unbind(1)
        skala = torch.stack([img_w, img_h, img_w, img_h], dim=1).to(boxes.dtype)
        boxes = boxes * skala[:, None, :]
        boxes = boxes.clamp_min(0.0).clamp(max=skala[:, None, :])
        for b in range(logits.shape[0]):
            _STASH.append({
                "logits": logits[b].detach().float().cpu().numpy().astype(np.float16),
                "boxes": boxes[b].detach().float().cpu().numpy().astype(np.float32),
                "ukuran": target_sizes[b].detach().cpu().numpy().astype(np.int32),
            })
        return asli(self, outputs, target_sizes)

    PostProcess.forward = forward_rekam
    print("tambalan terpasang: logit mentah seluruh query akan direkam")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", required=True)
    ap.add_argument("--split", default="test", choices=["val", "test"])
    ap.add_argument("--resolution", type=int, default=1280)
    ap.add_argument("--chunk", type=int, default=8)
    ap.add_argument("--keluaran", required=True)
    args = ap.parse_args()

    pasang_tambalan()
    from rfdetr import RFDETRLarge

    model = RFDETRLarge(pretrain_weights=args.ckpt, resolution=args.resolution)

    idir = DS / SPLIT_DIR[args.split] / "images"
    paths = sorted(idir.iterdir())
    print(f"{args.split}: {len(paths)} citra")

    for i in range(0, len(paths), args.chunk):
        chunk = [str(p) for p in paths[i:i + args.chunk]]
        model.predict(chunk, threshold=0.001)
        if (i // args.chunk) % 10 == 0:
            print(f"  {i + len(chunk)}/{len(paths)}", flush=True)

    if len(_STASH) != len(paths):
        raise RuntimeError(
            f"jumlah rekaman ({len(_STASH)}) != jumlah citra ({len(paths)}). "
            "Urutan tidak dapat dipercaya; jangan dipakai.")

    keluaran = Path(args.keluaran)
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        keluaran,
        logits=np.stack([s["logits"] for s in _STASH]),
        boxes=np.stack([s["boxes"] for s in _STASH]),
        ukuran=np.stack([s["ukuran"] for s in _STASH]),
        nama=np.array([p.stem for p in paths]),
        kelas=np.array(NAMES),
        ckpt=np.array([args.ckpt]),
        split=np.array([args.split]),
    )
    l = np.stack([s["logits"] for s in _STASH])
    print(f"-> {keluaran}  bentuk logits {l.shape}  "
          f"rentang [{l.min():.2f}, {l.max():.2f}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
