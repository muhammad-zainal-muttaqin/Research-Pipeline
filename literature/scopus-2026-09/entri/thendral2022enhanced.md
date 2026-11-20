# An Enhanced Computer Vision Algorithm for Apple Fruit Yield Estimation in an Orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `thendral2022enhanced` |
| Judul asli | An Enhanced Computer Vision Algorithm for Apple Fruit Yield Estimation in an Orchard |
| Penulis | Thendral, R.; David, D. Stalin |
| Tahun | 2022 |
| Venue | Lecture Notes in Electrical Engineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [thendral2022enhanced.pdf](../pdf/thendral2022enhanced.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-16-6448-9_27

## Gambaran Umum

Pendugaan hasil panen buah penting bagi pengelola kebun. Data jumlah buah membantu petani dan pengemas merencanakan tenaga kerja, ruang penyimpanan, jumlah wadah panen, dan strategi pemasaran. Pada praktiknya, pendugaan masih dilakukan secara manual dengan menghitung buah satu per satu. Cara ini padat karya, memakan waktu, kurang akurat, dan mahal. Penulis menghitung jumlah apel per pohon lalu mengalikannya dengan jumlah pohon per acre untuk memperkirakan total hasil. Kajian ini bertujuan mengembangkan algoritma penglihatan komputer yang mengenali dan menghitung apel matang pada pohon di bawah cahaya matahari alami. Algoritma memanfaatkan filter *Discrete Wavelet Transform* (DWT) dan segmentasi berbasis warna.

Kajian ini menggunakan 20 citra buah apel pada pohon. Penulis mengumpulkan citra tersebut secara acak dari internet. Setiap citra memuat banyak buah. Citra diambil dalam kondisi cahaya alami siang hari tanpa sumber cahaya buatan. Citra berupa gambar warna RGB dari satu pandang, yang memperlihatkan potongan pohon. Teks tidak merinci jenis kamera, platform, atau ukuran citra. Teks juga tidak menyebut pembagian data latih dan data uji. Penulis menyatakan algoritma divalidasi dengan 20 citra tersebut. Tabel 2 membandingkan jumlah hitungan manual dan jumlah hitungan algoritma untuk setiap pohon, beserta selisih dan deteksi keliru.

Penulis membandingkan enam metode penghalusan citra, yaitu filter rata-rata, Gaussian, median, bilateral, Wiener, dan DWT. Perbandingan memakai *root mean square error* (RMSE) dan *peak signal-to-noise ratio* (PSNR). Filter DWT memberi nilai terbaik, yaitu RMSE 0,01 dan PSNR 36,66 dB. Filter Gaussian memberi PSNR 34,83 dB. Tahap segmentasi mengubah citra RGB ke model warna *YIQ*. Komponen I dipilih karena memuat piksel buah dan sedikit latar belakang, sedangkan komponen Y dan Q memuat banyak latar belakang. Citra komponen I kemudian diubah menjadi citra biner. Penulis menerapkan operasi morfologi berupa erosi dan pengisian, lalu membuang objek kecil yang tidak diperlukan. Hasil akhir dibandingkan dengan hitungan manual. Penulis melaporkan korelasi yang erat antara keduanya. Akurasi algoritma mencapai 93 persen dengan tingkat kesalahan keseluruhan 1,5 persen.

Penulis tidak merinci batasan metode secara terpisah. Dalam kesimpulan, penulis menyatakan bahwa penelitian lanjutan akan mengintegrasikan algoritma ini dengan lengan manipulator robot pemanen. Pendahuluan juga menyebutkan bahwa pendekatan lain sering menghasilkan positif palsu karena bagian tanaman lain. Catatan itu merujuk pada kajian terdahulu, sehingga bukan batasan yang diakui penulis untuk metode ini.
