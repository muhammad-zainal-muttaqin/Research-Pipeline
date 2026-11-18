# Detection of palm fruit maturity level in the grading process through image recognition and fuzzy inference system to improve quality and productivity of crude palm oil (CPO)

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `syaifuddin2020detection` |
| Judul asli | Detection of palm fruit maturity level in the grading process through image recognition and fuzzy inference system to improve quality and productivity of crude palm oil (CPO) |
| Penulis | Syaifuddin, A; Mualifah, L N A; Hidayat, L; Abadi, A M |
| Tahun | 2020 |
| Venue | Journal of Physics Conference Series |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [syaifuddin2020detection.pdf](../pdf/syaifuddin2020detection.pdf)
- DOI resmi: https://doi.org/10.1088/1742-6596/1581/1/012003

## Gambaran Umum

Penelitian ini menangani penentuan tingkat kematangan buah kelapa sawit dalam proses grading (penggolongan mutu). Proses grading di industri masih dilakukan secara manual oleh tenaga ahli, sehingga tidak efektif untuk skala besar. Penulis menyatakan bahwa mutu minyak sawit mentah (CPO) yang baik, dengan rendemen tinggi dan asam lemak bebas rendah, bergantung pada tingkat kematangan buah yang tepat. Kematangan tandan dikelompokkan menjadi tiga fraksi, yaitu mentah (*unripe*), matang siap panen (*ripe*), dan terlalu matang (*overripe*). Tujuannya adalah membangun sistem pengenalan tingkat kematangan dari warna luar buah secara langsung (*real time*).

Data berupa citra buah kelapa sawit yang dikumpulkan dan dipilih penulis; jumlah pasti sampel tidak dinyatakan, tetapi rincian hasil menyebut 78 data latih dan 21 data uji. Penelitian dilakukan dari Oktober 2018 hingga April 2019 dengan metode *research and development*. Tahapannya meliputi pengambilan dan penyortiran sampel, praproses citra (pemotongan, pengubahan ukuran, pengubahan ke citra keabuan), ekstraksi ciri dengan *Gray Level Co-occurrence Matrix* (GLCM), seleksi ciri dengan regresi metode *backward* memakai SPSS, pembagian data latih dan data uji, pengelompokan dengan *Fuzzy C-Means* (FCM), pembangunan sistem fuzzy, serta uji akurasi. Seluruh pemrosesan memakai MATLAB dan ditampilkan melalui antarmuka pengguna grafis (GUI).

Mekanisme pengenalan memakai ekstraksi tekstur GLCM yang awalnya menghasilkan 22 peubah. Seleksi regresi *backward* menyisakan delapan peubah signifikan sebagai masukan, yaitu uniformity (X1), inverse difference (X2), correlation (X3), homogeneity (X4), sum of squares (X5), difference entropy (X6), information measures of correlation (2) (X7), dan maximal correlation coefficient (X8). Pengelompokan FCM menghasilkan delapan klaster optimum yang ditentukan secara coba-coba; setiap klaster menjadi satu aturan *if-then*. Sistem memakai fungsi keanggotaan Gauss, model Sugeno orde pertama dengan konsekuen berupa persamaan linear yang diselesaikan dengan dekomposisi nilai singular (*singular value decomposition*), dan defuzzifikasi metode rata-rata bobot. Keluaran dibagi menjadi tiga himpunan fuzzy, yaitu 1 untuk buah mentah, 2 untuk buah matang, dan 3 untuk buah terlalu matang.

Akurasi dihitung sebagai jumlah data benar dibagi jumlah seluruh data dikali 100%. Pada data latih, akurasi sebesar 73,07% (57 dari 78 data), sedangkan pada data uji sebesar 71,4% (15 dari 21 data). Penulis menyatakan sejumlah faktor memengaruhi hasil sistem, meliputi data citra, tahap praproses, metode ekstraksi, metode dan jumlah peubah masukan, serta arsitektur sistem fuzzy. Penulis tidak menyebutkan keterbatasan lain secara eksplisit di luar faktor-faktor tersebut.

