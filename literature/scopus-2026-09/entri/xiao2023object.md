# Object Detection and Recognition Techniques Based on Digital Image Processing and Traditional Machine Learning for Fruit and Vegetable Harvesting Robots: An Overview and Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xiao2023object` |
| Judul asli | Object Detection and Recognition Techniques Based on Digital Image Processing and Traditional Machine Learning for Fruit and Vegetable Harvesting Robots: An Overview and Review |
| Penulis | Xiao, Feng; Wang, Haibin; Li, Yaoxiang; Cao, Ying; Lv, Xiaomeng; Xu, Guangfei |
| Tahun | 2023 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [xiao2023object.pdf](../pdf/xiao2023object.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy13030639

## Gambaran Umum

Tinjauan ini mengkaji teknik deteksi dan pengenalan objek berbasis pengolahan citra digital serta pembelajaran mesin tradisional untuk robot pemanen buah dan sayur. Biaya tenaga kerja pemanenan mencapai 30–50% dari total biaya produksi, sehingga robot pemanen menarik karena produktivitas tinggi dan biaya rendah. Akurasi, kecepatan, dan ketahanan deteksi serta pengenalan berhubungan langsung dengan efisiensi, mutu, dan kecepatan pemanenan. Kajian ini menjadi pasangan dari tinjauan Xiao dkk. tentang metode pembelajaran mendalam; fokusnya adalah metode klasik yang masih banyak dipakai sebelum era pembelajaran mendalam. Sistem penglihatan memakai kamera hitam putih, RGB, spektral, dan termal untuk memperoleh informasi warna, bentuk, tekstur, dan ukuran buah.

Penulis mengelompokkan metode pengolahan citra digital menjadi empat keluarga. Metode berbasis warna memakai ruang RGB, HSV, HSI, Lab, HSB, dan YCbCr serta ekstraksi histogram, himpunan, momen, dan vektor koherensi warna; metode ini cocok ketika warna buah sangat berbeda dari latar dan banyak dipakai di rumah kaca. Metode berbasis bentuk memakai fitur batas, deskriptor Fourier, faktor bentuk, dan momen invarians serta transformasi Hough lingkaran; metode ini kurang terpengaruh pencahayaan dan sesuai untuk buah bulat seperti apel dan sitrus. Metode berbasis tekstur memakai GLCM, Tamura, SAR, Gabor, dan wavelet, sedangkan metode fusi multifitur menggabungkan dua atau lebih fitur untuk mengatasi keterbatasan satu fitur. Angka yang dikutip dari kajian primer mencakup 81,6% untuk tomat matang dengan HSV dan segmentasi watershed, 96,1%/94,2%/86% untuk blueberry matang, setengah matang, dan muda, 91,3% dengan waktu 72 ms untuk apel memakai Hough, 98,3% untuk tandan buah sawit, serta 96,8% untuk stroberi terpisah berbanding 53,6% untuk stroberi tertutup.

Untuk segmentasi dan klasifikasi, penulis mengkaji enam keluarga pembelajaran mesin tradisional: K-means, SVM, KNN, AdaBoost, pohon keputusan, dan Bayes. SVM bekerja dengan mencari hyperplane pemisah berjarak maksimum dan di banyak kajian mengungguli KNN maupun pohon keputusan; SVM juga dapat menangani sampel sedikit, tetapi sensitif terhadap pemilihan fungsi kernel dan parameter serta kurang baik untuk klasifikasi banyak kelas. K-means cepat dan tidak memerlukan label, tetapi nilai K dan pusat awal yang dipilih secara acak sangat memengaruhi hasil. AdaBoost menggabungkan pengklasifikasi lemah menjadi pengklasifikasi kuat, namun rentan terhadap derau dan memerlukan waktu latih lama. KNN akurat dan tahan terhadap data abnormal, tetapi mahal secara komputasi. Pohon keputusan mudah diinterpretasi tetapi mudah overfitting, sedangkan Bayes sederhana dan cepat tetapi memerlukan probabilitas prior. Contoh angka dari kajian primer meliputi 98,8%/97,5% untuk litchi tak tertutup/tertutup sebagian dengan K-means, 91,67% dalam 26 ms untuk terong dengan SVM, 94,41% dalam 950 ms untuk tomat dengan SVM, 89,04% dalam 320 ms untuk paprika hijau dengan LSSVM, 96% untuk tomat dengan AdaBoost, 85,6% untuk sitrus hijau muda, 76% untuk impurities gandum dengan pohon keputusan, serta 93,13%/93,45%/93,24% untuk akurasi, presisi, dan sensitivitas deteksi jeruk.

Penulis mencatat bahwa studi yang melaporkan akurasi absolut dan perbandingan kinerja antarmetode dalam lingkungan yang sama sangat sulit ditemukan, sehingga diperlukan dataset dan kode yang dibuka serta dataset acuan yang terus diperbarui. Tantangan yang diuraikan mencakup latar yang mirip buah, buah mengelompok, tertutup sebagian, atau bergoyang, sensitivitas terhadap perubahan pencahayaan, pengenalan citra malam, kabur dan derau, waktu komputasi tinggi, serta kemampuan generalisasi. Metode tradisional umumnya sensitif terhadap data abnormal, memerlukan penetapan parameter di awal, bersifat spesifik untuk satu adegan, kurang efektif untuk banyak kelas, dan terutama dipakai untuk satu spesies di rumah kaca. Penulis menyimpulkan bahwa fusi multifikur dan SVM memberi akurasi lebih baik, dan menyarankan fusi banyak algoritma, pengoptimalan model, fusi data mult sensor, serta komputasi awan sebagai arah lanjutan. Secara keseluruhan, sistem penglihatan robot pemanen saat ini belum sepenuhnya memenuhi persyaratan komersialisasi.
