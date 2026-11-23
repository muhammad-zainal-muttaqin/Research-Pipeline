# ViT-FFrCnt: A Few-shot Fruit Counting Approach with Multiscale Vision Transformer

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `quan2023vit` |
| Judul asli | ViT-FFrCnt: A Few-shot Fruit Counting Approach with Multiscale Vision Transformer |
| Penulis | Quan, Khanh-An C.; Vuong, Huy Gia; Tran, Minh-Triet |
| Tahun | 2023 |
| Venue | 2023 International Conference on Multimedia Analysis and Pattern Recognition Mapr 2023 Proceedings |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, citrus, mango, strawberry, sweet pepper, avocado |

## Tautan Akses
- PDF: [quan2023vit.pdf](../pdf/quan2023vit.pdf)
- DOI resmi: https://doi.org/10.1109/mapr59823.2023.10289072

## Gambaran Umum

Penelitian ini bertujuan mencacah buah dari satu citra tanpa melatih detektor khusus untuk tiap jenis buah. Penulis menyebut bahwa pencacahan berbasis deteksi membutuhkan data berlabel dalam jumlah besar untuk setiap kategori buah. Detektor yang sudah dilatih juga tidak dapat menangani kategori baru tanpa pelatihan ulang. Penulis mengusulkan ViT-FFrCnt, pencacah *few-shot* (hanya memakai beberapa contoh) yang tidak bergantung pada kelas.

Data yang dipakai adalah set data DeepFruit, yaitu 535 citra dari enam kelas: mangga, paprika, stroberi, apel, alpukat, dan jeruk. Kelas *rockmelon* dikeluarkan karena kesalahan anotasi. Sensor, tempat pengambilan, dan pemberi label tidak disebut. Pembagian latih, validasi, dan uji dipakai, tetapi jumlah citra per bagian tidak disebut. Model few-shot hanya dilatih pada mangga, paprika, dan stroberi, lalu diuji pada keenam kelas. Detektor pembanding dilatih dan diuji pada semua kelas.

Metodenya memakai *Vision Transformer* (ViT, jaringan berbasis perhatian yang memotong citra menjadi petak 16 x 16) sebagai tulang punggung. Fitur dari blok 3, 6, 9, dan 12 disusun menjadi fitur multiskala. Contoh buah (*exemplar*, kotak pembatas satu buah) diubah menjadi fitur oleh jaringan konvolusi empat blok dan ditambah fitur ukuran kotak. Fitur citra dan contoh dicocokkan dengan perhatian terdeformasi multiskala. Kepala regresi menghasilkan peta kepadatan, dan jumlah buah adalah jumlah seluruh nilai peta itu.

Pada set uji DeepFruit untuk semua kelas, pendekatan ini mencapai MAE 1,13 dan RMSE 1,48. Pembanding adalah Mask R-CNN (3,15 dan 4,88), Faster R-CNN (2,80 dan 3,97), RetinaNet (2,57 dan 3,92), dan YOLOv5 (1,20 dan 1,84). Penulis menyebut perbaikan relatif 17,94% terhadap YOLOv5 pada MAE uji. Pada alpukat, kelas yang tidak ada di data latih, MAE 0,59 lebih rendah daripada semua detektor. Pada jeruk, kelas yang juga tidak dilatih, MAE 1,08 lebih tinggi daripada YOLOv5 (0,83).

Keterbatasan yang dapat diperiksa: YOLOv5 memberi MAE lebih rendah pada mangga (1,00 berbanding 1,37) dan jeruk (0,83 berbanding 1,08), sehingga klaim "terendah di semua kelas" tidak sesuai tabel. Hasil dilaporkan sebagai rerata atas contoh dari set latih, tanpa ragam antar-*seed*. Pembagian per pohon tidak disebut. Hanya satu citra per masukan, tanpa penggabungan antarpandang. Acuan hitung adalah label kotak pembatas pada citra.
