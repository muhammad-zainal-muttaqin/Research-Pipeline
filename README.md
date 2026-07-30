# Research-Pipeline

Repositori ini menyatukan dua jalur riset tentang tandan buah segar kelapa sawit:

1. Tinjauan pustaka tentang YOLO, RGB-D, dan deteksi tandan.
2. Eksperimen deteksi yang menguji keputusan teknis dari tinjauan tersebut.

## Hasil yang berlaku saat ini

Hasil empat kelas yang boleh dikutip adalah **RF-DETR-L pada E-021**:
**test mAP50 0,6038** dan **mAP50-95 0,2770**. Semua pembanding E-021
dievaluasi dengan protokol `pycocotools` yang sama.

E-022 menguji depth sensor Orbbec pada dataset berbeda. Pipeline sensor dan
reproyeksi depth ke RGB telah divalidasi, tetapi **klaim peningkatan deteksi
belum sah**. Angka seed-42 dipertahankan sebagai rekam historis dan auditnya
menjelaskan mengapa angka tersebut tidak boleh dipakai sebagai hasil final.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Mengutip metrik final | [Metrik E-021](docs/experiments/METRICS.md) |
| Memeriksa koreksi E-022 | [Audit E-022](docs/experiments/AUDIT-E022.md), lalu [arsip seed-42](docs/experiments/archive/E022-seed42-awal.md) |
| Memahami seluruh eksperimen | [Pintu masuk eksperimen](docs/experiments/README.md) |
| Menjalankan ulang E-021 | [Panduan reproduksi](reproduce/experiments/REPRODUCE.md) |
| Menemukan skrip dan bukti hasil | [Peta skrip](reproduce/experiments/PETA-SKRIP.md) |
| Membaca sintesis literatur | [Sintesis lintas makalah](docs/literature/synthesis.md) |
| Menyusun naskah | [Sumber LaTeX](docs/manuscript/source/) dan [panduan naskah](docs/manuscript/guides/) |

## Struktur singkat

| Lokasi | Isi |
|---|---|
| [`docs/`](docs/) | Dokumen yang dibaca manusia: eksperimen, literatur, naskah, dan audit |
| [`evidence/`](evidence/) | Bukti mentah: hasil eksperimen, split, log, PDF sumber, ekstraksi, dan dataset lokal |
| [`reproduce/`](reproduce/) | Kode, konfigurasi, dan perintah untuk menghasilkan atau mengaudit bukti |
| [`artifacts/`](artifacts/) | Keluaran LaTeX, naskah lama, dan berkas kerja yang dipertahankan |
| [`site/`](site/) | Pembuat Ruang Baca dan pustaka kliennya |
| [`index.html`](index.html) | Ruang Baca publik hasil build, tetap di akar untuk GitHub Pages |

`evidence/datasets/` dan `evidence/literature/pdf/` adalah bahan lokal besar
yang sengaja tidak masuk Git. Struktur ini memisahkan bahan pembaca dari
bukti, tanpa mengubah isi JSON, split, log, PDF, atau dataset.

## Perintah lokal

```bash
node site/build.js --dry
node site/build.js
latexmk -pdf -outdir=artifacts/papers docs/manuscript/source/main.tex
```

Jalankan pembuat situs setelah mengubah entri literatur, sintesis, atau
laporan eksperimen. `index.html` adalah keluaran build dan tidak disunting
langsung.
