# Assessing a multi-camera system to enhance fruit visibility for robotic harvesting in a V-trellised apple orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `villacres2024assessing` |
| Judul asli | Assessing a multi-camera system to enhance fruit visibility for robotic harvesting in a V-trellised apple orchard |
| Penulis | Villacr\'es, Juan; Vougioukas, Stavros |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [villacres2024assessing.pdf](../pdf/villacres2024assessing.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109164

## Gambaran Umum
Makalah ini menilai seberapa besar penambahan kamera pada sudut elevasi dan azimut berbeda meningkatkan jumlah buah apel yang terlihat pada kanopi berbentuk V (*V-trellised*) di kebun apel Pink Lady. Tujuan terapannya adalah persepsi untuk robot pemanen, dengan catatan bahwa hasilnya juga relevan bagi estimasi hasil berbasis citra. Empat kamera RGB-D Intel RealSense D435i dipasang pada satu tiang di atas kereta dorong: kamera 1 tegak lurus terhadap bidang kanopi (acuan), dan tiga kamera lain memiliki posisi tetap relatif terhadap kamera 1 dengan orientasi bervariasi.

Penulis memperkenalkan *Multi-Camera Fruit Detection Ratio* (MC-FDR), yaitu jumlah buah yang terlihat oleh himpunan kamera tertentu dibagi jumlah buah yang terlihat oleh gabungan keempat kamera pada wilayah minat (*region of interest*, ROI) bersama. Anotasi dilakukan manual (bukan detektor otomatis) agar penilaian visibilitas bebas dari galat detektor. Satu kamera tegak lurus mencakup 86,3% sampai 88,3% buah yang terlihat oleh empat kamera, dua kamera (kamera 1 dan 3) mencapai 95,3% sampai 97,5%, dan tiga kamera (kamera 1, 2, 3) mencapai 98,8% sampai 99,7%.

Penulis menyimpulkan bahwa manfaat kamera ketiga dan keempat perlu dipertimbangkan terhadap biaya dan kerumitan tambahan. Makalah ini tidak melakukan pencacahan atau estimasi hasil; ia mengukur visibilitas buah.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi dan lokalisasi buah di dalam kanopi diperlukan untuk robot pemanen, estimasi hasil berbasis penglihatan, dan deteksi dini penyakit, tetapi terhambat oklusi oleh daun, cabang, dan buah lain. Oklusi memengaruhi pengenalan dan penghitungan buah sehingga menimbulkan galat estimasi hasil. Penulis menyatakan bahwa buah yang sepenuhnya tertutup tidak dapat dideteksi sensor RGB, dan menyederhanakan lingkungan (membuang daun atau buah sekitar) tidak realistis.

Penelitian sebelumnya yang dikutip penulis menilai visibilitas dengan satu kamera yang dipindah-pindah (misalnya Hemming dkk. pada paprika: sekitar 69% dengan satu pandangan dan 90% dengan banyak pandangan; Bulanon dkk. pada jeruk: hingga 91% dari sembilan sudut). Penulis menyatakan bahwa studi ini berbeda karena mengevaluasi beberapa kamera yang merekam secara serentak. Simulasi kanopi 3D tidak dipakai karena model terkalibrasi yang mencerminkan pemangkasan dan penjarangan kebun sebenarnya belum tersedia.

## Ide Utama
Visibilitas buah diukur dalam wilayah minat yang merupakan irisan proyeksi medan pandang (FoV) semua kamera pada bidang kanopi. Hitungan tolok ukur (*gold standard*) adalah gabungan buah yang terlihat pada keempat kamera, dan jumlah buah sebenarnya (hasil panen) sengaja tidak dipakai sebagai acuan karena tidak memengaruhi penghitungan perbaikan visibilitas. Kamera tambahan dipilih sudutnya agar sedapat mungkin berbeda dari kamera acuan, tanpa membuat irisan medan pandang terlalu kecil.

## Cara Kerja Langkah demi Langkah

```
 [4 kamera D435i + RTK GNSS]
      -> [kalibrasi ekstrinsik papan catur]
      -> [filter kedalaman > 3 m; proyeksi titik ke kamera acuan; ROI = irisan]
      -> [anotasi manual titik apel pada kamera acuan, proyeksi ke kamera lain]
      -> [MC-FDR untuk 1, 2, 3 dibanding 4 kamera]
```

### 1. Kebun dan akuisisi data
Pengujian berlangsung pada 14 Oktober 2022 di kebun apel Pink Lady di Lodi, California, AS (suhu rerata 19,6 °C, tanpa hujan, kelembapan sekitar 40%). Kanopi berbentuk V tanpa pemangkasan, penjarangan daun, atau pembuangan apel untuk mengurangi kelompok buah. Bagian atas kanopi selebar sekitar 1,4 m; tinggi apel terendah dan tertinggi sekitar 0,45 m dan 3,2 m; kerapatan sekitar 10 buah per meter persegi. Empat kamera RealSense D435i identik dipasang pada tiang di kereta yang ditarik manual sepanjang baris; posisi kereta dicatat dengan penerima RTK GNSS Piksi Multi pada 10 Hz. Citra 1280 × 720 pada 30 fps direkam antara pukul 11.00 dan 14.00 dengan ROS Noetic. Ekstrinsik antarkamera diestimasi dengan papan catur 7 × 9 (kotak 60 mm).

### 2. Pemilihan posisi dan sudut kamera
Kanopi V dimodelkan sebagai bidang datar. Prosedur iteratif: ukur geometri kanopi dan jarak antarbaris, tentukan luas ROI yang diinginkan, bangun kalkulator ROI (pustaka SymPy), letakkan kamera acuan pada setengah jarak antarbaris dengan sumbu optik tegak lurus kanopi, lalu naikkan sudut azimut dan elevasi bertahap sambil menyesuaikan jarak antarkamera agar luas ROI tidak turun di bawah target. Untuk ROI 1 × 1 m dan kanopi bertinggi 2,75 m dengan dasar 1,4 m, selisih sudut maksimum yang ditemukan adalah 30° pada jarak horizontal 0,8 m dan vertikal 0,8 m. Tiang berada sekitar 2 m dari barisan.

### 3. Empat konfigurasi uji
Sudut yang diuji adalah 0°, 15°, dan 30°. Kamera 2 hanya divariasikan elevasinya (15° atau 30°), kamera 3 hanya azimutnya (15° atau 30°), dan kamera 4 mengombinasikan elevasi dan azimut (15° dan 30°). Uji 1: kamera 2 elevasi 30°, kamera 3 azimut 30°, kamera 4 30° dan 30°. Uji 2: 30°, 15°, dan 30° dengan 15°. Uji 3: 15°, 30°, dan 15° dengan 30°. Uji 4: 15°, 15°, dan 15° dengan 15°.

### 4. Pembentukan ROI dan anotasi
Bingkai disubsampel menjadi 0,5 fps agar tumpang tindih antarbingkai rendah. Titik dengan kedalaman lebih dari 3 m dibuang untuk menghilangkan baris lain dan latar belakang. Titik tersisa diproyeksikan ke 3D dengan matriks intrinsik, dikonversi ke sistem kamera acuan dengan ekstrinsik, lalu diproyeksikan balik ke piksel kamera acuan; lubang diisi dengan operasi penutupan morfologis (*closing*). ROI adalah irisan proyeksi semua kamera lain. Apel dianotasi sebagai titik pada citra kamera acuan di dalam ROI lewat antarmuka Qt, lalu diproyeksikan ke kamera lain; apel yang tidak terlihat pada suatu kamera ditandai tidak terlihat. Apel yang sudah terlihat di kamera acuan tidak dilabeli ulang agar tidak terhitung ganda. Antarmuka memungkinkan penyesuaian posisi manual karena apel kecil dan ketelitian kedalaman menurun dengan jarak. Proses diulang dengan tiap kamera sebagai acuan.

### 5. Metrik MC-FDR
$\text{MC-FDR}=\dfrac{|\bigcup_{j\in k} C_j|}{|\bigcup_{l=1}^{m} C_l|}$, dengan $k$ himpunan kamera yang dinilai dan $m=4$.

## Eksperimen dan Hasil
Setiap uji memakai 100 citra per kamera (400 citra per uji) sepanjang satu baris kebun 402,92 m. Jarak tempuh uji 1 sampai 4 berturut-turut 70,53 m, 98,56 m, 114,05 m, dan 119,78 m. Jumlah apel teranotasi dalam ROI pada uji 1 sampai 4 adalah 1.075, 1.438, 1.298, dan 1.380 (total 5.191). Acuan adalah gabungan anotasi manual empat kamera, bukan hitungan panen.

MC-FDR satu kamera (Tabel 1, persen):

| Kamera | Uji 1 | Uji 2 | Uji 3 | Uji 4 |
|---|---|---|---|---|
| 1 (tegak lurus) | 86,3 | 87,3 | 88,2 | 88,3 |
| 2 | 82,4 | 79,4 | 85,8 | 84,3 |
| 3 | 80,8 | 84,2 | 85,0 | 83,4 |
| 4 | 76,7 | 70,4 | 79,4 | 76,9 |

Dua kamera (Tabel 2, persen):

| Pasangan | Uji 1 | Uji 2 | Uji 3 | Uji 4 |
|---|---|---|---|---|
| 1 dan 2 | 93,2 | 92,6 | 95,1 | 94,9 |
| 1 dan 3 | 95,3 | 97,0 | 97,2 | 97,5 |
| 1 dan 4 | 94,7 | 93,7 | 95,2 | 95,3 |
| 2 dan 3 | 95,3 | 95,1 | 97,0 | 96,5 |
| 2 dan 4 | 90,3 | 87,1 | 92,8 | 91,5 |
| 3 dan 4 | 89,1 | 88,9 | 91,9 | 90,8 |

Tiga kamera (Tabel 3, persen):

| Kombinasi | Uji 1 | Uji 2 | Uji 3 | Uji 4 |
|---|---|---|---|---|
| 1, 2, 3 | 98,8 | 99,1 | 99,5 | 99,7 |
| 1, 2, 4 | 97,5 | 96,1 | 97,5 | 97,3 |
| 1, 3, 4 | 97,8 | 98,5 | 98,7 | 98,9 |
| 2, 3, 4 | 96,7 | 96,0 | 98,1 | 97,9 |

Kamera 1 terbaik sebagai kamera tunggal pada keempat uji, sedangkan kamera 4 (terjauh dari kamera 1) terburuk, dengan nilai terendah 70,4% pada uji 2. Penulis menghubungkan keunggulan kamera 1 dengan kanopi V yang datar dan sejajar bidang kamera. Pasangan kamera 1 dan 3 terbaik pada semua uji; tanpa kamera 1, pasangan 2 dan 3 terbaik. Kamera kedua menaikkan MC-FDR sekitar 9% dibanding kamera tegak lurus saja menurut penulis. Penambahan kamera keempat pada kombinasi 1, 2, 3 hanya menambah 0,3% sampai 1,2%, yaitu sekitar 13 apel dari 1.075 pada uji 1 dan 4 apel dari 1.380 pada uji 4 menurut penulis.

## Kelebihan dan Keterbatasan
Kelebihan: pengukuran visibilitas independen dari detektor karena anotasinya manual; pengambilan data dilakukan di kebun nyata tanpa penyederhanaan kanopi; metodologi pemilihan sudut berbasis geometri ROI bersifat umum untuk kanopi planar; dan hasil dilaporkan untuk satu, dua, dan tiga kamera pada empat konfigurasi sudut.

Keterbatasan yang dinyatakan penulis: data hanya satu varietas apel di satu kebun dengan rezim pemangkasan dan penjarangan tertentu; data dikumpulkan pada satu hari dan jendela waktu 11.00 sampai 14.00 sepanjang baris 403 m; sudut dipilih dari rentang diskret saja. Penulis menyarankan replikasi pada kebun, varietas, hari, dan waktu lain.

Menurut pembacaan ringkasan ini: (a) MC-FDR diukur terhadap gabungan empat kamera, sehingga buah yang tidak terlihat oleh keempat kamera tidak masuk penyebut, dan ukuran ini tidak menyatakan fraksi terhadap seluruh buah pada kanopi; (b) kamera lain tidak diuji pada sisi seberang kanopi atau dari sisi baris lain, sehingga hasil tidak berlaku bagi pandangan dari dua sisi pohon; (c) tidak ada ulangan statistik atau selang kepercayaan antaruji, dan konfigurasi sudut berubah antar uji pada jarak tempuh yang berbeda sehingga perbandingan antaruji tidak murni; (d) anotasi titik pada kamera lain bergantung pada proyeksi berbasis kedalaman yang kurang akurat untuk apel kecil dan jauh, sehingga dikoreksi manual.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menghitung buah dan tidak melacak identitas antarbingkai. Namun, ia menangani masalah inti identitas lintas pandang: buah yang sama dilihat oleh beberapa kamera dengan sudut berbeda. Mekanismenya adalah proyeksi geometris titik pusat buah dari kamera acuan ke kamera lain melalui kedalaman dan kalibrasi ekstrinsik, sehingga buah yang sama dikenali tanpa pencocokan tampilan; buah yang sudah terlihat di kamera acuan tidak dilabeli ulang agar tidak terhitung ganda. Hitungan tidak dilaporkan per kelas, dan acuan hitungnya adalah gabungan anotasi manual citra, bukan panen maupun hitungan lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: prinsip penetapan identitas melalui proyeksi geometris dengan kedalaman dan kalibrasi kamera, penggunaan irisan medan pandang sebagai wilayah evaluasi, dan temuan kuantitatif bahwa sudut tambahan menaikkan visibilitas dengan hasil yang menurun pada kamera ketiga dan keempat. Ketergantungan pada kanopi planar dan jarak 3 m membatasi pemindahan langsung ke pohon sawit yang berbentuk tiga dimensi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `villacres2024assessing`.

Villacrés dan Vougioukas (2024) menilai visibilitas apel pada kanopi berbentuk V dengan empat kamera RGB-D pada orientasi berbeda dan memperkenalkan *Multi-Camera Fruit Detection Ratio* (MC-FDR) terhadap gabungan buah terlihat pada empat kamera. Satu kamera tegak lurus mencakup 86,3% sampai 88,3%, dua kamera hingga 97,5%, dan tiga kamera 96,0% sampai 99,7% dari buah yang terlihat oleh empat kamera, berdasarkan anotasi manual 5.191 apel dalam ROI pada empat uji di satu kebun.

Catatan verifikasi data: Angka MC-FDR bersumber dari Tabel 1, 2, dan 3; jumlah apel per uji (1.075, 1.438, 1.298, 1.380; total 5.191) dan jarak tempuh dari bagian 4.2; geometri kanopi dan sudut maksimum dari bagian 4.1. Rentang tiga kamera 96,0% sampai 99,7% pada abstrak mencakup semua kombinasi tiga kamera pada Tabel 3, sedangkan rentang 98,8% sampai 99,7% pada bagian diskusi hanya untuk kamera 1, 2, 3 (nilai uji 2 dan 3 pada Tabel 3 adalah 99,1% dan 99,5%). Klaim "sekitar 9%" penambahan kamera kedua berasal dari teks penulis, bukan dari perhitungan ringkasan ini. Kode, citra, dan data anotasi tidak tersedia kecuali atas permintaan (pernyataan ketersediaan data). Tidak ada hasil deteksi otomatis, hitungan per kelas, atau hasil panen yang dilaporkan.
