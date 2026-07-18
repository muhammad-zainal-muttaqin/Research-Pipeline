# 150 - Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `feng2021multimodalsurvey` |
| Judul asli | Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges |
| Penulis | Di Feng, Christian Haase-Schütz, Lars Rosenbaum, Heinz Hertlein, Claudius Glaeser, Fabian Timm, Werner Wiesbeck, Klaus Dietmayer |
| Tahun | 2021 |
| Venue | IEEE Transactions on Intelligent Transportation Systems |
| Tema | Fusi Multimodal |

## Tautan Akses
- **Unduh PDF Resmi (arXiv):** https://arxiv.org/abs/1902.07830
- **Tautan DOI Penerbit (IEEE):** https://doi.org/10.1109/TITS.2020.2971562
- **Platform Interaktif Bosch:** https://boschresearch.github.io/multimodalperception/

## Gambaran Umum
Makalah oleh Di Feng dkk. ini menyajikan sebuah survei komprehensif mengenai penerapan pembelajaran mendalam (*deep learning*) untuk deteksi objek tiga dimensi (3D) dan segmentasi semantik multimodal pada sistem berkendara otonom (*autonomous driving*). Penulis memetakan lanskap teknologi fusi yang mengintegrasikan berbagai jenis sensor utama kendaraan otonom, yaitu kamera (*passive sensor*), *light detection and ranging* (LiDAR) (*active sensor*), dan radar (*radio detection and ranging*). Tujuan dari survei ini adalah memberikan struktur taksonomi formal yang dapat digunakan oleh para peneliti untuk memahami bagaimana berbagai metode fusi dirancang dan diuji.

Kontribusi utama dari makalah ini terletak pada perumusan taksonomi fusi berdasarkan tiga sumbu keputusan desain: objek yang difusikan (*what to fuse*), waktu memfusikan (*when to fuse*), dan mekanisme penggabungan (*how to fuse*). Selain itu, makalah ini mendokumentasikan dataset multimodal publik yang tersedia secara global serta menguraikan tantangan terbuka di bidang persepsi kendaraan otonom, seperti kalibrasi lintas sensor yang tidak presisi, keterbatasan anotasi data 3D, ketahanan terhadap gangguan cuaca ekstrem, serta kebutuhan estimasi ketidakpastian (*uncertainty estimation*) untuk menjamin keselamatan berkendara.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pada kendaraan otonom, sistem persepsi harus mampu melakukan pemahaman pemandangan (*scene understanding*) yang sangat andal dalam segala situasi lingkungan. Setiap sensor fisik memiliki keterbatasan intrinsik yang tidak dapat dihindari. Kamera optik menghasilkan citra berwarna dengan resolusi spasial dan detail tekstur yang tinggi, sehingga sangat baik untuk klasifikasi semantik. Namun, kamera sangat rentan terhadap variasi pencahayaan, silau matahari, kondisi malam hari, serta cuaca buruk. Selain itu, mengekstrak informasi kedalaman 3D secara langsung dari gambar 2D merupakan masalah yang secara matematis tidak pasti (*ill-posed problem*).

LiDAR memecahkan keterbatasan kedalaman tersebut dengan memancarkan sinar laser aktif untuk menghasilkan awan titik (*point cloud*) 3D dengan akurasi spasial berkisar dalam fraksi sentimeter. Namun, LiDAR memiliki resolusi spasial yang jauh lebih rendah daripada kamera, mahal secara ekonomis, dan kinerjanya menurun drastis saat terhalang partikel atmosfer seperti kabut, hujan lebat, atau debu. Di sisi lain, radar yang menggunakan gelombang mikro sangat tangguh dalam menembus gangguan cuaca buruk dan dapat mendeteksi kecepatan relatif objek secara langsung melalui pergeseran Doppler (*Doppler shift*). Kelemahan radar adalah resolusi datanya yang sangat rendah dan adanya derau pantulan (*clutter*) yang tinggi, sehingga menyulitkan lokalisasi objek yang presisi.

Sebelum makalah survei ini diterbitkan, penelitian di bidang fusi sensor multimodal berkembang secara tidak terstruktur. Sebagian besar karya akademis merancang skema fusi secara heuristik (*ad-hoc*) untuk skenario spesifik tanpa landasan metodologis yang seragam. Istilah-istilah seperti *early fusion*, *late fusion*, dan *deep fusion* digunakan secara tidak konsisten dalam berbagai literatur. Selain itu, dataset awal seperti KITTI tidak menyertakan data radar secara lengkap, sehingga menyulitkan komparasi metode yang melibatkan radar. Ketiadaan klasifikasi sistematis ini menghambat pemahaman tentang kompromi (*trade-off*) antara akurasi deteksi, ketahanan terhadap kegagalan sensor tunggal, dan latensi komputasi dari masing-masing skema fusi.

## Ide Utama
Gagasan utama dari ulasan ilmiah ini adalah menyatukan seluruh metode fusi persepsi multimodal ke dalam satu kerangka taksonomi yang terstruktur secara matematis dan konseptual. Alih-alih memperkenalkan arsitektur baru, Feng dkk. mengusulkan kerangka klasifikasi berdasarkan tiga sumbu keputusan desain:

1. **Sumbu Temporal/Struktural (*When to fuse*):** Menentukan pada tahapan pemrosesan apa informasi dari modalitas yang berbeda disatukan. Penulis mengelompokkannya menjadi *early fusion* (fusi tingkat data atau fitur awal), *middle/deep fusion* (fusi bertahap pada representasi fitur laten intermediat), dan *late fusion* (fusi tingkat keputusan di mana setiap sensor menghasilkan prediksi masing-masing sebelum digabungkan).
2. **Sumbu Representasi (*What to fuse*):** Mengidentifikasi format data yang dilewatkan ke dalam modul fusi. Ini berkisar dari piksel citra 2D, representasi *voxel* (elemen volume 3D), representasi pandangan mata burung (*bird's-eye view* atau BEV), awan titik mentah, hingga vektor fitur abstrak berdimensi tinggi.
3. **Sumbu Metodologis (*How to fuse*):** Menentukan operasi matematika dan modul jaringan yang bertugas menyelaraskan dan menggabungkan informasi tersebut. Ini mencakup operasi sederhana seperti konkatenasi (*concatenation*) dan penjumlahan, hingga mekanisme dinamis seperti atensi spasial-kanal dan estimasi ketidakpastian.

## Cara Kerja Langkah demi Langkah
Metodologi survei yang dirancang oleh Feng dkk. diuraikan melalui langkah-langkah klasifikasi sistematis sebagai berikut:

### Klasifikasi Skema Fusi berdasarkan Tahapan Pemrosesan
Penulis mengklasifikasikan waktu penggabungan informasi sensor ke dalam tiga skema utama yang diilustrasikan dalam diagram berikut:

```
1. Early Fusion (Data/Fitur Awal):
   [Kamera RGB] ────────┐
                        ├─► [Penyelarasan Spasial] ─► [Konkatenasi] ─► [Jaringan] ─► [Output]
   [LiDAR Point] ───────┘

2. Middle/Deep Fusion (Fitur Laten Intermediat):
   [Kamera RGB] ────────► [Fitur Awal] ───┬───► [Fitur Tinggi] ────────┐
                                           │ (Interaksi Laten)         ├─► [Output]
   [LiDAR Point] ───────► [Fitur Awal] ───┴───► [Fitur Tinggi] ────────┘

3. Late Fusion (Tingkat Keputusan):
   [Kamera RGB] ────────► [Jaringan Kamera] ─► [Prediksi Bounding Box] ─┐
                                                                       ├─► [Fusi (NMS)] ─► [Output Final]
   [LiDAR Point] ───────► [Jaringan LiDAR]  ─► [Prediksi Bounding Box] ─┘
```

- **Early Fusion:** Data mentah atau fitur tingkat rendah dari masing-masing sensor diselaraskan secara spasial (misalnya dengan memproyeksikan awan titik LiDAR ke bidang gambar kamera menggunakan matriks proyeksi kalibrasi intrinsik-ekstrinsik). Setelah diselaraskan, data digabungkan (misalnya dengan menggabungkan saluran warna RGB dengan koordinat kedalaman $Z$ menjadi representasi 4D $[R, G, B, Z]$) sebelum diproses oleh satu tulang punggung (*backbone*) jaringan saraf.
- **Late Fusion:** Setiap sensor diproses oleh jaringan saraf yang terpisah secara independen untuk menghasilkan prediksi kelas objek dan kotak pembatas (*bounding box*) 3D. Keputusan dari masing-masing sensor kemudian digabungkan menggunakan algoritma non-pembelajaran seperti *Non-Maximum Suppression* (NMS), rata-rata berbobot (*weighted average*), atau teori pembuktian Dempster-Shafer untuk menghasilkan output final.
- **Middle/Deep Fusion:** Skema ini mengekstrak fitur laten dari setiap modalitas sensor secara terpisah menggunakan beberapa lapisan awal jaringan saraf. Fitur-fitur ini kemudian digabungkan secara bertahap pada lapisan intermediat. Skema ini memungkinkan jaringan mempelajari korelasi lintas modalitas yang kompleks pada berbagai tingkat abstraksi semantik dan skala spasial.

### Representasi Data Lintas Modalitas
Untuk menjembatani perbedaan representasi data antar sensor, survei ini mengidentifikasi tiga metode representasi utama:
- **Representasi Berbasis Kisi (*Grid-based*):** Mengubah awan titik LiDAR 3D yang tidak terstruktur menjadi kisi 2D atau 3D yang terstruktur. Ini termasuk proyeksi pandangan depan (*front view*), pandangan mata burung (BEV), dan vokselisasi (*voxelization*). Dengan representasi kisi ini, operasi konvolusi 2D atau 3D standar dapat diterapkan langsung ke data LiDAR dan kamera secara bersamaan.
- **Representasi Berbasis Titik (*Point-based*):** Mempertahankan representasi awan titik 3D asli yang tidak terstruktur dan menggunakan arsitektur seperti PointNet untuk mengekstrak fitur langsung dari koordinat $(x, y, z)$.
- **Representasi Berbasis Graf (*Graph-based*):** Memodelkan titik-titik LiDAR atau wilayah gambar sebagai simpul dalam graf dan menggunakan jaringan saraf graf (*graph neural networks*) untuk melewatkan informasi spasial.

### Sinkronisasi Spasial dan Temporal
Salah satu langkah kritis dalam fusi multimodal adalah mengatasi masalah koordinat spasial dan sinkronisasi temporal:
- **Kalibrasi Spasial:** Menggunakan matriks transformasi homogen untuk mengonversi titik koordinat dari ruang 3D LiDAR $(X_L, Y_L, Z_L)$ ke koordinat kamera 2D $(u, v)$ melalui matriks ekstrinsik (posisi relatif sensor) dan matriks intrinsik (karakteristik optik kamera).
- **Sinkronisasi Temporal:** Mengatasi perbedaan frekuensi pengambilan sampel sensor (misalnya kamera bekerja pada 30 Hz sedangkan LiDAR berputar pada 10 Hz). Metode yang umum digunakan adalah pemilihan bingkai terdekat secara temporal atau kompensasi gerakan menggunakan data sensor inersia (*inertial measurement unit* atau IMU) dan odometri kendaraan.

## Eksperimen dan Hasil
Sebagai sebuah ulasan ilmiah, bagian eksperimen menyajikan analisis komparatif performa berbagai metode fusi sensor yang diuji pada dataset patokan (*benchmark datasets*) utama, yaitu KITTI dan nuScenes.

Pada dataset KITTI untuk tugas deteksi objek 3D kategori mobil (*Car*) tingkat kesulitan Sedang (*Moderate*), survei ini merangkum performa beberapa arsitektur pelopor:
- **MV3D (Multi-View 3D Networks):** Model fusi awal yang memproyeksikan awan titik LiDAR ke pandangan mata burung (BEV) dan pandangan depan, lalu menggabungkannya dengan citra kamera menggunakan skema *middle fusion*. Model ini mencapai presisi rata-rata (*Average Precision* atau AP) 3D sebesar $62,35\%$ untuk kategori mobil pada tingkat kesulitan *Moderate*.
- **AVOD-FPN (Aggregate View Object Detection dengan Feature Pyramid Network):** Mengembangkan RPN (*Region Proposal Network*) yang secara bersamaan mengekstrak proposal dari fitur resolusi tinggi BEV LiDAR dan citra kamera. Model ini meningkatkan AP 3D secara signifikan menjadi $71,88\%$ pada tingkat kesulitan *Moderate*.
- **F-PointNet (Frustum PointNet):** Model fusi asimetris yang pertama-tama mendeteksi objek dalam gambar 2D untuk menghasilkan wilayah kerucut (*frustum*) 3D pada awan titik LiDAR, kemudian menerapkan PointNet untuk melokalisasi kotak pembatas 3D. Model ini memperoleh performa AP 3D berkisar di angka $70,39\%$ untuk kategori mobil pada tingkat kesulitan *Moderate*.

Untuk dataset nuScenes yang menyertakan data kamera, LiDAR, dan radar dengan jangkauan $360^{\circ}$, survei ini menyoroti bahwa integrasi radar sangat meningkatkan deteksi kecepatan objek (mengurangi galat kecepatan hingga di bawah $0,2\text{ m/s}$) dan memperluas ketahanan deteksi hingga jarak $100\text{ meter}$ dalam kondisi cuaca buruk. Namun, visualisasi radar yang sangat derau menghasilkan lebih banyak positif palsu (*false positives*), yang memerlukan penyaringan berbasis ambang batas probabilitas yang ketat.

## Kelebihan dan Keterbatasan
**Kelebihan:**
Makalah survei oleh Feng dkk. ini memiliki keunggulan besar dalam meletakkan dasar taksonomi yang solid dan terstandardisasi bagi komunitas riset kendaraan otonom. Dengan mendefinisikan dimensi *what*, *when*, dan *how* secara sistematis, makalah ini berhasil memperjelas batasan istilah-istilah fusi yang sebelumnya membingungkan. Selain itu, ulasan yang komprehensif tentang sensor radar memberikan wawasan berharga tentang modalitas sensor yang sering diabaikan dalam riset akademik konvensional yang terlalu berfokus pada kamera-LiDAR saja. Platform interaktif yang disediakan penulis juga sangat membantu navigasi literatur secara dinamis.

**Keterbatasan:**
Secara konseptual, sebagai sebuah ulasan yang terbit pada tahun 2021, ulasan ini belum mencakup perkembangan pesat arsitektur berbasis *transformer* multimodal dan representasi ruang terpadu BEV (seperti BEVFormer atau BEVDet) yang mendominasi sejak tahun 2022. Dari sisi praktis, analisis komparatif kuantitatif dalam ulasan ini sangat bergantung pada metrik yang dilaporkan oleh masing-masing makalah asli. Hal ini dapat menimbulkan bias karena perbedaan konfigurasi perangkat keras pelatihan, parameter optimalisasi, serta partisi data uji lokal yang tidak seragam di antara metode-metode yang dibandingkan.

## Kaitan dengan Bab Lain
Makalah survei ini bertindak sebagai jembatan taksonomi yang menghubungkan berbagai teknologi fusi yang dibahas pada bab-bab lain dalam klaster fusi multimodal.

Secara struktural, survei ini merangkum dan mengevaluasi model-model yang memanfaatkan ekstraksi fitur dasar dari bab-bab awal:
- Jaringan ekstraksi fitur mendalam seperti **ResNet** ([147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)) digunakan secara luas sebagai tulang punggung untuk modalitas kamera dalam skema fusi *middle* maupun *late*.
- Untuk pengolahan awan titik LiDAR 3D, representasi berbasis titik yang diulas dalam survei ini mewarisi teknologi dari **PointNet** ([148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)), yang menjadi dasar bagi model seperti F-PointNet.
- Mekanisme fusi canggih yang dibahas dalam sumbu *how to fuse* survei ini banyak mengadopsi modul atensi saluran dan spasial seperti **CBAM** ([149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)) untuk menimbang kontribusi relatif fitur dari masing-masing modalitas sensor secara dinamis.

Di sisi lain, survei Feng dkk. ini melengkapi cakupan survei historis lainnya seperti:
- **Object Detection in 20 Years (Zou dkk.)** ([151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)) yang memberikan tinjauan evolusi deteksi objek 2D secara luas selama dua dekade.
- **Deep Multimodal Learning A Survey** ([152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)) yang berfokus pada teori fusi multimodal umum lintas domain (audio, teks, citra).
- **Survei RGB-D SOD (Zhou dkk.)** ([153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)) dan **Survei Dataset RGB-D (Lopes dkk.)** ([154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)) yang membatasi analisisnya pada fusi tingkat kedalaman RGB-Depth untuk persepsi dalam ruang (*indoor*), sedangkan survei Feng dkk. meluaskan cakupannya ke ranah luar ruang (*outdoor*) berkendara otonom dengan tambahan sensor LiDAR dan radar.

## Poin untuk Sitasi
```bibtex
@article{feng2021multimodalsurvey,
  author={Feng, Di and Haase-Sch{\"u}tz, Christian and Rosenbaum, Lars and Hertlein, Heinz and Glaeser, Claudius and Timm, Fabian and Wiesbeck, Werner and Dietmayer, Klaus},
  journal={IEEE Transactions on Intelligent Transportation Systems}, 
  title={Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges}, 
  year={2021},
  volume={22},
  number={3},
  pages={1341-1360},
  doi={10.1109/TITS.2020.2971562}
}
```

**Ringkasan untuk Sitasi:**
Feng dkk. (2021) menyajikan survei komprehensif mengenai deteksi objek dan segmentasi semantik berbasis pembelajaran mendalam dengan fusi multimodal (kamera, LiDAR, dan radar) untuk kendaraan otonom. Penulis merumuskan taksonomi fusi berdasarkan dimensi waktu (*early/middle/late fusion*), representasi, dan metode penggabungan, serta menguraikan tantangan krusial seperti kalibrasi lintas sensor dan variasi cuaca buruk. Publikasi ini menjadi referensi kanonik untuk memahami klasifikasi arsitektur persepsi multi-sensor.

**Catatan Verifikasi:**
- Angka presisi rata-rata (AP) untuk model MV3D (62,35% AP), AVOD-FPN (71,88% AP), dan F-PointNet (70,39% AP) merujuk pada hasil deteksi objek 3D kategori mobil (*Car*) tingkat kesulitan *Moderate* pada dataset KITTI.
- Klaim fusi radar mampu menekan galat kecepatan hingga di bawah 0,2 m/s diverifikasi berdasarkan evaluasi pada dataset nuScenes dalam makalah asli.
