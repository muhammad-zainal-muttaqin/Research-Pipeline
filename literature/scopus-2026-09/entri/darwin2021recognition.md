# Recognition of bloom/yield in crop images using deep learning models for smart agriculture: A review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `darwin2021recognition` |
| Judul asli | Recognition of bloom/yield in crop images using deep learning models for smart agriculture: A review |
| Penulis | Darwin, Bini; Dharmaraj, Pamela; Prince, Shajin; Popescu, Daniela Elena; Hemanth, Duraisamy Jude |
| Tahun | 2021 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple, citrus, grape, tomato, cucumber |

## Tautan Akses
- PDF: [darwin2021recognition.pdf](../pdf/darwin2021recognition.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy11040646

## Gambaran Umum

Tinjauan ini mengkaji penggunaan penglihatan mesin dan model pembelajaran mendalam untuk mengenali bunga dan buah pada citra tanaman guna estimasi hasil serta pertanian presisi. Penulis berangkat dari masalah bahwa penghitungan fisik buah muda, bunga, atau buah pada berbagai fase pertumbuhan bersifat padat karya dan mahal, sementara hasil panen berubah tiap tahun mengikuti iklim, tanah, dan pemupukan. Tinjauan ini juga mengaitkan estimasi hasil dengan kebutuhan data untuk skema asuransi tanaman di India, seperti percobaan pemotongan tanaman dan skema PMFBY, yang selama ini bergantung pada survei lapang berskala kecil. Komoditas yang dicakup mencakap buah anggur, apel, jeruk, dan tomat, serta tanaman tebu, jagung, kedelai, mentimun, dan gandum.

Sumber literatur dikumpulkan melalui penelusuran kata kunci "machine vision" dan "deep learning techniques in agriculture" pada IEEE Xplore, Scopus, Wiley Online Library, dan ScienceDirect; sekitar 50% makalah yang ditinjau terbit pada 2018–2020. Tinjauan ini memakai sejumlah himpunan data publik, antara lain Apple A (100 citra), Apple B (18 citra latih dan 30 citra uji), peach (24), pear (18), Apples (1.120), Mangoes (1.964), Almonds (620), dan Fruits 360 (82.213 citra). Alur kerja yang dirangkum mencakup akuisisi citra dari kamera darat, pencitraan jarak jauh Landsat 8 OLI dengan pan-sharpening, dan UAV berkamera RGB-NIR; peningkatan mutu citra dengan interpolasi bicubic atau bilinear, filter Gaussian dan median, serta perataan histogram; segmentasi berbasis ambang, warna, tekstur, bentuk, dan operasi morfologis seperti watershed; ekstraksi ciri warna, tekstur, HOG, SIFT, MSCR, dan Haar; lalu klasifikasi dengan CNN, DCNN, InceptionV3, YOLO, FRCNN, SVM, KNN, AdaBoost, BPNN, ANN, MLR, RVM, SNN, autoencoder, ResNet-50, VGG, dan GoogleNet.

Mekanisme utama yang dibahas adalah deteksi dan penghitungan buah atau bunga dari citra, penggunaan intensitas pembungaan untuk memprediksi hasil, dan penggabungan citra RGB dengan inframerah dekat untuk meningkatkan deteksi. Fusi citra RGB-NIR dengan logika kabur mencapai tingkat keberhasilan segmentasi 0,89, lebih tinggi daripada transformasi piramida Laplacian sebesar 0,72. Pendekatan structure-from-motion mengubah jejak dua dimensi menjadi penanda tiga dimensi sehingga mengurangi penghitungan ganda, dan model YOLO dilaporkan mendeteksi objek secara real time lebih cepat daripada FRCNN. Untuk estimasi hasil skala luas, penulis mencatat penggunaan produk MODIS seperti LAI, GPP, FPAR, ET, kelembapan tanah, dan EVI dengan pembelajaran mendalam, serta temuan bahwa data RGB lebih efektif daripada NDVI.

Berikut sejumlah angka hasil beserta metrik dan acuan hitungnya. Penulis menyimpulkan bahwa teknik pembelajaran mendalam mencapai akurasi rata-rata 92,51% pada beragam aplikasi pertanian, dengan skor F1 rata-rata sekitar 0,8 untuk klasifikasi. Robot pemanen apel Fuji di Iwate University mencapai akurasi 88%; deteksi kematangan tomat dengan BPNN mencapai 99,31% dengan simpangan baku 1,2%; AdaBoost untuk deteksi buah tomat mencapai 96% dengan waktu 15–24 detik; dan CNN termodifikasi Inception-ResNet mencapai 91% dengan waktu 0,006 detik. Prediksi hasil padi dengan MLR dan ANN menghasilkan RMSE 0,051, R = 0,99, dan MAE 0,041, sedangkan estimasi jagung, kedelai, dan gandum memakai weighted relevance vector machine menghasilkan akurasi 94,9%. Deteksi apel dengan MLP dan CNN menghasilkan F1 0,861 dan R² = 0,826; estimasi hasil mangga menghasilkan r² = 0,74; dan klasifikasi SVM serta kNN masing-masing mencapai 98,49% dan 98,50%. Metrik yang dipakai mencakup RMSE, MAE ternormalisasi, RRSE, koefisien korelasi, MAPE, presisi, recall, F-measure, kurva ROC, waktu sikap, serta keberhasilan pemanenan dan pelepasan buah.

Penulis menyatakan sejumlah batasan. Akuisisi citra dipengaruhi pencahayaan, bayangan, sudut dan jarak kamera, serta oklusi oleh daun, ranting, dan buah lain; pengambilan citra berulang juga dapat memicu penghitungan ganda. Segmentasi berbasis ambang bergantung pada pencahayaan dan pemilihan nilai ambang yang tidak selalu berlaku umum, sementara segmentasi tekstur dan bentuk memakan waktu serta menghasilkan batas yang kabur. Model pembelajaran mendalam memerlukan himpunan data besar sehingga menaikkan waktu komputasi, dan klasifikasi SVM dianggap rumit serta sensitif terhadap jenis data. Penulis menyatakan pula bahwa metode-metode tersebut masih perlu diuji untuk estimasi hasil waktu nyata dan dikembangkan lebih lanjut melalui teknik hibrida.
