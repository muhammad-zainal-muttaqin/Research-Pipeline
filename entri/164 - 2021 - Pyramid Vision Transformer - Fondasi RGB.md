# 164 - Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2021pvt` |
| Judul asli | Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions |
| Penulis | Wang, Wenhai; Xie, Enze; Li, Xiang; Fan, Deng-Ping; Song, Kaitao; Liang, Ding; Lu, Tong; Luo, Ping; Shao, Ling |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2102.12122
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Pyramid%20Vision%20Transformer%3A%20A%20Versatile%20Backbone%20for%20Dense%20Prediction%20without%20Convolutions
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Pyramid%20Vision%20Transformer%3A%20A%20Versatile%20Backbone%20for%20Dense%20Prediction%20without%20Convolutions&sort=relevance

## Gambaran Umum
*Pyramid Vision Transformer* (PVT) memperkenalkan paradigma baru dalam penggunaan arsitektur Transformer untuk tugas-tugas *dense prediction* (prediksi tingkat piksel) seperti deteksi objek dan segmentasi semantik. Sebelum PVT diperkenalkan, model *Vision Transformer* (ViT) orisinal hanya dirancang untuk klasifikasi citra global dengan menghasilkan fitur beresolusi tunggal yang kasar. Selain itu, kompleksitas komputasi dari mekanisme *self-attention* (atensi mandiri) pada ViT meningkat secara kuadratis seiring dengan bertambahnya resolusi citra input, menjadikannya sangat berat dan tidak praktis untuk tugas-tugas spasial mendetail. PVT mengatasi keterbatasan ini dengan mengintegrasikan struktur piramida multiskala yang terinspirasi dari arsitektur *convolutional neural network* (CNN) ke dalam kerangka kerja Transformer murni tanpa konvolusi.

Hasil utama dari PVT adalah arsitektur *backbone* (tulang punggung) Transformer serbaguna yang menghasilkan representasi fitur dengan resolusi spasial yang semakin mengecil secara bertahap (skala fitur yang beragam). Untuk menekan beban komputasi atensi pada resolusi tinggi, PVT memperkenalkan mekanisme *spatial-reduction attention* (SRA) yang mengurangi dimensi spasial dari *key* (kunci) dan *value* (nilai) sebelum melakukan operasi atensi. Dengan rancangan ini, PVT mampu memproses citra beresolusi tinggi dengan efisiensi memori yang sebanding dengan CNN tradisional seperti ResNet, namun tetap mempertahankan kemampuan ekstraksi fitur global yang unggul.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Keberhasilan model ViT dalam klasifikasi citra menunjukkan bahwa mekanisme atensi global dapat menggantikan operasi konvolusi lokal dalam mengekstrak representasi visual yang kuat. Namun, ketika ViT dicoba untuk diterapkan pada tugas-tugas visual yang membutuhkan informasi spasial mendetail seperti deteksi objek dan segmentasi semantik, muncul dua kendala utama yang belum terpecahkan.

Pertama, ViT memiliki arsitektur *columnar* (berbentuk kolom tunggal) yang mempertahankan resolusi spasial yang sama di sepanjang seluruh lapisan Transformer (biasanya dengan faktor *stride* sebesar 16). Struktur resolusi tunggal ini tidak cocok untuk tugas *dense prediction*. Metode deteksi objek modern seperti RetinaNet membutuhkan fitur piramidal multiskala untuk mendeteksi objek dengan berbagai variasi ukuran. Objek yang sangat kecil membutuhkan peta fitur beresolusi tinggi (misalnya dengan faktor reduksi 4 kali) untuk mempertahankan detail spasial, sementara objek besar membutuhkan peta fitur beresolusi rendah dengan bidang penerima (*receptive field*) yang luas untuk menangkap konteks objek secara utuh.

Kedua, mekanisme atensi standar dalam ViT menghitung korelasi antara setiap token dengan token lainnya secara penuh. Jika citra input beresolusi tinggi (misalnya $800 \times 1200$ piksel) dibagi menjadi *patch* (tambalan citra) kecil berukuran $4 \times 4$ piksel untuk mempertahankan resolusi tinggi, jumlah token $N$ akan mencapai $60.000$. Karena kompleksitas waktu dan memori dari atensi mandiri bersifat kuadratis terhadap jumlah token ($O(N^2)$), kebutuhan komputasi menjadi sangat tidak fisibel untuk dijalankan pada perangkat keras standar. Oleh karena itu, diperlukan sebuah metode untuk menghasilkan fitur hierarkis multiskala menggunakan Transformer tanpa menimbulkan ledakan komputasi pada lapisan awal yang memproses fitur beresolusi spasial tinggi.

## Ide Utama
Ide utama PVT adalah menggabungkan konsep piramida progresif dari CNN dengan representasi atensi global dari Transformer. PVT membagi jaringan menjadi empat tahap (*stage*) yang secara bertahap menurunkan resolusi spasial peta fitur sekaligus meningkatkan jumlah saluran (*channel*), mirip dengan pola pembagian resolusi pada ResNet.

Untuk mengatasi kompleksitas komputasi $O(N^2)$ pada tahap-tahap awal yang beresolusi tinggi, PVT menggunakan Spatial-Reduction Attention (SRA). Alih-alih menghitung atensi global penuh antara *query* ($Q$), *key* ($K$), dan *value* ($V$) dengan dimensi spasial yang sama besar, SRA menerapkan operasi reduksi spasial terproyeksi khusus pada tensor $K$ dan $V$. Melalui operasi ini, dimensi spasial $K$ dan $V$ dipangkas secara signifikan oleh rasio reduksi ($R_i$), sementara $Q$ tetap dijaga pada resolusi penuh. Peta fitur keluaran dari SRA tetap memiliki resolusi spasial yang tinggi karena ditentukan oleh dimensi $Q$, tetapi biaya komputasi dan kebutuhan memori atensi global diturunkan secara linear sebesar faktor $R_i^2$.

## Cara Kerja Langkah demi Langkah
PVT memproses citra input melalui empat tahap secara berurutan untuk mengekstrak fitur piramidal. 

### Struktur Piramida Progresif
Masing-masing tahap $i$ dalam PVT terdiri dari lapisan pembagian patch (disebut sebagai *patch embedding*) dan beberapa lapisan *transformer encoder*. 

1. **Tahap 1:** Citra input berukuran $H \times W \times 3$ dibagi menjadi token-token berukuran $4 \times 4$ piksel dengan stride 4. Hasil pembagian diproyeksikan secara linear menjadi fitur dengan dimensi $C_1$. Hasilnya adalah peta fitur $F_1$ beresolusi $\frac{H}{4} \times \frac{W}{4} \times C_1$.
2. **Tahap 2:** Output dari Tahap 1, yaitu $F_1$, dibagi lagi menggunakan patch berukuran $2 \times 2$ piksel dengan stride 2. Saluran fitur ditingkatkan menjadi $C_2$. Tahap ini menghasilkan peta fitur $F_2$ beresolusi $\frac{H}{8} \times \frac{W}{8} \times C_2$.
3. **Tahap 3:** Proses yang sama diulang pada output $F_2$ dengan patch berukuran $2 \times 2$ piksel dan stride 2. Saluran fitur ditingkatkan menjadi $C_3$. Tahap ini menghasilkan peta fitur $F_3$ beresolusi $\frac{H}{16} \times \frac{W}{16} \times C_3$.
4. **Tahap 4:** Output $F_3$ diproses kembali dengan patch berukuran $2 \times 2$ piksel dan stride 2 untuk menghasilkan peta fitur akhir $F_4$ beresolusi $\frac{H}{32} \times \frac{W}{32} \times C_4$.

Berikut adalah visualisasi aliran data dan arsitektur piramidal dari PVT:

```
                  Citra Input (H x W x 3)
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ TAHAP 1 (F1: H/4 x W/4 x C1)                            │
 │ ├─ Patch Embedding (4x4, Stride 4)                      │
 │ └─ L1 x Transformer Encoder dengan SRA (Reduction R1=8) │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ TAHAP 2 (F2: H/8 x W/8 x C2)                            │
 │ ├─ Patch Embedding (2x2, Stride 2)                      │
 │ └─ L2 x Transformer Encoder dengan SRA (Reduction R2=4) │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ TAHAP 3 (F3: H/16 x W/16 x C3)                          │
 │ ├─ Patch Embedding (2x2, Stride 2)                      │
 │ └─ L3 x Transformer Encoder dengan SRA (Reduction R3=2) │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │ TAHAP 4 (F4: H/32 x W/32 x C4)                          │
 │ ├─ Patch Embedding (2x2, Stride 2)                      │
 │ └─ L4 x Transformer Encoder dengan SRA (Reduction R4=1) │
 └──────────────────────────┬─────────────────────────────┘
                            │
                            ▼
                  Fitur Piramidal {F1, F2, F3, F4}
              (Umpan balik ke Head Deteksi/Segmentasi)
```

### Mekanisme Spatial-Reduction Attention (SRA)
Mekanisme SRA menggantikan modul *multi-head self-attention* (MHA) standar pada setiap encoder. Secara matematis, operasi SRA menerima input $Q$, $K$, dan $V$. Reduksi spasial dilakukan pada $K$ dan $V$ sebelum proses atensi dihitung.

Langkah reduksi spasial $\text{SR}(X)$ untuk input token $X \in \mathbb{R}^{N_i \times C_i}$ (dengan $N_i = H_i W_i$) didefinisikan sebagai berikut:

$$\text{SR}(X) = \text{LN}(\text{Reshape}(\text{LinearProjection}(\text{Reshape}(X, H_i, W_i, C_i)), \frac{H_i W_i}{R_i^2}, R_i^2 C_i)) W^S$$

Dalam implementasi praktis, reduksi spasial ini dicapai dengan:
1. Mengubah bentuk tensor $X$ dari deret token satu dimensi menjadi representasi citra dua dimensi berukuran $H_i \times W_i \times C_i$.
2. Menerapkan konvolusi 2D dengan ukuran kernel sebesar $R_i$ dan stride sebesar $R_i$ untuk mereduksi dimensi spasial dari $H_i \times W_i$ menjadi $\frac{H_i}{R_i} \times \frac{W_i}{R_i}$.
3. Mengubah kembali bentuk tensor menjadi deret token sepanjang $N_i' = \frac{H_i W_i}{R_i^2}$ dengan dimensi saluran sebesar $C_i$.
4. Menerapkan *layer normalization* (normalisasi lapisan) untuk menstabilkan aktivasi.
5. Menerapkan proyeksi linear menggunakan matriks parameter $W^S \in \mathbb{R}^{C_i \times C_i}$ untuk menyelaraskan dimensi saluran keluaran.

Setelah reduksi spasial dilakukan pada $K$ dan $V$, nilai atensi untuk setiap kepala atensi (*attention head*) dihitung menggunakan persamaan:

$$\text{head}_j = \text{Attention}(QW_j^Q, \text{SR}(K)W_j^K, \text{SR}(V)W_j^V)$$

$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_{head}}}\right) V$$

Di sini, matriks atensi $Q K^T$ berdimensi $N_i \times N_i'$. Karena $N_i' = \frac{N_i}{R_i^2}$, kompleksitas memori dan FLOPs berkurang sebesar $R_i^2$ kali lipat dibanding atensi standar.

### Contoh Numerik Konkret
Sebagai contoh konkret, mari kita tinjau varian PVT-Small yang memproses citra input beresolusi $224 \times 224$ piksel:

1. **Tahap 1:** Resolusi spasial input adalah $H_1 = 56$ dan $W_1 = 56$, sehingga jumlah token $N_1 = 3136$. Dimensi saluran $C_1 = 64$. Rasio reduksi diatur sebesar $R_1 = 8$. Tanpa SRA, kalkulasi atensi mandiri membutuhkan matriks berukuran $3136 \times 3136$ (sekitar 9,8 juta elemen). Dengan SRA, dimensi $K$ dan $V$ direduksi menjadi $N_1' = \frac{3136}{8^2} = 49$. Matriks atensi yang dihasilkan hanya berukuran $3136 \times 49$ (sekitar 153 ribu elemen).
2. **Tahap 2:** Resolusi spasial input adalah $H_2 = 28$ dan $W_2 = 28$, sehingga jumlah token $N_2 = 784$. Dimensi saluran $C_2 = 128$. Rasio reduksi $R_2 = 4$. Panjang token tereduksi adalah $N_2' = \frac{784}{16} = 49$. Matriks atensi berukuran $784 \times 49$.
3. **Tahap 3:** Resolusi spasial input adalah $H_3 = 14$ dan $W_3 = 14$, sehingga jumlah token $N_3 = 196$. Dimensi saluran $C_3 = 320$. Rasio reduksi $R_3 = 2$. Panjang token tereduksi adalah $N_3' = \frac{196}{4} = 49$. Matriks atensi berukuran $196 \times 49$.
4. **Tahap 4:** Resolusi spasial input adalah $H_4 = 7$ dan $W_4 = 7$, sehingga jumlah token $N_4 = 49$. Dimensi saluran $C_4 = 512$. Rasio reduksi $R_4 = 1$. Karena rasio reduksi bernilai 1, SRA bertindak sebagai atensi mandiri global standar tanpa reduksi spasial. Matriks atensi berukuran $49 \times 49$.

Menarik untuk dicatat bahwa pada seluruh tahap di atas, jumlah token untuk $K$ dan $V$ selalu bernilai konstan ($N_i' = 49$) untuk input $224 \times 224$ piksel. Hal ini menjaga agar kompleksitas komputasi atensi pada semua lapisan tetap terdistribusi secara seimbang.

## Eksperimen dan Hasil
PVT dievaluasi secara ekstensif pada dataset klasifikasi ImageNet-1K, dataset deteksi objek COCO, dan dataset segmentasi semantik ADE20K. Penulis memperkenalkan empat varian ukuran model: PVT-Tiny, PVT-Small, PVT-Medium, dan PVT-Large.

Tabel di bawah menyajikan performa PVT pada klasifikasi ImageNet-1K:

| Varian Model | Parameter (M) | GFLOPs (224x224) | Top-1 Akurasi (%) |
| :--- | :---: | :---: | :---: |
| **PVT-Tiny** | 13,2 | 1,9 | 75,1 |
| **PVT-Small** | 24,5 | 3,8 | 79,8 |
| **PVT-Medium** | 44,2 | 6,7 | 81,2 |
| **PVT-Large** | 61,4 | 9,8 | 81,7 |

Sebagai perbandingan, model ResNet50 (backbone CNN standar) memiliki 25,6M parameter dengan akurasi Top-1 sebesar 76,1%. PVT-Small dengan parameter yang sebanding (24,5M) mencapai akurasi 79,8%, yang berarti unggul 3,7% secara mutlak dibanding ResNet50.

Untuk tugas deteksi objek pada dataset COCO val2017, PVT diintegrasikan dengan detektor RetinaNet (1x training schedule). Hasilnya menunjukkan keunggulan PVT dibandingkan ResNet:
- PVT-Tiny + RetinaNet (23,0M parameter) memperoleh 36,7% Box AP.
- PVT-Small + RetinaNet (34,2M parameter) memperoleh 40,4% Box AP.
- PVT-Medium + RetinaNet (53,9M parameter) memperoleh 41,9% Box AP.
- PVT-Large + RetinaNet (71,1M parameter) memperoleh 42,6% Box AP.

Sebagai pembanding, ResNet50 + RetinaNet (37,7M parameter) memperoleh 36,3% Box AP. PVT-Small yang memiliki parameter lebih sedikit dan beban komputasi sebanding mampu mengungguli ResNet50 dengan margin 4,1% AP mutlak.

Pada tugas segmentasi instans menggunakan framework Mask R-CNN (COCO val2017):
- PVT-Tiny + Mask R-CNN memperoleh 36,7% Box AP dan 35,1% Mask AP.
- PVT-Small + Mask R-CNN memperoleh 40,4% Box AP dan 37,8% Mask AP.

Angka ini melampaui ResNet50 + Mask R-CNN (38,0% Box AP dan 34,4% Mask AP) dengan jumlah parameter yang setara (sekitar 44M).

Pada segmentasi semantik di dataset ADE20K menggunakan decoder Semantic FPN:
- PVT-Tiny + Semantic FPN memperoleh 35,7% mIoU.
- PVT-Small + Semantic FPN memperoleh 39,8% mIoU.
- PVT-Large + Semantic FPN memperoleh 42,1% mIoU.

Sebagai pembanding, ResNet50 + Semantic FPN memperoleh 36,7% mIoU, menegaskan bahwa representasi atensi global yang diekstrak PVT memberikan pemahaman semantik kontekstual yang lebih baik dibandingkan representasi konvolusi lokal.

## Kelebihan dan Keterbatasan
PVT menawarkan sejumlah kelebihan penting, namun juga memiliki keterbatasan bawaan.

**Kelebihan:**
1. Jaringan ini merupakan backbone Transformer murni bebas konvolusi pertama yang mampu menghasilkan fitur piramidal multiskala yang kompatibel langsung dengan head deteksi dan segmentasi standar (seperti RetinaNet, Mask R-CNN, dan Semantic FPN).
2. Mekanisme Spatial-Reduction Attention (SRA) berhasil memotong kompleksitas kuadratis atensi global, memungkinkan penggunaan Transformer pada lapisan beresolusi tinggi dengan input citra besar tanpa kendala memori GPU.
3. Menawarkan trade-off performa-versus-parameter yang sangat kompetitif, secara konsisten melampaui ResNet dan ResNeXt pada berbagai tugas hilir visual.

**Keterbatasan:**
1. Dari sisi rekayasa, pengurangan resolusi spasial pada Key dan Value dalam SRA dilakukan menggunakan operasi konvolusi dengan stride besar. Hal ini berpotensi menghilangkan informasi spasial halus pada lapisan-lapisan awal, yang sangat krusial untuk mendeteksi tepi tajam atau objek yang sangat kecil.
2. Secara konseptual, PVT menggunakan *positional embedding* (penyematan posisi) absolut yang bersifat statis. Akibatnya, model ini tidak fleksibel saat menghadapi perubahan resolusi citra input pada fase inferensi (misalnya saat mendeteksi citra beresolusi tinggi $800 \times 1200$). Positional embedding harus di-interpolasi secara linear, yang sering kali mendegradasi akurasi karena Transformer sangat sensitif terhadap gangguan koordinat spasial token.
3. Meskipun SRA mereduksi kompleksitas sebesar $R_i^2$, kompleksitas komputasi atensi secara fundamental tetap bersifat kuadratis terhadap jumlah token input. Ketika menangani resolusi citra yang sangat tinggi (misal citra medis gigapiksel), komputasi SRA tetap akan mengalami peningkatan beban secara kuadratis jika rasio reduksi tidak disesuaikan secara dinamis.

## Kaitan dengan Bab Lain
PVT menempati posisi silsilah yang penting dalam transisi dari model Vision Transformer orisinal menuju backbone visual Transformer hierarkis modern:

1. **Mewarisi dari Vision Transformer (ViT):** PVT mewarisi konsep *self-attention* global dari [Vision Transformer (ViT)](./024%20-%202021%20-%20Vision%20Transformer%20(ViT)%20-%20Fondasi%20RGB.md). Perbedaannya, jika ViT menggunakan arsitektur resolusi tunggal sepanjang jaringan, PVT memodifikasinya menjadi arsitektur hierarkis piramida progresif.
2. **Alternatif bagi Swin Transformer:** PVT dirilis hampir bersamaan dengan [Swin Transformer](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md). Keduanya memecahkan masalah kompleksitas atensi resolusi tinggi dengan cara yang berbeda. Swin Transformer membatasi atensi secara lokal dalam jendela bergeser untuk mencapai kompleksitas linear, sedangkan PVT tetap mempertahankan atensi global dengan mereduksi resolusi spasial token Key dan Value melalui SRA.
3. **Evolusi pada Swin Transformer V2:** Keterbatasan PVT terkait positional embedding statis dan hilangnya detail spasial halus diatasi pada generasi berikutnya, seperti pada [Swin Transformer V2](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md) yang mengadopsi *continuous position bias* serta PVTv2 yang menggunakan *overlapping patch embedding* tanpa positional embedding absolut.
4. **Penyedia Fitur bagi Detektor Transformer Modern:** Peta fitur piramidal yang dihasilkan oleh PVT menjadi basis penting bagi detektor objek berbasis Transformer generasi berikutnya. Detektor-detektor seperti [Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md), [DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md), [DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md), dan [Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md) sangat bergantung pada backbone dengan kemampuan multiskala untuk mengumpankan representasi spasial berkualitas tinggi ke dalam decoder Transformer mereka.
5. **Kaitan dengan RT-DETR:** Konsep efisiensi representasi atensi yang diinisiasi oleh PVT mengarah pada pengembangan detektor real-time seperti [RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md), yang memadukan backbone vision efisien dengan pemrosesan atensi hibrida untuk mengeliminasi ketergantungan terhadap operasi *non-maximum suppression* (NMS) pasca-pemrosesan.
6. **Korelasi dengan ConvNeXt:** Desain piramida modular PVT dan Swin juga memicu respons dari kubu CNN melalui [ConvNeXt](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md), yang memodernisasi CNN klasik ([ResNet](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)) dengan meniru komponen desain Transformer (seperti pemisahan tahap patchify) guna menantang dominasi model Transformer hierarkis.
7. **Kaitan dengan Sparse R-CNN:** Modul deteksi dua-tahap modern seperti [Sparse R-CNN](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md) memanfaatkan peta fitur multiskala yang diekstrak oleh PVT untuk memperbarui proposal bounding box secara dinamis tanpa bergantung pada *anchor* (jangkar) padat.
8. **Kaitan dengan FPN dan RetinaNet:** Integrasi PVT dengan [Feature Pyramid Networks (FPN)](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20(FPN)%20-%20Fondasi%20RGB.md) dan [RetinaNet (Focal Loss)](./016%20-%202017%20-%20RetinaNet%20(Focal%20Loss)%20-%20Fondasi%20RGB.md) membuktikan kelayakan Transformer bebas konvolusi sebagai pengganti langsung dari backbone CNN dalam tugas-tugas deteksi objek multiskala tradisional.

## Poin untuk Sitasi
Kunci BibTeX: `wang2021pvt`

Ringkasan kutipan:
"Pyramid Vision Transformer (PVT) memperkenalkan struktur piramida progresif bebas konvolusi pertama untuk vision transformer, yang memungkinkannya menghasilkan fitur multiskala untuk tugas-tugas dense prediction. Melalui mekanisme Spatial-Reduction Attention (SRA), PVT secara efisien mereduksi dimensi spasial token Key dan Value untuk menjaga kompleksitas komputasi atensi global tetap terkendali pada citra resolusi tinggi."

Catatan verifikasi:
Nilai AP RetinaNet+PVT-Small (40,4 AP) dan AP RetinaNet+ResNet50 (36,3 AP) diverifikasi langsung dari eksperimen COCO val2017 pada naskah asli. Kinerja segmentasi semantik (42,1% mIoU pada ADE20K menggunakan Semantic FPN dengan backbone PVT-Large) telah sesuai dengan klaim yang dilaporkan oleh Wang dkk. pada prosiding ICCV 2021.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
1. CLS 2. DET 3. SEG ...

1. CLS TF-E 3 TF-E 2 !×

Figure 1: Comparisons of different architectures, where “Conv” and “TF-E” stand for “convolution” and “Transformer encoder”, respectively. (a) Many CNN backbones use a pyramid structure for dense prediction tasks such as object detection (DET), instance and semantic segmentation (SEG). (b) The recently proposed Vision Transformer (ViT) [13] is a “columnar” structure specifically designed for image classification (CLS). (c) By incorporating the pyramid structure from CNNs, we present the Pyramid Vision Transformer (PVT), which can be used as a versatile backbone for many computer vision tasks, broadening the scope and impact of ViT. Moreover, our experiments also show that PVT can easily be combined with DETR [6] to build an end-to-end object detection system without convolutions.

Abstract

ous vision tasks without convolutions, where it can be used as a direct replacement for CNN backbones. (3) We validate PVT through extensive experiments, showing that it boosts the performance of many downstream tasks, including object detection, instance and semantic segmentation. For example, with a comparable number of parameters, PVT+RetinaNet achieves 40.4 AP on the COCO dataset, surpassing ResNet50+RetinNet (36.3 AP) by 4.1 absolute AP (see Figure 2). We hope that PVT could serve as an alternative and useful backbone for pixel-level predictions and facilitate future research.

Although convolutional neural networks (CNNs) have achieved great success in computer vision, this work investigates a simpler, convolution-free backbone network useful for many dense prediction tasks. Unlike the recentlyproposed Vision Transformer (ViT) that was designed for image classification specifically, we introduce the Pyramid Vision Transformer (PVT), which overcomes the difficulties of porting Transformer to various dense prediction tasks. PVT has several merits compared to current state of the arts. (1) Different from ViT that typically yields lowresolution outputs and incurs high computational and memory costs, PVT not only can be trained on dense partitions of an image to achieve high output resolution, which is important for dense prediction, but also uses a progressive shrinking pyramid to reduce the computations of large feature maps. (2) PVT inherits the advantages of both CNN and Transformer, making it a unified backbone for vari-

44 PVT-M

Figure 2: Performance comparison on COCO val2017 of different backbones using RetinaNet for object detection, where “T”, “S”, “M” and “L” denote our PVT models with tiny, small, medium and large size. We see that when the number of parameters among different models are comparable, PVT variants significantly outperform their corresponding counterparts such as ResNets (R) [22], ResNeXts (X) [73], and ViT [13].

tion [40, 14], semantic [83] and instance segmentation [40], in addition to image classification [12]. Inspired by the success of Transformer [64] in natural language processing, many researchers have explored its application in computer vision. For example, some works [6, 85, 72, 56, 24, 42] model the vision task as a dictionary lookup problem with learnable queries, and use the Transformer decoder as a task-specific head on top of the CNN backbone. Although some prior arts have also incorporated attention modules [70, 48, 80] into CNNs, as far as we know, exploring a clean and convolution-free Transformer backbone to address dense prediction tasks in computer vision is rarely studied. Recently, Dosovitskiy et al. [13] introduced the Vision Transformer (ViT) for image classification. This is an interesting and meaningful attempt to replace the CNN backbone with a convolution-free model. As shown in Figure 1 (b), ViT has a columnar structure with coarse image patches as input.1 Although ViT is applicable to image classification, it is challenging to directly adapt it to pixel-level dense predictions such as object detection and segmentation, because (1) its output feature map is single-scale and low-resolution, and (2) its computational and memory costs are relatively high even for common input image sizes (e.g., 1 Due

shorter edge of 800 pixels in the COCO benchmark [40]). To address the above limitations, this work proposes a pure Transformer backbone, termed Pyramid Vision Transformer (PVT), which can serve as an alternative to the CNN backbone in many downstream tasks, including image-level prediction as well as pixel-level dense predictions. Specifically, as illustrated in Figure 1 (c), our PVT overcomes the difficulties of the conventional Transformer by (1) taking fine-grained image patches (i.e., 4×4 pixels per patch) as input to learn high-resolution representation, which is essential for dense prediction tasks; (2) introducing a progressive shrinking pyramid to reduce the sequence length of Transformer as the network deepens, significantly reducing the computational cost, and (3) adopting a spatial-reduction attention (SRA) layer to further reduce the resource consumption when learning high-resolution features. Overall, the proposed PVT possesses the following merits. Firstly, compared to the traditional CNN backbones (see Figure 1 (a)), which have local receptive fields that increase with the network depth, our PVT always produces a global receptive field, which is more suitable for detection and segmentation. Secondly, compared to ViT (see Figure 1 (b)), thanks to its advanced pyramid structure, our method can more easily be plugged into many representative dense prediction pipelines, e.g., RetinaNet [39] and Mask R-CNN [21]. Thirdly, we can build a convolutionfree pipeline by combining our PVT with other task-specific Transformer decoders, such as PVT+DETR [6] for object detection. To our knowledge, this is the first entirely convolution-free object detection pipeline. Our main contributions are as follows: (1) We propose Pyramid Vision Transformer (PVT), which is the first pure Transformer backbone designed for various pixel-level dense prediction tasks. Combining our PVT and DETR, we can construct an end-to-end object detection system without convolutions and handcrafted components such as dense anchors and non-maximum suppression (NMS). (2) We overcome many difficulties when porting Transformer to dense predictions, by designing a progressive shrinking pyramid and a spatial-reduction attention (SRA). These are able to reduce the resource consumption of Transformer, making PVT flexible to learning multi-scale and high-resolution features. (3) We evaluate the proposed PVT on several different tasks, including image classification, object detection, instance and semantic segmentation, and compare it with popular ResNets [22] and ResNeXts [73]. As presented in Figure 2, our PVT with different parameter scales can consistently archived improved performance compared to the prior arts. For example, under a comparable number of parameters, using RetinaNet [39] for object detection, PVT-Small achieves 40.4 AP on COCO val2017, outper-

2. Related Work 2.1. CNN Backbones CNNs are the work-horses of deep neural networks in visual recognition. The standard CNN was first introduced in [34] to distinguish handwritten numbers. The model contains convolutional kernels with a certain receptive field that captures favorable visual context. To provide translation equivariance, the weights of convolutional kernels are shared over the entire image space. More recently, with the rapid development of the computational resources (e.g., GPU), the successful training of stacked convolutional blocks [33, 54] on large-scale image classification datasets (e.g., ImageNet [51]) has become possible. For instance, GoogLeNet [59] demonstrated that a convolutional operator containing multiple kernel paths can achieve very competitive performance. The effectiveness of a multi-path convolutional block was further validated in Inception series [60, 58], ResNeXt [73], DPN [10], MixNet [65] and SKNet [36]. Further, ResNet [22] introduced skip connections into the convolutional block, making it possible to create/train very deep networks and obtaining impressive results in the field of computer vision. DenseNet [25] introduced a densely connected topology, which connects each convolutional block to all previous blocks. More recent advances can be found in recent survey/review papers [31, 53]. Unlike the full-blown CNNs, the vision Transformer backbone is still in its early stage of development. In this work, we try to extend the scope of Vision Transformer by designing a new versatile Transformer backbone suitable for most vision tasks.

resolution or multi-scale feature maps for accurate object detection. Semantic Segmentation. CNNs also play an important role in semantic segmentation. In the early stages, FCN [44] introduced a fully convolutional architecture to generate a spatial segmentation map for a given image of any size. After that, the deconvolution operation was introduced by Noh et al. [47] and achieved impressive performance on the PASCAL VOC 2012 dataset [52]. Inspired by FCN, UNet [50] was proposed for the medical image segmentation domain specifically, bridging the information flow between corresponding low-level and high-level feature maps of the same spatial sizes. To explore richer global context representation, Zhao et al. [81] designed a pyramid pooling module over various pooling scales, and Kirillov et al. [32] developed a lightweight segmentation head termed Semantic FPN, based on FPN [38]. Finally, the DeepLab family [8, 41] applies dilated convolutions to enlarge the receptive field while maintaining the feature map resolution. Similar to object detection methods, semantic segmentation models also rely on high-resolution or multi-scale feature maps.

2.3. Self-Attention and Transformer in Vision As convolutional filter weights are usually fixed after training, they cannot be dynamically adapted to different inputs. Many methods have been proposed to alleviate this problem using dynamic filters [30] or self-attention operations [64]. The non-local block [70] attempts to model long-range dependencies in both space and time, which has been shown beneficial for accurate video classification. However, despite its success, the non-local operator suffers from the high computational and memory costs. Criss-cross [26] further reduces the complexity by generating sparse attention maps through a criss-cross path. Ramachandran et al. [48] proposed the stand-alone selfattention to replace convolutional layers with local selfattention units. AANet [3] achieves competitive results when combining the self-attention and convolutional operations. LambdaNetworks [2] uses the lambda layer, an efficient self-attention to replace the convolution in the CNN. DETR [6] utilizes the Transformer decoder to model object detection as an end-to-end dictionary lookup problem with learnable queries, successfully removing the need for handcrafted processes such as NMS. Based on DETR, deformable DETR [85] further adopts a deformable attention layer to focus on a sparse set of contextual elements, obtaining faster convergence and better performance. Recently, Vision Transformer (ViT) [13] employs a pure Transformer [64] model for image classification by treating an image as a sequence of patches. DeiT [63] further extends ViT using a novel distillation approach. Different from previous models, this work introduces the pyramid structure into Transformer to present a pure Transformer

Figure 3: Overall architecture of Pyramid Vision Transformer (PVT). The entire model is divided into four stages, each of which is comprised of a patch embedding layer and a Li -layer Transformer encoder. Following a pyramid structure, the output resolution of the four stages progressively shrinks from high (4-stride) to low (32-stride). backbone for dense prediction tasks, rather than a taskspecific head or an image classification model.

downstream tasks, including image classification, object detection, and semantic segmentation.

3. Pyramid Vision Transformer (PVT)

3.2. Feature Pyramid for Transformer

3.1. Overall Architecture

Unlike CNN backbone networks [54, 22], which use different convolutional strides to obtain multi-scale feature maps, our PVT uses a progressive shrinking strategy to control the scale of feature maps by patch embedding layers. Here, we denote the patch size of the i-th stage as Pi . At the beginning of stage i, we first evenly divide the input feai−1 ture map Fi−1 ∈ RHi−1×Wi−1×Ci−1 into Hi−P1 W patches, and 2 i then each patch is flatten and projected to a Ci -dimensional embedding. After the linear projection, the shape of the embedded patches can be viewed as HPi−i 1 × WPi−i 1 × Ci , where the height and width are Pi times smaller than the input. In this way, we can flexibly adjust the scale of the feature map in each stage, making it possible to construct a feature pyramid for Transformer.

Our goal is to introduce the pyramid structure into the Transformer framework, so that it can generate multi-scale feature maps for dense prediction tasks (e.g., object detection and semantic segmentation). An overview of PVT is depicted in Figure 3. Similar to CNN backbones [22], our method has four stages that generate feature maps of different scales. All stages share a similar architecture, which consists of a patch embedding layer and Li Transformer encoder layers. In the first stage, given an input image of size H×W ×3, 2 we first divide it into HW 42 patches, each of size 4×4×3. Then, we feed the flattened patches to a linear projection and obtain embedded patches of size HW 42 ×C1 . After that, the embedded patches along with a position embedding are passed through a Transformer encoder with L1 layers, and W the output is reshaped to a feature map F1 of size H 4 × 4 ×C1 . In the same way, using the feature map from the previous stage as input, we obtain the following feature maps: F2 , F3 , and F4 , whose strides are 8, 16, and 32 pixels with respect to the input image. With the feature pyramid {F1 , F2 , F3 , F4 }, our method can be easily applied to most 2 As done for ResNet, we keep the highest resolution of our output feature map at 4-stride.

3.3. Transformer Encoder The Transformer encoder in the stage i has Li encoder layers, each of which is composed of an attention layer and a feed-forward layer [64]. Since PVT needs to process high-resolution (e.g., 4-stride) feature maps, we propose a spatial-reduction attention (SRA) layer to replace the traditional multi-head attention (MHA) layer [64] in the encoder. Similar to MHA, our SRA receives a query Q, a key K, and a value V as input, and outputs a refined feature. The difference is that our SRA reduces the spatial scale of K

Through these formulas, we can find that the computational/memory costs of our attention operation are Ri2 times lower than those of MHA, so our SRA can handle larger input feature maps/sequences with limited resources.

Following the design rules of ResNet [22], we (1) use small output channel numbers in shallow stages; and (2) concentrate the major computation resource in intermediate stages. To provide instances for discussion, we describe a series of PVT models with different scales, namely PVT-Tiny, Small, -Medium, and -Large, in Table 1, whose parameter numbers are comparable to ResNet18, 50, 101, and 152 respectively. More details of employing these models in specific downstream tasks will be introduced in Section 4.

3.5. Discussion The most related work to our model is ViT [13]. Here, we discuss the relationship and differences between them. First, both PVT and ViT are pure Transformer models without convolutions. The primary difference between them is the pyramid structure. Similar to the traditional Transformer [64], the length of ViT’s output sequence is the same as the input, which means that the output of ViT is singlescale (see Figure 1 (b)). Moreover, due to the limited resource, the input of ViT is coarse-grained (e.g., the patch size is 16 or 32 pixels), and thus its output resolution is relatively low (e.g., 16-stride or 32-stride). As a result, it is difficult to directly apply ViT to dense prediction tasks that require high-resolution or multi-scale feature maps. Our PVT breaks the routine of Transformer by introducing a progressive shrinking pyramid. It can generate multi-scale feature maps like a traditional CNN backbone. In addition, we also designed a simple but effective attention layer—SRA, to process high-resolution feature maps and reduce computational/memory costs. Benefiting from the above designs, our method has the following advantages over ViT: 1) more flexible—can generate feature maps of different scales/channels in different stages; 2) more versatile—can be easily plugged and played in most downstream task models; 3) more friendly to computation/memory—can handle higher resolution feature maps or longer sequences.

4. Application to Downstream Tasks 4.1. Image-Level Prediction Image classification is the most classical task of imagelevel prediction. To provide instances for discussion, we design a series of PVT models with different scales, namely PVT-Tiny, -Small, -Medium, and -Large, whose parameter numbers are similar to ResNet18, 50, 101, and 152, respec-

Table 1: Detailed settings of PVT series. The design follows the two rules of ResNet [22]: (1) with the growth of network depth, the hidden dimension gradually increases, and the output resolution progressively shrinks; (2) the major computation resource is concentrated in Stage 3. tively. Detailed hyper-parameter settings of the PVT series are provided in the supplementary material (SM). For image classification, we follow ViT [13] and DeiT [63] to append a learnable classification token to the input of the last stage, and then employ a fully connected (FC) layer to conduct classification on top of the token.

be an arbitrary shape, the position embeddings pre-trained on ImageNet may no longer be meaningful. Therefore, we perform bilinear interpolation on the pre-trained position embeddings according to the input resolution.

4.2. Pixel-Level Dense Prediction

In addition to image-level prediction, dense prediction that requires pixel-level classification or regression to be performed on the feature map, is also often seen in downstream tasks. Here, we discuss two typical tasks, namely object detection, and semantic segmentation. We apply our PVT models to three representative dense prediction methods, namely RetinaNet [39], Mask RCNN [21], and Semantic FPN [32]. RetinaNet is a widely used single-stage detector, Mask R-CNN is the most popular two-stage instance segmentation framework, and Semantic FPN is a vanilla semantic segmentation method without special operations (e.g., dilated convolution). Using these methods as baselines enables us to adequately examine the effectiveness of different backbones. The implementation details are as follows: (1) Like ResNet, we initialize the PVT backbone with the weights pre-trained on ImageNet; (2) We use the output feature pyramid {F1 , F2 , F3 , F4 } as the input of FPN [38], and then the refined feature maps are fed to the follow-up detection/segmentation head; (3) When training the detection/segmentation model, none of the layers in PVT are frozen; (4) Since the input for detection/segmentation can

5. Experiments

5.1. Image Classification Settings. Image classification experiments are performed on the ImageNet 2012 dataset [51], which comprises 1.28 million training images and 50K validation images from 1,000 categories. For fair comparison, all models are trained on the training set, and report the top-1 error on the validation set. We follow DeiT [63] and apply random cropping, random horizontal flipping [59], label-smoothing regularization [60], mixup [78], CutMix [76], and random erasing [82] as data augmentations. During training, we employ AdamW [46] with a momentum of 0.9, a mini-batch size of 128, and a weight decay of 5 × 10−2 to optimize models. The initial learning rate is set to 1 × 10−3 and decreases following the cosine schedule [45]. All models are trained for 300 epochs from scratch on 8 V100 GPUs. To benchmark, we apply a center crop on the validation set, where a 224× 224 patch is cropped to evaluate the classification accuracy. Results. In Table 2, we see that our PVT models are superior to conventional CNN backbones under similar parameter numbers and computational budgets. For example, when

Table 2: Image classification performance on the ImageNet validation set. “#Param” refers to the number of parameters. “GFLOPs” is calculated under the input scale of 224 × 224. “*” indicates the performance of the method trained under the strategy of its original paper.

the GFLOPs are roughly similar, the top-1 error of PVTSmall reaches 20.2, which is 1.3 points higher than that of ResNet50 [22] (20.2 vs. 21.5). Meanwhile, under similar or lower complexity, PVT models archive performances comparable to the recently proposed Transformer-based models, such as ViT [13] and DeiT [63] (PVT-Large: 18.3 vs. ViT(DeiT)-Base/16: 18.3). Here, we clarify that these results are within our expectations, because the pyramid structure is beneficial to dense prediction tasks, but brings little improvements to image classification. Note that ViT and DeiT have limitations as they are specifically designed for classification tasks, and thus are not suitable for dense prediction tasks, which usually require effective feature pyramids.

5.2. Object Detection Settings. Object detection experiments are conducted on the challenging COCO benchmark [40]. All models are trained on COCO train2017 (118k images) and evaluated on val2017 (5k images). We verify the effectiveness of PVT backbones on top of two standard detectors, namely RetinaNet [39] and Mask R-CNN [21]. Before training, we use the weights pre-trained on ImageNet to initialize the backbone and Xavier [18] to initialize the newly added lay-

ers. Our models are trained with a batch size of 16 on 8 V100 GPUs and optimized by AdamW [46] with an initial learning rate of 1 × 10−4 . Following common practices [39, 21, 7], we adopt 1× or 3× training schedule (i.e., 12 or 36 epochs) to train all detection models. The training image is resized to have a shorter side of 800 pixels, while the longer side does not exceed 1,333 pixels. When using the 3× training schedule, we randomly resize the shorter side of the input image within the range of [640, 800]. In the testing phase, the shorter side of the input image is fixed to 800 pixels. Results. As shown in Table 3, when using RetinaNet for object detection, we find that under comparable number of parameters, the PVT-based models significantly surpasses their counterparts. For example, with the 1× training schedule, the AP of PVT-Tiny is 4.9 points better than that of ResNet18 (36.7 vs. 31.8). Moreover, with the 3× training schedule and multi-scale training, PVT-Large archive the best AP of 43.4, surpassing ResNeXt101-64x4d (43.4 vs. 41.8), while our parameter number is 30% fewer. These results indicate that our PVT can be a good alternative to the CNN backbone for object detection. Similar results are found in instance segmentation experiments based on Mask R-CNN, as shown in Table 4. With the 1× training schedule, PVT-Tiny achieves 35.1 mask AP (APm ), which is 3.9 points better than ResNet18 (35.1 vs. 31.2) and even 0.7 points higher than ResNet50 (35.1 vs. 34.4). The best APm obtained by PVT-Large is 40.7, which is 1.0 points higher than ResNeXt101-64x4d (40.7 vs. 39.7), with 20% fewer parameters.

5.3. Semantic Segmentation Settings. We choose ADE20K [83], a challenging scene parsing dataset, to benchmark the performance of semantic segmentation. ADE20K contains 150 fine-grained semantic categories, with 20,210, 2,000, and 3,352 images for training, validation, and testing, respectively. We evaluate our PVT backbones on the basis of Semantic FPN [32], a simple segmentation method without dilated convolutions [74]. In the training phase, the backbone is initialized with the weights pre-trained on ImageNet [12], and other newly added layers are initialized with Xavier [18]. We optimize our models using AdamW [46] with an initial learning rate of 1e-4. Following common practices [32, 8], we train our models for 80k iterations with a batch size of 16 on 4 V100 GPUs. The learning rate is decayed following the polynomial decay schedule with a power of 0.9. We randomly resize and crop the image to 512 × 512 for training, and rescale to have a shorter side of 512 pixels during testing. Results. As shown in Table 5, when using Semantic FPN [32] for semantic segmentation, PVT-based models consistently outperforms the models based on ResNet [22] or ResNeXt [73]. For example, with al-

Table 4: Object detection and instance segmentation performance on COCO val2017. APb and APm denote bounding box AP and mask AP, respectively. .

Table 5: Semantic segmentation performance of different backbones on the ADE20K validation set. “GFLOPs” is calculated under the input scale of 512 × 512. “*” indicates 320K iterations training and multi-scale flip testing.

most the same number of parameters and GFLOPs, our PVT-Tiny/Small/Medium are at least 2.8 points higher than ResNet-18/50/101. In addition, although the parameter number and GFLOPs of our PVT-Large are 20% lower than those of ResNeXt101-64x4d, the mIoU is still 1.9 points higher (42.1 vs. 40.2). With a longer training schedule and multi-scale testing, PVT-Large+Semantic FPN archives the best mIoU of 44.8, which is very close to the state-of-the-art performance of the ADE20K benchmark. Note that Semantic FPN is just a simple segmentation head. These results demonstrate that our PVT backbones can extract better features for semantic segmentation than the CNN backbone,

Method ResNet50 [22] PVT-Small (ours)

Table 6: Performance of the pure Transformer object detection pipeline. We build a pure Transformer detector by combining PVT and DETR [6], whose AP is 2.4 points higher than the original DETR based on ResNet50 [22].

5.4. Pure Transformer Detection & Segmentation PVT+DETR. To reach the limit of no convolution, we build a pure Transformer pipeline for object detection by simply combining our PVT with a Transformer-based detection head—DETR [6]. We train models on COCO train2017 for 50 epochs with an initial learning rate of 1 × 10−4 . The learning rate is divided by 10 at the 33rd epoch. We use random flipping and multi-scale training as data augmentation. All other experimental settings is the same as those in Sec. 5.2. As reported in Table 6, PVT-based DETR archieves 34.7 AP on COCO val2017, outperforming the original ResNet50-based DETR by 2.4 points (34.7 vs. 32.3). These results prove that a pure Transformer detector can also works well in the object detection task. PVT+Trans2Seg.We build a pure Transformer model for semantic segmentation by combining our PVT with

Table 8: Performance comparison between ViT and our PVT using RetinaNet for object detection. ViT-Small/4 runs out of GPU memory due to small patch size (i.e., 4×4 per patch). ViT-Small/32 obtains 31.7 AP on COCO val2017, which is 8.7 points lower than our PVT-Small.

Trans2Seg [72], a Transformer-based segmentation head. According to the experimental settings in Sec. 5.3, we perform experiments on ADE20K [83] with 40k iterations training, single scale testing, and compare it with ResNet50+Trans2Seg [72] and DeeplabV3+ [9] with ResNet50-d8 (dilation 8) and -d16(dilation 8) in Table 7. We find that our PVT-Small+Trans2Seg achieves 42.6 mIoU, outperforming ResNet50-d8+DeeplabV3+ (41.5). Note that, ResNet50-d8+DeeplabV3+ has 120.5 GFLOPs due to the high computation cost of dilated convolution, and our method has only 31.6 GFLOPs, which is 4 times fewer. In addition, our PVT-Small+Trans2Seg performs better than ResNet50-d16+Trans2Seg (mIoU: 42.6 vs. 39.7, GFlops: 31.6 vs. 79.3). These results prove that a pure Transformer segmentation network is workable.

5.5. Ablation Study Settings. We conduct ablation studies on ImageNet [12] and COCO [40] datasets. The experimental settings on ImageNet are the same as the settings in Sec. 5.1. For COCO, all models are trained with a 1× training schedule (i.e., 12 epochs) and without multi-scale training, and other settings follow those in Sec. 5.2. Pyramid Structure. A Pyramid structure is crucial when applying Transformer to dense prediction tasks. ViT (see Figure 1 (b)) is a columnar framework, whose output is single-scale. This results in a low-resolution output feature map when using coarse image patches (e.g., 32×32 pixels per patch) as input, leading to poor detection perfor-

Table 7: Performance of the pure Transformer semantic segmentation pipeline. We build a pure Transformer detector by combining PVT and Trans2Seg [72]. It is 2.9% higher than ResNet50-d16+Trans2Seg and 1.1% higher than ResNet50-d8+DeeplabV3+ with lower GFlops. “d8” and “d16” means dilation 8 and 16, respectively.

Table 9: Deeper vs. Wider. “Top-1” denotes the top-1 error on the ImageNet validation set. “AP” denotes the bounding box AP on COCO val2017. The deep model (i.e., PVTMedium) obtains better performance than the wide model (i.e., PVT-Small-Wide ) under comparable parameter number. mance (31.7 AP on COCO val2017),3 as shown in Table 8. When using fine-grained image patches (e.g., 4×4 pixels per patch) as input like our PVT, ViT will exhaust the GPU memory (32G). Our method avoids this problem through a progressive shrinking pyramid. Specifically, our model can process high-resolution feature maps in shallow stages and low-resolution feature maps in deep stages. Thus, it obtains a promising AP of 40.4 on COCO val2017, 8.7 points higher than ViT-Small/32 (40.4 vs. 31.7). Deeper vs. Wider. The problem of whether the CNN backbone should go deeper or wider has been extensively discussed in previous work [22, 77]. Here, we explore this 3 For adapting ViT to RetinaNet, we extract the features from the layer 2, 4, 6, and 8 of ViT-Small/32, and interpolate them to different scales.

Method ResNet50+GC r4 [5] PVT-Small (ours)

Method

Table 10: PVT vs. CNN w/ non-local. AP denotes mask AP. Under similar parameter nubmer and GFLOPs, our PVT outperform the CNN backbone w/ Non-Local (ResNet50+GC r4) by 1.6 APm (37.8 vs. 36.2).

problem in our PVT. For fair comparisons, we multiply the hidden dimensions {C1 , C2 , C3 , C4 } of PVT-Small by a scale factor 1.4 to make it have an equivalent parameter number to the deep model (i.e., PVT-Medium). As shown in Table 9, the deep model (i.e., PVT-Medium) consistently works better than the wide model (i.e., PVT-Small-Wide) on both ImageNet and COCO. Therefore, going deeper is more effective than going wider in the design of PVT. Based on this observation, in Table 1, we develop PVT models with different scales by increasing the model depth. Pre-trained Weights. Most dense prediction models (e.g., RetinaNet [39]) rely on the backbone whose weights are pre-trained on ImageNet. We also discuss this problem in our PVT. In the top of Figure 5, we plot the validation AP curves of RetinaNet-PVT-Small w/ (red curves) and w/o (blue curves) pre-trained weights. We find that the model w/ pre-trained weights converges better than the one w/o pre-trained weights, and the gap between their final AP reaches 13.8 under the 1× training schedule and 8.4 under the 3× training schedule and multi-scale training. Therefore, like CNN-based models, pre-training weights can also help PVT-based models converge faster and better. Moreover, in the bottom of Figure 5, we also see that the convergence speed of PVT-based models (red curves) is faster than that of ResNet-based models (green curves). PVT vs. “CNN w/ Non-Local” To obtain a global receptive field, some well-engineered CNN backbones, such as GCNet [5], integrate the non-local block in the CNN framework. Here, we compare the performance of our PVT (pure Transformer) and GCNet (CNN w/ non-local), using Mask R-CNN for instance segmentation. As reported in Table 10, we find that our PVT-Small outperforms ResNet50+GC r4 [5] by 1.6 points in APm (37.8 vs. 36.2), and 2.0 points in APm 75 (38.3 vs. 40.3), under comparable parameter number and GFLOPs. There are two possible reasons for this result: (1) Although a single global attention layer (e.g., nonlocal [70] or multi-head attention (MHA) [64]) can acquire global-receptive-field features, the model performance keeps improving as the model deepens. This indicates that stacking multiple MHAs can further enhance the representation capabilities of features. Therefore, as a pure Transformer backbone with more global attention layers, our PVT tends to perform better than the CNN backbone

Table 11: Latency and AP under different input scales. “Scale” and “Time” denote the input scale and time cost per image. When the shorter side is 640 pixels, the PVTSmall+RetinaNet has a lower GFLOPs and time cost (on a V100 GPU) than ResNet50+RetinaNet, while obtaining 2.4 points better AP (38.7 vs. 36.3).

equipped with non-local blocks (e.g., GCNet). (2) Regular convolutions can be deemed as special instantiations of spatial attention mechanisms [84]. In other words, the format of MHA is more flexible than the regular convolution. For example, for different inputs, the weights of the convolution are fixed, but the attention weights of MHA change dynamically with the input. Thus, the features learned by the pure Transformer backbone full of MHA layers, could be more flexible and expressive. Computation Overhead. With increasing input scale, the growth rate of the GFLOPs of our PVT is greater than ResNet [22], but lower than ViT [13], as shown in Figure 6. However, when the input scale does not exceed 640×640 pixels, the GFLOPs of PVT-Small and ResNet50 are similar. This means that our PVT is more suitable for tasks with medium-resolution input. On COCO, the shorter side of the input image is 800 pixels. Under this condition, the inference speed of RetinaNet based on PVT-Small is slower than the ResNet50based model, as reported in Table 11. (1) A direct solution for this problem is to reduce the input scale. When reducing the shorter side of the input image to 640 pixels, the model based on PVT-Small runs faster than the ResNet50based model (51.7ms vs., 55.9ms), with 2.4 higher AP (38.7 vs. 36.3). 2) Another solution is to develop a selfattention layer with lower computational complexity. This is a worth exploring direction, we recently propose a solution PVTv2 [67]. Detection & Segmentation Results. In Figure 7, we also present some qualitative object detection and instance segmentation results on COCO val2017 [40], and semantic segmentation results on ADE20K [83]. These results indicate that a pure Transformer backbone (i.e., PVT) without convolutions can also be easily plugged in dense prediction models (e.g., RetinaNet [39], Mask R-CNN [21], and Semantic FPN [32]), and obtain high-quality results.
