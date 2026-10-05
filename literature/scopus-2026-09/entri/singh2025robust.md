# Robust real-time strawberry maturity detection using UAV-mounted deep learning for precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `singh2025robust` |
| Judul asli | Robust real-time strawberry maturity detection using UAV-mounted deep learning for precision agriculture |
| Penulis | Singh, Rajmeet; Gadade, Appaso M.; Hussain, Irfan |
| Tahun | 2025 |
| Venue | BMC Plant Biology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [singh2025robust.pdf](../pdf/singh2025robust.pdf)
- DOI resmi: https://doi.org/10.1186/s12870-025-07246-7

## Gambaran Umum
Makalah ini melaporkan sistem pemantauan stroberi (*Fragaria* spp.) di dalam rumah kaca yang terdiri atas dua bagian: model deteksi stroberi matang bernama YOLOv9-GLEAN (pada teks juga tertulis YOLOv9-GELAN) dan pengendali pelacakan lintasan hibrida PID+LQR untuk pesawat nirawak empat rotor (*quadrotor*). Sistem diuji pada simulasi Gazebo yang meniru rumah kaca Silal di Abu Dhabi dan pada rumah kaca nyata di lokasi yang sama. Pesawat nirawak terbang mengikuti titik rute (*waypoint*) yang ditentukan sebelumnya pada ketinggian sekitar 4 m dengan kecepatan 2 m/s, sedangkan deteksi dan pencacahan stroberi matang dilakukan secara otonom dari video kamera onboard.

Data pelatihan terdiri atas 1.050 citra satu kelas (stroberi matang): 800 citra nyata dari rumah kaca dan 250 citra sintetis berbasis CAD yang dibuat dengan Blender. Pada rangkaian pembanding (Tabel 2), YOLOv9-s + GLEAN memperoleh presisi 0,991 dan *recall* 0,990, dan kurva presisi-*recall* memberi mAP@0,5 sebesar 0,994. Pada pengujian pencacahan di rumah kaca nyata (Tabel 5), akurasi hitungan dari video pesawat nirawak terhadap hitungan acuan (*ground truth*) berkisar 89,7% sampai 95,7% menurut waktu pengamatan. Kesimpulan makalah menyebut akurasi pencacahan 94,6% pada simulasi dan 95,7% pada lapangan.

Pengendali hibrida PID+LQR dibandingkan dengan PID dan LQR tunggal pada uji respons langkah (Tabel 4) dan memberi *overshoot* terendah, yaitu 10,85%. Sebagian besar halaman makalah memuat pemodelan dinamika dan perancangan pengendali, bukan pencacahan buah.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pemantauan rumah kaca secara manual bersifat padat karya dan sulit diskalakan. Metode visi komputer klasik (pencocokan templat, fitur SIFT/SURF, segmentasi warna) dinilai rentan terhadap variasi cahaya, oklusi daun dan ranting, serta tekstur latar yang kompleks. Penulis juga menyatakan belum ada penelitian yang secara khusus menggunakan UAV untuk pemantauan stroberi di rumah kaca, baik pada simulasi maupun dunia nyata.

Kendala khusus yang disebut adalah GPS tidak berfungsi di dalam rumah kaca karena atap berlapis film polietilen (PE). Karena itu pesawat nirawak dinavigasi dengan titik rute yang ditentukan sebelumnya (semiotonom dalam navigasi, otonom penuh dalam deteksi stroberi matang).

## Ide Utama
Gagasan makalah adalah mengintegrasikan detektor satu tahap berbasis YOLOv9 yang ringan untuk objek kecil dengan pengendali PID+LQR pada satu platform pesawat nirawak, lalu memvalidasinya pada kembaran digital (*digital twin*) rumah kaca dan pada rumah kaca sebenarnya. Pengendali PID dipakai untuk loop luar (ketinggian dan posisi), sedangkan LQR dipakai untuk loop dalam (stabilisasi sikap), menurut penjelasan penulis. Hukum kendali total dituliskan sebagai $U_T = U_{PID} + U_{LQR}$.

Pencacahan dilakukan dengan menjalankan bobot terlatih (`best.pt`) pada antarmuka ROS, memberi nomor identitas (*ID*) terpisah pada setiap stroberi yang terdeteksi, dan menghitung objek yang melewati garis penghitung (*line counter*) berwarna merah. Algoritma pelacak yang memberi ID tidak disebutkan namanya di teks.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Pesawat nirawak merekam video saat terbang di atas tanaman. Pesawat yang dipakai untuk simulasi dan uji nyata adalah Modal AI Starling 2 dengan bobot lepas landas 285 g, waktu terbang 40 menit, kamera berwarna 12 MP, GPS UBlox M10, dan cip Qualcomm QRB5165 (Tabel 3). Dataset berjumlah 1.050 citra (800 nyata, 250 sintetis CAD) dengan satu kelas, stroberi matang. Teknik *domain randomization* (variasi kecerahan, latar, dan area bayangan) diterapkan pada citra. Anotasi dilakukan dengan CVAT. Augmentasi mencakup rotasi, pembalikan, dan pengaburan. Pembagian data 70:20:10, yaitu 735 citra latih, 210 validasi, dan 105 uji. Jumlah pohon atau tanaman, kultivar, dan jumlah kotak pembatas tidak dilaporkan.

### 2. Arsitektur detektor
Model dasar adalah YOLOv9 dengan blok GELAN (*Generalized ELAN*, gabungan konsep CSPNet dan ELAN). Masukan berukuran 640 x 640 x 3. Backbone memakai dua blok konvolusi (kernel 3, stride 2), blok RepNCSPELAN, blok ADown, dan SPPELAN. Neck memakai *upsample* dan *concat*, dan kepala memiliki tiga blok deteksi untuk objek kecil, sedang, dan besar. Penulis memilih YOLOv9 dibanding YOLOv10 sampai v12 dengan alasan keseimbangan akurasi, kecepatan, dan ukuran model untuk perangkat tepi, serta ketahanan terhadap pergeseran domain pada data campuran sintetis-nyata. Teks mengaitkan GLEAN dengan kemampuan resolusi super (*super-resolution*) yang mengurangi positif dan negatif palsu, tetapi tidak menjelaskan modul GLEAN secara rinci, sehingga rincian arsitektur GLEAN tidak dapat diverifikasi dari teks.

### 3. Pelatihan
Pelatihan memakai laju belajar awal 0,001, momentum 0,90, *weight decay* 0,0005, ukuran batch 16, dan citra 640, pada GPU NVIDIA RTX 3090 dengan PyTorch. Teks menyebut 300 epoch pada bagian konfigurasi, tetapi analisis kurva latih menyebut 200 epoch. Model yang dilatih adalah YOLOv9-GELAN, YOLOv9, dan YOLOv8. Metrik yang dipakai adalah presisi, *recall*, F1, AP, dan mAP.

### 4. Pemodelan dan pengendali pesawat nirawak
Dinamika dimodelkan dengan kuaternion dan persamaan gerak enam derajat kebebasan di MATLAB-Simulink. Asumsinya adalah badan kaku, tanpa gangguan eksternal (angin), dan gravitasi konstan. Pengendali PID disusun untuk ketinggian, *roll*, *pitch*, *yaw*, dan posisi. LQR dirancang dari model yang dilinearisasi pada posisi melayang, dengan matriks $Q$ dan $R$ berupa matriks identitas. Simulasi memakai kosimulasi Simulink-Gazebo melalui ROS (Noetic, Ubuntu 20.04).

### 5. Pencacahan stroberi matang
Bobot terlatih diintegrasikan ke ROS untuk mendeteksi dan melacak stroberi matang secara waktu nyata pada video dari simulasi dan dari rumah kaca nyata. Setiap stroberi diberi ID, lalu dihitung saat melewati garis penghitung. Hasil dibandingkan dengan hitungan acuan pada Tabel 5.

## Eksperimen dan Hasil
Detektor dievaluasi pada data validasi (teks menyebut evaluasi pada "validation dataset"). Matriks konfusi (Gambar 7) dilaporkan dengan total 735 prediksi untuk ketiga model. Angka 735 sama dengan jumlah citra latih; teks tidak menjelaskan hubungan ini, sehingga data yang dipakai untuk matriks konfusi tidak dapat dipastikan.

| Model | TP | FN | FP |
|---|---|---|---|
| YOLOv8 | 711 | 22 | 3 |
| YOLOv9 | 719 | 15 | 1 |
| YOLOv9-GLEAN | 724 | 10 | 1 |

Perbandingan model pada Tabel 2:

| Model | Parameter (M) | FLOPs | Presisi | *Recall* | FPS | Ukuran (MB) | Inferensi (ms) |
|---|---|---|---|---|---|---|---|
| YOLOv12 | 24 | 21,5 | 0,987 | 0,98 | 27 | 45 | 2,0 |
| YOLOv11 | 14 | 21,6 | 0,981 | 0,99 | 26 | 27 | 1,9 |
| YOLOv10-s | 11,3 | 26,0 | 0,99 | 0,992 | 25 | 21 | 1,5 |
| YOLOv8-s | 11,2 | 25,6 | 0,98 | 0,979 | 28 | 22,5 | 0,9 |
| YOLOv9-s + GLEAN (diusulkan) | 11,2 | 25,0 | 0,991 | 0,990 | 30 | 23 | 0,75 |

Kurva pada Gambar 9 memberi F1 0,99 pada ambang keyakinan 0,471, presisi 1,00 pada ambang 0,943, dan mAP@0,5 0,994. Kurva latih (Gambar 8) menunjukkan mAP50 sekitar 1,0 dan mAP50-95 sekitar 0,95. Kesimpulan menyebut pemrosesan waktu nyata 23 fps, sedangkan Tabel 2 menyebut 30 FPS untuk model yang sama; perbedaan ini tidak dijelaskan. Selisih presisi antarmodel pada Tabel 2 sangat kecil (0,980 sampai 0,991), dan makalah tidak melaporkan pengulangan seed atau uji signifikansi.

Pengendali pada uji respons langkah (Tabel 4):

| Pengendali | *Overshoot* (%) | Waktu naik (s) | Waktu tunak (s) |
|---|---|---|---|
| PID | 30,77 | 0,79 | 0,77 |
| LQR | 23,44 | 0,53 | 0,51 |
| PID+LQR (diusulkan) | 10,85 | 0,63 | 0,61 |

Pada uji lintasan nyata di rumah kaca Silal, pesawat nirawak mengikuti lintasan persegi dengan kinerja yang disebut memuaskan. Penulis menyebut presisi posisi sekitar ±5 cm pada bagian diskusi; angka ini tidak disertai tabel pengukuran.

Pencacahan di rumah kaca nyata (Tabel 5):

| Waktu | Rerata stroberi matang (hitungan video pesawat nirawak) | Hitungan acuan | Akurasi (%) |
|---|---|---|---|
| 08.30 | 45 | 47 | 95,7 |
| 12.30 | 46 | 49 | 93,8 |
| 18.30 | 44 | 49 | 89,7 |

Teks ekstraksi Tabel 5 menempatkan kolom "Avg. ripe strawberry counting video" dan "Ground truth", sehingga pemetaan kolom di atas adalah pembacaan ringkasan ini; ketiganya konsisten dengan akurasi sebagai rasio hitungan video terhadap acuan. Akurasi 93,8% dan 89,7% sedikit berbeda dari hasil pembagian sederhana 46/49 (sekitar 93,9%) dan 44/49 (sekitar 89,8%) yang dihitung ringkasan ini. Hasil pencacahan simulasi hanya muncul sebagai angka 94,6% pada kesimpulan, tanpa tabel pada teks yang tersedia.

## Kelebihan dan Keterbatasan
Kelebihan: sistem menggabungkan detektor, pelacakan lintasan, dan pencacahan dalam satu platform yang diuji pada simulasi dan rumah kaca nyata; dataset menggabungkan citra nyata dan sintetis; kinerja detektor dibandingkan dengan beberapa versi YOLO.

Keterbatasan yang dinyatakan penulis: pengendali ganda meningkatkan kompleksitas komputasi; sistem sensitif terhadap ketidakpastian model (pergeseran pusat gravitasi akibat peralatan, perubahan parameter motor akibat baterai atau suhu); gangguan frekuensi tinggi seperti arus udara ventilasi di atas 2 m/s belum ditangani; model diasumsikan tanpa angin dan tanpa penghalang pada ketinggian terbang; pada diskusi disebut pengurangan waktu terbang 8 sampai 12% akibat beban komputasi. Penulis juga menyatakan rencana integrasi odometri visual dan sensor tambahan.

Menurut pembacaan ringkasan ini, terdapat keterbatasan lain. Pertama, dataset hanya satu kelas (matang), sehingga makalah tidak menunjukkan klasifikasi kematangan multikelas walaupun judulnya menyebut deteksi kematangan. Kedua, metrik hampir jenuh (mAP@0,5 0,994) pada 105 citra uji, tanpa pengulangan, dan sumber data matriks konfusi tidak jelas. Ketiga, ada ketidakkonsistenan internal: penamaan GLEAN dan GELAN, 300 dan 200 epoch, 30 FPS dan 23 fps. Keempat, pembanding PID dan LQR pada Tabel 4 diberi rujukan literatur, sehingga tidak jelas apakah dibandingkan pada model yang sama. Kelima, hitungan acuan di lapangan hanya berupa tiga pengamatan dengan sekitar 44 sampai 49 buah, tanpa menjelaskan cara memperoleh acuan, dan akurasi dihitung dari rasio hitungan total, sehingga galat positif palsu dan negatif palsu dapat saling meniadakan. Keenam, klaim pengurangan waktu pemantauan 75 sampai 80% pada diskusi tidak didukung pengukuran pada bagian hasil.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali hanya sebatas pada video: stroberi diberi ID dan dihitung ketika melewati garis penghitung, sehingga mekanismenya berupa pelacakan dalam video dengan penghitung garis (kode C1, pelacakan video). Tidak ada pencocokan lintas pandang, rekonstruksi 3D, atau koreksi statistik dua sisi. Algoritma pelacak, aturan asosiasi, dan penanganan ID yang terputus atau tertukar tidak dijelaskan, serta tidak ada metrik pelacakan seperti peralihan ID (*ID switch*).

Hitungan dilaporkan untuk satu kelas saja (stroberi matang), bukan per kelas. Acuan hitungannya adalah "ground truth" pada Tabel 5 yang cara penentuannya tidak dijelaskan (tidak jelas apakah hitung manual lapangan, panen, atau anotasi video). Hal yang dapat dipindahkan ke pencacahan tandan sawit multisisi terbatas: gagasan penghitung garis dengan ID pelacak dapat dipakai untuk satu sisi bila video tersedia, tetapi makalah tidak memberi bukti untuk identitas lintas sisi pohon, dan tiga pengukuran dengan sekitar 45 buah tidak memadai sebagai bukti kinerja pencacahan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `singh2025robust`.

Singh dkk. (2025, *BMC Plant Biology* 25:1367) mengembangkan sistem deteksi stroberi matang berbasis YOLOv9-GLEAN yang dipasang pada pesawat nirawak empat rotor dengan pengendali lintasan hibrida PID+LQR untuk pemantauan rumah kaca. Model dilatih pada 1.050 citra satu kelas (800 nyata, 250 sintetis) dan melaporkan presisi 0,991, *recall* 0,990, serta mAP@0,5 0,994. Pencacahan berbasis ID pelacak dan garis penghitung pada rumah kaca nyata memberi akurasi 89,7% sampai 95,7% terhadap hitungan acuan pada tiga waktu pengamatan. Pencacahan dilakukan untuk satu kelas dari satu video, tanpa mekanisme identitas lintas pandang.

Catatan verifikasi data: Jumlah citra dan pembagian data (1.050; 735/210/105) ada pada bagian Dataset. Presisi, *recall*, FPS, dan inferensi ada pada Tabel 2; mAP@0,5 0,994 dan F1 0,99 pada Gambar 9 (teks keterangan gambar dan paragraf sekitarnya); jumlah TP/FN/FP pada paragraf Gambar 7; metrik pengendali pada Tabel 4; hasil pencacahan pada Tabel 5, dan 94,6% serta 95,7% pada Kesimpulan. Tabel 5 dari ekstraksi PDF terpisah per sel sehingga susunan kolom dibaca dari urutan sel. Tidak dapat diverifikasi dari teks: rincian modul GLEAN, algoritma pelacak, cara penentuan hitungan acuan, hasil pencacahan simulasi dalam bentuk tabel, jumlah tanaman dan kultivar, serta data yang dipakai untuk matriks konfusi. Ketidakkonsistenan angka (300 dan 200 epoch; 30 dan 23 fps) ada pada teks aslinya. Gambar dan persamaan matriks pada teks ekstraksi sebagian terpecah, tetapi tidak memengaruhi angka utama.
