# Research on Greenhouse Eggplant Fruit Detection and Tracking-Based Counting Using an Improved YOLOv5s-DeepSORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2026research` |
| Judul asli | Research on Greenhouse Eggplant Fruit Detection and Tracking-Based Counting Using an Improved YOLOv5s-DeepSORT |
| Penulis | Zhu, Jianfei; Bai, Long; Liu, Caishan; Nian, Chengxu; Zhang, Keke; Yang, Sibo |
| Tahun | 2026 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [zhu2026research.pdf](../pdf/zhu2026research.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture16020253

## Gambaran Umum
Makalah ini (Zhu dkk., *Agriculture* 2026, 16, 253) mengusulkan sistem deteksi dan pencacahan buah terong bulat (Tianjin round eggplant) di rumah kaca dari video yang direkam sepanjang baris tanaman. Sistem terdiri dari detektor YOLOv5s yang diperingan, pelacak DeepSORT, dan aturan pencacahan berbasis zona hitung (*counting zone*). Detektor dimodifikasi dengan tiga perubahan: *backbone* diganti MobileNetV3, modul perhatian kanal *Efficient Channel Attention* (ECA) disisipkan, dan blok C3 pada *neck* diganti blok C2f.

Data berasal dari 10 video valid (masing-masing 2 sampai 3 menit, 960 × 544 piksel, 30 fps) yang direkam dengan kamera Intel RealSense D435i di sebuah rumah kaca di Provinsi Shandong, Tiongkok. Tujuh video dipakai untuk membangun set data deteksi (4.601 citra setelah augmentasi), dan tiga video (V01 sampai V03) dicadangkan untuk menguji pelacakan dan pencacahan. Hanya citra RGB yang dipakai untuk deteksi; kamera kedalaman tidak dimanfaatkan.

Hasil utama: detektor yang diperbaiki mencapai presisi 97,8% dan mAP@0,5 sebesar 99,2% dengan 4.450.127 parameter dan 8,1 GFLOPs, dibandingkan YOLOv5s awal (presisi 95,5%, mAP@0,5 97%, 7.063.542 parameter, 16,5 GFLOPs). Pada tiga video uji, metode pencacahan mencapai akurasi 83,3%, 82,4%, dan 94,8%; penulis melaporkan akurasi rata-rata 86,82% dan koefisien determinasi $R^2 = 0{,}9677$ terhadap hitungan manual. SORT, DeepSORT, dan ByteTrack pada deteksi yang sama menghasilkan jumlah ID yang jauh melebihi hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil panen terong rumah kaca bergantung pada ketepatan hitungan buah. Penulis menyatakan bahwa pencacahan manual oleh pekerja di lapangan bersifat subjektif, padat karya, dan terganggu oleh oklusi buah, sehingga tidak memadai untuk pemantauan waktu-nyata skala besar. Metode pengolahan citra klasik berbasis warna, bentuk, dan tekstur dinilai kurang tangguh pada kondisi rumah kaca yang memiliki oklusi daun dan batang, pantulan spekular, gangguan latar dari struktur bangunan, dan tumpang tindih antarbuah.

Pada video, buah yang sama muncul pada bingkai-bingkai berurutan, sehingga deteksi per bingkai saja menimbulkan hitungan ganda. Pelacakan multi-objek (*multi-object tracking*, MOT) memberi setiap target sebuah ID yang bertahan, tetapi kerapatan buah yang tinggi dan oklusi berat menyebabkan pergantian ID (*ID switch*) untuk target yang sama. Pergantian ID itu menggembungkan hitungan bila jumlah ID dipakai sebagai jumlah buah. Penulis juga menyebut bahwa model YOLO yang lebih baru tidak selalu lebih baik pada lingkungan rumah kaca khusus dan bahwa akurasi yang lebih tinggi sering menambah beban komputasi yang menyulitkan penerapan pada perangkat terbatas.

## Ide Utama
Gagasan pertama adalah memperingan detektor tanpa menurunkan akurasi, agar dapat dipasang pada robot inspeksi. Gagasan kedua adalah mengganti hitungan "ID terakhir" (akumulasi ID) dengan aturan pemicu wilayah: sebuah ID dihitung satu kali, yaitu ketika pusat kotak pembatas (*bounding box*) pertama kali memasuki zona hitung di tengah bingkai dan ID tersebut belum tercatat dalam himpunan ID yang telah dihitung. Zona hitung dipilih di tengah bingkai karena target di dekat tepi bingkai cenderung terlihat sebagian, tidak stabil, atau berkotak tidak lengkap saat baru masuk bidang pandang.

Penulis tidak menyelesaikan masalah pergantian ID pada tingkat algoritma asosiasi. Aturan zona hitung dan himpunan ID hanya mengurangi akumulasi hitungan ganda dalam bingkai berurutan, sedangkan ambang IoU 0,3 dan masa simpan lintasan (`max_age` atau `max_life`) dinyatakan hanya "sebagian" menurunkan peluang pergantian ID.

## Cara Kerja Langkah demi Langkah

```
 Video per baris -> ekstraksi bingkai (tiap 15) -> anotasi LabelMe -> latih detektor
 Video uji -> YOLOv5s ringan -> DeepSORT (Kalman + ReID + IoU) -> zona hitung
                                                    -> himpunan ID terhitung -> jumlah
```

### 1. Akuisisi data
Video direkam pada 12 November 2024 di sebuah fasilitas sayuran rumah kaca di Desa Jijialishuang, Kota Qingzhou, Provinsi Shandong. Tanaman sasaran adalah terong bulat Tianjin dengan sistem tanam lahan datar, jarak baris 1,5 m, dan panjang lorong 12 sampai 15 m. Buah terutama berada pada ketinggian 0,5 sampai 1,2 m. Kamera Intel RealSense D435i dipasang pada platform bergerak setinggi 0,8 m dari tanah dengan sudut pitch sekitar -10 derajat untuk meniru sudut pandang robot inspeksi. Platform ditarik manual dengan kecepatan tetap 0,1 m/s sepanjang baris tanaman. Kondisi pencahayaan bervariasi, dengan gangguan bangunan, oklusi daun, dan pencahayaan tidak seragam. Hasilnya 10 video valid berdurasi 2 sampai 3 menit.

### 2. Penyusunan set data
Tujuh video dipilih acak untuk set data deteksi dan tiga video lainnya dicadangkan untuk menguji pelacakan dan pencacahan. Bingkai diekstraksi tiap 15 bingkai dari tujuh video itu. Augmentasi memakai OpenCV 4.8.0.76: pembalikan, pemotongan, penyesuaian kecerahan, derau Gaussian, pengaburan, dan efek vinyet. Setelah augmentasi dan seleksi diperoleh 4.601 citra, dibagi 8:1:1 menjadi 3.681 citra latih serta masing-masing 460 citra validasi dan uji. Anotasi berupa kotak pembatas berkelas tunggal "eggplant" dibuat dengan LabelMe 5.5.0 dalam format TXT YOLO. Makalah tidak melaporkan jumlah kotak anotasi total. Makalah juga tidak merinci apakah citra hasil augmentasi dari satu bingkai asal dapat tersebar di lebih dari satu subset.

### 3. Detektor YOLOv5s yang diperbaiki
- **MobileNetV3** menggantikan *backbone* CSPDarknet53. Blok MobileNetV3 memakai konvolusi 1 × 1 untuk ekspansi, konvolusi terpisah-kedalaman (*depthwise separable*) 3 × 3, modul *Squeeze-and-Excitation* (SE), konvolusi 1 × 1 untuk proyeksi, dan koneksi residual. Penulis menurunkan bahwa rasio biaya konvolusi terpisah-kedalaman terhadap konvolusi standar adalah $1/N + 1/D_K^2$, yang untuk kernel 3 × 3 dan N besar mendekati 1/9.
- **ECA** memakai *global average pooling*, konvolusi 1D dengan ukuran kernel adaptif $K = \psi(C)$, dan fungsi Sigmoid untuk menghasilkan bobot perhatian kanal tanpa lapisan terhubung penuh.
- **C2f** menggantikan blok C3 pada *neck* untuk memperkuat fusi fitur multi-skala dan aliran gradien.

Pelatihan memakai masukan 640 × 640, ukuran *batch* 16, SGD dengan laju belajar awal 0,01 dan *weight decay* 0,0005, selama 100 *epoch* dengan augmentasi Mosaic dimatikan pada 10 *epoch* terakhir. Perangkat keras: CPU Core i5-12400F, GPU NVIDIA GeForce RTX 4060 Ti, RAM 32 GB; perangkat lunak Python 3.8.20, CUDA 11.3, dan PyTorch 1.9.0.

### 4. Pelacakan dan pencacahan
Bingkai diubah ukurannya menjadi 640 × 640 dengan strategi *letterbox*. Prediksi disaring dengan *non-maximum suppression* (ambang keyakinan 0,6; ambang IoU 0,5) dan hanya kelas terong yang dipertahankan. DeepSORT memprediksi keadaan lintasan dengan filter Kalman dan mengekstraksi sematan tampilan (*appearance embedding*) dengan jaringan ReID ringan. Asosiasi memakai kaskade pencocokan: lintasan terkonfirmasi lebih dahulu dicocokkan berdasarkan jarak kosinus sematan dengan gerbang jarak Mahalanobis dari prediksi Kalman; lintasan tersisa dan belum terkonfirmasi dicocokkan dengan IoU pada ambang 0,3. Lintasan dipertahankan hingga `max_age` bingkai tanpa pencocokan, dan deteksi yang tidak cocok membuka lintasan baru.

Zona hitung ditetapkan pada sumbu horizontal bingkai, dengan batas kiri pada seperlima lebar citra dan batas kanan pada empat perlima lebar citra. Hitungan bertambah satu hanya bila tiga syarat terpenuhi bersamaan: target cocok dengan lintasan yang ada (IoU > 0,3), pusat kotak berada dalam zona hitung, dan ID target belum ada dalam himpunan ID terhitung. Setiap ID dihitung paling banyak satu kali sepanjang video.

### 5. Metrik
Deteksi dinilai dengan presisi, *recall*, dan mAP@0,5 (ambang IoU 0,5 dipilih karena pencacahan hanya memerlukan deteksi yang benar, bukan lokalisasi kotak yang sangat presisi); pada Tabel 3 dilaporkan pula mAP@0,5-0,95. Pencacahan dinilai dengan Counting Accuracy $= (1 - |N_P - N_G|/N_G) \times 100\%$ dan Relative Error $= |N_P - N_G|/N_G \times 100\%$, dengan $N_P$ jumlah prediksi dan $N_G$ hitungan manual.

## Eksperimen dan Hasil
**Perbandingan *backbone* ringan (Tabel 1).** Berdasarkan YOLOv5s awal, empat *backbone* ringan dibandingkan:

| Model | Parameter | Presisi (%) | mAP@0,5 (%) | Ukuran (MB) | GFLOPs |
|---|---|---|---|---|---|
| YOLOv5s | 7.063.542 | 95,5 | 97 | 14,4 | 16,5 |
| GhostNet | 4.870.410 | 94,7 | 98,7 | 10,1 | 7,9 |
| ShuffleNetV2 | 3.792.950 | 93,4 | 96,3 | 7,9 | 8 |
| EfficientNetV2 | 5.404.158 | 94,4 | 98 | 11,1 | 5,6 |
| MobileNetV3 | 3.359.308 | 94,6 | 98,7 | 7 | 6 |

Penulis menyatakan bahwa MobileNetV3 menurunkan parameter, FLOPs, dan ukuran model masing-masing sebesar 52,4%, 63,6%, dan 51,4%, serta memilihnya sebagai *backbone*.

**Ablasi (Tabel 2).** Kombinasi modul pada YOLOv5s:

| MobileNetV3 | ECA | C2f | P (%) | R (%) | mAP@0,5 (%) | Parameter | GFLOPs |
|---|---|---|---|---|---|---|---|
| tidak | tidak | tidak | 95,5 | 98,8 | 97 | 7.063.542 | 16,5 |
| ya | tidak | tidak | 94,6 | 98,4 | 98,7 | 3.359.308 | 6 |
| tidak | ya | tidak | 98,3 | 99,6 | 99,6 | 7.162.105 | 16,6 |
| tidak | tidak | ya | 98,3 | 99,5 | 99,6 | 8.087.542 | 18,6 |
| tidak | ya | ya | 98,7 | 99,4 | 99,7 | 8.153.337 | 18,6 |
| ya | tidak | ya | 96,8 | 98,6 | 99,2 | 4.384.332 | 8,1 |
| ya | ya | tidak | 95,7 | 96,6 | 98,9 | 3.457.871 | 6,1 |
| ya | ya | ya | 97,8 | 97,5 | 99,2 | 4.450.127 | 8,1 |

Konfigurasi akhir (ketiga modul) memiliki presisi dan *recall* lebih rendah daripada varian ECA saja atau C2f saja pada YOLOv5s awal, tetapi jauh lebih ringan. Penulis menyebut bahwa konfigurasi akhir mengurangi parameter dan FLOPs masing-masing sebesar 37,0% dan 50,9% terhadap YOLOv5s awal; angka itu konsisten dengan nilai tabel (4.450.127 terhadap 7.063.542 parameter; 8,1 terhadap 16,5 GFLOPs).

**Perbandingan dengan detektor lain (Tabel 3).**

| Model | P (%) | R (%) | mAP@0,5 (%) | mAP@0,5-0,95 (%) | Parameter | GFLOPs |
|---|---|---|---|---|---|---|
| YOLOv5m | 96,1 | 96,2 | 98,9 | 86,3 | 21.056.406 | 50,6 |
| YOLOv8s | 96,9 | 97,7 | 99,2 | 91,4 | 11.108.531 | 27,3 |
| YOLOv9s | 97 | 97,9 | 99 | 92,2 | 7.195.635 | 26,9 |
| YOLOv10n | 95,2 | 97,1 | 98,6 | 88,1 | 2.707.430 | 8,4 |
| YOLOv11n | 96 | 97,6 | 99,2 | 90,6 | 2.590.035 | 6,4 |
| YOLOv5s | 95,5 | 98,8 | 97 | 85,4 | 7.063.542 | 16,5 |
| YOLOv5s diperbaiki | 97,8 | 97,5 | 99,2 | 89,5 | 4.450.127 | 8,1 |

Presisi model yang diperbaiki adalah yang tertinggi pada tabel, tetapi mAP@0,5-0,95 dan *recall*-nya lebih rendah daripada YOLOv8s dan YOLOv9s. Model ini memiliki parameter dan FLOPs sedikit lebih banyak daripada YOLOv10n dan YOLOv11n. Penulis melaporkan analisis kualitatif pada lima kondisi (terik, gelap, kabur gerak, objek kecil, oklusi cabang dan daun) dengan ambang keyakinan 0,1 dan menyimpulkan bahwa model yang diperbaiki lebih tangguh; analisis itu hanya berupa lima citra terpilih, dan hasilnya tidak dikuantifikasi.

**Pencacahan pada tiga video uji (Tabel 4).** Semua pelacak memakai deteksi yang sama dari YOLOv5s yang diperbaiki. Jumlah akhir tiap video didefinisikan sebagai ID tertinggi pada pelacak pembanding.

| Video | Hitungan manual | SORT | DeepSORT | ByteTrack | Metode usulan | Akurasi metode usulan (%) | Galat relatif metode usulan (%) |
|---|---|---|---|---|---|---|---|
| V01 | 60 | 113 | 132 | 211 | 50 | 83,3 | 16,7 |
| V02 | 68 | 113 | 145 | 223 | 56 | 82,4 | 17,6 |
| V03 | 58 | 124 | 134 | 215 | 55 | 94,8 | 5,2 |

Untuk pelacak pembanding, Tabel 4 mencantumkan akurasi bernilai negatif pada banyak kasus (misalnya DeepSORT V01 -20 dan galat 120; ByteTrack V01 -151,6 dan galat 251,6). Pada V02, ByteTrack menghasilkan 223 ID, yang menurut penulis 3,3 kali jumlah buah sebenarnya; DeepSORT dan SORT masing-masing 2,1 dan 1,7 kali.

**Ringkasan hitungan (bagian Diskusi 4.1).** Penulis melaporkan korelasi prediksi dengan hitungan manual $R^2 = 0{,}9677$, akurasi maksimum 94,83%, dan akurasi rata-rata 86,82%. Rata-rata sederhana dari tiga akurasi pada Tabel 4 (83,3; 82,4; 94,8) kira-kira 86,8%, sehingga cocok dengan angka tersebut (dihitung dalam ringkasan ini). Teks Diskusi menyatakan "ten eggplant fruit videos" dikumpulkan dan dievaluasi, tetapi Tabel 4 hanya berisi tiga video; makalah tidak menjelaskan dasar $R^2$ tersebut, sehingga tidak diketahui apakah $R^2$ dihitung dari tiga atau lebih video.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak dari makalah: (1) detektor yang jauh lebih ringan dengan presisi tertinggi pada perbandingan yang dilaporkan; (2) aturan pencacahan yang sederhana, daring, dan berjalan langsung pada aliran video tanpa rekonstruksi atau pemosaikan citra; (3) perbandingan tiga pelacak baku pada deteksi yang identik.

Keterbatasan yang dinyatakan penulis: set data 4.601 citra mungkin tidak mencakup variasi praktik budidaya, kultivar, musim, dan pencahayaan ekstrem; hitungan bergantung pada mutu deteksi dan pelacakan; pada daun lebat, tumpang tindih buah berat, atau perubahan sudut pandang, buah yang telah dihitung dapat muncul kembali setelah oklusi dengan ID baru sehingga terjadi hitungan ganda; ukuran dan letak zona hitung perlu dioptimalkan; kinerja dapat dipengaruhi kecepatan robot dan laju bingkai.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, evaluasi pencacahan hanya memakai tiga video dari satu rumah kaca, satu kultivar, dan satu hari perekaman, sehingga kesimpulan tentang akurasi rata-rata 86,82% berbasis sampel yang sangat kecil. Kedua, galat metode usulan pada V01 dan V02 (16,7% dan 17,6%) dan semuanya berupa undercount (50 terhadap 60, 56 terhadap 68, 55 terhadap 58); makalah tidak menganalisis arah galat itu. Ketiga, pembanding SORT, DeepSORT, dan ByteTrack dihitung dengan jumlah ID tertinggi tanpa zona hitung, sedangkan metode usulan memakai zona hitung; jadi perbandingan menggabungkan efek zona hitung dan efek pelacak, dan makalah tidak melaporkan DeepSORT yang dilengkapi zona hitung yang sama. Keempat, set data dibangun dari tujuh video dan diperbesar dengan augmentasi, tanpa pernyataan tentang pencegahan kebocoran antara bingkai yang berdekatan pada subset latih, validasi, dan uji; nilai mAP@0,5 hingga 99,6% pada beberapa varian ablasi dapat mencerminkan hal ini, tetapi penyebabnya tidak dapat dipastikan dari teks. Kelima, set data tidak dipublikasikan (tersedia atas permintaan yang wajar).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat berulang kali, tetapi hanya dalam satu aliran video dari satu pandang yang bergerak sepanjang baris tanaman. Mekanisme identitasnya adalah pelacakan temporal (DeepSORT dengan filter Kalman, sematan ReID, dan IoU) ditambah penjaga hitungan berupa zona hitung dan himpunan ID terhitung. Tidak ada pencocokan lintas-pandang, rekonstruksi 3D, atau koreksi statistik dua sisi. Buah yang muncul kembali setelah oklusi dan memperoleh ID baru tidak dapat dicegah dari hitungan ganda, sebagaimana diakui penulis.

Hitungan hanya dilaporkan untuk satu kelas (terong), tanpa pemisahan per tingkat kematangan; rencana penilaian kematangan disebut sebagai pekerjaan mendatang. Acuan hitungannya adalah hitungan manual per video (60, 68, dan 58 buah), bukan hasil panen. Untuk pencacahan tandan kelapa sawit multi-sisi, gagasan yang dapat dipindahkan terbatas: pencatatan ID yang sudah dihitung dan metrik akurasi serta galat relatif dapat dipakai, tetapi aturan zona hitung bergantung pada gerak kamera yang searah dan ID yang bertahan, yang tidak berlaku bila setiap sisi pohon difoto terpisah. Hasilnya juga menunjukkan bahwa pelacak umum tanpa penjaga identitas tambahan menggembungkan hitungan secara besar pada buah yang mirip dan terhalang.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhu2026research`.

Zhu dkk. (2026) mengusulkan kerangka deteksi dan pencacahan terong rumah kaca berbasis YOLOv5s yang diperbaiki (*backbone* MobileNetV3, modul ECA, blok C2f) dan DeepSORT dengan strategi zona hitung. Detektor mencapai mAP@0,5 sebesar 99,2% dengan 4.450.127 parameter dan 8,1 GFLOPs pada set data 4.601 citra dari video rumah kaca. Pada tiga video uji, metode pencacahan mencapai akurasi 83,3%, 82,4%, dan 94,8% terhadap hitungan manual, sedangkan SORT, DeepSORT, dan ByteTrack menghasilkan hitungan yang jauh melampaui jumlah buah sebenarnya.

Catatan verifikasi data: Teks makalah dalam bahasa Inggris dan terbaca utuh; tabel hasil terekstraksi satu sel per baris tetapi urutannya dapat dipetakan. Parameter, GFLOPs, presisi, *recall*, dan mAP@0,5 terdapat pada Tabel 1 sampai 3 (seksi 3.1 sampai 3.3). Hitungan manual, hitungan pelacak, akurasi, dan galat relatif terdapat pada Tabel 4 (seksi 3.5); pada Tabel 4 kolom akurasi dan galat relatif untuk pelacak pembanding dipetakan berdasarkan urutan nilai pada teks ekstraksi, dan angka negatif disalin apa adanya. $R^2 = 0{,}9677$, akurasi maksimum 94,83%, dan akurasi rata-rata 86,82% dikutip dari seksi 4.1 dan 5; angka 94,83% berbeda tipis dari 94,8% pada Tabel 4 karena pembulatan. Perbedaan antara pernyataan "sepuluh video" pada seksi 4.1 dan tiga video pada Tabel 4 tidak dapat diselesaikan dari teks. Penurunan parameter 37,0% dan FLOPs 50,9% dikutip dari abstrak dan seksi 5. Selisih mAP@0,5 sebesar 2,2 poin persentase pada seksi 5 sesuai dengan 99,2% dikurangi 97,0%. Jumlah kotak anotasi, hasil per kelas selain terong, dan rincian pembagian subset pada tingkat video tidak dilaporkan.
