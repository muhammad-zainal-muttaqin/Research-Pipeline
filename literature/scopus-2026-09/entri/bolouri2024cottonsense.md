# CottonSense: A high-throughput field phenotyping system for cotton fruit segmentation and enumeration on edge devices

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bolouri2024cottonsense` |
| Judul asli | CottonSense: A high-throughput field phenotyping system for cotton fruit segmentation and enumeration on edge devices |
| Penulis | Bolouri, Farshad; Kocoglu, Yildirim; Lorraine B Pabuayon, Irish; Lorin Ritchie, Glen; Sari-Sarraf, Hamed |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [bolouri2024cottonsense.pdf](../pdf/bolouri2024cottonsense.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108531

## Gambaran Umum

Studi ini membangun CottonSense, sistem fenotiping berdaya hasil tinggi untuk mengsegmentasi dan menghitung buah kapas pada perangkat tepi (edge device). Penghitungan buah secara manual di lapangan terbatas pada beberapa tanaman dan rawan kesalahan, sementara sistem otomatis sebelumnya belum teruji pada kondisi lapangan agronomis sepanjang musim tanam. Kapas menghasilkan buah dalam jangka panjang dengan beberapa tahap perkembangan yang hadir bersamaan. Tujuan sistem ini adalah mengidentifikasi dan membedakan buah pada empat tahap, yakni square, flower, closed boll, dan open boll, dalam citra dua dan tiga dimensi, serta menghitungnya pada populasi tanaman yang besar dengan biaya dan daya rendah.

Pengumpulan data dilakukan dari Juli sampai November 2021 di stasiun pemuliaan BASF di Lubbock, Texas, pada lahan 128 baris × 29 kolom dengan panjang baris 7,62 m dan jarak baris 1,0 m. Dua kamera kedalaman Intel RealSense D435i dipasang pada traktor dan menghasilkan citra RGB-D serta data IMU, siang dan malam dengan pencahayaan LED. Pengolahan berjalan di NVIDIA Jetson AGX Xavier di dalam kabin traktor. Awan titik untuk setiap baris dibangun dengan RTAB-Map memakai deteksi fitur GFTT, deskriptor Rotated BRIEF, pencocokan FLANN, dan data IMU; awan dari kedua kamera digabung dengan Colored Point Cloud Registration. Segmentasi buah pada awan titik dilakukan dengan memproyeksikan piksel tersegmentasi memakai matriks kamera dari RTAB-Map, dengan kedalaman z = d(u,v), x = (u − cx)·d/fx, dan y = (v − cy)·d/fy.

Dataset dibentuk oleh lima anotator memakai MATLAB Image Labeler; batas setiap buah ditandai dengan anotasi poligon. Protokol anotasi menetapkan tahap yang lebih maju untuk buah dalam masa transisi, satu poligon untuk bagian buah yang tertutup organ lain, hanya buah dengan batas jelas yang diberi anotasi pada adegan padat, dan buah rontok di tanah tidak dihitung. Dari 344 citra yang diambil dalam rentang waktu, 281 citra menjadi data latih dan 63 citra data uji (rasio 7:3 per kelas). Jumlah instance data latih adalah 1.748 open boll, 1.508 closed boll, 636 flower, dan 1.401 square; data uji memuat 484, 644, 278, dan 595 instance. Model Mask R-CNN memakai backbone ResNet-50 dengan Feature Pyramid Network dan bobot awal dari MS COCO; ResNet-101 tidak dipilih karena keterbatasan daya komputasi Xavier. Model dioptimasi dengan TensorRT presisi FP16, yang menghasilkan kecepatan inferensi 2,4 kali lebih tinggi dengan AP yang sama.

Penghitungan memakai algoritme pelacakan turunan SORT yang dimodifikasi agar dapat menangani empat kelas. Pelacakan dimulai saat buah pertama kali terdeteksi, memakai filter Kalman untuk memprediksi posisi dan pencocokan IoU pada frame berikutnya, lalu menghitung buah bila jumlah frame berturut-turut dengan pencocokan mencapai ambang. Label akhir ditentukan oleh kelas yang paling sering muncul pada lintasan tersebut. Ambang ditetapkan 100 frame untuk penghitungan dan 300 frame untuk penghentian lintasan, berdasarkan pengamatan bahwa buah tampak sekitar 10 detik pada kecepatan traktor 0,10–0,15 m/s dan laju 30 FPS. Evaluasi penghitungan memakai 16 video tambahan dari baris lahan kering dengan populasi daun dan buah lebih rendah, sehingga memungkinkan hitungan manual, yang dikumpulkan pada 9 September sampai 12 Oktober 2022.

Hasil dinyatakan dengan AP pada IoU 0,5 untuk segmentasi dan deteksi, serta R² untuk kesepakatan hitungan. AP rata-rata sebesar 78,7% untuk segmentasi dan 78,9% untuk deteksi; AP deteksi per kelas adalah open boll 85,4%, closed boll 79,5%, flower 76,9%, dan square 74,0%. Survei terhadap 10 pakar fisiologi kapas pada 80 citra yang tidak dipakai dalam pengembangan model menunjukkan perbedaan relatif rata-rata 27% antarpakar dan R² 0,97 untuk jumlah buah total per citra serta 0,85 secara rata-rata per kelas; abstrak dan simpulan menyebut R² 0,94. Algoritme penghitungan mencapai R² rata-rata 0,93 terhadap hitungan manual, dengan rincian 0,97 untuk open boll, 0,95 closed boll, 0,93 flower, dan 0,88 square. Penulis menyatakan keterbatasan berupa ketidakpastian pada prediksi palsu: bunga yang tertinggal pada boll (bloom tag), buah yang tertutup braktea sehingga square dan closed boll sulit dibedakan, serta adegan padat yang hanya sebagian buahnya diberi anotasi. Pekerjaan berikutnya yang diusulkan adalah menambahkan penghitungan daun dan buku (node).
