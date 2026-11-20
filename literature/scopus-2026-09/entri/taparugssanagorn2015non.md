# A non-destructive oil palm ripeness recognition system using relative entropy

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `taparugssanagorn2015non` |
| Judul asli | A non-destructive oil palm ripeness recognition system using relative entropy |
| Penulis | Taparugssanagorn, Attaphongse; Siwamogsatham, Siwaruk; Pomalaza-R\'aez, Carlos |
| Tahun | 2015 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [taparugssanagorn2015non.pdf](../pdf/taparugssanagorn2015non.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2015.09.018

## Gambaran Umum

Penelitian ini bertujuan memprediksi tingkat kematangan tandan buah segar (TBS) kelapa sawit secara tidak merusak. Waktu panen yang tepat sangat penting karena kandungan minyak buah berubah seiring tingkat kematangannya. Cara tradisional, seperti menghitung buah yang lepas dari tandan, dinilai tidak akurat, memakan waktu, dan menambah biaya panen. Penulis mengusulkan pendekatan pengolahan citra yang memanfaatkan *relative entropy*. Metode ini menghitung jarak *Kullback–Leibler* (KL) antara distribusi warna citra uji dan citra standar untuk setiap tingkat kematangan. Kelas dengan jarak terkecil dipilih sebagai hasil klasifikasi.

Data penelitian terdiri atas seratus citra TBS kelapa sawit jenis Nigrescens dalam ruang warna RGB. Citra diambil dengan kamera digital di bawah cahaya alami, sehingga tidak memerlukan pencahayaan khusus. Setiap tandan termasuk dalam salah satu dari tiga tingkat kematangan: sepenuhnya matang, sedang matang, dan belum matang. Setiap tingkat diwakili oleh satu citra standar. Sistem diuji dalam dua bentuk, yaitu skrip Matlab dan aplikasi seluler. Penulis menyatakan bahwa hasil aplikasi seluler sama dengan hasil Matlab.

Metode diuji dengan histogram warna berjumlah 4, 8, 16, dan 32 bin. Untuk setiap jumlah bin, jarak KL dibandingkan dengan jarak Euclidean yang lazim dipakai pada penelitian sebelumnya. Akurasi dihitung sebagai jumlah sampel yang benar dibagi jumlah seluruh sampel, dengan penilaian visual dari 25 pakar kelapa sawit sebagai acuan. Rata-rata akurasi di semua jumlah bin mencapai 96%. Hasil ini lebih tinggi daripada sistem logika fuzzy pada penelitian May dan Amaran (2011), yang mencapai 86,67%. Jarak KL memberikan hasil yang lebih baik daripada jarak Euclidean, dengan waktu komputasi yang hanya sedikit lebih lama. Rata-rata waktu komputasi untuk seratus sampel uji sekitar 3,5 detik menggunakan kode Matlab. Sebagai contoh, pada Tabel 1 dengan histogram 8 bin, sampel 1 memiliki jarak KL terkecil sebesar 0,2438 terhadap tingkat sedang matang.

Penulis menilai sistem ini sederhana dan berguna bagi petani serta pengusaha perkebunan. Dalam pembahasan, penulis menyebut dua kemungkinan penerapan, yaitu penilaian kualitas TBS di lokasi rampa sebelum masuk ke sterilizer dan pemanenan langsung di lapangan. Penilaian di rampa dianggap penting karena menentukan kapasitas pengolahan, dan sistem ini diharapkan menggantikan inspeksi visual manusia. Penulis juga menyatakan bahwa sistem dapat dipakai untuk ukuran citra apa pun. Keterbatasan utamanya adalah asumsi bahwa pengguna hanya memotret bagian tandan buah, bukan seluruh pohon atau kebun. Penulis tidak membahas lebih lanjut kondisi pencahayaan yang berbeda, variasi varietas di luar Nigrescens, atau jumlah sampel yang lebih besar sebagai batasan.
