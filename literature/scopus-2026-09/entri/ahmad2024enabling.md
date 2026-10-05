# Enabling Consumer UAVs for Precision Agriculture Applications: A Case Study of Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmad2024enabling` |
| Judul asli | Enabling Consumer UAVs for Precision Agriculture Applications: A Case Study of Yield Estimation |
| Penulis | Ahmad, Jamil; Gueaieb, Wail; Saddik, Abdulmotaleb El; Masi, Giulia De; Karray, Fakhri |
| Tahun | 2024 |
| Venue | Digest of Technical Papers IEEE International Conference on Consumer Electronics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, peach/nectarine |

## Tautan Akses
- PDF: [ahmad2024enabling.pdf](../pdf/ahmad2024enabling.pdf)
- DOI resmi: https://doi.org/10.1109/icce59016.2024.10444191

## Gambaran Umum
Makalah konferensi ICCE 2024 ini mengusulkan alur pemrosesan video dari drone (*unmanned aerial vehicle*, UAV) kelas konsumen yang berjalan pada ponsel pintar Android untuk mengestimasi hasil panen buah. Alur terdiri atas pra-pemrosesan, deteksi buah, dan estimasi hasil. Detektor merupakan modul paling mahal secara komputasi, sehingga dijalankan hanya pada sebagian bingkai karena video bersifat redundan. Detektor yang dipakai adalah YOLOv8-Nano yang dimodifikasi (YOLOv8-Nano-M) dan dikuantisasi ke INT8.

Evaluasi memakai dua set data: persik (2.000 citra) dan apel (1.000 citra), masing-masing dibagi 80/20 untuk pelatihan dan pengujian. Pada deteksi, YOLOv8-Nano-M mencapai mAP50 0,750 (presisi 0,752, *recall* 0,699), dibandingkan YOLOv8-Large dengan mAP50 0,775. Korelasi Pearson antara estimasi hasil dan acuan adalah 0,89 untuk persik dan 0,83 untuk apel. Pada ponsel kelas menengah (Snapdragon 732G), model YOLOv8-Nano-M dengan masukan 320 piksel mencapai 9,1 FPS, dan pada Snapdragon 870 mencapai 20,0 FPS.

## Latar Belakang: Masalah yang Ingin Dipecahkan
UAV khusus pertanian presisi mahal sehingga membatasi penerapan pada lahan kecil sampai menengah, terutama di negara berkembang. UAV kelas konsumen murah dan memiliki kamera RGB beresolusi tinggi serta kemampuan streaming video, tetapi daya baterai terbatas dan tidak memiliki pemrosesan di dalam pesawat untuk tugas padat komputasi. Solusi komersial seperti DJI SmartFarm Web bergantung pada kamera, modul GPS, stasiun kendali darat, dan server awan yang mahal.

Karya terdahulu yang dirangkum penulis mencakup penghitungan jeruk dengan UAV, Citrus-YOLO, DeepSort, dan pencacah terdistribusi tak seragam (F1 89,07%, MAPE 12,74%), serta penghitungan organ generatif tomat dengan YOLOv5 dan DeepSort yang berjalan pada PC (F1 rata-rata 0,63). Penulis menyatakan bahwa persoalan ketangguhan dan efisiensi masih memerlukan solusi baru.

## Ide Utama
Ponsel pintar dipakai sebagai platform komputasi portabel untuk UAV konsumen. Video diterima dari pengendali jarak jauh atau melalui SDK produsen UAV, lalu diproses di perangkat. Efisiensi dicapai dengan model deteksi ringan yang dikuantisasi, pemrosesan bingkai terpilih, dan estimasi hasil sederhana berbasis jumlah buah terdeteksi dikalikan faktor koreksi untuk buah yang tidak terlihat atau tidak terdeteksi.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Gambar diambil dari UAV dengan kamera RGB. Buah tampak sangat kecil pada citra drone. Detail kultivar, lokasi, ketinggian terbang, dan jumlah pohon tidak dilaporkan; yang tertulis hanya jumlah citra (persik 2.000, apel 1.000) dan bahwa data berasal dari kebun yang berbeda.

### 2. Pra-pemrosesan dan augmentasi
Pra-pemrosesan melakukan normalisasi intensitas sebelum inferensi. Untuk menangani variasi skala, citra berlabel dipotong menjadi petak-petak kecil yang saling tumpang tindih dengan anotasi kotak disesuaikan, lalu diaugmentasi dengan rotasi, pembalikan horizontal dan vertikal, serta *motion blur*.

### 3. Deteksi buah
Penulis memakai keluarga YOLOv8 (anchor-free, modul C2f, kepala terpisah untuk deteksi dan klasifikasi, fungsi kerugian CIoU dan DFL). Varian YOLOv8n dimodifikasi lebar dan kedalamannya menjadi YOLOv8-Nano-M (2,8 juta parameter, 7,6 FLOPS dibandingkan 3,2 juta parameter dan 8,7 FLOPS pada YOLOv8-Nano; satuan FLOPS sebagaimana tertulis pada Tabel II). Model kemudian dikuantisasi pascapelatihan dari FP32 ke INT8, dikonversi ke format PyTorch Lite, dan dipasang pada aplikasi Android. Modifikasi lebar dan kedalaman tidak dirinci angkanya dalam teks.

### 4. Estimasi hasil
Total buah diekstrapolasi dengan $N_F = \sum_{n=1}^{N_t} F_d^n \, C_f$, dengan $N_t$ jumlah pohon, $F_d^n$ jumlah buah terdeteksi pada pohon ke-$n$, dan $C_f$ faktor koreksi untuk buah tak terlihat atau tak terdeteksi. Faktor koreksi dapat diatur adaptif menurut tinggi pohon, ukuran tajuk, dan kepadatan buah; nilai yang dipakai pada eksperimen tidak dilaporkan.

### 5. Aplikasi prototipe
Aplikasi Android dibangun dengan Java dan pustaka pytorch-android-lite. Bingkai dari drone diperkecil, dinormalisasi, dijadikan tensor, diinferensi, lalu pascapemrosesan (*non-maximum suppression* dan penskalaan kotak) dilakukan dalam Java. Bingkai terbaru diproses dan jumlah buah dikumpulkan per pohon; sebagian bingkai sengaja dibuang karena video redundan. Makalah tidak menjelaskan cara menentukan batas antarpohon atau cara mencegah penghitungan ganda buah yang sama pada bingkai berbeda.

## Eksperimen dan Hasil
Pelatihan dilakukan pada server Xeon 10 inti dengan RAM 128 GB dan GPU Nvidia RTX A6000 (48 GB). Aplikasi diuji pada POCO X3 NFC (Snapdragon 732G, kelas menengah; ditulis "POXO" pada makalah) dan Xiaomi Pad 6 (Snapdragon 870). Metrik: presisi, *recall*, dan mAP50.

| Model | Presisi | Recall | mAP50 |
|---|---|---|---|
| YOLOv8-Nano | 0,751 | 0,701 | 0,752 |
| YOLOv8-Small | 0,748 | 0,659 | 0,753 |
| YOLOv8-Medium | 0,738 | 0,718 | 0,751 |
| YOLOv8-Large | 0,757 | 0,717 | 0,775 |
| YOLOv8-Nano-M | 0,752 | 0,699 | 0,750 |

Tabel III tidak menyebut set data (apel, persik, atau gabungan) yang dipakai untuk metrik tersebut.

Waktu inferensi dan FPS (rata-rata pada set uji):

| Model | SD-732G (detik [FPS]) | SD-870 (detik [FPS]) |
|---|---|---|
| YOLOv8-Nano | 0,43 [2,3] | 0,11 [10,2] |
| YOLOv8-Small | 0,80 [1,3] | 0,24 [4,2] |
| YOLOv8-Medium | 1,10 [0,9] | 0,63 [1,6] |
| YOLOv8-Large | 1,44 [0,7] | 0,74 [1,4] |
| YOLOv8-Nano-416 | 0,23 [4,3] | 0,07 [14,3] |
| YOLOv8-Nano-320 | 0,14 [7,2] | 0,06 [16,6] |
| YOLOv8-Nano-M-320 | 0,11 [9,1] | 0,05 [20,0] |

Untuk estimasi hasil, korelasi Pearson pada set uji adalah 0,89 untuk persik dan 0,83 untuk apel. Penulis menyimpulkan bahwa YOLOv8-Large paling akurat, sedangkan YOLOv8-Nano-M kompetitif dengan biaya komputasi jauh lebih kecil, dan bahwa model terkuantisasi dengan resolusi masukan lebih kecil cukup cepat untuk inferensi waktu-nyata pada aliran video UAV.

## Kelebihan dan Keterbatasan
Kelebihan: biaya perangkat keras rendah, pemrosesan di perangkat tanpa server, dan model ringan yang mencapai sekitar 9 sampai 20 FPS pada ponsel. Penulis juga menyebut rekaman video dapat disimpan dan dipakai untuk membandingkan musim atau efek perlakuan di kemudian hari.

Keterbatasan yang dinyatakan penulis: kebutuhan penelitian lanjutan untuk meningkatkan akurasi dan ketangguhan detektor, mengintegrasikan sensor lain, serta membangun antarmuka yang ramah pengguna. Penulis tidak membahas keterbatasan metode estimasi hasil.

Menurut pembacaan ringkasan ini: (1) tidak ada mekanisme pelacakan atau identitas buah antarbingkai, sehingga duplikasi hitungan pada bingkai yang tumpang tindih tidak ditangani secara eksplisit; (2) faktor koreksi $C_f$, definisi acuan hasil panen, jumlah pohon uji, dan hasil per set data tidak dilaporkan, sehingga korelasi 0,89 dan 0,83 sulit ditafsirkan; (3) selisih mAP50 antar model sangat kecil (0,750 sampai 0,775), dan kecepatan pada Tabel IV bergantung pada resolusi masukan yang berbeda dari Tabel III.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani identitas buah yang sama pada banyak pengamatan. Pada Seksi III-D disebutkan bahwa bingkai yang paling baru diproses dan jumlah buah dikumpulkan per pohon, dengan sebagian bingkai dibuang, tetapi tidak ada pelacakan, pencocokan multi-pandang, ataupun koreksi duplikasi. Pada Seksi III-C, buah yang tidak terlihat dari satu sisi diperhitungkan melalui faktor koreksi $C_f$ yang bersifat global, bukan melalui penggabungan pengamatan. Hitungan tidak dilaporkan per kelas (hanya satu kelas buah), dan acuan estimasi dinyatakan melalui korelasi Pearson tanpa uraian apakah acuannya panen, hitung lapangan, atau anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan sawit hanya sisi rekayasa: detektor YOLOv8 ringan terkuantisasi pada ponsel. Faktor koreksi tunggal untuk buah tak terlihat adalah kebalikan dari pendekatan identitas lintas pandang, sehingga makalah ini lebih cocok sebagai pembanding dasar (*baseline*) yang tidak menangani duplikasi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `ahmad2024enabling`.

Ahmad dkk. mengusulkan alur pemrosesan video UAV konsumen pada ponsel Android dengan detektor YOLOv8-Nano termodifikasi dan terkuantisasi serta estimasi hasil berbasis jumlah buah terdeteksi dikalikan faktor koreksi. Pada set data apel (1.000 citra) dan persik (2.000 citra), korelasi Pearson estimasi hasil adalah 0,83 dan 0,89, dengan mAP50 deteksi 0,750 untuk YOLOv8-Nano-M dan kecepatan 9,1 sampai 20,0 FPS pada ponsel. Makalah tidak memuat mekanisme pelacakan atau pencegahan hitungan ganda.

Catatan verifikasi data: mAP50, presisi, dan *recall* dari Tabel III; FPS dan waktu inferensi dari Tabel IV; parameter dan FLOPS dari Tabel II; jumlah citra dan pembagian 80/20 dari Seksi IV-A; korelasi 0,89 dan 0,83 dari Seksi IV-B. Tidak dapat diverifikasi dari teks: set data yang dipakai pada Tabel III, nilai $C_f$, jumlah pohon, jenis acuan estimasi hasil, lokasi dan kultivar, serta ketinggian terbang. Teks ekstraksi terbaca baik; tabel terpisah per baris tetapi urutannya dapat direkonstruksi.
