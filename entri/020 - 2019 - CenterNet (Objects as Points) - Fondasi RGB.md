# 020 - Objects as Points

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2019objects` |
| Judul asli | Objects as Points |
| Penulis | Xingyi Zhou, Dequan Wang, Philipp Krähenbühl |
| Tahun | 2019 |
| Venue | arXiv preprint arXiv:1904.07850 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1904.07850
- **Google Scholar:** https://scholar.google.com/scholar?q=Objects%20as%20Points
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Objects%20as%20Points&sort=relevance
- **Repositori kode resmi:** https://github.com/xingyizhou/CenterNet

## Gambaran Umum

Makalah ini memperkenalkan CenterNet, detektor objek yang merepresentasikan setiap objek sebagai satu titik, yaitu titik pusat kotak pembatasnya (*bounding box*). Deteksi dirumuskan ulang sebagai estimasi *keypoint* (titik kunci): sebuah jaringan konvolusi penuh menghasilkan *heatmap* (peta skor per piksel) yang puncaknya menandai pusat objek pada tiap kelas, sedangkan ukuran kotak dan koreksi posisi sub-piksel diregresi langsung dari fitur pada lokasi puncak. Karena satu objek hanya diwakili satu puncak, tahap enumerasi kandidat kotak (*anchor*) dan pasca-pemrosesan *Non-Maximum Suppression* (NMS) tidak lagi diperlukan.

Kerangka yang sama, tanpa perubahan struktural, juga dipakai untuk estimasi kotak 3D monokular dan pose manusia multi-orang; cukup dengan menambah kanal keluaran pada titik pusat. Pada tolok ukur MS COCO, CenterNet mencapai 37,4% AP pada 52 FPS dengan *backbone* DLA-34 dan 45,1% AP dengan pengujian multi-skala pada 1,4 FPS — kombinasi kecepatan-akurasi terbaik di antara detektor satu tahap pada tahun publikasinya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hingga 2019, detektor objek yang paling berhasil memandang deteksi sebagai klasifikasi atas enumerasi besar kandidat kotak. Detektor dua tahap dari keluarga R-CNN (bab 012 dan 013) mengusulkan ribuan wilayah kandidat lalu mengklasifikasikannya satu per satu. Detektor satu tahap seperti YOLOv3 (bab 003), SSD (bab 015), dan RetinaNet (bab 016) menyebarkan puluhan ribu *anchor box* — kotak acuan berukuran dan berrasio tetap — pada setiap citra, lalu mengklasifikasikan dan menyesuaikan masing-masing secara langsung.

Pola enumerasi ini membawa tiga masalah. Pertama, boros: hampir semua kandidat tidak menutupi objek apa pun, sehingga muncul ketidakseimbangan contoh positif-negatif yang harus ditangani dengan teknik khusus seperti *focal loss*. Kedua, penetapan label positif-negatif bergantung pada ambang IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak) yang ditetapkan manual; pada Faster R-CNN (bab 014), sebuah anchor berlabel positif bila IoU-nya di atas 0,7 terhadap objek dan negatif bila di bawah 0,3. Ketiga, satu objek biasanya terdeteksi oleh banyak kandidat, sehingga hasil harus dirampingkan dengan NMS, operasi berbasis IoU yang tidak dapat diturunkan (*differentiable*); akibatnya detektor tidak sepenuhnya terlatih *end-to-end* (satu proses optimasi dari masukan ke keluaran).

Jalur bebas anchor melalui estimasi *keypoint* sudah ditempuh lebih dulu: CornerNet (2018) mendeteksi pasangan sudut kotak dan ExtremeNet (2019) mendeteksi empat titik ekstrem ditambah pusat. Keduanya menghapus anchor, tetapi memerlukan pengelompokan kombinatorial untuk memasangkan titik milik objek yang sama — tahap yang memperlambat inferensi dan menambah kerumitan.

## Ide Utama

Satu objek cukup diwakili satu titik: pusat kotaknya. Dengan representasi ini, deteksi menjadi masalah estimasi *keypoint* standar, persoalan yang saat itu sudah diselesaikan dengan baik pada estimasi pose manusia. Masukan berupa citra; keluaran berupa *heatmap* per kelas; setiap puncak lokal pada heatmap adalah satu deteksi. Semua properti objek yang lain — lebar dan tinggi kotak, koreksi posisi, hingga atribut 3D dan posisi sendi — diregresi dari vektor fitur tepat pada titik pusat tersebut.

Dalam tafsir yang menjembatani paradigma lama, titik pusat dapat dipandang sebagai satu *anchor* tunggal tanpa bentuk, dengan tiga perbedaan: penetapannya hanya berdasarkan lokasi, tanpa ambang IoU; hanya ada satu kandidat positif per objek; dan resolusi keluaran dinaikkan (*stride* 4, bukan 16), sehingga satu lokasi cukup untuk objek segala ukuran. Konsekuensinya, NMS tidak dibutuhkan dan pencarian puncak lokal menggantikan fungsinya.

## Cara Kerja Langkah demi Langkah

### Heatmap Pusat

Keluaran inti CenterNet adalah *heatmap* berukuran (W/R)×(H/R)×C, dengan W×H ukuran citra masukan, R = 4 adalah *output stride* (faktor pengecilan spasial), dan C jumlah kelas (C = 80 pada COCO). Nilai 1 pada suatu posisi menandakan pusat objek; nilai 0 berarti latar. Untuk pelatihan, pusat kebenaran p dipetakan ke resolusi rendah: p̃ = ⌊p/R⌋. Contoh: pada citra 512×512, heatmap berukuran 128×128; pusat objek pada piksel (200, 300) jatuh pada posisi (50, 75).

Titik kebenaran tidak ditandai sebagai satu piksel biner, melainkan disebarkan sebagai gundukan fungsi Gaussian: nilai target pada posisi sekitar p̃ berbentuk exp(−jarak²/(2σ²)), dengan simpangan baku σ yang menyesuaikan ukuran objek mengikuti aturan CornerNet — radius dipilih sehingga kotak apa pun yang pusatnya berada dalam radius itu masih memiliki IoU ≥ 0,7 terhadap kotak kebenaran. Bila dua gundukan sekelas saling tumpang tindih, diambil nilai maksimum per posisi. Piksel di sekitar pusat dengan demikian menjadi positif yang dilemahkan, bukan negatif penuh.

### Fungsi Loss Heatmap

Heatmap dilatih dengan *penalty-reduced focal loss* dari CornerNet: regresi logistik per piksel dengan pembobotan *focal* (α = 2, β = 4). Piksel dengan target 1 dihukum sebagai positif; piksel lain dihukum sebagai negatif, tetapi penaltinya diperkecil dengan faktor (1−Y)^β bila target Gaussian-nya tinggi — jaringan tidak dihukum berat karena memberi skor sedang di dalam radius toleransi pusat. Loss dinormalisasi dengan N, jumlah objek dalam citra.

### Regresi Ukuran dan Offset

Pemetaan ⌊p/R⌋ membuang sisa pembagian, sehingga pusat hasil dekode dapat meleset hingga 4 piksel pada skala citra asli. Untuk menutup galat diskritisasi ini, jaringan memprediksi *offset* lokal Ô (2 kanal, dibagi semua kelas) berisi selisih p/R − p̃, serta ukuran kotak Ŝ (2 kanal: lebar dan tinggi), keduanya pada lokasi pusat. Keduanya dilatih dengan loss L1 yang hanya aktif pada lokasi pusat; posisi lain diabaikan. Ukuran diprediksi dalam piksel mentah tanpa normalisasi skala, sehingga bobot loss-nya diperkecil: λ_size = 0,1 dan λ_off = 1. Loss total deteksi adalah L_det = L_k + 0,1·L_size + L_off.

### Backbone dan Kepala Prediksi

Karena heatmap menuntut resolusi keluaran tinggi, CenterNet memakai *backbone* (jaringan pengekstrak fitur) yang dirancang untuk estimasi keypoint, dalam empat varian. Hourglass-104 terdiri atas dua modul *hourglass* bertingkat dengan koneksi *skip*, sama seperti pada CornerNet. ResNet-18 dan ResNet-101 ditambah tiga lapis *up-convolution* (konvolusi transpos untuk menaikkan resolusi; kanal 256, 128, 64), dengan satu konvolusi *deformable* 3×3 — konvolusi yang posisi cupliknya digeser oleh offset terpelajar — sebelum setiap *upsampling*. DLA-34 (*Deep Layer Aggregation*), jaringan dengan koneksi hierarkis antar-lapis, dimodifikasi serupa untuk prediksi padat. Setiap modalitas keluaran dihasilkan kepala terpisah: konvolusi 3×3, ReLU, lalu konvolusi 1×1; total C+4 kanal per posisi.

### Inferensi Tanpa NMS

Saat inferensi, puncak diekstrak per kelas: semua posisi bernilai lebih besar atau sama dengan kedelapan tetangganya dipertahankan, lalu diambil 100 teratas. Operasi ini terimplementasi efisien sebagai *max pooling* 3×3 — posisi yang nilainya tidak berubah setelah pooling adalah puncak lokal. Setiap puncak (x̂, ŷ) dengan nilai heatmap s langsung menjadi satu deteksi: skornya s, pusatnya dikoreksi offset menjadi (x̂+δx̂, ŷ+δŷ), dan kotaknya dibangun dari ukuran yang diregresi, yaitu (x̂+δx̂−ŵ/2, ŷ+δŷ−ĥ/2, x̂+δx̂+ŵ/2, ŷ+δŷ+ĥ/2). Tidak ada perhitungan IoU antar-kandidat maupun penekanan duplikat.

Alur data lengkap dari citra ke deteksi:

```
citra 512x512
     │
     ▼
┌─────────────────────────────┐
│ backbone (DLA-34 / ResNet   │   output stride R = 4
│ + up-conv / Hourglass-104)  │
└─────────────────────────────┘
     │  peta fitur 128x128
     ▼
┌───────────┬───────────┬───────────┐
│ heatmap   │ offset    │ ukuran    │   setiap kepala:
│ C kanal   │ 2 kanal   │ 2 kanal   │   3x3 conv ->
│ (kelas)   │ (dx, dy)  │ (w, h)    │   ReLU -> 1x1 conv
└───────────┴───────────┴───────────┘
     │
     ▼
puncak lokal: max-pool 3x3 (nilai >= 8 tetangga),
ambil 100 puncak teratas
     │
     ▼
kotak = (x+dx-w/2, y+dy-h/2, x+dx+w/2, y+dy+h/2)
skor  = nilai heatmap pada puncak
```

Seluruh keluaran diperoleh dalam satu kali umpan-maju jaringan; satu-satunya tahap di luar jaringan adalah *max pooling* 3×3 untuk mengekstrak puncak.

### Perluasan ke 3D dan Pose

Untuk deteksi 3D monokular (dari satu citra kamera), tiga kepala ditambahkan: kedalaman absolut melalui transformasi sigmoid-balik d = 1/σ(d̂) − 1, karena kedalaman sukar diregresi langsung; dimensi 3D (tinggi, lebar, panjang) dalam meter; dan orientasi yang dikodekan sebagai 8 skalar dalam dua *bin* sudut mengikuti skema Mousavian et al. Untuk pose multi-orang, posisi 17 sendi manusia diregresi sebagai offset dari pusat orang (34 kanal), lalu ditempelkan ke deteksi sendi terdekat pada *heatmap* sendi terpisah yang dilatih seperti heatmap pusat. Kedua perluasan tidak mengubah kerangka deteksi pusat; yang bertambah hanya kanal keluaran.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada MS COCO (118 ribu citra latih, 5 ribu validasi, 20 ribu test-dev) dengan metrik AP COCO, yaitu rata-rata presisi pada ambang IoU 0,5 sampai 0,95; semakin tinggi semakin baik, maksimal 100%. Kecepatan diukur pada mesin yang sama untuk semua pembanding yang tersedia kodenya (GPU Titan Xp).

Hasil utama pada validasi COCO, beserta interpretasinya:

- ResNet-18: 28,1% AP pada 142 FPS — model tercepat, dengan akurasi yang masih layak untuk aplikasi waktu-nyata berdaya rendah.
- DLA-34: 37,4% AP pada 52 FPS — lebih dari dua kali lebih cepat daripada YOLOv3 (33,0% AP, 20 FPS) sekaligus 4,4 poin AP lebih akurat.
- Hourglass-104: 40,3% AP pada 14 FPS, naik menjadi 42,2% dengan uji *flip* (rata-rata keluaran citra asli dan bayangan cerminnya), dan 45,1% dengan pengujian multi-skala pada 1,4 FPS. Angka terakhir ini melampaui semua detektor satu tahap pada test-dev, termasuk CornerNet (42,1% pada 4,1 FPS) dan ExtremeNet (43,7% pada 3,1 FPS) yang memakai backbone yang sama tetapi jauh lebih lambat karena tahap pengelompokannya.
- ResNet-101: 34,8% AP pada 45 FPS, dibandingkan RetinaNet ber-backbone setara (34,4% AP, 18 FPS) — akurasi setara dengan kecepatan lebih dari dua kali lipat.

Dua analisis tambahan memperkuat klaim desainnya. Pertama, risiko tabrakan pusat — dua objek berbeda yang pusatnya jatuh pada piksel heatmap yang sama — ternyata kecil: pada data latih COCO hanya ada 614 pasang objek yang bertabrakan dari total 860.001 objek (kurang dari 0,1%), lebih rendah daripada objek yang terlewat oleh proposal wilayah (~2%) maupun oleh penempatan anchor (20% pada Faster R-CNN). Kedua, menambahkan NMS pada keluaran CenterNet hampir tidak berpengaruh: AP DLA-34 naik dari 39,2% menjadi 39,7%, dan Hourglass-104 tetap 42,2%. Hasil ini membenarkan bahwa pencarian puncak memang pengganti NMS yang memadai.

Pada tolok ukur KITTI (deteksi 3D kendaraan dari satu citra), CenterNet setara dengan Deep3DBox dan Mono3D pada metrik AP dan AOS (*average orientation similarity*), sedikit lebih baik pada AP tampak atas (*bird's-eye-view*), dengan kecepatan sekitar dua orde lebih tinggi. Pada estimasi pose manusia COCO, varian DLA-34 mencapai 58,9% AP keypoint pada 23 FPS dan Hourglass-104 mencapai 64,0% pada 6,6 FPS. Regresi offset sendi murni masih lemah pada ambang kesamaan yang ketat, tetapi penyempurnaan dengan heatmap sendi membuatnya kompetitif terhadap metode multi-tahap.

## Kelebihan dan Keterbatasan

Kelebihan: (1) *pipeline* paling sederhana di antara detektor sezamannya — satu umpan-maju tanpa anchor, tanpa ambang IoU untuk penetapan label, dan tanpa NMS; (2) sepenuhnya *end-to-end differentiable*; (3) satu kerangka berlaku untuk deteksi 2D, 3D monokular, dan pose, cukup dengan menambah kepala keluaran; (4) trade-off kecepatan-akurasi terbaik di kelasnya pada 2019.

Keterbatasan: (1) dua objek yang pusatnya berimpit hanya akan terdeteksi satu; walau analisis tabrakan pada bagian sebelumnya menunjukkan kasusnya jarang pada COCO, secara konseptual batas ini tetap ada, misalnya pada objek yang sejajar garis pandang kamera; (2) kualitas heatmap menuntut backbone resolusi tinggi, sehingga varian paling akurat bergantung pada Hourglass-104 yang berat (1,4 FPS pada pengujian multi-skala), dan ablasi penulis menunjukkan penurunan resolusi uji ke 384×384 memangkas 3 poin AP; (3) akurasi pada objek kecil (AP_S 24,1% untuk varian terbaik) masih di bawah detektor dua tahap terkuat pada masa itu; (4) dari sisi rekayasa, ketergantungan pada konvolusi deformable pada varian ResNet dan DLA menambah kerumitan implementasi pada perangkat yang tidak menyediakan operasi tersebut.

## Kaitan dengan Bab Lain

CenterNet melanjutkan garis penyederhanaan pipeline yang dimulai [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md): bila YOLOv1 menghapus tahap proposal wilayah, CenterNet menghapus anchor dan NMS sekaligus. Pembanding langsungnya adalah [bab 003 (YOLOv3)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), detektor berbasis anchor yang pada tolok ukur yang sama dikalahkan CenterNet dalam kecepatan maupun akurasi, serta [bab 016 (RetinaNet)](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md) yang *focal loss*-nya diwarisi CenterNet untuk melatih heatmap. Arah "satu titik per objek, tanpa anchor" kemudian diadopsi keluarga YOLO sendiri: [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) melepaskan anchor dan memprediksi dari satu lokasi, dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md) meniadakan NMS melalui penetapan label ganda — dua sasaran yang lebih dulu dibuktikan layak oleh CenterNet. Representasi titik pusatnya juga menjadi fondasi keluarga metode lanjutan seperti CenterTrack (pelacakan) dan CenterPoint (deteksi 3D LiDAR).

## Poin untuk Sitasi

Kutip dengan kunci `zhou2019objects`. Ringkasan yang aman dikutip: "CenterNet merepresentasikan objek sebagai titik pusat kotaknya; deteksi menjadi estimasi keypoint pada heatmap dengan output stride 4, sedangkan ukuran dan offset kotak diregresi dari fitur pusat, tanpa anchor maupun NMS. Pada MS COCO, model DLA-34 mencapai 37,4% AP pada 52 FPS dan model Hourglass-104 mencapai 45,1% AP dengan pengujian multi-skala."

Catatan verifikasi: angka 28,1%/142 FPS, 37,4%/52 FPS, dan 45,1%/1,4 FPS berasal dari abstrak naskah. Angka 42,2% (uji flip Hourglass-104) dan perbandingan 34,8% lawan 34,4% terhadap RetinaNet diambil dari teks naskah; repositori resmi mencatat 34,6% untuk varian ResNet-101, sehingga angka ini perlu dicocokkan dengan tabel naskah sebelum dikutip. Angka pose (58,9% dan 64,0% AP keypoint) diambil dari tabel hasil repositori resmi untuk set validasi; hasil KITTI dikutip secara kualitatif dari naskah.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract 40

Figure 1: Speed-accuracy trade-off on COCO validation for real-time detectors. The proposed CenterNet outperforms a range of state-of-the-art algorithms. moves duplicated detections for the same instance by computing bounding box IoU. This post-processing is hard to differentiate and train [23], hence most current detectors are not end-to-end trainable. Nonetheless, over the past five years [19], this idea has achieved good empirical success [12,21,25,26,31,35,47,48,56,62,63]. Sliding window based object detectors are however a bit wasteful, as they need to enumerate all possible object locations and dimensions. In this paper, we provide a much simpler and more efficient alternative. We represent objects by a single point at their bounding box center (see Figure 2). Other properties, such as object size, dimension, 3D extent, orientation, and pose are then regressed directly from image features at the center location. Object detection is then a standard keypoint estimation problem [3,39,60]. We simply feed the input image to a fully convolutional network [37, 40] that generates a heatmap. Peaks in this heatmap correspond to object centers. Image features at each peak predict the objects bounding box height and weight. The model trains using standard dense supervised learning [39,60]. Inference is a single network forward-pass, without non-maximal suppression for post-processing.

1. Introduction Object detection powers many vision tasks like instance segmentation [7, 21, 32], pose estimation [3, 15, 39], tracking [24, 27], and action recognition [5]. It has down-stream applications in surveillance [57], autonomous driving [53], and visual question answering [1]. Current object detectors represent each object through an axis-aligned bounding box that tightly encompasses the object [18, 19, 33, 43, 46]. They then reduce object detection to image classification of an extensive number of potential object bounding boxes. For each bounding box, the classifier determines if the image content is a specific object or background. Onestage detectors [33, 43] slide a complex arrangement of possible bounding boxes, called anchors, over the image and classify them directly without specifying the box content. Two-stage detectors [18, 19, 46] recompute imagefeatures for each potential box, then classify those features. Post-processing, namely non-maxima suppression, then re1

2. Related work Object detection by region classification. One of the first successful deep object detectors, RCNN [19], enumerates object location from a large set of region candidates [52], crops them, and classifies each using a deep network. Fast-RCNN [18] crops image features instead, to save computation. However, both methods rely on slow low-level region proposal methods. Object detection with implicit anchors. Faster RCNN [46] generates region proposal within the detection network. It samples fixed-shape bounding boxes (anchors) around a low-resolution image grid and classifies each into “foreground or not”. An anchor is labeled foreground with a >0.7 overlap with any ground truth object, background with a < 0.3 overlap, or ignored otherwise. Each generated region proposal is again classified [18].

Changing the proposal classifier to a multi-class classification forms the basis of one-stage detectors. Several improvements to one-stage detectors include anchor shape priors [44, 45], different feature resolution [36], and loss re-weighting among different samples [33]. Our approach is closely related to anchor-based onestage approaches [33, 36, 43]. A center point can be seen as a single shape-agnostic anchor (see Figure 3). However, there are a few important differences. First, our CenterNet assigns the “anchor” based solely on location, not box overlap [18]. We have no manual thresholds [18] for foreground and background classification. Second, we only have one positive “anchor” per object, and hence do not need NonMaximum Suppression (NMS) [2]. We simply extract local peaks in the keypoint heatmap [4, 39]. Third, CenterNet uses a larger output resolution (output stride of 4) compared to traditional object detectors [21, 22] (output stride of 16). This eliminates the need for multiple anchors [47]. Object detection by keypoint estimation. We are not the first to use keypoint estimation for object detection. CornerNet [30] detects two bounding box corners as keypoints, while ExtremeNet [61] detects the top-, left-, bottom-, rightmost, and center points of all objects. Both these methods build on the same robust keypoint estimation network as our CenterNet. However, they require a combinatorial grouping stage after keypoint detection, which significantly slows down each algorithm. Our CenterNet, on the other hand, simply extracts a single center point per object without the need for grouping or post-processing. Monocular 3D object detection. 3D bounding box estimation powers autonomous driving [17]. Deep3Dbox [38] uses a slow-RCNN [19] style framework, by first detecting 2D objects [46] and then feeding each object into a 3D estimation network. 3D RCNN [29] adds an additional head to Faster-RCNN [46] followed by a 3D projection. Deep Manta [6] uses a coarse-to-fine Faster-RCNN [46] trained on many tasks. Our method is similar to a one-stage version of Deep3Dbox [38] or 3DRCNN [29]. As such, CenterNet is much simpler and faster than competing methods.

(a) Standard anchor based detection. Anchors count as positive with an overlap IoU > 0.7 to any object, negative with an overlap IoU < 0.3, or are ignored otherwise.

(b) Center point based detection. The center pixel is assigned to the object. Nearby points have a reduced negative loss. Object size is regressed.

for each center point. All classes c share the same offset prediction. The offset is trained with an L1 loss p

Figure 3: Different between anchor-based detectors (a) and our center point detector (b). Best viewed on screen.

4. Objects as Points

3. Preliminary

We do not normalize the scale and directly use the raw pixel coordinates. We instead scale the loss by a constant λsize . The overall training objective is Ldet = Lk + λsize Lsize + λof f Lof f .

We set λsize = 0.1 and λof f = 1 in all our experiments unless specified otherwise. We use a single network to predict the keypoints Ŷ , offset Ô, and size Ŝ. The network predicts a total of C + 4 outputs at each location. All outputs share a common fully-convolutional backbone network. For each modality, the features of the backbone are then passed through a separate 3 × 3 convolution, ReLU and another 1 × 1 convolution. Figure 4 shows an overview of the network output. Section 5 and supplementary material contain additional architectural details. From points to bounding boxes At inference time, we first extract the peaks in the heatmap for each category independently. We detect all responses whose value is greater or equal to its 8-connected neighbors and keep the top 100 peaks. Let P̂c be the set of n detected center points P̂ = {(x̂i , ŷi )}ni=1 of class c. Each keypoint location is given by an integer coordinates (xi , yi ). We use the keypoint values Ŷxi yi c as a measure of its detection confidence, and produce a bounding box at location (x̂i + δ x̂i − ŵi /2, ŷi + δ ŷi − ĥi /2, x̂i + δ x̂i + ŵi /2, ŷi + δ ŷi + ĥi /2),

The 3D dimensions of an object are three scalars. We directly regress to their absolute values in meters using a W H separate head Γ̂ ∈ R R × R ×3 and an L1 loss. Orientation is a single scalar by default. However, it can be hard to regress to. We follow Mousavian et al. [38] and represent the orientation as two bins with in-bin regression. (d)Specifically, Pose Estimation the orientation is encoded using 8 scalars, with 4 scalars for each bin. For one bin, two scalars are used for softmax classification and the rest two scalar regress to an angle within each bin. Please see the supplementary for details about these losses.

4.2. Human pose estimation 3D size [3]

Figure 4: Outputs of our network for different tasks: top for object detection, middle for 3D object detection, bottom: for pose estimation. All modalities are produced from a common backbone, with a different 3 × 3 and 1 × 1 output convolutions separated by a ReLU. The number in brackets indicates the output channels. See section 4 for details. where (δ x̂i , δ ŷi ) = Ôx̂i ,ŷi is the offset prediction and (ŵi , ĥi ) = Ŝx̂i ,ŷi is the size prediction. All outputs are produced directly from the keypoint estimation without the need for IoU-based non-maxima suppression (NMS) or other post-processing. The peak keypoint extraction serves as a sufficient NMS alternative and can be implemented efficiently on device using a 3 × 3 max pooling operation.

4.1. 3D detection 3D detection estimates a three-dimensional bounding box per objects and requires three additional attributes per center point: depth, 3D dimension, and orientation. We add a separate head for each of them. The depth d is a single scalar per center point. However, depth is difficult to regress to directly. We instead use the output transformaˆ − 1, where σ tion of Eigen et al. [13] and d = 1/σ(d) is the sigmoid function. We compute the depth as an adW H ditional output channel D̂ ∈ [0, 1] R × R of our keypoint estimator. It again uses two convolutional layers separated by a ReLU. Unlike previous modalities, it uses the inverse sigmoidal transformation at the output layer. We train the depth estimator using an L1 loss in the original depth domain, after the sigmoidal transformation.

Human pose estimation aims to estimate k 2D human joint locations for every human instance in the image (k = 17 for COCO). We considered the pose as a k × 2dimensional property of the center point, and parametrize each keypoint by an offset to the center point. We directly H W regress to the joint offsets (in pixels) Jˆ ∈ R R × R ×k×2 with an L1 loss. We ignore the invisible keypoints by masking the loss. This results in a regression-based one-stage multiperson human pose estimator similar to the slow-RCNN version counterparts Toshev et al. [51] and Sun et al. [49]. To refine the keypoints, we further estimate k human W H joint heatmaps Φ̂ ∈ R R × R ×k using standard bottom-up multi-human pose estimation [4,39,41]. We train the human joint heatmap with focal loss and local pixel offset analogous to the center detection discussed in Section. 3. We then snap our initial predictions to the closest detected keypoint on this heatmap. Here, our center offset acts as a grouping cue, to assign individual keypoint detections to their closest person instance. Specifically, let (x̂, ŷ) be a detected center point. We first regress to all joint locations lj = (x̂, ŷ) + Jˆx̂ŷj for j ∈ 1 . . . k. We also extract all nj keypoint locations Lj = {˜lji }i=1 with a confidence > 0.1 for each joint type j from the corresponding heatmap Φ̂··j . We then assign each regressed location lj to its closest detected keypoint arg minl∈Lj (l − lj )2 considering only joint detections within the bounding box of the detected object.

5. Implementation details We experiment with 4 architectures: ResNet-18, ResNet101 [55], DLA-34 [58], and Hourglass-104 [30]. We modify both ResNets and DLA-34 using deformable convolution layers [12] and use the Hourglass network as is. Hourglass The stacked Hourglass Network [30, 40] downsamples the input by 4×, followed by two sequential hourglass modules. Each hourglass module is a symmetric 5-layer down- and up-convolutional network with skip connections. This network is quite large, but generally yields the best keypoint estimation performance.

Table 1: Speed / accuracy trade off for different networks on COCO validation set. We show results without test augmentation (N.A.), flip testing (F), and multi-scale augmentation (MS). ResNet Xiao et al. [55] augment a standard residual network [22] with three up-convolutional networks to allow for a higher-resolution output (output stride 4). We first change the channels of the three upsampling layers to 256, 128, 64, respectively, to save computation. We then add one 3 × 3 deformable convolutional layer before each up-convolution with channel 256, 128, 64, respectively. The up-convolutional kernels are initialized as bilinear interpolation. See supplement for a detailed architecture diagram. DLA Deep Layer Aggregation (DLA) [58] is an image classification network with hierarchical skip connections. We utilize the fully convolutional upsampling version of DLA for dense prediction, which uses iterative deep aggregation to increase feature map resolution symmetrically. We augment the skip connections with deformable convolution [63] from lower layers to the output. Specifically, we replace the original convolution with 3 × 3 deformable convolution at every upsampling layer. See supplement for a detailed architecture diagram. We add one 3 × 3 convolutional layer with 256 channel before each output head. A final 1 × 1 convolution then produces the desired output. We provide more details in the supplementary material. Training We train on an input resolution of 512 × 512. This yields an output resolution of 128×128 for all the models. We use random flip, random scaling (between 0.6 to 1.3), cropping, and color jittering as data augmentation, and use Adam [28] to optimize the overall objective. We use no augmentation to train the 3D estimation branch, as cropping or scaling changes the 3D measurements. For the residual networks and DLA-34, we train with a batch-size of 128 (on 8 GPUs) and learning rate 5e-4 for 140 epochs, with learning rate dropped 10× at 90 and 120 epochs, respectively (following [55]). For Hourglass-104, we follow ExtremeNet [61] and use batch-size 29 (on 5 GPUs, with master GPU batch-size 4) and learning rate 2.5e-4 for 50 epochs with 10× learning rate dropped at the 40 epoch. For detection, we fine-tune the Hourglass-104 from ExtremeNet [61] to save computation. The down-sampling layers of Resnet101 and DLA-34 are initialized with ImageNet pretrain and the up-sampling layers are randomly initialized. Resnet-101

and DLA-34 train in 2.5 days on 8 TITAN-V GPUs, while Hourglass-104 requires 5 days. Inference We use three levels of test augmentations: no augmentation, flip augmentation, and flip and multi-scale (0.5, 0.75, 1, 1.25, 1.5). For flip, we average the network outputs before decoding bounding boxes. For multi-scale, we use NMS to merge results. These augmentations yield different speed-accuracy trade-off, as is shown in the next section.

In unlucky circumstances, two different objects might share the same center, if they perfectly align. In this scenario, CenterNet would only detect one of them. We start by studying how often this happens in practice and put it in relation to missing detections of competing methods. Center point collision In the COCO training set, there are 614 pairs of objects that collide onto the same center point at stride 4. There are 860001 objects in total, hence

CenterNet is unable to predict < 0.1% of objects due to collisions in center points. This is much less than slow- or fastRCNN miss due to imperfect region proposals [52] (∼ 2%), and fewer than anchor-based methods miss due to insufficient anchor placement [46] (20.0% for Faster-RCNN with 15 anchors at 0.5 IOU threshold). In addition, 715 pairs of objects have bounding box IoU > 0.7 and would be assigned to two anchors, hence a center-based assignment causes fewer collisions. NMS To verify that IoU based NMS is not needed for CenterNet, we ran it as a post-processing step on our predictions. For DLA-34 (flip-test), the AP improves from 39.2% to 39.7%. For Hourglass-104, the AP stays at 42.2%. Given the minor impact, we do not use it. Next, we ablate the new hyperparameters of our model. All the experiments are done on DLA-34. Training and Testing resolution During training, we fix the input resolution to 512 × 512. During testing, we follow CornerNet [30] to keep the original image resolution and zero-pad the input to the maximum stride of the network. For ResNet and DLA, we pad the image with up to 32 pixels, for HourglassNet, we use 128 pixels. As is shown in Table. 3a, keeping the original resolution is slightly better than fixing test resolution. Training and testing in a lower resolution (384 × 384) runs 1.7 times faster but drops 3AP. Regression loss We compare a vanilla L1 loss to a Smooth L1 [18] for size regression. Our experiments in Table 3c show that L1 is considerably better than Smooth L1.

(a) Testing resolution: Lager resolutions perform better but run slower.

(c) Regression loss. L1 loss works better than Smooth L1.

Table 3: Ablation of design choices on COCO validation set. The results are shown in COCO AP, time in milliseconds. It yields a better accuracy at fine-scale, which the COCO evaluation metric is sensitive to. This is independently observed in keypoint regression [49, 50]. Bounding box size weight We analyze the sensitivity of our approach to the loss weight λsize . Table 3b shows 0.1 gives a good result. For larger values, the AP degrades significantly, due to the scale of the loss ranging from 0 to output size w/R or h/R, instead of 0 to 1. However, the value does not degrade significantly for lower weights. Training schedule By default, we train the keypoint estimation network for 140 epochs with a learning rate drop at 90 epochs. If we double the training epochs before dropping the learning rate, the performance further increases by 1.1 AP (Table 3d), at the cost of a much longer training schedule. To save computational resources (and polar bears), we use 140 epochs in ablation experiments, but stick with 230 epochs for DLA when comparing to other methods. Finally, we tried a multiple “anchor” version of CenterNet by regressing to more than one object size. The experiments did not yield any success. See supplement.

6.2. 3D detection We perform 3D bounding box estimation experiments on KITTI dataset [17], which contains carefully annotated 3D bounding box for vehicles in a driving scenario. KITTI contains 7841 training images and we follow standard training and validation splits in literature [10, 54]. The evaluation metric is the average precision for cars at 11 recalls (0.0 to 1.0 with 0.1 increment) at IOU threshold 0.5, as in object detection [14]. We evaluate IOUs based on 2D bounding box (AP), orientation (AOP), and Bird-eye-view bounding box (BEV AP). We keep the original image resolution and pad to 1280×384 for both training and testing. The training

converges in 70 epochs, with learning rate dropped at the 45 and 60 epoch, respectively. We use the DLA-34 backbone and set the loss weight for depth, orientation, and dimension to 1. All other hyper-parameters are the same as the detection experiments. Since the number of recall thresholds is quite small, the validation AP fluctuates by up to 10% AP. We thus train 5 models and report the average with standard deviation. We compare with slow-RCNN based Deep3DBox [38] and Faster-RCNN based method Mono3D [9], on their specific validation split. As is shown in Table 4, our method performs on-par with its counterparts in AP and AOS and does slightly better in BEV. Our CenterNet is two orders of magnitude faster than both methods.

6.3. Pose estimation Finally, we evaluate CenterNet on human pose estimation in the MS COCO dataset [34]. We evaluate keypoint AP, which is similar to bounding box AP but replaces the bounding box IoU with object keypoint similarity. We test and compare with other methods on COCO test-dev. We experiment with DLA-34 and Hourglass-104, both fine-tuned from center point detection. DLA-34 converges in 320 epochs (about 3 days on 8GPUs) and Hourglass-104 converges in 150 epochs (8 days on 5 GPUs). All additional loss weights are set to 1. All other hyper-parameters are the same as object detection. The results are shown in Table 5. Direct regression to keypoints performs reasonably, but not at state-of-the-art. It struggles particularly in high IoU regimes. Projecting our output to the closest joint detection improves the results throughout, and performs competitively with state-of-theart multi-person pose estimators [4,21,39,41]. This verifies that CenterNet is general, easy to adapt to a new task. Figure 5 shows qualitative examples on all tasks.

Table 4: KITTI evaluation. We show 2D bounding box AP, average orientation score (AOS), and bird eye view (BEV) AP on different validation splits. Higher is better.

Table 5: Keypoint detection on COCO test-dev. -reg/ -jd are for direct center-out offset regression and matching regression to the closest joint detection, respectively. The results are shown in COCO keypoint AP. Higher is better.

7. Conclusion In summary, we present a new representation for objects: as points. Our CenterNet object detector builds on successful keypoint estimation networks, finds object centers, and regresses to their size. The algorithm is simple, fast, accurate, and end-to-end differentiable without any NMS postprocessing. The idea is general and has broad applications beyond simple two-dimensional detection. CenterNet can estimate a range of additional object properties, such as pose, 3D orientation, depth and extent, in one single forward pass. Our initial experiments are encouraging and open up a new direction for real-time object recognition and related tasks.
