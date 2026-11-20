# YOLO-PDGT: A lightweight and efficient algorithm for unripe pomegranate detection and counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fan2025yolo` |
| Judul asli | YOLO-PDGT: A lightweight and efficient algorithm for unripe pomegranate detection and counting |
| Penulis | Fan, Zihan; Lu, Dingze; Liu, Man; Liu, Zishen; Dong, Qi; Zou, Huiqi; Hao, Hongjuan; Su, Yaoheng |
| Tahun | 2025 |
| Venue | Measurement Journal of the International Measurement Confederation |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | pomegranate |

## Tautan Akses
- PDF: [fan2025yolo.pdf](../pdf/fan2025yolo.pdf)
- DOI resmi: https://doi.org/10.1016/j.measurement.2025.117852

## Gambaran Umum

Pencacahan buah delima muda penting untuk memperkirakan hasil panen dan merencanakan pengelolaan kebun. Saat ini pemantauan dan pencacahan masih dilakukan secara manual. Cara ini tidak efisien dan kurang akurat karena kelelahan dan kehilangan konsentrasi pekerja. Otomatisasi menjadi kebutuhan, tetapi model deteksi berbasis *deep learning* sering sulit menjaga kecepatan dan akurasi secara bersamaan. Warna buah yang mirip dengan latar, oklusi oleh cabang dan daun, serta ukuran buah yang kecil menambah kesulitan. Penelitian ini bertujuan membangun model ringan dan cepat untuk pemantauan real-time di kebun delima.

Data terdiri atas 1.387 citra delima awal yang diambil di Lintong Pomegranate Industrial Park, Xi'an, Provinsi Shaanxi, Tiongkok. Peneliti terutama memakai ponsel pintar pada jarak kerja sekitar 1,5 m, dan menambahkan citra dari jarak dekat dan jauh. Pengambilan gambar dilakukan dari pukul 10.00 hingga 20.00 dalam kondisi cahaya dan cuaca yang beragam. Anotasi dibuat dengan Labelme sebagai *bounding box*. Setelah augmentasi, jumlah citra menjadi 2.774 dengan 29.300 target. Sebanyak 21.513 target (73,4 %) tergolong kecil, yaitu kurang dari 0,5 % luas citra. Data dibagi secara acak dengan perbandingan 7:3 untuk pelatihan dan validasi. Augmentasi meliputi peningkatan kecerahan menjadi 1,3 kali dan *cutout* acak pada 50 area per citra.

Model YOLO-PDGT mengurangi jumlah kanal pada Neck, mengganti modul C2f dengan modul PDWC, dan memakai DWSConv serta GhostConv untuk *downsampling*. Triplet Attention ditambahkan untuk memperbaiki deteksi objek kecil. Ukuran model menyusut sekitar 82,3 %, sedangkan FPS naik 67,64 %. Nilai mAP@0,5 naik 0,2 % dibanding baseline. Hasil lengkap model adalah presisi 93,4 %, recall 92,6 %, mAP@0,5 97,2 %, dan F1 92,9 %. Pada 600 citra validasi yang memuat 9.306 kotak acuan, mAP untuk objek kecil mencapai 96,1 %, naik 0,7 % dari YOLOv8s. Pada pencacahan 200 citra validasi, R2 mencapai 0,96, lebih tinggi 0,1 dari baseline, dan RMSE lebih rendah 0,11. Uji t berpasangan untuk selisih FPS menghasilkan p = 0,000012. Model tetap mengenali buah dengan oklusi lebih dari 80 %, tetapi tingkat kepercayaannya turun pada kondisi cahaya rendah.

Penulis mengakui bahwa penurunan akurasi akibat pemampatan model dikompensasi oleh dua modul Triplet Attention. Dibanding Model 3, mekanisme ini menaikkan mAP@0,5 sebesar 1,1 % dan F1 sebesar 1,6 %. Penulis juga menyatakan bahwa metode *downsampling* yang spesifik untuk tugas ini dapat membatasi generalisasi. Model belum diuji penerapannya di lingkungan nyata karena keterbatasan kondisi eksperimen dan lama pertumbuhan delima. Rencana berikutnya adalah mengembangkan metode optimasi yang lebih kompatibel dan menerapkannya pada robot atau perangkat seluler untuk deteksi dinamis.
