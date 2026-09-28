#!/usr/bin/env python3
"""Membuat semua gambar naskah main6 dari data penyaringan dan matriks bukti.

Semua angka pada gambar dihitung ulang dari berkas di literature/scopus-2026-09,
sehingga gambar selalu sesuai dengan data. Keluaran: PDF (vektor, untuk LaTeX)
dan PNG (pratinjau) di manuscript/figures/main6/.

  python3 tools/scopus/gambar_tinjauan.py
"""
import csv
import glob
import re
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[2]
TOPIK = ROOT / "literature/scopus-2026-09/topik"
OUT = ROOT / "manuscript/figures/main6"
OUT.mkdir(parents=True, exist_ok=True)

# Palet Okabe-Ito (aman untuk buta warna).
C = {"hitam": "#000000", "oranye": "#E69F00", "biru_muda": "#56B4E9",
     "hijau": "#009E73", "kuning": "#F0E442", "biru": "#0072B2",
     "merah": "#D55E00", "ungu": "#CC79A7", "abu": "#8C8C8C", "abu_muda": "#D9D9D9"}

plt.rcParams.update({
    "font.family": "Liberation Sans",
    "font.size": 8,
    "axes.titlesize": 8.5,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "pdf.fonttype": 42,
})

KATEGORI = {
    "C1": "Multi-observation counting",
    "C2": "Single-view counting and yield",
    "C3": "Oil-palm bunch imaging",
    "C4": "Counting by class in single images",
    "C5": "Depth, 3D, and non-RGB fruit sensing",
    "R": "Earlier reviews",
    "T": "Methods from outside agriculture",
}
WARNA_KAT = {"C1": C["biru"], "C2": C["biru_muda"], "C3": C["merah"],
             "C4": C["oranye"], "C5": C["hijau"], "R": C["ungu"], "T": C["abu"]}

MEK = ["M0", "M1", "M2", "M3", "M4", "M5"]
NAMA_MEK = {
    "M0": "M0 No association",
    "M1": "M1 Statistical correction",
    "M2": "M2 Appearance matching",
    "M3": "M3 Temporal tracking",
    "M4": "M4 Geometric / 3D association",
    "M5": "M5 Learned association",
}
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

    fig, ax = plt.subplots(figsize=(7.0, 5.6))
    ax.set_xlim(0, 100)
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
            "C4": "class counting", "C5": "depth and 3D", "R": "reviews", "T": "outside agriculture"}
    b1 = ", ".join(f"{nama[k]} {inc[k]}" for k in ["C1", "C2", "C3", "C4"])
    b2 = ", ".join(f"{nama[k]} {inc[k]}" for k in ["C5", "R", "T"])
    rinci = b1 + "\n" + b2
    kotak(8, 2, 90, 14, f"Studies included, n = {n_inc}\n{rinci}", warna="#EAF2FA", tebal=False)
    panah(30, 26, 30, 16)
    simpan(fig, "F01_prisma")
    return {"diambil": diambil, "unik": unik, "x0": x0, "xj": xj, "kand": kand,
            "judul_saja": judul_saja, "xa": xa, "inc": inc}


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

    kotak(1, 33, 17, 25, "1  Acquisition", "views per plant\nordering (video or\ndiscrete views)\npose, depth,\nbaseline, sides", "#F7F7F7")
    kotak(21, 33, 17, 25, "2  Observations", "detections or\nmasks in each\nimage; one\nfruit may yield\nseveral boxes", "#F7F7F7")
    kotak(41, 33, 20, 25, "3  Association", "decide which\nobservations belong\nto the same fruit\n(mechanisms\nM0–M5 below)", "#EAF2FA")
    kotak(64, 33, 16, 25, "4  Attributes", "class label, size,\nmass assigned to\nthe unique\ninstance, not to\neach box", "#FFF4E0")
    kotak(83, 33, 16, 25, "5  Inventory", "one record per\nphysical fruit,\naggregated by\nclass, tree, row,\nor block", "#EAF7F1")
    panah(18, 45.5, 21, 45.5)
    panah(38, 45.5, 41, 45.5)
    panah(61, 45.5, 64, 45.5)
    panah(80, 45.5, 83, 45.5)

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
        judul2 = {"M0": "M0\nNo association", "M1": "M1\nStatistical\ncorrection",
                  "M2": "M2\nAppearance\nmatching", "M3": "M3\nTemporal\ntracking",
                  "M4": "M4\nGeometric or 3D\nassociation", "M5": "M5\nLearned\nassociation"}[m]
        ax.text(x + lebar / 2, y0 + 21.5, judul2, ha="center",
                va="top", fontsize=6.5, fontweight="bold", linespacing=1.15)
        ax.text(x + lebar / 2, y0 + 11.2, "Assumes:", ha="center", va="top", fontsize=6.0,
                style="italic", color="#333333")
        ax.text(x + lebar / 2, y0 + 8.4, asumsi, ha="center", va="top", fontsize=5.9,
                linespacing=1.25)
    ax.add_patch(FancyArrowPatch((51, 33), (51, 26.2), arrowstyle="-|>", mutation_scale=9,
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
    ax1.set_title("(a) Identity mechanisms by period", loc="left")

    akuisisi = Counter(r["akuisisi_manual"] for r in c1)
    nama_ak = {"V": "Video along a path", "D": "Discrete views", "S": "3D scan or point cloud",
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
                ax.text(j, i, str(v), ha="center", va="center", fontsize=5.8, zorder=4)
    ax.set_xticks(range(len(MEK)))
    ax.set_xticklabels([m for m in MEK])
    ax.set_yticks(range(len(baris)))
    lab = []
    for t in baris:
        n = sum(1 for r in c1 if ((r["tanaman"] or "crop not named").split(";")[0] if (r["tanaman"] or "crop not named").split(";")[0] in utama else "other crops") == t)
        lab.append(f"{t} ({n})")
    ax.set_yticklabels(lab)
    ax.invert_yaxis()
    ax.set_xlim(-0.6, len(MEK) - 0.4)
    ax.grid(color="#EEEEEE", linewidth=0.5, zorder=0)
    ax.set_xlabel("Identity mechanism (a study may use several)")
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
    fig, ax = plt.subplots(figsize=(4.8, 2.0))
    urut = list(kel) + ["No quantitative metric in the abstract"]
    vals = [100 * hit[k] / len(ada_abs) for k in urut]
    ax.barh(range(len(urut))[::-1], vals, color=[C["biru"], C["hijau"], C["abu"], C["abu_muda"]], height=0.6)
    for i, (k, v) in enumerate(zip(urut, vals)):
        ax.text(v + 1, len(urut) - 1 - i, f"{hit[k]} ({v:.0f}%)", va="center", fontsize=6.4)
    ax.set_yticks(range(len(urut))[::-1])
    ax.set_yticklabels(urut, fontsize=6.4)
    ax.set_xlim(0, 100)
    ax.set_xlabel(f"Multi-observation studies with an abstract (n = {len(ada_abs)}); several metric types per study allowed")
    simpan(fig, "F07_metrik")
    return hit, len(ada_abs), kelas


def main():
    mat = muat_matriks()
    p = gambar_prisma()
    gambar_tahun(mat)
    gambar_kerangka()
    per, n_per, ak = gambar_mekanisme(mat)
    gambar_peta_tanaman(mat)
    gambar_sawit(mat)
    hit, n_abs, kelas = gambar_metrik(mat)
    print("PRISMA", p)
    print("akuisisi", ak)
    print("metrik", hit, n_abs, "per-kelas", kelas)


if __name__ == "__main__":
    main()
