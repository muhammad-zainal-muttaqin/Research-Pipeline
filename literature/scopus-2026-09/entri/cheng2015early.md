# Early yield estimation of 'Gala' apple trees using image processing combined with support vector machine

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cheng2015early` |
| Judul asli | Early yield estimation of 'Gala' apple trees using image processing combined with support vector machine |
| Penulis | Cheng, H.; others |
| Tahun | 2015 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [cheng2015early.pdf](../pdf/cheng2015early.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2015.03.002

## Gambaran Umum

Kajian ini memperkirakan hasil panen apel "Gala" per pohon pada tahap awal, yaitu saat buah masih hijau (sekitar tiga bulan sebelum panen) dan setelah penjarangan buah. Penulis menyebut estimasi hasil dini sebagai dasar pengelolaan kebun yang presisi. Mereka juga menyebut bahwa model linear dari jumlah dan ukuran buah di citra tajuk kurang baik pada tahap ini. Alasannya, buah kecil dan banyak yang tertutup daun. Penulis mengusulkan lima fitur citra, termasuk fitur keterlindungan buah, yang menjadi masukan model *support vector machine* (SVM).

Citra diambil di kebun apel milik Universitas Bonn, Jerman (lokasi tertulis "Kein Altendorf"). Pohon berbentuk gelendong ramping. Setiap pohon dipotret satu kali dari sisi barat dengan kamera digital Canon PowerShot SX110 IS dalam kondisi berawan. Kain putih dipasang di belakang pohon, dan dua bola acuan berwarna merah dan putih digantung pada setiap pohon. Hasil panen sebenarnya diperoleh dengan menimbang semua apel setiap pohon. Set latih berisi 50 pohon dan set uji 15 pohon. Pembagian per pohon tidak dijelaskan lebih jauh. Citra diubah ke ukuran 512 × 683 piksel.

Citra tajuk disegmentasi di ruang warna YCbCr, yaitu ruang warna yang memisahkan kecerahan (Y) dari selisih biru (Cb) dan merah (Cr). Piksel apel dipilih dengan syarat Cb ≤ 100 dan Cr ≥ 120. Daun dipilih dengan Cr ≤ 125 pada citra yang buahnya sudah dihapus. Operasi morfologi dan deteksi lingkaran Hough (untuk bola acuan) melengkapi proses ini. Jumlah buah dihitung dari area terhubung. Area lebih besar dari satu bola dihitung dua buah, dan area lebih besar dari dua bola dihitung tiga buah. Lima fitur adalah jumlah buah, luas buah terhadap luas citra, rasio luas buah terhadap daun, proporsi jumlah buah terlindung, dan proporsi luas buah terlindung. SVM regresi dengan kernel RBF memakai pencarian grid.

Pada set latih, R² adalah 0,7242, MAPE 9%, dan MFE 0,21. RMSE-nya 1,71 kg. Pada 15 pohon uji, MAPE adalah 13% dan RMSE 2,45 kg. Pada set uji yang sama, jaringan saraf BP mencapai RMSE 2,64 kg dan MAPE 14%, sedangkan model linear dari informasi buah saja mencapai RMSE 4,63 kg dan MAPE 31%. Penulis menyatakan model lima parameter paling baik karena MSE pelatihan paling kecil (0,00117 dibanding 0,00160 untuk dua parameter).

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Set uji hanya 15 pohon dari satu kebun, satu kultivar, dan satu musim. Setiap pohon hanya dipotret dari satu sisi dalam cuaca berawan, dan penulis menyatakan pengaruh cahaya lain dan citra dua sisi belum diteliti. Ambang warna ditentukan dari citra yang sama. Penulis menyatakan cara penghitungan buah masih perlu diperbaiki. Hitungan buah dari citra tidak dibandingkan dengan hitung tangan, sehingga galat hitungnya tidak dilaporkan.
