# 094 - 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-View Spatial Feature Fusion for 3D Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yoo20203dcvf` |
| Judul asli | 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-View Spatial Feature Fusion for 3D Object Detection |
| Penulis | Jin Hyeok Yoo, Yecheol Kim, Jisong Kim, Jun Won Choi |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020), hlm. 720–736 |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2004.12636
- **Google Scholar:** https://scholar.google.com/scholar?q=3D-CVF%3A%20Generating%20Joint%20Camera%20and%20LiDAR%20Features%20Using%20Cross-View%20Spatial%20Feature%20Fusion%20for%203D%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=3D-CVF%3A%20Generating%20Joint%20Camera%20and%20LiDAR%20Features%20Using%20Cross-View%20Spatial%20Feature%20Fusion%20for%203D%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan 3D-CVF (*Cross-View Feature Fusion*), arsitektur deteksi objek 3D yang menggabungkan citra kamera dan *point cloud* (kumpulan titik koordinat 3D) LiDAR pada level fitur, bukan pada level data mentah. Masalah yang disasar adalah penyelarasan spasial: fitur kamera hidup dalam koordinat citra 2D berperspektif, sedangkan fitur LiDAR hidup dalam koordinat dunia 3D, sehingga menggabungkan keduanya secara langsung menghasilkan pencocokan yang kasar. 3D-CVF mengatasi hal ini dengan memproyeksikan fitur kamera ke ruang *bird's-eye view* (BEV, tampak dari atas) memakai kalibrasi yang dapat dilatih, kemudian menggabungkannya dengan fitur LiDAR memakai mekanisme gerbang (*gated fusion*) yang menimbang kontribusi tiap sumber sensor per lokasi spasial.

Pada saat publikasi, 3D-CVF mencapai kinerja *state-of-the-art* di antara metode fusi kamera-LiDAR pada tolok ukur KITTI, dengan *average precision* (AP, presisi rata-rata) 3D sebesar 80,05% untuk kelas mobil pada tingkat kesulitan sedang di data uji. Kontribusi terbesarnya justru terlihat pada objek jauh: pada rentang 40–70 meter, penggabungan kamera menaikkan AP sebesar 5,29 poin dibandingkan model LiDAR tunggal, jauh lebih besar daripada kenaikan pada objek dekat (0,16 poin). Makalah ini berada dalam garis penelitian fusi sensor untuk kendaraan otonom bersama MV3D (bab 091), AVOD (bab 092), dan PointPainting (bab 093), serta menjadi rujukan bagi metode fusi berbasis *transformer* yang muncul kemudian seperti TransFusion (bab 097) dan BEVFusion (bab 098).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sensor LiDAR menghasilkan *point cloud* yang mengukur jarak secara langsung dan akurat, tetapi kepadatan titiknya menurun tajam seiring jarak — pada 50 meter, satu objek mungkin hanya tertutupi segelintir titik pemindaian. Sensor kamera menghasilkan citra padat dengan tekstur dan warna kaya, tetapi tidak memuat informasi kedalaman secara eksplisit. Kombinasi keduanya secara intuitif saling melengkapi, tetapi metode fusi awal seperti MV3D dan AVOD (dibahas pada bab 091 dan 092) menggabungkan fitur dari beberapa sudut pandang (citra depan, BEV LiDAR) memakai operasi penggabungan sederhana seperti rata-rata atau penjumlahan kanal, tanpa mekanisme eksplisit untuk menyelaraskan posisi spasial fitur dari dua ruang koordinat yang berbeda.

Ketidakselarasan ini muncul karena proyeksi dari titik 3D ke piksel citra bergantung pada kalibrasi kamera-LiDAR yang presisinya terbatas, dan karena satu piksel citra sebenarnya berkorespondensi dengan garis proyeksi (bukan satu titik tunggal) dalam ruang 3D. Pendekatan lain, PointPainting (bab 093, tahun rilis sama), menyelesaikan masalah ini dengan cara berbeda: menempelkan (*painting*) skor segmentasi semantik dari citra ke setiap titik LiDAR sebelum diproses oleh detektor berbasis *point cloud*. 3D-CVF mengambil arah yang berlainan — fusi dilakukan pada level peta fitur BEV, bukan pada level titik individual, sehingga kedua modal (kamera dan LiDAR) tetap diproses oleh jaringan masing-masing sebelum digabungkan. Masalah intinya tetap sama: bagaimana memproyeksikan fitur kamera ke BEV sedemikian rupa sehingga posisinya benar-benar berkorespondensi dengan fitur LiDAR pada lokasi yang sama.

## Ide Utama

Gagasan inti 3D-CVF adalah memindahkan fitur kamera ke ruang representasi yang sama dengan fitur LiDAR (BEV) melalui proyeksi yang dikalibrasi secara otomatis (*auto-calibrated projection*), lalu menggabungkan kedua peta fitur BEV tersebut dengan bobot yang berbeda-beda di setiap lokasi, bukan bobot tunggal untuk seluruh citra. Bobot ini dihasilkan oleh jaringan gerbang kecil yang mempelajari, untuk setiap sel BEV, seberapa besar informasi kamera dan seberapa besar informasi LiDAR yang perlu dipakai pada lokasi itu.

Intuisinya: pada sel BEV yang berhimpitan dengan objek jauh atau tipis (di mana titik LiDAR jarang), fitur kamera yang padat memberi informasi tambahan bernilai tinggi; pada sel yang sudah tertutup rapat oleh titik LiDAR (objek dekat), kontribusi tambahan dari kamera relatif kecil. Karena penimbangan ini dipelajari per lokasi lewat data, jaringan tidak memerlukan aturan manual tentang kapan mempercayai sensor mana — pola ini muncul dari pelatihan.

## Cara Kerja Langkah demi Langkah

Arsitektur 3D-CVF tersusun atas lima komponen: dua alur pemrosesan modal terpisah (LiDAR dan kamera), satu tahap penyelarasan lintas-pandang, satu tahap penggabungan bergerbang, dan satu tahap perbaikan dua-langkah berbasis *region of interest* (RoI, wilayah kandidat objek).

```
citra RGB (kamera)          point cloud (LiDAR)
      │                            │
  ResNet-18 + FPN            voksel + 6 lapis
  (fitur 2D, 256 kanal)      konvolusi 3D jarang
      │                     (fitur BEV, 128 kanal)
      │                            │
      └──── proyeksi BEV ──────────┤   auto-calibrated
       (offset kalibrasi Δx, Δy,   │   projection
        interpolasi bilinear)      │
      │                            │
      ▼                            ▼
   F_kamera (BEV)   <——————>   F_lidar (BEV)
      │        gated feature fusion       │
      │   gerbang σ(konv([F_k ⊕ F_l]))    │
      ▼                                    ▼
  F_kamera bergerbang  +  F_lidar bergerbang
              │
              ▼
     fitur gabungan BEV → RPN 3D → proposal kotak
              │
              ▼
   3D RoI fusion-refinement (tahap kedua)
              │
              ▼
        kotak 3D akhir + kelas
```

### Dua Alur Pemrosesan Awal

Citra kamera diproses oleh ResNet-18 (jaringan konvolusi 18 lapis) yang dilengkapi *Feature Pyramid Network* (FPN, jaringan yang menggabungkan peta fitur dari beberapa skala resolusi agar objek besar dan kecil sama-sama terdeteksi baik; dibahas terpisah pada bab 018), menghasilkan peta fitur 2D dengan 256 kanal. *Point cloud* LiDAR diolah dengan pengodean voksel (pembagian ruang 3D menjadi sel kubus kecil, tiap sel merangkum titik-titik di dalamnya menjadi satu vektor fitur) diikuti enam lapis konvolusi 3D jarang (*sparse convolution*, konvolusi yang hanya menghitung pada sel yang terisi, menghemat komputasi karena sebagian besar ruang 3D kosong), menghasilkan peta fitur BEV dengan 128 kanal.

### Auto-Calibrated Projection

Setiap sel pada peta BEV dipetakan balik ke koordinat citra memakai parameter kalibrasi kamera-LiDAR, lalu fitur pada empat piksel citra terdekat diambil dan digabung memakai interpolasi bilinear berbobot jarak. Untuk mengoreksi kesalahan kalibrasi yang selalu ada pada sensor nyata, jaringan mempelajari sepasang nilai koreksi (Δx, Δy) yang menggeser titik proyeksi sebelum interpolasi dilakukan — inilah makna "otomatis terkalibrasi": koreksi kecil ini dipelajari dari data, bukan diukur ulang secara manual. Hasilnya adalah peta fitur kamera versi BEV yang selaras posisi dengan peta fitur LiDAR BEV.

### Gated Feature Fusion

Kedua peta fitur BEV (kamera dan LiDAR) digabungkan sepanjang dimensi kanal, lalu dua konvolusi terpisah menghasilkan peta gerbang untuk masing-masing modal, dilewatkan fungsi sigmoid (fungsi yang memetakan nilai apa pun ke rentang 0–1, dipakai sebagai bobot). Fitur kamera dikalikan elemen-demi-elemen dengan gerbangnya, demikian pula fitur LiDAR, sehingga tiap lokasi BEV memperoleh bobot kontribusi kamera dan LiDAR yang berbeda. Fitur gerbang dari kedua modal kemudian digabung menjadi satu peta fitur bersama yang diteruskan ke jaringan pengusul wilayah (*region proposal network*, RPN) untuk menghasilkan kandidat kotak 3D awal.

### Perbaikan Dua Tahap dengan 3D RoI Fusion

Setelah RPN menghasilkan kandidat kotak, tahap kedua memperbaiki posisi dan ukuran tiap kotak. Untuk tiap kandidat, fitur pada beberapa lapis resolusi BEV diambil lewat *3D RoI pooling* (pengumpulan fitur dari wilayah kandidat), sementara fitur kamera pada wilayah yang sama diambil dan diolah dengan struktur mirip PointNet (jaringan yang mengolah kumpulan titik/fitur tak terurut menjadi satu vektor ringkas). Kedua fitur ini digabung ulang untuk menghasilkan koreksi akhir terhadap posisi, ukuran, dan orientasi kotak 3D. Perbaikan dua tahap ini menyumbang kenaikan tambahan pada AP dibandingkan hanya memakai fitur gabungan tahap pertama, seperti ditunjukkan pada uji ablasi di bagian berikut.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur deteksi 3D untuk kendaraan otonom. KITTI menyediakan 7.481 citra latih dan 7.518 citra uji, dengan metrik AP 3D dihitung pada 40 titik *recall* (proporsi objek yang berhasil ditemukan), dipecah menjadi tiga tingkat kesulitan (mudah, sedang, sulit) berdasarkan ukuran objek, tingkat oklusi, dan pemotongan pada tepi citra. Evaluasi utama dilakukan pada kelas mobil karena kelas lain (pejalan kaki, pesepeda) memiliki jumlah data latih yang lebih sedikit pada KITTI. nuScenes menyediakan 28.130 sampel latih dan 6.019 sampel validasi dari enam kamera dan satu LiDAR 32 kanal, dengan metrik *nuScenes Detection Score* (NDS, skor gabungan yang memperhitungkan akurasi posisi, ukuran, orientasi, dan kelas) serta *mean Average Precision* (mAP) di sepuluh kategori objek.

Pada data uji KITTI, 3D-CVF mencapai AP 3D sebesar 89,20% (mudah), 80,05% (sedang), dan 73,11% (sulit) untuk kelas mobil, mengungguli MMF (88,40% / 77,43% / 70,22%) dan bersaing dengan STD, metode berbasis LiDAR tunggal (87,95% / 79,71% / 75,09%). Interpretasinya: pada tingkat kesulitan sedang dan sulit, 3D-CVF unggul tipis atas metode fusi lain, tetapi metode LiDAR tunggal terbaik (STD) masih sedikit lebih baik pada kasus sulit — menunjukkan bahwa keuntungan fusi kamera tidak selalu konsisten di semua kondisi. Pada nuScenes, 3D-CVF mencapai 42,17% mAP dan 49,78% NDS, naik dari model dasar LiDAR tunggal sebesar 39,43% mAP dan 46,21% NDS (kenaikan 2,74 poin mAP dan 3,57 poin NDS).

Analisis berdasarkan jarak objek pada KITTI menunjukkan pola penting: pada rentang 0–20 meter, penambahan kamera hanya menaikkan AP dari 89,86% menjadi 90,02% (0,16 poin), sedangkan pada rentang 40–70 meter, AP naik dari 30,57% menjadi 35,86% (5,29 poin). Interpretasinya konsisten dengan alasan teknis fusi sensor: pada jarak dekat, titik LiDAR sudah cukup padat sehingga informasi tambahan dari kamera memberi sedikit nilai; pada jarak jauh, titik LiDAR menjadi jarang sehingga tekstur kamera yang tetap padat menjadi penentu utama keberhasilan deteksi.

Uji ablasi pada data validasi KITTI mengukur kontribusi tiap komponen secara bertahap dari model dasar (LiDAR saja, AP sedang 78,31%): penambahan *gated fusion* menaikkan AP sedang menjadi 79,19%; penambahan pemetaan lintas-pandang (proyeksi terkalibrasi) menaikkan menjadi 79,25%; dan penambahan perbaikan RoI 3D tahap kedua menaikkan menjadi 79,88%. Interpretasinya: *gated fusion* menyumbang kenaikan terbesar (0,88 poin) di antara ketiga komponen tambahan, menunjukkan bahwa penimbangan adaptif per lokasi adalah kontributor utama, sedangkan penyempurnaan kalibrasi proyeksi dan perbaikan RoI memberi kenaikan lebih kecil namun tetap konsisten arahnya.

## Kelebihan dan Keterbatasan

Kelebihan utama 3D-CVF adalah penyelesaian eksplisit terhadap masalah penyelarasan spasial lintas-modal, dengan mekanisme kalibrasi yang dapat disetel-halus dari data alih-alih mengandalkan kalibrasi sensor statis semata. Penimbangan bergerbang per lokasi memberi kerangka yang masuk akal secara fisik: kontribusi kamera memang seharusnya lebih besar pada jarak jauh, dan hasil eksperimen mengonfirmasi hal itu secara kuantitatif. Kinerjanya juga kompetitif pada dua tolok ukur berbeda (KITTI dan nuScenes) dengan karakteristik sensor yang berlainan.

Dari sisi rekayasa, arsitektur ini menambah beban komputasi yang tidak kecil: proses fusi menambah sekitar 25 milidetik per bingkai di atas 50 milidetik model dasar, sehingga total waktu inferensi mendekati 75 milidetik per bingkai — jauh dari kecepatan model deteksi 3D LiDAR tunggal yang lebih ringan. Secara konseptual, ketergantungan pada kalibrasi kamera-LiDAR tetap ada meski dengan koreksi otomatis; bila kalibrasi awal keliru terlalu jauh, mekanisme koreksi Δx, Δy mungkin tidak cukup untuk memulihkan keselarasan. Evaluasi utama pada KITTI juga terbatas pada kelas mobil, sehingga generalisasi ke kelas objek yang lebih kecil dan jarang (pejalan kaki, pesepeda) belum terbukti langsung dari eksperimen yang dilaporkan.

## Kaitan dengan Bab Lain

3D-CVF melanjutkan garis fusi kamera-LiDAR yang dimulai oleh MV3D (bab 091) dan AVOD (bab 092), tetapi mengganti operasi penggabungan sederhana pada kedua pendahulu tersebut dengan proyeksi terkalibrasi dan gerbang adaptif per lokasi. Berbeda dengan PointPainting (bab 093), yang menyatukan modal pada level titik LiDAR individual sebelum masuk ke detektor, 3D-CVF menyatukan modal pada level peta fitur BEV — dua strategi fusi yang saling melengkapi dalam literatur meski dipublikasikan pada tahun yang sama. Prinsip penimbangan adaptif per lokasi yang diperkenalkan di sini muncul kembali dalam bentuk lebih umum pada metode fusi berbasis *transformer* seperti [097 - 2022 - TransFusion - Deteksi 3D](./097%20-%202022%20-%20TransFusion%20-%20Deteksi%203D.md), yang menggantikan gerbang konvolusi dengan mekanisme atensi lintas-modal, dan pada [098 - 2023 - BEVFusion - Deteksi 3D](./098%20-%202023%20-%20BEVFusion%20-%20Deteksi%203D.md), yang menyatukan kamera dan LiDAR pada representasi BEV bersama secara lebih umum untuk berbagai tugas persepsi sekaligus.

## Poin untuk Sitasi

Kutip dengan kunci `yoo20203dcvf`. Ringkasan yang aman dikutip: "3D-CVF menyelaraskan fitur kamera dan LiDAR secara spasial melalui proyeksi terkalibrasi otomatis ke BEV, digabungkan dengan mekanisme gerbang adaptif per lokasi, mencapai AP 3D 80,05% pada kelas mobil tingkat sedang di data uji KITTI dan NDS 49,78% pada nuScenes." Angka AP KITTI (89,20/80,05/73,11), hasil nuScenes (42,17% mAP, 49,78% NDS), rincian uji ablasi per komponen, dan analisis kenaikan berbasis jarak (0,16 hingga 5,29 poin) diambil dari pembacaan naskah arXiv versi ar5iv; disarankan verifikasi ulang terhadap tabel resmi versi ECCV/Springer sebelum dikutip dalam karya formal, mengingat kemungkinan perbedaan kecil antara versi pracetak dan versi terbit.
