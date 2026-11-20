# Ground based hyperspectral imaging for extensive mango yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gutierrez2019ground` |
| Judul asli | Ground based hyperspectral imaging for extensive mango yield estimation |
| Penulis | Guti\'errez, Salvador; Wendel, Alexander; Underwood, James |
| Tahun | 2019 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [gutierrez2019ground.pdf](../pdf/gutierrez2019ground.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2018.12.041

## Gambaran Umum

Estimasi hasil buah di blok kebun merupakan kebutuhan pertanian presisi, tetapi praktiknya masih mengandalkan pengambilan sampel pohon dan penghitungan buah manual yang padat karya. Pencitraan RGB telah terbukti cukup untuk estimasi hasil, sedangkan pencitraan hiperspektral (HSI) menjanjikan pengukuran sifat lain, seperti deteksi penyakit, klasifikasi kultivar, dan estimasi kematangan. Penelitian ini menguji apakah HSI pemindaian garis (line-scan) dari platform darat dapat menggantikan RGB untuk estimasi hasil dengan satu sensor, dan membandingkan kinerjanya dengan pendekatan RGB mutakhir pada skala kebun penuh.

Data dikumpulkan pada 6 dan 7 Desember 2017 di kebun mangga komersial (Mangifera indica L., kultivar B74) di Simpson Farms, Bundaberg, Queensland, Australia. Sepuluh baris pohon sepanjang 58–260 m mencakup 494 pohon yang dibagi menjadi lima himpunan: latih hitungan lapangan (27 pohon), uji hitungan lapangan (18), latih RGB (18), validasi RGB (215), dan uji RGB (216). Platform kendaraan darat tanpa awak bernama Shrimp membawa kamera hiperspektral pemindaian garis Resonon Pika II Vis-NIR, lidar Velodyne HDL64E, dan GPS RTK Novatel SPAN-CPT. Kamera merekam 648 piksel per garis dengan 244 titik spektra 12-bit pada rentang 390–890 nm (resolusi 2 nm) pada 133 bingkai per detik. Praproses mencakup konversi bilangan digital menjadi radiansi dengan koreksi arus gelap dan medan datar, lalu kompensasi iluminasi dengan metode LOGSEP.

Delimitasi pohon dilakukan dengan segmentasi data lidar yang diproyeksikan ke bingkai kamera. Setiap piksel diklasifikasikan sebagai mangga atau bukan mangga oleh jaringan saraf konvolusional dengan dua lapisan konvolusi dan dua lapisan terhubung penuh; konvolusi berjalan hanya sepanjang spektrum, bukan antarpiksel tetangga. Citra biner hasil klasifikasi diproses dengan dilatasi dan erosi morfologi, transformasi jarak Euclidean, dan pencarian maksimum lokal; jumlah maksimum lokal menjadi hitungan buah. Tujuh parameter proses ini dioptimalkan dengan algoritma genetika CHC memakai koefisien determinasi (R²) sebagai fungsi objektif.

Pengujian terhadap hitungan manual di pohon menghasilkan R² hingga 0,75 pada 18 pohon uji, dengan galat akar kuadrat rata-rata (RMSE) 36,478 buah pada model terbaik setelah koreksi persamaan slope-intercept. Terhadap hitungan RGB mengikuti Stein dkk. (2016), model terbaik memberi R² 0,77 (tampilan tunggal), 0,83 (tampilan ganda), dan 0,74 (multi-tampilan) pada 215 pohon validasi serta nilai yang hampir sama pada 216 pohon uji. Model yang dilatih hanya pada data RGB dan diterapkan pada hitungan lapangan memberi R² 0,72 dengan RMSE 41–45 buah. Pengulangan pada 6 dan 7 Desember memberi R² 0,88 (hitungan lapangan) dan 0,91 (RGB), dengan selisih hitungan total 2,8% dan 1,3%. Acuan hitung adalah koefisien determinasi dan RMSE terhadap hitungan buah manual di pohon serta hitungan RGB; cawat uji adalah 18 pohon hitungan lapangan dan 216 pohon uji RGB yang tidak dipakai dalam pelatihan atau validasi.

Penulis menyatakan HSI tidak mencapai tingkat akurasi RGB, terutama pada multi-tampilan, karena resolusi dan medan pandang kamera hiperspektral lebih rendah dan kamera pemindaian garis hanya memiliki satu dimensi spatial sehingga teknik multi-tampilan tidak dapat diterapkan. Oklusi oleh daun, cabang, dan buah lain menyebabkan hitungan selalu lebih rendah dari jumlah buah sebenarnya; penulis menyatakan undercounting ini konsisten dan dapat dikompensasi dengan kalibrasi slope-intercept, dengan sekitar 20 sampel kalibrasi cukup untuk menentukan faktornya. HSI tetap terkena oklusi seperti RGB karena citra akhirnya berupa citra dua dimensi. Penulis menyimpulkan HSI layak digunakan terutama ketika sensor tersebut sudah dipilih untuk mengukur sifat lain.
