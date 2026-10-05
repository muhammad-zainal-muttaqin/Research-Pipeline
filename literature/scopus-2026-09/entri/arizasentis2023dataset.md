# Dataset on UAV RGB videos acquired over a vineyard including bunch labels for object detection and tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arizasentis2023dataset` |
| Judul asli | Dataset on UAV RGB videos acquired over a vineyard including bunch labels for object detection and tracking |
| Penulis | Ariza-Sent\'\is, Mar; V\'elez, Sergio; Valente, Jo\~ao |
| Tahun | 2023 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [arizasentis2023dataset.pdf](../pdf/arizasentis2023dataset.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2022.108848

## Gambaran Umum

Makalah ini adalah artikel data (*Data in Brief*) yang merilis kumpulan video RGB dari pesawat nirawak (*unmanned aerial vehicle*, UAV) di atas kebun anggur komersial seluas 1,06 ha di Tomiño, Pontevedra, Galicia, Spanyol, bersama label masker tandan anggur yang terlihat. Kumpulan data ini dimaksudkan untuk melatih dan menguji algoritma deteksi serta pelacakan objek untuk pencacahan tandan anggur pada tahap awal perkembangan.

Tanaman yang diamati ialah *Vitis vinifera* cv. Loureiro. Dataset memuat 40 video RGB dari empat penerbangan (satu penerbangan per baris tanaman), dan 29 video di antaranya dianotasi dengan masker tingkat piksel dalam gaya MOTS (*Multi-Object Tracking and Segmentation*), dengan total 681 bingkai berlabel. Makalah ini tidak melaporkan hasil model apa pun; kontribusinya ialah data dan anotasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Menurut penulis, pencacahan tandan anggur pada tahap dini memberi informasi tentang potensi hasil panen bagi pengelola kebun, tetapi hitung manual di lapangan memakan tenaga dan waktu. Penginderaan jauh dengan UAV berkamera RGB atau multispektral dinyatakan dapat mempercepat dan menelitikan pekerjaan itu. Diperlukan data video berlabel yang memuat oklusi daun nyata agar algoritma deteksi dan pelacakan dapat dilatih untuk pencacahan tandan.

## Ide Utama

Gagasan dataset ini ialah merekam sisi barisan tanaman dari ketinggian rendah dan menganotasi setiap tandan yang terlihat dengan masker yang konsisten secara temporal, sehingga setiap tandan mempertahankan identitas yang sama sepanjang urutan video. Format MOTS dipilih untuk keperluan ini. Dataset sengaja tidak memangkas daun, sehingga oklusi daun tetap ada dan dapat dipakai untuk meneliti tandan yang setengah tersembunyi.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Penerbangan dilakukan pada 28 Juni 2021 di atas empat baris (baris 4, 6, 7, dan 8; baris 5 tidak direkam karena banyak tanaman terkena penyakit esca dan sedikit tandan) pada hari cerah dengan kecepatan angin di bawah 0,5 m/s. Platform ialah DJI Matrice 210 RTK dengan kamera DJI Zenmuse X5S (sensor 20,8 megapiksel, ukuran piksel 3,4 μm). Kecepatan terbang 0,7 m/s pada ketinggian 3 m di atas permukaan tanah. Kamera dimiringkan 60 derajat. Video berukuran 4096 × 2160 piksel pada 59,94 bingkai per detik, tanpa pemrosesan lanjutan. Panjang tiap baris sekitar 110 m. Fase buah berada di antara ukuran kacang polong (BBCH75) dan penutupan tandan (BBCH79), sekitar dua bulan sebelum panen.

Kebun ditanam tahun 1990 dengan orientasi NE-SW, sistem *vertical shoot positioning*, jarak tanam 2,5 × 3 m, dan batang bawah 196.17C. Tidak ada pemangkasan daun (*leaf removal*).

### 2. Isi dataset

| Penerbangan | Baris | Jumlah video | Ukuran total (GB) |
|---|---|---|---|
| 1 | 4 | 14 | 2,01 |
| 2 | 6 | 8 | 0,99 |
| 3 | 7 | 14 | 3,47 |
| 4 | 8 | 4 | 1,02 |

Total ukuran video per baris dinyatakan 7,5 GB pada keterangan Tabel 1. Nama berkas berpola "Row*nomorBaris*.*nomorKlip*_*nomorBagian*".

### 3. Prosedur anotasi

Sebanyak 29 video dianotasi memakai perangkat CVAT dengan gaya MOTS. Tandan dianotasi dengan akurasi per piksel tanpa tangkai, dan setiap tandan yang terlihat diberi label walau berada dalam bayangan. Anotasi berformat PNG; jumlah bingkai per video berkisar 15 sampai 28, total 681 bingkai berlabel. Anotasi konsisten secara temporal, yaitu setiap instans tandan memiliki identitas yang sama sepanjang video. Pada contoh Row 6.1_3, jumlah tandan terlihat pada cuplikan ialah 16. Penulis menyebut Mask R-CNN dan PointTrack sebagai contoh algoritma yang dapat dilatih dengan data ini.

## Eksperimen dan Hasil

Makalah ini tidak memuat eksperimen model, metrik deteksi, atau hasil pencacahan. Hasilnya ialah deskripsi dataset yang dirangkum pada tabel berikut.

| Atribut | Nilai |
|---|---|
| Luas kebun | 1,06 ha |
| Jumlah penerbangan | 4 |
| Jumlah video | 40 |
| Video beranotasi | 29 |
| Bingkai berlabel | 681 |
| Bingkai per video beranotasi | 15 sampai 28 |
| Resolusi video | 4096 × 2160 |
| Laju bingkai | 59,94 bingkai/detik |
| Repositori | Zenodo, 10.5281/zenodo.7330951 |

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis: data mencakup oklusi daun nyata, anotasi tingkat piksel yang konsisten secara temporal, serta kemungkinan pemakaian untuk fenotipe (panjang dan lebar tandan) dan pemeriksaan kesehatan kebun.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan. Data berasal dari satu kebun, satu kultivar, dan satu hari perekaman, dan hanya satu sisi tiap baris yang direkam, sehingga tandan di sisi lain baris atau tandan yang tertutup daun tidak dianotasi dan tidak dihitung. Sebelas dari 40 video tidak beranotasi. Tidak ada acuan hitung manual atau hitung panen yang dilaporkan dalam makalah ini, sehingga akurasi pencacahan tidak dapat dinilai dari dataset ini saja. Tidak ada garis dasar (*baseline*) model yang dilaporkan.

## Kaitan dengan Tinjauan main6

Dataset ini mendukung penanganan tandan yang terlihat pada banyak bingkai melalui anotasi identitas konsisten antarbingkai (gaya MOTS) pada video satu sisi baris tanaman. Makalah ini sendiri tidak menyajikan mekanisme pelacakan atau pencocokan; mekanisme itu diserahkan kepada pemakai data (misalnya PointTrack). Hitungan tidak dilaporkan per kelas, dan acuan hitung ialah anotasi citra, bukan panen maupun hitung manual lapangan.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan ialah rancangan anotasi dengan identitas konsisten dan praktik merekam sisi baris secara terpisah. Karena hanya satu sisi baris yang direkam dan tidak ada pencocokan antar-sisi, dataset ini tidak menyediakan data untuk menguji identitas lintas sisi.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `arizasentis2023dataset`.

Ariza-Sentís dkk. (2023, *Data in Brief* 46, 108848) merilis 40 video RGB UAV dari kebun anggur cv. Loureiro seluas 1,06 ha di Spanyol, direkam pada ketinggian 3 m dengan kamera dimiringkan 60 derajat, dengan masker tandan gaya MOTS pada 29 video (681 bingkai berlabel) untuk melatih algoritma deteksi dan pelacakan dalam pencacahan tandan anggur.

Catatan verifikasi data: seluruh angka berasal dari Tabel Spesifikasi, Tabel 1, Seksi 2.1, 2.2, dan 3. Total 7,5 GB berasal dari keterangan Tabel 1; penjumlahan ukuran baris pada tabel itu ialah 7,49 GB (dihitung), selisih pembulatan. Makalah ini tidak melaporkan hasil model, sehingga tidak ada metrik yang dapat diverifikasi. Teks sebelas video tanpa anotasi dihitung dari 40 dikurangi 29. Jumlah tandan total pada seluruh dataset tidak dilaporkan.
