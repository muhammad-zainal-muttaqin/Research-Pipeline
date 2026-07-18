# 154 - A Survey on RGB-D Datasets

## Metadata Ringkas

| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `lopes2022rgbddatasets` |
| Judul Asli | A Survey on RGB-D Datasets |
| Penulis | Lopes, Alexandre; Souza, Roberto; Pedrini, Helio |
| Tahun | 2022 |
| Venue | Computer Vision and Image Understanding |
| Tema | Fusi Multimodal |

## Tautan Akses

- **DOI Resmi**: https://doi.org/10.1016/j.cviu.2022.103489
- **Arsip arXiv**: https://arxiv.org/abs/2201.05761
- **Repositori Awesome GitHub**: https://github.com/alelopes/awesome-rgbd-datasets

## Gambaran Umum

Makalah ini menyajikan survei komprehensif mengenai lanskap dataset *red, green, blue plus depth* (RGB-D) dalam penelitian komputer visi. Penulis mengidentifikasi dan menganalisis 231 dataset RGB-D publik yang dapat diakses, kemudian mengelompokkannya ke dalam tiga kategori utama: adegan/objek (*scene/objects*), tubuh manusia (*human body*), dan aplikasi medis (*medical applications*). Selain itu, survei ini memetakan teknologi sensor kedalaman yang digunakan untuk merekam data serta menganalisis pengaruh jenis sensor terhadap kemampuan generalisasi model pembelajaran mesin.

Hasil utama dari penelitian ini adalah penyediaan katalog terstruktur yang didukung oleh repositori dinamis berbasis web. Katalog ini berfungsi sebagai panduan praktis bagi peneliti dalam memilih dataset yang sesuai dengan kebutuhan riset. Dengan mendokumentasikan spesifikasi sensor, skala data, dan jenis anotasi secara terstandardisasi, makalah ini membantu mengatasi tantangan fusi sensor multimodal, khususnya masalah kesenjangan domain (*domain gap*) lintas-sensor pada tugas estimasi kedalaman monokuler (*monocular depth estimation*).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum publikasi survei ini, perkembangan penelitian berbasis sensor RGB-D mengalami hambatan akibat fragmentasi data yang tinggi. Ratusan dataset dikembangkan secara independen menggunakan perangkat keras dan protokol berbeda, tanpa adanya panduan pemetaan terpadu. Hal ini menyulitkan peneliti dalam memilih data latih yang optimal.

Terdapat tiga masalah utama yang melatarbelakangi penulisan survei ini:
- **Kesulitan Penemuan Dataset (*Dataset Discovery*)**: Banyak dataset dengan informasi kedalaman tidak mencantumkan kata kunci "RGB-D" atau "depth" pada judul atau abstrak mereka (misalnya dataset mengemudi otonom KITTI). Akibatnya, pencarian literatur berbasis kata kunci konvensional cenderung melewatkan dataset kunci tersebut.
- **Kesenjangan Karakteristik Sensor Kedalaman**: Perangkat keras perekam data kedalaman bekerja dengan prinsip fisika yang berbeda-beda. Perbedaan ini menghasilkan tingkat kerapatan data, rentang operasional, dan jenis derau yang berbeda secara signifikan, yang memengaruhi ketahanan model yang dilatih di atasnya.
- **Ketiadaan Taksonomi Terstandardisasi**: Belum terdapat klasifikasi formal yang memetakan dataset RGB-D berdasarkan tujuan aplikasinya. Hal ini mempersulit analisis mengenai domain mana yang telah memiliki data melimpah dan mana yang masih kekurangan representasi data kedalaman.

## Ide Utama

Gagasan inti dari makalah ini adalah membangun kerangka kerja peninjauan literatur yang komprehensif menggunakan metodologi pencarian mundur (*backward snowballing*) untuk melacak seluruh dataset RGB-D publik yang pernah dirilis secara global. Ide utama ini diwujudkan melalui tiga kontribusi:
- **Penyusunan Taksonomi Hierarkis**: Mengelompokkan dataset ke dalam tiga kategori utama (adegan/objek, tubuh manusia, dan medis) serta membaginya ke dalam subkategori tugas spesifik.
- **Standardisasi Atribut Evaluasi**: Menilai setiap dataset menggunakan delapan atribut metadata standar (termasuk jenis sensor, nama perangkat, skala data, dan modalitas ekstra) untuk memberikan gambaran kualitas data yang objektif.
- **Penyediaan Repositori Dinamis**: Membuat repositori terbuka di GitHub (`awesome-rgbd-datasets`) yang diperbarui secara berkala oleh komunitas untuk menjaga relevansi survei ini dari waktu ke tempo.

## Cara Kerja Langkah demi Langkah

Metodologi survei ini dijalankan melalui serangkaian tahapan sistematis untuk menyaring dan mengklasifikasikan dataset RGB-D.

### Metodologi Pencarian Backward Snowballing
Penulis menggunakan pendekatan *backward snowballing* untuk meminimalkan risiko terlewatnya dataset penting akibat ketidakcocokan kata kunci. Proses dimulai dengan mengevaluasi daftar pustaka dari makalah-makalah survei terdahulu. Dari penelusuran terhadap 1.513 naskah ilmiah, penulis mengidentifikasi 305 makalah kandidat yang memuat dataset dengan informasi kedalaman.

Alur penyaringan dataset digambarkan sebagai berikut:

```
               [ 1.513 Makalah Ilmiah di Database Awal ]
                                  │
                                  ▼ (Backward Snowballing)
               [  305 Makalah Kandidat Dataset RGB-D   ]
                                  │
      ┌───────────────────────────┴───────────────────────────┐
      ▼ (Kriteria Inklusi)                                    ▼ (Kriteria Eksklusi)
  - Fokus pada estimasi kedalaman                        - Bukan Bahasa Inggris
  - Menggunakan sensor depth,                            - Dataset bersifat privat
    stereo, atau sintetis                                - Hasil tidak valid
  - Data dapat diakses publik                            - Makalah duplikat
      │                                                       │
      └───────────────────────────┬───────────────────────────┘
                                  ▼
               [  231 Dataset Terpilih dan Dapat Diakses   ]
```

### Penerapan Kriteria Inklusi dan Eksklusi
Setelah mengidentifikasi 305 kandidat, penulis menerapkan enam kriteria penyaringan. Dataset harus dapat diakses secara publik, disajikan dalam makalah berbahasa Inggris, dan menyajikan bukti validitas hasil eksperimen. Dataset yang bersifat privat atau naskah duplikat yang menyajikan variasi minor dari dataset yang sama langsung dieleminasi. Melalui penyaringan ini, diperoleh 231 dataset final.

### Skema Taksonomi Hierarkis Dataset RGB-D
Seluruh dataset yang lolos seleksi diklasifikasikan berdasarkan struktur taksonomi hierarkis berikut:

```
                           [ DATASET RGB-D ]
                                  │
      ┌───────────────────────────┼───────────────────────────┐
      ▼                           ▼                           ▼
[ Scene/Objects ]              [ Body ]                  [ Medical ]
      │                           │                           │
      ├─ SLAM / Odometry /        ├─ Aktivitas Manusia        └─ Aplikasi Medis
      │  Rekonstruksi             │  (Full Body)                 & Healthcare
      │  (KITTI, ScanNet)         │  (NTU RGB+D)                 (Anatomi,
      │                           │                              Surgical)
      ├─ Segmentasi & Info        └─ Gestur / Tubuh
      │  Tambahan                    Parsial
      │  (NYUv2, Scene Flow)         (NYU Hand Pose)
      │
      ├─ Depth Data Only
      │
      └─ Lain-lain (Tracking,
         Reflection, Light Field)
```

- **Adegan/Objek (*Scene/Objects*)**: Berfokus pada pemetaan lingkungan spasial dan objek individual. Subkategorinya meliputi *SLAM, Odometry, atau Rekonstruksi* (contoh: KITTI, ScanNet), *Segmentasi dan Informasi Tambahan* (contoh: NYU Depth v2), *Hanya Data Kedalaman*, dan *Lain-lain* (seperti pelacakan objek).
- **Tubuh Manusia (*Body*)**: Berfokus pada data yang berpusat pada manusia, terbagi menjadi *Aktivitas Manusia* (contoh: NTU RGB+D) dan *Gestur / Bagian Tubuh Parsial* (contoh: NYU Hand Pose Dataset).
- **Aplikasi Medis (*Medical*)**: Kategori khusus untuk dataset yang merekam anatomi pasien, rekonstruksi bedah, atau pemantauan kesehatan rehabilitatif.

### Karakteristik Sensor Kedalaman
Survei ini membagi teknologi sensor kedalaman menjadi lima kelompok teknologi:
- **Cahaya Terstruktur (*Structured Light*)**: Proyektor memancarkan pola inframerah acak yang telah diketahui (contoh: Microsoft Kinect v1). Sensor menghitung deformasi pola untuk menentukan kedalaman melalui triangulasi. Akurat untuk jarak dekat (0,5–3,5 meter) di dalam ruangan (*indoor*), tetapi gagal di bawah sinar matahari akibat interferensi inframerah eksternal.
- **Waktu Terbang (*Time-of-Flight* - ToF)**: Mengukur waktu tempuh pulsa cahaya dari sensor ke objek dan kembali ke penangkap cahaya (contoh: Microsoft Kinect v2). Kecepatan bingkai (*frame rate*) tinggi dan kesalahan konstan terhadap jarak, tetapi rentan terhadap interferensi jalur ganda (*multipath interference*) di sudut ruangan.
- **Deteksi dan Pengukuran Cahaya (*LiDAR*)**: Menggunakan pulsa laser yang berputar untuk memindai jarak jauh hingga ratusan meter (contoh: Velodyne). Sangat tahan terhadap variasi cahaya luar ruangan (*outdoor*), tetapi menghasilkan peta kedalaman yang sangat renggang (*sparse*).
- **Kamera Stereo (*Stereo Camera*)**: Menggunakan dua lensa kamera pasif dengan jarak basis (*baseline*) yang diketahui untuk menghitung disparitas piksel (contoh: ZED Stereo). Murah dan bekerja baik di luar ruangan, tetapi memerlukan komputasi pencocokan piksel yang berat dan gagal pada permukaan homogen tanpa tekstur.
- **Data Sintetis (*Synthetic Data*)**: Menggunakan mesin grafis 3D (seperti CARLA) untuk merender citra RGB beserta informasi kedalaman murni (*ground truth* bebas derau). Menyediakan anotasi sempurna tanpa keterbatasan fisik, namun memiliki kesenjangan domain (*domain gap*) yang tinggi dengan citra dunia nyata.

### Atribut Metadata Evaluasi Dataset
Penulis mencatat delapan atribut metadata standar untuk setiap dataset: Tahun (*Year*), Tipe Adegan (*Scene Type*), Tipe Sensor (*Sensor Type*), Nama Sensor (*Sensor Name*), Modalitas Data (*Data Modalities*), Data Tambahan (*Extra Data*), Citra/Adegan (*Images/Scenes*), dan Aplikasi (*Application*).

## Eksperimen dan Hasil

Karena makalah ini bertipe survei, evaluasi eksperimental dilakukan melalui analisis statistik terhadap distribusi 231 dataset yang dikatalogkan.

Analisis statistik menunjukkan beberapa tren penting:
- **Dominasi Adegan Dalam Ruangan**: Lebih dari 60% dataset adegan/objek direkam dalam ruangan menggunakan sensor cahaya terstruktur dan ToF karena kemudahan operasional sensor inframerah aktif tanpa gangguan matahari.
- **Peningkatan Dataset Luar Ruangan**: Seiring populernya riset kendaraan otonom, dataset berbasis LiDAR mengalami pertumbuhan signifikan setelah tahun 2015, dicirikan oleh jarak jangkauan yang jauh (hingga 120 meter) tetapi memiliki kerapatan yang rendah (*sparse*).
- **Tantangan Generalisasi Model**: Survei merangkum hasil eksperimen estimasi kedalaman monokuler dari berbagai literatur, menunjukkan bahwa model yang dilatih pada dataset dengan sensor tertentu (misalnya NYU Depth v2 yang berbasis cahaya terstruktur) mengalami penurunan performa metrik *mean Absolute Relative error* (AbsRel) sebesar 40% hingga 60% ketika diuji langsung pada dataset dengan sensor berbeda (seperti KITTI yang berbasis LiDAR). Hal ini menegaskan pentingnya pemilihan dataset yang representatif terhadap sensor target sebelum pelatihan model.

## Kelebihan dan Keterbatasan

Secara objektif, makalah survei ini memiliki aspek kekuatan dan kelemahan berikut:

### Kelebihan
- **Penyaringan Sistematis**: Metode *backward snowballing* efektif menemukan dataset tersembunyi yang tidak menggunakan kata kunci standar pada judul mereka, menghasilkan katalog yang lengkap.
- **Taksonomi Komprehensif**: Pembagian ke dalam tiga kategori utama mencakup hampir seluruh spektrum aplikasi fusi multimodal yang relevan bagi akademisi maupun praktisi.
- **Keberlanjutan Repositori**: Repositori dinamis GitHub memberikan nilai tambah jangka panjang untuk memperbarui katalog secara dinamis.

### Keterbatasan
- **Ketiadaan Standardisasi Format**: Dari sisi rekayasa data, survei ini tidak menyediakan alat bantu atau *API* terpadu untuk memuat data. Peneliti tetap harus menulis kode parser unik karena format penyimpanan data kedalaman yang bervariasi (PNG 16-bit, NumPy, PLY/PCD).
- **Ketiadaan Evaluasi Empiris Mandiri**: Secara konseptual, analisis generalisasi model lintas-sensor hanya merujuk pada hasil literatur lain. Penulis tidak melakukan eksperimen pembanding secara mandiri (*independent benchmarking*) menggunakan satu arsitektur model standar untuk mengevaluasi kualitas informasi kedalaman antar-dataset secara adil.

## Kaitan dengan Bab Lain

Bab ini berfungsi sebagai peta komprehensif yang menjembatani sumber data untuk berbagai arsitektur dan metodologi fusi multimodal yang dibahas dalam bab-bab lain:
- **Backbone Ekstraksi**: Jaringan ekstraksi fitur pada [147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md) dilatih menggunakan dataset segmentasi RGB-D (seperti NYU Depth v2) untuk mengekstrak fitur spasial citra kedalaman.
- **Pemrosesan Data Spasial 3D**: Representasi awan titik (*point cloud*) yang diproses oleh [148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md) diperoleh dari konversi data kedalaman dari sensor LiDAR atau kamera stereo yang dikategorikan dalam survei ini.
- **Optimalisasi Fusi Fitur**: Modul atensi dalam [149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md) digunakan untuk menyeimbangkan kontribusi fitur RGB dan *depth map* secara adaptif pada dataset fusi multimodal.
- **Sintesis Metodologi Algoritma**: Survei deteksi objek dan segmentasi pada [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md) sangat bergantung pada dataset luar ruangan (KITTI dan Waymo) yang karakteristik sensornya (LiDAR vs. stereo) dianalisis secara fisik dalam bab ini.
- **Evolusi Deteksi Objek**: Perkembangan teknologi deteksi objek selama dua dekade yang dirangkum dalam [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md) menunjukkan bahwa transisi dari deteksi 2D ke 3D didorong oleh ketersediaan dataset RGB-D berskala besar.
- **Kerangka Kerja Fusi Teoritis**: Klasifikasi fusi yang didefinisikan dalam [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md) diimplementasikan secara praktis pada dataset-dataset yang tercatat dalam katalog ini.
- **Deteksi Objek Menonjol**: Survei mengenai deteksi objek menonjol berbasis kedalaman pada [153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md) menganalisis metode-metode yang dilatih menggunakan dataset spesifik yang berada di bawah subkategori *Scene/Objects* dalam taksonomi Lopes dkk.

## Poin untuk Sitasi

Kunci BibTeX untuk merujuk makalah ini adalah:

```bibtex
@article{lopes2022rgbddatasets,
  title={A survey on RGB-D datasets},
  author={Lopes, Alexandre and Souza, Roberto and Pedrini, Helio},
  journal={Computer Vision and Image Understanding},
  volume={222},
  pages={103489},
  year={2022},
  publisher={Elsevier}
}
```

*Pernyataan Sitasi yang Disarankan*:
Lopes dkk. (2022) menyajikan survei komprehensif terhadap 231 dataset RGB-D publik yang diklasifikasikan ke dalam tiga domain utama: adegan/objek, tubuh manusia, dan medis. Makalah ini memetakan lima teknologi sensor kedalaman (cahaya terstruktur, *time-of-flight*, LiDAR, stereo, dan sintetis) serta menyoroti tantangan generalisasi lintas-sensor pada model pembelajaran mesin untuk estimasi kedalaman.

*Catatan Verifikasi*:
- Jumlah dataset dalam naskah jurnal cetak asli adalah 231 dataset (berkembang dari 203 dataset pada versi draf awal). Sebelum mengutip jumlah dataset terbaru, harap periksa pembaruan pada repositori GitHub dinamis mereka (`awesome-rgbd-datasets`).
- Detail kriteria inklusi dan eksklusi penyaringan naskah terdokumentasi lengkap pada Tabel 2 dalam publikasi asli.
