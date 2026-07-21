# 003 - YOLOv3: An Incremental Improvement

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `redmon2018yolov3` |
| Judul asli | YOLOv3: An Incremental Improvement |
| Penulis | Joseph Redmon, Ali Farhadi |
| Tahun | 2018 |
| Venue | arXiv preprint arXiv:1804.02767 (laporan teknis) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1804.02767
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv3%3A%20An%20Incremental%20Improvement
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv3%3A%20An%20Incremental%20Improvement&sort=relevance

## Gambaran Umum

YOLOv3 adalah pemutakhiran inkremental atas YOLOv2 (bab 002): tidak ada perubahan paradigma, melainkan tiga perbaikan terarah. Pertama, backbone Darknet-19 diganti Darknet-53 — jaringan 53 lapis dengan koneksi residual yang memperkuat ekstraksi fitur tanpa memperlambat berarti. Kedua, prediksi dilakukan pada tiga skala peta fitur sekaligus (bukan satu skala seperti sebelumnya), yang secara langsung menyerang kelemahan terbesar YOLOv2: deteksi objek kecil. Ketiga, klasifikasi memakai pengklasifikasi logistik independen per kelas alih-alih *softmax*, sehingga label yang saling tumpang tindih dapat ditangani.

Hasilnya adalah keseimbangan kecepatan-akurasi yang matang: YOLOv3-608 mencapai 33,0% AP pada COCO dengan 51 milidetik per citra — sekitar 3,8 kali lebih cepat dari RetinaNet pada akurasi yang masih kompetitif, dan unggul pada metrik longgar (AP50 57,9%). Kombinasi kecepatan, kemudahan modifikasi, dan dokumentasi yang terbuka menjadikan YOLOv3 baseline paling banyak dipakai dalam tinjauan ini, termasuk pada klaster aplikasi pertanian dan integrasi RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Dua masalah tersisa dari YOLOv2. Masalah pertama adalah objek kecil. YOLOv2 memang menambahkan *passthrough layer*, tetapi prediksi tetap dilakukan pada satu peta fitur 13×13: pada peta serinci itu, objek yang hanya berukuran beberapa piksel pada citra asal sudah terlalu tereduksi untuk dikenali. Detektor pesaing seperti RetinaNet (bab 016) dan SSD (bab 015) mengatasi masalah ini dengan memprediksi pada beberapa skala fitur sekaligus — fitur dangkal yang rinci untuk objek kecil, fitur dalam yang kaya makna untuk objek besar.

Masalah kedua adalah kapasitas fitur. Darknet-19 relatif dangkal; menambah kedalaman jaringan biasa justru menurunkan kinerja karena degradasi gradien — masalah yang di komunitas visi dipecahkan oleh koneksi residual pada ResNet (bab 147). Selain itu, mekanisme WordTree dari YOLO9000 terbukti rumit dan tidak dilanjutkan; sebagai gantinya diperlukan cara sederhana untuk menangani label yang saling tumpang tindih (mis. sebuah kotak bisa sah berlabel "perempuan" dan "orang" sekaligus), yang tidak dapat dilakukan *softmax* karena *softmax* memaksa satu kelas pemenang.

## Ide Utama

Gagasan YOLOv3 dapat diringkas menjadi: pertahankan mesin prediksi YOLOv2 yang sudah stabil, lalu perkuat dua komponen penentunya — fitur dan skala. Fitur diperkuat dengan backbone residual yang dalam; skala diperbanyak dengan menempelkan kepala prediksi pada tiga tingkat kedalaman jaringan, mengikuti pola piramida fitur (FPN, bab 018). Setiap skala diberi tanggung jawab terhadap ukuran objek yang berbeda melalui pembagian *anchor*, sehingga objek kecil dideteksi pada peta rinci dan objek besar pada peta kasar. Untuk klasifikasi, satu *softmax* diganti banyak pengklasifikasi biner independen — perubahan kecil yang menghapus asumsi bahwa kelas-kelas saling eksklusif.

## Cara Kerja Langkah demi Langkah

### Darknet-53

Backbone baru ini memiliki 53 lapis konvolusi, tersusun dari pasangan konvolusi 1×1 dan 3×3 yang diulang, dengan **koneksi residual**: keluaran suatu blok ditambahkan dengan masukannya sendiri sebelum diteruskan. Penjumlahan pintas ini memberi gradien jalur langsung saat pelatihan, sehingga jaringan yang dalam tetap dapat dilatih tanpa degradasi. Tidak ada *pooling*; pengecilan resolusi dilakukan konvolusi berlangkah (*stride*) 2. Menurut naskah, Darknet-53 mencapai akurasi klasifikasi ImageNet setara ResNet-101 dengan kecepatan 1,5 kali lipat, dan setara ResNet-152 dengan kecepatan 2 kali lipat.

### Prediksi Tiga Skala

Keluaran Darknet-53 pada citra masukan 416×416 menghasilkan peta fitur 13×13 (dibagi 32). YOLOv3 memasang kepala prediksi pada peta ini, kemudian mengambil fitur dua tingkat lebih awal: peta 13×13 di-*upsample* dua kali menjadi 26×26 dan digabung (*concatenate*) dengan fitur dari lapis tengah; kepala kedua memprediksi pada 26×26 (dibagi 16). Proses yang sama diulang sekali lagi untuk menghasilkan kepala ketiga pada 52×52 (dibagi 8). Dengan demikian objek besar dideteksi pada peta 13×13, objek sedang pada 26×26, dan objek kecil pada peta 52×52 yang rinci.

```
citra 416x416
     │
     ▼
Darknet-53 (residual)                 kepala prediksi (per skala:
     │                                3 anchor × (4 box + 1 objek + C kelas))
     ├── 13x13  ──────────────────►  objek besar   (anchor terbesar)
     │      │
     │      └─ upsample ×2, gabung fitur lapis tengah
     ├── 26x26  ──────────────────►  objek sedang
     │      │
     │      └─ upsample ×2, gabung fitur lapis awal
     └── 52x52  ──────────────────►  objek kecil   (anchor terkecil)
```

Setiap skala memakai 3 *anchor box*, sehingga totalnya 9 anchor yang ditentukan dengan *k-means clustering* pada dataset COCO (mewarisi teknik dimension clusters dari bab 002). Anchor terbesar ditempatkan pada skala terkasar, anchor terkecil pada skala terinci. Rumus prediksi kotak identik dengan YOLOv2: offset pusat diikat pada sel melalui fungsi logistik, ukuran diprediksi sebagai faktor skala terhadap anchor.

### Skor Objek dan Klasifikasi Multi-Label

Setiap kotak prediksi memperoleh skor *objectness* melalui regresi logistik: nilai 1 untuk anchor yang tumpang tindih paling baik dengan objek kebenaran, 0 untuk lainnya. Untuk kelas, YOLOv3 mengganti *softmax* dengan **pengklasifikasi logistik independen per kelas** yang dilatih dengan *binary cross-entropy*. Artinya setiap kelas dinilai sendiri-sendiri "ya/tidak", sehingga satu kotak dapat memperoleh beberapa label sekaligus tanpa dipaksa memilih satu pemenang. Perubahan ini sekaligus menutup mekanisme WordTree yang rumit dari generasi sebelumnya.

## Eksperimen dan Hasil

Evaluasi dilakukan pada COCO dengan metrik AP rata-rata pada ambang IOU 0,5:0,95 (metrik ketat), AP50 (ambang longgar), serta AP per ukuran objek (kecil/sedang/besar). Hasil utama:

- YOLOv3-608: 33,0% AP, 57,9% AP50, pada 51 ms per citra (Titan X).
- YOLOv3-320: 28,2% AP pada 22 ms — setara akurasi SSD-321 tetapi tiga kali lebih cepat.
- Pembanding: RetinaNet-101-800 mencapai 37,8% AP dan 61,1% AP50 pada 198 ms.

Interpretasinya dua sisi. Pada ambang longgar (AP50) YOLOv3 nyaris menyamai RetinaNet dengan kecepatan hampir 4 kali lipat — untuk banyak aplikasi praktis, ini titik yang lebih berguna. Namun pada ambang ketat YOLOv3 tertinggal, yang menunjukkan lokalisasinya masih kurang halus: kotaknya benar, tetapi tidak tepat-tepat. Pada sisi positif, AP untuk objek kecil naik jelas dibanding YOLOv2 berkat prediksi tiga skala — persis masalah yang hendak dipecahkan.

## Kelebihan dan Keterbatasan

Kelebihan: (1) keseimbangan kecepatan-akurasi terbaik pada masanya untuk kelas detektor *real-time*; (2) deteksi objek kecil membaik signifikan lewat prediksi tiga skala; (3) backbone residual menjadi fondasi yang kuat untuk modifikasi lanjutan; (4) desainnya sederhana, terdokumentasi terbuka, dan mudah dipotong-tempel — alasan utamanya menjadi baseline de-facto pada banyak bab aplikasi dalam tinjauan ini.

Keterbatasan: (1) AP pada ambang IOU ketat kalah dari detektor yang berorientasi akurasi seperti RetinaNet; (2) masih bergantung pada *anchor* yang harus disetel per dataset (baru dihapus pada bab 005); (3) objek yang sangat kecil atau berhimpitan rapat tetap sulit; (4) dari sisi ilmiah, makalah ini berupa laporan teknis tanpa ablation formal yang mendalam — klaim kontribusi tiap komponen tidak sekuat makalah konferensi penuh.

## Kaitan dengan Bab Lain

Bab ini melanjutkan langsung bab 002: mesin prediksi (anchor, offset terikat sel, *objectness* logistik) diwarisi, sedangkan WordTree ditinggalkan. Dua komponen barunya adalah adopsi dari luar keluarga YOLO: koneksi residual dari ResNet (bab 147) dan piramida fitur multi-skala dari FPN (bab 018), keduanya menjawab kelemahan objek kecil yang tersisa sejak bab 001. Resep YOLOv3 inilah yang disempurnakan secara masif oleh bab 004 (YOLOv4), dan head-nya yang berbasis *anchor* menjadi titik berangkat pembaruan bab 005 (YOLOX). Pada klaster aplikasi — terutama pertanian (bab 120–127) — YOLOv3 adalah backbone yang paling sering dimodifikasi.

## Poin untuk Sitasi

Kutip dengan kunci `redmon2018yolov3`; perhatikan bahwa terbitannya berupa laporan teknis arXiv, bukan prosiding konferensi. Ringkasan yang aman dikutip: "YOLOv3 memadukan backbone residual Darknet-53 dengan prediksi tiga skala bergaya piramida fitur dan klasifikasi logistik multi-label, mencapai 33,0% AP (57,9% AP50) pada COCO dengan 51 ms per citra." Angka hasil di atas dari tabel naskah; perbandingan kecepatan antarperangkat keras sebaiknya dikutip bersama keterangan GPU yang dipakai naskah.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
We present some updates to YOLO! We made a bunch of little design changes to make it better. We also trained this new network that’s pretty swell. It’s a little bigger than last time but more accurate. It’s still fast though, don’t worry. At 320 × 320 YOLOv3 runs in 22 ms at 28.2 mAP, as accurate as SSD but three times faster. When we look at the old .5 IOU mAP detection metric YOLOv3 is quite good. It achieves 57.9 AP50 in 51 ms on a Titan X, compared to 57.5 AP50 in 198 ms by RetinaNet, similar performance but 3.8× faster. As always, all the code is online at https://pjreddie.com/yolo/.

Abstract

Figure 1. We adapt this figure from the Focal Loss paper [9]. YOLOv3 runs significantly faster than other detection methods with comparable performance. Times from either an M40 or Titan X, they are basically the same GPU.

1. Introduction

2.1. Bounding Box Prediction

Sometimes you just kinda phone it in for a year, you know? I didn’t do a whole lot of research this year. Spent a lot of time on Twitter. Played around with GANs a little. I had a little momentum left over from last year [12] [1]; I managed to make some improvements to YOLO. But, honestly, nothing like super interesting, just a bunch of small changes that make it better. I also helped out with other people’s research a little. Actually, that’s what brings us here today. We have a camera-ready deadline [4] and we need to cite some of the random updates I made to YOLO but we don’t have a source. So get ready for a TECH REPORT! The great thing about tech reports is that they don’t need intros, y’all know why we’re here. So the end of this introduction will signpost for the rest of the paper. First we’ll tell you what the deal is with YOLOv3. Then we’ll tell you how we do. We’ll also tell you about some things we tried that didn’t work. Finally we’ll contemplate what this all means.

During training we use sum of squared error loss. If the ground truth for some coordinate prediction is t̂* our gradient is the ground truth value (computed from the ground truth box) minus our prediction: t̂* − t* . This ground truth value can be easily computed by inverting the equations above. YOLOv3 predicts an objectness score for each bounding box using logistic regression. This should be 1 if the bounding box prior overlaps a ground truth object by more than any other bounding box prior. If the bounding box prior

2. The Deal So here’s the deal with YOLOv3: We mostly took good ideas from other people. We also trained a new classifier network that’s better than the other ones. We’ll just take you through the whole system from scratch so you can understand it all. 1

Figure 2. Bounding boxes with dimension priors and location prediction. We predict the width and height of the box as offsets from cluster centroids. We predict the center coordinates of the box relative to the location of filter application using a sigmoid function. This figure blatantly self-plagiarized from [15].

Next we take the feature map from 2 layers previous and upsample it by 2×. We also take a feature map from earlier in the network and merge it with our upsampled features using concatenation. This method allows us to get more meaningful semantic information from the upsampled features and finer-grained information from the earlier feature map. We then add a few more convolutional layers to process this combined feature map, and eventually predict a similar tensor, although now twice the size. We perform the same design one more time to predict boxes for the final scale. Thus our predictions for the 3rd scale benefit from all the prior computation as well as finegrained features from early on in the network. We still use k-means clustering to determine our bounding box priors. We just sort of chose 9 clusters and 3 scales arbitrarily and then divide up the clusters evenly across scales. On the COCO dataset the 9 clusters were: (10 × 13), (16 × 30), (33 × 23), (30 × 61), (62 × 45), (59 × 119), (116 × 90), (156 × 198), (373 × 326).

2.4. Feature Extractor is not the best but does overlap a ground truth object by more than some threshold we ignore the prediction, following [17]. We use the threshold of .5. Unlike [17] our system only assigns one bounding box prior for each ground truth object. If a bounding box prior is not assigned to a ground truth object it incurs no loss for coordinate or class predictions, only objectness.

2.2. Class Prediction Each box predicts the classes the bounding box may contain using multilabel classification. We do not use a softmax as we have found it is unnecessary for good performance, instead we simply use independent logistic classifiers. During training we use binary cross-entropy loss for the class predictions. This formulation helps when we move to more complex domains like the Open Images Dataset [7]. In this dataset there are many overlapping labels (i.e. Woman and Person). Using a softmax imposes the assumption that each box has exactly one class which is often not the case. A multilabel approach better models the data.

2.3. Predictions Across Scales YOLOv3 predicts boxes at 3 different scales. Our system extracts features from those scales using a similar concept to feature pyramid networks [8]. From our base feature extractor we add several convolutional layers. The last of these predicts a 3-d tensor encoding bounding box, objectness, and class predictions. In our experiments with COCO [10] we predict 3 boxes at each scale so the tensor is N × N × [3 ∗ (4 + 1 + 80)] for the 4 bounding box offsets, 1 objectness prediction, and 80 class predictions.

Table 2. Comparison of backbones. Accuracy, billions of operations, billion floating point operations per second, and FPS for various networks.

Each network is trained with identical settings and tested at 256 × 256, single crop accuracy. Run times are measured on a Titan X at 256 × 256. Thus Darknet-53 performs on par with state-of-the-art classifiers but with fewer floating point operations and more speed. Darknet-53 is better than ResNet-101 and 1.5× faster. Darknet-53 has similar performance to ResNet-152 and is 2× faster. Darknet-53 also achieves the highest measured floating point operations per second. This means the network structure better utilizes the GPU, making it more efficient to evaluate and thus faster. That’s mostly because ResNets have just way too many layers and aren’t very efficient.

2.5. Training We still train on full images with no hard negative mining or any of that stuff. We use multi-scale training, lots of data augmentation, batch normalization, all the standard stuff. We use the Darknet neural network framework for training and testing [14].

models like RetinaNet in this metric though. However, when we look at the “old” detection metric of mAP at IOU= .5 (or AP50 in the chart) YOLOv3 is very strong. It is almost on par with RetinaNet and far above the SSD variants. This indicates that YOLOv3 is a very strong detector that excels at producing decent boxes for objects. However, performance drops significantly as the IOU threshold increases indicating YOLOv3 struggles to get the boxes perfectly aligned with the object. In the past YOLO struggled with small objects. However, now we see a reversal in that trend. With the new multi-scale predictions we see YOLOv3 has relatively high APS performance. However, it has comparatively worse performance on medium and larger size objects. More investigation is needed to get to the bottom of this. When we plot accuracy vs speed on the AP50 metric (see figure 5) we see YOLOv3 has significant benefits over other detection systems. Namely, it’s faster and better.

4. Things We Tried That Didn’t Work We tried lots of stuff while we were working on YOLOv3. A lot of it didn’t work. Here’s the stuff we can remember. Anchor box x, y offset predictions. We tried using the normal anchor box prediction mechanism where you predict the x, y offset as a multiple of the box width or height using a linear activation. We found this formulation decreased model stability and didn’t work very well. Linear x, y predictions instead of logistic. We tried using a linear activation to directly predict the x, y offset instead of the logistic activation. This led to a couple point drop in mAP. Focal loss. We tried using focal loss. It dropped our mAP about 2 points. YOLOv3 may already be robust to the problem focal loss is trying to solve because it has separate objectness predictions and conditional class predictions. Thus for most examples there is no loss from the class predictions? Or something? We aren’t totally sure.

Table 3. I’m seriously just stealing all these tables from [9] they take soooo long to make from scratch. Ok, YOLOv3 is doing alright. Keep in mind that RetinaNet has like 3.8× longer to process an image. YOLOv3 is much better than SSD variants and comparable to state-of-the-art models on the AP50 metric.

Figure 3. Again adapted from the [9], this time displaying speed/accuracy tradeoff on the mAP at .5 IOU metric. You can tell YOLOv3 is good because it’s very high and far to the left. Can you cite your own paper? Guess who’s going to try, this guy → [16]. Oh, I forgot, we also fix a data loading bug in YOLOv2, that helped by like 2 mAP. Just sneaking this in here to not throw off layout.

Dual IOU thresholds and truth assignment. Faster RCNN uses two IOU thresholds during training. If a prediction overlaps the ground truth by .7 it is as a positive example, by [.3 − .7] it is ignored, less than .3 for all ground truth objects it is a negative example. We tried a similar strategy but couldn’t get good results. We quite like our current formulation, it seems to be at a local optima at least. It is possible that some of these techniques could eventually produce good results, perhaps they just need some tuning to stabilize the training.

5. What This All Means YOLOv3 is a good detector. It’s fast, it’s accurate. It’s not as great on the COCO average AP between .5 and .95 IOU metric. But it’s very good on the old detection metric of .5 IOU. Why did we switch metrics anyway? The original COCO paper just has this cryptic sentence: “A full discussion of evaluation metrics will be added once the evaluation server is complete”. Russakovsky et al report that that humans have a hard time distinguishing an IOU of .3 from .5! “Training humans to visually inspect a bounding box with IOU of 0.3 and distinguish it from one with IOU 0.5 is sur-

prisingly difficult.” [18] If humans have a hard time telling the difference, how much does it matter? But maybe a better question is: “What are we going to do with these detectors now that we have them?” A lot of the people doing this research are at Google and Facebook. I guess at least we know the technology is in good hands and definitely won’t be used to harvest your personal information and sell it to.... wait, you’re saying that’s exactly what it will be used for?? Oh. Well the other people heavily funding vision research are the military and they’ve never done anything horrible like killing lots of people with new technology oh wait.....1 I have a lot of hope that most of the people using computer vision are just doing happy, good stuff with it, like counting the number of zebras in a national park [13], or tracking their cat as it wanders around their house [19]. But computer vision is already being put to questionable use and as researchers we have a responsibility to at least consider the harm our work might be doing and think of ways to mitigate it. We owe the world that much. In closing, do not @ me. (Because I finally quit Twitter). 1 The author is funded by the Office of Naval Research and Google.
