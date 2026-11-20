# Automatic detection and calculation of palm oil fresh fruit bunches using faster R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `prasetyo2020automatic` |
| Judul asli | Automatic detection and calculation of palm oil fresh fruit bunches using faster R-CNN |
| Penulis | Prasetyo, N.A.; others |
| Tahun | 2020 |
| Venue | International Journal of Applied Science and Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [prasetyo2020automatic.pdf](../pdf/prasetyo2020automatic.pdf)
- DOI resmi: https://doi.org/10.6703/ijase.202005_17(2).121

## Gambaran Umum

Penelitian ini bertujuan menghitung tandan buah segar (TBS) kelapa sawit secara otomatis dari citra. Latar belakangnya adalah penghitungan manual yang sulit dan memakan waktu, terutama untuk tandan yang tidak merata, berukuran besar, dan berada pada jarak jauh. Penulis juga menunjukkan bahwa metode peramalan yang ada, seperti metode fuzzy rule-based time series dan regresi linear, hanya memprediksi kebutuhan bahan baku, bukan ketersediaan nyata tandan di lapangan. Karena itu, penulis mengusulkan sistem deteksi dan penghitungan otomatis berbasis pembelajaran mendalam.

Datanya berupa 100 citra JPG yang diunduh dari internet, dengan ukuran antara 181 × 278 hingga 1300 × 956 piksel. Anotasi dibuat dalam format COCO menggunakan alat poligon, menghasilkan 536 anotasi TBS. Pelatihan memakai komputer Intel Core i7 3770K, RAM 16 GB, dan NVIDIA GTX980, dengan sistem Ubuntu 16.04, Python 3.6, serta kerangka TensorFlow. Evaluasi memakai validasi silang 5 lipat: data dibagi menjadi lima partisi berisi 20 citra setiapnya, lalu lima percobaan dijalankan dengan empat partisi sebagai latih dan satu sebagai validasi. Setiap model dilatih selama 5.000 epoch dan diuji pada 10 citra.

Mekanisme deteksi memakai Faster R-CNN, yang terdiri dari dua modul, yaitu Region Proposal Network (RPN) dan detektor Fast R-CNN. RPN memprediksi keberadaan objek dan kotak pembatasnya, kemudian detektor mengklasifikasikan hasil tersebut menurut kelas objek. Penulis membandingkan empat arsitektur jaringan, yakni Inception ResNet V2, Inception V2, ResNet50, dan ResNet101. Penghitungan dilakukan dengan membandingkan hasil deteksi sistem terhadap hitungan manual. Metrik evaluasi berupa presisi, recall, false negative rate, false alarm, dan F1 score, yang dihitung dari jumlah true positive, false positive, dan false negative.

Hasilnya menunjukkan F1 score rata-rata di atas 80% untuk keempat model. Nilai rata-rata F1 score berturut-turut adalah 82% (Inception ResNet V2), 85% (Inception V2), 86% (ResNet50, tertinggi), dan 82% (ResNet101). Nilai presisi rata-rata sekitar 97% untuk semua model, dengan recall antara 71% dan 75%. Penulis menyatakan kegagalan deteksi terutama disebabkan tingkat oklusi yang tinggi (1–75% dan 75–99%) serta tumpukan tandan yang terlalu rapat sehingga batas antartandan tidak jelas. Kasus lain mencakup dua tandan yang terdeteksi sebagai satu dan tandan yang tidak terdeteksi karena anotasi kurang beragam. Penulis menyarankan penambahan dataset berkualitas lebih baik, termasuk citra berpiksel kecil, serta modifikasi arsitektur untuk memperbaiki hasil.
