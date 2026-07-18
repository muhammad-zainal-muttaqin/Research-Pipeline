# 133 - EFC-YOLO: An Efficient Surface-Defect-Detection Algorithm for Steel Strips

## Metadata Ringkas
| Kunci BibTeX | `yang2023efcyolo` |
| Judul asli | EFC-YOLO: An Efficient Surface-Defect-Detection Algorithm for Steel Strips |
| Penulis | Yang, Yize; Li, Fengyi; Wang, Bao |
| Tahun | 2023 |
| Venue | Sensors |
| Tema | Industri |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=EFC-YOLO%3A%20An%20Efficient%20Surface-Defect-Detection%20Algorithm%20for%20Steel%20Strips
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=EFC-YOLO%3A%20An%20Efficient%20Surface-Defect-Detection%20Algorithm%20for%20Steel%20Strips&sort=relevance
- **DOI (MDPI):** https://doi.org/10.3390/s23177619

## Gambaran Umum
Makalah ini memperkenalkan EFC-YOLO (*Efficient Fusion Coordination YOLO*), sebuah model deteksi objek satu tahap yang dirancang khusus untuk mendeteksi cacat permukaan pada gulungan baja strip (*steel strips*) secara efisien dan *real-time*. Keberhasilan deteksi cacat pada industri metalurgi sangat bergantung pada kemampuan model mendeteksi cacat berukuran mikro sekaligus mempertahankan laju komputasi yang tinggi agar dapat berjalan pada perangkat keras tepi (*edge computing*) dengan spesifikasi terbatas. EFC-YOLO mengatasi tantangan ini dengan memodifikasi arsitektur YOLOv7 melalui penyederhanaan operator konvolusi dan restrukturisasi jaringan penggabungan fitur.

Hasil eksperimen utama menunjukkan bahwa EFC-YOLO berhasil mencapai akurasi deteksi (*mean Average Precision* atau mAP) sebesar 85,9% pada dataset standar industri NEU-DET. Pencapaian akurasi ini dibarengi dengan penurunan beban komputasi (*Giga Floating-Point Operations* atau GFLOPs) yang sangat signifikan, yakni sebesar 60% dibandingkan dengan model pembanding YOLOv7 standar. Keberhasilan ini membuat EFC-YOLO sangat potensial untuk diaplikasikan secara langsung pada lini produksi industri manufaktur baja tanpa memerlukan infrastruktur komputasi berbiaya tinggi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Proses manufaktur baja strip panas dan dingin sering kali menghasilkan berbagai jenis cacat permukaan akibat fluktuasi mekanis, kontaminasi zat asing, atau ketidakstabilan suhu gilingan. Cacat-cacat ini meliputi retak rambut (*crazing*), inklusi zat non-logam (*inclusion*), tambalan permukaan (*patches*), permukaan bopeng (*pitted surface*), kerak akibat proses giling panas (*rolled-in scale*), dan goresan mekanis (*scratches*). Jika cacat-cacat ini tidak diidentifikasi sejak dini, kualitas struktural baja dapat menurun secara drastis, yang pada akhirnya memicu kerugian finansial yang signifikan bagi produsen dan pengguna akhir.

Metode inspeksi visual tradisional yang mengandalkan mata manusia memiliki keterbatasan berupa subjektivitas tinggi, inkonsistensi penilaian, kerentanan terhadap kelelahan operator, serta kecepatan inspeksi yang sangat lambat. Keterbatasan ini membuat inspeksi manual tidak kompatibel dengan lini produksi modern yang beroperasi secara kontinu pada kecepatan tinggi. Penerapan sistem visi komputer (*computer vision*) berbasis pembelajaran mendalam (*deep learning*) menawarkan solusi otomatis yang menjanjikan. Namun, arsitektur pendeteksi objek modern seperti YOLOv7 standar, meskipun memiliki akurasi tinggi, memiliki parameter yang terlalu besar dan kebutuhan komputasi yang masif. Hal ini menyebabkan latensi tinggi saat model dideploy pada perangkat tertanam (*embedded system*) di pabrik.

Di sisi lain, upaya memangkas arsitektur model secara naif demi mengejar efisiensi sering kali mengorbankan akurasi deteksi, terutama pada jenis cacat berukuran kecil atau yang memiliki kontras rendah dengan latar belakang seperti *crazing* dan *pitted surface*. Dengan demikian, bidang inspeksi industri membutuhkan sebuah model yang mampu menyeimbangkan secara ketat antara akurasi deteksi cacat multi-skala dan kecepatan pemrosesan yang efisien.

## Ide Utama
Ide utama di balik EFC-YOLO adalah mendesain ulang arsitektur pemrosesan fitur YOLOv7 untuk mereduksi redundansi spasial dan menyederhanakan mekanisme interaksi spasial tanpa mengorbankan informasi penting terkait posisi cacat. Ide utama ini diwujudkan melalui tiga pilar modifikasi teknis:
1. **Modul Fusion-Faster dengan Konvolusi Parsial (*Partial Convolution* / PConv):** Menggantikan modul konvolusi standar pada bagian awal *backbone* untuk memproses hanya sebagian saluran (*channels*) fitur aktif, sehingga meminimalkan beban komputasi dan akses memori yang berlebihan.
2. **Atensi Koordinat dengan Jalur Pintas (*Shortcut Coordinate Attention* / SCA):** Mengintegrasikan mekanisme atensi spasial yang menyandikan koordinat horizontal dan vertikal secara terpisah, ditambah dengan jalur pintas langsung (*shortcut*) untuk menjaga stabilitas aliran gradien dan mempertahankan representasi spasial objek cacat kecil.
3. **Leher (Neck) Jaringan Berbasis de-weighted BiFPN:** Menggantikan struktur leher PANet (*Path Aggregation Network*) bawaan YOLOv7 dengan varian BiFPN (*Bi-directional Feature Pyramid Network*) yang telah disederhanakan (*de-weighted*) guna mempercepat peleburan informasi multi-skala dengan memotong simpul komputasi yang redundan.

## Cara Kerja Langkah demi Langkah

### Modul Fusion-Faster dan Operasi Partial Convolution (PConv)
Untuk mengurangi redundansi spasial di dalam lapisan fitur yang tebal, EFC-YOLO menerapkan konsep konvolusi parsial (*Partial Convolution* atau PConv). Konvolusi konvensional 3x3 memproses seluruh $C$ saluran input, menghasilkan operasi komputasi yang tinggi. Sebaliknya, PConv mengeksploitasi redundansi ini dengan hanya menerapkan operasi penapisan pada sebagian kecil saluran ($c_p < C$, di mana rasio umumnya ditetapkan sebesar $1/4$ atau $25\%$), sedangkan sisa saluran lainnya ($C - c_p$) dibiarkan tidak berubah (*identity mapping*).

Mekanisme operasi PConv dan integrasinya ke dalam modul Fusion-Faster digambarkan pada skema di bawah ini:

```
                  Partial Convolution (PConv)
                  
                  Input Tensor: [C x H x W]
                           │
                           ▼
                 Split Channels (1:3)
                 ┌─────────┴─────────┐
                 │ c_p               │ C - c_p
                 ▼                   ▼
           ┌───────────┐       ┌───────────┐
           │ Conv 3x3  │       │ Identity  │ (Bypass)
           └─────┬─────┘       └─────┬─────┘
                 ▼                   ▼
           ┌─────────────────────────┐
           │ Concatenate & Shuffle   │
           └─────────────┬───────────┘
                         ▼
                 Output: [C x H x W]
```

Melalui modul Fusion-Faster, keluaran dari PConv dilewatkan ke operasi konvolusi 1×1 untuk memastikan terjadinya pencampuran informasi yang optimal di seluruh dimensi saluran. Sebagai contoh numerik konkret: jika sebuah tensor fitur memiliki dimensi $C = 256$ dengan resolusi spasial $H = 80$ and $W = 80$, konvolusi standar 3x3 dengan $C_{out} = 256$ akan memerlukan FLOPs sebesar:
$$\text{FLOPs}_{\text{std}} = 256 \times 256 \times 3 \times 3 \times 80 \times 80 \approx 3,77 \times 10^9 \text{ operasi}$$
Dengan menggunakan PConv dengan rasio $1/4$ ($c_p = 64$), komputasi hanya berjalan pada saluran terpilih, sehingga FLOPs terpangkas menjadi:
$$\text{FLOPs}_{\text{PConv}} = 64 \times 64 \times 3 \times 3 \times 80 \times 80 \approx 2,36 \times 10^8 \text{ operasi}$$
Hal ini menghasilkan efisiensi komputasi spasial hingga 16 kali lebih hemat pada lapisan konvolusi tersebut, tanpa kehilangan kemampuan representasi fitur secara dramatis.

### Mekanisme Shortcut Coordinate Attention (SCA)
Untuk mengimbangi pengurangan parameter di bagian *backbone*, EFC-YOLO memasang modul *Shortcut Coordinate Attention* (SCA). Modul ini bekerja dengan memisahkan pooling spasial global menjadi pooling horizontal ($X$) dan vertikal ($Y$). Langkah ini memungkinkan model menangkap ketergantungan jarak jauh sepanjang satu arah koordinat serta mempertahankan informasi posisi objek cacat secara akurat pada arah koordinat lainnya.

SCA menambahkan jalur pintas residual (*shortcut*) di atas mekanisme *Coordinate Attention* (CA) standar. Persamaan matematika sederhana untuk menghitung atensi koordinat ini melibatkan penggabungan deskriptor fitur spasial horizontal $z^h$ dan vertikal $z^w$ yang diolah melalui konvolusi 1x1 bersama ($\mathbf{f}$), fungsi aktivasi non-linier, kemudian dipecah kembali menjadi komponen $\mathbf{f}^h$ dan $\mathbf{f}^w$. Komponen-komponen tersebut dilewatkan ke fungsi sigmoid untuk menghasilkan bobot atensi horizontal $g^h$ dan vertikal $g^w$. Peta fitur hasil akhirnya dihitung sebagai berikut:
$$\mathbf{Y}_{c}(i,j) = \mathbf{X}_{c}(i,j) \times g_{c}^{h}(i) \times g_{c}^{w}(j) + \mathbf{X}_{c}(i,j)$$
Dengan adanya penambahan suku $+\mathbf{X}_{c}(i,j)$ sebagai jalur pintas residual, informasi spasial awal dari cacat kecil yang sangat rentan tereliminasi selama proses ekstraksi bertingkat dapat tetap dipertahankan secara utuh menuju lapisan pendeteksian berikutnya.

### Struktur Leher (Neck) de-weighted BiFPN
Pada YOLOv7 standar, peleburan fitur lintas skala dilakukan oleh PANet yang memiliki struktur aliran dua arah (*top-down* dan *bottom-up*). Struktur ini menuntut biaya komputasi yang tinggi karena memproses setiap simpul penggabungan dengan bobot konvolusi penuh. EFC-YOLO menyederhanakan komponen ini dengan menerapkan desain *de-weighted* BiFPN yang terinspirasi dari arsitektur EfficientDet tetapi dioptimalkan secara agresif untuk deteksi cacat industri.

Penyederhanaan ini diwujudkan dengan memotong simpul-simpul antara (*intermediate nodes*) yang hanya memiliki satu jalur masukan, karena secara empiris simpul tersebut memberikan kontribusi minimal pada penggabungan fitur tetapi memakan waktu inferensi yang signifikan. Selain itu, koneksi lateral langsung ditambahkan dari simpul masukan awal ke simpul keluaran pada skala yang sama. Konsep pembobotan dinamis pada BiFPN asli diganti dengan peleburan berbasis konkatenasi (*concatenation*) statis yang langsung diikuti konvolusi titik demi titik (*pointwise convolution* 1x1). Langkah ini memangkas beban komputasi leher jaringan secara drastis namun tetap menjamin aliran informasi multi-skala yang kaya untuk mendeteksi cacat besar seperti *patches* sekaligus cacat tipis seperti *scratches*.

Secara makro, integrasi seluruh komponen ini dalam pipeline EFC-YOLO dapat divisualisasikan sebagai berikut:

```
                          Pipeline EFC-YOLO
                          
   Input Image (640x640)
           │
           ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Backbone: YOLOv7 + Fusion-Faster Modules (PConv)        ├─► P3 (SCA)
   └─────────────────────────────────────────────────────────┘     │
                                                                   ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Neck: De-weighted BiFPN Multi-scale Fusion              ├─► P4 (SCA)
   └─────────────────────────────────────────────────────────┘     │
                                                                   ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Head: Predicts Bounding Boxes & Confidence Scores       ├─► P5 (SCA)
   └─────────────────────────────────────────────────────────┘
```

## Eksperimen dan Hasil
EFC-YOLO dievaluasi secara komprehensif menggunakan dataset cacat permukaan baja standar industri, yaitu **NEU-DET** yang dirilis oleh Northeastern University. Dataset ini memuat 1.800 citra abu-abu (*grayscale*) dengan resolusi masing-masing 200×200 piksel. Citra-citra tersebut terbagi secara merata ke dalam okeh kategori cacat permukaan baja lembaran, yaitu:
1. *Crazing* (Cr): Retak rambut halus yang menyebar membentuk pola jaring.
2. *Inclusion* (In): Inklusi zat non-logam yang menempel pada permukaan baja.
3. *Patches* (Pa): Tambalan atau plak material yang tertekan pada permukaan.
4. *Pitted surface* (Ps): Bopeng atau lubang-lubang kecil akibat korosi atau erosi mekanis.
5. *Rolled-in scale* (Rs): Kerak oksida besi yang tergilas masuk ke dalam pelat baja.
6. *Scratches* (Sc): Goresan linier akibat gesekan dengan peralatan pabrik.

### Hasil Kinerja Kuantitatif
Dalam pengujian performa deteksi, EFC-YOLO menunjukkan keunggulan yang signifikan dibandingkan arsitektur YOLOv7 asli dan model pendeteksi objek lainnya:

| Model | mAP (@0,5) (%) | GFLOPs | Parameter (M) |
|---|---|---|---|
| YOLOv7 (Baseline) | 83,7% | 105,2 | 37,2 |
| **EFC-YOLO (Usulan)** | **85,9%** | **39,2** | **30,4** |
| YOLOv5s | 76,5% | 16,5 | 7,2 |
| Faster R-CNN | 78,2% | 180,0 | 137,0 |

### Interpretasi Angka Hasil
Berdasarkan data eksperimen di atas, EFC-YOLO mencatatkan nilai mAP sebesar 85,9%, yang berarti terjadi peningkatan akurasi sebesar 2,2% secara absolut dibandingkan dengan baseline YOLOv7 (83,7%). Peningkatan akurasi ini sangat penting karena diraih di saat yang sama ketika kompleksitas komputasi model (GFLOPs) dipotong sebesar 62,7% dari 105,2 GFLOPs menjadi hanya 39,2 GFLOPs. Dari aspek ukuran model, parameter jaringan juga berhasil direduksi dari 37,2 M menjadi 30,4 M (berkurang sekitar 18,2%).

Jika dibandingkan dengan model yang lebih ringan seperti YOLOv5s, EFC-YOLO unggul sangat jauh dalam aspek akurasi (+9,4% mAP) meskipun memiliki jumlah GFLOPs yang lebih besar. Hal ini menunjukkan bahwa EFC-YOLO berhasil menemukan titik temu (*sweet spot*) yang optimal antara kecepatan inferensi yang ramah perangkat tepi (*real-time edge capability*) dan ketangguhan deteksi cacat mikro di lingkungan industri baja.

## Kelebihan dan Keterbatasan

### Kelebihan
- **Efisiensi Energi dan Komputasi Tinggi:** Pengurangan GFLOPs sebesar lebih dari 60% meminimalkan konsumsi daya dan penggunaan memori, sehingga model sangat cocok dijalankan pada GPU industri berdaya rendah (*low-power industrial GPU*) atau perangkat tertanam seperti NVIDIA Jetson.
- **Deteksi Cacat Kecil yang Tangguh:** Berkat integrasi modul *Shortcut Coordinate Attention* (SCA), model ini menunjukkan performa tinggi dalam melokalisasi cacat dengan fitur spasial halus seperti *crazing* dan *scratches* yang biasanya terabaikan oleh detektor standar.
- **Peleburan Fitur Multi-Skala yang Ringkas:** Desain *de-weighted* BiFPN memangkas latensi transmisi fitur antar-lapisan tanpa mengorbankan kualitas peleburan informasi semantik.

### Keterbatasan
- **Generalisasi pada Citra Multi-Saluran (RGB) Belum Teruji:** Secara konseptual, model ini dievaluasi secara mendalam pada citra abu-abu (*grayscale*) dari dataset NEU-DET. Kinerjanya pada citra berwarna (RGB) dengan gangguan variasi warna dan pencahayaan industri yang ekstrem masih memerlukan penyelidikan lebih lanjut.
- **Sensitivitas Konfigurasi Saluran Aktif ($c_p$):** Dari sisi rekayasa, efisiensi PConv sangat dipengaruhi oleh pemilihan rasio saluran aktif. Jika rasio disetel terlalu rendah (misalnya di bawah $12,5\%$), model dapat mengalami degradasi representasi fitur yang parah untuk cacat yang memiliki bentuk geometri kompleks seperti *inclusion* dan *patches*.

## Kaitan dengan Bab Lain
EFC-YOLO memiliki posisi yang erat dengan beberapa bab penelitian deteksi cacat di klaster Industri:
1. **Suksesor dan Perbandingan Metodologi:** Bab ini dapat dibaca berdampingan dengan [PCB-YOLO](./134%20-%202024%20-%20PCB-YOLO%20%28PCB%20Defects%29%20-%20Industri.md) yang dikembangkan pada tahun 2024. PCB-YOLO mengadopsi taktik serupa dengan mengintegrasikan *Coordinate Attention* dan penggabungan multi-skala untuk mendeteksi cacat pada papan sirkuit cetak (PCB). Perbedaannya, EFC-YOLO berfokus pada minimalisasi beban komputasi menggunakan konvolusi parsial (PConv) di tingkat *backbone*, sedangkan PCB-YOLO berfokus pada akurasi deteksi komponen elektronik mikro.
2. **Konteks Literatur Global:** Penelitian ini memperkuat survei metodologi yang dibahas dalam [Review Defect Detection (Bhatt dkk.)](./135%20-%202021%20-%20Review%20Defect%20Detection%20%28Bhatt%20dkk.%29%20-%20Industri.md). Tinjauan pustaka Bhatt dkk. menjelaskan pentingnya deteksi cacat permukaan secara *real-time* di dunia manufaktur pintar (*Smart Manufacturing*), di mana EFC-YOLO bertindak sebagai salah satu implementasi YOLO konkret yang menjawab tantangan efisiensi tersebut.
3. **Evolusi Arsitektur YOLO Industri:** Dibandingkan dengan [Safety Helmet Detection (Improved YOLOv5)](./136%20-%202021%20-%20Safety%20Helmet%20Detection%20%28Improved%20YOLOv5%29%20-%20Industri.md) yang mengoptimalkan YOLOv5 untuk pengawasan keselamatan kerja (*safety helmet*), EFC-YOLO menunjukkan lompatan paradigma dengan memodifikasi YOLOv7 menggunakan konsep konvolusi parsial demi menekan biaya komputasi tanpa mengorbankan akurasi.

## Poin untuk Sitasi
- **Kunci BibTeX:** `yang2023efcyolo`
- **Ringkasan untuk Tinjauan Pustaka:** EFC-YOLO merupakan varian YOLOv7 yang dioptimalkan untuk inspeksi cacat permukaan strip baja dengan menggunakan modul Fusion-Faster (berbasis Partial Convolution), mekanisme atensi *Shortcut Coordinate Attention* (SCA), dan struktur leher *de-weighted* BiFPN. Model ini mencapai mAP 85,9% pada dataset NEU-DET dengan memotong kebutuhan komputasi (GFLOPs) sebesar 60% dibandingkan model baseline YOLOv7.
- **Catatan Verifikasi:** Terdapat ketidaksesuaian nama penulis pada basis data sitasi `references.bib` (tercatat sebagai *Yang, Yize; Li, Fengyi; Wang, Bao*) dengan naskah publikasi asli MDPI Sensors 2023 (yang ditulis oleh *Yanshun Li, Shuobo Xu, Zimo Zhu, Peng Wang, Kefeng Li, Qiang He, dan Quanfeng Zheng*). Selalu lakukan verifikasi dan sinkronisasi berkas `.bib` sebelum melakukan sitasi formal.
