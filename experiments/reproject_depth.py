#!/usr/bin/env python3
"""E-022: SawitMVC-Depth .raw (grid kamera depth) -> PNG kanal-4 kanonik di grid RGB.

MENGGANTIKAN pipeline/prepare_depth.py untuk dataset ini. Skrip lama berasumsi
depth sudah tersejajar ke RGB oleh SDK dan hanya melakukan resize — asumsi itu
DIPALSUKAN untuk dataset ini (lihat depth_calib.py dan verify_depth_mi.py:
MI H3 reproyeksi 0,2638 bit vs H1 resize 0,2381 bit, dengan kontrol pergeseran
+-24 px turun ke ~0,22).

Keluaran: PNG uint8 satu kanal, 1280x800, senama dengan citranya, mengikuti
kontrak pipeline/fourch.py: 0 = tidak ada data, 1..255 = inverse depth pada
rentang metrik TETAP [Z_NEAR, Z_FAR].

Rentang metrik ditentukan dari histogram split TRAIN saja (bukan val/test) —
statistik yang dihitung atas test adalah kebocoran. Angka final dicatat ke
depth_meta.json dan dibekukan bersama bobot.
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import cv2
import numpy as np

from depth_calib import (MAX_VALID_MM, baca_depth_mm, baca_kalibrasi,
                         encode_inverse, reproyeksi, tambal_lubang)

DATA = Path("/workspace/SawitMVC-Depth/data")


def peta_metrik(stem: str) -> np.ndarray:
    """.raw -> peta depth (mm) di grid RGB 1280x800, lubang sudah ditambal."""
    z = baca_depth_mm(DATA / "depth" / f"{stem}.raw")
    kal = baca_kalibrasi(DATA / "depth" / f"{stem}.json")
    return tambal_lubang(reproyeksi(z, kal))


def _kerja(argumen: tuple[str, str, float, float]) -> tuple[str, int, int]:
    stem, tujuan, zn, zf = argumen
    peta = peta_metrik(stem)
    png = encode_inverse(peta, zn, zf)
    cv2.imwrite(str(Path(tujuan) / f"{stem}.png"), png)
    return stem, int((png > 0).sum()), png.size


def statistik_train(stems: list[str], contoh: int = 120) -> dict:
    """Histogram depth pasca-reproyeksi pada TRAIN saja -> pilih Z_NEAR/Z_FAR."""
    rng = np.random.default_rng(42)
    pilih = [stems[i] for i in rng.choice(len(stems), min(contoh, len(stems)), replace=False)]
    nilai = []
    invalid = []
    for s in pilih:
        p = peta_metrik(s)
        v = p[p > 0]
        invalid.append(1.0 - v.size / p.size)
        if v.size:
            nilai.append(rng.choice(v, min(20000, v.size), replace=False))
    semua = np.concatenate(nilai)
    persentil = {f"p{q}": float(np.percentile(semua, q)) for q in (0.1, 1, 5, 25, 50, 75, 95, 99, 99.9)}

    sapuan = []
    for zn in (0.5, 0.6, 0.7, 0.8, 1.0):
        for zf in (8.0, 10.0, 12.0, 15.0):
            kode = encode_inverse(semua, zn, zf)
            h = np.bincount(kode[kode > 0], minlength=256)[1:].astype(np.float64)
            h /= h.sum()
            nz = h > 0
            sapuan.append({
                "z_near": zn, "z_far": zf,
                "entropi_bit": float(-(h[nz] * np.log2(h[nz])).sum()),
                "saturasi_dekat": float(np.mean(semua < zn * 1000)),
                "saturasi_jauh": float(np.mean(semua > zf * 1000)),
                "level_median": int(np.median(kode[kode > 0])),
            })
    return {"n_citra_contoh": len(pilih), "invalid_rerata": float(np.mean(invalid)),
            "persentil_mm": persentil, "sapuan_z": sapuan}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split-train", type=Path, default=Path("splits_depth/fold0/train.txt"),
                    help="dipakai HANYA untuk memilih Z_NEAR/Z_FAR (anti-kebocoran)")
    ap.add_argument("--tujuan", type=Path, default=Path("depth_png"))
    ap.add_argument("--z-near", type=float, default=None, help="paksa nilai; default: pilih dari train")
    ap.add_argument("--z-far", type=float, default=None)
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()

    args.tujuan.mkdir(parents=True, exist_ok=True)
    semua_stem = sorted(p.stem for p in (DATA / "depth").glob("*.raw"))
    print(f"{len(semua_stem)} berkas depth ditemukan")

    zn, zf = args.z_near, args.z_far
    stat = None
    if zn is None or zf is None:
        if not args.split_train.is_file():
            raise SystemExit(f"butuh {args.split_train} untuk memilih rentang metrik "
                             f"(atau berikan --z-near/--z-far eksplisit)")
        train_stems = [Path(x.strip()).stem for x in args.split_train.read_text().splitlines() if x.strip()]
        print(f"menghitung histogram pada {len(train_stems)} citra TRAIN...")
        stat = statistik_train(train_stems)
        # pilih pasangan dengan entropi tertinggi yang saturasi dekat <= 5%
        layak = [s for s in stat["sapuan_z"] if s["saturasi_dekat"] <= 0.05]
        terbaik = max(layak, key=lambda s: s["entropi_bit"])
        zn, zf = terbaik["z_near"], terbaik["z_far"]
        print(f"rentang terpilih: Z_NEAR={zn} Z_FAR={zf} "
              f"(entropi {terbaik['entropi_bit']:.2f} bit, level median {terbaik['level_median']})")

    tugas = [(s, str(args.tujuan), zn, zf) for s in semua_stem]
    hasil = []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        for i, r in enumerate(ex.map(_kerja, tugas, chunksize=4)):
            hasil.append(r)
            if (i + 1) % 200 == 0:
                print(f"  {i + 1}/{len(tugas)}")

    n_png = len(list(args.tujuan.glob("*.png")))
    if n_png != len(semua_stem):
        raise SystemExit(f"GAGAL: {n_png} PNG dari {len(semua_stem)} berkas depth")

    cakupan = float(np.mean([v / t for _, v, t in hasil]))
    meta = {
        "sumber": str(DATA),
        "pemetaan": "reproyeksi penuh (intrinsik depth -> 3D -> ekstrinsik -> intrinsik color + Brown-Conrady K6), forward-warp z-buffer, tambal lubang median-3x3 dua iterasi",
        "z_near_m": zn, "z_far_m": zf,
        "invalid_mm_di_atas": MAX_VALID_MM,
        "kontrak": "PNG uint8 1 kanal 1280x800; 0 = tidak ada data; 1..255 inverse depth pada [z_near, z_far]",
        "n_berkas": n_png,
        "cakupan_piksel_valid_rerata": cakupan,
        "statistik_train": stat,
    }
    (args.tujuan / "depth_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"\nselesai: {n_png} PNG di {args.tujuan}")
    print(f"cakupan piksel valid rata-rata: {cakupan:.3f}")
    print(f"meta -> {args.tujuan / 'depth_meta.json'}")


if __name__ == "__main__":
    main()
