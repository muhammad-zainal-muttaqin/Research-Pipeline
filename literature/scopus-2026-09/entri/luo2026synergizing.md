# Synergizing Residual and Dense Architectures for Fine-Grained Oil Palm Grading: A Deep Feature Concatenation Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2026synergizing` |
| Judul asli | Synergizing Residual and Dense Architectures for Fine-Grained Oil Palm Grading: A Deep Feature Concatenation Approach |
| Penulis | Luo, Yang; P. P. Abdul Majeed, Anwar; Omar, Zaid; Jagtap, Sandeep; Garcia-Garcia, Guillermo; Chen, Yi |
| Tahun | 2026 |
| Venue | Mathematics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [luo2026synergizing.pdf](../pdf/luo2026synergizing.pdf)
- DOI resmi: https://doi.org/10.3390/math14050769

## Gambaran Umum

Kajian ini mengatasi penilaian mutu tandan buah segar (TBS) kelapa sawit yang masih mengandalkan tenaga manusia. Penilaian manual di lingkungan kebun yang tidak terstruktur bersifat padat karya, berbahaya, dan subjektif; penilai rentan lelah dan bias, sehingga salah mengelompokkan tandan dan menurunkan mutu minyak sawit kasar. Penulis berpendapat bahwa pendekatan convolutional neural network (CNN) konvensional yang hanya menambah kedalaman jaringan sering mengalami penurunan manfaat atau overfitting pada dataset berukuran sedang. Tujuan kajian adalah mengusulkan kerangka *Deep Feature Concatenation* (DFC) yang menggabungkan representasi dari dua arsitektur berbeda tanpa memperdalam satu jaringan, serta mempertahankan efisiensi komputasi untuk penempatan pada perangkat tepi.

Tanaman yang dikaji adalah kelapa sawit varietas Tenera. Dataset utama berisi 466 citra resolusi tinggi yang dikumpulkan langsung di beberapa perkebunan komersial di Johor, Negeri Sembilan, dan Perak, Malaysia, di bawah pencahayaan alami dengan bayangan, okklusi pelepah sebagian, dan variasi intensitas spektral. Penilai ahli membagi citra ke dalam lima kelas: matang (*ripe*, 201), mentah (*unripe*, 164), lewat matang (*overripe*, 74), rusak (*damaged*, 15), dan kosong (*empty*, 12). Ketimpangan kelas dan volume yang kecil diatasi dengan augmentasi luring berupa rotasi ±15°, pembalikan horizontal (p = 0,5), pemotongan acak (faktor skala 0,85–1,0, p = 0,7), serta gangguan fotometrik berupa kecerahan ±15 unit piksel dan kontras ±10 persen. Augmentasi menghasilkan 4.000 citra seimbang (800 per kelas). Untuk mencegah kebocoran data, penulis memakai pembagian berpasangan *Parent–Child*, yaitu citra asli beserta seluruh turunannya diperlakukan sebagai satu kelompok utuh, lalu dibagi menjadi latih (70 persen), validasi (15 persen), dan uji (15 persen) pada tingkat kelompok.

Mekanisme penghitungan memisahkan pembelajaran representasi dari inferensi. Citra berukuran 224 × 224 diekstraksi secara paralel oleh ResNet50 dan DenseNet121 yang telah dilatih pada ImageNet, dengan bobot dibekukan. Vektor dari lapisan *Global Average Pooling* masing-masing berdimensi 2.048 dan 1.024, lalu dikonkatenasi mentah menjadi vektor gabungan 3.072 dimensi tanpa normalisasi awal. Vektor gabungan distandardisasi memakai Z-score dengan statistik yang dihitung hanya dari data latih, kemudian direduksi dengan PCA hingga mempertahankan 99 persen varians terjelaskan, menghasilkan 984 dimensi. Klasifikasi dilakukan oleh probe linier dangkal (SVM, kNN, atau LR) yang hyperparameter-nya ditentukan lewat *GridSearchCV* dengan validasi silang 5 lipat bersarang di dalam partitioned latih. ResNet101 dan DenseNet201 dipakai sebagai pembanding untuk menguji apakah sekadar menambah kedalaman lebih baik daripada fusi fitur.

Evaluasi memakai akurasi, presisi, *recall*, dan F1-score makro pada cawat uji 15 persen, dengan interval kepercayaan 95 persen menurut metode Wilson serta uji McNemar pada α = 0,05. Konfigurasi DFC Raw dengan SVM mencapai akurasi uji tertinggi 97,75 persen (95 persen CI: 0,962–0,987) dan F1 makro 0,9755, lebih tinggi sekitar 1,2 persen daripada baseline terbaik ResNet50 + SVM (96,55 persen). Uji McNemar menunjukkan keunggulan DFC Raw atas ResNet50 signifikan untuk SVM (p = 0,039) dan kNN (p < 0,001), serta atas DenseNet121 untuk SVM (p = 0,004). Konfigurasi DFC Optimized memakai PCA menekan dimensi dari 3.072 menjadi 984 (penurunan 68 persen); dengan LR, akurasi 97,30 persen dan waktu konvergensi turun dari 272 detik menjadi kurang dari 4 detik, tanpa kehilangan akurasi yang signifikan (p = 1,000). Model mencapai 100 persen pada kelas rusak, kosong, dan lewat matang, serta 94,52 persen pada 73 citra asli tak teraugmentasi. Seluruh kesalahan terkonsentrasi pada transisi matang–mentah, dengan 8 citra mentah salah menjadi matang dan 6 citra matang salah menjadi mentah pada DFC Optimized.

Penulis menyatakan sejumlah batasan. Kajian bertumpu pada satu sumber data yang hanya berisi 466 citra asli lalu diperbesar menjadi 4.000 citra lewat augmentasi agresif; meskipun pembagian *Parent–Child* mencegah kebocoran langsung, jumlah sampel biologis unik tetap kecil, terutama untuk kelas langka rusak (n = 15) dan kosong (n = 12), sehingga rasio citra sintetis terhadap asli sangat tinggi dan sensitivitas 100 persen pada kelas tersebut lebih merupakan batas atas pemisahan fitur daripada bukti generalisasi lapangan. Tidak ada cawat uji eksternal independen, dan seluruh citra berasal dari satu wilayah geografis, sehingga bias situs seperti perbedaan latar daun, pencahayaan siang, dan kultivar lokal tidak dapat dikesampingkan. Penulis juga mencatat biaya komputasi fusi dua backbone (sekitar 7,0 GFLOP dan latensi GPU sekitar 18 ms) serta belum teruji generalisasi lintas kebun.

