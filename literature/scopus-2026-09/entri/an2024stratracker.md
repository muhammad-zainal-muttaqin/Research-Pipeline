# StraTracker: A dynamic counting method for growing strawberries based on multi-target tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `an2024stratracker` |
| Judul asli | StraTracker: A dynamic counting method for growing strawberries based on multi-target tracking |
| Penulis | An, Qilin; Cui, Yongzhi; Tong, Wenyu; Liu, Yangchun; Zhao, Bo; Wei, Liguo |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [an2024stratracker.pdf](../pdf/an2024stratracker.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109564

## Gambaran Umum
Makalah ini (An dkk., *Computers and Electronics in Agriculture* 227, 2024, 109564) mengusulkan StraTracker, algoritme pelacakan multi-objek (*multi-object tracking*, MOT) untuk mengenali dan menghitung stroberi pada lima tahap pertumbuhan dari video yang direkam oleh platform bergerak di rumah kaca. Penghitungan diubah menjadi masalah pelacakan bingkai demi bingkai: setiap buah memperoleh identitas (ID) dan dihitung menurut ID dan tahap pertumbuhannya. Sistem terdiri atas detektor YOLOv8n, modul asosiasi fitur berbasis BoT-SORT yang ditambah modul *Feature Slicing Attention* (FSA) dan *Adaptive Kalman Filtering* (AKF), serta modul penghitungan dua area (*dual-area counting*, DC).

Data berupa set StraMOT yang dikumpulkan sendiri oleh penulis di rumah kaca Academy of Agricultural Sciences, Weifang, Provinsi Shandong, Tiongkok, pada kultivar stroberi 'Rouge', 'Suizhu', dan 'Zhangji'. Lima kelas adalah pembungaan, hijau, putih, mulai berwarna, dan matang.

Hasil utama yang dilaporkan: detektor mencapai AP rerata 91,93% pada 38,3 FPS; StraTracker mencapai MOTA 83,28%, HOTA 77,26%, MOTP 81,35% dengan 259 pergantian ID (IDs), lebih baik daripada enam pelacak pembanding yang diuji; dan penghitungan dengan metode DC mencapai akurasi 90,43%, GEH 2,33, dan R² 0,91 terhadap hitungan manual pada 44 video.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Stroberi terus berbunga dan berbuah sepanjang siklus tumbuh sehingga buah pada tahap berbeda muncul bersamaan. Pemantauan manual atau dengan instrumen khusus dinilai mahal dan merusak buah. Penghitungan berbasis detektor pada citra statis tidak cukup untuk menghitung buah pada seluruh kebun, sehingga penulis menggunakan MOT untuk mengasosiasikan buah lintas bingkai. Penelitian terdahulu yang disebut penulis (bunga kamelia, kacang tanah, apel) menangani buah yang matang pada periode yang sama dan tidak memantau seluruh siklus pertumbuhan.

Tantangan khusus yang diidentifikasi pada BoT-SORT: ukuran buah yang kecil dan bervariasi, bayangan yang saling menutupi dan gangguan cahaya, kotak pelacak yang tidak sesuai dengan buah, serta pergantian ID yang menggelembungkan hitungan akibat ID ganda untuk buah yang sama.

## Ide Utama
Gagasan utamanya adalah membuat hitungan bergantung pada ID pelacakan yang stabil dan pada penentuan tahap pertumbuhan di titik tertentu pada lintasan, bukan menghitung semua ID yang pernah muncul. Karena itu pelacak diperbaiki agar kotak dan ID lebih stabil (FSA untuk fitur penampilan buah kecil, AKF untuk filter Kalman yang beradaptasi), dan penghitungan memakai dua area penilaian: area pertama menyaring ID berdasarkan keyakinan deteksi, sedangkan area kedua menetapkan tahap pertumbuhan dan menaikkan hitungan untuk ID yang sudah tercatat di area pertama.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Platform pemantau beroda dengan motor hub bergerak melintasi guludan pada kecepatan 3,7 km/jam. Data direkam antara November 2021 sampai April 2022 dan Oktober 2022 sampai Maret 2023 di rumah kaca, dengan pengambilan di beberapa kebun tiap dua minggu pada cuaca dan cahaya berbeda. Video disimpan dengan resolusi 1920 × 1080 pada 60 fps format MP4 dan dianotasi dengan CVAT (kotak pembatas, ID lintasan, kelas, rasio keterlihatan).

Lima tahap pertumbuhan: MATURE (warna keseluruhan 70% atau lebih merah), NEARLY_M (sebagian berwarna, area warna sampai 70%), GROWING_W (hijau berubah menjadi putih muda), GROWING_G (buah hijau kecil), dan FLOWERING (bunga). Berdasarkan Tabel 2, set lengkap berisi 57 video dengan panjang rerata 10,46 menit dan 35.792 bingkai asli; subset latih 13 video dengan 4.103 bingkai dan 27.741 kotak; subset uji 1.095 bingkai dan 7.404 kotak; set uji penghitungan 44 video dengan 30.594 bingkai. Teks lain menyebut 35.145 target teranotasi (MATURE 6.373, NEARLY_M 7.271, GROWING_W 8.923, GROWING_G 6.941, FLOWERING 5.637) dan 5.198 bingkai valid hasil pemotongan setiap 60 bingkai. Augmentasi (RandAugment, buram gerak, pergantian latar dengan AI) menaikkan bingkai latih menjadi 16.412 (110.964 kotak) dan uji menjadi 4.380 (29.616 kotak) pada Tabel 2; teks menyebut 20.792 data valid setelah augmentasi.

### 2. Detektor
YOLOv8n dipilih setelah dibandingkan dengan Fast-RCNN, RetinaNet, NanoDet, YOLOv5s, dan YOLOv7-tiny pada StraMOT, berdasarkan keseimbangan akurasi dan kecepatan (3,2 juta parameter).

### 3. Asosiasi fitur (berbasis BoT-SORT)
Deteksi dipisah menjadi skor tinggi dan skor rendah menurut ambang τ. Deteksi skor tinggi diproses modul FSA yang membagi fitur buah menjadi *patch* dan memakai atensi Query-Key-Value sebelum jaringan ekstraksi fitur penampilan (NFNet). Lintasan diprediksi dengan kompensasi gerak kamera dan AKF. Asosiasi pertama memakai gabungan IoU dan jarak ReID; asosiasi kedua memakai IoU saja untuk sisa deteksi dan lintasan; lintasan dan deteksi yang tidak cocok dibuang; lintasan baru dibuat untuk deteksi sisa dengan skor di atas η. AKF mendefinisikan ulang vektor keadaan filter Kalman untuk mengestimasi langsung lebar dan tinggi kotak, dan menyesuaikan derau pengukuran R(k) secara adaptif dengan faktor pelupa b antara 0,95 dan 0,99.

### 4. Penghitungan
Empat metode dibandingkan: penghitungan berbasis ID (IC), garis hitung (LC), area (AC), dan dua area (DC). DC memeriksa keyakinan saat kotak melewati area pertama dan menyimpan ID-nya, lalu saat kotak melewati area kedua menilai tahap pertumbuhan dan menambah hitungan kelas itu bila ID ada pada daftar area pertama. Rentang hitung paling efektif disebut antara 1/5 dan 1/10 dengan keseimbangan terbaik pada 1/8 (teks tidak menjelaskan satuan rentang ini).

```
 Video --> YOLOv8n --> deteksi (skor tinggi / rendah)
                          |
              FSA (fitur) + AKF (gerak) + CMC
                          |
        asosiasi 1 (IoU+ReID) --> asosiasi 2 (IoU) --> lintasan beri ID
                          |
   area 1: simpan ID dengan keyakinan > tau --> area 2: tentukan tahap
                          |
                 hitungan per tahap pertumbuhan
```

## Eksperimen dan Hasil
Perangkat latih: GPU NVIDIA RTX 3090; pengujian lapangan pada mini komputer dengan RTX 2060. Pelacak pembanding dilatih 100 *epoch* pada StraMOT dengan bobot praterlatih MOT17. Tabel 3 membandingkan detektor (AP per kelas, FPS, parameter); YOLOv8n memperoleh AP 93,74 (MATURE), 90,31 (NEARLY_M), 91,63 (GROWING_W), 92,35 (GROWING_G), dan 91,64 (FLOWERING) pada 38,3 FPS dengan 3,2 juta parameter.

Tabel 5 membandingkan pelacak (MOTA, MOTP, HOTA dalam persen; IDs; FPS):

| Pelacak | MOTA | MOTP | HOTA | IDs | FPS |
|---|---|---|---|---|---|
| SORT | 63,32 | 66,61 | 55,85 | 682 | 9,3 |
| DeepSORT | 70,44 | 77,69 | 58,36 | 514 | 18,2 |
| ByteTrack | 77,83 | 79,56 | 68,72 | 361 | 38,6 |
| OCSORT | 76,18 | 78,41 | 73,16 | 397 | 43,5 |
| BoT-SORT | 78,52 | 80,52 | 74,39 | 330 | 32,7 |
| StrongSort | 81,69 | 79,05 | 73,83 | 318 | 30,9 |
| BoT-SORT (YOLOv8) | 80,57 | 80,81 | 74,89 | 305 | 34,2 |
| StraTracker | 83,28 | 81,35 | 77,26 | 259 | 38,3 |

Ablasi (Tabel 4) dari BoT-SORT: dengan augmentasi data MOTA 78,83 dan IDs 321; dengan YOLOv8 dan AKF MOTA 81,01 dan IDs 294; dengan FSA tambahan MOTA 82,72 dan IDs 267; dan model lengkap MOTA 83,28, MOTP 81,35, HOTA 77,26, IDs 259, 38,3 FPS. Selisih total terhadap BoT-SORT dasar: MOTA naik 4,76 poin, HOTA 2,87 poin, MOTP 0,83 poin (teks menyebut peningkatan "HOTA 0,83% dan MOTP 2,87%", sedangkan selisih pada Tabel 4 adalah HOTA 77,26 - 74,39 = 2,87 dan MOTP 81,35 - 80,52 = 0,83; selisih ini dihitung oleh ringkasan ini, sehingga label pada teks tampak tertukar).

Perbandingan metode penghitungan (Tabel 6, 44 video, acuan hitungan manual):

| Metode | Akurasi (%) | GEH | R² | FPS |
|---|---|---|---|---|
| IC | 80,64 | 4,85 | 0,68 | 43,9 |
| LC | 83,15 | 4,19 | 0,76 | 41,3 |
| AC | 87,72 | 3,02 | 0,87 | 41,7 |
| DC | 90,43 | 2,33 | 0,91 | 38,3 |

Regresi DC: Y = 0,9841X - 0,4501 (R² 0,91). Teks narasi menyebut akurasi LC 87,72% dan AC 83,15%, yang bertukar terhadap baris pada Tabel 6.

Kondisi pencahayaan dan sudut kamera (Tabel 7; hitungan acuan dan hitungan StraTracker, akurasi, GEH): cahaya matahari 0°: 249 dan 234, 93,97%, 0,96; 30°: 192 dan 176, 91,61%, 1,25; 45°: 261 dan 287, 90,03%, 1,36. Cahaya belakang 0°: 394 dan 339, 86,04%, 2,87; 30°: 458 dan 393, 85,81%, 3,15; 45°: 352 dan 394, 83,90%, 3,52. Cahaya terhalang 0°: 315 dan 291, 92,38%, 1,37; 30°: 157 dan 134, 85,35%, 3,71; baris 45° (216 acuan dan 238 prediksi) terpotong pada ekstraksi sehingga akurasi dan GEH tidak terbaca. Pada 45° model menghitung lebih banyak daripada acuan karena mendeteksi buah di baris sebelah. Penulis menyarankan sudut kamera antara 0° dan 30°.

Uji lapangan (Desember 2022 sampai Januari 2023, empat guludan sekitar 100 m) menghasilkan peta sebaran tahap pertumbuhan; misalnya tahap putih mencapai maksimum 33,84% dan tahap matang 6,79% pada pengamatan awal, dan tahap matang mencapai 30,64% pada 10 Januari.

## Kelebihan dan Keterbatasan
Kelebihan: kerangka MOT yang menghitung per tahap pertumbuhan dan memetakan sebaran buah di kebun; ablasi yang memisahkan kontribusi detektor, AKF, FSA, dan augmentasi; perbandingan dengan enam pelacak populer pada data yang sama; dan analisis terhadap kondisi cahaya dan sudut kamera.

Keterbatasan yang dinyatakan penulis: kesesuaian lingkungan dan akurasi hitungan masih perlu ditingkatkan; pengaruh berbagai faktor terhadap akurasi perlu diteliti lebih jauh; pencahayaan berlawanan menurunkan akurasi; metode DC menurunkan FPS; metode IC menghitung seluruh ID termasuk ID ganda dan deteksi palsu sehingga hitungan melebihi nilai sebenarnya. Pekerjaan lanjutan mencakup validasi pada tanaman lain, peningkatan platform, dan skema penghitungan.

Menurut pembacaan ringkasan ini, keterbatasan lain adalah: satu rumah kaca di satu lokasi sehingga generalisasi tidak teruji; akurasi hitungan DC (90,43%) bergantung pada penempatan dua area dan pada platform yang bergerak lurus di sepanjang guludan, sedangkan teks tidak melaporkan analisis kepekaan terhadap letak area; ada ketidakkonsistenan antara narasi dan tabel (Tabel 6 dan selisih ablasi); angka pada set data (35.792 vs 35.145 anotasi; 20.792 vs 56.584 bingkai) tidak seluruhnya sejalan; dan evaluasi pencacahan hanya memakai hitungan manual pada video, bukan hitungan panen.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan mekanisme pelacakan multi-objek dari satu video yang bergerak: ID unik diberikan dan dipertahankan antarbingkai oleh asosiasi gerak dan penampilan (IoU, ReID, filter Kalman), kemudian hitungan diambil pada dua area, bukan dari jumlah ID. Hitungan dilaporkan per tahap pertumbuhan (lima kelas) pada keluaran dan peta kebun, tetapi evaluasi akurasi pada Tabel 6 dan Tabel 7 dinyatakan sebagai hitungan total; penulis tidak melaporkan akurasi hitungan per kelas secara terpisah. Acuan hitungan adalah hitungan manual pada 44 video uji (Bagian 4.4.1); teks tidak menyebut hitungan panen. Pelacakan hanya antarbingkai satu video berurutan, tidak antarsisi.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: pemisahan "ID stabil" dan "hitungan pada titik keputusan" sehingga ID ganda tidak langsung menaikkan hitungan, penggunaan penilaian keyakinan dan tahap kelas pada satu titik per lintasan, serta temuan bahwa sudut pandang miring (45°) meningkatkan hitungan berlebih akibat buah dari baris di sebelahnya. Mekanisme ini tidak menangani pencocokan antarsisi pohon atau antarcitra tak berurutan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `an2024stratracker`.

An dkk. mengusulkan StraTracker, pelacak multi-objek berbasis BoT-SORT dengan detektor YOLOv8n, modul FSA, modul AKF, dan penghitungan dua area (DC) untuk menghitung stroberi pada lima tahap pertumbuhan dari video platform bergerak di rumah kaca. Pada set data StraMOT buatan sendiri, StraTracker mencapai MOTA 83,28%, HOTA 77,26%, dan 259 pergantian ID; penghitungan DC mencapai akurasi 90,43% dan R² 0,91 terhadap hitungan manual pada 44 video, dengan akurasi lebih rendah pada cahaya belakang.

Catatan verifikasi data: angka detektor dari Tabel 3 dan Bagian 4.2 (AP rerata 91,93% sesuai abstrak; teks bagian 4.2 juga menyebut "mAP 93,74% untuk buah matang", yang merupakan AP kelas MATURE pada Tabel 3); ablasi dari Tabel 4; perbandingan pelacak dari Tabel 5; perbandingan penghitungan dari Tabel 6 dan Bagian 4.4.1; kondisi cahaya dan sudut dari Tabel 7 (baris terakhir terpotong pada ekstraksi); statistik data dari Tabel 2 dan Bagian 2. Ada ketidakkonsistenan antara narasi dan tabel (nilai LC dan AC pada Tabel 6 versus narasi; label HOTA dan MOTP pada narasi ablasi), dan jumlah bingkai pada Tabel 2 berbeda dari angka pada teks. Jumlah pohon atau tanaman dan jumlah buah total tidak dilaporkan. Gambar tidak terbaca dari ekstraksi teks.
