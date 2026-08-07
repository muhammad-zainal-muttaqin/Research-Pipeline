# Naskah

Naskah tinjauan pustaka dalam format LaTeX, tersedia dalam dua template
(IEEEtran dan Elsevier). Folder ini juga memuat figur final, panduan
penulisan, laporan eksperimen dalam format LaTeX, dan keluaran kompilasi
(PDF dan presentasi).

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Menyunting isi naskah | [`source/evidence-body.tex`](source/evidence-body.tex) — semua penyuntingan masuk ke sini |
| Mengompilasi naskah | `latexmk -pdf -outdir=manuscript/output/papers manuscript/source/main.tex` |
| Melihat figur final | [`figures/`](figures/) — F01–F08 (`.jpg`), C01–C02, H/N/R series (`.png`) |
| Membaca panduan penulisan | [`guides/PANDUAN-PENULISAN.md`](guides/PANDUAN-PENULISAN.md) |
| Mengunduh PDF jadi | [`output/papers/`](output/papers/) — `main.pdf` (IEEEtran), `main-elsarticle.pdf` (Elsevier) |
| Melihat dek presentasi | [`output/presentation/`](output/presentation/) |

## Isi folder

| Lokasi | Isi |
|---|---|
| `source/` | Sumber LaTeX: `evidence-body.tex` (isi aktif), `main.tex` (driver IEEEtran), `main-elsarticle.tex` (driver Elsevier), `references.bib` (202 rekord BibTeX), `experiment-ledgers.tex`, `appendix-synthesis.tex` |
| `figures/` | Figur final F01–F08, distribusi korpus C01–C02, seri H/N/R, brief deskripsi (`.md`), panduan pembuatan figur, `THEME.md` |
| `guides/` | Panduan penulisan, rencana situs, rencana tinjauan pustaka, keputusan reframe, terjemahan label figur |
| `reports/` | `reports.tex` (laporan lengkap), `reports-simple.tex` (ringkas EN), `reports-simple-id.tex` (ringkas ID) |
| `output/papers/` | PDF hasil kompilasi dan artefak LaTeX (`.aux`, `.bbl`, `.log`) |
| `output/presentation/` | Dek presentasi PPTX |

## Catatan

- **Jangan menyunting `main.tex` atau `main-elsarticle.tex` untuk mengubah isi.**
  Keduanya hanya driver yang `\input` berkas `evidence-body.tex`.
- `reports.tex` dikompilasi dari akar repo, bukan dari `reports/`.
  Perintah: `latexmk -pdf -outdir=manuscript/output/papers manuscript/reports/reports.tex`
