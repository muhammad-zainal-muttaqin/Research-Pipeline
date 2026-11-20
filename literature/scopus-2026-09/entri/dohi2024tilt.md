# Tilt-Invariant Lemon Size Estimation Using RGB-D Camera Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dohi2024tilt` |
| Judul asli | Tilt-Invariant Lemon Size Estimation Using RGB-D Camera Images |
| Penulis | Dohi, Ayuna; Buayai, Prawit; Kwon, Ki-Ryong; Mao, Xiaoyang |
| Tahun | 2024 |
| Venue | Proceedings 2024 International Conference on Cyberworlds Cw 2024 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [dohi2024tilt.pdf](../pdf/dohi2024tilt.pdf)
- DOI resmi: https://doi.org/10.1109/cw64301.2024.00041

## Gambaran Umum

Kajian ini membahas pengukuran ukuran buah lemon hijau (*Citrus*) dari citra RGB-D, yaitu citra warna yang dipasangkan dengan citra kedalaman (*depth*) dari kamera sensor kedalaman. Tujuannya bukan menghitung buah, melainkan memperkirakan diameter setiap buah dalam milimeter. Pengukuran ini dilakukan pada kebun lemon dalam ruangan dan luar ruangan, dengan 2.038 citra sebagai data.

Metodenya bekerja dalam dua tahap. Tahap pertama adalah model deteksi berbasis *deep learning* yang menemukan dua objek: lemonnya sendiri dan ujung buah (*tip*), yaitu titik ujung kecil pada kulit buah. Model melaporkan mAP50 0,791 untuk deteksi lemon dan 0,880 untuk deteksi ujung buah. Tahap kedua memperkirakan diameter. Mask setiap buah dicocokkan dengan elips, lalu dihitung fitur kemiringan (*tilt*) dari posisi ujung buah. Lima fitur ini menjadi masukan model regresi, yaitu Lasso, Ridge, Elastic Net, dan Random Forest. Augmentasi dengan rotasi dan perubahan kecerahan (faktor 0,6 sampai 1,6) dipakai untuk memperbanyak variasi data latih.

Hasil utama menunjukkan bahwa Random Forest mengungguli tiga model lain pada ketiga metrik ukuran (MAE, MSE, dan RMSE) pada data uji. Elastic Net memiliki RMSE terkecil di antara tiga model linear, yaitu 42,52, tetapi nilai itu masih lebih dari dua kali RMSE Random Forest. Untuk buah yang sepenuhnya terlihat, MAE mencapai 2,94 mm. Akurasi turun ketika buah tertutup daun atau buah lain, dan penurunan ini dinyatakan penulis tanpa angka perbandingan yang dapat dikutip di sini.

Keterbatasan kajian ini berkaitan dengan objek dan lingkungan. Objeknya lemon hijau, bukan kelapa sawit, dan tidak ada data tandan atau pelepah. Metode ini bergantung pada kualitas depth, sehingga kondisi luar ruangan yang kuat cahaya matahari dapat mengurangi kualitas pengukuran, meskipun kajian ini memisahkan hasil dalam dan luar ruangan.

Bagi tinjauan tentang penghitungan buah, kajian ini menunjukkan bahwa informasi kedalaman dapat dipakai untuk mengubah deteksi 2D menjadi ukuran fisik per buah. Ini relevan untuk pertanyaan tentang pengukuran dengan depth atau 3D. Kajian ini tidak mengukur identitas buah lintas pandang, sehingga tidak menjawab pertanyaan tentang deduplikasi.
