#!/usr/bin/env python3
"""Mencari halaman PDF yang memuat suatu potongan teks.

Nomor halaman = urutan halaman berkas PDF (halaman pertama = 1), sesuai aturan
kolom `halaman` di literature/scopus-2026-09/verifikasi/KODE-ULANG.md.

  python tools/scopus/cari_halaman.py <key> "potongan teks" ["potongan lain" ...]
  python tools/scopus/cari_halaman.py <key> --halaman 5        # cetak teks halaman 5
  python tools/scopus/cari_halaman.py <key> --jumlah           # jumlah halaman

Pencocokan mengabaikan huruf besar/kecil, spasi berlebih, dan pemenggalan baris.
"""
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "literature/scopus-2026-09/pdf"


def normal(t):
    t = t.replace("­", "").replace("-\n", "")
    return re.sub(r"\s+", " ", t).lower()


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    path = PDF / f"{sys.argv[1]}.pdf"
    if not path.exists():
        sys.exit(f"PDF tidak ada: {path}")
    fitz.TOOLS.mupdf_display_errors(False)
    doc = fitz.open(path)
    if sys.argv[2] == "--jumlah":
        print(len(doc))
        return
    if sys.argv[2] == "--halaman":
        n = int(sys.argv[3])
        sys.stdout.reconfigure(encoding="utf-8")
        print(doc[n - 1].get_text())
        return
    halaman = [normal(p.get_text()) for p in doc]
    for frag in sys.argv[2:]:
        f = normal(frag)
        kena = [i + 1 for i, t in enumerate(halaman) if f in t]
        print(f"{frag[:60]!r}: halaman {kena if kena else 'tidak ditemukan'}")


if __name__ == "__main__":
    main()
