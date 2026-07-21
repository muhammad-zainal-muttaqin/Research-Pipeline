# 137 - TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2021tphyolov5` |
| Judul asli | TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios |
| Penulis | Zhu, Xingkui; Lyu, Shuchang; Wang, Xu; Zhao, Qi |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) |
| Tema | Remote Sensing |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios&sort=relevance

## Gambaran Umum
TPH-YOLOv5 merupakan model deteksi objek satu tahap (*one-stage detector*) yang dirancang khusus untuk menganalisis citra hasil tangkapan wahana udara tanpa awak (*unmanned aerial vehicle* / UAV) atau drone. Model ini dikembangkan untuk memecahkan tantangan khas pada citra udara, seperti ukuran objek yang sangat kecil (hanya beberapa piksel), kepadatan objek yang tinggi, variasi skala ekstrem, serta latar belakang yang bising dan kompleks. Melalui integrasi modul *Transformer Prediction Head* (TPH) dan *Convolutional Block Attention Module* (CBAM) ke dalam kerangka dasar YOLOv5, model ini mampu mengekstraksi informasi konteks global secara efektif.

Penerapan modifikasi tersebut memberikan peningkatan akurasi deteksi yang signifikan dibandingkan model YOLOv5 standar. Pada ajang kompetisi VisDrone Challenge 2021, model ini berhasil menempati peringkat kelima pada kategori deteksi objek dengan nilai *mean Average Precision* (mAP) sebesar 39,18%. Keberhasilan ini membuktikan bahwa integrasi mekanisme perhatian (*attention mechanism*) dan pemrosesan berbasis *Transformer* dapat menutupi kelemahan detektor konvensional pada skenario penginderaan jauh (*remote sensing*) udara.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi objek pada citra yang diperoleh dari platform UAV menghadapi kendala geometris dan radiometris yang tidak ditemukan pada citra perspektif horizontal biasa. Objek target seperti pejalan kaki atau kendaraan sering kali hanya berukuran di bawah $10 \times 10$ piksel dan berkumpul dalam kepadatan ekstrem di area perkotaan. Akibat ketinggian terbang drone yang dinamis, ukuran objek yang sama dapat mengalami fluktuasi skala yang lebar dari satu bingkai citra ke bingkai berikutnya.

Detektor objek satu tahap konvensional seperti YOLOv5 sering kali tidak mampu mendeteksi objek sekecil ini. Fitur spasial objek kecil cenderung terdegradasi akibat operasi konvolusi dan penyusutan spasial (*downsampling*) bertingkat di dalam tulang punggung (*backbone*) jaringan. Selain itu, operasi konvolusi lokal standar memiliki keterbatasan dalam menangkap ketergantungan jarak jauh (*long-range dependencies*), sehingga model kesulitan mengasosiasikan objek dengan konteks lingkungan sekitarnya untuk mengenali objek yang mengalami oklusi (terhalang). Terakhir, latar belakang citra yang kompleks, seperti jalan raya, vegetasi, dan bayangan gedung, menghasilkan tingkat kebisingan (*noise*) yang tinggi, memicu terjadinya deteksi positif palsu (*false positives*). Ketiadaan informasi konteks global dan hilangnya resolusi spasial halus menjadi celah utama yang ingin diselesaikan oleh penelitian ini.

## Ide Utama
Ide utama TPH-YOLOv5 berfokus pada restrukturisasi arsitektur YOLOv5 untuk memelihara detail spasial halus dan menangkap informasi konteks global melalui tiga pilar:
1. **Penambahan Jalur Prediksi Resolusi Tinggi (P2):** Jalur deteksi keempat ditambahkan untuk beroperasi pada peta fitur dengan tingkat penyusutan (*stride*) rendah (hanya 4 kali penyusutan dari resolusi input), guna melestarikan representasi spasial objek yang sangat kecil sebelum hilang akibat operasi konvolusi lebih dalam.
2. **Transformer Prediction Head (TPH):** Mengganti blok konvolusi *CSP Bottleneck* pada leher deteksi dengan blok *Transformer Encoder*. Blok ini memanfaatkan mekanisme perhatian mandiri (*self-attention*) untuk mengekstrak hubungan spasial global antar-fitur di seluruh citra.
3. **Penyaringan Fitur Menggunakan CBAM:** Modul perhatian spasial dan saluran CBAM disisipkan di dalam leher jaringan (*neck*) untuk menyaring sinyal fitur secara adaptif, memusatkan fokus model pada objek sasaran dan meredam kebisingan latar belakang.

Sebagai pelengkap pasca-pemrosesan, sistem ini menggunakan pengklasifikasi sekunder berbasis ResNet-18 yang bekerja pada potongan gambar objek untuk meminimalkan kesalahan klasifikasi pada kategori yang secara visual mirip.

## Cara Kerja Langkah demi Langkah
Diagram berikut menunjukkan modifikasi alur kerja arsitektural TPH-YOLOv5 dibandingkan dengan baseline YOLOv5, yang mencakup penambahan head P2, integrasi CBAM, dan penggunaan blok Transformer pada prediction head.

```
       ┌────────────────────────────────────────────────────────┐
       │                 Input Citra (640x640)                  │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │  Backbone: CSPDarknet53  │
                     └──────┬───┬───┬───┬───────┘
                            │   │   │   │
        P2 Feature (160x160)│   │   │   │ P5 Feature (20x20)
       ┌────────────────────┘   │   │   └───────────────────────┐
       │                        │   │                           │
       │    P3 Feature (80x80)  │   │ P4 Feature (40x40)        │
       │   ┌────────────────────┘   └───────────────┐           │
       │   │                                        │           │
       ▼   ▼                                        ▼           ▼
     ┌────────────────────────────────────────────────────────────┐
     │                    Neck: PANet + CBAM                      │
     │  - Multi-scale Feature Fusion                              │
     │  - Channel & Spatial Attention via CBAM Module             │
     └─┬───┬────────────────────────────────────────┬───┬─────────┘
       │   │                                        │   │
       │   │                                        │   │
       ▼   ▼                                        ▼   ▼
     ┌───────────┐                            ┌───────────┐
     │  TPH (P2) │                            │  TPH (P4) │
     │  160x160  │                            │   40x40   │
     └─────┬─────┘                            └─────┬─────┘
           │                                        │
           ▼                                        ▼
    [Objek Sangat Kecil]                      [Objek Sedang]
                                  
     ┌───────────┐                            ┌───────────┐
     │  TPH (P3) │                            │  TPH (P5) │
     │   80x80   │                            │   20x20   │
     └─────┬─────┘                            └─────┬─────┘
           │                                        │
           ▼                                        ▼
      [Objek Kecil]                            [Objek Besar]
```

### ### Integrasi Jalur Deteksi P2 Resolusi Tinggi
Pada model YOLOv5 standar, deteksi dilakukan pada tiga peta fitur dengan dimensi spasial $80 \times 80$, $40 \times 40$, and $20 \times 20$ (untuk input citra $640 \times 640$). Untuk mempertahankan informasi objek mikro, TPH-YOLOv5 memperkenalkan jalur deteksi keempat yang disebut P2. Jalur ini beroperasi pada tingkat penyusutan (*stride*) 4, menghasilkan peta fitur beresolusi $160 \times 160$ piksel. Dengan mengalirkan fitur resolusi tinggi dari lapisan awal *backbone* langsung ke leher jaringan (*neck*), detail geometris objek yang berukuran di bawah $8 \times 8$ piksel dapat dipertahankan tanpa mengalami degradasi akibat operasi *downsampling* yang berulang.

### ### Penerapan Blok Transformer Encoder pada Head Deteksi
Gagasan utama untuk membedakan objek dalam kondisi padat dan terhalang diselesaikan dengan mengganti blok konvolusi *CSP Bottleneck* pada prediction head dengan blok *Transformer Encoder*. Blok ini terdiri dari lapisan *Multi-Head Self-Attention* (MHSA) dan lapisan *Feed-Forward Network* (FFN) dua tingkat yang dilengkapi dengan normalisasi lapisan (*layer normalization*).

Dalam blok ini, setiap nilai piksel spasial dari peta fitur diubah menjadi representasi vektor yang berfungsi sebagai token. Melalui mekanisme MHSA, model menghitung bobot keterkaitan dinamis antara satu lokasi piksel dengan seluruh lokasi piksel lainnya di dalam citra. Hal ini memungkinkan model untuk menangkap konteks spasial global secara komprehensif, sehingga ketika sebuah objek (misalnya mobil) terhalang oleh pohon, model tetap dapat mengenalinya berdasarkan fitur lingkungan sekitarnya (seperti pola jalan raya atau bayangan linier).

### ### Penguatan Fitur Melalui CBAM di Neck
Untuk mereduksi kebisingan latar belakang yang bising pada citra udara, modul CBAM disisipkan sebelum fitur digabungkan dalam *Path Aggregation Network* (PANet). CBAM bekerja secara sekuensial:
1. *Channel Attention Module* (CAM) menekan saluran fitur yang tidak relevan dengan mengevaluasi kontribusi setiap saluran melalui operasi rata-rata (*average pooling*) dan maksimum (*max pooling*).
2. *Spatial Attention Module* (SAM) menentukan lokasi spasial yang paling penting dengan memproyeksikan fitur saluran ke bentuk peta probabilitas dua dimensi, memastikan detektor berfokus pada area keberadaan objek nyata dan mengabaikan area latar belakang seperti atap gedung atau air.

### ### Pemurnian Klasifikasi Menggunakan Pengklasifikasi Crop Sekunder
Objek dengan resolusi spasial yang sangat rendah sering kali memiliki fitur visual yang mirip, menyebabkan kesalahan klasifikasi antar-kelas yang berdekatan (seperti sepeda motor dengan sepeda). Untuk mengatasi masalah ini, TPH-YOLOv5 menerapkan modul pasca-pemrosesan berupa pengklasifikasi sekunder berbasis arsitektur ResNet-18.

Setiap kotak pembatas (*bounding box*) kandidat yang dihasilkan oleh model deteksi dipotong (*cropped*) dari citra asli beresolusi tinggi, diubah ukurannya (*resized*) menjadi $64 \times 64$ piksel, dan dilewatkan ke ResNet-18 yang telah dilatih secara terpisah pada dataset potongan objek. Pengklasifikasi ini bertugas memverifikasi dan memperbaiki label kelas yang meragukan dari hasil deteksi utama, sehingga secara signifikan mengurangi kesalahan klasifikasi pada objek-objek kecil yang membingungkan.

## Eksperimen dan Hasil
Evaluasi kinerja TPH-YOLOv5 dilakukan pada dataset benchmark **VisDrone-DET2021**. Dataset ini menantang karena berisi ribuan citra udara perkotaan dengan kepadatan objek tinggi yang diambil dari berbagai sudut pandang UAV.

Studi ablasi (*ablation study*) pada subset **VisDrone-DET test-dev** menunjukkan dampak dari masing-masing modifikasi arsitektur:

| Konfigurasi Model | mAP (%) | GFLOPs |
|---|:---:|:---:|
| YOLOv5 (Baseline) | 28,88 | 219,0 |
| YOLOv5 + P2 (Head Deteksi Mikro) | 31,03 | - |
| YOLOv5 + P2 + Transformer (TPH) | 32,84 | - |
| TPH-YOLOv5 (YOLOv5 + P2 + TPH + CBAM) | 33,63 | 259,0 |
| TPH-YOLOv5 + *Multi-Scale Testing* | 34,90 | - |
| TPH-YOLOv5 + *Multi-Scale Testing* + *Classifier* ResNet-18 | 35,74 | - |

Integrasi head P2 memberikan lonjakan akurasi awal yang besar (+2,15% mAP), memvalidasi kegunaan peta fitur resolusi tinggi. Blok Transformer (TPH) menambahkan peningkatan sebesar +1,81% mAP, membuktikan kegunaan fitur konteks global. Gabungan seluruh komponen menghasilkan nilai mAP sebesar 33,63%.

Saat dievaluasi pada dataset **VisDrone-DET2021 test-challenge** yang lebih kompetitif, model final TPH-YOLOv5 mencapai skor mAP sebesar **39,18%** (pada IoU 0,5:0,95) dengan menggunakan pengujian multi-skala dan pengklasifikasi sekunder. Hasil ini mengamankan peringkat kelima pada kompetisi VisDrone 2021, menunjukkan keunggulan performa dibanding detektor satu tahap standar lainnya.

## Kelebihan dan Keterbatasan
Kelebihan utama TPH-YOLOv5 adalah kemampuannya yang luar biasa dalam melokalisasi objek mikro dan menangani skenario padat objek yang mengalami oklusi. Integrasi mekanisme perhatian mandiri (*self-attention*) global melalui Transformer dan CBAM memungkinkan model membedakan objek dari latar belakang yang berisik secara presisi.

Namun, secara konseptual dan dari sisi rekayasa, model ini memiliki keterbatasan berupa beban komputasi yang sangat besar. Penambahan head keempat (P2) dan modul Transformer meningkatkan tuntutan komputasi dari 219,0 GFLOPs menjadi 259,0 GFLOPs. Peningkatan ini menyebabkan penurunan kecepatan inferensi (*frames per second* / FPS) yang drastis, sehingga membatasi kemampuan model untuk diterapkan secara langsung (*on-board*) pada perangkat komputasi tepi dengan daya terbatas di dalam drone untuk pemrosesan video *real-time*. Selain itu, penggunaan pengklasifikasi sekunder ResNet-18 di tahap pasca-pemrosesan memecah alur kerja deteksi menjadi proses dua tahap yang tidak efisien karena waktu inferensinya berbanding lurus dengan jumlah objek yang terdeteksi dalam citra.

## Kaitan dengan Bab Lain
Perkembangan deteksi objek pada citra penginderaan jauh (*remote sensing*) menunjukkan transisi dari metode berbasis pemotongan eksternal menuju modifikasi arsitektur internal.

Silsilah ini dapat ditarik dari model **YOLT** ([You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md)) yang mengatasi masalah resolusi citra satelit yang besar dengan teknik pembagian ubin (*tiling*) eksternal dan inferensi dua langkah. TPH-YOLOv5 mengambil pendekatan berbeda dengan memodifikasi arsitektur jaringan secara internal melalui penambahan head P2 resolusi tinggi dan modul Transformer untuk menghindari *tiling* yang lambat.

Pendekatan representasi fitur hierarkis untuk mengatasi variasi skala juga telah dirintis dalam **Robust CNN High-Res Remote Sensing** ([Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md)), yang memodelkan hubungan spasial antar-skala menggunakan jaringan konvolusi bertingkat. TPH-YOLOv5 memperluas konsep pemodelan spasial ini dengan menggabungkan mekanisme perhatian mandiri global (*self-attention*) dari Transformer dan perhatian spasial-saluran CBAM.

Evolusi model drone berikutnya diwakili oleh **UAV-YOLOv8** ([UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md)). UAV-YOLOv8 berupaya mengatasi keterbatasan beban komputasi yang tinggi pada TPH-YOLOv5 dengan memanfaatkan arsitektur *anchor-free* YOLOv8 dan modul perhatian yang lebih ringan, memulihkan kecepatan inferensi tanpa mengorbankan akurasi deteksi objek kecil pada platform UAV.

## Poin untuk Sitasi
Kunci BibTeX untuk merujuk naskah ini adalah `zhu2021tphyolov5`.
Berikut adalah ringkasan yang aman dikutip dalam tinjauan pustaka:

> Zhu dkk. mengusulkan TPH-YOLOv5, variasi YOLOv5 untuk skenario UAV yang menambahkan head prediksi beresolusi tinggi keempat (P2) dan mengintegrasikan blok Transformer Encoder di bagian prediction head serta modul CBAM di leher jaringan. Model ini dilengkapi dengan pengklasifikasi sekunder berbasis ResNet-18 pada pasca-pemrosesan untuk menyaring klasifikasi objek kecil yang membingungkan, mencapai mAP sebesar 39,18% pada dataset VisDrone-DET2021.

Catatan untuk verifikasi lebih lanjut:
- Perlu dicatat bahwa penambahan pengklasifikasi ResNet-18 yang terpisah merupakan penyumbang peningkatan akurasi akhir sebesar 0,84% mAP pada test-dev (dari 34,90% menjadi 35,74%). Pengguna yang bermaksud mengimplementasikan sistem ini secara terpadu tanpa pengklasifikasi tambahan harus merujuk pada performa deteksi murni TPH-YOLOv5 sebesar 33,63% mAP pada subset test-dev.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract Object detection on drone-captured scenarios is a recent popular task. As drones always navigate in different altitudes, the object scale varies violently, which burdens the optimization of networks. Moreover, high-speed and low-altitude flight bring in the motion blur on the densely packed objects, which leads to great challenge of object distinction. To solve the two issues mentioned above, we propose TPH-YOLOv5. Based on YOLOv5, we add one more prediction head to detect different-scale objects. Then we replace the original prediction heads with Transformer Prediction Heads (TPH) to explore the prediction potential with self-attention mechanism. We also integrate convolutional block attention model (CBAM) to find attention region on scenarios with dense objects. To achieve more improvement of our proposed TPH-YOLOv5, we provide bags of useful strategies such as data augmentation, multiscale testing, multi-model integration and utilizing extra classifier. Extensive experiments on dataset VisDrone2021 show that TPH-YOLOv5 have good performance with impressive interpretability on drone-captured scenarios. On DET-test-challenge dataset, the AP result of TPH-YOLOv5 are 39.18%, which is better than previous SOTA method (DPNetV3) by 1.81%. On VisDrone Challenge 2021, TPHYOLOv5 wins 5th place and achieves well-matched results with 1st place model (AP 39.43%). Compared to baseline model (YOLOv5), TPH-YOLOv5 improves about 7%, which is encouraging and competitive.

Figure 1. Intuitive cases to explain the three main problems in object detection on drone-captured images. The cases in first row, second row and third row respectively shows the size variation, high-density and large coverage of objects on drone-captured images.

1. Introduction Object detection technology on drone-captured scenarios has been widely used in many practical applications, such as plant protection [18, 41], wildlife protection [23, 22] and urban surveillance [1, 15]. In this paper, we focus on improv* Contribute Equally. † Corresponding author.

ing the performance of object detection on drone-captured images and providing insight for the above-mentioned numerous applications. Recent years have witnessed significant progresses in object detection tasks using deep convolutional neural networks [40, 37, 34, 27, 58]. Some notable benchmark datasets like MS COCO [30] and PASCALVOC [9] greatly

Figure 2. The overview of working pipeline using TPH-YOLOv5. Compared to original version, we mainly improve the head by applying Transformer Prediction Head (TPH). We also add one more head to better detect different scale objects. In addition, we employ bag of tricks like data augmentation, multi-scale testing, model ensemble and self-trained classifier to make TPH-YOLOv5 stronger.

promote the development of object detection application. However, most previous deep convolutional neural networks are designed for natural scene images. Directly applying previous models to tackle object detection task on drone-captured scenarios mainly has three problems, which are intuitively illustrated by some cases in Fig.1. First, the object scale varies violently because the flight altitude of drones change greatly. Second, drone-captured images contain objects with high density, which brings in occlusion between objects. Third, drone-captured images always contain confusing geographic elements because of covering large area. The above-mentioned three problems make the object detection of drone-captured images very challenging.

also add multi-scale testing (ms-testing) and multi-model ensemble strategies during inference to obtain more convincing detection results. Moreover, through visualizing the failure cases, we find that our proposed architecture has excellent localization ability but poor classification ability, especially on some similar categories like “tricycle” and “awning-tricycle”. To solve this problem, we provide a selftrained classifier (ResNet18 [17]) using the image patches cropping from training data as classification training set. With self-trained classifier, our method has 0.8%∼1.0% improvement on AP value. Our contributions are listed as follows:

In object detection task, YOLO series [37, 38, 39, 2] play an important role in one-stage detectors. In this paper, we propose an improved model, TPH-YOLOv5 based on YOLOv5 [21] to solve the above-mentioned three problems. The overview of the detection pipeline using TPHYOLOv5 is shown in Fig.2. We respectively use CSPDarknet53 [52, 2] and path aggregation network (PANet [33]) as backbone and neck of TPH-YOLOv5, which follows the original version. In the head part, we first introduce one more head for tiny object detection. Totally, TPH-YOLOv5 contains four detection heads separately used for the detection of tiny, small, medium, large objects. Then, we replace the original prediction heads with Transformer Prediction Heads (TPH) [7, 49] to explore the prediction potential. To find the attention region in images with large coverage, we adopt Convolutional Block Attention Module (CBAM [54]) to sequentially generate the attention map along channelwise and spatial-wise dimensions. Compared to YOLOv5, our improved TPH-YOLOv5 can better deal with dronecaptured images.

• We add one more prediction head to deal with large scale variance of objects.

To further improve the performance of TPH-YOLOv5, we employ bag of tricks (Fig.2). Specifically, we adopt data augmentation during training, which promote the adaptation for dramatic size changes of objects in images. We

• We integrate the Transformer Prediction Heads (TPH) into YOLOv5, which can accurately localize objects in high-density scenes. • We integrate CBAM into YOLOv5, which can help the network to find region of interest in images that have large region coverage. • We provide useful bag of tricks and filtering some useless tricks for object detection task on drone-captured scenarios. • We use self-trained classifier to improve the classification ability on some confusing categories. • On VisDrone2021 test-challenge dataset, our proposed TPH-YOLOv5 achieve 39.18% (AP), outperforming DPNetV3 (previous SOTA method) by 1.81%. In VisDrone2021 DET challenge, TPH-YOLOv5 wins 5th place and has minor gap comparing with 1st place models.

2. Related Work 2.1. Data Augmentation The effectiveness of data augmentation is to expand the dataset, so that the model has higher robustness to the images obtained from different environments. Photometric distortions and geometric distortions are wildly used by researchers. As for photometric distortion, we adjusted the hue, saturation and value of the images. In dealing with geometric distortion, we add random scaling, cropping, translation, shearing, and rotating. In addition to the abovementioned global pixel augmentation methods, there are some more unique data augmentation methods. Some researchers have proposed methods using multiple images together for data augmentation i.e. MixUp [57], CutMix [56] and Mosaic [2]. MixUp randomly select two samples from the training images to perform random weighted summation, and the labels of the samples also correspond to the weighted summation. Unlike occlusion works that generally use zero-pixel ”black cloth” to occlude a image, CutMix uses an area of another image to cover the occluded area. Mosaic is an improved version of the CutMix. Mosaic stitches four images, which greatly enriches the background of the detected object. In addition, batch normalization calculates the activation statistics of 4 different images on each layer. In TPH-YOLOv5, we use a combination of MixUp, Mosaic and traditional methods in data augmentation.

2.2. Multi-Model Ensemble Method in Object Detection Deep learning neural networks are non-linear methods. They provide greater flexibility and can scale in proportion to the amount of training data. One disadvantage of this flexibility is that they learn through random training algorithms, which means that they are sensitive to the details of the training data, and may find a different set of weights each time they train, resulting in different predictions. This gives the neural network a high variance. A successful way to reduce the variance of neural network models is to train multiple models instead of a single model, and combine the predictions of these models. There are three different methods to ensemble boxes from different object detection models: Non-maximum suppression (NMS) [36], Soft-NMS [53], weighted boxes fusion (WBF) [43]. In the NMS method, if the overlap, intersection over union (IoU) of the boxes is higher than a certain threshold, they are considered to belong to the same object. For each object, NMS only leaves one bounding box with the highest confidence, and other bounding boxes are deleted. Therefore, the box filtering process depends on the choice of this single IoU threshold, which have a big impact on model performance. Soft-NMS has made

a slightly change to NMS, which made Soft-NMS shows a significant improvement over traditional NMS on standard benchmark datasets (such as PASCAL VOC [10] and MS COCO [30]). It sets an attenuation function for the confidence of adjacent bounding boxes based on the IoU value instead of completely setting their confidence scores to zero and delete them. WBF works differently from NMS. Both NMS and Soft-NMS exclude some boxes, while WBF merges all boxes to form the final result. Therefore, it can solve all the inaccurate predictions of the model. We use WBF to ensemble final models, which performs much better than NMS.

Figure 3. The architecture of the TPH-YOLOv5. a) CSPDarknet53 backbone with three transformer encoder blocks at the end. b) The Neck use the structure like PANet. c) Four TPHs (transformer prediction heads) use the feature maps from transformer encoder blocks in Neck. In addition, the number of each block is marked with orange numbers on the left side of the block.

gies. There are also some additional blocks used in neck, like SPP [16], ASPP [5], RFB [31], CBAM [54]. Head. As a classification network, the backbone cannot complete the positioning task, and the head is designed to be responsible for detecting the location and category of the object by the features maps extracted from the backbone. Heads are generally divided into two kinds: one-stage object detector and two-stage object detector. Two-stage detectors have long been the dominant method in the field of object detection, and the most representative one is the RCNN series [14, 13, 40]. Compared with the two-stage detector, the one-stage detector predicts the bounding box and the class of objects at the same time. The speed advantage of the one-stage detector is obvious, but the accuracy is lower. For one-stage detectors, the most representative models are YOLO series [37, 38, 39, 2], SSD [34] and RetinaNet [29].

3. TPH-YOLOv5 3.1. Overview of YOLOv5 YOLOv5 has four different models including YOLOv5s, YOLOv5m, YOLOv5l and YOLOv5x. Generally, YOLOv5 respectively uses the architecture of CSPDarknet53 with an SPP layer as backbone, PANet as Neck and YOLO detection head [37]. To further optimize the whole architecture, bag of freebies and specials [2] are provided. Since it is the most notable and convenient one-stage detector, we select it

as our baseline. When we train the model using VisDrone2021 dataset [64] with data augmentation strategy (Mosaic and MixUp), we find that the results of YOLOv5x are much better than YOLOv5s, YOLOv5m and YOLOv5l, and the gap of AP value is more than 1.5%. Even though the training computation cost of the YOLOv5x model is more than that of other three models, we still choose to use YOLOv5x to pursue the best detection performance. In addition, according to the features of drone-captured images, we adjust the parameters of commonly used photometric distortions and geometric distortions.

3.2. TPH-YOLOv5 The framework of TPH-YOLOv5 is illustrated in Fig. 3. We modify the original YOLOv5 to make it specialize in the VisDrone2021 dataset. Prediction head for tiny objects. We investigate the VisDrone2021 dataset and find that it contains many extremely small instances, so we add one more prediction head for tiny objects detection. Combined with the other three prediction heads, our four-head structure can ease the negative influence caused by violent object scale variance. As shown in Fig. 3, the prediction head (head No.1) we add is generated from low-level, high-resolution feature map, which is more sensitive to tiny objects. After adding an additional detection head, although the computation and memory cost increase, the performance of tiny objects detection gets large

Figure 5. The overview of CBAM module. Two sequential submodules are used to refine feature map that go through CBAM, residual paths are also used.

Figure 4. The architecture of transformer encoder, which contains two main blocks, a multi-head attention block and a feed-forward neural network (MLP). LayerNorm and Dropout layers help the network converge better and prevent the network from over fitting. Multi-head attention can help the current node not only pay attention to the current pixels, but also obtain the semantics of the context.

Transformer encoder block. Inspired by the vision transformer [6], we replace some convolutional blocks and CSP bottleneck blocks in original version of YOLOv5 with transformer encoder blocks. The structure is shown in Fig. 4. Compared to original bottleneck block in CSPDarknet53, we believe that transformer encoder block can capture global information and abundant contextual information. Each transformer encoder contains two sub-layers. The first sub-layer is a multi-head attention layer and the second one (MLP) is a fully-connected layer. Residual connections are used between each sub-layer. Transformer encoder blocks increase the ability to capture different local information. It can also explore the feature representation potential with self-attention mechanism [50]. On the VisDrone2021 dataset, transformer encoder blocks have better performance on occluded objects with high-density. Based on YOLOv5, we only apply transformer encoder blocks in the head part to form Transformer Prediction Head (TPH) and the end of backbone. Because the feature maps at the end of the network have low resolution. Applying TPH on low-resolution feature maps can decrease the expensive computation and memory cost. Moreover, when we enlarge the resolution of input images, we optional remove some TPH blocks at early layers to make the training

process available. Convolutional block attention module (CBAM). CBAM [54] is a simple but effective attention module. It is a lightweight module that can be integrated into most notable CNN architectures, and it can be trained in an end-to-end manner. Given a feature map, CBAM sequentially infers the attention map along two separate dimensions of channel and spatial, and then multiplies the attention map with the input feature map to perform adaptive feature refinement. The structure of the CBAM module is shown in the Fig. 5. According to the experiment in the paper [54], after integrating CBAM into different models on different classification and detection datasets, the performance of the model get large improved, which proves the effectiveness of this module. On drone-captured images, large covering region always contains confusing geographical elements. Using CBAM can extract the attention area to help TPH-YOLOv5 resist the confusing information and focus on useful target objects. Ms-testing and model ensemble. We train five different models in terms of different perspectives for model ensemble. During inference phase, we first perform ms-testing strategy on single model. The implementation details of ms-testing are the following three steps. 1) Scaling the testing image to 1.3 times. 2) Respectively reducing the image to 1 time, 0.83 times, and 0.67 times. 3) Flipping the images horizontally. Finally, we feed the six different-scaling images to TPH-YOLOv5 and use NMS to fuse the testing predictions. On different models, we perform the same ms-testing operation and fuse the final five predictions by WBF to get the final result. Self-trained classifier. After training the VisDrone2021 dataset with TPH-YOLOv5, we test the test-dev dataset and then analyze the results by visualizing the failure cases and draw a conclusion that TPH-YOLOv5 has excellent localization ability but poor classification ability. We further explore the confusion matrix which is shown in Fig.6, and observe that the precision of the some hard categories such as tricycle and awning-tricycle are very low. Therefore, we propose an extra self-trained classifier. First, we construct

a training set by cropping the ground-truth bounding boxes and resizing each image patches to 64×64. Then we select ResNet18 [17] as classifier network. As shown in experimental results, our method get around 0.8%˜1.0% improvement on AP value with the help of this self-trained classifier.

Figure 7. Some images were taken too high, resulting in many small objects, which cannot be recognized.

4. Experiments We use the testset-challenge and testset-dev of the VisDrone2021 dataset to evaluate our model, and we report mAP (average of all 10 IoU thresholds, ranging from [0.5: 0.95]) and AP50. VisDrone2021-DET dataset is the same as VisDrone2019-DET dataset and VisDrone2018DET dataset.

4.1. Implementation Details We implement TPH-YOLOv5 on Pytorch 1.8.1. All of our models use an NVIDIA RTX3090 GPU for training and testing. In the training phase, we use part of pre-trained model from yolov5x, because TPH-YOLOv5 and YOLOv5 share most part of backbone (block 0˜8) and some part of head (block 10˜13 and block 15˜18), there are many weights can be transferred from YOLOv5x to TPH-YOLOv5, by using these weights we can save a lot of training time. Because the VisDrone2021 training set is a bit small, we only train the model on VisDrone2021 trainset for 65 epochs, and the first 2 epochs are used for warm-up. We use adam optimizer for training, and use 3e-4 as the initial learning rate with the cosine lr schedule. The learning rate of the last epoch decays to 0.12 of the initial learning rate. The size of the input image of our model is very large, the long side of the image is 1536 pixels, which leads to the batch size is only 2. Data analysis. According to our previous engineering experience, it is very important to walk through dataset before

training the model, which can often be of great help to the improvement of mAP. We have analyzed bounding boxes in the VisDrone2021 dataset. When the input image size is set to 1536, there are 622 of 342391 labels are less than 3 pixels in size. As shown in Fig. 7, these small objects are hard to recognize. When we use gray squares to cover these small objects and train our model on the processed dataset, the mAP improves by 0.2, better than not. Ms-testing. When training neural network models for computer vision problems, data augmentation is a technique often used to improve performance and reduce generalization errors. When using a model to make predictions, image data augmentation of test dataset can also be applied to allow the model to make predictions on multiple different versions of images. The prediction of the augmented images can be averaged to get better prediction performance. We scale the test images to three different sizes in mstesting, and then flip them horizontally, so that a total of 6 different images are obtained. After testing six different images and fusing the results, we get the final test result.

4.2. Comparisons with the State-of-the-art On VisDrone2021-DET testset-challenge. Due to the limited number of submissions in the VisDrone2021 competition server, we only obtained the results of 4 models on testset-challenge and the final results of the ensemble of 5 models. We finally got a good score of 39.18 on testset-challenge, which is much higher than VisDrone2020’s best score of 37.37. Ranked fifth in the VisDrone 2021 leader board, our score is 0.25 lower than the 39.43 of the first place. If the number of submissions is not used up, we will definitely get better results. Table 1 lists the score of our model, compared with the scores in the previous year’s VisDrone competition and the scores of algorithms submitted by the committee.

result. 1) TPH-YOLOv5-1 use the input image size of 1920 and all categories have equal weights. 2) TPH-YOLOv52 use the input image size of 1536 and all categories have equal weights. 3) TPH-YOLOv5-3 use the input image size of 1920 and the weight of each category is related to the number of labels, which is shown in Fig. 8. The more labels of a certain category, the lower the weight it is given. 4) TPH-YOLOv5-4 use the input image size of 1536 and the weight of each category is related to the number of labels. 5) TPH-YOLOv5-5 use the backbone of YOLOv5l and use the input image size of 1536.

4.3. Ablation Studies On VisDrone2021-DET testset-dev. we analyze importance of each proposed component on local testset-dev as we cannot test these on VisDrone2021 competition server, the number of submissions to the competition server is very valuable. The impact of each component is listed in the table 2. Methods YOLOv5 YOLOv5+P2 YOLOv5+P2+transformer TPH-YOLOv5 (previous+CBAM) TPH-YOLOv5+ms-testing TPH-YOLOv5+ms-testing+Classifier

Some detection result on VisDrone2021 testsetchallenge. We have selected some representative images as the display of the test results. Fig. 9 shows the result of large objects, tiny objects, dense objects and the image covering a large area.

5. Conclusion In this paper, we add some cutting-edge techniques i.e. transformer encoder block, CBAM and some experienced tricks to YOLOv5 and form a state-of-the-art detector called TPH-YOLOv5, which is especially good at object detection in drone-captured scenarios. We refresh the record of VisDrone2021 dataset, our experiments showed that TPH-YOLOv5 achieved state-of-the-art performance in VisDrone2021 dataset. We have tried a large number of features, and used some of them to improve the accuracy of object detector. We hope this report can help developers and researchers get a better experience in the analysis and processing of drone-captured scenarios.

Table 3. Comparison of TPH-YOLOv5 models‘ performances on VisDrone2021 testset-dev for each category.

Figure 9. Some visualization results from our TPH-YOLOv5 on testset-challenge, different category use bounding boxes with different color. The performance is good at localization tiny objects, dense objects and objects blurred by motion.
