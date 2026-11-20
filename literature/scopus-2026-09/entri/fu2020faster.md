# Faster R–CNN–based apple detection in dense-foliage fruiting-wall trees using RGB and depth features for robotic harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fu2020faster` |
| Judul asli | Faster R–CNN–based apple detection in dense-foliage fruiting-wall trees using RGB and depth features for robotic harvesting |
| Penulis | Fu, Longsheng; Majeed, Yaqoob; Zhang, Xin; Karkee, Manoj; Zhang, Qin |
| Tahun | 2020 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [fu2020faster.pdf](../pdf/fu2020faster.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2020.07.007

## Gambaran Umum

Fu dkk. (2020) meneliti deteksi apel saat panen pada pohon yang tumbuh di dinding vertikal, untuk keperluan robot pemanen. Sistem memakai Faster R-CNN dengan masukan citra RGB dan depth dari sensor Kinect V2. Data yang dipakai berupa 800 citra berukuran 1920×1080 piksel dari kebun komersial dekat Prosser, Washington, yang diambil pada 2017 dan 2018. Hasil utama: AP tertinggi 0,89 dicapai dengan citra Foreground-RGB, yaitu citra yang latarnya dibuang menggunakan depth, dengan backbone VGG16. Waktu proses rata-rata 0,181 s per citra uji.

Pada tanaman dengan pohon berdinding vertikal, buah tersebar pada permukaan tajuk yang rapat. Pelepah dan daun menutupi sebagian buah, sehingga deteksi berbasis warna saja mudah keliru. Kajian ini menguji apakah informasi kedalaman dapat memisahkan buah dari latar sebelum detektor bekerja.

Depth dipakai untuk membuang piksel yang berada di luar jarak kerja buah. Citra yang tersisa, Foreground-RGB, lalu dimasukkan ke detektor. Kajian ini membandingkannya dengan Original-RGB, yaitu citra RGB tanpa penyaringan.

Detektor yang dipakai adalah Faster R-CNN. Dua backbone diuji: ZFNet dan VGG16. Setiap backbone dilatih pada Original-RGB dan pada Foreground-RGB. Data dibagi 70/15/15 untuk latih, validasi, dan uji. Dalam eksperimen subset, 560 citra latih digunakan, dan kajian ini menyebut sekitar 300 citra sebagai jumlah yang disarankan.

Metrik utama adalah Average Precision (AP). Pada Original-RGB, VGG16 mencapai AP 0,871 dan ZFNet 0,787. Dengan Foreground-RGB, VGG16 mencapai AP 0,89, yang merupakan hasil tertinggi kajian ini. Kajian ini melaporkan waktu pemrosesan per citra uji untuk masing-masing backbone.

Kajian ini mengukur kontribusi depth secara langsung dengan membandingkan dua jenis citra pada detektor yang sama. Dari sisi rekayasa, data hanya berasal dari satu kebun dan dua musim, sehingga generalisasi ke kultivar atau sistem tanam lain belum diuji.
