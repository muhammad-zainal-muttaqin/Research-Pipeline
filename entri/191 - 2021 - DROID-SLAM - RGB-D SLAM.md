# 191 - DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `teed2021droidslam` |
| Judul asli | DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras |
| Penulis | Zachary Teed, Jia Deng |
| Tahun | 2021 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2021) |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2108.10869
- **Proceedings NeurIPS (PDF resmi):** https://proceedings.neurips.cc/paper/2021/hash/89fcd07f20b6785b92134bd6c1d0fa42-Abstract.html
- **Google Scholar:** https://scholar.google.com/scholar?q=DROID-SLAM%3A%20Deep%20Visual%20SLAM%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras

## Gambaran Umum

DROID-SLAM adalah sistem *SLAM* (*Simultaneous Localization and Mapping*, estimasi posisi kamera dan peta lingkungan secara serentak) berbasis pembelajaran dalam yang menyatukan estimasi *optical flow* (aliran optik, perpindahan piksel antar-*frame*) yang dipelajari dengan optimasi geometris klasik. Inti sistemnya adalah lapis *Dense Bundle Adjustment* (DBA, penyesuaian berkas pandang padat yang dapat didiferensialkan) yang disisipkan langsung di dalam jaringan saraf berulang (*recurrent*): pada setiap iterasi, jaringan memprediksi revisi korespondensi piksel antar-*frame* beserta tingkat kepercayaannya, lalu lapis DBA menyelesaikan pose kamera dan *depth* (kedalaman) per-piksel yang konsisten secara geometris. Sistem ini dilatih hanya pada video monokular sintetis, tetapi saat pengujian menerima masukan monokular, stereo, maupun RGB-D tanpa mengubah arsitektur — hanya menambah kendala geometris pada graf yang dioptimalkan. Pada TartanAir, EuRoC, dan TUM-RGBD, DROID-SLAM dilaporkan menekan galat trajektori jauh di bawah metode SLAM berbasis pembelajaran sebelumnya dan jarang mengalami kegagalan pelacakan total, kondisi yang masih sering muncul pada sistem klasik berbasis fitur ketika gerak kamera cepat atau tekstur adegan minim.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sistem SLAM klasik berbasis fitur, seperti ORB-SLAM2 (bab 107) dan ORB-SLAM3 (bab 190), membangun peta dari sekumpulan titik fitur jarang (*sparse*) yang dideteksi dan dicocokkan antar-*frame*, lalu memperbaiki pose dan posisi titik peta melalui *bundle adjustment* — optimasi bersama yang meminimalkan galat reproyeksi seluruh titik dan pose secara serentak. Pendekatan ini akurat pada kondisi baik, tetapi rapuh ketika korespondensi fitur sulit ditemukan: gerak kamera cepat menyebabkan *motion blur*, permukaan bertekstur minim tidak menghasilkan cukup titik fitur yang andal, dan pencahayaan berubah drastis membuat deskriptor fitur tidak cocok. Kegagalan pencocokan fitur pada tahap awal berpotensi menjalar menjadi kegagalan pelacakan total (*catastrophic tracking failure*): sistem kehilangan estimasi pose sepenuhnya dan tidak dapat pulih tanpa inisialisasi ulang.

Generasi awal SLAM berbasis pembelajaran dalam, seperti DeepV2D dan DeepFactors, mencoba mengatasi kerapuhan ini dengan meregresi pose dan *depth* langsung memakai jaringan konvolusi. Pendekatan tersebut lebih tangguh terhadap variasi visual, tetapi umumnya kurang akurat dibandingkan metode klasik karena tidak menegakkan konsistensi geometris seketat *bundle adjustment* eksplisit — regresi jaringan cenderung menghasilkan estimasi yang mulus secara statistik, tetapi tidak selalu memenuhi kendala proyeksi kamera yang tepat. Celah yang tersisa adalah menggabungkan ketangguhan fitur yang dipelajari dengan ketelitian geometris optimasi klasik, dalam satu sistem yang dapat dilatih *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah) dan bekerja pada berbagai jenis sensor kamera tanpa dilatih ulang untuk masing-masing.

## Ide Utama

Gagasan inti DROID-SLAM adalah menempatkan optimasi *bundle adjustment* sebagai satu lapis yang dapat didiferensialkan di dalam arsitektur jaringan berulang, bukan sebagai tahap pasca-pemrosesan terpisah dari fitur yang dipelajari. Pada setiap iterasi, jaringan menerima sepasang *frame* dan memprediksi dua hal: ke mana korespondensi piksel seharusnya direvisi (mirip prediksi *flow*), dan seberapa yakin jaringan terhadap revisi tersebut untuk tiap piksel. Kedua keluaran ini diperlakukan sebagai target korespondensi sementara yang diselesaikan lapis DBA menjadi pembaruan pose kamera dan *depth* per-piksel yang taat kaidah proyeksi kamera, lalu diumpankan kembali ke iterasi berikutnya sehingga estimasi makin presisi. Karena DBA diformulasikan sebagai operasi yang dapat diturunkan (*differentiable*), galat pada keluaran akhir dapat merambat balik (*backpropagation*) melalui seluruh proses optimasi hingga ke bobot jaringan fitur — jaringan belajar memprediksi korespondensi yang membuat optimasi geometris konvergen ke hasil benar, bukan sekadar mendekati target secara statistik.

## Cara Kerja Langkah demi Langkah

### Representasi Keadaan dan Graf Frame

DROID-SLAM menyimpan dua variabel keadaan per *frame*: pose kamera dalam grup SE(3) (rotasi dan translasi tiga dimensi) dan peta *inverse depth* (kebalikan kedalaman, satu nilai per piksel pada resolusi 1/8 citra masukan). Hubungan antar-*frame* direpresentasikan sebagai graf *frame*: setiap *node* adalah satu *frame*, dan setiap sisi (*edge*) menghubungkan dua *frame* yang dianggap saling tumpang tindih pandangannya (*co-visible*). Graf ini diperbarui secara dinamis seiring video berjalan — ketika kamera kembali melintasi wilayah yang pernah direkam, sisi baru dapat terbentuk kembali ke *frame* lama yang relevan, memberi efek koreksi jalur berulang (mirip fungsi *loop closure*, pengenalan tempat yang pernah dikunjungi untuk mengoreksi akumulasi galat) tanpa modul pengenalan tempat terpisah seperti pada sistem klasik.

### Enkoder Fitur dan Volume Korelasi

Setiap *frame* diproses oleh dua jaringan konvolusi terpisah: enkoder fitur untuk pencocokan antar-*frame*, dan enkoder konteks yang menghasilkan fitur sebagai masukan tambahan pengoperasi pembaruan. Untuk setiap sisi pada graf *frame*, volume korelasi 4-dimensi dibentuk dengan menghitung hasil kali titik (*dot product*) antara vektor fitur setiap piksel *frame* pertama terhadap seluruh piksel *frame* kedua, mengikuti skema RAFT (*Recurrent All-Pairs Field Transforms*, jaringan estimasi *optical flow* berulang). Volume ini dikumpulkan pada beberapa skala resolusi (piramida) sehingga pencarian korespondensi mencakup pergeseran piksel besar maupun kecil.

### Pengoperasi Pembaruan Berulang (ConvGRU)

Sebuah *Gated Recurrent Unit* (GRU) konvolusi — unit jaringan berulang yang mempertahankan keadaan tersembunyi (*hidden state*) antar-iterasi — menerima fitur hasil pencarian pada volume korelasi di sekitar estimasi korespondensi saat ini, ditambah fitur konteks dan keadaan tersembunyi sebelumnya. Keluarannya adalah dua peta per-piksel untuk setiap sisi graf: medan revisi korespondensi (arah dan besar perubahan yang diusulkan) dan peta kepercayaan (bobot yang menunjukkan seberapa dapat diandalkan revisi tersebut, misalnya rendah pada area bertekstur minim atau teroklusi). Pengoperasi ini dijalankan berulang sehingga estimasi makin tajam pada iterasi berikutnya.

### Lapis Dense Bundle Adjustment

Revisi korespondensi dan peta kepercayaan dari GRU diperlakukan sebagai pengamatan yang harus dijelaskan oleh geometri kamera. Lapis DBA menyelesaikan pembaruan pose dan *depth* yang meminimalkan galat reproyeksi berbobot kepercayaan, memakai pembaruan Gauss-Newton (metode optimasi iteratif untuk masalah kuadrat terkecil nonlinear) yang dilinearisasi pada koordinat lokal aljabar Lie dari SE(3). Karena jumlah variabel *depth* jauh lebih banyak daripada variabel pose, struktur matriks Hessian yang blok-diagonal dimanfaatkan melalui komplemen Schur: variabel *depth* per-piksel dieliminasi terlebih dahulu, menyisakan sistem persamaan kecil pada variabel pose yang lebih murah diselesaikan, sebelum *depth* dihitung kembali dari hasilnya. Skema ini struktural sama dengan *bundle adjustment* klasik, tetapi dirancang agar tetap dapat diturunkan sehingga gradien merambat balik ke bobot jaringan.

Alur satu putaran pembaruan dapat diringkas sebagai berikut:

```
frame i, frame j (sisi pada graf frame)
        |
        v
  enkoder fitur+konteks -> volume korelasi 4D
        |
        v
  ConvGRU (keadaan tersembunyi t-1)
        |
        v
  revisi korespondensi + peta kepercayaan
        |
        v
  lapis Dense Bundle Adjustment
  (Gauss-Newton, komplemen Schur)
        |
        v
  pose SE(3) & inverse depth diperbarui  --> diumpankan ke iterasi t+1
```

### Dukungan Stereo dan RGB-D

Untuk masukan stereo, graf *frame* diperluas dengan menambahkan sisi tetap antara citra kiri dan kanan pada setiap langkah waktu, memberi kendala *baseline* (jarak antar-lensa) yang diketahui sehingga skala metrik langsung tersedia. Untuk masukan RGB-D, nilai *depth* dari sensor ditambahkan sebagai suku penalti dalam optimasi — bukan diperlakukan sebagai kebenaran mutlak, melainkan kendala tambahan yang menarik estimasi *depth* jaringan agar tidak menyimpang jauh dari pengukuran sensor, sambil tetap dikoreksi oleh konsistensi geometris antar-*frame*. Karena mekanisme dasarnya sama untuk ketiga modalitas, satu bobot jaringan yang dilatih pada video monokular sintetis dapat langsung dipakai untuk stereo maupun RGB-D tanpa pelatihan ulang khusus modalitas.

### Prosedur Pelatihan

DROID-SLAM dilatih pada TartanAir, kumpulan data video sintetis dengan lintasan kamera dan lingkungan tiga dimensi beragam yang menyediakan pose kamera dan *depth* kebenaran-dasar (*ground truth*) secara presisi karena dihasilkan dari simulasi. Pelatihan dilakukan hanya dengan masukan monokular; galat dihitung dengan membandingkan pose dan korespondensi hasil optimasi tiap iterasi terhadap kebenaran-dasar, lalu dirambatkan balik melalui seluruh rantai iterasi GRU dan lapis DBA sekaligus.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada tiga tolok ukur: TartanAir (lintasan sintetis yang tidak dipakai untuk pelatihan), EuRoC (rekaman drone dalam ruangan dengan kebenaran-dasar dari sistem penangkap gerak), dan TUM-RGBD (rekaman kamera genggam berpasangan RGB dan *depth*). Metrik utama adalah *Absolute Trajectory Error* (ATE, galat posisi rata-rata antara trajektori estimasi dan kebenaran-dasar setelah penyelarasan skala/rotasi, dalam meter — semakin kecil semakin baik) serta jumlah kegagalan pelacakan total per rangkaian uji.

Menurut publikasi dan ringkasan hasil yang beredar, pada TartanAir DROID-SLAM mencapai galat rata-rata sekitar delapan kali lebih rendah daripada TartanVO dan sekitar dua puluh kali lebih rendah daripada DeepV2D, tanpa kegagalan pelacakan. Selisih sebesar itu menunjukkan bahwa penggabungan optimasi geometris eksplisit dengan fitur yang dipelajari memberi keuntungan akurasi yang jauh melampaui perbaikan inkremental atas metode regresi langsung. Pada EuRoC monokular, galat ditekan sekitar 82% dibandingkan metode lain yang juga tanpa kegagalan, dan sekitar 43% lebih rendah daripada ORB-SLAM3 bila dibatasi pada rangkaian yang berhasil dilacak ORB-SLAM3; dengan stereo, selisihnya sekitar 71% terhadap ORB-SLAM3. Pada TUM-RGBD, seluruh sembilan rangkaian uji berhasil dilacak, dengan ATE sekitar 83% lebih rendah daripada DeepFactors dan 90% lebih rendah daripada DeepV2D. Pola konsistennya: DROID-SLAM tidak hanya lebih akurat, tetapi terutama lebih jarang gagal total — sedangkan ORB-SLAM3 pada sebagian rangkaian EuRoC gagal melacak sepenuhnya karena kehilangan korespondensi fitur.

## Kelebihan dan Keterbatasan

Kelebihan utamanya adalah penyatuan fitur yang dipelajari dengan optimasi geometris eksplisit dalam satu arsitektur yang dapat dilatih *end-to-end*, sehingga sistem memperoleh akurasi mendekati atau melampaui *bundle adjustment* klasik sekaligus ketangguhan generalisasi jaringan saraf. Sifat serba guna lintas modalitas — satu bobot jaringan bekerja pada monokular, stereo, dan RGB-D — juga menonjol karena kebanyakan sistem SLAM klasik memerlukan penyesuaian *pipeline* berbeda untuk tiap jenis sensor. Mekanisme graf *frame* yang membentuk sisi baru ke *frame* lama memberi ketangguhan tambahan terhadap drift jangka panjang tanpa modul pengenalan tempat terpisah.

Dari sisi rekayasa, kebutuhan komputasinya besar: volume korelasi dihitung untuk setiap pasangan piksel pada setiap sisi graf, dan jumlah variabel *depth* yang dioptimalkan tumbuh sebanding dengan resolusi citra serta ukuran jendela aktif graf, sehingga memori GPU menjadi kendala nyata untuk lintasan panjang atau perangkat berdaya rendah. Secara konseptual, sistem ini mengasumsikan adegan statis; objek dinamis tidak dimodelkan secara eksplisit dan berpotensi mencemari korespondensi yang dipakai lapis DBA, meskipun peta kepercayaan yang dipelajari dapat menekan sebagian pengaruhnya secara implisit. Penanganan *depth* RGB-D sebagai penalti lunak juga berarti sensor yang sangat *noisy* pada kondisi tertentu (permukaan reflektif, jarak jauh) tidak diberi perlakuan koreksi eksplisit di luar bobot kepercayaan umum.

## Kaitan dengan Bab Lain

DROID-SLAM berada pada klaster RGB-D SLAM yang sama dengan ORB-SLAM3 (bab [190 - 2021 - ORB-SLAM3 - RGB-D SLAM](./190%20-%202021%20-%20ORB-SLAM3%20-%20RGB-D%20SLAM.md)) dan pendahulunya ORB-SLAM2 (bab [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)). Ketiganya dibandingkan langsung pada EuRoC dan TUM-RGBD, tetapi berangkat dari paradigma berbeda: ORB-SLAM2/3 membangun peta dari fitur ORB jarang yang dicocokkan dan dioptimalkan lewat *bundle adjustment* pasca-deteksi fitur, sedangkan DROID-SLAM melipat seluruh proses pencocokan dan optimasi ke dalam satu jaringan berulang yang dilatih *end-to-end*. Ketangguhan DROID-SLAM pada rangkaian yang membuat ORB-SLAM3 gagal menunjukkan posisinya sebagai alternatif yang menutupi kelemahan utama pendekatan berbasis fitur tangan, sekaligus menjadi rujukan arsitektur bagi karya SLAM/*visual odometry* berbasis pembelajaran berikutnya yang mengadopsi graf *frame* dan optimasi diferensiabel serupa.

## Poin untuk Sitasi

Kutip dengan kunci `teed2021droidslam`. Ringkasan yang aman dikutip: "DROID-SLAM menggabungkan pengoperasi pembaruan berulang berbasis *optical flow* dengan lapis *Dense Bundle Adjustment* yang dapat didiferensialkan untuk memperbarui pose kamera dan *depth* per-piksel secara bersamaan; dilatih hanya pada video monokular sintetis (TartanAir), sistem ini digeneralisasi ke masukan stereo dan RGB-D serta menunjukkan galat trajektori dan tingkat kegagalan pelacakan yang jauh lebih rendah daripada metode SLAM klasik maupun berbasis pembelajaran sebelumnya pada EuRoC dan TUM-RGBD." Angka persentase penurunan ATE (sekitar 8x dan 20x pada TartanAir; 82%, 43%, dan 71% pada EuRoC; 83% dan 90% pada TUM-RGBD) berasal dari ringkasan sekunder karena ekstraksi teks langsung dari PDF NeurIPS tidak berhasil — wajib diverifikasi terhadap tabel asli sebelum dikutip dalam karya formal. Jumlah iterasi GRU, hyperparameter pelatihan, dan mekanisme eksplisit pengenalan tempat di luar sisi graf yang terbentuk ulang juga belum terverifikasi langsung dari naskah.
