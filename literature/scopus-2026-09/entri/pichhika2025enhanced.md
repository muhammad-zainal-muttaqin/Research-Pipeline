# Enhanced YOLO-Based Mango Detection and Centroid Tracking for Precise Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pichhika2025enhanced` |
| Judul asli | Enhanced YOLO-Based Mango Detection and Centroid Tracking for Precise Yield Estimation |
| Penulis | Pichhika, Hari Chandana; Subudhi, Priyambada; Prasad Yerra, Raja Vara |
| Tahun | 2025 |
| Venue | Applied Fruit Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [pichhika2025enhanced.pdf](../pdf/pichhika2025enhanced.pdf)
- DOI resmi: https://doi.org/10.1007/s10341-025-01385-9

## Gambaran Umum
Makalah ini mengusulkan sistem estimasi hasil mangga dari video yang direkam mengelilingi pohon. Sistem terdiri atas detektor YOLOv5 yang dimodifikasi ("Enhanced MangoYOLO5") dan algoritma pelacakan titik pusat (*centroid tracking*) yang diperluas dengan rujukan beberapa bingkai dan ambang dinamis. Modifikasi detektor meliputi *Attentive Feature Fusion* (AFF) pada tulang punggung (*backbone*), *Convolutional Block Attention Module* (CBAM) dan sambungan rapat (*dense connection*) pada leher jaringan (*neck*), serta kepala deteksi tambahan berukuran 10×10.

Data berupa video delapan pohon mangga 'Banganapalle' di kampus IIIT Sri City, Andhra Pradesh, India (April sampai Juni 2022), yang diambil dengan kamera genggam pada jarak 1,5 sampai 2 m. Pengujian dilakukan pada lima video. Abstrak melaporkan mAP 93,6%, sedangkan pada perbandingan detektor (Tabel 1, citra tambalan 256×256) mAP model usulan adalah 91,6% dan pada citra resolusi penuh 92,8% (Tabel 2); angka 93,6% berasal dari tabel ablasi metode (Tabel 7).

Pada lima video uji, hitungan model usulan lebih rendah daripada hitungan manual pada semua video (misalnya 74 dari 105 pada video 1), dengan galat absolut rerata (*mean absolute error*, MAE) yang dilaporkan 0,17 sampai 0,52. Model usulan mencatat MOTA tertinggi pada kelima video (0,79 sampai 0,84).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan manual buah mangga memakan tenaga dan waktu serta rentan hitungan berulang. Banyak penelitian hanya memakai satu sisi pohon, padahal mangga tersebar di seluruh tajuk. Perekaman dari beberapa sisi menimbulkan masalah hitungan ganda bila buah yang sama muncul pada video dari sudut berbeda. Pelacak seperti SORT dan DeepSORT menurut penulis kurang efektif untuk objek statis yang bentuk dan ukurannya serupa, seperti mangga, karena variasi ciri objek terbatas.

Penulis membandingkan dua pendekatan penyatuan pandang: rekonstruksi 3D, yang membutuhkan perangkat khusus seperti kamera ganda atau LiDAR dan pemrosesan rumit, dan pelacakan, yang lebih murah dan hanya memerlukan video. Penulis memilih pelacakan karena objek statis dan konfigurasi sederhana.

## Ide Utama
Gagasan pertama adalah memperkuat detektor MangoYOLO5 (model pada penelitian terdahulu penulis) agar mengurangi deteksi palsu dan memperbaiki lokalisasi mangga yang tertutup sebagian. Gagasan kedua adalah memperluas pelacak titik pusat sederhana dengan rujukan dua bingkai sebelumnya (bingkai $t-1$ dan $t-2$) untuk menangani oklusi, dengan ambang jarak yang berubah-ubah sesuai pergerakan titik pusat terkini, dan dengan validasi IoU. Jumlah akhir buah adalah banyaknya ID unik sepanjang video.

## Cara Kerja Langkah demi Langkah

```
  Video 360 derajat -> bingkai -> Enhanced MangoYOLO5 (kotak)
     -> pelacak titik pusat: jarak berbobot 1/k (k = 1, 2), ambang dinamis,
        validasi IoU -> ID per mangga -> hitungan = jumlah ID unik
```

### 1. Akuisisi data
Delapan pohon *Mangifera indica* 'Banganapalle' direkam dengan kamera ponsel genggam beresolusi 1920×1080 pada siang hari (April sampai Juni 2022) di kebun kampus IIIT Sri City. Pohon berukuran sedang (tinggi 2 sampai 3 m, diameter tajuk 1 sampai 2 m, sekitar 50 sampai 60 mangga tampak per pohon, jarak antarpohon sekitar 2 m). Perekam berjalan 360 derajat selama sekitar 60 sampai 80 detik per pohon, pada jarak 1,5 sampai 2 m, dengan cuaca cerah dan berawan sebagian.

### 2. Penyiapan data
Dataset awal berisi 704 tambalan citra (*patch*) berukuran 256×256 piksel dari tiga video. Dengan augmentasi (rotasi 90, 180, dan 270 derajat, pembalikan horizontal dan vertikal, serta penskalaan) diperoleh total 5.000 tambalan latih. Sekitar 400 citra beresolusi penuh (1920×1080) juga dipakai untuk pelatihan dan validasi. Pengujian memakai lima video terpisah. Anotasi dibuat dengan makesense.ai. Pembagian latih dan validasi 80% dan 20%.

### 3. Detektor Enhanced MangoYOLO5
Blok AFF pada tulang punggung berisi atensi kanal, atensi spasial, fusi fitur lintas lapisan (C2F), agregasi fitur multiskala (MSFA), dan sambungan identitas. CBAM dan sambungan rapat dipasang pada leher jaringan. Kepala deteksi tambahan 10×10 ditambahkan pada kepala yang sudah memuat 20×20, 40×40, dan 80×80. Ambang IoU untuk penyaringan kotak diatur 0,5 dibandingkan 0,7 yang konvensional. Semua model dilatih dengan 100 epoch, laju belajar 0,01, pengoptimal AdamW, dan ukuran batch 16, pada GPU NVIDIA Tesla dengan memori 16 GB.

### 4. Pelacak titik pusat dengan rujukan banyak bingkai
Titik pusat dihitung dari kotak: $C = ((x_{min}+x_{max})/2,\ (y_{min}+y_{max})/2)$. Jarak berbobot waktu antara titik pusat bingkai $t$ dan bingkai $t-k$ dihitung sebagai $d = \frac{1}{k}\sqrt{(x_t - x_{t-k})^2 + (y_t - y_{t-k})^2}$ dengan $k = 1, 2$. Pasangan dinyatakan cocok bila $d < \theta$ dan IoU kotak minimal $\tau_{IoU}$ (0,5). Bila tidak ada kecocokan pada bingkai $t-1$, bingkai $t-2$ diperiksa; bila tetap tidak ada, ID baru diberikan.

### 5. Ambang dinamis
Ambang awal $\theta_{init}$ adalah 10 piksel. Ambang diperbarui dengan rerata dan simpangan baku jarak titik pusat terkini pada penyangga riwayat, dengan faktor penghalus $\alpha = 0{,}7$ dan pengali $k = 1{,}5$, dan dibatasi pada rentang 5 sampai 20 piksel. Hitungan akhir adalah jumlah ID unik.

## Eksperimen dan Hasil
Deteksi dievaluasi dengan presisi, recall, dan mAP. Tabel 1 membandingkan model pada tambalan 256×256 (cuplikan; waktu estimasi dan FLOPs ada pada makalah).

| Model | Presisi (%) | Recall (%) | mAP (%) |
|---|---|---|---|
| Faster R-CNN | 74 | 48 | 59 |
| MangoNet | 75,5 | 50 | 60,3 |
| YOLOv5s | 85,5 | 58,9 | 68,5 |
| MangoYOLO5 (dasar) | 79,5 | 68,4 | 81,2 |
| YOLOv8 | 87,5 | 75,2 | 89,8 |
| YOLOv10 | 89 | 76,5 | 91,4 |
| YOLOv11 | 89,5 | 77,2 | 91,7 |
| Enhanced MangoYOLO5 | 89,3 | 77 | 91,6 |

Pada tambalan, YOLOv11 (91,7%) sedikit lebih tinggi daripada model usulan (91,6%), sehingga klaim mAP tertinggi pada teks tidak sesuai dengan tabel. Pada citra resolusi penuh (Tabel 2), model usulan mencapai presisi 91%, recall 79%, dan mAP 92,8%, sedangkan YOLOv11 mencapai 93%, 80,2%, dan 93,7%. Penulis menyatakan peningkatan resolusi penuh hanya menaikkan mAP dari 91,6% menjadi 92,8%, dengan FLOPs naik sekitar 30%.

Ablasi detektor (Tabel 6): dasar MangoYOLO5 mAP 83,9%, dengan AFF 85,4%, dengan AFF dan CBAM 86,5%, ditambah sambungan rapat 87,2%, ditambah kepala 10×10 89,5%, dan model lengkap 91,6%. Ablasi ambang IoU (Tabel 4): ambang 0,5, 0,6, dan 0,7 masing-masing menghasilkan mAP 91,6%, 91,3%, dan 91,1% (recall 77%, 73,8%, dan 70,4%).

Hitungan terhadap acuan (Tabel 3, lima video; acuan berupa hitungan manual pada bingkai saat pelabelan; MAE dilaporkan sebagai nilai pecahan).

| Video | Hitungan manual | SORT | DeepSORT | FairMOT | Model usulan | MAE usulan | MOTA usulan |
|---|---|---|---|---|---|---|---|
| 1 | 105 | 459 | 255 | 114 | 74 | 0,30 | 0,79 |
| 2 | 62 | 30 | 26 | 42 | 50 | 0,19 | 0,82 |
| 3 | 52 | 10 | 5 | 28 | 25 | 0,52 | 0,80 |
| 4 | 26 | 16 | 11 | 14 | 19 | 0,27 | 0,84 |
| 5 | 36 | 12 | 2 | 27 | 30 | 0,17 | 0,80 |

Model usulan menghasilkan hitungan di bawah hitungan manual pada kelima video. FairMOT lebih dekat ke acuan pada video 1 dan 3 menurut penulis, tetapi MOTA-nya lebih rendah (misalnya 0,76 dan 0,69). SORT menghasilkan banyak hitungan berlebih pada video 1 (459). Pada Gambar 8, model usulan memiliki FP dan IDSW terendah dan MT tertinggi; nilai grafiknya tidak terbaca pada teks.

Ablasi metode (Tabel 7), dengan dasar pelacak titik pusat berambang statis: MOTA 79% dan mAP 91,6%; dengan penghalusan IoU, mAP 87,4% dan MOTA 80,5%; dengan rujukan banyak bingkai, MOTA 82,1%; dengan IoU dan ambang dinamis, MOTA 83,4%; model lengkap mAP 93,6% dan MOTA 85,2%.

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: modul atensi menekan deteksi palsu dengan biaya komputasi sedang (19,6 G FLOPs dan 8,5 juta parameter pada tambalan), pelacak sederhana tanpa fitur penampilan sehingga cocok untuk objek serupa, dan MOTA lebih tinggi daripada SORT, DeepSORT, dan FairMOT pada kelima video.

Keterbatasan yang dinyatakan penulis: MOTA berkisar 76% sampai 84% dan menurun pada video berkualitas buruk (resolusi rendah, kabur, pencahayaan tidak konsisten), oklusi ekstrem, dan gerak kamera mendadak. Pekerjaan lanjutan mencakup mekanisme pelacakan yang lebih canggih dan variasi jarak pencitraan. Data tersedia atas permintaan setelah penerimaan.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Terdapat ketidakkonsistenan angka: abstrak dan kesimpulan menyebut mAP 93,6%, sedangkan Tabel 1 dan Tabel 6 menyebut 91,6%, dan kesimpulan menyebut MOTA maksimum 84%, sedangkan Tabel 7 menyebut 85,2%. Hitungan terhadap acuan menunjukkan kekurangan hitung pada seluruh video uji, tetapi makalah menonjolkan MOTA dan tidak membahas bias ke bawah ini. Acuan hitung adalah hitungan manual pada video, dan tidak ada hitungan panen. Lima video uji berasal dari satu kebun dan satu kultivar. Pelacak tidak memiliki mekanisme penyatuan identitas setelah buah menghilang lebih dari dua bingkai, sehingga buah yang muncul kembali setelah putaran penuh akan menerima ID baru, padahal hitungan akhir adalah jumlah ID unik. Pelatihan dan validasi dari bingkai video yang berdekatan berpotensi mempertinggi skor deteksi.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali, yakni pada video 360 derajat satu pohon, dengan pelacakan titik pusat berbasis deteksi yang memakai rujukan dua bingkai sebelumnya dan validasi IoU. Identitas hanya dipertahankan lewat kedekatan posisi dan tumpang tindih pada bingkai berdekatan; tidak ada pencocokan lintas sisi pohon yang terpisah jauh dalam waktu, dan tidak ada rekonstruksi 3D. Hitungan dilaporkan sebagai jumlah total per video, tanpa pembagian per kelas, karena hanya satu kelas (mangga) yang dihitung. Acuan hitungnya adalah hitungan manual pada bingkai video pada saat pelabelan, bukan panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan pelacak ringan tanpa fitur penampilan untuk objek statis yang serupa, rujukan lebih dari satu bingkai untuk oklusi, ambang jarak adaptif, serta validasi dengan IoU. Namun, hitungan yang selalu di bawah acuan pada kelima video menunjukkan bahwa buah yang tidak terdeteksi atau yang ID-nya terputus tidak dipulihkan, dan mekanisme ini tidak mengatasi penyatuan identitas antar-sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `pichhika2025enhanced`.

Pichhika dkk. mengusulkan detektor MangoYOLO5 yang ditingkatkan (AFF, CBAM, sambungan rapat, dan kepala deteksi 10×10) yang dipadukan dengan pelacak titik pusat berambang dinamis dan rujukan dua bingkai untuk memperkirakan hasil mangga dari video 360 derajat. Pada lima video uji, model usulan memperoleh MOTA 0,79 sampai 0,84, lebih tinggi daripada SORT, DeepSORT, dan FairMOT, sedangkan hitungannya lebih rendah daripada hitungan manual pada semua video (misalnya 74 dari 105 pada video 1). Makalah melaporkan mAP 91,6% pada tambalan dan 93,6% pada ablasi metode.

Catatan verifikasi data: Angka deteksi bersumber dari Tabel 1, 2, 4, dan 6, angka pelacakan dan hitungan dari Tabel 3 dan Tabel 7, dan parameter pelacak dari seksi Dynamic Threshold Computation. Terdapat ketidakkonsistenan internal antara mAP 91,6% dan 93,6% serta antara MOTA maksimum 84% pada kesimpulan dan 85,2% pada Tabel 7; kedua angka dilaporkan apa adanya. Teks ekstraksi memuat beberapa rumus dengan simbol rusak (Persamaan 5 sampai 7) sehingga bentuk persis tidak diverifikasi. Gambar 8 (FP, FN, IDSW, MT) tidak terbaca pada teks. Definisi MAE pada Tabel 3 tidak dijelaskan; nilainya konsisten dengan galat relatif terhadap hitungan manual. Jumlah mangga pada dataset latih dan uji tidak dilaporkan selain hitungan manual lima video.
