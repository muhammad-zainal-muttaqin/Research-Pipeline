# Advancing palm oil fruit ripeness classification using transfer learning in deep neural networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kurniawan2025advancing` |
| Judul asli | Advancing palm oil fruit ripeness classification using transfer learning in deep neural networks |
| Penulis | Kurniawan, Rudi; Samsuryadi, Samsuryadi; Susilawati Mohamad, Fatma; Oktafia Lingga Wijaya, Harma; Santoso, Budi |
| Tahun | 2025 |
| Venue | Bulletin of Electrical Engineering and Informatics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kurniawan2025advancing.pdf](../pdf/kurniawan2025advancing.pdf)
- DOI resmi: https://doi.org/10.11591/eei.v14i2.8651

## Gambaran Umum

Kajian ini mengatasi identifikasi kematangan buah sawit yang dilakukan secara manual dan dianggap subjektif serta memerlukan banyak tenaga dan waktu. Tujuan kajian adalah menguji model pembelajaran mendalam berbasis transfer learning untuk mengklasifikasikan buah sawit ke dalam tiga kelas, yaitu raw, ripe, dan rotten. Penulis membandingkan VGG16, VGG19, ResNet152V2, DenseNet201, MobileNet, InceptionV3, dan Xception.

Data dikumpulkan dari perkebunan masyarakat di Desa Durian Remuk, Kecamatan Muara Beliti, Kabupaten Musi Rawas, Sumatra Selatan. Citra diambil dengan kamera ponsel 128 megapiksel dalam format JPG. Dataset terdiri dari 1.500 citra yang dibagi rata ke dalam tiga kelas. Susunan awal adalah 450 citra latihan dan 50 citra uji per kelas; dari data latihan diambil 20% sebagai validasi, sehingga akhirnya terdapat 1.080 citra latihan, 270 validasi, dan 150 uji. Seluruh citra diubah menjadi 640 × 640 piksel dan disimpan sebagai PNG, dengan latar belakang dihapus terlebih dahulu. Augmentasi terdiri dari penskalaan 1/255, zoom 0,1, rotasi 0,1 radian, serta pergeseran horizontal dan vertikal 0,1.

Model memakai arsitektur convolutional neural network dengan lapisan konvolusi, ReLU, max-pooling, lapisan penuh, dan softmax sebagai pengklasifikasi. Setiap arsitektur dilatih dengan bobot hasil pralatihan, lalu dievaluasi memakai matriks confusion matrix untuk menghitung akurasi, presisi, recall, dan skor F1. Kestabilan diuji dengan validasi silang lima lipat. Nilai hyperparameter spesifik seperti learning rate, ukuran batch, jumlah epoch, dan optimizer tidak dinyatakan dalam teks.

Pada Tabel 3, ResNet152V2 mencatat akurasi validasi 0,9888 dengan loss 0,0135 dan akurasi uji 1,0000 dengan loss 0,0316, serta presisi, recall, dan F1 sebesar 1,00. DenseNet201 dan MobileNet juga mencapai akurasi uji 1,0000, masing-masing dengan loss uji 0,0179 dan 0,0221. InceptionV3 mencatat akurasi uji 0,9866; Xception 0,9800; VGG16 0,9533; dan VGG19 0,9399. Validasi silang lima lipat memberi akurasi validasi 0,9861-0,9954 untuk ResNet152V2, 0,9907-1,0000 untuk DenseNet201, dan 0,9907-1,0000 untuk MobileNet. Abstrak menyebut ResNet152V2 sebagai model dengan akurasi tertinggi dan loss validasi terendah, tetapi Tabel 3 menunjukkan DenseNet201 dan MobileNet memiliki akurasi validasi lebih tinggi, yaitu 0,9962, sehingga pernyataan itu tidak sejalan dengan tabel.

Penulis menyatakan tiga batasan. Dataset belum mencakup keragaman penuh kondisi buah sawit di wilayah lain dan di bawah berbagai faktor lingkungan. Uji pada lingkungan operasional nyata belum dilakukan, sehingga diperlukan data yang lebih besar dan lebih beragam untuk memastikan kekuatan dan kepraktisan model. Penulis juga menyatakan tidak mengkaji secara mendalam pengaruh teknik augmentasi lain maupun penyetelan hyperparameter. Kajian ini mengklasifikasikan citra buah tunggal, bukan menghitung tandan per pohon atau mengaitkan pengamatan lintas pandang.
