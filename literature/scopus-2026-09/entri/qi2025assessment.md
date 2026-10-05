# Assessment of the tomato cluster yield estimation algorithms via tracking-by-detection approaches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qi2025assessment` |
| Judul asli | Assessment of the tomato cluster yield estimation algorithms via tracking-by-detection approaches |
| Penulis | Qi, Zhongxian; Zhang, Tianxue; Yuan, Ting; Zhou, Wei; Zhang, Wenqiang |
| Tahun | 2025 |
| Venue | Information Processing in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [qi2025assessment.pdf](../pdf/qi2025assessment.pdf)
- DOI resmi: https://doi.org/10.1016/j.inpa.2025.02.005

## Gambaran Umum

Makalah ini mengevaluasi algoritma estimasi hasil panen tandan tomat di rumah kaca dengan pendekatan pelacakan-berbasis-deteksi (*tracking-by-detection*). Penulis membangun set data pelacakan multi-objek (*multi-object tracking*, MOT) tandan tomat yang dibuka untuk umum, lalu membandingkan dua detektor (YOLOv8 dan RT-DETR) dan empat pelacak (SORT, DeepSort, ByteTrack, dan BotSort) pada tugas penghitungan tandan per baris tanam. Jumlah tandan dihitung dengan metode berbasis wilayah tetap pada bingkai, bukan dengan nilai ID maksimum.

Data direkam di Hongfu Agricultural Tomato Production Park, Distrik Daxing, Beijing, pada rumah kaca bergaya Belanda, memakai kamera OAK-D-Pro-W bersudut lebar pada kendaraan yang bergerak di rel dengan kecepatan sekitar 0,3 m/s. Terdapat 15 video (2023 sampai 2024, 720 × 1280 piksel, 30 fps) untuk uji pelacak dan 1.700 citra untuk detektor.

Hasil utama: pada AP@0,75 YOLOv8 mencapai 93,6% dan RT-DETR 94,9%. Dengan detektor RT-DETR, ByteTrack mencapai akurasi hitungan relatif rata-rata tertinggi (95,5%), sedangkan BotSort mencapai MOTA tertinggi (84,6%). Pelacak tanpa modul identifikasi ulang (*Re-Identification*, ReID), yaitu SORT dan ByteTrack, lebih tahan terhadap penurunan laju bingkai.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penghitungan tomat secara manual melelahkan dan memakan waktu, sedangkan estimasi hasil panen yang akurat penting bagi rantai pasok. Detektor modern dapat menemukan tandan, tetapi untuk penghitungan per baris tanam dibutuhkan asosiasi lintas bingkai agar tandan yang sama tidak dihitung berulang. MOT dengan strategi pelacakan-berbasis-deteksi memberi ID yang sama pada objek yang sama di bingkai berbeda, dan ID itu dapat dipakai sebagai dasar hitungan.

Penulis menyebut tiga kekosongan. Pertama, studi terdahulu lebih berfokus pada perbaikan keluaran detektor, dan belum ada analisis sistematis tentang tantangan serta batas berbagai pelacak di bidang pertanian. Kedua, tidak ada set data publik untuk menganalisis dampak detektor mutakhir terhadap pelacak pada penghitungan tandan buah. Ketiga, ada dua kesulitan spesifik: gangguan dari tandan pada baris latar belakang (hanya tandan pada baris yang sedang dihitung yang boleh dicacah), serta oklusi, kemiripan tampilan, dan cahaya matahari yang menyulitkan pelacak berbasis kemiripan penampilan.

## Ide Utama

Makalah ini bukan mengusulkan algoritma baru, melainkan penilaian empiris kombinasi detektor-pelacak pada satu skenario rumah kaca yang terstandar. Gagasan teknisnya adalah memisahkan pengaruh detektor dan pelacak, serta menguji ketahanan pelacak terhadap perubahan laju bingkai. Karena pelacak sering mengalami pertukaran ID (*identity switch*), nilai ID maksimum akan menaksir hitungan terlalu tinggi, sehingga penghitungan dilakukan dengan menghitung ID yang masuk ke wilayah tetap pada bingkai. Hanya tandan baris saat ini yang diberi anotasi dan dilatihkan, agar tandan latar belakang tidak dihitung.

## Cara Kerja Langkah demi Langkah

```
  Kamera pada kendaraan rel ──> video 30 fps
        │
   detektor (YOLOv8 atau RT-DETR) ──> kotak tandan
        │
   pelacak (SORT, DeepSort, ByteTrack, BotSort) ──> ID per tandan
        │
   hitungan berbasis wilayah tetap ──> jumlah tandan per video
```

### 1. Akuisisi data

Rumah kaca menanam tomat dengan jarak 1.600 mm antarbaris, sekitar 10 sampai 12 buah per tandan, dan sulur diturunkan berkala sehingga tandan pada fase berubah warna dan matang tersebar pada batang utama hingga rentang tinggi 1.400 mm. Kamera OAK-D-Pro-W dipilih karena sudut pandangnya lebar (horizontal 95 derajat dan vertikal 70 derajat), sedangkan Realsense atau Azure Kinect dinilai sulit mencakup tandan pada baris sempit. Kamera dipasang pada kendaraan platform yang melaju sepanjang rel dengan kecepatan sekitar 0,3 m/s. Penulis mengumpulkan 15 video mentah. Untuk detektor, video diambil bingkainya setiap 15 bingkai hingga diperoleh 1.700 citra, dibagi acak 8:2 menjadi data latih dan uji, dengan 9.068 instans berlabel. Varietas tomat tidak dilaporkan.

### 2. Set data pelacakan

Video dianotasi semi-otomatis dengan DarkLabel (Tabel 1). Lima belas video memuat 1.230 sampai 3.572 bingkai per video, dan kolom "Tomato clusters" berisi 52 sampai 141 tandan per video. Jumlah total bingkai (40.526) dan total tandan (1.614) dihitung dari kolom tabel itu dan tidak dinyatakan di teks. Pengekstrak fitur DeepSort dilatih terpisah memakai kotak urutan dari video set deteksi.

### 3. Detektor

YOLOv8 mewakili detektor satu tahap berbasis CNN dengan tulang punggung CNN, *neck* multiskala, kepala klasifikasi dan regresi, serta pascapemrosesan NMS. RT-DETR mewakili detektor berbasis *transformer* dengan pengodean hibrida, pemilihan kueri sadar-IoU, dan tanpa NMS. Ukuran model, hiperparameter pelatihan, dan jumlah epoch tidak dilaporkan pada teks.

### 4. Pelacak

SORT memakai filter Kalman dan asosiasi IoU dengan algoritma Hungarian. DeepSort menambahkan fitur penampilan CNN. ByteTrack mengasosiasikan kotak berkeyakinan tinggi terlebih dahulu, lalu mengasosiasikan kotak berkeyakinan rendah dengan lintasan yang belum berpasangan, tanpa fitur penampilan. BotSort memakai ekstraktor penampilan FastID, kompensasi gerak kamera, dan pencocokan dua tahap yang menggabungkan IoU dan ReID.

### 5. Metode penghitungan dan metrik

Wilayah tetap (masker) ditentukan pada bingkai. Sebuah tandan dihitung bila koordinat sudut kiri atas kotaknya memasuki wilayah itu, dan jumlah ID yang pernah masuk ke wilayah menjadi estimasi hitungan. Metrik detektor adalah AP pada IoU 0,5, 0,5:0,95, dan 0,75. Metrik pelacak adalah MOTA dan presisi relatif $P_{rel} = (1 - |N_{actual} - N_{est}| / N_{actual}) \times 100\%$ per video, dirata-ratakan atas 15 video. Pada Lampiran, IDF1 dilaporkan untuk video VT4.

## Eksperimen dan Hasil

Detektor (Tabel 2):

| Model | AP@0,5 | AP@0,5:0,95 | AP@0,75 |
|---|---|---|---|
| YOLOv8 | 98,5% | 80,4% | 93,6% |
| RT-DETR | 98,5% | 81,2% | 94,9% |

Pada IoU 0,5 kedua model setara, dan RT-DETR unggul pada ambang yang lebih ketat. Secara kualitatif, YOLOv8 membaca satu tandan pada fase berubah warna sebagai dua objek dan memasukkan tomat dari baris latar ke hitungan baris saat ini, sedangkan RT-DETR menghindari kedua kesalahan itu pada contoh yang ditampilkan.

Kombinasi detektor-pelacak pada 30 fps (Tabel 3; rerata atas 15 video):

| Detektor | SORT MOTA / $P_{rel}$ | DeepSort MOTA / $P_{rel}$ | ByteTrack MOTA / $P_{rel}$ | BotSort MOTA / $P_{rel}$ |
|---|---|---|---|---|
| YOLOv8 | 80,1% / 94,0% | 82,1% / 91,1% | 81,4% / 94,4% | 82,0% / 93,5% |
| RT-DETR | 82,3% / 94,9% | 84,3% / 87,6% | 83,5% / 95,5% | 84,6% / 95,2% |

Pada 30 fps, pelacak ber-ReID (DeepSort dan BotSort) memperoleh MOTA lebih tinggi. Kombinasi RT-DETR dan ByteTrack memberi $P_{rel}$ tertinggi (95,5%). Penulis menjelaskan bahwa $P_{rel}$ DeepSort pada YOLOv8 lebih tinggi daripada pada RT-DETR kemungkinan karena positif palsu YOLOv8 menghasilkan lebih banyak ID sehingga selisih hitungan akhir mengecil. BotSort memberi koefisien determinasi $R^2$ = 0,95 antara hitungan pelacak dan hitungan manual pada 15 video (Gambar 6b).

Sensitivitas terhadap laju bingkai pada video VT4 (GT = 120 tandan; Tabel A.1):

| FPS | Pelacak | MaxID | Hitungan | IDF1 | MOTA |
|---|---|---|---|---|---|
| 30 | SORT | 197 | 117 | 89,7% | 82,6% |
| 30 | DeepSort | 163 | 107 | 86,2% | 85,4% |
| 30 | ByteTrack | 187 | 117 | 91,1% | 85,0% |
| 30 | BotSort | 198 | 117 | 91,4% | 85,7% |
| 10 | SORT | 168 | 113 | 86,3% | 76,0% |
| 10 | DeepSort | 2.479 | 28 | 30,4% | 18,8% |
| 10 | ByteTrack | 178 | 112 | 90,2% | 82,1% |
| 10 | BotSort | 607 | 195 | 74,4% | 64,6% |

Pada 15 fps, ByteTrack mencatat MOTA 83,9% dan hitungan 114, sedangkan DeepSort 81,2% dan 114, SORT 79,4% dan 112, serta BotSort 83,8% dan 117. Penurunan terbesar terjadi pada DeepSort dan BotSort. Nilai MaxID jauh melebihi jumlah GT pada semua pelacak, misalnya 197 untuk SORT pada 30 fps dibanding 120 tandan, sehingga pemakaian ID maksimum sebagai hitungan akan menaksir terlalu tinggi.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: set data MOT tandan tomat dibuka untuk umum; dua detektor dan empat pelacak dibandingkan pada data yang sama; ada analisis sensitivitas terhadap laju bingkai; metode hitung berbasis wilayah mengatasi pertukaran ID; dan skenario rumah kaca yang terstandar memudahkan penerapan.

Keterbatasan yang dinyatakan penulis: kecepatan platform yang bervariasi dapat memengaruhi kualitas citra, detektor, dan prediksi Kalman pada pelacak; RT-DETR lebih lambat daripada YOLOv8 meskipun dinilai cukup untuk deteksi waktu nyata; ReID dapat membingungkan tandan yang berpose dan tingkat kematangan serupa; dan manfaat ReID serta kompensasi gerak kamera terbatas pada lintasan lurus.

Menurut pembacaan ringkasan ini: (a) hanya satu rumah kaca dan satu jalur rel yang diuji, sehingga generalisasi ke kebun terbuka atau pohon tinggi tidak terjawab; (b) analisis sensitivitas laju bingkai hanya pada satu video (VT4); (c) tidak ada pengulangan, simpangan baku antarlatihan, atau uji signifikansi pada perbedaan 95,5% terhadap 95,2% dan 94,9%; (d) hitungan berbasis wilayah tetap bergantung pada pengaturan wilayah dan arah gerak kamera, dan pengaruh parameter wilayah tidak dievaluasi; (e) hitungan hanya total tandan, tanpa kelas kematangan, meskipun kematangan disebut sebagai pekerjaan lanjutan; (f) satu lintasan tiap baris tanam, sehingga tandan yang terlihat dari baris sebelah atau dari sisi sebaliknya tidak ditangani.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat berulang pada bingkai video berurutan, dengan mekanisme pelacakan-berbasis-deteksi (MOT) ditambah penghitungan berbasis wilayah tetap sebagai koreksi atas pertukaran ID. Identitas ditentukan oleh asosiasi 2D antarbingkai (filter Kalman, IoU, dan pada sebagian pelacak ReID), bukan oleh geometri 3D atau pencocokan multi-pandang. Makalah menunjukkan bahwa ID maksimum menaksir hitungan terlalu tinggi (MaxID 163 sampai 198 untuk 120 tandan pada VT4, 30 fps), dan bahwa pelacak ber-ReID makin mudah melonjak jumlah ID-nya pada laju bingkai rendah (MaxID DeepSort 2.479 pada 10 fps). Makalah tidak menangani buah yang terlihat dari sisi tanaman yang berbeda.

Hitungan tidak dilaporkan per kelas. Acuan hitungnya adalah jumlah tandan per video (kolom "Tomato clusters" pada Tabel 1 dan GT pada Tabel A.1) dan anotasi video semi-otomatis. Cara perolehan hitungan GT, apakah dari anotasi video atau penghitungan lapangan, tidak dijelaskan secara eksplisit; sumbernya tampaknya penghitungan manual video, tetapi teks menyebutnya "manual vision". Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: pelacak tanpa ReID (ByteTrack atau SORT) lebih tahan terhadap variasi laju bingkai, hitungan berbasis wilayah lebih baik daripada ID maksimum, dan penting memberi anotasi hanya pada objek target agar objek latar tidak ikut dihitung. Pelacakan ini hanya berlaku untuk urutan video kontinu pada satu sisi dan tidak menggabungkan sisi pohon yang berbeda. Hal itu merupakan kesimpulan ringkasan ini.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `qi2025assessment`.

Qi dkk. (2025) membangun set data MOT publik untuk tandan tomat rumah kaca (15 video, 720 × 1280 piksel, 30 fps) dan membandingkan detektor YOLOv8 dan RT-DETR serta pelacak SORT, DeepSort, ByteTrack, dan BotSort dengan penghitungan berbasis wilayah tetap. Dengan RT-DETR sebagai detektor (AP@0,75 94,9%), ByteTrack menghasilkan presisi hitungan relatif rata-rata tertinggi (95,5%) dan BotSort MOTA tertinggi (84,6%); pelacak tanpa ReID (SORT dan ByteTrack) lebih tahan terhadap penurunan laju bingkai, sedangkan DeepSort dan BotSort menurun tajam pada 10 fps.

Catatan verifikasi data: AP detektor ada di Tabel 2 dan abstrak. MOTA dan $P_{rel}$ untuk delapan kombinasi ada di Tabel 3. MOTA 84,6% dan hitungan 95,5% juga tertulis di abstrak dan kesimpulan. Tabel 1 memuat jumlah bingkai, instans, dan tandan tiap video. Tabel A.1 hanya mencakup video VT4. Jumlah 1.700 citra, rasio 8:2, dan 9.068 instans ada di Bagian 2.1. Nilai $R^2$ 0,95 ada di Bagian 3.2. Jumlah total bingkai dan total tandan dihitung dalam entri ini dari Tabel 1. Nilai 8:2 untuk pelatihan deteksi tidak menyebut set validasi. Ukuran model, hiperparameter, varietas tomat, dan perolehan hitungan GT tidak dilaporkan. Pembacaan Tabel 1 dan Tabel A.1 berasal dari ekstraksi teks yang berbentuk daftar angka per baris, sehingga pengelompokan kolomnya merupakan penafsiran.
