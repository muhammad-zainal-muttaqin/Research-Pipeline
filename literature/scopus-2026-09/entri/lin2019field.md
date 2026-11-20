# In-field citrus detection and localisation based on RGB-D image analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2019field` |
| Judul asli | In-field citrus detection and localisation based on RGB-D image analysis |
| Penulis | Lin, Guichao; Tang, Yunchao; Zou, Xiangjun; Li, Jinhui; Xiong, Juntao |
| Tahun | 2019 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [lin2019field.pdf](../pdf/lin2019field.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2019.06.019

## Gambaran Umum

Lin dkk. (2019) menyajikan metode penghitungan dan pelokalisasi buah jeruk (*citrus*) di kebun memakai kamera RGB-D Kinect V2. Penulis mengambil citra di kebun Guangzhou, Tiongkok, pada 4 Desember 2017 dan 11 November 2018 tanpa cahaya buatan. Dari 506 citra RGB-D, sekitar 80% dipakai untuk pelatihan dan sisanya untuk uji. Kumpulan pertama memuat 1.198 buah dan kumpulan kedua 1.991 buah (Tabel 1 di makalah). Evaluasi perbandingan memakai 101 citra dan 637 buah (Tabel 2).

Masalah yang dipecahkan adalah deteksi buah yang saling menempel, tertutup daun, dan terkena sinar matahari. Kamera RGB saja sulit memisahkan buah yang warnanya mirip daun, sehingga penulis menambahkan informasi kedalaman. Kinect V2 memakai prinsip waktu terbang (*time of flight*, TOF) dan menghasilkan peta kedalaman 512×424 piksel. Piksel yang lebih jauh dari 1.800 mm disaring sebelum segmentasi.

Metode ini terdiri dari dua tahap. Pertama, klasifikasi Bayes memisahkan piksel buah dari latar dengan dua campuran Gaussian (*Gaussian mixture model*, GMM) berlima komponen, masing-masing untuk buah dan latar, pada ruang warna RGB. Kedua, piksel yang lolos dikelompokkan dengan metode kepadatan (Rodriguez dan Laio, 2014). Setiap kelompok kemudian diperiksa pengklasifikasi SVM (*support vector machine*) memakai fitur warna, gradien, dan geometri. Kelompok yang lolos diberi koordinat 3D dan diameter.

Hasil utama adalah F1 0,9197 dengan presisi 0,9839 dan recall 0,8634 pada 637 buah (Tabel 2). Galat lokalisasi rata-rata (*mean absolute distance error*, MEDE) pada sumbu x, y, dan z berturut-turut 7,0 mm, 4,0 mm, dan 13,0 mm. Galat ukuran diameter 1,0 mm (Tabel 3, 80 buah). Metode pembanding RegionGrowing mencapai F1 0,6950, EuclidClustering 0,6633, dan metode terdahulu 0,6975. YOLOv3 pada data yang sama mencapai F1 0,9332, lebih tinggi daripada metode usulan. Penulis menilai selisih itu kecil untuk keperluan pertanian.

Waktu pemrosesan 7,92 detik per citra, dengan rata-rata 6,30 buah per citra, atau 1,25 detik per buah yang dilokalisasi. Penulis sendiri menyatakan waktu eksekusi belum memuaskan. Sumber kesalahan yang disebut penulis meliputi buah yang bergabung sehingga recall turun, sinar matahari kuat yang menurunkan presisi kedalaman TOF, dan bias 13 mm pada sumbu z yang dikaitkan dengan galat sistematis Kinect dan galat kalibrasi pose.
