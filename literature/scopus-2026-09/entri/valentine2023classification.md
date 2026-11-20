# Classification of Oil Palm Fresh Fruit Bunches (FFB) Based on Its Maturity Colour Using Convolutional Neural Network (CNN) Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `valentine2023classification` |
| Judul asli | Classification of Oil Palm Fresh Fruit Bunches (FFB) Based on Its Maturity Colour Using Convolutional Neural Network (CNN) Approach |
| Penulis | Valentine, Stephenie Carmeline; Alfred, Rayner; Fui, Florence Sia; Shamrie Sainin, Mohd; Iswandono, Zamhar |
| Tahun | 2023 |
| Venue | Lecture Notes in Electrical Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [valentine2023classification.pdf](../pdf/valentine2023classification.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-19-8406-8_46

## Gambaran Umum

Penilaian kematangan tandan buah segar (TBS) kelapa sawit masih dilakukan secara manual oleh penilai di pabrik. Penilaian manual memiliki keterbatasan karena setiap penilai dapat memberi hasil yang berbeda, dan sengketa antara penjual dan penilai dapat terjadi karena kematangan diukur dari warna. Kajian ini mengusulkan sistem penilaian otomatis berbasis *deep learning* dengan *Convolutional Neural Network* (CNN). Kajian ini berfokus pada dua hal. Pertama, klasifikasi multi-kelas, karena sebagian besar penelitian sebelumnya hanya membedakan dua kelas. Kedua, optimasi parameter pelatihan, yaitu jumlah *epoch* dan *batch size*, yang jarang dikaji pada TBS kelapa sawit.

Data diambil dari Kaggle dan terdiri atas 413 citra TBS dengan tingkat kematangan yang sudah diketahui. Tiga kelasnya adalah *Ripe*, *Unripe*, dan *Overripe*. Citra dipotong secara manual agar hanya memuat TBS, lalu diubah ukurannya menjadi 128 x 128 piksel. Data dibagi ke dalam folder *Training*, *Testing*, dan *Validation*, dengan tiga subfolder kelas di masing-masing folder. Kajian ini menggunakan *image data augmentation* berupa pergeseran, rotasi, zoom, dan pembalikan citra untuk memperluas data dan meningkatkan generalisasi model. Kajian ini tidak menyebutkan jumlah citra untuk setiap subset. Sensor dan platform pencitraan tidak dijelaskan, karena citra diperoleh dari dataset publik.

Model dibangun dengan tiga lapisan konvolusi, tiga lapisan *max pooling*, *dropout*, dan satu lapisan terhubung penuh. Lapisan terhubung penuh terdiri atas *dense* 64 unit dengan aktivasi ReLU, *dropout* 0,25, dan lapisan *softmax* tiga unit. Optimizer *Adam* dengan laju pembelajaran 0,01 dipakai karena penulis menilainya paling akurat untuk model CNN ini. Penulis memvariasikan epoch (25, 50, 75, dan 100) dan batch size (32 dan 64), sementara parameter lain dijaga tetap. Hasil terbaik pada tabel evaluasi adalah akurasi uji 0,902 pada 75 epoch dengan batch size 64, dengan akurasi latih 0,967. Pada batch size 32, akurasi uji 0,878 tercapai pada 75 dan 100 epoch, dengan akurasi validasi 0,783 pada 75 epoch dan 0,826 pada 100 epoch. Pada 25 epoch dengan batch size 32, akurasi uji 0,864. Pada 50 epoch dengan batch size 32, akurasi uji turun menjadi 0,268, sedangkan akurasi validasi 0,652. Kajian ini melaporkan akurasi, bukan metrik per kelas.

Penulis menyatakan bahwa jumlah epoch dan batch size sangat memengaruhi kinerja model CNN. Penulis juga menyebutkan bahwa epoch 100 dan batch size yang lebih besar, misalnya 64, menghasilkan akurasi yang lebih tinggi. Hasil di tabel tidak sepenuhnya mendukung pernyataan ini. Pada batch size 64, akurasi uji tertinggi dicapai pada 75 epoch, bukan 100 epoch. Kajian ini juga belum membandingkan model dengan arsitektur lain, dan hasil yang dilaporkan berasal dari satu rangkaian pelatihan dengan dataset kecil.
