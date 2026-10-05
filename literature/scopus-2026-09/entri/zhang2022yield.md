# Yield and maturity estimation of apples in orchards using a 3-step deep learning-based method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022yield` |
| Judul asli | Yield and maturity estimation of apples in orchards using a 3-step deep learning-based method |
| Penulis | Zhang, Xinxing; Song, Zhuping; Liang, Qianyue; Gao, Shumin |
| Tahun | 2022 |
| Venue | Quality Assurance and Safety of Crops and Foods |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [zhang2022yield.pdf](../pdf/zhang2022yield.pdf)
- DOI resmi: https://doi.org/10.15586/qas.v14i2.1008

## Gambaran Umum
Makalah ini menyajikan metode tiga langkah berbasis pembelajaran mendalam untuk memperkirakan hasil panen dan tingkat kematangan apel di kebun dari citra RGB. Langkah pertama adalah jaringan deteksi satu tahap bernama Deep-count (varian YOLOv4 dengan *backbone* ResNet-101 dan PANet berkonvolusi *depth-wise*) yang menghitung apel terlihat dari sisi depan dan sisi belakang pohon. Langkah kedua adalah jaringan klasifikasi (EfficientNet-b4) yang menyaring objek salah deteksi sekaligus mengelompokkan apel menjadi matang dan belum matang. Langkah ketiga adalah algoritma estimasi beban buah yang mengalikan jumlah buah terlihat dari kedua sisi dengan faktor koreksi per kebun untuk memperhitungkan buah yang tersembunyi.

Data dikumpulkan di tiga kebun apel di Qingdao, Provinsi Shandong, Tiongkok, pada September sampai Oktober 2020, berupa 944 citra dari 472 pohon (satu citra sisi depan dan satu citra sisi belakang per pohon) dengan kamera Intel RealSense D-435i beresolusi 1920 x 1080. Pada perbandingan kesalahan estimasi hasil terhadap hitungan manual, metode yang diusulkan memperoleh galat 4,3 ± 1,08 %, 4,93 ± 0,83 %, dan 4,25 ± 1,47 % untuk kebun A, B, dan C, lebih rendah dari YOLOv3, YOLOv4, dan Faster R-CNN pada ketiga kebun. Jaringan klasifikasi memperoleh F1 rerata 0,92 dan akurasi 0,96 untuk tiga kelas (salah deteksi, matang, belum matang).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkiraan hasil dan kematangan apel sebelum panen penting untuk pengelolaan tenaga kerja. Penulis menyatakan bahwa petani lazimnya memperkirakan hasil dengan mengambil sampel beberapa pohon acak dan menduga kematangan berdasarkan pengalaman, yang tidak akurat dan tidak efisien. Metode berbasis ambang warna atau bentuk dan metode pembelajaran mesin tradisional (SVM, model campuran Gauss) bergantung pada fitur yang ditentukan lebih dahulu sehingga kurang tahan terhadap perubahan cahaya, rotasi, dan skala.

Metode pembelajaran mendalam sudah banyak dipakai untuk deteksi buah dan klasifikasi kematangan, tetapi penghitungan yang akurat masih sulit karena salah hitung saat deteksi. Penulis juga mencatat bahwa penelitian yang memperkirakan hasil dan kematangan sekaligus di kebun masih terbatas. Karena itu dua perbaikan yang dituju adalah peningkatan akurasi hitungan dan estimasi hasil bersama kematangan.

## Ide Utama
Gagasan utama adalah memisahkan tugas deteksi dari tugas penyaringan dan klasifikasi: detektor dirancang berdaya ingat (*recall*) tinggi dengan presisi relatif lebih rendah, kemudian jaringan klasifikasi citra potongan buah menghapus salah deteksi dan menetapkan kematangan. Hitungan dari dua sisi pohon dijumlahkan lalu dikoreksi dengan faktor yang dikalibrasi terhadap hitungan manual per kebun.

Penulis menyatakan bahwa detektor adalah kunci akurasi estimasi hasil, dan bahwa kombinasi arsitektur detektor yang dioptimalkan dengan jaringan klasifikasi halus diperlukan untuk presisi estimasi hasil berbasis citra.

## Cara Kerja Langkah demi Langkah

```
 Citra sisi depan + citra sisi belakang (per pohon)
              |
              v
 Deteksi (Deep-count: ResNet-101 + PANet) --> kotak apel
              |
              v
 Potong kotak --> Klasifikasi (EfficientNet-b4)
              |        salah deteksi | matang | belum matang
              v
 N_total = r x (N_depan + N_belakang)
```

### 1. Akuisisi data
Citra diambil di tiga kebun apel di Qingdao, Shandong, pada September sampai Oktober 2020, mulai sekitar enam minggu sebelum musim panen hingga sebagian besar apel matang secara komersial. Apel yang difoto enam minggu sebelum panen umumnya pucat dan menjadi merah terang dua minggu kemudian. Pengambilan memvariasikan cuaca (berawan, setengah berawan, cerah) dan waktu (pagi, siang, sore). Untuk tiap pohon diambil satu citra sisi depan dan satu citra sisi belakang dengan sudut pandang acak, memakai Intel RealSense D-435i beresolusi 1920 x 1080. Pohon diberi nomor dan nama berkas citra mengikuti nomor pohon agar citra kedua sisi dapat dipasangkan. Total 944 citra dari 472 pohon. Kultivar apel tidak dilaporkan dalam teks.

### 2. Anotasi dan pembagian data
Untuk detektor, citra diubah ukurannya menjadi 480 x 414 piksel dan dianotasi dengan LabelMe dalam format PASCAL VOC; hanya apel berukuran lebih dari 32 x 32 piksel yang dianotasi. Untuk klasifikasi, wilayah tiap apel dipotong dari label deteksi dan diubah ukurannya menjadi 112 x 112 piksel. Tiga pakar manusia memberi label secara independen ke tiga kelas (objek salah deteksi, apel matang, apel belum matang), dan kelas akhir adalah yang disepakati ketiganya. Hasilnya 944 citra deteksi dan 2.400 citra klasifikasi, dengan 1.172 citra apel belum matang dan sisanya apel matang (sesuai teks; jumlah kelas salah deteksi tidak dirinci dan tidak jelas dari teks). Pembagian data 50 % latih, 25 % validasi, 25 % uji. Augmentasi pada citra deteksi mencakup kecerahan, saturasi warna, ketajaman, potong, rotasi (-30 sampai 30 derajat), dan translasi (-150 sampai 150 piksel); augmentasi klasifikasi serupa tanpa pemotongan.

### 3. Jaringan deteksi Deep-count
Deep-count mengikuti arsitektur YOLOv4 dengan *backbone* ResNet (diuji ResNet-34, ResNet-50, ResNet-101) dan MobileNet-V2 sebagai pembanding, memakai peta fitur C3, C4, dan C5, lalu jaringan agregasi jalur (PANet) dua arah. Penulis memodifikasi PANet dengan konvolusi *depth-wise* untuk efisiensi dan membandingkannya dengan FPN. Ambang keyakinan penekanan non-maksimum ditetapkan 0,5. Detektor diimplementasikan di TensorFlow 1.15 dengan *backbone* berbobot ImageNet, dilatih dengan Adam (laju belajar 0,001, peluruhan 0,9 per epoch), ukuran *batch* 32, 80 epoch, dan penghentian dini; GPU yang dipakai adalah GTX 1080Ti.

### 4. Jaringan klasifikasi
Dibandingkan VGG-19, MobileNet-V2, ResNet-50, ResNet-101, DenseNet, dan EfficientNet-b4 pada data yang sama. Pelatihan memakai Adam, 40 epoch, ukuran *batch* 64 (diimplementasikan di PyTorch).

### 5. Estimasi hasil per pohon
Rumus estimasi adalah $N_{total} = r(N_{front} + N_{back})$. Faktor koreksi $r$ dihitung sebagai rasio jumlah buah hasil hitungan manual terhadap jumlah dari citra kedua sisi. Teks menyebut sampel acak 15 pohon per kebun pada metodologi, tetapi lima sampai delapan pohon pada hasil eksperimen. Dari hasil per pohon ini, beban buah kebun diperkirakan dengan mengulang operasi untuk sejumlah pohon. Tidak ada pencocokan buah yang sama antara dua sisi pohon; buah yang terlihat dari kedua sisi dan buah tersembunyi dikompensasi hanya oleh faktor $r$.

## Eksperimen dan Hasil
### Deteksi
Perbandingan arsitektur deteksi (Tabel 2 makalah):

| Model | Backbone | Precision | Recall | F1 | Waktu |
|---|---|---|---|---|---|
| YOLO-V4 | DarkNet 53 lapis | 0,92 | 0,93 | 0,92 | 78 ms |
| Deep-count (PANet) | ResNet-34 | 0,84 | 0,88 | 0,85 | 35 ms |
| Deep-count (PANet) | MobileNet-V2 (1,4) | 0,87 | 0,84 | 0,86 | 32 ms |
| Deep-count (PANet) | ResNet-50 | 0,92 | 0,91 | 0,91 | 44 ms |
| Deep-count (FPN) | ResNet-101 | 0,88 | 0,92 | 0,89 | 67 ms |
| Deep-count (PANet) | ResNet-101 | 0,92 | 0,95 | 0,94 | 53 ms |

Perbandingan dengan jaringan deteksi lain (Tabel 3): SSD F1 0,83 (57 ms); Faster R-CNN F1 0,87 (154 ms); YOLOv3 F1 0,88 (64 ms); Deep-count (FPN) 0,89 (67 ms); YOLOv4 0,92 (78 ms); Deep-count (PANet) 0,94 (53 ms).

### Klasifikasi
Hasil jaringan klasifikasi (Tabel 4 makalah):

| Model | Precision | Recall | Mean F1 | ACC |
|---|---|---|---|---|
| VGG-19 | 0,76 | 0,71 | 0,73 | 0,82 |
| MobileNet-V2 (1,4) | 0,86 | 0,72 | 0,78 | 0,86 |
| ResNet-50 | 0,86 | 0,82 | 0,84 | 0,89 |
| ResNet-101 | 0,88 | 0,86 | 0,87 | 0,91 |
| DenseNet (k = 24) | 0,89 | 0,91 | 0,90 | 0,93 |
| EfficientNet-b4 | 0,91 | 0,92 | 0,92 | 0,96 |

Galat klasifikasi terutama muncul saat membedakan apel matang dari belum matang karena variasi cahaya dan warna.

### Estimasi hasil
Faktor koreksi per kebun (Tabel 5): kebun A 1,090 ± 0,080 (rerata citra 23,7; rerata manual 25,6), kebun B 1,040 ± 0,127 (37,2; 33,8), kebun C 0,954 ± 0,060 (28,4; 26,4); faktor ditentukan dari lima sampai delapan pohon per kebun. Perbandingan galat estimasi hasil (Tabel 6 makalah; hitungan rerata per pohon):

| Kebun | Metode | Rerata citra | Rerata manual | Galat (%) |
|---|---|---|---|---|
| A | Diusulkan | 24,5 | 25,6 | 4,3 ± 1,08 |
| A | Faster R-CNN | 24,2 | 25,6 | 5,46 ± 1,77 |
| A | YOLOv3 | 23,6 | 25,6 | 7,8 ± 2,24 |
| A | YOLOv4 | 27,1 | 25,6 | 5,86 ± 1,12 |
| B | Diusulkan | 36,2 | 34,5 | 4,93 ± 0,83 |
| B | Faster R-CNN | 32,4 | 34,5 | 6,08 ± 1,89 |
| B | YOLOv3 | 32,1 | 34,5 | 7,26 ± 2,54 |
| B | YOLOv4 | 36,6 | 34,5 | 5,21 ± 1,07 |
| C | Diusulkan | 29,4 | 28,2 | 4,25 ± 1,47 |
| C | Faster R-CNN | 30,6 | 28,2 | 8,5 ± 1,95 |
| C | YOLOv3 | 25,9 | 28,2 | 8,15 ± 2,56 |
| C | YOLOv4 | 26,0 | 28,2 | 7,3 ± 1,22 |

Faktor koreksi yang sama dipakai untuk keempat model pada tiap kebun.

## Kelebihan dan Keterbatasan
Kelebihan: hanya kamera RGB yang diperlukan; estimasi hasil dan kematangan dilakukan sekaligus; label kematangan dan salah deteksi disepakati tiga pakar; pemisahan deteksi berdaya ingat tinggi dan klasifikasi penyaring terbukti memberi galat estimasi lebih rendah daripada detektor pembanding pada tiga kebun; pengambilan data mencakup beberapa kondisi cahaya, cuaca, dan tahap kematangan.

Keterbatasan yang dinyatakan penulis: jaringan mungkin melewatkan sebagian kecil objek yang kecil atau tertutup akibat cahaya dan sudut kamera; galat klasifikasi terutama terjadi antara apel matang dan belum matang karena variasi cahaya dan warna; data meskipun bervariasi belum sepenuhnya meniru kompleksitas lingkungan kebun; buah tersembunyi daun tetap menyebabkan salah deteksi sehingga diperlukan faktor koreksi.

Menurut pembacaan ringkasan ini, estimasi hasil bergantung pada faktor koreksi yang dikalibrasi dengan hitungan manual pada sampel pohon dari kebun yang sama, sehingga tidak berlaku tanpa kalibrasi ulang di kebun lain, dan rentang simpangan baku faktor (misalnya ±0,127) belum diteruskan ke galat estimasi. Menurut pembacaan ringkasan ini, citra dari dua sisi pohon dijumlahkan tanpa pencocokan buah, sehingga buah yang tampak dari kedua sisi dapat terhitung ganda dan hanya dikompensasi oleh faktor $r$ yang tunggal. Menurut pembacaan ringkasan ini, hasil estimasi hasil dilaporkan dalam hitungan rerata per pohon (puluhan buah per pohon) dari sampel yang kecil, dan tidak ada hasil kematangan per kelas pada tingkat hitungan pohon; evaluasi kematangan hanya pada tingkat klasifikasi potongan citra. Menurut pembacaan ringkasan ini, teks memuat ketidakkonsistenan angka (lihat catatan verifikasi), sehingga angka tabel perlu dirujuk langsung.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari dua sisi pohon (depan dan belakang) dengan mekanisme koreksi statistik dua sisi: hitungan dari kedua citra dijumlahkan lalu dikalikan faktor $r$ per kebun yang dikalibrasi terhadap hitungan manual. Tidak ada pelacakan, pencocokan multi-pandang, atau rekonstruksi 3D; tidak ada upaya mengenali apel yang sama pada kedua sisi. Buah yang terlihat dari kedua sisi dan buah tersembunyi dikompensasi secara agregat oleh $r$ yang bernilai di sekitar 1 (0,954 sampai 1,090).

Hitungan estimasi hasil tidak dilaporkan per kelas kematangan; kematangan dinilai hanya pada klasifikasi potongan citra (F1 0,92, akurasi 0,96) tanpa hitungan pohon per kelas. Acuan hitungan adalah hitungan manual buah per pohon di lapangan pada pohon sampel (lima sampai delapan pohon untuk kalibrasi menurut hasil, atau 15 menurut metodologi), bukan hasil panen dan bukan anotasi citra. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan dua pandang dengan faktor koreksi yang dikalibrasi terhadap hitungan lapangan, serta pemisahan deteksi dan klasifikasi kematangan; keterbatasannya adalah ketiadaan pengenalan identitas lintas sisi dan hitungan per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhang2022yield`.

Ringkasan yang aman dikutip: Zhang dkk. (2022) mengusulkan metode tiga langkah untuk estimasi hasil dan kematangan apel: detektor Deep-count (ResNet-101 dengan PANet) menghitung apel terlihat dari sisi depan dan belakang pohon, jaringan EfficientNet-b4 menyaring salah deteksi dan mengklasifikasikan matang atau belum matang (F1 0,92; akurasi 0,96), dan jumlah dua sisi dikalikan faktor koreksi per kebun yang dikalibrasi dengan hitungan manual. Pada 944 citra dari 472 pohon di tiga kebun di Qingdao, galat estimasi hasil adalah 4,3 %, 4,93 %, dan 4,25 %, lebih rendah dari YOLOv3, YOLOv4, dan Faster R-CNN, tanpa pencocokan buah antarsisi pohon.

Catatan verifikasi data: Jumlah citra dan pohon berasal dari bagian Image collection; jumlah citra klasifikasi dan pembagian data dari bagian Image data labelling; hasil deteksi dari Tabel 2 dan Tabel 3; klasifikasi dari Tabel 4; faktor koreksi dari Tabel 5; galat estimasi dari Tabel 6 dan teks pada bagian Experimental on Yield Estimation. Teks makalah memuat beberapa ketidakkonsistenan: (1) teks hasil menyebut Deep-count F1 0,92, recall 0,94, precision 0,91, sedangkan Tabel 3 dan Tabel 2 menunjukkan precision 0,92, recall 0,95, F1 0,94; (2) Tabel 2 memuat YOLO-V4 pada kelompok Deep-count dan Tabel 3 memuat SSD, yang tidak disebut dalam teks; (3) metodologi menyebut sampel 15 pohon per kebun untuk faktor $r$, sedangkan hasil menyebut lima sampai delapan pohon; (4) rasio rerata manual terhadap rerata citra pada Tabel 5 (misalnya 25,6/23,7 sekitar 1,08, dihitung; 33,8/37,2 sekitar 0,91, dihitung) tidak sama dengan koefisien yang dicantumkan untuk kebun B, dan rerata manual kebun B pada Tabel 5 (33,8) berbeda dari Tabel 6 (34,5); (5) kesimpulan menyebut "ResNet-10" dan "EfficientNet-64", yang tampaknya salah ketik untuk ResNet-101 dan EfficientNet-b4. Jumlah apel total, kultivar, jumlah pohon yang diuji per kebun untuk estimasi hasil, jumlah citra kelas salah deteksi, dan perincian pembagian data per kebun tidak dilaporkan. Gambar 6 (grafik galat per pohon) tidak dapat diverifikasi dari teks. Ekstraksi teks memuat potongan kecil pada awal bagian Augmentasi, tetapi isinya masih dapat dibaca.
