# An Object-Tracking Technique for Counting Grape Clusters in Brazilian Northeast's Pergola Vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sasse2025object` |
| Judul asli | An Object-Tracking Technique for Counting Grape Clusters in Brazilian Northeast's Pergola Vineyards |
| Penulis | Sasse, Arthur M.; Wieland, Jo\~ao Pedro V. B.; Pereira, Adriano G.; Proen\cca, Lincoln R.; Freitas, Ian M. P.; Rangel, Pablo; de Farias, Claudio M. |
| Tahun | 2025 |
| Venue | Proceedings of the 2025 28th International Conference on Information Fusion Fusion 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [sasse2025object.pdf](../pdf/sasse2025object.pdf)
- DOI resmi: https://doi.org/10.23919/fusion65864.2025.11124157

## Gambaran Umum
Makalah prosiding ini mengusulkan teknik ringan untuk menghitung tandan anggur dari video ponsel yang direkam tangan di kebun anggur dengan sistem pergola (*pergola*, kanopi berbentuk terowongan) di Timur Laut Brasil. Teknik ini menggabungkan detektor YOLOv8 (varian YOLOv8s) dengan pelacak ByteTrack, dan jumlah tandan dihitung dari banyaknya ID unik atau dari garis penghitung.

Data berasal dari satu kebun anggur meja di Lembah São Francisco, Brasil: 445 bingkai beranotasi dari empat video yang direkam dengan kamera 26 mm iPhone XR, diperluas dengan augmentasi menjadi 1.069 bingkai. Evaluasi hitungan memakai video berdurasi 5 detik dengan 74 tandan.

Hasil: deteksi mencapai mAP@50 75,1%, F1 69,9%, presisi 71%, dan *recall* 68,9%. Penghitungan dengan ID unik menghasilkan galat absolut 20 tandan (27% di atas nilai sebenarnya), sedangkan garis penghitung menghasilkan galat 53 tandan (71,62% di bawah nilai sebenarnya). Penulis menyebutnya sebagai baseline pertama untuk kebun pergola.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan tandan penting untuk estimasi hasil dan perencanaan panen, tetapi hitung manual memerlukan banyak tenaga dan rawan galat. Di kebun yang diteliti, pekerja berjalan di sepanjang barisan dan mencatat jumlah tandan. Metode yang ada, menurut penulis, menghitung butir (bukan tandan), hanya untuk citra statis, memerlukan peralatan khusus, atau belum diuji pada sistem pergola. Pada pergola, tandan tersebar pada kedalaman berbeda di dalam kanopi terowongan, sehingga ukuran tampak dan oklusi sangat bervariasi, berbeda dari kebun berbaris tempat tandan membentuk "dinding" pada jarak seragam dari kamera. Citra pesawat nirawak tidak berguna karena dedaunan padat di bagian atas pergola.

## Ide Utama
Penulis memilih deteksi objek dengan pelacakan 2D (*tracking-by-detection*) karena bekerja pada video, lebih murah secara komputasi daripada pemetaan 3D, dan hanya memerlukan video RGB. Setiap tandan dianggap membentuk lintasan ketika kamera bergerak masuk ke dalam kebun, sehingga ID unik pelacak dapat dipakai sebagai hitungan. Prosedur perekaman meniru cara pekerja berjalan di barisan agar mudah diterapkan sebagai aplikasi ponsel.

## Cara Kerja Langkah demi Langkah

```
 video ponsel -> YOLOv8s (deteksi tandan) -> ByteTrack (ID per tandan)
   -> hitungan = jumlah ID unik   atau   garis penghitung (heatmap)
```

### 1. Akuisisi data
Empat video direkam di kebun yang diteliti, tiga pada sore hari dan satu pada pagi hari, oleh satu anggota tim dengan kamera 26 mm iPhone XR. Sebanyak 445 bingkai dianotasi di Roboflow. Augmentasi (rotasi, pembalikan horizontal, penyesuaian kecerahan dan kontras, sedikit perubahan saturasi) menghasilkan 1.069 bingkai, dibagi 88% latih, 8% validasi, 4% uji. Citra 1080p (rasio 16:9) diubah ukurannya menjadi 640×640 piksel. Kultivar tidak dilaporkan.

### 2. Deteksi
YOLOv8s, dipralatih pada MS-COCO, dilatih 25 epoch dengan *hyperparameter* bawaan; dipilih agar dapat berjalan pada perangkat tepi berdaya rendah. Percobaan lain (YOLOv8s 75 epoch, YOLOv5s 200 epoch dengan bobot dari studi lain, YOLOv12n 200 epoch) memberi hasil sedikit lebih buruk.

### 3. Pelacakan
ByteTrack (filter Kalman dan algoritma Hungaria) dengan pengaturan bawaan. Deteksi berkeyakinan tinggi dicocokkan lebih dahulu, lalu deteksi berkeyakinan rendah ditautkan ke lintasan yang belum berpasangan. Implementasi memakai pustaka Ultralytics dan Roboflow Supervision.

### 4. Pencacahan
Dua cara: (a) jumlah ID unik pada lintasan, dan (b) garis penghitung yang posisinya ditentukan sewenang-wenang berdasarkan peta panas deteksi pada citra latih; tandan dihitung ketika kotaknya melintasi garis.

## Eksperimen dan Hasil
Pertanyaan penelitian: RQ1 deteksi pada citra statis (mAP@50, F1, presisi, *recall*), RQ2 pencacahan pada video (*mean absolute error*, MAE). Deteksi dievaluasi pada 88 citra validasi; pencacahan pada video 5 detik dari rekaman terpisah yang tidak dipakai melatih, dengan acuan hitungan dari anotasi video di CVAT. Eksperimen dijalankan sekali pada GPU NVIDIA GeForce RTX 4060.

| Metrik deteksi | Nilai |
|---|---|
| Presisi | 71% |
| Recall | 68,9% |
| F1 | 69,9% |
| mAP@50 | 75,1% |

| Cara menghitung | Acuan | MAE | Arah galat |
|---|---|---|---|
| ID unik | 74 tandan | 20 | 27% di atas |
| Garis penghitung | 74 tandan | 53 | 71,62% di bawah |

Penulis menyatakan perbandingan langsung dengan studi lain tidak mungkin karena sistem kebun dan sudut pandang berbeda. Garis penghitung memberikan penghitungan yang jauh terlalu rendah karena banyak tandan tidak pernah melintasi garis akibat perspektif kebun. Penghitungan dengan ID unik cenderung berlebih sehingga penulis menyebut perlunya mekanisme fusi; menurut hipotesis penulis, beberapa garis penghitung yang digabung dapat lebih akurat.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: hanya memerlukan video RGB dari ponsel, ringan (YOLOv8s), implementasi dirilis publik, dan sesuai dengan cara kerja hitung manual yang sudah ada.

Keterbatasan yang dinyatakan penulis: data terbatas (percobaan lain menunjukkan konvergensi dini yang menyiratkan perlunya data lebih banyak); eksperimen dijalankan sekali tanpa pengulangan sehingga signifikansi statistik tidak diuji; hanya satu video uji; posisi garis penghitung belum dioptimalkan; gerak kamera tidak seragam di medan tidak rata dapat memicu kesalahan asosiasi; fusi sensor, stereo, atau RGB-D disebut sebagai arah lanjutan.

Menurut pembacaan ringkasan ini: evaluasi pencacahan hanya pada 5 detik video dengan 74 tandan sehingga galat 27% tidak dapat digeneralisasi; ID unik dari pelacak 2D bergantung pada keberlanjutan lintasan dan tidak ada mekanisme untuk mengenali kembali tandan yang hilang lalu muncul; bingkai latih dan uji dapat berasal dari video yang sama dalam pembagian citra beraugmentasi (asal pembagian tidak diuraikan dalam teks); pembanding (mis. pelacak lain atau hitungan manual lapangan) tidak ada.

## Kaitan dengan Tinjauan main6
Makalah menangani tandan yang terlihat pada banyak bingkai video dengan mekanisme pelacakan multi-objek 2D (ByteTrack) dan hitungan dari ID unik atau garis penghitung. Tidak ada pencocokan lintas sisi atau pandang yang terpisah; hanya satu video yang bergerak masuk di koridor. Hitungan tidak dilaporkan per kelas (satu kelas, tandan anggur). Acuan hitungan adalah anotasi video dengan CVAT, bukan panen atau hitung lapangan.

Yang dapat dipindahkan: contoh hasil tentang risiko kedua mekanisme pencacahan, yaitu ID unik yang menghitung berlebih (27% di atas) dan garis penghitung yang menghitung terlalu sedikit (71,62% di bawah) ketika perspektif membuat objek tidak melintasi garis. Temuan ini relevan sebagai peringatan bagi pencacahan tandan sawit dari video yang mengelilingi pohon, tetapi tidak menyediakan mekanisme identitas lintas sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `sasse2025object`.

Sasse dkk. mengusulkan teknik penghitungan tandan anggur pada kebun pergola dari video ponsel tangan dengan YOLOv8s dan ByteTrack. Dilatih pada 1.069 bingkai (445 asli) dari satu kebun di Timur Laut Brasil, detektor mencapai mAP@50 75,1% dan F1 69,9%; pada video uji 5 detik berisi 74 tandan, penghitungan ID unik menghasilkan galat 20 tandan (27% di atas acuan), sedangkan garis penghitung 53 tandan di bawah acuan (71,62%).

Catatan verifikasi data: Metrik deteksi dan hasil pencacahan ada pada Seksi V; rincian dataset pada Seksi IV-A; pengaturan pelatihan pada Seksi IV-C. Hitungan absolut hasil pelacakan (di luar MAE) tidak dilaporkan. Tidak dapat diverifikasi dari teks: kultivar, cara pembagian latih, validasi, dan uji pada bingkai beraugmentasi, serta hasil percobaan model lain (hanya disebut lebih buruk). Teks ekstraksi terbaca baik.
