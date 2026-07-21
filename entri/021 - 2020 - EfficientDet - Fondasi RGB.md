# 021 - EfficientDet: Scalable and Efficient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tan2020efficientdet` |
| Judul asli | EfficientDet: Scalable and Efficient Object Detection |
| Penulis | Mingxing Tan, Ruoming Pang, Quoc V. Le (Google Research, Brain Team) |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1911.09070
- **Kode sumber resmi:** https://github.com/google/automl/tree/master/efficientdet
- **Google Scholar:** https://scholar.google.com/scholar?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan EfficientDet, sebuah keluarga detektor objek satu tahap (*one-stage*, tanpa tahap pengusulan wilayah) yang dirancang dengan dua prinsip: fusi fitur multi-skala yang efisien dan penskalaan model yang terkoordinasi. Kontribusi pertamanya adalah BiFPN (*bi-directional feature pyramid network*), modul penggabung fitur lintas skala yang mengalirkan informasi dua arah (atas ke bawah dan bawah ke atas) dan memberi setiap masukan bobot yang dipelajari. Kontribusi keduanya adalah *compound scaling*: satu koefisien φ yang menskalakan resolusi masukan, kedalaman, dan lebar seluruh komponen detektor secara serentak.

Hasilnya adalah delapan model bernama EfficientDet-D0 sampai D7 (ditambah varian D7x) yang mencakup rentang biaya 2,5 miliar hingga 410 miliar FLOPs (*floating-point operations*, jumlah operasi kali-tambah per citra). Model terkecil, D0, menandingi akurasi YOLOv3 dengan 28 kali lebih sedikit FLOPs. Model terbesar mencapai 55,1 AP pada COCO *test-dev* — akurasi terbaik pada masanya — dengan 77 juta parameter, 2,7 kali lebih kecil dan 7,4 kali lebih hemat FLOPs daripada detektor terbaik sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Menjelang 2020, peningkatan akurasi detektor objek dibayar dengan biaya komputasi yang terus naik. Detektor berbasis AmoebaNet dan NAS-FPN (pencari arsitektur piramida fitur secara otomatis) memerlukan 167 juta parameter dan 3045 miliar FLOPs, sekitar 30 kali lipat RetinaNet, demi akurasi tertinggi pada COCO. Ukuran dan latensi sebesar itu menyulitkan penerapan pada robotika dan kendaraan otonom. Upaya efisiensi yang sudah ada — detektor satu tahap, detektor *anchor-free* (tanpa kotak acuan), atau kompresi model — umumnya mengorbankan akurasi dan hanya menyasar satu rentang sumber daya tertentu.

Penulis mengidentifikasi dua kelemahan spesifik pada desain yang berlaku. Pertama, fusi fitur multi-skala. FPN (*feature pyramid network*, piramida fitur) menggabungkan fitur dari berbagai resolusi hanya ke satu arah, dari skala kasar ke skala halus, dan menjumlahkan semua fitur masukan tanpa pembeda; padahal fitur pada resolusi berbeda tidak memberi kontribusi yang sama besar. PANet memperbaiki arah aliran dengan menambah jalur bawah ke atas, tetapi tetap menjumlahkan fitur secara setara. NAS-FPN mencari topologi fusi secara otomatis, tetapi memerlukan ribuan jam GPU dan menghasilkan struktur tak beraturan yang sukar ditafsirkan. Kedua, penskalaan model. Detektor lazim diperbesar hanya dengan mengganti *backbone* (jaringan pengekstrak fitur awal) yang lebih besar atau menaikkan resolusi masukan, tanpa menyentuh jaringan fitur dan jaringan prediksi. Penskalaan satu dimensi seperti ini terbukti tidak efisien.

## Ide Utama

Gagasan pertama makalah ini: fusi fitur multi-skala sebaiknya dipandang sebagai masalah pembobotan yang dapat dipelajari. Setiap fitur masukan diberi satu bobot skalar; jaringan mempelajari bobot itu selama pelatihan, sehingga fitur yang lebih berguna mendapat porsi lebih besar pada keluaran. Aliran informasi dibuat dua arah dan blok fusi diulang beberapa kali agar fitur bercampur lebih dalam.

Gagasan kedua: ukuran model sebaiknya tidak diskalakan per komponen, melainkan lewat satu koefisien φ yang menaikkan resolusi masukan, kedalaman dan lebar *backbone*, jaringan fitur (BiFPN), dan jaringan prediksi secara bersamaan. Prinsip ini diadaptasi dari EfficientNet — keluarga pengklasifikasi citra yang menskalakan lebar, kedalaman, dan resolusi secara gabungan — dan EfficientNet pula yang dipakai sebagai *backbone*. Dari satu baseline φ = 0, menaikkan φ satu per satu menghasilkan keluarga D0 sampai D7 untuk anggaran komputasi yang berbeda-beda.

## Cara Kerja Langkah demi Langkah

### Backbone dan Fitur Multi-Skala

Detektor menerima citra masukan, lalu *backbone* EfficientNet (varian B0–B7 yang telah dilatih sebelumnya pada ImageNet) menghasilkan fitur pada lima tingkat resolusi, dinamai P3 sampai P7. Fitur P_i memiliki resolusi 1/2^i dari citra masukan. Pada masukan 640×640 piksel, P3 berukuran 80×80 (640/2³) dan P7 berukuran 5×5 (640/2⁷). Fitur resolusi tinggi seperti P3 peka terhadap objek kecil; fitur resolusi rendah seperti P7 membawa konteks objek besar.

### Struktur BiFPN

BiFPN menggabungkan kelima tingkat fitur melalui dua jalur. Jalur *top-down* mengalirkan informasi dari P7 ke P3: fitur kasar di-*resize* (diperbesar) lalu digabung dengan fitur halus satu tingkat di bawahnya. Jalur *bottom-up* mengalirkan informasi sebaliknya, dari P3 ke P7, dengan pengecilan resolusi. Dibanding PANet, tiga penyederhanaan dilakukan: (1) simpul yang hanya memiliki satu sisi masukan dibuang, karena tanpa fusi ia hampir tidak berkontribusi; (2) ditambah sisi pintas dari fitur masukan asli ke simpul keluaran pada tingkat yang sama, sehingga lebih banyak fitur tergabung dengan biaya kecil; (3) satu pasang jalur atas-bawah diperlakukan sebagai satu lapis, dan lapis ini diulang beberapa kali. Hasilnya adalah topologi teratur yang dapat ditumpuk, berbeda dengan topologi tak beraturan keluaran NAS-FPN.

Alur keseluruhan detektor dirangkum pada diagram berikut:

```
citra R x R ──► ┌──────────────┐
                │  backbone    │
                │ EfficientNet │
                └──────┬───────┘
        P3    P4    P5    P6    P7     <- P_i: resolusi R/2^i
        │     │     │     │     │
   ┌────▼─────▼─────▼─────▼─────▼─────┐
   │  BiFPN (diulang D = 3+phi kali)  │
   │   top-down:  P7 ► P6 ► P5 ► P4 ► P3
   │   bottom-up: P3 ► P4 ► P5 ► P6 ► P7
   │   tiap fusi: O = Σ wi·Ii/(ε+Σwj) │
   └────┬─────────────────────────────┘
        ▼
   head kelas + head box (bobot dibagi antar-level)
        ▼
   prediksi: kelas + bounding box tiap anchor
```

### Fusi Terbobot

Pada setiap simpul fusi, fitur-fitur masukan tidak dijumlah mentah, melainkan dikalikan bobot lalu dinormalisasi. Penulis menguji tiga skema. Fusi tak berbatas (O = Σ w_i·I_i) berisiko membuat pelatihan tidak stabil karena bobot bebas membesar. Fusi berbasis *softmax* membatasi bobot ke rentang 0–1, tetapi operasi softmax menambah latensi berarti pada GPU. Skema yang dipilih adalah fusi ternormalisasi cepat: O = Σ w_i·I_i / (ε + Σ w_j), dengan w_i ≥ 0 dijamin oleh fungsi ReLU (penyearah yang memetakan nilai negatif ke nol) dan ε = 0,0001 untuk mencegah pembagian nol. Sebagai contoh numerik, bila dua fitur masukan memiliki bobot 2 dan 1, keluarannya adalah 2/3 kali fitur pertama ditambah 1/3 kali fitur kedua. Skema ini mencapai akurasi setara softmax tetapi berjalan 1,26–1,31 kali lebih cepat pada GPU. Setiap fusi memakai konvolusi terpisah-per-kedalaman (*depthwise separable convolution*), yaitu konvolusi yang memproses tiap kanal secara terpisah sebelum menggabungkannya, sehingga biayanya jauh lebih murah dari konvolusi biasa.

### Compound Scaling

Satu koefisien φ mengatur seluruh dimensi model. Lebar BiFPN (jumlah kanal) tumbuh eksponensial, W = 64·(1,35^φ); kedalamannya tumbuh linier, D = 3+φ; kedalaman jaringan prediksi kotak/kelas mengikuti 3+⌊φ/3⌋; resolusi masukan naik 128 piksel per tingkat, R = 512+128φ (kelipatan 128 diperlukan karena fitur terkasar berukuran 1/128 masukan). Faktor 1,35 dipilih lewat pencarian grid pada enam kandidat nilai. Pada φ = 3 diperoleh D3: 6 lapis BiFPN selebar 64·1,35³ ≈ 157 kanal, resolusi masukan 896×896. *Backbone* mengikuti koefisien EfficientNet B0 sampai B6 agar bobot pralatih ImageNet dapat dipakai ulang. D7x menambah satu tingkat fitur (P3–P8) dan *backbone* lebih besar pada resolusi yang sama dengan D7.

### Kepala Prediksi dan Pelatihan

Fitur keluaran BiFPN diteruskan ke dua kepala: pengklasifikasi kelas dan peramalan *bounding box* (kotak pembatas objek). Seperti RetinaNet, bobot kedua kepala dibagi di seluruh tingkat fitur, dan prediksi dilakukan relatif terhadap *anchor* (kotak acuan dengan rasio aspek tetap; di sini {1/2, 1, 2}). Pelatihan pada COCO 2017 (118 ribu citra) memakai *focal loss* — fungsi galat yang menekan kontribusi contoh mudah agar model fokus pada contoh sulit — dengan α = 0,25 dan γ = 1,5, selama 300 *epoch* untuk D0–D6 dan 600 *epoch* untuk D7/D7x pada TPUv3. Evaluasi memakai *soft-NMS*, varian penekanan duplikat deteksi yang menurunkan skor alih-alih membuang kotak yang tumpang tindih.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada COCO 2017 dengan metrik AP (*average precision*; rata-rata presisi pada berbagai ambang tumpang tindih, semakin tinggi semakin baik), dilaporkan pada himpunan validasi (5 ribu citra) dan *test-dev* (20 ribu citra tanpa kebenaran dasar publik). Semua hasil memakai satu model dan satu skala uji.

Hasil kunci dan interpretasinya:

- D0 (512×512): 34,6 AP *test-dev*, 3,9 juta parameter, 2,5 miliar FLOPs. YOLOv3 pada perbandingan yang sama mencapai 33,0 AP dengan 71 miliar FLOPs — akurasi D0 lebih tinggi dengan 28 kali lebih sedikit komputasi.
- D1 (640×640): 40,5 AP dengan 6,6 juta parameter dan 6,1 miliar FLOPs, melawan RetinaNet-R50 39,2 AP dengan 34 juta parameter dan 97 miliar FLOPs — sekitar 5 kali lebih kecil dan 16 kali lebih hemat.
- D7 (1536×1536): 53,7 AP dengan 52 juta parameter dan 325 miliar FLOPs; D7x: 55,1 AP, 77 juta parameter, 410 miliar FLOPs. Detektor terbaik sebelumnya, AmoebaNet + NAS-FPN, mencapai 50,7 AP validasi dengan 209 juta parameter dan 3045 miliar FLOPs — D7x melampauinya 4 poin AP dengan biaya komputasi 7,4 kali lebih rendah.
- Latensi terukur (ukuran batch 1, perangkat keras sama): keluarga EfficientDet berjalan hingga 4,1 kali lebih cepat pada GPU dan 10,8 kali lebih cepat pada CPU dibanding pesaing berakurasi setara.

Studi ablasi memisahkan sumbangan tiap komponen. Mulai dari RetinaNet standar (ResNet-50 + FPN), mengganti *backbone* dengan EfficientNet-B3 menambah sekitar 3 AP dengan biaya yang sedikit lebih rendah; mengganti FPN dengan BiFPN menambah sekitar 4 AP lagi sekaligus mengurangi parameter dan FLOPs. Perbandingan antar-jaringan fitur menunjukkan BiFPN terbobot mengungguli FPN, PANet berulang, dan NAS-FPN pada akurasi sekaligus biaya. Sebagai uji transfer, varian segmentasi citra pada PASCAL VOC 2012 mencapai 81,74% mIoU (rata-rata irisan-per-gabungan per piksel), 1,7 poin di atas DeepLabV3+ dengan 9,8 kali lebih sedikit FLOPs.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah efisiensi yang konsisten di seluruh rentang biaya: setiap anggota keluarga D0–D7 mengungguli pesaing pada kelas komputasinya, sehingga satu resep arsitektur melayani kebutuhan dari perangkat kecil hingga server. BiFPN juga menawarkan struktur fusi yang teratur dan mudah direplikasi, berbeda dengan keluaran pencarian arsitektur otomatis. Resep *compound scaling* memberikan cara sederhana menaikkan atau menurunkan kapasitas tanpa merancang ulang model.

Keterbatasannya: penskalaan majemuk di sini berbasis heuristik dan diakui penulis belum tentu optimal; lebar *backbone* mengikuti koefisien EfficientNet demi ketersediaan bobot pralatih, bukan hasil optimasi. Pelatihannya mahal — 300 sampai 600 *epoch* dengan ukuran batch besar pada puluhan inti TPUv3 — sehingga reproduksi penuh menuntut sumber daya besar. Dari sisi rekayasa, FLOPs yang rendah tidak otomatis berarti latensi rendah pada semua perangkat keras; angka latensi makalah diukur pada GPU Titan V dan V100 tertentu, dan model terbesar tetap memerlukan ratusan milidetik per citra pada GPU kelas tersebut, jauh dari kebutuhan *real-time*.

## Kaitan dengan Bab Lain

EfficientDet melanjutkan dua garis yang dibahas pada bab-bab sebelumnya. Dari silsilah detektor satu tahap, ia mewarisi formulasi prediksi berbasis *anchor* dan *focal loss* yang juga dipakai YOLOv3 ([bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)); YOLOv3 pula yang menjadi tolok ukur efisiensi pada rezim akurasi rendah dalam makalah ini. Gagasan fusi lintas skala dua arah mengembangkan PANet, yang pada tahun yang sama diadopsi oleh YOLOv4 ([bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)) sebagai *neck*-nya; BiFPN menambahkan pembobotan terlatih dan pengulangan blok di atas gagasan itu. Kerangka *backbone*–*neck*–*head* sebagai tiga komponen yang masing-masing dapat dioptimalkan berguna untuk membaca bab-bab berikutnya, termasuk desain leher piramida pada YOLOX ([bab 005](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)) dan YOLOv7 ([bab 007](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)).

## Poin untuk Sitasi

Kutip dengan kunci `tan2020efficientdet`. Ringkasan yang aman dikutip: "EfficientDet menggabungkan BiFPN — fusi piramida fitur dua arah dengan bobot terlatih — dan *compound scaling* yang menskalakan resolusi, kedalaman, dan lebar seluruh komponen detektor dengan satu koefisien, menghasilkan keluarga D0–D7 yang mencapai akurasi COCO setara atau lebih tinggi dari detektor sebelumnya dengan parameter 4–9 kali lebih sedikit dan FLOPs 13–42 kali lebih rendah." Catatan verifikasi: abstrak arXiv menyebut "D7 mencapai 55,1 AP", tetapi tabel hasil menunjukkan angka 55,1 AP / 77 juta parameter / 410 miliar FLOPs dicapai oleh varian D7x, sedangkan D7 mencapai 53,7 AP — cocokkan penamaan model dengan tabel naskah sebelum mengutip angka spesifik. Angka latensi GPU/CPU bergantung pada perangkat keras dan implementasi; kutip dengan konteks pengukurannya.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract Model efficiency has become increasingly important in computer vision. In this paper, we systematically study neural network architecture design choices for object detection and propose several key optimizations to improve efficiency. First, we propose a weighted bi-directional feature pyramid network (BiFPN), which allows easy and fast multiscale feature fusion; Second, we propose a compound scaling method that uniformly scales the resolution, depth, and width for all backbone, feature network, and box/class prediction networks at the same time. Based on these optimizations and better backbones, we have developed a new family of object detectors, called EfficientDet, which consistently achieve much better efficiency than prior art across a wide spectrum of resource constraints. In particular, with singlemodel and single-scale, our EfficientDet-D7 achieves stateof-the-art 55.1 AP on COCO test-dev with 77M parameters and 410B FLOPs1 , being 4x – 9x smaller and using 13x – 42x fewer FLOPs than previous detectors. Code is available at https://github.com/google/automl/tree/ master/efficientdet.

45 COCO AP

Figure 1: Model FLOPs vs. COCO accuracy – All numbers are for single-model single-scale. Our EfficientDet achieves new state-of-the-art 55.1% COCO AP with much fewer parameters and FLOPs than previous detectors. More studies on different backbones and FPN/NAS-FPN/BiFPN are in Table 4 and 5. Complete results are in Table 2. stage [27, 33, 34, 24] and anchor-free detectors [21, 44, 40], or compress existing models [28, 29]. Although these methods tend to achieve better efficiency, they usually sacrifice accuracy. Moreover, most previous works only focus on a specific or a small range of resource requirements, but the variety of real-world applications, from mobile devices to datacenters, often demand different resource constraints. A natural question is: Is it possible to build a scalable detection architecture with both higher accuracy and better efficiency across a wide spectrum of resource constraints (e.g., from 3B to 300B FLOPs)? This paper aims to tackle this problem by systematically studying various design choices of detector architectures. Based on the onestage detector paradigm, we examine the design choices for backbone, feature fusion, and class/box network, and identify two main challenges: Challenge 1: efficient multi-scale feature fusion – Since introduced in [23], FPN has been widely used for multi-

1. Introduction Tremendous progresses have been made in recent years towards more accurate object detection; meanwhile, stateof-the-art object detectors also become increasingly more expensive. For example, the latest AmoebaNet-based NASFPN detector [45] requires 167M parameters and 3045B FLOPs (30x more than RetinaNet [24]) to achieve state-ofthe-art accuracy. The large model sizes and expensive computation costs deter their deployment in many real-world applications such as robotics and self-driving cars where model size and latency are highly constrained. Given these real-world resource constraints, model efficiency becomes increasingly important for object detection. There have been many previous works aiming to develop more efficient detector architectures, such as one1 Similar to [14, 39], FLOPs denotes number of multiply-adds.

scale feature fusion. Recently, PANet [26], NAS-FPN [10], and other studies [20, 18, 42] have developed more network structures for cross-scale feature fusion. While fusing different input features, most previous works simply sum them up without distinction; however, since these different input features are at different resolutions, we observe they usually contribute to the fused output feature unequally. To address this issue, we propose a simple yet highly effective weighted bi-directional feature pyramid network (BiFPN), which introduces learnable weights to learn the importance of different input features, while repeatedly applying topdown and bottom-up multi-scale feature fusion. Challenge 2: model scaling – While previous works mainly rely on bigger backbone networks [24, 35, 34, 10] or larger input image sizes [13, 45] for higher accuracy, we observe that scaling up feature network and box/class prediction network is also critical when taking into account both accuracy and efficiency. Inspired by recent works [39], we propose a compound scaling method for object detectors, which jointly scales up the resolution/depth/width for all backbone, feature network, box/class prediction network. Finally, we also observe that the recently introduced EfficientNets [39] achieve better efficiency than previous commonly used backbones. Combining EfficientNet backbones with our propose BiFPN and compound scaling, we have developed a new family of object detectors, named EfficientDet, which consistently achieve better accuracy with much fewer parameters and FLOPs than previous object detectors. Figure 1 and Figure 4 show the performance comparison on COCO dataset [25]. Under similar accuracy constraint, our EfficientDet uses 28x fewer FLOPs than YOLOv3 [34], 30x fewer FLOPs than RetinaNet [24], and 19x fewer FLOPs than the recent ResNet based NAS-FPN [10]. In particular, with single-model and single test-time scale, our EfficientDet-D7 achieves state-of-the-art 55.1 AP with 77M parameters and 410B FLOPs, outperforming previous best detector [45] by 4 AP while being 2.7x smaller and using 7.4x fewer FLOPs. Our EfficientDet is also up to 4x to 11x faster on GPU/CPU than previous detectors. With simple modifications, we also demonstrate that our single-model single-scale EfficientDet achieves 81.74% mIOU accuracy with 18B FLOPs on Pascal VOC 2012 semantic segmentation, outperforming DeepLabV3+ [6] by 1.7% better accuracy with 9.8x fewer FLOPs.

have attracted substantial attention due to their efficiency and simplicity [21, 42, 44]. In this paper, we mainly follow the one-stage detector design, and we show it is possible to achieve both better efficiency and higher accuracy with optimized network architectures. Multi-Scale Feature Representations: One of the main difficulties in object detection is to effectively represent and process multi-scale features. Earlier detectors often directly perform predictions based on the pyramidal feature hierarchy extracted from backbone networks [4, 27, 36]. As one of the pioneering works, feature pyramid network (FPN) [23] proposes a top-down pathway to combine multi-scale features. Following this idea, PANet [26] adds an extra bottom-up path aggregation network on top of FPN; STDL [43] proposes a scale-transfer module to exploit cross-scale features; M2det [42] proposes a U-shape module to fuse multi-scale features, and G-FRNet [2] introduces gate units for controlling information flow across features. More recently, NAS-FPN [10] leverages neural architecture search to automatically design feature network topology. Although it achieves better performance, NAS-FPN requires thousands of GPU hours during search, and the resulting feature network is irregular and thus difficult to interpret. In this paper, we aim to optimize multi-scale feature fusion with a more intuitive and principled way. Model Scaling: In order to obtain better accuracy, it is common to scale up a baseline detector by employing bigger backbone networks (e.g., from mobile-size models [38, 16] and ResNet [14], to ResNeXt [41] and AmoebaNet [32]), or increasing input image size (e.g., from 512x512 [24] to 1536x1536 [45]). Some recent works [10, 45] show that increasing the channel size and repeating feature networks can also lead to higher accuracy. These scaling methods mostly focus on single or limited scaling dimensions. Recently, [39] demonstrates remarkable model efficiency for image classification by jointly scaling up network width, depth, and resolution. Our proposed compound scaling method for object detection is mostly inspired by [39].

3. BiFPN In this section, we first formulate the multi-scale feature fusion problem, and then introduce the main ideas for our proposed BiFPN: efficient bidirectional cross-scale connections and weighted feature fusion.

2. Related Work

3.1. Problem Formulation

Figure 2: Feature network design – (a) FPN [23] introduces a top-down pathway to fuse multi-scale features from level 3 to 7 (P3 - P7 ); (b) PANet [26] adds an additional bottom-up pathway on top of FPN; (c) NAS-FPN [10] use neural architecture search to find an irregular feature network topology and then repeatedly apply the same block; (d) is our BiFPN with better accuracy and efficiency trade-offs. Figure 2(a) shows the conventional top-down FPN [23]. It takes level 3-7 input features P~ in = (P3in , ...P7in ), where Piin represents a feature level with resolution of 1/2i of the input images. For instance, if input resolution is 640x640, then P3in represents feature level 3 (640/23 = 80) with resolution 80x80, while P7in represents feature level 7 with resolution 5x5. The conventional FPN aggregates multi-scale features in a top-down manner:

efficiency, this paper proposes several optimizations for cross-scale connections: First, we remove those nodes that only have one input edge. Our intuition is simple: if a node has only one input edge with no feature fusion, then it will have less contribution to feature network that aims at fusing different features. This leads to a simplified bidirectional network; Second, we add an extra edge from the original input to output node if they are at the same level, in order to fuse more features without adding much cost; Third, unlike PANet [26] that only has one top-down and one bottom-up path, we treat each bidirectional (top-down & bottom-up) path as one feature network layer, and repeat the same layer multiple times to enable more high-level feature fusion. Section 4.2 will discuss how to determine the number of layers for different resource constraints using a compound scaling method. With these optimizations, we name the new feature network as bidirectional feature pyramid network (BiFPN), as shown in Figure 2 and 3.

3.3. Weighted Feature Fusion

3.2. Cross-Scale Connections

When fusing features with different resolutions, a common way is to first resize them to the same resolution and then sum them up. Pyramid attention network [22] introduces global self-attention upsampling to recover pixel localization, which is further studied in [10]. All previous methods treat all input features equally without distinction. However, we observe that since different input features are at different resolutions, they usually contribute to the output feature unequally. To address this issue, we propose to add an additional weight for each input, and let the network to learn the importance of each input feature. Based on this idea, we consider three weighted fusion approaches: P Unbounded fusion: O = i wi · Ii , where wi is a

Conventional top-down FPN is inherently limited by the one-way information flow. To address this issue, PANet [26] adds an extra bottom-up path aggregation network, as shown in Figure 2(b). Cross-scale connections are further studied in [20, 18, 42]. Recently, NAS-FPN [10] employs neural architecture search to search for better cross-scale feature network topology, but it requires thousands of GPU hours during search and the found network is irregular and difficult to interpret or modify, as shown in Figure 2(c). By studying the performance and efficiency of these three networks (Table 5), we observe that PANet achieves better accuracy than FPN and NAS-FPN, but with the cost of more parameters and computations. To improve model 3

4.1. EfficientDet Architecture

learnable weight that can be a scalar (per-feature), a vector (per-channel), or a multi-dimensional tensor (per-pixel). We find a scale can achieve comparable accuracy to other approaches with minimal computational costs. However, since the scalar weight is unbounded, it could potentially cause training instability. Therefore, we resort to weight normalization to bound the value range of each weight. P ewi Softmax-based fusion: O = i P wj · Ii . An intuitive je idea is to apply softmax to each weight, such that all weights are normalized to be a probability with value range from 0 to 1, representing the importance of each input. However, as shown in our ablation study in section 6.3, the extra softmax leads to significant slowdown on GPU hardware. To minimize the extra latency cost, we further propose a fast fusion approach. P wi P Fast normalized fusion: O = i · Ii , where + j wj wi ≥ 0 is ensured by applying a Relu after each wi , and = 0.0001 is a small value to avoid numerical instability. Similarly, the value of each normalized weight also falls between 0 and 1, but since there is no softmax operation here, it is much more efficient. Our ablation study shows this fast fusion approach has very similar learning behavior and accuracy as the softmax-based fusion, but runs up to 30% faster on GPUs (Table 6).

Figure 3 shows the overall architecture of EfficientDet, which largely follows the one-stage detectors paradigm [27, 33, 23, 24]. We employ ImageNet-pretrained EfficientNets as the backbone network. Our proposed BiFPN serves as the feature network, which takes level 3-7 features {P3 , P4 , P5 , P6 , P7 } from the backbone network and repeatedly applies top-down and bottom-up bidirectional feature fusion. These fused features are fed to a class and box network to produce object class and bounding box predictions respectively. Similar to [24], the class and box network weights are shared across all levels of features.

4.2. Compound Scaling Aiming at optimizing both accuracy and efficiency, we would like to develop a family of models that can meet a wide spectrum of resource constraints. A key challenge here is how to scale up a baseline EfficientDet model. Previous works mostly scale up a baseline detector by employing bigger backbone networks (e.g., ResNeXt [41] or AmoebaNet [32]), using larger input images, or stacking more FPN layers [10]. These methods are usually ineffective since they only focus on a single or limited scaling dimensions. Recent work [39] shows remarkable performance on image classification by jointly scaling up all dimensions of network width, depth, and input resolution. Inspired by these works [10, 39], we propose a new compound scaling method for object detection, which uses a simple compound coefficient φ to jointly scale up all dimensions of backbone , BiFPN, class/box network, and resolution. Unlike [39], object detectors have much more scaling dimensions than image classification models, so grid search for all dimensions is prohibitive expensive. Therefore, we use a heuristic-based scaling approach, but still follow the main idea of jointly scaling up all dimensions.

Our final BiFPN integrates both the bidirectional crossscale connections and the fast normalized fusion. As a concrete example, here we describe the two fused features at level 6 for BiFPN shown in Figure 2(d):

Backbone network – we reuse the same width/depth scaling coefficients of EfficientNet-B0 to B6 [39] such that we can easily reuse their ImageNet-pretrained checkpoints.

where P6td is the intermediate feature at level 6 on the topdown pathway, and P6out is the output feature at level 6 on the bottom-up pathway. All other features are constructed in a similar manner. Notably, to further improve the efficiency, we use depthwise separable convolution [7, 37] for feature fusion, and add batch normalization and activation after each convolution.

BiFPN network – we linearly increase BiFPN depth Dbif pn (#layers) since depth needs to be rounded to small integers. For BiFPN width Wbif pn (#channels), exponentially grow BiFPN width Wbif pn (#channels) as similar to [39]. Specifically, we perform a grid search on a list of values {1.2, 1.25, 1.3, 1.35, 1.4, 1.45}, and pick the best value 1.35 as the BiFPN width scaling factor. Formally, BiFPN width and depth are scaled with the following equation:

4. EfficientDet Based on our BiFPN, we have developed a new family of detection models named EfficientDet. In this section, we will discuss the network architecture and a new compound scaling method for EfficientDet.

Figure 3: EfficientDet architecture – It employs EfficientNet [39] as the backbone network, BiFPN as the feature network, and shared class/box prediction network. Both BiFPN layers and class/box net layers are repeated multiple times based on different resource constraints as shown in Table 1. early increase the depth (#layers) using equation: Dbox = Dclass = 3 + bφ/3c

Table 1: Scaling configs for EfficientDet D0-D6 – φ is the compound coefficient that controls all other scaling dimensions; BiFPN, box/class net, and input size are scaled up using equation 1, 2, 3 respectively.

2}. During training, we apply horizontal flipping and scale jittering [0.1, 2.0], which randomly rsizes images between 0.1x and 2.0x of the original size before cropping. We apply soft-NMS [3] for eval. For D0-D6, each model is trained for 300 epochs with total batch size 128 on 32 TPUv3 cores, but to push the envelope, we train D7/D7x for 600 epochs on 128 TPUv3 cores. Table 2 compares EfficientDet with other object detectors, under the single-model single-scale settings with no test-time augmentation. We report accuracy for both test-dev (20K test images with no public ground-truth) and val with 5K validation images. Notably, model performance depends on both network architecture and trainning settings (see appendix), but for simplicity, we only reproduce RetinaNet using our trainers and refer other models from their papers. In general, our EfficientDet achieves bet-

5. Experiments 5.1. EfficientDet for Object Detection We evaluate EfficientDet on COCO 2017 detection datasets [25] with 118K training images. Each model is trained using SGD optimizer with momentum 0.9 and weight decay 4e-5. Learning rate is linearly increased from 0 to 0.16 in the first training epoch and then annealed down using cosine decay rule. Synchronized batch norm is added after every convolution with batch norm decay 0.99 and epsilon 1e-3. Same as the [39], we use SiLU (Swish-1) activation [8, 15, 31] and exponential moving average with decay 0.9998. We also employ commonly-used focal loss [24] with α = 0.25 and γ = 1.5, and aspect ratio {1/2, 1, 5

Table 2: EfficientDet performance on COCO [25] – Results are for single-model single-scale. test-dev is the COCO test set and val is the validation set. Params and FLOPs denote the number of parameters and multiply-adds. Latency is for inference with batch size 1. AA denotes auto-augmentation [45]. We group models together if they have similar accuracy, and compare their model size, FLOPs, and latency in each group. ter efficiency than previous detectors, being 4x – 9x smaller and using 13x - 42x less FLOPs across a wide range of accuracy or resource constraints. On relatively low-accuracy regime, our EfficientDet-D0 achieves similar accuracy as YOLOv3 with 28x fewer FLOPs. Compared to RetinaNet [24] and Mask-RCNN [13], our EfficientDet achieves similar accuracy with up to 8x fewer parameters and 21x fewer FLOPs. On high-accuracy regime, our EfficientDet also consistently outperforms recent object detectors [10, 45] with much fewer parameters and FLOPs. In particular, our single-model single-scale EfficientDet-D7x achieves a new state-of-the-art 55.1 AP on test-dev, outperforming prior art by a large margin in both accuracy (+4 AP) and efficiency (7x fewer FLOPs). In addition, we have also compared the inference latency on Titan-V FP32 , V100 GPU FP16, and single-thread CPU. Notably, our V100 latency is end-to-end including preprocessing and NMS postprocessing. Figure 4 illustrates the comparison on model size and GPU/CPU latency. For fair comparison, these figures only include results that are measured on the same machine with the same settings. Compared to previous detectors, EfficientDet models are up to 4.1x faster on GPU and 10.8x faster on CPU, suggesting

5.2. EfficientDet for Semantic Segmentation While our EfficientDet models are mainly designed for object detection, we are also interested in their performance on other tasks such as semantic segmentation. Following [19], we modify our EfficientDet model to keep feature level {P 2, P 3, ..., P 7} in BiFPN, but only use P 2 for the final per-pixel classification. For simplicity, here we only evaluate a EfficientDet-D4 based model, which uses a ImageNet pretrained EfficientNet-B4 backbone (similar size to ResNet-50). We set the channel size to 128 for BiFPN and 256 for classification head. Both BiFPN and classification head are repeated by 3 times. Table 3 shows the comparison between our models and previous DeepLabV3+ [6] on Pascal VOC 2012 [9]. Notably, we exclude those results with ensemble, testtime augmentation, or COCO pretraining. Under the same single-model single-scale settings, our model achieves 1.7% better accuracy with 9.8x fewer FLOPs than the prior art of DeepLabV3+ [6]. These results suggest that EfficientDet is also quite promising for semantic segmentation. 6

Figure 4: Model size and inference latency comparison – Latency is measured with batch size 1 on the same machine equipped with a Titan V GPU and Xeon CPU. AN denotes AmoebaNet + NAS-FPN trained with auto-augmentation [45]. Our EfficientDet models are 4x - 9x smaller, 2x - 4x faster on GPU, and 5x - 11x faster on CPU than other detectors.

Table 3: Performance comparison on Pascal VOC semantic segmentation.

6. Ablation Study In this section, we ablate various design choices for our proposed EfficientDet. For simplicity, all accuracy results here are for COCO validation set.

times and replace all convs with depthwise separable convs, which is the same as BiFPN. We use the same backbone and class/box prediction network, and the same training settings for all experiments. As we can see, the conventional topdown FPN is inherently limited by the one-way information flow and thus has the lowest accuracy. While repeated FPN+PANet achieves slightly better accuracy than NASFPN [10], it also requires more parameters and FLOPs. Our BiFPN achieves similar accuracy as repeated FPN+PANet, but uses much less parameters and FLOPs. With the additional weighted feature fusion, our BiFPN further achieves the best accuracy with fewer parameters and FLOPs.

6.1. Disentangling Backbone and BiFPN Since EfficientDet uses both a powerful backbone and a new BiFPN, we want to understand how much each of them contributes to the accuracy and efficiency improvements. Table 4 compares the impact of backbone and BiFPN using RetinaNet training settings. Starting from a RetinaNet detector [24] with ResNet-50 [14] backbone and top-down FPN [23], we first replace the backbone with EfficientNetB3, which improves accuracy by about 3 AP with slightly less parameters and FLOPs. By further replacing FPN with our proposed BiFPN, we achieve additional 4 AP gain with much fewer parameters and FLOPs. These results suggest that EfficientNet backbones and BiFPN are both crucial for our final models.

6.3. Softmax vs Fast Normalized Fusion As discussed in Section 3.3, we propose a fast normalized feature fusion approach to get ride of the expensive softmax while retaining the benefits of normalized weights. Table 6 compares the softmax and fast normalized fusion approaches in three detectors with different model sizes. As shown in the results, our fast normalized fusion approach achieves similar accuracy as the softmax-based fusion, but runs 1.26x - 1.31x faster on GPUs. In order to further understand the behavior of softmaxbased and fast normalized fusion, Figure 5 illustrates the

Figure 5: Softmax vs. fast normalized feature fusion – (a) - (c) shows normalized weights (i.e., importance) during training for three representative nodes; each node has two inputs (input1 & input2) and their normalized weights always sum up to 1.

Table 5: Comparison of different feature networks – Our weighted BiFPN achieves the best accuracy with fewer parameters and FLOPs.

Figure 6: Comparison of different scaling methods – compound scaling achieves better accuracy and efficiency. ing from the same baseline detector, our compound scaling method achieves better efficiency than other methods, suggesting the benefits of jointly scaling by better balancing difference architecture dimensions.

Table 6: Comparison of different feature fusion – Our fast fusion achieves similar accuracy as softmax-based fusion, but runs 28% - 31% faster.

7. Conclusion

learned weights for three feature fusion nodes randomly selected from the BiFPN layers in EfficientDet-D3. Notably, P wj wi the normalized weights (e.g., e / e for softmaxj P based fusion, and wi /( + j wj ) for fast normalized fusion) always sum up to 1 for all inputs. Interestingly, the normalized weights change rapidly during training, suggesting different features contribute to the feature fusion unequally. Despite the rapid change, our fast normalized fusion approach always shows very similar learning behavior to the softmax-based fusion for all three nodes.

In this paper, we systematically study network architecture design choices for efficient object detection, and propose a weighted bidirectional feature network and a customized compound scaling method, in order to improve accuracy and efficiency. Based on these optimizations, we develop a new family of detectors, named EfficientDet, which consistently achieve better accuracy and efficiency than the prior art across a wide spectrum of resource constraints. In particular, our scaled EfficientDet achieves state-of-the-art accuracy with much fewer parameters and FLOPs than previous object detection and semantic segmentation models.

6.4. Compound Scaling

As discussed in section 4.2, we employ a compound scaling method to jointly scale up all dimensions of depth/width/resolution for backbone, BiFPN, and box/class prediction networks. Figure 6 compares our compound scaling with other alternative methods that scale up a single dimension of resolution/depth/width. Although start-

Special thanks to Golnaz Ghiasi, Adams Yu, Daiyi Peng for their help on infrastructure and discussion. We also thank Adam Kraft, Barret Zoph, Ekin D. Cubuk, Hongkun Yu, Jeff Dean, Pengchong Jin, Samy Bengio, Reed Wanderman-Milne, Tsung-Yi Lin, Xianzhi Du, Xiaodan Song, Yunxing Dai, and the Google Brain team. We 8

thank the open source community for the contributions.
