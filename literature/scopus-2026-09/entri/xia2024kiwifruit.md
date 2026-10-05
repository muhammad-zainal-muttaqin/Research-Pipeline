# Kiwifruit Counting Using Kiwidetector and Kiwitracker

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xia2024kiwifruit` |
| Judul asli | Kiwifruit Counting Using Kiwidetector and Kiwitracker |
| Penulis | Xia, Yi; Nguyen, Minh; Yan, Wei Qi |
| Tahun | 2024 |
| Venue | Lecture Notes in Networks and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [xia2024kiwifruit.pdf](../pdf/xia2024kiwifruit.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-47724-9_41

## Gambaran Umum
Makalah ini mengusulkan model pencacahan buah kiwi dari video yang terdiri atas dua modul: KiwiDetector untuk deteksi berbasis YOLOv7 dan KiwiTracker untuk pelacakan serta pencacahan berbasis filter Kalman dan algoritma Hungarian (gaya DeepSORT). Data berupa 1.500 citra dan video kiwi yang diunduh dari internet, bukan hasil akuisisi lapangan oleh penulis.

Hasil utama yang dilaporkan: KiwiDetector mencapai mAP@0,5 sebesar 0,937 dan mAP@0,5:0,95 sebesar 0,622 setelah 150 epoch pelatihan, serta mengungguli YOLOv4, YOLOv5, dan YOLOv6 pada empat metrik. KiwiTracker mencapai *Average Counting Precision* (ACP) 0,802 pada sepuluh video dengan acuan hitung manual. Pada semua sepuluh video, jumlah hitungan model lebih besar daripada hitungan manual (galat positif), yang berarti model cenderung menghitung berlebih.

Penulis menyatakan bahwa metode ini dapat membantu estimasi hasil panen. Makalah tidak melaporkan pengujian pada pohon utuh dari beberapa sisi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah kiwi diperlukan untuk memprakirakan hasil panen, mengatur jadwal panen, mengurangi tenaga kerja, dan mendukung keputusan harga serta prakiraan pendapatan kebun. Fitur buatan tangan (tekstur, warna, bentuk) dinilai kurang tangguh terhadap perubahan cahaya, pantulan, dan oklusi di lingkungan nyata. Penulis juga menyebut tantangan pelacakan multi-objek (*multi-object tracking*, MOT): perubahan penampakan objek yang sama antarbingkai, oklusi, dan jumlah objek yang berubah. Penulis menyatakan tidak ada dataset kiwi berlabel terbuka untuk pelatihan deteksi.

## Ide Utama
Gagasannya adalah memisahkan tugas menjadi deteksi per bingkai dengan YOLOv7 dan asosiasi antarbingkai dengan filter Kalman serta pencocokan Hungarian yang memakai jarak Euklides dan IoU. Setiap lintasan yang bertahan diberi ID, dan jumlah ID unik menjadi hitungan buah pada video. Sebuah lintasan yang gagal dicocokkan selama 30 bingkai berturut-turut dibuang.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi dan penyiapan data
Citra dan video kiwi diunduh dari internet, video dipecah menjadi bingkai, dan terkumpul 1.500 citra awal. Pelabelan memakai Roboflow dengan *Auto-Orient*, dan citra diubah ukurannya menjadi 640 × 640 piksel. Augmentasi berupa pembalikan horizontal dan vertikal acak menambah data menjadi 1.885 citra, dibagi menjadi 1.516 citra latih, 246 citra validasi, dan 123 citra uji. Lokasi, kultivar, dan perangkat kamera tidak dilaporkan.

### 2. KiwiDetector (YOLOv7)
Penulis memilih YOLOv7 agar baik pada objek kiwi kecil dan latar yang rumit. Arsitektur terdiri atas masukan (augmentasi *mosaic*, perhitungan jangkar adaptif, penskalaan citra adaptif), *backbone* dengan struktur ELAN dan MP, serta bagian leher dan kepala dengan modul SPPCSPC dan lapisan REP. Pelatihan 150 epoch di Google Colab dengan GPU Tesla T4 (16 GB), Python 3.8.16, PyTorch 1.13.0, CUDA 11.2.

### 3. KiwiTracker (pelacakan dan pencacahan)
1. Deteksi kiwi pada tiap bingkai oleh KiwiDetector menghasilkan kotak pembatas dan peta fitur.
2. Filter Kalman memprediksi posisi dan gerak target pada bingkai berikutnya.
3. Algoritma Hungarian yang diperbaiki mencocokkan target antarbingkai berdasarkan jarak Euklides dan IoU untuk mengurangi duplikasi ID.
4. Lintasan yang gagal dicocokkan disimpan sementara dan ikut dicocokkan pada bingkai berikutnya, sampai gagal 30 bingkai berturut-turut, lalu dibuang.
5. Pencocokan yang berhasil diteruskan ke penghitung yang mengeluarkan jumlah total.

### 4. Metrik evaluasi
Deteksi dinilai dengan presisi, *recall*, dan mAP pada IoU 0,5 serta 0,5 sampai 0,95. Pencacahan dinilai dengan ACP, yaitu rata-rata $1 - |M - G|/G$ pada $n$ video, dengan $M$ hitungan algoritma dan $G$ hitungan manual. Acuan hitung manual pada tiap video diperoleh dengan mencatat jumlah buah pada bingkai pertama lalu menambahkan buah baru pada bingkai berikutnya. Penulis menyebut "visible kiwifruits" sebagai acuan, yaitu buah yang terlihat.

## Eksperimen dan Hasil
Deteksi diuji pada 123 citra uji dengan pembanding YOLOv4, YOLOv5, dan YOLOv6. Pencacahan diuji pada sepuluh video, termasuk video kebun nyata dan video sabuk pengangkut penyortiran.

Hasil deteksi (tabel pembanding pada makalah):

| Model | Presisi | *Recall* | mAP@0,5 | mAP@0,5:0,95 |
|---|---|---|---|---|
| YOLOv4 | 0,881 | 0,843 | 0,904 | 0,531 |
| YOLOv5 | 0,902 | 0,851 | 0,913 | 0,585 |
| YOLOv6 | 0,919 | 0,876 | 0,919 | 0,607 |
| KiwiDetector | 0,933 | 0,889 | 0,937 | 0,622 |

Hasil pencacahan pada sepuluh video (acuan manual, GT; hitungan model; galat; presisi hitungan):

| Video | GT | Hitungan model | Galat | Presisi |
|---|---|---|---|---|
| 1 | 485 | 577 | +92 | 0,810 |
| 2 | 1074 | 1306 | +232 | 0,784 |
| 3 | 712 | 843 | +131 | 0,816 |
| 4 | 441 | 521 | +80 | 0,819 |
| 5 | 1379 | 1691 | +312 | 0,774 |
| 6 | 293 | 348 | +55 | 0,812 |
| 7 | 491 | 587 | +96 | 0,804 |
| 8 | 313 | 369 | +56 | 0,821 |
| 9 | 1098 | 1349 | +251 | 0,771 |
| 10 | 604 | 721 | +117 | 0,806 |

ACP KiwiTracker adalah 0,802. Penulis menjelaskan bahwa hasil itu terjadi karena model menghitung kiwi secara berulang. Angka ribuan pada tabel ditulis tanpa pemisah pada makalah.

## Kelebihan dan Keterbatasan
Kelebihan: alur deteksi dan pelacakan sederhana, perbandingan detektor memakai empat metrik, dan hasil pencacahan disajikan per video beserta galatnya sehingga bias hitung berlebih terlihat jelas.

Keterbatasan yang dinyatakan penulis: kinerja kurang optimal pada video dengan latar rumit, terutama objek pengganggu seperti batang pohon, daun mati, dan pejalan kaki yang menyebabkan salah deteksi. Penulis mengusulkan menambah data dengan lebih banyak objek pengganggu atau memberi label tersendiri untuk objek itu.

Menurut pembacaan ringkasan ini: (a) seluruh galat bertanda positif dengan pola konsisten, sehingga ACP 0,802 mencerminkan penghitungan berlebih yang sistematis, bukan galat acak; (b) pembagian data citra tidak dijelaskan terpisah per video atau per sumber, sehingga kemungkinan kebocoran antara citra latih dan uji tidak dapat dinilai; (c) video pencacahan tidak dipastikan terpisah dari data latih; (d) satu video adalah sabuk pengangkut yang tidak sebanding dengan kebun; (e) tidak ada pembanding pelacak lain dan tidak ada analisis galat penyebab pergantian ID.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan: deteksi per bingkai, prediksi Kalman, pencocokan Hungarian berbasis jarak Euklides dan IoU, dan penghitungan ID unik. Hitungan tidak dilaporkan per kelas; hanya satu kelas buah kiwi. Acuan hitung adalah hitung manual pada video (buah yang terlihat), bukan hasil panen dan bukan hitung lapangan pada pohon.

Untuk pencacahan tandan sawit multi-sisi, makalah ini hanya memberi gambaran pelacakan dalam satu urutan video yang kontinu. Tidak ada mekanisme penyatuan identitas lintas sisi pohon, dan pola penghitungan berlebih pada Tabel hasil menunjukkan bahwa pelacak yang bergantung pada kesinambungan gerak cenderung menciptakan ID baru. Pola ini relevan sebagai peringatan, tetapi penyebabnya tidak dianalisis pada makalah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `xia2024kiwifruit`.

Xia, Nguyen, dan Yan (2024) mengusulkan KiwiDetector (YOLOv7) dan KiwiTracker (filter Kalman dan pencocokan Hungarian) untuk pencacahan kiwi dari video. KiwiDetector mencapai mAP@0,5 sebesar 0,937 pada 123 citra uji, dan KiwiTracker mencapai ACP 0,802 pada sepuluh video terhadap hitung manual, dengan hitungan model selalu lebih besar daripada acuan.

Catatan verifikasi data: Angka deteksi (0,937; 0,622; dan perbandingan YOLOv4 sampai YOLOv6) tertulis pada tabel perbandingan model dan kesimpulan; angka pembagian data (1.500, 1.885, 1.516, 246, 123) pada Bagian 2. Angka hitungan per video dan ACP 0,802 tertulis pada tabel hasil pencacahan dan Bagian 3.2. Penomoran tabel pada teks tidak konsisten (teks merujuk Tabel 2 dan 3, sedangkan tabel diberi label 1 dan 2). Teks ekstraksi terbaca utuh. Lokasi, kultivar, dan resolusi video tidak dilaporkan; sumber data adalah unduhan internet sehingga kondisi akuisisi tidak dapat diverifikasi.
