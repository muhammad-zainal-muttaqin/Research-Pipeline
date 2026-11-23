# Real-time Fruit Detection Method Based on RGB-D Image Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023real` |
| Judul asli | Real-time Fruit Detection Method Based on RGB-D Image Fusion |
| Penulis | Wang, Lingjie; Zhu, Yunfeng; Gu, Siqi; Chen, Zhenyu |
| Tahun | 2023 |
| Venue | Proceedings 2023 10th International Conference on Dependable Systems and their Applications Dsa 2023 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wang2023real.pdf](../pdf/wang2023real.pdf)
- DOI resmi: https://doi.org/10.1109/dsa59317.2023.00028

## Gambaran Umum

Penelitian ini bertujuan membuat pendeteksi buah *real-time* berbasis gabungan citra warna dan kedalaman (RGB-D) untuk pemetikan otomatis dan estimasi hasil. Penulis menyebut dua masalah: lingkungan kebun yang kompleks dan ukuran model yang besar sehingga sulit berjalan pada perangkat mesin pertanian. Penulis juga menyebut bahwa pendeteksi berbasis RGB saja salah mendeteksi apel yang saling menimpa karena tidak memiliki informasi kedalaman.

Data memakai set data KFuji RGB-DS, yang direkam di kebun apel Fuji komersial di Catalonia, Spanyol, pada 25 sampai 28 September 2017. Dua kamera Microsoft Kinect v2 dipasang pada platform bergerak setinggi 1 m dan 3 m, dan perekaman dilakukan malam hari dengan lampu buatan. Set data berisi 967 citra pohon apel dengan 12.839 apel berlabel kotak pembatas. Setiap citra asli dibagi menjadi sembilan subcitra 548×373 piksel yang saling tumpang tindih. Pembagian latih, validasi, dan uji adalah 8:1:1. Pemberi label tidak disebut.

Metode terdiri atas dua pengekstrak fitur berstruktur sama (satu untuk RGB, satu untuk kedalaman), modul fusi berbasis perhatian (*attention*, pembobotan wilayah dan kanal penting), dan modul prediksi berstruktur piramida yang memakai fitur multiskala RGB dan fitur hasil fusi. Bobot spasial dari fitur RGB dikalikan ke fitur kedalaman untuk menekan derau. Kotak pembatas persegi panjang diganti lingkaran agar sesuai bentuk apel dan mengurangi parameter. Pelatihan memakai satu GPU NVIDIA GTX 1060, ukuran batch 32, dan 100 iterasi.

Pada KFuji RGB-DS, metode ini mencapai AP50 94,3%, presisi 90,2%, dan *recall* 94,0%, dengan kecepatan 41 FPS. Sebagai pembanding, YOLOv5s berbasis RGB mencapai AP50 95,2%, presisi di atas 93%, dan *recall* 94,3%, dengan 34 FPS. Fusi tingkat data menurunkan AP50 sebesar 3,5% dibandingkan FaceBoxes RGB, dan fusi tingkat keputusan menurunkan AP50 sebesar 23,0% (12 FPS). Pada FaceBoxes, kotak lingkaran memberi AP50 0,943 (kotak persegi 0,941), parameter 1,03 M (1,17 M), dan 53 FPS (50 FPS).

Keterbatasan yang dapat diperiksa: yang diukur hanya deteksi kotak, tanpa pencacahan atau estimasi hasil. Metode tidak melampaui YOLOv5s dan Faster R-CNN pada AP50 dan presisi, sehingga manfaat kedalaman tidak terbukti pada akurasi. Pembagian data dilakukan pada subcitra 8:1:1, dan penulis tidak menyebut pemisahan per pohon atau per citra asal, sehingga subcitra yang tumpang tindih dapat berada di himpunan berbeda. Kedalaman yang dipakai adalah hasil praproses gabungan kedalaman dan intensitas inframerah. Penulis mengakui kesalahan deteksi tetap terjadi bila kedalaman tidak akurat atau hilang pada area luas. Hanya satu set data apel yang diuji.
