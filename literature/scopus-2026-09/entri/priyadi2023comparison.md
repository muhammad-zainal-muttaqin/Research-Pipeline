# Comparison of YOLOv8 and EfficientDet4 Algorithms in Detecting the Ripeness of Oil Palm Fruit Bunch

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `priyadi2023comparison` |
| Judul asli | Comparison of YOLOv8 and EfficientDet4 Algorithms in Detecting the Ripeness of Oil Palm Fruit Bunch |
| Penulis | Priyadi, Muhammad Reza Azhar; Suharjito |
| Tahun | 2023 |
| Venue | 10th International Conference on ICT for Smart Society Iciss 2023 Proceeding |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [priyadi2023comparison.pdf](../pdf/priyadi2023comparison.pdf)
- DOI resmi: https://doi.org/10.1109/iciss59129.2023.10291928

## Gambaran Umum

Kajian ini membandingkan YOLOv8s dan EfficientDet Lite 4 untuk mendeteksi kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyebut penilaian kematangan yang tidak akurat menyulitkan penentuan waktu panen dan menurunkan mutu produk. Tujuannya adalah menentukan algoritma deteksi yang paling sesuai, dengan metrik mAP, *cls_loss* (galat klasifikasi), dan *box_loss* (galat letak kotak).

Data berupa video ponsel yang menampilkan pandangan 360° buah sawit, direkam oleh pekerja di perkebunan di Kalimantan. Video diubah menjadi 8.299 citra melalui Roboflow dengan laju bingkai yang diatur. Ada enam kelas: mentah, kurang matang, matang, terlalu matang, abnormal, dan tandan kosong. Pelabelan memakai kotak pembatas dan *smart polygon*. Pembagian data 70% latih, 20% validasi, 10% uji. Augmentasi berupa rotasi dan rotasi 90 derajat menaikkan jumlah citra menjadi 19.843. Pemberi label tidak disebut.

Kedua model adalah detektor satu tahap (*one-stage*), yaitu jaringan yang memprediksi kotak dan kelas dalam satu lintasan. YOLOv8s memakai kepala deteksi tanpa jangkar (*anchor-free*). EfficientDet Lite 4 memakai tulang punggung EfficientNet dan BiFPN, jaringan yang memadukan fitur beberapa skala dua arah. Keduanya diawali bobot COCO 2017. YOLOv8s dilatih 100 *epoch*, *batch* 16, citra 640×640. EfficientDet Lite 4 dilatih 15 *epoch*, *batch* 2, citra 1024×1024. mAP50 dan mAP50-95 adalah rerata presisi pada ambang tumpang-tindih (IoU) 0,5 dan 0,5 sampai 0,95.

YOLOv8s mencapai mAP50 0,976 dan mAP50-95 0,766 pada Tabel IV, dengan 10 sampai 15 FPS dan model 21,5 MB. EfficientDet Lite 4 (format .tflite, data uji) mencapai mAP50 0,940 dan mAP50-95 0,661, dengan 1 sampai 1,5 FPS dan model 19,6 MB. Selisihnya 0,036 untuk mAP50 dan 0,105 untuk mAP50-95. *cls_loss* dan *box_loss* EfficientDet (0,1126 dan 0,0014) lebih kecil daripada YOLOv8s (0,39 dan 0,917). Abstrak menyebut peningkatan 4% dan 16%, sedangkan angka abstrak mAP50 (0,978) berbeda dari tabel (0,976).

Keterbatasan yang dapat diperiksa dari teks: bingkai berasal dari video yang sama sehingga pembagian per citra berpotensi menaruh TBS yang sama di data latih dan uji, dan pembagian per TBS tidak disebut. Kedua model dilatih dengan jumlah *epoch*, *batch*, dan ukuran citra berbeda. Perbandingan nilai *loss* antarmodel memakai fungsi galat yang berbeda sehingga tidak langsung sebanding. Hanya satu varian tiap keluarga yang diuji, dan lokasi tandan (pohon atau tanah) tidak disebut. Tidak ada pencacahan buah.
