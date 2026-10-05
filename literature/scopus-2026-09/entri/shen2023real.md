# Real-time tracking and counting of grape clusters in the field based on channel pruning with YOLOv5s

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shen2023real` |
| Judul asli | Real-time tracking and counting of grape clusters in the field based on channel pruning with YOLOv5s |
| Penulis | Shen, Lei; Su, Jinya; He, Runtian; Song, Lijie; Huang, Rong; Fang, Yulin; Song, Yuyang; Su, Baofeng |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [shen2023real.pdf](../pdf/shen2023real.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107662

## Gambaran Umum

Makalah ini mengembangkan jalur pencacahan ringan dari ujung ke ujung untuk melacak dan menghitung tandan anggur anggur (*grape clusters*) dari video lapangan secara waktu-nyata. Detektornya adalah YOLOv5s yang dipangkas kanalnya (*channel pruning*) dan memakai *soft non-maximum suppression* (Soft-NMS), pelacaknya SORT (*Simple Online and Realtime Tracking*), dan penghitungannya memakai garis hitung (*counting line*) dengan dua mode arah gerak kendaraan. Objeknya adalah tandan anggur anggur Chardonnay di sebuah lahan budi daya di Distrik Yangling, Provinsi Shaanxi, Tiongkok.

Pemangkasan menurunkan jumlah parameter 79%, ukuran model 76%, dan FLOPs 58% dengan ukuran model akhir 3,4 MB. Pada himpunan uji citra, mAP mencapai 82,3% dan waktu inferensi rata-rata 6,1 ms per citra. Pada delapan video uji, akurasi hitung rata-rata 84,9%, koefisien korelasi dengan hitung manual 0,9905 (dinyatakan penulis sebagai R^2), dan kecepatan pemrosesan video hingga 50,4 bingkai per detik.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa estimasi hasil kebun anggur skala industri umumnya bersifat destruktif, padat karya, atau berupa pengambilan sampel kecil yang diekstrapolasi, sehingga keandalannya tidak terjamin. Penghitungan tandan di lapangan dibutuhkan untuk perencanaan logistik dan keputusan sebelum panen.

Dua masalah teknis disebut. Pertama, sebagian besar model deteksi buah berbasis pembelajaran mendalam berukuran besar dan hanya cocok untuk platform berkinerja tinggi, sehingga menyulitkan penerapan pada terminal mobil dan robot kebun. Kedua, tandan anggur memiliki variasi bentuk yang besar dibandingkan apel atau mangga sehingga pelacakan dan penghitungan dari video sulit. Penulis mengutip bahwa pelacakan buah pada penelitian terdahulu hilang akibat oklusi atau gerak mendadak platform sehingga terjadi penghitungan ganda, dan bahwa pendekatan multi-pandang atau rekonstruksi 3D dapat mengatasinya tetapi memakan waktu sehingga sulit untuk waktu-nyata.

## Ide Utama

Gagasan pokoknya adalah memisahkan beban komputasi dari deteksi dan mengurangi dampak pertukaran identitas (*ID switching*) pada hasil hitung. Detektor diperkecil dengan pemangkasan kanal hingga 3,4 MB, Soft-NMS memperbaiki deteksi tandan yang saling tumpang tindih, dan penghitungan dilakukan hanya ketika titik pusat kotak lintasan melintasi garis hitung, sehingga pertukaran identitas sebelum atau sesudah garis tidak memengaruhi hasil. Penulis menyatakan bahwa jumlah identitas yang diberikan pelacak biasanya lebih besar daripada jumlah sesungguhnya, dan garis hitung ini yang meredamnya.

## Cara Kerja Langkah demi Langkah

```
video -> YOLOv5s terpangkas (+ Soft-NMS) -> SORT (Kalman + Hungarian)
      -> garis hitung (2:3) -> hitung = N_m + N_f (satu dari dua mode arah)
```

### 1. Akuisisi data

Citra tandan Chardonnay dipotret dengan kamera digital SONY ILCE-5100L (3008 × 1668 piksel) pada Juli–September sebelum panen: 218 citra pada 2020 (jarak 0,5–1 m) dan 464 citra pada 2021 (jarak 1–1,5 m), sehingga total 682 citra dalam berbagai cuaca dan pencahayaan. Video dikumpulkan pada 2021 dengan kendaraan lapangan terkendali jarak jauh yang membawa kamera digital pada ketinggian 1,2 m, jarak horizontal sekitar 1,5 m dari tanaman, kecepatan sekitar 0,5–1 m/detik, 30 bingkai per detik, dengan arah gerak selatan–utara maupun sebaliknya. Terdapat delapan video (V1–V8) dengan panjang berbeda. Jarak antarbaris tanam sekitar 3 m. Jumlah tanaman tidak dilaporkan.

### 2. Anotasi dan augmentasi

Anotasi poligon dibuat di Labelme sehingga diperoleh 6.227 instans tandan; kotak pembatas dihitung otomatis dari poligon. Data dibagi 8:2 menjadi 544 pasangan latih dan 138 pasangan uji. Augmentasi kombinasi acak dilakukan empat kali (pembalikan, kecerahan, kabur gerak, kontras, derau Gaussian) sehingga himpunan latih menjadi 2.720 citra.

### 3. Detektor YOLOv5s dan pemangkasan kanal

YOLOv5s dilatih dengan transfer learning dari bobot COCO (masukan 640 × 640, laju belajar 0,01, *batch* 16, 200 epoch, SGD). Pemangkasan kanal memakai faktor skala $\gamma$ pada lapisan *batch normalization* dengan regularisasi L1 (penalti $\lambda = 0{,}002$) saat pelatihan jarang (*sparse training*), lalu kanal dengan $\gamma$ di bawah ambang dibuang. Laju pemangkasan 0,85; jumlah kanal turun dari 9.504 menjadi 3.578. Penyetelan halus berlangsung 100 epoch dengan laju belajar 0,02 dan *batch* 16. Soft-NMS memakai pembobot Gaussian untuk meredam, bukan menghapus, kotak yang tumpang tindih.

### 4. Pelacakan dengan SORT

Keadaan tandan dimodelkan sebagai vektor 8 dimensi $(u, v, r, h, \dot u, \dot v, \dot r, \dot h)$ dengan filter Kalman. Asosiasi antarbingkai memakai IoU antara kotak prediksi dan kotak deteksi sebagai matriks biaya, diselesaikan dengan algoritme Hungarian.

### 5. Penghitungan dengan garis hitung

Garis hitung dipasang pada posisi dengan rasio luas kiri:kanan sekitar 2:3. Pada mode gerak ke kiri, hitungan awal $N_0$ adalah jumlah deteksi di sisi kiri garis pada bingkai pertama; bingkai kedua hingga bingkai ke-$(T-1)$ menambahkan tandan yang melintas dari kanan ke kiri (menjadi $N_m$); hasil akhir adalah $N_m$ ditambah jumlah deteksi di sisi kanan garis pada bingkai terakhir ($N_{f1}$). Mode gerak ke kanan simetris. Mode ditentukan otomatis dari posisi relatif kotak antarbingkai. Akurasi hitung $P_c = (1 - |N_g - N_a|/N_g) \times 100\%$, dengan acuan $N_g$ dari hitung manual dua penghitung pada video.

Perangkat: Ubuntu 20.04, Intel Core i9-11900K, RAM 32 GB, NVIDIA RTX 3090 24 GB, Python 3.7, PyTorch 1.7.1.

## Eksperimen dan Hasil

### Detektor sebelum dan sesudah pemangkasan (Tabel 1)

| Metrik | YOLOv5s asli | Setelah pemangkasan | Setelah penyetelan halus | Penyetelan halus dengan Soft-NMS |
|---|---|---|---|---|
| Parameter | 7,0 × 10^6 | 1,5 × 10^6 | 1,5 × 10^6 | 1,5 × 10^6 |
| FLOPs (G) | 15,8 | 6,7 | 6,7 | 6,7 |
| Ukuran model (MB) | 14,4 | 3,3 | 3,4 | 3,4 |
| F1 (%) | 79,5 | 78,6 | 79,1 | 79,5 |
| mAP (%) | 82,5 | 81,7 | 82,1 | 82,3 |
| Waktu inferensi (s) | 6,8 × 10^-3 | 6,1 × 10^-3 | 6,1 × 10^-3 | 6,1 × 10^-3 |

### Perbandingan detektor (Tabel 2)

| Algoritme | P (%) | R (%) | F1 (%) | mAP (%) | Ukuran (MB) | Kecepatan (bingkai/detik) |
|---|---|---|---|---|---|---|
| YOLOv4 | 87,84 | 64,22 | 74,00 | 80,11 | 256,3 | 39,8 |
| YOLOv4-tiny | 83,68 | 59,43 | 69,00 | 72,87 | 23,6 | 236,3 |
| SSD 300 | 87,28 | 48,76 | 63,00 | 63,78 | 95,0 | 125,1 |
| EfficientDet-D1 | 86,28 | 69,01 | 77,00 | 81,19 | 26,9 | 25,6 |
| Metode penulis | 84,3 | 75,3 | 79,50 | 82,3 | 3,4 | 163,9 |

### Penghitungan pada delapan video

Akurasi hitung berkisar 75% hingga 92% dengan rerata 84,9% (Gambar 10, tidak terbaca dari teks); kecepatan rata-rata algoritme 43,1–50,4 bingkai per detik. V6 dan V7 lebih rendah (rerata 76,7%) dan video lain di atas 85%. Pada keseluruhan video, V6 mencapai akurasi 78,04% dan V7 75,47%. Pada 300 bingkai pertama, hitungan algoritme ($N_a$) dibanding hitungan manual ($N_g$) tercantum pada Tabel 3 (panjang video dalam bingkai: V1 1.027, V2 936, V3 1.469, V4 326, V5 726, V6 936, V7 731, V8 902):

| Video | $N_a$ pada bingkai 300 | $N_g$ pada bingkai 300 |
|---|---|---|
| V1 | 32 | 34 |
| V2 | 26 | 33 |
| V3 | 22 | 26 |
| V4 | 35 | 36 |
| V5 | 26 | 33 |
| V6 | 20 | 24 |
| V7 | 19 | 26 |
| V8 | 28 | 31 |

Penulis melaporkan galat relatif rerata 7,06% untuk lima bingkai pertama, galat maksimum tidak melebihi 17% pada segmen 300 bingkai, dan akurasi tertinggi 97,22% pada V4 untuk 300 bingkai pertama (menurut teks). Pada posisi garis 3:2 dan 1:1 selain 2:3, simpangan baku rerata hasil hitung sekitar 1,70 pada delapan video. Hasil V2 identik untuk ketiga posisi garis.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: model sangat kecil dengan akurasi mAP yang dipertahankan, pemrosesan melebihi 30 bingkai per detik pada delapan video, ketahanan terhadap pertukaran identitas lewat garis hitung, dan ketidakpekaan terhadap posisi garis.

Keterbatasan yang dinyatakan penulis: hanya tandan yang terlihat dari satu sisi baris tanaman yang dihitung, sedangkan tandan pada kedua sisi tanaman dapat terhitung ganda ketika kendaraan bergerak pada kedua sisi baris; rencana kerja lanjutan memakai kamera kedalaman untuk menolak hitungan ganda antarsisi. Guncangan video akibat perubahan kecepatan platform dapat menghilangkan lacakan. Kasus khusus: deteksi yang hilang terus-menerus di sekitar garis dapat membuat tandan melintas tanpa terhitung. Anotasi manual menimbulkan ketidakpastian dan oklusi ekstrem menghasilkan positif palsu.

Menurut pembacaan ringkasan ini: hanya delapan video dengan satu kebun, satu kultivar, dan satu platform yang dipakai, sehingga generalisasi terbatas. Dalam Tabel 3 hitungan algoritme pada bingkai 300 lebih rendah daripada hitungan manual pada semua delapan video, selaras dengan penghitungan kurang akibat deteksi yang terputus. Akurasi dihitung dari total per video tanpa pemisahan per kelas.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam satu video melalui pelacakan antarbingkai (SORT dengan Kalman dan Hungarian) yang dikombinasikan dengan penghitungan lintas garis, sehingga tiap lintasan yang melewati garis dihitung satu kali. Tidak ada pencocokan identitas antarsisi baris atau antarpandang; penulis secara eksplisit menyebut bahwa tandan pada sisi lain baris tanaman dapat terhitung ganda dan menjadikannya pekerjaan mendatang dengan kamera kedalaman.

Hitungan tidak dilaporkan per kelas; ada satu kelas (tandan) saja. Acuan hitungnya adalah hitung manual dari video oleh dua penghitung (bukan hasil panen dan bukan hitung langsung di lapangan). Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah aturan hitung lintas garis dua arah dengan inisialisasi dan penutupan yang mengatasi tandan di sisi garis pada bingkai pertama dan terakhir. Batas yang disebut penulis sendiri, yaitu tidak adanya identitas antarsisi, justru merupakan masalah inti untuk sawit multi-sisi sehingga makalah ini hanya menyelesaikan bagian dalam-satu-sisi.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `shen2023real`.

Shen dkk. mengembangkan jalur pelacakan dan penghitungan tandan anggur dari video lapangan dengan YOLOv5s terpangkas kanal (3,4 MB; mAP 82,3%; 6,1 ms per citra), Soft-NMS, SORT, dan garis hitung dengan dua mode arah gerak. Pada delapan video, akurasi hitung rata-rata 84,9% (kisaran 75%–92%), koefisien korelasi dengan hitung manual 0,9905, dan kecepatan hingga 50,4 bingkai per detik; penulis mencatat bahwa tandan pada sisi lain baris tanaman tidak ditangani dan dapat terhitung ganda.

Catatan verifikasi data: Angka detektor diambil dari Tabel 1 dan 2 dan Seksi 3.1–3.2; akurasi 84,9%, kisaran 75%–92%, rerata 76,7% untuk V6 dan V7, dan kecepatan 43,1–50,4 bingkai per detik dari Seksi 3.4; korelasi 0,9905 dari Seksi 4.2 (disebut sebagai $R^2$ pada Seksi 4.2 dan sebagai koefisien korelasi pada abstrak). Hitungan 300 bingkai dari Tabel 3, yang kolom bingkai lainnya tidak dikutip. Total hitungan per video penuh (Gambar 10) tidak terbaca dari teks. Teks memuat ketidakkonsistenan kecil: ukuran model terpangkas 3,3 MB (Seksi 3.1, kolom pemangkasan) dan 3,4 MB (abstrak dan setelah penyetelan halus); selisih kecepatan 124,1 bingkai/detik terhadap YOLOv4 sesuai dengan Tabel 2 (163,9 − 39,8). Asal dataset acuan 6.227 instans dirujuk pada makalah penulis sebelumnya. Jumlah tanaman tidak dilaporkan. Tabel dan lampiran suplemen (Gambar S1–S3, Tabel S1) tidak termasuk dalam teks.
