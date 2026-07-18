# 186 - PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shi2020pvrcnn` |
| Judul asli | PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection |
| Penulis | Shaoshuai Shi, Chaoxu Guo, Li Jiang, Zhe Wang, Jianping Shi, Xiaogang Wang, Hongsheng Li |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1912.13192
- **Google Scholar:** https://scholar.google.com/scholar?q=PV-RCNN%3A%20Point-Voxel%20Feature%20Set%20Abstraction%20for%203D%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PV-RCNN%3A%20Point-Voxel%20Feature%20Set%20Abstraction%20for%203D%20Object%20Detection&sort=relevance

## Gambaran Umum

PV-RCNN (*Point-Voxel Region-based Convolutional Neural Network*) adalah detektor objek 3D dua tahap untuk *point cloud* (kumpulan titik koordinat 3D hasil pemindaian LiDAR) yang menggabungkan dua representasi data yang sebelumnya dipakai terpisah oleh metode lain: representasi voxel (sel kubus hasil diskretisasi ruang 3D) yang diproses dengan konvolusi jarang (*sparse convolution*), dan representasi titik mentah yang diproses dengan operasi *set abstraction* bergaya PointNet++. Masalah yang dipecahkan adalah trade-off antara kecepatan/efisiensi memori (kekuatan metode berbasis voxel) dan presisi lokasi (kekuatan metode berbasis titik) yang pada metode-metode terdahulu harus dipilih salah satu.

Mekanisme intinya adalah modul *voxel set abstraction* (VSA) yang meringkas fitur multiskala dari *backbone* voxel 3D ke sejumlah kecil titik kunci (*keypoint*), lalu modul *RoI-grid pooling* yang mengumpulkan fitur dari keypoint tersebut untuk menyempurnakan proposal kotak 3D pada tahap kedua. Pada tolok ukur KITTI, PV-RCNN mencapai *average precision* (AP) 3D sebesar 81,43% untuk kelas mobil pada tingkat kesulitan sedang (*moderate*) di set uji resmi, menempati posisi pertama papan peringkat KITTI pada saat publikasi, mengungguli metode terbaik sebelumnya sebesar 1,72 poin persentase. Kode sumber resmi tersedia pada repositori `sshaoshuai/PV-RCNN` dan kemudian diintegrasikan ke *toolbox* OpenPCDet.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek 3D dari *point cloud* LiDAR menghadapi masalah representasi data yang berbeda dari citra RGB: titik-titik pindaian tersebar tidak beraturan di ruang 3D dan jumlahnya bervariasi antarwilayah (padat dekat sensor, jarang di kejauhan). Dua strategi representasi berkembang untuk mengatasinya. Strategi pertama, berbasis voxel, membagi ruang 3D menjadi sel-sel voxel beraturan lalu memproses sel berisi titik dengan konvolusi 3D jarang — pendekatan yang dipakai SECOND (*Sparsely Embedded Convolutional Detection*), metode deteksi 3D yang memanfaatkan konvolusi jarang untuk efisiensi komputasi pada data voxel yang sebagian besar kosong. Strategi ini efisien dan menghasilkan fitur konteks yang kaya karena reseptif konvolusi menutupi area luas, tetapi proses voxelisasi membuang informasi lokasi titik yang presisi karena banyak titik dipetakan ke satu sel voxel yang sama.

Strategi kedua, berbasis titik, memproses *point cloud* mentah langsung dengan operasi *set abstraction* seperti pada PointNet++ — arsitektur jaringan yang mengelompokkan titik-titik bertetangga secara hierarkis dan mengekstrak fitur tanpa diskretisasi ruang. PointRCNN, metode deteksi 3D dua tahap yang mengusulkan proposal langsung dari titik, memanfaatkan strategi ini untuk mempertahankan presisi lokasi. Kelemahannya, operasi pencarian tetangga pada titik mentah berbiaya komputasi tinggi dan sulit diskalakan ke *point cloud* berukuran besar seperti pada Waymo Open Dataset yang berisi ratusan ribu titik per pemindaian. Part-A2, metode lain yang membagi objek menjadi bagian-bagian (*parts*) untuk penyempurnaan kotak, juga menghadapi batasan serupa dalam memadukan efisiensi dan presisi. Masalah ini penting karena deteksi 3D akurat dan cepat merupakan prasyarat persepsi kendaraan otonom dan robotika, sehingga metode yang hanya unggul di satu sisi (kecepatan atau presisi) tidak memadai untuk penerapan nyata.

## Ide Utama

Gagasan inti PV-RCNN adalah memakai representasi voxel untuk menghasilkan proposal kotak 3D secara efisien, kemudian memakai representasi titik hanya pada sejumlah kecil lokasi terpilih (keypoint) untuk memperkaya fitur proposal tersebut sebelum penyempurnaan akhir. Alih-alih memproses seluruh titik mentah seperti metode berbasis titik murni, PV-RCNN terlebih dahulu menjalankan *backbone* voxel 3D jarang untuk menghasilkan peta fitur multiskala dan proposal awal. Sejumlah kecil keypoint — misalnya 2.048 titik untuk KITTI — kemudian dipilih dari *point cloud* asli dengan algoritme *furthest point sampling* (pengambilan sampel titik yang secara iteratif memilih titik terjauh dari titik-titik yang sudah terpilih, sehingga hasil samplingnya tersebar merata).

Pada setiap keypoint, modul *voxel set abstraction* mengumpulkan fitur dari beberapa level *backbone* voxel di sekitarnya menggunakan operasi *set abstraction* PointNet++, sehingga satu keypoint mewakili konteks multiskala dari voxel-voxel di sekelilingnya. Dengan cara ini, sejumlah kecil keypoint menjadi representasi ringkas dari seluruh *scene* yang tetap membawa presisi lokasi titik. Fitur keypoint tersebut kemudian dipakai untuk menyempurnakan proposal kotak 3D pada tahap kedua, menggantikan pendekatan yang langsung mem-pool fitur dari grid voxel proposal (yang kurang presisi) atau dari seluruh titik mentah (yang mahal).

## Cara Kerja Langkah demi Langkah

### Tahap Pertama: Backbone Voxel 3D dan Proposal Awal

*Point cloud* masukan dibagi menjadi voxel-voxel kecil, lalu diproses oleh *backbone* konvolusi 3D jarang bertingkat (mengikuti desain SECOND) yang menghasilkan peta fitur pada beberapa resolusi (voxel berukuran 1×, 2×, 4×, dan 8× dari resolusi awal). Peta fitur pada resolusi terkasar diproyeksikan ke tampak-atas (*bird's-eye view*/BEV) untuk menghasilkan proposal kotak 3D awal melalui kepala deteksi *region proposal network* (RPN) satu tahap, serupa dengan mekanisme SECOND.

### Voxel Set Abstraction (VSA): Meringkas Voxel ke Keypoint

Modul VSA adalah komponen inti yang menjembatani representasi voxel dan titik. Untuk setiap keypoint (dipilih dengan *furthest point sampling* dari titik asli, n = 2.048 untuk KITTI dan n = 4.096 untuk Waymo), VSA mengumpulkan fitur dari voxel-voxel bertetangga pada empat level *backbone* sekaligus: fitur ini digabung dengan fitur voxel mentah, fitur BEV, dan koordinat titik asli. Penggabungan ini membuat setiap keypoint membawa informasi dari berbagai skala resolusi spasial dalam satu vektor fitur.

Diagram berikut merangkum alur dari *point cloud* ke keypoint hingga penyempurnaan proposal:

```
point cloud LiDAR
      |
      v
voxelisasi -> backbone konvolusi 3D jarang (4 level resolusi)
      |                                  |
      v                                  v
proyeksi BEV -> proposal RPN      Voxel Set Abstraction (VSA)
      |                            (furthest point sampling,
      |                             n=2048 keypoint, gabung
      |                             fitur 4 level + BEV + raw)
      |                                  |
      +---------------> keypoint dengan fitur multiskala
                                  |
                                  v
                    Predicted Keypoint Weighting (PKW)
                    (bobot ulang keypoint foreground)
                                  |
                                  v
                    RoI-grid pooling (grid 6x6x6 per proposal)
                                  |
                                  v
                    penyempurnaan kotak 3D + skor keyakinan
```

Diagram ini menunjukkan bahwa VSA bekerja paralel dengan cabang RPN: cabang atas menghasilkan proposal kasar dari BEV, sedangkan cabang bawah membangun representasi keypoint yang kaya konteks untuk dipakai pada tahap penyempurnaan.

### Predicted Keypoint Weighting (PKW): Menonjolkan Titik Foreground

Karena keypoint dipilih dengan sampling geometris tanpa mempertimbangkan apakah titik tersebut berada pada objek (*foreground*) atau latar (*background*), sebagian keypoint akan jatuh pada wilayah kosong yang kurang informatif. Modul PKW mengatasi ini dengan jaringan tiga lapis *multilayer perceptron* (MLP) berfungsi sigmoid yang memprediksi peluang setiap keypoint tergolong *foreground*, dilatih dengan pengawasan segmentasi titik memakai *focal loss* (fungsi *loss* yang menekan kontribusi contoh mudah dan menonjolkan contoh sulit). Skor ini dipakai untuk membobot ulang fitur keypoint sebelum dipakai pada tahap penyempurnaan, sehingga keypoint pada objek memberi kontribusi lebih besar dibandingkan keypoint pada latar kosong.

### RoI-Grid Pooling: Penyempurnaan Proposal

Untuk setiap proposal kotak 3D dari RPN, PV-RCNN menempatkan grid keteraturan 6×6×6 titik grid di dalam kotak proposal. Setiap titik grid mengumpulkan fitur dari keypoint-keypoint di sekitarnya (dalam radius tertentu) melalui operasi *set abstraction*, menghasilkan representasi proposal yang padat dan seragam meskipun jumlah titik asli di dalam kotak bervariasi. Fitur dari 216 titik grid (6×6×6) tersebut digabung dan diproses oleh jaringan penyempurnaan (*refinement head*) dua cabang: satu memprediksi koreksi posisi/ukuran/orientasi kotak, satu lagi memprediksi skor keyakinan yang mengukur kualitas *Intersection over Union* (IoU) antara kotak akhir dan kebenaran tanah.

### Pelatihan

Jaringan dilatih menyeluruh (*end-to-end*) dengan gabungan beberapa fungsi *loss*: *loss* proposal RPN, *loss* segmentasi keypoint untuk PKW, dan *loss* regresi/klasifikasi pada tahap penyempurnaan. Pada KITTI, pelatihan penuh memakan waktu sekitar 5 jam pada 8 GPU GTX 1080Ti.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dua dataset. KITTI adalah tolok ukur deteksi 3D untuk skenario berkendara yang berisi pemindaian LiDAR beranotasi kotak 3D untuk kelas mobil, pejalan kaki, dan pengendara sepeda (*cyclist*), dengan tiga tingkat kesulitan (*easy*, *moderate*, *hard*) berdasarkan ukuran, oklusi, dan pemotongan objek. Waymo Open Dataset adalah dataset berskala lebih besar dengan jumlah *scene* dan kepadatan titik jauh melampaui KITTI, dipakai untuk menguji skalabilitas metode. Metrik utama adalah AP 3D, yaitu rata-rata presisi yang memperhitungkan ketepatan kotak 3D terhadap kebenaran tanah pada ambang IoU tertentu.

Pada set uji resmi KITTI, PV-RCNN mencapai AP 3D sebesar 81,43% untuk kelas mobil pada tingkat kesulitan sedang, unggul 1,72 poin persentase dari metode terbaik sebelumnya (STD, 79,71%) dan menempatkannya pada posisi pertama papan peringkat KITTI untuk deteksi mobil pada saat publikasi, mengalahkan metode LiDAR-saja maupun metode gabungan LiDAR-kamera. Sebagai perbandingan, metode berbasis voxel murni SECOND mencapai 72,55% pada metrik yang sama, PointRCNN berbasis titik murni mencapai 75,64%, dan Part-A2-Net mencapai 78,49%. Interpretasinya: selisih 8-9 poin terhadap SECOND menunjukkan bahwa penambahan cabang berbasis titik memberi kontribusi presisi lokasi yang signifikan dibandingkan voxel saja, sementara keunggulan atas PointRCNN menunjukkan manfaat proposal awal yang efisien dari cabang voxel.

Studi ablasi pada set validasi KITTI menguji kontribusi tiap komponen fitur pada VSA. Model yang hanya memakai fitur titik mentah mencapai 81,98% AP (moderate); model penuh yang menggabungkan fitur voxel multiskala dari empat level *backbone* dengan fitur BEV dan fitur titik mentah mencapai 84,83% AP (moderate). Selisih hampir 3 poin ini mengindikasikan bahwa fitur voxel multiskala menambah konteks yang tidak tersedia dari titik mentah saja, mendukung klaim utama makalah bahwa kombinasi kedua representasi lebih baik daripada salah satunya. Pada Waymo Open Dataset, makalah melaporkan bahwa PV-RCNN mengungguli metode pembanding dengan margin besar, tetapi angka mAP/mAPH per level kesulitan pada rilis awal makalah ini tidak berhasil diverifikasi secara konsisten dari sumber sekunder pada penelusuran ini dan perlu dicek langsung ke tabel makalah sebelum dikutip.

## Kelebihan dan Keterbatasan

Kelebihan utama PV-RCNN adalah presisi lokasi yang tinggi berkat kombinasi konteks voxel multiskala dan detail geometris dari titik mentah, dibuktikan oleh posisi teratas papan peringkat KITTI pada saat publikasi. Modul PKW memberi mekanisme eksplisit untuk memprioritaskan keypoint yang informatif, mengurangi pemborosan kapasitas model pada titik latar kosong. Desain dua tahap (proposal cepat dari voxel, penyempurnaan presisi dari keypoint) memisahkan tanggung jawab kecepatan dan akurasi secara efisien dibandingkan memproses seluruh titik mentah pada kedua tahap.

Dari sisi rekayasa, kombinasi dua representasi menambah kompleksitas komputasi dan memori dibandingkan metode satu representasi: setiap keypoint memerlukan operasi pencarian tetangga pada beberapa level voxel, dan proposal memerlukan operasi RoI-grid pooling tambahan, sehingga PV-RCNN secara desain lebih lambat daripada detektor satu tahap seperti SECOND meski makalah aslinya tidak melaporkan angka *frame per second* secara eksplisit dalam sumber yang diverifikasi pada penelusuran ini. Secara konseptual, pemilihan jumlah keypoint (2.048 untuk KITTI) merupakan hyperparameter tetap yang tidak otomatis menyesuaikan kepadatan titik pada *scene* berbeda, sehingga pada *point cloud* yang jauh lebih besar seperti Waymo, jumlah keypoint dinaikkan (4.096) sebagai penyesuaian manual. Ketergantungan penuh pada data LiDAR juga berarti metode ini tidak memanfaatkan informasi tekstur dari kamera RGB, berbeda dengan metode fusi LiDAR-kamera yang berkembang setelahnya.

## Kaitan dengan Bab Lain

PV-RCNN mewarisi *backbone* konvolusi voxel jarang dari SECOND dan gagasan proposal berbasis titik dari PointRCNN dan Part-A2, memadukan keduanya melalui modul VSA yang menjadi kontribusi orisinalnya. Dibandingkan dengan bab 185 (CenterPoint), yang memakai representasi *center-based* satu tahap tanpa anchor pada peta fitur voxel/pillar untuk mengejar kecepatan, PV-RCNN menempuh jalur dua tahap yang mengutamakan presisi dengan biaya komputasi lebih tinggi. Bab 187 (BEVFormer) dan bab 188 (DETR3D) berada pada jalur berbeda: keduanya mengandalkan kamera multi-tampilan dan mekanisme atensi berbasis *transformer* untuk deteksi 3D tanpa LiDAR, sehingga menjadi pembanding arsitektural terhadap PV-RCNN yang murni berbasis titik LiDAR. Modul *voxel set abstraction* pada PV-RCNN memakai prinsip *set abstraction* PointNet++ (operasi pengelompokan dan agregasi fitur titik hierarkis), sehingga bab ini juga berkaitan dengan literatur pemrosesan *point cloud* berbasis PointNet apabila entri tersebut dibahas pada bagian lain tinjauan.

- [185 - 2021 - CenterPoint - Deteksi 3D](./185%20-%202021%20-%20CenterPoint%20-%20Deteksi%203D.md)
- [187 - 2022 - BEVFormer - Deteksi 3D](./187%20-%202022%20-%20BEVFormer%20-%20Deteksi%203D.md)
- [188 - 2022 - DETR3D - Deteksi 3D](./188%20-%202022%20-%20DETR3D%20-%20Deteksi%203D.md)

## Poin untuk Sitasi

Kutip dengan kunci `shi2020pvrcnn`. Ringkasan yang aman dikutip: "PV-RCNN menggabungkan *backbone* konvolusi voxel 3D jarang dengan modul *voxel set abstraction* berbasis PointNet++ untuk meringkas fitur multiskala ke sejumlah keypoint, kemudian menyempurnakan proposal kotak 3D melalui RoI-grid pooling, mencapai 81,43% AP 3D (moderate, kelas mobil) pada set uji resmi KITTI dan menempati posisi pertama papan peringkat pada saat publikasi (CVPR 2020)." Angka ablasi studi (81,98% vs 84,83% AP moderate pada set validasi), jumlah keypoint (2.048 untuk KITTI, 4.096 untuk Waymo), dan ukuran grid RoI-grid pooling (6×6×6) berasal dari isi makalah dan sebaiknya dicek ulang terhadap tabel asli sebelum dikutip dalam karya formal. Angka hasil kuantitatif pada Waymo Open Dataset (mAP/mAPH per kelas dan level kesulitan) tidak berhasil diverifikasi secara konsisten pada penelusuran ini dan wajib dikonfirmasi langsung ke makalah sebelum disitasi.
