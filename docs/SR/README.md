# Solution Report (SR) — Indeks

Satu berkas SR untuk satu **ide solusi**. Tiap SR menjawab rantai yang sama:

```
1. Masalah      apa yang ingin diselesaikan, dan kenapa itu masalah
2. Ide          gagasan solusinya, berikut rujukan korpus yang mendasarinya
3. Solusi       apa yang benar-benar dibangun/dijalankan (skrip, konfigurasi)
4. Hasil        angka apa adanya, termasuk yang tidak menyenangkan
5. Putusan      DIKONFIRMASI / DIPALSUKAN / TIDAK KONKLUSIF, plus alasan
6. Reproduksi   perintah persis untuk mengulang
```

`docs/EKSPERIMEN.md` adalah **log kronologis** semua eksperimen (E-NNN); berkas
SR di sini adalah **pandangan per-ide** yang merangkum satu atau beberapa E-NNN
menjadi satu cerita utuh dari masalah sampai putusan.

Kode ada di `/workspace/experiments/` (di luar repo).

## Daftar

| SR | Ide | Eksperimen | Putusan |
|---|---|---|---|
| [SR-001](SR-001-ambiguitas-kematangan.md) | Ukur plafon ambiguitas B2/B3 dari `class_mismatch` | E-001 | **DIPALSUKAN** |
| [SR-002](SR-002-resolusi-master-mentah.md) | Pakai master mentah 3024×4032 untuk B4 | E-002 | **TIDAK KONKLUSIF** (terblokir) |
| [SR-003](SR-003-da3-video-orbit.md) | DA3 multi-view pada video orbit | E-003, E-004 | **DIKONFIRMASI** |
| [SR-004](SR-004-da3-empat-sisi.md) | DA3 multi-view pada 4/8 sisi foto | E-005 | **DIKONFIRMASI** |
| [SR-005](SR-005-sinyal-depth-tandan.md) | Kedalaman sebagai pemisah tandan (piksel) | E-006 | **DIPALSUKAN** |
| [SR-006](SR-006-penautan-geometris.md) | Penautan tandan lintas-sisi secara geometris | E-007 | **DIPALSUKAN** |

## Ide yang belum dikerjakan

| Ide | Isi | Sumber |
|---|---|---|
| I-3 | Bangkitkan pseudo-depth untuk 3.992 gambar | entri 175/198 — **SELESAI**, aset untuk I-4/I-5 |
| I-4 | YOLO 4-kanal (early fusion) vs baseline RGB | Expandable YOLO, §174 |
| I-5 | Fusi middle/late dua cabang | Ophoff dkk., §174 |
| I-8 | Gerbang mutu depth + fallback RGB | §174, §265 |
| I-10 | Kaskade deteksi-lalu-proyeksi | §174 |
| I-11 | Analisis terstratifikasi ukuran/oklusi/iluminasi | §234–262 |

## Ide tambahan dari `docs/deep-research-report.md`

Laporan itu memuat matriks 24 ide dan menempatkan **perombakan inti detektor**
sebagai prioritas pertama — kesimpulan yang **sejalan dengan temuan eksperimen
kita sendiri**: SR-005 memalsukan depth sebagai pemisah tandan, dan E-007
menunjukkan tahap counting sudah mendekati plafonnya (koreksi k mencapai 95,57%
dengan deteksi sempurna). Karena itu sisa perbaikan harus datang dari detektor.

Ide berikut diambil dari laporan tersebut, diprioritaskan menurut kecocokannya
dengan mode kegagalan yang **sudah terukur** pada dataset ini (B4 AP50 0,354;
B4 kotak terkecil; B1 hanya 9,7% dari data).

| Ide | Isi | Kenapa relevan di sini |
|---|---|---|
| **I-12** | **Pelatihan berbasis ubin (tiling) resolusi tinggi** — potong citra jadi ubin dan latih pada skala asli, bukan memperkecil seluruh citra ke 640 | Menyerang B4 langsung: pada `imgsz=640` dari sumber 960×1280, tandan B4 tinggal segelintir piksel. **Bukan tuning** — ini regime pelatihan berbeda, dan tidak memerlukan pemetaan dataset mentah yang terblokir di SR-002 |
| **I-13** | **Loss berimbang kelas / focal** | Ketimpangan nyata: B3 51,6% vs B1 9,7%. Murah dan langsung menyasar kelas minor |
| **I-14** | **Detektor NMS-free end-to-end (RT-DETR)** sebagai pembanding | Laporan menempatkan ini prioritas 1: NMS sering jadi plafon struktural pada objek rapat/bertumpuk — persis kondisi tandan di mahkota |
| **I-15** | **Neck multiskala lebih kuat (BiFPN / Gather-and-Distribute)** | Menyasar kegagalan objek kecil, yaitu B4 |
| **I-16** | **Copy-paste / augmentasi tandan sintetis** | Memperkaya kasus ekor (B1, oklusi berat) tanpa anotasi baru |
| **I-17** | **Kalibrasi ambang per strata** (ukuran/iluminasi) | Sering memberi perbaikan deployment nyata tanpa melatih ulang |
| **I-18** | **Kepala multi-tugas** (deteksi + kematangan terpisah) | Memisahkan kegagalan geometris (A) dari fotometrik (B) di dalam arsitektur |
| **I-19** | **Kalibrasi depth metrik** (Metric3D entri 177 / ZoeDepth) | Hanya relevan bila klaim geometris/jarak dilaporkan; DA3 saat ini menghasilkan depth **relatif** (`is_metric` kosong) |

Catatan penting untuk I-14: **baseline DiB sudah memakai YOLO26**, yang menurut
rancangannya sudah end-to-end tanpa NMS. Jadi sebagian argumen "ganti ke
NMS-free" mungkin sudah terpenuhi — perlu diverifikasi sebelum ide ini
dijalankan, agar tidak mengulang sesuatu yang sudah ada.
