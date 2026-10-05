# Apple Detection and Counting Using Neural Networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `garderes2024apple` |
| Judul asli | Apple Detection and Counting Using Neural Networks |
| Penulis | Garderes, Roxana; Guti\'errez, Facundo; Tanco, Mercedes Marzoa; Tejera, Gonzalo |
| Tahun | 2024 |
| Venue | Proceedings 2024 50th Latin American Computing Conference Clei 2024 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [garderes2024apple.pdf](../pdf/garderes2024apple.pdf)
- DOI resmi: https://doi.org/10.1109/clei64178.2024.10700174

## Gambaran Umum
Makalah ini (prosiding CLEI 2024, berbahasa Inggris pada abstrak dan Spanyol pada isi) mengkaji deteksi dan pencacahan apel pada video barisan pohon menggunakan detektor berbasis jaringan saraf dan algoritma pelacakan. Empat detektor dilatih: YOLOv5 (varian *small*), YOLOv8 (varian *nano*), dan dua varian Faster R-CNN dari Detectron2 (Faster-50 dan Faster-101). Tiga pelacak diuji: StrongSort, ByteTrack, dan OCSort. Penulis juga membangun simulator kebun apel berbasis ROS untuk menghasilkan video berlabel, dan mengevaluasi dua model koreksi hitungan, yaitu regresi linear dan koefisien pengali.

Data berasal dari lima set citra untuk deteksi (tiga dari Roboflow, dua buatan sendiri di INIA Las Brujas, Uruguay), set MinneApple, serta video barisan apel nyata dan simulasi untuk pelacakan. Detektor terbaik adalah YOLOv5 dan YOLOv8 yang dilatih pada DS2: AP50 uji 0,906 dan 0,904 pada set ujinya sendiri (Tabel I), dan AP50 0,865 serta 0,853 pada DS5 (Tabel II). Abstrak melaporkan mAP50 0,87 dan 0,85. OCSort dinilai pelacak terbaik dengan HOTA tertinggi 60,24% dan waktu sekitar 30 ms per bingkai.

Pada video penuh satu barisan dengan 2.133 apel yang dipanen, semua kombinasi menghasilkan hitungan jauh di atas nilai sebenarnya (3.695 sampai 5.782). Koreksi berkoefisien menurunkan galat relatif rata-rata menjadi 0,20 pada video nyata penuh, sedangkan regresi linear menghasilkan 0,45.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkiraan jumlah buah yang akan dipanen mendukung perencanaan penjualan, tenaga kerja, dan distribusi. Pencacahan di kebun terbuka sulit karena ukuran, warna, dan bentuk buah bervariasi, serta karena oklusi oleh buah lain, ranting, dan daun. Cuaca, waktu pengambilan, dan lintasan perekaman mengubah visibilitas barisan pohon yang bersebelahan, sehingga hasil hitungan berubah.

Penulis menyatakan dua kendala tambahan. Pertama, set citra apel publik cukup untuk deteksi, tetapi tidak ditemukan rekaman video barisan penuh yang diperlukan untuk menguji pencacahan. Kedua, pada pencacahan video, hitungan ganda terjadi ketika buah tertutup sementara lalu tampak kembali, atau terlihat dari kedua sisi barisan. Penulis juga mencatat bahwa tiga kategori buah menurut visibilitas, yaitu terlihat dari satu sisi, dari kedua sisi, dan tidak terlihat dari luar pohon, menyebabkan galat pada pencacahan berbasis pelacakan.

## Ide Utama
Gagasan utamanya adalah menyatukan detektor satu kelas (apel) dengan pelacak multi-objek (*multi-object tracking*, MOT) sehingga jumlah identitas unik yang ditetapkan pelacak menjadi hitungan buah. Karena hitungan itu menyimpang akibat visibilitas variabel, penulis menambahkan koreksi statistik sederhana yang dikalibrasi pada video simulasi dengan jumlah apel yang diketahui pasti.

Simulator dipakai untuk memperoleh kebenaran dasar (*ground truth*) jumlah dan koordinat apel yang tidak tersedia pada video lapangan. Penulis menyatakan simulator itu hanya alat pelengkap yang mengabaikan pencahayaan, tekstur, ketidakrataan jalan, dan cuaca, sehingga tidak menggantikan validasi di lapangan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Set deteksi: DS1 (232 citra, Roboflow, apel terokulasi sebagian tidak diberi label), DS2 (1.789 citra, Roboflow, memuat MinneApple, citra udara, dan citra jarak dekat), DS3 (331 citra), DS4 (80 citra buatan sendiri di INIA Las Brujas dengan Xiaomi Redmi Note 11 Pro 5G, pohon sebagian tertutup jaring burung), DS5 (48 citra buatan sendiri tanpa jaring), dan DS7 (MinneApple: 41.000 apel berlabel pada 1.000 citra selama dua tahun). Pembagian data latih, validasi, dan uji adalah 70%, 20%, dan 10%. Augmentasi mencakup *crop*, rotasi ±15°, saturasi ±40%, kecerahan ±50%, eksposur ±15%, dan *blur* hingga 1 px.

Set pelacakan: DS-SIM (video simulasi 6 detik, satu barisan empat pohon, 61 apel), DS-INIA-1 (20 detik, 139 apel), dan DS-INIA-2 (25 detik, 200 apel). Video lapangan direkam dengan Samsung Galaxy S21 FE pada robot Jackal, satu sisi barisan pada arah pergi dan sisi lain pada arah kembali, sekitar 200 bingkai berlabel per bagian. Video tanpa label: DS-INIA-IDA (2 menit 38 detik), DS-INIA-VUELTA (2 menit 39 detik), dan DS-INIA-COMPLETO (5 menit 45 detik). Pada barisan itu dipanen 2.133 apel, tetapi jumlah yang tampak pada video tidak diketahui.

### 2. Simulator
Simulator memakai ROS, Ignition Gazebo, dan API Python Blender, berasal dari proyek Fields Ignition. Pohon dibangkitkan dengan cabang utama dan sekunder, lalu daun dan buah ditambahkan secara acak. Parameter mencakup jumlah baris, jumlah pohon per baris, jarak antarpohon, dan jarak antarbaris. Robot Husky dengan kamera RGB dikonfigurasi menyerupai lensa ZED 2.

### 3. Deteksi
YOLOv5s, YOLOv8n, Faster-50 (`faster_rcnn_R_50_FPN_3x`), dan Faster-101 (`faster_rcnn_X_101_32x8d_FPN_3x`) dilatih di Google Colab dengan variasi jumlah *epoch* (20, 50, 100, 200, 500 sesuai bobot model). Metrik utama adalah AP50.

### 4. Pelacakan
Pelacakan memakai pustaka BoxMOT dengan OCSort, ByteTrack, dan StrongSort. Metrik dari MOT Challenge adalah MOTA, IDF1, dan HOTA, ditambah EAIDs (galat absolut jumlah identitas yang ditetapkan).

### 5. Koreksi hitungan
Dua model koreksi dibangun dari 20 instansi simulator berbaris lima pohon (kecepatan 0,2 m/s, kamera tetap). Model pertama adalah regresi linear dari hitungan prediksi ke hitungan sebenarnya. Model kedua adalah koefisien pengali, yaitu rerata rasio hitungan sebenarnya terhadap hitungan prediksi. Instansi uji: V1_5 (satu baris lima pohon, 375 apel), V1_10 (sepuluh pohon, 722 apel), V3_5 (tiga baris lima pohon, 362 apel pada baris yang diamati), dan video nyata penuh.

## Eksperimen dan Hasil
Hasil deteksi terbaik per model pada set uji DS2 (Tabel I) dan hasil sebagian model pada DS5 (Tabel II, dilatih pada DS2) ditampilkan di bawah.

| Model | Epoch (Tabel I) | AP50 uji DS2 | AP50 pada DS5 | Waktu pada DS5 (ms) |
|---|---|---|---|---|
| YOLOv5 | 50 | 0,906 | 0,865 | 14,3 |
| YOLOv8 | 200 | 0,904 | 0,853 | 4,9 |
| Faster-101 | 20 | 0,869 | 0,783 | 282,0 |
| Faster-50 | 50 | 0,878 | 0,773 | 139,0 |

Pada DS5, DS4 yang hanya 80 citra memberi AP50 0,854 (YOLOv5) dan 0,850 (YOLOv8), lebih tinggi daripada DS7 (MinneApple, 0,836 dan 0,823), meskipun DS7 berisi 1.000 citra. Penulis menyimpulkan bahwa kemiripan data latih dengan data uji berpengaruh, dan bahwa set citra berlabel untuk pemanenan tidak memadai untuk pelatihan deteksi dan pencacahan.

Hasil pelacakan pada data berlabel (Tabel III) untuk OCSort. Penugasan baris ke set data mengikuti urutan pada tabel yang terekstraksi.

| Detektor | Set | HOTA | MOTA | IDF1 | EAIDs |
|---|---|---|---|---|---|
| YOLOv5 | DS-SIM | 50,406 | 58,372 | 76,864 | 11 |
| YOLOv5 | DS-INIA-1 | 55,310 | 43,424 | 71,141 | 205 |
| YOLOv5 | DS-INIA-2 | 52,981 | 51,114 | 70,341 | 172 |
| YOLOv8 | DS-SIM | 55,418 | 64,441 | 79,196 | 26 |
| YOLOv8 | DS-INIA-1 | 60,240 | 54,424 | 73,473 | 184 |
| YOLOv8 | DS-INIA-2 | 57,109 | 58,684 | 70,326 | 164 |

OCSort memberi HOTA dan MOTA tertinggi pada semua kasus, StrongSort memberi EAIDs terendah, dan IDF1 terbaik berpindah antara keduanya. Waktu OCSort dan ByteTrack berada pada orde 30 ms, sedangkan StrongSort 3 sampai 4 kali lebih lambat.

Hitungan pada video tanpa label (Tabel IV, nilai sebenarnya 2.133 apel):

| Detektor | Pelacak | Pergi | Kembali | Jumlah | Rekaman penuh |
|---|---|---|---|---|---|
| YOLOv5 | OCSort | 2.932 | 2.789 | 5.721 | 5.782 |
| YOLOv5 | ByteTrack | 2.587 | 2.503 | 5.090 | 5.121 |
| YOLOv5 | StrongSort | 2.659 | 2.385 | 5.044 | 5.092 |
| YOLOv8 | OCSort | 2.621 | 2.569 | 5.190 | 5.259 |
| YOLOv8 | ByteTrack | 1.877 | 1.818 | 3.695 | 3.730 |
| YOLOv8 | StrongSort | 1.959 | 1.808 | 3.767 | 3.810 |

Penulis menyatakan hitungan jauh di atas nilai sebenarnya terutama karena apel pada baris belakang terdeteksi dengan keyakinan tinggi dan ukuran kotak yang kadang lebih besar daripada apel baris utama, sehingga penyaringan berdasarkan keyakinan atau ukuran tidak efektif. Upaya penghapusan latar (alat penghapus latar, panorama dari video, kamera stereo ZED 2) tidak memberi hasil memuaskan karena keterbatasan sumber daya.

Hasil koreksi hitungan (Tabel V; GT = hitungan sebenarnya, CA = koefisien pengali, Reg. = regresi linear, ER = galat relatif):

| Instansi | GT | Hasil CA | ER CA | Hasil Reg. | ER Reg. |
|---|---|---|---|---|---|
| V1_5 | 375 | 373 | 0,06 ± 0,04 | 366 | 0,04 ± 0,03 |
| V1_10 | 722 | 672 | 0,07 ± 0,03 | 491 | 0,32 ± 0,15 |
| V3_5 | 362 | 348 | 0,04 ± 0,02 | 354 | 0,02 ± 0,09 |
| DS-INIA-COMPLETO | 2.133 | 2.533 | 0,20 ± 0,19 | 1.261 | 0,45 ± 0,28 |

Regresi linear unggul bila jumlah pohon sama dengan data latih, sedangkan koefisien lebih stabil ketika jumlah pohon berubah.

## Kelebihan dan Keterbatasan
Kelebihan: perbandingan detektor dan pelacak dilakukan pada data yang sama dengan waktu komputasi dilaporkan; simulator menyediakan kebenaran dasar jumlah buah; koreksi hitungan dievaluasi pada kondisi data yang berbeda dari data kalibrasi.

Keterbatasan yang dinyatakan penulis: simulator mengabaikan banyak aspek dunia nyata dan tidak menggantikan validasi lapangan; jumlah apel yang tampak pada video lapangan tidak diketahui; deteksi apel baris belakang tidak berhasil dihilangkan; Faster R-CNN hanya dapat dilatih dengan jumlah *epoch* terbatas karena waktu latih; hasil koreksi tidak konsisten bila karakteristik data uji berbeda dari data latih; perbedaan varian YOLOv8n dan YOLOv5s dapat memengaruhi perbandingan.

Menurut pembacaan ringkasan ini, acuan hitungan lapangan (2.133 apel yang dipanen setelah perekaman) mencakup apel yang tidak terlihat pada video, sehingga galat tidak sepenuhnya dapat dipisahkan dari kegagalan deteksi atau pelacakan. Menurut pembacaan ringkasan ini, koefisien dan regresi dikalibrasi hanya pada simulasi, dan satu video nyata digunakan untuk pengujiannya, sehingga generalisasi ke kebun nyata belum dibuktikan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali melalui pelacakan antarbingkai (detektor dan MOT) pada video yang direkam dari kedua sisi barisan, ditambah koreksi statistik terhadap hitungan akhir. Penulis menyebut bahwa apel yang terlihat dari kedua sisi barisan dan yang tidak terlihat menghasilkan galat pelacakan, tetapi tidak ada mekanisme yang mencocokkan identitas buah lintas sisi barisan. Hasil pelacakan pergi dan kembali dijumlahkan (kolom "Jumlah"), sehingga apel yang terlihat dari kedua sisi dihitung ganda dan diatasi hanya oleh koreksi pengali atau regresi.

Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas (apel). Acuan hitung berupa jumlah apel yang dipanen pada barisan (2.133) untuk video lapangan, kebenaran dasar simulator untuk video simulasi, dan anotasi bingkai untuk metrik pelacakan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan koreksi hitungan dengan faktor kalibrasi dan peringatan tentang tandan latar yang terdeteksi dengan keyakinan tinggi. Pelacakan berbasis video tidak menyelesaikan identitas lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `garderes2024apple`.

Garderes dkk. membandingkan YOLOv5, YOLOv8, dan dua varian Faster R-CNN untuk deteksi apel, serta StrongSort, ByteTrack, dan OCSort untuk pelacakan pada video barisan kebun apel, dengan bantuan simulator ROS. YOLOv5 dan YOLOv8 unggul (AP50 uji 0,906 dan 0,904 pada set DS2), OCSort memberi HOTA tertinggi (60,24%) dengan waktu sekitar 30 ms, tetapi hitungan pada video penuh melebihi jumlah panen 2.133 karena apel baris belakang, dan koreksi koefisien menurunkan galat relatif menjadi 0,20 pada video nyata penuh.

Catatan verifikasi data: Angka AP50 per model ada pada Tabel I dan Tabel II, metrik pelacakan pada Tabel III, hitungan video penuh pada Tabel IV, dan hasil koreksi pada Tabel V; jumlah dan ukuran set data ada pada Bagian III-D. Abstrak melaporkan mAP50 0,87 dan 0,85 yang sesuai dengan nilai pada DS5 (0,865 dan 0,853). Pada Tabel III hasil ekstraksi teks, label set data berada di tengah blok baris sehingga pemetaan baris ke set data (DS-SIM, DS-INIA-1, DS-INIA-2) mengikuti urutan blok dan tidak sepenuhnya pasti; HOTA 60,24 yang dikutip abstrak tampak pada baris YOLOv8 dengan OCSort pada blok kedua. Tidak ada tabel yang melaporkan hitungan per kelas, dan tidak ada angka untuk apel yang benar-benar tampak pada video lapangan.
