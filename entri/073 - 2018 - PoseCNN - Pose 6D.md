# 073 - PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xiang2018posecnn` |
| Judul asli | PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes |
| Penulis | Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, Dieter Fox |
| Tahun | 2018 |
| Venue | Robotics: Science and Systems (RSS) 2018 |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1711.00199
- **Halaman proyek (kode & dataset):** https://rse-lab.cs.washington.edu/projects/posecnn/
- **Google Scholar:** https://scholar.google.com/scholar?q=PoseCNN%3A%20A%20Convolutional%20Neural%20Network%20for%206D%20Object%20Pose%20Estimation%20in%20Cluttered%20Scenes
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PoseCNN%3A%20A%20Convolutional%20Neural%20Network%20for%206D%20Object%20Pose%20Estimation%20in%20Cluttered%20Scenes&sort=relevance

## Gambaran Umum

PoseCNN adalah jaringan saraf konvolusi untuk mengestimasi pose 6D objek — tiga derajat translasi dan tiga derajat rotasi relatif terhadap kamera — pada adegan padat yang objeknya saling menutupi. Masukannya satu citra warna; keluarannya label objek setiap piksel, posisi 3D pusat setiap objek, dan orientasi 3D setiap objek, dengan syarat model 3D objek telah diketahui. Gagasan penentunya adalah memisahkan estimasi translasi dari estimasi rotasi: translasi diperoleh dengan melokalisasi pusat 2D objek pada citra dan memprediksi jaraknya ke kamera, sedangkan rotasi diperoleh dengan meregresi kuaternion (representasi rotasi 3D berkomponen empat) dari fitur visual di sekitar objek.

Hasil utamanya tiga. Pertama, pada dataset baru yang diperkenalkan makalah ini, YCB-Video (21 objek, 92 video, 133.827 bingkai), PoseCNN mencapai area di bawah kurva akurasi 75,9 untuk metrik ADD-S hanya dengan citra warna, berbanding 29,8 dari pendekatan regresi koordinat 3D. Kedua, fungsi rugi baru bernama ShapeMatch-Loss membuat jaringan dapat dilatih pada objek simetris tanpa sinyal pelatihan yang saling bertentangan. Ketiga, dengan penyempurnaan ICP memakai data kedalaman, PoseCNN mencapai akurasi 78,0% pada dataset OccludedLINEMOD, melampaui metode RGB-D terbaik sebelumnya (76,7%).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi pose 6D dibutuhkan robot untuk memanipulasi objek: posisi dan orientasi objek harus diketahui sebelum objek digenggam. Sebelum PoseCNN, metode yang ada terbagi dalam dua keluarga dengan kelemahan berlawanan. Metode berbasis templat mencocokkan model 3D objek terhadap citra pada banyak lokasi; metode ini cocok untuk objek tanpa tekstur, tetapi skor kecocokannya turun tajam bila objek terhalang (teroklusi) objek lain. Metode berbasis fitur mencocokkan titik-titik khas antara citra dan model 3D; metode ini tahan terhadap oklusi, tetapi gagal pada objek miskin tekstur karena titik khas tidak dapat dihitung.

Kelas ketiga, pendekatan pembelajaran yang meregresi koordinat objek 3D untuk setiap piksel lalu memulihkan pose dengan RANSAC (algoritme estimasi yang mencari konsensus dari korespondensi bebas pencilan), menghadapi ambiguitas pada objek simetris: satu penampakan dapat bersesuaian dengan banyak rotasi yang sama-sama benar, sehingga target regresi menjadi tidak konsisten. Regresi translasi dan rotasi secara langsung dari fitur citra juga tidak stabil, karena kedua parameter memiliki sifat visual yang berbeda. Masalah terakhir bersifat praktis: tolok ukur yang tersedia saat itu, misalnya LINEMOD, hanya memuat sekitar 1.000 citra beranotasi per objek — terlalu kecil untuk melatih jaringan dalam.

## Ide Utama

Ide inti PoseCNN adalah dekomposisi tugas sesuai sifat visual masing-masing parameter pose. Translasi menentukan di mana objek tampak pada citra dan seberapa besar ukurannya; rotasi menentukan penampilan permukaannya. Oleh karena itu translasi tidak diregresi langsung, melainkan dihitung secara geometris: jaringan melokalisasi proyeksi pusat objek pada citra (dua koordinat piksel) dan memprediksi jarak pusat ke kamera (satu nilai kedalaman); dengan parameter kamera yang diketahui, tiga angka ini cukup untuk memulihkan translasi 3D. Rotasi tetap diregresi dari fitur yang dipotong pada wilayah objek.

Lokalisasi pusat tidak dilakukan dengan mendeteksi satu titik, melainkan dengan pemungutan suara (*voting*): setiap piksel objek memprediksi arah menuju pusat, dan pusat ditetapkan pada titik temu suara terbanyak. Karena suara datang dari seluruh piksel objek yang terlihat, pusat tetap dapat ditemukan walaupun letaknya sendiri terhalang objek lain.

## Cara Kerja Langkah demi Langkah

Jaringan terdiri atas dua tahap: ekstraksi fitur bersama, lalu tahap *embedding* (pereduksi fitur berdimensi tinggi menjadi fitur khas per tugas berdimensi rendah) yang bercabang tiga. Alur datanya sebagai berikut:

```
citra RGB (640 x 480)
   |
   ▼
┌────────────────────────────────────────────────────┐
| Tahap 1: 13 lapis konvolusi + 4 max-pooling        |
| (VGG16, bobot awal ImageNet)                       |
| keluaran: peta fitur 512 kanal, resolusi 1/8, 1/16 |
└────────────────────────────────────────────────────┘
   |
   ▼ Tahap 2: embedding, lalu tiga cabang
┌───────────────┬────────────────┬───────────────────┐
| A. pelabelan  | B. translasi   | C. rotasi         |
| semantik:     | vektor unit ke | RoI pooling fitur |
| kelas objek   | pusat + Tz     | dalam kotak,      |
| tiap piksel   | tiap piksel    | 3 FC, keluaran    |
| (n kanal)     | per kelas (3n) | kuaternion (4n)   |
└──────┬────────┴───────┬────────┴─────────▲─────────┘
       | label piksel   |                  | kotak pembatas
       └───────────────>| voting Hough     | dari batas
                        | -> pusat 2D + Tz | piksel inlier
                        ▼                  |
                 pusat 2D + Tz             |
                        |                  |
                        └───────┬──────────┘
                                ▼
              translasi T=(Tx,Ty,Tz) + rotasi R (kuaternion)
                                ▼
                     pose 6D tiap objek terdeteksi
                                ▼
              opsional: penyempurnaan ICP bila ada depth
```

Satu ekstraktor fitur menyuplai tiga cabang: pelabelan semantik, arah pusat plus kedalaman, dan regresi rotasi. Hasil cabang pertama dan kedua digabung oleh lapisan voting Hough menjadi translasi, sedangkan cabang ketiga menghasilkan rotasi; keduanya membentuk pose 6D per objek.

### Tahap 1: Ekstraksi Fitur

Tahap pertama terdiri atas 13 lapis konvolusi dan 4 lapis *max-pooling* (operasi yang mengambil nilai maksimum dalam jendela kecil untuk menurunkan resolusi peta fitur), mengikuti arsitektur VGG16 dan diinisialisasi dari bobot hasil pelatihan klasifikasi ImageNet (dataset klasifikasi citra berskala besar). Tahap ini menghasilkan peta fitur 512 kanal pada dua resolusi: 1/8 dan 1/16 dari ukuran citra masukan. Seluruh cabang memakai fitur yang sama, sehingga konvolusi hanya dihitung sekali per citra.

### Cabang A: Pelabelan Semantik per Piksel

Cabang ini mengklasifikasikan setiap piksel ke salah satu dari n kelas objek. Kedua peta fitur 512 kanal direduksi menjadi 64 kanal; peta resolusi 1/16 dinaikkan dua kali lipat dengan lapis dekonvolusi (konvolusi transpose yang menaikkan resolusi spasial), dijumlahkan dengan peta 1/8, lalu satu lapis dekonvolusi lain menaikkan resolusi delapan kali ke ukuran citra penuh. Lapis konvolusi terakhir menghasilkan skor kelas dengan n kanal. Pelatihan memakai rugi entropi silang *softmax*; pengujian memakai *softmax* untuk memperoleh probabilitas kelas tiap piksel. Desain ini mengikuti *fully convolutional network* (FCN), jaringan konvolusi tanpa lapis terhubung penuh yang keluarannya berupa peta beresolusi citra.

### Cabang B: Arah Pusat dan Kedalaman

Arsitekturnya sama dengan cabang A, tetapi dimensi *embedding*-nya 128 dan keluarannya 3n kanal: untuk setiap piksel dan setiap kelas, jaringan meregresi tiga angka — dua komponen vektor satuan arah menuju pusat objek dan satu nilai kedalaman pusat (Tz). Vektor satuan (panjang selalu satu) dipilih alih-alih vektor perpindahan karena invarian terhadap skala: piksel dekat dan jauh dari pusat memiliki target regresi dengan besar sama, hanya arahnya berbeda. Rugi yang dipakai adalah *smoothed L1*, fungsi rugi regresi yang kuadratik untuk galat kecil dan linear untuk galat besar sehingga tidak sensitif terhadap pencilan.

### Lapisan Voting Hough

Untuk menetapkan pusat 2D objek, setiap piksel berlabel kelas tertentu memberi suara pada lokasi-lokasi citra sepanjang sinar arah yang diprediksinya; lokasi berskor tertinggi menjadi pusat objek. Bila terdapat beberapa instans dari kelas yang sama, diterapkan *non-maximum suppression* (dari lokasi berskor tinggi yang berdekatan hanya yang tertinggi dipertahankan) dan diambil lokasi yang melampaui ambang. Piksel yang memvoting suatu pusat disebut *inlier* pusat itu; Tz dihitung sebagai rata-rata kedalaman yang diprediksi para inlier, dan kotak pembatas (*bounding box*) objek diturunkan sebagai persegi terkecil yang memuat seluruh inlier. Translasi 3D dipulihkan dengan persamaan proyeksi kamera lubang jarum: cx = fx·Tx/Tz + px dan cy = fy·Ty/Tz + py, dengan (fx, fy) panjang fokus dan (px, py) titik utama kamera. Contoh numerik: bila fx = fy = 500 piksel, titik utama (320, 240), pusat terpilih (420, 340), dan Tz = 0,8 m, maka Tx = (420−320)/500 × 0,8 = 0,16 m dan Ty = (340−240)/500 × 0,8 = 0,16 m. Lapisan voting berjalan di GPU dan tidak meneruskan gradien, sehingga pelatihan cabang berhenti di keluaran regresi.

### Cabang C: Regresi Rotasi

Cabang ini memakai dua lapis *RoI pooling* — operasi yang memotong peta fitur sesuai kotak pembatas objek dan mengubahnya ke ukuran tetap — untuk mengambil fitur visual objek dari tahap pertama. Fitur hasil *pooling* dijumlahkan, lalu dilewatkan ke tiga lapis terhubung penuh (*fully connected*, FC) berdimensi 4096, 4096, dan 4n: setiap kelas memperoleh empat keluaran yang membentuk kuaternion rotasinya. Kuaternion adalah bilangan empat komponen yang merepresentasikan rotasi 3D tanpa kegandaan sudut.

### Dua Fungsi Rugi Rotasi

Fungsi pertama, PoseLoss (PLoss), adalah rata-rata kuadrat jarak antara titik-titik model 3D yang diputar oleh rotasi kebenaran dasar dan titik yang sama yang diputar oleh rotasi prediksi; nilainya minimum saat kedua rotasi identik. Pada objek simetris, PLoss memberi sinyal yang keliru: rotasi prediksi yang benar secara bentuk tetap dihukum karena berbeda dari rotasi anotasi. Fungsi kedua, ShapeMatch-Loss (SLoss), menghitung untuk setiap titik model hasil rotasi prediksi jaraknya ke titik terdekat pada model hasil rotasi kebenaran dasar; rugi bernilai nol selama kedua bentuk 3D berimpit, tanpa perlu menyebutkan sumbu simetri secara manual.

### Penyempurnaan dengan ICP

Bila data kedalaman tersedia, pose keluaran jaringan disempurnakan dengan *Iterative Closest Point* (ICP), algoritme yang secara berulang mencari titik terdekat antara model 3D dan awan titik hasil pengamatan untuk meminimalkan jaraknya. PoseCNN memakai ICP dengan asosiasi data proyektif dan residual titik-ke-bidang, dengan label semantik untuk memotong titik milik objek. Karena ICP rawan terjebak pada minimum lokal, beberapa pose hasil perturbasi pose awal disempurnakan dan yang terbaik dipilih dengan metrik penyelarasan.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua dataset. YCB-Video memuat 21 objek dari himpunan objek YCB (kumpulan objek standar untuk riset manipulasi) dalam 92 video beresolusi 640×480 dengan total 133.827 bingkai; 80 video dipakai untuk pelatihan dan 2.949 bingkai kunci dari 12 video sisanya untuk pengujian, ditambah 80.000 citra sintetis untuk pelatihan. OccludedLINEMOD memuat 1.214 bingkai dengan anotasi delapan objek yang saling menutupi. Jaringan diimplementasikan dengan TensorFlow dan dilatih dengan SGD (*stochastic gradient descent*) bermomentum.

Metrik yang dipakai adalah ADD, rata-rata jarak titik-titik model yang berpasangan antara pose benar dan pose prediksi, dan ADD-S, varian untuk objek simetris yang memakai titik terdekat. Alih-alih satu ambang tetap, akurasi dihitung pada rentang ambang sampai 10 cm dan dilaporkan sebagai area di bawah kurva akurasi-ambang (AUC; makin besar makin baik). Pada OccludedLINEMOD, pose dianggap benar bila ADD atau ADD-S berada di bawah 10% diameter model.

Hasil AUC pada YCB-Video (rata-rata 21 objek):

- regresi koordinat 3D (warna saja): ADD 15,1 / ADD-S 29,8
- PoseCNN (warna saja): ADD 53,7 / ADD-S 75,9
- regresi koordinat 3D + ICP: ADD 74,5 / ADD-S 90,1
- PoseCNN + ICP: ADD 79,3 / ADD-S 93,0

Dengan warna saja, PoseCNN mengungguli garis dasar regresi koordinat 3D sebesar 38,6 poin pada ADD dan 46,1 poin pada ADD-S; ini menunjukkan lokalisasi pusat melalui voting lebih tahan oklusi daripada pencocokan koordinat 3D per piksel. Penyempurnaan ICP menaikkan kedua metode, tetapi PoseCNN tetap unggul (93,0 berbanding 90,1) karena inisialisasi pose yang lebih baik memperbesar peluang ICP konvergen. Kesalahan tersisa terkonsentrasi pada kaleng tuna yang kecil dan miskin tekstur, serta pada pasangan klem besar dan klem ekstra besar yang berpenampilan hampir identik dan saling tertukar.

Analisis fungsi rugi rotasi menunjukkan mekanisme penanganan simetri. Pada objek simetris (balok kayu dan klem besar), histogram galat rotasi dengan PLoss tersebar dari 0° sampai 180° — bukti jaringan menerima target yang ambigu. Dengan SLoss, galat terkonsentrasi pada sudut-sudut simetri objek (180° untuk balok kayu; 0° dan 180° untuk klem besar), artinya jaringan belajar rotasi yang benar sampai sebatas simetri bentuk.

Pada OccludedLINEMOD, PoseCNN+ICP mencapai 78,0%, di atas Michel dkk. (76,7%), Hinterstoisser dkk. (76,3%), Krull dkk. (70,3%), dan Brachmann dkk. (56,6%) yang semuanya memakai RGB-D. Lonjakan terbesar terjadi pada dua objek simetris: Eggbox 72,2% berbanding 47,6% milik Michel dkk., dan Glue 76,7% berbanding 73,8% — bukti kontribusi SLoss. Dengan warna saja, PoseCNN mencapai 24,9%; angka ini rendah karena ambang 10% diameter objek-objek kecil di dataset ini umumnya di bawah 2 cm, ketelitian yang sukar dicapai tanpa kedalaman. Pada metrik galat re-proyeksi (jarak antar-proyeksi titik model pada citra), kurva PoseCNN berada jauh di atas metode satu tahap berbasis warna dari Tekin dkk., terutama pada ambang kecil.

## Kelebihan dan Keterbatasan

Kelebihan: (1) satu jaringan dilatih ujung-ke-ujung (*end-to-end*) untuk tiga tugas sekaligus tanpa pencocokan templat eksternal; (2) voting pusat membuat translasi tahan oklusi, karena piksel yang terlihat tetap memvoting pusat yang terhalang; (3) SLoss menangani simetri tanpa anotasi sumbu simetri manual; (4) inferensi hanya membutuhkan citra warna, tidak bergantung pada sensor kedalaman; (5) YCB-Video menjadi tolok ukur standar bidang ini.

Keterbatasan: (1) tanpa kedalaman, akurasi pada ambang ketat tertinggal jauh, yaitu 24,9% pada OccludedLINEMOD; (2) jaringan tidak dapat membedakan dua objek berpenampilan hampir sama, karena keputusan kelas sepenuhnya visual; (3) penulis mencatat SLoss kadang terjebak pada minimum lokal ruang pose, serupa dengan ICP; (4) dari sisi rekayasa, lapisan voting Hough yang tidak meneruskan gradien memutus jalur optimasi menyeluruh antara regresi arah dan lokalisasi pusat; (5) secara konseptual, kebutuhan akan model 3D setiap objek dan satu set keluaran per kelas membatasi penerapan pada himpunan objek yang sudah diketahui.

## Kaitan dengan Bab Lain

Bab ini membuka klaster Pose 6D dalam tinjauan dan menjadi titik banding bagi seluruh bab sesudahnya. [Bab 074 - DenseFusion](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md) menggantikan tahap ICP pasca-jaringan dengan fusi fitur RGB dan geometri per titik serta penyempurnaan berbasis jaringan. [Bab 075 - PVN3D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md) memindahkan gagasan voting dari piksel 2D ke titik kunci 3D pada awan titik. [Bab 076 - FFB6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md) dan [Bab 077 - G2L-Net](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md) meneruskan garis fusi RGB-D ini. [Bab 078 - FoundationPose](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md) menjawab keterbatasan kelima di atas dengan melepaskan kebutuhan pelatihan ulang untuk objek baru. Posisi PoseCNN dalam lanskap yang lebih luas dipetakan pada [Bab 079 - Review Pose 6D & Deteksi 3D](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md).

## Poin untuk Sitasi

Kutip dengan kunci `xiang2018posecnn`. Ringkasan yang aman dikutip: "PoseCNN mengestimasi pose 6D objek dari satu citra warna dengan mendekopel translasi — dilokalisasi melalui voting arah pusat per piksel ditambah regresi kedalaman — dan rotasi yang diregresi sebagai kuaternion. Fungsi rugi ShapeMatch-Loss memungkinkan pelatihan pada objek simetris, dan makalah ini sekaligus memperkenalkan tolok ukur YCB-Video (21 objek, 133.827 bingkai)." Seluruh angka hasil di bab ini (AUC 53,7/75,9/79,3/93,0 pada YCB-Video; 78,0%, 24,9%, dan angka pembanding pada OccludedLINEMOD) telah dicocokkan dengan Tabel II dan Tabel III naskah. Dua catatan verifikasi: makalah tidak melaporkan kecepatan inferensi, sehingga klaim kecepatan tidak boleh dikutip tanpa sumber lain; angka per objek selain yang dikutip di sini perlu diverifikasi langsung ke Tabel II–III naskah sebelum sitasi formal.
