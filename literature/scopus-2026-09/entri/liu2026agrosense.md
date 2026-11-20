# Agrosense v2: An AI-enabled system for precision orchard sensing and tree-level monitoring

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026agrosense` |
| Judul asli | Agrosense v2: An AI-enabled system for precision orchard sensing and tree-level monitoring |
| Penulis | Liu, Shiyu; Ampatzidis, Yiannis; Guan, Hengyue; Liu, Wenhao; Zhou, Congliang; Choi, Daeun; Lee, Won Suk |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [liu2026agrosense.pdf](../pdf/liu2026agrosense.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111797

## Gambaran Umum

Studi ini membahas penghitungan pohon dan buah jeruk dari urutan citra yang direkam di kebun. Penghitungan buah secara manual sulit diskalakan ke seluruh kebun, sedangkan penghitungan dari satu citra tidak mencakup seluruh pohon. Penulis mengusulkan alur kerja yang menghitung pohon di tingkat individu dari urutan citra, lalu menghitung buah yang terdeteksi pada setiap pohon, dan juga mengklasifikasikan kepadatan tajuk. Pertanyaan utamanya adalah apakah pohon dan buah dapat dihitung dengan akurasi memadai dari rekaman lapangan tanpa acuan penghitungan manual untuk setiap pohon.

Data dikumpulkan dari tiga lokasi: SWFREC, Field A, dan Field B. Penulis menggunakan pengukuran *RTK-GNSS* (sistem penentuan posisi satelit dengan koreksi real-time) dan *IMU* BNO055 (unit pengukur gerak dan orientasi) untuk georeferensi, sehingga setiap pengamatan dapat dikaitkan dengan posisi di kebun. Untuk deteksi buah, citra beresolusi 1920×1200 dibagi menjadi 1.132 citra latih, 142 citra validasi, dan 141 citra uji. Untuk deteksi batang, 2.145 citra latih dan validasi dipakai, dengan 3.413 sampel pohon untuk uji. Untuk klasifikasi kepadatan tajuk, tersedia 3.634 sampel prapelatihan, 26.435 sampel penyetelan, dan 3.396 sampel pohon untuk uji. Teks tidak menyebut spesies, varietas, atau umur tanaman secara rinci di luar identitas kebun jeruk tersebut.

Metode terdiri atas beberapa tahap. Deteksi batang memakai *YOLOv11-Nano* (model deteksi objek ringan) dengan masukan 640×640 piksel. Model dilatih pada MPS di MacBook Pro M3 Pro dan dijalankan di Jetson AGX Orin dengan batch 1 pada 15 FPS. Kotak batang disaring dengan tiga aturan: posisi pusat vertikal di bawah 0,3, luas minimal 0,005, dan rasio piksel tidak hitam pada area tajuk. Ambang tersebut bersifat heuristik. Pelacakan batang secara temporal menjaga identitas pohon antarbingkai. Akurasi penghitungan pohon tercatat 95,96% (SWFREC), 92,73% (Field A), dan 97,79% (Field B). Klasifikasi kepadatan tajuk mencapai 94,1% sampai 96,8%. Untuk buah, penulis membandingkan YOLOv11 (varian n, s, m, l) dan *RT-DETR* (detektor berbasis transformer), dengan metrik mAP@0,5 dan mAP@0,5:0,95 pada buah di pohon dan buah di tanah. RT-DETR memberi mAP@0,5 tertinggi, yaitu 0,837 untuk buah di pohon dan 0,722 untuk buah di tanah.

Penulis menyebut beberapa keterbatasan. Oklusi, rumput tinggi, dan tajuk yang saling menyatu menurunkan kualitas deteksi. Pelacakan batang juga dapat gagal, dan hasilnya memengaruhi identitas pohon. Penulis tidak melakukan validasi penghitungan buah manual untuk seluruh pohon, sehingga hitungan berbasis deteksi hanya dinyatakan layak untuk perbandingan relatif dan pemetaan. Deteksi buah di tanah peka terhadap bayangan dan latar yang ramai. Penulis menyebut pekerjaan lanjutan berupa penggunaan multi-pandang, LiDAR, dan radar. Bagi tinjauan ini, studi tersebut mengelompokkan hitungan per pohon dalam satu pandang lintasan dan tidak membahas deduplikasi buah lintas pandang.
