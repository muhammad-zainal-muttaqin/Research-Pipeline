#!/usr/bin/env python3
"""Rezim pengukuran seri F — bootstrap tingkat POHON, persentil + BCa.

## Kenapa bukan `eval_extras.py`

`eval_extras.py` (E-021) me-resample **citra**, 2.000 replikat, hanya mAP50.
Itu salah unit untuk dataset ini: satu pohon menyumbang 4-8 citra dari sudut
berbeda, dan sisi-sisi itu memuat TANDAN FISIK YANG SAMA (graf `_confirmedLinks`,
k ~ 1,89). Resample citra memperlakukan 4 pandangan atas satu pohon sebagai 4
pengamatan bebas, sehingga CI-nya terlalu sempit dan selisih antar-lengan tampak
lebih meyakinkan daripada sebenarnya.

Berkas ini me-resample **pohon** (unit yang benar-benar bebas), 10.000 replikat,
dan melaporkan interval persentil **dan** BCa untuk mAP50, mAP50-95, serta AP50
tiap kelas.

## Masukan: `.npz` dump, bukan inferensi kedua

`eval/dump_logits_rfdetr.py` sudah menyimpan logit mentah dan kotak SELURUH
query. Deteksi yang dipancarkan `PostProcess` dapat direkonstruksi dari situ
PERSIS -- top-k `num_select` atas `sigmoid(z)` pada grid datar Q x C
(`postprocess.py:106`) -- sehingga satu inferensi melayani F-005 dan berkas ini
sekaligus. Tidak ada jalur skor kedua yang bisa menyimpang diam-diam.

## Berpasangan

Bila dua `.npz` diberikan, selisihnya dihitung pada **replikat pohon yang sama**
(paired bootstrap). Itu membuang varians antar-pohon yang dimiliki bersama kedua
lengan, dan merupakan satu-satunya cara sah membandingkan baseline dengan
perlakuan yang dilatih dari seed dan urutan data yang sama.

Pemakaian:
  python eval/bootstrap_pohon.py --npz-a results/F-004/logits_test_seed42.npz
  python eval/bootstrap_pohon.py --npz-a base.npz --npz-b perlakuan.npz --label-b K2
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
DS = Path(__file__).resolve().parents[1] / "rfdetr_ds"

import numpy as np

KELAS = ["B1", "B2", "B3", "B4"]
SPLIT_DIR = {"val": "valid", "test": "test"}
IOU_THR = np.arange(0.5, 0.96, 0.05)     # 10 ambang COCO
NUM_SELECT = 300                          # sama dengan RFDETRLarge


def muat_gt(split: str, nama: list[str], ukuran: np.ndarray):
    """GT xyxy piksel per citra, per kelas."""
    ldir = DS / SPLIT_DIR[split] / "labels"
    gt: dict[tuple[int, int], list] = {}
    for i, stem in enumerate(nama):
        h, w = int(ukuran[i][0]), int(ukuran[i][1])
        lf = ldir / f"{stem}.txt"
        if not lf.is_file():
            continue
        for line in lf.read_text().splitlines():
            if not line.strip():
                continue
            c, cx, cy, bw, bh = map(float, line.split())
            gt.setdefault((i, int(c)), []).append(
                [(cx - bw / 2) * w, (cy - bh / 2) * h,
                 (cx + bw / 2) * w, (cy + bh / 2) * h])
    return gt


def deteksi_dari_npz(logits: np.ndarray, boxes: np.ndarray, num_select: int = NUM_SELECT):
    """Rekonstruksi keluaran PostProcess: (skor, kelas, kotak) top-k per citra."""
    z = logits.astype(np.float32)
    prob = 1.0 / (1.0 + np.exp(-z))          # (Q, C)
    datar = prob.ravel()
    k = min(num_select, datar.size)
    idx = np.argpartition(-datar, k - 1)[:k]
    idx = idx[np.argsort(-datar[idx])]
    q, c = idx // z.shape[1], idx % z.shape[1]
    return datar[idx], c, boxes[q]


def iou_xyxy(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ix1 = np.maximum(a[:, None, 0], b[None, :, 0])
    iy1 = np.maximum(a[:, None, 1], b[None, :, 1])
    ix2 = np.minimum(a[:, None, 2], b[None, :, 2])
    iy2 = np.minimum(a[:, None, 3], b[None, :, 3])
    iw = np.clip(ix2 - ix1, 0, None)
    ih = np.clip(iy2 - iy1, 0, None)
    inter = iw * ih
    aa = (a[:, 2] - a[:, 0]) * (a[:, 3] - a[:, 1])
    bb = (b[:, 2] - b[:, 0]) * (b[:, 3] - b[:, 1])
    return np.where(inter > 0, inter / np.maximum(aa[:, None] + bb[None, :] - inter, 1e-9), 0.0)


def cocokkan(npz_path: str):
    """Per (citra, kelas): skor terurut + tp pada 10 ambang IoU, plus nGT.

    Pencocokan greedy menurut skor, satu GT dipakai sekali per ambang -- kaidah
    yang sama dengan pycocotools (dan `eval_extras.py`, yang hanya IoU 0,5).
    """
    d = np.load(npz_path, allow_pickle=True)
    nama = [str(x) for x in d["nama"]]
    split = str(d["split"][0])
    gt = muat_gt(split, nama, d["ukuran"])

    per: dict[tuple[int, int], tuple] = {}
    ngt: dict[tuple[int, int], int] = {}
    for i in range(len(nama)):
        sk, kl, kt = deteksi_dari_npz(d["logits"][i], d["boxes"][i])
        for c in range(len(KELAS)):
            g = np.array(gt.get((i, c), []), np.float32).reshape(-1, 4)
            ngt[(i, c)] = len(g)
            m = kl == c
            if not m.any():
                per[(i, c)] = (np.zeros(0, np.float32), np.zeros((len(IOU_THR), 0), np.float32))
                continue
            s, b = sk[m], kt[m].astype(np.float32)
            tp = np.zeros((len(IOU_THR), len(s)), np.float32)
            if len(g):
                io = iou_xyxy(b, g)               # (n_det, n_gt), sudah urut skor
                for t, thr in enumerate(IOU_THR):
                    dipakai = np.zeros(len(g), bool)
                    for n in range(len(s)):
                        v = io[n].copy()
                        v[dipakai] = -1
                        j = int(np.argmax(v))
                        if v[j] >= thr:
                            tp[t, n] = 1
                            dipakai[j] = True
            per[(i, c)] = (s, tp)
    return nama, per, ngt


def ap_dari(scores: np.ndarray, tp: np.ndarray, ngt: int) -> float:
    """AP COCO 101 titik dari (skor, tp) yang SUDAH digabung."""
    if ngt == 0:
        return float("nan")
    if scores.size == 0:
        return 0.0
    o = np.argsort(-scores)
    t = tp[o]
    ctp = np.cumsum(t)
    cfp = np.cumsum(1 - t)
    rec = ctp / ngt
    prec = ctp / np.maximum(ctp + cfp, 1e-9)
    prec = np.maximum.accumulate(prec[::-1])[::-1]
    rthr = np.linspace(0, 1, 101)
    idx = np.searchsorted(rec, rthr, side="left")
    p = np.where(idx < len(prec), prec[np.clip(idx, 0, len(prec) - 1)], 0.0)
    return float(p.mean())


def metrik(idx_citra: np.ndarray, per, ngt) -> dict:
    """mAP50, mAP50-95, AP50 per kelas untuk himpunan citra tertentu."""
    ap50_k, ap5095_k = [], []
    hasil = {}
    for c in range(len(KELAS)):
        n = int(sum(ngt[(i, c)] for i in idx_citra))
        s = np.concatenate([per[(i, c)][0] for i in idx_citra]) if len(idx_citra) else np.zeros(0)
        t = (np.concatenate([per[(i, c)][1] for i in idx_citra], axis=1)
             if len(idx_citra) else np.zeros((len(IOU_THR), 0)))
        a50 = ap_dari(s, t[0], n)
        a_all = [ap_dari(s, t[k], n) for k in range(len(IOU_THR))]
        hasil[f"AP50_{KELAS[c]}"] = a50
        if not np.isnan(a50):
            ap50_k.append(a50)
            ap5095_k.append(float(np.nanmean(a_all)))
    hasil["mAP50"] = float(np.mean(ap50_k)) if ap50_k else float("nan")
    hasil["mAP50_95"] = float(np.mean(ap5095_k)) if ap5095_k else float("nan")
    return hasil


def bca(boot: np.ndarray, amatan: float, jack: np.ndarray, alpha: float = 0.05):
    """Interval bias-corrected and accelerated.

    Persentil saja menganggap sebaran bootstrap tidak bias dan berskala tetap.
    BCa mengoreksi keduanya lewat z0 (bias) dan a (percepatan, dari jackknife).
    Rezim §5.2 menuntut keduanya dilaporkan.
    """
    from scipy.stats import norm
    boot = boot[~np.isnan(boot)]
    if boot.size < 100:
        return [float("nan"), float("nan")]
    prop = float((boot < amatan).mean())
    prop = min(max(prop, 1e-6), 1 - 1e-6)
    z0 = norm.ppf(prop)
    jm = np.nanmean(jack)
    num = float(np.nansum((jm - jack) ** 3))
    den = 6.0 * float(np.nansum((jm - jack) ** 2)) ** 1.5
    a = num / den if den else 0.0
    out = []
    for q in (alpha / 2, 1 - alpha / 2):
        zq = norm.ppf(q)
        adj = z0 + (z0 + zq) / max(1 - a * (z0 + zq), 1e-9)
        out.append(float(np.percentile(boot, 100 * norm.cdf(adj))))
    return [round(out[0], 4), round(out[1], 4)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz-a", required=True)
    ap.add_argument("--npz-b", default=None, help="lengan kedua; hasilnya kontras berpasangan")
    ap.add_argument("--label-a", default="A")
    ap.add_argument("--label-b", default="B")
    ap.add_argument("--replikat", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--keluaran", required=True)
    args = ap.parse_args()

    nama, per_a, ngt_a = cocokkan(args.npz_a)
    per_b = ngt_b = None
    if args.npz_b:
        nama_b, per_b, ngt_b = cocokkan(args.npz_b)
        if nama_b != nama:
            raise RuntimeError("urutan citra dua npz berbeda; kontras tidak sah")

    # Unit resample = POHON. stem "<pohon>_<sisi>" -> pohon.
    pohon: dict[str, list[int]] = {}
    for i, s in enumerate(nama):
        pohon.setdefault(s.rsplit("_", 1)[0], []).append(i)
    kunci = sorted(pohon)
    print(f"{len(nama)} citra, {len(kunci)} pohon, {args.replikat} replikat")

    semua = np.arange(len(nama))
    amat_a = metrik(semua, per_a, ngt_a)
    amat_b = metrik(semua, per_b, ngt_b) if per_b else None

    kunci_metrik = ["mAP50", "mAP50_95"] + [f"AP50_{k}" for k in KELAS]
    rng = np.random.default_rng(args.seed)
    boot = {k: [] for k in kunci_metrik}
    boot_d = {k: [] for k in kunci_metrik}
    for r in range(args.replikat):
        pilih = rng.integers(0, len(kunci), len(kunci))
        idx = np.concatenate([pohon[kunci[j]] for j in pilih])
        ma = metrik(idx, per_a, ngt_a)
        for k in kunci_metrik:
            boot[k].append(ma[k])
        if per_b:
            mb = metrik(idx, per_b, ngt_b)
            for k in kunci_metrik:
                boot_d[k].append(mb[k] - ma[k])
        if (r + 1) % 1000 == 0:
            print(f"  replikat {r + 1}/{args.replikat}", flush=True)

    # Jackknife per POHON (untuk percepatan BCa).
    jack = {k: [] for k in kunci_metrik}
    jack_d = {k: [] for k in kunci_metrik}
    for j in range(len(kunci)):
        idx = np.concatenate([pohon[kunci[m]] for m in range(len(kunci)) if m != j])
        ma = metrik(idx, per_a, ngt_a)
        for k in kunci_metrik:
            jack[k].append(ma[k])
        if per_b:
            mb = metrik(idx, per_b, ngt_b)
            for k in kunci_metrik:
                jack_d[k].append(mb[k] - ma[k])

    def ringkas(bt, amatan, jk):
        b = np.array(bt, float)
        return {
            "titik": round(float(amatan), 4),
            "ci95_persentil": [round(float(np.nanpercentile(b, 2.5)), 4),
                               round(float(np.nanpercentile(b, 97.5)), 4)],
            "ci95_bca": bca(b, float(amatan), np.array(jk, float)),
            "sd_bootstrap": round(float(np.nanstd(b)), 4),
        }

    lap = {
        "unit_resample": "POHON",
        "alasan_unit": "citra satu pohon dan sisi tertaut satu tandan berkorelasi (k ~ 1,89)",
        "n_citra": len(nama), "n_pohon": len(kunci),
        "replikat": args.replikat, "seed": args.seed,
        "npz_a": args.npz_a, "label_a": args.label_a,
        args.label_a: {k: ringkas(boot[k], amat_a[k], jack[k]) for k in kunci_metrik},
    }
    if per_b:
        lap["npz_b"] = args.npz_b
        lap["label_b"] = args.label_b
        lap[args.label_b] = {k: round(float(amat_b[k]), 4) for k in kunci_metrik}
        lap["kontras_berpasangan_B_minus_A"] = {
            k: ringkas(boot_d[k], amat_b[k] - amat_a[k], jack_d[k]) for k in kunci_metrik
        }
        lap["catatan_kontras"] = (
            "CI yang memuat nol = TIDAK KONKLUSIF. Jangan dinaikkan jadi INDIKASI "
            "tanpa replikasi multi-seed (pelajaran E-032, E-033b).")

    Path(args.keluaran).parent.mkdir(parents=True, exist_ok=True)
    Path(args.keluaran).write_text(json.dumps(lap, indent=2, ensure_ascii=False))
    print(json.dumps(lap, indent=2, ensure_ascii=False))
    print(f"\n-> {args.keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
