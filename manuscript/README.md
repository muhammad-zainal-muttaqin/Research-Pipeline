# Naskah

Naskah *review* dalam format LaTeX, figur final, panduan penulisan, laporan
eksperimen, dan keluaran kompilasi (PDF dan presentasi).

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menyunting naskah kandidat aktif | [`source/main6-body.tex`](source/main6-body.tex) (driver `main6.tex`) |
| Mengompilasi naskah | `cd manuscript/source && tectonic main6.tex`, lalu pindahkan PDF ke `output/papers/` |
| Mengunduh PDF jadi | [`output/papers/main6.pdf`](output/papers/main6.pdf) |
| Melihat gambar `main6` | [`figures/main6/`](figures/main6/) — F01–F07 (PDF + PNG), dibuat `tools/scopus/gambar_tinjauan.py`; simulator interaktif di `figures/main6/interaktif/` |
| Melihat figur naskah lama | [`figures/`](figures/) — F01–F09 (`.jpg`/`.png`), C01–C02, seri H/N/R (`.png`) |
| Membaca panduan penulisan | [`guides/PANDUAN-PENULISAN.md`](guides/PANDUAN-PENULISAN.md) dan pola tinjauan [`guides/POLA-TINJAUAN-PUSTAKA.md`](guides/POLA-TINJAUAN-PUSTAKA.md) |
| Memeriksa asal angka `main6` | [`../literature/scopus-2026-09/`](../literature/scopus-2026-09/README.md) |
| Melihat dek presentasi | [`output/presentation/`](output/presentation/) |

## Versi naskah

| Berkas | Isi | Status |
|---|---|---|
| `main6.tex` + `main6-body.tex` | *Cross-View Identity in Image-Based Fruit Counting: A Systematic Review and Design Space for Class-Wise Inventories*. Ditulis ulang dari awal: 971 kajian Scopus, 187 kajian C1, mekanisme identitas M0–M5; 22 halaman, 12 seksi, 2 lampiran, 7 gambar | **Kandidat aktif** |
| `main5v3.tex` + `main5v3-body.tex` | *Design-space review* dengan alur per kasus studi | **Usang** (*deprecated*), arsip; jangan disunting |
| `main5v2.tex` + `main5v2-body.tex` | Versi sebelum revisi alur; ringkasan di `RINGKASAN-MAIN5V2.md` | Usang, arsip |
| `main5.tex` + `main5-body.tex` | Gabungan pertama aliran A+B | Usang, arsip baseline; jangan diubah |
| `main.tex` / `main-elsarticle.tex` + `evidence-body.tex` | Naskah asli 182 sumber (IEEEtran / Elsevier) | Stabil |
| `main2`–`main4`, `main-elsarticle3.tex` | Iterasi gabungan yang gagal | Arsip, jangan disunting |

`main6` memakai `references6.bib` (1.031 rekord, 271 dikutip), dibuat oleh
`tools/scopus/buat_bib.py` dari rekaman Scopus dan metadata Crossref.
`main5*` memakai `references3.bib` (235 rekord); naskah asli memakai
`references.bib` (219 rekord).

## Isi folder

| Lokasi | Isi |
|---|---|
| `source/` | Sumber LaTeX, tiga berkas BibTeX, lampiran `main6-appendix-*.tex` (dibuat skrip), `experiment-ledgers.tex`, `appendix-synthesis.tex` |
| `figures/` | Figur final, brief deskripsi (`.md`), panduan pembuatan figur, `THEME.md` |
| `guides/` | Panduan penulisan, rencana situs dan tinjauan, keputusan *reframe*, terjemahan label figur |
| `reports/` | `reports.tex` (laporan lengkap), `reports-simple.tex` (ringkas EN), `reports-simple-id.tex` (ringkas ID) |
| `output/papers/` | PDF hasil kompilasi (artefak `.aux`/`.log` di-*ignore*) |
| `output/presentation/` | Dek presentasi PPTX |

## Catatan

- Driver (`main*.tex`) hanya memuat preambul, abstrak, dan `\input` isi; isi
  naskah disunting di berkas `*-body.tex`.
- Hanya `tectonic` yang tersedia; `latexmk` dan `pdflatex` tidak terpasang.
- `main6-appendix-c1.tex`, `main6-appendix-queries.tex`, `references6.bib`, dan
  `figures/main6/F0*` adalah keluaran `tools/scopus/`; jangan disunting tangan.
  Jalankan ulang skripnya bila data korpus berubah.
- `reports.tex` dikompilasi dari folder `reports/`:
  `cd manuscript/reports && tectonic reports.tex`.
