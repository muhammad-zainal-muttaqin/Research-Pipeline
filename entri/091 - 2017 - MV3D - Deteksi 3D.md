# 091 - Multi-View 3D Object Detection Network for Autonomous Driving

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2017mv3d` |
| Judul asli | Multi-View 3D Object Detection Network for Autonomous Driving |
| Penulis | Xiaozhi Chen, Huimin Ma, Ji Wan, Bo Li, Tian Xia |
| Tahun | 2017 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1611.07759
- **Google Scholar:** https://scholar.google.com/scholar?q=Multi-View%203D%20Object%20Detection%20Network%20for%20Autonomous%20Driving
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Multi-View%203D%20Object%20Detection%20Network%20for%20Autonomous%20Driving&sort=relevance

## Gambaran Umum

MV3D (*Multi-View 3D Object Detection Network*) memperkenalkan kerangka fusi sensor yang memadukan titik awan (*point cloud*) dari LiDAR dengan citra RGB untuk mendeteksi objek 3D pada skenario berkendara otonom. Alih-alih memproses satu modalitas sensor, jaringan ini menghasilkan usulan kotak 3D (*3D proposal*) dari representasi tampak-atas (*bird's-eye view*, BEV) titik LiDAR, kemudian menggabungkan fitur dari tiga tampilan berbeda — BEV, tampak-depan (*front view*, FV), dan citra RGB — melalui mekanisme fusi berbasis wilayah (*region-based fusion*) yang disebut *deep fusion*.

Pada tolok ukur KITTI, kombinasi ketiga tampilan (BEV+FV+RGB) mencapai *average precision* 3D (AP3D) sebesar 62,68% untuk kelas mobil pada tingkat kesulitan sedang (IoU 0,7), jauh melampaui VeloFCN berbasis LiDAR tunggal (13,66%) dan 3DOP berbasis stereo (5,07%). Makalah ini adalah salah satu rujukan paling awal yang mempertemukan geometri LiDAR dan tekstur kamera secara terpadu, dan pola desainnya — proposal dari BEV, fusi berbasis wilayah — banyak diwarisi atau ditantang oleh metode fusi 3D sesudahnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum MV3D, deteksi 3D untuk kendaraan otonom umumnya bertumpu pada satu modalitas sensor saja, dan masing-masing memiliki kekurangan struktural. Metode berbasis citra tunggal seperti Mono3D memperkirakan kedalaman secara tidak langsung dari petunjuk visual (ukuran objek, garis horizon, bayangan), sehingga estimasi jarak dan volume 3D-nya kasar. Metode berbasis stereo seperti 3DOP menghitung peta disparitas dari sepasang kamera, tetapi disparitas rentan galat pada objek jauh atau permukaan tanpa tekstur. Metode berbasis LiDAR seperti VeloFCN dan Vote3Deep memiliki geometri paling akurat, karena LiDAR mengukur jarak langsung dengan sinar laser, tetapi titik yang dihasilkan jarang (*sparse*) — semakin jauh objek, semakin sedikit titik yang mengenainya — dan sama sekali tidak membawa informasi tekstur atau warna.

Ketiadaan satu sumber data yang lengkap membuat ketiga pendekatan tunggal itu saling menutupi kelemahan yang berbeda: LiDAR presisi secara geometris namun jarang, sedangkan RGB kaya tekstur namun tak memiliki kedalaman. Masalah kedua yang belum terpecahkan pada masanya adalah cara menyelaraskan (*align*) data dari sensor dengan bentuk representasi yang sangat berbeda — titik 3D tak berurutan versus grid piksel 2D — agar keduanya dapat diproses oleh satu jaringan konvolusi yang sama, mengingat arsitektur seperti Faster R-CNN (bab 014) yang menjadi dasar rancangan region proposal pada MV3D awalnya dirancang murni untuk citra 2D.

## Ide Utama

Gagasan inti MV3D adalah memproyeksikan titik LiDAR ke dua representasi 2D terstruktur — BEV dan FV — sehingga jaringan konvolusi standar dapat memprosesnya seperti citra biasa, lalu memakai BEV sebagai sumber utama usulan kotak 3D karena tampak atas mempertahankan ukuran fisik objek dan menghindari masalah oklusi (objek satu menutupi objek lain) yang muncul pada tampak depan. Usulan 3D yang dihasilkan dari BEV kemudian diproyeksikan ke ketiga tampilan (BEV, FV, RGB), fitur dari masing-masing wilayah diekstrak, dan fitur itu digabung secara bertahap di beberapa lapis jaringan, bukan hanya sekali di awal atau di akhir. Dengan begitu, jaringan mempelajari cara memadukan geometri LiDAR dan tekstur RGB secara langsung dari data, bukan lewat aturan tangan.

## Cara Kerja Langkah demi Langkah

### Representasi Tiga Tampilan

BEV disusun dengan membagi ruang titik LiDAR di sekitar kendaraan (rentang 0–70,4 meter ke depan dan −40 hingga 40 meter ke samping pada data KITTI) menjadi sel berukuran 0,1×0,1 meter, sehingga terbentuk peta berukuran sekitar 704×800 sel. Setiap sel diberi tiga jenis kanal: kanal ketinggian (*height*) sebanyak M lapis, masing-masing berisi ketinggian maksimum titik pada irisan ketinggian tertentu; satu kanal intensitas, berisi pantulan (*reflectance*) dari titik tertinggi pada sel; dan satu kanal kerapatan (*density*), dihitung sebagai min(1,0 ; log(N+1)/log(64)) dengan N jumlah titik dalam sel — rumus ini menormalkan kerapatan agar tidak melonjak tak terbatas saat titik sangat banyak. Total kanal BEV adalah M+2.

FV dibentuk dengan memproyeksikan titik 3D ke bidang silinder memakai sudut azimut dan elevasi, menghasilkan peta berukuran 64×512 untuk sensor LiDAR 64-balok (Velodyne HDL-64E), dengan tiga kanal: ketinggian, jarak, dan intensitas. Citra RGB diskalakan ulang sehingga sisi terpendeknya berukuran 500 piksel. Ketiga representasi ini memakai satuan ukur yang berbeda-beda (meter untuk BEV/FV, piksel untuk RGB), sehingga proyeksi antar-tampilan memerlukan kalibrasi geometris yang menghubungkan koordinat LiDAR dengan bidang citra kamera.

### Pembangkitan Usulan 3D dari BEV

Jaringan usulan wilayah (*region proposal network*, RPN — konsep yang sama dipakai Faster R-CNN untuk mengusulkan kotak kandidat 2D) diterapkan pada peta fitur BEV yang telah diperbesar dua kali lipat lewat dekonvolusi. Pada tiap posisi, empat kotak awal (*prior box*) diletakkan, dimensinya diambil dari dua kelompok ukuran mobil hasil pengelompokan data nyata (3,9×1,6 meter dan 1,0×0,6 meter), dengan orientasi dibatasi pada 0° atau 90° pada tahap usulan ini — orientasi presisi disempurnakan pada tahap berikutnya. Dari seluruh kandidat, 2.000 kotak teratas dipertahankan saat pelatihan dan disaring dengan *Non-Maximum Suppression* berambang IoU 0,7, menyisakan 300 kotak saat pengujian.

### Fusi Mendalam Berbasis Wilayah (Deep Fusion)

Setiap usulan 3D diproyeksikan ke tiga tampilan, dan fitur pada wilayah proyeksi itu diekstrak dengan *ROI pooling* (pemetaan wilayah beragam ukuran ke fitur berukuran tetap) dari peta fitur BEV, FV, dan RGB. Fitur ketiganya lalu digabung memakai operasi rata-rata elemen per elemen (*element-wise mean*), bukan sekadar digabungkan (*concatenate*) satu kali. Skema ini disebut *deep fusion* karena penggabungan dilakukan berulang di beberapa lapis jaringan berikutnya: keluaran gabungan pada satu lapis diproses lagi oleh cabang paralel per tampilan sebelum digabung ulang di lapis selanjutnya. Susunan ini dikontraskan dengan dua alternatif yang lebih sederhana: *early fusion* (fitur ketiga tampilan digabung sekali saja di awal) dan *late fusion* (masing-masing tampilan diproses terpisah sampai akhir, baru digabung sebelum keluaran).

Diagram berikut meringkas alur fusi tersebut:

```
tampilan:      BEV          FV          RGB
                |            |            |
usulan 3D  -> proyeksi -> proyeksi -> proyeksi
                |            |            |
             ROI pool     ROI pool     ROI pool
                |            |            |
                f_BV ------ f_FV ------ f_RGB
                     \       |       /
                  rata-rata elemen per elemen
                             |
                       lapis gabungan
                     (diulang beberapa kali,
                      cabang per-tampilan
                      diproses lagi di antaranya)
                             |
                 keluaran: kelas + kotak 3D
```

Selama pelatihan, jaringan juga memakai jalur bantu (*auxiliary path*) berbobot sama yang dihubungkan ke tiap cabang tampilan sebelum fusi, dilatih dengan *drop-path* — sebagian jalur tampilan dimatikan secara acak (baik satu tampilan penuh maupun satu simpul tertentu) agar jaringan tidak bergantung berlebihan pada satu tampilan saja. Jalur bantu ini dibuang saat inferensi. Jaringan dasar memakai VGG-16 dengan jumlah kanal dipangkas separuh, menghasilkan total parameter sekitar 75% dari VGG-16 asli.

### Fungsi Loss dan Inferensi

Pelatihan memakai dua jenis loss: *cross-entropy* untuk klasifikasi (skor keberadaan objek pada tahap usulan, skor kelas pada tahap akhir) dan *smooth L1* untuk regresi parameter kotak (koordinat kotak 3D pada tahap usulan, selisih sudut kotak berorientasi pada tahap akhir). Pada tahap inferensi, jaringan memproses satu bingkai data dalam sekitar 0,36 detik pada GPU GeForce Titan X — jauh dari kecepatan waktu-nyata (*real-time*) yang dicapai detektor RGB murni seperti YOLO (bab 001), karena beban komputasi tambahan dari pemrosesan tiga tampilan sekaligus.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tolok ukur KITTI 3D Object Detection untuk kelas mobil, dengan metrik *average precision* untuk lokalisasi 3D (APloc, mengabaikan ketinggian kotak) dan deteksi 3D penuh (AP3D), diukur pada dua ambang IoU: 0,5 (longgar) dan 0,7 (ketat, menjadi standar pada penelitian berikutnya). Pada IoU 0,7 tingkat sedang (*moderate* — kategori kesulitan standar KITTI berdasarkan tinggi kotak, oklusi, dan pemotongan citra), MV3D penuh (BV+FV+RGB) mencapai AP3D 62,68%, dibandingkan VeloFCN 13,66%, 3DOP 5,07%, dan Mono3D 2,31%. Artinya, menambahkan fusi tiga tampilan menghasilkan AP hampir lima kali lipat dari metode LiDAR tunggal terbaik saat itu, dan lebih dari sepuluh kali lipat dari metode berbasis stereo. Pada tingkat mudah dan sulit, AP3D masing-masing 71,29% dan 56,56%.

Ablasi kombinasi tampilan pada IoU 0,5 tingkat sedang menunjukkan kontribusi tiap tampilan: BEV sendiri mencapai 85,50%, RGB sendiri 68,86%, dan FV sendiri hanya 56,30% — FV paling lemah karena proyeksi silinder menimbulkan distorsi bentuk pada objek jauh. Menambahkan RGB pada kombinasi BEV+FV menaikkan AP dari 87,65% menjadi 89,05%, mengonfirmasi bahwa tekstur kamera tetap memberi informasi pelengkap meskipun BEV sudah kuat. Ablasi strategi fusi menunjukkan *deep fusion* dengan jalur bantu (89,05%) mengungguli *deep fusion* tanpa jalur bantu (88,29%), *late fusion* (87,70%), dan *early fusion* (87,60%) — selisihnya kecil namun konsisten, menunjukkan bahwa penggabungan bertahap memberi sedikit keuntungan dibanding penggabungan tunggal. Makalah juga melaporkan AP deteksi 2D pada citra kamera yang lebih tinggi dibanding metode berbasis LiDAR lain pada set uji KITTI, meski angka rinci tabel tersebut sebaiknya dicek ulang ke naskah asli.

## Kelebihan dan Keterbatasan

Kelebihan utama MV3D adalah menjadi salah satu perintis fusi multi-tampilan berbasis wilayah untuk deteksi 3D, dengan pilihan BEV sebagai sumber usulan yang terbukti secara empiris lebih informatif daripada FV maupun RGB sendirian. Skema *deep fusion* dengan jalur bantu menunjukkan bahwa penggabungan bertahap, dilatih dengan regularisasi *drop-path*, memberi hasil sedikit lebih baik daripada penggabungan sekali di awal atau akhir. Perbaikan AP yang besar atas baseline satu modalitas (Mono3D, 3DOP, VeloFCN) menunjukkan nilai nyata dari memadukan geometri dan tekstur.

Dari sisi rekayasa, kecepatan inferensi 0,36 detik per bingkai (kurang dari 3 *frame* per detik) jauh dari cukup untuk kendali kendaraan waktu-nyata, karena tiga cabang tampilan harus diproses dan digabung berulang. Evaluasi juga difokuskan pada kelas mobil saja; secara konseptual, resolusi sel BEV 0,1 meter yang dirancang untuk dimensi mobil kemungkinan kurang memadai untuk objek kecil seperti pejalan kaki atau pesepeda, karena jejak objek tersebut pada BEV hanya mencakup sedikit sel. Pembatasan orientasi usulan pada 0° atau 90° di tahap awal juga berisiko melewatkan kendaraan yang menghadap arah diagonal sebelum disempurnakan pada tahap akhir. Ketergantungan pada kalibrasi presisi antara LiDAR dan kamera menambah kompleksitas penerapan di kendaraan nyata dibandingkan sistem satu sensor.

## Kaitan dengan Bab Lain

MV3D memakai kerangka usulan wilayah dua tahap yang diwarisi dari Faster R-CNN (bab [014 - 2017 - Faster R-CNN - Fondasi RGB](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)), tetapi mengganti sumber usulan dari citra 2D menjadi BEV LiDAR. Keterbatasan kecepatan dan pembatasan orientasinya menjadi sasaran perbaikan langsung pada AVOD (bab [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)), yang mempertahankan gagasan fusi BEV-RGB berbasis wilayah tetapi merancang fusi lebih ringan di tahap usulan itu sendiri. Pendekatan berbasis proyeksi 2D yang dipakai MV3D juga menjadi pembanding bagi metode yang memproses titik LiDAR langsung dalam bentuk 3D, seperti VoxelNet (bab [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)) dan PointRCNN (bab [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)), yang menghindari kehilangan informasi akibat proyeksi ke bidang 2D.

## Poin untuk Sitasi

Kutip dengan kunci `chen2017mv3d`. Ringkasan yang aman dikutip: "MV3D memfusikan representasi bird's-eye-view dan front-view dari LiDAR dengan citra RGB melalui deep fusion berbasis wilayah, mencapai AP3D 62,68% (IoU 0,7, tingkat sedang) untuk deteksi mobil pada KITTI — jauh melampaui baseline LiDAR tunggal (VeloFCN, 13,66%) dan stereo (3DOP, 5,07%)." Angka AP3D/APloc pada IoU 0,5 dan 0,7 serta hasil ablasi kombinasi tampilan dan strategi fusi diperoleh dari pembacaan naskah (versi HTML ar5iv) dan disilangkan dengan sumber kedua untuk angka 62,68%. Angka AP deteksi 2D pada set uji KITTI (perbandingan dengan Vote3D, Vote3Deep, 3D FCN) belum disilangkan dengan sumber kedua dan sebaiknya diverifikasi ulang ke tabel naskah asli sebelum dikutip dalam karya formal. Dimensi peta BEV (±704×800 sel) adalah hasil perhitungan dari rentang dan ukuran sel yang disebutkan naskah, bukan angka yang eksplisit tertulis sebagai satu bilangan di teks — sebaiknya dicek silang pula.
