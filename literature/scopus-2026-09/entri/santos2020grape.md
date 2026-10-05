# Grape detection, segmentation, and tracking using deep neural networks and three-dimensional association

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `santos2020grape` |
| Judul asli | Grape detection, segmentation, and tracking using deep neural networks and three-dimensional association |
| Penulis | Santos, Thiago T.; de Souza, Leonardo L.; dos Santos, Andreza A.; Avila, Sandra |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [santos2020grape.pdf](../pdf/santos2020grape.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2020.105247

## Gambaran Umum
Makalah ini menyajikan alur kerja untuk mendeteksi, menyegmentasi, dan melacak tandan anggur anggur-vinifera (*wine grape*) pada citra kebun dengan sistem pagar rambat (*trellis*). Komponen utamanya adalah dataset publik Embrapa Wine Grape Instance Segmentation Dataset (WGISD) berisi 300 citra RGB dengan 4.432 tandan dari lima varietas, perangkat anotasi masker interaktif berbasis pencocokan graf, evaluasi Mask R-CNN terhadap YOLOv2 dan YOLOv3, serta asosiasi tiga dimensi (*3D association*) berbasis *Structure-from-Motion* (SfM) untuk melacak tandan yang sama pada urutan bingkai video dan menghindari penghitungan ganda.

Pada himpunan uji bermasker (27 citra, 408 tandan), Mask R-CNN dengan *backbone* ResNet-101 mencapai F1 0,915 untuk segmentasi instans pada IoU 0,3 dan 0,847 pada IoU 0,5. Pada deteksi kotak untuk seluruh himpunan uji (58 citra, 850 tandan beranotasi kotak menurut Tabel 2, sedangkan teks seksi 3.4 menyebut 837 tandan), Mask R-CNN memperoleh F1 0,890 pada IoU 0,3 dan 0,840 pada IoU 0,5, lebih tinggi daripada YOLOv2 (0,802 dan 0,652) dan YOLOv3 (0,718 dan 0,579). Segmentasi semantik pada tingkat piksel memberikan F1 0,889.

Evaluasi pelacakan memakai satu urutan video lapangan (500 bingkai kunci pertama), tetapi makalah hanya menampilkannya secara kualitatif; jumlah lintasan hasil algoritma dan hitungan acuan tidak dilaporkan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan buah pada tingkat individual diperlukan untuk prediksi hasil, pertanian presisi, dan pemanenan otomatis. Kotak pembatas (*bounding box*) pada deteksi objek kurang sesuai untuk tandan anggur karena bentuk, ukuran, warna, dan kekompakan tandan sangat bervariasi, bahkan dalam satu varietas. Segmentasi semantik (klasifikasi piksel buah dan bukan buah) juga tidak memadai bila terjadi oklusi parah antar-tandan. Segmentasi instans, yaitu deteksi objek yang digabung dengan atribusi piksel ke tiap objek, dipilih agar bentuk tandan dan oklusi oleh daun, ranting, batang, maupun tandan lain dapat ditangani.

Karya terdahulu pada anggur berfokus pada penghitungan butir (*berry*) dengan fitur buatan tangan, yang menghindari masalah segmentasi tandan. Detektor berbasis Faster R-CNN dari penelitian lain menghasilkan F1 hingga 0,90 untuk apel dan mangga, tetapi deteksi pada citra tunggal tidak dapat mencegah penghitungan ganda bila kamera bergerak. Penulis menyebut Liu dkk. (2019) sebagai acuan untuk integrasi pelacakan dan SfM pada kebun mangga, dan mengikuti gagasan serupa untuk anggur.

## Ide Utama
Gagasan pokoknya adalah memisahkan dua tahap. Tahap persepsi memakai jaringan saraf untuk menghasilkan masker instans tiap tandan pada setiap bingkai. Tahap integrasi spasial memakai titik 3D dari SfM sebagai bukti bahwa dua masker pada bingkai berbeda mengamati objek dunia nyata yang sama: bila satu titik 3D terproyeksi ke dalam masker pada bingkai $i$ dan masker pada bingkai $i'$, kedua masker dihubungkan oleh sebuah sisi graf berbobot jumlah titik penghubung. Jumlah lintasan terpanjang yang terpisah pada graf itu menjadi estimasi jumlah tandan pada seluruh urutan bingkai.

Penulis juga menyatakan bahwa bukti dari banyak bingkai dapat mengonfirmasi deteksi dan menyaring positif palsu dari tahap persepsi.

## Cara Kerja Langkah demi Langkah
```
 Video / citra -> [Mask R-CNN] -> masker instans per bingkai
        |                               |
        +-> [COLMAP SfM] -> titik 3D    |
                  |                     v
                  +----> graf G: simpul = instans, sisi = titik 3D bersama
                                |
                  saring sisi (satu masuk, satu keluar; bobot terbesar)
                                |
                  jalur terpanjang (DFS), buang jalur < 5 sisi
                                |
                  jumlah jalur = estimasi jumlah tandan
```

### 1. Akuisisi data (WGISD)
Dataset berisi 300 citra RGB yang menampilkan 4.432 tandan dari lima varietas: Chardonnay (65 citra, 840 tandan), Cabernet Franc (65, 1.069), Cabernet Sauvignon (57, 643), Sauvignon Blanc (65, 1.317), dan Syrah (48, 563). Citra diambil di satu kebun anggur (*winery*) dengan sistem pagar rambat dan pemangkasan ganda yang menghasilkan kanopi berkerapatan rendah; tanpa pemangkasan atau perlakuan khusus untuk dataset. Citra empat varietas diambil pada 27 April 2018 dan Syrah pada tanggal yang ditulis 2017-04-27 pada Tabel 1. Kamera berada pada pose frontal dengan sumbu utama kurang lebih tegak lurus kawat pagar rambat. Rincian kamera dan lokasi dipindahkan ke Lampiran A dan tidak terbaca pada teks yang tersedia. Masker biner tersedia untuk 2.020 tandan dari 4.432. Dataset berlisensi CC BY-NC 4.0.

### 2. Anotasi masker interaktif
Anotasi poligon dinilai sangat melelahkan, termasuk dengan prediksi simpul Polygon-RNN++. Penulis membuat perangkat berbasis segmentasi citra interaktif melalui pencocokan graf relasional beratribut (Noma dkk., 2012). Citra pertama kali dipecah berlebih dengan algoritma *watershed* menjadi graf; pengguna menggambar coretan (*scribble*) untuk tandan dan latar atau objek penghalang di depan; label dirambatkan lewat pencocokan graf, dan langkah ini dapat diulang. Kotak pembatas yang sudah ada dipakai sebagai masukan.

### 3. Pelatihan jaringan
Citra dipilih acak dengan pembagian sekitar 80-20%, menghasilkan 242 citra latih/validasi (3.582 tandan berkotak) dan 58 citra uji (850 tandan berkotak) menurut Tabel 2. Untuk segmentasi instans, 110 citra bermasker tersedia: 88 citra latih (1.307 tandan) dan 22 citra validasi (305 tandan); himpunan uji bermasker berisi 27 citra dengan 408 tandan. Augmentasi memakai pustaka imgaug (*Gaussian blur*, normalisasi kontras, derau Gaussian aditif, dan *pixel dropout*), 20 augmentasi acak per citra, sehingga citra latih menjadi 1.848. Mask R-CNN memakai implementasi Matterport (Keras/TensorFlow), diinisialisasi dengan bobot COCO tanpa lapisan yang dibekukan, masukan 1024x1024 dengan *zero padding*, dan dibandingkan antara ResNet-101 dan ResNet-50 (ResNet-101 terbaik). YOLOv2 dan YOLOv3 dilatih memakai Darknet dengan bobot awal ImageNet dan satu kelas. Perangkat keras: satu GPU NVIDIA TITAN Xp 12 GB; Mask R-CNN dilatih sekitar 10 jam (100 epoch), YOLO empat hari.

### 4. Metrik evaluasi
Presisi (P), *recall* (R), dan F1 dihitung untuk tiga masalah: segmentasi semantik (piksel; 27 citra, 408 tandan), deteksi objek (kotak, IoU, seluruh himpunan uji), dan segmentasi instans (masker, IoU, 27 citra bermasker). Rerata presisi (AP) mengikuti definisi Pascal VOC. Ambang keyakinan 0,9 dipakai untuk kelas anggur; pengujian 0,5, 0,7, 0,9, dan 0,95 menunjukkan variasi F1 di bawah 0,005.

### 5. Asosiasi 3D untuk pelacakan
Graf berarah $G = (V, E)$ dibangun dengan simpul $u_{i,j}$ (instans ke-$j$ pada bingkai ke-$i$). Sisi dari $u_{i,j}$ ke $v_{i',j'}$ ($i < i'$) dibuat bila ada titik 3D $X_k$ dari COLMAP yang terproyeksi ke kedua masker; bobot sisi adalah jumlah titik penghubung. Karena oklusi dapat membuat banyak sisi bertemu pada satu simpul, setiap simpul dibatasi satu sisi masuk dan satu sisi keluar dengan mempertahankan sisi berbobot maksimum; strategi ini diharapkan mendukung tandan penghalang, sedangkan tandan terhalang dilacak oleh sisi yang melompati banyak bingkai ($i' > i+1$). Lintasan terpanjang dicari dengan *depth-first search*; lintasan yang lebih pendek dari 5 sisi dibuang untuk menyingkirkan positif palsu. Jumlah lintasan merupakan estimasi jumlah tandan pada seluruh urutan.

## Eksperimen dan Hasil
Hasil segmentasi instans Mask R-CNN (ResNet-101) pada himpunan uji bermasker (Tabel 3, ambang keyakinan 0,9):

| IoU | AP | P instans | R instans | F1 |
|---|---|---|---|---|
| 0,3 | 0,855 | 0,938 | 0,892 | 0,915 |
| 0,5 | 0,743 | 0,869 | 0,826 | 0,847 |
| 0,7 | 0,478 | 0,696 | 0,662 | 0,678 |
| 0,9 | 0,008 | 0,070 | 0,066 | 0,068 |

Pada segmentasi semantik, seluruh piksel uji menghasilkan P 0,920, R 0,860, dan F1 0,889 (Tabel 4); F1 per citra berkisar sekitar 0,82 sampai 0,93 tanpa varietas yang menonjol. Penulis menyimpulkan bahwa penetapan butir ke tandan, bukan pengenalan butir, adalah faktor utama yang menurunkan IoU. Anotasi acuan sendiri rawan galat pada gerombol tandan besar.

Deteksi objek pada seluruh himpunan uji (Tabel 5, F1):

| IoU | Mask R-CNN | YOLOv2 | YOLOv3 |
|---|---|---|---|
| 0,3 | 0,890 | 0,802 | 0,718 |
| 0,5 | 0,840 | 0,652 | 0,579 |
| 0,7 | 0,684 | 0,350 | 0,323 |
| 0,8 | 0,511 | 0,154 | 0,164 |

AP pada IoU 0,5 berturut-turut 0,719, 0,478, dan 0,394. Penulis mencatat bahwa YOLO hanya dilatih pada himpunan bermasker yang sama, padahal anotasi kotak lebih cepat dibuat dan dataset kotak dapat lebih besar.

Evaluasi pelacakan memakai video yang direkam kamera ponsel Full HD (1.920x1.080) saat kendaraan servis bergerak sepanjang baris tanaman; 500 bingkai kunci MPEG pertama dipakai. Bingkai kunci dipilih karena artefak kompresi lebih sedikit, jumlah bingkai berkurang, dan tumpang tindih tetap cukup untuk SfM. Hasil ditampilkan secara kualitatif (Gambar 6 dan 10 serta video daring). Jumlah lintasan terhitung, hitungan manual acuan, dan galat hitung tidak dilaporkan. Uji generalisasi kualitatif pada empat citra daring menunjukkan sebagian besar tandan terdeteksi tanpa penyetelan, dengan positif palsu pada daun bertekstur dan pemecahan tandan pada tahap perkembangan awal.

## Kelebihan dan Keterbatasan
Kelebihan: dataset publik dengan masker, perbandingan langsung segmentasi instans dan deteksi kotak pada data yang sama, bukti bahwa Mask R-CNN lebih tahan pada IoU tinggi, serta mekanisme asosiasi 3D yang sederhana dan hanya memerlukan kamera RGB biasa.

Keterbatasan yang dinyatakan penulis: segmentasi tandan sulit bahkan bagi anotator karena oklusi dan tidak adanya masukan 3D atau anotasi di lapangan; proses SfM padat komputasi sehingga SLAM (misalnya ORB-SLAM atau SVO) diusulkan sebagai alternatif waktu nyata; pendekatan Liu dkk. yang memakai buah sebagai penanda tidak jelas perilakunya bila tidak ada buah pada suatu segmen video; generalisasi pada pose kamera dan tahap perkembangan lain baru dinilai secara kualitatif.

Menurut pembacaan ringkasan ini, evaluasi pelacakan tidak memiliki hitungan acuan sehingga klaim penghindaran penghitungan ganda belum terukur secara kuantitatif. Himpunan uji bermasker kecil (27 citra), pengulangan dengan beberapa *seed* tidak dilaporkan, dan hanya satu urutan video dari satu baris tanaman yang diuji. Penentuan batas lintasan minimum 5 sisi tidak diuji sensitivitasnya. Data satu kebun anggur saja sehingga generalisasi antarkebun belum dapat disimpulkan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme pelacakan berbasis asosiasi 3D (C1): masker instans pada bingkai berurutan dihubungkan melalui titik 3D SfM bersama, sisi dipangkas menjadi satu masuk dan satu keluar, dan jalur terpanjang dihitung sebagai satu tandan. Mekanisme ini bergantung pada urutan bingkai dengan tumpang tindih yang cukup untuk SfM. Hitungan dilaporkan bukan per kelas: hanya satu kelas (tandan anggur) yang dievaluasi, meskipun varietas dan warna berbeda. Acuan metrik deteksi dan segmentasi adalah anotasi citra (kotak dan masker); acuan hitungan tandan pada video tidak dilaporkan, dan tidak ada hitung manual di lapangan maupun hasil panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan graf asosiasi yang diberi bobot bukti geometri bersama dan penyaringan lintasan pendek untuk menekan positif palsu. Pada pohon sawit dengan beberapa sisi, urutan bingkai kontinu tidak selalu tersedia dan tandan terlihat dari sisi yang tidak tumpang tindih, sehingga makalah ini tidak menjawab bagaimana identitas dipertahankan antar-sisi tanpa bukti titik 3D bersama. Makalah juga tidak menyediakan koreksi per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `santos2020grape`.

Santos dkk. memperkenalkan dataset WGISD (300 citra, 4.432 tandan, lima varietas anggur), perangkat anotasi masker interaktif, dan pipeline yang menggabungkan Mask R-CNN dengan asosiasi 3D berbasis SfM untuk melacak tandan anggur pada urutan video dan menghindari penghitungan ganda. Mask R-CNN mencapai F1 0,915 (IoU 0,3) dan 0,847 (IoU 0,5) untuk segmentasi instans pada 408 tandan uji, serta lebih unggul daripada YOLOv2 dan YOLOv3 pada deteksi kotak. Hasil pelacakan ditampilkan secara kualitatif tanpa hitungan acuan.

Catatan verifikasi data: angka segmentasi instans ada pada Tabel 3, segmentasi semantik pada Tabel 4, deteksi kotak pada Tabel 5, jumlah citra dan tandan pada Tabel 1 dan 2, serta pengaturan pelatihan pada seksi 3.3. Ekstraksi teks memecah tabel menjadi satu angka per baris; kolom dicocokkan menurut urutan dan konsisten dengan teks (misalnya F1 0,915 pada IoU 0,3). Terdapat ketidaksesuaian kecil: teks seksi 3.4 menyebut 837 tandan uji, sedangkan Tabel 2 menjumlahkan 850. Rincian kamera dan lokasi (Lampiran A) serta bagian akhir daftar pustaka tidak terbaca pada teks. Jumlah lintasan, hitungan acuan, dan galat pelacakan pada video tidak dapat diverifikasi karena tidak dilaporkan. Teks ini adalah naskah penulis yang diterima (versi arXiv v3).
