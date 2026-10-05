# Drone-Computer Communication Based Tomato Generative Organ Counting Model Using YOLO V5 and Deep-Sort

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `egi2022drone` |
| Judul asli | Drone-Computer Communication Based Tomato Generative Organ Counting Model Using YOLO V5 and Deep-Sort |
| Penulis | Egi, Yunus; Hajyzadeh, Mortaza; Eyceyurt, Engin |
| Tahun | 2022 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [egi2022drone.pdf](../pdf/egi2022drone.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture12091290

## Gambaran Umum
Makalah ini mengusulkan sistem pencacahan organ generatif tomat (bunga, tomat hijau, dan tomat merah) di rumah kaca. Video direkam dengan drone DJI Spark dan dikirim ke laptop. Detektor YOLO V5 dipasangkan dengan pelacak Deep-SORT (*Simple Online and Realtime Tracking with a deep association metric*), lalu hitungan dihasilkan dari lintasan objek yang melewati dua garis hitung pada bingkai video. Objek yang diteliti adalah tomat (*Solanum lycopersicum* L.) di rumah kaca Universitas Şırnak, Turki.

Data latih berasal dari 1.097 citra RGB mentah yang diambil dengan drone. Setelah augmentasi rotasi 90 derajat searah dan berlawanan arah jarum jam, jumlahnya menjadi 2.329 citra dengan 6.957 anotasi untuk tiga kelas: bunga, tomat hijau, dan tomat merah. Data dibagi menjadi latih, validasi, dan uji dengan rasio 70%, 20%, dan 10%.

Hasil deteksi pada Tabel 2 adalah mAP@0.5 seluruh kelas 0,630 dan mAP@0.95 0,321, dengan mAP@0.5 per kelas 0,796 (tomat merah), 0,549 (tomat hijau), dan 0,508 (bunga). Pada satu lorong rumah kaca, hitungan sistem dibandingkan dengan hitungan manual. Akurasi yang dilaporkan adalah 99% untuk tomat hijau, 85% untuk tomat merah, dan 50% untuk bunga.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkembangan organ generatif tomat berkaitan dengan estimasi hasil panen. Penulis menyatakan bahwa pencacahan manual memakan waktu, mahal, tidak akurat di lingkungan yang menantang, dan terkendala oleh daun, cabang yang menghalangi, serta hitungan ganda. Metode visi komputer klasik berbasis ambang warna, ukuran, dan bentuk dinilai kurang mampu menghadapi variabilitas lingkungan rumah kaca.

Penulis juga menyatakan bahwa hitungan ganda antara bunga dan buah dapat menunjukkan masalah penyerbukan, sedangkan hitungan tomat merah membantu memperkirakan biaya pengemasan dan pengangkutan sebelum panen. Karena itu, sistem perlu menghitung ketiga kelas sekaligus dan menghindari penghitungan objek dari lorong lain.

## Ide Utama
Gagasan utamanya adalah menyatukan deteksi per bingkai (YOLO V5) dengan pelacakan antarbingkai (Deep-SORT) pada video drone, sehingga satu tomat atau bunga yang tampak pada banyak bingkai dihitung satu kali ketika lintasannya melewati garis hitung. Penapis ukuran (*size filter*) berdasarkan tinggi dan lebar kotak ditambahkan agar objek yang jauh, yaitu objek di lorong lain, tidak ikut dihitung. Jarak drone ke lorong tomat ditetapkan 25 cm pada Algoritma 2.

Identitas objek di sini dipertahankan antarbingkai pada satu lintasan video dari satu sisi lorong. Makalah tidak membahas penyatuan identitas antarpandang yang terpisah.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Bibit tomat dibeli di pasar terbuka dan ditanam dengan jarak 25 cm dalam baris serta 125 cm antarbaris. Video RGB direkam dengan drone DJI Spark berkamera 12 MP pada siang hari di rumah kaca Universitas Şırnak. Perekaman dilakukan pada dua tanggal, 10 Juni 2021 dan 20 Juni 2021, keduanya cerah, dengan resolusi 1080p dan 30 fps (Tabel 1). Lorong rumah kaca lurus dengan jarak antarlorong 80 cm. Drone mengirim bingkai video ke laptop HP Omen dengan GPU GeForce 1050Ti melalui *Real-Time Messaging Protocol* (RTMP).

Video diubah menjadi citra dengan OpenCV, yaitu satu citra setiap 15 bingkai (jeda setengah detik). Citra tanpa buah tomat dibuang sehingga tersisa citra beresolusi 1920 x 1080. Makalah menyebut angka 2.329 pada bagian ini, sedangkan bagian Hasil menyebut 1.097 citra mentah yang menjadi 2.329 citra setelah augmentasi. Kedua keterangan ini tidak sepenuhnya selaras, sehingga urutan pembentukan kumpulan data tidak dapat dipastikan dari teks.

### 2. Pelabelan dan augmentasi
Augmentasi tingkat spasial dan tingkat piksel digunakan. Citra diubah ukurannya menjadi 608 x 608, 512 x 512, dan 416 x 416 dengan menjaga rasio aspek dan menambahkan bingkai hitam. Kumpulan data meningkat dari 1.097 menjadi 2.329 citra dan 6.957 anotasi. Pelabelan memakai tiga kelas: 0 bunga, 1 tomat hijau, 2 tomat merah. Pembagian data 70%, 20%, dan 10% dilakukan atas 2.329 citra hasil augmentasi. Makalah tidak menyebut apakah citra hasil augmentasi dari citra yang sama dijaga agar tidak tersebar ke himpunan yang berbeda.

### 3. Detektor YOLO V5
Arsitektur terdiri atas *backbone* CSPDarknet, *neck* PANet, dan kepala YOLO. Ukuran masukan 416 piksel dan ambang IOU 0,1 sampai 0,7. Parameter latih yang dinyatakan adalah 200 epoch, ukuran *batch* 16, dan laju belajar 0,001, dijalankan di Google Colab dengan PyTorch.

### 4. Pelacakan Deep-SORT
Deep-SORT memakai gabungan filter Kalman dan algoritma Hungarian. Fitur tampilan diambil dari jaringan residual lebar (dua lapis konvolusi dan enam blok residual lebar) yang menghasilkan vektor fitur berdimensi 128 yang dinormalisasi $\ell_2$. Jarak kosinus minimum antara lintasan dan deteksi serta jarak Mahalanobis dipakai pada pencocokan bertingkat (*cascade matching*). Makalah juga menguraikan pelacak IOU (Algoritma 1) sebagai latar, tetapi sistem akhir memakai Deep-SORT.

### 5. Penghitungan
Dua garis kuning diletakkan di bagian bawah bingkai. Hitungan bertambah setiap kali sebuah objek melewati kedua garis tersebut. Objek dibedakan berdasarkan kelas (bunga, tomat hijau, tomat merah). Penapis ukuran menolak objek yang kotaknya tidak memenuhi ambang tinggi dan lebar maksimum.

## Eksperimen dan Hasil
Detektor dievaluasi pada himpunan uji. Pelacakan dan penghitungan dievaluasi pada satu lorong rumah kaca, dengan hitungan manual sebagai acuan. Galat hitungan dinyatakan sebagai *Mean Absolute Percentage Error* (MAPE) dan akurasi diberikan sebagai pelengkapnya.

Hasil deteksi (Tabel 2, dilaporkan sebagai *best mAP@0.5 and mAP@0.95*):

| Kelas | P | R | mAP@0.5 | mAP@0.95 |
|---|---|---|---|---|
| Semua | 0,741 | 0,570 | 0,630 | 0,321 |
| Bunga | 0,703 | 0,508 | 0,508 | 0,249 |
| Tomat hijau | 0,618 | 0,492 | 0,549 | 0,269 |
| Tomat merah | 0,772 | 0,757 | 0,796 | 0,442 |

Nilai F1 per kelas pada tingkat keyakinan 0,423 adalah 0,74 (tomat merah), 0,56 (tomat hijau), dan 0,61 (bunga), dengan rerata F1 semua kelas 0,63. Penulis menyatakan prediksi terbaik muncul pada tingkat keyakinan 0,5 sampai 0,8.

Hasil hitungan pada satu lorong (Tabel 3), terdiri atas lima segmen pengamatan:

| Kelas | Manual (total) | Drone-AI (total) | MAPE | Akurasi |
|---|---|---|---|---|
| Bunga | 12 | 18 | 50% | 50% |
| Tomat hijau | 237 | 240 | 1% | 99% |
| Tomat merah | 31 | 36 | 15% | 85% |

Selisih sederhana yang dihitung dari tabel: sistem menghitung 6 bunga lebih banyak, 3 tomat hijau lebih banyak, dan 5 tomat merah lebih banyak daripada hitungan manual. Pada segmen individual, hitungan sistem lebih rendah daripada hitungan manual pada tomat hijau segmen 1 (44 terhadap 52), sehingga galat total yang kecil sebagian merupakan hasil saling mengimbangi antarsegmen. Penulis menjelaskan akurasi bunga yang rendah oleh jumlah bunga acuan yang tidak memadai di lingkungan itu.

Penulis menjelaskan bahwa kinerja deteksi tomat merah lebih tinggi karena jumlah sampel latih yang banyak dan ciri warna yang khas, sedangkan tomat hijau lebih rendah karena daun hijau ada di hampir semua area, dan bunga terendah karena sampel sedikit serta kemiripan dengan kelopak tomat.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: hitungan per kelas dalam satu lintasan, proses pencacahan dalam hitungan menit dan bukan jam atau hari, serta penapis ukuran yang mencegah penghitungan ulang objek dari lorong lain. Keterbatasan yang dinyatakan penulis: jumlah bunga untuk pelatihan tidak memadai sehingga galat hitungan bunga 50%. Penulis berencana memperbesar data dan menambah teknik augmentasi pada pekerjaan berikutnya.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, evaluasi hitungan hanya mencakup satu lorong dengan lima segmen, sehingga ketepatan statistiknya terbatas; jumlah bunga acuan hanya 12 dan tomat merah 31. Kedua, teks memuat angka yang tidak konsisten: abstrak menyebut model terbaik pada epoch 96 dengan mAP@0.5 0,618, sedangkan bagian Hasil menyebut epoch 192 dengan mAP@0.5 0,63; abstrak juga menyebut presisi 1 pada keyakinan 0,923 dan F1 pada keyakinan 0,423. Ketiga, nilai mAP@0.5 kelas bunga pada Tabel 2 (0,508) sama dengan nilainya recall, sehingga ada kemungkinan salah ketik yang tidak dapat dipastikan. Keempat, akurasi dihitung dari selisih total per kelas, sehingga galat positif dan negatif antarsegmen saling meniadakan, dan makalah tidak melaporkan ukuran ketepatan identitas pelacakan seperti perpindahan identitas. Kelima, pembagian data berasal dari citra hasil augmentasi sehingga kebocoran antara himpunan latih dan uji tidak dapat dikesampingkan dari teks.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam bingkai video yang berurutan. Mekanismenya adalah pelacakan multi-objek dengan Deep-SORT (filter Kalman, asosiasi Hungarian, dan fitur tampilan) dan penghitungan saat lintasan melewati garis hitung, ditambah penapis ukuran untuk mengabaikan objek dari lorong lain. Cakupannya satu pandang bergerak sepanjang lorong, bukan penyatuan identitas antar sisi atau antar pandangan yang terpisah, dan teks tidak membahas pencocokan antar-lintasan untuk sisi lorong yang berlawanan.

Hitungan dilaporkan per kelas (bunga, tomat hijau, tomat merah), tetapi kelasnya adalah organ tanaman dan warna buah, bukan tingkat kematangan bertahap. Acuan hitungnya adalah hitungan manual pada satu lorong, bukan hasil panen. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola hitungan per kelas dari lintasan terlacak serta penapis ukuran untuk menolak objek di luar baris target. Pola itu tidak menyelesaikan identitas lintas sisi pohon, dan kelas yang tidak seimbang (bunga) terbukti menurunkan akurasi hitungan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `egi2022drone`.

Egi dkk. (2022) membangun sistem pencacahan tomat rumah kaca berbasis video drone DJI Spark yang menggabungkan detektor YOLO V5 dengan pelacak Deep-SORT dan dua garis hitung. Pada kumpulan data 2.329 citra dengan 6.957 anotasi (tiga kelas: bunga, tomat hijau, tomat merah), detektor mencapai mAP@0.5 0,630. Pada satu lorong, akurasi hitungan terhadap hitungan manual dilaporkan 99% untuk tomat hijau, 85% untuk tomat merah, dan 50% untuk bunga.

Catatan verifikasi data: Angka deteksi (mAP@0.5 0,630; mAP@0.95 0,321; nilai per kelas) berasal dari Tabel 2 dan bagian Analysis and Results. Nilai F1 per kelas dan rerata 0,63 berasal dari bagian Analysis and Results serta abstrak. Hitungan manual dan hitungan drone (12 dan 18, 237 dan 240, 31 dan 36), MAPE, dan akurasi berasal dari Tabel 3. Jumlah citra 1.097 dan 2.329, 6.957 anotasi, serta pembagian 70:20:10 berasal dari bagian 2.8 sampai 2.10 dan Kesimpulan. Teks tidak konsisten antara abstrak (epoch 96, mAP@0.5 0,618) dan bagian Hasil (epoch 192, mAP@0.5 0,63). Nilai mAP@0.5 kelas bunga pada Tabel 2 identik dengan recall-nya. Perbedaan jumlah 2.329 citra pada bagian 2.8 dan 2.9 tidak dapat diselesaikan dari teks. Jumlah pohon atau tanaman, kultivar, dan jumlah lorong yang diuji selain satu lorong pada Tabel 3 tidak dilaporkan. Ekstraksi teks mengacak bentuk tabel tetapi nilai angka dapat dibaca; gambar tidak tersedia dari teks.
