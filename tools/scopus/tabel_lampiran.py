#!/usr/bin/env python3
"""Membuat tabel lampiran LaTeX (matriks bukti C1) dari matriks_bukti.csv.

Tabel memakai kode yang sama dengan berkas bukti/mekanisme_C1.txt sehingga
setiap sel dapat dilacak ke keputusan pengodean. Keluaran:
manuscript/source/main6-appendix-c1.tex
"""
import csv
from pathlib import Path

from latex_teks import ke_latex

ROOT = Path(__file__).resolve().parents[2]
MAT = ROOT / "literature/scopus-2026-09/topik/bukti/matriks_bukti.csv"
OUT = ROOT / "manuscript/source/main6-appendix-c1.tex"

PLAT = {"UAV": "UAV", "ground vehicle/robot": "GV", "handheld/smartphone": "HH",
        "fixed camera": "FX", "conveyor/lab": "LB"}
MET = [("count", {"MAE", "RMSE", "R2", "MAPE/rel. error", "count accuracy"}),
       ("track", {"MOTA", "IDF1", "HOTA", "ID switch"}),
       ("det", {"mAP/AP", "F1"})]
CROP_ABBR = {"peach/nectarine": "peach", "sweet pepper": "pepper", "litchi/longan": "litchi",
             "plum/apricot": "plum", "passion fruit": "passion f.", "other berries": "berry",
             "persimmon/guava": "persimmon", "pumpkin/squash": "pumpkin", "nut crops": "nut"}


def sel_metrik(r):
    if r["ada_abstrak"] != "ya":
        return "n.a."
    ms = set(r["metrik"].split(";")) if r["metrik"] else set()
    out = [nama for nama, s in MET if ms & s]
    return ", ".join(out) if out else "none"


def main():
    rows = [r for r in csv.DictReader(open(MAT)) if r["kode"] == "C1"]
    rows.sort(key=lambda r: (int(r["year"]), r["first_author"]))
    baris = []
    for r in rows:
        tan = r["tanaman"].split(";")[0] if r["tanaman"] else "--"
        tan = CROP_ABBR.get(tan, tan)
        plat = ", ".join(PLAT[p] for p in r["platform"].split(";") if p in PLAT) or "--"
        mek = r["mekanisme"].replace("DATA", "dataset")
        kelas = "yes" if r["per_kelas"] == "Y" else "--"
        penulis = ke_latex(r["first_author"].split(" ")[0].replace("&", r"\&"))
        baris.append(f"{penulis} \\cite{{{r['key']}}} & {r['year']} & {tan} & {plat} & "
                     f"{r['akuisisi_manual']} & {mek} & {kelas} & {sel_metrik(r)} \\\\")
    kepala = r"""%% Dibuat otomatis oleh tools/scopus/tabel_lampiran.py; jangan disunting manual.
\begin{footnotesize}
\setlength{\tabcolsep}{4pt}
\begin{longtable}{@{}p{3.8cm}lp{2.2cm}p{2.0cm}lp{2.6cm}lp{3.2cm}@{}}
\caption{Evidence matrix for the %d multi-observation (C1) studies. Acq.: V video along a path, D discrete views, S 3D scan, T revisits over time, 1 single view. Platform: GV ground vehicle or robot, UAV, HH handheld or smartphone, LB laboratory or conveyor, FX fixed camera (-- not stated in the abstract). Mechanisms M0--M5 as in Section~\ref{sec:framework}. Class: counts reported per class. Metrics: types reported in the abstract (count agreement, tracking or identity, detection quality); n.a. means no abstract was available.}\label{tab:c1matrix}\\
\toprule
Study & Year & Crop & Platform & Acq. & Mechanism & Class & Metrics\\
\midrule
\endfirsthead
\toprule
Study & Year & Crop & Platform & Acq. & Mechanism & Class & Metrics\\
\midrule
\endhead
\bottomrule
\endfoot
""" % len(rows)
    OUT.write_text(kepala + "\n".join(baris) + "\n\\end{longtable}\n\\end{footnotesize}\n")
    print(len(rows), "baris ->", OUT)


if __name__ == "__main__":
    main()
