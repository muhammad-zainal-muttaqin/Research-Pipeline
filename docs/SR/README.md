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
| [SR-007](SR-007-diagnosis-b4.md) | Diagnosis penyebab kegagalan B4 | E-009, E-010 | **DIKONFIRMASI** (kontras) / **DIPALSUKAN** (kepadatan) |
| [SR-008](SR-008-kanal-tekstur.md) | Kanal tekstur sebagai modalitas keempat | E-011 | **DIKONFIRMASI** (tekstur) / **DIPALSUKAN** (penajam kontras) |
| [SR-009](SR-009-ordinalitas-kelas.md) | Kematangan itu kontinu, bukan empat kotak | E-012 | **DIKONFIRMASI** |
| [SR-010](SR-010-hambatan-klasifikasi.md) | Hambatan mAP ada di klasifikasi kematangan, bukan deteksi | E-014 | **DIKONFIRMASI** |
| [SR-011](SR-011-plafon-kematangan.md) | Plafon kematangan ~68% | E-016 | **DITARIK** (bukti cacat, lihat E-018) |
| [SR-012](SR-012-dua-tahap.md) | Detektor dua tahap (deteksi agnostik + kepala kematangan) | E-017 | **DIPALSUKAN** |

## Apa yang sudah kita pelajari — cerita singkatnya

Sembilan ide diuji; empat dipalsukan, dan justru itu yang mempersempit arah.
Rantai temuannya:

1. **Bottleneck ada di detektor, bukan penghitung.** E-007 mereproduksi Tabel 4
   DiB persis, dan menunjukkan koreksi sederhana `k = 1,8905` sudah mencapai
   95,57% bila diberi deteksi sempurna. Ruang perbaikan di tahap counting tipis.
2. **Geometri DA3 bekerja — tetapi bukan di tempat yang kita butuhkan.** DA3
   memulihkan pose 4/8 sisi dengan benar pada 50/50 pohon (SR-004) dan orbit
   video pada 5/6 video (SR-003). Namun kedalaman **tidak** memisahkan tandan
   di tingkat piksel (SR-005), dan penautan geometris **kalah** dari koreksi
   statistik (SR-006).
3. **B4 gagal karena tersamar, bukan bertumpuk.** Kontrasnya di bawah kotak
   acak, kedalamannya tidak membedakan, dan ia justru paling renggang dari
   semua kelas (SR-007). Motivasi asli jalur kedalaman — "tandan bertumpuk" —
   ternyata salah.
4. **Satu-satunya sinyal tersisa untuk B4 adalah tekstur.** Kanal Laplacian
   membalik peringkat: B4 dari kelas paling tidak terpisah menjadi paling
   terpisah (SR-008). Penajam kontras (CLAHE, unsharp) justru gagal.
5. **B2 gagal karena sebab yang sama sekali berbeda.** Kematangan itu variabel
   kontinu yang dipotong empat; kebingungan hanya terjadi antar kelas
   bersebelahan (SR-009). Metrik DiB sudah mengakui ini lewat `Class ±1 Acc`,
   tetapi pelatihan detektornya belum.

Kesimpulan operasionalnya: **B4 butuh keterlihatan (tekstur), B2 butuh
diskriminasi ordinal.** Menggabungkan keduanya sebagai "kelas sulit" akan
menyesatkan arah kerja.

## Ide yang belum dikerjakan

| Ide | Isi | Sumber |
|---|---|---|
| I-3 | Bangkitkan pseudo-depth untuk 3.992 gambar | entri 175/198 — **SELESAI**, aset untuk I-4/I-5 |
| I-4 | YOLO 4-kanal RGB+D (early fusion) vs baseline RGB | Expandable YOLO, §174 — **berjalan** |
| I-5 | Fusi middle/late dua cabang | Ophoff dkk., §174 |
| I-8 | Gerbang mutu depth + fallback RGB | §174, §265 |
| I-10 | Kaskade deteksi-lalu-proyeksi | §174 |
| **I-21** | **YOLO 4-kanal RGB+tekstur** | SR-008 — **berjalan**, dasar bukti terkuat |
| **I-22** | **Loss ordinal / kepala regresi kematangan** | SR-009 |

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
