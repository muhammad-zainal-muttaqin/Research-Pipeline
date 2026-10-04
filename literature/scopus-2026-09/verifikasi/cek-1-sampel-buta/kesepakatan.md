# Cek 1: Kesepakatan Peninjau dan Penyaringan AI

Kesepakatan dihitung pada 4 Oktober 2026. Peninjau adalah Muhammad Zainal Muttaqin. Ukuran kesepakatan adalah kappa Cohen, κ = (*p*_o − *p*_e) / (1 − *p*_e), dengan *p*_o sebagai proporsi kesepakatan teramati dan *p*_e sebagai proporsi kesepakatan yang diharapkan terjadi secara kebetulan. Selang kepercayaan 95% ditulis dalam kurung siku dan bersifat indikatif.

## 1. Tahap judul

Sampel terdiri atas 300 judul yang ditarik secara acak dari 5.723 judul yang disaring (benih acak 20260929). Keputusan peninjau dan keputusan AI dibandingkan secara biner, yaitu lanjut ke tahap abstrak atau eksklusi.

| Ukuran | Nilai |
|---|---|
| Jumlah judul | 300 |
| Kesepakatan | 256 dari 300 (85,3%) |
| Kappa Cohen [selang kepercayaan 95%] | 0,57 [0,45; 0,69] |
| PABAK (*prevalence-adjusted bias-adjusted kappa*) | 0,71 |
| Ketidaksepakatan | 44 |

| | AI: lanjut | AI: eksklusi |
|---|---|---|
| **Peninjau: lanjut** | 43 | 25 |
| **Peninjau: eksklusi** | 19 | 213 |

**Aturan lulus.** Terdapat 5 judul yang dieksklusi AI tetapi ditandai peninjau sebagai C1 atau C3. Kelima judul itu diberi tanda pada kolom `kritis` di `ketidaksepakatan.csv`. Status lulus tahap judul ditetapkan setelah keputusan akhir atas kelima judul tersebut tersedia.

| idx | Peninjau | Judul |
|---|---|---|
| 4128 | Yes-C1 | Deep learning-based image segmentation for grape bunch detection |
| 1338 | Yes-C3 | Oil palm counting and age estimation from WorldView-3 imagery and LiDAR data using an integrated OBIA height model and regression analysis |
| 3038 | Yes-C1 | A YOLO-based citrus image recognition and harvesting system |
| 3661 | Yes-C1 | Grape Maturity Detection and Visual Pre-Positioning Based on Improved YOLOv4 |
| 3901 | Yes-C1 | Research on Spatial Positioning System of Fruits to be Picked in Field Based on Binocular Vision and SSD Model |

## 2. Tahap abstrak

Sampel terdiri atas 300 rekaman yang ditarik secara acak dari 1.143 rekaman tahap abstrak (benih acak 20261004). Peninjau menilai 165 rekaman dari sampel itu. Sebanyak 98 dari 165 rekaman tersebut termasuk subsampel acak 100 yang ditarik dari rekaman berabstrak. Keputusan AI yang dibandingkan adalah kode yang dipakai korpus saat ini.

| Perbandingan | Kesepakatan (*n* = 165) | Kappa [selang kepercayaan 95%] |
|---|---|---|
| Kode penuh (C1–C5, R, T, X-E1 sampai X-E7) | 86 dari 165 (52,1%) | 0,45 [0,36; 0,54] |
| Kode dengan semua eksklusi digabung | 87 dari 165 (52,7%) | 0,45 [0,37; 0,54] |
| Biner: masuk atau eksklusi | 139 dari 165 (84,2%) | 0,23 [−0,04; 0,50] |

Hasil pada 98 rekaman yang termasuk subsampel acak 100 adalah sebagai berikut.

| Perbandingan | Kesepakatan (*n* = 98) | Kappa [selang kepercayaan 95%] |
|---|---|---|
| Kode penuh | 56 dari 98 (57,1%) | 0,51 [0,39; 0,62] |
| Biner: masuk atau eksklusi | 80 dari 98 (81,6%) | 0,20 [−0,13; 0,54] |

Matriks berikut memuat sebaran kode untuk 165 rekaman. Baris menyatakan kode peninjau, kolom menyatakan kode AI, dan semua kode eksklusi digabung sebagai X. Tanda titik tengah (·) berarti nol.

| | C1 | C2 | C3 | C4 | C5 | R | T | X | Jumlah |
|---|---|---|---|---|---|---|---|---|---|
| **C1** | 12 | 2 | · | · | · | · | · | · | 14 |
| **C2** | 3 | 14 | · | 1 | 2 | · | · | 2 | 22 |
| **C3** | · | · | 25 | · | · | 2 | · | · | 27 |
| **C4** | 3 | 3 | · | · | · | · | · | 6 | 12 |
| **C5** | 9 | 1 | · | 1 | 14 | 3 | · | · | 28 |
| **R** | 7 | 3 | 2 | 2 | 1 | 13 | 4 | · | 32 |
| **T** | · | 1 | 1 | · | · | 1 | 3 | · | 6 |
| **X** | 3 | 7 | · | · | 2 | 3 | 3 | 6 | 24 |
| **Jumlah** | 37 | 31 | 28 | 4 | 19 | 22 | 10 | 14 | 165 |

**Aturan lulus.** Tidak terdapat rekaman yang dieksklusi AI tetapi dinilai peninjau sebagai C1 atau C3.

## 3. Berkas

| Berkas | Isi |
|---|---|
| `sampel_judul.csv` | Keputusan peninjau dan keputusan AI untuk 300 judul, dengan kolom `keputusan_final_fatma` |
| `sampel_abstrak.csv` | Keputusan peninjau dan keputusan AI untuk 165 rekaman tahap abstrak, dengan kolom `keputusan_final_fatma` |
| `sampel_judul_manusia.xlsx` | Lembar isian asli peninjau untuk tahap judul |
| `ketidaksepakatan.csv` | Semua rekaman yang keputusannya berbeda, dengan kolom `keputusan_final_fatma` dan `alasan_fatma` |
| `../log_perubahan.csv` | Koreksi isian peninjau |
