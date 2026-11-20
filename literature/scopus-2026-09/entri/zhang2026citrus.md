# Citrus instance segmentation and yield prediction based on parallel multiscale channel enhanced

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2026citrus` |
| Judul asli | Citrus instance segmentation and yield prediction based on parallel multiscale channel enhanced |
| Penulis | Zhang, Daode; Chu, Hang |
| Tahun | 2026 |
| Venue | Scientia Horticulturae |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhang2026citrus.pdf](../pdf/zhang2026citrus.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2026.114895

## Gambaran Umum

Segmentasi instans jeruk merupakan prasyarat penting bagi deteksi, pengenalan, dan estimasi hasil buah jeruk di kebun yang kompleks. Daun yang menutupi buah, buah yang saling tumpang tindih, dan perubahan cahaya menurunkan akurasi metode deteksi berbasis kotak pembatas. Kajian ini mengusulkan YOLO11n-LMPS, yaitu pengembangan dari YOLO11n-Seg, untuk segmentasi instans jeruk sekaligus estimasi hasil. Penulis menilai bahwa pendekatan kotak pembatas belum cukup menggambarkan kontur, batas antarbuah, dan area kontak antarbuah, sehingga segmentasi tingkat piksel dipandang lebih sesuai untuk pengenalan individual buah yang tumpang tindih.

Data dikumpulkan pada 12 November 2024 di Lianghu Farm, Distrik Jiangxia, Kota Wuhan, Provinsi Hubei. Citra diambil dengan kamera Canon pada jarak acak 0,5 m hingga 1,5 m, dengan arah pencahayaan belakang dan depan. Pengambilan dilakukan dari beberapa sudut di area terbuka untuk meniru lingkungan panen robot. Citra asli berukuran 4320×2880 piksel dipotong menjadi enam sub-citra, lalu melalui penyaringan kualitas sehingga diperoleh 1519 citra. Seluruh sub-citra yang berasal dari citra asli yang sama ditempatkan pada subset yang sama untuk mencegah kebocoran data. Anotasi dibuat dengan perangkat lunak LabelMe dan dikonversi ke format YOLO. Pembagian data latih, validasi, dan uji adalah 8:1:1. Jumlah buah per citra tidak disebutkan dalam bagian yang dibaca. Model dilatih selama 250 epoch dengan ukuran batch 16, weight decay 0,0005, dan laju pembelajaran 0,01.

Model dasar YOLO11n-Seg diperkuat dengan tiga modul. Modul PMCE (*Parallel Multi-scale Channel Enhancement*) menangkap fitur berbagai ukuran buah dan menekan derau latar. Modul LSEAM (*Lightweight Separated and Enhancement Attention Module*) ditempatkan dalam C2PSA untuk meningkatkan atensi dan ketahanan terhadap penutupan, dengan kompleksitas komputasi yang lebih rendah. Modul MSDA (*Multi-scale Dilated Attention*) memperluas medan reseptif dan menangkap informasi semantik global. Pada model akhir YOLO11n-LMPS, mAPmask 50 mencapai 91,6% dan mAPmask 50:95 mencapai 71,1%. Untuk deteksi, mAPbox 50 mencapai 92,1% dan mAPbox 50:95 mencapai 74,1%. Pada ablasi, YOLO11n-Seg memiliki mAPbox 50:95 sebesar 72,1%. Modul LSEAM menaikkan Pbox dari 81,7% menjadi 81,9% dan mAPbox 50 menjadi 90,4%. Penambahan MSDA menaikkan Pbox menjadi 84,4% dan mAPbox 50:95 menjadi 72,7%. Penambahan PMCE menaikkan Rbox dari 83,7% menjadi 85,0%, dan mAPbox 50:95 menjadi 74,1%. Pada segmentasi, mAPmask 50 naik dari 91,1% menjadi 91,6% dan mAPmask 50:95 naik dari 69,8% menjadi 71,1% setelah PMCE ditambahkan. Penulis menyatakan bahwa ketiga modul saling melengkapi dan model akhir menghasilkan performa tertinggi dibanding model pembanding utama.

Penulis menyatakan bahwa YOLO11n-LMPS meningkatkan akurasi deteksi dan segmentasi buah jeruk pada skenario kebun yang kompleks. Penulis juga menyatakan bahwa model ini menawarkan solusi yang andal untuk estimasi hasil. Hasil estimasi hasil dalam bentuk jumlah buah atau angka panen tidak disajikan dalam bagian abstrak dan bagian yang dibaca. Penulis menilai model ini cukup ringan untuk dipasang pada platform bergerak, tetapi kebutuhan perangkat keras pada platform tersebut tidak dirinci dalam bagian yang dibaca.

Batasan kajian yang secara eksplisit dinyatakan dalam bagian yang dibaca adalah kesulitan pada objek tertutup dan objek multiskala. Penulis juga menyebut bahwa sebagian besar citra mengalami penutupan akibat faktor eksternal. Penulis menilai bahwa penutupan berat dengan batas kontur yang tidak jelas diberi strategi abaikan (*ignore*) dan tidak dianotasi. Strategi ini mengurangi jumlah contoh untuk kasus penutupan berat. Kajian ini menggunakan satu jenis kamera dan satu lokasi kebun pada satu tanggal pengambilan citra.
