# 088 - PointPillars: Fast Encoders for Object Detection from Point Clouds

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lang2019pointpillars` |
| Judul asli | PointPillars: Fast Encoders for Object Detection from Point Clouds |
| Penulis | Alex H. Lang, Sourabh Vora, Holger Caesar, Lubing Zhou, Jiong Yang, Oscar Beijbom |
| Tahun | 2019 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2019) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1812.05784
- **Google Scholar:** https://scholar.google.com/scholar?q=PointPillars%3A%20Fast%20Encoders%20for%20Object%20Detection%20from%20Point%20Clouds
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PointPillars%3A%20Fast%20Encoders%20for%20Object%20Detection%20from%20Point%20Clouds&sort=relevance

## Gambaran Umum

PointPillars memperkenalkan cara meng-*encode* (mengubah menjadi representasi numerik yang dapat diproses jaringan saraf) *point cloud* — kumpulan titik 3D hasil pemindaian sensor *LiDAR* (*Light Detection and Ranging*, sensor yang mengukur jarak dengan memantulkan berkas laser) — menjadi kolom-kolom vertikal yang disebut *pillar*, sehingga seluruh proses deteksi objek 3D dapat dijalankan memakai konvolusi 2D biasa, bukan konvolusi 3D yang jauh lebih mahal. Rumusan ini menghindari dua kelemahan pendekatan sebelumnya sekaligus: konvolusi 3D pada grid *voxel* yang lambat, dan proyeksi 2D dengan fitur buatan tangan (*hand-crafted*) yang membatasi akurasi.

Hasilnya adalah kombinasi kecepatan dan akurasi yang belum tercapai metode lain saat itu: pada *benchmark* KITTI, PointPillars mencapai 74,99% *average precision* (AP) 3D kelas mobil pada tingkat kesulitan sedang, berjalan pada 62 Hz (62 kali per detik) — dua sampai empat kali lebih cepat dari metode pembanding sekelas, bahkan mengungguli beberapa metode fusi kamera-LiDAR meski hanya memakai data LiDAR. Makalah ini menjadi rujukan arsitektur bagi banyak detektor 3D dan metode fusi sensor sesudahnya dalam klaster Deteksi 3D pada tinjauan ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

*Point cloud* dari LiDAR berbentuk himpunan titik 3D tak terurut dengan kerapatan tidak merata: titik memadat di dekat sensor dan menjarang pada jarak jauh. Bentuk data ini tidak cocok langsung dengan konvolusi 2D, yang membutuhkan grid piksel teratur. Dua strategi lebih dahulu mengatasi ketidakcocokan tersebut, masing-masing dengan kompromi berbeda.

Strategi pertama, dipakai VoxelNet (bab 087), membagi ruang 3D menjadi grid *voxel* (elemen volume, analog piksel dalam 3D) lalu menjalankan konvolusi 3D pada grid tersebut. Pendekatan ini mempertahankan struktur 3D penuh, tetapi konvolusi 3D pada grid yang sebagian besar kosong (titik LiDAR jarang mengisi seluruh volume) sangat boros komputasi — makalah ini mencatat waktu pengkodean fitur VoxelNet mencapai 190 milidetik per citra, jauh melebihi anggaran waktu operasi *real-time*. Strategi kedua, dipakai MV3D (bab 091) dan AVOD (bab 092), memproyeksikan *point cloud* ke peta ketinggian dan kepadatan yang dirancang manual dari sudut pandang atas (*bird's-eye view*/BEV) dan sudut pandang depan. Proyeksi ini menghindari konvolusi 3D, tetapi fiturnya bersifat tetap dan dirancang manusia, bukan dipelajari dari data, sehingga membatasi kemampuan model menyesuaikan representasi dengan pola data sebenarnya.

Kesenjangan yang tersisa: dibutuhkan encoder yang, seperti VoxelNet, mempelajari fiturnya sendiri dari titik mentah, tetapi seperti MV3D/AVOD, hanya memakai operasi 2D yang cepat. PointPillars mengisi celah itu.

## Ide Utama

Gagasan inti PointPillars adalah mengganti *voxel* 3D dengan *pillar*: kolom vertikal tanpa pembagian pada sumbu tinggi (z). Bidang datar x-y dibagi menjadi grid sel persegi; setiap sel diperluas menjadi satu kolom yang mencakup seluruh rentang tinggi *point cloud*. Karena tidak ada pembagian pada sumbu z, tidak diperlukan hyperparameter resolusi vertikal seperti pada *voxel* 3D, dan konvolusi 3D dapat dihindari sepenuhnya.

Fitur setiap *pillar* dipelajari, bukan dirancang manual: sebuah jaringan sederhana bergaya *PointNet* (jaringan yang memproses titik satu per satu lalu menggabungkannya dengan operasi tak bergantung urutan, seperti max-pooling) mengubah titik-titik dalam satu *pillar* menjadi satu vektor fitur. Vektor fitur tiap *pillar* ditempatkan kembali pada lokasi (x, y) asalnya, membentuk gambar semu (*pseudo-image*) dua dimensi, yang lalu diproses tulang punggung (*backbone*) CNN 2D standar dan kepala deteksi bergaya SSD (*Single Shot Detector*, detektor satu tahap yang memprediksi kotak langsung dari peta fitur tanpa tahap pengusulan wilayah terpisah — dibahas pada bab 015). Seluruh proses dari titik mentah sampai kotak 3D dilatih *end-to-end*.

## Cara Kerja Langkah demi Langkah

### Pembentukan Pillar dan Augmentasi Titik

Bidang x-y dibagi menjadi grid sel berukuran 0,16 × 0,16 meter. Setiap sel yang memuat minimal satu titik disebut *pillar* aktif. Karena jumlah *pillar* aktif berbeda antar citra, model membatasi jumlah maksimum *pillar* (P = 12.000 per citra) dan titik per *pillar* (N = 100); kelebihan diambil sampel acak, kekurangan diisi nol.

Setiap titik mentah memiliki empat nilai terukur: koordinat (x, y, z) dan r (intensitas pantulan/*reflectance* sinar laser). Nilai ini didekorasi (ditambah) lima nilai turunan: selisih (x, y, z) titik terhadap rata-rata aritmetik seluruh titik dalam *pillar*-nya (posisi relatif terhadap pusat massa *pillar*), serta selisih (x, y) titik terhadap titik tengah geometris sel *pillar*-nya. Dengan tambahan ini, setiap titik memiliki D = 9 dimensi fitur, dan seluruh citra direpresentasikan sebagai tensor (D=9, P=12.000, N=100).

### Pillar Feature Network (PFN)

Tensor titik yang telah didekorasi diproses satu lapis linear (setara konvolusi 1×1) diikuti *batch normalization* dan ReLU, menghasilkan C = 64 fitur per titik. Seluruh titik dalam satu *pillar* lalu digabung dengan max-pooling di sepanjang dimensi N (titik), menghasilkan satu vektor fitur berdimensi C = 64 untuk mewakili seluruh *pillar* — operasi yang membuat hasil tidak bergantung pada urutan titik, karena titik dalam satu *pillar* tidak memiliki urutan alami.

### Pemindaian Kembali ke Pseudo-Image

Vektor fitur tiap *pillar* ditempatkan kembali (*scatter*) ke lokasi (x, y) sel asalnya pada grid; sel tanpa *pillar* aktif diisi nol. Hasilnya adalah tensor tiga dimensi (C=64, H, W), secara struktural identik dengan citra biasa (tinggi H, lebar W, C kanal), sehingga alat CNN 2D standar dapat langsung dipakai tanpa modifikasi.

Alur data lengkap dari titik mentah sampai keluaran kotak dirangkum berikut ini.

```
titik mentah per titik: (x, y, z, r)          4 nilai per titik
        |  kelompokkan ke pillar pada bidang x-y (sel 0,16 x 0,16 m)
        v
tensor titik  (D=9, P=12.000, N=100)      D=9: 4 asli + 5 offset
        |  Pillar Feature Network (linear + BatchNorm + ReLU)
        v
fitur titik   (C=64, P=12.000, N=100)
        |  max-pooling atas dimensi N (titik dalam satu pillar)
        v
fitur pillar  (C=64, P=12.000)
        |  scatter ke lokasi (x, y) sel asal pillar
        v
pseudo-image  (C=64, H, W)                 setara citra 2D biasa
        |  backbone 2D CNN (3 blok downsample, gabung ke 6C=384)
        v
peta fitur gabungan  (384, H', W')
        |  kepala deteksi SSD (jangkar 2D per kelas, 2 orientasi)
        v
kotak 3D (x, y, z, l, w, h, yaw) + kelas + skor per jangkar
```

### Backbone 2D dan Kepala Deteksi

*Backbone* terdiri atas tiga blok konvolusi berurutan, masing-masing menurunkan resolusi spasial pseudo-image sambil menaikkan jumlah kanal (64, 128, dan 256 kanal, dengan 4, 6, dan 6 lapis konvolusi). Keluaran tiap blok diskalakan naik (*upsampling*) ke satu resolusi bersama lalu digabungkan (*concatenate*) menjadi satu peta fitur berkanal 384 (enam kali C=64), menyatukan fitur beresolusi kasar (konteks luas, cocok objek besar seperti mobil) dan fitur beresolusi halus (detail lokal, cocok objek kecil seperti pejalan kaki).

Kepala deteksi mengikuti gaya SSD: pada setiap lokasi grid ditempatkan kotak jangkar (*anchor*) berukuran tetap sesuai statistik ukuran objek per kelas (misalnya jangkar mobil berukuran 1,6 × 3,9 × 1,5 meter), masing-masing dalam dua orientasi (0° dan 90°). Jaringan memprediksi selisih (residual) posisi, ukuran, dan sudut hadap terhadap jangkar terdekat, bukan koordinat mutlak. Kecocokan jangkar dengan kotak kebenaran (*ground truth*) ditentukan memakai IOU (*Intersection over Union*, rasio luas irisan terhadap gabungan) pada bidang BEV.

### Fungsi Loss dan Pelatihan

Pelatihan memakai tiga komponen loss yang sama dengan SECOND (metode voxel-3D pembanding utama). Loss klasifikasi memakai *focal loss* (menurunkan bobot contoh mudah, memusatkan pembelajaran pada contoh sulit; α=0,25, γ=2), penting karena jangkar latar belakang jauh lebih banyak daripada jangkar berisi objek. Loss lokalisasi memakai *Smooth L1* pada tujuh parameter kotak (x, y, z, panjang, lebar, tinggi, sudut hadap). Karena regresi sudut saja tidak dapat membedakan kotak dengan orientasi terbalik 180°, ditambahkan loss klasifikasi arah berupa *softmax* dua kelas (maju/mundur). Ketiga loss dijumlahkan dengan bobot berbeda (2 lokalisasi, 1 klasifikasi, 0,2 arah) dan dinormalkan dengan jumlah jangkar positif.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada *benchmark* KITTI (kumpulan data deteksi objek berkendara otonom dari Karlsruhe Institute of Technology, tiga kelas: mobil, pejalan kaki, pesepeda; tiga tingkat kesulitan berdasarkan ukuran, oklusi, dan pemotongan citra objek: mudah, sedang, sulit). Metrik yang dipakai adalah AP (*average precision*) pada evaluasi kotak 3D penuh dan proyeksi BEV, dibandingkan dengan VoxelNet, SECOND, F-PointNet (fusi kamera-LiDAR), MV3D, dan AVOD.

Pada tingkat kesulitan sedang di data uji KITTI, AP 3D kelas mobil PointPillars mencapai 74,99% pada 62 Hz, mengungguli SECOND (73,66% AP, 20 Hz) dan VoxelNet (65,11% AP, 4,4 Hz), serta F-PointNet (70,39% AP, 5,9 Hz) yang memakai fusi kamera dan LiDAR. Untuk BEV, AP kesulitan sedang PointPillars adalah 86,10% (mobil), 50,23% (pejalan kaki), dan 62,25% (pesepeda). Interpretasinya: PointPillars unggul akurasi atas seluruh metode LiDAR-saja yang dibandingkan, sekaligus tiga kali lebih cepat dari SECOND dan lebih dari sepuluh kali lebih cepat dari VoxelNet — capaian ini didapat tanpa data kamera sama sekali, mengungguli F-PointNet yang justru memakai informasi tambahan dari citra.

Rincian waktu inferensi menunjukkan sumber utama percepatan: dari total 16,2 milidetik (62 Hz), penyaringan titik memakan 1,4 ms, pembentukan *pillar* 2,7 ms, unggah data ke GPU 2,9 ms, PFN hanya 1,3 ms, dan *backbone* beserta kepala deteksi 7,7 ms. Angka 1,3 ms untuk PFN kontras tajam dengan 190 ms untuk pengkodean fitur voxel 3D VoxelNet — selisih inilah yang menjelaskan sebagian besar keunggulan kecepatan PointPillars. Varian yang dipercepat lebih lanjut, dengan grid lebih kasar dan optimisasi TensorRT, mencapai 9 ms (105 Hz) dengan akurasi sedikit menurun.

Studi ablasi (pengujian pengaruh satu komponen dengan menonaktifkan/mengubahnya) menunjukkan encoder yang dipelajari (PFN) secara konsisten mengungguli encoder tetap berbasis fitur tangan pada seluruh resolusi grid yang diuji, dan augmentasi titik dengan offset posisi menambah sekitar 0,5 poin mAP (*mean average precision*, rata-rata AP di seluruh kelas).

## Kelebihan dan Keterbatasan

Kelebihan utama PointPillars adalah kesederhanaan arsitektur: seluruh operasi setelah pembentukan *pillar* memakai konvolusi 2D standar, tanpa konvolusi 3D atau fitur buatan tangan, sehingga mudah diimplementasikan dan mudah dipercepat perangkat keras yang sudah dioptimalkan untuk CNN 2D. Kombinasi kecepatan (62–105 Hz) dan akurasi yang mengungguli metode LiDAR-saja lain, bahkan sebagian metode fusi, menjadikannya pilihan praktis untuk aplikasi *real-time* seperti kendaraan otonom.

Dari sisi rekayasa, max-pooling pada Pillar Feature Network menyatukan seluruh titik dalam satu kolom vertikal menjadi satu vektor, sehingga sebagian informasi struktur vertikal di dalam *pillar* — misalnya perbedaan bentuk pada ketinggian berbeda dalam satu objek — tidak dipertahankan secara eksplisit setelahnya. Secara konseptual, PointPillars hanya memproses data LiDAR sehingga tidak memakai informasi warna atau tekstur dari kamera; ketiadaan ini membatasi kemampuan model membedakan objek dengan bentuk geometris mirip namun kelas berbeda. Ukuran sel grid yang seragam juga berarti objek jauh atau kecil, yang tercakup lebih sedikit titik LiDAR, direpresentasikan dengan lebih sedikit informasi dibanding objek dekat — konsisten dengan AP pejalan kaki (43,53–51,91% pada berbagai kesulitan) yang jauh di bawah AP mobil.

## Kaitan dengan Bab Lain

PointPillars secara langsung menjawab kelemahan komputasi VoxelNet (bab 087): dengan mengganti *voxel* dan konvolusi 3D dengan *pillar* dan konvolusi 2D, PFN pada makalah ini menggantikan tahap pengkodean fitur yang memakan 190 ms pada VoxelNet menjadi 1,3 ms, sementara akurasi tetap meningkat. Arsitektur *pillar*-nya menjadi kerangka dasar bagi metode fusi sensor sesudahnya: [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md) menambahkan skor semantik dari jaringan segmentasi citra ke tiap titik LiDAR sebelum diproses backbone bergaya PointPillars, dan [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md) memakai representasi BEV serupa untuk menggabungkan fitur kamera dan LiDAR. Untuk pendekatan yang tidak bergantung pada LiDAR sama sekali, [095 - 2019 - Pseudo-LiDAR - Deteksi 3D](./095%20-%202019%20-%20Pseudo-LiDAR%20-%20Deteksi%203D.md) membangun *point cloud* semu dari citra kedalaman kamera monokular/stereo untuk diproses dengan encoder sejenis PointPillars.

## Poin untuk Sitasi

Kutip dengan kunci `lang2019pointpillars`. Ringkasan aman dikutip: "PointPillars meng-encode *point cloud* menjadi kolom vertikal (*pillar*) yang diproses jaringan bergaya PointNet, memungkinkan seluruh pipeline deteksi 3D berjalan dengan konvolusi 2D; pada KITTI, metode ini mencapai 74,99% AP 3D kelas mobil (tingkat sedang) pada 62 Hz, mengungguli VoxelNet dan SECOND baik akurasi maupun kecepatan." Angka AP 3D/BEV, waktu inferensi (190 ms VoxelNet vs 1,3 ms PFN), dan parameter loss (α, γ, bobot β) diperoleh dari salinan HTML naskah (ar5iv) karena versi CVF Open Access memblokir pengambilan otomatis; verifikasi ulang terhadap Tabel 1 dan 2 makalah asli dianjurkan sebelum dikutip dalam karya formal, khususnya angka pada tingkat kesulitan mudah dan sulit yang tidak dibahas rinci di sini.
