# Towards perspective-free object counting with deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `onororubio2016perspective` |
| Judul asli | Towards perspective-free object counting with deep learning |
| Penulis | O\~noro-Rubio, Daniel; L\'opez-Sastre, Roberto J. |
| Tahun | 2016 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [onororubio2016perspective.pdf](../pdf/onororubio2016perspective.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-46478-7_38

## Gambaran Umum

Oñoro-Rubio dan López-Sastre (2016) mengusulkan penghitungan objek tanpa memperhatikan sudut pandang (*perspective-free*) dengan regresi peta densitas. Jaringan konvolusi memprediksi peta densitas dari citra, lalu jumlah objek diperoleh dengan menjumlahkan nilai peta. Kajian ini menguji dua arsitektur, yaitu CCNN (*Counting CNN*) dan Hydra CNN, pada dua dataset kendaraan dan kerumunan.

Penghitungan objek dengan deteksi kotak mengalami kesulitan pada objek yang tumpang tindih dan pada kerumunan padat. Kajian ini mengusulkan regresi densitas sebagai alternatif, dengan alasan bahwa jumlah objek dapat diperoleh dari integral peta densitas tanpa menemukan setiap objek secara terpisah.

Setiap objek dalam citra latih diberi peta densitas dengan jumlah total satu. Jaringan belajar memetakan patch citra ke peta densitas. Pada saat uji, jumlah prediksi adalah jumlah nilai peta densitas pada seluruh citra.

- CCNN memakai patch 72×72 dan menghasilkan peta densitas 18×18, dilatih dengan loss Euclidean.
- Hydra CNN memakai *pyramid* multi-skala dengan satu kepala per skala. Body *fully-connected* berukuran Fc6 512, Fc7 512, dan Fc8 324.

Metrik utama adalah GAME(L), yang membagi citra menjadi 4^L region dan menjumlahkan MAE tiap region. GAME(0) setara dengan MAE.

Pada TRANCOS, GAME(0) untuk CCNN adalah 12,49, untuk Hydra 2s 11,41, dan untuk Hydra 3s 10,99. Dua metode pembanding [5] dan [6] memperoleh 17,77 dan 13,76. Hydra 3s memberi GAME(3) terkecil, yaitu 19,32.

Pada UCF CC 50, MAE CCNN adalah 488,67 dan MSD 646,68.

Secara konseptual, regresi densitas tidak memerlukan kotak batas, sehingga cocok untuk objek yang tertutup sebagian. Dari sisi bukti, kajian ini hanya menguji kendaraan dan kerumunan. Tidak ada pengujian pada buah, daun, atau tandan, dan jarak kamera serta skala objeknya berbeda dari kebun.
