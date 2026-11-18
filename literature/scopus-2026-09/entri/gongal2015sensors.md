# Sensors and systems for fruit detection and localization: A review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gongal2015sensors` |
| Judul asli | Sensors and systems for fruit detection and localization: A review |
| Penulis | Gongal, A.; Amatya, S.; Karkee, M.; Zhang, Q.; Lewis, K. |
| Tahun | 2015 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple, citrus, pear |

## Tautan Akses
- PDF: [gongal2015sensors.pdf](../pdf/gongal2015sensors.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2015.05.021

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang sensor dan sistem untuk deteksi dan pelokalan buah guna pemanenan robotik serta perkiraan beban panen pada tanaman buah khusus. Masalah utamanya adalah pemanenan manual yang padat karya, mahal, dan berisiko cedera, sehingga diperlukan sistem otomatis. Penulis menegaskan bahwa deteksi dan pelokalan buah merupakan informasi paling dasar bagi pemanen berbasis penglihatan mesin, karena keakuratan keduanya menentukan keberhasilan pemanenan dan perkiraan hasil. Karena berupa tinjauan, artikel ini tidak menyajikan eksperimen baru; seluruh angka hasil berasal dari kajian yang ditinjau.

Tanaman yang dibahas terutama apel, pir, dan sitrus, dengan bahasan tambahan pada persik, tomat, mangga, nanas, blewah, dan kiwi. Data berupa citra buah di kebun, baik siang maupun malam, dari kamera digital maupun platform bergerak. Sensor yang ditinjau terdiri atas kamera hitam-putih, kamera warna (CCD/CMOS), kamera spektral (multispektral dan hiperspektral), serta kamera termal. Fitur yang dipakai mencakup warna, bentuk dan ukuran geometris, tekstur, atau gabungannya. Metode klasifikasi meliputi K-means, KNN, pengklasifikasi Bayes, jaringan saraf tiruan, dan mesin vektor pendukung (SVM). Untuk pelokalan, penulis mengkaji kamera tunggal, penentu jarak laser, stereovisi, dan kamera tiga dimensi berbasis *time-of-flight* (TOF).

Mekanisme deteksi mengikuti rangkaian akuisisi citra, prapengolahan (misalnya konversi ke ruang warna HSI/HSV dan ekualisasi histogram), segmentasi buah, penyaringan derau, operasi morfologi, pelabelan, ekstraksi fitur, dan pada beberapa kajian diikuti klasifikasi serta penghitungan. Segmentasi memisahkan buah dari daun, ranting, dan latar belakang memakai ambang warna, perbedaan kanal, tekstur Gabor, transformasi *Hough* lingkaran, atau analisis komponen utama (PCA). Mekanisme pelokalan mengubah posisi dua dimensi buah menjadi koordinat tiga dimensi melalui triangulasi kamera tunggal, visual servoing dengan penentu jarak laser, pencocokan stereovisi berbasis disparitas, atau peta jarak segera dari kamera TOF. Koordinat tiga dimensi ini juga dipakai untuk mengenali buah yang sama yang muncul berulang pada citra dari sisi berlawanan, sehingga tidak dihitung dua kali.

Angka hasil yang dikutip mencakup beragam metrik dengan acuan hitung yang berbeda-beda. Secara agregat, akurasi deteksi buah sitrus dan apel berada pada kisaran 70–92%, dengan angka tertinggi 92% untuk apel merah memakai kamera warna dan SVM berkernel RBF pada 150 citra contoh dengan fitur warna dan bentuk terintegrasi (Ji dkk. 2012). Ringkasan tabel penulis menunjukkan akurasi 80–85% untuk fitur warna, 68–75% untuk fitur geometris, 75,3–85% untuk tekstur, dan 87–90% untuk gabungan fitur; untuk metode klasifikasi, K-means 53–80%, Bayes 75%, KNN 85–90%, jaringan saraf 61–84%, dan SVM 92–93%. Contoh perhitungan spesifik meliputi akurasi 90% pada jeruk yang terlihat dengan tingkat deteksi palsu 4% (Hannan dkk. 2010), peningkatan dari 58% memakai warna dan 74% memakai bentuk menjadi 87% tanpa deteksi palsu saat keduanya digabung (Jiménez dkk. 1999b), serta koefisien regresi 0,80 untuk apel hijau muda dan 0,85 untuk apel merah matang antara hitungan otomatis dan manual (Zhou dkk. 2012). Pada citra hiperspektral, segmentasi buah mencapai 88,1% (Safren dkk. 2007), sedangkan kamera termal menghasilkan koefisien regresi maksimum 0,88 untuk apel matang (Stajnko dkk. 2004). Untuk pelokalan, kamera tunggal mencapai galat sekitar 15 mm (Mehta & Burks 2014), penentu jarak laser mencapai ±3 mm (Bulanon dkk. 2010), dan kamera TOF mencapai 87% dalam mengenali apel yang muncul berulang (Gongal dkk. 2015).

Batasan yang dikemukakan penulis mencakup oklusi oleh daun dan ranting, pengelompokan buah, serta kondisi pencahayaan yang berubah-ubah sebagai hambatan utama deteksi dan pelokalan. Kamera hitam-putih tidak menyediakan informasi warna; kamera warna sensitif terhadap pencahayaan dan kesulitan membedakan buah hijau dari daun; pencitraan spektral mahal dan lambat; kamera termal dipengaruhi ukuran buah serta paparan sinar matahari langsung; stereovisi kompleks dan lambat; sementara kamera TOF beresolusi rendah dan mahal. Penulis juga mencatat bahwa akurasi lokasi absolut jarang dilaporkan dan perbandingan kinerja antarteknik dalam lingkungan luar ruang yang sama belum tersedia. Metode pembelajaran terselia meningkatkan kompleksitas sistem serta memerlukan sampel latih yang cukup dan tepat. Hingga artikel ini ditulis, belum ada sistem robotik yang dikomersialkan untuk pemanenan buah pohon segar karena keterbatasan ketahanan, kecepatan, dan biaya; sistem pemanen kiwi yang paling berhasil sekalipun hanya mencapai kecepatan satu buah per detik.

