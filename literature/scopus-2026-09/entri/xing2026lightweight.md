# A lightweight multi-view detection and counting method for real-time cherry tomato yield estimation using greenhouse inspection robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xing2026lightweight` |
| Judul asli | A lightweight multi-view detection and counting method for real-time cherry tomato yield estimation using greenhouse inspection robots |
| Penulis | Xing, Xushuo; Gao, Jin; Deng, Xue; Wang, Shubo; Qi, Peng; Wang, Fangyan; Hou, Xiuning; Gao, Junfeng |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [xing2026lightweight.pdf](../pdf/xing2026lightweight.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102260

## Gambaran Umum
Makalah ini mengusulkan kerangka jaringan bertingkat ringan "deteksi-pelacakan-pencacahan-kompensasi" untuk mencacah tomat ceri (*cherry tomato*) pada robot inspeksi rumah kaca. Kerangka ini terdiri atas detektor ringan (varian YOLO dengan modul G-FConv, L-MFA, kepala deteksi asimetris terpisah LADH, dan atensi SimAM), pelacak Deep OC-SORT, serta metode kompensasi multi-pandang (*multi-view compensation*, MVC). Model dijalankan pada perangkat tepi NVIDIA Jetson Orin Nano dengan akselerasi TensorRT. Data berupa video yang direkam dengan kamera Intel RealSense D455 yang dipasang pada robot inspeksi di sebuah taman industri pertanian di Qingdao, Tiongkok, selama November 2024 sampai Maret 2025.

Hasil utamanya: detektor mencapai mAP@0,5 sebesar 90,8 % dengan ukuran 3,98 MB dan 5,3 GFLOPs, serta kecepatan 31,3 FPS pada Jetson Orin Nano. Pada pencacahan, galat absolut rerata (MAE) Deep OC-SORT sebesar 595,03 turun menjadi 26,11 dengan MVC, yang oleh penulis dinyatakan sebagai pengurangan galat 95,6 %. Abstrak dan kesimpulan menyebut ketepatan pencacahan 95,2 %, dan kesimpulan menyebut akurasi prediksi hasil 93 % pada validasi di lingkungan produksi nyata.

Hal penting untuk pembaca: MVC pada makalah ini tidak memakai beberapa kamera. MVC membagi setiap bingkai dari satu kamera menjadi subwilayah dan menggabungkan hasil hitung antarsubwilayah, sehingga istilah "multi-pandang" di sini bermakna pembagian ruang pada satu citra.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil tomat yang akurat diperlukan agar produksi selaras dengan kebutuhan pasar. Tomat tandan (*truss tomato*) di rumah kaca saling tumpang tindih dan menutupi, batas objek kabur, citra mengalami *motion blur* akibat gerak robot atau ayunan tandan, dan pose buah beragam. Metode tradisional berbasis ruang warna, tepi, atau HOG+SVM disebut peka terhadap pencahayaan dan lemah pada objek bertumpuk. Pelacakan multi-objek (MOT) berbasis "deteksi-ekstraksi fitur-asosiasi data" bergantung pada akurasi deteksi dan menimbulkan pertukaran identitas (*ID switch*) pada kondisi oklusi, sedangkan algoritma seperti OC-SORT dan Deep OC-SORT masih terbatas pada oklusi, deformasi, dan objek serupa. Penulis juga menyebut bahwa model pembelajaran mendalam yang besar sulit dipasang pada perangkat tepi, dan bahwa algoritma pencacahan yang dirancang khusus untuk skenario ini belum tersedia.

## Ide Utama
Gagasan pertama adalah memperkecil detektor agar dapat berjalan waktu-nyata pada robot, dengan konvolusi jarang berbasis PConv dan ekspansi linear ala Ghost, agregasi fitur multi-skala yang memakai blok CG (*context-guided*), kepala deteksi asimetris dengan kompresi kanal bertahap, dan atensi SimAM tanpa parameter tambahan.

Gagasan kedua adalah menangani pertukaran identitas dengan mengganti tuntutan kestabilan pelacakan jangka panjang menjadi kestabilan lokal. Setiap bingkai dibagi menjadi K subwilayah bersebelahan (tiga subwilayah dipakai). Penulis berargumen bahwa deformasi proyeksi objek hampir tidak berubah dalam lingkungan spasial terbatas (konsistensi penampilan lokal) dan bahwa objek yang tertutup pada satu subwilayah dapat terdeteksi pada subwilayah lain (redundansi komplementer multi-pandang). Hitungan akhir diperbaiki dengan informasi konteks antarsubwilayah.

## Cara Kerja Langkah demi Langkah

```
  [Video RealSense D455] -> [Detektor ringan: GhostConv, L-MFA, G-FConv,
     SPPF, LADH+SimAM] -> [Deep OC-SORT: ID per objek]
     -> [MVC: bagi bingkai jadi 3 subwilayah, hitung lokal, kompensasi
        lintas subwilayah] -> [Jumlah ut / rt] -> [TensorRT di Jetson]
```

### 1. Akuisisi data
Video direkam November 2024 sampai Maret 2025 di Kaisheng Haofeng (Laixi) Smart Agriculture Industrial Park, Qingdao, Provinsi Shandong. Tiap baris berisi dua jalur tanaman tomat yang tumbuh berlawanan arah. Kamera Intel RealSense D455 dipasang pada robot inspeksi pada jarak 400 sampai 600 mm dari tanaman; video berukuran 1280 x 720 pada 30 FPS. Cuaca semuanya cerah; pencahayaan normal sekitar 65 %, redup sekitar 25 %, dan terang sekitar 10 %. Sebagian video dipakai langsung sebagai data validasi deteksi. Sisanya diambil bingkai kuncinya dengan interval 60 FPS menghasilkan 1.792 citra yang dianotasi dengan Makesense AI dalam dua kelas, tomat matang "rt" (33.433 instans) dan mentah "ut" (17.940 instans). Pada buah yang tertutup, penganotasi menggambar kotak batas lengkap dengan menduga kontur dari bagian yang terlihat. Pembagian data adalah 7:2:1 untuk latih, validasi, dan uji. Penulis juga menyiapkan data pengujian pelacakan dengan label ID memakai DarkLabel; jumlah videonya tidak dinyatakan secara terpisah.

### 2. Detektor ringan
Tulang punggung memakai GhostConv, modul L-MFA (struktur *Cross-Stage Partial* dengan blok CG yang memiliki ekstraktor lokal 3 x 3 *depthwise*, ekstraktor konteks sekitar berdilasi 2, dan ekstraktor global), dua modul G-FConv bertumpuk (PConv 3 x 3 dengan kanal keluaran seperempat kanal masukan dan ekspansi Ghost rasio 2), serta SPPF yang menghasilkan peta fitur P3, P4, dan P5. Kepala LADH memakai tiga cabang terpisah, dan SimAM dipasang pada lapisan deteksi tertinggi. Pelatihan memakai masukan 640 x 640, ukuran *batch* 64, laju belajar awal 0,00672, momentum 0,86304, peluruhan bobot 0,00241, penghentian dini bila mAP tidak membaik selama 50 *epoch*, dan *transfer learning* pada data tomat buatan sendiri.

### 3. Pelacakan Deep OC-SORT
Deep OC-SORT memakai fitur penampilan (ReID) dari CNN terlatih, filter Kalman, koreksi gerak kamera (CMC), penampilan dinamis (DA), dan pembobotan adaptif (AW) antara jarak Mahalanobis dan jarak kosinus; asosiasi diselesaikan dengan algoritma Hungaria. Ambang keyakinan deteksi 0,5 dan ambang IoU 0,3.

### 4. Kompensasi multi-pandang (MVC)
Modul pemartisi spasial membuat K subwilayah bersebelahan. Tiap bingkai diproses jaringan bertingkat dan keluarannya diberi ID, lalu modul kompensasi lintas pandang memakai konteks antarsubwilayah untuk memperbaiki keputusan hitung. Menurut penulis, objek yang hilang sementara pada satu subwilayah dapat terdeteksi dan terhitung pada subwilayah bersebelahan, atau galat dikurangi lewat batasan logis pada batas wilayah. Pembanding adalah kompensasi pandang tunggal (*single-view compensation*, SVC) dan hitungan berbasis ID Deep OC-SORT. Rincian rumus kompensasi tidak diberikan dalam teks.

### 5. Penerapan pada perangkat tepi
Model diubah dari format ONNX ke mesin TensorRT dengan `trtexec`, lalu dijalankan pada Jetson Orin Nano. Penulis menyebut kalibrasi presisi bobot dan aktivasi, fusi lapisan dan tensor, serta eksekusi multi-aliran.

## Eksperimen dan Hasil
Hasil ablasi (Tabel 1) pada data validasi:

| Model | P (%) | Recall (%) | mAP50 (%) | mAP50-95 (%) | Ukuran (MB) | Parameter (juta) | GFLOPs |
|---|---|---|---|---|---|---|---|
| Model 0 (dasar) | 88,3 | 86,6 | 90,5 | 61,3 | 6,24 | 3,157200 | 8,9 |
| Model 5 (CG + G-FConv + LADH) | 86,8 | 85,8 | 90,3 | 59,1 | 3,98 | 1,939637 | 5,3 |
| Model 6 (ditambah SimAM) | 88,3 | 86,2 | 90,8 | 59,8 | 3,98 | 1,939637 | 5,3 |

Pembanding detektor (Tabel 2): SSD mAP@0,5 56,3 % (99,1 MB; 23,880 juta parameter; 30,5 GFLOPs), YOLOv8n 90,5 % (6,24 MB; 8,9 GFLOPs), MobileNet-YOLO 88,8 % (5,04 MB; 6,4 GFLOPs), YOLOv9t 91,2 % (4,43 MB; 8,5 GFLOPs), dan model usulan 90,8 % (3,98 MB; 5,3 GFLOPs). Dibandingkan dengan Model 0, parameter berkurang 38,9 % menurut teks, ukuran 36,2 %, dan GFLOPs 40,4 %. mAP50-95 Model 6 (59,8 %) lebih rendah daripada Model 0 (61,3 %), dan recall sedikit lebih rendah; penulis menyebut keduanya "relatif stabil".

Metrik pelacakan (Tabel 3): MOTA, HOTA, dan IDF1 rendah pada data uji pelacakan, yang oleh penulis dikaitkan dengan oklusi dan kemunculan ulang buah.

| Model | MOTA (%) | HOTA (%) | IDF1 (%) | DetA (%) |
|---|---|---|---|---|
| Dasar | -8,97 | 8,36 | 10,47 | 68,2 |
| Usulan | -8,77 | 8,56 | 11,05 | 71,5 |

Penulis menyimpulkan dari DetA yang jauh lebih tinggi daripada HOTA dan IDF1 bahwa hambatan utama ada pada asosiasi, bukan deteksi.

Pencacahan pada enam segmen video (Tabel 4; hitungan GT dan hitungan tiap metode):

| Segmen | GT | SVC | MVC | Deep OC-SORT |
|---|---|---|---|---|
| Seg 1 | 58 | 50 | 50 | 189 |
| Seg 2 | 105 | 96 | 102 | 559 |
| Seg 3 | 229 | 203 | 214 | 908 |
| Seg 4 | 288 | 251 | 251 | 1.034 |
| Seg 5 | 343 | 305 | 305 | 1.254 |
| Seg 6 | 417 | 387 | 395 | 1.067 |
| MAE | | 30,72 | 26,11 | 595,03 |
| RMSE | | 34,04 | 30,50 | 644,44 |

MVC menurunkan MAE dan RMSE dibandingkan SVC masing-masing sekitar 15 % dan 10 % menurut teks. Selisih 95,6 % dalam abstrak sesuai dengan MAE 595,03 menjadi 26,11 (pengecekan sederhana dari angka tabel). Terlihat bahwa kedua metode kompensasi menghasilkan hitungan di bawah GT pada keenam segmen.

Pengaruh laju bingkai (Tabel 5, tiga video, GT 464, 392, dan 436): MAE SVC adalah 80,33 (10 FPS), 63,67 (20 FPS), dan 59,67 (30 FPS); MAE MVC adalah 68, 51,33, dan 38,33. RMSE SVC adalah 88,3; 66,26; dan 63,47, sedangkan RMSE MVC adalah 70,69; 51,96; dan 38,41. Pada 30 FPS MVC menurunkan MAE 35,8 % dan RMSE 39,5 % relatif terhadap SVC.

Hitungan per kelas matang (Tabel 6, enam video): WMAE adalah 21,88 untuk SVC, 20,10 untuk MVC, dan 598,08 untuk Deep OC-SORT. Contohnya, pada Video 1 GT adalah 118 "ut" dan 206 "rt", sedangkan hitungan MVC adalah 93 dan 184, dan hitungan Deep OC-SORT adalah 588 dan 708. Pada uji iluminasi buatan (50 % sampai 150 %, dua rangkaian video), MVC disebut lebih baik daripada SVC pada kondisi terang dan terlalu terang; angkanya hanya disajikan dalam diagram radar (Gambar 13). Regresi hitungan prediksi terhadap hitung manual per petak di rumah kaca nyata memberi R2 = 0,99 dengan persamaan Y = 0,926X - 6,1605 (Gambar 14).

## Kelebihan dan Keterbatasan
Kelebihan: kerangka ini menyatukan detektor ringan, pelacak, dan koreksi hitungan yang dapat berjalan pada robot (31,3 FPS pada Jetson Orin Nano); hitungan dilaporkan per kelas kematangan (matang dan mentah); analisis memasukkan pengaruh laju bingkai dan pencahayaan; dan hitungan Deep OC-SORT yang berlebih (ID berulang) ditunjukkan secara terbuka.

Keterbatasan yang dinyatakan penulis: dataset perlu diperluas ke skenario lingkungan yang lebih kompleks; desain ringan mengorbankan sensitivitas pada objek yang sangat kecil atau sangat buram di jarak jauh; pertukaran identitas akibat oklusi dan pergeseran posisi akibat gerak kamera masih perlu diperbaiki; MVC memakai partisi wilayah tetap sehingga kurang luwes bila robot bergerak tidak seragam atau bergetar kuat; galat kumulatif pada baris tanam yang sangat panjang masih menjadi hambatan; dan penulis menyarankan penggabungan data IMU dengan odometri visual. Data tidak dapat dibagikan karena penulis tidak memiliki izin.

Menurut pembacaan ringkasan ini, ada keterbatasan lain. Pertama, kompensasi MVC tidak dijelaskan secara rinci dalam teks (tidak ada algoritma atau rumus eksplisit, hanya prinsip dan diagram), sehingga sulit direproduksi. Kedua, kedua metode kompensasi menghasilkan hitungan di bawah GT pada semua segmen Tabel 4, sehingga koreksi tampak menekan hitungan berlebih tetapi tidak menutup kekurangan hitung; MI dan "FP" pada Tabel 4 tidak didefinisikan dengan jelas selain keterangan FP = MI / GT. Ketiga, MVC berasal dari pembagian satu citra menjadi tiga subwilayah sehingga bukan identitas lintas kamera atau lintas sisi tanaman, dan penerapannya mengandalkan jalur gerak robot yang teratur pada barisan tanam. Keempat, penjelasan angka tidak sepenuhnya konsisten: abstrak menyebut ketepatan hitung 95,2 % dan kesimpulan menyebut akurasi prediksi hasil 93 %, tetapi teks hasil tidak memuat tabel yang menurunkan kedua angka itu secara langsung. Kelima, MOTA bernilai negatif sehingga metrik pelacakan standar tidak mendukung kualitas pelacakan, dan jumlah video uji pelacakan (enam segmen, tiga video pada uji laju bingkai) kecil.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan dua mekanisme yang digabung: pelacakan multi-objek berbasis deteksi dan ID (Deep OC-SORT) serta koreksi hitungan berbasis subwilayah (MVC) pada satu kamera yang bergerak menyusuri baris tanam. Buah yang terlihat ulang akibat pertukaran identitas ditangani dengan mempersempit kebutuhan kestabilan ID menjadi lokal dan menggabungkan hitungan antarsubwilayah. Tidak ada pencocokan identitas buah antarkamera atau antarsisi tanaman, dan teks menyatakan bahwa metode ini bekerja pada aliran video 2D dari satu kamera tanpa rekonstruksi 3D.

Hitungan dilaporkan per kelas kematangan (matang "rt" dan mentah "ut") pada Tabel 6, dengan WMAE sebagai ukuran gabungan. Acuan hitungnya adalah hitung manual pada video (GT) dan hitung manual per petak untuk regresi di rumah kaca; hasil panen tidak dipakai. Hal yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pelaporan hitungan per kelas dengan WMAE, pemisahan hambatan asosiasi dari deteksi lewat perbandingan DetA dengan HOTA dan IDF1, serta pengamatan bahwa hitungan berbasis ID tunggal dapat melebihi GT berkali-kali lipat pada adegan padat. Kompensasi subwilayah itu sendiri belum menjawab identitas lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `xing2026lightweight`.

Xing dkk. (2026) mengusulkan kerangka bertingkat ringan "deteksi-pelacakan-pencacahan-kompensasi" untuk mencacah tomat ceri pada robot inspeksi rumah kaca. Detektor ringan mencapai mAP@0,5 90,8 % dengan 3,98 MB dan 5,3 GFLOPs (31,3 FPS pada Jetson Orin Nano). Metode kompensasi multi-pandang, yang membagi tiap bingkai satu kamera menjadi subwilayah dan menggabungkan hitungannya, menurunkan MAE hitungan dari 595,03 (Deep OC-SORT) menjadi 26,11 pada enam segmen video, dengan hitungan dilaporkan per kelas matang dan mentah.

Catatan verifikasi data: Hasil ablasi dan pembanding detektor berasal dari Tabel 1 dan Tabel 2; metrik pelacakan dari Tabel 3; hitungan enam segmen, MAE, dan RMSE dari Tabel 4; pengaruh laju bingkai dari Tabel 5; hitungan per kelas dan WMAE dari Tabel 6; regresi R2 = 0,99 dari seksi 4.5 dan Gambar 14; 31,3 FPS dan ketepatan 95,2 % dari kesimpulan. Teks ekstraksi memuat tabel sebagai sel terpisah sehingga pemetaan kolom Tabel 4 (Count, MI, FP) dibaca dari urutan sel; kolom Count pada Tabel 4 dibaca sebagai hitungan akhir tiap metode, sedangkan makna kolom MI (diduga hitungan salah identifikasi) diambil dari catatan tabel. Pada Tabel 5, nilai MAE dan RMSE per kondisi laju bingkai tercantum pada baris judul, dan nilai per video hanya Count, MI, dan FP. Angka 95,2 % (ketepatan hitung) dan 93 % (akurasi prediksi hasil) tidak dapat ditelusuri ke tabel tertentu dalam teks. Parameter model pada teks tertulis 1,93 juta (seksi 4.3), 1,94 juta (Tabel 2 dalam teks), dan 1,939637 juta (Tabel 1). Angka diagram radar (Gambar 13) dan jumlah video pengujian pelacakan tidak tersedia. Jumlah petak untuk regresi Gambar 14 dan rincian kompensasi MVC tidak dilaporkan.
