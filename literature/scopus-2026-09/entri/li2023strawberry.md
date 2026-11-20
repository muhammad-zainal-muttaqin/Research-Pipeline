# Strawberry R-CNN: Recognition and counting model of strawberry based on improved faster R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2023strawberry` |
| Judul asli | Strawberry R-CNN: Recognition and counting model of strawberry based on improved faster R-CNN |
| Penulis | Li, Jiajun; Zhu, Zifeng; Liu, Hongxin; Su, Yurong; Deng, Limiao |
| Tahun | 2023 |
| Venue | Ecological Informatics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [li2023strawberry.pdf](../pdf/li2023strawberry.pdf)
- DOI resmi: https://doi.org/10.1016/j.ecoinf.2023.102210

## Gambaran Umum

Studi ini membahas penghitungan buah stroberi dari citra yang diambil dengan kamera ponsel di kebun. Masalah yang diangkat adalah deteksi dan hitung stroberi pada tingkat kematangan yang berbeda, dengan buah belum matang yang sulit dibedakan dari daun. Penulis menghitung stroberi pada setiap foto secara terpisah. Tidak ada upaya mengaitkan buah yang sama antarfoto atau antarsudut pandang.

Data yang digunakan berupa 1.514 foto smartphone berukuran 4608×3456 piksel (JPG). Foto diambil dari jarak kamera 0,2 sampai 0,3 m di kebun organik Longhu Mountain, Qingdao. Jumlah citra kemudian ditambah lewat augmentasi menjadi 9.084 citra. Pembagian data 6:2:2 dilakukan per kelompok citra, sehingga citra dari kelompok yang sama tidak muncul di data latih dan data uji sekaligus.

Model yang diusulkan adalah Faster R-CNN dengan backbone kaskade dua jaringan. Penulis mengganti RoIPooling dengan RoIAlign dan memakai interpolasi bilinear. Pada hasil deteksi, mAP tercatat 0,8733. Nilai F1 untuk stroberi belum matang tercatat 0,8447. Pada tahap penghitungan, akurasi hitung per foto untuk stroberi matang mencapai 99,1%, sedangkan untuk stroberi belum matang 73,7%. Angka 99,1% ditulis penulis sebagai "error rate", tetapi dari konteksnya itu adalah akurasi hitung, bukan tingkat galat. Penulis juga membandingkan model dengan YOLOv3, SSD, Faster R-CNN ResNet50, ResNet101, dan VGG19 (Tabel 7).

Penulis menyebut dua keterbatasan. Pertama, stroberi belum matang berwarna mirip daun dan buah yang baru tumbuh sangat kecil, sehingga akurasi hitungnya turun. Kedua, backbone kaskade menaikkan akurasi tetapi memperlambat inferensi. Penulis merencanakan kaskade yang lebih ringan untuk perangkat di kebun. Model disajikan lewat platform cloud. Data tidak diunggah dan tersedia atas permintaan.
