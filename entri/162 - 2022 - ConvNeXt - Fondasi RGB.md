# 162 - A ConvNet for the 2020s

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2022convnext` |
| Judul asli | A ConvNet for the 2020s |
| Penulis | Liu, Zhuang; Mao, Hanzi; Wu, Chao-Yuan; Feichtenhofer, Christoph; Darrell, Trevor; Xie, Saining |
| Tahun | 2022 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2201.03545
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20ConvNet%20for%20the%202020s
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20ConvNet%20for%20the%202020s&sort=relevance

## Gambaran Umum
ConvNeXt adalah arsitektur *convolutional neural network* (CNN) murni yang dirancang untuk membuktikan bahwa struktur konvolusi standar tetap kompetitif di era dominasi *Vision Transformer* (ViT). Makalah ini memodernisasi arsitektur klasik ResNet-50 secara bertahap dengan mengadopsi berbagai keputusan desain makro dan mikro yang digunakan dalam model ViT, khususnya Swin Transformer. Melalui perbaikan bertahap pada resep pelatihan, rasio komputasi tahapan, *patchify stem*, *depthwise convolution*, *inverted bottleneck*, peningkatan ukuran kernel, serta penyederhanaan fungsi aktivasi dan lapisan normalisasi, ConvNeXt berhasil menandingi atau bahkan melampaui akurasi serta efisiensi komputasi Swin Transformer pada tugas klasifikasi citra ImageNet, deteksi objek COCO, dan segmentasi semantik ADE20K.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum kemunculan ConvNeXt, literatur visi komputer didominasi oleh pergeseran dari arsitektur berbasis konvolusi seperti ResNet ke arsitektur berbasis perhatian global seperti ViT dan Swin Transformer. Swin Transformer menunjukkan kinerja unggul pada berbagai tugas hilir karena kemampuannya memodelkan ketergantungan jarak jauh dan fleksibilitas dalam menangani input multi-skala. Fenomena ini memicu asumsi bahwa CNN konvensional memiliki keterbatasan inheren dibandingkan dengan mekanisme perhatian (*attention mechanism*) dalam memproses representasi spasial citra yang kompleks. Namun, analisis mendalam menunjukkan bahwa keunggulan Transformer tidak hanya berasal dari mekanisme perhatian global, melainkan juga didukung oleh teknik pelatihan modern serta konfigurasi arsitektur makro-mikro yang lebih optimal. Masalah utama yang ingin dipecahkan oleh penelitian ini adalah menguji apakah CNN murni dapat mencapai tingkat kinerja yang setara dengan Transformer jika diberikan teknik pelatihan dan prinsip desain arsitektural modern yang serupa.

## Ide Utama
Gagasan inti dari ConvNeXt adalah merekonstruksi arsitektur CNN klasik (menggunakan ResNet-50 sebagai baseline) dengan meniru elemen-elemen kunci dari Swin Transformer tanpa memasukkan mekanisme perhatian spasial atau *self-attention* yang dinamis. Jaringan tetap mempertahankan sifat konvolusi murni yang memiliki bias induktif berupa lokalisasi spasial (*spatial locality*) dan ekuivariansi translasi (*translation equivariance*). Transformasi arsitektur ini dilakukan melalui eksplorasi empiris sistematis yang mengisolasi kontribusi setiap elemen desain. Hasil akhirnya adalah model konvolusi yang memiliki representasi fitur hierarkis mirip dengan Swin Transformer, tetapi dengan implementasi komputasi yang lebih sederhana dan kecepatan inferensi (*throughput*) yang lebih tinggi pada unit pemroses grafis (GPU) standar.

## Cara Kerja Langkah demi Langkah
Untuk memahami bagaimana ConvNeXt dibangun, proses transisi dari ResNet-50 ke ConvNeXt-T dibagi menjadi beberapa fase terukur yang mempertahankan kapasitas komputasi (*floating-point operations* atau FLOPs) agar tetap setara dengan Swin-T (~4,5G FLOPs):

### 1. Resep Pelatihan Modern (Training Recipe)
Langkah pertama tidak mengubah arsitektur fisik model, melainkan memperbarui protokol pelatihan agar setara dengan teknik pelatihan Vision Transformer (DeiT-style). Protokol ini mencakup perpanjangan masa pelatihan dari 90 *epoch* menjadi 300 *epoch*, penggunaan pengoptimal AdamW menggantikan SGD (*Stochastic Gradient Descent*), serta penerapan augmentasi data yang agresif seperti *Mixup*, *CutMix*, dan *RandAugment*. Selain itu, regulasi ditambahkan melalui *Stochastic Depth* (DropPath) dan *Label Smoothing*. Penerapan resep pelatihan baru ini meningkatkan akurasi *top-1* ResNet-50 pada ImageNet-1K secara signifikan dari 76,1% menjadi 78,8%.

### 2. Desain Makro (Macro Design)
Desain makro jaringan disesuaikan untuk meniru cara Swin Transformer membagi komputasi di setiap tahap:
- **Rasio Komputasi Tahapan (Stage Compute Ratio):** Rasio jumlah blok residual pada setiap tahap (*stage*) diubah dari konfigurasi ResNet-50 (3, 4, 6, 3) menjadi (3, 3, 9, 3) agar serupa dengan Swin-T (1:1:3:1). Modifikasi ini meningkatkan akurasi dari 78,8% menjadi 79,4%.
- **Patchify Stem:** ResNet menggunakan lapisan masuk (*stem*) berupa konvolusi 7x7 dengan langkah (*stride*) 2 diikuti oleh lapisan *max pooling* 3x3 dengan langkah 2 yang melakukan reduksi spasial sebesar 4 kali. Lapisan ini diganti dengan lapisan *patchify* seperti pada ViT, yaitu konvolusi 4x4 dengan langkah 4, yang langsung mereduksi resolusi spasial citra input sebesar 4 kali. Perubahan ini meningkatkan akurasi dari 79,4% menjadi 79,5%.

### 3. ResNeXt-ify (Grouped Convolution)
Struktur blok residual dimodifikasi dengan menggunakan *depthwise convolution*, di mana konvolusi dilakukan secara terpisah untuk setiap saluran (*channel*). Konvolusi ini sebanding dengan mekanisme *self-attention* di mana informasi spasial diproses per saluran sebelum diintegrasikan secara linear. Karena operasi *depthwise* mengurangi jumlah FLOPs, lebar saluran dasar jaringan ditingkatkan dari 64 menjadi 96 saluran guna menjaga komputasi keseluruhan tetap setara dengan Swin-T. Langkah ini menaikkan akurasi dari 79,5% menjadi 80,5%.

### 4. Inverted Bottleneck
Blok bottleneck ResNet klasik memproses fitur dengan urutan dimensi besar-kecil-besar (lebar saluran masukan diperkecil oleh konvolusi 1x1, diproses oleh konvolusi 3x3, lalu diperbesar kembali oleh konvolusi 1x1). ConvNeXt membalik urutan ini menjadi konfigurasi *inverted bottleneck* (kecil-besar-kecil), mirip dengan struktur blok MLP (*multilayer perceptron*) pada Transformer dan blok MobileNetV2. Saluran masukan diperbesar 4 kali lipat oleh konvolusi 1x1 sebelum diproses oleh lapisan konvolusi spasial. Akurasi naik dari 80,5% menjadi 80,6%.

### 5. Large Kernel Size (Ukuran Kernel Besar)
Untuk meniru area pandangan (*receptive field*) global dari perhatian Transformer, ukuran kernel pada lapisan konvolusi diperbesar:
- **Pergeseran Posisi Konvolusi Spasial:** Lapisan konvolusi *depthwise* dipindahkan ke bagian paling awal blok (sebelum konvolusi 1x1 ekspansi), mirip dengan posisi lapisan perhatian pada Transformer yang mendahului blok MLP. Langkah ini menurunkan akurasi menjadi 79,9%, namun merupakan prasyarat penting untuk optimalisasi kernel besar.
- **Kernel 7x7:** Ukuran kernel ditingkatkan dari 3x3 menjadi 7x7. Dengan posisi konvolusi spasial di depan blok yang memiliki saluran lebih sedikit (96 saluran dibandingkan 384 saluran setelah ekspansi), operasi kernel besar menjadi efisien tanpa lonjakan FLOPs yang signifikan. Peningkatan ukuran kernel menaikkan akurasi kembali ke 80,6%.

### 6. Desain Mikro (Micro Design)
Beberapa penyesuaian detail dilakukan pada tingkat fungsi aktivasi dan lapisan normalisasi:
- **Penggunaan GELU:** Fungsi aktivasi ReLU diganti dengan *Gaussian Error Linear Unit* (GELU) untuk menyelaraskan dengan ViT. Akurasi tetap stabil pada 80,6%.
- **Reduksi Lapisan Aktivasi:** Jika ResNet menaruh aktivasi setelah setiap konvolusi, ConvNeXt hanya menggunakan satu lapisan aktivasi GELU per blok, yang ditempatkan di antara dua konvolusi 1x1 (setelah ekspansi saluran). Reduksi ini meningkatkan akurasi dari 80,6% menjadi 81,3%.
- **Reduksi Lapisan Normalisasi:** Lapisan normalisasi dikurangi menjadi hanya satu lapisan per blok, ditempatkan sebelum konvolusi 1x1 ekspansi. Akurasi naik dari 81,3% menjadi 81,4%.
- **Layer Normalization (LayerNorm):** Lapisan *Batch Normalization* (BatchNorm) diganti sepenuhnya dengan LayerNorm. Ini menstabilkan pelatihan dan memudahkan transfer fitur ke model lain. Akurasi meningkat dari 81,4% menjadi 81,5%.
- **Pemisahan Lapisan Downsampling:** Lapisan penurun resolusi (*downsampling*) dipisahkan dari blok residual utama. ConvNeXt menggunakan lapisan konvolusi 2x2 dengan langkah 2 yang didahului oleh LayerNorm di antara tahapan komputasi. Modifikasi ini menghasilkan peningkatan akurasi dari 81,5% menjadi 82,0%.

Melalui optimasi halus tambahan, akurasi model ConvNeXt-T mencapai 82,1%.

Berikut adalah perbandingan arsitektur blok antara ResNet klasik dan ConvNeXt:

```
       [ ResNet Block ]                      [ ConvNeXt Block ]
       
            Input                                 Input
              │                                     │
              ├───┐ (shortcut)                      ├───┐ (shortcut)
              ▼   │                                 ▼   │
           Conv 1x1                               Depthwise
         (down-proj)                              Conv 7x7
              │                                     │
          BatchNorm                                 │
              │                                 LayerNorm
            ReLU                                    │
              │                                     ▼
           Conv 3x3                              Conv 1x1
              │                              (expansion, 4x)
          BatchNorm                                 │
              │                                   GELU
            ReLU                                    │
              │                                     ▼
           Conv 1x1                              Conv 1x1
          (up-proj)                            (reduction)
              │                                     │
          BatchNorm                                 │
              │   │                                 │   │
              ▼   │                                 ▼   │
              ┼◄──┘ (tambah)                        ┼◄──┘ (tambah)
              │                                     │
            ReLU                                 Output
              │
            Output
```

## Eksperimen dan Hasil
ConvNeXt dievaluasi pada berbagai tugas visual standar untuk membuktikan kemampuannya sebagai pengekstraksi fitur umum.

### Klasifikasi Citra pada ImageNet-1K
Dalam evaluasi klasifikasi menggunakan dataset ImageNet-1K (resolusi 224x224), varian-varian ConvNeXt menunjukkan performa yang unggul jika dibandingkan dengan varian Swin Transformer yang setara dalam hal jumlah parameter dan FLOPs:
- **ConvNeXt-T** meraih akurasi *top-1* sebesar 82,1% dengan komputasi 4,5G FLOPs dan 28 juta parameter, melampaui **Swin-T** yang meraih 81,3% pada komputasi yang sama.
- **ConvNeXt-S** meraih akurasi 83,1% (50 juta parameter, 8,7G FLOPs), setara dengan **Swin-S** yang meraih 83,2%.
- **ConvNeXt-B** meraih akurasi 83,8% (89 juta parameter, 15,4G FLOPs), mengungguli **Swin-B** yang meraih 83,5%.

### Deteksi Objek pada COCO
Sebagai *backbone* pada detektor objek Cascade Mask R-CNN, ConvNeXt dievaluasi menggunakan metrik *box Average Precision* (AP^box) dan *mask Average Precision* (AP^mask). Menggunakan ConvNeXt-T sebagai pengganti Swin-T meningkatkan AP^box dari 50,4 menjadi 51,3 (+0,9 AP). Pada skala yang lebih besar, Cascade Mask R-CNN dengan *backbone* ConvNeXt-B menghasilkan AP^box sebesar 52,7, mengungguli Swin-B yang menghasilkan 51,9.

### Segmentasi Semantik pada ADE20K
Pada tugas segmentasi semantik menggunakan kerangka kerja UperNet pada dataset ADE20K, ConvNeXt-T mencapai nilai *mean Intersection over Union* (mIoU) sebesar 46,0%, melampaui Swin-T yang mencatat 44,5%. ConvNeXt-B mencapai 49,1% mIoU, berada di atas Swin-B dengan 48,1% mIoU. Hasil eksperimen ini mengonfirmasi bahwa representasi spasial yang dihasilkan oleh operasi konvolusi dengan kernel besar dan ter-modernisasi sangat efektif untuk tugas-tugas prediksi piksel padat (*dense prediction*).

## Kelebihan dan Keterbatasan
Secara konseptual, kelebihan utama ConvNeXt adalah kesederhanaan arsitekturnya. Dengan mempertahankan struktur konvolusi murni, model ini tidak memerlukan mekanisme perhitungan perhatian kuadratik yang mahal pada citra beresolusi tinggi, sehingga memiliki memori *overhead* yang lebih rendah saat pelatihan. Dari sisi rekayasa hardware, konvolusi standar telah dioptimalkan secara mendalam pada level *driver* CUDA dan perpustakaan cuDNN. Hal ini membuat ConvNeXt memiliki kecepatan pemrosesan (*throughput*) yang lebih tinggi pada GPU dibandingkan dengan Swin Transformer yang memiliki operasi penataan ulang memori (*memory reshaping*) yang kompleks akibat *shifted windows*.

Namun, secara konseptual, ConvNeXt memiliki keterbatasan berupa tidak adanya mekanisme perbandingan global dinamis secara eksplisit pada lapisan-lapisan awal. Meskipun kernel 7x7 memperlebar *receptive field*, area tersebut tetap bersifat lokal dan tidak dapat menangani ketergantungan jarak jauh (*long-range dependencies*) sefleksibel mekanisme *self-attention* tanpa adanya penumpukan lapisan yang cukup dalam. Selain itu, model ini membutuhkan durasi pelatihan yang sangat panjang (minimal 300 *epoch*) dan augmentasi data yang sangat intensif agar dapat mencapai konvergensi optimal; jika dilatih dengan protokol klasifikasi konvensional ResNet yang pendek (90 *epoch*), keunggulannya atas CNN klasik tidak akan terlihat secara maksimal.

## Kaitan dengan Bab Lain
ConvNeXt menempati posisi silsilah penting dalam klaster **Fondasi RGB**. Jaringan ini mewarisi ide ekstraksi fitur hierarkis multi-skala dari arsitektur konvolusi klasik, namun secara radikal merombak konfigurasinya dengan mengadopsi struktur non-konvolusi dari era Transformer.

Secara genealogis, ConvNeXt bertindak sebagai jembatan konseptual antara model-model berbasis perhatian global seperti [Pyramid Vision Transformer](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md) (PVT) serta [Swin Transformer V2](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md) dengan model deteksi objek modern yang membutuhkan *backbone* pengekstraksi fitur berkinerja tinggi. Desain *inverted bottleneck* dan penyederhanaan normalisasi dalam ConvNeXt terbukti menjadi fondasi penting bagi arsitektur detektor satu-tahap (*one-stage detector*) dan dua-tahap (*two-stage detector*). Representasi fitur yang dihasilkan oleh ConvNeXt banyak digunakan untuk memasok detektor modern seperti [RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md) dan [Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md), di mana efisiensi *backbone* menentukan kelayakan model untuk aplikasi waktu-nyata (*real-time*). Kemampuannya mempertahankan stabilitas representasi spasial juga membuatnya sering digunakan sebagai ekstraktor fitur visual primer pada model deteksi kosakata terbuka (*open-vocabulary detection*) seperti [YOLO-World](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md) dan detektor canggih berbasis kueri seperti [Gold-YOLO](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md), [DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md), [DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md), [Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md), serta [Sparse R-CNN](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi
Kunci BibTeX untuk mensitasi karya ini adalah `liu2022convnext`.

Ringkasan kutipan yang aman digunakan dalam tinjauan pustaka:
> Jaringan ConvNeXt memodernisasi arsitektur CNN murni dengan mengadopsi pilihan desain makro dan mikro dari Vision Transformer, seperti patchify stem, depthwise convolution kernel 7x7, inverted bottleneck, serta minimalisasi lapisan normalisasi dan aktivasi. Eksperimen menunjukkan bahwa ConvNeXt menandingi atau melampaui kinerja Swin Transformer pada ImageNet-1K, COCO, dan ADE20K dengan efisiensi inferensi hardware yang lebih optimal.

Catatan verifikasi data:
- Akurasi *top-1* sebesar 82,1% untuk ConvNeXt-T, 83,1% untuk ConvNeXt-S, dan 83,8% untuk ConvNeXt-B pada ImageNet-1K dengan resolusi input 224x224.
- Hasil deteksi objek pada COCO menggunakan Cascade Mask R-CNN menghasilkan 51,3 AP untuk ConvNeXt-T (naik dari 50,4 AP pada Swin-T) dan 52,7 AP untuk ConvNeXt-B (naik dari 51,9 AP pada Swin-B).
- Hasil segmentasi semantik pada ADE20K menggunakan UperNet menghasilkan 46,0% mIoU untuk ConvNeXt-T dan 49,1% mIoU untuk ConvNeXt-B.
