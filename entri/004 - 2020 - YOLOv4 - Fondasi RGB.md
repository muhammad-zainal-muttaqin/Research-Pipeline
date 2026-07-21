# 004 - YOLOv4: Optimal Speed and Accuracy of Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bochkovskiy2020yolov4` |
| Judul asli | YOLOv4: Optimal Speed and Accuracy of Object Detection |
| Penulis | Alexey Bochkovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao |
| Tahun | 2020 |
| Venue | arXiv preprint arXiv:2004.10934 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2004.10934
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv4%3A%20Optimal%20Speed%20and%20Accuracy%20of%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv4%3A%20Optimal%20Speed%20and%20Accuracy%20of%20Object%20Detection&sort=relevance

## Gambaran Umum

YOLOv4 bukanlah paradigma baru, melainkan **sintesis rekayasa**: penulisnya mengumpulkan puluhan teknik peningkatan deteksi yang tersebar di literatur 2015–2020, menguji kombinasinya secara sistematis, dan menyusun hasil terbaiknya menjadi satu resep detektor. Resep itu terdiri atas backbone CSPDarknet53, neck SPP + PANet, dan head YOLOv3 (bab 003), dilatih dengan seperangkat teknik yang dikelompokkan menjadi *Bag of Freebies* (teknik yang menambah biaya hanya saat pelatihan) dan *Bag of Specials* (modul yang menambah sedikit biaya inferensi demi akurasi yang jauh lebih besar).

Hasilnya: 43,5% AP (65,7% AP50) pada COCO dengan kecepatan ±65 FPS pada satu GPU V100 — titik kecepatan-akurasi terbaik pada masanya. Sama pentingnya, seluruh resep dapat dilatih pada **satu GPU konsumen** (1080 Ti atau 2080 Ti), sehingga detektor kelas riset menjadi terjangkau bagi praktisi — alasan utama YOLOv4 menjadi basis banyak bab aplikasi dalam tinjauan ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Antara 2015 dan 2020, literatur deteksi objek menghasilkan banyak teknik perbaikan: fungsi loss baru, metode augmentasi, modul perhatian, desain backbone hemat komputasi, dan sebagainya. Namun teknik-teknik itu diusulkan terpisah-pisah, diuji pada detektor yang berbeda-beda, dan tidak jelas kombinasi mana yang benar-benar bekerja ketika disatukan. Praktisi yang ingin memakai detektor terbaik harus menebak sendiri resepnya — dan sebagian resep menuntut pelatihan multi-GPU yang mahal.

YOLOv3 (bab 003) pada saat yang sama sudah menjadi baseline industri karena cepat dan stabil, tetapi akurasinya mulai tertinggal dari detektor baru seperti EfficientDet (bab 021). Pertanyaan yang dijawab makalah ini: seberapa jauh akurasi YOLOv3 dapat dinaikkan hanya dengan memilih dan mengombinasikan teknik yang sudah ada, tanpa mengorbankan kecepatan *real-time* dan tanpa menuntut perangkat pelatihan besar?

## Ide Utama

Gagasan pengorganisasian makalah ini adalah pembagian semua teknik peningkatan ke dalam dua kantong:

- ***Bag of Freebies* (BoF)** — teknik yang hanya mengubah strategi pelatihan tanpa menambah biaya inferensi sedikit pun: metode augmentasi data, fungsi loss yang lebih baik, regularisasi, penjadwalan laju pembelajaran. Karena "gratis" saat model dipakai, teknik ini murni menguntungkan bila terbukti menaikkan akurasi.
- ***Bag of Specials* (BoS)** — modul arsitektur atau pasca-pemrosesan yang menambah sedikit biaya inferensi tetapi memberi lompatan akurasi yang tidak sebanding kecilnya: perluasan receptive field, modul perhatian, agregasi fitur, NMS yang lebih baik.

Dengan kerangka ini, kontribusi makalah adalah **kurasi berbasis eksperimen**: setiap kandidat teknik diuji pengaruhnya pada detektor yang sama, dan hanya yang terbukti pada konfigurasi YOLO yang dipertahankan.

## Cara Kerja Langkah demi Langkah

### Arsitektur: Backbone, Neck, Head

Detektor YOLOv4 dipahami paling mudah sebagai tiga bagian. **Backbone** CSPDarknet53 adalah Darknet-53 (bab 003) yang dimodifikasi dengan *Cross Stage Partial* (CSP): peta fitur pada setiap tahap dibelah dua — satu cabang melewati blok residual, satu cabang menjadi pintasan — lalu keduanya digabung kembali. Pembelahan ini mengurangi komputasi sekitar 20% sekaligus memperkaya aliran gradien, sehingga akurasi terjaga atau justru naik dengan biaya lebih murah.

**Neck** terdiri atas dua modul. SPP (*Spatial Pyramid Pooling*) meneruskan peta fitur melalui beberapa *max-pooling* berukuran berbeda (5×5, 9×9, 13×13) secara paralel lalu menggabungkan hasilnya dengan masukan asal; efeknya, receptive field diperluas tanpa mengubah resolusi. PANet (*Path Aggregation Network*) menambah jalur agregasi **bottom-up** di atas jalur top-down ala FPN (bab 018): informasi lokasi yang rinci dari lapis dangkal disalurkan ke atas, melengkapi informasi semantik dari lapis dalam yang disalurkan ke bawah. **Head** tetap kepala prediksi YOLOv3 — tiga skala, berbasis *anchor*.

Susunan ketiga bagian dan tempat dua "kantong" teknik bekerja:

```
citra ──► backbone CSPDarknet53 ──► neck ──► head YOLOv3 ──► deteksi
              │                  ┌──┴──┐        │              │
              │                  ▼     ▼        ▼              ▼
        fitur dibelah dua,    SPP   PANet   3 skala,     NMS (DIoU):
        digabung kembali   (pool  (top-down  anchor      saring kotak
        (hemat ±20% FLOPs)  5/9/13) +bottom-up)           duplikat

  Bag of Freebies (hanya saat latih): Mosaic, CutMix, CmBN, DropBlock,
      label smoothing, CIoU loss, SAT, cosine annealing
  Bag of Specials (biaya inferensi kecil): Mish, CSP, SPP, SAM, PAN, DIoU-NMS
```

### Bag of Freebies: Teknik Pelatihan

Teknik BoF yang dipertahankan setelah seleksi antara lain:

- **Mosaic augmentation**: empat citra pelatihan digabung menjadi satu citra komposit. Model belajar mengenali objek pada konteks dan skala yang lebih beragam dalam satu masukan, dan statistik *batch normalization* dihitung dari empat citra sekaligus — ini mengurangi kebutuhan *mini-batch* besar, kunci pelatihan pada satu GPU.
- **CIoU loss**: fungsi loss regresi kotak pengganti sum-squared. Selain menghukum ketidakcocokan luasan (IoU), CIoU juga menghukum jarak antara pusat kotak prediksi dan kebenaran serta ketidaksesuaian rasio aspek, sehingga regresi kotak konvergen lebih cepat dan lebih tepat.
- **Self-Adversarial Training (SAT)**: pelatihan dua tahap di mana model terlebih dahulu menghasilkan citra adversarial terhadap dirinya sendiri (mengubah piksel, bukan bobot, untuk "menipu" deteksi), kemudian dilatih agar tetap mendeteksi dengan benar pada citra yang diubah itu — bentuk regularisasi yang memperkuat ketahanan.
- **CmBN** (*Cross mini-Batch Normalization*): statistik normalisasi dikumpulkan dari beberapa iterasi kecil dalam satu *batch*, menstabilkan pelatihan batch kecil.
- Pendukung lain: *label smoothing* (target kelas dilembutkan dari 0/1 keras menjadi nilai antara, mengurangi overconfidence), *DropBlock* (regularisasi yang membuang blok wilayah bersebelahan pada peta fitur alih-alih piksel acak), penjadwalan *cosine annealing*, dan bentuk masukan acak.

### Bag of Specials: Modul Tambahan

Teknik BoS yang dipertahankan antara lain: aktivasi **Mish** (fungsi aktivasi halus pengganti ReLU yang terbukti memberi akurasi sedikit lebih baik pada backbone ini), **SAM** termodifikasi (*Spatial Attention Module*: modul perhatian yang menimbang wilayah penting pada peta fitur; penulis mengubahnya dari perhatian spasial menjadi perhatian titik), dan **DIoU-NMS**: *Non-Maximum Suppression* yang menyeleksi kotak duplikat bukan hanya dari luas irisan, tetapi juga jarak antar-pusat kotak, sehingga dua objek bersebelahan lebih jarang saling hapus.

## Eksperimen dan Hasil

Pengujian dilakukan pada COCO dengan analisis ablation menyeluruh — inilah nilai ilmiah utama makalah ini: pengaruh tiap fitur, tiap kombinasi BoF/BoS, dan tiap pilihan backbone diukur terpisah. Hasil akhir pada COCO test-dev:

- YOLOv4: 43,5% AP dan 65,7% AP50, pada kecepatan ±65 FPS (Tesla V100).
- Peningkatan terhadap YOLOv3 (33,0% AP, bab 003): sekitar 10 poin AP tanpa kehilangan status *real-time*.
- Perbandingan sezaman: mengungguli kombinasi kecepatan-akurasi EfficientDet pada pengujian penulis, dengan kebutuhan pelatihan jauh lebih ringan.

Ablation menunjukkan CSP backbone, Mosaic, dan CIoU termasuk penyumbang gain paling konsisten; dan yang tak kalah penting bagi praktik, seluruh konfigurasi terbukti dapat dilatih pada satu GPU 1080 Ti/2080 Ti.

## Kelebihan dan Keterbatasan

Kelebihan: (1) titik kecepatan-akurasi terbaik saat rilis; (2) resep lengkap dan terdokumentasi, direproduksi luas; (3) hemat perangkat — pelatihan satu GPU; (4) nilai metodologis: peta kontribusi puluhan teknik dalam satu kerangka uji.

Keterbatasan: (1) jumlah teknik dan hiperparameter yang ditumpuk sangat banyak, sehingga menyetel ulang untuk dataset baru tidak sepele; (2) tetap berbasis *anchor*; (3) peningkatannya bersifat rekayasa inkremental, bukan gagasan konseptual baru; (4) dari sisi reproduksi, sebagian klaim ablation sensitif pada detail implementasi yang tidak semuanya terdokumentasi selengkap kode sumbernya.

## Kaitan dengan Bab Lain

Resep YOLOv4 berdiri langsung di atas bab 003: head dan kerangka dasarnya adalah YOLOv3. Bahan-bahannya datang dari banyak bab lain: piramida fitur FPN (bab 018), pola CSP dari keluarga desain backbone, serta tradisi augmentasi dan loss dari literatur deteksi umum. Sebagai "resep jadi", YOLOv4 menjadi basis modifikasi aplikatif dalam tinjauan ini — misalnya deteksi bunga apel dengan pemangkasan model (bab 122) — dan menjadi titik referensi bagi YOLOX (bab 005) yang kemudian merombak head-nya menjadi *anchor-free*.

## Poin untuk Sitasi

Kutip dengan kunci `bochkovskiy2020yolov4`. Ringkasan yang aman dikutip: "YOLOv4 menyeleksi dan mengombinasikan teknik pelatihan (Bag of Freebies: Mosaic, CIoU loss, SAT) dan modul arsitektur (Bag of Specials: CSP, SPP, PAN, Mish) menjadi detektor 43,5% AP pada COCO dengan ±65 FPS yang dapat dilatih pada satu GPU konsumen." Angka 43,5% / 65,7% AP50 / ±65 FPS dari abstrak naskah; rincian ablation per komponen sebaiknya dikutip langsung dari tabel-tabel naskah.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract There are a huge number of features which are said to improve Convolutional Neural Network (CNN) accuracy. Practical testing of combinations of such features on large datasets, and theoretical justification of the result, is required. Some features operate on certain models exclusively and for certain problems exclusively, or only for small-scale datasets; while some features, such as batch-normalization and residual-connections, are applicable to the majority of models, tasks, and datasets. We assume that such universal features include Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP), Cross mini-Batch Normalization (CmBN), Self-adversarial-training (SAT) and Mish-activation. We use new features: WRC, CSP, CmBN, SAT, Mish activation, Mosaic data augmentation, CmBN, DropBlock regularization, and CIoU loss, and combine some of them to achieve state-of-the-art results: 43.5% AP (65.7% AP50 ) for the MS COCO dataset at a realtime speed of ∼65 FPS on Tesla V100. Source code is at https://github.com/AlexeyAB/darknet.

Figure 1: Comparison of the proposed YOLOv4 and other state-of-the-art object detectors. YOLOv4 runs twice faster than EfficientDet with comparable performance. Improves YOLOv3’s AP and FPS by 10% and 12%, respectively. The main goal of this work is designing a fast operating speed of an object detector in production systems and optimization for parallel computations, rather than the low computation volume theoretical indicator (BFLOP). We hope that the designed object can be easily trained and used. For example, anyone who uses a conventional GPU to train and test can achieve real-time, high quality, and convincing object detection results, as the YOLOv4 results shown in Figure 1. Our contributions are summarized as follows:

1. Introduction The majority of CNN-based object detectors are largely applicable only for recommendation systems. For example, searching for free parking spaces via urban video cameras is executed by slow accurate models, whereas car collision warning is related to fast inaccurate models. Improving the real-time object detector accuracy enables using them not only for hint generating recommendation systems, but also for stand-alone process management and human input reduction. Real-time object detector operation on conventional Graphics Processing Units (GPU) allows their mass usage at an affordable price. The most accurate modern neural networks do not operate in real time and require large number of GPUs for training with a large mini-batch-size. We address such problems through creating a CNN that operates in real-time on a conventional GPU, and for which training requires only one conventional GPU.

1. We develope an efficient and powerful object detection model. It makes everyone can use a 1080 Ti or 2080 Ti GPU to train a super fast and accurate object detector. 2. We verify the influence of state-of-the-art Bag-ofFreebies and Bag-of-Specials methods of object detection during the detector training. 3. We modify state-of-the-art methods and make them more effecient and suitable for single GPU training, including CBN [89], PAN [49], SAM [85], etc. 1

2. Related work

2.2. Bag of freebies

Usually, a conventional object detector is trained offline. Therefore, researchers always like to take this advantage and develop better training methods which can make the object detector receive better accuracy without increasing the inference cost. We call these methods that only change the training strategy or only increase the training cost as “bag of freebies.” What is often adopted by object detection methods and meets the definition of bag of freebies is data augmentation. The purpose of data augmentation is to increase the variability of the input images, so that the designed object detection model has higher robustness to the images obtained from different environments. For examples, photometric distortions and geometric distortions are two commonly used data augmentation method and they definitely benefit the object detection task. In dealing with photometric distortion, we adjust the brightness, contrast, hue, saturation, and noise of an image. For geometric distortion, we add random scaling, cropping, flipping, and rotating. The data augmentation methods mentioned above are all pixel-wise adjustments, and all original pixel information in the adjusted area is retained. In addition, some researchers engaged in data augmentation put their emphasis on simulating object occlusion issues. They have achieved good results in image classification and object detection. For example, random erase [100] and CutOut [11] can randomly select the rectangle region in an image and fill in a random or complementary value of zero. As for hide-and-seek [69] and grid mask [6], they randomly or evenly select multiple rectangle regions in an image and replace them to all zeros. If similar concepts are applied to feature maps, there are DropOut [71], DropConnect [80], and DropBlock [16] methods. In addition, some researchers have proposed the methods of using multiple images together to perform data augmentation. For example, MixUp [92] uses two images to multiply and superimpose with different coefficient ratios, and then adjusts the label with these superimposed ratios. As for CutMix [91], it is to cover the cropped image to rectangle region of other images, and adjusts the label according to the size of the mix area. In addition to the above mentioned methods, style transfer GAN [15] is also used for data augmentation, and such usage can effectively reduce the texture bias learned by CNN. Different from the various approaches proposed above, some other bag of freebies methods are dedicated to solving the problem that the semantic distribution in the dataset may have bias. In dealing with the problem of semantic distribution bias, a very important issue is that there is a problem of data imbalance between different classes, and this problem is often solved by hard negative example mining [72] or online hard example mining [67] in two-stage object detector. But the example mining method is not applicable 3

2.3. Bag of specials

In terms of feature integration, the early practice is to use skip connection [51] or hyper-column [22] to integrate lowlevel physical feature to high-level semantic feature. Since multi-scale prediction methods such as FPN have become popular, many lightweight modules that integrate different feature pyramid have been proposed. The modules of this sort include SFAM [98], ASFF [48], and BiFPN [77]. The main idea of SFAM is to use SE module to execute channelwise level re-weighting on multi-scale concatenated feature maps. As for ASFF, it uses softmax as point-wise level reweighting and then adds feature maps of different scales. In BiFPN, the multi-input weighted residual connections is proposed to execute scale-wise level re-weighting, and then add feature maps of different scales.

For those plugin modules and post-processing methods that only increase the inference cost by a small amount but can significantly improve the accuracy of object detection, we call them “bag of specials”. Generally speaking, these plugin modules are for enhancing certain attributes in a model, such as enlarging receptive field, introducing attention mechanism, or strengthening feature integration capability, etc., and post-processing is a method for screening model prediction results. Common modules that can be used to enhance receptive field are SPP [25], ASPP [5], and RFB [47]. The SPP module was originated from Spatial Pyramid Matching (SPM) [39], and SPMs original method was to split feature map into several d × d equal blocks, where d can be {1, 2, 3, ...}, thus forming spatial pyramid, and then extracting bag-of-word features. SPP integrates SPM into CNN and use max-pooling operation instead of bag-of-word operation. Since the SPP module proposed by He et al. [25] will output one dimensional feature vector, it is infeasible to be applied in Fully Convolutional Network (FCN). Thus in the design of YOLOv3 [63], Redmon and Farhadi improve SPP module to the concatenation of max-pooling outputs with kernel size k × k, where k = {1, 5, 9, 13}, and stride equals to 1. Under this design, a relatively large k × k maxpooling effectively increase the receptive field of backbone feature. After adding the improved version of SPP module, YOLOv3-608 upgrades AP50 by 2.7% on the MS COCO object detection task at the cost of 0.5% extra computation. The difference in operation between ASPP [5] module and improved SPP module is mainly from the original k ×k kernel size, max-pooling of stride equals to 1 to several 3 × 3 kernel size, dilated ratio equals to k, and stride equals to 1 in dilated convolution operation. RFB module is to use several dilated convolutions of k ×k kernel, dilated ratio equals to k, and stride equals to 1 to obtain a more comprehensive spatial coverage than ASPP. RFB [47] only costs 7% extra inference time to increase the AP50 of SSD on MS COCO by 5.7%. The attention module that is often used in object detection is mainly divided into channel-wise attention and pointwise attention, and the representatives of these two attention models are Squeeze-and-Excitation (SE) [29] and Spatial Attention Module (SAM) [85], respectively. Although SE module can improve the power of ResNet50 in the ImageNet image classification task 1% top-1 accuracy at the cost of only increasing the computational effort by 2%, but on a GPU usually it will increase the inference time by about 10%, so it is more appropriate to be used in mobile devices. But for SAM, it only needs to pay 0.1% extra calculation and it can improve ResNet50-SE 0.5% top-1 accuracy on the ImageNet image classification task. Best of all, it does not affect the speed of inference on the GPU at all.

In the research of deep learning, some people put their focus on searching for good activation function. A good activation function can make the gradient more efficiently propagated, and at the same time it will not cause too much extra computational cost. In 2010, Nair and Hinton [56] propose ReLU to substantially solve the gradient vanish problem which is frequently encountered in traditional tanh and sigmoid activation function. Subsequently, LReLU [54], PReLU [24], ReLU6 [28], Scaled Exponential Linear Unit (SELU) [35], Swish [59], hard-Swish [27], and Mish [55], etc., which are also used to solve the gradient vanish problem, have been proposed. The main purpose of LReLU and PReLU is to solve the problem that the gradient of ReLU is zero when the output is less than zero. As for ReLU6 and hard-Swish, they are specially designed for quantization networks. For self-normalizing a neural network, the SELU activation function is proposed to satisfy the goal. One thing to be noted is that both Swish and Mish are continuously differentiable activation function. The post-processing method commonly used in deeplearning-based object detection is NMS, which can be used to filter those BBoxes that badly predict the same object, and only retain the candidate BBoxes with higher response. The way NMS tries to improve is consistent with the method of optimizing an objective function. The original method proposed by NMS does not consider the context information, so Girshick et al. [19] added classification confidence score in R-CNN as a reference, and according to the order of confidence score, greedy NMS was performed in the order of high score to low score. As for soft NMS [1], it considers the problem that the occlusion of an object may cause the degradation of confidence score in greedy NMS with IoU score. The DIoU NMS [99] developers way of thinking is to add the information of the center point distance to the BBox screening process on the basis of soft NMS. It is worth mentioning that, since none of above postprocessing methods directly refer to the captured image features, post-processing is no longer required in the subsequent development of an anchor-free method. 4

Table 1: Parameters of neural networks for image classification. Backbone model

3. Methodology

Hypothetically speaking, we can assume that a model with a larger receptive field size (with a larger number of convolutional layers 3 × 3) and a larger number of parameters should be selected as the backbone. Table 1 shows the information of CSPResNeXt50, CSPDarknet53, and EfficientNet B3. The CSPResNext50 contains only 16 convolutional layers 3 × 3, a 425 × 425 receptive field and 20.6 M parameters, while CSPDarknet53 contains 29 convolutional layers 3 × 3, a 725 × 725 receptive field and 27.6 M parameters. This theoretical justification, together with our numerous experiments, show that CSPDarknet53 neural network is the optimal model of the two as the backbone for a detector. The influence of the receptive field with different sizes is summarized as follows:

3.1. Selection of architecture

Our objective is to find the optimal balance among the input network resolution, the convolutional layer number, the parameter number (filter size2 * filters * channel / groups), and the number of layer outputs (filters). For instance, our numerous studies demonstrate that the CSPResNext50 is considerably better compared to CSPDarknet53 in terms of object classification on the ILSVRC2012 (ImageNet) dataset [10]. However, conversely, the CSPDarknet53 is better compared to CSPResNext50 in terms of detecting objects on the MS COCO dataset [46]. The next objective is to select additional blocks for increasing the receptive field and the best method of parameter aggregation from different backbone levels for different detector levels: e.g. FPN, PAN, ASFF, BiFPN. A reference model which is optimal for classification is not always optimal for a detector. In contrast to the classifier, the detector requires the following:

• Exceeding the network size - increases the number of connections between the image point and the final activation We add the SPP block over the CSPDarknet53, since it significantly increases the receptive field, separates out the most significant context features and causes almost no reduction of the network operation speed. We use PANet as the method of parameter aggregation from different backbone levels for different detector levels, instead of the FPN used in YOLOv3. Finally, we choose CSPDarknet53 backbone, SPP additional module, PANet path-aggregation neck, and YOLOv3 (anchor based) head as the architecture of YOLOv4. In the future we plan to expand significantly the content of Bag of Freebies (BoF) for the detector, which theoretically can address some problems and increase the detector accuracy, and sequentially check the influence of each feature in an experimental fashion. We do not use Cross-GPU Batch Normalization (CGBN or SyncBN) or expensive specialized devices. This allows anyone to reproduce our state-of-the-art outcomes on a conventional graphic processor e.g. GTX 1080Ti or RTX 2080Ti.

Figure 3: Mosaic represents a new method of data augmentation.

mixed, while CutMix mixes only 2 input images. This allows detection of objects outside their normal context. In addition, batch normalization calculates activation statistics from 4 different images on each layer. This significantly reduces the need for a large mini-batch size.

Self-Adversarial Training (SAT) also represents a new data augmentation technique that operates in 2 forward backward stages. In the 1st stage the neural network alters the original image instead of the network weights. In this way the neural network executes an adversarial attack on itself, altering the original image to create the deception that there is no desired object on the image. In the 2nd stage, the neural network is trained to detect an object on this modified image in the normal way.

As for training activation function, since PReLU and SELU are more difficult to train, and ReLU6 is specifically designed for quantization network, we therefore remove the above activation functions from the candidate list. In the method of reqularization, the people who published DropBlock have compared their method with other methods in detail, and their regularization method has won a lot. Therefore, we did not hesitate to choose DropBlock as our regularization method. As for the selection of normalization method, since we focus on a training strategy that uses only one GPU, syncBN is not considered.

3.3. Additional improvements In order to make the designed detector more suitable for training on single GPU, we made additional design and improvement as follows: • We introduce a new method of data augmentation Mosaic, and Self-Adversarial Training (SAT) Figure 4: Cross mini-Batch Normalization.

CmBN represents a CBN modified version, as shown in Figure 4, defined as Cross mini-Batch Normalization (CmBN). This collects statistics only between mini-batches within a single batch.

We modify SAM from spatial-wise attention to pointwise attention, and replace shortcut connection of PAN to concatenation, as shown in Figure 5 and Figure 6, respectively.

Mosaic represents a new data augmentation method that mixes 4 training images. Thus 4 different contexts are 6

4. Experiments We test the influence of different training improvement techniques on accuracy of the classifier on ImageNet (ILSVRC 2012 val) dataset, and then on the accuracy of the detector on MS COCO (test-dev 2017) dataset.

4.1. Experimental setup In ImageNet image classification experiments, the default hyper-parameters are as follows: the training steps is 8,000,000; the batch size and the mini-batch size are 128 and 32, respectively; the polynomial decay learning rate scheduling strategy is adopted with initial learning rate 0.1; the warm-up steps is 1000; the momentum and weight decay are respectively set as 0.9 and 0.005. All of our BoS experiments use the same hyper-parameter as the default setting, and in the BoF experiments, we add an additional 50% training steps. In the BoF experiments, we verify MixUp, CutMix, Mosaic, Bluring data augmentation, and label smoothing regularization methods. In the BoS experiments, we compared the effects of LReLU, Swish, and Mish activation function. All experiments are trained with a 1080 Ti or 2080 Ti GPU.

3.4. YOLOv4 In this section, we shall elaborate the details of YOLOv4.

In MS COCO object detection experiments, the default hyper-parameters are as follows: the training steps is 500,500; the step decay learning rate scheduling strategy is adopted with initial learning rate 0.01 and multiply with a factor 0.1 at the 400,000 steps and the 450,000 steps, respectively; The momentum and weight decay are respectively set as 0.9 and 0.0005. All architectures use a single GPU to execute multi-scale training in the batch size of 64 while mini-batch size is 8 or 4 depend on the architectures and GPU memory limitation. Except for using genetic algorithm for hyper-parameter search experiments, all other experiments use default setting. Genetic algorithm used YOLOv3-SPP to train with GIoU loss and search 300 epochs for min-val 5k sets. We adopt searched learning rate 0.00261, momentum 0.949, IoU threshold for assigning ground truth 0.213, and loss normalizer 0.07 for genetic algorithm experiments. We have verified a large number of BoF, including grid sensitivity elimination, mosaic data augmentation, IoU threshold, genetic algorithm, class label smoothing, cross mini-batch normalization, selfadversarial training, cosine annealing scheduler, dynamic mini-batch size, DropBlock, Optimized Anchors, different kind of IoU losses. We also conduct experiments on various BoS, including Mish, SPP, SAM, RFB, BiFPN, and Gaussian YOLO [8]. For all experiments, we only use one GPU for training, so techniques such as syncBN that optimizes multiple GPUs are not used.

4.2. Influence of different features on Classifier training

4.3. Influence of different features on Detector training

First, we study the influence of different features on classifier training; specifically, the influence of Class label smoothing, the influence of different data augmentation techniques, bilateral blurring, MixUp, CutMix and Mosaic, as shown in Fugure 7, and the influence of different activations, such as Leaky-ReLU (by default), Swish, and Mish.

Further study concerns the influence of different Bag-ofFreebies (BoF-detector) on the detector training accuracy, as shown in Table 4. We significantly expand the BoF list through studying different features that increase the detector accuracy without affecting FPS: • S: Eliminate grid sensitivity the equation bx = σ(tx )+ cx , by = σ(ty ) + cy , where cx and cy are always whole numbers, is used in YOLOv3 for evaluating the object coordinates, therefore, extremely high tx absolute values are required for the bx value approaching the cx or cx + 1 values. We solve this problem through multiplying the sigmoid by a factor exceeding 1.0, so eliminating the effect of grid on which the object is undetectable. • M: Mosaic data augmentation - using the 4-image mosaic during training instead of single image • IT: IoU threshold - using multiple anchors for a single ground truth IoU (truth, anchor) > IoU threshold

Figure 7: Various method of data augmentation. In our experiments, as illustrated in Table 2, the classifier’s accuracy is improved by introducing the features such as: CutMix and Mosaic data augmentation, Class label smoothing, and Mish activation. As a result, our BoFbackbone (Bag of Freebies) for classifier training includes the following: CutMix and Mosaic data augmentation and Class label smoothing. In addition we use Mish activation as a complementary option, as shown in Table 2 and Table 3.

Table 2: Influence of BoF and Mish on the CSPResNeXt-50 classifier accuracy. MixUp CutMix Mosaic Bluring

Table 3: Influence of BoF and Mish on the CSPDarknet-53 classifier accuracy. MixUp CutMix Mosaic Bluring

Further on we study the influence of different backbone models on the detector accuracy, as shown in Table 6. We notice that the model characterized with the best classification accuracy is not always the best in terms of the detector accuracy.

4.5. Influence of different mini-batch size on Detector training Finally, we analyze the results obtained with models trained with different mini-batch sizes, and the results are shown in Table 7. From the results shown in Table 7, we found that after adding BoF and BoS training strategies, the mini-batch size has almost no effect on the detector’s performance. This result shows that after the introduction of BoF and BoS, it is no longer necessary to use expensive GPUs for training. In other words, anyone can use only a conventional GPU to train an excellent detector.

First, although classification accuracy of CSPResNeXt50 models trained with different features is higher compared to CSPDarknet53 models, the CSPDarknet53 model shows higher accuracy in terms of object detection. Second, using BoF and Mish for the CSPResNeXt50 classifier training increases its classification accuracy, but further application of these pre-trained weightings for detector training reduces the detector accuracy. However, using BoF and Mish for the CSPDarknet53 classifier training increases the accuracy of both the classifier and the detector which uses this classifier pre-trained weightings. The net result is that backbone CSPDarknet53 is more suitable for the detector than for CSPResNeXt50.

We observe that the CSPDarknet53 model demonstrates a greater ability to increase the detector accuracy owing to various improvements. 9

Figure 8: Comparison of the speed and accuracy of different object detectors. (Some articles stated the FPS of their detectors for only one of the GPUs: Maxwell/Pascal/Volta)

5. Results

6. Conclusions We offer a state-of-the-art detector which is faster (FPS) and more accurate (MS COCO AP50...95 and AP50 ) than all available alternative detectors. The detector described can be trained and used on a conventional GPU with 8-16 GB-VRAM this makes its broad use possible. The original concept of one-stage anchor-based detectors has proven its viability. We have verified a large number of features, and selected for use such of them for improving the accuracy of both the classifier and the detector. These features can be used as best-practice for future studies and developments.

Comparison of the results obtained with other stateof-the-art object detectors are shown in Figure 8. Our YOLOv4 are located on the Pareto optimality curve and are superior to the fastest and most accurate detectors in terms of both speed and accuracy. Since different methods use GPUs of different architectures for inference time verification, we operate YOLOv4 on commonly adopted GPUs of Maxwell, Pascal, and Volta architectures, and compare them with other state-of-the-art methods. Table 8 lists the frame rate comparison results of using Maxwell GPU, and it can be GTX Titan X (Maxwell) or Tesla M40 GPU. Table 9 lists the frame rate comparison results of using Pascal GPU, and it can be Titan X (Pascal), Titan Xp, GTX 1080 Ti, or Tesla P100 GPU. As for Table 10, it lists the frame rate comparison results of using Volta GPU, and it can be Titan Volta or Tesla V100 GPU.

Table 8: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (testdev 2017). (Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with batch=1 without using tensorRT.) Method

Table 9: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (test-dev 2017). (Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with batch=1 without using tensorRT.) Method

Table 10: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (test-dev 2017). (Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with batch=1 without using tensorRT.) Method
