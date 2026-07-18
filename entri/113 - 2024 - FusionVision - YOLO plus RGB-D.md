# 113 - FusionVision: A Comprehensive Approach of 3D Object Reconstruction and Segmentation from RGB-D Cameras Using YOLO and Fast Segment Anything

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `elamraoui2024fusionvision` |
| Judul asli | FusionVision: A Comprehensive Approach of 3D Object Reconstruction and Segmentation from RGB-D Cameras Using YOLO and Fast Segment Anything |
| Penulis | Safouane El Ghazouali, Youssef Mhirit, Ali Oukhrid, Umberto Michelucci, Hichem Nouira |
| Tahun | 2024 |
| Venue | *Sensors* (MDPI), vol. 24, no. 9, artikel 2889; pracetak arXiv:2403.00175 |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2403.00175
- **Google Scholar:** https://scholar.google.com/scholar?q=FusionVision%3A%20A%20Comprehensive%20Approach%20of%203D%20Object%20Reconstruction%20and%20Segmentation%20from%20RGB-D%20Cameras%20Using%20YOLO%20and%20Fast%20Segment%20Anything
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=FusionVision%3A%20A%20Comprehensive%20Approach%20of%203D%20Object%20Reconstruction%20and%20Segmentation%20from%20RGB-D%20Cameras%20Using%20YOLO%20and%20Fast%20Segment%20Anything&sort=relevance

## Gambaran Umum

FusionVision mengusulkan *pipeline* (alur pemrosesan bertahap) yang memadukan detektor YOLOv8 dengan FastSAM — versi cepat dari *Segment Anything Model* (SAM), model segmentasi umum yang mampu mensegmentasi objek apa pun berdasarkan isyarat masukan (*prompt*) tanpa pelatihan khusus per kelas — untuk mengubah aliran citra dari kamera RGB-D menjadi rekonstruksi dan segmentasi objek dalam ruang tiga dimensi. Kotak deteksi dari YOLOv8 dipakai sebagai *prompt* kotak bagi FastSAM sehingga segmentasi hanya memproses wilayah yang relevan, bukan seluruh bidang citra. Masker piksel hasil segmentasi kemudian diselaraskan dengan peta kedalaman memakai parameter kalibrasi kamera, menghasilkan awan titik (*point cloud* — kumpulan titik koordinat 3D) khusus per objek yang selanjutnya disaring dari titik-titik derau sebelum menjadi kotak pembatas 3D.

Pada himpunan data khusus beranggotakan tiga kelas objek (cup/gelas, computer/komputer, bottle/botol) yang direkam dengan kamera Intel RealSense D435i, YOLOv8n hasil pelatihan mencapai mAP50 97,92% dan presisi 97,08%. Tahap deteksi dan segmentasi berjalan sekitar 27–34 *frame* per detik (FPS), sedangkan *pipeline* penuh yang menyertakan rekonstruksi dan visualisasi 3D melambat menjadi sekitar 5 FPS. Kode sumber dan model terlatih dipublikasikan terbuka di GitHub oleh penulis. Makalah ini menjadi salah satu contoh terbaru pada klaster YOLO plus RGB-D karena menggabungkan tiga komponen berbeda — deteksi 2D, segmentasi generik, dan geometri kamera — dalam satu sistem yang bertujuan tetap berjalan mendekati waktu nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Kamera RGB-D — seperti Intel RealSense atau Microsoft Kinect — merekam warna dan kedalaman setiap piksel sekaligus, sehingga posisi tiga dimensi tiap titik citra dapat dihitung bila parameter kalibrasi kameranya diketahui. Untuk mengolah rekaman ini menjadi objek 3D, dua strategi umum sudah ada sebelumnya. Strategi pertama memasukkan kanal *depth* (kedalaman) sebagai kanal tambahan pada masukan jaringan deteksi sejak lapis pertama — pendekatan *early fusion* (fusi dini) yang dipakai pada bab 112 (Expandable YOLO). Strategi kedua memakai model segmentasi umum seperti SAM, yang dapat mensegmentasi objek apa pun dari sebuah titik, kotak, atau teks tanpa pelatihan ulang, tetapi mahal secara komputasi karena mekanisme atensinya dievaluasi pada seluruh citra untuk setiap permintaan segmentasi.

Kedua kelemahan ini saling berlawanan: SAM penuh presisi tetapi terlalu lambat untuk robotika atau navigasi, sedangkan deteksi kotak saja cepat tetapi tidak presisi — latar di dalam kotak ikut terhitung sebagai objek saat diproyeksikan ke 3D, sehingga rekonstruksinya kotor oleh titik yang bukan permukaan objek. Masalah yang ingin dipecahkan FusionVision adalah menggabungkan kecepatan detektor dengan presisi batas segmentasi, lalu memproyeksikan hasilnya ke ruang 3D memakai kanal kedalaman, tanpa mengorbankan kecepatan hingga tidak layak dipakai pada aliran video langsung.

## Ide Utama

Gagasan inti FusionVision adalah menyusun dua model murah secara berjenjang, bukan menjalankan satu model mahal pada seluruh citra. Detektor cepat (YOLOv8) dijalankan lebih dahulu untuk mempersempit wilayah pencarian menjadi kotak-kotak kandidat per objek. Kotak-kotak ini dipakai sebagai *prompt* bagi FastSAM — arsitektur segmentasi instansi satu tahap yang membangkitkan mask dari prototipe konvolusi, mirip YOLACT — sehingga FastSAM hanya menghaluskan batas objek pada wilayah yang sudah ditunjuk, bukan mencari objek dari nol pada seluruh citra. Karena beban komputasi FastSAM sebanding dengan jumlah dan ukuran kotak yang diberikan, bukan dengan ukuran penuh citra, total waktu pemrosesan tetap terkendali.

Masker piksel hasil segmentasi lalu dipetakan ke koordinat 3D memakai kalibrasi kamera dan peta kedalaman; hanya piksel di dalam masker yang diikutkan, sehingga awan titik yang terbentuk sudah bersih dari latar sejak awal, kemudian disaring lagi dengan teknik pemrosesan titik klasik sebelum menjadi kotak pembatas 3D akhir. Rangkaian tahap inilah yang membedakan FusionVision dari pendekatan fusi dini: kedalaman dipakai belakangan, hanya untuk proyeksi geometris, setelah deteksi dan segmentasi RGB selesai.

## Cara Kerja Langkah demi Langkah

Diagram berikut merangkum alur data dari citra RGB dan peta kedalaman hingga kotak pembatas 3D:

```
citra RGB 640x480              peta kedalaman 640x480
        |                                |
        v                                |
   YOLOv8n (deteksi objek)               |
        | kotak (x,y,w,h) per objek      |
        v                                |
   FastSAM (prompt = kotak)              |
        | mask biner per objek           |
        +----------------+---------------+
                          v
         penyelarasan RGB-D (Kc, Kd, Tcd)
                          v
                awan titik per objek
                          |
        downsampling voxel (ukuran 5)
                          |
   penghilangan outlier statistik
   (300 tetangga, rasio 2,0)
                          v
        kotak pembatas 3D + rekonstruksi bersih
```

### Akuisisi Data dan Pelatihan YOLOv8

Penulis merekam 100 citra khusus dengan kamera Intel RealSense D435i untuk tiga kelas objek — cup (gelas), computer (komputer/laptop), dan bottle (botol) — dalam berbagai posisi dan kondisi pencahayaan, lalu memberi anotasi kotak pembatas secara manual. Data ini diperbanyak dengan augmentasi flip horizontal dan vertikal serta rotasi sudut, kemudian dibagi 80% untuk pelatihan dan 20% untuk validasi. Model yang dilatih adalah YOLOv8n, varian teringan dari keluarga YOLOv8, selama 300 *epoch* dengan optimizer Adam dan laju belajar 0,01, memakai empat komponen *loss*: *objectness loss* (entropi silang biner untuk keberadaan objek), *classification loss* (entropi silang lintas kelas), *bounding box loss* (galat kuadrat rata-rata koordinat kotak), dan *center coordinate loss* (*focal loss* pada prediksi titik pusat). Kurva pelatihan mulai stabil sekitar *epoch* ke-170, dengan hasil akhir presisi 97,08%, *recall* 96,94% (proporsi objek sebenarnya yang berhasil terdeteksi), mAP50 97,92%, dan mAP50-95 87,9% (mAP dirata-ratakan pada ambang IOU 0,50 sampai 0,95).

### Segmentasi Batas Objek dengan FastSAM

FastSAM menerima kotak keluaran YOLOv8 sebagai *prompt* dan menghasilkan masker piksel untuk objek di dalam kotak tersebut, yang kemudian diubah menjadi masker biner (setiap piksel bernilai objek atau bukan objek). Karena FastSAM hanya memproses wilayah yang sudah ditunjuk oleh kotak deteksi, tahap ini menambah beban komputasi yang relatif kecil dibandingkan menjalankan segmentasi umum pada seluruh citra — terlihat pada kecepatan pemrosesan yang hampir tidak berubah antara tahap deteksi saja dan deteksi ditambah segmentasi (rinciannya di bagian eksperimen).

### Penyelarasan RGB-Depth dan Proyeksi ke Awan Titik

Piksel pada peta kedalaman dan piksel pada citra RGB berasal dari dua sensor fisik berbeda pada badan kamera, sehingga posisinya perlu diselaraskan sebelum digabung. Makalah merumuskan transformasi ini sebagai Z₀[u₀ v₀ 1]ᵀ = Kc · Tcd · Kd⁻¹ · [Z u v 1]ᵀ: Kc dan Kd adalah matriks intrinsik (parameter internal lensa dan sensor) kamera RGB dan kamera kedalaman, sedangkan Tcd adalah matriks transformasi rigid (rotasi dan translasi) yang menyatakan selisih posisi fisik kedua sensor. Melalui persamaan ini, setiap piksel kedalaman (u, v, Z) dipetakan ke koordinat piksel RGB (u₀, v₀, Z₀); hanya piksel yang jatuh di dalam masker biner FastSAM yang diikutsertakan, sehingga keluarannya adalah awan titik yang sudah terbatas pada permukaan objek, bukan seluruh adegan.

### Pembersihan Awan Titik dan Rekonstruksi 3D

Awan titik per objek melewati dua tahap pembersihan klasik. Pertama, *downsampling* berbasis *voxel* (kubus ruang diskret) dengan ukuran sisi 5 satuan memadatkan titik-titik yang berdekatan menjadi satu titik representatif, mengurangi jumlah titik tanpa mengubah bentuk objek secara berarti. Kedua, penghilangan pencilan statistik (*statistical outlier removal*) memeriksa 300 tetangga terdekat tiap titik dan membuang titik yang jaraknya melampaui rasio deviasi standar 2,0 dari rata-rata tetangganya — menyaring titik derau yang muncul akibat kesalahan pembacaan kedalaman di tepi objek atau pada permukaan yang memantulkan cahaya. Awan titik bersih inilah yang dipakai menghitung kotak pembatas 3D dan bentuk rekonstruksi akhir per objek.

## Eksperimen dan Hasil

Seluruh pengujian dijalankan pada perangkat keras yang sama: GPU NVIDIA RTX 2080 Ti, sistem operasi Ubuntu 22.04 LTS, dan kamera Intel RealSense D435i dengan resolusi 640×480 untuk citra RGB maupun peta kedalaman. Tabel berikut merangkum kecepatan pemrosesan pada tiap tahap tambahan yang disusupkan ke *pipeline*:

| Tahap | Perkiraan laju (FPS) |
|---|---|
| RGB + kedalaman mentah | ~90 |
| + deteksi YOLOv8 | ~34 |
| + segmentasi FastSAM | ~33,7 |
| + rekonstruksi & visualisasi 3D | ~5 |

Interpretasinya: menambahkan deteksi YOLOv8 menurunkan laju dari ~90 menjadi ~34 FPS, sedangkan menambahkan segmentasi FastSAM di atasnya hampir tidak menurunkan laju lebih jauh (~33,7 FPS) karena FastSAM hanya bekerja pada wilayah kotak yang sudah dipersempit — bukti strategi berjenjang menekan biaya segmentasi. Biaya terbesar justru muncul pada rekonstruksi dan visualisasi 3D, yang menjatuhkan laju hingga ~5 FPS: inti deteksi-dan-segmentasi 2D tetap mendekati waktu nyata, sementara keluaran 3D tervisualisasi penuh jauh dari itu. Makalah juga melaporkan penyaringan awan titik menghilangkan sebagian besar titik yang tidak relevan dari bidang pandang penuh — angka persentase persisnya berbeda antar bagian naskah sehingga perlu dicek ulang sebelum dikutip (lihat *Poin untuk Sitasi*).

Kualitas segmentasi FastSAM diukur dengan sejumlah metrik: indeks Jaccard (IOU antar masker) 0,94, koefisien Dice (ukuran tumpang tindih dua himpunan piksel, mirip F1 pada level piksel) 0,92, presisi 0,93, *recall* 0,94, skor F1 0,92, dan akurasi piksel 0,96. Angka-angka ini menunjukkan masker FastSAM secara konsisten menutupi bentuk objek dengan baik setelah diberi *prompt* kotak dari YOLOv8.

Pengujian generalisasi pada kondisi lingkungan yang belum pernah dilihat saat pelatihan menunjukkan penurunan performa yang tidak merata antar kelas. Kelas botol paling terdampak: presisi turun hingga 0,31 dan IOU turun hingga 0,52 pada subset uji paling menantang, jauh di bawah kelas cup dan computer pada subset yang sama. Penulis mengaitkan penurunan ini dengan permukaan botol yang transparan atau memantulkan cahaya, yang membuat sensor kedalaman salah membaca jarak permukaan — kesalahan yang lalu ikut memengaruhi kualitas proyeksi 3D, bukan hanya deteksi 2D.

## Kelebihan dan Keterbatasan

Kelebihan utama FusionVision terletak pada strategi berjenjangnya: menjalankan detektor murah lebih dahulu untuk mempersempit wilayah kerja model segmentasi menekan biaya komputasi dibandingkan menjalankan SAM penuh, terbukti dari laju pemrosesan yang nyaris tidak turun antara tahap deteksi saja dan deteksi-ditambah-segmentasi. Rancangannya modular — YOLOv8, FastSAM, dan tahap geometri 3D dapat diganti model lain tanpa mengubah keseluruhan alur — dan keluarannya lebih lengkap daripada sekadar kotak 2D, yakni rekonstruksi 3D yang sudah dibersihkan dari derau. Ketersediaan kode dan model terlatih secara terbuka mendukung reproduksi hasil oleh pihak lain.

Keterbatasan yang diakui penulis mencakup penurunan tajam performa pada kondisi lingkungan baru, khususnya untuk objek transparan atau reflektif seperti botol, serta kesalahan estimasi masker FastSAM pada sudut pandang sensor tertentu. Dari sisi rekayasa, himpunan data pelatihan sangat kecil — 100 citra untuk tiga kelas objek sederhana — sehingga metrik pelatihan yang sangat tinggi (mAP50 97,92%) mencerminkan kondisi terkontrol, bukan bukti generalisasi luas, sejalan dengan anjloknya presisi kelas botol pada uji kondisi baru. Secara konseptual, seluruh *pipeline* bergantung pada kualitas sensor kedalaman: pada permukaan transparan, mengilap, atau di luar jangkauan sensor stereo/*time-of-flight*, baik deteksi 2D maupun proyeksi 3D ikut terganggu. Laju ~5 FPS untuk keluaran 3D tervisualisasi juga masih jauh dari cukup untuk aplikasi robotik yang menuntut reaksi cepat, meski inti deteksi-segmentasi saja sudah mendekati waktu nyata.

## Kaitan dengan Bab Lain

FusionVision berada pada klaster YOLO plus RGB-D bersama sejumlah bab lain yang memakai kedalaman untuk tugas berbeda. Bab 112 (Expandable YOLO) memasukkan kanal *depth* sebagai masukan tambahan sejak lapis pertama jaringan (fusi dini), berlawanan dengan strategi FusionVision yang memakai kedalaman belakangan, hanya untuk proyeksi geometris setelah deteksi dan segmentasi RGB selesai — dua filosofi fusi yang dapat dibandingkan langsung karena menyasar masalah serupa dengan urutan pemrosesan berbeda. Bab 115 (YOLOv8-URE) juga menggabungkan deteksi berbasis YOLOv8 dengan awan titik untuk tugas *robotic grasping* (pengambilan objek oleh lengan robot) pada adegan bertumpuk, dan bab 116 (Grasp via YOLO + RGB-D Fusion) mengangkat tema serupa pada domain penggenggaman objek. Ketiganya berbagi kebutuhan yang sama dengan FusionVision: mengubah deteksi 2D menjadi representasi 3D untuk aplikasi hilir, meski jalur teknis menuju ke sana berbeda-beda.

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)

## Poin untuk Sitasi

Kutip dengan kunci `elamraoui2024fusionvision`. Ringkasan yang aman dikutip: "FusionVision memadukan YOLOv8 dan FastSAM secara berjenjang untuk mensegmentasi objek pada citra RGB-D, lalu memproyeksikan masker hasilnya ke awan titik memakai kalibrasi kamera, mencapai mAP50 97,92% pada deteksi dan laju sekitar 5 FPS untuk keluaran rekonstruksi 3D penuh." Perlu diverifikasi ulang ke tabel asli pada jurnal *Sensors* sebelum dikutip formal: (1) angka persentase pengurangan jumlah titik awan setelah penyaringan — dua bagian sumber yang dirujuk untuk penulisan bab ini menyebut nilai dasar dan hasil akhir yang berbeda, sehingga hanya arah penurunannya (signifikan) yang dapat dipastikan, bukan angka persisnya; (2) rincian metrik IOU/presisi per subset uji generalisasi (Set 1/2/3) yang dikutip di sini berasal dari ekstraksi otomatis naskah, bukan pembacaan langsung tabel PDF/HTML asli.
