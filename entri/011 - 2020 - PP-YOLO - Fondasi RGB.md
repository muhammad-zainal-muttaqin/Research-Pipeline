# 011 - PP-YOLO: An Effective and Efficient Implementation of Object Detector

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `long2020ppyolo` |
| Judul asli | PP-YOLO: An Effective and Efficient Implementation of Object Detector |
| Penulis | Xiang Long, Kaipeng Deng, Guanzhong Wang, Yang Zhang, Qingqing Dang, Yuan Gao, Hui Shen, Jianguo Ren, Shumin Han, Errui Ding, Shilei Wen (Baidu Inc) |
| Tahun | 2020 |
| Venue | arXiv preprint arXiv:2007.12099 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.12099
- **Kode sumber (PaddleDetection):** https://github.com/PaddlePaddle/PaddleDetection
- **Google Scholar:** https://scholar.google.com/scholar?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector&sort=relevance

## Gambaran Umum

PP-YOLO adalah detektor objek satu tahap yang dibangun tim Baidu di atas YOLOv3 (bab 003) dengan kerangka kerja PaddlePaddle. Tujuannya secara eksplisit bukan mengusulkan arsitektur baru, melainkan menyusun detektor dengan keseimbangan efektivitas dan efisiensi yang siap dipakai pada aplikasi nyata. Dua perubahan besar dilakukan: *backbone* (jaringan ekstraksi fitur di awal detektor) DarkNet-53 diganti dengan ResNet50-vd yang tahap terakhirnya memakai konvolusi deformable, dan sepuluh trik dari literatur diseleksi satu per satu dengan syarat tidak menaikkan biaya inferensi secara berarti.

Hasil akhirnya pada COCO test-dev adalah 45,2% AP pada kecepatan 72,9 FPS (GPU V100, ukuran masukan 608), mengungguli YOLOv4 yang pada resolusi sama mencapai 43,5% AP pada 62 FPS. Karena kenaikan akurasi diperoleh dari trik yang hampir tidak menambah parameter maupun biaya komputasi, bab ini berfungsi sebagai resep rekayasa: urutan pemasangan trik beserta kontribusi masing-masing dilaporkan terbuka dan dapat ditiru.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada 2020, YOLOv3 telah menjadi detektor yang paling banyak dipakai di industri karena cepat dan mudah dilatih, tetapi akurasinya tertinggal dari detektor dua tahap. YOLOv4 (bab 004), yang terbit beberapa bulan sebelum makalah ini, membuktikan bahwa kumpulan trik pelatihan dan modul murah dapat mengangkat akurasi YOLOv3 secara besar. Namun YOLOv4 memakai backbone CSPDarknet-53 dan menyertakan eksplorasi augmentasi data yang ekstensif, sehingga sebagian resepnya mahal untuk direplikasi.

Dua celah dibiarkan terbuka. Pertama, belum jelas kombinasi trik mana yang efektif bila dipasang berurutan pada YOLOv3, karena trik yang berguna sendirian belum tentu berguna bila digabungkan. Kedua, backbone DarkNet-53 kurang dioptimalkan oleh kerangka kerja pembelajaran mendalam dibandingkan ResNet, padahal pada penerapan nyata kecepatan inferensi sangat ditentukan oleh kualitas optimasi pustaka terhadap jaringan yang dipakai. Masalah yang dipecahkan makalah ini dirumuskan sebagai berikut: bagaimana menyusun detektor praktis yang akurat dan cepat dari komponen yang sudah ada, tanpa merancang arsitektur baru dan tanpa pencarian hiperparameter otomatis (NAS) yang mahal.

## Ide Utama

Gagasan inti PP-YOLO adalah memperlakukan pembangunan detektor sebagai resep rekayasa, bukan sebagai penelitian arsitektur. Titik tolaknya YOLOv3 utuh; backbone-nya ditukar dengan varian ResNet yang lebih didukung pustaka optimasi; kemudian sepuluh trik yang sudah terpublikasi dipasang satu demi satu. Setiap trik hanya diterima bila menaikkan akurasi tanpa menambah jumlah parameter dan FLOPs (jumlah operasi *floating point*, ukuran biaya komputasi model) secara berarti.

Masukannya tetap citra RGB dan keluarannya tetap kisi prediksi YOLOv3. Yang berubah adalah kualitas tiap komponen di sepanjang alur: ekstraksi fitur lebih baik, pelatihan lebih stabil, fungsi loss selaras dengan metrik evaluasi, skor deteksi memperhitungkan ketepatan lokalisasi, dan pasca-pemrosesan berjalan paralel. Karena hampir semua perubahan bekerja saat pelatihan atau menelan biaya di bawah satu milidetik, kecepatan inferensi praktis tidak berkurang.

## Cara Kerja Langkah demi Langkah

### Backbone: ResNet50-vd-dcn

YOLOv3 asli memakai backbone DarkNet-53; PP-YOLO menggantinya dengan ResNet50-vd, varian ResNet-50 berkoneksi sisa (*residual*) yang jalur pintasannya diperhalus saat resolusi diturunkan sehingga informasi tidak hilang. Penggantian langsung ternyata menurunkan akurasi, karena parameter dan FLOPs ResNet50-vd lebih kecil dari DarkNet-53. Sebagai kompensasi, seluruh konvolusi 3×3 pada tahap terakhir diganti konvolusi deformable (DCN, *deformable convolution*): konvolusi yang posisi pencuplikannya digeser oleh offset yang dipelajari, sehingga dapat mengikuti bentuk objek yang tidak beraturan. DCN hanya dipasang pada tahap terakhir karena terlalu banyak DCN memperlambat inferensi. Keluaran tahap 3, 4, dan 5 backbone dinamai C3, C4, C5.

### Neck FPN dan Head YOLOv3

Bagian *neck* (penghubung) memakai FPN (*Feature Pyramid Network*): modul yang menggabungkan peta fitur dalam (kaya makna, miskin detail spasial) dengan peta fitur dangkal (kaya detail) melalui koneksi lateral, menghasilkan piramida fitur tiga tingkat P3, P4, P5. Untuk citra W×H, resolusi Pl adalah W/2^l × H/2^l; pada masukan 608×608, P5 berukuran 19×19 dan P3 berukuran 76×76. *Head* (kepala prediksi) persis milik YOLOv3: satu konvolusi 3×3 diikuti konvolusi 1×1 per skala, dengan keluaran 3(K+5) kanal. Setiap lokasi pada peta keluaran dikaitkan dengan tiga *anchor* (kotak acuan berukuran tetap yang menjadi titik tolak regresi kotak), masing-masing memprediksi K probabilitas kelas, 4 koordinat kotak, dan 1 skor *objectness* (keyakinan adanya objek).

Posisi penyuntikan trik pada arsitektur ditunjukkan diagram berikut:

```
citra masukan (mis. 608x608)
        │
        ▼
┌──────────────────────────┐
│ backbone ResNet50-vd-dcn │  konv 3x3 tahap terakhir = DCN
└───┬────────┬─────────┬───┘
   C5│      C4│       │C3
     ▼        ▼        ▼
┌──────────────────────────┐
│ FPN: P5, P4, P3          │  * SPP hanya di peta teratas
│ (koneksi lateral)        │  ▲ DropBlock hanya di FPN
└───┬────────┬─────────┬───┘  ● CoordConv di konv 1x1 FPN
   P5│      P4│       │P3       dan konv pertama head
     ▼        ▼        ▼
┌──────────────────────────┐
│ head YOLOv3 per skala:   │  konv 3x3 → konv 1x1
│ keluaran 3(K+5) kanal    │  + cabang prediksi IoU
└────────────┬─────────────┘
             ▼
  skor = kelas x objectness x IoU prediksi
             ▼
       Matrix NMS (paralel)
             ▼
        deteksi akhir
```

### Trik Pelatihan: Ukuran Batch, EMA, DropBlock

Tiga trik pertama hanya mengubah cara melatih. Ukuran *batch* (jumlah citra per langkah pembaruan bobot) dinaikkan dari 64 menjadi 192 untuk menstabilkan pelatihan, dengan penyesuaian laju pembelajaran. EMA (*Exponential Moving Average*) memelihara parameter bayangan W_EMA = λW_EMA + (1−λ)W dengan peluruhan λ = 0,9998; evaluasi memakai parameter bayangan yang lebih halus, bukan bobot akhir pelatihan. DropBlock adalah dropout terstruktur yang mematikan satu wilayah bersebelahan pada peta fitur sekaligus, bukan satuan acak; pada PP-YOLO ia hanya dipasang di FPN karena pemasangan di backbone justru menurunkan akurasi.

### Trik Loss dan Skor: IoU Loss, IoU Aware, Grid Sensitive

IoU (*Intersection over Union*) adalah rasio luas irisan terhadap luas gabungan dua kotak, dan menjadi dasar metrik AP. YOLOv3 meregresi kotak dengan loss L1 yang tidak selaras dengan IoU; PP-YOLO menambahkan cabang loss IoU di samping loss L1, bukan menggantinya seperti yang dilakukan YOLOv4. IoU Aware menambah cabang kecil yang memprediksi IoU antara kotak prediksi dan kotak kebenaran; saat inferensi, skor akhir dihitung sebagai probabilitas kelas × objectness × IoU prediksi, sehingga kotak yang posisinya lebih tepat mendapat peringkat lebih tinggi saat penyortiran. Biayanya hanya 0,01% parameter dan 0,0001% FLOPs. Grid Sensitive mengubah dekode pusat kotak dari x = s(gx + σ(px)) menjadi x = s(gx + ασ(px) − (α−1)/2) dengan α = 1,05. Fungsi sigmoid σ bernilai antara 0 dan 1, sehingga bentuk asli tidak pernah menghasilkan pusat tepat pada batas sel: pusat pada batas gx = 3 menuntut σ(px) = 0, yang tidak terjangkau. Rentang baru, yaitu −0,025 sampai 1,025, menutup kedua batas sel; trik ini menambah waktu pasca-pemrosesan hanya sekitar 0,1 milidetik.

### Trik Pasca-Pemrosesan dan Modul Murah: Matrix NMS, CoordConv, SPP

NMS (*Non-Maximum Suppression*) membuang kotak ganda yang saling menutupi dengan menyisakan kotak berskor tertinggi; versi klasiknya berjalan sekuensial, satu kotak demi satu kotak. Matrix NMS, yang dipinjam dari SOLOv2, merumuskan peluruhan skor gaya Soft-NMS sebagai operasi matriks sehingga dapat dieksekusi paralel di GPU dan lebih cepat tanpa kehilangan akurasi. CoordConv menambahkan dua kanal koordinat (posisi x dan y piksel) pada masukan konvolusi agar jaringan dapat mempelajari ketergantungan posisi; ia hanya dipasang pada konvolusi 1×1 di FPN dan konvolusi pertama head, dengan tambahan 0,03 juta parameter dan 0,05 GFLOPs. SPP (*Spatial Pyramid Pooling*) menggabungkan keluaran *max-pooling* berukuran 1, 5, 9, dan 13 pada peta fitur teratas untuk memperluas wilayah penglihatan (*receptive field*); karena kanal masukan konvolusi sesudahnya membesar, trik ini menambah sekitar 1 juta parameter dan 0,36 GFLOPs, atau sekitar 2% parameter dan 1% FLOPs model.

### Model Pralatih yang Lebih Baik

Trik terakhir adalah inisialisasi: backbone diawali dari ResNet50-vd hasil distilasi pada ImageNet — proses di mana model guru yang lebih besar mengajar model kecil — alih-alih bobot pralatih biasa. Karena hanya mengganti titik awal pelatihan, trik ini sama sekali tidak memengaruhi arsitektur maupun biaya inferensi.

## Eksperimen dan Hasil

Seluruh eksperimen dilakukan pada dataset COCO: sekitar 118 ribu citra trainval35k untuk pelatihan, 5 ribu citra minival untuk ablasi, dan sekitar 20 ribu citra test-dev untuk penilaian akhir. Pelatihan memakai SGD selama 250 ribu iterasi pada 8 GPU, laju pembelajaran awal 0,01 yang dibagi sepuluh pada iterasi ke-150 ribu dan ke-200 ribu, pelatihan multi-skala 320–608 piksel, dan augmentasi MixUp (pencampuran dua citra beserta labelnya). Kecepatan diukur pada satu GPU V100 dengan batch 1, tanpa dan dengan TensorRT (pustaka optimasi inferensi NVIDIA).

Ablasi pada minival menunjukkan kontribusi tiap langkah secara berurutan. YOLOv3 dasar (model A) memperoleh 38,9% AP. Penggantian backbone menjadi ResNet50-vd-dcn (B) menghasilkan 39,1% dengan parameter, FLOPs, dan waktu inferensi lebih kecil. Paket strategi pelatihan — batch besar, EMA, DropBlock (C) — melompat ke 41,4%, kenaikan 2,3 poin yang menjadi lompatan terbesar dalam resep ini. Berturut-turut kemudian IoU Loss (D) 41,9%, IoU Aware (E) 42,5%, Grid Sensitive (F) 42,8%, Matrix NMS (G) 43,4%, CoordConv (H) 43,9%, SPP (I) 44,2%, dan model pralatih distilasi (J) 44,5%. Interpretasinya: tidak ada satu trik yang dominan; kenaikan total 5,6 poin dari A ke J adalah akumulasi banyak perbaikan kecil yang masing-masing terverifikasi hampir tidak menaikkan biaya inferensi.

Hasil akhir pada test-dev 2017: pada masukan 608, PP-YOLO mencapai 45,2% AP pada 72,9 FPS tanpa TensorRT dan 155,6 FPS dengan TensorRT. Pada resolusi yang sama YOLOv4 mencapai 43,5% AP pada 62 FPS, sehingga PP-YOLO unggul 1,7 poin AP sekaligus lebih cepat sekitar 18%. EfficientDet-D3 sedikit lebih akurat (45,8%) tetapi hanya berjalan sekitar 34,5 FPS, kurang dari setengah kecepatan PP-YOLO. Seri hasil pada resolusi 320/416/512/608 — dari 39,3% AP pada 132,2 FPS sampai 45,2% AP pada 72,9 FPS — memperlihatkan bahwa pengguna dapat memilih titik kerja sesuai anggaran latensi. Percepatan TensorRT pada PP-YOLO (sekitar 100%) lebih besar daripada pada YOLOv4 (sekitar 70%); menurut penulis, hal ini disebabkan optimasi TensorRT terhadap ResNet lebih matang daripada terhadap Darknet.

## Kelebihan dan Keterbatasan

Kelebihan utama PP-YOLO adalah kepraktisan. Resepnya terbuka per langkah, backbone-nya didukung luas oleh pustaka optimasi, kode dan modelnya dirilis dalam basis kode PaddleDetection, dan kenaikan akurasinya tidak dibayar dengan latensi. Sebagai bukti konsep, makalah ini menunjukkan bahwa seleksi trik yang disiplin dapat mengalahkan desain yang lebih baru pada pertukaran kecepatan-akurasi.

Keterbatasannya bersifat dua lapis. Dari sisi kontribusi, makalah ini murni rekayasa kombinatorik: tidak ada komponen baru, dan penulis sendiri menyatakan trik-trik tersebut tidak independen, sehingga resepnya belum tentu berpindah utuh ke detektor lain. Dari sisi desain, PP-YOLO tetap detektor berbasis anchor dengan kepala YOLOv3; kelemahan pada objek kecil terlihat dari rincian AP objek kecil 26,3% berbanding AP objek besar 57,2% pada konfigurasi 608. Dari sisi rekayasa, implementasi asli terikat pada PaddlePaddle dan pengukuran kecepatan dilakukan pada lingkungan penulis (V100), sehingga angka FPS pembanding sebaiknya dibaca sebagai perbandingan internal, bukan nilai absolut. Selain itu, augmentasi data dan pencarian arsitektur sengaja tidak dieksplorasi, sehingga ruang perbaikan masih terbuka.

## Kaitan dengan Bab Lain

Bab ini mewarisi hampir seluruh kerangka dari [bab 003 (YOLOv3)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md): kisi prediksi tiga skala, anchor, dan bentuk kepala deteksi. Hubungannya dengan [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md) bersifat paralel sekaligus komplementer: keduanya menyusun ulang YOLOv3 dengan kumpulan trik, tetapi PP-YOLO meminjam Grid Sensitive dan SPP dari YOLOv4 sambil memilih jalur backbone ResNet dan himpunan trik yang berbeda. Garis ini berlanjut pada penerus internalnya, PP-YOLOv2 dan PP-YOLOE, yang tidak tercakup dalam entri tinjauan ini. Jalur berbeda diambil [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) yang melepaskan anchor sekaligus memodernisasi penetapan label, sedangkan fondasi formulasi kisi itu sendiri dibahas pada [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `long2020ppyolo`. Ringkasan yang aman dikutip: "PP-YOLO menyusun ulang YOLOv3 di atas backbone ResNet50-vd-dcn dengan sepuluh trik yang hampir tidak menambah parameter dan FLOPs, mencapai 45,2% AP pada COCO test-dev dengan kecepatan 72,9 FPS di V100 — lebih akurat dan lebih cepat dari YOLOv4 pada resolusi yang sama." Seluruh angka berasal dari naskah arXiv versi v3; makalah ini berstatus preprint tanpa tinjauan sejawat. Angka ablasi per trik (seri A sampai J, dari 38,9% ke 44,5% pada minival) dan rincian biaya tiap trik dikutip dari Tabel 1 dan teks naskah; verifikasi ulang ke tabel aslinya disarankan sebelum sitasi formal.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract

50 PP-YOLO (ours) YOLOv4

Object detection is one of the most important areas in computer vision, which plays a key role in various practical scenarios. Due to limitation of hardware, it is often necessary to sacrifice accuracy to ensure the infer speed of the detector in practice. Therefore, the balance between effectiveness and efficiency of object detector must be considered. The goal of this paper is to implement an object detector with relatively balanced effectiveness and efficiency that can be directly applied in actual application scenarios, rather than propose a novel detection model. Considering that YOLOv3 has been widely used in practice, we develop a new object detector based on YOLOv3. We mainly try to combine various existing tricks that almost not increase the number of model parameters and FLOPs, to achieve the goal of improving the accuracy of detector as much as possible while ensuring that the speed is almost unchanged. Since all experiments in this paper are conducted based on PaddlePaddle, we call it PPYOLO. By combining multiple tricks, PP-YOLO can achieve a better balance between effectiveness (45.2% mAP) and efficiency (72.9 FPS), surpassing the existing state-of-theart detectors such as EfficientDet and YOLOv4. Source code is at https://github.com/PaddlePaddle/ PaddleDetection.

Figure 1. Comparison of the proposed PP-YOLO and other stateof-the-art object detectors. PP-YOLO runs faster than YOLOv4 and improves mAP from 43.5% to 45.2%.

them, the network structures of YOLO to YOLOv3 have relatively large changes. YOLOv4 considers various strategies such as bag of freebies and bag of specials on the basis of YOLOv3, which greatly improves the performance of the detector. This paper introduces an improved YOLOv3 model based on PaddlePaddle (PP-YOLO). A bunch of tricks that almost not increase the infer time are added to improve the overall performance of the model. Unlike YOLOv4, we did not explore different backbone networks and data augmentation methods, nor did we use NAS to search for hyperparameters. For the backbone, we directly use the most common ResNet[13] as the backbone of PP-YOLO. For data augmentation, we directly used the most basic MixUp [43]. One reason is that ResNet is used more wildly, such that various deep learning frameworks have deeply optimized for ResNet series, which will be more convenient in actual deployment and will have better infer speed in practical. Another reason is that the replacement of backbone and data augmentation are relatively independent factors, almost irrelevant to the tricks discussed

in this paper. Since there are already a lot of works to study backbone network and to explore data augmentation, we do not repeat them in this paper. Searching for hyperparameters using NAS often consumes more computing power, so there is usually no condition to use NAS to perform a hyperparameter search in each new scenario. Therefore, we still use the manually set parameters following YOLOv3[32]. We believe that using a better backbone network, using more effective data augmentation method and using NAS to search for hyperparameters can further improve the performance of PP-YOLO. The focus of this paper is how to stack some effective tricks that hardly affect efficiency to get better performance. Many of these tricks cannot be directly applied to the network structure of YOLOv3, so small modification is required. Moreover, where to add tricks also needs careful consideration and experiment. This paper is not intended to introduce a novel object detecotor. It is more like a recipe, which tell you how to build a better detector step by step. We have found some tricks that are effective for the YOLOv3 detector, which can save developers’ time of trial and error. The final PP-YOLO model improves the mAP on COCO from 43.5% to 45.2% at a speed faster than YOLOv4. The code and model is released in the PaddleDetection code-base (https://github. com/PaddlePaddle/PaddleDetection).

ization problem, including CornerNet[19], CenterNet[8], ExtremeNet[47] and RepPoint[40]. Breaking the limitation imposed by hand-craft anchors, anchor-free methods show great potential for extreme object scales and aspect ratios [16]. The performance of some recently proposed anchorfree detectors can also compete with state-of-the-art anchorbased detectors. YOLO series detectors [30, 31, 32, 1] have been widely used in practice, due to their excellent effectiveness and efficiency. Until the writing of this paper, it has developed to YOLOv4[1]. YOLOv4 discusses a large number of tricks including many “bag of freebies” which not increase the infer time, and several “bag of specials” that increase the inference cost by a small amount but can significantly improve the accuracy of object detection. YOLOv4 greatly improves the effectiveness and efficiency of the YOLOv3[32]. This paper is also developed based on YOLOv3 model and also explored a lot of tricks. Unlike YOLOV4, we have not explored some widely studied parts such as data augmentation and backbone. Many tricks we discussed in this paper are different from YOLOV4 and the detailed implementation of tricks is also different.

3. Method An one-stage anchor-based detector is normally made up of a backbone network, a detection neck, which is typically a feature pyramid network (FPN), and a detection head for object classification and localization. They are also common components in most of the one-stage anchorfree detectors based on anchor-point. We first revise the detail structure of YOLOv3 and introduce a modified version which replace the backbone to ResNet50-vd-dcn, which is used as the basic baseline in this paper. Then we introduce a bunch of tricks which can improve the performance of YOLOv3 almost without losing efficiency.

3.1. Architecture Backbone The overall architecture of YOLOv3 is shown in Fig. 2. In original YOLOv3[32], DarkNet-53 is first applied to extract feature maps at different scales. Since ResNet[13] has been widely used and and has been studied more extensively, there are more different variants for selection, and it has also been better optimized by deep learning frameworks. So, we replace the original backbone DarkNet-53 with ResNet50-vd in PP-YOLO. Considering directly replace DarkNet-53 with ResNet50-vd will hurt the performance of YOLOv3 detector. We replace some convolutional layers in ResNet50-vd with deformable convolutional layers. The effectiveness of Deformable Convolutional Networks (DCN) has been verified in many detection models. DCN itself will not significantly increase the number of parameters and FLOPs in the model, but in practical

1 Head

Figure 2. The network architecture of YOLOv3 and inject points for PP-YOLO. Activation layers are omitted for brevity. Details are described in Section 3.1 and Section 3.2.

application, too many DCN layers will greatly increase infer time. Therefore, in order to balance the efficiency and effectiveness, we only replace 3 × 3 convolution layers in the last stage with DCNs. We denote this modified backbone as ResNet50-vd-dcn, and the output of stage 3, 4 and 5 as C3 , C4 , C5 . Detection Neck Then the FPN [21] is used to build an feature pyramid with lateral connections between feature maps. Feature maps C3 , C4 , C5 are input to the FPN module. We denote the output feature maps of pyramid level l as Pl , where l = 3, 4, 5 in our experiments. The resolution of Pl is W ×H for an input image of size W × H. The 2l 2l detail structure of FPN is shown in Fig. 2. Detection Head The detection head of YOLOv3 is very simple. It consists of two convolutional layers. A 3 × 3 convolutional followed by an 1 × 1 convolutional layer is adopt to get the final predictions. The output channel of each final prediction is 3(K + 5), where K is number of classes. Each position on each final prediction map has been associate with three different anchors. For each anchor, the first K channels are the prediction of probability for K classes. The following 4 channels are the prediction for bounding box localization. The last channel is the prediction of objectness score. For classification and localization, cross entropy loss and L1 loss is adopt correspondingly. An objectness loss [32] is applied to supervise objectness score, which is used to identify whether is there an object or not.

3.2. Selection of Tricks The various tricks we used in this paper are described in this section. These tricks are all already existing, which coming from different works [10, 1, 42, 39, 38, 25, 12]. This paper does not propose an novel detection method, but just focuses on combining the existing tricks to implement an effective and efficient detector. Because many tricks cannot be applied to YOLOv3 directly, we need to adjust them according to the its structure. Larger Batch Size Using a larger batch size can improve the stability of training and get better results. Here we change the training batch size from 64 to 192, and adjust the training schedule and learning rate accordingly. EMA When training a model, it is often beneficial to maintain moving averages of the trained parameters. Evaluations that use averaged parameters sometimes produce significantly better results than the final trained values [35]. The Exponential Moving Average (EMA) compute the moving averages of trained parameters using exponential decay. For each parameter W , we maintain an shadow parameter WEM A = λWEM A + (1 − λ)W,

where λ is the decay. We apply EMA with decay λ of 0.9998 and use the shadow parameter WEM A for evaluation. DropBlock [10] DropBlock is a form of structured dropout,

where α is set to 1.05 in this paper. This makes it easier for the model to predict bounding box center exactly located on the grid boundary. The FLOPs added by Grid Sensitive is really small, and can be totally ignored. Matrix NMS [38] Matrix NMS is motivated by Soft-NMS, which decays the other detection scores as amonotonic de-

creasing function of their overlaps. However, such process is sequential like traditional Greedy NMS and could not be implemented in parallel. Matrix NMS views this process from another perspective and implement it in a parallel manner. Therefore, the Matrix NMS is faster than traditional NMS, which will not bring any loss of efficiency. CoordConv [25] CoordConv, which works by giving convolution access to its own input coordinates through the use of extra coordinate channels. CoordConv allows networks to learn either complete translation invariance or varying degrees of translation dependence. Considering that CoordConv will add two inputs channels to the convolution layer, some parameters and FLOPs will be added. In order to reduce the loss of efficiency as much as possible, we do not change convolutional layers in backbone, and only replace the 1x1 convolution layer in FPN and the first convolution layer in detection head with CoordConv. The detailed inject points of the CoordConv are marked by ”diamonds” in Figure 2. SPP [12] The Spatial Pyramid Pooling (SPP) is first proposed by He et al[12]. SPP integrates SPM into CNN and use max-pooling operation instead of bag-of-word operation. YOLOv4 apply SPP module by concatenating max-pooling outputs with kernel size k × k, where k = {1, 5, 9, 13}, and stride equals to 1. Under this design, a relatively large k × k max-pooling effectively increase the receptive field of backbone feature. In detail, the SPP only applied on the top feature map as shown in Figure 2 with ”star” mark. No parameter are introduced by SPP itself, but the number of input channel of the following convolutional layer will increase. So around 2% additional papameters and 1% extra FLOPs are introduced. Better Pretrain Model Using a pretrain model with higher classification accuracy on ImageNet may result in better detection performance. Here we use the distilled ResNet50-vd model as the pretrain model [29] . This obviously does not affect the efficiency of the detector.

4. Experiment In this section, we present the effectiveness of different tricks. Experiments were carried out on the bounding box detection track of the COCO dataset [23]. Following the common practice [32, 35, 1], we use trainval35k split for training, which contains ∼118k images, minival split (5k) for validation and ablation study, and test-dev split(∼20k) for testing.

4.1. Implementation Details We use ResNet50-vd-dcn[13] as the backbone networks unless specified. The architecture of FPN and head in our basic models is completely the same as YOLOv3[32]. The details have been presented in section 3.1. We initialize

Table 1. The ablation study of tricks on the MS-COCO minival split.

our detectors following common practice. Specifically, our backbone networks are initialized with the weights pretrained on ImageNet[7]. For the FPN and detection heads, we initialize them randomly as same as in YOLOv3[32]. For the baseline model (A, B), The training schedule is as same as YOLOv3. Under larger batch size setting, the entire network is trained with stochastic gradient descent (SGD) for 250K iterations with the initial learning rate being 0.01 and a minibatch of 192 images distributed on 8 GPUs. The learning rate is divided by 10 at iteration 150K and 200K, respectively. Weight decay is set as 0.0005, and momentum is set as 0.9. Multi-scale training from 320 to 608 pixels is applied. MixUp[43] is adopted for data augmentation.

4.2. Ablation Study In this section, we present the effectiveness of each module in an incremental manner. The reason is that each trick is not completely independent. Some tricks are effective when applied alone, but they are not effective when combined together. Since there are too many combinations of various tricks, it is difficult to conduct a comprehensive analysis. Therefore, we show how to improve the performance of the object detector step by step in the order of our exploration and discovering the effectiveness of tricks. Results are shown in Table 1, where infer time and FPS do not consider the influence of NMS following YOLOv4[1]. A → B First of all, we try to build a basic version of PPYOLO. Because the ResNet[13] series is more widely used, we first replace the original YOLOv3 backbone Darknet53 with ResNet50-vd. However, we found that it will cause a significant decrease in mAP. Considering that the number of parameters and FLOPs of ResNet50-vd are much smaller than those of Darknet53, we replace the 3 × 3 convolutional layer in the last stage of ResNet with deformable convolution layer[6]. In this way, we get a basic PP-YOLO model (B) with a mAP of 39.1%, which is slightly higher than the original YOLOv3 (A), but its parameters, FLOPs and infer time are much smaller than the original YOLOv3 model. B → C We first try to optimize the training strategy. We use

by 0.3% further. After adding these two modules, the infer time has increased by 0.3ms. I → J Replacing the pre-trained model is a very common approach. However, the accuracy of pretrained classification model is higher does not mean that the final detection model is more effective, and the degree of improvement will be affected by the tricks we used. So we consider it at the end. For fair comparisons, we still use ImageNet for pretraining. We use a distilled ResNet50-vd model for backbone initialization. The mAP of PP-YOLO can be further improved by 0.3%. In fact, using other detection datasets for pre-training can greatly improve the performance of the model, but this is beyond the scope of this paper.

ported in official code-base. Compared with other state-of-the-art methods, our PPYOLO has certain advantages in speed and accuracy. For example, compared with YOLOv4, our PPYOLO can increased the mAP on COCO from 43.5% to 45.2% with FPS improved from 62 to 72.9. It is worth noticing that tensorRT accelerates the PP-YOLO model more obviously. The relative improvement of PP-YOLO (around 100%) is larger than YOLOv4(around 70%). We speculate that it is mainly because tensorRT optimizes for ResNet model better than Darknet. In addition, we can get a series of PP-YOLO results by changing the input size of the image. Here we also show the results for 320, 416, 512 and 608 input sizes. Figure 1 shows that PP-YOLO results have advantages in the balance of speed and accuracy compared with other detectors.

5. Conclusions This paper introduce a new implementation of object detector based on PaddlePaddle, called PP-YOLO. PPYOLO is faster (FPS) and more accurate(COCO mAP) than other state-of-the-art detectors, such as EfficientDet and YOLOv4. In this paper, we explore a lot of tricks and show how to combine these tricks on the YOLOv3 detector and demonstrate their effectiveness. We hope this paper can help developers and researchers save exploration time and get better performance in practical applications.
