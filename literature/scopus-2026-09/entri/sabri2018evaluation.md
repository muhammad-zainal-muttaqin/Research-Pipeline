# Evaluation of color models for palm oil fresh fruit bunch ripeness classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sabri2018evaluation` |
| Judul asli | Evaluation of color models for palm oil fresh fruit bunch ripeness classification |
| Penulis | Sabri, Nurbaity; Ibrahim, Zaidah; Isa, Dino |
| Tahun | 2018 |
| Venue | Indonesian Journal of Electrical Engineering and Computer Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [sabri2018evaluation.pdf](../pdf/sabri2018evaluation.pdf)
- DOI resmi: https://doi.org/10.11591/ijeecs.v11.i2.pp549-557

## Gambaran Umum

Penelitian ini mengevaluasi delapan model warna untuk klasifikasi otomatis tingkat kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyatakan bahwa penentuan tahap panen yang tepat penting untuk mutu dan rendemen minyak, sementara warna merupakan indikator utama kematangan yang digunakan petani. Persoalannya, warna citra dipengaruhi pencahayaan luar ruang yang berubah-ubah, sehingga pemilihan model warna yang tepat menjadi krusial dalam sistem penglihatan mesin. Kajian ini membandingkan model HSV, I1I2I3, LAB, XYZ, YCbCr, YIQ, YUV, dan RGB.

Datanya berupa 500 citra warna TBS yang diambil oleh seorang pakar perkebunan dari perkebunan di Batu Pahat, Johor Darul Takzim, Malaysia. Rinciannya adalah 87 citra terlalu matang (*over-ripe*), 126 citra matang (*ripe*), 109 citra kurang matang (*under-ripe*), dan 147 citra mentah (*unripe*). Citra dipotong secara manual untuk memperoleh daerah minat berupa area TBS sekaligus menghilangkan objek lain, seperti pohon dan daun. Tingkat kematangan mengikuti penetapan Malaysian Palm Oil Board, yakni ungu kehitaman untuk mentah, merah kehitaman untuk kurang matang, merah untuk matang, dan merah jingga untuk terlalu matang.

Mekanisme klasifikasi mencakup akuisisi citra, praproses, transformasi ke delapan model warna, ekstraksi ciri momen warna, lalu klasifikasi. Ciri yang diekstraksi berupa momen pertama (rata-rata), momen kedua (simpangan baku), dan momen ketiga (kemencondongan) untuk setiap kanal warna. Klasifiker yang dipakai adalah *Support Vector Machine* (SVM) multiclass dengan fungsi kernel polinomial, yang memisahkan kelas dengan mencari margin maksimum di sekitar hiperdatar. Ekstraksi ciri dilakukan dengan MATLAB R2016a dan analisis memakai Weka; data dibagi secara acak menjadi 80% latih dan 20% uji.

Tingkat klasifikasi kematangan berturut-turut adalah HSV 87,2%, I1I2I3 85,1%, LAB 97,2%, XYZ 87,2%, YCbCr 98,9%, YIQ 85,6%, YUV 98,9%, dan RGB 68,6%. YCbCr dan YUV menghasilkan tingkat klasifikasi tertinggi dan sama; penulis menyatakan kedua model ini lebih kebal terhadap pencahayaan serta lebih sedikit terpengaruh kilau dan siluet permukaan citra. Kedua model sama-sama salah mengklasifikasikan citra terlalu matang sebagai kurang matang, yang diduga karena jumlah data latih yang tidak seimbang antartahap. RGB tanpa transformasi memberikan hasil terendah karena korelasi tinggi antartahap kematangan. Penulis menyatakan pengembangan aplikasi mobile, penambahan data, serta perbandingan lanjutan atas ciri dan klasifiker masih direncanakan.
