# Three-dimensional photogrammetric mapping of cotton bolls in situ based on point cloud segmentation and clustering

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2020three` |
| Judul asli | Three-dimensional photogrammetric mapping of cotton bolls in situ based on point cloud segmentation and clustering |
| Penulis | Sun, Shangpeng; Li, Changying; Chee, Peng W.; Paterson, Andrew H.; Jiang, Yu; Xu, Rui; Robertson, Jon S.; Adhikari, Jeevan; Shehzad, Tariq |
| Tahun | 2020 |
| Venue | ISPRS Journal of Photogrammetry and Remote Sensing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [sun2020three.pdf](../pdf/sun2020three.pdf)
- DOI resmi: https://doi.org/10.1016/j.isprsjprs.2019.12.011

## Gambaran Umum
Makalah ini (Sun dkk., *ISPRS Journal of Photogrammetry and Remote Sensing* 160, 2020, hlm. 195-207) mengusulkan metode pemetaan tiga dimensi (3D) buah kapas (*cotton boll*, selanjutnya "boll") secara *in situ* di lapangan. Awan titik (*point cloud*) direkonstruksi dari citra multi-pandang dengan algoritme *structure from motion* (SfM), lalu dilakukan segmentasi awan titik berbasis wilayah untuk memisahkan titik boll dari titik ranting, dan pengelompokan berbasis kepadatan untuk menghitung boll individual, termasuk boll yang saling bersentuhan. Dari hasil itu diturunkan jumlah boll, volume boll, dan posisi tiga dimensi boll.

Data berasal dari 30 petak tanaman kapas (*Gossypium* spp.) pada dua lahan percobaan di Greene County, Georgia, AS: 15 petak pada lahan uji varietas (SVT) dan 15 petak pada lahan *nested association mapping* (NAM). Satu petak berupa baris sepanjang 3 m. Acuan hitung adalah panen manual (hitungan boll dan bobot serat per petak) yang dilakukan segera setelah pengambilan citra.

Hasil utama yang dilaporkan: akurasi rerata hitungan boll sekitar 90% untuk 30 petak, dengan akurasi terbaik sekitar 95% (MAPE 5,08%, RMSE 16,87). Koefisien determinasi (R²) antara hasil serat dan jumlah boll bernilai di atas 0,87 dan antara hasil serat dan volume boll di atas 0,66. Metode ini juga dipakai untuk menganalisis sebaran spasial boll.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Jumlah dan posisi boll merupakan komponen hasil serat yang penting bagi pemulia tanaman, tetapi penghitungan manual memakan waktu dan tenaga. Metode berbasis citra dua dimensi (2D) yang ada tidak dapat menghitung jumlah boll maupun memperkirakan ukurannya, dan menurut penulis semua metode 2D mengalami dua keterbatasan: oklusi sulit diatasi karena tidak ada informasi kedalaman, dan struktur objek sulit ditentukan.

Sensor aktif (LiDAR beresolusi tinggi) mahal, sedangkan Kinect-v2 murah tetapi beresolusi rendah untuk ciri tingkat organ di lapangan. Rekonstruksi berbasis citra (pasif) dipandang menyeimbangkan biaya dan resolusi. Penulis menyatakan bahwa, berdasarkan tinjauan yang mereka lakukan, deteksi dan karakterisasi boll tunggal dengan teknologi 3D belum dieksplorasi. Metode untuk malai gandum dan sorgum tidak dapat langsung dipakai karena boll tersebar di seluruh tanaman (fitur posisi tidak dapat dipakai untuk segmentasi), warna berubah akibat sinar matahari, dan boll berbentuk rumit serta sering bersentuhan.

## Ide Utama
Ide utamanya adalah memisahkan dua masalah: (1) memisahkan titik boll dari titik ranting memakai fitur wilayah (warna, spasial, dan bentuk) yang kurang peka terhadap cahaya matahari dibanding warna titik tunggal; dan (2) menghitung boll individual dari kelompok titik boll memakai kepadatan titik dan ukuran, dengan kelompok besar (multi-boll) dipecah menurut hasil bagi volume kelompok terhadap volume boll tunggal rerata. Pengambilan citra dari lima kamera pada satu platform traktor memberi banyak sudut pandang sehingga oklusi berkurang. Hitungan akhir diperoleh dari awan titik tunggal per petak, sehingga satu boll di ruang 3D dihitung satu kali, bukan satu kali per citra.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Lima kamera Fuji X-A10 dipasang pada platform traktor: satu kamera memotret dari atas pada ketinggian sekitar 150 cm dan empat kamera dipasang di satu sisi petak pada jarak sekitar 90 cm dari batang utama. Empat kamera samping membentuk persegi panjang dengan sisi pendek 29 cm dan sisi panjang 44 cm. Pengaturan kamera: mode prioritas rana (kecepatan rana lebih cepat dari 1/200 detik), ISO 200, panjang fokus 16 mm, resolusi 4896 × 3264 piksel. Kecepatan traktor sekitar 0,2 sampai 0,3 m/detik, pemicu serentak untuk kelima kamera pada 1,5 bingkai per detik, dengan tumpang tindih antarcitra lebih dari 60%. Traktor melintasi tiap baris dua kali untuk memindai kedua sisi tanaman sehingga terkumpul sekitar 150 sampai 225 citra per petak. Pengambilan pertama dilakukan pada 24 November 2017 di lahan SVT (15 petak) dan kedua pada 14 Desember 2017 di lahan NAM (15 petak). Kedua hari cerah dengan tingkat iluminasi berbeda (kecepatan rana 1/250 dan 1/400 detik, apertur 7,1). Lahan NAM memuat lebih dari 200 genotipe turunan persilangan galur liar *G. hirsutum* ras *yucatanense* dengan kultivar elit DES 56 atau Acala Maxxa; lahan SVT memuat satu genotipe.

Palang skala buatan dengan empat penanda diletakkan di depan tiap petak untuk membangun sistem koordinat kartesius lokal dan mengkalibrasi ukuran awan titik. Rekonstruksi memakai Agisoft PhotoScan Professional versi 1.2.5 dengan batas titik fitur dan titik pencocokan 60.000 per citra. Satu awan titik petak berisi sekitar 4 juta titik. Panen manual dilakukan sesudah pengambilan citra (Tabel 1): jumlah boll per petak pada SVT berkisar 85 sampai 349 (rerata 218) dan pada NAM 37 sampai 377 (rerata 206); hasil serat pada SVT 330 sampai 1474 g (rerata 845,5 g) dan pada NAM 113 sampai 1633 g (rerata 747,3 g).

### 2. Praproses awan titik
Bidang tanah dihapus dengan ambang ketinggian 10 cm. Garis tanam diperkirakan dengan mengiris awan titik setebal 3 cm dari dasar, mengelompokkan irisan itu dengan DBSCAN 2D (minPts 5, Eps 2 cm), lalu menyesuaikan garis dengan RANSAC. Awan titik kemudian diputar agar garis tanam berada pada x = 0.

### 3. Segmentasi: pemisahan boll dari ranting
Awan titik dibagi menjadi wilayah berlebih-segmen (*over-segmentation*) dengan dua cara yang dibandingkan: *voxel cloud connectivity segmentation* (VCCS, supervoxel) dengan R_seed = 0,08 m dan R_voxel = 0,002 m (bobot warna, spasial, normal masing-masing 1), serta *color-based region growing segmentation* (CRGS) dengan ambang warna 10 dan ambang spasial 8 cm. Dari tiap wilayah diekstraksi vektor fitur 97 dimensi: 64 dimensi histogram warna (16 bin untuk kanal R, G, B, dan S), 30 dimensi fitur spasial (histogram 10 bin per sumbu terhadap titik pusat wilayah), dan fitur bentuk dari nilai eigen matriks kovarians (wilayah berstruktur linear untuk ranting, mendekati bola untuk boll). Klasifikator SVM berkernel RBF dilatih dengan 651 wilayah berlabel manual (328 boll dan 323 ranting), dibagi 0,7 : 0,3 untuk latih dan validasi, dengan parameter C dan γ dicari melalui *grid search* dan validasi silang 5 lipatan. Setelah klasifikasi, filter warna dipakai untuk membuang kulit buah (*exocarp*) hitam.

### 4. Pengelompokan dan penghitungan boll
Titik boll dikelompokkan dengan DBSCAN 3D (Eps 2 cm, MinPts 10). Kelompok bervolume kurang dari 1 cm³ dibuang sebagai derau. Kelompok lain dianggap boll tunggal atau kelompok multi-boll. Volume boll tunggal rerata (v_m) diperkirakan secara iteratif dari matriks rasio volume antarkelompok (modus jumlah rasio bernilai satu) sampai v_m tidak berubah. Jumlah boll dalam kelompok multi-boll adalah volume kelompok dibagi v_m, dibulatkan, lalu k-means 3D dipakai untuk menentukan batas boll individual. Volume boll diestimasi dengan *convex hull*, dan posisi boll diambil dari rerata koordinat titiknya. Boll tunggal dinyatakan berbentuk bola berdiameter 5 sampai 10 cm (volume 133 sampai 523 cm³).

```
 5 kamera, traktor --> SfM (PhotoScan) --> awan titik per petak
        --> hapus tanah, putar sejajar garis tanam
        --> VCCS atau CRGS (wilayah) --> SVM: boll vs ranting
        --> DBSCAN 3D --> kelompok tunggal / multi-boll (bagi volume)
        --> jumlah, volume, posisi boll --> sebaran spasial, regresi hasil serat
```

### 5. Validasi
Hitungan boll dibandingkan dengan hitungan manual memakai MAPE, R², dan RMSE. Regresi linear menghubungkan hasil serat dengan jumlah boll dan dengan volume boll. Sebaran spasial boll dianalisis dengan membagi ruang menjadi irisan pada sumbu tinggi dan sumbu x.

## Eksperimen dan Hasil
Klasifikasi wilayah boll dan ranting: untuk wilayah VCCS, parameter optimal C = 5,28 dan γ = 4,60 dengan akurasi latih 95,6% dan validasi 91,6%; untuk wilayah CRGS, C = 1 dan γ = 2,30 dengan akurasi latih 94,7% dan validasi 91,4%. VCCS sekitar lima kali lebih cepat daripada CRGS.

Hitungan boll: akurasi rerata sekitar 90% untuk 30 petak; akurasi terbaik sekitar 95% (MAPE 5,08%, RMSE 16,87). Data pengambilan pertama (SVT) memberi MAPE dan RMSE lebih baik daripada pengambilan kedua (NAM), yang dikaitkan penulis dengan boll yang sudah terkulai dan lebih tertutup di akhir musim. R² hitungan terhadap acuan lebih baik di NAM karena rentang jumlah boll lebih lebar. Teks tidak menyajikan MAPE dan RMSE hitungan boll per metode dalam tabel; nilainya hanya ada pada diagram pencar (Gambar 8) yang tidak terbaca dari ekstraksi teks.

Korelasi dengan hasil serat (Tabel 2; hasil serat diprediksi dari boll):

| Atribut | Metode | SVT: R² / MAPE (%) / RMSE (g) | NAM: R² / MAPE (%) / RMSE (g) |
|---|---|---|---|
| Jumlah boll | VCCS | 0,91 / 7,99 / 77,09 | 0,90 / 19,29 / 143,84 |
| Jumlah boll | CRGS | 0,87 / 8,15 / 93,57 | 0,90 / 17,75 / 141,01 |
| Volume boll | VCCS | 0,66 / 17,10 / 152,05 | 0,84 / 37,86 / 179,94 |
| Volume boll | CRGS | 0,66 / 17,59 / 151,70 | 0,85 / 34,36 / 173,25 |

Jumlah boll berkorelasi lebih baik dengan hasil serat daripada volume boll di kedua lahan.

Analisis sebaran spasial pada satu petak contoh: kotak pembatas boll berukuran 0,83 m, 3,35 m, dan 0,78 m pada sumbu x, y, z; sekitar 70% boll berada di sisi kanan petak (tanaman miring akibat badai Irma); 91,4% boll berada dalam jarak 0,3 m dari garis tanam; tinggi boll terendah 0,11 m, tertinggi 0,78 m, rerata 0,42 m; dan sekitar 85% boll berada pada rentang tinggi 0,2 sampai 0,6 m.

Sumber galat hitungan menurut penulis adalah pemecahan kelompok multi-boll. Bila boll di kanopi atas belum terbuka penuh dan kecil sedangkan boll bawah terbuka dan besar, v_m yang dihitung mendekati boll kecil sehingga kelompok besar terlalu banyak dipecah (penghitungan berlebih). Bila semua boll terbuka penuh, v_m besar sehingga kelompok dua boll dapat terhitung satu (penghitungan kurang). Waktu pemrosesan sekitar tiga sampai lima jam per petak.

## Kelebihan dan Keterbatasan
Kelebihan yang dapat dicatat: sistem berbiaya rendah (kamera biasa), awan titik 3D yang padat dari banyak sudut pandang mengurangi oklusi, fitur wilayah (bentuk dan sebaran spasial) tidak peka terhadap variasi iluminasi, boll yang bersentuhan dipecah melalui volume, dan keluarannya (jumlah, volume, posisi) lebih kaya daripada hitungan 2D. Validasi memakai acuan panen manual pada 30 petak dan dua kondisi musim.

Keterbatasan yang dinyatakan penulis: platform traktor berat sehingga dapat mengganggu dan memadatkan tanah serta memerlukan pengemudi; kualitas citra bergantung pada angin dan pencahayaan (siang hari disarankan) dan pengaturan kamera bergantung pada pengalaman manusia; rekonstruksi dan analisis dilakukan luring dan lambat (tiga sampai lima jam per petak); fitur dirancang manual dan jumlah sampel berlabel terbatas; serta pemecahan kelompok multi-boll menjadi sumber galat. Penulis menyarankan robot ringan, UAV dengan kamera miring, dan pembelajaran mendalam 3D sebagai pekerjaan lanjutan.

Menurut pembacaan ringkasan ini, keterbatasan lain adalah: seluruh data berasal dari satu lokasi dan satu musim (dua tanggal), sehingga generalisasi tidak teruji; hanya ada satu kelas (boll), tanpa atribut kelas seperti tingkat kematangan; angka MAPE dan RMSE hitungan boll per lahan hanya tersedia pada gambar; dan teks menyebut tanggal pengambilan pertama sebagai 24 November 2017 pada bagian metode tetapi 22 November 2017 pada bagian hasil. Klaim bahwa metode ini lebih akurat daripada metode 2D tidak didukung perbandingan langsung pada data yang sama; perbandingan hanya merujuk pada makalah lain.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme rekonstruksi 3D: citra dari lima kamera dan beberapa posisi traktor digabung melalui SfM menjadi satu awan titik per petak, sehingga identitas boll ditetapkan di ruang 3D (kelompok titik) dan bukan per citra. Boll yang bersentuhan dipisahkan menurut rasio volume. Hitungan dilaporkan per petak, tidak per kelas atribut; hanya satu kelas (boll) yang ditangani. Acuan hitung adalah panen manual pada petak yang sama, yaitu hitungan boll sesudah pengambilan citra, bukan anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan bahwa penyatuan pandangan di ruang 3D dengan SfM dan skala metrik dari palang penanda dapat menghilangkan penghitungan ganda lintas pandangan, serta penggunaan panen atau hitungan fisik sebagai acuan validasi. Pembatasnya adalah bahwa pendekatan ini memerlukan citra yang saling tumpang tindih dalam jumlah besar (150 sampai 225 per petak) dan pemrosesan beberapa jam, serta tidak menangani label kelas per buah. Teks tidak membahas tanaman tinggi seperti kelapa sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `sun2020three`.

Sun dkk. memetakan buah kapas secara *in situ* dengan rekonstruksi SfM dari citra multi-pandang lima kamera pada platform traktor, memisahkan titik boll dari ranting dengan klasifikasi SVM berbasis wilayah (VCCS atau CRGS), dan menghitung boll individual dengan DBSCAN 3D serta pemecahan kelompok multi-boll berdasarkan volume. Pada 30 petak (dua lahan di Georgia, AS), akurasi rerata hitungan boll sekitar 90% terhadap panen manual (terbaik sekitar 95%, MAPE 5,08%), dan R² hasil serat terhadap jumlah boll serta volume boll masing-masing di atas 0,87 dan 0,66. Metode ini juga menghasilkan volume dan posisi 3D boll.

Catatan verifikasi data: akurasi rerata sekitar 90%, akurasi terbaik sekitar 95% (MAPE 5,08%, RMSE 16,87), dan alasan perbedaan antartanggal berasal dari Bagian 3.2; ringkasan Tabel 1 (statistik panen manual) dan Tabel 2 (R², MAPE, RMSE regresi hasil serat) dari tabel yang terbaca dengan baik pada ekstraksi; akurasi SVM (95,6%, 91,6%, 94,7%, 91,4%) dan parameter C serta γ dari Bagian 3.1; sebaran spasial dari Bagian 3.4. Nilai R² di atas 0,87 dan 0,66 pada abstrak dan Bagian 3.3 merupakan batas bawah dari Tabel 2 (0,87 sampai 0,91 untuk jumlah dan 0,66 sampai 0,85 untuk volume). Gambar (termasuk Gambar 8 dengan diagram pencar hitungan) tidak terbaca dari teks, sehingga MAPE dan RMSE hitungan boll per lahan dan per metode tidak dapat diverifikasi. Rumus pada ekstraksi teks terpotong sebagian dan tidak dipakai untuk angka. Jumlah citra total tidak dilaporkan selain 150 sampai 225 per petak.
