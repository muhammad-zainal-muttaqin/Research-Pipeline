# Naskah

Naskah *review* dalam format LaTeX, figur final, panduan penulisan, laporan
eksperimen, dan keluaran kompilasi (PDF dan presentasi).

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menyunting naskah kandidat aktif | [`source/main6-body.tex`](source/main6-body.tex) (driver `main6.tex`) |
| Mengompilasi naskah | `cd manuscript/source && tectonic main6.tex`, lalu pindahkan PDF ke `output/papers/` |
| Mengunduh PDF jadi | [`output/papers/main6.pdf`](output/papers/main6.pdf); bahan tambahan [`output/papers/main6-supplementary.pdf`](output/papers/main6-supplementary.pdf) (sumber `source/main6-supplementary.tex`, kompilasi dengan cara yang sama) |
| Melihat gambar `main6` | [`figures/main6/`](figures/main6/) — F01–F10 (PDF + PNG), dibuat `tools/scopus/gambar_tinjauan.py`; simulator interaktif di `figures/main6/interaktif/` |
| Melihat figur naskah 182 sumber dan laporan eksperimen | [`figures/`](figures/) — F01–F08, C01–C02, seri H/N/R yang dipakai `reports/*.tex` |
| Membaca aturan gaya `main6` | [`guides/GAYA-NASKAH-MAIN6.md`](guides/GAYA-NASKAH-MAIN6.md); dasarnya [`guides/POLA-TINJAUAN-PUSTAKA.md`](guides/POLA-TINJAUAN-PUSTAKA.md) |
| Menulis entri korpus lama | [`guides/PANDUAN-PENULISAN.md`](guides/PANDUAN-PENULISAN.md) |
| Memeriksa asal angka `main6` | [`../literature/scopus-2026-09/`](../literature/scopus-2026-09/README.md) |
| Melihat dek presentasi | [`output/presentation/`](output/presentation/) |

## Versi naskah

| Berkas | Isi | Status |
|---|---|---|
| `main6.tex` + `main6-body.tex` | *Cross-View Identity in Image-Based Fruit Counting: A Systematic Review and Design Space for Class-Wise Inventories*. 470 kajian Scopus (214 multi-pengamatan), mekanisme asosiasi M0–M5; 34 halaman, 11 seksi, 2 lampiran, 7 gambar, 6 tabel | **Kandidat aktif** |
| `main.tex` / `main-elsarticle.tex` + `evidence-body.tex` | Naskah asli 182 sumber (IEEEtran / Elsevier); PDF-nya ditautkan Ruang Baca | Stabil, jangan disunting |

`main6` memakai `references6.bib` (dibuat `tools/scopus/buat_bib.py` dari
rekaman Scopus dan metadata Crossref; memuat lebih banyak rekaman daripada
yang dikutip). Naskah 182 sumber dan laporan eksperimen memakai
`references.bib` (219 rekaman). Iterasi `main2`–`main5v3` dihapus pada 18
November 2026 dan tetap dapat dibuka di tag Git `arsip-pra-rapi-2026-11-18`.

## Isi folder

| Lokasi | Isi |
|---|---|
| `source/` | Sumber LaTeX, dua berkas BibTeX, angka naskah `main6-angka.tex` (dibuat `angka_naskah.py`), lampiran `main6-appendix-*.tex` (dibuat skrip), `experiment-ledgers.tex`, `appendix-synthesis.tex` |
| `figures/` | Gambar `main6` (`main6/`, keluaran skrip) dan figur raster naskah 182 sumber serta laporan eksperimen |
| `guides/` | `GAYA-NASKAH-MAIN6.md` (aturan gaya `main6`), `POLA-TINJAUAN-PUSTAKA.md` (pola tinjauan yang baik), `PANDUAN-PENULISAN.md` (entri korpus lama) |
| `reports/` | `reports.tex` (laporan lengkap), `reports-simple.tex` (ringkas EN), `reports-simple-id.tex` (ringkas ID) |
| `output/papers/` | PDF hasil kompilasi (artefak `.aux`/`.log` di-*ignore*) |
| `output/presentation/` | Dek presentasi PPTX |

## Catatan

- Driver (`main*.tex`) hanya memuat preambul, abstrak, dan `\input` isi; isi
  naskah disunting di berkas `*-body.tex`.
- Hanya `tectonic` yang tersedia; `latexmk` dan `pdflatex` tidak terpasang.
- `main6-angka.tex`, `main6-appendix-c1.tex`, `main6-appendix-queries.tex`, `references6.bib`, dan
  `figures/main6/F0*` adalah keluaran `tools/scopus/`; jangan disunting tangan.
  Jalankan ulang skripnya bila data korpus berubah.
- `reports.tex` dikompilasi dari folder `reports/`:
  `cd manuscript/reports && tectonic reports.tex`.
