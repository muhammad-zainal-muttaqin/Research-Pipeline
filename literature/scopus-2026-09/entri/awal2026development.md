# Development of a plant sensing robot using virtual space and evaluation of its accuracy

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `awal2026development` |
| Judul asli | Development of a plant sensing robot using virtual space and evaluation of its accuracy |
| Penulis | Awal, Sutan Muhamad Sadam; Sakurai, Yamato; Thanh Pham, Dong; Nomura, Koichi; Kitano, Masaharu; Yasutake, Daisuke; Mitsuoka, Muneshi; Okayasu, Takashi |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus, tomato, cherry |

## Tautan Akses
- PDF: [awal2026development.pdf](../pdf/awal2026development.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102429

## Gambaran Umum

Makalah ini mengembangkan alur kerja simulasi berbasis ROS 2 dan Gazebo untuk mengevaluasi robot seluler omnidireksional di rumah kaca sebelum diuji secara fisik. Alur kerja itu menyatukan navigasi pusat barisan tanaman berbasis LiDAR, kontrol misi multi-baris dengan penanda AprilTag, pengendalian sudut pandang kamera PTZ (*pan-tilt-zoom*), segmentasi instans YOLO, pelacakan ByteTrack, dan pencacahan tomat ceri per tingkat kematangan (hijau, oranye, merah). Seluruh eksperimen dilakukan pada rumah kaca virtual yang dibangkitkan secara prosedural dengan 126 tanaman dan 1.320 buah sebagai acuan (*ground truth*) pada tingkat tanaman. Tidak ada eksperimen pada rumah kaca nyata.

Pencacahan memakai ByteTrack dengan lapisan identitas kanonik (*canonical ID*): sebuah buah dihitung satu kali ketika titik pusat jejaknya masuk jendela hitung, dan status "sudah dihitung" dipertahankan ketika ByteTrack memberi ID mentah baru setelah jejak terputus. Model segmentasi terpilih adalah YOLOv8m-seg tanpa augmentasi. Pada kecepatan robot 0,2 m/s, sistem menghitung 1.189 buah atau 90,1% dari acuan, dengan MAE tingkat tanaman 2,02 buah, RMSE 4,16 buah, dan F1 tingkat hitungan 0,898. Kinerja turun pada kecepatan 0,6 m/s ke atas (45,6% dari acuan pada 0,6 m/s dan 33,2% pada 1,0 m/s).

Misi AprilTag mereproduksi rute multi-baris pada kecepatan 0,2 sampai 1,0 m/s dengan galat lintas jalur rata-rata 0,045 sampai 0,056 m. Penulis menyatakan bahwa hasil ini adalah kinerja simulasi terkendali dan tidak boleh dibaca sebagai estimasi kinerja di rumah kaca nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Robot rumah kaca harus bernavigasi dan mengindra buah di bawah batas kanopi yang tidak teratur, oklusi, kondisi pengamatan yang berubah, dan ruang transisi antarbaris yang sempit. Penulis menilai bahwa sebagian besar studi terdahulu berfokus pada navigasi, pemanenan, atau satu tugas persepsi saja. Studi yang menyatukan navigasi seluler, sudut pandang kamera yang dapat dikendalikan, kontrol misi berbasis penanda, segmentasi buah, pelacakan multi-objek, dan pencacahan dalam satu lingkungan simulasi dinilai masih sedikit.

Penyatuan itu dianggap penting karena ketepatan pemantauan buah bergantung pada stabilitas lintasan robot, orientasi kamera, kecepatan akuisisi, oklusi, dan asosiasi temporal antarbingkai, bukan hanya pada akurasi model visual. Deteksi atau segmentasi saja tidak cukup untuk pencacahan dari video karena buah yang sama muncul pada banyak bingkai. Penelitian terdahulu penulis memakai sistem kamera PTZ pada robot rel di atas kepala untuk fenotipe mentimun; rel tetap membatasi fleksibilitas pada rumah kaca yang dinamis. Makalah ini mewarisi konsep pengendalian sudut pandang kamera PTZ aktif, bukan perangkat keras rel.

## Ide Utama

Gagasan utamanya adalah memperlakukan simulasi bukan hanya sebagai tempat uji sebelum penerapan, tetapi sebagai alat diagnostik. Dengan acuan tingkat tanaman yang tepat dan lingkungan yang dapat diulang, interaksi antara kecepatan robot, sudut pandang kamera, kualitas segmentasi, kestabilan pelacakan, dan akurasi hitungan dapat diukur secara terpisah dan gabungan.

Untuk masalah identitas buah yang terlihat lebih dari sekali, makalah memakai dua lapis. Lapis pertama adalah pelacakan temporal ByteTrack pada aliran video dari kamera PTZ yang bergerak sepanjang barisan. Lapis kedua adalah ID kanonik yang menyimpan status "sudah dihitung" ketika ID mentah berganti. Pencacahan juga dibatasi oleh daerah minat (*region of interest*, ROI) berupa jendela hitung pada bidang citra.

## Cara Kerja Langkah demi Langkah

### 1. Lingkungan simulasi dan robot

Simulasi berjalan pada Ubuntu 22.04.3 LTS dengan ROS 2 Humble dan Gazebo Classic 11.10.2, pada stasiun kerja Intel Core i5-13400F, RAM 16 GB, dan NVIDIA GeForce RTX 4070. Mesin fisika adalah ODE dengan langkah maksimum 0,001 s. Angin, perubahan iluminasi, dan cuaca tidak diaktifkan.

Robot dimodelkan di Fusion 360 lalu dikonversi ke URDF. Dimensinya 372 mm panjang, 374,5 mm lebar, dan sekitar 1,4 m tinggi, dengan empat roda Mecanum. Di Gazebo, gerak basis dihasilkan oleh plugin `libgazebo_ros_planar_move.so`, sehingga dinamika roda dan gesekan tidak dimodelkan. Sensor yang disimulasikan adalah LiDAR 3D bergaya Velodyne pada 10 Hz, kamera PTZ 1920 × 1080 piksel pada 30 Hz, dan kamera RGB depan 800 × 800 piksel pada 30 Hz, dengan derau Gaussian pada kamera. Bidang pandang horizontal kamera PTZ untuk deteksi tag adalah 1,8 rad (sekitar 103°).

### 2. Rumah kaca virtual dan acuan buah

Tanaman tomat ceri dibangkitkan dengan kerangka simulasi pertanian tomat dari Espejel dkk. Parameternya: *seed* 1000, 6 baris, panjang baris 10 m, jarak antarbaris 1,2 m, jarak antartanaman 0,5 m, dan ukuran dunia 9 × 13 m. Tinggi tanaman 0,8 sampai 1,2 m dan jumlah buah per tanaman 0 sampai 36. Terdapat 126 tanaman (21 per baris) dengan 1.320 buah: merah 828 (62,7%), oranye 336 (25,5%), hijau 156 (11,8%). Rerata buah per tanaman 10,48 ± 11,66, sebanyak 54 tanaman (42,9%) tidak berbuah, koefisien variasi 111,3%, dan entropi Shannon ternormalisasi 0,813. Penulis menyatakan morfologi tomat ini disederhanakan dan bukan representasi botani yang setia.

### 3. Navigasi LiDAR dan misi AprilTag

Pengendali pusat barisan memfilter titik LiDAR (tinggi 0,0 sampai 1,0 m, jarak maksimum 1,0 m), menghitung jarak median ke batas kiri dan kanan dari sepuluh pengukuran terakhir, lalu mengendalikan kecepatan lateral dengan PID diskret (kP 0,70, kI 0,00, kD 0,15, zona mati 0,03 m, kecepatan lateral maksimum 0,12 m/s). Orientasi dijaga dengan PID dari odometri (kP 1,20, kI 0,00, kD 0,15, zona mati 2°). Kecepatan maju nominal 0,3 m/s. Parameter disetel secara empiris di Gazebo.

AprilTag 0 sampai 3 memicu penelusuran maju dan mundur dalam baris serta pemutaran kamera PTZ ke kanan atau kiri. Tag 4 dibaca kamera depan untuk pemindahan lateral ke baris berikutnya, dan tag 5 mengakhiri misi.

### 4. Dataset dan pelatihan segmentasi

Citra dibangkitkan dari dua lingkungan dengan *seed* 1001 dan 1002, dianotasi manual di Roboflow dalam format segmentasi YOLO dengan tiga kelas kematangan. Konfigurasi tanpa augmentasi berisi 755 citra (529 latih, 151 validasi, 75 uji). Augmentasi hanya pada subset latih (tiga keluaran per citra) menghasilkan 1.587 citra latih dan 1.813 citra total, dengan variasi kecerahan −21% sampai +21% dan derau hingga 1,41% piksel. Semua citra diubah menjadi 640 × 640 piksel. Model YOLOv8-seg dan YOLOv11-seg skala n, s, dan m dilatih pada kedua konfigurasi (12 pelatihan) hingga 300 epoch dengan *early stopping* (kesabaran 50), ukuran *batch* 32, SGD, dan laju belajar awal 0,01.

### 5. Pencacahan dengan ByteTrack dan ID kanonik

Model terpilih diterapkan pada urutan citra rekaman robot dari keenam baris, pada satu kondisi statis dan lima kecepatan (0,2; 0,4; 0,6; 0,8; 1,0 m/s). ByteTrack mengasosiasikan deteksi antarbingkai. Sebuah jejak dihitung paling banyak satu kali ketika titik pusatnya memasuki jendela hitung. Lapisan ID kanonik mempertahankan status terhitung ketika jejak diasosiasikan ulang setelah gangguan sementara. Metrik hitungan: Pred./GT (%), MAE, RMSE, serta presisi, *recall*, dan F1 tingkat hitungan dengan $TP_i=\min(C_i,G_i)$, $FP_i=\max(C_i-G_i,0)$, $FN_i=\max(G_i-C_i,0)$. Pengaruh kondisi akuisisi diuji dengan uji Friedman dan perbandingan berpasangan terkoreksi Holm.

## Eksperimen dan Hasil

### Deteksi AprilTag

Pada uji jarak, tidak ada deteksi pada 0,00 sampai 0,50 m (0 dari 65), 98,70% pada 0,50 sampai 0,75 m (76 dari 77), dan 100% pada semua interval 0,75 sampai 1,50 m. Pada uji sudut pandang, keberhasilan 100% pada 5 sampai 15° dan 15 sampai 30°, tetapi 40,10% pada 0 sampai 5° dan 39,22% pada 30 sampai 45°. Pada uji kecepatan, keberhasilan tertinggi 90,57% pada 0,207 m/s dan terendah 52,63% pada 0,864 m/s.

### Navigasi LiDAR

RMSE lintasan di bawah 0,012 m pada lima baris tanaman dan satu koridor dinding sebagai pembanding, masing-masing dengan satu lintasan acuan manual (joystick) dan tiga pengulangan otonom per arah. RMSE maju pada baris tanaman 0,0040 sampai 0,0111 m dan mundur 0,0011 sampai 0,0021 m. Galat sudut arah (*heading MAE*) di bawah 4,30°. Penulis menjelaskan bahwa selisih maju dan mundur sebagian disebabkan oleh keadaan awal pengendali dan sebagian oleh normalisasi awal-akhir pada pascapemrosesan.

### Misi AprilTag multi-baris (tiga pengulangan per kecepatan)

| Kecepatan (m/s) | MAE (m) | RMSE (m) | Persentil ke-95 (m) | Galat maksimum (m) |
|---|---|---|---|---|
| 0,2 | 0,045 ± 0,003 | 0,064 ± 0,002 | 0,072 ± 0,004 | 0,815 ± 0,007 |
| 0,4 | 0,049 ± 0,017 | 0,076 ± 0,026 | 0,099 ± 0,012 | 0,914 ± 0,465 |
| 0,6 | 0,056 ± 0,011 | 0,094 ± 0,028 | 0,107 ± 0,011 | 0,827 ± 0,408 |
| 0,8 | 0,053 ± 0,011 | 0,091 ± 0,004 | 0,149 ± 0,038 | 0,825 ± 0,047 |
| 1,0 | 0,051 ± 0,004 | 0,092 ± 0,003 | 0,123 ± 0,041 | 0,841 ± 0,015 |

Galat maksimum terjadi terutama di ujung jalur dan saat transisi lateral antarbaris.

### Pemilihan model segmentasi (validasi, epoch terbaik menurut mAP50-95 mask)

| Pelatihan | Model | P mask | R mask | F1 mask | mAP50-95 mask | mAP50-95 kotak | FPS |
|---|---|---|---|---|---|---|---|
| Tanpa aug. | YOLOv8n | 0,780 | 0,728 | 0,753 | 0,330 | 0,619 | 56,72 |
| Tanpa aug. | YOLOv8s | 0,786 | 0,770 | 0,778 | 0,368 | 0,655 | 53,81 |
| Tanpa aug. | YOLOv8m (dipilih) | 0,790 | 0,770 | 0,780 | 0,374 | 0,651 | 54,10 |
| Tanpa aug. | YOLOv11m | 0,786 | 0,768 | 0,777 | 0,382 | 0,652 | 43,35 |
| Aug. | YOLOv8m | 0,772 | 0,779 | 0,775 | 0,377 | 0,670 | 45,42 |
| Aug. | YOLOv11m | 0,646 | 0,779 | 0,706 | 0,416 | 0,336 | 58,75 |

Tabel 8 pada makalah memuat dua belas baris. Tabel di atas hanya mengutip enam baris. YOLOv11m-seg dengan augmentasi memiliki mAP50-95 mask tertinggi (0,416) tetapi tidak dipilih karena presisi dan F1 rendah dapat menimbulkan penghitungan berlebih. YOLOv8m-seg tanpa augmentasi dipilih berdasarkan keseimbangan F1, kinerja lokalisasi, dan kecepatan.

### Pencacahan buah tingkat tanaman (126 tanaman, 1.320 buah)

| Kondisi | Pred./GT (%) | MAE | RMSE | Presisi | Recall | F1 |
|---|---|---|---|---|---|---|
| Statis | 81,2 | 3,38 | 6,13 | 0,917 | 0,745 | 0,822 |
| 0,2 m/s | 90,1 | 2,02 | 4,16 | 0,948 | 0,854 | 0,898 |
| 0,4 m/s | 74,8 | 3,78 | 6,71 | 0,927 | 0,694 | 0,794 |
| 0,6 m/s | 45,6 | 5,89 | 10,09 | 0,980 | 0,447 | 0,614 |
| 0,8 m/s | 40,7 | 7,53 | 11,70 | 0,845 | 0,344 | 0,489 |
| 1,0 m/s | 33,2 | 7,27 | 11,39 | 0,961 | 0,319 | 0,479 |

Uji Friedman menunjukkan pengaruh nyata kondisi akuisisi ($\chi^2(5)=162{,}95$, $p<0{,}001$, $W$ Kendall 0,259). Kondisi 0,2 m/s memiliki galat mutlak lebih rendah daripada kondisi statis ($p=0{,}040$) dan semua kecepatan lebih tinggi ($p<0{,}001$); statis dan 0,4 m/s tidak berbeda nyata ($p=0{,}158$). Penurunan pada kecepatan tinggi didominasi oleh buah yang terlewat, bukan penghitungan berlebih: pada 0,6 dan 1,0 m/s presisi tetap 0,980 dan 0,961 sedangkan *recall* turun menjadi 0,447 dan 0,319.

### Diagnostik identitas dan kematangan

Dari jejak kanonik yang terhitung, 71,2% terkait lebih dari satu ID ByteTrack mentah dan 62,0% mengalami sekurangnya satu penautan ulang setelah dihitung. Sekitar 26,1% jejak mendapat lebih dari satu label kematangan selama masa hidupnya, dan 18,4% menunjukkan pergantian merah-oranye. Evaluasi awal terbatas ByteTrack pada delapan bingkai beranotasi manual dari satu urutan 0,2 m/s menghasilkan MOTA 34,9%, IDF1 54,0%, presisi 89,2%, dan *recall* 82,8%; penulis menyebutnya diagnostik, bukan tolok ukur MOT formal. Kasus kualitatif: pada Baris 1 Tanaman 8, acuan berisi 12 buah oranye tanpa buah merah, sedangkan prediksi berisi 10 oranye dan satu merah; pada Baris 6 Tanaman 1, sistem menghitung 9 dari 12 buah merah karena oklusi kanopi.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: lingkungan dapat diulang dengan acuan tepat per tanaman dan kelas, evaluasi gabungan navigasi dan persepsi pada beberapa kecepatan, serta pelaporan galat yang jujur (misalnya penyebab selisih maju dan mundur, serta bahwa metrik presisi, *recall*, dan F1 bersifat tingkat hitungan, bukan tingkat objek).

Keterbatasan yang dinyatakan penulis: iluminasi simulasi stabil dan tanpa angin; model tanaman dan tekstur terbatas; simulasi LiDAR tanpa model derau dan kehilangan pengukuran sehingga hasil navigasi mungkin optimistis; tanaman statis; roda tidak dimodelkan; tag dapat tertutup atau rusak pada kondisi nyata; tidak ada penghindaran rintangan dinamis; ROI dan ID kanonik menekan duplikasi temporal tetapi tidak menolak buah dari baris sebelah yang jatuh dalam ROI; frame-level ID acuan tidak tersedia sehingga evaluasi MOT standar tidak dapat dilakukan; kecepatan 0,2 m/s dan batas atas 0,4 m/s hanya berlaku untuk konfigurasi ini. Data disebut tersedia atas permintaan. Validasi fisik direncanakan, termasuk gerbang kedalaman untuk menolak buah dari baris tetangga.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pertama, citra pelatihan dan citra uji berasal dari generator yang sama dengan tekstur buah yang sederhana, sehingga akurasi segmentasi dan kebingungan merah-oranye tidak mewakili variasi buah nyata. Kedua, perbandingan kecepatan memakai urutan rekaman yang sama untuk setiap baris, dan makalah menyatakan bahwa pemrosesan ulang tidak dianggap sebagai percobaan independen, sehingga sebaran statistik hanya mencerminkan variasi antartanaman pada satu lingkungan. Ketiga, hasil pencacahan mengandalkan hanya sisi baris yang dilihat kamera PTZ pada satu penelusuran maju atau mundur, dan makalah tidak membandingkan cakupan kedua sisi baris sebagai identitas lintas sisi. Keempat, tidak ada pembanding pencacahan lain seperti metode tanpa ID kanonik, sehingga kontribusi lapisan ID kanonik terhadap hitungan akhir tidak dikuantifikasi.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme pelacakan video: segmentasi YOLO, ByteTrack, ID kanonik yang menyimpan status terhitung setelah penautan ulang, dan ROI yang membatasi pencacahan pada jendela hitung. Identitas dipertahankan sepanjang waktu pada satu sisi barisan yang diamati. Makalah tidak menyatukan identitas buah antarsisi pohon atau antarpenelusuran maju dan mundur, dan mekanismenya tidak memakai pencocokan geometris multi-pandang. Penulis juga menyatakan bahwa ROI dan ID kanonik tidak menolak buah dari baris tetangga, dan mengusulkan gerbang kedalaman sebagai pekerjaan lanjutan yang belum diuji.

Hitungan dilaporkan per kelas kematangan (hijau, oranye, merah), tetapi hasil kuantitatif utama (Tabel 9) dilaporkan sebagai jumlah total per tanaman; acuan per kelas hanya dipakai pada kasus kualitatif. Acuan hitung adalah pemetaan manual baris dan tanaman terhadap lingkungan yang dibangkitkan (*ground truth* sintetis), bukan panen, hitung lapangan, atau anotasi citra nyata. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan ID kanonik yang mempertahankan status terhitung setelah jejak terputus, diagnostik fragmentasi ID, serta temuan bahwa kecepatan akuisisi menentukan *recall*. Bukti makalah terbatas pada data simulasi dan satu tanaman kecil berbuah ceri, sehingga tidak ada bukti untuk tandan sawit.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `awal2026development`.

Awal dkk. mengembangkan alur kerja simulasi ROS 2 dan Gazebo untuk robot omnidireksional di rumah kaca virtual yang dibangkitkan secara prosedural (126 tanaman tomat ceri, 1.320 buah), yang menyatukan navigasi LiDAR, kontrol misi AprilTag, segmentasi YOLOv8m-seg, ByteTrack, dan pencacahan ber-ID kanonik per tingkat kematangan. Pada kecepatan 0,2 m/s sistem menghitung 90,1% dari acuan dengan F1 tingkat hitungan 0,898, dan kinerja menurun nyata pada kecepatan 0,6 m/s ke atas terutama karena buah yang terlewat. Hasil ini berasal dari simulasi dan belum divalidasi pada rumah kaca nyata.

Catatan verifikasi data: Angka pencacahan utama (Pred./GT, MAE, RMSE, presisi, *recall*, F1) tercantum pada Tabel 9 (seksi 3.4), dan hasil uji Friedman pada teks seksi 3.4. Angka model segmentasi berasal dari Tabel 8 (seksi 3.3), dan hanya enam dari dua belas baris yang dikutip di atas. Statistik acuan buah (1.320 buah, 828 merah, 336 oranye, 156 hijau, 126 tanaman) berasal dari seksi 2.3. Angka navigasi dan misi berasal dari Tabel 6 dan Tabel 7 serta seksi 3.2, dan hasil AprilTag dari Tabel 5. Evaluasi ByteTrack (MOTA 34,9%, IDF1 54,0%) berasal dari seksi 2.6.3. Teks ekstraksi dapat dibaca tanpa kerusakan berarti pada bagian yang dirujuk. Tabel yang bergantung pada gambar (Gambar 14 dan 16 sampai 18) tidak diverifikasi nilainya. Tidak dilaporkan: jumlah instans buah per kelas pada dataset pelatihan, jumlah bingkai atau durasi video per kecepatan, dan hitungan akhir per kelas kematangan secara agregat. Daftar pustaka tidak dibaca seluruhnya.
