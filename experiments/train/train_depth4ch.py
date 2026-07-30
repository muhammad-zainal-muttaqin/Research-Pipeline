#!/usr/bin/env python3
"""E-022: latih detektor ultralytics di SawitMVC-Depth, lengan RGB atau RGB-D 4-kanal.

Satu skrip untuk KEDUA lengan supaya perbandingannya tidak bisa bocor: seluruh
hiperparameter identik, HANYA kehadiran kanal kedalaman yang berbeda.

Tiga pagar keadilan yang dipasang sengaja:

1. **HSV dimatikan di KEDUA lengan.** `RandomHSV.apply_image` melewati citra
   non-3-kanal secara DIAM (`ultralytics/data/augment.py:1461`), jadi lengan
   4-kanal otomatis kehilangan augmentasi HSV. Kalau lengan RGB tetap memakai
   HSV, selisih mAP bisa salah diatribusikan ke depth. Maka hsv_h=hsv_s=hsv_v=0
   untuk dua-duanya.
2. **Inflasi conv pertama.** Transfer bobot ultralytics melewati tensor yang
   bentuknya beda, jadi tanpa callback `fourch.make_inflate_callback` conv
   pertama 4-kanal mulai ACAK — lengan RGB-D akan kalah karena inisialisasi,
   bukan karena depth. Callback mengisi kanal 1..3 dari bobot pratlatih (urutan
   BGR) dan kanal ke-4 = 0, sehingga model berangkat PERSIS dari perilaku RGB
   pratlatih.
3. **Modality dropout = 0 secara default.** Dengan dropout 0,25 lengan RGB-D
   sebenarnya berlatih 25% tanpa depth; hasil datar lalu ditafsirkan "depth
   tidak menolong" padahal yang diuji bukan itu. Dropout dijalankan sebagai
   varian terpisah untuk kebutuhan produksi dua-mode.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "/workspace/research-pipeline/pipeline")
import fourch  # noqa: E402

SPLIT = Path("/workspace/experiments/splits_depth")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arch", default="yolo26n", help="yolo26n | yolo26s | rtdetr-l | ...")
    ap.add_argument("--modal", choices=["rgb", "rgbd"], required=True)
    ap.add_argument("--split", default="seed42")
    ap.add_argument("--depth-dir", default="/workspace/experiments/depth_png")
    ap.add_argument("--dropout", type=float, default=0.0)
    ap.add_argument("--depth-acak", action="store_true",
                    help="kontrol negatif: kanal ke-4 diisi derau, bukan depth")
    ap.add_argument("--depth-tukar", action="store_true",
                    help="kontrol registrasi: kanal ke-4 = depth ASLI tapi milik citra LAIN")
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--project", default="runs_e022")
    ap.add_argument("--name", default=None)
    args = ap.parse_args()

    nama = args.name or f"{args.arch}_{args.modal}_{args.split}"
    data = SPLIT / args.split / ("data_rgbd4.yaml" if args.modal == "rgbd" else "data_rgb.yaml")
    bobot = f"{args.arch}.pt"

    if args.modal == "rgbd":
        if args.depth_acak:
            _patch_depth_acak(args.seed)
        elif args.depth_tukar:
            _patch_depth_tukar(args.depth_dir, str(SPLIT / args.split))
        else:
            fourch.patch_loader(args.depth_dir, dropout=args.dropout)

    from ultralytics import RTDETR, YOLO
    Model = RTDETR if "rtdetr" in args.arch else YOLO
    model = Model(bobot)
    if args.modal == "rgbd":
        model.add_callback("on_pretrain_routine_end", fourch.make_inflate_callback(bobot))

    mulai = time.time()
    model.train(
        data=str(data), epochs=args.epochs, imgsz=args.imgsz, batch=args.batch,
        seed=args.seed, workers=args.workers, project=args.project, name=nama,
        exist_ok=True, patience=args.epochs, plots=False, deterministic=True, val=True,
        # pagar keadilan #1 — HSV mati di kedua lengan (lihat docstring)
        hsv_h=0.0, hsv_s=0.0, hsv_v=0.0,
    )
    durasi = time.time() - mulai

    # ultralytics menaruh keluaran di runs/detect/<project>/<name> bila project relatif
    save_dir = Path(model.trainer.save_dir)
    best = save_dir / "weights" / "best.pt"
    m = model.val(data=str(data), split="test", imgsz=args.imgsz, batch=args.batch,
                  project=args.project, name=f"{nama}_test", exist_ok=True)

    hasil = {
        "run": nama, "arch": args.arch, "modal": args.modal, "split": args.split,
        "epochs": args.epochs, "imgsz": args.imgsz, "batch": args.batch, "seed": args.seed,
        "dropout": args.dropout, "depth_acak": args.depth_acak,
        "depth_dir": args.depth_dir if args.modal == "rgbd" else None,
        "durasi_detik": round(durasi, 1), "bobot": str(best),
        "test": {"mAP50": float(m.box.map50), "mAP50_95": float(m.box.map),
                 "P": float(m.box.mp), "R": float(m.box.mr),
                 "AP50_perkelas": {f"B{i+1}": float(m.box.ap50[i]) for i in range(len(m.box.ap50))}},
    }
    out = save_dir / "hasil.json"
    out.write_text(json.dumps(hasil, indent=2))
    print(json.dumps(hasil["test"], indent=2))
    print(f"-> {out}")
    return 0


def _pohon(stem: str) -> str:
    """Pohon dari nama berkas: DAMIMAS_A21B_0002_3 -> DAMIMAS_A21B_0002.

    Sama persis dengan pohon_dari() di eval_e022_pycoco.py — unit resample
    bootstrap dan unit pemisah donor tukar HARUS memakai definisi yang sama.
    """
    return stem.rsplit("_", 1)[0]


def _patch_depth_tukar(depth_dir: str, split_dir: str) -> None:
    """Kontrol REGISTRASI: kanal ke-4 = peta depth asli, tetapi milik citra LAIN.

    Kontrol derau hanya menguji "apakah kanal ke-4 mana pun berpengaruh". Kontrol
    ini lebih ketat: statistik, tekstur, dan rentang nilai depth tetap realistis;
    yang dihancurkan HANYA keselarasan spasialnya dengan RGB. Jadi kalau depth
    asli mengalahkan depth-tertukar, yang bekerja memang REGISTRASI — bukan
    sekadar "ada peta bernuansa halus di kanal keempat".

    Pertukaran memakai pergeseran daftar (deterministik, tanpa seed acak) supaya
    tiap citra selalu mendapat pasangan yang sama di setiap epoch dan setiap run.
    """
    import cv2
    import numpy as np
    import ultralytics.data.base as base
    from ultralytics.data.base import BaseDataset

    # CACAT AUDIT 2026-07-30 (diperbaiki): versi lama membangun daftar donor dari
    # SELURUH 1408 PNG lintas split, jadi 192/980 citra TRAIN (19,6%) memakai peta
    # depth milik pohon TEST dan 92/980 (9,4%) milik pohon VAL saat backprop.
    # Peta depth uji tidak boleh pernah dilihat saat latih, sekalipun sebagai
    # kontrol yang sengaja dibuat salah. Sekarang donor dipilih HANYA dari split
    # yang sama, dan dijamin berasal dari POHON yang berbeda.
    pasangan: dict[str, str] = {}
    for split in ("train", "val", "test"):
        berkas = Path(split_dir) / f"{split}.txt"
        if not berkas.is_file():
            continue
        stem = sorted(Path(x.strip()).stem for x in berkas.read_text().splitlines() if x.strip())
        n = len(stem)
        geser = max(4, n // 2)  # >=4 sisi = dijamin lompat ke pohon lain
        for i, s in enumerate(stem):
            donor = stem[(i + geser) % n]
            if _pohon(donor) == _pohon(s):  # pengaman kalau split sangat kecil
                for j in range(1, n):
                    donor = stem[(i + geser + j) % n]
                    if _pohon(donor) != _pohon(s):
                        break
            pasangan[s] = donor
        print(f"depth-tukar[{split}]: {n} citra, donor dari split yang sama")
    sendiri = sum(1 for s, d in pasangan.items() if _pohon(s) == _pohon(d))
    assert sendiri == 0, f"{sendiri} pasangan memakai pohon sendiri"
    print(f"depth-tukar: {len(pasangan)} pasangan, 0 lintas-split, 0 pohon-sendiri")

    orig_init = BaseDataset.__init__

    def patched_init(self, *a, **kw):
        orig_init(self, *a, **kw)
        if getattr(self, "channels", 3) == 4:
            self.cv2_flag = -996

    BaseDataset.__init__ = patched_init
    orig_imread = base.imread

    def imread_tukar(filename, flags=cv2.IMREAD_COLOR):
        if flags != -996:
            return orig_imread(filename, flags)
        bgr = cv2.imread(str(filename), cv2.IMREAD_COLOR)
        if bgr is None:
            return None
        lain = pasangan.get(Path(filename).stem)
        d8 = cv2.imread(f"{depth_dir}/{lain}.png", cv2.IMREAD_GRAYSCALE) if lain else None
        if d8 is None:
            d8 = np.zeros(bgr.shape[:2], np.uint8)
        return np.dstack([bgr, d8])

    base.imread = imread_tukar


def _patch_depth_acak(seed: int) -> None:
    """Kontrol negatif: kanal ke-4 berisi derau, bukan informasi kedalaman.

    Kalau lengan 'RGB-D' derau ini menaikkan mAP sebanyak lengan depth asli,
    maka kenaikannya berasal dari kapasitas tambahan di stem, bukan dari
    kedalaman — dan klaim 'depth menolong' batal.
    """
    import zlib

    import cv2
    import numpy as np
    import ultralytics.data.base as base
    from ultralytics.data.base import BaseDataset

    # CACAT AUDIT 2026-07-30 (diperbaiki): versi lama membuat SATU rng bersama di
    # sini lalu memanggilnya di dalam imread. Akibatnya derau berubah tiap epoch
    # dan tiap pekerja dataloader — jadi lengan derau diam-diam mendapat
    # AUGMENTASI (kanal ke-4 diacak ulang terus-menerus), sementara lengan depth
    # mendapat kanal yang TETAP. Itu bukan kontrol yang setara: derau jadi
    # regularisator. Sekarang seed diturunkan per BERKAS dengan zlib.crc32 —
    # sama seperti padanan RF-DETR — sehingga tiap citra selalu memperoleh pola
    # derau yang sama persis, sebagaimana depth-nya tetap.
    orig_init = BaseDataset.__init__

    def patched_init(self, *a, **kw):
        orig_init(self, *a, **kw)
        if getattr(self, "channels", 3) == 4:
            self.cv2_flag = -998

    BaseDataset.__init__ = patched_init
    orig_imread = base.imread

    def imread_acak(filename, flags=cv2.IMREAD_COLOR):
        if flags != -998:
            return orig_imread(filename, flags)
        bgr = cv2.imread(str(filename), cv2.IMREAD_COLOR)
        if bgr is None:
            return None
        # seed per berkas: stabil lintas epoch, lintas pekerja, dan lintas proses
        # (zlib.crc32 deterministik; hash() diacak PYTHONHASHSEED, jangan dipakai)
        rng = np.random.default_rng(zlib.crc32(Path(filename).stem.encode()) ^ seed)
        derau = rng.integers(0, 256, bgr.shape[:2], dtype=np.uint8)
        return np.dstack([bgr, derau])

    base.imread = imread_acak


if __name__ == "__main__":
    raise SystemExit(main())
