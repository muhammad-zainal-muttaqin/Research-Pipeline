# Classification of Oil Palm Fresh Fruit Bunches Based on Their Maturity Using Thermal Imaging Technique

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zolfagharnassab2022classification` |
| Judul asli | Classification of Oil Palm Fresh Fruit Bunches Based on Their Maturity Using Thermal Imaging Technique |
| Penulis | Zolfagharnassab, Shahrzad; Shariff, Abdul Rashid Bin Mohamed; Ehsani, Reza; Jaafar, Hawa Ze; Aris, Ishak Bin |
| Tahun | 2022 |
| Venue | Agriculture Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [zolfagharnassab2022classification.pdf](../pdf/zolfagharnassab2022classification.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture12111779

## Gambaran Umum

Penelitian ini mengatasi penentuan kematangan tandan buah segar (TBS) kelapa sawit, yang memengaruhi mutu minyak dan efisiensi pabrik. Cara penilaian yang biasa dipakai, yaitu pemeriksaan fisik buah, memakan waktu, mahal, dan rawan kesalahan manusia. Penulis mengusulkan pencitraan termal sebagai penentu kematangan yang tidak kontak, tidak merusak, cepat, dan sederhana di lapangan. Tujuannya mencari hubungan antara suhu rata-rata TBS hasil pencitraan termal dan kategori kematangan, lalu mengklasifikasikannya.

Data berupa 297 TBS kultivar Nigrescens yang dikumpulkan di United Plantation Research and Development (UPRD), Teluk Intan, Perak, Malaysia. Penelitian membagi data menjadi dua eksperimen, yaitu 147 sampel dan 150 sampel untuk validasi. Sampel dikelompokkan menjadi tiga kategori, yaitu belum matang (under-ripe), matang (ripe), dan terlalu matang (over-ripe), berdasarkan jumlah buah lepas: 0, 0–10, dan lebih dari 10. Sampel disimpan pada suhu ruang semalaman, diberi label, ditimbang, dan dinilai oleh grader terlatih. Citra termal diambil menggunakan kamera FLIR E60 dengan resolusi 320 × 240 piksel, sensitivitas termal 0,05 °C, dan rentang suhu −20 hingga 650 °C. Kalibrasi memakai emisivitas 95%, jarak tetap 1 meter, serta pencatatan kelembapan dan suhu lingkungan setiap tiga puluh menit. Citra diambil dari sisi depan dan belakang tandan.

Mekanisme klasifikasi bertumpu pada besaran selisih suhu, ∆Temp, yang dihitung sebagai suhu tandan dikurangi suhu lingkungan. Citra termal diproses dengan perangkat lunak ThermCAM Researcher Pro: derau dikurangi dengan filter median, daerah minat (region of interest) ditentukan berbentuk elips mengikuti bentuk tandan, lalu segmentasi ambang batas dan digitasi batas buah dipakai untuk mendapatkan suhu rata-rata. Penulis juga menguji ∆Temp dibagi berat tandan (∆Temp/Wt), tetapi membuangnya karena uji ANOVA menunjukkan perbedaan antarkategori tidak signifikan. Klasifikasi dilakukan di SPSS dengan empat metode, yaitu linear discriminant analysis (LDA), mahalanobis discriminant analysis (MDA), kernel nearest neighbor (KNN), dan artificial neural network (ANN) berjenis multilayer perceptron yang dilatih dengan back-propagation.

Hasil menunjukkan ∆Temp menurun konsisten seiring kematangan. Pada eksperimen pertama, rata-rata ∆Temp berturut-turut untuk under-ripe, ripe, dan over-ripe adalah 2,88 °C, 1,83 °C, dan 1,14 °C; pada eksperimen kedua, 3,19 °C, 2,07 °C, dan 1,26 °C. Uji ANOVA memberi nilai signifikansi di bawah 0,05 untuk ∆Temp, sehingga ketiga kategori berbeda secara statistik, dan uji t menunjukkan kedua eksperimen dapat diulang. Akurasi klasifikasi keseluruhan pada tahap uji adalah 85,4% (LDA), 81,8% (MDA), 74,2% (KNN), dan 92,5% (ANN); pada tahap latih, ANN mencapai 99,1%. Akurasi dinyatakan sebagai persentase sampel yang diklasifikasikan benar pada tahap latih dan tahap uji.

Batasan penulis: data tidak tersedia untuk umum karena pembatasan privasi. Penulis juga menyebut metode berbasis warna RGB terpengaruh perubahan pencahayaan, sedangkan pencitraan termal lebih tahan terhadap pencahayaan; batasan lain tidak dinyatakan.
