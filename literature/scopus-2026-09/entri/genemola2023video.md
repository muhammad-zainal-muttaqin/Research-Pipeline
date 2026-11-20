# Video-Based Fruit Detection and Tracking for Apple Counting and Mapping

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2023video` |
| Judul asli | Video-Based Fruit Detection and Tracking for Apple Counting and Mapping |
| Penulis | Gen\'e-Mola, Jordi; Felip-Pom\'es, Marc; Net-Barn\'es, Francesc; Morros, Josep-Ramon; Miranda, Juan C.; Arn\'o, Jaume; As\'\in, Lu\'\is; Lordan, Jaume; Ruiz-Hidalgo, Javier; Gregorio, Eduard |
| Tahun | 2023 |
| Venue | 2023 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2023 Proceedings |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2023video.pdf](../pdf/genemola2023video.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor58484.2023.10424135

## Gambaran Umum

Penelitian ini bertujuan menghitung buah secara otomatis untuk memantau produksi, memprediksi hasil panen, dan mengidentifikasi variasi produksi di dalam kebun. Kesulitan utama adalah oklusi buah. Pendekatan yang diusulkan memakai penginderaan banyak pandang dari video bergerak yang direkam saat kamera dijalankan sepanjang barisan pohon. Buah dideteksi pada setiap frame, lalu pelacak multiobjek (MOT) dipakai agar buah yang sama tidak dihitung dua kali. Penelitian membandingkan tiga pelacak, yaitu SORT, DeepSORT, dan ByteTrack, dengan detektor YOLOv5x, lalu menerapkannya untuk memetakan produksi apel pada dua tanggal, yaitu empat minggu dan satu minggu sebelum panen.

Data berasal dari kebun apel eksperimen varietas Story ® Inored di Mollerussa, Catalonia, Spanyol. Pohon ditanam dengan sistem *tall spindle*, jarak tanam 3,6 m × 1 m, dan tinggi kanopi maksimum 3,5 m. Sistem perekam terdiri atas kamera Kinect Azure DK yang disinkronkan dengan sensor GNSS Ardusimple simpleRTK2B, dipasang pada tiang di bagian belakang kendaraan segala medan listrik dan dikendalikan dengan perangkat lunak AK_ACQS. Kebun terdiri atas empat barisan sepanjang 105 meter dengan 420 pohon. Setiap barisan dibagi menjadi 21 segmen sepanjang 5 meter, sehingga total 84 segmen. Panen dilakukan pada 5 Oktober 2021. Acuan hitung jumlah buah per segmen diperoleh dengan memanen setiap segmen dan menghitung buah memakai mesin pemilah apel komersial Maf Roda Agrobotic.

Kebun dipindai dua kali, pada 6 September 2021 saat apel berwarna merah muda dan hijau, serta pada 28 September 2021 saat apel berwarna merah penuh. Kendaraan bergerak pada kecepatan 0,556 m/s dengan jarak sensor 2,25 m dari sumbu barisan, dan setiap pohon dipindai dua kali dari sisi timur dan barat. Video direkam pada 30 frame per detik. Untuk latihan dan validasi, 1.087 frame dari segmen 5 dan 6 barisan 2 dianotasi secara manual dengan kotak dan nomor identitas apel memakai Supervisely. YOLOv5x yang telah dilatih awal pada COCO disesuaikan dengan data tersebut memakai SGD, laju pembelajaran 0,01, dan ukuran batch 4. SORT memakai Kalman Filter dan Hungarian Algorithm; DeepSORT menambah deskriptor penampakan dari jaringan re-identifikasi dengan metrik cosine serta ambang skor 0,7; ByteTrack menambah tahap asosiasi kedua untuk deteksi berskor rendah guna mengatasi oklusi parsial.

Penghitungan per segmen menjumlahkan buah yang terlacak dari sisi timur dan barat, lalu memasukkan jumlah itu ke model linear f(x,β)=β0+β1x. Pengujian memakai validasi silang per barisan: koefisien untuk suatu barisan diperoleh dari barisan lainnya. Deteksi dinilai dengan precision, recall, F1, dan mAP; pelacakan dengan MOTA, IDF1, dan HOTA; penghitungan dengan MAE, MBE, MAPE, RMSE, dan R². YOLOv5x mencapai F1 0,834 dan mAP 0,871 setelah 273 epoch. ByteTrack memberi MOTA 0,6817, IDF1 0,8369, HOTA 0,6894, dan waktu 15,4 ms per citra; SORT berturut-turut 0,6401, 0,8091, 0,6804, dan 15,3 ms; DeepSORT 0,5735, 0,7646, 0,6824, dan 128,0 ms.

Pada pemindaian 6 September 2021, sistem memberi MAE 38,43, MBE −0,20, MAPE 8,45% (±0,8% SE), RMSE 49,04, dan R² 0,66. Pada 28 September 2021, MAE turun menjadi 34,98, MBE 0,15, MAPE 7,47% (±0,6% SE), RMSE 45,64, dan R² naik menjadi 0,70. Peta hasil prediksi juga menunjukkan zona produksi tinggi di bagian selatan dan rendah di bagian utara kebun. Penulis menyebut keterbatasan berupa acuan hitung yang hilang untuk segmen 4, 5, dan 6 barisan 2 serta segmen 4 barisan 4 akibat kesalahan akuisisi. Fitur penampakan pada DeepSORT tidak meningkatkan pelacakan karena apel memiliki penampakan yang saling mirip. Penulis menganjurkan penyempurnaan pelacak serta pengkajian kondisi pemindaian, seperti pencahayaan, kecepatan kendaraan dan akuisisi, orientasi kamera, dan sudut pandang, serta pengujian pada varietas buah lain dengan penampakan berbeda.
