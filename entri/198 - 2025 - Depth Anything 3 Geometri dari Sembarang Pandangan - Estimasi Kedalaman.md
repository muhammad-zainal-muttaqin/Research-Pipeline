# 198 - Depth Anything 3: Recovering the Visual Space from Any Views

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2025depthanything3` |
| Judul asli | Depth Anything 3: Recovering the Visual Space from Any Views |
| Penulis | Haotong Lin, Sili Chen, Jun Hao Liew, Donny Y. Chen, Zhenyu Li, Guang Shi, Jiashi Feng, Bingyi Kang (ByteDance Seed) |
| Tahun | 2025 |
| Venue | arXiv preprint arXiv:2511.10647 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2511.10647
- **Versi HTML naskah:** https://arxiv.org/html/2511.10647v1
- **Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views&sort=relevance

## Gambaran Umum

Depth Anything 3 (DA3) memperluas keluarga Depth Anything dari estimasi kedalaman satu citra menjadi model geometri untuk **sembarang jumlah citra masukan**: satu foto, beberapa foto dari sudut berbeda, atau bingkai-bingkai video — dengan atau tanpa posisi kamera yang diketahui. Dari masukan itu model menghasilkan geometri 3D yang konsisten antarcitra, sehingga kedalaman dari semua pandangan dapat dilebur menjadi satu awan titik 3D yang utuh.

Kontribusi konseptualnya adalah **penyederhanaan ekstrem** pada dua sisi. Pertama, arsitektur: alih-alih merancang jaringan khusus multi-pandangan seperti pendahulunya (VGGT), DA3 memakai satu transformer polos — encoder DINOv2 standar — tanpa satu pun modifikasi struktural; satu-satunya penyesuaian adalah cara token ditata saat *forward pass*. Kedua, target pelatihan: alih-alih dilatih multi-tugas dengan banyak keluaran (kedalaman, pose, peta titik, pelacakan), DA3 hanya memprediksi dua peta per citra — peta kedalaman dan peta sinar (*depth-ray*) — yang ternyata cukup untuk menurunkan semua besaran lain, termasuk pose kamera.

Hasilnya: SOTA pada 18 dari 20 konfigurasi tolok ukur geometri visual baru yang dibangun penulis, melampaui VGGT dengan margin rata-rata 44,3% pada akurasi pose kamera dan 25,1% pada akurasi geometri (menurut abstrak versi terbaru), sekaligus mengungguli Depth Anything 2 pada kedalaman monokular.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular (bab 071, 175) menghasilkan peta kedalaman yang tampak meyakinkan per citra, tetapi tidak menjamin **konsistensi lintas pandangan**: dua foto dari sudut berbeda bisa memperoleh kedalaman yang saling bertentangan pada titik 3D yang sama. Padahal robotika, pemetaan, dan realitas tertambah justru menuntut konsistensi itu.

Cara klasik mengatasinya adalah *Structure from Motion* (SfM) dan *Multi-View Stereo* (MVS): deteksi titik kunci, pencocokan antarcitra, estimasi pose, *bundle adjustment*, lalu stereo padat. Pipeline modular ini rapuh pada permukaan polos, reflektif, atau perubahan sudut besar. Generasi terpelajar menggantinya dengan satu jaringan: DUSt3R memprediksi peta titik 3D dari pasangan citra, dan VGGT — pemegang SOTA sebelum DA3 — melangkah lebih jauh dengan pelatihan berskala besar. Tetapi keduanya, terutama VGGT, membayar dengan **kompleksitas**: arsitektur multi-tahap yang dirancang khusus, target prediksi yang redundan (pose + peta titik lokal dan global + kedalaman), dan pelatihan multi-tugas dari nol yang tidak dapat memanfaatkan model pralatih berskala besar. Dua pertanyaan yang dijawab DA3: (1) apakah target prediksi bisa direduksi ke himpunan minimal, dan (2) apakah satu transformer polos sudah cukup.

## Ide Utama

Jawaban DA3 atas kedua pertanyaan itu adalah "ya". Transformernya boleh polos asalkan token lintas pandangan dapat bertukar informasi — dan itu bisa dicapai hanya dengan **menata ulang token** pada sebagian lapis, tanpa mengubah arsitektur. Target prediksinya boleh tunggal asalkan bentuknya tepat — dan bentuk yang tepat adalah **sinar kamera per piksel**: bila untuk setiap piksel diketahui dari titik mana sinar itu berangkat, ke arah mana, dan seberapa jauh ia mengenai permukaan, maka posisi kamera dan struktur 3D seluruhnya sudah ditentukan. Tidak perlu kepala pose, kepala peta titik, atau kepala pelacakan terpisah.

## Cara Kerja Langkah demi Langkah

### Apa yang Disederhanakan

Perbandingan berikut merangkum apa yang dikurangi DA3 dari desain ala VGGT:

```
Desain khusus multi-tugas (mis. VGGT)        Depth Anything 3
─────────────────────────────────────        ─────────────────
N citra                                      N citra (+pose, opsional)
  │                                            │
  ▼                                            ▼
transformer khusus multi-tahap:              SATU transformer polos (DINOv2),
blok atensi bergantian yang                  tanpa modifikasi arsitektur;
dirancang khusus + redundansi                hanya penataan ulang token:
  │                                            lapis awal  : atensi dalam-citra
  ▼                                            lapis akhir : atensi silang/dalam
banyak kepala prediksi:                        │      (bergantian, rasio 1:2)
 ├─ kepala pose                                ▼
 ├─ kepala kedalaman                         Dual-DPT head (reassembly berbagi,
 ├─ kepala peta titik (lokal+global)          ├─ cabang fusi depth -> peta kedalaman
 └─ kepala pelacakan                          └─ cabang fusi ray   -> peta sinar
  │                                            │
  ▼                                            ▼
banyak loss multi-tugas yang                 P = t + D(u,v)·d  →  titik 3D, pose,
harus ditimbang satu per satu                dan awan titik diturunkan dari
                                             dua peta ini saja
```

Yang dikurangi: blok-blok atensi khusus, kepala-kepala prediksi tambahan, dan penimbangan banyak loss multi-tugas. Yang dipertahankan justru aset paling berharga: bobot pralatih DINOv2 berskala besar, sehingga DA3 mewarisi kemampuan ekstraksi fiturnya secara penuh — sesuatu yang hilang bila arsitektur dilatih dari nol.

### Masukan dan Token Kamera

Model menerima N citra (N = 1 berarti monokular biasa). Setiap citra dibagi menjadi *patch* dan diubah menjadi token oleh encoder DINOv2. Di depan token-token setiap citra ditambahkan satu **token kamera**: bila parameter kamera (intrinsik K, rotasi, translasi) diketahui, token itu diisi hasil lewat satu MLP kecil; bila tidak, dipakai token bersama yang dipelajari. Token kamera ikut dalam semua operasi atensi, sehingga informasi pose — bila ada — menyebar ke seluruh fitur. Karena pose bersifat opsional, satu model yang sama melayani masukan berpose maupun tanpa pose.

### Atensi Silang Adaptif-Masukan

L lapis transformer dibagi dua kelompok dengan rasio 2:1. Pada Ls lapis pertama, atensi bekerja **di dalam masing-masing citra** (token satu foto hanya beratensi dengan token foto itu sendiri). Pada Lg lapis terakhir, atensi **bergantian** antara dalam-citra dan lintas-citra — dan di sinilah satu-satunya "penyesuaian" terjadi: token-token dari semua citra ditata ulang (*rearranged*) sehingga operasi atensi standar transformer sekaligus menjangkau pandangan lain. Tidak ada modul baru; yang berubah hanyalah susunan data yang masuk operasi yang sudah ada. Desain ini adaptif terhadap masukan: dengan satu citra, model secara alami merosot menjadi estimator kedalaman monokular tanpa biaya tambahan.

### Representasi Depth-Ray

Ini kunci mengapa satu target cukup. Untuk setiap piksel p = (u, v), kamera memandang dunia melalui sebuah **sinar** yang dinyatakan enam angka: titik asal t (posisi pusat kamera di dunia, 3 angka) dan arah d (3 angka). Secara geometri, arah itu adalah d = R·K⁻¹·p: piksel diproyeksikan-balik ke ruang kamera lalu diputar ke ruang dunia. Model memprediksi, untuk setiap citra, **peta kedalaman** D (satu nilai per piksel) dan **peta sinar** M (enam nilai per piksel). Titik 3D dunia yang dilihat piksel itu kemudian diperoleh dengan satu perkalian dan satu penjumlahan:

```
                     kamera (pusat t)
                        \
                         \   sinar: arah d = R·K⁻¹·p
                          \
   piksel p=(u,v) ────────●────────────────●  P = t + D(u,v) · d
   pada citra             ^                ^
                          sinar kamera     titik 3D di dunia,
                                           jaraknya = kedalaman D(u,v)
```

Mengapa tidak langsung memprediksi pose (matriks rotasi R)? Karena matriks rotasi memiliki kendala ortogonalitas yang sulit dipelajari jaringan secara stabil. Sinar per piksel menyandikan pose yang sama **secara implisit** tanpa kendala itu; bila pose eksplisit diperlukan, ia dapat diturunkan dari peta sinar melalui perhitungan homografi (algoritme DLT dilanjutkan dekomposisi RQ untuk memisahkan K dan R). Untuk kepraktisan, DA3 juga menyediakan **kepala kamera ringan** yang memprediksi FOV, rotasi (kuaternion), dan translasi langsung dari token kamera — biayanya diabaikan karena hanya mengolah satu token per citra. Eksperimen ablation makalah (Tabel 6) menunjukkan target depth-ray ini bukan hanya minimal, tetapi juga **mengungguli** alternatifnya: peta titik saja (ala DUSt3R) tidak menjamin konsistensi, sedangkan target redundan (ala VGGT) justru menimbulkan keterkaitan antar-keluaran yang menurunkan akurasi pose.

### Dual-DPT Head

Kedua peta diproduksi oleh satu kepala prediksi bernama Dual-DPT. Fitur dari backbone mula-mula melewati modul *reassembly* **yang dipakai bersama**, lalu bercabang ke dua set lapis fusi yang berbeda — satu untuk kedalaman, satu untuk sinar — dan ditutup dua lapis keluaran. Berbagi pemrosesan awal membuat kedua tugas saling menguatkan (kedalaman dan sinar adalah dua sisi dari geometri yang sama), sementara pemisahan di ujung mencegah representasi yang redundan.

### Pelatihan Guru–Murid

Data nyata berlabel kedalaman sering kali jarang atau bising (penuh lubang dan derau). Karena itu DA3 memakai paradigma guru–murid: sebuah model **guru** — estimator kedalaman monokular yang juga hanya berupa DINOv2 + decoder DPT — dilatih khusus pada ±20 dataset **sintetik** (yang labelnya sempurna) hingga menghasilkan kedalaman berkualitas tinggi. Untuk setiap citra nyata, kedalaman relatif dari guru diselaraskan ke pengukuran asli yang jarang/bising melalui estimasi skala-geser RANSAC, sehingga diperoleh label yang padat, halus, tetapi tetap setia secara geometris. DA3 (murid) dilatih pada campuran label asli dan label guru ini — supervisi beralih ke label guru setelah langkah ke-120 ribu dari total 200 ribu langkah pada 128 GPU H100. Guru yang sama juga dipakai melatih varian monokular (mengungguli Depth Anything 2) dan varian kedalaman metrik (mengikuti kerangka ruang kanonik Metric3Dv2).

## Eksperimen dan Hasil

Penulis membangun tolok ukur geometri visual dari lima dataset (HiRoom, ETH3D, DTU, 7Scenes, ScanNet++; total ±89 scene, dari level objek hingga luar ruang) dengan tiga kelompok pengujian: akurasi pose (metrik AUC dari galat rotasi/translasi relatif), akurasi rekonstruksi (F1 atas awan titik hasil leburan TSDF), dan kualitas *rendering* (PSNR/SSIM/LPIPS pada sintesis pandangan baru). Hasil utama:

- **SOTA pada 18 dari 20 konfigurasi pengujian** dalam tolok ukur tersebut.
- Melampaui VGGT dengan margin rata-rata **44,3% akurasi pose** dan **25,1% akurasi geometri** (abstrak versi terbaru; versi v1 melaporkan 35,7% dan 23,6% — lihat Poin untuk Sitasi). Pada tabel pose v1, misalnya, AUC@30 DA3 pada ETH3D dan DTU mengungguli VGGT, Pi3, MapAnything, dan DUSt3R/Fast3R dengan jarak lebar.
- Pada tolok ukur monokular standar, varian monokularnya **mengungguli Depth Anything 2** — model guru/basisnya sendiri.
- Sebagai aplikasi hilir, fine-tuning DA3 dengan kepala Gaussian (GS-DPT) untuk sintesis pandangan baru *feed-forward* (FF-NVS) mengungguli model khusus tugas itu (mis. DepthSplat), dan makin baik geometri DA3, makin baik pula hasil NVS — bukti bahwa geometri adalah fondasi tugas-tugas 3D lain.

Interpretasinya: margin diperoleh bukan dari arsitektur yang lebih besar (parameter DA3 justru lebih ramping dari VGGT 1,19B), melainkan dari pemilihan target yang tepat dan pemanfaatan penuh pralatih DINOv2 — persis tesis "pemodelan minimal" yang diusung makalah.

## Kelebihan dan Keterbatasan

Kelebihan: (1) satu model untuk spektrum penuh masukan — monokular, multi-pandangan, video, berpose/tanpa pose; (2) arsitektur sederhana yang mewarisi skala pralatih DINOv2 dan mudah direproduksi konsepnya; (3) target depth-ray yang minimal terbukti mengungguli target yang lebih kaya; (4) fondasi kuat untuk tugas hilir (NVS, varian metrik); (5) seluruh pelatihan memakai dataset akademik publik.

Keterbatasan: (1) biaya pelatihan sangat besar (128 GPU H100, 200 ribu langkah) — reproduksi penuh di luar jangkauan kebanyakan laboratorium; (2) tolok ukur baru dibangun oleh tim yang sama, sehingga validasi independen masih diperlukan; (3) inferensi multi-pandangan pada transformer tetap mahal seiring bertambahnya jumlah citra (pelatihan memakai 2–18 pandangan); (4) karya akhir 2025 — angka dan protokolnya belum lama terbuka untuk pemeriksaan komunitas.

## Kaitan dengan Bab Lain

Bab ini puncak sementara garis kedalaman dalam tinjauan: berawal dari estimasi per-citra (bab 062–068), dimantapkan Depth Anything (bab 071) dan Depth Anything V2 (bab 175) — yang menjadi basis arsitektur guru sekaligus pembanding langsung. Varian metriknya mengikuti kerangka kanonik Metric3Dv2, sejalan dengan bab 177 (Metric3D). Pergeserannya dari "kedalaman per citra" ke "geometri konsisten lintas pandangan" melayani kebutuhan klaster Deteksi 3D (bab 087–098) dan RGB-D SLAM (bab 107–111), dan paling enak dibaca berdampingan dengan survei kedalaman metrik (bab 199) serta varian *real-time* AsyncMDE (bab 200).

## Poin untuk Sitasi

Kutip dengan kunci `lin2025depthanything3`. Ringkasan yang aman dikutip: "Depth Anything 3 menunjukkan satu transformer polos (DINOv2) dengan target prediksi depth-ray tunggal cukup untuk memulihkan geometri konsisten dari sembarang jumlah pandangan, dengan atau tanpa pose kamera, melampaui VGGT pada seluruh tugas tolok ukur geometri visual." **Catatan versi:** abstrak arXiv terbaru melaporkan margin 44,3% (pose) dan 25,1% (geometri), sedangkan teks v1 melaporkan 35,7% dan 23,6% — angka berubah antarversi, maka kutiplah angka sesuai versi yang dirujuk dan sebutkan versinya. Rincian arsitektur pada bab ini (rasio lapis 2:1, Dual-DPT, token kamera, pelatihan guru–murid) diambil dari teks lengkap v1; verifikasi ke naskah sebelum penggunaan formal.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract We present Depth Anything 3 (DA3), a model that predicts spatially consistent geometry from an arbitrary number of visual inputs, with or without known camera poses. In pursuit of minimal modeling, DA3 yields two key insights: a single plain transformer (e.g., vanilla DINO encoder) is sufficient as a backbone without architectural specialization, and a singular depth-ray prediction target obviates the need for complex multi-task learning. Through our teacher-student training paradigm, the model achieves a level of detail and generalization on par with Depth Anything 2 (DA2 ). We establish a new visual geometry benchmark covering camera pose estimation, any-view geometry and visual rendering. On this benchmark, DA3 sets a new state-of-the-art across all tasks, surpassing prior SOTA VGGT by an average of 35.7% in camera pose accuracy and 23.6% in geometric accuracy. Moreover, it outperforms DA2 in monocular depth estimation. All models are trained exclusively on public academic datasets. Correspondence: Bingyi Kang Project Page: depth-anything-3.github.io

1 “Depth Anything 3” marks a new generation for the series, expanding from monocular to any-view inputs, built on our conviction that depth is the cornerstone of understanding the physical world.

Mono. Depth Accuracy Figure 1 Given any number of images and optional camera poses, Depth Anything 3 reconstructs the visual space, producing consistent depth and ray maps that can be fused into accurate point clouds, resulting in high-fidelity 3D Gaussians and geometry. It significantlyoutperforms VGGT in multi-view geometry and pose accuracy; with monocular inputs, it also surpasses Depth Anything 2 while matching its detail and robustness.

Introduction

The ability to perceive and understand 3D spatial information from visual input is a cornerstone of human spatial intelligence [4] and a critical requirement for applications like robotics and mixed reality. This fundamental capability has inspired a wide array of 3D vision tasks, including Monocular Depth Estimation [23], Structure from Motion [80], Multi-View Stereo [73] and Simultaneous Localization and Mapping [58]. Despite the strong conceptual overlap between these tasks—often differing by only a single factor, such as the number of input views—the prevailing paradigm has been to develop highly specialized models for each one. While recent efforts [91, 97] have explored unified models to address multiple tasks simultaneously, they typically suffer from key limitations: they often rely on complex, bespoke architectures, are trained via joint optimization over tasks from scratch, and consequently cannot effectively leverage large-scale pretrained models. In this work, we step back from established 3D task definitions and return to a more fundamental goal inspired by human spatial intelligence: recovering 3D structure from arbitrary visual inputs, be it a single image, multiple views of a scene, or a video stream. Forsaking intricate architectural engineering, we pursue a minimal modeling strategy guided by two central questions. First, is there a minimal set of prediction targets, or is joint modeling across numerous 3D tasks necessary? Second, can a single plain transformer 3

suffice for this objective? Our work provides an affirmative answer to both. We present Depth Anything 3, a single transformer model trained exclusively for joint any-view depth and pose estimation via a specially chosen ray representation. We demonstrate that this minimal approach is sufficient to reconstruct the visual space from any number of images, with or without known camera poses. Depth Anything 3 formulates the above geometric reconstruction target as a dense prediction task. For a

given set of N input images, the model is trained to output N corresponding depth maps and ray maps, each pixel-aligned with its respective input. The architecture to achieve this begins with a standard pretrained vision transformer (e.g., Oquab et al. 61), as its backbone, leveraging its powerful feature extraction capabilities. To handle arbitrary view counts, we introduce a key modification: an input-adaptive cross-view self-attention mechanism. This module dynamically rearranges tokens during the forward pass in selected layers, enabling efficient information exchange across all views. For the final prediction, we propose a new dual DPT head designed to jointly outputs both depth and ray values, by processing the same set of features with distinct fusion parameters. To enhance flexibility, the model can optionally incorporate known camera poses via a simple camera encoder, allowing it to adapt to various practical settings. This overall design results in a clean and scalable architecture that directly inherits the scaling properties of its pretrained backbone. We train Depth Anything 3 via a teacher-student paradigm to unify diverse training data, which is necessary for a generalist model. Our data sources include varied formats like real-world depth camera captures (e.g., Baruch et al. 5), 3D reconstruction (e.g., Reizenstein et al. 68), and synthetic data, where real-world depth may be of poor quality (Fig. 4). To resolve this, we adopt a pseudo-labeling strategy inspired by prior works [112, 113]. Specifically, we train a powerful teacher monocular depth model on synthetic data to generate dense, high-quality pseudo-depth for all real-world data. Crucially, to preserve geometric integrity, we align these dense pseudo-depth maps with the original sparse or noisy depth. This approach proved remarkably effective, significantly enhancing label detail and completeness without sacrificing the geometric accuracy. To better evaluate our model and track progress in the field, we establish a comprehensive benchmark for assessing geometry and pose accuracy. The benchmark comprises 5 distinct datasets, totaling over 89 scenes, ranging from object-level to indoor and outdoor environments. By directly evaluating pose accuracy across scenes and fusing the predicted pose and depth into a 3D point cloud for accuracy assessment, the benchmark faithfully measures the pose and depth accuracy of visual geometry estimators. Experiments show that our model achieves state-of-the-art performance on 18 out of 20 settings. Moreover, on standard monocular benchmarks, our model outperforms Depth Anything 2 [113]. To further demonstrate the fundamental capability of Depth Anything 3 in advancing other 3D vision tasks, we introduce a challenging benchmark for feed-forward novel view synthesis (FF-NVS), comprising over 160 scenes. We adhere to the minimal modeling strategy and fine-tune our model with an additional DPT head to predict pixel-aligned 3D Gaussian parameters. Extensive experiments yield two key findings: 1) fine-tuning a geometry foundation model for NVS substantially outperforms highly specialized task-specific models [108]; 2) enhanced geometric reconstruction capability directly correlates with improved FF-NVS performance, establishing Depth Anything 3 as the optimal backbone for this task.

Related Work

Traditional systems [70, 71] decompose reconstruction into feature detection and matching, robust relative pose estimation, incremental or global SfM with bundle adjustment, and dense multi-view stereo for per-view depth and fused point clouds. These methods remain strong on well-textured scenes, but their modularity and brittle correspondences complicate robustness under low texture, specularities, or large viewpoint changes. Early learning methods injected robustness at the component level: learned detectors [20], descriptors for matching [22], and differentiable optimization layers that expose pose/depth updates to gradient flow [31, 33, 62]. On the dense side, cost-volume networks [106, 114] for MVS replaced hand-crafted regularization with 3D CNNs, improving depth accuracy especially at large baselines and thin structures compared with classical PatchMatch. Early end-to-end approaches [86, 90] moved beyond modular SfM/MVS pipelines by directly regressing camera poses and per-image depths from pairs of images.

Figure 2 Pipeline of Depth Anything 3. Depth Anything 3 employs a single transformer (vanilla DINOv2 model) without any architectural modifications. To enable cross-view reasoning, an input-adaptive cross-view self-attention mechanism is introduced. A dual-DPT head is used to predict depth and ray maps from visual tokens. Camera parameters, if available, are encoded as camera tokens and concatenated with patch tokens, participating in all attention operations.

These approaches reduced engineering complexity and demonstrated the feasibility of learned joint depth pose estimation, but they often struggled with scalability, generalization, and handling arbitrary input cardinalities. A turning point came with DUSt3R [96], which leveraged transformers to directly predict point map between two views and compute both depth and relative pose in a purely feed-forward manner. This work laid the foundation for subsequent transformer-based methods aiming to unify multi-view geometry estimation at scale. Follow-up models extended this paradigm with multi-view inputs [10, 85, 94, 110], video input [19, 59, 94, 121], robust correspondence modeling [48], camera parameter injection [39, 43], large-scale SfM [18], SLAM applications [54], and view synthesis with 3D Gaussians [11, 13, 41, 79, 108, 122]. Among these, [91] push accuracy to a new level through large-scale training, a multi-stage architecture, and redundancy in design. In contrast, we focus on a minimal modeling strategy built around a single, simple transformer. Monocular depth estimation.

Early monocular depth estimation methods relied on fully supervised learning on single-domain datasets, which often produced models specialized to either indoor rooms [75] or outdoor driving scenes [26]. These early deep models achieved good accuracy within their training domain but struggled to generalize to novel environments, highlighting the challenge of cross-domain depth prediction. Modern generalist approaches [6, 42, 95, 112, 113, 118] exemplify this trend by leveraging massive multi-dataset training and advanced architectures like vision transformers [67] or DiT [64]. Trained on millions of images, they learn broad visual cues and incorporate techniques such as affine-invariant depth normalization. In contrast, our method is primarily designed for a unified visual geometry estimation task, yet it still demonstrates competitive monocular depth performance. Feed-Forward Novel View Synthesis Novel view synthesis (NVS) has long been a core problem in computer vision and graphics [8, 34, 49], and interest has increased with the rise of neural rendering [28, 44, 57, 77, 78]. A particularly promising direction is feed-forward NVS, which produces 3D representations in a single pass through an image-to-3D network, avoiding tedious per-scene optimization. Early methods adopted NeRF as the underlying 3D representation [12, 14, 35, 52, 107, 119], but recent work has largely shifted to 3DGS due to its explicit structure and real-time rendering. Representative approaches improve image-to-3D networks with geometry priors, e.g., epipolar attention [11], cost volumes [13], and depth priors [107]. More recently, multi-view geometry foundation models [85, 91, 96, 110] have been integrated to improve modeling capacity, particularly in pose-free settings, yet methods built upon such models are often evaluated by relying on a single chosen foundation model [41, 79, 116]. Here, we systematically benchmark the contribution of different geometry foundation models to NVS and propose strategies to better exploit them, enabling feed-forward 3DGS to handle both posed and pose-free inputs, variable numbers of views, and arbitrary resolutions.

We tackle the recovery of consistent 3D geometry from diverse visual inputs—single image, multi-view collections, or videos—and optionally incorporate known camera poses when available.

through which the underlying 3D visual space can be faithfully recovered. Depth-ray representation.

Predicting a valid rotation matrix Ri is challenging due to the orthogonality constraint. To avoid this, we represent camera pose implicitly with a per-pixel ray map, aligned with the input image and depth map. For each pixel p, the camera ray r ∈ R6 is defined by its origin t ∈ R3 and direction d ∈ R3 : r = (t, d). The direction is obtained by backprojecting p into the camera frame and rotating it to the world frame: d = RK−1 p. The dense ray map M ∈ RH×W ×6 stores these parameters for all pixels. We do not normalize d, so its magnitude preserves the projection scale. Thus, a 3D point in world coordinates is simply P = t + D(u, v) · d. This formulation enables consistent point cloud generation by combining predicted depth and ray maps through element-wise operations. Given an input image I ∈ RH×W ×3 , the corresponding ray map is denoted by M ∈ R . This map comprises per-pixel ray origins, stored in the first three channels (M(:, :, : 3)), and ray directions, stored in the last three (M(:, :, 3 :)). Deriving Camera Parameters from the Ray Map. H×W ×6

This is a standard least-squares problem that can be efficiently solved using the Direct Linear Transform (DLT) algorithm [2]. Once the optimal homography H∗ is found, we recover the camera parameters. Since the intrinsic matrix K is upper-triangular and the rotation matrix R is orthonormal, we can uniquely decompose H∗ using RQ decomposition to obtain K, R. Minimal prediction targets.

Recent works aim to build unified models for diverse 3D tasks, often using multitask learning with different targets—for example, point maps alone [96], or redundant combinations of pose, local/global point maps, and depth [91, 94, 110]. While point maps are insufficient to ensure consistency, redundant targets can improve pose accuracy but often introduce entanglement that compromises it. In 6

contrast, our experiments (Tab. 6) show that a depth-ray representation forms a minimal yet sufficient target set for capturing both scene structure and camera motion, outperforming alternatives like point maps or more complex outputs. However, recovering camera pose from the ray map at inference is computationally costly. We address this by adding a lightweight camera head, DC . This transformer operates on camera tokens to predict the field of view (f ∈ R2 ), rotation as a quaternion (q ∈ R4 ), and translation (t ∈ R3 ). Since it processes only one token per view, the added cost is negligible.

Architecture

We now detail the architecture of Depth Anything 3, which is illustrated in Fig. 2. The network is composed of three main components: a single transformer model as the backbone, an optional camera encoder for pose conditioning, and a Dual-DPT head for generating predictions. Single transformer backbone. We use a Vision Transformer with L blocks, pretrained on large-scale monocular

image corpora (e.g., DINOv2 [61]). Cross-view reasoning is enabled without architectural changes via an input-adaptive self-attention, implemented by rearranging input tokens. We divide the transformer into two groups of sizes Ls and Lg . The first Ls layers apply self-attention within each image, while the subsequent Lg layers alternate between cross-view and within-view attention, operating on all tokens jointly through tensor reordering. In practice, we set Ls : Lg = 2 : 1 with L = Ls + Lg . As shown in our ablation study in Tab. 7, this configuration provides the optimal trade-off between performance and efficiency compared to other arrangements. This design is input-adaptive: with a single image, the model naturally reduces to monocular depth estimation without extra cost. Camera condition injection. To seamlessly handle both posed and unposed inputs, we prepend each view with

Dual-DPT head. For the final prediction stage, we propose a novel Dual-DPT head that jointly produces dense depth and ray values. As shown in Tab. 6, this design is both powerful and efficient. Given a set of features from the backbone, the Dual-DPT head first processes them through a shared set of reassembly modules. Subsequently, the processed features are fused using two distinct sets of fusion layers: one for the depth branch and one for the ray branch. Finally, two separate output layers produce the final depth and ray map predictions. This architecture ensures that both branches operate on the same set of processed features, differing only in the final fusion stage. Such a design encourages strong interaction between the two prediction tasks, while avoiding redundant intermediate representations.

Teacher-student learning paradigm. Our training data comes from diverse sources, including real-world

depth captures, 3D reconstructions, and synthetic datasets. Real-world depth is often noisy and incomplete (Fig. 4), limiting its supervisory value. To mitigate this, we train a monocular relative depth estimation “teacher” model solely on synthetic data to generate high-quality pseudo-labels. These pseudo-depth maps are aligned with the original sparse or noisy ground truth via RANSAC least squares, enhancing label detail and completeness while preserving geometric accuracy. We term this model Depth-Anything-3-Teacher, trained on

a large synthetic corpus covering indoor, outdoor, object-centric, and diverse in-the-wild scenes to capture fine geometry. We detail our teacher design in the Sec. 4.1. Training objectives.

Following the formulation in Sec. 3.1, our model Fθ maps an input I to a set of outputs comprising a depth map D̂, a ray map R̂, and an optional camera pose ĉ: Fθ : I 7→ {D̂, R̂, ĉ}. The gray color indicates that ĉ is an optional output, included primarily for practical convenience. Prior to loss computation, all ground-truth signals are normalized by a common scale factor. This scale is defined as the mean ℓ2 norm of the valid reprojected point maps P, a step that ensures consistent magnitude across different modalities and stabilizes the training process. The overall training objective is defined as a weighted sum of several terms: L = LD (D̂, D) + LM (R̂, M) + LP (D̂ ⊙ d + t, P) + βLC (ĉ, v) + αLgrad (D̂, D),

where ∇x and ∇y are the horizontal and vertical finite difference operators. This loss preserves sharp edges while ensuring smoothness in planar regions. In practice, we set α = 1 and β = 1.

Implementation Details

We provide our training datasets in Table 1. Note that for datasets with potential overlap between training and testing (ScanNet++), we ensure a strict separation at the scene level, i.e., scenes in training and testing are mutually exclusive. Note that using Scannet++ for training is fair to other methods, as it is widely used for training in [91, 96]. Training details.

As shown in Fig. 4, the real-world datasets are of poor quality, thus we train the teacher model exclusively on synthetic data to provide supervision for real-world data. Our teacher model is trained as a monocular relative depth predictor. During inference or supervision, noisy ground-truth depth can be used to provide scale and shift parameters, allowing for the alignment of the predicted relative depth with absolute depth measurements.

Figure 4 Poor quality real-world datasets. We show some examples of the poor quality real-world datasets.

Table 1 Datasets used in Depth Anything 3 , including number of scenes, data type. Usage

Training objectives. For geometric supervision, in addition to a standard depth-gradient loss, we adopt ROE alignment with the global–local loss introduced in [95]. To further refine local geometry, we introduce a distance-weighted surface-normal loss. For each center pixel, we sample four neighboring points and compute unnormalized normals ni . We then weight these normals by: wi =

where E denotes the angular error between normals. Ground truth is undefined in sky regions and in background areas of object-only datasets. To prevent these regions from degrading the depth prediction and to facilitate downstream use, we jointly predict a sky mask and an object mask aligned with the depth output, supervised with MSE loss. The overall training objective is LT = αLgrad + Lgl + LN + Lsky + Lobj

where α = 0.5. Here, Lgrad , Lgl , Lsky , and Lobj denote the gradient loss, global–local loss, sky-mask loss, and object-mask loss, respectively.

Real-world datasets are crucial for generalizing camera pose estimation, yet they rarely provide clean depths; supervision is often noisy or sparse (Fig. 4). Depth Anything 3 Teacher provides high-quality relative depth, which we align to noisy metric measurements (e.g., COLMAP or active sensors) via a robust ransac scale–shift procedure. Let D̃ denote the teacher’s relative depth and D the available sparse depth with validity mask mp over domain Ω. We estimate scale s and shift t by RANSAC least squares, using an inlier threshold equal to the mean absolute deviation from the residual median: X 2 (ŝ, t̂) = arg min mp s D̃p + t − Dp , DT →M = ŝ D̃ + t̂. (8) s>0, t

The aligned DT →M provides scale-consistent and pose–depth coherent supervision for Depth Anything 3, complementing our joint depth–ray objectives and improving real-world generalization, as evidenced in Fig. 8.

We additionally train a monocular depth model under a teacher–student paradigm. We follow the DA2 framework, training the monocular student on unlabeled images with teacher-generated pseudo-labels. The key difference from DA2 lies in the prediction target: our student predicts depth maps, whereas DA2 predicts disparity. We further supervise the student with the same loss used for the teacher, applied to the pseudo-depth labels. The monocular model also predicts relative depth. Trained solely on unlabeled data with teacher supervision, it achieves state-of-the-art performance on standard monocular depth benchmarks as shown in Tab. 10.

Next, we demonstrate that our teacher model can be used for training a metric depth estimation model with sharp boundaries. Following Metric3Dv2 [37], we apply canonical camera space transformation to address 10

The training largely follows that of the monocular teacher model. All images are trained at a base resolution of 504 with varying aspect ratios (1:1, 1:2, 16:9, 9:16, 3:4, 1:1.5, 1.5:1, 1:1.8). We employ AdamW optimizer and set the learning rate for encoder and decoder to 5e-6 and 5e-5, respectively. We apply random rotation augmentation where training images are rotated at 90 or 270 degree with 5% probability. We set canonical focal length f c to 300. We use the aligned prediction from teacher model as supervision. With a probability of 20%, we use the original ground-truth labels for training. We train with batch size of 64 for 160K iterations. The training objective is a weighted sum of depth loss Ldepth , Lgrad and sky-mask loss Lsky .

Inspired by human spatial intelligence, we believe that consistent depth estimation can greatly enhance downstream 3D vision tasks. We choose feed-forward novel view synthesis (FF-NVS) as the demonstration task, given its growing attention driven by advances in neural 3D representations (i.e., we choose 3DGS) and its relevance to numerous applications. Adhere to the minimal modeling strategy, we perform FF-NVS by fine-tuning with an added DPT head (GS-DPT) to infer pixel-aligned 3D Gaussians [11, 13]. GS-DPT head. Given visual tokens for each view extracted via our single transformer backbone (Sec. 3.2), 3 GS-DPT predicts the camera-space 3D Gaussian parameters {σi , qi , si , ci }H×W i=1 , where σi , qi ∈ H, si ∈ R , 3 ci ∈ R denote the opacity, rotation quaternion, scale, and RGB color of the i-th 3D Gaussian, respectively. Among them, σi is predicted by the confidence head, while others are predicted by the main GS-DPT head. The estimated depth is unprojected to world coordinates to obtain the global positions Pi ∈ R3 of the 3D Gaussians. These primitives are then rasterized to synthesize novel views from given camera poses.

Training objectives. The NVS model is fine-tuned with two training objectives, namely photometric loss (i.e.,

LMSE and LLPIPS ) on rendered novel views and scale-shift-invariant depth loss LD on the estimated depth of observed views, following the teacher–student learning paradigm (Sec. 3.3).

Unlike the above pose-conditioned version intended to benchmark DA3 as a strong feed-forward 3DGS backbone, we also present an alternative better suited to in-the-wild evaluation. This version is designed to integrate seamlessly with DA3 using identical pretrained weights, enabling novel view synthesis with or without camera poses, and across varying resolutions and input view counts. Pose-adaptive formulation. Rather than assuming that all input images are uncalibrated [41, 79, 116, 122], we adopt a pose-adaptive design that accepts both posed and unposed inputs, yielding a flexible framework that works with or without poses. Two design choices are required to achieve this: 1) all 3DGS parameters are predicted in local camera space. 2) the backbone must handle posed and unposed images seamlessly. Our DA3 backbone satisfies both requirements (Sec. 3.2). In particular, when poses are available, we scale (via [87]) and unproject the predicted depth and camera-space 3DGS to world space to align with them. When poses are not available, we directly use the predicted poses for the unprojection to world space.

To reduce the trade-off between accurate surface geometry and rendering quality [29], we predict an additional depth offset in the GS-DPT head. For more in-the-wild robustness, we replace per 3D Gaussian color with spherical harmonic coefficients to reduce conflicts with geometry via modeling view-dependent surface. Enhanced training strategies. To avoid unstable training, we initialize the DA3 backbone from pretrained weights and freeze it when training, tuning only the GS-DPT head. To improve in-the-wild performance, we train with varying image resolutions and varying numbers of context views. Specifically, higher-resolution inputs are paired with fewer context views and lower-resolution inputs with more views, which stabilizes training while supporting diverse evaluation scenarios.

Implementation Details

For training the NVS model, we leverage the large-scale DL3DV dataset [53], which provides diverse real-world scenes with camera poses estimated by COLMAP. We use 10,015 scenes from DL3DV for training the feed-forward 3DGS model. To ensure fair evaluation, we strictly maintain exclusivity between training and testing splits: the 140 DL3DV scenes used for benchmarking are completely disjoint from the training set, preventing any data leakage.

We further introduce a visual geometry benchmark to assess geometry prediction models. It directly evaluates pose accuracy, depth via reconstruction accuracy and visual rendering quality.

For each scene, we select all available images; if the total number exceeds the limit, we randomly sample 100 images using a fixed random seed. The selected images are then processed through a feed-forward model to generate consistent pose and depth estimations, after which the pose accuracy is computed. Geometry estimation. For the same image set, we perform reconstruction using the predicted poses together with the predicted depths. To align the reconstructed point cloud with the ground-truth, we employ evo [87] to align the predicted poses to the ground-truth poses, obtaining a transformation that maps the reconstruction into the ground-truth coordinate system. To improve robustness, we adopt a RANSAC-based alignment procedure. Specifically, we repeatedly apply evo on randomly sampled pose subsets and evaluate each candidate transformation by counting the number of inlier poses, where inliers are defined as those with translation errors below the median of the overall pose deviations. The transformation with the largest inlier set is then chosen and applied to fuse the aligned predicted point cloud with the predicted depth maps by TSDF fusion. Finally, reconstruction quality is assessed by comparing the aligned reconstruction with the ground-truth point cloud using the metrics described in Sec. 6.2. Visual rendering.

For each testing scene, the number of images typically ranges from 300 to 400 across all benchmark datasets. We sample one out of every 8 images as target novel views for evaluation. From the remaining viewpoints, we use COLMAP camera poses provided by each dataset and apply farthest point sampling, considering both camera translation and rotation distances, to select 12 images as input context views. For DL3DV, we use the official Benchmark set for testing. For Tanks and Temples, all Training Data scenes are included except Courthouse. For MegaDepth, we select scenes numbered from 5000 to 5018, as these are most suitable for NVS.

For assessing pose estimation, we follow the evaluation protocol introduced in [89, 91] and report results using the AUC. This metric is derived from two components: Relative Rotation Accuracy (RRA) and Relative Translation Accuracy (RTA). RRA and RTA quantify the angular deviation in rotation and translation, respectively, between two images. Each error is compared against a set of thresholds to obtain

accuracy values. AUC is then computed as the integral of the accuracy–threshold curve, where the curve is determined by the smaller of RRA and RTA at each threshold. To illustrate performance under different tolerance levels, we primarily report results at thresholds of 3 and 30. Reconstrution metrics.

Let G denote the ground-truth point set and R the reconstructed point set under evaluation. We measure accuracy using dist(R → G) and completeness using dist(G → R) following [1]. The Chamfer Distance (CD) is then defined as the average of these two terms. Based on these distances, we define the P precision and recall of the reconstructionPR with respect to adistance threshold d. Precision is given by

artists. We use a threshold d of 0.05m for the F1 reconstruction metric calculation. For TSDF fusion, we set the parameters voxel size to 0.007m. ETH3D provides high-resolution indoor and outdoor images with ground-truth depth from laser sensors. We

aggregate the ground-truth depth maps with TSDF fusion for GT 3D shapes. We select 11 scenes: courtyard, electro, kicker, pipes, relief, delivery area, facade, office, playground, relief 2, terrains, for the benchmark. All frames are used in the evaluation. We use a threshold d of 0.25 for the F1 reconstruction metric calculation. For TSDF fusion, we set the parameters voxel size to 0.039m. DTU is an indoor dataset consisting of 124 different objects, each scene is recorded from 49 views. It provides

ground-truth point clouds collected under well-controlled conditions. We evaluate models on the 22 evaluation scans of the DTU dataset following [114]. We adopt the RMBG 2.0 [126] to remove meaningless background pixels and use the default depth fusion strategy proposed in [124]. All frames are used in the evaluation. 7Scenes is a challenging real-world dataset, consisting of low-resolution images with severe motion blurs for

in-door scenes. We follow the implementation in [130] to fuse RGBD images with TSDF fusion and prepare ground-truth 3D shapes. We downsample the number of frames for each scene by 11 to faciliate evaluation. We use a threshold d of 0.05m for the F1 reconstruction metric calculation. For TSDF fusion, we set the parameters voxel size to 0.007m. ScanNet++ is an extensive indoor dataset providing high-resolution images, depth maps from iPhone LiDAR,

and high-resolution depth maps sampled from reconstructions of laser scans. We select 20 scenes for the benchmark. As depth maps from iPhone LiDAR lack of invalid ground-truth indicators, we use depth maps sampled from reconstructions of laser scans as ground-truth depth by default. We aggregate the ground-truth depth maps with TSDF fusion for GT 3D shapes. We downsample the number of frames for each scene by 5 to faciliate evaluation. We use a threshold d of 0.05m for the F1 reconstruction metric calculation. For TSDF fusion, we set the parameters voxel size to 0.02m. Visual rendering quality.

We evaluate visual rendering quality on diverse large-scale scenes. We introduce a new NVS benchmark built from three datasets, including DL3DV [53] with 140 scenes, Tanks and Temples [45] with 6, and MegaDepth [51] with 19, each spanning around 300 sampled frames. Ground truth camera poses, estimated with COLMAP, are used directly to ensure accurate and fair comparison across diverse models. We report PSNR, SSIM, and LPIPS metrics on rendered novel views using given camera poses.

Table 2 Comparisons with SOTA methods on pose accuracy. We report both Auc3 ↑ and Auc30 ↑ metrics. The top-3 results are highlighted as first , second , and third .

Methods

Figure 5 Comparisons of pose estimation quality. Camera trajectories for two videos are shown. Ground-truth trajectories are derived using COLMAP on images with dynamic objects masked.

Experiments

Baselines. VGGT [91] is an end-to-end transformer that jointly predicts camera parameters, depth, and 3D points from one or many views. Pi3 [99] further adopts a permutation-equivariant design to recover affine-invariant cameras and scale-invariant point maps from unordered images. MapAnything [43] provides a feed-forward framework that can also take camera pose as input for dense geometric prediction. Fast3R [111] extends point-map regression to hundreds or even thousands of images in a single forward pass. Finally, DUSt3R [97] tackles uncalibrated image pairs by regressing point maps and aligning them globally. Our method is similar to VGGT [91], but adopts a new architecture and a different camera representation, and it is orthogonal to Pi3 [99]. Pose estimation.

As shown in Tab. 2 and Fig. 5, comparing against five baselines [43, 91, 96, 99, 110], our DA3-Giant model attains the best performance on nearly all metrics, with the only exception being Auc30 on the DTU dataset. Notably, on Auc3 our model delivers at least an 8% relative improvement over all competing methods, and on ScanNet++ it achieves a 33% relative gain over the second-best model. Geometry estimation.

As shown in Tab. 3, our DA3-Gaint establishes a new SOTA in nearly all scenarios, outperforming all competitors in all five pose-free settings. On average, DA3-Gaint achieves a relative 14

Table 3 Comparisons with SOTA methods on reconstruction accuracy. For all datasets except DTU, we report the F-Score (F1 ↑). For DTU, we report the chamfer distance (CD ↓, unit: mm). w/o p. and w/ p. denote without pose and with pose, indicating whether ground-truth camera poses are provided for reconstruction. The top-3 results are highlighted as first , second , and third .

Methods

improvement of 25.1% over VGGT and 21.5% over Pi3. Fig. 7 and Fig. 6 visualize our predicted depth and recovered point clouds. The results are not only clean, accurate, and complete, but also preserve fine-grained geometric details, clearly demonstrating a superiority over other methods. Even more notably, our much smaller DA3-Large (0.30B parameters) demonstrates remarkable efficiency. Despite being 3× smaller, it surpasses the prior SOTA VGGT (1.19B parameters) in five out of the ten settings, with particularly strong performance on the ETH3D. When camera poses are available, both our method and MapAnything can exploit them for improved results, and other methods also benefit from ground-truth pose fusion. Our model shows clear gains on most datasets except 7Scenes, where the limited video setting already saturates performance and reduces the benefit of pose conditioning. Notably, with pose conditioning, performance gains from scaling model size are smaller than in pose-free models, indicating that pose estimation scales more strongly than depth estimation and requires larger models to fully realize improvements.

Monocular depth accuracy also reflects geometry quality. As shown in Tab. 4, on the standard monocular depth benchmarks reported in [113], our model outperforms VGGT and Depth Anything 2. For reference, we also include the results of our teacher model. Table 4 Monocular depth comparisons. δ1 ↑

Method

To fairly evaluate feed-forward novel view synthesis (FF-NVS), we compare against three recent 3DGS models—pixelSplat [11], MVSplat [13], and DepthSplat [108]—and further test alternative frameworks by replacing our geometry backbone with Fast3R [111], MV-DUSt3R [85], and VGGT [91]. All models are trained on DL3DV-10K training set under a unified protocol and evaluated on our benchmark (Sec. 6.3). As reported in Tab. 5, all models perform substantially better on DL3DV than on the other datasets, suggesting that 3DGS-based NVS is sensitive to trajectory and pose distributions standardized by DL3DV, rather than scene content. Comparing the two groups, geometry-model-based frameworks consistently outperform specialized feed-forward models, demonstrating that a simple backbone plus DPT head can 15

Figure 6 Comparisons of point cloud quality. Our model produces point clouds that are more geometrically regular and substantially less noisy than those generated by other methods.

Figure 7 Comparisons of depth quality. Compared with other methods, our depth maps exhibit finer structural detail and higher semantic correctness across diverse scenes.

surpass complex task-specific designs. The advantage stems from large-scale pretraining, which enables better generalization and scalability than approaches relying on epipolar transformers, cost volumes, or cascaded modules. Within this group, NVS performance correlates with geometry estimation capability, making DA3 the strongest backbone. Looking forward, we expect FF-NVS can be effectively addressed with simple architectures leveraging pretrained geometry backbones, and that the strong spatial understanding of DA3 will benefit other 3D vision tasks.

Analysis for Depth Anything 3

Training our DA3-Giant model requires 128×H100 GPUs for approximately 10 days. To reduce carbon footprint and computational cost, all ablation experiments reported in this section are conducted using the ViT-L backbone with a maximum of 10 views, requiring approximately 4 days on 32×H100 GPUs. 7.2.1

To validate our depth-ray representation, we compare different prediction combinations summarized in Tab. 6. All models use a ViT-L backbone, identical training settings (view size: 10, batch size: 128, steps: 120k). We evaluate four heads: 1) depth for dense depth maps; 2) pcd for direct 3D point clouds; 3) cam for 9-DoF camera pose c = (t, q, f ); and 4) our proposed ray, predicting per-pixel ray maps (Sec. 3.1). The ray head uses a Dual-DPT architecture, while pcd uses a separate DPT head. For models without pcd, point clouds 16

Table 5 Comparisons with SOTA methods on NVS task. We report NVS comparsions with exisiting feed-forward 3DGS models and counterparts using other backbones. For each scene, we use 12 input context views and test on target views sampled every 8 views over a set of over 300 views. Image resolution is 270 × 480.

Table 6 Ablations of prediction-target combinations. Note that all experiments in this table do not have camera condition token. The best and second best are highlighted.

Methods

are obtained by combining depth with camera parameters from ray or cam. As shown in Table 6, the minimal depth + ray configuration consistently outperforms depth + pcd + cam and depth + cam across all datasets and metrics, achieving nearly 100% relative gain in Auc3 over depth + cam. Adding an auxiliary cam head (depth + ray + cam) yields no further benefit, confirming the sufficiency of the depth-ray representation. We adopt depth + ray + cam as our final representation, as the camera head incurs negligible computational overhead, amounting to approximately 0.1% of the computation cost of the main backbone. 7.2.2

We compare a standard ViT-L backbone with a VGGT-style architecture that stacks two distinct transformers, tripling the block count. For fair capacity comparison, the VGGT-style model uses smaller ViT-B backbones, yielding a similar parameter size to our ViT-L. Our backbone supports two attention strategies: Full Alt., which alternates cross-view/within-view attention in all layers (L = Lg ), and our default partial alternation. As shown in Table 7, the VGGT-style model drops to 79.8% of our baseline performance, confirming the superiority of a single-transformer design at similar scale. We attribute this gap to full pretraining of our backbone versus two-thirds untrained blocks in VGGT. Moreover, the Full Alt. variant degrades across nearly all metrics—except F1 on 7Scenes—indicating that partial alternation is the more effective and robust strategy. 7.2.3

Ablation and Analysis

We assess the effectiveness of the dual-DPT head via an ablation in which two separate DPT heads predict depth and ray maps independently. Results are reported in Tab. 7, item (d). Compared with the model equipped with the dual-DPT head, the variant without it shows consistent drops across metrics, confirming the effectiveness of our dual-DPT design.

Table 7 Ablation study. We evaluate three architectural designs with comparable model sizes (a-c), the effects of the dual-DPT head (d), teacher label supervision (e), and the pose conditioning module (f-g). The best and second best are highlighted. Methods marked with "*" are evaluated with ground-truth pose fusion. HiRoom

Methods

Table 8 Comparison of Models with Parameters and Running Speed. The maximum number of images was tested on an 80 GB A100 GPU. If we store some intermediate tokens in CPU memory, we could process many more images. The running speed was measured on an A100 GPU with a scene of 32 images, and we report the average speed per image. The image resolution is 504 × 336.

34.1 FPS

37.6 FPS 78.37 FPS 126.5 FPS 160.5 FPS

We ablate the use of teacher model labels as supervision, with quantitative results reported in Tab. 7, item (e). Training without teacher labels yields a slight improvement on DTU but leads to performance drops on 7Scenes and ScanNet++. Notably, the degradation is pronounced on HiRoom. We attribute this to HiRoom’s synthetic nature and its ground truth containing abundant fine structures; supervision from the teacher helps the student capture such details more accurately. Qualitative comparisons in Fig. 8 corroborate this trend: models trained with teacher-label supervision produce depth maps with substantially richer detail and finer structures. Pose conditioning.

To assess the pose-conditioning module, we ablate it on the ViT-L backbone and report results in Tab. 7, items (f) and (g). Unlike other entries in the table, these two are evaluated with ground-truth pose fusion (marked with “*”), whereas the rest use predicted pose fusion. Across metrics, configurations with pose conditioning consistently outperform those without, confirming the effectiveness of the pose-conditioning module. Running time.

We present analysis on Parameters, max number of images and running speed in Tab. 8

We provide additional visualizations of camera pose and depth estimation on in-the-wild scenes in Fig. 9, demonstrating the robustness and quality of our model across diverse real-world scenarios.

Analysis for Depth-Anything-3-Monocular

Image w/o Teacher w/ Teacher Figure 8 Comparison of teacher-label supervision. Supervision with teacher-generated labels yields depth maps with substantially richer detail and finer structures. Table 9 Ablations for teacher model. Training with V3 datasets and multi-resolution strategy yields the best performance. Depth-based geometry achieves the best AbsRel and SqRel. The full teacher-loss outperforms other variants. (AbsRel: ↓, SqRel: ↓, δ1 : ↑). The results are averaged over KITTI, NYU, ETH3D, SUN-RGBD and DIODE. Data

The teacher model’s metrics are reported in Tab. 4. Our new teacher consistently outperforms DA2 across all datasets, with the sole exception of NYU, where performance is on par with DA2. For the teacher ablation, we employ a ViT-L backbone and a batch size of 64. Evaluation follows the DA2 benchmark protocol, and we additionally report Squared Relative Error (SqRel), defined as the mean squared error between predictions and ground truth normalized by the ground truth. As shown in Tab. 9, across geometries, depth emerges as the most effective target compared with disparity and point maps. For training objectives, the full teacher loss proposed in this work outperforms both the DA2 loss and a variant without proposed normal-loss term. Finally, data scaling contribute notably to performance: upgrading datasets from V2 to V3 and adopting a multi-resolution training strategy yield consistent improvements in the teacher’s final metrics. 7.3.2

As shown in Tab. 10, our monocular student model with a ViT-L backbone outperforms the DA2 student across all evaluation datasets. Notably, on the ETH3D [72] benchmark the new monocular student achieves an improvement of over 10% compared with DA2. The improved performance is attributed to the enhanced teacher model with better geometry supervision and the scaled training data (V3). On challenging datasets like SINTEL, our student also demonstrates substantial gains (+5.1%), validating the effectiveness of our teacher-student distillation framework.

Analysis for Depth-Anything-3-Metric

Figure 9 Visualizations of camera pose and depth estimation on in-the-wild scenes.

SUN-RGBD [81] and DIODE (indoor) [88]. As shown in Tab. 11, DA3-metric achieves state-of-the-art performance on ETH3D (δ1 = 0.917, AbsRel = 0.104), substantially outperforming the second-best method UniDepthv2 (δ1 = 0.863) by a large margin. DA3-metric also achieves best performance on SUN-RGBD for AbsRel (0.105) and second-best on DIODE (δ1 = 0.838, AbsRel = 0.128). While UniDepthv1 and UniDepthv2 achieve the best results on NYUv2 and KITTI, DA3-metric demonstrates strong generalization and competitive performance across all benchmarks, particularly excelling on diverse outdoor scenes like ETH3D. We ablate the Teacher supervision in Tab. 11. The results show interesting trade-offs: removing Teacher supervision slightly improves metrics on NYUv2 and KITTI, while maintaining comparable performance on other datasets. As shown in Fig. 10, Teacher supervision significantly improves sharpness and fine detail quality, demonstrating that Teacher provides complementary knowledge beyond standard metrics.

Analysis for Feed-forward 3DGS

We retrain all compared feed-forward 3DGS models, ensuring that the training configuration matches the testing setup by using 12 input context views selected through farthest point sampling. We apply engineering optimizations such as flash attention and fully shared data parallelism to enable all models to process 12 Table 10 Monocular student depth comparisons. δ1 ↑

Method

Table 11 Comparison with state-of-the-arts on metric depth estimation. The best and second best are highlighted. Bottom rows show ablation results with and without teacher supervision. Note that the ablation setting is slightly different from the final model on training resolution, which leads to minor differences in performance.

Methods

Figure 10 Effectiveness of Teacher model for supervising metric depth estimation. Incorporating Teacher model for supervision significantly improves the metric depth sharpness.

input views efficiently. Depth training loss are incorporated for all baselines to ensure stable training and convergence. All models are trained on 8 A100 GPUs for 200K steps with a batch size of 1, except for pixelSplat, which is trained for 100K steps due to rather slow epipolar attention. All results are reported at H × W = 270 × 480. Visual quality analysis.

We present visual comparisons with other models in Fig. 11 under novel view synthesis settings. As illustrated, simply augmenting our DA3 model with a 3D Gaussian DPT head yields significantly improved rendering quality over existing state-of-the-art approaches. Our model demonstrates particular strength in challenging regions, such as thin structures (e.g., columns in the first and third scenes) and large-scale outdoor environments with wide-baseline input views (last two scenes), as shown in Fig. 11. These results underscore the importance of a robust geometry backbone for high-quality visual rendering, consistent with our quantitative findings in Tab. 5. We anticipate that the strong geometric understanding of DA3 will also benefit other 3D vision tasks.

Conclusion and Discussion

Depth Anything 3 shows that a plain transformer, trained on depth-and-ray targets with teacher–student supervision, can unify any-view geometry without ornate architectures. Scale-aware depth, per-pixel rays, and adaptive cross-view attention let the model inherit strong pretrained features while remaining lightweight and easy to extend. On the proposed visual geometry benchmark the approach sets new pose and reconstruction records, with both giant and compact variants surpassing prior models, while the same backbone powers efficient feed-forward novel view synthesis model. We view Depth Anything 3 as a step toward versatile 3D foundation models. Future work can extend its reasoning to dynamic scenes, integrate language and interaction cues, and explore larger-scale pretraining to close the loop between geometry understanding and actionable world models. We hope the model and dataset releases, benchmark, and simple modeling principles offered here catalyze broader research on general-purpose 3D perception.

Acknowledgement We thank Xiaowei Zhou, Sida Peng and Hengkai Guo for their valuable discussions during the development of this project. We are also grateful to Yang Zhao for his engineering support. The input images in the teaser demo were extracted from a publicly available YouTube video [21], credited to the original creator.

Figure 11 Qualitative comparisons with state-of-the-art methods for visual rendering. The first column shows the selected input views, while the remaining columns display novel views rendered by comparison models and ground truth. For each scene, two rendered novel viewpoints are presented in consecutive rows. The first three scenes are from DL3DV, the following two are from Tanks and Temples, and the last three are from MegaDepth. Compared to other methods, our model consistently achieves superior rendering quality across diverse and challenging scenes.
