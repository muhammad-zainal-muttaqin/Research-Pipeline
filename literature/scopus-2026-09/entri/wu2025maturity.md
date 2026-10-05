# Maturity detection and counting of blueberries in real orchards using a 1novel STF-YOLO model integrated with ByteTrack algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2025maturity` |
| Judul asli | Maturity detection and counting of blueberries in real orchards using a 1novel STF-YOLO model integrated with ByteTrack algorithm |
| Penulis | Wu, Na; Wu, Jie; Wang, Zhechen; Zhao, Yun; Xu, Xing; Wang, Yali; Skobelev, Petr; Mi, Yanan |
| Tahun | 2025 |
| Venue | Frontiers in Plant Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry, peach/nectarine, blueberry |

## Tautan Akses
- PDF: [wu2025maturity.pdf](../pdf/wu2025maturity.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2025.1682024

## Gambaran Umum
Makalah ini mengusulkan STF-YOLO, yaitu model deteksi berbasis YOLOv8n yang dimodifikasi untuk mendeteksi tiga tingkat kematangan blueberry (matang/biru, semi-matang/ungu, belum matang/hijau) di kebun nyata, dan menggabungkannya dengan pelacak ByteTrack untuk menghitung buah pada video. Model memakai empat modul baru: *Detail Situational Awareness Attention* (DSAA) pengganti blok C2f, *Adaptive Edge Fusion* (AEF), *Multi-scale Neck Structure* (MNS), dan *Shared Differential Convolution Head* (SDCH).

Data berupa 891 citra yang diekstraksi dari video blueberry yang direkam dengan iPhone 13 Pro (3840 x 2160 piksel) di kebun Shimen, Tongxiang, Zhejiang, Tiongkok, pada Mei sampai Juni 2024, dari jarak 80 sampai 100 cm. Pada set uji, STF-YOLO mencapai mAP50 79,7 % (YOLOv8n 76,2 %, selisih 3,5 poin) dan mAP50-95 52,5 % dengan 2,67 juta parameter dan 6,7 GFLOPs. Bersama ByteTrack, rerata akurasi hitungan (mPc) pada tiga video adalah 72,49 % untuk tiga kelas kematangan.

Uji lintas dataset melaporkan mAP50 pada MegaFruit sebesar 91,6 % (persik), 70,5 % (stroberi), dan 90,6 % (blueberry), serta 66,3 % pada PASCAL VOC2007. Makalah ini tergolong gabungan deteksi dengan atribut kematangan dan pencacahan video per kelas, dengan acuan hitungan manual saat perekaman video.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Panen blueberry di Tiongkok bergantung pada tenaga manual. Penulis menyebut dua masalah: kekurangan tenaga kerja pada musim puncak dengan jendela panen optimum 24 sampai 72 jam, dan kerusakan buah akibat penekanan manual sebesar 15 % sampai 20 % (merujuk Ali dkk., 2015). Perkiraan hasil panen saat ini bertumpu pada pengalaman petani sehingga subjektif dan galatnya besar, padahal keputusan tenaga kerja, kemasan, rantai dingin, dan penjualan dibuat berminggu-minggu sebelum panen.

Blueberry sulit dideteksi karena berukuran kecil, tumbuh bergerombol, dan warnanya mirip latar belakang (terutama buah hijau). Studi sebelumnya yang dirujuk pada umumnya memakai citra jarak dekat (20 sampai 50 cm di atas kanopi), yang tidak menangkap seluruh tanaman dan tidak cocok untuk robot panen lapangan. Penulis mengutip hasil terdahulu: MacEachern dkk. (2023) mAP50 79,79 % pada tiga tahap kematangan, Liu dkk. (2023) mAP50 78,3 %, dan Zhao dkk. (2024) dengan citra drone setinggi sekitar 5 m hanya meningkat dari 48,9 % ke 54,4 %. Penulis menyimpulkan bahwa deteksi dan penghitungan operasional memerlukan citra seluruh tanaman dari jarak yang membuat kejelasan buah berkurang.

## Ide Utama
Gagasan utama adalah merancang detektor ringan khusus objek kecil yang membedakan kematangan melalui isyarat warna dan tekstur halus, lalu menyambungkan hasil deteksi per bingkai dengan pelacak MOT sehingga buah yang sama tidak dihitung ulang pada bingkai berbeda. Hitungan dilaporkan terpisah untuk tiga kelas kematangan dan dibandingkan dengan hitungan manual yang dilakukan saat video direkam.

Kontribusi arsitektural adalah empat modul: DSAA menambah persepsi detail lewat *Convolutional Additive Token Mixer* dan *Convolutional Gated Linear Unit*; AEF memisahkan komponen frekuensi rendah dan tinggi untuk memperkuat tepi buah yang terhalang daun; MNS menambah modul *Context Guided Down-sampling* (CGDS) untuk konteks multiskala; SDCH berbagi konvolusi lintas P3, P4, dan P5 untuk mengurangi parameter.

## Cara Kerja Langkah demi Langkah

```
 Video blueberry --> bingkai --> STF-YOLO (3 kelas kematangan)
                                      |
                                      v
                    ByteTrack (asosiasi dua tahap) --> ID jejak per kelas
                                      |
                                      v
                    hitungan per kelas vs hitungan manual --> Pc, mPc
```

### 1. Akuisisi data
Video direkam pada Mei sampai Juni 2024 (musim pematangan) di kebun Shimen, Tongxiang, Provinsi Zhejiang, antara pukul 09.00 dan 17.00 dengan iPhone 13 Pro pada resolusi 3840 x 2160 piksel, kamera berjarak 80 sampai 100 cm dari tanaman. Dari video diekstraksi 891 citra, satu bingkai per pengambilan. Kultivar dan jumlah tanaman tidak dilaporkan.

### 2. Anotasi dan pembagian data
Citra dianotasi dengan LabelImg memakai kotak pembatas minimum, termasuk buah yang terhalang sebagian. Kematangan dinilai secara visual dari warna: matang (biru), semi-matang (ungu), belum matang (hijau). Setiap citra diperbesar sedikitnya 200 % dan semua label ditinjau dan dikoreksi secara independen. Pembagian acak: 623 latih (70 %), 134 validasi (15 %), 134 uji (15 %). Augmentasi (rotasi, derau Gauss, pembalikan, penskalaan) pada set latih dan validasi menghasilkan 3.115 citra latih dan 665 citra validasi; set uji berisi 134 citra. Citra diubah ukurannya dari 3840 x 2160 menjadi 640 x 640. Jumlah label (Tabel 1): latih 16.120 matang, 15.420 belum matang, 7.780 semi-matang; validasi 3.195, 3.025, dan 1.355; uji 702, 680, dan 291.

### 3. Arsitektur STF-YOLO
Pada pengaturan pelatihan, ukuran masukan 640 x 640, 150 epoch, ukuran *batch* 8, laju belajar 0,01, di komputer dengan AMD Ryzen 9 5900X, RTX 3090, dan RAM 128 GB. DSAA mengganti C2f dengan ekstraksi fitur dasar, CATM (perhatian Q, K, V dengan operasi spasial 3 x 3 dan operasi kanal), dan CGLU (gerbang sigmoid). AEF menjalankan dua jalur paralel: konvolusi awal dan pengumpulan rerata adaptif multiskala (misalnya 3 x 3, 6 x 6, 9 x 9, 12 x 12), lalu modul perhatian kontur menghitung komponen frekuensi tinggi sebagai selisih fitur dan rerata lokal 3 x 3 dan menambahkannya kembali ke fitur. MNS memakai modul CGDS; jumlah terbaik adalah tiga. SDCH memakai blok Conv, GroupNorm, dan SiLU, dilanjutkan dua lapis *Detail-Enhanced Convolution* bersama (gabungan konvolusi biasa dan konvolusi selisih pusat, sudut, horizontal, vertikal) untuk P3, P4, dan P5, lalu cabang regresi dan klasifikasi.

### 4. Pelacakan dan penghitungan
ByteTrack menautkan deteksi antarbingkai dengan asosiasi dua tahap (deteksi berkeyakinan tinggi lebih dahulu, lalu deteksi berkeyakinan rendah). Akurasi hitungan per kelas $P_c = (1 - |N_a - N_t|/N_t) \times 100\,\%$, dan $mP_c$ adalah rerata $P_c$ untuk biru, hijau, dan ungu, dengan $N_a$ hitungan otomatis dan $N_t$ hitungan sebenarnya. Hitungan sebenarnya diperoleh dengan menghitung buah secara manual pada tiap tahap pertumbuhan saat video dikumpulkan. Jumlah buah pada tiap video tidak dilaporkan dalam teks yang tersedia.

## Eksperimen dan Hasil
### Deteksi
Perbandingan dengan sembilan varian YOLO ringan (Tabel 2 makalah) pada set uji:

| Model | Precision (%) | Recall (%) | mAP50 (%) | mAP50-95 (%) | Param (M) | FLOPs (G) |
|---|---|---|---|---|---|---|
| YOLOv5n | 80,8 | 70,8 | 76,8 | 50,7 | 2,50 | 7,1 |
| YOLOv6n | 81,0 | 68,8 | 76,4 | 50,5 | 4,23 | 11,8 |
| YOLOv8n | 81,7 | 68,6 | 76,2 | 51,2 | 3,01 | 8,1 |
| YOLOv9t | 81,9 | 71,1 | 77,7 | 51,3 | 1,97 | 7,6 |
| YOLOv10n | 80,2 | 69,1 | 76,0 | 50,7 | 2,27 | 6,5 |
| YOLOv11n | 82,0 | 70,7 | 77,8 | 52,1 | 2,58 | 6,3 |
| YOLO-MIF | 81,6 | 69,1 | 77,2 | 51,6 | 3,01 | 8,1 |
| MAF-YOLO | 80,9 | 71,4 | 77,3 | 50,9 | 2,99 | 8,7 |
| YOLO-SDFM | 82,2 | 72,0 | 78,1 | 51,6 | 3,44 | 8,5 |
| STF-YOLO | 82,3 | 72,1 | 79,7 | 52,5 | 2,67 | 6,7 |

Per kelas, mAP50 STF-YOLO adalah 85,7 % (matang; YOLOv9t 86,3 % lebih tinggi), 81,4 % (semi-matang), dan 71,8 % (belum matang). Kelas belum matang (hijau) paling sulit karena kontras rendah terhadap daun.

Ablasi (Tabel 3, dari YOLOv8n 76,2 % mAP50): DSAA 77,2 %; AEF 77,9 %; MNS 76,8 %; SDCH 77,3 %; DSAA+AEF 78,2 %; DSAA+AEF+MNS 78,3 %; seluruh modul 79,7 % dengan 6,7 GFLOPs. Pengaturan jumlah CGDS (Tabel 7): mAP50 terbaik 79,7 % pada CGDS = 3 (2,67 M parameter, 6,7 GFLOPs), sedangkan CGDS = 0 sampai 5 berada pada kisaran 77,7 % sampai 79,7 %.

### Penghitungan video
Hasil ByteTrack dengan STF-YOLO pada tiga video (Tabel 4 makalah):

| Video | mPc (%) | Pc biru (%) | Pc ungu (%) | Pc hijau (%) |
|---|---|---|---|---|
| 1 | 69,07 | 73,74 | 72,55 | 60,92 |
| 2 | 74,94 | 86,07 | 79,17 | 59,60 |
| 3 | 73,45 | 76,71 | 71,43 | 72,22 |
| Semua | 72,49 | 78,84 | 74,38 | 64,24 |

Akurasi terendah ada pada kelas hijau, yang oleh penulis dikaitkan dengan kontras warna rendah terhadap latar; peningkatan pada Video 3 diduga karena latar lebih terang. Perbandingan pelacak: ByteTrack mPc rerata 72,49 %, OC-SORT 72,08 % (tertinggi pada Video 2 dengan 77,75 %), dan StrongSORT 40,31 %. Penulis menyatakan hitungan manual bisa lebih akurat daripada hasil otomatis ini tetapi tidak skalabel.

### Generalisasi dan oklusi
Pada MegaFruit (Tabel 5), STF-YOLO memperoleh 91,6 % (persik), 70,5 % (stroberi), dan 90,6 % (blueberry), dibandingkan YOLOv8n 90,8 %, 70,5 %, 90,2 %. Subset blueberry MegaFruit direkam pada jarak 20 sampai 30 cm sehingga lebih mudah. Pada PASCAL VOC2007 (Tabel 6), mAP50 66,3 % (YOLOv8n 66,2 %), precision 78,1 %, recall 50,9 %. Pada analisis oklusi (Tabel 8 bagian yang tersedia), tingkat lolos STF-YOLO dibanding YOLOv8: 82,35 % berbanding 63,72 % (oklusi ringan, < 50 %), 56,25 % berbanding 46,87 % (sedang, 50 % sampai 70 %), dan 32,26 % berbanding 22,58 % (berat, > 70 %).

## Kelebihan dan Keterbatasan
Kelebihan: model ringan (2,67 juta parameter, 6,7 GFLOPs); membedakan tiga tingkat kematangan sekaligus; citra diambil pada jarak 80 sampai 100 cm yang mencakup lebih banyak bagian tanaman daripada studi jarak dekat; hitungan video dilaporkan per kelas kematangan dan dibandingkan dengan hitungan manual; ada perbandingan pelacak (ByteTrack, OC-SORT, StrongSORT) dan uji lintas dataset.

Keterbatasan yang dinyatakan penulis: skala dan keragaman dataset terbatas; ketidakseimbangan kelas sekitar 2:2:1 (matang : belum matang : semi-matang) karena buah semi-matang berumur paling singkat; menyimpulkan jumlah buah total dalam ruang 3D dari citra 2D sulit; oklusi berat masih menjadi penyebab utama galat hitungan dan deteksi; akurasi hitungan rerata 72,49 % masih di bawah penghitungan manusia; konversi hitungan menjadi hasil panen bergantung pada pengambilan sampel dan penimbangan; deteksi gagal pada cahaya sangat redup; robustnya terhadap kultivar, tahap pertumbuhan, cuaca, dan cahaya perlu diuji. Pekerjaan lanjutan yang disebut mencakup geometri multi-pandang atau rekonstruksi 3D untuk mengatasi oklusi.

Menurut pembacaan ringkasan ini, kenaikan mAP50 sebesar 3,5 poin diperoleh dari satu set uji berisi 134 citra tanpa pengulangan seed atau interval kepercayaan, sehingga selisih antarmodel yang berbeda sekitar 1 sampai 2 poin belum tentu bermakna. Menurut pembacaan ringkasan ini, set uji berasal dari pembagian acak citra yang diekstraksi dari video yang sama sehingga bingkai latih dan uji berpotensi mirip. Menurut pembacaan ringkasan ini, jumlah buah acuan per video dan jumlah video tidak dirinci selain tiga video, sehingga akurasi hitungan sulit ditimbang. Menurut pembacaan ringkasan ini, $P_c$ memakai selisih mutlak antara hitungan otomatis dan sebenarnya sehingga galat berlawanan arah pada tingkat video tidak terlihat, dan ByteTrack hanya mengelola identitas dalam satu urutan video dari satu sisi tanaman.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan MOT (ByteTrack, *tracking-by-detection*), sehingga satu buah mendapat satu ID jejak dan dihitung sekali. Identitas dijaga dalam satu urutan video dari satu arah pandang kamera; tidak ada pencocokan lintas sisi tanaman dan tidak ada rekonstruksi 3D. Hitungan dilaporkan per kelas kematangan (biru, ungu, hijau) dengan $P_c$ per kelas dan rerata $mP_c$ 72,49 % (biru 78,84 %, ungu 74,38 %, hijau 64,24 %). Acuan hitungan adalah hitungan manual buah pada tiap tahap pertumbuhan saat video dikumpulkan, bukan hasil panen dan bukan anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pelaporan akurasi hitungan per kelas kematangan, bukti bahwa kelas dengan kontras rendah terhadap latar (hijau) paling sulit dihitung, dan penggunaan hitungan manual lapangan sebagai acuan. Mekanisme ByteTrack hanya berlaku untuk urutan bingkai berkesinambungan dan tidak menyelesaikan identitas lintas sisi pohon, yang oleh penulis sendiri diarahkan pada geometri multi-pandang di pekerjaan lanjutan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wu2025maturity`.

Ringkasan yang aman dikutip: Wu dkk. (2025) mengusulkan STF-YOLO, model berbasis YOLOv8n dengan modul DSAA, AEF, MNS, dan SDCH, untuk mendeteksi blueberry pada tiga tingkat kematangan di kebun nyata (891 citra, jarak 80 sampai 100 cm), dengan mAP50 79,7 % dan mAP50-95 52,5 % pada 134 citra uji. Dikombinasikan dengan ByteTrack pada tiga video, rerata akurasi hitungan terhadap hitungan manual adalah 72,49 % (biru 78,84 %, ungu 74,38 %, hijau 64,24 %); kelas hijau paling sulit karena kontras rendah terhadap daun, dan oklusi berat tetap menjadi sumber galat utama.

Catatan verifikasi data: Jumlah citra dan pembagian data berasal dari seksi 2.2 dan Tabel 1; hasil deteksi dari Tabel 2 dan seksi 3.2; ablasi dari Tabel 3; hitungan video dari Tabel 4 (seksi 3.4); hasil MegaFruit dan VOC2007 dari Tabel 5 dan Tabel 6; pengaturan CGDS dari Tabel 7; hasil oklusi dari seksi 4.4 dan Tabel 8, yang teks ekstraksinya terpotong sehingga hanya persentase dalam teks utama yang dipakai. Teks ekstraksi memuat satu ketidakkonsistenan kecil: seksi 3.3 menyebut SDCH mengurangi FLOPs 17,6 %, sedangkan kesimpulan menyebut pengurangan kompleksitas 17,28 % (8,1G ke 6,7G adalah sekitar 17,28 %, dihitung); angka mAP50-95 "hingga +1,3 %" pada ablasi MNS tidak dapat dicocokkan dengan Tabel 3. Perbandingan "3,5 % untuk recall dan mAP" cocok dengan selisih tabel (72,1 dikurangi 68,6 dan 79,7 dikurangi 76,2, dihitung). Kultivar blueberry, jumlah tanaman, jumlah video dan durasinya, serta jumlah buah acuan per video tidak dilaporkan dalam teks. Persamaan dan beberapa gambar tidak terbaca penuh dari ekstraksi; isi gambar tidak dapat diverifikasi dari teks.
