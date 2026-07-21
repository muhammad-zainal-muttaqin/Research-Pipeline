# 165 - DETRs with Collaborative Hybrid Assignments Training

## Metadata Ringkas
| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `zong2023codetr` |
| Judul asli | DETRs with Collaborative Hybrid Assignments Training |
| Penulis | Zhuofan Zong, Guanglu Song, Yu Liu |
| Tahun | 2023 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema | Fondasi RGB |

## Tautan Akses
- arXiv: https://arxiv.org/abs/2211.12860
- Google Scholar: https://scholar.google.com/scholar?q=DETRs%20with%20Collaborative%20Hybrid%20Assignments%20Training
- Semantic Scholar: https://www.semanticscholar.org/search?q=DETRs%20with%20Collaborative%20Hybrid%20Assignments%20Training&sort=relevance

## Gambaran Umum
*DEtection TRansformer* (DETR) memperkenalkan paradigma deteksi objek *end-to-end* bebas *Non-Maximum Suppression* (NMS) berbasis pencocokan satu-ke-satu (*one-to-one set matching*). Namun, pencocokan ini menyebabkan supervisi jarang (*sparse supervision*) pada keluaran *encoder*. Hanya sedikit kueri yang mendapat label positif saat pelatihan, menghambat pembelajaran fitur diskriminatif oleh *encoder* dan memperlambat konvergensi.

*Collaborative Hybrid Assignments Training* (Co-DETR) mengatasi masalah ini dengan mengintegrasikan beberapa kepala bantu (*auxiliary heads*) paralel bersupervisi satu-ke-banyak (*one-to-many*) seperti *Adaptive Training Sample Selection* (ATSS) dan Faster R-CNN selama pelatihan. Skema ini memaksa *encoder* mempelajari fitur spasial yang padat. Koordinat positif dari kepala bantu diekstraksi menjadi kueri positif kustom (*customized positive queries*) untuk mempercepat pembelajaran atensi *decoder*. Saat inferensi, seluruh kepala bantu dibuang sehingga model beroperasi tanpa beban komputasi tambahan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
DETR (022) mengubah paradigma deteksi objek dengan merumuskan tugas sebagai prediksi himpunan langsung via pencocokan bipartit satu-ke-satu. Pendekatan ini mengeliminasi komponen NMS buatan tangan dan kotak acuan (*anchor box*). Namun, DETR membutuhkan konvergensi pelatihan yang sangat lambat (hingga 500 epoch) dan kinerjanya tertinggal dari detektor berbasis CNN pada skala tertentu.

Upaya seperti *Deformable DETR* (023) dan *DN-DETR* (159) mempercepat konvergensi pada sisi *decoder* lewat atensi lokal terdeformasi dan latihan denoising. Namun, masalah kurangnya efisiensi fitur *encoder* belum teratasi. Pada DETR standar, representasi spasial *encoder* disupervisi secara tidak langsung melalui *decoder* satu-ke-satu. Karena jumlah objek dalam citra sedikit dibanding total piksel, hanya sebagian kecil token fitur *encoder* yang menerima gradien supervisi positif. Token lainnya dipaksa menjadi latar belakang (*background*). Supervisi yang jarang ini menghambat *encoder* mempelajari fitur visual diskriminatif. Sebaliknya, detektor konvensional menggunakan penetapan satu-ke-banyak (*one-to-many*) di mana beberapa *anchor* dipasangkan ke satu objek target, menghasilkan supervisi yang jauh lebih padat pada fitur representasional.

## Ide Utama
Ide utama Co-DETR adalah menggabungkan keunggulan supervisi padat skema satu-ke-banyak (*one-to-many*) tradisional untuk melatih *encoder*, sementara *decoder* utama tetap menggunakan skema satu-ke-satu (*one-to-one*) demi mempertahankan deteksi *end-to-end* tanpa NMS. Pendekatan ini dinamakan pelatihan kolaboratif hibrida.

Fitur multi-skala hasil *encoder* dikirim ke kepala *decoder* DETR utama dan beberapa kepala bantu satu-ke-banyak secara paralel. Kepala bantu bertindak sebagai pengawas tambahan yang memaksa *encoder* mempelajari fitur di seluruh area potensial objek, bukan hanya representasi tunggal dari pencocokan Hungarian. Umpan balik gradien dari kepala-kepala bantu diakumulasikan untuk memperbarui parameter *encoder*. Selain itu, koordinat spasial positif kepala bantu diekstraksi menjadi kueri tambahan untuk mempercepat pembelajaran *decoder*. Seluruh kepala bantu ini dibuang saat inferensi, sehingga model hasil pelatihan tetap berupa detektor DETR standar yang efisien tanpa parameter tambahan pada data uji.

## Cara Kerja Langkah demi Langkah

### Aliran Data Utama dan Ekstraksi Fitur Multi-Skala
Aliran data dimulai dengan memproses citra masukan melalui *backbone* untuk menghasilkan peta fitur multi-skala. Pada citra masukan beresolusi $800 \times 800$ piksel, *backbone* mengekstrak fitur pada resolusi spasial yang menurun, misalnya tingkat C3 ($100 \times 100$ piksel), C4 ($50 \times 50$ piksel), dan C5 ($25 \times 25$ piksel). Fitur multi-skala ini diratakan dan dimasukkan ke dalam *encoder* Transformer (seperti *Deformable Encoder*) untuk menghasilkan representasi fitur terenkode dengan dimensi spasial yang sama.

```
                             ┌──────────────┐
                             │ Citra Input  │
                             └──────┬───────┘
                                    ▼
                             ┌──────────────┐
                             │   Backbone   │
                             └──────┬───────┘
                                    ▼
                             ┌──────────────┐
                             │   Encoder    │
                             └───┬───┬───┬──┘
                                 │   │   │  (Fitur Encoder Berbagi)
        ┌────────────────────────┘   │   └───────────────────────┐
        ▼                            ▼                           ▼
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│  Aux Head 1  │             │  Aux Head 2  │             │   Decoder    │
│ (One-to-Many)│             │ (One-to-Many)│             │ (One-to-One) │
│  [ATSS/FCOS] │             │ [Faster RCN] │             └──────┬───────┘
└──────┬───────┘             └──────┬───────┘                    │
       │                            │                            │
       └──────────────┬─────────────┘                            │
                      ▼                                          │
       (Koordinat Positif Diekstraksi)                           │
                      │                                          │
                      ▼                                          │
       ┌──────────────────────────────┐                          │
       │ Customized Positive Queries  │                          │
       └──────────────┬───────────────┘                          │
                      └──────────────────────────────────────────┼───┐
                                                                 ▼   ▼
                                                            ┌──────────────┐
                                                            │ Prediksi Box │
                                                            └──────────────┘
                                                             (Hanya Cabang
                                                             Utama Digunakan
                                                             saat Inferensi)
```

### Pelatihan Kolaboratif dengan Kepala Bantu Satu-ke-Banyak
Fitur terenkode multi-skala dari *encoder* didistribusikan ke kepala detektor utama (DETR) dan $M$ kepala bantu paralel. Setiap kepala bantu dikonfigurasi menggunakan metode deteksi tradisional seperti ATSS (menetapkan sampel positif secara adaptif berdasarkan kalkulasi statistik jarak terdekat dan IoU) atau FCOS (pemetaan objek secara *anchor-free* berdasarkan pusat piksel).

Sebagai contoh, jika menggunakan kepala ATSS, metode ini menetapkan beberapa token fitur spasial dekat pusat objek sebagai sampel positif. Ini memberikan pengawasan padat kepada *encoder* karena banyak token didorong untuk memprediksi kelas dan penyimpangan (*offset*) kotak pembatas (*bounding box*) objek target. Setiap kepala bantu menghitung nilai kerugiannya sendiri secara independen.

### Pembuatan Kueri Positif Kustom untuk Decoder
Selain memberikan supervisi gradien pada *encoder*, kepala bantu membantu mempercepat pelatihan *decoder*. Dari setiap kepala bantu, koordinat spasial ($x, y, w, h$) yang ditetapkan sebagai sampel positif diekstraksi. Koordinat ini merepresentasikan area yang sangat mungkin mengandung objek target (*foreground*).

Koordinat positif tersebut ditransformasikan menjadi kueri posisi (*positional queries*) tambahan untuk *decoder* utama. Pada fase pelatihan, $N$ buah kueri objek acak pada *decoder* ditambahkan dengan kueri positif kustom ini. Dengan menyajikan kueri yang terarah langsung ke lokasi objek positif kepada *decoder*, beban *decoder* dalam mempelajari atensi silang (*cross-attention*) berkurang signifikan, mempercepat konvergensi.

### Formulasi Fungsi Rugi Total
Fungsi rugi total $\mathcal{L}_{\text{total}}$ yang dioptimalkan selama pelatihan dirumuskan sebagai akumulasi bobot dari rugi detektor utama dan rugi seluruh kepala bantu:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{main}} + \sum_{i=1}^{M} \lambda_i \mathcal{L}_{\text{aux}}^{(i)}$$

Di mana $\mathcal{L}_{\text{main}}$ melambangkan fungsi rugi detektor DETR utama (mencakup *Hungarian classification*, *L1 regression*, dan *GIoU loss*). $\mathcal{L}_{\text{aux}}^{(i)}$ menyatakan fungsi rugi kepala bantu ke-$i$ (klasifikasi menggunakan *Focal Loss* dan regresi kotak pembatas menggunakan kombinasi *L1* dan *GIoU loss*). Parameter $\lambda_i$ bertindak sebagai koefisien bobot penyeimbang kontribusi setiap kepala bantu, yang biasanya diatur mendekati $1,0$.

### Proses Inferensi Tanpa Overhead
Setelah pelatihan selesai, seluruh kepala bantu dan mekanisme kueri positif kustom dilepaskan. Bobot parameter pada *encoder* dan *decoder* utama yang telah dioptimalkan disimpan. Pada fase inferensi, citra masukan hanya melewati *backbone*, *encoder*, and *decoder* utama menggunakan kueri standar. Karena jalur bantu tidak diproses, waktu komputasi, penggunaan memori GPU, dan latensi inferensi persis sama dengan detektor DETR dasar.

## Eksperimen dan Hasil
Evaluasi eksperimental Co-DETR dilakukan pada dataset MS COCO 2017 (118 ribu citra latih, 5 ribu citra validasi, dan 20 ribu citra *test-dev*). Arsitektur dasar yang diuji mencakup *DAB-DETR*, *Deformable DETR*, dan detektor *DINO*.

Pada pengujian menggunakan *Deformable DETR* dengan *backbone* ResNet-50 pada skema pelatihan singkat 12 epoch, Co-DETR meningkatkan performa dari 43,8% *mean Average Precision* (AP) menjadi 49,6% AP (+5,8% AP). Untuk skema pelatihan 36 epoch, performa meningkat dari 46,9% AP menjadi 50,1% AP (+3,2% AP). Peningkatan tinggi pada epoch awal membuktikan bahwa Co-DETR berhasil mempercepat konvergensi melalui supervisi padat pada fitur *encoder*.

Ketika diintegrasikan dengan detektor SOTA *DINO-Deformable-DETR* berbasis *Swin-L*, Co-DETR meningkatkan performa pada data validasi COCO dari 58,5% AP menjadi 59,5% AP (+1,0% AP). Dengan memanfaatkan *backbone* ViT-L (304 juta parameter) yang dilatih awal pada dataset Objects365, Co-DETR mencapai 66,0% AP pada COCO *test-dev* dan 67,9% AP pada LVIS val. Hasil ini menetapkan standar kinerja baru saat publikasi dan menunjukkan skalabilitas metode ke arsitektur model besar tanpa menambah beban komputasi ketika digunakan pada sistem produksi.

## Kelebihan dan Keterbatasan
Kelebihan utama Co-DETR terletak pada efisiensinya yang asimetris. Model diuntungkan oleh supervisi padat satu-ke-banyak selama pelatihan, namun tetap mempertahankan kesederhanaan arsitektur satu-ke-satu tanpa NMS saat inferensi. Hal ini sangat berguna untuk penerapan praktis karena tidak menambah operasi matematika (*FLOPs*) atau latensi inferensi pada perangkat target.

Namun, dari sisi rekayasa, keterbatasan utama Co-DETR adalah kebutuhan memori GPU (*VRAM*) yang melonjak selama pelatihan karena pengaktifan beberapa kepala bantu secara paralel di atas fitur multi-skala. Secara konseptual, jumlah kepala bantu juga memiliki batas optimal sekitar 4 kepala. Menambahkan lebih dari 6 kepala bantu justru menurunkan akurasi akibat timbulnya konflik penetapan label (*label assignment conflict*). Konflik ini terjadi ketika satu token fitur menerima instruksi gradien kontradiktif dari beberapa kepala bantu yang menerapkan kriteria sampel positif-negatif berbeda, menghambat pembaruan bobot *encoder*.

## Kaitan dengan Bab Lain
Co-DETR memiliki keterkaitan erat dengan beberapa bab dalam silsilah deteksi objek berbasis Transformer dan CNN:
- **[DETR (022)](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md)**: Sebagai fondasi utama, DETR memperkenalkan paradigma deteksi *end-to-end* bebas NMS. Co-DETR secara langsung mengatasi kelemahan mendasar DETR berupa supervisi yang jarang pada *encoder*.
- **[Deformable DETR (023)](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md)**: Co-DETR sering menggunakan Deformable DETR sebagai arsitektur dasar. Pembatasan atensi pada Deformable DETR dikombinasikan dengan supervisi padat Co-DETR menghasilkan konvergensi yang sangat cepat.
- **[Vision Transformer (ViT) (024)](./024%20-%202021%20-%20Vision%20Transformer%20(ViT)%20-%20Fondasi%20RGB.md)** dan **[Swin Transformer (025)](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)**: Kedua arsitektur ini bertindak sebagai *backbone* ekstraksi fitur yang digunakan oleh Co-DETR untuk mencapai performa akurasi puncak di atas 66,0% AP pada COCO.
- **[DINO detector (158)](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)**: DINO merupakan salah satu model detektor dasar yang diintegrasikan dengan skema pelatihan Co-DETR untuk mencatatkan rekor akurasi tertinggi pada masanya.
- **[DN-DETR (159)](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)**: Sementara DN-DETR berfokus pada stabilisasi *decoder* melalui latihan denoising, Co-DETR melengkapinya dengan memperkuat representasi *encoder* menggunakan skema hibrida kolaboratif.
- **[RT-DETR (155)](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)**: RT-DETR berfokus pada kecepatan inferensi waktu nyata dengan merancang ulang *encoder*. Sebaliknya, Co-DETR berfokus pada akurasi maksimal dengan mengoptimalkan pelatihan *encoder* yang kompleks dan membuang seluruh modul tambahan saat inferensi.

## Poin untuk Sitasi
Kunci BibTeX: `zong2023codetr`

Ringkasan untuk sitasi:
"Co-DETR memperkenalkan kerangka kerja pelatihan kolaboratif hibrida yang menempatkan beberapa kepala bantu satu-ke-banyak (seperti ATSS dan Faster R-CNN) secara paralel di atas *encoder* DETR selama fase pelatihan. Metode ini memperkaya supervisi fitur *encoder* dan mempercepat konvergensi *decoder* melalui ekstraksi kueri positif kustom, tanpa memberikan beban komputasi tambahan atau parameter ekstra pada saat proses inferensi dijalankan."

Catatan verifikasi:
"Perlu diverifikasi apakah hasil 66,0% AP pada COCO *test-dev* menggunakan model ViT-L melibatkan teknik penambahan skala gambar masukan bervariasi (*multi-scale testing*) dan *Test-Time Augmentation* (TTA), serta pastikan kecukupan kapasitas memori GPU saat mereproduksi skema latihan dengan 4 kepala bantu paralel."

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract

In this paper, we provide the observation that too few queries assigned as positive samples in DETR with oneto-one set matching leads to sparse supervision on the encoder’s output which considerably hurt the discriminative feature learning of the encoder and vice visa for attention learning in the decoder. To alleviate this, we present a novel collaborative hybrid assignments training scheme, namely Co-DETR, to learn more efficient and effective DETR-based detectors from versatile label assignment manners. This new training scheme can easily enhance the encoder’s learning ability in end-to-end detectors by training the multiple parallel auxiliary heads supervised by one-to-many label assignments such as ATSS and Faster RCNN. In addition, we conduct extra customized positive queries by extracting the positive coordinates from these auxiliary heads to improve the training efficiency of positive samples in the decoder. In inference, these auxiliary heads are discarded and thus our method introduces no additional parameters and computational cost to the original detector while requiring no hand-crafted non-maximum suppression (NMS). We conduct extensive experiments to evaluate the effectiveness of the proposed approach on DETR variants, including DAB-DETR, Deformable-DETR, and DINO-DeformableDETR. The state-of-the-art DINO-Deformable-DETR with Swin-L can be improved from 58.5% to 59.5% AP on COCO val. Surprisingly, incorporated with ViT-L backbone, we achieve 66.0% AP on COCO test-dev and 67.9% AP on LVIS val, outperforming previous methods by clear margins with much fewer model sizes. Codes are available at https://github.com/Sense-X/Co-DETR.

Figure 1. Performance of models with ResNet-50 on COCO val. Co-DETR outperforms other counterparts by a large margin.

a series of variants [31, 37, 44] such as ATSS [41], RetinaNet [21], FCOS [32], and PAA [17] lead to the significant breakthrough of object detection task. One-to-many label assignment is the core scheme of them, where each groundtruth box is assigned to multiple coordinates in the detector’s output as the supervised target cooperated with proposals [11, 27], anchors [21] or window centers [32]. Despite their promising performance, these detectors heavily rely on many hand-designed components like a non-maximum suppression procedure or anchor generation [1]. To conduct a more flexible end-to-end detector, DEtection TRansformer (DETR) [1] is proposed to view the object detection as a set prediction problem and introduce the one-to-one set matching scheme based on a transformer encoder-decoder architecture. In this manner, each ground-truth box will only be assigned to one specific query, and multiple handdesigned components that encode prior knowledge are no longer needed. This approach introduces a flexible detection pipeline and encourages many DETR variants to further improve it. However, the performance of the vanilla end-to-end object detector is still inferior to the traditional detectors with one-to-many label assignments.

1. Introduction Object detection is a fundamental task in computer vision, which requires us to localize the object and classify its category. The seminal R-CNN families [11, 14, 27] and * Corresponding author.

0.6 IoF

0.6 IoF

Figure 2. IoF-IoB curves for the feature discriminability score in the encoder and attention discriminability score in the decoder.

In this paper, we try to make DETR-based detectors superior to conventional detectors while maintaining their end-to-end merit. To address this challenge, we focus on the intuitive drawback of one-to-one set matching that it explores less positive queries. This will lead to severe inefficient training issues. We detailedly analyze this from two aspects, the latent representation generated by the encoder and the attention learning in the decoder. We first compare the discriminability score of the latent features between the Deformable-DETR [43] and the one-to-many label assignment method where we simply replace the decoder with the ATSS head. The feature l2 -norm in each spatial coordinate is utilized to represent the discriminability score. Given the encoder’s output F ∈ RC×H×W , we can obtain the discriminability score map S ∈ R1×H×W . The object can be better detected when the scores in the corresponding area are higher. As shown in Figure 2, we demonstrate the IoF-IoB curve (IoF: intersection over foreground, IoB: intersection over background) by applying different thresholds on the discriminability scores (details in Section 3.4). The higher IoF-IoB curve in ATSS indicates that it’s easier to distinguish the foreground and background. We further visualize the discriminability score map S in Figure 3. It’s obvious that the features in some salient areas are fully activated in the one-to-many label assignment method but less explored in one-to-one set matching. For the exploration of decoder training, we also demonstrate the IoF-IoB curve of the cross-attention score in the decoder based on the Deformable-DETR and the Group-DETR [5] which introduces more positive queries into the decoder. The illustration in Figure 2 shows that too few positive queries also influence attention learning and increasing more positive queries in the decoder can slightly alleviate this. This significant observation motivates us to present a simple but effective method, a collaborative hybrid assignment training scheme (Co-DETR). The key insight of CoDETR is to use versatile one-to-many label assignments to improve the training efficiency and effectiveness of both the encoder and decoder. More specifically, we integrate the auxiliary heads with the output of the transformer encoder. These heads can be supervised by versatile one-to-many label assignments such as ATSS [41], FCOS [32], and Faster RCNN [27]. Different label assignments enrich the super-

2. Related Works One-to-many label assignment. For one-to-many label assignment in object detection, multiple box candidates can be assigned to the same ground-truth box as positive samples in the training phase. In classic anchor-based detectors, such as Faster-RCNN [27] and RetinaNet [21], the sample selection is guided by the predefined IoU threshold and matching IoU between anchors and annotated boxes. The anchor-free FCOS [32] leverages the center priors and as2

Figure 4. Framework of our Collaborative Hybrid Assignment Training. The auxiliary branches are discarded during evaluation.

tive hybrid assignments training scheme and the customized positive queries generation. We will detailedly describe these modules and give insights why they can work well.

signs spatial locations near the center of each bounding box as positives. Moreover, the adaptive mechanism is incorporated into one-to-many label assignments to overcome the limitation of fixed label assignments. ATSS [41] performs adaptive anchor selection by the statistical dynamic IoU values of top-k closest anchors. PAA [17] adaptively separates anchors into positive and negative samples in a probabilistic manner. In this paper, we propose a collaborative hybrid assignment scheme to improve encoder representations via auxiliary heads with one-to-many label assignments. One-to-one set matching. The pioneering transformerbased detector, DETR [1], incorporates the one-to-one set matching scheme into object detection and performs fully end-to-end object detection. The one-to-one set matching strategy first calculates the global matching cost via Hungarian matching and assigns only one positive sample with the minimum matching cost for each ground-truth box. DNDETR [18] demonstrates the slow convergence results from the instability of one-to-one set matching, thus introducing denoising training to eliminate this issue. DINO [39] inherits the advanced query formulation of DAB-DETR [23] and incorporates an improved contrastive denoising technique to achieve state-of-the-art performance. Group-DETR [5] constructs group-wise one-to-many label assignment to exploit multiple positive object queries, which is similar to the hybrid matching scheme in H-DETR [16]. In contrast with the above follow-up works, we present a new perspective of collaborative optimization for one-to-one set matching.

3.2. Collaborative Hybrid Assignments Training To alleviate the sparse supervision on the encoder’s output caused by the fewer positive queries in the decoder, we incorporate versatile auxiliary heads with different one-tomany label assignment paradigms, e.g., ATSS, and Faster R-CNN. Different label assignments enrich the supervisions on the encoder’s output which forces it to be discriminative enough to support the training convergence of these heads. Specifically, given the encoder’s latent feature F, we firstly transform it to the feature pyramid {F1 , · · · , FJ } via the multi-scale adapter where J indicates feature map with 22+J downsampling stride. Similar to ViTDet [20], the feature pyramid is constructed by a single feature map in the single-scale encoder, while we use bilinear interpolation and 3 × 3 convolution for upsampling. For instance, with the single-scale feature from the encoder, we successively apply downsampling (3×3 convolution with stride 2) or upsampling operations to produce a feature pyramid. As for the multi-scale encoder, we only downsample the coarsest feature in the multi-scale encoder features F to build the feature pyramid. Defined K collaborative heads with corresponding label assignment manners Ak , for the i-th collaborative head, {F1 , · · · , FJ } is sent to it to obtain the predictions P̂i . At the i-th head, Ai is used to compute the supervised targets for the positive and negative samples in Pi . Denoted G as the ground-truth set, this procedure can be formulated as:

3. Method 3.1. Overview Following the standard DETR protocol, the input image is fed into the backbone and encoder to generate latent features. Multiple predefined object queries interact with them in the decoder via cross-attention afterwards. We introduce Co-DETR to improve the feature learning in the encoder and the attention learning in the decoder via the collabora-

the set of spatial positive coordinates. Pi and Pi are the supervised targets in the corresponding coordinates, including the categories and regressed offsets. To be specific, we describe the detailed information about each variable in Table 1. The loss functions can be defined as: {pos}

e i,l refers to the output predictions of the l-th decoder layer P in the i-th auxiliary branch. Finally, the training objective for Co-DETR is:

Note that the regression loss is discarded for negative samples. The training objective of the optimization for K auxiliary heads is formulated as follows: Lenc =

where Ledec stands for the loss in the original one-to-one set l matching branch [1], λ1 and λ2 are the coefficient balancing the losses.

3.4. Why Co-DETR works

3.3. Customized Positive Queries Generation

Co-DETR leads to evident improvement to the DETRbased detectors. In the following, we try to investigate its effectiveness qualitatively and quantitatively. We conduct detailed analysis based on Deformable-DETR with ResNet50 [15] backbone using the 36-epoch setting. Enrich the encoder’s supervisions. Intuitively, too few positive queries lead to sparse supervisions as only one query is supervised by regression loss for each ground-truth. The positive samples in one-to-many label assignment manners receive more localization supervisions to help enhance the latent feature learning. To further explore how the sparse supervisions impede the model training, we detailedly investigate the latent features produced by the encoder. We introduce the IoF-IoB curve to quantize the discriminability score of the encoder’s output. Specifically, given the latent feature F of the encoder, inspired by the feature visualization in Figure 3, we compute the IoF (intersection over foreground) and IoB (intersection over background). Given the encoder’s feature Fj ∈ RC×Hj ×Wj at level j, we first calculate the l2 -norm Fbj ∈ R1×Hj ×Wj and resize it to the image size H × W . The discriminability score D(F) is computed by averaging the scores from all levels:

In the one-to-one set matching paradigm, each groundtruth box will only be assigned to one specific query as the supervised target. Too few positive queries lead to inefficient cross-attention learning in the transformer decoder as shown in Figure 2. To alleviate this, we elaborately generate sufficient customized positive queries according to the label assignment Ai in each auxiliary head. Specifically, given {pos} the positive coordinates set Bi ∈ RMi ×4 in the i-th auxiliary head, where Mi is the number of positive samples, the extra customized positive queries Qi ∈ RMi ×C can be generated by: {pos}

)) + Linear(E({F∗ }, {pos})). (4) where PE(·) stands for positional encodings and we select the corresponding features from E(·) according to the index pair (j, positive coordinates or negative coordinates in Fj ). As a result, there are K + 1 groups of queries that contribute to a single one-to-one set matching branch and K branches with one-to-many label assignments during training. The auxiliary one-to-many label assignment branches share the same parameters with L decoders layers in the original main branch. All the queries in the auxiliary branch are regarded as positive queries, thus the matching process is discarded. To be specific, the loss of the l-th decoder layer Qi = Linear(PE(Bi

process. Furthermore, in order to quantify how well crossattention is being optimized, we also calculate the IoF-IoB curve for attention score. Similar to the feature discriminability score computation, we set different thresholds for attention score to get multiple IoF-IoB pairs. The comparisons between Deformable-DETR, Group-DETR, and CoDeformable-DETR can be viewed in Figure 2. We find that the IoF-IoB curves of DETRs with more positive queries are generally above Deformable-DETR, which is consistent with our motivation.

3.5. Comparison with other methods

Differences between our method and other counterparts. Group-DETR, H-DETR, and SQR [2] perform oneto-many assignments by one-to-one matching with duplicate groups and repeated ground-truth boxes. Co-DETR explicitly assigns multiple spatial coordinates as positives for each ground truth. Accordingly, these dense supervision signals are directly applied to the latent feature map to enable it more discriminative. By contrast, Group-DETR, HDETR, and SQR lack this mechanism. Although more positive queries are introduced in these counterparts, the oneto-many assignments implemented by Hungarian Matching still suffer from the instability issues of one-to-one matching. Our method benefits from the stability of off-theshelf one-to-many assignments and inherits their specific matching manner between positive queries and ground-truth boxes. Group-DETR and H-DETR fail to reveal the complementarities between one-to-one matching and traditional one-to-many assignment. To our best knowledge, we are the first to give the quantitative and qualitative analysis on the detectors with the traditional one-to-many assignment and one-to-one matching. This helps us better understand their differences and complementarities so that we can naturally improve the DETR’s learning ability by leveraging off-theshelf one-to-many assignment designs without requiring additional specialized one-to-many design experience. No negative queries are introduced in the decoder. Duplicate object queries inevitably bring large amounts of negative queries for the decoder and a significant increase in GPU memory. However, our method only processes the positive coordinates in the decoder, thus consuming less memory as shown in Table 7.

Figure 5. The instability (IS) [18] of Deformable-DETR and CoDeformable-DETR on COCO dataset. These detectors are trained for 12 epochs with ResNet-50 backbones.

where the resize operation is omitted. We visualize the discriminability scores of ATSS, Deformable-DETR, and our Co-Deformable-DETR in Figure 3. Compared with Deformable-DETR, both ATSS and Co-Deformable-DETR own stronger ability to distinguish the areas of key objects, while Deformable-DETR is almost disturbed by the background. Consequently, we define the indicators for foreground and background as 1(D(F) > S) ∈ RH×W and 1(D(F) < S) ∈ RH×W , respectively. S is a predefined score thresh, 1(x) is 1 if x is true and 0 otherwise. As for g the mask of foreground Mf g ∈ RH×W , the element Mfh,w is 1 if the point (h, w) is inside the foreground and 0 otherwise. The area of intersection over foreground (IoF) I f g can be computed as: PH PW fg h=1 w=1 (1(D(Fh,w ) > S) · Mh,w ) fg I = . (8) PH PW fg h=1 w=1 Mh,w Concretely, we compute the area of intersection over background areas (IoB) in a similar way and plot the curve IoF and IoB by varying S in Figure 2. Obviously, ATSS and Co-Deformable-DETR obtain higher IoF values than both Deformable-DETR and Group-DETR under the same IoB values, which demonstrates the encoder representations benefit from the one-to-many label assignment. Improve the cross-attention learning by reducing the instability of Hungarian matching. Hungarian matching is the core scheme in one-to-one set matching. Cross-attention is an important operation to help the positive queries encode abundant object information. It requires sufficient training to achieve this. We observe that the Hungarian matching introduces uncontrollable instability since the ground-truth assigned to a specific positive query in the same image is changing during the training process. Following [18], we present the comparison of instability in Figure 5, where we find our approach contributes to a more stable matching

4. Experiments 4.1. Setup Datasets and Evaluation Metrics. Our experiments are conducted on the MS COCO 2017 dataset [22] and LVIS v1.0 dataset [12]. The COCO dataset consists of 115K labeled images for training and 5K images for validation. We report the detection results by default on the val subset. The results of our largest model evaluated on the 5

Method

Method

Table 3. Results of strong baselines on COCO val. Methods with † use 5 feature levels. ‡ refers to Swin-L backbone.

test-dev (20K images) are also reported. LVIS v1.0 is a large-scale and long-tail dataset with 1203 categories for large vocabulary instance segmentation. To verify the scalability of Co-DETR, we further apply it to a large-scale object detection benchmark, namely Objects365 [30]. There are 1.7M labeled images used for training and 80K images for validation in the Objects365 dataset. All results follow the standard mean Average Precision(AP) under IoU thresholds ranging from 0.5 to 0.95 at different object scales.

Implementation Details. We incorporate our Co-DETR into the current DETR-like pipelines and keep the training setting consistent with the baselines. We adopt ATSS and Faster-RCNN as the auxiliary heads for K = 2 and only keep ATSS for K = 1. More details about our auxiliary heads can be found in the supplementary materials. We choose the number of learnable object queries to 300 and set {λ1 , λ2 } to {1.0, 2.0} by default. For Co-DINODeformable-DETR++, we use large-scale jitter with copypaste [10].

4.3. Comparisons with the state-of-the-art We apply our method with K = 2 to DeformableDETR++ and DINO. Besides, the quality focal loss [19] and NMS are adopted for our Co-DINO-Deformable-DETR. We report the comparisons on COCO val in Table 4. Compared with other competitive counterparts, our method converges much faster. For example, Co-DINO-DeformableDETR readily achieves 52.1% AP when using only 12 epochs with ResNet-50 backbone. Our method with SwinL can obtain 58.9% AP for 1× scheduler, even surpassing other state-of-the-art frameworks on 3× scheduler. More importantly, our best model Co-DINO-DeformableDETR++ achieves 54.8% AP with ResNet-50 and 60.7% AP with Swin-L under 36-epoch training, outperforming all existing detectors with the same backbone by clear margins. To further explore the scalability of our method, we extend the backbone capacity to 304 million parameters. This large-scale backbone ViT-L [7] is pre-trained using a selfsupervised learning method (EVA-02 [8]). We first pre-train Co-DINO-Deformable-DETR with ViT-L on Objects365 for 26 epochs, then fine-tune it on the COCO dataset for 12 epochs. In the fine-tuning stage, the input resolution is randomly selected between 480×2400 and 1536×2400. The detailed settings are available in supplementary materials. Our results are evaluated with test-time augmentation. Table 5 presents the state-of-the-art comparisons on the

4.2. Main Results In this section, we empirically analyze the effectiveness and generalization ability of Co-DETR on different DETR variants in Table 2 and Table 3. All results are reproduced using mmdetection [4]. We first apply the collaborative hybrid assignments training to single-scale DETRs with C5 features. Surprisingly, both Conditional-DETR and DAB-DETR obtain 2.4% and 2.3% AP gains over the baselines with a long training schedule. For DeformableDETR with multi-scale features, the detection performance is significantly boosted from 37.1% to 42.9% AP. The overall improvements (+3.2% AP) still hold when the training time is increased to 36 epochs. Moreover, we conduct experiments on the improved Deformable-DETR (denoted as Deformable-DETR++) following [16], where a +2.4% AP gain is observed. The state-of-the-art DINO-Deformable6

Method

Table 4. Comparison to the state-of-the-art DETR variants on COCO val.

Method

Method

COCO test-dev benchmark. With much fewer model sizes (304M parameters), Co-DETR sets a new record of 66.0% AP on COCO test-dev, outperforming the previous best model InternImage-G [34] by +0.5% AP.

+3.5% and +2.5% AP, respectively. We further finetune the Objects365 pretrained Co-DETR on this dataset. Without elaborate test-time augmentation, our approach achieves the best detection performance of 67.9% and 71.9% AP on LVIS val and minival. Compared to the 3-billion parameter InternImage-G with test-time augmentation, we obtain +4.7% and +6.1% AP gains on LVIS val and minival while reducing the model size to 1/10.

We also demonstrate the best results of Co-DETR on the long-tailed LVIS detection dataset. In particular, we use the same Co-DINO-Deformable-DETR++ as the model on COCO but choose FedLoss [42] as the classification loss to remedy the impact of unbalanced data distribution. Here, we only apply bounding boxes supervision and report the object detection results. The comparisons are available in Table 6. Co-DETR with Swin-L yields 56.9% and 62.3% AP on LVIS val and minival, surpassing ViTDet with MAE-pretrained [13] ViT-H and GLIPv2 [40] by

4.4. Ablation Studies Unless stated otherwise, all experiments for ablations are conducted on Deformable-DETR with a ResNet-50 backbone. We choose the number of auxiliary heads K to 1 by default and set the total batch size to 32. More ablations and 7

Method

Table 8. Performance of our approach with various auxiliary oneto-many heads on COCO val.

Table 9. “aux head” denotes training with an auxiliary head and “pos queries” means the customized positive queries generation.

analyses can be found in the supplementary materials. Criteria for choosing auxiliary heads. We further delve into the criteria for choosing auxiliary heads in Table 7 and 8. The results in Table 8 reveal that any auxiliary head with one-to-many label assignments consistently improves the baseline and ATSS achieves the best performance. We find the accuracy continues to increase as K increases when choosing K smaller than 3. It is worth noting that performance degradation occurs when K = 6, and we speculate the severe conflicts among auxiliary heads cause this. If the feature learning is inconsistent across the auxiliary heads, the continuous improvement as K becomes larger will be destroyed. We also analyze the optimization consistency of multiple heads next and in the supplementary materials. In summary, we can choose any head as the auxiliary head and we regard ATSS and Faster-RCNN as the common practice to achieve the best performance when K ≤ 2. We do not use too many different heads, e.g., 6 different heads to avoid optimization conflicts. Conflicts analysis. The conflicts emerge when the same spatial coordinate is assigned to different foreground boxes or treated as background in different auxiliary heads and can confuse the training of the detector. We first define the distance between head Hi and head Hj , and the average distance of Hi to measure the optimization conflicts as:

where KL, D, I, C refer to KL divergence, dataset, the input image, and class activation maps (CAM) [29]. As illustrated in Figure 6, we compute the average distances among auxiliary heads for K > 1 and the distance between the DETR head and the single auxiliary head for K = 1. We find the distance metric is insignificant for each auxiliary head when K = 1 and this observation is consistent with our results in Table 8: the DETR head can be collaboratively improved with any head when K = 1. When K is increased to 2, the distance metrics increase slightly and our method achieves the best performance as shown in Table 7. The distance surges when K is increased from 3 and 6, indicating severe optimization conflicts among these auxiliary heads lead to a decrease in performance. However, the baseline with 6 ATSS achieves 49.5% AP and can be decreased to 48.9% AP by replacing ATSS with 6 various heads. Accordingly, we speculate too many diverse auxiliary heads, e.g., more than 3 different heads, exacerbate the conflicts. In summary, optimization conflicts are influenced by the number of various auxiliary heads and the relations among these heads. Should the added heads be different? Collaborative training with two ATSS heads (49.2% AP) still improves the model with one ATSS head (48.7% AP) as ATSS is complementary to the DETR head in our analysis. Besides, introducing a diverse and complementary auxiliary head rather

Method

ter region of the instance and provide sufficient supervision signals for the detector. Does distribution difference lead to instability? We compute the average distance between original and customized queries in Figure 7b. The average distance between original negative queries and customized positive queries is significantly larger than the distance between original and customized positive queries. As this distribution gap between original and customized queries is marginal, there is no instability encountered during training.

than the same one as the original head, e.g., Faster-RCNN, can bring better gains (49.5% AP). Note that this is not contradictory to above conclusion; instead, we can obtain the best performance with few different heads (K ≤ 2) as the conflicts are insignificant, but we are faced with severe conflicts when using many different heads (K > 3). The effect of each component. We perform a componentwise ablation to thoroughly analyze the effect of each component in Table 9. Incorporating the auxiliary head yields significant gains since the dense spatial supervision enables the encoder features more discriminative. Alternatively, introducing customized positive queries also contributes remarkably to the final results, while improving the training efficiency of the one-to-one set matching. Both techniques can accelerate convergence and improve performance. In summary, we observe the overall improvements stem from more discriminative features for the encoder and more efficient attention learning for the decoder. Comparisons to the longer training schedule. As presented in Table 10, we find Deformable-DETR can not benefit from longer training as the performance saturates. On the contrary, Co-DETR greatly accelerates the convergence as well as increasing the peak performance. Performance of auxiliary branches. Surprisingly, we observe Co-DETR also brings consistent gains for auxiliary heads in Table 11. This implies our training paradigm contributes to more discriminative encoder representations, which improves the performances of both decoder and auxiliary heads. Difference in distribution of original and customized positive queries. We visualize the positions of original positive queries and customized positive queries in Figure 7a. We only show one object (green box) per image. Positive queries assigned by Hungarian Matching in the decoder are marked in red. We mark positive queries extracted from Faster-RCNN and ATSS in blue and orange, respectively. These customized queries are distributed around the cen-

5. Conclusions In this paper, we present a novel collaborative hybrid assignments training scheme, namely Co-DETR, to learn more efficient and effective DETR-based detectors from versatile label assignment manners. This new training scheme can easily enhance the encoder’s learning ability in end-to-end detectors by training the multiple parallel auxiliary heads supervised by one-to-many label assignments. In addition, we conduct extra customized positive queries by extracting the positive coordinates from these auxiliary heads to improve the training efficiency of positive samples in decoder. Extensive experiments on COCO dataset demonstrate the efficiency and effectiveness of CoDETR. Surprisingly, incorporated with ViT-L backbone, we achieve 66.0% AP on COCO test-dev and 67.9% AP on LVIS val, establishing the new state-of-the-art detector with much fewer model sizes.
