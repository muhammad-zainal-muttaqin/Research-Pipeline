#!/usr/bin/env python3
"""F-002 (P2) — Apakah respons frekuensi tinggi memisahkan tandan dari PELEPAH?

Gerbang untuk K1 (cabang frekuensi samping). Dijalankan SEBELUM satu jam GPU
pun terpakai, disiplin yang sama seperti E-006, E-010, dan E-011.

## Kenapa E-011 belum menjawab ini

E-011 (`contrast_boost_test.py`) mengukur **isi kotak vs cincin sekeliling** dan
menemukan Laplacian menaikkan keterpisahan B4 sebesar +0,0458 di atas kendali,
mengungguli Sobel (+0,0367). Itu hasil nyata, tetapi cincin sekeliling memuat
APA SAJA — langit, batang, tanah, tandan lain.

Mode gagal yang dikhawatirkan justru spesifik: **cabang frekuensi tinggi menyala
pada tepi pelepah**, bukan pada isi tandan. Pelepah sawit adalah struktur
berfrekuensi sangat tinggi (anak daun tipis berulang), dan B4 yang gelap
kehijauan justru kelas yang paling menyatu dengannya (CLAUDE.md §"Arah kelas").
Kalau frekuensi tinggi tidak memisahkan tandan dari pelepah, cabang K1 akan
belajar menyalakan pelepah dan kenaikan apa pun yang muncul bukan berasal dari
mekanisme yang diklaim.

Berkas ini karena itu mendefinisikan ulang wilayah pembanding:

    pelepah = cincin sekeliling kotak  MINUS  seluruh kotak GT tandan lain

sehingga yang tersisa adalah vegetasi/pelepah murni, bukan tandan tetangga.

## Lengan yang diuji

  asli       luminans L (acuan, bukan frekuensi tinggi)
  gradmag    besar gradien Sobel        -- pembanding E-011 (+0,0367 pada cincin)
  laplacian  respons Laplacian          -- pembanding E-011 (+0,0458 pada cincin)
  dwt_lh/hl/hh  sub-band Haar satu tingkat  -- yang diusulkan K1
  dwt_energi    sqrt(LH^2 + HL^2 + HH^2)    -- ringkasan tiga sub-band

Seluruh peta frekuensi tinggi dihaluskan Gaussian sigma=2 PERSIS seperti E-011
memperlakukan gradmag dan laplacian. Tanpa itu perbandingan DWT vs Laplacian
tercemar oleh beda penghalusan, bukan beda kandungan frekuensi.

DWT Haar ditulis langsung dengan numpy: `pywt` tidak terpasang di venv ini, dan
Haar satu tingkat cukup pendek sehingga menambah dependensi tidak sepadan.

## Yang memalsukan (ditulis sebelum melihat hasil)

K1 GUGUR bila tidak ada satu pun lengan frekuensi tinggi yang menaikkan AUC
tandan-vs-pelepah lebih dari **+0,02** di atas kendali kotak acak pada B4.
Ambang +0,02 diambil dari E-011 supaya kedua uji dapat dibaca pada skala yang
sama.

Pemakaian:  python analysis/freq_vs_pelepah.py --images 250
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
SPLIT_TEST = EVIDENCE_ROOT / "splits_rgb" / "sawitmvc" / "test.txt"
CLASSES = ["B1", "B2", "B3", "B4"]

# Piksel minimum agar sebuah wilayah dianggap dapat diukur. Wilayah pelepah bisa
# menyusut drastis pada citra padat setelah kotak tandan lain dikurangkan;
# yang tersisa terlalu kecil ditolak dan DIHITUNG, bukan didiamkan.
MIN_PIKSEL = 200


def load_boxes(stem: str) -> list[list[float]]:
    """Baca label YOLO -> [kelas, cx, cy, w, h] ternormalisasi."""
    f = SRC / "labels" / f"{stem}.txt"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().strip().splitlines():
        p = line.split()
        if len(p) >= 5:
            out.append([int(p[0])] + [float(v) for v in p[1:5]])
    return out


def haar_subbands(gray: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """DWT Haar satu tingkat, dikembalikan pada resolusi PENUH.

    Sub-band Haar beresolusi setengah; supaya koordinat kotak GT tetap berlaku
    apa adanya, ketiganya diperbesar kembali 2x dengan INTER_NEAREST (tanpa
    interpolasi, supaya tidak menambah penghalusan yang tak disengaja).
    """
    h, w = gray.shape
    g = gray[: h - h % 2, : w - w % 2].astype(np.float32)
    a, b = g[0::2, 0::2], g[0::2, 1::2]
    c, d = g[1::2, 0::2], g[1::2, 1::2]
    lh = (a + b - c - d) / 2.0   # detail horizontal (tepi mendatar)
    hl = (a - b + c - d) / 2.0   # detail vertikal   (tepi tegak)
    hh = (a - b - c + d) / 2.0   # detail diagonal
    out = []
    for band in (lh, hl, hh):
        full = cv2.resize(np.abs(band), (w, h), interpolation=cv2.INTER_NEAREST)
        out.append(full)
    return out[0], out[1], out[2]


def prep_variants(bgr: np.ndarray) -> dict[str, np.ndarray]:
    """Peta skalar 1-kanal yang keterpisahannya diuji.

    `asli`, `gradmag`, `laplacian` disalin PERSIS dari `contrast_boost_test.py`
    (E-011) supaya angka di sini dapat dibandingkan langsung dengan angka di
    sana; yang berbeda hanya wilayah pembandingnya.
    """
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    grad = cv2.GaussianBlur(cv2.magnitude(gx, gy), (0, 0), 2)

    lap = np.abs(cv2.Laplacian(gray, cv2.CV_32F, ksize=3))
    lap = cv2.GaussianBlur(lap, (0, 0), 2)

    lh, hl, hh = haar_subbands(gray)
    # Penghalusan IDENTIK dengan grad/lap di atas -- lihat docstring.
    lh = cv2.GaussianBlur(lh, (0, 0), 2)
    hl = cv2.GaussianBlur(hl, (0, 0), 2)
    hh = cv2.GaussianBlur(hh, (0, 0), 2)
    energi = np.sqrt(lh * lh + hl * hl + hh * hh)

    return {
        "asli": lab[:, :, 0].astype(np.float32),
        "gradmag": grad,
        "laplacian": lap,
        "dwt_lh": lh,
        "dwt_hl": hl,
        "dwt_hh": hh,
        "dwt_energi": energi,
    }


def mask_pelepah(shape, box, kotak_lain, ring_scale: float = 2.0):
    """Kembalikan (mask_isi, mask_pelepah).

    mask_pelepah = cincin sekeliling `box`, dikurangi `box` itu sendiri DAN
    dikurangi seluruh kotak GT tandan lain. Itulah yang membuat uji ini berbeda
    dari E-011: pembandingnya vegetasi, bukan "apa saja di sekitar".
    """
    H, W = shape
    x0, y0, x1, y1 = box
    if x1 - x0 < 4 or y1 - y0 < 4:
        return None, None

    isi = np.zeros((H, W), bool)
    isi[y0:y1, x0:x1] = True

    bw, bh = x1 - x0, y1 - y0
    ex, ey = int(bw * (ring_scale - 1) / 2), int(bh * (ring_scale - 1) / 2)
    X0, Y0 = max(0, x0 - ex), max(0, y0 - ey)
    X1, Y1 = min(W, x1 + ex), min(H, y1 + ey)

    pelepah = np.zeros((H, W), bool)
    pelepah[Y0:Y1, X0:X1] = True
    pelepah &= ~isi
    for ox0, oy0, ox1, oy1 in kotak_lain:
        pelepah[max(0, oy0):min(H, oy1), max(0, ox0):min(W, ox1)] = False

    return isi, pelepah


def auc(a: np.ndarray, b: np.ndarray, rng) -> float | None:
    """AUC Mann-Whitney antara dua populasi piksel. 0,5 = tidak informatif.

    Dilaporkan sebagai max(auc, 1-auc) mengikuti E-011: yang ditanyakan adalah
    KETERPISAHAN, bukan arah mana yang lebih terang.
    """
    if a.size < MIN_PIKSEL or b.size < MIN_PIKSEL:
        return None
    if a.size > 3000:
        a = rng.choice(a, 3000, replace=False)
    if b.size > 3000:
        b = rng.choice(b, 3000, replace=False)
    conc = np.concatenate([a, b])
    ranks = conc.argsort().argsort().astype(np.float64) + 1
    ra = ranks[: len(a)].sum()
    nilai = (ra - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))
    return float(max(nilai, 1 - nilai))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=int, default=250)
    ap.add_argument("--ring-scale", type=float, default=2.0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--keluaran", default=str(
        EVIDENCE_ROOT / "results" / "F-002" / "freq_vs_pelepah.json"))
    args = ap.parse_args()

    stems = [Path(x.strip()).stem for x in SPLIT_TEST.read_text().splitlines() if x.strip()]
    stems = stems[: args.images]
    rng = np.random.default_rng(args.seed)

    real: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    ctrl: dict[str, list] = defaultdict(list)
    n_kotak = 0
    n_tolak = 0

    for stem in stems:
        bgr = cv2.imread(str(SRC / "images" / f"{stem}.jpg"))
        if bgr is None:
            continue
        H, W = bgr.shape[:2]
        maps = prep_variants(bgr)
        boxes = load_boxes(stem)

        piks = [(c, (int((cx - bw / 2) * W), int((cy - bh / 2) * H),
                     int((cx + bw / 2) * W), int((cy + bh / 2) * H)))
                for c, cx, cy, bw, bh in boxes]

        for i, (c, box) in enumerate(piks):
            lain = [b for j, (_, b) in enumerate(piks) if j != i]
            isi, pelepah = mask_pelepah((H, W), box, lain, args.ring_scale)
            if isi is None:
                continue
            n_kotak += 1
            ditolak = False
            for name, m in maps.items():
                nilai = auc(m[isi], m[pelepah], rng)
                if nilai is None:
                    ditolak = True
                    continue
                real[name][CLASSES[c]].append(nilai)
            if ditolak:
                n_tolak += 1

            # Kendali: kotak acak berukuran SAMA di tempat lain pada citra yang
            # sama, diperlakukan identik (termasuk pengurangan kotak GT). Tanpa
            # kendali ini, AUC mentah tidak dapat ditafsirkan -- itu pelajaran
            # E-011 dan disiplin lengan `derau`/`tukar` E-027/E-032.
            pw, ph = box[2] - box[0], box[3] - box[1]
            rx = int(rng.integers(0, max(1, W - pw)))
            ry = int(rng.integers(0, max(1, H - ph)))
            kbox = (rx, ry, rx + pw, ry + ph)
            k_isi, k_pel = mask_pelepah((H, W), kbox, [b for _, b in piks], args.ring_scale)
            if k_isi is None:
                continue
            for name, m in maps.items():
                nilai = auc(m[k_isi], m[k_pel], rng)
                if nilai is not None:
                    ctrl[name].append(nilai)

    def rerata(v):
        return round(float(np.mean(v)), 4) if v else None

    varian = list(prep_variants(np.zeros((8, 8, 3), np.uint8)).keys())
    tabel = {}
    for name in varian:
        kendali = rerata(ctrl[name])
        baris = {k: rerata(real[name][k]) for k in CLASSES}
        baris["kendali"] = kendali
        for k in CLASSES:
            baris[f"{k}_minus_kendali"] = (
                round(baris[k] - kendali, 4) if baris[k] is not None and kendali is not None else None
            )
        tabel[name] = baris

    # Putusan gerbang: ambang +0,02 pada B4, mengikuti E-011.
    AMBANG = 0.02
    lengan_freq = ["gradmag", "laplacian", "dwt_lh", "dwt_hl", "dwt_hh", "dwt_energi"]
    b4 = {n: tabel[n]["B4_minus_kendali"] for n in lengan_freq}
    terbaik = max((v for v in b4.values() if v is not None), default=None)
    lolos = terbaik is not None and terbaik > AMBANG

    lap = {
        "eksperimen": "F-002",
        "pertanyaan": "apakah frekuensi tinggi memisahkan isi tandan dari PELEPAH?",
        "wilayah_pembanding": "cincin sekeliling MINUS seluruh kotak GT tandan lain",
        "split": "SawitMVC-test",
        "n_citra": len(stems),
        "n_kotak_terukur": n_kotak,
        "n_kotak_sebagian_ditolak": n_tolak,
        "min_piksel": MIN_PIKSEL,
        "ring_scale": args.ring_scale,
        "seed": args.seed,
        "auc": tabel,
        "gerbang": {
            "ambang_B4_minus_kendali": AMBANG,
            "B4_minus_kendali_per_lengan": b4,
            "terbaik": terbaik,
            "putusan": "LOLOS" if lolos else "GUGUR",
            "arti": ("K1 boleh dilanjutkan" if lolos else
                     "K1 gugur: cabang frekuensi akan menyala pada pelepah"),
        },
        "pembanding_E011": {
            "catatan": "E-011 memakai cincin TANPA pengurangan kotak lain; angkanya tidak sebanding langsung",
            "laplacian_B4_minus_kendali": 0.0458,
            "sobel_B4_minus_kendali": 0.0367,
        },
    }
    print(json.dumps(lap, indent=2, ensure_ascii=False))
    keluaran = Path(args.keluaran)
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    keluaran.write_text(json.dumps(lap, indent=2, ensure_ascii=False))
    print(f"\n-> {keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
