# CB-YOLO-DeepSORT: Real-Time Yield Estimation for Tomatoes in Greenhouses

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xing2025cb` |
| Judul asli | CB-YOLO-DeepSORT: Real-Time Yield Estimation for Tomatoes in Greenhouses |
| Penulis | Xing, Yu; Hu, Huan; Zhang, Junning; Han, ZhenHao; Han, JinLong |
| Tahun | 2025 |
| Venue | 15th IEEE International Conference on Cyber Technology in Automation Control and Intelligent Systems Cyber 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [xing2025cb.pdf](../pdf/xing2025cb.pdf)
- DOI resmi: https://doi.org/10.1109/cyber67662.2025.11168194

## Gambaran Umum
Makalah prosiding (IEEE CYBER 2025, Shanghai) ini mengusulkan CB-YOLO-DeepSORT, yaitu detektor YOLOv5s yang ditambah modul atensi CBAM dan fungsi kerugian CIoU, digabungkan dengan pelacak pelacakan multi-objek (*multi-object tracking*, MOT) DeepSORT. Tujuannya adalah mengenali dua tingkat kematangan tomat (matang dan mentah) serta menghitung buah matang pada rekaman video di rumah kaca. Sistem ini dibungkus dalam platform inspeksi berbasis web dengan robot yang memakai ROS dan Jetson Xavier.

Dataset terdiri atas 2.116 citra asli dari dua rumah kaca di Tiongkok, yang diperluas menjadi 4.260 citra dengan 14.995 instans berlabel. Hasil utama yang dilaporkan: mAP@0,5 sebesar 99,5% pada detektor CB-YOLO, serta MOTA 87,5% (video berdensitas rendah, 8 buah) dan 80,9% (video 5, 89 buah). Pelacakan dievaluasi pada lima video dengan jumlah buah acuan 8 sampai 89.

Penghitungan didasarkan pada nilai ID terbesar yang diberikan pelacak pada satu video. Makalah tidak melaporkan galat hitungan mutlak terhadap jumlah acuan secara langsung, melainkan MOTA, MOTP, jumlah identitas tertukar, dan jumlah salah identifikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Inspeksi tomat rumah kaca masih mengandalkan tenaga manual yang tidak efisien, mahal, dan subjektif. Detektor berbasis YOLO sudah dipakai, tetapi penulis menyatakan masih ada persoalan pada deteksi objek kecil, oklusi dinamis, dan stabilitas klasifikasi kematangan. Tomat mentah berwarna hijau tua sangat mirip dengan dedaunan.

Penulis juga menilai penelitian pencacahan terdahulu (misalnya pelacak stroberi dan penghitung tomat berbasis YOLOv8) belum memadai untuk lingkungan rumah kaca yang kompleks dan belum menyediakan pemantauan jumlah buah dan estimasi hasil secara waktu-nyata. Selain itu, buah yang sama muncul di banyak bingkai video, sehingga pencacahan per bingkai tanpa penugasan identitas akan menghitung berulang.

## Ide Utama
Gagasannya adalah memisahkan dua masalah: (1) deteksi dan klasifikasi kematangan per bingkai diperkuat dengan atensi kanal dan spasial (CBAM) serta kerugian regresi kotak CIoU, dan (2) identitas buah antarbingkai dijaga oleh DeepSORT, yang memadukan filter Kalman dan pencocokan Hungaria dengan fitur tampilan. Setiap tomat matang yang terlacak diberi ID unik mulai dari 1, dan ID maksimum pada video dianggap sebagai jumlah total buah.

Selain itu, hasil deteksi dan jumlah dikirim ke dasbor web untuk menampilkan cuplikan harian dan tren kematangan mingguan.

## Cara Kerja Langkah demi Langkah
```
 Video rumah kaca -> CB-YOLO (per bingkai, 2 kelas)
                          |
                          v
        DeepSORT (Kalman + Hungaria + fitur tampilan)
                          |
                          v
        ID unik per tomat matang -> ID maksimum = jumlah buah
                          |
                          v
        ROS / Flask / SQLite -> dasbor web
```

### 1. Akuisisi data dan anotasi
Citra diambil di Jingpeng Smart Greenhouse (Institut Penelitian Mesin Pertanian, Distrik Tongzhou, Beijing) dan sebuah rumah kaca tomat di Rongcheng, Weihai, Provinsi Shandong. Terkumpul 2.116 citra sRGB beresolusi 4928×3264 dan 4032×3024 piksel, diambil pada berbagai kondisi cahaya, sudut pemotretan, arah pencahayaan, dan oklusi (buah, daun, batang). Kultivar, jumlah tanaman, dan jenis kamera tidak dilaporkan. Anotasi memakai LabelImg dengan kotak pembatas minimum. Buah yang terlihat parsial dianotasi hanya bila minimal 50% areanya tampak. Dua kelas: `ripe_tomatoes` (merah penuh dan keras) dan `unripe_tomatoes` (hijau tua dan keras).

### 2. Prapemrosesan dan augmentasi
Citra dipotong, dikompresi, dan diubah ukurannya menjadi 640×640 piksel dalam format JPEG. Dipakai pemerataan histogram adaptif, penyesuaian saturasi acak (±5%), penskalaan, pembalikan horizontal dan vertikal, rotasi ±90°, derau Gauss, kabur Gauss 0,5 piksel, dan transformasi multi-skala. Setelah itu dataset menjadi 4.260 citra berisi 14.995 instans, dibagi 80% latih, 10% uji, dan 10% validasi.

### 3. Detektor CB-YOLO
Model dasar adalah YOLOv5s. Modul CBAM (atensi kanal dengan pooling rerata dan maksimum, lalu atensi spasial dengan konvolusi 7×7) disisipkan setelah modul CSP1_X dan CSP2_1 pada *backbone*. Kerugian GIoU diganti CIoU, yang menambahkan jarak titik tengah dan konsistensi rasio aspek. Pelatihan: optimizer Adam, laju belajar maksimum 0,01 dengan *cosine annealing*, ukuran batch 16, 200 epoch, pada GPU RTX 3090 24 GB.

### 4. Pelacakan dan pencacahan
Detektor CB-YOLO dihubungkan dengan DeepSORT. Pelacak memakai filter Kalman untuk prediksi gerak dan algoritma Hungaria untuk pencocokan, dengan pencocokan bertingkat dan fitur tampilan untuk mengurangi pertukaran identitas saat oklusi panjang. Jumlah buah ditetapkan sebagai ID maksimum pada video.

### 5. Platform inspeksi
Perangkat keras robot memakai ROS Noetic pada Jetson Xavier (Ubuntu 20.04). Layanan *backend* memakai Flask dan SQLite yang berkomunikasi dengan ROS melalui rosbridge. Antarmuka memakai HTML5, JavaScript, dan roslibjs. Platform menampilkan jumlah tomat, sebaran kematangan, estimasi hasil harian, dan tren kematangan mingguan, serta memperkirakan jumlah buah yang matang dalam 7 hari melalui korelasi warna buah.

## Eksperimen dan Hasil
Detektor dievaluasi dengan presisi (P), recall (R), dan mAP@0,5. Studi ablasi (Tabel III):

| CBAM | CIoU | P (%) | R (%) | mAP@0,5 (%) |
|---|---|---|---|---|
| tidak | tidak | 98,4 | 96,4 | 99,3 |
| ya | tidak | 99,3 | 99,5 | 99,5 |
| tidak | ya | 98,8 | 97,0 | 99,3 |
| ya | ya | 99,8 | 99,5 | 99,5 |

Penulis menyatakan CBAM saja menaikkan presisi 0,9 poin, recall 3,1 poin, dan mAP@0,5 0,2 poin (selisih ini sesuai dengan Tabel III).

Hasil pelacakan dan pencacahan pada lima video (Tabel IV):

| Video | Jumlah acuan | Salah identifikasi | Tidak terdeteksi | IDS | MOTA (%) | MOTP (%) |
|---|---|---|---|---|---|---|
| 1 | 8 | 0 | 0 | 1 | 87,5 | 86,2 |
| 2 | 17 | 1 | 0 | 2 | 82,35 | 84,5 |
| 3 | 33 | 2 | 1 | 3 | 81,82 | 84,5 |
| 4 | 52 | 3 | 3 | 4 | 80,77 | 83,9 |
| 5 | 89 | 5 | 6 | 6 | 80,9 | 83,1 |

Penulis menafsirkan MOTA sekitar 82% pada skenario berdensitas sedang dan turun sedikit seiring bertambahnya jumlah tomat, kemungkinan akibat oklusi yang menyebabkan buah tak terdeteksi atau ID tertukar. Pemeriksaan sederhana pada baris video 2 (17 − 1 − 0 − 2 = 14, dibagi 17) menghasilkan 82,35%, sesuai dengan nilai tabel. Tidak ada pembanding pelacak lain, dan tidak ada galat hitungan akhir (hitungan ID maksimum terhadap acuan) yang dilaporkan terpisah.

## Kelebihan dan Keterbatasan
Kelebihan: pipeline lengkap dari deteksi, pelacakan, hingga platform robot dan dasbor; acuan jumlah dan metrik MOT dilaporkan per video; dataset mencakup variasi cahaya, sudut, dan oklusi. Keterbatasan yang dinyatakan penulis: MOTA menurun pada densitas tinggi akibat oklusi, serta deteksi dapat menghasilkan positif palsu atau luput pada latar kompleks dan cahaya yang bervariasi.

Menurut pembacaan ringkasan ini, terdapat sejumlah ketidakkonsistenan dan celah. Teks menyebut 9.858 instans `ripe_tomatoes` dan 5.137 `unripe_tomatoes`, sedangkan Tabel I menaruh 9.858 pada baris "Unripe" dan 5.137 pada "Ripe". Abstrak menyatakan CB-YOLO melampaui YOLOv5s sebesar 2,5 poin persentase, padahal Tabel III menunjukkan YOLOv5s dasar sudah 99,3% dan selisih mAP@0,5 hanya 0,2 poin. mAP yang mendekati 99,5% pada pembagian acak citra hasil augmentasi berpotensi menggelembung bila citra turunan dari citra yang sama jatuh pada subset berbeda; makalah tidak menjelaskan apakah pembagian dilakukan sebelum augmentasi. Hanya lima video, dan kondisi cahaya, jumlah tanaman, serta kecepatan kamera tidak dilaporkan. Pencacahan hanya untuk buah matang, sehingga tidak ada hitungan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat berulang pada bingkai video dengan mekanisme pelacakan-oleh-deteksi (*tracking-by-detection*) menggunakan DeepSORT. Identitas dijaga melalui prediksi gerak (Kalman) dan pencocokan tampilan, dan jumlah diambil dari ID terbesar. Hitungan tidak dilaporkan per kelas kematangan: hanya buah matang yang dihitung, meskipun detektornya membedakan dua kelas. Acuan hitung adalah jumlah buah per video yang disebut "ground truth"; apakah dihitung di lapangan atau dari anotasi video tidak dinyatakan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan penugasan ID dan penghitungan ID unik. Pada sawit, perpindahan antarsisi pohon tidak kontinu seperti video, sehingga pelacakan temporal tidak langsung berlaku. Ukuran kesalahan identitas (IDS, salah identifikasi, tidak terdeteksi) yang dilaporkan di sini dapat dipakai sebagai contoh pelaporan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `xing2025cb`.

Xing dkk. mengusulkan CB-YOLO-DeepSORT untuk estimasi hasil tomat rumah kaca, yang menggabungkan YOLOv5s berbantuan CBAM dan kerugian CIoU dengan pelacak DeepSORT. Pada dataset 4.260 citra (14.995 instans, dua kelas kematangan), detektor mencapai mAP@0,5 99,5%. Pada lima video dengan 8 sampai 89 buah acuan, MOTA berkisar 80,77% sampai 87,5% dan MOTP 83,1% sampai 86,2%.

Catatan verifikasi data: mAP@0,5, presisi, dan recall berasal dari Tabel III; MOTA, MOTP, IDS, dan jumlah acuan dari Tabel IV; ukuran dataset dan pembagiannya dari Seksi II-B dan Tabel I; hiperparameter dari Tabel II. Abstrak menyebut keunggulan 2,5 poin atas YOLOv5s yang tidak sesuai dengan Tabel III (selisih mAP@0,5 hanya 0,2 poin pada ablasi), dan label kelas pada Tabel I bertentangan dengan teks. Tidak dilaporkan: kultivar, jumlah tanaman, galat hitungan akhir per video, apakah pembagian data dilakukan sebelum augmentasi, serta rincian pembanding pelacak. Ekstraksi tabel dalam teks berupa deretan angka sehingga pemetaan kolom disimpulkan dari urutan baris.
