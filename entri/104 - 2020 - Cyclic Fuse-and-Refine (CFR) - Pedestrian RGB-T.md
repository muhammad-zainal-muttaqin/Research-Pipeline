# 104 - Multispectral Fusion for Object Detection with Cyclic Fuse-and-Refine Blocks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2020cfr` |
| Judul asli | Multispectral Fusion for Object Detection with Cyclic Fuse-and-Refine Blocks |
| Penulis | Heng Zhang, Elisa Fromont, Sébastien Lefevre, Bruno Avignon |
| Tahun | 2020 |
| Venue | IEEE International Conference on Image Processing (ICIP 2020) |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **arXiv:** https://arxiv.org/abs/2009.12664
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Multispectral%20Fusion%20for%20Object%20Detection%20with%20Cyclic%20Fuse-and-Refine%20Blocks&sort=relevance

## Gambaran Umum

Makalah ini mengusulkan modul fusi bernama *Cyclic Fuse-and-Refine* (CFR, gabung-dan-saring siklik) untuk deteksi objek pada citra multispektral — pasangan citra yang berasal dari dua pita spektrum berbeda, dalam hal ini citra tampak (RGB) dan citra termal inframerah panjang (*long-wave infrared*, LWIR) yang merekam pancaran panas objek. Alih-alih menggabungkan fitur RGB dan termal satu kali lalu meneruskannya langsung ke kepala deteksi, CFR mengulang proses penggabungan (*fuse*) dan penyempurnaan (*refine*) fitur beberapa kali sebelum fitur akhir dipakai untuk memprediksi kotak objek. Modul ini dirancang sebagai komponen sisipan (*plug-in*) yang dapat ditambahkan pada titik fusi pertengahan jaringan detektor tanpa mengubah arsitektur secara keseluruhan.

Pada dataset pejalan kaki multispektral KAIST, detektor yang disisipi CFR mencapai *miss rate* (tingkat objek yang gagal terdeteksi, makin kecil makin baik) keseluruhan 6,13% pada set uji tersanitasi, dengan 7,68% pada citra siang dan 3,19% pada citra malam. Pada dataset kedua, FLIR ADAS (citra jalan raya siang-malam untuk kendaraan, sepeda, dan pejalan kaki), penyisipan CFR menaikkan *mean Average Precision* (mAP) dari 71,17% menjadi 72,39% dibandingkan model dasar tanpa modul ini. Bab ini melanjutkan garis fusi RGB-termal untuk deteksi pejalan kaki yang dimulai pada dataset KAIST (bab 100) dan diperluas pada bab 101–103; perbedaan utamanya terletak pada skema iteratif, bukan gerbang pembobotan satu arah seperti pada ketiga bab tersebut.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi pejalan kaki berbasis kamera tunggal RGB gagal pada malam hari atau kondisi cahaya rendah, sedangkan kamera termal tetap merekam pancaran panas tubuh manusia terlepas dari pencahayaan, tetapi kehilangan detail tekstur dan warna yang berguna pada siang hari. Karena itu, sistem deteksi pejalan kaki modern menggabungkan kedua modal ini. Metode-metode fusi sebelumnya — termasuk IAF R-CNN (bab 101) yang membobot modal berdasarkan estimasi kondisi pencahayaan, MBNet (bab 102) yang menyeimbangkan kontribusi modal secara adaptif, dan GAFF (bab 103) yang memakai *attention* (mekanisme pembobotan fitur otomatis) berjenjang — semuanya menggabungkan fitur RGB dan termal dalam satu kali lintasan: fitur mentah tiap modal dihitung, digabungkan sekali, lalu hasil gabungan diteruskan searah ke tahap deteksi.

Skema satu-lintasan ini memiliki keterbatasan struktural. Setelah proses fusi selesai, tidak ada jalur bagi hasil gabungan untuk kembali menyaring fitur modal asal sebelum keputusan akhir diambil. Akibatnya, derau pada satu modal — misalnya siluet termal yang kabur pada objek jauh, atau citra RGB yang gelap pada malam hari — ikut terbawa ke representasi gabungan tanpa mekanisme koreksi lanjutan. Makalah ini berangkat dari premis bahwa fitur gabungan, yang sudah memuat informasi dari kedua modal, semestinya dapat dipakai balik untuk menyaring fitur modal asal, dan bahwa proses ini dapat diulang beberapa kali agar kedua modal saling memperbaiki satu sama lain secara bertahap.

## Ide Utama

Gagasan inti CFR adalah mengganti satu langkah fusi dengan satu siklus fusi-dan-penyaringan yang diulang beberapa kali. Setiap siklus terdiri atas dua operasi berurutan. Pertama, operasi *fuse*: peta fitur RGB dan peta fitur termal pada lapis tertentu digabungkan (*concatenate*) lalu diproses oleh satu konvolusi 3×3 dengan normalisasi *batch* (teknik penstabil pelatihan yang menormalkan aktivitas tiap lapis) untuk menghasilkan satu peta fitur gabungan. Kedua, operasi *refine*: peta fitur gabungan ini ditambahkan sebagai koneksi residual (nilai yang dijumlahkan langsung, bukan menggantikan) ke masing-masing peta fitur modal asal, diikuti fungsi aktivasi ReLU, sehingga menghasilkan peta fitur RGB dan termal versi baru yang telah disaring oleh informasi gabungan.

Peta fitur hasil penyaringan pada siklus pertama menjadi masukan bagi siklus kedua, dan seterusnya. Dengan begitu, informasi mengalir dua arah: dari modal ke fusi, dan dari fusi kembali ke modal — berulang beberapa kali sebelum fitur akhir diteruskan ke kepala deteksi. Mekanisme inilah yang membedakan CFR dari fusi satu-lintasan pada bab 101–103, yang hanya menempuh arah modal-ke-fusi satu kali.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dasar

CFR diimplementasikan di atas FSSD (*Feature Fusion Single Shot Detector*), varian detektor satu tahap yang menggabungkan peta fitur dari beberapa kedalaman jaringan sebelum kepala prediksi, dengan tulang punggung (*backbone*, jaringan ekstraksi fitur) VGG16. Jaringan memiliki dua cabang paralel dengan bobot terpisah: satu cabang memproses citra RGB, satu cabang memproses citra termal. Titik penggabungan pertama ditempatkan setelah lapis konvolusi conv4_3, yaitu pertengahan jaringan — pola fusi pertengahan (*halfway fusion*) yang sama juga dipakai pada bab 102 dan 103, berbeda dari fusi dini pada tingkat piksel atau fusi lambat pada tingkat keluaran akhir.

### Blok Fuse dan Blok Refine

Skema satu siklus CFR dapat digambarkan sebagai berikut:

```
   fitur RGB (F_rgb)          fitur termal (F_th)
        │                          │
        └────────concat────────────┘
                    │
             konv 3x3 + BatchNorm
                    │
              fitur gabungan (F_fuse)
              │                 │
          + residual        + residual
              │                 │
            ReLU              ReLU
              │                 │
        F_rgb baru        F_th baru
        (masuk siklus       (masuk siklus
         berikutnya)          berikutnya)
```

Pada blok *fuse*, F_rgb dan F_th digabungkan sepanjang dimensi kanal, lalu satu konvolusi 3×3 dengan bobot bersama menghasilkan F_fuse — satu peta fitur tunggal yang memuat informasi dari kedua modal. Pada blok *refine*, F_fuse dijumlahkan sebagai residual ke F_rgb dan F_th secara terpisah, kemudian melalui ReLU. Karena F_fuse yang sama disuntikkan ke kedua cabang, kedua modal menerima umpan balik informasi yang identik namun diproses ulang oleh jalur masing-masing pada siklus berikutnya.

### Jumlah Siklus dan Efeknya

Percobaan menguji 0 (dasar tanpa CFR) sampai 4 siklus. Tabel berikut merangkum *miss rate* pada KAIST beserta skor DICE (ukuran kemiripan antara segmentasi turunan dari cabang termal dan cabang RGB pada tiap siklus, menandakan seberapa selaras kedua modal setelah disaring):

| Jumlah siklus | Miss rate keseluruhan |
|---|---|
| 0 (dasar) | 7,68% |
| 1 | 6,90% |
| 2 | 6,40% |
| 3 | 6,13% |
| 4 | 7,09% |

Miss rate menurun secara konsisten sampai tiga siklus, lalu naik kembali pada siklus keempat. Interpretasinya: penyaringan berulang memperbaiki fitur sampai titik tertentu, tetapi siklus yang berlebihan membuat fitur RGB dan termal menjadi terlalu mirip satu sama lain sehingga informasi yang saling melengkapi antar-modal justru berkurang. Tiga siklus dipilih sebagai konfigurasi akhir pada seluruh percobaan lain di makalah ini.

### Biaya Komputasi

Setiap siklus tambahan menyumbang biaya inferensi sekitar 0,4 milidetik, jauh lebih kecil dibandingkan biaya konvolusi utama jaringan. Dengan tiga siklus, total tambahan waktu inferensi berada pada orde milidetik tunggal, sehingga CFR tidak mengubah kelas kecepatan detektor dasarnya secara berarti.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada KAIST Multispectral Pedestrian (diperkenalkan pada bab 100), dataset pasangan citra RGB-termal untuk deteksi pejalan kaki yang direkam pada kondisi siang dan malam. Memakai anotasi uji yang telah disanitasi (versi anotasi yang diperbaiki dari kesalahan pelabelan pada rilis awal dataset), model dengan tiga siklus CFR mencapai *miss rate* 6,13% secara keseluruhan, 7,68% pada subset siang, dan 3,19% pada subset malam. Selisih besar antara siang dan malam konsisten dengan sifat termal: pada malam hari, citra RGB kehilangan sebagian besar informasi sedangkan citra termal tetap merekam siluet tubuh manusia dengan jelas, sehingga fusi lebih mudah menghasilkan deteksi akurat. Menurut makalah, hasil ini mengungguli metode fusi sebelumnya yang diuji pada protokol yang sama, termasuk MSDS-RCNN, IAF R-CNN, dan pendekatan berbasis *attention* semacam GAFF.

Evaluasi kedua dilakukan pada FLIR ADAS, dataset citra jalan raya siang-malam untuk tiga kelas objek (sepeda, mobil, pejalan kaki). Karena rilis asli memuat banyak pasangan RGB-termal yang tidak sejajar secara spasial, penulis menyusun subset kurasi berisi 4.129 pasangan latih dan 1.013 pasangan uji yang telah diperiksa kesejajarannya. Pada subset ini, model dasar tanpa CFR mencapai mAP 71,17%, dan penyisipan tiga siklus CFR menaikkannya menjadi 72,39% — kenaikan sekitar 1,2 poin persentase yang konsisten pada seluruh tiga kelas objek. Hasil pada dua dataset dengan karakteristik berbeda (pejalan kaki tunggal pada KAIST, tiga kelas objek jalan raya pada FLIR) menunjukkan bahwa manfaat CFR tidak spesifik untuk satu tugas deteksi saja.

## Kelebihan dan Keterbatasan

Kelebihan utama CFR adalah kesederhanaan mekanismenya: hanya konvolusi, normalisasi *batch*, penjumlahan residual, dan ReLU, tanpa mekanisme *attention* yang lebih rumit seperti pada GAFF (bab 103). Karena berbentuk modul sisipan, CFR dapat ditambahkan pada titik fusi pertengahan berbagai arsitektur detektor tanpa mengubah struktur keseluruhan, dan biaya komputasi tambahannya kecil. Perbaikan konsisten pada dua dataset dengan jumlah kelas dan karakteristik pencahayaan berbeda menunjukkan modul ini tidak terbatas pada deteksi pejalan kaki saja.

Keterbatasan yang tercatat dalam makalah adalah sensitivitas terhadap jumlah siklus: performa memburuk melewati tiga siklus, sehingga jumlah siklus optimal harus ditentukan lewat percobaan pada tiap dataset, bukan nilai baku yang berlaku umum. Dari sisi rekayasa, blok fuse memakai bobot bersama dan operasi simetris terhadap kedua modal, sehingga desain ini secara implisit mengasumsikan kedua modal memiliki keandalan yang setara pada titik fusi — asumsi yang dapat kurang tepat pada kondisi ekstrem ketika satu modal jauh lebih rusak daripada modal lainnya, situasi yang justru menjadi motivasi utama pendekatan berbasis bobot adaptif pada bab 101 dan 102. Secara konseptual, titik fusi CFR tetap pada satu kedalaman jaringan tertap (setelah conv4_3), sehingga modul ini tidak mengeksplorasi fusi pada beberapa kedalaman berbeda secara bersamaan.

## Kaitan dengan Bab Lain

CFR mewarisi dataset dan definisi tugas dari bab 100 (KAIST Multispectral Pedestrian), sumber data uji utamanya. Dibandingkan dengan tiga bab sebelumnya pada klaster Pedestrian RGB-T — bab 101 (IAF R-CNN, pembobotan modal berdasarkan pencahayaan), bab 102 (MBNet, penyeimbangan modal adaptif), dan bab 103 (GAFF, *attention* berjenjang) — CFR menempuh jalur berbeda dengan mengubah fusi satu-lintasan menjadi proses iteratif bersiklus. Gagasan umpan balik siklik ini relevan bagi bab 105 (CMPD, fusi lintas-modal berbasis ketidakpastian) sebagai pembanding pendekatan iteratif versus pendekatan berbasis estimasi ketidakpastian, dan bagi bab 106 (fusi RGB-D oleh Farahnakian & Heikkonen) sebagai contoh bahwa penyaringan fitur berulang antar-modal juga berpotensi diterapkan di luar pasangan RGB-termal, misalnya pada pasangan RGB-kedalaman.

- [100 - 2015 - KAIST Multispectral Pedestrian - Pedestrian RGB-T](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)
- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [103 - 2021 - GAFF - Pedestrian RGB-T](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md)
- [105 - 2022 - CMPD (Uncertainty-Guided Cross-Modal) - Pedestrian RGB-T](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md)
- [106 - 2021 - RGB-D Fusion for Detection (Farahnakian & Heikkonen) - Pedestrian RGB-T](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md)

## Poin untuk Sitasi

Kutip dengan kunci `zhang2020cfr`. Ringkasan yang aman dikutip: "CFR mengusulkan modul fusi iteratif yang menggabungkan lalu menyaring fitur RGB dan termal secara siklis di dalam FSSD berbasis VGG16, mencapai *miss rate* 6,13% pada KAIST tersanitasi (7,68% siang, 3,19% malam) dan menaikkan mAP pada FLIR ADAS kurasi dari 71,17% menjadi 72,39% dengan tiga siklus penyaringan." Angka *miss rate* per siklus (7,68% / 6,90% / 6,40% / 6,13% / 7,09%) dan angka mAP FLIR berasal dari pembacaan naskah arXiv dan dianggap cukup andal, tetapi angka perbandingan langsung terhadap metode lain (MSDS-RCNN, IAF R-CNN, IATDNN+IASS) tidak diperoleh secara konsisten dari sumber sekunder yang tersedia dan wajib diverifikasi ke tabel asli makalah sebelum dikutip dalam karya formal.
