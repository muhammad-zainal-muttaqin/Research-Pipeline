# Oil palm fruit ripeness detection using K-Nearest neighbour

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `astuti2019oil` |
| Judul asli | Oil palm fruit ripeness detection using K-Nearest neighbour |
| Penulis | Astuti, I F; Nuryanto, F D; Widagdo, P P; Cahyadi, D |
| Tahun | 2019 |
| Venue | Journal of Physics Conference Series |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [astuti2019oil.pdf](../pdf/astuti2019oil.pdf)
- DOI resmi: https://doi.org/10.1088/1742-6596/1277/1/012028

## Gambaran Umum

Studi ini membangun alat untuk memeriksa tingkat kematangan buah kelapa sawit dari citra. Petani sering tidak mengetahui warna buah yang menandakan kematangan optimal untuk dipanen, dan penilaian tingkat kematangan hanya dapat dilakukan oleh ahli. Karena itu penulis membangun sistem pakar berbasis pengolahan citra. Sistem ini memakai metode *K-Nearest Neighbor* (KNN), yaitu klasifikasi yang menentukan kelas suatu data dari mayoritas tetangga terdekatnya, untuk menentukan kelas kematangan dari citra yang dimasukkan pengguna.

Data yang dipakai berasal dari buah sawit varietas Tenera yang dibudidayakan di Kalimantan Timur. Sebanyak 80 citra latih dibagi ke tujuh tingkat kematangan: sangat mentah (F00), mentah (F0), belum berkembang penuh (F1), dua tingkat matang (F2 dan F3), dan dua tingkat terlalu matang (F4 dan F5). Setiap citra diubah ukurannya menjadi 300×300 piksel. Pengujian memakai tujuh citra uji, masing-masing satu untuk setiap tingkat kematangan, dan ketujuh citra itu tidak termasuk data latih.

Setiap citra diubah ukurannya dengan *bicubic interpolation* (interpolasi bikubik), lalu tepinya dideteksi dengan *Sobel edge detection*. Dari citra tepi tersebut dihitung nilai fitur: rerata, simpangan baku, *skewness* (tingkat kemiringan distribusi intensitas), *entropy* (ukuran keacakan distribusi intensitas), *energy*, intensitas, *contrast*, dan *homogeneity*. Sistem menghitung jarak Euclidean antara fitur citra uji dan setiap citra latih, lalu memilih kelas dari tetangga terdekat. Pada satu contoh, sistem menghasilkan tingkat F2 yang oleh penulis disebut matang cukup. Hasil utama studi dinyatakan sebagai efektivitas dan akurasi deteksi sebesar 65% dengan penerapan Sobel edge detection.

Penulis menyatakan bahwa metode KNN dengan Sobel edge detection dapat menjadi salah satu solusi untuk membantu petani memanen pada kematangan optimal. Batasan yang dinyatakan dalam teks berkaitan dengan cakupan data: sistem hanya menghitung nilai fitur dari warna buah pada varietas Tenera yang dibudidayakan di Kalimantan Timur. Ukuran citra juga tetap, yaitu 300×300 piksel. Angka 65% adalah satu-satunya ukuran hasil yang dinyatakan dalam kesimpulan, dan hasil itu diperoleh dari pengujian dengan tujuh citra uji.
