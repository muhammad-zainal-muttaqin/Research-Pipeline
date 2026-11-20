# A Dynamic Object Counting Method for Strawberry Fruits using Vision Transformer Networks and Kalman Filter Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2023dynamic` |
| Judul asli | A Dynamic Object Counting Method for Strawberry Fruits using Vision Transformer Networks and Kalman Filter Tracking |
| Penulis | Zhou, Xuehai XZ; Zhang, Yuyang YZ; Sun, Shangpeng Sun SS; Rosenbaum, Phil PR |
| Tahun | 2023 |
| Venue | 2023 Asabe Annual International Meeting |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [zhou2023dynamic.pdf](../pdf/zhou2023dynamic.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202301450

## Gambaran Umum

Penelitian ini bertujuan mengembangkan metode penghitungan dinamis dua dimensi untuk buah stroberi dari video yang direkam dengan ponsel. Penghitungan buah menjadi dasar estimasi hasil panen dan pengaturan aliran produk ke pasar. Penulis menimbang tiga pendekatan, yaitu penghitungan berdasarkan data 3D, regresi, dan deteksi. Data 3D memerlukan sensor seperti LiDAR yang mahal serta daya komputasi besar; regresi menghasilkan satu angka tanpa informasi lokasi dan memerlukan penggabungan beberapa citra yang berisiko kehilangan informasi. Penulis memilih penghitungan berbasis deteksi karena dapat menampilkan kotak pembatas lokasi dan lebih sesuai untuk skala besar. Tiga tujuan penelitian adalah membangun YOLOv5s yang ditingkatkan dengan lapisan vision transformer, membangun algoritma penghitungan dinamis berbasis StrongSORT, dan menguji metode pada video kebun stroberi dalam ruangan.

Data dikumpulkan di kebun dalam ruangan di Montréal, Kanada, pada 9 Februari 2023 dan 2 Maret 2023. Stroberi ditanam pada rak rapat berukuran 2,9 m tinggi, 3,0 m panjang, dan 0,6 m lebar dengan lima lapis. Pada sesi Februari sebagian besar buah masih mentah berwarna hijau muda; pada sesi Maret sebagian besar buah matang berwarna merah cerah. Ponsel Google Pixel 7 Pro dipasang pada gimbal DJI OSMO Mobile 6 dan digerakkan dengan kecepatan sekitar 0,15 m/s. Sepuluh video direkam, lima per sesi, masing-masing berdurasi rata-rata 20 detik pada 30 frame per detik dan resolusi 1920×1080, dengan rata-rata 33 buah per video. Video dipangkas dengan Final Cut Pro untuk membuang buah pada lapis sebelahnya dan rak di latar belakang. Augmentasi data meliputi perubahan warna dan kecerahan, rotasi, penajaman, pencampuran, dan konversi ke skala abu-abu.

Kerangka kerja terdiri atas dua modul. Modul deteksi memakai YOLOv5s yang disisipi lapisan vision transformer; citra dibagi menjadi sejumlah patch tak bertumpang tindih yang dipetakan ke embedding, lalu mekanisme self-attention multi-kepala menghitung bobot antar-embedding untuk menangkap ketergantungan jarak jauh. Modul penghitungan memakai StrongSORT, yang menggabungkan filter Kalman dan pencocokan Hungarian, ditambah modul exponential moving average dan modul maximization of enhanced correlation coefficient untuk mengatasi guncangan kamera. StrongSORT memberi identitas pelacakan serta label status sementara, terkonfirmasi, atau terhapus. Algoritma DynCount memetakan identitas yang terkonfirmasi ke angka hitungan berurutan; jika identitas sudah ada dalam larik, buah tidak dihitung ulang. Hasil penghitungan dan kotak pembatas ditampilkan kembali pada video.

Pelatihan dan validasi berjalan pada Ubuntu 22.04 LTS dengan kartu grafis GeForce RTX 3060Ti. Penulis memakai pembelajaran transfer dan tidak melakukan anotasi pada data latih; 40 citra dari sesi 9 Februari diberi label dengan labelImg, masing-masing 20 untuk validasi dan 20 untuk pengujian, sedangkan data latih berjumlah 440 citra setelah augmentasi. Ambang keyakinan deteksi ditetapkan 0,24 dan ambang IoU 0,18. Dengan ukuran batch 16, waktu pelatihan kurang dari 13 menit. Pola overfitting mulai muncul sekitar epoch ke-60, sehingga jumlah epoch ditetapkan 75. Loss objek terendah 0,0117 dan berosilasi sekitar 0,015. Deteksi mencapai mAP tertinggi 89,94% pada IoU 0,5 dan 54,96% pada rentang IoU 0,5–0,95.

Acuan hitung dibangun oleh dua orang yang menghitung secara mandiri, lalu hasilnya dirata-ratakan. Selisih hitungan metode terhadap acuan berkisar dari 87,50% sampai 112,77%, dengan nilai di atas 100% berarti metode melebihitung. Dari galat absolut, akurasi rata-rata untuk sepuluh video adalah 92,05%. Penulis menyebut keterbatasan berupa buah yang tertutup daun berat tidak terdeteksi, kemunculan kembali buah setelah tertutup yang salah dikenali sebagai buah baru, serta buah mentah yang lebih mudah terlewat karena warnanya dan oklusi daun. Guncangan saat berjalan, gangguan fokus, dan kesulitan menjaga kecepatan pengambilan juga memengaruhi hasil. Penurunan ambang keyakinan dapat menangkap buah yang tertutup, tetapi menambah positif palsu. Penulis menganjurkan penggunaan UAV berkamera, penggabungan citra berturut menjadi video, penambahan data, serta model regresi untuk mengompensasi faktor tersebut.
