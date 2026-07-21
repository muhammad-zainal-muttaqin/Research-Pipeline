# 013 - Fast R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `girshick2015fastrcnn` |
| Judul asli | Fast R-CNN |
| Penulis | Ross Girshick |
| Tahun | 2015 |
| Venue | IEEE International Conference on Computer Vision (ICCV 2015) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1504.08083
- **Kode sumber (lisensi MIT, Python/C++ dengan Caffe):** https://github.com/rbgirshick/fast-rcnn
- **Google Scholar:** https://scholar.google.com/scholar?q=Fast%20R-CNN
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Fast%20R-CNN&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Fast R-CNN (*Fast Region-based Convolutional Network*), detektor objek karya Ross Girshick pada ICCV 2015. Gagasan utamanya: peta fitur konvolusi dihitung satu kali untuk seluruh citra, fitur setiap usulan wilayah (*proposal*) diekstrak dari peta itu melalui lapis *RoI pooling*, dan satu jaringan berkepala ganda — klasifikasi *softmax* dan regresi kotak — dilatih dalam satu tahap memakai *multi-task loss*. Rumusan ini menghapus pelatihan tiga tahap dan ekstraksi fitur per proposal yang membuat pendahulunya, R-CNN dan SPPnet, lambat serta boros penyimpanan.

Hasilnya: pelatihan VGG16 sekitar 9 kali lebih cepat daripada R-CNN, pengujian 213 kali lebih cepat, dengan akurasi lebih tinggi — 70,0% mAP pada PASCAL VOC 2007 dengan data latih gabungan, dibandingkan 66,0% pada R-CNN. Arsitektur ini menjadi cetak biru detektor dua tahap berikutnya; Faster R-CNN dan Mask R-CNN dibangun langsung di atasnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, detektor paling akurat adalah R-CNN (dibahas pada [bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md)). R-CNN bekerja dalam dua tahap: algoritme *selective search* mengusulkan sekitar 2.000 kandidat wilayah citra (*region proposal*, potongan segi empat yang mungkin berisi objek), kemudian setiap wilayah diubah ukurannya dan diproses satu per satu oleh jaringan saraf konvolusi (CNN), diklasifikasikan oleh SVM (*support vector machine*, pengklasifikasi yang dilatih terpisah), lalu posisinya diperbaiki regresor kotak.

Makalah ini mencatat tiga kelemahan R-CNN. Pertama, pelatihannya multi-tahap — CNN, SVM, dan regresor dilatih terpisah tanpa saling mengoptimalkan. Kedua, mahal dalam waktu dan ruang: fitur setiap proposal ditulis ke disk, memakan 2,5 hari-GPU untuk 5 ribu citra latih VOC07 dan ratusan gigabita penyimpanan. Ketiga, deteksi lambat: 47 detik per citra dengan VGG16, karena setiap proposal memicu satu *forward pass* CNN tanpa berbagi komputasi.

SPPnet (*Spatial Pyramid Pooling network*) mempercepat R-CNN 10–100 kali dengan menghitung peta fitur konvolusi sekali untuk seluruh citra; fitur tiap proposal diekstrak lewat *spatial pyramid pooling*, pembagian wilayah fitur ke beberapa tingkat kisi tetap yang di-*max-pooling* lalu digabung. Namun SPPnet tetap dilatih multi-tahap, tetap menulis fitur ke disk, dan penyetelan halusnya tidak dapat memperbarui lapis konvolusi di bawah lapis SPP — keterbatasan yang menahan akurasi jaringan dalam, dan menjadi celah yang diisi Fast R-CNN.

## Ide Utama

Gagasan inti Fast R-CNN adalah memindahkan proposal dari ruang piksel ke ruang fitur. Alih-alih memotong dan memproses ulang setiap proposal sebagai citra terpisah, citra utuh dilewatkan melalui lapis konvolusi satu kali; setiap proposal kemudian cukup dibaca dari peta fitur hasilnya. Karena proposal yang tumpang tindih menutupi wilayah citra yang sama, komputasi konvolusi tidak pernah diulang.

Secara mekanis, masukan jaringan adalah satu citra dan daftar proposalnya; keluaran tiap proposal berupa dua hal sekaligus: distribusi probabilitas atas K kelas objek plus satu kelas latar, dan empat angka koreksi kotak untuk setiap kelas. Kedua tugas dilatih bersama dengan satu fungsi loss, sehingga seluruh jaringan — termasuk semua lapis konvolusi — diperbarui dalam satu tahap. Tidak ada lagi SVM terpisah, tidak ada lagi berkas fitur di disk.

## Cara Kerja Langkah demi Langkah

### Arsitektur Keseluruhan

Alur data Fast R-CNN dari masukan ke keluaran digambarkan sebagai berikut:

```
MASUKAN: 1 citra utuh (sisi pendek 600 piksel) + sekitar 2000 proposal

   citra ──> ┌──────────────────────────┐
              │ konvolusi VGG16          │  peta fitur dihitung
              │ 13 conv + 5 max pooling  │  SATU KALI per citra
              └────────────┬─────────────┘
                           v
              peta fitur conv, stride 16
              (citra 600x1000 -> 37x62 x 512 kanal)
                           |
   proposal (r,c,h,w) ──> proyeksi jendela h x w
                           v
              ┌──────────────────────────┐
              │ RoI pooling              │  per proposal:
              │ jendela dibagi grid 7x7, │  fitur ukuran tetap
              │ max pooling tiap sel     │  7x7x512
              └────────────┬─────────────┘
                           v
                fc6 (4096) -> fc7 (4096)
                       ┌───┴───┐
                       v       v
                softmax     regresi kotak:
                K+1 kelas   4 offset per kelas
                (VOC: 21)   (tx, ty, tw, th)
```

Citra masukan diskalakan agar sisi pendeknya 600 piksel (sisi panjang maksimal 1000) — satu skala tunggal, tanpa piramida citra. Pada VGG16, lima lapis *max pooling* (pengambilan nilai maksimum dalam jendela kecil, yang mereduksi resolusi spasial) menghasilkan *stride* total 16, sehingga citra 600×1000 piksel menjadi peta fitur sekitar 37×62 posisi dengan 512 kanal. Setiap proposal dinyatakan sebagai jendela (r, c, h, w) — pojok kiri atas, tinggi, lebar — yang diproyeksikan ke peta fitur ini, lalu diproses seperti pada diagram.

### Lapis RoI Pooling

*RoI pooling* (*Region of Interest pooling*) mengubah jendela fitur berukuran sembarang menjadi fitur berukuran tetap. Jendela h×w dibagi kisi H×W sel (untuk VGG16, H = W = 7), lalu nilai maksimum setiap sel diambil per kanal. Contoh numerik: proposal 256×256 piksel menjadi jendela 16×16 pada peta fitur (karena stride 16); jendela itu dibagi kisi 7×7 sehingga tiap sel mencakup sekitar 2×2 posisi; *max pooling* tiap sel menghasilkan keluaran 7×7 per kanal, atau 7×7×512 — berapa pun ukuran proposal awalnya. Lapis ini adalah kasus khusus *spatial pyramid pooling* dengan satu tingkat piramida. Bedanya dari SPPnet: gradien dialirkan balik menembus lapis ini dengan mengikuti posisi argmax saat *max pooling*, diakumulasikan untuk semua proposal, sehingga lapis konvolusi di bawahnya ikut belajar.

### Inisialisasi dari Jaringan Praterlatih

Fast R-CNN tidak dilatih dari nol. Tiga jaringan ImageNet menjadi titik awal: CaffeNet (varian AlexNet, model S), VGG_CNN_M_1024 (model M), dan VGG16 (model L). Setiap jaringan dimodifikasi tiga kali: lapis *max pooling* terakhir diganti lapis *RoI pooling*; lapis *fully connected* (terhubung penuh) dan *softmax* klasifikasi ImageNet 1000 kelas diganti dua kepala baru — *softmax* K+1 kelas dan regresor kotak per kelas; dan jaringan diubah agar menerima dua masukan, citra dan daftar proposalnya.

### Loss Multi-Tugas

Setiap proposal latih berlabel kelas u (u = 0 untuk latar) dan target regresi v. Loss per proposal adalah L = L_cls + λ·[u ≥ 1]·L_loc. Komponen L_cls adalah *log loss* −log p_u, negatif logaritma probabilitas *softmax* pada kelas benar. Komponen L_loc hanya aktif untuk proposal objek (penanda [u ≥ 1] bernilai 1 bila dipenuhi), menjumlahkan selisih offset prediksi dan target pada keempat koordinat dengan *smooth L1*: fungsi bernilai 0,5x² bila |x| < 1 dan |x| − 0,5 bila tidak. Bentuk kuadrat-linear ini lebih tahan pencilan daripada loss kuadrat milik R-CNN, sehingga gradien tidak mudah meledak. Offset berparameterkan geser skala-invarian untuk pusat dan geser logaritmik untuk lebar-tinggi. Semua eksperimen memakai λ = 1 dengan target dinormalisasi ke rerata nol dan variansi satu.

### Pengambilan Mini-Batch dan Pelatihan

Efisiensi pelatihan berasal dari pengambilan contoh berjenjang. Setiap *mini-batch* SGD (*stochastic gradient descent*) berisi R = 128 proposal dari hanya N = 2 citra, 64 proposal per citra. Proposal secitra berbagi komputasi dan memori pada *forward* dan *backward pass*, sehingga skema ini sekitar 64 kali lebih cepat daripada mengambil satu proposal dari 128 citra berbeda — strategi R-CNN dan SPPnet. Seperempat proposal adalah contoh objek, yaitu yang irisan dengan kotak kebenaran memiliki IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak) minimal 0,5; sisanya contoh latar dengan IoU maksimum antara 0,1 dan 0,5 — batas 0,1 berperan sebagai heuristik penambangan contoh sulit. Augmentasi hanya pembalikan horizontal dengan peluang 0,5. Pelatihan berjalan 30 ribu iterasi dengan laju 0,001, dilanjutkan 10 ribu iterasi dengan 0,0001.

### Deteksi dan Akselerasi SVD

Saat pengujian, sekitar 2.000 proposal per citra dinilai dalam satu *forward pass*, lalu *Non-Maximum Suppression* (NMS — pembuangan kotak ganda yang saling menutupi, mempertahankan yang berskor tertinggi) diterapkan per kelas. Sebanyak 45% waktu *forward pass* deteksi pada VGG16 habis di lapis *fully connected* karena jumlah proposal besar. Makalah ini memangkasnya dengan *truncated SVD*: matriks bobot lapis didekomposisi dan hanya nilai singular teratas yang dipertahankan, sehingga satu lapis besar digantikan dua lapis kecil tanpa non-linearitas. Pada VGG16, lapis fc6 (25088×4096) dipangkas ke 1024 nilai singular dan fc7 (4096×4096) ke 256; waktu deteksi turun lebih dari 30% dengan penurunan mAP hanya 0,3 poin (66,9% menjadi 66,6%), tanpa penyetelan ulang.

## Eksperimen dan Hasil

Evaluasi dilakukan pada PASCAL VOC 2007, 2010, dan 2012 dengan metrik mAP (*mean Average Precision*, rerata presisi di seluruh kelas; maksimal 100%). Semua pengukuran waktu memakai satu GPU Nvidia K40.

Pada VOC 2007 (model L), Fast R-CNN mencapai 66,9% mAP, mengalahkan R-CNN (66,0%) dan SPPnet (63,1%). Selisih 3,8 poin atas SPPnet penting karena dicapai dengan pelatihan satu skala, sedangkan SPPnet memakai lima skala — bukti bahwa menyetel halus lapis konvolusi lebih berharga daripada piramida citra. Dengan data latih digabung (VOC07+VOC12, tiga kali lipat menjadi 16,5 ribu citra), mAP naik menjadi 70,0%. Pada VOC 2010, Fast R-CNN mencapai 68,8% dengan data gabungan, melampaui SegDeepM (67,2%) yang memakai anotasi segmentasi. Pada VOC 2012, skornya 65,7% — teratas di papan peringkat saat itu — dan 68,4% dengan data gabungan, dibandingkan 62,4% untuk R-CNN.

Kecepatan berubah lebih besar lagi. Pelatihan VGG16 turun dari 84 jam (R-CNN) menjadi 9,5 jam; waktu uji turun dari 47,0 detik per citra menjadi 0,32 detik (146 kali) dan menjadi 0,22 detik dengan SVD (213 kali). Terhadap SPPnet, pelatihan 2,7 kali lebih cepat dan pengujian 7–10 kali lebih cepat, sekaligus lebih akurat.

Ablasi menguatkan pilihan desain. Pelatihan multi-tugas menaikkan mAP klasifikasi murni +0,8 hingga +1,1 poin dibanding pelatihan klasifikasi saja, dan mengalahkan pelatihan bertahap. Membekukan lapis konvolusi (hanya lapis *fully connected* yang disetel, meniru SPPnet) menjatuhkan mAP dari 66,9% ke 61,4%; menyetel dari conv3_1 ke atas (9 dari 13 lapis) terbukti cukup. *Softmax* bawaan mengalahkan SVM *post-hoc* sebesar +0,1 hingga +0,8 poin pada ketiga model. Menambah proposal dari 1.000 ke 10.000 tidak menaikkan mAP, dan 45 ribu kotak rapat malah menjatuhkannya ke 52,9% — proposal *selective search* yang jarang berperan sebagai kaskade penyaring yang menguntungkan. Sebagai baseline awal di MS COCO, Fast R-CNN memperoleh 35,9% mAP gaya PASCAL dan 19,7% AP gaya COCO yang juga direrata atas ambang IoU — jauh di bawah angka VOC, menggambarkan ketatnya metrik baru tersebut.

## Kelebihan dan Keterbatasan

Kelebihan utama Fast R-CNN adalah penyederhanaan menyeluruh: satu tahap pelatihan menggantikan tiga, semua lapis ikut diperbarui, ratusan gigabita cache fitur di disk hilang, dan akurasi justru naik. Kecepatannya membuat eksperimen yang sebelumnya mahal menjadi praktis, dan kode sumbernya dirilis dengan lisensi MIT.

Keterbatasannya berlapis. Pertama, proposal tetap dari algoritme eksternal yang tidak dilatih; angka 0,32 detik per citra secara eksplisit tidak memasukkan waktu pembangkitan proposal, sehingga dari sisi rekayasa tahap inilah hambatan berikutnya. Kedua, model terbesar tidak dapat memakai multi-skala karena keterbatasan memori GPU saat itu. Ketiga, secara konseptual, komputasi lapis *fully connected* tetap diulang untuk setiap proposal, termasuk yang saling tumpang tindih. Keempat, laju sekitar 3–5 citra per detik masih jauh dari *real-time*.

## Kaitan dengan Bab Lain

Bab ini adalah kelanjutan langsung [bab 012 (R-CNN)](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md): kerangka proposal–CNN–klasifikasi dipertahankan, tetapi struktur pelatihannya diganti total. Dari SPPnet dipinjam gagasan berbagi peta fitur; kontribusi bab ini adalah membuatnya dapat dilatih penuh. Keterbatasan proposal eksternal yang tersisa dijawab [bab 014 (Faster R-CNN)](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md), yang mengganti *selective search* dengan jaringan pengusul wilayah yang dilatih bersama detektor. [Bab 017 (Mask R-CNN)](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md) kemudian memperhalus *RoI pooling* menjadi *RoIAlign* demi segmentasi instans. Di arah berlawanan, [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) membuang proposal sama sekali demi kecepatan; perbandingannya dengan Fast R-CNN pada VOC 2007 (63,4% mAP pada 45 FPS melawan 70,0% pada sekitar 3 FPS) menjadi titik tolak perdebatan satu tahap versus dua tahap yang membingkai klaster Fondasi RGB.

## Poin untuk Sitasi

Kutip dengan kunci `girshick2015fastrcnn`. Ringkasan yang aman dikutip: "Fast R-CNN menghitung peta fitur konvolusi satu kali untuk seluruh citra dan mengekstrak fitur setiap proposal melalui RoI pooling, lalu melatih klasifikasi softmax dan regresi kotak bersama dalam satu tahap; pelatihan VGG16 sekitar 9 kali lebih cepat dari R-CNN, pengujian hingga 213 kali lebih cepat, dengan mAP lebih tinggi pada PASCAL VOC." Seluruh angka pada bab ini diverifikasi terhadap teks lengkap arXiv:1504.08083, versi yang dinyatakan tampil di ICCV 2015. Dua catatan sebelum sitasi formal: angka "66% lawan 62%" pada pendahuluan makalah adalah pembulatan dari 65,7% lawan 62,4% pada VOC 2012 tanpa data tambahan; dan hasil MS COCO (35,9% dan 19,7%) dinyatakan penulis sebagai baseline awal, bukan hasil akhir.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract This paper proposes a Fast Region-based Convolutional Network method (Fast R-CNN) for object detection. Fast R-CNN builds on previous work to efficiently classify object proposals using deep convolutional networks. Compared to previous work, Fast R-CNN employs several innovations to improve training and testing speed while also increasing detection accuracy. Fast R-CNN trains the very deep VGG16 network 9× faster than R-CNN, is 213× faster at test-time, and achieves a higher mAP on PASCAL VOC 2012. Compared to SPPnet, Fast R-CNN trains VGG16 3× faster, tests 10× faster, and is more accurate. Fast R-CNN is implemented in Python and C++ (using Caffe) and is available under the open-source MIT License at https: //github.com/rbgirshick/fast-rcnn.

1. Introduction Recently, deep ConvNets [14, 16] have significantly improved image classification [14] and object detection [9, 19] accuracy. Compared to image classification, object detection is a more challenging task that requires more complex methods to solve. Due to this complexity, current approaches (e.g., [9, 11, 19, 25]) train models in multi-stage pipelines that are slow and inelegant. Complexity arises because detection requires the accurate localization of objects, creating two primary challenges. First, numerous candidate object locations (often called “proposals”) must be processed. Second, these candidates provide only rough localization that must be refined to achieve precise localization. Solutions to these problems often compromise speed, accuracy, or simplicity. In this paper, we streamline the training process for stateof-the-art ConvNet-based object detectors [9, 11]. We propose a single-stage training algorithm that jointly learns to classify object proposals and refine their spatial locations. The resulting method can train a very deep detection network (VGG16 [20]) 9× faster than R-CNN [9] and 3× faster than SPPnet [11]. At runtime, the detection network processes images in 0.3s (excluding object proposal time)

1.1. R-CNN and SPPnet The Region-based Convolutional Network method (RCNN) [9] achieves excellent object detection accuracy by using a deep ConvNet to classify object proposals. R-CNN, however, has notable drawbacks: 1. Training is a multi-stage pipeline. R-CNN first finetunes a ConvNet on object proposals using log loss. Then, it fits SVMs to ConvNet features. These SVMs act as object detectors, replacing the softmax classifier learnt by fine-tuning. In the third training stage, bounding-box regressors are learned. 2. Training is expensive in space and time. For SVM and bounding-box regressor training, features are extracted from each object proposal in each image and written to disk. With very deep networks, such as VGG16, this process takes 2.5 GPU-days for the 5k images of the VOC07 trainval set. These features require hundreds of gigabytes of storage. 3. Object detection is slow. At test-time, features are extracted from each object proposal in each test image. Detection with VGG16 takes 47s / image (on a GPU). R-CNN is slow because it performs a ConvNet forward pass for each object proposal, without sharing computation. Spatial pyramid pooling networks (SPPnets) [11] were proposed to speed up R-CNN by sharing computation. The SPPnet method computes a convolutional feature map for the entire input image and then classifies each object proposal using a feature vector extracted from the shared feature map. Features are extracted for a proposal by maxpooling the portion of the feature map inside the proposal into a fixed-size output (e.g., 6 × 6). Multiple output sizes are pooled and then concatenated as in spatial pyramid pooling [15]. SPPnet accelerates R-CNN by 10 to 100× at test time. Training time is also reduced by 3× due to faster proposal feature extraction. 1 All timings use one Nvidia K40 GPU overclocked to 875 MHz.

SPPnet also has notable drawbacks. Like R-CNN, training is a multi-stage pipeline that involves extracting features, fine-tuning a network with log loss, training SVMs, and finally fitting bounding-box regressors. Features are also written to disk. But unlike R-CNN, the fine-tuning algorithm proposed in [11] cannot update the convolutional layers that precede the spatial pyramid pooling. Unsurprisingly, this limitation (fixed convolutional layers) limits the accuracy of very deep networks.

1.2. Contributions We propose a new training algorithm that fixes the disadvantages of R-CNN and SPPnet, while improving on their speed and accuracy. We call this method Fast R-CNN because it’s comparatively fast to train and test. The Fast RCNN method has several advantages: 1. Higher detection quality (mAP) than R-CNN, SPPnet 2. Training is single-stage, using a multi-task loss 3. Training can update all network layers 4. No disk storage is required for feature caching Fast R-CNN is written in Python and C++ (Caffe [13]) and is available under the open-source MIT License at https://github.com/rbgirshick/ fast-rcnn.

Figure 1. Fast R-CNN architecture. An input image and multiple regions of interest (RoIs) are input into a fully convolutional network. Each RoI is pooled into a fixed-size feature map and then mapped to a feature vector by fully connected layers (FCs). The network has two output vectors per RoI: softmax probabilities and per-class bounding-box regression offsets. The architecture is trained end-to-end with a multi-task loss.

RoI max pooling works by dividing the h × w RoI window into an H × W grid of sub-windows of approximate size h/H × w/W and then max-pooling the values in each sub-window into the corresponding output grid cell. Pooling is applied independently to each feature map channel, as in standard max pooling. The RoI layer is simply the special-case of the spatial pyramid pooling layer used in SPPnets [11] in which there is only one pyramid level. We use the pooling sub-window calculation given in [11].

2.2. Initializing from pre-trained networks

Fig. 1 illustrates the Fast R-CNN architecture. A Fast R-CNN network takes as input an entire image and a set of object proposals. The network first processes the whole image with several convolutional (conv) and max pooling layers to produce a conv feature map. Then, for each object proposal a region of interest (RoI) pooling layer extracts a fixed-length feature vector from the feature map. Each feature vector is fed into a sequence of fully connected (fc) layers that finally branch into two sibling output layers: one that produces softmax probability estimates over K object classes plus a catch-all “background” class and another layer that outputs four real-valued numbers for each of the K object classes. Each set of 4 values encodes refined bounding-box positions for one of the K classes.

We experiment with three pre-trained ImageNet [4] networks, each with five max pooling layers and between five and thirteen conv layers (see Section 4.1 for network details). When a pre-trained network initializes a Fast R-CNN network, it undergoes three transformations. First, the last max pooling layer is replaced by a RoI pooling layer that is configured by setting H and W to be compatible with the net’s first fully connected layer (e.g., H = W = 7 for VGG16). Second, the network’s last fully connected layer and softmax (which were trained for 1000-way ImageNet classification) are replaced with the two sibling layers described earlier (a fully connected layer and softmax over K + 1 categories and category-specific bounding-box regressors). Third, the network is modified to take two data inputs: a list of images and a list of RoIs in those images.

2.1. The RoI pooling layer

2.3. Fine-tuning for detection

The RoI pooling layer uses max pooling to convert the features inside any valid region of interest into a small feature map with a fixed spatial extent of H × W (e.g., 7 × 7), where H and W are layer hyper-parameters that are independent of any particular RoI. In this paper, an RoI is a rectangular window into a conv feature map. Each RoI is defined by a four-tuple (r, c, h, w) that specifies its top-left corner (r, c) and its height and width (h, w).

Training all network weights with back-propagation is an important capability of Fast R-CNN. First, let’s elucidate why SPPnet is unable to update weights below the spatial pyramid pooling layer. The root cause is that back-propagation through the SPP layer is highly inefficient when each training sample (i.e. RoI) comes from a different image, which is exactly how R-CNN and SPPnet networks are trained. The inefficiency

2. Fast R-CNN architecture and training

stems from the fact that each RoI may have a very large receptive field, often spanning the entire input image. Since the forward pass must process the entire receptive field, the training inputs are large (often the entire image). We propose a more efficient training method that takes advantage of feature sharing during training. In Fast RCNN training, stochastic gradient descent (SGD) minibatches are sampled hierarchically, first by sampling N images and then by sampling R/N RoIs from each image. Critically, RoIs from the same image share computation and memory in the forward and backward passes. Making N small decreases mini-batch computation. For example, when using N = 2 and R = 128, the proposed training scheme is roughly 64× faster than sampling one RoI from 128 different images (i.e., the R-CNN and SPPnet strategy). One concern over this strategy is it may cause slow training convergence because RoIs from the same image are correlated. This concern does not appear to be a practical issue and we achieve good results with N = 2 and R = 128 using fewer SGD iterations than R-CNN. In addition to hierarchical sampling, Fast R-CNN uses a streamlined training process with one fine-tuning stage that jointly optimizes a softmax classifier and bounding-box regressors, rather than training a softmax classifier, SVMs, and regressors in three separate stages [9, 11]. The components of this procedure (the loss, mini-batch sampling strategy, back-propagation through RoI pooling layers, and SGD hyper-parameters) are described below. Multi-task loss. A Fast R-CNN network has two sibling output layers. The first outputs a discrete probability distribution (per RoI), p = (p0 , . . . , pK ), over K + 1 categories. As usual, p is computed by a softmax over the K +1 outputs of a fully connected layer. The second sibling layer outputs

bounding box and hence Lloc is ignored. For bounding-box regression, we use the loss X Lloc (tu , v) = smoothL1 (tui − vi ), (2) i∈{x,y,w,h}

is a robust L1 loss that is less sensitive to outliers than the L2 loss used in R-CNN and SPPnet. When the regression targets are unbounded, training with L2 loss can require careful tuning of learning rates in order to prevent exploding gradients. Eq. 3 eliminates this sensitivity. The hyper-parameter λ in Eq. 1 controls the balance between the two task losses. We normalize the ground-truth regression targets vi to have zero mean and unit variance. All experiments use λ = 1. We note that [6] uses a related loss to train a classagnostic object proposal network. Different from our approach, [6] advocates for a two-network system that separates localization and classification. OverFeat [19], R-CNN [9], and SPPnet [11] also train classifiers and bounding-box localizers, however these methods use stage-wise training, which we show is suboptimal for Fast R-CNN (Section 5.1). Mini-batch sampling. During fine-tuning, each SGD mini-batch is constructed from N = 2 images, chosen uniformly at random (as is common practice, we actually iterate over permutations of the dataset). We use mini-batches of size R = 128, sampling 64 RoIs from each image. As in [9], we take 25% of the RoIs from object proposals that have intersection over union (IoU) overlap with a groundtruth bounding box of at least 0.5. These RoIs comprise the examples labeled with a foreground object class, i.e. u ≥ 1. The remaining RoIs are sampled from object proposals that have a maximum IoU with ground truth in the interval [0.1, 0.5), following [11]. These are the background examples and are labeled with u = 0. The lower threshold of 0.1 appears to act as a heuristic for hard example mining [8]. During training, images are horizontally flipped with probability 0.5. No other data augmentation is used. Back-propagation through RoI pooling layers. Backpropagation routes derivatives through the RoI pooling layer. For clarity, we assume only one image per mini-batch (N = 1), though the extension to N > 1 is straightforward because the forward pass treats all images independently. Let xi ∈ R be the i-th activation input into the RoI pooling layer and let yrj be the layer’s j-th output from the rth RoI. The RoI pooling layer computes yrj = xi∗ (r,j) , in which i∗ (r, j) = argmaxi0 ∈R(r,j) xi0 . R(r, j) is the index

set of inputs in the sub-window over which the output unit yrj max pools. A single xi may be assigned to several different outputs yrj . The RoI pooling layer’s backwards function computes partial derivative of the loss function with respect to each input variable xi by following the argmax switches: XX ∂L ∂L = [i = i∗ (r, j)] . ∂xi ∂y rj r j

In words, for each mini-batch RoI r and for each pooling output unit yrj , the partial derivative ∂L/∂yrj is accumulated if i is the argmax selected for yrj by max pooling. In back-propagation, the partial derivatives ∂L/∂yrj are already computed by the backwards function of the layer on top of the RoI pooling layer. SGD hyper-parameters. The fully connected layers used for softmax classification and bounding-box regression are initialized from zero-mean Gaussian distributions with standard deviations 0.01 and 0.001, respectively. Biases are initialized to 0. All layers use a per-layer learning rate of 1 for weights and 2 for biases and a global learning rate of 0.001. When training on VOC07 or VOC12 trainval we run SGD for 30k mini-batch iterations, and then lower the learning rate to 0.0001 and train for another 10k iterations. When we train on larger datasets, we run SGD for more iterations, as described later. A momentum of 0.9 and parameter decay of 0.0005 (on weights and biases) are used.

2.4. Scale invariance We explore two ways of achieving scale invariant object detection: (1) via “brute force” learning and (2) by using image pyramids. These strategies follow the two approaches in [11]. In the brute-force approach, each image is processed at a pre-defined pixel size during both training and testing. The network must directly learn scale-invariant object detection from the training data. The multi-scale approach, in contrast, provides approximate scale-invariance to the network through an image pyramid. At test-time, the image pyramid is used to approximately scale-normalize each object proposal. During multi-scale training, we randomly sample a pyramid scale each time an image is sampled, following [11], as a form of data augmentation. We experiment with multi-scale training for smaller networks only, due to GPU memory limits.

3.1. Truncated SVD for faster detection For whole-image classification, the time spent computing the fully connected layers is small compared to the conv layers. On the contrary, for detection the number of RoIs to process is large and nearly half of the forward pass time is spent computing the fully connected layers (see Fig. 2). Large fully connected layers are easily accelerated by compressing them with truncated SVD [5, 23]. In this technique, a layer parameterized by the u × v weight matrix W is approximately factorized as W ≈ U Σt V T

3. Fast R-CNN detection Once a Fast R-CNN network is fine-tuned, detection amounts to little more than running a forward pass (assuming object proposals are pre-computed). The network takes as input an image (or an image pyramid, encoded as a list of images) and a list of R object proposals to score. At

method †

Table 1. VOC 2007 test detection average precision (%). All methods use VGG16. Training set key: 07: VOC07 trainval, 07 \ diff: 07 without “difficult” examples, 07+12: union of 07 and VOC12 trainval. † SPPnet results were prepared by the authors of [11].

method

Table 2. VOC 2010 test detection average precision (%). BabyLearning uses a network based on [17]. All other methods use VGG16. Training set key: 12: VOC12 trainval, Prop.: proprietary dataset, 12+seg: 12 with segmentation annotations, 07++12: union of VOC07 trainval, VOC07 test, and VOC12 trainval. method

to this CaffeNet as model S, for “small.” The second network is VGG CNN M 1024 from [3], which has the same depth as S, but is wider. We call this network model M, for “medium.” The final network is the very deep VGG16 model from [20]. Since this model is the largest, we call it model L. In this section, all experiments use single-scale training and testing (s = 600; see Section 5.2 for details).

4.2. VOC 2010 and 2012 results On these datasets, we compare Fast R-CNN (FRCN, for short) against the top methods on the comp4 (outside data) track from the public leaderboard (Table 2, Table 3).3 For the NUS NIN c2000 and BabyLearning methods, there are no associated publications at this time and we could not find exact information on the ConvNet architectures used; they are variants of the Network-in-Network design [17]. All other methods are initialized from the same pre-trained VGG16 network. Fast R-CNN achieves the top result on VOC12 with a mAP of 65.7% (and 68.4% with extra data). It is also two orders of magnitude faster than the other methods, which are all based on the “slow” R-CNN pipeline. On VOC10, 3 http://host.robots.ox.ac.uk:8080/leaderboard (accessed April 18, 2015)

SegDeepM [25] achieves a higher mAP than Fast R-CNN (67.2% vs. 66.1%). SegDeepM is trained on VOC12 trainval plus segmentation annotations; it is designed to boost R-CNN accuracy by using a Markov random field to reason over R-CNN detections and segmentations from the O2 P [1] semantic-segmentation method. Fast R-CNN can be swapped into SegDeepM in place of R-CNN, which may lead to better results. When using the enlarged 07++12 training set (see Table 2 caption), Fast R-CNN’s mAP increases to 68.8%, surpassing SegDeepM.

4.3. VOC 2007 results On VOC07, we compare Fast R-CNN to R-CNN and SPPnet. All methods start from the same pre-trained VGG16 network and use bounding-box regression. The VGG16 SPPnet results were computed by the authors of [11]. SPPnet uses five scales during both training and testing. The improvement of Fast R-CNN over SPPnet illustrates that even though Fast R-CNN uses single-scale training and testing, fine-tuning the conv layers provides a large improvement in mAP (from 63.1% to 66.9%). R-CNN achieves a mAP of 66.0%. As a minor point, SPPnet was trained without examples marked as “difficult” in PASCAL. Removing these examples improves Fast R-CNN mAP to 68.1%. All other experiments use “difficult” examples.

4.4. Training and testing time

4.5. Which layers to fine-tune?

Fast training and testing times are our second main result. Table 4 compares training time (hours), testing rate (seconds per image), and mAP on VOC07 between Fast RCNN, R-CNN, and SPPnet. For VGG16, Fast R-CNN processes images 146× faster than R-CNN without truncated SVD and 213× faster with it. Training time is reduced by 9×, from 84 hours to 9.5. Compared to SPPnet, Fast RCNN trains VGG16 2.7× faster (in 9.5 vs. 25.5 hours) and tests 7× faster without truncated SVD or 10× faster with it. Fast R-CNN also eliminates hundreds of gigabytes of disk storage, because it does not cache features.

For the less deep networks considered in the SPPnet paper [11], fine-tuning only the fully connected layers appeared to be sufficient for good accuracy. We hypothesized that this result would not hold for very deep networks. To validate that fine-tuning the conv layers is important for VGG16, we use Fast R-CNN to fine-tune, but freeze the thirteen conv layers so that only the fully connected layers learn. This ablation emulates single-scale SPPnet training and decreases mAP from 66.9% to 61.4% (Table 5). This experiment verifies our hypothesis: training through the RoI pooling layer is important for very deep nets.

Table 4. Runtime comparison between the same models in Fast RCNN, R-CNN, and SPPnet. Fast R-CNN uses single-scale mode. SPPnet uses the five scales specified in [11]. † Timing provided by the authors of [11]. Times were measured on an Nvidia K40 GPU.

Truncated SVD. Truncated SVD can reduce detection time by more than 30% with only a small (0.3 percentage point) drop in mAP and without needing to perform additional fine-tuning after model compression. Fig. 2 illustrates how using the top 1024 singular values from the 25088 × 4096 matrix in VGG16’s fc6 layer and the top 256 singular values from the 4096 × 4096 fc7 layer reduces runtime with little loss in mAP. Further speed-ups are possible with smaller drops in mAP if one fine-tunes again after compression.

Figure 2. Timing for VGG16 before and after truncated SVD. Before SVD, fully connected layers fc6 and fc7 take 45% of the time.

layers that are fine-tuned in model L SPPnet L ≥ fc6 ≥ conv3 1 ≥ conv2 1 ≥ fc6 VOC07 mAP 61.4 66.9 67.2 63.1 test rate (s/im) 0.32 0.32 0.32 2.3 Table 5. Effect of restricting which layers are fine-tuned for VGG16. Fine-tuning ≥ fc6 emulates the SPPnet training algorithm [11], but using a single scale. SPPnet L results were obtained using five scales, at a significant (7×) speed cost.

Does this mean that all conv layers should be fine-tuned? In short, no. In the smaller networks (S and M) we find that conv1 is generic and task independent (a well-known fact [14]). Allowing conv1 to learn, or not, has no meaningful effect on mAP. For VGG16, we found it only necessary to update layers from conv3 1 and up (9 of the 13 conv layers). This observation is pragmatic: (1) updating from conv2 1 slows training by 1.3× (12.5 vs. 9.5 hours) compared to learning from conv3 1; and (2) updating from conv1 1 over-runs GPU memory. The difference in mAP when learning from conv2 1 up was only +0.3 points (Table 5, last column). All Fast R-CNN results in this paper using VGG16 fine-tune layers conv3 1 and up; all experiments with models S and M fine-tune layers conv2 and up.

5. Design evaluation We conducted experiments to understand how Fast RCNN compares to R-CNN and SPPnet, as well as to evaluate design decisions. Following best practices, we performed these experiments on the PASCAL VOC07 dataset.

5.1. Does multi-task training help? Multi-task training is convenient because it avoids managing a pipeline of sequentially-trained tasks. But it also has the potential to improve results because the tasks influence each other through a shared representation (the ConvNet) [2]. Does multi-task training improve object detection accuracy in Fast R-CNN? To test this question, we train baseline networks that use only the classification loss, Lcls , in Eq. 1 (i.e., setting

λ = 0). These baselines are printed for models S, M, and L in the first column of each group in Table 6. Note that these models do not have bounding-box regressors. Next (second column per group), we take networks that were trained with the multi-task loss (Eq. 1, λ = 1), but we disable boundingbox regression at test time. This isolates the networks’ classification accuracy and allows an apples-to-apples comparison with the baseline networks. Across all three networks we observe that multi-task training improves pure classification accuracy relative to training for classification alone. The improvement ranges from +0.8 to +1.1 mAP points, showing a consistent positive effect from multi-task learning. Finally, we take the baseline models (trained with only the classification loss), tack on the bounding-box regression layer, and train them with Lloc while keeping all other network parameters frozen. The third column in each group shows the results of this stage-wise training scheme: mAP improves over column one, but stage-wise training underperforms multi-task training (forth column per group).

5.2. Scale invariance: to brute force or finesse? We compare two strategies for achieving scale-invariant object detection: brute-force learning (single scale) and image pyramids (multi-scale). In either case, we define the scale s of an image to be the length of its shortest side. All single-scale experiments use s = 600 pixels; s may be less than 600 for some images as we cap the longest image side at 1000 pixels and maintain the image’s aspect ratio. These values were selected so that VGG16 fits in GPU memory during fine-tuning. The smaller models are not memory bound and can benefit from larger values of s; however, optimizing s for each model is not our main concern. We note that PASCAL images are 384 × 473 pixels on average and thus the single-scale setting typically upsamples images by a factor of 1.6. The average effective stride at the RoI pooling layer is thus ≈ 10 pixels. In the multi-scale setting, we use the same five scales specified in [11] (s ∈ {480, 576, 688, 864, 1200}) to facilitate comparison with SPPnet. However, we cap the longest side at 2000 pixels to avoid exceeding GPU memory. Table 7 shows models S and M when trained and tested with either one or five scales. Perhaps the most surprising result in [11] was that single-scale detection performs almost as well as multi-scale detection. Our findings con-

Table 7. Multi-scale vs. single scale. SPPnet ZF (similar to model S) results are from [11]. Larger networks with a single-scale offer the best speed / accuracy tradeoff. (L cannot use multi-scale in our implementation due to GPU memory constraints.)

firm their result: deep ConvNets are adept at directly learning scale invariance. The multi-scale approach offers only a small increase in mAP at a large cost in compute time (Table 7). In the case of VGG16 (model L), we are limited to using a single scale by implementation details. Yet it achieves a mAP of 66.9%, which is slightly higher than the 66.0% reported for R-CNN [10], even though R-CNN uses “infinite” scales in the sense that each proposal is warped to a canonical size. Since single-scale processing offers the best tradeoff between speed and accuracy, especially for very deep models, all experiments outside of this sub-section use single-scale training and testing with s = 600 pixels.

5.3. Do we need more training data? A good object detector should improve when supplied with more training data. Zhu et al. [24] found that DPM [8] mAP saturates after only a few hundred to thousand training examples. Here we augment the VOC07 trainval set with the VOC12 trainval set, roughly tripling the number of images to 16.5k, to evaluate Fast R-CNN. Enlarging the training set improves mAP on VOC07 test from 66.9% to 70.0% (Table 1). When training on this dataset we use 60k mini-batch iterations instead of 40k. We perform similar experiments for VOC10 and 2012, for which we construct a dataset of 21.5k images from the union of VOC07 trainval, test, and VOC12 trainval. When training on this dataset, we use 100k SGD iterations and lower the learning rate by 0.1× each 40k iterations (instead of each 30k). For VOC10 and 2012, mAP improves from 66.1% to 68.8% and from 65.7% to 68.4%, respectively.

post-hoc, as was done in R-CNN and SPPnet. To understand the impact of this choice, we implemented post-hoc SVM training with hard negative mining in Fast R-CNN. We use the same training algorithm and hyper-parameters as in R-CNN. method R-CNN [9, 10] FRCN [ours] FRCN [ours]

Table 8. Fast R-CNN with softmax vs. SVM (VOC07 mAP).

Table 8 shows softmax slightly outperforming SVM for all three networks, by +0.1 to +0.8 mAP points. This effect is small, but it demonstrates that “one-shot” fine-tuning is sufficient compared to previous multi-stage training approaches. We note that softmax, unlike one-vs-rest SVMs, introduces competition between classes when scoring a RoI.

5.5. Are more proposals always better? There are (broadly) two types of object detectors: those that use a sparse set of object proposals (e.g., selective search [21]) and those that use a dense set (e.g., DPM [8]). Classifying sparse proposals is a type of cascade [22] in which the proposal mechanism first rejects a vast number of candidates leaving the classifier with a small set to evaluate. This cascade improves detection accuracy when applied to DPM detections [21]. We find evidence that the proposalclassifier cascade also improves Fast R-CNN accuracy. Using selective search’s quality mode, we sweep from 1k to 10k proposals per image, each time re-training and retesting model M. If proposals serve a purely computational role, increasing the number of proposals per image should not harm mAP. 66

Figure 3. VOC07 test mAP and AR for various proposal schemes.

We find that mAP rises and then falls slightly as the proposal count increases (Fig. 3, solid blue line). This experiment shows that swamping the deep classifier with more proposals does not help, and even slightly hurts, accuracy.

5.6. Preliminary MS COCO results We applied Fast R-CNN (with VGG16) to the MS COCO dataset [18] to establish a preliminary baseline. We trained on the 80k image training set for 240k iterations and evaluated on the “test-dev” set using the evaluation server. The PASCAL-style mAP is 35.9%; the new COCO-style AP, which also averages over IoU thresholds, is 19.7%.

6. Conclusion This paper proposes Fast R-CNN, a clean and fast update to R-CNN and SPPnet. In addition to reporting state-of-theart detection results, we present detailed experiments that we hope provide new insights. Of particular note, sparse object proposals appear to improve detector quality. This issue was too costly (in time) to probe in the past, but becomes practical with Fast R-CNN. Of course, there may exist yet undiscovered techniques that allow dense boxes to perform as well as sparse proposals. Such methods, if developed, may help further accelerate object detection. Acknowledgements. I thank Kaiming He, Larry Zitnick, and Piotr Dollár for helpful discussions and encouragement.
