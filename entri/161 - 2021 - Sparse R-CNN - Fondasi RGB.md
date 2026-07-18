# 161 - Sparse R-CNN: End-to-End Object Detection with Learnable Proposals

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2021sparsercnn` |
| Judul asli | Sparse R-CNN: End-to-End Object Detection with Learnable Proposals |
| Penulis | Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng Xu, Wei Zhan, Masayoshi Tomizuka, Lei Li, Zehuan Yuan, Changhu Wang, Ping Luo |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2011.12450
- **Google Scholar:** https://scholar.google.com/scholar?q=Sparse+R-CNN%3A+End-to-End+Object+Detection+with+Learnable+Proposals
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Sparse+R-CNN%3A+End-to-End+Object+Detection+with+Learnable+Proposals&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Sparse R-CNN, sebuah paradigma deteksi objek berbasis metode jarang (*sparse*) murni yang dirancang untuk beroperasi secara ujung-ke-ujung (*end-to-end*) tanpa memerlukan *Non-Maximum Suppression* (NMS) atau ratusan ribu kandidat objek (*anchor boxes*) yang ditentukan secara manual. Detektor objek tradisional umumnya mengandalkan kandidat objek yang sangat padat pada peta fitur gambar untuk memastikan cakupan deteksi yang tinggi. Sebaliknya, Sparse R-CNN mengajukan mekanisme revolusioner berupa sekumpulan kecil proposal kotak (*proposal boxes*) dan fitur proposal (*proposal features*) yang bersifat dapat dipelajari (*learnable*) dan dinamis. 

Evaluasi pada dataset COCO menunjukkan bahwa Sparse R-CNN mencapai kinerja yang setara dengan detektor mapan dalam hal akurasi dan kecepatan inferensi, serta memiliki konvergensi pelatihan yang jauh lebih cepat dibandingkan dengan detektor berbasis *Transformer* global seperti DETR. Dengan menggunakan model dasar ResNet-50 FPN, Sparse R-CNN mampu memperoleh *Average Precision* (AP) sebesar 42,8% pada kecepatan 23 *frame per second* (FPS) menggunakan 100 proposal, dan meningkat hingga 45,0% AP pada kecepatan 22 FPS ketika menggunakan 300 proposal objek. Keberhasilan ini menantang konvensi penggunaan prioritas kandidat padat (*dense prior*) dalam arsitektur deteksi objek.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hingga dipublikasikannya Sparse R-CNN pada tahun 2021, bidang deteksi objek didominasi oleh pendekatan berbasis kandidat padat. Detektor satu tahap seperti RetinaNet (bab 016) dan detektor dua tahap seperti Faster R-CNN (bab 014) menempatkan ratusan ribu *anchor box* dengan berbagai skala dan rasio aspek pada setiap posisi grid spasial gambar. Meskipun efektif untuk mendeteksi berbagai variasi objek, skema ini melahirkan beberapa masalah fundamental. Pertama, penempatan kotak yang sangat padat menciptakan ketidakseimbangan kelas (*class imbalance*) ekstrem antara objek nyata dan latar belakang. Kedua, model membutuhkan mekanisme pencocokan banyak-ke-satu (*many-to-one label assignment*) yang rumit selama pelatihan dan pasca-pemrosesan NMS saat inferensi untuk menyaring prediksi ganda yang tumpang tindih. Pasca-pemrosesan NMS sangat sensitif terhadap nilai ambang batas (*threshold*) persimpangan di atas gabungan (*Intersection over Union* atau IoU) dan menghalangi optimalisasi jaringan secara utuh dari ujung ke ujung.

Sebagai alternatif, model berbasis *attention* (atensi) global seperti DETR (bab 022) memperkenalkan konsep prediksi himpunan langsung tanpa NMS menggunakan *object queries*. Meskipun menawarkan kesederhanaan arsitektural, DETR memiliki kelemahan kritis berupa konvergensi pelatihan yang sangat lambat. Jaringan membutuhkan waktu hingga 500 *epoch* pelatihan untuk mencapai akurasi optimal. Lambatnya konvergensi ini disebabkan oleh absennya prioritas spasial lokal pada arsitektur atensi global penuh, sehingga jaringan harus mempelajari pemetaan geometris objek dari nol pada gambar beresolusi tinggi. Oleh karena itu, terdapat kebutuhan mendesak untuk mengembangkan detektor objek yang mempertahankan kesederhanaan prediksi *end-to-end* tanpa NMS, namun memiliki efisiensi komputasi dan kecepatan konvergensi pelatihan yang setara dengan detektor berbasis wilayah konvensional.

## Ide Utama

Gagasan utama Sparse R-CNN adalah merumuskan ulang konsep wilayah proposal menjadi representasi yang murni jarang dan dapat dioptimalkan secara langsung melalui fungsi kerugian berbasis prediksi himpunan (*set prediction loss*). Model ini sepenuhnya menghilangkan komponen pembangkit proposal padat seperti *Region Proposal Network* (RPN) serta struktur *anchor box* statis. Sebagai gantinya, Sparse R-CNN memelihara sejumlah kecil parameter laten yang dapat dipelajari langsung melalui *gradient descent* (penurunan gradien), yang terdiri atas dua bagian:
1. **Proposal Box ($B \in \mathbb{R}^{N \times 4}$):** Sekumpulan kecil $N$ kotak pembatas (biasanya $N = 100$ atau $300$) yang diwakili oleh koordinat ternormalisasi $[x_c, y_c, w, h]$. Kotak-kotak ini bertindak sebagai estimasi awal lokasi objek di dalam citra.
2. **Proposal Feature ($F \in \mathbb{R}^{N \times C}$):** Vektor fitur laten berdimensi $C$ (secara standar $C = 256$) yang dipasangkan satu-ke-satu dengan setiap proposal box. Fitur ini bertindak sebagai representasi instansi spesifik (*instance-specific representation*) yang mengodekan karakteristik visual objek seperti bentuk, orientasi, dan detail semantik.

Untuk menghubungkan representasi jarang ini dengan fitur citra global, Sparse R-CNN memperkenalkan kepala interaktif instansi dinamis (*Dynamic Instance Interactive Head*). Alih-alih menerapkan lapisan konvolusi statis dengan bobot yang sama untuk seluruh gambar, vektor proposal feature digunakan untuk memproyeksikan parameter filter konvolusi dinamis. Filter dinamis ini kemudian diterapkan secara eksklusif pada fitur wilayah gambar yang diekstrak berdasarkan koordinat proposal box terkait. Dengan demikian, interaksi fitur terjadi secara terfokus pada wilayah potensial, yang tidak hanya menghemat komputasi tetapi juga mempercepat pembelajaran representasi spasial objek.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Multi-Skala dengan Backbone dan FPN

Proses deteksi dimulai dengan melewatkan citra masukan beresolusi tinggi (misalnya, $800 \times 1333$ piksel) ke dalam jaringan tulang punggung (*backbone*) berupa ResNet-50. Output dari berbagai blok konvolusi ResNet diekstrak dan disalurkan ke modul *Feature Pyramid Networks* (FPN) (bab 018). FPN menggabungkan fitur semantik tingkat tinggi dengan fitur resolusi spasial tinggi tingkat rendah secara *top-down* dan koneksi lateral. Proses ini menghasilkan piramida fitur multi-skala yang mencakup tingkat resolusi P2 hingga P5. Piramida fitur ini berfungsi untuk memastikan model dapat menangani variabilitas ukuran objek, mulai dari objek berukuran sangat kecil hingga objek yang mendominasi bidang pandang citra.

### Inisialisasi Proposal yang Dapat Dipelajari

Pada awal pelatihan, parameter proposal box ($B_0$) dan proposal feature ($F_0$) diinisialisasi secara acak atau diletakkan merata untuk mencakup seluruh area citra. Parameter-parameter ini bukan merupakan keluaran dari ekstraksi fitur citra masukan, melainkan bobot jaringan (*network weights*) yang dapat diperbarui secara langsung melalui propagasi balik (*backpropagation*). Selama fase pelatihan, koordinat $B_0$ akan belajar mencari distribusi lokasi objek terbaik di seluruh dataset, sementara $F_0$ belajar mengenali pola fitur universal objek. Saat fase inferensi, nilai awal $B_0$ dan $F_0$ bersifat statis (tetap) dan digunakan sebagai input awal untuk seluruh gambar yang diproses.

### Struktur Iteratif Bertingkat (Cascaded Refinement)

Sparse R-CNN menerapkan penyempurnaan secara bertahap menggunakan arsitektur bertingkat yang terdiri dari $U = 6$ tahapan (*stages*). Pada setiap tahapan $u \in \{1, 2, \dots, U\}$, model menerima proposal box $B_{u-1}$ dan proposal feature $F_{u-1}$ dari tahap sebelumnya, lalu menghasilkan versi penyempurnaan berupa $B_u$ dan $F_u$. Struktur iteratif ini terbukti sangat krusial karena detektor hanya bekerja pada representasi yang sangat jarang, sehingga koreksi posisi dan klasifikasi objek perlu dilakukan secara progresif untuk mencapai akurasi tinggi.

### Mekanisme Dynamic Instance Interactive Head

Untuk setiap tahapan $u$, modul interaktif mengeksekusi langkah-langkah pemrosesan sebagai berikut:

```
[ Peta Fitur FPN ]       [ Proposal Box (N x 4) ]    [ Proposal Feature (N x C) ]
       │                         │                               │
       │                         │                               ▼
       │                         │                     ┌──────────────────┐
       │                         │                     │  Self-Attention  │
       │                         │                     │    (Antar-Obj)   │
       │                         │                     └─────────┬────────┘
       │                         │                               │
       ▼                         ▼                               ▼
 ┌─────────────────────────────────┐                             │
 │            RoIAlign             │                             │
 └───────────────┬─────────────────┘                             │
                 │                                               ▼
                 ▼ (N x 7x7 x C)                        ┌──────────────────┐
        [ Fitur RoI (f_roi) ]                           │ Proyeksi Linier  │
                 │                                      └────────┬─────────┘
                 │                                               │
                 │                                               ▼
                 │       ┌───────────────────────────┐    Bobot Dinamis
                 ├──────►│  Dynamic Convolution (W1) │◄─── W1 (N x C x C)
                 │       └─────────────┬─────────────┘
                 │                     ▼ (ReLU)
                 │       ┌───────────────────────────┐
                 └──────►│  Dynamic Convolution (W2) │◄─── W2 (N x C x C)
                         └─────────────┬─────────────┘
                                       ▼
                             [ Fitur Objek (f_obj) ]
                                       │
                                       ▼
                             ┌───────────────────┐
                             │  Global Pooling   │
                             └─────────┬─────────┘
                                       │
                                       ▼ (N x C)
                               ┌───────┴───────┐
                               ▼               ▼
                       ┌──────────────┐┌──────────────┐
                       │ Klasifikasi  ││   Regresi    │
                       └──────────────┘└───────┬──────┘
                                               ▼
                                         [ Box Baru ] ──► (Tahap Berikutnya)
```

1. **Ekstraksi Fitur Wilayah (*RoIAlign*):** Menggunakan proposal box tahap saat ini $B_{u-1} \in \mathbb{R}^{N \times 4}$, fitur dari piramida FPN diekstrak menggunakan operasi RoIAlign (bab 017). Operasi ini menghindari kesalahan kuantisasi dengan menggunakan interpolasi bilinear untuk memetakan koordinat riil kotak ke grid spasial tetap berukuran $S \times S$ (umumnya $7 \times 7$). Hasilnya adalah tensor fitur RoI $f_{roi} \in \mathbb{R}^{N \times 7 \times 7 \times C}$ di mana $C = 256$.
2. **Korelasi Antar-Objek (*Self-Attention*):** Seluruh proposal feature $F_{u-1} \in \mathbb{R}^{N \times C}$ dimasukkan ke dalam modul *Multi-Head Self-Attention* (MHSA). Langkah ini sangat penting karena memungkinkan setiap proposal objek berinteraksi satu sama lain secara global. Melalui MHSA, model dapat mempelajari relasi spasial dan semantik antar-objek (misalnya, keberadaan objek cangkir di dekat piring) serta mendeteksi duplikasi prediksi. Hal ini secara efektif menggantikan peran pengurang tumpang-tindih pasca-pemrosesan seperti NMS.
3. **Pembangkitan Parameter Dinamis:** Vektor proposal feature ke-$i$, $f_{prop, i} \in \mathbb{R}^{C}$, dilewatkan ke lapisan proyeksi linier terpisah untuk menghasilkan dua buah matriks bobot dinamis: $W_{1, i} \in \mathbb{R}^{C \times C}$ dan $W_{2, i} \in \mathbb{R}^{C \times C}$.
4. **Interaksi Dinamis (*Dynamic Convolution*):** Fitur RoI ke-$i$ ($f_{roi, i} \in \mathbb{R}^{49 \times C}$) dikalikan secara matriks dengan $W_{1, i}$, dilanjutkan dengan aktivasi unit linier terarah (*Rectified Linear Unit* atau ReLU). Hasilnya kemudian dikalikan dengan $W_{2, i}$ untuk menghasilkan fitur objek akhir $f_{obj, i} \in \mathbb{R}^{49 \times C}$. Rumus operasinya adalah:
   $$f'_{roi, i} = \text{ReLU}(f_{roi, i} W_{1, i})$$
   $$f_{obj, i} = f'_{roi, i} W_{2, i}$$
   Melalui mekanisme ini, setiap instansi proposal memiliki filter konvolusi khususnya sendiri yang secara adaptif memilah informasi spasial paling relevan di dalam wilayah RoI tersebut.
5. **Penyusutan Spasial:** Operasi *global average pooling* (pemusatan rata-rata global) diterapkan pada dimensi spasial $7 \times 7$ dari $f_{obj, i}$ untuk mereduksi dimensinya menjadi satu vektor fitur representatif berukuran $1 \times C$.

### Cabang Prediksi dan Pembaruan Parameter

Vektor representatif hasil penyusutan spasial disalurkan ke dua cabang kepala prediksi (*prediction heads*) terpisah yang berupa lapisan terhubung penuh (*fully connected layers*):
- **Cabang Klasifikasi:** Memprediksi probabilitas kelas objek menggunakan fungsi aktivasi *sigmoid*.
- **Cabang Regresi:** Memprediksi nilai penyimpangan (*offset*) kotak $[dx, dy, dw, dh]$ untuk memperbarui koordinat proposal box dari $B_{u-1}$ menjadi koordinat baru $B_u$.

Selain memprediksi kelas dan koordinat kotak, vektor representatif tersebut digunakan untuk memperbarui proposal feature $F_{u-1}$ menjadi $F_u$ menggunakan koneksi residual (*residual connection*) demi menjaga kestabilan aliran gradien selama pelatihan bertingkat.

### Hungarian Bipartite Matching Loss

Untuk melatih model secara *end-to-end*, Sparse R-CNN menggunakan mekanisme pencocokan bipartit Hungarian (*Hungarian bipartite matching*) untuk memetakan $N$ kotak prediksi dengan $M$ kotak objek sebenarnya (*ground truth*) di mana $N \ge M$. Biaya pencocokan (*matching cost*) didefinisikan sebagai fungsi gabungan dari:
1. Probabilitas kelas yang diprediksi (dihitung menggunakan *Focal Loss* untuk mengatasi ketidakseimbangan kelas).
2. Keselarasan koordinat kotak pembatas (dihitung menggunakan kombinasi kerugian L1 absolut dan kerugian *Generalized IoU* atau GIoU).

Algoritme Hungarian mencari permutasi pencocokan satu-ke-satu yang meminimalkan total biaya global tersebut. Setelah pencocokan optimal tercapai, kerugian klasifikasi dan regresi hanya dihitung dan diakumulasikan dari pasangan yang berhasil dicocokkan, sedangkan prediksi yang tidak berpasangan hanya dikenakan penalti klasifikasi latar belakang. Pendekatan ini menjamin model menghasilkan tepat satu kotak deteksi unik untuk setiap objek fisik.

## Eksperimen dan Hasil

Evaluasi kinerja Sparse R-CNN dilakukan pada dataset tolok ukur deteksi objek COCO 2017 menggunakan partisi *validation set* (val). Konfigurasi eksperimen standar menggunakan jadwal pelatihan 36 *epoch* (dikenal sebagai jadwal 3x) dengan teknik augmentasi pemotongan acak (*random crop*).

Berikut adalah rangkuman performa Sparse R-CNN lintas arsitektur tulang punggung (*backbone*) dan jumlah proposal objek pada dataset COCO:

| Jaringan Tulang Punggung (Backbone) | Jumlah Proposal ($N$) | AP (%) | AP50 (%) | AP75 (%) | Kecepatan Inferensi (FPS) |
|---|:---:|:---:|:---:|:---:|:---:|
| ResNet-50 FPN | 100 | 42,8 | 61,2 | 45,7 | 23 |
| ResNet-50 FPN | 300 | 45,0 | 63,4 | 48,2 | 22 |
| ResNet-101 FPN | 100 | 44,1 | 62,1 | 47,2 | 19 |
| ResNet-101 FPN | 300 | 46,4 | 64,6 | 49,5 | 18 |
| ResNeXt-101 FPN | 300 | 46,9 | 66,3 | 51,2 | - |

Interpretasi hasil eksperimen ini menunjukkan beberapa poin penting:
- **Pengaruh Jumlah Proposal ($N$):** Meningkatkan jumlah proposal dari 100 menjadi 300 pada model ResNet-50 FPN meningkatkan AP secara signifikan sebesar 2,2% (dari 42,8% menjadi 45,0%). Penurunan kecepatan inferensi yang terjadi sangat minim, yaitu hanya turun dari 23 FPS menjadi 22 FPS. Hal ini menunjukkan efisiensi tinggi dari struktur pemrosesan jarang (*sparse*) paralel dalam *Dynamic Instance Interactive Head*.
- **Konvergensi Kecepatan Pelatihan:** Dibandingkan dengan DETR (ResNet-50) yang membutuhkan 500 *epoch* pelatihan untuk memperoleh 42,0% AP, Sparse R-CNN dengan konfigurasi setara mampu mencapai 42,8% AP hanya dalam 36 *epoch*. Keberhasilan ini merepresentasikan percepatan konvergensi pelatihan sebesar lebih dari 10 kali lipat, membuktikan efektivitas integrasi prioritas spasial lokal via RoIAlign pada arsitektur prediksi set langsung.
- **Akurasi vs Kecepatan:** Model dasar ResNet-50 (300 proposal) memperoleh AP 45,0%, melampaui detektor dua tahap Faster R-CNN standar (37,0% hingga 40,2% AP tergantung konfigurasi) sekaligus mengeliminasi pasca-pemrosesan NMS, dengan tetap mempertahankan kinerja waktu nyata (*real-time*) di atas 20 FPS pada GPU NVIDIA V100.

## Kelebihan dan Keterbatasan

Sisi Kelebihan:
1. **Arsitektur Ujung-ke-Ujung Bersih:** Sparse R-CNN menawarkan desain detektor yang sangat minimalis dengan membuang modul pembangkit prioritas padat seperti RPN dan pasca-pemrosesan NMS, menyederhanakan siklus *deployment* model ke perangkat keras target.
2. **Konvergensi Pelatihan Sangat Cepat:** Mengatasi masalah utama DETR dengan membatasi atensi global pada wilayah lokal RoI, sehingga model dapat dilatih dengan anggaran komputasi standar (36 *epoch*).
3. **Representasi Instansi Dinamis:** Penggunaan konvolusi dinamis berbasis *proposal features* memungkinkan penyesuaian parameter filter secara unik untuk setiap objek, menghasilkan ekstraksi fitur yang sangat adaptif dan akurat.
4. **Efisiensi Komputasi Tinggi:** Struktur deteksi murni jarang menjamin model hanya memproses sejumlah kecil proposal ($N=100$ atau $300$) sepanjang jaringan, menekan beban memori pada bagian *head* detektor.

Sisi Keterbatasan:
1. **Ketergantungan *Recall* pada Nilai $N$:** Secara konseptual, karena jumlah proposal bersifat tetap ($N$), model ini memiliki keterbatasan *recall* alami jika diaplikasikan pada citra yang memiliki tingkat kepadatan objek sangat ekstrem (misalnya, ribuan objek kecil dalam satu citra satelit atau kerumunan padat) yang melebihi nilai $N$ tersebut.
2. **Kompleksitas Parameter Dinamis:** Secara rekayasa, proses pembangkitan bobot konvolusi dinamis ($W_1$ dan $W_2$) membutuhkan alokasi memori dinamis dan operasi perkalian matriks batch yang intensif selama fase propagasi maju dan balik. Hal ini membuat optimasi pada perangkat keras berdaya rendah (*embedded systems*) lebih menantang dibandingkan konvolusi statis konvensional.

## Kaitan dengan Bab Lain

Peta perkembangan arsitektur deteksi objek menunjukkan bahwa Sparse R-CNN menempati posisi hibrida yang unik:

1. **Warisan Paradigma Wilayah:** Sparse R-CNN mewarisi konsep proposal wilayah dari detektor dua tahap tradisional seperti [R-CNN](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md), [Fast R-CNN](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md), dan [Faster R-CNN](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md). Namun, Sparse R-CNN memperbarui cara proposal ini diperoleh dengan membuang modul heuristik eksternal maupun RPN, menggantinya dengan parameter *learnable proposals* yang dioptimalkan bersama parameter model lainnya.
2. **Ketergantungan Modul Fitur:** Model ini memanfaatkan mekanisme ekstraksi sub-piksel presisi *RoIAlign* yang dikembangkan pada [Mask R-CNN](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md) serta struktur representasi multi-skala dari [Feature Pyramid Networks (FPN)](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20%28FPN%29%20-%20Fondasi%20RGB.md) untuk mendeteksi variasi ukuran objek.
3. **Fungsi Kerugian yang Diadopsi:** Untuk klasifikasi wilayah, Sparse R-CNN memanfaatkan *Focal Loss* dari [RetinaNet (Focal Loss)](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md) guna menangani ketidakseimbangan kelas objek.
4. **Rumusan Prediksi Himpunan:** Formulasi prediksi langsung tanpa NMS diadopsi langsung dari konsep *object queries* dan *Hungarian bipartite matching loss* yang diperkenalkan oleh [DETR](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md).
5. **Pengaruh pada Detektor Modern:** Keberhasilan Sparse R-CNN dalam mempercepat konvergensi query menginspirasi pengembangan varian Transformer deteksi generasi berikutnya seperti [Conditional DETR](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md), [DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md), dan [DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md) yang mengintegrasikan teknik denoising query, serta [RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md) yang mencapai performa waktu nyata penuh.
6. **Integrasi ke Backbone dan Detektor Komprehensif:** Konsep deteksi jarang ini juga memengaruhi desain ekstraksi fitur pada tulang punggung modern seperti [Pyramid Vision Transformer](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md), [ConvNeXt](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md), [Swin Transformer V2](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md), serta pendekatan deteksi kolaboratif seperti [Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

- **Kunci BibTeX:** `sun2021sparsercnn`
- **Ringkasan untuk Sitasi:**
  "Sparse R-CNN memperkenalkan paradigma deteksi objek *end-to-end* murni jarang (*sparse*) dengan menggunakan proposal kotak (*proposal boxes*) dan proposal fitur (*proposal features*) yang dapat dipelajari secara dinamis. Melalui penggunaan kepala interaktif instansi dinamis (*Dynamic Instance Interactive Head*) dan fungsi kerugian pencocokan bipartit Hungarian (*Hungarian bipartite matching loss*), model ini sukses mengeliminasi kebutuhan akan ratusan ribu *anchor box* maupun pasca-pemrosesan NMS. Hasil evaluasi menunjukkan akurasi yang kompetitif pada dataset COCO dengan kecepatan konvergensi pelatihan yang jauh lebih cepat daripada model Transformer global seperti DETR."
- **Catatan Verifikasi:**
  "Angka performa utama sebesar 45,0% AP pada dataset COCO menggunakan backbone ResNet-50 FPN dengan 300 proposal objek dicapai dalam jadwal pelatihan standar 36 *epoch* (3x schedule) dengan kecepatan inferensi 22 FPS pada GPU NVIDIA V100."
