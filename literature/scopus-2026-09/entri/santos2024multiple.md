## Gambaran Umum
Makalah ini mengusulkan alur kerja (*pipeline*) pencacahan buah jeruk manis dari video untuk perkiraan hasil panen di kebun komersial. Alur tersebut terdiri atas deteksi buah tampak dengan jaringan saraf konvolusional (*convolutional neural network*, CNN), pelacakan antarbingkai dengan algoritma Hungarian, komponen relokalisasi berbasis estimasi lokasi 3D buah untuk menangani buah yang tertutup dan buah yang muncul kembali, serta regresor jaringan saraf yang memperkirakan jumlah buah total pada pohon. Teks yang tersedia adalah versi *preprint* (arXiv 2312.16724v1, 29 Desember 2023). Data berasal dari program Orange Crop Forecast milik Fundecitrus di sabuk jeruk São Paulo dan Minas Gerais, Brasil. Buah yang dicacah umumnya masih hijau (belum matang), dan video direkam dengan ponsel pada tingkat tanah di antara baris pohon.

Penulis menerbitkan dua set data: MORANGET (12 urutan video beranotasi untuk pelacakan multi-objek, *multi-object tracking*, MOT) dan ORANDET (57.812 ubin citra dengan 222.201 kotak pembatas untuk deteksi jeruk). Pada analisis sensitivitas dengan deteksi hasil anotasi yang dikurangi secara acak, galat relatif pencacahan buah tampak pada 12 urutan gabungan adalah 2,34% (tingkat deteksi 100%), 3,01% (80%), 14,44% (60%), dan 55,93% (40%). Dengan detektor CNN, galat relatif gabungan terbaik adalah 1,25% (YOLOv5l, skor lebih dari 0,7) dengan HOTA 0,56039.

Regresor hasil panen mencapai koefisien determinasi $R^2$ = 0,61 pada seluruh 1.139 pohon, naik menjadi 0,79 dan 0,85 setelah pohon dengan cakupan hitungan di bawah 20% atau 30% dari acuan panen dikeluarkan. Acuan evaluasi regresor adalah hitungan hasil pemanenan lebih awal seluruh buah pada pohon (*fruit stripping*), bukan anotasi citra.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkiraan panen jeruk di Brasil dilakukan Fundecitrus dengan pemanenan lebih awal seluruh buah pada sampel sekitar 1.500 pohon. Prosedur itu padat karya, sehingga pencacahan buah berbasis citra dipertimbangkan sebagai pengganti atau pelengkap. Sistem berbasis citra tunggal cenderung menghitung terlalu rendah karena satu sudut pandang tidak menjangkau sebagian besar buah. Sistem berbasis banyak citra atau video cenderung menghitung terlalu tinggi karena buah yang sama tampak pada beberapa bingkai, sehingga diperlukan asosiasi data yang mencegah penghitungan ganda.

Penulis menyatakan bahwa evaluasi akurasi pencacahan multi-bingkai masih kurang, terutama untuk (i) buah hijau yang tertutup dan masuk kembali ke medan pandang pada pohon berdaun lebat, dan (ii) pembandingan terhadap hitungan lapangan yang sebenarnya. Pohon jeruk setinggi hingga 5 m tidak dapat masuk utuh ke satu bingkai kamera dari ruang antarbaris, dan satu sudut pandang tetap tidak mencakup seluruh buah. Pelacak berbasis gerak (misalnya filter Kalman) dinilai kurang memadai untuk oklusi panjang dan perubahan arah gerak, sehingga jalur buah terputus dan hasil menjadi terlalu tinggi.

## Ide Utama
Gagasan utama adalah menambahkan komponen jangka panjang berupa relokalisasi 3D ke pelacakan antarbingkai. Gerak kamera (*ego-motion*) diestimasi dengan *structure from motion* (SfM) memakai COLMAP. Setiap buah yang telah terlacak cukup lama dimodelkan sebagai bola dengan pusat dan jari-jari 3D, lalu diproyeksikan ulang ke bingkai berikutnya. Kotak hasil proyeksi dicocokkan dengan deteksi baru yang belum terkait dengan jalur mana pun. Dengan demikian identitas buah dipertahankan bukan berdasarkan tampilan, melainkan berdasarkan lokasi geometris.

Gagasan kedua adalah pemakaian pose kamera yang sama untuk mempercepat anotasi: pengguna menggambar kotak pada beberapa bingkai, alat menaksir bola 3D buah, lalu memproyeksikannya ke semua bingkai. Gagasan ketiga adalah regresor yang memetakan jumlah buah tampak dari kedua sisi pohon, ditambah varietas, tinggi, lebar, kedalaman, umur, wilayah, dan sektor, ke jumlah buah sebenarnya. Penulis menjelaskan bahwa hanya pose kamera yang diperlukan, bukan rekonstruksi 3D penuh.

## Cara Kerja Langkah demi Langkah

```
 video satu sisi pohon -> ekstraksi bingkai -> seleksi bingkai (ORB + FLANN)
        |                                          |
        |                                  SfM (COLMAP): matriks P_i
        |                                          |
        +--> deteksi CNN (ubin 416x416) -----------+--> pelacak:
                                                      Hungarian + relokalisasi 3D
                                                              |
                         jumlah buah tampak sisi A dan B + data pohon
                                                              |
                                              regresor jaringan saraf -> hasil pohon
```

### 1. Akuisisi data dan set data
Program Orange Crop Forecast memakai pengambilan sampel acak berstrata (wilayah, varietas, umur) atas 1.560 pohon: 1.200 pohon undian awal dan 360 pohon pengganti yang lebih muda. Pemanenan lebih awal dilakukan pada 28 Maret sampai 11 Mei 2022; buah dihitung dengan alat hitung otomatis di laboratorium Araraquara, SP, dan dikelompokkan menurut periode pembungaan F1 sampai F4. Fundecitrus menyediakan acuan hitungan, tinggi, umur, dan varietas untuk 1.543 pohon. Video direkam dengan ponsel beresolusi 1940 × 1080 piksel, orientasi potret, satu video per sisi pohon (sisi yang menghadap baris), dengan lintasan dari bagian bawah ke tengah lalu puncak tajuk. Pencahayaan tidak dikendalikan. Jumlah ponsel dan tipe kamera tidak dilaporkan.

MORANGET berisi 12 urutan (satu sisi satu pohon) dari lima wilayah di negara bagian São Paulo (Limeira, Duartina, Porto Ferreira, Brotas, Avaré), empat varietas (Valencia, Natal, Pera, Hamlin), dengan jumlah bingkai 222 sampai 634 dan jumlah jeruk beranotasi 13 sampai 192 per urutan; totalnya 1.198 jalur buah. Sembilan urutan direkam dengan ponsel pada gimbal. ORANDET dibangun dari empat urutan MORANGET (V04, V05, V07, V11) yang dipotong menjadi 21.031 ubin berukuran 416 × 416 piksel, ditambah 3.065 ubin dari studi deteksi jeruk terdahulu. Delapan urutan sisanya menjadi data uji (33.716 ubin).

### 2. Pemilihan bingkai dan estimasi kamera
Semua bingkai diekstraksi dengan FFmpeg. Bingkai dipilih secara iteratif: deskriptor ORB dibandingkan dengan FLANN antara bingkai terakhir terpilih dan bingkai berikutnya, dan bingkai baru dimasukkan bila jumlah korespondensi di bawah ambang atau jarak rata-rata titik kunci melebihi 10 piksel. Prosedur ini mengurangi jumlah bingkai 50 sampai 70 persen. Matriks proyeksi $P_i$ (3 × 4) tiap bingkai diestimasi dengan COLMAP sehingga $x_i = P_i X$. Pohon dengan video buruk gagal pada tahap SfM dan tidak diproses lebih lanjut.

### 3. Deteksi buah
Enam arsitektur dilatih pada ORANDET: YOLOv3, YOLOv5, YOLOv6, YOLOv7, YOLOv8, dan EfficientDet (B0 dan B3), memakai MMYOLO dan MMDetection, optimizer SGD dengan momentum, serta augmentasi *flip* acak dan *mosaic* (kecuali pada YOLOv3 dan EfficientDet). Saat pelacakan, tiap bingkai dibagi menjadi 24 ubin 416 × 416 dengan tumpang tindih 82 piksel, diproses bersama, digabung kembali, dan diberi *non-maximum suppression* dengan ambang IoU 0,2. Ambang skor 0,5, 0,6, dan 0,7 diuji.

### 4. Asosiasi kotak dan pelacakan
Kotak pada dua himpunan dicocokkan dengan varian algoritma Hungarian (Jonker-Volgenant tanpa inisialisasi, SciPy) dengan biaya $1 - \mathrm{IoU}$; pasangan dengan IoU nol dibuang. Jalur berstatus ACTIVE bila ada kotak pada bingkai berjalan dan LOST bila tidak ada. Pada tiap bingkai, relokalisasi dilakukan lebih dahulu, kemudian asosiasi dengan bingkai berikutnya. Jalur yang tidak cocok menjadi LOST, dan kotak yang tidak cocok membentuk jalur baru.

### 5. Estimasi posisi 3D dan relokalisasi
Jalur kontigu dengan sedikitnya lima kotak memicu estimasi pusat buah dengan triangulasi linear langsung (DLT) yang dibungkus RANSAC (sampel tiga kotak, ambang galat proyeksi ulang, rasio *inlier*, batas iterasi). Jari-jari 3D diperkirakan dari ukuran kotak, jarak kamera ke buah, dan panjang fokus melalui median taksiran, dikalikan konstanta $c = 0{,}9$ karena kotak cenderung melebihi batas buah. Untuk jalur LOST, pusat dan jari-jari diproyeksikan ke bingkai berjalan menjadi kotak $\tilde b_i$, lalu dicocokkan dengan deteksi yang belum terhubung. Hanya jalur dengan model 3D yang berhasil diestimasi yang dihitung sebagai buah. Jalur boleh tidak kontigu.

### 6. Regresor hasil panen
Dari 1.543 pohon, 1.197 berhasil diproses oleh tahap sebelumnya, dan 1.139 pohon tersisa setelah pohon dengan data dimensi hilang atau tanpa hitungan pelacakan pada salah satu sisi dikeluarkan. Target regresor adalah F1 + F2 + F3 karena buah periode keempat terlalu kecil untuk terdeteksi. Masukan mencakup hitungan pelacakan sisi A dan B, varietas, kelompok varietas, umur, dimensi pohon, wilayah, dan sektor; variabel kategorikal dikodekan *one-hot* dan variabel numerik distandardisasi. Dibandingkan dengan SVM, *bagging*, dan *gradient boosting*, jaringan umpan-maju memberi hasil terbaik. Arsitekturnya terdiri atas tiga lapis padat (7, 7, dan 1 neuron) dengan satu lapis normalisasi *batch*, total 386 parameter (372 dapat dilatih). Pemilihan memakai validasi silang sepuluh lipatan dan uji t-Student pada $p = 0{,}05$. Implementasi memakai Keras.

## Eksperimen dan Hasil
Pelacakan dievaluasi pada MORANGET dengan HOTA, DetA (komponen deteksi), AssA (komponen asosiasi), dan MOTA, serta galat relatif jumlah jalur terhadap jumlah buah beranotasi (CbyT terhadap CbyT-GT). Acuan hitung pada tahap ini adalah anotasi video (1.198 jalur pada 12 urutan), bukan hitungan lapangan; hitungan lapangan hanya dipakai untuk regresor.

**Sensitivitas terhadap deteksi (Tabel 5, kotak anotasi dihapus acak, tanpa komponen belajar mesin).**

| Tingkat deteksi | HOTA | MOTA | CbyT | Galat relatif | Median per urutan |
|---|---|---|---|---|---|
| 100% | 0,93516 | 0,97308 | 1.170 | 2,34% | 1,23% |
| 80% | 0,71210 | 0,73859 | 1.162 | 3,01% | 2,20% |
| 60% | 0,46614 | 0,46427 | 1.025 | 14,44% | 12,35% |
| 40% | 0,19832 | 0,15328 | 528 | 55,93% | 55,77% |

Nilai CbyT-GT adalah 1.198 pada semua baris. Tanpa relokalisasi (Tabel 6), hitungan menjadi tidak stabil: galat relatif 95,08% pada deteksi 100% (2.337 jalur) dan 248,58% pada deteksi 80% (4.176 jalur).

**Deteksi pada ORANDET (Tabel 7, 121.685 kotak uji, skor 0,5, IoU 0,5).**

| Model | Presisi | *Recall* | F1 |
|---|---|---|---|
| YOLOv5l | 0,77 | 0,69 | 0,73 |
| YOLOv8l | 0,82 | 0,65 | 0,72 |
| YOLOv7l | 0,79 | 0,66 | 0,72 |
| YOLOv3 | 0,88 | 0,58 | 0,70 |
| YOLOv6l | 0,81 | 0,58 | 0,67 |
| EfficientDet B3 | 0,85 | 0,55 | 0,67 |
| EfficientDet B0 | 0,87 | 0,51 | 0,64 |

**Pelacakan dengan detektor CNN (Tabel 8, lima hasil terbaik).**

| Detektor (ambang skor) | HOTA | MOTA | CbyT | Galat relatif | Median |
|---|---|---|---|---|---|
| YOLOv5l (> 0,7) | 0,56039 | 0,58540 | 1.183 | 1,25% | 6,95% |
| YOLOv3 (> 0,5) | 0,51003 | 0,54786 | 1.153 | 3,76% | 8,45% |
| YOLOv8l (> 0,6) | 0,54216 | 0,56415 | 1.128 | 5,84% | 9,40% |
| YOLOv7l (> 0,6) | 0,52306 | 0,53131 | 1.140 | 4,84% | 10,24% |
| EfficientDet B3 (> 0,5) | 0,55564 | 0,56775 | 1.086 | 9,34% | 11,82% |

Pada Tabel 9 (YOLOv5l), galat per urutan berkisar dari 0,87% (V12) sampai 37,50% (V09). Urutan V09 dan V10 menunjukkan dua sisi satu pohon kecil dengan angin, oklusi daun berat, dan buah yang lebih matang daripada data latih; kurang dari 20 jeruk tampak sehingga sedikit buah yang terlewat menghasilkan galat relatif besar. Penulis mencatat bahwa hitungan dapat akurat meskipun HOTA dan MOTA sedang (sekitar 0,5), karena jalur yang terputus sebagian menurunkan HOTA tetapi tidak menurunkan hitungan selama jalur tidak digabungkan dengan buah lain.

**Regresor hasil panen.**

| Kondisi | Pohon (uji) | $R^2$ |
|---|---|---|
| Seluruh data, hitungan dari YOLOv3 | 1.139 (228 uji; 911 latih) | 0,61 |
| Cakupan hitungan minimal 20% dari acuan | 741 (148 uji) | 0,79 |
| Cakupan hitungan minimal 30% dari acuan | 558 (98 uji) | 0,85 |
| Cakupan minimal 30%, hitungan dari YOLOv5l | 668 (111 uji; 557 latih) | 0,82 |

Penulis juga melaporkan bahwa pada sebagian besar urutan MORANGET, jeruk yang teridentifikasi anotator setara dengan 30 sampai 50% hasil panen sebenarnya (F1 + F2 + F3), dengan pengecualian V03 (12,5%).

## Kelebihan dan Keterbatasan
Kelebihan yang tampak dari makalah: evaluasi memakai metrik MOT baku (HOTA, DetA, AssA, MOTA) dan bukan hanya galat hitungan; relokalisasi diuji secara terpisah melalui ablasi (Tabel 6); analisis sensitivitas memisahkan kualitas deteksi dari kualitas pelacakan; hasil dikaitkan dengan hitungan lapangan dari pemanenan awal pada lebih dari seribu pohon; dan data serta anotasi dipublikasikan. Alat anotasi berbasis pose kamera mempercepat pembuatan acuan jalur.

Keterbatasan yang dinyatakan penulis: buah di bagian dalam tajuk tidak pernah tampak sehingga hitungan visual tidak dapat mencapai 100%; relokalisasi dan pelacakan terganggu oleh angin, oklusi berat, dan buah yang lebih matang daripada data latih (V09 dan V10); kegagalan SfM pada video berkualitas buruk menyebabkan pohon keluar dari alur; kualitas video lapangan sangat memengaruhi hasil; batas antarpohon sulit ditentukan secara visual sehingga penentuan buah ke pohon yang benar tidak bebas galat pada sistem berbasis citra; dan validitas asumsi bahwa sedikitnya 30% hasil panen tampak pada tajuk masih perlu diuji.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Nilai $R^2$ tertinggi (0,85) diperoleh setelah pohon dengan cakupan hitungan rendah dikeluarkan menggunakan acuan hasil panen, sehingga syarat penyaringan itu tidak dapat diterapkan pada pohon baru yang hasil panennya belum diketahui; set uji pun mengecil menjadi 98 pohon. Analisis sensitivitas memakai kotak anotasi yang dihapus acak tanpa positif palsu atau ketidaksejajaran kotak, sehingga tidak mewakili kesalahan detektor nyata. Pelacakan dievaluasi pada hanya 12 urutan (12 pohon-sisi). Hitungan per kelas (misalnya kematangan) tidak dilaporkan karena yang dicacah hanyalah satu kelas "jeruk". Pemilihan ambang skor dilakukan pada data evaluasi yang sama dengan pelaporan (lima hasil terbaik per model dilaporkan), dan makalah tidak menyebut pemisahan data khusus untuk pemilihan itu.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari satu kali dalam beberapa bingkai video. Mekanismenya adalah pelacakan multi-objek dengan asosiasi Hungarian berbasis IoU antarbingkai ditambah relokalisasi 3D berbasis pose kamera dari SfM (COLMAP) untuk menyambung kembali jalur yang hilang akibat oklusi atau keluar-masuk medan pandang. Pencacahan dilakukan untuk satu kelas saja ("jeruk"), sehingga tidak ada hitungan per kelas. Kedua sisi pohon direkam dalam video terpisah, dan hitungan sisi A serta sisi B dijumlahkan sebagai masukan regresor tanpa pencocokan identitas buah antarsisi; makalah tidak menjelaskan penanganan buah yang tampak dari kedua sisi.

Acuan hitung bersifat ganda. Untuk kualitas pelacakan, acuannya adalah anotasi jalur pada video MORANGET. Untuk regresor hasil panen, acuannya adalah hitungan hasil pemanenan lebih awal seluruh buah pada pohon. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi mencakup gagasan relokalisasi geometris berdasarkan pose kamera yang tidak memerlukan kemiripan tampilan, penggunaan hitungan lapangan untuk mengevaluasi regresor, regresi dari hitungan visual ke total sebenarnya, serta pelaporan galat gabungan (yang lebih kecil) di samping galat per pohon. Pemindahan itu bergantung pada ketersediaan pose kamera, sedangkan makalah ini tidak menyediakan mekanisme pencocokan antarsisi pohon yang terpisah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `santos2024multiple`.

Santos dkk. mengusulkan alur kerja pencacahan jeruk manis dari video ponsel yang terdiri atas deteksi CNN, pelacakan multi-objek dengan asosiasi Hungarian, relokalisasi buah yang tertutup atau keluar-masuk medan pandang berdasarkan estimasi lokasi 3D dari pose kamera (SfM), dan regresor jaringan saraf yang memetakan hitungan visual dan data pohon ke hasil panen. Pada 12 urutan MORANGET, hitungan gabungan dengan detektor YOLOv5l memiliki galat relatif 1,25% dari 1.198 jalur acuan (HOTA 0,56039), dan tanpa relokalisasi galat pada deteksi 100% naik menjadi 95,08%. Regresor mencapai $R^2$ = 0,61 pada 1.139 pohon dan 0,85 setelah pohon dengan cakupan hitungan di bawah 30% dari hasil panen dikeluarkan. Makalah ini menyediakan set data MORANGET dan ORANDET yang tersedia untuk umum.

Catatan verifikasi data: Seluruh angka diambil dari teks *preprint* arXiv (judul pada berkas teks: "A pipeline for multiple orange detection and tracking with 3-D fruit relocalization and neural-net based yield regression in commercial citrus orchards"; judul pada daftar tugas dan versi jurnal dapat berbeda, dan ada kemungkinan angka versi terbit berbeda). Angka sensitivitas berasal dari Tabel 5 dan Tabel 6 (baris "All"); angka deteksi dari Tabel 7; angka pelacakan dari Tabel 8 dan Tabel 9; ukuran MORANGET dari Tabel 1 dan ORANDET dari Tabel 2; arsitektur regresor dari Tabel 4; hasil regresor dari seksi 4.3 (Gambar 10, 11, dan 12). Jumlah pohon bervariasi menurut tahap (1.543, 1.197, 1.139, 741, 558, 668) sebagaimana tertulis di seksi 3.1, 3.4.1, dan 4.3. Teks ekstraksi tabel terbaca dengan baik, tetapi gambar tidak dapat diperiksa dari teks. Parameter yang tidak dilaporkan pada teks yang dibaca mencakup nilai numerik ambang RANSAC (galat proyeksi ulang maksimum, rasio *inlier*, iterasi maksimum) dan hiperparameter latih detektor seperti jumlah epoch. Hasil per kelas tidak ada karena pencacahan satu kelas.
