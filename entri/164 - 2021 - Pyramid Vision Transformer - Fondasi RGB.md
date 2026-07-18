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
