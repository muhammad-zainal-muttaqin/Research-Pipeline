# Federated Learning for Grading Oil Palm Fruit Ripeness in the Oil Palm Industry

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `laddawong2025federated` |
| Judul asli | Federated Learning for Grading Oil Palm Fruit Ripeness in the Oil Palm Industry |
| Penulis | Laddawong, Patchanee; Pianroj, Yutthapong; Chotikawanid, Piyanart; Punvichai, Teerasak; Jumrat, Saysunee; Kham-Ouam, Atitaya; Muangprathub, Jirapond |
| Tahun | 2025 |
| Venue | Applied Computational Intelligence and Soft Computing |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [laddawong2025federated.pdf](../pdf/laddawong2025federated.pdf)
- DOI resmi: https://doi.org/10.1155/acis/9241523

## Gambaran Umum

Ladda Wong dkk. (2025) dalam *Applied Computational Intelligence and Soft Computing* menerapkan *federated learning* (FL, yaitu pelatihan model bersama tanpa memindahkan data mentah antarlokasi) untuk mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit dari citra RGB. Setiap pabrik melatih model lokal sendiri, dan hanya parameter model yang dikirim ke pusat untuk dirata-ratakan dengan *Federated Averaging* (FedAvg). Model global mencapai akurasi 90,0%.

Data latih berjumlah 5.209 citra, dibagi menjadi 2.571 citra *single-palm* dan 2.638 citra *multipalm*. Citra mencakup empat tingkat kematangan (raw, semiraw, semiripe, dan ripe) dan empat varietas, diambil di dalam dan di luar ruangan. Citra berukuran 4032 × 3024 piksel diubah menjadi 640 × 640 piksel. Evaluasi memakai matriks kebingungan, akurasi, MAE, dan RMSE, dengan validasi silang 5 lipatan. Pembagian data mengikuti lokasi pabrik.

Tabel 6 membandingkan model global dengan empat model pabrik. Model global memakai 5.029 input dan mencapai akurasi 90,0%, RMSE 0,02, dan MAE 0,10. Model pabrik 1 memakai 102 input dan mencapai akurasi 93,5%, RMSE 0,03, dan MAE 0,10. Model pabrik 2 memakai 100 input dan mencapai akurasi 92,5%, RMSE 0,05, dan MAE 0,12. Model pabrik 3 memakai 99 input dan mencapai akurasi 95,0%, RMSE 0,01, dan MAE 0,09. Model pabrik 4 memakai 100 input dan mencapai akurasi 96,0%. Penulis menyatakan bahwa model pabrik 3 dan 4 paling akurat dan paling yakin, sedangkan model global memiliki keyakinan prediksi yang lebih rendah. Gambar 5 menampilkan akurasi dan loss per epoch hingga 50 epoch. Penulis juga menyatakan bahwa pilihan model bergantung pada kesesuaian tiap situasi. Abstrak juga menyebut aplikasi web untuk validasi.
