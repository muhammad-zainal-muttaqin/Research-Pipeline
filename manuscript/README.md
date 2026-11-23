# Naskah

Naskah *review* dalam format LaTeX, figur final, panduan penulisan, laporan
eksperimen, dan keluaran kompilasi (PDF dan presentasi).

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menyunting naskah kandidat aktif | [Badan `main7`](source/main7-body.tex) dan [driver LaTeX](source/main7.tex) |
| Mengompilasi naskah | Dari `manuscript/source/`, jalankan `tectonic -Z search-path=../templates/els-cas-templates main7.tex`. Jalankan perintah yang sama untuk `main7-supplementary.tex`, lalu pindahkan kedua PDF ke `output/papers/` |
| Membaca hasil | [Naskah utama](output/papers/main7.pdf), [bahan tambahan](output/papers/main7-supplementary.pdf), dan [daftar kajian](output/papers/main7-supplementary-studies.csv) |
| Melihat gambar | [`figures/main6/`](figures/main6/) untuk gambar korpus, dibuat `tools/scopus/gambar_tinjauan.py`. [Figur galat inventaris `main7`](figures/main7/galat-inventaris.pdf) berupa PDF vektor, dibuat `tools/scopus/gambar_galat_inventaris.py` |
| Melihat figur naskah 182 sumber dan laporan eksperimen | [`figures/`](figures/) - F01–F08, C01–C02, seri H/N/R yang dipakai `reports/*.tex` |
| Membaca aturan gaya `main6` dan bentuk entri korpus lama | [`../AGENTS.md`](../AGENTS.md) §12 dan §14 |
| Memeriksa asal angka `main6` | [`../literature/scopus-2026-09/`](../literature/scopus-2026-09/README.md) |
| Melihat dek presentasi | [`output/presentation/`](output/presentation/) |

## Versi naskah

| Berkas | Isi | Status |
|---|---|---|
| `main7.tex` + `main7-body.tex` | Sintesis berdasarkan kondisi pengambilan citra, cara menautkan buah, dan jenis rujukan hitung. Bahan tambahan memuat metode rinci, daftar periksa PRISMA 2020, dan tabel perbandingan | **Kandidat aktif pada cabang `main7`** |
| `main6.tex` + `main6-body.tex` | Versi sebelumnya dengan korpus yang sama | Pembanding |
| `main.tex` / `main-elsarticle.tex` + `evidence-body.tex` | Naskah asli 182 sumber (IEEEtran / Elsevier); PDF-nya ditautkan Ruang Baca | Stabil, jangan disunting |

`main6` dan `main7` memakai `references6.bib` (dibuat `tools/scopus/buat_bib.py` dari
rekaman Scopus dan metadata Crossref; memuat lebih banyak rekaman daripada
yang dikutip). Naskah 182 sumber dan laporan eksperimen memakai
`references.bib` (219 rekaman). Iterasi `main2`–`main5v3` dihapus pada 18
November 2026 dan tetap dapat dibuka di tag Git `arsip-pra-rapi-2026-11-18`.

## Isi folder

| Lokasi | Isi |
|---|---|
| `source/` | Sumber LaTeX, dua berkas BibTeX, angka naskah `main6-angka.tex` (dibuat `angka_naskah.py`), lampiran `main6-appendix-*.tex` (dibuat skrip), `experiment-ledgers.tex`, `appendix-synthesis.tex` |
| `figures/` | Gambar `main6` (`main6/`, keluaran skrip) dan figur raster naskah 182 sumber serta laporan eksperimen |
| `reports/` | `reports.tex` (laporan lengkap), `reports-simple.tex` (ringkas EN), `reports-simple-id.tex` (ringkas ID) |
| `output/papers/` | PDF hasil kompilasi (artefak `.aux`/`.log` di-*ignore*) |
| `output/presentation/` | Dek presentasi PPTX |

## Catatan

- Driver (`main*.tex`) hanya memuat preambul, abstrak, dan `\input` isi; isi
  naskah disunting di berkas `*-body.tex`.
- Hanya `tectonic` yang tersedia; `latexmk` dan `pdflatex` tidak terpasang.
- `main6-angka.tex`, `main6-appendix-c1.tex`, `main6-appendix-queries.tex`, `references6.bib`, dan
  `figures/main6/F*` adalah keluaran `tools/scopus/`; jangan disunting tangan.
  Jalankan ulang skripnya bila data korpus berubah. Daftar kajian untuk
  versi `main7` dibuat dari akar repo dengan
  `python3 tools/scopus/tabel_lampiran.py --daftar-kajian main7`.
- `reports.tex` dikompilasi dari folder `reports/`:
  `cd manuscript/reports && tectonic reports.tex`.
