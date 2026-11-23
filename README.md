# Research-Pipeline

Repositori ini menyatukan dua jalur riset tentang tandan buah segar kelapa sawit:

1. Tinjauan pustaka untuk jurnal terindeks Scopus. Naskah aktif **`main6`**,
   *Cross-View Identity in Image-Based Fruit Counting: A Systematic Review and
   Design Space for Class-Wise Inventories*, memetakan 895 kajian
   (2012–2026) yang teks lengkapnya dinilai, dan mengelompokkan 248 kajian multi-pengamatan ke dalam enam
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
| Memeriksa koreksi E-022 | [Audit E-022](experiments/AUDIT-E022.md) |
| Memahami seluruh eksperimen | [Pintu masuk eksperimen](experiments/README.md) |
| Menjalankan ulang E-021 | [Panduan reproduksi](experiments/code/REPRODUCE.md) |
| Menemukan skrip dan bukti hasil | [Peta skrip](experiments/code/README.md) |
| Membaca sintesis literatur | [Sintesis lintas makalah](literature/synthesis.md) |
| Membaca naskah *review* terkini | [`main6.pdf`](manuscript/output/papers/main6.pdf), sumber [`main6-body.tex`](manuscript/source/main6-body.tex) |
| Mengerjakan verifikasi `main6` (tugas peninjau) | [Verifikasi](literature/scopus-2026-09/verifikasi/README.md), lalu [daftar tugas](literature/scopus-2026-09/verifikasi/TUGAS.md) |
| Memeriksa korpus dan protokol tinjauan `main6` | [Korpus Scopus 2026-09](literature/scopus-2026-09/README.md), [protokol](literature/scopus-2026-09/PROTOKOL.md), [kueri](literature/scopus-2026-09/QUERY.md), [788 ringkasan per kajian](literature/scopus-2026-09/entri/) |
| Membaca aturan gaya naskah `main6` | [`AGENTS.md`](AGENTS.md) §12 |
| Menyusun naskah | [README naskah](manuscript/README.md) |

## Struktur

| Lokasi | Isi |
|---|---|
| [`literature/`](literature/) | Tinjauan pustaka: korpus Scopus `main6` (`scopus-2026-09/`, termasuk 895 ringkasan per kajian di `entri/`), 182 ringkasan lama, sintesis, entri ditahan, teks terekstrak, dan PDF sumber |
| [`experiments/`](experiments/) | Eksperimen: status, log, metrik, sub-laporan, skrip (`code/`), hasil (`results/`), log training, dan split |
| [`manuscript/`](manuscript/) | Naskah: sumber LaTeX, figur, panduan penulisan, laporan, dan keluaran PDF/PPTX |
| [`pipeline/`](pipeline/) | Deliverable produksi: pipeline YOLO 4-kanal untuk kamera Orbbec Gemini |
| [`tools/`](tools/) | Skrip utilitas: pipeline korpus `main6` (`scopus/`) dan pembuat dek presentasi |
| [`site/`](site/) | Pembuat Ruang Baca (1.077 entri: 182 korpus lama + 895 entri `main6`) dan pustaka kliennya |
| [`index.html`](index.html) | Ruang Baca publik hasil build (1.077 entri), tetap di akar untuk GitHub Pages |

`literature/pdf/` dan `datasets/` adalah bahan lokal besar yang sengaja
tidak masuk Git.

## Perintah lokal

```bash
node site/build.js --dry
node site/build.js
cd manuscript/source && tectonic -Z search-path=../templates/els-cas-templates main6.tex   # latexmk tidak tersedia
```

Jalankan pembuat situs setelah mengubah entri literatur lama, entri `main6`,
sintesis, katalog PDF `main6`, atau laporan eksperimen. `index.html` adalah
keluaran build dan tidak disunting langsung.
