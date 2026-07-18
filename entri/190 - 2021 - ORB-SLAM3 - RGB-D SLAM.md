# 190 - ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `campos2021orbslam3` |
| Judul asli | ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM |
| Penulis | Carlos Campos, Richard Elvira, Juan J. Gómez Rodríguez, José M. M. Montiel, Juan D. Tardós |
| Tahun | 2021 |
| Venue | IEEE Transactions on Robotics (T-RO), vol. 37, no. 6, hlm. 1874–1890 |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.11898
- **Google Scholar:** https://scholar.google.com/scholar?q=ORB-SLAM3%3A%20An%20Accurate%20Open-Source%20Library%20for%20Visual%2C%20Visual-Inertial%2C%20and%20Multimap%20SLAM
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ORB-SLAM3%3A%20An%20Accurate%20Open-Source%20Library%20for%20Visual%2C%20Visual-Inertial%2C%20and%20Multimap%20SLAM&sort=relevance
- **Kode sumber:** https://github.com/UZ-SLAMLab/ORB_SLAM3

## Gambaran Umum

ORB-SLAM3 adalah pustaka *SLAM* (*Simultaneous Localization and Mapping*, penentuan posisi kamera sekaligus pembangunan peta lingkungan secara bersamaan dan seketika) yang menyatukan tiga kemampuan dalam satu sistem: SLAM visual murni, SLAM visual-inersial (menggabungkan kamera dengan sensor IMU/*Inertial Measurement Unit*, pengukur percepatan dan kecepatan sudut), dan SLAM multi-peta. Sistem ini bekerja pada kamera monokular, stereo, dan RGB-D, dengan model lensa *pinhole* maupun *fisheye* (lensa sudut sangat lebar). Makalah ini adalah penerus langsung ORB-SLAM2 (bab 107), dengan dua tambahan utama: inisialisasi visual-inersial berbasis estimasi *Maximum-a-Posteriori* (MAP, estimasi parameter yang memaksimalkan probabilitas gabungan data dan prior) yang bekerja sejak detik-detik awal perekaman, serta struktur *Atlas* yang menampung banyak peta terputus dan menggabungkannya kembali saat area yang sama dikunjungi ulang. Pada pengujian EuRoC dan TUM-VI, penulis melaporkan ORB-SLAM3 dua hingga sepuluh kali lebih akurat dibandingkan sistem visual-inersial sebelumnya, dengan galat rata-rata sekitar 3,5–4,3 cm pada penerbangan drone EuRoC dan sekitar 9–11 mm pada gerak genggam cepat TUM-VI.

## Latar Belakang: Masalah yang Ingin Dipecahkan

ORB-SLAM2 sudah menyediakan SLAM fitur yang akurat untuk kamera monokular, stereo, dan RGB-D, tetapi tanpa dukungan sensor inersial dan tanpa mekanisme pemulihan yang baik saat pelacakan (*tracking*) gagal total. Dua kekurangan itulah yang mendorong ORB-SLAM3. Pertama, sistem visual-inersial yang ada sebelumnya — misalnya VINS-Mono dan VINS-Fusion — umumnya memakai inisialisasi bertahap: parameter inersial (skala, arah gravitasi, bias giroskop dan akselerometer, kecepatan) diestimasi dengan solusi aljabar tertutup yang mengabaikan model derau sensor secara ketat, baru kemudian disempurnakan lewat optimisasi visual-inersial penuh. Pendekatan ini membutuhkan waktu inisialisasi lama, pada kisaran 20–30 detik, sebelum estimasi skala cukup stabil untuk dipakai.

Kedua, ketika kamera bergerak sangat cepat, memasuki area bertekstur minim, atau tertutup sesaat, pelacakan berbasis fitur mudah kehilangan jejak. Sistem SLAM lama umumnya menghentikan pemetaan atau memaksa relokalisasi terhadap peta yang sama, sehingga seluruh informasi yang terkumpul sebelum kegagalan berisiko terbuang atau sesi terpisah tidak pernah tergabung. Pada aplikasi robotika dan realitas tertambah (*augmented reality*) yang berjalan lama, kegagalan semacam ini berulang kali terjadi, dan sistem yang tidak punya cara elegan menggabungkan kembali sesi-sesi terputus kehilangan konsistensi peta jangka panjang.

## Ide Utama

Gagasan inti ORB-SLAM3 ada dua, saling melengkapi. Pertama, seluruh proses inisialisasi visual-inersial dirumuskan sebagai satu masalah estimasi MAP sejak awal, bukan sebagai solusi aljabar diikuti penghalusan belakangan. Estimasi MAP mencari nilai parameter yang memaksimalkan probabilitas gabungan antara data pengamatan (visual dan inersial) dan pengetahuan prior tentang derau sensor, sehingga ketidakpastian setiap sumber data diperhitungkan secara konsisten sejak langkah pertama. Konsekuensinya, estimasi skala dan bias IMU menjadi jauh lebih cepat konvergen dibandingkan solusi aljabar bertahap.

Kedua, sistem tidak lagi memaksakan satu peta tunggal yang harus selalu tersambung. Struktur data bernama *Atlas* menyimpan banyak submap independen: begitu pelacakan hilang, ORB-SLAM3 langsung memulai submap baru alih-alih berhenti atau memaksa relokalisasi. Setiap submap memiliki *keyframe* (bingkai kunci, citra terpilih yang menyimpan pose kamera dan titik peta terkait) dan titik peta sendiri. Pengenalan tempat (*place recognition*) berjalan terus-menerus di latar belakang terhadap seluruh submap dalam Atlas, bukan hanya submap aktif; begitu kecocokan geometris ditemukan, submap-submap yang relevan digabungkan menjadi satu peta yang konsisten.

## Cara Kerja Langkah demi Langkah

### Empat Utas Paralel

Seperti ORB-SLAM2, sistem berjalan sebagai empat utas (*thread*) paralel: *tracking* (pelacakan pose kamera per bingkai), *local mapping* (perluasan dan penghalusan peta lokal), *loop closing* (deteksi dan koreksi jalur tertutup pada peta yang sama), serta utas baru *Atlas management* yang menangani penggabungan submap. Fitur yang dipakai untuk pelacakan dan pencocokan adalah fitur ORB (*Oriented FAST and Rotated BRIEF*), deskriptor citra biner yang cepat dihitung dan tahan terhadap rotasi citra.

```
Kamera/IMU -> Tracking -> Local Mapping -> Loop Closing/Merging
                 |              |                  |
             pose per       keyframe +         query Atlas
             bingkai        titik peta         (semua submap)
                 |                                  |
            submap aktif  <----------------  gabung bila cocok
```

Diagram di atas meringkas alur: *tracking* menghasilkan pose kamera untuk setiap bingkai baru pada submap aktif; *local mapping* menambah keyframe dan titik peta ke submap itu; secara paralel, setiap keyframe baru diperiksa terhadap seluruh isi Atlas, bukan hanya submap yang sedang aktif, sehingga kecocokan dengan sesi lama dapat ditemukan kapan saja.

### Inisialisasi Visual-Inersial Tiga Tahap

Inisialisasi visual-inersial berjalan dalam tiga langkah berurutan. Tahap pertama adalah SLAM visual murni selama sekitar dua detik, menghasilkan peta berskala sembarang (belum diketahui skala metriknya) dengan sekitar sepuluh keyframe dan beberapa ratus titik, dioptimalkan dengan *bundle adjustment* visual (optimasi bersama pose kamera dan posisi titik peta agar proyeksi ulang ke citra sesuai pengamatan). Tahap kedua adalah estimasi MAP murni-inersial: dengan lintasan visual yang sudah ada dianggap tetap, sistem menyelesaikan skala metrik, arah gravitasi, bias giroskop-akselerometer, dan kecepatan tiap keyframe, memakai pengukuran inersial yang telah diintegrasi-awal (*preintegration*, penggabungan sampel IMU berfrekuensi tinggi menjadi satu batasan antar-keyframe). Tahap ketiga menggabungkan seluruh parameter — visual dan inersial — dalam satu optimisasi gabungan penuh. Menurut naskah, pendekatan ini mencapai galat skala sekitar 5% dalam dua detik pertama dan menyusut ke sekitar 1% dalam lima belas detik, jauh lebih cepat dibandingkan metode aljabar tertutup yang butuh puluhan detik untuk stabil.

### Atlas dan Penggabungan Peta

Atlas terdiri atas kumpulan submap, masing-masing dengan grafik *covisibility* (grafik yang menghubungkan keyframe yang mengamati titik peta yang sama) dan pohon rentang (*spanning tree*) sendiri. Satu submap berstatus aktif — tempat *tracking* dan *local mapping* berjalan — sementara submap lain berstatus tidak aktif namun tetap tersimpan penuh. Setiap kali *local mapping* membuat keyframe baru, modul pengenalan tempat berbasis DBoW2 (basis data kata visual berbobot untuk pencarian citra mirip secara cepat) mencari beberapa kandidat keyframe serupa di seluruh Atlas, kemudian setiap kandidat diverifikasi secara geometris bertahap agar presisi kecocokan mendekati sempurna.

Bila kandidat yang cocok berasal dari submap aktif sendiri, sistem menjalankan *loop closing*: transformasi Sim(3) (transformasi kemiripan tiga dimensi mencakup rotasi, translasi, dan skala; atau SE(3) tanpa skala pada mode dengan IMU/stereo) dihitung untuk menutup jalur dan galat drift disebar lewat optimisasi grafik pose (*pose-graph optimization*). Bila kandidat berasal dari submap lain, sistem melakukan penggabungan peta (*map merging*): submap aktif dan submap yang cocok disatukan lewat penyelarasan langsung, kemudian diperkuat dengan pencarian pada "jendela pengelasan" (*welding window*) — kumpulan keyframe covisible di sekitar titik pertemuan — untuk menambah asosiasi data, dan ditutup dengan *bundle adjustment* lokal serta optimisasi grafik pose global.

## Eksperimen dan Hasil

Evaluasi kuantitatif utama dilakukan pada dua *benchmark* visual-inersial: EuRoC (sekuens dari drone yang terbang di dalam ruangan pabrik dan ruang vicon, dengan kamera stereo dan IMU tersinkron) dan TUM-VI (sekuens genggam tangan dengan kamera fisheye dan IMU, representatif untuk skenario *augmented/virtual reality*). Metrik yang dipakai adalah *Absolute Trajectory Error* (ATE, galat rata-rata jarak Euclidean antara lintasan estimasi dan lintasan kebenaran-dasar setelah penyelarasan).

Pada EuRoC, konfigurasi stereo-inersial mencapai galat rata-rata sekitar 3,5 cm, sedangkan monokular-inersial sekitar 4,3 cm; keduanya mengungguli VINS-Fusion (13,8 cm untuk stereo-inersial) dan VINS-Mono (11,0 cm untuk monokular-inersial) pada sekuens yang sama. Pada TUM-VI, konfigurasi stereo-inersial mencapai rata-rata sekitar 9 mm dan monokular-inersial sekitar 11 mm pada sekuens ruangan, angka yang menurut penulis kompetitif untuk kebutuhan pelacakan gerak cepat khas AR/VR. Pada pengujian multi-sesi pada rangkaian sekuens EuRoC MH01–MH05 — skenario yang secara langsung menguji kemampuan Atlas menggabungkan sesi terputus — ORB-SLAM3 stereo-inersial mencapai galat sekitar 4,7 cm, jauh lebih rendah dibandingkan VINS-Mono pada rangkaian sekuens yang sama (21,0 cm), memperlihatkan manfaat menggabungkan informasi lintas sesi dibandingkan memulai ulang setiap sesi secara terpisah.

Interpretasi keseluruhan: perbaikan akurasi terbesar berasal dari inisialisasi MAP yang lebih cepat konvergen dan dari kemampuan menggunakan kembali informasi lintas sesi lewat Atlas, bukan semata dari perubahan fitur atau *front-end* visual, karena fitur ORB dan struktur pelacakan dasarnya mewarisi langsung dari ORB-SLAM2. Perlu dicatat, evaluasi kuantitatif dalam naskah berfokus pada EuRoC dan TUM-VI (mode visual-inersial); makalah tidak menyertakan tabel hasil ATE terpisah untuk mode RGB-D pada *benchmark* seperti TUM RGB-D, meskipun dukungan sensor RGB-D disediakan pada implementasi dan diklaim menghasilkan akurasi yang kompetitif secara kualitatif.

## Kelebihan dan Keterbatasan

Kelebihan utama ORB-SLAM3 adalah cakupan sensor yang luas — satu basis kode melayani monokular, stereo, dan RGB-D, dengan atau tanpa IMU, serta model lensa *pinhole* dan *fisheye* — sehingga satu sistem dapat dipakai lintas platform robot tanpa penulisan ulang. Kemampuan Atlas menyelamatkan sesi yang terputus akibat oklusi atau tekstur minim adalah perbaikan nyata dibandingkan ORB-SLAM2, yang pada kondisi serupa kehilangan seluruh peta sejak titik kegagalan. Inisialisasi MAP yang konvergen dalam hitungan detik membuat mode visual-inersial dapat dipakai lebih cepat setelah sistem dinyalakan, dibandingkan solusi aljabar bertahap yang butuh puluhan detik.

Dari sisi keterbatasan yang dinyatakan atau tersirat dari desainnya, sistem tetap bergantung pada fitur titik ORB yang jarang (*sparse*), sehingga rentan pada permukaan bertekstur sangat minim, pencahayaan ekstrem, atau pola berulang yang menyesatkan pencocokan fitur. Secara konseptual, ORB-SLAM3 dirancang untuk lingkungan yang secara dominan statis; objek bergerak dalam pemandangan tidak ditangani secara eksplisit oleh modul manapun dalam pustaka ini, sehingga penerapan pada lingkungan dinamis memerlukan lapisan tambahan seperti yang dibahas pada DynaSLAM (bab 108) dan DS-SLAM (bab 109). Dari sisi rekayasa, jumlah parameter yang perlu disetel — ambang deteksi fitur, jumlah level piramida citra, parameter kovarians IMU, ambang verifikasi geometris pada pengenalan tempat — cukup banyak, dan performa optimal umumnya membutuhkan penyesuaian per platform kamera/IMU. Terakhir, karena evaluasi kuantitatif naskah tidak mencakup mode RGB-D pada *benchmark* standar, klaim akurasi RGB-D ORB-SLAM3 tidak didukung tabel angka spesifik dalam makalah ini dan sebaiknya diperiksa lewat pengujian mandiri atau makalah turunan sebelum dikutip sebagai hasil kuantitatif.

## Kaitan dengan Bab Lain

ORB-SLAM3 adalah kelanjutan langsung dari ORB-SLAM2 (bab [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)): struktur empat utas, fitur ORB, dan format keyframe/titik peta pada ORB-SLAM3 mewarisi langsung dari pendahulunya, dengan tambahan inti berupa inisialisasi MAP visual-inersial dan struktur Atlas multi-peta. Pustaka ini juga menjadi basis untuk sistem SLAM semantik yang menangani lingkungan dinamis, seperti DynaSLAM (bab [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)) dan DS-SLAM (bab [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)), yang menambahkan deteksi objek bergerak di atas kerangka pelacakan fitur serupa ORB-SLAM. Dibandingkan dengan DROID-SLAM (bab [191 - 2021 - DROID-SLAM - RGB-D SLAM](./191%20-%202021%20-%20DROID-SLAM%20-%20RGB-D%20SLAM.md)), yang terbit pada tahun sama, ORB-SLAM3 mewakili paradigma berbasis fitur jarang yang dioptimalkan lewat *bundle adjustment* eksplisit, sedangkan DROID-SLAM memakai jaringan saraf dalam untuk mengestimasi aliran optik dan kedalaman padat sebagai pengganti pencocokan fitur — dua garis pendekatan yang saling melengkapi dalam tinjauan SLAM RGB-D pada klaster ini.

## Poin untuk Sitasi

Kutip dengan kunci `campos2021orbslam3`. Ringkasan yang aman dikutip: "ORB-SLAM3 menyatukan SLAM visual, visual-inersial, dan multi-map dalam satu pustaka yang mendukung kamera monokular, stereo, dan RGB-D dengan lensa pinhole maupun fisheye, memakai inisialisasi inersial berbasis estimasi Maximum-a-Posteriori dan struktur Atlas untuk menggabungkan sesi peta yang terputus." Angka ATE (3,5 cm dan 4,3 cm pada EuRoC stereo/mono-inersial; 9 mm dan 11 mm pada TUM-VI; 4,7 cm pada pengujian multi-sesi EuRoC) diambil dari tabel hasil arXiv 2007.11898 dan sebaiknya dicocokkan ulang dengan tabel resmi pada naskah T-RO sebelum dikutip dalam karya formal, karena versi arXiv dan versi jurnal dapat memiliki perbedaan kecil pada angka tabel. Klaim kuantitatif untuk mode RGB-D murni tidak ditemukan dalam tabel hasil naskah dan perlu diverifikasi terpisah, misalnya lewat pengujian mandiri pada TUM RGB-D atau makalah yang mengutip perbandingan tersebut.
