# 093 - PointPainting: Sequential Fusion for 3D Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vora2020pointpainting` |
| Judul asli | PointPainting: Sequential Fusion for 3D Object Detection |
| Penulis | Sourabh Vora, Alex H. Lang, Bassam Helou, Oscar Beijbom |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1911.10150
- **Google Scholar:** https://scholar.google.com/scholar?q=PointPainting%3A%20Sequential%20Fusion%20for%203D%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PointPainting%3A%20Sequential%20Fusion%20for%203D%20Object%20Detection&sort=relevance

## Gambaran Umum

PointPainting mengusulkan skema fusi kamera-LiDAR yang disebut fusi sekuensial: skor segmentasi semantik dari citra RGB diproyeksikan ke setiap titik *point cloud* (kumpulan titik koordinat 3D hasil pindaian LiDAR) LiDAR sebelum titik tersebut diproses oleh detektor 3D yang sudah ada. Setiap titik LiDAR "dicat" dengan vektor skor kelas hasil segmentasi citra, sehingga titik yang semula hanya membawa informasi geometri (koordinat dan intensitas pantulan) kini juga membawa informasi semantik dari kamera. Detektor hilir — PointPillars, VoxelNet, atau PointRCNN — menerima titik yang telah diperkaya ini tanpa perubahan arsitektur, kecuali penyesuaian jumlah kanal masukan.

Pada validasi KITTI, penyisipan skema ini menaikkan *mean Average Precision* (mAP) ketiga detektor tersebut, dan pada tolok ukur nuScenes selisihnya lebih besar lagi. Kontribusi utama makalah bukan detektor baru, melainkan bukti bahwa informasi semantik citra dapat disuntikkan ke detektor LiDAR mana pun melalui titik masukannya sendiri, tanpa menyentuh lapisan jaringan di dalamnya. Pendekatan ini menempatkan PointPainting sebagai lapisan pra-pemrosesan yang dapat dipasang di depan (*plug-in*) berbagai detektor 3D berbasis LiDAR.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sampai 2019, detektor 3D berbasis LiDAR saja — seperti VoxelNet (bab 087), PointPillars (bab 088), dan PointRCNN (bab 089) — secara konsisten mengungguli metode fusi kamera-LiDAR pada tolok ukur populer semacam KITTI. Kesenjangan ini janggal karena citra RGB memuat informasi tekstur dan warna yang tidak dimiliki *point cloud*, sehingga secara intuitif fusi seharusnya menambah, bukan mengurangi, akurasi. Makalah PointPainting menjadikan kesenjangan ini sebagai motivasi langsung: metode fusi yang ada gagal memanfaatkan citra secara efektif.

Penyebabnya terletak pada desain metode fusi terdahulu. MV3D (bab 091) dan AVOD (bab 092) melakukan fusi pada level fitur di tengah jaringan: fitur dari cabang citra dan cabang *point cloud* digabungkan pada peta fitur menengah, sehingga arsitektur kedua cabang harus dirancang berpasangan dan disesuaikan ulang setiap kali salah satu cabang diganti. Frustum PointNets (bab 090) memakai deteksi 2D pada citra untuk membatasi ruang pencarian 3D berbentuk kerucut pandang (*frustum*), tetapi kesalahan pada tahap deteksi 2D langsung membatasi ruang pencarian 3D secara permanen. Ketiganya berbagi masalah yang sama: fusi terikat erat pada arsitektur detektor tertentu, sehingga metode fusi tidak dapat langsung dipasangkan ke detektor LiDAR generasi baru begitu detektor itu terbit. PointPainting mencari cara memasukkan informasi semantik citra tanpa mengikat diri pada satu arsitektur detektor.

## Ide Utama

Gagasan inti PointPainting adalah memindahkan titik penggabungan informasi dari level fitur jaringan ke level data masukan. Alih-alih menggabungkan fitur di tengah jaringan, setiap titik LiDAR diperkaya lebih dulu, sebelum masuk ke detektor mana pun, dengan skor kelas hasil segmentasi semantik citra pada piksel yang berkorespondensi dengannya. Titik yang telah diperkaya ini disebut titik yang "dicat" (*painted point*): representasinya tetap berupa titik individual dengan koordinat (x, y, z) dan intensitas pantulan, hanya saja kini ditambahi beberapa angka skor kelas.

Karena penggabungan terjadi pada data masukan, bukan pada arsitektur jaringan, detektor hilir tidak perlu tahu bagaimana skor semantik itu dihasilkan. Detektor hanya melihat titik dengan jumlah kanal masukan yang lebih banyak dari biasanya. Konsekuensinya, metode ini dapat dipasangkan ke detektor LiDAR generasi mana pun tanpa mendesain ulang arsitektur — cukup mengubah lapisan pertama yang membaca jumlah kanal masukan.

## Cara Kerja Langkah demi Langkah

Alur PointPainting terdiri atas tiga tahap berurutan: segmentasi semantik citra, proyeksi dan pengecatan titik, lalu deteksi 3D oleh jaringan LiDAR standar.

```
citra RGB                        point cloud LiDAR (mentah)
   |                                     |
   v                                     |
segmentasi semantik                      |
(mis. DeepLabv3+)                        |
   |                                     |
   v                                     v
skor kelas per piksel  ----->  proyeksi titik ke citra
(mis. 4 kelas di KITTI)         (kalibrasi kamera-LiDAR)
                                          |
                                          v
                          titik "dicat": (x, y, z, refleksi,
                                skor kelas 1..K)
                                          |
                                          v
                       detektor 3D LiDAR (PointPillars,
                       VoxelNet, atau PointRCNN) — arsitektur
                       tidak berubah, hanya kanal masukan
```

### Segmentasi Semantik Citra

Tahap pertama menjalankan jaringan segmentasi semantik pada citra RGB untuk menghasilkan skor kelas bagi setiap piksel. Segmentasi semantik adalah tugas memberi label kelas pada tiap piksel citra (bukan hanya kotak pembatas). Pada eksperimen KITTI, makalah memakai DeepLabv3+ yang dilatih pada Mapillary, disetel halus pada Cityscapes, lalu disetel halus lagi pada anotasi segmentasi KITTI dengan 4 kelas keluaran (mobil, pejalan kaki, pesepeda, dan latar belakang). Pada eksperimen nuScenes dipakai jaringan berbasis ResNet dengan 11 kelas keluaran (10 kelas objek deteksi ditambah latar belakang), dilatih pada dataset nuImages.

### Proyeksi dan "Pengecatan" Titik LiDAR

Tahap kedua memproyeksikan setiap titik LiDAR ke bidang citra memakai parameter kalibrasi kamera-LiDAR yang sudah diketahui (matriks rotasi, translasi, dan proyeksi kamera). Titik yang jatuh pada koordinat piksel tertentu diberi (dicat dengan) vektor skor kelas piksel tersebut. Hasilnya, satu titik yang semula hanya memuat 4 angka (x, y, z, intensitas pantulan) kini memuat 4 + K angka, dengan K jumlah kelas segmentasi. Titik yang berada di luar jangkauan pandang kamera (misalnya di belakang kendaraan) tidak memperoleh skor tambahan dan biasanya diberi vektor nol atau ditandai sebagai tidak tercakup.

### Penyesuaian Detektor Hilir

Tahap ketiga memasukkan titik yang telah dicat ke detektor 3D LiDAR standar. Karena hanya dimensi vektor fitur titik yang bertambah, penyesuaian yang diperlukan terbatas pada lapisan pembacaan fitur pertama. Untuk PointPillars, dimensi fitur per titik naik dari 9 menjadi 13 (menambahkan 4 skor kelas KITTI), dan lapisan penyandi (*encoder*) pilar disesuaikan dari (9, 64) menjadi (13, 64) saluran. Untuk VoxelNet, dimensi naik dari 7 menjadi 11, dengan lapisan penyandi voxel berubah dari (7, 32) dan (64, 128) menjadi (11, 32) dan (64, 128). Untuk PointRCNN, dimensi naik dari 4 menjadi 8, dan penyesuaian diterapkan baik pada penyandi maupun pada tahap *region pooling* (pengumpulan fitur wilayah kandidat) tahap kedua. Tidak ada lapisan baru yang ditambahkan; hanya lebar kanal masukan yang berubah.

### Pertimbangan Waktu Nyata

Karena segmentasi citra dan pemindaian LiDAR berjalan pada laju berbeda, makalah membandingkan dua skema pencocokan waktu: pencocokan bersamaan (*concurrent matching*, memakai citra pada waktu yang sama persis dengan pindaian LiDAR) dan pencocokan berurutan (*consecutive matching*, memakai citra dari siklus sebelumnya agar kedua proses dapat dijalankan berpipa/*pipelined*). Skema kedua menambah latensi proyeksi sekitar 0,15 milidetik dan latensi penyandi sekitar 0,6 milidetik, total tambahan sekitar 0,75 milidetik, tanpa penurunan akurasi dibandingkan pencocokan bersamaan — artinya PointPainting dapat dijalankan berpipa pada sistem waktu nyata tanpa mengorbankan latensi maupun akurasi.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada set validasi KITTI (deteksi kendaraan, pejalan kaki, dan pesepeda) serta pada nuScenes. Metrik BEV (*bird's-eye view*, deteksi dari sudut pandang atas) dilaporkan sebagai mAP pada tingkat kesulitan sedang (*moderate*):

| Detektor | mAP dasar | mAP setelah dicat | Selisih |
|---|---|---|---|
| PointPillars | 73,78 | 76,27 | +2,50 |
| VoxelNet | 71,83 | 73,55 | +1,71 |
| PointRCNN | 72,42 | 75,80 | +3,37 |

Ketiga detektor — masing-masing mewakili desain berbeda (satu tahap berbasis pilar, satu tahap berbasis *voxel*, dan dua tahap berbasis titik) — memperoleh kenaikan mAP setelah dicat, dengan total 24 dari 27 perbandingan (3 detektor × 3 kelas × 3 tingkat kesulitan) membaik. Kenaikan terbesar konsisten terjadi pada kelas yang lebih sulit dideteksi dari geometri saja: pejalan kaki dan pesepeda naik lebih tajam daripada mobil (misalnya pesepeda PointRCNN naik 6,10 poin, sedangkan mobil PointRCNN hanya naik 1,45 poin). Pola ini masuk akal karena mobil sudah cukup dikenali dari bentuk geometrinya, sementara pejalan kaki dan pesepeda lebih mudah dibedakan lewat tekstur dan warna citra yang tidak tersedia bagi detektor LiDAR saja.

Pada set uji KITTI, PointRCNN yang dicat mencapai mAP BEV 69,86, naik 2,94 poin dari PointRCNN dasar (66,92), dan pada saat publikasi menjadi hasil terbaik pada papan peringkat KITTI untuk tugas deteksi BEV. Pada nuScenes, PointPillars+ (varian PointPillars yang telah ditingkatkan penulis makalah, dengan resolusi pilar diperkecil dari 0,25 m menjadi 0,2 m serta arsitektur dan augmentasi data yang disempurnakan) mencapai mAP 46,4 dan *NuScenes Detection Score* (NDS, metrik gabungan akurasi deteksi dan estimasi atribut) 58,1, naik dari 40,1 dan 55,0 pada versi tanpa pengecatan — kenaikan 6,3 poin mAP. Kenaikan terbesar pada nuScenes terjadi pada kelas sepeda (+10,1 AP) dan kerucut lalu lintas (+16,8 AP), kelas yang secara geometri kecil dan mirip objek lain, tetapi mudah dibedakan secara visual.

Studi ablasi pada nuScenes menunjukkan hubungan hampir linear antara mIoU (*mean Intersection over Union*, metrik kualitas segmentasi) segmentasi dan mAP deteksi 3D: semakin baik segmentasi, semakin besar kenaikan deteksi. Ketika skor segmentasi diganti kotak kebenaran (*oracle*, seolah segmentasi sempurna), mAP naik hingga 27 poin — angka ini menunjukkan bahwa perbaikan segmentasi 2D di masa depan berpotensi meningkatkan deteksi 3D lebih jauh tanpa mengubah detektor sama sekali.

## Kelebihan dan Keterbatasan

Kelebihan utama PointPainting adalah kesederhanaan dan sifat *plug-in*-nya: metode ini tidak memerlukan pelatihan gabungan dua cabang jaringan seperti MV3D atau AVOD, dan terbukti meningkatkan tiga arsitektur detektor yang berbeda desainnya tanpa modifikasi arsitektur di luar lapisan masukan. Kenaikan akurasi paling nyata justru pada kelas sulit (pejalan kaki, pesepeda, objek kecil di nuScenes), yang secara langsung relevan untuk keselamatan kendaraan otonom.

Dari sisi rekayasa, keterbatasan pertama adalah sifat sekuensialnya: karena segmentasi dan deteksi dilatih terpisah, galat pada tahap segmentasi merambat ke tahap deteksi tanpa jalur koreksi baliknya. Makalah sendiri mencatat bahwa performa jauh menurun pada kelas dengan segmentasi buruk, misalnya *trailer* (perolehan/*recall* segmentasi 39%) dan kendaraan konstruksi (40%) pada nuScenes. Kedua, titik yang jatuh pada wilayah tumpang tindih antar-kamera (pada susunan sensor dengan citra dari berbagai sudut) dipilih skor kelasnya secara acak dari salah satu citra; makalah mengusulkan pemilihan berbasis entropi sebagai perbaikan yang belum diuji. Ketiga, secara konseptual, ketidakcocokan definisi kelas antara segmentasi dan deteksi (misalnya sepeda sebagai objek versus pesepeda sebagai gabungan objek dan pengendara di KITTI) memerlukan penanganan manual pasca-proses. Terakhir, pada set validasi mini KITTI yang kecil, hasil deteksi 3D (bukan BEV) untuk kelas mobil pada PointRCNN yang dicat justru sedikit menurun, kemungkinan akibat ukuran set validasi yang terlalu kecil untuk kesimpulan yang stabil.

## Kaitan dengan Bab Lain

PointPainting mewarisi tiga detektor LiDAR yang dibahas pada bab 087 (VoxelNet), bab 088 (PointPillars), dan bab 089 (PointRCNN) sebagai basis yang diperkaya, tanpa mengubah arsitekturnya. Metode ini juga menjawab keterbatasan pendekatan fusi level-fitur yang dibahas pada bab 091 (MV3D), bab 092 (AVOD), dan bab 090 (Frustum PointNets): ketiganya mengikat fusi pada arsitektur tertentu, sedangkan PointPainting memindahkan fusi ke level data sehingga lepas dari arsitektur detektor. Bab 094 ([3D-CVF](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md)) mengambil arah berbeda pada masalah yang sama — fusi kamera-LiDAR — dengan menggabungkan fitur pada level tersembunyi jaringan dan bobot adaptif antar-sensor, sehingga kedua bab dapat dibaca berdampingan sebagai dua strategi fusi yang berlawanan filosofi: fusi pada data mentah versus fusi pada fitur. Bab 095 ([Pseudo-LiDAR](./095%20-%202019%20-%20Pseudo-LiDAR%20-%20Deteksi%203D.md)) juga menyuntikkan informasi kamera ke jalur deteksi berbasis titik, tetapi dengan cara berbeda: mengubah citra kedalaman menjadi *point cloud* semu, bukan mengecat titik LiDAR asli dengan skor semantik.

## Poin untuk Sitasi

Kutip dengan kunci `vora2020pointpainting`. Ringkasan yang aman dikutip: "PointPainting memproyeksikan skor segmentasi semantik citra ke titik LiDAR sebelum diproses detektor 3D standar, menaikkan mAP PointPillars, VoxelNet, dan PointRCNN pada KITTI, serta mencapai hasil terbaik papan peringkat KITTI BEV untuk PointRCNN yang dicat pada saat publikasi." Angka mAP KITTI validasi (73,78→76,27 untuk PointPillars; 71,83→73,55 untuk VoxelNet; 72,42→75,80 untuk PointRCNN), hasil uji KITTI (66,92→69,86), dan hasil nuScenes (40,1→46,4 mAP; 55,0→58,1 NDS) diambil dari pembacaan versi HTML naskah (ar5iv); disarankan verifikasi ulang ke tabel asli PDF/CVF sebelum dikutip dalam karya formal, khususnya rincian per-kelas dan per-tingkat kesulitan yang tidak tercakup penuh di ringkasan ini.
