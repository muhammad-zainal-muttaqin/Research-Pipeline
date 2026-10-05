# Reliability of a commercial platform for estimating flower cluster and fruit number, yield, tree geometry and light interception in apple trees under different rootstocks and row orientations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `scalisi2021reliability` |
| Judul asli | Reliability of a commercial platform for estimating flower cluster and fruit number, yield, tree geometry and light interception in apple trees under different rootstocks and row orientations |
| Penulis | Scalisi, Alessio; McClymont, Lexie; Underwood, James; Morton, Peter; Scheding, Steve; Goodwin, Ian |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [scalisi2021reliability.pdf](../pdf/scalisi2021reliability.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106519

## Gambaran Umum

Makalah ini mengkalibrasi dan memvalidasi platform bergerak komersial, Cartographer (Green Atlas), untuk memprediksi jumlah kluster bunga, jumlah buah, hasil panen, dan geometri pohon pada apel 'ANABP-01' (dipasarkan sebagai Bravo). Platform ini dipasang pada kendaraan segala medan listrik (*all-terrain vehicle*, ATV) dan menggabungkan kamera RGB, LiDAR, dan GPS. Jaringan saraf konvolusional (*convolutional neural network*, CNN) mendeteksi bunga dan buah per citra, sedangkan LiDAR mengukur tinggi pohon, luas kanopi, dan kerapatan kanopi. Selain itu, penulis memodelkan hubungan geometri pohon dengan intersepsi cahaya dan menguji pengaruh batang bawah (*rootstock*) serta orientasi baris terhadap produktivitas.

Percobaan dilakukan di kebun Sundial, Tatura SmartFarm, Victoria, Australia, pada 2020-2021: kebun melingkar kerapatan tinggi (sekitar 2857 pohon/ha, sekitar 1,3 ha) dengan 60 petak percobaan, tiap petak berisi sebelas pohon 'ANABP-01' dan satu pohon penyerbuk 'Granny Smith'. Pohon berada pada daun ketiga, dengan tiga batang bawah (Bud.9, M9 (T337), M26) dan empat orientasi baris.

Hasil utama: galat kalibrasi kluster bunga sekitar 5 kluster per citra (RMSE). Setelah validasi terhadap mesin sortir komersial pada saat panen, galat jumlah buah adalah RMSE 5 buah/pohon (rc = 0,88) dan galat hasil panen RMSE 1 kg/pohon (rc = 0,89). Galat tingkat blok untuk jumlah buah dan hasil panen masing-masing 4,6% dan 1,2%. Makalah ini bukan metode pelacakan atau pencocokan buah lintas pandang; penghitungan dilakukan per citra, lalu diskalakan dengan faktor kalibrasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hortikultura bergerak ke arah mekanisasi, otomasi, dan penginderaan nondestruktif. Penelitian terdahulu umumnya mendeteksi buah apel dengan segmentasi citra dan CNN pada citra RGB atau RGB-D untuk menghitung buah, memperkirakan hasil panen, atau memandu mesin panen. LiDAR dipakai untuk menentukan arsitektur kanopi (tinggi pohon, ukuran dan kerapatan kanopi), dan awan titik LiDAR dipakai untuk memodelkan intersepsi cahaya. Penulis mengutip Anderson dkk. (2021) bahwa galat estimasi hasil panen yang umumnya diterima berada pada kisaran 5-10%, dengan nilai berbeda antarindustri buah.

Cartographer sudah tersedia secara komersial untuk memetakan sebaran jumlah buah apel dan parameter geometri pohon, tetapi keandalannya perlu dikalibrasi terhadap pengukuran manual yang melelahkan. Tujuan penelitian ada empat: (i) menetapkan hubungan antara ukuran manual dan hasil pindai untuk kluster bunga, jumlah buah, hasil panen, dan tinggi pohon; (ii) menetapkan hubungan parameter geometri LiDAR (luas kanopi, kerapatan kanopi, dan luas daun penampang kanopi, *canopy cross-sectional leaf area*, CSLA) dengan intersepsi cahaya; (iii) menentukan pengaruh intersepsi cahaya terhadap kerapatan bunga dan buah serta hasil panen; (iv) menentukan pengaruh batang bawah dan orientasi baris.

## Ide Utama

Gagasan utamanya adalah memperlakukan keluaran deteksi platform sebagai pencacah relatif per citra, lalu mengubahnya menjadi jumlah absolut melalui faktor kalibrasi. Faktor kalibrasi adalah kebalikan kemiringan regresi linear (intersep ditetapkan nol) antara deteksi per citra dan hitungan manual. Kalibrasi dilakukan terpisah untuk setiap batang bawah dan tanggal pindai karena kelompok batang bawah membentuk gugus data yang berbeda. Hasil panen diperoleh dengan mengalikan jumlah buah terkalibrasi dengan bobot buah rerata per batang bawah, dengan bobot dihitung dari diameter ekuatorial buah.

Untuk geometri pohon, CSLA didefinisikan sebagai hasil kali luas kanopi dan kerapatan kanopi. Luas kanopi (m2) adalah luas poligon di sekeliling titik LiDAR pada transek yang dipindai tanpa batang pohon. Kerapatan kanopi adalah rasio berkas cahaya LiDAR yang memantul terhadap seluruh berkas yang dipancarkan dalam area kanopi. Intersepsi cahaya diukur sebagai luas bayangan efektif (*effective area of shade*, EAS).

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Pemindaian memakai Cartographer pada kecepatan sekitar 7-8 km/jam untuk pindai kalibrasi dan 20 km/jam untuk pemetaan blok kebun. Citra dicatat dengan laju 5 citra per detik. Kedua sisi setiap petak dipindai. Antarmuka ponsel dipakai untuk mencatat metadata. Data tingkat petak diekstrak dengan memotong titik hasil pindai dengan poligon petak dari QGIS (v.3.10), dengan presisi geografis yang ditingkatkan oleh posisi RTK (*real-time kinematic*) dan diperiksa silang pada posisi tiang penanda petak pada citra RGB.

Pindai pendek menghasilkan hitungan kluster bunga dan buah per citra untuk kalibrasi. Pindai kontinu seluruh blok menghasilkan prediksi yang belum terkalibrasi dan data geometri pohon (tanpa kalibrasi tambahan), lalu hitungan bunga dan buah diproses ulang dengan faktor kalibrasi.

### 2. Kalibrasi kluster bunga

Pindai pendek dilakukan pada enam petak saat 50% mekar (1 Oktober 2020). Pada hari yang sama, kluster pada semua pohon di petak itu dihitung manual (tahap fenologi *pink balloon* sampai *open cluster*). Hubungan hitungan manual per pohon dan deteksi per citra dicocokkan dengan regresi linear berintersep nol. Hitungan bunga tidak divalidasi karena tidak ada data validasi independen.

### 3. Kalibrasi dan validasi jumlah buah serta hasil panen

Jumlah buah ditentukan pada dua belas petak pada tiga tahap ukuran buah, yaitu 44, 102, dan 154 hari setelah mekar penuh (*days after full bloom*, DAFB), dengan hitungan manual pada hari pindai yang sama. Validasi dilakukan terhadap hitungan per petak dari mesin sortir komersial (Compac InVision 9000) saat panen pada 36 petak. Diameter buah diukur dengan jangka sorong pada 108 buah (36 per batang bawah) seminggu sebelum panen; hubungan bobot dan diameter buah mengikuti FW = 0,0003 x FD^3,04 (galat baku estimasi 21 g, n = 559 menurut keterangan Gambar 2).

### 4. Tinggi pohon

Pindai diam dilakukan pada pohon tengah dari 36 petak pada 45, 101, dan 154 DAFB agar sesuai dengan pohon yang diukur manual dengan tongkat ukur. Galat tinggi tanah yang terdeteksi dikurangkan dari prediksi.

### 5. Hubungan geometri pohon dan intersepsi cahaya

EAS adalah rerata fraksi intersepsi radiasi aktif fotosintesis (*photosynthetically active radiation*, PAR) pada kotak penanaman (jarak pohon x jarak baris), diukur pada tiga waktu (tengah hari surya, dan 3,5 jam sebelum dan sesudahnya) pada hari cerah dengan kereta cahaya berisi 24 sensor PAR dengan jarak 0,125 m pada batang 3 m. Pengukuran dilakukan pada dua tanggal (44 dan 102 DAFB) pada 60 petak. Hubungan luas kanopi, kerapatan kanopi, dan CSLA terhadap EAS dimodelkan dengan regresi linear pada median per petak.

### 6. Analisis statistik

Galat kalibrasi dan validasi dinyatakan dengan RMSE regresi linear. Ketangguhan validasi dinilai dengan koefisien korelasi konkordansi Lin (rc). Pengaruh intersepsi cahaya diuji dengan korelasi Pearson (r), sedangkan pengaruh orientasi baris dan batang bawah diuji dengan ANOVA dua arah dan uji Tukey HSD (p < 0,05). Analisis memakai R (v. 4.0.2).

## Eksperimen dan Hasil

Data uji: 60 petak, empat orientasi baris (N-S, NE-SW, E-W, NW-SE), tiga batang bawah. Pembanding adalah hitungan manual (bunga, buah pada tiga tanggal, tinggi pohon) dan hitungan mesin sortir komersial saat panen (buah dan hasil panen). Metrik: RMSE, rc, R2, r.

Hasil kalibrasi per tanggal ketika batang bawah digabung adalah kemiringan 0,99 (44 DAFB), 1,38 (102 DAFB), dan 1,62 (154 DAFB), dengan RMSE 8, 10, dan 10 buah/citra. Setelah kalibrasi dipisah per batang bawah, RMSE turun (Tabel 1):

| DAFB | Batang bawah | Faktor kalibrasi | RMSE (buah/citra) |
|---|---|---|---|
| 44 | Bud.9 | 0,837 | 1 |
| 44 | M9 | 1,059 | 2 |
| 44 | M26 | 1,161 | 3 |
| 102 | Bud.9 | 0,632 | 6 |
| 102 | M9 | 0,746 | 7 |
| 102 | M26 | 0,787 | 6 |
| 154 | Bud.9 | 0,548 | 5 |
| 154 | M9 | 0,602 | 5 |
| 154 | M26 | 0,708 | 4 |

Hasil utama lainnya:

| Parameter | Hasil | Sumber di makalah |
|---|---|---|
| Kluster bunga (kalibrasi, 50% mekar) | y = 4,205 (0,069) x; RMSE = 5 kluster/citra | Gambar 3 |
| Jumlah buah, validasi 154 DAFB | y = 12,4 + 0,85 x; rc = 0,88; RMSE = 5 buah/pohon | Gambar 7A |
| Hasil panen, validasi 154 DAFB | y = 2,57 + 0,81 x; rc = 0,89; RMSE = 1 kg/pohon | Gambar 7B |
| Galat blok, jumlah buah dan hasil | 4,6% dan 1,2% | Diskusi |
| Tinggi pohon terkalibrasi | rc = 0,93 (intersep 0,171 m dikurangkan; R2 = 0,858 pada model sebelum kalibrasi) | Gambar 8, seksi 3.1.3 |
| EAS dari CSLA | EAS = 0,07 + 0,23 CSLA; R2 = 0,76; RMSE = 0,03 | Persamaan (1) |
| Korelasi CSLA dengan kluster bunga, jumlah buah, hasil | r = 0,562; 0,531; 0,631 (p < 0,001) | Gambar 11 |

CSLA memiliki hubungan paling stabil dengan EAS (R2 >= 0,70) pada dua tanggal, sedangkan kerapatan kanopi berbeda nyata antartanggal (p intersep 0,027; p kemiringan 0,010). Hubungan CSLA dan EAS tidak berbeda nyata antarorientasi baris dan batang bawah (Tabel 3). Orientasi baris dan batang bawah berpengaruh nyata terhadap semua parameter Cartographer tanpa interaksi nyata (Tabel 4). Rerata per orientasi baris untuk jumlah buah per pohon: E-W 72, NE-SW 67, N-S 61, NW-SE 63. Rerata per batang bawah: Bud.9 58, M26 76, M9 63. Hasil panen per pohon (kg): E-W 14,0; NE-SW 13,1; N-S 11,8; NW-SE 12,3; Bud.9 10,9; M26 14,7; M9 12,9. Ukuran efek (eta kuadrat) batang bawah untuk jumlah buah adalah 0,49 dan untuk orientasi baris 0,15.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: satu platform menghasilkan banyak parameter (bunga, buah, hasil, tinggi, geometri kanopi, intersepsi cahaya); galat blok di bawah 5% untuk jumlah buah dan 1,2% untuk hasil panen; validasi dilakukan terhadap data independen dari mesin sortir komersial; peta panas georeferensi dapat mendukung penjarangan, pemangkasan, pemupukan, dan irigasi.

Keterbatasan yang dinyatakan penulis: kalibrasi jumlah buah harus dilakukan terpisah antarbatang bawah dan saat kondisi dalam blok berubah (batang bawah, jarak tanam, jarak baris, arsitektur pohon). Jumlah bunga tidak divalidasi karena tidak ada data validasi independen. Overestimasi kluster bunga disebabkan deteksi dari baris sebelah (positif palsu), dari pohon bersebelahan, deteksi bunga individual dalam kluster sebagai kluster tersendiri, serta deteksi yang terlewat (negatif palsu). Pohon masih muda (daun ketiga; EAS maksimum < 0,35), sehingga pengaruh orientasi baris pada hubungan CSLA-EAS perlu dikaji ulang pada kanopi dewasa. Hubungan bunga, buah, dan hasil dengan CSLA perlu diteliti pada CSLA > 1,10 m2. Pengaruh CSLA pada produktivitas mungkin bersifat tidak langsung melalui intersepsi cahaya.

Menurut pembacaan ringkasan ini, hanya satu kultivar, satu lokasi, dan satu musim yang diuji, dan jumlah buah diukur per citra tanpa mekanisme untuk memastikan buah yang sama tidak terhitung pada citra berurutan; faktor kalibrasi menyerap efek itu secara implisit bersama positif palsu dari baris sebelah. Teks tidak merinci arsitektur CNN dan data latihnya, sehingga detektor tidak dapat dinilai terpisah.

## Kaitan dengan Tinjauan main6

Makalah tidak menangani identitas buah lintas pandang secara eksplisit. Pada citra berurutan 5 citra per detik, buah yang sama tentu tampak pada beberapa citra, tetapi makalah tidak menjelaskan pelacakan, pencocokan multi-pandang, atau rekonstruksi 3D untuk menghitung buah satu kali. Penanganannya hanya berupa faktor kalibrasi empiris (kebalikan kemiringan regresi), yang berubah menurut batang bawah dan tahap pertumbuhan (misalnya 0,837 sampai 0,548 untuk Bud.9 dari 44 sampai 154 DAFB). Hitungan tidak dilaporkan per kelas; yang dilaporkan adalah total per citra, pohon, petak, dan blok.

Acuan hitungnya adalah hitungan manual di lapangan untuk kalibrasi dan hitungan mesin sortir komersial saat panen untuk validasi, bukan anotasi citra. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola kalibrasi hitungan per citra terhadap acuan independen saat panen, penyetelan kalibrasi per kelompok kondisi, dan validasi pada tingkat petak dan blok. Sebaliknya, pendekatan ini tidak menjamin hitungan unik lintas sisi dan tidak menyediakan hitungan per kelas.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `scalisi2021reliability`.

Scalisi dkk. (2021) mengkalibrasi dan memvalidasi platform pindai kebun komersial Cartographer (LiDAR, GPS, dan kamera dengan CNN) pada apel 'ANABP-01' di Tatura, Australia. Setelah kalibrasi per batang bawah, validasi terhadap mesin sortir komersial saat panen menghasilkan RMSE 5 buah/pohon dan 1 kg/pohon untuk jumlah buah dan hasil panen, dengan galat tingkat blok 4,6% dan 1,2%. Luas daun penampang kanopi (CSLA) menjadi prediktor intersepsi cahaya yang paling stabil, dan batang bawah serta orientasi baris berpengaruh nyata terhadap produktivitas.

Catatan verifikasi data: Angka kalibrasi per batang bawah berasal dari Tabel 1, galat validasi dari Gambar 7 dan seksi 3.1.2, galat blok (4,6% dan 1,2%) dari Diskusi, regresi geometri dari Tabel 2 dan Persamaan (1), korelasi dari Gambar 11, serta rerata perlakuan dari Tabel 4. Teks ekstraksi memuat tabel dalam bentuk sel terpisah per baris sehingga pembacaan Tabel 4 mengikuti urutan kolom FCN, FN, YI, TH, CA, CD, CSLA, EAS; angka itu dicocokkan dengan urutan kolom, tetapi tidak dapat diperiksa secara visual pada teks. Arsitektur CNN, jumlah citra latih, dan jumlah citra per kalibrasi tidak dilaporkan dalam teks. RMSE jumlah buah pada Gambar 7 dinyatakan sebagai 5 buah/pohon; satuan RMSE kalibrasi adalah buah per citra.
