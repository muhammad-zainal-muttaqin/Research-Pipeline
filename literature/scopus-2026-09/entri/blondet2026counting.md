# Counting Avocados in Orchard Videos Using a YOLO and BoT-SORT-Based Architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `blondet2026counting` |
| Judul asli | Counting Avocados in Orchard Videos Using a YOLO and BoT-SORT-Based Architecture |
| Penulis | Blondet, Diego Albitres; Alvarez, Franco Galindo; Cubas, Carlos Fernando Montoya |
| Tahun | 2026 |
| Venue | Communications in Computer and Information Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | avocado |

## Tautan Akses
- PDF: [blondet2026counting.pdf](../pdf/blondet2026counting.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-032-20322-9_36

## Gambaran Umum
Makalah prosiding (SIMBig 2025, CCIS 2895) ini membangun sistem pencacahan buah alpukat Hass dari video kebun komersial di Peru. Sistem memakai YOLOv8m untuk mendeteksi buah pada tiap bingkai dan BoT-SORT dengan modul identifikasi ulang (*re-identification*, ReID) untuk menautkan deteksi antarbingkai. Jumlah ID unik yang dihasilkan pada satu video menjadi hitungan kumulatif buah.

Dataset terdiri atas 1.207 citra: 124 dari repositori publik dan 1.083 dari kebun mitra Frucontrol SAC, direkam dengan Google Pixel 8a pada 1080p dan 60 fps. Pada set uji, detektor mencapai presisi 0,953, *recall* 0,888, F1 0,919, mAP@0,5 0,953, dan mAP@[0,5:0,95] 0,788. Untuk pencacahan, sistem mencapai *Absolute Counting Precision* (ACP) 92,68%, *Mean Absolute Error* (MAE) 2,0, dan *Root Mean Square Error* (RMSE) 3,16 pada video evaluasi.

Pelacakan per bingkai lebih lemah: MOTA berkisar 39,6% sampai 67,4%. Penulis menyatakan bahwa pengaturan BoT-SORT sengaja mengutamakan ketepatan hitungan akhir daripada kesinambungan lintasan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Peru adalah pengekspor alpukat Hass terkemuka, tetapi penulis menyatakan belum ada solusi pencacahan otomatis yang tervalidasi pada kondisi produksi nyata. Hitung manual dinilai tidak akurat, mahal karena memerlukan pengamat ahli, dan lambat dalam cakupan. Kondisi lapangan menyulitkan deteksi: kerapatan buah tinggi, oklusi parsial (sebagian buah tertutup daun lebih dari 50%), dan kemiripan warna antara buah hijau gelap dan daun.

## Ide Utama
Pencacahan dilakukan sebagai penghitungan ID unik dari pelacak pada satu video, bukan penjumlahan deteksi per bingkai. Agar tidak terjadi hitungan ganda, parameter asosiasi BoT-SORT disetel konservatif dan modul ReID diaktifkan sehingga buah yang sempat tertutup daun dapat menerima kembali ID aslinya. Penulis menerima pelacakan yang lebih terputus demi hitungan akhir yang lebih akurat.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi dan penyusunan data
Foto dan video diambil di kebun alpukat Hass sekitar tengah hari di bawah sinar matahari langsung, saat buah berada pada tingkat kematangan seragam, sekitar dua minggu sebelum panen. Dari video diambil satu bingkai per detik. Dataset tersedia di Roboflow Universe. Penulis sengaja menargetkan kondisi sulit, dan anotator dilatih melabeli buah yang tertutup sebagian. Jumlah pohon dan jumlah kebun tidak dilaporkan.

Tiap citra dibagi dua untuk menggandakan jumlah sampel dan menambah rincian. Augmentasi Roboflow menghasilkan tiga variasi per citra latih, sehingga total 2.897 instans menurut makalah (flip horizontal dan vertikal, rotasi ±15°, saturasi ±25%, kecerahan ±15%, eksposur ±10%, blur sampai 2,5 piksel, derau Gauss pada sampai 0,1% piksel). Pembagian data adalah 80% latih, 10% validasi, dan 10% uji.

### 2. Detektor
YOLOv8m dari pustaka Ultralytics dipakai tanpa mengubah struktur internal maupun hiperparameter, dengan ukuran masukan 640 × 640 piksel dan ukuran *batch* otomatis. Pelatihan maksimum 100 epoch dengan penghentian dini bila validasi tidak membaik selama 20 epoch, pada Google Cloud Colab Enterprise dengan GPU Tesla T4 (16 GB).

### 3. Pelacakan dan pencacahan
BoT-SORT bawaan Ultralytics dipakai dengan penyesuaian: ambang asosiasi maksimum dan minimum 0,38 dan 0,12, ambang inisialisasi lintasan baru 0,6, ambang pencocokan lintasan ke lintasan 0,4, ambang kedekatan 0,2, ambang penampakan 0,5, dan ReID aktif. Sistem menyimpan daftar global ID lintasan unik, dan keluaran akhir adalah jumlah ID unik pada video.

### 4. Data evaluasi pencacahan
Video representatif dianotasi dengan CVAT.ai: semua alpukat yang terlihat pada tiap bingkai diidentifikasi, dan hitungan kumulatif sistem dibandingkan dengan acuan (*ground truth*, GT) itu.

## Eksperimen dan Hasil
Detektor dibandingkan dengan CS YOLOv5s (dari pembanding hijau pepper), YOLOv7, dan YOLOv11m pada kondisi pelatihan yang sama.

| Model | mAP@0,5 | mAP@0,5:0,95 | Presisi | *Recall* | F1 |
|---|---|---|---|---|---|
| CS YOLOv5s | 0,828 | 0,557 | 0,782 | 0,779 | 0,780 |
| YOLOv7 | 0,952 | 0,729 | 0,931 | 0,879 | 0,904 |
| YOLOv11m | 0,946 | 0,766 | 0,931 | 0,889 | 0,910 |
| YOLOv8m | 0,953 | 0,788 | 0,952 | 0,888 | 0,919 |

Pada matriks konfusi, penulis menyebut 1.646 instans alpukat, dengan 1.387 terdeteksi benar, 135 negatif palsu (terutama akibat oklusi parsial), dan 124 positif palsu (terutama daun berbentuk mirip alpukat). Model awal yang dilatih hanya dengan citra publik mencapai mAP@0,5 0,61 pada dataset ini, naik menjadi 0,953 setelah citra kebun ditambahkan (penulis menyebut kenaikan lebih dari 56%).

Hasil pencacahan per video (tabel pada makalah):

| Video | GT | Hitungan model | ACP (%) | MAE | MOTA (%) | MOTP (%) | ID *switch* |
|---|---|---|---|---|---|---|---|
| 001 | 57 | 57 | 100,0 | 0 | 67,4 | 95,1 | 9 |
| 002 | 11 | 13 | 81,82 | 2 | 67,2 | 92,4 | 1 |
| 003 | 54 | 60 | 88,89 | 6 | 43,9 | 95,7 | 4 |
| 004 | 78 | 78 | 100,0 | 0 | 39,6 | 96,2 | 3 |

Nilai agregat untuk YOLOv8m dan BoT-SORT pada empat video adalah ACP 92,68%, MAE 2, dan RMSE 3,16. Penulis membandingkan hasil ini dengan Du dkk. (2024) pada cabai hijau (ACP 95,33%, MAE 3,33, MOTA sekitar 90%) yang diperoleh pada kondisi lapangan terkendali.

## Kelebihan dan Keterbatasan
Kelebihan: data direkam di kebun komersial tanpa stabilisasi atau pengendalian lingkungan, hasil per video dilaporkan bersama metrik pelacakan, dan kompromi antara hitungan akhir dan kesinambungan lintasan dinyatakan secara terbuka. Penulis juga mempublikasikan dataset.

Keterbatasan yang dinyatakan penulis: MOTA lebih rendah daripada kondisi terkendali karena oklusi sementara, jarak buah yang bervariasi, dan fluktuasi cahaya. Penulis menyarankan pekerjaan lanjutan berupa penambahan variasi data (cahaya, tingkat oklusi, varietas, kematangan), aplikasi seluler atau pengambilan dengan drone, dan optimasi parameter pelacakan.

Menurut pembacaan ringkasan ini: (a) hanya empat video evaluasi dengan jumlah buah 11 sampai 78, sehingga ACP 92,68% bertumpu pada sampel yang sangat kecil; (b) teks menyebut tiga video representatif pada Bagian 3.6 dan 4.3, tetapi tabel memuat empat video; (c) video evaluasi tidak dipastikan terpisah dari video sumber citra latih; (d) tingkat kematangan seragam sehingga tidak ada hitungan per kelas; (e) jumlah 1.387 benar dan 135 negatif palsu tidak berjumlah 1.646, sehingga angka matriks konfusi tidak sepenuhnya konsisten; (f) presisi 0,953 identik dengan mAP@0,5.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan: BoT-SORT dengan ReID, ambang asosiasi yang disetel untuk menekan ID duplikat, dan penghitungan ID unik. Hitungan tidak dilaporkan per kelas, karena kematangan seragam dan hanya satu kelas buah. Acuan hitungnya adalah anotasi video (semua alpukat yang terlihat pada tiap bingkai), bukan hasil panen dan bukan hitung lapangan.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: (1) pola penyetelan pelacak untuk menekan hitungan ganda dengan konsekuensi lintasan lebih terputus, (2) pelaporan MAE, RMSE, dan ID *switch* bersama ACP. Keterbatasannya: pelacak hanya menjamin identitas dalam satu urutan video kontinu, sedangkan penyatuan identitas antar-sisi pohon yang tidak berurutan tidak ditangani.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `blondet2026counting`.

Blondet dkk. (2026) membangun sistem pencacahan alpukat Hass dari video kebun komersial di Peru dengan YOLOv8m dan BoT-SORT berfitur ReID. Detektor mencapai mAP@0,5 0,953, dan pencacahan mencapai ACP 92,68%, MAE 2,0, dan RMSE 3,16 pada empat video beranotasi, dengan MOTA 39,6% sampai 67,4%.

Catatan verifikasi data: Angka deteksi tertulis pada Bagian 4.2 dan tabel perbandingan model (Tabel 4). Angka per video tertulis pada Tabel 1 dan 3, serta agregat pada Tabel 2. Nilai agregat dapat dicocokkan dengan nilai per video (rata-rata ACP 92,68%, MAE 2, RMSE 3,16 dihitung ulang dari Tabel 1 sesuai). Hal yang tidak konsisten atau tidak dilaporkan: jumlah video (tiga pada teks, empat pada tabel), jumlah instans pada matriks konfusi, lokasi kebun, jumlah pohon, dan keterpisahan video evaluasi dari data latih. Teks ekstraksi terbaca utuh.
