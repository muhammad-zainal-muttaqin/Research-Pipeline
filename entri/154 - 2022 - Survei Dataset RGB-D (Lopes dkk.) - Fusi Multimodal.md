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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
ABSTRACT RGB-D data is essential for solving many problems in computer vision. Hundreds of public RGB-D datasets containing various scenes, such as indoor, outdoor, aerial, driving, and medical, have been proposed. These datasets are useful for different applications and are fundamental for addressing classic computer vision tasks, such as monocular depth estimation. This paper reviewed and categorized image datasets that include depth information. We gathered 231 datasets that contain accessible data and grouped them into three categories: scene/objects, body, and medical. We also provided an overview of the different types of sensors, depth applications, and we examined trends and future directions of the usage and creation of datasets containing depth data, and how they can be applied to investigate the development of generalizable machine learning models in the monocular depth estimation field. © 2022 Elsevier Ltd. All rights reserved.

1. Introduction Depth is a critical information for many computer vision and image analysis applications. For example, it has been applied for tasks such as synthetic object insertion in computer graphics (Luo et al., 2020), robotic grasping (Lenz et al., 2015) automatic 2D to 3D conversion in film (Xie et al., 2016), robotassisted surgery (Stoyanov et al., 2010), and autonomous driving (Levinson et al., 2011). Despite using depth sensors that capture the distance information, researchers also use stereo vision matching to infer it, especially for its condensed size and cost. Lately, deep learning methods are being used to produce more precise and dense depth maps. For example, they can improve finer-grained details (Miangoleh et al., 2021), produce dense maps from sparse inputs (Uhrig et al., 2017), and refine depth for mirror surfaces (Tan et al., 2021a). An important field of study for depth is monocular depth estimation, especially because it does not require using depth sensors, reducing the size and cost of computer vision systems’ se-

tups. Also, it can be applied to existing monocular systems, that comprise the majority of image capturing systems available. For instance, Light Detection And Ranging (LiDAR) scanners usually cost thousands of dollars, and their cost and weight can be impractical for many small drone applications. As a result of the extensive range of applications of depth, a considerable number of datasets include distance measurements of points of the scene they acquire. These datasets are collected using different sensors in distinct scenes for applications such as Simultaneous Localization and Mapping (SLAM) (Sturm et al., 2012), Reconstruction (Dai et al., 2017), Object Segmentation (McCormac et al., 2017), and Human Activity Recognition (Zhang et al., 2016a). With the increasing number and diversity of datasets, researchers were able to explore more generalistic forms of depth estimation, leading to techniques focused on zero-shot cross-dataset depth estimation (Li and Snavely, 2018a; Xian et al., 2020a; Ranftl et al., 2021a, 2020). The idea is to produce powerful methods able to estimate depth for inthe-wild scenes, increasing the range of applications for depth estimation. The main contribution of this paper is to categorize and summarize the existing datasets with depth data. We propose a survey that can be used by researchers of both individual applications and general systems. While there are good reviews of RGB-D datasets (Firman, 2016; Cai et al., 2017), the most

2 recent one was published in 2017, and datasets have evolved both in complexity and size since then. Our survey presents a comprehensive literature review on more than 200 publicly available datasets included from an initial list of more than 300 datasets. Nearly half of the public datasets were published in 2017 or after, therefore, not included in any other review. We also made this work available on a website1 to facilitate the filtering by application, scene type, sensor, and year. The remainder of this paper is structured as follows. In the next section, we discuss and categorize depth sensors, explaining the main differences and applications for each category. In Section 3, we present the methodology used to perform the literature review. In Section 4, we present the datasets divided into categories, describing the most influential datasets for each category and presenting the rest in tables. In Section 5, we present tendencies and discuss future directions for RGB-D data usage. Finally, we provide a summary of the field and discuss how the area is evolving in Section 6. 2. Sensors Range (or depth) data is crucial for understanding the 3D scene projected onto a 2D plane forming an image. There are multiple ways to obtain such information, either using a depth sensor or estimating depth. A depth sensor is a device that provides the distance from the sensor to an element in the scene, although it is possible to collect distance information using two or more RGB cameras from a scene. We define as Stereo Camera Sensing, all systems formed by two or more cameras. Therefore, light field cameras are also included here. Previously, authors proposed distinct divisions for the types of sensors (Fisher and Konolige, 2008; Choi, 2019). In this survey, we use a categorization of depth sensors inspired by Choi (2019)’s work. We divide the sensors into the following categories: Structured Light, Time-of-Flight (TOF), Light Detection and Ranging (LiDAR), and Stereo Camera Sensing. We display examples of each category in Figure 1. Ultrasonic and Radar sensors also produce distance information, but they are out of the scope of this work because they are rarely used to produce depth information associated with RGB data. We detail each one of the sensors categories in the following sub-sections and show the differences of these types and possible application scenes in Table 1. 2.1. Structured Light Structured Light sensors (also called Active Stereo sensors) rely on a projector of light captured by a camera. The simplest way to achieve such a goal is to project a point with a device and capture this point in the scene with the camera. The depth of this point can be measured by a technique called Triangulation. For estimating depth, it is necessary to find the position of the projected point in the image plane, have the distance between the camera and the light projector, the camera’s internal parameters, and the position in space of the projector. With this

information, it is possible to create a triangle and calculate the height of the triangle formed by the camera, projector, and illuminated scene point to determine the distance. The strategy of projecting points would be slow in practice since it is necessary to project a point for every position that is represented as a pixel in the image. A more efficient strategy is to project the light as a stripe that associated with different coding strategies, such as the Binary Coded Structured Light strategy, can reduce the number of frames necessary to produce a full depth map. It can also be coded with RGB lights. Details about different codification strategies are discussed by Salvi et al. (2004). Most Structured Light sensors do not work under direct sunlight since they rely on light projection in a scene. Therefore, they are usually suitable for indoor scene applications. Researchers have proposed strategies to overcome challenging light conditions (O’Toole et al., 2015), and now these sensors appear in smartphones for face identification systems for both indoor and outdoor scenes. They typically have a low range limit, not going further than 10 meters. Examples of this type of sensor include Matterport, Kinect v1, and RealSense SR300 cameras. 2.2. Time-of-Flight TOF sensors estimate the distance of an object in the scene to a sensor by measuring the time it takes for an emitted light to be received by the sensor. Therefore, TOF sensors rely on the time that a light wave takes to go to a point in a scene and to be reflected to a sensor. The concept is barely the same as the Ultrasonic and Radar Sensors, but here light is used as the emitted signal. There are multiple strategies for capturing the time-of-flight of light. The most straightforward strategy is using a technique called Pulse Modulation, where a very fast pulse of light is emitted and then received by the sensor. The time delay between the emitted light pulse and the received light pulse is used to compute the distance of the object in the scene. ContinuousWave Modulation is another strategy, where the light is modulated by its intensity, and the distance is measured by calculating the shift in phase of the original emitted light and the received light. TOF sensors generally are compromised under strong sunlight conditions (Kazmi et al., 2012), making this sensor more commonly applied to indoor scenes. Existing studies try to overcome the effect under intense background light (Buttgen and Seitz, 2008) and to reduce the measurement uncertainty under such conditions. Examples of this type of sensor include Kinect v2 (Xbox One sensor), SoftKinetic DS 325, and RIEGL VZ-400. 2.3. LiDAR LiDAR sensors use the same idea of measuring the time that an emitted light is received by a sensor, but they rely on one or multiple laser beams (concentrated light) to produce depth measurements of points in the scene, and the device usually has a rotating mirror to generate 360° scans of a scene. Hence, LiDAR sensors produce point clouds of a scene, not a dense

3 Table 1: Sensors overview comparing the usual application, distances and sparsity for each type of sensor.

depth map of it. They rely on focused laser beams, which allow them to collect distance measurements as far as a few kilometers. LiDAR sensor models have different specifications (e.g., resolution, scans per second, and distance accuracy), and some scans are built in a multilayer (multiple laser beams) configuration, allowing them to measure not only in a 360° plane of the sensor but in 3D. LiDAR measurement accuracy is usually independent of distance, although some models can fail in adverse weather conditions, such as dense fogs and turbulent snow (Jokela et al., 2019). Each LiDAR point also includes the intensity measurements, which can be interpreted as a measurement of reflectivity of the point that the light hit. This value is suitable for many applications, such as vegetation cover understanding and tunnel damage detection (Kashani et al., 2015), giving LiDAR additional information that other types of sensors do not produce. LiDAR sensors emit light; therefore, they work in difficult lighting conditions, such as dark environments. They are suitable for indoor and outdoor application scenes, but the available models are usually limited to specific applications, such as aerial measurements, outdoor/driving applications, and small indoor spaces depth estimation. Examples of such types of sensors include Velodyne Sensors, Faro Focus 3D Laser, and SICK LMS-511. 2.4. Stereo Camera Sensing We define here Stereo Camera Sensing (SCS) as any system formed by two or more image sensors or lenses used to produce a Depth Map of a scene. Hence, simplistic pairs of cameras and complex light field systems composed by multiple microlenses are both identified in the same category. A straightforward strategy to measure depth from two or more cameras is Triangulation. The Triangulation idea is the same as applied in Structured Light sensors, but using a camera instead of a projector. The idea is that finding the position of a pixel in the image plane of camera A projected from a point P in the space, and the position of a pixel projected by the same point P in camera B, it is possible to find the depth of that point in a scene with the intrinsic parameters of the camera. After finding both lines projected in both cameras from point P, it is only necessary to know the distance between the two cameras (baseline distance) and internal parameters of the cameras to know the depth of the point P. A limitation of this strategy occurs when the point of interest has no texture. For instance, it is practically impossible to determine which point of a smooth painted wall observed in the image projected by camera A is equivalent to the image projected by camera B. Therefore, it is difficult to determine a point’s

depth with acceptable accuracy without the correspondence of the pixels in both image planes. Recently, Deep Learning based methods have tried to address this limitation, increasing the accuracy of the estimation (Zbontar and LeCun, 2015). Examples of such types of sensors include light field cameras and ZED cameras. 3. Methodology A literature review should synthesize previous knowledge, identify biases and gaps in the literature (Rowe, 2014). Since our study aims to describe, categorize, and identify future trends for RGB-D datasets, we defined a non-conventional methodology to find the related papers. Instead of defining search terms to find the papers directly, we collected datasets using backward snowballing. The premise is that many datasets containing depth data do not have depth estimation as their primary goal, as in KITTI Dataset (Geiger et al., 2013). Therefore, defining search strings that could find depth datasets using generalist terms would result in numerous false-positive results. For instance, the search string RGB-D OR Depth AND Dataset searching in abstract, keywords, or title brings more than 23 thousand results in Scopus. Moreover, if we define a complex composed search string to filter the results, we would miss many datasets in the search. As monocular depth estimation, salient object detection, and action recognition are prominent fields in the area, we defined the following search string to perform backward snowballing: (("single image" OR monocular) AND depth AND estimation) OR (("Salient Object Detection" OR "Action Recognition") AND RGB-D). The terms “monocular” and “single image” are applied mainly for monocular depth estimation but are also used for stereo trained systems, depth completion, and other applications. We conducted the review in Scopus and Google Scholar search engines. In Scopus, we revised all papers from January 1st, 2016, through August 31st, 2021. From Google Scholar, we followed the same dates, but we also included a stop criterion. If we found one search page without relevant items, we would end the year’s search. The inclusion of Google Scholar is justified because many relevant papers are published in arXiv. Consequently, those could also be included in this work. The exclusion and inclusion criteria for papers are defined in Table 2. These criteria are applied to the papers found using the previous search term. After excluding papers, backward snowballing was applied to find the datasets used/described by the remaining works. Initially, we reviewed 2,119 papers, which led to 374 dataset candidates. We also applied an exclusion criterion to these candidates, and only papers with active project

Fig. 1: Examples of depth data with image (first row) and depth (second row) of the following sensors: (a) Structured Light from NYUv2 (Silberman et al., 2012), (b) TOF from AVD (Ammirato et al., 2017), (c) LiDAR from KITTI (Geiger et al., 2013), and (d) Stereo Camera Sensing from ReDWeb (Xian et al., 2018), where the authors compute correspondence maps by using optical flow. Table 2: Inclusion and Exclusion Criteria.

Papers that discuss depth estimation Papers using depth sensors, stereo image sensing, or synthetic data Papers not written in English Papers exclusively using private datasets Papers not presenting minimal evidence of valid results Duplicated paper/report. We kept the most complete one

websites, contact information to download the dataset, or direct download link were included. Hence, the final list of datasets to be included was reduced to 231 datasets. 4. Datasets In recent years, many datasets have been created using the sensors or stereo vision sensing presented in the previous section. In addition to datasets using real data, this paper also includes datasets containing synthetic data. These were created mainly by simulation systems and often presented extra data such as semantic segmentation and 3D object detection bounding boxes. We divided the selected datasets into three different categories and six different sub-categories representing different application areas. The taxonomy tree is available in Figure 2. The categories represent the intended application of the dataset. In the first level, we identify datasets that are mainly interested in Scenes/Objects, Human Body, or Medical Applications. The following sub-sections explore each application area, and list all of them in each sub-category’s table. We also detail three, two or one datasets for each sub-category, based on the total number of datasets of each sub-category. If we detail three papers, the two first ones are the most cited papers that contain complementary scenarios. For example, KITTI Dataset and ScanNet Dataset contain street and indoor scenes, respectively. The third paper is the most cited paper published in 2017 or later. If we detail two papers, these are the most cited ones that contain complementary scenarios, and if we detailed one paper, it is the most cited in the sub-category.

4.1. Scene/Objects In this category, we grouped all datasets generally intended to expose scenes, individual objects, or groups of objects containing or not humans.. Therefore, datasets that reconstruct scenes/objects, segment elements of a scene, salient objects using depth, and contain exclusively depth maps are subcategorized here. We created an “Other” sub-category to accommodate datasets that did not fit into these previous subcategories. Some papers explore multiple applications, primarily synthetic datasets, since they can create reconstruction and segmentation data directly using simulation environments. These papers are presented in one of their application areas to reduce redundancy. The only exception is for datasets of “SLAM, Odometry, or Reconstruction” and “Segmentation or Other Extra Information” sub-categories that are presented together in Table 5, since this combination is very frequent for datasets. 4.1.1. SLAM, Odometry, or Reconstruction This sub-category contains multiple types of applications, however, all of them have a common characteristic: they present extra information that makes possible to recreate in any detail level, a 3D scene. For SLAM and odometry related papers, they typically present camera pose information, giving position and orientation of the capturing apparatus of each frame/image. We treated odometry differently from SLAM since odometry essentially aims to estimate the path of the camera, and SLAM tries to obtain a consistent trajectory and scene map of the camera (Yousif et al., 2015). All collected datasets that contain data exclusively for SLAM, Odometry, or Reconstruction are shown in Table 3. In general, applications of indoor scenes focus on reconstruction, and external scenes (such as driving scenes) focus on SLAM/odometry. Table 5 also contains datasets of this sub-category, however, with extra annotated information such as semantic segmentation data. Some of the most cited datasets in the field include: KITTI Dataset. Analyzing the datasets presented in this paper, this is the most cited one. The KITTI Dataset consists of a complex system of IMU/GPS, LiDAR scanner, and multiple

5 Dataset

Segmentation or Other Extra Information Depth Data Only Other Fig. 2: Taxonomy for RGB-D datasets. cameras (Geiger et al., 2013). They recorded 6 hours of traffic scenes and, in addition to collecting the information from the sensors, provided data from 3D object detection bounding boxes, optical flow, and visual odometry/SLAM (Geiger et al., 2012). The project was expanded over the years, and the authors included data for tracking, road/lane detection, semantic/instance segmentation, and depth completion. Its depth completion data is composed of 94 thousand depth annotated RGB images (Uhrig et al., 2017) to produce dense depth maps from LiDAR points. This dataset influenced the creation of the synthetic datasets Virtual KITTI (Gaidon et al., 2016) and Virtual KITTI 2 (Cabon et al., 2020). Recently, the KITTI authors released the KITTI-360 Dataset (Liao et al., 2021), which has more cameras, sensors, and more annotated data than the original KITTI Dataset. ScanNet Dataset. ScanNet is an indoor dataset collected using an occipital structure sensor - a structured light sensor similar to Microsoft Kinect v1 (Dai et al., 2017). The authors performed a dense reconstruction and conducted object instance-level annotation of all surfaces in the reconstruction. They also conducted a CAD Model Retrieval and Alignment for the objects in the scenes, which means that a 3D CAD model represented each instance of the annotated object in a scene. This dataset contains 2.5M views in 2,119 different scenes. SunCG Dataset. The project associated with this dataset is focused on semantic scene completion, where from a single point of view, it estimates a complete 3D representation with the semantic label associated with the scene (Song et al., 2017). Instead of estimating the semantic segmentation of visible surfaces, this project aims to predict the occluded space (3D scene representation) and a label for each voxel in the scene. Therefore, it deals with Reconstruction and Segmentation as a unified task. This dataset comprises synthetic data containing an entire

3D model scene (which can be related to reconstruction), with semantic labels associated with it. 4.1.2. Segmentation or Other Extra Information In this sub-category, all datasets have extra information that leads to a better scene understanding. Extra information can be seen as semantic or instance segmentation, 2D or 3D object detection, optical flow, salient object detection, etc. For instance, datasets that explore potential applications for depth estimation algorithms and semantic segmentation, and datasets dedicated to salient object detection were categorized here. The complete list of datasets containing extra information is available in Table 4. We provide the type of extra information for each dataset in the “Extra Data” column. Researchers interested in a specific application, for instance, salient object detection, should use it to filter datasets related to their field of interest. Table 5 also reports datasets for this sub-category, as well as information of “SLAM, Odometry, or Reconstruction” sub-category. Therefore, researchers interested in semantic segmentation datasets may check both tables and refer to the “Extra Data” column to find the datasets that match their interest. Next, three of the most influencing and promising papers for this sub-category are presented. NYUv2. This dataset contains indoor images and is the most cited dataset for this type of scene in the “Segmentation or Other Extra Information” sub-category. It was collected using Microsoft Kinect v1 sensor and is composed of aligned RGB and depth images, labeled data containing semantic segmentation, and raw data (Silberman et al., 2012). This project is a continuation of NYUv1 (Silberman and Fergus, 2011), which uses the same sensor and type of data, but has fewer scenes and total frames. Scene Flow Datasets. This dataset is a collection of three datasets: FlyingThing3D, Monkaa, and Driving. The first is composed of everyday objects flying along random

133 Scenes (almost 20M Images (from Multiple Sensors)

15 Sequences

152 Scenes (12607 Frames)

2 Sequences

20 Sequences (16657 Frames)

795066 Images

10 Scenes (2703 Frames)

24 Scenes

1000 Scenes

17 Distinct Floors From 6 Different Multistorey

4 Scenes (2 Living Room, 2 Offices)

2 Scenes: Statue And Targetbox

KinectFusion (Kinect V1) For Two Scenes. Riegl VZ-400 For Office

25 High-res, 10 Low-res

7 Dataset Name

5 Objects (scenes)

9 Scenes: 4 Scenes Using PrimeSense, 5 Scenes Using Stereo Camera

600 Images (from 125 Objects)

1 Scene

534 Images

2 Scenes (19 Images)

20537 Sequences And Scenes

trajectories (Mayer et al., 2016). The second was created using Blender computer graphics software, based on the information from an animated short film called Monkaa. The third is composed of a street scene. Scene Flow contains only synthetic data for all three datasets and, in addition to depth and RGB frames, the authors also include optical flow, segmentation, and stereo disparity change data. Waymo Perception. This dataset is a street scene dataset composed of RGB and LiDAR labels. It consists of street scenes, and the authors labeled LiDAR using 3D bounding boxes for vehicles, pedestrians, cyclists, and signs (Sun et al., 2020). They also provide RGB images annotations with 2D bounding boxes of vehicles, pedestrians, and cyclists. The 3D bounding boxes also have unique tracking IDs for tracking applications. The Waymo Perception Dataset is composed of 1,150 scenes with 20 seconds of recording each. 4.1.3. Depth Data Only The datasets presented here are for the specific purpose of training depth estimation algorithms. They do not directly provide reconstruction, SLAM, or other information, although some of these applications are direct results of depth estimation. For example, these works explore monocular depth estimation (Cho et al., 2021b), zero-shot depth estimation (Yin et al., 2020), and multi-camera depth estimation (Antequera et al., 2020). We present all papers found specifically for depth estimation in Table 6. All datasets for all categories and sub-categories in this paper also contain depth information as it is an inclusion

criterion for papers to be incorporated to this work. Some relevant papers in this sub-category are: ReDWeb Dataset. This dataset deals with the in-the-wild scenario, covering scenes such as street, office, park, farm, etc. As formed in the acronym of this dataset’s name “Relative Depth from Web” (ReDWeb), this dataset is formed by stereo images collected from the Internet (Xian et al., 2018). The authors use optical flow to generate correspondence maps and create a relative depth map of the image. They post-process the data by segmenting the sky to increase the quality of the depth maps. SQUID Dataset. This dataset is composed of underwater images collected from four different sites: two in the Red Sea and two in the Mediterranean Sea (Berman et al., 2021). In addition to collecting stereo pair images, the authors included a ColorChecker to propose color restoration techniques in underwater images. Middlebury Datasets. These datasets are a composition of data released in different papers over the years of 2001, 2003, 2005, 2006, and 2014. These datasets are acquired using different strategies: custom structured light using a video projector for the Middlebury 2003 (Scharstein and Szeliski, 2003), Middlebury 2005 (Scharstein and Pal, 2007; Hirschmüller and Scharstein, 2007), Middlebury 2006 (Scharstein and Pal, 2007; Hirschmüller and Scharstein, 2007), and Middlebury 2014 (Scharstein et al., 2014), while Middlebury 2001 (Scharstein and Szeliski, 2002) uses stereo image pair dis-

6 Scenes (6690 Images)

4160 Images From 3 Different Cities (a Fourth Is Not Available)

5 Sequences (with Sub-sequences) At 5 Fps. 200k Images From Videos

28919 Images 21 Sequences (100k Images)

1200 Images 2256 Scenes (39049 Frames) 100 Images

33 Patches 38 Patches 97 Sequences (29k Frames)

464 Scenes (407024 Frames) With 1449 Labeled Aligned RGB-D Images

9 Dataset Name

54 Sequences (420k Frames)

parities. Despite using a custom structure light system, Middlebury 2014 contains improvements in the acquisition process. 4.1.4. Other This sub-category contains all datasets that do not fit into the previous divisions. There is no sub-category in “Other” with more than four examples. Therefore, we did not create a specific sub-section for them. All datasets here contain depth data and are divided into the following applications: novel view synthesis, foggy images for visibility restoration, relative depth between pairs of random points, object tracking, depth refinement for mirror surfaces, and synthesis of 4D RGB-D light field images. In Table 7, we display all these datasets and their respective application as a column of the table. The most cited dataset included here is: FRIDA2. This dataset is a synthetic dataset of foggy images of the street view. It is formed by 330 synthetic images of 66 different scenes, where each image without fog is associated with four images that vary the intensity of the artificial fog presented in it (Tarel et al., 2012). Therefore, 66 images without fog have one depth map and four foggy images associated with it. FRIDA2 is a continuation of The Foggy Road Image DAtabase (FRIDA) (Tarel et al., 2010), which has similar characteristics to FRIDA2, but fewer images (only 18 distinct scenes). These datasets are created for image enhancement in foggy images, trying to reduce the impact of the fog in the visibility of street scenes.

and sign language recognition. Here, we have only two subcategories: the first one encompass full-body activities and the second one includes partial body parts, such as hands or face. It is essential to notice that some of these datasets also include depth maps of the scene, but the focus of the dataset is on the Human Body (or part of it). Therefore, they are classified in this category. 4.2.1. Human Activities This sub-category has all datasets focused on human activities, such as drinking, eating, playing tennis, and walking. Here, we have datasets that analyze actions for an individual person (Wang et al., 2012b, 2014) or two-person interactions (Yun et al., 2012). The majority of the works in the “Human Activities” subcategory are collected in controlled scenes, and we only found Hollywood 3D (Hadfield and Bowden, 2013) using in-the-wild datasets. The majority of the datasets are indoor scenes, but as they are centered on actions, they are classified in the “Scene Type” column as “Full Body”. The most common extra data is the person pose (or skeleton) of the people involved in the scene. Such information can help improve automatic action recognition algorithms. Datasets containing Human Activities are presented in Table 8. Next, we present three influential datasets in this sub-category: NTU RGB+D. This dataset contains more than 50,000 video samples representing 60 distinct actions that are divided into three major groups: health-related actions (e.g., falling down, staggering), 40 daily actions (e.g., eating, drinking), 11 mutual actions (e.g., kicking, hugging) (Shahroudy et al., 2016). Forty subjects aged between 10 and 35 performed the actions in this dataset. The dataset was collected using three Kinect v2 from different horizontal views and is available with RGB, Depth, in-

3 LiDAR (40 And 64-beam LiDARs), 5 Radars, Stereo Camera

Normal Maps, Edges, Semantic Labels Semantic Segmentation, Navigation Data (Position, Orientation, Angular Velocity, Etc) 2D-object Detection, 3D-object Detection, Tracking, Instance Segmentation, Optical Flow. These Are Not In Necessary In The Same Dataset Instance Segmentation

1000 Scenes (20 Seconds Each). 1.4M Images And 390k LiDAR Sweeps

15 Scenes (144k Images)

11 Sequences To Over 320k Images And 100k Laser Scans

50 Sequences (100k Frames)

50 Videos (21260 Frames)

75 Scenes 3500 Scenes With 21835 Rooms (196515 Frames) 18 Scenes

572 Scenes. 1400 Floor Spaces From 572 Buildings

20 Million Images

4.5 Million Scenes

6 Large-scale Indoor Areas (70496 Images)

16 Test Scenes

frared (IR) sequences, and person pose (skeleton) information. The authors extended the NTU RGB+D to a new dataset called NTU RGB+D 120, which contains other 60 classes and 57,600 samples, also containing the same capturing system and data modalities as the previous dataset (Liu et al., 2019). MSR DailyActivity3D Dataset. This dataset covers sixteen different activities: drink, eat, read a book, call cellphone, write on a paper, use a laptop, use a vacuum cleaner, cheer up, sit still, toss paper, play games, lie down on a sofa, walk, play guitar, stand up, and sit down (Wang et al., 2012b). Ten subjects performed each action twice: one for standing and one for sitting position. This dataset also includes person pose information for each frame. The authors used the Kinect v1 to acquire the depth of the scenes.

person used for training and the other two for testing, leading to over 80 thousand acquired frames. MSR Gesture3D. This dataset contains sign language gestures. The authors collected 12 dynamic American Sign Language (ASL) gestures from ten people. The dataset was captured using Kinect v1, and has 336 sequences since each person performed multiple recordings of all selected signs. The authors performed a hand segmentation, and depth information is available only for the segmented hand regions. Background and body portions below the wrist were removed.

4.3. Medical MSR Action3D. This dataset covers twenty different actions performed by ten subjects. Each action was performed two to three times, resulting in 557 filtered sequences and 23,797 frames (Li et al., 2010). The actions are divided into three sets, where the first categorize actions with similar moviments. The third set is composed by complex actions together. All sequences were acquired using Kinect v1 sensor. 4.2.2. Gestures (Partial Body) Here, we grouped all works that involve human actions or activities and have data available for human body parts, such as arms, head, and hand. There is a wide variety of dataset purposes in this sub-category, such as action recognition based on a first-person view (no torso/head parts available in video) (Tang et al., 2017), salad preparation (Stein and McKenna, 2013), hand-pose information (Tompson et al., 2014), and sign language recognition (Wang et al., 2012a). The most cited datasets in this sub-category include: NYU Hand Pose Dataset. This dataset was captured using three Kinect v1, with two side views and a frontal view. The authors also re-created a synthetic hand pose for each view (Tompson et al., 2014), and made available 36 hand point locations for each frame. Three people acquired the data: one

In this category, we present datasets that are from any part of the medical field. The exclusion criteria removed most of the datasets found here because these contained only private data. For instance, we collected eleven datasets containing endoscopic data, but only three meets all criteria to be included in our work. This situation is common in medical applications as sharing medical information requires regulated procedures. We found only four datasets available in this category, of which three of them contain endoscopic data and one contains 3D models of the iris. The most cited dataset in containing depth information in the medical field is: Colonoscopy CG Dataset. This dataset is composed of endoscopic data of the colon. To the best of our knowledge, this is the most frequent type of data that contains depth maps in the Medical category, even if analyzing datasets with non-shared data. The authors generated a synthetic dataset using Unity graphic engine based on a human CT colonography scan. They extracted a surface mesh using manual segmentation and meshing (Rau et al., 2019). Their work also proposed and tested an algorithm in real data, but this data is not available for the community thus not included in this paper.

12 Table 6: Datasets of “Depth Data Only” sub-category Dataset Name

49 Environments (80k Images)

42923 Samples

33 Images 21 Images

6 Images 30 Scenes (8574 Indoor Images, 16884 Outdoor Images)

The datasets presented in Section 4 compose a collection of different scenes, sensors, and activities. We provide information about the Sensor Type, Number of Images/Scenes, Scene Type, Sensor Name, and Data Modalities available for each dataset. Unlike previous surveys of RGB-D datasets (Firman, 2016), we do not categorize the datasets regarding their realism since this is a subjective criterion and it is up to the researcher who will analyze the datasets to decide. Despite the variety of datasets presented, we identified common tendencies in all areas and discussed them in this section. Although synthetic data is becoming more present each time, the usage of real data is presented in the majority of the datasets. Comparing the 2016-2018 to the 2019-2021 trienniums, we

5. Discussion

found a 50% increase in the numbers of datasets containing synthetic data. Synthetic datasets are usually cheaper to produce than performing real data acquisition because extra annotations, e.g., semantic segmentation or object tracking, are automatically generated. On the other hand, complex scene annotations for real data are costly, especially in scenes such as driving and aerial. Synthetic datasets were initially created using simulators (Tarel et al., 2010, 2012), but these simulators were distinct to real-world scenarios since the computational power of the machines was limited. Hence, it was not possible to generate consistent and realistic datasets for complex scenes. Recently, realistic simulators were created for driving scenes, such

13 Table 7: “Other” Scene/Objects RGB-D Datasets Dataset Name

7011 Scenes With Mirror

as CARLA (Dosovitskiy et al., 2017), Nvidia Drive Sim2 , and indoor scenes, such as Habitat (Szot et al., 2021; Savva et al., 2019). Despite the usage of simulators, other datasets rely on game engines or general computer graphics engines to build their systems, such as SYNTHIA (Ros et al., 2016), Virtual KITTI (Gaidon et al., 2016), and Virtual KITTI 2 (Cabon et al., 2020) that used Unity3 as graphic engine, and GTA-SfM (Wang and Shen, 2020) that uses scenes from the game GTAV. The usage of synthetic data has been combined with real data to produce more complex scenes. These are applied especially for techniques that explore the generalization of their methods in non-expected scenes, i.e., using datasets not used in the training step (Ummenhofer et al., 2017; Ranftl et al., 2020; Eftekhar et al., 2021). These papers combine datasets containing different types of acquisition and scenes to produce generalizable models. Ranftl et al. (2020) created multiple cross-dataset training strategies, and its combination of datasets with more images — called MIX5— contains data from DIML, MegaDepth, RedWeb, WSVD, and 3D Movies datasets. Ranftl et al. (2021b) expanded this combination, creating the MIX6 cross-dataset set containing about 1.4 million training images. Both works were evaluated using a mixture of testing datasets. The robustness of the models are also evaluated in a cross-dataset strategy for estimating depth from a monocular video (Kopf et al., 2021), and instead of testing in multiple types of scenes, Ji et al. (2021) combined distinct datasets of the same type of scene to improve the results for the indoor environment. Recently, domain adaptation has been applied to improve the performance of the combination of datasets in the training step (Guo et al., 2018; Atapour-Abarghouei and Breckon, 2018; Zhao et al., 2019). Atapour-Abarghouei and Breckon (2018), for instance, combines one synthetic and one real dataset using domain adaptation to improve the result of training. They claim

that directly using synthetic data may not improve the results for realistic data evaluation due to dataset bias. They adapt the domain of a synthetic dataset to a real dataset using Style Transfer and combine them to train their models. Zhao et al. (2019) also performs domain adaptation, and they claim that due to the lack of paired synthetic and real images, the synthetic-torealistic image translation adds distortions to the depth estimation. They overcome this difficulty by exploring a more complex training procedure involving synthetic-to-realistic and realistic-to-synthetic translations. To generate more realistic synthetic data, Su et al. (2015) proposed the use of 3D CAD Models to produce 2D synthetic images, since these CAD Models allow multiple viewpoints and complete control of the deformations in the modeled objects to increase the variability of the created dataset. Planche et al. (2017) also used 3D CAD Models, but they intended to create realistic depth data from the 3D objects. They proposed a framework that simulates real distortion factors of depth data acquisition, e.g., material reflectance and sensor noise, to generate reliable depth data. In addition to using synthetic data, domain adaptation could also be applied to real-to-real translation (Lopez-Rodriguez and Mikolajczyk, 2020; Hornauer et al., 2021) since the dataset bias also affects distinct real datasets, especially by variations of scale and capture’s position of the scenes (Torralba and Efros, 2011).

6. Conclusions In this work, we presented a survey of publicly available image datasets that contain depth information. We categorized and summarized over 200 datasets based on the image scenes, sensors used to collect the depth information, and the different applications for which these datasets can be used. Almost half of the datasets we describe were proposed after the publication of the last survey (Cai et al., 2017). The new datasets expand the scope of applications that depth datasets can be used for, such as medical applications. The new datasets also expand the quality and quantity of data for other areas.

14 Table 8: Datasets of “Human Activity” sub-category Dataset Name

2136 Images 1201 Sequences

23 Sequences (100 People, 2004 Secs)

7 Sequences (Multiple Actions Per Sequence)

800 Frames For Each Person (26 People)

10 Sequences 56880 Sequences

65 Sequences (5.5 Capture Hours)

264 Scenes 4953 Sequences

60 Sequences 861 Sequences

707 Sequences (1720800 Frames)

447260 RGB-D Frames (almost 3.6M RGB Frames)

583 Sequences (53 Subjects)

We also presented different forms of acquiring depth information from a scene. We expect that this explanation could be used in conjunction with extra information of the datasets to allow researchers to choose the ones that best fulfill their needs. Researchers of zero-shot learning trying to increase generalization capabilities for their model could also benefit from our work since they may select distinct datasets in terms of sensor type, application, and scene type for training and evaluating their methods. CRediT authorship contribution statement Alexandre Lopes: Conceptualization, Formal analysis, Investigation, Methodology, Writing - review & editing. Roberto Souza: Funding acquisition, Methodology, Project administration, Supervision, Writing – review & editing. Helio Pedrini: Methodology, Project administration, Supervision, Writing – review & editing. Declaration of competing interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. Acknowledgements The authors are grateful to the National Council for Scientific and Technological Development, Brazil (CNPq grant 309330/2018-1). Roberto Souza thanks the Natural Sciences and Engineering Research Council (NSERC - RGPIN-202102867) for ongoing operational support.
