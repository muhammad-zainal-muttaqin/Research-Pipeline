# MFFT: an improved method for stable ID tracking and counting of multi-class mango segmentation with multi-feature fusion in complex occlusion scenarios

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `huang2026mfft` |
| Judul asli | MFFT: an improved method for stable ID tracking and counting of multi-class mango segmentation with multi-feature fusion in complex occlusion scenarios |
| Penulis | Huang, Wentao; Li, Yingsheng; Tan, Beike; Bakari\'c, Marija Brki\'c; Zhu, Zhiqiang; Zhang, Xiaoshuan |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [huang2026mfft.pdf](../pdf/huang2026mfft.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.112149

## Gambaran Umum
Makalah ini mengusulkan MFFT (*Multi-Feature Fusion Tracking*), sebuah alur kerja yang menggabungkan segmentasi mangga, pelacakan dengan penggabungan beberapa fitur, pencacahan, dan estimasi biomassa. Data berasal dari kebun mangga komersial kultivar Jinhuang seluas 0,3 hektare di Baoting, Provinsi Hainan, Tiongkok, yang direkam dengan ponsel pada Maret 2025. Mangga yang dibungkus (*bagged*) pada pohon dan mangga yang jatuh di tanah diperlakukan sebagai dua kelas. Model segmentasi memakai *backbone* Swin-T dan dekoder Transformer kustom, dan pelacak memakai kombinasi IoU, momen Hu, histogram HSV, dan panjang diagonal mangga, filter Kalman yang diperluas, serta manajemen siklus hidup ID.

Hasil utama yang dilaporkan: mIoU segmentasi 0,71, F1 0,73, mAP50 0,67, mAP50-95 0,33, dan kecepatan 40,32 FPS pada 256 × 256 piksel. Pada pelacakan, MFFT mencapai MOTA 0,6513, MOTP 0,6366, dan IDF1 0,7075 pada video uji. Galat relatif rerata (MRE) pencacahan 4,30% dan galat estimasi biomassa 4,49%, dibandingkan dengan ByteTrack (29,19% dan 8,35%), DeepSORT (41,31% dan 10,39%), dan StrongSORT (74,39% dan 10,86%).

Makalah ini menyatakan bahwa hanya mangga yang jelas teridentifikasi di bagian depan bingkai atau di tanah yang dihitung; mangga yang jauh di latar belakang atau terlalu tinggi di tajuk dikecualikan. Teks makalah berbahasa Inggris.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pada kebun mangga dengan sudut pandang dan pencahayaan yang bervariasi, buah dibungkus, bergerombol dan saling menempel, serta tertutup daun dan buah lain, sehingga segmentasi buah kurang akurat, pergantian ID (*ID switch*) sering terjadi, dan galat pelacakan serta pencacahan besar. Metode segmentasi instans dan semantik yang ada dinilai mengalami keterbatasan adaptasi pada data sedikit dan lingkungan kebun mangga. Penulis menyebut pelacak daring seperti SORT dan DeepSORT bergantung pada hasil deteksi atau segmentasi dan pencocokan fitur, sedangkan penelitian pelacakan dan pencacahan mangga pada kondisi oklusi berat masih sedikit; metode pelacak titik pusat (*centroid*) yang ada dinilai tidak sesuai untuk oklusi timbal balik yang berat.

Penulis juga menyatakan bahwa penelitian estimasi biomassa belum menyatukan hasil segmentasi dengan hasil pencacahan, dan contoh yang dikutip (estimasi hasil markisa dengan YOLOv8n + OC-SORT + CRCM) dinilai tidak berkorelasi dengan hasil panen sebenarnya.

## Ide Utama
Ide utama ada tiga. Pertama, segmentasi tingkat piksel dengan modul penguat fitur dangkal, perhatian terhadap batas, dan penyaringan latar belakang, lalu instans dipisahkan dengan analisis komponen terhubung (instans semu, *pseudo-instance*). Kedua, panjang diagonal mangga (hasil analisis komponen utama, PCA, pada masker) dipakai sebagai fitur morfologi yang stabil terhadap perubahan sudut pandang, baik sebagai bagian dari pencocokan maupun sebagai variabel keadaan filter Kalman. Ketiga, manajemen siklus hidup ID yang menyimpan, menghaluskan, menghancurkan, dan menggunakan kembali ID untuk menekan hitungan ganda dan hilangnya target.

Perhitungan biomassa memakai panjang diagonal hasil segmentasi yang dihubungkan dengan hasil pelacakan, bukan dengan luas masker. Penulis menyatakan bahwa upaya melatih model untuk menyimpulkan panjang diagonal dari anotasi diagonal ditinggalkan karena aturan anotasi tidak seragam dan kinerja belajar sangat buruk.

## Cara Kerja Langkah demi Langkah

```
 video 30 FPS -> kunci bingkai 2 FPS -> segmentasi (Swin-T + dekoder kustom)
      -> instans semu (morfologi + kontur) -> fitur: posisi, Hu, HSV, diagonal
      -> Kalman 8 dimensi + kecocokan Hungarian (4 fitur berbobot)
      -> siklus hidup ID (tentatif, terkonfirmasi, kedaluwarsa)
      -> hitungan per kelas + biomassa dari panjang diagonal
```

### 1. Akuisisi data
Lokasi: kebun mangga Jinhuang komersial 0,3 ha di Baoting, Hainan. Wilayah penghitungan ditetapkan per baris sebagai area minat (*region of interest*, ROI) dengan pengenal unik. Perekaman dilakukan pada periode pematangan dan panen, Maret 2025, dengan ponsel (kamera utama 50 MP dengan fokus 24 mm dan kamera sudut lebar 48 MP dengan fokus 13 mm), resolusi 720 × 1280 piksel, ISO otomatis 100 sampai 800, dan kecepatan rana 1/60 sampai 1/1000 detik. Sudut pandang mencakup pandangan setinggi tanah dan pandangan samping antarbaris, di bawah berbagai pencahayaan (cerah, berawan, redup, senja) dan waktu hari. Video direkam pada 30 FPS lalu diambil kunci bingkai pada 2 FPS; bingkai buram atau salah pencahayaan disaring dan tiap citra memuat sedikitnya 10 instans mangga. Jumlah pohon atau baris tidak dilaporkan.

Anotasi poligon tingkat piksel dengan LabelMe dalam dua kelas (mangga di pohon, mangga di tanah): 552 citra, dibagi acak 8:2 menjadi 439 citra latih dan 113 citra validasi. Semua citra diubah ke 256 × 256 piksel dan dinormalisasi dengan statistik ImageNet. Seluruh sampel adalah mangga yang dibungkus secara alami sesuai praktik kebun.

### 2. Segmentasi
*Backbone* Swin-T praterlatih menghasilkan peta fitur 96 × 64 × 64, 192 × 32 × 32, 384 × 16 × 16, dan 768 × 8 × 8. Strategi pelepasan pembekuan bertahap diterapkan: tahap 1 dan 2 dibekukan pada awal, tahap 2 dilepas pada epoch 15 dan tahap 1 pada epoch 25. Dekoder kustom diadaptasi dari Mask2Former dan mencakup modul *Shallow Feature Enhancement* (SFE), lapisan proyeksi dengan *coordinate attention*, fusi multiskala (tahap 2 sampai 4 disamakan dengan tahap 1, lalu konvolusi 3 × 3 ke 256 kanal), modul perhatian objek kecil (SOA), modul perhatian batas (BAM) dengan konvolusi dilasi 1, 2, dan 4, modul penekan latar belakang (BGM), agregasi bertopeng, kepala masker, dan modul penghalusan masker. Fungsi kerugian campuran dinamis terdiri atas enam komponen: *focal cross-entropy* dengan *online hard example mining* (bobot 0,3), *focal Dice* (0,3), Lovász-Softmax (0,2), *instance repulsion* (0,1), *class contrast* (0,05), dan *polygon boundary* (0,05).

### 3. Hiperparameter latih
GPU laptop NVIDIA RTX 3060 6 GB dengan CPU AMD Ryzen 7 5800H. Ukuran batch 1 dengan akumulasi gradien 8 langkah (batch efektif 8), AdamW (*weight decay* 0,0001), laju belajar awal 0,0001 (0,000005 untuk tahap 1 dan 2, 0,00002 untuk tahap 3 dan 4), 100 epoch, pemanasan linear 3 epoch lalu *cosine annealing* 97 epoch, presisi campuran (AMP), dan penghentian dini setelah 20 epoch tanpa perbaikan.

### 4. Ekstraksi instans dan fitur
Dari masker kelas, instans dipisahkan dengan erosi-dilasi, deteksi kontur (area di bawah 30 piksel dibuang), kotak pembatas minimum, dan optimasi lambung cembung. Empat fitur dihitung: posisi (kotak dan pusat), bentuk (deskriptor 6 dimensi dari momen Hu), warna (histogram HSV 18 × 8 × 8, 288 dimensi), dan panjang diagonal. Panjang diagonal diperoleh dengan PCA pada piksel masker, proyeksi ke sumbu utama, dan jarak Euclid antara titik ekstrem; arah utama disesuaikan menurut kelas (vertikal untuk mangga di pohon, horizontal untuk mangga di tanah).

### 5. Pelacakan
Filter Kalman yang diperluas memakai vektor keadaan 8 dimensi $[x, y, w, h, L, dx, dy, dL]^T$ dan vektor ukur 5 dimensi, dengan $Q = 0{,}003\,I_8$ dan $R = 0{,}03\,I_5$. Kemiripan total dihitung sebagai $S_{total} = W_{IoU} S_{IoU} + W_{shape} S_{shape} + W_{color} S_{color} + W_{diag} S_{diag}$ dengan bobot 0,25, 0,25, 0,2, dan 0,3. Kemiripan bentuk memakai jarak kosinus vektor Hu, kemiripan warna memakai jarak Bhattacharyya antar-histogram, dan kemiripan diagonal berupa rasio panjang dikalikan indikator kesamaan kelas, sehingga pencocokan antarkelas tidak sah. Pencocokan optimal memakai algoritma Hungarian dengan ambang kemiripan 0,5.

### 6. Siklus hidup ID
Parameter: `ID_CACHE_FRAMES` = 8, `ID_SMOOTH_FRAMES` = 4, `ID_DESTROY_FRAMES` = 10, dan `ID_REUSE_THRESH` = 0,85. Tiga status ID adalah tentatif, terkonfirmasi, dan kedaluwarsa. ID yang tidak cocok selama 10 bingkai berturut-turut masuk ke kolam kedaluwarsa, dan ID baru mencoba memakai kembali ID kedaluwarsa yang kemiripannya melampaui 0,85 sebelum ID baru dibuat.

### 7. Estimasi biomassa
Panjang diagonal hasil segmentasi digabung dengan hasil pelacakan dan dihubungkan dengan data biomassa melalui regresi linear (Tabel 4). Cara perolehan nilai biomassa acuan (satuan dan metode pengukuran) tidak diuraikan pada teks yang tersedia.

## Eksperimen dan Hasil
Perangkat evaluasi mencakup presisi, *recall*, mIoU, F1, mAP50, mAP50-95, jumlah parameter, FLOPs, FPS, dan waktu inferensi untuk segmentasi, serta IDF1, MOTA, MOTP, dan waktu inferensi untuk pelacakan. Pembanding segmentasi adalah Mask R-CNN, Mask2Former, DETR, dan YOLOv8s; pembanding pelacakan adalah ByteTrack, DeepSORT, dan StrongSORT yang dipasangkan dengan jaringan segmentasi yang sama.

**Segmentasi (Tabel 1, set validasi 113 citra).**

| Model | Presisi | *Recall* | mIoU | F1 | mAP50 | mAP50-95 | FPS |
|---|---|---|---|---|---|---|---|
| Mask R-CNN | 0,78 | 0,80 | - | - | 0,69 | 0,36 | 6,28 |
| Mask2Former | 0,72 | 0,77 | 0,64 | 0,67 | 0,63 | 0,30 | 10,36 |
| DETR | 0,75 | 0,85 | - | - | 0,78 | 0,40 | 21,77 |
| YOLOv8s | 0,79 | 0,81 | - | - | 0,84 | 0,47 | 24,88 |
| MFFT (segmentasi) | 0,82 | 0,78 | 0,71 | 0,73 | 0,67 | 0,33 | 40,32 |

Penulis mengakui bahwa mAP50 dan mAP50-95 model mereka lebih rendah daripada DETR dan YOLOv8s. Ablasi modul perhatian (Tabel 2) menunjukkan mIoU 0,64 tanpa perhatian, 0,69 dengan modul tereduksi, 0,67 dengan CBAM, 0,64 dengan SE, dan 0,71 dengan modul penulis (mAP50 0,55, 0,61, 0,57, 0,59, dan 0,67). Ablasi *backbone* (Tabel 3) memberi mIoU 0,65 sampai 0,68 untuk EfficientNet-B0, EfficientNetV2-S, MobileNet_v3_large, dan ConvNeXt_T, dibandingkan 0,71 untuk Swin-T. Teks naratif menulis mAP50 "0,73" untuk model penulis pada bagian ablasi, padahal tabel mencatat mAP50 0,67 dan F1 0,73; angka tabel dipakai di sini.

**Pelacakan pada video uji (Tabel 6).**

| Pelacak | MOTA | MOTP | IDF1 | Waktu inferensi (ms) |
|---|---|---|---|---|
| MFFT | 0,6513 | 0,6366 | 0,7075 | 75,36 |
| ByteTrack | 0,6117 | 0,6308 | 0,6684 | 29,82 |
| DeepSORT | 0,5501 | 0,6260 | 0,6373 | 47,02 |
| StrongSORT | 0,4995 | 0,5963 | 0,5225 | 58,91 |

**Pencacahan dan biomassa (Tabel 4, 40 titik data video).**

| Metode | Pencacahan: kemiringan, RMSE, MAE, MRE | Biomassa: $R^2$, RMSE, MAE, MRE |
|---|---|---|
| MFFT | 1,04; 12,95; 8,75; 4,30% ($R^2$ 0,98) | 0,99; 6,09; 4,79; 4,49% |
| ByteTrack | 0,65; 113,49; 93,78; 29,19% | 0,97; 8,99; 7,74; 8,35% |
| DeepSORT | 0,55; 165,51; 134,95; 41,31% | 0,96; 9,88; 8,42; 10,39% |
| StrongSORT | 0,50; 248,57; 219,70; 74,39% | 0,96; 8,47; 7,31; 10,86% |

**Per kelas (Tabel 5, 30 titik data video).** Untuk mangga di pohon, MFFT memiliki persamaan $y = 1{,}13x - 10{,}75$, $R^2$ 0,98, dan MRE 6,37%; untuk mangga di tanah, $y = 1{,}01x + 1{,}01$, $R^2$ 0,99, dan MRE 3,36%. ByteTrack memperoleh MRE 10,78% (pohon) dan 24,36% (tanah). Tabel S1 sampai S3 (suplemen) memuat ablasi dekoder, kesalahan diagonal per tingkat oklusi (240 sampel), dan perbandingan filter Kalman biasa dengan yang diperluas; tabel suplemen itu tidak ada pada teks yang tersedia sehingga angkanya tidak dilaporkan di sini.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak: pencacahan dilaporkan terpisah untuk dua kelas, evaluasi memakai metrik pelacakan baku (MOTA, MOTP, IDF1) selain regresi hitungan, tiga pelacak dibandingkan pada segmentasi yang sama, ablasi dilakukan pada modul perhatian, *backbone*, dekoder, dan filter Kalman, dan model tetap berjalan pada GPU laptop 6 GB.

Keterbatasan yang dinyatakan penulis: (1) komponen terhubung dapat menggabungkan beberapa buah yang rapat menjadi satu instans dan segmentasi tidak lengkap di cahaya buruk, sehingga mengganggu pengukuran diagonal, pencocokan, dan hitungan; (2) pelacak sangat bergantung pada segmentasi, ID switch tetap terjadi, dan fitur visual dasar dapat gagal mengidentifikasi ulang pada gerak cepat atau oklusi penuh sesaat; (3) estimasi biomassa hanya 2D dan rawan bias akibat sudut pandang dan bentuk buah tak beraturan; (4) data hanya mangga yang dibungkus, belum divalidasi silang atau pada set data eksternal; (5) waktu inferensi MFFT adalah yang terlama di antara pelacak yang dibandingkan.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Set validasi hanya 113 citra dan pembagian acak 8:2 tidak menyebut pemisahan berdasarkan baris atau pohon, sehingga citra dari lokasi yang sama dapat muncul di kedua set (tidak dijelaskan di teks). Hitungan acuan pada 40 dan 30 titik data video, serta cara memperoleh nilai biomassa acuan, tidak dijelaskan rinci. Jumlah ID dalam satu video demonstrasi (24 untuk MFFT dan 28 untuk ByteTrack) hanyalah contoh tunggal. Hasil hanya untuk satu kebun dan satu kultivar. Bobot penggabungan fitur dipilih lewat "perbandingan ekstensif" tanpa tabel yang ditunjukkan pada teks. Data tersedia atas permintaan menurut pernyataan data, meskipun abstrak menyebut kode dan data tersedia terbuka melalui Google Drive.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak pada banyak bingkai video dengan pelacakan multi-objek berbasis penggabungan fitur: IoU, bentuk (momen Hu), warna (HSV), dan panjang diagonal, dengan asosiasi Hungarian, filter Kalman yang diperluas, serta manajemen siklus hidup ID termasuk penggunaan ulang ID kedaluwarsa. Identitas dipertahankan dalam satu video dari satu pergerakan kamera; tidak ada pencocokan antarsisi pohon atau antarvideo. Hitungan dilaporkan per kelas (mangga di pohon dan di tanah), tetapi kelasnya adalah lokasi buah, bukan tingkat kematangan, dan hanya pencocokan dalam kelas yang sama yang diizinkan. Acuan hitungnya adalah hitungan pada video (cara pengambilannya tidak diuraikan secara eksplisit), bukan hitungan panen atau hitungan lapangan pada pohon. Pelacak memakai kotak dan masker 2D tanpa pose kamera atau kedalaman.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: aturan bahwa kecocokan hanya sah dalam kelas yang sama, pembobotan beberapa fitur (bentuk, warna, ukuran, IoU), pemakaian ukuran morfologi (panjang diagonal) sebagai petunjuk identitas dan sebagai penduga massa, serta manajemen siklus hidup ID. Fitur warna tidak dapat dipindahkan begitu saja karena warna tandan berubah dengan kematangan dan sudut pandang, sedangkan makalah sendiri mencatat bahwa sudut pandang dan iluminasi memengaruhi tampilan target.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `huang2026mfft`.

Huang dkk. (2026) mengusulkan MFFT, alur kerja segmentasi mangga, pelacakan, pencacahan, dan estimasi biomassa untuk mangga di pohon dan di tanah pada kebun mangga Jinhuang di Hainan. Pelacak menggabungkan IoU, momen Hu, histogram HSV, dan panjang diagonal hasil PCA dengan filter Kalman 8 dimensi, algoritma Hungarian, dan manajemen siklus hidup ID. Pada video uji, MFFT mencapai MOTA 0,6513 dan IDF1 0,7075, serta MRE pencacahan 4,30% dan MRE biomassa 4,49%, dibandingkan ByteTrack dengan MRE pencacahan 29,19%. Segmentasi pada set validasi 113 citra memberi mIoU 0,71 dan mAP50 0,67 pada 40,32 FPS; pelacakan hanya dalam video tunggal tanpa pencocokan antarsisi.

Catatan verifikasi data: Angka segmentasi berasal dari Tabel 1 sampai Tabel 3; angka pelacakan dari Tabel 6; angka pencacahan dan biomassa dari Tabel 4; angka per kelas dari Tabel 5; ukuran data (552, 439, 113 citra) dari seksi 2.1; parameter ID dan bobot dari seksi 2.3; hiperparameter dari seksi 2.4.2. Teks ekstraksi terbaca baik, tetapi gambar dan Tabel S1 sampai S3 (suplemen) tidak tersedia; matriks persamaan Kalman terbaca sebagai deretan angka sehingga hanya dimensinya yang dilaporkan. Terdapat ketidakkonsistenan kecil: teks ablasi menulis mAP50 0,73 untuk model penulis, sedangkan tabel menunjukkan 0,67 (angka tabel dipakai); FPS pencacahan pada Tabel 4 (13,26 untuk MFFT) berbeda dari FPS segmentasi (40,32). Tidak dapat diverifikasi dari teks: jumlah pohon dan baris, jumlah video uji, sumber hitungan acuan pada 40 dan 30 titik data, satuan dan metode biomassa acuan, serta jumlah mangga total pada data.
