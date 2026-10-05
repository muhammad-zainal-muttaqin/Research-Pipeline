# Multi-Object Tracking for Apple Counting in Orchards Using Stereo Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wei2025multi` |
| Judul asli | Multi-Object Tracking for Apple Counting in Orchards Using Stereo Vision |
| Penulis | Wei, Jiahua; Kevric, Ermin; Zach, Juri; Stelldinger, Peer; Rose, Hendrik Wilhelm |
| Tahun | 2025 |
| Venue | Conference Proceedings 2025 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wei2025multi.pdf](../pdf/wei2025multi.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor66923.2025.11512512

## Gambaran Umum

Makalah prosiding (IEEE MetroAgriFor 2025) ini mengusulkan kerangka pencacahan apel per pohon di kebun berbasis kamera stereo. Setiap deteksi dilokalisasi dalam sistem koordinat tergeoreferensi dengan memadukan GPS dan odometri visual, lalu dikaitkan ke pohon terdekat berdasarkan jarak Euklides. Buah dideteksi dengan YOLOv8x, dan dua algoritma pelacakan multi-objek (*multi-object tracking*, MOT), yaitu OC-SORT dan ByteTrack, dibandingkan untuk menjaga identitas buah antarbingkai berurutan.

Data diambil di kebun percobaan Esteburg dekat Hamburg, Jerman, pada empat kultivar apel (Elstar, Wellant, Rockit, dan Pia 41). Detektor mencapai mAP0.5:0.95 sebesar 0,56 dan skor F1 0,78. Pada validasi hitungan 30 pohon Elstar, kerangka ini menghasilkan 555 apel setelah penyaringan duplikat, dibandingkan 535 apel hasil hitung mesin, sehingga selisih total 20 apel, dengan RMSE 6,24% per pohon dan R² 0,96.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil panen apel umumnya bertumpu pada hitung manual pada subsampel kecil pohon yang diekstrapolasi ke seluruh kebun dengan model regresi. Penulis menyatakan sampel terbatas ini dapat menimbulkan galat besar karena pola berbuah bervariasi antartahun dan lokasi tumbuh. Hitungan dari citra tunggal rentan galat akibat oklusi parsial dan sudut pandang, sedangkan metode berbasis citra 2D rentan terhadap ambiguitas skala dan deteksi ganda dari beberapa sudut pandang.

Pengaitan otomatis buah ke pohon masih awal karena tajuk pohon saling menutupi dan pengamatan dari sisi depan dan belakang barisan pohon harus digabungkan. Pendekatan terdahulu yang disebut penulis memakai LiDAR untuk lokalisasi 3D dan asosiasi pohon, sedangkan karya ini terutama bergantung pada kamera stereo yang lebih murah dan mudah dipasang.

## Ide Utama

Buah dilacak antarbingkai dengan MOT sehingga identitas tiap buah tetap, kemudian posisinya diproyeksikan ke ruang 3D tergeoreferensi. Karena posisi ditetapkan dalam kerangka global, buah yang sama yang terlihat dari dua sisi barisan pohon dapat diidentifikasi melalui kedekatan koordinatnya, lalu duplikatnya dibuang. Aliran optik (*optical flow*) dari odometri visual ditambahkan ke filter Kalman pelacak untuk memperbaiki estimasi kecepatan pada laju bingkai rendah.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Platform pembawa multisensor dipasang pada gandengan tiga titik traktor sempit. Citra diambil dengan dua kamera industri Basler ace 2 Pro (a2A5328-15ucPRO, 24,4 MP, hingga 15 fps) dalam susunan stereo, dengan jarak kamera ke pohon tetap sekitar 1,5 m dan tinggi tajuk maksimum 3 m. Modul RTK-GNSS simpleRTK3B Heading (Septentrio mosaic-H) menyediakan georeferensi. LiDAR terpasang tetapi hanya dipakai untuk validasi. Komputasi tepi memakai NVIDIA Jetson AGX Orin, sedangkan pelatihan memakai stasiun kerja dengan GPU NVIDIA RTX 6000 Ada.

Citra diambil pada 22 Agustus (Elstar) dan 5 September 2024 (kultivar lain), menjelang panen, dengan kecepatan traktor rata-rata 1 m/s, resolusi 4608 × 5328, dan laju 5 fps. Kalibrasi stereo dilakukan di lapangan dengan pola PuzzleBoard. Sebanyak 200 citra dianotasi dengan kotak pembatas untuk deteksi, 131 bingkai berurutan Wellant dan Elstar dilabeli dengan lintasan untuk pelacakan, dan 30 pohon Elstar dipakai untuk validasi hitungan akhir. Anotasi dilakukan dengan CVAT.

### 2. Lokalisasi sensor

Odometri visual stereo dalam (*deep visual stereo odometry*, DVSO) yang dilatih secara swa-awasi menghasilkan aliran optik (berbasis PWC-Net yang disesuaikan), peta kedalaman padat, dan odometri kamera. Kedalaman dihitung dari disparitas, jarak dasar stereo, dan panjang fokus. *Unscented Kalman Filter* (UKF) memadukan odometri visual dengan observasi GNSS untuk memperoleh posisi dan orientasi global kamera serta mengoreksi pergeseran akumulatif.

### 3. Deteksi dan pelacakan

YOLOv8x dilatih awal pada COCO dan di-*fine-tune* pada data sendiri dengan augmentasi Albumentations; hiperparameter dicari dengan pencarian acak Ray Tune. ByteTrack memakai asosiasi dua tahap dengan algoritma Hungarian (deteksi berkeyakinan tinggi lalu rendah) berbasis IoU. OC-SORT menambahkan suku konsistensi gerak pada matriks biaya agar lebih tahan terhadap oklusi. Kecepatan dari aliran optik dimasukkan sebagai pengukuran tambahan pada filter Kalman, dengan derau pengukuran dimodelkan dari nilai kepastian aliran.

### 4. Asosiasi apel ke pohon dalam 3D

Pusat kotak tiap apel dipetakan ke ruang kamera 3D dengan matriks intrinsik dan kedalaman rerata dalam kotak (Persamaan 2), lalu ditransformasikan ke kerangka global dengan rotasi dan translasi dari UKF (Persamaan 3). Posisi pohon dicatat sekali dengan tiang berGNSS karena deteksi pohon tidak andal pada tajuk rapat. Apel dikaitkan ke pohon dengan jarak Euklides minimum (Persamaan 4). Pada validasi, hitungan dari kedua sisi tiap pohon digabung berdasarkan koordinat GPS global, dan apel yang berjarak lebih dekat daripada ambang berdasar diameter apel Elstar prapanen (diasumsikan 70 hingga 85 mm) dianggap duplikat sehingga satu di antaranya dibuang.

## Eksperimen dan Hasil

Detektor dievaluasi dengan validasi silang k-lipatan (80% latih, 20% validasi) dan mencapai mAP0.5:0.95 0,56 serta F1 0,78. Semua apel yang terlihat, termasuk yang tertutup lebih dari 90%, dianotasi. Pelacak dievaluasi pada Wellant (pohon spindel, kerapatan buah tinggi, oklusi relatif rendah) dan Elstar (tajuk rapat, buah lebih sedikit, oklusi berat). Tabel I makalah memuat hasil berikut.

| Pelacak | Aliran optik | Dataset | HOTA | MOTA | IDF1 | DeTA |
|---|---|---|---|---|---|---|
| ByteTrack | Tidak | Wellant | 0,59 | 0,62 | 0,66 | 0,63 |
| ByteTrack | Tidak | Elstar | 0,58 | 0,51 | 0,67 | 0,50 |
| ByteTrack | Ya | Wellant | 0,63 | 0,63 | 0,70 | 0,63 |
| ByteTrack | Ya | Elstar | 0,58 | 0,52 | 0,67 | 0,50 |
| OC-SORT | Tidak | Wellant | 0,61 | 0,68 | 0,74 | 0,64 |
| OC-SORT | Tidak | Elstar | 0,59 | 0,52 | 0,67 | 0,52 |
| OC-SORT | Ya | Wellant | 0,64 | 0,64 | 0,70 | 0,65 |
| OC-SORT | Ya | Elstar | 0,59 | 0,53 | 0,69 | 0,51 |

Di antara metode dengan aliran optik, OC-SORT memperoleh HOTA tertinggi (0,64 pada Wellant) dan dipilih untuk validasi hitungan. Penulis menjelaskan bahwa pada 5 fps filter Kalman menerima sedikit pembaruan sehingga inisialisasi acak berpengaruh besar; pelacak tanpa aliran optik tetap memberi hasil mirip karena kecepatan awal telah ditetapkan melalui optimasi hiperparameter Ray Tune, yang memerlukan konfigurasi ulang manual untuk tiap dataset.

Validasi hitungan memakai 30 pohon Elstar karena hanya kultivar ini yang dipanen dengan platform Pluk-O-Trak (Munckhof Fruit Tech Innovators) pada 2024 sehingga tersedia hitungan mesin. Total 535 apel terhitung mesin pada 30 pohon. Metode ini semula memperkirakan 619 apel, yang turun menjadi 555 setelah penerapan ambang duplikat, sehingga total selisih 20 apel (dihitung: 555 − 535), dengan RMSE 6,24% per pohon dan R² 0,96. Penulis menduga kelebihan hitung terutama berasal dari pertukaran identitas (*identity switch*; IDF1 0,69 pada Tabel I) dan dari penyertaan apel hijau Pia 41 pada data latih yang meningkatkan positif palsu karena mirip daun kecil. Karena tajuk rapat, banyak apel hanya terlihat dari satu sisi barisan sehingga dampak deteksi ganda lintas sisi kecil.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis adalah penggunaan kamera stereo yang hemat biaya dan mudah dipasang tanpa LiDAR pada alur pemrosesan, pengaitan buah ke pohon di ruang 3D yang mengatasi distorsi perspektif dan hitungan ganda dari sisi berlawanan, serta acuan hitung mesin yang menghindari bias hitung manual.

Keterbatasan yang dinyatakan penulis: data tambahan harus dikumpulkan dan dianotasi untuk menguji generalisasi; data buah berlabel 3D dari LiDAR diperlukan untuk mengembangkan pelacakan sepenuhnya dalam 3D; kinerja tanpa aliran optik bergantung pada inisialisasi kecepatan yang benar; dan *identity switch* serta positif palsu pada apel hijau menyebabkan kelebihan hitung.

Menurut pembacaan ringkasan ini, validasi hitungan hanya mencakup satu kultivar (Elstar) pada 30 pohon dan satu musim, sehingga generalisasi belum terbukti. Posisi pohon harus didaftarkan manual sekali. Ambang duplikat bergantung pada asumsi diameter apel 70 hingga 85 mm. Penyaringan ambang itu mengurangi estimasi dari 619 menjadi 555, sehingga hasil sensitif terhadap pilihan ambang, dan sensitivitas ini tidak dianalisis.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali melalui dua mekanisme. Pertama, pelacakan MOT antarbingkai berurutan (OC-SORT dan ByteTrack dengan filter Kalman dan aliran optik) untuk mempertahankan ID buah. Kedua, penggabungan hitungan dari kedua sisi barisan pohon dengan menyatukan deteksi yang berjarak lebih kecil daripada ambang diameter buah dalam koordinat global GPS dan odometri visual. Hitungan tidak dilaporkan per kelas karena hanya ada satu kelas (apel). Acuan hitungnya adalah hitung mesin pemanen (Pluk-O-Trak), bukan hitung manual atau anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan menyatukan deteksi lintas sisi berdasarkan kedekatan pada kerangka koordinat bersama dengan ambang berdasar ukuran objek, serta penggunaan acuan hitung dari sumber independen. Pada pemotretan sawit dari beberapa sisi pohon, pose kamera tidak diperoleh dari GNSS dan odometri berkesinambungan seperti pada platform traktor ini, sehingga bagian lokalisasi global tidak dapat dipindahkan secara langsung. Makalah tidak membahas atribut kelas.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `wei2025multi`.

Wei dkk. mengusulkan kerangka pencacahan apel 3D berbasis kamera stereo yang memadukan YOLOv8x, pelacakan OC-SORT dengan aliran optik, dan odometri visual yang difusikan dengan GNSS melalui UKF untuk menempatkan setiap apel pada koordinat global dan mengaitkannya ke pohon. Pada 30 pohon Elstar, metode ini menghasilkan 555 apel setelah penyaringan duplikat terhadap 535 apel hasil hitung mesin, dengan RMSE 6,24% per pohon dan R² 0,96.

Catatan verifikasi data: mAP0.5:0.95 0,56 dan F1 0,78 tertulis di seksi IV. Metrik pelacakan bersumber dari Tabel I (urutan sel tabel dibaca dari ekstraksi teks dan konsisten dengan teks). Abstrak menyebut HOTA 0,59, MOTA 0,52, dan IDF1 0,67 untuk OC-SORT pada data validasi, sedangkan Tabel I memberi 0,59, 0,53, dan 0,69 pada Elstar dengan aliran optik; perbedaan ini tidak dijelaskan makalah. Angka 535, 619, 555, selisih 20 apel, RMSE 6,24%, dan R² 0,96 bersumber dari seksi IV; selisih 20 apel juga tertulis di makalah, sedangkan 555 − 535 dihitung di sini sebagai pemeriksaan. Makalah tidak menjelaskan cara RMSE dinyatakan dalam persen, tidak melaporkan jumlah citra latih per kultivar, dan Gambar 4 (diagram sebar) tidak terbaca dari teks. Teks berbahasa Inggris dan terbaca baik.
