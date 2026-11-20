# Single-image crowd counting via multi-column convolutional neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2016single` |
| Judul asli | Single-image crowd counting via multi-column convolutional neural network |
| Penulis | Zhang, Yingying; Zhou, Desen; Chen, Siqin; Gao, Shenghua; Ma, Yi |
| Tahun | 2016 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhang2016single.pdf](../pdf/zhang2016single.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2016.70

## Gambaran Umum

Kajian ini membahas penghitungan jumlah orang dari satu citra diam. Masalah utamanya adalah sudut pandang dan kepadatan kerumunan yang sangat bervariasi. Metode berbasis segmentasi latar depan dan deteksi individu sering gagal ketika terjadi oversi, karena banyak orang saling menutupi pada kerumunan padat. Metode berbasis regresi fitur juga bergantung pada segmentasi yang akurat, yang sulit dicapai tanpa informasi geometri adegan. Penulis karena itu menghitung jumlah orang tanpa segmentasi latar depan, dengan memperkirakan *density map* kerumunan lalu mengintegrasikannya menjadi jumlah.

Data yang digunakan adalah kumpulan citra kerumunan baru bernama Shanghaitech. Kumpulan ini berisi 1.198 citra dengan total 330.165 kepala beranotasi. Data terbagi menjadi dua bagian. Part A berisi 482 citra yang diunduh secara acak dari internet, dan sebagian besar memuat banyak orang. Part B berisi 716 citra yang diambil dari jalan-jalan padat di kawasan metropolitan Shanghai. Kepadatan kerumunan berbeda jauh antara kedua bagian tersebut. Untuk Part A, 300 citra dipakai untuk pelatihan dan 182 citra untuk pengujian. Untuk Part B, 400 citra dipakai untuk pelatihan. Penulis juga menguji model yang dilatih pada satu sumber data ke data lain melalui *transfer learning*. Penelitian ini tidak menggunakan tanaman, lokasi lapangan, atau platform pertanian.

Metode yang diusulkan memiliki tiga kolom CNN dengan ukuran filter berbeda. Setiap kolom memiliki *receptive field* besar, sedang, atau kecil. Dengan cara ini, fitur dapat menyesuaikan diri dengan variasi ukuran kepala akibat efek perspektif atau resolusi. Lapisan *fully connected* diganti dengan lapisan konvolusi 1 × 1, sehingga citra masukan boleh berukuran sembarang. Peta kepadatan yang sebenarnya dibangun dengan *geometry-adaptive kernels*, yang tidak memerlukan peta perspektif. Evaluasi memakai *mean absolute error* (MAE) dan *mean squared error* (MSE). Pada Part A, MCNN mencatat MAE 110,2 dan MSE 173,2. Metode pembanding Zhang et al. mencatat MAE 181,8 dan MSE 277,7. LBP+RR mencatat MAE 303,2 dan MSE 371,0. MCNN-CCR mencatat MAE 245,0 dan MSE 336,1. Pada Part B, MCNN mencatat MAE 26,4 dan MSE 41,3. Zhang et al. mencatat MAE 32,0 dan MSE 49,8. LBP+RR mencatat MAE 59,1 dan MSE 81,7. MCNN-CCR mencatat MAE 70,9 dan MSE 95,9. Penulis menyimpulkan bahwa MCNN mengungguli seluruh metode pembanding pada semua kumpulan data yang diuji.

Penulis menyatakan bahwa model ini dirancang untuk gambar diam dengan sudut pandang sembarang. Model tidak bergantung pada peta perspektif, tetapi tetap membutuhkan data latih beranotasi kepala dalam jumlah besar. Keterbatasan ini tercermin pada pembuatan kumpulan data baru yang harus dianotasi secara manual. Penulis juga menyebut bahwa keberhasilan transfer ke kumpulan data lain bergantung pada sumber pelatihan. Kajian ini berfokus pada manusia, sehingga penerapannya pada objek lain, termasuk buah, memerlukan pelatihan ulang dan validasi terpisah.
