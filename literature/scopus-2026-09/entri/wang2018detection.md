# Detection and counting of immature green citrus fruit based on the Local Binary Patterns (LBP) feature using illumination-normalized images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2018detection` |
| Judul asli | Detection and counting of immature green citrus fruit based on the Local Binary Patterns (LBP) feature using illumination-normalized images |
| Penulis | Wang, Chenglin; Lee, Won Suk; Zou, Xiangjun; Choi, Daeun; Gan, Hao; Diamond, Justice |
| Tahun | 2018 |
| Venue | Precision Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [wang2018detection.pdf](../pdf/wang2018detection.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-018-9574-5

## Gambaran Umum

Penulis menyatakan bahwa deteksi dan penghitungan buah jeruk hijau muda dengan kamera RGB dapat membantu peta hasil dini. Masalah utamanya adalah perubahan cahaya, oklusi acak, dan warna buah yang mirip daun. Penelitian ini mengusulkan normalisasi cahaya, deteksi kandidat, dan penyaringan dengan fitur tekstur. Teks menyebut hasil akurasi 85,6% pada set validasi.

Data berupa 100 citra kanopi jeruk dari kebun di Gainesville, Florida, pada Oktober 2015. Citra diambil dengan Canon PowerShot SD880IS dan diubah ke 800 × 600 piksel. Untuk latih dipakai 24 citra dengan 200 sampel buah dan 200 sampel bukan buah, masing-masing 24 × 24 piksel. Set validasi berisi 76 citra dengan 458 buah. Teks tidak menyebut pembagian per pohon.

Metode terdiri atas empat tahap. *Retinex* dan transformasi wavelet menormalkan cahaya. *K-means* pada warna hijau dan *circular Hough transform* (CHT) mencari kandidat lingkaran. *Local binary patterns* (LBP) mengubah tekstur menjadi kode biner per piksel, lalu *AdaBoost* menyaring positif palsu. Jendela 10 × 10 piksel mencari buah yang tersisa.

Hasil utama: metode usulan memperoleh 392 dari 458 buah benar (85,6%), dengan 54 positif palsu dan 66 terlewat. Metode 1 mencapai 329 benar (71,8%) dengan 113 positif palsu. Metode 2 mencapai 351 benar (76,6%) dengan 121 positif palsu. Waktu rata-rata 16.928 ms per citra.

Keterbatasan yang dapat diperiksa dari teks: validasi hanya 76 citra dari satu kebun dan satu kamera. Teks tidak menyebut cara pelabelan 458 buah sebagai acuan. Akurasi dihitung sebagai buah benar dibagi total buah acuan, bukan dengan metrik presisi atau recall.
