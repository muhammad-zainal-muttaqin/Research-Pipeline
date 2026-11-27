# Segmentation of Outdoor Oil Palm Fruit Images for Ripeness Detection using YOLO Algorithm and Features Thresholding

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rosbi2025segmentation` |
| Judul asli | Segmentation of Outdoor Oil Palm Fruit Images for Ripeness Detection using YOLO Algorithm and Features Thresholding |
| Penulis | Rosbi, Munirah; Omar, Zaid |
| Tahun | 2025 |
| Venue | Aip Conference Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [rosbi2025segmentation.pdf](../pdf/rosbi2025segmentation.pdf)
- DOI resmi: https://doi.org/10.1063/5.0208643

## Gambaran Umum

Kajian ini (AIP Conference Proceedings 3056, 2025) menggabungkan deteksi YOLO dan ambang warna untuk memisahkan tandan buah segar (TBS) dari latar sebelum kematangannya diklasifikasikan. Tujuannya mengurangi derau latar pada fitur warna.

Data berupa 124 citra TBS Tenera dari kebun sawit di Malaysia, separuh matang dan separuh mentah. Tahap pertama melokalisasi tandan dengan YOLOv2. Sebanyak 108 citra dilabeli kotak dan diperbanyak dengan augmentasi menjadi 432 citra latih. Tahap kedua membuang latar yang tersisa di dalam kotak dengan ambang Otsu. Kanal a\* ruang warna CIELAB membuang daun dan bagian pohon yang hijau, sedangkan kanal S ruang warna HSV membuang tanah dan pasir.

Pada 16 citra uji, IoU rerata kotak 0,77 dengan nilai tertinggi 0,91. Momen warna dari citra yang sudah disegmentasi dimasukkan ke Gaussian Naive Bayes, dengan akurasi kematangan sampai 93%.

Jumlah citra uji hanya 16. Kajian ini mengelaskan satu tandan per citra dan tidak mencacah tandan.
