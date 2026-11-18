# Multiple object tracking: A literature review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2021multiple` |
| Judul asli | Multiple object tracking: A literature review |
| Penulis | Luo, Wenhan; Xing, Junliang; Milan, Anton; Zhang, Xiaoqin; Liu, Wei; Kim, Tae-Kyun |
| Tahun | 2021 |
| Venue | Artificial Intelligence |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [luo2021multiple.pdf](../pdf/luo2021multiple.pdf)
- DOI resmi: https://doi.org/10.1016/j.artint.2020.103448

## Gambaran Umum

Masalah utama adalah pelacakan multi-objek (*multiple object tracking*, MOT), yaitu menemukan sejumlah objek dalam video, menjaga identitasnya, dan menghasilkan lintasan masing-masing. Tugas ini sulit karena perubahan penampilan yang mendadak dan oklusi parah, serta karena jumlah objek berubah dari waktu ke waktu dan identitas harus tetap terjaga. Penelitian ini adalah tinjauan pustaka komprehensif pertama tentang MOT. Fokus tinjauan adalah pejalan kaki karena objek ini bersifat tidak kaku, memiliki banyak aplikasi praktis, dan menjadi subjek sekitar 70% penelitian MOT yang dikumpulkan. Objek lain yang disebut mencakup kendaraan, pemain olahraga, kawanan hewan, sel, dan bagian-bagian suatu objek. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Tinjauan ini tidak memakai data eksperimen baru, melainkan menyusun rumusan masalah dan mengumpulkan hasil publikasi. Rumusan umum MOT dinyatakan sebagai estimasi *maximum a posteriori*, yaitu mencari keadaan seluruh objek yang memaksimalkan probabilitas keadaan tersebut diberikan seluruh pengamatan. Metode dikelompokkan berdasarkan cara inisialisasi — *detection-based tracking* (DBT) yang mendeteksi objek otomatis lalu merangkainya menjadi lintasan, dan *detection-free tracking* (DFT) yang memulai dari objek yang ditentukan manual — serta berdasarkan cara pemrosesan (daring atau luring) dan jenis keluaran (stokastik atau deterministik). Komponen utama sistem MOT yang ditinjau adalah model penampilan, model gerak, model interaksi, model eksklusi, penanganan oklusi, dan metode inferensi.

Mekanisme deteksi dan asosiasi dijelaskan melalui dua pertanyaan: bagaimana mengukur kesamaan antarobjek dalam frame dan bagaimana memulihkan identitas lintas frame. Model penampilan memakai representasi fitur lokal (KLT, aliran optik), fitur regional (histogram warna dan templat piksel sebagai orde nol, HOG sebagai orde satu, matriks kovarians regional sebagai orde dua), serta fitur lain seperti kedalaman, gait, dan fiturCNN. Kemiripan dihitung dengan ukuran tunggal — korelasi silang ternormalisasi, jarak Bhattacharyya yang diubah menjadi skor kemiripan, atau kemiripan kosinus — maupun dengan penggabungan beberapa petunjuk lewat strategi *boosting*, konkatenasi, penjumlahan, perkalian, dan kaskade. Model gerak memakai asumsi kecepatan konstan dengan kehalusan kecepatan, posisi, atau akselerasi. Inferensi data asosiasi dilakukan secara probabilistik dengan filter Kalman, filter Kalman yang diperluas (*extended Kalman filter*), dan filter partikel, atau secara deterministik dengan pencocokan graf bipartit memakai algoritma Hungaria, pemrograman dinamis dan linear, jaringan aliran biaya minimum, *conditional random field*, dan *maximum-weight independent set*.

Evaluasi menggunakan metrik deteksi — Recall, Precision, *false alarms per frame* (FAF/FPPI), MODA, dan MODP — serta metrik pelacakan — ID switches, MOTA, MOTP, *tracking distance error*, OSPA, MT, ML, PT, FM, RS, dan RL. MOTA menggabungkan negatif palsu, positif palsu, dan laju ketidaksesuaian; MOTP adalah rata-rata tumpang tindih atas pencocokan yang benar; keduanya mengikuti metrik CLEAR MOT. Dataset publik yang dirangkum mencakup MOT16 (14 video, 11.000 frame), KITTI (50 video), PETS2009, CAVIAR, Caltech Pedestrian (137 video, 250.000 frame), ETH Pedestrian, Town Centre, dan lain-lain. Karena keterbatasan ruang, hanya hasil pada sekuens PETS2009-S2L1 yang ditampilkan; metode luring mencapai rata-rata MOTA 0,935, MOTP 0,775, MT 0,95, IDS 5,9, dan FM 8,3, sedangkan metode daring mencapai MOTA 0,913, MOTP 0,748, MT 1,00, IDS 7,0, dan FM 10,3. Penulis mencatat perbandingan langsung antarmetode tidak sepenuhnya adil karena perbedaan metode, hipotesis deteksi, sudut pandang, dan informasi awal yang dipakai.

Batasan yang dinyatakan penulis mencakup ketergantungan kinerja MOT pada detektor objek — hipotesis deteksi yang berbeda pada metode yang sama menghasilkan kinerja yang sangat berbeda, dan beberapa publikasi tidak menjelaskan modul deteksinya — serta banyaknya parameter yang menyulitkan penyetelan dan reproduksi hasil. Metode juga sering tidak dapat digeneralisasi ke video lain karena perbedaan sudut kamera, keadaan kamera statis atau bergerak, dan detektor yang dilatih pada video tertentu. Dataset dianggap lebih kecil daripada dataset pelacakan objek tunggal dan masih terpusat pada pejalan kaki, sedangkan kode sumber yang tersedia masih sedikit. Arah penelitian yang diusulkan meliputi adaptasi detektor untuk video tertentu, MOT multisangkap kamera dan 3D, MOT dengan pemahaman adegan, MOT berbasis pembelajaran mendalam, serta penggabungan dengan segmentasi, identifikasi ulang, estimasi pose, dan pengenalan aksi.

