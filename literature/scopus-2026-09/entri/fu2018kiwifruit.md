# Kiwifruit yield estimation using image processing by an Android mobile phone

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fu2018kiwifruit` |
| Judul asli | Kiwifruit yield estimation using image processing by an Android mobile phone |
| Penulis | Fu, Longsheng; Liu, Zhihao; Majeed, Yaqoob; Cui, Yongjie |
| Tahun | 2018 |
| Venue | IFAC Papersonline |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [fu2018kiwifruit.pdf](../pdf/fu2018kiwifruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.ifacol.2018.08.137

## Gambaran Umum

Fu dkk. (2018) menghitung buah kiwi dari foto yang diambil dengan ponsel Android (*android mobile phone*, AMP) di bawah kanopi, lalu memakai hasil hitungan itu untuk memperkirakan hasil panen kebun.
Penghitungan dilakukan pada kelopak buah (*calyx*), bagian ujung bawah buah kiwi yang tampak sebagai pola melingkar. Citra diubah ke ruang warna RGB, HSV, dan L*a*b*, lalu saluran dengan distribusi paling berekor-tebal dipilih berdasarkan nilai kurtosis. Saluran H (HSV) dan a* (L*a*b*) dipilih dengan kurtosis 19,5 dan 21,3, dan rentang nilainya dipakai untuk segmentasi. Setelah itu, citra diproses dengan ambang batas, erosi dan dilasi, deteksi tepi Canny, dan templat lingkaran. Sebuah titik dihitung sebagai kelopak bila sebaran tepi di dalam templat cukup seragam, yang diukur dengan rasio lebar terhadap tinggi mendekati 1. Papan referensi berukuran diketahui digantung di bawah kanopi untuk mengonversi luas piksel menjadi luas nyata.

Hasil utama ada beberapa. Pada 100 citra, penghitungan algoritma dibandingkan dengan hitungan manusia di area yang sama, dan rasio estimasi rata-rata adalah 76,4%. Kesalahan utama dikaitkan dengan kelopak yang tertutup daun atau cabang, dan kelopak berbentuk oval yang membuat rasio lebar-tinggi di luar rentang templat. Rasio pengenalan benar 77,9% pada sore hari dan 74,2% pada pagi hari, dan pengambilan dengan lampu kilat memberi hasil lebih tinggi daripada tanpa lampu. Galat rata-rata pengukuran luas papan referensi pada 20 citra adalah 0,76%, dengan galat maksimum 1,03%. Estimasi hasil panen rata-rata 80 buah per meter persegi, sedikit di bawah hasil aktual 106 buah per meter persegi, yang oleh penulis dikaitkan dengan penanaman yang tidak merata, luas kebun yang tercatat terlalu besar, dan buah yang jatuh saat panen. Waktu proses sekitar 2,0 detik per citra pada ponsel dengan CPU 2,15 GHz.

Batas studi ini perlu dinyatakan secara eksplisit. Jumlah citra uji hanya 100, sehingga variasi antarkebun belum diukur. Angka 76,4% adalah rasio terhadap hitungan manusia dan bukan presisi atau recall terhadap anotasi terverifikasi, serta tidak dilaporkan per kondisi kanopi. Perbandingan hasil panen hanya dilakukan untuk satu periode, yaitu akhir Oktober. Dari sisi rekayasa, pendekatan ini sederhana dan murah, tetapi ketergantungannya pada bentuk kelopak membatasi penerapannya pada kondisi lain.
