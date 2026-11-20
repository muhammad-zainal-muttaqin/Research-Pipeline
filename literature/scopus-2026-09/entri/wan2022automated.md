# Automated image identification, detection and fruit counting of top-view pineapple crown using machine learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wan2022automated` |
| Judul asli | Automated image identification, detection and fruit counting of top-view pineapple crown using machine learning |
| Penulis | Wan Nurazwin Syazwani, R.; Muhammad Asraf, H.; Megat Syahirul Amin, M.A.; Nur Dalila, K.A. |
| Tahun | 2022 |
| Venue | Alexandria Engineering Journal |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | pineapple |

## Tautan Akses
- PDF: [wan2022automated.pdf](../pdf/wan2022automated.pdf)
- DOI resmi: https://doi.org/10.1016/j.aej.2021.06.053

## Gambaran Umum

Kajian ini membahas pengenalan, deteksi, dan pencacahan mahkota nanas (*pineapple crown*) dari citra RGB tampak atas yang direkam dengan pesawat nirawak (UAV). Penulis menilai pengenalan buah dari citra udara sebagai unsur kunci agrikultur presisi, terutama untuk memperkirakan hasil panen pada setiap petak kebun. Masalah utamanya adalah kondisi lapangan yang berubah-ubah. Pencahayaan siang hari bervariasi, bentuk objek tidak beraturan, dan tekstur daun rumit. Warna mahkota juga mirip dengan daun, sehingga sulit dibedakan dari latar. Penulis menyatakan bahwa ini adalah kajian pertama yang secara khusus menganalisis citra nanas berbasis UAV.

Data dikumpulkan pada Maret 2019 di kebun nanas di bagian selatan Malaysia, saat musim panen. Pesawat yang digunakan adalah DJI Phantom 3 Advanced dengan kamera CMOS RGB 12 megapiksel dan gimbal tiga sumbu. Pesawat terbang pada ketinggian 3 m di atas tanah dengan kecepatan 16 m/s, dan merekam 110 baris dari 1,44 acre. Kajian ini membatasi area pada satu divisi yang menghasilkan 1.300 bingkai berukuran 2.704 x 1.520 piksel. Citra yang saling tumpang tindih digabung menjadi video RGB dengan Image Composite Editor. Dari data itu, 20 citra contoh dipilih secara acak lalu dianotasi secara manual. Anotasi menghasilkan 360 mahkota, yaitu 180 nanas dan 180 latar berupa daun, rumput, dan tanah. Data dibagi menjadi data latih dan data uji, masing-masing berisi 90 nanas dan 90 latar.

Alur kerjanya meliputi pra-pemrosesan citra, ekstraksi fitur bentuk, warna, dan tekstur, seleksi fitur, lalu klasifikasi. Pra-pemrosesan mencakup peningkatan kontras dengan CLAHE, penghapusan latar pada ruang warna HSV, dan operasi morfologi. Seleksi fitur memakai *feature selection* berbasis ANOVA satu arah. Penulis membandingkan enam pengklasifikasi, yaitu ANN, SVM, RF, NB, DT, dan KNN, dengan beberapa algoritma pelatihan. Hasil terbaik diperoleh dari ANN-GDX dengan seleksi fitur ANOVA, dengan akurasi 94,4%, presisi 92,6%, spesifisitas 96,5%, dan sensitivitas 96,7%. Seleksi fitur menaikkan kinerja klasifikasi sebesar 2,94%. KNN kasar memiliki akurasi terendah dan turun 36,02% dari akurasi maksimum. Pada tahap pencacahan, ANN-GDX dengan ANOVA mencacah 87 dari 90 citra uji dengan benar. SVM kuadratik mencapai hasil yang sebanding. Penulis juga melaporkan bahwa RF dan DT kurang tepat untuk pencacahan, dengan hasil 76 dan 69 dari 90 citra.

Penulis mengakui bahwa tingkat *false negative* dan *false positive* masih tinggi. Penyebabnya, fitur nanas dan daun cukup mirip, terutama dari warna dan bentuk daun. Penulis juga menyatakan bahwa studi ini merupakan penyelidikan awal yang terbatas pada satu divisi kebun. Penulis menilai algoritma belum sepenuhnya menghilangkan noise dan belum sepenuhnya akurat dalam pencacahan. Pekerjaan lanjutan diarahkan pada peningkatan deteksi yang tahan noise, penambahan fitur yang dievaluasi, dan keputusan klasifikasi yang lebih akurat.
