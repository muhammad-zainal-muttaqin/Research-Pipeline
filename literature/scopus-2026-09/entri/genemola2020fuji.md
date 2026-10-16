# Fuji-SfM dataset: A collection of annotated images and point clouds for Fuji apple detection and location using structure-from-motion photogrammetry

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2020fuji` |
| Judul asli | Fuji-SfM dataset: A collection of annotated images and point clouds for Fuji apple detection and location using structure-from-motion photogrammetry |
| Penulis | Gen\'e-Mola, Jordi; Sanz-Cortiella, Ricardo; Rosell-Polo, Joan R.; Morros, Josep-Ramon; Ruiz-Hidalgo, Javier; Vilaplana, Ver\'onica; Gregorio, Eduard |
| Tahun | 2020 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2020fuji.pdf](../pdf/genemola2020fuji.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2020.105591

## Gambaran Umum

Makalah ini adalah artikel data (*Data in Brief*) yang menerbitkan dataset Fuji-SfM: citra warna dan awan titik tiga dimensi (3D) dari kebun apel komersial Fuji (*Malus domestica* Borkh. cv. Fuji) di Agramunt, Catalonia, Spanyol. Data diambil pada September 2017, tiga minggu sebelum panen, pada tahap pertumbuhan BBCH 85. Dataset terkait dengan makalah metode yang sama dari para penulis tentang deteksi dan lokalisasi 3D buah dengan segmentasi instans dan fotogrametri *structure-from-motion* (SfM).

Dataset terdiri atas tiga bagian: (1) 288 sub-citra warna beserta masker segmentasi apel untuk melatih jaringan segmentasi instans seperti Mask R-CNN; (2) 582 citra urutan gerak (*motion sequence*) dari 11 pohon apel berurutan yang memuat 1455 apel, dipakai membangun model 3D dengan SfM; (3) awan titik 3D hasil pindaian dengan posisi apel acuan dalam koordinat global. Penulis menyatakan ini dataset pertama untuk deteksi buah yang memuat citra urutan gerak untuk membangun model 3D pohon dengan SfM beserta anotasi lokasi 2D dan 3D.

Makalah tidak melaporkan metrik kinerja model; kontribusinya adalah data dan anotasinya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa dataset deteksi buah yang ada berbasis sensor RGB, RGB-D, dan LiDAR, sedangkan dataset dengan awan titik 3D berwarna hasil SfM belum tersedia. Data seperti itu diperlukan untuk mengembangkan, melatih, dan menguji algoritma deteksi buah berbasis citra RGB, awan titik berwarna, atau kombinasi keduanya, dengan aplikasi prediksi hasil panen, pemetaan hasil panen, dan pemanenan otomatis. Dataset ini juga dimaksudkan agar semua metode dan hasil pada makalah penelitian terkait dapat direproduksi.

## Ide Utama

Gagasannya adalah menyediakan, dalam satu paket, citra yang dianotasi untuk deteksi 2D, urutan citra bertumpang tindih untuk rekonstruksi 3D, dan acuan posisi 3D setiap apel pada awan titik. Dengan acuan 3D yang dinyatakan dalam koordinat global, apel yang tampak pada banyak citra dari posisi kamera berbeda berkorespondensi dengan satu kotak 3D, sehingga posisi buah menjadi identitas bersama lintas citra.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Kamera yang dipakai adalah Canon EOS 60D DSLR dengan sensor CMOS APS-C 18 MP (5184 x 3456 piksel) dan lensa Canon EF-S 24 mm f/2.8 STM (panjang fokus setara film 35 mm adalah 38 mm; makalah menulis ukuran sensor 22,3 x 14,8 mm pada satu tempat dan 22,3 x 14,9 mm pada tempat lain). Citra diambil dengan tangan bebas dari jarak sekitar 3 m terhadap bidang tengah baris pohon dan ketinggian 1,7 m. Pohon dilatih dalam sistem *tall spindle* dengan tinggi kanopi maksimum sekitar 3,5 m dan lebar 1,5 m.

Set citra urutan gerak diambil dari kedua sisi 11 pohon berurutan yang memuat total 1455 apel. Terdapat 53 posisi pemotretan per sisi dengan jarak sekitar 0,2 m (disebut sekitar 22 cm pada tabel spesifikasi) antara dua posisi berurutan. Pada tiap posisi dilakukan sapuan vertikal 5 sampai 6 foto sehingga seluruh tinggi pohon tercakup. Hasilnya 291 citra per sisi, dengan tumpang tindih vertikal lebih dari 30% dan horizontal lebih dari 90%. Sisi timur dipotret pagi hari (11:53 sampai 12:26) dan sisi barat sore hari (15:27 sampai 16:05) agar pencahayaan kedua sisi serupa. Citra untuk set masker diambil dari zona kebun yang dipilih acak.

### 2. Set masker (Mask-set)

Folder ini berisi 12 citra mentah. Karena kinerja jaringan deteksi menurun pada objek kecil, setiap citra dibagi menjadi 24 sub-citra berukuran 1024 x 1024 piksel. Sebanyak 288 sub-citra yang dihasilkan dibagi menjadi 231 untuk pelatihan dan 57 untuk validasi, lalu dianotasi manual dengan poligon memakai perangkat lunak VIA. Anotasi disimpan dalam format CSV dan JSON, dan dapat diubah menjadi masker biner dengan fungsi seperti `poly2mask` di MATLAB.

### 3. Set SfM dan awan titik

Sebanyak 582 citra (291 per sisi) dari 11 pohon dipakai membangun model 3D dengan SfM berbasis *bundle adjustment* memakai Agisoft Professional Photoscan v1.4. Penanda yang diketahui posisinya dipakai untuk penskalaan dan georeferensi. Awan titik tiap sisi baris digabung menjadi satu awan titik, disimpan dalam format TXT dengan baris `[x, y, z, R, G, B]` (R, G, B bernilai 0 sampai 255).

### 4. Anotasi 3D

Awan titik dianotasi manual dengan perangkat lunak CloudCompare v2.9 dengan menempatkan kotak pembatas 3D persegi panjang di sekeliling tiap apel. Sebanyak 1455 apel dianotasi. Tiap anotasi disimpan dalam berkas TXT: baris pertama berisi posisi pusat apel `[x, y, z]` dan delapan baris berikutnya berisi sudut kotak. Dataset tersedia di Zenodo (DOI 10.5281/zenodo.3712808).

## Eksperimen dan Hasil

Makalah ini tidak memuat eksperimen model. Hasilnya berupa komposisi dataset.

| Bagian | Isi | Jumlah |
|---|---|---|
| Mask-set | citra mentah | 12 |
| Mask-set | sub-citra 1024 x 1024 piksel | 288 (231 latih, 57 validasi) |
| SfM-set | citra urutan gerak | 582 (291 per sisi) |
| SfM-set | pohon apel | 11 |
| Awan titik | apel dianotasi (kotak 3D) | 1455 |
| Akuisisi | posisi pemotretan per sisi baris | 53 |

Kinerja deteksi, jumlah titik awan, dan galat lokalisasi tidak dilaporkan dalam makalah ini; makalah merujuk pada artikel penelitian terkait yang pada saat penerbitan berstatus *submitted*.

## Kelebihan dan Keterbatasan

Penulis tidak memuat bagian keterbatasan. Kelebihan yang dinyatakan penulis: dataset pertama dengan awan titik berwarna hasil SfM beserta citra urutan gerak sumbernya dan anotasi 2D serta 3D; dataset memungkinkan algoritma berbasis RGB, awan titik, atau gabungan keduanya; dan seluruh hasil makalah penelitian terkait dapat direproduksi.

Menurut pembacaan ringkasan ini, keterbatasannya adalah satu kultivar, satu kebun, dan satu musim; hanya 11 pohon pada set 3D; anotasi 3D dilakukan manual tanpa pengukuran kesepakatan antarpenganotasi; set masker hanya berisi 12 citra mentah; dan tidak ada hasil dasar (*baseline*). Terdapat pula ketidakkonsistenan kecil pada ukuran sensor (22,3 x 14,8 mm versus 14,9 mm) dan jarak antarposisi (sekitar 22 cm versus 0,2 m).

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali: apel yang sama tampak pada banyak citra urutan gerak yang bertumpang tindih (horizontal lebih dari 90%) dari dua sisi baris. Mekanismenya adalah rekonstruksi 3D SfM dan anotasi kotak 3D per apel pada awan titik global, sehingga satu apel memiliki satu posisi 3D terlepas dari banyaknya citra yang memuatnya. Penggabungan deteksi lintas citra sendiri tidak diuraikan dalam makalah ini, melainkan pada makalah penelitian terkait.

Hitungan tidak dilaporkan per kelas (hanya apel). Acuan hitung adalah anotasi manual pada awan titik, yaitu 1455 apel pada 11 pohon; makalah tidak menyebut hitung panen atau hitung lapangan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multisisi adalah prosedur pembuatan acuan identitas: pemotretan dua sisi dengan tumpang tindih tinggi, penggabungan kedua sisi ke satu koordinat global memakai penanda, dan anotasi satu kotak 3D per buah. Keterbatasan pemindahan: tajuk kelapa sawit jauh lebih tinggi dan berbeda struktur dari pohon *tall spindle* setinggi sekitar 3,5 m, dan makalah tidak menguji kondisi itu.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `genemola2020fuji`.

Gené-Mola dkk. menerbitkan dataset Fuji-SfM yang memuat 288 sub-citra beranotasi masker apel, 582 citra urutan gerak dari 11 pohon apel Fuji dengan 1455 apel, serta awan titik 3D hasil SfM yang dianotasi dengan kotak 3D untuk setiap apel dalam koordinat global. Dataset dimaksudkan untuk pengembangan algoritma deteksi dan lokalisasi buah berbasis citra RGB, awan titik berwarna, atau gabungannya, dan tersedia di Zenodo.

Catatan verifikasi data: Jumlah 288, 231, 57, 12, 582, 291, 53, 11 pohon, dan 1455 apel berasal dari abstrak, tabel spesifikasi, dan seksi 1 dan 2. Spesifikasi kamera, jarak, tumpang tindih, dan jam pemotretan berasal dari seksi 2 dan tabel spesifikasi. Tidak ada metrik kinerja yang dapat diverifikasi karena tidak dilaporkan. Teks ekstraksi PDF terbaca baik.
