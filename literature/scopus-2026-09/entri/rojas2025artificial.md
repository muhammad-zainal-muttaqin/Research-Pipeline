# Artificial Vision Systems for Fruit Inspection and Classification: Systematic Literature Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rojas2025artificial` |
| Judul asli | Artificial Vision Systems for Fruit Inspection and Classification: Systematic Literature Review |
| Penulis | Rojas Santelices, Ignacio; Cano, Sandra; Moreira, Fernando; Pe\~na Fritz, \'Alvaro |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [rojas2025artificial.pdf](../pdf/rojas2025artificial.pdf)
- DOI resmi: https://doi.org/10.3390/s25051524

## Gambaran Umum

Tinjauan sistematis ini mengkaji sistem visi buatan untuk inspeksi mutu dan sortasi buah. Pemeriksaan manual memakan waktu, bersifat subjektif, dan rawan kesalahan manusia, sehingga diperlukan sistem otomatis yang mendeteksi cacat, menilai kematangan, dan menentukan kelas buah. Penulis merumuskan tiga pertanyaan: bidang aplikasi, konfigurasi perangkat keras akuisisi, serta algoritma dan teknik pemrosesan citra yang paling umum. Sistem dipakai di tiga lingkungan, yaitu kebun untuk pemanenan dan pemantauan, lini pengolahan industri untuk sortasi, dan titik konsumsi seperti pasar swalayan untuk menilai kesegaran.

Penelusuran mengikuti pedoman PRISMA pada basis data Web of Science dan Scopus dengan kata kunci terkait klasifikasi buah, deteksi cacat, visi mesin, dan pemrosesan citra. Pencarian awal menghasilkan 505 artikel; setelah diterapkan filter tahun 2015–2024, jenis dokumen, bahasa Inggris, dan akses terbuka, 310 dokumen dikeluarkan. Perangkat Mendeley menghilangkan 126 duplikat sehingga tersisa 69 artikel; penyaringan judul dan abstrak serta pemeriksaan teks lengkap menghasilkan 56 artikel final.

Alur pemrosesan citra terdiri dari prapemrosesan, segmentasi, ekstraksi ciri, dan klasifikasi. Prapemrosesan memakai filter Gaussian, peningkatan kontras dan ketajaman, normalisasi RGB, konversi ke ruang warna HSV atau CIE L*a*b*, serta augmentasi berupa rotasi, perubahan kecerahan, dan pencerminan. Segmentasi memakai operator tepi Sobel dan Canny, ambang batas Otsu, pengelompokan *mean shift*, dan *watershed*; teknik ini sering digabung, misalnya Sobel untuk kontur awal lalu Canny untuk perbaikan. Ekstraksi ciri mencakup warna, tekstur, bentuk, ukuran, dan ciri spektral; model pembelajaran mendalam seperti VGG-16, ResNet, DenseNet, dan YOLO dipakai bersama ciri klasik. Klasifikasi memakai CNN, model pralatih yang disesuaikan lewat *transfer learning*, serta algoritma seperti SVM, regresi linear, KNN, dan ANN.

Kamera RGB mendominasi akuisisi (84%), diikuti kamera hiperspektral (5%), ponsel pintar (5%), multispektral (4%), dan radiofrekuensi (2%); 61% kajian memakai cahaya lingkungan, sedangkan lini industri memakai lampu LED di dalam kubah pencitraan. Sebanyak 74% studi memakai dataset sendiri, 24% dataset patokan, dan 2% keduanya; dataset patokan yang dipakai meliputi Fruit 360 hingga 65.429 citra dan FruitNet 19.526 citra. Sekitar 70% artikel terbit antara tahun 2020 dan 2024, dengan India (11 studi), Tiongkok (9), serta Spanyol dan Iran (masing-masing 4) sebagai negara paling produktif. Tujuan klasifikasi terbanyak adalah jenis buah (32%), kematangan (23%), dan varietas (16%). Model FruitVision berbasis MobileNetV3 mencapai akurasi 97,96–99,50%, dengan 99,50% pada pisang dibandingkan 98,84% untuk DenseNet201; analisis diskriminan linear pada belimbing memberi akurasi kalibrasi 96,2% dan validasi 93,3%.

Penulis menyatakan perbandingan langsung antarstudi tidak memungkinkan karena setiap kajian memakai dataset, kondisi akuisisi, dan tujuan yang berbeda, sehingga tidak ada konsensus mengenai konfigurasi optimal. Variasi buah, pencahayaan, dan oklusi tetap menjadi tantangan; sebagian besar percobaan dilakukan di laboratorium, dan pelatihan CNN memerlukan dataset besar berlabel serta penyesuaian hyperparameter secara coba-coba yang memakan waktu. Penulis menyarankan standarisasi konfigurasi untuk meningkatkan reproduktibilitas, serta pengembangan algoritma adaptif dan sistem ringan berbasis MobileNet untuk perangkat tepi. Penulis menyatakan tidak ada konflik kepentingan; pendanaan berasal dari Fundação para a Ciência e a Tecnologia, proyek UIDB/05105/2020.
