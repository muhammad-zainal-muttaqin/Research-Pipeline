# An Oil Palm Loose Fruits Image Detection System using Faster R -CNN and Jetson TX2

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xiang2021oil` |
| Judul asli | An Oil Palm Loose Fruits Image Detection System using Faster R -CNN and Jetson TX2 |
| Penulis | Xiang, Ang Jin; Huddin, Aqilah Baseri; Ibrahim, Mohd Faisal; Hashim, Fazida Hanim |
| Tahun | 2021 |
| Venue | Proceedings of the International Conference on Electrical Engineering and Informatics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [xiang2021oil.pdf](../pdf/xiang2021oil.pdf)
- DOI resmi: https://doi.org/10.1109/iceei52609.2021.9611111

## Gambaran Umum

Penulis menyatakan bahwa buah lepas (*loose fruit*, brondolan) sawit mengandung minyak lebih tinggi daripada TBS, sekitar 48% untuk seluruh brondolan dibandingkan sekitar 22% untuk TBS. Pengumpulan manual atau dengan alat pengumpul tipe rol dinilai kurang efisien dan melelahkan pekerja. Studi ini mengusulkan sistem deteksi brondolan dengan Faster R-CNN dan perangkat NVIDIA Jetson TX2 sebagai mata mesin pengumpul otomatis.

Data berupa 500 citra brondolan dari kebun sawit di Bukit Bangkong, Selangor, yang diambil saat masa panen dengan ukuran, pencahayaan, dan latar belakang berbeda. Citra diubah ukurannya menjadi 640x480 piksel dan diberi kotak pembatas dengan LabelImg. Augmentasi (pembalikan, rotasi, *padding*, intensitas, *color jittering*, penajaman tepi) dilakukan. Citra dipilih acak dengan rasio 4:1, yaitu 400 untuk latih dan 100 untuk validasi dan uji. Jenis sensor, jumlah pohon, dan pemberi label tidak disebut.

Faster R-CNN adalah detektor dua tahap. Jaringan konvolusi membentuk peta fitur, *region proposal network* mengusulkan wilayah calon objek, lalu *ROI pooling* dan pengklasifikasi menetapkan kelas dan kotak. Pelatihan dihentikan pada iterasi 80000 saat *loss* 0,0496 di bawah ambang 0,05. Model dengan *loss* terendah dipilih. Model dipindahkan ke Jetson TX2 pada kendaraan *rocker-bogie* sebagai purwarupa.

Pada data uji, Tabel 1 melaporkan mAP 0,770 pada IoU 0,50 sampai 0,95, 0,916 pada IoU 0,75, dan 0,998 pada IoU 0,5, sedangkan teks menulis 0,988 untuk IoU 0,5. Matriks konfusi pada IoU 0,5 berisi 353 positif benar, 10 positif palsu, dan 10 negatif palsu, dengan presisi dan *recall* 0,97 dan akurasi 0,94. Pada IoU 0,9 presisi 0,98, *recall* 0,93, dan akurasi 0,91. mAP untuk objek kecil, sedang, dan besar adalah 0,264, 0,688, dan 0,837.

Keterbatasan yang dapat diperiksa: pembagian acak per citra tanpa pembagian per lokasi atau pohon, dan tidak jelas apakah ada set validasi terpisah dari uji, padahal teks menyebut 100 citra dipakai untuk keduanya. Nilai mAP IoU 0,5 tidak konsisten antara teks dan tabel. Akurasi dihitung dengan negatif benar bernilai 0, sehingga rumusnya tidak bermakna sebagai akurasi klasik. Tidak ada pembandingan dengan detektor lain, tidak ada kecepatan inferensi pada Jetson TX2, dan hanya satu kelas yang dideteksi.
