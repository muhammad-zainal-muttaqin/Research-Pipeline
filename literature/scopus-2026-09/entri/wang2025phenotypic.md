# Phenotypic Trait Acquisition Method for Tomato Plants Based on RGB-D SLAM

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2025phenotypic` |
| Judul asli | Phenotypic Trait Acquisition Method for Tomato Plants Based on RGB-D SLAM |
| Penulis | Wang, Penggang; He, Yuejun; Zhang, Jiguang; Liu, Jiandong; Chen, Ran; Zhuang, Xiang |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [wang2025phenotypic.pdf](../pdf/wang2025phenotypic.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15151574

## Gambaran Umum

Makalah ini mengusulkan sistem rekonstruksi semantik 3D berbasis ORB-SLAM3 yang ditingkatkan, dipasang pada kendaraan darat tanpa awak (*unmanned ground vehicle*, UGV), untuk memperoleh sifat fenotipik tanaman tomat di lingkungan budi daya terlindung. Sistem memakai kamera RGB-D Intel RealSense D435i, modul segmentasi semantik BiSeNetV2 yang hanya dijalankan pada bingkai kunci (*keyframe*), penyaringan dua tahap (*pass-through* lalu statistik) untuk membuang pencilan, dan OctoMap untuk penyimpanan peta. Kendaraan dilengkapi algoritme A* untuk navigasi otonom.

Data uji dikumpulkan pada 18 April 2025 di basis budi daya tomat di Kabupaten Gu'an, Kota Langfang, Tiongkok. Kumpulan data segmentasi buatan sendiri terdiri dari 600 citra beranotasi (300 pandangan lebar dari D435i dan 300 jarak dekat dari kamera Nikon Z30) dengan anotasi hanya pada buah tomat. Jumlah tanaman yang dipakai untuk evaluasi fenotipe adalah 10 tanaman, sedangkan hitungan buah dievaluasi pada tiga tanaman tunggal dan tiga barisan tanaman.

Hasil utama yang dilaporkan: BiSeNetV2 mencapai mIoU 95,37% dan 61,98 FPS; OctoMap mengurangi konsumsi memori rata-rata 96,70%; galat relatif tinggi tanaman, lebar tajuk, dan volume berturut-turut 3,86%, 14,34%, dan 27,14%; galat hitungan buah 14,36% dan galat volume buah 14,25%; serta galat lintasan absolut rata-rata (mATE) 0,16 m dan RMSE 0,21 m pada data lapangan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pengukuran sifat fenotipik secara manual (misalnya tinggi tanaman, lebar tajuk, jumlah buah) memerlukan banyak tenaga dan tidak efisien. Metode rekonstruksi 3D konvensional, yaitu *multi-view stereo* (MVS), *structure from motion* (SfM), dan *time-of-flight* (ToF, termasuk LiDAR dan kamera kedalaman), menurut penulis sensitif terhadap pencahayaan atau bergantung pada perangkat pindai yang mahal, sehingga sulit dipakai di luar ruangan. SLAM visual (*visual simultaneous localization and mapping*, vSLAM) dinilai murah dan andal di luar ruangan.

Penulis menyebut tiga celah pada penelitian terdahulu. Pertama, peta SLAM biasanya hanya memuat fitur geometris dan kurang ekspresif untuk wilayah yang diminati. Kedua, banyak studi semantik masih mengambil data secara manual, yang sulit pada perkebunan skala besar. Ketiga, sistem berbasis wahana tanpa awak sering memakai sensor mahal seperti LiDAR dan bekerja luring. Sistem yang diusulkan ditujukan menutup celah tersebut dengan peta semantik berkinerja waktu-nyata pada perangkat tertanam.

## Ide Utama

Gagasan utamanya adalah pendekatan "segmentasi dahulu, rekonstruksi kemudian" (*segment-then-reconstruct*): citra bingkai kunci disegmentasi pada tingkat piksel oleh jaringan ringan, lalu label semantik diproyeksikan ke ruang 3D dengan peta kedalaman, pose kamera, dan parameter intrinsik. Dengan begitu awan titik yang dihasilkan sudah berlabel buah, dan hitungan buah diperoleh dengan mencocokkan bola (*spherical fitting*) pada titik berlabel buah. Komputasi dijaga ringan dengan segmentasi hanya pada bingkai kunci dan penyimpanan peta dalam OctoMap.

Identitas buah antarpandangan tidak ditangani oleh pelacak khusus. Konsistensi diperoleh dari peta global tunggal yang dibangun SLAM: titik dari banyak bingkai kunci terakumulasi di koordinat dunia yang sama, sehingga satu buah fisik menjadi satu gugus titik 3D, lalu gugus itu dicocokkan dengan bola.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data dan platform

Citra tomat diambil dengan Intel RealSense D435i (pandangan lebar) dan Nikon Z30 dengan lensa 50 sampai 250 mm f/4,5 sampai 6,3 (jarak dekat), mencakup tomat dengan tingkat kematangan dan pencahayaan yang bervariasi. Semua citra diseragamkan menjadi 640 × 480 piksel dan dianotasi dengan Labelme (versi 5.4.1), menghasilkan 600 citra. Pembagian data latih, validasi, dan uji adalah 7:2:1. Tanaman ditanam dengan metode gantung tali (*string-hanging*) dengan kepadatan tinggi. Platform UGV terdiri dari modul sensor (D435i, LiDAR 2D, RTK), modul sasis (muatan maksimum 50 kg, kecepatan maksimum 0,8 m/s), dan modul kendali berbasis PC dengan Ubuntu 20.04 dan ROS. LiDAR dipakai untuk penghindaran rintangan, dan RTK memberikan lintasan acuan. Jenis atau kultivar tomat tidak dilaporkan.

### 2. ORB-SLAM3 yang ditingkatkan

Pelacakan dan estimasi pose dilakukan pada setiap bingkai. Sebuah bingkai menjadi bingkai kunci bila translasi atau rotasi terhadap bingkai kunci sebelumnya melampaui ambang, atau bila jumlah titik peta yang terlacak turun tajam. Segmentasi semantik dijalankan hanya pada bingkai kunci. Modul optimisasi lokal dan penutupan loop (*loop closure*) ORB-SLAM3 dipertahankan untuk menjaga konsistensi global.

### 3. Segmentasi semantik BiSeNetV2

BiSeNetV2 memiliki cabang detail (lebar dan dangkal) dan cabang semantik (dalam dan sempit), lapisan agregasi terpandu (*guided aggregation layer*), dan kepala bantu FCNHead yang hanya dipakai saat pelatihan. Pelatihan memakai iterasi tetap maksimum 20.000 dan laju belajar $1 \times 10^{-3}$ pada Intel Core i9-14900KF dan NVIDIA RTX 4080S dengan PyTorch 1.11. Pembanding: ICNet, PSPNet, SegFormer, DeepLabv3+, dan BiSeNetV1.

### 4. Penyaringan dua tahap

Tahap pertama adalah *pass-through filtering* pada rentang koordinat $(X, Y, Z)$ untuk membuang titik non-tanaman. Tahap kedua adalah penyaringan statistik berdasarkan jarak rerata ke $k$ tetangga terdekat, dengan titik dipertahankan bila jarak itu berada dalam $[\mu - k\delta, \mu + k\delta]$.

### 5. OctoMap

Awan titik padat dikonversi menjadi pohon oktan (*octree*) dengan status hunian dalam bentuk log-odds. Resolusi dasar yang disebutkan untuk visualisasi barisan tanaman adalah 0,05 m.

### 6. Ekstraksi fenotipe

Tinggi $H_p = H_{max} - H_{min}$, lebar tajuk $W_p = ((W_{max} - W_{min}) + (L_{max} - L_{min}))/2$, dan volume $V_p = H_p \times W_p \times W_p$. Tinggi tanaman didefinisikan dari pangkal hingga gugus buah kelima. Untuk buah, titik berwarna dipilih dengan filter bersyarat ambang warna, lalu RANSAC Shape Detection di CloudCompare dipakai untuk pencocokan bola dengan radius minimum 0,023 dan maksimum 0,030 (satuan tidak dinyatakan pada teks). Jumlah bola sama dengan hitungan buah, dan volume buah $V_p = \frac{4}{3}\pi r^3$. Acuan volume buah adalah elipsoid dari panjang, lebar, dan tinggi buah yang diukur dengan jangka sorong.

## Eksperimen dan Hasil

Hasil perbandingan segmentasi (Tabel 1, data tomat sendiri):

| Model | Encoder | mIoU (%) | mAcc (%) | FPS |
|---|---|---|---|---|
| ICNet | PSPNet50 | 93,51 | 96,19 | 60,12 |
| PSPNet | ResNet50 | 95,26 | 97,39 | 53,48 |
| SegFormer | Mix Transformer B0 | 94,44 | 96,84 | 57,97 |
| DeepLabv3+ | ResNet50 | 92,21 | 96,41 | 51,63 |
| BiSeNetV1 | ResNet18 | 93,77 | 96,58 | 61,59 |
| BiSeNetV2 | tidak ada | 95,37 | 97,38 | 61,98 |

Penyimpanan (Tabel 2): penyaringan mengurangi memori rata-rata 9,92%, dan OctoMap rata-rata 96,70%. Contoh: peta semantik tanaman pertama 7,73 MB, setelah penyaringan 6,96 MB, dan OctoMap 0,32 MB; barisan pertama 73,63 MB menjadi 64,35 MB lalu 1,32 MB.

Fenotipe 10 tanaman (Tabel 3), dibandingkan dengan pengukuran manual: galat relatif rata-rata tinggi 3,86%, lebar tajuk 14,34%, dan volume 27,14%. Galat volume per tanaman berkisar dari 11,96% (tanaman 6) sampai 40,06% (tanaman 3), dan penulis menyebut volume mengakumulasi galat tinggi dan lebar tajuk.

Hitungan buah (Tabel 4), acuan hitung manual:

| Sampel | Prediksi | Acuan | Galat relatif (%) |
|---|---|---|---|
| Tanaman 1 | 7 | 6 | 16,67 |
| Tanaman 2 | 9 | 12 | 25,00 |
| Tanaman 3 | 10 | 11 | 9,09 |
| Barisan 1 | 46 | 52 | 11,54 |
| Barisan 2 | 39 | 44 | 11,36 |
| Barisan 3 | 47 | 56 | 12,50 |
| Rerata | | | 14,36 |

Seluruh enam prediksi lebih kecil atau (pada tanaman 1) lebih besar dari acuan; lima dari enam sampel menunjukkan prediksi di bawah acuan. Volume buah (Tabel 5) dievaluasi pada sembilan buah dari satu tanaman dengan galat relatif rata-rata 14,25%, dengan kisaran 6,50% sampai 28,71%.

Lokalisasi (Tabel 6), pada dataset publik Rgbd_kidnap dan dataset lapangan (acuan RTK):

| Sistem | Rgbd_kidnap mATE / RMSE / Std (m) | Lapangan mATE / RMSE / Std (m) |
|---|---|---|
| ORB-SLAM2 | 0,09 / 0,10 / 0,04 | 0,45 / 0,49 / 0,19 |
| ORB-SLAM3 | 0,17 / 0,37 / 0,33 | 0,16 / 0,21 / 0,11 |

Pada Rgbd_kidnap, ORB-SLAM2 tampak lebih baik menurut metrik evo. Penulis menjelaskan bahwa perangkat evo hanya membandingkan segmen lintasan yang selaras berdasarkan stempel waktu, sehingga segmen yang hilang tidak dihitung. Selisih pada data lapangan adalah 0,29 m (mATE) dan 0,28 m (RMSE) yang dihitung dari tabel dan sesuai dengan teks makalah. Segmentasi semantik tidak mempengaruhi akurasi lokalisasi, sehingga uji lokalisasi hanya membandingkan ORB-SLAM3 dan ORB-SLAM2.

## Kelebihan dan Keterbatasan

Keterbatasan yang dinyatakan penulis: sistem bergantung pada kamera RGB-D sehingga sensitif terhadap perubahan pencahayaan (cahaya kuat atau bayangan dapat menimbulkan galat kedalaman). Tumpang-tindih daun dan oklusi buah menyebabkan segmentasi tidak lengkap dan mengurangi akurasi estimasi fenotipe. Buah yang tertutup dikeluarkan dari pencocokan bola, dan sisa titik derau dapat membuat bola yang dicocokkan saling tumpang-tindih. Penulis berencana menguji pada sayuran dan buah rumah kaca lain serta memperbaiki cara memperoleh acuan fenotipe.

Menurut pembacaan ringkasan ini, evaluasi hitungan buah sangat kecil (tiga tanaman dan tiga barisan, satu tanaman untuk volume buah, 10 tanaman untuk fenotipe) tanpa ulangan atau selang kepercayaan. Hitungan buah hanya dilaporkan sebagai total per sampel, tanpa pemeriksaan identitas per buah terhadap acuan, sehingga galat total dapat menutupi pasangan galat positif palsu dan negatif palsu. Pembagian data segmentasi memakai citra yang berasal dari sesi pengambilan yang sama (satu tanggal), sehingga kemampuan generalisasi tidak diuji. Data diakses hanya atas permintaan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari banyak pandangan secara implisit melalui peta 3D global: titik dari bingkai kunci yang berbeda terakumulasi di satu kerangka koordinat oleh SLAM (dengan penutupan loop), sehingga buah yang sama menjadi satu gugus titik, lalu dihitung sebagai satu bola hasil RANSAC. Tidak ada pelacak identitas atau pencocokan antarpandangan terpisah. Hitungan tidak dilaporkan per kelas (hanya satu kelas semantik, buah tomat, yang dianotasi, meski citra mencakup berbagai tingkat kematangan). Acuan hitungnya adalah hitung manual pada tanaman atau barisan yang direkonstruksi, bukan panen maupun anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menyatukan banyak pandangan di ruang 3D bersama sehingga hitungan terjadi pada tingkat objek 3D, bukan tingkat bingkai, serta pencocokan primitif geometris untuk menghitung objek. Keterbatasan penerapannya adalah skala (tomat berdiameter sekitar 5 sampai 7 cm dengan radius bola 0,023 sampai 0,030 yang diatur manual), kebutuhan RGB-D pada jarak dekat, dan kegagalan penghitungan buah yang tertutup, yang pada tandan sawit tertanam di pelepah akan lebih sering terjadi.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `wang2025phenotypic`.

Wang dkk. mengusulkan sistem rekonstruksi semantik 3D berbasis ORB-SLAM3 dan BiSeNetV2 yang dipasang pada kendaraan darat tanpa awak untuk mengekstraksi sifat fenotipik tomat. Penghitungan buah dilakukan dengan pencocokan bola RANSAC pada awan titik berlabel buah, dengan galat relatif rata-rata hitungan buah sebesar 14,36% terhadap hitung manual pada tiga tanaman dan tiga barisan, serta galat tinggi tanaman 3,86%, lebar tajuk 14,34%, dan volume 27,14% pada 10 tanaman.

Catatan verifikasi data: Angka segmentasi berasal dari Tabel 1, penyimpanan dari Tabel 2, fenotipe tanaman dari Tabel 3, hitungan buah dari Tabel 4, volume buah dari Tabel 5, dan lokalisasi dari Tabel 6; parameter peralatan berasal dari seksi 2.1 dan 3.1. Tabel pada teks ekstraksi terbaca sebagai daftar sel dan dipetakan berdasarkan urutan. Kalimat "enam prediksi" pada pembacaan hitungan dihitung dari Tabel 4 (lima prediksi di bawah acuan, satu di atas). Satuan radius bola (0,023 dan 0,030) tidak dinyatakan di teks. Makalah berbahasa Inggris. Jumlah buah per tanaman sangat kecil dan jenis atau kultivar tomat tidak dilaporkan. Teks daftar pustaka terpotong dan tidak dipakai.
