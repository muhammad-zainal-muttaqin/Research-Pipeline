# Open-Source High-Throughput Phenotyping for Blueberry Yield and Maturity Prediction Across Environments: Neural Network Model and Labeled Dataset for Breeders

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2024open` |
| Judul asli | Open-Source High-Throughput Phenotyping for Blueberry Yield and Maturity Prediction Across Environments: Neural Network Model and Labeled Dataset for Breeders |
| Penulis | Zhang, Jing; Maleski, Jerome; Ashrafi, Hudson; Spencer, Jessica A.; Chu, Ye |
| Tahun | 2024 |
| Venue | Horticulturae |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [zhang2024open.pdf](../pdf/zhang2024open.pdf)
- DOI resmi: https://doi.org/10.3390/horticulturae10121332

## Gambaran Umum

Kajian ini mengatasi keterbatasan tenaga kerja dalam menentukan waktu kematangan dan hasil panen blueberry untuk keperluan pemuliaan. Waktu kematangan menentukan jendela panen, sedangkan hasil panen tinggi memberi keuntungan ekonomi. Selama ini, penilaian hasil panen untuk setiap aksesi pemuliaan dilakukan dengan penilaian visual yang bersifat kategorik dan subjektif. Penulis mengembangkan metode fenotiping berdaya guna tinggi berbasis jaringan saraf untuk memprediksi waktu kematangan sekaligus menyediakan pengganti ukuran hasil panen, lalu memublikasikan dataset berlabel dan model terlatihnya.

Citra warna asli dikumpulkan di dua lokasi. Di Alapaha, Georgia, citra 91 galur southern highbush dari 27 keluarga persilangan diambil pada 12 dan 23 Mei 2023 dengan kamera Panasonic Lumix DMC-LX10 beresolusi 5472 × 3648 piksel. Di Castle Hayne, Carolina Utara, citra diambil pada 19 Mei 2024 dengan kamera Canon EOS Rebel T7 beresolusi 6000 × 4000 piksel. Sekitar 80 citra mentah dipotong menjadi 5 × 3 keping berukuran maksimal 1200 × 1200 piksel, menghasilkan sekitar 466 keping. Anotasi dilakukan di Roboflow dengan dua kelas, yaitu buah matang dan buah belum matang (hijau atau merah muda). Citra diubah ke 640 × 640 piksel dan diaugmentasi dengan pembalikan horizontal, pemotongan 0–20%, rotasi ±15°, saturasi ±25%, dan blur hingga 2,5 piksel, sehingga dihasilkan 2.686 citra. Pembagian data adalah 80% latih, 14% validasi, dan 6% uji. Tiga versi YOLOv11 (nano, small, medium) dilatih selama 30 epoch dengan ukuran batch 8, ukuran citra 680, dan ambang keyakinan 0,4 pada NVIDIA GeForce RTX 4070 Ti memakai Ultralytics 8.3.13 dan PyTorch 2.4.0. Dataset dan model tersedia terbuka melalui Zenodo dan GitHub.

Mekanisme deteksi memakai YOLOv11 untuk mengenali setiap buah sebagai matang atau belum matang. Karena buah pada satu tanaman tidak masak bersamaan, waktu kematangan diperkirakan dari rasio buah matang terhadap total buah. Pengujian dilakukan pada sepuluh galur: buah dipanen tangan, dipisahkan menurut kelas, dan ditimbang; jumlah buah diestimasi dari berat total dibagi berat rata-rata 25 buah dikali 25. Prediksi model dijumlahkan dari seluruh keping citra satu tanaman, lalu dikorelasikan dengan hitungan panen tangan memakai korelasi Pearson. Pada 91 galur, penulis menghitung rasio kematangan dari prediksi model dan membandingkannya dengan penilaian visual teknisi pada skala 1–6, lalu melakukan analisis komponen utama terhadap jumlah buah dan rasio tersebut.

Metrik yang dihitung adalah presisi, recall, dan F1-score. YOLO11m memiliki kinerja tertinggi. Pada data validasi, kelas matang mencapai presisi 0,90, recall 0,91, dan F1 0,90; kelas belum matang mencapai 0,81, 0,79, dan 0,80. Pada data uji, kelas matang mencapai 0,89, 0,91, dan 0,90, sedangkan kelas belum matang mencapai 0,78, 0,76, dan 0,77. Pada sepuluh tanaman uji, model mendeteksi sekitar 25% buah (matang 16–34%, belum matang 12–44%); korelasi dengan panen tangan adalah r = 0,66 untuk jumlah buah matang, r = 0,86 untuk buah belum matang, dan r = 0,72 untuk rasio buah matang. Rasio matang rata-rata model dan panen tangan sama, yaitu 0,84. Pada 91 galur, jumlah buah total berkorelasi dengan jumlah buah matang (r = 0,90) dan belum matang (r = 0,84); penilaian visual berkorelasi dengan rasio matang (r = 0,84), tetapi berkorelasi negatif dengan jumlah buah belum matang (r = −0,80) dan total (r = −0,61). Analisis komponen utama menjelaskan 71% varians pada komponen pertama dan 23,2% pada komponen kedua, lalu membagi galur menjadi empat klaster dengan proporsi 28%, 20%, 24%, dan 13%.

Batasan yang dinyatakan penulis mencakup data latih yang hanya berasal dari tanaman southern highbush berusia 4–5 tahun dan citra yang diambil pada bulan Mei, sehingga kinerja dapat menurun pada tipe blueberry lain atau tahap pertumbuhan berbeda. Model hanya menangkap sekitar 25% hasil panen karena satu citra mencakup satu sisi tanaman; model cocok untuk sistem dengan arsitektur kanopi dan tahap pertumbuhan yang seragam. Buah yang terkena silau matahari sulit dikenali, sehingga penulis menyarankan penggunaan filter polarisasi, pengambilan citra saat cuaca berawan, dan jarak pengambilan yang tetap. Citra diambil pada satu titik waktu, sehingga perbandingan hasil total antargalur tidak memungkinkan. Penulis menyatakan generalisasi model dibatasi oleh keragaman dataset dan mengarahkan pekerjaan lanjutan pada perluasan data, sistem akuisisi otomatis, serta penerapan pada komputasi tepi.

