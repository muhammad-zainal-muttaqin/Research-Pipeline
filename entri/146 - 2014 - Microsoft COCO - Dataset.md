# 146 - Microsoft COCO: Common Objects in Context

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2014coco` |
| Judul Asli | Microsoft COCO: Common Objects in Context |
| Penulis | Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, C. Lawrence Zitnick |
| Tahun | 2014 |
| Venue | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema | Dataset |

## Tautan Akses
*   **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Microsoft%20COCO%3A%20Common%20Objects%20in%20Context
*   **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Microsoft%20COCO%3A%20Common%20Objects%20in%20Context&sort=relevance
*   **ArXiv (naskah lengkap PDF):** https://arxiv.org/abs/1405.0312

## Gambaran Umum
Microsoft *Common Objects in Context* (MS COCO) merupakan dataset berskala besar yang dirancang khusus untuk mendorong pengenalan objek berbasis pemahaman adegan (*scene understanding*). Makalah ini mengatasi kelemahan dataset visi komputer terdahulu yang berfokus pada klasifikasi objek tunggal atau pendeteksian objek berlatar belakang bersih. Hasil utama penelitian ini adalah penyediaan dataset berisi 328.000 citra dengan 2,5 juta objek yang dianotasi secara padat menggunakan batas piksel presisi (*instance segmentation*).

Selain menyajikan citra dalam konteks alami, COCO mendefinisikan ulang evaluasi performa model pendeteksi objek dengan memperkenalkan metrik rata-rata *Average Precision* (AP) pada rentang ambang batas pencocokan yang ketat. Metrik baru ini menuntut model memprediksi lokasi objek secara presisi. Sejak dirilis pada 2014, COCO telah menjadi benchmark standar *de facto* untuk menguji dan membandingkan kinerja berbagai algoritma deteksi objek modern, termasuk rumpun model *You Only Look Once* (YOLO).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum dataset COCO dirilis, pengembangan deteksi objek bergantung pada dataset seperti PASCAL VOC atau ImageNet. Dataset tersebut memiliki kelemahan sistematis berupa bias citra ikonik (*iconic image bias*), di mana objek target berada tepat di tengah gambar, berukuran besar, tanpa oklusi (penghalangan), dan berlatar belakang bersih. Model yang dilatih pada data ikonik kerap gagal saat diuji pada situasi dunia nyata yang kompleks, di mana objek sering bertumpukan atau hanya terlihat sebagian.

Dataset lama juga memiliki keterbatasan jumlah objek per citra. PASCAL VOC rata-rata hanya memuat kurang dari tiga objek per citra, berbeda jauh dengan kondisi dunia nyata yang padat. Keterbatasan ini menghalangi model mempelajari hubungan kontekstual antar-objek (seperti posisi cangkir yang biasanya berdekatan dengan meja). Pendeteksian objek kecil pun kurang terwakili akibat keterbatasan resolusi dan dominasi objek berukuran besar.

Dari sisi evaluasi, metrik kinerja deteksi terdahulu kurang menuntut akurasi lokalisasi yang tinggi. Metrik AP pada PASCAL VOC hanya menggunakan ambang batas pencocokan *Intersection over Union* (IoU) tunggal sebesar 0,50 (AP50). Ambang batas yang longgar ini membiarkan model dengan prediksi kotak pembatas (*bounding box*) yang kurang presisi tetap memperoleh skor tinggi selama klasifikasinya benar. Oleh karena itu, komunitas membutuhkan benchmark baru dengan anotasi yang lebih kaya dan metrik evaluasi yang lebih ketat demi mendorong kemajuan sistem deteksi objek praktis.

## Ide Utama
Gagasan utama COCO adalah menggeser fokus pengenalan objek terisolasi menuju pemahaman adegan holistik dengan menempatkan objek sehari-hari dalam konteks alami mereka (*objects in context*). Penulis meyakini pengenalan objek yang tangguh memerlukan pemahaman latar belakang dan interaksi spasial antar-objek di sekelilingnya. Untuk merealisasikan tujuan ini pada skala ratusan ribu citra, ide kuncinya terletak pada pipa anotasi multi-tahap memanfaatkan tenaga kerja massal (*crowdsourcing*) melalui platform Amazon Mechanical Turk (AMT).

Proses anotasi didekonstruksi menjadi tugas-tugas mikro yang lebih sederhana agar mengurangi kesalahan manusia dan menghemat biaya. Pipa kerja ini memisahkan proses verifikasi kelas objek, pelokalan posisi secara kasar, dan penggambaran batas poligon secara presisi. Setiap tahap divalidasi oleh beberapa pekerja independen guna memastikan cakupan temuan (*recall*) maksimal serta keakuratan batas segmentasi objek.

## Cara Kerja Langkah demi Langkah
Pembuatan dataset COCO dirancang melalui pipa anotasi tiga tahap terstruktur menggunakan platform AMT dengan langkah-langkah berikut:

```
                    [ Citra Kandidat dari Web ]
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             Penyaringan Awal Citra Non-Ikonik               │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│          Tahap 1: Pelabelan Kategori (8 Pekerja)            │
│       - Mengonfirmasi keberadaan kategori objek             │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│          Tahap 2: Penandaan Instansi (8 Pekerja)            │
│       - Menaruh titik (klik) pada setiap instansi           │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│          Tahap 3: Segmentasi Instansi (1 Pekerja)           │
│       - Menggambar poligon presisi untuk setiap objek      │
│       - Menerapkan label 'iscrowd' untuk tumpukan objek     │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
            [ Dataset Akhir: Gambar + Mask + Box ]
```

### Pengumpulan Citra Non-Ikonik
Langkah pertama dimulai dengan pengumpulan gambar dari internet. Penulis menghindari pencarian kata kunci tunggal (seperti "anjing") karena menghasilkan citra ikonik dengan objek tunggal di tengah latar belakang bersih. Pencarian dilakukan memakai pasangan kata kunci (seperti "anjing dan frisbee" atau "cangkir di atas meja") untuk menangkap interaksi antar-objek dalam lingkungan kompleks. Citra kandidat disaring oleh pekerja AMT untuk membuang gambar ikonik dan menyisakan adegan kontekstual yang kaya.

### Tahap 1: Pelabelan Kategori (Category Labeling)
Sistem menampilkan sebuah citra bersama daftar kategori objek kepada pekerja AMT. Pekerja bertugas menandai kategori objek yang terlihat dalam gambar tersebut. Untuk meminimalkan kesalahan objek yang terlewat (*false negative*), setiap citra dievaluasi secara independen oleh 8 pekerja AMT yang berbeda. Kategori objek dinyatakan ada dalam citra jika disetujui melalui konsensus suara terbanyak dari para pekerja tersebut, menghasilkan daftar kelas terverifikasi.

### Tahap 2: Penandaan Instansi (Instance Spotting)
Setelah kategori terkonfirmasi, citra masuk ke tahap kedua. Pekerja AMT diberikan satu kategori objek spesifik yang telah divalidasi pada tahap sebelumnya, lalu diminta menandai setiap instansi objek tersebut dengan menaruh titik koordinat (klik) di atasnya. Tahap ini juga dikerjakan oleh 8 pekerja independen per citra guna memastikan objek kecil atau yang mengalami oklusi dapat teridentifikasi. Koordinat titik hasil klik berfungsi sebagai penanda posisi kasar bagi instansi objek.

### Tahap 3: Segmentasi Instansi (Instance Segmentation)
Pekerja AMT menggambar batas poligon secara presisi di sekeliling setiap objek yang titiknya telah ditandai pada Tahap 2. Tugas ini menuntut ketelitian tinggi, sehingga hanya pekerja AMT yang lulus modul pelatihan pra-anotasi dan tes kualifikasi khusus yang diperbolehkan berpartisipasi. Pekerja menggambar poligon luar yang menyelimuti seluruh bagian objek yang tampak, termasuk bagian yang terhalang oleh objek lain.

Untuk objek yang berkumpul sangat padat (seperti sekumpulan buah dalam keranjang atau kerumunan penonton), COCO menyediakan atribut khusus `iscrowd`. Jika label `iscrowd` bernilai benar (`iscrowd = 1`), pekerja tidak perlu menggambar poligon untuk setiap objek secara terpisah. Seluruh area kelompok tersebut dianotasi sebagai satu kesatuan masker dengan format *Run-Length Encoding* (RLE). Pendekatan ini menghemat waktu anotasi dan menjaga kesederhanaan komputasi saat melatih model deteksi.

### Skala dan Pembagian Dataset (Dataset Splits)
Proyek COCO mengumpulkan 328.000 citra. Pada rilis awal COCO 2014, dataset dibagi menjadi tiga bagian: data pelatihan (*train split*) sebanyak 82.783 citra, data validasi (*validation split*) sebanyak 40.504 citra, dan data pengujian (*test split*) sebanyak 40.775 citra. Dalam rancangan awalnya, COCO mengidentifikasi 91 kategori objek umum. Namun, akibat keterbatasan jumlah sampel untuk beberapa kelas (seperti "topi" dan "sepatu"), hanya 80 kategori objek yang memiliki anotasi segmentasi lengkap dan digunakan sebagai benchmark standar evaluasi deteksi objek 2D global.

## Eksperimen dan Hasil
Penulis menggunakan model *Deformable Parts Model* (DPMv5) dan model berbasis jaringan saraf konvensional (*Convolutional Neural Network*/CNN) awal seperti R-CNN untuk membangun batas atas performa awal (*baseline performance*) pada dataset COCO. Evaluasi dilakukan memakai metrik AP baru yang mereka usulkan, yaitu rata-rata AP pada 10 ambang batas IoU dari 0,50 hingga 0,95 dengan interval langkah 0,05 (AP@[0.50:0.95] atau AP). Evaluasi juga mencakup AP50, AP75 (ambang batas ketat IoU 0,75), serta AP berdasarkan skala objek: kecil (AP_S, luas area < $32^2$ piksel), sedang (AP_M, $32^2 \leq$ luas area $\leq 96^2$ piksel), dan besar (AP_L, luas area > $96^2$ piksel).

Hasil eksperimen baseline menunjukkan tingginya tingkat kesulitan dataset COCO. Model DPMv5 yang dilatih pada dataset COCO (DPMv5-C) hanya mencapai nilai AP50 sebesar 19,7% pada tugas deteksi kotak pembatas. Ketika model DPMv5 yang dilatih pada PASCAL VOC 2012 (DPMv5-P) diuji silang pada COCO, kinerjanya merosot tajam sebesar 12,7 AP. Sebaliknya, model yang dilatih pada COCO (DPMv5-C) hanya mengalami penurunan kinerja sebesar 7,7 AP saat diuji pada dataset lain. Hal ini membuktikan secara empiris bahwa model yang dilatih menggunakan variasi konteks alami dalam COCO memiliki kemampuan generalisasi lintas domain yang lebih unggul.

Model berbasis CNN awal seperti R-CNN mencatat performa deteksi kotak pembatas yang lebih baik dibandingkan DPMv5, namun skor AP keseluruhannya tetap di bawah 30%. Rendahnya skor ini disebabkan buruknya kinerja detektor pada objek-objek kecil (AP_S di bawah 5%). Eksperimen ini memperlihatkan bahwa keberadaan objek kecil yang berlimpah dan tingkat oklusi tinggi dalam citra non-ikonik COCO menjadi tantangan utama yang membutuhkan inovasi arsitektur lebih lanjut pada representasi skala multi-fitur jaringan saraf konvensional.

## Kelebihan dan Keterbatasan
Evaluasi analitis terhadap dataset COCO menunjukkan kekuatan utama dan kelemahan yang melekat pada pengembangannya:

### Kelebihan
*   **Standardisasi Metrik Evaluasi Modern**: Pengenalan metrik AP rata-rata lintas ambang batas IoU (0,50 hingga 0,95) memaksa komunitas riset meningkatkan akurasi lokalisasi kotak pembatas model deteksi.
*   **Kualitas Anotasi Piksel-Presisi**: Penyediaan anotasi poligon untuk segmentasi instansi pada skala besar memungkinkan dataset digunakan untuk tugas deteksi objek, segmentasi semantik, dan segmentasi instansi secara bersamaan.
*   **Representasi Dunia Nyata yang Autentik**: Fokus pada citra non-ikonik menyajikan tantangan oklusi, keberagaman skala objek, dan kompleksitas konteks latar belakang yang mirip dengan kondisi operasional di dunia nyata.

### Keterbatasan
*   **Biaya Anotasi Tinggi**: Secara rekayasa, pembuatan anotasi poligon manual melalui crowdsourcing membutuhkan biaya finansial besar dan waktu yang lama. Proses ini tidak mudah diskalakan tanpa bantuan model segmentasi otomatis.
*   **Keterbatasan Dimensi Sensor (RGB 2D)**: Secara konseptual, COCO hanya menyediakan data visual RGB 2D standar tanpa informasi kedalaman (*depth*) atau orientasi spasial 3D objek. Hal ini membuatnya kurang optimal untuk tugas persepsi spasial 3D pada domain robotika atau sistem kendaraan otonom.

## Kaitan dengan Bab Lain
Dataset COCO memiliki peran penting sebagai benchmark standar yang menghubungkan berbagai klaster penelitian dataset dalam tinjauan pustaka ini:

*   **Perbandingan dengan NYU Depth v2** (lihat [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)): NYU Depth v2 berfokus pada data kedalaman (RGB-D) dalam ruangan berskala kecil (1.449 citra berlabel padat). COCO mengorbankan informasi sensor kedalaman demi mendapat skala gambar RGB 2D yang jauh lebih masif (328.000 citra) guna memperkuat generalisasi model deteksi visual pada skenario yang lebih luas.
*   **Perbandingan dengan SUN RGB-D** (lihat [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)): SUN RGB-D menggabungkan data RGB-D dari berbagai sensor untuk 10.335 citra dalam ruangan. Berbeda dengan SUN RGB-D yang terfokus pada estimasi kotak pembatas 3D di area dalam ruangan, COCO menyediakan benchmark deteksi objek 2D dan segmentasi instansi 2D yang mencakup lingkungan dalam ruangan (*indoor*) dan luar ruangan (*outdoor*) secara seimbang.
*   **Perbandingan dengan ScanNet** (lihat [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)): ScanNet menyediakan pindaian rekonstruksi mesh 3D untuk lingkungan dalam ruangan. Sementara ScanNet memajukan pemahaman spasial 3D berbasis geometri, COCO tetap menjadi fondasi utama bagi evaluasi segmentasi instansi 2D pada citra RGB biasa.
*   **Perbandingan dengan KITTI** (lihat [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)) dan **nuScenes** (lihat [145 - 2020 - nuScenes - Dataset](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)): KITTI dan nuScenes adalah dataset otomotif berskala besar untuk mengemudi otonom dengan distribusi kelas yang sangat bias terhadap elemen jalan raya (mobil, pejalan kaki, pesepeda). Sebaliknya, COCO mencakup spektrum objek sehari-hari yang jauh lebih umum (80 kategori objek) dengan distribusi yang lebih merata untuk pengenalan objek umum.

## Poin untuk Sitasi
Kunci BibTeX: `lin2014coco`

Kutipan yang disarankan untuk tinjauan pustaka:
> Dataset Microsoft COCO (Lin dkk., 2014) merupakan benchmark deteksi objek dan segmentasi instansi berskala besar yang terdiri atas 328.000 citra dengan anotasi piksel-presisi untuk 80 kategori objek dalam konteks non-ikonik. Makalah ini memperkenalkan metrik evaluasi rata-rata AP lintas ambang batas IoU 0,50 hingga 0,95 yang menjadi standar de-facto dalam pengujian kinerja model visi komputer modern termasuk arsitektur YOLO.

Catatan verifikasi data:
*   Jumlah kategori objek yang dirancang awalnya adalah 91, namun versi rilis 2014 hanya menyediakan anotasi segmentasi lengkap untuk 80 kategori.
*   Skor baseline AP50 untuk model Deformable Parts Model (DPMv5-C) yang dilaporkan dalam makalah asli adalah sebesar 19,7% pada tugas deteksi kotak pembatas COCO.
