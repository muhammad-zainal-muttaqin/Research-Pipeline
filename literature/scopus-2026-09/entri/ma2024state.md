# State-of-the-Art Techniques for Fruit Maturity Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ma2024state` |
| Judul asli | State-of-the-Art Techniques for Fruit Maturity Detection |
| Penulis | Ma, Jie; Li, Minjie; Fan, Wanpeng; Liu, Jizhan |
| Tahun | 2024 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple, mango, strawberry, cherry |

## Tautan Akses
- PDF: [ma2024state.pdf](../pdf/ma2024state.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy14122783

## Gambaran Umum

Tinjauan ini mengkaji teknik penentuan kematangan buah di lapang, yang masih sulit dilakukan secara tepat dan bergantung pada penilaian subjektif pekerja berpengalaman. Tahap panen menentukan penyimpanan, transportasi, masa jual, dan mutu buah; biaya tenaga kerja panen mencapai 30-50% dari total biaya produksi, dengan kebutuhan sekitar 30-35 jam tenaga terampil per acre untuk apel. Penulis menelaah tiga kelompok metode, yaitu analisis spektral, pengolahan citra digital tradisional, dan pembelajaran mendalam. Pencarian di Web of Science hingga September 2024 dengan kata kunci deep, learning, fruit, dan maturity detection menemukan 195 artikel. Tujuan tinjauan ini adalah merangkum kemajuan masing-masing metode, membandingkan kelebihan dan kekurangannya, serta mengidentifikasi tantangan penerapannya.

Analisis spektral memakai Raman imaging (RI), hyperspectral imaging (HSI), dan near-infrared (NIR) spectroscopy melalui akuisisi data, praproses, reduksi dimensi, pemilihan panjang gelombang, dan pemodelan kematangan. NIR menangkap perubahan padatan terlarut, keasaman, kadar air, dan pH, tetapi memerlukan kalibrasi dengan sampel yang konsentrasinya diketahui dan terpengaruh ketebalan buah di atas 10 mm. HSI menggabungkan informasi spektral dan spasial, sedangkan RI mengamati getaran ikatan kovalen. Metode tradisional mengekstraksi ciri warna (RGB, HSV, Lab, YCbCr), tekstur (GLCM, Gabor, BGLAM), dan bentuk, lalu memakai klasifier seperti SVM, K-means, decision tree, ANN, dan random forest. Pembelajaran mendalam memakai convolutional neural network (CNN) dalam detektor dua tahap (Faster R-CNN, Mask R-CNN) dan satu tahap (SSD, YOLO beserta turunannya), dengan perbaikan pada backbone, neck, dan prediction head seperti mekanisme atensi, fusi fitur, dan fungsi rugi yang dimodifikasi.

Tabel hasil yang disajikan menunjukkan kinerja yang tinggi pada sejumlah tanaman. Pada metode spektral, klasifikasi buah sawit memakai RI dan KNN mencapai presisi 90,9%, durian memakai NIR dan LDA 97,28%, stroberi memakai HSI dan PCA-SVM 99,17%, serta Camellia oleifera memakai HSI dan SPA 92,0%; regresi nanas memakai NIR dan PLSR menghasilkan koefisien korelasi 0,97. Pada citra tradisional, blueberry dengan HOG dan fitur Lab memakai KNN mencapai 92,06%, sawit dengan fitur warna dan ANN 98,3%, sawit dengan fitur tekstur dan SVM 93%, serta mulberry dengan ANN 98,26%. Detektor dua tahap menghasilkan mAP 98,14% pada buah, 98,40% pada kelapa, 96,14% pada tomat, dan 98,00% pada tomat sapi. Detektor satu tahap menghasilkan mAP 98,14% pada blueberry (YOLOv5), 97,42% pada tomat (YOLOv5), 98,7% pada apel (YOLOv5), 91,91% pada mangga (YOLOv4), dan 74,2% pada kopi (YOLOv8); satu kajian apel bahkan melaporkan mAP 99%. Angka-angka ini memakai metrik mAP untuk deteksi, presisi atau akurasi untuk klasifikasi, serta korelasi dan RPD untuk kalibrasi spektral, sesuai dengan pengukuran pada setiap kajian.

Penulis mencatat sejumlah keterbatasan. Faktor lingkungan berupa perubahan pencahayaan, tumpang tindih buah, oklusi, cahaya belakang, dan paparan berlebih mengganggu deteksi. Dataset kematangan buah terbuka masih langka; anotasi kotak pembatas dilakukan manual dan bersifat subjektif, sementara buah pada tahap kematangan berdekatan memiliki perbedaan ciri yang kecil. Metode spektral sensitif terhadap iluminasi, memerlukan perangkat keras mahal, dan HSI memakan waktu serta kapasitas penyimpanan besar; NIR terbatas pada deteksi titik tunggal dan distribusi komponen internal yang tidak merata. Pengolahan citra tradisional murah tetapi memiliki akurasi dan ketahanan rendah, sedangkan pembelajaran mendalam memerlukan dataset besar, biaya komputasi tinggi, dan memiliki keterbatasan interpretabilitas. Penulis juga mencatat bahwa buah berbentuk kerucut atau tumbuh menghadap atas, seperti polong teratai dan bunga matahari, belum banyak diteliti. Arah berikutnya mencakup HSI real-time berbiaya rendah, augmentasi dan generasi data, pembelajaran semi-terserelia, pemangkasan model, serta distilasi pengetahuan.

