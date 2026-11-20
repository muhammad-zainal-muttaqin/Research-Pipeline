# The Image Extraction Using the HSV Method to Determine the Maturity Level of Palm Oil Fruit with the k-nearest Neighbor Algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pusadan2023image` |
| Judul asli | The Image Extraction Using the HSV Method to Determine the Maturity Level of Palm Oil Fruit with the k-nearest Neighbor Algorithm |
| Penulis | Mohammad Yazdi Pusadan; Indah Safitri; Wirdayanti |
| Tahun | 2023 |
| Venue | Jurnal Resti |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [pusadan2023image.pdf](../pdf/pusadan2023image.pdf)
- DOI resmi: https://doi.org/10.29207/resti.v7i6.5558

## Gambaran Umum

Kajian ini membahas penyortiran tingkat kematangan buah kelapa sawit (*Elaeis guineensis* Jacq.) dengan bantuan pengolahan citra digital. Di perkebunan, buah sawit disortir secara manual dengan cara mengamati warnanya. Cara ini dinilai memakan waktu, terutama karena luas kebun yang tidak kecil. Kesalahan sortir juga sering terjadi ketika petugas membedakan buah matang dari buah mentah. Buah yang keliru tersortir tidak memenuhi kriteria kematangan di unit pengolahan, sehingga mutu minyak turun dan perusahaan dirugikan. Penulis mengusulkan sistem yang mengklasifikasikan buah sawit ke dalam kategori matang dan mentah. Sistem tersebut menggunakan algoritma *k-nearest neighbor* (k-NN) berdasarkan fitur warna *Hue Saturation Value* (HSV).

Data penelitian merupakan data primer yang diambil langsung di kebun PT. Unggul Widya Teknologi Lestari di Sulawesi Barat. Citra diambil dengan kamera pada jarak sekitar 20 sampai 30 cm. Platform yang digunakan adalah ponsel pintar. Jumlah data seluruhnya 400 citra, terdiri atas 200 citra buah mentah dan 200 citra buah matang. Pembagian data memakai metode *hold out* dengan rasio 70% data latih dan 30% data uji. Data latih berjumlah 280 citra, yaitu 140 citra buah mentah dan 140 citra buah matang. Data uji berjumlah 120 citra. Bagian metode menyebut 60 citra buah mentah dan 60 citra buah matang untuk data uji. Abstrak mencantumkan rincian yang berbeda, yakni 60 citra buah matang dan 45 citra buah mentah. Selain itu, pengujian langsung dilakukan pada buah di kebun perusahaan dan hasilnya dibandingkan dengan data Dinas Perkebunan dan Peternakan Kabupaten Pasangkayu.

Tahapan sistem terdiri atas akuisisi citra, prapemrosesan, ekstraksi fitur, dan klasifikasi. Prapemrosesan meliputi *cropping* untuk membuang bagian citra yang tidak diperlukan, *resize* untuk menyeragamkan ukuran, dan normalisasi nilai RGB agar setiap komponen warna dapat dibandingkan karena citra diambil pada intensitas cahaya yang berbeda. Nilai RGB yang sudah dinormalisasi kemudian dikonversi menjadi nilai HSV, dan nilai itulah yang menjadi masukan bagi k-NN. Kinerja sistem diuji dengan *confusion matrix* pada nilai k 5 dan 7. Hasil pengujian menunjukkan rata-rata akurasi sebesar 94,16%. Penulis menyebutkan bahwa target akurasi penelitian adalah di atas 75%. Penulis juga menyatakan bahwa penelitian ini bertujuan menutup celah penelitian sebelumnya, khususnya peningkatan akurasi dan penentuan rentang nilai ambang.
