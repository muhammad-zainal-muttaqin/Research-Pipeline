#!/usr/bin/env python3
"""Memperkecil PDF akses terbuka sebelum disimpan di repo, lalu mengekstrak teksnya.

Gambar di dalam PDF diturunkan resolusinya (default 150 dpi, JPEG mutu 70)
dan objek yang tidak terpakai dibuang. Teks dan vektor tidak diubah. Bila
hasilnya tidak lebih kecil, berkas asli yang disalin.

Contoh:
  python3 tools/scopus/kompres_pdf.py --masuk /tmp/pdf --keluar literature/scopus-2026-09/pdf \
      --teks literature/scopus-2026-09/teks --kunci daftar_kunci.txt
"""
import argparse
import shutil
from pathlib import Path

import fitz  # PyMuPDF


def kompres(src, dst, dpi, mutu):
    doc = fitz.open(src)
    try:
        doc.rewrite_images(dpi_threshold=dpi + 10, dpi_target=dpi, quality=mutu,
                           lossy=True, lossless=True, bitonal=True, color=True,
                           gray=True)
    except Exception:
        pass
    doc.save(dst, garbage=4, deflate=True, clean=True)
    doc.close()
    if dst.stat().st_size >= src.stat().st_size:
        shutil.copyfile(src, dst)


def ekstrak_teks(src, dst):
    doc = fitz.open(src)
    teks = "\n".join(page.get_text() for page in doc)
    doc.close()
    dst.write_text(teks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--masuk", required=True)
    ap.add_argument("--keluar", required=True)
    ap.add_argument("--teks", required=True)
    ap.add_argument("--kunci", help="berkas berisi kunci yang boleh disalin, satu per baris")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--mutu", type=int, default=70)
    args = ap.parse_args()
    masuk, keluar, teks = Path(args.masuk), Path(args.keluar), Path(args.teks)
    keluar.mkdir(parents=True, exist_ok=True)
    teks.mkdir(parents=True, exist_ok=True)
    boleh = None
    if args.kunci:
        boleh = {k.strip() for k in open(args.kunci) if k.strip()}
    total_a = total_b = 0
    for src in sorted(masuk.glob("*.pdf")):
        if boleh is not None and src.stem not in boleh:
            continue
        dst = keluar / src.name
        if not dst.exists():
            try:
                kompres(src, dst, args.dpi, args.mutu)
            except Exception as exc:
                print("gagal", src.name, exc)
                continue
        t = teks / f"{src.stem}.txt"
        if not t.exists():
            try:
                ekstrak_teks(dst, t)
            except Exception as exc:
                print("teks gagal", src.name, exc)
        total_a += src.stat().st_size
        total_b += dst.stat().st_size
    print(f"asli {total_a / 1e6:.0f} MB -> repo {total_b / 1e6:.0f} MB")


if __name__ == "__main__":
    main()
