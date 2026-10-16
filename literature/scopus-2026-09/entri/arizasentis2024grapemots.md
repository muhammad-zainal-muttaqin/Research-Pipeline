# GrapeMOTS: UAV vineyard dataset with MOTS grape bunch annotations recorded from multiple perspectives for enhanced object detection and tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arizasentis2024grapemots` |
| Judul asli | GrapeMOTS: UAV vineyard dataset with MOTS grape bunch annotations recorded from multiple perspectives for enhanced object detection and tracking |
| Penulis | Ariza-Sent\'\is, Mar; Wang, Kaiwen; Cao, Zhen; V\'elez, Sergio; Valente, Jo\~ao |
| Tahun | 2024 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [arizasentis2024grapemots.pdf](../pdf/arizasentis2024grapemots.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2024.110432

## Gambaran Umum

Makalah ini adalah artikel data (*Data in Brief*) yang menerbitkan dataset GrapeMOTS: video UAV (*unmanned aerial vehicle*) kebun anggur beserta anotasi tandan anggur dalam gaya *Multiple Object Tracking and Segmentation* (MOTS), yaitu segmentasi per piksel dengan identitas (ID) yang dipertahankan antarbingkai. Video direkam dari beberapa sudut pandang agar tandan yang tertutup daun lebih mungkin terlihat dari setidaknya satu sudut.

Data dikumpulkan pada musim panen 2023, tanggal 19 dan 20 September, di kebun komersial anggur (*Vitis vinifera* cv. Loureiro) seluas 1,06 hektare di Tomiño, Pontevedra, Galicia, Spanyol. Dataset memuat 11 video dengan 5958 bingkai berlabel (angka yang dinyatakan makalah), berukuran total 78,8 GB tanpa video asli. Delapan video direkam dengan perencanaan lintasan multisudut dan tiga video direkam dari pandangan depan sebagai kontrol.

Makalah ini tidak melaporkan model, metrik deteksi, atau hasil pencacahan. Kontribusinya berupa sumber data dan anotasinya; keterbatasan dinyatakan "None" oleh penulis.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pencacahan buah di lapangan melelahkan bagi manusia karena jumlah buah besar. Algoritma deteksi dan pelacakan objek dapat membantu, tetapi menurut penulis algoritma tersebut menghitung terlalu sedikit (*undercounting*) karena oklusi, yaitu buah tersembunyi di balik daun atau cabang. Penulis menyatakan perekaman dari banyak sudut pandang diperlukan untuk meningkatkan peluang merekam buah dari titik yang paling terlihat.

Penulis juga menyatakan bahwa dataset terbuka utama tidak memuat label untuk buah tertentu seperti tandan anggur. Dataset ini diposisikan sebagai pelengkap dataset sebelumnya dari kebun yang sama: dataset yang memakai kamera genggam dari berbagai sudut untuk menghindari oklusi (lebih dari 11.000 citra, dirujuk dari makalah lain) dan dataset yang menyediakan instans untuk lokalisasi tandan tanpa pelacakan. Pembeda dataset ini adalah penambahan ID tandan yang sama antarbingkai.

## Ide Utama

Gagasan utamanya adalah merekam baris tanaman dari sisi yang sama melalui beberapa sudut pandang dan memberi satu ID tetap pada setiap tandan anggur, termasuk ketika tandan itu tampak dari sudut berbeda dengan bentuk berbeda. Dengan demikian, dataset dapat dipakai melatih dan menguji algoritma deteksi dan pelacakan agar tandan dihitung satu kali dan agar oklusi daun berkurang.

Penulis menyebut bahwa pelacakan tandan memungkinkan pencacahan per sisi baris kebun yang relevan bagi estimasi hasil panen, dan bahwa anotasi bersama informasi acuan dapat dipakai mengekstraksi sifat fenotipik.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Platform yang dipakai adalah DJI Phantom4 RTK dengan sensor RGB terintegrasi (rentang bukaan f2.8 hingga f11, kecepatan rana 8 hingga 1/8000 s). Penerbangan dilakukan pada ketinggian 3 m di atas permukaan tanah (AGL), kecepatan terbang tidak stabil antara 0,1 dan 1 m/s, langit cerah, dan kecepatan angin di bawah 0,5 m/s. Pesawat terbang di atas baris yang bersebelahan dan merekam sisi baris yang menjadi sasaran. Tanaman ditanam tahun 1990 dalam sistem *vertical trellis* berorientasi timur laut-barat daya, dengan jarak antarbaris 3 m dan antartanaman 2,5 m. Daun tidak dipangkas sehingga oklusi daun tinggi. Panjang tiap baris sekitar 110 m, dan bingkai dari kedua sisi kanopi baris tersedia.

Dua jenis video diperoleh. Delapan video berawalan PathPlanning_ mengikuti perencanaan lintasan berbasis *Ant Colony Optimization* (ACO) dengan pandangan multisudut, masing-masing dari tanaman anggur yang berbeda. Tiga video berawalan NoPathPlanning_ memberi pandangan depan sisi kanopi pada tanaman yang sama dengan video multisudut sehingga dapat dibandingkan. Video PathPlanning_1 dan PathPlanning_3 berukuran 1920 x 1080 piksel pada 30,00 bingkai/detik. Video lain berukuran 3840 x 2160 piksel pada 29,97 bingkai/detik, kecuali NoPathPlanning_2 dan NoPathPlanning_3 yang berukuran sama tetapi 30,00 bingkai/detik.

### 2. Anotasi

Sebelas video dianotasi dengan perangkat lunak CVAT dalam gaya MOTS, dengan ketelitian per piksel. Tandan yang berada dalam bayangan juga dianotasi agar model dapat menggeneralisasi pada beragam pencahayaan. Anotasi hanya mencakup tandan anggur, tanpa tangkai dan daun di sekitarnya. Pada video multisudut, tandan tampak dari sudut berbeda dengan bentuk beragam, dan ID yang sama dipertahankan untuk tandan yang terlihat dari sudut berbeda. Untuk efisiensi, langkah bingkai 2 dipakai pada sebagian besar video, kecuali PathPlanning_1 dan ketiga video tanpa perencanaan lintasan. Video NoPathPlanning_2 dan NoPathPlanning_3 juga memuat label batang tanaman (*trunk*) dan tiang (*pole*).

### 3. Format dan distribusi

Video disediakan dalam format MP4, sedangkan bingkai dan anotasi dalam format PNG. Folder instans memuat berkas teks berisi label anotasi. Dataset tersedia di Zenodo dengan DOI 10.5281/zenodo.10625595.

## Eksperimen dan Hasil

Makalah tidak memuat eksperimen model. Hasil utamanya adalah deskripsi dataset pada Tabel 1.

| Video | Multisudut | Label | Bingkai teranotasi | Ukuran (GB) |
|---|---|---|---|---|
| PathPlanning_1 | Ya | Grape bunch | 927 | 3,8 |
| PathPlanning_2 | Ya | Grape bunch | 209 | 3,3 |
| PathPlanning_3 | Ya | Grape bunch | 400 | 1,7 |
| PathPlanning_4 | Ya | Grape bunch | 373 | 6,2 |
| PathPlanning_5 | Ya | Grape bunch | 270 | 4,3 |
| PathPlanning_6 | Ya | Grape bunch | 284 | 4,6 |
| PathPlanning_7 | Ya | Grape bunch | 224 | 3,2 |
| PathPlanning_8 | Ya | Grape bunch | 374 | 5,7 |
| NoPathPlanning_1 | Tidak | Grape bunch | 898 | 13,6 |
| NoPathPlanning_2 | Tidak | Grape bunch, trunk, pole | 899 | 15,2 |
| NoPathPlanning_3 | Tidak | Grape bunch, trunk, pole | 900 | 16,4 |

Teks makalah menyatakan total 5958 bingkai berlabel. Penjumlahan kolom bingkai teranotasi pada Tabel 1 (dihitung oleh ringkasan ini) menghasilkan 5.758 bingkai, yaitu 3.061 pada delapan video multisudut dan 2.697 pada tiga video kontrol. Selisih 200 bingkai tidak dijelaskan dalam makalah. Jumlah tandan teranotasi, jumlah ID unik, dan jumlah segmentasi tidak dilaporkan.

## Kelebihan dan Keterbatasan

Penulis menyatakan keterbatasan "None". Kelebihan yang tersirat dari desain data: terdapat pasangan video multisudut dan video pandangan depan dari tanaman yang sama sehingga pengaruh sudut pandang terhadap oklusi dapat dibandingkan; ID tandan dipertahankan lintas sudut; anotasi per piksel; dan data dapat digabung dengan dataset lain dari kebun yang sama (video, ortofoto UAV, LiDAR).

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan yang tidak dinyatakan penulis. Pertama, makalah tidak melaporkan jumlah tandan, jumlah ID, ataupun acuan hitung lapangan (panen atau hitung manual) sehingga akurasi pencacahan tidak dapat dinilai dari dataset ini. Kedua, tidak ada hasil dasar (*baseline*) deteksi atau pelacakan. Ketiga, hanya satu kultivar, satu kebun, dan satu musim yang tercakup. Keempat, makalah tidak menjelaskan bagaimana kesesuaian ID antarsudut diverifikasi, dan penjumlahan Tabel 1 tidak sama dengan total bingkai yang tertulis.

## Kaitan dengan Tinjauan main6

Makalah ini menangani tandan yang terlihat lebih dari sekali, yaitu tandan yang sama muncul pada banyak bingkai video dan dari beberapa sudut pandang UAV. Mekanismenya bukan algoritma, melainkan anotasi: ID yang sama diberikan secara manual pada tandan yang sama lintas bingkai dan lintas sudut dalam format MOTS. Dataset ini karenanya menyediakan acuan identitas untuk menguji pelacakan atau pencocokan lintas pandang. Makalah menyatakan pelacakan memungkinkan pencacahan per sisi baris.

Hitungan tidak dilaporkan per kelas; hanya satu kelas buah (tandan anggur) yang dilabeli, ditambah batang dan tiang pada dua video. Acuan hitungnya adalah anotasi citra (video), bukan panen atau hitung manual di lapangan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multisisi adalah rancangan data: pasangan rekaman multisudut dan rekaman kontrol dari objek yang sama serta ID yang konsisten lintas sudut, yang menjadi bentuk acuan identitas untuk menguji pencacahan. Makalah tidak menawarkan metode penggabungan identitas yang dapat dipindahkan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `arizasentis2024grapemots`.

Ariza-Sentís dkk. menerbitkan dataset GrapeMOTS yang berisi 11 video UAV kebun anggur cv. Loureiro (Tomiño, Spanyol, September 2023) dengan anotasi tandan gaya MOTS dan ID tandan yang dipertahankan lintas bingkai dan lintas sudut. Delapan video direkam multisudut dengan perencanaan lintasan ACO dan tiga video direkam dari pandangan depan sebagai kontrol; dataset tersedia di Zenodo. Makalah tidak melaporkan hasil deteksi atau pencacahan.

Catatan verifikasi data: Spesifikasi video, tanggal, luas kebun, jarak tanam, dan ketinggian terbang berasal dari Tabel Spesifikasi dan seksi 3 dan 4. Jumlah bingkai per video berasal dari Tabel 1. Total 5958 bingkai berlabel dan ukuran 78,8 GB berasal dari seksi 4; jumlah baris Tabel 1 menurut penjumlahan ringkasan ini adalah 5.758, sehingga angka total tidak dapat direkonsiliasi dari teks. Jumlah tandan, jumlah ID unik, pembagian latih dan uji, serta kinerja model tidak dapat diverifikasi karena tidak dilaporkan. Teks ekstraksi PDF terbaca baik, tetapi tabel diekstraksi satu sel per baris.
