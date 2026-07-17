# 072 - Deep Learning for Monocular Depth Estimation: A Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ming2021depthsurvey` |
| Judul asli | Deep Learning for Monocular Depth Estimation: A Review |
| Penulis | Yue Ming, Xuyang Meng, Chunxiao Fan, Hui Yu |
| Tahun | 2021 |
| Venue | Neurocomputing, vol. 438, hlm. 14–33 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1016/j.neucom.2020.12.089
- **Halaman repositori (University of Portsmouth):** https://researchportal.port.ac.uk/en/publications/deep-learning-for-monocular-depth-estimation-a-review/
- **Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Learning%20for%20Monocular%20Depth%20Estimation%3A%20A%20Review
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Deep%20Learning%20for%20Monocular%20Depth%20Estimation%3A%20A%20Review&sort=relevance

## Gambaran Umum

Makalah ini adalah tinjauan (*review*) yang memetakan metode *deep learning* untuk estimasi kedalaman monokular, yaitu tugas memprediksi jarak setiap piksel dari kamera hanya dengan bermodal satu citra RGB. Ming dan rekan menghimpun publikasi rentang 2014 sampai 2020, lalu menatanya ke dalam taksonomi berdasarkan cara metode memperoleh sinyal pelatihan: *supervised* (dengan label kedalaman), *unsupervised*/*self-supervised* (tanpa label, memanfaatkan kendala geometri), dan *semi-supervised* (memadukan sedikit label dengan kendala geometri). Selain itu makalah membahas ragam arsitektur jaringan, fungsi *loss*, dataset publik beserta metrik evaluasinya, serta tantangan yang masih terbuka.

Nilai makalah ini terletak pada fungsinya sebagai peta bidang, bukan pada satu arsitektur baru. Bagi pembaca tinjauan pustaka ini, makalah tersebut menjadi kerangka untuk menempatkan bab-bab kedalaman lain — mulai dari metode terawasi seperti Eigen dkk. (bab 062) dan BTS (bab 065) hingga metode swa-awasan seperti Monodepth (bab 063) dan Monodepth2 (bab 064) — pada posisinya masing-masing dalam satu taksonomi yang konsisten.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra bersifat *ill-posed* (tak berketetapan): tak terhingga banyaknya susunan tiga dimensi yang, ketika diproyeksikan ke bidang citra dua dimensi, menghasilkan citra yang sama persis. Kamera tunggal membuang informasi jarak, sehingga sebuah objek kecil yang dekat dan objek besar yang jauh dapat menempati wilayah piksel yang identik. Konsekuensinya, kedalaman tidak dapat dipulihkan dari geometri semata; metode apa pun harus menyandarkan diri pada regularitas statistik dunia nyata yang dipelajari dari data.

Sebelum era *deep learning*, kedalaman dari satu tampilan diperkirakan lewat isyarat khusus seperti *shape-from-focus*/*shape-from-defocus* (kedalaman disimpulkan dari tingkat ketajaman atau keburaman bagian citra). Metode semacam ini menuntut asumsi ketat — pengaturan optik terkendali, banyak pengambilan pada fokus berbeda, atau kalibrasi khusus — sehingga sukar diterapkan pada citra sembarang. Sensor kedalaman langsung seperti LiDAR (pemindai laser jarak) dan kamera RGB-D (kamera yang merekam warna sekaligus kedalaman) memberi hasil akurat, tetapi mahal, boros daya, atau terbatas jangkauannya.

Munculnya *convolutional neural network* (jaringan saraf konvolusi, disingkat CNN) yang mampu mempelajari isyarat kedalaman monokular — perspektif, ukuran objek yang dikenal, oklusi, gradien tekstur — langsung dari sekumpulan besar contoh mengubah keadaan. Namun dalam beberapa tahun jumlah metode meledak dengan asumsi pelatihan, arsitektur, fungsi *loss*, dan tolok ukur yang berbeda-beda, sehingga sulit dibandingkan secara adil. Kondisi inilah yang hendak dijawab tinjauan Ming dkk.: menyediakan klasifikasi yang koheren agar keragaman itu dapat dipahami dan dinilai.

## Ide Utama

Gagasan pengorganisasian utama makalah adalah membedakan metode berdasarkan *jenis sinyal pengawasan* yang dipakai saat pelatihan, karena pilihan ini menentukan dataset yang dibutuhkan, bentuk fungsi *loss*, dan sifat keluaran (kedalaman metrik dalam satuan nyata atau hanya kedalaman relatif). Dari sumbu ini turun tiga kategori besar: *supervised*, *unsupervised*/*self-supervised*, dan *semi-supervised*. Sumbu kedua yang dipakai untuk memilah adalah komponen teknis lintas kategori — rancangan arsitektur, fungsi *loss*, serta protokol dataset dan metrik.

Inti telaah ini bukan mengklaim satu pendekatan menang, melainkan menunjukkan *pertukaran* (*trade-off*) yang melekat: metode terawasi memberi kedalaman metrik akurat tetapi menuntut label kedalaman yang mahal; metode swa-awasan melepas kebutuhan label dengan bersandar pada kendala geometri, tetapi umumnya hanya memulihkan kedalaman relatif dan rapuh terhadap objek bergerak. Taksonomi menjadi alat untuk menempatkan pertukaran ini secara eksplisit.

## Cara Kerja Langkah demi Langkah

Bagian ini menguraikan taksonomi dan komponen metodologis yang disintesis makalah, bukan pipeline satu model. Struktur klasifikasinya dapat dilihat sebagai berikut.

```
   Estimasi Kedalaman Monokular (deep learning)
                     │
     ┌───────────────┼───────────────────┐
     ▼               ▼                    ▼
 Supervised     Self-supervised      Semi-supervised
 (label depth)  (tanpa label)        (label sebagian)
     │               │                    │
 regresi depth   ┌───┴────┐          label jarang +
 per piksel      ▼        ▼          kendala geometri
                stereo   video       / data sintetis
                (L-R)   (depth+pose)
```

### Metode Terawasi (*Supervised*)

Metode terawasi melatih jaringan untuk meregresi nilai kedalaman setiap piksel dengan target kebenaran (*ground truth*) yang diperoleh dari sensor: peta kedalaman padat dari kamera RGB-D untuk citra dalam ruangan, atau titik kedalaman jarang dari LiDAR untuk citra luar ruangan. Karya rintisan Eigen dkk. (2014) memakai jaringan bertingkat kasar-ke-halus (*coarse-to-fine*) untuk memperkirakan kedalaman global lalu menyempurnakannya secara lokal, dan memperkenalkan *loss* invarian-skala yang menghukum galat bentuk relatif kedalaman tanpa menghukum ketaktentuan skala global. Perkembangan berikutnya menambahkan *conditional random field* (CRF, model yang menghaluskan prediksi dengan mempertimbangkan kesamaan piksel bertetangga), regresi berbasis pengelompokan nilai kedalaman ke dalam interval (*binning*), serta *backbone* yang lebih dalam. Keunggulannya adalah kedalaman metrik yang akurat; bebannya adalah ketergantungan pada label yang mahal dan, untuk LiDAR, hanya tersedia jarang sehingga sebagian besar piksel tak berlabel.

### Metode Swa-Awasan (*Unsupervised* / *Self-supervised*)

Kategori ini menghilangkan kebutuhan label kedalaman dengan mengganti pengawasan langsung menjadi kendala geometri sebagai sinyal pelatihan. Dua sub-keluarga menonjol. Pertama, pendekatan berbasis stereo: jaringan dilatih memakai pasangan citra kiri-kanan terkalibrasi, memprediksi *disparitas* (pergeseran piksel antara kedua tampilan yang berbanding terbalik dengan kedalaman), lalu merekonstruksi satu tampilan dari tampilan lawannya. Selisih antara citra rekonstruksi dan citra asli — disebut *loss* fotometrik — menjadi sinyal belajar. Godard dkk. (Monodepth, bab 063) menambahkan kendala konsistensi kiri-kanan agar disparitas dari kedua arah saling cocok. Kedua, pendekatan berbasis video monokular: jaringan kedalaman dilatih bersama jaringan pose yang memperkirakan gerak kamera antar-bingkai (*ego-motion*), sehingga satu bingkai dapat disintesis dari bingkai tetangga; galat sintesis menjadi *loss*. Monodepth2 (bab 064) menyempurnakan skema ini. Kelemahannya: keluaran umumnya berupa kedalaman relatif (skala tak tertentu), dan asumsi adegan statis pada varian video dilanggar oleh objek yang bergerak.

### Metode Semi-Awasan (*Semi-supervised*)

Kategori ketiga memadukan sedikit sinyal berlabel dengan kendala geometri untuk mengambil manfaat keduanya. Bentuknya beragam: melengkapi *loss* fotometrik swa-awasan dengan titik LiDAR jarang sebagai jangkar skala metrik; memakai data sintetis berlabel padat lalu menjembatani selisih domain ke citra nyata (*domain adaptation*); atau menggabungkan pengawasan stereo dengan sebagian kebenaran kedalaman. Tujuannya menekan biaya anotasi sambil memulihkan skala metrik yang hilang pada pendekatan swa-awasan murni.

### Arsitektur dan Fungsi Loss

Lintas ketiga kategori, tulang punggung arsitektur yang berulang adalah *encoder-decoder* (penyandi-penerjemah): penyandi memampatkan citra menjadi fitur beresolusi rendah bermuatan semantik, penerjemah memulihkannya menjadi peta kedalaman beresolusi penuh, dengan *skip connection* (jalur pintas antar-resolusi) untuk mengembalikan detail tepi yang hilang saat pemampatan. Varian mencakup prediksi multi-skala, penghalusan CRF, dan pelatihan berlawanan berbasis *generative adversarial network* (GAN). Fungsi *loss* yang ditinjau meliputi galat L1/L2 terhadap kebenaran, *loss* invarian-skala, *loss* fotometrik, *loss* konsistensi kiri-kanan, dan regularisasi kehalusan (*smoothness*) yang mendorong kedalaman berubah mulus kecuali pada tepi citra.

### Dataset dan Metrik

Makalah merangkum dataset publik yang menjadi tolok ukur bidang ini. Yang paling sering muncul adalah KITTI (adegan mengemudi luar ruangan dengan kedalaman LiDAR jarang) dan NYU Depth v2 (adegan dalam ruangan dengan kedalaman padat dari kamera Kinect); dataset luar ruangan lain seperti Make3D dan Cityscapes juga dibahas. Metrik evaluasi baku dibedakan menjadi metrik galat (makin kecil makin baik) dan metrik akurasi (makin besar makin baik). Metrik galat mencakup *Absolute Relative error* (AbsRel, rata-rata galat mutlak dinormalkan terhadap kedalaman sebenarnya), *Squared Relative error* (SqRel), *Root Mean Square Error* (RMSE), dan RMSE dalam ranah logaritma. Metrik akurasi berupa persentase piksel yang rasio prediksi terhadap kebenarannya berada di bawah ambang δ, dengan tiga ambang lazim 1,25, 1,25², dan 1,25³. Sebagai contoh konkret, δ < 1,25 menghitung berapa persen piksel yang prediksinya menyimpang kurang dari 25 persen dari kedalaman sebenarnya; pada peta kedalaman 640×480 piksel yang memuat 307.200 nilai, metrik ini menyatakan berapa banyak dari nilai-nilai itu yang jatuh dalam toleransi tersebut.

## Eksperimen dan Hasil

Sebagai tinjauan, makalah tidak menjalankan eksperimen baru, melainkan mengompilasi dan membandingkan angka yang dilaporkan berbagai metode pada tolok ukur bersama, terutama KITTI dan NYU Depth v2, memakai metrik AbsRel, RMSE, dan akurasi ambang di atas. Analisis komparatif ini memperlihatkan pola umum: metode terawasi cenderung unggul pada metrik galat metrik karena dilatih langsung terhadap kedalaman sebenarnya, sementara metode swa-awasan mempersempit selisih dari waktu ke waktu tanpa memerlukan label, dengan mengorbankan ketertentuan skala. Karena kondisi pelatihan tiap metode berbeda (resolusi, potongan dataset, protokol evaluasi), makalah menekankan bahwa perbandingan angka lintas kategori perlu dibaca sebagai indikasi tren, bukan peringkat mutlak. Interpretasi ini penting: kenaikan atau penurunan satu metrik hanya bermakna bila dibandingkan pada protokol yang setara.

## Kelebihan dan Keterbatasan

Kelebihan tinjauan ini adalah cakupan yang menyeluruh untuk rentang 2014–2020 dan taksonomi yang bersandar pada satu sumbu jelas (jenis pengawasan), sehingga metode yang beragam dapat ditempatkan tanpa tumpang-tindih kategori. Ikhtisar dataset dan metriknya memberi rujukan praktis bagi peneliti yang hendak memilih protokol evaluasi. Makalah juga menutup dengan diskusi tantangan terbuka: pemulihan skala metrik pada metode swa-awasan, generalisasi lintas domain (model yang dilatih pada satu dataset kerap merosot pada dataset lain), penanganan objek dinamis yang melanggar asumsi adegan statis, ketajaman tepi dan daerah oklusi, serta efisiensi komputasi untuk penerapan waktu-nyata.

Keterbatasannya, dari sisi cakupan, adalah batas waktu 2020. Gelombang metode berbasis *transformer* dan model kedalaman lintas-dataset berskala besar — DPT (bab 067), MiDaS (bab 068), dan AdaBins (bab 066) — baru muncul atau matang setelahnya, sehingga tren *foundation model* untuk kedalaman tidak tercakup penuh. Secara konseptual, taksonomi berbasis jenis pengawasan juga menyederhanakan metode hibrida yang menempati lebih dari satu kategori sekaligus, sehingga penempatannya kadang tidak tunggal.

## Kaitan dengan Bab Lain

Bab ini berfungsi sebagai payung bagi klaster Estimasi Kedalaman dalam tinjauan. Kategori terawasinya diwakili [062 - Depth dari Citra Tunggal (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md) sebagai perintis dan [065 - BTS](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md) sebagai penyempurna berlabel. Kategori swa-awasannya dijabarkan pada [063 - Monodepth](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md) untuk jalur stereo dan [064 - Monodepth2](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) serta [069 - PackNet](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md) untuk jalur video. Tren pasca-cakupan yang disebut di bagian keterbatasan berlanjut ke [066 - AdaBins](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md), [067 - DPT](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md), dan [068 - MiDaS](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md). Dalam kaitan dengan fokus utama tinjauan, metode-metode yang dipetakan di sini menyediakan kedalaman semu (*pseudo-depth*) yang dapat melengkapi kanal warna pada pipeline deteksi RGB-D, sehingga bab ini menjembatani klaster kedalaman dengan klaster deteksi.

## Poin untuk Sitasi

Kutip dengan kunci `ming2021depthsurvey`. Ringkasan yang aman dikutip: "Ming dkk. (2021) meninjau metode *deep learning* untuk estimasi kedalaman monokular pada rentang 2014–2020, menatanya ke dalam taksonomi *supervised*, *self-supervised*, dan *semi-supervised*, serta merangkum arsitektur, fungsi *loss*, dataset (antara lain KITTI dan NYU Depth v2), dan metrik evaluasi baku." Perlu diverifikasi ke naskah asli sebelum sitasi formal: daftar lengkap dataset yang dibahas (khususnya penyebutan Make3D dan Cityscapes), definisi dan ambang persis metrik akurasi (δ < 1,25 dan turunannya), serta rentang tahun cakupan yang tepat. Batas volume/halaman (Neurocomputing vol. 438, hlm. 14–33) berasal dari catatan bibliografis dan sebaiknya dicocokkan dengan halaman penerbit.
