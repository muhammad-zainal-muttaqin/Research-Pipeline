# 025 - Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2021swin` |
| Judul asli | Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows |
| Penulis | Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, Baining Guo |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2021) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2103.14030
- **Kode sumber resmi:** https://github.com/microsoft/Swin-Transformer
- **Google Scholar:** https://scholar.google.com/scholar?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Swin Transformer, *backbone* (jaringan pengekstrak fitur) visi berbasis Transformer untuk tujuan umum. Dua kelemahan Transformer visi sebelumnya, ViT (bab 024), diperbaiki sekaligus: biaya *self-attention* (atensi-diri, mekanisme yang membobot relasi antartoken) yang kuadratik terhadap jumlah token, dan peta fitur beresolusi tunggal yang tidak cocok untuk prediksi padat seperti deteksi objek dan segmentasi semantik. Solusinya: *self-attention* hanya dihitung di dalam jendela lokal yang tidak tumpang tindih, partisi jendela digeser pada lapisan berikutnya agar informasi tetap mengalir antar-jendela, dan peta fitur disusun hierarkis dari resolusi tinggi ke rendah.

Model terbesarnya mencapai akurasi top-1 87,3% pada klasifikasi ImageNet-1K (dengan pra-pelatihan ImageNet-22K), 58,7 box AP dan 51,1 mask AP pada COCO *test-dev*, serta 53,5 mIoU pada ADE20K — ketiganya melampaui hasil terbaik sebelumnya dengan margin lebih dari dua poin.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pemodelan visi lama didominasi jaringan saraf konvolusi (CNN) seperti ResNet, yang membangun representasi secara hierarkis: resolusi peta fitur diturunkan bertahap sambil jumlah kanal dinaikkan. Struktur multi-skala ini penting karena ukuran objek dalam citra sangat bervariasi, dan kerangka hilir seperti FPN (*Feature Pyramid Network*, modul yang menggabungkan peta fitur beberapa resolusi untuk mendeteksi objek berbagai ukuran) dirancang di atasnya.

Vision Transformer (ViT, bab 024) membuktikan arsitektur Transformer mampu menyaingi CNN pada klasifikasi: citra dipotong menjadi *patch* (petak piksel) berukuran tetap, setiap petak diubah menjadi satu *token* (vektor satuan pemrosesan), dan semua token berinteraksi melalui *self-attention* global. Desain ini menyimpan dua masalah. Pertama, biaya komputasinya kuadratik terhadap jumlah token karena setiap token berelasi dengan semua token lain — tidak terjangkau pada citra beresolusi tinggi yang menghasilkan ribuan token. Kedua, resolusi token dipertahankan sama dari awal sampai akhir, sehingga hanya dihasilkan peta fitur satu skala.

Upaya lain menekan biaya attention dengan *sliding window* (jendela geser): attention setiap piksel dibatasi pada tetangganya, tetapi himpunan pembanding yang berbeda per piksel membuat akses memorinya tidak efisien. Makalah ini merancang Transformer yang sekaligus efisien, hierarkis, dan kuat daya modelnya.

## Ide Utama

Gagasan intinya terdiri atas dua bagian yang saling melengkapi. Pertama, *self-attention* dihitung hanya di dalam **jendela lokal** yang mempartisi citra tanpa tumpang tindih; karena ukuran jendela tetap, biaya per jendela konstan dan total biaya linear terhadap jumlah token. Kedua, partisi jendela **digeser** pada blok berikutnya, sehingga jendela baru melintasi batas jendela lama dan token yang tadinya terpisah kini berbagi satu jendela. Pergantian dua konfigurasi ini memulihkan konektivitas antar-jendela tanpa mengorbankan efisiensi.

Di atas keduanya, representasi dibuat hierarkis melalui *patch merging*: kelompok token bertetangga digabung menjadi satu token baru per tahap, mengikuti pola penurunan resolusi pada CNN. Keluaran tiap tahap berbeda resolusi, sehingga Swin dapat langsung menggantikan *backbone* CNN pada kerangka deteksi atau segmentasi yang ada.

## Cara Kerja Langkah demi Langkah

### Partisi Patch dan Token

Citra RGB masukan dibagi menjadi *patch* 4×4 piksel yang tidak tumpang tindih. Setiap petak direpresentasikan sebagai gabungan nilai piksel mentahnya: 4×4×3 = 48 angka. Sebuah lapisan linear (*linear embedding*) memproyeksikan vektor 48 dimensi ini menjadi vektor C dimensi, dengan C sebagai lebar kanal dasar model. Pada citra 224×224, pembagian ini menghasilkan 56×56 = 3.136 token.

### Blok Swin Transformer

Blok Swin Transformer adalah blok Transformer standar yang modul attention-nya diganti attention berjendela. Susunannya: normalisasi *LayerNorm* (LN, penormalan fitur per token), modul *multi-head self-attention* berjendela, koneksi residual (keluaran modul ditambahkan ke masukannya), LN kedua, MLP dua lapis dengan aktivasi GELU, dan koneksi residual kedua. *Multi-head* berarti attention dihitung paralel pada beberapa sub-ruang fitur (kepala) yang lalu digabung; dimensi tiap kepala 32. Blok dipasangkan: blok berpartisi reguler (W-MSA) diikuti blok berpartisi bergeser (SW-MSA).

### Attention di dalam Jendela (W-MSA)

Pada W-MSA (*window multi-head self-attention*), peta fitur h×w token dipartisi menjadi jendela-jendela berisi M×M token (M = 7 secara baku, 49 token per jendela), dan attention hanya dihitung antar-token dalam jendela yang sama. Biaya attention global adalah Ω(MSA) = 4hwC² + 2(hw)²C — suku kedua kuadratik terhadap jumlah token hw — sedangkan versi berjendela Ω(W-MSA) = 4hwC² + 2M²hwC, linear terhadap hw karena M tetap.

Contoh numerik pada tahap pertama (h = w = 56): attention global membutuhkan 3.136² ≈ 9,8 juta pasangan token per kepala, sedangkan W-MSA membutuhkan 64 jendela × 49² = 153.664 pasangan — 64 kali lebih sedikit. Selisih ini makin besar pada citra beresolusi tinggi.

### Partisi Jendela yang Digeser (SW-MSA)

Attention murni berjendela tidak memiliki koneksi antar-jendela, sehingga daya modelnya turun. SW-MSA (*shifted window*) menggeser partisi jendela sejauh ⌊M/2⌋ token ke arah kiri-atas (3 token untuk M = 7), sehingga informasi menyebar antar-jendela melalui kedalaman jaringan. Ilustrasinya pada peta 8×8 token dengan jendela 4×4 (geseran 2 token):

```
partisi reguler (W-MSA)         partisi bergeser (SW-MSA)
peta 8x8 token, jendela 4x4     digeser (2,2): 9 jendela
┌────────┬────────┐             ┌───┬──────┬───┐
│        │        │             │   │      │   │
│   A    │   B    │             ├───┼──────┼───┤
│        │        │             │   │      │   │
├────────┼────────┤    ---->    ├───┼──────┼───┤
│        │        │             │   │      │   │
│   C    │   D    │             ├───┼──────┼───┤
│        │        │             │   │      │   │
└────────┴────────┘             └───┴──────┴───┘
```

Jendela tengah pada konfigurasi bergeser mencakup seperempat wilayah jendela A, B, C, dan D; token yang tadinya terpisah kini saling ber-attention. Pergeseran menambah jumlah jendela (2×2 menjadi 3×3) dengan jendela tepi lebih kecil dari M×M. Solusi naif berupa *padding* (token kosong tambahan) menaikkan komputasi sampai 2,25 kali; makalah memakai *cyclic shift* (bagian yang keluar tepi dipindahkan ke sisi berlawanan) diikuti *attention mask* (larangan attention antar-token yang semula tidak bersebelahan), sehingga jumlah jendela yang dihitung tetap. Implementasi ini 13–18% lebih cepat daripada *padding* naif.

### Penggabungan Patch dan Empat Tahap Hierarkis

Lapisan *patch merging* ditempatkan antar-tahap: fitur setiap kelompok 2×2 token bertetangga digabungkan menjadi vektor 4C, lalu lapisan linear memproyeksikannya ke 2C. Jumlah token berkurang empat kali lipat dan resolusi turun dua kali lipat per dimensi. Pengulangan prosedur ini membentuk empat tahap beresolusi H/4×W/4, H/8×W/8, H/16×W/16, dan H/32×W/32 — sama dengan pembagian resolusi pada CNN seperti ResNet. Alurnya untuk Swin-T pada citra 224×224:

```
citra RGB 224x224
   │  patch 4x4 + linear embedding (48 -> C=96)
   ▼
Tahap 1:  56x56 token, dim 96    [2 blok Swin]
   │  patch merging: gabung 2x2 tetangga (96 -> 192)
   ▼
Tahap 2:  28x28 token, dim 192   [2 blok Swin]
   │  patch merging (192 -> 384)
   ▼
Tahap 3:  14x14 token, dim 384   [6 blok Swin]
   │  patch merging (384 -> 768)
   ▼
Tahap 4:  7x7 token, dim 768     [2 blok Swin]
   ▼
keluaran multi-skala -> klasifikasi / deteksi / segmentasi
```

### Bias Posisi Relatif

Attention tidak mengetahui posisi token. Alih-alih *absolute position embedding* (vektor posisi per token seperti pada ViT), Swin menambahkan *relative position bias* (bias posisi relatif) B pada skor kesamaan: Attention(Q,K,V) = SoftMax(QKᵀ/√d + B)V. Q, K, V adalah matriks *query*, *key*, dan *value*: proyeksi linear fitur token untuk mencari kesamaan, membandingkan, dan membawa isi yang dibobotkan. B diambil dari matriks (2M−1)×(2M−1) = 13×13 yang dipelajari, diindeks oleh jarak relatif antar-token pada kedua sumbu. Bias relatif ini memberi ketidakpekaan terhadap pergeseran posisi objek (*translation invariance*) yang berguna untuk prediksi padat.

### Varian Model

Empat varian disediakan dengan mengatur lebar kanal dasar C dan jumlah blok per tahap: Swin-T (C = 96, blok {2,2,6,2}; 29 juta parameter dan 4,5 GFLOPs, sekelas ResNet-50), Swin-S (C = 96, blok {2,2,18,2}; 50 juta parameter, sekelas ResNet-101), Swin-B (C = 128, blok {2,2,18,2}; 88 juta parameter, sekelas ViT-B), dan Swin-L (C = 192, blok {2,2,18,2}; 197 juta parameter). FLOPs (*floating-point operations*) mengukur biaya komputasi satu inferensi; G berarti giga (miliar).

## Eksperimen dan Hasil

Tiga tolok ukur dipakai: klasifikasi pada ImageNet-1K (1,28 juta citra latih, 1.000 kelas) dengan metrik akurasi top-1 (proporsi citra yang kelas teratas prediksinya benar); deteksi objek dan segmentasi instans pada COCO 2017 (118 ribu citra latih) dengan AP (*Average Precision*, ringkasan kurva presisi-recall pada berbagai ambang tumpang tindih) untuk kotak (*box AP*) dan masker piksel (*mask AP*); serta segmentasi semantik pada ADE20K (150 kategori) dengan mIoU (*mean Intersection over Union*, rata-rata rasio irisan terhadap gabungan antara peta kelas prediksi dan kebenaran). Deteksi diuji pada empat kerangka (Cascade Mask R-CNN, ATSS, RepPoints v2, Sparse R-CNN) dan segmentasi pada kerangka UperNet, dengan hanya mengganti *backbone*-nya.

Hasil utamanya sebagai berikut:

- ImageNet-1K: Swin-T mencapai 81,3% top-1, melampaui DeiT-S (79,8%), varian ViT berukuran sebanding, dengan margin +1,5 poin. Dengan pra-pelatihan ImageNet-22K (14,2 juta citra), Swin-B mencapai 86,4% pada resolusi 384², unggul 2,4 poin atas ViT-B/16 (84,0%) pada *throughput* (citra per detik) yang hampir sama (84,7 banding 85,9) dan FLOPs lebih rendah (47,0G banding 55,4G). Swin-L mencapai 87,3%.
- COCO: Swin-T unggul konsisten +3,4 sampai +4,2 box AP atas ResNet-50 pada keempat kerangka deteksi (pada Cascade Mask R-CNN: 50,5 banding 46,3). Pada ukuran model dan kecepatan sebanding, Swin-B mencapai 51,9 box AP dan 45,0 mask AP, mengungguli ResNeXt101-64x4d (48,3 dan 41,7). Sistem terbaik (Swin-L pada kerangka HTC++ dengan pengujian multi-skala) mencapai 58,7 box AP dan 51,1 mask AP pada *test-dev*, melampaui hasil terbaik sebelumnya sebesar +2,7 (Copy-paste) dan +2,6 (DetectoRS). Kenaikan beberapa poin AP tergolong besar untuk tolok ukur ini.
- ADE20K: Swin-S mencapai 49,3 mIoU, jauh di atas DeiT-S (44,0) pada biaya komputasi sebanding. Swin-L dengan pra-pelatihan ImageNet-22K mencapai 53,5 mIoU, unggul +3,2 atas SETR (50,3) — pendekatan berbasis ViT untuk segmentasi — dengan model lebih kecil (234 juta banding 308 juta parameter).

Ablasi (uji dengan mematikan satu komponen) pada Swin-T menegaskan rancangannya. Tanpa penggeseran jendela, akurasi turun ke 80,2% top-1 (−1,1), 47,7 box AP (−2,8), dan 43,3 mIoU (−2,8) — bukti bahwa koneksi antar-jendela berkontribusi nyata. Bias posisi relatif memberi tambahan +1,2 poin top-1 dibanding tanpa posisi dan +2,3 mIoU; menambahkan posisi absolut justru sedikit merugikan deteksi dan segmentasi. Partisi bergeser seakurat *sliding window* (81,3% banding 81,4% top-1), tetapi Swin-T utuh 4,1 kali lebih cepat daripada implementasi *sliding window* naif.

## Kelebihan dan Keterbatasan

Kelebihan: (1) kompleksitas linear membuat attention terjangkau pada citra beresolusi tinggi; (2) peta fitur hierarkis beresolusi standar CNN sehingga langsung kompatibel dengan FPN maupun UperNet; (3) partisi bergeser memulihkan koneksi antar-jendela dengan latensi tambahan kecil dan efisien pada perangkat keras umum; (4) satu arsitektur yang sama kuat pada klasifikasi, deteksi, dan segmentasi.

Keterbatasan: attention tetap lokal per lapisan; interaksi sangat jauh hanya terjalin tidak langsung melalui tumpukan lapisan. Dari sisi rekayasa, implementasinya lebih rumit dari CNN standar (partisi bergeser, *cyclic shift*, *attention mask* khusus), dan *throughput* yang dilaporkan masih berbasis fungsi PyTorch umum — pembanding ResNe(X)t diuntungkan kernel cuDNN yang sangat dioptimalkan, sehingga perbandingan kecepatan belum final. Angka terbaik pada ketiga tolok ukur juga bergantung pada pra-pelatihan ImageNet-22K; tanpa data tambahan itu keunggulannya lebih tipis. Ukuran jendela baku 7×7 mengikat: pada resolusi yang jauh berbeda diperlukan *padding* atau interpolasi bias posisi.

## Kaitan dengan Bab Lain

Bab ini menjawab keterbatasan ViT pada [bab 024](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md): attention global kuadratik digantikan attention berjendela linear, dan peta fitur satu skala digantikan hierarki empat tahap. Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)) turut membangun fitur multi-resolusi tetapi mempertahankan attention kuadratik. Desain ini disempurnakan penerusnya, Swin Transformer V2 ([bab 163](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)), yang menskalakan kapasitas dan resolusi model. Dari sisi CNN, ConvNeXt ([bab 162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)) memodernisasi ResNet dengan menyerap pilihan desain Transformer sebagai pembanding kuat Swin. Jejak praktisnya terlihat pada metode hilir yang memakainya sebagai *backbone*, misalnya SwinNet ([bab 043](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)) untuk deteksi objek menonjol RGB-D.

## Poin untuk Sitasi

Kutip dengan kunci `liu2021swin` (ICCV 2021, halaman 10012–10022). Ringkasan yang aman dikutip: "Swin Transformer adalah *backbone* visi hierarkis yang menghitung *self-attention* di dalam jendela lokal tidak tumpang tindih dan menggeser partisi jendela antar-lapisan, sehingga berkompleksitas linear terhadap ukuran citra sekaligus tetap menghubungkan antar-jendela. Model ini mencapai 87,3% top-1 pada ImageNet-1K, 58,7 box AP pada COCO *test-dev*, dan 53,5 mIoU pada ADE20K."

Catatan verifikasi sebelum sitasi formal: angka 87,3% top-1 dan 53,5 mIoU diperoleh dengan pra-pelatihan ImageNet-22K, dan angka COCO terbaik memakai kerangka HTC++ dengan pengujian multi-skala — sebutkan konteks ini bila mengutip. Akurasi Swin-B 224² pada ImageNet-1K tercatat 83,3% pada teks tetapi 83,5% pada tabel makalah (arXiv v2); periksa versi prosiding sebelum mengutipnya.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
1. Introduction Modeling in computer vision has long been dominated by convolutional neural networks (CNNs). Beginning with AlexNet [39] and its revolutionary performance on the ImageNet image classification challenge, CNN architectures have evolved to become increasingly powerful through * Equal contribution. † Interns at MSRA. ‡ Contact person.

Figure 1. (a) The proposed Swin Transformer builds hierarchical feature maps by merging image patches (shown in gray) in deeper layers and has linear computation complexity to input image size due to computation of self-attention only within each local window (shown in red). It can thus serve as a general-purpose backbone for both image classification and dense recognition tasks. (b) In contrast, previous vision Transformers [20] produce feature maps of a single low resolution and have quadratic computation complexity to input image size due to computation of selfattention globally.

greater scale [30, 76], more extensive connections [34], and more sophisticated forms of convolution [70, 18, 84]. With CNNs serving as backbone networks for a variety of vision tasks, these architectural advances have led to performance improvements that have broadly lifted the entire field. On the other hand, the evolution of network architectures in natural language processing (NLP) has taken a different path, where the prevalent architecture today is instead the Transformer [64]. Designed for sequence modeling and transduction tasks, the Transformer is notable for its use of attention to model long-range dependencies in the data. Its tremendous success in the language domain has led researchers to investigate its adaptation to computer vision, where it has recently demonstrated promising results on certain tasks, specifically image classification [20] and joint vision-language modeling [47]. In this paper, we seek to expand the applicability of Transformer such that it can serve as a general-purpose

backbone for computer vision, as it does for NLP and as CNNs do in vision. We observe that significant challenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection [42, 53, 54]. In existing Transformer-based models [64, 20], tokens are all of a fixed scale, a property unsuitable for these vision applications. Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size. To overcome these issues, we propose a generalpurpose Transformer backbone, called Swin Transformer, which constructs hierarchical feature maps and has linear computational complexity to image size. As illustrated in Figure 1(a), Swin Transformer constructs a hierarchical representation by starting from small-sized patches (outlined in gray) and gradually merging neighboring patches in deeper Transformer layers. With these hierarchical feature maps, the Swin Transformer model can conveniently leverage advanced techniques for dense prediction such as feature pyramid networks (FPN) [42] or U-Net [51]. The linear computational complexity is achieved by computing self-attention locally within non-overlapping windows that partition an image (outlined in red). The number of patches in each window is fixed, and thus the complexity becomes linear to image size. These merits make Swin Transformer suitable as a general-purpose backbone for various vision tasks, in contrast to previous Transformer based architectures [20] which produce feature maps of a single resolution and have quadratic complexity. A key design element of Swin Transformer is its shift of the window partition between consecutive self-attention layers, as illustrated in Figure 2. The shifted windows bridge the windows of the preceding layer, providing connections among them that significantly enhance modeling power (see Table 4). This strategy is also efficient in regards to real-world latency: all query patches within a window share the same key set1 , which facilitates memory access in hardware. In contrast, earlier sliding window based self-attention approaches [33, 50] suffer from low latency on general hardware due to different key sets for different query pixels2 . Our experiments show that the proposed

Figure 2. An illustration of the shifted window approach for computing self-attention in the proposed Swin Transformer architecture. In layer l (left), a regular window partitioning scheme is adopted, and self-attention is computed within each window. In the next layer l + 1 (right), the window partitioning is shifted, resulting in new windows. The self-attention computation in the new windows crosses the boundaries of the previous windows in layer l, providing connections among them.

1 The query and key are projection vectors in a self-attention layer. 2 While there are efficient methods to implement a sliding-window

weights across a feature map, it is difficult for a sliding-window based self-attention layer to have efficient memory access in practice.

HRNet [65], and EfficientNet [58]. In addition to these architectural advances, there has also been much work on improving individual convolution layers, such as depthwise convolution [70] and deformable convolution [18, 84]. While the CNN and its variants are still the primary backbone architectures for computer vision applications, we highlight the strong potential of Transformer-like architectures for unified modeling between vision and language. Our work achieves strong performance on several basic visual recognition tasks, and we hope it will contribute to a modeling shift.

resolution is high, due to its low-resolution feature maps and the quadratic increase in complexity with image size. There are a few works applying ViT models to the dense vision tasks of object detection and semantic segmentation by direct upsampling or deconvolution but with relatively lower performance [2, 81]. Concurrent to our work are some that modify the ViT architecture [72, 15, 28] for better image classification. Empirically, we find our Swin Transformer architecture to achieve the best speedaccuracy trade-off among these methods on image classification, even though our work focuses on general-purpose performance rather than specifically on classification. Another concurrent work [66] explores a similar line of thinking to build multi-resolution feature maps on Transformers. Its complexity is still quadratic to image size, while ours is linear and also operates locally which has proven beneficial in modeling the high correlation in visual signals [36, 25, 41]. Our approach is both efficient and effective, achieving state-of-the-art accuracy on both COCO object detection and ADE20K semantic segmentation.

Self-attention based backbone architectures Also inspired by the success of self-attention layers and Transformer architectures in the NLP field, some works employ self-attention layers to replace some or all of the spatial convolution layers in the popular ResNet [33, 50, 80]. In these works, the self-attention is computed within a local window of each pixel to expedite optimization [33], and they achieve slightly better accuracy/FLOPs trade-offs than the counterpart ResNet architecture. However, their costly memory access causes their actual latency to be significantly larger than that of the convolutional networks [33]. Instead of using sliding windows, we propose to shift windows between consecutive layers, which allows for a more efficient implementation in general hardware.

3. Method 3.1. Overall Architecture An overview of the Swin Transformer architecture is presented in Figure 3, which illustrates the tiny version (SwinT). It first splits an input RGB image into non-overlapping patches by a patch splitting module, like ViT. Each patch is treated as a “token” and its feature is set as a concatenation of the raw pixel RGB values. In our implementation, we use a patch size of 4 × 4 and thus the feature dimension of each patch is 4 × 4 × 3 = 48. A linear embedding layer is applied on this raw-valued feature to project it to an arbitrary dimension (denoted as C). Several Transformer blocks with modified self-attention computation (Swin Transformer blocks) are applied on these patch tokens. The Transformer blocks maintain the number W of tokens ( H 4 × 4 ), and together with the linear embedding are referred to as “Stage 1”. To produce a hierarchical representation, the number of tokens is reduced by patch merging layers as the network gets deeper. The first patch merging layer concatenates the features of each group of 2 × 2 neighboring patches, and applies a linear layer on the 4C-dimensional concatenated features. This reduces the number of tokens by a multiple of 2 × 2 = 4 (2× downsampling of resolution), and the output dimension is set to 2C. Swin Transformer blocks are applied afterwards for feature transformation, with the resW olution kept at H 8 × 8 . This first block of patch merging and feature transformation is denoted as “Stage 2”. The procedure is repeated twice, as “Stage 3” and “Stage 4”, with H H W output resolutions of 16 × W 16 and 32 × 32 , respectively. These stages jointly produce a hierarchical representation,

Self-attention/Transformers to complement CNNs Another line of work is to augment a standard CNN architecture with self-attention layers or Transformers. The selfattention layers can complement backbones [67, 7, 3, 71, 23, 74, 55] or head networks [32, 27] by providing the capability to encode distant dependencies or heterogeneous interactions. More recently, the encoder-decoder design in Transformer has been applied for the object detection and instance segmentation tasks [8, 13, 85, 56]. Our work explores the adaptation of Transformers for basic visual feature extraction and is complementary to these works. Transformer based vision backbones Most related to our work is the Vision Transformer (ViT) [20] and its follow-ups [63, 72, 15, 28, 66]. The pioneering work of ViT directly applies a Transformer architecture on nonoverlapping medium-sized image patches for image classification. It achieves an impressive speed-accuracy tradeoff on image classification compared to convolutional networks. While ViT requires large-scale training datasets (i.e., JFT-300M) to perform well, DeiT [63] introduces several training strategies that allow ViT to also be effective using the smaller ImageNet-1K dataset. The results of ViT on image classification are encouraging, but its architecture is unsuitable for use as a general-purpose backbone network on dense vision tasks or when the input image 3

Figure 3. (a) The architecture of a Swin Transformer (Swin-T); (b) two successive Swin Transformer Blocks (notation presented with Eq. (3)). W-MSA and SW-MSA are multi-head self attention modules with regular and shifted windowing configurations, respectively.

with the same feature map resolutions as those of typical convolutional networks, e.g., VGG [52] and ResNet [30]. As a result, the proposed architecture can conveniently replace the backbone networks in existing methods for various vision tasks.

where the former is quadratic to patch number hw, and the latter is linear when M is fixed (set to 7 by default). Global self-attention computation is generally unaffordable for a large hw, while the window based self-attention is scalable.

Swin Transformer block Swin Transformer is built by replacing the standard multi-head self attention (MSA) module in a Transformer block by a module based on shifted windows (described in Section 3.2), with other layers kept the same. As illustrated in Figure 3(b), a Swin Transformer block consists of a shifted window based MSA module, followed by a 2-layer MLP with GELU nonlinearity in between. A LayerNorm (LN) layer is applied before each MSA module and each MLP, and a residual connection is applied after each module.

Shifted window partitioning in successive blocks The window-based self-attention module lacks connections across windows, which limits its modeling power. To introduce cross-window connections while maintaining the efficient computation of non-overlapping windows, we propose a shifted window partitioning approach which alternates between two partitioning configurations in consecutive Swin Transformer blocks. As illustrated in Figure 2, the first module uses a regular window partitioning strategy which starts from the top-left pixel, and the 8 × 8 feature map is evenly partitioned into 2 × 2 windows of size 4 × 4 (M = 4). Then, the next module adopts a windowing configuration that is shifted from that of the preceding layer, by displacing the windows by M (b M 2 c, b 2 c) pixels from the regularly partitioned windows. With the shifted window partitioning approach, consecutive Swin Transformer blocks are computed as

3.2. Shifted Window based Self-Attention The standard Transformer architecture [64] and its adaptation for image classification [20] both conduct global selfattention, where the relationships between a token and all other tokens are computed. The global computation leads to quadratic complexity with respect to the number of tokens, making it unsuitable for many vision problems requiring an immense set of tokens for dense prediction or to represent a high-resolution image.

Self-attention in non-overlapped windows For efficient modeling, we propose to compute self-attention within local windows. The windows are arranged to evenly partition the image in a non-overlapping manner. Supposing each window contains M × M patches, the computational complexity of a global MSA module and a window based one

where ẑl and zl denote the output features of the (S)WMSA module and the MLP module for block l, respectively; 3 We omit SoftMax computation in determining complexity.

We observe significant improvements over counterparts without this bias term or that use absolute position embedding, as shown in Table 4. Further adding absolute position embedding to the input as in [20] drops performance slightly, thus it is not adopted in our implementation. The learnt relative position bias in pre-training can be also used to initialize a model for fine-tuning with a different window size through bi-cubic interpolation [20, 63].

Figure 4. Illustration of an efficient batch computation approach for self-attention in shifted window partitioning.

3.3. Architecture Variants

W-MSA and SW-MSA denote window based multi-head self-attention using regular and shifted window partitioning configurations, respectively. The shifted window partitioning approach introduces connections between neighboring non-overlapping windows in the previous layer and is found to be effective in image classification, object detection, and semantic segmentation, as shown in Table 4.

We build our base model, called Swin-B, to have of model size and computation complexity similar to ViTB/DeiT-B. We also introduce Swin-T, Swin-S and Swin-L, which are versions of about 0.25×, 0.5× and 2× the model size and computational complexity, respectively. Note that the complexity of Swin-T and Swin-S are similar to those of ResNet-50 (DeiT-S) and ResNet-101, respectively. The window size is set to M = 7 by default. The query dimension of each head is d = 32, and the expansion layer of each MLP is α = 4, for all experiments. The architecture hyper-parameters of these model variants are:

4. Experiments We conduct experiments on ImageNet-1K image classification [19], COCO object detection [43], and ADE20K semantic segmentation [83]. In the following, we first compare the proposed Swin Transformer architecture with the previous state-of-the-arts on the three tasks. Then, we ablate the important design elements of Swin Transformer.

4.1. Image Classification on ImageNet-1K Settings For image classification, we benchmark the proposed Swin Transformer on ImageNet-1K [19], which contains 1.28M training images and 50K validation images from 1,000 classes. The top-1 accuracy on a single crop is reported. We consider two training settings:

• Regular ImageNet-1K training. This setting mostly follows [63]. We employ an AdamW [37] optimizer for 300 epochs using a cosine decay learning rate scheduler and 20 epochs of linear warm-up. A batch size of 1024, an initial learning rate of 0.001, and a

4 To make the window size (M, M ) divisible by the feature map size of (h, w), bottom-right padding is employed on the feature map if needed.

weight decay of 0.05 are used. We include most of the augmentation and regularization strategies of [63] in training, except for repeated augmentation [31] and EMA [45], which do not enhance performance. Note that this is contrary to [63] where repeated augmentation is crucial to stabilize the training of ViT. • Pre-training on ImageNet-22K and fine-tuning on ImageNet-1K. We also pre-train on the larger ImageNet-22K dataset, which contains 14.2 million images and 22K classes. We employ an AdamW optimizer for 90 epochs using a linear decay learning rate scheduler with a 5-epoch linear warm-up. A batch size of 4096, an initial learning rate of 0.001, and a weight decay of 0.01 are used. In ImageNet-1K fine-tuning, we train the models for 30 epochs with a batch size of 1024, a constant learning rate of 10−5 , and a weight decay of 10−8 .

Results with regular ImageNet-1K training Table 1(a) presents comparisons to other backbones, including both Transformer-based and ConvNet-based, using regular ImageNet-1K training. Compared to the previous state-of-the-art Transformerbased architecture, i.e. DeiT [63], Swin Transformers noticeably surpass the counterpart DeiT architectures with similar complexities: +1.5% for Swin-T (81.3%) over DeiT-S (79.8%) using 2242 input, and +1.5%/1.4% for Swin-B (83.3%/84.5%) over DeiT-B (81.8%/83.1%) using 2242 /3842 input, respectively. Compared with the state-of-the-art ConvNets, i.e. RegNet [48] and EfficientNet [58], the Swin Transformer achieves a slightly better speed-accuracy trade-off. Noting that while RegNet [48] and EfficientNet [58] are obtained via a thorough architecture search, the proposed Swin Transformer is adapted from the standard Transformer and has strong potential for further improvement.

4.2. Object Detection on COCO Settings Object detection and instance segmentation experiments are conducted on COCO 2017, which contains 118K training, 5K validation and 20K test-dev images. An ablation study is performed using the validation set, and a system-level comparison is reported on test-dev. For the ablation study, we consider four typical object detection frameworks: Cascade Mask R-CNN [29, 6], ATSS [79], RepPoints v2 [12], and Sparse RCNN [56] in mmdetection [10]. For these four frameworks, we utilize the same settings: multi-scale training [8, 56] (resizing the input such that the shorter side is between 480 and 800 while the longer side is at most 1333), AdamW [44] optimizer (initial learning rate of 0.0001, weight decay of 0.05, and batch size of 16), and 3x schedule (36 epochs). For system-level comparison, we adopt an improved HTC [9] (denoted as HTC++) with instaboost [22], stronger multi-scale training [7], 6x schedule (72 epochs), soft-NMS [5], and ImageNet-22K pre-trained model as initialization. We compare our Swin Transformer to standard Con-

Results with ImageNet-22K pre-training We also pretrain the larger-capacity Swin-B and Swin-L on ImageNet22K. Results fine-tuned on ImageNet-1K image classification are shown in Table 1(b). For Swin-B, the ImageNet22K pre-training brings 1.8%∼1.9% gains over training on ImageNet-1K from scratch. Compared with the previous best results for ImageNet-22K pre-training, our models achieve significantly better speed-accuracy trade-offs: Swin-B obtains 86.4% top-1 accuracy, which is 2.4% higher than that of ViT with similar inference throughput (84.7 vs. 85.9 images/sec) and slightly lower FLOPs (47.0G vs. 55.4G). The larger Swin-L model achieves 87.3% top-1 accuracy, +0.9% better than that of the Swin-B model. 6

vNets, i.e. ResNe(X)t, and previous Transformer networks, e.g. DeiT. The comparisons are conducted by changing only the backbones with other settings unchanged. Note that while Swin Transformer and ResNe(X)t are directly applicable to all the above frameworks because of their hierarchical feature maps, DeiT only produces a single resolution of feature maps and cannot be directly applied. For fair comparison, we follow [81] to construct hierarchical feature maps for DeiT using deconvolution layers.

Comparison to previous state-of-the-art Table 2(c) compares our best results with those of previous state-ofthe-art models. Our best model achieves 58.7 box AP and 51.1 mask AP on COCO test-dev, surpassing the previous best results by +2.7 box AP (Copy-paste [26] without external data) and +2.6 mask AP (DetectoRS [46]).

Comparison to ResNe(X)t Table 2(a) lists the results of Swin-T and ResNet-50 on the four object detection frameworks. Our Swin-T architecture brings consistent +3.4∼4.2 box AP gains over ResNet-50, with slightly larger model size, FLOPs and latency. Table 2(b) compares Swin Transformer and ResNe(X)t

on COCO, and +2.3/+2.9 mIoU on ADE20K in relation to those without position encoding and with absolute position embedding, respectively, indicating the effectiveness of the relative position bias. Also note that while the inclusion of absolute position embedding improves image classification accuracy (+0.4%), it harms object detection and semantic segmentation (-0.2 box/mask AP on COCO and -0.6 mIoU on ADE20K). While the recent ViT/DeiT models abandon translation invariance in image classification even though it has long been shown to be crucial for visual modeling, we find that inductive bias that encourages certain translation invariance is still preferable for general-purpose visual modeling, particularly for the dense prediction tasks of object detection and semantic segmentation.

Different self-attention methods The real speed of different self-attention computation methods and implementations are compared in Table 5. Our cyclic implementation is more hardware efficient than naive padding, particularly for deeper stages. Overall, it brings a 13%, 18% and 18% speed-up on Swin-T, Swin-S and Swin-B, respectively. The self-attention modules built on the proposed shifted window approach are 40.8×/2.5×, 20.2×/2.5×, 9.3×/2.1×, and 7.6×/1.8× more efficient than those of sliding windows in naive/kernel implementations on four network stages, respectively. Overall, the Swin Transformer architectures built on shifted windows are 4.1/1.5, 4.0/1.5, 3.6/1.5 times faster than variants built on sliding windows for Swin-T, Swin-S, and Swin-B, respectively. Table 6 compares their accuracy on the three tasks, showing that they are similarly accurate in visual modeling. Compared to Performer [14], which is one of the fastest Transformer architectures (see [60]), the proposed shifted window based self-attention computation and the overall Swin Transformer architectures are slightly faster (see Table 5), while achieving +2.3% top-1 accuracy compared to Performer on ImageNet-1K using Swin-T (see Table 6).

When training from scratch with a 2242 input, we employ an AdamW [37] optimizer for 300 epochs using a cosine decay learning rate scheduler with 20 epochs of linear warm-up. A batch size of 1024, an initial learning rate of 0.001, a weight decay of 0.05, and gradient clipping with a max norm of 1 are used. We include most of the augmentation and regularization strategies of [63] in training, including RandAugment [17], Mixup [77], Cutmix [75], random erasing [82] and stochastic depth [35], but not repeated augmentation [31] and Exponential Moving Average (EMA) [45] which do not enhance performance. Note that this is contrary to [63] where repeated augmentation is crucial to stabilize the training of ViT. An increasing degree of stochastic depth augmentation is employed for larger models, i.e. 0.2, 0.3, 0.5 for Swin-T, Swin-S, and Swin-B, respectively. For fine-tuning on input with larger resolution, we employ an adamW [37] optimizer for 30 epochs with a constant learning rate of 10−5 , weight decay of 10−8 , and the same data augmentation and regularizations as the first stage except for setting the stochastic depth ratio to 0.1.

sentation and has linear computational complexity with respect to input image size. Swin Transformer achieves the state-of-the-art performance on COCO object detection and ADE20K semantic segmentation, significantly surpassing previous best methods. We hope that Swin Transformer’s strong performance on various vision problems will encourage unified modeling of vision and language signals. As a key element of Swin Transformer, the shifted window based self-attention is shown to be effective and efficient on vision problems, and we look forward to investigating its use in natural language processing as well.

Acknowledgement We thank many colleagues at Microsoft for their help, in particular, Li Dong and Furu Wei for useful discussions; Bin Xiao, Lu Yuan and Lei Zhang for help on datasets.

ImageNet-22K pre-training We also pre-train on the larger ImageNet-22K dataset, which contains 14.2 million images and 22K classes. The training is done in two stages. For the first stage with 2242 input, we employ an AdamW optimizer for 90 epochs using a linear decay learning rate scheduler with a 5-epoch linear warm-up. A batch size of 4096, an initial learning rate of 0.001, and a weight decay of 0.01 are used. In the second stage of ImageNet-1K finetuning with 2242 /3842 input, we train the models for 30 epochs with a batch size of 1024, a constant learning rate of 10−5 , and a weight decay of 10−8 .

A2. Detailed Experimental Settings A2.1. Image classification on ImageNet-1K The image classification is performed by applying a global average pooling layer on the output feature map of the last stage, followed by a linear classifier. We find this strategy to be as accurate as using an additional class token as in ViT [20] and DeiT [63]. In evaluation, the top-1 accuracy using a single crop is reported. Regular ImageNet-1K training The training settings mostly follow [63]. For all model variants, we adopt a default input image resolution of 2242 . For other resolutions such as 3842 , we fine-tune the models trained at 2242 resolution, instead of training from scratch, to reduce GPU consumption. 9

model as initialization. We adopt stochastic depth with ratio of 0.2 for all Swin Transformer models.

A2.3. Semantic segmentation on ADE20K ADE20K [83] is a widely-used semantic segmentation dataset, covering a broad range of 150 semantic categories. It has 25K images in total, with 20K for training, 2K for validation, and another 3K for testing. We utilize UperNet [69] in mmsegmentation [16] as our base framework for its high efficiency. In training, we employ the AdamW [44] optimizer with an initial learning rate of 6 × 10−5 , a weight decay of 0.01, a scheduler that uses linear learning rate decay, and a linear warmup of 1,500 iterations. Models are trained on 8 GPUs with 2 images per GPU for 160K iterations. For augmentations, we adopt the default setting in mmsegmentation of random horizontal flipping, random re-scaling within ratio range [0.5, 2.0] and random photometric distortion. Stochastic depth with ratio of 0.2 is applied for all Swin Transformer models. Swin-T, Swin-S are trained on the standard setting as the previous approaches with an input of 512×512. Swin-B and Swin-L with ‡ indicate that these two models are pre-trained on ImageNet-22K, and trained with the input of 640×640. In inference, a multi-scale test using resolutions that are [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]× of that in training is employed. When reporting test scores, both the training images and validation images are used for training, following common practice [71].

A3.2. Different Optimizers for ResNe(X)t on COCO Table 9 compares the AdamW and SGD optimizers of the ResNe(X)t backbones on COCO object detection. The Cascade Mask R-CNN framework is used in this comparison. While SGD is used as a default optimizer for Cascade Mask R-CNN framework, we generally observe improved accuracy by replacing it with an AdamW optimizer, particularly for smaller backbones. We thus use AdamW for ResNe(X)t backbones when compared to the proposed Swin Transformer architectures.

We apply the proposed hierarchical design and the shifted window approach to the MLP-Mixer architectures [61], referred to as Swin-Mixer. Table 10 shows the performance of Swin-Mixer compared to the original MLPMixer architectures MLP-Mixer [61] and a follow-up ap-

Table 8 lists the performance of Swin Transformers with different input image sizes from 2242 to 3842 . In general, a larger input resolution leads to better top-1 accuracy but with slower inference speed. 10

proach, ResMLP [61]. Swin-Mixer performs significantly better than MLP-Mixer (81.3% vs. 76.4%) using slightly smaller computation budget (10.4G vs. 12.7G). It also has better speed accuracy trade-off compared to ResMLP [62]. These results indicate the proposed hierarchical design and the shifted window approach are generalizable.
