# 138 - Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2019remotesensing` |
| Judul asli | Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection |
| Penulis | Zhang, Yuanlin; Yuan, Yuan; Feng, Yachuang; Lu, Xiaoqiang |
| Tahun | 2019 |
| Venue | IEEE Transactions on Geoscience and Remote Sensing |
| Tema | Remote Sensing |

## Tautan Akses
- Cari / unduh via Google Scholar: https://scholar.google.com/scholar?q=Hierarchical%20and%20Robust%20Convolutional%20Neural%20Network%20for%20Very%20High-Resolution%20Remote%20Sensing%20Object%20Detection
- Semantic Scholar (metrik sitasi & PDF): https://www.semanticscholar.org/search?q=Hierarchical%20and%20Robust%20Convolutional%20Neural%20Network%20for%20Very%20High-Resolution%20Remote%20Sensing%20Object%20Detection&sort=relevance
- DOI: https://doi.org/10.1109/TGRS.2019.2900302

## Gambaran Umum
Makalah ini mengusulkan kerangka deteksi objek berbasis jaringan saraf tiruan konvolusional yang hierarkis dan kokoh (*Hierarchical and Robust Convolutional Neural Network* / HRCNN) untuk citra penginderaan jauh (*remote sensing*) dengan resolusi sangat tinggi (*Very High-Resolution* / VHR). Penginderaan jauh adalah ilmu untuk memperoleh informasi objek tanpa kontak fisik langsung, umumnya menggunakan sensor pada satelit atau pesawat udara. Permasalahan utama dalam deteksi objek citra VHR adalah variasi skala objek yang lebar, orientasi acak di segala arah, serta kompleksitas latar belakang geografis yang tinggi.

Model HRCNN mengekstrak fitur konvolusi multiskala guna merepresentasikan informasi semantik spasial secara hierarkis. Selain itu, model ini menumpuk (*stacking*) representasi fitur dari beberapa lapisan terhubung penuh (*fully connected layer* / FC) untuk memperkuat ketahanan klasifikasi terhadap distorsi rotasi dan perubahan skala. Penulis juga memperkenalkan dataset benchmark baru bernama *High-Resolution Remote Sensing Detection* (HRRSD) yang dirancang seimbang secara jumlah objek per kategori guna mencegah bias kelas.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi objek pada citra penginderaan jauh resolusi sangat tinggi (VHR) merupakan tugas penting dalam analisis data geospasial. Sebelum makalah ini terbit pada 2019, detektor objek standar seperti *Faster R-CNN* (detektor dua-tahap berbasis usulan wilayah) dan *Single Shot MultiBox Detector* (SSD, detektor satu-tahap tanpa usulan wilayah) langsung diadaptasi dari domain citra sehari-hari. Namun, detektor umum tersebut mengalami penurunan performa signifikan karena tiga karakteristik citra udara:
1. **Variasi Skala Ekstrem:** Objek sejenis memiliki dimensi piksel berbeda akibat perbedaan resolusi sensor atau ukuran fisik (misal perahu kecil vs kapal kargo besar). Detektor standar gagal mendeteksi objek multiskala secara simultan tanpa pemrosesan citra berlapis yang memakan biaya komputasi tinggi.
2. **Orientasi Acak:** Karena citra diambil dari sudut tegak lurus (*nadir view*), objek dapat menghadap ke segala arah (0-360 derajat). Jaringan saraf konvolusional (*Convolutional Neural Network* / CNN) standar memiliki keterbatasan dalam invariansi rotasi (*rotation invariance*), yaitu ketahanan fitur terhadap perubahan sudut objek.
3. **Latar Belakang Rumit (*Cluttered Background*):** Objek target dikelilingi oleh elemen bumi bertekstur mirip (pepohonan, jalan, bayangan gedung), memicu tingginya kesalahan deteksi positif palsu (*false positive*).

Pendekatan terdahulu menangani variasi orientasi lewat augmentasi data putaran citra acak saat latihan, yang memperlambat konvergensi model tanpa menjamin kekebalan fitur abstrak terhadap rotasi spasial.

## Ide Utama
Gagasan inti model HRCNN terletak pada dua modifikasi struktural berikut:
1. **Representasi Fitur Spasial Hierarkis:** Model mengekstrak fitur secara multiskala menggunakan *Feature Pyramid Network* (FPN). FPN membangun piramida fitur tingkat tinggi dengan resolusi spasial bervariasi lewat jalur atas-bawah (*top-down pathway*) dan koneksi lateral. Dengan demikian, objek kecil dideteksi pada peta fitur beresolusi spasial tinggi (lapisan bawah), sedangkan objek besar dideteksi pada peta fitur beresolusi rendah yang kaya semantik (lapisan atas).
2. **Kepala Prediksi Robust dengan Stacked FC Layers:** Untuk mengatasi sensitivitas orientasi, model menumpuk (*concatenate*) fitur dari dua lapisan terhubung penuh berturutan, yaitu lapisan `fc6` (spasial lokal) dan `fc7` (semantik global). Penumpukan ini menghasilkan representasi fitur terpadu yang memadukan detail geometris lokal dengan identitas semantik global untuk memperkuat ketahanan prediksi terhadap perubahan orientasi objek.

## Cara Kerja Langkah demi Langkah
Alur kerja sistem deteksi objek HRCNN dibagi menjadi empat tahapan utama:

### 1. Ekstraksi Fitur Multiskala Hierarkis
Citra masukan dilewatkan ke tulang punggung (*backbone*) ResNet-50 untuk menghasilkan peta fitur dari berbagai blok konvolusi (C2, C3, C4, C5). FPN kemudian menggabungkan peta fitur ini secara lateral dan melalui jalur atas-bawah dengan operasi interpolasi naik (*upsampling*). Hasilnya adalah empat tingkat peta fitur piramida (P2, P3, P4, P5) yang merepresentasikan objek pada skala berbeda secara hierarkis.

### 2. Pembuatan Usulan Wilayah (*Region Proposals*)
Peta fitur P2-P5 dialirkan ke Jaringan Usulan Wilayah (*Region Proposal Network* / RPN). RPN memproyeksikan kotak acuan (*anchors*) dengan berbagai aspek rasio pada setiap piksel peta fitur secara paralel guna mendeteksi keberadaan objek potensial. Kotak usulan (*region proposals*) dengan nilai probabilitas tertinggi dipilih untuk tahap berikutnya.

### 3. Penyatuan Wilayah Tertarik (*RoI Pooling / RoIAlign*)
Kotak usulan yang bervariasi dimensinya diubah menjadi dimensi seragam menggunakan operasi penyatuan wilayah tertarik (*Region of Interest Pooling* / *RoI Pooling*). *Region of Interest* (RoI) adalah wilayah persegi panjang yang diusulkan oleh RPN pada peta fitur. Operasi *RoI Pooling* membagi wilayah tersebut menjadi sub-grid berukuran tetap (misal 7×7) dan mengambil nilai maksimum dari tiap sub-grid, menghasilkan peta fitur berukuran 7×7×Saluran.

### 4. Klasifikasi dan Regresi dengan Stacked FC Layers
Peta fitur hasil *RoI Pooling* diratakan (*flattened*) dan dimasukkan ke lapisan terhubung penuh pertama (`fc6`) untuk menghasilkan vektor berdimensi 4096, lalu diteruskan ke lapisan terhubung penuh kedua (`fc7`) untuk menghasilkan vektor berdimensi 4096 lainnya. Fitur dari `fc6` dan `fc7` ditumpuk secara sejajar (*channel-wise concatenation*) menjadi vektor berdimensi 8192. Vektor terpadu ini dimasukkan ke lapisan klasifikasi akhir (memakai fungsi *softmax*) dan lapisan regresi kotak pembatas (*bounding box regression*) untuk memprediksi koordinat objek.

Diagram berikut menggambarkan alur data dan mekanisme penumpukan fitur pada kepala prediksi HRCNN:

```
[ Citra VHR Masukan ]
          │
          ▼
┌───────────────────┐
│     Backbone      │ (ResNet-50 / VGG-16)
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Fitur Piramida   │ (P2, P3, P4, P5 - Fitur Hierarkis)
└────┬──────────┬───┘
     │          │
     │          ▼
     │   ┌─────────────┐
     │   │     RPN     │ ──► [ Usulan Wilayah (Proposals) ]
     │   └─────────────┘                 │
     ▼                                   │
┌────────────────────────────────────────▼┐
│            Penyatuan RoI                │ (RoI Pooling / RoIAlign)
└────────────────────┬────────────────────┘
                     │ Fitur Wilayah (7x7 x Saluran)
                     ▼
            ┌────────────────┐
            │   FC Layer 6   │ ──┐
            └────────┬───────┘   │
                     │           ▼
                     │       ┌────────────────────────┐
                     ▼       │    Penumpukan Fitur    │ (Feature Stacking /
            ┌────────────────│   (Concatenation)      │  Concatenation)
            │   FC Layer 7   │ ──►  [fc6 + fc7]       │
            └────────────────┘       └──────┬─────────┘
                                            │
                                            ├──────────────────────┐
                                            ▼                      ▼
                                     ┌─────────────┐        ┌─────────────┐
                                     │ Klasifikasi │        │   Regresi   │
                                     │    Objek    │        │  Kotak Bbox │
                                     └─────────────┘        └─────────────┘
```

Lapisan `fc6` mempertahankan sensitivitas terhadap karakteristik geometris lokal objek (seperti orientasi tepi). Lapisan `fc7` mengodekan identitas semantik kelas objek secara global. Penggabungan kedua lapisan menghasilkan representasi terpadu yang memadukan detail geometris lokal dengan identitas semantik global untuk memperkuat akurasi deteksi terhadap rotasi objek.

## Eksperimen dan Hasil
Evaluasi komparatif dilakukan pada dua dataset utama:

### 1. Dataset HRRSD
Dataset ini diperkenalkan oleh penulis untuk mengatasi ketidakseimbangan kelas (*class imbalance*):
- **Jumlah Data:** Terdiri dari 21.761 citra udara beresolusi tinggi dari Google Earth dan Baidu Map.
- **Kategori Objek:** Mencakup 55.740 objek yang terbagi merata ke dalam 13 kategori (pesawat, kapal, jembatan, tangki penyimpanan, kendaraan, lapangan atletik, pelabuhan, persimpangan jalan, lapangan tenis, lapangan basket, lapangan sepak bola, persimpangan T, dan bundaran).
- **Pembagian:** Terbagi menjadi 5.401 citra latih, 5.417 citra validasi, dan 10.943 citra uji.

### 2. Dataset NWPU VHR-10
Berisi 800 citra VHR dengan 10 kelas objek (pesawat, kapal, tangki penyimpanan, lapangan baseball, lapangan tenis, lapangan basket, lapangan atletik, mercusuar, pelabuhan, dan kendaraan) untuk menguji generalisasi eksternal.

### Hasil Kuantitatif Utama
Metrik evaluasi yang digunakan adalah presisi rata-rata mean (*mean Average Precision* / mAP). mAP mengukur rata-rata presisi dari seluruh kelas objek pada ambang batas irisan atas gabungan (*Intersection over Union* / IoU) sebesar 0,5. IoU mengukur tingkat tumpang tindih antara kotak pembatas prediksi dengan kotak pembatas acuan (*ground truth*).

Pada NWPU VHR-10, model HRCNN dengan backbone ResNet-50 mencapai performa mAP kompetitif:
- **HRCNN (ResNet-50):** Mencapai mAP sekitar **80,2%** hingga **90,0%** (bergantung konfigurasi).
- **Faster R-CNN Standar (tanpa FPN):** Mencapai mAP sekitar **76,5%**.
- **SSD Standar:** Mencapai mAP sekitar **71,2%**.

Eksperimen ablasi (*ablation study*) — uji coba mematikan komponen tertentu untuk menganalisis kontribusinya — membuktikan bahwa integrasi piramida fitur hierarkis meningkatkan performa deteksi sebesar **3,4%** mAP. Penggunaan kepala prediksi robust dengan penumpukan fitur `fc6 + fc7` memberikan peningkatan tambahan sebesar **1,5%** mAP, terutama menaikkan nilai AP pada objek yang rentan terhadap rotasi seperti kapal (*ship*) dan pesawat (*airplane*).

## Kelebihan dan Keterbatasan

### Kelebihan
- **Dataset HRRSD Seimbang:** Penyediaan dataset berskala besar dengan kelas objek yang seimbang membantu mengurangi masalah bias model terhadap kelas mayoritas selama proses pelatihan.
- **Invariansi Rotasi yang Efisien:** Penumpukan fitur FC (`fc6` dan `fc7`) meningkatkan akurasi objek yang berputar tanpa memerlukan pemutar citra atau struktur berorientasi sudut yang menambah beban komputasi.
- **Deteksi Multiskala yang Kuat:** Integrasi FPN dengan pembagian skala usulan wilayah meminimalkan masalah hilangnya deteksi pada objek kecil.

### Keterbatasan
- **Efisiensi Komputasi Rendah:** Dari sisi rekayasa, paradigma dua-tahap (Faster R-CNN) memerlukan waktu inferensi lebih lambat dan memori GPU besar, sehingga kurang cocok untuk aplikasi *real-time* atau perangkat keras terbatas (*edge devices*).
- **Batasan Kotak Pembatas Horizontal (*Horizontal Bounding Box* / HBB):** Secara konseptual, model hanya memprediksi HBB. Ini kurang optimal untuk objek padat dengan orientasi miring (seperti kapal di pelabuhan), karena kotak pembatas yang lebar memicu penekanan non-maksimum (*Non-Maximum Suppression* / NMS) yang keliru mengeliminasi deteksi valid.
- **Ketergantungan Citra RGB:** Model hanya memakai data RGB, tidak memanfaatkan informasi multispektral atau data kedalaman (RGB-D) yang berguna untuk memisahkan objek dari bayangan.

## Kaitan dengan Bab Lain
Model HRCNN (2019) menempati posisi historis penting dalam evolusi deteksi objek penginderaan jauh:
- **Kaitan dengan [Bab 140](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md) (YOLT):** YOLT (2018) memecahkan masalah citra satelit area luas menggunakan pemecahan ubin citra (*tiling*) dengan detektor satu-tahap cepat. Sebaliknya, HRCNN mengorbankan kecepatan demi akurasi melalui arsitektur dua-tahap untuk meningkatkan ketahanan klasifikasi terhadap variasi rotasi dan skala di dalam ubin citra.
- **Kaitan dengan [Bab 137](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md) (TPH-YOLOv5) & [Bab 139](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md) (UAV-YOLOv8):** Dataset HRRSD yang diperkenalkan HRCNN sering digunakan sebagai benchmark bagi model satu-tahap modern. TPH-YOLOv5 (2021) dan UAV-YOLOv8 (2023) mengatasi masalah kecepatan inferensi HRCNN menggunakan arsitektur satu-tahap (YOLO) yang ditambahkan kepala prediksi resolusi tinggi dan mekanisme perhatian (*attention*) untuk mendeteksi objek ultra-kecil secara *real-time*.

## Poin untuk Sitasi
### Kunci BibTeX
`zhang2019remotesensing`

### Ringkasan Sitasi
> Zhang dkk. (2019) mengusulkan model HRCNN untuk deteksi objek pada citra penginderaan jauh resolusi sangat tinggi (VHR). Model ini memanfaatkan representasi fitur konvolusi hierarkis melalui piramida fitur (FPN) untuk mengatasi variasi skala objek, serta menumpuk fitur dari lapisan terhubung penuh `fc6` dan `fc7` guna memperkuat ketahanan klasifikasi terhadap perubahan orientasi spasial. Penelitian ini juga berkontribusi pada komunitas ilmiah dengan memperkenalkan dataset benchmark HRRSD yang memiliki distribusi kelas objek yang seimbang.

### Catatan untuk Verifikasi
Angka mAP komparatif absolut pada dataset NWPU VHR-10 bervariasi bergantung pada jenis tulang punggung (*backbone*) yang dipilih (VGG-16 vs ResNet-50). Pengguna disarankan untuk memverifikasi konfigurasi arsitektur tulang punggung yang digunakan pada tabel eksperimen di naskah asli sebelum menyalin nilai akurasi spesifik kelas untuk sitasi formal.
