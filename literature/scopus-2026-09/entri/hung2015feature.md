# A feature learning based approach for automated fruit yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hung2015feature` |
| Judul asli | A feature learning based approach for automated fruit yield estimation |
| Penulis | Hung, Calvin; Underwood, James; Nieto, Juan; Sukkarieh, Salah |
| Tahun | 2015 |
| Venue | Springer Tracts in Advanced Robotics |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [hung2015feature.pdf](../pdf/hung2015feature.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-07488-7_33

## Gambaran Umum

Kajian ini memperkirakan hasil panen apel dari citra yang diambil di kebun. Kamera dipasang di kendaraan darat tanpa awak (*unmanned ground vehicle*, UGV) bernama Shrimp, dengan kamera depan Ladybug3. Setiap bingkai citra dibaca oleh algoritma yang menghitung jumlah buah yang tampak di sisi baris kebun, lalu hasilnya dibandingkan dengan jumlah buah yang dihitung manual setelah panen dan dengan bobotnya.

Data dikumpulkan di kebun apel dengan cahaya alami di luar ruangan. Citra berukuran sekitar 1232 × 1616 piksel, dan sekitar 8.000 citra dikumpulkan. Untuk pelatihan, sebagian citra diberi label piksel: 90 sub-citra dan 800 sub-citra dipakai untuk melatih dan menguji pengklasifikasi. Pemrosesan satu bingkai memakan waktu sekitar 30 detik, sehingga sistem ini tidak berjalan secara real time.

Metode utamanya adalah fitur yang dipelajari sendiri (*feature learning*) dengan autoencoder jarang (*sparse autoencoder*) multi-skala. Fitur ini menjadi suku unary pada *conditional random field* (CRF), yaitu model yang memberi label setiap piksel sebagai buah apel, daun, atau latar belakang. Jumlah piksel buah dijumlahkan per sisi baris, lalu dinormalisasi dengan jumlah citra. Sebagai pembanding, penulis juga memakai transformasi Hough lingkaran setelah ambang batas 95%, erosi, dan dilasi. Penilaian pada tingkat piksel memakai ukuran F dan akurasi klasifikasi.

Hasil klasifikasi piksel untuk apel mencapai ukuran F 87,3, sedangkan untuk almond 84,8. Pada klasifikasi biner, akurasi untuk apel tercatat 93,3%. Korelasi terkuat antara hitungan algoritma dan jumlah buah sebenarnya tercatat R² = 0,810 (sekitar 0,81), tetapi angka ini berlaku untuk hitungan yang belum dikalibrasi. Kecocokan setelah kalibrasi lebih buruk untuk tiga sisi, yaitu 8a, 7b, dan 6a, sehingga angka R² tidak dapat langsung dibaca sebagai ketepatan penghitungan di seluruh kebun.

Penulis sendiri mencatat beberapa batas. Bayangan dan oklusi menyebabkan hitungan kurang dari jumlah sebenarnya. Waktu pemrosesan sekitar 30 detik per bingkai membuat metode ini belum cocok untuk pemantauan langsung di lapangan. Penulis menyatakan bahwa kinerja di bawah cahaya terkendali kemungkinan lebih tinggi, tetapi klaim itu belum diverifikasi dalam kajian ini.
