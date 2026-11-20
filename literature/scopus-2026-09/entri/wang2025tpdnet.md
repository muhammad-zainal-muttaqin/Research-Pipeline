# TPDNet: Triple phenotype deepen networks for monocular 3D object detection of melons and fruits in fields

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2025tpdnet` |
| Judul asli | TPDNet: Triple phenotype deepen networks for monocular 3D object detection of melons and fruits in fields |
| Penulis | Wang, Yazhou; Zhang, Tianhan; Wu, Xingcai; Li, Qinglei; Li, Yuquan; Wang, Qi |
| Tahun | 2025 |
| Venue | Plant Phenomics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | melon |

## Tautan Akses
- PDF: [wang2025tpdnet.pdf](../pdf/wang2025tpdnet.pdf)
- DOI resmi: https://doi.org/10.1016/j.plaphe.2025.100048

## Gambaran Umum

Pencacahan dan pemanenan otomatis buah di lapangan memerlukan informasi tiga dimensi, bukan hanya posisi pada bidang datar. Biaya tenaga kerja untuk panen disebut mencapai 30–50 % dari total biaya produksi, sehingga otomatisasi menjadi kebutuhan penting. Deteksi dua dimensi hanya memberikan posisi pada bidang citra. Metode *point cloud* akurat, tetapi perangkatnya mahal. Karena itu, penulis mengusulkan deteksi objek tiga dimensi *monokular*, yaitu metode yang hanya memakai satu citra RGB. Dua masalah utama diangkat penulis. Pertama, satu citra RGB tidak memberikan informasi kedalaman secara langsung. Kedua, belum ada data set tiga dimensi untuk tanaman di lapangan. Penulis membangun data set untuk *wax gourd* dan mengusulkan jaringan bernama TPDNet.

Data dikumpulkan di Guiyang, Provinsi Guizhou, Tiongkok, pada September hingga Oktober 2023. Perangkat yang dipakai adalah LiDAR *solid-state* Neuvition Titan M1-A yang memiliki kamera 2 megapiksel dengan resolusi hingga 1080p. Perangkat ini mendukung hingga 700 garis pindai dengan 1750 piksel per garis dan akurasi pengukuran 5 mm. Kamera dan LiDAR dikalibrasi terlebih dahulu untuk memperoleh matriks ekstrinsik dan intrinsik. Data set berisi 943 adegan dengan total 5313 kotak pembatas (*bounding box*) berlabel dua dimensi dan tiga dimensi. Data mencakup citra, *point cloud*, label, dan parameter perangkat. Label kedalaman diturunkan dari data LiDAR.

TPDNet terdiri atas empat komponen. Modul estimasi kedalaman dibantu label kedalaman diskret. Modul penguatan kedalaman memperbaiki representasi fitur kedalaman pada dimensi spasial dan kanal. Modul agregasi fenotipe memakai dua *cross-attention* untuk menghubungkan fitur citra dan fitur kedalaman. Modul intensifikasi fenotipe memakai *self-attention* untuk menghasilkan representasi fitur yang lebih lengkap. Model dilatih selama 300 epoch dengan Adam, ukuran *batch* 3, dan laju belajar awal 0,0001 pada GPU NVIDIA A40. Metrik utama adalah AP40. Ambang IoU ditetapkan 0,75 untuk deteksi dua dimensi dan 0,5 untuk BEV dan tiga dimensi. Hasil TPDNet mencapai AP3D 63,13 % dan APBEV 63,61 %. Dibandingkan MonoDETR, MonoDistill, dan MonoDTR, APBEV lebih tinggi 12,06 %, 8,46 %, dan 4,87 %. AP3D lebih tinggi 12,7 %, 16,89 %, dan 8,5 %. Untuk AP2D, performa antarmodel dinyatakan setara.
