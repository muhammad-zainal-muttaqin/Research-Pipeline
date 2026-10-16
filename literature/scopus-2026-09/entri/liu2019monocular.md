# Monocular Camera Based Fruit Counting and Mapping with Semantic Data Association

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2019monocular` |
| Judul asli | Monocular Camera Based Fruit Counting and Mapping with Semantic Data Association |
| Penulis | Liu, Xu; Chen, Steven W.; Liu, Chenhao; Shivakumar, Shreyas S.; Das, Jnaneshwar; Taylor, Camillo J.; Underwood, James; Kumar, Vijay |
| Tahun | 2019 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [liu2019monocular.pdf](../pdf/liu2019monocular.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2019.2901987

## Gambaran Umum
Makalah ini menyajikan jalur pencacahan dan pemetaan buah yang hanya memakai satu kamera monokular, dirancang murah, ringan, dan cepat. Jalur itu mendeteksi buah dan batang pohon dengan jaringan saraf konvolusional (*convolutional neural network*, CNN), melacak keduanya antarcitra dengan filter Kalman yang menggabungkan keluaran detektor dan aliran optik (*optical flow*), lalu memakai *structure from motion* (SfM) semantik berbasis "buah sebagai fitur" untuk mengubah lintasan 2D menjadi penanda 3D (*landmark*) yang dipakai mengenali penghitungan ganda.

Data berasal dari kebun mangga Simpson Farms di Bundaberg, Queensland, Australia, direkam pada 6 Desember 2017 oleh kendaraan darat tanpa awak milik Australian Centre for Field Robotics, dengan kamera Prosilica GT3300C (3296 × 2472 piksel, 5 Hz). Kebenaran lapangan adalah hitungan manual pada 18 pohon. Sistem dibandingkan dengan sistem pembanding berperangkat mahal (kamera, LiDAR, dan GPS/INS).

Hasil utama: galat rerata per pohon 27,8 (simpangan baku 29,6) untuk sistem monokular dibandingkan 19,8 (22,9) untuk sistem pembanding multipandang. Regresi linear terhadap hitungan lapangan menghasilkan kemiringan 0,86 dan $R^2$ 0,78 untuk sistem monokular, serta 0,97 dan 0,88 untuk sistem pembanding. Rerata sekitar 175 mangga per pohon.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sistem penghitung buah robotik umumnya memakai kamera stereo, sensor kedalaman, LiDAR, dan GPS/INS. Paket sensor semacam itu dapat mencapai sekitar $25.000 dan beratnya beberapa kilogram, serta memerlukan kalibrasi antarmodalitas. Motivasi penulis adalah penghitung buah untuk petani jambu mete di Mozambik, tempat infrastruktur dan pengetahuan teknis terbatas, sehingga perangkat kompleks tidak layak.

Menghitung dari urutan citra pada dua sisi baris pohon menghasilkan estimasi lebih lengkap karena sebagian besar buah hanya terlihat dari satu sudut, tetapi menimbulkan tiga masalah penghitungan ganda: (1) buah yang sama terdeteksi pada citra berurutan; (2) buah yang sama terlihat dari kedua sisi pohon; dan (3) buah yang dilacak, hilang, lalu terdeteksi dan dilacak ulang (*double tracking*).

## Ide Utama
Penulis menaikkan beban kinerja dari perangkat keras ke algoritma: hanya satu kamera yang dipakai, dan identitas buah ditentukan oleh penanda 3D hasil SfM yang memakai pusat buah (hasil pelacakan) sebagai fitur, bukan titik SIFT. Penanda 3D itu kemudian dipakai untuk tiga hal: menolak lintasan ganda dengan mengasosiasikan ulang penanda dengan deteksi 2D, menghapus penghitungan ganda dari dua sisi pohon dengan membandingkan kedalaman buah terhadap sentroid pohon (didekati batang), dan menghasilkan peta buah.

## Cara Kerja Langkah demi Langkah

```
 Dua urutan citra (sisi timur dan barat) -> Faster R-CNN (buah) + FCN (batang)
   -> pelacakan 2D (KLT + Kalman + Hungaria) -> SfM semantik (COLMAP)
   -> asosiasi ulang penanda dengan deteksi -> pemisahan sisi dengan sentroid pohon
   -> SfM akhir -> hitungan dan peta
```

### 1. Deteksi buah
Detektor memakai Faster R-CNN dengan jaringan usulan wilayah dan modul klasifikasi, diikuti ambang probabilitas dan *non-maximum suppression*. Anotasi mengikuti metode Bargoti dkk.: 1.500 potongan citra 500 × 500 diambil acak dari 15.000 citra kebun (masing-masing 3296 × 2472 piksel), tiap buah diberi kotak pembatas; hanya buah pada pohon baris pertama yang dianotasi, dan buah pada pohon kebenaran lapangan dikeluarkan dari data latih.

### 2. Pelacakan pada bidang citra
Aliran optik KLT (Kanade-Lucas-Tomasi) memprediksi posisi buah pada citra berikutnya. Penugasan antara deteksi pada dua citra berurutan diselesaikan dengan algoritma Hungaria dengan biaya yang menggabungkan jarak pusat ternormalisasi luas dan tumpang tindih kotak. Posisi akhir diperoleh dari filter Kalman dengan vektor keadaan 4 dimensi (posisi dan kecepatan piksel) dan vektor pengukuran 6 dimensi (prediksi KLT, pusat deteksi, dan pengukuran kecepatan tambahan dari arah aliran optik rerata). Matriks kovarians $Q$ = diag(6, 2, 3, 1) dan $R$ = diag(3, 1, 1, 0,5, 1, 0,5). Seluruh riwayat lintasan membentuk himpunan kecocokan fitur buah.

### 3. SfM semantik
Himpunan kecocokan fitur buah dimasukkan ke COLMAP untuk menentukan pasangan citra awal (verifikasi geometri epipolar dan RANSAC), memperkirakan pose kamera dengan *Perspective-n-Point*, mentriangulasi penanda, dan mengoptimasi dengan *bundle adjustment* (meminimalkan galat proyeksi ulang). Dibandingkan SfM berbasis SIFT, pendekatan ini melewati ekstraksi dan pencocokan deskriptor; pada video 1.000 bingkai dengan CPU i7 empat inti, rekonstruksi SfM sekitar 5 menit dibandingkan 10 jam untuk SfM berbasis SIFT (belum termasuk pelacakan 2D).

### 4. Penghapusan *double tracking*
Setiap penanda diproyeksikan kembali ke tiap citra dan dicocokkan dengan deteksi lewat penugasan Hungaria kedua. Biaya memuat komponen usia penanda (jumlah citra tempat penanda teramati; ambang usia $O_0$ = 7, bobot 0,5) sehingga penanda yang lebih tua diutamakan dan penanda baru untuk buah yang sama dibuang. Penanda tanpa deteksi pasangan dibuang.

### 5. Penghapusan penghitungan ganda dari dua sisi
Dataset merekam semua baris menghadap timur lalu menghadap barat, sehingga SfM menghasilkan dua awan titik terpisah per baris. Batang pohon disegmentasi dengan jaringan ekstraksi konteks berbasis FCN dengan CRF padat (hanya sepertiga tengah citra dipakai), sudut Shi-Tomasi pada batang dilacak dengan KLT selama 4 bingkai ($b$ = 3), lalu ditriangulasi. Kedalaman batang diwakili kuartil ketiga kedalaman titik sudut. Untuk tiap penanda buah, penulis memeriksa 15 bingkai ke belakang dan memberi suara "sebelum" atau "sesudah" sentroid; penanda dihitung bila suara "sebelum" lebih banyak. Hanya buah pada sisi pohon yang lebih dekat ke kamera yang dihitung.

### 6. Penyempurnaan akhir
Asosiasi akhir diperhalus dengan KLT berdasarkan tebakan awal posisi, lalu SfM akhir menghasilkan peta buah.

## Eksperimen dan Hasil
Pembanding adalah sistem dari Stein dkk. yang memakai Faster R-CNN yang sama, pose dari GPS/INS/RTK, dan awan titik LiDAR untuk sentroid pohon, dengan dua varian: *Suite Multi-view* (semua citra urutan) dan *Suite Dual-view* (hanya dua citra dari dua sisi berlawanan). Kebenaran lapangan: hitungan manual pada 18 pohon yang dipilih dari 10 baris untuk memaksimalkan variasi NDVI; pohon bervariasi dalam ukuran dan tingkat oklusi. Untuk perbandingan per pohon, pohon target ditopeng secara manual pada algoritma penulis.

Hasil (Gambar 9 dan 10):

| Ukuran | Mono Final | Suite Multi-view |
|---|---|---|
| Galat hitungan per pohon, rerata | 27,8 | 19,8 |
| Galat hitungan per pohon, simpangan baku | 29,6 | 22,9 |
| Kemiringan regresi | 0,86 | 0,97 |
| $R^2$ regresi | 0,78 | 0,88 |

Hitungan mentah dari pelacakan 2D dan dari penanda cenderung melebihkan hitungan; penanda menaikkan kedekatan dengan kebenaran lapangan pada sebagian besar kasus, dan hasil akhir setelah penghapusan penghitungan ganda dua sisi jauh lebih kuat dan akurat (Gambar 7 dan 8, kualitatif). Varian *Suite Dual-view* sangat menghitung terlalu sedikit karena hanya memakai dua citra per pohon, yang menurut penulis menunjukkan keunggulan penghitungan dari urutan citra. Kedua sistem utama cenderung menghitung sedikit di bawah hitungan lapangan, yang menurut penulis wajar karena hitungan lapangan mencakup buah yang tertutup sepenuhnya.

## Kelebihan dan Keterbatasan
Kelebihan: hanya memakai satu kamera monokular dan dapat berjalan pada perangkat murah; SfM berbasis buah jauh lebih cepat daripada berbasis SIFT; penanda 3D juga memperbaiki deteksi 2D dengan memperkirakan posisi buah yang sangat tertutup (Gambar 4); keluaran juga berupa peta buah.

Keterbatasan yang dinyatakan penulis: sistem monokular kalah dari sistem pembanding pada pohon dengan hitungan tinggi; penulis menduga penyebabnya adalah buah yang tertutup, karena pada sisi tertentu buah dapat berada di belakang sentroid batang tetapi tidak terlihat dari sisi lain, sehingga pembuangan berdasarkan sisi terlalu agresif dan menyebabkan penghitungan kurang. Integrasi dua awan titik yang lebih canggih diperlukan; bila dua sisi baris direkam berturutan, langkah penolakan berbasis sentroid tidak diperlukan. Diperlukan percobaan lanjutan untuk memahami kurva imbal balik antara kompleksitas perangkat keras dan perangkat lunak.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup satu kebun mangga dan satu hari pengambilan dengan 18 pohon, tanpa pengujian pada tanaman lain. Nilai $R^2$ dan kemiringan dihitung dari 18 titik. Topeng pohon target dibuat manual, sehingga sistem belum sepenuhnya otomatis pada tahap evaluasi. Hitungan tidak dilaporkan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali secara eksplisit dan terstruktur dalam tiga tingkat: pelacakan 2D antarbingkai (KLT, filter Kalman, algoritma Hungaria), penanda 3D hasil SfM yang diasosiasikan ulang dengan deteksi untuk menolak lintasan ganda, dan aturan sentroid-batang untuk memisahkan dua sisi baris pohon. Pemisahan sisi dilakukan dengan menghitung hanya buah pada sisi pohon yang lebih dekat ke kamera, yaitu aturan pemilihan sisi, bukan pencocokan buah yang sama antarsisi.

Hitungan hanya satu kelas (mangga), tidak per kelas. Acuan hitungnya adalah hitungan manual lapangan pada 18 pohon, yang mencakup buah yang tertutup penuh, dan hitungan dari sistem pembanding. Yang dapat dipindahkan ke tandan sawit multi-sisi: keluarga masalah tiga jenis penghitungan ganda sebagai kerangka analisis; aturan pemisahan sisi dengan sentroid batang (dengan catatan penulis bahwa aturan ini dapat membuang buah yang hanya terlihat dari satu sisi); penanda 3D sebagai identitas buah; dan penggunaan penanda untuk memulihkan deteksi yang tertutup. Keterbatasannya adalah ketergantungan pada urutan video berkelanjutan dan batang yang terlihat di tengah citra.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `liu2019monocular`.

Liu dkk. (2019) mengusulkan penghitung dan pemeta buah monokular yang menggabungkan detektor Faster R-CNN, pelacakan dengan aliran optik dan filter Kalman, serta SfM semantik berbasis buah yang menghasilkan penanda 3D untuk menolak penghitungan ganda, termasuk dari dua sisi baris pohon melalui sentroid batang. Pada 18 pohon mangga, galat hitungan rerata per pohon adalah 27,8 (simpangan baku 29,6) dibandingkan 19,8 (22,9) pada sistem pembanding berperangkat LiDAR dan GPS/INS, dengan kemiringan regresi 0,86 dan $R^2$ 0,78 terhadap hitungan lapangan.

Catatan verifikasi data: Galat rerata dan simpangan baku ada pada tabel di Gambar 10, kemiringan dan $R^2$ pada seksi V (teks bawah Gambar 9), serta rerata sekitar 175 mangga per pohon pada keterangan Gambar 8. Hitungan per pohon tidak tersedia dalam teks (hanya pada Gambar 7 dan 8), sehingga tidak dapat diverifikasi. Teks tidak melaporkan metrik deteksi Faster R-CNN dan merujuk pada makalah lain untuk rinciannya. Unit galat adalah jumlah buah per pohon, dan teks tidak menyatakan bahwa itu galat absolut; ini diasumsikan dari konteks "per-tree count error". Waktu SfM 5 menit versus 10 jam tercantum pada seksi V. Berkas teks adalah versi *preprint* yang diterima Januari 2019.
