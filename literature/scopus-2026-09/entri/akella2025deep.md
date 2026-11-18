# Deep Learning-Based Coconut Ripeness Classification and Yield Estimation using YOLO and Kalman Filtering

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `akella2025deep` |
| Judul asli | Deep Learning-Based Coconut Ripeness Classification and Yield Estimation using YOLO and Kalman Filtering |
| Penulis | Akella, Atul; Reddy, Nalla Krishna; Mahesh, M; Veerapu, Goutham |
| Tahun | 2025 |
| Venue | 2025 International Conference on Sensors and Related Networks Sennet 2025 Special Focus on Digital Healthcare 64220 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | coconut |

## Tautan Akses
- PDF: [akella2025deep.pdf](../pdf/akella2025deep.pdf)
- DOI resmi: https://doi.org/10.1109/sennet64220.2025.11136053

## Gambaran Umum

Penelitian ini mengatasi deteksi dan klasifikasi buah kelapa menurut tahap kematangannya untuk mendukung penentuan panen, penghematan tenaga kerja, dan estimasi hasil. Penulis menyatakan bahwa kematangan memengaruhi nilai komersial, kandungan gizi, dan kesesuaian buah untuk air kelapa, santan, maupun minyak, sementara pemeriksaan manual bersifat padat karya, subjektif, dan rawan salah. Tujuan penelitian adalah membangun sistem yang mengidentifikasi kelapa pada tiga tahap kematangan, yaitu tahap 1 (mentah), tahap 2 (setengah matang), dan tahap 3 (matang), sekaligus menghitung jumlah buah secara otomatis untuk estimasi hasil.

Data berasal dari repositori sumber terbuka berupa citra kelapa resolusi tinggi yang diambil di lingkungan alami dan diberi anotasi kotak pembatas untuk lokasi serta tahap kematangan dalam format YOLO, berupa label kelas dan koordinat pusat serta lebar dan tinggi ternormalisasi. Penulis tidak menyebut jumlah citra. Pra-pemrosesan mencakup pembuangan citra duplikat dan berkualitas rendah serta pemeriksaan anotasi, diikuti augmentasi berupa rotasi, balik horizontal dan vertikal, penskalaan, pengaburan, derau Gaussian, mosaik empat citra, dan penutupan wilayah acak. Data dibagi 70% latih, 15% validasi, dan 15% uji. Tiga model dilatih: CNN buatan dengan konvolusi, *pooling*, dan lapisan penuh serta *dropout* menggunakan Adam, laju belajar 0,0001, batch 32, dan 50 epoch; YOLOv8 dengan bobot awal COCO, Adam, batch 16, 25 epoch, serta rugi CIoU dan *focal*; dan YOLOv11 yang dipadukan filter Kalman serta algoritma Hungarian, dilatih dengan SGD, laju belajar 0,001, momentum 0,9, batch 16, dan 100 epoch.

Mekanisme penghitungan memakai dua pendekatan. Metode berbasis frame menjumlahkan seluruh deteksi pada setiap frame, tetapi penulis menyatakan metode ini dapat menghitung lebih karena buah yang sama muncul di beberapa frame berurutan. Metode garis lintas menetapkan garis virtual di dalam wilayah menarik, melacak tiap buah lintas frame dengan filter Kalman, dan memakai algoritma Hungarian untuk asosiasi deteksi; sebuah buah dihitung sekali ketika lintasannya memotong garis tersebut. Penulis menyatakan cara ini mengurangi penghitungan ganda pada objek yang tumpang tindih atau saat kamera bergerak, tetapi tidak melaporkan angka akurasi penghitungan.

Hasil dihitung pada himpunan uji dengan metrik presisi, recall, mAP50, dan mAP50:95 menurut Tabel I. YOLOv8 mencatat mAP50 60,6% dan mAP50:95 44,6%; per tahap, mAP50 berturut-turut 38,8%; 74,3%; dan 68,8%, dengan mAP50:95 27,9%; 58,0%; dan 47,8%. YOLOv11 dengan filter Kalman dan Hungarian mencatat mAP50 56,9% dan mAP50:95 43%, dengan mAP50 per tahap 32,8%; 75,6%; dan 62,4%, serta kecepatan 5,0 ms per citra. CNN buatan mencapai presisi, recall, dan F1 bernilai 1,00 pada himpunan validasi untuk ketiga tahap, tanpa nilai mAP yang dilaporkan.

Batasan yang dinyatakan penulis meliputi indikasi overfitting pada CNN buatan karena keterbatasan ukuran dan keragaman data, sehingga nilai sempurna tersebut tidak dianggap sebagai kinerja umum. YOLOv11 memiliki presisi rendah pada tahap 1, dengan rugi validasi yang berfluktuasi dan pembelajaran yang kurang stabil. Penulis menyarankan perluasan data dan augmentasi lagi, terutama untuk buah tahap 1, serta pengembangan pemetaan geospasial dan model ringan untuk perangkat seluler dan tepi. Angka akurasi metode penghitungan, jumlah citra, dan rincian perangkat keras tidak dinyatakan dalam naskah.

