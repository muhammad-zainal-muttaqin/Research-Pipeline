# 071 - Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024depthanything` |
| Judul asli | Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data |
| Penulis | Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Jiashi Feng, Hengshuang Zhao |
| Tahun | 2024 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2401.10891
- **Halaman proyek:** https://depth-anything.github.io
- **Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%3A%20Unleashing%20the%20Power%20of%20Large-Scale%20Unlabeled%20Data
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Depth%20Anything%3A%20Unleashing%20the%20Power%20of%20Large-Scale%20Unlabeled%20Data&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Depth Anything, model fondasi untuk estimasi kedalaman monokular (*monocular depth estimation*, MDE): tugas memprediksi peta kedalaman — jarak setiap piksel terhadap kamera — dari satu citra RGB. Makalah ini tidak merancang modul jaringan baru, melainkan menyerang masalah dari sisi data: sebuah *data engine* mengumpulkan sekitar 62 juta citra tanpa label dari delapan dataset publik dan memberinya anotasi otomatis. Model siswa dilatih meniru *pseudo-label* (label hasil prediksi model, bukan pengukuran sensor) dari model guru, dengan dua strategi kunci: target optimasi yang lebih sulit melalui distorsi kuat, dan supervisi yang mempertahankan prior semantik dari encoder pra-latih DINOv2.

Hasilnya adalah model kedalaman relatif *zero-shot* — dievaluasi pada dataset yang tidak pernah dilihat saat pelatihan — yang mengungguli MiDaS v3.1 pada enam tolok ukur sekaligus, dan mencetak rekor baru pada NYUv2 dan KITTI setelah disetel halus dengan kedalaman metrik. Model dirilis dalam tiga ukuran: ViT-S (24,8 juta parameter), ViT-B (97,5 juta), dan ViT-L (335,3 juta).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra adalah masalah *ill-posed*: satu citra dua dimensi bersesuaian dengan tak-hingga susunan adegan tiga dimensi, sehingga model harus mempelajari prior dari data. Garis penelitiannya bergerak dari pelatihan terawasi pada data sensor (Eigen dkk., bab 062), pencampuran banyak dataset dengan loss *affine-invariant* (MiDaS, bab 068), hingga *backbone Vision Transformer* (DPT, bab 067).

Kendala yang tersisa adalah cakupan data. Dataset berlabel dibangun dari sensor (LiDAR, kamera RGB-D), pencocokan stereo, atau *structure-from-motion* — mahal, lambat, atau mustahil pada situasi tertentu — sehingga cakupannya sempit dan model seperti MiDaS terdegradasi parah di luar cakupannya. Model fondasi di bidang lain menunjukkan generalisasi lahir dari data berskala puluhan juta; makalah ini menunjukkan cara mencapai skala itu untuk kedalaman tanpa label.

## Ide Utama

Gagasan intinya adalah memindahkan sumber skala dari "lebih banyak label" ke "lebih banyak citra". Citra monokular tanpa label tersedia hampir tanpa biaya, jauh lebih beragam, dan dapat dianotasi otomatis oleh model guru — model MDE memprediksi kedalaman dengan satu kali *forward pass*.

Masalahnya, *self-training* naif (siswa meniru guru) tidak memberi gain dalam percobaan awal penulis. Dua strategi diusulkan. Pertama, siswa diberi target optimasi yang lebih sulit: citra masukannya didistorsi kuat, sementara targetnya tetap dihasilkan guru dari citra bersih. Kedua, siswa diikat pada prior semantik DINOv2 melalui loss penyelarasan fitur, bukan melalui tugas segmentasi tambahan.

## Cara Kerja Langkah demi Langkah

### Mesin Data: 1,5 Juta Berlabel dan 62 Juta Tak-Berlabel

Himpunan berlabel berisi 1,5 juta citra dari enam dataset publik — BlendedMVS (115 ribu), DIML (927 ribu), HRWSI (20 ribu), IRS (103 ribu), MegaDepth (128 ribu), TartanAir (306 ribu) — dengan label dari stereo atau *structure-from-motion*. Himpunan tak-berlabel berisi lebih dari 62 juta citra dari delapan dataset publik: SA-1B, Open Images V7, BDD100K, ImageNet-21K, LSUN, Objects365, Places365, dan Google Landmarks. NYUv2 dan KITTI sengaja disingkirkan dari data latih agar tetap murni sebagai uji *zero-shot*.

### Melatih Guru pada Data Berlabel

Arsitektur mengikuti MiDaS: encoder *Vision Transformer* (ViT), yang memotong citra menjadi *patch* 14×14 piksel dan mengolahnya sebagai urutan token, diinisialisasi dari bobot DINOv2 — model ViT pra-latih mandiri (*self-supervised*) yang kuat pada tugas semantik — ditambah decoder DPT yang merakit fitur multi-skala menjadi peta kedalaman. Nilai kedalaman t diubah ke ruang disparitas d = 1/t dan dinormalisasi ke rentang 0–1 per peta. Loss-nya bersifat *affine-invariant*: prediksi dan target digeser dengan mediannya lalu diskalakan dengan simpangan absolut rata-ratanya, sebelum dibandingkan per piksel. Normalisasi ini membuat dua peta yang hanya berbeda skala dan pergeseran dianggap identik, sehingga dataset bersatuan berbeda dapat dicampur — dan keluaran model menjadi kedalaman relatif (urutan dekat–jauh), bukan jarak dalam meter. Varian terbaik tahap ini, yang berbasis ViT-L, menjadi guru T.

### Pseudo-Label dan Distorsi Kuat untuk Siswa

Guru T memprediksi peta kedalaman untuk seluruh citra tak-berlabel dalam bentuk bersih. Siswa S diinisialisasi ulang dari bobot DINOv2 — bukan melanjutkan bobot guru, sesuai temuan *self-training* — lalu dilatih pada gabungan data berlabel dan berlabel semu. Kombinasi naif ini gagal memperbaiki baseline: guru dan siswa berbagi arsitektur serta inisialisasi yang sama, sehingga keduanya cenderung benar dan salah pada tempat yang sama dan tidak saling menambah pengetahuan.

Solusinya adalah menyulitkan siswa dengan dua distorsi pada citra tak-berlabel, sementara guru tetap melihat citra bersih. Distorsi pertama fotometrik: *color jittering* dan *Gaussian blurring* kuat. Distorsi kedua spasial: CutMix, diterapkan dengan peluang 50%. Pada CutMix, dua citra 518×518 piksel, u_a dan u_b, dijahit memakai mask biner M yang bernilai 1 pada satu wilayah persegi: citra campuran u_ab = u_a ⊙ M + u_b ⊙ (1 − M) berisi potongan citra pertama di dalam persegi dan citra kedua di luarnya. Loss dihitung terpisah per wilayah — prediksi siswa pada wilayah M dibandingkan dengan *pseudo-label* guru untuk u_a, sisanya dengan *pseudo-label* untuk u_b — lalu digabung dengan rata-rata berbobot menurut luas wilayah. Target ini menuntut prediksi benar pada citra rusak atau campuran, yang tidak dituntut *self-training* naif.

### Penyelarasan Fitur Semantik dengan DINOv2

Upaya pertama memberi label segmentasi lewat kombinasi model RAM, GroundingDINO, dan HQ-SAM (ruang 4.000 kelas) gagal menambah performa; pemetaan citra ke kelas diskrit diduga membuang terlalu banyak informasi semantik. Sebagai gantinya dipakai loss penyelarasan fitur: fitur per piksel dari encoder siswa, f, didorong memiliki kemiripan kosinus tinggi dengan fitur f′ dari encoder DINOv2 yang dibekukan, melalui loss bernilai 1 dikurangi rata-rata kemiripan kosinus keduanya. Diterapkan pula margin toleransi α = 0,85: piksel yang kemiripannya sudah melewati α dikeluarkan dari loss. Alasannya, DINOv2 menghasilkan fitur serupa untuk bagian berbeda dari satu objek (misalnya depan dan belakang mobil), padahal kedalamannya berbeda; tanpa toleransi, model dipaksa meniru fitur yang kontraproduktif bagi diskriminasi kedalaman antar-bagian objek.

### Jadwal Pelatihan dan Inferensi

Seluruh citra dipangkas ke 518×518 piksel saat pelatihan. Guru dilatih 20 *epoch* pada data berlabel; siswa menyapu seluruh 62 juta citra satu kali, dengan rasio citra berlabel terhadap tak-berlabel 1:2 per *batch*. Optimizer-nya AdamW, dengan laju belajar encoder 5×10⁻⁶ dan decoder sepuluh kali lebih besar. Loss total adalah rata-rata dari loss berlabel, loss *pseudo-label*, dan loss penyelarasan. Saat inferensi citra tidak dipangkas — kedua sisi cukup dibuat kelipatan 14 — dan prediksi diinterpolasi ke resolusi asli.

Alur dua tahap tersebut dirangkum pada diagram berikut:

```
    TAHAP 1 (latih guru)           TAHAP 2 (latih siswa)
 ┌────────────────────────┐     ┌────────────────────────────┐
 │ 1,5 jt citra berlabel  │     │ 62 jt citra tak-berlabel   │
 │ (6 dataset publik)     │     │ (8 dataset publik)         │
 └───────────┬────────────┘     └─────┬────────────────┬─────┘
             ▼                        ▼ bersih         ▼ distorsi kuat
  encoder DINOv2 (ViT)      ┌──────────────┐    (jitter warna, blur,
  + decoder DPT             │ guru T (beku)│     CutMix 50%)
  loss affine-invariant     └──────┬───────┘            │
             │                     ▼                    ▼
             ▼              pseudo-label depth   siswa S (re-init,
        guru T (ViT-L)            │              DINOv2 + DPT)
                                  └──► loss L_u ◄──────┘
 loss total = rata-rata( L_l [berlabel], L_u [pseudo-label],
                         L_feat [align ke DINOv2 beku, alpha 0,85] )
```

Diagram menegaskan bahwa guru dilatih hanya pada data berlabel lalu dibekukan, dan siswa tidak pernah melihat citra tak-berlabel yang bersih.

## Eksperimen dan Hasil

Kemampuan *zero-shot* kedalaman relatif diuji pada enam dataset yang tidak pernah dilihat: KITTI, NYUv2, Sintel, DDAD, ETH3D, dan DIODE. Metriknya AbsRel (rata-rata galat relatif absolut, makin kecil makin baik) dan δ1 (persentase piksel dengan rasio prediksi terhadap kebenaran di bawah 1,25, makin besar makin baik). Pembandingnya model terkuat MiDaS v3.1.

- Pada DDAD (berkendara otonom), AbsRel turun dari 0,251 menjadi 0,230 dan δ1 naik dari 0,766 menjadi 0,789.
- Pada KITTI, Depth Anything mencapai AbsRel 0,076 dan δ1 0,947, berbanding 0,127 dan 0,850 milik MiDaS — padahal MiDaS memakai citra latih KITTI sehingga tidak lagi *zero-shot*, sedangkan Depth Anything tidak pernah melihatnya.
- Model ViT-B sudah mengungguli MiDaS yang berbasis model jauh lebih besar; bahkan ViT-S — kurang dari sepersepuluh ukurannya — masih menang pada Sintel, DDAD, dan ETH3D.

Interpretasinya, perbaikan bukan sekadar fungsi kapasitas model: varian kecil dengan resep data yang sama tetap unggul, sehingga cakupan datalah faktor pembedanya. Untuk kedalaman metrik, encoder ViT-L disetel halus dalam kerangka ZoeDepth (model yang memasang *head* bin kedalaman metrik di atas encoder MiDaS). Pada NYUv2, δ1 naik dari 0,964 menjadi 0,984 dan AbsRel turun dari 0,069 menjadi 0,056, melampaui VPD sebagai metode terbaik sebelumnya; pada KITTI, δ1 naik dari 0,978 menjadi 0,982. Pada pengujian metrik *zero-shot*, mengganti encoder MiDaS di dalam ZoeDepth dengan encoder Depth Anything memperbaiki hasil pada seluruh dataset uji indoor maupun outdoor.

Encoder hasil pelatihan MDE ini juga unggul untuk segmentasi semantik — 86,2 mIoU pada Cityscapes (Swin-L 84,3; ConvNeXt-XL 84,6) dan 59,4 pada ADE20K (sebelumnya 58,3) — sehingga berpotensi menjadi encoder multi-tugas. Studi ablasi memvalidasi tiap komponen: *pseudo-label* tanpa distorsi tidak memberi perbaikan; distorsi kuat membuat data tak-berlabel menaikkan generalisasi secara signifikan; loss penyelarasan memperkuat efek itu. Margin toleransi terbukti penting (rata-rata AbsRel pada enam dataset uji 0,188 tanpa toleransi berbanding 0,175 dengan α = 0,85), sedangkan penyelarasan pada data berlabel tidak membantu (0,180 berbanding 0,179). Model ini juga memperbaiki ControlNet berkondisi kedalaman untuk sintesis citra terkendali.

## Kelebihan dan Keterbatasan

Kelebihannya: (1) generalisasi *zero-shot* terkuat pada masanya di enam tolok ukur, dicapai tanpa modul arsitektur baru — kontribusinya murni pada resep data dan pelatihan; (2) tiga ukuran model menutupi kebutuhan dari perangkat terbatas hingga akurasi maksimal; (3) encoder-nya berguna ganda untuk kedalaman metrik dan segmentasi; (4) *pipeline* anotasi otomatis dapat diskalakan nyaris tanpa batas.

Keterbatasannya: (1) keluaran aslinya kedalaman relatif, sehingga aplikasi yang membutuhkan jarak metrik harus menyetel halus dengan data metrik; (2) penulis sendiri menyatakan ukuran model terbesar baru ViT-L dan resolusi latih 518 piksel kurang memadai untuk aplikasi dunia nyata; (3) mutu *pseudo-label* dibatasi kemampuan guru — kesalahan sistematis guru pada domain tertentu akan diwarisi siswa; (4) dari sisi rekayasa, anotasi 62 juta citra dan pelatihan siswa memakan biaya komputasi besar, sehingga reproduksi penuh sulit bagi laboratorium kecil; (5) secara konseptual, seluruh resep bertumpu pada encoder pra-latih sekelas DINOv2 — ini strategi komposisi di atas model fondasi yang ada, bukan resep dari nol.

## Kaitan dengan Bab Lain

Dalam silsilah kedalaman monokular tinjauan ini, regresi kedalaman terawasi diletakkan oleh Eigen dkk. pada [bab 062](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md); arsitektur decoder yang dipakai berasal dari DPT pada [bab 067](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md); resep loss *affine-invariant* dan peran pembanding utama diwarisi dari MiDaS pada [bab 068](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md); posisinya di antara metode lain dipetakan pada [bab 072](./072%20-%202021%20-%20Review%20Depth%20Monokular%20%28Ming%20dkk.%29%20-%20Estimasi%20Kedalaman.md). Bagi agenda YOLO + RGB-D, bab ini pemasok *pseudo-depth* murah: peta kedalamannya dapat menggantikan sensor kedalaman pada skenario RGB murni, sehingga fusi RGB-D dapat dibangun tanpa perangkat keras tambahan.

## Poin untuk Sitasi

Kutip dengan kunci `yang2024depthanything`. Ringkasan yang aman dikutip: "Depth Anything melatih model fondasi kedalaman monokular dengan menggabungkan 1,5 juta citra berlabel dan sekitar 62 juta citra tak-berlabel yang diberi *pseudo-label* otomatis; dua strategi kunci — target optimasi lebih sulit melalui distorsi kuat dan penyelarasan fitur ke DINOv2 — menjadikan modelnya unggul *zero-shot* atas MiDaS pada enam tolok ukur serta mencetak rekor kedalaman metrik pada NYUv2 dan KITTI setelah disetel halus." Seluruh angka diambil dari naskah arXiv v2; makalah ini tergolong sangat baru dan memuat banyak tabel, sehingga setiap angka wajib diverifikasi ulang ke naskah asli sebelum sitasi formal.
