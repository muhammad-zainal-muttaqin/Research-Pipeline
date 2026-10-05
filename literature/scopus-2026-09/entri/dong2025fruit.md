# Fruit detection and yield estimation in Camellia oleifera based on improved YOLOv8 and ByteTrack algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dong2025fruit` |
| Judul asli | Fruit detection and yield estimation in Camellia oleifera based on improved YOLOv8 and ByteTrack algorithm |
| Penulis | Dong, Zhipeng; Long, Wei; Yang, Fan; Yu, Chunlian; Du, Jiayi; Wang, Kailiang; Lyu, Leyan |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | camellia |

## Tautan Akses
- PDF: [dong2025fruit.pdf](../pdf/dong2025fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101435

## Gambaran Umum
Makalah ini menyajikan alur pendugaan hasil panen *Camellia oleifera* (pohon penghasil minyak teh) dari video yang direkam dengan telepon pintar sambil mengelilingi pohon. Alur itu terdiri atas tiga tahap: deteksi buah permukaan dengan YOLOv8 yang dimodifikasi (tulang punggung RepViT, lapisan deteksi P2, dan fungsi kerugian Shape IoU), pelacakan dengan ByteTrack yang ditambah pencocokan fitur ORB untuk menghitung buah unik per video, dan regresi dari jumlah buah permukaan ke jumlah buah total per pohon serta ke hasil panen per pohon (dengan bobot rerata buah).

Data dikumpulkan di Changshan Oil Tea Experimental Base (Zhejiang, Tiongkok) pada tiga klon, yaitu CL4, CL40, dan CL53, masing-masing 20 pohon (total 60 pohon), pada 15 sampai 18 November 2023. Dari video diambil 3.630 citra dengan 64.975 buah beranotasi. Detektor yang ditingkatkan mencapai mAP50 86,21% (YOLOv8 dasar 81,70%), dengan 6,6 juta parameter. Pelacak yang ditingkatkan mencapai MOTA 63,7%, MOTP 80,2%, dan IDF1 77,1%.

Regresi dari jumlah buah permukaan terhadap jumlah buah sebenarnya per pohon menghasilkan R² 0,945 (campuran tiga klon) dan R² pendugaan hasil panen 0,902 (regresi linear dengan jumlah buah dan bobot rerata buah). Teks memuat beberapa ketidakkonsistenan angka yang dicatat pada bagian verifikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Hasil panen *C. oleifera* berfluktuasi karena fenomena pembuahan bergilir (*alternate bearing*), sehingga pendugaan produksi yang akurat dianggap penting bagi pemanenan dan penentuan harga. Cara tradisional, yaitu memetik, menghitung, dan menimbang buah, akurat tetapi lambat, padat karya, mahal, dan merusak lingkungan menurut penulis. Pendugaan berbasis tanah, cuaca, dan pengelolaan lahan dinilai sulit dari segi pengumpulan dan integrasi data.

Penulis menyatakan bahwa kebanyakan studi pendugaan hasil berbasis citra memakai citra tunggal yang terhambat oklusi dan adegan dinamis, sedangkan video memberi informasi temporal dan gerak. Buah *C. oleifera* kecil dan sering tertutup daun, sehingga deteksi dan pelacakan menjadi sulit. Penulis menilai bahwa metode terdahulu belum memenuhi sekaligus tuntutan akurasi, kecepatan, dan kompleksitas komputasi pada penghitungan berbasis video.

## Ide Utama
Gagasan utamanya adalah mengubah hitungan buah yang tampak di permukaan tajuk dari video menjadi dugaan hasil panen per pohon melalui dua regresi. Pertama, jumlah buah permukaan (hasil deteksi dan pelacakan) dipetakan ke jumlah buah total hasil panen penuh per pohon. Kedua, jumlah buah dikalikan bobot rerata buah dari sampel fenotipe, sehingga perbedaan ukuran buah antarklon ikut diperhitungkan.

Identitas buah antarbingkai dijaga oleh ByteTrack yang diperkaya pencocokan fitur ORB (*oriented FAST and rotated BRIEF*), yaitu pencocok titik fitur yang dipakai pada kotak deteksi yang tidak cocok dengan lintasan. Satu pohon direkam dalam satu putaran penuh, sehingga identitas dipertahankan lintas sisi pohon secara berurutan dalam video yang sama.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data dan anotasi
Tiga klon (CL4, CL40, CL53) dipilih, masing-masing dengan 20 pohon berumur serupa yang sehat. Perekaman memakai Xiaomi 13 (kamera utama 50 MP) dan Apple iPhone 13 (12 MP) pada video 4K 60 fps, antara pukul 08.30 dan 17.00 dalam cahaya alami. Operator mengelilingi setiap pohon dengan kecepatan sekitar 0,2 m/s, dengan ponsel miring ke atas 45° dan jarak 0,6 sampai 1,5 m dari tajuk. Bingkai diambil setiap 30 bingkai sehingga citra berdekatan tumpang tindih sekitar 70%, menghasilkan 3.630 citra. Anotasi memakai LabelImg dengan satu kelas (buah) dan 64.975 kotak. Citra dibagi latih dan uji 8:2; augmentasi mencakup rotasi, penskalaan, dan penyesuaian warna.

Setelah perekaman, semua buah tiap pohon dipanen dan dihitung; 30 buah per pohon dipilih acak untuk ditimbang dengan neraca berketelitian 0,01 g.

### 2. Detektor YOLOv8 yang ditingkatkan
Tiga perubahan diterapkan pada YOLOv8: (i) tulang punggung CSPDarkNet-53 diganti RepViT, yang menggabungkan CNN dan *Vision Transformer* dengan reparameterisasi struktural dan rasio ekspansi 2; (ii) lapisan deteksi P2 ditambahkan pada leher FPN dan PAN untuk objek kecil; (iii) kerugian regresi kotak CIoU diganti Shape IoU, yang memperhitungkan bentuk dan skala kotak itu sendiri. Pelatihan memakai GPU RTX 4090, ukuran citra 640 × 640, 300 epoch, ukuran batch 16, optimizer SGD dengan laju belajar awal 0,01 yang turun menjadi 0,0001, momentum 0,937, dan *weight decay* 0,0005. Mosaic dimatikan pada 10 epoch terakhir.

### 3. Pelacakan dan penghitungan
Paradigma *tracking-by-detection* dipakai. Ambang keyakinan deteksi diset 0,001 dengan ambang skor tinggi dan rendah. Kotak berskor tinggi dicocokkan dengan lintasan hasil prediksi filter Kalman; kotak yang tidak cocok diproses dengan ekstraksi dan pencocokan fitur ORB. Lintasan baru dibuat setelah kotak tidak cocok selama tiga bingkai berturut-turut. Jumlah ID unik pada satu video menjadi hitungan buah permukaan.

```
 video putaran pohon --> YOLOv8 (RepViT + P2 + Shape IoU)
        --> ByteTrack + ORB --> jumlah buah permukaan
        --> regresi --> jumlah buah total per pohon
        --> x bobot rerata buah --> hasil panen per pohon
```

### 4. Regresi jumlah buah dan hasil
Regresi linear dipakai sebagai model utama, dan sepuluh regresor lain (DT, RF, AdaBoost, GBDT, ExtraTrees, CatBoost, KNN, BPnet, SVR, XGBoost, LightGBM) diuji sebagai pembanding. Sebanyak 40 pohon dipakai untuk membangun model dan 20 pohon cadangan untuk verifikasi.

## Eksperimen dan Hasil
Detektor dibandingkan dengan Faster R-CNN, SSD, YOLOv3, YOLOv5, YOLOv7, YOLOv8, dan YOLOv9 sampai YOLOv12. Pelacak dibandingkan dengan SORT, DeepSORT, DeepMOT, Bot-SORT, dan ByteTrack. Metrik deteksi adalah presisi, *recall*, mAP50, dan mAP50-95; metrik pelacakan adalah MOTA, MOTP, dan IDF1.

Tabel 1. Perbandingan detektor (Tabel 1 makalah, sebagian).

| Model | FLOPs (G) | Parameter (juta) | P (%) | Recall (%) | mAP50 (%) | mAP50-95 (%) |
|---|---|---|---|---|---|---|
| Faster R-CNN | 180 | 42,3 | 57,33 | 62,17 | 60,25 | 27,34 |
| SSD | 273,7 | 33,8 | 68,81 | 71,41 | 70,73 | 34,10 |
| YOLOv5 | 48,8 | 20,9 | 80,43 | 73,11 | 80,21 | 41,76 |
| YOLOv8 | 28,7 | 11,1 | 81,06 | 74,07 | 81,70 | 44,28 |
| YOLOv12 | 22,2 | 17,6 | 81,78 | 74,36 | 81,78 | 44,63 |
| YOLOv8 yang ditingkatkan | 23,2 | 6,6 | 85,13 | 77,84 | 86,21 | 48,97 |

Ablasi (Tabel 2): RepViT saja menaikkan mAP50 dari 81,70% menjadi 85,13%; P2 saja 83,61%; Shape IoU saja 82,17%; gabungan ketiganya 86,21%.

Tabel 2. Perbandingan pelacak pada data *C. oleifera* (Tabel 3 makalah).

| Metode | MOTA | MOTP | IDF1 |
|---|---|---|---|
| SORT | 53,7 | 68,4 | 67,2 |
| DeepSORT | 59,8 | 73,6 | 70,2 |
| DeepMOT | 61,9 | 75,9 | 75,1 |
| Bot-SORT | 59,4 | 77,7 | 74,6 |
| ByteTrack | 62,6 | 79,4 | 76,7 |
| ByteTrack yang ditingkatkan | 63,7 | 80,2 | 77,1 |

Untuk penghitungan, 60 klip video dipilih acak sebagai sampel evaluasi dan menghasilkan R² 0,945 antara hitungan algoritma dan hitungan manual. Regresi jumlah buah sebenarnya terhadap jumlah buah permukaan per klon: CL4 y = 1,1660x − 3,734 (R² 0,989), CL40 y = 1,448x + 5,445 (R² 0,931), CL53 y = 1,144x + 14,829 (R² 0,914), dan campuran y = 1,138x + 14,868 (R² 0,945). Kemiringan CL40 yang besar dikaitkan penulis dengan pohon yang tinggi sehingga pengambilan data terganggu.

Pada 20 pohon verifikasi, Tabel 4 mencatat R² 0,622 sampai 0,901 dan MAPE 9,898% sampai 13,859% untuk berbagai regresor; LightGBM dan ExtraTrees masing-masing memperoleh R² 0,901. Untuk hasil panen per pohon (Tabel 5), regresi linear dan BPnet memperoleh R² 0,902; regresi linear memperoleh MSE 0,297, RMSE 0,545, MAE 0,415, dan MAPE 17,555. Menambahkan bobot rerata buah menaikkan R² per klon: CL4 dari 0,921 menjadi 0,976, CL40 menjadi 0,906, dan CL53 menjadi 0,893; campuran mencapai R² 0,905 dan RMSE 0,451.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak: acuan jumlah buah berasal dari pemanenan dan penghitungan seluruh buah per pohon, pengambilan data memakai ponsel biasa, dan perbandingan dilakukan terhadap banyak detektor serta pelacak. Rekaman mengelilingi pohon sehingga buah dari berbagai sisi tajuk tercakup.

Keterbatasan yang dinyatakan penulis: kinerja bervariasi antarklon, dengan CL40 yang kurang terwakili pada data latih dan mirip bentuknya dengan CL4; ketelitian deteksi dipengaruhi variasi ukuran buah dan tinggi pohon; generalisasi ke buah lain sulit; kondisi cahaya dan oklusi memengaruhi ketangguhan; dan skalabilitas ke kebun yang lebih besar belum diuji. Penulis berencana menambahkan pelacakan multi-pandang (*multiple-view tracking*).

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Tidak ada ukuran galat hitungan video yang berdiri sendiri, misalnya MAE atau MAPE, selain R² 0,945 yang dilaporkan dengan dua tafsiran (hitungan video terhadap hitungan manual pada 60 klip, dan jumlah buah total terhadap jumlah buah permukaan per pohon). Hitungan manual pada klip tidak dijelaskan prosedurnya. Pelacak ORB hanya menaikkan MOTA 1,1 poin dari ByteTrack dasar pada data yang sama, tanpa ulangan atau uji kemaknaan. Pembagian 40 pohon untuk model dan 20 pohon untuk verifikasi kecil. Identitas buah tidak dikaitkan antar-video; regresi permukaan ke total menyerap buah yang tersembunyi sebagai faktor skala per klon, sehingga model harus dikalibrasi ulang untuk klon atau kebun lain.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam satu video yang mengelilingi pohon. Mekanismenya adalah pelacakan berbasis deteksi (ByteTrack dengan filter Kalman dan pencocokan ORB) yang menetapkan ID unik. Rekaman melingkar mencakup beberapa sisi pohon, tetapi identitas hanya dijaga secara berurutan dalam satu video; tidak ada pencocokan antar-video, antar-sisi yang terpisah, maupun rekonstruksi 3D. Buah yang tidak terlihat dari permukaan dikoreksi secara statistik melalui regresi permukaan ke total.

Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas (buah). Acuan hitungnya adalah hitungan hasil panen penuh per pohon (semua buah dipanen dan dihitung) untuk regresi, dan hitungan manual untuk 60 klip video. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan dua tahap, yaitu hitungan permukaan yang dipetakan ke total melalui regresi per kultivar, dan penggunaan acuan panen penuh per pohon. Koreksi regresi bersifat spesifik klon, sebagaimana terlihat pada kemiringan yang berbeda untuk CL4, CL40, dan CL53.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `dong2025fruit`.

Dong dkk. (2025) mengusulkan alur pendugaan hasil *Camellia oleifera* dari video yang mengelilingi pohon, yang memakai YOLOv8 dengan tulang punggung RepViT, lapisan P2, dan Shape IoU (mAP50 86,21%), ByteTrack yang diperkaya pencocokan fitur ORB (MOTA 63,7%, IDF1 77,1%), serta regresi dari jumlah buah permukaan ke jumlah buah total (R² 0,945) dan hasil per pohon (R² 0,902) pada 60 pohon dari tiga klon.

Catatan verifikasi data: Angka detektor berasal dari Tabel 1 dan Tabel 2, angka pelacak dari Tabel 3, angka regresi dari Tabel 4, Tabel 5, Gambar 9 sampai 11, dan teks Seksi 3.4 dan 3.5. Jumlah citra, anotasi, pohon, dan pembagian data berasal dari Seksi 2.1 dan Seksi 3.4. Teks memuat ketidakkonsistenan yang tidak dapat diselesaikan dari teks: Tabel 4 mencatat regresi linear dengan R² 0,831 dan MAPE 13,859 (baris identik dengan DT), sedangkan teks menyebut regresi linear dan ExtraTrees dengan R² 0,901; Seksi 3.5 menyebut R² keseluruhan 0,854 dan RMSE 0,559 (dan 0,389 untuk CL4) sehingga angka RMSE per klon tidak konsisten antar paragraf; Kesimpulan menyebut RMSE 10,989 untuk uji akurasi, padahal angka itu sama dengan MAPE ExtraTrees pada Tabel 4; Seksi 3.5 menyebut MAE 0,415 sebagai RMSE di Seksi 4.3 (RMSE 0,415) sementara Tabel 5 memuat RMSE 0,545 dan MAE 0,415. Teks juga memuat kalimat sisipan yang terpotong dan mengulang abstrak di tengah Seksi 3.5. Tabel dan gambar tambahan (Tabel S1 dan S2) tidak tersedia pada teks ekstraksi. Hasil dan angka MOTA diambil dari Tabel 3; peningkatan 1,1, 0,8, dan 0,4 poin dihitung dari tabel yang sama dan sesuai dengan yang tertulis di teks.
