# Yield estimation and health assessment of temperate fruits: A modular framework

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmad2024yield` |
| Judul asli | Yield estimation and health assessment of temperate fruits: A modular framework |
| Penulis | Ahmad, Jamil; Gueaieb, Wail; El Saddik, Abdulmotaleb; De Masi, Giulia; Karray, Fakhri |
| Tahun | 2024 |
| Venue | Engineering Applications of Artificial Intelligence |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [ahmad2024yield.pdf](../pdf/ahmad2024yield.pdf)
- DOI resmi: https://doi.org/10.1016/j.engappai.2024.108871

## Gambaran Umum

Kajian ini membangun kerangka modular untuk citra UAV dan RGB yang menjalankan tiga tugas: deteksi buah, klasifikasi kesehatan buah, dan regresi jumlah buah. Detektor yang dipakai adalah YOLO-NAS. Penulis menambahkan augmentasi scale-space, dynamic upscaling (DynUp) dengan super-resolusi, dan modul kesehatan yang memakai depthwise separable convolution serta additive attention. Kesehatan buah dibedakan dalam tiga kelas: healthy, brown rot, dan shot hole. Penghitungan tidak dilakukan dengan menghitung kotak deteksi saja. Jumlah buah diperkirakan dari kepadatan buah rata-rata dan luas kanopi.

Tiga dataset publik dipilih karena nilai ekonominya dan ketersediaan datanya: Apple, Peach, dan Citrus. Pada bagian eksperimen dipakai Peach, CitDet, dan MinneApple. Peach berisi 240 citra dan 2.344 buah. MinneApple berisi sekitar 41.000 instans dalam 1.000 citra. CitDet berisi 579 citra pohon utuh. Perangkat keras yang disebut penulis adalah GPU RTX A6000 48 GB, Jetson AGX Orin 64 GB, dan Jetson Nano 4 GB.

Pada deteksi, mAP50 YOLO-NAS-S adalah 0,820 di MinneApple, 0,783 di CitDet, dan 0,762 di Peach. Augmentasi scale-space menaikkan mAP50 hingga 1,2%. Pada penghitungan, korelasi R² adalah 0,93 di Peach, 0,80 di CitDet, dan 0,76 di MinneApple. Peach memiliki mAP terendah tetapi R² tertinggi. Penulis mengaitkannya dengan oklusi yang konsisten dan kepadatan buah yang hampir seragam, sehingga akurasi per kotak dan akurasi jumlah total tidak selalu sejalan. Di Peach, YOLO-NAS-S kalah tipis dari FasterRCNN-InceptionV2 (mAP50 0,770). Di CitDet, YOLOv7 dengan tiling unggul (0,831). Di MinneApple, YOLO-NAS-S melampaui FRCNN, SOD-ResNet (0,806), dan YOLOv7.

Batas kajian ini: pembanding tidak seragam antardataset, setiap dataset memakai satu unit pengukuran penghitungan, dan belum ada uji lintas-dataset. Penulis menyebut oklusi serta generalisasi ke buah dan tanaman lain sebagai batas. Penghitungan dilakukan per citra tanpa penautan antarpandang atau deduplikasi buah yang sama dari beberapa citra. Penulis menyebut informasi temporal dan sensor tambahan sebagai pekerjaan lanjutan.
