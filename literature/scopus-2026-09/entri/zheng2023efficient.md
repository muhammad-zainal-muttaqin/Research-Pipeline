# An efficient online citrus counting system for large-scale unstructured orchards based on the unmanned aerial vehicle

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2023efficient` |
| Judul asli | An efficient online citrus counting system for large-scale unstructured orchards based on the unmanned aerial vehicle |
| Penulis | Zheng, Zhenhui; Xiong, Juntao; Wang, Xiao; Li, Zexing; Huang, Qiyin; Chen, Haoran; Han, Yonglin |
| Tahun | 2023 |
| Venue | Journal of Field Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zheng2023efficient.pdf](../pdf/zheng2023efficient.pdf)
- DOI resmi: https://doi.org/10.1002/rob.22147

## Gambaran Umum

Makalah ini mengusulkan sistem pencacahan buah jeruk daring (*online*) dan *end-to-end* dari video pesawat nirawak (*unmanned aerial vehicle*, UAV) di kebun luas yang tidak terstruktur. Sistem terdiri dari platform siaran langsung video UAV (Nginx-rtmp-module dan aplikasi Android Fly4Citrus), jaringan deteksi Citrus-YOLO (modifikasi YOLOv5), pelacakan DeepSORT, dan pencacah baru bernama *nonuniform distributed counter* (NUDC) yang mengoreksi hitungan ketika pelacakan gagal. Objek penelitian adalah jeruk Emperor (*Emperor citrus*) di Zengcheng dan jeruk oranye (*orange*) di Baiyun, keduanya di Guangzhou, Tiongkok.

Data berupa 50 video UAV (30 dari kebun jeruk Emperor pada Oktober 2021 dan 20 dari kebun oranye pada April 2022), masing-masing memuat 5 sampai 10 pohon dan 300 sampai 600 buah, dibagi menjadi 35 video latih dan validasi serta 15 video uji. Pada skenario lapangan dengan pencahayaan sesuai, F1 deteksi 89,07% dan MAPE hitungan 12,75%. Pada pengujian luring, F1 deteksi Citrus-YOLO rerata 94,51% dan MAPE 5,28%. Mode daring menambah penundaan 8 sampai 15 detik dan kehilangan paket 3,4%, dengan MAPE 14,95%.

Penulis menyatakan bahwa hanya buah pada satu sisi pohon yang dihitung, dan pencacahan multi-pandang dengan beberapa UAV disebut sebagai pekerjaan lanjutan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil kebun sebelum panen biasanya dilakukan berdasarkan pengalaman petani, hitung manual, dan data historis, sehingga lambat, mahal, subjektif, dan sulit akurat pada kebun dengan variabilitas spasial tinggi. Metode otomatis terdahulu memotret pohon dari satu atau dua sisi lalu menghitung secara luring, atau memakai rekonstruksi 3D (*structure from motion*, SfM, dan *simultaneous localization and mapping*, SLAM) yang memerlukan peralatan mahal dan, menurut makalah, dapat memakan lebih dari 10 jam untuk memproses informasi 3D.

Penulis menilai bahwa penelitian terdahulu berfokus pada algoritma dan mengabaikan penyaluran data antara sensor dan pemroses, sehingga sistem *end-to-end* belum ada. Tiga alasan kebutuhan sistem daring dikemukakan: penyetelan lapangan (kecepatan terbang, jarak kamera, ketinggian), ketepatan waktu (jeruk dipanen sekitar 30 sampai 50 hari setelah matang), dan perluasan ke banyak UAV. Dari sudut pandang UAV, jeruk berukuran kecil, rapat, saling menutupi, dan tertutup daun, sehingga deteksi dan pelacakan sulit. Penggunaan ID maksimum sebagai hitungan menghasilkan penghitungan ganda yang besar; pada contoh di makalah ID maksimum mencapai 1.274 sedangkan acuan 318.

## Ide Utama

Gagasan utamanya adalah memperlakukan identitas buah lintas bingkai sebagai masalah pelacakan dalam aliran video, lalu mengoreksi galat pelacakan pada tahap penghitungan, bukan hanya pada tahap pelacakan. Pelacakan DeepSORT memberi ID pada tiap buah. Untuk menghindari penghitungan ganda akibat pergantian ID dan kegagalan pelacakan, NUDC menempatkan beberapa garis hitung pada citra dengan kepadatan tidak seragam.

Alasan perancangannya adalah buah di tengah citra relatif jelas dan besar sehingga mudah dilacak stabil, sedangkan buah di sisi kiri dan kanan lebih jauh dari kamera, buram, dan sering berganti ID. Garis hitung dibuat rapat di tengah dan menjarang ke sisi. Satu garis hitung tunggal (*single line counter*, SLC) menghindari penghitungan ganda tetapi terlalu banyak melewatkan buah ketika deteksi gagal pada bingkai kunci.

## Cara Kerja Langkah demi Langkah

```
  [ UAV + DJI GO 4 / Fly4Citrus ] --RTMP--> [ Server Nginx ] --HLS--> [ PC ]
                                                                        |
        [ Citrus-YOLO ] --> [ DeepSORT (Kalman + Hungarian) ] --> [ NUDC ]
        (deteksi)            (ID lintas bingkai)                  (hitungan)
```

### 1. Perangkat keras dan akuisisi data

UAV adalah DJI Phantom 4 Pro v2 dan Phantom 4 Advanced. Komputer pengolah memakai NVIDIA GeForce RTX 3060 (11,0 GB memori) dengan Ubuntu 18.04. Video berdurasi 2 sampai 5 menit dengan sekitar 2.500 bingkai per video, dan laju bingkai UAV 24 bingkai/detik. Ground truth diperoleh dengan melabeli video memakai DarkLabel. Dari video latih diekstrak 12.640 citra latih. Dua kebun diuji dengan total 88 pohon (52 dan 36 pohon menurut Tabel 3).

### 2. Platform siaran langsung UAV

Aplikasi DJI GO 4 di ponsel mendorong aliran video melalui protokol RTMP ke server Nginx-rtmp-module. Komputer pengolah menarik aliran melalui HLS. Aplikasi Fly4Citrus dikembangkan dari Mobile SDK DJI untuk mengatur ISO, sumber video, dan penerbangan otonom dengan jarak, ketinggian, kecepatan, dan arah yang ditetapkan, menggantikan kendali manual.

### 3. Deteksi dengan Citrus-YOLO

Citrus-YOLO memodifikasi YOLOv5 dengan mengganti PANet menjadi BiFPN pada jaringan fusi fitur dan menambahkan satu kepala deteksi objek kecil. Pelatihan memakai bobot awal YOLOv5_l6, citra 1.280 × 1.280, *batch* 32, laju belajar awal 0,01, momentum 0,937, peluruhan bobot 0,0005, selama 100 epoch dengan augmentasi *mosaic* dan *flip*. Untuk inferensi, citra diubah menjadi 640 × 640 dan model dipercepat dengan TensorRT.

### 4. Pelacakan antarbingkai

Pelacak memakai filter Kalman dengan model gerak seragam dan algoritma Hungarian. Asosiasi memakai pencocokan bertingkat (*cascade matching*) berdasarkan jarak Mahalanobis (ambang 9,4877) dan jarak kosinus fitur penampilan dari jaringan residual (100 vektor fitur terakhir per jejak), digabung secara linear dengan bobot $\lambda$, lalu pencocokan IoU untuk sisa deteksi dan jejak. Penambahan fitur penampilan dimaksudkan mengurangi pergantian ID saat kamera bergoyang akibat angin atau pengendalian UAV.

### 5. Strategi penghitungan NUDC

NUDC terdiri dari dua *counter_a* (menghitung buah di batas citra), dua *counter_b* (rentang kerja kecil di kedua sisi, menghitung buah yang jelas dan mengurangi hitungan buah yang gagal dilacak), dan satu *counter_c* (menghitung sebagian besar buah di tengah). Posisi dan lebar tepat tiap penghitung tidak dirinci dalam teks yang tersedia.

## Eksperimen dan Hasil

Pembanding deteksi adalah YOLOX dan YOLOv5, dan pembanding penghitungan adalah ByteTrack dan YOLOv5 + DeepSORT yang masing-masing diberi NUDC. Metrik deteksi dihitung pada seluruh aliran video, bukan per bingkai. Metrik hitungan: IDSR (tingkat pergantian ID), rasio hitungan terhadap acuan, L1 loss, dan rerata galat; pada ablasi dipakai MAPE dan MAE atas 15 video uji.

### Deteksi (rerata, Tabel 1)

| Metode | Presisi (%) | *Recall* (%) | F1 (%) | FPS |
|---|---|---|---|---|
| YOLOX | 92,84 | 82,67 | 86,63 | 8,33 |
| YOLOv5 | 95,94 | 90,29 | 92,89 | 66,67 |
| Citrus-YOLO | 96,60 | 92,65 | 94,51 | 52,63 |

Catatan penyusunan tabel: teks ekstraksi Tabel 1 berupa deretan angka tanpa kolom, sehingga baris rerata diurai dari urutan angka. Urutan itu konsisten dengan teks makalah, yaitu selisih F1 Citrus-YOLO terhadap YOLOv5 dan YOLOX sebesar 1,62 dan 7,88 poin persentase (selisih dihitung: 94,51 − 92,89 dan 94,51 − 86,63) dan selisih FPS 14,04 terhadap YOLOv5. Nilai FPS di atas hanya terbaca pada baris video pertama.

### Kecepatan inferensi (Tabel 2)

| Konfigurasi | FPS | mAP (%) |
|---|---|---|
| 4096 × 2160 tanpa akselerasi | 16,67 | 96,64 |
| 640 × 640 tanpa akselerasi | 52,63 | 95,25 |
| 640 × 640 TensorRT float16 | 160,18 | 94,19 |
| 640 × 640 TensorRT float32 | 158,73 | 94,78 |

Metode dengan TensorRT float32 dipakai pada sistem. Teks juga menyebut angka 144,31 dan 142,86 FPS untuk akselerasi, yang berbeda dari Tabel 2; ketidakkonsistenan ini dicatat pada bagian verifikasi.

### Penghitungan (Tabel 3)

| Metrik | ByteTrack (52 pohon) | YOLOv5_DeepSORT (52 pohon) | Citrus-YOLO (52 pohon) | ByteTrack (36 pohon) | YOLOv5_DeepSORT (36 pohon) | Citrus-YOLO (36 pohon) |
|---|---|---|---|---|---|---|
| IDSR | 95 | 267 | 200 | 871 | 133 | 88 |
| Hitungan/acuan | 2461/4362 | 3958/4362 | 4408/4362 | 2441/1226 | 1138/1226 | 1162/1226 |
| L1 loss | −1901 | −404 | 46 | 1215 | −88 | −64 |
| Rerata galat | −43,58% | −9,26% | 1,05% | 99,10% | 7,18% | 5,22% |

Rerata galat tertulis di makalah: ByteTrack 71,34%, YOLOv5_DeepSORT 8,22%, dan metode usulan 3,135%. Penulis menyatakan angka ini adalah hasil perkiraan dengan galat, karena tiap video berisi sekitar 2.500 bingkai dan banyak buah per bingkai sehingga acuan manual mahal.

### Ablasi (Tabel 4, 15 video uji)

| Metode | MAPE (%) | MAE |
|---|---|---|
| YOLOX + ByteTrack | 208,1 | 875,4 |
| YOLOv5 + DeepSORT | 298,4 | 1.375,2 |
| Citrus-YOLO + DeepSORT | 383,7 | 1.691,6 |
| YOLOX + ByteTrack + SLC | 85,3 | 328,1 |
| YOLOv5 + DeepSORT + SLC | 75,3 | 306,1 |
| Citrus-YOLO + DeepSORT + SLC | 70,4 | 281,5 |
| YOLOX + ByteTrack + NUDC | 70,1 | 214,3 |
| YOLOv5 + DeepSORT + NUDC | 8,9 | 41,5 |
| Citrus-YOLO + DeepSORT + NUDC | 7,1 | 25,9 |

Dengan ID maksimum sebagai hitungan, Citrus-YOLO justru memiliki galat terbesar karena mendeteksi lebih banyak buah sehingga menghasilkan lebih banyak ID. NUDC menurunkan galat paling besar.

### Eksperimen lapangan

| Skenario | Hasil |
|---|---|
| Luring (Tabel 5, 33 pohon, 4 baris) | hitungan 1.322 dari total acuan 1.256, rerata IDs 18, rerata MAPE 5,28% |
| Daring | penundaan 8 sampai 15 s, kehilangan paket 3,4%, hitungan 1.444, rerata IDs 57,67, rerata MAPE 14,95% |
| Cahaya kuat (>70 kLux, Tabel 6, 20 pohon) | F1 87,19%, MAPE 15,99% |
| Cahaya sesuai (25 sampai 50 kLux) | F1 89,07%, MAPE 12,75% |
| Cahaya lemah (<10 kLux) | F1 87,05%, MAPE 15,59% |
| Satu, dua, tiga UAV | waktu sekitar 0,05; 0,06; 0,10 s per bingkai; memori GPU 2,34; 6,50; 8,61 GB tanpa TensorRT (teks menulis "g") |

Pada pembandingan dengan Zhang dkk. (2022) yang memakai kendaraan lapangan, mode luring metode ini mendapat F1 94,51%, MAPE 5,28%, dan FPS deteksi 158,73 dibandingkan 91,60%, 8,10%, dan 83,3; FPS deteksi ditambah penghitungan 50. Mode daring: F1 87,77%, MAPE 14,95%.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: sistem lengkap dari akuisisi sampai hitungan, dapat dipakai beberapa UAV paralel dalam waktu nyata, percepatan inferensi dengan TensorRT yang menurunkan mAP hanya 0,47%, dan penekanan penghitungan ganda lewat NUDC pada dua kebun dengan karakter berbeda.

Keterbatasan yang dinyatakan penulis: kualitas jaringan komunikasi memengaruhi mode daring (kehilangan bingkai merusak asumsi gerak seragam filter Kalman); ID sering berganti ketika buah muncul kembali setelah tertutup lama (misalnya oleh tiang batu), sehingga penghitungan ganda tetap terjadi; hanya buah pada satu sisi pohon yang dihitung, sehingga sebagian buah di sisi dalam atau sisi lain terlewat; konsumsi sumber daya naik seiring jumlah UAV; dan acuan angka memiliki galat karena pelabelan manual yang berat. Penulis menyebut pencacahan multi-pandang dengan kerja sama beberapa UAV sebagai pekerjaan mendatang.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pertama, jumlah video uji hanya 15 dan hasil tidak disertai ulangan atau interval kepercayaan. Kedua, acuan hitung dari pelabelan video (bukan panen atau hitung manual per pohon di lapangan) tidak diverifikasi silang, dan penulis sendiri menyebut angka Tabel 3 sebagai perkiraan. Ketiga, ablasi pada Tabel 4 menunjukkan MAPE awal yang sangat besar (misalnya 383,7%) yang menegaskan bahwa hasil bergantung hampir sepenuhnya pada pencacah, bukan pada detektor. Keempat, beberapa angka pada makalah tidak konsisten antarbagian (lihat catatan verifikasi), dan pembandingan dengan Zhang dkk. memakai perangkat dan skenario yang berbeda. Kelima, jeruk adalah buah kecil yang tampak serupa dan tidak dihitung per kelas kematangan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam aliran video dengan mekanisme pelacakan: Kalman filter, pencocokan Hungarian berbasis jarak Mahalanobis dan fitur penampilan (DeepSORT), serta pencacah garis berganda (NUDC) yang menetapkan kapan sebuah ID dihitung. Identitas dijaga sepanjang waktu pada satu sisi pohon, dan penulis menyatakan bahwa ID masih sering berganti setelah oklusi lama. Tidak ada mekanisme untuk menyatukan identitas antarsisi pohon atau antarpenerbangan.

Hitungan dilaporkan sebagai total per video atau per kebun, bukan per kelas. Acuan hitungnya adalah pelabelan video manual (DarkLabel) dan hitung manual, bukan hasil panen. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan bahwa hitungan harus ditentukan oleh aturan penghitungan yang tahan terhadap fragmentasi ID, bukan oleh ID maksimum, serta temuan bahwa buah yang tampak kecil atau jauh dari kamera lebih sering berganti ID. Karena makalah hanya memakai satu sisi, mekanisme lintas sisi harus disediakan dari sumber lain.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zheng2023efficient`.

Zheng dkk. mengusulkan sistem pencacahan jeruk daring berbasis UAV yang menggabungkan siaran langsung video, detektor Citrus-YOLO, pelacak DeepSORT, dan pencacah garis tidak seragam (NUDC) untuk menekan penghitungan ganda akibat kegagalan pelacakan. Pada uji lapangan dengan pencahayaan sesuai, sistem mencapai F1 deteksi 89,07% dan MAPE hitungan 12,75%, dan pada pengujian luring MAPE 5,28%, sedangkan mode daring memiliki MAPE 14,95%. Hanya satu sisi pohon yang dihitung.

Catatan verifikasi data: Angka F1 89,07% dan MAPE 12,75% berasal dari Tabel 6 (seksi 4.5.3). MAPE luring 5,28% dan daring 14,95% berasal dari Tabel 5 (seksi 4.5.2). Angka hitungan dan galat per kebun berasal dari Tabel 3 (seksi 4.3), dan ablasi dari Tabel 4 (seksi 4.4). Ketidakkonsistenan pada makalah: judul kolom Tabel 3 dan label Tabel 1 menyebut "Orange orchards" untuk kedua kebun sehingga identitas kebun jeruk Emperor tidak pasti dari teks; Tabel 4 menulis MAPE 7,1 dan MAE 25,9 sedangkan teks dan kesimpulan menulis 7,05% dan 25,87; teks seksi 4.2.1 menulis FPS 144,31 dan kesimpulan 142,86, sedangkan Tabel 2 menulis 160,18 dan 158,73; kesimpulan menyebut memori GPU 2,93, 8,09, dan 10,78 g sedangkan seksi 4.5.4 menulis 2,34, 6,50, 8,61 g ditambah 0,59, 1,59, 2,17 g; FPS pada Tabel 1 hanya terbaca untuk video pertama (66,67 dan 52,63; selisih 14,04 sesuai teks). Tabel 1 hasil ekstraksi berbentuk deretan angka tanpa kolom, sehingga baris rerata dibaca dari urutan dan sebaiknya dicocokkan dengan PDF. Tidak dilaporkan: jumlah pasti buah per kebun uji, lokasi dan lebar tepat garis hitung NUDC, serta nilai $\lambda$.
