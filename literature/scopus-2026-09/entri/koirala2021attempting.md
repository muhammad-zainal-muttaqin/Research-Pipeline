# Attempting to estimate the unseen—correction for occluded fruit in tree fruit load estimation by machine vision with deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `koirala2021attempting` |
| Judul asli | Attempting to estimate the unseen—correction for occluded fruit in tree fruit load estimation by machine vision with deep learning |
| Penulis | Koirala, Anand; Walsh, Kerry B.; Wang, Zhenglin |
| Tahun | 2021 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [koirala2021attempting.pdf](../pdf/koirala2021attempting.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy11020347

## Gambaran Umum

Penelitian ini mengatasi koreksi oklusi dalam estimasi beban buah pohon dari citra. Buah yang tersembunyi oleh daun atau buah lain tidak terhitung oleh penglihatan mesin, sehingga hasil hitungan citra perlu dikalikan faktor oklusi yang selama ini diestimasi manual dari pohon sampel. Penulis menguji hipotesis bahwa fitur kanopi pada citra memuat petunjuk jumlah buah tersembunyi, dan membandingkan lima metode prediksi beban buah langsung dengan metode patokan berupa hitungan MangoYOLO yang dikoreksi faktor oklusi.

Tanaman yang dipakai adalah mangga (*Mangifera indica* cv. Calypso) di tiga kebun di Queensland, Australia, dengan jumlah pohon 494, 121, dan 265. Citra dua sisi per pohon diambil pada malam hari dengan kamera RGB Basler acA2440 5 Mp dan panel LED 720 W yang dipasang pada platform bergerak 5 km/jam, pada musim 2017 (7–8 Desember) dan 2018 (13–14 Januari). Acuan hitung berupa panen tangan pada pohon sampel: 17, 6, dan 12 pohon pada 2017, diperluas menjadi 44, 19, dan 35 pohon (himpunan ABC-x, 98 pohon), serta 35 pohon pada 2018. Acuan kedua adalah hitungan packhouse untuk seluruh kebun.

Mekanisme penghitungan memakai MangoYOLO, modifikasi YOLOv3 dengan 33 lapisan yang dilatih pada 1.300 citra berisi 11.820 buah; jumlah kotak bounding box dihitung sebagai buah tampak. Model lain memprediksi beban buah langsung: MLP_yield dengan 12 peubah (arsitektur 12-6-1), Random_forest_yield dengan 100 pohon keputusan, Deep_yield yang menggabungkan MangoYOLO, MLP, regresi, Xception_siamese, dan Xception_classification, serta Xception_yield yang menerima citra gabungan dua sisi kanopi. Oklusi sebagian dipisahkan dari buah tampak penuh melalui ellipse fitting dengan ambang eksentrisitas 0,75. Xception_classification mengelompokkan kanopi ke dalam tiga kategori kerapatan buah memakai k-means. Sampel ABC-x 2017 dibagi 80:20 untuk latih dan uji pada MLP, Random Forest, dan Deep_yield, serta 90:10 untuk Xception_yield; citra 2018 dipakai sebagai cawat uji lintas musim.

Pada himpunan latih ABC-x 2017 terhadap hitungan tangan, Random_forest_yield mencapai R² = 0,98 dan RMSE = 17,8 buah per pohon, sedangkan Deep_yield R² = 0,92 dan RMSE = 30,4 dan MangoYOLO_yield R² = 0,69 dengan RMSE = 65,4. Terhadap hitungan packhouse seluruh kebun 2017, galat MLP_yield 1,6%, Random_forest_yield 2,3%, dan MangoYOLO_yield 13,6%. Pada cawat uji 2018 terhadap hitungan tangan, MangoYOLO_yield mencapai R² = 0,73, lebih tinggi daripada MLP_yield (0,66), Random_forest_yield (0,60), dan Deep_yield (0,34). Hitungan MangoYOLO mentah memiliki kemiringan 0,44 (2017) dan 0,32 (2018) terhadap panen, yang menunjukkan sebagian besar buah tidak tampak pada citra dua sisi.

Penulis menyatakan tidak ada fitur kanopi yang berkorelasi dengan jumlah buah tersembunyi: rasio buah oklusi sebagian terhadap buah tampak memiliki R² sebesar 0,007 (ABC-x 2017) dan 0,044 (ABC 2018) terhadap rasio buah tersembunyi. Model dengan pembelajaran langsung mengungguli metode patokan pada musim dan kebun sumber data latih, tetapi kinerjanya pada musim lain lebih rendah daripada metode referensi. Penulis menyatakan latih pada satu musim tidak cukup karena arsitektur pohon dan kerapatan daun berubah antarmusim dan antarkebun, lalu menyarankan pelatihan lintas beberapa musim dan kebun.

