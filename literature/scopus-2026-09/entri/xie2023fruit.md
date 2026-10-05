# Fruit Distribution Acquisition with Multi-Vision for Multi-Arm Harvesting Robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xie2023fruit` |
| Judul asli | Fruit Distribution Acquisition with Multi-Vision for Multi-Arm Harvesting Robots |
| Penulis | Xie, Feng; Sun, Na; Li, Jiaheng; Feng, Qingchun; Li, Tao |
| Tahun | 2023 |
| Venue | 2023 8th International Conference on Control Robotics and Cybernetics CRC 2023 |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [xie2023fruit.pdf](../pdf/xie2023fruit.pdf)
- DOI resmi: https://doi.org/10.1109/crc60659.2023.10488608

## Gambaran Umum
Makalah prosiding ini membahas lokalisasi buah apel pada robot pemanen berlengan banyak (*multi-arm harvesting robot*) yang memiliki beberapa unit penglihatan stereo dengan bidang pandang yang saling tumpang tindih. Masalah yang disasar adalah buah yang sama muncul pada beberapa kamera dengan estimasi pusat massa (*centroid*) yang berbeda, sehingga sulit dipastikan apakah dua posisi berasal dari buah yang sama. Akibatnya robot dapat memetik buah yang sama berulang kali.

Metode yang diusulkan terdiri atas tiga komponen: kalibrasi ekstrinsik gabungan empat kamera RGBD terhadap satu kamera tetap, jaringan multitugas untuk deteksi dan segmentasi buah dengan lokalisasi berbasis kerucut pandang (*frustum*) dan klaster DBSCAN, serta penyaringan duplikat dengan memproyeksikan pusat buah ke kamera bersebelahan dan membandingkan jaraknya dengan ambang $\lambda$. Penulis menyebut judul metode ini sebagai pencocokan awan titik permukaan buah, tetapi uraian langkah fusi pada makalah bertumpu pada proyeksi posisi dan ambang jarak.

Hasil utama yang dilaporkan: galat posisi pusat buah rata-rata 9,2 mm dan galat diameter rata-rata 8,6 mm, dibandingkan 10,2 mm dan 9,7 mm pada metode pembanding dari makalah sebelumnya penulis. Pada kesimpulan, penulis menyatakan probabilitas deteksi positif palsu dan target ganda berkurang sebesar 20%. Angka per tabel tidak dapat diverifikasi karena tabel hasil tidak terbaca pada teks ekstraksi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Robot pemanen berlengan banyak memasang satu unit penglihatan pada tiap lengan. Karena bidang pandang kamera-kamera itu tumpang tindih, buah yang sama sering tampak pada lebih dari satu kamera. Secara ideal, setelah koordinat ditransformasikan dengan matriks parameter ekstrinsik antarkamera, estimasi posisi buah yang sama dari kamera berbeda akan berimpit sehingga duplikat dapat dibuang.

Penulis menyebut dua penyebab ketidakberimpitan. Pertama, posisi pemasangan kamera stereo berubah akibat perawatan, dan pose antarkamera bergeser perlahan seiring gerak lengan. Kedua, algoritma lokalisasi visual tidak sempurna sehingga estimasi posisi menyimpang pada tingkat yang bervariasi. Kedua faktor ini menyebabkan target buah ganda pada persepsi kolaboratif dan menurunkan efisiensi robot.

## Ide Utama
Gagasan utamanya adalah memperbaiki dua sumber galat sekaligus sebelum memutuskan identitas buah: (1) menyelaraskan kerangka koordinat semua kamera melalui kalibrasi gabungan, dan (2) meningkatkan akurasi lokalisasi buah pada tiap kamera dengan memakai kotak pembatas lengkap untuk menentukan sumbu kerucut pandang dan masker permukaan untuk menentukan titik acuan. Setelah itu, identitas buah ditentukan dengan aturan jarak sederhana pada citra kamera bersebelahan.

## Cara Kerja Langkah demi Langkah

### 1. Platform dan akuisisi data
Robot terdiri atas platform beroda, empat lengan Cartesian 3 derajat kebebasan (penggerak hibrida elektrik-pneumatik), penjepit 2 derajat kebebasan berjari tiga, sistem penglihatan, sistem pengangkut buah, sistem penerangan, dan modul kontrol pusat. Sistem penglihatan memuat empat kamera RGBD yang dipasang di bagian atas modul linier ketiga. Citra dikirim ke modul komputasi tepi (*edge computing*) untuk deteksi dan segmentasi.

Data pelatihan jaringan berasal dari dua sumber: dataset terbuka MinneApple (1000 citra dengan lebih dari 41.000 instans apel berlabel) dan dataset yang dikumpulkan sendiri di dua kebun standar modern di Distrik Haidian dan Distrik Changping, Beijing, dengan kamera RealSense D435i (1000 citra dengan lebih dari 12 ribu instans apel berlabel, dengan kelas oklusi tanpa oklusi, oklusi daun, oklusi cabang, dan oklusi buah). Pembagian data latih dan validasi 4:1. Kultivar apel tidak dilaporkan.

### 2. Kalibrasi ekstrinsik multikamera
Satu kamera tambahan $C_{fixed}$ dipasang pada posisi tetap terhadap kerangka dasar robot, dan matriks ekstrinsiknya dianggap diketahui. Keempat kamera $C_i$ dihubungkan melalui matriks transformasi homogen $T^{C_i}_{C_{i+1}} \in SE(3)$ yang dikalibrasi memakai papan kalibrasi (papan catur) yang tampak pada bidang pandang bersama minimal dua kamera. Parameter dioptimalkan dengan meminimalkan galat reproyeksi menggunakan metode Levenberg-Marquardt. Penulis menyatakan bahwa mengalibrasi semua kamera relatif terhadap kamera tetap merupakan cara tercepat.

### 3. Deteksi, segmentasi, dan lokalisasi pada satu kamera
Jaringan konvolusional dalam multitugas dari makalah sebelumnya penulis dipakai. Jaringan itu dibangun di atas YOLOv4 dengan enkoder bersama dan dua dekoder: kepala deteksi yang memprediksi tipe oklusi dan kotak pembatas lengkap, serta kepala segmentasi instans yang menghasilkan masker piksel bagian buah yang terlihat. Pelatihan dilakukan pada stasiun kerja dengan GPU NVIDIA GeForce RTX 3070 (8 GB) dan augmentasi berupa distorsi fotometrik, pencerminan, pemotongan acak, pembalikan acak, dan ekspansi acak.

Lokalisasi memakai kotak pembatas lengkap dan parameter intrinsik kamera untuk membentuk kerucut pandang tiga dimensi; sumbu simetri kerucut dianggap garis yang melewati pusat massa buah. Masker segmentasi dan peta kedalaman yang selaras menghasilkan awan titik permukaan buah. DBSCAN diterapkan untuk menyaring titik derau di dalam kerucut (misalnya akibat oklusi). Radius buah kemudian ditentukan dari parameter intrinsik dan kotak pembatas, lalu digabung dengan garis pusat untuk menghitung posisi pusat massa.

### 4. Fusi informasi multipandang dan penghapusan duplikat
Prosedur fusi ke daftar buah global memiliki enam langkah.

1. Objek yang tidak berada pada wilayah tumpang tindih dipindahkan langsung ke daftar buah global.
2. Untuk objek pada wilayah tumpang tindih kamera ke-$i$, pusat kotak deteksi diproyeksikan ke citra kamera bersebelahan memakai matriks intrinsik dan ekstrinsik. Bila jarak Euklides antara posisi proyeksi dan pusat objek pada kamera tetangga kurang dari ambang $\lambda$, kedua objek dianggap buah yang sama, dikeluarkan dari daftar kedua kamera, dan dimasukkan ke daftar global. Bila jarak melebihi ambang, objek dianggap berbeda.
3. Bila objek terletak pada bidang pandang tumpang tindih keempat kamera, prosedur diulang untuk kamera lain. Objek yang muncul pada kamera lain lebih dari satu kali dihapus dari daftar masing-masing dan ditambahkan ke daftar global; objek yang tidak muncul pada kamera lain digolongkan sebagai buah mencurigakan (*suspicious fruit*) dan tetap pada daftar asal.
4. Proses diulang untuk kamera lain sampai semua objek pada wilayah tumpang tindih diperiksa keunikannya.
5. Daftar buah global dikirim ke perencana tugas.
6. Setelah semua buah pada daftar dipetik, lengan kembali ke posisi pengamatan dan mengulang lima langkah di atas.

## Eksperimen dan Hasil
Eksperimen lokalisasi dilakukan dengan tiga kelompok citra RGBD pada jarak sekitar 500 mm, 800 mm, dan 1000 mm dari permukaan kerja buah. Pembanding adalah metode lokalisasi berbasis kotak pembatas yang lazim dipakai (disingkat "bbx. mtd."). Eksperimen fusi dilakukan di kebun nyata pada sepuluh titik kerja dengan jumlah dan sebaran apel yang berbeda; citra RGBD diambil dari empat kamera pada tiap titik. Acuan posisi buah pada eksperimen fusi adalah pengukuran manual berbantuan radar laser (disebut *laser radar* pada makalah).

| Ukuran | Reduksi galat pada kelompok 1 (median, rerata, simpangan baku) | Reduksi galat pada tiga kelompok (median, rerata, simpangan baku) |
|---|---|---|
| Posisi pusat massa buah | 67%, 50%, 10% | 59%, 43%, 9% |
| Diameter buah | 75%, 80%, 96% | 70%, 70%, 78% |

Angka reduksi di atas dibandingkan dengan metode kotak pembatas. Galat rata-rata posisi pusat massa dan diameter adalah 9,2 mm dan 8,6 mm, dibandingkan 10,2 mm dan 9,7 mm pada metode di rujukan [14] makalah. Pada kesimpulan, penulis menyatakan probabilitas positif palsu dan penghapusan target ganda berkurang 20%; dasar perhitungan angka 20% ini tidak dijelaskan pada teks hasil.

Secara kualitatif, Gambar 7 menunjukkan pasangan titik proyeksi dan titik pusat yang berdekatan pada bidang pandang tumpang tindih kamera 3 dan kamera 4. Gambar 8 menunjukkan bola posisi hasil metode (merah) sejalan dengan bola posisi hasil pengukuran manual (hijau) pada titik kerja ketiga. Gambar 9 dan 10 memperlihatkan kegagalan: deteksi tidak akurat, positif palsu, dan oklusi menyebabkan perbedaan citra yang besar pada bidang tumpang tindih sehingga target yang sama dinilai berbeda, dan kemudian muncul deteksi terlewat. Penyesuaian ambang jarak $\lambda$ dapat mengurangi deteksi terlewat, tetapi berisiko menganggap dua buah berdekatan yang berbeda sebagai buah yang sama.

## Kelebihan dan Keterbatasan
Kelebihan: metode memisahkan masalah identitas lintas kamera menjadi kalibrasi ekstrinsik, lokalisasi yang lebih akurat, dan aturan jarak yang sederhana sehingga murah dihitung. Kalibrasi gabungan menggunakan satu kamera tetap sebagai acuan. Evaluasi dilakukan pada kebun nyata, dan kegagalan ditampilkan secara terbuka.

Keterbatasan yang dinyatakan penulis: kesalahan deteksi, positif palsu, dan oklusi dapat menyebabkan penilaian buah yang sama sebagai berbeda, dan pelonggaran ambang $\lambda$ berisiko menyatukan buah berbeda yang berdekatan.

Menurut pembacaan ringkasan ini, evaluasi pencocokan identitas hanya disajikan sebagai ilustrasi pada sepuluh titik kerja, tanpa angka presisi atau *recall* pencocokan per titik. Angka reduksi 20% tidak disertai tabel. Nilai ambang $\lambda$ tidak dilaporkan. Ujicoba hanya pada apel dengan kamera yang dipasang kaku pada lengan robot, tanpa pergerakan kamera mengelilingi tajuk.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali, yaitu pada beberapa kamera dengan bidang pandang tumpang tindih. Mekanismenya adalah pencocokan multipandang berbasis geometri: pusat deteksi diproyeksikan antarkamera memakai parameter intrinsik dan ekstrinsik hasil kalibrasi, lalu pasangan dengan jarak di bawah ambang dianggap satu buah. Hitungan per kelas tidak dilaporkan; deteksi memakai kelas apel dengan label tipe oklusi. Acuan evaluasi adalah posisi buah dari pengukuran manual berbantuan radar laser, bukan hasil panen atau hitung manual total buah.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menyelaraskan kerangka kamera terlebih dahulu, lalu memutuskan identitas dengan ambang jarak pada proyeksi. Keterbatasannya: pendekatan ini mengandaikan kamera berposisi tetap dan bidang pandang tumpang tindih yang jelas, sedangkan pada pohon sawit multi-sisi sisi-sisi pohon hampir tidak tumpang tindih sehingga aturan jarak perlu diganti dengan penanda lain.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `xie2023fruit`.

Xie dkk. (2023) mengusulkan perolehan sebaran buah apel dari empat kamera RGBD pada robot pemanen berlengan banyak: kalibrasi ekstrinsik gabungan, jaringan multitugas berbasis YOLOv4 untuk deteksi dan segmentasi dengan lokalisasi kerucut pandang dan DBSCAN, serta penghapusan duplikat melalui proyeksi pusat deteksi ke kamera bersebelahan dengan ambang jarak. Galat rata-rata posisi pusat dan diameter buah dilaporkan 9,2 mm dan 8,6 mm, dan penulis menyatakan penurunan probabilitas positif palsu dan target ganda sebesar 20%.

Catatan verifikasi data: Angka 9,2 mm, 8,6 mm, 10,2 mm, dan 9,7 mm tertulis pada Bagian III-C. Angka reduksi galat (67%, 50%, 10%; 59%, 43%, 9%; 75%, 80%, 96%; 70%, 70%, 78%) tertulis pada Bagian III-B, sedangkan tabel hasil asli ("Table 2.3") tidak terbawa pada teks ekstraksi. Angka 20% tertulis pada Bagian IV tanpa penjelasan dasar perhitungannya. Jumlah apel per titik kerja, nilai ambang $\lambda$, dan kultivar tidak dilaporkan. Teks ekstraksi memuat sebagian rumus yang terpecah, tetapi isi utama terbaca.
