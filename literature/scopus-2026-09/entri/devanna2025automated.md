# Automated On-Tree Detection and Size Estimation of Pomegranates by a Farmer Robot

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `devanna2025automated` |
| Judul asli | Automated On-Tree Detection and Size Estimation of Pomegranates by a Farmer Robot |
| Penulis | Devanna, Rosa Pia; Vicino, Francesco; Garofalo, Simone Pietro; Vivaldi, Gaetano Alessandro; Pascuzzi, Simone; Reina, Giulio; Milella, Annalisa |
| Tahun | 2025 |
| Venue | Robotics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | pomegranate |

## Tautan Akses
- PDF: [devanna2025automated.pdf](../pdf/devanna2025automated.pdf)
- DOI resmi: https://doi.org/10.3390/robotics14100131

## Gambaran Umum

Studi ini mengatasi pengukuran ukuran buah delima di pohon, yang selama ini dilakukan secara manual dengan kaliper untuk diameter ekuator dan polar. Cara tersebut padat karya, bergantung pada penilaian manusia dalam pemilihan sampel, dan jumlah sampelnya biasanya kecil sehingga rentan terhadap bias. Ukuran buah diperlukan untuk menilai kematangan, memprediksi waktu panen dan hasil, memantau pertumbuhan, serta mengendalikan lengan robot saat pemanen. Penulis mengusulkan kerangka pengukuran otomatis yang dipasang pada robot petani dengan sensor RGB-D konsumen, sehingga tidak memerlukan target kalibrasi tambahan dan dapat dipakai di lapangan secara berkelanjutan.

Pengujian dilakukan di kebun delima komersial di Grottaglie, Apulia, Italia, pada Oktober 2021 menjelang panen. Robot darat Polibot dari Politeknik Bari melintasi satu baris yang berisi 15 pohon dengan jarak rata-rata sekitar 3 m; kamera Intel RealSense D435 dipasang sekitar 1 m di atas tanah dan mengambil pandangan samping dari jarak sekitar 1,5 m pada 6 fps dan resolusi 1.280 × 720 piksel, menghasilkan 945 frame. Dari 15 pohon, 96 buah dipanen secara acak dan diukur dengan kaliper sebagai acuan kebenaran. Untuk melatih segmentasi, buah hasil panen juga dipotret di laboratorium dalam dua kondisi, yaitu pencahayaan seragam terkontrol dan cahaya matahari kuat yang tidak merata. Jaringan segmentasi memakai DeepLabv3+ dengan backbone ResNet18 yang telah dilatih sebelumnya, melalui transfer learning tiga tahap dengan anotasi semi-terawasi.

Mekanisme segmentasi memanfaatkan peningkatan kompleksitas citra secara bertahap. Tahap pertama memakai citra buah lepas di atas latar putih yang memungkinkan mask diperoleh langsung dengan ambang warna. Tahap kedua menerapkan model tersebut pada citra dengan cahaya kuat tidak merata; mask kasar hasil model diperbaiki dengan operasi morfologi, digabungkan dengan data awal, lalu dipakai untuk melatih ulang model. Tahap ketiga mengulang prosedur dengan sejumlah kecil citra lapangan agar model beradaptasi. Mask biner hasil segmentasi diproses lebih lanjut dengan analisis komponen terhubung, operasi morfologi berupa dilasi dan erosi, serta ellipse fitting berbasis momen. Karena buah delima mendekati bentuk bola, elips yang sangat lonjong dibuang melalui ambang eksentrisitas agar hanya buah yang terlihat penuh yang diukur. Sumbu utama elips ditafsirkan sebagai diameter polar dan ekuator pada bidang 2D; titik potong kedua sumbu dengan elips dipetakan ke peta kedalaman yang telah disejajarkan secara spasial dan waktu. Karena kedalaman di tepi buah sering hilang atau salah, penulis menerapkan penyaringan outlier berbasis N kali simpangan baku dengan N = 1, lalu menetapkan posisi kutub ke titik kedalaman bukan nol terdekat. Diameter polar dan ekuator akhirnya dihitung sebagai jarak Euclidean antar kedua titik kutub dalam satuan sentimeter.

Kinerja segmentasi dilaporkan dengan presisi 93,33%, recall 81,49%, dan F1-score 86,42%, dengan waktu pemrosesan rata-rata 0,15 detik per frame pada GPU Nvidia RTX 2080 Ti dan CPU Intel Core i7-4790, lebih cepat daripada laju akuisisi 6 Hz. Untuk 96 sampel buah, data kaliper memiliki rata-rata diameter ekuator 8,91 cm dengan simpangan baku 0,85 cm, sedangkan estimasi kamera menghasilkan 9,15 cm dengan simpangan baku 1,31 cm; pada diameter polar, rata-rata acuan 7,89 cm dengan simpangan baku 0,88 cm berhadapan dengan estimasi 7,62 cm dengan simpangan baku 1,37 cm. Metrik error menunjukkan MAE 1,10 cm untuk diameter ekuator dan 1,05 cm untuk diameter polar, RMSE masing-masing 1,35 cm dan 1,31 cm, simpangan baku error absolut 0,78–0,79 cm, serta MAPE 12,4% dan 13,3%. Error antar sampel sebagian besar berada dalam kisaran ±2 cm.

Batasan yang dinyatakan penulis mencakup pengaruh segmentasi yang buruk ketika buah tertutup sebagian oleh daun atau buah lain serta ketika kontras pencahayaan kuat, karena seluruh pengujian dilakukan dalam kondisi alami tanpa pengaturan cahaya atau penghilangan oklusi. Sensor kedalaman konsumen yang dipasang pada platform bergerak kadang menghasilkan artefak gerak dan penurunan kualitas citra. Penulis mengakui error di sini lebih besar daripada pendekatan fully supervised seperti Mask R-CNN yang digabungkan dengan F-PointNet dan pelengkapan bola, yang melaporkan RMSE 0,235 cm untuk radius pada 100 sampel, meski sistem yang diusulkan mengurangi pelabelan manual sehingga lebih mudah diterapkan skala besar. Sebelum dipakai secara komersial, masih diperlukan perbaikan pada daya tahan perangkat keras, cakupan pengambilan data, perawatan jangka panjang, serta kemampuan algoritme menghadapi beragam pencahayaan, arsitektur kanopi, orientasi buah, dan oklusi. Penulis juga menyebut perlunya memperbesar sampel, membandingkan dengan Mask R-CNN, arsitektur YOLO terbaru, dan pembelajaran zero-shot, serta menguji portabilitas ke tanaman atau tahap pertumbuhan lain; data tersedia atas permintaan penulis.

