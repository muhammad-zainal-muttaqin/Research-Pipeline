# 006 - YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022yolov6` |
| Judul asli | YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications |
| Penulis | Chuyi Li, Lulu Li, Hongliang Jiang, Kaiheng Weng, Yifei Geng, Liang Li, dkk. (Meituan Inc.) |
| Tahun | 2022 |
| Venue | arXiv preprint arXiv:2209.02976 (laporan teknis) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2209.02976
- **Repositori kode resmi (Meituan):** https://github.com/meituan/YOLOv6
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications&sort=relevance

## Gambaran Umum

YOLOv6 adalah detektor objek satu tahap — model yang memprediksi lokasi dan kelas seluruh objek dalam satu kali evaluasi jaringan — yang dikembangkan tim Meituan dan dirilis sebagai laporan teknis pada September 2022. Alih-alih mengusulkan paradigma baru, makalah ini merancang ulang kerangka YOLO agar optimal pada perangkat keras produksi: kecepatan diukur pada GPU kelas menengah NVIDIA Tesla T4, arsitektur dipilih berbeda per ukuran model, dan kuantisasi (konversi bobot dan aktivasi menjadi integer 8 bit) menjadi bagian rancangan sejak awal.

Hasilnya lima model (N, T, S, M, L) dengan kombinasi akurasi-kecepatan terdepan pada COCO saat dirilis. YOLOv6-N mencapai 35,9% AP dengan *throughput* (citra per detik) 1234 FPS; YOLOv6-S mencapai 43,5% AP pada 495 FPS, melampaui YOLOv5-S, YOLOX-S, dan PP-YOLOE-S sekelasnya; versi terkuantisasinya mencapai 43,3% AP pada 869 FPS.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv4 (bab 004) merapikan kerangka detektor menjadi *backbone*, *neck*, dan *head*, lini YOLO berkembang melalui YOLOv5, YOLOX (bab 005), PP-YOLOE, dan YOLOv7. Namun industri menuntut hal lain dari tolok ukur: latensi rendah pada perangkat spesifik, kuantisasi mudah, dan beberapa ukuran model. Penulis mengidentifikasi lima celah:

1. Reparameterisasi struktural — melatih jaringan dalam bentuk bercabang lalu meleburnya menjadi konvolusi tunggal saat inferensi, dipopulerkan RepVGG — belum dimanfaatkan baik pada deteksi; arsitektur jalur tunggalnya juga tumbuh eksplosif biayanya bila diperbesar.
2. Kuantisasi model berbasis reparameterisasi mudah merusak akurasi karena konfigurasinya berbeda antara pelatihan (bercabang) dan inferensi (lebur).
3. Latensi detektor sebelumnya umumnya diukur pada GPU mahal seperti V100, bukan GPU produksi seperti Tesla T4.
4. Strategi penetapan label dan fungsi loss mutakhir perlu diverifikasi ulang untuk tiap arsitektur.
5. Perbaikan yang menambah biaya pelatihan tetapi tidak menambah biaya inferensi — misalnya distilasi pengetahuan — dapat diterima industri dan layak dieksploitasi.

## Ide Utama

Gagasan inti YOLOv6 adalah merancang ulang kerangka YOLO dengan satu kriteria: setiap komponen dipilih berdasarkan bukti ablasi, dan arsitektur boleh berbeda antar-ukuran. Model kecil memakai *backbone* jalur tunggal berbasis reparameterisasi karena paling cepat pada perangkat nyata; model besar memakai blok multi-cabang yang lebih hemat parameter. Semua teknik yang menaikkan akurasi tanpa menambah biaya inferensi — penetapan label TAL, fungsi loss yang tepat, distilasi diri, pelatihan lebih lama — dipakai, dan kuantisasi diperbaiki dari sisi pelatihan agar model INT8 tetap akurat.

## Cara Kerja Langkah demi Langkah

### Gambaran Alur Data

*Backbone* adalah jaringan ekstraksi fitur yang menurunkan citra 640×640 piksel menjadi beberapa peta fitur yang semakin kecil. *Neck* menggabungkan fitur dangkal (kaya informasi posisi) dengan fitur dalam (kaya semantik) menjadi piramida fitur multi-skala. *Head* menghasilkan prediksi kelas dan kotak objek dari fitur gabungan tersebut.

```
                ALUR DATA YOLOv6 (model N/T/S; masukan 640x640)

 citra 640 x 640
      |
      v
+------------------------------------------------------------+
| BACKBONE - EfficientRep                                    |
| pelatihan : RepBlock = tumpukan blok RepVGG bercabang      |
| inferensi : tiap blok dilebur jadi RepConv (conv 3x3+ReLU) |
+------------------------------------------------------------+
      | peta fitur multi-skala
      v
+------------------------------------------------------------+
| NECK - Rep-PAN                                             |
| topologi PAN (agregasi atas-bawah + bawah-atas),           |
| blok CSP diganti RepBlock (model besar: CSPStackRep)       |
+------------------------------------------------------------+
      | fitur gabungan tiap skala
      v
+------------------------------------------------------------+
| HEAD - Efficient Decoupled Head (anchor-free)              |
| satu conv 3x3 bersama, lalu dua cabang:                    |
|   +-- klasifikasi -> skor kelas per titik                  |
|   +-- regresi     -> jarak titik ke 4 sisi kotak           |
+------------------------------------------------------------+
```

Diagram di atas menegaskan bahwa blok bercabang hanya ada saat pelatihan, lalu dilebur menjadi konvolusi tunggal untuk inferensi. Keluaran *head* tiap skala berupa skor kelas per titik dan empat jarak ke sisi-sisi kotak objek.

### Backbone: EfficientRep dan CSPStackRep

Untuk model kecil (N/T/S), backbone EfficientRep dibangun dari RepBlock: tumpukan blok gaya RepVGG yang saat pelatihan bercabang tiga (konvolusi 3×3, konvolusi 1×1, dan koneksi identitas), masing-masing diikuti *batch normalization* (lapisan yang menormalkan aktivasi agar stabil). Setelah pelatihan, ketiga cabang yang memperkaya gradien ini dilebur menjadi satu konvolusi 3×3 setara yang disebut RepConv, diikuti aktivasi ReLU.

```
  REPARAMETERISASI STRUKTURAL SATU BLOK (gaya RepVGG)

  saat pelatihan (3 cabang)       saat inferensi (1 jalur)

        masukan                         masukan
   +------+-------+                         |
 conv3x3 conv1x1 identitas             conv 3x3 tunggal
   |      |       |                   (ketiga cabang dan
   +------+-------+                    batchnorm dilebur)
       jumlah                             |
         |                             keluaran
      keluaran
```

Peleburan ini tepat secara matematis: konvolusi 1×1 dan identitas setara dengan konvolusi 3×3 berkernel *padding*, lalu dijumlahkan, dan konvolusi 3×3 jalur tunggal sangat efisien pada GPU umum. Namun pada model besar, parameter dan biaya komputasinya tumbuh eksplosif, sehingga M dan L memakai CSPStackRep Block: tumpukan sub-blok berisi dua RepConv dengan koneksi residual (jalan pintas yang menjumlahkan masukan dan keluaran blok), dibungkus koneksi CSP (*Cross Stage Partial*: peta fitur dibagi dua, satu melewati blok dan satu dilewatkan langsung, lalu digabung kembali) untuk memangkas komputasi tanpa kehilangan keragaman gradien.

### Neck: Rep-PAN

Neck YOLOv6 mengadopsi topologi PAN (*Path Aggregation Network*) dari YOLOv4 dan YOLOv5: piramida fitur dengan jalur agregasi dua arah (dari fitur dalam ke dangkal dan sebaliknya), sehingga tiap skala memuat semantik dan detail posisi. Rep-PAN berbeda dari PAN YOLOv5 pada blok pembangunnya: blok CSP diganti RepBlock (model kecil) atau CSPStackRep Block (model besar).

### Head: Efficient Decoupled Head dan Anchor-Free

*Decoupled head* adalah head yang memisahkan cabang klasifikasi dan cabang regresi kotak; head YOLOv5 sebaliknya bersifat *coupled* (kedua tugas berbagi parameter). FCOS dan YOLOX menambahkan dua konvolusi 3×3 pada tiap cabang; YOLOv6 menyederhanakannya lewat strategi *hybrid-channel* (satu konvolusi 3×3 di tengah, lebarnya mengikuti backbone dan neck), sehingga latensi turun dengan penurunan akurasi minimal.

Head ini juga bersifat *anchor-free*: prediksi bukan offset terhadap *anchor box* (kotak acuan berukuran tetap yang dirancang sebelumnya), melainkan jarak dari sebuah titik (*anchor point*) ke empat sisi kotak objek. Dekode lebih sederhana dan pasca-pemrosesan lebih cepat karena kandidat keluaran berkurang hingga sepertiga.

### Penetapan Label: TAL

*Label assignment* adalah proses saat pelatihan untuk menentukan prediksi mana yang bertanggung jawab (contoh positif) atas setiap objek kebenaran. Versi awal YOLOv6 memakai SimOTA (strategi warisan YOLOX yang merumuskan penetapan label sebagai masalah transport optimal), tetapi SimOTA memperlambat dan tidak jarang mendestabilkan pelatihan. Sebagai gantinya dipakai TAL (*Task Alignment Learning*, dari TOOD): metrik tunggal gabungan skor klasifikasi dan kualitas kotak menjadi kriteria penetapan, sehingga ketidakselarasan kedua tugas berkurang.

### Fungsi Loss

Untuk loss klasifikasi, YOLOv6 memilih VFL (*Varifocal Loss*) setelah menguji Focal Loss, Poly Loss, dan QFL; VFL adalah turunan Focal Loss (modifikasi *cross-entropy* yang menekan kontribusi contoh mudah) yang memperlakukan contoh positif dan negatif secara asimetris sehingga sinyal belajarnya seimbang. Untuk loss regresi dipakai keluarga loss IoU. IoU (*Intersection over Union*) adalah rasio luas irisan terhadap gabungan dua kotak; GIoU tetap memberi gradien pada kotak tak beririsan, sedangkan SIoU menambahkan penalti sudut, jarak pusat, dan bentuk. YOLOv6 memakai SIoU untuk N dan T, dan GIoU untuk sisanya. DFL (*Distribution Focal Loss*) memodelkan posisi tiap sisi kotak sebagai distribusi probabilitas diskrit 17 nilai, bukan satu angka, sehingga lokalisasi batas yang kabur membaik; karena keluarannya 17 kali lebih besar, DFL hanya dipakai pada M dan L. Loss objektivitas (penalti untuk kotak berkualitas rendah, dari FCOS dan YOLOX) dicoba tetapi dibuang karena menurunkan akurasi.

### Distilasi Diri dan Durasi Pelatihan

*Knowledge distillation* melatih model murid agar meniru keluaran model guru dengan meminimalkan divergensi KL (ukuran selisih dua distribusi probabilitas). YOLOv6 memakai distilasi diri: gurunya adalah arsitektur yang sama yang sudah dilatih sebelumnya, sehingga tanpa biaya inferensi tambahan. Distilasi diterapkan pada klasifikasi dan, berkat DFL yang menghasilkan distribusi, juga pada regresi. Bobot loss distilasi meluruh mengikuti kurva kosinus: label lunak guru lebih mudah dipelajari di awal, label keras lebih bermanfaat di akhir. Durasi pelatihan juga diperpanjang dari 300 menjadi 400 epoch.

### Kuantisasi untuk Penerapan

PTQ (*post-training quantization*) mengkuantisasi model terlatih memakai himpunan kalibrasi kecil; QAT (*quantization-aware training*) menyisipkan kuantisasi tiruan selama pelatihan. Keduanya bermasalah pada model berbasis reparameterisasi karena struktur pelatihan dan inferensinya berbeda. YOLOv6 memperbaikinya dengan tiga langkah: (1) pelatihan memakai RepOptimizer, yang melakukan reparameterisasi pada gradien tiap langkah optimasi, sehingga bobot ramah PTQ; (2) analisis sensitivitas menemukan enam lapisan paling terdampak untuk dibiarkan berhitung dalam *float*; (3) bila PTQ belum cukup, QAT dibangun di atas RepOptimizer ditambah distilasi per kanal (guru berupa model FP32-nya sendiri) dan optimasi graf komputasi.

## Eksperimen dan Hasil

Model dilatih pada COCO 2017 (sekitar 118 ribu citra, 80 kelas) dan dievaluasi pada 5.000 citra validasi. Metrik utamanya AP (*Average Precision* COCO: rata-rata presisi pada ambang IoU 0,50–0,95). Pelatihan memakai SGD bermomentum dengan peluruhan kosinus, *exponential moving average* (rata-rata bergerak bobot), dan augmentasi Mosaic-Mixup, selama 300 epoch tanpa pra-pelatihan pada 8 GPU A100. Kecepatan diukur pada satu Tesla T4 dengan TensorRT presisi FP16, sebagai latensi (*batch* 1) dan *throughput* (*batch* 32).

| Model | AP | AP50 | FPS (*batch* 1) | FPS (*batch* 32) | Latensi | Parameter | FLOPs |
|---|---|---|---|---|---|---|---|
| YOLOv6-N | 35,9% | 51,2% | 802 | 1234 | 1,2 ms | 4,3 M | 11,1 G |
| YOLOv6-T | 40,3% | 56,6% | 449 | 659 | 2,2 ms | 15,0 M | 36,7 G |
| YOLOv6-S | 43,5% | 60,4% | 358 | 495 | 2,8 ms | 17,2 M | 44,2 G |
| YOLOv6-M | 49,5% | 66,8% | 179 | 233 | 5,6 ms | 34,3 M | 82,2 G |
| YOLOv6-L | 52,5% | 70,0% | 98 | 121 | 10,2 ms | 58,5 M | 144,0 G |

YOLOv6-N melampaui YOLOv5-N (28,0% AP) sebesar 7,9 poin dan YOLOv7-Tiny masukan 416 (33,3% AP) sebesar 2,6 poin, sekaligus menjadi yang tercepat. YOLOv6-S lebih akurat 3,0 poin dari YOLOX-S (40,5% AP) dan 0,4 poin dari PP-YOLOE-S (43,1% AP) dengan kecepatan lebih tinggi. YOLOv6-M melampaui YOLOv5-M (45,4% AP) sebesar 4,2 poin pada kecepatan sebanding, dan varian YOLOv6-L-ReLU (51,7% AP, 8,8 ms) melampaui YOLOX-L, PP-YOLOE-L, dan YOLOv7 pada akurasi dan kecepatan sekaligus.

Ablasi membuktikan sumbangan tiap komponen. Dari baseline YOLOv5-N (28,0% AP), penambahan head terpisah memberi 29,4%; pelepasan *anchor* memberi 30,7% sekaligus mempercepat 51% karena dimensi keluaran tiga kali lebih kecil; EfficientRep dan Rep-PAN memberi 34,3% dengan 21% lebih cepat; dan head *hybrid-channel* menutup pada 34,5% AP dengan 1242 FPS. Untuk penetapan label, TAL mencapai 35,0% AP pada YOLOv6-N, di atas SimOTA (34,5%) dan ATSS (32,5%). Distilasi diri menaikkan YOLOv6-L dari 51,0% menjadi 52,3% AP, dan perpanjangan ke 400 epoch menambah 0,4–0,6 poin pada model kecil.

Hasil kuantisasi menunjukkan mengapa penanganan khusus diperlukan: PTQ polos pada YOLOv6-S menjatuhkan AP dari 42,4% menjadi 35,0%, sedangkan dengan RepOptimizer menjadi 40,9%. Jalur QAT penuh mencapai 43,3% AP pada 869 FPS — hanya 0,1 poin di bawah model FP16 (43,4%) tetapi 60% lebih cepat (541 FPS).

## Kelebihan dan Keterbatasan

Kelebihan YOLOv6 adalah orientasi penerapannya yang konsisten: pengukuran pada GPU kelas produksi, rancangan berbeda per skala, jalur kuantisasi yang menjaga akurasi, dan pemilihan komponen melalui ablasi terdokumentasi.

Keterbatasannya: secara konseptual, kontribusinya adalah integrasi rekayasa atas teknik yang sudah ada, bukan paradigma baru. Dari sisi rekayasa, angka kecepatan terikat pada TensorRT dan Tesla T4; model terkuantisasi diuji dengan TensorRT 8 sedangkan model lain dengan TensorRT 7 — diakui penulis sendiri — sehingga perbandingan lintas makalah perlu kehati-hatian. Distilasi regresi bergantung DFL yang hanya dipakai M dan L, sehingga model kecil tidak memperoleh manfaat penuhnya; model besar justru kembali ke konvolusi biasa dengan SiLU, sehingga manfaat reparameterisasi tidak seragam antar-skala.

## Kaitan dengan Bab Lain

Formulasi deteksi satu tahap diwarisi dari [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md). Dekomposisi backbone–neck–head, pola CSP, topologi PAN, dan augmentasi Mosaic diambil dari [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md). Paradigma *anchor-free*, head terpisah, dan SimOTA diwarisi dari [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md), meskipun SimOTA kemudian digantikan TAL. YOLOv6 sezaman dengan [bab 007 (YOLOv7)](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md): keduanya memakai reparameterisasi struktural, tetapi YOLOv6 membedakan diri lewat rancangan per skala model dan penanganan kuantisasi yang eksplisit. Garis penyempurnaan ini dilanjutkan [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `li2022yolov6`. Ringkasan yang aman dikutip: "YOLOv6 (Li dkk., 2022) adalah detektor objek satu tahap berorientasi industri dari Meituan dengan backbone reparameterisasi EfficientRep, neck Rep-PAN, head anchor-free efisien, serta pelatihan berbasis TAL, Varifocal Loss, dan distilasi diri. YOLOv6-S mencapai 43,5% AP pada 495 FPS di Tesla T4; versi INT8-nya mencapai 43,3% AP pada 869 FPS."

Catatan verifikasi sebelum sitasi formal: (1) AP YOLOv6-L dilaporkan 52,3% pada abstrak tetapi 52,5% pada Tabel 1 naskah; (2) angka FPS bergantung versi TensorRT dan ukuran *batch* (model terkuantisasi diuji dengan TensorRT 8, model lain TensorRT 7); (3) makalah memuat dua rilis (v1.0, v2.0) dengan hasil kuantisasi berbeda; (4) venue berupa laporan teknis arXiv tanpa penelaahan sejawat.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
55 YOLOv6-M

50 QuantizedYOLOv6-S COCO AP (%)

Abstract For years, YOLO series have been de facto industry-level standard for efficient object detection. The YOLO community has prospered overwhelmingly to enrich its use in a multitude of hardware platforms and abundant scenarios. In this technical report, we strive to push its limits to the next level, stepping forward with an unwavering mindset for industry application. Considering the diverse requirements for speed and accuracy in the real environment, we extensively examine the up-to-date object detection advancements either from industry or academy. Specifically, we heavily assimilate ideas from recent network design, training strategies, testing techniques, quantization and optimization methods. On top of this, we integrate our thoughts and practice to build a suite of deployment* Equal contributions. † Corresponding author.

1. Introduction

• We refashion a line of networks of different sizes tailored for industrial applications in diverse scenarios. The architectures at different scales vary to achieve the best speed and accuracy trade-off, where small models feature a plain single-path backbone and large models are built on efficient multi-branch blocks.

YOLO series have been the most popular detection frameworks in industrial applications, for its excellent balance between speed and accuracy. Pioneering works of YOLO series are YOLOv1-3 [32–34], which blaze a new trail of one-stage detectors along with the later substantial improvements. YOLOv4 [1] reorganized the detection framework into several separate parts (backbone, neck and head), and verified bag-of-freebies and bag-of-specials at the time to design a framework suitable for training on a single GPU. At present, YOLOv5 [10], YOLOX [7], PPYOLOE [44] and YOLOv7 [42] are all the competing candidates for efficient detectors to deploy. Models at different sizes are commonly obtained through scaling techniques.

• We imbue YOLOv6 with a self-distillation strategy, performed both on the classification task and the regression task. Meanwhile, we dynamically adjust the knowledge from the teacher and labels to help the student model learn knowledge more efficiently during all training phases. • We broadly verify the advanced detection techniques for label assignment, loss function and data augmentation techniques and adopt them selectively to further boost the performance.

In this report, we empirically observed several important factors that motivate us to refurnish the YOLO framework: (1) Reparameterization from RepVGG [3] is a superior technique that is not yet well exploited in detection. We also notice that simple model scaling for RepVGG blocks becomes impractical, for which we consider that the elegant consistency of the network design between small and large networks is unnecessary. The plain single-path architecture is a better choice for small networks, but for larger models, the exponential growth of the parameters and the computation cost of the single-path architecture makes it infeasible; (2) Quantization of reparameterization-based detectors also requires meticulous treatment, otherwise it would be intractable to deal with performance degradation due to its heterogeneous configuration during training and inference. (3) Previous works [7, 10, 42, 44] tend to pay less attention to deployment, whose latencies are commonly compared on high-cost machines like V100. There is a hardware gap when it comes to real serving environment. Typically, lowpower GPUs like Tesla T4 are less costly and provide rather good inference performance. (4) Advanced domain-specific strategies like label assignment and loss function design need further verifications considering the architectural variance; (5) For deployment, we can tolerate the adjustments of the training strategy that improve the accuracy performance but not increase inference costs, such as knowledge distillation.

2. Method The renovated design of YOLOv6 consists of the following components, network design, label assignment, loss function, data augmentation, industry-handy improvements, and quantization and deployment: • Network Design: Backbone: Compared with other mainstream architectures, we find that RepVGG [3] backbones are equipped with more feature representation power in small networks at a similar inference speed, whereas it can hardly be scaled to obtain larger models due to the explosive growth of the parameters and computational costs. In this regard, we take RepBlock [3] as the building block of our small networks. For large models, we revise a more efficient CSP [43] block, named CSPStackRep Block. Neck: The neck of YOLOv6 adopts PAN topology [24] following YOLOv4 and YOLOv5. We enhance the neck with RepBlocks or CSPStackRep Blocks to have RepPAN. Head: We simplify the decoupled head to make it more efficient, called Efficient Decoupled Head.

With the aforementioned observations in mind, we bring the birth of YOLOv6, which accomplishes so far the best trade-off in terms of accuracy and speed. We show the comparison of YOLOv6 with other peers at a similar scale in Fig. 1. To boost inference speed without much performance degradation, we examined the cutting-edge quantization methods, including post-training quantization (PTQ) and quantization-aware training (QAT), and accommodate them in YOLOv6 to achieve the goal of deployment-ready networks.

• Label Assignment: We evaluate the recent progress of label assignment strategies [5, 7, 18, 48, 51] on YOLOv6 through numerous experiments, and the results indicate that TAL [5] is more effective and training-friendly. • Loss Function: The loss functions of the mainstream anchor-free object detectors contain classification loss,

Figure 2: The YOLOv6 framework (N and S are shown). Note for M/L, RepBlocks is replaced with CSPStackRep. box regression loss and object loss. For each loss, we systematically experiment it with all available techniques and finally select VariFocal Loss [50] as our classification loss and SIoU [8]/GIoU [35] Loss as our regression loss.

consists of several convolutional layers, and it predicts final detection results according to multi-level features assembled by the neck. It can be categorized as anchorbased and anchor-free, or rather parameter-coupled head and parameter-decoupled head from the structure’s perspective. In YOLOv6, based on the principle of hardwarefriendly network design [3], we propose two scaled reparameterizable backbones and necks to accommodate models at different sizes, as well as an efficient decoupled head with the hybrid-channel strategy. The overall architecture of YOLOv6 is shown in Fig. 2.

• Industry-handy improvements: We introduce additional common practice and tricks to improve the performance including self-distillation and more training epochs. For self-distillation, both classification and box regression are respectively supervised by the teacher model. The distillation of box regression is made possible thanks to DFL [20]. In addition, the proportion of information from the soft and hard labels is dynamically declined via cosine decay, which helps the student selectively acquire knowledge at different phases during the training process. In addition, we encounter the problem of the impaired performance without adding extra gray borders at evaluation, for which we provide some remedies.

As mentioned above, the design of the backbone network has a great impact on the effectiveness and efficiency of the detection model. Previously, it has been shown that multibranch networks [13, 14, 38, 39] can often achieve better classification performance than single-path ones [15, 37], but often it comes with the reduction of the parallelism and results in an increase of inference latency. On the contrary, plain single-path networks like VGG [37] take the advantages of high parallelism and less memory footprint, leading to higher inference efficiency. Lately in RepVGG [3], a structural re-parameterization method is proposed to decouple the training-time multi-branch topology with an inference-time plain architecture to achieve a better speedaccuracy trade-off. Inspired by the above works, we design an efficient re-parameterizable backbone denoted as EfficientRep. For small models, the main component of the backbone is RepBlock during the training phase, as shown in Fig. 3 (a). And each RepBlock is converted to stacks of 3 × 3 convolutional layers (denoted as RepConv) with ReLU activation functions during the inference phase, as shown in Fig. 3 (b). Typically a 3×3 convolution is highly optimized on mainstream GPUs and CPUs and it enjoys higher computational density. Consequently, EfficientRep Backbone sufficiently

• Quantization and deployment: To cure the performance degradation in quantizing reparameterizationbased models, we train YOLOv6 with RepOptimizer [2] to obtain PTQ-friendly weights. We further adopt QAT with channel-wise distillation [36] and graph optimization to pursue extreme performance. Our quantized YOLOv6-S hits a new state of the art with 42.3% AP and a throughput of 869 FPS (batch size=32).

2.1. Network Design A one-stage object detector is generally composed of the following parts: a backbone, a neck and a head. The backbone mainly determines the feature representation ability, meanwhile, its design has a critical influence on the inference efficiency since it carries a large portion of computation cost. The neck is used to aggregate the low-level physical features with high-level semantic features, and then build up pyramid feature maps at all levels. The head 3

utilizes the computing power of the hardware, resulting in a significant decrease in inference latency while enhancing the representation ability in the meantime. However, we notice that with the model capacity further expanded, the computation cost and the number of parameters in the single-path plain network grow exponentially. To achieve a better trade-off between the computation burden and accuracy, we revise a CSPStackRep Block to build the backbone of medium and large networks. As shown in Fig. 3 (c), CSPStackRep Block is composed of three 1×1 convolution layers and a stack of sub-blocks consisting of two RepVGG blocks [3] or RepConv (at training or inference respectively) with a residual connection. Besides, a cross stage partial (CSP) connection is adopted to boost performance without excessive computation cost. Compared with CSPRepResStage [45], it comes with a more succinct outlook and considers the balance between accuracy and speed. + : Element-wise add

counterparts in FCOS [41] and YOLOX [7] decouple the two branches, and additional two 3×3 convolutional layers are introduced in each branch to boost the performance. In YOLOv6, we adopt a hybrid-channel strategy to build a more efficient decoupled head. Specifically, we reduce the number of the middle 3×3 convolutional layers to only one. The width of the head is jointly scaled by the width multiplier for the backbone and the neck. These modifications further reduce computation costs to achieve a lower inference latency. Anchor-free Anchor-free detectors stand out because of their better generalization ability and simplicity in decoding prediction results. The time cost of its post-processing is substantially reduced. There are two types of anchorfree detectors: anchor point-based [7, 41] and keypointbased [16, 46, 53]. In YOLOv6, we adopt the anchor pointbased paradigm, whose box regression branch actually predicts the distance from the anchor point to the four sides of the bounding boxes.

2.2. Label Assignment 𝟏×𝟏 Conv

Label assignment is responsible for assigning labels to predefined anchors during the training stage. Previous work has proposed various label assignment strategies ranging from simple IoU-based strategy and inside ground-truth method [41] to other more complex schemes [5, 7, 18, 48, 51].

Figure 3: (a) RepBlock is composed of a stack of RepVGG blocks with ReLU activations at training. (b) During inference time, RepVGG block is converted to RepConv. (c) CSPStackRep Block comprises three 1×1 convolutional layers and a stack of sub-blocks of double RepConvs following the ReLU activations with a residual connection.

SimOTA OTA [6] considers the label assignment in object detection as an optimal transmission problem. It defines positive/negative training samples for each ground-truth object from a global perspective. SimOTA [7] is a simplified version of OTA [6], which reduces additional hyperparameters and maintains the performance. SimOTA was utilized as the label assignment method in the early version of YOLOv6. However, in practice, we find that introducing SimOTA will slow down the training process. And it is not rare to fall into unstable training. Therefore, we desire a replacement for SimOTA.

In practice, the feature integration at multiple scales has been proved to be a critical and effective part of object detection [9, 21, 24, 40]. We adopt the modified PAN topology [24] from YOLOv4 [1] and YOLOv5 [10] as the base of our detection neck. In addition, we replace the CSPBlock used in YOLOv5 with RepBlock (for small models) or CSPStackRep Block (for large models) and adjust the width and depth accordingly. The neck of YOLOv6 is denoted as Rep-PAN. 2.1.3

Task alignment learning Task Alignment Learning (TAL) was first proposed in TOOD [5], in which a unified metric of classification score and predicted box quality is designed. The IoU is replaced by this metric to assign object labels. To a certain extent, the problem of the misalignment of tasks (classification and box regression) is alleviated. The other main contribution of TOOD is about the taskaligned head (T-head). T-head stacks convolutional layers to build interactive features, on top of which the Task-Aligned Predictor (TAP) is used. PP-YOLOE [45] improved Thead by replacing the layer attention in T-head with the

lightweight ESE attention, forming ET-head. However, we find that the ET-head will deteriorate the inference speed in our models and it comes with no accuracy gain. Therefore, we retain the design of our Efficient decoupled head. Furthermore, we observed that TAL could bring more performance improvement than SimOTA and stabilize the training. Therefore, we adopt TAL as our default label assignment strategy in YOLOv6.

to be effective because of its consistency with the evaluation metric. There are many variants of IoU, such as GIoU [35], DIoU [52], CIoU [52], α-IoU [11] and SIoU [8], etc, forming relevant loss functions. We experiment with GIoU, CIoU and SIoU in this work. And SIoU is applied to YOLOv6-N and YOLOv6-T, while others use GIoU. Probability Loss Distribution Focal Loss (DFL) [20] simplifies the underlying continuous distribution of box locations as a discretized probability distribution. It considers ambiguity and uncertainty in data without introducing any other strong priors, which is helpful to improve the box localization accuracy especially when the boundaries of the ground-truth boxes are blurred. Upon DFL, DFLv2 [19] develops a lightweight sub-network to leverage the close correlation between distribution statistics and the real localization quality, which further boosts the detection performance. However, DFL usually outputs 17× more regression values than general box regression, leading to a substantial overhead. The extra computation cost significantly hinders the training of small models. Whilst DFLv2 further increases the computation burden because of the extra sub-network. In our experiments, DFLv2 brings similar performance gain to DFL on our models. Consequently, we only adopt DFL in YOLOv6-M/L. Experimental details can be found in Section 3.3.3.

2.3. Loss Functions Object detection contains two sub-tasks: classification and localization, corresponding to two loss functions: classification loss and box regression loss. For each sub-task, there are various loss functions presented in recent years. In this section, we will introduce these loss functions and describe how we select the best ones for YOLOv6. 2.3.1

Improving the performance of the classifier is a crucial part of optimizing detectors. Focal Loss [22] modified the traditional cross-entropy loss to solve the problems of class imbalance either between positive and negative examples, or hard and easy samples. To tackle the inconsistent usage of the quality estimation and classification between training and inference, Quality Focal Loss (QFL) [20] further extended Focal Loss with a joint representation of the classification score and the localization quality for the supervision in classification. Whereas VariFocal Loss (VFL) [50] is rooted from Focal Loss [22], but it treats the positive and negative samples asymmetrically. By considering positive and negative samples at different degrees of importance, it balances learning signals from both samples. Poly Loss [17] decomposes the commonly used classification loss into a series of weighted polynomial bases. It tunes polynomial coefficients on different tasks and datasets, which is proved better than Cross-entropy Loss and Focal Loss through experiments. We assess all these advanced classification losses on YOLOv6 to finally adopt VFL [50]. 2.3.2

Object loss was first proposed in FCOS [41] to reduce the score of low-quality bounding boxes so that they can be filtered out in post-processing. It was also used in YOLOX [7] to accelerate convergence and improve network accuracy. As an anchor-free framework like FCOS and YOLOX, we have tried object loss into YOLOv6. Unfortunately, it doesn’t bring many positive effects. Details are given in Section 3.

2.4. Industry-handy improvements The following tricks come ready to use in real practice. They are not intended for a fair comparison but steadily produce performance gain without much tedious effort.

Box regression loss provides significant learning signals localizing bounding boxes precisely. L1 loss is the original box regression loss in early works. Progressively, a variety of well-designed box regression losses have sprung up, such as IoU-series loss [8, 11, 35, 47, 52, 52] and probability loss [20].

Empirical results have shown that detectors have a progressing performance with more training time. We extended the training duration from 300 epochs to 400 epochs to reach a better convergence. 2.4.2

IoU-series Loss IoU loss [47] regresses the four bounds of a predicted box as a whole unit. It has been proved

2.5. Quantization and Deployment

sical knowledge distillation technique minimizing the KLdivergence between the prediction of the teacher and the student. We limit the teacher to be the student itself but pretrained, hence we call it self-distillation. Note that the KL-divergence is generally utilized to measure the difference between data distributions. However, there are two sub-tasks in object detection, in which only the classification task can directly utilize knowledge distillation based on KL-divergence. Thanks to DFL loss [20], we can perform it on box regression as well. The knowledge distillation loss can then be formulated as: reg cls reg LKD = KL(pcls t ||ps ) + KL(pt ||ps ),

For industrial deployment, it has been common practice to adopt quantization to further speed up runtime without much performance compromise. Post-training quantization (PTQ) directly quantizes the model with only a small calibration set. Whereas quantization-aware training (QAT) further improves the performance with the access to the training set, which is typically used jointly with distillation. However, due to the heavy use of re-parameterization blocks in YOLOv6, previous PTQ techniques fail to produce high performance, while it is hard to incorporate QAT when it comes to matching fake quantizers during training and inference. We here demonstrate the pitfalls and our cures during deployment.

cls where pcls t and ps are class prediction of the teacher model and the student model respectively, and accordingly preg t and preg are box regression predictions. The overall loss s function is now formulated as:

RepOptimizer [2] proposes gradient re-parameterization at each optimization step. This technique also well solves the quantization problem of reparameterization-based models. We hence reconstruct the re-parameterization blocks of YOLOv6 in this fashion and train it with RepOptimizer to obtain PTQ-friendly weights. The distribution of feature map is largely narrowed (e.g. Fig. 4, more in B.1), which greatly benefits the quantization process, see Sec 3.5.1 for results.

where Ldet is the detection loss computed with predictions and labels. The hyperparameter α is introduced to balance two losses. In the early stage of training, the soft labels from the teacher are easier to learn. As the training continues, the performance of the student will match the teacher so that the hard labels will help students more. Upon this, we apply cosine weight decay to α to dynamically adjust the information from hard labels and soft ones from the teacher. We conducted detailed experiments to verify the effect of self-distillation on YOLOv6, which will be discussed in Section 3. 2.4.3

We notice that a half-stride gray border is put around each image when evaluating the model performance in the implementations of YOLOv5 [10] and YOLOv7 [42]. Although no useful information is added, it helps in detecting the objects near the edge of the image. This trick also applies in YOLOv6. However, the extra gray pixels evidently reduce the inference speed. Without the gray border, the performance of YOLOv6 deteriorates, which is also the case in [10, 42]. We postulate that the problem is related to the gray borders padding in Mosaic augmentation [1, 10]. Experiments on turning mosaic augmentations off during last epochs [7] (aka. fade strategy) are conducted for verification. In this regard, we change the area of gray border and resize the image with gray borders directly to the target image size. Combining these two strategies, our models can maintain or even boost the performance without the degradation of inference speed.

Figure 4: Improved activation distribution of YOLOv6-S trained with RepOptimizer.

We further improve the PTQ performance by partially converting quantization-sensitive operations into float computation. To obtain the sensitivity distribution, several metrics are commonly used, mean-square error (MSE), signal-noise ratio (SNR) and cosine similarity. Typically for comparison, one can pick the output feature map (after the activation of a certain layer) to calculate these metrics with and without quantization. As an alternative, it is also viable to 6

compute validation AP by switching quantization on and off for the certain layer [29]. We compute all these metrics on the YOLOv6-S model trained with RepOptimizer and pick the top-6 sensitive layers to run in float. The full chart of sensitivity analysis can be found in B.2. 2.5.3

In case PTQ is insufficient, we propose to involve quantization-aware training (QAT) to boost quantization performance. To resolve the problem of the inconsistency of fake quantizers during training and inference, it is necessary to build QAT upon the RepOptimizer. Besides, channelwise distillation [36] (later as CW Distill) is adapted within the YOLOv6 framework, shown in Fig. 5. This is also a self-distillation approach where the teacher network is the student itself in FP32-precision. See experiments in Sec 3.5.1. Teacher (Float32)

3. Experiments

3.3. Ablation Study

3.1. Implementation Details

We use the same optimizer and the learning schedule as YOLOv5 [10], i.e. stochastic gradient descent (SGD) with momentum and cosine decay on learning rate. Warm-up, grouped weight decay strategy and the exponential moving average (EMA) are also utilized. We adopt two strong data augmentations (Mosaic [1,10] and Mixup [49]) following [1,7,10]. A complete list of hyperparameter settings can be found in our released code. We train our models on the COCO 2017 [23] training set, and the accuracy is evaluated on the COCO 2017 validation set. All our models are trained on 8 NVIDIA A100 GPUs, and the speed performance is measured on an NVIDIA Tesla T4 GPU with TensorRT version 7.2 unless otherwise stated. And the speed

Backbone and neck We explore the influence of singlepath structure and multi-branch structure on backbones and necks, as well as the channel coefficient (denoted as CC) of CSPStackRep Block. All models described in this part adopt TAL as the label assignment strategy, VFL as the classification loss, and GIoU with DFL as the regression loss. Results are shown in Table 2. We find that the optimal network structure for models at different sizes should come up with different solutions. For YOLOv6-N, the single-path structure outperforms the multi-branch structure in terms of both accuracy and speed. Although the single-path structure has more FLOPs and parameters than the multi-branch structure, it could 7

Network

Method

Table 1: Comparisons with other YOLO-series detectors on COCO 2017 val. FPS and latency are measured in FP16-precision on a Tesla T4 in the same environment with TensorRT. All our models are trained for 300 epochs without pre-training or any external data. Both the accuracy and the speed performance of our models are evaluated with the input resolution of 640×640. ‘‡’ represents that the proposed self-distillation method is utilized. ‘∗’ represents the re-evaluated result of the released model through the official code. run faster due to a relatively lower memory footprint and a higher degree of parallelism. For YOLOv6-S, the two block styles bring similar performance. When it comes to larger models, multi-branch structure achieves better performance in accuracy and speed. And we finally select multi-branch with a channel coefficient of 2/3 for YOLOv6-M and 1/2 for YOLOv6-L. Furthermore, we study the influence of width and depth of the neck on YOLOv6-L. Results in Table 3 show that the slender neck performs 0.2% better than the wide-shallow neck with the similar speed.

Table 2: Ablation study on backbones and necks. YOLOv6L here is equipped with ReLU.

Moreover, we further verify the effectiveness of combinations of RepConv/ordinary convolution (denoted as Conv) and ReLU/SiLU/LReLU in networks of different sizes to achieve a better trade-off. As shown in Table 4, Conv with SiLU performs the best in accuracy while the combination of RepConv and ReLU achieves a better trade-off. We suggest users adopt RepConv with ReLU in latency-sensitive applications. We choose to use RepConv/ReLU combi8

Method

Table 7: Comparisons of label assignment methods in warm-up stage.

nation in YOLOv6-N/T/S/M for higher inference speed and use the Conv/SiLU combination in the large model YOLOv6-L to speed up training and improve performance.

best two strategies. Compared with the ATSS, SimOTA can increase AP by 2.0%, and TAL brings 0.5% higher AP than SimOTA. Considering the stable training and better accuracy performance of TAL, we adopt TAL as our label assignment strategy. In addition, the implementation of TOOD [5] adopts ATSS [51] as the warm-up label assignment strategy during the early training epochs. We also retain the warm-up strategy and further make some explorations on it. Details are shown in Table 7, and we can find that without warm-up or warmed up by other strategies (i.e., SimOTA) it can also achieve the similar performance.

Miscellaneous design We also conduct a series of ablation on other network parts mentioned in Section 2.1 based on YOLOv6-N. We choose YOLOv5-N as the baseline and add other components incrementally. Results are shown in Table 5. Firstly, with decoupled head (denoted as DH), our model is 1.4% more accurate with 5% increase in time cost. Secondly, we verify that the anchor-free paradigm is 51% faster than the anchor-based one for its 3× less predefined anchors, which results in less dimensionality of the output. Further, the unified modification of the backbone (EfficientRep Backbone) and the neck (Rep-PAN neck), denoted as EB+RN, brings 3.6% AP improvements, and runs 21% faster. Finally, the optimized decoupled head (hybrid channels, HC) brings 0.2% AP and 6.8% FPS improvements in accuracy and speed respectively. 3.3.2

Table 5: Ablation study on all network designs in an incremental way. FPS is tested with FP16-precision and batchsize=32 on Tesla T4 GPUs.

Table 3: Ablation study on the neck settings of YOLOv6-L. SiLU is selected as the activation function. Model

In Table 6, we analyze the effectiveness of mainstream label assign strategies. Experiments are conducted on YOLOv6N. As expected, we observe that SimOTA and TAL are the

where Lcls , Lreg and Lobj are classification loss, regression loss and object loss. λ and µ are hyperparameters. 9

Table 9: Ablation study on IoU-series box regression loss functions. The classification loss is VFL [50].

Table 8: Ablation study on classification loss functions. Method

In this subsection, we evaluate each loss function on YOLOv6. Unless otherwise specified, the baselines for YOLOv6-N, YOLOv6-S and YOLOv6-M are 35.0%, 42.9% and 48.0% trained with TAL, Focal Loss and GIoU Loss. Classification Loss We experiment Focal Loss [22], Poly loss [17], QFL [20] and VFL [50] on YOLOv6-N/S/M. As can be seen in Table 8, VFL brings 0.2%/0.3%/0.1% AP improvements on YOLOv6-N/S/M respectively compared with Focal Loss. We choose VFL as the classification loss function.

Table 10: Ablation study on probability loss functions. Object Loss

Method

Regression Loss IoU-series and probability loss functions are both experimented with on YOLOv6-N/S/M. The latest IoU-series losses are utilized in YOLOv6N/S/M. Experiment results in Table 9 show that SIoU Loss outperforms others for YOLOv6-N and YOLOv6-T, while CIoU Loss performs better on YOLOv6-M. For probability losses, as listed in Table 10, introducing DFL can obtain 0.2%/0.1%/0.2% performance gain for YOLOv6-N/S/M respectively. However, the inference speed is greatly affected for small models. Therefore, DFL is only introduced in YOLOv6-M/L.

Table 11: Effectiveness of object loss. obviously increases the difficulty. Based on the experimental results and this analysis, the object loss is then discarded in YOLOv6.

Object Loss Object loss is also experimented with YOLOv6, as shown in Table 11. From Table 11, we can see that object loss has negative effects on YOLOv6-N/S/M networks, where the maximum decrease is 1.1% AP on YOLOv6-N. The negative gain may come from the conflict between the object branch and the other two branches in TAL. Specifically, in the training stage, IoU between predicted boxes and ground-truth ones, as well as classification scores are used to jointly build a metric as the criteria to assign labels. However, the introduced object branch extends the number of tasks to be aligned from two to three, which

3.4. Industry-handy improvements More training epochs In practice, more training epochs is a simple and effective way to further increase the accuracy. Results of our small models trained for 300 and 400 epochs are shown in Table 12. We observe that training for longer epochs substantially boosts AP by 0.4%, 0.6%, 0.5% for YOLOv6-N, T, S respectively. Considering the acceptable cost and the produced gain, it suggests that training for 10

Table 12: Experiments of more training epochs on small models.

Table 13: Ablation study on the self-distillation. Table 14: Experimental results about the strategies for solving the problem of the performance degradation without extra gray border. Self-distillation We conducted detailed experiments to verify the proposed self-distillation method on YOLOv6L. As can be seen in Table 13, applying the self-distillation only on the classification branch can bring 0.4% AP improvement. Furthermore, we simply perform the selfdistillation on the box regression task to have 0.3% AP increase. The introduction of weight decay boosts the model by 0.6% AP.

3.5. Quantization Results We take YOLOv6-S as an example to validate our quantization method. The following experiment is on both two releases. The baseline model is trained for 300 epochs. 3.5.1

The average performance is substantially improved when the model is trained with RepOptimizer, see Table 15. RepOptimizer is in general faster and nearly identical.

Gray border of images In Section 2.4.3, we introduce a strategy to solve the problem of performance degradation without extra gray borders. Experimental results are shown in Table 14. In these experiments, YOLOv6-N and YOLOv6-S are trained for 400 epochs and YOLOv6-M for 300 epochs. It can be observed that the accuracy of YOLOv6-N/S/M is lowered by 0.4%/0.5%/0.7% without Mosaic fading when removing the gray border. However, the performance degradation becomes 0.2%/0.5%/0.5% when adopting Mosaic fading, from which we find that, on the one hand, the problem of performance degradation is mitigated. On the other hand, the accuracy of small models (YOLOv6-N/S) is improved whether we pad gray borders or not. Moreover, we limit the input images to 634×634 and add gray borders by 3 pixels wide around the edges (more results can be found in Appendix C). With this strategy, the size of the final images is the expected 640×640. The results in Table 14 indicate that the final performance of YOLOv6-N/S/M is even 0.2%/0.3%/0.1% more accurate with the final image size reduced from 672 to 640.

full QAT in Table 16. Partial QAT leads to better accuracy with a slightly reduced throughput. Model

[2] Xiaohan Ding, Honghao Chen, Xiangyu Zhang, Kaiqi Huang, Jungong Han, and Guiguang Ding. Reparameterizing your optimizers rather than architectures. arXiv preprint arXiv:2205.15242, 2022. 2, 3, 6 [3] Xiaohan Ding, Xiangyu Zhang, Ningning Ma, Jungong Han, Guiguang Ding, and Jian Sun. Repvgg: Making vgg-style convnets great again. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 13733–13742, 2021. 2, 3, 4 [4] Stefan Elfwing, Eiji Uchibe, and Kenji Doya. Sigmoidweighted linear units for neural network function approximation in reinforcement learning. Neural Networks, 107:3–11, 2018. 8 [5] Chengjian Feng, Yujie Zhong, Yu Gao, Matthew R Scott, and Weilin Huang. Tood: Task-aligned one-stage object detection. In ICCV, 2021. 2, 4, 9 [6] Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, and Jian Sun. Ota: Optimal transport assignment for object detection. 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 303–312, 2021. 4 [7] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian Sun. Yolox: Exceeding yolo series in 2021. arXiv preprint arXiv:2107.08430, 2021. 2, 4, 5, 6, 7, 8, 9, 15 [8] Zhora Gevorgyan. Siou loss: More powerful learning for bounding box regression. arXiv preprint arXiv:2205.12740, 2022. 3, 5, 10 [9] Golnaz Ghiasi, Tsung-Yi Lin, and Quoc V Le. Nas-fpn: Learning scalable feature pyramid architecture for object detection. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 7036–7045, 2019. 4 [10] Jocher Glenn. YOLOv5 release v6.1. https://github. com/ultralytics/yolov5/releases/tag/v6. 1, 2022. 2, 4, 6, 7, 8, 15 [11] Jiabo He, Sarah Erfani, Xingjun Ma, James Bailey, Ying Chi, and Xian-Sheng Hua. α-iou: A family of power intersection over union losses for bounding box regression. Advances in Neural Information Processing Systems, 34:20230–20242, 2021. 5 [12] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 770–778, 2016. [13] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Identity mappings in deep residual networks. In European conference on computer vision, pages 630–645. Springer, 2016. 3 [14] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q Weinberger. Densely connected convolutional networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 4700–4708, 2017. 3 [15] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems, 25, 2012. 3 [16] Hei Law and Jia Deng. Cornernet: Detecting objects as paired keypoints. In Proceedings of the European conference on computer vision (ECCV), pages 734–750, 2018. 4

Table 16: QAT performance of YOLOv6-S (v1.0) under different settings. Due to the removal of quantization-sensitive layers in v2.0 release, we directly use full QAT on YOLOv6-S trained with RepOptimizer. We eliminate inserted quantizers through graph optimization to obtain higher accuracy and faster speed. We compare the distillation-based quantization results from PaddleSlim [30] in Table 17. Note our quantized version of YOLOv6-S is the fastest and the most accurate, also see Fig. 1. Model

4. Conclusion In a nutshell, with the persistent industrial requirements in mind, we present the current form of YOLOv6, carefully examining all the advancements of components of object detectors up to date, meantime instilling our thoughts and practices. The result surpasses other available real-time detectors in both accuracy and speed. For the convenience of the industrial deployment, we also supply a customized quantization method for YOLOv6, rendering an ever-fast detector out-of-box. We sincerely thank the academic and industrial community for their brilliant ideas and endeavors. In the future, we will continue expanding this project to meet higher standards and more demanding scenarios.
