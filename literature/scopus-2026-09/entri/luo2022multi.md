# Multi-Class on-Tree Peach Detection Using Improved YOLOv5s and Multi-Modal Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2022multi` |
| Judul asli | Multi-Class on-Tree Peach Detection Using Improved YOLOv5s and Multi-Modal Images |
| Penulis | Luo, Q.; others |
| Tahun | 2022 |
| Venue | Smart Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple, kiwifruit, peach/nectarine |

## Tautan Akses
- PDF: [luo2022multi.pdf](../pdf/luo2022multi.pdf)
- DOI resmi: https://doi.org/10.12133/j.smartag.sa202210004

## Gambaran Umum

Deteksi buah persik yang akurat merupakan prasyarat bagi pengelolaan kebun otomatis, termasuk panen mekanis. Cahaya yang tidak merata dan oklusi oleh daun serta ranting membuat buah sulit dideteksi, terutama buah persik yang dibungkus kantong di kebun. Penelitian ini mengusulkan metode deteksi multi-kelas buah persik dengan memperbaiki YOLOv5s dan memanfaatkan data visual *multi-modal*. Tujuannya membedakan persik tanpa bungkus dan persik berbungkus pada pohon di kebun alami.

Data dikumpulkan di kebun persik di Dawei Town, Kota Hefei, Provinsi Anhui, Tiongkok, menggunakan kamera *RGB-D* Microsoft Azure Kinect. Kamera ini menghasilkan citra RGB, intensitas pantulan inframerah (IR), dan citra kedalaman (*depth*) yang bekerja berdasarkan prinsip *time of flight* (ToF). Kumpulan data memuat 4127 citra multi-modal yang sejajar piksel, dengan anotasi dua kelas, yaitu persik tanpa bungkus dan persik berbungkus. Pengambilan dilakukan pada Agustus hingga September, pukul 07.00 sampai 21.00, dalam kondisi cerah, berawan, dan malam dengan cahaya buatan. Tingkat oklusi dibagi menjadi ringan (0–30%), sedang (30–60%), dan berat (60–100%). Jarak kamera ke batang pohon berkisar 0,1 m sampai 1,5 m.

Metode yang diusulkan memodifikasi YOLOv5s versi kecil dengan *coordinate attention* untuk menangkap ketergantungan jarak jauh sepanjang satu arah spasial sambil menjaga informasi posisi di arah lainnya. Konvolusi *depthwise separable* dipakai untuk menurunkan beban komputasi. Model dilatih dengan PyTorch 1.11.0 pada satu GPU NVIDIA RTX2080Ti, dengan ukuran citra 640×640 piksel, ukuran batch delapan, dan 150 epoch. Model akhir memiliki 5,05 juta parameter.

Hasil utama menunjukkan nilai *mean average precision* (mAP) sebesar 98,6% untuk persik tanpa bungkus dan 88,9% untuk persik berbungkus, dengan masukan multi-modal dalam kondisi cahaya kompleks dan oklusi berat. Dibandingkan hanya memakai citra RGB, angka ini naik 5,3% dan 16,5%. Dibandingkan YOLOv5s, naik 2,8% dan 6,2%. Untuk persik berbungkus, mAP lebih tinggi 16,3% daripada YOLOX-Nano, 8,1% daripada PP-YOLO-Tiny, dan 4,5% daripada EfficientDet-D0. Model juga diuji pada apel Fuji dan kiwi Hayward dan memberikan hasil yang lebih baik pada tingkat berbeda dibandingkan metode pembanding. Pada perangkat seluler NVIDIA Jetson Nano, model mencapai 19 deteksi per detik dengan masukan lima kanal, sehingga dinilai mampu bekerja secara waktu nyata.

Penulis menyimpulkan bahwa kontribusi setiap modalitas pencitraan dan perbaikan pada YOLOv5s membantu hasil deteksi persik tanpa bungkus maupun berbungkus di kebun alami. Penulis memandang hasil ini sebagai dasar bagi persepsi visual sistem panen buah otomatis.
