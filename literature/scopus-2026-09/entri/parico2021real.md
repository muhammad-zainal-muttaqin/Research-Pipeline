# Real time pear fruit detection and counting using yolov4 models and deep sort

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `parico2021real` |
| Judul asli | Real time pear fruit detection and counting using yolov4 models and deep sort |
| Penulis | Parico, Addie Ira Borja; Ahamed, Tofael |
| Tahun | 2021 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pear |

## Tautan Akses
- PDF: [parico2021real.pdf](../pdf/parico2021real.pdf)
- DOI resmi: https://doi.org/10.3390/s21144803

## Gambaran Umum

Makalah ini membangun penghitung buah pir (*pear*) waktu-nyata untuk aplikasi telepon seluler yang hanya memakai citra RGB. Sistem terdiri dari dua bagian: detektor objek keluarga YOLOv4 (YOLOv4, YOLOv4-CSP, dan YOLOv4-tiny, masing-masing pada beberapa resolusi jaringan) dan algoritma pelacakan multi-objek (*multi-object tracking*, MOT) Deep SORT. Selain itu, penulis mengusulkan prosedur sistematis untuk memilih model deteksi pada penelitian pertanian, mencakup penetapan metrik target, skema pembagian data empat bagian, dan analisis galat bertahap.

Data berasal dari video kebun pir sistem pohon sambung (*joint-tree*) seluas 0,15 ha di Tsukuba-Plant Innovation Research Center, Universitas Tsukuba, Jepang. Video diambil dari sisi bawah pohon dengan dua kamera pada dua hari berbeda. Hasil video diubah menjadi 448 citra, lalu diperluas melalui augmentasi menjadi 1.337 citra. Kultivar pir tidak dilaporkan.

Hasil utama: YOLOv4-CSP-608 menghasilkan AP50 uji 98,32 dengan F1 0,98, sedangkan YOLOv4-512 dipilih sebagai model penghitung karena seimbang antara akurasi (AP50 uji 96,64), kecepatan (37,3 FPS), dan biaya komputasi. Pada satu video uji berdurasi 32 detik, penghitungan berbasis ID unik Deep SORT mencapai F1count 87,85%, sedangkan penghitungan berbasis garis *region of interest* (ROI) mencapai 72,94%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Petani pir di Jepang menghitung hasil panen secara manual dan mengalami kehilangan pascapanen yang relatif tinggi akibat daya simpan buah yang pendek. Keputusan cepat juga diperlukan ketika terjadi cuaca ekstrem seperti topan. Penulis menginginkan aplikasi telepon seluler yang menghitung pir secara waktu-nyata, sehingga detektornya harus cepat, akurat, dan tidak mahal secara komputasi. Video yang diambil dari bawah pohon menimbulkan kesulitan berupa pencahayaan kontras tinggi dan oklusi.

Penulis menunjukkan tiga kekurangan pada studi terdahulu yang memakai YOLO untuk deteksi buah. Pertama, tidak ada studi yang mempertimbangkan akurasi deteksi, kecepatan inferensi, dan biaya komputasi secara bersamaan. Kedua, sebagian besar studi tidak melaporkan kurva *loss*, sehingga *overfitting* atau *underfitting* sulit diperiksa. Ketiga, studi terdahulu berfokus pada deteksi dan tidak menangani penghitungan waktu-nyata. Satu studi yang menggabungkan YOLO dengan filter Kalman untuk menghitung pir (F1 0,972) tidak menyebut kecepatan sistem maupun apakah pelacakannya daring (*online*) atau luring (*offline*).

Penghitungan murni dari jumlah deteksi dinilai rentan karena deteksi dapat berkedip (*flickering*) antarbingkai dan gagal pada oklusi atau pencahayaan sulit. Pelacakan dipakai sebagai cadangan agar setiap deteksi memperoleh ID unik.

## Ide Utama

Gagasan intinya adalah memadukan detektor YOLOv4 yang dipilih secara sistematis dengan Deep SORT, yaitu pelacak daring yang menggabungkan metrik gerak (filter Kalman dan algoritma Hungarian) dengan metrik penampilan berbasis jaringan konvolusi. Jumlah pir dihitung dari pelacakan, bukan dari jumlah deteksi per bingkai. Dua cara penghitungan dibandingkan: jumlah ID unik, dan jumlah titik pusat objek terlacak yang melewati garis horizontal ROI.

Kontribusi kedua bersifat metodologis. Model dipilih berdasarkan tiga target sekaligus: akurasi (AP), kecepatan (target paling sedikit 24 FPS sebagai batas waktu-nyata), dan biaya komputasi (FLOPs serta memori GPU). Penulis juga mengusulkan pembagian data 70:10:10:10 untuk kasus ketidakcocokan distribusi antara data latih (resolusi tinggi) dan data target (citra telepon seluler beresolusi lebih rendah).

## Cara Kerja Langkah demi Langkah

```
 Video ──> bingkai tiap 0,5 detik ──> anotasi kotak ──> augmentasi
                                                           │
   Tahap-1 (6.000 iterasi) ──> Tahap-2 (penyetelan halus) ──┘
                │
        analisis galat (A–D) ──> pilih model (AP, FPS, FLOPs)
                │
   YOLOv4-512 + Deep SORT ──> hitung ID unik / lintasan garis ROI
```

### 1. Akuisisi data

Video direkam dengan dua perangkat: kamera ponsel (sensor CMOS 16 MP, 1920 × 1080, 30 FPS, pada 29 Juli 2020, pukul 12–13, berawan) dan DJI Osmo Pocket (3840 × 2160, 60 FPS, pada 6 Agustus 2020, pukul 9–10, berawan sebagian). Lokasi: kebun pir sistem pohon sambung seluas 0,15 ha di Tsukuba, Ibaraki (36°06′56,8″ LU, 140°05′37,7″ BT). Jumlah pohon yang direkam tidak dilaporkan. Video diambil dari sisi bawah pohon.

### 2. Persiapan data

Bingkai diekstrak dengan filter "Scene video" pada VLC setiap setengah detik (setiap 30 bingkai untuk video 60 FPS dan setiap 15 bingkai untuk video 30 FPS). Citra tanpa pir dibuang, menyisakan 314 citra 4K dan 134 citra 1920 × 1088 (total 448). Anotasi kotak pembatas dibuat dengan Supervisely, lalu dikonversi dengan Roboflow. Augmentasi pada citra 4K meliputi pembalikan acak, kecerahan ±25%, gamma ±20%, dan *coarse dropout* hingga 6% piksel. Citra diubah ukuran menjadi 416 × 416, 512 × 512, dan 608 × 608 dengan bantalan hitam agar rasio aspek tetap. Dataset menjadi 1.337 citra.

### 3. Pembagian data

Karena data latih berupa citra resolusi tinggi sedangkan sasaran adalah citra ponsel, data dibagi dengan rasio 70:10:10:10 menjadi data latih, latih-validasi (*train-val*), validasi, dan uji. Data latih dan latih-validasi berisi citra resolusi tinggi. Data validasi dan uji berisi citra ponsel. Data latih-validasi diaugmentasi untuk meniru kualitas citra yang lebih rendah.

### 4. Model dan pelatihan

Tiga varian dibandingkan. YOLOv4 memakai tulang punggung CSPDarknet53 dengan aktivasi Mish, leher PANet dengan Leaky ReLU, dan modul SPP. YOLOv4-CSP memakai CSPDarknet53 dengan Mish, leher CSPPANet, dan CSPSPP. YOLOv4-tiny memakai CSPOSANet dengan Leaky ReLU dan leher FPN. Pelatihan memakai kerangka Darknet pada Google Colab dengan GPU Tesla T4, jangkar kustom dari *k-means*, dan augmentasi saat pelatihan. Tahap-1 berjalan 6.000 iterasi dengan pemanasan linear 1.000 iterasi, peluruhan multilangkah (laju 0,1 pada iterasi 4.800 dan 5.400), laju belajar awal 0,001 (YOLOv4 dan YOLOv4-CSP) atau 0,00261 (YOLOv4-tiny), *momentum* 0,949, *weight decay* 0,0005, ukuran *batch* 64, dan *loss* lokalisasi CIoU. Tahap-2 berupa penyetelan halus untuk memastikan bobot dengan mAP terbaik dari Tahap-1 telah mencapai nilai maksimum (Algoritma A1 di lampiran).

### 5. Analisis galat dan pemilihan model

Galat dibandingkan berpasangan antartahap A sampai D (galat sasaran, latih, latih-validasi, validasi, uji) untuk menilai bias, *overfitting* pada data latih, ketidakcocokan distribusi, dan *overfitting* pada data validasi. Model dibandingkan pada data uji dengan kriteria: metrik tertinggi, kecepatan inferensi mendekati atau di atas 24 FPS, dan konsumsi GPU.

### 6. Penghitungan dengan Deep SORT

Model terpilih dikonversi ke TensorFlow dan dijalankan bersama Deep SORT pada satu video ponsel uji yang belum pernah dilihat (1080 × 1920, 32 detik, 30 FPS) pada laptop dengan Intel Core i7-7700HQ, RAM 16 GB, dan NVIDIA GeForce GTX 1060. Metode ROI menghitung titik pusat objek terlacak yang melewati garis horizontal pada 50% tinggi video (nilai optimal dari beberapa ROI yang diuji). Metode ID unik menghitung jumlah ID berbeda yang dihasilkan Deep SORT. Metrik penghitungan: presisi, *recall*, F1, dan MOTA, dengan *mismatch* ditetapkan nol karena objek tidak bergerak.

## Eksperimen dan Hasil

Evaluasi deteksi memakai metrik Pascal VOC (IoU 0,5, ambang keyakinan 0,25 untuk FN pada perhitungan TP/FP/FN, dan AP dengan interpolasi 11 titik). Jumlah citra pada tiap bagian pembagian data tidak dilaporkan terpisah. Tabel berikut merangkum hasil deteksi pada data uji (Tabel 7, 8, dan A3 makalah).

| Model | P | R | F1 | AP50 uji | FPS | Memori inferensi (GB) | BFLOPs |
|---|---|---|---|---|---|---|---|
| YOLOv4-tiny-416 | 1,00 | 0,87 | 0,93 | 94,09 | 59,4 | 2,07 | 6,789 |
| YOLOv4-tiny-512 | 0,98 | 0,88 | 0,93 | 93,53 | 54,4 | 2,11 | 10,283 |
| YOLOv4-tiny-608 | 1,00 | 0,89 | 0,94 | 94,19 | 50,3 | 2,15 | 14,500 |
| YOLOv4-416 | 0,98 | 0,90 | 0,94 | 93,76 | 46,1 | 2,60 | 59,571 |
| YOLOv4-512 | 1,00 | 0,94 | 0,97 | 96,64 | 37,3 | 2,78 | 90,235 |
| YOLOv4-608 | 1,00 | 0,94 | 0,97 | 96,76 | 26,4 | 3,04 | 127,232 |
| YOLOv4-CSP-512 | 1,00 | 0,92 | 0,96 | 97,16 | 21,4 | 2,62 | 76,142 |
| YOLOv4-CSP-608 | 1,00 | 0,95 | 0,98 | 98,32 | 20,1 | 2,79 | 107,359 |

Data latih-validasi menghasilkan AP50 antara 83,78 dan 92,86, sedangkan data validasi antara 92,11 dan 95,39 (Tabel 7). Penulis menyimpulkan bahwa ketidakcocokan antara data resolusi tinggi dan rendah teratasi dan tidak terjadi *overfitting* pada data validasi, karena AP50 meningkat dari validasi ke uji. YOLOv4-CSP-608 terbaik pada hampir semua metrik tetapi kecepatannya 20,1 FPS, di bawah batas 24 FPS. YOLOv4-608 (26,4 FPS) adalah model paling akurat yang masih memenuhi batas waktu-nyata menurut Subbab 4.3, tetapi kesimpulan akhir memilih YOLOv4-512 (AP > 96%, 37,3 FPS, FNR 6%) sebagai detektor penghitung. Pada metrik ketat AP75, YOLOv4-tiny-608 (80,12) sebanding atau lebih baik daripada YOLOv4-416 (79,61). Ukuran bobot model YOLOv4-tiny sekitar 22,96 MB, sedangkan YOLOv4 sekitar 250 MB dan YOLOv4-CSP sekitar 205 MB (Tabel 6).

Hasil penghitungan pada video uji (Tabel 9):

| Metrik penghitungan (%) | ID unik | Garis ROI |
|---|---|---|
| MOTA | 75,47 | 56,60 |
| FN rate | 11,32 | 41,51 |
| FP rate | 13,21 | 1,89 |
| Presisi | 87,04 | 96,88 |
| *Recall* | 88,68 | 58,49 |
| F1 | 87,85 | 72,94 |

Metode ID unik lebih sensitif dan menghasilkan F1 lebih tinggi. Metode ROI lebih ketat sehingga presisinya tinggi, tetapi *recall* rendah. Pada rincian FN metode ROI (Gambar 23), 73% pir yang terlewat sebenarnya terdeteksi YOLOv4. Dari seluruh FN tersebut, 50% terdeteksi hanya setelah melewati garis ROI dan 23% terdeteksi sesaat sebelum atau ketika melewati garis. Penulis mengaitkan kasus pertama dengan keterbatasan sumber daya komputasi dan kasus kedua dengan ketergantungan Deep SORT pada informasi penampilan saat pencahayaan sulit dan oklusi meningkat. Total pir acuan pada video uji tidak disebutkan dalam teks yang tersedia (nilai MOTA dan laju kesalahan hanya diberikan sebagai persentase).

Pengamatan kualitatif (Gambar 19 sampai 22): pada oklusi ringan semua model mendeteksi pir; pada oklusi tinggi dengan pencahayaan baik hanya model YOLOv4-CSP yang berhasil; pir kecil yang terokulasi hanya terdeteksi baik oleh YOLOv4-608 dan 512.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: prosedur pemilihan model mempertimbangkan akurasi, kecepatan, dan biaya komputasi sekaligus; kurva *loss* dan analisis galat dilaporkan sehingga *overfitting* dapat diperiksa; penghitungan memakai pelacak daring yang cocok untuk waktu-nyata; dan dua strategi penghitungan dibandingkan dengan metrik yang jelas.

Keterbatasan yang dinyatakan penulis: pelacakan Deep SORT dapat gagal pada pencahayaan sulit dan oklusi tinggi karena bergantung pada penampilan, sehingga penulis menyarankan memprioritaskan informasi gerak; deteksi berkedip membuat metode ROI melewatkan pir yang sebenarnya terdeteksi; bahkan YOLOv4-tiny membutuhkan sekitar 2 GB GPU sehingga ponsel kelas bawah tidak dapat memakainya; inferensi lokal pada ponsel tidak cocok untuk model akurasi tertinggi, sehingga komputasi awan disarankan dengan syarat sambungan internet. Penulis menyarankan menghitung ID yang bertahan selama periode tertentu (misalnya lebih dari 80% masa hidup) untuk mengurangi dampak kedipan.

Menurut pembacaan ringkasan ini, evaluasi penghitungan hanya memakai satu video berdurasi 32 detik sehingga angka F1count dan MOTA tidak dapat digeneralisasi, dan tidak ada interval kepercayaan atau ulangan. Menurut pembacaan ringkasan ini, pengukuran kecepatan dan memori diambil pada perangkat dan kerangka berbeda (Tesla T4 untuk deteksi, GTX 1060 untuk penghitungan), sedangkan ponsel sebagai target aplikasi tidak diuji. Menurut pembacaan ringkasan ini, Tabel 7 memuat AP50 uji yang lebih tinggi daripada AP50 validasi untuk sebagian besar model, yang dapat mencerminkan ukuran data uji yang kecil, dan pembagian data tidak dirinci jumlah citranya. Penghitungan dari satu pandang bergerak pada objek diam dengan ID yang dapat terduplikasi bila pelacak kehilangan jejak tidak dikoreksi oleh mekanisme lain.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari satu kali dalam urutan bingkai video yang bergerak. Mekanismenya adalah pelacakan multi-objek: Deep SORT memberi ID unik pada tiap deteksi dengan menggabungkan prediksi gerak (filter Kalman, algoritma Hungarian) dan fitur penampilan, lalu hitungan diperoleh dari jumlah ID unik atau dari lintasan titik pusat melewati garis ROI. Mekanisme ini bekerja dalam satu lintasan video menerus dari bawah pohon, bukan pencocokan identitas lintas sisi pohon yang direkam terpisah. Perilaku pelacak saat objek keluar lalu masuk kembali ke bingkai (identitas diganti) tidak dianalisis; kesalahan terkait ID dinilai hanya melalui FP dan FN penghitungan.

Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas (pir). Acuan hitungan adalah penghitungan pada video uji; makalah tidak menyatakan secara rinci apakah acuan berasal dari hitungan manual di lapangan atau dari pengamatan video, dan jumlah total acuan tidak tertulis dalam teks. Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah pola detektor kemudian pelacak daring, pembandingan hitungan ID unik dengan hitungan garis ROI, serta pengamatan bahwa kedipan deteksi mengurangi *recall* metode ROI. Pola itu tidak menyelesaikan pencocokan identitas antarsisi pohon yang tidak berurutan dalam satu video, dan penerapan per kelas memerlukan atribut kelas pada tiap lintasan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `parico2021real`.

Ringkasan yang aman dikutip: Parico dan Ahamed (2021) membangun penghitung pir waktu-nyata dari video RGB dengan detektor YOLOv4 dan pelacak Deep SORT. Di antara varian YOLOv4 pada data uji, YOLOv4-CSP-608 mencapai AP50 98,32 sedangkan YOLOv4-512 dipilih untuk penghitungan dengan AP50 96,64 dan 37,3 FPS. Pada satu video uji berdurasi 32 detik, penghitungan berdasarkan ID unik Deep SORT menghasilkan F1 87,85% dengan *recall* 88,68%, lebih baik daripada penghitungan garis ROI (F1 72,94%, *recall* 58,49%).

Catatan verifikasi data: Angka deteksi dibaca dari Tabel 7, Tabel 8, dan Tabel A3 (lampiran). Angka penghitungan dibaca dari Tabel 9 dan rincian FN dari Gambar 23 (teks Subbab 4.8). Parameter pelatihan berasal dari Subbab 3.7 dan Tabel A2. Jumlah citra (448 dan 1.337) berasal dari Subbab 3.2. Teks ekstraksi PDF terbaca baik, tetapi gambar, kurva, dan rumus tidak terbaca penuh; lampiran Algoritma A1 dan Tabel A4 di luar bagian yang dibaca, sehingga rincian penyetelan halus tidak diringkas. Total pir acuan pada video uji, kultivar, jumlah pohon, jumlah citra per bagian pembagian, dan cara pembuatan acuan hitungan tidak dapat diverifikasi dari teks. Ada perbedaan kecil di makalah: abstrak menyebut FLOPS 6,8–14,5 untuk YOLOv4-tiny, sedangkan Tabel A3 memberi 6,789 sampai 14,500 BFLOPs; ringkasan ini memakai Tabel A3.
