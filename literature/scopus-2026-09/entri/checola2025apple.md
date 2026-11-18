# Apple phenotyping using deep learning and 3D depth analysis: An experimental study on fruitlet sizing during early development

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `checola2025apple` |
| Judul asli | Apple phenotyping using deep learning and 3D depth analysis: An experimental study on fruitlet sizing during early development |
| Penulis | Checola, Giorgio; Moser, Damiano; Sonego, Paolo; Iob, Cristian; Micheli, Franco; Franceschi, Pietro |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [checola2025apple.pdf](../pdf/checola2025apple.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.100964

## Gambaran Umum

Penelitian ini mengatasi pengukuran ukuran buah apel muda (*fruitlet*) pada tahap perkembangan awal, yang diperlukan untuk pengelolaan penipisan buah dan pemodelan hasil. Penulis menyatakan bahwa pengumpulan data biometrik secara manual memakan waktu, padat karya, dan rawan salah, sehingga sulit dilakukan skala besar. Tujuan penelitian adalah membangun alur visi berbasis RGB-D yang menggabungkan YOLO dengan informasi kedalaman serta analisis statistik atas deretan frame, untuk mendeteksi dan mengelompokkan buah muda ke dalam karangan bunga (*flower corymb*) sekaligus menghasilkan jumlah dan estimasi diameter per video.

Tanaman yang dipakai adalah apel Fuji klon Aztec pada batang bawah M9 dengan sistem *tall spindle*. Penulis menandai 35 karangan bunga dan merekam video selama rata-rata 10 detik dari jarak sekitar 30 cm dari berbagai arah, pada resolusi 640 × 480 untuk RGB dan kedalaman serta 15 fps. Tujuh sesi pemantauan dilakukan antara 24 April dan 29 Mei, mencakup fase BBCH 72–74 hingga buah mencapai lebih dari 40 mm. Kamera yang dipakai adalah Intel RealSense D435i dengan penyaring spasial dan pengisian lubang. Data yang diperoleh berupa 234 berkas video format bag dan 1.054 pengukuran buah; dari sekitar 16.000 frame RGB, 481 citra dipilih secara acak berstrata dan diberi sekitar 4.000 anotasi berupa kotak sejajar sumbu dan kotak berorientasi, lalu dibagi 60% latih, 20% validasi, dan 20% uji. Pelatihan dijalankan pada instans AWS g5.2xlarge dengan GPU NVIDIA A10G 24 GB.

Mekanisme deteksi memakai YOLOv11l dengan ukuran citra 640, batch 32, dan delapan pekerja; model ini mengungguli YOLOv8 dan YOLOv10. Estimasi ukuran dilakukan dengan proyeksi kamera balik memakai parameter intrinsik, dengan nilai z berupa median kedalaman di dalam kotak pembatas setelah membuang kedalaman nol dan latar belakang dengan kedalaman sekurangnya 0,7 m. Diameter ditetapkan sebagai nilai terkecil dari dua dimensi kotak agar sesuai dengan pengukuran jangka sorong. Untuk mengisolasi karangan sasaran, penulis memakai pengelompokan hierarki dengan *complete linkage* dan ambang jarak 7,5 cm antarbuah. Pemilihan frame memakai selisih diskrit orde pertama dari jumlah deteksi untuk mencari frame dengan jumlah buah stabil dan tertinggi; hubungan antarframe dibangun dengan algoritma Hungarian berdasarkan selisih diameter absolut, lalu nilai median tiap kelompok dijadikan ukuran akhir. Deteksi anomali memakai *variational autoencoder* terhubung penuh dengan ruang latent berdimensi 5, rugi rekonstruksi *binary cross-entropy* dan divergensi Kullback–Leibler, serta ambang persentil ke-94 pada galat kuadrat rata-rata.

Hasil deteksi mencapai AP@0,5 sebesar 0,895 pada validasi dan 0,894 pada uji, dengan AP@[0,5:0,95] sekitar 0,77, presisi 0,881, dan recall 0,846; nilai turun menjadi 0,65 pada sesi pertama karena buah masih kecil dan menyerupai bunga. Dari 234 video, model tidak pernah mendeteksi jumlah buah yang benar pada 55 video (23,5%). Dengan penyaringan frame dan deteksi anomali, jumlah buah tepat diperoleh pada 56,4% video (132 dari 234), naik menjadi sekitar 75% setelah video yang tidak pernah terdeteksi benar dikeluarkan. Hasil akhir mencatat 918 benar positif, 136 negatif palsu, dan 12 positif palsu, dengan galat hitung rata-rata 0,63 buah per video. Estimasi diameter memiliki RMSE rata-rata 1,05 mm dan modus 0,72 mm, dengan nilai R² per jenis tunas 0,974; 0,863; dan 0,976; anotasi kotak berorientasi menghasilkan RMSE di bawah 0,3 mm. Tanpa deteksi anomali, video dengan padanan lengkap tinggal 125 dan RMSE naik menjadi 1,15 mm.

Batasan yang dinyatakan penulis meliputi generalisasi deteksi yang belum sempurna pada pencahayaan buruk serta buah kecil dan layu; data kedalaman yang hilang pada frame buram atau buah tertutup daun sehingga estimasi ukuran gagal meski deteksi benar; pengelompokan hierarki yang kadang membuang deteksi benar dan ambangnya ditentukan secara coba-coba; penggunaan dimensi kotak sebagai pengganti bentuk buah yang sebenarnya; serta sifat tanpa pengawasan dan keterbatasan data pada VAE yang menyulitkan penilaian keandalan penyaringan. Penulis juga mencatat peningkatan resolusi RGB dan kedalaman serta laju frame memberi manfaat, tetapi membatasi proses akuisisi, dan menyarankan desain kebun seperti sistem Guyot untuk mengurangi oklusi.

