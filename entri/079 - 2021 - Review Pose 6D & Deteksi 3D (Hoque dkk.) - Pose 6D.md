# 079 - A Comprehensive Review on 3D Object Detection and 6D Pose Estimation With Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hoque2021posesurvey` |
| Judul asli | A Comprehensive Review on 3D Object Detection and 6D Pose Estimation With Deep Learning |
| Penulis | Sabera Hoque, Md. Yasir Arafat, Shuxiang Xu, Ananda Maiti, Yuchen Wei |
| Tahun | 2021 |
| Venue | IEEE Access, vol. 9, hlm. 143746–143770 |
| Tema | Pose 6D |

## Tautan Akses
- **DOI (akses terbuka, lisensi CC-BY):** https://doi.org/10.1109/ACCESS.2021.3114399
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Comprehensive%20Review%20on%203D%20Object%20Detection%20and%206D%20Pose%20Estimation%20with%20Deep%20Learning
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Comprehensive%20Review%20on%203D%20Object%20Detection%20and%206D%20Pose%20Estimation%20with%20Deep%20Learning&sort=relevance

## Gambaran Umum

Makalah ini adalah survei yang memetakan dua tugas persepsi tiga dimensi yang berkembang secara paralel namun jarang dibahas dalam satu kerangka: deteksi objek 3D (memprediksi kotak pembatas tiga dimensi — pusat, ukuran, dan orientasi objek — beserta kelasnya) dan estimasi pose 6D (memulihkan enam derajat kebebasan posisi suatu objek yang model tiganya sudah diketahui: tiga derajat rotasi dan tiga derajat translasi relatif terhadap kamera). Deteksi 3D cukup menemukan dan mengelompokkan objek dalam ruang; estimasi pose 6D menuntut kecocokan penuh terhadap satu instans objek tertentu, sehingga hasilnya dapat dipakai langsung untuk manipulasi fisik oleh robot.

Sintesis dilakukan atas metode berbasis *deep learning* (pembelajaran mendalam menggunakan jaringan saraf berlapis banyak) yang bekerja pada tiga jenis masukan sensor: citra RGB semata, data kedalaman berbentuk *point cloud* (awan titik — himpunan titik tiga dimensi hasil pengukuran sensor), dan gabungan RGB-D. Kendaraan otonom dipakai sebagai studi kasus karena domain ini membutuhkan kedua tugas sekaligus: deteksi 3D untuk melokalisasi kendaraan dan pejalan kaki di sekitar, serta potensi kebutuhan pose 6D pada tahap interaksi fisik lanjutan. Menurut abstrak makalah, meskipun sudah banyak riset pada estimasi pose 6D dari citra RGB, tantangannya belum sepenuhnya terpecahkan; survei ini merangkum metode, kumpulan data, metrik evaluasi, dan kendala yang masih terbuka, sekaligus menunjukkan perbandingan antarkerangka kerja populer. Dalam tinjauan pustaka ini, bab tersebut berfungsi sebagai peta yang menaungi rangkaian bab metode tunggal pose 6D (bab 073–078).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum survei ini ditulis, riset deteksi objek 3D dan estimasi pose 6D berkembang dari dua komunitas yang berbeda kebiasaan. Deteksi objek 3D tumbuh dari kebutuhan kendaraan otonom, memakai sensor LiDAR (*Light Detection and Ranging* — sensor pengukur jarak dengan pantulan laser) dan kumpulan data seperti KITTI, dievaluasi dengan *Average Precision* (AP, rata-rata presisi) pada ambang *Intersection over Union* (IoU) tiga dimensi. Estimasi pose 6D tumbuh dari kebutuhan robotika manipulasi, memakai sensor RGB-D murah seperti Kinect, dievaluasi dengan metrik ADD dan ADD-S (dijelaskan pada bagian berikutnya). Kedua komunitas memakai teknik *deep learning* yang serupa — konvolusi, jaringan awan titik, fusi lintas modalitas — tetapi jarang saling merujuk karena istilah, kumpulan data, dan protokol pengujiannya berbeda.

Masalah praktisnya adalah kecepatan kemunculan metode baru. Dalam lima tahun sebelum survei ini terbit, muncul berturut-turut PoseCNN (bab 073) yang meregresi pose langsung dari RGB, DenseFusion (bab 074) yang memfusikan fitur RGB dan kedalaman per piksel, PVN3D (bab 075) yang memindahkan prediksi ke pemungutan suara titik kunci pada awan titik, serta FFB6D (bab 076) yang memperdalam fusi menjadi dua arah pada setiap lapisan jaringan. Bagi peneliti yang perlu memilih metode untuk aplikasi tertentu, perbandingan yang adil antarmetode sulit dilakukan karena setiap makalah asli melaporkan angkanya sendiri pada *backbone*, sensor, dan pembagian data yang tidak selalu sama. Kebutuhan yang belum terpenuhi adalah satu rujukan yang menyusun ulang literatur yang terfragmentasi ini ke dalam kerangka klasifikasi yang konsisten.

## Ide Utama

Gagasan inti survei ini adalah mengorganisasi literatur yang tersebar ke dalam dua sumbu yang saling silang: jenis tugas (deteksi objek 3D atau estimasi pose 6D) dan jenis masukan sensor (RGB semata, kedalaman/awan titik semata, atau fusi RGB-D). Pada setiap sel dari matriks ini, survei mendaftar metode representatif serta kumpulan data dan metrik yang biasa dipakai pada sel tersebut, sehingga metode yang tidak pernah dibandingkan langsung dalam makalah aslinya dapat ditempatkan pada kerangka pembanding yang sama memakai angka yang masing-masing sudah dilaporkan penulis aslinya. Kendaraan otonom dipilih sebagai studi kasus karena satu domain ini memerlukan hampir seluruh sel matriks tersebut sekaligus: LiDAR murni dan fusi kamera-LiDAR untuk deteksi 3D di jalan raya, sedangkan prinsip pose 6D relevan bagi tugas manipulasi hilir seperti bongkar-muat otomatis.

## Cara Kerja Langkah demi Langkah

Bagian ini menguraikan metodologi survei — cara ia menyusun taksonomi dan memetakan literatur — bukan pipeline satu model, karena makalah ini adalah karya tinjauan, bukan usulan metode baru.

### Definisi Cakupan Dua Tugas

Survei memulai dengan memisahkan dua definisi tugas secara eksplisit. Deteksi objek 3D memprediksi kotak pembatas berorientasi bebas (*oriented bounding box*) dalam ruang tiga dimensi tanpa memerlukan model tiga dimensi spesifik dari objeknya; cukup diketahui kelasnya. Estimasi pose 6D mengasumsikan model tiga dimensi objek sudah tersedia (bekerja pada tingkat instans, bukan tingkat kategori) dan mengeluarkan matriks transformasi lengkap [R|T] — R matriks rotasi 3×3, T vektor translasi tiga elemen — yang menyelaraskan model itu ke pose objek pada citra. Pemisahan ini penting karena kedua tugas sering disebut campur aduk dalam literatur populer, padahal kebutuhan datanya berbeda: deteksi 3D cukup dilatih dari anotasi kotak, sedangkan pose 6D memerlukan model CAD (*Computer-Aided Design*) per objek.

### Taksonomi Berdasarkan Modalitas Sensor

Untuk setiap tugas, survei mengelompokkan metode menurut modalitas masukan yang dipakai: RGB semata, awan titik/kedalaman semata, atau fusi RGB-D. Pengelompokan ini dipilih karena modalitas sensor menentukan kelas kesalahan yang dihadapi metode: pendekatan RGB semata kehilangan skala absolut akibat proyeksi perspektif kamera, pendekatan awan titik semata kehilangan tekstur sehingga sulit membedakan objek berbentuk mirip tetapi berpenampakan berbeda, sedangkan fusi RGB-D berusaha menutup kedua celah itu dengan menggabungkan keduanya. Struktur pengelompokan tersebut dapat diringkas sebagai berikut.

```
              persepsi 3D dalam tinjauan Hoque dkk. (2021)
     ┌───────────────────────┴───────────────────────┐
deteksi objek 3D                              estimasi pose 6D
(kotak pembatas 3D + kelas)         (rotasi R + translasi T, objek dikenal)
     │                                               │
 ┌───┼────┐                                     ┌────┼────┐
RGB  titik RGB+LiDAR                            RGB  titik RGB-D
murni awan (fusi sensor)                        murni awan (fusi padat,
                                                       dominan pada literatur)
     │                                               │
tolok ukur: KITTI                          tolok ukur: LineMOD, YCB-Video
metrik: AP pada ambang IoU 3D               metrik: ADD, ADD-S
```

Pada cabang deteksi 3D, metode berbasis awan titik dibagi menjadi pendekatan voksel (memetakan titik ke sel-sel grid tiga dimensi lalu memakai konvolusi tiga dimensi) dan pendekatan titik langsung (memproses koordinat mentah tanpa voksel, mengikuti garis keturunan PointNet). Pada cabang pose 6D, survei membedakan regresi langsung (jaringan memprediksi R dan T langsung, seperti PoseCNN), metode berbasis korespondensi (memprediksi titik dua dimensi lalu tiga dimensi, diselesaikan dengan algoritme PnP — *Perspective-n-Point*), dan pemungutan suara titik kunci (setiap titik memprediksi arah menuju titik kunci tiga dimensi, seperti PVN3D dan FFB6D). Fusi RGB-D disebut mendominasi literatur pose 6D karena robot memerlukan ketahanan terhadap oklusi (objek terhalang sebagian) yang sulit dicapai satu modalitas saja.

### Kumpulan Data dan Metrik yang Dipetakan

Survei menyusun daftar kumpulan data standar tiap kelompok metode. Untuk deteksi 3D, KITTI menjadi rujukan utama: kumpulan data adegan luar ruang dari sensor LiDAR dan kamera stereo, dengan pembagian tingkat kesulitan mudah, sedang, dan sulit berdasarkan tingkat oklusi dan ukuran objek pada citra, dievaluasi dengan AP pada ambang IoU tiga dimensi tertentu. Untuk estimasi pose 6D, LineMOD (13 objek bertekstur rendah, satu instans per adegan) dan YCB-Video (21 objek pada adegan berantakan dengan banyak instans) menjadi rujukan utama, dievaluasi dengan ADD (rata-rata jarak titik model pada pose prediksi terhadap pose kebenaran, untuk objek asimetris) dan ADD-S (versi jarak ke titik-terdekat, adil bagi objek simetris karena banyak orientasi tampak identik).

### Studi Kasus Kendaraan Otonom dan Tantangan Terbuka

Kendaraan otonom menjadi benang merah yang menghubungkan kedua tugas: LiDAR dan kamera melakukan deteksi 3D terhadap kendaraan dan pejalan kaki lain, sementara prinsip pose 6D relevan bagi tugas hilir yang memerlukan kepresisian lebih tinggi. Dari sintesis literatur, survei mengidentifikasi tantangan berulang pada kedua tugas: oklusi, simetri objek yang membuat pose ambigu, kesenjangan domain antara data sintetis dan data nyata, serta generalisasi ke objek yang belum pernah dilihat saat pelatihan (masalah tingkat kategori versus tingkat instans yang disinggung pada bagian definisi tugas). Tantangan generalisasi ke objek baru inilah yang kemudian menjadi fokus langsung metode yang lebih baru seperti FoundationPose (bab 078), terbit tiga tahun setelah survei ini.

## Eksperimen dan Hasil

Sebagai karya tinjauan, makalah ini tidak menjalankan eksperimen sendiri; "hasil" yang disajikan adalah kompilasi dan perbandingan angka yang telah dilaporkan oleh makalah-makalah primer, disusun ulang ke dalam tabel per kumpulan data dan per metrik agar dapat dibandingkan berdampingan. Berdasarkan abstrak makalah, penulis secara eksplisit menyatakan tujuan ini: menyusun perbandingan antara sejumlah kerangka kerja populer pada deteksi objek 3D dan estimasi pose 6D. Isi tabel perbandingan itu sendiri — nilai AP per metode pada KITTI, nilai ADD/ADD-S per metode pada LineMOD dan YCB-Video — tidak dapat diakses dalam bentuk teks lengkap oleh penulis bab ini karena naskah penuh berada di balik pembatas akses yang tidak dapat diambil; hanya abstrak dan ringkasan otomatis dari basis data sitasi yang berhasil diverifikasi. Sebagai gambaran kualitatif yang konsisten dengan makalah-makalah primer yang dibahas pada bab lain tinjauan ini (bab 073–077), metode fusi RGB-D secara umum melaporkan ADD-S lebih tinggi daripada metode RGB semata, dan metode pemungutan suara titik kunci melaporkan galat lokalisasi lebih kecil daripada regresi pose langsung — tren yang selaras dengan taksonomi survei, tetapi angka tabel spesifik dari naskah Hoque dkk. sendiri perlu dicocokkan langsung ke sumber asli sebelum dikutip.

## Kelebihan dan Keterbatasan

Kelebihan survei ini terletak pada cakupan gandanya: sebagian besar tinjauan pose 6D hanya membahas estimasi pose, sedangkan survei ini menyandingkannya dengan deteksi objek 3D dalam satu kerangka klasifikasi yang konsisten, memakai studi kasus kendaraan otonom untuk mengaitkan keduanya secara praktis. Pemetaan kumpulan data dan metrik antarkomunitas riset yang biasanya terpisah memudahkan pembaca baru memahami lanskap bidang tanpa menelusuri puluhan makalah primer satu per satu. Identifikasi tantangan terbuka pada bagian akhir — generalisasi ke objek baru, oklusi, simetri — terbukti relevan karena tantangan itu menjadi sasaran langsung metode yang terbit setelahnya, seperti FoundationPose.

Dari sisi rekayasa, keterbatasan yang melekat pada semua karya tinjauan berlaku di sini: karena diterbitkan tahun 2021, tabel perbandingannya tidak memuat metode yang terbit setelahnya, seperti FoundationPose dan detektor 3D berbasis transformer. Secara konseptual, perbandingan lintas makalah yang disusun ulang survei tetap mewarisi ketidaksetaraan protokol pengujian dari makalah aslinya — perangkat keras, pembagian data latih-uji, dan *backbone* yang berbeda-beda — sehingga angka yang disandingkan tidak selalu dapat dibandingkan secara ketat apel-ke-apel, keterbatasan umum pada agregasi literatur pascaterbit, bukan kekhususan survei ini semata. Keterbatasan tambahan bagi bab ini: karena naskah penuh tidak terjangkau saat penulisan ulang, rincian metode pada tiap sel taksonomi disajikan secara kualitatif berdasarkan abstrak dan konsistensi dengan bab-bab metode primer dalam klaster yang sama.

## Kaitan dengan Bab Lain

Bab ini menaungi seluruh klaster Pose 6D dalam tinjauan sebagai peta lanskap, bukan sebagai satu metode tunggal. [PoseCNN (bab 073)](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md) mewakili sel regresi pose langsung berbasis RGB; [DenseFusion (bab 074)](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md) dan [PVN3D (bab 075)](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md) mewakili sel fusi RGB-D dengan pemungutan suara titik kunci; [FFB6D (bab 076)](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md) memperdalam sel yang sama dengan fusi dua arah; [G2L-Net (bab 077)](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md) menjadi pembanding tambahan pada LineMOD. Tantangan generalisasi ke objek baru yang diidentifikasi survei ini menjadi rujukan langsung [FoundationPose (bab 078)](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md), terbit tiga tahun sesudahnya dan menyasar batasan tingkat-instans yang sama. Fungsi bab ini setara dengan klaster Survei YOLO (bab 026–034) bagi keluarga YOLO: rangkuman lintas metode yang memposisikan setiap bab metode tunggal dalam lanskap bidang yang lebih luas.

## Poin untuk Sitasi

Kutip dengan kunci `hoque2021posesurvey`. Ringkasan yang aman dikutip: "Hoque dkk. (2021) menyusun tinjauan yang memetakan deteksi objek 3D dan estimasi pose 6D berbasis *deep learning* ke dalam taksonomi bersama menurut jenis tugas dan modalitas sensor (RGB, awan titik, RGB-D), menyandingkan kumpulan data dan metrik dari kedua komunitas riset, dan memakai kendaraan otonom sebagai studi kasus." Catatan verifikasi sebelum sitasi formal: naskah penuh (IEEE Access, DOI 10.1109/ACCESS.2021.3114399, akses terbuka CC-BY) tidak berhasil diambil teks lengkapnya oleh penulis bab ini — hanya abstrak dan ringkasan otomatis dari basis data sitasi (Semantic Scholar) yang terverifikasi; rincian isi tabel perbandingan metode, daftar lengkap metode per sel taksonomi, dan angka AP/ADD/ADD-S spesifik yang dikutip di dalam naskah Hoque dkk. wajib dicocokkan langsung ke PDF asli via DOI sebelum dipakai dalam karya formal.
