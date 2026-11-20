# Tomato cluster detection and counting using improved YOLOv5 based on RGB-D fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rong2023tomato` |
| Judul asli | Tomato cluster detection and counting using improved YOLOv5 based on RGB-D fusion |
| Penulis | Rong, Jiacheng; Zhou, Hui; Zhang, Fan; Yuan, Ting; Wang, Pengbo |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [rong2023tomato.pdf](../pdf/rong2023tomato.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107741

## Gambaran Umum

Penelitian ini bertujuan menghitung hasil panen tomat secara otomatis di rumah kaca. Penghitungan manual membutuhkan banyak tenaga kerja, sedangkan tenaga kerja pertanian semakin berkurang. Robot inspeksi dapat membantu tugas ini, tetapi muncul dua masalah. Pertama, tomat pada barisan seberang ikut terdeteksi sehingga hasil terlalu tinggi. Kedua, tomat yang sama bisa terhitung lebih dari sekali saat kamera bergerak sepanjang barisan. Penulis mengusulkan metode yang menggabungkan deteksi objek, pelacakan lintas *frame*, dan penghitungan pada area pelacakan tertentu.

Data dikumpulkan di lokasi rumah kaca Nihui di Suzhou, Tiongkok, menggunakan robot inspeksi yang bergerak di atas tanah dan lintasan. Robot ini membawa dua kamera RGB-D, yaitu Intel RealSense D435i dan Microsoft Azure Kinect DK, dengan resolusi 1280 × 720 piksel. Kamera dipasang pada ketinggian 1050 mm dan 1550 mm dari lantai, dengan jarak 500 sampai 700 mm dari tomat. Sebanyak 574 pasang citra RGB dan citra kedalaman diambil dalam berbagai kondisi cahaya, lalu dilabeli dengan *bounding box* menggunakan alat labelImg. Hanya kelompok tomat dengan lebih dari empat buah yang dilabeli. Tomat yang berjarak lebih dari 0,8 m dari kamera tidak dilabeli karena termasuk latar belakang. Data dibagi menjadi data latih, validasi, dan uji dengan perbandingan 6:2:2.

Metode yang diusulkan terdiri atas tiga bagian. Pertama, YOLOv5-4D menerima masukan gabungan citra RGB dan citra kedalaman untuk mengurangi deteksi tomat latar belakang. Kedua, ByteTrack melacak kelompok tomat di antara *frame* video. Ketiga, metode penghitungan pada *tracking region* menghindari hitungan ganda akibat perpindahan ID, atau *ID switch*. Pada data uji, YOLOv5-4D mencapai akurasi deteksi 97,9 persen dan mAP@0,5:0,95 sebesar 0,748. Pada pengujian lapangan, rata-rata akurasi penghitungan mencapai 95,1 persen. Algoritma terintegrasi berjalan lebih dari 40 FPS pada laptop dengan CPU Ryzen 5800H dan GPU RTX 3070, sehingga penulis menilai penghitungan dapat dilakukan secara real time. Model dilatih selama 2000 epoch dengan ukuran masukan 640 piksel.

Penulis menyatakan beberapa batasan. Ukuran *batch* maksimum hanya 3 karena keterbatasan memori GPU, dan penulis menilai ukuran ini kecil untuk konvergensi model. Penulis juga menyatakan bahwa klasifikasi tingkat kematangan tomat belum dilakukan. Menurut penulis, prediksi hasil panen akan lebih berdampak pada rantai pasok dan pasar setelah tahap klasifikasi kematangan ditambahkan. Dengan demikian, cakupan penelitian ini masih terbatas pada penghitungan kelompok tomat.
