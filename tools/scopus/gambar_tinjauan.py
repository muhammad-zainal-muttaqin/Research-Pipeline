#!/usr/bin/env python3
"""Membuat semua gambar naskah main6 dari data penyaringan dan matriks bukti.

Semua angka pada gambar dihitung ulang dari berkas di literature/scopus-2026-09,
sehingga gambar selalu sesuai dengan data. Keluaran: PDF (vektor, untuk LaTeX)
dan PNG (pratinjau) di manuscript/figures/main6/.

F11 memotong dua citra dari literature/references/SawitMVC-DiB-2026.pdf
(CC BY 4.0) dengan `pdfimages` (poppler). F12 membaca hasil yang dilaporkan
kajian dari topik/bukti/nilai_terlapor.csv; setiap baris memuat kutipan
sumbernya, dan nilai berkolom nilai_rujukan diubah menjadi persen rujukan.

  python3 tools/scopus/gambar_tinjauan.py            # semua gambar
  python3 tools/scopus/gambar_tinjauan.py F08 F09    # gambar tertentu saja
"""
import csv
import glob
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from tabel_lampiran import ALASAN, KATEGORI

from gaya_gambar import (ABU, ABU_MUDA, AKSEN, AKSEN2, C, FS, FS_JUDUL, FS_KECIL, GARIS, LATAR, LEBAR_SUPP,
                         LEBAR_TEKS, PETA_WARNA, REDUP, SOROT, WARNA_GABUNGAN, WARNA_KAT, WARNA_MEK, campur,
                         kotak, panah)
from gaya_gambar import simpan as simpan_gaya

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MPath

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
TOPIK = KORPUS / "topik"
OUT = ROOT / "manuscript/figures/main6"
OUT.mkdir(parents=True, exist_ok=True)

MEK = ["M0", "M1", "M2", "M3", "M4", "M5"]
# Kode M0-M5 hanya kunci internal berkas data; naskah, tabel, dan gambar memakai nama.
NAMA_MEK = {
    "M0": "No association",
    "M1": "Statistical correction",
    "M2": "Appearance matching",
    "M3": "Temporal tracking",
    "M4": "Geometric or 3D association",
    "M5": "Learned association",
}
NAMA_PENDEK = {"M0": "no association", "M1": "statistical", "M2": "appearance", "M3": "tracking",
               "M4": "geometric", "M5": "learned"}


def nama_gabungan(kode):
    """'M3+M2' -> 'Appearance + tracking'; satu mekanisme -> nama lengkap; urutan tetap M0..M5."""
    bagian = sorted(set(kode.split("+")))
    if len(bagian) == 1:
        return NAMA_MEK.get(bagian[0], kode)
    t = " + ".join(NAMA_PENDEK[b] for b in bagian)
    return t[0].upper() + t[1:]


def muat_tambahan():
    """Rekaman yang diidentifikasi dengan metode lain (bukan pencarian Scopus)."""
    path = TOPIK / "tambahan_metode_lain.csv"
    if not path.exists():
        return []
    return list(csv.DictReader(open(path, encoding="utf-8-sig")))
def simpan(fig, nama, batas=LEBAR_TEKS):
    return simpan_gaya(fig, OUT / nama, batas)


def muat_matriks():
    return list(csv.DictReader(open(TOPIK / "bukti/matriks_bukti.csv")))


def muat_keputusan():
    dec = {}
    for fn in sorted(glob.glob(str(TOPIK / "penyaringan/abstrak_*.txt"))):
        for line in open(fn):
            m = re.match(r"^(\d+)\s+(C[1-5]|T|R|M|X)(?:\s+(E\d))?", line)
            if m:
                dec[int(m.group(1))] = (m.group(2), m.group(3) or "")
    return dec


def muat_c3():
    out = {}
    for line in open(TOPIK / "bukti/kode_C3.txt"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        out[int(p[0])] = {"tugas": p[1], "lokasi": p[2], "modalitas": p[3],
                          "multipandang": p[4], "per_kelas": p[5]}
    return out


# ---------------------------------------------------------------- F1 PRISMA


def gambar_prisma():
    """Diagram alur PRISMA 2020: identifikasi, penyaringan judul dan abstrak,
    pencarian teks lengkap, penilaian teks lengkap, dan kajian yang masuk."""
    from kode_bukti import muat_teks_lengkap
    counts = list(csv.DictReader(open(TOPIK / "counts.csv")))
    diambil = sum(int(r["retrieved"]) for r in counts)
    unik = sum(1 for _ in csv.DictReader(open(TOPIK / "records_all.csv")))
    tj = list(csv.DictReader(open(TOPIK / "penyaringan/tahap_judul.csv")))
    x0 = sum(1 for r in tj if r["keputusan_judul"] == "X0")
    xj = sum(1 for r in tj if r["keputusan_judul"] == "X")
    dec = muat_keputusan()
    kand = len(dec)
    xa = Counter(d[1] for d in dec.values() if d[0] == "X")
    judul_saja = 0
    for fn in glob.glob(str(TOPIK / "penyaringan/abstrak_*.txt")):
        for line in open(fn):
            if re.match(r"^\d+\s", line) and ("T00" in fn or "(judul)" in line):
                judul_saja += 1
    tl = muat_teks_lengkap(TOPIK)
    dicari = len(tl)
    tak = sum(1 for s, _, _ in tl.values() if s == "tidak diperoleh")
    dinilai = [v for v in tl.values() if v[0] == "dinilai"]
    menunggu = sum(1 for s, _, _ in tl.values() if s == "menunggu")
    xt = Counter(e for _, k, e in dinilai if k == "X")
    inc = Counter(k for _, k, _ in dinilai if k != "X")
    lain = muat_tambahan()
    lain_ada = [r for r in lain if (KORPUS / "pdf" / (r["key"] + ".pdf")).exists()]

    kanan = 128 if lain else 100
    fig, ax = plt.subplots(figsize=(6.66, 7.4))
    ax.set_xlim(0, kanan)
    ax.set_ylim(0, 132)
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)

    def kotak_teks(x, y, w, h, teks, warna="white", fs=FS):
        kotak(ax, x, y, w, h, warna)
        ax.text(x + w / 2, y + h / 2, teks, ha="center", va="center", fontsize=fs, linespacing=1.25)

    def panah_(x1, y1, x2, y2):
        panah(ax, x1, y1, x2, y2)

    abu = LATAR
    for y, lab in [(120, "Identification"), (86, "Screening"), (40, "Eligibility"), (7, "Included")]:
        ax.text(1, y, lab, rotation=90, ha="left", va="center", fontsize=FS, fontweight="bold")
    kotak_teks(8, 115, 44, 11, f"Records identified from Scopus\nn = {diambil:,}")
    kotak_teks(60, 115, 36, 11, f"Duplicate records removed\nn = {diambil - unik:,}", abu)
    panah_(52, 120.5, 60, 120.5)
    kotak_teks(8, 99, 44, 10, f"Unique records\nn = {unik:,}")
    panah_(30, 115, 30, 109)
    kotak_teks(60, 97, 36, 14, f"Records removed by document type\n(proceedings front matter, errata,\nnotes, editorials, letters,\nretractions), n = {x0}", abu)
    panah_(52, 104, 60, 104)
    kotak_teks(8, 84, 44, 9, f"Records screened on title\nn = {unik - x0:,}")
    panah_(30, 99, 30, 93)
    ulang = list(csv.DictReader(open(ROOT / "literature/scopus-2026-09/verifikasi/.teknis/ulang_eksklusi_judul.csv")))
    kembali = sum(1 for r in ulang if r["kode"] != "X" and r["bertahan_setelah_disanggah"] == "ya")
    kotak_teks(60, 82.5, 36, 12, f"Records excluded, n = {xj:,}\n{len(ulang):,} exclusions re-read on abstract;\n"
          f"{kembali} returned to the next stage", abu)
    panah_(52, 88.5, 60, 88.5)
    kotak_teks(8, 66, 44, 12, f"Records assessed on title and abstract\nn = {kand:,}\n"
          f"{kand - judul_saja} with abstract; {judul_saja} with title and source only")
    panah_(30, 84, 30, 78)
    kotak_teks(56, 62, 42, 19, f"Records excluded, n = {sum(xa.values())}\n" + "\n".join(
        f"{nama}: {xa[e]}" for e, nama in ALASAN if xa[e]), abu, fs=FS_KECIL)
    panah_(52, 72, 56, 72)
    kotak_teks(8, 49, 44, 10, f"Reports sought for retrieval\nn = {dicari:,}")
    panah_(30, 66, 30, 59)
    if menunggu:
        kotak_teks(60, 47, 36, 14, f"Reports not retrieved\nn = {tak:,}\nRetrieved, awaiting full-text\nassessment, n = {menunggu:,}", abu)
    else:
        kotak_teks(60, 49, 36, 10, f"Reports not retrieved\nn = {tak:,}", abu)
    panah_(52, 54, 60, 54)
    kotak_teks(8, 30, 44, 10, f"Reports assessed for eligibility\nn = {len(dinilai)}")
    panah_(30, 49, 30, 40)
    kotak_teks(56, 26, 42, 18, f"Reports excluded, n = {sum(xt.values())}\n" + "\n".join(
        f"{nama}: {xt[e]}" for e, nama in ALASAN if xt[e]), abu, fs=FS_KECIL)
    panah_(52, 35, 56, 35)
    nama = {"C1": "multi-observation", "C2": "single-view counting", "C3": "oil palm",
            "C4": "single-image class-wise counting", "C5": "depth and 3D sensing",
            "R": "earlier reviews", "T": "methods outside agriculture"}
    semua = inc + Counter(r["kode"] for r in lain_ada if r["kode"] != "X")
    b1 = ", ".join(f"{nama[k]} {semua[k]}" for k in ["C1", "C2", "C3", "C4"])
    b2 = ", ".join(f"{nama[k]} {semua[k]}" for k in ["C5", "R", "T"])
    lebar = 118 if lain else 90
    kotak_teks(8, 1, lebar, 13, f"Studies included, n = {sum(semua.values())}\n{b1},\n{b2}", SOROT)
    panah_(30, 30, 30, 14)
    if lain:
        ax.text(30, 130, "Identification of studies via Scopus", ha="center", fontsize=FS, style="italic")
        ax.text(114.5, 130, "Identification of studies via other methods", ha="center", fontsize=FS, style="italic")
        kotak_teks(103, 115, 23, 11, f"Records identified from\nreference lists and\nknown papers\nn = {len(lain)}")
        kotak_teks(103, 49, 23, 10, f"Reports sought\nfor retrieval\nn = {len(lain)}")
        panah_(114.5, 115, 114.5, 59)
        tak_lain = len(lain) - len(lain_ada)
        kotak_teks(103, 30, 23, 10, f"Reports assessed\nfor eligibility\nn = {len(lain_ada)}"
              + (f"\nnot retrieved, n = {tak_lain}" if tak_lain else ""))
        panah_(114.5, 49, 114.5, 40)
        if lain_ada:
            panah_(114.5, 30, 114.5, 14)
    simpan(fig, "F01_prisma")
    return {"diambil": diambil, "unik": unik, "x0": x0, "xj": xj, "kand": kand, "judul_saja": judul_saja,
            "xa": xa, "dicari": dicari, "tidak_diperoleh": tak, "dinilai": len(dinilai), "menunggu": menunggu, "xt": xt, "inc": inc,
            "metode_lain": len(lain), "metode_lain_diperoleh": len(lain_ada)}


# ---------------------------------------------------- F2 corpus per tahun
def gambar_tahun(mat):
    hitung = defaultdict(Counter)
    for r in mat:
        hitung[r["kode"]][int(r["year"])] += 1
    tahun = list(range(2012, max(int(r["year"]) for r in mat) + 1))
    assert sum(hitung[k][t] for k in hitung for t in tahun) == len(mat), "F02: ada kajian di luar sumbu tahun"
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    dasar = [0] * len(tahun)
    for k in ["C1", "C2", "C3", "C4", "C5", "R", "T"]:
        v = [hitung[k][t] for t in tahun]
        ax.bar(tahun, v, bottom=dasar, color=WARNA_KAT[k], width=0.78,
               label=KATEGORI[k], linewidth=0)
        dasar = [a + b for a, b in zip(dasar, v)]
    for t, d in zip(tahun, dasar):
        ax.text(t, d + 2, str(d), ha="center", va="bottom", fontsize=FS_KECIL)
    ax.set_xticks(tahun)
    ax.set_xticklabels([str(t) for t in tahun])
    ax.set_ylabel("Included studies")
    ax.set_ylim(0, max(dasar) * 1.12)
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.13), handlelength=1.2, columnspacing=1.0)
    simpan(fig, "F02_tahun", LEBAR_SUPP)


# ------------------------------------------- F3 kerangka ruang rancangan
def gambar_kerangka():
    fig, ax = plt.subplots(figsize=(6.7, 2.8))
    fig.subplots_adjust(0, 0, 1, 1)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 44.5)
    ax.axis("off")

    def tahap(x, y, w, h, judul, isi, warna):
        kotak(ax, x, y, w, h, warna, sudut=1)
        ax.text(x + w / 2, y + h - 2.2, judul, ha="center", va="top", fontsize=FS, fontweight="bold")
        ax.text(x + w / 2, y + h - 5.4, isi, ha="center", va="top", fontsize=FS_KECIL, linespacing=1.3)

    tahap(1, 26, 16, 16, "1  Acquisition", "Views per plant;\nvideo or discrete\nviews; pose,\ndepth, baseline", "white")
    tahap(20, 26, 16, 16, "2  Observation", "Detections or\nmasks per image;\none fruit may\nyield several", "white")
    tahap(39, 26, 19, 16, "3  Association", "Decide which\nobservations show\nthe same fruit", SOROT)
    tahap(61, 26, 20, 16, "4  Attribute assignment", "Class, size, or\nmass assigned\nonce per fruit,\nnot per box", "white")
    tahap(84, 26, 15, 16, "5  Inventory", "One record per\nfruit, totalled by\nclass, tree, row,\nor block", "white")
    for x1, x2 in [(17, 20), (36, 39), (58, 61), (81, 84)]:
        panah(ax, x1, 34, x2, 34)

    y0 = 1
    lebar = 15.6
    asumsi = {
        "M0": "No fruit appears\nin two images",
        "M1": "A stable ratio\nbetween observed\nand true counts",
        "M2": "Fruit differ enough\nin appearance to be\ntold apart",
        "M3": "Ordered, overlapping\nframes; smooth camera\nmotion; static fruit",
        "M4": "Accurate pose,\nscale, and depth;\nstatic scene",
        "M5": "Identity-labelled\ntraining data that\nmatch the conditions\nof use",
    }
    judul2 = {"M0": "No\nassociation", "M1": "Statistical\ncorrection",
              "M2": "Appearance\nmatching", "M3": "Temporal\ntracking",
              "M4": "Geometric or 3D\nassociation", "M5": "Learned\nassociation"}
    for i, m in enumerate(MEK):
        x = 1 + i * (lebar + 1.0)
        kotak(ax, x, y0, lebar, 18, campur(WARNA_MEK[m], 0.3))
        ax.text(x + lebar / 2, y0 + 16.6, judul2[m], ha="center", va="top", fontsize=FS,
                fontweight="bold", linespacing=1.15)
        ax.text(x + lebar / 2, y0 + 11.0, "Assumes:", ha="center", va="top", fontsize=FS_KECIL, style="italic")
        ax.text(x + lebar / 2, y0 + 8.6, asumsi[m], ha="center", va="top", fontsize=FS_KECIL, linespacing=1.25)
    panah(ax, 48.5, 26, 48.5, 19.6)
    simpan(fig, "F03_kerangka")


# ------------------------------------------- F4 mekanisme C1 per tahun
def gambar_mekanisme(mat):
    c1 = [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]
    periode = [(2012, 2017), (2018, 2020), (2021, 2022), (2023, 2024), (2025, 2026)]
    lab = ["2012–17", "2018–20", "2021–22", "2023–24", "2025–26"]
    per = {p: Counter() for p in periode}
    n_per = Counter()
    for r in c1:
        y = int(r["year"])
        for p in periode:
            if p[0] <= y <= p[1]:
                n_per[p] += 1
                for m in set(r["mekanisme"].split("+")):
                    per[p][m] += 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.25, 2.7), gridspec_kw={"width_ratios": [1.45, 1]})
    lebar = 0.13
    for j, m in enumerate(MEK):
        v = [100 * per[p][m] / n_per[p] if n_per[p] else 0 for p in periode]
        xs = [i + (j - 2.5) * lebar for i in range(len(periode))]
        ax1.bar(xs, v, width=lebar, color=WARNA_MEK[m], edgecolor=REDUP, linewidth=0.3,
                label=NAMA_MEK[m])
    ax1.set_xticks(range(len(periode)))
    ax1.set_xticklabels([f"{l}\n(n = {n_per[p]})" for l, p in zip(lab, periode)])
    ax1.set_ylabel("Studies using the mechanism (%)")
    ax1.set_ylim(0, 100)
    ax1.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.2), handlelength=1.2, columnspacing=1.0)
    ax1.set_title("(a) Mechanism by period")

    akuisisi = Counter(r["akuisisi_manual"] for r in c1)
    nama_ak = {"V": "Video along a path", "D": "Discrete views", "S": "3D scan",
               "T": "Revisits over time", "1": "Single view"}
    urut = [k for k in ["V", "D", "S", "T", "1"] if akuisisi[k]]
    ax2.barh([nama_ak[k] for k in urut][::-1], [akuisisi[k] for k in urut][::-1],
             color=AKSEN, height=0.6)
    for i, k in enumerate(urut[::-1]):
        ax2.text(akuisisi[k] + 2, i, str(akuisisi[k]), va="center")
    ax2.set_xlabel("Studies")
    ax2.set_xlim(0, max(akuisisi.values()) * 1.18)
    ax2.set_title("(b) Acquisition design")
    fig.tight_layout(w_pad=2)
    simpan(fig, "F04_mekanisme", LEBAR_SUPP)
    return per, n_per, akuisisi


# ------------------------------------------- F5 peta tanaman x mekanisme
def gambar_peta_tanaman(mat):
    c1 = [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]
    tan = Counter()
    for r in c1:
        for t in (r["tanaman"] or "crop not named").split(";")[:1]:
            tan[t] += 1
    utama = [t for t, _ in tan.most_common(9)]
    sel = defaultdict(Counter)
    for r in c1:
        t = (r["tanaman"] or "crop not named").split(";")[0]
        t = t if t in utama else "other crops"
        for m in set(r["mekanisme"].split("+")):
            sel[t][m] += 1
    baris = utama + (["other crops"] if any("other crops" == k for k in sel) else [])
    fig, ax = plt.subplots(figsize=(4.9, 3.4))
    maks = max(v for d in sel.values() for v in d.values())
    for i, t in enumerate(baris):
        for j, m in enumerate(MEK):
            v = sel[t][m]
            if v:
                ax.scatter(j, i, s=18 + 380 * v / maks, color=WARNA_MEK[m], edgecolor=GARIS,
                           linewidth=0.4, alpha=0.9, zorder=3)
                ax.text(j, i, str(v), ha="center", va="center", fontsize=FS_KECIL, zorder=4)
    ax.set_xticks(range(len(MEK)))
    ax.set_xticklabels([NAMA_MEK[m].replace(" ", "\n", 1).replace("or 3D\n", "or 3D ").replace("Geometric\nor 3D association", "Geometric or 3D\nassociation")
                        for m in MEK], fontsize=FS_KECIL)
    ax.set_yticks(range(len(baris)))
    lab = []
    for t in baris:
        n = sum(1 for r in c1 if ((r["tanaman"] or "crop not named").split(";")[0] if (r["tanaman"] or "crop not named").split(";")[0] in utama else "other crops") == t)
        lab.append(f"{t} ({n})")
    ax.set_yticklabels(lab)
    ax.invert_yaxis()
    ax.set_xlim(-0.6, len(MEK) - 0.4)
    ax.grid(color=LATAR, linewidth=0.5, zorder=0)
    ax.set_xlabel("Association mechanism")
    simpan(fig, "F05_tanaman_mekanisme", LEBAR_SUPP)


def peta_panas(ax, data, maks):
    """Peta panas vektor (pcolormesh) dengan angka sel; sel nol dibiarkan kosong. Sel berpusat di bilangan bulat."""
    import numpy as np
    arr = np.array(data, dtype=float)
    ax.pcolormesh(np.arange(arr.shape[1] + 1) - 0.5, np.arange(arr.shape[0] + 1) - 0.5,
                  np.ma.masked_equal(arr, 0), cmap=PETA_WARNA, vmin=0, vmax=maks,
                  edgecolors="white", linewidth=0.6)
    for i, baris in enumerate(data):
        for j, v in enumerate(baris):
            if v:
                ax.text(j, i, str(v), ha="center", va="center", fontsize=FS_KECIL,
                        color="white" if v / maks > 0.55 else "black")
    ax.set_xlim(-0.5, arr.shape[1] - 0.5)
    ax.set_ylim(arr.shape[0] - 0.5, -0.5)
    ax.tick_params(length=0)


# ------------------------------------------- F6 korpus kelapa sawit
def gambar_sawit(mat):
    masuk = {int(r["idx"]) for r in mat if r["kode"] == "C3"}
    c3 = {i: v for i, v in muat_c3().items() if i in masuk}
    tahun = {int(r["idx"]): int(r["year"]) for r in mat if r["idx"].isdigit()}
    tugas = ["KLS", "DET", "HIT", "LF", "MUTU", "SENSOR", "DATA"]
    nama_t = {"KLS": "Ripeness classification\nof bunch images", "DET": "Bunch detection\nin a scene",
              "HIT": "Bunch counting", "LF": "Loose fruit\ndetection", "MUTU": "Quality, defect,\nmass, or pose",
              "SENSOR": "Non-RGB sensing", "DATA": "Dataset papers"}
    lokasi = ["POHON", "TANAH", "CAMPUR", "KEBUN", "PABRIK", "UAV", "WEB", "?"]
    nama_l = {"POHON": "On the palm", "TANAH": "Ground or\ncollection\npoint", "CAMPUR": "Palm and\nground",
              "KEBUN": "Plantation,\nposition\nnot stated", "PABRIK": "Mill,\nconveyor, or\nlaboratory",
              "UAV": "UAV", "WEB": "Web or\npublic set", "?": "Not\nreported"}
    m = defaultdict(Counter)
    for v in c3.values():
        if v["tugas"] in tugas:
            m[v["tugas"]][v["lokasi"]] += 1
    lokasi = [l for l in lokasi if any(m[t][l] for t in tugas)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.25, 3.0), gridspec_kw={"width_ratios": [1.5, 1]})
    maks = max(c for d in m.values() for c in d.values())
    peta_panas(ax1, [[m[t][l] for l in lokasi] for t in tugas], maks)
    ax1.set_xticks(range(len(lokasi)))
    ax1.set_xticklabels([nama_l[l].replace("\n", " ") for l in lokasi], fontsize=FS_KECIL, rotation=35,
                        ha="right", rotation_mode="anchor")
    ax1.set_yticks(range(len(tugas)))
    ax1.set_yticklabels([f"{nama_t[t]} ({sum(m[t].values())})" for t in tugas], fontsize=FS_KECIL)
    ax1.set_title("(a) Task and setting")

    th = list(range(2012, 2027))
    semua = Counter(tahun[i] for i in c3)
    mv = Counter(tahun[i] for i, v in c3.items() if v["multipandang"] == "Y")
    hit = Counter(tahun[i] for i, v in c3.items() if v["tugas"] == "HIT")
    ax2.bar(th, [semua[t] for t in th], color=ABU_MUDA, width=0.8, label="All oil-palm studies")
    ax2.bar(th, [hit[t] for t in th], color=AKSEN, width=0.8, label="Counting studies")
    thv = [t for t in th if mv[t]]
    ax2.plot(thv, [mv[t] for t in thv], "o", color=AKSEN2, markersize=3.4, mec=GARIS, mew=0.4,
             label="Several views of one bunch or palm")
    ax2.set_xticks([2012, 2015, 2018, 2021, 2024, 2026])
    ax2.set_ylabel("Studies")
    ax2.legend(loc="upper left")
    ax2.set_title("(b) Studies per year")
    fig.tight_layout(w_pad=1.5)
    simpan(fig, "F06_sawit", LEBAR_SUPP)
    return c3


# ------------------------------------------- F7 metrik yang dilaporkan
NAMA_METRIK = {"hitung": "Count agreement (MAE, RMSE, $R^2$, MAPE, count accuracy)",
               "identitas": "Tracking or identity (MOTA, IDF1, HOTA, ID switches)",
               "deteksi": "Detection quality (mAP, AP, F1)",
               "tidak ada": "No quantitative metric"}
NAMA_RUJUKAN = {"anotasi": "Annotated images or video", "pohon": "Hand count on the plant",
                "panen": "Harvest count", "packhouse": "Packhouse count",
                "tidak ada": "No count reference stated"}


def batang_persen(ax, nama, hit, n, warna):
    urut = list(nama)
    vals = [100 * hit[k] / n for k in urut]
    y = range(len(urut))[::-1]
    ax.barh(y, vals, color=warna, height=0.6)
    for yy, k, v in zip(y, urut, vals):
        ax.text(v + 1.5, yy, f"{hit[k]} ({v:.0f}%)", va="center")
    ax.set_yticks(list(y))
    ax.set_yticklabels([nama[k].replace(" (", "\n(") for k in urut])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of studies (%)")


def kajian_metode(mat):
    return [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]


def gambar_metrik(mat):
    c1 = kajian_metode(mat)
    berkode = [r for r in c1 if r["tingkat_metrik"].strip()]
    hit = Counter(x for r in berkode for x in set(r["tingkat_metrik"].split(";")) if x)
    kelas = sum(1 for r in c1 if r["per_kelas"] == "Y")
    fig, ax = plt.subplots(figsize=(3.6, 2.1))
    batang_persen(ax, NAMA_METRIK, hit, len(berkode), [AKSEN, AKSEN, AKSEN, ABU])
    ax.set_xlim(0, 118)
    ax.set_xticks(range(0, 101, 20))
    ax.tick_params(axis="y", length=0)
    simpan(fig, "F07_metrik")
    return hit, len(berkode), kelas


def gambar_metrik_rujukan(mat):
    """F07 ditambah panel rujukan hitung; dihitung seperti nRef* di angka_naskah.py."""
    c1 = kajian_metode(mat)
    berkode = [r for r in c1 if r["tingkat_metrik"].strip()]
    hit = Counter(x for r in berkode for x in set(r["tingkat_metrik"].split(";")) if x)
    rh = Counter(x for r in c1 for x in r["referensi_hitung"].split(";") if x)
    fig, (a, b) = plt.subplots(1, 2, figsize=(5.8, 2.1), gridspec_kw={"wspace": 1.0})
    batang_persen(a, NAMA_METRIK, hit, len(berkode), [AKSEN, AKSEN, AKSEN, ABU])
    batang_persen(b, NAMA_RUJUKAN, rh, len(c1), [AKSEN, AKSEN, AKSEN, AKSEN, ABU])
    a.set_title("(a) Metric type")
    b.set_title("(b) Count reference")
    for ax in (a, b):
        ax.set_xlim(0, 118)
        ax.set_xticks(range(0, 101, 20))
        ax.tick_params(axis="y", length=0)
    simpan(fig, "F13_metrik_rujukan")
    return {k: hit[k] for k in NAMA_METRIK}, {k: rh[k] for k in NAMA_RUJUKAN}, len(berkode), len(c1)


# ------------------------------------------- F8 jaringan istilah
# Kosakata tetap: (label, pola regex pada judul + abstrak, huruf kecil).
ISTILAH = [
    ("detection", r"\bdetect"), ("segmentation", r"\bsegment"), ("counting", r"\bcount"),
    ("yield estimation", r"yield (estimat|predict|forecast)"), ("tracking", r"\btrack"),
    ("video", r"\bvideo"), ("multi-view", r"multi-?view|multiple views"),
    ("re-identification", r"re-?identif"), ("data association", r"data association|\bassociation\b"),
    ("double counting", r"double.count|duplicat|repeated count"),
    ("structure from motion", r"structure.from.motion|\bsfm\b"),
    ("3D reconstruction", r"3d reconstruct|three-dimensional reconstruct|\bnerf\b|gaussian splatting"),
    ("point cloud", r"point cloud"), ("LiDAR", r"\blidar\b"), ("RGB-D", r"rgb-?d\b|depth camera"),
    ("stereo vision", r"\bstereo|binocular"), ("depth", r"\bdepth\b"),
    ("occlusion", r"occlu"), ("UAV", r"\buav\b|\bdrone|unmanned aerial"),
    ("robot", r"\brobot"), ("smartphone", r"smartphone|mobile phone|handheld"),
    ("YOLO", r"\byolo"), ("Mask R-CNN", r"mask r-?cnn"), ("Faster R-CNN", r"faster r-?cnn"),
    ("transformer", r"transformer|\bdetr\b"), ("deep learning", r"deep learning|convolutional neural"),
    ("SORT-family tracker", r"deepsort|deep sort|bytetrack|bot-sort|\bsort\b|oc-sort"),
    ("Kalman filter", r"kalman"), ("ripeness / maturity", r"ripe|maturity|ripening"),
    ("classification", r"classif"), ("grading", r"\bgrad(e|ing)\b"),
    ("fruit size", r"fruit size|size estimat|diameter"), ("localization", r"locali[sz]"),
    ("orchard", r"orchard"), ("greenhouse", r"greenhouse"),
    ("apple", r"\bapple"), ("citrus", r"citrus|\borange"), ("grape", r"grape|vineyard"),
    ("tomato", r"tomato"), ("mango", r"mango"), ("strawberry", r"strawberr"),
    ("oil palm", r"oil palm|fresh fruit bunch|elaeis"), ("hyperspectral", r"hyperspectral|multispectral"),
    ("review", r"\breview|\bsurvey"),
]


def gambar_istilah(mat):
    import networkx as nx
    from networkx.algorithms.community import greedy_modularity_communities

    abstrak = {}
    for line in open(TOPIK / "enrich.jsonl", encoding="utf-8"):
        d = json.loads(line)
        abstrak[d["eid"]] = d.get("abstract") or ""
    frek = Counter()
    pasangan = Counter()
    for r in mat:
        teks = (r["title"] + " " + abstrak.get(r["eid"], "")).lower()
        ada = sorted(lab for lab, pola in ISTILAH if re.search(pola, teks))
        frek.update(ada)
        pasangan.update(combinations(ada, 2))
    MIN_NODE, MIN_EDGE = 20, 12
    G = nx.Graph()
    for lab, _ in ISTILAH:
        if frek[lab] >= MIN_NODE:
            G.add_node(lab, n=frek[lab])
    for (a, b), w in sorted(pasangan.items()):
        if w >= MIN_EDGE and a in G and b in G:
            # kekuatan asosiasi (van Eck dan Waltman): c_ij / (c_i * c_j)
            G.add_edge(a, b, w=w, s=w / (frek[a] * frek[b]))
    kom = [sorted(c) for c in greedy_modularity_communities(G, weight="s")]
    kom.sort(key=lambda c: (-len(c), c[0]))
    warna_kom = [C["biru"], C["merah"], C["hijau"], C["oranye"], C["ungu"], C["biru_muda"], ABU]
    warna = {n: warna_kom[min(i, len(warna_kom) - 1)] for i, c in enumerate(kom) for n in c}
    # Tata letak Kamada-Kawai (deterministik): jarak sasaran mengecil bila asosiasi kuat.
    smaks = max(d["s"] for _, _, d in G.edges(data=True))
    jarak = {a: {b: 3.4 for b in G} for a in G}
    for a, b, d in G.edges(data=True):
        jarak[a][b] = jarak[b][a] = 1.0 + 2.0 * (1 - (d["s"] / smaks) ** 0.5)
    for a in G:
        jarak[a][a] = 0.0
    pos = nx.kamada_kawai_layout(G, dist=jarak)
    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    wmaks = max(d["w"] for _, _, d in G.edges(data=True))
    for a, b, d in sorted(G.edges(data=True), key=lambda e: e[2]["w"]):
        sama = warna[a] == warna[b]
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=warna[a] if sama else ABU_MUDA,
                linewidth=0.25 + 2.6 * d["w"] / wmaks, alpha=0.30 if sama else 0.22, zorder=1,
                solid_capstyle="round")
    nmaks = max(frek[n] for n in G)
    ukuran = {n: 20 + 420 * frek[n] / nmaks for n in G}
    for n in G:
        ax.scatter(*pos[n], s=ukuran[n], color=warna[n], edgecolor="white",
                   linewidth=0.6, alpha=0.92, zorder=3)
    ax.axis("off")
    ax.margins(0.08)
    # Label ditaruh di sisi simpul yang tidak menimpa simpul atau label lain.
    fig.canvas.draw()
    rnd = fig.canvas.get_renderer()
    px = fig.dpi / 72
    terisi = []
    for n in G:
        cx, cy = ax.transData.transform(pos[n])
        r = (ukuran[n] ** 0.5) / 2 * px
        terisi.append((cx - r, cy - r, cx + r, cy + r))

    def tumpang(b):
        return sum(1 for t in terisi if b[0] < t[2] and t[0] < b[2] and b[1] < t[3] and t[1] < b[3])

    for n in sorted(G, key=lambda n: -frek[n]):
        j = (ukuran[n] ** 0.5) / 2 + 1.5
        terbaik = None
        for dx, dy, ha, va in [(0, -j, "center", "top"), (0, j, "center", "bottom"),
                               (j, 0, "left", "center"), (-j, 0, "right", "center")]:
            t = ax.annotate(n, pos[n], xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                            zorder=4, fontsize=FS_KECIL + (FS_JUDUL + 0.5 - FS_KECIL) * (frek[n] / nmaks) ** 0.5)
            e = t.get_window_extent(rnd)
            b = (e.x0, e.y0, e.x1, e.y1)
            k = tumpang(b)
            if terbaik is None or k < terbaik[0]:
                if terbaik:
                    terbaik[1].remove()
                terbaik = (k, t, b)
            else:
                t.remove()
            if k == 0:
                break
        terisi.append(terbaik[2])
    simpan(fig, "F08_istilah", LEBAR_SUPP)
    return {"node": G.number_of_nodes(), "sisi": G.number_of_edges(), "klaster": kom,
            "frekuensi": frek.most_common(), "n_studi": len(mat),
            "dengan_abstrak": sum(1 for r in mat if abstrak.get(r["eid"]))}


# ------------------------------------------- F9 alur akuisisi-mekanisme-platform-tanaman
def kat_mekanisme(r):
    m = "+".join(sorted(set(r["mekanisme"].split("+"))))
    return m if m in ("M0", "M1", "M2", "M3", "M4", "M5", "M2+M3", "M3+M4") else "Other combinations"


def kat_platform(r):
    p = [x for x in r["platform"].split(";") if x]
    if not p:
        return "Not stated"
    if len(p) > 1:
        return "Several platforms"
    return {"ground vehicle/robot": "Ground vehicle or robot", "UAV": "UAV",
            "handheld/smartphone": "Handheld or smartphone", "conveyor/lab": "Laboratory or conveyor",
            "fixed camera": "Fixed camera"}[p[0]]


def kat_tanaman(r, utama):
    t = r["tanaman"].split(";")[0] if r["tanaman"] else "crop not named"
    return t if t in utama or t == "crop not named" else "other crops"


def gambar_alur(mat):
    c1 = [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]
    tan = Counter(r["tanaman"].split(";")[0] for r in c1 if r["tanaman"])
    utama = [t for t, _ in tan.most_common(7)]
    nama_ak = {"V": "Video along a path", "D": "Discrete views", "S": "3D scan",
               "T": "Revisits over time", "1": "Single view"}
    urut = [
        [nama_ak[k] for k in ["V", "D", "S", "T", "1"]],
        ["M0", "M1", "M2", "M2+M3", "M3", "M3+M4", "M4", "M5", "Other combinations"],
        ["Ground vehicle or robot", "UAV", "Handheld or smartphone", "Laboratory or conveyor",
         "Fixed camera", "Several platforms", "Not stated"],
        utama + ["other crops", "crop not named"],
    ]
    judul = ["Acquisition", "Association mechanism", "Platform", "Crop"]
    warna_m = {**WARNA_MEK, **WARNA_GABUNGAN}
    jalur = [(nama_ak[r["akuisisi_manual"]], kat_mekanisme(r), kat_platform(r), kat_tanaman(r, utama))
             for r in c1]
    n = len(jalur)
    urut = [[k for k in kol if any(j[i] == k for j in jalur)] for i, kol in enumerate(urut)]
    fig, ax = plt.subplots(figsize=(6.25, 4.6))
    xs = [0, 1, 2, 3]
    lebar = 0.035
    celah = 0.05
    posisi = []
    for i, kol in enumerate(urut):
        tot = Counter(j[i] for j in jalur)
        skala = (1 - celah * (len(kol) - 1)) / n
        y = 1.0
        d = {}
        for k in kol:
            h = tot[k] * skala
            d[k] = (y - h, y, skala)
            ax.add_patch(plt.Rectangle((xs[i] - lebar, y - h), 2 * lebar, h, color=GARIS, linewidth=0))
            lab = nama_gabungan(k) if i == 1 and k != "Other combinations" else k
            if 0 < i < 3:
                ax.text(xs[i], y + 0.003, f"{lab} ({tot[k]})", ha="center", va="bottom", fontsize=FS_KECIL - 0.5, zorder=5,
                        bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor="none", alpha=0.75))
            else:
                ha, dx = ("right", -lebar - 0.02) if i == 0 else ("left", lebar + 0.02)
                ax.text(xs[i] + dx, y - h / 2, f"{k} ({tot[k]})", ha=ha, va="center", fontsize=FS_KECIL)
            y -= h + celah
        posisi.append(d)
        ax.text(xs[i], 1.075, judul[i], ha="center", va="bottom", fontsize=FS, fontweight="bold")
    for i in range(3):
        alir = Counter((j[i], j[i + 1], j[1]) for j in jalur)
        kiri = {k: posisi[i][k][1] for k in urut[i]}
        kanan = {k: posisi[i + 1][k][1] for k in urut[i + 1]}
        y_kiri = {}
        for f in sorted(alir, key=lambda f: (urut[i].index(f[0]), urut[i + 1].index(f[1]), urut[1].index(f[2]))):
            h = alir[f] * posisi[i][f[0]][2]
            y_kiri[f] = (kiri[f[0]] - h, kiri[f[0]])
            kiri[f[0]] -= h
        for f in sorted(alir, key=lambda f: (urut[i + 1].index(f[1]), urut[i].index(f[0]), urut[1].index(f[2]))):
            h = alir[f] * posisi[i + 1][f[1]][2]
            b0, b1 = kanan[f[1]] - h, kanan[f[1]]
            kanan[f[1]] -= h
            a0, a1 = y_kiri[f]
            x0, x1 = xs[i] + lebar, xs[i + 1] - lebar
            xm = (x0 + x1) / 2
            verts = [(x0, a1), (xm, a1), (xm, b1), (x1, b1), (x1, b0), (xm, b0), (xm, a0), (x0, a0), (x0, a1)]
            codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.LINETO,
                     MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.CLOSEPOLY]
            ax.add_patch(PathPatch(MPath(verts, codes), facecolor=warna_m[f[2]], edgecolor="none", alpha=0.55))
    pegangan = [plt.Rectangle((0, 0), 1, 1, color=warna_m[m], alpha=0.7) for m in urut[1]]
    ax.legend(pegangan, [nama_gabungan(k) if k != "Other combinations" else k for k in urut[1]],
              ncol=4, fontsize=FS_KECIL, loc="upper center",
              bbox_to_anchor=(0.5, 0.0), handlelength=1.2, columnspacing=1.0, handletextpad=0.4)
    ax.set_xlim(-0.55, 3.45)
    ax.set_ylim(-0.02, 1.13)
    ax.axis("off")
    simpan(fig, "F09_alur", LEBAR_SUPP)
    return {i: Counter(j[i] for j in jalur) for i in range(4)}


# ------------------------------------------- F10 sensor dan platform per tanaman
def gambar_sensor(mat):
    c1 = [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]
    tan = Counter(r["tanaman"].split(";")[0] for r in c1 if r["tanaman"])
    utama = [t for t, _ in tan.most_common(9)]
    baris = utama + ["other crops", "crop not named"]
    kol_mod = ["RGB", "RGB-D", "stereo", "LiDAR", "multispectral", "monocular depth"]
    kol_plat = ["ground vehicle/robot", "UAV", "handheld/smartphone", "conveyor/lab", "fixed camera", ""]
    nama = {"RGB": "RGB camera", "RGB-D": "RGB-D camera", "stereo": "Stereo camera", "LiDAR": "LiDAR",
            "multispectral": "Multispectral", "monocular depth": "Estimated depth",
            "ground vehicle/robot": "Ground vehicle\nor robot", "UAV": "UAV",
            "handheld/smartphone": "Handheld or\nsmartphone", "conveyor/lab": "Laboratory\nor conveyor",
            "fixed camera": "Fixed camera", "": "Not stated"}
    sel = defaultdict(Counter)
    nb = Counter()
    for r in c1:
        t = kat_tanaman(r, utama)
        nb[t] += 1
        for m in r["modalitas"].split(";"):
            sel[t][m] += 1
        for p in (r["platform"].split(";") if r["platform"] else [""]):
            sel[t][p] += 1
    baris = [t for t in baris if nb[t]]
    kol_mod = [k for k in kol_mod if any(sel[t][k] for t in baris)]
    kol_plat = [k for k in kol_plat if any(sel[t][k] for t in baris)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.25, 3.3), sharey=True, layout="constrained",
                                   gridspec_kw={"width_ratios": [len(kol_mod), len(kol_plat)]})
    maks = max(sel[t][k] for t in baris for k in kol_mod + kol_plat)
    for ax, kol, judul in [(ax1, kol_mod, "(a) Sensing modality"), (ax2, kol_plat, "(b) Platform")]:
        data = [[sel[t][k] for k in kol] for t in baris]
        # pcolormesh menghasilkan sel vektor (tidak diraster seperti imshow).
        im = ax.pcolormesh(data, cmap=PETA_WARNA, vmin=0, vmax=maks, edgecolors="white", linewidth=0.6)
        for i, t in enumerate(baris):
            for j, k in enumerate(kol):
                v = sel[t][k]
                if v:
                    ax.text(j + 0.5, i + 0.5, str(v), ha="center", va="center", fontsize=FS_KECIL,
                            color="white" if v / maks > 0.55 else "black")
        ax.set_xticks([j + 0.5 for j in range(len(kol))])
        ax.set_xticklabels([nama[k].replace("\n", " ") for k in kol], fontsize=FS_KECIL, rotation=35, ha="right", rotation_mode="anchor")
        ax.set_title(judul)
        ax.tick_params(length=0)
    ax1.set_yticks([i + 0.5 for i in range(len(baris))])
    ax1.set_yticklabels([f"{t} ({nb[t]})" for t in baris])
    ax1.invert_yaxis()
    cb = fig.colorbar(im, ax=[ax1, ax2], fraction=0.025, pad=0.015)
    cb.set_label("Number of studies")
    cb.solids.set_rasterized(False)
    cb.outline.set_linewidth(0.5)
    simpan(fig, "F10_sensor", LEBAR_SUPP)
    return {t: dict(sel[t]) for t in baris}


# ------------------------------------------- F11 foto sensus sawit (direproduksi, CC BY 4.0)
DIB_PDF = ROOT / "literature/references/SawitMVC-DiB-2026.pdf"


def citra_dib(halaman):
    """Citra tertanam pertama di halaman PDF Data in Brief SawitMVC.

    Butuh `pdfimages` (poppler). Citra tidak disimpan di repo; selalu diambil ulang dari PDF.
    """
    import subprocess
    import tempfile

    from PIL import Image

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdfimages", "-j", "-f", str(halaman), "-l", str(halaman), str(DIB_PDF),
                        f"{tmp}/img"], check=True)
        jalur = sorted(Path(tmp).glob("img-*.jpg"))[0]
        img = Image.open(jalur).convert("RGB")
        img.load()
    assert img.width == 1511, f"ukuran citra halaman {halaman} berubah: {img.size}"
    return img


# Batas piksel foto di citra DiB (tanpa label dan bilah teks bawaan, yang ditulis ulang di sini).
FOTO_SISI = [(564, 31, 795, 341), (797, 31, 1028, 341), (1031, 31, 1262, 341), (1264, 31, 1495, 341)]
FOTO_KELAS = [(12, 61, 379, 427), (385, 61, 752, 427), (758, 61, 1125, 427), (1132, 61, 1498, 427)]
LABEL_KELAS = ["B1 (≤1 month)", "B2 (~2 months)", "B3 (~3 months)", "B4 (~4 months)"]


def gambar_foto_sawit():
    import numpy as np
    from matplotlib.patches import Circle, Rectangle

    sisi = citra_dib(6)
    kelas = citra_dib(7)
    W = LEBAR_TEKS - 0.06
    jarak = 0.06
    lebar_skema = 1.45
    lebar_foto = (W - lebar_skema - 0.12 - 3 * jarak) / 4
    tinggi_foto = lebar_foto * 310 / 231
    lebar_kelas = (W - 3 * jarak) / 4
    tinggi_kelas = lebar_kelas * 366 / 367
    judul_h, label_h = 0.2, 0.17
    H = judul_h + label_h + tinggi_foto + 0.14 + judul_h + label_h + tinggi_kelas
    fig = plt.figure(figsize=(W, H))

    def kotak_in(x, y, w, h):
        return fig.add_axes((x / W, y / H, w / W, h / H))

    atas = H - judul_h
    fig.text(0, (atas + 0.04) / H, "(a) One palm photographed from four sides", fontsize=FS_JUDUL, va="bottom")
    ax = kotak_in(0, atas - label_h - tinggi_foto, lebar_skema, tinggi_foto + label_h)
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.75 * (tinggi_foto + label_h) / lebar_skema, 1.75 * (tinggi_foto + label_h) / lebar_skema)
    ax.set_aspect("equal")
    ax.axis("off")
    r = 0.8
    ax.add_patch(Circle((0, 0), r, fill=False, ls=(0, (3, 2)), lw=0.7, edgecolor=ABU))
    ax.add_patch(Circle((0, 0), 0.2, facecolor=REDUP, edgecolor=GARIS, lw=0.6))
    ax.text(0, -0.3, "trunk", ha="center", va="top", fontsize=FS_KECIL)
    for i, sudut in enumerate([90, 0, -90, 180]):
        t = np.radians(sudut)
        x, y = r * np.cos(t), r * np.sin(t)
        ax.add_patch(Rectangle((x - 0.08, y - 0.08), 0.16, 0.16, facecolor=AKSEN, edgecolor=GARIS, lw=0.5))
        if sudut in (90, -90):
            ax.text(x, y + 0.24 * np.sign(y), f"Side {i + 1}", ha="center", va="center", fontsize=FS)
        else:
            ax.text(x + 0.14 * np.sign(x), y, f"Side {i + 1}", ha="left" if x > 0 else "right", va="center",
                    fontsize=FS)
    u = np.array([np.cos(np.radians(-45)), np.sin(np.radians(-45))])
    ax.annotate("", xy=tuple(r * u), xytext=tuple(0.2 * u),
                arrowprops=dict(arrowstyle="<->", lw=0.6, color=GARIS, shrinkA=0, shrinkB=0))
    ax.text(*(0.5 * u + 0.3 * np.array([1, 1]) / np.sqrt(2)), "2–3 m", fontsize=FS_KECIL, rotation=-45,
            ha="center", va="center")

    x0 = lebar_skema + 0.12
    for i, kotak_px in enumerate(FOTO_SISI):
        x = x0 + i * (lebar_foto + jarak)
        ax = kotak_in(x, atas - label_h - tinggi_foto, lebar_foto, tinggi_foto)
        ax.imshow(np.asarray(sisi.crop(kotak_px)))
        ax.set_axis_off()
        fig.text((x + lebar_foto / 2) / W, (atas - label_h + 0.03) / H, f"Side {i + 1}", ha="center",
                 va="bottom", fontsize=FS)

    atas_b = atas - label_h - tinggi_foto - 0.14 - judul_h
    fig.text(0, (atas_b + 0.04) / H, "(b) The four census classes", fontsize=FS_JUDUL, va="bottom")
    for i, (kotak_px, label) in enumerate(zip(FOTO_KELAS, LABEL_KELAS)):
        x = i * (lebar_kelas + jarak)
        ax = kotak_in(x, atas_b - label_h - tinggi_kelas, lebar_kelas, tinggi_kelas)
        ax.imshow(np.asarray(kelas.crop(kotak_px)))
        ax.set_axis_off()
        fig.text((x + lebar_kelas / 2) / W, (atas_b - label_h + 0.03) / H, label, ha="center", va="bottom",
                 fontsize=FS)
    simpan(fig, "F11_foto_sawit")


# ------------------------------------------- F12 hasil yang dilaporkan pada data yang sama
JENIS_A = {"tidak ditautkan": ("Not linked (single view or sum)", ABU, "o"),
           "ditautkan dengan pelacakan": ("Linked by tracking", WARNA_MEK["M3"], "s"),
           "ditautkan dengan langkah geometris": ("Linked with a geometric step", WARNA_MEK["M4"], "^")}
JENIS_B = {"nomor identitas terbesar": ("Largest identity number", ABU, "o"),
           "satu garis hitung": ("Single counting line", AKSEN2, "s"),
           "aturan hitung penulis": ("Authors' counting rule", AKSEN, "^")}


NASKAH = ROOT / "manuscript/source"
SUFIKS_TAHUN = {"zheng2023efficient": "b", "zhou2024advancing": "b"}
TANDA_AKSEN = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303"}


def label_sitasi(kunci_gambar):
    """kunci di gambar -> label penulis-tahun seperti di daftar pustaka naskah (natbib), termasuk sufiks a/b."""
    bib = (NASKAH / "references6.bib").read_text(encoding="utf-8")
    dikutip = set()
    for f in NASKAH.glob("main6*.tex"):
        for g in re.findall(r"\\cite[a-z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", f.read_text(encoding="utf-8")):
            dikutip.update(k.strip() for k in g.split(","))
    dasar = {}
    for kunci, isi in re.findall(r"@\w+\{([^,]+),(.*?)\n\}", bib, re.S):
        penulis = re.search(r"author = \{(.*)\},?\n", isi).group(1).split(" and ")
        nama = penulis[0].split(",")[0]
        nama = re.sub(r"\{?\\([\"'`^~])\{?([A-Za-z])\}?\}?", lambda m: m.group(2) + TANDA_AKSEN[m.group(1)], nama)
        nama = unicodedata.normalize("NFC", nama.replace("{", "").replace("}", ""))
        tahun = re.search(r"year = \{(\d{4})\}", isi).group(1)
        dasar[kunci] = (nama + (" et al." if len(penulis) > 2 else " and " + penulis[1].split(",")[0] if len(penulis) == 2 else ""), tahun)
    label = {}
    for kunci in kunci_gambar & set(dasar):
        nama, tahun = dasar[kunci]
        kembar = sorted(k for k in dikutip if dasar.get(k) == (nama, tahun))
        if len(kembar) > 1:
            assert kunci in SUFIKS_TAHUN, f"{kunci}: tambahkan sufiks tahun dari daftar pustaka naskah ke SUFIKS_TAHUN ({kembar})"
            tahun += SUFIKS_TAHUN[kunci]
        label[kunci] = f"{nama} ({tahun})"
    return label


def gambar_hasil(mat):
    baris = list(csv.DictReader(open(TOPIK / "bukti/nilai_terlapor.csv", encoding="utf-8")))
    penulis = label_sitasi({b["kunci"] for b in baris})
    kunci_hilang = {b["kunci"] for b in baris} - set(penulis)
    assert not kunci_hilang, f"kunci tidak ada di matriks bukti: {kunci_hilang}"
    assert {b["jenis_lengan"] for b in baris if b["panel"] == "a"} <= set(JENIS_A)
    assert {b["jenis_lengan"] for b in baris if b["panel"] == "b"} <= set(JENIS_B)

    def nilai(b):
        lo, hi = float(b["nilai_bawah"]), float(b["nilai_atas"])
        if b["nilai_rujukan"]:
            ref = float(b["nilai_rujukan"])
            lo, hi = 100 * lo / ref, 100 * hi / ref
        return lo, hi

    def tata_baris(rows):
        """Satu baris per lengan; judul kajian di atas kelompoknya."""
        posisi, judul, y, sebelum = {}, [], 0.0, None
        for b in rows:
            kunci = (b["kunci"], b["lengan"])
            if kunci in posisi:
                continue
            if b["kunci"] != sebelum:
                data = b["data"][0].lower() + b["data"][1:]
                judul.append((y, f"{penulis[b['kunci']]}; {data}"))
                y += 1.05
            posisi[kunci] = y
            sebelum = b["kunci"]
            y += 1
        return posisi, judul, y

    def judul_kajian(ax, judul):
        for yy, t in judul:
            ax.text(0.004, yy, t, transform=ax.get_yaxis_transform(), ha="left", va="center",
                    style="italic")

    def legenda(ax, jenis, turun):
        ax.legend(handles=[plt.Line2D([], [], marker=m, color=c, ls="", mec=GARIS, mew=0.4, label=n)
                           for n, c, m in jenis.values()],
                  loc="upper center", bbox_to_anchor=(0.5, -turun), ncol=3)

    a = [b for b in baris if b["panel"] == "a"]
    b_rows = [b for b in baris if b["panel"] == "b"]
    pos_a, judul_a, tinggi_a = tata_baris(a)
    pos_b, judul_b, tinggi_b = tata_baris(b_rows)
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(6.0, 0.24 * (tinggi_a + tinggi_b) + 1.6),
                                     gridspec_kw={"height_ratios": [tinggi_a, tinggi_b], "hspace": 0.38})

    for b in a:
        nama, warna, penanda = JENIS_A[b["jenis_lengan"]]
        yy = pos_a[(b["kunci"], b["lengan"])]
        lo, hi = nilai(b)
        ax_a.plot([0, lo], [yy, yy], color=warna, lw=0.7, alpha=0.6)
        if hi > lo:
            ax_a.plot([lo, hi], [yy, yy], color=warna, lw=3.2, solid_capstyle="butt")
        ax_a.plot([hi], [yy], penanda, color=warna, ms=5, mec=GARIS, mew=0.4)
        if b["nilai_rujukan"]:
            teks = f"{lo:.1f}"
        else:
            teks = b["nilai_bawah"] if hi == lo else f"{b['nilai_bawah']}–{b['nilai_atas']}"
        ax_a.text(hi + 3, yy, teks, va="center", fontsize=FS_KECIL)
    ax_a.axvline(100, color=GARIS, lw=0.6, ls="--")
    ax_a.set_yticks(list(pos_a.values()))
    ax_a.set_yticklabels([l for _, l in pos_a])
    judul_kajian(ax_a, judul_a)
    ax_a.set_ylim(tinggi_a - 0.5, -0.6)
    ax_a.set_xlim(0, 200)
    ax_a.set_xlabel("Count relative to the reference (%)")
    ax_a.set_title("(a) Linked and unlinked counts")
    legenda(ax_a, JENIS_A, 0.11)

    for (k, l), yy in pos_b.items():
        vals = sorted(float(b["nilai_bawah"]) for b in b_rows if b["kunci"] == k and b["lengan"] == l)
        ax_b.plot([vals[0], vals[-1]], [yy, yy], color=REDUP, lw=0.7)
    for b in b_rows:
        nama, warna, penanda = JENIS_B[b["jenis_lengan"]]
        yy = pos_b[(b["kunci"], b["lengan"])]
        v = float(b["nilai_bawah"])
        ax_b.plot([v], [yy], penanda, color=warna, ms=5, mec=GARIS, mew=0.4, zorder=3)
        rata = {"aturan hitung penulis": "right", "satu garis hitung": "left"}.get(b["jenis_lengan"], "center")
        ax_b.text(v, yy - 0.28, b["nilai_bawah"], ha=rata, va="bottom", fontsize=FS_KECIL)
    ax_b.set_xscale("log")
    ax_b.set_xlim(3, 700)
    ax_b.set_xticks([5, 10, 20, 50, 100, 200, 500])
    ax_b.set_xticklabels(["5", "10", "20", "50", "100", "200", "500"])
    ax_b.minorticks_off()
    ax_b.set_yticks(list(pos_b.values()))
    ax_b.set_yticklabels([l for _, l in pos_b])
    metrik = {b["kunci"]: "mean relative error" if b["metrik"].startswith("galat relatif") else "MAPE"
              for b in b_rows}
    judul_kajian(ax_b, [(yy, t + "; " + metrik[k]) for (yy, t), k in
                        zip(judul_b, dict.fromkeys(b["kunci"] for b in b_rows))])
    ax_b.set_ylim(tinggi_b - 0.4, -0.6)
    ax_b.set_xlabel("Count error (%, log scale)")
    ax_b.set_title("(b) Counting rules on the same tracks")
    legenda(ax_b, JENIS_B, 0.2)
    simpan(fig, "F12_hasil")
    return len(a), len(b_rows)


def main():
    pilih = {a.upper() for a in sys.argv[1:]}

    def mau(kode):
        return not pilih or kode in pilih

    mat = muat_matriks()
    if mau("F01"):
        print("PRISMA", gambar_prisma())
    if mau("F02"):
        gambar_tahun(mat)
    if mau("F03"):
        gambar_kerangka()
    if mau("F04"):
        per, n_per, ak = gambar_mekanisme(mat)
        print("akuisisi", ak)
    if mau("F05"):
        gambar_peta_tanaman(mat)
    if mau("F06"):
        gambar_sawit(mat)
    if mau("F07"):
        hit, n_abs, kelas = gambar_metrik(mat)
        print("metrik", hit, n_abs, "per-kelas", kelas)
    if mau("F08"):
        print("istilah", gambar_istilah(mat))
    if mau("F09"):
        print("alur", gambar_alur(mat))
    if mau("F10"):
        print("sensor", gambar_sensor(mat))
    if mau("F11"):
        gambar_foto_sawit()
    if mau("F12"):
        print("hasil", gambar_hasil(mat))
    if mau("F13"):
        print("metrik dan rujukan", gambar_metrik_rujukan(mat))


if __name__ == "__main__":
    main()
