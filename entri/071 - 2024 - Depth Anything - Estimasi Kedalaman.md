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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen set). Right two: photos captured by ourselves. Our model works robustly in low-light environments (1st and 3rd column), complex scenes (2nd and 5th column), foggy weather (5th column), and ultra-remote distance (5th and 6th column), etc.

1. Introduction

Abstract This work presents Depth Anything1 , a highly practical solution for robust monocular depth estimation. Without pursuing novel technical modules, we aim to build a simple yet powerful foundation model dealing with any images under any circumstances. To this end, we scale up the dataset by designing a data engine to collect and automatically annotate large-scale unlabeled data (∼62M), which significantly enlarges the data coverage and thus is able to reduce the generalization error. We investigate two simple yet effective strategies that make data scaling-up promising. First, a more challenging optimization target is created by leveraging data augmentation tools. It compels the model to actively seek extra visual knowledge and acquire robust representations. Second, an auxiliary supervision is developed to enforce the model to inherit rich semantic priors from pre-trained encoders. We evaluate its zero-shot capabilities extensively, including six public datasets and randomly captured photos. It demonstrates impressive generalization ability (Figure 1). Further, through fine-tuning it with metric depth information from NYUv2 and KITTI, new SOTAs are set. Our better depth model also results in a better depth-conditioned ControlNet. Our models are released here.

The field of computer vision and natural language processing is currently experiencing a revolution with the emergence of “foundation models” [6] that demonstrate strong zero-/fewshot performance in various downstream scenarios [45, 59]. These successes primarily rely on large-scale training data that can effectively cover the data distribution. Monocular Depth Estimation (MDE), which is a fundamental problem with broad applications in robotics [66], autonomous driving [64, 80], virtual reality [48], etc., also requires a foundation model to estimate depth information from a single image. However, this has been underexplored due to the difficulty of building datasets with tens of millions of depth labels. MiDaS [46] made a pioneering study along this direction by training an MDE model on a collection of mixed labeled datasets. Despite demonstrating a certain level of zero-shot ability, MiDaS is limited by its data coverage, thus suffering disastrous performance in some scenarios. In this work, our goal is to build a foundation model for MDE capable of producing high-quality depth information for any images under any circumstances. We approach this target from the perspective of dataset scaling-up. Traditionally, depth datasets are created mainly by acquiring depth data from sensors [18, 55], stereo matching [15], or SfM [33], which is costly, time-consuming, or even intractable in particular situations. We instead, for the first time, pay attention to large-scale unlabeled data. Compared with stereo images or

Work was done during an internship at TikTok. 1While the grammatical soundness of this name may be questionable,

labeled images from depth sensors, our used monocular unlabeled images exhibit three advantages: (i) (simple and cheap to acquire) Monocular images exist almost everywhere, thus they are easy to collect, without requiring specialized devices. (ii) (diverse) Monocular images can cover a broader range of scenes, which are critical to the model generalization ability and scalability. (iii) (easy to annotate) We can simply use a pre-trained MDE model to assign depth labels for unlabeled images, which only takes a feedforward step. More than efficient, this also produces denser depth maps than LiDAR [18] and omits the computationally intensive stereo matching process. We design a data engine to automatically generate depth annotations for unlabeled images, enabling data scaling-up to arbitrary scale. It collects 62M diverse and informative images from eight public large-scale datasets, e.g., SA-1B [27], Open Images [30], and BDD100K [82]. We use their raw unlabeled images without any forms of labels. Then, in order to provide a reliable annotation tool for our unlabeled images, we collect 1.5M labeled images from six public datasets to train an initial MDE model. The unlabeled images are then automatically annotated and jointly learned with labeled images in a self-training manner [31]. Despite all the aforementioned advantages of monocular unlabeled images, it is indeed not trivial to make positive use of such large-scale unlabeled images [73, 90], especially in the case of sufficient labeled images and strong pre-training models. In our preliminary attempts, directly combining labeled and pseudo labeled images failed to improve the baseline of solely using labeled images. We conjecture that, the additional knowledge acquired in such a naive self-teaching manner is rather limited. To address the dilemma, we propose to challenge the student model with a more difficult optimization target when learning the pseudo labels. The student model is enforced to seek extra visual knowledge and learn robust representations under various strong perturbations to better handle unseen images. Furthermore, there have been some works [9, 21] demonstrating the benefit of an auxiliary semantic segmentation task for MDE. We also follow this research line, aiming to equip our model with better high-level scene understanding capability. However, we observed when an MDE model is already powerful enough, it is hard for such an auxiliary task to bring further gains. We speculate that it is due to severe loss in semantic information when decoding an image into a discrete class space. Therefore, considering the excellent performance of DINOv2 in semantic-related tasks, we propose to maintain the rich semantic priors from it with a simple feature alignment loss. This not only enhances the MDE performance, but also yields a multi-task encoder for both middle-level and high-level perception tasks. Our contributions are summarized as follows:

cheap, and diverse unlabeled images for MDE. • We point out a key practice in jointly training largescale labeled and unlabeled images. Instead of learning raw unlabeled images directly, we challenge the model with a harder optimization target for extra knowledge. • We propose to inherit rich semantic priors from pretrained encoders for better scene understanding, rather than using an auxiliary semantic segmentation task. • Our model exhibits stronger zero-shot capability than MiDaS-BEiTL-512 [5]. Further, fine-tuned with metric depth, it outperforms ZoeDepth [4] significantly.

2. Related Work Monocular depth estimation (MDE). Early works [23, 37, 51] primarily relied on handcrafted features and traditional computer vision techniques. They were limited by their reliance on explicit depth cues and struggled to handle complex scenes with occlusions and textureless regions. Deep learning-based methods have revolutionized monocular depth estimation by effectively learning depth representations from delicately annotated datasets [18, 55]. Eigen et al. [17] first proposed a multi-scale fusion network to regress the depth. Following this, many works consistently improve the depth estimation accuracy by carefully designing the regression task as a classification task [3, 34], introducing more priors [32, 54, 76, 83], and better objective functions [68, 78], etc. Despite the promising performance, they are hard to generalize to unseen domains. Zero-shot depth estimation. Our work belongs to this research line. We aim to train an MDE model with a diverse training set and thus can predict the depth for any given image. Some pioneering works [10, 67] explored this direction by collecting more training images, but their supervision is very sparse and is only enforced on limited pairs of points. To enable effective multi-dataset joint training, a milestone work MiDaS [46] utilizes an affine-invariant loss to ignore the potentially different depth scales and shifts across varying datasets. Thus, MiDaS provides relative depth information. Recently, some works [4, 22, 79] take a step further to estimate the metric depth. However, in our practice, we observe such methods exhibit poorer generalization ability than MiDaS, especially its latest version [5]. Besides, as demonstrated by ZoeDepth [4], a strong relative depth estimation model can also work well in generalizable metric depth estimation by fine-tuning with metric depth information. Therefore, we still follow MiDaS in relative depth estimation, but further strengthen it by highlighting the value of large-scale monocular unlabeled images. Leveraging unlabeled data. This belongs to the research area of semi-supervised learning [31, 56, 90], which is popular with various applications [71, 75]. However, existing

works typically assume only limited images are available. They rarely consider the challenging but realistic scenario where there are already sufficient labeled images but also larger-scale unlabeled images. We take this challenging direction for zero-shot MDE. We demonstrate that unlabeled images can significantly enhance the data coverage and thus improve model generalization and robustness.

3.1. Learning Labeled Images

Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly.

This process is similar to the training of MiDaS [5, 46]. However, since MiDaS did not release its code, we first reproduced it. Concretely, the depth value is first transformed into the disparity space by d = 1/t and then normalized to 0∼1 on each depth map. To enable multi-dataset joint training, we adopt the affine-invariant loss to ignore the unknown scale and shift of each sample:

our easy-to-acquire and diverse unlabeled images will comprehend the data coverage and greatly enhance the model generalization ability and robustness. Furthermore, to strengthen the teacher model T learned from these labeled images, we adopt the DINOv2 [43] pretrained weights to initialize our encoder. In practice, we apply a pre-trained semantic segmentation model [70] to detect the sky region, and set its disparity value as 0 (farthest).

3.2. Unleashing the Power of Unlabeled Images

where d∗i and di are the prediction and ground truth, respectively. And ρ is the affine-invariant mean absolute error loss: ρ(d∗i , di ) = |dˆ∗i − dˆi |, where dˆ∗i and dˆi are the scaled and shifted versions of the prediction d∗i and ground truth di :

This is the main point of our work. Distinguished from prior works that laboriously construct diverse labeled datasets, we highlight the value of unlabeled images in enhancing the data coverage. Nowadays, we can practically build a diverse and large-scale unlabeled set from the Internet or public datasets of various tasks. Also, we can effortlessly obtain the dense depth map of monocular unlabeled images simply by forwarding them to a pre-trained well-performed MDE model. This is much more convenient and efficient than performing stereo matching or SfM reconstruction for stereo images or videos. We select eight large-scale public datasets as our unlabeled sources for their diverse scenes. They contain more than 62M images in total. The details are provided in the bottom half of Table 1. Technically, given the previously obtained MDE teacher model T , we make predictions on the unlabeled set Du to obtain a pseudo labeled set D̂u :

Our work utilizes both labeled and unlabeled images to facilitate better monocular depth estimation (MDE). Formally, the labeled and unlabeled sets are denoted as Dl = u N {(xi , di )}M i=1 and D = {ui }i=1 respectively. We aim to learn a teacher model T from Dl . Then, we utilize T to assign pseudo depth labels for Du . Finally, we train a student model S on the combination of labeled set and pseudo labeled set. A brief illustration is provided in Figure 2.

3. Depth Anything

To obtain a robust monocular depth estimation model, we collect 1.5M labeled images from 6 public datasets. Details of these datasets are listed in Table 1. We use fewer labeled datasets than MiDaS v3.1 [5] (12 training datasets), because 1) we do not use NYUv2 [55] and KITTI [18] datasets to ensure zero-shot evaluation on them, 2) some datasets are not available (anymore), e.g., Movies [46] and WSVD [61], and 3) some datasets exhibit poor quality, e.g., RedWeb (also low resolution) [67]. Despite using fewer labeled images,

With the combination set Dl ∪ Dˆu of labeled images and pseudo labeled images, we train a student model S on it. 3

Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The S denotes adding strong perturbations (Section 3.2). To equip our depth estimation model with rich semantic priors, we enforce an auxiliary constraint between the online student model and a frozen encoder to preserve the semantic capability (Section 3.3).

P where we omit the and pixel subscript i for simplicity. Then we aggregate the two losses via weighted averaging:

Following prior works [74], instead of fine-tuning S from T , we re-initialize S for better performance. Unfortunately, in our pilot studies, we failed to gain improvements with such a self-training pipeline, which indeed contradicts the observations when there are only a few labeled images [56]. We conjecture that, with already sufficient labeled images in our case, the extra knowledge acquired from additional unlabeled images is rather limited. Especially considering the teacher and student share the same pre-training and architecture, they tend to make similar correct or false predictions on the unlabeled set Du , even without the explicit self-training procedure. To address the dilemma, we propose to challenge the student with a more difficult optimization target for additional visual knowledge on unlabeled images. We inject strong perturbations to unlabeled images during training. It compels our student model to actively seek extra visual knowledge and acquire invariant representations from these unlabeled images. These advantages help our model deal with the open world more robustly. We introduce two forms of perturbations: one is strong color distortions, including color jittering and Gaussian blurring, and the other is strong spatial distortion, which is CutMix [84]. Despite the simplicity, the two modifications make our large-scale unlabeled images significantly improve the baseline of labeled images. We provide more details about CutMix. It was originally proposed for image classification, and is rarely explored in monocular depth estimation. We first interpolate a random pair of unlabeled images ua and ub spatially: u_{ab} = u_a \odot M + u_b \odot (1 - M),

We use CutMix with 50% probability. The unlabeled images for CutMix are already strongly distorted in color, but the unlabeled images fed into the teacher model T for pseudo labeling are clean, without any distortions.

3.3. Semantic-Assisted Perception There exist some works [9, 21, 28, 72] improving depth estimation with an auxiliary semantic segmentation task. We believe that arming our depth estimation model with such high-level semantic-related information is beneficial. Besides, in our specific context of leveraging unlabeled images, these auxiliary supervision signals from other tasks can also combat the potential noise in our pseudo depth label. Therefore, we made an initial attempt by carefully assigning semantic segmentation labels to our unlabeled images with a combination of RAM [86] + GroundingDINO [38] + HQ-SAM [26] models. After post-processing, this yields a class space containing 4K classes. In the joint-training stage, the model is enforced to produce both depth and segmentation predictions with a shared encoder and two individual decoders. Unfortunately, after trial and error, we still could not boost the performance of the original MDE model. We speculated that, decoding an image into a discrete class space indeed loses too much semantic information. The limited information in these semantic masks is hard to further boost our depth model, especially when our depth model has established very competitive results. Therefore, we aim to seek more informative semantic signals to serve as auxiliary supervision for our depth estimation task. We are greatly astonished by the strong performance of DINOv2 models [43] in semantic-related tasks, e.g., image retrieval and semantic segmentation, even with frozen weights without any fine-tuning. Motivated by these clues, we propose to transfer its strong semantic capability to our

Method

Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓ , δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS does not strictly follow the zero-shot evaluation on KITTI and NYUv2, because it uses their training images. We provide three model scales for different purposes, based on ViT-S (24.8M), ViT-B (97.5M), and ViT-L (335.3M), respectively. Best, second best results.

depth model with an auxiliary feature alignment loss. The feature space is high-dimensional and continuous, thus containing richer semantic information than discrete masks. The feature alignment loss is formulated as: \mathcal {L}_{feat} = 1 - \frac {1}{HW}\sum _{i=1}^{HW}\cos (f_i, f'_i),

depth regression. All labeled datasets are simply combined together without re-sampling. In the first stage, we train a teacher model on labeled images for 20 epochs. In the second stage of joint training, we train a student model to sweep across all unlabeled images for one time. The unlabeled images are annotated by a best-performed teacher model with a ViT-L encoder. The ratio of labeled and unlabeled images is set as 1:2 in each batch. In both stages, the base learning rate of the pre-trained encoder is set as 5e-6, while the randomly initialized decoder uses a 10× larger learning rate. We use the AdamW optimizer and decay the learning rate with a linear schedule. We only apply horizontal flipping as our data augmentation for labeled images. The tolerance margin α for feature alignment loss is set as 0.85. For more details, please refer to our appendix.

where cos(·, ·) measures the cosine similarity between two feature vectors. f is the feature extracted by the depth model S, while f ′ is the feature from a frozen DINOv2 encoder. We do not follow some works [19] to project the online feature f into a new space for alignment, because a randomly initialized projector makes the large alignment loss dominate the overall loss in the early stage. Another key point in feature alignment is that, semantic encoders like DINOv2 tend to produce similar features for different parts of an object, e.g., car front and rear. In depth estimation, however, different parts or even pixels within the same part, can be of varying depth. Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder. To solve this issue, we set a tolerance margin α for the feature alignment. If the cosine similarity of fi and fi′ has surpassed α, this pixel will not be considered in our Lf eat . This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision. As a side effect, our produced encoder not only performs well in downstream MDE datasets, but also achieves strong results in the semantic segmentation task. It also indicates the potential of our encoder to serve as a universal multi-task encoder for both middle-level and high-level perception tasks. Finally, our overall loss is an average combination of the three losses Ll , Lu , and Lf eat .

4.2. Zero-Shot Relative Depth Estimation As aforementioned, this work aims to provide accurate depth estimation for any image. Therefore, we comprehensively validate the zero-shot depth estimation capability of our Depth Anything model on six representative unseen datasets: KITTI [18], NYUv2 [55], Sintel [7], DDAD [20], ETH3D [52], and DIODE [60]. We compare with the best DPT-BEiTL-512 model from the latest MiDaS v3.1 [5], which uses more labeled images than us. As shown in Table 2, both with a ViT-L encoder, our Depth Anything surpasses the strongest MiDaS model tremendously across extensive scenes in terms of both the AbsRel (absolute relative error: |d∗ − d|/d) and δ1 (percentage of max(d∗ /d, d/d∗ ) < 1.25) metrics. For example, when tested on the well-known autonomous driving dataset DDAD [20], we improve the AbsRel (↓) from 0.251 → 0.230 and improve the δ1 (↑) from 0.766 → 0.789. Besides, our ViT-B model is already clearly superior to the MiDaS based on a much larger ViT-L. Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ETH3D. The performance advantage of these small-scale models demonstrates their great potential in computationally-constrained scenarios. It is also worth noting that, on the most widely used MDE

Method

Method

coder with metric depth information from NYUv2 [55] (for indoor scenes) or KITTI [18] (for outdoor scenes). Therefore, we simply replace the MiDaS encoder with our better Depth Anything encoder, leaving other components unchanged. As shown in Table 5, across a wide range of unseen datasets of indoor and outdoor scenes, our Depth Anything results in a better metric depth estimation model than the original ZoeDepth based on MiDaS.

4.3. Fine-tuned to Metric Depth Estimation Apart from the impressive performance in zero-shot relative depth estimation, we further examine our Depth Anything model as a promising weight initialization for downstream metric depth estimation. We initialize the encoder of downstream MDE models with our pre-trained encoder parameters and leave the decoder randomly initialized. The model is fine-tuned with correponding metric depth information. In this part, we use our ViT-L encoder for fine-tuning. We examine two representative scenarios: 1) in-domain metric depth estimation, where the model is trained and evaluated on the same domain (Section 4.3.1), and 2) zeroshot metric depth estimation, where the model is trained on one domain, e.g., NYUv2 [55], but evaluated in different domains, e.g., SUN RGB-D [57] (Section 4.3.2).

4.4. Fine-tuned to Semantic Segmentation In our method, we design our MDE model to inherit the rich semantic priors from a pre-trained encoder via a simple feature alignment constraint. Here, we examine the semantic capability of our MDE encoder. Specifically, we fine-tune our MDE encoder to downstream semantic segmentation datasets. As exhibited in Table 7 of the Cityscapes dataset [15], our encoder from large-scale MDE training (86.2 mIoU) is superior to existing encoders from large-scale ImageNet-21K pre-training, e.g., Swin-L [39] (84.3) and ConvNeXt-XL [41] (84.6). Similar observations hold on the ADE20K dataset [89] in Table 8. We improve the previous best result from 58.3 → 59.4. We hope to highlight that, witnessing the superiority of our pre-trained encoder on both monocular depth estimation and semantic segmentation tasks, we believe it has great potential to serve as a generic multi-task encoder for both middle-level and high-level visual perception systems.

As shown in Table 3 of NYUv2 [55], our model outperforms the previous best method VPD [87] remarkably, improving the δ1 (↑) from 0.964 → 0.984 and AbsRel (↓) from 0.069 to 0.056. Similar improvements can be observed in Table 4 of the KITTI dataset [18]. We improve the δ1 (↑) on KITTI from 0.978 → 0.982. It is worth noting that we adopt the ZoeDepth framework for this scenario with a relatively basic depth model, and we believe our results can be further enhanced if equipped with more advanced architectures. 4.3.2

Table 4. Fine-tuning and evaluating on KITTI [18] with our pre-trained MDE encoder. ∗: Reproduced by us.

benchmarks KITTI and NYUv2, although MiDaS v3.1 uses the corresponding training images (not zero-shot anymore), our Depth Anything is still evidently superior to it without training with any KITTI or NYUv2 images, e.g., 0.127 vs. 0.076 in AbsRel and 0.850 vs. 0.947 in δ1 on KITTI.

Table 3. Fine-tuning and evaluating on NYUv2 [55] with our pre-trained MDE encoder. We highlight best, second best results, as well as most discriminative metrics. ∗: Reproduced by us.

4.5. Ablation Studies Unless otherwise specified, we use the ViT-L encoder for our ablation studies here. Zero-shot transferring of each training dataset. In Table 6, we provide the zero-shot transferring performance of each training dataset, which means that we train a relative MDE model on one training set and evaluate it on the six unseen datasets. With these results, we hope to offer more insights for future works that similarly aim to build a general

We follow ZoeDepth [4] to conduct zero-shot metric depth estimation. ZoeDepth fine-tunes the MiDaS pre-trained en6

Method ZoeDepth [4] Depth Anything

Table 5. Zero-shot metric depth estimation. The first three test sets in the header are indoor scenes, while the last two are outdoor scenes. Following ZoeDepth, we use the model trained on NYUv2 for indoor generalization, while use the model trained on KITTI for outdoor evaluation. For fair comparisons, we report the ZoeDepth results reproduced in our environment. KITTI [18]

Table 6. Examine the zero-shot transferring performance of each labeled training set (left) to six unseen datasets (top). Better performance: AbsRel ↓ , δ1 ↑. We highlight the best, second, and third best results for each test dataset in bold, underline, and italic, respectively.

Method

Method

Table 7. Transferring our MDE pre-trained encoder to Cityscapes for semantic segmentation. We do not use Mapillary [1] for pretraining. s.s./m.s.: single-/multi-scale evaluation.

Table 8. Transferring our MDE encoder to ADE20K for semantic segmentation. We use Mask2Former as our segmentation model.

since the labeled images are already sufficient. However, with strong perturbations (S) applied to unlabeled images during re-training, the student model is challenged to seek additional visual knowledge and learn more robust representations. Consequently, the large-scale unlabeled images enhance the model generalization ability significantly. Moreover, with our used semantic constraint Lf eat , the power of unlabeled images can be further amplified for the depth estimation task. More importantly, as emphasized in Section 4.4, this auxiliary constraint also enables our trained encoder to serve as a key component in a multi-task visual system for both middle-level and high-level perception.

monocular depth estimation system. Among the six training datasets, HRWSI [68] fuels our model with the strongest generalization ability, even though it only contains 20K images. This indicates the data diversity counts a lot, which is well aligned with our motivation to utilize unlabeled images. Some labeled datasets may not perform very well, e.g., MegaDepth [33], however, it has its own preferences that are not reflected in these six test datasets. For example, we find models trained with MegaDepth data are specialized at estimating the distance of ultra-remote buildings (Figure 1), which will be very beneficial for aerial vehicles. Effectiveness of 1) challenging the student model when learning unlabeled images, and 2) semantic constraint. As shown in Table 9, simply adding unlabeled images with pseudo labels does not necessarily bring gains to our model,

Comparison with MiDaS trained encoder in downstream tasks. Our Depth Anything model has exhibited stronger zero-shot capability than MiDaS [5, 46]. Here, we further 7

Figure 4. We compare our depth prediction with MiDaS. Meantime, we use ControlNet to synthesize new images from the depth map.

Table 9. Ablation studies of: 1) challenging the student with strong perturbations (S) when learning unlabeled images, and 2) semantic constraint (Lf eat ). Limited by space, we only report the AbsRel (↓) metric, and shorten the dataset name with its first two letters.

Table 11. Comparison between the original DINOv2 and our produced encoder in terms of downstream fine-tuning performance.

4.6. Qualitative Results Method MiDaS Ours

We visualize our model predictions on the six unseen datasets in Figure 3. Our model is robust to test images from various domains. In addition, we compare our model with MiDaS in Figure 4. We also attempt to synthesis new images conditioned on the predicted depth maps with ControlNet [85]. Our model produces more accurate depth estimation than MiDaS, as well as better synthesis results. For more accurate synthesis, we re-trained a better depth-conditioned ControlNet based on our Depth Anything, aiming to provide better control signals for image synthesis and video editing. Please refer to our project page for more qualitative results on video editing [35] with our Depth Anything.

Table 10. Comparison between our trained encoder and MiDaS [5] trained encoder in terms of downstream fine-tuning performance. Better performance: AbsRel ↓ , δ1 ↑ , mIoU ↑ .

compare our trained encoder with MiDaS v3.1 [5] trained encoder in terms of the downstream fine-tuning performance. As demonstrated in Table 10, on both the downstream depth estimation task and semantic segmentation task, our produced encoder outperforms the MiDaS encoder remarkably, e.g., 0.951 vs. 0.984 in the δ1 metric on NYUv2, and 52.4 vs. 59.4 in the mIoU metric on ADE20K.

5. Conclusion In this work, we present Depth Anything, a highly practical solution to robust monocular depth estimation. Different from prior arts, we especially highlight the value of cheap and diverse unlabeled images. We design two simple yet highly effective strategies to fully exploit their value: 1) posing a more challenging optimization target when learning unlabeled images, and 2) preserving rich semantic priors from pre-trained models. As a result, our Depth Anything model exhibits excellent zero-shot depth estimation ability, and also serves as a promising initialization for downstream metric depth estimation and semantic segmentation tasks.

Comparison with DINOv2 in downstream tasks. We have demonstrated the superiority of our trained encoder when fine-tuned to downstream tasks. Since our finally produced encoder (from large-scale MDE training) is finetuned from DINOv2 [43], we compare our encoder with the original DINOv2 encoder in Table 11. It can be observed that our encoder performs better than the original DINOv2 encoder in both the downstream metric depth estimation task and semantic segmentation task. Although the DINOv2 weight has provided a very strong initialization, our largescale and high-quality MDE training can further enhance it impressively in downstream transferring performance.

Acknowledgement. This work is supported by the National Natural Science Foundation of China (No. 62201484), HKU Startup Fund, and HKU Seed Fund for Basic Research. 8

We resize the shorter side of all images to 518 and keep the original aspect ratio. All images are cropped to 518×518 during training. During inference, we do not crop images and only ensure both sides are multipliers of 14, since the pre-defined patch size of DINOv2 encoders [43] is 14. Evaluation is performed at the original resolution by interpolating the prediction. Following MiDaS [5, 46], in zero-shot evaluation, the scale and shift of our prediction are manually aligned with the ground truth. When fine-tuning our pre-trained encoder to metric depth estimation, we adopt the ZoeDepth codebase [4]. We merely replace the original MiDaS-based encoder with our stronger Depth Anything encoder, with a few hyper-parameters modified. Concretely, the training resolution is 392×518 on NYUv2 [55] and 384×768 on KITTI [18] to match the patch size of our encoder. The encoder learning rate is set as 1/50 of the learning rate of the randomly initialized decoder, which is much smaller than the 1/10 adopted for MiDaS encoder, due to our strong initialization. The batch size is 16 and the model is trained for 5 epochs. When fine-tuning our pre-trained encoder to semantic segmentation, we use the MMSegmentation codebase [14]. The training resolution is set as 896×896 on both ADE20K [89] and Cityscapes [15]. The encoder learning rate is set as 3e-6 and the decoder learning rate is 10× larger. We use Mask2Former [12] as our semantic segmentation model. The model is trained for 160K iterations on ADE20K and 80K iterations on Cityscapes both with batch size 16, without any COCO [36] or Mapillary [1] pre-training. Other training configurations are the same as the original codebase.

Table 12. Ablation studies on different values of the tolerance margin α for the feature alignment loss Lf eat . Limited by space, we only report the AbsRel (↓) metric here. Lf eat

because the labeled data has relatively higher-quality depth annotations. The involvement of semantic loss may interfere with the learning of these informative manual labels. In comparison, our pseudo labels are noisier and less informative. Therefore, introducing the auxiliary constraint to unlabeled data can combat the noise in pseudo depth labels, as well as arm our model with semantic capability.

8. Limitations and Future Works Currently, the largest model size is only constrained to ViTLarge [16]. Therefore, in the future, we plan to further scale up the model size from ViT-Large to ViT-Giant, which is also well pre-trained by DINOv2 [43]. We can train a more powerful teacher model with the larger model, producing more accurate pseudo labels for smaller models to learn, e.g., ViT-L and ViT-B. Furthermore, to facilitate real-world applications, we believe the widely adopted 512×512 training resolution is not enough. We plan to re-train our model on a larger resolution of 700+ or even 1000+.

7. More Ablation Studies All ablation studies here are conducted on the ViT-S model. The necessity of tolerance margin for feature alignment. As shown in Table 12, the gap between the tolerance margin of 1.00 and 0.85 or 0.70 clearly demonstrates the necessity of this design (mean AbsRel: 0.188 vs. 0.175).

9. More Qualitative Results

Applying feature alignment to labeled data. Previously, we enforce the feature alignment loss Lf eat on unlabeled data. Indeed, it is technically feasible to also apply this constraint to labeled data. In Table 13, apart from applying Lf eat on unlabeled data, we explore to apply it to labeled data. We find that adding this auxiliary optimization target to labeled data is not beneficial to our baseline that does not involve any feature alignment (their mean AbsRel values are almost the same: 0.180 vs. 0.179). We conjecture that this is

Figure 5. Qualitative results on KITTI. Due to the extremely sparse ground truth which is hard to visualize, we here compare our prediction with the most advanced MiDaS v3.1 [5] prediction. The brighter color denotes the closer distance.

Figure 6. Qualitative results on NYUv2. It is worth noting that MiDaS [5] uses NYUv2 training data (not zero-shot), while we do not.
