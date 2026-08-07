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
| Mengutip metrik final | [Metrik E-021](experiments/METRICS.md) |
| Memeriksa koreksi E-022 | [Audit E-022](experiments/AUDIT-E022.md), lalu [arsip seed-42](experiments/archive/E022-seed42-awal.md) |
| Memahami seluruh eksperimen | [Pintu masuk eksperimen](experiments/README.md) |
| Menjalankan ulang E-021 | [Panduan reproduksi](experiments/code/REPRODUCE.md) |
| Menemukan skrip dan bukti hasil | [Peta skrip](experiments/code/PETA-SKRIP.md) |
| Membaca sintesis literatur | [Sintesis lintas makalah](literature/synthesis.md) |
| Menyusun naskah | [Sumber LaTeX](manuscript/source/) dan [panduan naskah](manuscript/guides/) |
| Memeriksa keterlacakan klaim | [Audit](audit/) |

## Struktur

| Lokasi | Isi |
|---|---|
| [`literature/`](literature/) | Tinjauan pustaka: 182 ringkasan, sintesis, entri ditahan, protokol pencarian, teks terekstrak, dan PDF sumber |
| [`experiments/`](experiments/) | Eksperimen: status, log, metrik, sub-laporan, skrip (`code/`), hasil (`results/`), log training, dan split |
| [`manuscript/`](manuscript/) | Naskah: sumber LaTeX, figur, panduan penulisan, laporan, dan keluaran PDF/PPTX |
| [`pipeline/`](pipeline/) | Deliverable produksi: pipeline YOLO 4-kanal untuk kamera Orbbec Gemini |
| [`tools/`](tools/) | Skrip utilitas: pembuat matriks bukti, tabel sintesis, dan presentasi |
| [`audit/`](audit/) | Verifikasi lintas-topik: audit pra-submisi, register klaim, matriks bukti |
| [`legacy/`](legacy/) | Draf dan figur usang |
| [`site/`](site/) | Pembuat Ruang Baca dan pustaka kliennya |
| [`index.html`](index.html) | Ruang Baca publik hasil build, tetap di akar untuk GitHub Pages |

`literature/pdf/` dan `datasets/` adalah bahan lokal besar yang sengaja
tidak masuk Git.

## Perintah lokal

```bash
node site/build.js --dry
node site/build.js
latexmk -pdf -outdir=manuscript/output/papers manuscript/source/main.tex
```

Jalankan pembuat situs setelah mengubah entri literatur, sintesis, atau
laporan eksperimen. `index.html` adalah keluaran build dan tidak disunting
langsung.
