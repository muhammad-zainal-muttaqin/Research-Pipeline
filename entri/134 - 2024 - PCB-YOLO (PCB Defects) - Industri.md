# 134 - PCB-YOLO: Enhancing PCB Surface Defect Detection with Coordinate Attention and Multi-Scale Feature Fusion

## Metadata Ringkas
| Kunci BibTeX | `tang2024pcbyolo` |
| Judul asli | PCB-YOLO: Enhancing PCB Surface Defect Detection with Coordinate Attention and Multi-Scale Feature Fusion |
| Penulis | Tang, Junyan; others |
| Tahun | 2024 |
| Venue | PLOS ONE |
| Tema | Industri |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PCB-YOLO%3A%20Enhancing%20PCB%20Surface%20Defect%20Detection%20with%20Coordinate%20Attention%20and%20Multi-Scale%20Feature%20Fusion
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PCB-YOLO%3A%20Enhancing%20PCB%20Surface%20Defect%20Detection%20with%20Coordinate%20Attention%20and%20Multi-Scale%20Feature%20Fusion&sort=relevance

## Gambaran Umum
Makalah ini memperkenalkan *PCB-YOLO*, sebuah model deteksi objek satu tahap (*single-stage detector*) untuk mendeteksi cacat permukaan papan sirkuit cetak (*printed circuit board* atau PCB) secara akurat dan efisien. Inspeksi kualitas visual PCB dituntut mendeteksi cacat berukuran mikro secara padat pada sirkuit tembaga. PCB-YOLO memodifikasi model *YOLOv8n* untuk menekan jumlah parameter model sekaligus meningkatkan resolusi fitur spasial cacat kecil.

PCB-YOLO mencapai *mean Average Precision* (mAP50) sebesar 98,8% pada dataset PKU-Market-PCB, naik 3,1% dibanding baseline *YOLOv8n*. Peningkatan ini dicapai dengan pengurangan parameter model sebesar 13,3% (menjadi 2,6 M) dan beban komputasi (*floating-point operations* atau FLOPs) sebesar 14,8% (menjadi 6,9 G). Model ini juga bergeneralisasi dengan baik pada dataset cacat permukaan baja NEU-DET dengan mAP50 sebesar 79,2%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
PCB menentukan keandalan fungsional produk elektronik. Cacat permukaan seperti lubang bor yang hilang (*missing hole*), gigitan tikus (*mouse bite*), sirkuit terbuka (*open circuit*), tonjolan logam (*spur*), hubung singkat (*short circuit*), dan tembaga liar (*spurious copper*) harus diidentifikasi demi mencegah kegagalan sistematis perangkat elektronik.

Metode inspeksi optik otomatis (*automated optical inspection* atau AOI) tradisional berbasis pencocokan pola (*template matching*) sangat sensitif terhadap fluktuasi cahaya dan posisi papan, memicu alarm palsu (*false alarm*) yang tinggi. Penerapan model pembelajaran mendalam (*deep learning*) dua tahap seperti *Faster R-CNN* memiliki akurasi lebih baik, tetapi beban parameter yang besar dan kecepatan lambat (17,4 FPS) tidak cocok untuk inspeksi inline waktu nyata. Sebaliknya, detektor satu tahap yang lebih ringan seperti *YOLOv8n* sering kali melewatkan cacat mikro karena hilangnya detail spasial pada lapisan konvolusi yang dalam. Keseimbangan antara ukuran model dan akurasi deteksi cacat kecil menjadi tantangan utama yang harus dipecahkan.

## Ide Utama
Gagasan inti PCB-YOLO adalah mereduksi redundansi fitur pada saluran ekstraksi untuk menekan parameter, seraya memperkuat representasi spasial lokal dan koordinat posisi untuk mendeteksi cacat kecil. Ide utama ini diwujudkan melalui tiga modifikasi:
1. **Modul CRSCC (*Channel-Reconstruction and Spatial-Channel Convolution*):** Menggantikan modul *C2f* pada backbone untuk memurnikan informasi fitur spasial-saluran dan memangkas parameter redundan.
2. **Modul Atensi FFCA (*Feature Fusion Coordinate Attention*):** Memasang modul atensi koordinat pada neck fusi fitur multi-skala untuk menyandikan koordinat posisi horizontal dan vertikal secara terpisah guna mempertahankan resolusi spasial cacat mikro.
3. **Fungsi Kerugian WIPIoU (*Wise-Inner-MPDIoU*):** Menggantikan fungsi kerugian *CIoU* standar pada head dengan kerugian regresi yang mengintegrasikan batas pembantu (*auxiliary bounding boxes*) untuk mempercepat konvergensi gradien target kecil dan mengurangi sensitivitas terhadap data berkualitas rendah.

## Cara Kerja Langkah demi Langkah

### Prapemrosesan dan Ekspansi Dataset PKU-Market-PCB
Dataset PKU-Market-PCB berisi 673 citra asli beresolusi 640x640 piksel dengan enam jenis cacat permukaan PCB. Guna mencegah *overfitting*, penulis menerapkan augmentasi data sebanyak 6 kali lipat melalui rotasi acak, translasi spasial, penambahan derau (*noise*), dan penyesuaian kontras. Langkah ini meningkatkan jumlah total citra latih secara signifikan menjadi 4.038 citra.

### Modul Ekstraksi Fitur CRSCC
Guna menekan komputasi backbone, PCB-YOLO menggantikan modul *C2f* bawaan *YOLOv8n* dengan modul CRSCC. CRSCC mengintegrasikan struktur SCConv (*Spatial and Channel Reconstruction Convolution*) ke dalam percabangan *C2f*. SCConv memisahkan operasi konvolusi menjadi dua unit utama:
- SRU (*Spatial Reconstruction Unit*): Memisahkan saluran input berdasarkan variansi spasial untuk mengisolasi fitur cacat yang menonjol dari latar belakang. Saluran bervariansi spasial tinggi diperkuat, sedangkan saluran bervariansi rendah ditekan untuk menekan derau.
- CRU (*Channel Reconstruction Unit*): Mengurangi redundansi dimensi saluran menggunakan konvolusi parsial (*G-Conv* dan *P-Conv*) yang ringan, diikuti oleh penggabungan (*concat*) dan pertukaran saluran (*channel shuffle*) untuk memastikan pencampuran informasi.

Pemasangan modul CRSCC pada lapisan ke-7 dan ke-9 (Backbone7_9) menghasilkan performa paling optimal: mAP50 meningkat menjadi 96,3% dan parameter model turun menjadi 2,6 M, dibandingkan baseline *YOLOv8n* (mAP50 = 95,7%, parameter = 3,0 M).

### Mekanisme Atensi Koordinat FFCA
Cacat permukaan PCB berukuran mikro rentan hilang akibat operasi penyusutan dimensi di bagian neck. FFCA mengatasi kelemahan ini dengan memisahkan pooling spasial global menjadi pooling horizontal ($X$) dan vertikal ($Y$):
- Masukan fitur $H \times W$ dipisahkan menjadi dua jalur pooling satu dimensi sepanjang koordinat horizontal dan vertikal untuk menghasilkan peta fitur yang peka terhadap arah (*direction-aware*).
- Kedua peta fitur ini digabungkan dan diproses oleh konvolusi 1x1 bersama untuk merekam ketergantungan jarak jauh.
- Fitur hasil penggabungan dipecah kembali, dilewatkan melalui fungsi aktivasi sigmoid untuk menghasilkan bobot atensi arah horizontal dan vertikal, lalu dikalikan ke peta fitur masukan.

Penerapan FFCA pada leher jaringan menaikkan mAP50 sebesar 2,2 percentage points (menjadi 98,4% dalam ablation study), mempertahankan detail spasial cacat kecil.

### Fungsi Kerugian Regresi Bounding Box WIPIoU
WIPIoU menggantikan fungsi kerugian *CIoU* untuk meningkatkan sensitivitas gradien pada cacat kecil dengan mengintegrasikan tiga konsep:
- *Wise-IoU* (WIoU): Menerapkan mekanisme fokus dinamis untuk mereduksi pengaruh gradien dari sampel berkualitas rendah (derau anotasi), sehingga fokus pelatihan tertuju pada sampel kualitas sedang.
- *Inner-IoU*: Memperkenalkan kotak pembatas pembantu (*auxiliary bounding box*) yang skalanya disesuaikan dinamis melalui faktor rasio skala ($\lambda$). Ini membuat gradien regresi lebih sensitif terhadap pergeseran posisi cacat kecil.
- *MPDIoU*: Mengukur kerugian berdasarkan jarak titik-titik sudut diagonal kotak prediksi dan kotak kebenaran, menyederhanakan kalkulasi kesamaan bentuk dan mempercepat konvergensi gradien.

Penerapan WIPIoU meningkatkan mAP50 sebesar 0,4% (menjadi 98,8%) dan mempercepat penurunan kerugian pelatihan.

Berikut adalah visualisasi diagram alur data dan arsitektur model PCB-YOLO:

```
           Alur Pemrosesan Citra Masukan pada PCB-YOLO
           
   Input Image (640x640x3)
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Backbone: YOLOv8n (Layer 1 - Layer 6)         │
   └────────┬──────────────────────────────────────┘
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Backbone Layer 7: CRSCC Module (SCConv + C2f) │ <── Menekan redundansi
   └────────┬──────────────────────────────────────┘     saluran & parameter
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Backbone Layer 8: Conv & SPPF                 │
   └────────┬──────────────────────────────────────┘
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Backbone Layer 9: CRSCC Module (SCConv + C2f) │
   └────────┬──────────────────────────────────────┘
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Neck: PANet Fusi Fitur Multi-Skala            │ <── Meningkatkan atensi
   │       + FFCA Attention Modules (X-Y Pooling)  │     spasial cacat mikro
   └────────┬──────────────────────────────────────┘
            │
            ▼
   ┌───────────────────────────────────────────────┐
   │ Head: Decoupled Detection Head                │ <── Regresi presisi
   │       (Loss: WIPIoU dengan Kotak Pembantu)    │     pada target kecil
   └───────────────────────────────────────────────┘
```

## Eksperimen dan Hasil
Model dilatih menggunakan optimizer SGD, momentum 0,937, weight decay 0,0005, batch size 16, dan dilatih selama 300 epoch. Hasil perbandingan model pada dataset PKU-Market-PCB menunjukkan:
- PCB-YOLO mencapai **mAP50 sebesar 98,8%**, Precision 96,3%, Recall 97,9%, FPS 102,8, dengan parameter 2,6 M, dan FLOPs 6,9 G.
- Baseline *YOLOv8n* mencapai **mAP50 sebesar 95,7%**, Precision 94,5%, Recall 88,9%, FPS 94,3, dengan parameter 3,0 M, dan FLOPs 8,1 G.

PCB-YOLO menghasilkan peningkatan mAP50 sebesar **3,1 percentage points**, dengan parameter berkurang **13,3%** dan beban komputasi berkurang **14,8%**. Selain itu, kecepatan deteksi meningkat dari 94,3 FPS menjadi 102,8 FPS, memenuhi batas waktu nyata.

Dibandingkan dengan model satu tahap (*one-stage*) dan dua tahap (*two-stage*) lainnya:
- *Faster R-CNN* menghasilkan mAP50 lebih rendah (88,3%) dengan kecepatan lambat (17,4 FPS).
- *SSD* mencapai mAP50 sebesar 93,4% dengan parameter 38,8 M dan komputasi 12,3 GFLOPs.
- *RT-DETR-L* mencapai mAP50 sebesar 97,3%, tetapi parameter modelnya sangat besar (103,5 M) dengan FPS lambat (19,7 FPS).
- *YOLOv7-tiny* (94,6% mAP50) dan *YOLO11n* (94,4% mAP50) berada di bawah performa PCB-YOLO.
- *YOLO-HMC* mencapai mAP50 tinggi sebesar 98,6%, tetapi memerlukan parameter 5,94 M.

Untuk menguji performa generalisasi, model dievaluasi pada dataset cacat permukaan baja NEU-DET. PCB-YOLO mencapai mAP50 sebesar **79,2%** dengan parameter 2,6 M dan FLOPs 6,9 G. Hasil ini melampaui baseline *YOLOv8n* (mAP50 = 73,7%) sebesar **5,5 percentage points** dan setara dengan model *GLF-NET* (mAP50 = 79,2%) yang memiliki parameter jauh lebih besar (12,0 M) serta komputasi yang lebih berat (34,6 GFLOPs).

## Kelebihan dan Keterbatasan

**Kelebihan:**
PCB-YOLO menunjukkan keseimbangan performa yang sangat baik antara akurasi deteksi tinggi (mAP50 = 98,8%) dan sifat ringan model (parameter = 2,6 M, FLOPs = 6,9 G). Karakteristik ini memungkinkan model dideploy pada perangkat keras tertanam (*embedded hardware*) lokal di pabrik manufaktur elektronik dengan laju inferensi mencapai 102,8 FPS. Penerapan modul CRSCC yang berbasis SCConv terbukti berhasil memangkas redundansi spasial-saluran secara efektif. Selain itu, model ini menunjukkan kemampuan generalisasi lintas domain yang sangat baik (NEU-DET), membuktikan kekokohan arsitekturnya dalam mengenali cacat permukaan logam secara umum.

**Keterbatasan:**
*Dari sisi rekayasa*, PCB-YOLO masih bergantung pada citra masukan RGB dua dimensi statis. Di lingkungan lini produksi industri nyata, sirkuit tembaga pada PCB sering kali menghasilkan efek pantulan cahaya specular (*specular reflection*) atau bayangan akibat sudut pencahayaan yang tidak merata, memicu alarm palsu (*false alarm*) yang tinggi. Model ini belum mengintegrasikan informasi spasial kedalaman (*depth*) atau teknik pencahayaan terstruktur untuk mengatasi fluktuasi optik tersebut.

*Secara konseptual*, fungsi kerugian WIPIoU sangat bergantung pada faktor rasio skala kotak pembantu ($\lambda$) yang disetel secara manual dan empiris. Jika diterapkan pada dataset dengan ukuran objek cacat yang bervariasi secara ekstrem, keampuhan kotak pembantu statis ini dapat menurun, menuntut penyetelan ulang hiperparameter yang memakan waktu. Terdapat pula ketidakkonsistenan minor dalam naskah asli PLOS ONE di mana pada bagian kesimpulan dilaporkan peningkatan mAP50 sebesar 5,7% pada dataset PKU-Market-PCB, sementara data eksperimen menunjukkan angka 5,7% (atau tepatnya 5,5%) tersebut sebenarnya terjadi pada dataset generalisasi NEU-DET, sedangkan peningkatan pada dataset utama adalah 3,1% (dari 95,7% ke 98,8%).

## Kaitan dengan Bab Lain
PCB-YOLO memiliki keterkaitan erat dalam silsilah pengembangan deteksi cacat permukaan industri dengan bab-bab berikut:
- **[EFC-YOLO (Steel Strip Defects)](./133%20-%202023%20-%20EFC-YOLO%20%28Steel%20Strip%20Defects%29%20-%20Industri.md):** Kedua model ini berfokus pada deteksi cacat permukaan industri yang berukuran kecil dan tipis. EFC-YOLO menggunakan baseline *YOLOv7* dan memangkas beban komputasi dengan *Partial Convolution* (PConv) serta menambahkan atensi koordinat SCA (*Shortcut Coordinate Attention*). PCB-YOLO mewarisi gagasan pemangkasan parameter dan penyandian koordinat spasial tersebut, tetapi menerapkan baseline yang lebih baru (*YOLOv8n*), menggantikan modul *C2f* dengan modul CRSCC yang berbasis SCConv, dan mengintegrasikan modul atensi FFCA di bagian neck. Kedua makalah membuktikan bahwa penyandian koordinat spasial (*Coordinate Attention*) adalah kunci mendeteksi cacat kecil secara efisien.
- **[Review Defect Detection (Bhatt dkk.)](./135%20-%202021%20-%20Review%20Defect%20Detection%20%28Bhatt%20dkk.%29%20-%20Industri.md):** Bhatt dkk. merumuskan taksonomi deteksi cacat permukaan dan mengidentifikasi tantangan kritis seperti kelangkaan data cacat (*data scarcity*), variabilitas kondisi lingkungan pabrik, dan batasan pemrosesan waktu nyata (*real-time*). PCB-YOLO menjawab tantangan kelangkaan data secara praktis melalui ekspansi dataset PKU-Market-PCB sebanyak 6 kali lipat (dari 673 menjadi 4.038 citra), serta memperkenalkan fungsi kerugian WIPIoU yang toleran terhadap derau data lantai produksi.
- **[Safety Helmet Detection (Improved YOLOv5)](./136%20-%202021%20-%20Safety%20Helmet%20Detection%20%28Improved%20YOLOv5%29%20-%20Industri.md):** Analisis trade-off antara akurasi (mAP) dan kecepatan inferensi (FPS) pada PCB-YOLO beresonansi langsung dengan metodologi evaluasi yang dilakukan oleh Zhou dkk. pada pemantauan helm keselamatan K3 menggunakan empat varian *YOLOv5* (YOLOv5s hingga YOLOv5x). PCB-YOLO membuktikan bahwa modifikasi arsitektur yang cermat (CRSCC + FFCA + WIPIoU) pada detektor teringan (*YOLOv8n*) mampu melampaui akurasi model besar (*YOLOv8x*) sekaligus mempertahankan kecepatan di atas 100 FPS.

## Poin untuk Sitasi
Kunci BibTeX untuk bab ini adalah `tang2024pcbyolo`.

Model PCB-YOLO menyempurnakan arsitektur detektor *YOLOv8n* untuk inspeksi cacat permukaan papan sirkuit cetak (PCB) dengan menggabungkan modul konvolusi rekonstruksi spasial-saluran (CRSCC) pada backbone, modul atensi koordinat fusi fitur (FFCA) di bagian neck, dan fungsi kerugian WIPIoU di bagian head. Model ini mencapai mAP50 sebesar 98,8% pada dataset PKU-Market-PCB dengan kecepatan 102,8 FPS, menjadikannya sangat cocok untuk deteksi cacat mikro secara langsung pada perangkat komputasi tepi di lini produksi manufaktur elektronik.

*Catatan untuk verifikasi:*
Terdapat ketidaksesuaian kecil dalam naskah asli terkait nama penulis yang terdaftar di BibTeX key `tang2024pcbyolo` (Tang dkk., Sustainability 2023 yang mendeteksi cacat PCB berbasis YOLOv5) dengan judul dan naskah PLOS ONE volume 19 nomor 5 yang dibahas di sini (ditulis oleh Ze Wei dkk., PLOS ONE 2024/2025 yang berbasis YOLOv8n). Selain itu, terdapat ketidakkonsistenan pelaporan peningkatan mAP50 sebesar 5,7% di bagian kesimpulan naskah PLOS ONE, yang secara numerik merujuk pada performa generalisasi di dataset NEU-DET (73,7% menjadi 79,2% setara 5,5%), sedangkan peningkatan pada dataset utama PKU-Market-PCB adalah 3,1% (95,7% menjadi 98,8%).
