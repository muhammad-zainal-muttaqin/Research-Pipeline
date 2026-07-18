# 107 - ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `murartal2017orbslam2` |
| Judul asli | ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras |
| Penulis | Raúl Mur-Artal, Juan D. Tardós |
| Tahun | 2017 |
| Venue | IEEE Transactions on Robotics, vol. 33, no. 5, hlm. 1255–1262 |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1610.06475
- **Google Scholar:** https://scholar.google.com/scholar?q=ORB-SLAM2%3A%20An%20Open-Source%20SLAM%20System%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ORB-SLAM2%3A%20An%20Open-Source%20SLAM%20System%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ORB-SLAM2, sistem *SLAM* (*Simultaneous Localization and Mapping* — estimasi posisi kamera dan pembangunan peta lingkungan secara bersamaan dan seketika) berbasis fitur yang bekerja untuk tiga jenis sensor: kamera monokular (satu lensa), stereo (dua lensa dengan jarak baseline tetap), dan RGB-D (warna ditambah kedalaman per piksel). Sistem ini menyatukan pelacakan pose kamera per bingkai (*tracking*), pembangunan dan penghalusan peta titik tiga dimensi (*mapping*), serta pengenalan tempat yang pernah dikunjungi untuk mengoreksi galat kumulatif (*loop closing*, penutupan lingkar), seluruhnya berjalan waktu nyata pada CPU standar tanpa GPU.

Kontribusi utama ORB-SLAM2 terhadap pendahulunya, ORB-SLAM (monokular saja), adalah perluasan ke stereo dan RGB-D dengan pemanfaatan langsung informasi kedalaman untuk memperoleh skala metrik sejak bingkai pertama, serta mode lokalisasi ringan yang dapat beroperasi tanpa terus memperbarui peta. Pada evaluasi terhadap 29 barisan data (*sequence*) publik yang mencakup KITTI, EuRoC MAV, dan TUM RGB-D, sistem ini mencatat akurasi lintasan yang menyamai atau melampaui metode sejenis pada masanya, sambil mempertahankan kecepatan waktu nyata. Kode sumber dipublikasikan terbuka, dan implementasi ini menjadi rujukan baku (*baseline*) bagi banyak sistem SLAM turunan, termasuk yang menambahkan kesadaran semantik untuk menangani objek bergerak.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum ORB-SLAM2, sistem SLAM visual umumnya terpecah menurut jenis sensor: ada metode yang dirancang khusus monokular, khusus stereo, atau khusus RGB-D, masing-masing dengan basis kode dan asumsi berbeda. Metode berbasis kedalaman seperti KinectFusion berfokus pada rekonstruksi permukaan yang padat dan rinci, tetapi pendekatan ini mahal secara komputasi dan sulit menjaga konsistensi lintasan pada wilayah luas karena representasi permukaannya menyulitkan koreksi global saat lingkar (*loop*) dikenali kembali. Metode berbasis fitur monokular murni menghadapi masalah ambiguitas skala: dari citra tunggal, jarak sebenarnya antar-titik tidak dapat ditentukan tanpa informasi tambahan, dan inisialisasi peta awal memerlukan pergeseran sudut pandang (paralaks) yang memadai antara dua bingkai — sesuatu yang tidak selalu tersedia, misalnya saat kamera murni berputar di tempat.

Masalah kedua adalah galat kumulatif (*drift*): karena setiap estimasi pose baru dibangun di atas estimasi sebelumnya, kesalahan kecil menumpuk seiring panjang lintasan. Solusinya adalah pengenalan lingkar (*loop closure*) — mendeteksi bahwa kamera kembali ke tempat yang pernah direkam, lalu menyebarkan koreksi ke seluruh riwayat pose — tetapi deteksi yang andal dan koreksi yang murah bukan hal sepele pada peta besar. Masalah ketiga adalah kegagalan pelacakan: bila kamera bergerak terlalu cepat atau pandangan terhalang, sistem kehilangan jejak pose dan perlu **relokalisasi** (menemukan kembali posisi kamera di peta yang sudah ada) tanpa memulai peta dari nol. ORB-SLAM2 diajukan untuk menjawab ketiga masalah ini sekaligus, dalam satu kerangka yang seragam untuk monokular, stereo, dan RGB-D.

## Ide Utama

Gagasan inti ORB-SLAM2 adalah memakai satu arsitektur berbasis fitur ORB (*Oriented FAST and Rotated BRIEF* — deskriptor titik-kunci citra yang cepat dihitung dan tahan terhadap rotasi) untuk tiga modalitas sensor, dengan perbedaan utama hanya pada cara memperoleh kedalaman tiap titik fitur: pada stereo, kedalaman dihitung dari selisih posisi fitur di dua citra (disparitas); pada RGB-D, kedalaman dibaca langsung dari sensor. Dengan kedalaman tersedia sejak bingkai pertama, peta awal dapat dibangun seketika dari satu bingkai saja — berbeda dengan monokular murni yang harus menunggu paralaks memadai antara dua bingkai sebelum triangulasi dapat dilakukan.

Di atas fondasi ini, sistem menjalankan tiga alur kerja paralel yang saling melengkapi: satu alur memperkirakan pose kamera bingkai demi bingkai, satu alur menjaga kualitas peta lokal, dan satu alur mendeteksi kapan kamera kembali ke tempat lama untuk membetulkan seluruh lintasan sekaligus. Karena ketiganya berjalan sebagai proses terpisah, pelacakan pose tidak perlu menunggu peta selesai dioptimalkan penuh.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur dan Estimasi Kedalaman per Sensor

Setiap bingkai masuk diproses dengan mengekstraksi titik-kunci ORB pada beberapa tingkat skala citra (piramida skala), sehingga fitur pada objek dekat maupun jauh tetap terdeteksi. Untuk stereo, setiap fitur di citra kiri dicocokkan dengan kandidatnya di citra kanan sepanjang garis epipolar untuk menghitung disparitas, yang dikonversi menjadi kedalaman memakai baseline (jarak tetap antar-dua lensa) dan panjang fokus kamera. Untuk RGB-D, kedalaman diambil langsung dari peta kedalaman sensor pada koordinat piksel fitur tersebut.

Makalah membedakan titik **dekat** dan **jauh** berdasarkan ambang kedalaman relatif terhadap baseline stereo: titik dengan kedalaman kurang dari sekitar 40 kali baseline dianggap dekat dan dapat ditriangulasi andal dari satu bingkai saja, memberi informasi skala, translasi, dan rotasi yang kuat. Titik yang lebih jauh hanya memberi informasi rotasi yang andal; skala dan translasinya baru dapat dipertajam setelah diamati dari beberapa sudut pandang. Pembedaan ini membuat sistem stereo/RGB-D berinisialisasi lebih cepat dan stabil dibandingkan monokular murni, karena titik dekat langsung menyediakan skala metrik tanpa menunggu pergerakan kamera yang cukup untuk triangulasi multi-bingkai.

### Tiga Alur Kerja Paralel

```
Bingkai baru (RGB / stereo / RGB-D)
        |
        v
 [ TRACKING ]  --pose per bingkai--> keluaran lintasan
   cocokkan fitur ke peta lokal,
   minimkan galat reproyeksi
        |
        | (bingkai kunci baru)
        v
 [ LOCAL MAPPING ]
   sisipkan keyframe, triangulasi
   titik baru, bundle adjustment
   lokal, buang keyframe redundan
        |
        | (kandidat lingkar terdeteksi)
        v
 [ LOOP CLOSING ]
   cocokkan dengan DBoW2,
   optimasi pose graph,
   picu bundle adjustment penuh
   (thread ke-4, di latar belakang)
```

Alur **tracking** (pelacakan) berjalan setiap bingkai: fitur ORB bingkai saat ini dicocokkan dengan titik peta yang sudah ada, lalu pose kamera diperkirakan dengan meminimalkan galat reproyeksi (selisih antara posisi titik yang diamati dan posisi yang diprediksi bila titik peta diproyeksikan ke citra). Bila jumlah titik yang berhasil dilacak menurun cukup banyak dibandingkan *keyframe* (bingkai kunci, bingkai yang disimpan permanen sebagai rujukan peta) terakhir, bingkai saat ini dijadikan *keyframe* baru dan diteruskan ke alur berikutnya.

Alur **local mapping** (pemetaan lokal) menerima *keyframe* baru, mentriangulasi titik fitur baru yang belum ada di peta, lalu menjalankan *bundle adjustment* lokal — optimasi bersama pose beberapa *keyframe* bertetangga dan titik peta yang mereka amati agar peta tetap konsisten secara geometris. Alur ini juga membuang *keyframe* redundan agar ukuran peta tidak membengkak tanpa menambah informasi baru.

Alur **loop closing** (penutupan lingkar) mencari kecocokan tempat pada setiap *keyframe* baru memakai DBoW2 (*bag-of-words* dari deskriptor ORB — representasi citra sebagai histogram kemunculan pola visual, memungkinkan pencarian kecocokan tempat cepat tanpa membandingkan piksel). Bila lingkar terdeteksi dan tervalidasi, sistem menjalankan optimasi *pose graph* (optimasi hanya atas hubungan relatif antar-*keyframe*, lebih murah daripada mengoptimalkan seluruh titik peta), lalu memicu *bundle adjustment* penuh di latar belakang. DBoW2 juga dipakai untuk relokalisasi ketika pelacakan gagal.

### Mode Lokalisasi Ringan

ORB-SLAM2 menyediakan mode tambahan yang menonaktifkan *local mapping* dan *loop closing*. Pelacakan pada mode ini memakai odometri visual (perkiraan gerak antar-bingkai) untuk wilayah yang belum terpetakan, dan pencocokan langsung ke titik peta yang sudah ada untuk mencegah galat menumpuk (*zero-drift localization*) saat kamera memasuki kembali wilayah yang telah dipetakan.

## Eksperimen dan Hasil

Evaluasi dilakukan pada 29 barisan data publik yang mencakup tiga tolok ukur berbeda. Pada **KITTI** (barisan data luar ruangan dari kendaraan, stereo), ORB-SLAM2 mengungguli Stereo LSD-SLAM dengan galat translasi relatif umumnya di bawah 1% dan galat posisi absolut (RMSE — *root mean square error*, akar rata-rata kuadrat selisih posisi terhadap posisi kebenaran lapangan) berkisar 0,2–10,4 meter, bergantung panjang dan kompleksitas lintasan tiap barisan data. Pada **EuRoC MAV** (barisan data drone dalam pabrik, stereo), galat translasi RMSE konsisten di bawah 12 sentimeter pada 11 barisan data, bahkan mencapai 1,8–3,7 sentimeter pada barisan data bertingkat kesulitan rendah, melampaui Stereo LSD-SLAM pada barisan data yang sama-sama terselesaikan.

Pada **TUM RGB-D** (barisan data genggam dalam ruangan, RGB-D), ORB-SLAM2 mencatat akurasi lebih baik dibandingkan metode padat berbasis kedalaman seperti ElasticFusion, Kintinuous, DVO-SLAM, dan RGB-D SLAM, dengan galat RMSE 0,004 meter pada barisan fr2/xyz, 0,009 meter pada fr2/desk, dan 0,010 meter pada fr3/office — bukti bahwa pendekatan berbasis fitur jarang tetap menyamai atau melampaui akurasi metode berbasis kedalaman penuh, sekaligus jauh lebih ringan secara komputasi.

Dari sisi kecepatan, tracking memerlukan 25,6–49,5 milidetik per bingkai dan local mapping 129,5–267,3 milidetik per *keyframe*, cukup cepat agar tracking selesai sebelum bingkai berikutnya tiba. Loop closing, saat terpicu, memakan 108,6–598,7 milidetik, dan bundle adjustment penuh 349–1.793 milidetik, keduanya berjalan di latar belakang tanpa mengganggu tracking utama. Penulis mencatat dua kegagalan spesifik: motion blur (citra kabur akibat gerak cepat) memutus pelacakan pada barisan data V2_03_difficult di EuRoC, dan mode monokular murni gagal pada satu barisan data KITTI jalan raya karena kurangnya titik dekat untuk skala yang stabil.

## Kelebihan dan Keterbatasan

Kelebihan utama ORB-SLAM2 adalah keseragaman arsitektur lintas tiga jenis sensor dalam satu basis kode, sehingga peneliti dapat berpindah modalitas tanpa mengganti kerangka algoritmenya. Akurasi yang dicapai menyamai atau melampaui metode padat berbasis kedalaman pada TUM RGB-D, sekaligus jauh lebih hemat komputasi karena hanya memproses fitur jarang. Sistem berjalan waktu nyata pada CPU standar tanpa GPU, dan kode sumbernya dipublikasikan terbuka — faktor yang menjelaskan mengapa metode ini menjadi rujukan baku yang luas dipakai pada riset SLAM berikutnya.

Keterbatasan yang diakui penulis meliputi kerentanan terhadap motion blur pada gerak cepat dan kegagalan inisialisasi monokular pada adegan dengan sedikit titik dekat. Dari sisi konseptual, representasi peta ORB-SLAM2 berupa awan titik jarang, bukan permukaan padat, sehingga tidak cocok untuk aplikasi yang membutuhkan rekonstruksi rinci seperti perencanaan genggaman robot; penulis sendiri menyatakan sistem ini memprioritaskan konsistensi lokalisasi jangka panjang di atas kelengkapan rekonstruksi. Dari sisi rekayasa, sistem juga mengasumsikan lingkungan sebagian besar statis — fitur ORB yang menempel pada objek bergerak dapat merusak estimasi pose karena algoritme tidak membedakan titik pada latar diam dan titik pada objek dinamis. Asumsi inilah yang menjadi motivasi langsung bagi sejumlah sistem turunan yang menambahkan deteksi objek untuk menyaring fitur pada area bergerak sebelum estimasi pose dijalankan.

## Kaitan dengan Bab Lain

ORB-SLAM2 adalah fondasi klaster RGB-D SLAM dalam tinjauan ini: arsitektur tiga alur dan representasi peta berbasis fitur ORB yang diwariskannya dipakai kembali oleh [190 - 2021 - ORB-SLAM3 - RGB-D SLAM](./190%20-%202021%20-%20ORB-SLAM3%20-%20RGB-D%20SLAM.md), yang memperluas kerangka ini dengan penggabungan sensor inersia dan peta multi-sesi. Asumsi lingkungan statis pada ORB-SLAM2 menjadi celah yang langsung disasar oleh [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md) dan [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md), yang menambahkan deteksi semantik untuk menyaring fitur pada objek bergerak sebelum estimasi pose. Bab [111 - 2019 - Visual SLAM YOLO vs Mask R-CNN (Soares dkk.) - RGB-D SLAM](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md) membandingkan detektor objek yang dipasangkan di atas kerangka SLAM sejenis, sedangkan [191 - 2021 - DROID-SLAM - RGB-D SLAM](./191%20-%202021%20-%20DROID-SLAM%20-%20RGB-D%20SLAM.md) mewakili arah alternatif yang menggantikan tracking berbasis fitur ORB dengan estimasi berbasis pembelajaran mendalam ujung ke ujung.

## Poin untuk Sitasi

Kutip dengan kunci `murartal2017orbslam2`. Ringkasan yang aman dikutip: "ORB-SLAM2 adalah sistem SLAM berbasis fitur ORB yang bekerja pada kamera monokular, stereo, dan RGB-D dengan tracking, local mapping, dan loop closing berjalan paralel; pada evaluasi 29 barisan data publik (KITTI, EuRoC MAV, TUM RGB-D), sistem ini mencatat akurasi yang menyamai atau melampaui metode SLAM sejenis sambil tetap berjalan waktu nyata pada CPU standar." Angka RMSE (mis. 0,2–10,4 m pada KITTI; di bawah 12 cm pada EuRoC; 0,004–0,010 m pada TUM RGB-D) dan waktu pemrosesan per tahap diambil dari abstrak dan isi naskah arXiv/ar5iv yang berhasil diakses, tetapi rincian tabel lengkap per barisan data sebaiknya diverifikasi ulang ke Tabel III–VI naskah asli sebelum dikutip dalam karya formal. Ambang klasifikasi titik dekat/jauh (~40× baseline) juga berasal dari naskah dan sebaiknya dicek ulang terhadap definisi presisi pada bagian metodologi.
