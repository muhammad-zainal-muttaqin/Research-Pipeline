# 084 - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fang2020graspnet` |
| Judul asli | GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping |
| Penulis | Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Grasp Robotik |

## Tautan Akses
- **Halaman proyek (dataset + kode):** https://graspnet.net/
- **Kode baseline (GitHub):** https://github.com/graspnet/graspnet-baseline
- **Google Scholar:** https://scholar.google.com/scholar?q=GraspNet-1Billion%3A%20A%20Large-Scale%20Benchmark%20for%20General%20Object%20Grasping
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=GraspNet-1Billion%3A%20A%20Large-Scale%20Benchmark%20for%20General%20Object%20Grasping&sort=relevance

## Gambaran Umum

Makalah ini bukan usulan satu arsitektur, melainkan sebuah *benchmark*: dataset berskala besar beserta protokol evaluasi baku untuk masalah *grasping* objek umum, yaitu memprediksi cara sebuah lengan robot mencengkeram objek yang sebelumnya tidak dikenal. GraspNet-1Billion menyediakan 190 pemandangan (*scene*) meja berisi tumpukan objek, direkam sebagai 97.280 citra RGB-D (citra warna yang setiap pikselnya juga menyimpan jarak ke kamera), dan dianotasi dengan lebih dari 1,1 miliar *grasp pose* enam derajat kebebasan (6-DoF). Setiap anotasi grasp diberi label kualitas melalui perhitungan analitik, bukan pelabelan manual satu per satu, sehingga jumlah anotasi dapat mencapai orde miliaran.

Kontribusi makalah ada tiga: dataset berskala besar dengan anotasi grasp padat, metrik evaluasi analitik yang menilai grasp apa pun tanpa memerlukan daftar jawaban benar yang lengkap, dan satu jaringan *baseline* ujung-ke-ujung (*end-to-end*) yang memprediksi grasp langsung dari *point cloud* (himpunan titik 3D hasil proyeksi citra kedalaman). Ketiganya bersama-sama menstandarkan penilaian riset grasp, yang sebelumnya sulit dibandingkan antar-makalah karena setiap kelompok memakai objek, perangkat, dan definisi keberhasilan yang berbeda.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum GraspNet, dua dataset grasp berbasis pembelajaran yang paling banyak dipakai adalah Cornell Grasping Dataset dan Jacquard (bab 086). Keduanya memiliki dua keterbatasan struktural. Pertama, representasi grasp-nya *planar*: cengkeraman dinyatakan sebagai persegi panjang beorientasi pada bidang citra (posisi pusat, sudut putar, lebar), yang mengasumsikan robot mendekati objek tegak lurus dari atas. Representasi ini hanya mencakup empat derajat kebebasan efektif dan tidak dapat menyatakan pendekatan menyerong yang sering diperlukan pada objek nyata. Kedua, skalanya terbatas dan latar setnya sederhana; Cornell hanya memuat sekitar seribu citra objek tunggal, sehingga model yang dilatih padanya sukar digeneralisasikan ke tumpukan objek yang saling menutupi (*clutter*).

Masalah kedua yang lebih halus adalah evaluasi. Pada grasp 6-DoF, ruang kemungkinan cengkeraman untuk satu objek sangat besar dan kontinu, sehingga mustahil menyusun daftar lengkap semua grasp benar sebagai acuan. Akibatnya, banyak makalah menilai metode dengan eksperimen robot fisik pada sekumpulan kecil objek pilihan sendiri. Cara ini tidak dapat direproduksi: hasil satu laboratorium tidak sebanding dengan laboratorium lain karena objek, gripper, dan kriteria "berhasil" berbeda. Bidang ini membutuhkan tolok ukur bersama yang, seperti PASCAL VOC bagi deteksi objek (bab 001), memungkinkan perbandingan adil di atas data dan metrik yang sama.

## Ide Utama

Gagasan inti makalah adalah memindahkan beban pelabelan dari manusia ke perhitungan analitik, sehingga dataset grasp 6-DoF berskala besar menjadi mungkin. Untuk setiap objek, banyak kandidat grasp disebar di permukaan modelnya, lalu tiap kandidat dinilai dengan kriteria *force-closure*: sebuah grasp dikatakan stabil bila gaya kontak kedua jari gripper mampu menahan objek terhadap gaya dan torsi sembarang. Penilaian ini dihitung otomatis dari geometri kontak, tanpa percobaan fisik.

Karena setiap objek memiliki model 3D dan pose 6D-nya di setiap *scene* diketahui, label grasp yang dihitung pada satu objek dapat diproyeksikan ke seluruh *scene* dan seluruh sudut pandang kamera secara otomatis, dengan pemeriksaan tabrakan terhadap objek lain di tumpukan. Perkalian antara jumlah objek, jumlah *scene*, jumlah sudut pandang, dan jumlah kandidat grasp per objek inilah yang menghasilkan lebih dari satu miliar anotasi. Prinsip yang sama dipakai kembali saat evaluasi: kualitas grasp apa pun yang diprediksi model dapat dinilai langsung dengan force-closure, tanpa perlu mencocokkannya dengan daftar jawaban.

## Cara Kerja Langkah demi Langkah

### Pengumpulan Data

Sebanyak 190 *scene* disusun dari 88 objek yang setiap modelnya dipindai menjadi mesh 3D bertekstur. Tiap *scene* berisi sekitar sepuluh objek yang ditumpuk pada meja. Perekaman dilakukan oleh dua kamera RGB-D berbeda kualitas yang dipasang pada lengan robot — Intel RealSense D435 dan Microsoft Kinect Azure — sehingga metode dapat diuji ketahanannya terhadap perbedaan sensor. Lengan menggerakkan kamera menyusuri lintasan tetap sehingga setiap *scene* terekam dari banyak sudut. Total 97.280 citra RGB-D terkumpul; pembagiannya konsisten dengan 512 citra per *scene*, yaitu 256 sudut pandang untuk masing-masing dari dua kamera (97.280 ÷ 190 = 512; 512 ÷ 2 = 256).

### Anotasi Grasp 6-DoF

Sebuah *grasp pose* 6-DoF dinyatakan lengkap oleh posisi titik cengkeram dalam ruang 3D, arah pendekatan gripper (vektor menuju objek), sudut putar gripper terhadap sumbu pendekatannya, serta lebar bukaan jari. Enam derajat kebebasan (tiga translasi, tiga rotasi) inilah yang membedakannya dari grasp planar. Anotasi dibangun sekali per objek: kandidat grasp disampel padat pada permukaan mesh, dinilai dengan force-closure pada beberapa nilai koefisien gesek, lalu setiap kandidat menyandang skor kualitas. Label per objek kemudian ditransfer ke setiap *scene* memakai pose 6D objek dan disaring dengan pemeriksaan tabrakan terhadap tumpukan. Rata-rata, akumulasi ini menghasilkan lebih dari sepuluh ribu grasp berlabel per citra (1,1 miliar ÷ 97.280 ≈ 1,1 × 10⁴), padat jauh melampaui dataset planar terdahulu.

Diagram berikut merangkum aliran dari objek tunggal sampai anotasi tingkat *scene*:

```
  88 objek           190 scene              97.280 citra RGB-D
  (mesh 3D)          (tumpukan ~10 objek)   (2 kamera x 256 view)
      │                    │                        │
      ▼                    ▼                        ▼
  sampel grasp    ┌── pose 6D objek ──┐     proyeksi label +
  + skor force-   │   diketahui        │ ──> cek tabrakan per view
  closure         └────────────────────┘            │
      │                                              ▼
      └──────────────> label grasp per objek ──> >1,1 miliar grasp 6-DoF
```

### Metrik Evaluasi

Metrik utama adalah AP (*Average Precision*) berbasis force-closure. Model diminta menghasilkan sejumlah grasp untuk sebuah *scene*; tiap grasp prediksi dinilai langsung apakah *force-closure*-nya terpenuhi pada koefisien gesek tertentu, lalu dihitung Precision@k, yaitu proporsi grasp valid di antara k prediksi berperingkat teratas. Nilai AP adalah rata-rata Precision@k tersebut di seluruh nilai k dan seluruh koefisien gesek yang diuji. Koefisien gesek kecil berarti syarat stabil lebih ketat, sehingga notasi seperti AP0.8 dan AP0.4 menandai AP pada koefisien gesek 0,8 dan 0,4; angka AP0.4 selalu lebih rendah karena syaratnya lebih keras. Karena penilaian bersifat analitik, metrik ini menilai grasp apa pun tanpa daftar jawaban lengkap — inilah yang membuat evaluasi 6-DoF berskala besar menjadi praktis.

### Jaringan Baseline

*Baseline* memproses *point cloud* *scene* dengan tulang punggung (*backbone*) PointNet++, jaringan yang mengekstrak fitur langsung dari titik 3D tak beraturan. Prediksi grasp dipecah menjadi beberapa tahap terpisah. Tahap pertama memilih titik-titik kandidat dan memprediksi arah pendekatan gripper di tiap titik. Tahap kedua, bergantung pada arah tersebut, memprediksi parameter operasi gripper — sudut putar dalam bidang, lebar bukaan, dan kedalaman cengkeram. Pemisahan bertahap ini menyederhanakan ruang keluaran yang berdimensi tinggi menjadi sub-prediksi yang lebih mudah dipelajari, dan menghasilkan grasp 6-DoF utuh langsung dari satu *point cloud* tanpa tahap usulan eksternal.

## Eksperimen dan Hasil

Protokol pengujian membagi 190 *scene* menjadi 100 *scene* latih dan 90 *scene* uji. Bagian uji dipecah lagi menjadi tiga tingkat generalisasi berdasarkan kemiripan objeknya dengan objek latih: *seen* (objek yang sama dengan saat latih), *similar* (objek berbeda tetapi mirip), dan *novel* (objek yang sama sekali baru). Pembagian ini memisahkan hafalan dari generalisasi sejati: performa pada *novel* menunjukkan seberapa baik model mencengkeram objek yang belum pernah dilihat.

Menurut hasil yang dilaporkan repositori resmi untuk kamera RealSense (dengan pascapemrosesan deteksi tabrakan satu tampilan), *baseline* mencapai AP 47,47 pada *seen*, 42,27 pada *similar*, dan 16,61 pada *novel*. Pola angkanya informatif: performa turun tajam dari *similar* ke *novel*, memperlihatkan bahwa generalisasi ke bentuk objek yang benar-benar baru adalah bagian tersulit dari masalah ini dan menyisakan ruang besar untuk perbaikan. Nilai AP yang jauh di bawah 100 juga menegaskan bahwa *benchmark* ini tidak jenuh — masih menantang bagi metode sesudahnya, yang justru menjadi tujuan sebuah tolok ukur.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah skala dan kebakuan: dataset grasp 6-DoF nyata terbesar pada saat rilis, dengan dua kamera untuk menguji ketahanan lintas-sensor, dan metrik analitik yang dapat direproduksi tanpa robot fisik. Kombinasi ini menjadikannya infrastruktur bersama sehingga metode baru dapat dibandingkan pada dasar yang sama.

Keterbatasannya sebagian melekat pada pilihan desain. Secara konseptual, penilaian force-closure adalah model analitik stabilitas; grasp yang lolos secara analitik belum tentu berhasil pada perangkat fisik yang memiliki gesekan, deformasi, dan galat kalibrasi nyata, sehingga AP tinggi tidak otomatis berarti tingkat keberhasilan fisik tinggi. Dari sisi rekayasa, latar set terbatas pada tumpukan objek di atas meja yang direkam dengan satu jenis gripper paralel, sehingga generalisasi ke gripper lain atau latar di luar meja tidak dijamin. Selain itu, pemrosesan *point cloud* padat menuntut komputasi yang tidak ringan untuk penerapan waktu-nyata.

## Kaitan dengan Bab Lain

Bab ini berdiri sebagai lanjutan skala-besar dari dua dataset grasp planar terdahulu, terutama [086 - Jacquard Dataset](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md), yang juga menempuh jalan anotasi otomatis tetapi masih pada representasi planar; GraspNet menaikkannya ke 6-DoF dan latar tumpukan. Ia melengkapi garis metode prediksi grasp planar dari citra pada [082 - GR-ConvNet](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md) dan [083 - GR-ConvNet v2](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md) dengan menyediakan tolok ukur untuk grasp berbasis geometri 3D. Metrik dan datanya kemudian menjadi acuan evaluasi bagi metode fusi RGB-D pada [085 - BCMFNet](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md). Gagasan menghasilkan grasp langsung dari data sensor tanpa tahap usulan eksternal sejalan dengan semangat detektor satu tahap pada klaster Fondasi RGB, khususnya [001 - YOLOv1](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `fang2020graspnet`. Ringkasan yang aman dikutip: "GraspNet-1Billion adalah *benchmark* grasp 6-DoF berskala besar yang menyediakan 190 *scene* (97.280 citra RGB-D dari dua kamera), lebih dari 1,1 miliar anotasi grasp berbasis force-closure, sebuah metrik evaluasi analitik, dan jaringan *baseline* ujung-ke-ujung dari *point cloud*."

Angka yang telah terverifikasi dari halaman proyek resmi dan repositori: 190 *scene*, 88 objek, 97.280 citra RGB-D, dua kamera (RealSense D435 dan Kinect Azure), serta lebih dari 1,1 miliar grasp. Pembagian 100 *scene* latih / 90 *scene* uji terverifikasi dari ringkasan publik. Perlu diverifikasi ke naskah asli sebelum sitasi formal: (1) pembagian *scene* uji menjadi tepat 30 *seen* / 30 *similar* / 30 *novel* — belum dikonfirmasi dari sumber primer pada penulisan ini; (2) himpunan nilai koefisien gesek yang dipakai pada metrik AP (mis. rentang dan langkahnya); (3) nama dan pembagian tepat submodul *baseline* (ApproachNet / OperationNet / ToleranceNet) — struktur bertahapnya benar, tetapi penamaan komponen belum diverifikasi dari naskah; (4) angka AP *baseline* 47,47 / 42,27 / 16,61 berasal dari tabel repositori resmi (RealSense, dengan deteksi tabrakan satu tampilan) dan dapat berbeda dari tabel di naskah CVPR — cocokkan dengan tabel makalah asli.
