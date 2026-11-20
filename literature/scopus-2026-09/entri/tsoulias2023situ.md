# In-situ fruit analysis by means of LiDAR 3D point cloud of normalized difference vegetation index (NDVI)

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tsoulias2023situ` |
| Judul asli | In-situ fruit analysis by means of LiDAR 3D point cloud of normalized difference vegetation index (NDVI) |
| Penulis | Tsoulias, Nikos; Saha, Kowshik Kumar; Zude-Sasse, Manuela |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tsoulias2023situ.pdf](../pdf/tsoulias2023situ.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107611

## Gambaran Umum

Penelitian ini bertujuan mengukur buah apel langsung di pohon menggunakan *light detection and ranging* (LiDAR). Pengelolaan produksi yang presisi memerlukan informasi jumlah buah, ukuran buah, dan tingkat kematangan. Informasi tersebut dipakai untuk pengaturan beban tanaman, estimasi hasil panen, penentuan waktu panen, dan pemilihan buah oleh robot panen. Metode warna dan spektrofotometri yang ada umumnya harus dilakukan dekat dengan buah dan rentan terhadap kondisi cahaya lapangan. Karena itu, penulis mengusulkan pemindaian laser tanpa kontak yang dapat menghitung buah, mengukur ukurannya, dan menduga klorofil pada kulit buah.

Data penelitian dikumpulkan dari kebun apel dan laboratorium. Di kebun, platform sensor memantau 109 pohon dari kedua sisi satu baris sepanjang 84 m, dan 12 pohon dianalisis dalam penelitian ini. Platform tersebut membawa dua pemindai LiDAR, sebuah *inertial measurement unit* (IMU), dan antena RTK-GNSS. Pengukuran dilakukan pada lima tanggal selama perkembangan buah, yaitu 65 sampai 130 hari setelah bunga mekar penuh (DAFB). Sebagai pembanding, penulis melakukan validasi manual di kebun terhadap 4.632 buah. Di laboratorium, sebanyak 225 buah dianalisis, dan sebagian sampel buah dipindai ulang menggunakan konveyor linear dengan jarak pindai 0,9 m. Sampel referensi dikumpulkan dari 45 buah pada setiap tahap pengukuran untuk analisis kimia dan fisik.

Metode utama mengolah titik awan 3D yang dihasilkan dari kedua pemindai. Reflektansi intensitas dikalibrasi dengan target putih dan hitam, lalu pohon dipisahkan menggunakan silinder yang berpusat pada posisi batang. Buah disegmentasi dari titik awan pohon dan dihitung jumlahnya. Ukuran buah diestimasi dari titik awan dan dibandingkan dengan diameter hasil pengukuran manual. Indeks *normalized difference vegetation index* (NDVI) buah dihitung dari dua panjang gelombang, 660 nm dan 905 nm. Pada tanggal pengukuran terakhir (130 DAFB), jumlah buah mencapai R2 = 0,99 dan ukuran buah mencapai R2 = 0,98 dengan RMSE 3,02 %. NDVI buah mencapai R2 = 0,65 dengan RMSE 0,65 %, dan kandungan klorofil mencapai R2 = 0,78 dengan RMSE 1,31 %. Dalam hasil rinci, nilai F1 deteksi buah berkisar antara 85,7 dan 91,4 pada tanggal 65 sampai 130 DAFB.

Penulis menyatakan beberapa batasan. Ketidakakuratan pengukuran lebih besar pada dua tanggal pertama ketika ukuran buah masih kecil. Pada tahap awal tersebut, hubungan antara diameter LiDAR dan diameter manual juga lebih lemah. Selisah jumlah buah antara hitungan manual dan estimasi juga paling besar pada 65 DAFB, dengan R2 = 0,88 ketika ukuran rata-rata buah 35,5 mm. Hasil per pohon berbeda-beda, meskipun ketepatan hitungan secara keseluruhan tinggi. Penulis menilai pendekatan ini sebagai alat yang berguna untuk memperoleh data tanaman yang relevan bagi produksi, tetapi akurasi per pohon dan per tahap pertumbuhan perlu diperhatikan.
