# Robot-assisted Neural Radiance fields for plot-level cotton crop 3D reconstruction and yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jiang2026robot` |
| Judul asli | Robot-assisted Neural Radiance fields for plot-level cotton crop 3D reconstruction and yield estimation |
| Penulis | Jiang, Lizhi; Chee, Peng W.; Li, Changying; Fu, Longsheng |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [jiang2026robot.pdf](../pdf/jiang2026robot.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.112063

## Gambaran Umum

Makalah ini (*Computers and Electronics in Agriculture* 252, 2026, 112063) mengusulkan alur kerja berbasis *Neural Radiance Fields* (NeRF) untuk merekonstruksi tanaman kapas tingkat petak (*plot-level*) dalam 3D, menghitung buah kapas (*boll*), dan memperkirakan hasil. Citra RGB diambil di lahan pemuliaan kapas di Tifton, Georgia, Amerika Serikat, pada 25 Oktober 2024, memakai robot darat MARS berkamera banyak dan, sebagai pembanding, ponsel genggam. Lahan terdiri atas 160 petak dengan 32 genotipe; kapas telah didefoliasi satu minggu sebelum pengambilan data dan kepadatan tanamnya rendah.

Hasil utama: konfigurasi lima kamera Lumix pada robot memberi rekonstruksi terbaik (PSNR 17,2100 dB, SSIM 0,4883, LPIPS 0,5435). Pada 26 petak yang sama yang dipotret dengan kedua metode, galat persentase absolut rerata (MAPE) jumlah buah adalah 5,43% (data Lumix) dan 5,29% (data ponsel), sedangkan MAPE bobot buah per petak 8,78% (Lumix) dan 9,77% (ponsel). Regresi jumlah buah terprediksi terhadap hitungan sebenarnya pada data Lumix menghasilkan R² 0,95, dan regresi bobot menghasilkan R² 0,89.

Penyatuan identitas buah dari banyak pandang dilakukan di ruang 3D: masker 2D buah dari semua citra diproyeksikan melalui medan semantik NeRF (FruitNeRF) ke awan titik buah, lalu titik-titik dikelompokkan dengan HDBSCAN dan jumlah klaster menjadi jumlah buah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Jumlah buah kapas merupakan indikator hasil yang penting dalam pemuliaan, tetapi penghitungannya masih bergantung pada pengambilan sampel manual di lapangan yang lambat, melelahkan, dan rentan galat manusia. Buah kapas tersebar dalam ruang 3D pada kanopi yang rapat dan tertutup sebagian, sehingga citra 2D bersifat bergantung pada sudut pandang, dan hitungan dari satu citra terganggu oleh oklusi dan buah yang saling tumpang tindih. Citra pesawat tanpa awak (UAV) umumnya hanya menampilkan pandangan atas dan melewatkan struktur samping dan di bawah kanopi.

Masalah kedua adalah kebutuhan anotasi titik 3D yang sangat padat untuk melatih segmentasi awan titik pada kanopi petak, ditambah langkanya data awan titik petak kapas. Pemindai LiDAR darat mahal dan tidak memberi warna, sedangkan kamera RGB-D beresolusi rendah sehingga detail halus hilang. Penulis menyatakan bahwa integrasi NeRF dengan segmentasi 3D pada kapas tingkat petak belum banyak dieksplorasi.

## Ide Utama

Gagasan utamanya adalah memindahkan informasi semantik dari ruang 2D ke 3D tanpa anotasi 3D. Masker 2D buah dihasilkan model segmentasi pada setiap citra, lalu NeRF dilatih bersama masker itu sehingga tiap titik 3D memiliki label "buah" atau "latar". Titik-titik berlabel buah diekspor sebagai awan titik dan dikelompokkan untuk memperoleh instans buah. Karena semua citra dari berbagai kamera dan sudut berbagi satu representasi 3D, buah yang tampak pada banyak citra jatuh pada lokasi 3D yang sama dan terhitung sekali.

Anotasi 2D disederhanakan dengan alur semiotomatis: detektor YOLOv11x menghasilkan kotak, kotak itu menjadi isyarat (*prompt*) bagi *Segment Anything Model* (SAM), dan masker yang salah diperbaiki manual.

## Cara Kerja Langkah demi Langkah

```
 Video multi-kamera -> ~90 bingkai/kamera -> COLMAP (pose kamera)
        |                                          |
 YOLOv11x segmentasi -> masker 2D buah             |
        |                                          v
        +----------> FruitNeRF (Nerfacto + medan semantik)
                                  |
                      awan titik buah -> HDBSCAN -> jumlah buah
```

### 1. Akuisisi data

Robot MARS membawa sepuluh kamera yang dipasang kira-kira merata pada rangka kanopi: lima Lumix DMC-G7 (3840 x 2160) dan lima Fuji X-A10 (1920 x 1080), seluruhnya merekam video 30 FPS dalam mode otomatis. Batang penopang berjarak sekitar 2,48 m dan batang kamera berada pada ketinggian sekitar 1,97 m. Robot dikemudikan manual dengan kecepatan sekitar 0,15 sampai 0,2 m/s; satu petak dipindai sekitar 40 detik, dan 39 petak dipindai dengan cara ini. Ponsel (iPhone 11, 3840 x 2160, 30 FPS) dipasang pada penstabil genggam dengan lensa sudut lebar, satu petak dipindai sekitar 130 detik melalui dua lintasan pandangan atas dan orbit samping pada dua ketinggian, dan 41 petak dipindai. Sebanyak 26 petak yang sama dipotret oleh kedua metode dan dipakai untuk menilai akurasi hitungan; petak lainnya dipakai untuk melatih model segmentasi 2D. Pengambilan data dengan robot dilakukan pukul 16.00 sampai 18.00 dan dengan ponsel pukul 11.00 sampai 14.00. Data diambil dari baris pertama, kedua, dan ketujuh.

### 2. Rekonstruksi NeRF

Bingkai diekstraksi dari video dan diubah ke 1920 x 1080: sekitar 90 bingkai per video kamera robot dan 500 bingkai dari video ponsel, dengan tumpang tindih antarbingkai yang diperkirakan lebih dari 90% (perkiraan dari kecepatan, laju bingkai, dan cakupan citra, bukan dari registrasi citra). COLMAP memperkirakan parameter kamera. Model Nerfacto di Nerfstudio dilatih 30.000 iterasi dengan 1024 sinar per iterasi, optimizer Rectified Adam, dan laju belajar 0,0005.

### 3. Segmentasi 2D buah

Detektor YOLOv11x dilatih pada data tahun 2022 (pandangan atas; 606 citra latih dan 260 citra validasi), SAM menghasilkan masker, lalu model segmentasi YOLOv11x dilatih pada data 2022 dan disetel halus pada data 2024 (85 citra latih, 25 validasi, 15 uji). Pelatihan memakai resolusi 1280 x 1280, ukuran batch 8, 300 epoch. Penulis menaksir waktu anotasi per citra berkurang sedikitnya 50% (taksiran kasar).

### 4. FruitNeRF dan pengelompokan

Medan semantik berupa MLP tiga lapis dengan 128 neuron tersembunyi ditambahkan pada medan densitas dan warna. Awan titik buah diekspor (3000 sinar per batch, 6000 titik per sisi kotak batas), dibersihkan dengan penyaringan tetangga, dan dipotong manual per petak. HDBSCAN lalu menentukan klaster; parameter `min_cluster_size` dan `min_samples` dioptimalkan melalui percobaan berulang: 9 dan 2 untuk data ponsel, 19 dan 2 untuk data Lumix. Perlu dicatat bahwa parameter dioptimalkan berdasarkan MAPE terhadap hitungan sebenarnya pada data yang sama dengan yang dilaporkan.

### 5. Metrik

Kualitas citra dinilai dengan variansi Laplacian (ketajaman), PSNR, SSIM, dan LPIPS; akurasi hitungan dengan RMSE, MAE, dan MAPE, dengan selang kepercayaan 95% dari *bootstrap* 10.000 iterasi pada tingkat petak.

## Eksperimen dan Hasil

Kualitas rekonstruksi dirata-ratakan pada sepuluh petak representatif (Tabel 4):

| Konfigurasi kamera | PSNR (dB) | SSIM | LPIPS (lebih rendah lebih baik) |
|---|---|---|---|
| 10 kamera (5 Lumix + 5 Fuji) | 14,5190 | 0,3766 | 0,6915 |
| 5 Lumix | 17,2100 | 0,4883 | 0,5435 |
| 5 Fuji | 14,6100 | 0,3186 | 0,6314 |
| Ponsel | 16,2105 | 0,3435 | 0,4909 |

Skor ketajaman (Tabel 3): Lumix 1151, Fuji 521, iPhone 1967. Segmentasi 2D YOLOv11x pada data 2024 (Tabel 5): data uji P 0,860, R 0,820, mAP50 0,874, mAP50-95 0,610; data validasi P 0,801, R 0,765, mAP50 0,833, mAP50-95 0,566.

Akurasi hitungan dan hasil (Tabel 6, selang kepercayaan 95% dalam kurung):

| Target | Sumber | MAE | RMSE | MAPE |
|---|---|---|---|---|
| Jumlah buah | Ponsel | 21,42 buah (14,54 sampai 28,65) | 28,25 buah | 5,29% (3,62 sampai 7,08) |
| Jumlah buah | Lumix | 21,88 buah (15,69 sampai 28,81) | 27,76 buah | 5,43% (4,08 sampai 6,80) |
| Hasil (bobot) | Ponsel | 148,22 g (93,89 sampai 195,50) | 192,12 g | 9,77% (5,75 sampai 13,70) |
| Hasil (bobot) | Lumix | 147,96 g (92,07 sampai 197,85 g) | 190,06 g | 8,78% (5,43 sampai 12,31) |

Acuan hitungan adalah jumlah buah yang dihitung manual (*ground truth*), dan acuan hasil adalah bobot buah per petak yang ditimbang. Untuk perbandingan, penulis mengutip MAPE 8,92% pada studi 2D terdahulu (Sun dkk., 2019) pada data yang berbeda. Konfigurasi sepuluh kamera campuran memiliki PSNR 2,691 dB lebih rendah, SSIM 0,1117 lebih rendah, dan LPIPS 0,2006 lebih tinggi dibanding Lumix. Penulis menyimpulkan bahwa konsistensi citra antarpandang lebih penting daripada jumlah kamera. Hanya data lima Lumix yang dipakai untuk menghitung buah dari data robot. Makalah tidak memuat pembanding hitungan 2D plot-level; penulis berargumen bahwa pembanding 2D yang adil memerlukan penjahitan citra atau asosiasi buah lintas pandang yang sulit di lapangan.

## Kelebihan dan Keterbatasan

Kelebihan: hitungan diverifikasi terhadap hitungan manual dan bobot yang ditimbang, dengan selang kepercayaan *bootstrap*; alur kerja tidak memerlukan anotasi awan titik 3D dan hanya memakai RGB; ketidakkonsistenan sensor (kamera campuran) dianalisis; dan dataset anotasi 2D disediakan lewat tautan figshare, sedangkan data lainnya tersedia atas permintaan.

Keterbatasan yang dinyatakan penulis: percobaan dilakukan pada kondisi pasca-defoliasi dengan kepadatan tanam rendah yang kurang menantang dibanding kanopi komersial tertutup; perbandingan kamera tidak terkendali karena waktu, iluminasi, dan lintasan berbeda; lima kamera Lumix hanya memberi pandangan samping dan atas sehingga awan titik tidak lengkap; HDBSCAN kadang menggabungkan dua buah yang berdekatan sehingga hitungan sedikit kurang; kebutuhan komputasi NeRF tinggi dan belum sesuai untuk penggunaan waktu nyata; robot dikemudikan manual; dan pembanding 2D tidak dibuat.

Menurut pembacaan ringkasan ini: (a) jumlah petak yang dinilai kecil (26 petak) dan parameter HDBSCAN dipilih dari MAPE pada petak yang sama, sehingga akurasi mungkin optimistis; (b) tidak ada pembagian terpisah untuk menyetel parameter dan menguji hitungan; (c) tidak ada hitungan per kelas, sehingga hasilnya tidak langsung menunjukkan kinerja pada inventaris per kategori; (d) ketergantungan pada pose kamera COLMAP dan pada pelatihan NeRF per petak membuat biaya per sisi tinggi; (e) kinerja pada buah yang tidak terbuka dan kanopi rapat tidak diuji.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari banyak pandang dan banyak kamera pada satu petak. Mekanismenya adalah rekonstruksi 3D: pose kamera dari COLMAP, medan semantik NeRF yang memuat label buah, ekspor awan titik buah, dan pengelompokan densitas (HDBSCAN) sebagai penentu identitas buah unik. Identitas tidak dicocokkan secara eksplisit antarcitra; ia muncul dari lokasi 3D yang sama. Hitungan tidak dilaporkan per kelas (hanya satu kelas "buah kapas"). Acuan hitungnya adalah hitung manual buah per petak (dan bobot yang ditimbang untuk hasil), bukan anotasi citra.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah konsep memetakan masker 2D dari semua sisi ke satu representasi 3D lalu menghitung klaster, serta temuan bahwa konsistensi sensor dan cakupan sudut mempengaruhi kualitas awan titik. Kendalanya: pohon sawit jauh lebih besar daripada petak kapas, jumlah pandang per pohon sawit dibatasi 4 sampai 8 sisi, dan penggabungan dua buah yang berdekatan oleh klaster (Gambar 14) akan memengaruhi hitungan per kelas. Makalah tidak menguji atribut kelas seperti kematangan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `jiang2026robot`.

Jiang dkk. (2026) merekonstruksi petak kapas pasca-defoliasi dalam 3D dengan NeRF dari citra RGB yang diambil robot darat berkamera banyak (dan ponsel sebagai pembanding), memproyeksikan masker 2D buah dengan FruitNeRF ke awan titik buah, dan mengelompokkannya dengan HDBSCAN. Pada 26 petak yang dibandingkan dengan hitungan manual, MAPE jumlah buah adalah 5,43% untuk data lima kamera Lumix dan 5,29% untuk data ponsel, dan MAPE bobot buah 8,78% dan 9,77%. Hasil ini berlaku untuk kanopi berkepadatan rendah pasca-defoliasi dan satu kelas buah.

Catatan verifikasi data: angka kualitas rekonstruksi berasal dari Tabel 4, ketajaman dari Tabel 3, metrik segmentasi dari Tabel 5, serta MAE, RMSE, MAPE, dan selang kepercayaan dari Tabel 6. R² 0,95 (jumlah buah, Lumix) dan R² 0,89 (bobot, Lumix) berasal dari seksi 3.3 (Gambar 10b dan 11b). Jumlah petak (160 total; 39 dengan robot; 41 dengan ponsel; 26 identik) berasal dari seksi 2.1; jumlah petak yang dipakai pada Tabel 6 secara eksplisit tidak disebut selain 26 petak identik tersebut, sehingga dianggap oleh ringkasan ini sebagai jumlah evaluasi tetapi tidak dinyatakan secara langsung. Kualitas rekonstruksi dirata-ratakan pada sepuluh petak representatif. Selisih rekonstruksi sepuluh kamera dilaporkan penulis di seksi 3.1. Data tersedia atas permintaan, sehingga angka tidak dapat diverifikasi ulang dari data. Teks makalah berbahasa Inggris dan terbaca baik; Tabel 4 dan 6 terbaca utuh dari ekstraksi.
