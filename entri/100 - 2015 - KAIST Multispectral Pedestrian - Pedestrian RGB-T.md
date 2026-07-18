# 100 - Multispectral Pedestrian Detection: Benchmark Dataset and Baseline

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hwang2015kaist` |
| Judul asli | Multispectral Pedestrian Detection: Benchmark Dataset and Baseline |
| Penulis | Soonmin Hwang, Jaesik Park, Namil Kim, Yukyung Choi, In So Kweon |
| Tahun | 2015 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2015) |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **CVF Open Access (halaman resmi & PDF):** https://openaccess.thecvf.com/content_cvpr_2015/html/Hwang_Multispectral_Pedestrian_Detection_2015_CVPR_paper.html
- **Halaman proyek & unduhan dataset:** https://soonminhwang.github.io/rgbt-ped-detection/
- **Google Scholar:** https://scholar.google.com/scholar?q=Multispectral%20Pedestrian%20Detection%3A%20Benchmark%20Dataset%20and%20Baseline
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Multispectral%20Pedestrian%20Detection%3A%20Benchmark%20Dataset%20and%20Baseline&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan dataset KAIST Multispectral Pedestrian, kumpulan data pejalan kaki pertama berskala besar yang menyediakan pasangan citra warna (RGB) dan citra termal gelombang panjang (*long-wave infrared*/LWIR) yang tersejajar secara fisik piksel demi piksel. Citra direkam dari kendaraan bergerak pada skenario lalu lintas siang dan malam, dilengkapi anotasi kotak pembatas (*bounding box*) padat beserta tingkat oklusi dan korespondensi temporal antar-bingkai. Selain dataset, makalah menyajikan serangkaian *baseline* (garis dasar pembanding) detektor multispektral yang dibangun bertahap di atas ACF (*Aggregated Channel Features*), sebuah detektor pejalan kaki berbasis kanal fitur teragregasi.

Hasil utamanya bersifat kuantitatif dan kualitatif sekaligus: penambahan kanal termal ke detektor berbasis warna menurunkan *log-average miss rate* (tingkat galat lolos rata-rata, dijelaskan pada bagian protokol evaluasi) sekitar 15 poin persentase secara keseluruhan, dengan penurunan paling tajam terjadi pada rekaman malam hari — dari 90,17% menjadi 63,99%. Dataset ini menjadi tolok ukur (*benchmark*) rujukan yang dipakai hampir seluruh makalah deteksi pejalan RGB-termal (RGB-T) sesudahnya, termasuk seluruh bab pada klaster Pedestrian RGB-T dalam tinjauan ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2015, riset deteksi pejalan kaki didominasi citra warna. Tolok ukur populer seperti Caltech Pedestrian dan KITTI hanya menyediakan citra RGB, sehingga metode yang dikembangkan di atasnya juga hanya mengandalkan informasi warna dan tekstur tampak. Pendekatan ini gagal pada kondisi cahaya rendah: pada malam hari, kontras citra RGB menurun tajam dan derau sensor meningkat, sehingga bentuk manusia sulit dibedakan dari latar belakang.

Kamera termal menawarkan jalan keluar karena mengukur radiasi panas, bukan pantulan cahaya tampak — manusia dan makhluk hidup lain memancarkan radiasi pada pita gelombang panjang inframerah (7,5–13 mikrometer) akibat suhu tubuhnya, sehingga tetap terlihat jelas tanpa bergantung pada pencahayaan lingkungan. Namun sebelum makalah ini, dataset publik yang memasangkan citra RGB dan termal secara memadai belum tersedia. Dataset sejenis yang ada, seperti OSU-CT dan LITIV, berskala kecil (belasan ribu bingkai) dan umumnya memakai konfigurasi stereo — dua kamera terpisah pada posisi berbeda. Konfigurasi stereo menimbulkan paralaks, yaitu pergeseran posisi objek yang tampak berbeda antar-dua sudut pandang kamera akibat jarak antara kedua lensa, sehingga memerlukan algoritme registrasi (penyelarasan) tambahan pascaperekaman yang tidak selalu akurat, terutama untuk objek pada jarak berbeda-beda seperti pejalan kaki di berbagai kedalaman jalan.

Masalah kedua adalah minimnya data malam hari. Sebagian besar dataset pejalan kaki sebelumnya direkam pada kondisi siang atau pencahayaan baik, sehingga metode yang dilatih di atasnya tidak teruji pada skenario gelap — padahal kecelakaan lalu lintas yang melibatkan pejalan kaki secara proporsional lebih sering terjadi pada malam hari.

## Ide Utama

Gagasan inti makalah ini adalah membangun perangkat akuisisi yang menyejajarkan citra RGB dan termal sejak proses perekaman, alih-alih mengoreksi ketidaksejajaran secara komputasional setelah data terkumpul. Alat ini memakai pembagi berkas (*beam splitter*) optik: satu berkas cahaya dari sumbu pandang yang sama dipecah dan diarahkan ke dua sensor sekaligus, satu sensor warna dan satu sensor termal. Karena kedua sensor menerima citra dari sumbu optik yang identik, pasangan citra yang dihasilkan bebas paralaks tanpa memerlukan algoritme penyelarasan tambahan.

Di atas dataset yang terkumpul, makalah menunjukkan nilai praktisnya lewat serangkaian *baseline* yang menambahkan informasi termal secara bertahap ke detektor ACF, lalu mengukur seberapa besar setiap tambahan menurunkan tingkat galat deteksi pada kondisi siang, malam, dan gabungan keduanya. Dengan cara ini, makalah tidak hanya menyediakan data, tetapi juga bukti kuantitatif bahwa kanal warna dan termal saling melengkapi.

## Cara Kerja Langkah demi Langkah

### Akuisisi Perangkat Keras

Rig perekaman terdiri atas kamera RGB, kamera termal, dan pembagi berkas yang dipasang pada penjepit tiga sumbu (*three-axis jig*) untuk menjaga kesejajaran optik keduanya tetap presisi. Skema penempatan komponennya, dilihat dari atas dan dari depan, adalah sebagai berikut.

```
tampak atas rig                      tampak depan rig
                                      
   kamera termal                        kamera RGB
        |                                    |
   penjepit tiga sumbu                  pembagi berkas
        |                                    |
   pembagi berkas --- kamera RGB       (satu sumbu optik bersama)
                                      
   satu berkas cahaya dari sumbu pandang yang sama dipecah oleh
   pembagi berkas menuju sensor RGB dan sensor termal; posisi
   piksel kedua citra sejajar sejak perekaman, tanpa paralaks
```

Rig dipasang pada kendaraan dan dijalankan pada rute lalu lintas biasa, merekam pasangan citra RGB dan termal secara bersamaan pada siang dan malam hari. Karena kedua sensor berbagi sumbu optik yang sama, setiap piksel citra RGB berkorespondensi langsung dengan piksel termal pada koordinat yang sama, sehingga proses anotasi maupun pelatihan detektor dapat langsung menumpuk (*stack*) kedua kanal tanpa transformasi geometris tambahan.

### Skema Anotasi

Setiap bingkai diberi anotasi kotak pembatas untuk tiga kategori objek: *person* (satu pejalan kaki tunggal), *people* (kelompok pejalan kaki yang saling tumpang tindih sehingga sulit dipisah menjadi kotak individual), dan *cyclist* (pesepeda). Tingkat oklusi (keterhalangan objek oleh benda lain) ditandai dengan warna kotak: hijau untuk tanpa oklusi, kuning untuk oklusi sebagian, dan merah untuk oklusi berat. Anotasi juga menyertakan korespondensi temporal, yaitu penandaan objek yang sama antar-bingkai berurutan dalam satu klip video, mengikuti konvensi yang sudah dipakai Caltech Pedestrian.

### Skala Dataset dan Pembagian Latih-Uji

Menurut tabel perbandingan dataset pada makalah, himpunan latih terdiri atas 41,5 ribu anotasi pejalan kaki pada 50,2 ribu citra, sedangkan himpunan uji terdiri atas 44,7 ribu anotasi pejalan kaki pada 45,1 ribu citra, sehingga total mencapai sekitar 95 ribu pasangan bingkai RGB-termal. Angka ini ditempatkan setara dengan dataset warna-saja berskala besar seperti Caltech Pedestrian dan KITTI, sekaligus menjadi dataset RGB-termal pertama yang menyediakan label oklusi dan korespondensi temporal pada skala tersebut — dataset RGB-termal sebelumnya seperti LITIV maupun OSU-CT jauh lebih kecil dan tidak menyertakan kedua jenis label itu sekaligus.

### Baseline Detektor Multispektral

Untuk menunjukkan nilai kanal termal, makalah membangun empat varian detektor secara bertahap di atas ACF, detektor pejalan kaki yang mengekstraksi sekumpulan kanal fitur (gradien, magnitudo gradien, dan warna) dari citra lalu mengklasifikasikannya dengan jendela geser multi-skala:

1. **ACF** — hanya memakai kanal dari citra RGB, tanpa informasi termal.
2. **ACF+T** — menambahkan citra termal mentah sebagai kanal fitur tambahan.
3. **ACF+T+TM+TO** — menambahkan pula magnitudo termal (TM, kekuatan gradien pada citra termal) dan orientasi termal (TO, arah gradien pada citra termal).
4. **ACF+T+THOG** — menambahkan histogram orientasi gradien yang dihitung khusus dari citra termal (*thermal HOG*), varian dengan performa terbaik.

Urutan ini disusun agar dapat dibedakan sumbangan setiap jenis informasi termal terhadap penurunan galat deteksi, bukan sekadar membandingkan detektor warna melawan detektor gabungan sebagai satu blok.

### Protokol Evaluasi

Evaluasi memakai kurva *miss rate* (proporsi pejalan kaki yang gagal terdeteksi) terhadap FPPI (*false positives per image*, jumlah deteksi keliru rata-rata per citra), mengikuti protokol yang dipopulerkan Caltech Pedestrian Benchmark. Sumbu FPPI memakai skala logaritmik karena rentang nilainya membentang beberapa orde besaran, dari sangat sedikit deteksi keliru hingga cukup banyak. Kinerja setiap detektor diringkas menjadi satu angka *log-average miss rate*: rata-rata tingkat galat lolos pada rentang FPPI yang relevan secara praktis, sesuai konvensi subset "reasonable" (kondisi wajar) yang lazim dipakai pada evaluasi deteksi pejalan kaki, yakni mengecualikan pejalan kaki yang teroklusi berat atau berukuran sangat kecil pada citra. Semakin kecil angka ini, semakin baik detektornya.

## Eksperimen dan Hasil

Makalah melaporkan kurva *miss rate* versus FPPI pada tiga kondisi pengujian terpisah: gabungan siang-malam, siang saja, dan malam saja. Ringkasan angka *log-average miss rate* untuk keempat varian detektor pada masing-masing kondisi adalah sebagai berikut.

| Kondisi | ACF | ACF+T | ACF+T+TM+TO | ACF+T+THOG |
|---|---|---|---|---|
| Siang & malam | 79,26% | 72,46% | 68,11% | 64,76% |
| Siang | 81,09% | 76,48% | 70,02% | 64,17% |
| Malam | 90,17% | 74,54% | 64,92% | 63,99% |

Interpretasinya bertingkat. Pertama, pada kondisi malam, detektor ACF warna-saja memiliki *miss rate* tertinggi di antara seluruh kombinasi (90,17%), mengonfirmasi bahwa citra warna kehilangan sebagian besar informasi berguna saat cahaya kurang. Kedua, penambahan kanal termal mentah (ACF+T) menurunkan *miss rate* malam hari sebesar hampir 16 poin persentase (menjadi 74,54%), penurunan jauh lebih besar dibandingkan penurunan pada kondisi siang (dari 81,09% menjadi 76,48%, sekitar 5 poin persentase) — bukti langsung bahwa manfaat kanal termal paling besar justru ketika informasi warna paling lemah. Ketiga, varian terbaik ACF+T+THOG menyempitkan selisih siang-malam: 64,17% pada siang berbanding 63,99% pada malam, hampir setara, menunjukkan bahwa kombinasi fitur termal yang lengkap dapat menyeimbangkan kinerja detektor across kedua kondisi pencahayaan. Secara keseluruhan pada kondisi gabungan siang-malam, *baseline* terbaik menurunkan *miss rate* dari 79,26% menjadi 64,76%, selisih sekitar 15 poin persentase — angka yang secara eksplisit disebut oleh penulis sebagai penurunan rata-rata hasil kontribusi kanal termal.

Hasil ini menetapkan argumen inti dataset: informasi RGB dan termal bersifat komplementer, bukan salah satu menggantikan yang lain, karena keduanya memberi kontribusi berbeda tergantung kondisi cahaya.

## Kelebihan dan Keterbatasan

Kelebihan utama dataset ini terletak pada tiga hal. Pertama, akuisisi berbasis pembagi berkas menghasilkan penyejajaran piksel yang presisi sejak perekaman, mengeliminasi kebutuhan algoritme registrasi pascaproses yang rawan galat pada dataset stereo sebelumnya. Kedua, skala datanya — puluhan ribu bingkai dengan anotasi padat, oklusi, dan korespondensi temporal — menyamai dataset warna-saja papan atas pada masanya, sesuatu yang belum dicapai dataset RGB-termal sebelumnya. Ketiga, cakupan siang dan malam secara eksplisit memungkinkan evaluasi terpisah per kondisi cahaya, sesuatu yang jarang tersedia pada benchmark pejalan kaki sebelum ini.

Dari sisi rekayasa, keterbatasan pertama adalah rig pembagi berkas memerlukan perangkat keras khusus yang tidak mudah direplikasi peneliti lain, berbeda dengan dataset stereo yang cukup memakai dua kamera murah terpisah. Kedua, secara konseptual, dataset ini terbatas pada skenario lalu lintas kendaraan; generalisasi ke skenario lain (misalnya pengawasan statis atau ruang dalam ruangan) tidak diuji oleh makalah asli. Ketiga, *baseline* ACF yang diajukan merupakan detektor generasi lama berbasis fitur tangan (bukan pembelajaran mendalam), sehingga angka *miss rate* yang dilaporkan bukan batas atas kemampuan deteksi pada dataset ini — literatur sesudahnya menunjukkan penurunan *miss rate* jauh lebih besar memakai jaringan saraf konvolusi.

## Kaitan dengan Bab Lain

Bab ini adalah fondasi data bagi seluruh klaster Pedestrian RGB-T dalam tinjauan ini: tanpa benchmark yang disediakan di sini, metode-metode fusi sesudahnya tidak memiliki tolok ukur bersama untuk dibandingkan. [101 - IAF R-CNN](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md) memakai dataset ini untuk melatih mekanisme pembobotan modal berdasar kondisi cahaya siang/malam yang sama-sama diukur pada makalah ini. [102 - MBNet](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md), [103 - GAFF](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md), [104 - Cyclic Fuse-and-Refine](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md), dan [105 - CMPD](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md) seluruhnya melaporkan angka *miss rate* pada protokol siang/malam/gabungan yang persis mengikuti format evaluasi yang diperkenalkan di sini. Paralel konseptualnya berada pada [106 - RGB-D Fusion for Detection](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md), yang membahas komplementaritas dua modal berbeda (RGB dan kedalaman) dengan argumen struktural serupa: modal tunggal gagal pada kondisi tertentu, sedangkan kombinasi modal menutupi kelemahan itu.

## Poin untuk Sitasi

Kutip dengan kunci `hwang2015kaist`. Ringkasan yang aman dikutip: "KAIST Multispectral Pedestrian memperkenalkan dataset RGB-termal tersejajar piksel (via pembagi berkas) berskala puluhan ribu bingkai dengan anotasi oklusi dan korespondensi temporal, serta baseline ACF multispektral yang menurunkan log-average miss rate sekitar 15 poin persentase dibanding detektor warna-saja, dengan manfaat terbesar pada malam hari (90,17% menjadi 63,99%)." Angka pada tabel hasil (79,26%/72,46%/68,11%/64,76% dan turunannya per kondisi siang/malam) diambil dari kurva Gambar 3 pada naskah ekstraksi resmi dan cukup dapat diandalkan. Angka skala dataset (41,5 ribu/50,2 ribu latih, 44,7 ribu/45,1 ribu uji, total ±95 ribu bingkai) berasal dari tabel perbandingan pada naskah yang sama. Perlu verifikasi tambahan: sejumlah sumber sekunder menyebut total anotasi akhir dataset sebagai 103.128 kotak pembatas mencakup 1.182 pejalan kaki unik dengan resolusi citra 640×480 piksel pada laju 20 Hz — angka ini kemungkinan berasal dari versi rilis dataset yang telah diperbarui setelah publikasi awal dan belum berhasil dikonfirmasi silang terhadap naskah CVPR 8 halaman penuh (hanya versi ekstrak dua halaman yang berhasil diperiksa langsung); batas ambang tinggi piksel dan rentang FPPI persis untuk subset "reasonable" juga belum terverifikasi ke naskah lengkap.
