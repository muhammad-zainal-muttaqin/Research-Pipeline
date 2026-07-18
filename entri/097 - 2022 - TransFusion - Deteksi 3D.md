# 097 - TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bai2022transfusion` |
| Judul asli | TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers |
| Penulis | Xuyang Bai, Zeyu Hu, Xinge Zhu, Qingqiu Huang, Yilun Chen, Hongbo Fu, Chiew-Lan Tai |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (naskah lengkap gratis):** https://arxiv.org/abs/2203.11496
- **Kode sumber resmi (PyTorch):** https://github.com/XuyangBai/TransFusion
- **Google Scholar:** https://scholar.google.com/scholar?q=TransFusion%3A%20Robust%20LiDAR-Camera%20Fusion%20for%203D%20Object%20Detection%20with%20Transformers

## Gambaran Umum

TransFusion adalah detektor objek 3D yang menggabungkan data *LiDAR* (sensor laser penghasil awan titik/*point cloud* tiga dimensi) dengan citra kamera memakai mekanisme *attention* dari arsitektur *Transformer*, bukan proyeksi geometris langsung. Masalah yang disasar adalah kerapuhan metode fusi terdahulu: metode-metode itu memetakan setiap titik *LiDAR* ke satu piksel citra tertentu lewat matriks kalibrasi kamera-*LiDAR*, sehingga kesalahan kalibrasi atau kualitas citra yang buruk (gelap, silau, kabur) langsung merusak fitur gabungan yang dihasilkan.

Gagasan TransFusion adalah mengganti pemetaan tetap tersebut dengan asosiasi lunak: setiap kandidat objek "bertanya" ke citra melalui *attention*, dan jaringan mempelajari sendiri wilayah citra mana yang layak dipercaya. Model ini terdiri atas dekoder *Transformer* dua lapis: lapis pertama memprediksi kotak 3D awal dari fitur *LiDAR* saja, lapis kedua menyempurnakan prediksi itu dengan menarik informasi dari citra secara selektif. Pada uji coba *nuScenes* (kumpulan data deteksi objek berkendara berskala besar), TransFusion mencapai 68,9% mAP dan 71,7% NDS pada set uji, unggul tipis atas metode fusi sebelumnya sekaligus jauh lebih tahan terhadap citra malam hari, citra kamera yang hilang, dan kesalahan kalibrasi sensor.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek 3D untuk kendaraan otonom umumnya mengandalkan *LiDAR* karena sensor ini memberi ukuran dan jarak yang akurat secara langsung. Namun awan titik *LiDAR* menjadi jarang pada jarak jauh dan tidak membawa informasi tekstur atau warna, sehingga objek tipis, kecil, atau jauh sering terlewat. Kamera melengkapi kekurangan ini dengan resolusi tinggi dan informasi semantik yang kaya, tetapi tidak memberi kedalaman secara langsung. Menggabungkan keduanya masuk akal, tetapi metode-metode fusi yang ada pada masanya — misalnya *PointPainting* (bab 093) yang "mengecat" tiap titik *LiDAR* dengan label semantik dari citra, atau *3D-CVF* (bab 094) yang memproyeksikan fitur citra ke ruang *voxel* (sel volume 3D) — semuanya bergantung pada **asosiasi keras**: satu titik atau satu *voxel* dipetakan ke satu lokasi piksel tertentu memakai matriks kalibrasi yang tetap.

Asosiasi keras ini rapuh terhadap dua kondisi. Pertama, kesalahan kalibrasi atau pergeseran mekanis antar-sensor (getaran kendaraan, perubahan suhu) membuat titik dipetakan ke piksel yang salah, dan fitur yang terambil menjadi tidak relevan atau menyesatkan. Kedua, ketika citra berkualitas buruk — malam hari, silau matahari, kabur akibat gerakan — fitur pada piksel yang dipetakan tetap dipakai apa adanya, tanpa mekanisme untuk mengabaikannya. Metode fusi terdahulu jarang diuji secara eksplisit pada kondisi semacam ini, padahal keandalan sensor merupakan syarat keselamatan pada kendaraan otonom. Masalah kedua yang lebih halus adalah pemborosan: citra beresolusi tinggi hanya dimanfaatkan pada titik-titik yang kebetulan memiliki pasangan *LiDAR*, sehingga sebagian besar informasi citra tidak pernah tersentuh oleh proses fusi.

## Ide Utama

Gagasan inti TransFusion adalah mengganti pemetaan titik-ke-piksel yang tetap dengan **asosiasi lunak** berbasis *attention*: setiap kandidat deteksi direpresentasikan sebagai *object query* (vektor terpelajar yang mewakili satu slot kandidat objek, konsep yang diperkenalkan DETR, bab 022), dan *query* itu mengambil informasi dari citra melalui mekanisme *cross-attention* — bukan dengan mengambil satu piksel tetap, melainkan dengan menghitung bobot relevansi ke sekelompok piksel di sekitar lokasi yang diperkirakan, lalu menjumlahkan fitur tersebut sesuai bobotnya.

Karena bobot ini dipelajari dari data, jaringan dapat menurunkan kepercayaan pada wilayah citra yang tampak tidak informatif (gelap, kabur, salah posisi akibat kalibrasi meleset) dan menaikkan kepercayaan pada wilayah yang jelas. Prosesnya dipecah menjadi dua tahap berurutan: tahap pertama menghasilkan kotak 3D awal hanya dari *LiDAR*, tahap kedua menyempurnakannya dengan citra. Pemisahan ini penting karena kotak awal dari *LiDAR* sudah cukup akurat untuk menentukan ke wilayah citra mana *attention* semestinya diarahkan.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur dari LiDAR dan Kamera

Awan titik *LiDAR* diolah dengan tulang punggung (*backbone*) bergaya *VoxelNet*: titik-titik dikelompokkan ke dalam *voxel* (sel volume 3D), diproses dengan konvolusi 3D jarang (*sparse convolution*), lalu dipadatkan menjadi peta fitur *BEV* (*Bird's-Eye View*, tampak atas) berukuran tinggi × lebar × kanal. Representasi *BEV* ini menjadi dasar bagi seluruh prediksi selanjutnya karena posisi dan orientasi objek di jalan pada dasarnya adalah masalah dua dimensi (x, y) ditambah ketinggian. Citra dari enam kamera (konfigurasi standar *nuScenes*, meliputi pandangan depan, samping, dan belakang) diproses tulang punggung 2D terpisah, menghasilkan peta fitur citra per kamera yang tetap beresolusi tinggi.

### Inisialisasi Query dari Peta Panas LiDAR

Alih-alih memakai *query* acak atau parameter tetap seperti pada DETR, TransFusion menghitung peta panas (*heatmap*) khusus kelas di atas fitur *BEV*: setiap lokasi diberi skor kemungkinan menjadi pusat objek kelas tertentu. Sejumlah N lokasi dengan skor lokal tertinggi dipilih sebagai posisi awal *query* — pendekatan yang disebut inisialisasi bergantung-masukan (*input-dependent*). Setiap *query* juga diberi penyisipan (*embedding*) yang mencerminkan kelas kandidatnya, karena ukuran objek pada skala *BEV* berbeda nyata antar-kelas (pejalan kaki jauh lebih kecil dari bus). Menurut studi ablasi (pengujian pengaruh tiap komponen) pada set validasi *nuScenes*, inisialisasi bergantung-masukan menyumbang kenaikan 5,7 poin mAP dibandingkan *query* dengan parameter tetap, dan penyisipan kelas menyumbang tambahan 0,3 poin.

### Dekoder Lapis Pertama: Prediksi dari LiDAR

Lapis pertama dekoder menjalankan *self-attention* antar-*query* (agar kandidat yang tumpang tindih saling menyesuaikan diri) diikuti *cross-attention* dari tiap *query* ke seluruh fitur *BEV*. Keluarannya adalah kotak 3D awal untuk tiap *query*: posisi pusat (x, y, z), ukuran (panjang, lebar, tinggi), sudut putar (*yaw*), kecepatan, dan skor kelas. Model yang berhenti di tahap ini disebut TransFusion-L (varian *LiDAR* saja) dan sudah menjadi detektor yang kuat dengan sendirinya — pada set uji *nuScenes* mencapai 65,5% mAP dan 70,2% NDS.

### Dekoder Lapis Kedua: Fusi Adaptif dengan Attention Termodulasi Spasial

Lapis kedua menambahkan informasi citra melalui teknik yang disebut penulis *Spatially Modulated Cross Attention* (SMCA, *attention* silang termodulasi spasial). Pusat kotak 3D hasil lapis pertama diproyeksikan ke bidang citra tiap kamera memakai matriks kalibrasi — tetapi proyeksi ini hanya dipakai untuk menentukan **wilayah** perhatian, bukan untuk mengambil satu piksel tunggal. Di sekitar titik proyeksi itu, dipasang topeng Gaussian dua dimensi yang meredam bobot *attention* secara halus seiring jarak dari pusat; *cross-attention* kemudian dibatasi dan dibobot oleh topeng tersebut, sehingga *query* mengambil kombinasi berbobot dari fitur citra di wilayah relevan, bukan satu piksel yang bisa saja meleset akibat kalibrasi tidak sempurna. Studi ablasi mencatat modul fusi ini menyumbang kenaikan 4,0 poin mAP pada set validasi.

### Inisialisasi Berpandu Citra

Untuk objek yang sulit terlihat pada awan titik (jauh, tipis, atau nyaris tidak memantulkan laser), TransFusion menambahkan jalur kedua: fitur citra multi-kamera diproyeksikan ke bidang *BEV* melalui *cross-attention* terpisah, menghasilkan peta panas versi citra. Peta panas ini dirata-ratakan dengan peta panas *LiDAR* sebelum pemilihan N lokasi awal *query*, sehingga kandidat yang hanya tampak jelas di citra tetap berpeluang terpilih. Komponen ini menyumbang kenaikan 1,2 poin mAP menurut ablasi yang sama.

### Pelatihan dan Pencocokan Himpunan

Pelatihan memakai skema pencocokan himpunan (*set prediction*) seperti DETR: algoritme Hungarian mencocokkan tiap prediksi kotak dengan kebenaran lapangan (*ground truth*) terdekat, lalu galat dihitung dengan *focal loss* untuk klasifikasi dan L1 untuk regresi posisi. Karena tiap *query* sudah dipaksa mewakili satu kandidat objek berbeda sejak pencocokan, tahap penyaringan kotak tumpang tindih (*Non-Maximum Suppression*/NMS) yang lazim pada detektor lain tidak diperlukan lagi saat inferensi. Pelatihan dilakukan dua tahap berurutan: TransFusion-L dilatih dan dikonvergenkan lebih dulu, baru kemudian lapis fusi citra ditambahkan dan dilatih di atasnya; penulis mencatat pelatihan gabungan sejak awal (bersama-sama) memberi hasil yang lebih buruk.

Alur data dari kedua sensor hingga kotak akhir dirangkum berikut.

```
LiDAR point cloud                 Citra 6 kamera
      |                                 |
voxelisasi + BEV                 backbone 2D per-kamera
      |                                 |
fitur BEV (HxWxC)                 fitur citra per-kamera
      |                                 |
peta panas kelas -> top-N query <--(dirata-rata dgn peta
      |                            panas dari citra)
      v
DEKODER LAPIS 1: self-attn antar-query + cross-attn ke BEV
      |
      v
kotak 3D awal (x,y,z,l,w,h,yaw)  <-- keluaran TransFusion-L
      |
      v
proyeksi pusat kotak ke tiap kamera -> topeng Gaussian (SMCA)
      |
      v
DEKODER LAPIS 2: cross-attn berbobot topeng ke fitur citra
      |
      v
kotak 3D akhir + kelas per query (tanpa NMS)
```

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada *nuScenes* (kumpulan data deteksi 3D berkendara dengan *LiDAR* dan 6 kamera, dinilai dengan metrik mAP dan *NuScenes Detection Score*/NDS yang menggabungkan akurasi klasifikasi dan kesalahan atribut) serta *Waymo Open Dataset* (dinilai dengan mAPH, mAP berbobot arah/*heading*). Tabel berikut merangkum hasil pada set uji *nuScenes* dan set validasi *Waymo*.

| Model | nuScenes test (mAP / NDS) | Waymo val (mAPH gabungan) |
|---|---|---|
| TransFusion-L (LiDAR saja) | 65,5% / 70,2% | 64,9% |
| TransFusion (LiDAR + kamera) | 68,9% / 71,7% | 65,5% |

Selisih 3,4 poin mAP pada *nuScenes* menunjukkan kontribusi nyata fusi citra ketika awan titik cukup jarang (jarak jauh, kendaraan bergerak cepat). Pada *Waymo*, sensor *LiDAR* yang dipakai menghasilkan titik jauh lebih rapat, sehingga selisih mAPH menyempit menjadi 0,6 poin — citra menyumbang lebih sedikit ketika *LiDAR* saja sudah memadai. TransFusion juga diuji pada tugas pelacakan objek 3D (*3D tracking*, mengaitkan deteksi antar-*frame* video menjadi lintasan) dan mencatatkan AMOTA 0,718 pada set uji *nuScenes*, menempati posisi pertama papan peringkat pelacakan *nuScenes* saat makalah dipublikasikan — bukti bahwa kualitas deteksi per-*frame* yang stabil turut memperbaiki konsistensi lintasan antar-waktu.

Bagian paling relevan dengan klaim ketahanan (*robustness*) makalah adalah tiga uji degradasi terkendali pada set validasi. Pertama, pada subset citra malam hari, TransFusion naik dari 49,2% menjadi 55,2% mAP (+6,0 poin) dibandingkan model fusi berbasis konkatenasi fitur yang hanya naik 0,2 poin dan *PointAugmenting* yang naik 1,8 poin — menunjukkan asosiasi lunak tetap menarik manfaat dari citra gelap, sedangkan metode berbasis proyeksi keras nyaris tidak terbantu. Kedua, ketika seluruh 6 citra kamera dihilangkan saat inferensi, mAP TransFusion hanya turun 3,9 poin (ke 61,7%), sementara model konkatenasi turun 23,8 poin dan *PointAugmenting* turun 17,2 poin — TransFusion pada dasarnya kembali berperilaku seperti TransFusion-L ketika citra tidak tersedia, karena *attention* dapat memberi bobot mendekati nol pada fitur yang tidak berguna. Ketiga, dengan kesalahan kalibrasi buatan berupa pergeseran 1 meter antar-sensor, mAP TransFusion hanya turun 0,49 poin, jauh di bawah penurunan *PointAugmenting* (2,33 poin) dan konkatenasi (2,85 poin).

## Kelebihan dan Keterbatasan

Kelebihan utama TransFusion adalah ketahanannya terhadap kondisi sensor yang tidak ideal, dibuktikan lewat tiga uji degradasi terkendali di atas, bukan sekadar klaim kualitatif. Desain *set prediction* tanpa NMS menyederhanakan jalur inferensi, dan TransFusion-L sebagai produk sampingan sudah menjadi detektor *LiDAR* mandiri yang kompetitif, sehingga metode dapat dipakai bertahap: mulai dari *LiDAR* saja, lalu ditingkatkan dengan citra tanpa mengubah representasi dasar. Penulis juga menunjukkan generalisasi metode ke tugas pelacakan 3D tanpa perubahan arsitektur berarti.

Keterbatasan yang diakui penulis: peningkatan pada *Waymo* jauh lebih tipis daripada pada *nuScenes*, karena kepadatan titik *LiDAR* dan kategori objek yang lebih kasar pada dataset tersebut membuat fusi citra kurang bermanfaat; pelatihan juga harus dilakukan dua tahap berurutan karena pelatihan gabungan sejak awal terbukti memberi hasil lebih buruk. Dari sisi rekayasa, dua tulang punggung terpisah (3D untuk *LiDAR*, 2D untuk tiap kamera) ditambah dekoder *Transformer* dua lapis menambah beban komputasi dibandingkan metode fusi satu aliran; makalah tidak melaporkan kecepatan inferensi (FPS) secara eksplisit dalam ringkasan yang berhasil diverifikasi, sehingga biaya waktu nyata perlu dicek langsung pada naskah sebelum dijadikan dasar perbandingan kecepatan. Secara konseptual, mekanisme SMCA tetap memakai matriks kalibrasi untuk menentukan pusat topeng Gaussian, sehingga metode ini bukan sepenuhnya bebas kalibrasi — yang diperbaiki adalah ketergantungan mutlak padanya, bukan penghapusan totalnya.

## Kaitan dengan Bab Lain

TransFusion menjawab langsung kerapuhan asosiasi keras yang menjadi ciri metode fusi generasi sebelumnya: *PointPainting* (bab 093), yang mengecat titik *LiDAR* dengan label semantik dari citra, dan *3D-CVF* (bab 094), yang memproyeksikan fitur citra ke ruang *voxel* — keduanya diuji ulang di sini sebagai pembanding pada eksperimen ketahanan dan kalah pada kondisi degradasi sensor. Konsep *object query* dan pencocokan himpunan yang dipakai TransFusion diwarisi langsung dari DETR (bab 022), diadaptasi dari deteksi 2D ke 3D dengan menambah dimensi kedalaman dan orientasi. Tulang punggung *voxel*-*BEV* TransFusion-L sendiri melanjutkan garis metode berbasis *voxel* seperti *VoxelNet* (bab 087). Arah lanjutan dari gagasan fusi berbasis *attention* ini ditempuh *BEVFusion* (bab 098), yang menyatukan representasi *LiDAR* dan kamera ke satu ruang *BEV* bersama sebelum fusi, alih-alih memproyeksikan per-*query* seperti pada TransFusion — lihat [098 - 2022 - BEVFusion - Deteksi 3D](./098%20-%202022%20-%20BEVFusion%20-%20Deteksi%203D.md) untuk perbandingan langsung kedua pendekatan.

## Poin untuk Sitasi

Kutip dengan kunci `bai2022transfusion`. Ringkasan yang aman dikutip: "TransFusion mengganti asosiasi keras titik-piksel pada fusi *LiDAR*-kamera dengan asosiasi lunak berbasis *attention* Transformer dua lapis, mencapai 68,9% mAP dan 71,7% NDS pada set uji *nuScenes* serta ketahanan signifikan terhadap citra malam hari, kamera yang hilang, dan kesalahan kalibrasi sensor." Angka mAP/NDS test set, hasil Waymo, dan tiga angka uji ketahanan (malam hari, citra hilang, misalignment 1 meter) diperoleh dari versi HTML naskah (ar5iv) dan tabel README repositori kode resmi; angka kecepatan inferensi (FPS/latensi) dan jumlah parameter tepat tidak berhasil diverifikasi silang dari dua sumber independen sehingga sebaiknya dicek ulang ke tabel asli sebelum dikutip dalam karya formal.
