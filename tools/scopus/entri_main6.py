#!/usr/bin/env python3
"""Kepala entri ringkasan korpus main6.

Setiap kajian korpus main6 yang PDF-nya tersedia memiliki satu berkas ringkasan
di literature/scopus-2026-09/entri/<kunci>.md. Isi ringkasan (mulai dari
"## Gambaran Umum") ditulis dari teks lengkap. Kepala berkas (judul, tabel
metadata, tautan akses) dihitung skrip ini dari matriks bukti dan
references6.bib, lalu menggantikan apa pun yang berada di atas
"## Gambaran Umum". Kepala tidak disunting dengan tangan.

    python3 tools/scopus/entri_main6.py            # segarkan kepala semua entri
    python3 tools/scopus/entri_main6.py --daftar   # kajian ber-PDF yang belum beringkasan
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature" / "scopus-2026-09"
MATRIKS = KORPUS / "topik" / "bukti" / "matriks_bukti.csv"
BIB = ROOT / "manuscript" / "source" / "references6.bib"
PDF_DIR = KORPUS / "pdf"
ENTRI_DIR = KORPUS / "entri"
AWAL_ISI = "## Gambaran Umum"

KELOMPOK = {
    "C1": "Gabungan beberapa pengamatan",
    "C2": "Pencacahan satu pandang",
    "C3": "Pencitraan TBS kelapa sawit",
    "C4": "Atribut kelas dan pencacahan",
    "C5": "Depth, 3D, dan non-RGB",
    "R": "Tinjauan terdahulu",
    "T": "Metode dari luar pertanian",
}


def penulis_bib():
    """Kunci -> daftar penulis dari references6.bib."""
    teks = BIB.read_text(encoding="utf-8")
    hasil = {}
    for m in re.finditer(r"^@\w+\{([^,]+),(.*?)^\}", teks, re.M | re.S):
        a = re.search(r"^\s*author\s*=\s*\{(.*)\},?\s*$", m.group(2), re.M)
        if a:
            nama = re.sub(r"[{}]", "", a.group(1))
            hasil[m.group(1)] = "; ".join(n.strip() for n in nama.split(" and "))
    return hasil


def sel(t):
    return re.sub(r"\s+", " ", t or "").strip().replace("|", "\\|")


def kepala(r, penulis):
    L = [f"# {sel(r['title'])}", "", "## Metadata Ringkas", "| Field | Nilai |", "|---|---|",
         f"| Kunci BibTeX | `{r['key']}` |",
         f"| Judul asli | {sel(r['title'])} |",
         f"| Penulis | {sel(penulis.get(r['key']) or r['first_author'])} |",
         f"| Tahun | {r['year']} |",
         f"| Venue | {sel(r['source'])} |",
         f"| Kode | {r['kode']} ({KELOMPOK[r['kode']]}) |"]
    if r["tanaman"]:
        L.append(f"| Tanaman | {sel(r['tanaman'].replace(';', ', '))} |")
    L += ["", "## Tautan Akses", f"- PDF: [{r['key']}.pdf](../pdf/{r['key']}.pdf)"]
    if r["doi"]:
        L.append(f"- DOI resmi: https://doi.org/{r['doi']}")
    L += ["", ""]
    return "\n".join(L)


def main():
    with MATRIKS.open(encoding="utf-8", newline="") as f:
        matriks = [r for r in csv.DictReader(f) if (PDF_DIR / (r["key"] + ".pdf")).exists()]
    if "--daftar" in sys.argv:
        for r in matriks:
            if not (ENTRI_DIR / (r["key"] + ".md")).exists():
                print(r["key"])
        return
    penulis = penulis_bib()
    n = 0
    for r in matriks:
        p = ENTRI_DIR / (r["key"] + ".md")
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        i = t.find(AWAL_ISI)
        if i < 0:
            print(f"tanpa '{AWAL_ISI}': {p.name}")
            continue
        p.write_text(kepala(r, penulis) + t[i:].rstrip() + "\n", encoding="utf-8", newline="\n")
        n += 1
    print(f"{n} kepala entri disegarkan dari {len(matriks)} kajian ber-PDF")


if __name__ == "__main__":
    main()
