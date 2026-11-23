# Machine vision for counting fruit on mango tree canopies

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qureshi2017machine` |
| Judul asli | Machine vision for counting fruit on mango tree canopies |
| Penulis | Qureshi, W. S.; Payne, A.; Walsh, K. B.; Linker, R.; Cohen, O.; Dailey, M. N. |
| Tahun | 2017 |
| Venue | Precision Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [qureshi2017machine.pdf](../pdf/qureshi2017machine.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-016-9458-5

## Gambaran Umum

Qureshi dkk. (2017) menyebut estimasi hasil buah di kebun masih bergantung pada hitung tangan pada sebagian pohon. Cara itu lambat dan rawan galat. Penulis mengusulkan dua metode baru untuk mencacah mangga pada citra kanopi pohon, yaitu segmentasi padat berbasis tekstur dan deteksi berbasis bentuk. Keduanya dibandingkan dengan dua metode yang sudah ada pada set citra yang sama.

Data berupa citra kanopi mangga (*Mangifera indica*) yang diambil malam hari dengan kamera Canon 50D dan lampu sorot, resolusi 4752 x 3168 piksel. Pengambilan berlangsung selama tiga musim di beberapa kebun, pada jarak 2 sampai 4 m dari batang. Set kalibrasi berisi 20 citra dari 18 pohon dengan 705 buah. Ada beberapa set validasi, misalnya Validation 0 dengan 80 citra dan 2.464 buah. Pelabelan memakai fitur hitung Photoshop. RMSE hitung tangan oleh dua operator pada set kalibrasi adalah 3,3 buah per citra.

Empat metode dibandingkan. Metode A memakai tapis warna dan kehalusan serta pelabelan blob. Metode B memakai klasifikasi piksel *KNN* (*k-nearest neighbour*, klasifikasi menurut tetangga terdekat) lalu model bentuk elips untuk buah. Metode C memakai *superpixel* (kelompok piksel serupa), fitur *SIFT* padat yang dikelompokkan menjadi kata visual, dan klasifikasi *SVM* (*support vector machine*), disusul tapis warna. Metode D menjalankan C lalu A. Parameter hanya dioptimalkan pada set kalibrasi.

Pada citra dengan kondisi sama seperti kalibrasi, jumlah buah terestimasi berada dalam 16% dari jumlah sebenarnya dan F1 deteksi di atas 0,68. Contohnya pada set kalibrasi, F1 metode A 0,80, B 0,83, C 0,83, D 0,80, dengan R2 0,67, 0,56, 0,72, dan 0,74. Pada Validation 3B, F1 turun menjadi 0,46 (A), 0,66 (B), 0,67 (C), dan 0,41 (D). Hasil lebih buruk bila bentuk kanopi atau kondisi pencitraan berbeda. Penulis menyarankan pencitraan malam dengan pencahayaan tetap.

Keterbatasan dapat diperiksa dari teks. Metrik deteksi dihitung pada 20 citra pertama untuk sebagian set besar, bukan semua citra. Tidak ada pembagian per pohon yang dinyatakan terpisah dari kalibrasi untuk set Validation 1, yang berisi pohon sama dengan kalibrasi pada malam berbeda. Buah dihitung per citra, termasuk buah dari tajuk tetangga, dan tidak ada penautan buah antarcitra pohon yang sama. Kondisi di luar pencitraan malam tidak diuji.
