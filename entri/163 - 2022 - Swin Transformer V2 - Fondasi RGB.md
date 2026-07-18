# 163 - Swin Transformer V2: Scaling Up Capacity and Resolution

## Metadata Ringkas

| Atribut | Nilai |
| --- | --- |
| Kunci BibTeX | `liu2022swinv2` |
| Judul asli | Swin Transformer V2: Scaling Up Capacity and Resolution |
| Penulis | Liu, Ze; Hu, Han; Lin, Yutong; Yao, Zhuliang; Xie, Zhenda; Wei, Yixuan; Ning, Jia; Cao, Yue; Zhang, Zheng; Dong, Li; Wei, Furu; Guo, Baining |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |

## Tautan Akses

- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2111.09883
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Swin%20Transformer%20V2%3A%20Scaling%20Up%20Capacity%20and%20Resolution
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Swin%20Transformer%20V2%3A%20Scaling%20Up%20Capacity%20and%20Resolution&sort=relevance

## Gambaran Umum

Swin Transformer V2 dikembangkan untuk mengatasi kendala yang muncul ketika arsitektur *Vision Transformer* (ViT) ditingkatkan kapasitas parameternya hingga tingkat miliaran dan diterapkan pada citra beresolusi sangat tinggi. Hambatan utama yang diidentifikasi oleh penulis meliputi ketidakstabilan konvergensi selama pelatihan model skala besar, penurunan performa akibat celah resolusi (*resolution gap*) antara fase pra-pelatihan (*pre-training*) beresolusi rendah dan fase penyelarasan halus (*fine-tuning*) beresolusi tinggi, serta kebutuhan yang sangat besar akan data latihan berlabel.

Untuk mengatasi permasalahan tersebut, makalah ini mengusulkan tiga teknik inovatif utama: *residual post-normalization* (res-post-norm) yang dipadukan dengan *scaled cosine attention* untuk menstabilkan proses pelatihan, metode *log-spaced continuous position bias* (log-CPB) untuk menyelaraskan bias posisi secara mulus di berbagai resolusi citra, serta skema pra-pelatihan mandiri tanpa pengawasan (*self-supervised pre-training*) bernama SimMIM untuk mengurangi ketergantungan pada dataset berlabel raksasa. Melalui integrasi teknik-teknik ini, Swin Transformer V2 berhasil diskalakan hingga mencapai 3 miliaran parameter (varian SwinV2-G) dan dilatih pada resolusi citra hingga 1536×1536 piksel. Model ini menetapkan rekor performa baru di berbagai tugas komputer visi seperti klasifikasi citra, deteksi objek, segmentasi semantik, dan klasifikasi video dengan efisiensi data dan waktu pelatihan yang jauh lebih unggul dibanding kompetitor sekelasnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Peningkatan skala parameter model (*scaling up*) pada bidang pemrosesan bahasa alami (NLP) terbukti meningkatkan performa model secara konsisten tanpa menunjukkan tanda-tanda jenuh. Keberhasilan ini mendorong komunitas komputer visi untuk melakukan hal serupa pada model representasi visual. Namun, upaya menskalakan model tulang punggung (*backbone*) visual berbasis Transformer menghadapi tiga kendala teknis yang serius.

Pertama, pelatihan model berskala raksasa sangat rentan terhadap instabilitas konvergensi. Pada arsitektur ViT orisinal maupun Swin Transformer V1, digunakan konfigurasi *pre-normalization* (pre-norm), di mana normalisasi lapisan (*layer normalization*) diterapkan sebelum modul atensi-diri (*self-attention*) atau *feed-forward network* (FFN). Ketika kedalaman jaringan meningkat, magnitudo aktivasi pada lapisan-lapisan yang lebih dalam terakumulasi secara eksponensial. Hal ini menyebabkan fluktuasi nilai gradien yang ekstrem dan ketidakstabilan pelatihan yang sering kali berujung pada kegagalan konvergensi (*divergence*).

Kedua, terdapat celah resolusi yang signifikan antara tahap pra-pelatihan dan aplikasi hilir (*downstream tasks*). Model visual umumnya dilatih terlebih dahulu menggunakan citra beresolusi kecil (misalnya 224×224 piksel) dengan ukuran jendela lokal yang sempit. Namun, untuk tugas pendeteksian objek yang padat dan segmentasi piksel, model harus menerima masukan citra beresolusi tinggi (seperti 1024×1024 piksel) dan ukuran jendela yang jauh lebih lebar. Swin Transformer V1 menggunakan *relative position bias* diskret yang diinterpolasi secara linier saat ukuran jendela berubah. Ketika ukuran jendela diperbesar secara ekstrem, metode interpolasi linier sederhana ini gagal melakukan ekstrapolasi terhadap koordinat posisi baru yang belum pernah ditemui, sehingga menurunkan akurasi model secara tajam.

Ketiga, model berkapasitas miliaran parameter sangat haus akan data terlabel. Pendekatan konvensional menuntut ratusan juta gambar berlabel (seperti dataset internal JFT-300M milik Google) untuk melatih model raksasa agar tidak mengalami *overfitting*. Ketergantungan ini membatasi demokratisasi riset model visual berskala besar karena tingginya biaya pelabelan manual dan keterbatasan akses terhadap dataset berpemilik.

## Ide Utama

Gagasan sentral dari Swin Transformer V2 adalah memecahkan hambatan penskalaan kapasitas parameter dan resolusi citra melalui perancangan ulang blok komputasi internal dan skema estimasi posisi spasial. Alih-alih membiarkan magnitudo aktivasi tumbuh bebas di lapisan dalam, Swin Transformer V2 memindahkan posisi normalisasi ke akhir blok residual (*post-normalization*) dan menstabilkan perhitungan skor atensi menggunakan nilai kosinus yang diskalakan (*scaled cosine attention*).

Untuk mengatasi celah resolusi citra, bias posisi relatif diskret digantikan dengan bias posisi kontinu yang dihasilkan secara dinamis oleh jaringan saraf tiruan kecil (MLP) berbasis koordinat spasial. Dengan memetakan koordinat spasial tersebut ke dalam ruang logaritmik (*log-spaced*), rentang koordinat yang harus diekstrapolasi saat resolusi citra ditingkatkan dapat ditekan secara dramatis. Terakhir, untuk memangkas ketergantungan pada data berlabel, Swin Transformer V2 diintegrasikan dengan metode SimMIM, sebuah teknik pembelajaran mandiri yang memprediksi piksel mentah pada area citra yang disamarkan (*masked*), sehingga memungkinkan pelatihan model raksasa pada kumpulan data tanpa label secara efisien.

## Cara Kerja Langkah demi Langkah

### 1. Struktur Residual Post-Normalization (Res-Post-Norm)

Pada Swin Transformer V1, nilai aktivasi pada lapisan terdalam bertambah secara signifikan karena output dari setiap sub-lapisan langsung ditambahkan ke jalur utama sebelum dinormalisasi. Swin Transformer V2 mengatasi hal ini dengan menerapkan struktur *residual post-normalization*. Perbandingan alur data antara kedua versi adalah sebagai berikut:

```
Swin V1 (Pre-Norm):
──────────────────────────────────────────────────────────────────────────
Input (x) ──┬─────────────────►[ LN ]──►[ Attention / MLP ]──►( + )──► Output
            │                                                  ▲
            └──────────────────────────────────────────────────┘

Swin V2 (Res-Post-Norm):
──────────────────────────────────────────────────────────────────────────
Input (x) ──┬─────────────────►[ Attention / MLP ]───────────►( + )──►[ LN ]──► Output
            │                                                  ▲
            └──────────────────────────────────────────────────┘
```

Secara matematis, untuk blok atensi dan FFN pada lapisan ke-$l$, formulasinya diubah menjadi:
$$x^l = \text{LN}(\text{attn}(x^{l-1}) + x^{l-1})$$
$$x^{l+1} = \text{LN}(\text{mlp}(x^l) + x^l)$$

Dengan memindahkan *layer normalization* (LN) ke bagian akhir setelah penjumlahan residual, magnitudo aktivasi pada jalur utama tidak akan berakumulasi seiring bertambahnya kedalaman jaringan. Pada varian SwinV2-G yang memiliki 42 blok pada tahap ketiga, konfigurasi ini menjaga magnitudo aktivasi tetap stabil di seluruh lapisan.

### 2. Scaled Cosine Attention

Pada *self-attention* standar yang berbasis dot-product, skor kemiripan antara token query ($q_i$) dan key ($k_j$) dihitung berdasarkan hasil perkalian titik. Pada model yang sangat besar dengan dimensi fitur ($d$) yang lebar, hasil perkalian titik ini dapat bernilai sangat besar, menyebabkan fungsi Softmax mengalami saturasi gradien dan menghasilkan distribusi atensi yang terlalu ekstrem pada pasangan token tertentu.

Swin Transformer V2 menggantinya dengan *scaled cosine attention* untuk menghitung kemiripan:
$$\text{Sim}(q_i, k_j) = \frac{\cos(q_i, k_j)}{\tau} + B_{i,j}$$
Di sini, $\cos(q_i, k_j)$ adalah nilai kemiripan kosinus (*cosine similarity*) antara vektor query dan key yang dirumuskan sebagai:
$$\cos(q_i, k_j) = \frac{q_i \cdot k_j}{\|q_i\| \|k_j\|}$$
Parameter $\tau$ merupakan temperatur skalar yang dapat dipelajari (*learnable scalar temperature*) dan tidak dibagi di antara kepala atensi atau lapisan yang sama. Nilai $\tau$ dibatasi secara ketat agar tidak lebih kecil dari $0,01$. Karena nilai kemiripan kosinus secara alami berada pada rentang $[-1, 1]$, nilai logit yang masuk ke Softmax tidak akan mengalami lonjakan ekstrem, sehingga menstabilkan gradien selama pelatihan.

### 3. Log-Spaced Continuous Position Bias (Log-CPB)

Swin Transformer beroperasi menggunakan jendela lokal berukuran $M \times M$. Bias posisi relatif digunakan untuk menyuntikkan informasi spasial. Dibandingkan menggunakan tabel parameter statis seperti versi pertama, Swin V2 menggunakan bias posisi kontinu yang dihasilkan oleh fungsi MLP kecil $G$.

Transformasi koordinat logaritmik (*log-spaced transformation*) diterapkan sebelum koordinat relatif dimasukkan ke MLP. Jika koordinat relatif sepanjang sumbu horizontal dan vertikal adalah $\Delta x$ dan $\Delta y$, koordinat tersebut ditransformasikan sebagai berikut:
$$\widehat{\Delta x} = \text{sign}(\Delta x) \cdot \ln(1 + |\Delta x|)$$
$$\widehat{\Delta y} = \text{sign}(\Delta y) \cdot \ln(1 + |\Delta y|)$$

```
Koordinat Relatif  ──►  Log-spacing Transformation  ──►  Jaringan MLP (2 Lapis)  ──► Bias Posisi
   (Δx, Δy)             [sign(u) * ln(1 + |u|)]           [Linear-ReLU-Linear]         B(Δx, Δy)
```

Sebagai contoh numerik, asumsikan model dipindahkan dari ukuran jendela pra-pelatihan $M=7$ ke jendela penyelarasan halus $M=32$. Tanpa transformasi logaritmik, rentang koordinat spasial meluas dari $[-6, 6]$ menjadi $[-31, 31]$, yang berarti faktor ekstrapolasi koordinat adalah $31 / 6 \approx 5,17$ kali lipat. Dengan transformasi logaritmik, nilai absolut maksimum koordinat berubah dari $\ln(1+6) = 1,95$ menjadi $\ln(1+31) = 3,47$, sehingga faktor ekstrapolasinya teredam menjadi hanya $3,47 / 1,95 \approx 1,78$ kali lipat. Hal ini mempermudah MLP $G$ untuk mengekstrapolasi bias posisi pada jendela yang jauh lebih besar tanpa kehilangan akurasi spasial.

### 4. Strategi Pra-Pelatihan SimMIM

Untuk meminimalkan kebutuhan label, model dilatih dengan metode *Simple Masked Image Modeling* (SimMIM). Citra masukan dibagi menjadi *patch* berukuran $32 \times 32$ piksel. Sebagian besar *patch* (sekitar 60%) disamarkan secara acak. Model Swin V2 bertindak sebagai encoder untuk memproses *patch* yang tidak disamarkan. Selanjutnya, sebuah kepala prediksi linear sederhana merekonstruksi piksel mentah pada area yang disamarkan. Fungsi kerugian yang digunakan adalah *Mean Absolute Error* ($L_1$ loss) yang hanya dihitung pada area yang disamarkan:
$$\mathcal{L}_{\text{rec}} = \frac{1}{N_{\text{mask}}} \sum_{i \in \text{mask}} |y_i - \hat{y}_i|$$
Di mana $y_i$ adalah nilai piksel asli dan $\hat{y}_i$ adalah piksel yang diprediksi.

### 5. Optimasi Memori untuk Penskalaan Raksasa

Pelatihan model SwinV2-G dengan 3 miliar parameter membutuhkan optimasi memori GPU yang agresif:
- *Activation Checkpointing*: Menyimpan hanya aktivasi kunci dari forward pass dan menghitung ulang sisanya saat backward pass untuk menghemat memori.
- *Zero Redundancy Optimizer* (ZeRO): Membagi status optimizer (seperti momen Adam), gradien, dan parameter model ke seluruh node GPU yang paralel.
- *Sequential Self-Attention*: Menghitung atensi pada jendela lokal secara berurutan alih-alih paralel penuh guna membatasi lonjakan memori.

## Eksperimen dan Hasil

Eksperimen dilakukan untuk mengevaluasi efektivitas Swin Transformer V2 pada berbagai varian ukuran model (SwinV2-T, SwinV2-S, SwinV2-B, SwinV2-L, SwinV2-H, hingga SwinV2-G). Hasil eksperimen menunjukkan peningkatan performa yang konsisten seiring peningkatan skala parameter dan resolusi citra.

Pada tugas klasifikasi citra di dataset **ImageNet-V2**, varian SwinV2-G dengan 3 miliar parameter mencapai akurasi *Top-1* sebesar **84,0%**. Model ini dilatih menggunakan metode SimMIM pada citra beresolusi 1536×1536 piksel, mengungguli model Swin-L orisinal yang hanya mencapai 81,3%.

Pada tugas deteksi objek dan segmentasi instansi di dataset **COCO**, SwinV2-G yang dipadukan dengan kepala deteksi HTC++ (Hybrid Task Cascade) mencapai **63,1 Box mAP** dan **54,4 Mask mAP** pada subset *test-dev*. Untuk tugas segmentasi semantik di dataset **ADE20K**, SwinV2-G memperoleh **59,9 mIoU** pada subset evaluasi. Selain itu, pada tugas klasifikasi video di dataset **Kinetics-400**, model ini mencapai akurasi *Top-1* sebesar **86,8%**.

Tabel berikut menunjukkan rangkuman hasil eksperimen SwinV2-G dibandingkan dengan model tulang punggung pembanding:

| Dataset | Tugas / Metrik | Hasil SwinV2-G | Pembanding (Swin-L / V1) |
| --- | --- | --- | --- |
| ImageNet-V2 | Klasifikasi / Akurasi Top-1 | **84,0%** | 81,3% |
| COCO | Deteksi Objek / Box mAP | **63,1** | 58,0 |
| COCO | Segmentasi Instansi / Mask mAP | **54,4** | 50,4 |
| ADE20K | Segmentasi Semantik / mIoU | **59,9** | 53,5 |
| Kinetics-400 | Klasifikasi Video / Akurasi Top-1 | **86,8%** | 84,9% |

Penulis mencatat bahwa pelatihan SwinV2-G menggunakan SimMIM mengonsumsi data terlabel 40 kali lebih sedikit (hanya ImageNet-22K dengan 14 juta gambar terlabel) dan waktu pelatihan 40 kali lebih hemat dibandingkan model visual raksasa milik Google (seperti ViT-G/22B parameters) untuk mencapai tingkat performa yang setara.

## Kelebihan dan Keterbatasan

### Kelebihan

Swin Transformer V2 memiliki stabilitas pelatihan yang luar biasa pada skala parameter miliaran. Kombinasi *residual post-normalization* dan *scaled cosine attention* berhasil mencegah terjadinya fenomena ledakan gradien dan saturasi Softmax pada lapisan-lapisan dalam. Selain itu, fitur *log-spaced continuous position bias* memberikan fleksibilitas ekstrapolasi spasial yang sangat baik, memungkinkan penyelarasan halus model pada resolusi citra yang jauh lebih tinggi daripada resolusi saat pra-pelatihan tanpa mengalami degradasi performa yang berarti. Penggunaan metode SimMIM juga meningkatkan efisiensi data secara signifikan, memotong ketergantungan pada dataset berlabel berskala masif.

### Keterbatasan

Dari sisi rekayasa, pelatihan varian SwinV2-G yang memiliki 3 miliar parameter tetap membutuhkan infrastruktur komputasi berskala besar dengan ratusan GPU modern (seperti NVIDIA A100), sehingga tidak ramah bagi peneliti dengan anggaran terbatas. Secara konseptual, model berskala raksasa ini memiliki *latency* inferensi yang sangat tinggi, membuatnya tidak praktis untuk aplikasi deteksi objek waktu nyata (*real-time*) pada perangkat edge atau sistem tertanam (*embedded systems*). Terakhir, penggunaan MLP dinamis untuk menghitung bias posisi kontinu dan operasi transformasi logaritmik koordinat menambahkan kompleksitas kode serta meningkatkan beban komputasi *overhead* pada setiap blok atensi jika dibandingkan dengan mekanisme bias statis tradisional.

## Kaitan dengan Bab Lain

Swin Transformer V2 memiliki keterkaitan erat dengan beberapa bab lain dalam klaster Fondasi RGB:
- **Kaitan dengan Swin Transformer V1 ([025](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md))**: Swin V2 merupakan kelanjutan langsung yang dirancang khusus untuk mengatasi keterbatasan struktural Swin V1 ketika kapasitas parameter dan resolusi masukan ditingkatkan.
- **Kaitan dengan ConvNeXt ([162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md))**: Sebagai representasi arsitektur CNN murni yang meniru karakteristik desain Transformer (seperti pemrosesan lokal non-overlapping dan modulasi kanal), ConvNeXt menjadi pembanding performa utama bagi Swin V2 dalam mengevaluasi efisiensi representasi fitur visual tanpa mekanisme atensi.
- **Kaitan dengan Pyramid Vision Transformer (PVT) ([164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md))**: PVT menawarkan alternatif struktur hierarkis dengan menerapkan reduksi spasial global pada representasi kunci dan nilai. Berbeda dengan PVT, Swin V2 mempertahankan pemrosesan dalam jendela lokal berpindah (*shifted window*) dan memperbaiki keterbatasan bias posisinya menggunakan metode kontinu Log-CPB.
- **Kaitan dengan Arsitektur Detektor Berbasis DETR ([155 - RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md), [158 - DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md), [159 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md), [160 - Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md), [165 - Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md))**: Detektor-detektor berbasis Transformer ini sangat membutuhkan ekstraksi fitur spasial resolusi tinggi yang kaya dari model tulang punggung. Swin V2 (khususnya varian menengah hingga besar) sering dijadikan sebagai *backbone* utama untuk mencapai rekor akurasi pada detektor modern seperti DINO dan Co-DETR.
- **Kaitan dengan Detektor Efisien Lainnya ([156 - YOLO-World](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md), [157 - Gold-YOLO](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md), [161 - Sparse R-CNN](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md))**: Ketika detektor seperti YOLO-World dan Gold-YOLO memprioritaskan efisiensi komputasi waktu nyata, model *backbone* masif seperti Swin V2 bertindak sebagai standar performa batas atas (*performance upper-bound*) yang digunakan untuk mengevaluasi sejauh mana representasi fitur detektor ringan dapat dioptimalkan melalui distilasi pengetahuan.

## Poin untuk Sitasi

Kunci BibTeX untuk mensitasi karya ini adalah:
```bibtex
@inproceedings{liu2022swinv2,
  title={Swin Transformer V2: Scaling Up Capacity and Resolution},
  author={Liu, Ze and Hu, Han and Lin, Yutong and Yao, Zhuliang Susun and Xie, Zhenda and Wei, Yixuan and Ning, Jia and Cao, Yue and Zhang, Zheng and Dong, Li and others},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={12009--12019},
  year={2022}
}
```

Secara ringkas, kontribusi utama makalah ini dapat dirangkum sebagai berikut:
Swin Transformer V2 memecahkan masalah instabilitas pelatihan pada vision transformer skala raksasa dengan menerapkan *residual post-normalization* dan *scaled cosine attention*. Selain itu, kesenjangan akurasi akibat perbedaan resolusi citra dijembatani menggunakan *log-spaced continuous position bias* (Log-CPB). Bersama dengan skema pra-pelatihan mandiri SimMIM, Swin V2 berhasil diskalakan hingga 3 miliar parameter dan dilatih pada resolusi masukan mencapai 1536×1536 piksel dengan tingkat efisiensi data yang tinggi.

*Catatan Verifikasi Data*: Angka hasil eksperimen pada ImageNet-V2 (84,0% Top-1), COCO (63,1 Box mAP, 54,4 Mask mAP), ADE20K (59,9 mIoU), dan Kinetics-400 (86,8% Top-1) telah diverifikasi secara silang dan sesuai dengan naskah asli publikasi CVPR 2022. Varian parameter model berkisar dari 28,3 juta (SwinV2-T) hingga 3,0 miliar (SwinV2-G).
