# Automatic visual estimation of tomato cluster maturity in plant rows

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tenorio2021automatic` |
| Judul asli | Automatic visual estimation of tomato cluster maturity in plant rows |
| Penulis | Tenorio, Gabriel Lins; Caarls, Wouter |
| Tahun | 2021 |
| Venue | Machine Vision and Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [tenorio2021automatic.pdf](../pdf/tenorio2021automatic.pdf)
- DOI resmi: https://doi.org/10.1007/s00138-021-01202-9

## Gambaran Umum

Kajian ini bertujuan mempercepat dan mempermudah evaluasi kondisi panen pada kebun tomat. Dalam praktiknya, pekerja harus mengamati dan menyentuh setiap buah untuk menilai kematangannya sebelum memutuskan panen hari ini atau besok. Proses ini memakan waktu, terutama di kebun yang luas. Pada sebagian kebun, misalnya rumah kaca gaya Belanda, tomat ceri tidak dipanen per buah melainkan per kluster, sehingga keputusan panen harus mempertimbangkan kematangan seluruh buah dalam satu kluster. Penulis mengembangkan sistem pemantauan yang hanya memerlukan kamera RGB biasa dan komputer tertanam. Sistem ini terdiri dari tiga bagian, yaitu deteksi kluster, estimasi tingkat kematangan, dan pencacahan.

Tanaman yang diteliti adalah tomat ceri pada tiga barisan tanaman di sebuah rumah kaca di Vestfold, Norwegia. Sensornya berupa kamera RGB yang terjangkau. Komputer tertanam yang digunakan adalah perangkat Intel Movidius. Citra direkam dalam bentuk video dari jarak yang relatif jauh sehingga satu bingkai memuat banyak kluster. Data dikumpulkan sendiri oleh penulis dan dibagi menjadi data latih, data validasi, dan data uji. Untuk memperoleh *ground truth* pencacahan, penulis menghitung kluster unik pada setiap video secara manual.

Sistem menggunakan dua model *Deep Learning* yang dilatih terpisah. Model pertama mendeteksi lokasi kluster tomat dengan *bounding box*. Hasil terbaik diperoleh dengan MobileNetV1 sebagai ekstraktor fitur dan pemilihan *anchor* yang sesuai, dengan *Intersection over Union* (IoU) sekitar 89 persen. Model kedua memperkirakan tingkat kematangan. Nilai *root mean square error* (RMSE) model VGG16 sebesar 0,07709, sedangkan metode pengolahan citra berbasis segmentasi menghasilkan 0,2153 dan MobileNetV1 menghasilkan 0,2522. Abstrak melaporkan RMSE 7,7 persen untuk model VGG16. Pada pencacahan, penulis membandingkan penghitungan berbasis *region of interest* dengan penghitungan yang dilengkapi *tracking*. Penghitungan berbasis *region of interest* dinilai sederhana dan cepat, tetapi presisinya terbatas. Penghitungan yang memakai pelacakan dengan informasi temporal mampu mengenali kluster yang sama lintas bingkai dan menghasilkan presisi lebih tinggi. Kombinasi model yang dilatih penuh dengan pelacakan menghasilkan pencacahan yang tepat untuk sebagian besar kluster pada beberapa tahap kematangan.

Penulis juga menguji kecepatan pemrosesan pada CPU desktop dan pada Neural Compute Stick. Hasilnya, perangkat tertanam cukup baik untuk deteksi objek, tetapi lambat untuk model gabungan. Penulis menyatakan bahwa kecepatan umum sudah memadai untuk membantu petani menilai kematangan dengan CPU biasa.

Penulis menyatakan beberapa batasan. Model regresi kematangan memiliki banyak parameter sehingga membatasi jumlah bingkai per detik, bahkan pada CPU desktop. Penghitungan berbasis *region of interest* memiliki presisi yang terbatas. Metode segmentasi kurang akurat untuk kluster yang bercampur atau masih hijau, meskipun cukup baik untuk kluster berisi tomat merah. Melatih dua model terpisah juga kurang efisien secara komputasi dibandingkan satu model yang melakukan deteksi dan regresi sekaligus. Penulis menyarankan paralelisasi beberapa Neural Compute Stick atau perangkat tertanam lain, seperti NVIDIA Jetson AGX Xavier, untuk meningkatkan kecepatan. Penulis juga menyebut bahwa GPU desktop menjadi pilihan peningkatan yang mudah jika performa lebih tinggi diperlukan.
