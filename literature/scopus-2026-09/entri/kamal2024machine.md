# Machine Vision for Automated Maturity Grading of Oil Palm Fruits: A Systematic Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kamal2024machine` |
| Judul asli | Machine Vision for Automated Maturity Grading of Oil Palm Fruits: A Systematic Review |
| Penulis | Kamal, Afsar; Kamarudin, Nur Diyana; Bin Ahmad, Khairol Amali; Rahayu, Syarifah Bahiyah; Mohd Isa, Mohd Rizal; Makhtar, Siti Noormiza; Yaakub, Zulkifli |
| Tahun | 2024 |
| Venue | Machine Graphics and Vision |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kamal2024machine.pdf](../pdf/kamal2024machine.pdf)
- DOI resmi: https://doi.org/10.22630/mgv.2024.33.2.3

## Gambaran Umum

Tinjauan sistematis ini mengkaji penggunaan pembelajaran mesin, khususnya pembelajaran mendalam, untuk mengotomatisasi penilaian tingkat kematangan tandan buah segar kelapa sawit. Kematangan menentukan mutu minyak dan produktivitas di Indonesia, Malaysia, dan Thailand, sementara metode tradisional bersifat memakan waktu, banyak tenaga, dan rawan kesalahan. Penulis menelaah kelebihan dan keterbatasan tiap kajian, teknik praproses citra yang dipakai untuk melatih model, serta prospek pengembangan berikutnya. Convolutional neural network (CNN) diidentifikasi sebagai metode klasifikasi dominan karena kemampuannya mempelajari fitur yang kompleks.

Rangkaian metode yang dirangkum mencakup praproses, klasifikasi, dan model pembelajaran mendalam. Akuisisi citra memakai kamera RGB, pencitraan hiperspektral (HSI), dan pencitraan inframerah dekat (NIR) pada panjang gelombang 700-2.500 nm. Praproses meliputi peningkatan mutu citra, pengubahan ukuran, normalisasi warna, segmentasi, ekstraksi ciri, penskalaan ciri, dan augmentasi data. Segmentasi memakai ambang batas Otsu, deteksi tepi Canny dan Sobel, wilayah, U-Net, K-means, serta fuzzy C-means. Ekstraksi ciri mencakup histogram, transformasi, tekstur, dan ciri statistik; penskalaan memakai Min-Max, Z-Score, PCA, dan CLAHE. Klasifikasi tradisional mencakup decision tree, KNN, SVM, dan logistic regression, sedangkan metode pembelajaran mendalam mencakup CNN, RNN, generative adversarial network (GAN), serta ensemble seperti random forest dan gradient boosting machine.

Tabel perbandingan yang disusun penulis memperlihatkan rentang kinerja yang luas. Dengan 48 sampel yang dibagi menjadi 32 data latih dan 16 data uji, PCA mencapai akurasi 99,2%; CNN pada 120 sampel (96 latih, 24 uji) mencapai 100% [98]. SVM berbasis fitur warna mencapai 57% dan bag of visual words 70% [40], sedangkan ResAtt DenseNet dan DenseNet Sigmoid masing-masing 69% [111]. Pada deteksi dan klasifikasi, YOLOv4-Tiny 3L menghasilkan mAP 90,56% pada 57 sampel [58], YOLOv4-512 mencapai 88,94% pada 4.160 sampel [109], dan deep neural network (DNN) menghasilkan akurasi keseluruhan 99,35% serta akurasi Kappa 98,49% pada 13.218 sampel [56]. Ringkasan model pembelajaran mendalam mencatat AlexNet 100% [49], VGG-16 98,13% [127], YOLOv3 97,28%, YOLOv4 97,74%, dan YOLOv4-CSPDarknet53 dengan mAP 97,64% [58]. Angka-angka ini dihitung dari partisi data latih dan uji yang tercantum di setiap kajian; metode deteksi YOLO dilaporkan dengan metrik mAP, bukan akurasi klasifikasi.

Penulis menyatakan sejumlah keterbatasan pada kajian yang ditinjau, terutama ukuran dataset yang terbatas serta pengaruh variasi lingkungan dan regional terhadap kinerja model. Kondisi pencahayaan, derau, dan keterbatasan mutu citra menjadi kendala dalam praproses, sementara kompleksitas komputasi model pembelajaran mendalam menjadi pertimbangan tersendiri. Tinjauan ini tidak memakai dataset eksternal dan mengarahkan penelitian lanjutan pada pendekatan spektral-visual serta quantum deep learning (QDL) untuk meningkatkan ketepatan penilaian kematangan.
