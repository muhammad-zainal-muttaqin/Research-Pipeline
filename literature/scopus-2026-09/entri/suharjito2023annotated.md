# Annotated Datasets of Oil Palm Fruit Bunch Piles for Ripeness Grading Using Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `suharjito2023annotated` |
| Judul asli | Annotated Datasets of Oil Palm Fruit Bunch Piles for Ripeness Grading Using Deep Learning |
| Penulis | Suharjito; Junior, Franz Adeta; Koeswandy, Yosua Putra; Debi; Nurhayati, Pratiwi Wahyu; Asrol, Muhammad; Marimin |
| Tahun | 2023 |
| Venue | Scientific Data |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [suharjito2023annotated.pdf](../pdf/suharjito2023annotated.pdf)
- DOI resmi: https://doi.org/10.1038/s41597-023-01958-x

## Gambaran Umum

Artikel ini adalah deskriptor data yang menyajikan himpunan data tandan buah segar kelapa sawit dalam bentuk tumpukan di pabrik pengolahan. Penulis menyatakan bahwa mutu minyak sawit ditentukan oleh tingkat kematangan buah, sementara kajian sebelumnya memakai citra tandan dengan kategori tidak lengkap dan variasi yang terbatas sehingga tidak mencerminkan kondisi nyata di pabrik. Penilaian kematangan secara visual juga bergantung pada persepsi pengamat, sulit dilakukan pada pohon tinggi, dan menunggu buah rontok dapat menimbulkan kehilangan panen. Tujuan penelitian adalah menyediakan himpunan data video dan citra yang diambil langsung dari pabrik dengan enam kategori sesuai kondisi bagian grading, serta divalidasi oleh pakar penentu kematangan di pabrik.

Data direkam di beberapa pabrik sawit di Kalimantan Selatan, pada bagian grading, di atas lantai beton halaman belakang pabrik. Pengambilan memakai telepon genggam dengan format MP4 beresolusi 1280×720 piksel. Kamera diputar 360° mengelilingi tumpukan tandan agar berbagai posisi terekam. Rekaman dilakukan antara pukul 12.00 dan 13.00 pada cuaca cerah; karena cuaca tidak selalu cerah, pengumpulan memakan waktu sekitar dua bulan. Himpunan data terdiri atas 45 video satu kategori dan 56 video yang memuat beberapa kategori dalam satu video, dengan durasi sekitar 10–15 detik per video. Enam kategori yang dipakai adalah unripe, under-ripe, ripe, overripe, empty bunch, dan abnormal fruit.

Praproses mengubah video menjadi citra berurutan memakai VLC Media Player dengan rasio 30, yaitu satu frame per detik untuk mengurangi redundansi. Citra hasil ekstraksi beresolusi 416×416 piksel. Anotasi kotak pembatas dilakukan manual dengan DarkLabel dan disimpan dalam format YOLO berupa berkas .txt yang memuat [id kelas, x, y, w, h]; setiap kelas disimpan pada berkas terpisah. Data selanjutnya diolah dengan Roboflow. Tabel 2 mencatat total 7.171 citra dan 14.559 objek, dengan rincian unripe 1.130 citra/2.913 objek, under-ripe 1.289/2.575, ripe 1.880/2.974, over ripe 1.162/2.641, empty bunch 473/857, dan abnormal 1.237/2.599. Pembagian data latih, validasi, dan uji adalah 70:20:10, yaitu 2.908, 835, dan 417 citra. Penulis menyatakan data tersedia di Science Data Bank.

Validasi teknis memakai tiga varian YOLOv4 dengan masukan 320, 416, dan 512 piksel. Konfigurasi pelatihan sama untuk ketiganya: batch 64, subdivisi 16, tiga kanal, momentum 0,949, decay 0,0005, learning rate 0,001, burn-in 1.000, maksimum 12.000 batch, langkah penurunan laju pada 9.600 dan 10.800 dengan faktor 0,1. Metrik yang dilaporkan adalah presisi, recall, F1-score, dan rata-rata IoU pada data uji. YOLOv4-320 memperoleh presisi 0,99, recall 1,00, F1 0,99, dan IoU 88,01% dengan 1.406 true positive, 20 false positive, dan 4 false negative. YOLOv4-416 memperoleh 0,97, 1,00, 0,98, dan 88,27% dengan 1.404/37/6. YOLOv4-512 memperoleh 0,99, 1,00, 0,99, dan 88,94% dengan 1.408/20/2. Penulis menyatakan loss validasi konvergen ke nol dan nilai mAP mendekati 1.

Batasan yang dinyatakan penulis mencakup ketidakseimbangan jumlah citra antarkelas karena tandan abnormal dan empty bunch sulit diperoleh dari pengiriman ke pabrik, serta belum dilakukannya augmentasi data. Penulis juga mencatat bahwa latar halaman belakang pabrik lebih sederhana daripada latar kebun, sehingga deteksi langsung di perkebunan dapat menurun. Penggunaan video membuat praproses lebih sulit dan waktu pelatihan lebih lama dibandingkan citra diam. Artikel ini menyediakan data untuk deteksi, klasifikasi, dan penghitungan buah, tetapi tidak melaporkan eksperimen penghitungan tandan atau asosiasi antarpandangan.

