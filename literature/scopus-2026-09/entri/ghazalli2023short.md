# Short Review on Palm Oil Fresh Fruit Bunches Ripeness and Classification Technique

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ghazalli2023short` |
| Judul asli | Short Review on Palm Oil Fresh Fruit Bunches Ripeness and Classification Technique |
| Penulis | Shuwaibatul Aslamiah Ghazalli; Hazlina Selamat; Nurulaqilla Khamis; Mohammad Fadzli Haniff |
| Tahun | 2023 |
| Venue | Journal of Advanced Research in Applied Mechanics |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [ghazalli2023short.pdf](../pdf/ghazalli2023short.pdf)
- DOI resmi: https://doi.org/10.37934/aram.106.1.3747

## Gambaran Umum

Tinjauan singkat ini membahas penentuan tingkat kematangan tandan buah segar kelapa sawit. Mutu minyak dipengaruhi oleh kandungan asam lemak bebas yang rendah, laju ekstraksi minyak yang tinggi, dan tingkat kematangan buah. Tandan yang matang tepat waktu menghasilkan minyak lebih banyak dan bermutu lebih baik, sedangkan tandan mentah menghasilkan minyak paling sedikit dan tandan terlalu matang menghasilkan minyak bermutu rendah. Penilaian kematangan saat ini masih dilakukan secara visual oleh pekerja. Badan Minyak Sawit Malaysia menetapkan dua kriteria, yaitu warna permukaan tandan dan jumlah buah lepas. Penghitungan buah lepas tidak selalu tepat karena buah dapat jatuh di bawah pohon lain, tersangkut di pelepah, hanyut saat hujan, atau dimakan binatang; caranya juga memakan waktu dan tenaga.

Tinjauan ini merangkum kajian sebelumnya, bukan percobaan baru, dan tidak menyatakan strategi pencarian literatur. Kajian dikelompokkan ke dalam tiga teknik, yaitu ekstraksi ciri warna, ekstraksi ciri tekstur, dan pembelajaran dalam. Selain tandan kelapa sawit, kajian perbandingan mencakup mangga, pepaya, pisang, kurma, apel, semangka, dan tomat. kriteria warna membedakan tandan matang berwarna jingga kemerahan, mentah berwarna ungu gelap, kurang matang berwarna jingga setengah, terlalu matang berwarna jingga, dan tandan kosong berwarna cokelat setengah. Pedoman buah lepas menetapkan lebih dari sepuluh buah untuk tandan matang, kurang dari sepuluh untuk kurang matang, tanpa buah lepas untuk mentah, dan lebih dari 50% buah lepas dengan 10% masih menempel untuk terlalu matang.

Mekanisme ekstraksi ciri warna memakai nilai rata-rata kanal RGB atau konversi ke ruang warna lain, seperti HSI, HSV, YCbCr, Lab, XYZ, YIQ, dan YUV. Ekstraksi ciri tekstur memakai analisis wilayah menarik, matriks kookurensi tingkat abu-abu, dan pola biner lokal. Pembelajaran dalam memakai jaringan saraf konvolusional, Residual Network, dan YOLO, yang mengekstraksi ciri warna, tekstur, dan bentuk secara otomatis sehingga pengguna tidak perlu mengekstrak ciri satu per satu.

Angka hasil berikut berasal dari kajian primer yang dirangkum dan dihitung dengan metrik masing-masing, karena tinjauan ini tidak menghasilkan data baru. Konversi HSI menghasilkan akurasi sekitar 70% untuk penilaian tandan sawit. Untuk mangga, HSV menghasilkan akurasi 84,2%, lebih rendah daripada RGB yang mencapai 90,4%, sedangkan kombinasi HSV dengan SVM pada dataset tandan sawit terbatas hanya mencapai 57%. Pada klasifikasi empat tingkat kematangan dengan SVM multiclass, akurasi tiap ruang warna adalah YCbCr 98,9%, YUV 98,9%, Lab 97,2%, HSV 87,2%, XYZ 87,2%, I1I2I3 85,1%, YIQ 85,6%, dan RGB 68,6%. Analisis wilayah menarik dengan KNN maupun ANN menghasilkan akurasi 94%. CNN dengan data akustik pada semangka mencapai 96%, CNN dengan transfer learning ResNet-18 mencapai 98,03%, dan model ResNet terlatih pada dataset Fruit360 mencapai 95,83%. YOLOv3 pada deteksi tomat menurunkan waktu inferensi hingga 5 detik.

Penulis menyatakan sejumlah batasan. Ekstraksi ciri warna paling sederhana, tetapi mengandalkan nilai rata-rata warna sehingga kurang tepat, dan kanal RGB peka terhadap pencahayaan sehingga kurang cocok untuk lingkungan luar ruang. Matriks kookurensi tingkat abu-abu peka terhadap ukuran sampel tekstur, sedangkan pola biner lokal peka terhadap derau. Analisis wilayah menarik memerlukan waktu komputasi tinggi. Pembelajaran dalam lebih cepat dan tangguh, tetapi memerlukan dataset besar, sekitar lebih dari 100 sampel per kelas untuk pelatihan awal. Penulis menyimpulkan bahwa ekstraksi ciri warna paling populer karena kesederhanaannya, tekstur memegang peranan penting menurut pedoman badan minyak sawit, dan pembelajaran dalam paling menjanjikan karena dapat mempelajari ekstraksi ciri langsung dari data.

