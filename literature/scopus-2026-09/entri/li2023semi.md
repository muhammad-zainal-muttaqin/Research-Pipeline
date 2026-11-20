# Semi-supervised Counting of Grape Berries in the Field Based on Density Mutual Exclusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2023semi` |
| Judul asli | Semi-supervised Counting of Grape Berries in the Field Based on Density Mutual Exclusion |
| Penulis | Li, Yanan; Tang, Yuling; Liu, Yifei; Zheng, Dingrun |
| Tahun | 2023 |
| Venue | Plant Phenomics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [li2023semi.pdf](../pdf/li2023semi.pdf)
- DOI resmi: https://doi.org/10.34133/plantphenomics.0115

## Gambaran Umum

Li dkk. (2023) mengusulkan CDMENet, metode penghitungan objek berbasis density map dengan pelatihan semi-supervised. Di Tabel 1, CDMENet dengan 50% label mencapai MAE 26,47, RMSE 36,32, dan R² 0,9839.

Metode ini memakai backbone VGG16 dengan gaya CSRNet dan dilated convolution berlaju (rate) 2. Density map dibentuk dengan menaruh kernel Gaussian bersigma 15 pada setiap titik anotasi, lalu jumlah nilai density map dipakai sebagai hitungan objek. Pelatihan semi-supervised memakai dua tambahan. Pertama, tugas bantu segmentasi biner untuk setiap level kepadatan, dengan aturan saling eksklusif antarlevel (density mutual exclusion). Kedua, density difference loss yang mengukur kemiripan arah antara prediksi dan target memakai cosine similarity. Tugas bantu ini memanfaatkan citra yang tidak berlabel titik.

Tabel 1 membandingkan beberapa setting. CDMENet dengan 10% label mencapai MAE 30,57, RMSE 40,21, dan R² 0,9787. CDMENet dengan 50% label mencapai MAE 26,47, RMSE 36,32, dan R² 0,9839. TasselNetV2+ dengan 100% label mencapai MAE 41,03, RMSE 55,00, dan R² 0,9647. Baris TasselNetV2+ memakai seluruh label, sedangkan baris CDMENet 10% memakai sebagian kecil label. Karena jumlah label berbeda, pembaca perlu membandingkan per baris dengan hati-hati dan tidak merata-ratakannya.

Penulis mengklaim bahwa dibanding state of the art, R² naik 6,10%, sedangkan MAE dan RMSE turun masing-masing 49,36% dan 54,08%. Angka persentase ini belum dicocokkan dengan baris pembanding tertentu di Tabel 1.

Dari sisi tinjauan, studi ini mengukur hitungan per citra. Ia tidak mengukur apakah buah yang sama terlihat di beberapa pandang, sehingga tidak menjawab masalah deduplikasi lintas pandang.

Kajian ini relevan sebagai bukti bahwa density map dengan label sebagian dapat menurunkan galat hitungan pada tanaman berbuah kecil. Hasilnya belum menunjukkan kinerja pada sawit atau pada citra dari beberapa sisi.
