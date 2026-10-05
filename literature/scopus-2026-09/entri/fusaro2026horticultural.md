# Horticultural temporal fruit monitoring via 3D instance segmentation and re-identification using colored point clouds

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fusaro2026horticultural` |
| Judul asli | Horticultural temporal fruit monitoring via 3D instance segmentation and re-identification using colored point clouds |
| Penulis | Fusaro, Daniel; Magistri, Federico; Behley, Jens; Pretto, Alberto; Stachniss, Cyrill |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, strawberry |

## Tautan Akses
- PDF: [fusaro2026horticultural.pdf](../pdf/fusaro2026horticultural.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111723

## Gambaran Umum
Makalah ini mengusulkan metode segmentasi instans (*instance segmentation*) buah dan identifikasi ulang (*re-identification*) buah yang sama pada awan titik 3D berwarna yang direkam pada waktu berbeda. Segmentasi dilakukan langsung pada awan titik dengan MinkPanoptic (modul inti MaskPLS). Setiap buah hasil segmentasi diubah menjadi deskriptor ringkas oleh jaringan saraf konvolusi jarang 3D (*sparse convolutional neural network*). Pencocokan antarwaktu dilakukan oleh jaringan pencocok berbasis atensi yang memprediksi distribusi probabilitas atas kandidat buah pada sesi sebelumnya, dengan kelas "tidak cocok" (*no-match*) yang eksplisit, lalu diselesaikan dengan penugasan rakus (*greedy*).

Data berupa awan titik stroberi dari pemindai laser terestrial Faro Focus3D-X130 di rumah kaca komersial (satu baris tanaman, tiga waktu pengamatan dengan selang sekitar satu minggu) dan awan titik apel Fuji dari dataset PFuji-Size yang dibangun dari fotogrametri citra RGB. Segmentasi diuji pada kedua dataset, sedangkan identifikasi ulang hanya pada dataset stroberi karena hanya dataset itu memiliki anotasi koherensi waktu.

Pada segmentasi, rerata PQ semua kelas dan dataset adalah 75,1% untuk MinkPanoptic dan 65,8% untuk Superpoint Transformer; untuk kelas buah saja PQ-nya 52,3% berbanding 36,8%. Pada identifikasi ulang dengan segmentasi MinkPanoptic, metode ini mencapai rerata mF1 65,1%, dibanding 55,3% untuk pencocok tetangga terdekat (*nearest neighbor*, NN) dan 51,3% untuk Riccardi dkk. Dengan anotasi *ground truth* sebagai masukan, NN justru lebih tinggi (mF1 79,9% berbanding 63,9%).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan buah yang konsisten dari waktu ke waktu diperlukan untuk fenotipe (*phenotyping*), analisis pola pertumbuhan, dan estimasi laju pematangan. Tugas ini sulit karena buah bervariasi dalam ukuran, bentuk, oklusi, dan orientasi, dan karena buah dapat muncul atau hilang (dipanen atau jatuh) di antara dua pengamatan. Buah tidak memiliki ciri unik yang mudah dibedakan, tersusun rapat, dan posisinya dapat berubah banyak, sehingga solusi sederhana berbasis posisi relatif dapat gagal.

Pendekatan berbasis citra 2D tidak memiliki informasi struktur, kedalaman, dan spasial 3D, sedangkan awan titik tidak berstruktur grid sehingga pengolahan citra konvensional tidak dapat dipakai langsung. Penulis menyatakan bahwa sepengetahuan mereka belum ada karya yang secara khusus menangani segmentasi instans buah 3D langsung pada awan titik, dan bahwa Riccardi dkk. adalah satu-satunya karya terbuka untuk identifikasi ulang buah pada awan titik. Metode segmentasi 3D mutakhir pun dilaporkan kesulitan bila data latih kecil.

## Ide Utama
Gagasan utamanya adalah memisahkan dua modul yang dilatih terpisah: segmentasi instans dan identifikasi ulang. Pemisahan ini dinyatakan memudahkan penggantian modul segmentasi dengan metode lain. Deskriptor buah dihitung dari awan titik pendukung (*support point cloud*) berjari-jari tetap di sekitar pusat buah, sehingga konteks sekitar buah ikut terbawa. Pencocokan memakai deskriptor kueri, deskriptor kandidat dari sesi sebelumnya, dan posisi relatif 3D di antara keduanya sebagai pengkodean posisi.

Kasus buah baru atau tidak terlihat ditangani dengan menambahkan deskriptor berisi nol sebagai kandidat "tidak cocok". Asumsi bahwa buah tidak bergerak lebih dari ambang $h$ antarpindaian diterapkan dengan menolkan probabilitas kandidat yang pusatnya lebih jauh dari $h$. Pelatihan menambahkan suku kerugian injektif agar pemetaan antarbuah bersifat satu-ke-satu.

## Cara Kerja Langkah demi Langkah

```
 awan titik berwarna P --> MinkPanoptic (offset + mean shift) --> instans buah
 instans buah --> awan titik pendukung (radius s) --> voxel --> MinkowskiNet
              --> global average pooling --> deskriptor d_i
 d_i (kueri) + D(t-1) + posisi relatif --> transformer --> softmax
              --> mask jarak h --> argmax / penugasan rakus --> y
```

### 1. Akuisisi data
Dataset stroberi (dari Riccardi dkk.) direkam dengan pemindai laser Faro Focus3D-X130 di rumah kaca komersial. Dataset ini berisi baris tanaman yang sama pada tiga waktu (P1, P2, P3) dengan selang sekitar satu minggu. Anotasi *ground truth* berjumlah 616 (P1), 556 (P2), dan 159 (P3) stroberi. Pada asosiasi P2 ke P1, 56 stroberi tidak memiliki pasangan; pada asosiasi P3 ke P2, 5 stroberi tidak memiliki pasangan. Awan titik dibangun dari penyelarasan beberapa pandang pemindaian sehingga sebagian besar bebas oklusi.

PFuji-Size berisi citra RGB resolusi tinggi dan awan titik fotogrametri pohon apel Fuji di lapangan, dengan anotasi pusat dan radius buah. Akuisisi 2018 dipakai untuk latih dan validasi, akuisisi 2020 untuk uji. Karena sebagian buah pada dua pohon pertama koleksi 2020 tidak teranotasi, hanya pohon ketiga yang dipakai untuk uji. Jumlah buah apel tidak dilaporkan pada teks yang tersedia.

### 2. Segmentasi instans
MinkPanoptic memprediksi label semantik buah serta vektor offset tiap titik buah ke pusat instansnya. Titik yang telah digeser oleh offset dikelompokkan dengan algoritma *mean shift* untuk memperoleh instans. Pelatihan mengikuti Marcuzzi dkk. dengan kerugian $L_{ins} = L_{sem} + \lambda_{off} L_{off}$; $L_{sem}$ gabungan *cross-entropy* dan Lovász-Softmax. Model dilatih dari awal. Pada dataset stroberi, laju belajar awal 0,01 dan koefisien peluruhan 0,97; pada apel, 0,03 dan 0,97. Lebar pita (*bandwidth*) *mean shift* dipilih pada set validasi: 0,01125 m untuk stroberi dan 0,035 m untuk apel. Waktu pelatihan sekitar 2 jam per dataset dan waktu inferensi 100 ms per 100 ribu titik.

Pada stroberi, MinkPanoptic dilatih dengan P1 sebagai set latih dan P2 sebagai validasi, lalu diuji pada P3. Dari tiga awan titik asli diambil 800 potongan latih dan 200 validasi dengan memotong di sekitar titik benih acak di baris tanaman. Lebar potongan 0,3 m dan ukuran voksel 0,0005 m untuk MinkPanoptic, sedangkan Superpoint Transformer memakai 0,15 m dan 0,001 m.

### 3. Ekstraksi deskriptor buah
Awan titik pendukung $S_i$ (semua titik dalam radius $s$ = 0,2 m dari pusat buah) divoksel dengan ukuran $v$ = 5·10⁻⁴ m, lalu diproses encoder MinkowskiNet: dua konvolusi jarang awal dengan *batch normalization* dan ReLU, kemudian $L$ = 4 blok dengan penurunan resolusi stride 2 dan jalur residu. Dimensi tersembunyi adalah 8, 8, 16, 16, dan 64. *Global average pooling* menghasilkan deskriptor $d_i \in \mathbb{R}^z$. Augmentasi mencakup rotasi acak $\pm 30^\circ$ pada tiap sumbu, derau posisi, dan derau warna.

### 4. Pencocokan dan penugasan
Deskriptor kueri digabungkan dengan setiap deskriptor sesi sebelumnya, ditambah pengkodean posisional dari posisi relatif $T$ sesuai Mildenhall dkk. Baris nol untuk kelas "tidak cocok" ditambahkan, lalu lapisan linear dan satu lapisan *transformer encoder* (dimensi masukan 512, *feedforward* 1.024, 8 kepala atensi) menghasilkan logit yang dinormalkan dengan softmax. Kandidat yang pusatnya lebih jauh dari $h$ = 0,05 m dimasking. Untuk banyak buah sekaligus, pasangan paling mungkin dipilih terlebih dahulu secara rakus dan dikeluarkan dari kumpulan kandidat. Kerugian pencocokan adalah $L_m = L_{ce} + \lambda_{inj} L_{inj}$ dengan bobot $\lambda_{ce}$ = 2, $\lambda_{Lov}$ = 10, $\lambda_{off}$ = 10, dan $\lambda_{inj}$ = 0,08; laju belajar tetap 3·10⁻⁴. Set latih $\hat{F}_1$, $\hat{F}_2$ dibagi manual berdasarkan posisi 3D menjadi sekitar 80% latih dan sisanya validasi.

## Eksperimen dan Hasil
Segmentasi dinilai dengan IoU, *panoptic quality* (PQ) beserta komponennya *segmentation quality* (SQ) dan *recognition quality* (RQ). Identifikasi ulang dinilai dengan F1p (pasangan benar), F1n (label tidak cocok benar), dan mF1 = (F1p + F1n)/2, dengan pencocokan prediksi ke anotasi pada ambang IoU 5% sampai 30%. Pembanding adalah NN dengan ambang jarak yang disetel Optuna ($\epsilon^* = 0{,}033$ m) dan Riccardi dkk. Semua nilai dalam persen.

Tabel segmentasi (kelas buah, dari Tabel II):

| Dataset | Metode | IoU | RQ | SQ | PQ |
|---|---|---|---|---|---|
| Stroberi | Superpoint Transformer | 48,3 | 48,8 | 79,2 | 38,7 |
| Stroberi | MinkPanoptic | 80,9 | 75,8 | 84,3 | 63,8 |
| PFuji-Size (apel) | Superpoint Transformer | 39,4 | 49,2 | 71,0 | 34,9 |
| PFuji-Size (apel) | MinkPanoptic | 50,1 | 52,1 | 78,3 | 40,7 |
| Rerata kedua dataset | Superpoint Transformer | 43,9 | 49 | 75,1 | 36,8 |
| Rerata kedua dataset | MinkPanoptic | 65,5 | 64,0 | 81,3 | 52,3 |

Metode segmentasi mutakhir lain (Mask3D, MaskPLS, OneFormer3D, Spherical Mask, P3Former) dilaporkan gagal menghasilkan segmentasi yang dapat dipakai pada data kecil ini, sehingga hanya Superpoint Transformer yang dilaporkan sebagai pembanding. Alasan yang dikemukakan penulis adalah ketergantungan pada voksel yang menghilangkan detail objek kecil, biaya komputasi voksel kecil, dan kemungkinan kueri belajar yang runtuh ke representasi serupa.

Tabel identifikasi ulang (rerata ambang 5% sampai 30% dan baris *ground truth*, dari Tabel III):

| Segmentasi | Metode | F1p | F1n | mF1 |
|---|---|---|---|---|
| MinkPanoptic (rerata) | NN | 73,0 | 37,7 | 55,3 |
| MinkPanoptic (rerata) | Riccardi dkk. | 71,9 | 30,8 | 51,3 |
| MinkPanoptic (rerata) | Metode ini | 75,8 | 54,4 | 65,1 |
| Superpoint Transformer (rerata) | NN | 70,9 | 20,7 | 45,8 |
| Superpoint Transformer (rerata) | Riccardi dkk. | 61,7 | 6,7 | 34,2 |
| Superpoint Transformer (rerata) | Metode ini | 68,2 | 35,2 | 51,7 |
| Anotasi *ground truth* | NN | 84,7 | 75,0 | 79,9 |
| Anotasi *ground truth* | Riccardi dkk. | 92,6 | 0,0 | 46,3 |
| Anotasi *ground truth* | Metode ini | 76,4 | 51,4 | 63,9 |

Dengan segmentasi MinkPanoptic, metode ini unggul dalam rerata mF1 sebesar 9,8 poin dari pesaing terbaik kedua; dengan Superpoint Transformer unggul 5,9 poin. Pada segmentasi Superpoint Transformer, NN memiliki F1p tertinggi (70,9) tetapi F1n rendah (20,7). Penulis menyebut metode mereka lebih baik dalam membedakan pasangan negatif, yang banyak muncul akibat segmentasi kasar. Pada masukan *ground truth*, NN dan Riccardi dkk. mengungguli metode ini pada F1p dan, untuk NN, juga pada mF1. Akurasi turun seiring ambang IoU naik; contohnya mF1 metode ini pada MinkPanoptic adalah 72,7 pada ambang 5% dan 55,2 pada ambang 30%.

Ablasi segmentasi menunjukkan PQ validasi berbentuk hampir parabola terhadap lebar pita *mean shift*, dan lebar pita terbaik tidak sama dengan radius rerata buah pada set validasi. Ablasi identifikasi ulang (validasi silang 5 lipatan, empat benih acak) memilih konfigurasi dimensi tersembunyi [8, 8, 16, 16, 64] dengan *feedforward* 512, mF1 61,2%, F1p 75,5%, dan F1n 47,0%. Penambahan deskriptor tetangga berbasis graf (GCNConv atau EdgeConv) tidak meningkatkan mF1: GCNConv mencapai 61,0%, 0,2 poin di bawah metode tanpa graf. Waktu pemrosesan 200 stroberi sepanjang sekitar 2 m baris tanaman adalah sekitar 1,2 detik pada GPU NVIDIA TITAN RTX; pelatihan modul deskriptor dan pencocokan kurang dari 1 jam.

## Kelebihan dan Keterbatasan
Penulis menyatakan bahwa kinerja identifikasi ulang bergantung pada mutu segmentasi karena buah yang menyatu atau deteksi palsu merambat ke tahap pencocokan. Identifikasi ulang hanya dievaluasi pada dataset stroberi karena tidak tersedia dataset lain dengan anotasi instans yang konsisten waktu. Ketergantungan pada data LiDAR resolusi tinggi dapat membatasi penerapan di lingkungan dengan sumber daya terbatas, dan penulis mengusulkan sensor berbiaya lebih rendah atau gabungan data 2D dan 3D sebagai pekerjaan lanjutan. Penulis juga mencatat bahwa awan titik kedua dataset sebagian besar bebas oklusi karena integrasi multi-pandang. Kode tersedia terbuka di repositori IRIS3D.

Menurut pembacaan ringkasan ini, identifikasi ulang diuji pada satu baris tanaman dengan hanya tiga waktu pengamatan, dan set uji (P3) hanya berisi 159 anotasi stroberi sehingga selisih antarmetode dapat peka terhadap satu sesi tertentu. Menurut pembacaan ringkasan ini, pada masukan *ground truth* metode NN lebih tinggi daripada metode usulan, sehingga keunggulan yang dilaporkan terutama berlaku pada skenario segmentasi hasil prediksi. Menurut pembacaan ringkasan ini, makalah tidak melaporkan simpangan baku antarbenih untuk tabel hasil uji akhir, dan metode segmentasi pembanding hanya satu.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang sama pada beberapa pengamatan: buah yang sama pada pindaian berbeda waktu dicocokkan lewat deskriptor 3D yang dipelajari, pengkodean posisi relatif, dan penugasan rakus satu-ke-satu dengan kelas "tidak cocok" untuk buah yang dipanen, jatuh, atau muncul baru. Mekanisme ini adalah pencocokan antarwaktu pada awan titik 3D, bukan pelacakan video. Hitungan per kelas tidak dilaporkan karena hanya ada satu kelas buah. Acuan evaluasi adalah anotasi pada awan titik (anotasi instans dan asosiasi antarwaktu), bukan hasil panen maupun hitungan manual di lapangan.

Untuk pencacahan tandan kelapa sawit multi-sisi, gagasan yang dapat dipindahkan adalah formulasi pencocokan dengan kelas "tidak cocok" dan penugasan satu-ke-satu, serta penggunaan posisi relatif sebagai petunjuk pencocokan. Pemindahan langsung terbatas karena metode bergantung pada awan titik padat berwarna dari pemindai laser dan pada asumsi buah tidak bergerak lebih dari 0,05 m antarpindaian. Pada pencacahan lintas sisi pohon, posisi buah antarpandang tidak berada pada kerangka koordinat yang sama tanpa registrasi 3D. Makalah tidak menguji tanaman kelapa sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `fusaro2026horticultural`.

Fusaro dkk. mengusulkan metode segmentasi instans dan identifikasi ulang buah pada awan titik 3D berwarna yang direkam pada waktu berbeda, dengan segmentasi MinkPanoptic, deskriptor konvolusi jarang 3D, dan pencocok berbasis atensi dengan kelas "tidak cocok". Pada dataset stroberi dari pemindai laser terestrial, metode ini mencapai rerata mF1 65,1% dengan segmentasi MinkPanoptic, dibanding 55,3% untuk pencocok tetangga terdekat dan 51,3% untuk Riccardi dkk.; pada anotasi *ground truth*, pencocok tetangga terdekat lebih tinggi (mF1 79,9% berbanding 63,9%). Segmentasi diuji juga pada apel Fuji (PFuji-Size), sedangkan identifikasi ulang hanya pada stroberi.

Catatan verifikasi data: Angka segmentasi bersumber dari Tabel II, angka identifikasi ulang dari Tabel III (baris "avg" dan "GT"), jumlah anotasi stroberi dari Tabel I, dan hasil ablasi dari Tabel IV serta seksi VI. Kutipan teks "mengungguli 9,8 poin dan 5,9 poin" tercantum di seksi IV-F, dan selisih tersebut sesuai dengan Tabel III. Ekstraksi PDF memecah tabel menjadi satu angka per baris; pembacaan Tabel II dan III dilakukan dengan menyusun ulang urutan kolom sehingga pemetaan kolom dapat keliru bila urutan ekstraksi berbeda. Pada Tabel II, nilai SQ dan PQ latar belakang untuk beberapa baris tidak konsisten antara satuan, dan hanya baris buah serta rerata yang dipakai di sini. Teks seksi VI-A menulis lebar pita 0,094 m sebagai radius rerata stroberi, sedangkan Tabel IV menulis 0,0094 m; ketidakkonsistenan ini tidak dapat diputuskan dari teks. Jumlah buah apel pada set uji dan ukuran tiap dataset apel tidak dilaporkan. Semua gambar (Gambar 1 sampai 8) tidak terbaca dari teks ekstraksi.
