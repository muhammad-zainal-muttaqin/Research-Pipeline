# In-field blueberry fruit phenotyping with a MARS-PhenoBot and customized BerryNet

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025field` |
| Judul asli | In-field blueberry fruit phenotyping with a MARS-PhenoBot and customized BerryNet |
| Penulis | Li, Zhengkun; Xu, Rui; Li, Changying; Munoz, Patricio; Takeda, Fumiomi; Leme, Bruno |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [li2025field.pdf](../pdf/li2025field.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110057

## Gambaran Umum

Li dkk. (2025) menyusun sistem fenotipe lapangan untuk blueberry. Robot bergerak di antara baris tanaman dan memotret tiap tanaman dari tiga pandang: atas, kiri, dan kanan. Model deteksi bernama BerryNet, yang dibangun di atas YOLOv8, mendeteksi klaster buah dan mensegmentasi tiap buah pada citra pandang tunggal. Hasil ketiga pandang kemudian digabung untuk memperkirakan jumlah buah per tanaman, jumlah klaster, rasio buah matang, dan kerapatan klaster.

Pada abstrak, deteksi klaster mencapai mAP50 54,9% dan segmentasi buah mencapai mAP50 85,8%. Estimasi hasil dari gabungan hitungan tiga pandang menghasilkan MAPE 23,1% dan R2 0,73 terhadap panen manual pada 26 tanaman dari 17 genotipe. Kematangan memiliki galat MAE sekitar 5%. Studi ini tidak melakukan pencocokan identitas buah lintas pandang.

Ground truth diperoleh dengan memanen manual 26 tanaman, 13 tanaman pada 12 April 2023 dan 13 pada 9 Mei 2023. Semua buah, baik belum matang, semi matang, maupun matang, dihitung. Untuk tiap tanaman, bingkai dari tiga pandang dipotong agar hanya memuat satu tanaman, lalu dianotasi dengan kotak pembatas.

Penggabungan pandang dilakukan dengan dua cara. Jumlah buah per tanaman dimodelkan dengan regresi linear berganda, Ymulti = a0 + a1Ytop + a2Yleft + a3Yright (persamaan 5). Jumlah klaster per tanaman dihitung sebagai rerata tiga pandang, Cmulti = Mean(Ctop, Cleft, Cright) (persamaan 6). Karena tidak ada ground truth klaster, rerata ini dipakai sebagai pengganti. Kedua cara bekerja pada hitungan per pandang. Tidak ada langkah yang menentukan apakah dua buah di pandang berbeda adalah buah yang sama.

Keterlihatan (visibility) didefinisikan sebagai rasio buah beranotasi dalam satu pandang terhadap jumlah buah hasil panen manual (persamaan 7). Penulis menyebut oklusi sebagai sumber galat utama, tetapi keterlihatan tidak dipakai untuk mengoreksi penggabungan.

Rasio buah matang per tanaman dihitung dari mask yang diprediksi, lalu dirata-ratakan di tiga pandang (persamaan 8 dan 9). Kompaktnes klaster dihitung sebagai luas mask buah dibagi luas persegi panjang terkecil yang melingkupi mask (persamaan 10). Dari setiap tanaman, 50% klaster terpadat dipilih. Jarak antarbuah dinormalisasi dengan diameter setara mask dan dihitung dari tetangga terdekat berbasis Voronoi. Perbedaan antargenotipe diuji dengan ANOVA (P = 0,05) dan uji Tukey HSD.

Analisis hanya memakai tiga pandang dan 26 tanaman. Regresi berganda dilatih pada jumlah tanaman yang kecil, sehingga kemampuan generalisasinya ke kebun lain belum diuji. Dari sisi evaluasi, studi ini mengukur galat hitungan terhadap panen manual, bukan jumlah buah unik. Karena itu kesalahan penggabungan lintas pandang, jika ada, tercampur dengan galat deteksi dan oklusi. Kajian ini tidak menyediakan data untuk memisahkan keduanya.
