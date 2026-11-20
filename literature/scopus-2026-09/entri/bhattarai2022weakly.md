# A weakly-supervised approach for flower/fruit counting in apple orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bhattarai2022weakly` |
| Judul asli | A weakly-supervised approach for flower/fruit counting in apple orchards |
| Penulis | Bhattarai, Uddhav; Karkee, Manoj |
| Tahun | 2022 |
| Venue | Computers in Industry |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [bhattarai2022weakly.pdf](../pdf/bhattarai2022weakly.pdf)
- DOI resmi: https://doi.org/10.1016/j.compind.2022.103635

## Gambaran Umum

Bhattarai dkk. (2022) mengusulkan CountNet, jaringan konvolusi yang menghitung jumlah buah atau bunga dalam satu citra sebagai masalah regresi. Pelatihan hanya memakai anotasi tingkat citra, yaitu total jumlah objek per citra, tanpa kotak atau titik lokasi. Model diuji pada dataset buah (Fruit-A dan dataset Gao dkk., 2020) serta dataset bunga apel. Hasil utamanya: MAE 2,9 pada Fruit-A (sekitar 9% dari rata-rata buah per citra) dan 3,9 pada dataset Gao dkk. (sekitar 8%). Pada bunga apel, MAE 12,0 (sekitar 17% dari rata-rata bunga per citra).

Penghitungan buah dengan deteksi objek membutuhkan kotak pembatas untuk setiap buah. Anotasi kotak mahal dan lambat, terutama untuk pohon dengan kerapatan buah tinggi. Penghitungan berbasis regresi memerlukan hanya satu angka per citra. Kelemahannya, model tidak tahu di mana objek berada, sehingga kesalahan tidak dapat ditelusuri ke lokasi. Kajian ini menguji apakah angka tingkat citra saja cukup untuk melatih penghitung yang akurat pada pohon apel dan buah lain.

CountNet memakai backbone VGG16 dan adaptive global average pooling, lalu meregresikan satu nilai jumlah. Karena pooling merata-ratakan peta fitur di seluruh citra, lokasi spasial tidak dipertahankan di kepala regresi. Jaringan dipaksa belajar fitur yang berkorelasi dengan jumlah, bukan lokasi objek.

CountNet memiliki 14,9 juta parameter terlatih. Sebagai pembanding, MSR (Farjon dkk., 2021) yang memakai ResNet-50 dan FPN memiliki 32,6 juta parameter. Kajian ini juga membandingkan LBP+KRR dan Modified Inception-ResNet (Rahnemoonfar dan Sheppard, 2017).

Label kebenaran dikumpulkan dengan anotasi tingkat citra: jumlah bunga atau buah ditulis per citra tanpa menandai lokasi atau ciri objek. Ini mengurangi biaya anotasi, tetapi model hanya menerima satu target per citra.

Penulis memakai Score-CAM dan Guided Backpropagation untuk melihat area aktivasi.

Metrik utama adalah MAE dan RMSE per citra, Pearson r, serta kemiringan dan intercept garis tren antara jumlah prediksi dan jumlah sebenarnya. Hasil yang dilaporkan:

- Fruit-A: MAE 2,9 (sekitar 9% dari rata-rata buah per citra).
- Dataset Gao dkk. (2020): MAE 3,9 (sekitar 8%).
- Bunga apel: MAE 12,0 (sekitar 17%).

Persentase kesalahan pada bunga apel lebih besar daripada pada buah. Penulis tidak menjelaskan penyebabnya secara terpisah dalam bagian yang sudah diperiksa. Angka MAE dari tiga dataset berbeda tidak sebanding secara langsung karena rata-rata jumlah per citra berbeda. Oleh karena itu persentase lebih informatif daripada MAE mentah.

Kelebihan utamanya adalah biaya anotasi yang rendah dan jumlah parameter yang lebih kecil dibanding MSR. Secara konseptual, angka tingkat citra tidak memberi tahu model apakah dua citra berbeda memuat buah yang sama, sehingga kajian ini tidak menyelesaikan masalah penghitungan lintas pandang.

Penulis sendiri melaporkan dua keterbatasan. Pertama, jaringan ikut menghitung bunga dari baris latar pada arsitektur kebun V-trellis. Kedua, jaringan secara substansial meremehkan jumlah buah pada citra yang sangat kurang cahaya. Keduanya menunjukkan bahwa model belajar dari pola citra yang terlihat, bukan dari objek yang terpisah.
