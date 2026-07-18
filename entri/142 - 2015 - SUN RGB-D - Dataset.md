# 142 - SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `song2015sunrgbd` |
| Judul asli | SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite |
| Penulis | Shuran Song, Samuel P. Lichtenberg, Jianxiong Xiao |
| Tahun | 2015 |
| Venue | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Dataset |

## Tautan Akses
* **Tautan Halaman Resmi Dataset:** http://rgbd.cs.princeton.edu/
* **Google Scholar:** https://scholar.google.com/scholar?q=SUN+RGB-D%3A+A+RGB-D+Scene+Understanding+Benchmark+Suite
* **Semantic Scholar:** https://www.semanticscholar.org/search?q=SUN+RGB-D%3A+A+RGB-D+Scene+Understanding+Benchmark+Suite
* **Tautan PDF Resmi (CVF Open Access):** https://openaccess.thecvf.com/content_cvpr_2015/papers/Song_SUN_RGB-D_A_2015_CVPR_paper.pdf

## Gambaran Umum
*SUN RGB-D* adalah paket tolok ukur (*benchmark suite*) dan dataset tiga dimensi (*3D*) dalam ruang berskala besar untuk mempercepat riset pemahaman adegan (*scene understanding*). Dataset ini menyatukan data dari berbagai sensor kedalaman (*depth sensor*) konsumen guna menyediakan 10.335 citra RGB-D yang terdaftar secara spasial dan dianotasi secara padat. Kehadirannya memfasilitasi pelatihan model pembelajaran mendalam (*deep learning*) yang membutuhkan data spasial untuk mengenali objek dan geometri ruangan secara simultan. Kontribusi utama proyek ini mencakup penyediaan 146.617 poligon segmentasi semantik 2D, 58.657 kotak pembatas (*bounding box*) 3D berorientasi yang sejajar dengan arah gravitasi, serta anotasi tata letak (*layout*) ruangan 3D. Evaluasi terstandardisasi diletakkan untuk tugas deteksi objek 3D, segmentasi semantik 2D/3D, dan tata letak ruang dalam satu kerangka kerja yang adil.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum SUN RGB-D dirilis pada tahun 2015, pemahaman adegan dalam ruang terhambat oleh sempitnya skala dataset yang tersedia. Meskipun sensor kedalaman konsumen seperti Microsoft Kinect v1 (2010) membuat akuisisi data spasial menjadi murah, dataset saat itu tidak cukup besar untuk melatih model klasifikasi atau deteksi berbasis jaringan saraf tiruan yang memiliki banyak parameter.
Sebagai contoh, dataset NYU Depth v2 ([silberman2012nyu](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)) hanya menyediakan 1.449 citra beranotasi. Dataset Berkeley 3D Object Dataset (*B3DO*) hanya mencakup 555 citra dengan pelabelan objek terbatas. Dataset SUN3D memiliki video yang panjang tetapi tidak memiliki anotasi kotak pembatas 3D berorientasi yang memadai untuk deteksi objek secara amodal (*amodal object detection*). Keadaan ini kontras dengan domain luar ruang (*outdoor*) yang telah memiliki dataset KITTI ([geiger2012kitti](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)) beranotasi 3D berskala besar.
Masalah kedua adalah bias sensor (*sensor bias*). Model yang dilatih pada satu jenis sensor gagal digeneralisasi pada sensor lain akibat variasi resolusi kedalaman, derau (*noise*), dan teknologi akuisisi. Sensor dengan metode cahaya terstruktur (*structured light*) seperti Kinect v1 memiliki karakteristik derau berbeda dengan sensor berbasis waktu tempuh cahaya (*time-of-flight*) seperti Kinect v2. Standardisasi lintas sensor diperlukan untuk menguji generalisasi model terhadap variasi perangkat keras di dunia nyata.

## Ide Utama
Ide utama SUN RGB-D adalah menggabungkan dataset indoor yang sudah ada dengan data baru dari berbagai sensor kedalaman modern guna membentuk basis data benchmark berukuran 10.335 citra RGB-D. Untuk mengatasi derau dan kekosongan data pada peta kedalaman mentah (*raw depth maps*), diusulkan perbaikan kedalaman (*depth refinement*) secara temporal dengan menyelaraskan video sequence pendek menggunakan metode *Scale-Invariant Feature Transform* (SIFT) dan *Iterative Closest Point* (ICP). Fusi temporal ini mengisi piksel kosong melalui estimasi median. Selain itu, penelitian ini memperkenalkan antarmuka anotasi 3D terproyeksi yang efisien. Dengan memproyeksikan kubus 3D dari ruang awan titik (*point cloud*) ke citra warna 2D secara interaktif, annotator dapat memverifikasi keselarasan orientasi dan kotak pembatas objek secara visual, mempercepat pengumpulan puluhan ribu anotasi 3D berkualitas tinggi.

## Cara Kerja Langkah demi Langkah

### Pengumpulan Data dan Keragaman Sensor
Dataset SUN RGB-D (10.335 citra) menggabungkan data lama dengan data baru yang diambil dari empat sensor kedalaman berbeda untuk mengatasi bias sensor:
1. **Microsoft Kinect v2**: Menyumbang 3.784 citra baru. Menggunakan teknologi waktu tempuh cahaya dengan resolusi warna 1920×1080 dan kedalaman 512×424 piksel.
2. **Intel RealSense**: Menyumbang 1.159 citra baru. Berukuran kecil, ditenagai tablet untuk ruang sempit, dengan resolusi 640×480 piksel untuk jarak dekat.
3. **Microsoft Kinect v1**: Menyumbang 2.003 citra dari NYU Depth v2 (1.449 citra) dan Berkeley B3DO (554 citra) dengan resolusi 640×480 piksel berbasis cahaya terstruktur.
4. **Asus Xtion**: Menyumbang 3.389 citra dari dataset SUN3D dengan resolusi 640×480 piksel berbasis cahaya terstruktur bertenaga USB rendah.

### Refinemen Kedalaman Temporal dengan SIFT-ICP
Peta kedalaman mentah dari sensor berbiaya rendah sering kali memiliki nilai kosong akibat permukaan reflektif atau oklusi. Langkah perbaikan peta kedalaman dilakukan sebagai berikut:
1. **Penyelarasan SIFT**: Fitur SIFT diekstraksi dari citra target dan bingkai video pendek tetangga untuk mencari titik korespondensi.
2. **Inisialisasi RANSAC**: Matriks transformasi 3D awal (rotasi dan translasi) dihitung menggunakan *Random Sample Consensus* (RANSAC) untuk menyaring korespondensi SIFT yang salah.
3. **Penyempurnaan ICP**: Transformasi awal disempurnakan dengan *Iterative Closest Point* (ICP) tipe *point-to-plane* pada awan titik mentah sampai konvergen.
4. **Fusi Median**: Nilai kedalaman akhir per piksel diperoleh dari nilai median temporal dari peta kedalaman yang telah diselaraskan untuk memuluskan derau dan mengisi area kosong pada objek statis.

### Kalibrasi Geometris dan Estimasi Kemiringan
Setiap citra dilengkapi parameter intrinsik kamera dan matriks ekstrinsik registrasi spasial antara kamera RGB dan sensor kedalaman. Agar kotak pembatas 3D sejajar dengan bidang lantai, koordinat kamera harus diputar ke koordinat dunia yang selaras dengan gravitasi. Sudut kemiringan (*tilt angle*) diestimasi melalui akselerometer internal sensor (pada Kinect) atau estimasi *Manhattan world* (pada Asus Xtion dan RealSense) yang menggunakan RANSAC 3D untuk mendeteksi bidang lantai dominan dan mencari tiga sumbu ortogonal dari normal permukaan objek.

### Pipeline Anotasi Semantik 2D dan Kotak Pembatas 3D
1. **Anotasi 2D**: Pekerja Amazon Mechanical Turk (AMT) melabeli poligon semantik 2D padat pada citra RGB menggunakan antarmuka berbasis web.
2. **Anotasi 3D**: Pekerja menyesuaikan kotak pembatas 3D berorientasi (*oriented 3D bounding box*) pada awan titik yang diproyeksikan ke citra 2D secara waktu nyata.
3. **Kontrol Kualitas**: Citra harus memiliki minimal 6 objek teranotasi dan mencakup minimal 30% area citra. Verifikator ahli melakukan penyaringan akhir untuk memperbaiki pergeseran kotak pembatas.

```
+-----------------------------------------------------------------+
|                    ALUR PROSES PEMBUATAN DATASET                |
+-----------------------------------------------------------------+
 Citra Diam Target & Video Pendek ──> Ekstraksi Fitur SIFT 2D
                                               │
 Peta Kedalaman Mentah (Raw)      ──> RANSAC: Estimasi Transformasi 3D
                                               │
 Awan Titik Mentah (Point Cloud)  ──> Point-to-Plane ICP (Penyempurnaan)
                                               │
 Peta Kedalaman Terdaftar         ──> Fusi Median Temporal (Pengisian Lubang)
                                               │
 Awan Titik Hasil Refinemen       ──> Estimasi Orientasi Gravitasi (Manhattan)
                                               │
 Citra RGB + Awan Titik Sejajar   ──> Antarmuka Anotasi 2D/3D Terproyeksi
                                               │
                                               v
                                   Anotasi Akhir:
                                   - 146.617 Poligon 2D
                                   - 58.657 Kotak Pembatas 3D Berorientasi
                                   - 3D Room Layout & Scene Category
```

## Eksperimen dan Hasil
Evaluasi performa menggunakan pembagian standar: 5.285 citra untuk pelatihan dan 5.050 citra untuk pengujian. Metrik evaluasi utama untuk deteksi objek 3D adalah *mean Average Precision* (mAP) dengan ambang batas *Intersection over Union* (IoU) 3D sebesar $0,25$.
Penulis mengevaluasi model baseline klasik seperti *Deformable Part Models* 3D (3D DPM) dan *Sliding Shapes* (pemindaian jendela 3D langsung pada awan titik). Hasil eksperimen menunjukkan bahwa deteksi objek 3D indoor sangat sulit akibat oklusi padat dan variasi penampilan objek.
Tabel berikut merangkum performa deteksi objek 3D (Average Precision, AP) dari model baseline *Sliding Shapes* pada beberapa kelas objek utama di set pengujian SUN RGB-D:

| Kategori Objek | Sliding Shapes (AP) |
| :--- | :---: |
| Kasur (*Bed*) | 42,09 |
| Kursi (*Chair*) | 25,78 |
| Meja (*Table*) | 23,28 |

Objek dengan struktur geometri yang konsisten seperti kasur memiliki AP lebih tinggi dibandingkan kursi atau meja yang memiliki variasi desain ekstrem dan struktur tipis yang sulit ditangkap secara detail oleh sensor kedalaman konsumen.

## Kelebihan dan Keterbatasan
Kelebihan utama SUN RGB-D adalah penyediaan data lintas sensor yang meminimalkan bias perangkat keras, memaksa model mempelajari fitur geometri yang lebih umum. Anotasi multi-tugas yang padat memungkinkan pemahaman adegan secara holistik yang menghubungkan representasi 2D dan 3D.
Secara konseptual, keterbatasan dataset ini terletak pada kualitas data kedalaman sensor konsumen. Meskipun diperbaiki dengan SIFT-ICP, area di luar jangkauan optimal (di atas 3,5 meter) atau permukaan yang sangat menyerap cahaya tetap memiliki derau spasial tinggi. Selain itu, dataset ini didominasi oleh tata letak ruangan standar Amerika Serikat/Barat, sehingga kurang merepresentasikan variasi arsitektur dalam ruang dari wilayah geografis lain. Anotasi manual untuk objek yang teroklusi sebagian juga memiliki ketidakpastian posisi spasial yang tinggi.

## Kaitan dengan Bab Lain
SUN RGB-D mewarisi data citra dari NYU Depth v2 ([silberman2012nyu](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)) sebanyak 1.449 citra dan Berkeley B3DO sebanyak 554 citra, tetapi melengkapinya dengan anotasi kotak pembatas 3D berorientasi yang sebelumnya tidak ada secara standar.
Dibandingkan dengan ScanNet ([dai2017scannet](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)), SUN RGB-D berfokus pada citra diam RGB-D tunggal yang terpisah, sedangkan ScanNet menyajikan rekonstruksi 3D ruangan penuh yang direkonstruksi dari video scan kontinu untuk menghasilkan mesh 3D beranotasi padat.
Dalam aplikasi spasial, SUN RGB-D adalah padanan dalam ruang bagi dataset luar ruang berbasis LiDAR dan kamera seperti KITTI ([geiger2012kitti](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)) dan nuScenes ([caesar2020nuscenes](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)), dengan jangkauan lebih pendek tetapi resolusi objek lebih tinggi. Jika dibandingkan dengan dataset segmentasi 2D seperti Microsoft COCO ([lin2014coco](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)), SUN RGB-D menambahkan dimensi spasial ketiga yang penting untuk robotika.

## Poin untuk Sitasi
Kunci BibTeX:
```bibtex
@inproceedings{song2015sunrgbd,
  title={SUN RGB-D: A RGB-D scene understanding benchmark suite},
  author={Song, Shuran and Lichtenberg, Samuel P and Xiao, Jianxiong},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={567--576},
  year={2015}
}
```

Ringkasan kutipan:
SUN RGB-D menyediakan dataset 10.335 citra RGB-D dalam ruang beranotasi padat dari empat sensor berbeda (Kinect v1/v2, Asus Xtion, Intel RealSense). Dataset ini merupakan tolok ukur standar untuk deteksi objek 3D berorientasi (58.657 kotak pembatas), segmentasi semantik 2D (146.617 poligon), dan estimasi tata letak ruangan 3D. Karakteristik lintas sensor yang dimilikinya membantu meminimalkan bias perangkat keras dalam evaluasi model visi komputer dalam ruang.

Catatan verifikasi:
Jumlah kotak pembatas 3D berorientasi tercatat sebanyak 58.657 kotak pembatas dalam makalah asli, tetapi beberapa rilis pembaruan atau filter kelas evaluasi dapat menyebutkan angka hingga 64.595 kotak pembatas. Pengguna perlu mengonfirmasi protokol *split* data latihan/uji yang digunakan untuk membandingkan performa deteksi secara adil.
