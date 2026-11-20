# Automatic counting of grapes from vineyard images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alsaffar2022automatic` |
| Judul asli | Automatic counting of grapes from vineyard images |
| Penulis | Al-Saffar, B.; others |
| Tahun | 2022 |
| Venue | Pakistan Journal of Agricultural Sciences |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [alsaffar2022automatic.pdf](../pdf/alsaffar2022automatic.pdf)
- DOI resmi: https://doi.org/10.21162/pakjas/22.644

## Gambaran Umum

Studi ini mengembangkan sistem penghitungan tandan dan buah sawit (*oil palm*) dari satu citra RGB. Penghitungan dilakukan per citra, sehingga setiap citra diproses sendiri tanpa mengaitkan buah yang sama di pandang lain. Sistem terdiri atas dua tahap. Tahap pertama mengklasifikasikan wilayah citra menjadi buah atau bukan buah dengan fitur buatan tangan (*handcrafted*), yaitu HOG (*histogram of oriented gradients*), LBP (*local binary pattern*), dan gabungan keduanya. Tahap kedua menghitung jumlah buah dan tandan dari hasil klasifikasi tersebut.

Ketiga kombinasi fitur diuji dengan tiga pengklasifikasi: ANN (jaringan saraf tiruan), SVM (*support vector machine*), dan CNN. Kombinasi terbaik adalah ANN dengan fitur HOG+LBP. Pada uji klasifikasi piksel, model ini mencapai akurasi 99,64±0,073%, presisi 99,70±0,094%, dan sensitivitas 99,59±0,117%. Angka ini mengukur kemampuan klasifikasi wilayah, bukan kemampuan menghitung tandan. Untuk penghitungan, studi melaporkan akurasi deteksi berry 89,82±2,58% dan akurasi deteksi bunch 91,72±2,88% (Tabel 2). Pada tiap lokasi, angka bunch adalah 89,75±4,78% di Adana, 96,25±2,97% di Tarsus, dan 89,22±0,876% di Iceland.

Pemisahan tandan yang bertumpuk memakai distance transform, connected components, dan k-means. Titik minat dicari dengan FRST (*fast radial symmetry transform*), lalu dikelompokkan dengan DBSCAN. Studi menyebut bahwa kontras rendah, bayangan, dan oklusi menurunkan kinerja. Keterbatasan ini ditulis dalam bahasa studi sendiri, dan belum ada pengukuran terpisah per kondisi tersebut.

Dataset pelatihan berasal dari Iceland, sedangkan uji kebun hanya memakai 17 citra dari Adana dan Tarsus. Jumlah citra uji yang kecil membatasi seberapa jauh angka akurasi dapat dibandingkan dengan studi lain. CNN memberi hasil lebih rendah karena data latihnya dinilai kurang.
