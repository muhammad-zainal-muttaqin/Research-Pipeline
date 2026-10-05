# A real-time semantic 3D vineyard mapping and fruit localization system for yield estimation in dynamic vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2026real` |
| Judul asli | A real-time semantic 3D vineyard mapping and fruit localization system for yield estimation in dynamic vineyards |
| Penulis | Yang, Runbin; Zhang, Xilong; Chen, Yanyang; Huang, Xiaotao; Feng, Sang |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [yang2026real.pdf](../pdf/yang2026real.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.101784

## Gambaran Umum

Makalah ini mengusulkan sistem pemetaan semantik 3D dan lokalisasi buah secara waktu nyata untuk estimasi hasil panen di kebun anggur yang dinamis, yaitu kebun yang dilalui orang. Sistem memadukan *backend* ORB-SLAM3 dengan jaringan segmentasi semantik ringan bernama EFSegNet, yang diturunkan dari PIDNet dengan dua tambahan: *Gradient Feature Fusion Block* (GFFM) pada cabang tepi dan *Deformable Spatial Attention* (DSA) pada cabang spasial. Masker semantik dipakai untuk membuang titik fitur dinamis (pejalan kaki) agar pelacakan SLAM stabil, dan untuk menandai titik awan buah. Awan titik global disaring dalam tiga tahap, lalu dikelompokkan dengan DBSCAN dan dimodelkan sebagai elipsoid lewat *Principal Component Analysis* (PCA) untuk memperoleh posisi 3D dan jumlah tandan anggur.

Data berasal dari kebun anggur hijau di Shangguo Pick-Your-Own Orchard, Distrik Panyu, Guangzhou, Tiongkok. Robot beroda dengan kamera stereo ZED2 merekam urutan citra; 940 citra RGB dipilih acak dan dianotasi tingkat piksel untuk dua kelas, yaitu buah dan pejalan kaki.

Hasil utama menurut abstrak: kecepatan 23,1 FPS, galat lokalisasi 3D rata-rata 21,02 mm, dan galat hitungan rata-rata 5,95% (dari dua skenario, 5,7% pada satu baris dan 6,2% pada dua baris). EFSegNet mencapai mIoU 89,45% dan *Boundary F-measure* 82,78% pada set uji, serta galat hitungan 6,23% pada subset yang sangat tertutup (PIDNet: 9,71%).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Robot inspeksi di kebun anggur perlu mengetahui sebaran buah dan hasil panen secara spasial. Penulis menyebut tiga masalah pada sistem yang ada: (a) peta rusak dan pelacakan melenceng akibat orang yang bergerak; (b) kendala komputasi yang mengganggu pemantauan waktu nyata; (c) hitungan tidak akurat karena agregasi spasial kasar di tajuk rapat. Segmentasi tandan anggur yang berbentuk tidak beraturan, tertutup, dan saling bersentuhan masih sulit. Jaringan ringan cenderung mengorbankan presisi batas demi kecepatan sehingga tandan yang bergerombol terhitung terlalu sedikit (*under-counting*), sedangkan arsitektur berbasis *Transformer* terlalu berat untuk platform bergerak.

Sistem SLAM buah terdahulu umumnya diuji pada skenario terkendali dan statis. Penulis juga membandingkan dengan jalur deteksi-pelacakan-penghitungan (*detection-tracking-counting*, DTC) murni visual, yang menurut mereka mengandalkan asosiasi 2D untuk menghilangkan duplikat dan dapat gagal ketika area dikunjungi ulang.

## Ide Utama

Gagasan pertama adalah memakai masker segmentasi untuk dua tujuan sekaligus: membuang titik fitur dinamis (pejalan kaki) dalam ORB-SLAM3 dan membentuk awan titik buah bersemantik. Gagasan kedua adalah memindahkan pencacahan ke ruang 3D. Tandan dikelompokkan sebagai gugus titik padat pada peta global yang berjangkar pada kerangka dunia SLAM, lalu tiap gugus dimodelkan sebagai elipsoid sehingga satu elipsoid dihitung sebagai satu tandan. Penulis berpendapat bahwa penjangkaran pada kerangka dunia SLAM mengurangi hitungan berulang dan memberi lokalisasi 3D setingkat sentimeter. Klaim pengurangan hitungan berulang ini tidak diuji secara terpisah dalam eksperimen (lihat bagian keterbatasan).

Gagasan ketiga adalah memperbaiki segmentasi batas tandan agar tandan yang bertumpuk terpisah. Untuk itu GFFM memadukan tiga konvolusi diferensial (pusat, sudut, dan radial) dengan jalur residual berpintu perhatian, sedangkan DSA memakai konvolusi *deformable* satu sumbu horizontal dan vertikal.

## Cara Kerja Langkah demi Langkah

```
  Citra stereo ──> EFSegNet ──> masker (buah / pejalan kaki)
        │                              │
        └──> ORB-SLAM3 (titik fitur dinamis dibuang)
                    │
   awan titik global (kedalaman keyframe + label semantik)
                    │
   voxel ──> outlier statistik ──> outlier radius
                    │
   DBSCAN (ε = 0,05 m, MinPts = 50) ──> PCA, elipsoid ──> posisi dan jumlah tandan
```

### 1. Akuisisi data dan perangkat

Platform adalah sasis diferensial berukuran 0,776 m × 0,671 m × 0,319 m, bobot 35,6 kg, kecepatan maksimum 1,65 m/s. Sensor utamanya ZED2 (stereo aktif dengan IMU, rentang kedalaman 0,2 sampai 20 m). *LiDAR* Robosense Helios 32 hanya dipakai untuk membuat acuan posisi 3D dan tidak ikut pada lintasan waktu nyata. Pemrosesan berjalan di laptop dengan CPU Intel i5-12500H, RAM 16 GB, dan GPU RTX 3060 (8 GB VRAM). Kamera dikonfigurasi 640 × 360 piksel pada 30 FPS. Dataset segmentasi terdiri atas 940 citra dengan pembagian latih, validasi, dan uji 8:1:1. Varietas anggur tidak dilaporkan (hanya disebut anggur hijau), dan jumlah pohon atau jumlah tandan total di kebun tidak dilaporkan.

### 2. Segmentasi semantik EFSegNet

EFSegNet mempertahankan struktur tiga cabang PIDNet (spasial, konteks, tepi). GFFM menggantikan konvolusi standar pada cabang tepi, dan DSA ditambahkan pada cabang spasial. Pelatihan memakai SGD, laju belajar 0,01, momentum 0,9, *weight decay* 0,005, ukuran *batch* 12, dan 60.000 iterasi (Tabel 1).

### 3. Pembuangan titik fitur dinamis

Satu utas segmentasi tambahan memberi masker pada tiap bingkai RGB. Pada tahap inisialisasi bingkai, titik fitur ORB yang jatuh pada label dinamis (pejalan kaki) dibuang, dan hanya titik latar statis yang dipakai untuk pelacakan dan pemetaan. Penanganan dinamika hanya untuk objek kaku seperti pejalan kaki; daun yang bergoyang karena angin tidak ditangani secara khusus.

### 4. Pemetaan semantik dan penyaringan awan titik

Awan titik padat dibangun dari kedalaman keyframe. Titik berlabel "grape" diwarnai sian, titik "pedestrian" dibuang, dan titik lain memakai warna RGB. Penyaringan tiga tahap terdiri atas penurunan sampel *voxel grid* (titik diganti centroid), pembuangan pencilan statistik (titik dibuang bila jarak rerata ke $k$ tetangga melebihi rerata global ditambah $\lambda \sigma$), dan pembuangan pencilan radius (titik dibuang bila jumlah tetangga dalam radius $r$ kurang dari $N_{min}$). Nilai $k$, $\lambda$, $r$, dan $N_{min}$ tidak dilaporkan pada teks.

### 5. Pengelompokan dan lokalisasi tandan

DBSCAN dengan $\varepsilon = 0{,}05$ m dan MinPts = 50 mengelompokkan titik anggur, dengan batas 5.000 titik per gugus agar fragmen tertutup tidak menyatu. PCA pada tiap gugus memberi pusat (rerata titik) sebagai posisi tandan dan panjang semi-sumbu elipsoid dari rentang tiap sumbu utama. Gugus dipertahankan hanya bila volume elipsoid $V_k$ berada pada $[0{,}001;\ 0{,}05]$ m³. Satu gugus yang lolos dihitung sebagai satu tandan.

## Eksperimen dan Hasil

Evaluasi mencakup enam aspek: segmentasi, pembuangan titik dinamis, rekonstruksi 3D, optimasi peta, lokalisasi dan hitungan tandan, serta kinerja waktu nyata. Acuan posisi 3D adalah centroid tandan yang dianotasi manual pada awan titik LiDAR (CloudCompare) setelah kalibrasi ekstrinsik LiDAR-kamera dengan papan catur, dengan sisa translasi rerata 2,91 mm (σ = 0,51 mm). Acuan jumlah tandan ("nilai sebenarnya" pada Tabel 7, 10, dan 11) tidak dijelaskan cara perolehannya dalam teks.

Segmentasi pada set data kebun anggur (Tabel 2; kelas buah dan pejalan kaki):

| Metode | mIoU (%) | mAcc (%) | FPS | Parameter (M) |
|---|---|---|---|---|
| DeepLabv3+ | 87,85 | 92,85 | 27,4 | 41,217 |
| BiSeNetv2 | 87,60 | 89,93 | 273,04 | 3,342 |
| SegFormer-B0 | 86,24 | 96,46 | 177,7 | 3,715 |
| DDRNet-23-slim | 88,02 | 92,88 | 321,94 | 5,732 |
| PIDNet | 88,41 | 92,9 | 162,16 | 28,759 |
| EFSegNet | 89,45 | 93,55 | 120,92 | 30,779 |

Ablasi (Tabel 3), mIoU dan *Boundary F-measure*: PIDNet 88,41 dan 78,32; ditambah GFFM 88,92 dan 80,28; ditambah jalur residual 89,12 dan 81,92; ditambah DSA (EFSegNet) 89,45 dan 82,78. FPS turun dari 162,16 menjadi 120,92.

Lokalisasi (Tabel 6) dan hitungan (Tabel 7), dengan galat relatif $|N_p - N_t| / N_t$:

| Skenario | RMSE 3D (mm) | Hitungan sebenarnya | Hitungan prediksi | Galat relatif |
|---|---|---|---|---|
| Urutan 1, pemindaian lateral | 19,02 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| Urutan 2, maju sepanjang baris | 20,98 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| Urutan 3, maju dengan pejalan kaki | 23,07 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| Rerata | 21,02 (SD 5,6) | | | |
| Satu baris | | 88 | 84 | 5,7% |
| Dua baris | | 146 | 137 | 6,2% |

Hasil lain: (1) Sensitivitas parameter DBSCAN (Tabel 8): $\varepsilon$ 0,04 sampai 0,06 m dan MinPts 40 sampai 60 menghasilkan galat 5,95% sampai 7,86%, terendah pada $\varepsilon$ 0,05 dan MinPts 50. (2) Pencahayaan (Tabel 9 dan 10): normal 19,73 mm dan galat hitungan 5,4% (92 sebenarnya, 87 prediksi); bayangan 21,99 mm dan 5,6% (89, 82); cahaya latar 25,22 mm dan 7,3% (96, 89). (3) Subset sangat tertutup (Tabel 11): EFSegNet mIoU 87,62% dan galat 6,23% (48 sebenarnya, 45 prediksi); PIDNet mIoU 84,14% dan galat 9,71% (48, 43). (4) Waktu per modul (Tabel 12): EFSegNet 7,57 ms, pelacakan 14,37 ms, pemetaan awan titik 21,4 ms, pengelompokan dan lokalisasi 8,1 ms (utas paralel); total 23,1 FPS. (5) Pada TUM RGB-D (Tabel 4), RMSE ATE dalam meter untuk sistem ini: 0,0052 (sitting-static), 0,031 (walking-halfsphere), 0,082 (walking-rpy), 0,037 (walking-static), 0,015 (walking-xyz), lebih rendah daripada ORB-SLAM3, DynaSLAM, DS-SLAM, dan Panoptic-SLAM pada kelima urutan.

Pembandingan dengan sistem lain (Tabel 13) tidak dilakukan pada data yang sama. Penulis menyandingkan angka dari makalah masing-masing: ORB-Livox RMSE 26 mm, SLAM-PYE RMSE horizontal 46,3 mm dan vertikal 54,0 mm, serta metode DTC dengan akurasi hitungan 84,9% pada 43,1 sampai 50,4 FPS.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: segmentasi yang menjaga batas tandan memperbaiki segmentasi dan hitungan pada subset tertutup, pembuangan titik dinamis menurunkan galat trayektori pada urutan TUM dinamis, kecepatan 23,1 FPS pada laptop, dan dataset dibagikan melalui repositori publik.

Keterbatasan yang dinyatakan penulis: (1) akurasi bergantung pada kedalaman stereo binokular, yang lemah pada area bertekstur rendah atau pencahayaan buruk (cahaya latar menaikkan RMSE menjadi 25,22 mm); (2) penyaringan tiga tahap menghilangkan detail geometri halus seperti sulur dan tangkai buah, walau tidak memengaruhi hitungan berbasis volume; (3) hanya objek kaku yang ditangani, dan dedaunan yang bergoyang tertiup angin belum dimodelkan. Rencana ke depan mencakup fusi LiDAR atau IMU, filter adaptif terhadap kepadatan titik, dan pemodelan daun yang bergoyang.

Menurut pembacaan ringkasan ini: (a) validasi hitungan kecil (88 dan 146 tandan pada dua skenario, serta sekitar 90 tandan pada tiap kondisi cahaya) dan asal "nilai sebenarnya" tidak dijelaskan; (b) beberapa galat relatif pada tabel tidak sesuai dengan hitungan di sebelahnya: 84 terhadap 88 menghasilkan sekitar 4,5% (tertulis 5,7%), 82 terhadap 89 menghasilkan sekitar 7,9% (tertulis 5,6%), dan 43 terhadap 48 menghasilkan sekitar 10,4% (tertulis 9,71%); rata-rata 5,95% pada abstrak adalah rerata dua angka tertulis 5,7% dan 6,2%; (c) klaim bahwa penjangkaran dunia SLAM mengurangi hitungan berulang tidak diuji dengan kasus kunjungan ulang atau perbandingan terhadap pelacak 2D; (d) pembanding pada Tabel 13 berbeda objek, sensor, dan data; (e) hitungan tidak dilaporkan per kelas dan hanya menghitung tandan yang terlihat; (f) satu kebun, satu spesies, dan varietas tidak dirinci.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari banyak pandang dan banyak bingkai, dengan mekanisme pencacahan di ruang 3D bersama. Titik buah dari keyframe diakumulasi pada peta global ORB-SLAM3, dikelompokkan dengan DBSCAN, lalu satu gugus yang lolos batas volume dihitung satu tandan. Identitas dengan demikian ditentukan oleh posisi pada peta global, bukan oleh pelacak ID 2D. Makalah tidak memuat evaluasi khusus untuk tandan yang terlihat berulang kali atau dikunjungi ulang, dan tidak membandingkan terhadap pelacak 2D pada data sendiri; keunggulan atas DTC hanya dikemukakan dalam pembahasan.

Hitungan tidak dilaporkan per kelas; hanya ada satu kelas buah. Acuan hitungnya adalah "nilai sebenarnya" per skenario yang asalnya (penghitungan lapangan atau anotasi citra) tidak dijelaskan dalam teks; acuan posisi berasal dari anotasi manual awan titik LiDAR. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: pola kelompok titik 3D dan pembatasan volume elipsoid untuk menghitung satu objek, serta masker semantik untuk membuang objek dinamis. Pola itu bergantung pada kualitas kedalaman stereo dan peta SLAM yang konsisten, sedangkan pengambilan citra sawit per sisi pohon tidak berupa lintasan kontinu. Hal ini merupakan kesimpulan ringkasan ini.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `yang2026real`.

Yang dkk. (2026) mengusulkan sistem pemetaan semantik 3D waktu nyata untuk kebun anggur dinamis yang menggabungkan ORB-SLAM3 dengan jaringan segmentasi EFSegNet (turunan PIDNet dengan GFFM dan DSA). Tandan anggur ditandai pada awan titik global, dikelompokkan dengan DBSCAN, dan dimodelkan sebagai elipsoid dengan PCA; satu elipsoid dihitung sebagai satu tandan. Pada kebun anggur hijau di Guangzhou, sistem mencapai RMSE lokalisasi 3D rata-rata 21,02 mm, galat hitungan rata-rata 5,95% (88 dan 146 tandan pada dua skenario), dan 23,1 FPS pada laptop dengan GPU RTX 3060.

Catatan verifikasi data: 23,1 FPS, 21,02 mm, dan 5,95% tercantum di abstrak dan kesimpulan. Hasil segmentasi ada pada Tabel 2 dan 3, lokalisasi pada Tabel 6, hitungan pada Tabel 7, sensitivitas DBSCAN pada Tabel 8, pencahayaan pada Tabel 9 dan 10, subset tertutup pada Tabel 11, waktu pada Tabel 12, dan pembanding pada Tabel 13. Jumlah 940 citra dan rasio 8:1:1 ada di Bagian 2.2 dan 3.1.1. Beberapa galat relatif pada Tabel 7, 10, dan 11 tidak sesuai dengan hitungan di sebelahnya (lihat bagian keterbatasan); perhitungan ulang dalam entri ini adalah selisih sederhana. Angka hitungan per urutan lokalisasi, asal "nilai sebenarnya", varietas anggur, dan parameter penyaringan tidak dilaporkan pada teks. Tabel 5 (trajektori TUM) berupa gambar dan tidak terbaca. Tabel 4 tidak mencantumkan satuan; entri ini menafsirkannya sebagai meter berdasarkan konvensi RMSE ATE.
