# Adapting SAM3 for 3D fruit counting with cross-view contrastive learning and Hough voting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2026adapting` |
| Judul asli | Adapting SAM3 for 3D fruit counting with cross-view contrastive learning and Hough voting |
| Penulis | Zhao, Kai; Kang, Chenchen; Rogiers, Suzy; Ghannoum, Oula; Guo, Yi |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, mango, sweet pepper, plum/apricot |

## Tautan Akses
- PDF: [zhao2026adapting.pdf](../pdf/zhao2026adapting.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.112325

## Gambaran Umum

Makalah ini mengusulkan SAM3-Adapt, kerangka kerja untuk pencacahan dan lokalisasi 3D buah pada kebun dan rumah kaca yang padat dan banyak oklusi. Kerangka ini menggabungkan model fondasi penglihatan SAM3 yang disesuaikan dengan *low-rank adaptation* (LoRA), representasi adegan *3D Gaussian Splatting* (3DGS), pembelajaran kontrastif lintas pandang dengan pembobotan ketidakpastian, dan pemungutan suara bergaya *Hough* (*Hough voting*) pada ruang Gaussian 3D, diikuti pengelompokan HDBSCAN untuk menghitung buah. Jumlah buah adalah jumlah klaster valid, dan pusat 3D tiap buah adalah rerata titik suara dalam klaster.

Data memakai tiga set publik: FruitNeRF (sintetis Blender dengan enam jenis buah dan tiga adegan nyata apel), Fuji-SfM (apel Fuji komersial, satu adegan, 1.455 buah beranotasi), dan BUP20 (paprika rumah kaca, RealSense D435i). Hasil utama: pada adegan sintetis, F1 plum 0,971 dan mangga 0,977 (FruitNeRF: 0,575 dan 0,816); pada Fuji-SfM, 1.450 buah terhitung dari 1.455; pada FruitNeRF nyata Tree03, 290 dari 291. Bobot LoRA dan pengaturan pascapemrosesan dari apel kebun dipakai tanpa diubah untuk paprika rumah kaca; hanya perintah teks (*prompt*) SAM3 diganti.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada kebun padat, buah yang berdekatan atau saling menutupi dapat tergabung menjadi satu daerah pada proyeksi 2D sehingga pencacahan 2D menghitung terlalu sedikit. Pendekatan berbasis detektor tunggal-pandang (misalnya keluarga YOLO) dan pelacakan video dinilai kurang tahan terhadap oklusi berat antarbuah. Struktur dari gerak (*Structure from Motion*, SfM) dapat menyelaraskan hasil deteksi lintas pandang. FruitNeRF mengurangi penghitungan ganda dengan segmentasi dan *volumetric rendering*, tetapi memakan komputasi dan waktu optimasi yang besar, serta bergantung pada pengelompokan dengan prior geometris khusus tanaman (templat awan titik buah, jari-jari rerata buah, batas atas jumlah buah per klaster).

Detektor kelas tertutup dan detektor kosakata terbuka berbasis kotak pembatas (misalnya Grounding DINO) memberi supervisi kasar yang tumpang tindih pada buah padat, sedangkan segmentasi 3DGS membutuhkan supervisi piksel yang konsisten antarpandang. SAM3 sendiri dilatih pada citra alami umum sehingga pada buah yang mirip warna dan tekstur sering menghasilkan masker yang menempel atau batasnya bergeser. Pelatihan dari awal mahal dan memerlukan anotasi besar.

## Ide Utama

Gagasan intinya adalah menghitung dan memisahkan buah di ruang 3D, bukan pada masker 2D. Setiap primitif Gaussian membawa fitur dan pergeseran 3D yang dapat dipelajari, sehingga primitif pada buah yang sama menghasilkan titik suara yang menyatu di pusat buah. Instance yang tumpang tindih pada gambar tetap terpisah di ruang 3D.

Konsistensi identitas lintas pandang dicapai tanpa pencocokan instance antarpandang, tanpa pelacakan objek, dan tanpa pembentukan pasangan positif lintas citra. Penulis menjelaskan bahwa setiap fitur Gaussian bersifat tingkat adegan dan bebas pandang, dibagi oleh semua pandang tempat primitif itu terlihat. Gradien kerugian kontrastif tiap pandang diakumulasi pada fitur yang sama, sehingga supervisi antarpandang terhubung melalui parameter bersama. Pencocokan Hungarian dengan buku kode objek dilakukan hanya di dalam satu pandang dan tidak melakukan pelacakan lintas pandang.

## Cara Kerja Langkah demi Langkah

```
 citra ──> SAM3+LoRA ──> masker 2D per citra ─┐
 citra ──> COLMAP ──> pose kamera ────────────┤
                                              v
          3DGS: warna + fitur 16-d + offset 3D per Gaussian
          kerugian: rekonstruksi + kontrastif + klaster + voting
                                              v
     pangkas primitif (sebaran lintas pandang, respons buku kode)
                                              v
           HDBSCAN pada titik suara ──> jumlah + pusat 3D buah
```

### 1. Data dan anotasi

Set FruitNeRF sintetis memuat enam jenis buah (apel, plum, lemon, pir, persik, mangga) dengan total 2.942 instance beranotasi dan koordinat 3D akurat, 300 bingkai per kategori pada 1024 × 1024. Set nyata FruitNeRF memuat 583 instance apel (Nikon D7100, 6000 × 4000, tiga adegan Tree01 sampai Tree03). Fuji-SfM memuat satu adegan dengan 1.455 instance (Sony Alpha 6000, 4000 × 3000). BUP20 memuat satu adegan paprika tanpa anotasi instance lengkap. Semua parameter kamera dikonversi ke format COLMAP. Untuk set nyata, anotasi dibuat semiotomatis: SAM3 memberi kandidat masker, lalu setiap citra dikoreksi manual dengan VGG Image Annotator (buang positif palsu, tambah buah terlewat, pisahkan instance menempel). Pada daerah padat, penulis memakai informasi multipandang dan struktur 3D; buah yang tidak dapat dibedakan sama sekali dikeluarkan dari acuan lokalisasi 3D.

### 2. Adaptasi SAM3 dengan LoRA

Dua matriks peringkat rendah disisipkan pada proyeksi Q, K, dan V di blok Transformer pengode citra, sedangkan dekoder masker tetap beku. Peringkat $r=8$ dipilih (2,95 juta parameter terlatih, sekitar 0,1% dari seluruh parameter SAM3). Pelatihan dua fase: fase pertama hanya modul LoRA, fase kedua membuka dua lapisan terakhir pengode. Kerugian segmentasi gabungan Focal dan Dice, AdamW, laju belajar $1 \times 10^{-4}$, *weight decay* 0,01, ukuran *batch* 4, 30 *epoch*, $\alpha=16$, dan *dropout* 0,1; GPU NVIDIA A6000 48 GB.

### 3. Pembelajaran kontrastif lintas pandang dengan ketidakpastian

Setiap Gaussian membawa fitur 16 dimensi yang dirender dengan $\alpha$-*blending*. Kerugian ProtoNCE dihitung per pandang terhadap prototipe instance dari masker SAM3. Bobot ketidakpastian per piksel membuang piksel dengan bobot di atas ambang $\tau=0{,}5$ dari supervisi kontrastif dan klaster. Analisis sensitivitas $\tau$ memberi F1 rerata tertinggi 0,977 pada 0,5 (Tabel 3).

### 4. Buku kode objek dan kerugian klaster

Buku kode 256 × 16 memetakan fitur piksel ke prototipe objek. Penugasan instance SAM3 ke kata kode dilakukan per pandang dengan algoritma Hungarian dan hanya dipakai sebagai target kerugian klaster.

### 5. Hough voting 3D dan pengelompokan

Tiap Gaussian memiliki pergeseran terbatas $\Delta p_i=\delta_{max}\tanh(\hat o_i)$ dengan $\delta_{max}=0{,}05\,d_{scene}$, diinisialisasi nol. Titik suara per piksel dirata-rata, diproyeksikan, dan dicocokkan dengan sentroid masker 2D. Setelah konvergensi, primitif dengan sebaran suara lintas pandang $\sigma_i$ di atas ambang tetap, atau respons buku kode rendah, dianggap latar dan dibuang. Ambang itu ditentukan sekali pada adegan sintetis dan tidak diubah per adegan. Titik tersisa diskalakan ke metrik Sim(3), lalu dikelompokkan dengan HDBSCAN (min_cluster_size 30, min_samples 10, alpha 1,0). Titik berlabel noise tidak dihitung.

### 6. Optimasi gabungan

Tujuan akhir: rekonstruksi + $\lambda_c$ kontrastif + $\lambda_v$ voting + $\lambda_n$ klaster, dengan $\lambda_c = 10^{-5}$, $\lambda_v = 10^{-6}$, $\lambda_n = 10^{-6}$, 30.000 iterasi 3DGS, dan model 3DGS dioptimasi ulang untuk tiap adegan.

## Eksperimen dan Hasil

Metrik penghitungan: presisi, *recall*, F1, dan *mean absolute error* (MAE). Untuk adegan sintetis ditambahkan galat pusat 3D (pencocokan Hungarian dengan ambang diameter rerata buah). Untuk segmentasi 3D dipakai IoU 3D (mIoU, mAcc, mAP, AP@0,25, AP@0,50). Pembanding utama adalah FruitNeRF (hasil rilisnya) dan, untuk segmentasi, Grounded-SAM2 dan SAM3 tanpa adaptasi.

Hitungan adegan sintetis (Tabel 5), format hitungan terdeteksi/acuan:

| Buah | FruitNeRF hitungan | FruitNeRF F1 | SAM3-Adapt hitungan | SAM3-Adapt F1 |
|---|---|---|---|---|
| Apel | 282/283 | 0,991 | 283/283 | 1,000 |
| Plum | 315/781 | 0,575 | 741/781 | 0,971 |
| Lemon | 326/326 | 0,982 | 323/326 | 0,974 |
| Pir | 229/250 | 0,956 | 243/250 | 0,986 |
| Persik | 148/152 | 0,987 | 147/152 | 0,980 |
| Mangga | 807/1150 | 0,816 | 1123/1150 | 0,977 |

Rerata galat hitungan absolut enam kategori adalah 13,67 buah (SAM3-Adapt) dan 139,17 buah (FruitNeRF). Galat pusat 3D berkisar 0,21 sampai 0,56 cm (SAM3-Adapt) dan 0,34 sampai 0,88 cm (FruitNeRF). Pada lemon, hitungan FruitNeRF sama dengan acuan, tetapi sekitar enam instance tetap salah cocok. Pada persik dan lemon, F1 FruitNeRF sedikit lebih tinggi daripada SAM3-Adapt.

Adegan nyata (Tabel 6):

| Adegan | FruitNeRF | SAM3-Adapt | Acuan |
|---|---|---|---|
| Tree01 | 173 | 175 | 179 |
| Tree02 | 112 | 112 | 113 |
| Tree03 | 264 | 290 | 291 |
| Fuji-SfM | 1.459 | 1.450 | 1.455 |
| BUP20 | 83 | 107 | tidak ada |

Ablasi pada plum dan mangga (Tabel 7), F1 rerata: baseline (SAM3 LoRA + 3DGS + DBSCAN) 0,827; + kontrastif 0,890; + kerugian klaster 0,923; + Hough voting (metode penuh) 0,974. Selisih penuh terhadap baseline adalah +0,147 (plum +0,190, mangga +0,104). Segmentasi 3D pada plum sintetis (Tabel 8): SAM3-Adapt mIoU 0,741, mAcc 0,823, mAP 0,581, AP@0,25 0,792, AP@0,50 0,562; FruitNeRF 0,498, 0,572, 0,341, 0,486, 0,273; Grounded-SAM2 0,382, 0,461, 0,218, 0,337, 0,142. Pada ablasi peringkat LoRA (Tabel 2), mIoU rerata 2D naik dari 0,561 (Grounded-SAM2) dan 0,606 (SAM3 tanpa adaptasi) menjadi 0,856 pada $r=8$.

Biaya komputasi pada adegan plum 300 bingkai (Tabel 4): SAM3-Adapt 2,4 jam *end-to-end*, FruitNeRF 3,3 jam, FruitNeRF++ 8,9 jam; kecepatan render sekitar 110 FPS untuk SAM3-Adapt (hanya pada rendering pandang baru) dan kurang dari 0,5 FPS untuk dua metode NeRF; memori GPU puncak 21 GB berbanding 24 GB. Pada adegan Fuji-SfM, COLMAP memakan hampir 4 jam (sekitar 45% dari seluruh alur). Penulis juga melaporkan kesalahan hitungan akhir dalam 2% saat voting dipakai pada tampilan kurva konvergensi (Gambar 11).

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: penghitungan dan pemisahan instance dilakukan di ruang 3D sehingga buah yang berimpit pada citra tetap terpisah; adaptasi LoRA hanya memperbarui sekitar 0,1% parameter; tidak ada prior bentuk atau ukuran buah sehingga pengaturan dapat dipindahkan lintas tanaman; dan identitas lintas pandang diperoleh tanpa pencocokan atau pelacakan eksplisit. Kode dan tautan dataset tersedia publik.

Keterbatasan yang dinyatakan penulis: evaluasi lokalisasi 3D hanya pada adegan sintetis karena set nyata tidak memiliki pusat 3D atau label instance yang andal; waktu proses besar (beberapa jam untuk pohon berukuran sedang, sekitar 4 jam hanya untuk COLMAP pada Fuji-SfM); setiap adegan membutuhkan model 3DGS yang dioptimasi terpisah sehingga sulit diskalakan ke ribuan pohon; asumsi adegan statis yang dapat dilanggar oleh angin, perubahan cahaya, dan pantulan; serta aplikasi pada tanaman merambat (anggur, kiwi) belum diuji.

Menurut pembacaan ringkasan ini, sebagian besar angka hitungan nyata berasal dari satu adegan per set (Fuji-SfM, BUP20) atau tiga adegan kecil, tanpa pengulangan atau variansi, dan hitungan BUP20 tidak memiliki acuan sehingga klaim transfer ke paprika hanya didukung kualitatif dan hitungan 107 versus 83 tanpa kebenaran dasar. Menurut pembacaan ringkasan ini, acuan nyata dibuat dengan bantuan keluaran SAM3 yang dikoreksi manual, sehingga dapat bias ke arah segmenter yang sama. Menurut pembacaan ringkasan ini, ambang $\sigma_{thr}$ ditentukan pada adegan sintetis tetapi nilainya tidak dicantumkan, dan ambang $\tau$ memberi hasil terbaik pada tiap kategori berbeda sehingga nilai F1 sintetis dipilih pada set yang sama dengan evaluasi.

## Kaitan dengan Tinjauan main6

Makalah ini secara langsung menangani buah yang terlihat dari banyak pandang. Mekanismenya adalah rekonstruksi 3D (3DGS dari pose COLMAP) dengan penggabungan identitas melalui fitur Gaussian bersama dan pemungutan suara pusat 3D, lalu pengelompokan titik suara menjadi satu klaster per buah. Tidak ada pencocokan eksplisit antarcitra atau pelacakan objek; pencocokan Hungarian hanya terjadi dalam satu pandang. Kesesuaian lintas pandang bergantung pada pose kamera yang akurat, adegan statis, dan optimasi 3DGS per adegan.

Hitungan tidak dilaporkan per kelas dalam arti atribut seperti kematangan: enam jenis buah dihitung per jenis, bukan per kelas dalam satu jenis. Acuan hitungan adalah anotasi citra (sintetis dari Blender, nyata dari anotasi semiotomatis yang dikoreksi manual dengan bantuan informasi multipandang), bukan panen atau hitung lapangan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menghitung pusat 3D tandan alih-alih menghitung dari masker 2D, pengelompokan tanpa prior ukuran, dan penyesuaian segmenter dengan LoRA. Tantangannya: pohon kelapa sawit tinggi dengan pandang yang terbatas (4 sampai 8 sisi) dan jumlah citra jauh lebih sedikit daripada ratusan bingkai per adegan di sini, adegan dinamis akibat angin, serta ketiadaan mekanisme per kelas kematangan, sehingga kelas harus ditambahkan sebagai atribut klaster.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zhao2026adapting`.

Ringkasan yang aman dikutip: Zhao dkk. (2026) mengusulkan SAM3-Adapt, yang menyesuaikan SAM3 dengan LoRA dan menggabungkannya dengan *3D Gaussian Splatting*, pembelajaran kontrastif lintas pandang berbobot ketidakpastian, dan *Hough voting* 3D yang diikuti pengelompokan HDBSCAN untuk menghitung dan melokalisasi buah. Pada adegan sintetis FruitNeRF, F1 mencapai 0,971 (plum) dan 0,977 (mangga), dibandingkan 0,575 dan 0,816 pada FruitNeRF. Pada adegan nyata, hitungan dekat acuan (misalnya 1.450 dari 1.455 pada Fuji-SfM dan 290 dari 291 pada Tree03), dan bobot serta pengaturan pascapemrosesan dipindahkan dari apel ke paprika rumah kaca dengan hanya mengganti perintah teks.

Catatan verifikasi data: Angka sintetis dibaca dari Tabel 5, hitungan nyata dari Tabel 6, ablasi dari Tabel 7, segmentasi 3D dari Tabel 8, ablasi peringkat LoRA dari Tabel 2, sensitivitas ambang dari Tabel 3, dan biaya komputasi dari Tabel 4 serta Bagian 3.1. Rerata galat 13,67 dan 139,17 buah serta peningkatan relatif 68,9% pada plum tertulis di teks Bagian 3.2.1. Gambar (termasuk Gambar 8 dan 11) tidak terbaca dalam teks. Nilai ambang $\sigma_{thr}$ dan bobot kerugian terkait tidak dicantumkan lengkap. Hitungan BUP20 tidak memiliki acuan. Teks ekstraksi terbaca baik; makalah diterbitkan di *Computers and Electronics in Agriculture* 255 (2026) 112325 (diterima 13 Agustus 2026).
