# Tracking and Counting Apples in Orchards under Intermittent Occlusions and Low Frame Rates

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `matos2024tracking` |
| Judul asli | Tracking and Counting Apples in Orchards under Intermittent Occlusions and Low Frame Rates |
| Penulis | Matos, Gon\ccalo P.; Santiago, Carlos; Costeira, Jo\~ao P.; Saldanha, Ricardo L.; Morgado, Ernesto M. |
| Tahun | 2024 |
| Venue | IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [matos2024tracking.pdf](../pdf/matos2024tracking.pdf)
- DOI resmi: https://doi.org/10.1109/cvprw63382.2024.00550

## Gambaran Umum
Makalah lokakarya CVPR 2024 ini mengusulkan algoritma pelacakan objek statis dengan kamera yang bergerak bebas, lalu menerapkannya untuk menghitung apel di kebun. Metode menggabungkan *Structure-from-Motion* (SfM) dengan pencocokan graf bipartit (algoritma Hungaria): buah direpresentasikan sebagai awan titik 3D yang bising, diproyeksikan kembali ke setiap bingkai 2D, lalu dicocokkan dengan deteksi pada bingkai itu. Dengan cara ini identitas buah tetap terjaga walaupun buah tertutup sebentar-sebentar (*intermittent occlusion*) dan laju bingkai rendah.

Data terdiri atas empat set video: tiga video lapangan di kebun apel INIAV, Alcobaça, Portugal (tiga varietas: Galafab, Schnico Red, Schniga Schnico; 3 sampai 6 pohon; sekitar 3 bingkai per detik), dan satu video sintetis hasil Blender (5 pohon, 25 bingkai per detik). Perbandingan dengan SORT, DeepSORT, dan ByteTrack dilakukan dengan deteksi acuan (*ground truth*) sebagai masukan.

Hasil: pelacak usulan mencapai galat persentase absolut (*absolute percentage error*, APE) tersaring 12,88%, 4,56%, 0,84%, dan 1,06% pada empat set data, dengan MOTA 0,6068 sampai 0,9375, lebih baik daripada ketiga pembanding pada semua set data.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil panen membantu perencanaan tenaga kerja, penyimpanan, dan pemasaran. Metode berbasis visi komputer yang ada umumnya mengandaikan kondisi ideal, sehingga gagal pada gerak kamera bebas dan oklusi sebentar-sebentar. Penulis menguraikan bahwa pelacak 2D berbasis kemiripan antarbingkai (filter Kalman, aliran optik, transformasi afin) kehilangan jejak bila objek tidak terlihat pada bingkai berikutnya dan bekerja buruk pada laju bingkai rendah. Pendekatan pencacahan dengan garis ROI mengandaikan kamera bergerak searah dengan kecepatan hampir konstan sehingga setiap objek melintasi garis sekali. Metode 3D yang ada umumnya memakai informasi 3D hanya untuk menghindari hitungan ganda, sedangkan pelacakannya tetap di 2D.

## Ide Utama
Pelacakan dilakukan di ruang 3D, bukan di bidang gambar. Setiap buah yang pernah dilihat menyimpan titik-titik 3D dari piksel semua deteksinya pada bingkai sebelumnya, dalam sistem koordinat global. Pada bingkai baru, titik-titik itu diproyeksikan kembali, dan jumlah titik yang jatuh di dalam setiap kotak deteksi menjadi skor kecocokan. Walaupun awan titik bising pada arah kedalaman, sebagian besar titik tetap jatuh di dalam kotak deteksi yang benar setelah diproyeksikan ulang. Asumsi: adegan statis (hari tanpa angin), kamera bergerak, parameter intrinsik diketahui, dan peta kedalaman padat tersedia untuk area deteksi.

## Cara Kerja Langkah demi Langkah

```
 video -> COLMAP (kamera, kedalaman)   deteksi 2D (YOLOv4 / anotasi)
              \                         /
   proyeksi titik 3D buah ke bingkai -> hitung titik dalam tiap kotak
   -> Hungaria -> ID lama diperbarui / ID baru dibuat -> buang jalur < 5
```

### 1. Akuisisi data
Tiga video lapangan diambil dengan kamera yang dibawa orang berjalan kaki, bergerak bebas pada tiga sumbu (menggeser, mengangguk), kadang mundur sehingga buah yang sama keluar dan masuk bingkai berulang. Pohon berbentuk datar pada kawat horizontal, mendekati panen, dengan oklusi berat oleh daun dan buah lain. Video sintetis dibuat dengan Blender, kamera bergerak horizontal dengan percepatan awal dan perlambatan akhir (meniru kendaraan pertanian), tanpa derau pada parameter kamera dan kedalaman.

### 2. Estimasi kamera dan kedalaman
Parameter intrinsik dan ekstrinsik serta peta kedalaman tiap bingkai diperoleh dengan COLMAP. Detektor yang dilatih adalah YOLOv4 untuk apel (detektor lain dinyatakan dapat dipakai); untuk evaluasi dipakai anotasi acuan sebagai deteksi "sempurna".

### 3. Pelacakan
Fungsi *project* memproyeksikan titik 3D semua buah yang sedang dilacak ke bingkai saat ini dengan mempertahankan ID. Fungsi *count* menghitung titik tiap buah di dalam tiap kotak deteksi untuk membentuk matriks skor. Algoritma Hungaria menetapkan ID buah ke deteksi. Deteksi yang tercocokkan memperbarui buah (menambah titik 3D); deteksi tanpa pasangan membentuk buah baru dengan ID baru. Jumlah buah adalah banyaknya objek pada akhir video setelah jalur dengan kurang dari 5 deteksi dibuang (ambang ditentukan secara eksperimen). Deteksi tanpa informasi kedalaman tidak dapat diproses.

## Eksperimen dan Hasil
Data (Tabel 1):

| Dataset | Pohon | Bingkai | Laju (fps) | Apel (acuan) |
|---|---|---|---|---|
| Galafab-west | 3 | 110 | sekitar 3 | 233 |
| Schnico-Red-east | 5 | 155 | sekitar 3 | 356 |
| Schniga-Schnico-west | 6 | 200 | sekitar 3 | 373 |
| Synthetic-apples-1 | 5 | 250 | 25 | 204 |

Metrik: APE, MOTA, presisi, dan *recall*, dengan IoU minimum 0,3. Acuan identitas dibuat manual dengan alat grafis buatan penulis (video sintetis: dihasilkan otomatis di Blender). Pembanding memakai basis kode penghitung buah Gené-Mola dkk. dengan SORT (max_age=30, min_hits=1), DeepSORT, dan ByteTrack.

Hasil dengan deteksi acuan (Tabel 2-5):

| Dataset | Pelacak | Recall | Apel (estimasi) | APE mentah (%) | APE tersaring (%) | MOTA |
|---|---|---|---|---|---|---|
| Galafab-west | Usulan | 0,99 | 203 | 15,93 | 12,88 | 0,7591 |
| | ByteTrack | 0,69 | 365 | 47,80 | 56,65 | 0,2099 |
| | SORT | 0,53 | 79 | 380,77 | 66,09 | 0,0468 |
| | DeepSORT | 0,04 | 40 | 82,42 | 82,83 | -0,1639 |
| Schniga-Schnico-west | Usulan | 0,91 | 356 | 27,75 | 4,56 | 0,6068 |
| | ByteTrack | 0,70 | 798 | 165,04 | 113,94 | 0,2079 |
| | SORT | 0,30 | 67 | 497,03 | 82,04 | -0,1841 |
| | DeepSORT | 0,08 | 162 | 35,38 | 56,57 | -0,2829 |
| Schnico-Red-east | Usulan | 0,96 | 359 | 4,44 | 0,84 | 0,6982 |
| | ByteTrack | 0,63 | 418 | 60,23 | 17,42 | 0,1600 |
| | SORT | 0,43 | 49 | 295,95 | 86,24 | -0,0498 |
| | DeepSORT | 0,05 | 71 | 78,19 | 80,06 | -0,1684 |
| Synthetic-apples-1 | Usulan | 1,00 | 186 | 9,90 | 1,06 | 0,9375 |
| | ByteTrack | 0,79 | 180 | 109,38 | 4,26 | 0,5375 |
| | SORT | 0,55 | 81 | 448,96 | 56,91 | 0,2930 |
| | DeepSORT | 0,32 | 74 | 60,42 | 60,64 | 0,1977 |

Presisi pelacak usulan 1,00 pada semua set data karena kotak masukan tidak diubah; presisi DeepSORT 0,53, 0,63, 0,54, dan 0,94 pada empat set data. Ablasi penyaring jalur pendek menunjukkan APE tersaring umumnya lebih baik daripada APE mentah; penulis menyebut batas minimal 2 pengamatan sudah menyaring sebagian besar positif palsu. Pada pengujian ketahanan terhadap deteksi tidak sempurna (menghapus deteksi acak untuk meniru *recall* 0,7, 0,5, dan 0,3), metode usulan konsisten lebih akurat daripada pembanding berdasarkan APE rata-rata empat set data (Gambar 3, angka tidak terbaca dari teks).

Kasus sulit yang dibahas: dua buah menyatu dalam satu deteksi YOLOv4, ambiguitas kedalaman sepanjang garis pandang (buah di pohon tertukar dengan buah di tanah), dan peta kedalaman COLMAP yang kosong sehingga *recall* di bawah 1,00.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: tahan terhadap oklusi sebentar-sebentar dan deteksi yang hilang atau palsu, tidak membatasi gerak kamera dan laju bingkai, hanya memerlukan kamera video, dan tidak memerlukan data latih untuk pelacaknya.

Keterbatasan yang dinyatakan penulis: dua buah yang konsisten tergabung dalam satu deteksi dihitung sebagai satu objek; ambiguitas kedalaman dapat menyebabkan jalur salah; peta kedalaman yang kosong membuat buah tidak terlacak; pertukaran identitas pada set Galafab-west (terutama buah di tanah yang berulang keluar dan masuk bingkai) menaikkan galat; ambang 5 deteksi ditentukan secara eksperimen dan mungkin perlu disesuaikan.

Menurut pembacaan ringkasan ini: perbandingan utama memakai deteksi acuan sehingga hasil dengan detektor nyata dan kombinasinya dengan pencacahan tidak dilaporkan secara kuantitatif; hanya tiga set lapangan berukuran kecil (110 sampai 200 bingkai); metode mengandaikan adegan statis dan memerlukan rekonstruksi SfM; pembanding dijalankan dengan parameter bawaan (kecuali SORT) dan hanya dari satu basis kode, sehingga kekalahan DeepSORT mungkin terkait konfigurasi tersebut; satu kelas buah (apel) tanpa atribut kelas.

## Kaitan dengan Tinjauan main6
Makalah ini secara eksplisit menangani buah yang terlihat berulang kali, baik dalam video berlaju rendah maupun saat buah keluar dan masuk bingkai. Mekanismenya adalah rekonstruksi 3D (SfM dan peta kedalaman), proyeksi ulang awan titik buah, dan pencocokan Hungaria; ini termasuk pencocokan multi-pandang dengan identitas disimpan dalam ruang 3D global, bukan pelacakan 2D antarbingkai berurutan. Hitungan tidak dilaporkan per kelas (satu kelas, apel). Acuan hitungannya adalah anotasi identitas manual pada video (jumlah apel yang terlihat di video), bukan panen atau hitung lapangan; untuk set sintetis acuan dibuat otomatis oleh Blender.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: penyimpanan identitas dalam koordinat global dan pencocokan dengan proyeksi ulang tidak bergantung pada urutan atau kemiripan antarbingkai, sehingga dapat berlaku bagi sisi pohon yang diambil terpisah, asalkan pose kamera dan kedalaman tersedia. Hambatannya: kebutuhan kedalaman padat, asumsi adegan statis, dan penyatuan dua buah dalam satu deteksi, yang relevan bagi tandan berdekatan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `matos2024tracking`.

Matos dkk. mengusulkan pelacak buah berbasis ruang 3D yang menggabungkan SfM (COLMAP) dengan pencocokan Hungaria antara awan titik 3D buah yang diproyeksikan ulang dan deteksi 2D, sehingga tahan terhadap oklusi sebentar-sebentar dan laju bingkai rendah (sekitar 3 fps). Dengan deteksi acuan pada tiga video kebun apel dan satu video sintetis, metode ini mencapai APE tersaring 0,84% sampai 12,88% dan MOTA 0,6068 sampai 0,9375, mengungguli SORT, DeepSORT, dan ByteTrack.

Catatan verifikasi data: Data set ada pada Tabel 1 (Seksi 4.1); hasil perbandingan pada Tabel 2-5 (Seksi 5.1). Terdapat ketidakcocokan kecil dalam teks: Tabel 1 mencantumkan 204 apel untuk Synthetic-apples-1, sedangkan keterangan Tabel 5 menyebut 188 apel, dan kedua angka tidak dijelaskan lebih lanjut; keterangan Tabel 2-4 menyebut acuan yang sama dengan Tabel 1 sambil menyatakan bahwa filter diterapkan pada acuan, sehingga makna "acuan tersaring" tidak jelas. Hasil ketahanan terhadap deteksi tidak sempurna hanya tersedia pada Gambar 3 dan tidak terbaca angkanya. Teks ekstraksi terbaca baik.
