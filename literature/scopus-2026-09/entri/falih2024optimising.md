# Optimising Yield Estimation for Grapes: Utilising the Sliding Window Technique for Visual Counting of Bunches and Berries

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `falih2024optimising` |
| Judul asli | Optimising Yield Estimation for Grapes: Utilising the Sliding Window Technique for Visual Counting of Bunches and Berries |
| Penulis | Falih, B.S.; others |
| Tahun | 2024 |
| Venue | Pakistan Journal of Agricultural Sciences |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [falih2024optimising.pdf](../pdf/falih2024optimising.pdf)
- DOI resmi: https://doi.org/10.21162/pakjas/24.46

## Gambaran Umum

Studi ini membahas penghitungan buah dan tandan anggur dari citra RGB tunggal, dengan tujuan memperkirakan hasil panen (*yield estimation*) sebelum panen. Penulis menggabungkan segmentasi warna, pencarian *sliding window* dengan fitur HOG (*Histogram of Oriented Gradients*), dan pengelompokan DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*) untuk memisahkan tandan yang berdekatan. Hasil utamanya adalah akurasi hitung buah rata-rata 83,73% dan akurasi hitung tandan rata-rata 94,66%.

Segmentasi memisahkan piksel anggur dari latar belakang dengan *k-means*, yaitu pengelompokan warna tanpa label. Detektor kaskade dengan sepuluh rangkaian pengklasifikasi kemudian memindai citra dengan jendela geser dan menandai kandidat buah. Kandidat yang berdekatan dikelompokkan dengan DBSCAN sehingga satu tandan dihitung sebagai satu kelompok. Penghitungan dilakukan terpisah untuk anggur merah dan putih.

Data uji terdiri dari enam citra anggur merah (CU Red), tiga citra dari Tarsus, dan empat citra anggur putih (CU White). Pada hitung buah, akurasi anggur merah 92,82% ± 0,96% dan anggur putih 76,71% ± 1,99%. Pada hitung tandan, akurasi anggur merah 96,5% ± 2,12% dan anggur putih 90,75% ± 2,47%. Pada tingkat piksel, akurasi 93,76%, sensitivitas 97,92%, spesifisitas 66,99%, PPV 94,99%, dan NPV 84,45%. Angka spesifisitas dan akurasi piksel ikut terdorong oleh piksel latar belakang yang benar (TN), sehingga angka piksel kurang mencerminkan kualitas hitung buah.

Studi ini menghitung buah dari satu sudut pandang per citra dan tidak memakai data kedalaman.

Keterbatasan yang dinyatakan penulis mencakup akurasi lebih rendah pada anggur putih karena warna daun dan latar mirip serta pencahayaan yang bervariasi. Penulis juga menyatakan bahwa pengumpulan data besar dari berbagai kebun dan varietas sulit dilakukan. Klaim bahwa metode "could be adopted for various real-time applications" belum didukung pengukuran waktu nyata: waktu deteksi yang dilaporkan adalah 1,76 s, 0,561 s, dan 1,75 s per himpunan citra.
