# 144 - Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite

## Metadata Ringkas

| Atribut | Nilai |
| :--- | :--- |
| Kunci BibTeX | `geiger2012kitti` |
| Judul asli | Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite |
| Penulis | Geiger, Andreas; Lenz, Philip; Urtasun, Raquel |
| Tahun | 2012 |
| Venue | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Dataset |

## Tautan Akses

*   Cari / unduh via Google Scholar: [Google Scholar](https://scholar.google.com/scholar?q=Are%20We%20Ready%20for%20Autonomous%20Driving%3F%20The%20KITTI%20Vision%20Benchmark%20Suite)
*   Semantic Scholar (metrik sitasi & PDF): [Semantic Scholar](https://www.semanticscholar.org/search?q=Are%20We%20Ready%20for%20Autonomous%20Driving%3F%20The%20KITTI%20Vision%20Benchmark%20Suite&sort=relevance)

## Gambaran Umum

*KITTI Vision Benchmark Suite* adalah dataset multi-sensor dan platform evaluasi terstandardisasi yang dirancang khusus untuk riset berkendara otonom (*autonomous driving*) dan robotika bergerak. Dataset ini menyediakan data dunia nyata terkalibrasi secara komprehensif, mencakup citra kamera stereo (baik monokrom maupun warna), data pemindaian laser tiga dimensi (*light detection and ranging* atau LiDAR), serta koordinat posisi berpresisi tinggi dari sistem navigasi inersia.

Sebelum KITTI diperkenalkan, sebagian besar algoritma visi komputer dievaluasi pada dataset laboratorium sintetis atau ruangan tertutup yang tidak mencerminkan kompleksitas jalan raya nyata. Hasil utama dari penelitian ini adalah pembentukan serangkaian tolok ukur (*benchmark*) publik yang menantang untuk tugas pencocokan stereo (*stereo matching*), estimasi aliran optik (*optical flow*), odometri visual (*visual odometry*), dan deteksi objek 3D. Keberadaan KITTI membantu mengidentifikasi kesenjangan besar antara performa algoritma di laboratorium dengan skenario berkendara nyata di perkotaan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Evaluasi algoritma persepsi visual pada awal dekade 2010-an sangat bergantung pada dataset dalam ruangan terkendali. Tolok ukur Middlebury untuk stereo matching dan optical flow menggunakan citra beresolusi rendah dengan pencahayaan buatan stabil. Meskipun algoritma mencapai akurasi tinggi pada dataset tersebut, performanya merosot tajam saat diuji pada luar ruangan dinamis dengan bayangan tajam, variasi pencahayaan alami, dan gerakan kendaraan berkecepatan tinggi.

Ketidaktersediaan dataset berskala besar yang mencakup sensor multimodal terkalibrasi menjadi penghambat utama pengembangan sistem berkendara otonom. Riset odometri visual dan lokalisasi simultan (*simultaneous localization and mapping* atau SLAM) sering kali dievaluasi secara terpisah tanpa acuan posisi dasar (*ground-truth trajectory*) yang akurat untuk jarak jauh. Tanpa standar evaluasi yang adil dan terbuka, sulit membandingkan kinerja metode deteksi objek dan estimasi kedalaman (*depth estimation*) secara objektif. Masalah ini sangat penting karena keselamatan kendaraan otonom bergantung pada keandalan sistem persepsi dalam mengidentifikasi rintangan dan memperkirakan posisi kendaraan di dunia nyata.

## Ide Utama

Ide utama dari KITTI adalah merekam data berkendara luar ruangan menggunakan platform kendaraan bergerak yang dilengkapi sensor visual, spasial, dan lokalisasi secara simultan, lalu menyediakannya sebagai tolok ukur terpadu. Kendaraan pengumpul data menangkap citra stereo berkecepatan tinggi bersamaan dengan *point cloud* 3D dari pemindai laser berputar. Informasi posisi dari GPS/IMU digunakan untuk menghitung trajektori presisi tinggi yang berfungsi sebagai acuan posisi dasar.

Secara teknis, dataset ini menyinkronkan waktu pengambilan data antar-sensor secara fisik pada tingkat perangkat keras (*hardware synchronization*) agar data citra dan data titik 3D merepresentasikan keadaan lingkungan yang sama pada setiap frame. Data mentah ini kemudian diproses untuk menghasilkan label acuan dasar: kotak pembatas 3D (*3D bounding boxes*) untuk deteksi objek, peta disparitas (*disparity map*) semi-padat untuk stereo matching, vektor pergeseran piksel untuk optical flow, dan koordinat pose absolut untuk visual odometry.

## Cara Kerja Langkah demi Langkah

### Sensor dan Platform Akuisisi Data
Platform pengumpul data KITTI menggunakan mobil Volkswagen Passat B6 dengan empat kamera video beresolusi tinggi, pemindai laser 3D berputar, dan unit GPS/IMU.

```
           +---------------------------------------------+
           |               ATAP KENDARAAN                |
           |                                             |
           |             [Velodyne HDL-64E]              |
           |                 (LiDAR 3D)                  |
           |                     |                       |
           |                     | (Pemicu Perangkat     |
           |                     |  Keras / Trigger)     |
           |                     v                       |
           |     [Cam 0]      [Cam 1]     [Cam 2]      [Cam 3]
           |   Stereo Gray  Stereo Gray Stereo Color Stereo Color
           |   (FL2-14S3M)  (FL2-14S3M) (FL2-14S3C)  (FL2-14S3C)
           |   |<-- 54cm -->|           |<-- 54cm -->|   |
           +---------|-----------------------------------+
                     |
                     v
             [OXTS RT 3003 GPS/IMU] (100 Hz)
```

Sistem kamera memiliki dua sensor monokrom dan dua sensor warna Point Grey Flea 2 beresolusi 1,4 megapiksel (rektifikasi menjadi 1242 × 375 piksel) dengan susunan stereo ber-baseline 54 cm. Bidang pandang (*field-of-view* atau FOV) kamera mencakup 90 derajat horizontal dan 35 derajat vertikal.

Sensor Velodyne HDL-64E LiDAR di atap berputar pada frekuensi 10 Hz dengan 64 saluran laser, mengukur jarak hingga 120 meter (akurasi ±2 cm) dan menghasilkan 100.000 titik *point cloud* per frame. Unit OXTS RT 3003 GPS/IMU melacak posisi kendaraan (*ego-motion*) pada frekuensi 100 Hz dengan koreksi *Real-Time Kinematic* (RTK) hingga akurasi 5 cm.

### Sinkronisasi Sensor dan Kalibrasi
Pencocokan data antar-sensor dikendalikan melalui mekanisme pemicu perangkat keras (*hardware trigger*). Pemindai laser Velodyne bertindak sebagai detak jam utama (*master clock*). Ketika kepala sensor Velodyne berputar dan melewati sumbu optik yang menghadap ke depan (sudut 0 derajat), ia mengirimkan sinyal elektronik pemicu ke kamera. Rana (*shutter*) kamera dibuka secara instan saat pemindaian laser berlangsung pada area pandang kamera tersebut. Mekanisme ini meminimalkan jeda waktu (*latency*) spasial antar-sensor akibat gerakan dinamis kendaraan.

Kalibrasi intrinsik kamera dimodelkan menggunakan proyeksi lubang jarum (*pinhole camera*) dengan koreksi distorsi radial-tangensial menggunakan papan catur (*checkerboard*). Kalibrasi ekstrinsik antara kamera dan sensor LiDAR dihitung melalui registrasi semi-otomatis dengan mencocokkan fitur tepi 3D pada objek kalibrasi khusus yang terlihat pada data *point cloud* Velodyne dan citra kamera. Seluruh koordinat spasial disatukan menggunakan matriks transformasi homogen 4×4.

### Proses Pembuatan Anotasi Ground-Truth
Anotasi data acuan dasar dibuat secara terpisah sesuai dengan jenis tugas tolok ukurnya:
1.  **Anotasi Deteksi Objek 3D**: Kotak pembatas 3D (*3D bounding box*) dianotasi secara manual oleh annotator manusia dengan memvisualisasikan data *point cloud* LiDAR 3D yang diproyeksikan ke citra kamera 2D. Setiap objek dilabeli dengan kotak pembatas 3D yang memiliki 7 parameter: posisi pusat $(x, y, z)$, dimensi fisik objek (tinggi $h$, lebar $w$, panjang $l$), dan sudut rotasi *yaw* (sudut orientasi arah hadap objek terhadap arah sumbu kendaraan). Kotak pembatas 2D didapatkan secara otomatis dengan menghitung proyeksi batas terluar (*bounding rectangle*) dari kotak pembatas 3D ke bidang gambar.
2.  **Anotasi Stereo Matching dan Optical Flow**: Akurasi disparitas pixel-level diperoleh menggunakan pendekatan semi-otomatis. Pertama, data *point cloud* LiDAR dari beberapa frame berturut-turut diakumulasi menggunakan informasi trajektori dari GPS/IMU untuk meningkatkan kerapatan titik. Poin-poin dinamis (seperti kendaraan bergerak) dihilangkan menggunakan anotasi objek 3D. Titik-titik statis kemudian diproyeksikan kembali ke sistem koordinat kamera pada frame target untuk menghasilkan peta disparitas dan aliran optik acuan dasar yang bersifat semi-padat (*semi-dense disparity and flow maps*). Densitas titik acuan dasar ini mencapai sekitar 50% dari total piksel gambar, yang dinilai cukup untuk evaluasi kuantitatif.

### Skala Dataset dan Pembagian Data
Dataset KITTI direkam di kota Karlsruhe, Jerman, mencakup area perkotaan (*urban*), pedesaan (*rural*), dan jalan tol (*highway*). Ukuran gambar hasil rektifikasi stereo (*stereo rectification*) adalah 1242 × 375 piksel. Pembagian data ditentukan berdasarkan jenis tugas evaluasi:
1.  **Deteksi Objek (2D dan 3D)**: Terdiri dari 7.481 citra latih (*training set*) yang dilengkapi dengan label anotasi publik, dan 7.518 citra uji (*testing set*) yang anotasinya dirahasiakan oleh pihak penyelenggara. Total terdapat 80.256 objek yang dianotasi, meliputi kelas *Car*, *Van*, *Truck*, *Pedestrian*, *Person (sitting)*, *Cyclist*, *Tram*, dan *Misc*. Hanya tiga kelas utama (*Car*, *Pedestrian*, dan *Cyclist*) yang dievaluasi secara resmi.
2.  **Visual Odometry / SLAM**: Menyediakan 22 sekuens video stereo terkalibrasi dengan panjang lintasan kumulatif 39,2 km. Sekuens 00 hingga 10 (total 23.201 frame) disediakan beserta trajektori acuan dasar untuk pelatihan, sedangkan sekuens 11 hingga 21 (total 20.351 frame) digunakan untuk pengujian tanpa rilis trajektori publik.
3.  **Stereo Matching dan Optical Flow (versi 2012)**: Terdiri dari 194 pasang citra pelatihan beserta peta disparitas/aliran optik acuan dasar semi-padat, dan 195 pasang citra pengujian.

## Eksperimen dan Hasil

Evaluasi pada benchmark deteksi objek 3D KITTI menggunakan metrik *Average Precision* (AP). Pengujian dibagi menjadi tiga tingkat kesulitan berdasarkan tinggi kotak pembatas di citra, tingkat halangan (*occlusion*), dan pemotongan batas gambar (*truncation*):
*   **Easy**: tinggi kotak pembatas $\ge 40$ piksel, tidak terhalang (oklusi = 0), terpotong $\le 15\%$.
*   **Moderate**: tinggi kotak pembatas $\ge 25$ piksel, terhalang sebagian (oklusi = 1), terpotong $\le 30\%$.
*   **Hard**: tinggi kotak pembatas $\ge 25$ piksel, terhalang berat (oklusi = 2), terpotong $\le 50\%$.

Ambang batas *Intersection over Union* (IoU) ditetapkan sebesar $70\%$ untuk objek *Car*, serta $50\%$ untuk objek *Pedestrian* dan *Cyclist*. Pada makalah aslinya di tahun 2012, baseline deteksi objek 2D dan 3D diuji menggunakan algoritma berbasis fitur *Histogram of Oriented Gradients* (HOG) dan *Deformable Part Models* (DPM). Hasil deteksi 3D menunjukkan kinerja yang sangat rendah pada masa itu; misalnya, untuk kelas *Car* tingkat kesulitan *Moderate*, nilai AP 3D berada di bawah $10,0\%$. Hasil ini mengindikasikan betapa sulitnya melakukan estimasi orientasi dan kedalaman 3D hanya dari citra monokular atau stereo tanpa metode pembelajaran mendalam (*deep learning*) modern.

Untuk visual odometry, evaluasi diukur berdasarkan *average translation error* dalam persentase (\%) dan *average rotation error* dalam derajat per 100 meter (deg/100m) pada seluruh kemungkinan subsekuens dengan panjang 100 hingga 800 meter. Metode odometry visual berbasis stereo klasik saat itu mencapai galat translasi sekitar $1,0\%$ hingga $2,5\%$ dari total jarak tempuh, membuktikan keunggulan informasi kedalaman stereo dibanding sistem monokular yang rentan terhadap penyimpangan skala (*scale drift*).

Pada tugas stereo matching, evaluasi dihitung dari persentase piksel dengan galat disparitas melebihi 3 piksel (disebut *Out-Noc* untuk daerah non-oklusi). Metode stereo matching terbaik saat itu memiliki tingkat kesalahan disparitas sekitar $3,0\%$ hingga $5,0\%$ pada citra pengujian.

## Kelebihan dan Keterbatasan

Kelebihan utama KITTI adalah penyediaan data multi-sensor nyata yang sinkron dan terkalibrasi dengan sangat presisi. Sebelum KITTI, riset visi komputer dan robotika berjalan secara terpisah; KITTI menyatukan komunitas tersebut dengan menyediakan satu platform untuk menguji deteksi objek, odometri, dan estimasi kedalaman sekaligus. Metodologi pengumpulan data dengan pemicu perangkat keras terbukti efektif mengurangi distorsi spasial akibat gerakan kendaraan. Tolok ukur evaluasi dengan pembagian tingkat kesulitan (*Easy*, *Moderate*, *Hard*) menjadi standar industri dalam menilai ketangguhan model persepsi.

Dari sisi keterbatasan, dataset KITTI direkam hanya dalam kondisi cuaca cerah hingga sedikit berawan pada siang hari di satu kota (Karlsruhe). Hal ini membuat model yang dilatih pada KITTI mengalami penurunan performa dramatis (*domain shift*) ketika diuji pada kondisi malam hari, hujan, salju, atau kabut. Secara konseptual, ukuran dataset KITTI relatif kecil jika dibandingkan dengan kebutuhan pelatihan model pembelajaran mendalam modern yang memerlukan variasi skenario jutaan frame.

Selain itu, dari sisi rekayasa, sensor LiDAR 64-channel Velodyne HDL-64E menghasilkan representasi *point cloud* yang lebih jarang pada jarak jauh (>50 meter), sehingga deteksi objek kecil pada jarak tersebut memiliki tingkat kesalahan yang tinggi. Sensor kamera yang dipasang menghadap ke depan juga membatasi cakupan persepsi kendaraan menjadi hanya sekitar 90 derajat, tidak mencakup 360 derajat di sekitar kendaraan.

## Kaitan dengan Bab Lain

KITTI berfungsi sebagai jembatan penting dari dataset berbasis dalam ruangan (*indoor*) ke luar ruangan (*outdoor*) dinamis. Dibandingkan dengan NYU Depth v2 [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md) yang mengandalkan kamera RGB-D aktif jarak pendek untuk ruangan terkendali, KITTI menggunakan kombinasi kamera pasif stereo dan LiDAR aktif untuk mengukur jarak luar ruangan hingga lebih dari 100 meter. Perluasan dataset luar ruangan ini juga berbeda dengan SUN RGB-D [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md) dan ScanNet [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md) yang tetap berfokus pada rekonstruksi spasial dan segmentasi semantik objek-objek dalam ruangan.

Dalam silsilah dataset deteksi objek umum, KITTI membawa tugas deteksi 2D dari objek-objek umum seperti pada Microsoft COCO [146 - 2014 - Microsoft COCO - Dataset](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md) ke domain berkendara otonom yang mensyaratkan kotak pembatas 3D untuk keselamatan navigasi fisik. Keterbatasan KITTI dalam hal skala data, cakupan sensor 360 derajat, dan keragaman cuaca kemudian diatasi oleh dataset modern seperti nuScenes [145 - 2020 - nuScenes - Dataset](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md). nuScenes memperluas konsep sensor fusion yang dirintis KITTI dengan menggunakan LiDAR 32-channel, 6 kamera warna untuk cakupan melingkar penuh, radar, serta volume data yang lebih besar dengan variasi kondisi malam dan hujan di area urban padat.

## Poin untuk Sitasi

Kunci BibTeX untuk merujuk publikasi ini adalah `geiger2012kitti`.

Ringkasan kutipan:
> KITTI Vision Benchmark Suite adalah dataset luar ruangan multi-sensor terkalibrasi pertama yang menyediakan data terpadu dari kamera stereo, LiDAR, dan GPS/IMU untuk tugas deteksi objek 3D, visual odometry, stereo matching, dan optical flow. Tolok ukur ini menetapkan standar evaluasi formal dengan tingkat kesulitan *Easy*, *Moderate*, dan *Hard* berbasis oklusi dan pemotongan objek.

Catatan verifikasi angka:
*   Tugas deteksi objek menggunakan pembagian 7.481 citra latih dan 7.518 citra uji.
*   Tugas visual odometry mencakup 22 sekuens stereo dengan panjang total 39,2 km.
*   Tugas stereo matching dan optical flow versi 2012 menggunakan pembagian 194 pasang citra latih dan 195 pasang citra uji.
