# Tools

Skrip utilitas yang bukan bagian eksperimen maupun naskah. Dipakai untuk
menjalankan pipeline korpus `main6` dan membangun dek presentasi. Skrip
pencarian OpenAlex dan matriks bukti korpus lama dihapus pada 18 November
2026; isinya ada di tag Git `arsip-pra-rapi-2026-11-18`.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menjalankan ulang korpus dan artefak naskah `main6` | [`scopus/`](scopus/) — perintah lengkap di [`literature/scopus-2026-09/README.md`](../literature/scopus-2026-09/README.md) |
| Membuat dek presentasi PPTX | [`presentation/`](presentation/) — sudah punya README sendiri |

## Isi folder

| Berkas / folder | Isi |
|---|---|
| `scopus/` | Pipeline `main6`: `scopus_search.py` (Scopus Search API), `enrich_records.py` (abstrak dan tautan OA), `fetch_pdfs.py` + `kompres_pdf.py` (PDF akses terbuka), `kode_bukti.py` (matriks bukti), `gambar_tinjauan.py` (gambar F01–F12), `angka_naskah.py` (angka naskah), verifikasi `verifikasi_*.py`, `tabel_lampiran.py` (Lampiran A), `lampiran_kueri.py` (Lampiran B), `buat_bib.py` + `latex_teks.py` (`references6.bib`), `entri_main6.py` (kepala entri `main6`), `katalog_pdf.py` (`KATALOG-PDF.md`), `cari_halaman.py` (mencari halaman PDF yang memuat potongan teks) |
| `presentation/` | Skrip pembuat dek PPTX: `build_charts.py`, `build_deck.py`, `build_panel.py`, `chart_rgb.py`, `verify_deck.py` |
