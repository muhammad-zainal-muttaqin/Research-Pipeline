# Ripeness Classification of Fresh Oil Palm Using Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `srithai2025ripeness` |
| Judul asli | Ripeness Classification of Fresh Oil Palm Using Deep Learning |
| Penulis | Srithai, Nathaphat; Rittireung, Krittiporn; Sungthong, Nongnoot; Srisomboon, Kanabadee; Lee, Wilaiporn; Sa-Ing, Vera |
| Tahun | 2025 |
| Venue | Proceedings Ieecon 2025 2025 13th International Electrical Engineering Congress Carbon Neutrality Challenges and Solutions Based on Sustainable Power of Nature |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [srithai2025ripeness.pdf](../pdf/srithai2025ripeness.pdf)
- DOI resmi: https://doi.org/10.1109/ieecon64081.2025.10987902

## Gambaran Umum

Kajian ini bertujuan mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit dengan pembelajaran mendalam, untuk panen dan penyortiran di pabrik. Penulis menyebut penilaian visual manual rentan galat akibat pengalaman operator, pencahayaan, dan tinggi pohon. Penulis menargetkan model yang dapat berjalan waktu nyata atau di perangkat bergerak.

Data berasal dari Science Data Bank: citra berurutan yang diambil dari video tandan sawit, 4.160 citra beresolusi 416x416 piksel, dengan enam kategori. Tabel I mencatat total 14.558 objek, tetapi tempat pengambilan, sensor, dan pemberi label tidak disebut. Penulis memakai fitur *Isolate Objects* di Roboflow untuk memotong tiap tandan menjadi citra tersendiri, lalu memilih tiga kelas: belum matang, matang, dan terlalu matang. Augmentasi mencakup pembalikan, pemotongan, rotasi, kecerahan, dan derau. Pembagian: 11.900 latih, 1.782 validasi, 975 uji dari total yang disebut 14.477 citra.

Metodenya memakai YOLOv9n, detektor satu tahap ringan (*nano*) yang memprediksi kotak pembatas dan kelas dalam satu lintasan jaringan. Bobot awal dari pralatih COCO. Penulis membandingkan dua pengoptimal (SGD dan Adam), tiga laju belajar (0,01; 0,001; 0,0001), dan ukuran *batch* 16 dan 32, selama 80 *epoch* di Google Colab dengan GPU T4. Tabel III memuat 6 konfigurasi.

Konfigurasi terbaik ialah Adam, laju belajar 0,001, *batch* 32. Hasilnya presisi 0,994, *recall* 0,996, mAP50 0,995, dan mAP50-95 0,926. Teks menyebut angka ini pada evaluasi data uji dan juga pada abstrak sebagai data latih dan validasi. Matriks konfusi uji: terlalu matang 283 dari 283 benar, matang 245 dari 246 benar (satu salah sebagai belum matang), belum matang 530 dari 530 benar.

Keterbatasan: tidak ada pembagian per pohon atau per video yang disebut, padahal citra berasal dari bingkai berurutan sehingga bingkai mirip dapat jatuh di latih dan uji. Jumlah citra uji tidak konsisten (975 di teks, 1.059 dari matriks konfusi). Hanya tiga kelas yang mudah dibedakan yang dipakai, dan kelas sulit dibuang. Tidak ada pembanding model lain walau tujuannya mencari versi YOLO terbaik. Tidak ada pencacahan.
