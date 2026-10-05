# Object detection and tracking on UAV RGB videos for early extraction of grape phenotypic traits

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arizasentis2023object` |
| Judul asli | Object detection and tracking on UAV RGB videos for early extraction of grape phenotypic traits |
| Penulis | Ariza-Sent\'\is, Mar; Baja, Hilmy; V\'elez, Sergio; Valente, Jo\~ao |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [arizasentis2023object.pdf](../pdf/arizasentis2023object.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108051

## Gambaran Umum
Makalah ini memakai pelacakan dan segmentasi multi-objek (*multi-object tracking and segmentation*, MOTS) pada video RGB dari pesawat nirawak (*unmanned aerial vehicle*, UAV) untuk mendeteksi, melacak, dan mengukur tandan serta buah anggur (*berry*) putih pada tahap perkembangan awal. Algoritma PointTrack dipakai untuk mendeteksi dan melacak tandan, sedangkan dua algoritma segmentasi instans (*instance segmentation*), YOLACT dan Spatial Embeddings, dibandingkan untuk mendeteksi buah di dalam tandan. Keluaran akhirnya adalah deskriptor *International Organisation of Vine and Wine* (OIV) untuk panjang, lebar, dan bentuk tandan (kode 202, 203, 208) serta buah (kode 220, 221, 223).

Data direkam pada 28 Juni 2021 di kebun anggur komersial kultivar Loureiro (Vitis vinifera) seluas 1,06 ha di Tomiño, Spanyol, tanpa pemangkasan daun, sehingga video mengandung oklusi daun. Terdapat 40 video (7,49 gigabita); 29 urutan video dianotasi untuk tandan (679 bingkai teranotasi) dan 33 citra dengan 4.905 masker buah dianotasi untuk deteksi buah.

Deteksi tandan terbaik (model Rec128_800 + 3200) mencapai MODSP 93,85, tetapi metrik pelacakan bernilai negatif (sMOTSA −9,51 dan MOTSA −8,17) sehingga penulis menyatakan hasil pelacakan tidak memadai dengan 679 bingkai latih. Pada penghitungan buah per tandan, Spatial Embeddings mencapai akurasi rerata 79,5% dan YOLACT 44,6%, terhadap anotasi buah yang tampak.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Jumlah dan dimensi tandan serta buah pada tahap awal perkembangan memberi petunjuk hasil panen, tetapi pencacahan dan pengukuran biasanya dilakukan manual sehingga lambat dan padat karya. Studi terdahulu umumnya memakai tandan merah, kebun dengan pemangkasan daun, kendaraan darat, atau kamera genggam. UAV dengan kamera RGB dipandang sebagai alternatif murah dan hemat waktu.

Penulis menyoroti bahwa metode pelacakan buah dengan filter Kalman atau algoritma Hungarian umumnya tidak dapat dilatih ujung ke ujung (*end-to-end*), karena cabang pelacakan ditambahkan pada detektor. Mereka juga menyebut kurangnya dataset berbasis UAV; dataset anggur yang ada (misalnya WGISD, 300 citra dengan sekitar 4.000 tandan pada jarak sekitar 1 m) memiliki citra yang jernih dan dekat. Tantangan khusus di sini adalah tandan hijau berlatar vegetasi hijau yang homogen, cahaya matahari kuat, dan oklusi daun.

## Ide Utama
Gagasan utamanya adalah memakai kerangka MOTS sehingga satu pipeline menghasilkan masker piksel tiap tandan beserta identitas pelacakan, lalu mengukur sifat fenotipe dari masker itu. Tandan dideteksi dan dilacak terlebih dahulu, kemudian buah dideteksi hanya di dalam tandan terdeteksi untuk menghindari kesulitan mengaitkan buah dengan tandan yang saling bersentuhan.

Dimensi dalam piksel dikonversi ke sentimeter memakai lebar tiang kebun yang tetap (9 cm) pada tiap urutan video. Deskriptor OIV kemudian diturunkan dari dimensi dan rasio lebar pada bagian tandan. Dua cara pengukuran panjang dan lebar tandan dibandingkan: ukuran kotak masker dan rotasi masker menurut jarak terjauh.

## Cara Kerja Langkah demi Langkah

```
 video UAV --> anotasi (CVAT) --+--> PointTrack --> tandan (masker + ID)
                                |
                                +--> YOLACT / Spatial Embeddings --> buah
 masker --> ukuran piksel --> cm (lebar tiang 9 cm) --> deskriptor OIV
```

### 1. Akuisisi data
Platform adalah UAV DJI Matrice 210 dengan kamera DJI Zenmuse X5S (bingkai 4096 × 2160, 59,94 bingkai per detik), pada kecepatan terbang 0,7 m/s dan ketinggian 3 m di atas tanah, pada hari cerah dengan angin di bawah 0,5 m/s. Penerbangan mencakup empat baris (baris 4, 6, 7, dan 8) dengan jarak tanam 2,5 × 3 m; baris 5 tidak diterbangi karena banyak tanamannya terserang penyakit esca. Dataset tandan berisi 29 urutan video dengan 679 bingkai, dibagi sekitar 70/30 untuk latih dan uji. Dataset buah berisi 33 citra dengan 4.905 masker, juga dibagi sekitar 70/30. Penerbangan dilakukan manual sehingga skala tiap urutan berbeda.

### 2. Anotasi
Anotasi memakai CVAT dengan format MOTS untuk tandan (per piksel, tanpa tangkai) dan format COCO untuk buah. Tandan dianotasi bila tampak, termasuk saat ternaungi. Buah dianotasi hanya bila tampak dari depan; buah tertutup diabaikan dan buah tidak dilacak lintas bingkai.

### 3. PointTrack untuk tandan
Pelatihan dua tahap: model segmentasi instans (Spatial Embeddings) dan model PointTrack untuk asosiasi *embedding* instans. Spatial Embeddings memakai pengoptimal Adam dengan laju belajar 5×10⁻⁵ (penyetelan halus 5×10⁻⁶) dan bobot awal dari KITTI MOTS; ukuran *batch* 20. PointTrack dilatih dengan Adam, laju belajar 2×10⁻³, *batch* 64. Lima model dihasilkan dengan variasi ukuran potongan instans (persegi panjang atau kotak) dan jumlah epoch; model kelima memakai pemindahan pembelajaran (*transfer learning*) dari dataset apel APPLE MOTS. Metrik pelacakan adalah MOTSA dan sMOTSA, sedangkan metrik deteksi adalah MOTSP dan MODSP.

### 4. Deteksi buah
Empat model dilatih: dua YOLACT (YO_80000_original dan YO_80000_downsized, ukuran *batch* 2 dan 8) dan dua Spatial Embeddings (SE_1500 dan SE_2300, *batch* 32). Penilaian memakai mAP50 gaya COCO. Spatial Embeddings tidak menghasilkan kotak pembatas sehingga hanya metrik masker yang tersedia. Pelatihan YOLACT memerlukan sekitar 672 jam (26 hari) dan 437 jam (18 hari), sedangkan Spatial Embeddings sekitar 40 dan 80 jam.

### 5. Penilaian fenotipe
Panjang dan lebar tandan diperoleh dengan metode 1 (ukuran kotak masker, mengasumsikan tandan menghadap ke bawah) dan metode 2 (masker diputar agar sumbu terpanjang vertikal, lebar sebagai jarak terbesar tegak lurus). Bentuk tandan (OIV 208) dihitung dari rasio lebar atas dan bawah pada potongan ketiga dan keempat dari lima potongan: rasio di bawah 1,1 adalah tingkat 1, di atas 1,3 adalah tingkat 2, dan di antaranya tingkat 3. Bentuk buah (OIV 223) dikategorikan dari rasio panjang terhadap lebar: di bawah 0,95 tingkat 1, 0,95 sampai 1,05 tingkat 2, 1,05 sampai 1,25 tingkat 3, dan di atas 1,25 tingkat 4. Sesuai OIV, sepuluh tandan dan tiga puluh buah dinilai. Perangkat keras adalah dua GPU Nvidia RTX Titan 24 GB.

## Eksperimen dan Hasil
Pembanding pada tandan adalah lima konfigurasi PointTrack; pembanding pada buah adalah YOLACT dan Spatial Embeddings. Acuan fenotipe dan hitungan buah adalah pengukuran visual dan anotasi manual pada bingkai video teranotasi.

| Model PointTrack | sMOTSA | MOTSA | MOTSP | IDS | MODSP |
|---|---|---|---|---|---|
| Rec64_600 + 1200 | −14,37 | −7,61 | 65,18 | 80 | 81,60 |
| Rec128_800 + 3200 | −9,51 | −8,17 | 66,58 | 19 | 93,85 |
| Box80_800 + 2400 | −28,43 | −21,97 | 63,47 | 71 | 82,54 |
| Box160_1000 + 2400 | −75,78 | −66,42 | 64,75 | 129 | 80,08 |
| BoxApp128_200 + 1200 | −55,12 | −46,70 | 65,11 | 155 | 79,92 |

Model Rec128_800 + 3200 terbaik pada MODSP dan memiliki IDS paling sedikit (19). Model dengan pemindahan pembelajaran dari apel termasuk yang terburuk. Nilai pelacakan negatif dikaitkan penulis dengan deteksi positif palsu (misalnya daun terdeteksi sebagai tandan), bukan dengan pergantian ID.

| Model buah | mAP50 kotak | mAP50 masker |
|---|---|---|
| YO_80000_original | 0,68 | 0,41 |
| YO_80000_downsized | 0,02 | 0,01 |
| SE20_1500 | tidak tersedia | 1,82 |
| SE20_2300 | tidak tersedia | 2,42 |

Penulis menyebut mAP50 Spatial Embeddings 5,9 kali lebih tinggi daripada YOLACT; angka itu konsisten dengan rasio 2,42 terhadap 0,41, tetapi satuan nilai mAP50 pada tabel tidak dijelaskan di teks. Satu buah hanya berukuran 4 sampai 12 piksel pada citra 4096 × 2160.

Untuk dimensi tandan, metode rotasi masker menghasilkan R² = 0,62 dan RMSE = 32,5, sedangkan metode ukuran masker R² = 0,47 dan RMSE = 37,7 (satuan RMSE tidak disebut pada teks). Untuk dimensi buah, korelasi dilaporkan R² = 0,85 dengan RMSE 0,65. Pada tingkat OIV buah, 84% prediksi sama dengan acuan dan 16% berbeda satu tingkat. Penulis memperkirakan simpangan sekitar 3 cm dari ukuran sebenarnya akibat konversi piksel ke sentimeter.

Hitungan buah per tandan (Tabel 7), sebagian:

| Tandan | Acuan | YOLACT | Spatial Embeddings |
|---|---|---|---|
| 1 | 33 | 2 (6%) | 10 (30%) |
| 2 | 43 | 35 (81%) | 47 (109%) |
| 3 (total) | 124 | 46 | 135 |
| 4 | 22 | 10 (45%) | 23 (105%) |
| 7 | 15 | 14 (93%) | 16 (107%) |
| 10 | 46 | 13 (28%) | 19 (41%) |

Rentang rasio hitungan YOLACT adalah 0% sampai 148% dan Spatial Embeddings 30% sampai 116%. Tandan 3 berisi dua tandan yang tergabung menjadi satu instans, sehingga hitungan dipisah kiri dan kanan untuk perbandingan. Deskriptor OIV 204 (kerapatan tandan) dan 222 (keseragaman ukuran buah) tidak dihasilkan karena deteksi buah yang terlewat.

## Kelebihan dan Keterbatasan
Penulis menyatakan kelebihan berupa perangkat UAV dan kamera komersial, cakupan area yang lebih luas dibanding kendaraan darat, dan ketersediaan dataset video serta anotasi MOTS secara daring. Keterbatasan yang dinyatakan penulis: pelacakan tidak memadai karena positif palsu, yang dikaitkan dengan kemiripan warna tandan hijau dan daun serta ukuran tandan yang kecil terhadap bingkai besar; hitungan buah hanya mewakili sisi tandan yang tampak sehingga tetap menaksir rendah jumlah sesungguhnya; tandan ternaungi tidak terdeteksi utuh; konversi piksel ke sentimeter dapat bergeser akibat sudut terbang berbeda antarbaris; dan dua deskriptor OIV tidak dihasilkan. Penulis juga menyarankan perekaman satu baris tanaman per video dan optimasi jalur terbang.

Menurut pembacaan ringkasan ini, skala pengujian fenotipe kecil (sepuluh tandan pada Tabel 6 dan 7, tiga puluh buah pada Tabel 8), sehingga estimasi akurasi memiliki ketidakpastian yang tidak dilaporkan. Menurut pembacaan ringkasan ini, tabel pelacakan hanya memuat satu jalannya pelatihan per konfigurasi tanpa pengulangan, dan hanya satu kebun serta satu kultivar yang diuji. Menurut pembacaan ringkasan ini, akurasi hitungan 79,5% dan 44,6% adalah rerata rasio terhadap anotasi buah yang tampak pada sepuluh tandan, bukan terhadap hitungan lapangan penuh.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tandan yang tampak pada banyak bingkai video dengan mekanisme MOTS (PointTrack), yaitu pelacakan identitas lewat *embedding* instans dari titik 2D. Namun hasil pelacakan dinyatakan tidak memadai (MOTSA dan sMOTSA negatif) dan tidak ada hitungan tandan unik yang dilaporkan dari identitas pelacakan; hasil yang dilaporkan untuk penghitungan adalah hitungan buah per tandan dari satu bingkai. Hitungan tidak dilaporkan per kelas. Acuan adalah anotasi citra (buah yang tampak dan dimensi terukur visual pada bingkai teranotasi), bukan panen atau hitung manual di lapangan.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah praktik evaluasi pelacakan dengan metrik MOTS yang memperhitungkan positif palsu dan pergantian ID, serta pelajaran bahwa kemiripan warna objek dengan latar membatasi *embedding* berbasis warna. Perbedaan penting adalah video UAV pada satu baris tanaman, bukan pengambilan multi-sisi pohon, dan makalah tidak membahas penyatuan hitungan dari sisi yang berbeda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `arizasentis2023object`.

Ariza-Sentís dkk. menerapkan MOTS pada video RGB UAV di kebun anggur Loureiro tanpa pemangkasan daun: PointTrack mencapai MODSP 93,85 pada deteksi tandan tetapi tidak memadai untuk pelacakan (sMOTSA −9,51 dan MOTSA −8,17 pada model terbaik, dilatih dengan 679 bingkai), sementara Spatial Embeddings menaksir jumlah buah per tandan lebih akurat (79,5%) daripada YOLACT (44,6%) terhadap anotasi buah yang tampak.

Catatan verifikasi data: Angka pelacakan dan deteksi tandan berasal dari Tabel 3, konfigurasi dari Tabel 2, metrik buah dari Tabel 4 dan 5, hitungan per tandan dari Tabel 7, R² dan RMSE dari seksi 3.3 dan 3.4, serta persentase OIV dari seksi 3.4. Abstrak menyebut "MODSA 93,85", sedangkan Tabel 3 mencantumkan 93,85 pada kolom MODSP; entri ini mengikuti tabel. Ekstraksi teks merusak tanda minus pada Rec128_800 (ditulis "¡9.51" dan "¡8.17"), dibaca sebagai −9,51 dan −8,17 sesuai pembahasan penulis. Sebagian nilai Tabel 5 (misalnya 1,82 dan 2,42) tidak berunit jelas. Teks tabel 6 dan 8 (tingkat OIV per tandan dan per buah) berupa warna dan tidak terbaca, sehingga hanya persentase ringkasan yang dikutip. Tabel 7 dipotong dan hanya sebagian baris yang disalin di atas; tandan 5, 6, 8, dan 9 tidak disalin tetapi tersedia di teks.
