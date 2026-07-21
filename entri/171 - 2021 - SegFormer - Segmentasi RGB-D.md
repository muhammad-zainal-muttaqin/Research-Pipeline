# 171 - SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xie2021segformer` |
| Judul asli | SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers |
| Penulis | Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M. Alvarez, Ping Luo |
| Tahun | 2021 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2021) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2105.15203
- **Google Scholar:** https://scholar.google.com/scholar?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers&sort=relevance

## Gambaran Umum

SegFormer adalah kerangka kerja segmentasi semantik (pelabelan kelas untuk setiap piksel citra) berbasis Transformer yang menggabungkan *encoder* hierarkis tanpa *positional encoding* (kode posisi) dengan *decoder* berupa lapisan MLP (*multilayer perceptron*, jaringan saraf lapis-penuh sederhana) tanpa konvolusi. Makalah ini menjawab dua masalah pada segmentasi berbasis Transformer generasi awal: ketergantungan pada kode posisi yang rapuh terhadap perubahan resolusi uji, dan *decoder* yang berat secara komputasi. Dengan *encoder* bernama MiT (*Mix Transformer*) berskala enam varian (B0 hingga B5) dan *decoder* MLP yang hanya mengagregasi fitur multiskala, SegFormer mencapai 51,0% mIoU (*mean Intersection-over-Union*, rata-rata rasio irisan-gabungan antara wilayah prediksi dan wilayah kebenaran, metrik utama segmentasi semantik) pada ADE20K dan 84,0% mIoU pada Cityscapes menggunakan varian terbesarnya, sekaligus menunjukkan ketahanan tinggi terhadap citra terkorupsi. Model ini menjadi salah satu tulang punggung (*backbone*) yang sering diadaptasi pada cabang RGB dari sistem segmentasi RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum SegFormer, segmentasi semantik didominasi jaringan konvolusi (*Convolutional Neural Network*, CNN) dengan struktur *encoder-decoder* (arsitektur yang mengecilkan resolusi citra secara bertahap lalu memulihkannya kembali), seperti DeepLabv3+ yang memakai konvolusi berdilasi untuk memperbesar bidang pandang tanpa menambah parameter berlebihan. Pendekatan CNN memiliki bidang pandang efektif (*effective receptive field*, wilayah citra masukan yang benar-benar memengaruhi satu keluaran fitur) yang terbatas secara struktural sehingga sulit menangkap konteks global tanpa tumpukan lapisan yang sangat dalam.

Upaya pertama menerapkan Transformer murni pada segmentasi, yaitu SETR, menggunakan *encoder* Vision Transformer (ViT, dibahas pada bab 024) yang menghasilkan fitur beresolusi tunggal dan kasar, lalu menambahkan *decoder* CNN yang berat untuk memulihkan resolusi. ViT juga bergantung pada *positional encoding* tetap yang ditambahkan ke setiap *patch* (potongan citra) di awal jaringan agar model mengetahui posisi spasialnya. Kode posisi semacam ini dilatih pada resolusi tertentu, sehingga saat citra uji berukuran berbeda dari citra latih, kode posisi harus diinterpolasi ulang secara manual dan hal ini menurunkan akurasi. Pyramid Vision Transformer (PVT, bab 164) dan Swin Transformer (bab 025) memperbaiki sisi efisiensi dengan struktur piramida multiskala dan atensi berjendela, tetapi keduanya masih mewarisi kode posisi dan umumnya dipasangkan dengan *decoder* segmentasi yang kompleks seperti *Feature Pyramid Network*. Masalah yang belum terpecahkan pada saat SegFormer diajukan adalah bagaimana merancang segmentasi berbasis Transformer yang efisien secara komputasi, tidak rapuh terhadap perubahan resolusi, dan tidak memerlukan *decoder* rumit.

## Ide Utama

Gagasan inti SegFormer adalah memisahkan tugas ekstraksi fitur multiskala dan agregasi fitur menjadi dua komponen yang masing-masing dibuat sesederhana mungkin. *Encoder* MiT menghasilkan fitur pada empat resolusi berbeda tanpa kode posisi eksplisit; informasi posisi disisipkan secara implisit melalui konvolusi 3×3 yang ditanam di dalam blok umpan-maju (*feed-forward*) Transformer, disebut Mix-FFN. Karena konvolusi bersifat lokal dan bergantung pada susunan piksel yang berdekatan, ia secara alami membawa informasi posisi tanpa perlu parameter kode posisi yang terikat pada resolusi tertentu. *Decoder*-nya berupa MLP ringan yang hanya melakukan proyeksi linear, penyamaan resolusi, dan penggabungan fitur dari keempat tahap *encoder* — tanpa konvolusi atau modul kompleks lain. Fitur dari tahap dangkal (resolusi tinggi) membawa detail lokal, sedangkan fitur dari tahap dalam (resolusi rendah) membawa konteks global; MLP sederhana cukup untuk menggabungkan keduanya karena Transformer, tidak seperti CNN, mampu menghasilkan atensi non-lokal bahkan pada tahap awal jaringan.

## Cara Kerja Langkah demi Langkah

### Encoder Hierarkis MiT

MiT terdiri atas empat tahap yang masing-masing menghasilkan peta fitur pada resolusi 1/4, 1/8, 1/16, dan 1/32 dari citra masukan, menyerupai struktur piramida pada CNN seperti ResNet. Pada citra masukan 512×512 piksel misalnya, keempat tahap menghasilkan peta fitur berukuran 128×128, 64×64, 32×32, dan 16×16. Peralihan antar-tahap dilakukan dengan *overlapped patch merging*: alih-alih memotong citra menjadi *patch* yang saling terpisah seperti pada ViT, MiT menggunakan konvolusi dengan ukuran kernel K, langkah geser (*stride*) S, dan *padding* P — tahap pertama memakai K=7, S=4, P=3, sedangkan tahap selanjutnya memakai K=3, S=2, P=1. Karena jendela konvolusi ini saling tumpang tindih, kontinuitas informasi di sekitar batas antar-*patch* tetap terjaga, berbeda dari pemotongan *patch* tanpa tumpang tindih yang memutus konteks lokal.

### Efficient Self-Attention

Mekanisme atensi mandiri (*self-attention*) standar pada Transformer memiliki kompleksitas komputasi O(N²) terhadap panjang urutan N (jumlah *patch*), karena setiap elemen dibandingkan dengan seluruh elemen lain. Pada tahap dangkal MiT, N sangat besar sebab resolusi fitur masih tinggi, sehingga komputasi ini menjadi mahal. SegFormer mereduksi urutan kunci (*key*) dan nilai (*value*) dengan rasio reduksi R sebelum dihitung skor atensinya, menurunkan kompleksitas menjadi O(N²/R). Rasio reduksi yang dipakai pada empat tahap berturut-turut adalah [64, 16, 4, 1] — tahap dangkal dengan N besar direduksi paling agresif, sedangkan tahap terdalam dengan N sudah kecil tidak direduksi sama sekali.

### Mix-FFN sebagai Pengganti Kode Posisi

Blok umpan-maju standar pada Transformer hanya terdiri atas dua lapisan linear dengan fungsi aktivasi di antaranya. Mix-FFN menyisipkan satu konvolusi 3×3 di antara dua lapisan tersebut:

```
Mix-FFN(x) = MLP( GELU( Conv3x3( MLP(x) ) ) ) + x
```

Konvolusi 3×3 ini menyebabkan kebocoran informasi posisi (*leaked location information*) karena keluaran setiap posisi kini bergantung pada susunan piksel tetangganya, bukan hanya nilai piksel itu sendiri. Dengan demikian, model tidak memerlukan parameter kode posisi terpisah yang ukurannya terikat pada resolusi citra latih.

### Decoder All-MLP

*Decoder* menerima empat peta fitur dari MiT dan memprosesnya dalam empat langkah: (1) proyeksi linear menyamakan jumlah kanal setiap peta fitur menjadi dimensi C yang seragam; (2) seluruh peta fitur diperbesar (*upsampling*) ke resolusi 1/4 citra masukan lalu digabung (*concatenate*) sepanjang dimensi kanal; (3) satu lapisan MLP menggabungkan (*fuse*) fitur gabungan tersebut; (4) satu lapisan MLP terakhir memetakan fitur ke peta segmentasi berukuran H/4 × W/4 × N_kelas, dengan N_kelas jumlah kategori target. Peta segmentasi ini kemudian diperbesar ke resolusi penuh untuk menghasilkan label per piksel.

Diagram berikut merangkum aliran data dari citra masukan hingga peta segmentasi:

```
citra HxWx3
   │
   ▼ Tahap 1 (K7,S4)      fitur H/4 x W/4     ──┐
   ▼ Tahap 2 (K3,S2)      fitur H/8 x W/8     ──┤ proyeksi linear
   ▼ Tahap 3 (K3,S2)      fitur H/16 x W/16   ──┤ + upsampling ke H/4
   ▼ Tahap 4 (K3,S2)      fitur H/32 x W/32   ──┘ + concat kanal
        (MiT: attention + Mix-FFN tiap tahap)      │
                                                     ▼
                                          MLP fusi -> MLP prediksi
                                                     │
                                                     ▼
                                      peta segmentasi H/4 x W/4 x N_kelas
```

### Varian Model B0–B5

SegFormer disediakan dalam enam ukuran, dari B0 (3,7 juta parameter, ditujukan untuk aplikasi ringan) hingga B5 (82,0 juta parameter, ditujukan untuk akurasi maksimal). Perbedaan antar-varian terutama terletak pada jumlah lapisan Transformer di tiap tahap dan lebar (dimensi tersembunyi) setiap tahap; struktur empat tahap dan mekanisme Mix-FFN tetap sama di seluruh varian, sehingga pengguna dapat memilih titik seimbang akurasi-efisiensi tanpa mengubah desain dasar.

## Eksperimen dan Hasil

SegFormer diuji pada tiga tolok ukur segmentasi semantik: ADE20K (data dalam ruangan dan luar ruangan dengan 150 kelas), Cityscapes (data jalan raya perkotaan dengan 19 kelas), dan COCO-Stuff (data 164 ribu citra dengan kelas benda dan latar). Pada ADE20K, SegFormer-B0 mencapai 37,4% mIoU dengan 8,4 GFLOPs (miliar operasi titik-mengambang), sedangkan SegFormer-B5 mencapai 51,0% mIoU dengan 183,3 GFLOPs — menunjukkan bahwa menambah kapasitas model menaikkan akurasi sekitar 13,6 poin dengan biaya komputasi naik lebih dari dua puluh kali lipat. Pada Cityscapes, SegFormer-B0 mencapai 76,2% mIoU pada kecepatan sekitar 48 *frame per second* (FPS) menggunakan citra beresolusi rendah, cocok untuk aplikasi waktu nyata, sedangkan SegFormer-B5 mencapai 84,0% mIoU pada kecepatan yang jauh lebih rendah karena resolusi uji dan kapasitas model lebih besar. Dibandingkan SETR (pendahulu berbasis Transformer), SegFormer mencapai akurasi lebih tinggi dengan model yang jauh lebih kecil dan lebih cepat — makalah melaporkan SegFormer-B5 unggul di atas SETR pada Cityscapes sambil beberapa kali lebih ringan dan lebih cepat pada tahap inferensi.

Pengujian ketahanan (*robustness*) dilakukan pada Cityscapes-C, versi Cityscapes yang dicemari beragam jenis korupsi citra (derau, cuaca, gangguan optik) pada berbagai tingkat keparahan, tanpa pelatihan ulang model (*zero-shot*). SegFormer-B5 mempertahankan akurasi jauh lebih tinggi daripada DeepLabv3+ di hampir seluruh jenis korupsi; makalah melaporkan keunggulan besar pada kondisi seperti derau Gaussian dan salju, menunjukkan bahwa *encoder* Transformer tanpa kode posisi tetap lebih tahan terhadap gangguan yang mengubah statistik citra dibandingkan CNN dengan *decoder* konvensional.

Studi ablasi pada makalah membandingkan Mix-FFN dengan kode posisi tetap saat resolusi uji diubah dari resolusi latih: model dengan Mix-FFN kehilangan akurasi jauh lebih sedikit dibandingkan model dengan kode posisi tetap, mengonfirmasi bahwa Mix-FFN adalah pengganti yang lebih tahan-resolusi. Ablasi lain mengganti *encoder* MiT dengan ResNet-101 pada *decoder* MLP yang sama; hasilnya jauh lebih rendah daripada memakai MiT berukuran sebanding, menunjukkan bahwa keunggulan *decoder* MLP bergantung pada bidang pandang non-lokal yang hanya dihasilkan Transformer, bukan berlaku umum untuk sembarang *encoder*.

## Kelebihan dan Keterbatasan

SegFormer menghilangkan dua sumber kerapuhan sekaligus: kode posisi yang terikat resolusi dan *decoder* segmentasi yang berat, sambil mempertahankan akurasi kompetitif melalui bidang pandang non-lokal bawaan Transformer. Skalabilitas enam varian memudahkan penerapan pada rentang kebutuhan komputasi yang luas, dari perangkat tepi (B0) hingga server dengan akurasi maksimal (B5). Ketahanan terhadap korupsi citra menjadikannya pilihan yang relevan untuk aplikasi luar ruangan dengan kondisi pencahayaan atau cuaca yang bervariasi.

Dari sisi rekayasa, varian besar seperti B4 dan B5 tetap menuntut memori dan komputasi yang signifikan, sehingga penerapan waktu nyata pada resolusi tinggi hanya realistis untuk varian kecil. Secara konseptual, meskipun reduksi rasio R menurunkan kompleksitas atensi, biaya komputasi pada tahap dangkal dengan resolusi tinggi tetap menjadi penyumbang FLOPs terbesar dibandingkan CNN pada tahap setara. SegFormer juga dirancang murni untuk masukan RGB; makalah tidak membahas penggabungan modalitas kedalaman (*depth*), sehingga adaptasi ke segmentasi RGB-D memerlukan modifikasi tambahan berupa cabang atau modul fusi terpisah di luar cakupan makalah aslinya.

## Kaitan dengan Bab Lain

SegFormer mewarisi konsep *encoder* hierarkis multiskala yang diperkenalkan Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)) dan menjawab kerapuhan kode posisi yang melekat pada Vision Transformer ([bab 024](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md)); desain atensi berjendela pada Swin Transformer ([bab 025](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)) merupakan pendekatan sezaman yang menyasar masalah efisiensi serupa dengan mekanisme berbeda. Sebagai *encoder* RGB yang ringan dan bebas kode posisi, SegFormer menjadi rujukan desain bagi metode segmentasi RGB-D berikutnya dalam klaster ini: EMSANet ([bab 172](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)) dan GeminiFusion ([bab 173](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)) memakai strategi fusi multimodal yang dapat dipasangkan dengan *encoder* bergaya MiT, sedangkan Omnivore ([bab 174](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md)) mengeksplorasi *backbone* Transformer tunggal untuk berbagai modalitas visual sekaligus, arah yang sejalan dengan prinsip kesederhanaan arsitektur yang diusung SegFormer.

## Poin untuk Sitasi

Kutip dengan kunci `xie2021segformer`. Ringkasan yang aman dikutip: SegFormer menggabungkan *encoder* Transformer hierarkis MiT tanpa *positional encoding* (memakai Mix-FFN sebagai gantinya) dengan *decoder* MLP ringan, mencapai efisiensi dan ketahanan terhadap korupsi citra yang lebih baik daripada metode CNN dan Transformer segmentasi sebelumnya pada ADE20K dan Cityscapes. Angka yang perlu diverifikasi ulang ke naskah asli sebelum sitasi formal: mIoU SegFormer-B5 pada ADE20K (sumber berbeda melaporkan kisaran 51,0%–51,8% tergantung versi/protokol pengujian skala tunggal-vs-multiskala), jumlah parameter B4 (kisaran 62–64 juta pada sumber berbeda), FPS persis untuk setiap varian pada Cityscapes, angka mIoU per jenis korupsi pada Cityscapes-C, serta hasil lengkap pada COCO-Stuff.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract We present SegFormer, a simple, efficient yet powerful semantic segmentation framework which unifies Transformers with lightweight multilayer perceptron (MLP) decoders. SegFormer has two appealing features: 1) SegFormer comprises a novel hierarchically structured Transformer encoder which outputs multiscale features. It does not need positional encoding, thereby avoiding the interpolation of positional codes which leads to decreased performance when the testing resolution differs from training. 2) SegFormer avoids complex decoders. The proposed MLP decoder aggregates information from different layers, and thus combining both local attention and global attention to render powerful representations. We show that this simple and lightweight design is the key to efficient segmentation on Transformers. We scale our approach up to obtain a series of models from SegFormer-B0 to SegFormer-B5, reaching significantly better performance and efficiency than previous counterparts. For example, SegFormer-B4 achieves 50.3% mIoU on ADE20K with 64M parameters, being 5× smaller and 2.2% better than the previous best method. Our best model, SegFormer-B5, achieves 84.0% mIoU on Cityscapes validation set and shows excellent zero-shot robustness on Cityscapes-C. Code will be released at: github.com/NVlabs/SegFormer.

Introduction

Semantic segmentation is a fundamental task in computer vision and enables many downstream applications. It is related to image classification since it produces per-pixel category prediction instead of image-level prediction. This relationship is pointed out and systematically studied in a seminal work [1], where the authors used fully convolutional networks (FCNs) for semantic segmentation tasks. Since then, FCN has inspired many follow-up works and has become a predominant design choice for dense prediction.

HRNet-W48 + OCR 43.0 70.5M 164.8G 17.0 Since there is a strong relation between classiSegFormer-B4 50.3 64.1M 95.7G 15.4 fication and semantic segmentation, many stateSETR 48.6 318.3M 362.1G 5.4 32 of-the-art semantic segmentation frameworks are 0 50 100 150 200 250 300 350 variants of popular architectures for image classiParams (Millions) Figure 1: Performance vs. model efficiency on ADE20K. All results fication on ImageNet. Therefore, designing backreported with single model and single-scale inference. SegFormer bone architectures has remained an active area are achieves a new state-of-the-art 51.0% mIoU while being significantly in semantic segmentation. Indeed, starting from more efficient than previous methods. early methods using VGGs [1, 2], to the latest methods with significantly deeper and more powerful backbones [3], the evolution of backbones has dramatically pushed the performance boundary of

Related Work

Semantic Segmentation. Semantic segmentation can be seen as an extension of image classification from image level to pixel level. In the deep learning era [12–16], FCN [1] is the fundamental work of semantic segmentation, which is a fully convolution network that performs pixel-to-pixel classification in an end-to-end manner. After that, researchers focused on improving FCN from different aspects such as: enlarging the receptive field [17–19, 5, 2, 4, 20]; refining the contextual information [21– 2

Figure 2: The proposed SegFormer framework consists of two main modules: A hierarchical Transformer encoder to extract coarse and fine features; and a lightweight All-MLP decoder to directly fuse these multi-level features and predict the semantic segmentation mask. “FFN” indicates feed-forward network.

29]; introducing boundary information [30–37]; designing various attention modules [38–46]; or using AutoML technologies [47–51]. These methods significantly improve semantic segmentation performance at the expense of introducing many empirical modules, making the resulting framework computationally demanding and complicated. More recent methods have proved the effectiveness of Transformer-based architectures for semantic segmentation [7, 46]. However, these methods are still computationally demanding. Transformer backbones. ViT [6] is the first work to prove that a pure Transformer can achieve state-of-the-art performance in image classification. ViT treats each image as a sequence of tokens and then feeds them to multiple Transformer layers to make the classification. Subsequently, DeiT [52] further explores a data-efficient training strategy and a distillation approach for ViT. More recent methods such as T2T ViT [53], CPVT [54], TNT [55], CrossViT [56] and LocalViT [57] introduce tailored changes to ViT to further improve image classification performance. Beyond classification, PVT [8] is the first work to introduce a pyramid structure in Transformer, demonstrating the potential of a pure Transformer backbone compared to CNN counterparts in dense prediction tasks. After that, methods such as Swin [9], CvT [58], CoaT [59], LeViT [60] and Twins [10] enhance the local continuity of features and remove fixed size position embedding to improve the performance of Transformers in dense prediction tasks. Transformers for specific tasks. DETR [52] is the first work using Transformers to build an end-toend object detection framework without non-maximum suppression (NMS). Other works have also used Transformers in a variety of tasks such as tracking [61, 62], super-resolution [63], ReID [64], Colorization [65], Retrieval [66] and multi-modal learning [67, 68]. For semantic segmentation, SETR [7] adopts ViT [6] as a backbone to extract features, achieving impressive performance. However, these Transformer-based methods have very low efficiency and, thus, difficult to deploy in real-time applications.

Method

This section introduces SegFormer, our efficient, robust, and powerful segmentation framework without hand-crafted and computationally demanding modules. As depicted in Figure 2, SegFormer consists of two main modules: (1) a hierarchical Transformer encoder to generate high-resolution coarse features and low-resolution fine features; and (2) a lightweight All-MLP decoder to fuse these multi-level features to produce the final semantic segmentation mask. Given an image of size H × W × 3, we first divide it into patches of size 4 × 4. Contrary to ViT that uses patches of size 16 × 16, using smaller patches favors the dense prediction task. We then use these patches as input to the hierarchical Transformer encoder to obtain multi-level features at {1/4, 1/8, 1/16, 1/32} of the original image resolution. We then pass these multi-level features to the W All-MLP decoder to predict the segmentation mask at a H 4 × 4 × Ncls resolution, where Ncls is the 3

number of categories. In the rest of this section, we detail the proposed encoder and decoder designs and summarize the main differences between our approach and SETR. 3.1

where xin is the feature from the self-attention module. Mix-FFN mixes a 3 × 3 convolution and an MLP into each FFN. In our experiments, we will show that a 3 × 3 convolution is sufficient to provide positional information for Transformers. In particular, we use depth-wise convolutions for reducing the number of parameters and improving efficiency. 4

SegFormer incorporates a lightweight decoder consisting only of MLP layers and this avoiding the hand-crafted and computationally demanding components typically used in other methods. The key to enabling such a simple decoder is that our hierarchical Transformer encoder has a larger effective receptive field (ERF) than traditional CNN encoders. The proposed All-MLP decoder consists of four main steps. First, multi-level features Fi from the MiT encoder go through an MLP layer to unify the channel dimension. Then, in a second step, features are up-sampled to 1/4th and concatenated together. Third, a MLP layer is adopted to fuse the concatenated features F . Finally, another MLP layer takes the fused feature to predict the W segmentation mask M with a H 4 × 4 × Ncls resolution, where Ncls is the number of categories. This lets us formulate the decoder as: F̂i = Linear(Ci , C)(Fi ), ∀i W W F̂i = Upsample( × )(F̂i ), ∀i 4 4 F = Linear(4C, C)(Concat(F̂i )), ∀i M = Linear(C, Ncls )(F ),

where M refers to the predicted mask, and Linear(Cin , Cout )(·) refers to a linear layer with Cin and Cout as input and output vector dimensions respectively. Stage-1

Effective Receptive Field Analysis. For semantic segmentation, maintaining large receptive field to include context information has been a central issue [5, 19, 20]. Here, we use effective receptive field (ERF) [70] as a toolkit to visualize and interpret why our MLP decoder design is so effective on Transformers. In Figure 3, we visualize ERFs of the four encoder stages and the decoder heads for both DeepLabv3+ and SegFormer. We can make the following observations:

Figure 3: Effective Receptive Field (ERF) on Cityscapes (average over 100 images). Top row: Deeplabv3+. Bottom row: SegFormer. ERFs of the four stages and the decoder heads of both architectures are visualized. Best viewed with zoom in.

• The ERF of DeepLabv3+ is relatively small even at Stage-4, the deepest stage. • SegFormer’s encoder naturally produces local attentions which resemble convolutions at lower stages, while able to output highly non-local attentions that effectively capture contexts at Stage-4. • As shown with the zoom-in patches in Figure 3, the ERF of the MLP head (blue box) differs from Stage-4 (red box) with a significant stronger local attention besides the non-local attention. The limited receptive field in CNN requires one to resort to context modules such as ASPP [18] that enlarge the receptive field but inevitably become heavy. Our decoder design benefits from the non-local attention in Transformers and leads to a larger receptive field without being complex. The same decoder design, however, does not work well on CNN backbones since the overall receptive field is upper bounded by the limited one at Stage-4, and we will verify this later in Table 1d, More importantly, our decoder design essentially takes advantage of a Transformer induced feature that produces both highly local and non-local attention at the same time. By unifying them, our MLP decoder renders complementary and powerful representations by adding few parameters. This is another key reason that motivated our design. Taking the non-local attention from Stage-4 alone is not enough to produce good results, as will be verified in Table 1d. 3.3

SegFormer contains multiple more efficient and powerful designs compared with SETR [7]: • We only use ImageNet-1K for pre-training. ViT in SETR is pre-trained on larger ImageNet-22K. 5

• SegFormer’s encoder has a hierarchical architecture, which is smaller than ViT and can capture both high-resolution coarse and low-resolution fine features. In contrast, SETR’s ViT encoder can only generate single low-resolution feature map. • We remove Positional Embedding in encoder, while SETR uses fixed shape Positional Embedding which decreases the accuracy when the resolution at inference differs from the training ones. • Our MLP decoder is more compact and less computationally demanding than the one in SETR. This leads to a negligible computational overhead. In contrast, SETR requires heavy decoders with multiple 3×3 convolutions.

Experiments

Experimental Settings

Datasets: We used three publicly available datasets: Cityscapes [71], ADE20K [72] and COCOStuff [73]. ADE20K is a scene parsing dataset covering 150 fine-grained semantic concepts consisting of 20210 images. Cityscapes is a driving dataset for semantic segmentation consisting of 5000 fineannotated high resolution images with 19 categories. COCO-Stuff covers 172 labels and consists of 164k images: 118k for training, 5k for validation, 20k for test-dev and 20k for the test-challenge. Implementation details: We used the mmsegmentation1 codebase and train on a server with 8 Tesla V100. We pre-train the encoder on the Imagenet-1K dataset and randomly initialize the decoder. During training, we applied data augmentation through random resize with ratio 0.5-2.0, random horizontal flipping, and random cropping to 512 × 512, 1024×1024, 512 × 512 for ADE20K, Cityscapes and COCO-Stuff, respectively. Following [9] we set crop size to 640 × 640 on ADE20K for our largest model B5. We trained the models using AdamW optimizer for 160K iterations on ADE20K, Cityscapes, and 80K iterations on COCO-Stuff. Exceptionally, for the ablation studies, we trained the models for 40K iterations. We used a batch size of 16 for ADE20K and COCO-Stuff, and a batch size of 8 for Cityscapes. The learning rate was set to an initial value of 0.00006 and then used a “poly” LR schedule with factor 1.0 by default. For simplicity, we did not adopt widely-used tricks such as OHEM, auxiliary losses or class balance loss. During evaluation, we rescale the short side of the image to training cropping size and keep the aspect ratio for ADE20K and COCO-Stuff. For Cityscapes, we do inference using sliding window test by cropping 1024 × 1024 windows. We report semantic segmentation performance using mean Intersection over Union (mIoU). 4.2

Ablation Studies

Influence of the size of model. We first analyze the effect of increasing the size of the encoder on the performance and model efficiency. Figure 1 shows the performance vs. model efficiency for ADE20K as a function of the encoder size and, Table 1a summarizes the results for the three datasets. The first thing to observe here is the size of the decoder compared to the encoder. As shown, for the lightweight model, the decoder has only 0.4M parameters. For MiT-B5 encoder, the decoder only takes up to 4% of the total number of parameters in the model. In terms of performance, we can observe that, overall, increasing the size of the encoder yields consistent improvements on all the datasets. Our lightweight model, SegFormer-B0, is compact and efficient while maintaining a competitive performance, showing that our method is very convenient for real-time applications. On the other hand, our SegFormer-B5, the largest model, achieves state-of-the-art results on all three datasets, showing the potential of our Transformer encoder. Influence of C, the MLP decoder channel dimension. We now analyze the influence of the channel dimension C in the MLP decoder, see Section 3.2. In Table 1b we show performance, flops, and parameters as a function of this dimension. We can observe that setting C = 256 provides a very competitive performance and computational cost. The performance increases as C increases; however, it leads to larger and less efficient models. Interestingly, this performance plateaus for channel dimensions wider than 768. Given these results, we choose C = 256 for our real-time models SegFormer-B0, B1 and C = 768 for the rest. 1

Table 1: Ablation studies related to model size, encoder and decoder design. (a) Accuracy, parameters and flops as a function of the model size on the three datasets. “SS” and “MS” means single/multi-scale test.

(b) Accuracy as a function of the MLP (c) Mix-FFN vs. positional encoding (PE) for (d) Accuracy on ADE20K of CNN and Transformer encoder with MLP decoder. dimension C in the decoder on ADE20K. different test resolution on Cityscapes. “S4” means stage-4 feature. C Flops ↓ Params ↓ mIoU ↑ Inf Res Enc Type mIoU ↑ Encoder

Table 2: Comparison to state of the art methods on ADE20K and Cityscapes. SegFormer has significant advantages on #Params, #Flops, #Speed and #Accuracy. Note that for SegFormer-B0 we scale the short side of image to {1024, 768, 640, 512} to get speed-accuracy tradeoffs.

Method

Mix-FFN vs. Positional Encoder (PE). In this experiment, we analyze the effect of removing the positional encoding in the Transformer encoder in favor of using the proposed Mix-FFN. To this end, we train Transformer encoders with a positional encoding (PE) and the proposed Mix-FFN and perform inference on Cityscapes with two different image resolutions: 768×768 using a sliding window, and 1024×2048 using the whole image. Table 1c shows the results for this experiment. As shown, for a given resolution, our approach using Mix-FFN clearly outperforms using a positional encoding. Moreover, our approach is less sensitive to differences in the test resolution: the accuracy drops 3.3% when using a positional encoding with a lower resolution. In contrast, when we use the proposed Mix-FFN the performance drop is reduced to only 0.7%. From these results, we can conclude using the proposed Mix-FFN produces better and more robust encoders than those using positional encoding. Effective receptive field evaluation. In Section 3.2, we argued that our MLP decoder benefits from Transformers having a larger effective receptive field compared to other CNN models. To quantify this effect, in this experiment, we compare the performance of our MLP-decoder when used with CNN-based encoders such as ResNet or ResNeXt. As shown in Table 1d, coupling our 7

MLP-decoder with a CNN-based encoder yields a significantly lower accuracy compared to coupling it with the proposed Transformer encoder. Intuitively, as a CNN has a smaller receptive field than the Transformer (see the analysis in Section 3.2), the MLP-decoder is not enough for global reasoning. In contrast, coupling our Transformer encoder with the MLP decoder leads to the best performance. Moreover, for Transformer encoder, it is necessary to combine low-level local features and high-level non-local features instead of only high-level feature. 4.3

Model robustness is important for many safety-critical tasks such as autonomous driving [77]. In this experiment, we evaluate the robustness of SegFormer to common corruptions and perturbations. To 8

Figure 4: Qualitative results on Cityscapes. Compared to SETR, our SegFormer predicts masks with substantially finer details near object boundaries. Compared to DeeplabV3+, SegFormer reduces long-range errors as highlighted in red. Best viewed in screen.

this end, we follow [77] and generate Cityscapes-C, which expands the Cityscapes validation set with 16 types of algorithmically generated corruptions from noise, blur, weather and digital categories. We compare our method to variants of DeeplabV3+ and other methods as reported in [77]. The results for this experiment are summarized in Table 5. Our method significantly outperforms previous methods, yielding a relative improvement of up to 588% on Gaussian Noise and up to 295% on snow weather. The results indicate the strong robustness of SegFormer, which we envision to benefit safety-critical applications where robustness is important. Table 5: Main results on Cityscapes-C. “DLv3+”, “MBv2”, “R” and “X” refer to DeepLabv3+, MobileNetv2, ResNet and Xception. The mIoUs of compared methods are reported from [77]. Method

Conclusion

In this paper, we present SegFormer, a simple, clean yet powerful semantic segmentation method which contains a positional-encoding-free, hierarchical Transformer encoder and a lightweight AllMLP decoder. It avoids common complex designs in previous methods, leading to both high efficiency and performance. SegFormer not only achieves new state of the art results on common datasets, but also shows strong zero-shot robustness. We hope our method can serve as a solid baseline for semantic segmentation and motivate further research. One limitation is that although our smallest 3.7M parameters model is smaller than the known CNN’s model, it is unclear whether it can work well in a chip of edge device with only 100k memory. We leave it for future work.

Acknowledgement We thank Ding Liang, Zhe Chen and Yaojun Liu for insightful discussion without which this paper would not be possible.

In this section, we list some important hyper-parameters of our Mix Transformer (MiT) encoder. By changing these parameters, we can easily scale up our encoder from B0 to B5. In summary, the hyper-parameters of our MiT are listed as follows: • Ki : the patch size of the overlapping patch embedding in Stage i; 9

In Figure 5, we present more qualitative results on Cityscapes, ADE20K and COCO-Stuff, compared with SETR and DeepLabV3+. Compared to SETR, our SegFormer predicts masks with significantly finer details near object boundaries because our Transformer encoder can capture much higher resolution features than SETR, which preserves more detailed texture information. Compared to DeepLabV3+, SegFormer reduces long-range errors benefit from the larger effective receptive field of Transformer encoder than ConvNet.

In Figure 6, we select some representative images and effective receptive field (ERF) of DeepLabV3+ and SegFormer. Beyond larger ERF, the ERF of SegFormer is more sensitive to the context of the image. We see SegFormer’s ERF learned the pattern of roads, cars, and buildings, while DeepLabV3+’s ERF shows a relatively fixed pattern. The results also indicate that our Transformer encoder has a stronger feature extraction ability than ConvNets.

In this section, we detailed show the zero-shot robustness compared with SegFormer and DeepLabV3+. Following [77], we test 3 severities for 4 kinds of “Noise” and 5 severities for the rest 12 kinds of corruptions and perturbations. As shown in Figure 7, with severity increase, DeepLabV3+ shows a considerable performance degradation. In contrast, the performance of SegFormer is relatively stable. Moreover, SegFormer has significant advantages over DeepLabV3+ on all corruptions/perturbations and all severities, demonstrating excellent zero-shot robustness.

Table 6: Detailed settings of MiT series. Our design follows the principles of ResNet [12]. (1) the channel dimension increase while the spatial resolution shrink with the layer goes deeper. (2) Stage 3 is assigned to most of the computation cost.

Figure 5: Qualitative results on Cityscapes, ADE20K and COCO-Stuff. First row: Cityscapes. Second row: ADE20K. Third row: COCO-Stuff. Zoom in for best view.

Figure 6: Effective Receptive Field on Cityscapes. ERFs of the four stages and the decoder heads of both architectures are visualized.

Figure 7: Comparison of zero shot robustness on Cityscapes-C between SegFormer and DeepLabV3+. Blue line is SegFormer and orange line is DeepLabV3+. X-Axis means corrupt severity and Y-Axis is mIoU. Following[77], we test 3 severities for “Noise” and 5 severities for the rest.
