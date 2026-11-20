# Automatic image segmentation of oil palm fruits by applying the contour-based approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `septiarini2020automatic` |
| Judul asli | Automatic image segmentation of oil palm fruits by applying the contour-based approach |
| Penulis | Septiarini, Anindita; Hamdani, Hamdani; Hatta, Heliza Rahmania; Anwar, Khoerul |
| Tahun | 2020 |
| Venue | Scientia Horticulturae |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [septiarini2020automatic.pdf](../pdf/septiarini2020automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2019.108939

## Gambaran Umum

Pencacahan buah sawit berbasis citra memerlukan tahap segmentasi untuk memisahkan area buah dari latar belakang. Tahap ini sulit dilakukan ketika latar alami berisi daun, batang, tanah, atau langit, dan pencahayaan tidak merata. Penulis mengusulkan metode segmentasi berbasis kontur untuk buah sawit yang memiliki bentuk dan warna beragam. Tujuannya memisahkan buah dari berbagai jenis latar. Metode ini ditujukan sebagai tahap awal sebelum klasifikasi tingkat kematangan.

Data terdiri atas 160 citra buah sawit yang diambil dengan kamera digital ponsel Samsung edge 7. Jarak pengambilan sekitar 40 sampai 90 cm, baik di luar ruangan dengan cahaya matahari maupun di dalam ruangan dengan penerangan cukup. Citra disimpan dalam ruang warna RGB berformat JPEG dengan resolusi 3264 × 2448 piksel. Dataset terdiri atas 60 buah mentah (*raw*), 50 buah belum matang (*under-ripe*), dan 50 buah matang. Sebanyak 52 citra memiliki latar sederhana dan 108 citra memiliki latar kompleks. *Ground truth* dibuat secara manual dengan Adobe Photoshop CS6. Seluruh 160 citra digunakan untuk mengevaluasi metode. Teks tidak merinci pembagian data latih dan data uji.

Metode bekerja dalam tiga tahap utama, yaitu lokalisasi buah, pra-pemrosesan, dan segmentasi. Citra diperkecil menjadi 640 × 480 piksel, lalu dikonversi ke ruang warna *Lab*. Ambang Otsu menghasilkan *region of interest* (ROI), dan operasi *opening* serta *closing* menghilangkan derau. Pada tahap segmentasi, *Canny* dengan penghalusan Gaussian mendeteksi tepi, kemudian dilakukan dilasi, pengisian lubang, dan rekonstruksi. Hasil akhirnya diperoleh setelah *closing* dan *opening*. Evaluasi memakai tiga indeks, yaitu akurasi segmentasi (Sc), kesalahan positif palsu (FPe), dan kesalahan negatif palsu (FNe). Untuk seluruh dataset, metode mencapai Sc 90,13%, FPe 2,92%, dan FNe 5,20%. Pada latar sederhana, nilainya Sc 90,48%, FPe 5,01%, dan FNe 3,48%. Pada latar kompleks, nilainya Sc 89,98%, FPe 2,08%, dan FNe 5,89%. Pada perbandingan dengan *active contour*, Sc hanya 61,75%, FPe 26,08%, dan FNe 14,59%. Metode Otsu mencapai Sc 77,06% dan FPe 10,37%. Metode yang diusulkan memiliki FPe dan FNe lebih rendah daripada kedua pembanding tersebut.

Penulis menyatakan bahwa kesalahan lebih sering terjadi pada buah multiwarna, latar kompleks, dan pencahayaan yang tidak seragam. Pada latar sederhana, kesalahan berupa segmentasi berlebih (*over-segmentation*) karena bayangan, batang, atau objek lain ikut terdeteksi sebagai buah. Segmentasi kurang (*under-segmentation*) umumnya terjadi pada buah multiwarna. Pada latar kompleks, derau sulit dibuang sehingga FNe lebih tinggi daripada FPe. Penulis juga mencatat bahwa beberapa buah tetap terdeteksi secara keliru sebagai latar belakang. Klasifikasi tingkat kematangan belum dikerjakan dalam kajian ini dan dinyatakan sebagai pekerjaan lanjutan. Teks tidak membahas pengujian pada kebun dengan jarak pengambilan lebih jauh atau pada jenis kamera lain.
