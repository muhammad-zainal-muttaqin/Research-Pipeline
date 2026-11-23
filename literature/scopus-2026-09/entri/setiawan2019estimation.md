# Estimation of Nigrescens Palm Oil Ripeness using Contrast and Skewness from 680 nm Image

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `setiawan2019estimation` |
| Judul asli | Estimation of Nigrescens Palm Oil Ripeness using Contrast and Skewness from 680 nm Image |
| Penulis | Setiawan, Agung W.; Danudirdjo, Donny; Ananda, Alfie R. |
| Tahun | 2019 |
| Venue | Proceedings 2019 International Seminar on Intelligent Technology and Its Application Isitia 2019 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [setiawan2019estimation.pdf](../pdf/setiawan2019estimation.pdf)
- DOI resmi: https://doi.org/10.1109/isitia.2019.8937225

## Gambaran Umum

Kajian ini mengestimasi tingkat kematangan buah sawit varietas *nigrescens* dari citra yang diambil dengan cahaya LED 680 nm. Penulis menyebut bahwa penilaian manual bersifat subjektif dan bergantung pada pengalaman penilai. Warna kulit *nigrescens* juga tidak berubah jelas selama pematangan. Tujuan kajian adalah menguji apakah *kontras* dan *skewness* (kemiringan distribusi intensitas) citra 680 nm dapat dipakai sebagai fitur sederhana.

Data mencakup 101 tandan buah segar. Kelas ditetapkan penilai senior dengan pengalaman lebih dari sepuluh tahun di pabrik pengolahan sawit. Data latih berisi 24 tandan (16 mentah, 7 matang, dan 1 terlalu matang). Data uji berisi 77 tandan (39 mentah dan 38 matang). Empat LED 680 nm menyinari tandan dari jarak sekitar 30 cm, dan kamera digital merekam citra di ruangan tertutup. Teks tidak menyebut tanaman atau apakah citra diambil di pabrik atau di kebun.

Citra berwarna diubah menjadi keabuan, lalu kontras dan skewness dihitung dari citra itu. Klasifikasi memakai *Classification Learner* di MATLAB. Kontras diklasifikasikan dengan *ensemble bagged trees*, yaitu sekumpulan pohon keputusan. Skewness diklasifikasikan dengan *linear discriminant*, yaitu pemisah linear antarkelas. Teks menyebut pemilihan algoritme dilakukan dengan akurasi pada data latih.

Hasil utama pada data uji: akurasi kontras 64,94%, skewness 68,83%, dan kombinasi kontras dengan skewness 68,83%. Penulis memilih skewness karena akurasinya sama dengan kombinasi dan lebih sederhana. Dari matriks kebingungan (Tabel V), 53 dari 77 tandan benar. Teks menyebut akurasi data latih 68,83% di satu bagian, tetapi Tabel IV memuat akurasi 66,67% untuk data latih kombinasi.

Keterbatasan yang dapat diperiksa: hanya satu tandan terlalu matang di data latih dan tidak ada tandan terlalu matang di data uji. Tidak ada pembagian per pohon. Hanya satu kamera dan satu jarak pemotretan. Teks tidak menyebut akurasi per kelas secara tertulis. Dua pernyataan akurasi data latih tidak konsisten satu sama lain.
