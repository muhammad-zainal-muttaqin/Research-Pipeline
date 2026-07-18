# 117 - Onboard Dynamic-Object Detection and Tracking for Autonomous Robot Navigation with RGB-D Camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xu2024onboard` |
| Judul asli | Onboard Dynamic-Object Detection and Tracking for Autonomous Robot Navigation with RGB-D Camera |
| Penulis | Zhefan Xu, Xiaoyang Zhan, Yumeng Xiu, Christopher Suzuki, Kenji Shimada |
| Tahun | 2024 (versi arXiv pertama 2023) |
| Venue | IEEE Robotics and Automation Letters (RA-L), Vol. 9, No. 1, hlm. 651–658 |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2303.00132
- **Kode sumber terbuka:** https://github.com/Zhefan-Xu/onboard_detector
- **Google Scholar:** https://scholar.google.com/scholar?q=Onboard%20Dynamic-Object%20Detection%20and%20Tracking%20for%20Autonomous%20Robot%20Navigation%20with%20RGB-D%20Camera

## Gambaran Umum

Makalah ini mengusulkan DODT (*Dynamic Obstacle Detection and Tracking*), sistem deteksi dan pelacakan objek dinamis tiga dimensi yang dirancang untuk *quadcopter* (wahana terbang beroda baling-baling empat) berukuran kecil dengan komputer *onboard* (terpasang di badan wahana) berdaya rendah. Sistem ini memakai kamera RGB-D — kamera yang menghasilkan citra warna sekaligus peta kedalaman per piksel — sebagai satu-satunya sensor persepsi, tanpa LiDAR (*Light Detection and Ranging*, sensor jarak berbasis pantulan laser). Gagasan utamanya adalah menggabungkan beberapa detektor yang murah secara komputasi namun kurang akurat sendiri-sendiri menjadi satu *ensemble* (gabungan) yang akurasinya lebih tinggi, dipadukan dengan metode pelacakan berbasis fitur statistik titik awan (*point cloud*) untuk menghindari salah pasang antarobjek.

Diuji pada dua komputer *onboard* (Intel NUC dan NVIDIA Jetson Xavier NX) dengan kebenaran posisi dari sistem penangkap gerak OptiTrack, DODT mencatat galat posisi 0,11 m — terendah di antara seluruh metode pembanding — dan galat kecepatan 0,23 m/s yang sebanding dengan metode terbaik pembanding. Seluruh proses berjalan secara *real-time* pada perangkat keras berdaya 10–20 watt, dan hasil pelacakannya terbukti dapat dipakai wahana untuk mengubah lintasan terbang secara otomatis saat menghindari objek bergerak dalam uji terbang nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Robot otonom yang beroperasi di lingkungan dalam ruang yang ramai memerlukan persepsi objek dinamis yang akurat agar dapat merencanakan gerak dengan aman. Riset deteksi objek tiga dimensi sejauh ini sebagian besar berasal dari bidang kendaraan otonom, yang memakai LiDAR untuk menghasilkan awan titik padat lalu memprosesnya dengan jaringan pembelajaran mendalam. Pendekatan ini tidak dapat dipindahkan langsung ke robot kecil seperti *quadcopter* berbasis penglihatan (*vision-based UAV*, wahana udara nirawak yang mengandalkan kamera), karena LiDAR terlalu berat untuk dibawa dan biaya komputasi jaringan berbasis LiDAR terlalu tinggi untuk komputer *onboard* berdaya 10–20 watt yang umum dipakai wahana kecil.

Kamera RGB-D menjadi alternatif yang lebih ringan, tetapi membawa dua keterbatasan sendiri. Pertama, jangkauan kedalamannya terbatas — misalnya kamera Intel RealSense D435i hanya andal pada rentang sekitar 0,3–3,0 m. Kedua, estimasi kedalamannya mengandung derau (*noise*) yang menyebabkan deteksi palsu dan hasil pelacakan yang tidak konsisten antar-*frame* (bingkai citra berurutan). Menurut penulis, metode berbasis RGB-D yang ada sebelumnya umumnya memakai satu detektor tunggal saja — baik detektor geometris non-pembelajaran maupun detektor berbasis pembelajaran seperti YOLO (*You Only Look Once*, detektor objek satu tahap yang merumuskan deteksi sebagai regresi tunggal dari citra ke kotak pembatas dan kelas — lihat bab 001) — sehingga akurasinya dibatasi oleh kelemahan detektor tunggal tersebut. Selain itu, metode pelacakan yang umum dipakai mencocokkan objek antar-*frame* berdasarkan jarak titik pusat (*center-distance*) semata, yang rawan salah pasang ketika beberapa objek saling berdekatan atau saling menutupi sebagian. Kombinasi keterbatasan sensor dan keterbatasan algoritme inilah yang menjadi celah yang coba ditutup oleh makalah ini.

## Ide Utama

Gagasan inti DODT adalah tidak mengandalkan satu detektor, melainkan menjalankan beberapa detektor ringan secara paralel dan menggabungkan keluarannya menjadi satu deteksi yang lebih andal — sebuah strategi *ensemble* (gabungan beberapa model lemah menjadi satu keputusan yang lebih kuat). Dua detektor non-pembelajaran yang murah secara komputasi dijalankan bersamaan pada setiap *frame*; jika keduanya sepakat mendeteksi objek pada lokasi yang tumpang tindih, hasilnya digabung dan dianggap lebih tepercaya daripada keluaran detektor mana pun sendirian. Sebuah detektor berbasis pembelajaran ringan bersifat opsional, dipakai untuk memperluas jangkauan deteksi dan membantu identifikasi objek, tetapi dapat dimatikan pada perangkat yang sangat terbatas dayanya.

Untuk pelacakan, sistem tidak mencocokkan objek antar-*frame* hanya berdasarkan posisi, melainkan berdasarkan vektor fitur yang memuat posisi, ukuran, jumlah titik awan, dan sebaran statistiknya. Kecepatan objek diestimasi dengan filter Kalman (metode estimasi keadaan berurutan yang menggabungkan prediksi model gerak dengan pengukuran baru) yang mengasumsikan percepatan konstan, bukan kecepatan konstan seperti kebanyakan metode sebelumnya, sehingga lebih sesuai untuk objek yang sedang berakselerasi atau berbelok.

## Cara Kerja Langkah demi Langkah

Alur pemrosesan dari citra RGB-D masukan hingga keputusan navigasi dapat digambarkan sebagai berikut.

```
citra RGB-D (warna + peta kedalaman)
            │
   ┌────────┼─────────────────┐
   ▼        ▼                 ▼
U-Depth   DBSCAN        YOLO-MAD (opsional)
(peta atas 2D)  (klaster titik 3D)  (kotak 2D + MAD kedalaman)
   │        │                 │
   └───┬────┴─────────┬───────┘
       ▼               
  fusi ensemble (cocokkan via IOU, gabung kotak)
       │
       ▼
  asosiasi data berbasis fitur
  (posisi, ukuran, jumlah titik, deviasi)
       │
       ▼
  filter Kalman akselerasi-konstan
  (estimasi posisi, kecepatan, percepatan)
       │
       ▼
  identifikasi statis/dinamis  -->  perencana gerak
```

### Detektor U-Depth

Detektor pertama membangun peta kedalaman tampak-atas (*U-depth map*) dari citra kedalaman: piksel-piksel dengan nilai kedalaman serupa dikelompokkan menurut kontinuitasnya untuk memperkirakan lebar objek, kemudian pencarian kontinuitas kedalaman dilakukan untuk memperkirakan tinggi objek. Dari kedua ukuran ini, kotak pembatas tiga dimensi dibentuk melalui triangulasi geometris sederhana, tanpa jaringan saraf.

### Detektor DBSCAN

Detektor kedua memakai DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*, algoritme pengelompokan berbasis kepadatan titik) untuk mengelompokkan awan titik yang telah disaring menjadi wilayah-wilayah yang diduga objek. Karena DBSCAN tidak mengasumsikan bentuk geometris tertentu, detektor ini tetap berfungsi saat data kedalaman berderau, berbeda dengan pendekatan berbasis asumsi bentuk yang mudah gagal pada kondisi tersebut.

### Fusi Ensemble

Kotak pembatas dari kedua detektor dicocokkan berpasangan memakai IOU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak). Pasangan kotak dengan IOU di atas ambang tertentu digabung: dimensi diambil dari nilai maksimum kedua kotak dan posisi dari rata-rata keduanya. Penggabungan ini menekan pengaruh derau yang muncul pada salah satu detektor saja. Studi ablasi (pengujian dengan menghapus satu komponen untuk mengukur kontribusinya) pada makalah menunjukkan bahwa tanpa fusi ensemble, tingkat deteksi palsu (*false positive*) naik dari 3,7% menjadi 18,6%.

### Detektor Opsional Berbasis Pembelajaran: YOLO-MAD

Modul ketiga bersifat opsional dan memakai varian YOLO yang ringan (berbasis *YOLO-Fastest*) untuk mendeteksi kotak dua dimensi pada citra RGB, kemudian memperkirakan kedalaman objek memakai MAD (*Median Absolute Deviation*, ukuran sebaran statistik yang tahan terhadap nilai pencilan) dari nilai kedalaman di dalam kotak tersebut. Modul ini memperluas jangkauan deteksi melampaui batas awan titik padat (sekitar 3 m) ke wilayah yang lebih jauh dan bernilai kedalaman lebih jarang, tetapi menuntut komputasi tambahan: pada Intel NUC modul ini memakan 14,3 milidetik dari total 19,12 milidetik waktu proses per *frame* (sekitar 75% dari total), dan pada Jetson Xavier NX memakan 23,5 dari 40,08 milidetik (sekitar 59%).

### Asosiasi Data Berbasis Fitur

Alih-alih mencocokkan objek antar-*frame* hanya dengan jarak titik pusat, sistem membangun vektor fitur yang memuat posisi, dimensi, jumlah titik awan, dan deviasi standarnya untuk tiap objek terdeteksi. Kemiripan antara objek pada *frame* sebelumnya dan *frame* saat ini dihitung dengan fungsi eksponensial negatif dari jarak Euklides kuadrat antarvektor fitur. Pendekatan ini mengurangi salah pasang saat dua objek saling berdekatan, karena posisi bukan satu-satunya penentu kecocokan. Ablasi menunjukkan bahwa tanpa asosiasi berbasis fitur ini, galat posisi naik dari 0,11 m menjadi 0,14 m.

### Pelacakan dengan Filter Kalman Akselerasi-Konstan

Keadaan tiap objek direpresentasikan sebagai vektor enam elemen: posisi x dan y, kecepatan pada kedua sumbu, serta percepatan pada kedua sumbu. Model gerak akselerasi-konstan ini lebih sesuai untuk objek yang berubah kecepatan (mempercepat, memperlambat, berbelok) dibandingkan model kecepatan-konstan yang mengasumsikan gerak lurus beraturan.

### Identifikasi Statis atau Dinamis

Modul terakhir mengklasifikasikan setiap objek terlacak sebagai statis atau dinamis berdasarkan estimasi kecepatan dari filter Kalman, dikombinasikan dengan pemungutan suara (*voting*) dari titik-titik awan di sekitarnya. Klasifikasi ini menentukan objek mana yang perlu diperhitungkan secara khusus oleh perencana gerak wahana.

## Eksperimen dan Hasil

Sistem diuji pada *quadcopter* kecil dengan dua jenis komputer *onboard* — Intel NUC dan NVIDIA Jetson Xavier NX — dengan posisi sebenarnya diukur memakai sistem penangkap gerak OptiTrack sebagai acuan kebenaran (*ground truth*). Metode dibandingkan dengan tiga pendekatan pembanding dari literatur: Metode I (deteksi stereo dengan pemodelan elipsoid), Metode II (klasterisasi dipadu YOLO), dan Metode III (pendekatan RGB-D SLAM sebelumnya oleh kelompok penulis yang sama).

| Metode | Galat posisi (m) | Galat kecepatan (m/s) | Tingkat deteksi palsu (%) |
|---|---|---|---|
| Metode I | 0,28 | 0,47 | — |
| Metode II | 0,18 | 0,29 | 16,4% |
| Metode III | 0,19 | 0,21 | 19,6% |
| DODT (diusulkan) | 0,11 | 0,23 | 3,7% |

Galat posisi DODT (0,11 m) adalah yang terendah di antara seluruh metode: sekitar 39% lebih rendah dari Metode II yang menjadi pembanding terbaik kedua (0,18 m). Galat kecepatan (0,23 m/s) sedikit lebih tinggi daripada Metode III (0,21 m/s), tetapi tetap lebih rendah daripada Metode I dan II — makalah menyebutnya "sebanding" karena selisihnya kecil. Tingkat deteksi palsu DODT (3,7%) jauh di bawah Metode II dan III (16,4% dan 19,6%), menunjukkan bahwa fusi ensemble efektif menekan deteksi keliru dibandingkan detektor tunggal yang dipakai metode pembanding.

Dari sisi kecepatan komputasi, total waktu proses per *frame* adalah 19,12 milidetik pada Intel NUC dan 40,08 milidetik pada Jetson Xavier NX ketika modul pembelajaran YOLO-MAD diaktifkan — setara dengan sekitar 50 Hz dan 25 Hz. Bila modul opsional itu dimatikan, kecepatan pemrosesan naik signifikan menjadi sekitar 210 Hz pada Intel NUC dan 60 Hz pada Jetson Xavier NX, karena komponen pembelajaran adalah bagian termahal dari keseluruhan proses. Interpretasinya: pengguna dapat memilih menonaktifkan modul pembelajaran demi kecepatan lebih tinggi pada perangkat yang sangat terbatas dayanya, dengan konsekuensi jangkauan deteksi yang lebih pendek.

Uji terbang nyata sejauh 15 m di lingkungan berisi objek bergerak menunjukkan wahana berhasil mengubah lintasannya secara otomatis untuk menghindari objek dinamis berdasarkan hasil pelacakan sistem, membuktikan kelayakan pendekatan ini di luar pengujian tolok ukur murni.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini terletak pada validasi menyeluruh: setiap komponen diuji lewat ablasi (fusi ensemble dan asosiasi berbasis fitur masing-masing terbukti menyumbang penurunan galat dan deteksi palsu), dan sistem divalidasi tidak hanya pada tolok ukur statis tetapi juga pada uji terbang nyata. Desain modular — detektor non-pembelajaran sebagai inti dan detektor pembelajaran sebagai tambahan opsional — memberi fleksibilitas menyesuaikan beban komputasi dengan daya perangkat yang tersedia, sesuatu yang jarang ditawarkan metode berbasis pembelajaran murni.

Keterbatasan yang diakui penulis meliputi hilangnya pelacakan saat objek keluar dari bidang pandang kamera (*field of view*) atau tertutup sepenuhnya oleh objek lain, serta jangkauan deteksi yang tetap dibatasi oleh bidang pandang dan jarak efektif sensor RGB-D. Dari sisi rekayasa, model akselerasi-konstan pada filter Kalman tetap merupakan pendekatan linear yang kurang sesuai untuk objek yang berbelok tajam atau bermanuver non-linear secara mendadak. Secara konseptual, pengujian dilakukan pada lingkungan dalam ruang dengan kebenaran posisi dari OptiTrack, sehingga generalisasi ke kondisi luar ruang dengan cahaya matahari langsung — yang dapat mengganggu sensor kedalaman inframerah pada banyak kamera RGB-D — belum tergambar dari data yang dipaparkan.

## Kaitan dengan Bab Lain

Modul YOLO-MAD pada bab ini adalah turunan ringan dari formulasi deteksi satu tahap yang pertama kali diletakkan pada bab 001 (YOLOv1): citra langsung dipetakan ke kotak pembatas dan kelas dalam satu evaluasi jaringan, di sini diringankan lebih jauh menjadi varian *YOLO-Fastest* agar muat pada komputer *onboard* berdaya rendah. Di dalam klaster YOLO plus RGB-D, bab ini melengkapi [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md), yang juga mengkaji cara menggabungkan kanal warna dan kedalaman, dan [119 - 2023 - Distance Measurement via YOLO + Depth (Chen dkk.) - YOLO plus RGB-D](./119%20-%202023%20-%20Distance%20Measurement%20via%20YOLO%20+%20Depth%20%28Chen%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md), yang sama-sama memakai peta kedalaman untuk memperkirakan jarak objek dari deteksi dua dimensi. Perbedaan penekanannya jelas: kedua bab tersebut berfokus pada akurasi deteksi/estimasi jarak objek statis, sedangkan bab ini menambahkan dimensi pelacakan temporal dan estimasi kecepatan yang dibutuhkan khusus untuk navigasi di antara objek yang bergerak.

## Poin untuk Sitasi

Kutip dengan kunci `xu2024onboard`. Ringkasan yang aman dikutip: "Xu dkk. mengusulkan DODT, sistem deteksi dan pelacakan objek dinamis tiga dimensi berbasis kamera RGB-D untuk *quadcopter* kecil, yang menggabungkan detektor U-Depth dan DBSCAN lewat strategi ensemble serta pelacakan berbasis fitur dengan filter Kalman akselerasi-konstan, mencapai galat posisi 0,11 m dan galat kecepatan 0,23 m/s — terbaik di antara metode pembanding yang diuji (IEEE RA-L, Vol. 9, No. 1, 2024, hlm. 651–658)." Angka galat posisi/kecepatan/tingkat deteksi palsu pada tabel perbandingan, angka waktu proses (19,12 ms/40,08 ms) dan frekuensi (50/25 Hz dengan modul pembelajaran, 210/60 Hz tanpanya), serta angka ablasi (0,17 m dan 18,6% tanpa ensemble; 0,14 m tanpa asosiasi berbasis fitur) diperoleh dari pembacaan naskah arXiv versi HTML; disarankan verifikasi silang terhadap PDF final IEEE RA-L sebelum dikutip dalam karya formal, karena angka pada versi jurnal terkadang berbeda tipis dari versi pracetak.
