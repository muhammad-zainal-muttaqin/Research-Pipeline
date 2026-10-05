# Automatic Apple Detection and Counting with AD-YOLO and MR-SORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024automatic` |
| Judul asli | Automatic Apple Detection and Counting with AD-YOLO and MR-SORT |
| Penulis | Yang, Xueliang; Gao, Yapeng; Yin, Mengyu; Li, Haifang |
| Tahun | 2024 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [yang2024automatic.pdf](../pdf/yang2024automatic.pdf)
- DOI resmi: https://doi.org/10.3390/s24217012

## Gambaran Umum

Makalah ini mengusulkan alur pencacahan apel dari video kebun berbasis pelacakan-melalui-deteksi (*tracking-by-detection*, TBD). Alur terdiri atas detektor AD-YOLO, yaitu YOLOv8s yang ditambah modul *Omni-dimensional Dynamic Convolution* (ODConv), *Global Attention Mechanism* (GAM), dan lapisan *Soft Spatial Pyramid Pooling* (SSPPL), serta pelacak MR-SORT (*Multiple Rematching SORT*) yang dibangun di atas BoT-SORT dengan pencocokan ulang berbasis fitur penampilan (deskriptor SURF dan algoritma VLAD) dan mekanisme validasi. Jumlah apel dalam video sama dengan nilai ID terbesar yang diberikan pelacak.

Data pelacakan berasal dari basis data publik apel tahun 2021 (tujuh video, tiap video 1 menit, 1920 × 1080, 30 fps, total 8.447 apel pada acuan). Data deteksi gabungan empat sumber (MinneApple, WSU, Fuji-SfM, dan 960 citra yang diekstrak dari tujuh video tersebut), berjumlah 22.374 citra setelah augmentasi.

Hasil utama: AD-YOLO mencapai mAP 96,4%, lebih tinggi 3,1 poin persentase daripada YOLOv8s (93,3%). Dengan AD-YOLO dan MR-SORT, jumlah *ID switch* (IDS) turun dari 835 menjadi 538 (selisih 297, atau 35,6%), MOTA 85,6%, galat rerata (MAE) 0,07, dan koefisien determinasi $R^2$ antara hitungan dan acuan 0,98.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pencacahan buah dari video dengan TBD terganggu oleh oklusi buah, variasi cahaya, dan gerak kamera yang menyebabkan *ID switch*, yaitu buah yang sama memperoleh ID berbeda pada dua bingkai sehingga hitungan menjadi tidak akurat. Penulis menyebut tiga masalah pada metode terdahulu: detektor kurang mampu mendeteksi apel yang tertutup; pelacak yang dipakai untuk apel kurang baik dan tidak menangani gerak kamera; dan metode pencocokan penampilan VLAD tidak stabil serta mudah terganggu lingkungan kompleks.

Penulis juga menyatakan bahwa pencocokan penampilan berbasis CNN kurang cocok untuk buah karena tidak ada set data identifikasi ulang (*re-identification*, Re-ID) tambahan dan variasi buah yang sama antarbingkai berdekatan kecil. Pendekatan pelacakan batang pohon dinilai tidak berlaku di kebun yang batangnya banyak tertutup.

## Ide Utama

Gagasan utamanya adalah pencocokan berganda: setelah pencocokan IoU pertama dan kedua pada BoT-SORT, lintasan dan deteksi yang belum cocok dicocokkan ulang berdasarkan kemiripan penampilan memakai VLAD dengan deskriptor SURF. Karena kinerja VLAD tidak stabil, ditambahkan mekanisme validasi: dua wilayah pada citra yang sama mengalami perpindahan relatif yang sama di antara bingkai berdekatan, sehingga seorang apel dianggap berhasil dilacak hanya bila wilayah apel itu dan satu wilayah apel lain sama-sama cocok berdasarkan penampilan.

Di sisi detektor, tiga modifikasi dirancang untuk meningkatkan deteksi apel tertutup dan mengurangi deteksi keliru yang memicu ID baru.

## Cara Kerja Langkah demi Langkah

```
  Video --> AD-YOLO --> MR-SORT (BoT-SORT + VLAD/SURF + validasi)
        --> ID per apel --> ID terbesar = jumlah apel
```

### 1. Data

Data pelacakan: tujuh video dari basis data publik apel kedua (diambil 2021), dengan jumlah apel per video 1.509, 2.475, 959, 1.637, 1.109, 397, dan 361 (total 8.447; Tabel 1). Anotasi mencakup nomor bingkai, ID, dan kotak pembatas.

Data deteksi: MinneApple (1.000 citra), WSU (238 citra, "Crop Load Estimation"), Fuji-SfM (288 citra), dan 960 citra dari tujuh video (Tabel 2). Anotasi disatukan menjadi format kotak pembatas ternormalisasi. Augmentasi mencakup pembalikan horizontal dan vertikal, perubahan kecerahan, kontras, dan saturasi, derau Gauss, derau garam dan merica, perubahan ukuran, serta kabur gerak, sehingga total 22.374 citra dengan pembagian 8:1:1 (latih 17.898, validasi 2.237, uji 2.239; Tabel 3). Kultivar apel tidak dilaporkan.

### 2. AD-YOLO

Berbasis YOLOv8s, AD-YOLO mengganti konvolusi umum pada modul CBS *backbone* dengan ODConv (atensi pada empat dimensi ruang kernel), menambah GAM (atensi kanal dan spasial) setelah modul C2f terakhir *backbone*, dan mengganti SPPF dengan SSPPL yang memakai *SoftPool*. Ukuran masukan 640 × 640; ukuran *batch* 32, laju belajar awal 0,01, momentum 0,937, *weight decay* 0,0005.

### 3. MR-SORT

Langkah: (1) prediksi posisi lintasan dengan filter Kalman dan kompensasi gerak kamera; (2) pencocokan Hungarian untuk kotak berskor tinggi berdasarkan IoU dan penampilan (VLAD dengan SURF); (3) asosiasi kotak berskor rendah dengan lintasan yang belum cocok; (4) pembaruan status, pembuatan lintasan baru, penghapusan lintasan tak aktif. Parameter: track_high_thresh 0,5; track_low_thresh 0,1; new_track_thresh 0,7; match_thresh 0,5; track_buffer 30; appearance_thresh 0,5. Pencocokan memadukan fitur penampilan, jarak Mahalanobis, dan IoU.

## Eksperimen dan Hasil

Perangkat: GPU NVIDIA GeForce RTX 3090 24 GB, CPU Intel i9-10900X, PyTorch 1.10.0. Metrik deteksi: P, R, mAP, jumlah parameter, dan waktu. Metrik pencacahan: IDS, MOTA, dan MAE (galat relatif rerata antara hitungan dan acuan per video). Acuan hitung berasal dari anotasi basis data video publik (jumlah apel pada Tabel 1); makalah menyebut pembandingan dengan nilai sebenarnya yang dihitung manual.

Ablasi detektor (Tabel 8):

| Model | GAM | ODConv | SSPPL | P | R | mAP | Parameter (MB) | Waktu (ms) |
|---|---|---|---|---|---|---|---|---|
| 1 (YOLOv8s) | tidak | tidak | tidak | 94,1% | 87,4% | 93,3% | 11,14 | 1,8 |
| 2 | ya | tidak | tidak | 95,1% | 88,4% | 94,1% | 17,81 | 2,0 |
| 3 | tidak | ya | tidak | 94,6% | 87,8% | 93,7% | 11,16 | 1,8 |
| 4 | tidak | tidak | ya | 94,8% | 88,4% | 94,0% | 17,52 | 1,8 |
| 8 (AD-YOLO) | ya | ya | ya | 97,4% | 92,1% | 96,4% | 24,28 | 2,2 |

Pada Tabel 9, pembanding lain pada data yang sama memiliki mAP: Faster R-CNN 81,2%, YOLOv5s 92,7%, YOLOv7-tiny 92,0%, YOLOv8m 95,1%. Augmentasi meningkatkan YOLOv8s dari mAP 81,4% (data asli) menjadi 93,3% (Tabel 6).

Ablasi pencacahan (Tabel 10, acuan 8.447 apel pada tujuh video):

| Detektor | Pelacak | Hitungan terprediksi | IDS | MOTA | MAE |
|---|---|---|---|---|---|
| YOLOv8s | BoT-SORT | 9.771 | 835 | 84,4% | 0,17 |
| AD-YOLO | BoT-SORT | 9.204 | 742 | 85,1% | 0,09 |
| YOLOv8s | MR-SORT | 9.488 | 603 | 84,9% | 0,14 |
| AD-YOLO | MR-SORT | 8.984 | 538 | 85,6% | 0,07 |

Regresi hitungan terhadap acuan untuk tujuh video: $y = 1{,}04x + 28{,}24$ dengan $R^2 = 0{,}98$ (Gambar 12). Pada Tabel 11, metode ini dibandingkan dengan empat algoritma lain; angka metode ini 8.984 hitungan, IDS 538, MOTA 85,6%, MAE 0,07, sedangkan algoritma lain memiliki MOTA 71,5% sampai 83,4% dan MAE 0,26 sampai 0,61. Kolom tabel pembanding pada teks ekstraksi tidak sepenuhnya sejajar sehingga angka per algoritma pembanding tidak dirinci di sini.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis: peningkatan ke dua komponen (detektor dan pelacak) masing-masing menurunkan hitungan berlebih; pencocokan penampilan tanpa data Re-ID tambahan; waktu inferensi detektor 2,2 ms; hasil dibandingkan dengan beberapa algoritma pencacahan lain.

Keterbatasan yang dinyatakan penulis: kinerja kemungkinan menurun pada lingkungan kebun yang lebih kompleks; ukuran model membesar sehingga menyulitkan penerapan ringan pada perangkat kecil (distilasi pengetahuan disebut sebagai arah lanjutan); prediksi hasil panen dalam kilogram memerlukan estimasi diameter dan bobot buah (kamera RGB-D disebut sebagai kemungkinan).

Menurut pembacaan ringkasan ini, hitungan akhir pada semua konfigurasi masih melebihi acuan (misalnya 8.984 terhadap 8.447 pada konfigurasi terbaik), sehingga *ID switch* tetap menghasilkan hitungan berlebih. Menurut pembacaan ringkasan ini, evaluasi hanya pada tujuh video dari satu basis data publik, kelas tunggal (apel), dan tidak ada hitungan per kelas. Menurut pembacaan ringkasan ini, citra deteksi dan video pelacakan berbagi sumber (960 citra diekstrak dari tujuh video yang sama), dan teks tidak menjelaskan apakah bingkai uji dipisahkan dari bingkai latih pada video yang sama.

## Kaitan dengan Tinjauan main6

Makalah ini menangani apel yang terlihat pada banyak bingkai melalui pelacakan video: filter Kalman, kompensasi gerak kamera, pencocokan IoU, dan pencocokan ulang penampilan (SURF dengan VLAD plus validasi relatif-perpindahan). Pencocokan ulang penampilan ditujukan khusus untuk mengurangi *ID switch* setelah oklusi penuh, yang diperlihatkan pada Gambar 11 (apel yang hilang pada bingkai 51 dan muncul kembali pada bingkai 68 tetap memperoleh nomor yang sama pada MR-SORT, sedangkan BoT-SORT memberi nomor baru).

Hitungan dilaporkan per video, tidak per kelas. Acuan hitungnya adalah jumlah apel pada anotasi video basis data publik (8.447 apel di tujuh video), bukan panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan pencocokan ulang berbasis penampilan yang diverifikasi dengan konsistensi perpindahan relatif antarwilayah, serta pelaporan IDS dan MOTA di samping galat hitungan. Pendekatan ini mengandaikan urutan video yang kontinu dan kemiripan penampilan antarbingkai yang tinggi; makalah tidak menangani pencocokan antar-sisi pohon dengan sudut pandang yang berbeda jauh.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `yang2024automatic`.

Ringkasan yang aman dikutip: Yang dkk. (2024) mengusulkan detektor AD-YOLO (YOLOv8s dengan ODConv, GAM, dan SSPPL) dan pelacak MR-SORT (BoT-SORT dengan pencocokan ulang SURF-VLAD dan mekanisme validasi) untuk pencacahan apel dari video. Pada tujuh video dengan acuan 8.447 apel, kombinasi keduanya menurunkan *ID switch* dari 835 menjadi 538, mencapai MOTA 85,6% dan MAE 0,07, dengan mAP detektor 96,4%.

Catatan verifikasi data: Angka detektor terdapat pada Tabel 6 sampai 9 dan Bagian 3.3. Angka pencacahan terdapat pada Tabel 10 serta Bagian 3.4 dan 5. Deskripsi data terdapat pada Tabel 1 sampai 3. Pada Tabel 10, nilai GT hanya tercetak pada baris pertama dan kolom IDS, MOTA, dan MAE terbaca urut sesuai baris; pemetaan ini disimpulkan dari urutan teks ekstraksi. Tabel 11 tidak terbaca sempurna pada teks ekstraksi (kolom tidak sejajar), sehingga hanya baris metode ini yang dikutip. Teks menyatakan bahwa mAP naik 3,1% terhadap YOLOv8; nilai ini adalah selisih 96,4% dan 93,3% dalam poin persentase (dihitung). Penurunan IDS 35,6% sama dengan 297 dari 835. Teks makalah menulis "NC = 2" sebagai jumlah jenis target pada rumus mAP, padahal deteksi dijelaskan sebagai satu objek (apel); ketidaksesuaian ini tidak dapat diselesaikan dari teks. Data dinyatakan tersedia atas permintaan.
