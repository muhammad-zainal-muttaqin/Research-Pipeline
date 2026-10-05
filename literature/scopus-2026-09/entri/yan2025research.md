# Research on an Apple Recognition and Yield Estimation Model Based on the Fusion of Improved YOLOv11 and DeepSORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yan2025research` |
| Judul asli | Research on an Apple Recognition and Yield Estimation Model Based on the Fusion of Improved YOLOv11 and DeepSORT |
| Penulis | Yan, Zhanglei; Wu, Yuwei; Zhao, Wenbo; Zhang, Shao; Li, Xu |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [yan2025research.pdf](../pdf/yan2025research.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15070765

## Gambaran Umum
Makalah ini mengusulkan APYOLO, yaitu detektor apel yang memperbaiki YOLOv11 dengan modul perhatian kanal multi-skala (*multi-scale channel attention*, MSCA) dan fungsi kerugian EnMPDIoU, lalu menggabungkannya dengan pelacak DeepSORT untuk estimasi hasil panen apel. Pada DeepSORT ditambahkan strategi garis penghitung (*region of line*, ROL) yang menghitung apel saat melintasi garis tertentu, dikombinasikan dengan ID unik tiap apel agar buah tidak terhitung ganda.

Data berupa 3.780 citra apel dan 10 berkas video pohon apel dari kebun di Alar, Xinjiang, Tiongkok (sekitar 2.000 pohon pada 12.871,17 m²), direkam pada 1 sampai 7 Oktober 2024 dengan iPhone 13. Pada pengujian detektor, APYOLO mencapai mAP@0,5 sebesar 82,0% dan mAP@0,5–0,95 sebesar 48,6%, dibanding 79,8% dan 46,5% untuk YOLOv11 dasar. Pada estimasi hasil panen dari 10 video, akurasi keseluruhan yang dilaporkan sekitar 84,45% dengan koefisien kecocokan 0,96556 terhadap hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil apel yang akurat penting untuk pengelolaan kebun, perencanaan pasar, dan pendapatan petani, sedangkan metode tradisional berbasis survei lapangan bersifat padat karya, bergantung pada pengamat, dan sulit diskalakan. Kendala utama pada kebun padat adalah apel yang tertutup daun, ranting, atau buah lain, sehingga buah terlewat atau salah dikenali dan hasil panen ditaksir terlalu rendah.

Penulis merujuk karya terdahulu pada arsitektur deteksi, kompresi model, fungsi kerugian, dan pelacakan multi-objek (*multi-object tracking*, MOT), serta menyebut bahwa oklusi dan tumpang tindih buah tetap menjadi tantangan. Makalah ini menjawabnya dengan peningkatan detektor untuk buah kecil atau tertutup sebagian dan mekanisme penghitungan berbasis pelacakan untuk menekan hitungan berulang.

## Ide Utama
Gagasan utamanya terdiri dari tiga komponen. Pertama, MSCA memakai pengumpulan (*pooling*) rerata dan maksimum pada arah tinggi dan lebar, menggabungkannya, lalu menghasilkan bobot perhatian bergaya *coordinate attention* untuk menangkap fitur apel pada berbagai ukuran. Kedua, EnMPDIoU memperbaiki MPDIoU dengan memakai jarak titik pusat kotak, selisih panjang diagonal, dan normalisasi dengan kuadrat diagonal kotak penutup terkecil.

Ketiga, DeepSORT dipakai untuk memberi ID unik tiap apel, dan garis ROL dipakai sebagai pemicu penghitungan saat apel melintasinya, sehingga apel yang melintasi garis berulang kali akibat ranting bergoyang tidak dihitung ganda. Penulis memilih DeepSORT karena IDF1 yang dilaporkan lebih tinggi daripada StrongSORT dan ByteTrack pada pembandingan internal mereka.

## Cara Kerja Langkah demi Langkah

```
 video --> bingkai --> APYOLO (YOLOv11 + MSCA + EnMPDIoU) --> kotak apel
 kotak --> DeepSORT (gerak + tampilan, ID unik) --> garis ROL --> hitungan
```

### 1. Akuisisi dan praproses data
Citra berukuran 1279 × 1706 piksel diambil pada hari cerah dan berawan, dengan variasi sudut, pencahayaan, dan jarak; fokusnya adalah apel menjelang panen yang tidak dibungkus. Karena sumber daya terbatas, 10 pohon dipilih acak untuk dihitung manual, dan 200 apel dipanen serta ditimbang. Massa rerata apel diperkirakan sekitar 0,254 kg. Praproses mencakup penghapusan citra yang sangat mirip dan augmentasi (skala abu-abu, normalisasi, rotasi, kecerahan, derau Gauss, dan pengaburan Gauss). Data dibagi acak 8:1:1: 3.024 citra latih serta masing-masing 378 citra validasi dan uji. Anotasi memakai LabelImg dalam format TXT. Penulis menyebut jumlah total citra tetap sama setelah penyaringan dan augmentasi.

### 2. Pelatihan
Pelatihan memakai GPU NVIDIA RTX 3090, PyTorch 1.12.1, dan CUDA 11.2. Pengoptimal adalah SGD dengan laju belajar awal 0,01, momentum 0,937, peluruhan bobot 0,0005, ukuran *batch* 32, ukuran citra 640 × 640, dan kesabaran (*patience*) 30 epoch untuk penghentian awal.

### 3. Modul MSCA
Pengumpulan rerata dan maksimum pada arah tinggi dan lebar menghasilkan empat representasi, yang digabungkan dan diproses konvolusi 1 × 1. Selanjutnya dilakukan penyematan koordinat (rerata global terurai sepanjang sumbu X dan Y) untuk menghasilkan bobot perhatian $g_h$ dan $g_w$, diikuti normalisasi *batch*, aktivasi h_swish, dan pada sebagian jalur konvolusi 3 × 3 lokal. Pada pembahasan teks, singkatan MSCA kadang dijabarkan sebagai *multi-scale context aggregation*; entri ini mengikuti istilah *multi-scale channel attention* pada abstrak.

### 4. Fungsi kerugian EnMPDIoU
Fungsi ini dihitung sebagai IoU dikurangi kuadrat jarak titik pusat dibagi kuadrat diagonal kotak penutup ($c^2$), dikurangi kuadrat selisih panjang diagonal kotak prediksi dan kotak acuan dibagi $c^2$. Penulis menyebut keunggulannya terhadap MPDIoU adalah ketahanan terhadap derau, kompleksitas, dan kesensitifan pada target kecil.

### 5. Pelacakan dan penghitungan
DeepSORT mengekstraksi fitur tampilan dan gerak dari kotak apel, menghitung kemiripan antarbingkai, dan memberi ID unik. Hitungan bertambah saat apel dengan ID tertentu melintasi garis ROL. Penulis membandingkan DeepSORT dengan StrongSORT dan ByteTrack: IDF1 79,682 untuk DeepSORT, 76,653 untuk StrongSORT, dan 71,697 untuk ByteTrack. Dataset pelacakan pembanding tidak dijelaskan terpisah dari data penelitian.

## Eksperimen dan Hasil
Detektor dievaluasi pada set uji dengan presisi (P), recall (R), mAP@0,5, mAP@0,5–0,95, jumlah parameter, GFLOPs, dan waktu inferensi, dibandingkan dengan YOLOv5, v6, v8, v9t, v10n, v10s, dan v11. Estimasi hasil dievaluasi pada 10 video terhadap hitungan manual.

| Model | P (%) | R (%) | mAP@0,5 (%) | mAP@0,5–0,95 (%) | Parameter | GFLOPs | Inferensi (ms) |
|---|---|---|---|---|---|---|---|
| APYOLO | 85,0 | 71,4 | 82,0 | 48,6 | 2.595.771 | 6,44 | 10,6 |
| YOLOv5 | 83,9 | 68,9 | 79,4 | 46,0 | 2.188.019 | 5,92 | 9,36 |
| YOLOv8 | 84,5 | 69,8 | 80,6 | 46,9 | 2.690.403 | 6,94 | 14,26 |
| YOLOv9t | 85,0 | 69,4 | 80,1 | 46,8 | 1.765.123 | 6,70 | 26,96 |
| YOLOv11 | 84,2 | 69,1 | 79,8 | 46,5 | 2.590.035 | 6,44 | 10,20 |

Ablasi (Tabel 4) menunjukkan bahwa MSCA saja menghasilkan P 88,5, R 71,3, mAP@0,5 82,1, dan mAP@0,5–0,95 48,5; EnMPDIoU saja menghasilkan P 84,0, R 71,7, mAP@0,5 81,8, dan mAP@0,5–0,95 48,7; gabungan keduanya menghasilkan P 85,0, R 71,4, mAP@0,5 82,0, dan mAP@0,5–0,95 48,6. Peningkatan APYOLO terhadap YOLOv11 yang disebut abstrak (2,2%, 2,1%, 0,8%, dan 2,3% untuk mAP@0,5, mAP@0,5–0,95, presisi, dan recall) sesuai dengan selisih poin persentase Tabel 4. MSCA menambah 5.736 parameter dan 0,4 ms waktu inferensi.

Pada estimasi hasil dari 10 video, penulis melaporkan koefisien kecocokan antara hitungan model dan hitungan manual sebesar 0,96556, galat terbaik 1,4%, dan akurasi keseluruhan sekitar 84,45%. Abstrak menyatakan bahwa kombinasi ID unik dan strategi ROL lebih akurat daripada ID unik saja, tetapi angka untuk ID unik saja tidak tercantum pada teks yang tersedia. Penulis menyebut galat yang dapat diterima pada estimasi hasil lapangan sekitar 5% sampai 15%.

## Kelebihan dan Keterbatasan
Penulis menyatakan keterbatasan berikut: penambahan MSCA dan EnMPDIoU menaikkan skala parameter dan waktu inferensi; garis ROL sedikit menurunkan sensitivitas terhadap gerakan kecil dan oklusi, terutama pada kebun padat berdaun lebat; data dikumpulkan pada kondisi relatif stabil sehingga cuaca seperti kabut, badai, atau badai pasir belum diuji; dan kapasitas pemrosesan pada perangkat tepi atau tertanam dapat terbatas. Penulis juga menyebut kasus positif palsu dan negatif palsu akibat latar kompleks, pencahayaan buruk, kemiripan warna, ukuran kecil, dan tumpang tindih buah. Rencana lanjutan mencakup fusi citra kedalaman atau inframerah, pemangkasan dan distilasi model, dan integrasi dengan lengan robot pemetik.

Menurut pembacaan ringkasan ini, hanya satu kebun dan satu rangkaian akuisisi (1 sampai 7 Oktober 2024) yang dipakai, dan data tidak tersedia untuk umum, sehingga hasil tidak dapat direplikasi dari luar. Menurut pembacaan ringkasan ini, selisih antarmodel pada Tabel 3 berkisar sekitar satu sampai tiga poin persentase tanpa pengulangan atau simpangan baku, sehingga signifikansinya tidak dapat dinilai. Menurut pembacaan ringkasan ini, akurasi estimasi 84,45% didefinisikan tidak jelas pada teks (tidak ada rumus), dan acuan hitungan adalah hitungan manual dari video, bukan buah yang dipanen dari seluruh pohon.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan: detektor YOLO dengan DeepSORT memberi ID unik tiap apel, dan hitungan bertambah saat ID melintasi garis ROL. Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas apel. Acuan hitungan adalah hitungan manual pada video yang sama (10 berkas video), sedangkan data massa buah dari 10 pohon (200 apel yang dipanen dan ditimbang) hanya dipakai untuk memperkirakan massa rerata apel. Perbandingan hitungan model terhadap panen aktual pada pohon yang sama tidak dilaporkan.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah penghitungan berbasis pelacakan dengan garis penghitung yang menekan hitungan ganda pada gerakan satu arah, serta praktik membandingkan algoritma pelacakan dengan IDF1. Pelacakan ini berlaku untuk satu urutan video, sehingga tidak menyatukan identitas buah yang sama pada sisi pohon yang berbeda, dan makalah tidak membahas hal itu. Strategi garis penghitung menghitung buah yang melintasi garis, bukan buah unik per pohon, sehingga tidak langsung sesuai dengan inventaris per pohon dari beberapa sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `yan2025research`.

Yan dkk. mengusulkan APYOLO, yaitu YOLOv11 yang ditambah perhatian kanal multi-skala (MSCA) dan kerugian EnMPDIoU, yang dikombinasikan dengan DeepSORT dan strategi garis penghitung (ROL) untuk menghitung apel pada video kebun di Alar, Xinjiang. Detektor mencapai mAP@0,5 82,0% dan mAP@0,5–0,95 48,6% (YOLOv11 dasar 79,8% dan 46,5%), dan akurasi estimasi hasil dari 10 video dilaporkan sekitar 84,45% terhadap hitungan manual.

Catatan verifikasi data: Angka detektor berasal dari Tabel 3 dan ablasi dari Tabel 4 (seksi 3.2). Jumlah data dan pembagian 8:1:1 berasal dari seksi 2.1; hiperparameter dari Tabel 2. Angka 84,45%, koefisien 0,96556, dan galat terbaik 1,4% berasal dari seksi 4 (Diskusi) dan merujuk Gambar 18 dan 19 yang tidak terbaca dari teks, sehingga hitungan per video tidak dapat diverifikasi. Nilai IDF1 pembanding pelacak disebut di seksi 2.7 tanpa tabel atau rincian dataset. Teks juga memuat klaim literatur tentang MSCA dan MPDIoU (misalnya angka berbasis ImageNet dan MOT16) yang bukan hasil makalah ini dan tidak dikutip di sini. Hasil ablasi pada kolom Tabel 4 ditulis berurutan pada ekstraksi, dengan tanda centang tidak terbaca pasti, sehingga konfigurasi tiap baris disimpulkan dari pembahasan teks.
