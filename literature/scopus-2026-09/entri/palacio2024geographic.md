# Geographic-Scale Coffee Cherry Counting with Smartphones and Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `palacio2024geographic` |
| Judul asli | Geographic-Scale Coffee Cherry Counting with Smartphones and Deep Learning |
| Penulis | Rivera-Palacio, Juan Camilo; Bunn, Christian; Rahn, Eric; Little-Savage, Daisy; Schmidt, Paul G\"unter; Ryo, Masahiro |
| Tahun | 2024 |
| Venue | Plant Phenomics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | cherry, coffee |

## Tautan Akses
- PDF: [palacio2024geographic.pdf](../pdf/palacio2024geographic.pdf)
- DOI resmi: https://doi.org/10.34133/plantphenomics.0165

## Gambaran Umum

Kajian ini menghitung cherry kopi (*Coffea arabica*) per pohon dari foto yang diambil dengan ponsel pintar. Tujuannya menyediakan cara penghitungan yang murah bagi petani kecil yang tidak memiliki kamera khusus atau sensor kedalaman. Setiap pohon difoto pada tiga cabang, satu foto per cabang. Model deteksi objek YOLO v8 menghitung cherry pada tiap foto. Jumlah buah per pohon diperkirakan dari rerata buah per cabang dikalikan jumlah cabang produktif.

Data dikumpulkan pada 2022 dari 8.904 foto di dua negara. Di Peru, lokasinya di Junín dan Piura. Di Kolombia, lokasinya di Cauca dan Quindío. Kegiatan itu melibatkan hampir 1.000 petani kecil. Model dilatih pada data Peru, lalu diuji pada data Peru dan Kolombia. Data uji mencakup 2.450 pohon di Kolombia dan 518 pohon di Peru, yang menghasilkan 7.350 foto di Kolombia dan 1.554 foto di Peru. Protokol pengambilan foto memakai satu cabang per posisi, tiga posisi per pohon, dan satu foto per cabang.

Mutu deteksi diukur dengan presisi dan recall. Pada ambang keyakinan yang dipilih penulis, presisi 0,85 dan recall 0,13. Model jadi jarang keliru saat menandai buah, tetapi melewatkan sebagian besar buah yang ada. Korelasi antara jumlah buah terhitung dan jumlah buah sebenarnya berbeda menurut posisi cabang. Korelasi tertinggi tercatat pada posisi bawah, cabang 3. Pada data Peru, R2 tercatat 0,59 menurut abstrak. Di Kolombia, R2 keseluruhan adalah 0,71. Nilai R2 per varietas berkisar 0,82 sampai 0,99, sehingga penulis mencatat variasi antarvarietas.

Ketika seluruh data uji Kolombia dan Peru digabung, performa keseluruhan adalah R2 0,72, MAE 252,63 cherry per pohon, MAPE 41,74%, dan RMSE 621,46 cherry per pohon. Korelasi di tingkat pohon cukup tinggi, tetapi galat absolutnya besar. MAE lebih dari 250 buah per pohon dan MAPE 41,74% berarti estimasi per pohon bisa meleset jauh dari jumlah sebenarnya. Angka ini hanya berlaku untuk model yang dilatih di Peru dan diuji di dua negara, dengan protokol satu foto per cabang.
