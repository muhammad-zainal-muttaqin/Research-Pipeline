# 101 - Illumination-Aware Faster R-CNN for Robust Multispectral Pedestrian Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2019illumination` |
| Judul asli | Illumination-aware Faster R-CNN for Robust Multispectral Pedestrian Detection |
| Penulis | Chengyang Li, Dan Song, Ruofeng Tong, Min Tang |
| Tahun | 2019 (jurnal); pracetak arXiv 2018 |
| Venue | Pattern Recognition, vol. 85, hlm. 161–171 |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **arXiv (pracetak gratis):** https://arxiv.org/abs/1803.05347
- **DOI (Pattern Recognition):** https://doi.org/10.1016/j.patcog.2018.08.005
- **Kode sumber (GitHub):** https://github.com/Li-Chengyang/IAF-RCNN

## Gambaran Umum

Makalah ini memperkenalkan IAF R-CNN (*Illumination-Aware Faster R-CNN*), detektor pejalan kaki multispektral yang menggabungkan citra warna (RGB) dan citra termal (inframerah panjang) dengan bobot fusi yang berubah menurut kondisi cahaya. Alih-alih memakai bobot fusi tetap, model ini menyisipkan jaringan kecil yang menaksir tingkat iluminasi citra, lalu memakai taksiran itu untuk menimbang seberapa besar kontribusi cabang RGB dibandingkan cabang termal pada tiap prediksi. Seluruh sistem dibangun di atas Faster R-CNN (bab 014), sehingga usulan wilayah objek dihasilkan oleh jaringan itu sendiri, bukan oleh algoritme eksternal seperti *Aggregated Channel Features* (ACF) yang dipakai metode-metode multispektral sebelumnya.

Pada tolok ukur KAIST Multispectral Pedestrian (bab 100), IAF R-CNN mencapai *miss rate* (tingkat kegagalan deteksi, semakin rendah semakin baik) 15,73% untuk seluruh data uji, dibandingkan 34,62% bila hanya memakai cabang RGB dan 22,71% bila hanya memakai cabang termal. Angka ini juga lebih rendah daripada metode fusi sebelumnya seperti *Halfway Fusion* (18,59%) dan *Fusion RPN+BF* (16,53%). Kontribusi utama makalah bukan sekadar menggabungkan dua modal, melainkan membuat bobot penggabungan itu bergantung pada estimasi cahaya per citra, yang terbukti lebih baik daripada bobot rata-rata tetap maupun aturan sederhana siang/malam.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi pejalan kaki untuk kendaraan otonom dan sistem pengawasan harus tetap andal pada malam hari, saat citra RGB kehilangan banyak informasi karena minimnya cahaya tampak. Kamera termal mengukur radiasi inframerah panjang yang dipancarkan tubuh manusia sehingga tetap kontras pada kegelapan, tetapi citra termal miskin tekstur dan warna sehingga sering gagal membedakan pejalan dari benda panas lain (misalnya knalpot kendaraan) pada siang hari. Dataset KAIST Multispectral Pedestrian (bab 100) menyediakan pasangan citra RGB-termal yang selaras spasial dan waktu, menjadikan riset fusi dua modal ini mungkin dilakukan secara sistematis.

Sebelum makalah ini, pendekatan fusi yang populer — misalnya *Halfway Fusion* yang diusulkan Liu dkk. (2016) — menetapkan satu arsitektur penggabungan tunggal yang dipakai sama untuk seluruh citra, tanpa mempertimbangkan apakah citra itu diambil siang atau malam. Pendekatan yang lebih tua, ACF+T+THOG, memakai fitur tangan (*handcrafted feature*) seperti *Aggregated Channel Features* dan *Thermal Histogram of Oriented Gradients* yang juga tidak menyesuaikan bobot modal terhadap kondisi cahaya. Padahal, keandalan RGB dan termal bersifat komplementer secara terbalik: RGB unggul saat cahaya cukup, termal unggul saat gelap. Fusi statis memaksa satu bobot untuk kedua situasi tersebut, sehingga performa tertekan pada salah satu kondisi. Masalah inilah yang mendorong penulis mengukur iluminasi secara eksplisit dan menjadikannya sinyal kontrol bobot fusi.

## Ide Utama

Gagasan inti makalah adalah mengukur kondisi cahaya sebuah citra sebagai satu nilai numerik, lalu memakai nilai itu untuk menimbang kontribusi cabang RGB dan cabang termal secara dinamis, per citra. Penulis menemukan bahwa skor keyakinan deteksi dari cabang RGB dan dari cabang termal berkorelasi dengan tingkat iluminasi: cabang RGB cenderung lebih dapat dipercaya saat siang, cabang termal cenderung lebih dapat dipercaya saat malam. Temuan korelasi ini dijadikan dasar rancangan: sebuah jaringan kecil bernama *Illumination-Aware Network* (IAN) dilatih untuk memprediksi nilai iluminasi dari citra RGB, dan nilai itu dilewatkan ke sebuah fungsi gerbang (*gate function*) yang menghasilkan bobot penggabungan. Dengan demikian, penggabungan RGB-termal bukan lagi keputusan arsitektur yang tetap, melainkan keluaran yang berubah mengikuti karakteristik tiap citra masukan.

## Cara Kerja Langkah demi Langkah

### Kerangka Deteksi Dua Cabang Berbasis Faster R-CNN

IAF R-CNN memakai dua jaringan VGG-16 (arsitektur konvolusi 16 lapis berbobot) sebagai penyari fitur, satu menerima citra RGB dan satu menerima citra termal. Berbeda dari metode fusi multispektral sebelumnya yang mengambil usulan wilayah objek dari algoritme eksternal ACF, sistem ini memakai *Region Proposal Network* (RPN) — komponen Faster R-CNN yang menghasilkan kandidat kotak objek langsung dari peta fitur konvolusi — sehingga seluruh pipeline dapat dilatih *end-to-end* (dari masukan citra ke keluaran deteksi tanpa tahap eksternal terpisah). Fitur dari kedua modal digabungkan pada satu titik dalam jaringan, kemudian dilewatkan ke lapis *Region of Interest* (ROI) *pooling* yang menyeragamkan ukuran fitur tiap kandidat kotak sebelum diklasifikasikan dan diregresikan posisinya.

### Enam Arsitektur Fusi yang Dibandingkan

Sebelum menetapkan rancangan akhir, penulis membandingkan enam titik penggabungan fitur RGB-termal: *Input Fusion* (penggabungan pada tingkat piksel masukan), *Early Fusion* (segera setelah beberapa lapis konvolusi awal), *Halfway Fusion* (di tengah jaringan, sebelum RPN), *Late Fusion* (mendekati lapis akhir), serta dua varian *Score Fusion* yang menggabungkan hasil dua RPN atau dua kepala deteksi terpisah pada tingkat skor keluaran. Dari perbandingan ini, *Halfway Fusion* dan *Score Fusion* varian pertama memberi *miss rate* terbaik, berkisar 17,4–17,6%, sehingga keduanya dijadikan dasar sebelum lapis penyadar-iluminasi ditambahkan.

### Jaringan Sadar-Iluminasi (Illumination-Aware Network)

IAN adalah jaringan konvolusi kecil — dua lapis konvolusi diikuti dua lapis terhubung penuh — yang menerima potongan citra RGB berukuran 56×56 piksel dan mengeluarkan satu nilai iluminasi iv dalam rentang [0, 1], dengan 0 berarti gelap (malam) dan 1 berarti terang (siang). Jaringan ini dilatih secara terawasi memakai label siang/malam yang tersedia pada metadata KAIST, sehingga tidak memerlukan anotasi tambahan. Pada pengujian ablasi, IAN yang dipelajari dari data terbukti lebih baik daripada ukuran iluminasi berbasis statistik piksel tangan (misalnya rata-rata dan rentang nilai kecerahan citra).

### Fungsi Gerbang Adaptif

Nilai iv dari IAN dilewatkan ke fungsi gerbang berbentuk sigmoid termodifikasi untuk menghasilkan bobot w yang menentukan porsi cabang RGB; cabang termal memperoleh bobot pelengkap (1 − w). Bobot ini diterapkan baik pada skor klasifikasi maupun pada keluaran regresi kotak pembatas dari kedua cabang, sehingga hasil akhir merupakan kombinasi berbobot dari kedua modal, bukan pilihan salah satu. Parameter kemiringan fungsi gerbang dipelajari selama pelatihan bersama seluruh jaringan.

Diagram berikut meringkas alur data dari dua citra masukan hingga deteksi akhir:

```
citra RGB ──> VGG-16 (RGB) ──> RPN/ROI ──> skor & kotak (RGB)
                                                    │
citra RGB (56x56) ──> IAN ──> iv ──> gerbang ──> w, (1-w)
                                                    │
citra termal ──> VGG-16 (termal) ──> RPN/ROI ──> skor & kotak (termal)
                                                    │
                              w x (RGB) + (1-w) x (termal)
                                                    │
                                          deteksi akhir + NMS
```

Pada malam hari, iv mendekati 0 sehingga bobot cabang termal mendominasi; pada siang hari, iv mendekati 1 sehingga bobot cabang RGB mendominasi. Pengujian ablasi menunjukkan gerbang yang dipelajari ini unggul 0,67 poin *miss rate* dibandingkan penggabungan rata-rata tetap, dan unggul 5,03 poin dibandingkan aturan keras beralih siang/malam (memilih satu cabang penuh berdasarkan ambang waktu).

### Fungsi Loss Multi-Tugas

Pelatihan menggabungkan beberapa komponen loss sekaligus: loss RPN untuk kualitas usulan wilayah, loss klasifikasi dan regresi kotak untuk masing-masing cabang modal, serta dua loss tambahan berupa segmentasi semantik pejalan — satu pada tingkat citra penuh dan satu pada tingkat ROI — yang berfungsi sebagai sinyal pelatihan tambahan (*auxiliary supervision*) agar fitur yang dipelajari lebih peka terhadap bentuk manusia. Seluruh komponen loss diberi bobot yang sama pada penjumlahannya.

### Penyesuaian Rekayasa untuk Data Multispektral

Selain gerbang iluminasi, penulis melaporkan tiga penyesuaian teknis terhadap kerangka Faster R-CNN standar agar cocok untuk pejalan kaki berukuran kecil pada KAIST: memperhalus *stride* fitur konvolusi menjadi 8 piksel (dari baku 16 piksel) agar objek kecil tidak hilang pada peta fitur, menyertakan instans pejalan yang tertutup sebagian (bukan membuangnya dari data latih), dan mengabaikan wilayah citra yang taksamar saat menghitung loss alih-alih memperlakukannya sebagai latar. Ketiga penyesuaian ini bersama-sama dilaporkan menurunkan *miss rate* sekitar 10,4 poin dibandingkan penerapan Faster R-CNN standar tanpa penyesuaian, sebelum gerbang iluminasi ditambahkan.

## Eksperimen dan Hasil

Evaluasi dilakukan pada KAIST Multispectral Pedestrian Benchmark (bab 100), yang memuat sekitar 95.328 pasang citra RGB-termal selaras dengan 103.128 kotak pejalan berlabel. Data uji terdiri atas 2.252 citra, dipecah menjadi 1.455 citra siang dan 797 citra malam. Metrik yang dipakai adalah *log-average miss rate* (MR) pada rentang *false positive per image* (FPPI) 10⁻² sampai 10⁰; semakin rendah nilainya, semakin sedikit pejalan yang terlewat pada tingkat kesalahan positif tertentu.

| Kondisi | RGB saja | Termal saja | IAF R-CNN |
|---|---|---|---|
| Semua data uji | 34,62% | 22,71% | 15,73% |
| Siang | 6,84% | 8,51% | 6,08% |
| Malam | 22,24% | 17,89% | 18,20% |

Pada keseluruhan data uji, fusi menekan *miss rate* menjadi kurang dari setengah performa cabang tunggal terbaik (22,71% menjadi 15,73%), yang menegaskan manfaat menggabungkan dua modal dengan bobot adaptif. Pada siang hari, hasil gabungan (6,08%) bahkan lebih baik daripada RGB saja (6,84%) maupun termal saja (8,51%), menunjukkan kedua modal saling melengkapi meski RGB dominan. Pada malam hari, hasil gabungan (18,20%) justru sedikit lebih buruk daripada termal saja (17,89%) — indikasi bahwa sinyal RGB yang nyaris tak berguna pada kegelapan total kadang tetap mengganggu keputusan gerbang alih-alih diabaikan sepenuhnya.

Dibandingkan metode sebelumnya, IAF R-CNN mengungguli ACF+T+THOG berbasis fitur tangan (25,94%), *Halfway Fusion* (18,59%), dan *Fusion RPN+BF* (16,53%), menjadikannya *miss rate* terendah di antara metode yang dibandingkan pada masa publikasinya. Dari sisi kecepatan, model ini memproses satu citra dalam 0,21 detik (kira-kira 4,8 *frame* per detik), tercepat di antara metode fusi multispektral yang dibandingkan, meski jauh dari kecepatan *real-time* detektor satu tahap seperti YOLO (bab 001).

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah pengalihan dari fusi statis ke fusi yang bergantung konteks: bobot RGB-termal berubah otomatis mengikuti iluminasi citra tanpa memerlukan label waktu saat inferensi, karena IAN menaksirnya langsung dari piksel. Kerangka Faster R-CNN yang dipakai juga menghapus ketergantungan pada usulan wilayah eksternal (ACF) yang membatasi metode-metode fusi sebelumnya, sehingga seluruh sistem dapat dioptimalkan menyeluruh. Perbandingan sistematis enam arsitektur fusi juga memberi dasar empiris yang jelas atas pilihan titik penggabungan fitur.

Dari sisi rekayasa, dua keterbatasan menonjol. Pertama, hasil malam hari yang sedikit lebih buruk daripada cabang termal tunggal menunjukkan gerbang belum sepenuhnya optimal pada kondisi cahaya ekstrem; nilai iluminasi mendekati nol seharusnya menekan kontribusi RGB nyaris habis, tetapi kenyataannya sedikit kontribusi itu masih merugikan. Kedua, arsitektur dua tahap (RPN lalu klasifikasi ROI) pada dua cabang jaringan membuat kecepatan inferensi (0,21 detik per citra) masih jauh dari kebutuhan aplikasi kendaraan otonom yang menuntut puluhan *frame* per detik. Secara konseptual, IAN dilatih hanya dengan label biner siang/malam, sehingga generalisasinya terhadap kondisi transisi seperti senja, fajar, atau pencahayaan buatan di jalan pada malam hari belum diuji secara eksplisit dalam makalah.

## Kaitan dengan Bab Lain

IAF R-CNN mewarisi kerangka deteksi dua tahap dari Faster R-CNN ([014 - Faster R-CNN](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)), dengan menambahkan cabang termal dan mekanisme gerbang iluminasi di atasnya. Data dan protokol evaluasinya berasal langsung dari KAIST Multispectral Pedestrian ([100 - KAIST](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)), yang menjadi tolok ukur baku seluruh klaster Pedestrian RGB-T. Gagasan pembobotan modal berbasis konteks yang diperkenalkan di sini menjadi rujukan bagi metode fusi berikutnya dalam klaster yang sama: MBNet ([102 - MBNet](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)) menghaluskan penyelarasan spasial dua modal, sedangkan GAFF ([103 - GAFF](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md)) menggantikan gerbang skalar tunggal dengan mekanisme *attention* yang lebih halus per posisi dan per kanal fitur.

## Poin untuk Sitasi

Kutip dengan kunci `li2019illumination`. Ringkasan yang aman dikutip: "IAF R-CNN menaksir iluminasi citra melalui jaringan IAN, lalu memakai nilai itu untuk menimbang cabang RGB dan termal secara adaptif dalam kerangka Faster R-CNN, mencapai *miss rate* 15,73% pada KAIST Multispectral Pedestrian Benchmark — lebih rendah daripada RGB saja (34,62%), termal saja (22,71%), dan metode fusi sebelumnya seperti Halfway Fusion (18,59%)." Angka-angka berikut diringkas dari pembacaan versi HTML pracetak (ar5iv) dan sebaiknya diverifikasi ulang ke tabel PDF/jurnal asli sebelum dikutip formal: perbandingan enam arsitektur fusi (17,4–17,6%), delta ablasi gerbang (0,67 poin dan 5,03 poin), kontribusi 10,4 poin dari penyesuaian rekayasa (*stride* 8 piksel, instans tertutup sebagian, wilayah taksamar), angka pembanding Fusion RPN+BF (16,53%), serta kecepatan inferensi 0,21 detik per citra.
