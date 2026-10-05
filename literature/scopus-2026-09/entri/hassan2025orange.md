# Orange yield estimation using object tracking and 3D reconstruction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hassan2025orange` |
| Judul asli | Orange yield estimation using object tracking and 3D reconstruction |
| Penulis | Hassan, Amna; Mumtaz, Rafia; Palade, Vasile; Amin, Arslan; Mahmood, Zahid; Khan, Noorullah; Noman, Muhammad; Imran, Muhammad; Wicha, Santichai |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [hassan2025orange.pdf](../pdf/hassan2025orange.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101088

## Gambaran Umum
Makalah ini mengusulkan alur kerja estimasi hasil jeruk (*orange*) per pohon dari video yang direkam dengan kamera genggam. Alur terdiri atas deteksi buah dengan YOLOv8 pada citra yang dibagi menjadi petak (*tiling*), pelacakan dengan Byte tracker yang dilengkapi pengelolaan "kamus" untuk menyambung ID antarpetak, klasifikasi kematangan dengan MobileViT, rekonstruksi 3D dengan COLMAP (*Structure-from-Motion*, SfM), serta pengelompokan K-means pada titik 3D untuk menetapkan buah ke pohon dan membuang buah yang terhitung ulang.

Data berupa 1.451 citra pohon jeruk dari kebun National Agricultural Research Center (NARC) Pakistan dan dataset yang dibagikan Guangxi Normal University (dianotasi ulang oleh penulis), serta dua video uji dari kebun di Sargodha. Pada citra uji, YOLOv8 nano yang dilatih dan diuji dengan petak mencapai presisi 78,2%, *recall* 69,7%, mAP50 76%, dan mAP50-95 38%. Klasifikasi kematangan dengan MobileViT XXS mencapai akurasi uji 97,8% (dua kelas) dan 86,9% (tiga kelas).

Pada video, hitungan algoritma dibandingkan dengan hitungan asli: tingkat deteksi 84,6% pada Video 1 (satu pohon, oklusi daun sedikit) dan 74,8% pada Video 2 (tiga pohon, oklusi dan pencahayaan lebih buruk). Hasil per pohon bervariasi dari 58,8% sampai 90,2%. Penulis menyimpulkan algoritma bekerja baik pada pohon dengan oklusi daun rendah.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan buah jeruk secara manual dan pemantauan tahap pertumbuhan dinilai lambat, rawan keterlambatan, dan menimbulkan estimasi yang tidak transparan dalam rantai pasok. Estimasi hasil diperlukan untuk pengelolaan sumber daya, transportasi, penyimpanan, ekspor, dan penaksiran harga. Penghitungan langsung pada pohon sulit karena buah tersebar dan dedaunan rapat.

Penulis merumuskan beberapa masalah teknis: model deteksi sensitif terhadap pencahayaan yang berubah sepanjang hari; buah kecil hilang saat citra diperkecil; buah muda berwarna mirip daun; dan pada video, pemrosesan tiap bingkai secara terpisah menyebabkan buah yang sama terhitung berulang sehingga diperlukan pelacakan. Penulis juga menanyakan apakah satu model deteksi dapat menyaingi pengklasifikasi khusus untuk kematangan, dan menginginkan hasil per pohon, bukan hanya total kebun.

## Ide Utama
Gagasan pertama adalah mengatasi buah kecil dengan membagi citra beresolusi tinggi menjadi petak 2 × 2, lalu mengubah tiap petak menjadi 640 × 640 piksel. Gagasan kedua adalah menyambung ID buah yang berpindah antarpetak melalui zona rawan di sekitar garis pembagi dan pencocokan jarak Euklides. Gagasan ketiga adalah memakai titik fitur 3D hasil SfM dalam dua cara: mengelompokkan buah ke pohon (K-means dengan $k$ sama dengan jumlah pohon dalam barisan) dan mendeteksi buah yang terhitung ulang, yaitu buah yang berbagi titik fitur yang sama.

## Cara Kerja Langkah demi Langkah

```
 [Video] -> [Tiling 2x2] -> [YOLOv8 per petak] -> [Byte tracker per petak
   + kamus ID di zona batas petak] -> [MobileViT: kematangan]
   -> [COLMAP/SfM pada area objek] -> [K-means 3D: pohon] -> [hitungan per pohon]
```

### 1. Akuisisi dan penyusunan data
Pengambilan data berlangsung Agustus sampai Desember agar mencakup beberapa tahap kematangan. Sumber pertama adalah citra kamera Kinect V2 dari kebun NARC (694 citra dari pandangan jauh). Sumber kedua adalah dataset Guangxi Normal University (pandangan dekat), yang dianotasi ulang. Total 1.451 citra dalam beragam pencahayaan dan cuaca, dibagi 80% latih, 10% uji, dan 10% validasi. Anotasi memakai Roboflow untuk kotak pembatas dan kelas kematangan: awalnya dua kelas (matang dan mentah), lalu dibuat versi tiga kelas dengan tambahan kelas matang sebagian (*partially-ripe*) karena ada tahap yang tidak sepenuhnya matang dan tidak dapat disebut mentah. Resolusi asli 5760 × 3840 atau 6000 × 4000 piksel.

Untuk uji video, dua video diambil dengan gerak linear di kebun Sargodha: satu video berisi satu pohon dan satu video berisi tiga pohon dalam satu baris, keduanya penuh buah dan daun. Satu video lain diambil dengan sudut dan gerak tak linear untuk menilai deteksi, pelacakan, dan klasifikasi (hasil kuantitatifnya tidak dilaporkan).

### 2. Augmentasi dan prapemrosesan
Citra dipetakan 2 × 2, kemudian diaugmentasi (pembalikan, rotasi, geser, perubahan hue, saturasi, kecerahan, eksposur, pengaburan, derau), dan tiap petak diubah menjadi 640 × 640. Hasil akhir 17.412 citra. Untuk klasifikasi, buah dipotong dari citra itu dan diubah menjadi 50 × 50 piksel, menghasilkan 143.988 jeruk (91.277 mentah dan 52.711 matang).

### 3. Deteksi YOLOv8
Varian nano, small, dan medium dilatih dalam empat pengaturan: tanpa petak saat latih dan uji; petak hanya saat inferensi; petak hanya saat latih; petak saat latih dan uji. Pelatihan memakai CPU i7-12700K, GPU Nvidia 3090 24 GB, laju belajar 0,01, *batch* 16, Adam, momentum 0,937, peluruhan bobot 0,005, 50 epoch.

### 4. Pelacakan dan penyambungan ID antarpetak
Byte tracker berjalan terpisah pada tiap petak sehingga buah yang berpindah petak mendapat ID baru. Daerah dalam 50 piksel dari garis pembagi disebut zona rawan. Objek yang hilang atau baru terdeteksi di zona ini dicocokkan memakai jarak Euklides pusat kotak. Objek yang tidak teridentifikasi dalam 10 bingkai setelah hilang dikeluarkan dari daftar pelacakan.

### 5. Klasifikasi kematangan
Dibandingkan YOLOv8 nano (klasifier) dan MobileViT XXS (hibrida CNN dan *vision transformer*). Masukan 50 × 50 piksel; MobileViT dilatih dengan SGD, laju belajar 0,01, dan entropi silang kategorikal. Pada video, klasifikasi dijalankan hanya bila objek pertama kali terdeteksi atau keyakinan klasifikasi sebelumnya di bawah 0,8.

### 6. Rekonstruksi 3D dan penetapan buah ke pohon
COLMAP (SIFT, SfM, *plane sweep*) memproyeksikan buah terdeteksi ke ruang 3D mengikuti metode Liu dkk. Fitur hanya dihitung di sekitar objek terdeteksi dengan margin 5 piksel, dan hanya setiap bingkai ketiga dipakai. K-means dijalankan pada seluruh titik 3D dengan $k$ sama dengan jumlah pohon pada baris. Setiap buah mengambil kluster yang paling sering muncul pada titik fiturnya; pusat kluster diurutkan menurut sumbu $x$ untuk memberi ID pohon. Buah tanpa titik fitur ditetapkan dengan K tetangga terdekat (lima buah terdekat). Bila satu titik fitur dimiliki lebih dari satu buah, buah dianggap terhitung ulang; kriteria akhir penghapusan (kesamaan lebih dari separuh titik fitur) tertulis tidak lengkap dalam teks ekstraksi.

## Eksperimen dan Hasil
Detektor dievaluasi dengan presisi, *recall*, mAP50, dan mAP50-95 pada himpunan validasi dan uji; klasifikasi dengan akurasi, presisi, *recall*, dan F1. Hasil pada himpunan uji (Tabel 2, persen):

| Varian | Latih | Uji | Presisi | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|---|---|
| Nano | tanpa petak | tanpa petak | 72,6 | 56,8 | 63,6 | 30,3 |
| Small | tanpa petak | tanpa petak | 75,1 | 61,1 | 67,5 | 33,4 |
| Medium | tanpa petak | tanpa petak | 76,9 | 59,1 | 66,3 | 32 |
| Nano | petak | petak | 78,2 | 69,7 | 76 | 38 |
| Nano | tanpa petak | petak | 68,8 | 57,6 | 61,7 | 25,9 |
| Small | tanpa petak | petak | 67,9 | 61,8 | 63,6 | 25,8 |
| Nano | petak | tanpa petak | 69,1 | 48,6 | 56 | 23,1 |

Pada himpunan validasi (Tabel 1), Nano berpetak mencapai presisi 82,2%, *recall* 74,6%, mAP50 78,8%, dan mAP50-95 46%. Penulis menyimpulkan bahwa pelatihan berpetak membantu bila pengujian juga berpetak, dan hasilnya terburuk bila diuji tanpa petak. Model tanpa petak yang diuji dengan petak mendeteksi lebih banyak jeruk tetapi menambah *false positive* (daun berwarna mirip).

Klasifikasi kematangan (Tabel 3, persen):

| Model | Kelas | Akurasi validasi | Akurasi uji | Presisi uji | Recall uji | F1 uji |
|---|---|---|---|---|---|---|
| YOLOv8 nano | 2 | 68,3 | 70,7 | 70,9 | 69,4 | 70,1 |
| MobileViT XXS | 2 | 97,5 | 97,8 | 97,6 | 97,5 | 97,7 |
| MobileViT XXS | 3 | 85,2 | 86,9 | 86,9 | 87,4 | 86,6 |

Abstrak menyebut akurasi tiga kelas 86,7%, sedangkan Tabel 3 dan teks hasil menyebut 86,9%. Penurunan pada tiga kelas dikaitkan penulis dengan kelas matang sebagian dan ketidakseimbangan kelas.

Penghitungan pada video (Tabel 4 dan 5):

| Video | Pohon | Hitungan asli | Hitungan prediksi | Tingkat deteksi (%) |
|---|---|---|---|---|
| Video 1 | total | 358 | 303 | 84,6 |
| Video 2 | total | 589 | 441 | 74,8 |
| Video 1 | Pohon 1 | 358 | 303 | 84,6 |
| Video 2 | Pohon 1 | 196 | 120 | 61,2 |
| Video 2 | Pohon 2 | 286 | 258 | 90,2 |
| Video 2 | Pohon 3 | 107 | 63 | 58,8 |

Tingkat deteksi pada tabel adalah hitungan prediksi dibagi hitungan asli, dan seluruhnya di bawah 100%, yaitu hitungan kurang (*undercount*). Penulis mengakui varians hasil yang besar, dan secara kualitatif algoritma bekerja terbaik pada oklusi rendah. Penyebab hitungan kurang yang dinyatakan penulis adalah buah tersembunyi di balik daun yang tidak tampak dalam video; algoritma juga melewatkan sebagian objek saat gerakan cepat. Cara memperoleh hitungan asli (misalnya hitungan manual) tidak dijelaskan dalam teks.

## Kelebihan dan Keterbatasan
Kelebihan: alur lengkap dari deteksi, pelacakan, kematangan, hingga hitungan per pohon; evaluasi empat pengaturan petak yang menunjukkan pengaruh resolusi; klasifikasi kematangan jauh lebih baik dengan MobileViT daripada klasifier YOLOv8; dan penggunaan titik fitur 3D untuk mengenali buah yang terhitung ulang.

Keterbatasan yang dinyatakan penulis: sistem bekerja baik hanya bila kamera bergerak linear, sehingga buah di balik daun tidak terlihat dan tidak terdeteksi (disarankan pandangan 360 derajat); gerakan kamera yang mundur dapat merekam ulang buah yang sudah tercatat sehingga menambah risiko penghitungan ulang dan belum ditangani; penulis mengusulkan pengambilan dari udara dan aplikasi seluler sebagai pengembangan.

Menurut pembacaan ringkasan ini: (a) evaluasi hitungan hanya memakai dua video (empat pohon) sehingga bukti kuantitatif sangat terbatas; (b) tidak ada metrik galat hitung (seperti MAE atau MCE) atau analisis kontribusi tiap komponen (pelacakan, 3D) terhadap hasil akhir; (c) tidak ada ablasi yang memisahkan efek pembuangan buah terhitung ulang oleh titik fitur 3D; (d) hasil kematangan tidak dilaporkan per kelas pada hitungan video; (e) tabel ekstraksi mengandung nilai yang janggal (presisi 3,8 pada baris Nano berpetak/tanpa petak versi Tabel 1, dan "0,619" pada kolom mAP50 yang seharusnya persen), yang menunjukkan kemungkinan salah ketik di sumber.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan dua mekanisme: pelacakan Byte tracker antarbingkai dengan penyambungan ID antarpetak (jarak Euklides), dan rekonstruksi 3D SfM yang memungkinkan penilaian buah terhitung ulang berdasarkan titik fitur bersama dan penetapan buah ke pohon melalui K-means. Dengan demikian makalah ini memperlakukan identitas pada tingkat pohon dari video satu lintasan, bukan lintas sisi pohon secara eksplisit. Hitungan dilaporkan per video dan per pohon, bukan per kelas kematangan, walaupun kematangan diklasifikasikan. Acuan hitungnya adalah "hitungan asli" per video; sumbernya (manual atau lainnya) tidak dijelaskan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: penggunaan titik fitur 3D bersama untuk menandai buah yang sama pada pandangan berbeda, penetapan buah ke pohon dengan pengelompokan 3D, dan penyambungan ID di batas petak. Namun, evaluasi sangat kecil dan menunjukkan hitungan kurang yang besar pada pohon beroklusi tinggi, dan penulis sendiri mencatat bahwa pandangan 360 derajat diperlukan agar buah yang tersembunyi tertangkap.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hassan2025orange`.

Hassan dkk. (2025) mengusulkan estimasi hasil jeruk per pohon dari video dengan YOLOv8 pada citra berpetak 2 × 2, Byte tracker dengan penyambungan ID antarpetak, klasifikasi kematangan MobileViT, serta rekonstruksi 3D COLMAP dan K-means untuk menetapkan buah ke pohon dan mengurangi penghitungan ganda. Pelatihan dan pengujian berpetak menghasilkan mAP50 76% pada data uji (YOLOv8 nano), dan pada dua video uji tingkat deteksi masing-masing 84,6% dan 74,8%, dengan hasil per pohon antara 58,8% dan 90,2%.

Catatan verifikasi data: Presisi, *recall*, mAP50, dan mAP50-95 detektor berasal dari Tabel 1 dan Tabel 2; akurasi klasifikasi dari Tabel 3 (abstrak menyebut 86,7% untuk tiga kelas, tabel dan teks 86,9%); hitungan video dari Tabel 4 dan Tabel 5. Total hitungan Video 2 (589 asli, 441 prediksi) konsisten dengan jumlah ketiga pohon (dijumlahkan dalam ringkasan ini: 196 + 286 + 107 dan 120 + 258 + 63). Beberapa sel pada ekstraksi tabel tampak tidak wajar (presisi 3,8; nilai 0,619) dan tidak dikutip. Cara memperoleh hitungan asli, hasil video ketiga (tak linear), serta galat hitung per kelas tidak dilaporkan. Teks bagian akhir bagian 4.5 terpotong pada kalimat kriteria penghapusan buah terhitung ulang. Data tersedia atas permintaan kepada penulis.
