# 092 - Joint 3D Proposal Generation and Object Detection from View Aggregation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ku2018avod` |
| Judul asli | Joint 3D Proposal Generation and Object Detection from View Aggregation |
| Penulis | Jason Ku, Melissa Mozifian, Jungwook Lee, Ali Harakeh, Steven L. Waslander |
| Tahun | 2018 |
| Venue | IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2018) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1712.02294
- **Kode sumber:** https://github.com/kujason/avod
- **Google Scholar:** https://scholar.google.com/scholar?q=Joint%203D%20Proposal%20Generation%20and%20Object%20Detection%20from%20View%20Aggregation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Joint%203D%20Proposal%20Generation%20and%20Object%20Detection%20from%20View%20Aggregation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan AVOD (*Aggregate View Object Detection*), detektor objek 3D untuk kendaraan otonom yang menggabungkan citra RGB dan *point cloud* (himpunan titik koordinat 3D) dari sensor LiDAR pada tahap pembangkitan proposal, bukan hanya pada tahap deteksi akhir. Fusi dilakukan di dalam satu *Region Proposal Network* (RPN, jaringan pengusul wilayah) yang menerima fitur dari kedua modalitas sekaligus, dengan peta fitur beresolusi tinggi yang dijaga tetap detail melalui arsitektur *encoder-decoder* bergaya *Feature Pyramid Network* (FPN, jaringan piramida fitur yang menggabungkan peta fitur kasar dan halus). Tujuannya adalah memperbaiki deteksi objek kecil seperti pejalan kaki dan pesepeda, yang pada pendekatan fusi lambat sebelumnya sering hilang akibat fitur yang terlalu diperkecil resolusinya.

Pada tolok ukur KITTI, AVOD mencapai *average precision* (AP, presisi rata-rata di seluruh ambang deteksi) 3D sebesar 71,88% untuk kelas mobil tingkat kesulitan moderat, mengungguli MV3D (bab 091) dan bersaing ketat dengan metode berbasis titik F-PointNet. Model berjalan pada 0,10 detik per citra (10 Hz) dengan memori GPU sekitar 2 GB saat inferensi dan hanya 38,073 juta parameter — sekitar 16% dari ukuran MV3D. Kombinasi akurasi, kecepatan, dan efisiensi memori inilah yang menjadi klaim utama makalah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

MV3D (bab 091), pendahulu langsung AVOD, memfusikan fitur dari *bird's-eye view* (BEV, proyeksi tampak-atas *point cloud*), tampak depan LiDAR, dan citra RGB, tetapi baru menggabungkan ketiganya pada tahap deteksi akhir setelah setiap cabang melalui banyak lapis *pooling* (penyatuan spasial yang mengecilkan peta fitur). Akibatnya, peta fitur yang dipakai untuk mengusulkan wilayah objek sudah kehilangan resolusi spasial jauh sebelum informasi antar-modalitas sempat digabung. Objek besar seperti mobil masih cukup tercakup pada peta fitur yang mengecil, tetapi objek kecil seperti pejalan kaki dan pesepeda — yang pada BEV hanya menempati beberapa piksel — mudah hilang sebelum fusi terjadi.

Masalah kedua adalah efisiensi memori. Deteksi 3D memerlukan jumlah *anchor* (kotak referensi berukuran dan berposisi tetap yang dipakai sebagai titik awal regresi) yang jauh lebih banyak daripada deteksi 2D, karena ruang pencarian mencakup posisi x, y, z serta orientasi. MV3D memakai representasi kotak 3D dengan 8 sudut (24 angka per kotak), sehingga jaringan pada tahap kedua menjadi berat dan boros memori ketika jumlah proposal besar. Ketiga, penyelarasan spasial antara fitur BEV dan fitur citra RGB pada resolusi tinggi bukan hal sepele: kedua modalitas memiliki geometri proyeksi yang berbeda, sehingga menyatukan fitur keduanya secara akurat memerlukan mekanisme pemetaan koordinat yang eksplisit.

## Ide Utama

AVOD mengusulkan tiga perubahan atas kerangka MV3D. Pertama, fusi BEV-RGB dipindahkan ke tahap paling awal yang mungkin, yaitu di dalam RPN itu sendiri, sehingga proposal 3D sudah mempertimbangkan kedua modalitas sejak awal, bukan hanya divalidasi ulang di tahap akhir. Kedua, setiap modalitas diproses oleh ekstraktor fitur *encoder-decoder* yang menghasilkan peta fitur beresolusi penuh (sama dengan resolusi masukan), bukan peta fitur yang telah menyusut delapan kali lipat seperti pada jaringan klasifikasi biasa. Resolusi penuh ini penting karena objek kecil pada BEV bisa jadi hanya berukuran beberapa piksel setelah beberapa kali *pooling*; menjaga resolusi berarti menjaga informasi itu tetap ada saat fusi dilakukan.

Ketiga, representasi kotak 3D disederhanakan. Alih-alih meregresi delapan sudut kotak (24 angka) seperti MV3D, AVOD meregresi empat sudut BEV ditambah dua nilai tinggi (10 angka), karena kotak 3D beraturan pada dasarnya adalah persegi panjang BEV yang diberi tinggi — merepresentasikan lebih banyak angka daripada derajat kebebasan sebenarnya justru menambah kesempatan jaringan melakukan kesalahan yang saling bertentangan secara geometris. Orientasi kotak diregresi terpisah sebagai vektor (cos θ, sin θ) agar tidak ada ambiguitas sudut di sekitar ±π (nilai sudut yang berlawanan arah tetapi secara numerik terpisah jauh).

## Cara Kerja Langkah demi Langkah

### Representasi Data Masukan

*Point cloud* LiDAR diproyeksikan menjadi peta BEV beresolusi 0,1 meter per piksel, mencakup wilayah 80×70 meter di sekitar kendaraan. Peta ini memiliki enam kanal: lima kanal ketinggian (setiap kanal merepresentasikan irisan ketinggian 0 sampai 2,5 meter yang dibagi rata) ditambah satu kanal kerapatan titik. Citra RGB dipakai apa adanya tanpa proyeksi ulang. Kedua masukan ini diproses oleh dua ekstraktor fitur terpisah namun berarsitektur identik.

### Ekstraksi Fitur Beresolusi Tinggi

Setiap ekstraktor memakai VGG-16 (jaringan konvolusi 16 lapis) yang dimodifikasi: jumlah kanal setiap lapis dipangkas separuh, dan jaringan dipotong pada blok konvolusi keempat. Bagian *encoder* ini mengecilkan peta fitur menjadi 1/8 dari resolusi masukan. Bagian *decoder* kemudian mengembalikan resolusi secara bertahap memakai konvolusi transpos (operasi kebalikan konvolusi yang memperbesar peta fitur), digabungkan dengan fitur *encoder* pada resolusi yang sama, lalu disaring ulang dengan konvolusi 3×3 — pola yang sama dengan FPN. Keluarannya adalah peta fitur beresolusi penuh untuk BEV maupun RGB, masing-masing telah membawa informasi semantik dari lapis dalam sekaligus detail spasial dari lapis dangkal.

### Pembangkitan dan Reduksi Anchor 3D

*Anchor* 3D disebar pada kisi BEV dengan jarak 0,5 meter; ukuran (panjang, lebar, tinggi) setiap kelas ditentukan dari statistik data latih, sedangkan posisi ketinggian mengikuti elevasi sensor. Jumlah *anchor* per citra berkisar 80.000–100.000 sebelum penyaringan. *Anchor* yang jatuh pada wilayah kosong (tidak ada titik LiDAR) dibuang lebih dulu memakai *integral image* (teknik penjumlahan kumulatif untuk menghitung isi suatu wilayah secara cepat), sehingga jumlah *anchor* yang benar-benar dievaluasi jauh berkurang. Sebelum masuk RPN, kedalaman peta fitur juga direduksi memakai konvolusi 1×1, karena dengan puluhan ribu *anchor*, penyimpanan fitur berdimensi penuh untuk setiap *anchor* akan membengkakkan memori.

### Fusi Fitur pada RPN

Untuk setiap *anchor*, operasi *crop-and-resize* (memotong wilayah peta fitur sesuai proyeksi *anchor*, lalu mengubah ukurannya ke dimensi tetap dengan interpolasi) diterapkan pada kedua peta fitur — BEV dan RGB — menghasilkan potongan berukuran 3×3 dari masing-masing modalitas. Kedua potongan ini digabung dengan **fusi rata-rata elemen-per-elemen** (menjumlah nilai fitur bersesuaian dari kedua modalitas lalu membaginya dua). Hasil fusi diteruskan ke dua cabang *fully connected* berukuran 256 unit: satu memprediksi skor objektif (ada objek atau tidak) lewat *cross-entropy*, satu lagi meregresi pergeseran posisi dan dimensi kotak (Δx, Δy, Δz, Δpanjang, Δlebar, Δtinggi) lewat *Smooth L1 loss* (fungsi galat regresi yang tidak terlalu sensitif terhadap nilai pencilan). Proposal yang tumpang tindih dirampingkan dengan *Non-Maximum Suppression* pada ambang IOU 0,8 di BEV, menyisakan 1.024 proposal saat pelatihan dan 300–1.024 proposal per kelas saat inferensi.

Diagram berikut merangkum alur data dari kedua modalitas sampai kotak 3D akhir:

```
BEV LiDAR (6 kanal)              Citra RGB
      |                               |
      v                               v
 Encoder-Decoder VGG-16        Encoder-Decoder VGG-16
 (fitur resolusi penuh)        (fitur resolusi penuh)
      |                               |
      +---------------+---------------+
                      v
        RPN: crop-and-resize 3x3
        per anchor, fusi rata-rata
                      |
                      v
     ~1.024 proposal 3D (NMS BEV, IOU 0,8)
                      |
                      v
     crop-and-resize 7x7, fusi rata-rata
                      |
                      v
   3 lapis FC (2.048 unit): kotak 4-sudut
   + 2 tinggi, orientasi (cos θ, sin θ), kelas
```

### Tahap Kedua: Regresi Kotak dan Orientasi

Proposal yang lolos dipotong kembali dari peta fitur (kali ini berukuran 7×7, dengan kedalaman fitur direduksi ke 32 kanal) dan difusikan dengan cara yang sama, rata-rata elemen-per-elemen. Tiga lapis *fully connected* berukuran 2.048 unit kemudian memprediksi tiga hal: regresi kotak 3D dalam format 4-sudut-plus-2-tinggi, vektor orientasi (cos θ, sin θ), dan probabilitas kelas. Sudut akhir kotak ditentukan dengan mencocokkan sudut BEV yang paling dekat dengan arah vektor orientasi yang diregresi, sehingga ambiguitas arah terselesaikan tanpa perlu memprediksi sudut secara langsung dalam radian.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tolok ukur KITTI 3D Object Detection, dengan metrik AP 3D dan AP BEV pada tiga tingkat kesulitan (mudah, moderat, sulit) dan ambang IOU 0,7 untuk mobil serta 0,5 untuk pejalan kaki dan pesepeda. Pada set uji, untuk kelas mobil AVOD mencapai AP 3D 81,94% (mudah), 71,88% (moderat), dan 66,38% (sulit), dengan waktu proses 0,10 detik per citra pada GPU Titan Xp. Sebagai pembanding, MV3D memerlukan 0,36 detik dan memperoleh AP 3D moderat 62,35%; VoxelNet 0,23 detik dengan 65,11%; F-PointNet 0,17 detik dengan 70,39%. AVOD dengan demikian unggul pada akurasi mobil sekaligus lebih cepat 1,7 kali dibandingkan F-PointNet.

| Kelas | AP 3D Mudah | AP 3D Moderat | AP 3D Sulit |
|---|---|---|---|
| Mobil | 81,94% | 71,88% | 66,38% |
| Pejalan kaki | 50,80% | 42,81% | 40,88% |
| Pesepeda | 64,00% | 52,18% | 46,61% |

Untuk pejalan kaki, AVOD sedikit lebih unggul daripada F-PointNet pada AP BEV, tetapi tertinggal tipis pada AP 3D moderat (42,81% berbanding 44,89%). Untuk pesepeda, AVOD tertinggal lebih jauh dari F-PointNet (52,18% berbanding 56,77% pada moderat); penulis mengaitkan selisih ini dengan bias jumlah contoh pesepeda yang sedikit pada data latih KITTI, bukan kelemahan arsitektural yang mendasar. Studi ablasi pada set validasi menunjukkan bahwa penggantian ekstraktor fitur biasa dengan arsitektur *encoder-decoder* beresolusi tinggi menaikkan AP moderat pejalan kaki dan pesepeda secara signifikan, sementara fusi RGB pada RPN (dibandingkan RPN yang hanya memakai BEV) menambah beberapa poin persentase AP pada kedua kelas objek kecil tersebut — mengonfirmasi bahwa resolusi tinggi dan fusi dini memang menyasar persoalan objek kecil yang menjadi motivasi utama makalah. Dari sisi efisiensi, model memiliki 38,073 juta parameter (sekitar 16% dari ukuran MV3D) dan memerlukan sekitar 231,263 miliar operasi hitung (FLOPs) per citra, dengan penggunaan memori GPU sekitar 2 GB saat inferensi.

## Kelebihan dan Keterbatasan

Kelebihan AVOD meliputi kecepatan *real-time* (10 Hz) dengan jejak memori rendah, cocok untuk perangkat keras kendaraan otonom yang terbatas; akurasi mobil yang melampaui MV3D dan VoxelNet; representasi kotak 3D yang lebih ringkas dan konsisten secara geometris dibandingkan format 8-sudut MV3D; serta perbaikan nyata pada deteksi objek kecil berkat fusi dini dan fitur beresolusi tinggi. Regresi orientasi lewat vektor (cos θ, sin θ) juga menghindari kegagalan umum pada metode yang meregresi sudut secara langsung.

Keterbatasan yang diakui penulis adalah kinerja pesepeda yang masih di bawah metode berbasis titik seperti F-PointNet, yang dikaitkan dengan kelangkaan contoh pada data latih. Dari sisi rekayasa, arsitektur dua tahap (RPN diikuti jaringan penyempurnaan) tetap menanggung biaya komputasi tambahan dibandingkan detektor satu tahap, meski AVOD sudah jauh lebih efisien daripada pendahulunya. Secara konseptual, representasi BEV dengan lima irisan ketinggian tetap merupakan diskritisasi kasar terhadap struktur vertikal sesungguhnya, sehingga objek dengan variasi ketinggian halus (misalnya bagian tubuh pejalan kaki) tidak seluruhnya terekam sebelum fusi terjadi. Metode ini juga bergantung pada kalibrasi geometris yang akurat antara LiDAR dan kamera, karena operasi *crop-and-resize* memerlukan proyeksi titik 3D yang tepat ke kedua bidang citra.

## Kaitan dengan Bab Lain

AVOD merupakan penyempurnaan langsung atas [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md): keduanya memakai BEV LiDAR dan RGB, tetapi AVOD memindahkan titik fusi ke tahap proposal dan mengganti ekstraktor fitur dengan arsitektur beresolusi tinggi. Prinsip menjaga resolusi fitur untuk objek kecil sejalan dengan gagasan [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md), yang menyelesaikan masalah serupa lewat pendekatan berbasis titik alih-alih fusi peta fitur. Gagasan fusi LiDAR-kamera pada resolusi tinggi ini kemudian diteruskan dan diperluas oleh metode yang lebih baru pada klaster yang sama, termasuk [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md) dan [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md), yang masing-masing mengusulkan skema fusi lain antara citra dan *point cloud*.

## Poin untuk Sitasi

Kutip dengan kunci `ku2018avod`. Ringkasan yang aman dikutip: "AVOD memfusikan fitur BEV LiDAR dan RGB pada tahap pengusulan proposal memakai ekstraktor fitur beresolusi tinggi bergaya FPN, mencapai AP 3D 71,88% pada kelas mobil tingkat moderat di KITTI dengan waktu proses 0,10 detik per citra dan 38,073 juta parameter." Angka-angka AP 3D/BEV per kelas, jumlah parameter (38,073 juta), FLOPs (231,263 miliar), memori GPU (2 GB), serta rincian studi ablasi diperoleh dari pembacaan otomatis naskah arXiv dan sebaiknya dicocokkan ulang dengan tabel asli sebelum dikutip dalam karya formal, khususnya nilai *Average Heading Similarity* (AHS) dan angka ablasi per komponen yang tidak direproduksi lengkap di bab ini.
