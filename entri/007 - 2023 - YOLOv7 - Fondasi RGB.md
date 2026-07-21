# 007 - YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023yolov7` |
| Judul asli | YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors |
| Penulis | Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao |
| Tahun | 2023 (pracetak arXiv Juli 2022) |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2207.02696
- **DOI (arXiv):** https://doi.org/10.48550/arXiv.2207.02696
- **Repositori kode resmi:** https://github.com/WongKinYiu/yolov7
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan YOLOv7, detektor objek satu tahap *real-time* yang dilatih dari awal hanya pada dataset MS COCO, tanpa bobot pralatih maupun data tambahan. Gagasan sentralnya adalah *trainable bag-of-freebies*: teknik yang menambah biaya pelatihan demi akurasi, tanpa menambah biaya inferensi (biaya menjalankan model jadi). Tiga komponen utamanya adalah blok agregasi fitur E-ELAN, konvolusi reparameterisasi terencana, dan penetapan label *coarse-to-fine* yang memakai kepala bantu.

Hasil utamanya: pada rentang 5 hingga 160 *frame* per detik (FPS) di GPU V100, YOLOv7 melampaui detektor *real-time* lain pada masanya dalam kombinasi kecepatan dan akurasi. Varian terbesarnya, YOLOv7-E6E, mencapai 56,8% AP (metrik akurasi utama COCO) pada 36 FPS — tertinggi di antara detektor *real-time* berkecepatan minimal 30 FPS saat terbit.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Silsilah YOLO merupakan upaya menaikkan akurasi tanpa mengorbankan kecepatan. YOLOv4 (bab 004) memperkenalkan konsep *bag-of-freebies* — teknik pelatihan yang menaikkan akurasi tanpa menambah biaya inferensi. YOLOX (bab 005) memopulerkan penetapan label dinamis: target pelatihan dihitung dari kualitas prediksi jaringan, bukan ditetapkan kaku dari kebenaran dasar (*ground truth*). YOLOv6 (bab 006) memakai reparameterisasi struktural gaya RepVGG: modul bercabang banyak saat pelatihan dilebur menjadi satu lapis konvolusi saat inferensi.

Penulis menemukan dua masalah baru. Pertama, RepConv — gabungan konvolusi 3×3, konvolusi 1×1, dan koneksi identitas (penjumlahan langsung masukan ke keluaran) — bekerja baik pada arsitektur polos, tetapi akurasinya turun saat diterapkan langsung pada arsitektur berkoneksi residual (blok yang menjumlahkan masukan ke keluarannya, seperti ResNet) atau berbasis konkatenasi (penggabungan peta fitur sepanjang dimensi kanal, seperti DenseNet); belum ada aturan kapan kombinasi itu aman. Kedua, bila detektor dilatih dengan lebih dari satu kepala keluaran melalui *deep supervision* (penambahan kepala bantu di lapisan tengah), muncul pertanyaan: kepala mana yang menetapkan target untuk kepala yang lain. Selain itu, penskalaan model lazimnya menganalisis tiap faktor secara terpisah, padahal pada model konkatenasi keduanya saling terkait.

## Ide Utama

Pisahkan tegas biaya pelatihan dari biaya inferensi. Selama pelatihan, jaringan boleh dibebani struktur tambahan — cabang konvolusi ekstra, kepala keluaran bantu, mekanisme penetapan label berlapis — asalkan semuanya dapat dilebur ke lapis lain atau dibuang saat inferensi.

Jalur datanya sendiri tidak berubah dari keluarga YOLO: citra mengalir melalui *backbone* (bagian awal jaringan yang mengekstraksi fitur) dan leher (*neck*, modul penggabung fitur multi-skala) berbasis blok E-ELAN, lalu ke kepala deteksi. Yang diubah makalah ini adalah cara blok dilatih, cara target pelatihan dibuat, dan cara model diskalakan.

## Cara Kerja Langkah demi Langkah

### Blok E-ELAN

Dasar arsitektur YOLOv7 adalah ELAN (*Efficient Layer Aggregation Network*), strategi desain dari grup penulis yang sama: jaringan dalam dapat belajar efektif bila jalur gradien terpendek dan terpanjangnya dikendalikan. Jalur gradien (*gradient path*) adalah rute sinyal gradien saat pembaruan bobot; jalur yang terlalu panjang menyulitkan konvergensi.

E-ELAN memperluas ELAN tanpa mengubah jalur gradiennya melalui tiga operasi: *expand*, *shuffle*, dan *merge cardinality* (*cardinality* = jumlah cabang paralel dalam satu blok). Setiap blok hitung diperluas memakai konvolusi grup (*group convolution* — konvolusi yang membagi kanal menjadi beberapa grup yang diproses terpisah). Peta fitur keluaran tiap blok dibagi menjadi g grup, dipertukarkan antarblok, lalu dikonkatenasi; terakhir, g grup dijumlahkan elemen demi elemen. Hanya bagian dalam blok hitung yang berubah, sedangkan lapisan transisi dipertahankan, sehingga kemampuan belajar naik tanpa merusak stabilitas gradien ELAN.

Alur data dalam satu lapisan E-ELAN:

```
masukan
   │
   ▼
┌──────────────────────────────────────┐
│ n blok hitung paralel; jalur gradien │   tiap blok: konvolusi grup,
│ ELAN dipertahankan utuh              │   kanal diperluas × pengali
└───┬────────┬────────┬────────┬───────┘
    ▼        ▼        ▼        ▼
  [FM1]    [FM2]    [FM3]    [FM4]   peta fitur tiap cabang
    │        │        │        │
    └────────┴───┬────┴────────┘
                 ▼
     shuffle: tiap peta dibagi g grup,
     grup dipertukarkan antarcabang,
     lalu dikonkatenasi
                 │
                 ▼
     merge cardinality:
     g grup dijumlahkan elemen demi elemen
                 │
                 ▼
             keluaran
```

### Penskalaan Gabungan untuk Model Berbasis Konkatenasi

*Model scaling* menghasilkan varian model berbeda ukuran dari satu desain dasar dengan mengubah kedalaman (jumlah lapis) atau lebar (jumlah kanal). Pada arsitektur biasa, tiap faktor dapat dianalisis terpisah karena memperdalam jaringan tidak mengubah lebar lapis lain. Pada model berbasis konkatenasi hal itu tidak berlaku: menaikkan kedalaman sebuah blok menambah jumlah peta fitur yang dikonkatenasi, sehingga lebar keluaran blok dan lebar masukan lapisan transisi berikutnya ikut berubah.

Solusinya, penskalaan gabungan (*compound scaling*): saat faktor kedalaman blok hitung dinaikkan, perubahan lebar keluarannya dihitung, lalu faktor lebar lapisan transisi dinaikkan dengan besar yang setara, sehingga rasio kanal optimal model dasar terjaga. Pada studi ablasi (uji yang mematikan komponen satu per satu untuk mengukur sumbangannya) dipakai kedalaman ×1,5 dan lebar transisi ×1,25. Cara ini menghasilkan varian YOLOv7-X, E6, dan D6.

### Reparameterisasi Terencana

Reparameterisasi struktural melatih modul bercabang banyak, lalu menggabungkannya menjadi satu lapis yang ekuivalen secara matematis saat inferensi. Penulis menemukan cabang koneksi identitas di dalam RepConv sumber masalahnya: ia tumpang tindih dengan koneksi residual ResNet dan mengganggu pola konkatenasi DenseNet, sehingga mengurangi keberagaman gradien antarpeta fitur dan menurunkan akurasi. Aturan yang diusulkan — reparameterisasi terencana (*planned re-parameterization*) — berbunyi sederhana: bila lapis konvolusi berada pada koneksi residual atau konkatenasi, pakai RepConvN (RepConv tanpa cabang identitas); RepConv penuh hanya untuk arsitektur polos.

Struktur RepConvN saat pelatihan dan hasil peleburannya saat inferensi:

```
saat pelatihan (dua cabang)          saat inferensi (dilebur)

        masukan                             masukan
      ┌────┴─────┐                              │
      ▼          ▼                              ▼
 ┌─────────┐ ┌─────────┐                 ┌─────────────┐
 │ conv 3x3│ │ conv 1x1│                 │ satu conv   │
 │  + BN   │ │  + BN   │                 │ 3x3 + bias  │
 └────┬────┘ └────┬────┘                 └──────┬──────┘
      └─────┬─────┘                             │
            ▼                                   ▼
      dijumlahkan                           keluaran
            │
            ▼
        keluaran

cabang identitas sengaja dibuang (RepConvN) pada lapis
yang memiliki koneksi residual atau konkatenasi
```

### Penetapan Label Coarse-to-Fine dengan Kepala Bantu

Makalah ini menamai kepala penghasil keluaran akhir sebagai *lead head* dan kepala bantu *deep supervision* sebagai *auxiliary head*; kepala bantu dibuang setelah pelatihan. Masalahnya ada pada penetapan target. Detektor modern memakai *label assigner*: mekanisme yang menghitung label lunak (*soft label*) dari gabungan prediksi jaringan dan *ground truth* — misalnya target skor keberadaan objek diset sebesar IoU (rasio luas irisan terhadap gabungan dua kotak) antara kotak prediksi dan kotak benar. Dengan dua kepala, praktik lazim saat itu adalah tiap kepala menghitung labelnya sendiri secara independen.

Strategi pertama, *lead head guided label assigner*: label lunak dihitung dari prediksi *lead head* dan *ground truth*, lalu dipakai melatih kedua kepala sekaligus. Alasannya, *lead head* lebih dalam sehingga prediksinya lebih mewakili data; kepala bantu yang dangkal mempelajari informasi yang sudah dikuasai *lead head*, sedangkan *lead head* memusatkan diri pada informasi sisa.

Strategi kedua, yang dipakai pada model final, adalah *coarse-to-fine lead head guided label assigner*. Label halus (*fine*) untuk *lead head* dibuat seperti strategi pertama; label kasar (*coarse*) untuk *auxiliary head* dibuat dengan melonggarkan syarat penetapan sampel positif, sehingga lebih banyak sel grid (sel pada peta fitur keluaran) dianggap positif dan *recall* (proporsi objek yang ditemukan) kepala bantu naik. Agar label kasar tidak merusak prior prediksi akhir, keluaran kepala bantu diberi batas atas: grid positif kasar tambahan tidak dapat menghasilkan label lunak sempurna karena skornya dibatasi menurut jarak ke pusat objek. Dengan begitu, batas optimasi label halus selalu lebih tinggi daripada label kasar.

### Bag-of-Freebies Lainnya

Tiga teknik tambahan melengkapi paket tanpa biaya inferensi. Pertama, fusi *batch normalization* (BN — normalisasi statistik tiap kanal terhadap rata-rata dan varians mini-batch): saat inferensi, parameter BN dilebur ke bobot dan bias lapis konvolusi yang bersebelahan. Kedua, pengetahuan implisit dari YOLOR: vektor yang saat pelatihan digabungkan dengan peta fitur konvolusi; saat inferensi vektor ini diprahitung dan dilebur ke bias atau bobot konvolusi di dekatnya. Ketiga, model *EMA* (*exponential moving average*): bobot inferensi diambil dari rata-rata bergerak eksponensial bobot selama pelatihan.

## Eksperimen dan Hasil

Seluruh eksperimen memakai MS COCO: *train2017* untuk pelatihan, *val2017* untuk verifikasi, dan *test-dev* (split uji resmi) untuk perbandingan akhir. AP dilaporkan menurut protokol COCO: rata-rata presisi pada ambang IoU 0,50–0,95. Tiga model dasar dirancang untuk tiga kelas perangkat: YOLOv7-tiny untuk GPU tepi (fungsi aktivasi *leaky ReLU*), YOLOv7 untuk GPU umum (aktivasi *SiLU*), dan YOLOv7-W6 untuk GPU *cloud*; varian lain diperoleh lewat penskalaan. Hasil utama pada resolusi 640:

- YOLOv7: 36,9 juta parameter, 104,7 GFLOPs (miliar operasi floating-point per citra, ukuran biaya komputasi), 161 FPS, 51,4% AP *test-dev*. Dibandingkan YOLOR-CSP (52,9 juta parameter, 120,4 GFLOPs, 106 FPS, 51,1% AP), model ini memangkas 43% parameter dan 15% komputasi sekaligus 55 FPS lebih cepat dengan AP sedikit lebih tinggi — paket *bag-of-freebies* hadir bersama arsitektur yang lebih hemat.
- YOLOv7-tiny-SiLU: 6,2 juta parameter, 286 FPS, 38,7% AP — 127 FPS lebih cepat dan 10,7 poin AP lebih tinggi daripada YOLOv5-N r6.1 (159 FPS, 28,0% AP *val*). Selisih ini menunjukkan perbaikan arsitektur paling terasa pada model kecil dengan anggaran komputasi sempit.
- YOLOv7-X: 53,1% AP pada 114 FPS; dibandingkan YOLOv5-X r6.1 (50,7% AP *val*, 83 FPS), ia 31 FPS lebih cepat dengan 22% parameter dan 8% komputasi lebih sedikit.

Pada resolusi 1280, YOLOv7-E6 mencapai 55,9% AP *val* pada 56 FPS; detektor transformer (detektor berbasis arsitektur atensi) SWIN-L Cascade Mask R-CNN mencapai 53,9% AP pada 9,2 FPS (GPU A100), sehingga YOLOv7-E6 unggul 2 poin AP sekaligus sekitar enam kali lebih cepat. YOLOv7-E6E mencapai 56,8% AP pada 36 FPS; dibandingkan YOLOR-D6 (56,5% AP *test*, 34 FPS) yang berparameter sama (151,7 juta), E6E memakai komputasi lebih rendah (843,2 lawan 935,6 GFLOPs) dengan AP 0,3 poin lebih tinggi — keuntungan datang dari desain, bukan penambahan ukuran.

Studi ablasi mengonfirmasi tiap komponen. Penskalaan gabungan memberi AP 0,5 poin lebih tinggi daripada penskalaan lebar saja, dengan parameter dan komputasi lebih kecil. Reparameterisasi terencana menghasilkan AP tertinggi pada model konkatenasi (3-stacked ELAN) maupun residual (CSPDarknet, *backbone* keluarga Darknet) dibanding RepConv biasa. Penambahan *loss* (fungsi galat yang diminimalkan saat pelatihan) bantu selalu menaikkan AP, dan strategi *coarse-to-fine* mengungguli penetapan independen maupun *lead-guided* biasa. Ketiga uji ini menunjukkan tiap klaim kontribusi berdiri sendiri.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini adalah efisiensi bukti: akurasi naik nyaris tanpa biaya inferensi karena seluruh struktur tambahan dilebur atau dibuang, cakupan variannya luas (5–160 FPS), dan pelatihan serta kode resminya terbuka untuk direproduksi dari awal tanpa data eksternal.

Keterbatasan berikut merupakan analisis penulis bab, bukan pernyataan penulis makalah. Dari sisi rekayasa, resep pelatihannya lebih kompleks daripada pendahulunya: dua kepala, dua set label, dan modul yang harus dilebur ulang lewat prosedur reparameterisasi terpisah sebelum dipakai. Dari sisi rekayasa pula, perbandingan kecepatan kelas berat dilakukan lintas GPU (V100 untuk YOLOv7, A100 untuk pembanding transformer), sehingga selisihnya tidak sepenuhnya setara. Secara konseptual, model utama tetap memakai kepala deteksi berbasis *anchor* (kotak acuan berukuran tetap yang menjadi titik tolak regresi posisi objek) dan masih memerlukan *Non-Maximum Suppression* (NMS — pembuangan kotak ganda yang tumpang tindih); varian *anchor-free* (u6) disediakan repositori, tetapi di luar hasil utama makalah.

## Kaitan dengan Bab Lain

Bab ini melanjutkan langsung resep [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md): konsep *bag-of-freebies* diperluas dari kumpulan trik pelatihan menjadi paket terstruktur yang mencakup arsitektur, reparameterisasi, dan penetapan label. Terhadap [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) dan [bab 006 (YOLOv6)](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md), YOLOv7 berperan sebagai koreksi sekaligus kelanjutan: penetapan label dinamis dan reparameterisasi struktural yang dipopulerkan kedua bab itu dianalisis ulang lalu diberi aturan pakai yang aman. Sebaliknya, [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md) menjadikan hasil bab ini garis dasar perbandingan utama pada kelas detektor *real-time*. Fondasi satu tahapnya mewarisi [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md): regresi langsung dari citra ke kotak objek dalam satu evaluasi.

## Poin untuk Sitasi

Kutip dengan kunci `wang2023yolov7`. Ringkasan yang aman dikutip: "YOLOv7 memperkenalkan *trainable bag-of-freebies* — paket teknik pelatihan yang menaikkan akurasi tanpa menambah biaya inferensi — melalui blok E-ELAN, reparameterisasi terencana, dan penetapan label *coarse-to-fine*; varian E6E-nya mencapai 56,8% AP COCO pada 36 FPS (GPU V100), akurasi tertinggi di antara detektor *real-time* minimal 30 FPS saat terbit, dan seluruh model dilatih dari awal hanya pada MS COCO."

Catatan verifikasi: tabel ablasi lengkap (Tabel 3–8 naskah) tidak terrender pada sumber HTML; angka ablasi di sini (kedalaman ×1,5, lebar ×1,25, +0,5 poin AP) berasal dari teks naskah — cocokkan ke tabel PDF sebelum sitasi formal. Klaim kecepatan kelas berat diukur lintas GPU (V100 lawan A100); kutip beserta konteksnya. Pernyataan bahwa model utama berbasis *anchor* dan memerlukan NMS diverifikasi dari repositori kode resmi, bukan dari naskah.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Figure 1: Comparison with other real-time object detectors, our proposed methods achieve state-of-the-arts performance.

opment of MCUNet [49, 48] and NanoDet [54] focused on producing low-power single-chip and improving the inference speed on edge CPU. As for methods such as YOLOX [21] and YOLOR [81], they focus on improving the inference speed of various GPUs. More recently, the development of real-time object detector has focused on the design of efficient architecture. As for real-time object detectors that can be used on CPU [54, 88, 84, 83], their design is mostly based on MobileNet [28, 66, 27], ShuffleNet [92, 55], or GhostNet [25]. Another mainstream real-time object detectors are developed for GPU [81, 21, 97], they mostly use ResNet [26], DarkNet [63], or DLA [87], and then use the CSPNet [80] strategy to optimize the architecture. The development direction of the proposed methods in this paper are different from that of the current mainstream real-time object detectors. In addition to architecture optimization, our proposed methods will focus on the optimization of the training process. Our focus will be on some optimized modules and optimization methods which may strengthen the training cost for improving the accuracy of object detection, but without increasing the inference cost. We call the proposed modules and optimization methods trainable bag-of-freebies.

1. Introduction Real-time object detection is a very important topic in computer vision, as it is often a necessary component in computer vision systems. For example, multi-object tracking [94, 93], autonomous driving [40, 18], robotics [35, 58], medical image analysis [34, 46], etc. The computing devices that execute real-time object detection is usually some mobile CPU or GPU, as well as various neural processing units (NPU) developed by major manufacturers. For example, the Apple neural engine (Apple), the neural compute stick (Intel), Jetson AI edge devices (Nvidia), the edge TPU (Google), the neural processing engine (Qualcomm), the AI processing unit (MediaTek), and the AI SoCs (Kneron), are all NPUs. Some of the above mentioned edge devices focus on speeding up different operations such as vanilla convolution, depth-wise convolution, or MLP operations. In this paper, the real-time object detector we proposed mainly hopes that it can support both mobile GPU and GPU devices from the edge to the cloud. In recent years, the real-time object detector is still developed for different edge device. For example, the devel1

2.2. Model re-parameterization

Recently, model re-parameterization [13, 12, 29] and dynamic label assignment [20, 17, 42] have become important topics in network training and object detection. Mainly after the above new concepts are proposed, the training of object detector evolves many new issues. In this paper, we will present some of the new issues we have discovered and devise effective methods to address them. For model reparameterization, we analyze the model re-parameterization strategies applicable to layers in different networks with the concept of gradient propagation path, and propose planned re-parameterized model. In addition, when we discover that with dynamic label assignment technology, the training of model with multiple output layers will generate new issues. That is: “How to assign dynamic targets for the outputs of different branches?” For this problem, we propose a new label assignment method called coarse-to-fine lead guided label assignment. The contributions of this paper are summarized as follows: (1) we design several trainable bag-of-freebies methods, so that real-time object detection can greatly improve the detection accuracy without increasing the inference cost; (2) for the evolution of object detection methods, we found two new issues, namely how re-parameterized module replaces original module, and how dynamic label assignment strategy deals with assignment to different output layers. In addition, we also propose methods to address the difficulties arising from these issues; (3) we propose “extend” and “compound scaling” methods for the real-time object detector that can effectively utilize parameters and computation; and (4) the method we proposed can effectively reduce about 40% parameters and 50% computation of state-of-the-art real-time object detector, and has faster inference speed and higher detection accuracy.

Model re-parametrization techniques [71, 31, 75, 19, 33, 11, 4, 24, 13, 12, 10, 29, 14, 78] merge multiple computational modules into one at inference stage. The model re-parameterization technique can be regarded as an ensemble technique, and we can divide it into two categories, i.e., module-level ensemble and model-level ensemble. There are two common practices for model-level reparameterization to obtain the final inference model. One is to train multiple identical models with different training data, and then average the weights of multiple trained models. The other is to perform a weighted average of the weights of models at different iteration number. Modulelevel re-parameterization is a more popular research issue recently. This type of method splits a module into multiple identical or different module branches during training and integrates multiple branched modules into a completely equivalent module during inference. However, not all proposed re-parameterized module can be perfectly applied to different architectures. With this in mind, we have developed new re-parameterization module and designed related application strategies for various architectures.

2.3. Model scaling Model scaling [72, 60, 74, 73, 15, 16, 2, 51] is a way to scale up or down an already designed model and make it fit in different computing devices. The model scaling method usually uses different scaling factors, such as resolution (size of input image), depth (number of layer), width (number of channel), and stage (number of feature pyramid), so as to achieve a good trade-off for the amount of network parameters, computation, inference speed, and accuracy. Network architecture search (NAS) is one of the commonly used model scaling methods. NAS can automatically search for suitable scaling factors from search space without defining too complicated rules. The disadvantage of NAS is that it requires very expensive computation to complete the search for model scaling factors. In [15], the researcher analyzes the relationship between scaling factors and the amount of parameters and operations, trying to directly estimate some rules, and thereby obtain the scaling factors required by model scaling. Checking the literature, we found that almost all model scaling methods analyze individual scaling factor independently, and even the methods in the compound scaling category also optimized scaling factor independently. The reason for this is because most popular NAS architectures deal with scaling factors that are not very correlated. We observed that all concatenationbased models, such as DenseNet [32] or VoVNet [39], will change the input width of some layers when the depth of such models is scaled. Since the proposed architecture is concatenation-based, we have to design a new compound scaling method for this model.

Figure 2: Extended efficient layer aggregation networks. The proposed extended ELAN (E-ELAN) does not change the gradient transmission path of the original architecture at all, but use group convolution to increase the cardinality of the added features, and combine the features of different groups in a shuffle and merge cardinality manner. This way of operation can enhance the features learned by different feature maps and improve the use of parameters and calculations.

3. Architecture

E-ELAN uses expand, shuffle, merge cardinality to achieve the ability to continuously enhance the learning ability of the network without destroying the original gradient path. In terms of architecture, E-ELAN only changes the architecture in computational block, while the architecture of transition layer is completely unchanged. Our strategy is to use group convolution to expand the channel and cardinality of computational blocks. We will apply the same group parameter and channel multiplier to all the computational blocks of a computational layer. Then, the feature map calculated by each computational block will be shuffled into g groups according to the set group parameter g, and then concatenate them together. At this time, the number of channels in each group of feature map will be the same as the number of channels in the original architecture. Finally, we add g groups of feature maps to perform merge cardinality. In addition to maintaining the original ELAN design architecture, E-ELAN can also guide different groups of computational blocks to learn more diverse features.

3.1. Extended efficient layer aggregation networks In most of the literature on designing the efficient architectures, the main considerations are no more than the number of parameters, the amount of computation, and the computational density. Starting from the characteristics of memory access cost, Ma et al. [55] also analyzed the influence of the input/output channel ratio, the number of branches of the architecture, and the element-wise operation on the network inference speed. Dollár et al. [15] additionally considered activation when performing model scaling, that is, to put more consideration on the number of elements in the output tensors of convolutional layers. The design of CSPVoVNet [79] in Figure 2 (b) is a variation of VoVNet [39]. In addition to considering the aforementioned basic designing concerns, the architecture of CSPVoVNet [79] also analyzes the gradient path, in order to enable the weights of different layers to learn more diverse features. The gradient analysis approach described above makes inferences faster and more accurate. ELAN [1] in Figure 2 (c) considers the following design strategy – “How to design an efficient network?.” They came out with a conclusion: By controlling the shortest longest gradient path, a deeper network can learn and converge effectively. In this paper, we propose Extended-ELAN (E-ELAN) based on ELAN and its main architecture is shown in Figure 2 (d).

3.2. Model scaling for concatenation-based models The main purpose of model scaling is to adjust some attributes of the model and generate models of different scales to meet the needs of different inference speeds. For example the scaling model of EfficientNet [72] considers the width, depth, and resolution. As for the scaled-YOLOv4 [79], its scaling model is to adjust the number of stages. In [15], Dollár et al. analyzed the influence of vanilla convolution and group convolution on the amount of parameter and computation when performing width and depth scaling, and used this to design the corresponding model scaling method.

Regardless of the gradient path length and the stacking number of computational blocks in large-scale ELAN, it has reached a stable state. If more computational blocks are stacked unlimitedly, this stable state may be destroyed, and the parameter utilization rate will decrease. The proposed 3

Figure 3: Model scaling for concatenation-based models. From (a) to (b), we observe that when depth scaling is performed on concatenation-based models, the output width of a computational block also increases. This phenomenon will cause the input width of the subsequent transmission layer to increase. Therefore, we propose (c), that is, when performing model scaling on concatenationbased models, only the depth in a computational block needs to be scaled, and the remaining of transmission layer is performed with corresponding width scaling.

The above methods are mainly used in architectures such as PlainNet or ResNet. When these architectures are in executing scaling up or scaling down, the in-degree and out-degree of each layer will not change, so we can independently analyze the impact of each scaling factor on the amount of parameters and computation. However, if these methods are applied to the concatenation-based architecture, we will find that when scaling up or scaling down is performed on depth, the in-degree of a translation layer which is immediately after a concatenation-based computational block will decrease or increase, as shown in Figure 3 (a) and (b). It can be inferred from the above phenomenon that we cannot analyze different scaling factors separately for a concatenation-based model but must be considered together. Take scaling-up depth as an example, such an action will cause a ratio change between the input channel and output channel of a transition layer, which may lead to a decrease in the hardware usage of the model. Therefore, we must propose the corresponding compound model scaling method for a concatenation-based model. When we scale the depth factor of a computational block, we must also calculate the change of the output channel of that block. Then, we will perform width factor scaling with the same amount of change on the transition layers, and the result is shown in Figure 3 (c). Our proposed compound scaling method can maintain the properties that the model had at the initial design and maintains the optimal structure.

Figure 4: Planned re-parameterized model. In the proposed planned re-parameterized model, we found that a layer with residual or concatenation connections, its RepConv should not have identity connection. Under these circumstances, it can be replaced by RepConvN that contains no identity connections.

RepConv actually combines 3 × 3 convolution, 1 × 1 convolution, and identity connection in one convolutional layer. After analyzing the combination and corresponding performance of RepConv and different architectures, we find that the identity connection in RepConv destroys the residual in ResNet and the concatenation in DenseNet, which provides more diversity of gradients for different feature maps. For the above reasons, we use RepConv without identity connection (RepConvN) to design the architecture of planned re-parameterized convolution. In our thinking, when a convolutional layer with residual or concatenation is replaced by re-parameterized convolution, there should be no identity connection. Figure 4 shows an example of our designed “planned re-parameterized convolution” used in PlainNet and ResNet. As for the complete planned re-parameterized convolution experiment in residual-based model and concatenation-based model, it will be presented in the ablation study session.

4. Trainable bag-of-freebies 4.1. Planned re-parameterized convolution Although RepConv [13] has achieved excellent performance on the VGG [68], when we directly apply it to ResNet [26] and DenseNet [32] and other architectures, its accuracy will be significantly reduced. We use gradient flow propagation paths to analyze how re-parameterized convolution should be combined with different network. We also designed planned re-parameterized convolution accordingly. 4

Figure 5: Coarse for auxiliary and fine for lead head label assigner. Compare with normal model (a), the schema in (b) has auxiliary head. Different from the usual independent label assigner (c), we propose (d) lead head guided label assigner and (e) coarse-to-fine lead head guided label assigner. The proposed label assigner is optimized by lead head prediction and the ground truth to get the labels of training lead head and auxiliary head at the same time. The detailed coarse-to-fine implementation method and constraint design details will be elaborated in Apendix.

4.2. Coarse for auxiliary and fine for lead loss

to execute label assignment. The method proposed in this paper is a new label assignment method that guides both auxiliary head and lead head by the lead head prediction. In other words, we use lead head prediction as guidance to generate coarse-to-fine hierarchical labels, which are used for auxiliary head and lead head learning, respectively. The two proposed deep supervision label assignment strategies are shown in Figure 5 (d) and (e), respectively.

Deep supervision [38] is a technique that is often used in training deep networks. Its main concept is to add extra auxiliary head in the middle layers of the network, and the shallow network weights with assistant loss as the guide. Even for architectures such as ResNet [26] and DenseNet [32] which usually converge well, deep supervision [70, 98, 67, 47, 82, 65, 86, 50] can still significantly improve the performance of the model on many tasks. Figure 5 (a) and (b) show, respectively, the object detector architecture “without” and “with” deep supervision. In this paper, we call the head responsible for the final output as the lead head, and the head used to assist training is called auxiliary head. Next we want to discuss the issue of label assignment. In the past, in the training of deep network, label assignment usually refers directly to the ground truth and generate hard label according to the given rules. However, in recent years, if we take object detection as an example, researchers often use the quality and distribution of prediction output by the network, and then consider together with the ground truth to use some calculation and optimization methods to generate a reliable soft label [61, 8, 36, 99, 91, 44, 43, 90, 20, 17, 42]. For example, YOLO [61] use IoU of prediction of bounding box regression and ground truth as the soft label of objectness. In this paper, we call the mechanism that considers the network prediction results together with the ground truth and then assigns soft labels as “label assigner.” Deep supervision needs to be trained on the target objectives regardless of the circumstances of auxiliary head or lead head. During the development of soft label assigner related techniques, we accidentally discovered a new derivative issue, i.e., “How to assign soft label to auxiliary head and lead head ?” To the best of our knowledge, the relevant literature has not explored this issue so far. The results of the most popular method at present is as shown in Figure 5 (c), which is to separate auxiliary head and lead head, and then use their own prediction results and the ground truth

Lead head guided label assigner is mainly calculated based on the prediction result of the lead head and the ground truth, and generate soft label through the optimization process. This set of soft labels will be used as the target training model for both auxiliary head and lead head. The reason to do this is because lead head has a relatively strong learning capability, so the soft label generated from it should be more representative of the distribution and correlation between the source data and the target. Furthermore, we can view such learning as a kind of generalized residual learning. By letting the shallower auxiliary head directly learn the information that lead head has learned, lead head will be more able to focus on learning residual information that has not yet been learned. Coarse-to-fine lead head guided label assigner also used the predicted result of the lead head and the ground truth to generate soft label. However, in the process we generate two different sets of soft label, i.e., coarse label and fine label, where fine label is the same as the soft label generated by lead head guided label assigner, and coarse label is generated by allowing more grids to be treated as positive target by relaxing the constraints of the positive sample assignment process. The reason for this is that the learning ability of an auxiliary head is not as strong as that of a lead head, and in order to avoid losing the information that needs to be learned, we will focus on optimizing the recall of auxiliary head in the object detection task. As for the output of lead head, we can filter the high precision results from the high recall results as the final output. However, we must note that if the additional weight of coarse label is close to 5

5. Experiments

that of fine label, it may produce bad prior at final prediction. Therefore, in order to make those extra coarse positive grids have less impact, we put restrictions in the decoder, so that the extra coarse positive grids cannot produce soft label perfectly. The mechanism mentioned above allows the importance of fine label and coarse label to be dynamically adjusted during the learning process, and makes the optimizable upper bound of fine label always higher than coarse label.

5.1. Experimental setup We use Microsoft COCO dataset to conduct experiments and validate our object detection method. All our experiments did not use pre-trained models. That is, all models were trained from scratch. During the development process, we used train 2017 set for training, and then used val 2017 set for verification and choosing hyperparameters. Finally, we show the performance of object detection on the test 2017 set and compare it with the state-of-the-art object detection algorithms. Detailed training parameter settings are described in Appendix. We designed basic model for edge GPU, normal GPU, and cloud GPU, and they are respectively called YOLOv7tiny, YOLOv7, and YOLOv7-W6. At the same time, we also use basic model for model scaling for different service requirements and get different types of models. For YOLOv7, we do stack scaling on neck, and use the proposed compound scaling method to perform scaling-up of the depth and width of the entire model, and use this to obtain YOLOv7-X. As for YOLOv7-W6, we use the newly proposed compound scaling method to obtain YOLOv7-E6 and YOLOv7-D6. In addition, we use the proposed EELAN for YOLOv7-E6, and thereby complete YOLOv7E6E. Since YOLOv7-tiny is an edge GPU-oriented architecture, it will use leaky ReLU as activation function. As for other models we use SiLU as activation function. We will describe the scaling factor of each model in detail in Appendix.

4.3. Other trainable bag-of-freebies In this section we will list some trainable bag-offreebies. These freebies are some of the tricks we used in training, but the original concepts were not proposed by us. The training details of these freebies will be elaborated in the Appendix, including (1) Batch normalization in conv-bn-activation topology: This part mainly connects batch normalization layer directly to convolutional layer. The purpose of this is to integrate the mean and variance of batch normalization into the bias and weight of convolutional layer at the inference stage. (2) Implicit knowledge in YOLOR [81] combined with convolution feature map in addition and multiplication manner: Implicit knowledge in YOLOR can be simplified to a vector by pre-computing at the inference stage. This vector can be combined with the bias and weight of the previous or subsequent convolutional layer. (3) EMA model: EMA is a technique used in mean teacher [75], and in our system we use EMA model purely as the final inference model. 6

Table 2: Comparison of state-of-the-art real-time object detectors. Model

5.2. Baselines

5.3. Comparison with state-of-the-arts

We choose previous version of YOLO [3, 79] and stateof-the-art object detector YOLOR [81] as our baselines. Table 1 shows the comparison of our proposed YOLOv7 models and those baseline that are trained with the same settings. From the results we see that if compared with YOLOv4, YOLOv7 has 75% less parameters, 36% less computation, and brings 1.5% higher AP. If compared with state-of-theart YOLOR-CSP, YOLOv7 has 43% fewer parameters, 15% less computation, and 0.4% higher AP. In the performance of tiny model, compared with YOLOv4-tiny-31, YOLOv7tiny reduces the number of parameters by 39% and the amount of computation by 49%, but maintains the same AP. On the cloud GPU model, our model can still have a higher AP while reducing the number of parameters by 19% and the amount of computation by 33%.

Figure 6: Planned RepConv 3-stacked ELAN. Blue circles are the position we replace Conv by RepConv.

5.4. Ablation study 5.4.1

Table 4: Ablation study on planned RepConcatenation model. Model

Table 3 shows the results obtained when using different model scaling strategies for scaling up. Among them, our proposed compound scaling method is to scale up the depth of computational block by 1.5 times and the width of transition block by 1.25 times. If our method is compared with the method that only scaled up the width, our method can improve the AP by 0.5% with less parameters and amount of computation. If our method is compared with the method that only scales up the depth, our method only needs to increase the number of parameters by 2.9% and the amount of computation by 1.2%, which can improve the AP by 0.2%. It can be seen from the results of Table 3 that our proposed compound scaling strategy can utilize parameters and computation more efficiently.

volution block that conforms to our design strategy, we additionally design a reversed dark block for the experiment, whose architecture is shown in Figure 7. Since the CSPDarknet with dark block and reversed dark block has exactly the same amount of parameters and operations, it is fair to compare. The experiment results illustrated in Table 5 fully confirm that the proposed planned re-parameterized model is equally effective on residual-based model. We find that the design of RepCSPResNet [85] also fit our design pattern.

Table 3: Ablation study on proposed model scaling. Model

Proposed planned re-parameterized model Figure 7: Reversed CSPDarknet. We reverse the position of 1 × 1 and 3 × 3 convolutional layer in dark block to fit our planned reparameterized model design strategy.

In order to verify the generality of our proposed planed re-parameterized model, we use it on concatenation-based model and residual-based model respectively for verification. The concatenation-based model and residual-based model we chose for verification are 3-stacked ELAN and CSPDarknet, respectively. In the experiment of concatenation-based model, we replace the 3 × 3 convolutional layers in different positions in 3-stacked ELAN with RepConv, and the detailed configuration is shown in Figure 6. From the results shown in Table 4 we see that all higher AP values are present on our proposed planned re-parameterized model. In the experiment dealing with residual-based model, since the original dark block does not have a 3 × 3 con-

Table 5: Ablation study on planned RepResidual model. Model

Figure 8: Objectness map predicted by different methods at auxiliary head and lead head.

Since the proposed YOLOv7 uses multiple pyramids to jointly predict object detection results, we can directly connect auxiliary head to the pyramid in the middle layer for training. This type of training can make up for information that may be lost in the next level pyramid prediction. For the above reasons, we designed partial auxiliary head in the proposed E-ELAN architecture. Our approach is to connect auxiliary head after one of the sets of feature map before merging cardinality, and this connection can make the weight of the newly generated set of feature map not directly updated by assistant loss. Our design allows each pyramid of lead head to still get information from objects with different sizes. Table 8 shows the results obtained using two different methods, i.e., coarse-to-fine lead guided and partial coarse-to-fine lead guided methods. Obviously, the partial coarse-to-fine lead guided method has a better auxiliary effect.

In the assistant loss for auxiliary head experiments, we compare the general independent label assignment for lead head and auxiliary head methods, and we also compare the two proposed lead guided label assignment methods. We show all comparison results in Table 6. From the results listed in Table 6, it is clear that any model that increases assistant loss can significantly improve the overall performance. In addition, our proposed lead guided label assignment strategy receives better performance than the general independent label assignment strategy in AP, AP50 , and AP75 . As for our proposed coarse for assistant and fine for lead label assignment strategy, it results in best results in all cases. In Figure 8 we show the objectness map predicted by different methods at auxiliary head and lead head. From Figure 8 we find that if auxiliary head learns lead guided soft label, it will indeed help lead head to extract the residual information from the consistant targets.

Table 6: Ablation study on proposed auxiliary head. Model

In this paper we propose a new architecture of realtime object detector and the corresponding model scaling method. Furthermore, we find that the evolving process of object detection methods generates new research topics. During the research process, we found the replacement problem of re-parameterized module and the allocation problem of dynamic label assignment. To solve the problem, we propose the trainable bag-of-freebies method to enhance the accuracy of object detection. Based on the above, we have developed the YOLOv7 series of object detection systems, which receives the state-of-the-art results.

Table 7: Ablation study on constrained auxiliary head. Size

6. Conclusions

In Table 7 we further analyze the effect of the proposed coarse-to-fine lead guided label assignment method on the decoder of auxiliary head. That is, we compared the results of with/without the introduction of upper bound constraint. Judging from the numbers in the Table, the method of constraining the upper bound of objectness by the distance from the center of the object can achieve better performance.

7. Acknowledgements The authors wish to thank National Center for Highperformance Computing (NCHC) for providing computational and storage resources. 9

8. More comparison

and convolutional-based detector ConvNeXt-XL CascadeMask R-CNN (8.6 FPS A100, 55.2% AP) by 551% in speed and 0.7% AP in accuracy, as well as YOLOv7 outperforms: YOLOR, YOLOX, Scaled-YOLOv4, YOLOv5, DETR, Deformable DETR, DINO-5scale-R50, ViT-Adapter-B and many other object detectors in speed and accuracy. More over, we train YOLOv7 only on MS COCO dataset from scratch without using any other datasets or pre-trained weights.

Figure 10: Comparison with other real-time object detectors. Table 10: Comparison of different setting. Model YOLOv7-X YOLOv7-X YOLOv7-X YOLOv7-X improvement

get higher AP when set higher IoU threshold.

Figure 11: Comparison with other real-time object detectors.
