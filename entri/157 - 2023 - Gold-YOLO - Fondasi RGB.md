# 157 - Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023goldyolo` |
| Judul asli | Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism |
| Penulis | Wang, Chengcheng; He, Wei; Nie, Ying; Guo, Jianyuan; Liu, Chuanjian; Han, Kai; Wang, Yunhe |
| Tahun | 2023 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2309.11331
- **Google Scholar:** https://scholar.google.com/scholar?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism&sort=relevance

## Gambaran Umum

Gold-YOLO merupakan arsitektur detektor objek waktu nyata (*real-time*) yang dirancang untuk mengatasi hambatan fusi fitur multi-skala pada detektor berbasis regresi satu tahap (*one-stage detector*). Masalah utama yang diselesaikan oleh model ini adalah kebocoran atau hilangnya informasi penting selama proses penggabungan fitur dalam struktur leher (*neck*) konvensional seperti *Feature Pyramid Network* (FPN) dan *Path Aggregation Network* (PANet). Jaringan piramida konvensional tersebut menyebarkan informasi secara bertahap hanya melalui lapisan-lapisan yang bertetangga dekat. Hal ini menyebabkan detail spasial dari lapisan bawah mengalami pelemahan (*information attenuation*) sebelum mencapai lapisan atas yang lebih abstrak.

Sebagai solusinya, Gold-YOLO introduces mekanisme *Gather-and-Distribute* (GD) yang beroperasi layaknya arsitektur *hub-and-spoke* (pusat dan jari-jari). Mekanisme ini mengumpulkan (*gather*) fitur dari seluruh tingkatan secara simultan ke dalam representasi global terpadu, lalu mendistribusikannya (*distribute*) secara langsung ke setiap level piramida fitur. Dengan pembagian beban komputasi yang efisien antara konvolusi reparameterisasi untuk fitur tingkat rendah (*low-stage*) dan atensi mandiri (*self-attention*) untuk fitur tingkat tinggi (*high-stage*), Gold-YOLO meningkatkan akurasi deteksi secara signifikan tanpa mengorbankan kecepatan inferensi waktu nyata. Eksperimen menunjukkan model ini mencapai performa unggul pada dataset MS COCO dibanding model sekelas seperti YOLOv6 dan YOLOv8, serta menjadi pelopor implementasi pra-pelatihan mandiri (*self-supervised pretraining*) bergaya *Masked Autoencoder* (MAE) pada famili YOLO.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Dalam deteksi objek berbasis citra RGB, kemampuan mendeteksi objek dengan variasi skala yang ekstrem merupakan salah satu tantangan paling mendasar. Model detektor satu tahap modern, seperti seri YOLO, biasanya membagi arsitekturnya menjadi tiga bagian utama: *backbone* (untuk mengekstraksi fitur visual bertingkat dari citra masukan), *neck* (untuk menggabungkan fitur multiskala tersebut), dan *head* (untuk memprediksi koordinat *bounding box* dan probabilitas kelas). Secara historis, struktur *neck* seperti FPN memperkenalkan jalur atas-ke-bawah (*top-down*) untuk menyuntikkan informasi semantik tingkat tinggi ke lapisan spasial bawah, sedangkan PANet menambahkan jalur bawah-ke-atas (*bottom-up*) untuk mentransfer detail spasial kembali ke atas.

Namun, fusi rekursif bertahap pada FPN dan PANet memiliki kelemahan inheren berupa hilangnya informasi jarak jauh. Sebagai contoh, jika detail spasial halus dari peta fitur resolusi tinggi $B2$ ingin diintegrasikan dengan fitur semantik kaya di level $B5$, informasi tersebut harus mengalir secara berjenjang melalui lapisan perantara $B3$ dan $B4$. Di setiap langkah perantara, operasi konvolusi berulang dan kompresi saluran (*channel reduction*) secara perlahan mengikis detail informasi asli. Meskipun fusi global lintas-lapisan secara penuh dapat dilakukan menggunakan mekanisme atensi visual penuh (*global attention*), biaya komputasi kuadratisnya terlalu mahal untuk aplikasi waktu nyata yang harus berjalan pada perangkat tepi (*edge devices*) dengan keterbatasan daya. Oleh karena itu, diperlukan suatu metode fusi global efisien yang mampu menjembatani semua lapisan fitur tanpa meningkatkan latensi inferensi secara signifikan.

## Ide Utama

Gagasan inti dari Gold-YOLO adalah mendesain ulang interaksi fitur pada bagian *neck* dari model rantai bertahap menjadi model terpusat melalui mekanisme *Gather-and-Distribute* (GD). Alih-alih membiarkan informasi mengalir secara perlahan antar-lapisan tetangga, mekanisme GD mengumpulkan fitur dari semua lapisan secara paralel, meleburnya menjadi representasi global terpadu yang kaya akan konteks, lalu mendistribusikannya secara langsung ke tingkat-tingkat target pada piramida fitur.

Untuk mencapai efisiensi komputasi yang tinggi, proses GD ini dibagi menjadi dua cabang fusi yang disesuaikan dengan karakteristik fiturnya:
1. **Low-stage GD**: Bekerja pada fitur-fitur awal yang beresolusi tinggi (dari tingkat $B2$ hingga $B5$) untuk mempertahankan detail spasial objek kecil. Karena ukuran spasial peta fitur ini besar, modul ini menggunakan blok konvolusi yang direparameterisasi (*reparameterized convolutions*) seperti *RepBlock* untuk menjaga operasi tetap cepat dan hemat memori.
2. **High-stage GD**: Bekerja pada fitur-fitur dalam yang kaya akan informasi semantik abstrak (dari tingkat $P3$ hingga $P5$). Karena ukuran spasial peta fitur ini sudah mengecil, modul ini menggunakan blok berbasis *Transformer* (atensi mandiri atau *self-attention*) untuk memodelkan hubungan spasial-semantik global jarak jauh secara optimal.

Distribusi representasi global ini ke jalur deteksi utama tidak dilakukan melalui penjumlahan sederhana, melainkan menggunakan modul *Information Injection* (Injector) berbasis *gated attention* (atensi berpagar). Modul Injector ini secara dinamis menyaring informasi global mana yang relevan untuk memperkuat fitur lokal pada setiap tingkat deteksi tertentu.

## Cara Kerja Langkah demi Langkah

Mekanisme fusi dan distribusi informasi pada Gold-YOLO dapat divisualisasikan melalui diagram alir berikut:

```
       [Citra Input]
             │
        ┌────┴────┐
        │Backbone │
        └────┬────┘
      ┌───┬──┴┬───┐
     B2  B3  B4  B5  ◄─── Peta fitur multiskala dari backbone
      │   │   │   │
      └───┼───┼───┼──┐
          ▼   ▼   ▼  ▼
      ┌────────────────┐
      │  Low-stage GD  │ ◄─── (FAM + IFM RepBlock)
      └───────┬────────┘
        ┌─────┼─────┐
        ▼     ▼     ▼
       P3    P4    P5  ◄─── Injeksi fitur spasial tersaring
        │     │     │
        └─────┼─────┘
              ▼
      ┌────────────────┐
      │ High-stage GD  │ ◄─── (FAM + IFM Transformer)
      └───────┬────────┘
        ┌─────┼─────┐
        ▼     ▼     ▼
       N3    N4    N5  ◄─── Injeksi konteks semantik global
        │     │     │
        ▼     ▼     ▼
      ┌────────────────┐
      │ Detection Head │ ◄─── Prediksi koordinat & kelas
      └────────────────┘
```

Proses pemrosesan fitur ini berlangsung melalui tahapan-tahapan sistematis berikut:

### 1. Aliran Fitur Awal dari Backbone
Citra masukan beresolusi $640 \times 640$ piksel dimasukkan ke dalam *backbone* ekstraksi fitur. *Backbone* menghasilkan empat peta fitur bertingkat dengan dimensi spasial yang berbeda:
- $B2$: resolusi $160 \times 160$ piksel, dengan jumlah saluran $C_2$.
- $B3$: resolusi $80 \times 80$ piksel, dengan jumlah saluran $C_3$.
- $B4$: resolusi $40 \times 40$ piksel, dengan jumlah saluran $C_4$.
- $B5$: resolusi $20 \times 20$ piksel, dengan jumlah saluran $C_5$.

### 2. Modul Penyelaras Fitur (Feature Alignment Module - FAM)
Sebelum fitur-fitur dari berbagai tingkat dapat digabungkan, dimensi spasial dan jumlah saluran mereka harus diselaraskan. Tugas ini dijalankan oleh FAM.
- Di dalam **Low-stage FAM**, semua peta fitur $\{B2, B3, B4, B5\}$ diselaraskan ke resolusi target yang setara dengan dimensi $B3$ ($80 \times 80$ piksel). Penyelarasan dilakukan dengan cara menurunkan sampel (*downsampling*) peta fitur resolusi tinggi $B2$ ($160 \times 160$) menggunakan penapisan rata-rata (*average pooling*) berukuran $2\times 2$ menjadi $80 \times 80$. Sebaliknya, peta fitur beresolusi lebih rendah $B4$ ($40 \times 40$) dan $B5$ ($20 \times 20$) ditingkatkan sampelnya (*upsampled*) menggunakan interpolasi bilinear menjadi $80 \times 80$. Setelah semua dimensi spasial selaras pada ukuran $80 \times 80$ piksel, keempat tensor tersebut digabungkan sepanjang dimensi saluran (*channel concatenation*).
- Di dalam **High-stage FAM**, proses serupa dilakukan untuk menyelaraskan fitur $\{P3, P4, P5\}$ ke resolusi terkecil yaitu resolusi $P5$ ($20 \times 20$ piksel) menggunakan *average pooling*.

### 3. Modul Pelebur Informasi (Information Fusion Module - IFM)
Setelah diselaraskan oleh FAM, tensor gabungan dilebur di dalam IFM untuk menghasilkan satu representasi global yang padat.
- Pada **Low-stage IFM**, fusi fitur-fitur spasial resolusi tinggi dilakukan melalui blok *RepBlock* (blok konvolusi reparameterisasi). Blok ini menggunakan beberapa cabang konvolusi paralel saat pelatihan untuk mengekstrak representasi spasial yang kaya, yang kemudian dilebur secara matematis menjadi satu konvolusi $3\times 3$ tunggal saat inferensi. Hasil peleburan ini menghasilkan fitur global tingkat rendah yang disimbolkan sebagai $F_{align\_low}$.
- Pada **High-stage IFM**, fusi fitur-fitur semantik dalam dilakukan menggunakan blok *Transformer* dengan mekanisme atensi mandiri multi-kepala (*multi-head self-attention*). Blok ini menghitung hubungan ketergantungan jarak jauh antara seluruh piksel pada fitur tingkat tinggi untuk menghasilkan representasi global tingkat tinggi $F_{align\_high}$.

### 4. Modul Penyuntik Informasi (Information Injection Module - Injector)
Representasi global yang telah dilebur oleh IFM disuntikkan kembali ke jalur utama deteksi. Modul Injector menggunakan mekanisme atensi berpagar (*gated attention*) untuk mengontrol aliran informasi global secara adaptif.
Secara matematis, untuk tingkat fitur-$i$, proses injeksi dirumuskan sebagai:
$$F_{output} = F_{local\_i} + \text{Sigmoid}(\text{Conv}_{1\times 1}(F_{inj\_i})) \odot F_{local\_i}$$
Di sini, $F_{local\_i}$ adalah peta fitur lokal pada level-$i$. Peta fitur global $F_{inj\_i}$ disesuaikan dimensi spasialnya agar cocok dengan $F_{local\_i}$ menggunakan interpolasi bilinear (jika perlu ditingkatkan sampelnya) atau *average pooling* (jika perlu diturunkan sampelnya). Operasi konvolusi $1\times 1$ digunakan untuk menyelaraskan jumlah saluran. Hasilnya dilewatkan ke fungsi *Sigmoid* untuk menghasilkan peta atensi (*attention map*) spasial-saluran dengan nilai rentang $[0, 1]$. Peta atensi ini kemudian dikalikan secara elemen demi elemen (*element-wise multiplication* yang disimbolkan $\odot$) dengan fitur lokal asli, lalu ditambahkan kembali ke fitur lokal tersebut melalui koneksi residual.

### 5. Lightweight Adjacent-Layer Fusion (LAF)
Untuk memperkuat fusi lokal tanpa membebani komputasi global, Gold-YOLO mengintegrasikan modul LAF. Sebelum fitur lokal diproses oleh Injector, modul LAF mengalirkan informasi secara langsung dari lapisan yang bertetangga dekat (misalnya, menggabungkan fitur dari $P3$ dan $P5$ langsung ke $P4$). Hal ini memastikan transisi skala antar-lapisan tetap halus dan konsisten.

### 6. Pra-pelatihan Mandiri Bergaya MAE
Sebagai tambahan peningkatan akurasi, *backbone* detektor Gold-YOLO dilatih terlebih dahulu secara mandiri menggunakan skema MAE pada dataset ImageNet-1K. Selama pra-pelatihan, sebagian besar area citra ditutupi (dimasker), dan jaringan dipaksa merekonstruksi kembali piksel yang hilang. Pendekatan ini membuat *backbone* memiliki representasi fitur visual awal yang sangat kuat sebelum disetel halus (*fine-tuning*) pada dataset MS COCO untuk tugas deteksi objek akhir.

## Eksperimen dan Hasil

Evaluasi performa Gold-YOLO dilakukan pada dataset tolok ukur deteksi objek MS COCO val2017. Evaluasi ini membandingkan akurasi deteksi menggunakan metrik *mean Average Precision* pada rentang ambang IoU (*Intersection over Union*) 0,5 hingga 0,95 ($mAP_{val}$), jumlah parameter (dalam juta, M), biaya komputasi (dalam GFLOPs), dan kecepatan inferensi (dalam *millisecond*, ms).

Hasil eksperimen utama untuk varian model Gold-YOLO pada resolusi citra masukan $640 \times 640$ piksel dirangkum dalam tabel berikut:

| Model | Parameter (M) | FLOPs (G) | mAP (val 0.5:0.95) (%) | Latensi T4 (ms) |
|---|---|---|---|---|
| Gold-YOLO-N | 5,6 | 12,1 | 39,9 | 2,7 |
| Gold-YOLO-S | 21,5 | 46,0 | 46,4 | 4,2 |
| Gold-YOLO-M | 41,3 | 87,5 | 51,1 | 6,5 |
| Gold-YOLO-L | 75,1 | 151,7 | 53,3 | 9,8 |

*(Catatan: Latensi diukur pada GPU NVIDIA Tesla T4 menggunakan pustaka akselerasi TensorRT dengan presisi FP16 pada resolusi 640x640).*

Interpretasi hasil eksperimen ini menunjukkan efisiensi tinggi dari mekanisme GD dibandingkan model-model pembanding:
- **Gold-YOLO-N** (model terkecil) meraih akurasi $39,9\%$ mAP dengan hanya $5,6\text{ M}$ parameter. Hasil ini mengungguli model baseline YOLOv6-N ($37,5\%$ mAP) sebesar +2,4% mAP pada latensi yang setara, serta mengungguli YOLOv8-N ($37,3\%$ mAP) sebesar +2,6% mAP.
- **Gold-YOLO-S** meraih $46,4\%$ mAP, melampaui YOLOv6-S ($43,8\%$ mAP) sebesar +2,6% mAP dan YOLOv8-S ($44,9\%$ mAP) sebesar +1,5% mAP.
- Varian **Gold-YOLO-M** ($51,1\%$ mAP) dan **Gold-YOLO-L** ($53,3\%$ mAP) secara konsisten mengungguli detektor-detektor waktu nyata sekelas pada anggaran latensi yang sama.

Studi ablasi (*ablation study*) dalam makalah mengonfirmasi bahwa kontribusi peningkatan akurasi terbesar disumbangkan oleh modul *Gather-and-Distribute* (GD) pada *neck*, disusul oleh modul injeksi informasi (Injector), dan disempurnakan oleh inisialisasi bobot melalui pra-pelatihan bergaya MAE.

## Kelebihan dan Keterbatasan

### Kelebihan
- **Fusi Fitur Global Efektif**: Gold-YOLO memecahkan masalah redaman informasi spasial-semantik lintas-lapisan yang jauh dengan mengumpulkan seluruh fitur ke hub terpusat dan menyebarkannya secara langsung.
- **Latensi Rendah**: Pembagian kerja antara Low-stage GD (RepBlock konvolusional) and High-stage GD (Transformer) menjaga latensi inferensi tetap berada pada batas waktu nyata untuk perangkat tepi.
- **Akurasi Tinggi Objek Kecil**: Penyelarasan resolusi spasial tinggi pada tingkat *Low-stage* serta penapisan selektif oleh modul Injector membuat deteksi objek berukuran kecil meningkat secara signifikan.
- **Inisialisasi Bobot Optimal**: Implementasi pra-pelatihan mandiri bergaya MAE memberikan transfer representasi visual awal yang jauh lebih kuat dibanding pelatihan dari nol (*training from scratch*).

### Keterbatasan
- **Kompleksitas Implementasi Tinggi**: Secara rekayasa perangkat lunak, struktur *neck* yang memisahkan aliran data menjadi Low-stage dan High-stage GD lebih rumit untuk dimodifikasi secara manual atau disesuaikan dengan arsitektur *backbone* kustom di luar bawaannya.
- **Ketergantungan Akselerasi Perangkat Keras**: Penggunaan modul *Transformer* (atensi mandiri) pada High-stage IFM membutuhkan memori GPU yang cukup besar saat inferensi jika tidak dioptimalkan dengan TensorRT. Tanpa optimasi kompilator perangkat keras, kecepatan inferensi pada CPU perangkat tepi dapat turun drastis.
- **Biaya Pra-pelatihan Sangat Besar**: Konseptual pra-pelatihan MAE pada dataset ImageNet-1K membutuhkan sumber daya komputasi (GPU) dan waktu pelatihan yang sangat besar sebelum model dapat disetel halus untuk deteksi objek.

## Kaitan dengan Bab Lain

Gold-YOLO berdiri di atas fondasi deteksi satu tahap berbasis regresi yang diletakkan oleh YOLOv1 (Bab [001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)). Dari sisi garis silsilah arsitektur, Gold-YOLO mengadopsi struktur *backbone* dan *head* dari YOLOv6, namun mengganti bagian *neck* RepPAN konvensional dengan mekanismenya sendiri. Model ini bertindak sebagai pembanding langsung bagi detektor waktu nyata modern lainnya seperti YOLOv8 dan RT-DETR (Bab [155](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)), di mana RT-DETR memilih membuang komponen NMS (*Non-Maximum Suppression*) sepenuhnya menggunakan arsitektur berbasis *Query Transformer*.

Penerapan mekanisme atensi mandiri pada *High-stage IFM* Gold-YOLO juga dipengaruhi oleh keberhasilan pemodelan visual global jarak jauh yang ditunjukkan oleh arsitektur *backbone* Transformer seperti Swin Transformer V2 (Bab [163](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)) dan perbaikan konvolusi modern pada ConvNeXt (Bab [162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)). Selain itu, konsep fusi global terpusat ini memberikan alternatif arsitektur bagi detektor berbasis teks-citra seperti YOLO-World (Bab [156](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)) dalam menyelaraskan representasi visual dengan token bahasa secara global.

## Poin untuk Sitasi

Kutip makalah ini dengan kunci BibTeX: `wang2023goldyolo`.

Ringkasan aman untuk dikutip dalam tinjauan pustaka:
> "Gold-YOLO memperkenalkan mekanisme Gather-and-Distribute (GD) pada bagian neck detektor untuk mengatasi kelemahan transmisi bertahap FPN/PAN. Dengan mengumpulkan seluruh fitur ke dalam hub terpusat dan mendistribusikannya kembali secara langsung menggunakan modul Injector atensi berpagar, Gold-YOLO meningkatkan akurasi deteksi multi-skala pada dataset MS COCO (39,9% hingga 53,3% mAP) dengan tetap mempertahankan kecepatan inferensi waktu nyata."

Catatan verifikasi sebelum sitasi formal:
- Pastikan angka latensi yang diukur pada GPU Tesla T4 (2,7 ms hingga 9,8 ms) tidak tertukar dengan kecepatan FPS mentah tanpa TensorRT.
- Konfirmasikan bahwa versi baseline YOLOv6 yang digunakan sebagai pembanding utama adalah YOLOv6 v3.0, karena versi ini menentukan keadilan perbandingan performa pada bab eksperimen.
- Validasi keberhasilan transfer bobot pra-pelatihan MAE pada citra masukan terhadap dataset khusus di luar MS COCO jika model ini diterapkan pada tugas klasifikasi atau segmentasi hilir.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract In the past years, YOLO-series models have emerged as the leading approaches in the area of real-time object detection. Many studies pushed up the baseline to a higher level by modifying the architecture, augmenting data and designing new losses. However, we find previous models still suffer from information fusion problem, although Feature Pyramid Network (FPN) and Path Aggregation Network (PANet) have alleviated this. Therefore, this study provides an advanced Gatherand-Distribute mechanism (GD) mechanism, which is realized with convolution and self-attention operations. This new designed model named as Gold-YOLO, which boosts the multi-scale feature fusion capabilities and achieves an ideal balance between latency and accuracy across all model scales. Additionally, we implement MAE-style pretraining in the YOLO-series for the first time, allowing YOLO-series models could be to benefit from unsupervised pretraining. Gold-YOLO-N attains an outstanding 39.9% AP on the COCO val2017 datasets and 1030 FPS on a T4 GPU, which outperforms the previous SOTA model YOLOv6-3.0-N with similar FPS by +2.4%. The PyTorch code is available at https://github.com/huawei-noah/EfficientComputing/tree/master/Detection/Gold-YOLO, and the MindSpore code is available at https://gitee.com/mindspore/models/tree/master/research/cv/Gold_YOLO.

Introduction

Object detection as a fundamental vision task that aims to recognize the categories and locate the positions of objects. It can be widely used in a wide range of applications, such as intelligent security, autonomous driving, robot navigation, and medical diagnosis. High-performance and low-latency object detector is receiving increasing attention for deployment on the edge devices. Over the past few years, researchers have extensive research on CNN-based detection networks, gradually evolving the object detection framework from two-stage (e.g., Faster RCNN [42] and Mask RCNN [25]) to one-stage (e.g., YOLO [39]), and from anchor-based (e.g., YOLOv3 [41] and YOLOv4 [2]) to anchor-free (e.g., CenterNet [10], FCOS [46] and YOLOX [11]). [12, 7, 17] studied the optimal network structure through NAS for object detection task, and [16, 23, 19] explore another way to improve the performance of the model by distillation. Single-stage detection models, especially YOLO series models, have been widely welcomed in the industry due to their simple structure and balance between speed and accuracy. Improvement of backbone is also an important research direction in the field of vision. As described in the survey [20], [26, 27, 59, 21] has achieved a balance between precision and speed, while [9, 35, 22, 18] has shown strong performance in precision. These backbones have improved the performance of the original model in different visual tasks, ranging from high-level tasks like object ∗

Figure 1: Comparison of state-of-the-art efficient object detectors in Tesla T4 GPU. Both latency and throughput (batch size of 32) are given for a handy reference. (a) and (b) test with TensorRT 7 and 8, respectively. detection to low-level tasks like image restoration. By using the encoder-decoder structure with the transformer, researchers have constructed a series of DETR-like object detection models, such as DETR [3] and DINO [56]. These models can capture long-range dependency between objects, enabling transformer-based detectors to achieve comparable or superior performance with most refined classical detectors. Despite the notable performance of transformer-based detectors,they fall short when compared to the speed of CNN-based models. Small-scale object detection models based on CNN still dominate the speed-accuracy trade-off, such as YOLOX [11] and YOLOv6-v8 [32,focus 48, 14]. We on the real-time object detection models, especially YOLO series for mobile deployment. Mainstream real-time object detectors consist of three parts: backbone, neck, and head. The backbone architecture has been widely investigated [41, 43, 9, 35] and the head architecture is typically straight forward, consisting of several convolutional or fully-connected layers. The necks in YOLO series usually use Feature Pyramid Network (FPN) and its variants to fuse multi-level features. These neck modules basically follow the architecture shown in Fig. 3. However, the current approach to information fusion has a notable flaw: when there is a need to integrate information across layers (e.g., level-1 and level-3 are fused), the conventional FPN-like structure fails to transmit information without loss, which hinders YOLOs from better information fusion. Built upon the concept of global information fusion, TopFormer [58] has achieved remarkable results in semantic segmentation tasks. In this paper, we expanding on the foundation of TopFormer’s theory, propose a novel Gather-and-Distribute mechanism (GD) for efficient information exchanging in YOLOs by globally fusing multi-level features and injecting the global information into higher levels. This significantly enhances the information fusion capability of the neck without significantly increasing the latency, improving the model’s performance across varying object sizes. Specifically, GD mechanism comprises two branches: a shallow gather-and-distribute branch and a deep gatherand-distribute branch, which extract and fuse feature information via a convolution-based block and an attention-based block, respectively. To further facilitate information flow, we introduce a lightweight adjacent-layer fusion module which combines features from neighboring levels on a local scale. Our Gold-YOLO architectures surpasses the existing YOLO series, effectively demonstrating the effectiveness of our proposed approach. To further improve the accuracy of the model, we also introduce a pre-training method, where we pre-train the backbone on ImageNet 1K using the MAE method, which significantly improves the convergence speed and accuracy of the model. For example, our Gold-YOLO-S with pre-training achieves 46.4% AP, which outperforms the previous SOTA YOLOv6-3.0-S with 45.0% AP at similar speed.

Related works

2.1 Real-time object detectors After years of development, the YOLO-series model has become popular in the real-time object detection area. YOLOv1-v3 [39, 40, 41] constructs the initial YOLOs, identifies a single-stage 2

Figure 2: The architecture of the proposed Gold-YOLO. detection structure consisting of three parts, backbone-neck-head, predicts objects of different sizes through multi-scale branches, become a representative single-stage object detection model. YOLOv4 [2] optimizes the previously used darknet backbone structure and propose a series of improvements, like the Mish activation function, PANet and data augmentation methods. YOLOv5 [13] inheriting the YOLOv4 [2] scheme with improved data augmentation strategy and a greater variety of model variants. YOLOX [11] incorporates Multi positives, Anchor-free, and Decoupled Head into the model structure, setting a new paradigm for YOLO-model design. YOLOv6 [32, 31] brings the reparameterization method to YOLO-series models for the first time, proposing EfficientRep Backbone and Rep-PAN Neck. YOLOv7 [48] focuses on analyzing the effect of gradient paths on the model performance and proposes the E-ELAN structure to enhance the model capability without destroying the original gradient paths. The YOLOv8 [14] takes the strengths of previous YOLO models and integrates them to achieve the SOTA of the current YOLO family. 2.2

Vision Transformer (ViT) emerged as a competitive alternative to convolutional neural networks (CNNs) that are widely used for different image recognition tasks. DETR [3] applies the transformer structure to the object detection task, reconstructing the detection pipeline and eliminating many handdesigned parts and NMS components to simplify the model design and overall process. Combining the sparse sampling capability of deformable convolution with the global relationship modeling capability of transformer, Deformable DETR [61] improve convergence speed while improve model speed and accuracy. DINO [56] first time introduced Contrastive denoising, Mix query selection and a look forward twice scheme. The recent RT-DETR [36] improved the encoder-decoder structure to solve the slow DETR-like model problem, outperforming YOLO-L/X in both accuracy and speed. However, the limitations of the DETR-like structure prevent it from showing sufficient dominance in the small model region, where YOLOs remain the SOTA of accuracy and velocity balance. 2.3

Traditionally, features at different levels carry positional information about objects of various sizes. Larger features encompass low-dimensional texture details and positions of smaller objects. In contrast, smaller features contain high-dimensional information and positions of larger objects. The original idea behind Feature Pyramid Networks (FPN) proposed by [34] is that these diverse pieces of information can enhance network performance through mutual assistance. FPN provides an efficient architectural design for fusing multi-scale features through cross-scale connections and information exchange, thereby boosting the detection accuracy of objects of varied sizes. Based on FPN, the Path Aggregation Network (PANet) [49] incorporates a bottom-up path to make information fusion between different levels more adequate.Similarly, EfficientDet [44] presents a new repeatable module (BiFPN) to increase the efficiency of information fusion between different levels. M2Det [60] introduced an efficient MLFPN architecture with U-shape and Feature Fusion Modules. Ping-Yang Chen [5] improved interaction between deep and shallow layers using bidirectional fusion modules. Unlike these inter-layer works, [37] explored individual feature information using the Centralized Feature Pyramid (CFP) method. Additionally, [53] extended FPN with the Asymptotic Feature Pyramid Network (AFPN) to interact across non-adjacent layers. In response to FPN’s limitations in detecting large objects, [30] proposed a refined FPN structure. YOLO-F [6] achieved 3

Figure 3: (a) is example diagram of traditional neck information fusion structure. (b) and (c) is AblationCAM [38] visualization

state-of-the-art performance with single-level features. SFNet [33] aligns different level features with semantic flow to improves FPN performance in model. SAFNet [29] introduced Adaptive Feature Fusion and Self-Enhanced Modules. [4] presented a parallel FPN structure for object detection with bi-directional fusion.However, due to the excessive number of paths and indirect interaction methods in the network, the previous FPN-based fusion structures still have drawbacks in low speed, cross-level information exchange and information loss. However, due to the excessive number of paths and indirect interaction methods in the network, the previous FPN-based fusion structures still have drawbacks in low speed, cross-level information exchange and information loss.

Method

Preliminaries

The YOLO series neck structure, as depicted in Fig.3, employs a traditional FPN structure, which comprises multiple branches for multi-scale feature fusion. However, it only fully fuse features from neighboring levels, for other layers information it can only be obtained indirectly ‘recursively’. In Fig.3, it shows the information fusion structure of the conventional FPN: where existing level-1, 2, and 3 are arranged from top to bottom. FPN is used for fusion between different levels. There are two distinct scenarios when level-1 get information from the other two levels: 1) If level-1 seeks to utilize information from level-2, it can directly access and fuse this information. 2) If level-1 wants to use level-3 information, level-1 should recursively calling the information fusion module of the adjacent layer. Specifically, the level-2 and level-3 information must be fused first, then level-1 can indirectly obtain level-3 information by combining level-2 information. This transfer mode can result in a significant loss of information during calculation. Information interactions between layers can only exchange information that is selected by intermediate layers, and not selected information is discarded during transmission. This leads to a situation where information at a certain level can only adequately assist neighboring layers and weaken the assistance provided to other global layers. As a result, the overall effectiveness of the information fusion may be limited. To avoid information loss in the transmission process of traditional FPN structures, we abandon the original recursive approach and construct a novel gather-and-distribute mechanism (GD). By using a unified module to gather and fuse information from all levels and subsequently distribute it to different levels, we not only avoid the loss of information inherent in the traditional FPN structure but also enhance the neck’s partial information fusion capabilities without significantly increasing latency. Our approach thus allows for more effective leveraging of the features extracted by the backbone, and can be easily integrated into any existing backbone-neck-head structure. 4

In our implementation, the process gather and distribute correspond to three modules: Feature Alignment Module (FAM), Information Fusion Module (IFM), and Information Injection Module (Inject). • The gather process involves two steps. Firstly, the FAM collects and aligns features from various levels. Secondly, IFM fuses the aligned features to generate global information. • Upon obtaining the fused global information from the gather process, the inject module distribute this information across each level and injects it using simple attention operations, subsequently enhancing the branch’s detection capability. To enhance the model’s ability to detect objects of varying sizes, we developed two branches: lowstage gather-and-distribute branch (Low-GD) and high-stage gather-and-distribute branch (High-GD). These branches extract and fuse large and small size feature maps, respectively. Further details are provided in Sections 4.1 and 4.2. As shown in Fig. 2, the neck’s input comprises the feature maps B2, B3, B4, B5 extracted by the backbone, where Bi ∈ RN ×CBi ×RBi . The batch size is denoted by N , the channels by C, and the dimensions by R = H × W . Moreover, the dimensions of RB2 , RB3 , RB4 , and RB5 are R, 12 R, 14 R, and 18 R, respectively. 3.2

In this branch, the output B2, B3, B4, B5 features from the backbone are selected for fusion to obtain high resolution features that retain small target information. The structure show in Fig.4(a) Low-stage feature alignment module. In low-stage feature alignment module (Low-FAM), we employ the average pooling (AvgPool) operation to down-sample input features and achieve a unified size. By resizing the features to the smallest feature size of the group (RB4 = 14 R), we obtain Falign . The Low-FAM technique ensures efficient aggregation of information while minimizing the computational complexity for subsequent processing through the transformer module. The target alignment size is chosen based on two conflicting considerations: (1) To retain more low-level information, larger feature sizes are preferable; however, (2) as the feature size increases, the computational latency of subsequent blocks also increases. To control the latency in the neck part, it is necessary to maintain a smaller feature size. Therefore, we choose the RB4 as the target size of feature alignment to achieve a balance between speed and accuracy. Low-stage information fusion module. The low-stage information fusion module (Low-IFM) design comprises multi-layer reparameterized convolutional blocks (RepBlock) and a split operation. Specifically, RepBlock takes Falign (channel = sum(CB2 , CB3 , CB4 , CB5 )) as input and produces Ff use (channel = CB4 + CB5 ). The middle channel is an adjustable value (e.g., 256) to accommodate varying model sizes. The features generated by the RepBlock are subsequently split in the channel dimension into Finj_P 3 and Finj_P 4 , which are then fused with the different level’s feature. The formula is as follows: Falign = Low_F AM ([B2, B3, B4, B5]) , Ffuse = RepBlock (Falign ) , Finj_P3 , Finj_P4 = Split(Ffuse ).

Information injection module. In order to inject global information more efficiently into the different levels, we draw inspiration from the segmentation experience [47] and employ attention operations to fuse the information, as illustrated in Fig. 5. Specifically, we input both local information (which refers to the feature of the current level) and global inject information (generated by IFM), denoted as Flocal and Finj , respectively. We use two different Convs with Finj for calculation, resulting in Fglobal_embed and Fact . While Flocal_embed is calculated with Flocal using Conv. The fused feature Fout is then computed through attention. Due to the size differences between Flocal and Fglobal , we employ average pooling or bilinear interpolation to scale Fglobal_embed and Fact according to the size of Finj , ensuring proper alignment. At the end of each attention fusion, we add the RepBlock to further extract and fuse the information. 5

Figure 4: Gather-and-Distribute structure. In (a), the Low-FAM and Low-IFM is low-stage feature alignment module and low-stage information fusion module in low-stage branch, respectively. In (b), the High-FAM and High-IFM is high-stage feature alignment module and high-stage information fusion module, respectively. In low stage, Flocal is equal to Bi, so the formula is as follows:

The High-GD fuses the features {P 3, P 4, P 5} that are generated by the Low-GD, as shown in Fig.4(b) High-stage feature alignment module. The high-stage feature alignment module (High-FAM) consists of avgpool, which is utilized to reduce the dimension of input features to a uniform size. Specifically, when the size of the input feature is {RP 3 , RP 4 , RP 5 }, avgpool reduces the feature size to the smallest size within the group of features (RP 5 = 18 R). Since the transformer module extracts high-level information, the pooling operation facilitates information aggregation while decreasing the computational requirements for the subsequent step in the Transformer module. High-stage information fusion module. The high-stage information fusion module (High-IFM) comprises the transformer block (explained in greater detail below) and a splitting operation, which involves a three-step process: (1) the Falign , derived from the High-FAM, are combined using the transformer block to obtain the Ff use . (2) The Ff use channel is reduced to sum(CP 4 , CP 5 ) via a Conv1 × 1 operation. (3) The Ff use is partitioned into Finj_N 4 and Finj_N 5 along the channel dimension through a splitting operation, which is subsequently employed for fusion with the current level feature. The formula is as follows: Falign = High_F AM ([P 3, P 4, P 5]), Ffuse = T ransf ormer(Falign ), Finj_N4 , Finj_N5 = Split(Conv1 × 1(Ffuse )).

The transformer fusion module in Eq. 8 comprises several stacked transformers, with the number of transformer blocks denoted by L. Each transformer block includes a multi-head attention block, a Feed-Forward Network (FFN), and residual connections. To configure the multi-head attention block, we adopt the same settings as LeViT [15], assigning head dimensions of keys K and queries Q to D (e.g., 16) channels, and V = 2D (e.g., 32) channels. In order to accelerate inference, we substitute the velocity-unfriendly operator, Layer Normalization, with Batch Normalization for each convolution, and replace all GELU activations with ReLU. This minimizes the impact of the transformer module on the model’s speed. To establish our Feed-Forward Network, we follow the methodologies presented in [28, 55] for constructing the FFN block. To enhance the local connections of the transformer block, we introduce a depth-wise convolution layer between the two 1x1 convolution layers. We also set the expansion factor of the FFN to 2, aiming to balance speed and computational cost. 6

We have achieved better performance than existing methods using only a global information fusion structure. To further enhance the performance, we drew inspiration from the PAFPN module in YOLOv6 [31] and introduced an Inject-LAF module. This module is an enhancement of the injection module and includes a lightweight adjacent layer fusion (LAF) module that is added to the input position of the injection module. To achieve a balance between speed and accuracy, we designed two LAF models: LAF low-level model and LAF high-level model, which are respectively used for low-level injection (merging features from adjacent two layers) and high-level injection (merging features from adjacent one layer). There structure is shown in Fig. 5 (b). To ensure that feature maps from different levels are aligned with the target size, the two LAF models in our implementation utilize only three operators: bilinear interpolation to up-sample features that are too small, average pooling to down-sample features that are too large, and 1x1 convolution to adjust features that differ from the target channel. The combination of the LAF module with the information injection module in our model effectively balances the between accuracy and speed. By using simplified operations, we are able to increase the number of information flow paths between different levels, resulting in improved performance without significantly increased the latency. 3.5

Table 1: Comparisons with other YOLO-series detectors on COCO 2017 val. FPS and latency are measured in FP16-precision on a Tesla T4 in the same environment with TensorRT 7. All our models are trained for 300 epochs. Both the accuracy and the speed performance of our models are evaluated with the input resolution of 640x640. ‘†’ represents that the self-distillation method is utilized, and ‘⋆’ represents that the MIM pre-training method is utilized. Method

convolutional networks (convnets). These challenges include the convolutional operations’ inability to handle irregular and randomly masked input images, as well as the inconsistency between the single-scale nature of BERT pretraining and the hierarchical structure of convnets. To address the first issue, unmasked pixels are treated as sparse voxels of 3D point clouds and employ sparse convolution for encoding. For the latter issue, a hierarchical decoder is developed to reconstruct images from multi-scale encoded features. The framework adopts a UNet-style architecture to decode multi-scale sparse feature maps, where all spatial positions are filled with embedded masks. We pretrain our model’s backbone on ImageNet 1K for multiple Gold-YOLO models, and results in notable improvements

Experiment

Datasets. We perform extensive experiments on the Microsoft COCO datasets to validate the proposed detector. For the ablation study, we train on COCO train2017 and validate on COCO val2017 datasets. We use the standard COCO AP metric with a single scale image as input, and report the standard mean average precision (AP) result under different IoU thresholds and object scales. Implementation details. We followed the setup of YOLOv6-3.0 [31] use the same structure (except for neck) and training configurations. The backbone of the network was implemented with 8

the EfficientRep Backbone, while the head utilized the Efficient Decoupled Head. The optimizer learning schedule and other setting also same as YOLOv6, i.e. stochastic gradient descent (SGD) with momentum and cosine decay on learning rate. Warm-up, grouped weight decay strategy and the exponential moving average (EMA) are utilized. Self-distillation and anchor-aided training (AAT) also be used in training. The strong data augmentations we adopt Mosaic [2, 13] and Mixup [57]. We conducted MIM unsupervised pretraining on the backbone using the 1.28 million ImageNet-1K datasets [8]. Following the experiment settings in Spark [45], we employed a LAMB optimizer [54] and cosine-annealing learning rate strategy, with a masking ratio of 60 % and a mask patch size of 32. For the Gold-YOLO-L models, we employed a batch size of 1024, while for the Gold-YOLO-M models, a batch size of 1152 was used. MIM pretraining was not employed for Gold-YOLO-N due to the limited capacity of its small backbone. All our models are trained on 8 NVIDIA A100 GPUs, and the speed performance is measured on an NVIDIA Tesla T4 GPU with TensorRT. 4.2

Ablation study Ablation study on GD structure

To verify the validity of our analysis concerning the FPN and to assess the efficacy of the proposed gather-and-distribute mechanism, we examined each module in GD independently, focusing on AP, number of parameters, and latency on the T4 GPU. The Low-GD predominantly targets small and medium-sized objects, whereas the High-GD primarily detect large-sized objects, and the LAF module bolsters both branches. The experimental results are displayed in Table 2 . Table 2: Ablation study on GD structure. The test model is Gold-YOLO-S on T4 GPU evaluate. Low-GD

Ablation study on LAF

In this ablation study, we conducted experiments to compare the effects of different module designs within the LAF framework and evaluate the influence of varying model sizes on accuracy. The 9

results of our study provide evidence to support the assertion that the existing LAF structure is indeed optimal. The difference between model-1 and model-2 is whether LAF uses add or concat, and model-3 increase the model size basis of model-2. The model-4 is based on model-3 but discards LAF. The experimental results are displayed in Table 3 . Table 3: Ablation study on LAF. Use TensorRT 7 on T4 GPU evaluate. model concat

Ablation study on other model and task

The GD mechanism is a general concept and can be applied beyond YOLOs. We have extend GD mechanism to other models and obtain significant improvement. On Instance Segmentation task, we replace different necks in Mask R-CNN and train/test on the COCO instance datasets. The result as shown in the Table 4. Table 4: Ablation study on Instance Segmentation Task. Model

On Semantic Segmentation task, we replace different necks in PointRend and train/test on the Cityscapes datasets. The result as shown in the Table 5. Table 5: Ablation study on Semantic Segmentation Task. Model

Table 6: Performance of GD mechanism on other object detection models. model

On object detection task, we replace different necks in EfficientDet and train/test on the COCO datasets. The result as shown in the Table 6.

Conclusion

In this paper, we revisit the traditional Feature Pyramid Network (FPN) architecture and critically analyze its constraints in terms of information transmission. Following this, we subsequently developed the Gold-YOLO series models for object detection tasks, achieving state-of-the-art results. In Gold-YOLO we introduce an innovative gather-and-distribute mechanism, strategically designed to enhance the efficacy and efficiency of information fusion and transmission, avoid unnecessary losses, thereby significantly improving the model’s detection capabilities. We truly hope that our work will prove valuable in addressing real-world problems and may also ignite fresh ideas for researchers in this field.

Acknowledgement We gratefully acknowledge the support of MindSpore, CANN (Compute Architecture for Neural Networks) and Ascend AI Processor used for this research.
