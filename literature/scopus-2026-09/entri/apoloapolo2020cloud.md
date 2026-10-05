# A Cloud-Based Environment for Generating Yield Estimation Maps From Apple Orchards Using UAV Imagery and a Deep Learning Technique

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `apoloapolo2020cloud` |
| Judul asli | A Cloud-Based Environment for Generating Yield Estimation Maps From Apple Orchards Using UAV Imagery and a Deep Learning Technique |
| Penulis | Apolo-Apolo, Orly Enrique; P\'erez-Ruiz, Manuel; Mart\'\inez-Guanter, Jorge; Valente, Jo\~ao |
| Tahun | 2020 |
| Venue | Frontiers in Plant Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [apoloapolo2020cloud.pdf](../pdf/apoloapolo2020cloud.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2020.01086

## Gambaran Umum
Makalah ini mengusulkan alur kerja estimasi hasil panen apel per pohon dari citra *unmanned aerial vehicle* (UAV, pesawat nirawak) yang dikerjakan pada lingkungan komputasi awan Google Colaboratory (Colab). Citra nadir dari UAV dirangkai menjadi ortomosaik (*orthomosaic*, citra udara tergeoreferensi hasil penggabungan banyak citra) dengan fotogrametri *Structure from Motion* (SfM). Ortomosaik dipotong per pohon berdasarkan koordinat pohon, buah apel pada tiap potongan dideteksi dengan Faster R-CNN, dan jumlah buah terdeteksi dipetakan menjadi peta hasil per pohon dan per baris tanam.

Data diambil pada kebun apel (*Malus x domestica* Borkh. cv 'Elstar') seluas 0,47 ha dengan 592 pohon dalam 14 baris di Randwijk, dekat Wageningen, Belanda, pada musim 2018 dan 2019. Karena citra dari atas hanya memperlihatkan sebagian buah, jumlah total buah per pohon diestimasi dengan regresi linear terhadap hasil panen manual pada 19 pohon sampel.

Hasil utama menurut ringkasan makalah: hitungan visual di lapangan oleh teknisi pertanian dibandingkan dengan jumlah buah yang dipanen menghasilkan R² 0,86 (MAE 10,35; RMSE 13,56), sedangkan hitungan buah pada citra dibandingkan dengan jumlah buah yang dipanen menghasilkan R² 0,80 (MAE 128,56; RMSE 130,56). Pada 20 potongan citra uji, deteksi Faster R-CNN mencapai rerata presisi 0,93, *recall* 0,90, F1 0,91, dan akurasi 0,90 terhadap hitungan visual pada citra.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil panen yang akurat diperlukan untuk memperkirakan volume pasokan dan mengorganisasi panen. Penulis menyatakan bahwa estimasi oleh petani umumnya berupa perkiraan visual yang tidak akurat dan tidak efisien waktu, serta tidak menggambarkan sebaran hasil di dalam kebun yang bervariasi secara spasial.

Metode deteksi buah berbasis pembelajaran mendalam sebelumnya sebagian besar memakai citra dari kendaraan darat setinggi permukaan tanah. Penulis menilai pendekatan itu membutuhkan platform khusus, memakan waktu, dan dapat memperparah pemadatan tanah. Selain itu, pembuatan peta tanaman dengan SfM biasanya memerlukan perangkat lunak komersial berbayar, komputer yang kuat, dan beberapa langkah yang diawasi manual. Penulis juga menyatakan bahwa metode yang ada belum menghasilkan produk akhir yang dapat langsung dimanfaatkan petani. Tiga tujuan yang dinyatakan adalah menguji kelayakan estimasi hasil dari deteksi apel pada citra UAV, melatih dan mempublikasikan model deteksi apel, serta menyusun peta hasil per pohon dan per baris.

## Ide Utama
Gagasannya adalah menyatukan deteksi buah dan pemrosesan geospasial pada satu platform awan berbasis Python. Citra UAV dikonversi menjadi ortomosaik tergeoreferensi, ortomosaik dipotong dengan topeng lingkaran berdiameter 1 m di sekitar koordinat tiap pohon, dan jumlah buah terdeteksi pada tiap potongan ditulis ke *shapefile* untuk divisualisasikan sebagai peta hasil.

Karena ortomosaik sudah menggabungkan banyak citra tumpang tindih menjadi satu citra, deteksi dijalankan pada satu pandangan nadir per pohon. Makalah tidak memuat mekanisme untuk mengaitkan buah yang sama pada citra yang berbeda; masalah buah yang terlihat lebih dari satu kali ditangani secara implisit lewat penggabungan citra pada tahap ortomosaik. Sisi pohon yang tertutup kanopi tidak teramati, sehingga hitungan citra dikoreksi dengan regresi linear terhadap hasil panen.

## Cara Kerja Langkah demi Langkah
```
 [Citra UAV nadir] -> [SfM + GCP: ortomosaik GeoTIFF 4,18 mm/piksel]
                              |
 [Koordinat pohon] -> [topeng lingkaran 1 m per pohon] -> [TIF per pohon]
                              |
                    [Faster R-CNN: hitung buah] -> [shapefile] -> [peta hasil]
```

### 1. Akuisisi data
Platform yang dipakai adalah DJI Phantom 4 Pro dengan kamera sensor CMOS 1/2,3 inci (piksel efektif 20 M, FOV lensa 84°, panjang fokus 8,8 mm). Rencana terbang berbentuk kisi dibuat dengan aplikasi DJI Ground Station Pro. Penerbangan pada kedua musim dilakukan dua hari sebelum panen pertama (40%) pada hari cerah dengan angin lemah. Total 806 citra diambil dalam pandangan nadir pada resolusi 5.472×3.648 piksel. Teks menyebut ketinggian terbang 10 m pada satu tempat dan 15 m di atas tanah pada tempat lain; ketidakkonsistenan ini tidak dijelaskan.

Sebanyak 354 citra tahun 2019 dipakai untuk membangun set data pelatihan CNN, dan 452 citra tahun 2018 dipakai untuk membuat ortomosaik, dengan tumpang tindih depan 85% dan samping 75%. Penerbangan 2018 hanya mencakup sebagian pohon karena sisa kebun sudah dipanen. Lima titik kontrol tanah (*ground control points*, GCP) dipasang pada tiap penerbangan dan diukur dengan Topcon RTK GNSS berakurasi di bawah 2,5 cm.

### 2. Acuan lapangan
Penulis merujuk pustaka yang menyatakan bahwa hanya sekitar 60 sampai 70% produksi terlihat dari luar pohon. Sebelum panen, 19 pohon dipilih acak dari baris 5. Pohon dibagi menjadi bagian atas, tengah, dan bawah, buah dihitung secara visual pada sisi kanan dan kiri, dan pita plastik dipakai untuk membatasi area guna menghindari penghitungan ganda. Seluruh apel kemudian dipanen manual dan ditimbang dalam tiga tahap. Penulis mengasumsikan jumlah buah per baris konsisten berdasarkan data historis dari petani.

### 3. Ortomosaik dan pemotongan per pohon
Ortomosaik dibuat dengan Agisoft PhotoScan Professional 1.2.3: penyelarasan foto pada akurasi "High", penempatan GCP secara manual, dan awan titik padat 110.449.395 titik. Keluarannya adalah GeoTIFF sistem koordinat WGS 84 (EPSG:4326) dengan 4,18 mm/piksel. Skrip Python membuat topeng lingkaran berdiameter 1 m pada koordinat tiap pohon dari *shapefile* penanaman, sehingga tepi kanopi dihindari, dan ortomosaik dipotong menjadi satu berkas TIF per pohon.

### 4. Set data dan pelatihan detektor
Citra UAV dipotong menjadi 416×416 piksel tanpa perubahan ukuran. Sampel awal 1.000 citra diperbanyak dengan rotasi 90°, 180°, dan 270° serta perubahan kontras dan kecerahan hingga menjadi 3.000 citra. Anotasi kotak pembatas dibuat manual dengan LabelImg dalam format PASCAL VOC. Model yang dipakai adalah Faster R-CNN Inception ResNet V2 Atrous COCO pada TensorFlow Object Detection API dengan *transfer learning*. Pelatihan berjalan di Google Colab pada satu GPU NVIDIA Tesla K80 12 GB selama sekitar 6 jam (di bagian diskusi disebut sekitar 5 jam) hingga nilai fungsi kerugian 0,06, dengan ukuran batch 2 dan laju pembelajaran 0,001.

### 5. Evaluasi dan pembuatan peta
Akurasi deteksi dievaluasi pada 20 potongan citra yang dipilih acak dari ortomosaik. Jumlah buah per citra (Nfp) dihitung manual dengan alat hitung Photoshop. Metrik yang dipakai adalah presisi, *recall*, F1, dan akurasi (TP dibagi Nfp). Regresi linear antara hitungan visual (lapangan dan citra) dan jumlah buah panen dianalisis di RStudio dengan MAE dan RMSE. Peta hasil dibuat dengan QGIS 3.12 dari jumlah buah terdeteksi dan koordinat pohon.

## Eksperimen dan Hasil
Sebaran buah pada 19 pohon sampel (Tabel 1) menunjukkan 175 sampai 308 buah per pohon dengan rerata 255,16 (kolom total pada tabel memuat nilai tertinggi 319 pada pohon nomor 43, sehingga rentang di teks dan tabel tidak sepenuhnya selaras). Rerata persentase buah bagian atas pohon adalah 27,31%, bagian tengah 37,63%, dan bagian bawah 35,06%. Hanya sebagian dari buah bagian atas yang terdeteksi pada citra UAV.

| Perbandingan | n | R² | MAE | RMSE |
|---|---|---|---|---|
| Hitungan visual lapangan terhadap jumlah buah dipanen (Gambar 8; angka dari ringkasan) | 19 pohon | 0,86 | 10,35 | 13,56 |
| Hitungan visual pada citra terhadap jumlah buah dipanen (Gambar 9; angka dari ringkasan) | 19 pohon | 0,80 | 128,56 | 130,56 |

| Metrik deteksi, rerata 20 citra uji (Tabel 2) | Nilai |
|---|---|
| TP rerata | 61,35 |
| FP rerata | 4,40 |
| FN rerata | 6,35 |
| Presisi | 0,93 |
| *Recall* | 0,90 |
| F1 | 0,91 |
| Nfp rerata (hitungan visual pada citra) | 67,70 |
| Akurasi | 0,90 |

Teks hasil menyatakan akurasi 88,96% terhadap hitungan visual, sedangkan Tabel 2 mencantumkan rerata 0,90. Teks juga menyatakan presisi di atas 90% dan F1 di atas 87%, padahal beberapa baris Tabel 2 berada di bawah nilai itu (misalnya presisi 0,83 dan 0,88 pada citra nomor 15 dan 16). Penulis menyebut bahwa hitungan buah pada citra tidak cukup untuk mengestimasi buah lainnya pada kanopi dengan model matematis tradisional, dan bahwa MAE serta RMSE yang tinggi menunjukkan variasi jumlah buah panen tidak dapat dimodelkan dengan baik oleh regresi linear standar.

Peta hasil per pohon (Gambar 11) memperlihatkan variabilitas spasial yang tinggi, dengan 9,12% pohon memiliki 30 sampai 40 buah. Peta per baris (Gambar 12) menunjukkan baris 5 dan 10 berisi buah paling sedikit, baris 1 dan 14 paling banyak, dan baris lain serupa. Waktu komputasi: penyelarasan foto 68 menit, awan titik padat 159 menit, dan pelatihan Faster R-CNN sekitar 5 jam; pelabelan manual memerlukan beberapa hari kerja.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: seluruh alur (persiapan data, deteksi pada citra tergeoreferensi, dan pemetaan) dapat dilakukan pada satu platform Colab yang gratis dan berbasis sumber terbuka, kode disediakan sebagai materi tambahan, dan hasilnya berupa peta hasil yang dapat dipakai untuk mengorganisasi panen. Penulis menyatakan metodenya sebagai yang pertama untuk estimasi hasil kebun berdasarkan jumlah buah terdeteksi pada skala pohon dari citra UAV.

Keterbatasan yang dinyatakan penulis: hanya sebagian buah terlihat dari atas; buah yang tertutup daun atau buah lain sulit dideteksi; positif palsu muncul pada buah hijau belum matang, pada kecerahan matahari tinggi, dan pada citra dengan efek *rolling shutter*; hitungan visual lapangan dipengaruhi gugur buah alami, kesalahan hitung ganda, dan mesin pemilah yang tidak mendeteksi buah kecil; regresi linear tidak memodelkan hubungan hitungan citra dan hasil panen dengan baik; serta pelabelan manual memakan waktu. Penulis juga menyatakan bahwa pengguna akhir yang dituju bukan produsen rata-rata, melainkan layanan koperasi.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Model pelatihan (citra 2019) dan ortomosaik (citra 2018) berasal dari musim berbeda, dan hanya 20 potongan citra yang dipakai untuk uji deteksi tanpa pemisahan yang dirinci dari data pelatihan. Regresi hanya memakai 19 pohon dari satu baris, dengan asumsi jumlah buah per baris konsisten. Deteksi hanya satu kelas (apel) tanpa atribut kematangan. Tidak ada pembanding metode lain, dan MAE serta RMSE pada ringkasan tidak ditampilkan di bagian hasil sehingga tidak dapat dicocokkan dengan gambar dari teks.

## Kaitan dengan Tinjauan main6
Makalah ini tidak memiliki mekanisme eksplisit untuk menyatukan pengamatan buah yang sama dari beberapa pandang. Buah yang terlihat pada beberapa citra UAV yang tumpang tindih ditangani secara tidak langsung: citra dirangkai menjadi satu ortomosaik, lalu buah dideteksi pada satu citra gabungan. Tidak ada pelacakan, pencocokan multi-pandang, atau rekonstruksi 3D tingkat buah. Sisi pohon dan buah di dalam kanopi tidak teramati dan dikoreksi dengan regresi linear terhadap hasil panen.

Hitungan tidak dilaporkan per kelas; hanya satu kelas (apel) yang dideteksi. Acuan hitungnya ada tiga jenis: hitungan visual di lapangan pada 19 pohon, jumlah buah hasil panen manual, dan hitungan visual pada citra untuk evaluasi detektor. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola acuan berlapis (hitung citra, hitung lapangan, dan panen) serta bukti bahwa hitungan satu pandang memerlukan koreksi untuk bagian yang tidak terlihat; mekanisme identitas lintas pandang sendiri tidak disediakan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `apoloapolo2020cloud`.

Ringkasan yang aman dikutip: Apolo-Apolo dkk. (2020) mengestimasi hasil apel per pohon dari citra nadir UAV dengan membangun ortomosaik melalui SfM, memotongnya per pohon, mendeteksi buah dengan Faster R-CNN, dan memetakan hasil per pohon dan per baris pada lingkungan Google Colab. Pada 19 pohon, hitungan buah pada citra dibandingkan dengan jumlah buah dipanen menghasilkan R² 0,80, dan hitungan visual lapangan menghasilkan R² 0,86. Pada 20 citra uji, rerata presisi deteksi 0,93, *recall* 0,90, dan F1 0,91.

Catatan verifikasi data: R², MAE, dan RMSE untuk kedua regresi berasal dari abstrak; bagian hasil hanya memuat R² (Gambar 8 dan 9) dan menilai MAE serta RMSE "tinggi" tanpa angka. Rerata metrik deteksi berasal dari baris "Avg" Tabel 2 dan terbaca utuh pada teks ekstraksi. Angka akurasi 88,96% di teks berbeda dari 0,90 pada Tabel 2. Data Tabel 1 terbaca (rerata 255,16 buah; 27,31%, 37,63%, 35,06%), tetapi judul kolomnya memakai singkatan yang tidak seragam. Jumlah citra 806, 354, dan 452, ukuran lahan, serta waktu komputasi berasal dari bagian metode dan diskusi. Ketinggian terbang tidak konsisten (10 m dan 15 m) dan tidak dapat diverifikasi. Gambar tidak terbaca dari teks. Berkas data tersedia hanya atas permintaan kepada penulis korespondensi.
