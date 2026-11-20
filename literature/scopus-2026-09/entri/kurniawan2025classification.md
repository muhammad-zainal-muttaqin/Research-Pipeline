# Classification of palm oil fruit ripeness based on AlexNet deep Convolutional Neural Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kurniawan2025classification` |
| Judul asli | Classification of palm oil fruit ripeness based on AlexNet deep Convolutional Neural Network |
| Penulis | Kurniawan, Rudi; Samsuryadi, Samsuryadi; Mohamad, Fatma Susilawati; Wijaya, Harma Oktafia Lingga; Santoso, Budi |
| Tahun | 2025 |
| Venue | Sinergi Indonesia |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kurniawan2025classification.pdf](../pdf/kurniawan2025classification.pdf)
- DOI resmi: https://doi.org/10.22441/sinergi.2025.1.019

## Gambaran Umum

Kajian ini mengatasi klasifikasi kematangan buah sawit yang dilakukan secara manual. Penulis menyatakan cara manual memakan waktu, mahal, dan rentan terhadap subjektivitas individu, sehingga tidak andal untuk skala besar. Tujuan kajian adalah menerapkan arsitektur AlexNet untuk meningkatkan efisiensi dan akurasi klasifikasi, lalu membandingkannya dengan convolutional neural network (CNN) buatan sendiri. Kelas yang dipakai adalah raw, ripe, dan rotten.

Data berasal dari perkebunan petani di Desa Durian Remuk, Kecamatan Muara Beliti, Kabupaten Musi Rawas, Sumatra Selatan, dengan luas sekitar 394 hektar. Citra diambil dengan kamera ponsel 128 megapiksel berformat JPG. Sejumlah 1.500 citra dibagi menjadi 500 citra per kelas. Susunan awal adalah 450 citra latihan dan 50 citra uji per kelas; 20% dari data latihan dipisahkan sebagai validasi, sehingga terdapat 1.080 citra latihan, 270 validasi, dan 150 uji. Citra awal berukuran 640 × 640 piksel, lalu diubah menjadi 224 × 224 piksel untuk pelatihan. Pra-pemrosesan mencakup segmentasi latar memakai ruang warna HSV, normalisasi nilai piksel ke rentang 0-1, serta augmentasi berupa zoom, rotasi, dan pergeseran horizontal serta vertikal.

Model pembanding terdiri dari tiga blok konvolusi, masing-masing berisi dua lapisan konvolusi dengan filter 3 × 3, diikuti max-pooling, flatten 36.864 unit, dua lapisan dense, dropout, dan softmax tiga kelas; jumlah parameter 2.438.563. AlexNet memakai lima lapisan konvolusi dengan filter 11 × 11, 5 × 5, dan 3 × 3, tiga lapisan max-pooling, flatten 256 unit, tiga lapisan dense berukuran 4.096, 4.096, dan 1.000 dengan dropout, lalu softmax tiga kelas; jumlah parameter 28.040.483. Kedua model dilatih selama maksimal 50 epoch dengan optimizer Adam, learning rate 0,00003, ukuran batch 32, EarlyStopping, dan ReduceLROnPlateau. Pelatihan dihentikan lebih awal pada epoch ke-28 untuk CNN dan epoch ke-21 untuk AlexNet.

Tabel 4 mencatat AlexNet mencapai loss validasi 0,0261 dan akurasi validasi 0,9962, sedangkan CNN mencatat 0,0377 dan 0,9925. Pada data uji, akurasi AlexNet 0,9900 dan CNN 0,9800; presisi, recall, dan skor F1 AlexNet masing-masing 0,99, sedangkan CNN 0,98. Teks menyatakan AlexNet lebih baik pula pada loss uji, tetapi Tabel 4 menunjukkan loss uji AlexNet 0,0646 lebih tinggi daripada CNN 0,0572. Pada matriks confusion 50 sampel per kelas, AlexNet mengklasifikasikan 49 dari 50 sampel rotten, 49 dari 50 ripe, dan 50 dari 50 raw; CNN mencatat 49, 48, dan 50. Dari 100 citra uji, AlexNet salah mengklasifikasikan 2 citra dan CNN 3 citra. Tidak ada interval kepercayaan atau uji signifikansi yang dinyatakan.

Penulis tidak menyediakan bagian batasan tersendiri. Pada bagian diskusi, penulis mengangkat pertanyaan tentang hubungan antara kompleksitas model dan kinerja serta perbandingan antara transfer learning dan model buatan sendiri, tanpa menyimpulkan batasan empiris. Penulis menyarankan penyelidikan lanjutan dengan VGGNet, DenseNet, EfficientNet, ResNet, dan Inception. Data hanya dapat diperoleh dengan menghubungi penulis sesuai alasan yang valid. Kajian ini mengklasifikasikan citra buah tunggal dan tidak membahas penghitungan tandan per pohon atau asosiasi lintas pandang.
