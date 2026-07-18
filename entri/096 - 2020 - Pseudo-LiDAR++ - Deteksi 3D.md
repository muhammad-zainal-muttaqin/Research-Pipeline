# 096 - Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `you2020pseudolidarpp` |
| Judul asli | Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving |
| Penulis | Yurong You, Yan Wang, Wei-Lun Chao, Divyansh Garg, Geoff Pleiss, Bharath Hariharan, Mark Campbell, Kilian Q. Weinberger |
| Tahun | 2020 |
| Venue | International Conference on Learning Representations (ICLR 2020) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1906.06310
- **OpenReview (versi ICLR yang diterima):** https://openreview.net/pdf?id=BJedHRVtPB
- **Kode sumber resmi:** https://github.com/mileyan/Pseudo_Lidar_V2
- **Google Scholar:** https://scholar.google.com/scholar?q=Pseudo-LiDAR%2B%2B%3A%20Accurate%20Depth%20for%203D%20Object%20Detection%20in%20Autonomous%20Driving
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Pseudo-LiDAR%2B%2B%3A%20Accurate%20Depth%20for%203D%20Object%20Detection%20in%20Autonomous%20Driving&sort=relevance

## Gambaran Umum

Makalah ini memperbaiki kelemahan utama *Pseudo-LiDAR* (bab 095): depth (kedalaman) yang diestimasi dari sepasang kamera stereo cukup akurat untuk objek dekat, tetapi galatnya membesar secara kuadratik terhadap jarak, sehingga objek jauh — justru yang paling kritis untuk keselamatan berkendara — sering luput terdeteksi. Pseudo-LiDAR++ mengajukan dua perbaikan yang saling melengkapi: (1) jaringan estimasi depth stereo baru yang dilatih langsung memakai galat kedalaman, bukan galat disparitas, sehingga tidak lagi memberi bobot berlebih pada objek dekat; dan (2) algoritme koreksi berbasis graf (*Graph-based Depth Correction*, GDC) yang memanfaatkan segelintir titik dari sensor LiDAR murah beresolusi rendah (disimulasikan 4-*beam*) untuk membetulkan bias sistematis pada seluruh peta depth.

Pada tolok ukur KITTI, kombinasi kedua perbaikan ini mempersempit selisih akurasi deteksi 3D antara sistem berbasis kamera stereo dan sistem berbasis LiDAR 64-*beam* yang jauh lebih mahal, dengan perbaikan paling menonjol pada objek jauh (30–70 meter). Kontribusi ini penting karena menunjukkan bahwa sebagian besar kesenjangan akurasi kamera-versus-LiDAR dapat ditutup tanpa membeli sensor LiDAR presisi tinggi, melainkan dengan sensor jarang yang harganya jauh lebih murah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Bab 095 (Pseudo-LiDAR) menunjukkan bahwa penyebab utama rendahnya akurasi deteksi 3D berbasis kamera bukan semata kualitas estimasi depth, melainkan representasinya: peta depth (front-view, satu nilai kedalaman per piksel) tidak cocok untuk konvolusi 3D, sedangkan mengubahnya menjadi *point cloud* (kumpulan titik koordinat 3D, representasi asli data LiDAR) memungkinkan detektor 3D berbasis LiDAR dipakai langsung pada data kamera. Perbaikan itu melompatkan akurasi, tetapi tidak menghilangkan satu sumber galat penting: jaringan stereo yang dipakai (mis. PSMNet) dilatih untuk meminimalkan galat *disparitas* (selisih posisi piksel yang sama antara citra kiri dan kanan kamera stereo), bukan galat kedalaman itu sendiri.

Hubungan disparitas dan depth bersifat berbanding terbalik, sehingga galat disparitas yang sama menghasilkan galat depth yang jauh berbeda tergantung jaraknya. Sebagai ilustrasi yang dipakai penulis, kesalahan satu piksel pada disparitas menghasilkan galat depth sekitar 0,1 meter pada jarak 5 meter, tetapi sekitar 5,8 meter pada jarak 50 meter. Karena fungsi *loss* berbasis disparitas memperlakukan tiap piksel setara, jaringan secara implisit dioptimalkan untuk objek dekat, dan performanya pada objek jauh — yang paling relevan bagi keselamatan berkendara karena membutuhkan waktu reaksi lebih panjang — tetap buruk. LiDAR presisi tinggi (mis. 64-*beam*) tidak memiliki masalah ini, tetapi harganya dapat mencapai puluhan ribu dolar per unit, sehingga tidak ekonomis untuk penerapan luas.

## Ide Utama

Gagasan pertama adalah mengganti sasaran optimisasi jaringan stereo: alih-alih meminimalkan selisih disparitas prediksi terhadap disparitas kebenaran, jaringan dilatih meminimalkan selisih kedalaman (depth) prediksi terhadap kedalaman kebenaran secara langsung. Perubahan sasaran ini menuntut perubahan pada arsitektur, karena volume biaya (*cost volume*, struktur internal yang menyimpan tingkat kecocokan piksel kiri-kanan pada tiap kandidat pergeseran) pada jaringan stereo konvensional disusun pada kisi disparitas, bukan kisi depth.

Gagasan kedua adalah memakai LiDAR yang sangat murah dan jarang (disimulasikan setara 4-*beam*, jauh di bawah 64-*beam*) bukan untuk menggantikan kamera, melainkan untuk mengoreksi bias sistematis pada *point cloud* pseudo-LiDAR yang dihasilkan dari depth stereo. Karena titik LiDAR jarang ini sedikit tetapi akurat, nilainya dipakai sebagai titik acuan (*landmark*) yang menjalar ke seluruh titik *point cloud* di sekitarnya melalui hubungan geometris lokal, bukan sekadar interpolasi sederhana.

## Cara Kerja Langkah demi Langkah

### Stereo Depth Network (SDN): melatih pada kisi depth

Jaringan SDN menerima citra stereo (pasangan kiri-kanan dari kamera yang sudah dikalibrasi) dan membangun *cost volume* langsung pada kisi kedalaman, bukan kisi disparitas seperti jaringan stereo konvensional (mis. PSMNet). Transformasi dari volume disparitas ke volume depth dilakukan dengan interpolasi bilinear. Rentang kedalaman yang dipakai adalah 1–80 meter dengan langkah kisi 1 meter, sehingga jaringan secara eksplisit dioptimalkan untuk membedakan objek pada rentang jarak yang relevan bagi berkendara di jalan raya. Fungsi *loss* menghitung selisih antara peta depth prediksi Z(u,v) dan peta depth kebenaran Z*(u,v) pada tiap piksel (u,v), sehingga galat pada objek jauh diberi bobot yang sepadan dengan galat pada objek dekat — berbeda dari jaringan berbasis disparitas yang bobot efektifnya timpang terhadap jarak.

### Dari depth ke point cloud: back-projection

Peta depth yang dihasilkan SDN diubah menjadi *point cloud* melalui *back-projection*: setiap piksel (u,v) dengan nilai depth Z dipetakan ke koordinat 3D (x,y,z) memakai parameter kalibrasi kamera. Proses ini identik dengan langkah inti Pseudo-LiDAR pada bab 095; perbedaannya di sini adalah kualitas peta depth masukan yang sudah dioptimalkan untuk jarak jauh.

### Graph-based Depth Correction (GDC)

GDC memakai data dari sensor LiDAR sangat jarang (disimulasikan setara 4-*beam*, sensor kelas ini dilaporkan berbiaya sekitar 600 dolar AS, jauh di bawah LiDAR 64-*beam* yang dapat mencapai sekitar 75.000 dolar AS — angka biaya ini perlu diverifikasi ke naskah asli). Titik-titik jarang tersebut diproyeksikan ke bidang citra untuk menandai sebagian kecil piksel sebagai titik acuan berdepth pasti. Selanjutnya dibangun graf ketetanggaan-terdekat (*k-nearest neighbor graph*, k = 10) di antara titik-titik *point cloud* pseudo-LiDAR memakai struktur pencarian KD-tree. Bobot tiap tepi graf dipelajari dengan menyelesaikan persoalan optimisasi yang meminimalkan selisih antara depth suatu titik dan kombinasi linear depth tetangganya (mirip prinsip pada *Locally Linear Embedding*: geometri lokal dipertahankan). Dengan bobot graf ini, koreksi dari titik-titik acuan LiDAR jarang didifusikan ke seluruh *point cloud*: depth akhir tiap titik diselesaikan sedemikian rupa sehingga tetap konsisten dengan hubungan tetangga lokal, sekaligus mendekati nilai pasti pada titik-titik acuan.

Alur keseluruhan, dari citra stereo sampai kotak 3D, dapat diringkas sebagai berikut.

```
citra stereo (kiri, kanan)
         │
         ▼
   SDN: cost volume pada kisi depth 1-80 m
         │  peta depth Z(u,v)
         ▼
   back-projection ke koordinat 3D
         │  point cloud pseudo-LiDAR
         ▼
 ┌────────────────────────────────────┐
 │ GDC (opsional, perlu LiDAR jarang)  │
 │  4-beam -> titik acuan (landmark)   │
 │  graf KNN (k=10) antar-titik        │
 │  difusi koreksi ke seluruh titik    │
 └────────────────────────────────────┘
         │  point cloud terkoreksi
         ▼
   detektor 3D (AVOD / PIXOR / P-RCNN)
         │
         ▼
   kotak 3D: (x, y, z, l, w, h, yaw)
```

Point cloud yang dihasilkan — baik sebelum maupun sesudah koreksi GDC — diteruskan ke detektor 3D yang semula dirancang untuk data LiDAR asli: AVOD (bab 092, fusi multi-tampilan), PIXOR (representasi tampak-atas), dan P-RCNN/PointRCNN (bab 089, berbasis *point cloud* langsung). Detektor-detektor ini tidak dimodifikasi arsitekturnya; hanya masukannya yang diganti dari LiDAR asli menjadi pseudo-LiDAR (dengan atau tanpa koreksi GDC).

## Eksperimen dan Hasil

Evaluasi dilakukan pada tolok ukur KITTI untuk deteksi objek mobil dalam 3D, dengan metrik *Average Precision* (AP) pada IoU (*Intersection over Union*, rasio tumpang tindih kotak prediksi dan kotak kebenaran) 0,7 — ambang yang cukup ketat untuk deteksi kendaraan. Perbandingan dipecah menurut jarak objek untuk menunjukkan letak perbaikan.

| Metode | 0–30 m | 30–50 m | 50–70 m |
|---|---|---|---|
| PSMNet (stereo baseline lama) | 65,6 | 15,8 | 0,0 |
| SDN (tanpa GDC) | 68,6 | 27,4 | 0,7 |
| SDN + GDC | 84,7 | 49,9 | 2,5 |
| LiDAR 64-*beam* (acuan atas) | 88,5 | 69,9 | 8,9 |

Angka-angka ini (bersumber dari pembacaan naskah via alat pengambilan otomatis, belum dicocokkan manual terhadap tabel asli — lihat *Poin untuk Sitasi*) memperlihatkan pola yang konsisten dengan motivasi makalah: pada objek dekat (0–30 m), SDN saja sudah menaikkan AP dari 65,6 menjadi 68,6, tetapi lompatan besar terjadi setelah GDC ditambahkan (84,7). Pada objek jauh (30–50 m), GDC menggandakan AP SDN dari 27,4 menjadi 49,9. Pada jarak terjauh (50–70 m), semua metode berbasis kamera masih jauh di bawah LiDAR 64-*beam*, tetapi SDN+GDC (2,5) tetap menunjukkan perbaikan dibandingkan SDN saja (0,7) dan PSMNet (0,0, gagal total mendeteksi objek pada jarak ini).

Pada kategori keseluruhan (Easy/Moderate/Hard, kombinasi kondisi oklusi dan ukuran objek pada protokol KITTI), penambahan GDC dengan LiDAR 4-*beam* menaikkan AP kategori Moderate dan Hard secara nyata, mendekati — meski belum menyamai — AP LiDAR 64-*beam* penuh. Dari sisi biaya sensor, hasil ini berarti sebagian besar akurasi LiDAR presisi tinggi dapat diperoleh dengan tambahan sensor LiDAR jarang yang jauh lebih murah, ditambah pemrosesan GDC yang menurut makalah berjalan sekitar 90 milidetik per *frame* pada satu GPU — cukup ringan dibandingkan waktu inferensi jaringan stereo itu sendiri.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah pemisahan yang jelas antara dua sumber galat pseudo-LiDAR — kesalahan sistematis akibat fungsi *loss* yang tidak selaras dengan tugas, dan bias yang dapat dikoreksi dengan sedikit informasi eksternal — sehingga masing-masing dapat diperbaiki dengan solusi yang tepat sasaran: perubahan *loss* untuk SDN, dan koreksi berbasis graf untuk GDC. Pendekatan ini juga bersifat modular: SDN dapat dipakai sendiri untuk memperbaiki depth, sedangkan GDC dapat ditambahkan hanya bila kendaraan dilengkapi LiDAR jarang, tanpa mengubah detektor 3D hilir.

Dari sisi rekayasa, keterbatasannya juga jelas. Pertama, GDC tetap bergantung pada keberadaan sensor LiDAR fisik, meski jarang dan murah — sistem tidak sepenuhnya lepas dari LiDAR, hanya mengurangi kebutuhan resolusinya. Kedua, kesenjangan dengan LiDAR 64-*beam* pada objek sangat jauh (50–70 m) belum tertutup: AP 2,5 berbanding 8,9 menunjukkan bahwa untuk skenario deteksi dini pada kecepatan tinggi, keunggulan LiDAR presisi tinggi masih relevan. Ketiga, seluruh metode bergantung pada kalibrasi stereo yang akurat; kesalahan kalibrasi kamera akan merambat langsung ke galat depth dan, pada akhirnya, ke posisi kotak 3D.

## Kaitan dengan Bab Lain

Bab ini adalah kelanjutan langsung dari bab 095 (Pseudo-LiDAR): representasi *point cloud* dari depth kamera yang diusulkan di bab tersebut dipakai apa adanya di sini, sementara kontribusi baru difokuskan pada kualitas depth itu sendiri dan koreksi bias jaraknya. Detektor 3D yang dipakai sebagai penerima *point cloud* pseudo-LiDAR — AVOD dan P-RCNN — dibahas tersendiri pada [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md) dan [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md); Pseudo-LiDAR++ menunjukkan bahwa detektor-detektor tersebut, yang semula dirancang untuk data LiDAR asli, dapat menerima masukan kamera terkoreksi dengan penurunan akurasi yang lebih kecil. Gagasan menggabungkan sinyal kamera dengan sedikit data LiDAR juga senada dengan strategi fusi pada [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md), meski mekanismenya berbeda: PointPainting mengecat titik LiDAR dengan fitur semantik dari kamera, sedangkan Pseudo-LiDAR++ mengoreksi kedalaman kamera dengan sedikit titik LiDAR.

## Poin untuk Sitasi

Kutip dengan kunci `you2020pseudolidarpp`. Ringkasan yang aman dikutip: "Pseudo-LiDAR++ memperbaiki Pseudo-LiDAR melalui jaringan stereo yang dilatih langsung pada galat kedalaman (bukan disparitas) dan koreksi berbasis graf memakai LiDAR jarang 4-*beam*, mempersempit kesenjangan akurasi deteksi 3D kamera terhadap LiDAR 64-*beam* pada tolok ukur KITTI, dengan perbaikan terbesar pada objek jauh." Tabel angka AP per rentang jarak (65,6/15,8/0,0 untuk PSMNet; 68,6/27,4/0,7 untuk SDN; 84,7/49,9/2,5 untuk SDN+GDC; 88,5/69,9/8,9 untuk LiDAR 64-*beam*), klaim perbaikan 40% pada objek jauh, angka biaya sensor (≈600 dolar AS untuk 4-*beam*, ≈75.000 dolar AS untuk 64-*beam*), dan waktu proses GDC (≈90 milidetik per *frame*) diperoleh melalui alat pengambilan naskah otomatis dan belum diverifikasi baris per baris terhadap tabel PDF asli — wajib dicocokkan ke `arxiv.org/abs/1906.06310` atau versi OpenReview sebelum dikutip dalam karya formal.
