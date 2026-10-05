# Incremental 3D Crop Model Association for Real-Time Counting in Dense Orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `park2026incremental` |
| Judul asli | Incremental 3D Crop Model Association for Real-Time Counting in Dense Orchards |
| Penulis | Park, Daesung; Ko, KwangEun; Pyo, Dongbum; Kang, Jaehyeon |
| Tahun | 2026 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [park2026incremental.pdf](../pdf/park2026incremental.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2026.3662648

## Gambaran Umum

Makalah ini mengusulkan kerangka kerja pencacahan tanaman waktu-nyata (*real-time*) untuk kebun yang ditanam rapat dan tidak beraturan. Setiap buah dimodelkan sebagai kotak pembatas 3D berorientasi (*3D oriented bounding box*, OBB) yang dibuat saat buah pertama kali terdeteksi, lalu diperbarui oleh pengamatan berikutnya. Pengamatan baru dicocokkan dengan model global memakai *Generalized Intersection over Union* (GIoU) 3D, dan model yang tidak meyakinkan disaring berdasarkan skor keyakinan segmentasi. Dengan cara ini, hitungan diperbarui selama pemindaian tanpa rekonstruksi 3D luring.

Data dikumpulkan dengan perangkat genggam berisi kamera RGB FLIR Blackfly, LiDAR Livox Avia, dan IMU di kebun tangerin (*Citrus unshiu* dan Kanpei) di Seogwipo, Jeju, Korea Selatan. Segmentasi instans memakai YOLOv11s-seg, sedangkan estimasi pose memakai FAST-LIVO. Tiga pola gerak diuji: *revisit*, *circular*, dan *straight*.

Hasil utama yang tertulis di teks adalah RMSE hitungan 8,9 dengan simpangan baku galat 6,4, terendah di antara pembanding (ByteTrack, DeepSORT, AgriSORT, CascadeSORT, dan analisis komponen terhubung/CCA pada peta 3D). Waktu proses rata-rata 35,30 ms per bingkai (sekitar 28,3 bingkai per detik).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pencacahan waktu-nyata diperlukan oleh sistem pertanian otonom, misalnya untuk koordinasi multi-robot, intervensi bertarget, dan pemanenan adaptif. Pada kebun alami, tanaman tidak tertata, dedaunan lebat, kerapatan tanam tinggi, dan jarak antartanaman dapat sekecil 0,2 m, sehingga oklusi dan pandangan parsial sering terjadi.

Pelacakan 2D berbasis deteksi (*tracking-by-detection*) murah secara komputasi, tetapi rentan terhitung ganda ketika pelacakan terputus akibat oklusi atau kegagalan deteksi. Pada lintasan pindai yang tidak terduga, tanaman sering dikunjungi ulang dan pelacak 2D memberikan ID baru sehingga buah yang sama terhitung lagi. Rekonstruksi 3D dengan SLAM atau *structure-from-motion* (SfM) mengurangi hitungan ganda, tetapi memerlukan pemrosesan satu per satu (*batch*) yang berat, menghasilkan rekonstruksi berlubang, bising, atau tidak selaras pada vegetasi, dan penutupan simpul (*loop closure*) SLAM tidak andal karena tampilan vegetasi yang berulang. Sensor RGB-D tidak efektif di bawah sinar matahari, sedangkan LiDAR pada ruang sempit memperbesar derau dari objek di dekatnya sehingga galat pemetaan menumpuk.

## Ide Utama

Gagasan utamanya adalah membangun instans buah 3D global secara bertahap selama pengumpulan data, bukan merekonstruksi seluruh adegan lebih dahulu. Model buah dibuat dari pindaian lokal per bingkai yang telah disaring, sehingga derau LiDAR tidak menumpuk lintas sudut pandang seperti pada peta global. Model lokal ditransformasikan ke kerangka global dengan pose odometri, lalu dicocokkan dengan model yang ada melalui GIoU 3D.

Identitas buah dijaga oleh dua mekanisme: kecocokan spasial (GIoU di atas ambang) dan penyaringan keyakinan atas model hasil fusi. Pendekatan ini hanya memerlukan anotasi 2D, karena penulis menyatakan anotasi kotak 3D sulit diperoleh di kebun rapat dan derau LiDAR membuatnya tidak andal.

## Cara Kerja Langkah demi Langkah

```
 kamera + LiDAR + IMU --> FAST-LIVO (pose) --> citra dan titik bergaransi pose
        citra --> YOLOv11s-seg (masker + skor) --> titik LiDAR dalam masker
        --> saring derau --> OBB (PCA) --> asosiasi GIoU 3D ke peta global
        --> saring keyakinan --> hitungan = jumlah model di peta
```

### 1. Akuisisi data

Perangkat genggam memuat kamera FLIR Blackfly (FL3-U3-1324C-C) berlensa Edmund Optics 86900 dengan panjang fokus 4,5 mm (resolusi 1280x1024, bidang pandang horizontal 84,7 derajat) dan LiDAR Livox Avia dengan IMU BMI088. Ekstrinsik kamera-LiDAR dikalibrasi dengan metode berbasis tepi. Pengambilan data dilakukan di kebun tangerin di Seogwipo, Jeju, pada pohon dewasa berdaun lebat. Buah berada pada keadaan pra-panen berwarna jingga, berdiameter 5 sampai 10 cm, dengan jarak sensor ke buah 0,2 sampai 3,0 m. Tiga pola gerak dikumpulkan: *revisit* (sensor kembali ke daerah yang pernah dilalui), *circular* (mengitari pohon di ruang sempit), dan *straight* (bergerak lurus ke arah pohon). Acuan berupa hitungan per bingkai yang dianotasi manual; rincian dataset ada pada Tabel I.

### 2. Estimasi pose

Pose sensor diestimasi dengan FAST-LIVO, yaitu odometri LiDAR-inersia-visual yang erat berpasangan dalam kerangka *iterated Kalman filter*, menghasilkan pasangan citra dan awan titik yang tersinkron dan berpose.

### 3. Pembuatan model buah 3D

YOLOv11s-seg menghasilkan masker instans beserta skor keyakinan pada tiap bingkai. Awan titik LiDAR yang telah dikalibrasi diproyeksikan ke bidang citra, dan titik yang jatuh di dalam masker diambil. Titik yang jarak ke tetangga terdekatnya melebihi 0,1 m dibuang, dan hanya klaster dengan sedikitnya lima titik tersisa yang dipakai. Pusat model adalah centroid titik tersaring, orientasi OBB ditentukan dengan *Principal Component Analysis* (PCA) lewat *Point Cloud Library*, dan dimensi ditentukan dari rentang minimum dan maksimum titik pada sumbu utama. Setiap OBB menyimpan ID, posisi, orientasi, dimensi, dan skor keyakinan.

### 4. Asosiasi bertahap

Model baru ditransformasikan ke kerangka global. Kandidat dicari sebagai model global terdekat berdasarkan jarak centroid memakai pohon k-d. Bila GIoU 3D melebihi ambang, kedua model digabung: awan titik disatukan, OBB baru dipasang pada titik gabungan, dan skor keyakinan digabungkan. Bila tidak ada kecocokan, model baru dimasukkan ke peta. GIoU dihitung dengan komputasi lambung cembung (*convex hull*) sehingga dapat menilai kotak berorientasi sembarang.

### 5. Penyaringan keyakinan

Sebuah model baru dipertimbangkan untuk dibuang setelah dilacak sedikitnya N = 9 bingkai, dan dibuang bila median skor keyakinan terakumulasi di bawah ambang. Hitungan adalah jumlah model dalam peta global. Ambang akhir ditetapkan pada sekuens validasi terpisah: $\tau_{conf} = 0{,}6$ dan $\tau_{GIoU} = 0{,}25$, konstan untuk semua sekuens uji.

### 6. Implementasi waktu-nyata

Dua utas berjalan paralel: estimasi keadaan pada CPU multi-inti dan pencacahan (deteksi, pembuatan model, asosiasi, penyaringan). Deteksi YOLOv11 dikonversi ke ONNX dan berjalan di GPU, sedangkan modul lain berjalan di CPU.

## Eksperimen dan Hasil

Detektor YOLOv11s-seg dilatih dari bobot awal COCO pada 1.449 citra kustom (70% latih, 10% validasi, 20% uji) dengan 13.587 masker buah yang dipisahkan dari sekuens pengujian; pelatihan 100 *epoch*, *batch* 32, hiperparameter bawaan. Detektor yang sama dipakai untuk semua metode agar perbandingan hanya menguji strategi asosiasi. Pembanding mencakup ByteTrack, DeepSORT, AgriSORT, CascadeSORT, dan CCA dari peta 3D yang dihasilkan FAST-LIVO (octree level 9, ukuran klaster minimum 5 titik). Dua ablasi diuji: GIoU diganti jarak Euclidean antarcentroid (ambang 0,03 m) dan GIoU tanpa penyaringan keyakinan.

| Metode atau varian | RMSE | Simpangan baku galat |
|---|---|---|
| Metode usulan | 8,9 | 6,4 |
| Usulan tanpa penyaringan keyakinan | 14,5 | 7,5 |
| Pembanding lain (ByteTrack, DeepSORT, AgriSORT, CascadeSORT, CCA, ablasi jarak) | tidak terbaca (Tabel II) | tidak terbaca (Tabel II) |

Secara kualitatif, teks menyatakan ByteTrack dan DeepSORT memiliki galat jauh lebih tinggi, AgriSORT dan CascadeSORT lebih baik daripada pelacak umum tetapi belum memuaskan, CCA memiliki galat tertinggi di antara metode berbasis peta karena penyimpangan pose dan galat rekonstruksi, dan ablasi jarak cenderung menghitung berlebih.

Analisis per bingkai menunjukkan hitungan mengikuti tren acuan dengan penundaan, karena buah jauh tampak pada citra RGB (dan masuk acuan) tetapi titik LiDAR-nya belum cukup untuk membentuk model 3D. Pada sekuens *revisit*, hitungan acuan dan estimasi tetap naik setelah penelusuran awal karena buah yang tadinya tertutup atau di luar bidang pandang terlihat pada jalur kembali. Analisis ambang (Gambar 8): menaikkan $\tau_{conf}$ menurunkan hitungan (kurang hitung pada 0,75), sedangkan menaikkan $\tau_{GIoU}$ menaikkan hitungan karena kurang terasosiasi.

| Modul | Hasil waktu |
|---|---|
| Total rata-rata per bingkai | 35,30 ms (sekitar 28,3 bingkai/detik) |
| Perangkat uji | CPU Intel i7-11800H 8 inti, RAM 16 GB, GPU NVIDIA GeForce RTX 3050Ti |

Rincian waktu per modul ada pada Tabel III yang tidak terbaca dari teks ekstraksi.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: pencacahan berjalan waktu-nyata tanpa rekonstruksi luring, derau LiDAR lebih terkendali karena model dibangun dari pindaian lokal, hanya anotasi 2D yang diperlukan, kinerja stabil pada kebun rapat tak beraturan dengan satu set ambang tetap, dan dataset dipublikasikan (Zenodo).

Keterbatasan yang dinyatakan penulis: deteksi berbasis RGB rentan terhadap hujan, malam hari, dan silau; tidak ada penutupan simpul global pada estimasi keadaan sehingga konsistensi jangka panjang pada skala besar dapat terpengaruh; model buah belum dipakai sebagai landmark odometri; dan oklusi akibat perbedaan sudut pandang kamera-LiDAR tidak dimodelkan secara eksplisit. Penulis juga mencatat penundaan hitungan akibat kepadatan titik LiDAR yang rendah pada jarak jauh.

Menurut pembacaan ringkasan ini, evaluasi dilakukan pada satu jenis tanaman (tangerin) dengan satu perangkat, dan jumlah sekuens serta jumlah buah acuan tidak dapat diverifikasi dari teks karena Tabel I tidak terbaca. Metode memerlukan LiDAR dan kalibrasi ekstrinsik, sehingga tidak dapat langsung dipakai pada pengambilan citra RGB saja. Hitungan juga bersifat total tanpa pemisahan per kelas.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali, termasuk saat tanaman dikunjungi ulang. Mekanismenya adalah rekonstruksi 3D bertahap: model buah dalam kerangka dunia dicocokkan lintas bingkai dan lintas kunjungan dengan GIoU 3D, dipadukan dengan penyaringan keyakinan. Hitungan dilaporkan sebagai total per sekuens tanpa pemisahan per kelas. Acuan hitungnya adalah anotasi manual per bingkai pada urutan data (bukan hasil panen dan bukan hitung manual di lapangan menurut teks).

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan identitas buah sebagai objek 3D yang diperbarui bertahap dan dicocokkan dengan ukuran tumpang tindih 3D, bukan identitas bingkai. Syaratnya adalah pose sensor yang andal dan pengukuran kedalaman yang memadai. Makalah ini memakai LiDAR, sedangkan masukan multi-sisi sawit berupa citra dari sisi berbeda, sehingga penggunaannya memerlukan sumber geometri lain. Pengelompokan per kelas tidak ditangani.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `park2026incremental`.

Park dkk. (IEEE Robotics and Automation Letters, 2026) mengusulkan pencacahan buah waktu-nyata pada kebun rapat dengan memodelkan tiap buah sebagai kotak 3D berorientasi yang dibuat dari pindaian LiDAR lokal dan segmentasi YOLOv11, lalu diasosiasikan secara bertahap melalui GIoU 3D dan disaring dengan skor keyakinan. Pada dataset kebun tangerin yang dikumpulkan sendiri, metode ini mencapai RMSE hitungan 8,9 (simpangan baku galat 6,4) dan waktu proses rata-rata 35,30 ms per bingkai, lebih baik daripada pelacak 2D dan metode berbasis peta yang dibandingkan.

Catatan verifikasi data: RMSE 8,9, simpangan baku 6,4, RMSE 14,5 dan simpangan baku 7,5 tanpa penyaringan keyakinan tertulis di teks Bagian IV-B. Waktu 35,30 ms dan 28,3 bingkai/detik tertulis di Bagian IV-E; ambang 0,6 dan 0,25, N = 9, serta ambang derau 0,1 m dan 5 titik tertulis di Bagian III dan IV-B; 1.449 citra dan 13.587 masker tertulis di Bagian IV-B. Tabel I (karakteristik dataset), Tabel II (hasil semua metode), dan Tabel III (waktu per modul) tidak terbaca pada teks ekstraksi sehingga jumlah sekuens, jumlah buah acuan, dan RMSE metode pembanding tidak dapat diverifikasi. Nilai ambang 0,03 m pada ablasi jarak disebut di teks tanpa penjelasan lebih lanjut. Hitung acuan adalah anotasi manual per bingkai.
