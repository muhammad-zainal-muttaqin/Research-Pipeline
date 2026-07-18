# 098 - BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2023bevfusion` |
| Judul asli | BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation |
| Penulis | Zhijian Liu, Haotian Tang, Alexander Amini, Xinyu Yang, Huizi Mao, Daniela Rus, Song Han |
| Tahun | 2023 (versi awal diunggah 2022) |
| Venue | IEEE International Conference on Robotics and Automation (ICRA 2023) |
| Tema | Deteksi 3D |

Catatan identitas: nama "BEVFusion" dipakai dua makalah berbeda yang terbit hampir bersamaan pada 2022. Bab ini membahas makalah kelompok MIT (Liu, Tang, Amini, dkk., kunci `liu2023bevfusion`). Makalah lain berjudul serupa (Liang dkk., NeurIPS 2022) memakai pendekatan berbeda — menambahkan fitur kamera ke ruang *voxel LiDAR* — dan tidak dibahas di sini.

## Tautan Akses
- **arXiv (naskah lengkap gratis):** https://arxiv.org/abs/2205.13542
- **Versi HTML (ar5iv):** https://ar5iv.labs.arxiv.org/html/2205.13542
- **Kode sumber resmi (PyTorch, MIT HAN Lab):** https://github.com/mit-han-lab/bevfusion
- **Google Scholar:** https://scholar.google.com/scholar?q=BEVFusion%3A%20Multi-Task%20Multi-Sensor%20Fusion%20with%20Unified%20Bird%27s-Eye%20View%20Representation

## Gambaran Umum

BEVFusion adalah kerangka fusi sensor yang menggabungkan citra kamera dan data *LiDAR* (sensor laser penghasil awan titik atau *point cloud* tiga dimensi) dengan cara memetakan kedua modalitas ke satu ruang representasi bersama, yaitu *bird's-eye view* (*BEV*, tampak atas), sebelum digabungkan. Masalah yang disasar adalah kehilangan informasi pada metode fusi generasi sebelumnya yang bekerja pada level titik: metode itu memproyeksikan fitur kamera ke titik *LiDAR* memakai kalibrasi geometris, sehingga sebagian besar piksel citra terbuang karena tidak memiliki pasangan titik *LiDAR* yang presisi.

Kontribusi teknis utamanya adalah teknik *BEV pooling* (penggabungan fitur ke sel *BEV*) yang dioptimalkan sehingga transformasi citra ke *BEV* — sebelumnya bagian paling lambat pada arsitektur ini — dipercepat sekitar 40 kali lipat. Pada tolok ukur *nuScenes* (kumpulan data deteksi objek berkendara dengan enam kamera dan *LiDAR*), BEVFusion mencapai 70,2% mAP dan 72,9% NDS untuk deteksi objek 3D pada set uji, serta 62,7% mIoU untuk segmentasi peta *BEV* pada set validasi, dengan komputasi lebih rendah dan lebih cepat daripada metode fusi pembanding. Kerangka ini juga bersifat multi-*task* (banyak tugas): arsitektur dasar yang sama dipakai untuk deteksi 3D maupun segmentasi peta *BEV* tanpa perubahan struktural berarti.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek 3D untuk kendaraan otonom umumnya membutuhkan gabungan *LiDAR* dan kamera: *LiDAR* memberi jarak dan ukuran yang akurat, sedangkan kamera memberi kepadatan semantik (warna, tekstur, tulisan pada rambu) yang tidak dimiliki awan titik. Sebelum BEVFusion, metode fusi seperti *PointPainting* (bab 093) mengecat setiap titik *LiDAR* dengan label semantik hasil segmentasi citra, sementara *PointAugmenting* dan *MVP* menambahkan fitur atau titik virtual pada awan titik berdasarkan proyeksi kamera. Seluruh pendekatan ini disebut fusi level-titik (*point-level fusion*): fitur kamera hanya dipindahkan ke lokasi yang memiliki pasangan titik *LiDAR*, dan menurut penulis kurang dari 5% piksel kamera berhasil dipasangkan, sedangkan sisanya dibuang begitu saja.

Akibatnya, fusi level-titik bekerja cukup baik untuk deteksi objek (kotak 3D tetap ditentukan geometri *LiDAR*), tetapi buruk untuk tugas yang bergantung pada kepadatan semantik, seperti segmentasi peta *BEV* (menandai kelas permukaan jalan pada tiap sel tampak atas: jalur kendaraan, trotoar, area penyeberangan). TransFusion (bab 097), terbit pada tahun yang sama, mengatasi kerapuhan proyeksi tetap dengan asosiasi lunak berbasis *attention* per kandidat objek, tetapi tetap memproyeksikan pusat kotak ke citra per kueri, bukan menyatukan seluruh adegan ke satu ruang bersama.

## Ide Utama

Gagasan inti BEVFusion adalah membalik urutan proses: alih-alih memproyeksikan satu modalitas ke modalitas lain, kedua aliran data — kamera dan *LiDAR* — masing-masing diubah secara independen menjadi peta fitur *BEV* berukuran dan orientasi spasial sama, baru kemudian digabungkan. Karena keduanya sudah berada di ruang koordinat identik sebelum fusi, tidak ada piksel kamera yang dibuang hanya karena tidak memiliki pasangan titik *LiDAR*.

Konsekuensinya, kerangka menjadi *task-agnostic* (tidak terikat satu tugas): kepala jaringan (*head*) apa pun yang bekerja di atas satu peta fitur *BEV* gabungan — untuk deteksi objek maupun segmentasi peta — dapat dipasang tanpa mengubah kedua aliran *encoder*. Tantangan teknis utama agar gagasan ini praktis adalah kecepatan konversi fitur kamera ke *BEV*, yang pada implementasi naif sangat lambat karena harus memetakan setiap piksel dari enam kamera ke posisi 3D yang mungkin sebelum diagregasi ke sel *BEV* yang benar.

## Cara Kerja Langkah demi Langkah

### Aliran Kamera: dari Citra ke BEV

Enam citra kamera (konfigurasi standar *nuScenes*: depan, samping, belakang) diproses dengan *backbone* Swin-T (varian ringan *Swin Transformer*, bab 025) dan *Feature Pyramid Network* (FPN, bab 018) untuk menghasilkan peta fitur multi-skala per kamera. Peta fitur ini diangkat ke ruang 3D dengan operasi *lift-splat*: untuk setiap piksel, jaringan memprediksi distribusi kedalaman diskret (peluang piksel berasal dari sejumlah jarak berbeda di depan kamera), lalu fitur piksel disebar (*splat*) ke titik-titik 3D sesuai distribusi itu. Titik-titik 3D hasil sebaran ini diratakan ke bidang *BEV* dengan menjumlahkan fitur yang jatuh pada sel *grid* yang sama.

### BEV Pooling yang Dioptimalkan

Langkah meratakan jutaan titik 3D ke sel *BEV* — disebut *BEV pooling* — pada implementasi awal menjadi titik lambat: dengan sekitar dua juta titik fitur per adegan, langkah ini memakan lebih dari 500 milidetik, sekitar 80% dari total waktu inferensi. BEVFusion mempercepatnya lewat dua perbaikan. Pertama, *precomputation* (prakomputasi): karena koordinat kamera terhadap kendaraan tetap dari waktu ke waktu, koordinat 3D dan indeks sel *BEV* setiap titik fitur dihitung sekali di muka, bukan dihitung ulang setiap inferensi — menekan latensi asosiasi *grid* dari 17 milidetik menjadi 4 milidetik. Kedua, *interval reduction* (reduksi interval) memakai kernel GPU khusus yang menjumlahkan fitur langsung per sel BEV, menggantikan operasi jumlah-prefiks (*prefix sum*) generik yang boros, sehingga latensi agregasi fitur turun dari 500 milidetik menjadi 2 milidetik. Gabungan kedua teknik memangkas waktu transformasi kamera-ke-*BEV* dari sekitar 500 milidetik menjadi 12 milidetik — percepatan sekitar 40 kali lipat — sehingga tahap ini turun dari mendominasi waktu proses menjadi sekitar 10% dari total waktu inferensi.

### Aliran LiDAR dan Penggabungan di Ruang BEV

Awan titik *LiDAR* diproses dengan *encoder* bergaya *VoxelNet* (bab 087): titik dikelompokkan ke *voxel* (sel volume 3D), diproses dengan konvolusi 3D jarang, lalu diratakan menjadi peta fitur *BEV* dengan grid spasial yang sama seperti aliran kamera. Kedua peta fitur *BEV* digabungkan dengan penggabungan kanal (*concatenation*), lalu diproses lebih lanjut oleh sejumlah blok residual konvolusional (*BEV encoder*) yang mengoreksi ketidaksejajaran spasial kecil antar-modalitas, misalnya akibat kesalahan kalibrasi ringan atau ketidaktepatan estimasi kedalaman pada aliran kamera. Peta fitur *BEV* gabungan ini menjadi masukan bagi kepala tugas: kepala deteksi memprediksi peta panas pusat objek beserta regresi ukuran dan orientasi kotak 3D, sedangkan kepala segmentasi memprediksi peta biner per kelas permukaan untuk setiap sel *BEV*.

Alur data dari kedua sensor hingga representasi bersama dirangkum berikut.

```
6 citra kamera                    LiDAR point cloud
      |                                  |
Swin-T + FPN                     voxelisasi + sparse conv 3D
      |                                  |
peta fitur per-kamera              fitur BEV LiDAR (HxWxC)
      |
prediksi kedalaman diskret
      |
lift-splat: sebar fitur ke titik 3D
      |
BEV POOLING (precompute + interval reduction, ~500ms->12ms)
      |
fitur BEV kamera (HxWxC)
      |                                  |
      +---------- concat kanal ----------+
                     |
        BEV encoder (blok residual konvolusi)
                     |
        fitur BEV gabungan (satu representasi)
              /                    \
    kepala deteksi 3D        kepala segmentasi peta
   (heatmap + regresi)         (biner per kelas)
```

### Pelatihan

Dua aliran *encoder* dilatih bersama sebagai satu jaringan, dengan augmentasi data terpisah pada citra (mis. pemotongan, pembalikan) dan pada awan titik (mis. rotasi, penskalaan global), karena keduanya berada pada ruang koordinat berbeda sebelum digabung ke *BEV*. Studi ablasi (pengujian pengaruh komponen tertentu dengan menghapus atau mengubahnya) menunjukkan bahwa melatih *backbone* citra secara menyeluruh, bukan membekukan bobot pralatihnya, memberi kenaikan sekitar 10 poin baik pada deteksi maupun segmentasi, dan kedua jenis augmentasi perlu diaktifkan bersamaan untuk hasil terbaik.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada *nuScenes*, dengan metrik mAP dan NDS (*nuScenes Detection Score*, metrik gabungan akurasi klasifikasi dan kesalahan atribut) untuk deteksi objek 3D, serta mIoU (*mean Intersection over Union*, rata-rata rasio irisan-gabungan antar-kelas) untuk segmentasi peta *BEV*. Tabel berikut merangkum perbandingan pada set uji deteksi *nuScenes*.

| Model | Modalitas | mAP | NDS | Latensi (ms) |
|---|---|---|---|---|
| CenterPoint | LiDAR saja | 60,3% | 67,3% | 80,7 |
| BEVFormer | Kamera saja | 44,5% | 53,5% | – |
| MVP | LiDAR+Kamera | 66,4% | 70,5% | 187,1 |
| PointAugmenting | LiDAR+Kamera | 66,8% | 71,0% | 234,4 |
| TransFusion | LiDAR+Kamera | 68,9% | 71,7% | 156,6 |
| BEVFusion | LiDAR+Kamera | 70,2% | 72,9% | 119,2 |

Interpretasinya: BEVFusion unggul 1,3 poin mAP dan 1,2 poin NDS atas TransFusion, sekaligus 1,3 kali lebih cepat (119,2 ms berbanding 156,6 ms) dan memakai komputasi lebih rendah (253,2 GMAC berbanding 485,8 GMAC, menurut angka yang dilaporkan makalah). Dibandingkan LiDAR-saja (CenterPoint, 60,3% mAP), tambahan kamera menyumbang hampir 10 poin; dibandingkan kamera-saja (BEVFormer, 44,5% mAP), kesenjangannya jauh lebih besar, menegaskan geometri LiDAR tetap menjadi sumber informasi dominan untuk deteksi 3D, sedangkan kamera menyumbang perbaikan penting tetapi bukan pengganti.

Perbedaan paling mencolok muncul pada segmentasi peta BEV, tugas yang menuntut kepadatan semantik: BEVFusion mencapai 62,7% mIoU pada set validasi, jauh di atas fusi level-titik seperti PointPainting (49,1%) dan MVP (49,0%), metode kamera-saja LSS (44,4%) dan CVT (40,2%), serta LiDAR-saja CenterPoint (48,6%). Selisih sekitar 13 poin mIoU atas fusi terdahulu konsisten dengan argumen makalah: karena fusi level-titik membuang lebih dari 95% fitur kamera akibat kelangkaan pasangan titik LiDAR, tugas yang bergantung pada tekstur permukaan (jalur, trotoar, marka) dirugikan jauh lebih besar daripada deteksi objek yang tetap bisa mengandalkan geometri LiDAR.

Studi ablasi kombinasi modalitas pada set validasi menunjukkan LiDAR-saja mencapai 57,6% mAP, kamera-saja 33,3%, dan gabungan keduanya 66,4% — menegaskan kontribusi tiap modalitas sekaligus efek saling melengkapi. Pada kondisi merugikan, keunggulan atas CenterPoint LiDAR-saja meningkat menjadi sekitar 10,7 poin mAP saat hujan, dan keunggulan segmentasi atas baseline kamera-saja meningkat sekitar 12,8 poin mIoU pada malam hari — kamera dan LiDAR saling menutupi kelemahan kondisi masing-masing. Sebaliknya, pelatihan gabungan kedua tugas sekaligus menunjukkan gejala *negative transfer* (satu tugas menurunkan performa tugas lain), yang menurut makalah dapat dikurangi sebagian dengan memisahkan sebagian parameter encoder antar-tugas.

## Kelebihan dan Keterbatasan

Kelebihan utama BEVFusion adalah efisiensi: optimisasi *BEV pooling* mengubah transformasi kamera-ke-*BEV* dari komponen paling lambat menjadi bagian kecil dari total waktu inferensi, sehingga kerangka fusi lengkap justru lebih cepat dan lebih murah secara komputasi daripada TransFusion yang berbasis *attention*. Sifat *task-agnostic* memungkinkan satu representasi *BEV* dipakai ulang untuk deteksi maupun segmentasi tanpa membangun ulang aliran *encoder*, dan keunggulannya pada segmentasi peta (62,7% berbanding di bawah 50% untuk seluruh pembanding) menunjukkan bahwa menyatukan modalitas sebelum fusi mempertahankan kepadatan semantik kamera yang hilang pada metode level-titik.

Keterbatasan yang diakui penulis: pelatihan gabungan multi-tugas menimbulkan *negative transfer*, sehingga memerlukan sebagian parameter terpisah per tugas. Dari sisi rekayasa, aliran kamera tetap bergantung pada estimasi kedalaman diskret yang tidak langsung (jaringan menebak distribusi peluang kedalaman, bukan mengukur kedalaman sebenarnya), sehingga akurasi posisi fitur kamera pada BEV berbanding lurus dengan kualitas estimasi ini. Secara konseptual, keunggulan besar pada segmentasi peta bergantung pada anotasi peta jalan resolusi tinggi seperti pada *nuScenes*; kerangka ini belum tentu memberi keunggulan sebesar itu pada dataset tanpa anotasi semacamnya. Perbandingan MACs dan latensi juga dilaporkan makalah sendiri, sehingga faktor lingkungan pengujian sebaiknya dicek ulang sebelum dipakai sebagai klaim kecepatan mutlak.

## Kaitan dengan Bab Lain

BEVFusion menjawab kelemahan fusi level-titik yang menjadi ciri *PointPainting* (bab 093) dan turunannya, yang membuang lebih dari 95% fitur kamera karena mensyaratkan pasangan titik *LiDAR* eksplisit. Dibandingkan *3D-CVF* (bab 094), yang juga memproyeksikan fitur citra ke ruang *voxel* tetapi tetap memakai asosiasi geometris tetap per titik, BEVFusion meratakan kedua modalitas ke grid *BEV* yang sama sebelum fusi, sehingga tidak ada piksel yang dibuang di muka. Hubungan paling langsung ada dengan TransFusion (bab 097), yang terbit pada tahun berdekatan dan sama-sama menyasar kerapuhan asosiasi tetap, tetapi lewat jalur berbeda: TransFusion memakai *attention* per kandidat objek untuk menarik fitur citra secara selektif, sedangkan BEVFusion menyatukan seluruh adegan ke satu representasi bersama sebelum kotak objek diprediksi — lihat [097 - 2022 - TransFusion - Deteksi 3D](./097%20-%202022%20-%20TransFusion%20-%20Deteksi%203D.md) untuk perbandingan kedua pendekatan. Tulang punggung *voxel*-*BEV* pada aliran *LiDAR* BEVFusion melanjutkan garis metode berbasis *voxel* seperti *VoxelNet*, dibahas pada [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md), sementara sifat multi-*task*-nya menjadikan bab ini rujukan penting bagi survei deteksi 3D [099 - 2019 - Survei Deteksi 3D (Arnold dkk.) - Deteksi 3D](./099%20-%202019%20-%20Survei%20Deteksi%203D%20%28Arnold%20dkk.%29%20-%20Deteksi%203D.md) dalam memetakan arah fusi berbasis representasi bersama.

## Poin untuk Sitasi

Kutip dengan kunci `liu2023bevfusion`. Ringkasan aman dikutip: "BEVFusion menyatukan fitur kamera dan LiDAR pada satu ruang BEV bersama sebelum digabung, dengan optimized BEV pooling yang mempercepat transformasi kamera-ke-BEV sekitar 40 kali lipat, mencapai 70,2% mAP dan 72,9% NDS untuk deteksi 3D serta 62,7% mIoU untuk segmentasi peta BEV pada nuScenes." Angka mAP/NDS/latensi/MACs tabel utama, mIoU segmentasi, dan detail BEV pooling (17ms→4ms; 500ms→2ms; total 500ms→12ms) diperoleh dari versi HTML naskah (ar5iv) dan dikonfirmasi silang dengan repositori kode resmi. Angka ablasi kombinasi modalitas (57,6%/33,3%/66,4% mAP) dan angka kondisi merugikan (hujan +10,7 mAP; malam hari +12,8 mIoU) berasal dari ringkasan tunggal dan belum dikonfirmasi silang dua sumber independen, sehingga perlu diverifikasi ulang ke tabel asli sebelum dikutip formal. Perbedaan penamaan dengan makalah "BEVFusion" lain (Liang dkk., NeurIPS 2022) juga perlu ditegaskan ulang saat menyusun daftar pustaka agar sitasi tidak tertukar.
