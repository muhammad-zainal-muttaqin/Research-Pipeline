# Multi-Object Multi-Camera Tracking Based on Deep Learning for Intelligent Transportation: A Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fei2023multi` |
| Judul asli | Multi-Object Multi-Camera Tracking Based on Deep Learning for Intelligent Transportation: A Review |
| Penulis | Fei, Lunlin; Han, Bing |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [fei2023multi.pdf](../pdf/fei2023multi.pdf)
- DOI resmi: https://doi.org/10.3390/s23083852

## Gambaran Umum

Tinjauan ini membahas pelacakan banyak objek dengan banyak kamera berbasis pembelajaran mendalam untuk transportasi cerdas. Masalah yang diangkat adalah menemukan dan mengidentifikasi sekaligus beberapa objek dari video yang direkam sejumlah kamera, yang berbeda dari pelacakan satu kamera karena jangkauan pandang jaringan kamera lebih luas. Objek yang dilacak terutama kendaraan dan pejalan kaki pada adegan lalu lintas. Penulis menyebut sejumlah kesulitan yang menyertai tugas ini, yaitu latar yang membingungkan, perubahan postur, oklusi, perbedaan mutu video, pencahayaan, dan sudut pandang antarkamera, serta ketiadaan area yang tumpang tindih. Akibatnya, tampilan objek yang sama sangat berbeda antarpandang, disamping variabilitas intra-kelas yang besar dan kemiripan antarkelas.

Tulisan ini adalah tinjauan, bukan eksperimen baru dengan model tunggal. Penulis mengelompokkan literatur menjadi empat tahap. Pertama, detektor objek dibedakan menjadi detektor dua tahap yang menghasilkan calon wilayah lalu mengklasifikasikannya, seperti R-CNN, Fast R-CNN, dan Faster R-CNN, serta detektor satu tahap seperti YOLO, SSD, dan RetinaNet yang lebih cepat tetapi umumnya kurang tepat. Kedua, metode pelacakan satu kamera dibagi menjadi penguatan dengan ciri mendalam, penyematan dalam jaringan, dan pembelajaran akhir-ke-akhir. Ketiga, pengenalan ulang kendaraan dikelompokkan menjadi pembelajaran tanpa pengawasan, mekanisme perhatian, dan fitur lokal; pendekatan tanpa pengawasan memakai adaptasi domain, pengelompokan ciri, pembelajaran kontrastif, serta jaringan adversarial generatif, sedangkan mekanisme perhatian memakai perhatian spasio-temporal dan pendekatan fitur lokal memakai segmentasi wilayah serta titik kunci. Keempat, pelacakan lintas kamera menyambung lintasan yang sudah dibentuk tiap kamera menjadi satu identitas global.

Alur asosiasi yang dirangkum penulis dimulai dari deteksi kendaraan per bingkai, berlanjut ke pelacakan satu kamera yang menghasilkan lintasan kandidat berbasis posisi dan ciri yang dipelajari, lalu pengenalan ulang kendaraan, dan diakhiri pencocokan lintasan antarkamera. Mekanisme pencocokan memakai kemiripan spasio-temporal, antara lain model tautan kamera berbasis trajektori yang mengekstrak ciri tampilan dan topologi, pengelompokan hierarki, pengkodean visual dinamis pada ruang tumpang tindih, model keputusan Markov, filter Kalman untuk memprediksi gerak, serta perhatian spasio-temporal untuk membangun representasi trajektori. Penulis juga mencatat teknik penyambungan ulang trajektori yang terputus dan pembuangan trajektori yang tidak dapat diandalkan melalui pencocokan lintas pandang.

Data dan metrik yang dirangkum mencakup sejumlah tolok ukur. BDD100K memuat 100.000 video berdurasi sekitar 40 detik pada 30 bingkai per detik. VehicleX memuat 1.362 kendaraan dan 192.150 citra sintetis. UA-DETRAC memuat 10 jam video dari 24 lokasi, lebih dari 140.000 bingkai, 8.250 objek kendaraan, dan lebih dari 1,21 juta kotak dengan empat kondisi cuaca. KITTI, nuScenes dengan 1.000 skenario berkendara dan sekitar 15 jam data, CityFlow, serta VehicleID juga dibahas. Metrik yang dijelaskan meliputi TP, TN, FP, FN, akurasi, presisi, recall, MOTA, MOTP, MT, ML, Frag, IDP, IDR, IDF1, dan jumlah peralihan identitas. Perbandingan pada Tabel 3 memakai BDD100K dengan metrik IDP, IDR, dan IDF1. GCNM mencatat IDF1 81,06 dengan IDP 71,95 dan IDR 92,81; UWIPL 79,87; ANU 74,06; BUPT 70,22; DyGLIP 64,90; Online-MTMC 64,26; ELECTRICITY 53,80; dan NCCU 45,97. Angka-angka ini adalah hasil metode yang ditinjau, bukan hasil percobaan penulis tinjauan.

Batasan dan arah lanjutan dinyatakan secara eksplisit. Penulis menilai tinjauan sebelumnya menggolongkan metode secara terlalu kasar dan kurang memuat hasil tiga tahun terakhir, sehingga tinjauan ini difokuskan pada transportasi cerdas. Tantangan yang tersisa adalah pemrosesan waktu nyata karena deteksi pada urutan citra menambah waktu latih, deteksi semi-terawasi karena model terbimbing sensitif terhadap perubahan adegan dan memerlukan data berlabel, serta perlunya himpunan data publik yang mencakup beragam kondisi lingkungan. Arah yang diusulkan meliputi pelacakan aktif berbasis pembelajaran, fusi informasi banyak pandang yang masih terkendala kabur akibat gerak kamera, dan pelacakan objek tiga dimensi. Penulis menyatakan tidak ada konflik kepentingan.
