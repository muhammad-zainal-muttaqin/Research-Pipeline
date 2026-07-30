#!/usr/bin/env python3
"""E-022: uji berpasangan RGB-D vs RGB — CI bootstrap atas SELISIHNYA.

CI terpisah per lengan tidak menjawab H-022. Yang diuji adalah selisih, dan
karena kedua lengan dinilai pada citra yang SAMA, bootstrap harus berpasangan:
resample pohon sekali, lalu hitung mAP50 kedua lengan pada himpunan pohon yang
sama itu, baru ambil selisihnya. Ini menghapus varians bersama (pohon sulit vs
pohon mudah) dan memberi CI yang jauh lebih tajam daripada dua CI terpisah.

Resample pada tingkat POHON, bukan citra: 4 sisi satu pohon tidak independen,
resample per citra membuat CI terlalu sempit.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
PIPELINE_ROOT = REPO_ROOT / "reproduce" / "pipeline"

import numpy as np
from pycocotools.cocoeval import COCOeval

from eval_e022_pycoco import NAMES, bangun_gt, pohon_dari, prediksi

_GT = None
_DT = None
METRIK = ["mAP50", "mAP50-95", *NAMES, *(f"{n}_5095" for n in NAMES)]


def _satu_bootstrap(ids):
    """Satu iterasi bootstrap di proses pekerja (GT/DT diwarisi lewat fork)."""
    try:
        a = map50_semua(_GT, _DT["rgbd"], ids)
        b = map50_semua(_GT, _DT["rgb"], ids)
    except Exception:
        return None
    return {m: a[m] - b[m] for m in METRIK
            if not (np.isnan(a[m]) or np.isnan(b[m]))}


def map50_semua(gt, dt, img_ids: list[int]) -> dict[str, float]:
    """mAP50 keseluruhan + AP50 per kelas dari SATU kali COCOeval.

    `accumulate()` mengisi `eval["precision"]` berbentuk [T,R,K,A,M] dengan K =
    kategori, jadi seluruh kelas sudah tersedia dalam satu evaluasi. Memanggil
    COCOeval terpisah per kelas (cara lama) 5x lebih mahal tanpa tambahan
    informasi apa pun — dan di dalam loop bootstrap perbedaannya menentukan
    apakah uji per-kelas bisa dijalankan sama sekali.

    Sekalian dihitung mAP50-95 (rata-rata 10 ambang IoU 0,50:0,05:0,95, gaya
    COCO) dari MATRIKS PRESISI YANG SAMA — accumulate() sudah mengisi semua T,
    jadi ini tidak menambah COCOeval sama sekali, hanya menambah agregasi.
    Kunci mAP50 & per-kelas AP50 lama TIDAK disentuh (masih t50 = indeks 0
    saja); mAP50-95 ditambahkan sebagai kunci BARU ("mAP50-95" + "{n}_5095"
    per kelas), sama seperti nilai -1 (tidak ada data) tetap dibuang sebelum
    dirata-ratakan, persis pola yang sudah dipakai untuk AP50.
    """
    ev = COCOeval(gt, dt, "bbox")
    ev.params.imgIds = img_ids
    with contextlib.redirect_stdout(io.StringIO()):
        ev.evaluate(); ev.accumulate()
    pr = ev.eval["precision"]  # [T, R, K, A, M]
    t50 = 0  # ev.params.iouThrs[0] == 0.5
    keluar = {}
    ap_kelas = []
    ap_kelas_5095 = []
    for k, n in enumerate(NAMES):
        p = pr[t50, :, k, 0, -1]
        p = p[p > -1]
        ap = float(p.mean()) if p.size else float("nan")
        keluar[n] = ap
        if not np.isnan(ap):
            ap_kelas.append(ap)

        # mAP50-95 per kelas: SEMUA ambang T (bukan cuma t50), sisanya sama —
        # -1 dibuang sebelum dirata-ratakan.
        p5095 = pr[:, :, k, 0, -1]  # [T, R]
        p5095 = p5095[p5095 > -1]
        ap5095 = float(p5095.mean()) if p5095.size else float("nan")
        keluar[f"{n}_5095"] = ap5095
        if not np.isnan(ap5095):
            ap_kelas_5095.append(ap5095)
    keluar["mAP50"] = float(np.mean(ap_kelas)) if ap_kelas else 0.0
    keluar["mAP50-95"] = float(np.mean(ap_kelas_5095)) if ap_kelas_5095 else 0.0
    return keluar


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rgb", required=True, help="folder run lengan RGB")
    ap.add_argument("--rgbd", required=True, help="folder run lengan RGB-D")
    ap.add_argument("--modal-a", default="rgb", choices=["rgb", "rgbd", "derau", "tukar"],
                    help="modalitas lengan pertama (default rgb)")
    ap.add_argument("--modal-b", default="rgbd", choices=["rgbd", "derau", "tukar"],
                    help="modalitas lengan kedua (derau = kontrol negatif)")
    ap.add_argument("--split", default="test")
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--seed", type=int, default=42,
                    help="seed modalitas kontrol; harus sama dengan seed training")
    ap.add_argument("--B", type=int, default=2000)
    ap.add_argument("--keluaran", default="results/e022_paired.json")
    args = ap.parse_args()

    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    gt, peta = bangun_gt(paths)
    img_ids = [peta[p.stem] for p in paths]

    dets = {}
    for label, run, modal in (("rgb", args.rgb, args.modal_a), ("rgbd", args.rgbd, args.modal_b)):
        print(f"prediksi {label} ...")
        dets[label] = prediksi(str(Path(run) / "weights" / "best.pt"), paths, peta,
                               args.imgsz, modal, seed=args.seed)
    dt = {k: gt.loadRes(v) for k, v in dets.items()}

    titik = {}
    for k in dt:
        s = map50_semua(gt, dt[k], img_ids)
        titik[k] = {
            "mAP50": s["mAP50"],
            "mAP50-95": s["mAP50-95"],
            "AP50_perkelas": {n: s[n] for n in NAMES},
            "AP50-95_perkelas": {n: s[f"{n}_5095"] for n in NAMES},
        }

    pohon = sorted({pohon_dari(p.stem) for p in paths})
    per_pohon = {t: [peta[p.stem] for p in paths if pohon_dari(p.stem) == t] for t in pohon}
    rng = np.random.default_rng(42)
    # Bootstrap itu embarrassingly parallel dan mesin ini punya 128 core, tetapi
    # loop serial hanya memakai ~1. Indeks resample dibangkitkan LEBIH DULU dari
    # satu rng ber-seed, jadi hasilnya identik dengan versi serial dan tidak
    # bergantung urutan penyelesaian proses.
    daftar_ids = []
    for _ in range(args.B):
        contoh = rng.choice(len(pohon), len(pohon), replace=True)
        daftar_ids.append([i for k in contoh for i in per_pohon[pohon[k]]])

    selisih = {m: [] for m in METRIK}
    n_proc = min(32, max(1, (os.cpu_count() or 8) // 4))
    print(f"bootstrap berpasangan {args.B}x pada {len(pohon)} pohon, {n_proc} proses ...")

    global _GT, _DT
    _GT, _DT = gt, dt
    with ProcessPoolExecutor(max_workers=n_proc) as ex:
        for hasil_iter in ex.map(_satu_bootstrap, daftar_ids, chunksize=8):
            if hasil_iter is None:
                continue
            for m, v in hasil_iter.items():
                selisih[m].append(v)

    hasil = {"n_pohon": len(pohon), "n_citra": len(paths), "titik": titik, "delta": {}}
    for m, v in selisih.items():
        d = np.array(v)
        if m in ("mAP50", "mAP50-95"):
            titik_delta = titik["rgbd"][m] - titik["rgb"][m]
        elif m.endswith("_5095"):
            kelas = m.removesuffix("_5095")
            titik_delta = (titik["rgbd"]["AP50-95_perkelas"][kelas]
                           - titik["rgb"]["AP50-95_perkelas"][kelas])
        else:
            titik_delta = (titik["rgbd"]["AP50_perkelas"][m]
                           - titik["rgb"]["AP50_perkelas"][m])
        hasil["delta"][m] = {
            "titik": float(titik_delta),
            "ci95": [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))],
            "rerata_boot": float(d.mean()),
            "frac_positif": float(np.mean(d > 0)),
            "B_efektif": int(d.size),
        }
    hasil["delta_mAP50"] = hasil["delta"]["mAP50"]["titik"]
    hasil["delta_ci95"] = hasil["delta"]["mAP50"]["ci95"]
    hasil["frac_boot_positif"] = hasil["delta"]["mAP50"]["frac_positif"]
    out = Path(args.keluaran)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hasil, indent=2))

    print(f"\n{'metrik':8s} {'RGB':>8s} {'RGB-D':>8s} {'delta':>9s} {'CI95':>22s} {'P(>0)':>7s}")
    for m in ["mAP50", *NAMES]:
        r = hasil["delta"][m]
        v_rgb = titik["rgb"]["mAP50"] if m == "mAP50" else titik["rgb"]["AP50_perkelas"][m]
        v_rgbd = titik["rgbd"]["mAP50"] if m == "mAP50" else titik["rgbd"]["AP50_perkelas"][m]
        ci = f"[{r['ci95'][0]:+.4f}, {r['ci95'][1]:+.4f}]"
        print(f"{m:8s} {v_rgb:8.4f} {v_rgbd:8.4f} {r['titik']:+9.4f} {ci:>22s} {r['frac_positif']:7.3f}")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
