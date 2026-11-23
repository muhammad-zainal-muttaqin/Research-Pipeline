# Multi-view traffic sign detection, recognition, and 3D localisation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `timofte2014multi` |
| Judul asli | Multi-view traffic sign detection, recognition, and 3D localisation |
| Penulis | Timofte, Radu; Zimmermann, Karel; Van Gool, Luc |
| Tahun | 2014 |
| Venue | Machine Vision and Applications |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [timofte2014multi.pdf](../pdf/timofte2014multi.pdf)
- DOI resmi: https://doi.org/10.1007/s00138-011-0391-3

## Gambaran Umum

Penulis menyatakan bahwa survei rambu lalu lintas untuk pemetaan jalan memerlukan jutaan kilometer citra jalan yang diulang secara berkala. Masalahnya adalah variasi pencahayaan, oklusi, dan posisi rambu yang berubah-ubah. Penelitian ini mengusulkan pipeline deteksi, pengenalan, dan lokalisasi 3D rambu dari citra multi-kamera. Kajian ini berada di luar pertanian dan dimasukkan sebagai metode yang dapat dipindahkan.

Data dikumpulkan dengan van yang dilengkapi delapan kamera atap, dengan citra 1.628 × 1.236 piksel setiap sekitar satu meter di jalan Belgia. Set data BelgiumTS memuat 13.444 anotasi rambu dan 4.565 rambu fisik berbeda. Pembagian latih berisi 8.851 anotasi, uji 2D 4.593 anotasi, dan uji 3D 1.625 anotasi. Teks tidak menyebut siapa pemberi label secara rinci.

Metode terdiri atas tiga tahap. Kandidat diambil dengan ambang warna dan pencocokan bentuk Hough. Deteksi memakai kaskade *AdaBoost* dan SVM. Hipotesis 3D dibentuk dari pasangan deteksi antarpandang, lalu dipilih dengan *minimum description length* (MDL), yaitu prinsip memilih himpunan hipotesis terkecil yang menjelaskan deteksi 2D.

Hasil deteksi tunggal dengan Det+Extr1 adalah FN-TS 2,3% (20 dari 859 rambu) dan FN-BB 4,0% (103 dari 2.571 anotasi) pada 2 positif palsu per citra 2 MP. Pada uji 3D, 304 dari 319 rambu (95,30%) terlokalisasi dengan benar dan 20 positif palsu. Klasifikasi tipe yang benar berjumlah 285 (97,04%).

Keterbatasan yang dapat diperiksa dari teks: evaluasi dibatasi pada 62 kelas rambu, sedangkan rambu yang tidak masuk kelas tidak diuji. Teks tidak mengukur pemetaan pada tanaman atau tandan buah, dan tidak ada pembagian per pohon.
