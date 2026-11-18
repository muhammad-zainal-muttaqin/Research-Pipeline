# Measurement of tomato fruits quantity at different ripening stages based on color point cloud images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022measurement` |
| Judul asli | Measurement of tomato fruits quantity at different ripening stages based on color point cloud images |
| Penulis | Zhang, X.; others |
| Tahun | 2022 |
| Venue | Journal of South China Agricultural University |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [zhang2022measurement.pdf](../pdf/zhang2022measurement.pdf)
- DOI resmi: https://doi.org/10.7671/j.issn.1001-411x.202105021

## Gambaran Umum

Penelitian ini bertujuan mengukur jumlah buah tomat pada empat tahap kematangan di dalam rumah kaca memakai citra awan titik berwarna. Penulis menyatakan bahwa penghitungan pada dua dimensi tidak memberikan informasi jarak, sehingga tidak dapat menentukan apakah sebuah buah termasuk tanaman yang sedang dihitung. Buah yang belum matang juga berwarna mirip daun serta sering bertumpang tindih dan tertutup, yang menyulitkan pengenalan. Pendekatan yang diusulkan memakai informasi kedalaman untuk membatasi tanaman pada baris dekat, menggabungkan dua pandangan guna mengurangi efek tumpang tindih, lalu menghitung buah dan mengklasifikasikan kematangannya.

Data dikumpulkan di rumah kaca tomat Institute of Information, Jiangsu Academy of Agricultural Sciences, dengan kultivar 'Qimei' dan 'Taotai fen'. Tanaman ditanam sistem tali dengan tinggi 145-165 cm, jarak antartanaman 40 cm, dan jarak antarbaris 120 cm. Pengambilan dilakukan pada 17 Desember 2020 pukul 14.00-17.00 dan 23 Desember 2020 pukul 14.30-17.00 dalam kondisi pencahayaan berbeda, menghasilkan 252 kelompok citra. Kamera RGB-D Kinect V2.0 dipasang pada platform bergerak ROS DashGo B1 yang berhenti pada titik tetap; resolusi kamera warna 1920 × 1080 piksel dan kamera kedalaman 512 × 424 piksel.

Citra warna dan kedalaman dikalibrasi menjadi citra RGB-D, lalu diubah menjadi awan titik tiga dimensi berwarna dengan Open3D. Praproses memotong awan titik berdasarkan nilai Z untuk menyisakan tanaman baris dekat, dan filter statistik membuang titik pencilan. Dua awan titik dari dua sudut pandang didaftarkan dalam dua tahap: perakitan kasar dengan RANSAC melalui fungsi pendaftaran global Open3D (voksel 0,02; ambang jarak 0,03), lalu perakitan halus dengan ICP point-to-plane (ambang jarak 0,001). Dari 252 awan titik awal dihasilkan 246 awan titik gabungan. Anotasi memakai CloudCompare dengan dua kelas, buah tomat dan lainnya, dan rasio latih validasi 4:1.

Deteksi buah memakai PointRCNN, jaringan dua tahap berbasis PointNet++. Tahap pertama mengekstraksi ciri dan menghasilkan kandidat tiga dimensi dengan segmentasi titik depan memakai Focal Loss serta regresi kotak berbasis bin; tahap kedua menyempurnakan skor kandidat dan kotak. Pelatihan memakai transfer learning dengan 20.000 epoch, ukuran kelompok 3 per GPU, dua GPU, laju belajar awal 0,01, faktor pembagi 10, dan pengoptimal adam_onecycle, pada PyTorch 1.3.1 dan OpenPCDet 0.3.0. Kematangan ditentukan dari warna daging buah menjadi empat kelas: masak hijau, transisi, masak, dan masak penuh. Dari 320 citra sampel (80 per kelas), penulis menghitung 10 ciri warna berupa rata-rata dan varians dari lima kanal (R, G, B, S, V), lalu memilih matriks ciri yang memuat μG, σS, dan μV untuk melatih support vector machine (SVM) dengan pembagian 60% latih dan 40% uji.

Dari 246 awan titik gabungan, 196 dipakai untuk latih dan 50 untuk prediksi. Pada 50 awan titik uji, jumlah buah acuan 277, terdeteksi 268, benar 231, salah 37, dan terlewat 46, sehingga presisi 86,19% dan recall 83,39%. Pada 50 kotak hasil prediksi yang dipilih secara acak, rata-rata galat relatif titik pusat terhadap kotak anotasi adalah 36,83%. SVM menghasilkan akurasi 94,27% pada data latih dan 96,09% pada data uji; penerapan pada 50 awan titik memberi 112 buah masak hijau, 72 transisi, 55 masak, dan 29 masak penuh. Pada empat baris tanaman yang dipindai, penghitungan menghasilkan 448, 393, 294, dan 281 buah untuk keempat kelas tersebut, dengan total 1.416 buah.

Penulis tidak memuat bagian batasan tersendiri. Kendala yang disebut dalam teks adalah warna buah muda yang mirip daun, tumpang tindih dan penutupan antarbuah, latar yang kompleks, ketiadaan informasi jarak pada citra dua dimensi, serta adanya titik pencilan akibat keterbatasan ketepatan kamera kedalaman dan kondisi rumah kaca. Penulis juga menyatakan bahwa perakitan dua sudut pandang diperlukan karena satu sudut tidak cukup untuk mengatasi penutupan. Tidak ada interval kepercayaan, uji signifikansi, atau rincian awan titik yang gagal dirakit yang dilaporkan.

