# Color-Based Ripeness Classification of Oil Palm Fresh Fruit Bunches Using Convolution Neural Networks and Data Augmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bakar2024color` |
| Judul asli | Color-Based Ripeness Classification of Oil Palm Fresh Fruit Bunches Using Convolution Neural Networks and Data Augmentation |
| Penulis | Bakar, Juhaida Abu; M Kehail, Mahmoud A; Mat Kassim, Muhamad Syafiq; Saravanan, Ranjithkumar; Cheng, Zhao Wei; Dahham Al-Marsoomi, Ali Ghazi |
| Tahun | 2024 |
| Venue | 2024 IEEE 7th International Conference on Electronics and Communication Engineering Icece 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [bakar2024color.pdf](../pdf/bakar2024color.pdf)
- DOI resmi: https://doi.org/10.1109/icece63871.2024.10976938

## Gambaran Umum

Kajian ini menilai apakah jaringan saraf konvolusi (*convolutional neural network*, CNN) dapat mengelompokkan kematangan tandan buah segar (TBS) kelapa sawit berdasarkan warna. Penulis menyebut penilaian manual oleh pemanen bersifat padat karya dan rawan kesalahan manusia karena bergantung pada pengamatan visual yang subjektif. Kajian mengklasifikasikan citra tandan, bukan menghitung buah.

Data berupa foto TBS yang dikumpulkan dari berbagai sumber internet, antara lain Kaggle, ditambah foto yang diambil sendiri. Tiga kelas ditetapkan menurut warna: kelas 0 mentah (hitam), kelas 1 kurang matang (dominan merah), dan kelas 2 matang (dominan jingga). Pakar diminta mengklasifikasikan foto yang diambil sendiri. Jumlah citra total, jumlah pohon, tempat pengambilan, jenis sensor, dan rasio pembagian tidak disebut. Data dibagi menjadi subset latih dan subset validasi.

Metode memakai pembelajaran transfer (*transfer learning*), yaitu model Xception yang sudah dilatih sebelumnya dipakai sebagai tulang punggung, lalu lapisan *flatten* dan lapisan padat untuk tiga kelas ditambahkan. Data diperbanyak dengan augmentasi citra, yaitu salinan citra yang sedikit diubah. Pelatihan memakai pengoptimal Adam, fungsi kerugian *categorical cross-entropy*, 150 *epoch*, dan ukuran *batch* 32. Peta aktivasi dan Grad-CAM dipakai untuk visualisasi, dan antarmuka grafis dibuat dengan PyQt5.

Akurasi keseluruhan 80,4%. Per kelas, akurasi 92,62% (kelas 0), 81,54% (kelas 1), dan 88,26% (kelas 2). Presisi 93, 59, dan 92%; *recall* 86, 81, dan 77%; skor F1 89, 68, dan 84%. Matriks konfusi menunjukkan kelas 1 paling lemah: 59% terklasifikasi benar dan 26% diprediksi sebagai kelas 2. Metrik dilaporkan pada subset validasi, bukan pada data uji terpisah.

Keterbatasan yang dapat diperiksa dari teks: tidak ada data uji terpisah dari subset validasi, tidak ada pembagian per pohon, jumlah citra tidak disebut, dan sumber internet dicampur dengan foto sendiri sehingga kondisi pengambilan tidak seragam. Penulis menyebut data terbatas dan menyarankan pengumpulan data tambahan serta CLAHE. Kelas kurang matang yang lemah dikaitkan penulis dengan jumlah data yang lebih kecil atau kemiripan dengan dua kelas lain, tanpa pengujian.
