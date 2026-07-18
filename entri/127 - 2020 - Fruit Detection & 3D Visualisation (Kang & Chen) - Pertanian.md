# 127 - Fruit Detection, Segmentation and 3D Visualisation of Environments in Apple Orchards

## Metadata Ringkas
| Atribut | Nilai |
| --- | --- |
| Kunci BibTeX | `kang2020strawberry` |
| Judul asli | Fruit Detection, Segmentation and 3D Visualisation of Environments in Apple Orchards |
| Penulis | Kang, Hanwen; Chen, Chao |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** [Google Scholar](https://scholar.google.com/scholar?q=Fruit%20Detection%2C%20Segmentation%20and%203D%20Visualisation%20of%20Environments%20in%20Apple%20Orchards)
- **Semantic Scholar (metrik sitasi & PDF):** [Semantic Scholar](https://www.semanticscholar.org/search?q=Fruit%20Detection%2C%20Segmentation%20and%203D%20Visualisation%20of%20Environments%20in%20Apple%20Orchards&sort=relevance)
- **Halaman arXiv (PDF & Abstrak):** [arXiv:1911.12889](https://arxiv.org/abs/1911.12889)

## Gambaran Umum
Penelitian oleh Kang dan Chen (2020) memperkenalkan DaSNet-V2, sebuah kerangka kerja persepsi visual multi-tugas (*multi-task visual perception*) berbasis pembelajaran mendalam (*deep learning*) untuk mendukung pemanenan buah apel secara robotik (*robotic apple harvesting*). DaSNet-V2 mengintegrasikan tiga fungsi penginderaan visual utama dalam satu arsitektur jaringan satu tahap (*one-stage detector*): deteksi buah apel, segmentasi instansi (*instance segmentation*) buah untuk memisahkan setiap buah secara individual, dan segmentasi semantik (*semantic segmentation*) cabang pohon sebagai rintangan fisik yang harus dihindari oleh lengan robot.

Untuk mendukung perencanaan gerakan lengan robot, kerangka kerja ini memadukan informasi visual 2D dengan data kedalaman dari sensor RGB-D (*Red Green Blue-Depth*) guna menghasilkan rekonstruksi visualisasi tiga dimensi (3D) dari lingkungan kebun apel secara langsung. Jaringan ini memanfaatkan tulang punggung ringan yang disebut *Lightweight Backbone* (LW-net) berbasis arsitektur sisa (*residual network*) agar dapat berjalan dengan efisiensi tinggi pada komputer tertanam (*embedded computer*) seperti NVIDIA Jetson TX2, dengan alternatif ResNet-101 untuk mencapai akurasi deteksi dan segmentasi maksimal.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengembangan robot pemanen buah otomatis di lingkungan kebun luar ruangan (*outdoor orchard*) menghadapi berbagai tantangan alami yang kompleks. Sebelum penelitian ini dilakukan, sebagian besar sistem penginderaan robot hanya berfokus pada deteksi buah menggunakan kotak pembatas (*bounding box*) 2D tanpa memperhitungkan geometri buah atau keberadaan cabang pohon yang menghalanginya. Padahal, untuk melakukan pemetikan yang sukses, robot membutuhkan informasi orientasi cengkeraman (*grasp pose*) dan batas fisik buah agar tidak merusak kulit apel saat dijepit oleh efektor akhir (*end-effector*).

Tantangan lainnya adalah rintangan berupa cabang dan ranting pohon. Jika lengan robot menabrak cabang saat bergerak menuju buah target, hal itu dapat merusak mekanis robot atau merusak pohon. Oleh karena itu, sistem persepsi robot harus mampu mendeteksi letak cabang di sekitar buah target secara simultan. Namun, pendekatan terdahulu umumnya memisahkan modul deteksi buah dan deteksi cabang ke dalam dua sistem yang berbeda, sehingga meningkatkan beban komputasi (*computational overhead*) secara drastis. Ketiadaan model persepsi satu tahap (*one-stage*) yang ringan dan mampu menghasilkan informasi spasial 3D buah sekaligus cabang secara bersamaan menjadi celah teknologi (*technology gap*) utama dalam bidang ini.

## Ide Utama
Gagasan inti dari penelitian ini adalah menyatukan tugas deteksi buah, segmentasi instansi buah, dan segmentasi semantik cabang ke dalam sebuah arsitektur jaringan satu tahap (*single-stage network*) dengan tulang punggung ekstraksi fitur yang dibagi bersama (*shared feature extractor*). Dengan membagi ekstraktor fitur yang sama, model hanya perlu melakukan satu kali umpan maju (*forward pass*) untuk memproses citra masukan, sehingga menghemat memori GPU (*Graphics Processing Unit*) and waktu komputasi secara signifikan.

Untuk mengolah kompleksitas visual kebun, DaSNet-V2 memanfaatkan informasi spasial dari sensor RGB-D. Model ini melakukan deteksi dan segmentasi 2D terlebih dahulu pada citra RGB. Hasil segmentasi 2D berupa masker piksel buah dan cabang kemudian disatukan (*fused*) dengan saluran kedalaman (*depth channel*) untuk memproyeksikan piksel-piksel tersebut ke dalam koordinat kartesian 3D menggunakan parameter intrinsik kamera. Pendekatan hibrida ini memberikan keseimbangan optimal antara kecepatan komputasi 2D yang tinggi dan kebutuhan visualisasi geometri 3D yang akurat.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi Input dan Prapemrosesan Citra
Proses dimulai dengan pengambilan data citra dari kamera sensor kedalaman RGB-D. Citra masukan disesuaikan ukurannya (*rescaling*) menjadi resolusi 369 × 277 piksel untuk meminimalkan beban komputasi tanpa menghilangkan fitur-fitur spasial esensial. Tapis Laplace (*Laplace filter*) diterapkan pada tahap prapemrosesan untuk mempertajam batas tepi buah guna mempermudah ekstraksi fitur.

### 2. Ekstraksi Fitur Menggunakan Shared Backbone
Citra RGB dimasukkan ke dalam jaringan tulang punggung (*backbone network*) yang dibagi bersama. Terdapat dua pilihan tulang punggung yang digunakan:
- **LW-net (Lightweight Backbone)**: Berbasis arsitektur jaringan sisa (*residual network*) ringan (mirip ResNet-18) yang menggunakan blok sisa leher botol (*bottleneck residual blocks*) untuk mempercepat transmisi data dan mengurangi jumlah parameter model pada komputer tertanam.
- **ResNet-101**: Digunakan ketika prioritas sistem adalah akurasi deteksi maksimal tanpa batasan ketat pada waktu komputasi.

### 3. Modul ASPP dan Gate FPN (GFPN)
Fitur dari tulang punggung dilewatkan ke modul *Atrous Spatial Pyramid Pooling* (ASPP) untuk menangkap informasi konteks multi-skala dengan laju dilatasi (*dilation rates*) yang berbeda. Selanjutnya, fitur dialirkan ke *Gate Feature Pyramid Network* (GFPN) yang menyaring (*gating*) fitur-fitur dari berbagai tingkat resolusi, memperkuat sinyal visual objek target (buah dan cabang), serta menekan derau latar belakang kebun.

### 4. Multi-Task Output Head
Setelah melalui GFPN, peta fitur dialirkan ke tiga kepala prediksi (*prediction heads*) paralel:
- **Kepala Deteksi Buah**: Menghasilkan kotak pembatas (*bounding box*) 2D beserta skor keyakinan (*confidence score*).
- **Kepala Segmentasi Instansi Buah**: Menghasilkan masker biner piksel untuk setiap apel secara terpisah.
- **Kepala Segmentasi Semantik Cabang**: Menghasilkan masker piksel untuk seluruh area cabang dalam citra secara keseluruhan sebagai rintangan.

### 5. Proyeksi Kedalaman dan Visualisasi 3D
Masker piksel 2D untuk buah dan cabang diintegrasikan dengan matriks data kedalaman dari saluran D. Setiap piksel dengan koordinat $(u, v)$ dan nilai kedalaman $d$ diproyeksikan ke dalam koordinat kartesian 3D $(X, Y, Z)$ melalui persamaan geometri kamera:

$$X = \frac{(u - c_x) \cdot d}{f_x}$$
$$Y = \frac{(v - c_y) \cdot d}{f_y}$$
$$Z = d$$

Hasil proyeksi ini berupa awan titik (*point cloud*) berwarna yang tersegmen untuk apel dan cabang, yang kemudian dikirim ke perencana gerakan lengan robot untuk menghitung lintasan penjangkauan buah apel tanpa menabrak cabang terdekat.

Berikut adalah diagram alur arsitektur sistem persepsi DaSNet-V2 secara keseluruhan:

```
                                 [ Citra RGB-D ]
                                        │
                         ┌──────────────┴──────────────┐
                         ▼                             ▼
                    [ Citra RGB ]                [ Saluran Depth ]
                         │                             │
                         ▼                             │
                 [ Shared Backbone ]                   │
                (LW-net / ResNet-101)                  │
                         │                             │
                         ▼                             │
              [ ASPP & Gate FPN (GFPN) ]               │
                         │                             │
        ┌────────────────┼────────────────┐            │
        ▼                ▼                ▼            │
  [ Head Deteksi ] [ Head Seg. Buah ] [ Head Seg. Cabang ]  │
   (Bounding Box)   (Instansi Apel)   (Semantik Cabang)│
        │                │                │            │
        └────────────────┼────────────────┘            │
                         ▼                             │
                 [ Masker Piksel 2D ]                  │
                         │                             │
                         └──────────────┬──────────────┘
                                        ▼
                              [ Fusi Spasial 2D-3D ]
                            (Persamaan Geometri Kamera)
                                        │
                                        ▼
                             [ Visualisasi 3D Scene ]
                              (Segmented Point Cloud)
                                        │
                                        ▼
                          [ Kontrol & Perencanaan Robot ]
```

## Eksperimen dan Hasil
Eksperimen untuk mengevaluasi kinerja DaSNet-V2 dilakukan di area kebun apel Fuji di Qingdao, China. Dataset pengujian mencakup variasi kondisi pencahayaan alami di lapangan, seperti penyinaran langsung dari depan (*front-lighting*), dari belakang (*back-lighting*), bayangan daun, serta pencahayaan buatan pada malam hari. Pengambilan data dilakukan pada jarak 0,3 hingga 1,0 meter dari kamera ke buah.

Berdasarkan hasil eksperimen, DaSNet-V2 dengan tulang punggung ResNet-101 mencapai skor F1 sebesar 0,832 untuk deteksi buah, akurasi segmentasi instansi buah sebesar 87,6%, dan akurasi segmentasi semantik cabang sebesar 77,2%. Sementara itu, dengan tulang punggung ringan LW-net, model ini mencapai skor F1 deteksi buah sebesar 0,827, akurasi segmentasi instansi buah sebesar 86,5%, dan akurasi segmentasi semantik cabang sebesar 75,7%.

Interpretasi hasil ini menunjukkan adanya kompromi (*trade-off*) yang kecil pada akurasi demi efisiensi komputasi. Penggunaan LW-net hanya menurunkan skor F1 deteksi sebesar 0,005 dan akurasi segmentasi buah sebesar 1,1% dibandingkan dengan ResNet-101. Namun, model dengan LW-net mampu menyelesaikan proses inferensi dalam waktu 287 milidetik (ms) per citra pada NVIDIA Jetson TX2. Kecepatan ini memenuhi syarat minimum operasional robot pemanen di lapangan (di bawah 300 ms) agar robot dapat beroperasi tanpa jeda berhenti yang lama.

## Kelebihan dan Keterbatasan
Kelebihan utama DaSNet-V2 adalah integrasi tiga tugas visual (deteksi buah, segmentasi instansi buah, dan segmentasi cabang) ke dalam satu jaringan satu tahap yang efisien. Penggunaan *shared backbone* dan prapemrosesan yang dioptimalkan memungkinkan model ini diimplementasikan secara langsung pada perangkat komputasi tepi (*embedded device*) robot di lapangan. Selain itu, fusi spasial langsung antara peta segmentasi 2D dan data kedalaman RGB-D menghasilkan *point cloud* 3D tersegmen secara langsung, mempermudah kontrol gerakan robot (*motion planning*) dan estimasi orientasi cengkeraman (*grasp pose*).

Keterbatasan konseptual model ini adalah deteksi cabang pohon yang masih berupa segmentasi semantik, bukan segmentasi instansi. Akibatnya, sistem tidak dapat membedakan batas-batas fisik antara cabang yang saling tumpang tindih, yang menyulitkan perencanaan gerakan robot di dalam kanopi pohon yang rimbun. Secara rekayasa, keandalan sistem sangat bergantung pada kualitas sensor kedalaman RGB-D. Pada siang hari dengan sinar matahari terik, sensor kedalaman berbasis cahaya terstruktur atau waktu terbang (*Time-of-Flight*) sering kali mengalami gangguan akibat radiasi inframerah matahari.

## Kaitan dengan Bab Lain
DaSNet-V2 merupakan evolusi penting dalam klaster **Pertanian** dan memiliki keterkaitan erat dengan bab-bab penelitian deteksi buah apel lainnya. Secara khusus, bab ini mewarisi fokus deteksi objek apel dari [Apple Detection (Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md) yang mengoptimalkan model YOLOv3 untuk mendeteksi apel di kebun secara cepat. Namun, jika [Apple Detection (Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md) hanya menghasilkan kotak pembatas 2D, DaSNet-V2 menghasilkan segmentasi instansi buah dan deteksi cabang pohon sebagai rintangan.

Kaitan erat juga terlihat dengan [Apple Detection RGB+Depth (Faster R-CNN)](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) yang menggunakan Faster R-CNN dua tahap dengan masukan RGB-D untuk deteksi buah. DaSNet-V2 menerapkan model satu tahap yang jauh lebih efisien untuk dijalankan pada perangkat tepi. Di sisi lain, DaSNet-V2 berbagi tujuan rekonstruksi 3D lingkungan dengan penelitian oleh Gene-Mola dkk. pada [Fruit Detection & 3D Location (Gene-Mola dkk.)](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md), yang melokalisasi buah apel dalam 3D menggunakan sensor RGB-D Kinect v2 dan SfM (*Structure-from-Motion*). Kontribusi unik DaSNet-V2 dibandingkan penelitian Gene-Mola dkk. adalah penyertaan segmentasi cabang pohon secara semantik untuk keperluan penghindaran rintangan secara dinamis.

Dari aspek integrasi robotik, metode ini menjadi basis data persepsi bagi robot panen buah otomatis pada [Automated Fruit Harvesting Robot (Onishi dkk.)](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md) dan [Iceberg Lettuce Harvesting Robot](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md), menandai pergeseran fokus riset menuju pemahaman geometri 3D scene secara menyeluruh guna mendukung aksi fisik robot di dunia nyata.

## Poin untuk Sitasi
Untuk merujuk penelitian ini dalam karya ilmiah, dapat digunakan kunci BibTeX berikut:
`kang2020strawberry` (Catatan: Kunci BibTeX ini dipertahankan sesuai dengan sistem indeks database repositori untuk memastikan integritas tautan rujukan).

Ringkasan kalimat yang aman untuk dikutip:
"Kang dan Chen (2020) mengusulkan DaSNet-V2, sebuah jaringan satu tahap multi-tugas yang mengintegrasikan deteksi buah apel, segmentasi instansi buah, dan segmentasi semantik cabang dalam satu arsitektur terpadu. Dengan memanfaatkan data RGB-D, sistem ini mampu merekonstruksi visualisasi 3D lingkungan kebun apel secara *real-time* pada komputer tertanam NVIDIA Jetson TX2 untuk memandu pergerakan lengan robot pemanen dan menghindari rintangan cabang."

Catatan verifikasi data:
Angka hasil eksperimen utama seperti skor F1 deteksi buah sebesar 0,827 (LW-net) dan 0,832 (ResNet-101), serta akurasi segmentasi buah sebesar 86,5% (LW-net) dan 87,6% (ResNet-101) telah diverifikasi langsung dari naskah publikasi resmi di Computers and Electronics in Agriculture (Vol. 171, 105302). Pengujian dilakukan pada kebun apel Fuji di Qingdao, China, dengan jarak pemotretan 0,3 hingga 1,0 meter dari kamera ke buah.
