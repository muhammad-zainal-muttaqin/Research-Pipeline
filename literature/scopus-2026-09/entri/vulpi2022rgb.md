# An RGB-D multi-view perspective for autonomous agricultural robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vulpi2022rgb` |
| Judul asli | An RGB-D multi-view perspective for autonomous agricultural robots |
| Penulis | Vulpi, Fabio; Marani, Roberto; Petitti, Antonio; Reina, Giulio; Milella, Annalisa |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [vulpi2022rgb.pdf](../pdf/vulpi2022rgb.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107419

## Gambaran Umum
Makalah ini menyajikan perangkat penginderaan RGB-D multipandang (*multi-view*) berbiaya rendah untuk robot pertanian darat, beserta alur pembuatan peta 3D bergeoreferensi dari lintasan robot. Perangkat terdiri atas tiga kamera RGB-D Intel RealSense D435 yang menutup bidang pandang horizontal sekitar 130° di depan kendaraan, serta sensor lokalisasi: kamera pelacak T265, RTK-GPS, dan IMU. Istilah "multipandang" di sini berarti beberapa kamera yang dipasang pada satu kendaraan, bukan pengamatan buah yang sama dari beberapa sisi pohon.

Pengujian lapangan dilakukan pada kebun anggur komersial di San Donaci, Apulia, Italia, dengan empat lintasan tertutup sepanjang baris sekitar 120 m pada September dan Oktober 2021. Hasil yang dilaporkan adalah akurasi lokalisasi dan peta awan titik yang diperkaya indeks vegetasi dan elevasi. Makalah ini tidak mendeteksi atau menghitung buah.

Hasil utama: penggabungan RTK-GPS, IMU, dan T265 dengan *Extended Information Filter* (EIF) menurunkan simpangan baku ketinggian ($\sigma_U$) dibandingkan RTK-GPS saja pada keempat uji, dan peta awan titik hasil EIF lebih rapi dibandingkan perakitan dengan GPS dan IMU saat koreksi RTK hilang.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan tanaman memerlukan data beresolusi spasial dan temporal tinggi. Satelit dan pesawat tidak memiliki resolusi yang memadai, dan pada tanaman rapat UAV masih sulit mengukur sifat pada tingkat daun atau buah. Penginderaan dari darat dengan robot dapat memberi data pada skala sentimeter, tetapi banyak metode terbatas pada lingkungan terstruktur seperti rumah kaca atau memerlukan sensor beresolusi tinggi yang mahal.

Kamera RGB-D konsumen umumnya memiliki bidang pandang sempit sehingga kurang cocok untuk survei berkelanjutan pada area luas. Perakitan awan titik dari beberapa kamera memerlukan estimasi pose kendaraan yang akurat, sedangkan RTK-GPS dapat kehilangan koreksi dan kamera pelacak visual-inersial mengalami penyimpangan jangka panjang.

## Ide Utama
Tiga kamera RGB-D menutup bidang pandang lebar, dan estimasi pose kendaraan dari gabungan sensor yang saling melengkapi (RTK-GPS, IMU, T265) melalui EIF dipakai untuk menempatkan awan titik tiap kamera ke satu kerangka dunia. Hasilnya adalah peta 3D bergeoreferensi dari tanaman yang dilalui. Peta itu juga dapat diubah menjadi jaring (*mesh*) dan diimpor ke simulator Gazebo untuk menguji algoritma navigasi otonom.

## Cara Kerja Langkah demi Langkah

### 1. Perangkat keras dan akuisisi
Larik sensor persepsi terdiri atas tiga D435, dengan bidang pandang sekitar 130° yang meluas sekitar 145° bila hanya memakai informasi kedalaman inframerah. Larik navigasi terdiri atas satu kamera pelacak T265, satu IMU X-Sense MTi-300, dan dua GPS u-blox ZED-F9P dalam konfigurasi *rover-base* untuk RTK-GPS. Semuanya ditempatkan di kotak PLA cetak 3D pada rangka aluminium dengan dua komputer Intel NUC bertenaga baterai litium; satu menjalankan Ubuntu untuk GPS dan IMU melalui ROS (data disimpan sebagai ROS *bag*), dan satu menjalankan Windows 11 dengan perangkat lunak SensorBox (Intel RealSense SDK 2.0 v. 2.49) untuk citra. Biaya kotak sensor sekitar 6,5 k€ (27% unit pengolah, 45% IMU, 14% kamera, 7% GPS, 7% baterai). Kode SensorBox tersedia di GitHub.

Kamera berjalan bebas (*free run*) hingga 30 bingkai per detik tanpa sinkronisasi perangkat keras; sinkronisasi dilakukan perangkat lunak dengan cap waktu. Kalibrasi spasial dilakukan "dengan konstruksi", karena sensor berada pada posisi tetap di dalam kotak.

### 2. Estimasi pose dengan EIF
Pose kotak sensor (posisi, kecepatan, kuaternion) diprediksi dari pengukuran IMU dan dikoreksi oleh RTK-GPS (posisi dan kecepatan dunia), IMU (orientasi dunia), dan T265 (posisi dan orientasi relatif). Metode ini dipilih karena keandalan filter Kalman dan karena filter partikel dinilai kurang akurat.

### 3. Perakitan awan titik
Setiap titik dari kamera ditransformasikan ke kerangka kotak sensor, lalu ke kerangka dunia East-North-Up dengan pose EIF. Awan titik tiga kamera digabung dan diturunkan resolusinya (ukuran voksel 0,01 m).

### 4. Simulasi
Peta diubah menjadi jaring: pengambilan sampel *Poisson-disk*, normal dari 10 titik terdekat, rekonstruksi permukaan *Ball Pivoting*, pemetaan tekstur, dan transfer warna; hasilnya diimpor ke Gazebo sebagai model SDF dengan contoh robot melintasi baris kebun anggur.

## Eksperimen dan Hasil
Robot jejak (*tracked*) dari Politecnico di Bari dipandu mengikuti lintasan tertutup pada dua baris yang berbeda (sekitar 120 m), empat uji (Test 1–4) dalam dua kampanye lapangan (September dan Oktober 2021) pada waktu hari berbeda. Data diproses luring. Dibandingkan tiga sumber lokalisasi: RTK-GPS saja, T265 saja, dan EIF. Metrik: jarak Euklides 3D ($D$), jarak 2D pada bidang gerak ($D_{EN}$), jarak ketinggian ($D_U$) antara titik awal dan akhir, dan simpangan baku ketinggian ($\sigma_U$) sepanjang lintasan (Tabel 1).

| Uji | Sumber | $D$ (m) | $D_{EN}$ (m) | $D_U$ (m) | $\sigma_U$ (m) |
|---|---|---|---|---|---|
| 1 | RTK-GPS | 1,501 | 1,511 | 0,026 | 0,451 |
| 1 | T265 | 1,276 | 1,275 | 0,046 | 2,425 |
| 1 | EIF | 1,514 | 1,513 | 0,032 | 0,228 |
| 2 | RTK-GPS | 0,579 | 0,579 | 0,013 | 0,452 |
| 2 | T265 | 5,909 | 4,921 | 3,270 | 2,199 |
| 2 | EIF | 0,579 | 0,579 | 0,011 | 0,209 |
| 3 | RTK-GPS | 1,852 | 1,517 | 1,063 | 0,370 |
| 3 | T265 | 7,264 | 5,811 | 4,359 | 1,440 |
| 3 | EIF | 1,833 | 1,484 | 1,077 | 0,355 |
| 4 | RTK-GPS | 1,290 | 1,073 | 0,717 | 0,670 |
| 4 | T265 | 5,341 | 4,760 | 2,424 | 1,497 |
| 4 | EIF | 0,739 | 0,356 | 0,647 | 0,428 |

Pada Test 1, $\sigma_U$ T265 sebesar 2,43 m, sekitar lima kali RTK-GPS, dan EIF 0,22 m (49% lebih kecil daripada RTK-GPS). Pada Test 2, EIF menurunkan $\sigma_U$ sebesar 53% terhadap GPS dan 90% terhadap T265. Pada Test 3, T265 menurun parah dan EIF terutama mengandalkan GPS. Pada Test 4, sinyal GPS buruk dan EIF mengompensasi dengan T265 sehingga lebih baik pada seluruh metrik. Penulis menyimpulkan odometri visual-inersial hanya sesuai untuk estimasi perpindahan jangka pendek.

Pemetaan: awan titik dari kamera depan dan dari ketiga kamera (sekitar 20 m) dirakit dengan odometri 6DoF EIF dan diperkaya *Green–Red Vegetation Index* (GRVI) serta elevasi. Perakitan dengan data GPS dan IMU saat koreksi RTK hilang menghasilkan awan titik yang berantakan, sedangkan EIF memperbaikinya (Gambar 16, kualitatif). Tidak ada metrik kuantitatif untuk kualitas peta.

## Kelebihan dan Keterbatasan
Kelebihan: perangkat modular, mandiri, dan berbiaya sekitar 6,5 k€; kodenya terbuka; fusi sensor mengurangi variasi ketinggian dan menutupi kehilangan RTK.

Keterbatasan yang dinyatakan penulis: pemrosesan dilakukan luring; kalibrasi spasial hanya "dengan konstruksi" (strategi optimasi dapat meningkatkan akurasi registrasi); kamera tidak tersinkronisasi secara perangkat keras; pekerjaan lanjutan mencakup klasifikasi semantik peta, integrasi dengan sistem manajemen pertanian, dan penyelesaian tantangan waktu nyata.

Menurut pembacaan ringkasan ini, evaluasi hanya memakai empat lintasan pada dua baris di satu kebun anggur, dengan ukuran yang bergantung pada jarak antara titik awal dan akhir lintasan tertutup (bukan galat terhadap peta acuan), dan kualitas peta dinilai secara visual saja. Pada Test 1 EIF tidak lebih baik daripada RTK-GPS pada $D$, $D_{EN}$, dan $D_U$. Data tersedia "atas permintaan".

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali dan tidak melakukan deteksi atau penghitungan buah. Mekanisme multipandangnya adalah perakitan awan titik dari tiga kamera yang dipasang tetap pada satu kendaraan dengan pose dari fusi sensor; ia tidak memuat identitas objek, pencocokan buah, maupun hitungan per kelas atau acuan hitung (panen atau anotasi), sehingga tidak ada yang dapat dikutip tentang hal tersebut.

Yang dapat dipindahkan secara terbatas ke pencacahan tandan sawit multi-sisi: gagasan menempatkan pengamatan dari beberapa sudut ke satu kerangka dunia melalui pose kendaraan yang akurat, yaitu prasyarat bila identitas objek ditentukan secara geometris, serta informasi bahwa kamera RGB-D D435 dapat dipakai di luar ruangan karena berbasis stereo inframerah. Penerapan itu masih berupa dasar perangkat keras dan lokalisasi, bukan metode pencacahan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `vulpi2022rgb`.

Vulpi dkk. (2022) menyajikan perangkat RGB-D multipandang berbiaya sekitar 6,5 k€ dengan tiga kamera Intel RealSense D435 (bidang pandang horizontal sekitar 130°) dan fusi RTK-GPS, IMU, serta kamera T265 melalui *Extended Information Filter* untuk membangun peta 3D bergeoreferensi dari kebun anggur. Pada empat lintasan tertutup sekitar 120 m, fusi EIF menurunkan simpangan baku ketinggian terhadap RTK-GPS saja (misalnya 0,228 m dibanding 0,451 m pada uji 1). Makalah tidak membahas deteksi atau penghitungan buah.

Catatan verifikasi data: Angka lokalisasi ada pada Tabel 1; persentase pengurangan $\sigma_U$ (49%, 53%, 90%) tertulis pada seksi 6.1. Kolom Tabel 1 pada ekstraksi terpisah satu nilai per baris tetapi urutan baris sumber-uji dapat dipulihkan dari pola yang konsisten (label uji tercetak pada baris kedua tiap kelompok). Biaya dan komposisinya ada pada seksi 3.1. Kualitas peta hanya dinilai secara visual (Gambar 13–16); tidak ada metrik atau jumlah buah.
