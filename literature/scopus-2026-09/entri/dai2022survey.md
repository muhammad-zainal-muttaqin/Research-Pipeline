# A survey of detection-based video multi-object tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dai2022survey` |
| Judul asli | A survey of detection-based video multi-object tracking |
| Penulis | Dai, Yan; Hu, Ziyu; Zhang, Shuqi; Liu, Lianjun |
| Tahun | 2022 |
| Venue | Displays |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [dai2022survey.pdf](../pdf/dai2022survey.pdf)
- DOI resmi: https://doi.org/10.1016/j.displa.2022.102317

## Gambaran Umum

Kajian ini merupakan survei tentang *multiple object tracking* (MOT) berbasis deteksi pada video. Penulis menyatakan bahwa MOT telah menjadi isu penting dalam bidang visi komputer, tetapi masih sulit dikerjakan. Penyebabnya antara lain perubahan tampilan objek yang mendadak dan oklusi yang berat. Tujuan tinjauan ini adalah merangkum perkembangan algoritma MOT selama sekitar satu dekade terakhir, lalu membandingkan hasil kuantitatifnya.

Tinjauan ini menjelaskan cakupan aplikasi MOT yang luas. Aplikasinya meliputi keamanan publik, lalu lintas kota, militer, kendaraan otonom, dan siaran olahraga. Penulis tidak menguji data baru. Mereka menyajikan hasil publik dari empat puluh algoritma pada dataset MOTChallenge, dengan tabel terpisah untuk MOT16 dan MOT20. MOT20 dirilis pada tahun 2020 dan memuat kategori seperti pejalan kaki, kendaraan, dan sepeda. Hasil dibagi menjadi kelompok *private detection* dan *public detection*, serta kelompok metode *online* dan *offline*.

Bagian metode membahas prinsip dasar MOT, kerangka umum algoritmanya, kesulitan teknis, dan solusi yang sudah ada. Penulis lalu mengklasifikasikan algoritma menjadi metode *online* dan *offline*, dan menyusun perkembangannya dalam linimasa dari tahun 2016 hingga 2020. Metrik evaluasi yang dibahas meliputi MOTA, IDF1, dan komponen seperti false positive, false negative, serta jumlah pertukaran identitas. Dari sisi hasil, penulis menemukan bahwa algoritma terbaik pada MOT16 dan MOT20 memakai deteksi privat. Temuan ini menegaskan bahwa kualitas deteksi menentukan performa pelacak. Metode *online* sedikit lebih baik daripada *offline*, tetapi metode *online* sering menghasilkan banyak pertukaran identitas dan fragmentasi trajektori. Hal ini terjadi karena metode tersebut tidak memperoleh informasi dari bingkai berikutnya saat terjadi oklusi atau deteksi yang hilang. Performa algoritma juga membaik dari tahun 2016 hingga 2022.

Penulis menyebutkan beberapa batasan. Pertama, perbandingan langsung antarmetode pada dataset yang sama mungkin tidak adil, karena kualitas detektor memengaruhi hasil akhir. Kedua, sebagian metode terlalu disesuaikan dengan dataset tertentu sehingga sulit digeneralisasi. Ketiga, metode yang menggabungkan observasi dari banyak sudut pandang tidak sebanding dengan metode yang hanya memakai satu sudut pandang, sehingga hanya metode yang sebanding yang dimasukkan ke tabel. Keempat, ruang lingkup dibatasi pada dataset MOTChallenge karena keterbatasan ruang penerbitan. Penulis juga menyatakan bahwa tinjauan ini menyusun arah riset masa depan dengan menganalisis kesamaan dari beberapa metode yang berkinerja baik.
