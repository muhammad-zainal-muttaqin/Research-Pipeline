# An improved framework based on tracking-by-detection for simultaneous estimation of yield and maturity level in cherry tomatoes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qi2024improved` |
| Judul asli | An improved framework based on tracking-by-detection for simultaneous estimation of yield and maturity level in cherry tomatoes |
| Penulis | Qi, Zhongxian; Zhang, Wenqiang; Yuan, Ting; Rong, Jiacheng; Hua, Wanjia; Zhang, Zhiqin; Deng, Xue; Zhang, Junxiong; Li, Wei |
| Tahun | 2024 |
| Venue | Measurement Journal of the International Measurement Confederation |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [qi2024improved.pdf](../pdf/qi2024improved.pdf)
- DOI resmi: https://doi.org/10.1016/j.measurement.2024.114117

## Gambaran Umum
Makalah ini mengusulkan kerangka berbasis *tracking-by-detection* untuk menghitung tandan tomat ceri (*cherry tomato*) di rumah kaca sekaligus memperkirakan tingkat kematangan tiap tandan. YOLOv8n mendeteksi tandan pada tiap bingkai video, Deep Sort memberi ID pada tiap tandan, dan NanoDet mendeteksi buah matang dan belum matang di dalam tandan. Nilai kematangan tandan ditentukan dari rasio jumlah buah matang terhadap total buah, lalu dikelompokkan menjadi lima tingkat. Modul fusi informasi menggabungkan hasil pelacakan dan kematangan, memakai metode penghitungan wilayah (*region counting*) untuk mengurangi galat akibat lompatan ID, dan memilih nilai kematangan dengan frekuensi kemunculan tertinggi pada bingkai-bingkai yang berbeda untuk tandan yang sama.

Data diambil di sebuah taman produksi tomat di Distrik Daxing, Beijing, pada Desember 2021 sampai Maret 2022, pada kultivar tomat ceri Hongfushi dalam rumah kaca bergaya Belanda. Hasil utama: akurasi hitung 92,79%, akurasi estimasi tingkat kematangan 90,84% (tanpa galat hitung) atau 84,29% (dengan galat hitung), dan laju proses rata-rata 15 bingkai per detik pada GPU NVIDIA RTX 2060.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengelolaan tomat ceri di rumah kaca pabrik memerlukan hitungan tandan dan kematangan yang cepat dan akurat, sedangkan pekerjaan manual padat karya. Pada citra rumah kaca, pencahayaan berubah-ubah, tandan saling menutupi, batang utama menghalangi tandan, dan tandan pada barisan di sebelahnya dapat salah dikenali. Penulis menyatakan metode yang ada umumnya mendeteksi kematangan buah individual pada seluruh citra, bukan kematangan satu tandan utuh, dan sebagian diuji hanya di laboratorium.

Penulis juga menyebut bahwa pelacak mengalami konversi ID (*ID jump*) yang menimbulkan galat hitung. Studi yang menggabungkan estimasi hasil (jumlah) dan kematangan sekaligus langka; satu-satunya yang ditemukan hanya memperoleh kedua informasi itu secara terpisah dan menganalisis kematangan secara kualitatif. Kombinasi YOLOv8 dan Deep Sort untuk jumlah tandan dinyatakan belum pernah diteliti.

## Ide Utama
Kerangka *tracking-by-detection* diperluas dengan modul estimasi kematangan dan modul fusi. Kematangan tandan tidak diklasifikasi langsung, melainkan dihitung dari proporsi buah matang dan belum matang dalam tandan, dan diperlakukan sebagai atribut yang melekat pada ID tandan. Karena satu tandan tampak dari sudut pandang berbeda pada bingkai-bingkai berbeda, estimasi kematangan per bingkai berubah-ubah akibat oklusi. Penulis memilih nilai tingkat kematangan dengan frekuensi tertinggi (modus) di antara bingkai-bingkai yang memuat ID yang sama, bukan nilai rata-rata. Lompatan ID dikoreksi dengan metode penghitungan wilayah yang dirujuk dari penelitian lain (Rong dkk.), sehingga jumlah ID tidak langsung dianggap jumlah tandan.

## Cara Kerja Langkah demi Langkah
```
 Bingkai video -> YOLOv8n (tandan) --+--> Deep Sort (ID tandan)
                                     |
                                     +--> potong ROI -> NanoDet (buah matang,
                                          belum matang) -> M = Nr/(Nr+Ng)
 ID + M -> modul fusi: penghitungan wilayah (jumlah tandan)
           + modus nilai kematangan per ID -> 5 tingkat
```

### 1. Akuisisi data
Perangkat akuisisi adalah Intel RealSense D435i pada kereta peron tinggi (kamera RGB 1280×720, 30 fps, sudut pandang 69° horizontal dan 42° vertikal, kamera diputar 90° sehingga citra beresolusi 720×1280). Kamera berjarak sekitar 0,6 m secara horizontal dari tandan dan 1 m secara vertikal dari tinggi rel. Jarak antarbaris tanam 1,5 m dan tiap tandan berisi sekitar 10 sampai 12 buah. Pengambilan dilakukan pada pagi, siang, dan sore dengan berbagai pose tandan. Terkumpul 2.127 citra asli untuk deteksi tandan dan 1.382 citra tandan terpotong untuk estimasi kematangan, masing-masing dibagi 8:2 menjadi data latih dan validasi dan dianotasi dengan LabelImg. Sebanyak 19 video sepanjang sekitar 30 detik (30 fps) dipakai untuk verifikasi penghitungan dan kematangan.

### 2. Detektor tandan
YOLOv8n dipilih; citra diubah ukurannya dari 720×1280 menjadi 416×416. Pelatihan 120 epoch (60 dibekukan dan 60 tidak dibekukan), batch 16, SGD dengan laju pembelajaran awal 0,01, momentum 0,937, peluruhan bobot 0,0005, penurunan laju kosinus, augmentasi *mosaic* dan *mixup* berprobabilitas 0,5. Komputasi memakai GPU NVIDIA 2060 6 GB.

### 3. Pelacakan Deep Sort
Deep Sort menggabungkan filter Kalman, algoritma Hungarian, dan fitur kedalaman (penampilan) dari kotak pembatas untuk mengurangi lompatan ID akibat oklusi dan perubahan penampilan. Kecocokan ditentukan dari kemiripan dan IoU pada bingkai berdekatan.

### 4. Estimasi kematangan
Tiap ROI tandan dimasukkan ke NanoDet-m-Plus (tulang punggung ShuffleNetV2, leher GhostPAN, kepala ringan dengan modul bantu AGM dan DSLA saat pelatihan) pada ukuran 320×320; model pembanding dilatih pada 384×384. NanoDet menghitung buah matang ($N_r$) dan belum matang ($N_g$). Nilai kematangan $M = N_r/(N_r+N_g)$ bila keduanya lebih dari nol, $M = 1{,}00$ bila $N_r > 0$ dan $N_g = 0$, dan $M = 0{,}00$ bila $N_r = 0$.

### 5. Fusi informasi
Nilai $M$ dikelompokkan ke lima tingkat kematangan berdasarkan sebaran nilai 0 sampai 1 dengan mengacu pada pembagian lima tingkat dari pustaka; batas tiap tingkat tidak dirinci pada teks. Tingkat 5 berarti tandan siap dipetik (dikonfirmasi pekerja rumah kaca). Tingkat yang paling sering muncul pada ID yang sama dipilih sebagai tingkat akhir. ID yang disaring oleh penghitungan wilayah tidak ikut menentukan tingkat kematangan.

### 6. Metrik
mAP, presisi, dan *recall* untuk detektor. Presisi hitung per video $= 1 - |N_{hitung} - N_{benar}|/N_{benar}$, dan akurasi hitung rata-rata $= 1 - \sum|N_{hitung} - N_{benar}| / \sum N_{benar}$.

## Eksperimen dan Hasil
Perbandingan detektor tandan (Tabel 3) menunjukkan YOLOX_tiny terbaik, tetapi YOLOv8n dipilih karena parameter dan komputasinya hampir separuh:

| Detektor tandan | Presisi | *Recall* | mAP0,5 | mAP0,75 | Waktu inferensi | Parameter |
|---|---|---|---|---|---|---|
| CenterNet | 97,46% | 92,00% | 97,20% | 85,40% | 74,85 s | 32,665 M |
| YOLOv5n | 94,27% | 78,93% | 92,40% | 72,60% | 44,15 s | 1,765 M |
| YOLOv5s | 91,37% | 81,87% | 94,50% | 78,30% | 45,88 s | 7,025 M |
| YOLOX_tiny | 92,71% | 98,40% | 98,50% | 92,80% | 51,85 s | 5,033 M |
| YOLOX_nano | 98,51% | 70,40% | 91,60% | 65,30% | 50,93 s | 896,949 K |
| YOLOv8n | 92,13% | 96,80% | 98,20% | 92,60% | 39,63 s | 3,011 M |

Penghitungan pada 19 video (Tabel 4) menunjukkan jumlah acuan 555 tandan dan jumlah terhitung 515, dengan selisih total 40; pada setiap video jumlah terhitung sama dengan atau lebih rendah daripada acuan. Contoh baris: klip 1 (30 acuan, 30 terhitung), klip 9 (38 acuan, 33 terhitung), klip 12 (44 acuan, 39 terhitung). Akurasi hitung rata-rata 92,79% (abstrak dan Tabel 6) terkonfirmasi oleh perhitungan sederhana ini ($1 - 40/555$, dihitung dari kolom total Tabel 4); teks hasil bagian 3.3 menyebut 93,43%.

Perbandingan detektor buah di dalam tandan (Tabel 5):

| Detektor buah | Ukuran masukan | mAP0,5 | mAP0,75 | Parameter |
|---|---|---|---|---|
| YOLOv5s | 384×384 | 95,10% | 81,40% | 7,025 M |
| YOLOv5n | 384×384 | 93,50% | 78,40% | 1,767 M |
| YOLOX_tiny | 384×384 | 97,50% | 91,00% | 5,033 M |
| YOLOX_nano | 384×384 | 96,90% | 88,30% | 896,949 K |
| YOLOv8n | 384×384 | 97,10% | 89,60% | 3,011 M |
| NanoDet-m-Plus | 320×320 | 98,00% | 92,30% | 2,44 M |

Strategi pembaruan kematangan pada 19 video: nilai dengan frekuensi tertinggi menghasilkan akurasi 90,84% (84,29% bila galat hitung dimasukkan), sedangkan nilai rata-rata hanya 69,96% (64,92% dengan galat hitung). Pada tandan dengan ID 16 pada video V19, hasil strategi rata-rata dan strategi frekuensi tertinggi masing-masing 72,91% dan 90,00% pada bingkai 976, serta 41,05% dan 90,00% pada bingkai 1016. Hasil akhir pada RTX 2060 (Tabel 6): 15 FPS, akurasi estimasi kematangan 90,84%, akurasi hitung 92,79%.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: jumlah dan kematangan tandan diperoleh sekaligus pada satu kerangka; modul kematangan sederhana dan tidak mengganggu penghitungan; strategi frekuensi tertinggi mengurangi galat akibat oklusi dan perbedaan sudut pandang; dan kecepatan 15 FPS cukup untuk penggunaan waktu nyata. Pengamatan dari sisi miring memungkinkan lebih banyak buah terdeteksi dibandingkan dari sisi depan.

Keterbatasan yang dinyatakan penulis: oklusi oleh batang utama dan antarbuah dalam tandan masih mengganggu estimasi kematangan, dan pergantian sudut pandang tidak sepenuhnya menyelesaikannya; ID tandan dapat tertukar bila tandan berpose dan kematangan mirip; lompatan ID juga menimbulkan galat kematangan karena satu ID dikaitkan dengan satu nilai kematangan; dataset terbatas dan tidak mencakup seluruh kerumitan pertumbuhan tomat; getaran pada video menurunkan kualitas citra; dan diperlukan analisis sensitivitas terhadap oklusi dan kualitas video.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Pengujian dilakukan pada satu rumah kaca, satu kultivar, dan 19 klip singkat, dan acuan kematangan pada video berupa penilaian manual yang rincian prosedurnya tidak diuraikan. Seluruh klip menghasilkan hitungan sama atau lebih rendah daripada acuan, sehingga terdapat kecenderungan kurang hitung. Batas lima tingkat kematangan dan rincian metode penghitungan wilayah tidak diuraikan pada teks. Teks hasil menyatakan waktu inferensi YOLOv8n 36,93 s per seribu citra, sedangkan Tabel 3 mencantumkan 39,63 s, dan menyebut YOLOv8n hanya 0,68% di bawah YOLOX_tiny, padahal selisih mAP0,5 pada Tabel 3 adalah 0,3 poin persentase.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tandan yang terlihat pada banyak bingkai video dengan pelacakan Deep Sort (filter Kalman, algoritma Hungarian, fitur penampilan) ditambah penghitungan wilayah untuk menyaring ID berlebih akibat lompatan ID. Pencocokan berlangsung dalam satu urutan video pada satu sisi barisan; tidak ada penggabungan lintas sisi pohon atau lintas barisan. Sebuah tandan yang tampak dari pandangan berbeda dalam video dikaitkan melalui ID pelacak yang sama, dan penulis menyatakan identifikasi keliru pada tandan serupa tetap terjadi.

Hitungan dan kematangan dilaporkan sebagai atribut per tandan: kematangan tiap tandan dikelompokkan menjadi lima tingkat dan digabungkan dengan ID, dengan tujuan memperkirakan jumlah tandan per tingkat di seluruh rumah kaca. Namun hasil kuantitatif yang diberikan adalah jumlah total per video dan akurasi estimasi tingkat kematangan, bukan matriks hitungan per tingkat. Acuan hitungnya adalah hitungan manual tandan pada video (555 tandan pada 19 video). Yang dapat dipindahkan ke tandan sawit multi-sisi adalah gagasan melekatkan atribut kelas (kematangan) pada ID objek dan memilih kelas akhir melalui modus lintas pengamatan untuk meredam kesalahan klasifikasi akibat oklusi, serta penggunaan region counting untuk menyaring ID berlebih. Perbedaannya, tomat ceri di rumah kaca berada pada tinggi dan jarak yang tetap, sedangkan sawit di lapangan tidak.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `qi2024improved`.

Ringkasan yang aman dikutip: Qi dkk. (2024) mengusulkan kerangka *tracking-by-detection* yang memakai YOLOv8n, Deep Sort, dan NanoDet untuk menghitung tandan tomat ceri di rumah kaca dan memperkirakan kematangan tiap tandan dari rasio buah matang terhadap total buah, dalam lima tingkat. Lompatan ID dikurangi dengan penghitungan wilayah dan kematangan akhir ditentukan dari nilai dengan frekuensi tertinggi lintas bingkai. Pada 19 video, akurasi hitung 92,79% dan akurasi kematangan 90,84% (84,29% dengan galat hitung) dicapai pada 15 bingkai per detik.

Catatan verifikasi data: akurasi hitung 92,79% dan akurasi kematangan 90,84% dan 84,29% dari abstrak, bagian 3.5, dan Tabel 6; angka mean 69,96% dan 64,92% dari bagian 3.5. Total 555, 515, dan 40 dari Tabel 4 terbaca utuh; 92,79% cocok dengan perhitungan dari total itu, sedangkan teks bagian 3.3 menyebut 93,43% tanpa menjelaskan selisihnya. Tabel 3 dan 5 terbaca utuh dari teks ekstraksi. Batas lima tingkat kematangan, rincian penghitungan wilayah, dan data per tingkat tidak ada pada teks. Gambar (termasuk Gambar 12) tidak terbaca dari teks. Data tersedia atas permintaan kepada penulis.
