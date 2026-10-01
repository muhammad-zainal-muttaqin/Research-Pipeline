#!/usr/bin/env python3
"""Membuat semua gambar naskah main6 dari data penyaringan dan matriks bukti.

Semua angka pada gambar dihitung ulang dari berkas di literature/scopus-2026-09,
sehingga gambar selalu sesuai dengan data. Keluaran: PDF (vektor, untuk LaTeX)
dan PNG (pratinjau) di manuscript/figures/main6/.

  python3 tools/scopus/gambar_tinjauan.py            # semua gambar
  python3 tools/scopus/gambar_tinjauan.py F08 F09    # gambar tertentu saja
"""
import csv
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, PathPatch
from matplotlib.path import Path as MPath

ROOT = Path(__file__).resolve().parents[2]
TOPIK = ROOT / "literature/scopus-2026-09/topik"
OUT = ROOT / "manuscript/figures/main6"
OUT.mkdir(parents=True, exist_ok=True)

# Palet Okabe-Ito (aman untuk buta warna).
C = {"hitam": "#000000", "oranye": "#E69F00", "biru_muda": "#56B4E9",
     "hijau": "#009E73", "kuning": "#F0E442", "biru": "#0072B2",
     "merah": "#D55E00", "ungu": "#CC79A7", "abu": "#8C8C8C", "abu_muda": "#D9D9D9"}

plt.rcParams.update({
    # Huruf serif setara Times agar sama dengan teks naskah; sumbu berbingkai penuh.
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Liberation Serif", "Nimbus Roman", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 8,
    "axes.titlesize": 8.5,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "axes.linewidth": 0.6,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "legend.edgecolor": "#888888",
    "legend.fancybox": False,
    "pdf.fonttype": 42,
})

KATEGORI = {
    "C1": "Multi-observation studies",
    "C2": "Single-view counting studies",
    "C3": "Oil-palm studies",
    "C4": "Single-image class-wise counting studies",
    "C5": "Depth and 3D sensing studies",
    "R": "Earlier reviews",
    "T": "Methods papers from outside agriculture",
}
WARNA_KAT = {"C1": C["biru"], "C2": C["biru_muda"], "C3": C["merah"],
             "C4": C["oranye"], "C5": C["hijau"], "R": C["ungu"], "T": C["abu"]}

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
WARNA_MEK = {"M0": C["abu_muda"], "M1": C["kuning"], "M2": C["ungu"],
             "M3": C["biru"], "M4": C["hijau"], "M5": C["merah"]}


def simpan(fig, nama):
    fig.savefig(OUT / f"{nama}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{nama}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


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
    counts = list(csv.DictReader(open(TOPIK / "counts.csv")))
    diambil = sum(int(r["retrieved"]) for r in counts)
    unik = sum(1 for _ in csv.DictReader(open(TOPIK / "records_all.csv")))
    tj = list(csv.DictReader(open(TOPIK / "penyaringan/tahap_judul.csv")))
    x0 = sum(1 for r in tj if r["keputusan_judul"] == "X0")
    xj = sum(1 for r in tj if r["keputusan_judul"] == "X")
    dec = muat_keputusan()
    kand = len(dec)
    xa = Counter(d[1] for d in dec.values() if d[0] == "X")
    inc = Counter(d[0] for d in dec.values() if d[0] != "X")
    n_inc = sum(inc.values())
    judul_saja = 0
    for fn in glob.glob(str(TOPIK / "penyaringan/abstrak_*.txt")):
        for line in open(fn):
            if re.match(r"^\d+\s", line) and ("T00" in fn or "(judul)" in line):
                judul_saja += 1

    lain = muat_tambahan()
    n_lain = len(lain)
    kanan = 128 if n_lain else 100
    fig, ax = plt.subplots(figsize=(7.0 * kanan / 100, 5.6))
    ax.set_xlim(0, kanan)
    ax.set_ylim(0, 100)
    ax.axis("off")

    def kotak(x, y, w, h, teks, warna="#FFFFFF", tebal=False):
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8",
                           linewidth=0.7, edgecolor="#333333", facecolor=warna)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, teks, ha="center", va="center", fontsize=7,
                fontweight="bold" if tebal else "normal", linespacing=1.3)

    def panah(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=8, linewidth=0.7, color="#333333"))

    for y, lab in [(88, "Identification"), (64, "Screening"), (37, "Eligibility"), (9, "Included")]:
        ax.text(1, y, lab, rotation=90, ha="left", va="center", fontsize=7.5,
                fontweight="bold", color="#444444")

    kotak(8, 82, 44, 13,
          f"Records identified from Scopus\n"
          f"n = {diambil:,}")
    kotak(60, 82, 36, 13,
          f"Duplicates removed\nn = {diambil - unik:,}",
          warna="#F2F2F2")
    panah(52, 88.5, 60, 88.5)
    kotak(8, 62, 44, 12, f"Unique records\nn = {unik:,}")
    panah(30, 82, 30, 74)
    kotak(60, 62, 36, 12,
          f"Removed by document type\n(proceedings front matter, errata, notes,\neditorials, letters, retracted)\nn = {x0}", warna="#F2F2F2")
    panah(52, 68, 60, 68)
    kotak(8, 44, 44, 12,
          f"Titles screened\nn = {unik - x0:,}")
    panah(30, 62, 30, 56)
    kotak(60, 44, 36, 12, f"Excluded at title stage\nn = {xj:,}", warna="#F2F2F2")
    panah(52, 50, 60, 50)
    kotak(8, 26, 44, 12,
          f"Records assessed for eligibility\nn = {kand:,}\n"
          f"with abstract {kand - judul_saja}; title and source only {judul_saja}")
    panah(30, 44, 30, 38)
    alasan = (f"Excluded, n = {sum(xa.values())}\n"
              f"Not fruit on the plant: {xa['E1']}\n"
              f"Postharvest or laboratory only: {xa['E2']}\n"
              f"Yield model without fruit-level detection: {xa['E3']}\n"
              f"Picking or manipulation only: {xa['E4']}\n"
              f"Detection without counting or evaluation: {xa['E5']}\n"
              f"Non-imaging sensor: {xa['E6']}; not in English: {xa['E7']}")
    kotak(56, 21, 42, 20, alasan, warna="#F2F2F2")
    panah(52, 32, 56, 32)
    nama = {"C1": "multi-observation", "C2": "single-view counting", "C3": "oil palm",
            "C4": "single-image class-wise counting", "C5": "depth and 3D sensing",
            "R": "earlier reviews", "T": "methods outside agriculture"}
    b1 = ", ".join(f"{nama[k]} {inc[k]}" for k in ["C1", "C2", "C3", "C4"])
    b2 = ", ".join(f"{nama[k]} {inc[k]}" for k in ["C5", "R", "T"])
    rinci = b1 + "\n" + b2
    if n_lain:
        kl = Counter(r["kode"] for r in lain)
        b3 = ", ".join(f"{nama[k]} {kl[k]}" for k in ["C1", "C2", "C3", "C4", "C5", "R", "T"] if kl[k])
        ax.text(30, 98.5, "Identification of studies via Scopus", ha="center", fontsize=7.2, style="italic")
        ax.text(114.5, 98.5, "Identification via other methods", ha="center", fontsize=7.2, style="italic")
        kotak(103, 82, 23, 13, f"Records identified from\na check of known papers\nn = {n_lain}")
        kotak(103, 26, 23, 12, f"Reports assessed\nfor eligibility\nn = {n_lain}")
        panah(114.5, 82, 114.5, 38)
        panah(114.5, 26, 114.5, 16)
        kotak(8, 2, 118, 14, f"Studies included, n = {n_inc + n_lain} "
              f"({n_inc} from Scopus: {b1},\n{b2}; {n_lain} from other methods: {b3})",
              warna="#EAF2FA", tebal=False)
    else:
        kotak(8, 2, 90, 14, f"Studies included, n = {n_inc}\n{rinci}", warna="#EAF2FA", tebal=False)
    panah(30, 26, 30, 16)
    simpan(fig, "F01_prisma")
    return {"diambil": diambil, "unik": unik, "x0": x0, "xj": xj, "kand": kand,
            "judul_saja": judul_saja, "xa": xa, "inc": inc, "metode_lain": n_lain}


# ---------------------------------------------------- F2 corpus per tahun
def gambar_tahun(mat):
    tahun = list(range(2012, 2027))
    hitung = defaultdict(Counter)
    for r in mat:
        hitung[r["kode"]][int(r["year"])] += 1
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    dasar = [0] * len(tahun)
    for k in ["C1", "C2", "C3", "C4", "C5", "R", "T"]:
        v = [hitung[k][t] for t in tahun]
        ax.bar(tahun, v, bottom=dasar, color=WARNA_KAT[k], width=0.78,
               label=KATEGORI[k], linewidth=0)
        dasar = [a + b for a, b in zip(dasar, v)]
    for t, d in zip(tahun, dasar):
        ax.text(t, d + 2, str(d), ha="center", va="bottom", fontsize=6.3)
    ax.set_xticks(tahun)
    ax.set_xticklabels([str(t) if t < 2026 else "2026*" for t in tahun])
    ax.set_ylabel("Included studies")
    ax.set_ylim(0, max(dasar) * 1.12)
    ax.legend(ncol=2, frameon=False, loc="upper left")
    ax.text(0.995, -0.2, "* 2026 records indexed up to 28 September 2026",
            transform=ax.transAxes, ha="right", fontsize=6.3, color="#555555")
    simpan(fig, "F02_tahun")


# ------------------------------------------- F3 kerangka ruang rancangan
def gambar_kerangka():
    fig, ax = plt.subplots(figsize=(7.0, 3.9))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis("off")

    def kotak(x, y, w, h, judul, isi, warna):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1",
                                    linewidth=0.7, edgecolor="#333333", facecolor=warna))
        ax.text(x + w / 2, y + h - 2.2, judul, ha="center", va="top", fontsize=7.4,
                fontweight="bold")
        ax.text(x + w / 2, y + h - 6.2, isi, ha="center", va="top", fontsize=6.4,
                linespacing=1.35)

    def panah(x1, y1, x2, y2, teks=None):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=9, linewidth=0.8, color="#333333"))
        if teks:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 1.4, teks, ha="center", fontsize=6,
                    color="#444444")

    kotak(1, 33, 16, 25, "1  Acquisition", "views per plant\nordering (video or\ndiscrete views)\npose, depth,\nbaseline, sides", "#F7F7F7")
    kotak(20, 33, 16, 25, "2  Observation", "detections or\nmasks in each\nimage; one\nfruit may yield\nseveral boxes", "#F7F7F7")
    kotak(39, 33, 19, 25, "3  Association", "decide which\nobservations belong\nto the same fruit\n(six mechanisms\nbelow)", "#EAF2FA")
    kotak(61, 33, 20, 25, "4  Attribute assignment", "class label, size,\nmass assigned to\nthe unique\ninstance, not to\neach box", "#FFF4E0")
    kotak(84, 33, 15, 25, "5  Inventory", "one record per\nphysical fruit,\naggregated by\nclass, tree, row,\nor block", "#EAF7F1")
    panah(17, 45.5, 20, 45.5)
    panah(36, 45.5, 39, 45.5)
    panah(58, 45.5, 61, 45.5)
    panah(81, 45.5, 84, 45.5)

    y0 = 2
    lebar = 15.6
    for i, m in enumerate(MEK):
        x = 1 + i * (lebar + 1.0)
        asumsi = {
            "M0": "each fruit is seen\nonce, or duplicates\nare ignored",
            "M1": "duplication is stable\nenough to calibrate\nagainst hand counts",
            "M2": "fruit look different\nenough to be matched\nby appearance",
            "M3": "consecutive frames\noverlap; motion is\nsmooth and bounded",
            "M4": "pose, scale, and\ndepth or reconstruction\nare reliable",
            "M5": "linked identities\nexist to train and\ntest the matcher",
        }[m]
        ax.add_patch(FancyBboxPatch((x, y0), lebar, 23, boxstyle="round,pad=0.25,rounding_size=0.8",
                                    linewidth=0.6, edgecolor="#333333", facecolor=WARNA_MEK[m], alpha=0.35))
        judul2 = {"M0": "No\nassociation", "M1": "Statistical\ncorrection",
                  "M2": "Appearance\nmatching", "M3": "Temporal\ntracking",
                  "M4": "Geometric or 3D\nassociation", "M5": "Learned\nassociation"}[m]
        ax.text(x + lebar / 2, y0 + 21.5, judul2, ha="center",
                va="top", fontsize=6.5, fontweight="bold", linespacing=1.15)
        ax.text(x + lebar / 2, y0 + 11.2, "Assumes:", ha="center", va="top", fontsize=6.0,
                style="italic", color="#333333")
        ax.text(x + lebar / 2, y0 + 8.4, asumsi, ha="center", va="top", fontsize=5.9,
                linespacing=1.25)
    ax.add_patch(FancyArrowPatch((48.5, 33), (48.5, 26.2), arrowstyle="-|>", mutation_scale=9,
                                 linewidth=0.8, color="#333333"))
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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.7), gridspec_kw={"width_ratios": [1.45, 1]})
    lebar = 0.13
    for j, m in enumerate(MEK):
        v = [100 * per[p][m] / n_per[p] if n_per[p] else 0 for p in periode]
        xs = [i + (j - 2.5) * lebar for i in range(len(periode))]
        ax1.bar(xs, v, width=lebar, color=WARNA_MEK[m], edgecolor="#555555", linewidth=0.3,
                label=NAMA_MEK[m])
    ax1.set_xticks(range(len(periode)))
    ax1.set_xticklabels([f"{l}\n(n = {n_per[p]})" for l, p in zip(lab, periode)])
    ax1.set_ylabel("Share of studies using the mechanism (%)")
    ax1.set_ylim(0, 100)
    ax1.legend(frameon=False, fontsize=6.2, ncol=2, loc="upper left")
    ax1.set_title("(a) Association mechanisms by period", loc="left")

    akuisisi = Counter(r["akuisisi_manual"] for r in c1)
    nama_ak = {"V": "Video along a path", "D": "Discrete views", "S": "3D scan",
               "T": "Revisits over time", "1": "Single view"}
    urut = ["V", "D", "S", "T", "1"]
    ax2.barh([nama_ak[k] for k in urut][::-1], [akuisisi[k] for k in urut][::-1],
             color=C["biru"], height=0.6)
    for i, k in enumerate(urut[::-1]):
        ax2.text(akuisisi[k] + 2, i, str(akuisisi[k]), va="center", fontsize=6.5)
    ax2.set_xlabel("Studies")
    ax2.set_xlim(0, max(akuisisi.values()) * 1.18)
    ax2.set_title("(b) Acquisition design", loc="left")
    fig.tight_layout(w_pad=2)
    simpan(fig, "F04_mekanisme")
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
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    maks = max(v for d in sel.values() for v in d.values())
    for i, t in enumerate(baris):
        for j, m in enumerate(MEK):
            v = sel[t][m]
            if v:
                ax.scatter(j, i, s=18 + 380 * v / maks, color=WARNA_MEK[m], edgecolor="#333333",
                           linewidth=0.4, alpha=0.9, zorder=3)
                ax.text(j, i, str(v), ha="center", va="center", fontsize=6.6, zorder=4)
    ax.set_xticks(range(len(MEK)))
    ax.set_xticklabels([NAMA_MEK[m].replace(" ", "\n", 1).replace("or 3D\n", "or 3D ").replace("Geometric\nor 3D association", "Geometric or 3D\nassociation")
                        for m in MEK], fontsize=6.2)
    ax.set_yticks(range(len(baris)))
    lab = []
    for t in baris:
        n = sum(1 for r in c1 if ((r["tanaman"] or "crop not named").split(";")[0] if (r["tanaman"] or "crop not named").split(";")[0] in utama else "other crops") == t)
        lab.append(f"{t} ({n})")
    ax.set_yticklabels(lab)
    ax.invert_yaxis()
    ax.set_xlim(-0.6, len(MEK) - 0.4)
    ax.grid(color="#EEEEEE", linewidth=0.5, zorder=0)
    ax.set_xlabel("Association mechanism (a study may use several)")
    simpan(fig, "F05_tanaman_mekanisme")


# ------------------------------------------- F6 korpus kelapa sawit
def gambar_sawit(mat):
    c3 = muat_c3()
    tahun = {int(r["idx"]): int(r["year"]) for r in mat}
    tugas = ["KLS", "DET", "HIT", "LF", "MUTU", "SENSOR", "DATA"]
    nama_t = {"KLS": "Ripeness classification\nof bunch images", "DET": "Bunch detection\nin a scene",
              "HIT": "Bunch counting", "LF": "Loose fruit\ndetection", "MUTU": "Quality, defect,\nmass, or pose",
              "SENSOR": "Non-RGB sensing\n(spectral, thermal, laser)", "DATA": "Dataset papers"}
    lokasi = ["POHON", "TANAH", "PABRIK", "UAV", "?"]
    nama_l = {"POHON": "On the palm", "TANAH": "Ground or\ncollection point", "PABRIK": "Mill, conveyor,\nor laboratory",
              "UAV": "UAV", "?": "Not reported"}
    m = defaultdict(Counter)
    for v in c3.values():
        if v["tugas"] in tugas:
            m[v["tugas"]][v["lokasi"]] += 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0), gridspec_kw={"width_ratios": [1.35, 1]})
    maks = max(c for d in m.values() for c in d.values())
    for i, t in enumerate(tugas):
        for j, l in enumerate(lokasi):
            v = m[t][l]
            ax1.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color=C["merah"],
                                        alpha=0.08 + 0.8 * v / maks if v else 0.0, linewidth=0))
            if v:
                ax1.text(j, i, str(v), ha="center", va="center", fontsize=6.6,
                         color="white" if v / maks > 0.55 else "black")
    ax1.set_xlim(-0.5, len(lokasi) - 0.5)
    ax1.set_ylim(len(tugas) - 0.5, -0.5)
    ax1.set_xticks(range(len(lokasi)))
    ax1.set_xticklabels([nama_l[l] for l in lokasi], fontsize=6.2)
    ax1.set_yticks(range(len(tugas)))
    ax1.set_yticklabels([f"{nama_t[t]} ({sum(m[t].values())})" for t in tugas], fontsize=6.2)
    ax1.set_title(f"(a) Oil-palm studies by task and setting (n = {len(c3)})", loc="left")
    for s in ax1.spines.values():
        s.set_visible(False)
    ax1.tick_params(length=0)

    th = list(range(2012, 2027))
    semua = Counter(tahun[i] for i in c3)
    mv = Counter(tahun[i] for i, v in c3.items() if v["multipandang"] == "Y")
    hit = Counter(tahun[i] for i, v in c3.items() if v["tugas"] == "HIT")
    ax2.bar(th, [semua[t] for t in th], color=C["abu_muda"], width=0.8, label="All oil-palm studies")
    ax2.bar(th, [hit[t] for t in th], color=C["merah"], width=0.8, label="Counting studies")
    thv = [t for t in th if mv[t]]
    ax2.plot(thv, [mv[t] for t in thv], "o", color=C["biru"], markersize=3.4,
             label="Several views of the same bunch or tree")
    ax2.set_xticks([2012, 2015, 2018, 2021, 2024, 2026])
    ax2.set_ylabel("Studies")
    ax2.legend(frameon=False, fontsize=6.1, loc="upper left")
    ax2.set_title("(b) By year", loc="left")
    fig.tight_layout(w_pad=1.5)
    simpan(fig, "F06_sawit")
    return c3


# ------------------------------------------- F7 metrik yang dilaporkan
def gambar_metrik(mat):
    c1 = [r for r in mat if r["kode"] == "C1" and r["mekanisme"] != "DATA"]
    kel = {
        "Count agreement (MAE, RMSE, R2, MAPE, count accuracy)": {"MAE", "RMSE", "R2", "MAPE/rel. error", "count accuracy"},
        "Tracking or identity (MOTA, IDF1, HOTA, ID switches)": {"MOTA", "IDF1", "HOTA", "ID switch"},
        "Detection quality (mAP, AP, F1)": {"mAP/AP", "F1"},
    }
    ada_abs = [r for r in c1 if r["ada_abstrak"] == "ya"]
    hit = Counter()
    for r in ada_abs:
        ms = set(r["metrik"].split(";")) if r["metrik"] else set()
        for k, s in kel.items():
            if ms & s:
                hit[k] += 1
        if not ms:
            hit["No quantitative metric in the abstract"] += 1
    kelas = sum(1 for r in c1 if r["per_kelas"] == "Y")
    fig, ax = plt.subplots(figsize=(4.6, 2.3))
    urut = list(kel) + ["No quantitative metric in the abstract"]
    vals = [100 * hit[k] / len(ada_abs) for k in urut]
    ax.barh(range(len(urut))[::-1], vals, color=[C["biru"], C["hijau"], C["abu"], C["abu_muda"]], height=0.6)
    for i, (k, v) in enumerate(zip(urut, vals)):
        ax.text(v + 1, len(urut) - 1 - i, f"{hit[k]} ({v:.0f}%)", va="center", fontsize=7.5)
    ax.set_yticks(range(len(urut))[::-1])
    ax.set_yticklabels([k.replace(" (", "\n(") for k in urut], fontsize=7.5)
    ax.set_xlim(0, 100)
    ax.set_xlabel(f"Share of the {len(ada_abs)} multi-observation studies with an abstract (%)\n"
                  "(a study may report several metric types)")
    simpan(fig, "F07_metrik")
    return hit, len(ada_abs), kelas


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
    warna_kom = [C["biru"], C["merah"], C["hijau"], C["oranye"], C["ungu"], C["biru_muda"], C["abu"]]
    warna = {n: warna_kom[min(i, len(warna_kom) - 1)] for i, c in enumerate(kom) for n in c}
    # Tata letak Kamada-Kawai (deterministik): jarak sasaran mengecil bila asosiasi kuat.
    smaks = max(d["s"] for _, _, d in G.edges(data=True))
    jarak = {a: {b: 3.4 for b in G} for a in G}
    for a, b, d in G.edges(data=True):
        jarak[a][b] = jarak[b][a] = 1.0 + 2.0 * (1 - (d["s"] / smaks) ** 0.5)
    for a in G:
        jarak[a][a] = 0.0
    pos = nx.kamada_kawai_layout(G, dist=jarak)
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    wmaks = max(d["w"] for _, _, d in G.edges(data=True))
    for a, b, d in sorted(G.edges(data=True), key=lambda e: e[2]["w"]):
        sama = warna[a] == warna[b]
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=warna[a] if sama else "#BBBBBB",
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
                            zorder=4, fontsize=6.0 + 2.2 * (frek[n] / nmaks) ** 0.5)
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
    simpan(fig, "F08_istilah")
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
    warna_m = dict(WARNA_MEK)
    warna_m.update({"M0": C["abu"], "M2+M3": C["biru_muda"], "M3+M4": C["oranye"],
                    "Other combinations": "#555555"})
    jalur = [(nama_ak[r["akuisisi_manual"]], kat_mekanisme(r), kat_platform(r), kat_tanaman(r, utama))
             for r in c1]
    n = len(jalur)
    urut = [[k for k in kol if any(j[i] == k for j in jalur)] for i, kol in enumerate(urut)]
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
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
            ax.add_patch(plt.Rectangle((xs[i] - lebar, y - h), 2 * lebar, h, color="#3A3A3A", linewidth=0))
            lab = nama_gabungan(k) if i == 1 and k != "Other combinations" else k
            if 0 < i < 3:
                ax.text(xs[i], y + 0.003, f"{lab} ({tot[k]})", ha="center", va="bottom", fontsize=5.6, zorder=5,
                        bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor="none", alpha=0.75))
            else:
                ha, dx = ("right", -lebar - 0.02) if i == 0 else ("left", lebar + 0.02)
                ax.text(xs[i] + dx, y - h / 2, f"{k} ({tot[k]})", ha=ha, va="center", fontsize=6.0)
            y -= h + celah
        posisi.append(d)
        ax.text(xs[i], 1.075, judul[i], ha="center", va="bottom", fontsize=7.4, fontweight="bold")
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
              ncol=5, frameon=False, fontsize=6.0, loc="upper center",
              bbox_to_anchor=(0.5, 0.0), handlelength=1.2, columnspacing=1.0, handletextpad=0.4)
    ax.set_xlim(-0.55, 3.45)
    ax.set_ylim(-0.02, 1.13)
    ax.axis("off")
    simpan(fig, "F09_alur")
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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.3), sharey=True, layout="constrained",
                                   gridspec_kw={"width_ratios": [len(kol_mod), len(kol_plat)]})
    maks = max(sel[t][k] for t in baris for k in kol_mod + kol_plat)
    for ax, kol, judul in [(ax1, kol_mod, "(a) Sensing modality"), (ax2, kol_plat, "(b) Platform")]:
        data = [[sel[t][k] for k in kol] for t in baris]
        # pcolormesh menghasilkan sel vektor (tidak diraster seperti imshow).
        im = ax.pcolormesh(data, cmap="Blues", vmin=0, vmax=maks, edgecolors="white", linewidth=0.6)
        for i, t in enumerate(baris):
            for j, k in enumerate(kol):
                v = sel[t][k]
                if v:
                    ax.text(j + 0.5, i + 0.5, str(v), ha="center", va="center", fontsize=6.8,
                            color="white" if v / maks > 0.55 else "black")
        ax.set_xticks([j + 0.5 for j in range(len(kol))])
        ax.set_xticklabels([nama[k] for k in kol], fontsize=6.6, rotation=35, ha="right", rotation_mode="anchor")
        ax.set_title(judul, loc="left")
        ax.tick_params(length=0)
    ax1.set_yticks([i + 0.5 for i in range(len(baris))])
    ax1.set_yticklabels([f"{t} ({nb[t]})" for t in baris])
    ax1.invert_yaxis()
    cb = fig.colorbar(im, ax=[ax1, ax2], fraction=0.025, pad=0.015)
    cb.set_label("Number of studies", fontsize=6.5)
    cb.solids.set_rasterized(False)
    cb.outline.set_linewidth(0.5)
    simpan(fig, "F10_sensor")
    return {t: dict(sel[t]) for t in baris}


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


if __name__ == "__main__":
    main()
