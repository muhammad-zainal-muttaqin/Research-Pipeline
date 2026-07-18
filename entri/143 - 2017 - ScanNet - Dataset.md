# 143 - ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dai2017scannet` |
| Judul asli | ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes |
| Penulis | Angela Dai, Angel X. Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, Matthias Nießner |
| Tahun | 2017 |
| Venue | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Dataset |

## Tautan Akses
- **arXiv (Preprint):** https://arxiv.org/abs/1702.04405
- **CVF Open Access (Versi PDF Resmi):** https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf
- **Google Scholar:** https://scholar.google.com/scholar?q=ScanNet%3A%20Richly-Annotated%203D%20Reconstructions%20of%20Indoor%20Scenes

## Gambaran Umum
ScanNet adalah dataset rekonstruksi tiga dimensi (3D) berskala besar yang dirancang untuk mendukung penelitian pemahaman adegan dalam ruangan (*indoor scene understanding*). Dataset ini menyediakan pindaian (*scan*) lingkungan dalam ruangan yang kaya akan anotasi semantik instansial pada tingkat objek 3D. Dataset ini mengatasi keterbatasan skala dataset pendahulu yang umumnya terbatas pada citra statis atau model sintetik yang tidak mencerminkan kompleksitas geometri dunia nyata.

ScanNet mengatasi hambatan tersebut dengan menyediakan 1.513 scan dari 707 ruang dalam ruangan yang unik, menghasilkan sekitar 2,5 juta bingkai video warna dan kedalaman (*RGB-D video frames*). Setiap scan dilengkapi dengan estimasi pose kamera yang presisi, model *mesh* segitiga 3D hasil rekonstruksi padat (*dense reconstruction*), anotasi segmentasi semantik instansial 3D, serta 9.621 penyelarasan (*alignments*) dengan model CAD (*Computer-Aided Design*) dari ShapeNet. ScanNet berfungsi sebagai tolok ukur (*benchmark*) standar untuk mengevaluasi berbagai tugas pemahaman spasial 3D, seperti pelabelan voxel semantik (*semantic voxel labeling*), klasifikasi objek 3D, dan pencarian objek 3D (*3D object retrieval*).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemindahan algoritma pembelajaran mendalam (*deep learning*) dari domain dua dimensi (2D) ke 3D terhambat oleh ketiadaan dataset 3D dunia nyata berskala besar dengan ukuran dan keragaman yang setara. Bidang pemahaman adegan 3D sebelum tahun 2017 didominasi oleh dataset yang memiliki beberapa keterbatasan struktural yang signifikan.

Pertama, dataset perintis seperti NYU Depth v2 ([141](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)) menyediakan video RGB-D, tetapi anotasi semantiknya terbatas pada 1.449 bingkai kunci (*keyframe*) individual. Kedua, dataset SUN RGB-D ([142](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)) menyatukan sekitar 10.335 citra RGB-D tunggal dengan anotasi kotak pembatas (*bounding box*) 3D, tetapi tidak menyediakan informasi rekonstruksi mesh 3D kontinu yang merepresentasikan geometri ruangan secara utuh.

Tantangan utama dalam pembuatan dataset 3D skala besar terletak pada kompleksitas akuisisi data dan tingginya biaya anotasi. Perekaman data 3D tradisional memerlukan pemindai laser industri yang mahal dan kurang dinamis. Di sisi lain, estimasi pose kamera dari sensor komoditas yang murah sering kali mengalami penyimpangan akumulatif (*drift*) yang parah, sehingga model rekonstruksi mesh menjadi terdistorsi. Lebih lanjut, proses pelabelan semantik 3D secara manual per verteks (*vertex*) pada data mesh 3D yang memiliki jutaan verteks sangat tidak efisien. Masalah-masalah inilah yang melatarbelakangi perancangan pipeline akuisisi dan anotasi ScanNet yang terintegrasi dan efisien.

## Ide Utama
Gagasan inti dari ScanNet adalah memadukan proses akuisisi data berbasis sensor konsumen yang murah dengan pipeline pemrosesan otomatis di sisi server (*server-side*), serta mengoptimalkan proses pelabelan manusia melalui metode urun daya (*crowdsourcing*) bertahap. Alur kerja ini meningkatkan skala dataset tanpa mengorbankan kualitas geometri atau akurasi anotasi.

Biaya ditekan menggunakan kombinasi tablet iPad Air dan sensor kedalaman Occipital Structure Sensor dengan umpan balik real-time kepada operator di lapangan. Di sisi server, data video mentah diproses menggunakan BundleFusion untuk menghasilkan rekonstruksi mesh 3D yang bebas dari distorsi *drift*. Untuk menyederhanakan pelabelan, mesh 3D dibagi secara otomatis menjadi wilayah kecil yang homogen secara geometris yang disebut segmen super (*supersegments*). Dengan demikian, pekerja urun daya tidak perlu melabeli jutaan verteks secara individu, melainkan cukup mengecat (*mesh painting*) atau mengelompokkan segmen-segmen super tersebut menjadi instansi objek tertentu menggunakan antarmuka berbasis web.

## Cara Kerja Langkah demi Langkah
Proses pembuatan, rekonstruksi, anotasi, dan validasi dataset ScanNet dijalankan melalui alur kerja terstruktur yang terbagi menjadi lima tahapan utama sebagai berikut:

```
                        +----------------------------+
                        |  iPad Air + Structure      |
                        |  Sensor (Video RGB-D)      |
                        +--------------+-------------+
                                       | (RGB-D Mentah)
                                       ▼
                        +----------------------------+
                        |  Server-Side BundleFusion  | <--- Estimasi Pose Global
                        |  3D Reconstruction Mesh    |      dan Integrasi Voxel
                        +--------------+-------------+
                                       | (Mesh 3D PLY)
                                       ▼
                        +----------------------------+
                        |   Pra-segmentasi Mesh      | <--- Felzenszwalb-
                        |   (Menghasilkan Segmen)    |      Huttenlocher 3D
                        +--------------+-------------+
                                       | (Mesh Tersegmentasi)
                                       ▼
                        +----------------------------+
                        |   Pekerjaan Urun Daya MTurk| <--- Pelabelan Instansi
                        |   WebGL SSTK Annotation   |      & Penyelarasan CAD
                        +--------------+-------------+
                                       | (Anotasi Objek)
                                       ▼
                        +----------------------------+
                        |   Validasi Kualitas (QA)   | <--- Konsensus >= 3/4
                        |   Diterima / Ditolak       |      Pekerja Validasi
                        +--------------+-------------+
                                       |
                                       ├─────────────────────────────┐
                                       ▼ (Diterima)                  ▼ (Diterima)
                        +----------------------------+ +----------------------------+
                        | Mesh Semantik 3D & Label   | | Penyelarasan Model CAD    |
                        | Voxel Teranotasi           | | ShapeNet (9.621 Model)     |
                        +----------------------------+ +----------------------------+
```

### 1. Akuisisi Data di Lapangan
Perekaman adegan dilakukan oleh operator manusia yang membawa iPad Air dengan Occipital Structure Sensor. Selama perekaman, operator berjalan mengelilingi ruangan dengan kecepatan normal. Aplikasi kustom pada iPad menampilkan visualisasi rekonstruksi mesh beresolusi rendah secara real-time melalui metode *voxel hashing* sederhana di dalam perangkat. Visualisasi ini memberikan umpan balik visual instan mengenai area yang belum terpindai atau mengalami kekosongan data (*holes*). Video RGB-D direkam pada resolusi 640×480 piksel untuk saluran warna dan kedalaman pada kecepatan 30 FPS.

### 2. Rekonstruksi 3D dan Estimasi Pose Offline
Setelah data RGB-D mentah diunggah ke server, estimasi pose kamera yang presisi dihitung secara offline. Langkah ini menggunakan kerangka kerja *BundleFusion*, sebuah algoritma rekonstruksi 3D berbasis GPU yang melakukan optimasi pose kamera global dan lokal secara *end-to-end*. BundleFusion mencocokkan fitur warna (*keypoint features*) di seluruh bingkai video secara global dan menggabungkannya dengan pencocokan geometris iteratif (*iterative closest point* / ICP) pada data kedalaman untuk menghasilkan lintasan kamera yang konsisten secara spasial dan bebas dari *drift*. Setelah pose kamera ditentukan, data kedalaman diintegrasikan menggunakan teknik integrasi volumetrik (*volumetric integration*) untuk mengekstrak mesh segitiga permukaan 3D dalam format PLY.

### 3. Pra-segmentasi Mesh Geometris
Untuk menghindari beban kerja pelabelan verteks demi verteks yang lambat, mesh segitiga hasil rekonstruksi diproses secara geometris sebelum diserahkan kepada annotator. Proses pra-segmentasi ini membagi mesh menjadi kelompok-kelompok kecil verteks yang homogen yang disebut segmen super (*supersegments*). Metode ini menggunakan adaptasi algoritma segmentasi berbasis graf Felzenszwalb dan Huttenlocher (2004) pada graf mesh 3D, dengan verteks bertindak sebagai simpul graf dan bobot tepi dihitung berdasarkan deviasi normal permukaan (*surface normals*) serta nilai kelengkungan (*curvature*) lokal antar-verteks.

### 4. Pelabelan Semantik dan Penyelarasan CAD via Urun Daya
Pekerja dari Amazon Mechanical Turk (MTurk) melakukan anotasi via antarmuka WebGL SSTK (*Semantic Scene Toolkit*) melalui dua langkah utama:
- **Pelabelan Semantik Instansial:** Pekerja diperlihatkan model mesh 3D yang telah tersegmentasi kasar. Mereka memilih label kelas dari menu (seperti kursi atau meja) lalu mengecat (*mesh painting*) segmen-segmen super dengan klik tetikus (*mouse clicks*) untuk mengelompokkannya menjadi satu instansi objek 3D tunggal.
- **Penyelarasan Model CAD:** Pekerja menyelaraskan objek pindaian 3D kasar dengan model CAD geometris bersih dari basis data ShapeNet. Pekerja memilih model ShapeNet yang paling mirip dengan objek asli, lalu menyesuaikan rotasi, translasi, dan skala (9 derajat kebebasan atau 9DoF) model CAD tersebut hingga bertumpukan secara presisi pada mesh hasil scan.

### 5. Validasi Kualitas dan Pengendalian Mutu
Setiap scan yang selesai terlabeli dikirim ke antrian tugas validasi terpisah di MTurk. Empat pekerja validasi baru yang independen akan memeriksa setiap instansi objek yang telah dianotasi. Mereka memberikan penilaian biner (diterima atau ditolak) untuk memverifikasi apakah batas objek sudah mencakup seluruh bagian fisik objek dan apakah penamaan kelasnya sudah benar. Jika setidaknya 3 dari 4 validator menyetujui anotasi tersebut, data scan tersebut diterima dan dimasukkan ke dalam rilis dataset resmi. Jika ditolak, objek yang bermasalah dikembalikan ke tugas anotasi awal untuk diperbaiki.

## Eksperimen dan Hasil
Untuk membuktikan kegunaan praktis dan kualitas data dari ScanNet, para penulis membagi dataset menjadi 1.201 scan untuk pelatihan, 312 scan untuk validasi, dan 100 scan untuk pengujian untuk mengevaluasi beberapa model dasar pada tugas-tugas berikut:

### 1. Klasifikasi Objek 3D (3D Object Classification)
Tugas ini memprediksi kategori kelas objek 3D dari segmen mesh yang diisolasi menggunakan kotak pembatas. Pengujian dilakukan pada 20 kategori objek dominan dalam ruangan. Dua model arsitektur 3D dibandingkan dalam eksperimen ini, yaitu VoxNet (berbasis representasi voxel) dan PointNet (berbasis representasi *point cloud* langsung). Hasil eksperimen menunjukkan akurasi sebagai berikut:
- **VoxNet:** Mencapai akurasi klasifikasi sebesar **73,0%**.
- **PointNet:** Mencapai akurasi klasifikasi sebesar **73,9%**.

Akurasi PointNet yang sedikit lebih tinggi menunjukkan bahwa pengolahan data awan titik langsung tanpa konversi ke representasi voxel terbukti efektif dan lebih hemat memori karena tidak memproses ruang kosong di dalam grid volumetrik.

### 2. Pelabelan Voxel Semantik (Semantic Voxel Labeling)
Tugas pelabelan voxel semantik memprediksi label semantik untuk setiap voxel dalam volume rekonstruksi 3D dengan resolusi voxel 0,05 meter (5 cm). Penulis membandingkan kinerja model baseline 3D CNN dengan metode berbasis proyeksi citra 2D terdahulu, seperti Hermans dkk. dan SemanticFusion. Hasil evaluasi diukur menggunakan metrik *mean Intersection over Union* (mIoU) pada 20 kelas:
- **Metode Hermans dkk. (2014):** Mencapai mIoU sebesar **21,3%**.
- **SemanticFusion (2016):** Mencapai mIoU sebesar **26,4%**.
- **Baseline 3D CNN (ScanNet):** Mencapai mIoU sebesar **32,8%**.

Model 3D CNN mampu memanfaatkan konteks geometri volumetrik langsung tanpa mengalami distorsi proyeksi balik seperti metode 2D yang mengalami distorsi spasial.

## Kelebihan dan Keterbatasan

### Kelebihan
- **Skala Data:** Menyediakan 1.513 scan (2,5 juta frame RGB-D), jauh melampaui dataset pemandangan dalam ruangan pendahulu yang kecil atau berupa citra tunggal.
- **Konsistensi Spasial:** Rekonstruksi mesh segitiga 3D konsisten secara spasial dan bebas dari akumulasi *drift* berkat BundleFusion.
- **Kekayaan Anotasi:** Menyediakan anotasi instansial 3D lengkap dan 9.621 penyelarasan model CAD ShapeNet.
- **Alur Kerja Terstandardisasi:** Pipeline pengumpulan data berumpan balik instan dan validasi urun daya mempercepat produksi data tanpa menurunkan akurasi *ground-truth*.

### Keterbatasan
- **Keterbatasan Fisik Sensor:** Dari sisi rekayasa, sensor Occipital Structure Sensor sensitif pada cahaya luar ruang, berjangkauan terbatas (0,5–3,5 m), dan gagal memindai permukaan kaca, cermin, atau benda hitam pekat.
- **Spesialisasi Domain Indoor Statis:** Secara konseptual, dataset ini murni terbatas pada lingkungan dalam ruangan statis, sehingga model yang dilatih dengannya tidak dapat secara langsung digeneralisasikan pada lingkungan luar ruangan yang dinamis atau skenario berkendara otonom.
- **Oklusi Geometris:** Sudut-sudut ruangan di belakang objek besar sering kali tidak terpindai secara utuh karena oklusi, menyisakan lubang pada mesh hasil rekonstruksi.

## Kaitan dengan Bab Lain
ScanNet memiliki hubungan erat dalam silsilah pengembangan dataset pemahaman spasial komputer 3D:
- **Pewarisan Konsep:** ScanNet mewarisi konsep pelabelan RGB-D indoor dari NYU Depth v2 ([141](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)) dan SUN RGB-D ([142](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)) guna mengatasi keterbatasan skala data mereka.
- **Kontras Metodologi Sensor:** Jika dibandingkan dengan dataset luar ruangan seperti KITTI ([144](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)) dan nuScenes ([145](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)) yang menggunakan sensor LiDAR aktif berjangkauan jauh untuk mendeteksi objek jalan raya, ScanNet menggunakan sensor RGB-D jarak dekat yang dioptimalkan untuk memetakan objek interior ruangan yang padat secara geometris.
- **Kesejajaran Klasifikasi Instansial:** Dari segi kelimpahan instansi, ScanNet berfungsi sebagai analogi 3D dari Microsoft COCO ([146](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)) untuk pemahaman objek individual dalam ruang spasial.
- **Pengaruh bagi Metode Deteksi:** Data rekonstruksi 3D dan anotasi instansial dari ScanNet menjadi pondasi pelatihan utama untuk berbagai model deteksi objek 3D berbasis point cloud penting, seperti VoteNet (Qi dkk., 2019).

## Poin untuk Sitasi
- **Kunci BibTeX:** `dai2017scannet`
- **Ringkasan Sitasi:**
  > ScanNet menyediakan 1.513 scan rekonstruksi 3D dari 707 ruangan indoor dengan 2,5 juta frame video RGB-D. Dataset ini dianotasi secara instansial pada level objek 3D serta diselaraskan dengan 9.621 model CAD dari ShapeNet melalui mekanisme crowdsourcing berbasis segmentasi mesh geometris. Dataset ini menjadi benchmark standar untuk evaluasi tugas pelabelan voxel semantik, klasifikasi objek 3D, dan pencarian objek 3D.
- **Catatan Verifikasi/Klaim:**
  > Hasil evaluasi klasifikasi objek 3D (PointNet mencapai akurasi 73,9% dan VoxNet mencapai 73,0%) serta pelabelan voxel semantik (mIoU 32,8% menggunakan model 3D CNN baseline) dievaluasi menggunakan pembagian data resmi (1.201 train / 312 val / 100 test) pada 20 kategori objek dominan. Anotasi pelurusan ShapeNet CAD sebanyak 9.621 model merupakan rilis awal dari paper CVPR 2017, sedangkan perluasan pelurusan yang lebih padat dan presisi untuk evaluasi tingkat lanjut dikembangkan kemudian pada proyek terpisah seperti Scan2CAD (2019).
