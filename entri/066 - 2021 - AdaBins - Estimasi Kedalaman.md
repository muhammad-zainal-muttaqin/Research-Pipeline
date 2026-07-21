# 066 - AdaBins: Depth Estimation Using Adaptive Bins

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bhat2021adabins` |
| Judul asli | AdaBins: Depth Estimation Using Adaptive Bins |
| Penulis | Shariq Farooq Bhat, Ibraheem Alhashim, Peter Wonka |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2011.14141
- **DOI (versi penerbit):** https://doi.org/10.1109/CVPR46437.2021.00400
- **Kode sumber resmi:** https://github.com/shariqfarooq123/AdaBins
- **Google Scholar:** https://scholar.google.com/scholar?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan AdaBins, sebuah blok arsitektur untuk memprediksi peta kedalaman rapat (*dense depth map*) dari satu citra RGB, yaitu tugas menetapkan satu nilai jarak kamera untuk setiap piksel. Masalah yang diserang adalah cara jaringan memperlakukan rentang kedalaman: metode regresi langsung dan metode klasifikasi dengan pembagian rentang yang tetap sama-sama mengabaikan kenyataan bahwa distribusi nilai kedalaman sangat berbeda antar-citra. Citra furnitur dari jarak dekat memusat pada kedalaman kecil, sedangkan citra koridor menyebar sampai kedalaman maksimum.

Gagasan utamanya adalah membagi rentang kedalaman menjadi N *bin* (sub-rentang) yang lebarnya dihitung ulang secara adaptif untuk setiap citra masukan oleh sebuah modul *Transformer* kecil bernama mini-ViT. Kedalaman akhir setiap piksel bukan hasil memilih satu bin, melainkan kombinasi linear berbobot *softmax* dari pusat seluruh bin. Dengan desain ini, model mencapai akurasi terbaik pada masanya di dua tolok ukur utama: akurasi ambang δ < 1,25 sebesar 0,903 pada NYU Depth v2 dan 0,964 pada KITTI, mengungguli pembanding kuat seperti BTS dan DAV pada semua metrik yang dilaporkan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular adalah masalah *ill-posed*: satu citra dapat bersesuaian dengan banyak geometri adegan yang berbeda, sehingga jaringan harus memanfaatkan statistik dan konteks adegan, bukan hanya isyarat lokal. Sejak Eigen dkk. (bab 062) memperkenalkan regresi kedalaman dengan CNN multi-skala pada 2014, pendekatan dominan memprediksi satu nilai kontinu per piksel secara langsung. Fu dkk. (2018) lewat metode DORN menempuh jalan lain: regresi diubah menjadi klasifikasi ordinal dengan membagi rentang kedalaman menjadi sejumlah *bin* berlebar tetap, dan kedalaman piksel ditetapkan dari bin yang menang. Akurasi metriknya membaik, tetapi karena setiap piksel dipetakan ke tepat satu bin, peta kedalaman mengandung artefak diskretisasi berupa diskontinuitas tajam yang mengganggu aplikasi lanjutan seperti rekonstruksi 3D.

Dua metode terkuat menjelang 2021, yaitu BTS (bab 065) dengan *local planar guidance* dan DAV dengan atensi koplanaritas, bergantung pada asumsi bahwa permukaan adegan cenderung planar — asumsi yang tidak selalu berlaku, terutama di luar ruangan. Ada pula masalah arsitektural yang lebih umum: pada arsitektur konvolusi biasa, informasi global baru terolah setelah tensor menyusut ke resolusi spasial sangat rendah di sekitar *bottleneck* (titik tersempit jaringan). Padahal distribusi kedalaman berbeda tajam antar-citra, dan analisis global atas distribusi tersebut jauh lebih berguna bila dilakukan pada resolusi tinggi, ketika informasi spasial masih utuh.

## Ide Utama

AdaBins memperbaiki skema bin melalui tiga perubahan. Pertama, lebar bin tidak ditetapkan di muka dan tidak pula satu pembagian untuk seluruh dataset, melainkan dihitung ulang untuk setiap citra oleh modul *Transformer* yang membaca fitur seluruh adegan — jaringan sendiri yang memutuskan bagian rentang kedalaman mana yang layak mendapat resolusi halus. Kedua, kedalaman piksel bukan pusat bin pemenang, melainkan nilai harapan atas semua pusat bin dengan bobot probabilitas *softmax*; keluaran tetap kontinu sehingga artefak diskretisasi hilang. Ketiga, pemrosesan global ini ditempatkan setelah dekoder pada tensor beresolusi setengah citra, bukan di *bottleneck*. Masukan blok adalah tensor fitur hasil dekode; keluarannya adalah vektor lebar bin dan satu set peta perhatian; keduanya digabungkan menjadi peta kedalaman.

## Cara Kerja Langkah demi Langkah

### Baseline Encoder-Decoder

Komponen pertama adalah jaringan *encoder-decoder* konvensional yang diadaptasi dari arsitektur Alhashim dan Wonka: *encoder* menurunkan resolusi citra sambil mengekstrak fitur, *decoder* menaikkannya kembali secara bertahap. Enkoder memakai EfficientNet-B5, jaringan konvolusi yang skala lebar, kedalaman, dan resolusinya diseimbangkan menurut satu koefisien majemuk. Berbeda dari jaringan dasar tersebut, keluaran dekoder bukan peta kedalaman, melainkan tensor fitur terdekode berukuran h × w × Cd dengan h = H/2 dan w = W/2 (setengah resolusi citra masukan, demi menghemat memori GPU). Kedalaman akhir diperoleh dengan *upsampling* bilinear dua kali pada tahap paling akhir.

### Mini-ViT: Penentu Lebar Bin Adaptif

Blok AdaBins diawali mini-ViT, versi kecil dari *Vision Transformer* — arsitektur berbasis mekanisme atensi yang memroses sekuens vektor dan memungkinkan setiap elemen sekuens saling memperhatikan tanpa konvolusi. Fitur terdekode dilewatkan konvolusi berkernel p × p dengan *stride* p (p = 16), menghasilkan tensor h/p × w/p × E yang diratakan menjadi sekuens S = hw/p² vektor berdimensi E = 128 yang disebut *patch embedding*. Setelah ditambah enkoding posisi yang dipelajari, sekuens ini diproses *encoder Transformer* kecil (4 lapis, 4 kepala atensi, MLP 1024). Sebuah *MLP head* beraktivasi ReLU membaca embedding keluaran pertama dan menghasilkan vektor N dimensi b′, yang dinormalisasi menjadi lebar bin b_i = (b′_i + ε) / Σ_j(b′_j + ε) dengan ε = 10⁻³, sehingga jumlah seluruh lebar bin tepat satu.

Normalisasi ini menciptakan kompetisi: memperlebar satu bin harus mengorbankan bin lain. Jaringan dengan demikian didorong menempatkan bin sempit pada sub-rentang yang padat nilai kedalaman dan bin lebar pada sub-rentang yang jarang. Pada citra koridor, bin menyebar sampai kedalaman maksimum; pada citra furnitur jarak dekat, bin terkonsentrasi di sekitar 1–2 meter. Pusat setiap bin dihitung sebagai c(b_i) = dmin + (dmax − dmin)(b_i/2 + Σ_{j<i} b_j). Sebagai contoh, pada rentang D = (0, 10) meter: bila b_1 = 0,2 maka c(b_1) = 10 × 0,1 = 1,0 meter, dan bila b_2 = 0,1 maka c(b_2) = 10 × (0,05 + 0,2) = 2,5 meter.

### Range-Attention-Maps

Keluaran kedua mini-ViT adalah *Range-Attention-Maps* (R). Embedding keluaran ke-2 sampai ke-(C+1) dari Transformer dipakai sebagai kernel konvolusi 1 × 1 yang dikonvolusikan dengan fitur terdekode (setelah satu konvolusi 3 × 3), menghasilkan tensor R berukuran h × w × C. Operasi ini setara dengan atensi hasil kali titik: fitur setiap piksel berperan sebagai *key* dan embedding Transformer sebagai *query*. Dengan cara ini, informasi global yang diolah Transformer disuntikkan ke informasi lokal setiap piksel pada resolusi tinggi.

### Regresi Hibrida

Tensor R dilewatkan konvolusi 1 × 1 menjadi N kanal, lalu diaktifkan *softmax* sehingga setiap piksel memiliki distribusi probabilitas p_k atas N pusat bin. Kedalaman piksel dihitung sebagai kombinasi linear d̃ = Σ_k c(b_k) · p_k. Misalnya sebuah piksel dengan p = (0,7; 0,3) pada pusat bin 2,0 meter dan 2,5 meter memperoleh d̃ = 0,7 × 2,0 + 0,3 × 2,5 = 2,15 meter — nilai kontinu yang tidak terkunci pada pusat bin mana pun, sehingga peta kedalaman halus tanpa tingkatan diskrit.

Alur lengkap dari citra ke kedalaman:

```
citra RGB  H x W x 3
     |
     v
+------------------------------------------+
| encoder EfficientNet-B5  +  decoder      |
+------------------------------------------+
     | fitur terdekode h x w x Cd  (h = H/2, w = W/2)
     v
+------------------------------------------+
| mini-ViT (Transformer, 4 lapis)          |
+------------------------------------------+
     |
     +-> vektor lebar bin b (jumlah = 1) -> pusat bin c(b)
     +-> Range-Attention-Maps R -> conv 1x1 -> softmax p
     v
+------------------------------------------+
| regresi hibrida:  d = sum p_k * c(b_k)   |
+------------------------------------------+
     | peta kedalaman h x w x 1
     v
 upsampling bilinear x2  ->  kedalaman akhir H x W x 1
```

Diagram di atas memperlihatkan dua keluaran mini-ViT yang menyatu pada tahap regresi hibrida: lebar bin menentukan posisi pusat bin pada rentang kedalaman, sedangkan R menentukan bobot per piksel atas pusat-pusat tersebut.

### Fungsi Loss

Pelatihan memakai dua suku. Suku pertama adalah versi berskala dari *scale-invariant loss* Eigen dkk.: dengan g_i = log d̃_i − log d_i, loss dihitung dari rata-rata kuadrat g_i dikurangi λ kali kuadrat rata-ratanya (λ = 0,85, dikali faktor skala μ = 10); bentuk ini menghukum ketidakkonsistenan galat log antar-piksel sehingga tidak sensitif terhadap galat skala global. Suku kedua adalah loss densitas pusat bin berupa *Chamfer loss* dua arah antara himpunan pusat bin dan himpunan nilai kedalaman kebenaran dasar (*ground truth*): setiap pusat bin didorong mendekati nilai kedalaman yang benar-benar ada pada citra, dan sebaliknya. Loss total adalah L_total = L_pixel + 0,1 · L_bins.

### Pelatihan

Model dilatih dengan pengoptimal AdamW (*weight decay* 10⁻²), kebijakan laju pembelajaran 1-*cycle* dengan maksimum 3,5 × 10⁻⁴, selama 25 epoch dengan *batch* 16 — sekitar 20 menit per epoch pada empat GPU V100 32 GB. Model berisi ±78 juta parameter: 28 juta pada enkoder, 44 juta pada dekoder, dan 5,8 juta pada modul AdaBins. Saat pengujian, kedalaman akhir adalah rata-rata prediksi citra asli dan prediksi citra cerminnya.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tiga dataset. NYU Depth v2 memuat 654 citra uji dalam ruangan (resolusi 640 × 480, kedalaman maksimum 10 meter); model dilatih pada subset 50 ribu citra. KITTI memuat adegan luar ruangan dari kendaraan bergerak; pelatihan memakai ±26 ribu citra dan pengujian 697 citra menurut pemisahan Eigen, pada rentang 0–80 meter. SUN RGB-D (5.050 citra uji) hanya dipakai untuk uji silang tanpa penyetelan ulang. Metrik yang dipakai: akurasi ambang δ < 1,25 (persentase piksel yang rasio terburuknya terhadap kebenaran dasar di bawah 1,25; makin besar makin baik), AbsRel (rata-rata galat relatif absolut; makin kecil makin baik), RMSE (akar rata-rata kuadrat galat), serta SqRel (kuadrat galat relatif) untuk KITTI.

Hasil utama:

- **NYU Depth v2:** δ1 = 0,903; AbsRel = 0,103; RMSE = 0,364. Pembanding terkuat sebelumnya, BTS, mencapai 0,885 / 0,110 / 0,392 dan DAV 0,882 / 0,108 / 0,412. Artinya, 90,3% piksel prediksi AdaBins menyimpang kurang dari 25% dari kebenaran dasar, galat relatif turun sekitar 6% dari pesaing terbaik, dan RMSE turun sekitar 7%.
- **KITTI:** δ1 = 0,964; AbsRel = 0,058; RMSE = 2,360; SqRel = 0,190, dibandingkan BTS 0,956 / 0,059 / 2,756 / 0,245. Makalah melaporkan perbaikan RMSE sekitar 13,5% dan SqRel 22,4% terhadap keadaan seni sebelumnya; penurunan galat kuadrat yang besar menandakan galat besar pada piksel jarak jauh berhasil ditekan.
- **SUN RGB-D (uji silang):** AbsRel = 0,159 dan δ1 = 0,771, dibandingkan BTS 0,172 dan 0,740. Model yang dilatih di NYU menggeneralisasi lebih baik ke sensor dan adegan baru, meskipun galatnya tetap jauh di atas pengujian dalam-domain (0,103).

Studi ablasi pada NYU mengukur sumbangan tiap pilihan desain (δ1 / AbsRel / RMSE): regresi standar tanpa modul 0,881 / 0,111 / 0,419; bin tetap seragam 0,892 / 0,107 / 0,383; bin tetap skala log 0,896 / 0,108 / 0,379; bin terlatih tetapi tetap untuk semua citra 0,893 / 0,109 / 0,381; AdaBins penuh 0,903 / 0,103 / 0,364. Semua varian berbasis bin mengungguli regresi standar, tetapi hanya bin adaptif per citra yang memberi lompatan besar — bukti bahwa adaptasi terhadap distribusi kedalaman spesifik citra adalah sumber utama perbaikan. Penambahan loss Chamfer menurunkan AbsRel dari 0,106 menjadi 0,103. Jumlah bin ditetapkan N = 256 karena perbaikan di atas nilai itu jenuh.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah adaptivitas tanpa asumsi geometris: berbeda dari BTS dan DAV, tidak ada asumsi planaritas yang dapat dilanggar adegan nyata. Regresi hibrida menghilangkan artefak diskretisasi metode bin tetap seperti DORN, pemrosesan global dilakukan pada resolusi tinggi, dan kode beserta bobot terlatih dirilis publik.

Keterbatasannya: (1) metode ini *supervised* penuh dan membutuhkan kebenaran dasar kedalaman rapat, kontras dengan jalur *self-supervised* Monodepth2 (bab 064); (2) rentang (dmin, dmax) dan jumlah bin N harus ditetapkan manual per dataset; (3) modul global menambah 5,8 juta parameter dan komputasi atensi pada resolusi tinggi — dari sisi rekayasa, total 78 juta parameter lebih berat dari BTS (47 juta) dan DAV (25 juta); (4) secara konseptual, generalisasi lintas dataset tetap terbatas, terlihat dari kenaikan AbsRel dari 0,103 menjadi 0,159 pada uji silang SUN RGB-D.

## Kaitan dengan Bab Lain

Bab ini mewarisi dua hal dari [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md): loss *scale-invariant* dan protokol pemisahan data uji yang menjadi standar evaluasi. Posisinya merupakan jawaban langsung atas keterbatasan regresi murni yang dipakai [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md), pembanding utamanya, sekaligus penyempurnaan skema bin tetap DORN. Jalurnya berseberangan dengan [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) yang mengejar akurasi tanpa label kedalaman. Pada tahun yang sama, [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md) membawa Transformer ke prediksi rapat dengan cara berbeda — mengganti *backbone* konvolusi sepenuhnya — sehingga kedua bab ini menandai masuknya Transformer ke estimasi kedalaman.

## Poin untuk Sitasi

Kutip dengan kunci `bhat2021adabins`. Ringkasan yang aman dikutip: "AdaBins membagi rentang kedalaman menjadi bin yang lebarnya diprediksi secara adaptif per citra oleh modul Transformer, dan menghitung kedalaman piksel sebagai kombinasi linear pusat bin; metode ini melampaui keadaan seni pada NYU Depth v2 (δ1 = 0,903, AbsRel = 0,103) dan KITTI (δ1 = 0,964, AbsRel = 0,058) pada semua metrik standar." Seluruh angka di bab ini diverifikasi dari naskah CVPR 2021 versi *open access*; satu hal yang perlu diperiksa ulang sebelum sitasi formal adalah klaim "perbaikan RMSE 13,5%" pada KITTI, karena naskah tidak menyebut eksplisit pembanding acuan persentase tersebut pada kalimat klaimnya.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract We address the problem of estimating a high quality dense depth map from a single RGB input image. We start out with a baseline encoder-decoder convolutional neural network architecture and pose the question of how the global processing of information can help improve overall depth estimation. To this end, we propose a transformerbased architecture block that divides the depth range into bins whose center value is estimated adaptively per image. The final depth values are estimated as linear combinations of the bin centers. We call our new building block AdaBins. Our results show a decisive improvement over the state-ofthe-art on several popular depth datasets across all metrics. We also validate the effectiveness of the proposed block with an ablation study and provide the code and corresponding pre-trained weights of the new state-of-the-art model 1 .

Figure 1: Illustration of AdaBins: Top: input RGB images. Middle: depth predicted by our model. Bottom: histogram of depth values of the ground truth (blue) and histogram of the predicted adaptive depth-bin-centers (red) with depth values increasing from left to right. Note that the predicted bin-centers are focused near smaller depth values for closeup images but are widely distributed for images with a wider range of depth values.

1. Introduction This paper tackles the problem of estimating a high quality dense depth map from a single RGB input image. This is a classical problem in computer vision that is essential for many applications [27, 31, 17, 7]. In this work, we propose a new architecture building block, called AdaBins that leads to a new state-of-the-art architecture for depth estimation on the two most popular indoor and outdoor datasets, NYU [37] and KITTI [14]. The motivation for our work is the conjecture that current architectures do not perform enough global analysis of the output values. A drawback of convolutional layers is that they only process global information once the tensors reach a very low spatial resolution at or near the bottleneck. However, we believe that global processing is a lot more powerful when done at high resolution. Our general idea is to perform a global statistical analysis of the output of a traditional encoder-decoder architecture and to refine the output with a learned post-processing building block that operates at the highest resolution. As a particular realization of this

idea, we propose to analyze and modify the distribution of the depth values. Depth distribution corresponding to different RGB inputs can vary to a large extent (see Fig. 1). Some images have most of the objects located over a very small range of depth values. Closeup images of furniture will, for example, contain pixels most of which are close to the camera while other images may have depth values distributed over a much broader range, e.g. a corridor, where depth values range from a small value to the maximum depth supported by the network. Along with the ill-posed nature of the problem, such a variation in depth distribution makes depth regression in an end-to-end manner an even more difficult task. Recent works have proposed to exploit assumptions about indoor environments such as planarity constraints [26, 22] to guide the network, which may or may not hold for a real-

Figure 2: Overview of our proposed network architecture. Our architecture consists of two major components: an encoderdecoder block and our proposed adaptive bin-width estimator block called AdaBins. The input to our network is an RGB image of spatial dimensions H and W , and the output is a single channel h × w depth image (e.g., half the spatial resolution). world environment, especially for outdoors scenes. Instead of imposing such assumptions, we investigate an approach where the network learns to adaptively focus on regions of the depth range which are more probable to occur in the scene of the input image. Our main contributions are the following: • We propose an architecture building block that performs global processing of the scene’s information. We propose to divide the predicted depth range into bins where the bin widths change per image. The final depth estimation is a linear combination of the bin center values.

Figure 3: Choices for bin widths. Uniform and Loguniform bins are pre-determined. ‘Trained bins’ vary from one dataset to another. Adaptive bins vary for each input image.

the bottleneck. Our results section compares to these (and many other) methods. Encoder-decoder networks have made significant contributions in many vision related problems such as image segmentation [35], optical flow estimation [10], and image restoration [28]. In recent years, the use of such architectures have shown great success both in the supervised and the unsupervised setting of the depth estimation problem [15, 41, 21, 48, 1]. Such methods typically use one or more encoder-decoder networks as a sub part of their larger network. In this paper we adapted the baseline encoderdecoder network architecture used by [1]. This allows us to more explicitly study the performance attribution of our proposed extension on the pipeline which is typically a difficult task. Transformer networks are gaining greater attention as a viable building block outside of their traditional use in NLP tasks and into computer vision tasks [32, 43, 2, 6]. Following the success of recent trends that combine CNNs with Transformers [2], we propose to leverage a Transformer encoder as a building block for non-local processing on the output of a CNN.

• We analyze our findings and investigate different modifications on the proposed AdaBins block and study their effect on the accuracy of the depth estimation.

2. Related Work The problem of 3D scene reconstruction from RGB images is an ill-posed problem. Issues such as lack of scene coverage, scale ambiguities, translucent or reflective materials all contribute to ambiguous cases where geometry cannot be derived from appearance. Recently, methods that rely on convolutional neural networks (CNNs) are able to produce reasonable depth maps from a single RGB input image at real-time speeds. Monocular depth estimation has been considered by many CNN methods as a regression of a dense depth map from a single RGB image [8, 25, 45, 16, 46, 11, 19, 1, 26, 22]. As the two most important competitors, we consider BTS [26] and DAV [22]. BTS uses local planar guidance layers to guide the features to full resolution instead of standard upsampling layers during the decoding phase. DAV uses a standard encoder-decoder scheme and proposes to exploit co-planarity of objects in the scene via attention at

3.1. Motivation

Our idea could be seen as a generalization of depth estimation via an ordinal regression network as proposed by Fu et al. [11]. Fu et al. observed that a performance improvement could be achieved if the depth regression task is transformed into a classification task. They proposed to divide the depth range into a fixed number of bins of predetermined width. Our generalization solves multiple limitations of the initial approach. First, we propose to compute adaptive bins that dynamically change depending on the features of the input scene. Second, a classification approach leads to a discretization of depth values which results in poor visual quality with obvious sharp depth discontinuities. This might still lead to good results with regard to the standard evaluation metrics, but it can present a challenge for downstream applications, e.g. computational photography or 3D reconstruction. Therefore, we propose to predict the final depth values as a linear combination of bin centers. This allows us to combine the advantages of classification with the advantages of depth-map regression. Finally, compared to other architectures, e.g. DAV [22], we compute information globally at a high resolution and not primarily in the bottleneck part at a low resolution.

Figure 4: An overview of the mini-ViT block. The input to the block is a multi-channel feature map of the input image. The block includes a Transformer encoder that is applied on patch embeddings of the input for the purpose of learning to estimate bin widths b and a set of convolutional kernels needed to compute our Range-Attention-Maps R. Second, discretizing the depth interval D into bins and assigning each pixel to a single bin leads to depth discretization artifacts. We therefore predict the final depth as a linear combination of bin centers enabling the model to estimate smoothly varying depth values. Third, several previous architectures propose performing global processing using attention blocks to process information after an encoder block in the architecture (e.g., image captioning [5, 18] or object detection [2]). Also, the current state-of-the-art in depth estimation uses this strategy [22]. Such an architecture consists of three blocks ordered as such: encoder, attention, followed by a decoder. We initially followed this approach but noticed that better results can be achieved when using attention at the spatially higher resolution tensors. We therefore propose an architecture that also has these three blocks, but ordered as follows: encoder, decoder, and finally attention. Fourth, we would like to build on the simplest possible architecture to isolate the effects of our newly proposed AdaBins concept. We therefore build on a modern encoderdecoder [1] using EfficientNet B5 [40] as the backbone for the encoder. In the next subsection, we provide a description of the entire architecture.

3.2. AdaBins design Here, we discuss four design choices of our proposed architecture that are most important for the obtained results. First, we employ an adaptive binning strategy to discretize the depth interval D = (dmin , dmax ) into N bins. This interval is fixed for a given dataset and is determined by dataset specification or manually set to a reasonable range. To illustrate our idea of dividing a depth interval into bins, we would like to contrast our final solution with three other possible design choices we evaluated: • Fixed bins with a uniform bin width: the depth interval D is divided into N bins of equal size. • Fixed bins with a log scale bin width: the depth interval D is divided into bins of equal size in log scale. • Trained bin widths: the bin widths are adaptive and can be learned for a particular dataset. While the bin widths are general, all images finally share the same bin subdivision of the depth interval D.

3.3. Architecture description Fig. 2 shows an overview of our proposed depth estimating architecture. Our architecture consists of two major components: 1) an encoder-decoder block built on a pretrained EfficientNet B5 [40] encoder and a standard feature upsampling decoder; 2) our proposed adaptive binwidth estimator block called AdaBins. The first component is primarily based on the simple depth regression network of Alhashim and Wonka [1] with some modifications. The two basic modifications are switching the encoder from

• AdaBins: the bin widths b are adaptively computed for each image. We recommend the strategy of AdaBins as the best option and our ablation study validates this choice by showing the superiority of this design over its alternatives. An illustration of the four design choices for bin widths can be seen in Fig. 3. 3

E. Thus, the result of this convolution is a tensor of size h/p × w/p × E (assuming both h and w are divisible by p). The result is reshaped into a spatially flattened tensor xp ∈ RS×E , where S = hw p2 serves as the effective sequence length for the transformer. We refer to this sequence of E-dimensional vectors as patch embeddings. Following common practice [2, 6], we add learned positional encodings to the patch embeddings before feeding them to the transformer. Our transformer is a small transformer encoder (see Table. 1 for details) and outputs a sequence of output embeddings xo ∈ RS×E . We use an MLP head over the first output embedding (we also experimented with a version that has an additional special token as first input, but did not see an improvement). The MLP head uses a ReLU activation and outputs an N-dimensional vector b0 . Finally, we normalize the vector b0 such that it sums up to 1, to obtain the bin-widths vector b as follows:

DenseNet [20] to EfficientNet B5 and using a different appropriate loss function for the new architecture. In addition, the output of the decoder is a tensor xd ∈ Rh×w×Cd , not a single channel image representing the final depth values. We refer to this tensor as the “decoded features”. The second component is a key contribution in this paper, the AdaBins module. The input to the AdaBins module are decoded features of size h×w ×Cd and the output tensor is of size h × w × 1. Due to memory limitations of current GPU hardware, we use h = H/2 and w = W/2 to facilitate better learning with larger batch sizes. The final depth map is computed by simply bilinearly upsampling to H × W × 1. The first block in the AdaBins module is called miniViT. An overview of this block is shown in Fig. 4. It is a simplified version of a recently proposed technique of using transformers for image recognition [6] with minor modifications. The details of mini-ViT are explained in the next paragraph. There are two outputs of mini-ViT: 1) a vector b of bin-widths, which defines how the depth interval D is to be divided for the input image, and 2) Range-AttentionMaps R of size h × w × C, that contain useful information for pixel-level depth computation.

where = 10−3 . The small positive ensures each binwidth is strictly positive. The normalization introduces a competition among the bin-widths and conceptually forces the network to focus on sub-intervals within D by predicting smaller bin-widths at interesting regions of D. In the next subsection, we describe how the RangeAttention-Maps R are obtained from the decoded features and the transformer output embeddings. Range attention maps. At this point, the decoded features represent a high-resolution and local pixel-level information while the transformer output embeddings effectively contain more global information. As shown in Fig. 4, output embeddings 2 through C + 1 from the transformer are used as a set of 1 × 1 convolutional kernels and are convolved with the decoded features (following a 3 × 3 convolutional layer) to obtain the Range-Attention Maps R. This is equivalent to calculating the Dot-Product attention weights between pixel-wise features treated as ‘keys’ and transformer output embeddings as ‘queries’. This simple design of using output embeddings as convolutional kernels lets the network integrate adaptive global information from the transformer into the local information of the decoded features. R and b are used together to obtain the final depth map.

Mini-ViT. Estimating sub-intervals within the depth range D which are more probable to occur for a given image would require a combination of local structural information and global distributional information at the same time. We propose to use global attention in order to calculate a binwidths vector b for each input image. Global attention is expensive both in terms of memory and computational complexity, especially at higher resolutions. However, recent rapid advances in transformers provide some efficient alternatives. We take inspiration from the Vision Transformer ViT [6] in designing our AdaBins module with transformers. We also use a much smaller version of the transformer proposed as our dataset is smaller and refer to this transformer as mini-ViT or mViT in the following description. Bin-widths. We first describe how the bin-widths vector b is obtained using mViT. The input to the mViT block is a tensor of decoded features xd ∈ Rh×w×Cd . However, a transformer takes a sequence of fixed size vectors as input. We first pass the decoded features through a convolutional block, named as Embedding Conv (see Fig 4), with kernel size p × p, stride p and number of output channels

We set β = 0.1 for all our experiments. We experimented with different loss functions including the RMSE loss, and the combined SSIM [42] plus L1 loss suggested by [1]. However, we were able to achieve the best results with our proposed loss. We offer a comparison of the different loss functions and their performance in our ablation study.

Figure 5: Demonstration of artifacts introduced by the discretization of the depth interval. Our hybrid regression results in smoother depth maps.

4. Experiments We conducted an extensive set of experiments on the standard depth estimation from a single image datasets for both indoor and outdoor scenes. In the following, we first briefly describe the datasets and the evaluation metrics, and then present quantitative comparisons to the state-of-the-art in supervised monocular depth estimation.

4.1. Datasets and evaluation metrics

NYU Depth v2 is a dataset that provides images and depth maps for different indoor scenes captured at a pixel resolution of 640 × 480 [37]. The dataset contains 120K training samples and 654 testing samples [8]. We train our network on a 50K subset. The depth maps have an upper bound of 10 meters. Our network outputs depth prediction having a resolution of 320 × 240 which we then upsample by 2× to match the ground truth resolution during both training and testing. We evaluate on the pre-defined center cropping by Eigen et al. [8]. At test time, we compute the final output by taking the average of an image’s prediction and the prediction of its mirror image which is commonly used in previous work.

Compared to Fu et al. [11] we do not predict the depth as the bin center of the most likely bin. This enables us to predict smooth depth maps without the discretization artifacts as can bee seen in Fig. 5.

KITTI is a dataset that provides stereo images and corresponding 3D laser scans of outdoor scenes captured using equipment mounted on a moving vehicle [14]. The RGB images have a resolution of around 1241 × 376 while the corresponding depth maps are of very low density with lots of missing data. We train our network on a subset of around 26K images, from the left view, corresponding to scenes not included in the 697 test set specified by [8]. The depth maps have an upper bound of 80 meters. We train our network on a random crop of size 704 × 352. For evaluation, we use the crop as defined by Garg et al. [13] and bilinearly upsample the prediction to match the ground truth resolution. The final output is computed by taking the average of an image’s prediction and the prediction of its mirror image.

where gi = log d˜i − log di and the ground truth depth di and T denotes the number of pixels having valid ground truth values. We use λ = 0.85 and α = 10 for all our experiments. Bin-center density loss. This loss term encourages the distribution of bin centers to follow the distribution of depth values in the ground truth. We would like to encourage the bin centers to be close to the actual ground truth depth values and the other way around. We denote the set of bin centers as c(b) and the set of all depth values in the ground truth image as X and use the bi-directional Chamfer Loss [9] as a regularizer: Lbins = chamf er(X, c(b)) + chamf er(c(b), X)

Method

Table 2: Comparison of performances on the NYU-Depth-v2 dataset. The reported numbers are from the corresponding original papers. Best results are in bold, second best are underlined. Method

Table 3: Comparison of performances on the KITTI dataset. We compare our network against the state-of-the-art on this dataset. The reported numbers are from the corresponding original papers. Measurements are made for the depth range from 0m to 80m. Best results are in bold, second best are underlined.

Table 4: Comparison of performance with respect to the choice of loss function.

cross-evaluating pre-trained models on the official test set of 5050 images. We do not use it for training.

4.2. Implementation details Evaluation metrics. We use the standard six metrics used in prior work [8] to compare our method against stateof-the-art. These error metrics are defined as: average Pn |y −ŷ | relative error (REL): n1 p p y p ; root mean squared

Method

Table 5: Results of models trained on the NYU-Depth-v2 dataset and tested on the SUN RGB-D dataset [39] without fine-tuning.

from max lr/25 to max lr for the first 30% of iterations followed by cosine annealing to max lr/75. Total number of epochs is set to 25 with batch size 16. Training our model takes 20 min per epoch on a single node with four NVIDIA V100 32GB GPUs. For all results presented we train for 25 epochs. Our main model has about 78M parameters: 28M for the CNN encoder, 44M for the CNN decoder, and 5.8M for the new AdaBins module.

Table 6: Comparison of different design choices for binwidths and regression. AdaBins module results in a significant boost in performance. Base: encoder-decoder with an EfficientNet B5 encoder. R: standard regression. HR: Hybrid Regression. (Log)Uniform-Fix: Fixed (log) uniform bin-widths. Train-Fix: Trained bin-widths but Fixed for each dataset.

4.3. Comparison to the state-of-the-art We consider the following two methods to be our main competitors: BTS [26] and DAV [22]. For completeness, we also include selected previous related methods in the comparison tables. For BTS and DAV we report the corresponding evaluation numbers from their papers. For BTS we also verified these numbers by retraining their network using the authors code. DAV did not have code available by the deadline, but the authors sent us the resulting depth images used in our figures. In our tables we report the numbers given by the authors in their paper 2 . NYU-Depth-v2: See Table 2 for the comparison of the performance on the official NYU-Depth-v2 test set. While the state of the art performance on NYU has been saturated for quite some time, we were able to significantly outperform the state of the art in all metrics. The large gap to the previous state of the art emphasises that our proposed architecture addition makes an important contribution to improving the results. KITTI: Table 3 lists the performance metrics on the KITTI dataset. Our proposed architecture significantly outperforms previous state-of-the-art across all metrics. In particular, our method improves the RMS score by about 13.5% and Squared Relative Difference by 22.4% over the previous state-of-the-art. SUN RGB-D: To compare the generalisation performance, we perform a cross-dataset evaluation by training

our network on the NYU-Depth-v2 dataset and evaluate it on the test set of the SUN RGB-D dataset without any finetuning. For comparison, we also used the same strategy for competing methods for which pretrained models are available [26, 47, 4] and report results in Table. 5.

4.4. Ablation study For our ablation study, we evaluate the influence of the following design choices on our results: AdaBins: We first evaluate the importance of our AdaBins module. We remove the AdaBins block from the architecture and use the encoder-decoder to directly predict the depth map by setting Cd = 1. We then use the loss given by Eq. 4 to train the network. We call this design standard regression and compare it against variants of our AdaBins module. Table. 6 shows that the architecture without AdaBins (Row 1) performs worse than all other variants (Rows 2-5). Bin types: In this set of experiments we examine the performance of adaptive bins over other choices as stated in Sec. 3.2. Table. 6 lists results for all the discussed variants. The Trained-but-Fixed variant performs worst among all choices and our final choice employing adaptive bins significantly improves the performance and outperforms all other variants. Number of bins (N ): To study the influence of the number of bins, we train our network for various values of N

2 The authors of DAV clarified in an email that they compute the depth

maps at 1/4th the resolution and then downsample the ground truth for evaluation. However, we believe that all other methods, including ours, evaluate at the full resolution.

Figure 7: Qualitative comparison with the state-of-the-art on the NYU-Depth-v2 dataset.

Figure 8: Qualitative comparison with the state-of-the-art on the KITTI dataset. solute Relative Error from 10.6% to 10.3%.

and measure the performance in terms of Absolute Relative Error metric. Results are plotted in Fig. 6. Interestingly, starting from N = 20, the error first increases with increasing N and then decreases significantly. As we keep increasing N above 256, and with higher values the gain in performance starts to diminish. We use N = 256 for our final model.

5. Conclusion We introduced a new architecture block, called AdaBins for depth estimation from a single RGB image. AdaBins leads to a decisive improvement in the state of the art for the two most popular datasets, NYU and KITTI. In future work, we would like to investigate if global processing of information at a high resolution can also improve performance on other tasks, such as segmentation, normal estimation, and 3D reconstruction from multiple images.

Loss function: Table. 4 lists performance corresponding to the three choices of loss function. Firstly, the L1 /SSIM combination does not lead to the state-of-the-art performance in our case. Secondly, we trained our network with and without the proposed Chamfer loss (Eq. 5). Introducing the Chamfer loss clearly gives a boost to the performance. For example, introducing the Chamfer loss reduces the Ab8
