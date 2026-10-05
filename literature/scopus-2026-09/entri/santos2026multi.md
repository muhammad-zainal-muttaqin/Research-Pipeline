## Gambaran Umum
Makalah ini (*Revista de Informática Teórica e Aplicada*, vol. 33, no. 2, 2026) memakai CoTracker, model berbasis *transformer* untuk pelacakan titik dengan perhatian silang antar-lintasan dan antar-waktu (*cross-track/cross-time attention*), untuk sekaligus melacak banyak buah, melokalisasi buah dalam 3D, dan memperkirakan pose kamera dari video kebun jeruk manis. Sistem menerima kotak pembatas dari detektor YOLOv5, memperlakukan buah sebagai penanda (*landmark*) untuk odometri visual, dan mengoptimalkan pose serta posisi buah dengan graf faktor (*factor graph*).

Evaluasi memakai subset tujuh dari 12 urutan dataset MOrangeT (jeruk manis: Pera, Valencia, Natal, Hamlin). Hasil gabungan: HOTA 47,457, prediksi 978 buah terhadap acuan 879 buah (109 positif palsu, 10 negatif palsu), galat pencacahan 11,26%. Galat per urutan berkisar dari 1,74% (V12) sampai 43,44% (V06). Penulis menyatakan metode ini tidak lebih baik daripada karya sebelumnya (HOTA 56,039 dan galat median pencacahan 6,95% pada dataset yang sama).

Penulis menyebut hasil sebagai bukti konsep (*proof of concept*) dengan potensi, bukan sebagai peningkatan terhadap pembanding sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Saat robot atau operator melintasi baris kebun, buah terekam dari banyak sudut, terhalang sementara oleh daun, dahan, atau buah lain, dan muncul kembali beberapa kali. Pencacahan tanpa hitungan ganda sulit karena kemiripan antarbuah yang tinggi dan ketiadaan ciri pembeda. Sebagian peneliti memodelkannya sebagai pelacakan multi-objek (*Multiple-Object Tracking*, MOT), sebagian lain memakai lokalisasi 3D untuk mengenali kembali buah yang muncul lagi, dengan *Structure from Motion* (SfM).

Penulis menyoroti bahwa MOT (SORT, ByteTrack) dan SfM (SIFT dengan FLANN) bergantung pada asosiasi antar-bingkai yang mengandaikan pengamatan saling bebas dan berfokus pada pasangan bingkai, sehingga pelacakan jangka panjang bergantung pada rantai pencocokan berpasangan yang benar. Penulis menyebut ini sebagai kurangnya integrasi spasial dan temporal.

## Ide Utama
CoTracker memproses sekelompok titik bersama-sama dalam jendela video pendek, sehingga informasi dari titik yang terlihat membantu melacak titik yang terhalang. Gagasan makalah ini adalah memakai pelacak itu sebagai satu mekanisme asosiasi data untuk MOT dan SfM sekaligus. Titik pusat kotak pembatas buah menjadi titik kueri. Lintasan titik membentuk lintasan kotak untuk tiap buah, dan lintasan itu menjadi dasar odometri visual dan triangulasi posisi 3D buah. Keluarannya adalah posisi 3D buah, pose kamera setiap bingkai, dan penanda keterlihatan buah pada tiap bingkai.

## Cara Kerja Langkah demi Langkah
### 1. Data dan deteksi
Data adalah subset MOrangeT, himpunan urutan citra pohon jeruk manis dengan anotasi format MOT16 (setiap jeruk yang terlihat memiliki identitas numerik dan kotak pembatas pada tiap bingkai). Dataset asli terdiri atas 12 urutan, masing-masing satu pohon; dipilih tujuh urutan yang cukup berisi buah untuk odometri visual. Rincian (urutan, gimbal, varietas, bingkai, jeruk terlihat): V01 (tanpa gimbal, Pera, 408, 110); V04 (tanpa, Valencia, 384, 105); V05 (tanpa, Natal, 293, 148); V06 (gimbal, Valencia, 447, 122); V08 (gimbal, Valencia, 544, 192); V11 (gimbal, Hamlin, 268, 87); V12 (gimbal, Hamlin, 307, 115). Kolom terakhir adalah jumlah buah yang terlihat, bukan populasi buah per pohon.

Kotak pembatas berasal dari YOLOv5 yang dilatih pada OranDet (3.065 citra dengan 9.769 buah beranotasi), dengan *non-maximum suppression* pada ambang IoU 0,2, dan kotak dengan skor keyakinan di bawah 0,7 dibuang. Alasannya, kehilangan deteksi dapat diatasi karena buah terlihat dari sudut lain, sedangkan deteksi palsu sulit dikompensasi.

### 2. Pelacakan titik dengan CoTracker
CoTracker melacak $N$ titik pada jendela pendek $T$ citra ($T = 8$). Masukannya adalah tensor kueri $N \times 3$ dan keluarannya adalah tensor $T \times N \times 2$ posisi disertai bendera keterlihatan. Dengan perhatian terfaktor, kompleksitas turun dari $O(N^2 T^2)$ menjadi $O(N^2 + T^2)$.

### 3. Penanda, lintasan, dan inisialisasi
Sebuah penanda berupa titik 3D homogen dan lintasan kotak pembatas yang diamati. Pada jendela pertama, pusat kotak dari bingkai pertama menjadi kueri; kotak yang memuat titik hasil lacak dianggap tertutupi (*covered*), dan kotak yang belum tertutupi menambah baris kueri pada bingkai berikutnya. Titik dengan empat pengamatan terlihat atau lebih (50% jendela) membentuk lintasan kotak. Odometri visual diinisialisasi dari dua bingkai dengan matriks esensial (algoritma lima titik dengan RANSAC), pose bingkai kedua dipulihkan, dan titik 3D ditriangulasi.

### 4. Lingkar utama dan graf faktor
Pose setiap bingkai berikutnya diestimasi dari korespondensi 3D-2D (PnP atau resection). Penanda diproyeksikan ke bingkai pertama jendela baru sebagai kueri awal. Posisi penanda dan pose dioptimasi bersama dengan graf faktor (faktor reproyeksi) dan algoritma Levenberg-Marquardt.

### 5. Pascapemrosesan dan implementasi
Buah yang terlihat kurang dari $V_{min} = 8$ bingkai dibuang karena diduga deteksi palsu atau sangat terhalang. Implementasi memakai Python 3.11, OpenCV 4.9, GTSAM 4.3, kode CoTracker 2 asli, dan kalibrasi intrinsik dari COLMAP.

## Eksperimen dan Hasil
Metrik: HOTA (skor 100 berarti pelacakan sempurna), jumlah prediksi, acuan, FP, FN, dan galat pencacahan. Acuan hitungan adalah anotasi citra (jumlah jeruk beridentitas unik pada tiap urutan), bukan panen; hitungan tidak dilaporkan per kelas.

| Urutan | HOTA | Prediksi | Acuan | FP | FN | Galat |
|---|---|---|---|---|---|---|
| V01 | 30,183 | 117 | 110 | 7 | 0 | 6,36% |
| V04 | 66,485 | 100 | 105 | 0 | 5 | -4,76% |
| V05 | 50,228 | 143 | 148 | 0 | 5 | -3,38% |
| V06 | 40,583 | 175 | 122 | 53 | 0 | 43,44% |
| V08 | 42,477 | 228 | 192 | 36 | 0 | 18,75% |
| V11 | 45,431 | 98 | 87 | 11 | 0 | 12,64% |
| V12 | 45,810 | 117 | 115 | 2 | 0 | 1,74% |
| Semua | 47,457 | 978 | 879 | 109 | 10 | 11,26% |

Galat gabungan 11% sangat dipengaruhi V06 (43%), yang memiliki banyak positif palsu akibat kesalahan pengenalan ulang buah yang muncul kembali, diduga karena estimasi pose yang buruk. Waktu pemrosesan 3D berkisar sekitar 3 menit (V05) sampai 15 menit (V08), jauh lebih cepat daripada metode berbasis COLMAP (sekitar setengah jam hanya untuk SfM pada urutan terpendek, dengan perangkat keras Intel Xeon 3,40 GHz dan RTX 4000) karena jumlah penanda dibatasi pada buah. Penulis membandingkan dengan karya sebelumnya sendiri (HOTA 56,039, galat median 6,95%) dan menyimpulkan metode ini tidak menunjukkan kinerja lebih baik; untuk dataset ini perhatian silang tidak memberi keuntungan jelas atas asumsi lintasan independen.

## Kelebihan dan Keterbatasan
Keterbatasan yang dinyatakan penulis: titik tunggal kurang mewakili tampilan dan geometri penuh buah 3D; hasil tidak melampaui karya sebelumnya; metode tidak diuji pada cuaca buruk dan asumsi penanda statis akan terganggu oleh angin (usulan: odometri visual semantik dengan penanda kaku seperti batang, tiang, pagar); hanya urutan dengan cukup buah yang dipilih untuk odometri visual; validasi pada dataset, spesies, dan sistem tanam lain diperlukan.

Menurut pembacaan ringkasan ini, bukti terbatas pada satu spesies dan tujuh urutan dengan pemilihan subset berdasarkan kecukupan buah, sehingga hasil tidak mewakili seluruh dataset; ada tiga urutan dengan galat di atas 10% dan dua urutan dengan FP puluhan; metode bergantung pada kualitas awal pose dan asumsi buah statis.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat berulang kali dalam satu video yang melintasi pohon, dengan mekanisme pelacakan titik berbasis perhatian (CoTracker) yang dikombinasikan dengan rekonstruksi 3D (odometri visual dan graf faktor), sehingga identitas buah dijaga lewat lintasan titik dan konsistensi proyeksi 3D. Hitungan dilaporkan per urutan (per pohon) dan total, bukan per kelas; acuannya adalah anotasi citra pada MOrangeT, bukan panen atau hitungan manual lapangan. Pemandangan yang dicakup adalah video bergerak mengitari satu pohon, bukan sisi pohon yang diambil terpisah.

Untuk pencacahan tandan sawit multi-sisi, hal yang dapat dipindahkan adalah pemodelan identitas melalui penanda 3D dengan pose kamera bersama dan pembuangan lintasan pendek (ambang 8 bingkai). Syaratnya adalah urutan bingkai berkelanjutan dengan tumpang tindih tinggi dan jumlah buah memadai untuk estimasi pose; keduanya belum tentu terpenuhi pada citra tetap dari 4 sampai 8 sisi pohon. Hasil makalah juga menunjukkan bahwa pengenalan ulang geometris rentan terhadap kesalahan pose.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `santos2026multi`.

Santos memakai CoTracker untuk melacak banyak buah, melokalisasi buah dalam 3D, dan memperkirakan pose kamera dari video kebun jeruk manis, dengan kotak pembatas YOLOv5 sebagai kueri dan optimasi graf faktor. Pada tujuh urutan MOrangeT, sistem memprediksi 978 buah terhadap acuan 879 (galat 11,26%; HOTA 47,457), tanpa menunjukkan kinerja lebih baik daripada karya penulis sebelumnya (HOTA 56,039; galat median 6,95%).

Catatan verifikasi data: Semua angka hasil ada pada Tabel 2 (seksi 3); rincian dataset pada Tabel 1 (seksi 2.1); jumlah citra dan buah OranDet pada seksi 2.2; parameter ($T = 8$, $V_{min} = 8$, ambang keyakinan 0,7, IoU 0,2) pada seksi 2.2 sampai 2.8; perbandingan dengan karya sebelumnya pada seksi 4.3. Detail MOrangeT di luar tabel tidak dilaporkan di teks ini. Makalah ini berbahasa Inggris dengan abstrak Portugis; teks ekstraksi baik.
