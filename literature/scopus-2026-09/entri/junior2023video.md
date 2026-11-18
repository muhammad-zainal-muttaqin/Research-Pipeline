# Video based oil palm ripeness detection model using deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `junior2023video` |
| Judul asli | Video based oil palm ripeness detection model using deep learning |
| Penulis | Junior, Franz Adeta; Suharjito |
| Tahun | 2023 |
| Venue | Heliyon |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [junior2023video.pdf](../pdf/junior2023video.pdf)
- DOI resmi: https://doi.org/10.1016/j.heliyon.2023.e13036

## Gambaran Umum

Penelitian ini menangani penentuan tingkat kematangan tandan buah segar kelapa sawit yang selama ini dilakukan secara manual. Penilaian manusia dianggap subjektif, tidak konsisten, mahal, dan lambat. Penulis mencatat bahwa kajian sebelumnya umumnya memakai citra diam tidak berurutan dan sistem klasifikasi tanpa lokalisasi objek, sehingga belum menguji deteksi pada data video yang menyerupai kondisi pengoperasian waktu nyata. Tujuan penelitian adalah membangun model deteksi objek yang dilatih dan diuji memakai video untuk mengenali enam tingkat kematangan sekaligus membandingkan kecepatan dan akurasinya dengan metode lain.

Data berupa video yang direkam di lokasi pengumpulan tandan di Kalimantan Tengah memakai telepon genggam, dalam kondisi luar ruang dengan posisi dan pencahayaan beragam. Saat perekaman, tandan diputar 360° agar seluruh permukaan terlihat. Enam kategori yang dipakai adalah ripe, over_ripe, under_ripe, unripe, empty, dan abnormal. Video disimpan dalam format MP4 beresolusi 1280×720 dengan 30 frame per detik. Penulis menggunakan 47 video latih dan 10 video uji di luar data latih, dengan rasio latih–validasi 7:3. Ekstraksi frame memakai VLC dengan rasio 30, yaitu satu frame per detik, menghasilkan 929 frame dari 49 video. Augmentasi menghasilkan 4.645 citra, terdiri atas citra asli, kecerahan acak, Gaussian blur, rotasi 45° dan 90°, serta translasi. Data uji terdiri atas enam video satu kelas (satu video per kelas) dengan 3.238 anotasi ground truth dan empat video campuran dua kelas dengan 1.288 anotasi.

Model yang dibandingkan adalah tiga varian YOLOv4, yaitu YOLOv4-CSPDarknet53 (161 lapisan), YOLOv4-Tiny (37 lapisan, dua skala deteksi), dan YOLOv4-Tiny 3L (44 lapisan, tiga skala deteksi 52×52, 26×26, dan 13×13), serta SSD-MobileNetV2 FPN dan EfficientDet-D0 sebagai pembanding YOLOv4 memakai DarkNet di Google Colaboratory dengan GPU Nvidia Tesla P100 dan RAM 54,8 GB, masukan 416×416, bobot awal pralatih MS COCO, 12.000 iterasi maksimum, dan optimizer dengan penurunan learning rate pada iterasi ke-9600 dan ke-10800. Fungsi rugi kotak pembatas memakai Complete IoU. Pengembangan model melalui empat tahap: percobaan augmentasi, penyesuaian hyperparameter laju pembelajaran dan ukuran batch, percobaan pembekuan lapisan, serta kombinasi konfigurasi terbaik. Metrik evaluasi adalah mAP50, F1-score, dan IoU; mAP dihitung sebagai rata-rata AP atas N kelas, sedangkan presisi dan recall dihitung dari true positive, false positive, dan false negative.

Pada data video satu kelas, YOLOv4-Tiny 3L (Model_16) memperoleh mAP50 90,56%, IoU 58,35%, F1 0,79, waktu deteksi 5 detik, dan 104,95 FPS; YOLOv4-Tiny (Model_12) memperoleh 83,57%, 56,90%, 0,78, 4 detik, dan 105,03 FPS; YOLOv4-CSPDarknet53 (Model_5) memperoleh 97,64%, 73,36%, 0,93, 19 detik, dan 41,5 FPS. Pada video campuran dua kelas, masing-masing memperoleh mAP50 70,21%, 59,17%, dan 48,54%. Penulis menyimpulkan YOLOv4-Tiny 3L paling sesuai untuk deteksi waktu nyata karena mAP tinggi dengan beban komputasi lebih ringan. Percobaan augmentasi menunjukkan augmentasi geometri memberi IoU validasi 84,14% dan IoU uji 67,73%, sedangkan kombinasi augmentasi memberi mAP50 uji 94,98%. Pembekuan 23 lapisan menaikkan mAP50 uji menjadi 98,53% pada video satu kelas. Ringkasan menyebut mAP50 72,15% untuk video multikelas pada konfigurasi laju pembelajaran 0,001 dan batch 64, nilai yang berbeda dari Tabel 8.

Penulis menyatakan beberapa batasan. Seluruh model gagal mendeteksi lebih dari satu kelas dengan baik dalam satu frame karena data latih memuat hanya satu kelas per citra. Model dengan lapisan terlalu dalam tidak cocok untuk himpunan data berukuran 4.645 citra. Pembekuan lapisan tidak meningkatkan kinerja secara bermakna dan hanya memperbaiki lokalisasi objek. Beberapa konfigurasi masih berhenti di minimum lokal karena jumlah langkah pelatihan kurang, sehingga hasilnya belum maksimal. Penulis juga menyebut pengumpulan video memakan waktu lebih lama dibanding citra diam karena cuaca dan keterbatasan waktu pencahayaan ideal. Penelitian ini menitikberatkan penilaian kematangan di fasilitas pengolahan, bukan penghitungan jumlah tandan; penulis mengusulkan penghitungan otomatis per kelas sebagai pengembangan berikutnya.

