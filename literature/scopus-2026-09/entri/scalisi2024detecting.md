# Detecting, mapping and digitising canopy geometry, fruit number and peel colour in pear trees with different architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `scalisi2024detecting` |
| Judul asli | Detecting, mapping and digitising canopy geometry, fruit number and peel colour in pear trees with different architecture |
| Penulis | Scalisi, Alessio; McClymont, Lexie; Peavey, Maddy; Morton, Peter; Scheding, Steve; Underwood, James; Goodwin, Ian |
| Tahun | 2024 |
| Venue | Scientia Horticulturae |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pear |

## Tautan Akses
- PDF: [scalisi2024detecting.pdf](../pdf/scalisi2024detecting.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2023.112737

## Gambaran Umum
Makalah ini memvalidasi platform bergerak bersensor (Cartographer, Green Atlas) untuk mengestimasi jumlah buah, warna kulit, dan persentase semburat merah (*blush coverage*) pada kebun pir dengan beberapa selebaran dan arsitektur pohon. Platform membawa dua kamera RGB, empat lampu strobo, pemindai LiDAR, dan GNSS. Jumlah buah diperoleh dari deteksi per citra yang dikalibrasi terhadap hitungan acuan; warna kulit dinyatakan dengan indeks perkembangan warna (*colour development index*, CDI) dari sudut hue pada piksel tengah kotak deteksi; geometri kanopi dihitung dari awan titik LiDAR. Penelitian dilakukan di Goulburn Valley, Victoria, Australia, pada dua musim panas (2020–21 dan 2021–22) di kebun eksperimen pir `ANP-0131` dengan lima sistem latih, dan satu musim di dua kebun komersial (`ANP-0131` dan `PremP009`).

Hasil utama: galat prediksi jumlah buah setelah kalibrasi kurang dari 6,5% pada semua sistem latih, dengan galat persen standar (%SE) 2,2% pada sistem dinding vertikal 2D (MLVT); galat kalibrasi di kebun komersial 4% (`PremP009`) dan 1% (`ANP-0131`). Prediksi semburat merah `ANP-0131` berhubungan dengan CDI dengan R2 = 0,666 dan RMSE 3,70%. Pada `PremP009`, CDI hasil platform sesuai dengan CDI alat kolorimeter genggam dengan koefisien korelasi konkordansi Lin rc = 0,794 dan %SE = 1,09. Jumlah buah dan semburat merah menurun dengan bertambahnya ukuran kanopi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengelolaan beban buah dan mutu buah di kebun sering bertumpu pada subsampel kecil atau pengamatan visual subjektif oleh pekerja musiman berpengalaman terbatas, sementara biaya tenaga kerja meningkat. Industri pir Australia menghadapi kenaikan biaya dan penurunan permintaan domestik, sehingga seleksi dengan warna merah menarik (semburat atau merah penuh) menjadi sasaran pemuliaan. Untuk kultivar `ANP-0131`, persentase semburat merah menentukan *packout*, sedangkan untuk `PremP009` intensitas warna merah merupakan parameter mutu.

Menurut penulis, belum ada bukti yang jelas bahwa penginderaan jarak jauh atau proksimal mampu memprediksi fitur pohon secara andal dan konsisten pada skala besar di kebun pir dengan konfigurasi sistem latih beragam. Deteksi buah umumnya terganggu oleh perubahan iluminasi, oklusi dedaunan, tumpang tindih buah, dan buah pada baris di sebelahnya; deteksi pada kanopi 2D lebih baik daripada 3D pada apel dan buah batu. Hipotesis penelitian adalah bahwa kinerja visi mesin untuk deteksi buah dan estimasi fitur buah memburuk pada kanopi 3D dibanding sistem 2D karena deteksi yang hilang.

## Ide Utama
Platform dipakai sebagai alat ukur yang divalidasi pada beberapa arsitektur pohon: deteksi per citra dikalibrasi terhadap jumlah buah acuan melalui regresi linear dengan intersep nol, warna kulit diestimasi dari CDI tanpa kalibrasi, dan geometri kanopi dari LiDAR dikaitkan dengan jumlah buah dan semburat merah. Hasilnya dipetakan secara geografis sehingga variabilitas spasial dapat dilihat sebagai peta panas. Karena sampel platform adalah citra (rerata CDI buah terdeteksi per citra), sebaran semburat merah yang diprediksi lebih sempit daripada sebaran populasi buah; penulis mengoreksinya dengan memperbesar residu terhadap rerata sampel.

## Cara Kerja Langkah demi Langkah

### 1. Lokasi, kultivar, dan rancangan percobaan
Kebun eksperimen `ANP-0131` di Tatura SmartFarm ditanam pada 2013 dengan jarak baris 4,5 m. Lima sistem latih diuji: *spindle* (SP), *central leader* (CL), *vase* (VA), *multileader open Tatura trellis* (MLOT), dan *multileader vertical trellis* (MLVT). SP, CL, VA, dan MLOT dianggap kanopi 3D; MLVT dianggap dinding berbuah 2D. Rancangannya blok acak lengkap petak terbagi dengan tiga ulangan, kecuali MLOT dan MLVT dengan sembilan ulangan; tiap petak sepanjang 14 m dengan satu baris pengukuran tengah. Kebun komersial (Calimna Orchard, Ardmona) masing-masing seluas 4,4 ha dengan sistem Tatura trellis (Y): `PremP009` (jarak pohon 1,2 m, 2.083 pohon/ha, pindai 7 Februari 2022) dan `ANP-0131` (jarak pohon 1,5 m, 1.667 pohon/ha, pindai 22 Februari 2022).

### 2. Akuisisi citra
Platform Cartographer merekam citra RGB dengan lampu strobo dan data LiDAR. Pemindaian dilakukan pagi hari pukul 07.00 AEDT; kecepatan rerata 4,4 km/jam (2021) dan 8,2 km/jam (2022). Citra dicatat dengan selang 5 citra per detik. Ukuran sampel pada musim kedua dinyatakan memadai (n > 200). Jumlah citra total per sistem latih tercantum di Tabel 2, misalnya 1.590 dan 1.515 citra untuk MLOT dan MLVT pada tahun pertama, serta 263, 251, 270, 896, dan 753 citra untuk SP, CL, VA, MLOT, dan MLVT pada tahun kedua. Arsitektur detektor pembelajaran mendalam yang dipakai platform tidak dijelaskan dalam makalah ini; makalah hanya menyebut model pembelajaran mendalam menghasilkan kotak deteksi buah pir dan merujuk validasi terdahulu pada apel dan buah batu.

### 3. Kalibrasi jumlah buah
Pemindaian dilakukan pada kedua sisi potongan baris pendek (7 sampai 10 m). Hitungan acuan di kebun eksperimen diperoleh saat panen dengan mesin penyortir buah komersial berpenginderaan optik (InVision 9000). Deteksi per citra dikalibrasi terhadap jumlah buah per hektare dengan regresi linear berintersep nol, karena jarak antarpohon berbeda antarsistem sehingga jumlah pohon yang tampak per citra bervariasi. Di kebun komersial, acuan adalah hitungan manual dengan pencacah klik pada empat zona 6 m (`PremP009`) dan tujuh zona 7,5 m (`ANP-0131`). Galat kalibrasi dinyatakan dengan galat standar kemiringan dan %SE.

### 4. Warna kulit
CDI dihitung dari sudut hue pada piksel tengah kotak deteksi. Untuk `ANP-0131`, hubungan CDI dengan persentase semburat merah hasil penyortir dibangun dengan regresi linear. Sebaran semburat merah pada lima kelas (0–20, 20–40, 40–60, 60–80, 80–100%) hasil prediksi dibandingkan dengan sebaran teramati, tanpa transformasi serta dengan residu digandakan atau ditigakalikan terhadap rerata: $x_1 = \mu + (\mu - x) \times 2$ dan $x_2 = \mu + (\mu - x) \times 3$, dengan nilai di bawah 0% dan di atas 100% dibulatkan. Untuk `PremP009`, CDI hasil platform divalidasi terhadap kolorimeter Bluetooth (60 buah per zona pada empat zona validasi).

### 5. Geometri kanopi dan analisis
LiDAR menghasilkan tinggi kanopi, luas kanopi (poligon di sekitar titik pada transek), kerapatan kanopi (rasio berkas yang memantul terhadap seluruh berkas), dan luas daun penampang (*cross-sectional leaf area*, CSLA = luas × kerapatan). Di kebun komersial `ANP-0131`, hubungan dianalisis pada 126 petak semu berukuran 12 m × 15 m setelah dua baris petak penyangga di tepi dibuang. Analisis memakai ANOVA, uji-t, regresi linear, dan uji lanjut Games-Howell di R; peta panas dibuat di QGIS.

## Eksperimen dan Hasil
Kalibrasi jumlah buah di kebun eksperimen (Tabel 3, regresi berintersep nol; kemiringan lebih besar berarti deteksi per hitungan acuan lebih tinggi):

| Sistem latih | Tahun 1: kemiringan (%SE) | Tahun 2: kemiringan (%SE) | Gabungan: kemiringan (%SE) |
|---|---|---|---|
| SP | 0,301 (10,3) | 0,529 (5,1) | 0,474 (6,4) |
| CL | 0,274 (5,6) | 0,450 (5,9) | 0,419 (5,6) |
| VA | 0,361 (5,2) | 0,466 (6,1) | 0,382 (4,6) |
| MLOT | 0,262 (4,9) | 0,332 (5,3) | 0,294 (4,0) |
| MLVT | 0,505 (2,8) | 0,689 (2,1) | 0,653 (2,2) |

Kemiringan MLOT dan MLVT berbeda nyata (p < 0,05) satu sama lain dan dari VA, SP, dan CL; kemiringan MLOT paling rendah dan MLVT paling tinggi. Di kebun komersial, kemiringan 0,588 (`PremP009`, galat 4%) dan 0,497 (`ANP-0131`, galat 1%).

Warna kulit dan sebaran semburat merah (Tabel 4; tahun 1 dan 2 digabung): populasi buah teramati 85.484 buah dengan rerata 26,3% dan SD 17,3; prediksi dari 2.798 citra memiliki rerata 25,9% dengan SD 6,58 (tanpa transformasi), 13,2 (residu digandakan), dan 19,1 (residu ditigakalikan).

| Galat dalam kelas (%) | Tanpa transformasi | Residu 2x | Residu 3x |
|---|---|---|---|
| Kelas 0–20% | 21 | 5 | 0 |
| Kelas 20–40% | 40 | 13 | 1 |
| Kelas 40–60% | 5 | 5 | 1 |
| Kelas 60–80% | 3 | 2 | 2 |
| Kelas 80–100% | 1 | 1 | 0 |

Hubungan CDI dengan semburat merah menghasilkan R2 = 0,666 (p < 0,001) dan RMSE 3,70% (RMSE dari abstrak); galat rerata semburat merah satu blok kurang dari 1,0%. Pada `PremP009`, rc = 0,794 dan %SE = 1,09; CDI zona hijau-karat 0,735, oranye-karat 0,770, merah-karat 0,775, dan oranye-merah 0,778. Rasio varians teramati terhadap prediksi adalah 2,4 kali.

Geometri kanopi tahun 2 (Tabel 5, rerata): tinggi kanopi 4,06 (SP), 3,95 (CL), 3,83 (VA), 3,31 (MLOT), dan 4,09 m (MLVT); lebar 1,98, 2,04, 2,38, 3,07, dan 1,53 m; luas 4,14, 4,03, 4,65, 3,92, dan 3,14 m2; kerapatan 0,60, 0,51, 0,50, 0,67, dan 0,63; CSLA 2,49, 2,10, 2,40, 2,61, dan 1,98 m2. Di kebun komersial `ANP-0131` tinggi kanopi 3,50 m, lebar 2,37 m, luas 3,24 m2, kerapatan 0,658, dan CSLA 2,20 m2.

Hubungan dengan geometri kanopi: pada kebun eksperimen, sistem latih digabung karena pemisahan menurunkan mutu hubungan; jumlah buah dan semburat merah menurun dengan CSLA (R2 pada kebun eksperimen 0,340 dan 0,339). Di kebun komersial, R2 adalah 0,536 (jumlah buah terhadap CSLA) dan 0,651 (semburat merah terhadap CSLA); kemiringan hubungan jumlah buah berbeda nyata antara kedua kebun (p < 0,001), sedangkan kemiringan semburat merah tidak (p > 0,05). Efisiensi jumlah buah per CSLA di kebun komersial adalah 50,8 (±3,14) buah m^-2 dan semburat merah per CSLA 10,9 (±0,253). MLVT menunjukkan jumlah buah dan semburat merah per CSLA tertinggi.

## Kelebihan dan Keterbatasan
Kelebihan: pengujian pada lima sistem latih dan dua kultivar di dua musim serta dua kebun komersial; acuan hitung berupa penyortir buah komersial (kebun eksperimen) dan hitungan manual (kebun komersial); metrik galat terhadap acuan jelas; dan keluaran dapat dipetakan secara geografis sehingga zona prioritas intervensi dapat diidentifikasi. Penulis juga menunjukkan koreksi sebaran citra terhadap sebaran buah memperbaiki klasifikasi kelas semburat merah.

Keterbatasan yang dinyatakan penulis: kalibrasi jumlah buah berbeda antarsistem latih (kemiringan berbeda), sehingga kalibrasi harus spesifik terhadap arsitektur; hubungan antara fitur kanopi dan hasil sebaiknya dikembangkan per sistem latih, tetapi memerlukan data beberapa tahun; hubungan di kebun eksperimen dipengaruhi jaring pelindung di atas kebun, yang tidak ada pada kebun komersial; cahaya eksternal memengaruhi warna piksel pada visi mesin pada umumnya; dan sistem 2D memerlukan pengelolaan lebih khusus pada tahun-tahun awal setelah penanaman. Dari data ketersediaan, data hanya tersedia atas permintaan yang wajar kepada penulis korespondensi. Dua penulis dan satu penulis lain adalah pendiri Green Atlas, produsen platform, dan menyatakan kepentingan komersial.

Menurut pembacaan ringkasan ini, deteksi per citra dikalibrasi menjadi jumlah buah per hektare per sistem latih dan tidak ada mekanisme yang melacak identitas buah antarcitra atau antarsisi baris; karena citra direkam 5 per detik, buah yang sama dapat muncul pada beberapa citra dan hal ini diserap oleh faktor kalibrasi (kemiringan) alih-alih ditangani secara eksplisit. Menurut pembacaan ringkasan ini, kinerja detektor (presisi, *recall*, mAP) tidak dilaporkan, dan penurunan kemiringan pada kanopi 3D hanya diatribusikan kepada oklusi tanpa pengukuran langsung. Menurut pembacaan ringkasan ini, galat 6,5% dan %SE adalah galat kalibrasi (kecocokan regresi), bukan galat prediksi pada data uji terpisah.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali dengan mekanisme pencocokan identitas. Kedua sisi potongan baris dipindai dan citra direkam berurutan, tetapi hitungan diperoleh dari jumlah deteksi per citra yang dikalibrasi dengan regresi linear terhadap hitungan acuan; pengulangan pengamatan buah yang sama diserap oleh koefisien kalibrasi spesifik per sistem latih. Hal ini tergolong koreksi statistik (pengganti identitas), dengan kemiringan kalibrasi berbeda antarsistem latih (0,294 sampai 0,653 pada data gabungan) yang menunjukkan bahwa faktor itu bergantung pada arsitektur kanopi. Hitungan jumlah buah tidak dilaporkan per kelas; kelas hanya muncul pada sebaran semburat merah (lima kelas persentase) yang dibangun dari CDI, bukan hitungan buah per kelas.

Acuan hitung adalah hasil penyortir optik saat panen (kebun eksperimen) dan hitungan manual dengan pencacah klik di zona kalibrasi (kebun komersial), bukan anotasi citra. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan kalibrasi per arsitektur kanopi terhadap acuan lapangan (kemiringan berbeda antara kanopi 2D dan 3D), pemisahan galat antar kelas sebaran dari galat rerata blok, serta koreksi varians sampel berbasis citra terhadap populasi buah. Makalah tidak memberikan metode untuk menyatukan identitas buah antarsisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `scalisi2024detecting`.

Scalisi dkk. (2024) memvalidasi platform bergerak bersensor RGB, strobo, dan LiDAR untuk mengestimasi jumlah buah, warna kulit, dan semburat merah pada pir dengan lima sistem latih di Australia. Setelah kalibrasi regresi linear terhadap hitungan acuan, galat jumlah buah kurang dari 6,5% pada semua sistem latih dan 2,2% pada dinding vertikal 2D; galat kalibrasi di dua kebun komersial adalah 4% dan 1%. Semburat merah `ANP-0131` diprediksi dari CDI dengan R2 = 0,67 dan RMSE 3,70%. Kalibrasi jumlah buah bergantung pada arsitektur pohon, dan jumlah buah serta semburat merah menurun dengan bertambahnya luas daun penampang kanopi.

Catatan verifikasi data: angka %SE dan kemiringan kalibrasi tercantum di Tabel 3; galat kebun komersial di Bagian 3.1.2; R2 0,666 di Bagian 3.2.1 dan R2 0,67 serta RMSE 3,70% di abstrak (RMSE tidak ditemukan ulang di badan teks); statistik sebaran dan galat kelas di Tabel 4; rc = 0,794 dan %SE = 1,09 di Bagian 3.2.2; geometri kanopi di Tabel 5 dan Bagian 3.3; R2 hubungan CSLA di Bagian 3.4.2. Teks ekstraksi terbaca baik, termasuk tabel; grafik (Gambar 2 sampai 11) tidak terbaca sehingga nilai R2 tiap panel Gambar 7 tidak dapat dilaporkan. Arsitektur dan kinerja detektor tidak dapat diverifikasi dari makalah ini.
