# Image based mango fruit detection, localisation and yield estimation using multiple view geometry

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `stein2016image` |
| Judul asli | Image based mango fruit detection, localisation and yield estimation using multiple view geometry |
| Penulis | Stein, Madeleine; Bargoti, Suchet; Underwood, James |
| Tahun | 2016 |
| Venue | Sensors Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [stein2016image.pdf](../pdf/stein2016image.pdf)
- DOI resmi: https://doi.org/10.3390/s16111915

## Gambaran Umum
Makalah ini menyajikan kerangka multisensor untuk mendeteksi, melacak, melokalisasi, dan memetakan setiap buah mangga di kebun komersial, dengan tujuan menaksir hasil tanpa kalibrasi terhadap hitungan manual di lapangan. Deteksi buah per citra dilakukan dengan Faster R-CNN (jaringan VGG16). Korespondensi antar-citra berurutan dibangun dengan geometri epipolar dari pose kamera yang diberikan sistem navigasi GPS/INS, lalu dioptimalkan dengan algoritma Hungarian. Data LiDAR dipakai untuk membuat masker pohon pada citra sehingga setiap buah dapat dikaitkan dengan pohon tertentu. Buah yang terlacak ditriangulasi untuk memperoleh posisi 3D.

Eksperimen dilakukan pada satu blok kebun mangga kultivar Calypso di Simpson Farms, Bundaberg, Queensland, Australia (2 ha, 10 baris, rerata panjang baris 240 m). Sebanyak 522 pohon dipindai dari dua sisi dan 71.609 buah mangga diestimasi. Validasi memakai 16 pohon dengan hitungan manual pada pohon di lapangan dan hitungan setelah panen. Metode multi-pandang memperoleh kemiringan regresi 1,0136 terhadap hitungan panen dan R² 0,90 tanpa kalibrasi, sedangkan metode pandang tunggal hanya menghitung 27% dan pandang ganda 54% dari buah. Abstrak menyatakan galat 1,36% pada tingkat pohon; kemiringan 1,0136 setara dengan selisih 1,36% (dihitung dari angka makalah, yang sendiri menulis "1,4%" pada seksi 3.3).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Praktik industri untuk taksiran jumlah buah di blok kebun adalah menghitung rerata buah pada beberapa pohon lalu mengalikannya dengan jumlah pohon. Jumlah buah per pohon sangat bervariasi sehingga taksiran sering tidak akurat, dan pengulangan penghitungan selama pertumbuhan terlalu padat karya. Hitungan setelah panen di gudang pengemasan hanya memberi data blok secara retrospektif dan tidak dapat memetakan sebaran hasil di dalam blok.

Sistem visi berbasis citra menghadapi masalah oklusi: hubungan antara jumlah buah yang terlihat dan jumlah buah sebenarnya tidak dapat diperbaiki oleh peningkatan kinerja deteksi saja. Sistem satu citra per pohon memerlukan kalibrasi terhadap hitungan manual di lapangan atau panen, yang padat karya, rentan galat manusia, dan tidak dijamin berlaku antar-tahun, kultivar, maupun geometri kanopi. Pendekatan multi-pandang dapat mengamati lebih banyak buah, tetapi menuntut setiap buah diidentifikasi secara unik dan diasosiasikan antar-citra untuk menghindari penghitungan berlebih. Kanopi mangga berbentuk 3D, dengan pencahayaan sulit seragam, jarak sensor ke buah bervariasi, dan pola oklusi halus yang membuat estimasi kedalaman stereo tidak dapat diandalkan.

## Ide Utama
Gagasan pokoknya adalah melakukan asosiasi dan pelacakan buah sepenuhnya pada ranah citra, dengan geometri epipolar yang diturunkan dari pose kamera GPS/INS, bukan dari pencocokan fitur citra atau estimasi kedalaman stereo atau SfM. Dengan demikian akurasi pelacakan dan penghitungan tidak dibatasi oleh akurasi kedalaman. Triangulasi 3D dilakukan setelah asosiasi data dan tidak memengaruhi hitungan.

Komponen kedua adalah pengaitan buah dengan pohon melalui masker citra yang dihasilkan dari segmentasi LiDAR, sehingga hasil per pohon, per baris, dan per blok dapat dibandingkan, termasuk pembandingan terkontrol antara metode pandang tunggal, ganda, dan multi.

## Cara Kerja Langkah demi Langkah
```
 Citra RGB -> [Faster R-CNN] -> deteksi per citra
 Pose GPS/INS -> [garis epipolar terbatas 2,5-8 m] -> asosiasi berpasangan
   -> [Hungarian] -> rantai pelacakan -> hitungan = jumlah ID unik
   -> [triangulasi sinar] -> posisi 3D
 LiDAR -> [HSMM pohon] -> masker pohon -> pemungutan suara -> hitungan per pohon
```

### 1. Akuisisi data
Data direkam dengan kendaraan darat tak berawak "Shrimp" milik ACFR yang membawa kamera warna dengan lampu kilat (*strobe*), LiDAR 3D, dan GPS/INS. Kamera Prosilica GT3300C dengan lensa Kowa LM8CX merekam pada 5 Hz, citra 3296 x 2472 piksel (8,14 megapiksel), diselaraskan dengan empat lampu kilat Excelitas MVS-5002. Kecepatan 1,4 m/s menghasilkan sekitar 25 sudut pandang tiap sisi pohon. LiDAR Velodyne HDL64E dipasang miring untuk menangkap seluruh tinggi kanopi (10 Hz, 1,3 juta titik per detik). GPS/INS Novatel SPAN memberikan pose enam derajat kebebasan pada 50 Hz tanpa koreksi RTK. Pengambilan data dilakukan pada 24 November 2015, saat dinilai manajemen kebun tidak ada lagi buah rontok yang berarti. Seluruh 522 pohon dipindai dari kedua sisi dengan lintasan sekitar 5 km (sekitar 3 jam, termasuk pengulangan baris).

### 2. Data acuan dan validasi
Delapan belas pohon dipilih untuk penghitungan manual, mencakup enam pohon berenergi rendah, sedang, dan tinggi menurut NDVI satelit. Hitungan di lapangan dilakukan pertengahan Desember 2015 dan hitungan panen pada 28 Januari 2016; hitungan panen dianggap lebih akurat, sehingga perbandingan bersifat prediktif sekitar dua bulan sebelum panen. Dua pohon dikeluarkan: r5t14 (selisih hitungan lapangan dan panen, 154 berbanding 333) dan satu pohon yang tertutup sepenuhnya oleh pohon non-mangga (diberi label r3t6n pada teks dan r3t2n pada Tabel 1). Sisa 16 pohon menjadi acuan.

### 3. Deteksi buah
Data latih berupa 1.500 potongan citra 500 x 500 yang dipilih acak dari sekitar 15.000 citra (0,3% dari seluruh data), dianotasi dengan kotak secara menyeluruh untuk semua buah yang dapat dikenali mata; buah di baris latar belakang diabaikan. Pembagian 1.000-250-250 (latih, validasi, uji) dipakai untuk menilai deteksi dengan IoU > 0,2 dan kecocokan satu-satu, menghasilkan F1 0,881 pada himpunan uji. Hiperparameter tetap mengikuti Bargoti dan Underwood. Untuk inferensi pada citra penuh dipakai prediktor FR-CNN berbasis ubin (*tiled*). Citra dari kedua sisi 18 pohon sasaran dianotasi manual sebagai himpunan "dual-view hand labelled" dan tidak dipakai melatih.

### 4. Segmentasi pohon dan masker
Pohon disegmentasi pada data LiDAR memakai *hidden semi-Markov model* (HSMM); kesalahan batas dikoreksi manual (satu atau dua per baris, sekitar 2 menit tiap koreksi). Titik LiDAR di-voksel 20 cm dan ditipiskan 5%, lalu diproyeksikan ke citra untuk mencatat pohon mana yang tampak. Masker tiap citra dibuat dengan memproyeksikan titik LiDAR penuh dan memperlebarnya (*dilation*) 20 piksel, pohon terjauh lebih dahulu. Buah yang dilacak pada banyak citra dan berada di batas dua pohon diberi pohon berdasarkan suara terbanyak. Untuk perbandingan, citra pandang tunggal ditetapkan sebagai citra dengan pusat masker terdekat ke tengah citra.

### 5. Pelacakan, penghitungan, dan triangulasi
Untuk tiap buah pada citra $t_n$, sebuah sinar dari titik fokus kamera dipotong pada jarak 2,5 m dan 8 m, lalu ujung-ujungnya diproyeksikan ke citra $t_{n+1}$ sebagai segmen epipolar terbatas. Biaya asosiasi adalah jarak tegak lurus antara pusat deteksi dan segmen, bernilai tak hingga bila jarak melebihi ambang atau pusat berada di luar ujung segmen. Algoritma Hungarian (Kuhn-Munkres) memilih penugasan; deteksi yang tidak cocok dengan citra sebelumnya maupun sesudahnya ditolak sebagai positif palsu. Hitungan adalah jumlah ID unik per pohon, baris, dan blok. Ambang jarak piksel adalah satu-satunya parameter yang disetel. Posisi 3D diperoleh dengan merata-ratakan titik tengah segmen terpendek antara semua pasangan sinar observasi. Selisih waktu kamera dan GPS/INS dioptimalkan dengan meminimalkan jarak asosiasi rerata.

## Eksperimen dan Hasil
Pemilihan ambang: pada rentang 1 sampai 6.000 piksel, regresi tanpa intersep (y = mx) antara estimasi multi-pandang dan hitungan panen pada 16 pohon menunjukkan dataran stabil di atas 15 piksel; nilai 30 piksel dipilih dengan R² 0,90 dan m = 1,014. Pada ambang sangat besar (>100 piksel) R² tetap sekitar 0,9 tetapi kemiringan turun ke 0,82. Koreksi selisih waktu menemukan minimum global 0,111 s (galat asosiasi 4,2 piksel dari 11,4 piksel), dengan simpangan baku 0,0044 s pada 32 sisi pohon.

| Metode (16 pohon, terhadap hitungan panen) | Kemiringan | R² | Proporsi buah terhitung |
|---|---|---|---|
| Pandang tunggal (FR-CNN) | 0,2680 | 0,8064 | 27% |
| Pandang ganda berlawanan (FR-CNN) | 0,5376 | 0,9352 | 54% |
| Pandang ganda (dilabel manual) | tidak dilaporkan pada teks | 0,95 | 64% |
| Multi-pandang (FR-CNN) | 1,0136 | 0,8982 | 101,4% |

Pada seluruh 522 pohon, hitungan dari sisi timur dan barat berkorelasi lemah (pandang tunggal R² 0,59; multi-pandang R² 0,63), sehingga pohon tidak membagi buah sama rata pada kedua sisi. Hubungan antara hitungan pandang ganda dan multi-pandang memiliki R² 0,84 dengan kemiringan 0,48; sekitar 20 dari 522 pohon merupakan pencilan yang diduga akibat penaksiran berlebih multi-pandang. Pengulangan satu sisi baris 5: pandang tunggal kemiringan 1,02 dan R² 0,96 (total 1.505 dan 1.532, galat 1,8%); multi-pandang kemiringan 0,97 dan R² 0,84 (total 3.026 dan 2.981, galat 1,5%).

Triangulasi pada empat pohon yang seluruh buahnya dilabel manual memberi jarak tetangga terdekat rerata 0,11 m dan persentil ke-95 sebesar 0,36 m. Peta hasil menaksir total 71.609 mangga setelah dikoreksi dengan membagi kemiringan 1,0136; total per baris berkisar dari 2.587 sampai 11.344 (baris 1 sampai 3 rendah karena letak gudang dan pohon non-mangga). Volume kanopi dari LiDAR hampir tidak berhubungan dengan hasil.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tidak memerlukan kalibrasi terhadap hitungan manual pada hasil multi-pandang; asosiasi tidak bergantung pada kedalaman stereo atau SfM; hanya satu parameter yang disetel dan hasil tidak sensitif di atas lantai derau; LiDAR bersifat opsional kecuali untuk hitungan per pohon; dan dilakukan perbandingan langsung metode pandang tunggal, ganda, dan multi.

Keterbatasan yang dinyatakan penulis: galat ketika bingkai hilang atau platform berosilasi (tiga pencilan pengulangan pada pohon 1, 12, dan 60); fragmentasi lintasan dan penghitungan ganda saat buah terhalang batang lalu muncul kembali (pelacakan hanya antar-bingkai berurutan); pertukaran identitas pada buah yang bergerombol; rumput tinggi yang membuat buah jatuh terhitung; kestabilan hubungan buah terlihat terhadap buah total belum diketahui untuk blok, kultivar, atau jenis buah lain. Penulis menyatakan kesalahan sinkronisasi waktu dan kehilangan bingkai telah diperbaiki pada percobaan berikutnya (NTP/PPS dan PTP).

Menurut pembacaan ringkasan ini, validasi hanya mencakup 16 pohon dari satu blok, satu kultivar, dan satu musim, dengan kemiringan 1,0136 dari pencocokan regresi tanpa intersep, bukan galat per pohon; penjelasan tentang "galat 1,36% pada tingkat pohon" pada abstrak sebaiknya dibaca sebagai bias agregat, bukan galat tiap pohon, karena R² hanya 0,90. Penulis sendiri mencatat pencilan multi-pandang dan repeatabilitas yang lebih rendah daripada pandang tunggal. Detektor melewatkan sebagian buah yang terlihat (pandang ganda: 54% oleh FR-CNN berbanding 64% oleh anotasi manual), sehingga kemiringan mendekati 1 dapat sebagian mencerminkan keseimbangan antara buah yang terlewat dan hitungan berlebih; penulis membahas dan menepis kemungkinan ini berdasarkan dataran kemiringan dan pemeriksaan visual, tetapi tidak dapat membuktikannya sepenuhnya.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali, dan mekanismenya jelas: asosiasi berpasangan antar-bingkai berurutan dengan segmen epipolar terbatas dari pose GPS/INS, dipadukan dengan algoritma Hungarian, sehingga satu buah mempertahankan satu ID sepanjang rantai pelacakan. Pasangan citra dari sisi pohon yang berlawanan tidak dicocokkan; sisi timur dan barat dilacak secara terpisah pada tiap lintasan baris dan hitungan kedua sisi dijumlahkan. Penulis menyatakan asosiasi 3D setelah triangulasi pernah dicoba pada data stereo oleh peneliti lain dan gagal karena galat penyelarasan GPS dari sisi berlawanan lebih besar daripada jarak antarbuah.

Hitungan hanya dilaporkan sebagai total buah per pohon, baris, dan blok untuk satu kelas (mangga), bukan per kelas kematangan. Acuan hitungan adalah hitungan manual pada pohon di lapangan dan hitungan setelah panen untuk 16 pohon. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah rancangan validasi (hitungan panen sebagai acuan, perbandingan pandang tunggal, ganda, dan multi), pemakaian satu parameter asosiasi yang tidak sensitif, serta pengaitan buah ke pohon dengan pemungutan suara. Pelacakan ini memerlukan urutan bingkai dengan pose yang tepat (GPS/INS dengan sinkronisasi waktu); penerapan pada sawit yang berdiri tinggi dan tandan besar perlu pose kamera yang andal dan tidak ditunjukkan oleh makalah ini. Makalah juga tidak menangani pencocokan identitas antar-sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `stein2016image`.

Stein, Bargoti, dan Underwood mengusulkan kerangka deteksi, pelacakan, lokalisasi, dan pemetaan buah mangga pada citra multi-pandang, dengan deteksi Faster R-CNN, asosiasi berpasangan memakai geometri epipolar dari pose GPS/INS dan algoritma Hungarian, serta pengaitan buah ke pohon melalui masker dari segmentasi LiDAR. Pada satu blok kebun mangga (522 pohon, 71.609 buah) dan 16 pohon acuan, metode multi-pandang menghasilkan kemiringan 1,0136 terhadap hitungan panen (R² 0,90) tanpa kalibrasi, sedangkan metode pandang tunggal dan ganda hanya menghitung 27% dan 54% dari buah.

Catatan verifikasi data: angka dalam abstrak dan hasil (522 pohon, 71.609 buah, 16 pohon, kemiringan dan R²) tertulis pada seksi 3.1 sampai 3.6, Gambar 10, 11, dan 12, serta Gambar 14 untuk total per baris; hitungan lapangan dan panen per pohon ada pada Tabel 1, yang diekstraksi sebagai daftar angka bertingkat dan hanya dipakai di sini untuk pohon yang dikecualikan. Teks memakai label pohon yang tidak konsisten untuk pohon yang tertutup (r3t6n pada teks, r3t2n pada Tabel 1), dan menyebut 16 pohon walaupun 18 dipilih. Terjadi pembulatan "1,36%" pada abstrak dan "1,4%" pada seksi 3.3. Koefisien kemiringan metode pandang ganda berlabel manual tidak terbaca pada teks. Teks yang tersedia terpotong pada seksi 4.4.4 (bagian kesimpulan dan sebagian daftar pustaka tidak dibaca).
