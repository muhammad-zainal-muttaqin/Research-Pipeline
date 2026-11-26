# Ripeness level detection of oil palm fresh fruit bunches using K-means clustering algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sari2023ripeness` |
| Judul asli | Ripeness level detection of oil palm fresh fruit bunches using K-means clustering algorithm |
| Penulis | Sari, Wahyuni Eka; Metandi, Farindika; Kurniawati, Yulia Ery |
| Tahun | 2023 |
| Venue | Aip Conference Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [sari2023ripeness.pdf](../pdf/sari2023ripeness.pdf)
- DOI resmi: https://doi.org/10.1063/5.0120735

## Gambaran Umum

Kajian ini (AIP Conference Proceedings 2023) mengelompokkan kematangan tandan buah segar (TBS) kelapa sawit ke dalam empat tingkat, yaitu mentah, setengah matang, matang, dan lewat matang, dengan K-means berdasarkan warna. Pertanyaan utamanya adalah ukuran jarak mana yang memberi kelompok terbaik.

Data berupa 120 foto ponsel beresolusi 4000×3000 piksel atas TBS hasil panen 2021 dari kebun di Kalimantan Timur dan Kalimantan Utara. Citra dipotong ke bagian tandan, lalu fitur berupa rerata indeks warna R, G, dan B dihitung dari histogram. Sebanyak 80 citra dipakai sebagai data latih dan 40 sebagai data uji. Pusat kelompok awal ditetapkan dari indeks warna, dan tiga ukuran jarak dibandingkan: Euclidean, Manhattan, dan Chebyshev.

Koefisien *silhouette* adalah 0,232 untuk Euclidean, 0,240 untuk Manhattan, dan 0,242 untuk Chebyshev, sehingga Chebyshev dipilih. Pada 40 citra uji, 36 citra dikelompokkan benar (90%).

Semua nilai *silhouette* jauh dari 1, sehingga keempat kelompok warna tumpang tindih. Kajian ini mengelaskan satu tandan per citra yang sudah dipotong dan tidak mendeteksi atau mencacah tandan dalam adegan.
