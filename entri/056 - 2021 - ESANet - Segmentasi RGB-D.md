# 056 - Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `seichter2021esanet` |
| Judul asli | Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis |
| Penulis | Daniel Seichter, Mona Köhler, Benjamin Lewandowski, Tim Wengefeld, Horst-Michael Gross |
| Tahun | 2021 |
| Venue | IEEE International Conference on Robotics and Automation (ICRA 2021), hlm. 13525–13531 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2011.06961
- **Kode sumber resmi (PyTorch + TensorRT):** https://github.com/TUI-NICR/ESANet
- **Google Scholar:** https://scholar.google.com/scholar?q=Efficient%20RGB-D%20Semantic%20Segmentation%20for%20Indoor%20Scene%20Analysis
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Efficient%20RGB-D%20Semantic%20Segmentation%20for%20Indoor%20Scene%20Analysis&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ESANet (*Efficient Scene Analysis Network*), jaringan segmentasi semantik RGB-D yang dirancang untuk robot mobile dengan daya komputasi terbatas. Segmentasi semantik adalah pemberian label kelas pada setiap piksel; RGB-D berarti masukan berupa citra warna (RGB) dan citra kedalaman (*depth*) yang teregistrasi. Masalahnya, metode segmentasi RGB-D yang akurat pada masa itu memakai dua sampai tiga encoder dalam dan terlalu lambat untuk inferensi *real-time* (mengikuti laju kamera) pada perangkat robot.

Hasil utama: pada dataset NYUv2, varian ESANet-R34-NBt1D mencapai 50,30 mIoU pada 29,7 *frame* per detik (FPS) di NVIDIA Jetson AGX Xavier dengan optimasi TensorRT. SA-Gate yang berakurasi setara mencapai 50,4 mIoU tetapi hanya 11,9 FPS pada perangkat yang sama.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Robot mobile di lingkungan dalam ruangan menjalankan beberapa tugas persepsi sekaligus — penghindaran rintangan, pemetaan, navigasi, persepsi manusia — dengan daya komputasi dan baterai terbatas. Segmentasi semantik cocok menjadi tahap pemrosesan awal bersama karena masker kelas per piksel dapat dipakai ulang oleh banyak tugas lanjutan. Deteksi manusia cukup dijalankan pada daerah berlabel "orang"; piksel berlabel "lantai" menandai ruang bebas gerak.

Adegan dalam ruangan umumnya rapat dengan objek yang saling menutupi. Informasi kedalaman memberi isyarat geometris yang tidak bergantung pencahayaan, dan terbukti menaikkan akurasi segmentasi sejak FuseNet (bab 051) dan RedNet (bab 052). Masalahnya, metode RGB-D yang akurat pada 2017–2020 memakai encoder ResNet-50 sampai ResNet-152 ganda dengan mekanisme fusi berlapis. RDFNet (bab 053) dengan dua encoder ResNet-152 hanya berjalan 5,8 FPS dan SA-Gate (bab 055) 11,9 FPS pada Jetson AGX Xavier. Di sisi lain, riset segmentasi efisien (ERFNet, SwiftNet, BiSeNet) berfokus pada RGB saja dan umumnya diuji pada GPU kelas atas, bukan perangkat *embedded* (tertanam) robot. Celah yang diisi makalah ini: arsitektur RGB-D yang akurat sekaligus cukup cepat untuk *real-time* pada perangkat robot.

## Ide Utama

Gagasan inti ESANet: dua encoder dangkal yang dirancang hemat, digabung dengan fusi murah, dapat menyamai metode RGB-D yang jauh lebih berat asalkan tiap komponen kompatibel dengan pengoptimal inferensi. Citra RGB dan citra kedalaman masing-masing diproses oleh encoder ResNet-34 yang blok konvolusinya difaktorkan sehingga lebih sedikit operasinya. Pada lima tingkat resolusi, fitur kedalaman ditimbang per kanal dengan mekanisme perhatian (*attention*) lalu dijumlahkan ke fitur RGB. Sebuah decoder dangkal dengan *upsampling* yang dipelajari memulihkan resolusi penuh. Karena seluruh komponen memakai operasi standar, jaringan dapat dikompilasi menjadi satu graf NVIDIA TensorRT.

## Cara Kerja Langkah demi Langkah

Alur data lengkap dari dua masukan ke peta kelas akhir:

```
citra RGB 640x480                citra depth 640x480
      │                                │
      ▼                                ▼
┌───────────────┐                ┌───────────────┐
│ encoder RGB   │                │ encoder depth │
│ ResNet34      │                │ ResNet34      │
│ (blok NBt1D)  │                │ (blok NBt1D)  │
└──────┬────────┘                └──────┬────────┘
       │   fusi pada 5 tingkat resolusi │
       │  ┌─────────────────────────────┴─┐
       │  │ fitur tiap modalitas ditimbang│
       └─►│ per kanal dengan modul SE,    │
          │ lalu dijumlahkan per elemen   │
          └──────────────┬────────────────┘
                         ▼
              peta fitur gabungan 20x15
              (1/32 resolusi masukan)
                    ┌────────────┐
                    │   modul    │ pooling global
                    │  konteks   │ + pooling 4x3
                    └─────┬──────┘
                          ▼
   ┌───────────────────────────────────────────┐
   │ decoder: 3 modul                          │
   │ (konv 3x3 -> 3 blok NBt1D -> upsampling   │
   │  terpelajari x2); skip connection dari    │
   │  encoder diproyeksikan konv 1x1 lalu      │
   │  dijumlahkan ke peta decoder              │
   └──────────────────┬────────────────────────┘
                      ▼
        peta kelas 160x120 (1/4 resolusi)
        -> 2 upsampling terpelajari lagi (x2)
                      ▼
            segmentasi akhir 640x480
```

### Dua Encoder dengan Blok Konvolusi Terfaktor (NBt1D)

Encoder adalah bagian jaringan yang mengekstrak fitur sekaligus mengecilkan resolusi. ESANet memakai dua encoder ResNet-34, satu untuk RGB dan satu untuk kedalaman. ResNet adalah keluarga jaringan konvolusi dengan sambungan residual (keluaran blok dijumlahkan dengan masukannya) yang menjadi *backbone* standar visi komputer. Berbeda dengan metode segmentasi akurat yang mengganti konvolusi berlangkah (*stride*) dengan konvolusi terdilatasi demi menjaga resolusi, ESANet membiarkan resolusi turun 32 kali: pada masukan 640×480, peta fitur akhir encoder berukuran 20×15. Pengecilan resolusi agresif ini adalah sumber utama kecepatannya.

Perubahan kedua ada pada blok dasar ResNet. Setiap konvolusi 3×3 diganti pasangan konvolusi 3×1 dan 1×3 yang diselingi aktivasi ReLU. Blok ini disebut *Non-Bottleneck-1D* (NBt1D) dan diambil dari ERFNet. Konvolusi 3×3 memerlukan 9 perkalian per piksel per kanal; pasangan 3×1 dan 1×3 hanya 3+3=6, sehingga biaya turun sekitar sepertiga tanpa mengubah ukuran medan reseptif (luas daerah masukan yang memengaruhi satu piksel keluaran). Uji ablasi menunjukkan penggantian ini memperbaiki akurasi dan kecepatan sekaligus: pada varian ResNet-34, mIoU NYUv2 naik dari 48,81 menjadi 50,30 dan FPS dari 27,5 menjadi 29,7. Kedua encoder dilatih awal (*pretraining*) pada dataset klasifikasi ImageNet sebelum disetel untuk segmentasi.

### Fusi Kedalaman dengan Penimbangan Kanal SE

Citra kedalaman memiliki statistik yang berbeda dari RGB karena nilai pikselnya menyatakan jarak, bukan warna. Karena itu kedalaman diproses pada cabang terpisah, bukan ditumpuk sebagai kanal keempat. Pada kelima tingkat resolusi encoder, fitur kedalaman difusikan ke encoder RGB. Sebelum dijumlahkan per elemen, fitur kedua modalitas ditimbang ulang per kanal dengan modul *Squeeze-and-Excitation* (SE): setiap kanal peta fitur dirangkum menjadi satu angka rata-rata global, lalu dua lapis terhubung penuh dan fungsi sigmoid menghasilkan satu bobot per kanal yang mengalikan peta fitur tersebut. Jaringan dengan demikian belajar menekan kanal modalitas yang tidak membantu dan menonjolkan yang informatif, tergantung isi masukan. Uji ablasi menunjukkan penimbangan SE sebelum fusi menaikkan mIoU secara terpisah dari komponen lain.

### Modul Konteks dengan Pooling Ukuran Tetap

Medan reseptif efektif encoder dangkal ini terbatas. ESANet menambahkan modul konteks bergaya *Pyramid Pooling Module* (PPM) dari PSPNet: fitur dirangkum pada beberapa ukuran *pooling* secara paralel lalu digabungkan, sehingga jaringan melihat konteks global dan lokal sekaligus. Agar kompatibel dengan TensorRT — yang hanya mendukung *pooling* berukuran tetap — ukuran *pooling* dipilih sebagai faktor dari resolusi masukan modul. Pada masukan 640×480, masukan modul konteks berukuran 20×15, sehingga dipakai dua cabang: *pooling* rata-rata global (20×15 menjadi 1×1) dan *pooling* 4×3.

### Decoder dengan Upsampling Terpelajari

Decoder memulihkan resolusi dan menghasilkan label kelas per piksel. ESANet memakai tiga modul decoder. Setiap modul terdiri atas konvolusi 3×3 (512 kanal pada modul pertama, menurun seiring kenaikan resolusi), tiga blok NBt1D tambahan, dan *upsampling* dua kali lipat. *Upsampling* tidak memakai *transposed convolution* — konvolusi balik yang mahal dan menimbulkan artefak pola grid — melainkan *upsampling* terpelajari yang ringan: resolusi diperbesar dengan interpolasi *nearest neighbor* (piksel terdekat digandakan), lalu konvolusi 3×3 *depthwise* (tiap kanal dikonvolusi terpisah) menggabungkan fitur piksel bertetangga. Kernel konvolusi ini diinisialisasi agar meniru interpolasi bilinear, kemudian bobotnya ikut dilatih. Penggantian dari bilinear ke *upsampling* terpelajari menaikkan mIoU 0,9 poin pada ablasi.

Detail halus yang hilang saat pengecilan resolusi dikembalikan lewat *skip connection* (sambungan lompatan): peta fitur gabungan RGB-D dari tingkat encoder beresolusi sama diproyeksikan dengan konvolusi 1×1 untuk menyesuaikan jumlah kanal, lalu dijumlahkan ke peta decoder. Decoder hanya memproses fitur sampai resolusi seperempat masukan (160×120). Sebuah konvolusi 3×3 kemudian memetakan fitur ke 40 kelas NYUv2, dan dua modul *upsampling* terpelajari terakhir mengembalikan resolusi penuh 640×480.

### Supervisi dan Optimasi Inferensi

Pelatihan memakai supervisi pada setiap skala decoder: konvolusi 1×1 menghasilkan segmentasi beresolusi kecil dari tiap modul yang dibandingkan dengan peta label yang diperkecil. Jaringan dilatih 500 *epoch* (putaran penuh atas data latih) dengan batch 8, pengoptimal SGD (momentum 0,9) atau Adam, penjadwal laju pembelajaran *one-cycle*, serta augmentasi penskalaan, pemotongan, pembalikan, dan jitter warna HSV. Kelas langka ditangani dengan *median frequency balancing* (bobot kelas dari kebalikan frekuensi kemunculannya). Untuk penerapan, jaringan diekspor ke ONNX (format pertukaran model antar-*framework*) lalu dikompilasi menjadi satu graf TensorRT dengan presisi Float16. Inferensi menjadi sampai lima kali lebih cepat daripada PyTorch pada perangkat yang sama.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tiga dataset. NYUv2 memuat 1.449 citra RGB-D dalam ruangan (795 latih, 654 uji) dengan 40 kelas. SUNRGB-D memuat 10.335 citra (5.285 latih, 5.050 uji) dengan 37 kelas. Cityscapes memuat 5.000 citra jalanan beranotasi halus dalam 19 kelas pada resolusi 2048×1024, dengan kedalaman dihitung dari peta *disparity* (selisih posisi objek pada pasangan kamera stereo). Metrik utama adalah mIoU (*mean Intersection over Union*): rata-rata, per kelas, dari rasio luas irisan terhadap luas gabungan antara piksel prediksi dan piksel kebenaran. Kecepatan diukur pada NVIDIA Jetson AGX Xavier (TensorRT 7.1, Float16) — perangkat yang dipasang pada robot, bukan GPU server.

Hasil utama pada dataset uji:

- ESANet-R34-NBt1D: 50,30 mIoU NYUv2 dan 48,17 mIoU SUNRGB-D pada 29,7 FPS.
- Varian yang sama dengan pelatihan awal pada SceneNet RGB-D (data sintetis): 51,58 mIoU NYUv2 — tertinggi pada tabel perbandingan makalah — pada kecepatan sama.
- Pembanding: SA-Gate 50,4 mIoU NYUv2 pada 11,9 FPS; ACNet 48,3/48,1 mIoU pada 16,5 FPS; RDFNet dengan ResNet-152 50,1/47,7 mIoU pada 5,8 FPS.

Interpretasinya: ESANet menyamai akurasi SA-Gate di NYUv2 (selisih 0,1 poin) dengan kecepatan 2,5 kali lipat, dan mengalahkan RDFNet-152 pada kedua dataset dengan kecepatan lima kali lipat. Pelatihan awal pada data sintetis menambah 1,28 poin mIoU NYUv2, lebih besar daripada perpindahan ke *backbone* lebih dalam — ResNet-50 hanya menambah 0,23 poin tetapi memperlambat inferensi dari 29,7 menjadi 22,6 FPS. Perbandingan modalitas memperkuat desain dua cabang: jaringan RGB-D berbasis ResNet-18 mengalahkan jaringan RGB saja berbasis ResNet-50 yang jauh lebih dalam, sekaligus lebih cepat.

Pada Cityscapes, varian RGB tunggal ESANet-R34-NBt1D pada resolusi 1024×512 berjalan di atas 30 FPS dan melampaui metode efisien lain (ERFNet, LEDNet, ESPNetv2, SwiftNet) setidaknya 2,2 poin mIoU. Bobot resmi RGB-D mencapai 75,22 mIoU pada 23,4 FPS (1024×512) dan 80,09 mIoU pada 6,2 FPS saat dievaluasi pada resolusi penuh 2048×1024. Peningkatan dari kedalaman lebih kecil daripada di NYUv2; penulis menduga peta *disparity* Cityscapes kurang presisi dibandingkan kedalaman sensor dalam ruangan. Makalah juga melaporkan penerapan pada robot bersensor Kinect2 untuk persepsi manusia, deteksi ruang bebas, dan pemetaan semantik.

## Kelebihan dan Keterbatasan

Kelebihan. Pertama, akurasi setara metode berat dicapai dengan kecepatan 2,5 sampai 5 kali lipat pada perangkat *embedded* yang benar-benar dipakai robot. Kedua, seluruh komponen berupa operasi standar sehingga kompatibel ONNX dan TensorRT; sebagian metode pembanding memuat operasi yang tidak didukung TensorRT. Ketiga, kode dan bobot terlatih tersedia terbuka sehingga dapat direproduksi. Keempat, terbukti berlaku di luar domain dalam ruangan (Cityscapes).

Keterbatasan. Akurasi absolutnya tetap di bawah metode terberat pada SUNRGB-D (48,17 berbanding 49,4 milik SA-Gate). Ketergantungan pada kualitas kedalaman tampak dari kecilnya peningkatan pada Cityscapes; dari sisi rekayasa, perpindahan sensor kedalaman juga berisiko karena pada SUNRGB-D mIoU per kamera bervariasi dari 32,42 sampai 53,39. Angka FPS terikat pada kombinasi perangkat dan pustaka tertentu (Jetson AGX Xavier, Jetpack 4.4, TensorRT 7.1), sehingga tidak otomatis berlaku pada perangkat lain. Secara konseptual, dua encoder ResNet-34 masih lebih berat daripada arsitektur yang dirancang khusus untuk efisiensi, sehingga ruang penghematan tambahan tetap terbuka.

## Kaitan dengan Bab Lain

ESANet melanjutkan garis fusi dua cabang yang diletakkan [FuseNet (bab 051)](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) dan [RedNet (bab 052)](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md): fitur kedalaman disuntikkan ke encoder RGB pada banyak tingkat resolusi, bukan hanya di awal atau di akhir. Terhadap mekanisme perhatian yang lebih berat pada [ACNet (bab 054)](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) dan [SA-Gate (bab 055)](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md), ESANet menunjukkan bahwa penimbangan kanal SE yang ringan sudah memadai. [RDFNet (bab 053)](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) menempuh jalur berbeda dengan memakai fitur kedua modalitas di decoder; ESANet tetap memakai satu decoder untuk fitur gabungan demi efisiensi. Makalah ini juga menjadi pembanding praktis bagi konvolusi khusus kedalaman seperti [ShapeConv (bab 057)](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md), karena konvolusi standar 3×3 yang teroptimasi perangkat keras ternyata lebih cepat. Generasi berikutnya seperti [CMX (bab 058)](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) mengejar akurasi lebih tinggi dengan arsitektur transformer lintas modalitas.

## Poin untuk Sitasi

Kutip dengan kunci `seichter2021esanet`. Ringkasan yang aman dikutip: "ESANet adalah arsitektur segmentasi semantik RGB-D yang efisien, terdiri atas dua encoder ResNet terfaktor (blok NBt1D), fusi kedalaman berbasis Squeeze-and-Excitation, dan decoder dengan upsampling terpelajari. Arsitektur ini mencapai akurasi setara metode yang jauh lebih berat sekaligus inferensi real-time pada perangkat embedded NVIDIA Jetson AGX Xavier."

Angka mIoU dan FPS di bab ini berasal dari Tabel I naskah (arXiv:2011.06961v3) dan README repositori resmi; FPS berlaku untuk konfigurasi Jetpack 4.4, TensorRT 7.1, Float16. Angka Cityscapes (75,22 dan 80,09 mIoU) bersumber dari README repositori — Tabel II naskah sebaiknya diperiksa langsung sebelum sitasi formal. Klaim ">30 FPS dan +2,2 mIoU" pada Cityscapes merujuk pada varian RGB tunggal, bukan model RGB-D.
