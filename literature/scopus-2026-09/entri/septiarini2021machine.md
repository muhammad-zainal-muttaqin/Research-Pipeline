# Machine vision for the maturity classification of oil palm fresh fruit bunches based on color and texture features

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `septiarini2021machine` |
| Judul asli | Machine vision for the maturity classification of oil palm fresh fruit bunches based on color and texture features |
| Penulis | Septiarini, Anindita; Sunyoto, Andi; Hamdani, Hamdani; Kasim, Anita Ahmad; Utaminingrum, Fitri; Hatta, Heliza Rahmania |
| Tahun | 2021 |
| Venue | Scientia Horticulturae |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [septiarini2021machine.pdf](../pdf/septiarini2021machine.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2021.110245

## Gambaran Umum

Kematangan tandan buah segar (TBS) kelapa sawit menentukan kualitas minyak sawit yang dihasilkan. Selama ini tingkat kematangan dinilai secara visual dari warna kulit buah. Penilaian visual bersifat subjektif dan sulit dilakukan secara konsisten pada skala panen. Kajian ini mengusulkan metode *machine vision* untuk mengklasifikasikan TBS menjadi tiga kelas, yaitu mentah (*raw*), matang (*ripe*), dan setengah matang (*half-ripe*). Tantangannya muncul pada citra TBS setengah matang yang warnanya tidak merata dan pada citra yang tertutup noise, misalnya pasir atau tanah gelap.

Data yang digunakan berupa citra TBS kelapa sawit dari sebuah perkebunan di Kabupaten Paser, Kalimantan Timur, Indonesia. Citra diambil dengan kamera bawaan telepon pintar Samsung A50 dalam format JPEG berukuran 4032 × 3024 piksel. Pengambilan dilakukan di area terbuka dengan pencahayaan terang, dengan jarak sekitar ±10 cm antara TBS dan kamera. Jumlah total citra adalah 240, dengan 80 citra untuk setiap kelas. Citra dibagi secara acak menjadi data latih dan data uji, masing-masing 120 citra, dan setiap bagian berisi 40 citra per kelas.

Metode terdiri atas dua tahap, yaitu pelatihan dan pengujian. Pra-pemrosesan mengubah ruang warna RGB ke HSI, HSV, YCbCr, dan YIQ. Dari lima ruang warna tersebut diekstraksi fitur warna dan tekstur, kemudian dipilih fitur terpenting dengan *principal component analysis* (PCA). Sebanyak 40 fitur direduksi menjadi lima fitur, yaitu HYIQ, μCr, HYCbCr, μI2, dan μYIQ, untuk mempersingkat waktu komputasi. Klasifikasi dilakukan dengan *artificial neural network* (ANN) yang dilatih dengan algoritma *back-propagation*. Kinerja diukur dengan *precision*, *recall*, dan *accuracy* berdasarkan *confusion matrix*. Penulis juga membandingkan Naïve Bayes dan SVM sebagai pengklasifikasi, serta seleksi fitur PCA, CFS, dan *gain ratio*.

Hasil terbaik diperoleh dengan kombinasi PCA dan ANN. Nilai precision mencapai 98,4%, recall 98,3%, dan accuracy 98,3%. Kombinasi *gain ratio* dan ANN juga mencapai accuracy 98,3%, tetapi penulis memilih PCA karena hanya menghasilkan lima fitur, sedangkan *gain ratio* menghasilkan enam fitur. Seluruh metode yang diuji mencapai accuracy minimal 90%. Pada kombinasi Naïve Bayes dengan PCA, accuracy tercatat 96,7%, sedangkan SVM dengan PCA mencapai 97,5%. Kesalahan klasifikasi paling sering terjadi ketika TBS setengah matang diprediksi sebagai matang, karena warna keduanya lebih mirip dibandingkan dengan mentah. Kesalahan lain terjadi satu kali pada citra TBS matang yang tertutup pasir atau tanah gelap sehingga warnanya menyerupai tingkat mentah.

Penulis menyatakan beberapa batasan. Kesalahan klasifikasi TBS setengah matang sebagai matang disebabkan oleh perubahan warna yang tidak merata pada buah. Penulis menilai keterbatasan ini dapat dikurangi dengan memperbaiki teknik akuisisi citra dan menghilangkan noise yang menutupi area buah. Metode ini juga hanya membedakan tiga kelas, sehingga pengembangan untuk lebih dari tiga kelas masih terbuka. Evaluasi hanya dilakukan pada satu dataset lokal dengan 120 citra uji, sehingga generalisasi ke kondisi lapangan lain belum diuji oleh penulis.
