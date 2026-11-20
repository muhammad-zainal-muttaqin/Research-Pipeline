# A vision-based robust grape berry counting algorithm for fast calibration-free bunch weight estimation in the field

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2020vision` |
| Judul asli | A vision-based robust grape berry counting algorithm for fast calibration-free bunch weight estimation in the field |
| Penulis | Liu, Scarlett; Zeng, Xiangdong; Whitty, Mark |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [liu2020vision.pdf](../pdf/liu2020vision.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2020.105360

## Gambaran Umum

Kajian ini mengusulkan metode penghitungan buah beri per tandan dari satu citra yang diambil dengan kamera smartphone. Masalah yang diangkat adalah penghitungan manual yang lambat dan tidak konsisten pada tandan yang tertutup daun dan buah lain. Hasil utamanya adalah estimasi jumlah beri per tandan dengan koefisien determinasi (R2) 0,82 sampai 0,95 terhadap hitungan manual, pada tahap perkembangan tandan yang berbeda.

Metode bekerja dengan menyegmentasi tandan dari latar menggunakan ambang Otsu, lalu mendeteksi tepi beri dengan operator Sobel dan transformasi Hough. Jumlah beri yang terlihat kemudian dikoreksi dengan model kemasan bola 3D. Model ini memakai faktor kerapatan (sparsity factor f) untuk memperkirakan beri yang tersembunyi di belakang beri lain. Kajian melaporkan akurasi 89% terhadap jumlah beri per tandan, dan akurasi di atas 99% jika dirata-ratakan pada 50 sampai 80 citra.

Keterbatasan utama ada pada pengambilan citra dari satu sisi. Beri pada sisi yang tidak terlihat tidak masuk hitungan, sehingga estimasi bergantung pada faktor kerapatan yang ditetapkan untuk tiap tandan. Kajian ini tidak membahas penggabungan citra dari beberapa pandang untuk menghindari hitungan ganda.
