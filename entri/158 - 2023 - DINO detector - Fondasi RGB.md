# 158 - DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2023dino` |
| Judul asli | DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection |
| Penulis | Zhang, Hao; Li, Feng; Liu, Shilong; Zhang, Lei; Su, Hang; Zhu, Jun; Ni, Lionel M.; Shum, Heung-Yeung |
| Tahun | 2023 |
| Venue | International Conference on Learning Representations (ICLR) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2203.03605
- **Google Scholar:** https://scholar.google.com/scholar?q=DINO%3A%20DETR%20with%20Improved%20DeNoising%20Anchor%20Boxes%20for%20End-to-End%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=DINO%3A%20DETR%20with%20Improved%20DeNoising%20Anchor%20Boxes%20for%20End-to-End%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DINO (*DETR with Improved DeNoising Anchor Boxes*), sebuah detektor objek berbasis *transformer* ujung-ke-ujung (*end-to-end*) yang dirancang untuk mengatasi lambatnya konvergensi pelatihan dan ketidakstabilan optimasi pada arsitektur DETR (*DEtection TRansformer*) awal. DINO mengintegrasikan tiga pembaruan utama untuk meningkatkan efisiensi dan performa deteksi, yaitu pelatihan de-noising kontrastif (*contrastive denoising training*), seleksi kueri campuran (*mixed query selection*), dan skema pembaruan koordinat *look-forward-twice*. Kombinasi dari ketiga metode ini menstabilkan pencocokan data serta mengoptimalkan inisialisasi kueri objek (*object queries*) pada dekoder.

Pada dataset MS COCO, DINO dengan tulang punggung (*backbone*) ResNet-50 mencapai rata-rata presisi *mean Average Precision* (mAP) sebesar 49,4% dalam waktu pelatihan singkat yaitu 12 epoch, dan meningkat menjadi 51,3% mAP dalam 24 epoch. Ketika diperluas menggunakan tulang punggung Swin Transformer Large dengan prapelatihan (*pre-training*) pada dataset Objects365, DINO mencatatkan akurasi puncak sebesar 63,2% mAP pada set validasi COCO `val2017` tanpa membutuhkan algoritme pascapemrosesan tambahan seperti *Non-Maximum Suppression* (NMS).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum DINO dikembangkan, sebagian besar detektor objek berkinerja tinggi mengandalkan arsitektur berbasis kotak acuan (*anchor*) konvensional seperti [004 - YOLOv4](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md) atau [014 - Faster R-CNN](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md). Jaringan-jaringan ini menghasilkan ribuan kandidat kotak pembatas (*bounding box*) yang tumpang tindih sehingga membutuhkan tahap pascapemrosesan berupa NMS untuk menyaring duplikasi deteksi. Prosedur NMS ini memiliki kelemahan inheren karena kinerjanya sangat sensitif terhadap pengaturan ambang batas (*threshold*) yang ditentukan secara heuristik dan sulit untuk diintegrasikan secara optimal dalam skema pelatihan ujung-ke-ujung.

Arsitektur [022 - DETR](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md) hadir sebagai alternatif dengan memperkenalkan pencocokan himpunan ujung-ke-ujung (*end-to-end bipartite matching*) menggunakan algoritma Hungarian. Pendeketan ini mencocokkan setiap objek acuan (*ground-truth*) dengan tepat satu prediksi kueri objek yang paling sesuai, sehingga menghilangkan kebutuhan akan NMS secara penuh. Meskipun demikian, DETR generasi awal memiliki keterbatasan dalam hal konvergensi pelatihan yang sangat lambat, sering kali membutuhkan 500 epoch pelatihan untuk menyamai performa detektor berbasis jaringan saraf konvolusional (*convolutional neural network* atau CNN) konvensional. Lambatnya konvergensi ini disebabkan oleh sifat tidak stabil dari pencocokan bipartit selama fase awal pelatihan. Fluktuasi kecil pada representasi fitur model dapat mengubah hasil pencocokan secara radikal, sehingga memaksa kueri objek yang sama mempelajari representasi spasial yang sangat berbeda pada epoch yang berbeda.

Beberapa upaya telah dilakukan untuk menstabilkan dan mempercepat pelatihan DETR. [023 - Deformable DETR](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md) membatasi area pencarian fitur spasial menggunakan atensi lokal yang dapat dideformasi. DAB-DETR merumuskan kueri objek sebagai koordinat kotak acuan eksplisit empat dimensi guna memberikan prior spasial yang stabil bagi mekanisme atensi. [159 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md) memperkenalkan tugas pelatihan de-noising pembantu (*auxiliary denoising task*) dengan menambahkan derau (*noise*) ke kotak *ground-truth* dan melatih dekoder untuk merekonstruksi kotak asli tanpa melewati proses pencocokan bipartit. Meskipun mempercepat konvergensi, DN-DETR hanya memanfaatkan de-noising positif (merekonstruksi kotak berderau kecil). Model ini rentan menghasilkan prediksi ganda karena tidak dilatih untuk menolak kandidat kotak yang berada dekat di sekitar objek *ground-truth*. Selain itu, inisialisasi kueri pada DN-DETR masih menggunakan pendekatan statis yang tidak adaptif terhadap isi citra, serta mekanisme perbaikan kotak spasial (*box refinement*) antar-lapisan dekoder masih kurang optimal karena memotong gradien pembaruan secara penuh demi menjaga stabilitas pelatihan (skema *look-forward-once*).

## Ide Utama

Gagasan utama DINO adalah merancang kerangka pelatihan kontrastif yang efisien dan menyatukan representasi spasial kueri dengan mekanisme pembaruan gradien terpadu di dalam dekoder. Ide ini diwujudkan melalui tiga komponen teknis utama:
1. **Contrastive Denoising Training (CDN):** Untuk menstabilkan pencocokan bipartit dan meminimalkan duplikasi deteksi, DINO menyertakan pasangan kueri berderau positif dan negatif secara bersamaan dalam pelatihan. Kueri positif ditambahkan derau dengan skala kecil agar model belajar merekonstruksi koordinat asli, sedangkan kueri negatif ditambahkan derau dengan skala yang lebih besar untuk memaksa model memprediksi kelas latar belakang (*no object*). Hal ini membentuk batas keputusan spasial yang lebih ketat di sekitar objek target.
2. **Mixed Query Selection:** DINO menginisialisasi bagian spasial dari kueri dekoder (kotak acuan) secara dinamis menggunakan fitur-fitur yang paling menonjol dari luaran enkoder. Sementara itu, bagian konten dari kueri dipertahankan sebagai penyematan (*embedding*) statis yang dapat dipelajari secara independen. Hibridisasi ini memberikan prior spasial yang adaptif terhadap citra masukan tanpa membatasi fleksibilitas representasi fitur objek yang dipelajari dekoder.
3. **Look-Forward-Twice (LFT):** DINO mengoptimalkan aliran informasi spasial dengan membiarkan gradien mengalir di antara lapisan dekoder yang berurutan selama perbaikan kotak iteratif. Alih-alih memutus aliran gradien secara total seperti pada model pendahulunya, DINO memanfaatkan estimasi offset dari lapisan berikutnya untuk menyupervisi pembaruan parameter pada lapisan saat ini secara retrospektif, sehingga meningkatkan konsistensi spasial model.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur dan Pemrosesan Enkoder

Citra masukan diproses oleh jaringan tulang punggung untuk menghasilkan peta fitur (*feature map*) multi-skala. Fitur-fitur ini menangkap representasi visual pada tingkat resolusi spasial yang berbeda. Peta fitur multi-skala kemudian dimasukkan ke dalam *Transformer Encoder* yang dilengkapi dengan mekanisme atensi terdeformasi multi-skala (*multi-scale deformable attention*). Mekanisme ini membatasi pencarian atensi hanya pada beberapa titik sampel di sekitar titik acuan tertentu, bukan melakukan komputasi global pada seluruh piksel citra. Modul ini menghasilkan peta fitur yang ter-refine dengan representasi spasial yang kaya dan komputasi yang efisien.

Skema alur data dan interaksi antar-komponen utama pada DINO digambarkan sebagai berikut:

```
[ Citra Input ]
       │
       ▼
┌──────────────┐
│   Backbone   │ (misalnya ResNet-50 / Swin Transformer)
└──────┬───────┘
       │ Fitur Multi-skala
       ▼
┌──────────────┐
│  Transformer │
│   Encoder    │ (Multi-scale Deformable Self-Attention)
└──────┬───────┘
       ├─────────────────────────┐ Fitur Refined
       ▼                         ▼
┌──────────────┐        ┌──────────────────┐
│ Top-K Select │        │ Mixed Query Sel. │ ──► Inisialisasi Positional Queries
└──────┬───────┘        └────────┬─────────┘     (Anchor Bounding Boxes)
       │                         │
       │                         │ + Learnable Content Queries
       ▼                         ▼
┌──────────────────────────────────────────┐
│           Transformer Decoder            │ ◄── [ Contrastive Denoising Queries ]
│ (Iterative Box Refinement - LFT Scheme)  │     - Positif (Derau Kecil ─► GT)
└──────────────────┬───────────────────────┘     - Negatif (Derau Besar ─► Background)
                   │
                   ▼
       ┌────────────────────────┐
       │     Prediction Heads   │ ──► Prediksi Kelas & Bounding Box
       └────────────────────────┘
```

### Mixed Query Selection

Di dalam dekoder, kueri objek terdiri dari dua bagian utama: kueri posisi (*positional queries*) yang mewakili koordinat kotak acuan, dan kueri konten (*content queries*) yang mewakili fitur semantik objek. DINO menggunakan metode seleksi kueri campuran untuk menginisialisasi kedua komponen ini:
1. Peta fitur luaran enkoder dievaluasi untuk memilih $K$ lokasi paling representatif berdasarkan skor probabilitas keberadaan objek (*objectness score*).
2. Koordinat spasial dari $K$ lokasi terbaik ini secara langsung digunakan untuk menetapkan kotak acuan awal ($x_i, y_i, w_i, h_i$) untuk kueri posisi dekoder.
3. Kueri konten tidak diinisialisasi dari fitur enkoder untuk menghindari bias awal, melainkan tetap menggunakan parameter penyematan statis yang dapat dipelajari (*learnable embedding*). Hal ini memastikan dekoder memiliki kebebasan untuk mempelajari detail semantik objek tanpa terikat langsung pada representasi awal yang dihasilkan enkoder.

### Contrastive Denoising Training (CDN)

Selama pelatihan, DINO mempercepat konvergensi dengan menambahkan cabang de-noising kontrastif pembantu yang tidak digunakan saat inferensi. Untuk setiap objek *ground-truth* berupa kelas $c$ dan koordinat kotak $b = (x, y, w, h)$, model membuat dua jenis kueri berderau dalam beberapa kelompok:
1. **Kelompok Denoising Positif:** Kotak *ground-truth* ditambahkan derau spasial bermagnitudo kecil yang dikontrol oleh parameter batas $\lambda_1$. Sebagai contoh, koordinat pusat kotak digeser sebesar $\Delta x$ dan $\Delta y$, serta ukuran kotak diubah sebesar $\Delta w$ dan $\Delta h$, dengan syarat $\max(|\Delta x|, |\Delta y|, |\Delta w|, |\Delta h|) < \lambda_1$. Tugas pelatihan untuk kelompok ini adalah memprediksi kembali kelas asli $c$ dan meregresi koordinat kotak asli $b$.
2. **Kelompok Denoising Negatif:** Kotak *ground-truth* ditambahkan derau spasial bermagnitudo lebih besar yang dikontrol oleh rentang antara $\lambda_1$ dan $\lambda_2$ (di mana $\lambda_1 < \lambda_2$). Kueri negatif sengaja ditempatkan di sekitar objek tetapi berada di luar batas margin positif. Tugas pelatihan untuk kelompok ini adalah memprediksi kelas latar belakang (*no object*). Hal ini mencegah model menghasilkan prediksi ganda pada posisi yang sedikit meleset dari objek asli.

Grup-grup kueri ini dipisahkan menggunakan masker atensi (*attention mask*) khusus. Hal ini memastikan kueri de-noising tidak dapat melihat kueri deteksi utama dan mencegah kebocoran informasi (*information leakage*) antar-kelompok, sehingga menjaga validitas evaluasi ujung-ke-ujung.

### Skema Pembaruan Look-Forward-Twice (LFT)

Dekoder pada DINO terdiri dari beberapa lapisan (biasanya 6 lapisan) yang memperbarui koordinat kotak secara iteratif. Pada lapisan ke-$i$, model menerima koordinat kotak $b_{i-1}$ dari lapisan sebelumnya dan memprediksi offset $\Delta b_i$ untuk menghasilkan koordinat kotak baru yang ter-refine.
Dalam skema *look-forward-once* pada model terdahulu, koordinat kotak diperbarui melalui fungsi pembaruan tanpa membiarkan aliran gradien mengalir kembali dari lapisan berikutnya ke lapisan sebelumnya (melalui fungsi pelepasan gradien atau *detach* pada $b_{i-1}$):
$$b_i = \text{Update}(\text{Detach}(b_{i-1}), \Delta b_i)$$
Meskipun metode ini menjaga stabilitas latihan, ia menghambat optimalisasi representasi spasial di lapisan-lapisan dangkal karena tidak mendapatkan umpan balik gradien dari lapisan yang lebih dalam.
DINO mengatasi masalah ini dengan skema *Look-Forward-Twice*. Proses pembaruan koordinat dilakukan melalui dua langkah aliran informasi:
1. Lapisan $i$ memprediksi koordinat sementara $b'_i = \text{Update}(b_{i-1}, \Delta b_i)$ dengan membiarkan gradien mengalir balik secara bebas ke $b_{i-1}$. Hal ini memungkinkan optimasi parameter pada lapisan $i$ dipengaruhi langsung oleh loss dari lapisan $i+1$.
2. Sebelum koordinat tersebut dikirimkan sebagai masukan spasial ke lapisan dekoder berikutnya ($i+1$), aliran gradien dilepaskan untuk meminimalkan akumulasi gradien yang berlebihan pada rantai dekoder yang panjang:
$$b_i = \text{Detach}(b'_i)$$
Dengan skema ini, parameter pada setiap lapisan dekoder disupervisi secara ganda oleh loss pada lapisan itu sendiri dan loss pada lapisan sesudahnya (sehingga disebut *look-forward-twice*), yang secara signifikan meningkatkan stabilitas regresi koordinat spasial.

## Eksperimen dan Hasil

Performa DINO dievaluasi secara komprehensif pada dataset deteksi objek MS COCO `val2017` and `test-dev`. Eksperimen dilakukan dengan membandingkan DINO terhadap beberapa detektor berbasis *transformer* pendahulunya, menggunakan tulang punggung ResNet-50 yang umum dipakai sebagai standar industri.

Berikut adalah tabel perbandingan performa pada dataset MS COCO `val2017` dengan menggunakan tulang punggung ResNet-50:

| Nama Model | Jumlah Epoch | Akurasi COCO AP (%) |
| :--- | :---: | :---: |
| DETR Asli | 500 | 42,0 |
| [160 - Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md) | 50 | 40,9 |
| DAB-DETR | 50 | 45,7 |
| [159 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md) | 12 | 46,0 |
| [159 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md) | 50 | 49,5 |
| **DINO** | **12** | **49,4** |
| **DINO** | **24** | **51,3** |
| **DINO** | **36** | **51,7** |

Hasil eksperimen pada tabel di atas menunjukkan keunggulan DINO yang signifikan:
- **Efisiensi Konvergensi:** Hanya dalam 12 epoch pelatihan, DINO mencapai akurasi sebesar **49,4% AP**. Hasil ini hampir menyamai performa terbaik DN-DETR yang dilatih selama 50 epoch (49,5% AP) dan melampaui DN-DETR pada jadwal pelatihan yang sama (46,0% AP) dengan selisih absolut sebesar 3,4%.
- **Akurasi Puncak:** Pada jadwal pelatihan 36 epoch, DINO mencatatkan akurasi sebesar **51,7% AP**, yang menetapkan rekor performa baru untuk detektor berbasis ResNet-50 tanpa prapelatihan tambahan.
- **Skalabilitas Model:** Ketika menggunakan tulang punggung Swin Transformer Large yang diprapelatih pada dataset Objects365, DINO mencapai akurasi puncak sebesar **63,2% AP** pada set `val2017` dan **63,3% AP** pada set `test-dev`. Ini menunjukkan kemampuan generalisasi dan skalabilitas DINO yang unggul ketika disandingkan dengan model representasi visual berkapasitas besar.

## Kelebihan dan Keterbatasan

### Kelebihan

1. **Konvergensi Pelatihan yang Sangat Cepat:** Skema pelatihan de-noising kontrastif secara drastis mengurangi waktu pelatihan yang dibutuhkan untuk mencapai konvergensi stabil. Reduksi waktu komputasi ini sangat berharga dari sudut pandang rekayasa praktis karena menghemat konsumsi energi dan sumber daya GPU.
2. **Akurasi Deteksi Unggul:** Dengan menggabungkan pemosisian spasial yang adaptif lewat seleksi kueri campuran (*Mixed Query Selection*) dan umpan balik gradien ganda lewat *Look-Forward-Twice*, DINO mampu memprediksi lokasi objek dengan presisi spasial yang lebih tinggi dibandingkan detektor ujung-ke-ujung lainnya.
3. **Bebas NMS:** Model ini tidak memerlukan pascapemrosesan berupa NMS untuk menyaring keluaran duplikat. Hal ini mempermudah proses integrasi dan penggelaran (*deployment*) model pada sistem real-time karena menyederhanakan alur komputasi.
4. **Generalisasi dan Skalabilitas Luar Biasa:** Performa DINO terus meningkat secara linier seiring dengan peningkatan kapasitas tulang punggung visual (seperti Swin Transformer), menjadikannya model fondasi yang sangat tangguh untuk berbagai tugas persepsi visual.

### Keterbatasan

1. **Beban Memori GPU yang Tinggi Selama Pelatihan:** Dari sisi rekayasa, penambahan grup kueri kontrastif positif dan negatif di dalam dekoder meningkatkan dimensi matriks atensi secara kuadratik. Hal ini menyebabkan lonjakan konsumsi memori GPU selama proses pelatihan, terutama saat menggunakan ukuran *batch* yang besar atau mendeteksi citra dengan kepadatan objek tinggi.
2. **Kompleksitas Implementasi Arsitektur:** Secara konseptual, alur data DINO jauh lebih rumit dibandingkan dengan detektor satu-tahap konvensional seperti YOLO. Logika atensi bertopeng pada CDN dan perhitungan gradien bertingkat pada skema LFT memerlukan implementasi kode yang presisi dan sulit didebug apabila terjadi inkonsistensi numerik.
3. **Kendala Akselerasi pada Perangkat Tepi:** Meskipun DINO bebas dari operasi NMS yang sulit diparalelkan, operasi atensi terdeformasi multi-skala di dalamnya masih kurang bersahabat dengan pustaka akselerasi bawaan pada beberapa perangkat komputasi tepi (*edge device*) kelas rendah. Hal ini membuat kecepatan inferensi riil pada perangkat tepi sering kali tidak secepat detektor satu-tahap berbasis CNN murni.

## Kaitan dengan Bab Lain

DINO menempati posisi evolusioner yang penting dalam klaster Fondasi RGB. Model ini secara langsung mewarisi dan menyempurnakan prinsip dekoder berbasis de-noising dari [159 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md), serta konsep pemodelan kueri objek sebagai kotak acuan spasial dinamis dari DAB-DETR. DINO juga memiliki kaitan konseptual dengan upaya pembatasan area pencarian spasial dekoder pada [160 - Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md) dan [161 - Sparse R-CNN](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md). Di tingkat representasi tulang punggung, DINO dipengaruhi oleh kemajuan ekstraksi fitur pada [024 - Vision Transformer (ViT)](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md) and [025 - Swin Transformer](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md).

Di sisi lain, arsitektur DINO menjadi batu loncatan utama bagi pengembangan detektor *real-time* berbasis transformer generasi berikutnya, seperti [155 - RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md). RT-DETR mengadopsi struktur dekoder berbasis kueri spasial dan skema latihan ujung-ke-ujung dari DINO, tetapi mengganti enkoder transformer DINO yang berat dengan arsitektur hibrida berbasis CNN (yaitu modul AIFI dan CCFM) untuk mereduksi beban komputasi secara radikal sehingga mampu mengalahkan efisiensi keluarga YOLO. Selain itu, DINO juga berfungsi sebagai standar pembanding (*baseline*) performa deteksi tingkat tinggi saat menggunakan tulang punggung visual canggih seperti [162 - ConvNeXt](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md) and [163 - Swin Transformer V2](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md), melandasi detektor berbasis pemahaman bahasa-gambar (*open-vocabulary*) seperti [156 - YOLO-World](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md), menyokong deteksi multi-skala komparatif pada [164 - Pyramid Vision Transformer](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md), melandasi strategi supervisi paralel pada [165 - Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md), serta arsitektur piramida informasi seperti [157 - Gold-YOLO](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kunci BibTeX: `zhang2023dino`

Kutipan akademis yang dapat digunakan:
> Model DINO (DETR with Improved DeNoising Anchor Boxes) memperkenalkan tiga inovasi utama berupa Contrastive Denoising Training (CDN), Mixed Query Selection, dan skema pembaruan kotak Look-Forward-Twice (LFT). Melalui teknik ini, DINO mampu meminimalkan ketidakstabilan pencocokan bipartit pada dekoder transformer dan mempercepat pelatihan secara drastis, dengan pencapaian akurasi sebesar 49,4% AP hanya dalam 12 epoch pada dataset COCO menggunakan tulang punggung ResNet-50.

Catatan verifikasi:
- Angka akurasi 49,4% AP pada 12 epoch, 51,3% AP pada 24 epoch, dan 51,7% AP pada 36 epoch dengan tulang punggung ResNet-50 telah diverifikasi dengan tabel hasil utama pada naskah asli DINO.
- Hasil SOTA sebesar 63,2% AP pada COCO `val2017` dan 63,3% AP pada COCO `test-dev` menggunakan model berskala besar dengan tulang punggung Swin-L yang diprapelatih pada Objects365 telah dicocokkan dengan laporan resmi penulis di Bagian 4.3 naskah asli.
