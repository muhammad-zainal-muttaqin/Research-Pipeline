#!/usr/bin/env python3
"""Membuat tabel lampiran LaTeX (matriks bukti C1) dari matriks_bukti.csv.

Kode di bukti/mekanisme_C1.txt (M0-M5, V/D/S/T/1) hanya kunci internal berkas
data. Tabel menuliskannya dengan nama, sama seperti naskah dan gambar, sehingga
pembaca tidak perlu menghafal kode. Keluaran:
manuscript/source/main6-appendix-c1.tex
"""
import csv
from pathlib import Path

from latex_teks import ke_latex  # noqa: F401  (dipakai skrip lain yang mengimpor modul ini)

ROOT = Path(__file__).resolve().parents[2]
MAT = ROOT / "literature/scopus-2026-09/topik/bukti/matriks_bukti.csv"
OUT = ROOT / "manuscript/source/main6-appendix-c1.tex"

PLAT = {"UAV": "UAV", "ground vehicle/robot": "Ground vehicle or robot", "handheld/smartphone": "Handheld",
        "fixed camera": "Fixed camera", "conveyor/lab": "Laboratory"}
AKUISISI = {"V": "Video", "D": "Discrete views", "S": "3D scan", "T": "Revisits", "1": "Single view"}
NAMA_MEK = {"M0": "No association", "M1": "Statistical correction", "M2": "Appearance matching",
            "M3": "Temporal tracking", "M4": "Geometric or 3D association", "M5": "Learned association",
            "DATA": "Dataset paper"}
NAMA_PENDEK = {"M0": "no association", "M1": "statistical", "M2": "appearance", "M3": "tracking",
               "M4": "geometric", "M5": "learned"}
TINGKAT = [("hitung", "Count"), ("identitas", "Identity"), ("deteksi", "Detection")]
DASAR = {"teks lengkap": "Full text", "abstrak": "Abstract", "judul": "Title"}
CROP_ABBR = {"peach/nectarine": "peach", "sweet pepper": "pepper", "litchi/longan": "litchi",
             "plum/apricot": "plum", "passion fruit": "passion fruit", "other berries": "berry",
             "persimmon/guava": "persimmon", "pumpkin/squash": "pumpkin", "nut crops": "nut"}


def nama_mekanisme(kode):
    """'M3+M2' -> 'Appearance + tracking'; urutan tetap M0..M5 apa pun urutan di berkas data."""
    bagian = sorted(set(kode.split("+")))
    if len(bagian) == 1:
        return NAMA_MEK.get(bagian[0], kode)
    t = " + ".join(NAMA_PENDEK[b] for b in bagian)
    return t[0].upper() + t[1:]


def sel_metrik(r):
    """Jenis metrik dari kolom tingkat_metrik (kode teks lengkap); "Not coded" bila kolom itu kosong."""
    ms = {x.strip() for x in r["tingkat_metrik"].split(";") if x.strip()}
    if not ms:
        return "Not coded"
    out = [nama for k, nama in TINGKAT if k in ms]
    return ", ".join(out).capitalize() if out else "None"


def sel_dasar(r):
    """Dasar pengodean: kolom verifikasi sumber_kode bila ada, selain itu dasar keputusan penyaringan."""
    v = (r.get("sumber_kode") or "").strip() or r.get("dasar_keputusan", "")
    return DASAR.get(v, "Abstract")


def main():
    rows = [r for r in csv.DictReader(open(MAT, encoding="utf-8")) if r["kode"] == "C1"]
    rows.sort(key=lambda r: (int(r["year"]), r["first_author"]))
    baris = []
    for r in rows:
        tan = ", ".join(CROP_ABBR.get(x, x) for x in r["tanaman"].split(";") if x).capitalize() or "Not stated"
        plat = ", ".join(PLAT[p] for p in r["platform"].split(";") if p in PLAT) or "Not stated"
        kelas = "Yes" if r["per_kelas"] == "Y" else "No"
        baris.append(f"\\citet{{{r['key']}}} & {tan} & {plat} & "
                     f"{AKUISISI.get(r['akuisisi_manual'], 'Not stated')} & {nama_mekanisme(r['mekanisme'])} & "
                     f"{kelas} & {sel_metrik(r)} & {sel_dasar(r)} \\\\")
    judul = (r"Study & Crop & Platform & Acquisition & Association mechanism & Per-class counts & "
             r"Metric types & Coded from\\")
    kepala = r"""%% Dibuat otomatis oleh tools/scopus/tabel_lampiran.py; jangan disunting manual.
\begin{footnotesize}
\setlength{\tabcolsep}{3pt}
\begin{longtable}{@{}L{3.5cm}L{1.5cm}L{1.9cm}L{1.6cm}L{3.2cm}L{1.1cm}L{1.9cm}L{1.2cm}@{}}
\caption{Detailed coding records of the %d multi-observation studies.}\label{tab:c1matrix}\\
\toprule
%s
\midrule
\endfirsthead
\toprule
%s
\midrule
\endhead
\bottomrule
\endfoot
\bottomrule
\multicolumn{8}{@{}p{\textwidth}@{}}{\rule{0pt}{2.6ex}\textit{Note:} A plus sign joins the mechanisms that a study combines. Not stated, the property was not found by the coding rules. Metric types were coded from the full text: Count, agreement between estimated and reference counts; Identity, a tracking metric such as MOTA, IDF1, HOTA, or ID switches; Detection, detection quality; None, no quantitative metric; Not coded, the metric type was not recorded during full-text coding. Coded from: the most complete source that was read when the codes were assigned. UAV, unmanned aerial vehicle.}\\
\endlastfoot
""" % (len(rows), judul, judul)
    OUT.write_text(kepala + "\n".join(baris) + "\n\\end{longtable}\n\\end{footnotesize}\n", newline="\n")
    print(len(rows), "baris ->", OUT)


if __name__ == "__main__":
    main()
