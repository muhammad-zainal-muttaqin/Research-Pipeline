# PineSORT: A Simple Online Real-Time Tracking Framework for Drone Videos in Agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xieli2025pinesort` |
| Judul asli | PineSORT: A Simple Online Real-Time Tracking Framework for Drone Videos in Agriculture |
| Penulis | Xie-Li, Danny; Fallas-Moya, Fabian |
| Tahun | 2025 |
| Venue | IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pineapple |

## Tautan Akses
- PDF: [xieli2025pinesort.pdf](../pdf/xieli2025pinesort.pdf)
- DOI resmi: https://doi.org/10.1109/cvprw67362.2025.00012

## Gambaran Umum
PineSORT adalah pelacak multi-objek (*multi-object tracking*, MOT) berbasis SORT untuk video drone di perkebunan nanas, dengan tujuan akhir estimasi hasil panen. Pelacak ini menangani laju bingkai rendah, pola yang berulang, penampilan buah yang serupa, dan gerak kamera drone. Tiga komponen utamanya adalah kompensasi gerak kamera berbasis ORB (*Oriented FAST and Rotated BRIEF*), asosiasi tiga tahap, dan pengelolaan tumpang tindih (*overlap management*). Makalah juga menyebut biaya arah gerak (*motion direction cost*) sebagai bagian dari pendekatan.

Data berupa 10 video dari perkebunan nanas Upala Agricola (Kosta Rika), direkam dengan drone DJI Mavic 3 pada resolusi 1920×1080, dari sudut tegak (90 derajat) dan miring (45 derajat). Detektor YOLOv11n dilatih dengan validasi silang lima lipatan (*5-fold cross-validation*). PineSORT dibandingkan dengan SORT, ByteTrack, DeepOCSORT, StrongSORT, BoTSORT, AgriSORT, HybridSORT, OCSORT, dan SFSORT.

Hasilnya, PineSORT memperoleh nilai ISP-IDF1 (metrik baru yang dirancang penulis) terbaik, dengan perbedaan terhadap BoTSORT yang signifikan secara statistik (uji Dunn, p = 0,0244). Pada pelatihan dan evaluasi dengan data tegak, PineSORT mencatat 131 pergantian identitas (*identity switch*, IDSW) dan BoTSORT 728. Makalah tidak melaporkan hitungan buah akhir atau galat penghitungan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Nanas, seperti banyak produk pertanian, tampak sangat mirip antarbuah dan tersusun berpola berulang, sehingga pelacak mudah mengganti identitas. Daun dapat menutupi buah, kotak deteksi dapat ganda untuk satu buah, dan sebaran nanas yang jarang meninggalkan ruang kosong yang luas. Gerak drone mengubah posisi, skala, dan perspektif objek dari bingkai ke bingkai, dan laju bingkai yang rendah menghasilkan perpindahan yang besar antarbingkai.

Penulis menyatakan bahwa penghitungan yang akurat bergantung pada identitas yang konsisten, sehingga IDSW perlu ditekan. Metode pelacakan pertanian yang ada, menurut penulis, belum memberikan ketepatan berbasis drone untuk estimasi hasil.

## Ide Utama
Pelacak mengasumsikan objek umumnya diam, berukuran relatif konsisten, dan berpenampilan serupa, sehingga isyarat penampilan (*ReID*) tidak diandalkan. Gerak kamera diperkirakan dari kecocokan titik fitur ORB antara bingkai $t-1$ dan $t$, lalu transformasi afin yang dihasilkan dipakai untuk mengoreksi keadaan filter Kalman sebelum asosiasi. Selain itu, asosiasi berlangsung dalam tiga tahap dan deteksi yang tumpang tindih dengan lintasan yang ada tidak dijadikan lintasan baru.

## Cara Kerja Langkah demi Langkah

```
  Bingkai t -> estimasi gerak kamera (ORB, t-1 ke t) -> koreksi Kalman
     -> asosiasi 1 (deteksi skor tinggi, IoU)
     -> asosiasi 2 (deteksi skor rendah, IoU, ambang lebih kecil)
     -> asosiasi 3 (sisa, DIoU, objek parsial)
     -> manajemen lintasan + pengelolaan tumpang tindih (IoU)
```

### 1. Akuisisi data
Sepuluh video direkam dengan DJI Mavic 3 pada resolusi 1920×1080 dari sudut tegak (90 derajat) dan miring (45 derajat), berdurasi 7 sampai 35 detik (183 sampai 882 bingkai per video). Anotasi dibuat dengan Label Studio dan diekspor ke format MOT pada 25 bingkai per detik. Jumlah nanas atau jumlah kotak anotasi tidak dilaporkan pada teks. Kultivar tidak dilaporkan.

### 2. Kompensasi gerak kamera dengan ORB
FAST mendeteksi titik kunci, BRIEF menghitung deskriptor biner, dan pencocokan memakai *brute-force matcher*. Matriks transformasi afin $A$ berukuran $2 \times 3$ (rotasi, skala, geseran, dan translasi $t_x$, $t_y$) dihitung dengan RANSAC pada OpenCV. Koordinat keadaan Kalman setiap lintasan digeser dengan translasi $(t_x, t_y)$. Pada eksperimen, ORB dibandingkan dengan SIFT dan aliran optik (*optical flow*, Shi-Tomasi dengan Lucas-Kanade).

### 3. Asosiasi tiga tahap
Tahap pertama mengasosiasikan lintasan dengan deteksi berkeyakinan tinggi memakai IoU dengan ambang tertentu. Tahap kedua memakai deteksi berkeyakinan rendah dengan ambang IoU yang lebih kecil. Tahap ketiga mengasosiasikan deteksi dan lintasan yang tersisa memakai *Distance IoU* (DIoU), yang memperhitungkan jarak pusat dan berguna untuk objek parsial yang sedang keluar bingkai. Penulis menyatakan memakai ambang 0,30 dan 0,10 secara sembarang (*arbitrary*); pemetaan ambang pada tiap tahap terbaca tidak jelas pada teks ekstraksi.

### 4. Pengelolaan tumpang tindih
Saat deteksi yang tidak tercocokkan akan dijadikan lintasan baru, IoU kotak itu dengan kotak lintasan yang ada dihitung. Bila melebihi ambang, deteksi redundan dibuang agar tidak menimbulkan pergantian identitas. Nilai ambang ditentukan secara empiris dan tidak disebut angkanya pada teks.

### 5. Metrik dan pelatihan
Evaluasi memakai TrackEval dengan MOTA, IDF1, HOTA, AssA, IDSW, MT, ML, PT, IDP, dan IDR. Penulis memperkenalkan ISP-IDF1 = IDF1 × (1 − (IDSW − min(IDSW)) / (max(IDSW) − min(IDSW)))$^k$ dengan $k = 4$. Detektor YOLOv11n dilatih dengan satu video untuk pelatihan dan sisanya untuk evaluasi, pada orientasi tegak, miring, dan gabungan.

## Eksperimen dan Hasil
Perbandingan kompensasi gerak kamera (Tabel 1, lima lipatan, rerata) menunjukkan ORB dan SIFT setara dan jauh lebih baik daripada aliran optik.

| Teknik | IDF1 | HOTA | AssA | IDSW total | ISP-IDF1 |
|---|---|---|---|---|---|
| ORB | 0,836 | 0,636 | 0,712 | 131 | 0,630 |
| Aliran optik | 0,813 | 0,621 | 0,687 | 451 | 0,400 |
| SIFT | 0,835 | 0,636 | 0,712 | 129 | 0,634 |

Perbandingan pelacak (Tabel 2, cuplikan: PineSORT dan BoTSORT, yaitu pelacak dasar terbaik menurut penulis; angka rerata lipatan kecuali IDSW yang berupa total):

| Evaluasi / pelatihan | Pelacak | HOTA | IDF1 | AssA | IDSW | ISP-IDF1 |
|---|---|---|---|---|---|---|
| Tegak / gabungan | PineSORT | 0,669 | 0,858 | 0,735 | 218 | 0,818 |
| Tegak / gabungan | BoTSORT | 0,624 | 0,811 | 0,682 | 795 | 0,686 |
| Tegak / tegak | PineSORT | 0,636 | 0,836 | 0,712 | 131 | 0,812 |
| Tegak / tegak | BoTSORT | 0,590 | 0,781 | 0,663 | 728 | 0,671 |
| Miring / gabungan | PineSORT | 0,587 | 0,784 | 0,651 | 491 | 0,706 |
| Miring / gabungan | BoTSORT | 0,576 | 0,768 | 0,643 | 1.079 | 0,610 |

Hasil sebagian pada Tabel 2 menunjukkan PineSORT tidak selalu unggul. Pada pelatihan tegak yang dievaluasi pada data miring, PineSORT mencatat IDF1 0,507 dan BoTSORT 0,522 (dibaca dari tabel). Uji Kruskal-Wallis atas ISP-IDF1 menghasilkan p < 2,2 × 10^-16, dan uji lanjutan Dunn antara BoTSORT dan PineSORT menghasilkan p = 0,0244. Analisis penulis atas pelacak lain: AgriSORT memiliki IDSW tertinggi, SFSORT banyak berganti identitas karena tidak memakai filter Kalman, StrongSORT sering berganti identitas karena objek homogen, dan HybridSORT dan OCSORT tidak berbeda secara statistik.

Kinerja terbaik muncul bila pelatihan memakai gabungan data tegak dan miring, dan pada pelatihan serta evaluasi dengan data tegak. Pelatihan pada satu orientasi dan evaluasi pada orientasi lain menghasilkan kinerja buruk.

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: tangguh terhadap perpindahan besar akibat laju bingkai rendah, IDSW jauh lebih sedikit daripada pelacak lain pada sebagian besar konfigurasi, dan evaluasi memakai uji statistik nonparametrik. Kompensasi ORB tidak bergantung pada asumsi gerak kecil seperti pada aliran optik.

Keterbatasan yang dinyatakan penulis: generalisasi antar-orientasi kamera lemah (pelatihan tegak dievaluasi miring, dan sebaliknya, memberi hasil buruk), dan pekerjaan lanjutan diarahkan pada skalabilitas serta lingkungan yang lebih sulit.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Dataset hanya 10 video dari satu perkebunan, dan lipatan validasi silang dipisahkan per video yang berasal dari area yang sama. Detektor dilatih dengan satu video per lipatan. Metrik ISP-IDF1 adalah rancangan penulis sendiri, bergantung pada nilai minimum dan maksimum IDSW antar-konfigurasi sehingga tidak sebanding antar-makalah. Makalah tidak melaporkan hitungan buah akhir atau galatnya terhadap acuan lapangan, padahal estimasi hasil menjadi tujuan yang dinyatakan. Pelacakan hanya berlangsung dalam satu video dan dalam satu arah gerak drone.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai satu video drone dengan pelacakan berbasis deteksi, dengan kompensasi gerak kamera untuk mempertahankan identitas antarbingkai. Identitas hanya dijaga dalam satu video dengan gerak kamera yang kira-kira satu arah. Pencocokan antar-video, antar-pandang yang berbeda sudut, atau antar-sisi tidak dilakukan; video tegak dan miring dievaluasi secara terpisah. Hitungan tidak dilaporkan per kelas, karena hanya satu kelas objek (nanas) yang dilacak. Acuan evaluasi adalah anotasi MOT pada bingkai video, bukan panen atau hitung manual di lapangan, dan jumlah buah akhir tidak dilaporkan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan bahwa pada objek diam yang serupa, kompensasi gerak kamera dan asosiasi berbasis posisi lebih berguna daripada isyarat penampilan (menurut makalah, StrongSORT yang bergantung penampilan justru sering berganti identitas), serta penekanan pada IDSW sebagai ukuran yang relevan terhadap hitungan. Namun, mekanisme ini bekerja dalam urutan bingkai yang kontinu dan tidak menyelesaikan penyatuan identitas antar-sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `xieli2025pinesort`.

Xie-Li dan Fallas-Moya mengusulkan PineSORT, pelacak multi-objek untuk video drone di perkebunan nanas yang memadukan kompensasi gerak kamera berbasis ORB, asosiasi tiga tahap, dan pengelolaan tumpang tindih. Dengan validasi silang lima lipatan pada 10 video, PineSORT memperoleh ISP-IDF1 yang lebih tinggi daripada BoTSORT secara signifikan (p = 0,0244). Pada pelatihan dan evaluasi dengan data tegak, IDSW total adalah 131 untuk PineSORT dan 728 untuk BoTSORT.

Catatan verifikasi data: Angka kompensasi kamera bersumber dari Tabel 1 dan angka perbandingan pelacak dari Tabel 2 (seksi 5.2); nilai p dari seksi 5.2. Pada teks ekstraksi, simbol matematika (ambang, tanda kurang dari, sama dengan, eksponen) hilang sebagian, sehingga ambang asosiasi dan kebalikan ambang tahap kedua tidak dapat dipastikan; baris Tabel 2 dibaca dengan urutan kolom MOTA, HOTA, IDF1, AssA, IDP, IDR, PT, MT, ML, IDSW, ISP-IDF1, dan angka cuplikan di atas selaras dengan Tabel 1. Jumlah nanas, jumlah bingkai anotasi, dan hitungan akhir tidak dilaporkan. Makalah ini berukuran pendek (prosiding workshop), dan tabel pelacak ekstraksinya panjang tetapi utuh.
