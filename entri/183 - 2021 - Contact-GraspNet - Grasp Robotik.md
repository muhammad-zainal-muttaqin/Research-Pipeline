# 183 - Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sundermeyer2021contactgraspnet` |
| Judul asli | Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes |
| Penulis | Martin Sundermeyer, Arsalan Mousavian, Rudolph Triebel, Dieter Fox |
| Tahun | 2021 |
| Venue | IEEE International Conference on Robotics and Automation (ICRA 2021) |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2103.14127
- **Google Scholar:** https://scholar.google.com/scholar?q=Contact-GraspNet%3A%20Efficient%206-DoF%20Grasp%20Generation%20in%20Cluttered%20Scenes
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Contact-GraspNet%3A%20Efficient%206-DoF%20Grasp%20Generation%20in%20Cluttered%20Scenes&sort=relevance
- **Kode resmi:** https://github.com/NVlabs/contact_graspnet

## Gambaran Umum

Contact-GraspNet adalah jaringan saraf yang menghasilkan *grasp* (cengkeraman) 6-DoF (*degree of freedom*, derajat kebebasan pergerakan penjepit di ruang tiga dimensi: tiga translasi dan tiga rotasi) langsung dari satu *point cloud* (kumpulan titik koordinat 3D) tunggal hasil pemindaian kedalaman, tanpa tahap pengusulan wilayah terpisah. Masalah yang dipecahkan adalah menghasilkan cengkeraman *parallel-jaw* (penjepit dua rahang sejajar) yang andal untuk objek yang belum pernah dilihat sebelumnya, pada susunan objek yang saling berhimpitan (*cluttered scene*, scene berantakan). Gagasan intinya adalah menautkan setiap grasp pada titik kontak yang benar-benar teramati di permukaan objek pada point cloud, sehingga posisi grasp tidak perlu dicari di seluruh ruang 6-DoF, melainkan diturunkan dari titik yang sudah pasti berada pada permukaan benda nyata. Jaringan dibangun di atas *backbone* (tulang punggung ekstraksi fitur) PointNet++ dan dilatih pada data sintetis dari dataset ACRONYM. Pada uji robot fisik dengan lengan Franka Panda terhadap 51 objek yang belum pernah dilihat dalam susunan berantakan, metode ini melaporkan tingkat keberhasilan grasp di atas 90%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Menghasilkan grasp 6-DoF untuk objek arbitrer memerlukan pencarian pada ruang parameter yang sangat besar: tiga nilai posisi dan tiga nilai orientasi penjepit, dikalikan dengan seluruh kemungkinan lokasi di scene. Pendekatan sebelumnya, misalnya 6-DOF GraspNet, menangani ruang ini dengan melatih *variational autoencoder* (VAE, jaringan generatif yang mempelajari distribusi data laten) untuk mengusulkan (*sample*) kandidat grasp secara acak di sekitar objek, kemudian menilai dan memperbaiki kandidat tersebut lewat jaringan evaluator terpisah dan proses iteratif *grasp refinement* (perbaikan bertahap posisi grasp). Proses sampling-lalu-evaluasi ini memerlukan banyak iterasi sebelum kandidat berkualitas ditemukan, sehingga lambat untuk digunakan pada kontrol robot secara reaktif. Pendekatan lain, GraspNet-1Billion, menyediakan benchmark berskala besar tetapi tetap bergantung pada tahap pengusulan kandidat yang terpisah dari tahap penilaian akhir.

Kelemahan bersama dari pendekatan sampling-dan-evaluasi adalah tidak adanya jaminan bahwa kandidat yang diusulkan berada dekat dengan permukaan objek yang benar-benar teramati sensor. Karena scene kedalaman hanya menangkap permukaan objek yang terlihat dari satu sudut pandang (data setengah, *single-view partial point cloud*), banyak kandidat grasp yang dihasilkan secara acak jatuh pada ruang kosong atau menembus geometri objek, sehingga harus disaring lebih lanjut. Pada scene berantakan, masalah ini makin berat karena objek saling menghalangi (*occlusion*) dan ruang gerak penjepit dibatasi objek tetangga, sehingga jumlah kandidat yang benar-benar dapat dieksekusi tanpa tabrakan menjadi kecil dibanding jumlah kandidat yang diusulkan.

## Ide Utama

Gagasan inti Contact-GraspNet adalah mengurangi dimensi pencarian grasp dengan menetapkan titik kontak grasp langsung pada titik-titik point cloud yang teramati. Karena titik-titik itu sudah pasti berada pada permukaan objek nyata, tiga derajat kebebasan translasi grasp otomatis terpenuhi begitu satu titik dipilih. Jaringan tidak lagi perlu mengusulkan posisi grasp dari ruang kosong 6-DoF; ia cukup memprediksi, untuk setiap titik pada point cloud, apakah titik itu merupakan titik kontak yang baik, dan bila ya, orientasi serta lebar bukaan penjepit yang sesuai. Representasi ini disebut penulis sebagai reduksi ke 4-DoF: translasi grasp diwarisi dari koordinat titik yang diamati, sedangkan sisa derajat kebebasan yang benar-benar perlu diprediksi jaringan adalah orientasi penjepit (arah pendekatan dan rotasi di sekitarnya) beserta lebar bukaan. Konsekuensinya, jaringan menghasilkan grasp untuk seluruh scene dalam satu kali proses maju (*forward pass*), bukan lewat iterasi sampling-evaluasi berulang.

## Cara Kerja Langkah demi Langkah

### Representasi Grasp Berbasis Titik Kontak

Setiap grasp dinyatakan oleh lima besaran: titik kontak c (koordinat 3D pada point cloud tempat salah satu rahang penjepit menyentuh permukaan objek), vektor arah dasar b (*baseline direction*, arah garis yang menghubungkan kedua rahang penjepit), vektor arah pendekatan a (*approach direction*, arah gerak penjepit menuju objek, tegak lurus terhadap b), lebar bukaan w (*grasp width*, jarak antar-rahang saat mencengkeram), dan jarak *standoff* d (jarak dari titik kontak ke titik acuan penjepit di sepanjang arah pendekatan). Karena c diambil langsung dari koordinat titik point cloud, jaringan hanya perlu memprediksi b, a, w, dan d untuk setiap titik kandidat — inilah reduksi ke 4-DoF yang dimaksud.

### Backbone PointNet++

Point cloud masukan, hasil pengangkatan (*back-projection*) citra kedalaman tunggal ke ruang 3D, disaring menjadi sekitar 20.000 titik lalu diproses oleh PointNet++ (jaringan pemroses point cloud yang bekerja langsung pada himpunan titik tak beraturan, dibahas pada bab 148). PointNet++ menyusun fitur secara hierarkis lewat lapis *set abstraction* (pengelompokan titik-titik bertetangga menjadi fitur lokal pada skala kian membesar) diikuti lapis *feature propagation* (interpolasi fitur global kembali ke resolusi titik yang lebih rapat). Hasil akhirnya adalah vektor fitur per titik untuk sekitar 2.048 titik yang dipilih lewat *farthest point sampling* (pengambilan sampel titik yang saling berjauhan agar mewakili seluruh permukaan objek secara merata).

```
point cloud tunggal (±20.000 titik, dari 1 citra kedalaman)
              │
              ▼
   PointNet++ (set abstraction bertingkat)
              │  fitur lokal skala kian besar
              ▼
   feature propagation (interpolasi ke titik rapat)
              │
              ▼
   2.048 titik terpilih, tiap titik -> kepala prediksi
   ┌─────────────┬─────────────┬─────────────┐
   │  skor        │  orientasi   │  lebar (w)   │
   │  keberhasilan│  (a, b)      │  10 bin      │
   └─────────────┴─────────────┴─────────────┘
              │
              ▼
      filter tabrakan (buang grasp yang menembus geometri)
              │
              ▼
        grasp 6-DoF final per scene
```

### Kepala Prediksi per Titik

Untuk setiap titik terpilih, jaringan mengeluarkan tiga hal: skor keberhasilan grasp (probabilitas bahwa titik tersebut merupakan titik kontak yang layak), vektor rotasi yang menentukan arah dasar dan arah pendekatan, dan lebar bukaan penjepit yang diprediksi sebagai klasifikasi ke dalam 10 kelas rentang lebar (*binning*), bukan regresi nilai kontinu langsung — pendekatan ini dipilih penulis untuk menangani ketidakseimbangan distribusi lebar grasp pada data pelatihan. Karena prediksi dilakukan serentak untuk seluruh 2.048 titik dalam satu proses maju, jaringan menghasilkan ribuan kandidat grasp per scene tanpa iterasi.

### Filter Tabrakan dan Pemilihan Akhir

Kandidat grasp hasil prediksi kemudian disaring dengan pemeriksaan tabrakan geometris terhadap point cloud scene: kandidat yang penjepitnya akan menembus titik-titik lain (baik objek target maupun objek tetangga) dibuang. Penyaringan ini memanfaatkan kembali informasi geometri yang sudah tersedia di point cloud, tanpa memerlukan model 3D lengkap dari setiap objek. Kandidat yang lolos diurutkan berdasarkan skor keberhasilan, dan grasp berskor tertinggi yang bebas tabrakan dipilih untuk dieksekusi.

### Data Pelatihan: ACRONYM

Jaringan dilatih pada dataset ACRONYM, kumpulan data grasp sintetis berskala besar dari kelompok riset yang sama, berisi label grasp untuk 8.872 model mesh (bentuk 3D) yang diambil dari ShapeNet, dengan total sekitar 17,7 juta grasp berlabel hasil simulasi fisika. Untuk melatih Contact-GraspNet, objek-objek ACRONYM disusun ke dalam scene tabletop sintetis berisi banyak objek sekaligus, lalu grasp yang berhasil pada susunan tunggal disaring ulang dengan pemeriksaan tabrakan terhadap susunan berantakan tersebut sebelum dipetakan ke titik kontak pada point cloud hasil rendering. Dengan cara ini, label pelatihan berupa titik kontak beserta orientasi dan lebar grasp yang valid diperoleh murni dari simulasi, tanpa anotasi manual pada citra nyata.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tingkat: simulasi fisika untuk mengukur kualitas dan cakupan grasp yang dihasilkan pada scene sintetis, dan uji fisik pada lengan robot Franka Panda untuk mengukur keberhasilan grasp di dunia nyata. Pada uji robot fisik, 51 objek yang tidak pernah dilihat selama pelatihan disusun dalam kondisi berantakan (*bin-picking*, pengambilan objek dari wadah tercampur), dan metode ini melaporkan tingkat keberhasilan grasp keseluruhan 90,20% serta tingkat keberhasilan pada percobaan pertama (*first-attempt success*) 84,31%. Kecepatan inferensi dilaporkan sekitar 0,28 detik untuk memproses satu scene penuh, dan sekitar 0,19 detik bila hanya memproses wilayah lokal tertentu — cukup cepat untuk mendukung kontrol grasp reaktif dalam lingkar tertutup (*closed-loop*), yaitu penyesuaian ulang grasp saat robot masih bergerak mendekati objek.

Interpretasi angka ini: tingkat keberhasilan di atas 90% pada objek yang sama sekali baru menunjukkan bahwa representasi berbasis titik kontak menggeneralisasi dengan baik dari data sintetis ke sensor kedalaman nyata, meski pelatihan sepenuhnya berlangsung dalam simulasi. Selisih antara keberhasilan keseluruhan (90,20%) dan keberhasilan percobaan pertama (84,31%) menunjukkan bahwa sebagian kegagalan awal masih dapat dipulihkan lewat percobaan ulang, konsisten dengan kecepatan inferensi yang mendukung eksekusi berulang tanpa biaya komputasi besar. Klaim penulis bahwa metode ini mengungguli metode *state-of-the-art* sebelumnya sebesar sekitar 10 poin persentase — kemungkinan besar merujuk pada 6-DOF GraspNet sebagai pembanding — perlu diverifikasi langsung ke tabel hasil pada naskah asli karena rincian metode pembanding dan kondisi pengujian yang setara belum terkonfirmasi penuh dari sumber sekunder yang diakses.

## Kelebihan dan Keterbatasan

Kelebihan utama metode ini adalah kesederhanaan jalur inferensi: satu proses maju melalui jaringan menghasilkan seluruh kandidat grasp untuk scene, tanpa iterasi sampling-evaluasi seperti pada 6-DOF GraspNet. Representasi berbasis titik kontak juga secara inheren menghindari kandidat grasp yang melayang jauh dari permukaan objek, karena translasi grasp diwarisi langsung dari geometri yang teramati. Generalisasi dari data sintetis ACRONYM ke sensor kedalaman nyata terbukti kuat pada uji robot fisik dengan objek yang belum pernah dilihat.

Dari sisi rekayasa, metode ini tetap bergantung pada kualitas dan kelengkapan point cloud masukan: karena hanya satu sudut pandang yang direkam, permukaan objek yang tidak terlihat sensor (misalnya sisi belakang objek yang menghadap menjauh dari kamera) tidak dapat dijadikan titik kontak, sehingga sebagian grasp yang secara geometris valid tidak pernah diusulkan. Secara konseptual, reduksi ke 4-DoF menyederhanakan pencarian tetapi mengasumsikan bahwa titik kontak yang baik selalu berada pada titik yang teramati langsung; untuk objek dengan permukaan transparan atau memantulkan cahaya, sensor kedalaman sering gagal menangkap geometri secara akurat, sehingga kualitas titik kontak yang dihasilkan ikut menurun. Filter tabrakan yang dipakai juga hanya memeriksa geometri point cloud yang tersedia, bukan model 3D lengkap objek, sehingga bagian yang tersembunyi dari sensor berpotensi menyebabkan tabrakan yang tidak terdeteksi saat eksekusi nyata.

## Kaitan dengan Bab Lain

Contact-GraspNet mewarisi PointNet++ sebagai backbone pemroses point cloud, konsep yang diperkenalkan pada bab [148 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md) dan pengembangannya. Dalam klaster Grasp Robotik, bab ini berdampingan dengan bab [184 - VGN - Grasp Robotik](./184%20-%202020%20-%20VGN%20-%20Grasp%20Robotik.md), yang memecahkan masalah serupa — grasp 6-DoF di scene berantakan — dengan pendekatan berbeda: VGN memproses scene sebagai grid volumetrik (TSDF, *truncated signed distance function*, representasi kepadatan permukaan pada grid 3D) dan memprediksi grasp per voxel, sementara Contact-GraspNet memprediksi grasp langsung per titik point cloud tanpa vokselisasi. Perbandingan keduanya relevan untuk menilai trade-off antara representasi grid (VGN, lebih mudah diproses konvolusi 3D tetapi resolusi dibatasi ukuran voxel) dan representasi titik (Contact-GraspNet, resolusi mengikuti kepadatan sensor tetapi memerlukan backbone khusus data tak beraturan seperti PointNet++). Kedua bab menjadi rujukan utama untuk aplikasi manipulasi robotik berbasis RGB-D dalam tinjauan ini.

## Poin untuk Sitasi

Kutip dengan kunci `sundermeyer2021contactgraspnet`. Ringkasan yang aman dikutip: "Contact-GraspNet menghasilkan grasp 6-DoF langsung dari satu point cloud dengan menautkan setiap grasp pada titik kontak yang teramati di permukaan objek, mereduksi dimensi pencarian menjadi 4-DoF; dilatih pada dataset sintetis ACRONYM (PointNet++ sebagai backbone), metode ini mencapai tingkat keberhasilan grasp 90,20% pada uji robot fisik terhadap 51 objek baru dalam kondisi berantakan." Angka berikut belum terverifikasi langsung ke tabel/teks lengkap naskah asli dan perlu dicek ulang sebelum dikutip secara formal: jumlah pasti grasp berlabel pada ACRONYM (dilaporkan sekitar 17,7 juta), jumlah mesh (8.872), angka keberhasilan percobaan pertama (84,31%), waktu inferensi (0,28 detik per scene penuh, 0,19 detik per wilayah lokal), serta klaim selisih sekitar 10 poin persentase di atas metode pembanding (identitas metode pembanding — diduga 6-DOF GraspNet — perlu dikonfirmasi ke naskah).
