#!/usr/bin/env python3
"""Katalog PDF korpus main6 untuk Ruang Baca.

Menulis literature/scopus-2026-09/KATALOG-PDF.md: satu tabel per kelompok kode,
berisi kajian yang PDF-nya tersedia di literature/scopus-2026-09/pdf/. Semua
isian diambil dari topik/bukti/matriks_bukti.csv; tidak ada ringkasan yang
ditulis. Berkas keluaran dibaca site/build.js sebagai dokumen spesial.

    python3 tools/scopus/katalog_pdf.py
    node site/build.js
"""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature" / "scopus-2026-09"
MATRIKS = KORPUS / "topik" / "bukti" / "matriks_bukti.csv"
PDF_DIR = KORPUS / "pdf"
OUT = KORPUS / "KATALOG-PDF.md"

KELOMPOK = [
    ("C1", "Metode yang menggabungkan beberapa pengamatan buah yang sama"),
    ("C2", "Pencacahan atau estimasi hasil dari satu pandang"),
    ("C3", "Pencitraan TBS kelapa sawit"),
    ("C4", "Atribut kelas disertai pencacahan dari citra tunggal"),
    ("C5", "Deteksi, lokalisasi, atau pengukuran buah dengan depth, 3D, atau modalitas non-RGB"),
    ("R", "Tinjauan terdahulu"),
    ("T", "Metode yang dapat dipindahkan dari luar pertanian"),
]


def sel(t):
    """Teks aman untuk sel tabel Markdown."""
    t = re.sub(r"\s+", " ", t or "").strip()
    return re.sub(r"([|*_\[\]`])", r"\\\1", t).replace("<", "&lt;")


def ribuan(n):
    return f"{n:,}".replace(",", ".")


def main():
    with MATRIKS.open(encoding="utf-8", newline="") as f:
        matriks = list(csv.DictReader(f))
    pdf = {p.stem for p in PDF_DIR.glob("*.pdf")}
    ada = [r for r in matriks if r["key"] in pdf]
    n_kode = Counter(r["kode"] for r in matriks)
    n_pdf = Counter(r["kode"] for r in ada)

    L = []
    a = L.append
    a("# Katalog PDF Korpus main6")
    a("")
    a(f"Katalog ini memuat {ribuan(len(ada))} kajian korpus `main6` yang PDF-nya tersedia, dari "
      f"{ribuan(len(matriks))} kajian dalam peta. Kajian dikelompokkan menurut kode penyaringan dan diurutkan "
      "dari tahun terbaru. Katalog dihasilkan `tools/scopus/katalog_pdf.py` dari matriks bukti, sehingga "
      "tidak disunting dengan tangan.")
    a("")
    a("## Rekapitulasi")
    a("")
    a("| Kode | Kelompok | Kajian dalam peta | PDF tersedia |")
    a("|---|---|---|---|")
    for kode, nama in KELOMPOK:
        a(f"| {kode} | {nama} | {n_kode[kode]} | {n_pdf[kode]} |")
    a(f"| | **Jumlah** | {ribuan(len(matriks))} | {ribuan(len(ada))} |")
    a("")
    for kode, nama in KELOMPOK:
        g = sorted((r for r in ada if r["kode"] == kode),
                   key=lambda r: (-int(r["year"]), r["first_author"].lower(), r["key"]))
        a(f"## {kode}: {nama} ({len(g)})")
        a("")
        a("| Tahun | Penulis pertama | Judul | Sumber | PDF | DOI |")
        a("|---|---|---|---|---|---|")
        for r in g:
            doi = f"[DOI](https://doi.org/{r['doi']})" if r["doi"] else ""
            a(f"| {r['year']} | {sel(r['first_author'])} | {sel(r['title'])} | {sel(r['source'])} | "
              f"[PDF](pdf/{r['key']}.pdf) | {doi} |")
        a("")
    OUT.write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"{OUT.relative_to(ROOT)}: {len(ada)} kajian ber-PDF dari {len(matriks)}")
    luar = sorted(pdf - {r["key"] for r in matriks})
    if luar:
        print("PDF di luar matriks (tidak masuk katalog):", ", ".join(luar))


if __name__ == "__main__":
    main()
