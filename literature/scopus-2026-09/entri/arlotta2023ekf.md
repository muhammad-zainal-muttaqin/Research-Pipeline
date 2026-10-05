# An EKF-Based Multi-Object Tracking Framework for a Mobile Robot in a Precision Agriculture Scenario

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arlotta2023ekf` |
| Judul asli | An EKF-Based Multi-Object Tracking Framework for a Mobile Robot in a Precision Agriculture Scenario |
| Penulis | Arlotta, Andrea; Lippi, Martina; Gasparri, Andrea |
| Tahun | 2023 |
| Venue | Proceedings of the 11th European Conference on Mobile Robots Ecmr 2023 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [arlotta2023ekf.pdf](../pdf/arlotta2023ekf.pdf)
- DOI resmi: https://doi.org/10.1109/ecmr59166.2023.10256338

## Gambaran Umum
Makalah konferensi ini (*European Conference on Mobile Robots*, ECMR 2023) mengusulkan kerangka pelacakan multi-objek (*multi-object tracking*, MOT) untuk robot bergerak berkamera RGB-D pada skenario pertanian presisi, dengan objek sasaran berupa tandan anggur meja (*table grape*) dalam proyek H2020 CANOPIES. Setiap objek yang dilacak diberi satu *Extended Kalman Filter* (EKF) yang memperhitungkan gerak robot, sehingga posisi objek relatif terhadap robot tetap dapat diperbarui ketika pengukuran terputus akibat oklusi atau objek keluar dari bidang pandang.

Validasi dilakukan pada simulator berbasis Unity yang menirukan kebun anggur dengan sistem pergola dan pola tanam 3 m × 3 m, serta uji awal di laboratorium dengan pohon sintetis berisi tiga tandan anggur tiruan. Pada simulasi, galat rerata posisi (jarak antara posisi sebenarnya dan hasil EKF) berkisar 0,075 m pada ladang 3×3 sampai 0,208 m pada ladang 6×6, tanpa positif palsu. Pada laboratorium, galat rerata 0,043 m dan semua tandan terlacak tanpa positif palsu.

Makalah ini tidak memuat hitungan buah, pengukuran akurasi pencacahan, maupun data lapangan nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Banyak aplikasi robotik memerlukan lokalisasi beberapa objek, tetapi identifikasi sesaat (*instant-by-instant*) tidak andal pada lingkungan pertanian yang dinamis dan tidak terstruktur karena oklusi dan perubahan pencahayaan. Penulis menyatakan metode deteksi dan lokalisasi mutakhir umumnya bertumpu pada teknik penglihatan komputer dan tidak memodelkan kenyataan bahwa kamera terpasang pada robot yang bergerak, padahal gerak itu perlu diperhitungkan dalam pelacakan. Metode *tracking-by-regression* (CenterTrack, FairMOT) disebut memerlukan banyak data berlabel dan mahal secara komputasi.

Kerangka ini dimaksudkan sebagai langkah menuju robot bergerak berlengan manipulator untuk panen, yang harus tetap dapat menargetkan buah matang meskipun sementara terhalang daun atau buah lain atau berada di luar bidang pandang kamera.

## Ide Utama
Objek diasumsikan statis di lingkungan, sehingga gerak relatifnya terhadap robot hanya disebabkan oleh gerak robot. Keadaan setiap objek adalah posisi tiga dimensi $p_o = [p_x, p_y, p_z]^T$ pada kerangka robot. Tahap prediksi EKF memakai kecepatan linear dan sudut robot (dari enkoder) untuk memperbarui posisi relatif tiap objek pada setiap saat, sedangkan tahap koreksi dijalankan hanya ketika ada pengukuran yang terasosiasi. Dengan demikian, tandan yang sementara tidak terdeteksi tetap memiliki estimasi posisi.

## Cara Kerja Langkah demi Langkah
```
 [Enkoder + RGB-D] -> [Detektor + posisi relatif] -> [Asosiasi data] -> [EKF per objek]
```

### 1. Akuisisi data
Robot membawa kamera RGB-D dan enkoder yang menghasilkan masukan kendali (kecepatan linear dan sudut). Pada simulasi dipakai basis bergerak Alitrak DCT-300P dengan torso robot humanoid PAL Robotics dan kamera RGB-D; simulator menghasilkan posisi sebenarnya objek dan terintegrasi dengan ROS. Robot menavigasi kebun anggur melalui kisi titik jalan di tengah tiap sel antar-tanaman, sehingga seluruh ladang tercakup. Ukuran ladang yang diuji adalah 3×3 sampai 6×6 (baris × kolom). Pada laboratorium, dipakai robot Turtlebot 2 dengan sensor Realsense D435, pohon sintetis dengan tiga tandan anggur tiruan, dan sistem tangkap gerak Optitrack sebagai acuan; robot dikendalikan dengan joystick bergerak acak di sekitar pohon selama 80 detik.

### 2. Deteksi dan pengukuran relatif
Detektor dapat berupa detektor siap pakai apa pun; penulis memakai modul deteksi dan segmentasi gugus anggur yang dikembangkan dalam proyek CANOPIES. Detektor memberi kotak pembatas dan masker segmentasi. Masker dipakai untuk membuat peta kedalaman bertopeng; pengukuran posisi diambil pada piksel di tengah tepi atas kotak pembatas (agar dekat dengan tangkai tandan, titik potong yang diinginkan), dengan kedalaman dirata-ratakan dari piksel tak-nol di dalam masker. Titik dipetakan ke kerangka kamera dengan model kamera lubang jarum lalu ke kerangka robot dengan transformasi homogen tetap.

### 3. Asosiasi data
Dihitung matriks jarak Euklides antara tiap pengukuran dan tiap objek terlacak. Pengukuran ditugaskan ke objek dengan jarak terkecil bila jarak itu di bawah ambang $\tau = 0{,}35$ m; bila tidak, pengukuran menjadi kandidat objek baru. Bila beberapa pengukuran terasosiasi ke objek yang sama, hanya pasangan berjarak minimum yang dipertahankan.

### 4. EKF per objek
Untuk tiap objek baru, EKF diinisialisasi dengan keadaan sama dengan pengukuran. Prediksi berjalan setiap kali masukan kendali tersedia, dan koreksi berjalan setiap kali pengukuran baru tersedia. Dinamika prediksi diturunkan dari hubungan posisi objek di kerangka dunia statis dan kecepatan robot. Parameter: kovarians derau pengukuran $R = \mathrm{diag}\{0{,}5, 0{,}5, 0{,}5\}$, kovarians derau proses $Q = 10^{-4} I_3$, kovarians galat awal $P_0 = 0{,}05 I_3$.

## Eksperimen dan Hasil
Pada simulasi, galat dihitung sebagai jarak antara posisi sebenarnya (posisi tangkai tandan) dan posisi estimasi EKF, dikumpulkan pada setiap titik jalan. "Positif palsu" didefinisikan sebagai jumlah filter aktif untuk objek yang sama.

| Ukuran ladang | Jumlah filter | Galat rerata (m) | SD (m) | Min (m) | Maks (m) | Positif palsu |
|---|---|---|---|---|---|---|
| 3×3 | 15 | 0,075 | 0,010 | 0,043 | 0,359 | 0 |
| 4×4 | 33 | 0,076 | 0,027 | 0,011 | 0,378 | 0 |
| 5×5 | 51 | 0,169 | 0,067 | 0,017 | 0,506 | 0 |
| 6×6 | 81 | 0,208 | 0,075 | 0,020 | 0,583 | 0 |

Penulis menjelaskan bahwa galat rerata dan maksimum naik seiring ukuran ladang karena pada jalur yang direncanakan banyak tandan terakhir diukur lama sebelumnya sehingga hanya diperbarui oleh tahap prediksi dan mengalami penyimpangan (*drift*). Galat minimum selalu di atas 0,01 m karena posisi sebenarnya adalah tangkai tandan, sedangkan estimasi memakai tengah tepi atas kotak pembatas. Pada uji laboratorium, galat rerata 0,043 m (SD 0,03 m), maksimum 0,148 m, minimum 0,003 m, semua tandan terlacak tanpa positif palsu. Tidak ada pembanding metode lain, tidak ada metrik pencacahan (misalnya galat hitungan), dan tidak ada data buah nyata di kebun.

## Kelebihan dan Keterbatasan
Keterbatasan yang dinyatakan penulis: pendekatan pada dasarnya cocok untuk pelacakan multi-objek lokal di sekitar robot, bukan untuk seluruh ladang (simulasi cakupan penuh hanya untuk menunjukkan hasil); validasi pada robot nyata masih awal dan perlu dilanjutkan pada pengaturan nyata; asumsi objek statis berasal dari kebutuhan proyek CANOPIES.

Menurut pembacaan ringkasan ini, kelemahan lain adalah: (1) uji nyata hanya laboratorium dengan tiga tandan tiruan, sehingga ketahanan terhadap oklusi dan detektor sesungguhnya belum teruji; (2) tidak ada pembanding (misalnya SORT atau DeepSORT) dan tidak ada metrik identitas MOT; (3) asosiasi hanya berdasarkan jarak Euklides pada kerangka robot dengan ambang tetap 0,35 m, tanpa kemiripan tampilan; (4) pelacakan bergantung pada odometri enkoder, sehingga galat odometri akan terakumulasi pada objek yang lama tidak terlihat; (5) nilai positif palsu nol pada simulasi tidak menunjukkan kinerja pada pemandangan padat dengan buah berdekatan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat berulang kali dengan mempertahankan satu filter per objek di kerangka robot dan mengasosiasikan pengukuran baru ke filter yang ada berdasarkan jarak Euklides (ambang 0,35 m). Mekanismenya adalah pelacakan berbasis geometri 3D dengan prediksi dari odometri, bukan kemiripan tampilan. Hitungan buah tidak dilaporkan, apalagi per kelas; yang dievaluasi hanyalah galat posisi dan jumlah filter ganda untuk satu objek (positif palsu). Acuannya adalah posisi objek dari simulator (simulasi) dan tangkap gerak Optitrack (laboratorium), bukan panen atau hitungan manual.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan mempertahankan keadaan posisi 3D per tandan dengan gerak kamera yang diketahui, sehingga pengamatan baru dapat dicocokkan secara geometris. Syaratnya adalah odometri atau pose kamera yang andal serta kedalaman; keduanya tidak tersedia pada citra sisi pohon yang diambil tanpa pose terukur. Atribut kelas tidak dipakai dalam asosiasi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `arlotta2023ekf`.

Arlotta dkk. mengusulkan kerangka pelacakan multi-objek berbasis satu EKF per objek untuk robot bergerak berkamera RGB-D, yang memakai odometri robot pada tahap prediksi dan asosiasi data berbasis jarak Euklides (ambang 0,35 m) untuk melacak tandan anggur meja secara relatif terhadap robot. Pada simulasi Unity, galat rerata posisi 0,075 sampai 0,208 m menurut ukuran ladang (3×3 sampai 6×6) tanpa positif palsu, dan pada uji laboratorium dengan tiga tandan tiruan galat rerata 0,043 m.

Catatan verifikasi data: Angka simulasi ada pada Tabel I (seksi IV-C); angka laboratorium (0,043 m, SD 0,03 m, maks 0,148 m, min 0,003 m, durasi 80 detik) pada seksi IV-D; parameter EKF dan ambang asosiasi pada seksi IV-B. Jumlah tandan di simulasi dibaca dari kolom "# Obj." Tabel I (jumlah filter yang diinisialisasi). Jumlah citra, hasil detektor, dan hitungan terhadap acuan tidak dilaporkan. Teks ekstraksi baik; terdapat catatan pengunduhan IEEE pada tiap halaman yang tidak memengaruhi isi.
