## Gambaran Umum
Makalah ini mengusulkan metode pendeteksian dan penghitungan apel pada video kebun dengan detektor ringan YOLOv4-tiny, pelacak berbasis filter Kalman (*Kalman filter*), dan algoritma Hungarian yang diperbaiki dengan jarak Euklides serta *Intersection over Union* (IoU). Objek penelitian adalah apel Fuji pada kebun modern berbentuk dinding buah vertikal (*vertical fruiting wall*) di Kabupaten Fufeng, Kota Baoji, Provinsi Shaanxi, Tiongkok. Data diambil pada akhir September 2020 dengan kamera RealSense D435 pada kereta kendali jarak jauh, menghasilkan 800 citra dan 10 video.

Detektor YOLOv4-tiny mencapai *Average Detection Precision* (ADP) 94,47% pada set uji citra dan akurasi deteksi video (*Video Detection Accuracy*, VDA) 96,15%. Pelacakan dengan pencocokan yang diperbaiki mencapai *Multiple Object Tracking Accuracy* (MOTA) 69,14% dan *Multiple Object Tracking Precision* (MOTP) 75,60%, naik 26,86 dan 20,78 poin persentase dari versi tanpa perbaikan. Akurasi penghitungan rerata (*Average Counting Precision*, ACP) pada 10 video adalah 81,94%, dengan koefisien determinasi $R^2$ 0,986 dan RMSE 33,711 terhadap hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Hasil kebun apel pada kebun komersial umumnya diperkirakan dengan penghitungan manual berbasis sampel yang memakan waktu dan tenaga. Penelitian penghitungan buah otomatis sebelumnya sebagian besar menggunakan citra statis dan tidak menghitung buah secara dinamis pada video. Metode tradisional berbasis warna, tekstur, dan bentuk sulit memenuhi kebutuhan kecepatan dan akurasi sekaligus serta tidak bersifat umum.

Pelacakan objek diperlukan untuk mengaitkan buah yang sama pada bingkai berbeda agar tidak terhitung berulang. Penulis mencatat studi terdahulu yang melacak mangga dengan filter Kalman menghasilkan 9,9% penghitungan ganda dan 7,3% kesalahan hitung dibandingkan hitungan manual, sehingga hitungan sekitar 2,6% lebih tinggi (angka dikutip dari makalah lain). Penelitian ini berfokus pada kebun modern bertipe dinding buah dengan jarak antarbaris 3,5 sampai 4,0 m.

## Ide Utama
Penghitungan buah pada video diubah menjadi masalah pelacakan multi-objek (*multi-object tracking*, MOT): setiap apel yang terdeteksi diberi identitas numerik pada kemunculan pertama dan jumlah identitas unik menjadi hitungan. Pencocokan prediksi Kalman dengan deteksi dilakukan dalam dua tahap, yaitu jarak Euklides lalu IoU untuk sisa yang gagal cocok, guna mengurangi lompatan identitas dan penghitungan berlebih.

```
 Bingkai video -> YOLOv4-tiny (deteksi apel)
        |
 Filter Kalman memprediksi posisi pada bingkai berikutnya
        |
 Hungarian + jarak Euklides  ->  sisa gagal cocok: Hungarian + IoU
        |
 Cocok: perbarui lintasan   Gagal 30 bingkai berturut-turut: hapus lintasan
 Deteksi tak cocok: apel baru, beri ID baru   ->   hitungan = jumlah ID
```

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data dan set data
Kebun berada di Fufeng, Baoji (107°9' BT, 34°38' LU) dengan kultivar Fuji. Jarak antartanaman 0,3 sampai 1,5 m dan antarbaris sekitar 3,5 sampai 4,0 m. Kamera RealSense D435 dipasang pada kereta kendali jarak jauh yang berjalan di antara baris; tinggi kamera minimal 1,43 m dan jarak ke baris pohon minimal 2,07 m. Terkumpul 800 citra beresolusi 720 x 1280 pada pukul 08.00 sampai 18.00 (cahaya depan, belakang, dan samping) dan 10 video MP4 pada 30 bingkai per detik dengan resolusi 720 x 1280.

Sebanyak 800 citra dianotasi dengan LabelImg. Kotak pembatas mencakup apel yang dapat dikenali atau yang kontur-nya dapat disimpulkan; apel pada baris belakang, pada tepi citra, yang jatuh ke tanah, dan yang diikat pada pohon tidak dianotasi. Augmentasi berupa rotasi 90, 180, dan 270 derajat, pembalikan horizontal dan vertikal (4.800 citra), kabur gerak (6.400), dan transformasi kecerahan (8.000). Pembagian acak 4:1 menghasilkan 5.120 citra latih dan 1.600 citra uji (78.776 sampel beranotasi).

### 2. Deteksi dengan YOLOv4-tiny
Masukan jaringan 416 x 416 piksel, dengan 21 lapisan konvolusi, 11 lapisan *route*, 3 lapisan *max-pooling*, dan 2 lapisan keluaran berskala 13 x 13 dan 26 x 26. Pelatihan memakai *Darknet* pada Intel Core i5-6400, RAM 16 GB, dan NVIDIA GTX 1080 8 GB, dengan laju belajar awal 0,001, *weight decay* 0,0005, momentum 0,9, dan 50.000 iterasi (pencarian grid). YOLOv3-tiny dilatih sebagai pembanding. Pada deteksi video, ambang keyakinan dinaikkan menjadi 0,8.

### 3. Pelacakan dengan filter Kalman
Karena video berlaju 30 bingkai per detik, perpindahan buah antarbingkai dianggap kecil dan gerak diasumsikan seragam linear. Filter Kalman memprediksi keadaan dan kovarians pada bingkai berikutnya, lalu memperbarui estimasi dengan deteksi yang cocok.

### 4. Pencocokan dengan Hungarian yang diperbaiki
Tahap pertama mencocokkan prediksi dan deteksi dengan jarak Euklides antara koordinat kotak pelacak dan kotak deteksi menggunakan algoritma Hungarian. Prediksi dan deteksi yang gagal cocok kemudian dicocokkan ulang dengan IoU dengan ambang maksimum yang ditentukan secara eksperimen (nilai ambang tidak tercantum pada teks). Lintasan yang gagal cocok disimpan sementara dan dihapus setelah 30 bingkai berturut-turut gagal; deteksi yang gagal cocok dianggap apel baru. Hitungan akhir adalah jumlah ID yang diberikan menurut urutan kemunculan apel.

### 5. Uji dan metrik
Deteksi dievaluasi dengan presisi, *recall*, F1, ADP, dan waktu deteksi per citra. Pelacakan dievaluasi dengan laju pergantian ID (*ID switch rate*, IDSR), MOTA, dan MOTP. Penghitungan dievaluasi dengan ACP, yaitu rerata $1 - |S - G|/G$ pada 10 video. Acuan hitungan manual dibuat oleh tiga peneliti yang memutar video bingkai demi bingkai, mencatat apel pada bingkai pertama dan apel baru pada bingkai berikutnya, lalu hasilnya dirata-ratakan. Pelacakan diuji pada laptop Intel Core i7-8565U dengan GPU MX250 2 GB.

## Eksperimen dan Hasil
Detektor diuji pada 1.600 citra uji. Pelacakan dan penghitungan diuji pada 10 video dengan 220 sampai 524 bingkai per video.

Perbandingan detektor (Tabel 1):

| Model | Presisi | Recall | F1 | ADP (%) | Waktu (s per bingkai) |
|---|---|---|---|---|---|
| YOLOv3-tiny | 0,85 | 0,91 | 0,88 | 92,71 | 0,027 |
| YOLOv4-tiny | 0,87 | 0,93 | 0,90 | 94,47 | 0,018 |

Pada set uji, YOLOv4-tiny mendeteksi 73.266 sampel benar (TP), 11.346 positif palsu (FP), dan 5.510 negatif palsu (FN); YOLOv3-tiny mendeteksi 71.501 TP, 12.291 FP, dan 7.275 FN.

Pelacakan sebelum dan sesudah perbaikan pencocokan (Tabel 2, dalam persen):

| Versi | VDA | IDSR | MOTA | MOTP |
|---|---|---|---|---|
| Sebelum perbaikan | 96,15 | 25,91 | 42,28 | 54,82 |
| Sesudah perbaikan | 96,15 | 11,92 | 69,14 | 75,60 |

Penghitungan pada 10 video menghasilkan ACP rerata 81,94%, dengan akurasi tiap video sekitar 80%, $R^2$ 0,986, dan RMSE 33,711 terhadap hitungan manual. Penulis menyatakan akurasi hitungan tidak turun seiring bertambahnya jumlah buah per video. Galat deteksi utama adalah apel yang tidak perlu dihitung, yaitu apel jatuh, terikat pada pohon, pada baris belakang, dan pada tepi citra yang terhalang berat. Apel yang terlewat sebagian besar tertutup berat dan jarang terjadi pada video karena apel muncul pada banyak bingkai.

## Kelebihan dan Keterbatasan
Kelebihan: detektor ringan (0,018 detik per citra), pencocokan dua tahap yang menurunkan IDSR dari 25,91% menjadi 11,92%, dan evaluasi penghitungan terhadap hitungan manual tiga peneliti pada 10 video.

Keterbatasan yang dinyatakan penulis: deteksi masih menghitung apel yang tidak relevan (jatuh, terikat, baris belakang, tepi citra). Perbaikan di masa depan yang diusulkan adalah ambang rasio aspek dan luas kotak untuk membuang kotak non-target. Lompatan ID akibat kompleksitas kebun dan mutu video disebut sebagai sumber utama galat pelacakan.

Menurut pembacaan ringkasan ini, akurasi hitungan rerata 81,94% menyiratkan galat hitung yang belum dijelaskan arahnya (kelebihan atau kekurangan hitungan tidak diuraikan per video pada teks). Menurut pembacaan ringkasan ini pula, evaluasi hanya mencakup satu kebun, satu kultivar, dan satu pandang kamera dari satu sisi baris, sehingga penanganan apel yang terlihat dari sisi berlawanan tidak diuji.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan video: filter Kalman dengan gerak seragam, pencocokan Hungarian berdasarkan jarak Euklides dan IoU, serta ID numerik yang diberikan pada kemunculan pertama. Pandangan dari sisi lain pohon tidak ditangani; kamera bergerak di satu sisi baris.

Hitungan tidak dilaporkan per kelas; apel dihitung sebagai satu kelas. Acuan hitung adalah hitungan manual pada video oleh tiga peneliti (rerata), bukan hasil panen. Hal yang dapat dipindahkan ke tandan kelapa sawit multi-sisi adalah pola pencocokan dua tahap (jarak lalu IoU) dengan masa hidup lintasan, serta laporan IDSR, MOTA, dan MOTP yang menilai kualitas identitas secara terpisah dari kualitas deteksi. Keterbatasannya, gerak seragam linear dan 30 bingkai per detik mungkin tidak berlaku untuk lintasan pengambilan citra antarsisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gao2021apple`.

Gao dkk. mengusulkan penghitungan apel pada video kebun dinding buah dengan YOLOv4-tiny, filter Kalman, dan algoritma Hungarian yang diperbaiki dengan jarak Euklides serta IoU. Perbaikan pencocokan menaikkan MOTA dari 42,28% menjadi 69,14% dan menurunkan laju pergantian ID dari 25,91% menjadi 11,92%. Pada 10 video, akurasi penghitungan rerata 81,94% terhadap hitungan manual tiga peneliti, dengan $R^2$ 0,986.

Catatan verifikasi data: makalah berbahasa Mandarin dengan abstrak berbahasa Inggris, dan ringkasan ini dibuat dari teks Mandarin. ADP 94,47% dan VDA 96,15% terdapat pada Tabel 1, bagian 2.1, dan abstrak. MOTA, MOTP, dan IDSR berasal dari Tabel 2. ACP 81,94%, $R^2$ 0,986, dan RMSE 33,711 terdapat pada bagian 2.3 dan kesimpulan. Abstrak berbahasa Inggris menyebut resolusi citra 720 x 1080 piksel, sedangkan badan teks menyebut 720 x 1280; ringkasan ini memakai 720 x 1280. Rumus filter Kalman hasil ekstraksi teks terpotong dan tidak dikutip. Nilai ambang IoU, jumlah apel per video, dan hitungan per video tidak dilaporkan pada teks (hanya pada Gambar 6 yang tidak terbaca).
