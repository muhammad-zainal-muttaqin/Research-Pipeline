# Multi-Object Tracking in Agricultural Applications using a Vision Transformer for Spatial Association

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hernandez2024multi` |
| Judul asli | Multi-Object Tracking in Agricultural Applications using a Vision Transformer for Spatial Association |
| Penulis | Hernandez, Byron; Medeiros, Henry |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [hernandez2024multi.pdf](../pdf/hernandez2024multi.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109379

## Gambaran Umum
Makalah ini memperkenalkan kerangka pelacakan multi-objek (*multi-object tracking*, MOT) untuk pertanian bernama FloraTracktor+. Kerangka ini menambahkan modul asosiasi spasial berbasis *Local Feature Matching Transformer* (LoFTR) pada pelacak *tracking-by-detection* FloraTracktor, yaitu modifikasi Tracktor. Modul itu memperkirakan posisi global tiap objek dalam koordinat piksel sehingga objek yang keluar dari bidang pandang kamera (*field of view*, FOV) dan kembali masuk dapat diberi identitas yang sama.

Evaluasi memakai dua set data publik: LettuceMOT (selada, kamera RGB pada robot bergerak) dan AppleMOT, yaitu versi berbasis kotak pembatas yang diturunkan penulis dari AppleMOTS (apel, dari UAV dan sensor yang dikenakan). Pada LettuceMOT, FloraTracktor+ melampaui GIAOTracker dan LettuceTrack. Abstrak menyatakan peningkatan rerata hingga 25% terhadap hasil publik terbaik. Pada AppleMOT, metrik berbasis kotak pembatas yang dicapai sebanding dengan metrik berbasis segmentasi (MOTS) pada makalah AppleMOTS asli. Pelacak berjalan rata-rata 82,7±22 milidetik per bingkai, sekitar 12 bingkai per detik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pelacakan objek pertanian sulit karena objeknya homogen: tanaman dan buah memiliki ciri visual yang kurang khas, sehingga penampilan tidak cukup untuk mengidentifikasi ulang (*re-identification*, reID) individu. Variasi cahaya, cuaca, dan kekacauan latar menambah kesulitan. Pelacakan akurat dibutuhkan untuk penyemprotan otomatis (setiap tanaman diperlakukan tepat satu kali) dan untuk penghitungan buah dalam estimasi hasil panen.

Penulis menyatakan hanya dua set data publik MOT pertanian yang tersedia, yaitu AppleMOTS dan LettuceMOT. LettuceTrack, pelacak yang dirancang untuk LettuceMOT, memanfaatkan hubungan spasial antartanaman tetapi mengandalkan gerak robot lurus dengan sumbu tengah barisan sebagai jangkar. Pendekatan itu gagal bila robot tidak bergerak lurus, misalnya ketika robot keluar dari barisan untuk mengisi baterai atau bahan kimia lalu masuk kembali di titik lain. Tracktor++ sebagai pembanding mengandalkan modul terpisah untuk penyelarasan kamera, pembaruan gerak, dan reID, serta memerlukan label identitas yang konsisten secara temporal untuk pelatihan.

## Ide Utama
Penulis menggunakan posisi global objek sebagai satu-satunya petunjuk untuk asosiasi jangka panjang. Penampilan dianggap tidak cukup diskriminatif, sehingga pelacak hanya menyimpan perkiraan lokasi global objek yang sudah tidak aktif. Satu modul LoFTR menggantikan tiga modul terpisah pada Tracktor++ (penyelarasan kamera, gerak, dan reID). LoFTR menghasilkan korespondensi titik antara dua bingkai berurutan, dari situ dihitung homografi, dan posisi global kamera diperbarui. Objek baru pada bingkai saat ini dicocokkan dengan objek tak aktif pada koordinat global memakai algoritma Hungarian. Akibatnya, pelatihan tidak memerlukan anotasi pelacakan; detektor hanya memerlukan anotasi kotak pembatas.

## Cara Kerja Langkah demi Langkah
```
 Bingkai I(t), I(t-1)
   |-> FloraTracktor (Faster R-CNN + regresi kotak) -> track aktif, tak aktif,
   |                                                    kandidat baru p(t)
   |-> LoFTR -> korespondensi -> RANSAC -> homografi H(t-1,t) -> posisi x(t)
                      |
   Jarak Euclidean di koordinat global antara p(t) dan track tak aktif
   -> Hungarian -> aktifkan kembali bila jarak < d_p
```

### 1. Data
LettuceMOT terdiri atas delapan urutan video petak selada, direkam dengan kamera RGB pada platform robot: lima ribu empat ratus enam puluh enam bingkai (5.466) beresolusi 810×1080 piksel, 707 instans objek unik, dan 42.735 anotasi. Urutannya adalah straight1 sampai straight4 (gerak maju), B&F1 dan B&F2 (maju-mundur menghindari rintangan), serta O&I1 dan O&I2 (robot keluar dari barisan dan masuk lagi di titik lain).

AppleMOTS terdiri atas 12 urutan video yang direkam dengan UAV Matrice 210 RTK V2, UAV Parrot Anafi, dan sensor yang dikenakan: 1.673 bingkai beresolusi 1296×972, 2.304 instans apel unik, dan 86.000 masker teranotasi. Penulis mengubah masker menjadi kotak pembatas berformat MOT dan menamai hasilnya AppleMOT. Jumlah pohon dan lokasi kebun tidak dilaporkan pada bagian yang terbaca.

### 2. FloraTracktor
Detektor dasarnya adalah Faster R-CNN dengan kepala regresi *region of interest* (ROI). Berbeda dari Tracktor yang menjalankan tiga langkah *non-maximum suppression* (NMS) terpisah, FloraTracktor menjalankan satu langkah NMS pada gabungan deteksi baru dan kotak hasil regresi dari track aktif dengan satu ambang IoU $\lambda_{nms}$. Track tetap aktif bila skor kotak hasil regresi melebihi $s_{active}$; bila tidak, track menjadi tak aktif dan disimpan. Track baru dibuat bila skor kotak lebih besar dari $s_{new}$ dan centroidnya berada paling jauh $f_d \cdot \phi$ dari tepi citra, dengan $\phi = 2\sqrt{wh/\pi}$ sebagai diameter pendekatan lingkaran kotak. Semua track yang dinonaktifkan disimpan untuk asosiasi jangka panjang.

### 3. Modul asosiasi spasial
LoFTR menghasilkan korespondensi titik antara $I_{t-1}$ dan $I_t$. Homografi $H_{t-1,t}$ diestimasi dengan RANSAC dan algoritma $n$-titik, lalu posisi global kamera diperbarui. Centroid tiap kotak diterjemahkan ke koordinat global dengan menambahkan posisi kamera. Matriks jarak Euclidean antara kandidat baru dan kotak track tak aktif diselesaikan dengan algoritma Hungarian. Track tak aktif diaktifkan kembali hanya bila jaraknya di bawah ambang $d_p$, yaitu rata-rata diameter pendekatan lingkaran semua kotak yang terlibat.

### 4. Pengaturan eksperimen
Metrik: CLEAR-MOT (MOTA, IDP, IDR, IDF1) dan HOTA beserta DetA, AssA, AssRe, dan AssPr, dihitung dengan alat TrackEval. Untuk membandingkan dengan makalah LettuceMOT, detektor dilatih pada urutan straight1 dan straight3 dan diuji pada urutan lain. Untuk membandingkan dengan LettuceTrack, pelatihan memakai straight3 dan straight4. Parameter bawaan: $f_d = 1$, $s_{new} = 0,5$, $s_{active} = 0,5$, $\lambda_{nms} = 0,2$. Pada AppleMOT, protokol AppleMOTS dipakai: latih pada urutan 0001 sampai 0005, uji pada 0006 sampai 0012, dengan $f_d = \max(I_W, I_H)$.

## Eksperimen dan Hasil
Tabel 1 makalah (protokol LettuceMOT) membandingkan GIAOTracker dan FloraTracktor+ pada urutan uji. Tabel berikut mengutip sebagian barisnya (MOTA, HOTA, IDF1 dalam persen).

| Urutan | Metode | MOTA | HOTA | IDF1 |
|---|---|---|---|---|
| straight2 | GIAOTracker | 90,20 | 87,24 | 94,72 |
| straight2 | FloraTracktor+ | 98,30 | 98,21 | 98,50 |
| B&F1 | GIAOTracker | 91,93 | 68,66 | 59,66 |
| B&F1 | FloraTracktor+ | 98,12 | 98,24 | 98,56 |
| O&I1 | GIAOTracker | 89,91 | 65,61 | 58,73 |
| O&I1 | FloraTracktor+ | 97,34 | 74,11 | 61,30 |
| O&I2 | GIAOTracker | 51,30 | 52,90 | 46,25 |
| O&I2 | FloraTracktor+ | 95,38 | 72,61 | 58,06 |

Penulis melaporkan peningkatan *association accuracy* (AssA) hampir 50% pada urutan B&F, 12% pada straight, dan 5% pada O&I, serta peningkatan HOTA rerata 35% pada B&F, 10% pada straight, dan 15% pada O&I. Pada Tabel 2 (protokol LettuceTrack), FloraTracktor+ mencapai HOTA 98,52 pada straight1 dan 98,24 pada B&F1, dibandingkan dengan LettuceTrack 77,59 dan 76,81. Penulis menyatakan peningkatan asosiasi lebih dari 25%, IDF1 lebih dari 15%, dan HOTA lebih dari 25%. Urutan O&I tetap sulit karena sebagian bingkai tidak memuat objek.

Pada AppleMOT (Tabel 3, urutan uji 0006 sampai 0012), FloraTracktor dibandingkan dengan ByteTrack:

| Metode | MOTA | HOTA | DetA | AssA | IDF1 |
|---|---|---|---|---|---|
| ByteTrack | 32,99 | 38,21 | 28,86 | 50,96 | 45,21 |
| FloraTracktor | 48,55 | 45,45 | 60,08 | 34,81 | 42,39 |

Penulis menyebut AssA ByteTrack yang lebih tinggi terutama akibat DetA yang jauh lebih rendah, dan IDF1 kedua metode sebanding. PointTrack, metode terbaik pada makalah AppleMOTS, memperoleh MOTSA 52,9% dengan penyaringan "ignore regions" dan 46% tanpa penyaringan; penulis menyatakan hasilnya melampaui nilai tanpa penyaringan sebesar 2,5%. Teks tidak menyebut apakah Tabel 3 memakai FloraTracktor atau FloraTracktor+ pada bagian teks, tetapi tabel berlabel FloraTracktor.

Tabel 4 membandingkan pelacak pada LettuceMOT secara agregat (rerata ± 3 simpangan baku):

| Metode | MOTA | HOTA | IDF1 |
|---|---|---|---|
| Tracktor | 93,94 ± 0,92 | 81,71 ± 12,00 | 74,19 ± 18,88 |
| Tracktor++ | 97,01 ± 0,68 | 74,38 ± 6,44 | 67,03 ± 12,68 |
| FloraTracktor | 95,29 ± 0,91 | 83,81 ± 12,27 | 78,03 ± 17,70 |
| FloraTracktor+ | 97,74 ± 0,96 | 91,98 ± 10,77 | 88,82 ± 16,85 |

Analisis sensitivitas (Gambar 2) menunjukkan kinerja stabil ketika $s_{new}$, $s_{active}$, dan $\lambda_{nms}$ divariasikan antara 0,2 dan 0,8. Waktu eksekusi rata-rata 82,7±22 ms per bingkai (sekitar 12 fps) pada GPU NVIDIA GeForce 3090 dan CPU Intel Core i7-11700KF, dengan implementasi Python tanpa optimisasi. Penulis menyatakan metode tetap bekerja bila bingkai diturunkan dengan rasio 20:1, karena pada urutan straight sebuah objek terlihat selama 40 sampai 50 bingkai.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tidak memerlukan anotasi pelacakan; parameter sedikit dan kinerja stabil terhadap perubahan parameter; menangani gerak robot tidak lurus; berjalan dalam waktu nyata; dan kode tersedia secara publik. Metode ini juga ditujukan agar tidak kehilangan generalitas di luar pertanian.

Keterbatasan yang dinyatakan penulis: pada urutan O&I, bila FOV tidak memuat objek dalam waktu lama, galat posisi terakumulasi dan menimbulkan distorsi pada panorama hasil rekonstruksi; lokalisasi tetap akurat selama minimal satu objek terlihat. Penulis menilai ini penting bagi aplikasi yang memerlukan akurasi posisi kumulatif, dan merencanakan fusi sensor (GPS dan IMU) pada pekerjaan lanjutan. Ground truth untuk "ignore regions" pada AppleMOTS tidak tersedia publik, sehingga perbandingan MOTSA tidak sepenuhnya setara.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Metode mengasumsikan objek diam dan kamera bergerak pada permukaan yang dapat dijelaskan oleh satu homografi, asumsi yang kurang tepat untuk kanopi tiga dimensi dengan paralaks besar atau objek yang saling menutupi dari sudut berbeda. Tidak ada hitungan total objek atau galat hitungan yang dilaporkan, hanya metrik pelacakan. Pada AppleMOT, hasil berada di bawah PointTrack bila ignore regions disaring, dan AssA di bawah ByteTrack. Tabel 4 menyajikan simpangan baku yang besar untuk HOTA dan IDF1, sehingga selisih antarmetode perlu dibaca dengan hati-hati.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat lebih dari sekali dengan mekanisme pelacakan video berbasis lokasi global: homografi dari korespondensi LoFTR antarbingkai memperbarui posisi global kamera, dan track tak aktif diaktifkan kembali bila objek baru jatuh dekat posisinya pada koordinat global (algoritma Hungarian dengan ambang jarak rata-rata diameter objek). Identitas dipertahankan lintas keluar-masuknya objek dari FOV tanpa memakai ciri penampilan.

Hitungan tidak dilaporkan per kelas; set datanya berkelas tunggal (selada atau apel). Acuan evaluasinya adalah anotasi identitas pada bingkai video, bukan panen atau hitung lapangan, dan hitungan akhir objek tidak dilaporkan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah ide asosiasi spasial tanpa penampilan dan tanpa anotasi pelacakan, serta metrik asosiasi (AssA, IDF1, HOTA). Batasannya adalah asumsi bidang tunggal dan objek diam di bawah gerak kamera hampir planar; pada pohon sawit dengan sisi berbeda, penerapannya memerlukan model geometri yang lebih kaya.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hernandez2024multi`.

Ringkasan yang aman dikutip: Hernandez dan Medeiros (2024) mengusulkan FloraTracktor+, pelacak *tracking-by-detection* untuk pertanian yang menambahkan modul asosiasi spasial berbasis LoFTR dan homografi untuk memperkirakan posisi global objek serta mengaktifkan kembali track objek yang keluar dan masuk kembali ke FOV, tanpa anotasi pelacakan. Pada LettuceMOT, metode ini melampaui GIAOTracker dan LettuceTrack, dengan HOTA rerata 91,98 dan IDF1 88,82 pada Tabel 4. Pada AppleMOT, MOTA 48,55 dicapai oleh FloraTracktor, dan penulis menyatakan hasilnya sebanding dengan metode berbasis segmentasi.

Catatan verifikasi data: Angka pada Tabel 1 sampai 4 dan waktu eksekusi terbaca utuh pada teks ekstraksi; tabel tersebar dalam satu nilai per baris sehingga pencocokan kolom mengikuti urutan kolom pada judul tabel. Persentase peningkatan (50%, 12%, 5%, 35%, 10%, 15%, 25%, 15%) dan klaim "hingga 25%" pada abstrak adalah klaim penulis dan tidak dihitung ulang. Nilai IDF1 straight4 GIAOTracker tercetak 92,722 pada teks. Teks mencampur nama FloraTracktor+, FloraTracktor, dan PlantTracktor+ pada beberapa bagian. Gambar 2 sampai 5 tidak terbaca dari teks. Lampiran notasi dan Lampiran B hanya terbaca sebagian karena berkas teks dipotong pada bagian akhir; daftar pustaka tidak dibaca.
