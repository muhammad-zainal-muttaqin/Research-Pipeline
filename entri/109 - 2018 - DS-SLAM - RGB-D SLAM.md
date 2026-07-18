# 109 - DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yu2018dsslam` |
| Judul asli | DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments |
| Penulis | Chao Yu, Zuxin Liu, Xin-Jun Liu, Fugui Xie, Yi Yang, Qi Wei, Qiao Fei |
| Tahun | 2018 |
| Venue | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2018) |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1809.08379
- **Google Scholar:** https://scholar.google.com/scholar?q=DS-SLAM%3A%20A%20Semantic%20Visual%20SLAM%20towards%20Dynamic%20Environments
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=DS-SLAM%3A%20A%20Semantic%20Visual%20SLAM%20towards%20Dynamic%20Environments&sort=relevance
- **Kode sumber (GitHub):** https://github.com/ivipsourcecode/DS-SLAM

## Gambaran Umum

Makalah ini memperkenalkan DS-SLAM (*Dynamic Semantic SLAM*), sistem *Simultaneous Localization and Mapping* (SLAM — proses sebuah robot memperkirakan posisinya sendiri sekaligus membangun peta lingkungan secara bersamaan, hanya dari data sensor) yang dirancang untuk lingkungan dinamis, yaitu ruangan berisi objek bergerak seperti orang berjalan. DS-SLAM dibangun di atas ORB-SLAM2 (bab 107), sistem SLAM visual berbasis fitur ORB yang pada dasarnya mengasumsikan seluruh titik lingkungan bersifat statis. Kontribusi utamanya adalah menggabungkan jaringan segmentasi semantik (pelabelan tiap piksel citra dengan kategori objeknya) bernama SegNet dengan pemeriksaan konsistensi gerak berbasis geometri epipolar, sehingga titik fitur pada objek bergerak dapat dikenali dan dibuang sebelum dipakai mengestimasi pose (posisi dan orientasi kamera).

Pada rangkaian uji dinamis dari *dataset* TUM RGB-D, DS-SLAM menurunkan galat lintasan absolut (*Absolute Trajectory Error*, ATE — ukuran selisih antara lintasan kamera yang diestimasi dan lintasan sebenarnya) hingga dua tingkat besaran dibandingkan ORB-SLAM2 polos pada rangkaian dengan gerakan manusia yang dominan, dengan perbaikan RMSE (*root mean square error*, galat kuadrat rata-rata berakar) mencapai 97,91% pada rangkaian *fr3_walking_static*. Sistem berjalan pada rerata 59,4 milidetik per bingkai pada perangkat keras uji, dan juga menghasilkan peta oktomap (peta 3D berbasis pembagian ruang kubik berjenjang) yang diberi label semantik untuk kebutuhan navigasi tingkat lanjut.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hampir seluruh sistem SLAM visual generasi sebelum DS-SLAM, termasuk ORB-SLAM2, berasumsi lingkungan bersifat statis: setiap titik yang teramati di citra dianggap diam terhadap dunia nyata, dan hanya kamera yang bergerak. Asumsi ini memudahkan estimasi pose karena pergerakan titik fitur di layar semata-mata disebabkan gerak kamera, sehingga dapat dipakai menghitung transformasi antar-bingkai. Ketika objek dinamis — misalnya orang berjalan — memasuki bidang pandang, titik fitur pada objek tersebut bergerak karena dua sebab sekaligus (gerak kamera dan gerak objek), dan sistem yang tidak menyaringnya salah menafsirkan pergerakan itu sebagai gerak kamera. Pada kasus ekstrem yang disebutkan dalam makalah, orang yang bergerak dapat menutupi lebih dari separuh bidang citra, sehingga estimasi pose menyimpang jauh atau bahkan gagal total.

Upaya sebelumnya menangani masalah ini umumnya memakai salah satu dari dua pendekatan yang tidak saling melengkapi. Pendekatan berbasis aliran optik (*optical flow* — pola pergerakan piksel antar-bingkai berurutan) murni, seperti metode estimasi optimum dan penarikan sampel seragam, cukup cepat tetapi kurang akurat dan tetap mahal secara komputasi bila sampel diambil rapat pada citra besar. Pendekatan lain yang mengelompokkan citra berdasarkan lintasan titik (*point trajectory clustering*) memisahkan objek dinamis lebih akurat, tetapi tidak berjalan secara *real-time*. Sistem yang murni mengandalkan segmentasi semantik menghadapi masalah berbeda: jaringan tersebut hanya mengenali kategori objek yang telah dilatih, tanpa mengetahui apakah objek kategori itu benar-benar bergerak saat perekaman. DS-SLAM mengisi celah ini dengan menggabungkan informasi kategori objek (semantik) dan bukti gerak nyata (geometri), sehingga keputusan menyaring titik fitur mempertimbangkan keduanya, bukan salah satunya saja.

## Ide Utama

Gagasan inti DS-SLAM adalah memisahkan dua sumber informasi — label semantik dan bukti gerak geometris — menjadi dua proses paralel, lalu menggabungkan hasil keduanya untuk memutuskan objek mana yang benar-benar bergerak. Segmentasi semantik memberi tahu sistem *di mana* objek berisiko dinamis (dalam makalah ini difokuskan pada manusia) berada di citra, tanpa memberi tahu apakah objek itu sedang bergerak. Pemeriksaan konsistensi gerak, sebaliknya, memberi tahu titik mana yang pergerakannya di citra tidak konsisten dengan model gerak kamera murni, tanpa mengetahui objek apa yang memuatnya. DS-SLAM menggabungkan keduanya: jika sejumlah titik yang dinyatakan bergerak oleh pemeriksaan geometris jatuh di dalam kontur objek yang disegmentasi sebagai manusia, seluruh objek dinyatakan dinamis, dan seluruh titik fitur di dalam konturnya dibuang sebelum estimasi pose.

Karena segmentasi semantik dengan jaringan saraf jauh lebih lambat daripada ekstraksi fitur ORB, kedua proses dijalankan pada utas (*thread* — alur eksekusi program yang berjalan bersamaan) terpisah, sehingga waktu tunggu segmentasi dapat diisi oleh perhitungan konsistensi gerak yang lebih ringan — jawaban langsung atas keterbatasan pada bagian latar belakang: akurasi metode berbasis lintasan titik didekati tanpa mengorbankan kecepatan aliran optik murni.

## Cara Kerja Langkah demi Langkah

Sistem DS-SLAM menjalankan lima utas secara paralel: *tracking* (pelacakan pose), segmentasi semantik, *local mapping* (pemetaan lokal), *loop closing* (deteksi dan koreksi lintasan yang kembali ke tempat semula), dan pembuatan peta semantik padat. Dua utas terakhir — *local mapping* dan *loop closing* — dipertahankan identik dengan ORB-SLAM2; kontribusi baru DS-SLAM terkonsentrasi pada tiga utas lainnya.

Alur data dari citra masukan hingga estimasi pose yang telah disaring dapat digambarkan sebagai berikut:

```
citra RGB+D per bingkai
   │
   ├──> [utas Tracking]
   │        1. ekstraksi fitur ORB
   │        2. cek konsistensi gerak kasar (epipolar)
   │        3. tunggu label dari utas Segmentasi
   │        4. gabungkan label + hasil gerak -> buang outlier
   │        5. estimasi pose dari fitur yang tersisa
   │
   └──> [utas Segmentasi Semantik]
            SegNet -> peta label per piksel (20 kelas)
                       (dikirim ke utas Tracking)

pose + keyframe tersaring
   │
   ├──> [Local Mapping]  -> bundle adjustment
   ├──> [Loop Closing]   -> deteksi & koreksi loop
   └──> [Peta Oktomap Semantik] -> voxel berlabel, log-odds
```

### Segmentasi Semantik dengan SegNet

DS-SLAM memakai SegNet, jaringan konvolusi berarsitektur *encoder-decoder* (penyandi-penyahsandi) untuk segmentasi semantik, dijalankan di atas kerangka kerja Caffe dan dilatih pada *dataset* PASCAL VOC sehingga mengenali 20 kelas objek. Karena manusia paling sering muncul dan paling mengganggu pada skenario aplikasi nyata, makalah membatasi asumsi kerja: titik fitur pada kelas "orang" diperlakukan sebagai kandidat *outlier* (titik pencilan yang harus dibuang), meskipun penulis menyatakan metodenya berlaku secara prinsip untuk kelas objek dinamis apa pun yang dikenali jaringan.

### Pemeriksaan Konsistensi Gerak

Proses ini menentukan apakah sebuah titik fitur bergerak secara nyata, tanpa memakai segmentasi gerak penuh yang mahal secara komputasi. Langkahnya empat tahap. Pertama, piramida aliran optik dihitung untuk mencari titik yang berpadanan antara bingkai sebelumnya dan bingkai saat ini. Kedua, pasangan titik yang terlalu dekat dengan tepi citra atau memiliki selisih intensitas besar pada blok 3×3 piksel di sekitarnya dibuang karena dianggap tidak dapat diandalkan. Ketiga, matriks fundamental (matriks yang memetakan sebuah titik di satu bingkai ke garis epipolar yang bersesuaian di bingkai lain) dihitung memakai RANSAC (*Random Sample Consensus* — metode estimasi parameter yang tahan terhadap data pencilan dengan memilih model yang didukung jumlah data konsisten terbanyak). Keempat, jarak dari setiap titik padanan ke garis epipolarnya dihitung; bila jarak ini melampaui ambang tertentu, titik dinyatakan bergerak, karena posisinya tidak dapat dijelaskan oleh gerak kamera murni. Secara matematis, bila P₁ dan P₂ adalah koordinat homogen dua titik padanan, garis epipolar diperoleh dari I₁ = F·P₁ dengan F matriks fundamental, dan jarak D dari P₂ ke garis tersebut dihitung sebagai |P₂ᵀ·F·P₁| dibagi akar jumlah kuadrat dua komponen pertama vektor garis; titik dengan D melebihi ambang preset ε dimasukkan ke himpunan titik dinamis.

### Penyaringan Outlier Gabungan

Hasil dua proses di atas digabungkan menjadi basis pengetahuan dua tingkat: label per objek (bergerak atau tidak) dan label per titik (bergerak atau tidak). Jika sejumlah titik dinamis dari pemeriksaan konsistensi gerak jatuh di dalam kontur objek manusia hasil segmentasi, seluruh objek dinyatakan bergerak, dan seluruh titik fitur di konturnya — bukan hanya titik yang lolos uji gerak — dibuang sebelum pencocokan fitur untuk estimasi pose. Penggabungan ini menutupi kelemahan masing-masing metode: kontur objek dari segmentasi semantik mengatasi kesulitan pemeriksaan gerak murni mengekstraksi batas penuh objek berdeformasi kompleks (misalnya anggota tubuh manusia yang bergerak tidak seragam), sementara pemeriksaan gerak mengoreksi galat segmentasi ketika objek statis salah dikenali sebagai kelas berisiko dinamis.

### Peta Oktomap Semantik

Utas kelima membangun peta 3D padat berbasis oktomap (representasi ruang yang membagi volume secara rekursif menjadi delapan subvolume kubik, sehingga hemat memori dan mudah diperbarui) dari keyframe, citra kedalaman, dan hasil segmentasi. Setiap voxel (elemen volume terkecil pada peta 3D) diberi warna yang merepresentasikan label semantiknya, misalnya merah untuk sofa dan biru untuk monitor. Untuk mengatasi segmentasi yang kadang tidak sempurna, DS-SLAM memakai skor log-odds (transformasi logit dari probabilitas okupansi voxel) yang diakumulasi dari observasi berulang: sebuah voxel dianggap terisi stabil hanya bila probabilitas okupansinya, setelah dikonversi balik dari skor log-odds, melewati ambang tertentu — menjaga peta tidak tercemar voxel sesaat dari kesalahan segmentasi tunggal atau objek dinamis yang sempat terekam.

## Eksperimen dan Hasil

Evaluasi kuantitatif dilakukan pada rangkaian dinamis *dataset* TUM RGB-D, tolok ukur standar SLAM RGB-D yang menyediakan lintasan kebenaran dari sistem penangkap gerak eksternal. Rangkaian *fr3_walking_xyz*, *fr3_walking_static*, *fr3_walking_rpy*, dan *fr3_walking_half* dikategorikan sebagai dinamika tinggi karena orang berjalan bolak-balik dalam bidang pandang, sedangkan *fr3_sitting_static* dikategorikan dinamika rendah karena subjek hanya bergerak sedikit sambil duduk. Metrik yang dipakai adalah ATE (galat lintasan absolut, mengukur konsistensi global lintasan) dan RPE (*Relative Pose Error*, mengukur laju penyimpangan translasi dan rotasi antar-pasangan pose berdekatan). Seluruh pengujian dijalankan pada komputer dengan prosesor Intel i7, GPU Nvidia Quadro P4000, dan RAM 32 GB.

Pada metrik ATE, DS-SLAM menurunkan RMSE dari 0,7521 meter (ORB-SLAM2) menjadi 0,0247 meter pada *fr3_walking_xyz* (perbaikan 96,71%), dan dari 0,3900 meter menjadi 0,0081 meter pada *fr3_walking_static*, perbaikan tertinggi sebesar 97,91%. Pada *fr3_walking_half*, RMSE turun dari 0,4863 menjadi 0,0303 meter (93,76%). Perbaikan paling kecil terjadi pada *fr3_walking_rpy* (48,97%), rangkaian dengan rotasi kamera murni sehingga pemisahan gerak objek dari gerak kamera secara geometris lebih sulit. Pada rangkaian dinamika rendah *fr3_sitting_static*, perbaikan RMSE ATE hanya 25,94%, karena ORB-SLAM2 tanpa modifikasi sudah menangani gerakan kecil itu dengan baik sehingga ruang perbaikan tersisa terbatas. Pola serupa — besar pada dinamika tinggi, kecil pada dinamika rendah — juga konsisten pada metrik RPE translasi dan rotasi pada tabel terpisah di naskah asli.

Dari sisi kecepatan, tabel waktu proses menunjukkan ekstraksi fitur ORB memakan rerata 9,375 milidetik dan pemeriksaan konsistensi gerak 29,509 milidetik, keduanya di utas *tracking*; segmentasi SegNet memakan 37,573 milidetik di utas terpisah. Rerata waktu pemrosesan utas utama per bingkai — mencakup segmentasi, estimasi odometri visual, optimasi graf pose, dan pembuatan peta oktomap padat — adalah 59,4 milidetik, setara sekitar 16,8 bingkai per detik bila dihitung sebagai kebalikan langsung angka tersebut. Kecepatan ini di bawah laju video standar (30 FPS), tetapi menurut penulis tetap lebih memadai dibandingkan metode penyaring objek dinamis nonreal-time sebelumnya. Pengujian tambahan pada robot fisik TurtleBot2 dengan kamera Kinect V2 beresolusi 960×540 mengonfirmasi secara kualitatif bahwa titik fitur pada orang bergerak berhasil disingkirkan dan peta oktomap semantik tetap stabil meski ada orang lalu-lalang.

## Kelebihan dan Keterbatasan

Kelebihan DS-SLAM terletak pada kombinasi dua sumber informasi yang saling menutupi kelemahan: segmentasi semantik menyediakan kontur objek utuh yang sulit diperoleh pemeriksaan gerak murni, sedangkan pemeriksaan gerak mengoreksi kesalahan klasifikasi semantik pada objek yang sebenarnya diam. Desain lima utas paralel memungkinkan segmentasi yang lambat berjalan tanpa memblokir jalur pelacakan pose sepenuhnya, dan peta oktomap semantik dengan skema log-odds memberi keluaran yang langsung berguna untuk navigasi robot, bukan sekadar awan titik geometris.

Dari sisi rekayasa, sistem ini tetap bergantung pada kualitas segmentasi SegNet, yang dilatih hanya pada 20 kelas PASCAL VOC — objek dinamis di luar kelas tersebut, misalnya hewan peliharaan atau kendaraan kecil di dalam ruangan, tidak akan tersaring. Secara konseptual, strategi "buang seluruh kontur objek bila sebagian titik dinyatakan bergerak" berisiko membuang informasi berguna ketika hanya sebagian kecil objek besar yang benar-benar bergerak. Penulis sendiri mengakui keterbatasan cakupan kelas objek yang dikenali dan kebutuhan membangun ulang peta oktomap setiap kali penutupan loop terdeteksi, karena struktur oktomap tidak dirancang untuk koreksi retroaktif yang murah. Kecepatan 59,4 milidetik per bingkai, meski lebih cepat dari pendekatan nonreal-time sebelumnya, tetap di bawah laju video kamera standar, sehingga pada gerak kamera yang sangat cepat performa pelacakan berisiko menurun.

## Kaitan dengan Bab Lain

DS-SLAM secara eksplisit dibangun sebagai lapisan tambahan di atas ORB-SLAM2 (bab [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)), mewarisi seluruh mekanisme pelacakan fitur ORB, pemetaan lokal, dan penutupan loop dari sistem tersebut tanpa perubahan, sementara menambahkan lapisan penyaringan dinamis dan peta semantik. Pendekatannya berbeda arah dengan DynaSLAM (bab [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)), yang diterbitkan pada tahun yang sama dan juga menyasar lingkungan dinamis; perbandingan langsung strategi penyaringan objek dinamis antara keduanya relevan dibaca berdampingan. Gagasan menggabungkan deteksi/segmentasi berbasis jaringan saraf dengan modul geometri SLAM ini kemudian diperluas pada bab [110 - 2022 - CFP-SLAM - RGB-D SLAM](./110%20-%202022%20-%20CFP-SLAM%20-%20RGB-D%20SLAM.md), dan dibandingkan secara empiris dengan pendekatan berbasis YOLO pada bab [111 - 2019 - Visual SLAM YOLO vs Mask R-CNN (Soares dkk.) - RGB-D SLAM](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md).

## Poin untuk Sitasi

Kutip dengan kunci `yu2018dsslam`. Ringkasan yang aman dikutip: "DS-SLAM menggabungkan segmentasi semantik SegNet dengan pemeriksaan konsistensi gerak berbasis geometri epipolar di atas ORB-SLAM2, menurunkan RMSE ATE hingga 97,91% pada rangkaian TUM RGB-D berdinamika tinggi dan menghasilkan peta oktomap semantik berbasis skor log-odds." Angka RMSE ATE (0,7521→0,0247 m; 0,3900→0,0081 m), persentase perbaikan (96,71%; 97,91%; 93,76%; 48,97%; 25,94%), waktu proses per modul (9,375 ms; 29,509 ms; 37,573 ms), rerata waktu per bingkai (59,4 ms), dan spesifikasi perangkat keras uji (Intel i7, Quadro P4000, RAM 32 GB) berasal langsung dari tabel dan teks naskah arXiv 1809.08379 dan telah diperiksa terhadap sumber tersebut. Angka setara 16,8 FPS adalah hasil hitung penulis bab ini dari 59,4 ms per bingkai, bukan angka yang dinyatakan eksplisit di naskah, sehingga sebaiknya diverifikasi ulang bila dikutip sebagai klaim FPS langsung.
