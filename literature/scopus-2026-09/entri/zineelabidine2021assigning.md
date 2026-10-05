# Assigning apples to individual trees in dense orchards using 3D colour point clouds

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zineelabidine2021assigning` |
| Judul asli | Assigning apples to individual trees in dense orchards using 3D colour point clouds |
| Penulis | Zine-El-Abidine, Mouad; Dutagaci, Helin; Galopin, Gilles; Rousseau, David |
| Tahun | 2021 |
| Venue | Biosystems Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [zineelabidine2021assigning.pdf](../pdf/zineelabidine2021assigning.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2021.06.015

## Gambaran Umum

Makalah ini mengusulkan alur pengolahan awan titik berwarna 3D (*3D color point cloud*) untuk menghitung apel pada pohon individu di kebun apel padat berstruktur *trellis* (rangka kawat penyangga). Persoalan yang ditangani bukan pendeteksian buah, melainkan penentuan pohon induk tiap apel (*tree membership*). Pemisahan pohon pada kebun padat sulit karena cabang pohon bersebelahan saling bersentuhan dan daun menutupi struktur cabang saat panen.

Strategi utamanya adalah merekonstruksi pohon yang sama dua kali: pada musim dingin tanpa daun (struktur cabang terlihat) dan pada masa panen (apel terlihat). Pohon dipisahkan pada awan titik musim dingin, apel dilokalisasi pada awan titik masa panen, kedua awan titik diselaraskan, dan tiap apel diberi identitas pohon dari titik cabang terdekat. Data berasal dari kebun uji varietas INRAe-Angers, Prancis, dengan pohon apel berumur 4 tahun, tujuh adegan (*scene*) berisi 4 sampai 5 pohon.

Hasil utama: seluruh batang pohon pada ketujuh adegan terdeteksi dengan jumlah yang sama dengan jumlah pohon sebenarnya. Apel terdeteksi diberi pohon induk yang benar dengan akurasi di atas 95% (100% pada empat adegan), dengan penurunan kurang dari 3% saat pemisahan pohon dilakukan otomatis dibandingkan pemisahan manual. Penulis menyebut hasil ini sebagai bukti kelayakan awal (*proof of feasibility*).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hasil panen apel biasanya diperkirakan dengan menghitung manual pada sampel tetap pohon (misalnya 5 atau 10%) lalu mengekstrapolasi. Cara ini lambat, padat karya, dan tidak selalu cukup presisi. Penghitungan buah berbasis penglihatan komputer umumnya bertujuan mengestimasi jumlah total buah yang teramati pada data yang diindra, tanpa memetakan buah ke pohon yang menumbuhkannya. Penulis menyebut tidak mengetahui studi terdahulu yang menangani masalah ini untuk apel.

Informasi hasil per pohon berguna untuk pemetaan hasil pada skala pohon, pengelolaan pohon individu agar keseragaman kebun meningkat, dan analisis berbasis pohon pada uji varietas. Tantangannya adalah pemisahan pohon: cabang pohon bertetangga saling bertaut, ukuran dan bentuk tajuk bervariasi, dan daun yang rapat saat panen menambah oklusi. Citra 2D juga menghilangkan keterhubungan cabang karena proyeksi, sehingga penulis memilih data 3D.

## Ide Utama

Gagasan intinya adalah mendaftarkan (*registration*) dua awan titik dari dua waktu berbeda. Awan titik musim dingin dipakai untuk memisahkan pohon karena struktur cabang tidak tertutup daun. Awan titik panen dipakai untuk mendeteksi apel. Setelah kedua awan titik diselaraskan, tiap apel mewarisi identitas pohon dari titik cabang berlabel terdekat pada awan titik musim dingin.

Satu objek kalibrasi, yaitu ColorChecker yang dipasang pada tongkat tripod di posisi diketahui, dipakai sebagai pola geometris (bukan sebagai acuan warna) untuk menentukan skala metrik, orientasi, wilayah minat, dan titik asal awan titik. Skala metrik memungkinkan parameter fisik (jarak antarpohon, diameter batang, diameter dan tinggi tiang) ditetapkan langsung. Penyelarasan awal oleh kalibrasi diperhalus dengan *Iterative Closest Point* (ICP).

## Cara Kerja Langkah demi Langkah

```
 Citra musim dingin ─> SfM+MVS ─> awan titik ─┐
                                              ├─> kalibrasi (ColorChecker)
 Citra panen ───────> SfM+MVS ─> awan titik ─┘
        │                                │
 deteksi apel (HSV)            pemisahan pohon (kawat, tiang, batang,
        │                       komponen terhubung) pada awan musim dingin
        └──────────> ICP ──> apel -> titik cabang terdekat -> pohon
```

### 1. Akuisisi data

Lokasi: kebun uji varietas INRAe-Angers, Prancis (47,48226° LU, 0,6152° BT). Pohon apel berumur 4 tahun dalam struktur *I-trellis* dengan tiang penyangga, tiap pohon adalah mutan yang diuji untuk menjadi varietas baru (nama kultivar tidak dilaporkan). Jarak antarpohon rata-rata 1 m, tinggi pohon 1 sampai 3 m, dan variasi bentuk tajuk tinggi. Tujuh adegan diambil, masing-masing sebagian baris kebun berisi 4 sampai 5 pohon (Tabel 1). Citra RGB berukuran 3000 × 4000 piksel direkam dengan kamera Fujifilm X20 dari satu sisi baris, dengan posisi dan sudut pandang kamera dipilih acak agar seluruh adegan tercakup, dan dipotret manual. Jumlah citra per adegan:

| Adegan | Jumlah pohon | Citra musim dingin | Citra panen |
|---|---|---|---|
| 1 | 5 | 236 | 364 |
| 2 | 5 | 189 | 382 |
| 3 | 5 | 221 | 380 |
| 4 | 4 | 183 | 374 |
| 5 | 5 | 206 | 380 |
| 6 | 4 | 199 | 376 |
| 7 | 4 | 227 | 376 |

Awan titik berwarna direkonstruksi dengan VisualSFM (*Structure from Motion*, SfM) dan PMVS/CMVS (*multi-view stereo*). Sebelum pengambilan citra, ColorChecker dipasang pada tripod dan dua jarak diukur manual dengan pita ukur: jarak minimum tripod ke baris pohon dan jarak ke pohon target yang ditunjuk.

### 2. Kalibrasi dan ekstraksi wilayah minat

ColorChecker dan tripod dideteksi otomatis pada awan titik (detail pada Material Pendukung A yang tidak ada dalam teks). Kalibrasi meliputi pengubahan skala ke ukuran metrik, pemutaran ke kerangka acuan kanonik (sumbu Y sejajar baris pohon, sumbu Z tegak lurus tanah), ekstraksi pohon di belakang ColorChecker, dan pemindahan titik asal ke dasar pohon yang ditunjuk.

### 3. Deteksi kawat *trellis* dan batang pohon (awan musim dingin)

Prosedur 12 langkah: voxelisasi (sel 5 mm), skeletonisasi sumbu medial, proyeksi ke bidang sejajar baris dan *Hough transform* untuk garis horizontal kandidat, penaksiran bidang *trellis* dengan MSAC (varian RANSAC, jarak inlier 0,5 cm), penggabungan garis menjadi empat garis kawat (pemisahan minimal 30 cm), pencarian kandidat batang dari histogram kepadatan titik di dekat bidang *trellis* (radius 5 cm, sel 1 cm), verifikasi batang melalui skeleton dan jalur terpendek (panjang minimal 1 m), serta penolakan tiang penyangga (jari-jari 4,5 cm, tinggi 2,3 m, rasio titik pada cangkang silinder di atas 0,8). Titik dalam jarak 3 cm dari sumbu batang diberi label batang. Titik kawat dan pipa air diperoleh lewat pencocokan garis MSAC (toleransi 7 cm untuk garis terendah dan 4 cm untuk lainnya) lalu dibuang bersama tiang.

### 4. Pemisahan pohon

Awan titik tanpa kawat dan tiang divoxelisasi dan diskeletonisasi, lalu komponen terhubung diekstrak. Komponen dengan jarak kurang dari 30 cm ke suatu batang diberi label batang itu. Komponen yang terhubung ke lebih dari satu batang dianggap menjangkau beberapa pohon bersentuhan dan dipecah dengan menemukan jalur terpendek antara titik puncak batang bertetangga, lalu memotong pada titik ekstrem tinggi (heuristik: titik tempat arah sumbu Z berbalik dianggap titik temu cabang). Komponen "mengambang" (tidak dekat batang mana pun) diberi label dari salah satu dari dua komponen berlabel terdekat; bila jarak ke yang satu lebih dari 3 kali jarak ke yang lain, dipilih yang terdekat, sedangkan bila tidak, garis diperpanjang dari titik ujung dan dipilih komponen dengan jarak minimum ke garis tersebut. Setiap titik akhirnya mewarisi label komponen skeleton terdekat.

### 5. Deteksi apel

Deteksi memakai ambang warna sederhana pada ruang HSV: rentang *hue* 0,15 sampai 0,2 untuk apel hijau atau kuning, dan 0 sampai 0,05 serta 0,95 sampai 1 untuk apel merah. Titik terpilih divoxelisasi, komponen terhubung dicari, dan pusat kotak pembatasnya menjadi lokasi apel. Penulis menyebut pendekatan ini primitif.

### 6. Penugasan apel ke pohon

Awan titik musim dingin dan panen yang sudah terkalibrasi diselaraskan dengan ICP (metrik titik ke titik). Apel diberi identitas pohon dari titik cabang berlabel terdekat pada awan musim dingin yang telah ditransformasi.

## Eksperimen dan Hasil

Acuan dibuat manual dengan CloudCompare: label semantik tiap titik awan musim dingin (batang, cabang, kawat+pipa air, tiang), posisi apel pada awan panen, dan identitas pohon tiap apel. Apel terdeteksi dianggap benar bila berada kurang dari 10 cm dari apel acuan dan tidak ada deteksi lain yang lebih dekat. Akurasi penugasan (ACC) adalah rasio benar-tertugaskan terhadap seluruh deteksi benar. Untuk memisahkan galat akibat deformasi cabang antarmusim dari galat pemisahan pohon otomatis, penugasan dijalankan pada dua jenis data: pohon dipisahkan manual dan pohon dipisahkan otomatis.

Tabel 3 makalah (deteksi apel berbasis warna):

| Adegan | Recall (%) | Presisi (%) |
|---|---|---|
| 1 | 74,50 | 61,29 |
| 2 | 87,34 | 62,16 |
| 3 | 88,54 | 58,21 |
| 4 | 90,00 | 48,64 |
| 5 | 90,62 | 58,58 |
| 6 | 77,41 | 65,62 |
| 7 | 80,85 | 66,66 |

Hasil segmentasi semantik pada awan musim dingin (Tabel 2): *recall* batang antara 83,23% (adegan 4) dan 95,47% (adegan 7); presisi batang antara 67,03% (adegan 5) dan 77,97% (adegan 1); F1 batang antara 76,76% dan 83,67%. Untuk kawat *trellis* dan pipa air, *recall* berkisar 75,47% sampai 91,48% dan presisi 73,65% sampai 88,20%. Tiang penyangga hanya ada pada adegan 1, 5, 6, dan 7 dengan *recall* 91,83% sampai 97,94% dan presisi 96,24% sampai 99,26%. Penulis menjelaskan presisi batang yang kurang sempurna oleh titik cabang dekat batang yang ikut berlabel batang. Jumlah batang terdeteksi sama dengan jumlah pohon sebenarnya pada ketujuh adegan.

Akurasi penugasan apel ke pohon (Gambar 8, nilai per adegan tidak terbaca dalam teks): penulis menyatakan akurasi tinggi pada kedua jenis data, 100% pada empat adegan, penurunan kurang dari 3% pada pemisahan otomatis dibandingkan manual, dan akurasi lebih dari 95% menurut abstrak dan kesimpulan.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: alur ini menjawab pertanyaan hasil per pohon yang tidak ditangani metode penghitungan total; pemanfaatan awan titik musim dingin mengatasi oklusi daun; objek kalibrasi menyediakan skala metrik sehingga parameter fisik dapat ditetapkan; dan hasil penugasan tinggi meskipun detektor apelnya sederhana. Penulis juga memisahkan galat penugasan akibat deformasi dari galat akibat pemisahan pohon otomatis.

Keterbatasan yang dinyatakan penulis: ini bukti kelayakan pertama; pengambilan citra manual memakan waktu dan ratusan citra per pohon diperlukan (disarankan drone atau robot darat); deformasi cabang antarmusim akan lebih besar pada pohon lebih tua sehingga diperlukan registrasi non-rigid; pemecahan pohon bersentuhan memakai heuristik sederhana; detektor apel berbasis warna bersifat primitif, tidak menangani kelompok apel (menyebabkan *false negative*), dan tidak memverifikasi bentuk (menyebabkan deteksi berlebih, dengan presisi rendah); serta objek kalibrasi dapat diganti pola geometris lain.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup satu kebun, pohon muda (4 tahun) di satu baris, dan tujuh adegan tanpa pengulangan, sehingga generalisasi pada kebun lain tidak teruji. Menurut pembacaan ringkasan ini, metode ini mengharuskan dua kampanye pengambilan data per tahun dan objek kalibrasi pada tiap adegan, dan identitas tidak diberikan oleh pelacakan lintas bingkai tetapi oleh kedekatan spasial, sehingga kesalahan registrasi atau pemisahan pohon langsung menjadi kesalahan penugasan. Menurut pembacaan ringkasan ini, akurasi penugasan dihitung hanya atas deteksi benar, sehingga tidak mencerminkan seluruh kesalahan hitungan per pohon yang juga dipengaruhi presisi deteksi yang rendah.

## Kaitan dengan Tinjauan main6

Makalah ini tidak menghitung buah yang terlihat lebih dari sekali; tidak ada mekanisme untuk menggabungkan pengamatan ganda atas satu buah. Rekonstruksi SfM dari banyak citra membuat satu apel muncul sebagai satu titik pada awan titik, tetapi makalah tidak menjadikan hal itu sebagai objek studi dan tidak menyatakan berapa apel yang dihitung. Mekanisme yang dibahas adalah penugasan buah ke pohon melalui registrasi awan titik dua musim. Hitungan tidak dilaporkan per kelas. Acuan berupa penandaan manual posisi apel pada awan titik panen (anotasi pada model 3D), bukan panen atau hitung manual lapangan, dan jumlah apel acuan tidak dilaporkan dalam teks.

Gagasan yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pendekatan geometris: memberi identitas pada objek lewat kedudukan relatif terhadap struktur tetap (di sini batang dan cabang, pada kelapa sawit dapat berupa batang dan pelepah) setelah semua pandangan dibawa ke satu kerangka metrik dengan objek kalibrasi. Penugasan buah ke pohon dengan data dari beberapa sisi juga relevan untuk memastikan satu tandan tidak dihitung pada dua pohon bertetangga. Keterbatasannya: metode ini mengandalkan pohon berstruktur teratur (*trellis*), awan titik padat dari ratusan citra per adegan, dan data musim tanpa daun, yang tidak tersedia pada kelapa sawit.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zineelabidine2021assigning`.

Ringkasan yang aman dikutip: Zine-El-Abidine dkk. (2020, *preprint* arXiv; terbit 2021) mengusulkan alur awan titik 3D berwarna untuk menugaskan apel terdeteksi ke pohon penghasilnya pada kebun apel padat berstruktur *trellis*, dengan memisahkan pohon pada awan titik musim dingin tanpa daun dan menyelaraskannya dengan awan titik masa panen. Pada tujuh adegan di INRAe-Angers (4 sampai 5 pohon per adegan), penulis melaporkan akurasi penugasan apel ke pohon di atas 95% dengan detektor apel berbasis warna sederhana (*recall* 74,50% sampai 90,62%, presisi 48,64% sampai 66,66%).

Catatan verifikasi data: Angka deteksi apel dibaca dari Tabel 3, segmentasi semantik dari Tabel 2, dan jumlah citra serta pohon dari Tabel 1. Nilai akurasi penugasan per adegan hanya ada pada Gambar 8 yang tidak terbaca dalam teks; yang tertulis hanya "di atas 95%" (abstrak dan kesimpulan), "100% pada empat adegan", dan "penurunan kurang dari 3%" (Bagian 3.2). Teks makalah memuat ketidakkonsistenan kecil: Bagian 3.2 menyebut *recall* "over 90,75%" dan presisi "65,37%", sedangkan nilai maksimum pada Tabel 3 adalah 90,62% dan 66,66%; ringkasan ini memakai Tabel 3. Material Pendukung A dan B (detail kalibrasi dan hasil visual semua adegan) tidak termasuk teks yang dibaca. Jumlah total apel acuan, jumlah apel terdeteksi, dan kultivar tidak dilaporkan. Teks ekstraksi dari *preprint* (versi 1, 26 Desember 2020) terbaca baik, tetapi gambar dan sebagian rumus tidak terbaca penuh.
