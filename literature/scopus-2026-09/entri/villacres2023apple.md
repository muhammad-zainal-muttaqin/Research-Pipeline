# Apple orchard production estimation using deep learning strategies: A comparison of tracking-by-detection algorithms

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `villacres2023apple` |
| Judul asli | Apple orchard production estimation using deep learning strategies: A comparison of tracking-by-detection algorithms |
| Penulis | Villacr\'es, Juan; Viscaino, Michelle; Delpiano, Jos\'e; Vougioukas, Stavros; Auat Cheein, Fernando |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [villacres2023apple.pdf](../pdf/villacres2023apple.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107513

## Gambaran Umum
Makalah ini membandingkan lima algoritma pelacakan berbasis deteksi (*tracking-by-detection*) untuk mencacah apel dari video yang direkam dengan kamera genggam yang berjalan menyusuri baris kebun. Algoritma yang dibandingkan adalah *Kalman Filter* (KF), *Kernelized Correlation Filter* (KCF), *Multi Hypothesis Tracking* (MHT), *Simple Online Real-Time Tracking* (SORT), dan *Deep Simple Online Real-Time Tracking* (DeepSORT). Setiap apel diberi pengenal (*identifier*, ID) yang dipertahankan sepanjang urutan bingkai, sehingga buah yang tampak pada banyak bingkai dihitung sekali. Penulis juga membangun dua basis data video apel berformat *Multiple Object Tracking* (MOT) dan menyatakan bahwa tidak ada basis data publik pelacakan buah sebelumnya.

Evaluasi dilakukan dalam dua tahap. Tahap pertama adalah analisis sensitivitas dengan deteksi acuan yang dikurangi secara acak (probabilitas deteksi 1,0 sampai 0,2) dan dengan laju bingkai yang diturunkan dari 30 menjadi 15, 10, dan 5 bingkai per detik. Tahap kedua adalah studi kasus dengan detektor sungguhan (YoloV5l dan Faster R-CNN) yang dilatih pada data publik berbeda dari data pelacakan.

Pada deteksi sempurna, MHT mencapai *Multiple Object Tracking Accuracy* (MOTA) 97,00 % dan DeepSORT 93,00 %. Pada studi kasus, DeepSORT memberi galat hitung relatif rerata terendah, yaitu 20,1 % dengan YoloV5 dan 31,5 % dengan Faster R-CNN. KF memberi galat 20,5 % dan 31,9 % dan penulis menyebut hasil ini serupa secara statistik. Seluruh hitungan adalah satu kelas (apel).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil kebun otomatis diperlukan untuk pengelolaan panen, penyimpanan, dan transportasi. Penghitungan manual pada beberapa cabang sampel yang diekstrapolasi ke seluruh blok dinyatakan memakan waktu dan dapat salah hingga 66 % (merujuk Meena dkk., 2014). Tahap deteksi buah sudah berkembang pesat dengan pembelajaran mendalam, tetapi tahap pencacahan dinyatakan masih bermasalah: bila urutan citra tumpang tindih dan tidak ditangani dengan benar, buah terhitung berulang sehingga hasil terlalu tinggi.

Dua cara untuk menghindari penghitungan ganda dibahas. Cara pertama memakai urutan bingkai yang tidak tumpang tindih, dengan kecepatan kamera konstan dan frekuensi subsampel yang tepat. Kelemahannya adalah galat pemilihan frekuensi atau kecepatan tidak konstan menyebabkan tumpang tindih, dan tidak semua buah terlihat dari sudut pandang kamera. Cara kedua memberi pengenal unik pada tiap buah sepanjang urutan citra (MOT), yang selama ini terutama dipakai untuk pelacakan pejalan kaki pada basis data seperti MOT15, MOT16, dan MOT17. Penulis menyatakan bahwa tidak ada basis data publik MOT untuk buah sehingga kinerja pelacak sulit dibandingkan, dan studi terdahulu memakai kondisi serta metrik yang berbeda-beda.

## Ide Utama
Gagasan utama adalah mengevaluasi pelacak dengan cara yang seragam pada dua basis data MOT baru, dan memisahkan pengaruh kualitas deteksi dari pengaruh algoritma pelacak. Pemisahan itu dilakukan lewat analisis sensitivitas: kotak acuan (*ground truth*) dihapus secara acak sehingga probabilitas deteksi turun bertahap, kemudian laju bingkai diturunkan dengan parameter pelacak yang tetap pada nilai untuk 30 bingkai per detik. Setelah itu, pelacak diuji dengan detektor pembelajaran mendalam yang dilatih pada data yang tidak berkorelasi dengan data pelacakan agar skenarionya realistis.

Kesimpulan penulis adalah bahwa pelacak yang menggabungkan gerak dan penampilan (DeepSORT) tampak lebih cocok untuk kebun daripada pelacak yang hanya memakai gerak, dan bahwa model kecepatan konstan cukup baik bila kamera bergerak relatif stabil.

## Cara Kerja Langkah demi Langkah

```
  [Video kamera genggam] -> [Detektor apel: YoloV5l / Faster R-CNN]
        -> [Kotak pembatas per bingkai] -> [Pelacak: KF / KCF / MHT /
           SORT / DeepSORT] -> [ID unik per apel] -> [Jumlah pelacak = hitungan]
```

### 1. Akuisisi data pelacakan
Dua basis data pelacakan dikumpulkan di satu kebun di California, AS (38°03'55,4"N 121°11'45,4"W) pada tahun 2016 dan 2021. Perekaman memakai kamera genggam berorientasi vertikal sambil seseorang berjalan menyusuri baris. Video 2016 direkam dengan iPhone 6s plus (12 megapiksel) dan video 2021 dengan iPhone 13 (12 megapiksel). Basis data 2016 terdiri atas sembilan video (T1 sampai T9), dengan resolusi 1920 x 1080 pada 30 bingkai per detik atau 1280 x 720 pada 120 bingkai per detik (Tabel 1). Basis data 2021 terdiri atas tujuh video beresolusi 1920 x 1080 pada 30 bingkai per detik, masing-masing satu menit atau 1.800 bingkai. Kecepatan perekaman tidak dicatat secara akurat; penulis memperkirakannya dengan aliran optik Lucas-Kanade dan menyatakan bahwa pada kasus terburuk (video 2 tahun 2021) variansnya tidak melebihi 14 % dari kecepatan rerata. Semua video dianotasi dalam format MOT dengan *Computer Vision Annotation Tool* (CVAT) dengan satu kelas; penganotasi dapat kembali ke bingkai sebelumnya bila apel hijau yang mirip daun akhirnya terlihat jelas.

### 2. Data pelatihan detektor
Tiga basis data publik digabung dan labelnya diubah menjadi kotak pembatas: MinneApple (1.000 citra, lebih dari 41.000 apel), WSU (bagian *Crop Load Estimation*, 238 citra), dan Fuji-SfM (sub-citra 1024 x 1024). Pembagian data (Tabel 2) adalah 670 citra latih dan 330 validasi untuk MinneApple, 166 dan 72 untuk WSU, serta 231 dan 57 untuk Fuji-SfM, atau 1.067 latih dan 459 validasi secara total.

### 3. Deteksi
Faster R-CNN memakai kotak jangkar berdasarkan panduan Gené-Mola dkk. (2019) untuk apel (rasio aspek 1:1, skala 4). YoloV5 dipakai dalam varian YoloV5l (46,5 juta parameter, masukan 640 piksel). Pada validasi, AP@0,5 adalah 75,13 % untuk Faster R-CNN dan 72,67 % untuk YoloV5.

### 4. Pelacakan dan pencacahan
Kelima pelacak bekerja pada kotak pembatas hasil deteksi. KF memprediksi keadaan kotak (pusat, kecepatan, lebar, tinggi) lalu mengasosiasikan prediksi dengan deteksi baru memakai matriks biaya *intersection over union* (IoU) dan algoritma Hungaria; pelacak baru dibuat untuk deteksi tanpa pasangan dan pelacak dihapus setelah beberapa bingkai tanpa asosiasi. Jendela prediksi KF diatur 8 bingkai secara heuristik untuk 30 bingkai per detik. KCF melatih satu pelacak per apel dengan fitur *histogram of oriented gradients* (HOG) dan korelasi dalam domain Fourier, tanpa model gerak. MHT mempertahankan banyak hipotesis lintasan dalam pohon lintasan dan memilih hipotesis global terbaik. SORT memakai KF dengan keadaan kotak (termasuk luas dan rasio aspek) dan asosiasi IoU saja. DeepSORT menambahkan deskriptor penampilan dari jaringan konvolusi, dengan jarak Mahalanobis dan jarak kosinus, serta pencocokan bertingkat (*matching cascade*); deskriptornya dilatih dengan urutan rerata 8 bingkai dan sekitar 1.500 apel. Hitungan akhir adalah jumlah pelacak yang dibuat sampai bingkai tertentu.

### 5. Analisis sensitivitas dan metrik
Probabilitas deteksi divariasikan 1,0; 0,8; 0,6; 0,4; dan 0,2 dengan menghapus kotak acuan secara acak (distribusi seragam). Laju bingkai diturunkan dengan faktor 2, 3, dan 6 (15, 10, dan 5 bingkai per detik). Metrik pelacakan adalah MOTA. Untuk hitungan, galat relatif per bingkai $\varepsilon_{rel} = |N_{actual} - N_{est}| / N_{actual} \times 100\%$ dirata-ratakan sepanjang video, karena galat pada bingkai terakhir bergantung pada titik berhenti video. $N_{actual}$ berasal dari hitung manual pada citra.

## Eksperimen dan Hasil
Analisis sensitivitas dilakukan pada tujuh video basis data 2021 (jumlah apel acuan 8.447 menurut Tabel A.1). Studi kasus dengan detektor sungguhan memakai basis data 2016 (Gambar 9).

MOTA rerata (Gambar 8 dan Tabel A.1) menurut probabilitas deteksi pada 30 bingkai per detik:

| Pelacak | 100 % | 80 % | 60 % | 40 % | 20 % |
|---|---|---|---|---|---|
| KF | 74,90 % | 74,30 % | 68,90 % | 55,60 % | 18,70 % |
| KCF | 75,30 % | 65,30 % | 47,50 % | 28,60 % | 12,90 % |
| MHT | 97,00 % | 96,40 % | 89,80 % | 9,00 % | 0,60 % |
| SORT | 94,60 % | 44,30 % | 13,80 % | 2,80 % | 0,30 % |
| DeepSORT | 93,00 % | 85,90 % | 69,30 % | 40,50 % | 7,50 % |

Pada penurunan laju bingkai (Tabel 3), parameter pelacak tidak disetel ulang. KF dan KCF menghasilkan MOTA mendekati nol atau negatif; misalnya pada 5 bingkai per detik dan deteksi 100 %, KF mencapai -119,6 % dan KCF -47,4 %. SORT adalah yang terbaik pada deteksi 100 % di ketiga laju (80,5 % pada 15, 60,4 % pada 10, dan 14,5 % pada 5 bingkai per detik). Pada deteksi 80 % dan di bawahnya, MHT dan DeepSORT lebih baik pada 15 dan 10 bingkai per detik (misalnya pada 15 bingkai per detik dan deteksi 80 %: MHT 59,4 % dan DeepSORT 64,5 % dibandingkan SORT 36,9 %). Pada 5 bingkai per detik, semua pelacak mendekati nol.

Studi kasus (Gambar 9, galat hitung relatif rerata pada basis data 2016):

| Pelacak | Detektor YoloV5 | Detektor Faster R-CNN |
|---|---|---|
| DeepSORT | 20,1 % | 31,5 % |
| KF | 20,5 % | 31,9 % |
| MHT | 32,5 % | 37,1 % |
| SORT | di atas 50 % | di atas 50 % |
| KCF | di atas 75 % | di atas 90 % |

Penulis juga melaporkan faktor oklusi (*occlusion factor*, OF; rasio buah sebenarnya terhadap hitungan citra, dirata-ratakan per bingkai) sebesar 1,6129 (YoloV5) dan 1,5152 (Faster R-CNN) untuk basis data 2016, serta 1,2085 dan 1,1333 untuk basis data 2021. Tidak ada koreksi hitungan memakai OF yang dilaporkan.

## Kelebihan dan Keterbatasan
Kelebihan makalah ini adalah perbandingan lima pelacak pada basis data yang sama dengan metrik seragam, pemisahan pengaruh detektor dan pelacak lewat analisis sensitivitas, pemakaian data latih detektor yang tidak berkorelasi dengan data uji, dan penyediaan basis data MOT apel secara publik (disebut tersedia di repositori; kontak penulis diberikan bila tautan bermasalah).

Keterbatasan yang dinyatakan penulis: analisis sensitivitas tidak memasukkan deteksi positif palsu, yang menurut penulis dapat menjelaskan mengapa MHT unggul pada sensitivitas tetapi tidak pada studi kasus, dan penulis menyatakan penelitian lanjutan diperlukan untuk menambahkan positif palsu. Parameter KF dan KCF disetel secara heuristik untuk 30 bingkai per detik sehingga performanya memburuk pada laju bingkai lebih rendah. Oklusi dapat berbeda antarpohon dan terdapat oklusi saat akuisisi dan pembuatan acuan; penulis menyarankan pohon kalibrasi sebagaimana direkomendasikan Anderson dkk. (2021). Kecepatan kamera tidak diukur dengan RTK. Hitungan akan terlalu rendah bila detektor gagal karena oklusi daun, dan terlalu tinggi bila buah tampak, tertutup, lalu tampak lagi sehingga pelacak baru dibuat.

Menurut pembacaan ringkasan ini, ada beberapa keterbatasan tambahan. Pertama, seluruh data berasal dari satu kebun apel di satu lokasi dan satu kelas, tanpa hitungan per kelas. Kedua, pelacakan hanya memakai satu pandang bergerak (satu sisi baris); tidak ada upaya mencocokkan buah antarsisi pohon. Ketiga, galat hitung 20,1 % pada skenario terbaik tergolong besar, dan makalah tidak membandingkan hitungan dengan hasil panen sebenarnya. Keempat, hasil sensitivitas (basis data 2021) dan hasil studi kasus (basis data 2016) berasal dari basis data yang berbeda sehingga tidak dapat dibaca sebagai satu rangkaian percobaan. Kelima, jumlah ulangan atau uji statistik untuk pernyataan "serupa secara statistik" antara DeepSORT dan KF tidak dirinci dalam teks.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan pelacakan multi-objek berbasis deteksi (*multi-object tracking*, MOT): ID unik dipertahankan antarbingkai dan hitungan adalah jumlah pelacak yang dibuat. Mekanisme asosiasinya adalah IoU dengan algoritma Hungaria (KF, SORT), korelasi penampilan HOG (KCF), pohon hipotesis (MHT), serta gerak ditambah penampilan CNN (DeepSORT). Makalah ini bukan metode lintas sisi pohon; satu pandang bergerak dipakai dan pada bagian karya terkait penulis hanya meninjau metode dua sisi dan multi-pandang milik pihak lain.

Hitungan dilaporkan sebagai total apel per video (satu kelas), bukan per kelas. Acuan hitungnya adalah hitung manual pada citra video (jumlah kumulatif apel yang dianotasi), bukan hasil panen. Hal yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah kerangka evaluasi pelacak terhadap kualitas deteksi (analisis sensitivitas), temuan bahwa pelacak berbasis gerak dan penampilan lebih tahan terhadap deteksi yang hilang, kepekaan pelacak terhadap laju bingkai dan parameter jendela prediksi, serta metrik galat relatif kumulatif. Pelacakan bingkai ke bingkai itu sendiri tidak menyelesaikan identitas antarsisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `villacres2023apple`.

Villacrés dkk. (2023) membandingkan lima pelacak berbasis deteksi (KF, KCF, MHT, SORT, DeepSORT) untuk mencacah apel dari video kamera genggam pada dua basis data MOT baru. Pada deteksi sempurna, MHT mencapai MOTA 97,00 % dan DeepSORT 93,00 %. Dengan detektor sungguhan, DeepSORT memberi galat hitung rerata terendah, yaitu 20,1 % (YoloV5) dan 31,5 % (Faster R-CNN), dengan KF yang hampir sama (20,5 % dan 31,9 %). Penulis menyimpulkan bahwa pelacak berbasis gerak dan penampilan lebih sesuai untuk kebun.

Catatan verifikasi data: MOTA pada deteksi 100 % sampai 20 % berasal dari Gambar 8, teks seksi 4.1, dan Tabel A.1 (lampiran). MOTA pada laju bingkai berbeda berasal dari Tabel 3 (hanya sebagian yang dikutip di atas). Galat hitung berasal dari seksi 4.2 dan Gambar 9, yang tidak memuat angka numerik untuk SORT dan KCF selain batas bawah ("di atas 50 %", "di atas 75 %" dan "di atas 90 %"). Abstrak menyebut galat 20,07 % dan 31,52 % sedangkan isi teks membulatkan menjadi 20,1 % dan 31,5 %. Teks menyebut galat hitung DeepSORT 20,1 % sebagai "detection error" pada kesimpulan, yang dibaca di sini sebagai galat hitung. Tabel 1 dalam teks ekstraksi tidak sepenuhnya konsisten: judulnya mengacu pada "databases used for the object detector pipelines in the case study" sementara isinya adalah daftar sembilan video (T1 sampai T9, kolom total apel 8.845), dan penjumlahan kolom apel per video tidak sama dengan total yang tertulis, sehingga angka total tersebut tidak dipakai di entri ini. Jumlah apel acuan 8.447 untuk analisis sensitivitas berasal dari Tabel A.1. Tidak dilaporkan: jumlah apel per video basis data 2021, jumlah pohon, kultivar, dan nilai OF yang dipakai untuk koreksi. Gambar tidak tersedia dalam teks ekstraksi.
