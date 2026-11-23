# Automated Yield Estimation of Fruits Using Multilayer Convolution Neural Networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sathesh2019automated` |
| Judul asli | Automated Yield Estimation of Fruits Using Multilayer Convolution Neural Networks |
| Penulis | Kumar, K Sathesh; Kumar, R Arun; Kumar, V Praveen |
| Tahun | 2019 |
| Venue | Proceedings of the 2019 International Conference on Advances in Computing and Communication Engineering Icacce 2019 |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [sathesh2019automated.pdf](../pdf/sathesh2019automated.pdf)
- DOI resmi: https://doi.org/10.1109/icacce46606.2019.9079955

## Gambaran Umum

Penulis menyebut estimasi hasil buah masih dilakukan manual, sehingga mahal, lama, dan tidak teliti. Mereka mengusulkan *convolutional neural network* (CNN, jaringan saraf konvolusi) berlapis jamak untuk menghitung buah apel pada citra pohon, termasuk buah yang bertumpuk.

Data latih berjumlah 640 citra apel. Data uji berupa 164 citra apel lain dan 50 citra acak yang diunduh dari Google. Semua citra diubah ukurannya menjadi 128x128 piksel. Sumber citra latih, pemberi label, dan jumlah buah tidak disebut. Hasil dilaporkan pada 50 citra yang dipilih acak.

Metodenya terdiri dari tiga langkah. Pertama, prapemrosesan *Zero Component Analysis* (ZCA, pemutihan data yang menonjolkan tepi) dengan normalisasi ukuran dan rerata. Kedua, CNN dengan lapisan konvolusi 64 kernel 4x4, 32 kernel 3x3, dan 128 kernel 1x1, ReLU, *max pooling* 2x2, dan lapisan penuh 512 neuron, yang mengklasifikasi citra sebagai buah atau bukan buah. Ketiga, transformasi *watershed* (pemisahan objek yang bersentuhan) untuk menghitung buah yang bertumpuk. Teks tidak merinci bagaimana CNN dan *watershed* digabung menjadi hitungan.

Hasil: rerata akurasi 93,4% pada 50 citra (Gambar 3). Tabel 1 hanya memuat sebagian contoh, misalnya hitungan 19 untuk acuan 21, 14 untuk 15, dan 8 untuk 8. Teks tidak mendefinisikan rumus akurasi hitungan. Teks menyatakan metode berfungsi pada berbagai pencahayaan, tetapi tidak ada uji per kondisi.

Keterbatasan yang dapat diperiksa: tidak ada pembagian per pohon, tidak disebut apakah citra uji terpisah dari citra latih, dan 50 citra unduhan tidak dijelaskan asalnya. Hanya apel merah yang diuji, dan tidak ada pembanding. Metrik galat standar (MAE, RMSE) tidak dilaporkan. Penulis menyebut metode Song dkk. yang memakai beberapa citra, tetapi metode mereka sendiri memakai citra tunggal.
