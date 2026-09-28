# Research-Pipeline

Repositori ini menyatukan dua jalur riset tentang tandan buah segar kelapa sawit:

1. Tinjauan pustaka untuk jurnal terindeks Scopus. Naskah aktif **`main6`**,
   *Cross-View Identity in Image-Based Fruit Counting: A Systematic Review and
   Design Space for Class-Wise Inventories*, memetakan 971 kajian Scopus
   (2012–2026) dan mengelompokkan 187 kajian multi-pengamatan ke dalam enam
   mekanisme asosiasi identitas (M0–M5). Korpus lama 182 ringkasan tentang YOLO,
   RGB-D, dan deteksi tandan tetap tersedia sebagai bahan latar.
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
| Membaca naskah *review* terkini | [`main6.pdf`](manuscript/output/papers/main6.pdf), sumber [`main6-body.tex`](manuscript/source/main6-body.tex) |
| Memeriksa korpus dan protokol tinjauan `main6` | [Korpus Scopus 2026-09](literature/scopus-2026-09/README.md), [protokol](literature/scopus-2026-09/PROTOKOL.md), [kueri](literature/scopus-2026-09/QUERY.md) |
| Membaca pola penulisan tinjauan yang dipakai | [`POLA-TINJAUAN-PUSTAKA.md`](manuscript/guides/POLA-TINJAUAN-PUSTAKA.md) |
| Menyusun naskah | [README naskah](manuscript/README.md) dan [panduan naskah](manuscript/guides/) |
| Memeriksa keterlacakan klaim | [Audit](audit/) |

## Struktur

| Lokasi | Isi |
|---|---|
| [`literature/`](literature/) | Tinjauan pustaka: korpus Scopus `main6` (`scopus-2026-09/`), 182 ringkasan lama, sintesis, entri ditahan, protokol pencarian, teks terekstrak, dan PDF sumber |
| [`experiments/`](experiments/) | Eksperimen: status, log, metrik, sub-laporan, skrip (`code/`), hasil (`results/`), log training, dan split |
| [`manuscript/`](manuscript/) | Naskah: sumber LaTeX, figur, panduan penulisan, laporan, dan keluaran PDF/PPTX |
| [`pipeline/`](pipeline/) | Deliverable produksi: pipeline YOLO 4-kanal untuk kamera Orbbec Gemini |
| [`tools/`](tools/) | Skrip utilitas: pipeline korpus `main6` (`scopus/`), pembuat matriks bukti, tabel sintesis, dan presentasi |
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
cd manuscript/source && tectonic main6.tex     # latexmk tidak tersedia
```

Jalankan pembuat situs setelah mengubah entri literatur, sintesis, atau
laporan eksperimen. `index.html` adalah keluaran build dan tidak disunting
langsung.
