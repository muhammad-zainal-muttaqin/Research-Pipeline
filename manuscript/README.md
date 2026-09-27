# Naskah

Naskah *review* dalam format LaTeX, figur final, panduan penulisan, laporan
eksperimen, dan keluaran kompilasi (PDF dan presentasi).

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menyunting naskah kandidat aktif | [`source/main5v3-body.tex`](source/main5v3-body.tex) (driver `main5v3.tex`) |
| Mengompilasi naskah | `cd manuscript/source && tectonic main5v3.tex`, lalu pindahkan PDF ke `output/papers/` |
| Mengunduh PDF jadi | [`output/papers/main5v3.pdf`](output/papers/main5v3.pdf) |
| Melihat figur final | [`figures/`](figures/) — F01–F08 (`.jpg`), C01–C02, seri H/N/R (`.png`) |
| Membaca panduan penulisan | [`guides/PANDUAN-PENULISAN.md`](guides/PANDUAN-PENULISAN.md) |
| Melihat dek presentasi | [`output/presentation/`](output/presentation/) |

## Versi naskah

| Berkas | Isi | Status |
|---|---|---|
| `main5v3.tex` + `main5v3-body.tex` | *Design-space review* dengan alur per kasus studi | **Kandidat aktif** |
| `main5v2.tex` + `main5v2-body.tex` | Versi sebelum revisi alur; ringkasan di `RINGKASAN-MAIN5V2.md` | Pembanding |
| `main5.tex` + `main5-body.tex` | Gabungan pertama aliran A+B | Baseline, jangan diubah |
| `main.tex` / `main-elsarticle.tex` + `evidence-body.tex` | Naskah asli 182 sumber (IEEEtran / Elsevier) | Stabil |
| `main2`–`main4`, `main-elsarticle3.tex` | Iterasi gabungan yang gagal | Arsip, jangan disunting |

`main5*` memakai `references3.bib` (235 rekord); naskah asli memakai
`references.bib` (219 rekord).

## Isi folder

| Lokasi | Isi |
|---|---|
| `source/` | Sumber LaTeX, dua berkas BibTeX, `experiment-ledgers.tex`, `appendix-synthesis.tex` |
| `figures/` | Figur final, brief deskripsi (`.md`), panduan pembuatan figur, `THEME.md` |
| `guides/` | Panduan penulisan, rencana situs dan tinjauan, keputusan *reframe*, terjemahan label figur |
| `reports/` | `reports.tex` (laporan lengkap), `reports-simple.tex` (ringkas EN), `reports-simple-id.tex` (ringkas ID) |
| `output/papers/` | PDF hasil kompilasi (artefak `.aux`/`.log` di-*ignore*) |
| `output/presentation/` | Dek presentasi PPTX |

## Catatan

- Driver (`main*.tex`) hanya memuat preambul, abstrak, dan `\input` isi; isi
  naskah disunting di berkas `*-body.tex`.
- Hanya `tectonic` yang tersedia; `latexmk` dan `pdflatex` tidak terpasang.
- `reports.tex` dikompilasi dari folder `reports/`:
  `cd manuscript/reports && tectonic reports.tex`.
