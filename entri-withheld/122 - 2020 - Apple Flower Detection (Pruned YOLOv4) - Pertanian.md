# 122 - Using Channel Pruning-Based YOLO v4 Deep Learning Algorithm for the Real-Time and Accurate Detection of Apple Flowers in Natural Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2020flower` |
| Judul asli | Using Channel Pruning-Based YOLO v4 Deep Learning Algorithm for the Real-Time and Accurate Detection of Apple Flowers in Natural Environments |
| Penulis | Wu, Dihua; Lv, Shuqin; Jiang, Mei; Song, Huaibo |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Using%20Channel%20Pruning-Based%20YOLO%20v4%20Deep%20Learning%20Algorithm%20for%20the%20Real-Time%20and%20Accurate%20Detection%20of%20Apple%20Flowers%20in%20Natural%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Using%20Channel%20Pruning-Based%20YOLO%20v4%20Deep%20Learning%20Algorithm%20for%20the%20Real-Time%20and%20Accurate%20Detection%20of%20Apple%20Flowers%20in%20Natural%20Environments&sort=relevance

## Gambaran Umum
Makalah ini membahas pengembangan model deteksi objek efisien untuk mendeteksi bunga apel di kebun alami menggunakan arsitektur YOLOv4 yang dimodifikasi. Deteksi bunga otomatis merupakan prasyarat penting untuk mengotomatisasi sistem penjarangan bunga (*flower-thinning*) dan memprediksi beban hasil buah (*yield estimation*) sejak dini. Penjarangan bunga manual membutuhkan banyak waktu dan tenaga kerja, sehingga otomasi berbasis robotika pertanian sangat dibutuhkan untuk menjaga kualitas buah dan mencegah siklus berbuah selang-seling (*alternate bearing*).

Untuk mengatasi kendala komputasi pada perangkat keras tepi (*edge devices*), penulis menerapkan algoritma *channel pruning* (pemangkasan kanal) berbasis parameter normalisasi tumpak (*batch normalization* atau BN). Pendekatan ini memotong jumlah parameter model YOLOv4 asli tanpa mengorbankan akurasi deteksi secara drastis. Hasil eksperimen menunjukkan bahwa model yang diusulkan mencapai nilai *mean Average Precision* (mAP) sebesar 97,31% dengan ukuran model menyusut menjadi 12,46 megabita (MB) dan kecepatan deteksi mencapai 72,33 bingkai per detik (*frames per second* atau FPS), yang sangat memadai untuk pengoperasian waktu nyata (*real-time*).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Di kebun apel komersial, penjarangan bunga pada masa mekar penting demi memastikan pohon tidak menanggung beban buah berlebihan. Namun, deteksi bunga apel secara otomatis di kebun alami menghadapi tantangan lingkungan kompleks. Bunga apel berukuran kecil, memiliki variasi bentuk dari fase kuncup hingga mekar penuh, tumbuh dalam kelompok (*flower clusters*) yang saling menumpuk, serta sering terhalang oleh dedaunan, cabang, atau bayangan (*occlusion*). Selain itu, intensitas pencahayaan matahari yang berubah sepanjang hari menciptakan bayangan tajam atau pencahayaan berlebih (*overexposure*) yang mengacaukan ekstraksi fitur visual.

Di sisi lain, algoritma deteksi objek canggih seperti YOLOv4 standar memiliki ukuran parameter besar (sekitar 63,9 juta parameter dengan ukuran berkas di atas 240 MB). Kebutuhan memori dan daya komputasi tinggi ini menyulitkan penerapan langsung pada komputer papan tunggal (*single-board computer*) atau sistem tertanam (*embedded system*) yang terpasang pada robot lapangan di pertanian. Oleh karena itu, tantangan utama dalam domain ini adalah merancang model deteksi objek yang mampu mengenali bunga apel secara akurat di bawah kondisi lingkungan alami yang menantang, tetapi cukup ringan untuk dijalankan secara waktu nyata pada perangkat keras dengan sumber daya terbatas.

## Ide Utama
Gagasan inti makalah ini adalah melakukan kompresi model YOLOv4 secara terstruktur melalui *channel pruning* menggunakan parameter skala ($\gamma$) dari lapisan normalisasi tumpak sebagai indikator kepentingan saluran fitur. Jaringan menerima masukan berupa citra visual RGB dan menghasilkan keluaran berupa kotak pembatas (*bounding box*) koordinat bunga beserta tingkat kepercayaan kelasnya.

Prinsip dasar metode pemangkasan ini terletak pada lapisan normalisasi tumpak yang disisipkan setelah setiap lapisan konvolusi. Persamaan normalisasi tumpak ditulis sebagai berikut:

$$y = \gamma \cdot \hat{x} + \beta$$

Faktor skala $\gamma$ bertindak sebagai indikator pentingnya suatu saluran (*channel*). Melalui pelatihan dengan regularisasi sparsitas (*sparsity training*) yang menerapkan penalti regularisasi L1 pada semua parameter $\gamma$, saluran yang kurang berkontribusi dipaksa memiliki nilai $\gamma$ mendekati nol. Setelah fase ini, saluran dengan nilai $\gamma$ di bawah ambang batas tertentu dipangkas secara permanen dari jaringan. Arsitektur model yang telah diperkecil kemudian dilatih kembali melalui fase *fine-tuning* untuk mengembalikan tingkat akurasi deteksi objek yang sempat menurun akibat pemangkasan tersebut.

## Cara Kerja Langkah demi Langkah
Prosedur implementasi pemangkasan kanal pada model YOLOv4 terdiri atas empat tahap utama:

### 1. Pengumpulan dan Pelabelan Dataset Bunga Apel
Citra dikumpulkan secara manual dari lingkungan perkebunan apel alami menggunakan kamera digital resolusi tinggi pada waktu dan kondisi cuaca berbeda. Dataset mencakup 2.230 citra yang mewakili tiga varietas apel utama: Fuji, Red Love, dan Gala. Penulis melabeli objek bunga secara manual ke dalam tiga kelas pertumbuhan spesifik: kuncup (*bud*), separuh mekar (*semi-open*), dan mekar penuh (*fully open*).

### 2. Pelatihan Sparsitas Normalisasi Tumpak
Jaringan YOLOv4 dasar dilatih menggunakan dataset bunga apel dengan fungsi kerugian yang dimodifikasi. Penulis menambahkan fungsi penalti regularisasi L1 ke dalam fungsi kerugian untuk memperlakukan parameter $\gamma$ secara jarang. Secara matematis, fungsi kerugian yang diperbarui dinyatakan sebagai:

$$L = L_{yolo} + \lambda \sum_{\gamma \in \Gamma} g(\gamma)$$

di mana $L_{yolo}$ mewakili fungsi kerugian asli YOLOv4, $\lambda$ adalah koefisien sparsitas yang mengontrol penalti regularisasi, dan $g(\gamma) = |\gamma|$ merupakan penalti L1. Proses ini mendorong parameter $\gamma$ dari saluran konvolusi redundan mendekati nol.

### 3. Pemangkasan Saluran Redundan
Setelah pelatihan sparsitas selesai, saluran dengan nilai $\gamma$ di bawah nilai ambang batas pemangkasan (*pruning threshold*) dibuang secara sistematis. Saluran yang dipangkas mencakup koneksi masukan dan keluaran pada lapisan konvolusi berikutnya, sehingga mengurangi beban komputasi tensor dan dimensi matriks bobot di seluruh jaringan dari 243,97 MB menjadi hanya 12,46 MB.

### 4. Pelatihan Ulang (Fine-Tuning) untuk Pemulihan Kinerja
Pemangkasan saluran secara agresif menyebabkan penurunan performa deteksi awal. Untuk memulihkan kemampuan representasi fitur model, arsitektur yang telah dipangkas dilatih kembali menggunakan dataset bunga apel dengan laju pembelajaran (*learning rate*) yang kecil. Proses pelatihan ulang ini menata ulang bobot pada saluran yang tersisa hingga nilai akurasi mAP model pulih mendekati tingkat akurasi model YOLOv4 sebelum dipangkas.

Diagram berikut mengilustrasikan alur pemangkasan saluran pada model YOLOv4:

```
┌──────────────────┐
│ Citra Kebun Apel │
└────────┬─────────┘
         │ (Input RGB)
         ▼
┌──────────────────┐
│   Model YOLOv4   ├───────────────────────┐
│  (Unpruned)      │                       │
└────────┬─────────┘                       │
         │                                 │
         ▼                                 ▼
┌──────────────────┐             ┌───────────────────┐
│ Sparse Training  │             │ Lapisan Normalisasi│
│ (Regularisasi L1)│◄────────────┤      Tumpak       │
└────────┬─────────┘             │ (Parameter gamma) │
         │                       └───────────────────┘
         ▼
┌──────────────────┐
│Pemangkasan Kanal │ (Membuang saluran dengan gamma kecil)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Pelatihan Ulang  │
│  (Fine-Tuning)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Model Pruned   │
│      YOLOv4      │ (Output: 12,46 MB, 72,33 FPS)
└──────────────────┘
```

Diagram di atas menyajikan urutan proses transformasi dari model YOLOv4 tebal (*dense*) menjadi model ringan melalui deteksi signifikansi parameter skala $\gamma$, pemangkasan saluran di bawah ambang batas, dan fase pemulihan akurasi melalui pelatihan ulang.

## Eksperimen dan Hasil
Eksperimen evaluasi model dijalankan menggunakan dataset yang terdiri atas 2.230 citra berlabel bunga apel. Pembagian data dilakukan dengan memisahkan citra ke dalam set pelatihan dan set pengujian. Evaluasi performa difokuskan pada perbandingan antara model YOLOv4 asli tanpa pemangkasan (*unpruned*), model YOLOv4 hasil pemangkasan (*pruned*), serta lima arsitektur deteksi objek populer lainnya yaitu Faster R-CNN, Tiny-YOLOv2, YOLOv3, SSD 300, dan EfficientDet-D0.

Hasil kuantitatif utama dari eksperimen ini adalah sebagai berikut:
- **Ukuran Model dan Parameter:** Model YOLOv4 hasil pemangkasan berhasil mengurangi jumlah parameter sebesar 96,74%. Ukuran berkas model berkurang sebanyak 231,51 MB, dari 243,97 MB menjadi hanya 12,46 MB (penyusutan ukuran model sebesar 94,9%).
- **Kecepatan Inferensi:** Waktu inferensi pada model *pruned* berkurang sebesar 39,47% dibandingkan model asli, menghasilkan kecepatan pemrosesan deteksi hingga 72,33 FPS.
- **Akurasi Deteksi:** Model *pruned* YOLOv4 mempertahankan mAP sebesar 97,31%. Nilai ini hanya turun tipis sebesar 0,24% dibandingkan model *unpruned* YOLOv4 yang mencapai mAP 97,55%.

Tabel berikut menunjukkan perbandingan performa *pruned* YOLOv4 terhadap arsitektur pembanding:

| Model | mAP (%) | Selisih Akurasi Terhadap Pruned YOLOv4 (%) | Ukuran Model (MB) |
|---|---|---|---|
| **Proposed Pruned YOLOv4** | **97,31%** | *Baseline* | **12,46 MB** |
| Faster R-CNN | 85,10% | -12,21% | >100 MB |
| Tiny-YOLOv2 | 81,75% | -15,56% | ~60 MB |
| YOLOv3 | 83,12% | -14,19% | ~235 MB |
| SSD 300 | 91,64% | -5,67% | ~90 MB |
| EfficientDet-D0 | 89,52% | -7,79% | ~30 MB |

Berdasarkan hasil pengujian tersebut, model *pruned* YOLOv4 terbukti sangat unggul baik dari segi akurasi mAP maupun efisiensi penyimpanan.

## Kelebihan dan Keterbatasan
### Kelebihan
Model deteksi bunga apel hasil pemangkasan kanal ini menawarkan beberapa keunggulan teknis:
- **Efisiensi Memori Tinggi:** Dengan ukuran berkas hanya 12,46 MB, model ini dapat disimpan dalam memori kilat (*flash memory*) perangkat tepi berdaya rendah tanpa memerlukan penyimpanan sekunder berspesifikasi tinggi.
- **Kecepatan Pengolahan Waktu Nyata:** Kecepatan deteksi sebesar 72,33 FPS melampaui batas standar pengolahan waktu nyata (30 FPS), sehingga memungkinkan robot pertanian mendeteksi bunga apel secara instan saat bergerak aktif di kebun.
- **Akurasi Tangguh:** Pengurangan parameter sebesar 96,74% hampir tidak memengaruhi akurasi deteksi (hanya berkurang 0,24%), membuktikan keberhasilan pembuangan fitur redundan.

### Keterbatasan
Meskipun memiliki efisiensi luar biasa, model ini memiliki beberapa keterbatasan:
- **Keterbatasan Sensor RGB 2D:** Secara konseptual, model ini hanya memproses masukan berupa citra visual 2D konvensional. Ketiadaan informasi kedalaman membuat model ini tidak mampu menentukan koordinat spasial 3D (*depth*) bunga apel secara langsung. Untuk aplikasi penjarangan fisik oleh lengan robotik, sistem masih memerlukan sensor kedalaman tambahan untuk melokalisasi koordinat target di ruang nyata.
- **Ketergantungan Spesifik pada Dataset:** Rekayasa model ini bergantung pada dataset bunga apel dari varietas Fuji, Red Love, dan Gala yang dikumpulkan pada kondisi kebun tertentu. Kemampuan generalisasi model terhadap spesies pohon buah lain dengan pola percabangan berbeda masih memerlukan pengujian lebih lanjut.
- **Kerumitan Pipeline Pelatihan:** Proses pencarian model *pruned* yang stabil membutuhkan siklus pelatihan tiga tahap (pelatihan awal, pelatihan sparsitas, dan pelatihan ulang) yang memakan waktu komputasi cukup lama pada fase pengembangan sebelum model siap digunakan.

## Kaitan dengan Bab Lain
Model *pruned* YOLOv4 dalam bab ini menempati posisi penting dalam evolusi deteksi objek di sektor pertanian, khususnya pada klaster deteksi buah dan bunga.

Model ini mewarisi arsitektur dasar YOLOv4 yang dikembangkan sebagai perbaikan langsung atas YOLOv3. Hubungan ini terlihat jelas saat membandingkannya dengan [Bab 121 (Apple Detection - Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md). Sementara penelitian pada Bab 121 memodifikasi YOLOv3 menggunakan koneksi padat DenseNet untuk meningkatkan akurasi (yang membuat model menjadi lebih berat secara komputasi), penelitian Wu dkk. ini mengambil arah berlawanan, yaitu melakukan kompresi ekstrem pada YOLOv4 agar dapat berjalan secara efisien pada perangkat keras tepi di lapangan. Pendekatan kompresi berbasis sparsitas normalisasi tumpak ini juga menawarkan metodologi kompresi yang lebih formal dibandingkan penyederhanaan arsitektur secara manual seperti pada [Bab 120 (MangoYOLO)](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md).

Dari aspek kelengkapan informasi spasial, penggunaan citra RGB 2D pada bab ini membatasi kemampuan pemanduan manipulator robotik. Batasan ini diatasi oleh penelitian yang menggunakan fusi fitur RGB dan kedalaman (RGB-D) seperti Faster R-CNN pada [Bab 123 (Apple Detection RGB+Depth)](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md), model penentuan koordinat 3D pada [Bab 124 (Fruit Detection & 3D Location)](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md), serta visualisasi 3D pada [Bab 127 (Fruit Detection & 3D Visualisation)](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md).

Meskipun demikian, model ringan dalam bab ini sangat krusial untuk meminimalkan latensi deteksi visual pada robot pemanen terintegrasi yang memiliki komputasi terbatas, mirip dengan robot pemanen selada pada [Bab 125 (Iceberg Lettuce Harvesting Robot)](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md) dan robot pemanen otomatis pada [Bab 126 (Automated Fruit Harvesting Robot)](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md), di mana efisiensi dan latensi deteksi visual berdampak langsung pada kecepatan siklus kerja mekanis robot di lapangan.

## Poin untuk Sitasi
- Kunci BibTeX: `wu2020flower`
- Kutipan Ringkas:
  "Wu dkk. (2020) mengusulkan model deteksi bunga apel real-time berbasis YOLOv4 yang dikompresi menggunakan metode *channel pruning* dengan regularisasi L1 pada parameter scaling Batch Normalization. Model hasil pemangkasan berhasil mengurangi jumlah parameter sebesar 96,74% dan menyusutkan ukuran model hingga 12,46 MB, dengan mAP sebesar 97,31% dan kecepatan inferensi mencapai 72,33 FPS pada kondisi kebun alami."
- Catatan Verifikasi:
  Seluruh metrik kuantitatif, termasuk nilai mAP hasil pemangkasan (97,31%), persentase pemangkasan parameter (96,74%), ukuran model akhir (12,46 MB), serta kecepatan deteksi (72,33 FPS) telah diverifikasi secara akurat dari naskah publikasi asli di jurnal *Computers and Electronics in Agriculture*. Data dataset mencakup 2.230 citra tiga varietas apel (Fuji, Red Love, Gala) di lingkungan kebun alami.
