# A lightweight SOD-YOLOv5n model-based winter jujube detection and counting method deployed on Android

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yu2024lightweight` |
| Judul asli | A lightweight SOD-YOLOv5n model-based winter jujube detection and counting method deployed on Android |
| Penulis | Yu, Chenhao; Feng, Junzhe; Zheng, Zhouzhou; Guo, Jiapan; Hu, Yaohua |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | jujube |

## Tautan Akses
- PDF: [yu2024lightweight.pdf](../pdf/yu2024lightweight.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.108701

## Gambaran Umum

Penghitungan jujube musim dingin secara manual memakan banyak tenaga dan waktu, serta rentan galat. Estimasi hasil panen memerlukan cara otomatis yang akurat. Namun, deteksi buah di kebun sulit dilakukan karena cahaya yang berubah, daun yang menutupi buah, dan buah yang saling menutupi. Model YOLO berukuran besar juga sulit dijalankan di ponsel petani. Penulis mengusulkan model *small object detection* ringan bernama SOD-YOLOv5n. Model ini dirancang untuk mendeteksi dan mencacah buah jujube secara real-time pada perangkat Android.

Data diambil di Stasiun Demonstrasi Jujube, Universitas Pertanian dan Kehutanan Barat Laut, di Kabupaten Dali, Weinan, Provinsi Shaanxi, Tiongkok. Pohon ditanam dengan jarak 2 m dalam baris dan 4 m antarbaris, dengan diameter tajuk rata-rata 2 m. Citra direkam dengan kamera *depth* Intel RealSense D435i dari jarak 50 sampai 100 cm dari buah. Pengambilan dilakukan pada tiga waktu dalam sehari, yaitu pukul 08.00 sampai 10.00, 12.00 sampai 14.00, dan 16.00 sampai 18.00, dalam berbagai kondisi cuaca. Dari pengambilan ini diperoleh 930 citra asli. Setelah augmentasi dengan pemotongan, pergeseran, perubahan kecerahan, penambahan derau, rotasi, pencerminan, dan penghapusan, jumlah citra menjadi 6.510. Data dibagi menjadi 80% untuk latih, 10% untuk validasi, dan 10% untuk uji. Penulis memberi anotasi berupa *bounding box* pada seluruh buah yang terlihat, termasuk buah yang tertutup daun atau buah lain. Pencacahan diuji pada 30 pohon jujube.

Penulis memodifikasi YOLOv5n dengan tiga cara. SPD-Conv menggantikan konvolusi bertahap dan lapisan *pooling* agar objek kecil dan citra beresolusi rendah lebih baik terdeteksi. Modul CARAFE menggantikan upsampling, sedangkan GSConv dipakai di bagian *neck* untuk memperkecil model. Dibandingkan YOLOv5n, SOD-YOLOv5n menaikkan presisi sebesar 2,40%, *recall* sebesar 1,80%, dan mAP sebesar 3,00%. Nilai RMSE dan MAPE turun masing-masing sebesar 9,11% dan 5,30%. Ukuran model adalah 3,64 MB, dan turun 16,51% setelah kuantisasi *float16*. Model terkuantisasi dipakai untuk membangun aplikasi JujubeDetector. Pada uji di kebun dengan 30 pohon, RMSE pencacahan adalah 1,45 dan R2 mencapai 0,97. Abstrak menulis RMSE sebesar 1,46. Waktu deteksi berkisar 30 ms sampai 90 ms. Dibanding YOLOv3-tiny, YOLOv4-tiny, dan YOLOv7-tiny, presisi model ini lebih tinggi masing-masing 4,18%, 5,32%, dan 1,21%. Pada empat citra uji, akurasi deteksinya 93,33%, yang tertinggi di antara model yang diuji.

Penulis menyatakan bahwa kinerja deteksi menurun pada kondisi cahaya kebun yang buruk. Dalam kondisi itu, kontras antara buah dan latar belakang berkurang sehingga bentuk buah kecil menjadi kabur. Dataset yang dipakai belum mencakup cukup banyak kondisi pencahayaan yang berbeda. Penulis merencanakan penambahan citra pada berbagai kondisi cahaya. Penulis juga berencana memasukkan citra buah pada tahap pertumbuhan yang berbeda agar pencacahan dapat dilakukan pada setiap tahap perkembangan.
