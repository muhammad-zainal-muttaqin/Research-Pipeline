# MangoYieldNet: Fruit yield estimation for mango orchards using DeepLabv3 + with ResNet18 architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `maheswari2025mangoyieldnet` |
| Judul asli | MangoYieldNet: Fruit yield estimation for mango orchards using DeepLabv3 + with ResNet18 architecture |
| Penulis | Maheswari, Prabhakar; Raja, Purushothaman; Natarajan, Sudha |
| Tahun | 2025 |
| Venue | Multimedia Tools and Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [maheswari2025mangoyieldnet.pdf](../pdf/maheswari2025mangoyieldnet.pdf)
- DOI resmi: https://doi.org/10.1007/s11042-025-20791-5

## Gambaran Umum

MangoYieldNet (Multimedia Tools and Applications, 2025) memperkirakan hasil kebun mangga dari citra pohon. Buah disegmentasi dengan DeepLabv3+ berbasis ResNet18 lalu dicacah dengan transformasi Hough lingkaran.

Dari 1.000 pohon di satu kebun, 278 pohon dipilih dengan rumus ukuran sampel dan mencakup tajuk lebat, sedang, dan jarang. Setiap pohon difoto dari dua sisi dengan DSLR pada jarak 5 m, sehingga terkumpul 556 citra 3980×2650 piksel. Label segmentasi dibuat per piksel di CVAT. Dengan augmentasi, data menjadi 1.152 citra yang dibagi 80:20. Uji terpisah memakai 30 citra dari dua sisi 15 pohon, dengan akurasi rerata 96,5% dan IoU rerata 95,97%.

Gerombol buah dibedakan dari buah tunggal menurut diameter lingkaran, sampai lima buah per gerombol. Untuk 278 pohon, jumlah hitungan model adalah 26.929 dan hitungan petani 28.345, dengan R2 0,98 pada regresi hitungan per pohon. Bobot dihitung dari jumlah buah dengan asumsi 100 buah per 20 kg, dan galat bobot total 4,99%.

Hitungan per pohon berasal dari dua citra tanpa penautan buah antarcitra. Penulis menyebut hitung ganda akibat dua sisi dan buah yang tertutup sebagai sumber galat. Hitungan acuan berasal dari petani, dan cara memperolehnya tidak dijelaskan.
