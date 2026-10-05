# A Dynamic Kalman Filtering Method for Multi-Object Fruit Tracking and Counting in Complex Orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhai2025dynamic` |
| Judul asli | A Dynamic Kalman Filtering Method for Multi-Object Fruit Tracking and Counting in Complex Orchards |
| Penulis | Zhai, Yaning; Zhang, Ling; Hu, Xin; Yang, Fanghu; Huang, Yang |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [zhai2025dynamic.pdf](../pdf/zhai2025dynamic.pdf)
- DOI resmi: https://doi.org/10.3390/s25134138

## Gambaran Umum

Makalah ini mengusulkan metode pelacakan dan pencacahan buah apel pada video kebun, yang menggabungkan detektor YOLOv8n yang dimodifikasi dengan *Kalman filter* berfaktor lupa variabel (*variable forgetting factor*). Asosiasi objek antarbingkai memakai gabungan *Intersection over Union* (IoU) dan fitur identifikasi ulang (*Re-Identification*, Re-ID), dan gerak kamera dikompensasi dengan aliran optik jarang (*sparse optical flow*). Tujuannya ialah mencacah buah pada urutan video tanpa menghitung buah yang sama berulang kali.

Data yang dipakai ialah kumpulan citra terbuka *appledatasets* (7.311 citra) untuk melatih dan menguji detektor, serta video sintetis *Synthetic-apples* (250 bingkai, 24 detik, 10 bingkai per detik, lima pohon) untuk mengevaluasi pelacakan dan pencacahan. Data berupa citra apel; makalah tidak memakai tandan kelapa sawit.

Hasil utama: detektor yang diusulkan mencapai mAP@0,5 sebesar 89,5% pada *appledatasets*. Pelacak yang diusulkan mencapai MOTA 95,0%, IDF1 65,5%, dan HOTA 82,4%. Untuk pencacahan, kombinasi detektor dan pelacak itu menghasilkan koefisien determinasi $R^2$ 0,85 dan RMSE 1,57.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa model pendeteksian buah berbasis pembelajaran mendalam umumnya dirancang untuk citra tunggal yang statis, sehingga kurang sesuai untuk pencacahan skala besar pada adegan kebun yang berubah. Metode YOLO yang ada dinilai mengabaikan konsistensi temporal yang diperlukan untuk pelacakan.

Penulis merinci tiga tantangan pada kebun kompleks: (1) buah yang rapat dan mirip secara visual meningkatkan ketidakcocokan identitas; (2) oklusi yang lama memecah lintasan dan mengakumulasi galat; (3) *motion blur* akibat gerak kamera atau platform memutus lintasan dan mengganggu kontinuitas hitungan. Pelacak yang sudah ada (SORT, DeepSORT, ByteTrack, BoTSORT) bergantung pada model prediksi gerak, dan *Kalman filter* standar memakai parameter derau tetap yang tidak menyesuaikan diri terhadap gerak mendadak.

## Ide Utama

Gagasan utamanya ialah membuat kovarians *Kalman filter* beradaptasi terhadap derau melalui faktor lupa $\lambda_t$ yang dihitung dari norma kuadrat residu pengukuran. Pada derau tinggi, filter mengurangi ketergantungan pada data historis; pada derau rendah, filter memanfaatkan data historis lebih penuh. Gagasan ini dilengkapi detektor yang lebih akurat untuk buah kecil dan terhalang, kompensasi gerak kamera, dan asosiasi IoU-Re-ID.

Pencacahan dilakukan dengan menghitung identitas lintasan unik (*ID counting*) pada urutan bingkai. Dengan demikian, buah yang sama pada bingkai berbeda dihitung satu kali selama identitasnya dipertahankan oleh pelacak. Makalah ini tidak menangani lintas pandang dalam arti pohon yang dipotret dari sisi berbeda, hanya urutan bingkai video.

## Cara Kerja Langkah demi Langkah

### 1. Data dan anotasi

*Appledatasets* berisi 7.311 citra dengan faktor sulit seperti target kecil, oklusi, target padat, dan lingkungan kebun kompleks; anotasi memakai LabelImg. Pembagian pelatihan, validasi, dan uji dilakukan acak dengan rasio 7:2:1. Augmentasi meliputi pembalikan, rotasi, penskalaan, penambahan derau, dan peningkatan kontras warna. Video *Synthetic-apples* berdurasi 24 detik pada 10 bingkai per detik (250 bingkai, lima pohon), dianotasi manual untuk kotak pembatas dan identitas dengan Darklabel dalam format MOT sebagai acuan. Lokasi, kultivar, dan sensor perekam citra tidak dilaporkan.

### 2. Detektor YOLOv8n yang dimodifikasi

YOLOv8n dipilih sebagai garis dasar. Tiga perubahan diterapkan: (a) tulang punggung (*backbone*) diganti EfficientNet-B0 dengan penskalaan majemuk; (b) modul *Multi-Scale Dilated Attention* (MSDA) ditambahkan untuk mengurangi galat akibat oklusi; (c) kepala deteksi diganti FASFF (*Four Adaptively Spatial Feature Fusion*), yaitu struktur empat kepala dengan fusi fitur spasial adaptif untuk objek kecil.

### 3. *Kalman filter* dinamis

Vektor keadaan berisi posisi dan kecepatan kotak ($x$, $y$, $w$, $h$ dan kecepatannya; delapan dimensi) dengan model kecepatan konstan. Inisialisasi kovarians memakai bobot derau 2 untuk posisi dan 10 untuk kecepatan, yang menurut penulis ditentukan secara empiris dan mengikuti rancangan BoT-SORT. Pembaruan kovarians memakai faktor lupa:

$$C_{t+1} = (I - KH)\frac{C^-_{t+1}}{\lambda_t} + \left(1 - \frac{1}{\lambda_t}\right)C_t,$$

dengan $\lambda_t = \lambda_{\min} + (\lambda_{\max}-\lambda_{\min})\exp(-\gamma\,\|\delta_t\|^2)$ dan $\delta_t$ ialah residu pengukuran. Nilai numerik $\lambda_{\min}$, $\lambda_{\max}$, dan $\gamma$ tidak dilaporkan pada teks yang dibaca.

### 4. Kompensasi gerak kamera

Gerak kamera dimodelkan dengan matriks transformasi afin $A$ yang diestimasi dari posisi beberapa target pada bingkai berurutan memakai aliran optik jarang dan RANSAC. Pusat dan ukuran kotak hasil prediksi dikoreksi dengan invers $A$ dan faktor skala.

### 5. Asosiasi data IoU-Re-ID

Fitur Re-ID diekstraksi dengan pustaka FastReID dan dihaluskan dengan rata-rata bergerak eksponensial. Jarak gabungan memakai aturan nilai minimum: $d_{\text{fused}} = \min(d_{\text{IoU}}, d_{\text{ReID}})$. Kandidat IoU berkorelasi rendah disaring melalui Re-ID. Asosiasi tahap pertama memakai IoU dan Re-ID pada deteksi berskor tinggi, dan asosiasi tahap kedua memakai IoU pada deteksi berskor rendah. Manajemen lintasan mencakup prediksi, pembaruan, pembuatan, penghentian, dan penghitungan ID.

## Eksperimen dan Hasil

Perangkat keras: prosesor AMD EPYC 9754S 128 inti, RAM 128 GB, dan NVIDIA GeForce RTX 4090 24 GB; perangkat lunak PyTorch 1.12.1, CUDA 11.6, Python 3.8. Metrik deteksi ialah mAP, GFLOPs, FPS, dan ukuran model; metrik pelacakan ialah MOTA, IDF1, dan HOTA; metrik pencacahan ialah $R^2$ dan RMSE terhadap hitungan manual pada video uji.

Tabel 1 menampilkan perbandingan detektor pada *appledatasets* (sebagian baris).

| Model | P (%) | mAP@0,5 (%) | mAP@0,5:0,95 (%) | GFLOPs |
|---|---|---|---|---|
| YOLOv5n | 81,0 | 84,1 | 38,0 | 4,2 |
| YOLOv7 | 53,1 | 79,0 | 33,1 | 103,5 |
| YOLOv8n (garis dasar) | 84,9 | 85,8 | 42,3 | 8,1 |
| YOLOv10n | 84,8 | 83,1 | 40,4 | 8,2 |
| YOLOv11 | 85,5 | 84,2 | 41,0 | 6,3 |
| YOLOv12n | 84,8 | 83,5 | 38,7 | 6,0 |
| EfficientNet saja (Model 1) | 84,0 | 87,1 | 44,5 | 5,6 |
| MSDA saja (Model 2) | 83,6 | 86,3 | 42,8 | 8,4 |
| FASFF saja (Model 3) | 83,2 | 88,7 | 44,9 | 15,4 |
| Diusulkan (Model 7) | 86,7 | 89,5 | 47,3 | 12,9 |

Teks narasi menyebut mAP@0,5:0,95 model usulan sebesar 47,5% dan peningkatan 5,0%, sedangkan Tabel 1 mencatat 47,3%; ketidaksesuaian ini dicatat apa adanya.

Tabel 2 memuat perbandingan pelacak. Kolom detektor menandai pemakaian YOLOv8n (metode 1 sampai 4) atau detektor yang ditingkatkan (metode 5 sampai 8).

| Pelacak | Detektor | MOTA (%) | IDF1 (%) | HOTA (%) |
|---|---|---|---|---|
| SORT | YOLOv8n | 65,0 | 39,0 | 59,1 |
| DeepSORT | YOLOv8n | 76,0 | 49,0 | 73,7 |
| ByteTrack | YOLOv8n | 75,0 | 37,0 | 68,6 |
| BoTSORT | YOLOv8n | 84,7 | 55,5 | 76,4 |
| SORT | Improved YOLO | 69,7 | 42,0 | 70,2 |
| DeepSORT | Improved YOLO | 86,7 | 49,7 | 74,2 |
| ByteTrack | Improved YOLO | 75,2 | 38,4 | 69,2 |
| BoTSORT | Improved YOLO | 89,2 | 61,9 | 80,2 |
| Dynamic Kalman filter tracker (diusulkan) | Improved YOLO | 95,0 | 65,5 | 82,4 |

Jarak Fréchet antara kurva hitungan dan acuan ialah 5,0 untuk metode usulan, dibandingkan 46,5 (metode 7) dan 24,3 (metode 8).

Tabel 3 memuat hasil pencacahan terhadap hitungan acuan manual.

| Metode | $R^2$ | RMSE | Persamaan regresi |
|---|---|---|---|
| YOLOv8 + BoTSORT | 0,72 | 2,13 | $y = 0{,}84x + 2{,}05$ |
| Improved YOLO + BoTSORT | 0,78 | 1,87 | $y = 0{,}84x + 2{,}55$ |
| Improved YOLO + dynamic Kalman filter tracker | 0,85 | 1,57 | $y = 0{,}89x + 1{,}75$ |

Pada distribusi selisih ID (Gambar 9), proporsi galat negatif turun dari 28,5% dan 20,8% menjadi 16,2% pada metode usulan, menurut label gambar pada teks ekstraksi.

## Kelebihan dan Keterbatasan

Kelebihan yang diklaim penulis: peningkatan konsisten pada MOTA, IDF1, HOTA, $R^2$, dan RMSE dibandingkan SORT, DeepSORT, ByteTrack, dan BoTSORT; kode dan citra eksperimen disediakan di repositori GitHub. Penulis menyatakan bahwa langkah berikutnya ialah memperbaiki kinerja waktu nyata dan penerapan pada perangkat bergerak, yang menyiratkan bahwa hal itu belum tercapai.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan. Evaluasi pelacakan dan pencacahan memakai satu video sintetis berdurasi 24 detik dengan lima pohon, sehingga generalisasi ke video lapangan nyata tidak teruji. Acuan hitungan ialah anotasi identitas pada video, bukan hitung buah panen. Hitungan hanya dievaluasi sebagai jumlah ID per bingkai, bukan per kelas. Nilai IDF1 (65,5%) jauh di bawah MOTA (95,0%), yang menunjukkan masih adanya perubahan identitas. Makalah tidak melaporkan ablasi untuk komponen kompensasi gerak kamera dan faktor lupa secara terpisah, dan nilai parameter faktor lupa tidak tercantum pada teks yang dibaca. Tidak ada ulangan atau varians antar-lari yang dilaporkan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam bingkai video berurutan dengan mekanisme pelacakan-berbasis-deteksi (*tracking-by-detection*): prediksi gerak *Kalman filter*, kompensasi gerak kamera, dan asosiasi IoU-Re-ID, lalu penghitungan jumlah identitas unik. Mekanisme ini bersifat temporal pada satu lintasan kamera, bukan pencocokan antar-sisi pohon. Hitungan tidak dilaporkan per kelas, dan acuan hitungnya ialah anotasi identitas pada video sintetis, bukan panen maupun hitung manual lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi ialah gagasan asosiasi gabungan geometri (IoU) dan penampilan (Re-ID) serta pembaruan kovarians adaptif terhadap derau. Asumsi gerak kecepatan konstan antarbingkai tidak langsung berlaku bila sisi pohon dipotret terpisah dengan lompatan pandang besar, sehingga komponen prediksi gerak perlu diganti oleh syarat geometri antar-pandang.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zhai2025dynamic`.

Zhai dkk. (2025, *Sensors* 25, 4138) mengusulkan pelacak buah berbasis YOLOv8n yang dimodifikasi (EfficientNet-B0, MSDA, kepala FASFF) dengan *Kalman filter* berfaktor lupa variabel, kompensasi gerak kamera, dan asosiasi IoU-Re-ID. Pada video sintetis apel berisi 250 bingkai dan lima pohon, pelacak ini mencapai MOTA 95,0% dan HOTA 82,4%, serta pencacahan dengan $R^2$ 0,85 dan RMSE 1,57; detektor mencapai mAP@0,5 89,5% pada kumpulan data *appledatasets*.

Catatan verifikasi data: angka detektor berasal dari Tabel 1 dan Seksi 3.1; angka pelacakan dari Tabel 2 dan Seksi 3.2; angka pencacahan dari Tabel 3 dan Seksi 3.3; ukuran dan pembagian data dari Seksi 2.1. Nilai mAP@0,5:0,95 model usulan tercatat 47,3% pada Tabel 1 dan 47,5% pada narasi Seksi 3.1. Persentase galat negatif pada Gambar 9 dibaca dari label gambar hasil ekstraksi dan tidak dapat dipastikan petaannya ke metode. Teks narasi menyebut HOTA ByteTrack 69,1% sedangkan Tabel 2 mencatat 69,2%. Lokasi, kultivar, dan perangkat perekam citra tidak dilaporkan, dan kegiatan evaluasi pada video lapangan nyata tidak ada.
