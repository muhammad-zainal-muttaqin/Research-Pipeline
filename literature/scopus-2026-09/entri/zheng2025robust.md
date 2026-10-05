# A Robust Tomato Counting Framework for Greenhouse Inspection Robots Using YOLOv8 and Inter-Frame Prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2025robust` |
| Judul asli | A Robust Tomato Counting Framework for Greenhouse Inspection Robots Using YOLOv8 and Inter-Frame Prediction |
| Penulis | Zheng, Wanli; Dai, Guanglin; Hu, Miao; Wang, Pengbo |
| Tahun | 2025 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [zheng2025robust.pdf](../pdf/zheng2025robust.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy15051135

## Gambaran Umum

Makalah ini mengusulkan kerangka penghitungan tomat untuk robot inspeksi rumah kaca swa-gerak. Kerangka memadukan detektor YOLOv8 untuk tandan (*cluster*) dan buah tunggal, penyaringan kedalaman (*depth filtering*) untuk membuang tomat latar belakang, serta prediksi antarbingkai (*inter-frame prediction*) yang memakai perpindahan robot dari sensor inersia (*inertial measurement unit*, IMU) untuk menautkan tandan yang sama pada bingkai berbeda. Tujuannya mengurangi penghitungan ganda, pergantian identitas, dan deteksi tomat latar.

Data diambil dari rumah kaca komersial di Suzhou, Provinsi Jiangsu, Tiongkok, dengan kamera RealSense D435i pada robot yang bergerak 0,1 m/s dan 5 bingkai per detik selama Oktober sampai Desember 2024. Pengujian dilakukan pada tiga punggungan (*ridge*) yang hitungan acuannya dihitung manual: 98, 105, dan 108 tandan, serta 1.010, 1.055, dan 1.177 buah.

Hasil utama: akurasi hitungan tandan rerata 97,30% (97,73%, 97,09%, 97,09% pada tiga percobaan), dibandingkan 80,91% sampai 85,76% untuk YOLOv8 + DeepSORT dan 74,80% sampai 83,90% untuk estimasi kerapatan. *Multiple object tracking accuracy* (MOTA) mencapai 0,954 pada punggungan 3 dan 0,980 serta 0,952 pada punggungan 1 dan 2, dibandingkan 0,582, 0,524, dan 0,600 untuk YOLOv8 + DeepSORT.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa penghitungan tomat manual memakan lebih dari 20 jam per minggu pada operasi besar, dengan biaya tenaga kerja sekitar 15% per musim dan laju galat hingga 35% (angka ini tidak disertai sumber pada teks). Estimasi hasil secara waktu-nyata dinilai berguna untuk logistik dan negosiasi harga.

Kesulitan di rumah kaca menurut penulis adalah oklusi oleh daun dan tandan lain, pencahayaan yang berubah, serta keterbatasan komputasi pada robot bergerak. Penulis menilai pelacak yang memakai fitur tampilan seperti DeepSORT rentan karena tomat sangat mirip satu sama lain, dan tomat pada punggungan seberang ikut terdeteksi sehingga menimbulkan positif palsu dan pergantian identitas.

## Ide Utama

Karena robot bergerak lurus dengan kecepatan diketahui dan jarak kamera ke tandan relatif tetap, posisi sebuah tandan pada bingkai berikutnya dapat diprediksi dari perpindahan robot menurut IMU dan kedalaman tandan, tanpa fitur tampilan. Kotak hasil prediksi dibandingkan dengan kotak deteksi pada bingkai lain memakai *intersection over union* (IOU); bila IOU melebihi 0,7, kedua kotak dianggap tandan yang sama. Penyaringan kedalaman 70 cm membuang tomat latar. Tandan yang sama dari beberapa bingkai dipertahankan sebagai satu entri, yaitu entri dengan jumlah buah tunggal terbanyak.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Tomat ditanam pada punggungan dengan jarak antarbaris 80 sampai 95 cm dan jarak antartanaman 25 sampai 35 cm; buah matang berada pada ketinggian 50 sampai 160 cm. Jalur sepanjang 60 m terletak di antara dua punggungan. Kamera RealSense D435i merekam citra warna dan kedalaman yang disejajarkan pada resolusi 1080 × 720 piksel. Pengumpulan berlangsung tiga periode per hari (06.00 sampai 08.00, 12.00 sampai 14.00, 16.00 sampai 17.00) dan menghasilkan sekitar 80 GB citra. Sebanyak 3.000 citra dipilih untuk dianotasi dengan Labelme dalam dua tahap: kotak tandan, lalu buah tunggal berlabel matang (merah) atau mentah (hijau). Tomat latar, tomat yang terpotong tepi citra, dan tomat di luar citra tidak dianotasi. Dua anotator memeriksa silang label. Augmentasi (pembalikan horizontal, translasi acak sampai 10%, rotasi acak sampai 10 derajat) menghasilkan 15.000 citra untuk tandan dan 15.000 citra untuk buah tunggal, dibagi 90% latih, 5% uji, dan 5% validasi secara acak. Kultivar tomat tidak dilaporkan; teks menyebut hanya "varietas yang sama". Robot berdimensi 1,4 × 0,86 × 2,2 m, berbobot 200 kg, dengan tiga kamera pada tiga ketinggian, IMU HWT901B, dan komputer NVIDIA Jetson Nano; kamera tengah dipakai untuk buah, pada jarak 40 sampai 50 cm dari bidang punggungan.

### 2. Deteksi

Dua model YOLOv8 dilatih: satu untuk tandan dan satu untuk buah tunggal (matang dan mentah). Model tandan menentukan wilayah minat; citra di luar kotak dihitamkan sebelum dimasukkan ke model buah tunggal.

### 3. Tuple spasiotemporal dan penyaringan

Setiap tandan pada tiap bingkai diubah menjadi tuple spasiotemporal yang memuat nomor bingkai, ID, posisi, ukuran, jumlah buah merah dan hijau, kedalaman rerata $D$, dan perpindahan robot $s$. Kedalaman tandan adalah rerata kedalaman buah pada titik pusat kotak. Tuple dibuang bila $D$ lebih dari 70 cm (tomat latar) atau bila koordinat $x$ kurang dari 100 atau lebih dari 1180 piksel (tandan terpotong tepi kiri atau kanan).

### 4. Prediksi antarbingkai dan penyatuan

Pusat kotak diproyeksikan ke koordinat kamera dengan parameter intrinsik, digeser dengan perpindahan $s$ antara dua bingkai dengan kedalaman dianggap tetap, lalu diproyeksikan balik menjadi kotak prediksi. IOU antara kotak prediksi dan semua kotak pada bingkai lain dihitung dengan ambang 0,7. Perbandingan dilakukan terhadap tuple dari $t$ bingkai sebelumnya dengan $t = 70$ (ditetapkan setelah pengujian). Jumlah tandan adalah jumlah entri tersisa, dan jumlah buah merah dan hijau adalah jumlah nilai $a$ dan $b$ seluruh entri.

### 5. Pascapemrosesan

Untuk tandan di tepi atas atau bawah, selisih antara panjang sisi melintang kotak tandan dan rerata panjang sisi buah tunggal dipakai sebagai kompensasi. Untuk tandan yang saling bertumpuk (kotak berpotongan), jumlah buah pada tandan yang terhalang ditaksir dari kerapatan buah pada tandan tetangga yang tidak terhalang, dengan ambang IOU untuk menyaring perpotongan semu.

### 6. Penentuan kematangan

Nilai $k = (R + a)/G$ dihitung dari komponen R (RGB), a (Lab), dan G (RGB), lalu dinormalisasi. Buah dengan $k$ 0 sampai 74% dianggap mentah dan 74 sampai 100% dianggap matang.

## Eksperimen dan Hasil

Percobaan memakai tiga punggungan yang berdekatan di rumah kaca yang sama dengan data pelatihan, pada tanaman dari varietas dan budi daya yang sama tetapi bukan tomat yang sama dengan data latih. Metode dijalankan pada GPU GTX 2060 komputer industri robot, sedangkan pelatihan memakai AMD R7 5800X dan RTX 3080 Ti. Pembanding adalah YOLOv8 + DeepSORT dan estimasi kerapatan (mengekstrapolasi dari sampel citra tiap 1,5 m, sekitar tiap 15 detik, dengan lebar bidang citra 623 mm).

Tabel 1. Acuan hitungan manual (Tabel 2 makalah).

| Besaran | Punggungan 1 | Punggungan 2 | Punggungan 3 |
|---|---|---|---|
| Tandan | 98 | 105 | 108 |
| Buah matang | 232 | 258 | 251 |
| Buah mentah | 778 | 797 | 926 |
| Total buah | 1.010 | 1.055 | 1.177 |

Tabel 2. Pelacakan tandan (Tabel 4 makalah).

| Metode | Punggungan | FN | FP | IDSW | MOTA |
|---|---|---|---|---|---|
| YOLOv8 + DeepSORT | 1 | 2 | 29 | 10 | 0,582 |
| YOLOv8 + DeepSORT | 2 | 3 | 34 | 13 | 0,524 |
| YOLOv8 + DeepSORT | 3 | 2 | 31 | 9 | 0,600 |
| Metode usulan | 1 | 2 | 0 | 0 | 0,980 |
| Metode usulan | 2 | 4 | 0 | 0 | 0,952 |
| Metode usulan | 3 | 3 | 1 | 1 | 0,954 |

Tabel 3. Akurasi dan kecepatan hitungan tandan (Tabel 5 makalah; EC = hitungan terestimasi pada tiga percobaan).

| Metode | EC (percobaan 1, 2, 3) | ACC (%) | FPS |
|---|---|---|---|
| Metode usulan | 302, 300, 300 | 97,73; 97,09; 97,09 | 28,84; 28,66; 28,67 |
| YOLOv8 + DeepSORT | 368, 371, 353 | 80,91; 79,94; 85,76 | 20,74; 21,09; 20,87 |
| Estimasi kerapatan | 253, 231, 277 (hasil hitung) | 81,81; 74,80; 83,90 | tidak dilaporkan |

Pada hitungan buah tunggal, koefisien determinasi $R^2$ adalah 0,853 (kemiringan regresi 0,921) untuk metode usulan, 0,622 untuk YOLOv8 + DeepSORT, dan 0,837 untuk estimasi kerapatan. Pascapemrosesan menaikkan $R^2$ menjadi 0,897 dengan kemiringan 0,856 pada analisis dua kelompok; penulis menyebut efeknya terutama pada tandan di tepi atas dan bawah serta tandan terhalang, dan mengakui adanya koreksi berlebih yang kadang menghasilkan hitungan lebih tinggi daripada acuan.

Tabel 4. Akurasi hitungan buah matang dan mentah (Tabel 6 makalah).

| Kelompok | Percobaan 1 | Percobaan 2 | Percobaan 3 |
|---|---|---|---|
| Metode usulan, matang (%) | 93,22 | 92,03 | 92,03 |
| Metode usulan, mentah (%) | 92,55 | 91,79 | 89,74 |
| Estimasi kerapatan, matang (%) | 77,70 | 64,14 | 80,08 |
| Estimasi kerapatan, mentah (%) | 72,57 | 78,62 | 77,10 |

Teks menyatakan akurasi buah matang 92,03%, buah mentah 91,79%, dan rerata kematangan 91,96%; angka itu sesuai dengan percobaan 2 pada Tabel 6, bukan rerata tiga percobaan. Waktu proses yang dilaporkan: 0,03 s per citra untuk deteksi tandan, 0,08 s per citra untuk deteksi buah tunggal, dan 0,18 s untuk mengubah tandan satu citra menjadi tuple spasiotemporal.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: pelacakan tidak bergantung pada kemiripan tampilan, positif palsu dan pergantian identitas turun tajam (positif palsu 0 sampai 1 dibanding 29 sampai 34), kecepatan 28,72 FPS dibanding 20,90 FPS untuk YOLOv8 + DeepSORT (Tabel 3), dan sistem cukup ringan untuk robot. Penulis juga menyatakan keterbatasan: metode memerlukan IMU berpresisi tinggi; tandan di tengah antara dua sisi dapat lolos ambang kedalaman menjadi positif palsu; pascapemrosesan dapat mengoreksi berlebih pada tandan terhalang berat; dan pemisahan kematangan berbasis warna mungkin memerlukan kalibrasi ulang untuk varietas lain. Pekerjaan mendatang mencakup ketahanan terhadap oklusi dan integrasi dengan sistem kendali.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Hanya tiga punggungan dari satu rumah kaca standar yang diuji, dengan jalur lurus dan kecepatan tetap, sehingga generalisasi ke kebun terbuka tidak teruji. Cakupan satu sisi baris tidak mengenai identitas lintas sisi. Metode mengandaikan kedalaman tandan tetap antarbingkai dan geometri kamera sejajar bidang punggungan. Beberapa angka pada makalah tidak konsisten (lihat catatan verifikasi).

## Kaitan dengan Tinjauan main6

Makalah ini menangani tandan yang terlihat pada banyak bingkai berurutan dari satu sisi punggungan. Mekanismenya adalah pelacakan berbasis posisi: prediksi posisi kotak dari odometri IMU dan kedalaman, lalu pencocokan IOU dengan ambang 0,7 pada jendela 70 bingkai, tanpa fitur tampilan. Hitungan dilaporkan terpisah untuk tomat matang dan mentah pada tingkat buah tunggal, sementara tandan dihitung sebagai satu kelas. Pengelompokan matang dan mentah diperoleh dari ambang warna, dan identitas dilacak pada tingkat tandan, bukan pada tingkat buah tunggal. Acuan hitungan adalah hitungan manual per punggungan.

Hal yang dapat dipindahkan ke tandan kelapa sawit multi-sisi: penggunaan isyarat geometris (perpindahan sensor dan kedalaman) untuk menautkan objek yang sama, bukan kemiripan tampilan, serta pemilihan entri dengan hitungan buah terbanyak dari beberapa pandangan. Batasan pemindahannya, mekanisme ini mengandaikan gerak platform yang terukur secara metrik dan satu sisi baris; tidak ada mekanisme untuk mengaitkan objek antara dua sisi pohon yang berbeda.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zheng2025robust`.

Zheng dkk. mengusulkan kerangka penghitungan tomat rumah kaca untuk robot inspeksi yang memadukan YOLOv8, penyaringan kedalaman 70 cm, dan prediksi posisi antarbingkai dari perpindahan IMU dengan ambang IOU 0,7 untuk menyatukan tandan yang sama tanpa fitur tampilan. Pada tiga punggungan dengan acuan hitungan manual, akurasi hitungan tandan rerata 97,30% dan MOTA 0,952 sampai 0,980, dibandingkan MOTA 0,524 sampai 0,600 pada YOLOv8 + DeepSORT.

Catatan verifikasi data: Acuan hitungan dari Tabel 2, MOTA dari Tabel 4, akurasi tandan dari Tabel 5, dan akurasi kematangan dari Tabel 6; metode dari Bagian 3. Teks ekstraksi terbaca utuh, dan tabel terbaca sebagai deretan nilai per baris yang dipetakan menurut urutan judul kolom. Ketidakkonsistenan pada makalah: abstrak menyebut akurasi deteksi tandan 97,09%, sedangkan Tabel 3 menyebut 97,30% (rerata tiga percobaan; 97,09% adalah percobaan 2 dan 3); Tabel 3 menyebut MOTA 0,569 dan Tabel 4 memberi 0,582, 0,524, 0,600 (0,569 tampaknya rerata, tetapi teks bagian 4.4 menulis 0,582); nilai "EC" 302, 300, 300 pada Tabel 5 tidak sama dengan jumlah acuan tandan tiga punggungan (311) dan tidak dijelaskan apakah itu hasil per percobaan; akurasi kerapatan tandan pada Bagian 5 ditulis 79,35% yang sama dengan rerata kematangan kerapatan; Tabel 6 memuat dua baris berlabel "Measured value (mature)" (nilai kedua tampaknya buah mentah) dan nilai terukur (234, 231, 231) tidak persis sama dengan acuan Tabel 2; $R^2$ pascapemrosesan 0,897 dibandingkan 0,856 pada Bagian 5, sedangkan kemiringan 0,856 pada Bagian 4.5 memiliki angka yang sama sehingga dapat tertukar. Klaim peningkatan MOTA 37,20% dan penurunan galat hitungan buah 16,85% terhadap baseline kerapatan (Bagian 1) tidak dapat ditelusuri ke tabel mana pun. Kultivar tomat, jumlah citra uji, dan jumlah bingkai total per percobaan (selain kolom "Sum of frames" pada Tabel 4) tidak dilaporkan. Data tersedia berdasarkan permintaan.
