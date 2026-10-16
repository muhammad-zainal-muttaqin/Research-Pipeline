# Autonomous UAV Navigation and Mapping for Accurate Fruit Detection and Counting in Controlled Environments: Simulation and Real-World Validation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `garg2025autonomous` |
| Judul asli | Autonomous UAV Navigation and Mapping for Accurate Fruit Detection and Counting in Controlled Environments: Simulation and Real-World Validation |
| Penulis | Garg, Kush; Chandna, Nishant; Aggarwal, Somin; Sehgal, Chirag; Gupta, Arjun; Rohilla, Rajesh |
| Tahun | 2025 |
| Venue | 2025 International Conference on Unmanned Aircraft Systems Icuas 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [garg2025autonomous.pdf](../pdf/garg2025autonomous.pdf)
- DOI resmi: https://doi.org/10.1109/icuas65942.2025.11007888

## Gambaran Umum

Makalah prosiding (ICUAS 2025) ini menyajikan sistem kendaraan udara tak berawak (*unmanned aerial vehicle*, UAV) otonom untuk mencacah buah di lingkungan pertanian terkendali (*Controlled Environment Agriculture*, CEA), yaitu rumah kaca. Sistem terdiri atas perencanaan jalur 3D berbasis algoritma A* hibrida dengan *Traveling Salesman Problem* (TSP), deteksi dan klasifikasi buah dengan YOLOv8 yang di-*fine-tune*, serta pencegahan hitungan ganda. Pengembangan dilakukan lebih dahulu pada simulasi Gazebo, lalu diperluas ke data nyata dengan fusi LiDAR-kamera, pelacakan piksel pusat buah, dan penyaringan awan titik.

Tanaman yang dicacah adalah tomat, paprika (pepper), dan terung pada simulasi, serta buah kuning dan merah pada data nyata. Akurasi hitungan rerata pada simulasi adalah 98,18% (12 skenario), sedangkan pada data nyata presisi rerata adalah 90,12% untuk buah merah dan 87,21% untuk buah kuning (5 penerbangan). Sistem ini dipakai pada kompetisi UAV ICUAS 2024 dengan peringkat kedua pada fase simulasi dari 24 tim dan peringkat ketiga keseluruhan pada fase dunia nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Tugas yang didefinisikan adalah UAV yang secara otonom mencacah beberapa jenis buah pada bedeng tanam tertentu di rumah kaca, dengan sasaran akurasi tinggi, waktu singkat, dan lintasan pendek. Penulis menyebut metode visi komputer klasik berbasis deteksi dan segmentasi warna gagal pada oklusi parsial dan variasi cahaya. Solusi pencarian urutan kunjungan seperti pencarian menyeluruh dan algoritma genetika dinilai mahal secara komputasi, sedangkan algoritma serakah dinilai tidak memberi aproksimasi memuaskan.

Pada lingkungan nyata, data bising menimbulkan hitungan ganda dan deteksi keliru. Fusi LiDAR-kamera dinilai rentan terhadap pergeseran (*drift*) dan derau, dan keterlambatan sinkronisasi data pada tanaman rimbun dapat memetakan cabang atau daun sebagai buah sehingga menambah positif palsu. Tanaman pada simulasi juga asimetris antara sisi depan dan belakang, sehingga sebuah buah dapat terlihat dari depan, belakang, atau keduanya.

## Ide Utama

Penulis menggabungkan tiga komponen. Pertama, lingkungan statis disederhanakan menjadi graf simpul sehingga perencanaan jalur dapat dibagi menjadi pencarian jalur terpendek antarsimpul (A* berbobot dengan tiga heuristik) dan penentuan urutan kunjungan (pohon rentang minimum dan algoritma Christofides). Kedua, pada simulasi buah yang terlihat dari sisi depan dan belakang dicocokkan melalui posisi relatif terhadap tepi bedeng. Ketiga, pada data nyata buah dilokalisasi dalam koordinat global dengan fusi LiDAR-kamera, dilacak pada 30 bingkai berurutan, difilter secara statistik, lalu dikelompokkan sehingga buah yang dikunjungi ulang atau dilihat dari sudut lain tidak dihitung dua kali.

## Cara Kerja Langkah demi Langkah

### 1. Lingkungan simulasi dan data

Simulasi berjalan di Gazebo 11 dengan ROS Noetic pada Ubuntu 20.04. Lingkungan memuat 27 bedeng tanam dalam 3 baris dan 3 tingkat, tiap bedeng berisi hingga tiga tanaman dari tiga jenis buah (tomat merah, paprika kuning, terung ungu). UAV hanya boleh terbang di sepanjang dan di sekitar rak. Lingkungan disederhanakan menjadi 90 simpul: 2 × n simpul untuk n bedeng (sisi depan dan belakang) dan 12 × r simpul pada ujung baris (r baris).

Data dunia nyata berasal dari fase akhir kompetisi ICUAS 2024 berupa berkas ROSBAG berisi umpan kamera RGB, LiDAR, IMU, dan GPS dari UAV pada lingkungan pertanian nyata dengan buah kuning dan merah. Perangkat keras terdiri atas quadcopter Kopterworx Hawk dengan kamera Intel RealSense D415, LiDAR Velodyne VLP-16, dan modul GPS RTK. Jumlah citra latih dan rincian pelatihan YOLOv8 tidak dilaporkan.

### 2. Perencanaan jalur

A* memakai heuristik gabungan h(n, g) = h_d + h_yaw + h_altitude, yaitu jarak Euklides ke tujuan, biaya penyesuaian yaw, dan bobot ketinggian (naik lebih mahal daripada turun). Urutan simpul pada tiap sisi ditentukan dengan menyusun matriks jarak dari bobot jalur A*, membentuk pohon rentang minimum, lalu menerapkan algoritma Christofides agar tiap simpul hanya memiliki dua sambungan. Penelusuran dilakukan baris demi baris karena perpindahan antarbaris hanya dapat melalui ujung baris.

### 3. Persepsi pada simulasi

Setelah UAV tiba di bedeng, beberapa citra diambil. Segmentasi berbasis kedalaman memisahkan objek di area minat dari latar, dan data IMU dipakai merotasi citra agar tanaman sejajar. Model YOLOv8-S yang di-*fine-tune* melakukan deteksi dan klasifikasi. Citra pencilan disaring dengan membandingkan jumlah bedeng dan jumlah buah terhadap median. Pandangan depan dan belakang dicocokkan melalui posisi bedeng yang diketahui. Buah dianggap sama pada kedua pandangan bila selisih jarak buah depan ke tepi kiri dan atas bedeng terhadap jarak buah belakang ke tepi kanan dan atas berada di bawah ambang; selanjutnya dipakai selisih rasio jarak terhadap lebar atau tinggi. Hitungan tiap rak dijumlahkan menjadi hitungan akhir.

### 4. Persepsi pada data nyata

Koordinat GPS dikonversi ke kerangka ENU lokal dengan titik awal lepas landas, lalu digeser sesuai ofset antara modul GPS dan LiDAR. Awan titik LiDAR dirotasi menurut roll, pitch, dan yaw dari IMU (Persamaan 5) dan ditambahkan ke posisi UAV untuk membentuk peta 3D. Kalibrasi intrinsik kamera memakai kisi AprilTag, dan kalibrasi ekstrinsik LiDAR-kamera dinyatakan dengan Persamaan 6 sehingga setiap piksel memperoleh koordinat 3D.

YOLOv8-S di-*fine-tune* pada data rumah kaca; ambang keyakinan menyaring deteksi latar yang keliru terklasifikasi sebagai kuning. Piksel pusat tiap buah dilacak selama 30 bingkai berurutan; bila perubahan piksel pusat berada di bawah ambang, titik-titik 3D pada bingkai itu dianggap milik buah yang sama. Buah diberi nomor bila memiliki lebih dari 15 titik, selain itu dibuang. Titik yang menyimpang jauh dari rerata dibuang. Klaster baru yang tumpang tindih dengan klaster yang sudah ada dianggap buah yang sama, sehingga buah tidak terhitung dua kali ketika pelacakan hilang, UAV kembali ke buah itu, atau buah dilihat dari belakang atau samping.

## Eksperimen dan Hasil

Pada simulasi, Tabel I melaporkan 12 skenario dengan daftar bedeng yang dikunjungi, jumlah buah kebenaran dasar (GT), jumlah prediksi, dan akurasi. Rerata akurasi 98,18%. Skor kumulatif 94,80 pada konfigurasi tak terlihat di ICUAS 2024 menggabungkan akurasi hitungan, total waktu, dan total jarak (Gambar 5).

| Skenario | Jumlah bedeng dikunjungi | GT | Prediksi | Akurasi (%) |
|---|---|---|---|---|
| 1 | 6 | 12 | 12 | 100 |
| 2 | 3 | 0 | 0 | 100 |
| 3 | 6 | 12 | 12 | 100 |
| 4 | 6 | 11 | 11 | 100 |
| 5 | 7 | 5 | 5 | 100 |
| 6 | 1–27 (semua) | 35 | 33 | 94,28 |
| 7 | 7 | 18 | 18 | 100 |
| 8 | 6 | 22 | 21 | 95,45 |
| 9 | 7 | 17 | 17 | 100 |
| 10 | 7 | 15 | 15 | 100 |
| 11 | 7 | 11 | 11 | 100 |
| 12 | 7 | 15 | 13 | 86,67 |

Jumlah bedeng pada kolom kedua dihitung dari daftar nomor bedeng pada Tabel I.

Pada data nyata, Tabel II melaporkan lima penerbangan.

| Penerbangan | GT kuning | GT merah | Terdeteksi kuning | Terdeteksi merah | Presisi kuning (%) | Presisi merah (%) |
|---|---|---|---|---|---|---|
| 1 | 12 | 8 | 14 | 10 | 85,71 | 80,00 |
| 2 | 14 | 14 | 16 | 13 | 87,50 | 92,86 |
| 3 | 15 | 11 | 17 | 12 | 88,24 | 91,67 |
| 4 | 11 | 13 | 13 | 12 | 84,62 | 92,31 |
| 5 | 18 | 16 | 20 | 15 | 90,00 | 93,75 |
| Rerata | | | | | 87,21 | 90,12 |

Makalah tidak mendefinisikan "presisi" pada Tabel II; nilai baris tabel tampak sama dengan rasio GT terhadap jumlah terdeteksi (misalnya 12/14 = 85,71%), yang merupakan pembacaan ringkasan ini. Penulis menyatakan hasil dekat 100% pada simulasi disebabkan citra latih dan uji berasal dari domain yang sama tanpa variasi data. Tantangan utama pada data nyata adalah buah tertutup sebagian oleh daun sehingga daun terpetakan sebagai buah; hal ini diatasi dengan pelacakan visual dan penyaringan titik di luar klaster buah padat.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis adalah penghematan waktu dan jalur melalui perencanaan hibrida A*-TSP, serta pencegahan hitungan ganda pada kondisi bising melalui koordinat global dan penyaringan awan titik. Sistem divalidasi pada kompetisi dengan peringkat kedua pada fase simulasi dan ketiga pada fase dunia nyata.

Keterbatasan yang dinyatakan penulis: akurasi simulasi mendekati 100% karena domain data seragam; kalibrasi kamera-LiDAR sulit dijaga walau properti ekstrinsik berubah sedikit; dan identifikasi ulang buah yang sama merupakan aspek penting yang menantang. Pekerjaan lanjutan mencakup penerapan pada lingkungan pertanian lain dan penambahan deteksi kondisi buah, tahap pertumbuhan, serangga, dan gulma.

Menurut pembacaan ringkasan ini, evaluasi dunia nyata hanya mencakup lima penerbangan dengan jumlah buah per penerbangan yang kecil (8 hingga 18 per warna), tanpa ukuran ragam. Seluruh nilai presisi pada Tabel II di bawah 100% disertai jumlah terdeteksi yang lebih besar daripada GT, yang menunjukkan kecenderungan hitung berlebih. Pencocokan depan-belakang pada simulasi bergantung pada posisi bedeng yang diketahui sebelumnya sehingga bergantung pada lingkungan statis dan tata letak yang tetap. Ambang pelacakan dan penyaringan tidak diberi nilai numerik selain 30 bingkai dan 15 titik.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali. Pada simulasi mekanismenya adalah pencocokan geometris pandangan depan dan belakang bedeng memakai posisi buah relatif terhadap tepi bedeng. Pada data nyata mekanismenya adalah pelacakan piksel pusat pada 30 bingkai, lokalisasi 3D global dengan fusi LiDAR-kamera, penyaringan statistik, dan penggabungan klaster yang tumpang tindih. Hitungan dilaporkan per jenis buah (kuning dan merah pada data nyata; tomat, paprika, dan terung pada simulasi dikelaskan oleh detektor, tetapi Tabel I melaporkan jumlah gabungan). Acuan hitung adalah kebenaran dasar yang dinyatakan pada tabel; asal penetapannya (hitung manual atau anotasi) tidak dijelaskan di teks.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan mencocokkan objek antarsisi berdasarkan posisi relatif terhadap kerangka tetap, serta penggabungan klaster yang tumpang tindih pada koordinat global. Pemindahan itu memerlukan pose kamera terukur (GPS RTK, IMU, LiDAR) yang tidak tersedia pada pemotretan ponsel pintar dari sisi pohon, dan lingkungan rumah kaca statis dengan tata letak tetap berbeda dari kebun terbuka.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `garg2025autonomous`.

Garg dkk. menyajikan sistem UAV otonom untuk pencacahan buah di rumah kaca yang menggabungkan perencanaan jalur A* hibrida dengan TSP, deteksi YOLOv8, pencocokan sisi depan dan belakang bedeng pada simulasi, dan pelacakan serta fusi LiDAR-kamera dengan penyaringan awan titik pada data nyata untuk mencegah hitungan ganda. Akurasi hitungan rerata adalah 98,18% pada simulasi dan presisi rerata 90,12% (merah) dan 87,21% (kuning) pada lima penerbangan nyata.

Catatan verifikasi data: Angka simulasi bersumber dari Tabel I dan teks seksi III-A.3; angka dunia nyata dari Tabel II dan seksi III-B.7; skor kumulatif 94,80 dari seksi III-A.3. Pada ekstraksi teks, kolom Tabel I tampak terpisah per sel namun nilainya dapat dipasangkan dan rerata 98,18% tertulis. Abstrak menyebut 98% dan 90%, yaitu pembulatan dari nilai tersebut. Definisi "presisi", jumlah citra latih, dan metrik deteksi YOLOv8 tidak dilaporkan; gambar tidak terbaca dari teks. Pada teks, Persamaan 4 diberi label "Altitude Weight (h_yaw)", yang tampak sebagai salah ketik. Lingkungan nyata disebut "rumah kaca" dan tanaman tidak disebut spesifik.
