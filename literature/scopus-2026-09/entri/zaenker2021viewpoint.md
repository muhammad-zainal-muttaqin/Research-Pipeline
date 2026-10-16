# Viewpoint Planning for Fruit Size and Position Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zaenker2021viewpoint` |
| Judul asli | Viewpoint Planning for Fruit Size and Position Estimation |
| Penulis | Zaenker, Tobias; Smitt, Claus; McCool, Chris; Bennewitz, Maren |
| Tahun | 2021 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [zaenker2021viewpoint.pdf](../pdf/zaenker2021viewpoint.pdf)
- DOI resmi: https://doi.org/10.1109/iros51168.2021.9636701

## Gambaran Umum
Makalah ini menyajikan perencanaan sudut pandang (*viewpoint planning*) untuk mengestimasi posisi dan ukuran buah pada tanaman dengan kamera RGB-D pada lengan robot. Sistem membangun *octree* tanaman dengan daerah minat (*regions of interest*, ROI) berupa buah, memakai octree itu untuk mengambil sampel kandidat sudut pandang yang menambah informasi di sekitar buah, dan menilainya dengan fungsi utilitas heuristik berdasarkan perkiraan perolehan informasi. Sistem beralih otomatis antara pengambilan sampel yang menarget ROI dan pengambilan sampel eksplorasi pada voksel batas (*frontier*) umum. Setelah tanaman terpindai cukup, voksel ROI dikelompokkan, lalu posisi dan ukuran buah diestimasi.

Evaluasi dilakukan pada dua skenario simulasi tanaman kapsikum (*capsicum*) dan pada demonstrasi di rumah kaca kapsikum komersial dengan lengan UR5e pada troli rel pipa. Pada simulasi, pendekatan yang diusulkan dibandingkan dengan pengambilan sampel eksplorasi murni; rata-rata jumlah ROI terdeteksi pada Skenario 2 adalah 27,0 ± 2,4 (Ours-UU) berbanding 24,8 ± 4,1 (Explo-UU) dan 17,4 ± 3,9 (Explo-UP). Akurasi volume terbaik hanya 0,52 pada Skenario 1 dan 0,56 pada Skenario 2.

Makalah ini tidak menangani pencacahan lintas pandang secara eksplisit. Buah dari banyak sudut pandang digabungkan pada satu peta voksel 3D bersama, kemudian dikelompokkan menjadi buah individual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Aplikasi pertanian seperti pemetikan buah dan penyemprotan terarah memerlukan informasi posisi dan ukuran buah. Sensor tetap sulit membangun model 3D karena bagian tanaman tertutup daun. Perencanaan sudut pandang konvensional biasanya bertujuan membangun model 3D lengkap, padahal untuk pemetikan hanya lokasi dan ukuran buah yang diperlukan, bukan bentuk setiap daun. Pendekatan perencanaan sebagian besar mengandaikan lingkungan statis yang peta awalnya diketahui, sehingga tidak cocok untuk tanaman yang berubah cepat. Makalah ini menjawab kebutuhan perencanaan yang mendeteksi buah saat berjalan dan memusatkan pandangan pada ROI.

## Ide Utama
Deteksi buah pada citra diproyeksikan ke peta 3D sebagai ROI, lalu ROI dipakai untuk mengambil sampel sudut pandang yang melihat buah dari arah lain. Pengambilan sampel eksplorasi yang tidak bergantung pada ROI dijalankan bila utilitas sudut pandang ROI jatuh di bawah ambang, agar buah baru dapat ditemukan. Perencanaan memilih satu sudut pandang terbaik berikutnya (bukan seluruh jalur), sehingga kompleksitasnya rendah dan dapat dipakai sebagai perencana sasaran tingkat tinggi untuk perencana gerak apa pun.

## Cara Kerja Langkah demi Langkah

### 1. Deteksi ROI
Pada simulasi, tanaman hanya berbuah merah sehingga deteksi memakai ambang warna pada ruang HSI: matahari antara -30° dan 50° serta saturasi dan intensitas paling sedikit 0,12 (teks menyebut "hue" untuk nilai pertama). Pada percobaan nyata ada paprika berwarna hijau yang tidak dapat dipisahkan dengan filter warna, sehingga dipakai jaringan segmentasi instans Yolact yang dilatih dengan dataset yang direkam di University of Bonn. Titik awan yang dihasilkan dari citra kedalaman yang disejajarkan warna diturunkan resolusinya ke resolusi octree dengan *voxel grid filter*, dan titik dalam masker buah ditandai sebagai ROI.

### 2. Octree untuk perencanaan
Octree kustom di atas OctoMap menyimpan dua nilai per simpul, yaitu probabilitas keterisian dan probabilitas ROI, keduanya dalam log-odds. Keterisian diperbarui dengan *ray casting* dari asal sensor ke tiap titik, dan simpul dianggap terisi bila log-odds positif dan bebas bila negatif. Probabilitas ROI diperbarui hanya pada simpul yang bersesuaian dengan titik, dan simpul menjadi ROI bila log-odds melewati ambang.

### 3. Pengambilan sampel kandidat sudut pandang
Dua octree tambahan dipakai: octree ruang kerja (hasil menyapu konfigurasi sendi lengan) dan octree pengambilan sampel yang menentukan wilayah target. Pengambilan sampel ROI menentukan target dari voksel bebas di sekitar ROI yang bertetangga dengan voksel tidak diketahui, lalu sudut pandang diambil acak dalam jangkauan sensor dan dibuang bila sinar ke target terhalang. Pengambilan sampel eksplorasi memakai voksel bebas yang bertetangga dengan voksel terisi sekaligus voksel tidak diketahui.

### 4. Evaluasi sudut pandang
Dua utilitas perolehan informasi dibandingkan. Utilitas voksel tak teramati ($U_U$) memakai rerata rasio voksel tidak diketahui per sinar,
$$IG_U = \frac{1}{|R|}\sum_{r\in R}\frac{N_{u,r}}{N_r}.$$
Utilitas hitungan kedekatan ($U_P$) membobotkan voksel tidak diketahui lebih tinggi bila dekat dengan ROI yang sudah teramati, dengan bobot $w = 0{,}5 + 0{,}5\,(max\_dist - dist)/max\_dist$. Utilitas akhir adalah $U = IG - \alpha C$, dengan $C$ jarak Euklides kamera ke sudut pandang sebagai pendekatan biaya.

### 5. Pemilihan dan eksekusi
Pada tiap putaran diambil 100 sudut pandang ROI dan 100 sudut pandang eksplorasi. Bila utilitas maksimum sudut pandang ROI melewati ambang empiris, kelompok itu dipakai; bila tidak, kelompok eksplorasi dipakai. Planner mencoba merencanakan jalur ke sudut pandang bernilai tertinggi lewat MoveIt, dan bila gagal memakai berikutnya sampai tidak ada yang melewati ambang.

### 6. Estimasi posisi dan ukuran buah
Simpul ROI dikelompokkan dengan ketetanggaan 26 voksel. Posisi buah adalah rerata koordinat simpul klaster, dan ukuran diestimasi dari volume kotak pembatas 3D.

## Eksperimen dan Hasil
Lengan UR5e (enam derajat kebebasan, jangkauan 85 cm) dipakai pada simulasi dan percobaan nyata. Resolusi octree ruang kerja 2 cm dan octree perencanaan 1 cm. Skenario 1: empat tanaman, dua di antaranya masing-masing berbuah tujuh dan dua lainnya tanpa buah, dengan lengan di atas tiang statis setinggi 85 cm. Skenario 2: empat tanaman masing-masing berbuah tujuh, dengan lengan menggantung dari langit-langit dan dapat bergerak di area 2 × 2 m. Waktu perencanaan tiga menit, dan 20 percobaan per konfigurasi, dengan uji Mann-Whitney U satu sisi. ROI terdeteksi dihitung bila pusat klaster berjarak kurang dari 20 cm dari klaster acuan.

Hasil (Tabel I, rerata ± simpangan baku dari 20 percobaan):

| Skenario | Metrik | Ours-UP | Ours-UU | Explo-UP | Explo-UU |
|---|---|---|---|---|---|
| 1 | Jumlah ROI terdeteksi | 13,2 ± 0,7 | 13,8 ± 0,4 | 12,8 ± 1,1 | 13,4 ± 1,4 |
| 1 | Volume ROI tercakup | 0,69 ± 0,07 | 0,64 ± 0,12 | 0,63 ± 0,11 | 0,40 ± 0,12 |
| 1 | Jarak pusat (cm) | 2,41 ± 0,48 | 2,44 ± 0,45 | 2,23 ± 0,54 | 2,80 ± 0,47 |
| 1 | Akurasi volume | 0,52 ± 0,07 | 0,49 ± 0,10 | 0,50 ± 0,21 | 0,35 ± 0,08 |
| 2 | Jumlah ROI terdeteksi | 23,3 ± 2,9 | 27,0 ± 2,4 | 17,4 ± 3,9 | 24,8 ± 4,1 |
| 2 | Volume ROI tercakup | 0,55 ± 0,11 | 0,68 ± 0,10 | 0,34 ± 0,08 | 0,36 ± 0,13 |
| 2 | Jarak pusat (cm) | 2,31 ± 0,45 | 2,21 ± 0,35 | 2,75 ± 0,51 | 2,96 ± 0,43 |
| 2 | Akurasi volume | 0,55 ± 0,07 | 0,56 ± 0,08 | 0,50 ± 0,09 | 0,40 ± 0,08 |

Pada Skenario 1, pendekatan yang diusulkan dengan $U_P$ terbaik, tetapi keunggulannya atas $U_U$ atau eksplorasi dengan $U_P$ kecil. Pada Skenario 2, $U_U$ terbaik, yang oleh penulis diduga karena $U_P$ memerlukan perhitungan jarak ke ROI terdekat sehingga lebih mahal pada lingkungan besar. Penulis menyatakan bahwa pendekatan dengan $U_U$ mencapai jumlah ROI terdeteksi dan volume tercakup yang jauh lebih tinggi daripada eksplorasi murni. Teks tidak menyebut nilai-p; penandaan tebal pada tabel tidak terbaca pada ekstraksi.

Percobaan nyata memakai RealSense L515 pada troli rel pipa dengan pengangkat gunting hingga 3 m; hanya lengan yang dikendalikan planner, dan troli digeser manual sepanjang platform. Tidak ada acuan dan jumlah percobaan terbatas, sehingga tidak ada analisis numerik. Satu segmen memuat dua paprika merah yang berhasil dikenali dan dikelompokkan. Peta kurang akurat daripada simulasi karena derau dan terdapat buah salah tanda akibat deteksi palsu jaringan.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: perencanaan berfokus ROI yang meningkatkan efisiensi perolehan informasi buah, metrik sederhana cukup bila sampel menarget ROI sehingga hemat komputasi, dan kode serta lingkungan simulasi tersedia di GitHub.

Keterbatasan yang dinyatakan penulis: akurasi volume terbatas (rerata 0,52 dan 0,56 pada konfigurasi terbaik) karena pengelompokan yang naif dan resolusi octree 1 cm yang tidak dapat dinaikkan untuk perencanaan daring; pada percobaan nyata ada deteksi palsu dan derau; dan belum ada acuan untuk percobaan nyata. Rencana ke depan adalah menggabungkan perencanaan dengan model 3D beresolusi tinggi.

Menurut pembacaan ringkasan ini, simulasi hanya mencakup dua skenario kecil (maksimum 28 buah acuan), pembanding hanya satu metode eksplorasi, dan jumlah buah terdeteksi pada Skenario 1 hampir seluruhnya sama antarkonfigurasi. Percobaan nyata berupa demonstrasi tanpa pengukuran sehingga ketepatan hitungan tidak terbukti di lapangan.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani identitas buah yang sama lintas pandang melalui pencocokan. Buah yang terlihat dari banyak sudut pandang digabungkan secara implisit pada peta voksel 3D bersama (log-odds ROI), lalu pengelompokan ketetanggaan 26 voksel memberikan satu klaster per buah. Identitas dengan demikian diperoleh dari koordinat 3D bersama, yang bergantung pada posisi lengan dan sensor yang diketahui. Hitungan tidak dilaporkan per kelas. Acuan hitung berupa buah dan kotak pembatasnya pada model tanaman simulasi; pada percobaan nyata tidak ada acuan (bukan panen, hitung manual, maupun anotasi).

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memilih sudut pandang berikutnya berdasarkan perolehan informasi di sekitar buah yang terdeteksi sebagian, dan gagasan menyatukan deteksi dari banyak pandang di peta 3D bersama untuk menjaga satu hitungan per buah. Hal itu memerlukan pose kamera yang diketahui, yang tidak tersedia pada pengambilan citra manual.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zaenker2021viewpoint`.

Zaenker dkk. mengusulkan perencanaan sudut pandang untuk estimasi posisi dan ukuran buah yang membangun *octree* dengan ROI buah, mengambil sampel sudut pandang di sekitar buah terdeteksi dan di voksel batas eksplorasi, serta mengelompokkan voksel ROI untuk menaksir buah. Pada simulasi tanaman kapsikum dengan 20 percobaan per konfigurasi, pendekatan ini mendeteksi lebih banyak ROI dan mencakup lebih banyak volume ROI daripada eksplorasi murni (misalnya Skenario 2: 27,0 ± 2,4 berbanding 24,8 ± 4,1 untuk utilitas yang sama), dengan akurasi volume terbaik 0,52 dan 0,56.

Catatan verifikasi data: seluruh angka diambil dari Tabel I dan bagian VI-A, VI-B; konfigurasi Skenario 1 dan 2 dari keterangan Gambar 3. Tanda tebal untuk signifikansi pada Tabel I tidak terbaca pada teks ekstraksi, sehingga pernyataan signifikansi hanya dikutip dari kalimat teks. Jumlah buah acuan tercantum sebagai tujuh buah per tanaman berbuah; jumlah ROI terdeteksi pada Skenario 2 (hingga 27,0) melebihi 28 buah acuan secara kasar tidak mungkin sebagai hitungan buah, dan hubungan antara "ROI terdeteksi" dan jumlah buah acuan tidak dijelaskan pada teks, sehingga tidak dapat diverifikasi. Percobaan nyata tidak memiliki angka. Teks makalah secara umum terbaca baik.
