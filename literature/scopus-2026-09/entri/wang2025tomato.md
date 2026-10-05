# Tomato Yield Estimation Using an Improved Lightweight YOLO11n Network and an Optimized Region Tracking-Counting Method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2025tomato` |
| Judul asli | Tomato Yield Estimation Using an Improved Lightweight YOLO11n Network and an Optimized Region Tracking-Counting Method |
| Penulis | Wang, Aichen; Xu, Yuanzhi; Hu, Dong; Zhang, Liyuan; Li, Ao; Zhu, Qingzhen; Liu, Jizhan |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [wang2025tomato.pdf](../pdf/wang2025tomato.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15131353

## Gambaran Umum
Makalah ini mengusulkan sistem estimasi hasil tomat yang terdiri atas dua bagian: jaringan YOLO11n yang diringankan untuk deteksi dan segmentasi semantik, serta metode penghitungan berbasis wilayah pelacakan (*region tracking-counting*) yang dioptimalkan dengan *particle swarm optimization* (PSO). Sistem menghitung tomat pada tiga tingkat kematangan (matang, setengah matang, mentah) dari video yang direkam saat kamera bergerak sepanjang barisan tanaman di rumah kaca. Masalah yang ditangani adalah galat hitung akibat oklusi dan tumpang tindih buah dan daun, serta kesalahan penetapan ID pada pelacakan.

Data diperoleh dari rumah kaca Jiangsu Xingang Agricultural Technology Co., Ltd. (Zhenjiang, Tiongkok) pada Juni 2023, berupa 808 citra mentah dan 21 potongan video berdurasi 30 detik. Jaringan YOLO11n yang ditingkatkan mencapai presisi 91,3% pada tugas deteksi (*box*) dan 90,5% pada tugas segmentasi (*seg*), dengan 2,66 M parameter dan 8,0 GFLOPs, atau berkurang 0,22 M parameter dan 2,5 G GFLOPs terhadap YOLO11n dasar.

Untuk penghitungan, metode wilayah hasil optimasi PSO mencapai *mean counting error* (MCE) 6,6% pada sembilan video uji. Angka itu lebih rendah 5,0 poin persentase daripada Bytetrack (11,6%) dan 2,1 poin persentase daripada metode garis silang (*cross-line counting*, 8,7%). Kinerja pada Jetson Orin NX dilaporkan 62 FPS dengan memori puncak sekitar 3,1 GB dan daya rata-rata 15,6 W.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil sebelum panen diperlukan untuk menyesuaikan strategi budi daya, penyimpanan, logistik, dan pemasaran, karena buah tomat panenan memiliki masa simpan yang singkat. Pengamatan dan pemetikan manual memerlukan banyak tenaga kerja dan tidak akurat akibat oklusi daun, pertumbuhan yang rapat, dan sulitnya membedakan tingkat kematangan. Metode penglihatan mesin konvensional bergantung pada operator rancangan manual yang harus disesuaikan pada tiap skenario.

Penulis menyatakan bahwa pelacakan multi-target dapat mengatasi kehilangan target dan penghitungan ganda akibat oklusi, tetapi pelacakan berbasis ID rentan terhadap kesalahan penetapan ID. Metode penghitungan satu pandang atau dua pandang disebut kesulitan mengenali buah berskala beragam karena oklusi. Penulis juga mencatat bahwa metode wilayah pelacakan terdahulu (Zhang dkk., rerata galat hitung 8%) tidak mengoptimalkan wilayah hitungnya. Model berukuran besar seperti Mask R-CNN terlalu berat untuk perangkat tepi (*edge device*).

## Ide Utama
Gagasan pertama adalah menghitung buah tidak dari jumlah ID unik yang pernah muncul, tetapi dari buah yang melewati garis tegak di tengah bidang pandang kamera. Karena kamera bergerak, setiap buah pasti melintasi garis itu, sehingga penghitungan tidak bergantung pada kesinambungan ID. Kelemahannya, buah yang tertutup daun tepat saat melintasi garis tidak terhitung.

Gagasan kedua adalah melebarkan garis itu menjadi wilayah simetris terhadap garis tengah citra. ID sebuah kotak pembatas dicatat dan dihitung begitu kotak mulai memasuki wilayah, sehingga oklusi sesaat tidak menyebabkan buah terlewat. Lebar wilayah dipilih dengan PSO dengan galat akar rerata kuadrat (RMSE) terhadap jumlah sebenarnya sebagai fungsi kebugaran (*fitness function*). Gagasan ketiga adalah meringankan YOLO11n dengan modul C3k2-F, DSConv, dan fungsi kerugian GIoU agar sistem dapat berjalan pada perangkat tepi.

## Cara Kerja Langkah demi Langkah

```
  [Video rumah kaca] -> [YOLO11n ringan: kotak + segmentasi + 3 kelas]
        -> [Bytetrack: Kalman + Hungarian, ID unik per buah]
        -> [Wilayah hitung (lebar hasil PSO) -> hitung ID yang masuk]
```

### 1. Akuisisi data
Kamera Intel RealSense D435 beresolusi 1280 × 720 dipasang pada batang geser vertikal sekitar 1,2 m dari barisan tanaman dan terhubung ke Jetson Orin NX melalui USB 3.0. Peralatan dibawa dengan kereta rel. Citra diambil pada beberapa tahap pertumbuhan, tingkat oklusi, dan kondisi cahaya, dengan total 808 citra mentah. Sebanyak 242 citra dipilih acak sebagai data uji, dan 566 citra menjadi data latih dan validasi awal. Citra diubah ukurannya menjadi 640 × 640. Anotasi memakai Labelme dengan tiga kelas (matang, setengah matang, mentah) yang dinilai dari nilai RGB. Kontur buah dianotasi termasuk bagian yang tertutup, dan buah dengan kurang dari 2500 piksel tidak dianotasi.

Video direkam dengan kereta rel bergerak berkecepatan tetap, dibagi menjadi 21 segmen berdurasi 30 detik (1280 × 720, 30 bingkai per detik): delapan segmen untuk latih, empat untuk validasi, dan sembilan untuk uji algoritma pelacakan dan penghitungan. Jumlah pohon atau tanaman, kultivar, dan jumlah buah total tidak dilaporkan.

### 2. Jaringan YOLO11n yang ditingkatkan
Garis dasarnya adalah YOLO11n (CSPNet dengan modul C2PSA dan C3k2). Tiga modifikasi dilakukan. Pertama, modul C3k2-F dirancang dengan mengganti *bottleneck* pada C3k dengan blok FasterNet yang memakai konvolusi parsial (PConv). Kedua, lapisan Conv diganti dengan DSConv (*depthwise separable convolution*). Ketiga, fungsi kerugian CIoU diganti GIoU, dengan *distribution focal loss* (DFL) dan BCE sebagai kerugian regresi.

Pelatihan memakai Ubuntu 20.04, GPU GTX 3080Ti, PyTorch 1.13.1, ukuran masukan 640 × 640, 200 epoch, ukuran *batch* 16, SGD dengan laju belajar awal 0,01, peluruhan bobot 0,0005, momentum 0,937, dan bobot praterlatih resmi. Ambang IoU latih dan uji adalah 0,7.

### 3. Pelacakan dengan Bytetrack
Deteksi pada tiap bingkai diteruskan ke Bytetrack: filter Kalman memprediksi posisi pada bingkai berikutnya, dan algoritma Hungarian mencocokkan objek antarbingkai. Lintasan yang gagal dicocokkan disimpan sementara, dan lintasan yang tidak cocok pada beberapa bingkai dihapus. Setiap buah yang terlacak memperoleh ID unik untuk dihitung.

### 4. Penghitungan garis silang dan wilayah
Pada metode garis silang, buah dihitung ketika kotaknya memotong garis tegak di tengah bidang pandang. Pada metode wilayah, garis dilebarkan menjadi wilayah simetris; ID kotak dicatat dan dihitung saat kotak mulai memasuki wilayah. Tinggi wilayah tetap 720 piksel, dan lebar $x$ dicari pada rentang [0, 1280] dengan PSO. Fungsi kebugaran adalah $G(y)=\sqrt{\sum_{i=1}^{n}(y'_i-y_i)^2/n}$, dengan $y'_i$ jumlah sebenarnya dan $y_i$ jumlah hasil algoritma pada video ke-$i$. Lebar dibulatkan menjadi bilangan genap. Optimasi berjalan 200 iterasi dan RMSE konvergen ke sekitar 2,5; lebar optimum 876 piksel, sehingga jendela akhir berukuran 876 × 720.

### 5. Metrik
Metrik deteksi adalah presisi, *recall*, AP, dan mAP. Metrik penghitungan adalah *mean precision* (MP), *mean error* (ME, proporsi pengenalan keliru terhadap hitungan sistem), *mean repetition* (MR, proporsi buah terhitung ganda), dan MCE, yaitu $\frac{1}{n}\sum_i |G_i-E_i|/G_i \times 100\%$, dengan $G_i$ jumlah sebenarnya dan $E_i$ jumlah prediksi pada video ke-$i$.

## Eksperimen dan Hasil
Uji ablasi dan pembandingan jaringan dilakukan pada 242 citra uji. Uji penghitungan memakai video: empat video validasi untuk memilih lebar wilayah dan sembilan video uji untuk evaluasi akhir. Acuan hitungan adalah jumlah buah sebenarnya per video (disebut hitungan manual pada Tabel 5); cara penghitungan acuan secara rinci tidak dijelaskan.

Tabel 1 (ablasi, data uji; P = presisi, R = *recall*, satuan persen):

| Model | P box | R box | mAP50 box | mAP50:90 box | P seg | mAP50 seg | Param (M) | GFLOPs |
|---|---|---|---|---|---|---|---|---|
| YOLO11n | 89,4 | 91,6 | 93,5 | 69,7 | 89,2 | 93,0 | 2,88 | 10,5 |
| + C3k2-F | 90,7 | 90,4 | 94,6 | 67,3 | 90,4 | 94,2 | 2,66 | 9,8 |
| + C3k2-F + DSConv | 90,3 | 88,2 | 94,2 | 66,4 | 89,8 | 93,7 | 2,66 | 8,0 |
| + C3k2-F + DSConv + GIoU | 91,3 | 86,2 | 93,3 | 65,8 | 90,5 | 92,3 | 2,66 | 8,0 |

Penambahan GIoU menaikkan presisi tetapi menurunkan *recall* dan mAP (R box turun dari 88,2% menjadi 86,2%). Penulis menyatakan bahwa mAP dan *recall* sedikit berkurang pada tahap ini. Pada tugas segmentasi, *recall* akhir adalah 85,4% dan mAP50:90 adalah 59,3%.

Tabel 2 (pembandingan jaringan; P dan mAP50 dalam persen):

| Model | P box | mAP50 box | P seg | mAP50 seg | FPS | Param (M) | GFLOPs |
|---|---|---|---|---|---|---|---|
| Mask-RCNN | 92,0 | 94,5 | 91,9 | 86,0 | 19 | 41,3 | 251,4 |
| YOLOv5n | 79,3 | 84,4 | 79,2 | 85,0 | 116 | 7,10 | 16,0 |
| YOLOv6n | 85,3 | 86,2 | 86,2 | 87,4 | 84 | 4,9 | 7,0 |
| YOLOv7 | 91,8 | 90,6 | 91,4 | 90,2 | 32 | 36,90 | 104,7 |
| YOLOv8n | 88,4 | 89,5 | 87,8 | 88,7 | 60 | 3,40 | 12,6 |
| YOLO11n ditingkatkan | 91,3 | 93,3 | 90,5 | 92,3 | 62 | 2,66 | 8,0 |

Mask-RCNN memiliki presisi box dan mAP50 box yang lebih tinggi daripada model yang diusulkan (92,0% dan 94,5%), tetapi dengan 19 FPS dan 251,4 GFLOPs.

Tabel 3 (galat penghitungan pada empat video validasi; jumlah buah):

| Video | Sebenarnya | Garis silang | Wilayah 500 piksel | Wilayah hasil PSO (876 piksel) |
|---|---|---|---|---|
| 1 | 157 | 145 | 175 | 171 |
| 2 | 167 | 153 | 173 | 171 |
| 3 | 123 | 113 | 114 | 116 |
| 4 | 134 | 119 | 125 | 124 |
| MCE (%) | | 8,8 | 7,3 | 6,1 |

Tabel 4 (tiga metode penghitungan, sembilan video uji, persen):

| Metode | MP | ME | MR | MCE |
|---|---|---|---|---|
| Bytetrack | 80,6 | 11,4 | 12,3 | 11,6 |
| Garis silang | 84,9 | 9,1 | 6,8 | 8,7 |
| Wilayah (PSO) | 86,6 | 7,4 | 8,3 | 6,6 |

Metode garis silang memiliki MR terendah (6,8%) karena tidak bergantung pada ID, tetapi kehilangan hitungan bila buah tertutup saat melintasi garis. Bytetrack memiliki MR tertinggi karena ID hilang pada oklusi lama.

Tabel 5 (hasil per kelas, sistem lengkap, persen):

| Kelas | MP | ME | MR | MCE |
|---|---|---|---|---|
| Matang | 93,4 | 7,5 | 8,7 | 12,3 |
| Setengah matang | 71,9 | 10,4 | 3,4 | 16,9 |
| Mentah | 91,3 | 7,3 | 11,8 | 17,3 |
| Semua | 86,6 | 7,4 | 8,3 | 6,6 |

Galat per kelas (12,3% sampai 17,3%) jauh lebih besar daripada galat gabungan (6,6%). Penulis menafsirkan MCE gabungan yang rendah sebagai bukti bahwa total tetap akurat walaupun terdapat penyimpangan pada tiap kelas. Penulis menyatakan kelas setengah matang paling sulit dikenali karena warna dan bentuknya mirip kelas lain, dan perpindahan label antara mentah dan setengah matang atau antara setengah matang dan matang menyebabkan penghitungan ganda. Pada Jetson Orin NX, seluruh alur berjalan rata-rata 62 FPS.

## Kelebihan dan Keterbatasan
Kelebihan yang dapat dibaca dari makalah: metode wilayah tidak bergantung pada ketepatan ID sepanjang lintasan, sistem menghasilkan hitungan per kelas kematangan, dan model cukup ringan untuk berjalan pada perangkat tepi dengan 62 FPS.

Keterbatasan yang dinyatakan penulis: akurasi deteksi buah setengah matang jelas lebih rendah daripada kelas matang dan mentah sehingga menimbulkan galat hitung; kumpulan data (808 citra dan 21 klip video) dan konfigurasi kamera belum mencakup keragaman kondisi lapangan, termasuk pencahayaan atau oklusi ekstrem; fungsi sistem masih dalam tahap pengembangan dengan cakupan terbatas dan biaya perangkat tinggi.

Menurut pembacaan ringkasan ini: (a) penghitungan bergantung pada gerak kamera yang lurus dan berkecepatan tetap pada satu sisi barisan, sehingga buah yang sama dari sisi lain atau pandangan berbeda tidak diidentifikasi sebagai satu buah; (b) video uji hanya sembilan segmen dan jumlah buahnya tidak dilaporkan total; (c) MCE 6,1% (Tabel 3, validasi) dan 6,6% (Tabel 4, uji) berasal dari kumpulan video berbeda, dan lebar wilayah dipilih pada video validasi yang kecil (empat video); (d) MCE per kelas pada Tabel 5 lebih besar daripada MCE semua kelas, dan teks tidak menjelaskan secara rinci mengapa MCE gabungan lebih kecil daripada tiap MCE per kelas; (e) tidak ada perbandingan dengan hitungan panen.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan dua mekanisme: pelacakan multi-objek Bytetrack (filter Kalman dan pencocokan Hungarian) yang memberi ID per buah, dan aturan penghitungan berbasis wilayah tetap pada bidang pandang yang menghitung tiap ID satu kali saat memasuki wilayah. Identitas hanya dijaga dalam satu lintasan video searah; tidak ada pencocokan lintas sisi atau lintas lintasan. Hitungan dilaporkan per kelas (matang, setengah matang, mentah) pada Tabel 5, dengan acuan berupa jumlah buah sebenarnya per video yang disebut hitungan manual; bukan hasil panen dan bukan anotasi citra tunggal.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan menghitung buah yang melewati wilayah penghitungan sehingga tidak bergantung pada ID yang utuh, pengoptimalan lebar wilayah pada data validasi, dan pelaporan galat per kelas kematangan. Makalah ini tidak menangani identitas lintas sisi pohon, sehingga tidak memberi solusi untuk buah yang sama pada citra dari sisi berbeda. Temuan bahwa kelas antara (setengah matang) paling rawan galat dan penghitungan ganda akibat perpindahan label juga relevan bagi inventaris per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wang2025tomato`.

Wang dkk. (2025) mengusulkan sistem estimasi hasil tomat rumah kaca yang menggabungkan YOLO11n ringan (C3k2-F, DSConv, GIoU; 2,66 M parameter, 8,0 GFLOPs) dengan penghitungan berbasis wilayah pelacakan yang lebarnya dioptimalkan oleh PSO. Pada sembilan video uji, sistem menghitung tiga kelas kematangan dengan MCE gabungan 6,6%, dibandingkan 11,6% untuk Bytetrack dan 8,7% untuk penghitungan garis silang. Galat per kelas lebih tinggi (12,3% sampai 17,3%), dan kelas setengah matang paling lemah dikenali.

Catatan verifikasi data: Angka deteksi dan segmentasi bersumber dari Tabel 1 dan Tabel 2; angka galat penghitungan dari Tabel 3 (video validasi), Tabel 4 (sembilan video uji), dan Tabel 5 (per kelas); lebar wilayah optimum 876 piksel dari Gambar 11 dan teks bagian 3.3; kinerja Jetson Orin NX (62 FPS, sekitar 3,1 GB, 15,6 W) dari akhir bagian 3.4. Teks ekstraksi tabel terbaca utuh. Selisih 5,0 dan 2,1 poin persentase tertulis di abstrak dan sesuai dengan Tabel 4. Pada Tabel 1, baris selisih terakhir hanya terbaca sebagian pada ekstraksi, sehingga selisih itu tidak dikutip. Jumlah tanaman, kultivar, jumlah buah total pada video, dan rincian anotasi acuan penghitungan tidak dilaporkan dalam teks. Data tersedia atas permintaan kepada penulis korespondensi.
