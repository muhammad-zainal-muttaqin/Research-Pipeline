# SLAM-PYE: Tightly coupled GNSS-binocular-inertial fusion for pitaya positioning, counting, and yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024slam` |
| Judul asli | SLAM-PYE: Tightly coupled GNSS-binocular-inertial fusion for pitaya positioning, counting, and yield estimation |
| Penulis | Wang, Hongjie; Hong, Xiangyu; Qin, Linlin; Shi, Chun; Wu, Gang |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pitaya |

## Tautan Akses
- PDF: [wang2024slam.pdf](../pdf/wang2024slam.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109177

## Gambaran Umum

Makalah ini mengusulkan SLAM-PYE, sistem estimasi posisi, jari-jari, jumlah, dan hasil panen buah naga (*pitaya*, *Hylocereus costaricensis*) di rumah kaca. Sistem menggabungkan citra dari kamera binokular, data inersia (*Inertial Measurement Unit*, IMU), dan pengukuran mentah *Global Navigation Satellite System* (GNSS) dua frekuensi dalam satu graf faktor probabilistik. Setiap buah memperoleh ID dan posisi global yang unik, sehingga buah yang terlihat berulang kali, misalnya karena perangkat bergerak maju lalu mundur atau buah tertutup lalu terlihat kembali, tidak dihitung dua kali. Perangkat dibawa dengan tangan pada platform genggam, tanpa *lidar*, kamera *depth* aktif, maupun lengan robot.

Data eksperimen terdiri atas empat urutan dalam ruangan (A sampai D) dengan 24 model buah naga tiruan pada rak, dan dua urutan di rumah kaca komersial di pinggiran Kota Hefei, Provinsi Anhui (E dan F, Desember 2023). Dua puluh buah dipilih, diberi nomor, lalu diukur jari-jari dan beratnya sebagai acuan. Detektor YOLOv8 dilatih pada 1.267 citra buatan sendiri dengan mAP@0,5 sebesar 95,1%.

Hasil utama menurut abstrak dan kesimpulan: RMSE posisi sekitar 7 cm, RMSE jari-jari 7 mm, dan MAPE berat per buah sekitar 16%. Pada urutan E, detektor menemukan 294 buah pada citra 2D dan sistem membuat 97 buah pada peta 3D. Penulis memeriksa secara manual bahwa tidak ada penghitungan ganda pada urutan E dan F. Sistem berjalan pada 23 bingkai per detik, lebih cepat daripada keluaran kamera (20 bingkai per detik).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil panen sebelum panen membantu alokasi sumber daya. Cara tradisional menimbang buah pada beberapa titik sampel bermasalah pada jumlah dan sebaran sampel. Penulis membedakan metode tidak langsung (model statistik dari faktor cuaca, geografi, dan citra multispektral) dan metode langsung (ukuran tiap buah dijumlahkan menjadi hasil total). Metode tidak langsung sulit digeneralisasi antarwilayah. Metode langsung membutuhkan posisi dan ukuran buah yang akurat.

Pendekatan langsung yang ada memiliki empat kelemahan menurut penulis. Pertama, sensor yang mengukur jarak langsung (kamera *depth*, *lidar*, lengan robot) mahal. Kamera *depth* berbasis cahaya terstruktur atau *Time of Flight* (ToF) juga rusak pembacaannya di bawah sinar matahari langsung. Kedua, *Structure from Motion* (SFM) memulihkan tekstur halus yang tidak diperlukan dan menuntut komputasi besar. Penulis mengutip satu studi SFM multi-pandang yang memerlukan 46 menit untuk galat jari-jari sekitar 4 mm. Ketiga, sensor tanpa pengukuran posisi global memberi posisi relatif yang berbeda untuk buah yang sama sehingga terjadi penghitungan ganda. Keempat, pandang tetap membuat sebagian buah tertutup dan terabaikan. Di rumah kaca berlapis film ganda, pengukuran GNSS juga terganggu pantulan sinyal (*multipath*), sehingga solusi RTK sulit terkunci dan *Single-Point Positioning* (SPP) melompat.

## Ide Utama

Identitas unik buah dijamin oleh posisi global, bukan oleh pelacak ID visual. Pelacak (Deep OC-Sort) hanya mengeliminasi duplikat pada bingkai bersebelahan. Bila buah menghilang lalu muncul kembali, pelacak memberi ID baru, dan makalah menunjukkan contohnya (Gambar 5: ID 115 dan 117 berubah menjadi 196 dan 198 saat perangkat bergerak mundur). Kendala pengukuran GNSS dan visual-inersia dalam satu graf faktor membuat peta konsisten secara global, sehingga buah yang sama dari beberapa pandang menyatu pada satu posisi.

Gagasan kedua adalah memperlakukan status buah (posisi dan jari-jari) sebagai variabel optimasi. Nilai awalnya dihitung secara analitik dari pengukuran satu pandang kamera binokular. Selanjutnya, residu proyeksi ulang dari banyak pandang memperbaiki nilai itu dan menyingkirkan pencilan. Penulis mengklaim, sepengetahuan mereka, ini pertama kali residu *pseudorange* bebas-ionosfer dan Doppler dimasukkan ke graf faktor visual-inersia untuk mengatasi *multipath* di rumah kaca. Berat tiap buah dihitung dari jari-jari dengan polinomial kubik, dan hasil total adalah jumlah berat semua buah.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data dan perangkat

Sensor dipasang pada platform genggam karena buah naga berada kurang dari satu meter di atas tanah. Perangkat terdiri atas kamera binokular buatan sendiri (sensor AR0234, *global shutter*, 1280 × 720 piksel, 20 Hz, garis dasar 55 mm), IMU BMI-088 (200 Hz), penerima GNSS ZED-F9P (10 Hz) dan UM982 (20 Hz), serta tiga antena. Keluaran citra dan *depth* kamera RealSense D455 sengaja diblokir; hanya data inersianya yang dipakai. Penghitungan memakai komputer dengan CPU Intel i7-8700, RAM 32 GB, dan GPU RTX-3060. Cap waktu kamera dan IMU disinkronkan ke UTC lewat sinyal PPS dari UM982.

Eksperimen dalam ruangan dilakukan di pusat eksperimen USTC. Acuan posisi berasal dari perangkat pemosisi optik Prime 17W. Jarak lintasan dari rak divariasikan dari urutan A ke D. Eksperimen rumah kaca dilakukan di kebun komersial berspesies *Hylocereus costaricensis* dengan jarak antartitik sampel 2 sampai 5 m (diukur dengan meteran sebagai acuan posisi). Jumlah pohon atau jumlah citra total tidak dilaporkan.

### 2. Prapemrosesan dan penyelarasan GNSS-VI

Kalibrasi dilakukan antara kamera binokular dan IMU (toolbox Kalibr) serta antara IMU dan penerima GNSS (jarak diukur manual dengan jangka sorong). Pengukuran IMU dipra-integrasi di antara bingkai. Data GNSS disaring dengan membuang satelit berstatus abnormal, rasio sinyal terhadap derau rendah, pengukuran dua frekuensi tidak lengkap, atau sudut elevasi rendah. Kombinasi $L_{MW}$ dan $L_{GF}$ mendeteksi lompatan fase, dan *pseudorange* dua frekuensi digabung menjadi *pseudorange* bebas-ionosfer. Konstelasi yang dipakai adalah GPS (L1, L2) dan BDS (B1, B3).

Penyelarasan koordinat lokal dengan koordinat ECEF dilakukan tiga langkah dari kasar ke halus. Langkah 1 memperkirakan posisi penerima hanya dari faktor *pseudorange* untuk memperoleh titik jangkar awal, yang menurut penulis bergeser sekitar sepuluh meter di rumah kaca. Langkah 2 memperkirakan rotasi dengan kendala faktor Doppler. Langkah 3 memperkirakan posisi jangkar dan rotasi dengan kendala kedua faktor. Berbeda dari karya pembanding yang hanya memperkirakan *yaw*, sistem ini menghitung rotasi tiga sumbu.

### 3. Faktor GNSS dalam graf optimasi

Faktor *pseudorange* membatasi posisi perangkat, dan faktor Doppler membatasi kecepatannya. Jumlah sinyal satelit melebihi selusin meskipun di dalam rumah kaca berfilm ganda, sehingga penulis tidak memodelkan degradasi GNSS. Optimasi dilakukan dalam jendela geser (pada ilustrasi berukuran tiga) dengan kernel Huber. Tiga strategi menyingkirkan pencilan: kernel Huber, pembuangan sisi graf yang residunya melebihi ambang, dan aturan atribut manual (sebaran vertikal dan jari-jari buah yang wajar).

### 4. Deteksi dan pelacakan buah

YOLOv8 (arsitektur tidak diubah) mengeluarkan kotak buah. Posisi proyeksi dan jari-jari proyeksi dihitung dari kotak itu. Jari-jari proyeksi dihitung dengan faktor $0{,}5 \times 0{,}7 \times \sqrt{c_l^2 + d_l^2}$. Kelas yang dilatih adalah matang dan belum matang; hanya buah matang yang diperlukan sistem. Deep OC-Sort memberi ID konsisten pada bingkai berurutan.

### 5. Estimasi posisi dan jari-jari dari satu pandang

Buah yang muncul di citra kiri dan kanan dengan keyakinan di atas ambang serta tinggi dan jari-jari serupa dianggap pasangan. Disparitas memberi kedalaman $d = f_x b / (p_x - p_z)$ lalu posisi 3D di kerangka kamera dan kerangka lokal. Jari-jari dihitung secara geometris dari sudut $\theta$ dan $\phi$ yang diturunkan dari jari-jari proyeksi dan kedalaman. Pengukuran dengan $\theta$ lebih dari 45 derajat dikecualikan.

### 6. Optimasi multi-pandang dan penyaringan

Residu proyeksi ulang pada posisi dan jari-jari dari banyak pandang meminimalkan galat status buah. Penulis menjelaskan bahwa posisi hasil satu pandang bergeser terutama pada arah kedalaman, dapat mencapai sepuluh kali jari-jari buah, sedangkan galat jari-jari sekitar satu orde besaran lebih kecil. Buah yang berjarak lebih dari dua puluh kali garis dasar diabaikan. Buah dengan posisi atau jari-jari tidak wajar, jumlah pengukuran multi-pandang di bawah ambang, atau jarak kamera tidak wajar disaring dari peta.

### 7. Estimasi berat dan hasil panen

Berat per buah dimodelkan dengan polinomial kubik $w = a r^3 + b r^2 + c r$. Dengan kuadrat terkecil dari 54 pasang berat dan jari-jari diperoleh $a = 0{,}011$, $b = -0{,}521$, $c = 14{,}656$, dengan $R^2 = 0{,}852$. Hasil rumah kaca adalah jumlah berat semua buah dalam peta.

## Eksperimen dan Hasil

Metrik mengikuti kerja lain: RMSE untuk posisi dan jari-jari, MAPE untuk berat, dan koefisien variasi (*Coefficient of Variation*, CV) untuk kestabilan estimasi berat dalam satu urutan. Setiap urutan dijalankan berulang agar pengaruh keacakan pemilihan fitur terukur; Tabel 4 memuat lima estimasi tipikal per urutan, sehingga ada 30 entri. Jumlah sampel adalah 24 buah dalam ruangan dan 20 buah di rumah kaca. Pembanding berupa sistem lain tidak diuji pada data yang sama; Tabel 7 hanya membandingkan perkiraan biaya perangkat.

| Ukuran | Dalam ruangan (A sampai D) | Rumah kaca (E dan F) |
|---|---|---|
| Galat horizontal (rentang RMSE pada Tabel 4) | sekitar 19 sampai 32 mm | sekitar 39 sampai 62 mm |
| Galat vertikal (rentang RMSE pada Tabel 4) | sekitar 12 sampai 27 mm | sekitar 39 sampai 61 mm |
| Galat posisi jarak Euklides (teks) | sekitar 30 mm | sekitar 70 mm |
| Median RMSE jari-jari | 6,4 mm (buah besar), 5,6 mm (buah kecil) | 7,1 mm |
| MAPE berat per buah | tidak dilaporkan | median 15,7% (E), 16% (F) |
| CV berat rata-rata urutan | tidak dilaporkan | 4,1% (E), 5,5% (F) |

Rentang kolom horizontal dan vertikal dibaca dari nilai minimum dan maksimum pada Tabel 4 yang terbaca dari ekstraksi teks.

Data tambahan yang dilaporkan:

- Galat posisi dari algoritma analitik satu pandang adalah 134 mm (horizontal) dan 237 mm (vertikal), sedangkan sistem lengkap mencapai RMSE di bawah 30 mm dalam ruangan (Bagian 5.2).
- Pada rumah kaca, rata-rata jari-jari per urutan berkisar 38,3 sampai 40,5 mm, rata-rata berat 422,4 sampai 492,4 g, dan MAPE berat per urutan 13,2% sampai 21,5% (Tabel 5).
- Dua puluh buah sampel semuanya terestimasi dan tidak ada yang menjadi pencilan. Dari 97 buah yang dibuat pada urutan E, penulis memperkirakan galat hasil panen seluruh rumah kaca sekitar 16%. Angka ini adalah perkiraan penulis dari median MAPE sampel, bukan galat yang diukur terhadap panen total.
- Pada urutan E, 294 buah terdeteksi pada citra 2D dan 97 dibuat pada peta 3D. Sebanyak 19 buah disaring dengan penyebab: jari-jari atau posisi 3D di luar rentang wajar (5), pengukuran multi-pandang di bawah ambang (12), jarak kamera tidak wajar (8). Sebagian buah disaring karena lebih dari satu sebab. Pemeriksaan manual menunjukkan hanya 13 dari 19 yang seharusnya disaring, sehingga ada buah normal yang ikut terbuang.
- Tidak ada *false positive* pada seluruh eksperimen menurut penulis.
- Waktu proses (Tabel 6): deteksi sekitar 12 ms, ekstraksi fitur sekitar 22 ms, estimasi pose sekitar 10 ms per bingkai, dan *local BA* 108,1 sampai 307,2 ms per urutan. Kecepatan keseluruhan 23 bingkai per detik.
- Biaya perangkat sekitar 200 dolar menurut Tabel 7, dibandingkan 900 sampai 1.300 dolar pada sistem pembanding berbasis *lidar* atau kamera *depth* yang dikutip penulis (hanya biaya sensor chip yang dihitung pada sistem ini).

Analisis sebaran menunjukkan buah terkonsentrasi di bagian timur laut rumah kaca, dekat kanal irigasi. Tinggi buah tidak menunjukkan preferensi dan jari-jari seragam, sekitar 40 mm.

## Kelebihan dan Keterbatasan

Kelebihan yang dibuktikan dalam makalah: identitas buah global unik tanpa sensor aktif, penghitungan ganda tidak ditemukan pada pemeriksaan manual, galat jari-jari kecil (sekitar 7 mm pada buah berjari-jari sekitar 40 mm), dan sistem berjalan waktu nyata dengan perangkat murah. Penggunaan banyak pandang juga membuat oklusi oleh cabang berdampak kecil karena sebagian besar buah terlihat utuh pada pandang tertentu.

Keterbatasan yang dinyatakan penulis:

- Akurasi vertikal lebih rendah daripada horizontal pada rumah kaca karena satelit hanya tersebar di sekeliling dan di atas, sehingga kendala horizontal pada graf lebih banyak. Penulis berencana menambah barometer dan magnetometer.
- Pelacak yang dirancang untuk objek umum dapat menyebabkan buah terlewat (*missing counting*). Kasus yang dibahas: dua buah berdekatan terbaca sebagai satu (ditekan dengan ambang jari-jari), buah kecil dan terlalu dini matang tidak dikenali, dan sebagian buah normal ikut tersaring.
- Berat dimodelkan sebagai elipsoid, dan penyimpangan bentuk buah dari model itu memengaruhi galat berat. Kecocokan polinomial kubik memiliki $R^2$ 0,852.
- Detektor dapat salah mengenali objek seperti bata merah dan buah busuk di tanah. Penulis mengatasi dengan data lebih banyak dan penyaringan tinggi dari tanah.
- Rencana pengujian pada buah yang lebih sulit, yaitu pir, apel pada pohon tinggi dan rapat, serta stroberi.

Menurut pembacaan ringkasan ini, terdapat keterbatasan yang tidak dinyatakan secara eksplisit:

- Validasi hasil panen hanya memakai 20 buah sampel dalam satu rumah kaca, sehingga galat 16% untuk seluruh rumah kaca merupakan ekstrapolasi. Jumlah buah sebenarnya di rumah kaca tidak dilaporkan sebagai acuan hitung, sehingga ketepatan hitungan total tidak terukur.
- Angka 97 buah pada urutan E berasal dari sistem dan dicek manual terhadap penghitungan ganda, tetapi tidak dibandingkan dengan hitung lapangan penuh.
- Metode bergantung pada penerimaan GNSS yang baik. Di bawah kanopi lebat atau tempat tanpa sinyal satelit, jaminan identitas global tidak berlaku, dan indikasi penggunaan di luar rumah kaca tidak diuji.
- Tidak ada perbandingan numerik langsung dengan metode lain pada data yang sama, dan dataset tidak dibuka umum (tersedia atas permintaan).

## Kaitan dengan Tinjauan main6

Makalah ini secara eksplisit menangani buah yang terlihat lebih dari sekali, dan merupakan contoh mekanisme identitas berbasis lokalisasi global. Buah dapat terlihat berulang kali karena perangkat bergerak maju lalu mundur dan karena oklusi sementara. Identitas diselesaikan dengan menyatukan seluruh deteksi pada satu posisi 3D di peta global yang dikunci oleh GNSS dan fusi visual-inersia, bukan dengan pencocokan penampilan. Pelacak bingkai-ke-bingkai ditunjukkan gagal untuk kasus ini (ID berubah setelah buah menghilang dari bingkai). Hitungan dilaporkan sebagai jumlah buah dan berat total, tidak per kelas. Detektor memang membedakan buah matang dan belum matang, tetapi hanya buah matang yang dihitung, dan tidak ada inventaris per kelas kematangan. Acuan hasil hitung adalah pemeriksaan manual penulis terhadap penghitungan ganda, sedangkan acuan berat dan jari-jari adalah penimbangan dan jangka sorong pada 20 buah terpilih; hitung lapangan total atau panen tidak digunakan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: prinsip menjadikan posisi 3D bersama sebagai kunci identitas, dengan optimasi multi-pandang yang menyingkirkan pencilan, serta peran pelacak 2D sebagai pemasok deteksi, bukan penentu identitas. Kendalanya, pohon sawit tinggi, buah berada di ketiak pelepah, dan pengambilan citra per sisi pohon tidak berupa lintasan kontinu, sehingga fusi visual-inersia kontinu pada sistem ini tidak langsung dapat dipakai. Pengukuran posisi global di bawah kanopi perlu dipertimbangkan secara terpisah. Hal itu merupakan kesimpulan ringkasan ini, bukan klaim makalah.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `wang2024slam`.

Wang dkk. (2024) mengusulkan SLAM-PYE, sistem yang mengikat pengukuran mentah GNSS dua frekuensi, citra binokular, dan data inersia dalam graf faktor untuk memperkirakan posisi, jari-jari, jumlah, dan hasil panen buah naga di rumah kaca komersial. Posisi global buah yang dioptimalkan dari banyak pandang dipakai untuk menjamin identitas unik sehingga buah yang terlihat berulang tidak dihitung dua kali, sedangkan pelacak ID visual hanya bekerja pada bingkai bersebelahan. Pada eksperimen rumah kaca, penulis melaporkan RMSE posisi sekitar 7 cm, RMSE jari-jari sekitar 7 mm, MAPE berat per buah sekitar 16%, dan tidak ada penghitungan ganda pada pemeriksaan manual dua urutan, dengan 20 buah sampel sebagai acuan dan kecepatan 23 bingkai per detik pada perangkat sekitar 200 dolar.

Catatan verifikasi data: RMSE posisi 7 cm, jari-jari 7 mm, dan MAPE sekitar 16% tertulis di abstrak dan kesimpulan. Median RMSE jari-jari 6,4 mm, 5,6 mm, dan 7,1 mm ada di Bagian 4.3. Median MAPE 15,7% dan 16%, CV 4,1% dan 5,5%, serta pernyataan penelusuran manual penghitungan ganda ada di Bagian 4.4, dengan nilai per urutan pada Tabel 5. Angka 294 deteksi 2D, 97 buah peta, 19 buah tersaring, dan 13 yang semestinya tersaring ada di Bagian 5.3. Galat posisi satu pandang 134 dan 237 mm ada di Bagian 5.2. Koefisien polinomial dan $R^2$ ada di Bagian 3.8, mAP@0,5 YOLOv8 dan 1.267 citra di Bagian 3.5, waktu proses di Tabel 6, dan biaya di Tabel 7. Tabel 4 terbaca dari ekstraksi teks dalam bentuk daftar angka per baris; rentang dalam entri ini dibaca dari angka tersebut dan perlu dicek ulang pada PDF bila dikutip. Jumlah pohon, jumlah citra rumah kaca, jumlah buah acuan lapangan, dan hasil panen total sebenarnya tidak dapat diverifikasi dari teks. Makalah memakai klaim "pertama kali" yang tidak dapat diperiksa dari teks.
