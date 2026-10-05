## Gambaran Umum
Makalah ini mengusulkan *twice matched fruit counting system*, yaitu alur pencacahan apel otomatis dari video baris pohon di kebun apel modern. Sistem terdiri dari tiga submetode: detektor fruit dan batang pohon (*trunk*) berbasis YOLOv4-tiny, pelacakan buah dengan pencocokan timbal balik (*mutual match*) dan pencocokan sekunder (*secondary match*), serta pencacahan dengan penetapan ID unik. Tujuannya adalah mengurangi kesalahan pencocokan pada buah bergerombol (*clustered fruit*) yang membuat satu buah dihitung lebih dari sekali.

Data diambil di kebun apel berkanopi pendek dan padat di Famen, Baoji, Shaanxi, Tiongkok, dengan kamera Intel RealSense D435 pada kendaraan kendali jarak jauh. Detektor mencapai mAP 96,4% dengan kecepatan 16 ms per citra. Pada sepuluh video uji 30 fps, rerata *ID Switch Rate* 3,9%, *Multiple Object Tracking Accuracy* 89,9%, dan *Multiple Object Tracking Precision* 93,5%. Terhadap hitungan manual per video, RMSE adalah 16,3 buah per video dan $R^2$ 0,93; metode pembanding DeepSORT mencapai RMSE 1.242,5 buah per video dan $R^2$ 0,73 karena menghitung berlebih. Sistem berjalan di CPU pada 3 sampai 5 frame per detik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah merupakan bagian dasar estimasi hasil panen. Pada video baris pohon, kunci pencacahan adalah pelacakan buah antarbingkai agar buah yang sama tidak dihitung ganda. Penulis mengutip tiga sumber penghitungan ganda dari Liu dkk. (2019): buah yang sama pada citra berurutan, buah yang sama dari dua sisi pohon, dan buah yang terlacak, hilang, lalu terdeteksi kembali.

Algoritma pelacakan untuk pejalan kaki atau mobil dinilai kurang cocok karena buah tampak serupa satu sama lain. Metode berbasis filter korelasi pada batang pohon hanya berlaku untuk kebun dengan dinding buah vertikal (*vertical fruiting-wall*), sedangkan kebun apel di Tiongkok umumnya padat dengan kanopi pendek dan batang tidak lurus. Penulis juga menyebut bahwa hasil sebelumnya pada kebun serupa mencapai akurasi pencacahan 81,9% karena salah pencocokan pada buah bergerombol.

## Ide Utama
Gerakan video diperkirakan dari perpindahan batang pohon yang terdeteksi pada bingkai berurutan, karena batang diam relatif terhadap buah. Perpindahan ini dipakai untuk memprediksi posisi buah pada bingkai berikutnya. Pencocokan dilakukan dua arah (prediksi ke deteksi dan deteksi ke prediksi) dengan strategi persaingan agar buah bergerombol tidak salah cocok. Pencocokan abnormal dibuang, lalu buah yang belum cocok dicocokkan lagi memakai perpindahan rerata buah yang cocok normal dan kriteria *Intersection over Union* (IoU).

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Kebun berjarak antartanaman 1,5 m dan antarbaris 4,0 m. Kamera dipasang pada menara kendaraan sekitar 1,4 m di atas tanah dan berjarak 2,0 m dari baris pohon. Total 1.000 citra asli dan 20 video asli beresolusi 720 × 1280 piksel diambil pada berbagai pencahayaan (depan dan belakang) antara 30 September 2020 dan 25 Oktober 2021, pukul 08.00 sampai 18.00, pada tahap buah matang. Video diambil pada 30 fps dengan kecepatan kendaraan sekitar 0,5 sampai 1,0 m/s sehingga objek bergeser sekitar 10 sampai 20 piksel antarbingkai. Laju bingkai 20 dan 15 fps ditiru dengan membuang bingkai. Seluruh buah diperlakukan sebagai buah matang karena buah belum matang tidak dapat dibedakan dari data RGB saja.

Dua puluh video dibagi sama banyak menjadi video eksperimen (10) dan video deteksi (10). Sepuluh video eksperimen (Vid_1 sampai Vid_10) berisi 135 sampai 295 bingkai dengan panjang baris 6,0 sampai 10,0 m. Sebanyak 600 citra diekstrak dari video deteksi dan digabung dengan 1.000 citra asli menjadi dataset deteksi. Citra diberi label kotak di LabelImg (sekitar 400 jam); buah di tanah dan di baris belakang tidak diberi label. Dataset berlabel memuat 93.050 instans buah dan batang. Augmentasi (kecerahan, kontras, *Gaussian blur*, ketajaman, *motion blur*, pencerminan horizontal) menambah citra latih dari 1.280 menjadi 11.520.

### 2. Detektor
YOLOv4-tiny dilatih dengan transfer learning dari COCO di kerangka Darknet: laju belajar 0,001, *weight decay* 0,0005, batch 64, maksimum 50.000 batch, SGD dengan momentum 0,9, ukuran potong latih 416 × 416. Pelatihan memakai GPU NVIDIA GTX 1080 8 GB. Pengujian sistem memakai laptop dengan GPU GeForce MX250 2 GB.

### 3. Perpindahan acuan dari batang pohon
Batang dengan jarak Euclid minimum pada bingkai berurutan dianggap batang yang sama, dan perpindahannya menjadi perpindahan acuan untuk memprediksi posisi buah. Batang yang dilacak berganti ke batang lain ketika mencapai batas kiri bidang pandang. Bila tidak ada batang terdeteksi, rerata perpindahan acuan lima bingkai sebelumnya dipakai.

### 4. Pencocokan timbal balik
Buah prediksi (posisi bingkai sebelumnya ditambah perpindahan acuan) dicocokkan ke buah terdeteksi, dan sebaliknya, berdasarkan jarak Euclid minimum antarpusat kotak. Tiga relasi (Match_p2d_1, Match_p2d_2, Match_d2p) bersaing menurut jumlah relasi yang dimiliki sehingga relasi Match_d2p memperoleh prioritas ketika satu buah terdeteksi memiliki relasi ke beberapa buah prediksi.

### 5. Penghapusan pencocokan abnormal
Buah dengan pencocokan yang bergeser lebih dari 30 piksel ke arah mana pun antarbingkai dinilai abnormal dan dibuang. Ambang itu dipilih karena lebar dan tinggi buah sekitar 30 sampai 40 piksel. Penulis mengasumsikan koordinat vertikal relatif konstan karena kecepatan rendah dan tanah rata.

### 6. Pencocokan sekunder
Buah belum cocok dan buah dengan pencocokan abnormal diprediksi ulang memakai rerata perpindahan buah yang cocok normal sebagai perpindahan acuan baru, lalu dicocokkan bila IoU lebih dari 0,4. Pelacakan dihentikan bila buah tidak terdeteksi lebih dari lima bingkai berturut-turut.

### 7. Pencacahan dengan penetapan ID
Setiap buah baru diberi ID bertambah satu, searah dengan gerak kamera (berlawanan arah gerak buah). Hasil hitungan adalah ID maksimum pada bingkai terakhir video.

## Eksperimen dan Hasil
Detektor diuji pada 320 citra pada ambang keyakinan 0,25 dengan 17.724 target buah dan 451 batang. Pencacahan dievaluasi pada 10 video eksperimen terhadap hitungan acuan manual dari tiga operator yang menandai buah dengan DarkLabel (hanya buah yang terlihat dari satu sisi antar baris; acuan valid bila variansi antaroperator kurang dari 1% dari hitungan acuan). Nilai acuan per video (rerata ± variansi): Vid_1 239 ± 2, Vid_2 269 ± 2, Vid_3 205 ± 1, Vid_4 263 ± 1, Vid_5 267 ± 2, Vid_6 304 ± 1, Vid_7 375 ± 2, Vid_8 283 ± 1, Vid_9 213 ± 1, Vid_10 187 ± 1 (keterangan Gambar 13).

Deteksi (Tabel 2):

| Objek | TP | FP | FN | P (%) | R (%) | AP (%) | mAP (%) | Kecepatan |
|---|---|---|---|---|---|---|---|---|
| Fruit | 16.723 | 2.684 | 1.001 | 86,5 | 94,5 | 94,2 | 96,4 | 16 ms/citra |
| Trunk | 445 | 4 | 6 | 98,6 | tidak terbaca pada tabel teks | 98,6 | - | - |

Pelacakan dan pencacahan, rerata sepuluh video (Bagian 3.2):

| Laju bingkai | $W_{ID}$ (%) | $P_{tr}$ (%) | $P_{mt}$ (%) | RMSE (buah/video) | $R^2$ | $P_c$ rerata (%) |
|---|---|---|---|---|---|---|
| 30 fps, metode usulan | 3,9 | 89,9 | 93,5 | 16,3 | 0,93 | 94,0 |
| 30 fps, DeepSORT | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan | 1.242,5 | 0,73 | tidak dilaporkan |
| 20 fps, metode usulan | 5,9 | 82,0 | 87,1 | 29,9 | 0,95 | 89,4 |
| 20 fps, DeepSORT | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan | 1.577,9 | 0,72 | tidak dilaporkan |
| 15 fps, metode usulan | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan | 42,4 | 0,94 | 84,4 |

Hitungan DeepSORT sekitar 3 sampai 7 kali hitungan acuan. Penulis mengaitkannya dengan buah yang mirip satu sama lain dan gerak kendaraan yang tidak teratur di tanah berlumpur. Kecepatan CPU: metode usulan 3 sampai 5 fps, DeepSORT 1 sampai 2 fps. Variasi ukuran kotak antarbingkai ($D_{dev}$) kecil: dari 7.658 nilai pada 200 buah, 5.209 (lebih dari 68,0%) bernilai 1 piksel atau kurang, dan nilai maksimum 5 piksel hanya muncul 6 kali. Pada Vid_1 bingkai 26 sampai 28, penghapusan pencocokan abnormal mengubah 40 lintasan menjadi 46 lintasan.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: ID buah relatif stabil termasuk pada buah bergerombol; pelacakan tetap berlanjut walaupun buah tidak terdeteksi pada satu bingkai (contoh buah No. 158 pada bingkai 95); kinerja tetap memadai ketika laju bingkai diturunkan dari 30 ke 20 fps; dan kecepatan CPU memungkinkan pemrosesan mendekati waktu nyata.

Keterbatasan yang dinyatakan penulis: presisi detektor rendah (86,5%) akibat buah di tanah dan di baris belakang yang terdeteksi; hanya buah matang yang dicacah; asumsi bahwa koordinat vertikal relatif konstan hanya berlaku pada kecepatan rendah dan tanah rata, sehingga kecepatan lebih tinggi, tanah tidak rata, atau kendaraan berbelok dapat menyulitkan; dan kemampuan generalisasi perlu diverifikasi pada dataset yang lebih beragam. Penulis berencana beralih ke segmentasi instans dan rekonstruksi 3D.

Menurut pembacaan ringkasan ini, evaluasi hanya memakai satu kebun, satu kultivar yang tidak disebut pada teks, dan sepuluh video, sehingga ketahanan statistik terbatas. Acuan hanya mencakup buah yang terlihat dari satu sisi baris, sehingga masalah penghitungan ganda dari dua sisi pohon tidak diuji. Perbandingan hanya dengan DeepSORT, dan metode pembanding tersebut tidak dijelaskan hasil pelacakannya.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan pelacakan: perpindahan antarbingkai diperkirakan dari batang pohon, buah dicocokkan dua arah dengan jarak Euclid dan IoU, dan ID unik ditetapkan sehingga hitungan akhir adalah ID maksimum. Penulis menyebut masalah penghitungan ganda dari dua sisi pohon, tetapi tidak menanganinya; video hanya dari satu sisi baris. Hitungan dilaporkan untuk satu kelas buah (semua dianggap matang), tidak per kelas. Acuan hitungnya adalah anotasi manual pada video oleh tiga operator, bukan panen atau hitung lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memakai objek diam (batang) sebagai acuan gerak kamera, pencocokan dua arah untuk objek serupa yang berdekatan, dan penghapusan pencocokan yang menyimpang. Namun metode ini mengandalkan lintasan horizontal sejajar pada baris tanaman berbentuk dinding dan tidak memberikan mekanisme identitas lintas sisi pohon, sehingga tidak langsung berlaku bagi pandang melingkari pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wu2023twice`.

Wu dkk. (2023) mengusulkan *twice matched fruit counting system* untuk pencacahan apel dari video baris pohon: YOLOv4-tiny mendeteksi buah dan batang, perpindahan batang dipakai memprediksi posisi buah, dan pencocokan timbal balik serta pencocokan sekunder menetapkan ID unik. Pada sepuluh video 30 fps, sistem mencapai RMSE 16,3 buah per video dan $R^2$ 0,93 terhadap hitungan manual, sedangkan DeepSORT mencapai RMSE 1.242,5 buah per video akibat penghitungan berlebih.

Catatan verifikasi data: mAP, TP/FP/FN, presisi, dan kecepatan deteksi berasal dari Tabel 2 dan Bagian 3.1; $W_{ID}$, $P_{tr}$, $P_{mt}$, RMSE, $R^2$, dan $P_c$ dari Bagian 3.2; hitungan acuan per video dari keterangan Gambar 13; parameter pelatihan dari Tabel 1. Nilai recall trunk tidak terbaca pada teks tabel hasil ekstraksi (hanya 98,6 yang muncul dan dapat berupa presisi maupun AP), sehingga tidak ditulis. Nilai per video pada Gambar 10 tidak tersedia dalam teks. Kultivar apel dan jumlah total buah acuan tidak dilaporkan di teks. Teks ekstraksi PDF terbaca dengan baik.
