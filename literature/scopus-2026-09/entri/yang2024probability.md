# Probability map-based grape detection and counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024probability` |
| Judul asli | Probability map-based grape detection and counting |
| Penulis | Yang, Canchen; Geng, Tianyu; Peng, Jian; Song, Zichen |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [yang2024probability.pdf](../pdf/yang2024probability.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109175

## Gambaran Umum

Pendeteksian dan pencacahan anggur merupakan tugas dasar dalam viticultur digital. Tugas ini mencakup tiga subtugas: deteksi kluster anggur, pencacahan buah anggur, dan pencacahan jumlah buah per kluster. Studi sebelumnya memperlakukan ketiga subtugas itu secara terpisah. Penulis berpendapat bahwa kluster dan buah memiliki hubungan spasial yang erat, sehingga ketiganya sebaiknya diselesaikan bersamaan. Masalah utama adalah bagaimana memperoleh hasil ketiga subtugas dari keluaran satu jaringan saraf. Pengukuran hasil panen dan pemetaan buah di kebun membutuhkan hitungan yang akurat, sehingga masalah ini penting untuk dipecahkan.

Data yang digunakan berasal dari dua sumber. Pertama, WGISD dikumpulkan pada 2017 hingga 2018 di kebun Guaspari Winery, Brasil. Dataset ini berisi 300 citra RGB dari lima varietas anggur. Semua citra memiliki anotasi *bounding box* kluster, dan 137 citra memiliki anotasi *mask* tingkat instans. Penulis menambahkan anotasi titik untuk 187.306 buah dari studi sebelumnya. Kedua, dataset Chengdu dikumpulkan oleh penulis di Longquanyi, Chengdu, pada Juli 2023. Dataset ini berisi 100 citra RGB dari dua varietas, yaitu Shine Muscat dan Summer Black. Di dalamnya terdapat 772 anotasi *bounding box* kluster dan 30.601 anotasi titik buah. Dataset ketiga, BpGC, dibentuk dari 137 citra WGISD yang dipadukan dengan anotasi buah. Dari 137 citra tersebut, 110 citra digunakan untuk latih dan validasi, sedangkan 27 citra digunakan untuk uji. Model dilatih menggunakan *trainval* WGISD bersama dataset Chengdu.

Metode PMGDC bekerja dalam dua tahap. Pertama, jaringan saraf memprediksi dua peta probabilitas, yaitu peta kluster dan peta buah. Kedua, tiga tahap pascapemrosesan mengekstrak hasil. Metode *local peak* dipakai untuk deteksi, sedangkan metode *Up-Hill* dan *Down-Hill* dipakai untuk menentukan buah dalam setiap kluster dan batas kluster. Pada data uji WGISD, kerangka ini mencapai AP(iou0,5) 0,851 untuk lokalisasi kluster. Untuk kluster, MAE-nya 1,845 dan RMSE-nya 2,142. Untuk buah, MAE-nya 23,414 dan RMSE-nya 31,391. Untuk jumlah buah per kluster, MRD-nya 0,142 dan 1-FVU-nya 0,865. Penulis menyatakan bahwa hasil pada citra di luar WGISD juga mendukung akurasi deteksi kerangka ini.

Penulis menyebutkan beberapa batasan. Pertama, metode hanya mendeteksi kluster dan buah yang terlihat. Buah yang tertutup tidak dibahas. Kedua, penelitian hanya mencakup deteksi dan pencacahan. Hasil itu belum diterapkan pada tugas hilir, seperti penentuan titik petik dan prediksi produksi aktual. Ketiga, WGISD tidak memiliki anotasi segmentasi instans untuk semua kluster. Akibatnya, peta probabilitas kebenaran dasar dibuat dari *bounding box*, sehingga kerangka ini kadang salah mengelompokkan buah di tepi kluster yang berdekatan. Penulis menyarankan pembuatan dataset yang lebih besar serta penggunaan satu jaringan saraf untuk ketiga subtugas secara *end-to-end*.
