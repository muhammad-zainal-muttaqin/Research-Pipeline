# 145 - nuScenes: A Multimodal Dataset for Autonomous Driving

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `caesar2020nuscenes` |
| Judul asli | nuScenes: A Multimodal Dataset for Autonomous Driving |
| Penulis | Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Giancarlo Baldan, Oscar Beijbom |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Dataset |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1903.11027
- **Google Scholar:** https://scholar.google.com/scholar?q=nuScenes%3A%20A%20Multimodal%20Dataset%20for%20Autonomous%20Driving
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=nuScenes%3A%20A%20Multimodal%20Dataset%20for%20Autonomous%20Driving&sort=relevance

## Gambaran Umum
nuScenes adalah dataset publik berskala besar untuk berkendara otonom (*autonomous driving*) dengan cakupan spasial 360 derajat melingkar penuh. Dataset ini merekam 1.000 skenario berkendara dinamis sepanjang 20 detik di Boston dan Singapura menggunakan rangkaian sensor (*sensor suite*) lengkap: enam kamera resolusi tinggi, satu sensor *Light Detection and Ranging* (LiDAR) 32-beam, lima radar FMCW (*Frequency Modulated Continuous Wave*), dan sensor navigasi terpadu.

Dataset ini mengatasi keterbatasan KITTI yang hanya mencakup visual satu arah depan, skala kecil, dan tanpa radar. nuScenes menyediakan 1,4 juta kotak pembatas 3D (*3D bounding boxes*) untuk 23 kelas objek pada 40.000 bingkai kunci (*keyframes*). Makalah ini juga memperkenalkan metrik *nuScenes Detection Score* (NDS) yang mengombinasikan *mean Average Precision* (mAP) dengan lima metrik galat fisik (translasi, skala, orientasi, kecepatan, dan atribut) untuk mengevaluasi ketangguhan model fusi sensor secara komprehensif.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum nuScenes, penelitian berkendara otonom sangat bergantung pada dataset KITTI (bab [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)). Namun, KITTI memiliki keterbatasan kritis karena kamera sensor hanya menghadap ke depan dengan sudut pandang (*field of view*) sekitar 90 derajat. Hal ini menyulitkan deteksi objek samping atau belakang, sedangkan navigasi aman membutuhkan kesadaran situasional 360 derajat.

Selain itu, KITTI berukuran kecil (15.000 sampel) dan diambil dari satu kota homogen pada cuaca cerah siang hari. Keterbatasan ini membuat model sulit bergeneralisasi ke skenario hujan, malam hari, atau area urban padat. KITTI juga tidak menyertakan radar, sensor penting dalam industri otomotif karena mampu mengukur kecepatan instan objek melalui efek Doppler dan andal dalam cuaca buruk.

Terakhir, metrik evaluasi seperti mAP 3D berbasis batas *Intersection over Union* (IoU 3D) terlalu sensitif terhadap galat kecil estimasi kedalaman (*depth*). Sedikit pergeseran pada sumbu kedalaman menjatuhkan nilai IoU 3D hingga nol meskipun orientasi dan dimensi kotak akurat. Oleh karena itu, diperlukan dataset multimodal 360 derajat dengan metrik yang lebih merefleksikan aspek keselamatan berkendara nyata.

## Ide Utama
Gagasan inti nuScenes adalah membangun ekosistem data berkendara otonom multimodal yang menangkap lingkungan sekitar kendaraan tanpa area buta (*blind spot*). nuScenes menggabungkan karakteristik sensor yang saling melengkapi: kamera memberikan resolusi spasial dan detail tekstur tinggi, LiDAR memberikan informasi geometris 3D yang presisi pada jarak menengah, sedangkan radar mendeteksi jarak jauh dan kecepatan instan yang tahan cuaca buruk.

Untuk evaluasi model, nuScenes menggeser paradigma dari ambang batas IoU 3D yang kaku ke jarak pusat 2D di atas tanah (*ground plane center distance*) sebagai kriteria pencocokan. Evaluasi disatukan ke dalam satu metrik skalar (NDS) yang mengukur berbagai galat fisik seperti translasi, skala, orientasi, kecepatan, dan atribut, sehingga performa dinilai berdasarkan utilitas praktis dalam berkendara nyata.

## Cara Kerja Langkah demi Langkah
Struktur tata letak sensor pada kendaraan perekam nuScenes dirancang untuk cakupan spasial 360 derajat penuh, seperti yang diilustrasikan pada diagram berikut:

```
                            CAM_FRONT
                           RADAR_FRONT
                                ▲
                                │
   CAM_FRONT_LEFT ◄───────────┌─┐───────────► CAM_FRONT_RIGHT
 RADAR_FRONT_LEFT             │ │             RADAR_FRONT_RIGHT
                              │ │ ◄── LIDAR_TOP (Atap)
                              │ │
                              │ │
    CAM_BACK_LEFT ◄───────────│ │───────────► CAM_BACK_RIGHT
  RADAR_BACK_LEFT             └─┘             RADAR_BACK_RIGHT
                                │
                                ▼
                            CAM_BACK
```

### Konfigurasi Sensor dan Sinkronisasi Temporal
Perekaman data nuScenes menggunakan satu unit kendaraan uji yang dilengkapi sensor melingkar terkalibrasi tinggi:
- Enam kamera Basler acA1920-40gc (12 Hz) beresolusi 1600×900 piksel untuk cakupan visual 360 derajat.
- Satu LiDAR Velodyne VLP-32 (20 Hz) berjangkauan 80 meter dan akurasi ±3 cm di atas atap kendaraan.
- Lima radar Continental ARS 408-21 (13 Hz, 77 GHz) di bumper depan (tiga) dan bumper belakang (dua) untuk cakupan radar 360 derajat.
- GPS/IMU Advanced Navigation Spatial (1000 Hz) untuk pose kendaraan (*ego-pose*).

Untuk menyinkronkan sensor dengan frekuensi berbeda, nuScenes menggunakan pemicu perangkat keras (*hardware trigger*). Kamera dipicu mengambil gambar tepat ketika berkas sinar LiDAR melintasi pusat bidang pandang masing-masing kamera. Mekanisme ini meminimalkan jeda waktu (*latency*) antara gambar kamera dan awan titik (*point cloud*) LiDAR hingga di bawah beberapa milidetik.

### Pemilihan Skenario dan Akuisisi Data
Data diambil di Boston dan Singapura untuk menguji generalisasi model terhadap perbedaan aturan lalu lintas (lalu lintas kiri vs kanan), marka jalan, dan morfologi jalan. Dari rekaman 15 jam sepanjang 242 km, dipilih 1.000 skenario berkendara masing-masing berdurasi 20 detik. Pemilihan skenario dilakukan secara manual demi menjamin variasi situasi jalan, kepadatan lalu lintas, cuaca (cerah/hujan), dan kondisi cahaya (siang/malam). Skenario mencakup persimpangan jalan padat, manuver memotong jalur oleh kendaraan lain, serta pejalan kaki tidak teratur.

### Protokol Anotasi 3D dan Interpolasi Lintasan
Untuk efisiensi biaya, nuScenes melabeli bingkai kunci secara manual pada frekuensi 2 Hz (setiap 0,5 detik). Kotak pembatas 3D didefinisikan sebagai vektor status 7 dimensi: $(x, y, z, w, l, h, \theta)$, di mana $(x, y, z)$ adalah posisi pusat 3D, $(w, l, h)$ dimensi fisik, dan $\theta$ sudut orientasi *yaw*.

Anotator juga memberikan label dari 23 kategori objek, status atribut dinamis, dan tingkat keterlihatan (*visibility*) objek dalam empat rentang persentase. Untuk bingkai antara di frekuensi sensor asli (20 Hz), digunakan interpolasi linear secara otomatis yang kemudian diperiksa secara semi-otomatis untuk menjamin kehalusan lintasan pelacakan (*track*) objek.

### Formulasi Metrik Evaluasi NDS (nuScenes Detection Score)
Untuk mengatasi kelemahan IoU 3D, nuScenes menggunakan jarak Euclidean 2D di atas tanah antara pusat prediksi dan pusat kebenaran (*ground truth*) dengan ambang batas $d \in \{0,5, 1, 2, 4\}$ meter untuk menghitung mAP. Selain mAP, dihitung lima metrik galat True Positive (TP) pada deteksi dengan jarak $\le 2$ meter:
- **mATE (mean Average Translation Error):** Galat translasi pusat 2D (meter).
- **mASE (mean Average Scale Error):** Galat skala ($1 - \text{IoU 3D}$ setelah pusat dan orientasi diselaraskan).
- **mAOE (mean Average Orientation Error):** Galat sudut yaw dalam radian $[0, \pi]$.
- **mAVE (mean Average Velocity Error):** Galat kecepatan absolut (m/s).
- **mAAE (mean Average Attribute Error):** Galat klasifikasi atribut ($1 - \text{akurasi atribut}$).

Galat TP ($mTP$) dinormalisasi dengan skor $1 - \min(1, mTP)$. Skor akhir NDS diformulasikan sebagai:
$$NDS = \frac{1}{10} \left[ 5 \cdot mAP + \sum_{mTP \in \mathbb{TP}} (1 - \min(1, mTP)) \right]$$
Di sini, $\mathbb{TP} = \{mATE, mASE, mAOE, mAVE, mAAE\}$. mAP diberi bobot 5, sedangkan kelima metrik galat masing-masing diberi bobot 1. Metrik ini memberikan penilaian adil terhadap ketepatan orientasi dan kecepatan yang krusial bagi keselamatan berkendara otonom.

## Eksperimen dan Hasil
Eksperimen awal nuScenes membandingkan metode berbasis kamera tunggal (seperti MonoDIS), LiDAR tunggal (seperti PointPillars), dan metode fusi. Hasil menunjukkan model berbasis kamera memiliki mAP rendah (< 20%) dan mATE tinggi (> 0,7 m) akibat keterbatasan estimasi kedalaman visual. Sebaliknya, metode LiDAR mencapai presisi geometri lebih tinggi dengan mATE di bawah 0,3 m.

Fusi multimodal memberikan hasil terbaik. Penggabungan kamera dan LiDAR meningkatkan deteksi objek kecil dan teroklusi. Integrasi radar secara signifikan meminimalkan galat kecepatan (mAVE) dibandingkan model tanpa radar, membuktikan pentingnya data radar untuk melacak dinamika kendaraan. Di papan peringkat saat ini, arsitektur fusi modern (seperti BEVFusion) mendominasi dengan nilai NDS di atas 75% dan mAP di atas 70%.

## Kelebihan dan Keterbatasan
Kelebihan nuScenes terletak pada cakupan sensor 360 derajat terpadu dengan kalibrasi dan sinkronisasi temporal presisi tinggi yang meminimalkan galat proyeksi spasial. Penyediaan data radar adalah keunggulan unik untuk estimasi kecepatan dinamis secara andal. Metrik NDS yang diusulkan juga mengevaluasi performa secara lebih representatif terhadap kebutuhan navigasi riil.

Namun, nuScenes memiliki beberapa keterbatasan. Dari sisi rekayasa, data radar sangat renggang (*sparse*) dan berderau (*noisy*), memerlukan penyaringan intensif. Secara konseptual, meskipun mencakup malam dan hujan, dataset ini didominasi cuaca cerah, sehingga performa pada cuaca ekstrem belum teruji penuh. Selain itu, anotasi manual 3D hanya tersedia pada keyframe 2 Hz; keakuratan interpolasi linier otomatis pada bingkai antara dapat berkurang saat objek mengalami perubahan gerak mendadak.

## Kaitan dengan Bab Lain
Sebagai dataset luar ruangan multimodal, nuScenes menyempurnakan standardisasi data yang dirintis oleh KITTI (bab [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)). nuScenes memperluas sudut pandang dari 90 derajat depan menjadi cakupan 360 derajat melingkar penuh, serta mengintegrasikan data radar yang absen di KITTI.

Dibandingkan dataset dalam ruangan (*indoor*) seperti NYU Depth v2 (bab [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)), SUN RGB-D (bab [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)), dan ScanNet (bab [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)), nuScenes beroperasi pada skala lingkungan luar ruangan (*outdoor*) dinamis jarak jauh. Sensor RGB-D pada dataset dalam ruangan tidak andal di luar ruangan karena interferensi sinar matahari, sehingga nuScenes beralih ke LiDAR dan radar untuk deteksi jarak jauh.

Bila dibandingkan dengan Microsoft COCO (bab [146 - 2014 - Microsoft COCO - Dataset](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)) yang menyediakan jutaan anotasi 2D lintas 80 kelas sehari-hari, nuScenes mengorbankan variasi kelas umum demi berfokus pada 23 kategori transportasi jalan raya, dengan kedalaman data dalam dimensi spasial 3D dan runtunan temporal.

## Poin untuk Sitasi
Kunci BibTeX: `caesar2020nuscenes`

nuScenes adalah dataset berkendara otonom berskala besar dengan cakupan 360 derajat yang menggabungkan 6 kamera, 1 LiDAR, dan 5 radar. Dataset ini menyediakan 1.000 skenario berkendara di Boston dan Singapura dengan anotasi kotak pembatas 3D penuh pada 40.000 bingkai kunci. Makalah ini memperkenalkan metrik nuScenes Detection Score (NDS) yang mengombinasikan mAP dan metrik galat fisik seperti translasi, orientasi, skala, kecepatan, dan atribut.

Catatan verifikasi: Meskipun mencakup 1,4 juta kotak pembatas 3D, anotasi manual hanya dilakukan pada bingkai kunci 2 Hz, sementara bingkai perantara 20 Hz menggunakan interpolasi linier otomatis.
