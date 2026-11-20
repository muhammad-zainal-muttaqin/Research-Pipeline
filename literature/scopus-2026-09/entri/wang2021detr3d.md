# DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2021detr3d` |
| Judul asli | DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries |
| Penulis | Wang, Y.; others |
| Tahun | 2021 |
| Venue | Proceedings of Machine Learning Research |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [wang2021detr3d.pdf](../pdf/wang2021detr3d.pdf)

## Gambaran Umum

Kajian ini membahas deteksi objek tiga dimensi dari citra beberapa kamera untuk kendaraan otonom. Pendekatan berbasis kamera sulit karena hanya tersedia informasi dua dimensi dari citra RGB. Metode yang ada umumnya membangun pipeline deteksi dari perhitungan 2D, lalu memerlukan banyak langkah pascapemrosesan untuk menggabungkan prediksi antarkamera dan membuang kotak yang berlebihan. Sebagian metode lain merekonstruksi awan titik semu dari kedalaman yang diprediksi, sehingga kesalahan kedalaman terakumulasi pada hasil akhir. Penulis mengusulkan DETR3D, pendekatan dari atas ke bawah yang memprediksi kotak pembatas langsung di ruang tiga dimensi tanpa modul prediksi kedalaman padat.

Data yang dipakai adalah nuScenes, kumpulan data berkendara otonom yang terdiri atas 1.000 urutan. Setiap urutan berdurasi sekitar 20 detik dengan laju sampling 20 bingkai per detik. Setiap sampel memuat citra dari enam kamera, yaitu depan kiri, depan, depan kanan, belakang kiri, belakang, dan belakang kanan, beserta parameter intrinsik dan ekstrinsik kamera. Anotasi tersedia setiap 0,5 detik, dengan total 28 ribu sampel latih, 6 ribu sampel validasi, dan 6 ribu sampel uji. Dari 23 kelas, 10 kelas dipakai untuk menghitung metrik. Model menggunakan ResNet101 dengan konvolusi terdeformasi pada tahap ketiga dan keempat, ditambah FPN dan kepala deteksi DETR3D enam lapisan dengan dimensi tersembunyi 256. Pelatihan memakai AdamW selama 12 epoch pada delapan GPU RTX 3090, dengan laju pembelajaran awal 10^-4 yang diturunkan pada epoch ke-8 dan ke-11.

Metode ini mengambil sekumpulan kecil kueri objek yang dipelajari dari seluruh data. Setiap kueri diproyeksikan ke semua kamera menggunakan matriks transformasi kamera, lalu fitur citra pada titik proyeksi tersebut dikumpulkan dan diperbarui melalui lapisan *self-attention* multi-kepala. Fungsi kerugian *set-to-set* ala DETR dipakai untuk mencocokkan prediksi dengan kebenaran dasar. Pada set validasi, DETR3D mencapai NDS 0,374 dan mAP 0,303 tanpa NMS. Nilai mATE-nya 0,860, sedangkan FCOS3D mencapai NDS 0,373 dan mAP 0,299 dengan mATE 0,785 dan memakai NMS. Pada daerah tumpang tindih kamera, yang berisi 18.147 kotak atau 9,7 persen dari total kotak validasi, DETR3D mencapai NDS 0,356 dan mAP 0,231. FCOS3D mencapai NDS 0,317 dan mAP 0,213 pada daerah yang sama. Penulis juga melaporkan varian dengan inisialisasi dari FCOS3D yang mencapai NDS 0,425 dan mAP 0,346 pada validasi, serta varian lanjutan dengan NDS 0,479 dan mAP 0,412. Pada set uji, penulis menyatakan metode ini mengungguli seluruh metode yang ada per 13 Oktober 2021, dengan backbone yang sama dengan DD3D.

Penulis menyatakan beberapa batasan. Pertama, kesalahan translasi masih besar. Pada validasi, mATE DETR3D lebih buruk daripada FCOS3D, yang diduga karena FCOS3D memprediksi kedalaman kotak secara langsung sehingga memberi supervisi translasi yang lebih kuat. Kedua, penulis menilai estimasi kedalaman tetap menjadi tantangan inti, meskipun model menghindari prediksi kedalaman eksplisit. Ketiga, hasil dan analisis dilakukan pada nuScenes dan tidak diuji pada domain lain. Penulis juga menyediakan hasil kualitatif pada enam kamera dan tampilan BEV, yang menunjukkan bahwa model dapat mendeteksi objek kecil, tetapi kesalahan translasi tetap menonjol.
