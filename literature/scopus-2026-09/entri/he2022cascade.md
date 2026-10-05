# Cascade-SORT: A robust fruit counting approach using multiple features cascade matching

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `he2022cascade` |
| Judul asli | Cascade-SORT: A robust fruit counting approach using multiple features cascade matching |
| Penulis | He, Leiying; Wu, Fangdong; Du, Xiaoqiang; Zhang, Guofeng |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [he2022cascade.pdf](../pdf/he2022cascade.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107223

## Gambaran Umum
Makalah ini mengusulkan Cascade-SORT, sebuah metode pencacahan buah dari video yang memperlakukan pencacahan sebagai masalah pelacakan multi-objek (*multi-object tracking*, MOT) dengan kerangka *tracking-by-detection* (TBD). Detektor yang dipakai adalah YOLO-v3. Asosiasi data antarbingkai dilakukan melalui pencocokan bertingkat (*cascade matching*) yang memadukan jarak Mahalanobis (gerak), kemiripan tampilan berbasis *vector of locally aggregated descriptors* (VLAD) dari fitur SIFT, dan *intersection over union* (IoU), disertai filter Kalman yang dioptimalkan untuk memprediksi lintasan objek yang tidak terdeteksi.

Metode diuji pada buah kamelia (*camellia*) sebagai objek utama dan pada apel sebagai uji keumuman. Pada satu video kamelia, prediksi jumlah adalah 44 dengan acuan 38 (hitung manual dari seluruh video). Pada tiga video apel, total prediksi 310 dengan acuan 292. Dibandingkan dengan SORT, Cascade-SORT memberi akurasi pelacakan lebih tinggi, jumlah pertukaran identitas (*ID switch*) lebih rendah, dan lebih tahan terhadap penurunan mutu detektor.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah dari aliran video rentan terhadap oklusi dan mutu deteksi, terutama pada buah yang tumbuh rapat dan berwarna mendekati latar. Banyak metode TBD mengasosiasikan kotak pembatas antarbingkai dengan jarak IoU, informasi kedalaman, atau aliran optik. Penulis menyatakan bahwa pendekatan itu menghasilkan banyak pertukaran identitas karena buah mudah tertutup dan deteksi tidak stabil akibat perubahan cahaya, sehingga buah yang sama dihitung lebih dari sekali. Aliran optik juga sensitif terhadap perubahan cahaya luar ruangan dan tidak tahan oklusi.

Deep-SORT memakai jaringan saraf konvolusi untuk identifikasi ulang (*re-identification*), tetapi memerlukan kumpulan data identifikasi ulang berskala besar yang jarang tersedia untuk buah. Metode JDE memerlukan data video beranotasi yang mahal. Penulis menyatakan bahwa metode yang hanya memakai satu fitur tidak tangguh.

## Ide Utama
Penulis menyatakan tiga kontribusi: (1) algoritma pencarian citra tanpa CNN (VLAD) untuk mengukur kemiripan tampilan sehingga tidak memerlukan kumpulan data identifikasi ulang berskala besar; (2) pencocokan bertingkat yang memadukan fitur gerak dan tampilan untuk asosiasi data antarbingkai; (3) kode terbuka sebagai baseline. Penulis juga memakai metrik MOT, yaitu MOTA dan ID switch, untuk menilai pencacahan, karena galat deteksi terlewat dan pertukaran identitas dapat saling meniadakan pada hitungan akhir.

## Cara Kerja Langkah demi Langkah

### 1. Data
Citra kamelia berjumlah 2.312 (1080 × 1920) diambil dengan kamera genggam pada hari berawan pukul 08.00–17.00 di kebun kamelia di Kota Jinhua, Provinsi Zhejiang, Tiongkok. Diameter buah matang sekitar 3 cm. Pembagian data deteksi: 2.082 latih, 23 validasi, 207 uji, dengan 27.693 objek buah pada data latih. Video uji berkecepatan 30 bingkai/detik direkam dengan perangkat yang sama dari jarak sekitar 1,5 m dan kecepatan gerak kamera sekitar 1 m/s. Video kamelia uji berisi 450 bingkai.

Untuk apel, dikumpulkan 4.194 citra dengan 64.019 objek di Kota Weihai, Provinsi Shandong, dengan pembagian 3.775 latih, 42 validasi, dan 370 uji. Tiga video berisi masing-masing tiga pohon apel dengan panjang 162, 181, dan 93 bingkai.

### 2. Deteksi
YOLO-v3 dengan tulang punggung Darknet-53 dilatih pada masukan 608 × 608, bobot awal ImageNet, laju belajar awal 0,001, ukuran *batch* 2, 4.000 iterasi, dan peluruhan laju belajar pada iterasi 3.200 dan 3.600. Model pada iterasi 3.100 dipakai sebagai detektor uji.

### 3. Pelacakan dan filter Kalman
Keadaan tiap objek berdimensi delapan: posisi kiri-atas, rasio aspek, tinggi, dan kecepatannya. Lintasan berstatus sementara (*tentative*, kurang dari tiga bingkai) dicocokkan dengan IoU berambang 0,3. Lintasan dikonfirmasi setelah cocok pada tiga bingkai berturut-turut, dan dihapus bila umurnya melebihi masa hidup maksimum. Untuk lintasan yang hilang, kecepatan prediksi Kalman dikoreksi dengan kecepatan lintasan terdekat yang cocok (tetangga terdekat), dengan bobot yang berubah menurut lama hilangnya, karena buah bersifat statis dan gerak tampak berasal dari gerak kamera.

### 4. Kemiripan tampilan dengan VLAD
Deskriptor SIFT (128 dimensi) dari dua citra objek dikelompokkan dengan k-means menjadi k = 10 kata visual, selisih deskriptor terhadap pusat terdekat diakumulasi, dinormalisasi L2, dan kemiripan dihitung dengan jarak kosinus.

### 5. Pencocokan bertingkat
Gerbang Mahalanobis (batas selang kepercayaan 95% dari distribusi χ²) menyaring kandidat awal; kemudian skor kemiripan VLAD dengan ambang $t_2 = 0{,}8$ dikalikan gerbang tersebut, dan deteksi bernilai terbesar dipilih untuk tiap lintasan. Lintasan yang belum cocok dicocokkan dengan IoU. Penugasan tetangga terdekat dipakai; algoritma Hungarian disebut tidak memberi perbedaan pada pengujian.

## Eksperimen dan Hasil
Acuan hitung berupa hitung manual oleh manusia dari seluruh aliran video. MOTA dan ID switch dinilai oleh manusia bingkai demi bingkai. Detektor YOLO-v3 mencapai AP 78,40%, recall 88,70%, dan IoU 68,14% pada data uji kamelia (Tabel 1). Regresi linear antara jumlah acuan dan estimasi (sampel tiap 50 bingkai) menghasilkan $y = 1{,}14x$ dengan $R^2 = 0{,}965$.

| Uji | Metode | MOTA | Terlewat (m) | Positif palsu (fp) | ID switch | Prediksi | Acuan |
|---|---|---|---|---|---|---|---|
| Kamelia, 1 video (Tabel 2) | SORT | 0,55 | 2 | 0 | 15 | 51 | 38 |
| Kamelia, 1 video (Tabel 2) | Cascade-SORT | 0,73 | 2 | 0 | 8 | 44 | 38 |
| Apel, total 3 video (Tabel 6) | SORT | 0,59 | 29 | 0 | 90 | 354 | 292 |
| Apel, total 3 video (Tabel 6) | Cascade-SORT | 0,68 | 29 | 0 | 65 | 310 | 292 |

Pada tiga video apel, prediksi Cascade-SORT adalah 72 (acuan 71), 127 (acuan 112), dan 111 (acuan 109) untuk video 1, 2, dan 3. Pada tingkat pohon, regresi linear untuk Cascade-SORT adalah $y = 1{,}09x$ dengan $R^2 = 0{,}636$; deviasi minimum dan maksimum per pohon adalah $-8$ dan 11, sedangkan total deviasi sembilan pohon hanya 18. Penulis menyimpulkan bahwa metode lebih akurat untuk hasil kebun daripada untuk jumlah per pohon.

Uji ketahanan: detektor lemah (AP 66,15%, recall 77,65%, IoU 60,13%) menurunkan MOTA Cascade-SORT dari 0,74 menjadi 0,34 pada gerak kamera halus (Tabel 4), sedangkan pada SORT dari 0,55 menjadi 0,28. Pada gerak kamera tidak stabil dan cepat (Tabel 5), kedua pelacak menghasilkan lebih banyak pertukaran identitas dan MOTA negatif (Cascade-SORT dengan detektor kuat $-0{,}07$; SORT $-0{,}42$). Deep-SORT dengan identifikasi ulang yang dilatih pada data pejalan kaki dilaporkan lebih buruk daripada SORT, tanpa tabel angkanya.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tidak memerlukan kumpulan data identifikasi ulang untuk melatih fitur tampilan; ID switch berkurang dan MOTA naik dibanding SORT; lebih tahan terhadap penurunan detektor; kode dinyatakan akan dibuka.

Keterbatasan yang dinyatakan penulis: kinerja bergantung pada detektor; VLAD tidak selalu akurat (kemiripan buah yang sama dan berbeda berubah searah terhadap nilai k, Gambar 10) dan hanya mengurangi pertukaran identitas akibat oklusi pendek sekitar 5 bingkai; VLAD memakan waktu sekitar 50 ms; pelacakan peka terhadap gerak kamera yang tidak stabil karena IoU dan filter Kalman linear; hitungan per pohon sulit akurat; buah bergerombol memicu pertukaran identitas yang dapat menambah hitungan.

Menurut pembacaan ringkasan ini, evaluasi kamelia memakai satu video berisi 38 buah, sehingga bukti statistiknya terbatas, dan evaluasi apel memakai tiga video. Tidak ada ablasi terpisah untuk komponen VLAD dan filter Kalman yang dioptimalkan pada teks yang tersedia. Tidak ada pelaporan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai berturut-turut melalui pelacakan video: identitas dipertahankan dengan filter Kalman, gerbang Mahalanobis, kemiripan tampilan VLAD, dan IoU. Hitungan adalah jumlah lintasan unik terkonfirmasi. Hitungan tidak dilaporkan per kelas. Acuan hitung adalah hitung manual oleh manusia dari video (bukan panen). Pengujian dilakukan pada gerak kamera searah satu pandang yang berkesinambungan, bukan lintas sisi pohon yang terputus.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola asosiasi bertingkat (gerak sebagai gerbang, tampilan sebagai pencocokan, IoU sebagai cadangan) dan penggunaan metrik ID switch bersama jumlah, sebab galat saling meniadakan. Keterbatasannya: asumsi kemiripan tampilan dan gerak berkesinambungan kurang berlaku saat pandang berpindah antarsisi pohon, dan uji lintas sisi tidak dilakukan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `he2022cascade`.

He dkk. (2022) mengusulkan Cascade-SORT untuk pencacahan buah dari video. Metode ini memakai detektor YOLO-v3, filter Kalman yang dioptimalkan, dan pencocokan bertingkat yang menggabungkan jarak Mahalanobis, kemiripan VLAD berbasis SIFT, dan IoU. Pada satu video kamelia, jumlah prediksi 44 terhadap acuan 38 dengan ID switch 8 (SORT 15), dan pada tiga video apel jumlah prediksi 310 terhadap acuan 292 dengan MOTA 0,68 (SORT 0,59).

Catatan verifikasi data: angka kamelia berasal dari Tabel 1 dan 2 serta Gambar 7; angka apel dari Tabel 6; uji ketahanan dari Tabel 3–5. Teks menyebut pengurangan ID switch sebesar 46,77% dan peningkatan MOTA sebesar 0,18, sedangkan nilai pada Tabel 2 (15 menjadi 8; 0,55 menjadi 0,73) memberi selisih sederhana 46,67% dan 0,18; selisih kecil ini dicatat tanpa koreksi. MOTA Cascade-SORT pada Tabel 2 (0,73) berbeda dari Tabel 4 (0,74) untuk video yang sama. Tabel 6 pada teks ekstraksi terpotong untuk kolom acuan baris total (Cascade-SORT), sehingga acuan total 292 dibaca dari baris SORT. Gambar 9 dan 10 tidak dapat dibaca dari teks. Jumlah tiga video pada tabel (SORT 77, 153, 124 dan Cascade-SORT 72, 127, 111) dibaca dari kolom tabel ekstraksi.
