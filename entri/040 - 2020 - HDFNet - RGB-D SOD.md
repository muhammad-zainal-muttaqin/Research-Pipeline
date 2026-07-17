# 040 - Hierarchical Dynamic Filtering Network for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pang2020hdfnet` |
| Judul asli | Hierarchical Dynamic Filtering Network for RGB-D Salient Object Detection |
| Penulis | Youwei Pang, Lihe Zhang, Xiaoqi Zhao, Huchuan Lu |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020), hlm. 235–252 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.06227
- **Kode sumber resmi (PyTorch):** https://github.com/lartpang/HDFNet
- **Google Scholar:** https://scholar.google.com/scholar?q=Hierarchical%20Dynamic%20Filtering%20Network%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Hierarchical%20Dynamic%20Filtering%20Network%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan HDFNet (*Hierarchical Dynamic Filtering Network*), sebuah jaringan untuk deteksi objek menonjol berbasis RGB-D (RGB-D *salient object detection*, SOD), yaitu tugas menghasilkan peta biner yang menandai objek paling mencolok dalam citra dengan bantuan peta kedalaman (citra yang setiap pikselnya menyatakan jarak ke kamera). Alih-alih menggabungkan fitur RGB dan kedalaman dengan operasi statis seperti penjumlahan atau konkatenasi, HDFNet memakai fitur campuran kedua modalitas untuk membangkitkan *kernel* konvolusi dinamis — bobot konvolusi yang dihitung khusus untuk setiap masukan dan setiap posisi piksel — yang diterapkan pada fitur RGB di sisi *decoder*. Karena diterapkan pada tiga tingkat fitur, skema ini disebut penyaringan dinamis hierarkis.

Makalah ini juga mengusulkan *hybrid enhanced loss* (HEL), supervisi tambahan pada wilayah tepi dan wilayah dalam objek tanpa menambah parameter saat inferensi. Pada delapan dataset dan enam metrik evaluasi, HDFNet mengungguli dua belas pembanding; pada dataset NJUD, versi VGG-16 mencapai F-measure maksimum 0,924 dengan galat absolut rata-rata (MAE) 0,037, sekaligus berjalan pada 52 FPS di GPU GTX 1080 Ti.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD berbasis citra RGB saja menghadapi kesulitan pada adegan dengan kontras rendah atau latar yang ramai, karena informasi penampakan semata tidak cukup untuk memisahkan objek dari sekelilingnya. Peta kedalaman menyediakan struktur spasial yang komplementer: objek pada jarak berbeda dari kamera cenderung terpisah jelas pada kanal kedalaman meskipun warnanya mirip dengan latar. Karena itu, metode RGB-D SOD berupaya memadukan kedua modalitas.

Cara pemaduan yang umum dipakai sebelum makalah ini bersifat statis: penjumlahan elemen-demi-elemen, konkatenasi kanal diikuti konvolusi, atau peta atensi dari kedalaman yang dikalikan ke fitur RGB. Pendekatan-pendekatan tersebut, termasuk DMRA (bab 035), memakai parameter fusi yang tetap untuk semua masukan setelah pelatihan selesai. Akibatnya, bobot konvolusi yang sama dipakai untuk citra dengan kualitas dan isi kedalaman yang berbeda-beda, sehingga kemampuan generalisasi model melemah. Masalah kedua lebih mendasar: pada tugas prediksi rapat (*dense prediction*) seperti SOD, kebutuhan optimasi berbeda pada setiap posisi spasial — piksel di tepi objek menuntut ketajaman batas, sedangkan piksel di dalam objek menuntut keseragaman — tetapi konvolusi berbagi bobot (*weight sharing*) memaksa satu set parameter melayani semua posisi, sehingga parameter yang dipelajari menjadi kompromi yang suboptimal. HDFNet menyerang kedua masalah ini sekaligus.

## Ide Utama

Gagasan inti HDFNet adalah mengubah peran kedalaman dari "fitur yang digabungkan" menjadi "penentu cara penggabungan". Fitur RGB dan fitur kedalaman dicampur lebih dahulu, dan dari fitur campuran itu dibangkitkan bobot konvolusi yang spesifik terhadap masukan (*image-specific*) dan spesifik terhadap posisi (*position-specific*). Bobot inilah yang disebut penyaring dinamis (*dynamic filter*): konvolusi yang bobotnya bukan hasil pelatihan semata, melainkan keluaran sebuah sub-jaringan, sehingga setiap citra uji mendapat perlakuan pemrosesan yang berbeda sesuai isinya.

Agar penyaringan menangkap konteks pada beberapa skala, kernel dinamis dibangkitkan dalam tiga laju dilasi (1, 3, dan 5) — sebuah piramida dilasi dinamis — dan diterapkan pada tiga tingkat fitur *decoder*. Sebagai pelengkap, fungsi *loss* diperkaya: selain entropi silang biner per piksel, ditambahkan hukuman khusus pada pita sekitar kontur objek dan hukuman terpisah untuk wilayah latar-depan dan latar-belakang, sehingga prediksi memiliki tepi tajam sekaligus isi objek yang konsisten.

## Cara Kerja Langkah demi Langkah

### Struktur Dua Aliran dan Lapisan Transpor

Jaringan terdiri atas dua aliran *encoder* dengan arsitektur identik — VGG-16, VGG-19, atau ResNet-50 yang dipraregistrasi pada ImageNet — satu untuk citra RGB dan satu untuk peta kedalaman; karena kedalaman berkanal tunggal, lapisan masukan aliran kedalaman diubah menjadi satu kanal dan diinisialisasi acak. Setiap *encoder* menghasilkan lima tingkat fitur (f1 sampai f5, dari resolusi besar ke kecil). Hanya tiga tingkat terdalam (f3, f4, f5) yang dipakai, karena fitur yang lebih dangkal beresolusi besar sehingga mahal dihitung dan lebih banyak mengandung derau.

Pada setiap tingkat, fitur RGB dan fitur kedalaman digabungkan oleh lapisan transpor yang dibangun sebagai *dense block* (blok terhubung rapat: setiap lapisan menerima keluaran semua lapisan sebelumnya, pola yang dipopulerkan DenseNet). Hasilnya adalah fitur campuran yang memuat struktur spasial dari kedalaman sekaligus detail penampakan dari RGB.

### Modul Piramida Dilasi Dinamis (DDPM)

Fitur campuran masuk ke *dynamic dilated pyramid module* (DDPM), yang memiliki dua masukan: fitur campuran dan fitur RGB dari sisi *decoder*. Di dalam DDPM bekerja dua submodul. Pertama, *kernel generation unit* (KGU) — sebuah blok terhubung rapat berisi empat lapisan — mengubah fitur campuran menjadi tensor bobot yang independen untuk setiap posisi peta fitur. Kedua, *kernel transformation unit* (KTU) menyusun ulang tensor bobot tersebut dan menyisipkan sejumlah nol di antara elemennya, sehingga terbentuk kernel konvolusi reguler berukuran 3×3 dengan laju dilasi 1, 3, dan 5. Dilasi adalah jarak antar-elemen kernel; dengan dilasi 1, 3, dan 5, kernel 3×3 mencakup wilayah efektif 3×3, 7×7, dan 11×11 piksel, sehingga tiga skala konteks diperoleh tanpa menambah jumlah bobot per posisi.

Sebelum disaring, fitur *decoder* direduksi kanalnya dari 64 menjadi 16 dengan konvolusi 1×1, lalu disaring oleh ketiga kernel dinamis secara *channel-wise* — setiap kanal dikonvolusi terpisah, mirip konvolusi *depth-wise separable*, tetapi dengan bobot yang berbeda pada setiap posisi spasial. Ketiga hasil cabang kemudian dikonkatenasi bersama fitur *decoder* tereduksi dan dilebur oleh konvolusi 3×3. Fitur hasil DDPM pada ketiga tingkat digabungkan ke jalur *top-down decoder* melalui penjumlahan elemen-demi-elemen hingga resolusi penuh, menghasilkan peta saliency akhir.

Alur data jaringan dapat diringkas sebagai berikut:

```
citra RGB 320x320                  peta kedalaman 320x320
      |                                   |
      v                                   v
+-------------+                   +-------------+
| encoder RGB |                   |enc. kedalaman|   VGG-16/19 atau ResNet-50
|  f3  f4  f5 |                   |  f3  f4  f5  |   (dipakai 3 blok terdalam)
+--+--+--+----+                   +--+--+--+-----+
   |  |  |     lapisan transpor      |  |  |
   |  |  +------- (dense block) -----+  |  |
   |  |              |                  |  |
   v  v              v                  v  v
+-------------------------------------------------+
| DDPM, satu per tingkat (i = 3, 4, 5):           |
|   fitur campuran -> KGU -> KTU                  |
|     (kernel 3x3 dinamis, dilasi d = 1, 3, 5)    |
|   fitur decoder -> reduksi 64->16 kanal         |
|     -> konvolusi adaptif per posisi & per kanal |
|   3 cabang + fitur tereduksi -> concat -> 3x3   |
+------------------------+------------------------+
                         v
        penggabungan top-down (penjumlahan) -> peta saliency P
```

### Fungsi Hybrid Enhanced Loss (HEL)

Supervisi standar SOD adalah entropi silang biner (BCE), yang menghitung galat setiap piksel secara independen. HEL menambahkan dua komponen. *Edge enhanced loss* (EEL) membatasi galat pada pita sekitar kontur objek: lokasi pita diperoleh dari selisih peta kebenaran dengan hasil *average pooling* 5×5 atasnya, sehingga hanya piksel dekat batas objek yang dihukum. *Region enhanced loss* (REL) menghitung galat terpisah di wilayah latar-depan dan latar-belakang, masing-masing dinormalisasi terhadap jumlah pikselnya, sehingga objek kecil tidak tertutup dominasi latar. *Loss* total adalah jumlah ketiganya; kedua komponen baru hanya aktif saat pelatihan.

### Pelatihan

Model dilatih dengan pengoptimal SGD bermomentum 0,9, laju pembelajaran awal 5×10⁻³ dengan strategi peluruhan *poly* berfaktor 0,9, dan *weight decay* 5×10⁻⁴. Masukan diubah ukurannya menjadi 320×320 piksel, dilatih selama 30 epoch dengan *batch size* 4 pada satu GPU GTX 1080 Ti, dengan augmentasi pembalikan horizontal, rotasi acak, dan jitter warna.

## Eksperimen dan Hasil

Evaluasi dilakukan pada delapan dataset RGB-D SOD: LFSD (100 citra), NJUD (1.985), NLPR (1.000), RGBD135 (135), SIP (1.000), SSD (80), STEREO (1.000), dan DUT-RGBD (1.200). Untuk tujuh dataset pertama, pelatihan memakai 1.485 sampel NJUD dan 700 sampel NLPR; untuk DUT-RGBD dipakai pembagian 800 latih dan 400 uji. Enam metrik dipakai: kurva *precision-recall*, F-measure maksimum dan adaptif (rata-rata harmonik berbobot presisi-recall), F-measure berbobot, S-measure (kemiripan struktural antara peta prediksi dan kebenaran), E-measure (keselarasan lokal-global), serta MAE.

Hasil utama versi VGG-16 antara lain: pada NJUD, F-measure maksimum 0,924 dan MAE 0,037 — lebih baik dari DMRA (0,896; 0,051) dan D3Net (0,903; 0,051), sehingga galat piksel turun sekitar 27% relatif terhadap keduanya. Pada NLPR dicapai F-measure maksimum 0,934 dengan MAE 0,020; pada STEREO 0,926 dengan MAE 0,040; pada DUT-RGBD 0,914 dengan MAE 0,041. Keseluruhan, metode ini unggul atas dua belas pembanding pada delapan dataset dan enam metrik. Kecepatan inferensinya 52 FPS dengan ukuran model sekitar 170 MB, yang pada 2020 tergolong ringkas dibanding metode atensi sezaman.

Studi ablasi (rata-rata berbobot seluruh dataset, VGG-16) menunjukkan kontribusi tiap komponen. Garis dasar *encoder-decoder* dengan fusi statis mencapai F-measure maksimum 0,875 dan MAE 0,067; menambahkan lapisan transpor dan DDPM menaikkannya menjadi 0,904 dan 0,052; menambahkan HEL menjadi 0,914 dan 0,041. Penyaringan dinamis menyumbang kenaikan terbesar, dan supervisi tepi-region menambah penurunan MAE sekitar 21% relatif. DDPM juga dibandingkan dengan modul penyaring dinamis DCM dari literatur segmentasi semantik: DDPM unggul dengan perbaikan relatif 5,60% pada F-measure berbobot dan 18,07% pada MAE, bukti bahwa kernel spesifik-posisi lebih efektif daripada kernel yang hanya spesifik-citra. Sebagai uji generalitas, HEL dipakai ulang untuk melatih empat model SOD RGB murni (R3Net, CPD, PoolNet, GCPANet); keempatnya membaik, misalnya PoolNet naik dari 0,832 menjadi 0,861 pada F-measure maksimum dengan MAE turun dari 0,060 menjadi 0,046.

## Kelebihan dan Keterbatasan

Kelebihan utama HDFNet adalah fusi lintas-modal yang adaptif: bobot pemrosesan ditentukan oleh isi masukan dan berbeda pada setiap posisi, sehingga gangguan pada peta kedalaman yang berderau dapat ditekan secara lokal — penulis makalah menunjukkan secara visual bahwa derau kedalaman yang mengacaukan prediksi garis dasar tersupresi oleh panduan DDPM. Piramida dilasi memberi konteks multi-skala tanpa menambah bobot per posisi, dan HEL memperbaiki kualitas tepi tanpa biaya inferensi. Kombinasi akurasi tertinggi, 52 FPS, dan model 170 MB menjadikannya titik referensi kuat pada masanya.

Keterbatasannya, pertama, struktur dua aliran menggandakan biaya *encoder*. Kedua, dari sisi rekayasa, pembangkitan kernel dinamis per posisi menambah jejak memori yang tumbuh seiring resolusi peta fitur; makalah hanya mengevaluasi masukan 320×320, dan skalabilitasnya ke resolusi tinggi tidak dibahas. Ketiga, secara konseptual, kualitas panduan tetap bergantung pada mutu peta kedalaman: eksperimen menunjukkan ketahanan terhadap derau ringan, tetapi perilaku model pada kedalaman yang sangat rusak tidak diuji. Keempat, seluruh arsitektur berbasis konvolusi lokal; mekanisme atensi global yang kemudian dipopulerkan Transformer belum dimanfaatkan.

## Kaitan dengan Bab Lain

HDFNet berada satu generasi setelah gelombang pertama metode RGB-D SOD berbasis CNN dalam tinjauan ini. Ia mewarisi persoalan yang dibuka DMRA (bab 035) — bagaimana memakai kedalaman tanpa tertipu kualitasnya — tetapi menjawabnya dengan cara berbeda: bukan atensi pada fitur, melainkan pembangkitan bobot konvolusi. Dalam tabel perbandingannya, HDFNet diuji langsung terhadap D3Net (bab 037) dan mengunggulinya pada NJUD maupun NLPR, sehingga kedua bab paling baik dibaca berdampingan sebagai dua strategi fusi yang bersaing pada tahun yang sama. Perbandingan sezaman lain yang relevan adalah BBS-Net (bab 036), JL-DCF (bab 038), dan S2MA (bab 039), yang sama-sama mengevaluasi pada NJUD dan NLPR; perbedaan angka S-measure dan MAE antar-bab tersebut memberi gambaran evolusi fusi RGB-D sebelum era Transformer yang diwakili VST (bab 042).

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)

## Poin untuk Sitasi

Kunci BibTeX: `pang2020hdfnet`.

Ringkasan yang aman dikutip: Pang dkk. (ECCV 2020) mengusulkan HDFNet untuk RGB-D SOD, yang membangkitkan kernel konvolusi dinamis multi-skala dari fitur campuran RGB dan kedalaman melalui *dynamic dilated pyramid module* untuk memandu *decoder* RGB pada tiga tingkat fitur, disertai *hybrid enhanced loss* yang memberi supervisi pada tepi dan wilayah objek. Metode ini melaporkan hasil terbaik atas dua belas pembanding pada delapan dataset dan enam metrik, dengan kecepatan 52 FPS pada GTX 1080 Ti.

Catatan verifikasi: seluruh angka hasil, ukuran dataset, hiperparameter, dan angka ablasi diambil dari naskah arXiv v3 (2007.06227); sebelum sitasi formal, cocokkan kembali dengan versi prosiding ECCV resmi (LNCS, hlm. 235–252).
