# Maturity grading of oil palm fresh fruit bunches based on a machine learning approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `septiarini2020maturity` |
| Judul asli | Maturity grading of oil palm fresh fruit bunches based on a machine learning approach |
| Penulis | Septiarini, Anindita; Hatta, Heliza Rahmania; Hamdani, Hamdani; Oktavia, Ana; Kasim, Anita Ahmad; Suyanto, Suyanto |
| Tahun | 2020 |
| Venue | 2020 5th International Conference on Informatics and Computing Icic 2020 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [septiarini2020maturity.pdf](../pdf/septiarini2020maturity.pdf)
- DOI resmi: https://doi.org/10.1109/icic50835.2020.9288603

## Gambaran Umum

Penelitian ini mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit ke dalam tiga kelas, yaitu mentah (*raw*), kurang matang (*under-ripe*), dan matang (*ripe*). Ciri yang dipakai hanya warna. Penulis menyebut penilaian kematangan oleh manusia bersifat subjektif, padahal kandungan minyak bergantung pada tingkat kematangan saat panen: buah mentah berminyak rendah, buah kurang matang belum optimal, dan buah matang berminyak tinggi.

Data berupa 150 citra lokal yang diambil dengan kamera ponsel Samsung A50 pada jarak sekitar 10 cm dari tandan. Ukuran citra asli 4032 × 3024 piksel dalam format JPEG. Tempat pengambilan citra dan posisi tandan (di pohon, di tanah, atau di pabrik) tidak disebut. Data dibagi menjadi 60 citra latih (20 per kelas) dan 90 citra uji (30 per kelas). Label kelas diberikan menurut kelas sebenarnya; penilai labelnya tidak disebut.

Metodenya terdiri dari tiga tahap. Pertama, citra diperkecil menjadi 500 × 500 piksel untuk mempercepat komputasi. Kedua, citra diubah ke ruang warna L*a*b*, lalu dihitung empat ciri: rata-rata intensitas kanal L, a, dan b, serta rata-rata intensitas citra L*a*b*. Tidak ada segmentasi tandan; ciri dihitung dari seluruh sub-citra. Ketiga, ciri itu diklasifikasikan dengan *linear discriminant analysis* (LDA), yaitu pengklasifikasi terawasi yang mencari kombinasi linear ciri yang paling memisahkan kelas. Sebagai pembanding, ciri yang sama dihitung di ruang warna HSV, YCbCr, YIQ, dan RGB.

Akurasi keseluruhan pada 90 citra uji adalah 98,88% untuk L*a*b*, 97,77% untuk YCbCr, YIQ, dan RGB, serta 86,66% untuk HSV (abstrak menuliskan 98,89%). Kelas mentah dan matang mencapai 100% di empat ruang warna. Galat terkumpul di kelas kurang matang: akurasinya 96,66% di L*a*b*, 93,33% di YCbCr, YIQ, dan RGB, serta 76,66% di HSV. Penulis menyebut kesalahan yang paling sering adalah citra kurang matang yang diklasifikasikan sebagai mentah, karena warna tandan tidak tersebar merata.

Keterbatasan yang dapat diperiksa dari teks: setiap citra memuat satu tandan dari jarak dekat, tidak ada deteksi atau pencacahan tandan, dan tidak ada pembagian data menurut tandan atau pohon, sehingga belum diketahui apakah citra latih dan uji berasal dari tandan yang sama. Penulis mengusulkan pengembangan dengan gabungan beberapa ruang warna atau pembelajaran mendalam.
