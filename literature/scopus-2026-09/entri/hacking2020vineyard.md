# Vineyard yield estimation using 2-D proximal sensing: A multitemporal approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hacking2020vineyard` |
| Judul asli | Vineyard yield estimation using 2-D proximal sensing: A multitemporal approach |
| Penulis | Hacking, Chris; Poona, Nitesh; Poblete-Echeverria, Carlos |
| Tahun | 2020 |
| Venue | Oeno One |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [hacking2020vineyard.pdf](../pdf/hacking2020vineyard.pdf)
- DOI resmi: https://doi.org/10.20870/oeno-one.2020.54.4.3361

## Gambaran Umum

Studi ini (Hacking dkk., 2020, *OENO One*) mencari tahap fenologi terbaik untuk mengestimasi hasil panen anggur dengan citra dua dimensi (2-D) dari jarak dekat (*proximal sensing*). Estimasi dilakukan pada dua tingkat: tandan (*bunch*) dan tanaman (*plant*). Penulis membandingkan dua teknik segmentasi tandan sebelum panen, yaitu *k-means clustering* (KMC) dan pengambangan warna (CT, *colour thresholding*). Segmentasi memisahkan piksel tandan dari latar belakang daun dan batang.

Data berupa akuisisi citra yang diulang setiap minggu pada kebun anggur dengan sistem tanaman tegak (*vertical shoot positioned*, VSP). Luas piksel tandan hasil segmentasi diregresikan terhadap massa tandan dalam gram, lalu divalidasi silang. Menurut abstrak, KMC mencapai akurasi segmentasi 0,942 dengan F1 0,948. Penulis mengklaim tidak ada studi hasil sebelumnya yang memakai segmentasi tandan tanpa pengawasan (*unsupervised*). Klaim ini merupakan pernyataan penulis dan belum diverifikasi ulang.

Hasil regresi pada tahap pematangan buah terakhir memberi r2 global 0,790 dengan RMSE 26,918 g. Penulis menyimpulkan bahwa KMC menghilangkan keharusan memilih ambang warna secara manual seperti pada CT, dan kedua teknik sama-sama baik. Estimasi terbaik diperoleh pada beberapa minggu terakhir sebelum panen (tahap E-L 36 sampai 38), dengan alternatif pada akhir pembentukan buah (E-L 33/34). Selama veraison (E-L 35), perubahan warna tandan secara signifikan menurunkan estimasi hasil. Karena itu penulis menyarankan penelitian berbasis warna menghindari jendela fenologi ini.

Penulis mencatat beberapa keterbatasan. Keterbatasan logistik membatasi ukuran sampel, dan keterbatasan teknik dicatat di bagian pembahasan. Dari sisi tinjauan ini, ringkasan studi hanya memuat satu sudut pandang per tanggal akuisisi, sehingga studi ini tidak menangani identitas lintas pandang. Angka r2 0,950 yang muncul di bagian pendahuluan berasal dari studi lain dan tidak dipakai sebagai hasil studi ini.
