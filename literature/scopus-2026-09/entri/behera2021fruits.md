# Fruits yield estimation using Faster R-CNN with MIoU

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `behera2021fruits` |
| Judul asli | Fruits yield estimation using Faster R-CNN with MIoU |
| Penulis | Behera, Santi Kumari; Rath, Amiya Kumar; Sethy, Prabira Kumar |
| Tahun | 2021 |
| Venue | Multimedia Tools and Applications |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [behera2021fruits.pdf](../pdf/behera2021fruits.pdf)
- DOI resmi: https://doi.org/10.1007/s11042-021-10704-7

## Gambaran Umum

Penulis membahas estimasi hasil buah dari citra tanaman di kebun. Masalah yang disebut adalah deteksi dan pencacahan buah yang sulit karena cahaya berubah, buah saling tumpang tindih, dan buah tertutup daun atau batang. Estimasi hasil sebelum panen dinilai perlu agar penyimpanan dan ekspor dapat disiapkan. Penulis mengubah *Intersection over Union* (IoU) pada *Faster R-CNN* (FR-CNN) menjadi MIoU agar buah yang tumpang tindih dan tertutup lebih mudah dideteksi.

Data berupa citra lapangan lima buah: mangga, apel, jeruk, delima, dan tomat. Citra diambil di beberapa lahan di distrik Sambalpur dan Sundargarh, Odisha, India, memakai kamera utama 64 MP ponsel Redmi Note 8 Pro, lalu diubah menjadi 800 x 600 piksel. Set latih 1.000 citra (200 per buah) dan set uji 100 citra (20 per buah). Pelabelan memakai aplikasi *Image Labeller* MATLAB 2019b. Siapa pemberi label tidak disebut. Pembagian per pohon tidak disebut.

Metode memakai FR-CNN dengan *backbone* VGG16 (jaringan pengekstrak fitur). FR-CNN terdiri dari *Region Proposal Network* (RPN), yang mengusulkan wilayah calon objek, dan detektor Fast R-CNN yang mengklasifikasi usulan dan menyesuaikan kotak. MIoU menambah IoU dengan suku yang memakai A, luas minimum yang memuat kotak prediksi P dan kotak acuan G, sehingga nilainya -1 bila P dan G tidak beririsan. Pelatihan memakai SGD, laju belajar 0,01, 50 epoch, dan ukuran *minibatch* 1.

Pada 20 citra uji per buah, koefisien korelasi (R2) hitungan model terhadap hitungan acuan untuk FR-CNN dengan MIoU adalah 0,98 (mangga), 0,92 (delima), 0,96 (tomat), 0,98 (apel), dan 0,95 (jeruk). FR-CNN asli memperoleh 0,81, 0,91, 0,89, 0,90, dan 0,92. Skor F1 rata-rata 0,9534, dengan jeruk 0,9794 dan mangga 0,9383. Pada set data ACFR, F1 apel 0,9523 dan mangga 0,9432, sedangkan pada KFuji RGB-DS F1 0,8912 untuk apel.

Keterbatasan yang dapat diperiksa dari teks: set uji hanya 20 citra per buah. Pembagian latih dan uji tidak dinyatakan per pohon atau per kebun. Hitungan acuan dibuat dari label citra; cara pembuatannya tidak dijelaskan rinci. Citra yang sama diproses sebagai pandang tunggal tanpa penautan buah antarcitra. Perbandingan dengan penelitian lain di Tabel 3 memakai data yang berbeda. Pada KFuji, hanya kanal RGB yang dipakai oleh metode ini.
