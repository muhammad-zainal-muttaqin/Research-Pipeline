# Key Technologies for Machine Vision for Picking Robots: Review and Benchmarking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xiao2025key` |
| Judul asli | Key Technologies for Machine Vision for Picking Robots: Review and Benchmarking |
| Penulis | Xiao, Xu; Jiang, Yiming; Wang, Yaonan |
| Tahun | 2025 |
| Venue | Machine Intelligence Research |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [xiao2025key.pdf](../pdf/xiao2025key.pdf)
- DOI resmi: https://doi.org/10.1007/s11633-024-1517-1

## Gambaran Umum

Tinjauan ini membahas sistem visi pada robot pemetik buah. Komponen yang dibahas adalah akuisisi citra, deteksi target, penentuan posisi spasial, dan pemahaman adegan. Penulis menguraikan tiga generasi metode deteksi. Generasi pertama adalah pengolahan citra digital tradisional, yaitu segmentasi berdasarkan warna, bentuk, tekstur, atau gabungan fitur. Generasi kedua adalah pembelajaran mesin, seperti K-means, *support vector machine*, dan *k-nearest neighbors*. Generasi ketiga adalah pembelajaran mendalam, seperti Faster R-CNN, SSD, dan keluarga YOLO. Setiap generasi disertai tabel yang merangkum tanaman, metode, dan hasil yang dilaporkan kajian asal. Teks lengkapnya tidak menyebut basis data, string pencarian, atau kriteria seleksi.

Tantangan yang diulang di seluruh tinjauan adalah perubahan cahaya, oklusi oleh daun dan cabang, keragaman tingkat kematangan, dan kebutuhan pemrosesan seketika. Pada metode berbasis warna, ambang segmentasi peka terhadap perubahan cahaya. Karena itu, kajian asal mencoba ruang warna lain, seperti HSI, L\*a\*b\*, dan YIQ. Pada pembelajaran mesin, parameter algoritme dan fungsi kernel harus disetel ulang bila dataset berganti. Penentuan posisi buah memakai kamera stereo, kamera RGB-D, atau LiDAR. Kamera dinilai rentan terhadap cahaya, sedangkan LiDAR dinilai mengukur ruang 3D dengan baik tetapi lemah dalam mengenali jenis objek.

Bagian akhir membahas fusi beberapa sensor, pada tingkat data dan tingkat keputusan, serta penggabungan visi dengan sistem kendali robot. Contohnya adalah end effector yang mengoreksi galat posisi dari modul visi. Penulis juga menyebut kamera berbasis peristiwa (*event-based vision*) untuk mempercepat respons sistem. Arah riset yang diusulkan adalah penyempurnaan algoritme, inovasi perangkat keras, dan penyesuaian teknologi terhadap kondisi pertanian yang berbeda.

Untuk korpus `main6`, kajian ini termasuk tinjauan terdahulu (R). Tujuannya adalah mendeteksi dan melokalisasi satu buah untuk dipetik, bukan mencacah buah unik. Kata "benchmarking" pada judul merujuk pada tabel rangkuman hasil kajian asal. Tinjauan ini tidak memuat pengujian ulang pada data yang sama.
