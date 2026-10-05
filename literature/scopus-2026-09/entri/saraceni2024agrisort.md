# AgriSORT: A Simple Online Real-time Tracking-by-Detection framework for robotics in precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saraceni2024agrisort` |
| Judul asli | AgriSORT: A Simple Online Real-time Tracking-by-Detection framework for robotics in precision agriculture |
| Penulis | Saraceni, Leonardo; Motoi, Ionut M.; Nardi, Daniele; Ciarfuglia, Thomas A. |
| Tahun | 2024 |
| Venue | Proceedings IEEE International Conference on Robotics and Automation |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [saraceni2024agrisort.pdf](../pdf/saraceni2024agrisort.pdf)
- DOI resmi: https://doi.org/10.1109/icra57147.2024.10610231

## Gambaran Umum
Makalah ini mengusulkan AgriSORT, sebuah kerangka pelacakan multi-objek (*multi-object tracking*, MOT) berbasis *tracking-by-detection* yang berjalan daring dan waktu-nyata untuk robotika pertanian presisi. Pelacak ini hanya memakai informasi gerak, tanpa fitur penampakan (*appearance*), untuk mengaitkan deteksi antarbingkai. Penulis mengikuti jalur SORT dan memodifikasi formulasi *Kalman Filter* agar sesuai dengan kondisi ketika objek target bersifat statis sedangkan kamera bergerak cepat dan tidak beraturan.

Data yang dipakai adalah empat urutan video anggur meja (*table grape*) dari kebun di Lazio selatan, Italia, yang direkam dengan kamera Intel RealSense D435i dan dianotasi dengan format MOT. Detektor yang dipakai adalah YOLOv5s. Penulis juga merilis tolok ukur MOT pertanian yang baru ini beserta kodenya.

Hasil utama pada Tabel II menunjukkan bahwa pada kedua urutan *CloseUp* AgriSORT mengungguli semua pelacak pembanding pada MOTA, IDF1, dan HOTA: pada CloseUp1 MOTA 65,93, IDF1 72,00, HOTA 48,71, dan pada CloseUp2 MOTA 66,13, IDF1 73,00, HOTA 56,08. Pada urutan *Overview* hasilnya lebih beragam; SORT tetap kompetitif pada beberapa metrik. AgriSORT mencatat jumlah lintasan *mostly tracked* (MT) tertinggi pada keempat urutan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Analisis bingkai tunggal tidak memadai untuk banyak tugas pertanian, karena perubahan sudut pandang dapat menghasilkan pengukuran yang berbeda. Penulis menyebut estimasi hasil panen sebagai salah satu kebutuhan utama: pelacakan diperlukan agar objek hanya dihitung satu kali. Penulis juga menyebut penggunaan sumber daya, manajemen tanaman, dan akurasi yang lebih konsisten dibanding deteksi saja sebagai kegunaan pelacakan.

Pelacak mutakhir seperti SORT, DeepSORT, dan JDE umumnya mengandalkan model penampakan karena dirancang untuk objek yang mudah dibedakan, misalnya mobil atau pejalan kaki. Penulis menyatakan bahwa pada lahan pertanian semua tanaman tampak serupa dan statis, sehingga fitur penampakan kurang efektif. Selain itu, model penampakan memerlukan data pelatihan tambahan yang jarang tersedia karena anotasi memerlukan tenaga ahli. Lingkungan kebun juga dicirikan gerak kamera ekstrem, perubahan pencahayaan mendadak, dan oklusi yang kuat. Pendekatan terdekat, LettuceTrack, memanfaatkan pola tanam yang teratur dan kamera menghadap ke bawah pada gerak lurus, sehingga menurut penulis tidak efektif untuk gerak bebas dan pencahayaan yang bervariasi.

## Ide Utama
Karena objek statis dan sumber gerak satu-satunya adalah kamera, gerak kamera dapat diestimasi dari bingkai ke bingkai lalu dipakai untuk memproyeksikan posisi lintasan sebelumnya ke bingkai saat ini. Dengan demikian pencocokan antara lintasan dan deteksi dapat dilakukan hanya dengan tumpang-tindih kotak (*intersection over union*, IoU), tanpa fitur penampakan.

Penulis mengubah *Kalman Filter* standar pada dua hal. Pertama, vektor keadaan hanya memuat pusat dan ukuran kotak, tanpa turunan gerak dan ukuran, karena turunan tersebut dinilai merugikan ketika asumsi gerak linear tidak berlaku. Kedua, langkah prediksi tidak memakai matriks transisi, melainkan transformasi afin hasil estimasi gerak kamera yang diterapkan pada pusat kotak, sedangkan lebar dan tinggi dibiarkan tetap.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Data dikumpulkan di kebun anggur meja di Lazio selatan, Italia, dengan sistem tiang rambat tradisional *Tendone* dan jarak antartanaman 3 meter; tanaman berumur lebih dari tiga tahun. Kamera Intel RealSense D435i direkam pada resolusi HD 1280x720 dengan laju 30 FPS agar kedalaman dan RGB dapat diselaraskan; beberapa urutan diturunkan ke 10 FPS untuk menguji detektor pada laju bingkai rendah. Kamera dibawa dengan tangan untuk menyimulasikan gerak robot saat panen atau estimasi hasil. Anotasi dilakukan dengan CVAT dalam format MOT. Jenis varietas anggur tidak dilaporkan.

Empat urutan dilaporkan pada Tabel I:

| Urutan | Resolusi | Panjang (bingkai) | FPS | Lintasan | Kotak |
|---|---|---|---|---|---|
| CloseUp1 | 1280x720 | 300 | 30 | 23 | 2.583 |
| CloseUp2 | 1280x720 | 300 | 30 | 22 | 3.581 |
| Overview1 | 1280x720 | 100 | 10 | 20 | 1.040 |
| Overview2 | 1280x720 | 100 | 10 | 31 | 721 |

Gerak mencakup perubahan arah mendadak, pola berbentuk U, dan pengambilan jarak dekat tandan anggur.

### 2. Deteksi
Detektor adalah YOLOv5s, dipilih karena keseimbangan kecepatan inferensi dan akurasi. Detektor dilatih pada set data anggur meja dari penelitian sebelumnya yang terdiri atas 242 citra beranotasi dan 1.469 citra yang dianotasi otomatis dengan strategi pembangkitan *pseudo-label*. Perangkat keras pelatihan dan inferensi adalah GPU laptop NVIDIA GeForce RTX 3070 Ti.

### 3. Estimasi gerak kamera
Fitur diekstraksi dengan metode Shi-Tomasi pada bingkai sebelumnya dan bingkai saat ini, lalu aliran optik dihitung dengan algoritma Lucas-Kanade. Dari pasangan titik yang cocok diestimasi matriks transformasi afin 2x3 yang menyatakan gerak kamera. Transformasi afin dapat menangkap translasi, rotasi, skala, dan *shear*, tetapi tidak distorsi perspektif. Penulis beralasan bahwa gerak robot sebagian besar sejajar baris kebun dan laju bingkai tinggi, sehingga efek perspektif terbatas.

### 4. Prediksi dan pembaruan Kalman Filter
Setiap objek terdeteksi diberi satu *Kalman Filter*. Keadaan dan pengukuran adalah $[x_c, y_c, w, h]^T$. Pada prediksi, pusat kotak diproyeksikan dengan matriks afin, sedangkan $w$ dan $h$ tidak berubah. Matriks derau proses dan derau pengukuran adalah matriks diagonal 4x4 dengan $\sigma_q = 0{,}05$ dan $\sigma_r = 0{,}00625$, dikalikan faktor $\delta t$ yang bergantung pada laju bingkai (0,033 untuk 30 FPS dan 0,1 untuk 10 FPS).

### 5. Asosiasi
Matriks penugasan disusun dari IoU antara tiap observasi dan tiap keadaan prediksi, lalu penugasan optimal dicari dengan algoritma Hungarian. Tidak ada fitur penampakan yang dipakai. Teks makalah menyatakan tujuan sebagai "meminimalkan IoU keseluruhan", sedangkan IoU pada dasarnya diharapkan dimaksimalkan; ringkasan ini mencatat rumusan tersebut apa adanya.

```
 bingkai t-1, t -> Shi-Tomasi + Lucas-Kanade -> transformasi afin (gerak kamera)
                                                       |
 lintasan t-1 --------- proyeksi pusat kotak <---------+
                                |
 deteksi YOLOv5s t ---> IoU + Hungarian ---> pembaruan Kalman Filter
```

## Eksperimen dan Hasil
Pembanding adalah SORT, ByteTrack, OC-SORT, StrongSORT, dan BoT-SORT. Semua pelacak memakai detektor yang sama. StrongSORT dan BoT-SORT memerlukan model penampakan tambahan yang tidak dapat disetel ulang karena tidak ada data, sehingga model bawaan pralatih dipakai. Metrik adalah MOTA, IDF1, HOTA, FP, FN, IDs, MT, dan ML, dihitung dengan TrackEval.

Tabel berikut merangkum perbandingan AgriSORT dengan pembanding terbaik pada metrik utama, disalin dari Tabel II makalah (nilai pembanding yang tidak ditampilkan dapat dilihat pada tabel asli).

| Urutan | Metode | MOTA | IDF1 | HOTA | FP | FN | IDs | MT | ML |
|---|---|---|---|---|---|---|---|---|---|
| CloseUp1 | AgriSORT | 65,93 | 72,00 | 48,71 | 459 | 872 | 11 | 11 | 4 |
| CloseUp1 | StrongSORT | 57,37 | 60,25 | 41,20 | 21 | 1.054 | 26 | 6 | 7 |
| CloseUp1 | BoT-SORT | 48,66 | 72,72 | 40,51 | 197 | 1.381 | 56 | 4 | 7 |
| CloseUp2 | AgriSORT | 66,13 | 73,00 | 56,08 | 655 | 1.146 | 10 | 12 | 1 |
| CloseUp2 | ByteTrack | 53,81 | 64,42 | 46,16 | 371 | 1.703 | 18 | 8 | 3 |
| Overview1 | AgriSORT | 62,21 | 73,72 | 52,74 | 255 | 284 | 12 | 13 | 0 |
| Overview1 | SORT | 62,69 | 73,91 | 51,20 | 108 | 367 | 9 | 8 | 2 |
| Overview2 | AgriSORT | 45,08 | 56,88 | 41,33 | 298 | 316 | 14 | 16 | 4 |
| Overview2 | SORT | 49,515 | 61,96 | 44,431 | 110 | 348 | 12 | 10 | 8 |

Pada CloseUp1 nilai IDF1 BoT-SORT (72,72) sedikit lebih tinggi daripada AgriSORT (72,00). Pada Overview1, SORT unggul tipis pada MOTA dan IDF1. Pada Overview2, SORT unggul pada MOTA, IDF1, dan HOTA. Penulis menjelaskan bahwa SORT kompetitif ketika asumsi gerak linear terpenuhi, seperti pada Overview2 yang berupa jalan lambat dan teratur sejajar kebun. AgriSORT juga memiliki FP lebih tinggi pada CloseUp dibanding beberapa pembanding, tetapi FN dan jumlah *ID switch* lebih rendah. OC-SORT mencatat jumlah *ID switch* terendah pada CloseUp1 menurut penulis, tetapi memiliki FN yang tinggi. Pada CloseUp1 teks makalah menyebut OC-SORT terbaik dalam IDs, sedangkan Tabel II menunjukkan IDs AgriSORT 11 dan OC-SORT 16; ketidaksesuaian ini dicatat pada bagian verifikasi di bawah. Penulis menekankan MT dan ML karena pada estimasi hasil, lintasan yang hilang menyebabkan tandan anggur yang sama terhitung lebih dari sekali.

Studi tambahan membandingkan estimasi gerak kamera dengan afin versus homografi dan Lucas-Kanade (LK) versus pencocokan fitur ORB (Tabel III). Contoh pada CloseUp1: LK + afin menghasilkan MOTA 65,93, IDF1 72,00, HOTA 48,71, dan 25,93 FPS; ORB + homografi menghasilkan MOTA 67,28, IDF1 76,32, HOTA 53,80, dan 19,71 FPS. Penulis menyimpulkan tidak ada teknik yang jelas dominan pada semua urutan: afin sedikit lebih baik pada urutan *Overview* dan homografi lebih baik pada *CloseUp*. ORB lebih lambat daripada LK rata-rata sekitar 34 FPS pada hampir semua urutan, dan waktu detektor sekitar 10 ms tidak termasuk dalam angka FPS. Kombinasi LK dan afin dipilih sebagai konfigurasi utama karena paling cepat.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis adalah tidak adanya kebutuhan data tambahan untuk model penampakan, ketergantungan minimal, kecepatan yang mendukung penerapan waktu-nyata pada robot, dan kemudahan diperluas ke tanaman lain selama tersedia detektor yang bekerja. Kode dan set data dirilis untuk perbandingan.

Keterbatasan yang dinyatakan penulis: pada gerak linear lambat (Overview2) SORT tetap kompetitif; estimasi gerak kamera masih dapat diperbaiki dengan teknik berbasis pembelajaran; dan pelacak belum diperluas ke kelas campuran yang mencakup objek bergerak seperti orang atau traktor.

Menurut pembacaan ringkasan ini, evaluasi terbatas pada satu komoditas (anggur meja), satu kebun, dan empat urutan pendek (100 sampai 300 bingkai) dengan 20 sampai 31 lintasan per urutan, sehingga generalisasi ke tanaman atau kondisi lain belum teruji. Menurut pembacaan ringkasan ini, model gerak berupa transformasi afin pada pusat kotak mengasumsikan objek statis dan tidak memodelkan perubahan skala kotak akibat gerak mendekat; AgriSORT juga tidak memiliki mekanisme pemulihan identitas melalui penampakan setelah oklusi panjang. Tidak ada pengujian pada pohon yang dikitari dari banyak sisi, dan evaluasi tidak mengaitkan hitungan akhir dengan hasil panen aktual.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat lebih dari sekali dalam urutan video: tandan anggur statis dipotret berulang pada bingkai berurutan saat kamera bergerak, dan identitas dipertahankan melalui pelacakan dengan kompensasi gerak kamera (estimasi afin dari aliran optik), prediksi *Kalman Filter*, dan asosiasi IoU dengan algoritma Hungarian. Mekanisme ini bersifat pelacakan antarbingkai berurutan dalam satu lintasan video, bukan pencocokan antarsisi pohon yang direkam terpisah. Penulis menyatakan secara eksplisit bahwa pelacakan diperlukan agar objek tidak terhitung ganda pada estimasi hasil, tetapi makalah tidak melaporkan jumlah buah total yang dihitung.

Hitungan per kelas tidak dilaporkan; pelacakan memperlakukan semua tandan sebagai satu kelas, dan acuan evaluasi adalah anotasi lintasan pada citra (format MOT di CVAT), bukan panen atau hitung manual di lapangan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan kompensasi gerak kamera pada pelacak tanpa fitur penampakan untuk objek statis yang serupa, serta metrik MT, ML, dan *ID switch* untuk menilai konsistensi identitas. Karena AgriSORT hanya mengaitkan bingkai berurutan, ia tidak menyelesaikan penggabungan identitas antarsisi pohon yang tidak tumpang-tindih secara temporal.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `saraceni2024agrisort`.

Saraceni dkk. mengusulkan AgriSORT, pelacak *tracking-by-detection* waktu-nyata yang hanya memakai informasi gerak untuk robotika pertanian: gerak kamera diestimasi dengan aliran optik Lucas-Kanade dan transformasi afin untuk memproyeksikan lintasan antarbingkai pada *Kalman Filter* yang dimodifikasi, lalu deteksi dicocokkan dengan IoU dan algoritma Hungarian. Pada empat urutan video anggur meja yang dianotasi, AgriSORT mengungguli SORT, ByteTrack, OC-SORT, StrongSORT, dan BoT-SORT pada dua urutan jarak dekat (misalnya MOTA 65,93 dan 66,13) dan mencatat MT tertinggi pada semua urutan, sedangkan pada urutan *overview* SORT tetap kompetitif pada beberapa metrik.

Catatan verifikasi data: Angka urutan data (Tabel I), hasil perbandingan pelacak (Tabel II), dan studi estimasi gerak kamera (Tabel III) diambil dari tabel makalah; ekstraksi teks menaruh tiap sel tabel pada baris terpisah sehingga pengelompokan kolom disusun dari urutan baris, dan isi tabel Tabel II yang disalin ke ringkasan ini dibaca dari urutan tersebut. Parameter $\sigma_q$, $\sigma_r$, dan $\delta t$ berasal dari Seksi IV-A. Jumlah citra pelatihan detektor (242 dan 1.469) berasal dari Seksi IV-A dan merujuk pada set data penelitian terdahulu. Teks makalah menyebut OC-SORT terbaik pada *ID switch* untuk CloseUp, sedangkan Tabel II memperlihatkan nilai IDs AgriSORT lebih rendah pada kedua urutan CloseUp; ketidaksesuaian ini tidak dapat diselesaikan dari teks. Jumlah pohon atau tandan anggur total, varietas, dan hasil panen aktual tidak dilaporkan. Makalah berupa pracetak arXiv (versi 2) yang menyebut diajukan ke IEEE.
