# Tomato Yield Estimation Using an Improved Lightweight YOLO11n Network and an Optimized Region Tracking-Counting Method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2025tomato` |
| Judul asli | Tomato Yield Estimation Using an Improved Lightweight YOLO11n Network and an Optimized Region Tracking-Counting Method |
| Penulis | Wang, Aichen; Xu, Yuanzhi; Hu, Dong; Zhang, Liyuan; Li, Ao; Zhu, Qingzhen; Liu, Jizhan |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [wang2025tomato.pdf](../pdf/wang2025tomato.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15131353

## Gambaran Umum

Makalah ini mengusulkan sistem estimasi hasil tomat dari video yang terdiri atas dua komponen: jaringan YOLO11n yang diperingan untuk deteksi dan segmentasi semantik buah, serta metode pelacakan-pencacahan berbasis wilayah (*region tracking-counting*) yang jendela hitungnya dioptimalkan dengan *particle swarm optimization* (PSO). Sistem ini menghitung buah tomat pada tiga tingkat kematangan, yaitu matang (*ripe*), setengah matang (*semi-ripe*), dan mentah (*unripe*). Masalah yang disasar adalah galat hitung akibat oklusi dan tumpang tindih antara buah dan daun di lingkungan rumah kaca.

Data diambil pada Juni 2023 di rumah kaca milik Jiangsu Xingang Agricultural Technology Co., Ltd. (Zhenjiang, Tiongkok) memakai kamera Intel RealSense D435 pada rel beroda. Terkumpul 808 citra mentah untuk pelatihan model deteksi dan 21 segmen video berdurasi 30 detik untuk menguji pelacakan dan pencacahan. Pada set uji citra, model usulan mencapai presisi 91,3% dan mAP50 93,3% untuk tugas kotak pembatas (*box*), serta presisi 90,5% dan mAP50 92,3% untuk tugas segmentasi, dengan 2,66 M parameter dan 8,0 GFLOPs.

Untuk pencacahan, metode wilayah yang dioptimalkan PSO mencapai *mean counting error* (MCE) 6,6% pada set uji video, lebih rendah 5,0 poin persentase daripada Bytetrack (11,6%) dan 2,1 poin persentase daripada metode hitung lintas-garis (*cross-line counting*, 8,7%). Sistem dilaporkan berjalan pada Jetson Orin NX dengan kecepatan rerata 62 FPS.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa estimasi hasil tomat sebelum panen berguna bagi pengaturan strategi tanam, penyimpanan, logistik, dan pemasaran, karena buah panen berumur simpan pendek. Cara manual padat karya dan menghasilkan galat akibat oklusi daun, pertumbuhan yang rapat, serta sulitnya membedakan tingkat kematangan. Pendekatan penglihatan mesin klasik berbasis operator rancangan manual dinilai kurang fleksibel karena perlu disesuaikan pada tiap skenario.

Penulis meninjau beberapa pendekatan pencacahan buah terdahulu. Metode satu pandang dan dua pandang (misalnya MangoYOLO dengan koefisien koreksi, yang galat hasilnya dikutip berkisar 4,6% sampai 15,2% pada lima kebun) disebut menghadapi kesulitan mengenali buah berskala beragam akibat oklusi. Metode pelacakan-pencacahan wilayah terdahulu (Zhang dkk., rerata galat hitung 8%) disebut tidak mengoptimalkan wilayah hitungnya. Penulis menyimpulkan bahwa oklusi, latar kompleks, dan variasi posisi buah masih menyebabkan hitungan kurang atau hitungan ganda.

Pelacak multi-objek seperti Bytetrack mengandalkan pemberian ID yang konsisten. Penulis menyebut bahwa ID yang salah tetapkan atau tidak cocok menimbulkan galat hitung besar, dan oklusi lama membuat ID hilang sehingga satu buah terhitung berulang.

## Ide Utama

Gagasan pertama adalah memperingan YOLO11n agar dapat dijalankan pada perangkat tepi (*edge device*) tanpa menurunkan akurasi secara berarti. Tiga perubahan dipakai: blok C3k2-F (gabungan FasterNet dan C3k2), penggantian lapisan Conv dengan *Depthwise Separable Convolution* (DSConv), dan penggantian fungsi kerugian CIoU dengan GIoU, ditambah *Distribution Focal Loss* (DFL) dan BCELoss pada regresi.

Gagasan kedua adalah mengurangi ketergantungan pencacahan pada kontinuitas ID pelacak. Metode lintas-garis menghitung sebuah buah ketika kotaknya memotong garis vertikal virtual di tengah bidang pandang. Karena kamera bergerak, setiap buah diasumsikan pasti melintasi garis itu sehingga ID yang tidak stabil tidak lagi menjadi sumber galat utama. Kelemahannya, buah yang terhalang daun tepat saat melintasi garis tidak terhitung. Penulis kemudian melebarkan garis menjadi wilayah simetris terhadap garis tengah vertikal citra dan mencatat ID sebuah kotak begitu kotak itu mulai memasuki wilayah tersebut. Lebar wilayah dipilih dengan PSO.

## Cara Kerja Langkah demi Langkah

```
  video --> YOLO11n ringan --> kotak + kelas
                                   |
                         Bytetrack (Kalman + Hungarian)
                                   |
                         ID unik per buah
                                   |
        hitung bila kotak mulai memasuki wilayah tengah (lebar dioptimalkan PSO)
                                   |
                         hitungan per kelas kematangan
```

### 1. Akuisisi data

Kamera Intel RealSense D435 beresolusi 1280 x 720 dipasang pada batang geser vertikal yang terhubung ke Jetson Orin NX melalui USB 3.0, dengan jarak sekitar 1,2 m dari barisan tanaman tomat. Perangkat dibawa oleh kereta rel sehingga dapat berpindah lokasi. Terkumpul 808 citra mentah pada berbagai tahap pertumbuhan, tingkat oklusi, dan kondisi cahaya. Sebanyak 242 citra dipilih acak sebagai set uji dan 566 citra sisanya menjadi set latih dan validasi awal. Citra dikompresi menjadi 640 x 640. Anotasi memakai Labelme (versi 5.5.0) dengan kontur tomat, termasuk bagian yang terhalang. Buah dengan piksel kurang dari 2500 tidak dianotasi. Tingkat kematangan dinilai dari nilai RGB menjadi tiga kelas: matang, setengah matang, dan mentah.

Untuk evaluasi pencacahan, video direkam dengan kereta bergerak pada kecepatan tetap. Terdapat 21 segmen berdurasi 30 detik (1280 x 720, 30 bingkai per detik): delapan untuk pelatihan algoritma pelacakan dan pencacahan, empat untuk validasi, dan sembilan untuk uji. Jumlah tanaman, kultivar, dan jumlah tomat total tidak dilaporkan pada teks.

### 2. Jaringan YOLO11n yang diperingan

YOLO11n dipilih sebagai garis dasar karena merupakan varian terkecil. Perubahan yang dilakukan: (a) blok C3k2-F, yaitu C3k2 yang lapisan *bottleneck*-nya diganti blok FasterNet berbasis *partial convolution* (PConv), untuk mengurangi FLOPs; (b) DSConv sebagai pengganti Conv, yang menurut penulis menurunkan kompleksitas komputasi tanpa menambah parameter; (c) GIoU sebagai pengganti CIoU. Pelatihan memakai PyTorch 1.13.1 pada GPU GTX 3080Ti dengan masukan 640 x 640, 200 *epoch*, *batch* 16, ambang IoU 0,7, SGD dengan laju belajar awal 0,01, *weight decay* 0,0005, momentum 0,937, dan bobot pralatih resmi.

### 3. Pelacakan dengan Bytetrack

Bytetrack yang terintegrasi dengan YOLO11n memakai tiga langkah: deteksi, estimasi keadaan dengan filter Kalman, dan pencocokan lintas bingkai dengan algoritma Hungarian. Lintasan yang gagal dicocokkan disimpan sementara; bila tidak cocok pada beberapa bingkai, lintasan dianggap hilang dan dihapus. Setiap buah yang terlacak mendapat ID unik untuk dihitung.

### 4. Hitung lintas-garis dan hitung wilayah

Metode lintas-garis menghitung buah ketika kotaknya memotong garis vertikal di tengah bidang pandang. Metode wilayah melebarkan garis itu menjadi wilayah dengan tinggi 720 piksel (resolusi vertikal) dan lebar yang dicari pada rentang [0, 1280]. Pada metode ini, ID sebuah kotak dicatat dan dihitung begitu kotak mulai memasuki wilayah.

### 5. Optimasi lebar wilayah dengan PSO

Fungsi kebugaran (*fitness*) adalah galat kuadrat rerata akar (RMSE) antara jumlah sebenarnya dan jumlah terhitung pada set video, dengan lebar dibulatkan menjadi bilangan genap. Optimasi berjalan 200 iterasi dan nilai kebugaran konvergen sekitar 2,5. Lebar 876 piksel memberi nilai kebugaran minimum sehingga ukuran akhir jendela adalah 876 x 720.

### 6. Metrik

Untuk jaringan: presisi, *recall*, AP, dan mAP, ditambah jumlah parameter dan GFLOPs. Untuk pencacahan: *mean precision* (MP), *mean error* (ME), *mean repetition* (MR), dan MCE. MCE didefinisikan sebagai rerata $|G_i - E_i| / G_i \times 100\%$ dengan $G_i$ jumlah sebenarnya dan $E_i$ jumlah prediksi pada video ke-$i$. Acuan jumlah sebenarnya adalah hitung manual (*manual counts*).

## Eksperimen dan Hasil

### Ablasi dan perbandingan jaringan

Pengujian dilakukan pada set uji 242 citra. Tabel 1 makalah memuat hasil ablasi, dan Tabel 2 membandingkan model usulan dengan jaringan lain.

| Model | Box P (%) | Box R (%) | Box mAP50 (%) | Seg P (%) | Seg mAP50 (%) | Param (M) | GFLOPs |
|---|---|---|---|---|---|---|---|
| YOLO11n | 89,4 | 91,6 | 93,5 | 89,2 | 93,0 | 2,88 | 10,5 |
| + C3k2-F | 90,7 | 90,4 | 94,6 | 90,4 | 94,2 | 2,66 | 9,8 |
| + C3k2-F + DSConv | 90,3 | 88,2 | 94,2 | 89,8 | 93,7 | 2,66 | 8,0 |
| + C3k2-F + DSConv + GIoU (usulan) | 91,3 | 86,2 | 93,3 | 90,5 | 92,3 | 2,66 | 8,0 |

Model usulan memiliki mAP50:90 65,8% (*box*) dan 59,3% (*seg*), dan presisi serta mAP50 lebih rendah pada YOLO11n dasar hanya untuk mAP50 dan *recall*. Berdasarkan baris selisih pada Tabel 1, *recall* *box* turun 5,4 poin dan mAP50 *box* turun 0,2 poin dibanding YOLO11n dasar, sedangkan presisi *box* naik 1,9 poin. Penulis menyatakan penambahan GIoU menaikkan presisi dengan sedikit penurunan mAP dan *recall*.

| Model | Box P (%) | Box mAP50 (%) | Seg P (%) | Seg mAP50 (%) | FPS | Param (M) | GFLOPs |
|---|---|---|---|---|---|---|---|
| Mask-RCNN | 92,0 | 94,5 | 91,9 | 86,0 | 19 | 41,3 | 251,4 |
| YOLOv5n | 79,3 | 84,4 | 79,2 | 85,0 | 116 | 7,10 | 16,0 |
| YOLOv6n | 85,3 | 86,2 | 86,2 | 87,4 | 84 | 4,9 | 7,0 |
| YOLOv7 | 91,8 | 90,6 | 91,4 | 90,2 | 32 | 36,90 | 104,7 |
| YOLOv8n | 88,4 | 89,5 | 87,8 | 88,7 | 60 | 3,40 | 12,6 |
| YOLO11n ringan (usulan) | 91,3 | 93,3 | 90,5 | 92,3 | 62 | 2,66 | 8,0 |

Mask-RCNN dan YOLOv7 paling dekat dalam akurasi, tetapi dengan FPS, parameter, dan GFLOPs yang menurut penulis tidak memenuhi kebutuhan perangkat tertanam. YOLOv5n dan YOLOv6n lebih cepat (116 dan 84 FPS) tetapi presisi dan mAP50-nya lebih rendah. Pada Tabel 2, Mask-RCNN memiliki mAP50 *box* (94,5%) lebih tinggi daripada model usulan (93,3%).

### Optimasi wilayah hitung

Pada set validasi video (empat video), Tabel 3 membandingkan tiga metode.

| Video | Jumlah sebenarnya | Lintas-garis | Wilayah 500 piksel | Wilayah PSO (876 piksel) |
|---|---|---|---|---|
| Video 1 | 157 | 145 | 175 | 171 |
| Video 2 | 167 | 153 | 173 | 171 |
| Video 3 | 123 | 113 | 114 | 116 |
| Video 4 | 134 | 119 | 125 | 124 |
| MCE (%) | | 8,8 | 7,3 | 6,1 |

### Evaluasi pencacahan pada set uji video

Tabel 4 membandingkan tiga metode pada set uji video (sembilan segmen menurut pembagian di Bagian 2.1).

| Metode | MP (%) | ME (%) | MR (%) | MCE (%) |
|---|---|---|---|---|
| Bytetrack | 80,6 | 11,4 | 12,3 | 11,6 |
| Lintas-garis | 84,9 | 9,1 | 6,8 | 8,7 |
| Wilayah (PSO) | 86,6 | 7,4 | 8,3 | 6,6 |

Bytetrack memiliki MR tertinggi karena hilangnya ID pada objek yang terhalang lama sehingga terjadi hitungan ganda. Metode lintas-garis memiliki MR terendah (6,8%) tetapi menghasilkan hitungan terlewat bila buah terhalang saat melintasi garis. Metode wilayah memiliki MCE terkecil.

Hasil per kelas kematangan (Tabel 5) adalah sebagai berikut.

| Kelas | MP (%) | ME (%) | MR (%) | MCE (%) |
|---|---|---|---|---|
| Matang | 93,4 | 7,5 | 8,7 | 12,3 |
| Setengah matang | 71,9 | 10,4 | 3,4 | 16,9 |
| Mentah | 91,3 | 7,3 | 11,8 | 17,3 |
| Semua | 86,6 | 7,4 | 8,3 | 6,6 |

Penulis menjelaskan bahwa kelas setengah matang paling sulit karena warna dan bentuknya mirip kelas lain, sedangkan kelas mentah memiliki MR tertinggi karena variasi ukuran dan warna yang membuat satu buah terhitung lebih dari sekali. Beberapa tomat setengah matang bernilai RGB mendekati matang atau mentah sehingga hasil deteksinya berganti-ganti kelas dan menimbulkan hitungan ganda (Gambar 12d,e). Penulis juga menulis bahwa MCE 6,6% setara akurasi hitung 93,4%.

Pada Jetson Orin NX, seluruh alur kerja mencapai rerata 62 FPS, memori puncak sekitar 3,1 GB, dan daya rerata 15,6 W.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: model ringan dengan akurasi deteksi yang dipertahankan, pelacakan dan pencacahan yang tidak terlalu bergantung pada kontinuitas ID, hasil per kelas kematangan, serta kecepatan waktu nyata pada perangkat tepi.

Keterbatasan yang dinyatakan penulis: akurasi deteksi buah setengah matang jelas lebih rendah daripada buah matang dan mentah sehingga menimbulkan galat hitung, dan ini rencananya diperbaiki dengan modifikasi model atau pencitraan spektral. Kumpulan data (808 citra dan 21 klip video) serta konfigurasi kamera mungkin belum mewakili keragaman kondisi lapangan, misalnya pencahayaan ekstrem atau oklusi berat. Fungsi sistem masih dalam tahap pengembangan, cakupan aplikasinya terbatas, dan biaya perangkatnya tinggi. Data tersedia atas permintaan kepada penulis korespondensi.

Menurut pembacaan ringkasan ini, terdapat beberapa hal yang perlu dicermati. Pertama, MCE dihitung per video lalu dirata-ratakan, sehingga galat positif dan negatif tidak saling meniadakan dalam satu video, tetapi MCE kelas pada Tabel 5 (12,3% sampai 17,3%) seluruhnya lebih tinggi daripada MCE gabungan (6,6%) tanpa penjelasan di teks tentang cara galat antarkelas saling mengimbangi pada hitungan total. Kedua, nilai MCE metode usulan berbeda antara set validasi (6,1%, Tabel 3) dan set uji (6,6%, Tabel 4); PSO dioptimalkan pada set video yang disebut sebagai set latih, sedangkan Tabel 3 dilaporkan pada set validasi, dan teks tidak merinci pembagian videonya per segmen. Ketiga, rujukan hitungnya adalah hitung manual pada video sehingga tidak dapat dibandingkan dengan hasil panen. Keempat, hanya sembilan video uji dari satu lokasi dan satu rumah kaca yang dipakai, dan klaim "*state-of-the-art*" pada kesimpulan tidak didukung perbandingan dengan sistem lain pada data yang sama selain Bytetrack dan lintas-garis. Kelima, kamera bergerak sejajar barisan tanaman dengan satu pandang sehingga buah yang tersembunyi pada sisi lain tanaman tidak ditangani.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat pada banyak bingkai video berurutan. Mekanismenya adalah pelacakan multi-objek (*multi-object tracking*) dengan Bytetrack (filter Kalman dan pencocokan Hungarian), kemudian aturan pencacahan yang hanya mencatat sebuah ID sekali, yaitu saat kotak memasuki wilayah hitung di tengah bidang pandang. Identitas dipertahankan lintas bingkai dalam satu lintasan kamera, bukan lintas sisi tanaman yang berbeda: kamera bergerak lurus di sepanjang barisan pada jarak sekitar 1,2 m dan tidak ada pencocokan antar-sisi atau antar-pandang yang terpisah. Teks tidak menyebut penanganan buah yang terlihat dari sisi berlawanan barisan.

Hitungan dilaporkan per kelas kematangan (matang, setengah matang, mentah) dengan MP, ME, MR, dan MCE tiap kelas (Tabel 5), sehingga bentuk keluarannya mirip inventaris per kelas. Acuan hitungnya adalah hitung manual pada video (disebut *ground truth (manual counts)*), bukan hasil panen dan bukan anotasi citra tunggal. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan wilayah hitung yang lebarnya dioptimalkan terhadap galat, pelaporan MR dan ME per kelas untuk memisahkan hitungan ganda dari deteksi keliru, serta temuan bahwa kelas perantara (setengah matang) memicu pergantian label dan hitungan ganda. Metode ini mengandaikan kamera bergerak sejajar objek, sehingga tidak langsung berlaku bagi pengambilan citra statis dari beberapa sisi pohon.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `wang2025tomato`.

Wang dkk. (2025) mengusulkan sistem estimasi hasil tomat rumah kaca yang menggabungkan YOLO11n ringan (blok C3k2-F, DSConv, dan GIoU; 2,66 M parameter, 8,0 GFLOPs) dengan metode pelacakan-pencacahan berbasis wilayah yang lebar wilayahnya dioptimalkan dengan PSO (876 piksel). Pada sembilan video uji, MCE sebesar 6,6% dicapai, dibandingkan 11,6% untuk Bytetrack dan 8,7% untuk hitung lintas-garis. Hitungan dilaporkan per kelas kematangan, dengan akurasi paling rendah pada kelas setengah matang, dan acuan hitungnya adalah hitung manual pada video.

Catatan verifikasi data: Angka jaringan terdapat pada Tabel 1 (ablasi) dan Tabel 2 (perbandingan jaringan) beserta Bagian 3.1 dan 3.2. Teks ekstraksi memuat kedua tabel itu sebagai kolom terurut sehingga pemetaan sel ke kolom dilakukan dari urutan baris dan sesuai dengan angka yang disebut pada narasi (misalnya 91,3; 86,2; 93,3; 65,8 untuk *box*). Angka optimasi PSO (lebar 876, nilai kebugaran sekitar 2,5, 200 iterasi) dari Bagian 3.3 dan keterangan Gambar 10 dan 11. Angka MCE pencacahan dari Tabel 3 (set validasi video), Tabel 4 (perbandingan tiga metode), dan Tabel 5 (per kelas). Selisih 5,0 dan 2,1 poin persentase sesuai pernyataan pada abstrak dan konsisten dengan Tabel 4. Hal yang tidak dapat diverifikasi dari teks: jumlah tomat sebenarnya pada set uji video, jumlah tanaman dan kultivar, jumlah buah per kelas pada anotasi citra, serta pembagian persis segmen video ke set latih, validasi, dan uji pada tiap tabel. Teks ekstraksi tidak rusak; gambar tidak tersedia.
