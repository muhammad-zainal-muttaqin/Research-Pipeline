# Fruit yield prediction and estimation in orchards: A state-of-the-art comprehensive review for both direct and indirect methods

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `he2022fruit` |
| Judul asli | Fruit yield prediction and estimation in orchards: A state-of-the-art comprehensive review for both direct and indirect methods |
| Penulis | He, Leilei; Fang, Wentai; Zhao, Guanao; Wu, Zhenchao; Fu, Longsheng; Li, Rui; Majeed, Yaqoob; Dhupia, Jaspreet |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [he2022fruit.pdf](../pdf/he2022fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.106812

## Gambaran Umum

Tinjauan ini mengkaji prediksi dan estimasi hasil panen kebun buah sebelum panen. Data hasil panen diperlukan untuk keputusan manajemen tentang tenaga kerja, penyimpanan, transportasi, dan pemasaran, tetapi pendekatan manual dengan menghitung atau menimbang sampel di beberapa petak kecil memakan waktu dan rawan salah karena perbedaan antarpohon serta variasi parameter kebun. Penulis meninjau literatur 2010–2021 dari lima basis data, yaitu Engineering Village, Springer Link, Wiley Online Library, IEEE Xplore, dan Web of Science, dengan kata kunci kebun atau buah, hasil atau jumlah, serta prediksi atau estimasi. Proses tinjauan mengikuti tiga tahap mencari, memeriksa, dan menyintesiskan; hanya artikel jurnal yang disertakan dan seleksi awal dilakukan pada 500 hasil pertama.

Penulis membedakan dua jalur. Prediksi tidak langsung membangun model dari fitur yang berkorelasi dengan hasil, baik fitur lingkungan (suhu, radiasi surya, presipitasi, irigasi, pemupukan, konsumsi energi, komposisi lebah) maupun fitur tanaman (indeks vegetasi seperti NDVI, GNDVI, dan red-edge NDVI, struktur dan volume kanopi, kerapatan bunga). Fitur lingkungan memerlukan pengumpulan data panjang, sedangkan fitur tanaman lebih mudah diperoleh sehingga lebih sering dipakai. Model yang digunakan mencakup regresi linear, regresi berganda, PLSR, serta pembelajaran mesin seperti ANN, SVM, pohon keputusan, random forest, ELM, GPR, XGBoost, dan ANFIS. Angka dari kajian primer yang dikutip mencakup akurasi rata-rata 85,95%, R² 0,80, dan RMSE 0,5 kg per tanaman merambat untuk anggur; R² 0,71 dan RMSE 19,90 kg per pohon untuk apel; R² 0,83–0,87 untuk mangga; R² 0,963 dan RMSE 343,026 kg per hektar untuk blueberry liar dengan XGBoost; serta error prediksi di bawah 7% untuk mangga dengan ANN.

Estimasi langsung mendeteksi dan menghitung buah pada pohon memakai tiga kelompok platform: platform manual darat dengan kamera RGB, sensor RGB-D, atau ponsel cerdas; platform kendaraan bermotor dan traktor; serta UAV. Deteksi memakai ambang warna, SVM, circle Hough transform, pencocokan templat, dan jaringan CNN, R-CNN, Faster R-CNN, SSD, YOLO, serta RetinaNet. Penghitungan dibedakan menjadi penghitungan deteksi, regresi, penyambungan citra, dan pelacakan video dengan optical flow, Kalman filter, atau pelacakan multiobjek Bayes. Angka yang dikutip dari kajian primer mencakup mAP 72% dengan error relatif minimum 7% untuk Faster R-CNN pada beberapa jenis buah, presisi di atas 90% dengan pelacakan multiobjek Bayes untuk apel, akurasi 95,56%–97,83% dengan ambang warna untuk anggur, akurasi rata-rata sekurangnya 90% dengan FCN untuk mangga, F1 0,97 dengan MangoYOLO disertai error di bawah 15%, presisi 91% dengan Faster R-CNN untuk stroberi, AP 92% dengan RetinaNet untuk melon, serta error deteksi rata-rata 13,6% dengan regresi CNN untuk mangga.

Penulis mengemukakan sejumlah batasan. Pemilihan fitur dengan reduksi dimensi seperti PCA dan algoritma genetika menurunkan biaya pengumpulan data, tetapi dapat melemahkan daya adaptasi model ketika diterapkan di kebun lain. Waktu pengamatan data spektral penting karena indeks vegetasi berubah sepanjang fase pertumbuhan dan berkorelasi berbeda pada tiap tahap; model yang sama menunjukkan variasi besar antarkebun. Penutupan buah oleh dahan, batang, atau buah lain menjadi hambatan utama estimasi langsung. Faktor koreksi yang dihitung dari rasio buah tampak dan tersembunyi hanya memberi perbaikan terbatas, aliran udara menambah biaya dan mengaburkan citra, pencitraan banyak sudut menyebabkan penghitungan ganda, dan pelacakan video mudah gagal karena ciri individual buah kurang jelas dibanding pejalan kaki atau kendaraan. Penulis menyimpulkan bahwa lingkungan alam yang kompleks dan praktik hortikultura yang tidak seragam masih menjadi hambatan komersialisasi, sehingga diperlukan penggabungan rekayasa teknologi dan standarisasi pengelolaan agronomi serta kerja sama antara insinyur dan ahli hortikultura.

