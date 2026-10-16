# Fruit Detection and Counting in Apple Orchards Based on Improved Yolov7 and Multi-Object Tracking Methods

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hu2023fruit` |
| Judul asli | Fruit Detection and Counting in Apple Orchards Based on Improved Yolov7 and Multi-Object Tracking Methods |
| Penulis | Hu, Jing; Fan, Chuang; Wang, Zhoupu; Ruan, Jinglin; Wu, Suyin |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [hu2023fruit.pdf](../pdf/hu2023fruit.pdf)
- DOI resmi: https://doi.org/10.3390/s23135903

## Gambaran Umum
Makalah ini (*Sensors* 2023, 23, 5903) mengusulkan pendeteksian dan pencacahan apel pada video dengan dua komponen. Komponen pertama adalah YOLOv7 yang diberi mekanisme atensi (CBAM atau *coordinate attention*, CA) di antara tulang punggung dan kepala jaringan. Komponen kedua adalah pelacakan multi-objek berjenjang (*cascade*) bergaya SORT yang memakai fitur penampilan SURF, bukan jaringan konvolusi, dengan filter Kalman dan jarak Mahalanobis untuk gerak serta jarak kosinus untuk penampilan.

Data deteksi berjumlah 4.246 citra apel yang dikumpulkan dari dataset publik dan citra daring, dibagi 80% latih dan 20% validasi. YOLOv7 dengan CA (disebut Yolov7t-CA) mencapai mAP@0,5 0,913 dan F1 0,85, dibandingkan 0,873 dan 0,83 untuk YOLOv7 dasar. Pada tiga video uji dengan total 290 apel hasil hitung manual, metode pelacakan yang diusulkan menghitung 310 apel dengan MAE gabungan 0,064, sedangkan SORT menghitung 373 (MAE 0,286), Cascade-SORT 333 (0,148), dan YOLOv7 tanpa pelacakan 495 (0,706).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis mengaitkan kebutuhan prakiraan hasil panen dengan penjualan buah daring yang bersifat pra-penjualan, sehingga jumlah panen tahunan perlu diketahui. Jumlah buah juga dipandang sebagai tolok ukur produktivitas dan efisiensi praktik pertanian. Penulis membedakan pencacahan berbasis deteksi dan berbasis regresi, dan menyatakan yang pertama umumnya lebih baik menurut penelitian terkini.

Metode deteksi buah klasik berbasis warna, bentuk, atau tekstur gagal pada perubahan cahaya, latar kompleks, dan cuaca. Model berbasis CNN efektif tetapi terbatas oleh penutupan dan ketidakmiripan antar-buah sejenis. Selain itu, deteksi saja pada video menimbulkan penghitungan ganda karena buah yang sama terdeteksi di banyak bingkai. DeepSORT memperbaiki ekstraksi penampilan dengan CNN tetapi kecepatan keseluruhan dibatasi kompleksitas model, dan pendekatan gabungan deteksi-penampilan memerlukan data video berlabel yang sulit dikumpulkan.

## Ide Utama
Ide utamanya ada dua. Pertama, atensi hibrida (CBAM dan CA), yang terinspirasi mekanisme atensi *Vision Transformer*, ditambahkan pada YOLOv7 agar fokus pada buah dan menekan latar. Kedua, karena penampilan buah yang sama berubah sangat sedikit dalam gerak antarbingkai yang singkat, ekstraktor fitur klasik SURF dianggap cukup dan jauh lebih cepat daripada CNN. Pelacak berjenjang menggabungkan jarak gerak (Mahalanobis dengan prediksi Kalman) dan jarak penampilan (kosinus pada deskriptor SURF), dengan cadangan IoU dan penanda masa hidup lintasan untuk menangani penutupan oleh daun.

Identitas buah dijaga antarbingkai dalam satu video. Makalah tidak membahas penyatuan identitas antar-video atau antar-sisi pohon.

## Cara Kerja Langkah demi Langkah
### 1. Data
Seluruh data apel berasal dari dataset publik atau citra bebas di internet: segmen apel dari dataset buah tropis (Pawara dkk.) dan apel berkualitas baik dari dataset penilaian mutu buah (Ismail dan Malik). Apel buruk dibuang karena jarang pada musim panen. Citra dapat diambil di luar atau di dalam ruangan dengan pencahayaan berbeda, dengan saling menutup dan terpotong di tepi. Hasil akhirnya 4.246 citra, dibagi 80% latih dan 20% validasi. Karena sebagian citra tak berlabel, model YOLOv7 yang diubah pertama dilatih pada data berlabel, dipakai menginferensi citra tak berlabel, dan LabelImg dipakai untuk anotasi ulang citra berlatar kompleks. Kultivar, lokasi, dan sensor tidak dilaporkan.

### 2. Augmentasi
Augmentasi mencakup pembalikan acak, kecerahan acak, MixUp, dan Mosaic. Citra diubah ke 640 x 640 piksel dengan rasio aspek dijaga melalui pengisian blok abu-abu.

### 3. Detektor YOLOv7 dengan atensi
CBAM menggabungkan atensi kanal (struktur mirip SE) dan atensi spasial. CA menyandikan hubungan kanal dan dependensi jarak jauh dengan informasi posisi melalui pengumpulan terarah, konvolusi 1 x 1, dan unit residu. Atensi diletakkan antara tulang punggung dan kepala, dan jaringan menghasilkan prediksi pada tiga skala. Tiga varian dibandingkan: YOLOv7, YOLOv7 dengan CBAM, dan YOLOv7 dengan CA. Pelatihan memakai transfer belajar dari bobot MS COCO, AutoAnchor, 300 epoch, ukuran batch 32, laju belajar awal 0,01 dengan penjadwalan kosinus hingga 0,0001, pemanasan 20 epoch, momentum 0,937, peluruhan bobot 0,0005, SGD, pada GPU T4 16 GB di Google Colab.

### 4. Ekstraksi penampilan SURF
Untuk setiap deteksi, SURF membangun ruang skala dan matriks Hessian untuk titik fitur invarian skala dan rotasi, dengan deskriptor berbasis respons wavelet Haar. Deskriptor akhir berupa matriks $N \times 128$ dengan $N$ jumlah titik fitur. Ambang Hessian adalah 400.

### 5. Prediksi gerak dan pencocokan berjenjang
Keadaan Kalman berdimensi 8 $(x_c, y_c, a, h, v_x, v_y, v_a, v_h)$ dengan gerak dianggap beraturan pada jarak pendek. Pencocokan gerak memakai jarak Mahalanobis, dan pencocokan penampilan memakai jarak kosinus antar matriks fitur SURF. Hasilnya tiga keadaan: lintasan tak cocok, deteksi tak cocok, dan lintasan cocok. Lintasan cocok diperbarui dengan filter Kalman kedua. Lintasan tak cocok diuji ulang dengan IoU (ambang `sort_iou_thresh` 0,7), lalu diberi penghitung masa hidup 5 bingkai untuk menampung penutupan penuh; bila cocok dalam 5 bingkai berikutnya, lintasan diaktifkan kembali, dan bila lebih dari 5 bingkai, lintasan dibuang dan dianggap selesai. Deteksi tak cocok menjadi lintasan baru. Parameter lain: `sort_max_age` 5 dan `sort_min_age` 3.

### 6. Pencacahan
Hitungan adalah jumlah lintasan yang dihasilkan pelacak pada video. Teks tidak memerinci aturan konfirmasi lintasan atau garis hitung.

## Eksperimen dan Hasil
Deteksi dievaluasi pada data validasi (teks tidak menyebut subset uji terpisah) dengan presisi, *recall*, F1, dan mAP dengan IoU 0,5. Dalam Tabel 2, kolom bertajuk "mAP@0.95" kemungkinan berarti mAP@0,5:0,95 (tidak dijelaskan). Pembanding eksternal adalah Yolov3 dari makalah Cascade-SORT (He dkk.), yang hanya mencantumkan presisi dan *recall* tertentu.

| Model | Presisi | *Recall* | mAP@0,5 | mAP@0,95 | F1 | Ukuran |
|---|---|---|---|---|---|---|
| Yolov7 | 0,864 | 0,809 | 0,873 | 0,634 | 0,83 | 12,3 M |
| Yolov7t-CBAM | 0,896 | 0,799 | 0,883 | 0,625 | 0,83 | 12,3 M |
| Yolov7t-CA | 0,924 | 0,816 | 0,913 | 0,638 | 0,85 | 12,1 M |
| Weak-Yolov3 (rujukan) | tidak ada | 0,766 | 0,661 | tidak ada | tidak ada | tidak ada |
| Strong-Yolov3 (rujukan) | tidak ada | 0,887 | 0,784 | tidak ada | tidak ada | tidak ada |

Catatan kolom: untuk dua baris Yolov3, kolom yang tersedia pada teks adalah *recall* dan mAP@0,5 dalam urutan kolom yang tercetak, yaitu kolom kedua dan ketiga setelah "Precision". Pembacaan ini mengikuti urutan nilai pada teks ekstraksi: (None, 0,766, 0,661, None, None, None).

Pencacahan dievaluasi pada tiga video dengan acuan hitung manual. MAE didefinisikan sebagai rerata galat relatif $\left| y^{(i)} - \hat{y}^{(i)} \right| / \hat{y}^{(i)}$ dengan $\hat{y}$ hitung manual.

| Video | Hitung manual | Metode | Hitungan | MAE |
|---|---|---|---|---|
| 0 | 134 | SORT | 185 | 0,380 |
| 0 | | Cascade-SORT | 159 | 0,186 |
| 0 | | Metode usulan | 148 | 0,104 |
| 0 | | YOLOv7 saja | 241 | 0,798 |
| 1 | 92 | SORT | 113 | 0,228 |
| 1 | | Cascade-SORT | 106 | 0,152 |
| 1 | | Metode usulan | 99 | 0,076 |
| 1 | | YOLOv7 saja | 157 | 0,706 |
| 2 | 64 | SORT | 75 | 0,171 |
| 2 | | Cascade-SORT | 68 | 0,062 |
| 2 | | Metode usulan | 63 | 0,016 |
| 2 | | YOLOv7 saja | 97 | 0,426 |
| Semua | 290 | SORT | 373 | 0,286 |
| Semua | | Cascade-SORT | 333 | 0,148 |
| Semua | | Metode usulan | 310 | 0,064 |
| Semua | | YOLOv7 saja | 495 | 0,706 |

Penulis menyatakan perbaikan MAE keseluruhan sebesar 0,222 terhadap SORT, 0,642 terhadap YOLOv7 saja, dan 0,084 terhadap Cascade-SORT (selisih ini cocok dengan angka tabel). Mereka juga mencatat bahwa performa tidak stabil di antara video karena kesulitan pencahayaan dan penutupan berbeda.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: atensi CA menaikkan mAP@0,5 dan F1 tanpa menambah ukuran model secara berarti (12,1 M parameter, lebih kecil daripada 12,3 M dasar); SURF menghindari biaya CNN untuk fitur penampilan; dan pelacakan menurunkan penghitungan ganda dibandingkan YOLOv7 saja yang menghitung 495 untuk 290 acuan.

Keterbatasan yang dinyatakan penulis: hanya dua mekanisme atensi yang diuji; hasil pelacakan tidak stabil antar-video; metrik pelacakan seperti *ID switch* dan MOTA belum dipakai; dan kecepatan serta ukuran model perlu dikurangi untuk GPU tepi (pemangkasan dan kompresi direncanakan). Mereka juga berencana membangun dataset video buah.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Dataset deteksi bukan citra kebun dari video uji: data berasal dari sumber publik dan daring (sebagian dalam ruangan), sedangkan sumber ketiga video uji tidak diuraikan. Evaluasi deteksi memakai data validasi tanpa subset uji yang disebut terpisah. Hitungan metode usulan masih melebihi hitung manual (310 terhadap 290), dan tiga video merupakan sampel kecil. Pernyataan peningkatan 0,6% presisi dan 0,4% mAP pada Bagian 4 tidak cocok dengan Tabel 2 (mAP@0,5 0,913 terhadap 0,873 untuk YOLOv7 dan 0,883 untuk CBAM), sehingga basis perbandingan pada kalimat itu tidak jelas. Tidak dijelaskan pula apakah SORT dan Cascade-SORT memakai detektor yang sama dengan metode usulan. Tidak ada hitungan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam satu video dengan pelacakan berbasis deteksi: Kalman, Mahalanobis, jarak kosinus pada deskriptor SURF, cadangan IoU, dan penghitung masa hidup lintasan 5 bingkai. Hitungan dilaporkan sebagai total apel per video (satu kelas), bukan per kelas. Acuannya adalah hitung manual pada video, bukan panen dan bukan anotasi citra.

Untuk pencacahan tandan sawit multi-sisi, penggunaan deskriptor penampilan klasik berbiaya rendah dapat dijadikan pembanding bagi fitur CNN pada pencocokan identitas. Namun, SURF dipilih dengan asumsi penampilan buah hampir tidak berubah antarbingkai berdekatan; pada pengambilan dari sisi pohon yang berbeda, tampilan tandan berubah besar, sehingga asumsi itu tidak dapat dipindahkan tanpa pengujian.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hu2023fruit`.

Hu dkk. (2023) menggabungkan YOLOv7 beratensi CA dengan pelacakan multi-objek berjenjang berbasis fitur penampilan SURF untuk mencacah apel pada video. Detektor mencapai mAP@0,5 0,913 dan F1 0,85 pada data validasi, dan pada tiga video uji pelacak menghitung 310 apel terhadap 290 hasil hitung manual (MAE 0,064), dibandingkan 495 apel bila hanya YOLOv7 tanpa pelacakan.

Catatan verifikasi data: Angka deteksi ada pada Tabel 2 (Seksi 3.1) dan angka pencacahan pada Tabel 3 (Seksi 3.2); selisih MAE 0,222, 0,642, dan 0,084 ada pada Seksi 4. Abstrak menyebut peningkatan mAP 4% dan F1 0,02, konsisten dengan Tabel 2 (0,913 terhadap 0,873; 0,85 terhadap 0,83). Baris Yolov3 pada Tabel 2 terekstraksi dengan urutan kolom yang tidak pasti; nilai itu dikutip dari makalah lain dan sebaiknya diperiksa pada PDF bila akan dikutip. Kolom "mAP@0.95" kemungkinan bermakna mAP@0,5:0,95. Jumlah citra uji, sumber, resolusi, dan panjang video, serta kecepatan pemrosesan tidak dilaporkan. Beberapa persamaan (Persamaan 1, 3, 4) terekstraksi rusak sehingga rumusnya hanya diringkas dari uraian teks.
