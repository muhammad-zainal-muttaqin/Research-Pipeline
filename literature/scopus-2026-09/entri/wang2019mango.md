# Mango fruit load estimation using a video based MangoYOLO—Kalman filter—hungarian algorithm method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2019mango` |
| Judul asli | Mango fruit load estimation using a video based MangoYOLO—Kalman filter—hungarian algorithm method |
| Penulis | Wang, Zhenglin; Walsh, Kerry; Koirala, Anand |
| Tahun | 2019 |
| Venue | Sensors Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [wang2019mango.pdf](../pdf/wang2019mango.pdf)
- DOI resmi: https://doi.org/10.3390/s19122742

## Gambaran Umum
Makalah ini mengusulkan metode penghitungan buah mangga pada pohon dari video yang direkam saat platform bergerak di sela baris kebun dengan kecepatan sekitar 5 km/jam. Metode menggabungkan detektor MangoYOLO (deteksi buah per bingkai), filter Kalman (prediksi posisi buah pada bingkai berikutnya, termasuk saat buah tertutup atau tidak terdeteksi), dan algoritma Hungarian (pencocokan buah antarbingkai) yang diperbaiki agar penugasan banyak-ke-satu (*multiple-to-one assignment*) ditangani. Ditambahkan konsep "meminjam" (*borrow*) kecepatan horizontal dan vertikal dari buah tetangga ketika model prediksi buah itu belum stabil.

Data berasal dari kebun mangga kultivar Calypso dan Honey Gold di Queensland, Australia, diambil pada malam hari dengan lampu LED 720 W dan kamera Basler 5 MP yang beroperasi pada 10 bingkai per detik. Pada satu video 110 bingkai berisi 192 buah (hitungan manusia), metode ini menghasilkan penghitungan ganda 9,9% dan hitungan hilang 7,3%, sehingga estimasi 2,6% lebih tinggi daripada hitungan manusia. Pada video baris 21 pohon dengan hitungan panen 3.286 buah, metode mencatat 2.050 buah (62% dari panen) dengan RMSE terkoreksi bias 18,0 buah per pohon, dibandingkan metode dua pandang (*dual-view*) yang mencatat 1.322 buah (40%) dengan RMSE terkoreksi bias 21,7 buah per pohon.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Prediksi hasil mangga idealnya dibuat enam minggu sebelum panen untuk memandu keputusan panen dan pemasaran. Produksi mangga bervariasi antarmusim dan antarpohon, sehingga estimasi yang sahih memerlukan penilaian banyak pohon dan hitungan manusia di lapangan tidak praktis. Pencitraan dua pandang (satu citra per sisi pohon, terpusat pada batang) hanya menangkap satu perspektif tiap sisi, sehingga sebagian buah tersembunyi. Penulis mencatat bahwa Koirala dkk. memakai faktor koreksi dari hitungan manusia pada sampel pohon, dengan nilai tertinggi 2,43 (pohon besar, daun lebat) dan terendah 1,05 (kanopi terbuka); estimasi akhir sensitif terhadap faktor koreksi ini.

Pencitraan dari kendaraan yang bergerak memberi banyak perspektif sehingga lebih banyak buah terlihat, tetapi memerlukan pelacakan agar tidak terhitung berulang. Mengutip Liu dkk., penulis menyebut tiga sumber penghitungan berlebih pada video: (1) buah yang sama pada bingkai berurutan; (2) buah yang terlacak lalu tidak terdeteksi karena oklusi dan kemudian terdeteksi kembali; (3) buah yang terlihat dari kedua sisi pohon. Penulis menambahkan kategori keempat: salah hitung buah baru yang muncul dekat posisi buah lama yang tidak terdeteksi pada bingkai saat ini sehingga keliru ditugaskan ke buah lama. Pendekatan 3D (LiDAR, GNSS presisi tinggi, SfM, epipolar) disebut mahal dan rentan akumulasi galat.

## Ide Utama
Penulis mengusulkan solusi berbiaya dan kerumitan rendah tanpa GNSS presisi atau LiDAR: lacak setiap buah dengan filter Kalman individual berstatus $(x, y, v_x, v_y)$, yang memprediksi posisi buah pada bingkai berikut meski sempat tidak terdeteksi. Rotasi kamera dan perubahan skala diperlakukan sebagai derau proses, dan buah di bagian citra berbeda dapat memiliki kecepatan berbeda. Algoritma Hungarian mencocokkan buah terlacak dengan deteksi baru berdasarkan jarak Euklides, dengan ambang jarak maksimum. Buah yang tidak terdeteksi tetap dipertahankan di daftar pelacakan sampai 15 bingkai berturut-turut.

## Cara Kerja Langkah demi Langkah

```
 [video 10 fps] -> [MangoYOLO: titik pusat kotak per buah]
      -> [Hungarian 1x (jarak <= 60 px) -> Hungarian ke-2 -> buang
          penugasan banyak-ke-satu yang berjarak lebih besar]
      -> [Kalman: perbarui bila cocok; prediksi bila tidak, "pinjam" kecepatan]
      -> [tidak terlihat > 15 bingkai: hapus; deteksi tak cocok: buah baru]
```

### 1. Akuisisi data
Kebun mangga kultivar Calypso dan Honey Gold (kebun GE1 dan HG B dalam studi sebelumnya) dicitrakan dengan platform pada kendaraan pertanian: lampu LED 720 W, kamera Basler acA2440-75um (5 MP, 2448 × 2048, dioperasikan pada 10 fps), lensa 5 mm, F/1,8, eksposur 2,5 ms, jarak kamera ke kanopi sekitar 2 m. Pencitraan dilakukan setelah matahari terbenam dengan kecepatan sekitar 5 km/jam sehingga ada sekitar 30 bingkai per pohon dan pergeseran sekitar 20 piksel per bingkai. Setiap pohon dilokasikan dalam 2 cm dengan Leica GS-14 (jaringan CORS) sekali saja, dan kamera dipicu berdasarkan posisi GNSS pohon pada metode dua pandang. Medan relatif datar sehingga kecepatan vertikal diasumsikan nol. Citra diubah menjadi 1024 × 1024 untuk MangoYOLO.

### 2. Deteksi MangoYOLO
Arsitektur dan bobot diambil dari Koirala dkk. (F1 0,968 dan AP 0,983 pada kerja asal). Ambang keyakinan 0,24 dan ambang NMS 0,45. Titik pusat kotak pembatas dipakai sebagai lokasi buah. Kotak dengan lebar kurang dari 12 piksel atau tinggi kurang dari 15 piksel dibuang untuk mengurangi buah dari sisi jauh kanopi yang akan terhitung dari sisi lain baris. Kecepatan pemrosesan 3,7 detik per bingkai pada laptop dengan GTX 1060 (407 detik untuk 110 bingkai).

### 3. Filter Kalman
Keadaan $(x, y, v_x, v_y)$ dengan interval waktu $dt=1$ bingkai. Kovarians derau proses 1,0 dan derau pengukuran 0,1 (empiris). Filter memerlukan sekurangnya empat pembaruan berturut-turut untuk model prediksi yang akurat. Untuk buah yang muncul kurang dari empat kali, kecepatan dipinjam dari buah tetangga yang modelnya stabil; bila tidak ada, dipakai kecepatan global $(v_x=20, v_y=0)$ piksel per bingkai (berdasarkan 5 km/jam pada medan datar). Buah yang muncul kembali pada posisi prediksi dalam 15 bingkai sejak terakhir terdeteksi dianggap buah yang sama.

### 4. Algoritma Hungarian yang diperbaiki
Matriks biaya berisi jarak Euklides pusat buah antarbingkai. Perbaikan: (i) Hungarian menghasilkan penugasan satu-ke-satu; (ii) ambang jarak maksimum membatalkan penugasan berjarak besar; (iii) Hungarian dijalankan kedua kali pada buah terlacak dan buah baru yang belum ditugaskan; (iv) bila dua buah terlacak ditugaskan ke satu buah baru, hanya penugasan berjarak lebih kecil yang dipertahankan. Buah yang tidak cocok dan belum melewati batas 15 bingkai memakai posisi prediksi Kalman dan penghitung "tidak terlihat" bertambah satu; deteksi yang tidak cocok menjadi buah baru dengan filter Kalman baru. Penulis mengakui kasus buah baru yang muncul sangat dekat (kurang dari 60 piksel) dengan buah lama yang tidak terdeteksi masih menyebabkan hitungan hilang, tetapi jarang.

### 5. Hitungan acuan
Citra dan video dihitung manusia; jumlah buah pada pohon juga dihitung setelah panen. Untuk video, hasil pelacakan diperiksa bingkai demi bingkai, dan selisih hitungan antara pohon target dan pohon tetangga dicatat sebagai hitungan pohon target. Galat asosiasi buah ke pohon memengaruhi hitungan per pohon tetapi tidak total baris.

## Eksperimen dan Hasil
Kinerja MangoYOLO. Pada citra Calypso musim 2018 (model dilatih dari citra 2017), R² = 0,988, RMSE = 5,0, dan bias = −4,0 buah per citra. Pada video Honey Gold 110 bingkai, R² = 0,665, RMSE = 2,1, dan bias = 0,0 buah per citra; rerata 31 buah terdeteksi per bingkai dengan 1,4 *false positive* dan 1,4 *false negative*. R² yang lebih rendah pada video dikaitkan penulis dengan variasi jumlah buah antarbingkai yang lebih sempit.

Pemilihan parameter. Pada jumlah bingkai tak teramati maksimum 0 (tanpa Kalman) hitungan 357 dibandingkan hitungan manusia 192; pada 15 bingkai hitungan 191, dekat 192, sehingga 15 dipilih. Ambang jarak Hungarian diuji 20 sampai 100 piksel (langkah 5): pada 20 piksel hitungan 956, dan dekat hitungan manusia pada 60 piksel.

Atribusi galat pada 110 bingkai (Tabel 1):

| Komponen | Buah | Persen |
|---|---|---|
| Hitungan manusia | 192 | 100% |
| (i) Ulang akibat oklusi pada bingkai sebelumnya | 3 | 1,5% |
| (ii) Ulang akibat FN pada bingkai sebelumnya | 1 | 0,5% |
| (iii) Prediksi posisi keliru | 15 | 7,8% |
| Total hitungan ulang | 19 | 9,9% |
| (iv) Hitungan hilang (buah baru ditugaskan ke posisi lama) | −14 | −7,3% |
| Hitungan estimasi | 197 | 102,6% |

Teks bagian 3.3 menyebut hitungan ulang 9,7% dan hitungan hilang 7,1% dengan selisih 2,6%, berbeda sedikit dari Tabel 1 dan abstrak (9,9% dan 7,3%).

Hitungan satu baris 21 pohon (Tabel 2):

| Ukuran | Panen | Dua pandang | Pelacakan (video) |
|---|---|---|---|
| Total (buah per 21 pohon) | 3.286 | 1.322 | 2.050 |
| Rerata (buah per pohon) | 156,5 | 63,0 | 97,6 |
| Bias (buah per pohon) | tidak ada | −93,5 | −58,9 |
| % hitungan mesin per panen | tidak ada | 40,2% | 62,3% |
| RMSE terkoreksi bias | tidak ada | 21,7 | 18,0 |
| Faktor koreksi | tidak ada | 2,5 | 1,6 |

Video untuk uji ini berisi 1.162 bingkai (42 bingkai berpusat pada batang pohon untuk metode dua pandang menurut abstrak). Penulis menyebut kebun uji sebagai kasus sulit dengan proporsi buah tersembunyi tinggi karena kanopi tebal berbentuk pagar. Mereka menyimpulkan bahwa metode video lebih baik daripada metode dua pandang untuk hitungan buah kebun mangga.

## Kelebihan dan Keterbatasan
Kelebihan: biaya dan kerumitan perangkat keras rendah (rig LED, kamera, dan komputer disebut kurang dari US$ 4.000, sedangkan LiDAR dan GNSS diferensial dapat menambah lebih dari US$ 30.000); tidak memerlukan GNSS diferensial bila yang diperlukan estimasi tingkat kebun; lebih banyak sudut pandang per pohon daripada metode dua pandang; dan faktor koreksi turun dari 2,5 menjadi 1,6.

Keterbatasan yang dinyatakan penulis: setiap sistem lewat-jalan (*drive-by*) tidak melihat sebagian buah di pohon; buah yang keluar dari pandangan lebih dari 15 bingkai, atau yang prediksi posisinya meleset, terhitung ganda (contoh buah 86 dan 99 pada Gambar 6); kasus buah baru yang muncul sangat dekat dengan buah lama yang tidak terdeteksi menyebabkan hitungan hilang; metode tidak menyediakan lokalisasi dalam kebun maupun segmentasi pohon (dapat dilengkapi GNSS atau penanda baris); penghitungan ganda dari dua sisi kanopi menjadi masalah lebih besar pada kanopi sempit, sehingga evaluasi pada arsitektur kanopi yang lebih sempit dinyatakan sebagai pekerjaan mendatang, bersama faktor koreksi per pohon atau per citra.

Menurut pembacaan ringkasan ini: (a) evaluasi bingkai demi bingkai hanya pada satu video 110 bingkai dan satu kultivar (Honey Gold), dan uji baris hanya pada satu baris 21 pohon, sehingga tidak ada ulangan; (b) metode tetap menghitung hanya 62% dari buah panen, dan hasilnya tidak menggantikan faktor koreksi tetapi hanya menurunkannya; (c) ambang 15 bingkai dan 60 piksel dipilih pada data yang sama dengan yang dipakai untuk evaluasi (satu video), dan nilainya bergantung pada kecepatan platform sekitar 5 km/jam dan 10 fps; (d) hitungan dilaporkan sebagai total, tanpa pemisahan kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dari sisi baris yang dilalui kendaraan, dengan mekanisme pelacakan: filter Kalman individual per buah, pencocokan Hungarian yang diperbaiki (dua putaran dan penyelesaian penugasan banyak-ke-satu), penyimpanan buah tak teramati sampai 15 bingkai, serta peminjaman kecepatan dari buah tetangga. Makalah ini mengidentifikasi empat kategori penghitungan ganda atau hilang pada video, termasuk buah yang terlihat dari kedua sisi pohon; kategori terakhir hanya dikurangi dengan ambang ukuran kotak (lebar kurang dari 12 piksel atau tinggi kurang dari 15 piksel) dan bukan dengan pencocokan identitas lintas sisi, dan penulis mengakuinya sebagai pekerjaan mendatang. Hitungan dilaporkan sebagai total tanpa kelas. Acuan hitungnya mencakup hitungan manusia pada bingkai atau video (untuk galat bingkai) dan hitungan panen pada pohon (untuk hasil baris).

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: taksonomi sumber hitungan ganda dan hitungan hilang, mekanisme pemeliharaan jejak buah yang tidak terdeteksi sementara (prediksi Kalman dan batas bingkai), penyelesaian penugasan banyak-ke-satu, serta analisis sensitivitas terhadap ambang jarak dan batas bingkai. Hasil faktor koreksi 1,6 sampai 2,5 antara hitungan mesin dan panen memberi gambaran besarnya buah tersembunyi pada kanopi tebal, yang relevan bagi tandan sawit di balik pelepah. Metode ini tidak memberikan identitas lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wang2019mango`.

Wang, Walsh, dan Koirala (2019) mengusulkan penghitungan buah mangga dari video malam hari (10 fps, kecepatan 5 km/jam) dengan detektor MangoYOLO, filter Kalman dengan konsep peminjaman kecepatan dari buah tetangga, dan algoritma Hungarian yang diperbaiki untuk penugasan banyak-ke-satu. Pada video baris 21 pohon, metode mencatat 62% dari hitungan panen (RMSE terkoreksi bias 18,0 buah per pohon) dibandingkan 40% (21,7 buah per pohon) untuk metode dua pandang; pada satu video 110 bingkai, hitungan ulang 9,9% dan hitungan hilang 7,3% menghasilkan estimasi 102,6% dari hitungan manusia.

Catatan verifikasi data: Angka 192, 197, 9,9%, 7,3%, dan 102,6% bersumber dari Tabel 1 dan abstrak; teks bagian 3.3 menyebut 9,7% dan 7,1% yang sedikit berbeda dan tidak dikutip sebagai angka utama. Angka baris 21 pohon (3.286, 1.322, 2.050, 62,3%, 40,2%, 18,0, 21,7, faktor koreksi 1,6 dan 2,5) bersumber dari Tabel 2. Parameter 15 bingkai, 60 piksel, serta hitungan 357, 191, dan 956 berasal dari bagian 3.2 (Gambar 8 dan 9, nilai hitungan dari teks). Tabel 1 dan 2 terbaca utuh dari ekstraksi. R² dan RMSE MangoYOLO dari bagian 3.1. Hitungan hasil panen dan buah pada bingkai tidak tersedia secara terpisah per kelas atau per tingkat kematangan. Rincian jumlah citra pelatihan tidak dilaporkan (model diadopsi dari Koirala dkk.). Data dan citra disebut tersedia sebagai berkas pendukung artikel.
