# LiDAR–Camera Fusion for 3D Fruit Counting and Density Mapping in Horizontal Trellis Orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lee2026lidarcamera` |
| Judul asli | LiDAR–Camera Fusion for 3D Fruit Counting and Density Mapping in Horizontal Trellis Orchards |
| Penulis | Lee, Jaehwan; Ohata, Meguna; Itoh, Hiromichi; Morimoto, Eiji |
| Tahun | 2026 |
| Venue | Journal of Robotics and Mechatronics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pear |

## Tautan Akses
- PDF: [lee2026lidarcamera.pdf](../pdf/lee2026lidarcamera.pdf)
- DOI resmi: https://doi.org/10.20965/jrm.2026.p0449

## Gambaran Umum

Makalah ini menyajikan sistem pemantauan buah waktu-nyata yang menggabungkan LiDAR dan kamera RGB untuk penghitungan buah tiga dimensi dan pemetaan kepadatan spasial pada kebun pir Jepang dengan sistem para-para horizontal (*horizontal trellis*). Sistem memakai fusi tingkat instans: deteksi 2D berbasis YOLO digabungkan dengan titik awan 3D hasil SLAM (FAST-LIO2) untuk melokalisasi buah secara individual. Identitas buah dikelola dalam basis data global berbasis koordinat 3D, dengan filter rerata bergerak kumulatif (*cumulative moving average*, CMA) untuk menstabilkan posisi pusat buah.

Data diambil pada 25 Agustus 2025, sekitar satu minggu sebelum panen, di kebun pir milik Food Resources Education and Research Center, Kobe University, pada satu petak 6 m × 70 m, dan seluruh akuisisi dilakukan malam hari dengan panel LED. Platform adalah kendaraan darat tak berawak (UGV) Hunter SE dengan LiDAR Livox Mid-360 dan kamera ZED2i. Kultivar yang disebut untuk penentuan ambang adalah pir "Kousui".

Hasil utama: pada 1.891 buah acuan, sistem memperkirakan 1.963 buah, dengan galat hitungan 3,8% dan akurasi 96,2%. Galat absolut rerata (MAE) kepadatan pada sel 2 m × 2 m adalah 0,64 buah/m². Detektor YOLOv11s dipilih dengan F1 0,983 pada set uji.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa budidaya pir Jepang padat karya dan bahwa sistem para-para horizontal menuntut pengelolaan buah dan pemangkasan di area luas, sehingga pemantauan hasil manual lambat dan rawan galat. Citra 2D tidak membawa kedalaman, sehingga buah kecil yang dekat dan buah besar yang jauh dapat menghasilkan kotak pembatas berukuran sama. Titik awan LiDAR membawa geometri yang tepat tetapi tidak membawa semantik untuk membedakan buah dari daun dan cabang.

Penelitian fusi sebelumnya, menurut penulis, berfokus pada kanopi vertikal seperti sistem V-trellis. Pada kebun para-para horizontal, jarak antarpohon yang lebar menuntut UGV melintas berkali-kali dan berbelok. Pelacakan 2D antarbingkai kesulitan mempertahankan identitas buah terutama saat berbelok atau kembali, sehingga menimbulkan hitungan ganda.

## Ide Utama

Dua gagasan diajukan. Pertama, filter pelacakan CMA yang menstabilkan posisi pusat buah terhadap oklusi sebagian oleh daun pada tampilan kamera menghadap ke atas. Kedua, manajemen instans 3D global: identitas buah ditautkan ke koordinat absolut dalam peta SLAM, bukan ke posisi relatif dalam citra, sehingga hitungan konsisten walaupun UGV melintas berkali-kali dengan arah berbeda.

## Cara Kerja Langkah demi Langkah

```
 LiDAR + IMU --> FAST-LIO2 --> peta 3D global + pose 6-DOF ----+
                                                                |
 Kamera RGB --> YOLO 2D --> kotak (cap waktu) ---> fusi tingkat instans
                                                                |
        proyeksi frustum, filter pusat 10% --> posisi 3D buah
                                                                |
        asosiasi tetangga terdekat (k-d tree, d_th = 0,075 m)
                                                                |
        FI-DB: perbarui CMA atau daftarkan baru; pangkas N < 3
```

### 1. Platform dan akuisisi

UGV Hunter SE membawa LiDAR Mid-360 (dimiringkan 26,5°) dan kamera ZED2i yang menghadap vertikal ke atas, dengan komputer NUC11PAHi7 (ROS 2 Humble, Ubuntu 22.04). Kamera menghadap atas menyebabkan saturasi akibat cahaya matahari, sehingga data diambil pada malam hari dengan panel LED (725 lx pada jarak 1,6 m). Protokol "berhenti dan jalan" (*stop-and-go*): UGV maju per 0,5 m lalu diam 5 detik agar LiDAR mengakumulasi titik awan yang lebih padat dan detektor memproses beberapa bingkai. Jalur dua arah dengan jarak lateral antarlintasan 1,5 m (tumpang tindih 50% dari medan pandang horizontal 3 m). Citra kamera berukuran 2208 × 1242 piksel pada rerata 8,3 fps. Rekaman sekitar 100 menit memuat 60.166 pindaian LiDAR (10 Hz), 1.203.302 pengukuran IMU (200 Hz), dan 49.698 citra RGB.

### 2. Kalibrasi LiDAR–kamera

Transformasi ekstrinsik $T_{CL}$ diperoleh dengan mode korespondensi manual pada perangkat kalibrasi karena kalibrasi otomatis menurun pada kebun tak terstruktur. Solusi meminimalkan galat reproyeksi total (Persamaan 1) dengan kuadrat terkecil nonlinear.

### 3. Deteksi 2D

Empat model YOLO dilatih dalam kerangka Ultralytics dengan bobot awal COCO: YOLOv11n, YOLOv11s, YOLOv12n, dan YOLOv12s (ukuran masukan 640 × 640, 450 epoch, ukuran batch 40, laju belajar awal 0,01, augmentasi Mosaic, MixUp, Copy-Paste). Anotasi memakai LabelImg dengan satu kelas "pear". Seleksi model memakai F1 sebagai penyaring awal dan jumlah negatif palsu (*false negatives*, FN) terendah sebagai kriteria penentu.

### 4. Lokalisasi 3D

Titik awan global diproyeksikan ke citra memakai pose dan kalibrasi tersinkron; kotak 2D dipakai sebagai wilayah minat (metode frustum). Untuk menyingkirkan latar daun dan cabang, hanya titik yang terproyeksi ke 10% bagian tengah kotak yang dipertahankan, karena pada kamera menghadap atas daun latar yang lebih tinggi menyebabkan estimasi jarak berlebih. Posisi 3D buah adalah sentroid klaster titik hasil penyaringan.

### 5. Asosiasi data dan basis data instans

Setiap observasi baru dicocokkan dengan instans terdekat dalam basis data instans buah (FI-DB) lewat pencarian tetangga terdekat dengan k-d tree. Kecocokan diterima bila jarak Euclidean kurang dari $d_{th} = 0{,}075$ m (Persamaan 5), dipilih karena diameter transversal pir "Kousui" saat panen 83,2 sampai 95,1 mm. Bila cocok, posisi diperbarui dengan CMA: $p'_{db,k} = \frac{1}{N_k}\{(N_k - 1)\, p_{db,k} + p_{W,new}\}$ (Persamaan 6). Bila tidak cocok, instans baru dengan ID unik didaftarkan. Instans dengan jumlah observasi $N_k$ di bawah $N_{min} = 3$ dipangkas sebagai deteksi palsu.

## Eksperimen dan Hasil

### Data detektor (Tabel 2)

| Subset | Citra | Label "pear" |
|---|---|---|
| Latih | 9.000 | 451.051 |
| Validasi | 2.580 | 88.247 |
| Uji | 100 | 4.077 |
| Total | 11.680 | 543.375 |

Pada set validasi, mAP@0,5 keempat model berkisar 0,989 sampai 0,990, dengan F1 0,970 untuk varian "Small".

### Kinerja detektor pada set uji (Tabel 3, ambang keyakinan 0,7)

| Model | Presisi | Recall | F1 | Waktu inferensi (ms) |
|---|---|---|---|---|
| YOLOv11n | 0,983 | 0,969 | 0,976 | 5,58 |
| YOLOv11s | 0,981 | 0,986 | 0,983 | 8,02 |
| YOLOv12n | 0,984 | 0,961 | 0,972 | 7,42 |
| YOLOv12s | 0,979 | 0,979 | 0,979 | 11,13 |

YOLOv11s dipilih karena F1 tertinggi dan FN terendah (55); YOLOv12n memiliki 159 FN. Kesalahan positif palsu terutama dari daun menguning dan pita pertanian merah; FN terutama pada oklusi berat atau bayangan gelap.

### Penghitungan sistem penuh dan kepadatan

| Ukuran | Nilai |
|---|---|
| Hitungan sistem | 1.963 buah |
| Acuan manual | 1.891 buah |
| Kelebihan hitungan bersih | 72 buah (galat relatif 3,8%) |
| Akurasi hitungan | 96,2% |
| Buah acuan terlewat | 14 dari 1.891 (0,7%) |
| Positif palsu | 86 |
| MAE kepadatan (sel 2 m × 2 m, 138 sel berisi buah) | 0,64 buah/m² |

Dari 86 positif palsu, 33 berasal dari YOLO yang salah mengenali daun kuning dan pita merah sebagai buah, dan 53 adalah hitungan ganda pada tahap lokalisasi walaupun CMA dipakai. Dari 53 hitungan ganda itu, 30 terjadi dalam ambang asosiasi (menurut penulis menunjukkan keterbatasan filter temporal atau presisi pencarian k-d tree) dan 23 akibat pergeseran SLAM yang melebihi ambang, terutama saat UGV berbelok; contoh pada Gambar 10 menunjukkan pergeseran 0,085 m. Contoh kepadatan: daerah jarang 2,5 buah/m² dan daerah padat 10,25 buah/m².

Acuan dibuat dengan anotasi manual pada peta titik awan berwarna hasil SLAM dengan video tersinkron sebagai validasi; satu penanda 3D ditempatkan di pusat tiap buah sehingga tidak ada penghitungan ganda dalam acuan.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: identitas buah berbasis koordinat absolut mencegah hitungan ganda pada lintasan berulang; peta kepadatan membantu diagnosis wilayah berproduktivitas rendah serta keputusan pemangkasan musim dingin; dan sistem berjalan modular dengan inferensi detektor 8,02 ms.

Keterbatasan yang dinyatakan penulis: positif palsu dari detektor (daun kuning, pita merah) dan hitungan ganda akibat pergeseran SLAM tetap menjadi sumber galat utama. Mitigasi yang diusulkan: menaikkan ambang keyakinan atau menambah sampel negatif, penutupan loop (*loop closure*) pada SLAM, dan pengelompokan berbasis kedekatan pada pascapemrosesan.

Menurut pembacaan ringkasan ini: (a) evaluasi hanya pada satu petak 6 m × 70 m dan satu hari akuisisi; (b) penghitungan dilakukan pada malam hari dengan pencahayaan LED terkendali, dan teks tidak menguji kondisi siang; (c) set uji detektor hanya 100 citra, dan set uji mungkin berasal dari lokasi yang sama dengan latih (pemisahan tidak dijelaskan); (d) ambang $d_{th}$ sengaja kecil dibanding diameter buah, sehingga sangat bergantung pada akurasi SLAM; (e) tidak ada hitungan per kelas, karena hanya ada satu kelas "pear"; (f) protokol berhenti-dan-jalan dengan pemanduan manual tidak setara dengan operasi otonom kontinu.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang tampak berkali-kali dari banyak posisi kendaraan, termasuk lintasan berulang dan berbelok. Mekanismenya adalah rekonstruksi 3D dan asosiasi di ruang dunia: deteksi 2D diproyeksikan ke titik awan SLAM, lalu identitas ditentukan oleh jarak Euclidean 3D ke instans yang sudah ada (ambang 0,075 m), dengan pembaruan CMA dan pemangkasan instans yang teramati kurang dari tiga kali. Dengan demikian identitas ditautkan ke koordinat absolut, bukan ke urutan bingkai. Hitungan tidak dilaporkan per kelas. Acuan hitungnya adalah anotasi manual pada peta titik awan, bukan panen.

Untuk pencacahan tandan kelapa sawit multi-sisi, gagasan yang dapat dipindahkan adalah penautan identitas ke koordinat dunia dengan ambang jarak yang lebih kecil daripada ukuran minimum objek, dan penyaringan instans yang hanya teramati sedikit. Gagasan itu menuntut pose kamera atau sensor yang akurat; pada kasus seperti SawitMVC yang berupa citra dari 4 sampai 8 sisi pohon, ketersediaan pose dan kedalaman perlu dipastikan. Penulis sendiri melaporkan bahwa pergeseran pose adalah sumber hitungan ganda yang tersisa.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `lee2026lidarcamera`.

Lee dkk. (2026) mengusulkan sistem penghitungan buah 3D pada kebun pir dengan para-para horizontal yang menggabungkan deteksi YOLOv11s dengan titik awan LiDAR-inersia SLAM (FAST-LIO2) pada tingkat instans. Identitas buah dikelola dalam basis data global berbasis koordinat 3D (ambang asosiasi 0,075 m, filter rerata bergerak kumulatif, pemangkasan instans dengan kurang dari tiga observasi). Pada petak 6 m × 70 m dengan 1.891 buah acuan, sistem menghitung 1.963 buah (akurasi 96,2%) dengan MAE kepadatan 0,64 buah/m².

Catatan verifikasi data: angka detektor ada pada Tabel 2 dan 3, hasil penghitungan pada Bagian 6.2.1, MAE pada Bagian 6.2.2, parameter pada Bagian 4 dan 5. Jumlah positif palsu 86 (33 deteksi ditambah 53 hitungan ganda) dan kelebihan 72 buah dinyatakan di teks. Teks ekstraksi terbaca baik, tetapi gambar tidak tersedia sehingga Gambar 11 (plot korelasi kepadatan) tidak diperiksa. Tidak dilaporkan: pemisahan lokasi antara data latih dan uji detektor, galat pose SLAM secara kuantitatif di luar contoh 0,085 m, dan perbandingan dengan metode pelacakan 2D lain.
