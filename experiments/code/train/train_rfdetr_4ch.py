#!/usr/bin/env python3
"""E-022: RF-DETR (rfdetr 1.8.3) dengan masukan 4-kanal RGB+D simultan.

rfdetr SUDAH punya jalur N-kanal bawaan (`ModelConfig.num_channels`), jadi tidak
perlu fork paket. Yang dibutuhkan tiga tambalan kecil:

PATCH A — pemuat data. `_LazyYoloDetectionDataset.__getitem__`
(`rfdetr/datasets/yolo.py:158-160`) membaca lewat `Image.open(...).convert("RGB")`
sehingga selalu 3 kanal. Dibungkus agar mengembalikan array 4 kanal
[R,G,B,D] uint8; depth dibaca dari PNG kanonik hasil reproject_depth.py.

PATCH B — normalisasi. `datasets/transforms.py:42` memakai mean/std ImageNet
3 elemen. Ditambah elemen ke-4 dari statistik kanal depth pada split TRAIN saja
(bukan val/test — itu kebocoran).

PATCH C — conv patch-embed. Heuristik bawaan `_adapt_input_conv`
(`rfdetr/inference.py:70-92`) MENGUBIN pola 3-kanal lalu mengalikan SELURUH
bobot dengan 3/4 = 0,75. Itu mengubah perilaku pratlatih dan membuat
perbandingan dengan lengan RGB tidak bersih. Ditimpa: kanal 1..3 = bobot
pratlatih apa adanya, kanal ke-4 = 0, sehingga model berangkat PERSIS dari
perilaku RGB pratlatih dan belajar memakai depth secara bertahap — sama seperti
`fourch.make_inflate_callback` untuk ultralytics.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
PIPELINE_ROOT = REPO_ROOT / "reproduce" / "pipeline"

import numpy as np

DEPTH_DIR = EVIDENCE_ROOT / "depth_png"


def statistik_depth_train(train_txt: Path) -> tuple[float, float]:
    """mean/std kanal depth (skala 0..1) dari split TRAIN saja."""
    import cv2
    stems = [Path(x.strip()).stem for x in train_txt.read_text().splitlines() if x.strip()]
    rng = np.random.default_rng(42)
    contoh = [stems[i] for i in rng.choice(len(stems), min(200, len(stems)), replace=False)]
    nilai = []
    for s in contoh:
        p = DEPTH_DIR / f"{s}.png"
        if p.is_file():
            d = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
            nilai.append(rng.choice(d.ravel(), 20000, replace=False))
    v = np.concatenate(nilai)
    return float(v.mean()), float(max(v.std(), 1e-3))


def patch_a_pemuat() -> None:
    """Pemuat data mengembalikan 4 kanal [R,G,B,D] uint8."""
    import cv2
    from PIL import Image

    import rfdetr.datasets.yolo as yolo_mod

    asli = yolo_mod._LazyYoloDetectionDataset.__getitem__

    def getitem_4ch(self, idx):
        sample = self._samples[idx]
        with Image.open(sample.image_path) as image:
            rgb = np.array(image.convert("RGB"))
        p = DEPTH_DIR / f"{Path(sample.image_path).stem}.png"
        d8 = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE) if p.is_file() else None
        if d8 is None:
            d8 = np.zeros(rgb.shape[:2], np.uint8)  # 0 = tidak ada data
        elif d8.shape[:2] != rgb.shape[:2]:
            d8 = cv2.resize(d8, (rgb.shape[1], rgb.shape[0]), interpolation=cv2.INTER_NEAREST)
        return sample.image_path, np.dstack([rgb, d8]), sample.to_detections()

    yolo_mod._LazyYoloDetectionDataset.__getitem__ = getitem_4ch
    print(f"patch A: pemuat 4-kanal aktif (depth dari {DEPTH_DIR})")
    return asli


def patch_a_derau() -> None:
    """Kontrol negatif: kanal ke-4 diisi derau, bukan depth.

    Derau dibangkitkan dari CRC32 nama berkas (bukan `hash()`, yang diacak
    per proses oleh PYTHONHASHSEED sehingga tidak dapat direproduksi), jadi tiap
    citra selalu mendapat derau yang sama di setiap epoch dan setiap run.
    """
    import zlib

    from PIL import Image

    import rfdetr.datasets.yolo as yolo_mod

    def getitem_derau(self, idx):
        sample = self._samples[idx]
        with Image.open(sample.image_path) as image:
            rgb = np.array(image.convert("RGB"))
        rng = np.random.default_rng(zlib.crc32(Path(sample.image_path).stem.encode()))
        d8 = rng.integers(0, 256, rgb.shape[:2], dtype=np.uint8)
        return sample.image_path, np.dstack([rgb, d8]), sample.to_detections()

    yolo_mod._LazyYoloDetectionDataset.__getitem__ = getitem_derau
    print("patch A: kanal ke-4 = DERAU (kontrol negatif, seed CRC32 per berkas)")


def patch_b_normalisasi(mean_d: float, std_d: float) -> None:
    import rfdetr.datasets.transforms as T

    asli_init = T.Normalize.__init__

    def init_4ch(self, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
        if len(mean) == 3:
            mean = (*mean, mean_d)
            std = (*std, std_d)
        asli_init(self, mean, std)

    T.Normalize.__init__ = init_4ch
    print(f"patch B: normalisasi 4-kanal, mean_D={mean_d:.4f} std_D={std_d:.4f} (dari TRAIN)")


def patch_c0_validasi_kanal(paksa_init_4: bool = False) -> None:
    """Validasi kanal di PatchEmbeddings memakai conv, bukan config.

    rfdetr membangun backbone dengan `config.num_channels=3` lalu MENUKAR conv
    patch-embed ke 4 kanal setelah bobot pratlatih dimuat — tetapi
    `self.num_channels` tetap 3 dan memvalidasi masukan di
    `dinov2_with_windowed_attn.py:307-311`, sehingga forward gagal dengan
    "Expected 3 but got 4". Tambalan dipasang di level KELAS karena model
    dibangun ulang di dalam `.train()` (tambalan level-instans hilang).
    """
    import torch
    import torch.nn as nn

    import rfdetr.models.backbone.dinov2_with_windowed_attn as dino

    Kelas = dino.Dinov2WithRegistersPatchEmbeddings

    # Idempoten: kedua lengan (mis. derau dan depth) dimuat dalam SATU proses saat
    # evaluasi berpasangan, jadi fungsi ini dipanggil dua kali. Tanpa penjaga ini
    # `init_4ch` membungkus dirinya sendiri dan gagal menyalin conv yang sudah
    # 4-kanal ke slot 3-kanal.
    if getattr(dino, "_e022_patched", False):
        return
    dino._e022_patched = True

    # Dua jalur yang saling BERKEBALIKAN, jadi tambalannya wajib kondisional:
    #
    #  - LATIH (paksa_init_4=False): checkpoint pratlatih berisi conv 3-kanal.
    #    Conv harus tetap 3-kanal saat load_state_dict, lalu diinflasi ke 4 di
    #    titik forward. Memaksa 4 di __init__ menggagalkan pemuatan:
    #    "copying a param with shape [384, 3, ...], current model is [384, 4, ...]".
    #
    #  - EVALUASI (paksa_init_4=True): checkpoint SUDAH 4-kanal. Conv harus
    #    sudah 4-kanal SEBELUM load_state_dict, kalau tidak galatnya terbalik:
    #    "copying a param with shape [384, 4, ...], current model is [384, 3, ...]".
    asli_init = Kelas.__init__

    def init_4ch(self, config):
        asli_init(self, config)
        p = self.projection
        if p.in_channels == 4:
            self.num_channels = 4
            return
        self.projection = nn.Conv2d(4, p.out_channels, kernel_size=p.kernel_size,
                                    stride=p.stride, padding=p.padding,
                                    bias=p.bias is not None)
        with torch.no_grad():
            self.projection.weight[:, :3] = p.weight
            self.projection.weight[:, 3] = 0.0
            if p.bias is not None:
                self.projection.bias.copy_(p.bias)
        self.num_channels = 4

    if paksa_init_4:
        Kelas.__init__ = init_4ch

    asli = Kelas.forward

    def forward_selaras(self, pixel_values):
        # rfdetr membangun ULANG model di dalam .train() dari config (num_channels=3),
        # jadi inflasi yang dilakukan sebelum train() hilang. Maka inflasi dikerjakan
        # di titik forward: sekali, saat batch 4-kanal pertama tiba.
        c = pixel_values.shape[1]
        proj = self.projection
        if c == 4 and proj.in_channels == 3:
            import torch.nn as nn
            baru_conv = nn.Conv2d(4, proj.out_channels, kernel_size=proj.kernel_size,
                                  stride=proj.stride, padding=proj.padding,
                                  bias=proj.bias is not None)
            baru_conv = baru_conv.to(proj.weight.device, proj.weight.dtype)
            with torch.no_grad():
                baru_conv.weight[:, :3] = proj.weight          # kanal RGB apa adanya
                baru_conv.weight[:, 3] = 0.0                   # depth mulai netral
                if proj.bias is not None:
                    baru_conv.bias.copy_(proj.bias)
            self.projection = baru_conv
            self.num_channels = 4
            print("patch C0: conv patch-embed diinflasi 3->4 saat forward "
                  "(kanal RGB pratlatih utuh, kanal depth = 0)")
        self.num_channels = self.projection.in_channels
        return asli(self, pixel_values)

    Kelas.forward = forward_selaras
    print("patch C0: validasi kanal PatchEmbeddings mengikuti conv, bukan config")


def patch_c_conv(model) -> None:
    """Timpa heuristik ubin-lalu-skala 0,75 dengan inflasi nol-kanal-4."""
    import torch
    import torch.nn as nn

    net = model.model.model if hasattr(model.model, "model") else model.model

    target = None
    for m in net.modules():
        if isinstance(m, nn.Conv2d) and m.in_channels == 4:
            target = m
            break
    if target is None:
        print("patch C: PERINGATAN — conv 4-kanal tidak ditemukan")
        return
    with torch.no_grad():
        w = target.weight.detach().clone()
        # heuristik bawaan: w[:, :3] = pratlatih * 0,75 dan w[:, 3] = kanal-R * 0,75
        pratlatih = w[:, :3] / 0.75
        target.weight[:, :3] = pratlatih
        target.weight[:, 3] = 0.0
    print(f"patch C: conv patch-embed {tuple(target.weight.shape)} — kanal 1-3 dipulihkan "
          f"ke bobot pratlatih (dibagi 0,75), kanal 4 = 0")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--varian", default="nano", choices=["nano", "small", "medium", "large"])
    ap.add_argument("--modal", choices=["rgb", "rgbd"], required=True)
    ap.add_argument("--depth-acak", action="store_true",
                    help="kontrol negatif: kanal ke-4 diisi derau, bukan depth")
    ap.add_argument("--dataset", default="rfdetr_ds_depth")
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--resolution", type=int, default=640)
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--grad-accum", type=int, default=2)
    ap.add_argument("--workers", type=int, default=8)
    # CACAT AUDIT 2026-07-30 (diperbaiki): seed dulu di-hardcode 42 di model.train(),
    # jadi setiap "seed berbeda" pada matriks multi-seed akan memakai RNG identik.
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--output", default=None)
    args = ap.parse_args()

    nama = args.output or f"runs_e022/rfdetr{args.varian}_{args.modal}"
    Path(nama).mkdir(parents=True, exist_ok=True)

    if args.modal == "rgbd":
        if args.depth_acak:
            patch_a_derau()
        else:
            patch_a_pemuat()
        patch_c0_validasi_kanal()
        mean_d, std_d = statistik_depth_train(Path(args.split_dir) / "train.txt")
        patch_b_normalisasi(mean_d, std_d)

    from rfdetr import RFDETRLarge, RFDETRMedium, RFDETRNano, RFDETRSmall
    KELAS = {"nano": RFDETRNano, "small": RFDETRSmall,
             "medium": RFDETRMedium, "large": RFDETRLarge}
    kw = {"resolution": args.resolution}
    if args.modal == "rgbd":
        kw["num_channels"] = 4
    model = KELAS[args.varian](**kw)
    if args.modal == "rgbd":
        patch_c_conv(model)

    mulai = time.time()
    model.train(
        dataset_dir=args.dataset, output_dir=nama, epochs=args.epochs,
        batch_size=args.batch, grad_accum_steps=args.grad_accum,
        num_workers=args.workers, resolution=args.resolution, device="cuda", seed=args.seed,
        early_stopping=False,
        # pagar keadilan E-021: default multi_scale+expanded_scales mengunci ke
        # skala TERBESAR (resolusi x 45/40), memberi keunggulan resolusi diam-diam
        multi_scale=False, expanded_scales=False,
        run_test=True,
    )
    durasi = time.time() - mulai

    meta = {"run": nama, "varian": args.varian, "modal": args.modal,
            "depth_acak": args.depth_acak,
            "epochs": args.epochs, "resolution": args.resolution,
            "batch": args.batch, "grad_accum": args.grad_accum,
            "durasi_detik": round(durasi, 1)}
    (Path(nama) / "hasil.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
