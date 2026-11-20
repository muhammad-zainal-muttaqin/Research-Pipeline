# Palm Oil Maturity Classification Using K-Nearest Neighbors Based on RGB and L*a*b Color Extraction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saifullah2023palm` |
| Judul asli | Palm Oil Maturity Classification Using K-Nearest Neighbors Based on RGB and L*a*b Color Extraction |
| Penulis | Saifullah, Shofan; Prasetyo, Dessyanto Boedi; Indahyani; Dre\.zewski, Rafa\l; Dwiyanto, Felix Andika |
| Tahun | 2023 |
| Venue | Procedia Computer Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [saifullah2023palm.pdf](../pdf/saifullah2023palm.pdf)
- DOI resmi: https://doi.org/10.1016/j.procs.2023.10.294

## Gambaran Umum

Penelitian ini bertujuan mengklasifikasikan tingkat kematangan kelapa sawit berdasarkan citra. Tingkat kematangan menentukan kualitas minyak sawit mentah yang dihasilkan. Pada praktiknya, pemilahan masih dilakukan secara manual dengan penilaian visual. Cara ini rawan kesalahan karena keterbatasan penglihatan manusia, dan prosesnya memakan waktu. Penulis karena itu mengusulkan deteksi otomatis berbasis pembelajaran mesin. Penulis memilih metode *K-Nearest Neighbors* (KNN) dan menguji dua jenis fitur warna, yaitu RGB dan L\*a\*b. Penulis juga menyatakan bahwa RGB pada penelitian sebelumnya hanya mencapai akurasi 68,8 persen, sehingga penelitian ini menambahkan praprosesan untuk memisahkan objek dari latar belakang.

Data terdiri atas 150 foto kelapa sawit yang diambil dengan kamera *smartphone* Vivo Y15 dalam format JPG. Setiap kelas berisi 50 citra, yaitu matang (*ripe*), *intermediate*, dan *unripe*. Citra awalnya memiliki ukuran yang beragam, lalu diubah ukurannya menjadi 300 × 500 piksel untuk mempercepat pemrosesan. Segmentasi dengan ambang batas membuat latar belakang menjadi putih. Objek kemudian dipotong menjadi 90 × 70 piksel untuk mengambil ciri warnanya. Teks tidak menyebutkan jumlah atau kondisi kebun asal buah. Pembagian data latih dan uji juga tidak dinyatakan dalam rasio. Penulis menggunakan *k-fold cross-validation* dengan K = 5, yaitu empat bagian untuk latih dan satu bagian untuk uji pada setiap iterasi.

Fitur dihitung dari nilai rata-rata setiap kanal warna pada citra. Untuk RGB, fitur diambil dari kanal merah, hijau, dan biru. Untuk L\*a\*b, citra dikonversi terlebih dahulu sebelum dihitung nilai rata-ratanya. Penulis menguji nilai K dari 1 sampai 9 dengan jarak Euclidean. Model KNN-RGB mencapai akurasi terbaik 97,77 persen pada K = 5, dengan rata-rata akurasi 95,4 persen. Model KNN-L\*a\*b juga mencapai akurasi terbaik 97,77 persen, tetapi rata-rata akurasinya 97,4 persen. Penulis melaporkan bahwa L\*a\*b unggul 2 sampai 4,8 poin persentase dibanding RGB dalam akurasi model. Penulis juga menyatakan bahwa akurasi RGB terendah disebabkan kurangnya pencahayaan saat akuisisi citra.

Penulis menyatakan bahwa fitur RGB rentan terhadap perubahan cahaya, sehingga hasilnya dapat turun pada kondisi pencahayaan yang kurang. Penulis menilai fitur L\*a\*b lebih tahan terhadap cahaya yang dipantulkan objek karena konversi warnanya tidak terpengaruh cahaya. Keterbatasan lain tidak dinyatakan secara eksplisit dalam bagian yang dibaca. Hasil ini diperoleh pada 150 citra dengan satu jenis kamera, sehingga generalisasinya ke kondisi kebun dan kamera lain belum diuji.
