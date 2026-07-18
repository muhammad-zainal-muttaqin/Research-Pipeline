# 108 - DynaSLAM: Tracking, Mapping, and Inpainting in Dynamic Scenes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bescos2018dynaslam` |
| Judul asli | DynaSLAM: Tracking, Mapping, and Inpainting in Dynamic Scenes |
| Penulis | Berta Bescos, José M. Fácil, Javier Civera, José Neira |
| Tahun | 2018 |
| Venue | IEEE Robotics and Automation Letters (RA-L), dipresentasikan di IEEE/RSJ IROS 2018 |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv:** https://arxiv.org/abs/1806.05620
- **DOI:** https://doi.org/10.1109/LRA.2018.2860039
- **Google Scholar:** https://scholar.google.com/scholar?q=DynaSLAM%3A%20Tracking%2C%20Mapping%2C%20and%20Inpainting%20in%20Dynamic%20Scenes

## Gambaran Umum

DynaSLAM memperluas ORB-SLAM2 — sistem *SLAM* (*Simultaneous Localization and Mapping*, pelokalan dan pemetaan serentak) berbasis fitur ORB yang dibahas pada bab 107 — agar tetap akurat pada lingkungan berisi objek yang bergerak. Sistem menambahkan dua tahap di depan jalur pelacakan dan pemetaan asli: deteksi konten dinamis, yang menggabungkan segmentasi semantik dari Mask R-CNN dengan pemeriksaan geometri multi-*view* (multi-sudut-pandang) berbasis kedalaman, dan pengisian latar (*background inpainting*) yang merekonstruksi bagian citra yang tertutup objek bergerak. DynaSLAM mendukung tiga konfigurasi kamera: monokular, stereo, dan RGB-D (warna dan kedalaman).

Pada sekuens paling dinamis dalam tolok ukur TUM RGB-D, yaitu *walking_xyz* (dua orang berjalan sementara kamera bergerak bebas pada tiga sumbu), galat trajektori absolut (ATE RMSE — *Absolute Trajectory Error*, *Root-Mean-Square*, ukuran rata-rata jarak antara lintasan kamera yang diestimasi dan lintasan sebenarnya) turun dari 0,459 m pada ORB-SLAM2 menjadi 0,015 m pada DynaSLAM, penurunan sekitar 96,7%. Selain pose kamera yang jauh lebih akurat, sistem ini menghasilkan keluaran tambahan berupa peta statis yang bersih dari objek bergerak, dicapai lewat penambalan latar.

## Latar Belakang: Masalah yang Ingin Dipecahkan

ORB-SLAM2 (bab 107) mengasumsikan *scene* (adegan/lingkungan yang direkam) bersifat kaku (*rigid*): seluruh titik fitur yang teramati dianggap diam terhadap dunia, sehingga posisi kamera dapat diestimasi dari pergeseran titik-titik itu antar-*frame*. Asumsi ini valid untuk ruangan kosong, tetapi gagal ketika ada objek yang benar-benar bergerak — orang berjalan, kendaraan melintas, kursi dipindahkan. Fitur yang menempel pada objek bergerak ikut berpindah karena gerakan objek itu sendiri, bukan karena gerakan kamera, sehingga mencemari perhitungan pose bila ikut disertakan.

Penanganan bawaan pada SLAM klasik hanya berupa penolakan pencilan (*outlier*) jangka pendek, misalnya lewat RANSAC (*Random Sample Consensus*, algoritme pemilihan subset data acak untuk mengestimasi model yang tahan pencilan). Mekanisme ini memadai bila objek dinamis kecil dan sesaat, tetapi rusak ketika objek dinamis menutupi porsi besar citra atau bergerak konsisten sepanjang banyak *frame* berurutan — persis situasi yang umum di kantor, rumah, atau jalan yang dilalui orang dan kendaraan. Karena robot layanan dan aplikasi realitas tertambah (*augmented reality*) umumnya beroperasi di lingkungan berpenghuni seperti itu, kegagalan pada *scene* dinamis membatasi penerapan SLAM klasik di luar laboratorium.

## Ide Utama

DynaSLAM mendeteksi konten dinamis lewat dua sinyal yang saling melengkapi, lalu membuang seluruh fitur yang jatuh pada area dinamis sebelum fitur itu dipakai untuk pelacakan pose maupun pembangunan peta. Sinyal pertama adalah prior semantik: sebuah jaringan segmentasi instans mengenali kelas objek yang *biasanya* dapat bergerak — misalnya orang atau sepeda — dari satu citra saja, tanpa perlu membandingkan dengan *frame* lain. Sinyal kedua adalah verifikasi geometris: posisi titik pada *frame* saat ini diproyeksikan dari beberapa *keyframe* (citra kunci yang disimpan sebagai rujukan) sebelumnya menggunakan data kedalaman; titik yang kedalamannya berubah signifikan dianggap benar-benar bergerak, terlepas dari kelas objeknya.

Kedua sinyal ini menutup kelemahan masing-masing. Prior semantik langsung mengenali orang yang berjalan sejak *frame* pertama tanpa menunggu riwayat gerak, tetapi tidak dapat mendeteksi objek yang secara kelas biasanya diam namun kebetulan sedang dipindahkan, misalnya buku atau kursi. Verifikasi geometris menangkap gerak objek jenis apa pun, tetapi memerlukan beberapa *keyframe* rujukan dengan tumpang tindih pandangan yang cukup, sehingga tidak dapat langsung menilai *frame* pertama sebuah urutan. Menggabungkan keduanya memberi cakupan deteksi yang lebih luas daripada memakai salah satunya saja.

## Cara Kerja Langkah demi Langkah

### Segmentasi Objek Berpotensi Dinamis dengan Mask R-CNN

Setiap *frame* RGB diproses oleh Mask R-CNN, jaringan segmentasi instans yang memperluas Faster R-CNN dengan cabang tambahan untuk memprediksi masker piksel per objek (dibahas lebih rinci pada bab 017). Implementasi yang dipakai dilatih pada dataset MS COCO dan difokuskan pada belasan kelas yang dianggap berpotensi bergerak, seperti orang, sepeda, mobil, sepeda motor, dan bus. Keluaran tahap ini adalah masker biner per piksel untuk objek-objek tersebut, disebut masker "dinamis apriori" karena hanya berdasarkan kelas objek, tanpa memeriksa apakah objek itu benar-benar sedang bergerak pada saat perekaman.

### Verifikasi Gerak Nyata dengan Geometri Multi-View

Untuk konfigurasi RGB-D, sistem lebih dulu memakai pelacakan berbiaya rendah (dijelaskan berikutnya) untuk memperoleh estimasi pose kasar pada *frame* saat ini. Titik-titik fitur dari beberapa *keyframe* sebelumnya — dipilih lima *keyframe* dengan tumpang tindih pandangan tertinggi terhadap *frame* saat ini — diproyeksikan ke citra saat ini memakai pose dan peta kedalaman yang tersedia. Kedalaman hasil proyeksi ini dibandingkan dengan kedalaman yang benar-benar terukur pada posisi tersebut; bila selisihnya (Δz) melewati ambang τz = 0,4 m, titik itu ditandai sebagai bergerak. Ambang ini ditentukan secara empiris dari anotasi manual pada sekumpulan citra contoh. Mekanisme ini menangkap objek yang secara kelas tidak masuk daftar Mask R-CNN, misalnya kursi yang dipindahkan seseorang.

### Menggabungkan Kedua Masker dan Membuang Fitur Dinamis

Masker dinamis akhir merupakan gabungan (union) dari masker Mask R-CNN dan masker geometri. Semua titik fitur ORB yang jatuh pada masker gabungan ini dikeluarkan sebelum tahap asosiasi fitur untuk pelacakan pose maupun sebelum titik itu dimasukkan ke peta. Dengan begitu, baik estimasi pose maupun peta 3D yang terbentuk hanya dibangun dari bagian *scene* yang diyakini statis.

Alur data dari citra masukan sampai peta statis dapat diringkas sebagai berikut.

```
citra RGB-D (frame ke-t)
        |
        v
  Mask R-CNN --------> masker dinamis apriori
        |                (orang, sepeda, mobil, dst.)
        v
  Geometri multi-view (5 keyframe, threshold Dz=0,4 m)
        |             -> masker gerak nyata
        v
  Gabungan masker dinamis (N+G)
        |
        v
  Buang fitur ORB pada masker --> pelacakan pose + pemetaan
        |
        v
  Background inpainting (RGB+D dari keyframe lampau)
        |
        v
  Peta statis bersih + citra latar terekonstruksi
```

### Pelacakan Berbiaya Rendah dan Pemetaan Utama

Sebelum verifikasi geometris dapat dijalankan, sistem memerlukan estimasi pose awal yang cepat. Untuk itu, sebuah pelacak ringan memproyeksikan titik peta yang sudah diketahui statis ke *frame* saat ini dan meminimalkan galat reproyeksi hanya pada wilayah tersebut, menghasilkan pose awal dalam orde 1,6–1,7 milidetik per *frame*. Pose awal ini dipakai untuk proyeksi pada tahap geometri di atas. Setelah masker dinamis final diperoleh, jalur pelacakan dan pemetaan utama — mewarisi mesin ORB-SLAM2, termasuk *bundle adjustment* (optimisasi bersama pose dan titik peta) dan *loop closing* (penutupan lintasan berulang) — dijalankan hanya dengan fitur pada wilayah statis.

### Background Inpainting

Setelah peta statis dan pose kamera tersedia, piksel latar yang tertutup objek bergerak pada *frame* saat ini direkonstruksi dengan memproyeksikan warna dan kedalaman dari *keyframe* statis sebelumnya yang memiliki pandangan ke area tersebut. Hasilnya adalah citra latar yang bersih dari objek dinamis, dapat dipakai untuk visualisasi maupun sebagai masukan bersih bagi sistem lain.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada sekuens dinamis tolok ukur TUM RGB-D — kumpulan data standar untuk SLAM RGB-D berisi urutan orang berjalan dan duduk sambil kamera bergerak dalam berbagai pola (xyz, *half sphere*, *rpy*, statis) — serta pada tolok ukur KITTI untuk konfigurasi stereo di lingkungan jalan raya. Metrik utamanya adalah ATE RMSE, sebagaimana dijelaskan di bagian Gambaran Umum.

Angka yang paling dapat diverifikasi dari naskah adalah hasil pada sekuens *walking_xyz*: DynaSLAM dengan kombinasi Mask R-CNN dan geometri (N+G) mencapai ATE RMSE 0,015 m, dibandingkan 0,459 m pada ORB-SLAM2 tanpa penyaringan dinamis — penurunan galat sekitar 96,7%, atau lintasan yang diestimasi mendekati 30 kali lebih presisi. Perbaikan sebesar ini konsisten dengan desain sistem: pada sekuens tersebut, dua orang yang berjalan menutupi porsi besar citra, sehingga tanpa penyaringan, mayoritas fitur yang dipakai ORB-SLAM2 justru berasal dari objek bergerak, bukan latar diam.

Naskah juga melaporkan tiga konfigurasi berbeda dari sistem: hanya memakai Mask R-CNN (N), hanya memakai geometri multi-view (G), dan gabungan keduanya (N+G). Konfigurasi gabungan secara konsisten menjadi yang terbaik pada sekuens yang diuji, karena menutup kelemahan yang telah dijelaskan pada bagian Ide Utama — N saja gagal pada objek dinamis di luar daftar kelas MS COCO, sedangkan G saja bergantung pada ketersediaan *keyframe* rujukan yang cukup. Dari sisi kecepatan, komponen-komponen pipeline memiliki biaya yang timpang: inferensi Mask R-CNN memakan sekitar 195 milidetik per citra pada GPU, verifikasi geometri sekitar 235–333 milidetik, dan pengisian latar sekitar 183–208 milidetik, jauh lebih mahal daripada pelacakan berbiaya rendah yang hanya 1,6–1,7 milidetik. Pada tolok ukur KITTI, yang didominasi *scene* jalan raya relatif statis, hasil DynaSLAM sebanding dengan ORB-SLAM2 pada sebagian besar sekuens, dengan selisih yang lebih terasa pada sekuens dengan kandungan dinamis lebih tinggi.

## Kelebihan dan Keterbatasan

Kelebihan utama DynaSLAM adalah lompatan akurasi pada *scene* dinamis dibandingkan SLAM berbasis fitur klasik, dibuktikan lewat penurunan ATE RMSE sekitar 96,7% pada sekuens *walking_xyz*. Sistem juga menghasilkan keluaran tambahan yang bernilai praktis, yaitu peta statis bersih lewat penambalan latar, dan fleksibel karena mendukung tiga konfigurasi kamera. Penggabungan sinyal semantik dan geometris membuat cakupan deteksi dinamis lebih luas daripada mengandalkan salah satu pendekatan saja.

Keterbatasan yang diakui penulis meliputi dua kasus spesifik: kendaraan yang sedang parkir — meski termasuk kelas "mobil" yang dianggap berpotensi dinamis — turut dibuang dari perhitungan pose walaupun sebenarnya diam, sehingga berpotensi membuang fitur berguna pada *scene* yang didominasi kendaraan diam; dan sekuens dengan gerakan kamera murni berupa rotasi (*rpy*) menghasilkan kualitas inpainting yang menurun, karena verifikasi geometri multi-view memerlukan pergeseran translasi kamera yang cukup untuk membandingkan kedalaman antar-*keyframe*.

Dari sisi rekayasa, biaya komputasi pipeline — terutama inferensi Mask R-CNN dan verifikasi geometri yang bersama-sama memakan ratusan milidetik per *frame* — membuat sistem ini tidak berjalan waktu nyata secara keseluruhan, sehingga lebih cocok untuk pemetaan luring (*offline*) atau pemetaan jangka panjang daripada navigasi daring pada robot bergerak. Secara konseptual, ketergantungan pada daftar kelas MS COCO yang telah ditentukan berarti objek dinamis di luar daftar tersebut hanya dapat dikenali lewat jalur geometri, yang sendiri memerlukan riwayat *keyframe* dan pergeseran kamera yang memadai.

## Kaitan dengan Bab Lain

DynaSLAM adalah perluasan langsung dari ORB-SLAM2 (bab 107): seluruh mesin pelacakan, pemetaan, dan *loop closing* diwarisi utuh, dengan tambahan tahap penyaringan dinamis dan inpainting di depannya. Komponen segmentasinya memakai Mask R-CNN, jaringan yang dibahas tersendiri pada bab 017, sehingga bab tersebut relevan untuk memahami bagaimana masker piksel per objek dihasilkan. Dalam klaster RGB-D SLAM, DynaSLAM sezaman dengan DS-SLAM (bab 109), yang memakai jalur berbeda — segmentasi semantik SegNet dikombinasikan dengan pemeriksaan konsistensi epipolar — untuk memecahkan masalah yang sama, sehingga kedua bab layak dibaca berdampingan sebagai dua strategi berbeda menuju tujuan yang sama. Kajian lanjutan pada bab 111 (Soares dkk., perbandingan YOLO dan Mask R-CNN untuk SLAM) memperluas pertanyaan yang diangkat DynaSLAM, yaitu memilih detektor mana yang paling seimbang antara akurasi segmentasi dan biaya komputasi untuk peran serupa.

- [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)
- [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)
- [111 - 2019 - Visual SLAM YOLO vs Mask R-CNN (Soares dkk.) - RGB-D SLAM](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md)

## Poin untuk Sitasi

Kutip dengan kunci `bescos2018dynaslam`. Ringkasan yang aman dikutip: "DynaSLAM memperluas ORB-SLAM2 dengan menggabungkan segmentasi Mask R-CNN dan verifikasi geometri multi-view untuk membuang fitur pada objek dinamis, menurunkan ATE RMSE pada sekuens TUM RGB-D *walking_xyz* dari 0,459 m menjadi 0,015 m, serta menambahkan penambalan latar untuk menghasilkan peta statis bersih." Angka 0,015 m / 0,459 m serta parameter (5 *keyframe* rujukan, ambang Δz = 0,4 m) berasal dari penelusuran naskah dan cukup dapat diandalkan; angka ATE RMSE untuk sekuens lain (*walking_halfsphere*, *walking_rpy*, *walking_static*, *sitting_xyz*, dan seterusnya), rincian angka pada tolok ukur KITTI, serta angka waktu komputasi per tahap (± 195 ms Mask R-CNN, ± 235–333 ms geometri, ± 183–208 ms inpainting) diperoleh dari pembacaan sekunder atas naskah dan sebaiknya dicocokkan langsung dengan tabel pada PDF asli sebelum dikutip dalam karya formal.
