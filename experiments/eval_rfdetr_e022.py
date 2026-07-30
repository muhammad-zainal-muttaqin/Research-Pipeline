#!/usr/bin/env python3
"""E-022: evaluasi test RF-DETR Nano (RGB & RGB-D) dari checkpoint_best_ema.pth.

Dipakai karena tahap `run_test` bawaan rfdetr tidak pernah jalan pada run RGB-D:
prosesnya mati saat menulis checkpoint epoch 60 ketika kuota disk habis
(checkpoint_59.ckpt terpotong tepat di 256 MB). Seluruh 60 epoch latih+val sudah
tuntas dan checkpoint EMA terbaik selamat, jadi tidak perlu latih ulang.

Konsisten dengan E-021: dipakai checkpoint EMA untuk val maupun test.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np

from eval_e022_pycoco import NAMES, bangun_gt, pohon_dari
from eval_e022_paired import map50_semua

DEPTH_DIR = Path("/workspace/experiments/depth_png")


def muat(ckpt: str, modal: str, resolution: int):
    import train_rfdetr_4ch as t4
    from rfdetr import RFDETRNano

    kw = {"pretrain_weights": ckpt, "resolution": resolution}
    if modal in ("rgbd", "derau"):
        t4.patch_c0_validasi_kanal(paksa_init_4=True)
        kw["num_channels"] = 4
    return RFDETRNano(**kw)


def masukan(p: Path, modal: str) -> np.ndarray:
    """RF-DETR mengharap RGB (bukan BGR). Kanal ke-4 sesuai modalitas."""
    import zlib
    bgr = cv2.imread(str(p), cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    if modal == "rgb":
        return rgb
    if modal == "derau":
        # seed CRC32 per berkas — sama seperti saat latih, reproducible
        rng = np.random.default_rng(zlib.crc32(p.stem.encode()))
        d8 = rng.integers(0, 256, rgb.shape[:2], dtype=np.uint8)
    else:
        d = DEPTH_DIR / f"{p.stem}.png"
        d8 = cv2.imread(str(d), cv2.IMREAD_GRAYSCALE) if d.is_file() else None
        if d8 is None:
            d8 = np.zeros(rgb.shape[:2], np.uint8)
    return np.dstack([rgb, d8])


def prediksi(model, paths: list[Path], peta: dict[str, int], modal: str) -> list[dict]:
    dets = []
    for p in paths:
        d = model.predict(masukan(p, modal), threshold=0.001)
        if isinstance(d, list):
            d = d[0]
        img_id = peta[p.stem]
        for k in range(len(d.xyxy)):
            x1, y1, x2, y2 = d.xyxy[k]
            dets.append({"image_id": img_id, "category_id": int(d.class_id[k]) + 1,
                         "bbox": [float(x1), float(y1), float(x2 - x1), float(y2 - y1)],
                         "score": float(d.confidence[k])})
    return dets


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="test")
    ap.add_argument("--split-dir", default="/workspace/experiments/splits_depth/seed42")
    ap.add_argument("--resolution", type=int, default=640)
    ap.add_argument("--B", type=int, default=2000)
    ap.add_argument("--a", default="runs_e022/rfdetrnano_rgb", help="run lengan A")
    ap.add_argument("--modal-a", default="rgb", choices=["rgb", "rgbd", "derau"])
    ap.add_argument("--b", default="runs_e022/rfdetrnano_rgbd", help="run lengan B")
    ap.add_argument("--modal-b", default="rgbd", choices=["rgb", "rgbd", "derau"])
    ap.add_argument("--keluaran", default="results/e022_paired_rfdetrnano.json")
    args = ap.parse_args()

    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    gt, peta = bangun_gt(paths)
    img_ids = [peta[p.stem] for p in paths]
    print(f"{args.split}: {len(paths)} citra, {len(gt.dataset['annotations'])} kotak GT")

    dt = {}
    for label, run, modal in (("rgb", args.a, args.modal_a), ("rgbd", args.b, args.modal_b)):
        ckpt = f"{run}/checkpoint_best_ema.pth"
        print(f"prediksi {label} ({modal}) dari {ckpt} ...")
        model = muat(ckpt, modal, args.resolution)
        dt[label] = gt.loadRes(prediksi(model, paths, peta, modal))
        del model

    titik = {k: map50_semua(gt, dt[k], img_ids) for k in dt}

    pohon = sorted({pohon_dari(p.stem) for p in paths})
    per_pohon = {t: [peta[p.stem] for p in paths if pohon_dari(p.stem) == t] for t in pohon}
    rng = np.random.default_rng(42)
    selisih = {m: [] for m in ["mAP50", *NAMES]}
    print(f"bootstrap berpasangan {args.B}x pada {len(pohon)} pohon ...")
    for _ in range(args.B):
        contoh = rng.choice(len(pohon), len(pohon), replace=True)
        ids = [i for k in contoh for i in per_pohon[pohon[k]]]
        try:
            a = map50_semua(gt, dt["rgbd"], ids)
            b = map50_semua(gt, dt["rgb"], ids)
        except Exception:
            continue
        for m in selisih:
            if not (np.isnan(a[m]) or np.isnan(b[m])):
                selisih[m].append(a[m] - b[m])

    hasil = {"titik": titik, "delta": {}, "n_pohon": len(pohon)}
    for m, v in selisih.items():
        d = np.array(v)
        hasil["delta"][m] = {
            "titik": float(titik["rgbd"][m] - titik["rgb"][m]),
            "ci95": [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))],
            "frac_positif": float(np.mean(d > 0)), "B_efektif": int(d.size),
        }
    hasil["delta_mAP50"] = hasil["delta"]["mAP50"]["titik"]
    hasil["delta_ci95"] = hasil["delta"]["mAP50"]["ci95"]

    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hasil, indent=2))

    print(f"\n{'metrik':8s} {'RGB':>8s} {'RGB-D':>8s} {'delta':>9s} {'CI95':>22s} {'P(>0)':>7s}")
    for m in ["mAP50", *NAMES]:
        r = hasil["delta"][m]
        ci = f"[{r['ci95'][0]:+.4f}, {r['ci95'][1]:+.4f}]"
        print(f"{m:8s} {titik['rgb'][m]:8.4f} {titik['rgbd'][m]:8.4f} "
              f"{r['titik']:+9.4f} {ci:>22s} {r['frac_positif']:7.3f}")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
