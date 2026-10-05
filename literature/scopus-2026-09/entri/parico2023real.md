# Real-Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `parico2023real` |
| Judul asli | Real-Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT |
| Penulis | Parico, Addie Ira Borja; Ahamed, Tofael |
| Tahun | 2023 |
| Venue | Iot and AI in Agriculture Self Sufficiency in Food Production to Achieve Society 5 0 and Sdgs Globally |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pear |

## Tautan Akses
- PDF: [parico2023real.pdf](../pdf/parico2023real.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-19-8113-5_11

## Gambaran Umum
Makalah ini membangun penghitung buah pir waktu nyata berbasis citra RGB saja untuk aplikasi telepon seluler. Penghitung terdiri atas detektor YOLOv4 (tiga varian: YOLOv4, YOLOv4-CSP, YOLOv4-tiny, masing-masing pada beberapa ukuran jaringan) dan pelacak multi-objek (*multi-object tracking*, MOT) Deep SORT. Data berasal dari video pohon pir sistem pohon-sambung (*joint-tree*) di kebun seluas 0,15 ha milik Universitas Tsukuba, Jepang, yang direkam dari sisi bawah pohon. Makalah juga menawarkan panduan sistematis untuk memilih model deteksi pada aplikasi pertanian, termasuk skema pembagian data empat bagian dan analisis galat.

Pada set uji, YOLOv4-CSP-608 memberi AP50 terbaik, yaitu 98,32% (abstrak menyebut 98%), sedangkan YOLOv4-tiny berjalan lebih dari 50 FPS dengan 6,8 sampai 14,5 BFLOPs. YOLOv4-512 dipilih sebagai kompromi (AP50 96,64%, 37,3 FPS, *false negative rate* 6%) untuk digabungkan dengan Deep SORT. Dua cara pencacahan dibandingkan pada satu video uji ponsel berdurasi 32 detik: metode ID unik menghasilkan F1count 87,85%, sedangkan metode garis wilayah minat (*region of interest*, ROI) menghasilkan F1count 72,94%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Petani pir di Jepang menghitung hasil panen secara manual dan mengalami kehilangan pascapanen yang tinggi akibat buah mudah rusak dan pengemasan; keputusan cepat juga diperlukan saat cuaca ekstrem seperti topan. Aplikasi telepon seluler untuk menghitung pir waktu nyata membutuhkan metode deteksi yang cepat, akurat, dan ringan secara komputasi. Video dari bawah pohon menimbulkan kontras tinggi, tantangan pencahayaan, dan oklusi.

Penulis menunjuk tiga kekurangan pada penelitian deteksi buah berbasis YOLO sebelumnya: tidak ada yang mempertimbangkan akurasi, kecepatan inferensi, dan biaya komputasi sekaligus; sebagian besar tidak melaporkan kurva *loss* sehingga *overfitting* atau *underfitting* sulit diperiksa; dan penelitian hanya berfokus pada deteksi, bukan pencacahan waktu nyata. Satu penelitian terdahulu (Itakura dkk.) memadukan YOLOv2 dengan filter Kalman untuk menghitung pir dengan F1 0,972, tetapi kecepatannya tidak dilaporkan dan tidak jelas apakah pelacakannya daring atau luring. Deteksi saja untuk pencacahan dinilai rawan galat karena kedip deteksi (*flickering*), kegagalan pada oklusi, dan pencahayaan sulit.

## Ide Utama
Gagasan makalah adalah menjadikan pelacakan sebagai cadangan terhadap kelemahan deteksi per bingkai: detektor YOLOv4 menghasilkan kotak per bingkai, Deep SORT menetapkan identitas (ID) unik per objek, dan jumlah pir diperoleh dari jumlah ID unik atau dari jumlah pusat objek yang melewati garis ROI. Deep SORT memperluas SORT (filter Kalman dan algoritme Hungaria) dengan metrik penampilan dari jaringan konvolusi sehingga lebih tahan terhadap oklusi dan perubahan sudut pandang.

Gagasan kedua bersifat metodologis: pemilihan model dilakukan terhadap tiga target sekaligus (akurasi, kecepatan minimal 24 FPS, biaya komputasi dalam FLOPs dan memori GPU), dengan pembagian data empat bagian dan analisis galat bertahap.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Video direkam dengan kamera telepon seluler (1920 x 1080, 30 FPS, 29 Juli 2020, pukul 12-13, berawan) dan DJI Osmo Pocket (3840 x 2160, 60 FPS, 6 Agustus 2020, pukul 9-10, berawan sebagian) di Tsukuba-Plant Innovation Research Center, Ibaraki. Kultivar pir tidak dilaporkan. Video diubah menjadi bingkai dengan filter *scene* VLC setiap setengah detik. Bingkai tanpa pir dibuang, tersisa 314 citra resolusi 4K dan 134 citra 1920 x 1088 (total 448 citra).

### 2. Pelabelan dan augmentasi
Kotak pembatas dilabeli di Supervisely dan dikonversi dengan Roboflow. Augmentasi pada citra 4K mencakup pembalikan acak, kecerahan -25% sampai +25%, gamma -20% sampai +20%, dan *coarse dropout* hingga 6% piksel. Citra diubah ukurannya menjadi 416, 512, dan 608 dengan padding hitam. Setelah augmentasi, dataset menjadi 1.337 citra.

### 3. Pembagian data
Karena distribusi tidak seragam (pelatihan memakai resolusi tinggi, sasaran adalah citra ponsel beresolusi rendah), data dibagi 70:10:10:10 menjadi himpunan pelatihan, validasi-pelatihan (*train-val*, resolusi tinggi tak terlihat), validasi, dan uji. Himpunan validasi dan uji berisi citra ponsel. Jumlah citra per himpunan tidak dilaporkan secara eksplisit di teks.

### 4. Pelatihan dan analisis galat
Pelatihan memakai Darknet pada Google Colab dengan GPU Tesla T4 selama 6.000 iterasi (pemanasan linear 1.000 iterasi, penurunan laju belajar bertahap pada iterasi 4.800 dan 5.400 dengan laju penurunan 0,1, $LR_0$ 0,001 untuk YOLOv4 dan YOLOv4-CSP serta 0,00261 untuk YOLOv4-tiny, momentum 0,949, *weight decay* 0,0005, kerugian lokalisasi CIoU, *anchor* kustom dari k-means). Tahap kedua adalah *fine-tuning* untuk memastikan bobot terbaik telah mencapai mAP maksimum. Analisis galat membandingkan AP50 pada himpunan validasi-pelatihan, validasi, dan uji untuk memeriksa bias, *overfitting*, ketidakcocokan distribusi, dan *overfitting* pada validasi. Augmentasi diterapkan pada himpunan validasi-pelatihan untuk meniru kualitas citra ponsel.

### 5. Pencacahan dengan Deep SORT
Model terpilih diubah ke format TensorFlow dan dijalankan bersama Deep SORT pada satu video uji ponsel yang tidak terlihat sebelumnya (1080 x 1920, 30 FPS, 32 detik) pada laptop dengan Intel Core i7-7700HQ, RAM 16 GB, dan NVIDIA GTX 1060. Dua metode dibandingkan: (1) ROI, yaitu jumlah pusat objek terlacak yang melewati garis horizontal pada 50% tinggi video (hasil uji beberapa posisi garis); (2) ID unik, yaitu jumlah ID yang dihasilkan Deep SORT. Metrik pencacahan mengikuti CLEAR MOT yang dimodifikasi; karena objek tidak bergerak, ketidakcocokan identitas (*mismatches*) diset nol.

## Eksperimen dan Hasil
Detektor dievaluasi pada himpunan uji citra ponsel (ambang IoU 0,5 dan ambang keyakinan 0,25 untuk FN; Tabel 7 memakai ambang keyakinan 0,5). Hasil AP50 pada tiga himpunan (Tabel 7), serta kecepatan dan biaya komputasi (Tabel A3):

| Model | AP50 train-val | AP50 val | AP50 uji | F1 uji | FPS | BFLOPs |
|---|---|---|---|---|---|---|
| YOLOv4-tiny-416 | 83,78 | 92,91 | 94,09 | 0,93 | 59,4 | 6,789 |
| YOLOv4-tiny-512 | 86,23 | 93,08 | 93,53 | 0,93 | 54,4 | 10,283 |
| YOLOv4-tiny-608 | 87,61 | 92,11 | 94,19 | 0,94 | 50,3 | 14,500 |
| YOLOv4-416 | 90,39 | 93,72 | 93,76 | 0,94 | 46,1 | 59,571 |
| YOLOv4-512 | 92,86 | 94,61 | 96,64 | 0,97 | 37,3 | 90,235 |
| YOLOv4-608 | 91,32 | 95,39 | 96,76 | 0,97 | 26,4 | 127,232 |
| YOLOv4-CSP-512 | 92,74 | 93,48 | 97,16 | 0,96 | 21,4 | 76,142 |
| YOLOv4-CSP-608 | 92,60 | 94,51 | 98,32 | 0,98 | 20,1 | 107,359 |

Pada Tabel 8 dan A3, YOLOv4-CSP-608 memiliki *recall* 0,95 (FN 14 dari 300 pada penghitungan TP+FN = 286+14), sedangkan YOLOv4-512 memiliki *recall* 0,94 (TP 283, FP 0, FN 17). Presisi sebagian besar model 0,98 sampai 1,00. Hanya YOLOv4-512, YOLOv4-416, dan YOLOv4-tiny memenuhi syarat 24 FPS atau lebih bersama YOLOv4-608 (26,4 FPS); YOLOv4-CSP-512 21,4 FPS dan YOLOv4-CSP-608 20,1 FPS tidak memenuhinya. YOLOv4-tiny memerlukan sekitar 2 GB memori GPU saat inferensi (2,07 sampai 2,15 GB pada Tabel A3).

Hasil pencacahan pada video uji 32 detik (Tabel 9):

| Metrik (%) | ID unik | Garis ROI |
|---|---|---|
| MOTA | 75,47 | 56,60 |
| FN rate | 11,32 | 41,51 |
| FP rate | 13,21 | 1,89 |
| Precision count | 87,04 | 96,88 |
| Recall count | 88,68 | 58,49 |
| F1 count | 87,85 | 72,94 |

Pada metode ROI, 73% dari hitungan yang terlewat sebenarnya telah terdeteksi oleh YOLOv4: 50% terdeteksi hanya setelah melewati garis, dan 23% terdeteksi sebelum atau saat melewati garis (Gambar 23). Penulis mengaitkan kelompok pertama dengan keterbatasan komputasi dan kelompok kedua dengan ketergantungan Deep SORT pada informasi penampilan di bawah pencahayaan sulit dan oklusi.

## Kelebihan dan Keterbatasan
Kelebihan: perbandingan sistematis tiga varian dan beberapa ukuran jaringan menurut akurasi, kecepatan, dan memori; skema pembagian data yang menangani ketidakcocokan resolusi; kurva *loss* dan analisis galat dilaporkan; pencacahan dievaluasi dengan metrik berbasis CLEAR MOT, dengan dua aturan hitung yang dibandingkan.

Keterbatasan yang dinyatakan atau tersirat dalam teks penulis: ROI sensitivitas rendah akibat kedip deteksi dan keterlambatan deteksi; Deep SORT bergantung pada penampilan sehingga lemah pada pencahayaan sulit dan oklusi (penulis menyarankan memprioritaskan informasi gerak); YOLOv4-tiny masih memerlukan sekitar 2 GB memori GPU sehingga ponsel kelas bawah tidak dapat memakainya; inferensi akurasi tertinggi disarankan berjalan di cloud dan memerlukan internet; penulis menyarankan menghitung ID yang bertahan lebih dari 80% masa hidup untuk mengurangi kedip.

Menurut pembacaan ringkasan ini, ada keterbatasan lain. Pertama, evaluasi pencacahan hanya memakai satu video 32 detik tanpa pengulangan, sehingga hasil F1count 87,85% dan 72,94% tidak memiliki ukuran ketidakpastian. Kedua, jumlah pir acuan pada video uji tidak disebutkan; persentase pada Tabel 9 konsisten dengan acuan 53 buah (misalnya 1,89% setara 1 dari 53 dan 58,49% setara 31 dari 53), tetapi angka 53 adalah turunan ringkasan ini, bukan nilai yang tertulis di teks. Ketiga, acuan hitungan dan cara pengambilannya (manual dari video atau hitung lapangan) tidak dijelaskan. Keempat, pemilihan YOLOv4-512 dilakukan setelah membandingkan beberapa model pada himpunan uji yang sama, dan jumlah citra tiap himpunan data tidak dilaporkan. Kelima, makalah memakai AP 11 titik gaya PASCAL VOC dan memutuskan ambang pada himpunan uji, bukan pada protokol COCO.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam video yang direkam satu pandang bergerak. Mekanismenya adalah pelacakan video dengan Deep SORT (filter Kalman, asosiasi Hungaria, dan metrik penampilan CNN) yang memberi ID unik, kemudian hitungan diambil dari jumlah ID unik atau dari jumlah objek yang melewati garis ROI (kode C1, pelacakan video). Penulis mencatat bahwa objek tidak bergerak, sehingga ketidakcocokan identitas diset nol; makalah tidak mengukur pergantian ID (*ID switch*) sungguhan. Tidak ada pencocokan lintas sisi pohon atau rekonstruksi 3D.

Hitungan dilaporkan untuk satu kelas (pir) dan tidak per kelas. Acuan hitungan tidak dijelaskan (lihat keterbatasan di atas). Pelajaran yang dapat dipindahkan ke pencacahan tandan sawit multisisi: metode ID unik yang lebih peka lebih cocok untuk recall dibanding garis ROI yang sempit, keputusan hitungan berdasarkan lama hidup ID (lebih dari 80% masa hidup) untuk menekan kedip, dan kebutuhan mengevaluasi detektor pada data dengan distribusi sasaran. Hasil ini tidak membuktikan identitas lintas pandang antar sisi pohon karena video hanya satu lintasan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `parico2023real`.

Parico dan Ahamed (makalah dimuat pada *Sensors* 2021, 21, 4803) membangun penghitung pir waktu nyata dari video RGB dengan YOLOv4 dan Deep SORT pada kebun pir sistem pohon-sambung, serta membandingkan YOLOv4, YOLOv4-CSP, dan YOLOv4-tiny pada tiga ukuran jaringan. YOLOv4-CSP-608 mencapai AP50 uji 98,32%, YOLOv4-512 dipilih sebagai kompromi (AP50 96,64%, 37,3 FPS), dan pada satu video uji pencacahan dengan ID unik memberi F1count 87,85% dibanding 72,94% untuk garis ROI.

Catatan verifikasi data: AP50 pada Tabel 7; P, R, F1, AP25/50/75, BFLOPs, FPS, memori, serta TP, FP, FN pada Tabel 8 dan A3; metrik pencacahan pada Tabel 9; rincian 73%, 50%, dan 23% pada Bagian 4.8 (Gambar 23); jumlah citra (314, 134, 448, 1.337) pada Bagian 3.2. Kunci BibTeX berawalan 2023, sedangkan teks yang dibaca adalah artikel *Sensors* 2021; perbedaan tahun itu tidak dapat dijelaskan dari teks. Tabel di teks hasil ekstraksi tersaji per sel sehingga susunan kolom dibaca dari urutan sel, dan kolom FPS, BFLOPs, serta TP/FP/FN pada Tabel A3 dipetakan dari urutan sel tersebut. Jumlah citra tiap himpunan dan acuan hitungan video uji tidak dilaporkan di teks.
