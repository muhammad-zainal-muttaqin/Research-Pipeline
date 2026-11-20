# A performance comparison of RGB, NIR, and depth images in immature citrus detection using deep learning algorithms for yield prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `choi2017performance` |
| Judul asli | A performance comparison of RGB, NIR, and depth images in immature citrus detection using deep learning algorithms for yield prediction |
| Penulis | Choi, Daeun; Lee, Won Suk; Schueller, John K.; Ehsani, Reza; Roka, Fritz; Diamond, Justice |
| Tahun | 2017 |
| Venue | 2017 Asabe Annual International Meeting |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [choi2017performance.pdf](../pdf/choi2017performance.pdf)
- DOI resmi: https://doi.org/10.13031/aim.201700076

## Gambaran Umum

Kajian ini membandingkan tiga jenis citra dari kamera Kinect v2 untuk mendeteksi buah jeruk pada pohon. Tujuannya adalah memperkirakan hasil panen dari jumlah buah yang terlihat. Ketiga jenis citra itu adalah RGB (warna), NIR (inframerah dekat), dan depth (kedalaman). Deteksi dilakukan dalam dua tahap: lingkaran kandidat dicari lebih dahulu, lalu setiap kandidat diklasifikasikan sebagai jeruk atau latar belakang.

Data yang dipakai terdiri atas 255 citra untuk setiap jenis citra. Citra dibagi secara acak menjadi 195 citra latih, 30 citra uji, dan 30 citra validasi. Pada citra validasi, setiap jenis data memuat 492 buah jeruk.

Untuk tahap pencarian kandidat, penulis memakai Circular Hough Transform (CHT) pada citra RGB dan NIR, serta estimasi lingkaran berbasis depth (CHOICE) pada citra depth. Tahap klasifikasi memakai AlexNet dengan transfer learning sebagai pengklasifikasi biner, dilatih terpisah untuk setiap modalitas. Hasil diukur dengan tingkat positif sejati (true positive rate), tingkat negatif palsu, tingkat positif palsu, dan rasio antara positif sejati dan positif palsu.

Citra NIR memberi hasil terbaik. Penulis melaporkan tingkat positif sejati 96% untuk deteksi lingkaran dan klasifikasi. Rasio positif sejati terhadap positif palsu adalah 1:1,1, yang berarti jumlah positif palsu hampir sama dengan jumlah positif sejati. Citra RGB dan depth menghasilkan lebih banyak positif palsu pada tahap deteksi. Akibatnya, tingkat positif palsu pada tahap klasifikasi juga lebih tinggi daripada NIR.

Penulis juga mencatat keterbatasan. Citra depth memuat derau akibat sinar matahari. Penulis mengusulkan faktor toleransi untuk mengabaikan derau itu sebagai pekerjaan lanjutan, bersama implementasi waktu nyata dan integrasi dengan kendaraan tanpa awak (UAV dan UGV). Kajian ini tidak membahas penggabungan hitungan antarpandang, sehingga setiap citra dihitung secara terpisah.
