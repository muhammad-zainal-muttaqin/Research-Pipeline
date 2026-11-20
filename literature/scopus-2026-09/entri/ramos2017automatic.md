# Automatic fruit count on coffee branches using computer vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ramos2017automatic` |
| Judul asli | Automatic fruit count on coffee branches using computer vision |
| Penulis | Ramos, P.J.; Prieto, F.A.; Montoya, E.C.; Oliveros, C.E. |
| Tahun | 2017 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | coffee |

## Tautan Akses
- PDF: [ramos2017automatic.pdf](../pdf/ramos2017automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2017.03.010

## Gambaran Umum

Panen kopi sulit diperkirakan sejak awal siklus. Petani biasanya mengandalkan pengalaman, sedangkan penghitungan buah yang paling andal memerlukan pengambilan sampel secara destruktif dan banyak tenaga kerja. Penelitian ini mengusulkan metode tanpa perusakan untuk menghitung jumlah buah pada satu cabang kopi. Sistem juga memperkirakan persentase kematangan dan berat buah. Dengan informasi ini, petani dapat merencanakan kebutuhan pekerja, fasilitas pascapanen, dan pemeliharaan mesin sebelum panen.

Data penelitian terdiri atas 1018 cabang kopi *Coffea arabica* dari varietas Castillo dan Caturra. Cabang dikumpulkan pada beberapa periode, dari Desember 2013 sampai Juli 2016. Citra diambil dengan kamera utama ponsel Samsung Galaxy S5 dari jarak 8 sampai 15 cm, tanpa *flash*, dan tanpa pengendalian pencahayaan. Setiap cabang difoto 3 sampai 5 kali agar seluruh *glomerulus* terekam, sehingga tersedia 4300 citra. Untuk membangun model linear, digunakan 90 cabang dengan 409 citra. Model itu kemudian dievaluasi pada 45 cabang dan divalidasi pada 940 cabang dari empat plot kopi varietas Castillo.

Sistem mengolah citra dalam lima tahap. Tahapnya meliputi penyesuaian citra, segmentasi wilayah bertekstur, deteksi kontur yang berupa busur buah, penyesuaian elips, dan klasifikasi. Klasifikasi membedakan buah menurut tingkat kematangan. Tingkat keberhasilan keseluruhan adalah 88,02% untuk SVM, 83,09% untuk KNN, dan 83,5% untuk Bayes. Buah dikelompokkan menjadi buah matang dan lewat matang, buah setengah matang, dan buah belum matang. Untuk kelompok matang dan lewat matang, serta kelompok belum matang, model linear satu-ke-satu memiliki koefisien determinasi di atas 0,93. Selisih absolut berkisar 8,5 sampai 17 buah, atau galat 18% sampai 33% terhadap rata-rata buah yang diamati. Kelompok setengah matang tidak lolos kriteria, dengan R² 0,356 dan intersep yang tidak sama dengan nol. Dibandingkan penelitian Stajnko dan Nuske, koefisien determinasi penelitian ini lebih tinggi dari 0,935, sedangkan pembanding hanya 0,60. Rata-rata selisih absolut sebesar 13,8 buah per cabang. Persentase kematangan rata-rata per cabang berada pada rentang 22,27% sampai 30,9% dengan tingkat kepercayaan 95%. Jumlah buah per cabang berada pada rentang 19,63 sampai 100,04.

Penulis menyatakan beberapa batasan. Citra dengan fokus kurang, cahaya matahari langsung atau tersaring, dan goyangan kamera menghasilkan galat hitung lebih dari 6%. Oklusi oleh daun dan buah lain, kelengkungan cabang, bagian sisi citra yang kabur, serta gerakan saat pengambilan gambar juga menurunkan akurasi. Pengambilan citra saat hujan juga menimbulkan kendala, misalnya tetesan air pada layar. Penulis menyarankan pengembangan algoritma deteksi untuk mengurangi selisih absolut. Penulis juga menyarankan aplikasi seluler untuk memeriksa kualitas citra dan mengontrol pengambilan gambar di lapangan.
