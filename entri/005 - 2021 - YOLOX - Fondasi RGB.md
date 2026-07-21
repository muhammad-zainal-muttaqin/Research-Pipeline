# 005 - YOLOX: Exceeding YOLO Series in 2021

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ge2021yolox` |
| Judul asli | YOLOX: Exceeding YOLO Series in 2021 |
| Penulis | Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, Jian Sun |
| Tahun | 2021 |
| Venue | arXiv preprint arXiv:2107.08430 (Megvii Technology) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2107.08430
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021&sort=relevance

## Gambaran Umum

YOLOX membongkar tiga asumsi desain yang diwarisi YOLO sejak bab 002: penggunaan *anchor box*, head yang menggabungkan klasifikasi dan regresi dalam satu cabang, dan penetapan label positif yang statis. Ketiganya diganti: prediksi menjadi *anchor-free* (setiap lokasi pada peta fitur langsung memprediksi satu objek), head dipisah menjadi cabang klasifikasi dan cabang regresi (*decoupled head*), dan penetapan label dilakukan secara dinamis oleh algoritme SimOTA yang memilih kandidat terbaik berdasarkan biaya prediksi.

Dampaknya konsisten di seluruh skala model. YOLOX menaikkan YOLOv3-Darknet53 menjadi 47,3% AP pada COCO (melampaui praktik terbaik saat itu sebesar 3,0 poin), YOLOX-L mencapai 50,0% AP pada 68,9 FPS (V100) melampaui YOLOv5-L sebesar 1,8 poin, dan YOLOX-Nano — hanya 0,91 juta parameter — mencapai 25,3% AP. Satu model YOLOX-L juga memenangi Streaming Perception Challenge pada Workshop on Autonomous Driving, CVPR 2021.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv2 (bab 002), keluarga YOLO memprediksi kotak sebagai koreksi terhadap *anchor* — kotak acuan yang bentuknya ditentukan lebih dahulu. Desain ini membawa tiga beban. Pertama, *anchor* adalah hiperparameter: jumlah, skala, dan rasionya harus disetel per dataset (mis. lewat klastering), dan setelan yang baik pada COCO belum tentu baik pada domain lain — inilah salah satu sumber bias domain. Kedua, penggunaan banyak *anchor* per lokasi memperbesar kepala prediksi. Ketiga, mekanisme penetapan label positif yang berbasis *anchor* bersifat statis: kandidat ditetapkan positif bila IOU-nya dengan objek kebenaran melampaui ambang tetap, tanpa memperhitungkan kualitas prediksi itu sendiri.

Di sisi lain, komunitas deteksi telah menunjukkan dua hal. FCOS (bab 019) membuktikan detektor *anchor-free* — satu prediksi per lokasi, langsung dari titik — dapat menyamai detektor berbasis *anchor*. Dan studi tentang *label assignment* menunjukkan bahwa memilih kandidat positif secara dinamis berdasarkan biaya (seperti OTA, *Optimal Transport Assignment*) menaikkan akurasi tanpa mengubah arsitektur. YOLOX adalah upaya membawa dua gagasan itu — ditambah pemisahan head — ke dalam keluarga YOLO yang telah terbukti praktis.

## Ide Utama

Gagasan pemersatu ketiga perubahan YOLOX adalah menyederhanakan apa yang dapat disederhanakan dan memindahkan kompleksitas ke tempat yang dapat dihitung otomatis. *Anchor* dihapus sehingga tidak ada lagi hiperparameter bentuk kotak yang harus disetel manusia. Head dipisah karena klasifikasi dan regresi adalah dua tugas berbeda yang selama ini dipaksa berbagi fitur yang sama. Dan penetapan label — keputusan "kandidat mana yang menjadi contoh positif untuk objek ini" — diserahkan kepada optimisasi biaya yang dihitung dari prediksi model itu sendiri, bukan aturan ambang tetap.

## Cara Kerja Langkah demi Langkah

### Anchor-Free

Pada YOLO berbasis *anchor*, setiap lokasi peta fitur mengeluarkan beberapa prediksi (satu per anchor). YOLOX mereduksi ini menjadi **satu prediksi per lokasi**: setiap titik pada peta fitur langsung memprediksi empat nilai — dua offset pusat relatif terhadap titik itu dan dua dimensi kotak — plus skor objek dan skor kelas. Titik-titik yang jatuh di dalam wilayah pusat objek (bukan hanya satu sel, tetapi area 3×3 di sekitar pusat, disebut *multi positives*) menjadi kandidat positif. Hasilnya: jumlah prediksi dan parameter head menyusut, dan seluruh hiperparameter *anchor* hilang.

### Decoupled Head

Pada YOLO klasik, satu cabang konvolusi menghasilkan keluaran klasifikasi dan regresi sekaligus. Kedua tugas ini memiliki kebutuhan fitur berbeda: klasifikasi membutuhkan fitur semantik "objek apa", regresi membutuhkan fitur geometris "di mana dan seberapa besar". YOLOX memisahkannya: satu konvolusi 1×1 mereduksi kanal, lalu dua cabang paralel (masing-masing dua konvolusi 3×3) menghasilkan keluaran klasifikasi dan regresi-objek secara terpisah. Efek yang dilaporkan: konvergensi pelatihan jauh lebih cepat dan akurasi akhir naik sekitar 1 poin AP — biaya komputasi tambahannya kecil.

```
peta fitur dari backbone+neck
        │  konvolusi 1×1 (reduksi kanal)
        ├──────────────┬──────────────────┐
        ▼              ▼                  ▼
  cabang klasifikasi  cabang regresi     (skor objek)
  2× konvolusi 3×3    2× konvolusi 3×3
        │              │                  │
        ▼              ▼                  ▼
   skor kelas      x, y, w, h         objectness
   per lokasi      per lokasi         per lokasi

  setiap lokasi = SATU prediksi (anchor-free, tanpa anchor berlapis)
```

### SimOTA: Penetapan Label Dinamis

Ini komponen paling teknis. Saat melatih detektor, setiap objek kebenaran harus "dipasangkan" dengan kandidat prediksi yang akan diawasi — pasangan inilah *label assignment*. OTA memformulasikannya sebagai masalah *optimal transport*: memasangkan pemasok (kandidat prediksi) ke penerima (objek kebenaran dan latar) dengan biaya total minimum, di mana biaya sebuah pasangan dihitung dari kualitas prediksi (galat klasifikasi + galat regresi). Formulasi ini bagus tetapi mahal — menambah ±25% waktu pelatihan karena algoritme iteratifnya.

SimOTA adalah penyederhanaannya: alih-alih menyelesaikan transport optimal penuh, untuk setiap objek dipilih **top-k** kandidat berbiaya terendah — dan k-nya sendiri diperkirakan dinamis dari distribusi IOU kandidat terbaik objek itu. Objek yang memiliki banyak kandidat berkualitas mendapat banyak contoh positif; objek yang sulit mendapat sedikit tetapi yang terbaik. Menurut naskah, SimOTA mempertahankan seluruh keuntungan OTA tanpa biaya iterasinya.

### Pelatihan

Di atas tiga perubahan itu, YOLOX memakai resep pelatihan kuat: augmentasi Mosaic (dari bab 004) ditambah MixUp (mencampur dua citra dan labelnya secara proporsional), keduanya dimatikan pada 15 *epoch* terakhir agar model menutup pelatihan pada data bersih. Baseline-nya sendiri sudah kuat: YOLOv3-SPP dengan *weight averaging* (EMA), penjadwalan kosinus, dan IoU loss.

## Eksperimen dan Hasil

Pengujian utama pada COCO lintas skala model, dari Nano hingga X, dengan ablation atas tiap komponen. Hasil utama:

- YOLOX-DarkNet53: 47,3% AP — menaikkan backbone YOLOv3 melampaui praktik terbaik sebelumnya sebesar 3,0 poin.
- YOLOX-L: 50,0% AP pada 68,9 FPS (Tesla V100), melampaui YOLOv5-L sebesar 1,8 poin pada jumlah parameter setara.
- YOLOX-Nano: 25,3% AP dengan 0,91 juta parameter dan 1,08 GFLOPs (melampaui NanoDet 1,8 poin); YOLOX-Tiny 32,8% AP — membuka pemakaian pada perangkat tepi.
- Satu model YOLOX-L memenangi Streaming Perception Challenge (WAD, CVPR 2021).

Ablation menunjukkan kontribusi berjenjang: augmentasi kuat memberi lompatan terbesar dari baseline, disusul *decoupled head* (yang juga mempercepat konvergensi) dan SimOTA sebagai pendorong akhir tanpa biaya inferensi.

## Kelebihan dan Keterbatasan

Kelebihan: (1) akurasi naik konsisten pada semua skala model, dari perangkat tepi hingga server; (2) desain lebih sederhana — tanpa *anchor*, tanpa hiperparameter bentuk kotak; (3) SimOTA memberi gain tanpa menambah biaya inferensi; (4) dukungan *deployment* luas (ONNX, TensorRT, NCNN, OpenVINO).

Keterbatasan: (1) SimOTA menambah kompleksitas prosedur pelatihan dibanding penetapan statis; (2) resep augmentasi kuat menuntut penjadwalan cermat (harus dimatikan di akhir pelatihan); (3) opsi *end-to-end* tanpa NMS yang dieksplorasi makalah masih kalah dari varian ber-NMS; (4) dari sisi konseptual, perubahan-perubahan ini adalah adopsi terukur dari literatur (FCOS, OTA) — kekuatan makalah ada pada integrasinya, bukan pada kebaruan tiap komponen.

## Kaitan dengan Bab Lain

YOLOX menutup garis evolusi yang dimulai bab 001: formulasi grid-regresi dipertahankan, tetapi *anchor* yang diperkenalkan bab 002 justru dihapus — kembali ke prediksi langsung, kini dengan mesin yang jauh lebih matang. Gagasan *anchor-free*-nya mewarisi FCOS (bab 019), resep pelatihannya mewarisi Mosaic dari bab 004, dan backbone-nya adalah Darknet-53 dari bab 003. Ke depan, desain *anchor-free* + *decoupled head* + penetapan label dinamis menjadi cetak biru yang diikuti banyak YOLO generasi berikutnya dalam tinjauan ini (bab 006–009), dan menjadi titik berangkat alami bagi integrasi RGB-D modern.

## Poin untuk Sitasi

Kutip dengan kunci `ge2021yolox`. Ringkasan yang aman dikutip: "YOLOX mengonversi YOLO menjadi detektor *anchor-free* dengan *decoupled head* dan penetapan label dinamis SimOTA, mencapai 47,3% AP (backbone YOLOv3) hingga 50,0% AP pada 68,9 FPS (YOLOX-L) pada COCO." Seluruh angka pada bab ini berasal dari abstrak dan tabel naskah; rincian ablation per komponen sebaiknya dikutip langsung dari tabel naskah.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Figure 1: Speed-accuracy trade-off of accurate models (top) and Size-accuracy curve of lite models on mobile devices (bottom) for YOLOX and other state-of-the-art object detectors. researchers in practical scenes, and we also provide deploy versions with ONNX, TensorRT, NCNN, and Openvino supported. Source code is at https://github.com/ Megvii-BaseDetection/YOLOX.

1. Introduction With the development of object detection, YOLO series [23, 24, 25, 1, 7] always pursuit the optimal speed and accuracy trade-off for real-time applications. They extract the most advanced detection technologies available at the time (e.g., anchors [26] for YOLOv2 [24], Residual Net [9] for YOLOv3 [25]) and optimize the implementation for best practice. Currently, YOLOv5 [7] holds the best trade-off performance with 48.2% AP on COCO at 13.7 ms.1 Nevertheless, over the past two years, the major advances in object detection academia have focused on anchor-free detectors [29, 40, 14], advanced label assignment strategies [37, 36, 12, 41, 22, 4], and end-to-end (NMS-free) detectors [2, 32, 39]. These have not been integrated into YOLO families yet, as YOLOv4 and YOLOv5 1 we choose the YOLOv5-L model at 640 × 640 resolution and test the model with FP16-precision and batch=1 on a V100 to align the settings of YOLOv4 [1] and YOLOv4-CSP [30] for a fair comparison

2. YOLOX 2.1. YOLOX-DarkNet53 We choose YOLOv3 [25] with Darknet53 as our baseline. In the following part, we will walk through the whole system designs in YOLOX step by step. Implementation details Our training settings are mostly consistent from the baseline to our final model. We train the models for a total of 300 epochs with 5 epochs warmup on COCO train2017 [17]. We use stochastic gradient descent (SGD) for training. We use a learning rate of lr×BatchSize/64 (linear scaling [8]), with a initial lr = 0.01 and the cosine lr schedule. The weight decay is 0.0005 and the SGD momentum is 0.9. The batch size is 128 by default to typical 8-GPU devices. Other batch sizes include single GPU training also work well. The input size is evenly drawn from 448 to 832 with 32 strides. FPS and 2 https://github.com/ultralytics/yolov3 3 https://github.com/RangiLyu/nanodet

thus train all the following models from scratch. Anchor-free Both YOLOv4 [1] and YOLOv5 [7] follow the original anchor-based pipeline of YOLOv3 [25]. However, the anchor mechanism has many known problems. First, to achieve optimal detection performance, one needs to conduct clustering analysis to determine a set of optimal anchors before training. Those clustered anchors are domain-specific and less generalized. Second, anchor mechanism increases the complexity of detection heads, as well as the number of predictions for each image. On some edge AI systems, moving such large amount of predictions between devices (e.g., from NPU to CPU) may become a potential bottleneck in terms of the overall latency. Anchor-free detectors [29, 40, 14] have developed rapidly in the past two year. These works have shown that the performance of anchor-free detectors can be on par with anchor-based detectors. Anchor-free mechanism significantly reduces the number of design parameters which need heuristic tuning and many tricks involved (e.g., Anchor Clustering [24], Grid Sensitive [11].) for good performance, making the detector, especially its training and decoding phase, considerably simpler [29]. Switching YOLO to an anchor-free manner is quite simple. We reduce the predictions for each location from 3 to 1 and make them directly predict four values, i.e., two offsets in terms of the left-top corner of the grid, and the height and width of the predicted box. We assign the center lo-

Figure 3: Training curves for detectors with YOLOv3 head or decoupled head. We evaluate the AP on COCO val every 10 epochs. It is obvious that the decoupled head converges much faster than the YOLOv3 head and achieves better result finally.

Strong data augmentation We add Mosaic and MixUp into our augmentation strategies to boost YOLOX’s performance. Mosaic is an efficient augmentation strategy proposed by ultralytics-YOLOv32 . It is then widely used in YOLOv4 [1], YOLOv5 [7] and other detectors [3]. MixUp [10] is originally designed for image classification task but then modified in BoF [38] for object detection training. We adopt the MixUp and Mosaic implementation in our model and close it for the last 15 epochs, achieving 42.0% AP in Tab. 2. After using strong data augmentation, we found ImageNet pre-training is no more beneficial, we 3

Methods

Table 2: Roadmap of YOLOX-Darknet53 in terms of AP (%) on COCO val. All the models are tested at 640×640 resolution, with FP16-precision and batch=1 on a Tesla V100. The latency and FPS in this table are measured without post-processing. cation of each object as the positive sample and pre-define a scale range, as done in [29], to designate the FPN level for each object. Such modification reduces the parameters and GFLOPs of the detector and makes it faster, but obtains better performance – 42.9% AP as shown in Tab. 2.

We briefly introduce SimOTA here. SimOTA first calculates pair-wise matching degree, represented by cost [4, 5, 12, 2] or quality [33] for each prediction-gt pair. For example, in SimOTA, the cost between gt gi and prediction pj is calculated as:

Multi positives To be consistent with the assigning rule of YOLOv3, the above anchor-free version selects only ONE positive sample (the center location) for each object meanwhile ignores other high quality predictions. However, optimizing those high quality predictions may also bring beneficial gradients, which may alleviates the extreme imbalance of positive/negative sampling during training. We simply assigns the center 3×3 area as positives, also named “center sampling” in FCOS [29]. The performance of the detector improves to 45.0% AP as in Tab. 2, already surpassing the current best practice of ultralytics-YOLOv3 (44.3% AP2 ).

reg where λ is a balancing coefficient. Lcls ij and Lij are classficiation loss and regression loss between gt gi and prediction pj . Then, for gt gi , we select the top k predictions with the least cost within a fixed center region as its positive samples. Finally, the corresponding grids of those positive predictions are assigned as positives, while the rest grids are negatives. Noted that the value k varies for different ground-truth. Please refer to Dynamic k Estimation strategy in OTA [4] for more details. SimOTA not only reduces the training time but also avoids additional solver hyperparameters in SinkhornKnopp algorithm. As shown in Tab. 2, SimOTA raises the detector from 45.0% AP to 47.3% AP, higher than the SOTA ultralytics-YOLOv3 by 3.0% AP, showing the power of the advanced assigning strategy.

SimOTA Advanced label assignment is another important progress of object detection in recent years. Based on our own study OTA [4], we conclude four key insights for an advanced label assignment: 1). loss/quality aware, 2). center prior, 3). dynamic number of positive anchors4 for each ground-truth (abbreviated as dynamic top-k), 4). global view. OTA meets all four rules above, hence we choose it as a candidate label assigning strategy. Specifically, OTA [4] analyzes the label assignment from a global perspective and formulate the assigning procedure as an Optimal Transport (OT) problem, producing the SOTA performance among the current assigning strategies [12, 41, 36, 22, 37]. However, in practice we found solving OT problem via Sinkhorn-Knopp algorithm brings 25% extra training time, which is quite expensive for training 300 epochs. We thus simplify it to dynamic top-k strategy, named SimOTA, to get an approximate solution.

End-to-end YOLO We follow [39] to add two additional conv layers, one-to-one label assignment, and stop gradient. These enable the detector to perform an end-to-end manner, but slightly decreasing the performance and the inference speed, as listed in Tab. 2. We thus leave it as an optional module which is not involved in our final models.

2.2. Other Backbones Besides DarkNet53, we also test YOLOX on other backbones with different sizes, where YOLOX achieves consistent improvements against all the corresponding counterparts.

YOLOX-Nano. Specifically, we remove the mix up augmentation and weaken the mosaic (reduce the scale range from [0.1, 2.0] to [0.5, 1.5]) when training small models, i.e., YOLOX-S, YOLOX-Tiny, and YOLOX-Nano. Such a modification improves YOLOX-Nano’s AP from 24.0% to 25.3%. For large models, we also found that stronger augmentation is more helpful. Indeed, our MixUp implementation is part of heavier than the original version in [38]. Inspired by Copypaste [6], we jittered both images by a random sampled scale factor before mixing up them. To understand the power of Mixup with scale jittering, we compare it with Copypaste on YOLOX-L. Noted that Copypaste requires extra instance mask annotations while MixUp does not. But as shown in Tab. 5, these two methods achieve competitive performance, indicating that MixUp with scale jittering is a qualified replacement for Copypaste when no instance mask annotation is available.

Table 4: Comparison of YOLOX-Tiny and YOLOX-Nano and the counterparts in terms of AP (%) on COCO val. All the models are tested at 416 × 416 resolution.

Table 5: Effects of data augmentation under different model sizes. “Scale Jit.” stands for the range of scale jittering for mosaic image. Instance mask annotations from COCO trainval are used when adopting Copypaste.

Modified CSPNet in YOLOv5 To give a fair comparison, we adopt the exact YOLOv5’s backbone including modified CSPNet [31], SiLU activation, and the PAN [19] head. We also follow its scaling rule to product YOLOXS, YOLOX-M, YOLOX-L, and YOLOX-X models. Compared to YOLOv5 in Tab. 3, our models get consistent improvement by ∼3.0% to ∼1.0% AP, with only marginal time increasing (comes from the decoupled head).

3. Comparison with the SOTA There is a tradition to show the SOTA comparing table as in Tab. 6. However, keep in mind that the inference speed of the models in this table is often uncontrolled, as speed varies with software and hardware. We thus use the same hardware and code base for all the YOLO series in Fig. 1, plotting the somewhat controlled speed/accuracy curve. We notice that there are some high performance YOLO series with larger model sizes like Scale-YOLOv4 [30] and YOLOv5-P6 [7]. And the current Transformer based detectors [21] push the accuracy-SOTA to ∼60 AP. Due to the time and resource limitation, we did not explore those important features in this report. However, they are already in our scope.

Tiny and Nano detectors We further shrink our model as YOLOX-Tiny to compare with YOLOv4-Tiny [30]. For mobile devices, we adopt depth wise convolution to construct a YOLOX-Nano model, which has only 0.91M parameters and 1.08G FLOPs. As shown in Tab. 4, YOLOX performs well with even smaller model size than the counterparts. Model size and data augmentation In our experiments, all the models keep almost the same learning schedule and optimizing parameters as depicted in 2.1. However, we found that the suitable augmentation strategy varies across different size of models. As Tab. 5 shows, while applying MixUp for YOLOX-L can improve AP by 0.9%, it is better to weaken the augmentation for small models like

Method

Table 6: Comparison of the speed and accuracy of different object detectors on COCO 2017 test-dev. We select all the models trained on 300 epochs for fair comparison.

hind this metric is to jointly evaluate the output of the entire perception stack at every time instant, forcing the stack to consider the amount of streaming data that should be ignored while computation is occurring [15]. We found that the best trade-off point for the metric on 30 FPS data stream is a powerful model with the inference time ≤ 33ms. So we adopt a YOLOX-L model with TensorRT to product our final model for the challenge to win the 1st place. Please refer to the challenge website5 for more details.

This research was supported by National Key R&D Program of China (No. 2017YFA0700800). It was also funded by China Postdoctoral Science Foundation (2021M690375) and Beijing Postdoctoral Research Foundation
