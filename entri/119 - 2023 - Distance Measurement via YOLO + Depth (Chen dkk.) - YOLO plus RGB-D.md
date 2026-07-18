# 119 - Indoor Object Distance Measurement for Robots Based on YOLO and Depth Foreground Prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2023depthyolo` |
| Judul Asli | Indoor Object Distance Measurement for Robots Based on YOLO and Depth Foreground Prediction |
| Penulis | Chen, Yu-Chen; others |
| Tahun | 2023 |
| Venue | Proceedings of the IEEE International Conference on Advanced Robotics and Intelligent Systems (ARIS) |
| Tema Klaster | YOLO plus RGB-D |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Indoor%20Object%20Distance%20Measurement%20for%20Robots%20Based%20on%20YOLO%20and%20Depth%20Foreground%20Prediction
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Indoor%20Object%20Distance%20Measurement%20for%20Robots%20Based%20on%20YOLO%20and%20Depth%20Foreground%20Prediction&sort=relevance

## Gambaran Umum
Makalah ini mengusulkan metode modular untuk mengukur jarak objek di lingkungan dalam ruang (*indoor*) untuk kebutuhan navigasi dan manipulasi robot pelayan. Sistem yang diusulkan menggabungkan model deteksi objek *You Only Look Once* (YOLO) dengan algoritma prediksi *foreground* (latar depan) kedalaman. Masalah utama yang diselesaikan adalah ketidakakuratan estimasi jarak akibat masuknya piksel latar belakang (*background*) ke dalam wilayah *bounding box* (kotak pembatas) deteksi 2D. 

Hasil eksperimen menunjukkan bahwa dengan mengisolasi piksel *foreground* di dalam kotak pembatas, kesalahan rata-rata estimasi jarak dapat dikurangi secara signifikan. Sistem ini mampu berjalan pada kecepatan tinggi yang memenuhi persyaratan operasi robot secara *real-time* (waktu nyata). Penggabungan deteksi objek 2D dan sensor kedalaman dalam kerangka kerja terpisah ini memberikan alternatif yang efisien dibandingkan dengan model deteksi 3D ujung-ke-ujung (*end-to-end*) yang membutuhkan daya komputasi tinggi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Robot yang beroperasi di lingkungan dalam ruang memerlukan kemampuan persepsi spasial yang akurat untuk navigasi dan manipulasi objek. Deteksi objek berbasis citra RGB dua dimensi konvensional hanya menyediakan posisi objek dalam koordinat piksel berupa kotak pembatas. Informasi ini tidak mencukupi karena robot memerlukan informasi jarak fisik absolut dari sensor kamera ke objek.

Untuk mengatasi keterbatasan ini, penggunaan kamera *RGB-D*—sensor yang menghasilkan citra warna dan informasi kedalaman secara sinkron—menjadi pendekatan populer. Metode sederhana untuk mengukur jarak objek adalah dengan mengambil koordinat kotak pembatas dari detektor objek, lalu menghitung nilai rata-rata kedalaman piksel di dalam kotak tersebut dari *depth map* (peta kedalaman). Peta kedalaman adalah citra dua dimensi di mana setiap nilai piksel mewakili jarak fisik objek dari sensor kamera.

Namun, metode sederhana ini memiliki kelemahan mendasar. Kotak pembatas dua dimensi hasil detektor objek sering kali mencakup piksel latar belakang di sekitarnya atau bagian dari lantai dan dinding. Jika piksel latar belakang ini ikut dihitung, nilai estimasi jarak objek akan terdistorsi secara signifikan, terutama ketika objek berada jauh dari latar belakang atau memiliki bentuk tidak beraturan. Oleh karena itu, diperlukan mekanisme untuk memisahkan data kedalaman milik objek (*foreground*) dari data kedalaman latar belakang sebelum jarak dihitung.

## Ide Utama
Gagasan utama dari penelitian ini adalah melakukan penyaringan data kedalaman secara lokal di dalam wilayah kotak pembatas hasil prediksi YOLO untuk memisahkan objek target dari latar belakangnya. Proses ini dinamakan *depth foreground prediction* (prediksi latar depan kedalaman). Sistem ini menerima masukan berupa citra RGB dan peta kedalaman yang saling terdaftar (*aligned*). 

Citra RGB diproses oleh model YOLO untuk mendeteksi objek dan menghasilkan koordinat kotak pembatas 2D. Koordinat ini digunakan untuk memotong wilayah yang sesuai pada peta kedalaman. Di dalam wilayah potongan tersebut, sebuah algoritma segmentasi kedalaman adaptif memisahkan piksel objek (*foreground*) dari piksel non-objek (*background*). Jarak akhir objek dari robot dihitung hanya dengan merata-ratakan nilai kedalaman dari piksel-piksel yang teridentifikasi sebagai *foreground*. Skema ini menghindari derau (*noise*) dari latar belakang tanpa memerlukan segmentasi instans (*instance segmentation*) berbasis piksel yang mahal secara komputasi.

## Cara Kerja Langkah demi Langkah
Sistem pengukuran jarak ini beroperasi dalam alur kerja modular yang terbagi menjadi beberapa tahapan utama.

```
           +----------------------------------------+
           |       Kamera RGB-D (Sensors)           |
           +-------------------|--------------------+
                               |
                +--------------+--------------+
                |                             |
         [Citra RGB]                     [Peta Kedalaman]
                |                             |
                v                             |
     +--------------------+                   |
     | Deteksi Objek YOLO |                   |
     +----------|---------+                   |
                |                             |
         [Bounding Box]                       |
         (xmin,ymin,xmax,ymax)                |
                |                             |
                +--------------+--------------+
                               |
                               v
               +-------------------------------+
               |    Pemotongan Bounding Box    |
               |      pada Peta Kedalaman      |
               +---------------|---------------+
                               v
               +-------------------------------+
               |  Depth Foreground Prediction  |
               | (Pemisahan Objek vs Latar)    |
               +---------------|---------------+
                               v
               +-------------------------------+
               |  Estimasi Jarak Rata-rata     |
               |      Piksel Foreground        |
               +---------------|---------------+
                               v
                     [ Jarak Objek (meter) ]
```

### 1. Akuisisi Data Sensor
Kamera RGB-D menangkap citra RGB dan peta kedalaman secara simultan. Kedua data diselaraskan secara spasial sehingga setiap koordinat piksel $(u, v)$ pada citra RGB merujuk pada titik fisik yang sama pada peta kedalaman.

### 2. Deteksi Objek 2D Menggunakan YOLO
Citra RGB dimasukkan ke dalam model YOLO untuk mendeteksi objek. Model memprediksi kotak pembatas $B_i = (x_{min}, y_{min}, x_{max}, y_{max})$ dan skor kepercayaan (*confidence score*) untuk setiap objek yang terdeteksi.

### 3. Pemotongan Wilayah Kedalaman (*Depth Patch Extraction*)
Koordinat $B_i$ dari hasil deteksi YOLO diterapkan pada peta kedalaman untuk memotong wilayah persegi panjang yang bersesuaian, menghasilkan matriks kedalaman lokal $D_i$ berukuran $W \times H$, di mana $W = x_{max} - x_{min}$ dan $H = y_{max} - y_{min}$.

### 4. Prediksi Latar Depan Kedalaman (*Depth Foreground Prediction*)
Pada matriks kedalaman lokal $D_i$, nilai kedalaman dianalisis untuk memisahkan objek dari latar belakang. Karena objek fisik umumnya bersifat kontinu dan berada pada jarak relatif seragam, nilai kedalamannya akan mengelompok pada rentang tertentu. Algoritma melakukan langkah-langkah berikut:
- **Analisis Histogram:** Histogram dari nilai kedalaman di dalam $D_i$ dihitung untuk mengidentifikasi distribusi frekuensi jarak.
- **Deteksi Puncak Terdekat:** Puncak pertama pada histogram (jarak terdekat yang signifikan) diasumsikan sebagai representasi dari objek target (*foreground*). Piksel dengan nilai kedalaman yang mendekati nol (karena kegagalan sensor) diabaikan.
- **Penerapan Ambang Batas Adaptif:** Ambang batas dinamis ditentukan berdasarkan nilai deviasi standar di sekitar puncak kedalaman tersebut. Piksel dengan nilai kedalaman $d$ yang memenuhi kriteria $|d - d_{peak}| \le \tau$ diklasifikasikan sebagai piksel *foreground*, di mana $d_{peak}$ adalah nilai kedalaman pada puncak histogram dan $\tau$ adalah parameter ambang batas toleransi (misalnya, $15\text{ cm}$). Piksel di luar rentang ini diklasifikasikan sebagai *background* dan dibuang.

### 5. Perhitungan Jarak Akhir
Jarak objek $D_{final}$ dihitung dengan merata-ratakan nilai semua piksel kedalaman yang tergolong *foreground*. Penyaringan piksel latar belakang ini menghindari bias estimasi jarak, dan hasilnya dikirim ke modul navigasi robot.

## Eksperimen dan Hasil
Eksperimen dilakukan untuk mengevaluasi akurasi deteksi objek dan keandalan pengukuran jarak pada lingkungan dalam ruang. Platform robot mobil yang digunakan dilengkapi dengan kamera RGB-D Intel RealSense D435. Dataset pengujian mencakup objek rumah tangga yang diletakkan pada variasi jarak antara $1,0$ hingga $4,0$ meter dari kamera.

Kinerja model deteksi YOLO dievaluasi menggunakan metrik *mean Average Precision* (mAP). Model YOLO yang digunakan mampu mendeteksi objek dengan mAP pada IoU (Intersection over Union) 0,5 mencapai $88,2\%$, menunjukkan performa deteksi yang andal untuk skenario navigasi robot. IoU adalah metrik untuk mengukur tingkat tumpang tertindih antara kotak pembatas prediksi dengan kotak pembatas aktual.

Untuk evaluasi pengukuran jarak, metode yang diusulkan dibandingkan dengan metode pembanding:
1. **Metode Rata-rata Kotak Pembatas Standar:** Menghitung rata-rata seluruh piksel di dalam kotak pembatas tanpa penyaringan.
2. **Metode Piksel Pusat (*Centroid*):** Mengambil nilai kedalaman hanya pada piksel pusat geometris dari kotak pembatas.

Hasil perbandingan kesalahan estimasi jarak rata-rata dirangkum dalam tabel berikut:

| Jarak Aktual (m) | Error Rata-rata Standar (cm) | Error Metode Centroid (cm) | Error Metode Usulan (cm) |
| :---: | :---: | :---: | :---: |
| 1,0 | 4,2 | 3,1 | 1,1 |
| 2,0 | 8,5 | 5,4 | 1,8 |
| 3,0 | 12,3 | 7,8 | 2,2 |
| 4,0 | 17,9 | 11,2 | 2,7 |

Hasil ini menunjukkan bahwa metode *depth foreground prediction* yang diusulkan mampu mempertahankan kesalahan estimasi jarak di bawah $3,0\text{ cm}$ bahkan pada jarak $4,0\text{ meter}$. Sebaliknya, metode rata-rata standar mengalami kesalahan hingga $17,9\text{ cm}$ karena piksel latar belakang mulai mendominasi area kotak pembatas ketika ukuran objek mengecil seiring bertambahnya jarak. Kecepatan pemrosesan sistem secara keseluruhan mencapai $32\text{ FPS}$ (frame per detik) pada perangkat komputasi tersemat (*embedded*), membuktikan kelayakan metode ini untuk navigasi robot waktu nyata.

## Kelebihan dan Keterbatasan
Sistem pengukuran jarak berbasis YOLO dan prediksi *foreground* kedalaman ini memiliki beberapa kelebihan dari sisi rekayasa dan kinerja praktis. Pertama, metode ini sangat efisien karena proses analisis kedalaman dan segmentasi lokal hanya dilakukan pada area kotak pembatas hasil YOLO, bukan pada seluruh citra kedalaman. Hal ini menghemat sumber daya komputasi dibandingkan metode segmentasi semantik penuh. Kedua, akurasi pengukuran jarak menjadi sangat stabil terhadap variasi latar belakang, karena piksel latar belakang disaring secara dinamis berdasarkan analisis sebaran histogram lokal.

Namun, secara konseptual dan praktis, metode ini memiliki beberapa keterbatasan penting. Kinerja sistem sangat bergantung pada kualitas keluaran dari sensor kedalaman RGB-D. Pada objek dengan permukaan spekular (seperti kaca, cermin, atau logam mengkilap), sensor inframerah sering kali gagal mendeteksi kedalaman, menghasilkan nilai kedalaman nol (*depth holes*). Kegagalan ini akan mengganggu distribusi histogram dan menurunkan akurasi deteksi *foreground*. 

  Selain itu, metode ini dirancang khusus untuk lingkungan dalam ruang. Penerapan pada luar ruang akan mengalami penurunan kinerja drastis karena cahaya matahari menginterfere dengan pola inframerah aktif yang dipancarkan oleh kamera RGB-D konsumen. Terakhir, jika terdapat dua objek dengan kelas yang sama yang saling tumpang tindih secara mendalam di dalam satu kotak pembatas, pemisahan *foreground* berbasis histogram sederhana dapat mengalami ambiguitas dalam menentukan objek target.

## Kaitan dengan Bab Lain
Penelitian ini merupakan bagian penting dari klaster **YOLO plus RGB-D** yang berfokus pada integrasi fitur visual 2D dan informasi kedalaman 3D untuk persepsi robotika.

Metode penggabungan modular (deteksi visual 2D diikuti pemrosesan kedalaman) menempatkan bab ini pada silsilah yang sama dengan [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md). Kedua makalah menggunakan YOLO untuk melokalisasi wilayah ketertarikan (*region of interest*), lalu mengekstraksi data spasial untuk tugas akhir robotik (estimasi jarak vs. estimasi titik genggam). Pendekatan modular ini juga sejalan dengan [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md) dan [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md) yang mengutamakan kecepatan eksekusi untuk skenario robot pelayan di dalam ruangan.

Sebaliknya, metode ini berbeda dari pendekatan fusi awal (*early fusion*) atau fusi menengah (*intermediate fusion*) seperti yang diusulkan oleh [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md) dan [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md). Makalah-makalah tersebut memodifikasi arsitektur *backbone* YOLO untuk menerima data RGB dan kedalaman secara bersamaan sejak lapisan pertama jaringan saraf, dengan tujuan meningkatkan akurasi deteksi kelas objek. Sementara itu, metode dalam bab ini menggunakan model YOLO RGB standar tanpa modifikasi arsitektur, dan hanya memanfaatkan data kedalaman pada tahap pasca-pemrosesan (*post-processing*) untuk ekstraksi koordinat 3D dan jarak fisik.

## Poin untuk Sitasi
Makalah ini dapat disitasi menggunakan kunci BibTeX berikut:
```bibtex
@inproceedings{chen2023depthyolo,
  title     = {Indoor Object Distance Measurement for Robots Based on YOLO and Depth Foreground Prediction},
  author    = {Chen, Yu-Chen and others},
  booktitle = {Proceedings of the IEEE International Conference on Advanced Robotics and Intelligent Systems (ARIS)},
  year      = {2023}
}
```

Secara singkat, kontribusi utama makalah ini yang aman untuk dirujuk dalam tinjauan pustaka adalah:
> Chen dkk. mengusulkan metode pengukuran jarak objek dalam ruang secara *real-time* dengan memadukan detektor objek YOLO dan algoritma *depth foreground prediction*. Metode ini mengisolasi data kedalaman objek target dari latar belakang pada potongan peta kedalaman di dalam kotak pembatas 2D, sehingga mampu mereduksi kesalahan estimasi jarak hingga kurang dari $3,0\text{ cm}$ pada jarak operasional sampai dengan $4,0\text{ meter}$.

**Catatan Verifikasi Akademik:** 
Terdapat ketidaksesuaian data bibliografis yang signifikan antara berkas `references.bib` pada repositori ini dengan basis data publikasi akademik global seperti IEEE Xplore. Di dalam `references.bib`, makalah dengan judul ini tercatat dengan penulis `Chen, Yu-Chen and others` dan diterbitkan di *Proceedings of the IEEE International Conference on Advanced Robotics and Intelligent Systems (ARIS) 2023*. Namun, penelusuran pada indeks IEEE Xplore menunjukkan bahwa makalah dengan judul yang sama persis ditulis oleh Maoliang Yin, Qiao Zhang, Wenfu Bi, dan Changchun Hua dari Yanshan University, serta dipresentasikan pada *2023 IEEE 13th International Conference on CYBER Technology in Automation, Control, and Intelligent Systems (CYBER)*. Penulis tinjauan menyarankan untuk melakukan verifikasi naskah fisik konferensi ARIS 2023 guna memastikan tidak adanya duplikasi publikasi atau kesalahan entri metadata pada repositori.
