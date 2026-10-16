# Research on UAV Online Visual Tracking Algorithm based on YOLOv5 and FlowNet2 for Apple Yield Inspection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2022research` |
| Judul asli | Research on UAV Online Visual Tracking Algorithm based on YOLOv5 and FlowNet2 for Apple Yield Inspection |
| Penulis | Wang, Shaopeng; Zhang, Xiaodong; Shen, Haiming; Tian, Minxuan; Li, Mingyang |
| Tahun | 2022 |
| Venue | Proceedings of the 4th Wrc Symposium on Advanced Robotics and Automation 2022 Wrc Sara 2022 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wang2022research.pdf](../pdf/wang2022research.pdf)
- DOI resmi: https://doi.org/10.1109/wrcsara57040.2022.9903925

## Gambaran Umum
Makalah prosiding (WRC Symposium on Advanced Robotics and Automation 2022, Beijing) ini mengusulkan algoritma pelacakan daring untuk estimasi hasil apel dari video yang direkam *UAV* (pesawat tanpa awak). Kerangkanya adalah pelacakan-oleh-deteksi (*tracking-by-detection*): YOLOv5 mendeteksi apel, FlowNet2 menghitung aliran optik (*optical flow*) untuk memprediksi posisi apel pada bingkai berikutnya, dan algoritma Hungaria mencocokkan posisi prediksi dengan posisi deteksi. Apel yang tidak cocok pada deteksi baru dianggap apel baru dan menambah hitungan.

Data berasal dari sebagian citra dataset MinneApple dan citra yang direkam dalam eksperimen simulasi, yakni apel tiruan (*model apples*) yang digantung pada pohon di luar ruangan dan direkam dengan DJI Mavic 3. Penulis melaporkan presisi deteksi sekitar 85% (abstrak: 85,5%), presisi pencacahan rerata 90,39% pada 9 video, dan kecepatan sekitar 20 FPS pada GPU NVIDIA GeForce 940MX 2 GB.

Perlu dicatat bahwa evaluasi pencacahan dilakukan pada apel tiruan dalam skenario simulasi, bukan pada kebun komersial dengan buah asli.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan jumlah buah apel membantu pengelolaan kebun, dan pemeriksaan rutin dengan robot terbang dipandang penting karena budidaya apel di Tiongkok masih didominasi tenaga manual. Penulis menilai penelitian deteksi apel sebelumnya menyasar kondisi ideal (jarak dekat dan oklusi ringan) dan sebagian besar algoritmanya tidak berjalan waktu-nyata pada robot inspeksi. Citra dari UAV memuat apel kecil, tertutup daun, dan mengalami perubahan cahaya kuat.

Untuk pelacakan dan pencacahan, penulis menyebut metode terdahulu bersifat luring: penghitungan per citra tunggal dengan klasifikasi gugus apel, pencocokan antarbingkai melalui rekonstruksi 3D yang memakan waktu, serta estimasi jumlah langsung dari satu citra dengan jaringan berbasis VGG16 yang tidak berlaku untuk urutan video. Kecepatan terbang UAV yang tinggi membuat perpindahan target antarbingkai besar.

## Ide Utama
Gagasannya adalah memprediksi posisi tiap apel pada bingkai berikutnya dengan aliran optik tingkat piksel, tanpa membangun satu model pelacak per apel (yang tidak praktis untuk banyak apel). Rerata aliran optik di dalam kotak pembatas dipakai sebagai gerak titik tengah kotak. Posisi prediksi lalu dicocokkan dengan hasil deteksi pada bingkai baru melalui pencocokan graf bipartit. Dengan prediksi gerak ini, apel yang sementara tertutup tetap dapat dipertahankan identitasnya dan tidak dihitung dua kali saat muncul kembali.

## Cara Kerja Langkah demi Langkah
```
 Bingkai i  -> YOLOv5 -> posisi apel
 Bingkai i,i+1 -> FlowNet2CS -> aliran optik -> posisi prediksi i+1
 Bingkai i+1 -> YOLOv5 -> posisi deteksi
 Prediksi vs deteksi -> Hungaria -> pembaruan antrean dan hitungan
```

### 1. Metode inspeksi UAV
UAV dengan kamera RGB dipakai sebagai platform. Untuk pohon tinggi dan rapat, citra diambil dari atas ke bawah. Untuk pohon pendek dengan lebar tanam besar, UAV terbang di tengah lorong pohon dan mengambil citra dari arah horizontal. Masalah dipecah menjadi tiga: deteksi apel kecil dan tertutup, estimasi posisi pada bingkai berurutan, serta pencocokan dan penghitungan.

### 2. Deteksi dengan YOLOv5s
Model inti adalah YOLOv5s (varian YOLOv5s dan YOLOv5s6 dibandingkan) dengan inisialisasi bobot pralatih COCO. Augmentasi memakai oklusi acak dan *mosaic*. Penulis membandingkan ukuran masukan 640 dan 1280 piksel.

### 3. Estimasi posisi dengan aliran optik
Metode Farneback tradisional memerlukan sekitar 100 ms per bingkai sehingga tidak memenuhi syarat waktu-nyata. Dipilih modul FlowNet2CS (bagian dari FlowNet2). Rerata aliran optik pada seluruh piksel dalam kotak pembatas dipakai sebagai perpindahan titik tengah, sehingga posisi prediksi pada waktu $t+1$ sama dengan posisi pada waktu $t$ ditambah rerata aliran tersebut.

### 4. Pencocokan dan strategi penghitungan
Posisi prediksi dan posisi deteksi dimodelkan sebagai dua himpunan simpul pada graf bipartit. Sebuah pasangan dianggap kandidat bila IoU kotak prediksi dan kotak deteksi melebihi ambang, atau bila kedua kotak tidak beririsan tetapi jarak antar titik tengah kurang dari ambang. Teks ekstraksi memuat nilai ambang dalam rumus yang rusak (tampak "80%" dan "30"), sehingga nilai dan satuan pastinya tidak dapat dipastikan. Pencocokan maksimum diselesaikan dengan algoritma Hungaria.

Aturan penghitungan: hitungan awal diinisialisasi dari bingkai pertama; apel yang cocok diperbarui posisinya; apel prediksi yang tidak cocok mempertahankan posisi prediksi dan dihapus bila tidak muncul pada 10 bingkai berturut-turut atau keluar dari bingkai; deteksi baru yang tidak cocok ditambahkan ke antrean dan menaikkan hitungan.

## Eksperimen dan Hasil
Dataset berisi 1.790 citra inspeksi simulasi (62,2% diambil dalam eksperimen, sisanya dari MinneApple) dengan 28.084 apel berlabel, dibagi 1.211 citra latih dan 579 citra uji, ditambah 9 video untuk verifikasi pelacakan dan estimasi hasil. Apel tiruan digantung pada pohon luar ruangan menyerupai kondisi tumbuh, dan direkam dengan DJI Mavic 3.

Hasil deteksi (Tabel I, hasil ekstraksi teks):

| Model | Ukuran masukan | Presisi | Recall | mAP@0,5 | mAP@0,5:0,95 | Kecepatan |
|---|---|---|---|---|---|---|
| YOLOv5s | 640 | 0,842 | 0,783 | 0,867 | 0,491 | 32 ms |
| YOLOv5s | 1280 | 0,853 | 0,827 | 0,897 | 0,531 | 107 ms |
| YOLOv5s6 | 640 | 0,853 | 0,783 | 0,864 | 0,469 | 35 ms |
| YOLOv5s6 | 1280 | 0,855 | 0,826 | 0,902 | 0,534 | 132 ms |

Penulis menyebut akurasi deteksi sebelumnya pada MinneApple hanya 77% sedangkan model ini mencapai sekitar 85%. Abstrak menyatakan 11% lebih tinggi; selisih sederhana 85,5 dikurangi 77 adalah 8,5 poin, sehingga angka 11% tidak dapat direproduksi dari teks. Penulis juga menyatakan bahwa model mendeteksi apel yang tidak dilabeli manual sehingga angka tabel dapat meremehkan kinerja.

Hasil pencacahan pada 9 video (Tabel II):

| Video | Acuan | Hitungan | Presisi |
|---|---|---|---|
| 1 | 29 | 27 | 93,10% |
| 2 | 30 | 27 | 90,00% |
| 3 | 31 | 29 | 93,55% |
| 4 | 20 | 17 | 85,00% |
| 5 | 15 | 16 | 93,33% |
| 6 | 40 | 45 | 87,50% |
| 7 | 33 | 33 | 100,00% |
| 8 | 35 | 44 | 74,29% |
| 9 | 31 | 32 | 96,77% |

Presisi rerata 90,39% dengan simpangan baku 7,12%. Pemeriksaan sederhana pada baris tabel menunjukkan "presisi" setara dengan satu dikurangi selisih mutlak hitungan terhadap acuan, dibagi acuan (misalnya video 8: 1 − 9/35 = 74,29%). Ukuran ini bukan presisi dalam arti deteksi dan tidak membedakan kelebihan dari kekurangan hitung. Waktu analisis sekitar 50 ms per bingkai (20 FPS).

## Kelebihan dan Keterbatasan
Kelebihan: pipeline waktu-nyata yang ringan dan berjalan pada GPU 2 GB, penanganan oklusi sementara melalui prediksi gerak, dan strategi penghitungan yang eksplisit (aturan hapus setelah 10 bingkai). Keterbatasan yang dinyatakan penulis: apel berpenyakit dan hama belum dimasukkan dalam dataset, dan metode belum dipindahkan ke robot pemetik. Penulis juga menyatakan angka deteksi mungkin meremehkan kinerja karena apel yang tidak dilabeli ikut terdeteksi.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pengujian pencacahan memakai apel tiruan yang digantung, dengan hanya 9 video dan acuan 15 sampai 40 apel per video, sehingga generalisasi ke kebun nyata tidak terbukti. Metrik "presisi" memungkinkan kesalahan lebih dan kurang saling meniadakan antarvideo, dan galat besar tampak pada video 8 (44 terhitung terhadap 35 acuan). Teks Seksi III-B menyebut model YOLOv5s6 pada masukan 640 memiliki akurasi 85,8% dan 32 ms, tetapi Tabel I mencatat 0,853 dan 35 ms untuk kombinasi itu (0,858 dan 32 ms tidak ada pada tabel), sehingga model terpilih dan angkanya tidak konsisten. Tidak ada pembanding pelacak lain (misalnya SORT atau DeepSORT) dan tidak ada ablasi aliran optik. Hasil dilaporkan pada GPU 940MX yang dianggap mewakili platform tertanam, tanpa uji pada perangkat UAV sebenarnya.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat berulang pada bingkai video dengan mekanisme pelacakan-oleh-deteksi, yaitu prediksi posisi dari aliran optik dan pencocokan Hungaria berdasarkan IoU atau jarak. Identitas apel dipertahankan sepanjang video, dan hitungan bertambah hanya bila muncul deteksi tanpa pasangan. Hitungan tidak dilaporkan per kelas; judul menyinggung apel sehat dan berpenyakit pada kontribusi, tetapi hasil yang dilaporkan hanyalah satu hitungan apel. Acuan hitung adalah jumlah apel per video yang disebut ground truth; apakah dihitung manual dari apel tiruan yang digantung atau dari anotasi video tidak dinyatakan secara eksplisit.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan prediksi posisi untuk mempertahankan identitas saat oklusi sementara, aturan penghapusan setelah beberapa bingkai tanpa pasangan, serta pencocokan bipartit. Syaratnya adalah adanya gerak kontinu antarbingkai. Untuk citra dari sisi pohon yang terpisah, prediksi aliran optik tidak berlaku sehingga pencocokan harus bersandar pada kriteria lain.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wang2022research`.

Wang dkk. mengusulkan algoritma pelacakan daring untuk estimasi hasil apel dari video UAV. Kerangkanya menggabungkan deteksi YOLOv5, prediksi posisi dengan aliran optik FlowNet2, dan pencocokan Hungaria. Pada 9 video apel tiruan yang digantung pada pohon, presisi pencacahan rerata yang dilaporkan adalah 90,39% (simpangan baku 7,12%) dengan kecepatan sekitar 20 FPS pada GPU 2 GB.

Catatan verifikasi data: Angka deteksi berasal dari Tabel I, angka pencacahan dari Tabel II, dan jumlah dataset (1.790 citra, 28.084 apel, 1.211 latih, 579 uji, 9 video) dari Seksi III-A. Rumus ambang pencocokan pada ekstraksi teks rusak sehingga nilai ambang tidak dapat diverifikasi. Klaim "11% lebih tinggi daripada penelitian sebelumnya" pada abstrak tidak cocok dengan selisih sederhana (85,5 − 77 = 8,5 poin). Model terpilih pada teks (85,8%) tidak sama dengan nilai pada Tabel I. Beberapa nilai tabel terpecah pada ekstraksi (misalnya "0826"), dan pemetaan kolom disimpulkan dari urutan baris.
