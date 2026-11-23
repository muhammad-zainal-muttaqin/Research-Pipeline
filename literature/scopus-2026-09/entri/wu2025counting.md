# Counting and Spatial Distribution of Camellia oleifera Fruits Based on YOLO-LGC

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2025counting` |
| Judul asli | Counting and Spatial Distribution of Camellia oleifera Fruits Based on YOLO-LGC |
| Penulis | Wu, D.; others |
| Tahun | 2025 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | camellia |

## Tautan Akses
- PDF: [wu2025counting.pdf](../pdf/wu2025counting.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2025.12.052

## Gambaran Umum

Kajian ini membahas deteksi dan pencacahan buah camellia minyak (*Camellia oleifera*) di kebun. Penulis menyebut penentuan parameter pemetikan sebagai tugas utama sebelum pemetikan mekanis, dan parameter itu bergantung pada deteksi serta pencacahan buah. Kendala yang disebut adalah buah yang saling menutupi, terhalang daun dan ranting, serta cahaya yang berubah. Penulis mengusulkan model YOLO-LGC berbasis YOLO 11n, ditambah pemetaan posisi buah dalam tiga lapisan tinggi (0 sampai 1,5 m, 1,5 sampai 1,8 m, dan di atas 1,8 m).

Data dikumpulkan pada musim matang tahun 2023 sampai 2024 (September sampai November) dari 150 pohon yang dipilih secara acak. Pohon berumur 8 tahun dengan varietas Changlin 1, Zhongke Daguo, dan Xianglin 1, di wilayah barat daya Provinsi Anhui. Citra diambil dengan kamera OAK-D-Pro beresolusi 4032 x 3040 piksel pada berbagai kondisi cahaya. Satu orang pemberi label memberi anotasi memakai RobotFlow. Hasilnya 1.676 citra dengan 8.637 kotak: 1.464 citra latih, 141 citra validasi, dan 71 citra uji (5.799, 1.938, dan 900 kotak). Pembagian per pohon tidak disebut.

Model mengganti blok C3K2 dengan modul LGC (*LNN Ghost dynamic Convolution*), yaitu konvolusi ringan yang memilih ukuran *kernel* secara adaptif. Model memakai PGI (*Programmable Gradient Information*), yaitu mekanisme yang mengatur perambatan gradien selama pelatihan. Model juga memakai *Dynamic UpSample*, yaitu modul pembesaran peta fitur yang menyesuaikan diri terhadap isi citra. Pada tahap deteksi waktu nyata, kamera stereo memberi kedalaman buah. Filter Kalman menghaluskan peta kedalaman dan menggabungkannya dengan data IMU (*inertial measurement unit*, sensor percepatan dan putaran) untuk menaksir tinggi kamera. Setiap buah diberi kubus sumbu-sejajar berjari-jari 20 mm yang berpusat pada koordinat kedalamannya. Uji tabrakan AABB (*axis-aligned bounding box*) antar-bingkai memberi ID kubus lama pada kubus baru yang bertumpang tindih, sehingga buah yang sama tidak dihitung dua kali.

Pada data uji, YOLO-LGC mencapai presisi 83,0%, *recall* 78,0%, dan mAP@0,5 87,6%, dibanding YOLO 11n dengan 82,0%, 76,4%, dan 85,1%. Kecepatan naik dari 229,8 ke 299,7 f/s, dan beban hitung naik dari 5,8 x 10^9 ke 6,7 x 10^9 FLOPs. Pada uji lapangan terhadap empat pohon, jumlah buah terdeteksi dibanding jumlah sebenarnya adalah 193 dan 200 (galat -3,5%), 261 dan 263 (-0,67%), 212 dan 213 (-0,47%), serta 274 dan 286 (-4,19%) (Tabel 5). Penulis menyatakan galat total semua pohon di bawah 5%. Galat per lapisan tinggi lebih besar, misalnya -25,00% pada lapisan rendah pohon pertama (6 terdeteksi dari 8 buah).

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Hanya empat pohon yang dipakai untuk uji hitung. Cara memperoleh jumlah sebenarnya tidak disebut. Pembagian latih, validasi, dan uji tidak dinyatakan per pohon, dan citra uji hanya 71. Satu orang melakukan pelabelan. Tidak ada perbandingan dengan metode pencacahan lain pada pohon yang sama.
