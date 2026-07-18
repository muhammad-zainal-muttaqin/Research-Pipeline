# 184 - Volumetric Grasping Network: Real-Time 6 DOF Grasp Detection in Clutter

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `breyer2021vgn` |
| Judul asli | Volumetric Grasping Network: Real-Time 6 DOF Grasp Detection in Clutter |
| Penulis | Michel Breyer, Jen Jen Chung, Lionel Ott, Roland Siegwart, Juan Nieto |
| Tahun | 2020 |
| Venue | Conference on Robot Learning (CoRL 2020) |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2101.01132
- **Proceedings resmi (PMLR):** https://proceedings.mlr.press/v155/breyer21a.html
- **Kode sumber:** https://github.com/ethz-asl/vgn
- **Google Scholar:** https://scholar.google.com/scholar?q=Volumetric%20Grasping%20Network%3A%20Real-Time%206%20DOF%20Grasp%20Detection%20in%20Clutter

## Gambaran Umum

Makalah ini memperkenalkan VGN (*Volumetric Grasping Network*), jaringan konvolusi 3D yang memprediksi *grasp* (cengkeraman) 6-*DoF* (*degrees of freedom*, derajat kebebasan posisi dan orientasi di ruang 3D) langsung dari representasi volumetrik sebuah *scene* (adegan) berisi objek yang bertumpuk. Alih-alih mengevaluasi kandidat *grasp* satu per satu, VGN menerima *Truncated Signed Distance Function* (TSDF) — representasi volumetrik permukaan yang dibangun dari beberapa citra kedalaman (*depth image*) — dan mengeluarkan, dalam satu kali evaluasi jaringan, peta kualitas *grasp*, orientasi *gripper* (pencengkeram), dan lebar bukaan untuk setiap *voxel* (elemen volume, unit terkecil grid 3D) dalam volume kerja. Pendekatan ini menghasilkan waktu perencanaan sekitar 10 milidetik pada GPU, cukup cepat untuk perencanaan *closed-loop* (lingkar tertutup, keputusan diperbarui berulang dari umpan balik sensor) tanpa pemeriksaan tabrakan eksplisit. Pada uji robot nyata dengan lengan Franka Emika Panda, VGN membersihkan 92% objek dari tumpukan campuran dengan tingkat keberhasilan cengkeraman per percobaan sekitar 80%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode deteksi *grasp* 6-*DoF* pada masanya umumnya bekerja dengan skema *sample-then-evaluate* (contoh dulu, lalu nilai): sistem membangkitkan ratusan hingga ribuan kandidat pose *grasp* dari data sensor, kemudian setiap kandidat dinilai satu per satu oleh jaringan klasifikasi terpisah untuk menentukan kualitasnya. Skema ini, dipakai misalnya oleh GPD (*Grasp Pose Detection*, metode pembanding pada makalah ini yang mengevaluasi kandidat *grasp* dari *point cloud* memakai jaringan klasifikasi), mahal secara komputasi karena setiap kandidat memerlukan evaluasi jaringan sendiri, sehingga total waktu tumbuh sebanding dengan jumlah kandidat yang diuji. Akibatnya proses menjadi lambat untuk skenario yang membutuhkan keputusan cepat berulang, seperti *decluttering* (membersihkan tumpukan objek satu demi satu) di lingkungan gudang atau daur ulang.

Masalah kedua terkait representasi data. Sebagian metode grasp bekerja langsung pada *point cloud* mentah atau citra RGB-D tunggal, yang tidak secara eksplisit mengintegrasikan informasi dari berbagai sudut pandang dan rawan terhadap bagian permukaan objek yang tidak terlihat sensor (*occlusion*, penghalangan pandangan). Pendekatan berbasis grid 2D seperti GG-CNN (*Generative Grasping CNN*, metode yang memprediksi peta kualitas grasp piksel demi piksel dari satu citra kedalaman) mengatasi kecepatan lewat prediksi padat, tetapi terbatas pada *grasp* dengan orientasi searah sumbu kamera karena representasinya dua dimensi. VGN diajukan untuk menggabungkan dua kebutuhan itu sekaligus: prediksi padat (seperti GG-CNN) tetapi dalam ruang tiga dimensi penuh (6-*DoF*, bukan hanya 2D atau 4-*DoF*), dengan data yang mengintegrasikan banyak sudut pandang lewat TSDF.

## Ide Utama

Gagasan inti VGN adalah mengubah deteksi *grasp* dari masalah klasifikasi kandidat menjadi masalah regresi padat pada volume. *Scene* direpresentasikan sebagai grid TSDF: setiap *voxel* menyimpan nilai jarak bertanda (positif di luar permukaan, negatif di dalam, dipotong/*truncated* pada rentang tertentu) terhadap permukaan objek terdekat, dibangun dengan menggabungkan (*fusion*) beberapa citra kedalaman dari sudut pandang berbeda. Jaringan 3D CNN kemudian memproses seluruh grid TSDF sekaligus dan, untuk **setiap** *voxel* dalam volume, memprediksi tiga besaran: skor kualitas *grasp* (peluang keberhasilan bila *gripper* dicengkeramkan pada posisi itu), orientasi *gripper* dalam bentuk kuaternion (representasi rotasi 3D memakai empat angka, menghindari masalah *gimbal lock* pada representasi sudut Euler), dan lebar bukaan *gripper* yang sesuai. Karena keluarannya padat — mencakup seluruh volume dalam satu *forward pass* — VGN tidak perlu membangkitkan dan menilai kandidat satu per satu; kandidat terbaik cukup diambil dari *voxel* dengan skor kualitas tertinggi pada peta keluaran.

## Cara Kerja Langkah demi Langkah

### Konstruksi TSDF dari Citra Kedalaman

Sistem mengumpulkan beberapa citra kedalaman dari kamera yang bergerak mengelilingi *scene* (pada data simulasi, jumlah sudut pandang bervariasi antara satu hingga enam per adegan). Setiap citra kedalaman diintegrasikan ke grid TSDF berukuran 40×40×40 *voxel* yang mencakup ruang kerja fisik 30×30×30 sentimeter, sehingga setiap *voxel* merepresentasikan kubus berukuran 0,75×0,75×0,75 sentimeter. Proses integrasi ini menggabungkan informasi permukaan dari berbagai sudut, mengisi bagian yang terhalang pada satu sudut pandang dengan informasi dari sudut pandang lain, dan menghasilkan representasi geometri *scene* yang lebih lengkap daripada satu citra kedalaman tunggal.

### Arsitektur 3D CNN

Jaringan berbentuk *encoder-decoder* (penyandi-penyurai) tiga dimensi. Bagian *encoder* terdiri atas tiga lapis konvolusi berstride (langkah geser lebih dari satu, mengecilkan resolusi spasial) dengan 16, 32, dan 64 kanal filter berturut-turut, mengecilkan grid 40³ menjadi peta fitur berukuran 64×5³. Bagian *decoder* mengembalikan resolusi lewat tiga lapis konvolusi yang diselingi operasi *upsampling* (pembesaran resolusi) bilinear dua kali lipat pada tiap tahap, sehingga keluaran akhir kembali ke resolusi 40³. Dari peta fitur pada resolusi penuh ini, tiga cabang keluaran terpisah menghasilkan: peta kualitas *grasp* berukuran 1×40³ (satu skor per *voxel*), peta orientasi berupa kuaternion per *voxel*, dan peta lebar bukaan *gripper* per *voxel*.

Diagram berikut merangkum alur data dari citra kedalaman hingga peta *grasp*:

```
beberapa citra depth        grid TSDF 40x40x40         3D CNN (encoder-decoder)
(1-6 sudut pandang)   -->   (ruang kerja 30x30x30cm) -->  encoder: 16,32,64 filter
                                                           bottleneck: 64 x 5^3
                                                           decoder: upsample 2x, 3 lapis
                                                                    |
                                                                    v
                                        tiga peta 40x40x40, satu per voxel:
                                        - kualitas grasp (skor 0-1)
                                        - orientasi (kuaternion)
                                        - lebar bukaan gripper
                                                    |
                                                    v
                                   pilih voxel skor tertinggi -> pose grasp 6-DoF
```

### Pelatihan dan Pembangkitan Data

Data latih dibangkitkan secara sintetis memakai simulator fisika PyBullet, bukan dikumpulkan dari robot nyata. Dua strategi penataan *scene* dipakai: "*pile*" (objek dijatuhkan bebas ke dalam kotak sehingga bertumpuk acak) dan "*packed*" (objek disusun berdiri berdekatan, meniru rak atau kemasan). Jumlah objek per adegan mengikuti distribusi acak (rerata sekitar 4–5 objek), diambil dari kumpulan 303 model 3D untuk pelatihan dan 40 model terpisah untuk pengujian, guna memastikan objek uji tidak pernah dilihat model saat pelatihan. Untuk setiap adegan, kandidat *grasp* dicoba secara acak dan diberi label berhasil/gagal berdasarkan simulasi fisika parallel-jaw *gripper* (pencengkeram dua rahang sejajar) yang benar-benar mengangkat objek. Label kandidat-kandidat ini kemudian dipetakan ke *voxel* terdekat pada grid TSDF untuk membentuk target pelatihan padat. Total data latih berskala jutaan label *grasp* terseimbang antara kelas berhasil dan gagal.

### Inferensi dan Eksekusi

Saat digunakan pada robot, kamera kedalaman terpasang pada pergelangan lengan (*wrist-mounted*) menangkap beberapa citra dari sudut berbeda, TSDF dibangun, dan satu *forward pass* jaringan menghasilkan tiga peta keluaran. Sistem memilih *voxel* dengan skor kualitas tertinggi (di atas ambang tertentu) sebagai kandidat *grasp*, mengonversi indeks *voxel* dan kuaternion terkait menjadi pose 6-*DoF* dalam koordinat dunia nyata, lalu mengeksekusikannya lewat kontroler robot. Karena seluruh proses dari citra ke pose berjalan dalam orde milidetik, keputusan grasp dapat diperbarui berulang selama pergerakan lengan menuju target — inilah yang memungkinkan operasi *closed-loop*.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua lingkungan: simulasi PyBullet dan robot nyata. Pada simulasi, uji *clutter removal* (pembersihan tumpukan objek berulang hingga habis atau gagal berturut-turut) dijalankan pada skenario *pile* dan *packed* dengan variasi jumlah objek, membandingkan VGN dengan baseline GPD. Pada skenario *packed* dengan lima objek, VGN mencapai tingkat keberhasilan cengkeraman dan tingkat pembersihan (*clearance rate*, proporsi objek yang berhasil diangkat dari total objek awal) yang lebih tinggi daripada GPD; pada skenario *pile*, keunggulan VGN paling terlihat pada *clearance rate* dibandingkan GPD, sementara tingkat keberhasilan per percobaan tunggal antara keduanya lebih dekat pada beberapa kondisi. Perbedaan ini menunjukkan bahwa keunggulan VGN bukan hanya pada akurasi satu percobaan, melainkan pada konsistensi menyelesaikan seluruh tumpukan — relevan karena *decluttering* menuntut keberhasilan berturut-turut, bukan satu kali cengkeraman terisolasi.

Pada uji robot nyata memakai lengan Franka Emika Panda tujuh sumbu dengan *gripper* paralel, sepuluh putaran percobaan dijalankan dengan campuran objek rumah tangga. VGN mencatat *clearance rate* 92% (hampir seluruh objek berhasil diangkat dari tumpukan) dengan tingkat keberhasilan per percobaan cengkeraman sekitar 80%. Selisih antara kedua angka ini wajar: *clearance rate* menghitung keberhasilan akhir per objek (termasuk percobaan ulang), sedangkan tingkat keberhasilan per percobaan menghitung setiap upaya individual, sehingga objek yang gagal pada percobaan pertama masih bisa berhasil diangkat pada percobaan berikutnya berkat sifat *closed-loop* sistem. Waktu inferensi jaringan pada GPU kelas GTX 1080 Ti tercatat sekitar 10 milidetik, jauh di bawah anggaran waktu siklus kontrol robot, sehingga memungkinkan pembaruan keputusan grasp beberapa kali per detik selama pergerakan lengan.

## Kelebihan dan Keterbatasan

Kelebihan utama VGN adalah kecepatan: prediksi padat satu-*pass* menghilangkan kebutuhan mengevaluasi kandidat satu per satu, sehingga waktu perencanaan tidak bergantung pada jumlah kandidat yang dipertimbangkan. Representasi TSDF multi-sudut-pandang memberi jaringan informasi geometri *scene* yang lebih lengkap daripada satu citra kedalaman tunggal, dan validasi pada robot nyata — bukan hanya simulasi — memperkuat klaim kepraktisan metode.

Dari sisi rekayasa, representasi grid 40³ pada ruang kerja 30 sentimeter membatasi resolusi spasial hingga sekitar 0,75 sentimeter per *voxel*; objek kecil atau bagian pegangan yang sempit berisiko tidak terwakili cukup detail pada grid sekasar ini. Secara konseptual, kualitas keluaran juga bergantung penuh pada kualitas TSDF yang dibentuk dari citra kedalaman — derau sensor kedalaman atau kegagalan integrasi antar-sudut-pandang akan menurunkan mutu peta *grasp* tanpa mekanisme koreksi eksplisit dalam jaringan. Volume 3D berukuran 40³ juga jauh lebih mahal secara memori dan komputasi daripada representasi 2D setara seperti pada GG-CNN, sehingga skalabilitas ke ruang kerja yang jauh lebih besar dari 30 sentimeter memerlukan penyesuaian resolusi atau arsitektur.

## Kaitan dengan Bab Lain

VGN berada dalam klaster Grasp Robotik bersama bab [183 - 2021 - Contact-GraspNet - Grasp Robotik](./183%20-%202021%20-%20Contact-GraspNet%20-%20Grasp%20Robotik.md). Kedua metode sama-sama menyasar *grasp* 6-*DoF* pada *scene* cluttered, tetapi berangkat dari filosofi berbeda: Contact-GraspNet memprediksi *grasp* dari *point cloud* dengan pendekatan berbasis titik kontak pada permukaan objek, sedangkan VGN memprediksi dari representasi volumetrik grid TSDF dengan konvolusi 3D penuh. Perbandingan ini relevan untuk pembaca yang mengevaluasi trade-off antara representasi berbasis titik (lebih hemat memori, resolusi mengikuti kepadatan titik) dan representasi berbasis grid (resolusi tetap, tetapi cocok untuk konvolusi standar dan integrasi multi-sudut-pandang seperti TSDF). Formulasi prediksi padat per-*voxel* pada VGN juga sejalan dengan prinsip GG-CNN yang diangkat dari 2D ke 3D, menempatkan VGN sebagai kelanjutan garis penelitian *dense grasp prediction* (prediksi grasp padat) ke ruang tiga dimensi penuh.

## Poin untuk Sitasi

Kutip dengan kunci `breyer2021vgn`. Ringkasan yang aman dikutip: "VGN memprediksi grasp 6-DoF dari representasi volumetrik TSDF lewat 3D CNN yang mengeluarkan peta kualitas, orientasi, dan lebar grasp untuk setiap voxel dalam satu forward pass, mencapai waktu perencanaan sekitar 10 milidetik dan clearance rate 92% pada uji robot nyata dengan lengan Franka Emika Panda." Angka detail berikut diambil dari versi HTML arXiv dan sebaiknya diverifikasi ulang terhadap PDF resmi sebelum dikutip dalam karya formal: resolusi grid 40×40×40 pada ruang kerja 30×30×30 cm, komposisi jaringan *encoder* 16/32/64 filter dengan *bottleneck* 64×5³, jumlah model 3D latih (303) dan uji (40), total label grasp sekitar dua juta, serta tabel hasil simulasi *pile*/*packed* untuk VGN versus GPD (mis. 62,3%/46,4% berbanding 59,9%/26,1% pada lima objek *pile*) dan tingkat keberhasilan robot nyata 80% (55 dari 68 percobaan). Nilai inferensi CPU (±1,25 detik pada Intel Core i7-8550U) juga perlu konfirmasi ulang.
