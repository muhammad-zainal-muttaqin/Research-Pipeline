# 111 - Visual SLAM in Human Populated Environments: Exploring the Trade-off Between Accuracy and Speed of YOLO and Mask R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `soares2019visualslam` |
| Judul asli | Visual SLAM in Human Populated Environments: Exploring the Trade-off Between Accuracy and Speed of YOLO and Mask R-CNN |
| Penulis | João Carlos Virgolino Soares, Marcelo Gattass, Marco Antonio Meggiolaro |
| Tahun | 2019 |
| Venue | 19th International Conference on Advanced Robotics (ICAR 2019), Belo Horizonte, hlm. 135–140 |
| Tema | RGB-D SLAM |

## Tautan Akses
- **DOI (IEEE Xplore):** https://doi.org/10.1109/ICAR46387.2019.8981617
- **PDF penulis (Lab. Robótica PUC-Rio):** http://meggi.usuarios.rdc.puc-rio.br/paper/C264_ICAR19_Visual_SLAM_in_human_populated_environments.pdf
- **Google Scholar:** https://scholar.google.com/scholar?q=Visual%20SLAM%20in%20Human%20Populated%20Environments%3A%20Exploring%20the%20Trade-off%20Between%20Accuracy%20and%20Speed%20of%20YOLO%20and%20Mask%20R-CNN
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Visual%20SLAM%20in%20Human%20Populated%20Environments%3A%20Exploring%20the%20Trade-off%20Between%20Accuracy%20and%20Speed%20of%20YOLO%20and%20Mask%20R-CNN&sort=relevance

## Gambaran Umum

Makalah ini menguji satu pertanyaan praktis pada *SLAM* visual (*Simultaneous Localization and Mapping* — pembentukan peta lingkungan sekaligus estimasi posisi kamera secara bersamaan) di ruang berpenghuni manusia: ketika titik fitur pada tubuh manusia yang bergerak harus disingkirkan agar tidak merusak estimasi lintasan kamera, apakah menyingkirkannya cukup dengan kotak pembatas (*bounding box*) hasil detektor objek seperti YOLO, atau perlu batas piksel presisi hasil segmentasi instans seperti Mask R-CNN? Soares, Gattass, dan Meggiolaro menyisipkan kedua detektor secara bergantian sebagai modul penyaring objek dinamis di depan sistem ORB-SLAM2, lalu membandingkan akurasi lintasan dan kecepatan pemrosesan dari kedua konfigurasi pada data RGB-D berisi orang bergerak.

Temuan utamanya bersifat kualitatif namun konsisten dengan intuisi rekayasa: kotak pembatas YOLO jauh lebih murah dihitung karena hanya satu tahap regresi (bab 001), tetapi kotak persegi selalu lebih luas daripada siluet tubuh sesungguhnya sehingga ikut membuang titik fitur latar belakang yang sebenarnya statis dan berguna. Mask R-CNN (bab 017) memberi batas mengikuti bentuk tubuh secara presisi, tetapi tahap pengusulan wilayah dan cabang mask tambahan membuatnya jauh lebih lambat. Makalah ini menjadi rujukan langsung bagi keputusan desain penulis yang sama pada sistem lanjutan mereka, Crowd-SLAM (2021), yang akhirnya memilih jalur deteksi kotak demi kecepatan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sistem SLAM visual klasik, termasuk ORB-SLAM2 (bab 107), dibangun dengan asumsi lingkungan statis: setiap titik fitur yang cocok antar-*frame* (bingkai citra berurutan) dianggap menandai objek diam, sehingga pergeserannya di citra murni disebabkan gerakan kamera. Asumsi ini valid untuk gedung kosong, tetapi gagal begitu ada manusia berjalan di depan kamera — titik fitur pada tubuh orang tersebut ikut dipakai untuk menghitung pose kamera seolah-olah statis, padahal pergerakannya berasal dari objek itu sendiri. Akibatnya lintasan kamera yang diestimasi menyimpang (*drift*) dari lintasan sebenarnya, dan pada kasus buruk pelacakan bisa gagal total.

Dua solusi sebelumnya menempuh jalur berbeda. DynaSLAM (bab 108) memakai Mask R-CNN untuk menandai piksel objek yang berpotensi bergerak (misalnya orang, mobil) secara presisi piksel demi piksel, dikombinasikan dengan pemeriksaan geometri multi-tampak (*multi-view geometry*) untuk menangkap objek dinamis yang tidak dikenali kelasnya oleh jaringan segmentasi. DS-SLAM (bab 109) memakai jaringan segmentasi semantik SegNet yang lebih ringan dipadukan dengan pemeriksaan batasan epipolar (*epipolar constraint* — aturan geometri yang menghubungkan posisi titik yang sama pada dua citra dari sudut pandang berbeda). Kedua pendekatan itu berangkat dari anggapan bahwa segmentasi piksel diperlukan agar penyaringan objek dinamis akurat, tetapi tidak ada dari keduanya yang secara langsung mengukur berapa besar akurasi yang sesungguhnya hilang bila segmentasi piksel diganti detektor kotak yang jauh lebih murah. Pertanyaan itulah yang secara spesifik diisi oleh makalah Soares dkk.: seberapa mahal harga yang dibayar segi akurasi bila memilih kecepatan.

## Ide Utama

Gagasan intinya adalah memperlakukan pemilihan detektor sebagai satu variabel eksperimen tunggal dalam pipeline SLAM yang sama, dengan segala komponen lain dijaga tetap. Baik YOLO maupun Mask R-CNN disisipkan pada posisi yang identik: sebagai modul penyaring yang berjalan pada setiap *frame* RGB sebelum ekstraksi fitur, bertugas menandai wilayah citra yang termasuk kelas "orang". Titik fitur ORB (fitur citra cepat yang tahan rotasi, dipakai ORB-SLAM2 untuk pencocokan antar-*frame*) yang jatuh pada wilayah bertanda itu dibuang sebelum dipakai mengestimasi pose kamera dan membangun peta.

Perbedaan hanya terletak pada bentuk wilayah yang ditandai. YOLO menghasilkan kotak pembatas persegi yang membungkus seluruh tubuh orang; seluruh titik fitur di dalam kotak itu — termasuk yang sebenarnya berada di latar belakang di sela-sela tubuh atau di tepi kotak — ikut terbuang. Mask R-CNN menghasilkan mask biner mengikuti kontur tubuh; hanya titik fitur yang benar-benar jatuh pada piksel tubuh yang terbuang, sementara titik latar di sekitar orang tetap dipertahankan untuk estimasi pose. Dengan kerangka pembanding ini, selisih akurasi dan kecepatan antara dua konfigurasi bisa dikaitkan langsung pada satu sebab: kekasaran wilayah penyaringan.

## Cara Kerja Langkah demi Langkah

### Kerangka dasar: ORB-SLAM2 dengan modul penyaring dinamis

ORB-SLAM2 berjalan sebagai tiga proses paralel: pelacakan (mencocokkan fitur *frame* saat ini dengan peta yang sudah ada untuk menghitung pose), pemetaan lokal (menambah dan menghaluskan titik peta baru), dan penutupan *loop* (mengenali kembali tempat yang sudah pernah dilalui untuk mengoreksi akumulasi galat). Makalah ini tidak mengubah ketiga proses tersebut; modul deteksi disisipkan sebagai tahap tambahan tepat sebelum ekstraksi fitur ORB pada tahap pelacakan, sehingga titik fitur yang berasal dari wilayah dinamis tidak pernah masuk ke perhitungan pose maupun ke peta.

Alur kerja dua konfigurasi yang dibandingkan:

```
citra RGB masuk setiap frame
            |
      ------+------
      |           |
      v           v
  YOLO(1 tahap   Mask R-CNN(2 tahap:
  regresi,       usul wilayah + cabang
  bab 001)       mask piksel, bab 017)
      |           |
      v           v
  kotak persegi   mask mengikuti
  "orang"         siluet "orang"
      |           |
      v           v
  buang titik ORB  buang titik ORB
  di DALAM KOTAK    HANYA pada piksel
  (ikut sebagian    bertanda "orang"
  latar di tepi)    (latar tetap)
      |           |
      ------+------
            v
   titik fitur statis tersisa
            |
            v
   ORB-SLAM2: pelacakan, pemetaan
   lokal, penutupan loop
```

Diagram di atas menunjukkan bahwa satu-satunya cabang yang berbeda antara dua konfigurasi adalah bentuk wilayah yang dipakai untuk membuang titik fitur; seluruh tahap sesudahnya identik.

### Konsekuensi bentuk wilayah terhadap kecepatan dan jumlah fitur

Karena YOLO memprediksi kotak dan kelas dalam satu kali evaluasi jaringan konvolusi (mekanisme regresi tunggal yang dijelaskan pada bab 001), waktu komputasinya per *frame* jauh lebih singkat dibanding Mask R-CNN, yang harus terlebih dahulu mengusulkan wilayah kandidat lalu menjalankan cabang konvolusi tambahan untuk menghasilkan mask piksel (bab 017). Selisih tahap inilah yang membuat konfigurasi berbasis YOLO dapat berjalan pada laju *frame* jauh lebih tinggi daripada konfigurasi berbasis Mask R-CNN.

Sebagai konsekuensi di sisi lain, kotak pembatas menyingkirkan lebih banyak titik fitur daripada yang seharusnya perlu disingkirkan. Pada citra dengan satu orang berdiri menyamping, misalnya, kotak pembatas mencakup ruang kosong di antara lengan dan badan serta celah di sekitar kaki — seluruh titik fitur latar pada celah itu ikut terbuang meski sesungguhnya statis dan berguna untuk estimasi pose. Semakin besar dan semakin banyak orang dalam bidang pandang kamera, semakin banyak pula titik statis yang tersingkir secara tidak perlu akibat bentuk kotak, sehingga jumlah titik fitur yang tersisa untuk pelacakan berkurang lebih tajam dibanding bila memakai mask presisi Mask R-CNN.

### Evaluasi lintasan

Akurasi kedua konfigurasi diukur dengan *ATE* (*Absolute Trajectory Error* — galat lintasan absolut, yaitu selisih rata-rata antara lintasan kamera yang diestimasi dan lintasan kebenaran dasar dari sistem penangkap gerak eksternal). Pengukuran ini dilakukan pada data RGB-D dari benchmark TUM RGB-D yang memuat rekaman orang bergerak di ruang dalam, benchmark yang sama juga dipakai DynaSLAM dan DS-SLAM sehingga hasilnya dapat dibandingkan silang dengan sistem sejenis.

## Eksperimen dan Hasil

Pengujian dilakukan dengan menjalankan pipeline ORB-SLAM2 yang sama dua kali pada rangkaian citra RGB-D berisi orang bergerak — sekali dengan modul penyaring YOLO, sekali dengan modul penyaring Mask R-CNN — lalu membandingkan ATE dan laju pemrosesan (*frame rate*) antara kedua jalannya. Pembandingnya adalah performa masing-masing konfigurasi terhadap dirinya sendiri pada data yang identik, bukan terhadap sistem eksternal lain di luar dua detektor tersebut.

Pola hasil yang dilaporkan konsisten dengan mekanisme yang diuraikan di atas: konfigurasi Mask R-CNN mencapai galat lintasan yang lebih rendah karena penyaringan titik fitur lebih tepat sasaran, sedangkan konfigurasi YOLO berjalan pada laju *frame* yang jauh lebih tinggi dan mendekati kebutuhan waktu-nyata (*real-time*) untuk robot bergerak, dengan galat lintasan yang sedikit lebih tinggi akibat titik statis yang ikut terbuang oleh kotak. Kesimpulan yang ditarik penulis: bagi aplikasi yang menuntut kecepatan, penurunan akurasi dari beralih ke kotak pembatas relatif kecil dibanding perolehan kecepatannya, sehingga deteksi objek merupakan kompromi yang masuk akal untuk SLAM waktu-nyata di lingkungan berpenghuni. Angka tepat ATE dan laju *frame* untuk masing-masing konfigurasi, serta daftar persis urutan TUM RGB-D yang diuji, tidak berhasil diverifikasi dari salinan naskah yang dapat diakses untuk penulisan bab ini dan perlu dicocokkan langsung ke tabel hasil pada naskah asli sebelum dikutip sebagai angka pasti.

Temuan ini kemudian tampak berlanjut pada keputusan desain penulis yang sama di sistem lanjutan mereka, Crowd-SLAM (2021): sistem tersebut memilih jalur deteksi objek berbasis YOLO, bukan segmentasi instans, sebagai penyaring dinamis utama, dengan menambahkan aturan tambahan untuk memperkecil wilayah kotak agar kerugian titik fitur latar berkurang.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah desain perbandingannya yang terkendali: dengan menjaga seluruh komponen SLAM tetap dan hanya menukar detektor, selisih akurasi dan kecepatan yang teramati dapat dikaitkan langsung pada satu sebab, yaitu kekasaran wilayah penyaringan kotak versus mask. Hasil ini memberi panduan rekayasa yang konkret bagi perancang sistem robot: bila sumber daya komputasi terbatas dan target adalah waktu-nyata, kompromi ke arah deteksi kotak beralasan; bila akurasi peta menjadi prioritas dan komputasi tersedia lebih longgar, segmentasi instans lebih unggul.

Dari sisi rekayasa, cakupan pengujian terbatas pada satu kelas objek dinamis, yaitu manusia, sehingga kesimpulan tentang kotak versus mask belum tentu berlaku sama untuk objek dinamis berbentuk lain seperti kendaraan atau hewan yang rasio luas kotak terhadap luas siluetnya bisa sangat berbeda dari manusia berdiri. Secara konseptual, perbandingan ini juga terikat pada generasi detektor tahun 2019; kesenjangan kecepatan antara detektor satu tahap dan detektor segmentasi dua tahap terus berubah seiring versi-versi YOLO maupun varian Mask R-CNN yang lebih baru, sehingga besaran selisih kecepatan yang diamati pada makalah ini tidak otomatis berlaku pada pasangan detektor versi terkini. Sebagai makalah konferensi pendek, ruang untuk ablasi tambahan — misalnya menguji beberapa ukuran kotak yang diperkecil secara heuristik — kemungkinan terbatas, dan hal ini sejalan dengan langkah lanjutan penulis sendiri pada Crowd-SLAM yang menambahkan penyesuaian kotak tersebut.

## Kaitan dengan Bab Lain

Bab ini berdiri di atas kerangka ORB-SLAM2 yang diuraikan pada [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md), dan secara langsung membandingkan dua filosofi detektor yang masing-masing dibahas mendalam pada [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) dan [017 - 2017 - Mask R-CNN - Fondasi RGB](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md). Dalam klaster RGB-D SLAM, temuannya melengkapi dua pendekatan penyaringan dinamis yang lebih dahulu ada: [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md), yang memakai Mask R-CNN dipadu geometri multi-tampak, dan [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md), yang memakai segmentasi semantik SegNet dipadu batasan epipolar. Kesimpulan bab ini — bahwa deteksi kotak menawarkan kompromi kecepatan yang wajar dengan kerugian akurasi terbatas — sejalan dengan arah desain sistem CFP-SLAM pada [110 - 2022 - CFP-SLAM - RGB-D SLAM](./110%20-%202022%20-%20CFP-SLAM%20-%20RGB-D%20SLAM.md) dan menjadi dasar langsung bagi keputusan penulis yang sama untuk memilih deteksi objek pada sistem lanjutan mereka, Crowd-SLAM (2021).

## Poin untuk Sitasi

Kutip dengan kunci `soares2019visualslam`. Ringkasan yang aman dikutip: "Soares, Gattass, dan Meggiolaro (ICAR 2019) menyisipkan YOLO dan Mask R-CNN secara bergantian sebagai penyaring objek dinamis pada ORB-SLAM2, dan menunjukkan bahwa deteksi kotak pembatas berjalan jauh lebih cepat dengan kerugian akurasi lintasan yang relatif kecil dibanding segmentasi instans piksel presisi." Identitas makalah (penulis, tahun, venue, DOI 10.1109/ICAR46387.2019.8981617, halaman 135–140), kerangka ORB-SLAM2, penggunaan benchmark TUM RGB-D, dan metrik ATE telah dikonfirmasi lewat sumber sekunder yang merujuk makalah ini. Angka pasti ATE dan laju *frame* untuk setiap konfigurasi, serta daftar persis urutan TUM RGB-D yang diuji, tidak berhasil diverifikasi dari salinan naskah yang dapat diakses saat penulisan bab ini — wajib dicocokkan ke tabel hasil pada naskah asli (via DOI IEEE Xplore atau PDF penulis di atas) sebelum dikutip sebagai angka pasti dalam karya formal.
