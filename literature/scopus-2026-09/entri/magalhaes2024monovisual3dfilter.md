# MonoVisual3DFilter: 3D tomatoes' localisation with monocular cameras using histogram filters

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `magalhaes2024monovisual3dfilter` |
| Judul asli | MonoVisual3DFilter: 3D tomatoes' localisation with monocular cameras using histogram filters |
| Penulis | Magalh\~aes, Sandro Augusto Costa; dos Santos, Filipe Neves; Moreira, Ant\'onio Paulo; Dias, Jorge Manuel Miranda |
| Tahun | 2024 |
| Venue | Robotica |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [magalhaes2024monovisual3dfilter.pdf](../pdf/magalhaes2024monovisual3dfilter.pdf)
- DOI resmi: https://doi.org/10.1017/s0263574724000936

## Gambaran Umum
Makalah ini mengusulkan MonoVisual3DFilter, yaitu algoritma untuk memperkirakan posisi tiga dimensi (3D) buah tomat dari kotak pembatas (*bounding box*) hasil deteksi pada kamera monokular. Algoritma ini memakai filter histogram (*histogram filter*), yaitu filter Bayes diskret yang diterapkan pada ruang keadaan kontinu yang dibagi menjadi sel-sel grid. Kamera dipindahkan ke beberapa sudut pandang tetap, dan probabilitas keberadaan objek pada setiap sel diperbarui di setiap sudut pandang. Motivasi penulis adalah keterbatasan kamera RGB-D pada lingkungan lapangan terbuka akibat gangguan pencahayaan.

Pengujian dilakukan pada tiga percobaan: dua percobaan simulasi dengan enam bola (diameter 5 cm dan 10 cm) di Ignition Gazebo, tanpa dan dengan derau, serta satu percobaan di meja uji laboratorium dengan tomat plastik dan daun buatan. Meja uji memakai kamera OAK-1 yang dipasang pada lengan robot Robotis Manipulator-H dan detektor YOLO v8 Tiny. Dua jenis kernel dibandingkan, yaitu kernel persegi dan kernel Gaussian, serta dua cara menghitung pusat objek, yaitu pusat geometris dan pusat terbobot.

Hasil utama menurut abstrak: galat absolut rata-rata (*mean absolute error*, MAE) di bawah 10 mm pada simulasi dan di bawah 20 mm pada meja uji laboratorium dengan jarak pengamatan sekitar 0,5 m. Pada Tabel II, MAE meja uji berkisar 0,0100 m sampai 0,0127 m, dan galat Euklides rata-rata berkisar 0,0204 m sampai 0,0222 m. Makalah tidak memuat pencacahan buah dan tidak menguji pohon atau buah nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan dan pemanenan buah oleh robot memerlukan posisi spasial buah. Penulis menyatakan bahwa sebagian besar penelitian persepsi buah memakai sensor RGB-D, tetapi sensor tersebut cenderung bermasalah di lapangan terbuka akibat pantulan dan pencahayaan yang kuat, dan sebagian besar uji dilakukan pada kondisi terkendali. Pertanyaan penelitian yang diajukan adalah bagaimana sensor monokular dapat dipakai dan dikendalikan untuk mempersepsikan posisi objek dalam ruang tugas 3D.

Penulis meninjau tiga kelompok alternatif. Pertama, jaringan saraf konvolusional (*convolutional neural network*, CNN) untuk estimasi kedalaman relatif atau pose 3D dari citra monokular, misalnya keluarga MiDaS. Kedua, algoritma estimasi pose berbasis pembelajaran mendalam seperti SilhoNet, Nerf-Pose, GDR-Net, MORE, dan GhostPose, yang menurut Tabel I dan teks melaporkan galat sekitar 2 cm atau kurang pada dataset masing-masing; Imitrob melaporkan galat 6,5 cm. Penulis menilai sebagian besar pendekatan itu bergantung pada model objek dan memerlukan banyak data berlabel. Ketiga, sensor tambahan seperti LiDAR, yang disebut mahal dan menambah beban pada manipulator. Penulis memilih pendekatan probabilistik karena dianggap lebih mudah diprediksi dan dijelaskan serta tidak bergantung pada data pelatihan khusus.

## Ide Utama
Gagasan utamanya adalah memperlakukan setiap deteksi kotak pembatas sebagai bukti probabilistik tentang ruang 3D di depan kamera. Setiap sel grid 3D diproyeksikan ke bidang citra pada setiap sudut pandang. Sel yang jatuh di dalam (atau dekat) kotak pembatas memperoleh probabilitas tinggi. Probabilitas dari semua sudut pandang dikalikan, sehingga hanya sel yang konsisten dengan seluruh pandangan yang tetap bernilai tinggi. Cara ini serupa dengan triangulasi, sebagaimana dinyatakan penulis. Setelah semua sudut pandang diproses, sel yang tersisa dikelompokkan dan pusat tiap kelompok dijadikan posisi satu objek.

Perlu dicatat bahwa identitas objek antarpandang tidak ditentukan melalui pencocokan eksplisit. Jumlah objek diambil dari jumlah deteksi pada kamera, dan algoritma *k-means* dengan jumlah kelompok sama dengan jumlah objek itu memisahkan awan sel menjadi objek-objek individual. Makalah tidak menjelaskan penanganan kasus ketika jumlah deteksi berbeda antarsudut pandang.

## Cara Kerja Langkah demi Langkah

```
  Deteksi bbox (YOLO v8 Tiny / detektor simulasi) pada tiap sudut pandang
        |
        v
  Grid 3D sel (probabilitas awal = 1 untuk semua sel)
        |
        v
  Untuk tiap sudut pandang: proyeksi sel -> citra (model pinhole)
        |        probabilitas sel dari kernel (persegi / Gaussian)
        v
  Kalikan dengan probabilitas sebelumnya, normalisasi
        |
        v
  k-means (k = jumlah objek terdeteksi) -> pusat geometris / terbobot
```

### 1. Akuisisi data dan platform
Simulasi memakai Ignition Gazebo dengan enam bola berukuran 5 cm dan 10 cm serta kamera kotak pembatas yang dipindahkan ke tiga sudut pandang tetap. Pada meja uji laboratorium, penulis membangun tanaman tiruan dengan daun buatan dan tomat plastik realistik, dengan kamera OAK-1 (modul RGB 12 MP) pada lengan Robotis Manipulator-H enam derajat kebebasan yang terpasang pada robot AgRob v16 berbasis Clearpath Husky. Detektor yang dipakai adalah YOLO v8 Tiny yang dilatih pada dataset tomat (rujukan [45, 46] pada makalah) dan beberapa sampel tomat plastik dari berbagai sudut. Jumlah citra latih tidak dilaporkan pada bagian yang dibaca.

Pada meja uji, satu sampai tiga tomat dilokalisasi sekaligus dalam enam percobaan, dengan total sepuluh tomat dan enam puluh pengukuran menurut teks. Lengan dipindahkan ke tiga pose tetap; semua permutasi pose dipakai sehingga setiap tomat menghasilkan enam estimasi per percobaan. Posisi acuan (*ground truth*) tomat diperoleh dari kinematika lengan: ujung efektor digerakkan hingga menyentuh buah, lalu posisinya dibaca dalam kerangka basis manipulator.

### 2. Dekomposisi ruang keadaan
Ruang di sekitar objek dibagi menjadi grid 3D hanya pada bagian yang dapat dijangkau manipulator, yaitu dua kali jangkauan manipulator, dengan pusat pada kerangka kamera di bidang yOz dan terjarak sejauh radius jangkauan pada sumbu Ox. Grid dibuat saat kamera pertama kali mendeteksi objek pada sudut pandang pertama. Probabilitas awal setiap sel adalah 1, sehingga objek dianggap mungkin berada di mana saja.

### 3. Pembaruan probabilitas dan kernel
Setiap sel ditransformasikan dari kerangka basis manipulator ke kerangka citra. Probabilitas sel pada satu sudut pandang adalah rata-rata dari probabilitas terhadap setiap kotak pembatas $j$ (persamaan 2), dan probabilitas total dikalikan dengan probabilitas sebelumnya (persamaan 3). Dua kernel dipelajari. Kernel persegi bernilai 1 bila titik berada di dalam kotak pembatas dan 0 bila di luar. Kernel Gaussian dua dimensi berpusat pada pusat kotak dengan simpangan baku $(\sigma_x, \sigma_y)$ yang sama dengan setengah ukuran kotak; pada percobaan simulasi dengan derau, penulis memakai $N(0, \text{ukuran}/3)$. Probabilitas per sudut pandang dan probabilitas total dinormalisasi dengan nilai maksimumnya.

### 4. Model proyeksi kamera
Transformasi memakai model lubang jarum (*pinhole*) dengan matriks intrinsik yang bergantung pada lebar dan tinggi citra serta panjang fokus, dihitung dari medan pandang horizontal. Untuk OAK-1, kalibrasi intrinsik tambahan dilakukan dengan perangkat lunak Kalibr.

### 5. Penentuan posisi objek
Setelah semua sudut pandang diproses, algoritma *k-means* mengelompokkan sel grid dengan jumlah kelompok sama dengan jumlah objek terdeteksi. Pusat objek dihitung dengan dua cara: pusat geometris kelompok (pusat *k-means*) atau pusat terbobot yang memakai bobot probabilitas sel.

### 6. Metrik evaluasi
Metrik yang dipakai adalah MAE, galat kuadrat rata-rata (*mean squared error*, MSE), akar galat kuadrat rata-rata (*root mean square error*, RMSE), dan galat persentase absolut rata-rata (*mean absolute percentage error*, MAPE). Pada meja uji ditambahkan galat jarak Euklides rata-rata.

## Eksperimen dan Hasil
Percobaan simulasi pertama tanpa derau menunjukkan bahwa kernel Gaussian dengan pusat terbobot paling menguntungkan menurut Gambar 11. Pada simulasi kedua, posisi dan ukuran kotak pembatas diberi derau Gaussian $N(0; 0{,}05)$ dan deteksi dihapus secara acak dengan peluang kegagalan 2%; kernel Gaussian dengan pusat terbobot kembali berkinerja lebih baik dan lebih tangguh dibanding kernel persegi. Nilai galat simulasi hanya ditampilkan pada Gambar 11 dan 12 dan tidak dapat dibaca dari teks ekstraksi; teks hanya menyatakan MAE di bawah 1 cm dan galat maksimum di bawah 10 mm pada simulasi.

Pada meja uji laboratorium, hasil kuantitatif dari Tabel II adalah sebagai berikut.

| Metrik | Persegi, terbobot | Persegi, geometris | Gaussian, terbobot | Gaussian, geometris |
|---|---|---|---|---|
| Galat Euklides rata-rata | 0,0205 m | 0,0206 m | 0,0222 m | 0,0204 m |
| MSE | $0{,}2187 \times 10^{-3}$ | $0{,}2197 \times 10^{-3}$ | $0{,}3399 \times 10^{-3}$ | $0{,}4960 \times 10^{-3}$ |
| RMSE | 0,0148 | 0,0148 | 0,0184 | 0,0223 |
| MAE | 0,0100 m | 0,0101 m | 0,0116 m | 0,0127 m |
| MAPE | 63,52% | 63,51% | 57,35% | 74,15% |

Berbeda dengan dugaan penulis, kernel Gaussian berkinerja lebih buruk daripada kernel persegi pada meja uji, dan pusat terbobot serta geometris memberi hasil yang hampir identik. Penulis menyatakan galat dapat mencapai sekitar 60 mm pada beberapa kasus. Penulis juga menyatakan sumber galat belum jelas, karena acuan posisi dari kinematika lengan tidak selalu tepat pada pusat tomat. Jarak pengamatan sekitar 0,5 m; penulis memperkirakan galat membaik pada jarak yang lebih dekat.

Pada pengujian oklusi parsial (Gambar 8j sampai 8l dan Gambar 14), algoritma dinyatakan mampu memperkirakan posisi tomat; penulis menyatakan algoritma tidak bekerja bila objek tertutup sepenuhnya karena detektor tidak mendeteksinya. Sudut pandang kolinear tidak memungkinkan estimasi posisi yang efektif, sedangkan sudut pandang yang saling tegak lurus memperbaiki perpotongan.

Sebagai pembanding kualitatif, penulis menjalankan MiDaS v3.1 DPT SWIN2 Large 384 pada citra Gambar 8g sampai 8i dengan kalibrasi regresi linear kasar. Peta kedalaman yang dihasilkan tampak datar, dan galat mencapai hingga 10 cm (Gambar 16b). Penulis sendiri menyatakan bahwa kesimpulan tentang MiDaS memerlukan percobaan kedalaman dan kalibrasi yang lebih lengkap.

Waktu komputasi pada prosesor Intel Core i7 dengan RAM 8 GB: sekitar 115 detik per pose untuk kernel Gaussian dan 99 detik per pose untuk kernel persegi tanpa paralelisasi. Pada bagian pembahasan lain, penulis menyebut sekitar satu menit per pose; kedua angka tersebut tertulis dalam makalah. Analisis hukum Amdahl memberi percepatan maksimum sekitar 17,5 untuk kernel Gaussian (Gambar 17).

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: algoritma tidak bergantung pada model objek dan hanya memerlukan detektor 2D, tidak memerlukan data pelatihan khusus untuk estimasi posisi, perilakunya lebih dapat diprediksi dan dijelaskan daripada pendekatan pembelajaran mendalam, mampu menangani oklusi parsial selama detektor dapat mendeteksi buah, dan sangat mudah diparalelkan karena sel grid bersifat independen.

Keterbatasan yang dinyatakan penulis: beban komputasi tinggi sehingga belum layak waktu-nyata; hasil berlaku pada kondisi laboratorium terkendali dengan buah tiruan, bukan lapangan nyata; galat pada meja uji sekitar 20 mm dan dapat mencapai sekitar 60 mm; acuan posisi dari kinematika lengan kurang pas pada pusat tomat; sudut pandang kolinear tidak efektif; algoritma tidak bekerja untuk objek yang tertutup penuh; dan kotak pembatas yang memuat area bukan objek mungkin lebih baik diganti masker segmentasi. Penulis mengusulkan pemilihan pose pengamatan yang adaptif, paralelisasi pada GPU atau FPGA, dan sensor tambahan seperti radar.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, hanya sepuluh tomat plastik dalam enam percobaan yang dievaluasi, dan tidak ada tanaman nyata, sehingga generalisasi tidak dapat dinilai. Kedua, MAPE pada meja uji berkisar 57,35% sampai 74,15%, nilai yang tinggi dibanding MAE dalam milimeter dan tidak dibahas rinci dalam teks. Ketiga, jumlah objek dianggap diketahui dari jumlah deteksi, sehingga deteksi palsu atau deteksi yang hilang pada satu sudut pandang tidak ditangani secara eksplisit dalam metode (hanya diuji pada simulasi dengan peluang kegagalan 2%). Keempat, perbandingan dengan MiDaS bersifat kualitatif dan memakai kalibrasi kasar, serta perbandingan dengan metode estimasi pose lain hanya merujuk angka dari dataset yang berbeda.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang sama diamati dari beberapa sudut pandang, tetapi bukan untuk pencacahan. Mekanismenya adalah fusi geometri multi-pandang: setiap sel grid 3D diproyeksikan ke setiap citra, probabilitas dari semua pandang dikalikan, lalu hasilnya dikelompokkan dengan *k-means*. Identitas lintas pandang diperoleh secara implisit melalui perpotongan geometri pada ruang 3D bersama, tanpa pencocokan tampilan atau pelacakan antarbingkai. Syarat mekanisme ini adalah pose kamera diketahui dari kinematika lengan, kalibrasi kamera tersedia, dan jumlah objek $k$ ditetapkan dari jumlah deteksi.

Hitungan per kelas tidak dilaporkan; hanya satu kelas (tomat) yang dipakai. Acuan yang dipakai adalah posisi 3D hasil pengukuran kinematika lengan pada tomat plastik, bukan panen, hitung manual lapangan, maupun anotasi citra. Gagasan yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pengelompokan hasil proyeksi deteksi ke ruang 3D bersama sehingga deteksi dari sisi berbeda yang menunjuk lokasi yang sama dianggap satu objek. Syarat pemindahannya adalah pose kamera yang diketahui per sisi pohon dan kalibrasi, dan hal itu tidak diuji pada buah besar, pohon tinggi, atau skala kebun. Makalah juga tidak menguji pengaruh deteksi ganda, deteksi palsu, atau jumlah objek yang tidak diketahui.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `magalhaes2024monovisual3dfilter`.

Ringkasan yang aman dikutip: Magalhães dkk. (2024) mengusulkan MonoVisual3DFilter, yaitu filter histogram Bayesian yang memperkirakan posisi 3D tomat dari kotak pembatas deteksi pada kamera monokular yang dipindahkan ke beberapa sudut pandang tetap. Pada simulasi, MAE dilaporkan di bawah 10 mm, dan pada meja uji laboratorium dengan tomat plastik dan jarak sekitar 0,5 m, MAE dilaporkan sekitar 20 mm. Pengujian terbatas pada sepuluh tomat plastik dalam kondisi laboratorium, dan komputasi sekitar 99 sampai 115 detik per pose tanpa paralelisasi.

Catatan verifikasi data: Angka MAE di bawah 10 mm (simulasi) dan di bawah 20 mm (meja uji) berasal dari abstrak dan bagian Pembahasan. Nilai per kernel pada meja uji berasal dari Tabel II. Nilai galat simulasi per kernel hanya ada pada Gambar 11 dan 12 sehingga tidak dapat diverifikasi dari teks. Jumlah sepuluh tomat dan enam puluh pengukuran tertulis di Seksi 2.5, sedangkan Seksi 3 menyebut enam estimasi per tomat; keterkaitan kedua angka itu tidak dijelaskan lebih lanjut. Waktu komputasi tertulis di Seksi 4 (sekitar satu menit per pose pada satu kalimat, 115 detik dan 99 detik per pose pada kalimat lain). Pada ekstraksi, Tabel I terpotong dan sebagian kolomnya tidak terbaca utuh, sehingga angka pada tabel itu hanya diambil dari uraian teks. Jumlah citra pelatihan YOLO v8 Tiny tidak dilaporkan pada teks yang dibaca. Teks yang dibaca berhenti pada bagian daftar pustaka pada baris ke-1.017 dari 1.091 baris, dan sisanya adalah referensi.
