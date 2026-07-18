# 149 - CBAM: Convolutional Block Attention Module

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `woo2018cbam` |
| Judul Asli | CBAM: Convolutional Block Attention Module |
| Penulis | Woo, Sanghyun; Park, Jongchan; Lee, Joon-Young; Kweon, In So |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Fusi Multimodal |

## Tautan Akses
- **Google Scholar:** https://scholar.google.com/scholar?q=CBAM%3A%20Convolutional%20Block%20Attention%20Module
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=CBAM%3A%20Convolutional%20Block%20Attention%20Module&sort=relevance
- **arXiv PDF:** https://arxiv.org/abs/1807.06521
- **ar5iv HTML:** https://ar5iv.labs.arxiv.org/html/1807.06521

## Gambaran Umum
*Convolutional Block Attention Module* (CBAM) adalah sebuah modul atensi ringan dan modular yang dirancang untuk jaringan saraf konvolusional (*convolutional neural network* atau CNN) tipe umpan maju (*feed-forward*). Modul ini bekerja dengan cara menyempurnakan peta fitur perantara secara adaptif melalui dua sub-modul atensi yang berurutan, yaitu atensi dimensi kanal (*channel attention*) dan atensi dimensi spasial (*spatial attention*). Sebagai modul yang bersifat serbaguna (*plug-and-play*), CBAM dapat diintegrasikan dengan mudah ke dalam arsitektur CNN modern untuk meningkatkan kapasitas representasi fitur dengan beban parameter dan komputasi yang sangat minimal.

Masalah mendasar yang dipecahkan oleh CBAM adalah perlakuan seragam operasi konvolusi konvensional terhadap semua kanal dan lokasi spasial pada peta fitur. CBAM memecah proses tersebut dengan mempelajari bobot atensi secara dinamis: sub-modul kanal menentukan "apa" yang penting secara semantik, sedangkan sub-modul spasial menentukan "di mana" informasi penting tersebut berada pada dimensi spasial. Integrasi CBAM ke berbagai arsitektur dasar konvensional menghasilkan peningkatan akurasi klasifikasi citra secara konsisten pada ImageNet-1K dan deteksi objek pada MS COCO serta PASCAL VOC 2007.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penelitian rekayasa arsitektur CNN untuk klasifikasi citra berskala besar sebagian besar berfokus pada tiga aspek struktural utama, yaitu kedalaman (*depth*), lebar (*width*), dan kardinalitas (*cardinality*). Kedalaman jaringan ditingkatkan melalui koneksi residual seperti pada ResNet untuk memudahkan propagasi gradien. Lebar jaringan diperbesar untuk menangkap fitur bervariasi seperti pada WideResNet. Sementara itu, kardinalitas ditingkatkan menggunakan operasi konvolusi kelompok pada ResNeXt untuk meningkatkan efisiensi parameter.

Meskipun modifikasi struktural ini meningkatkan kinerja, mekanisme perhatian dinamis (*attention*) untuk memilih fitur penting sering terabaikan. Operasi konvolusi standar mengekstrak fitur dengan menggabungkan informasi lintas-saluran dan spasial secara statis. Representasi fitur dapat ditingkatkan jika model secara aktif menekankan fitur relevan dan menekan informasi tidak informatif (*noise*).

Upaya mengintegrasikan mekanisme atensi ke dalam CNN dirintis oleh jaringan Squeeze-and-Excitation (SE-Net). SE-Net memperkenalkan mekanisme atensi kanal untuk merekalibrasi hubungan antarsaluran fitur secara dinamis. Namun, SE-Net hanya menggunakan pooling rata-rata global (*global average pooling*) untuk mengekstrak statistik spasial. Penggunaan pooling rata-rata saja mengabaikan informasi lokal yang menonjol, seperti objek berukuran kecil dengan kontras tinggi yang lebih cocok ditangkap melalui pooling maksimum (*max pooling*). Selain itu, SE-Net mengabaikan dimensi spasial sepenuhnya, padahal penentuan posisi spasial objek (*where* to focus) sangat penting untuk tugas lokalisasi seperti deteksi objek dan segmentasi citra. Masalah lokalisasi ini semakin krusial pada skenario fusi multimodal, di mana fitur-fitur dari sensor spasial yang berbeda harus diselaraskan secara spasial dan semantik agar tidak menimbulkan distorsi.

## Ide Utama
Gagasan inti dari CBAM adalah melakukan rekalibrasi fitur secara adaptif melalui kombinasi terpisah antara atensi kanal dan atensi spasial yang diterapkan secara berurutan. Alih-alih menghitung peta atensi 3D secara langsung yang membutuhkan biaya komputasi besar, CBAM memecah proses tersebut menjadi dua tahap 1D dan 2D yang efisien.

Secara mekanis, input bagi modul CBAM adalah peta fitur perantara $\mathbf{F} \in \mathbb{R}^{C \times H \times W}$, di mana $C$ mewakili jumlah kanal, sedangkan $H$ dan $W$ mewakili tinggi dan lebar spasial peta fitur. Alur pemrosesan data pada CBAM didefinisikan secara formal melalui dua persamaan berurutan berikut:

$$\mathbf{F}' = \mathbf{M}_c(\mathbf{F}) \otimes \mathbf{F}$$
$$\mathbf{F}'' = \mathbf{M}_s(\mathbf{F}') \otimes \mathbf{F}'$$

Di sini, $\mathbf{M}_c(\mathbf{F}) \in \mathbb{R}^{C \times 1 \times 1}$ adalah peta atensi kanal 1D, $\mathbf{M}_s(\mathbf{F}') \in \mathbb{R}^{1 \times H \times W}$ adalah peta atensi spasial 2D, dan $\otimes$ melambangkan perkalian elemen demi elemen (*element-wise multiplication*). Selama perkalian berlangsung, nilai-nilai atensi disiarkan (*broadcasted*) sepanjang sumbu yang sesuai. Melalui mekanisme ini, input awal $\mathbf{F}$ pertama-tama difilter untuk menentukan saluran informasi mana yang penting (menghasilkan $\mathbf{F}'$), kemudian $\mathbf{F}'$ difilter kembali untuk menentukan koordinat spasial mana yang paling relevan (menghasilkan output akhir $\mathbf{F}''$).

## Cara Kerja Langkah demi Langkah
Penjelasan operasional dari masing-masing sub-modul di dalam CBAM dijabarkan secara rinci sebagai berikut.

### Sub-modul Atensi Kanal (Channel Attention Module)
Sub-modul atensi kanal mengeksploitasi hubungan antarsaluran untuk mengidentifikasi jenis fitur "apa" yang relevan. Alur penghitungan atensi kanal dirinci sebagai berikut:

1. **Agregasi Fitur Spasial**: Peta fitur input $\mathbf{F}$ diperkecil dimensi spasialnya menggunakan dua operasi pooling secara bersamaan:
   - *Average pooling* spasial menghasilkan deskriptor rata-rata $\mathbf{F}^c_{avg} \in \mathbb{R}^{C \times 1 \times 1}$.
   - *Max pooling* spasial menghasilkan deskriptor maksimum $\mathbf{F}^c_{max} \in \mathbb{R}^{C \times 1 \times 1}$.
2. **Pemrosesan MLP Bersama**: Kedua deskriptor spasial ($\mathbf{F}^c_{avg}$ dan $\mathbf{F}^c_{max}$) dimasukkan ke dalam jaringan MLP yang sama (*shared network*). MLP ini menggunakan fungsi aktivasi *Rectified Linear Unit* (ReLU) dengan rasio reduksi saluran $r=16$ untuk menghemat parameter, sehingga dimensi lapisan tersembunyi menjadi $\mathbb{R}^{C/r \times 1 \times 1}$. Bobot proyeksi pertama $\mathbf{W}_0 \in \mathbb{R}^{C/r \times C}$ dan bobot proyeksi kedua $\mathbf{W}_1 \in \mathbb{R}^{C \times C/r}$ digunakan bersama-sama untuk memproses kedua deskriptor tersebut.
3. **Penggabungan dan Aktivasi**: Output dari MLP bersama untuk kedua deskriptor dijumlahkan secara elemen demi elemen, kemudian dilewatkan ke fungsi aktivasi sigmoid ($\sigma$) untuk menormalisasi nilai bobot ke rentang $[0, 1]$. Secara matematis, penghitungan ini ditulis sebagai:
   $$\mathbf{M}_c(\mathbf{F}) = \sigma(\mathbf{W}_1(\text{ReLU}(\mathbf{W}_0(\mathbf{F}^c_{avg}))) + \mathbf{W}_1(\text{ReLU}(\mathbf{W}_0(\mathbf{F}^c_{max}))))$$
4. **Rekalibrasi Kanal**: Bobot atensi $\mathbf{M}_c(\mathbf{F})$ dikalikan secara elemen demi elemen dengan peta fitur input $\mathbf{F}$ untuk menghasilkan fitur terkalibrasi saluran $\mathbf{F}'$.

### Sub-modul Atensi Spasial (Spatial Attention Module)
Sub-modul atensi spasial menentukan lokasi penting ("di mana") fitur harus difokuskan secara komplementer. Alur penghitungannya adalah sebagai berikut:

1. **Agregasi Lintas-Kanal**: Peta fitur yang telah terkalibrasi kanal $\mathbf{F}'$ diperkecil dimensinya sepanjang sumbu kanal $C$ menggunakan dua operasi pooling lintas-saluran:
   - *Average pooling* lintas-saluran menghasilkan peta deskriptor $\mathbf{F}^s_{avg} \in \mathbb{R}^{1 \times H \times W}$.
   - *Max pooling* lintas-saluran menghasilkan peta deskriptor $\mathbf{F}^s_{max} \in \mathbb{R}^{1 \times H \times W}$.
2. **Penggabungan Deskriptor**: Kedua peta deskriptor 2D tersebut digabungkan sepanjang sumbu kanal untuk membentuk tensor gabungan $\mathbf{F}^s_{cat} \in \mathbb{R}^{2 \times H \times W}$.
3. **Operasi Konvolusi**: Tensor gabungan didekatkan dengan lapisan konvolusi standar menggunakan filter berukuran besar, yaitu $7 \times 7$ (dinotasikan sebagai $f^{7\times7}$). Kernel besar $7 \times 7$ dipilih karena memiliki bidang pandang (*receptive field*) yang lebih luas untuk menangkap pola spasial global dibanding kernel $3 \times 3$.
4. **Aktivasi Sigmoid**: Output dari operasi konvolusi dilewatkan ke fungsi aktivasi sigmoid ($\sigma$) untuk menghasilkan peta atensi spasial 2D $\mathbf{M}_s(\mathbf{F}') \in \mathbb{R}^{1 \times H \times W}$. Secara matematis, persamaannya adalah:
   $$\mathbf{M}_s(\mathbf{F}') = \sigma(f^{7\times7}([\mathbf{F}^s_{avg}; \mathbf{F}^s_{max}]))$$
   Di sini, $[\mathbf{F}^s_{avg}; \mathbf{F}^s_{max}]$ mewakili operasi penggabungan sepanjang dimensi kanal.
5. **Rekalibrasi Spasial**: Peta atensi spasial $\mathbf{M}_s(\mathbf{F}')$ dikalikan secara elemen demi elemen dengan $\mathbf{F}'$ untuk menghasilkan peta fitur akhir $\mathbf{F}''$.

### Susunan dan Integrasi Modul
Kedua sub-modul disusun secara sekuensial dengan urutan kanal terlebih dahulu diikuti spasial. Susunan sekuensial ini lebih efektif dibanding paralel karena output atensi kanal dapat langsung memurnikan peta fitur sebelum atensi spasial diterapkan.

Berikut adalah diagram alir pemrosesan fitur di dalam CBAM:

```
           ┌──────────────────────────────────────────────┐
           │                                              │ (Skip Connection)
           ▼                                              │
Input F ───┬──► [ Channel Attention (Mc) ] ──► ⊗ ──► F' ──┴──► [ Spatial Attention (Ms) ] ──► ⊗ ──► Output F''
                 - AvgPool & MaxPool                            - AvgPool & MaxPool
                 - Shared MLP (W0, W1)                          - Conv 7x7
                 - Sum & Sigmoid                                - Sigmoid
```

Secara praktis, modul CBAM dapat disisipkan ke dalam arsitektur CNN modern seperti ResNet. Diagram di bawah ini menunjukkan integrasi CBAM di dalam satu blok residual ResNet (*ResBlock*):

```
                        ┌─────────────────────────┐
                        │                         │
                        ▼                         │
Input x ──► [ Conv 1x1 ] ──► [ Conv 3x3 ] ──► [ Conv 1x1 ] ──► [ CBAM Module ] ──► ⊕ ──► Output
```

Pada blok residual ResNet, CBAM ditempatkan setelah operasi konvolusi terakhir di dalam cabang utama dan tepat sebelum operasi penjumlahan elemen demi elemen dengan jalur pintas (*skip connection*).

## Eksperimen dan Hasil
Penulis melakukan evaluasi kinerja CBAM pada tiga tugas standar visi komputer, yaitu klasifikasi citra pada ImageNet-1K, deteksi objek pada MS COCO, dan deteksi objek pada PASCAL VOC 2007.

Pada ImageNet-1K, integrasi CBAM ke dalam arsitektur ResNet-50 menurunkan tingkat kesalahan *top-1 error* secara signifikan dari 24,56% (pada model baseline) menjadi 22,66%. Sebagai perbandingan, model yang menggunakan SE-Net hanya mencapai *top-1 error* sebesar 23,14%. Peningkatan performa ini dicapai dengan penambahan parameter yang sangat kecil, di mana jumlah parameter ResNet-50 + CBAM adalah 28,09 juta parameter dibandingkan dengan 25,56 juta parameter pada model baseline, dan kebutuhan komputasi hanya meningkat dari 3,858 GFLOPs menjadi 3,864 GFLOPs. Pada arsitektur yang lebih dalam seperti ResNet-101, penggunaan CBAM memangkas *top-1 error* dari 23,38% menjadi 21,51%, mengungguli varian SE-Net yang mencatat *top-1 error* sebesar 22,35%. Untuk model MobileNet, integrasi CBAM berhasil menurunkan *top-1 error* dari 31,39% menjadi 29,01%, yang membuktikan efektivitas CBAM pada arsitektur ringan.

Untuk tugas deteksi objek pada dataset MS COCO, CBAM dievaluasi menggunakan detektor Faster R-CNN. Hasil eksperimen menunjukkan peningkatan performa lokalisasi dan klasifikasi objek yang konsisten:
- Penggunaan tulang punggung (*backbone*) ResNet-50 dengan CBAM menghasilkan *mean Average Precision* (mAP) sebesar 28,1% mAP@[0,5, 0,95], meningkat 1,1% dibandingkan dengan model baseline Faster R-CNN ResNet-50 yang mencatat 27,0% mAP.
- Penggunaan tulang punggung ResNet-101 dengan CBAM meningkatkan mAP dari 29,1% pada baseline menjadi 30,8% (peningkatan sebesar 1,7%).

Pada dataset PASCAL VOC 2007, CBAM diuji pada detektor satu tahap (*one-shot detector*) StairNet. Hasil pengujian menunjukkan bahwa:
- Detektor StairNet dengan tulang punggung VGG16 yang diperkuat CBAM mencapai 79,3% mAP@0,5, melampaui baseline StairNet (78,9% mAP), model StairNet + SE (79,1% mAP), serta detektor SSD standar (77,8% mAP).
- Detektor StairNet dengan tulang punggung MobileNet mencapai 70,5% mAP@0,5 dengan tambahan CBAM, menunjukkan peningkatan dari baseline MobileNet StairNet yang sebesar 70,1% mAP.

## Kelebihan dan Keterbatasan
Kelebihan utama dari CBAM terletak pada sifatnya yang sangat ringan dan modular (*plug-and-play*). Modul ini dapat diintegrasikan ke arsitektur CNN dan dilatih secara ujung-ke-ujung (*end-to-end*). Visualisasi kualitatif dengan Grad-CAM menunjukkan model dengan CBAM memiliki area fokus yang lebih bersih dan terpusat tepat pada objek target dibandingkan baseline atau SE-Net. Hal ini membuktikan efektivitas kombinasi atensi kanal-spasial dalam menekan derau latar belakang (*background noise*).

Namun, secara konseptual, CBAM memiliki keterbatasan inheren. Modul atensi spasial pada CBAM menggunakan operasi konvolusi lokal (dengan ukuran filter $7 \times 7$) untuk menghasilkan bobot spasial. Pendekatan konvolusi lokal ini membuat CBAM kurang mampu menangkap korelasi spasial jarak jauh (*long-range dependencies*) secara global di seluruh wilayah citra, tidak seperti arsitektur berbasis Transformer yang memanfaatkan mekanisme *self-attention* untuk menghubungkan semua piksel secara global tanpa dibatasi ukuran kernel. Dari sisi rekayasa perangkat keras, penambahan operasi pooling maksimum dan rata-rata secara berurutan serta pencabangan MLP bersama dapat menambah latensi waktu inferensi (*inference latency*) yang cukup terasa saat dijalankan pada perangkat keras edge dengan kemampuan pemrosesan paralel yang rendah, meskipun penambahan FLOPs secara teoritis sangat kecil.

## Kaitan dengan Bab Lain
CBAM memiliki hubungan silsilah erat dengan arsitektur residual pada ResNet ([147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)), di mana modul ini disisipkan di dalam blok bottleneck residual. Dibandingkan arsitektur 3D seperti PointNet ([148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)) yang memproses titik tak terstruktur dengan pooling maksimum untuk invariansi permutasi, CBAM menerapkan pooling maksimum dan rata-rata secara terstruktur pada kisi citra 2D.

Dalam konteks fusi multimodal, peran CBAM sangat signifikan. Sebagaimana dijelaskan dalam survei deteksi dan segmentasi multimodal oleh Feng dkk. ([150 - 2021 - Survei Deteksi %26 Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal.md](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)) serta survei perkembangan 20 tahun deteksi objek oleh Zou dkk. ([151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal.md](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)), mekanisme atensi dua tahap seperti yang dirintis oleh CBAM sering diadopsi untuk menyelaraskan modalitas citra RGB dan data kedalaman (Depth). Mekanisme ini membantu mengatasi ketidaksejajaran spasial (*spatial misalignment*) antar-sensor. Hubungan teoritis mengenai bagaimana fitur-fitur dari berbagai modalitas dapat saling memberikan tuntunan dibahas dalam tinjauan pembelajaran multimodal oleh Ramachandram & Taylor ([152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram %26 Taylor) - Fusi Multimodal.md](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)).

Lebih lanjut, penerapan praktis dari atensi spasial-kanal ala CBAM menjadi standar dalam arsitektur deteksi objek menonjol (*Salient Object Detection* atau SOD) berbasis RGB-D yang disurvei oleh Zhou dkk. ([153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal.md](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)). Modul atensi ini memurnikan peta fitur kedalaman yang berasal dari sensor-sensor sebelum digabungkan dengan peta fitur RGB yang bersumber dari dataset multimodal seperti yang diulas oleh Lopes dkk. ([154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal.md](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)).

## Poin untuk Sitasi
Kunci BibTeX: `woo2018cbam`

Kutipan Tinjauan Pustaka:
"Woo dkk. (2018) memperkenalkan Convolutional Block Attention Module (CBAM) sebagai modul atensi ringan yang menyempurnakan representasi fitur CNN sepanjang dimensi kanal dan spasial secara berurutan. Integrasi CBAM pada arsitektur dasar seperti ResNet dan MobileNet terbukti secara empiris meningkatkan kinerja klasifikasi pada ImageNet-1K dan kinerja deteksi objek pada MS COCO serta PASCAL VOC dengan overhead parameter dan FLOPs yang sangat minimal."

Catatan Verifikasi:
"Seluruh data eksperimental dan formula matematis dalam bab ini telah diverifikasi secara silang dengan naskah asli publikasi konferensi ECCV 2018. Angka-angka penting seperti penurunan *top-1 error* ResNet-50 menjadi 22,66% serta peningkatan mAP Faster R-CNN ResNet-50 menjadi 28,1% pada MS COCO terbukti akurat."
