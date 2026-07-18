# 151 - Object Detection in 20 Years: A Survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zou2023objectdetectionsurvey` |
| Judul asli | Object Detection in 20 Years: A Survey |
| Penulis | Zou, Zhengxia; Chen, Keyan; Shi, Zhenwei; Guo, Yuhong; Ye, Jieping |
| Tahun | 2023 |
| Venue / Jurnal | Proceedings of the IEEE |
| Tema klaster | Fusi Multimodal |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Object%20Detection%20in%2020%20Years%3A%20A%20Survey
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Object%20Detection%20in%2020%20Years%3A%20A%20Survey&sort=relevance
- **DOI Jurnal:** https://doi.org/10.1109/JPROC.2023.3238549
- **arXiv Preprint:** https://arxiv.org/abs/1905.05055

## Gambaran Umum
Makalah ini menyajikan survei komprehensif mengenai perkembangan teknologi deteksi objek visual selama lebih dari dua dekade, yang memetakan transisi besar dari era fitur buatan tangan (*handcrafted features*) ke era pembelajaran mendalam (*deep learning*). Penulis membagi lintasan sejarah ini ke dalam dua periode utama dan mengidentifikasi dua belas algoritma pelopor sebagai tonggak sejarah (*milestone*). Selain meninjau arsitektur detektor, survei ini juga menyusun taksonomi teknis mengenai representasi multi-skala, strategi akselerasi sistem, dataset tolok ukur, serta metrik evaluasi standar.

Tujuan utama dari penulisan survei ini adalah memberikan pemetaan evolusi teknologi yang terpadu bagi para peneliti. Dengan menganalisis perubahan paradigma dari deteksi berbasis bagian terdeformasi (*deformable part models*) menjadi deteksi *end-to-end* berbasis jaringan saraf konvolusional (*convolutional neural networks*), makalah ini memaparkan bagaimana peningkatan efisiensi komputasi dicapai pada tingkat arsitektur, *pipeline*, dan optimasi numerik. Hasil akhirnya adalah peta jalan historis yang menjadi acuan penting untuk memahami bagaimana detektor modern beroperasi dan ke mana arah pengembangan riset di masa mendatang.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum publikasi survei ini, literatur deteksi objek sangat terfragmentasi. Bidang deteksi objek mengalami peningkatan jumlah penelitian dan publikasi setelah kemunculan pembelajaran mendalam, namun terdapat keterbatasan dokumentasi yang menghubungkan penemuan modern dengan teknik klasik yang mendahuluinya. Sebagian peneliti baru mengabaikan prinsip-prinsip dasar yang dikembangkan pada era fitur buatan tangan, seperti penambangan sampel negatif yang sulit (*hard negative mining*) atau representasi multi-skala, padahal prinsip-prinsip tersebut tetap diadopsi dan diadaptasi dalam arsitektur *deep learning*.

Kekurangan spesifik dari literatur sebelumnya adalah tidak adanya taksonomi yang terpadu untuk mengklasifikasikan teknik akselerasi deteksi objek. Saat kecepatan menjadi kebutuhan utama untuk implementasi praktis, optimasi kecepatan sering kali dibahas secara parsial pada tingkat perancangan tulang punggung (*backbone*) jaringan atau teknik pascapemrosesan saja. Selain itu, perkembangan dataset *benchmark* dari skala kecil (seperti PASCAL VOC awal) ke skala masif (seperti MS COCO atau Open Images) belum dipetakan secara kronologis untuk memperlihatkan bagaimana data memicu peningkatan kapasitas model deteksi. Pemetaan masalah ini penting karena pemahaman yang parsial dapat menghambat inovasi desain arsitektur baru yang efisien.

## Ide Utama
Gagasan inti makalah ini adalah menyusun taksonomi perkembangan deteksi objek secara komprehensif dengan membaginya ke dalam dua era kronologis: Era Fitur Buatan Tangan (2001–2013) dan Era Pembelajaran Mendalam (2014–sekarang). Penulis menetapkan dua belas algoritma kunci sebagai jangkar evolusi teknologi untuk melacak bagaimana fitur visual diekstraksi dan bagaimana *bounding box* (kotak pembatas) diprediksi.

Pada era *deep learning*, kontribusi dipecah menjadi klasifikasi detektor dua-tahap (*two-stage detectors*) dan detektor satu-tahap (*one-stage detectors*), serta transisi ke pendekatan berbasis titik kunci (*keypoint-based* atau *anchor-free*). Sebagai tambahan, makalah ini merumuskan taksonomi tiga tingkat untuk teknik akselerasi deteksi: tingkat alur kerja (*pipeline*), tingkat jaringan ekstraksi fitur (*backbone*), dan tingkat komputasi numerik dasar.

## Cara Kerja Langkah demi Langkah
Sebagai makalah peninjauan literatur (*survey paper*), struktur langkah demi langkah disesuaikan untuk menjelaskan metodologi survei dan taksonomi yang diajukan oleh Zou dkk.

### Segmentasi Era Historis
Penulis membagi perkembangan deteksi objek menjadi dua periode utama:
1. **Periode Deteksi Objek Tradisional (2001–2013):** Era ini dimulai dengan penemuan detektor Viola-Jones pada tahun 2001, yang memanfaatkan fitur *Haar-like* dan algoritma *AdaBoost* untuk mendeteksi wajah secara *real-time*. HOG (*Histogram of Oriented Gradients*) diperkenalkan pada tahun 2005 untuk menangkap gradien arah piksel lokal, yang sangat efektif untuk deteksi pejalan kaki (*pedestrian detection*). DPM (*Deformable Part Model*) pada tahun 2008 mengakhiri era ini dengan memodelkan objek secara fleksibel sebagai kumpulan bagian-bagian objek yang saling terhubung melalui fungsi deformasi pegas.
2. **Periode Deteksi Objek Berbasis Deep Learning (2014–sekarang):** Era ini dipicu oleh keberhasilan AlexNet pada tantangan ImageNet, yang diikuti oleh R-CNN pada tahun 2014. R-CNN menggantikan fitur buatan tangan dengan fitur yang dipelajari secara otomatis oleh jaringan saraf konvolusional.

### Taksonomi Arsitektur Detektor
Model deteksi objek berbasis *deep learning* diklasifikasikan ke dalam tiga kategori utama:
1. **Dua-Tahap (*Two-Stage*):** Proses deteksi dibagi menjadi tahap generasi usulan wilayah (*region proposal*) dan tahap klasifikasi serta regresi kotak pembatas. Jalur evolusinya dimulai dari R-CNN yang lambat karena mengekstrak fitur untuk setiap proposal secara terpisah, diikuti SPPNet (*Spatial Pyramid Pooling*) yang memperkenalkan ekstraksi fitur peta citra tunggal secara bersama (*shared feature map*), Fast R-CNN yang memadukan pooling ROI (*Region of Interest*) ke dalam jaringan *end-to-end*, dan Faster R-CNN yang mengintegrasikan RPN (*Region Proposal Network*) untuk memprediksi proposal langsung pada fitur konvolusi.
2. **Satu-Tahap (*One-Stage*):** Proses deteksi dilakukan dalam satu kali evaluasi *feed-forward* langsung dari citra masukan ke koordinat kotak pembatas dan probabilitas kelas. Aliran ini dipelopori oleh YOLOv1 (*You Only Look Once*) yang membagi citra menjadi sel grid dan memprediksi kotak pembatas secara regresif, SSD (*Single Shot MultiBox Detector*) yang menggunakan peta fitur multi-skala untuk mendeteksi objek dengan ukuran berbeda, dan RetinaNet yang mengatasi ketidakseimbangan kelas (*class imbalance*) ekstrem melalui formulasi *Focal Loss*.
3. **Tanpa Jangkar (*Anchor-Free*):** Menghilangkan penggunaan kotak jangkar (*anchor boxes*) yang membutuhkan *hyperparameter* manual rumit. Contohnya adalah CornerNet yang mendeteksi objek sebagai pasangan titik kunci (kiri-atas dan kanan-bawah) serta CenterNet yang memodelkan objek sebagai titik pusat tunggal dengan regresi ukuran.

### Evolusi Pendekatan Multi-Skala
Penulisan survei ini membagi metode penanganan objek multi-skala ke dalam empat strategi utama:
1. *Image Pyramid*: Citra masukan diubah ukurannya ke berbagai skala, dan detektor dievaluasi pada setiap skala citra secara terpisah. Pendekatan ini akurat tetapi memiliki beban komputasi tinggi.
2. *Single Feature Map*: Menggunakan satu peta fitur tunggal dari lapisan konvolusi terakhir untuk melakukan prediksi. Pendekatan ini cepat tetapi berkinerja buruk pada objek berukuran kecil karena hilangnya detail spasial.
3. *Multi-Scale Feature Maps (SSD)*: Prediksi dilakukan pada peta fitur dari lapisan konvolusi yang berbeda. Lapisan yang lebih dangkal mendeteksi objek kecil karena memiliki resolusi spasial tinggi, sedangkan lapisan yang lebih dalam mendeteksi objek besar karena memiliki bidang penerima (*receptive field*) yang luas.
4. *Feature Pyramid Networks (FPN)*: Menggabungkan fitur semantik tingkat tinggi dari lapisan dalam ke fitur spasial resolusi tinggi dari lapisan dangkal melalui koneksi lateral dan jalur *top-down*.

### Taksonomi Teknik Akselerasi Deteksi
Zou dkk. memetakan teknik akselerasi deteksi objek menjadi tiga tingkat hierarkis:
1. **Akselerasi Alur Kerja (*Pipeline Speed-up*):** Mengoptimalkan alur pemrosesan detektor, misalnya dengan berbagi komputasi peta fitur antara tahap proposal dan tahap klasifikasi (seperti pada Fast R-CNN), mengurangi jumlah proposal wilayah, atau menggunakan deteksi berbasis *cascade* (seperti Viola-Jones *cascade*).
2. **Akselerasi Tulang Punggung (*Backbone Speed-up*):** Mendesain jaringan ekstraksi fitur yang ringan atau melakukan kompresi model. Metode yang umum mencakup penggunaan konvolusi terpisah mendalam (*depthwise separable convolution*) seperti pada MobileNet, pemangkasan saluran (*channel pruning*), kuantisasi bobot (*weight quantization*), dan distilasi pengetahuan (*knowledge distillation*).
3. **Akselerasi Komputasi Numerik (*Numerical Computation Speed-up*):** Menggunakan teknik matematika untuk mempercepat operasi konvolusi dasar, seperti integral citra (*integral image*) untuk fitur Haar, transformasi Fourier cepat (*Fast Fourier Transform*), dan algoritma Winograd untuk komputasi matriks konvolusi yang efisien.

### Pemetaan Evolusi Dataset dan Metrik Evaluasi
Survei ini meninjau transisi dataset tolok ukur utama dari PASCAL VOC (20 objek, ±11.530 citra), MS COCO (80 objek, ±328.000 citra), hingga Open Images (600 objek, ±1,9 juta citra). Metrik evaluasi dijabarkan secara matematis dari tingkat *Intersection over Union* (IoU), presisi (*precision*), *recall*, hingga perhitungan *Mean Average Precision* (mAP) pada ambang batas IoU yang bervariasi (misalnya mAP@0.5 dan mAP@0.5:0.95).

Diagram berikut memvisualisasikan taksonomi terpadu yang dirumuskan oleh Zou dkk.:

```
                            TAKSONOMI ZOU ET AL.
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           ▼                         ▼                         ▼
   TAKSONOMI DETEKTOR        AKSELERASI SISTEM        MULTI-SKALA & DATASET
     (Era & Desain)         (Tiga Level Optimasi)     (Evolusi Standardisasi)
           │                         │                         │
     ┌─────┴─────┐             ┌─────┼─────┐             ┌─────┴─────┐
     ▼           ▼             ▼     ▼     ▼             ▼           ▼
 Traditional    Deep     Pipeline  Backbone Numerical  Strategi   Dataset &
  Detectors  Learning     (Shared   (Light- (Integral    Multi-     Metrik
  (VJ, HOG,  (Two-Stage,  Feature,  weight,  Image,    Skala (FPN,  (VOC, COCO,
    DPM)     One-Stage,  Cascade)  Pruning) Winograd)   Pyramids)    mAP)
            Anchor-free)
```

## Eksperimen dan Hasil
Sebagai makalah survei, evaluasi eksperimen dilakukan dengan membandingkan hasil-hari kuantitatif dari berbagai detektor pada dataset standar yang dihimpun dari literatur. Survei ini mengompilasi data performa mAP dan kecepatan (FPS) pada dataset PASCAL VOC 2007, VOC 2012, dan MS COCO.

Tabel di bawah ini merangkum evolusi performa detektor penting pada dataset MS COCO (mAP@0.5:0.95 dan mAP@0.5) berdasarkan data kompilasi yang disajikan oleh Zou dkk.:

| Detektor | Tahun | Backbone | mAP@0.5:0.95 (%) | mAP@0.5 (%) |
|---|---|---|---|---|
| R-CNN | 2014 | AlexNet | - | 31,4 |
| Fast R-CNN | 2015 | VGG-16 | 19,7 | 35,9 |
| Faster R-CNN | 2015 | VGG-16 | 21,9 | 42,7 |
| YOLOv1 | 2016 | DarkNet-24 | - | 37,8 |
| SSD300 | 2016 | VGG-16 | 23,2 | 41,2 |
| RetinaNet | 2017 | ResNet-101 | 39,1 | 59,1 |
| CornerNet | 2018 | Hourglass-104 | 40,5 | 56,5 |

Interpretasi hasil menunjukkan bahwa transisi dari dua-tahap awal (R-CNN) ke satu-tahap awal (YOLOv1) mengorbankan akurasi demi kecepatan komputasi. R-CNN membutuhkan waktu sekitar 47 detik per citra untuk pengujian menggunakan GPU K40, sedangkan YOLOv1 mampu memproses citra secara langsung pada kecepatan 45 FPS (bingkai per detik). Namun, pengenalan RetinaNet dengan ResNet-101 menunjukkan bahwa penanganan ketidakseimbangan kelas menggunakan *Focal Loss* mampu mendongkrak performa satu-tahap hingga mencapai mAP 39,1% pada MS COCO, melampaui Faster R-CNN dua-tahap (21,9%) dengan kecepatan yang tetap bersaing.

## Kelebihan dan Keterbatasan
Kelebihan utama dari survei yang disusun oleh Zou dkk. adalah kedalaman analisis historisnya yang melacak benang merah teknologi lintas era. Berbeda dengan survei lain yang hanya berfokus pada daftar model *deep learning*, makalah ini berhasil menstrukturkan prinsip rekayasa di balik optimasi deteksi objek, seperti bagaimana konsep *hard negative mining* dari era tradisional bertransformasi menjadi *Focal Loss* pada era modern. Pengelompokan taksonomi teknik akselerasi ke dalam tiga level sistematis memberikan kerangka kerja yang jelas bagi praktisi rekayasa perangkat lunak untuk mengidentifikasi *bottleneck* komputasi.

Namun, dari sisi rekayasa dan konseptual, terdapat beberapa keterbatasan dalam survei ini. Makalah ini tidak secara mendalam mengulas metode deteksi objek berbasis Transformer (seperti DETR dan varian Deformable DETR) karena basis penulisan draf awalnya diselesaikan sebelum arsitektur Transformer mendominasi bidang visi komputer. Selain itu, secara konseptual, survei ini membatasi cakupannya hanya pada citra RGB 2D konvensional. Makalah ini tidak membahas deteksi objek multimodal yang mengintegrasikan data kedalaman (RGB-D) atau sensor termal (RGB-T), yang merupakan pilar penting dalam sistem kemudi otonom dan robotika masa kini. Ini membuat relevansi langsungnya terhadap topik fusi multisensor menjadi terbatas, sehingga pembaca harus merujuk pada literatur khusus fusi multimodal untuk mendapatkan gambaran utuh tentang sistem multisensor.

## Kaitan dengan Bab Lain
Sebagai bagian dari klaster **Fusi Multimodal**, bab ini menempati posisi yang unik karena menyajikan landasan teori deteksi objek visual berbasis kamera RGB tunggal. Seluruh arsitektur fusi multimodal untuk deteksi objek (baik yang menggunakan data kedalaman maupun termal) dibangun di atas struktur detektor RGB dasar yang diulas oleh Zou dkk.

Bab ini mewarisi komponen ekstraksi fitur dari bab fondasi seperti [147 - ResNet](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md), yang dibahas dalam survei ini sebagai tulang punggung (*backbone*) utama bagi sebagian besar detektor era *deep learning*. Selanjutnya, bab ini menjadi jembatan konseptual langsung menuju bab survei yang lebih spesifik seperti [150 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.)](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md) dan [152 - Deep Multimodal Learning A Survey (Ramachandram & Taylor)](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md). Jika Zou dkk. menyajikan taksonomi deteksi dalam domain RGB, Feng dkk. dan Ramachandram & Taylor meluaskan taksonomi tersebut ke tingkat fusi multisensor (seperti kamera, LiDAR, dan radar). 

Di sisi lain, pembahasan dataset visual dalam bab ini terhubung erat dengan [154 - Survei Dataset RGB-D (Lopes dkk.)](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md) dan [153 - Survei RGB-D SOD (Zhou dkk.)](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md), di mana evolusi dataset bergerak dari standardisasi pengujian berbasis citra warna menuju dataset spasial 3D yang lebih kompleks.

## Poin untuk Sitasi
`zou2023objectdetectionsurvey`
Zou dkk. menyajikan survei perkembangan deteksi objek selama 20 tahun yang memetakan evolusi dari era fitur buatan tangan hingga era pembelajaran mendalam, serta merumuskan taksonomi detektor (dua-tahap vs satu-tahap), strategi multi-skala, dan teknik akselerasi sistem. Kerangka kerja ini menjadi referensi teoretis penting untuk memahami bagaimana detektor modern bertumpu pada pondasi algoritma klasik.

Catatan angka/klaim yang perlu diverifikasi:
- Nilai akurasi mAP pada MS COCO untuk model-model awal (R-CNN, Fast R-CNN, Faster R-CNN, YOLOv1, SSD) perlu dicocokkan dengan laporan publikasi masing-masing makalah untuk memastikan tidak adanya distorsi pembulatan atau variasi implementasi pengujian.
- Kecepatan pemrosesan (FPS) dan GPU spesifik yang digunakan pada setiap pengujian model yang dikompilasi memengaruhi klaim performa komputasi secara signifikan, sehingga memerlukan konfirmasi perangkat keras asli pada masing-masing naskah primer.
