# 074 - DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2019densefusion` |
| Judul asli | DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion |
| Penulis | Chen Wang, Danfei Xu, Yuke Zhu, Roberto Martín-Martín, Cewu Lu, Li Fei-Fei, Silvio Savarese |
| Tahun | 2019 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2019) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1901.04780
- **Halaman proyek:** https://sites.google.com/view/densefusion/
- **Repositori kode resmi:** https://github.com/j96w/DenseFusion
- **Google Scholar:** https://scholar.google.com/scholar?q=DenseFusion%3A%206D%20Object%20Pose%20Estimation%20by%20Iterative%20Dense%20Fusion
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=DenseFusion%3A%206D%20Object%20Pose%20Estimation%20by%20Iterative%20Dense%20Fusion&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DenseFusion, kerangka *end-to-end* (dilatih dari masukan ke keluaran sebagai satu kesatuan) untuk mengestimasi pose 6D objek yang model 3D-nya telah diketahui, dari satu citra RGB-D. Pose 6D adalah enam derajat kebebasan posisi objek relatif terhadap kamera — tiga komponen translasi dan tiga komponen rotasi, ditulis sebagai matriks transformasi p = [R|t]. Citra RGB-D adalah citra warna yang setiap pikselnya juga memuat nilai kedalaman (jarak ke kamera), misalnya dari sensor Kinect. Masalah yang dipecahkan adalah dua kelemahan metode sebelumnya: pemrosesan warna dan kedalaman secara terpisah yang membuang sifat saling melengkapi keduanya, serta ketergantungan pada pasca-pemrosesan ICP yang lambat.

Gagasan utamanya adalah fusi padat (*dense fusion*) tingkat piksel: setiap titik 3D dari peta kedalaman dipasangkan dengan fitur warna piksel yang bersesuaian, sehingga setiap titik membawa informasi geometri sekaligus penampakan. Dari setiap fitur gabungan, jaringan memprediksi satu pose lengkap beserta skor kepercayaan; prediksi berkepercayaan tertinggi menjadi keluaran, lalu sebuah modul *refinement* iteratif berbasis jaringan saraf memperbaikinya tanpa ICP. Pada tolok ukur YCB-Video, DenseFusion mengungguli PoseCNN yang sudah dimurnikan dengan ICP sebesar 3,5% pada metrik akurasi presisi tinggi, sambil berjalan sekitar 200 kali lebih cepat (16 *frame* per detik). Dalam uji robot nyata, pose hasil estimasi cukup akurat untuk mengangkat objek dengan tingkat keberhasilan 73%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi pose 6D diperlukan pada aplikasi yang menuntut interaksi fisik dengan objek: pemegangan robot (*grasping*), navigasi otonom, dan *augmented reality*. Metode klasik mengekstrak fitur rancangan manual (*handcrafted*) dari data RGB-D, mengelompokkan korespondensi, lalu memverifikasi hipotesis pose. Pendekatan ini rapuh terhadap oklusi (objek terhalang sebagian) dan perubahan pencahayaan, karena fiturnya tidak dipelajari dari data.

Generasi berikutnya memakai jaringan saraf dalam. [PoseCNN](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md) (bab 073) mengestimasi pose langsung dari citra RGB, tetapi untuk memanfaatkan kedalaman ia memerlukan tahap ICP (*Iterative Closest Point*): algoritme iteratif yang menyelaraskan model 3D objek ke *point cloud* — himpunan titik 3D hasil pengukuran sensor kedalaman — dengan meminimalkan jarak titik-terdekat secara berulang. ICP pada PoseCNN sangat disesuaikan, tidak dapat dilatih bersama jaringan utama, dan menjadi penghambat kecepatan. Pendekatan lain dari bidang mengemudi otonom, PointFusion, memadukan warna dan geometri dalam satu jaringan, tetapi fusinya bersifat global: satu vektor fitur citra disambungkan dengan satu vektor fitur geometri untuk seluruh objek. Fusi global semacam ini menghapus detail lokal; ketika objek terhalang, bagian yang keliru ikut menentukan pose. Kebutuhan yang belum terpenuhi saat itu adalah metode yang memanfaatkan kedua modalitas secara lokal per piksel, tetap akurat pada adegan berdesakan, dan berjalan *real-time* untuk kendali robot.

## Ide Utama

Gagasan inti DenseFusion adalah mengganti fusi global dengan fusi lokal yang disertai pemilihan prediksi. Secara mekanis: peta kedalaman diubah menjadi *point cloud* memakai parameter intrinsik kamera; setiap titik diproyeksikan kembali ke bidang citra sehingga dapat dipasangkan dengan fitur warna pikselnya; hasilnya adalah himpunan fitur gabungan, satu per titik. Setiap fitur gabungan memprediksi satu kandidat pose lengkap beserta skor *confidence* (kepercayaan) yang dipelajari jaringan secara mandiri. Titik pada bagian objek yang terlihat jelas menghasilkan prediksi baik dan kepercayaan tinggi; titik pada bagian terhalang atau salah segmentasi menghasilkan prediksi buruk, tetapi kepercayaannya otomatis direndahkan. Pose akhir adalah kandidat dengan kepercayaan tertinggi. Dengan cara ini oklusi tidak lagi mencemari satu prediksi global, karena prediksi dipilih dari bagian objek yang benar-benar terlihat. Di atas mekanisme tersebut, sebuah modul jaringan memperbaiki pose secara iteratif, menggantikan peran ICP dengan komponen yang dapat dilatih dan cepat.

## Cara Kerja Langkah demi Langkah

Alur keseluruhan dari masukan ke keluaran:

```
 masukan: citra RGB-D + mask segmen per objek
        │                                   │
        ▼                                   ▼
 potongan RGB (crop)             kedalaman termask -> P titik 3D
        │                                   │
        ▼                                   ▼
 ResNet-18 + 4 lapis up-sampling  PointNet (MLP, reduksi avg-pool)
        │                                   │
        ▼                                   ▼
 embedding warna 128-d/piksel     fitur geometri 128-d/titik
        │                                   │
        └─── pemasangan titik-piksel via intrinsik kamera ────┘
                                │
                                ▼
     fusi per titik: [warna 128 | geometri 128 | fitur global]
                                │
                                ▼
      P kandidat pose [R|t], masing-masing + confidence c
                                │
                                ▼
        pose terpilih = kandidat dengan c tertinggi
                                │
                                ▼
        refinement: 2 iterasi prediksi residu pose
```

Diagram menunjukkan dua cabang heterogen (citra dan titik) yang bertemu pada fusi per titik. Bagian berikut menguraikan setiap tahap.

### Segmentasi Semantik sebagai Tahap Pertama

Tahap pertama menghasilkan mask (peta biner per kelas) untuk setiap objek yang dikenal. Jaringannya berarsitektur *encoder-decoder* (enkoder memampatkan citra menjadi fitur, dekoder mengembalikannya ke resolusi penuh) dengan keluaran N+1 kanal untuk N kelas objek ditambah latar belakang. DenseFusion memakai jaringan segmentasi PoseCNN apa adanya; kontribusi makalah ini bukan pada segmentasi. Untuk tiap objek, mask menentukan dua hal: potongan citra (*crop*) di dalam kotak pembatas (*bounding box*) mask, dan himpunan piksel kedalaman yang akan diubah menjadi titik 3D.

### Ekstraksi Fitur Warna per Piksel

Potongan RGB diproses oleh enkoder ResNet-18 — jaringan residual 18 lapis yang memakai sambungan pintas untuk memudahkan pelatihan jaringan dalam — diikuti empat lapis *up-sampling* sebagai dekoder. Keluarannya adalah peta *embedding* (vektor fitur hasil pembelajaran) berukuran H×W×128: setiap piksel potongan membawa vektor 128 dimensi yang meringkaskan penampakan lokalnya. Resolusi keluaran dijaga agar korespondensi piksel-titik tetap dapat dibentuk.

### Ekstraksi Fitur Geometri per Titik

Piksel kedalaman termask diubah menjadi titik 3D dengan parameter intrinsik kamera: untuk piksel (u, v) berkedalaman d, koordinat titiknya adalah ((u−cx)·d/fx, (v−cy)·d/fy, d), dengan (fx, fy) panjang fokus dan (cx, cy) titik utama kamera. Titik-titik ini diproses varian PointNet, jaringan milik Qi dkk. (2017) yang dirancang untuk himpunan titik tidak berurutan: sebuah MLP (perseptron multilapis) memetakan setiap titik secara independen ke ruang fitur, lalu fungsi reduksi simetris menggabungkan seluruh fitur menjadi satu vektor global — disebut simetris karena hasilnya tidak bergantung urutan titik. DenseFusion memakai *average-pooling* (perata-rataan) alih-alih *max-pooling* yang lazim dipakai. Setiap titik keluar dengan fitur geometri 128 dimensi.

### Fusi Padat per Piksel

Setiap titik 3D diproyeksikan ke bidang citra memakai intrinsik yang sama, sehingga pasangan (fitur geometri titik, *embedding* warna piksel) terbentuk satu per satu. Pasangan disatukan dengan penyambungan (*concatenation*), lalu sebuah jaringan mereduksi seluruh pasangan menjadi satu fitur global; fitur global ini disalin dan disambungkan ke setiap fitur per titik agar konteks seluruh objek tersedia pada tiap prediksi lokal. Hasil tahap ini: P fitur gabungan, satu untuk setiap titik.

### Prediksi Pose per Titik dengan Confidence

Setiap fitur gabungan dilewatkan ke prediktor yang mengeluarkan satu pose [R|t] dan satu skor *confidence* c. Fungsi *loss* untuk kandidat ke-i adalah rata-rata jarak antara titik-titik model objek pada pose kebenaran dan pada pose prediksi — bentuk yang sama dengan metrik ADD pada bagian eksperimen. Untuk objek simetris (misalnya mangkuk) definisi itu ambigu karena banyak orientasi tampak identik; *loss*-nya diganti jarak ke titik model terdekat. Total *loss* berbentuk L = (1/N) Σ (Lᵢ·cᵢ − w·log cᵢ) dengan w = 0,01. Mekanismenya: prediksi buruk dapat menekan kontribusinya dengan menurunkan c, tetapi suku −w·log c menghukum kepercayaan yang terlalu rendah. Jaringan dengan demikian belajar sendiri titik mana yang layak dipercaya, tanpa label kepercayaan eksplisit — inilah *self-supervised confidence*. Pose keluaran adalah kandidat dengan c tertinggi.

### Refinement Iteratif Berbasis Jaringan

Modul terakhir menggantikan ICP. Setelah pose awal diperoleh, *point cloud* ditransformasikan dengan pose tersebut; pada kerangka baru ini, sisa galat pose tampak sebagai pergeseran kecil dari posisi kanonik objek. Fitur geometri dihitung ulang pada titik hasil transformasi, difusikan kembali dengan *embedding* warna yang dipakai ulang, lalu jaringan residu (empat lapis terhubung penuh) memprediksi koreksi pose. Prosedur diulang K = 2 kali; pose akhir adalah komposisi seluruh koreksi. Modul ini baru mulai dilatih setelah jaringan utama konvergen, karena prediksi pada awal pelatihan terlalu bising untuk dipelajari koreksinya.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur. YCB-Video memuat 21 objek pada 92 video RGB-D: 80 video untuk pelatihan, 2.949 *keyframe* dari 12 video sisanya untuk pengujian, ditambah 80.000 citra sintetis yang sama dengan yang dipakai PoseCNN. LineMOD memuat 13 objek bertekstur rendah. Metriknya: ADD adalah rata-rata jarak antara titik-titik model 3D yang ditransformasikan pose prediksi dan pose kebenaran; ADD-S memakai jarak ke titik terdekat sehingga adil bagi objek simetris. Pada YCB-Video dilaporkan AUC (luas di bawah kurva akurasi sampai ambang 0,1 m) dan persentase prediksi dengan ADD-S di bawah 2 cm; ambang 2 cm dipilih karena mendekati toleransi cengkeraman robot pada umumnya.

Hasil utama pada YCB-Video: varian lengkap mengalahkan PoseCNN+ICP sebesar 3,5% pada metrik ADD-S<2cm, dan varian tanpa *refinement* pun sudah mengunggulinya. Perbaikan ini terjadi justru pada tingkat presisi yang relevan untuk manipulasi. Uji ablasi menunjukkan kedua varian fusi padat mengungguli PointFusion dengan selisih besar; keunggulan dengan demikian berasal dari fusi lokal, bukan sekadar arsitektur yang lebih baru. *Refinement* paling membantu objek simetris tak bertekstur: akurasi mangkuk naik 29%, pisang 6%, dan *extra large clamp* 6%. Pada uji oklusi, kinerja DenseFusion hanya turun sekitar 2% ketika tingkat keterhalangan naik, sedangkan PoseCNN+ICP dan PointFusion menurun signifikan — bukti kuantitatif bahwa prediksi per titik menahan oklusi. Kecepatannya 16 FPS dengan rata-rata lima objek per *frame*, sekitar 200 kali lebih cepat daripada PoseCNN+ICP yang sebagian besar waktunya habis pada tahap ICP.

Pada LineMOD, varian per piksel tanpa *refinement* sudah 7% di atas metode pemurnian kedalaman terbaik saat itu, dan *refinement* menambah 8% lagi; rata-rata perbaikan galat ADD setelah dua iterasi adalah 0,8 cm. Uji robot memakai Toyota HSR bersensor Asus Xtion — berbeda dari Kinect-v2 pada data latih — dengan 60 percobaan mengangkat lima objek YCB; 73% berhasil. Objek tersulit adalah pisang (7 dari 12 percobaan), yang menurut penulis disebabkan model pisang pada eksperimen berbeda penampakan dari model pada data latih.

## Kelebihan dan Keterbatasan

Kelebihan: (1) fusi lokal per titik menjadikan estimasi tahan terhadap oklusi dan kesalahan segmentasi, terbukti dari degradasi hanya 2% pada uji oklusi; (2) seluruh komponen utama dapat dilatih *end-to-end* tanpa tahap ICP; (3) kecepatan hampir *real-time* pada 16 FPS; (4) model berpindah lintas sensor (Kinect-v2 ke Asus Xtion) tanpa penyetelan ulang pada uji robot.

Keterbatasan: (1) metode bersifat *instance-level* — hanya berlaku untuk objek yang model CAD-nya tersedia; (2) ia bergantung pada hasil segmentasi, dan repositori resmi mencatat kebingungan detektor antara objek *large clamp* dan *extra large clamp* yang menurunkan skor keseluruhan; (3) pelatihan bertahap dua — modul *refinement* baru dilatih setelah jaringan utama konvergen — memperumit reproduksi; (4) dari sisi rekayasa, *loss* objek simetris memerlukan pencarian tetangga terdekat per piksel yang menurut dokumentasi resmi sangat lambat di CPU, sehingga praktis membutuhkan GPU; (5) kegagalan pada pisang menunjukkan sensitivitas terhadap ketidakcocokan penampakan antara model dan objek nyata.

## Kaitan dengan Bab Lain

DenseFusion berdiri langsung di atas [PoseCNN](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md) (bab 073): jaringan segmentasinya dipakai apa adanya, protokol data YCB-Video beserta pembagian latih-ujinya diikuti persis, dan tahap ICP PoseCNN menjadi sasaran penggantian. Garis penerusnya terlihat pada bab-bab berikutnya dalam klaster ini: [PVN3D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md) (bab 075) memindahkan gagasan prediksi per titik ke pemungutan suara *keypoint* murni pada *point cloud* 3D; [FFB6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md) (bab 076) memperdalam fusi RGB-D dengan pertukaran fitur dua arah pada setiap skala; sedangkan [FoundationPose](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md) (bab 078) menandai peralihan ke model fondasi yang melonggarkan asumsi ketersediaan model CAD per objek. Perbandingan menyeluruh antarmetode dapat dibaca pada [bab 079](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md).

## Poin untuk Sitasi

Kutip dengan kunci `wang2019densefusion`. Ringkasan yang aman dikutip: "DenseFusion mengestimasi pose 6D dari citra RGB-D dengan memfusikan fitur warna dan geometri secara padat per piksel, memprediksi satu pose per titik beserta skor kepercayaan yang dipelajari secara mandiri, lalu memurnikan hasilnya dengan jaringan *refinement* iteratif. Metode ini mengungguli PoseCNN yang dimurnikan ICP pada tolok ukur YCB-Video dan LineMOD, dengan inferensi hampir *real-time* (16 FPS)."

Catatan verifikasi: klaim "3,5% pada ADD-S<2cm", "sekitar 200 kali lebih cepat", "16 FPS", "7% lalu 8% pada LineMOD", "0,8 cm", "73% keberhasilan pegangan", serta rincian arsitektur (ResNet-18, embedding 128 dimensi, w = 0,01, dua iterasi) tertulis eksplisit pada teks naskah arXiv:1901.04780. Nilai per objek dan agregat pada Tabel 1–3 naskah (antara lain AUC keseluruhan dan rincian waktu per komponen) tidak dikutip pada bab ini karena tabel tidak tersedia dalam bentuk teks pada sumber yang diakses; cocokkan ke PDF naskah sebelum mengutip angka tersebut.
