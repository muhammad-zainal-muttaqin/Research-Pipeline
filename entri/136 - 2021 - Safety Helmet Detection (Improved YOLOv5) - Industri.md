# 136 - Safety Helmet Wearing Detection Based on Improved YOLOv5

## Metadata Ringkas

| Atribut | Nilai |
| --- | --- |
| Kunci BibTeX | `zhou2021helmet` |
| Judul asli | Safety Helmet Wearing Detection Based on Improved YOLOv5 |
| Penulis | Zhou, Fang; Zhao, Huailin; Nie, Zhen |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision, Image and Deep Learning (CVIDL) |
| Tema | Industri |

## Tautan Akses

- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Safety%20Helmet%20Wearing%20Detection%20Based%20on%20Improved%20YOLOv5
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Safety%20Helmet%20Wearing%20Detection%20Based%20on%20Improved%20YOLOv5&sort=relevance

## Gambaran Umum

Makalah oleh Zhou dkk. (2021) menyajikan evaluasi komparatif arsitektur deteksi objek satu-tahap (*single-stage detector*) berbasis YOLOv5 untuk mendeteksi pemakaian helm keselamatan (*safety helmet*) di area konstruksi. Tujuan utamanya adalah merancang solusi pemantauan otomatis untuk mendukung kepatuhan regulasi keselamatan dan kesehatan kerja (K3). Sistem ini mendeteksi apakah pekerja mengenakan pelindung kepala dengan benar atau membiarkannya terbuka di area kerja berbahaya.

Penulis mengevaluasi empat varian YOLOv5 (YOLOv5s, YOLOv5m, YOLOv5l, dan YOLOv5x) pada dataset kustom sebanyak 6.045 citra yang dianotasi secara manual untuk kelas kepala berhelm (*helmet*) dan kepala tanpa helm (*head*). Hasil eksperimen menunjukkan varian YOLOv5x mencapai presisi rata-rata (*mean average precision* atau mAP) tertinggi sebesar 94,7%. Sementara itu, YOLOv5s menawarkan kecepatan inferensi tercepat sebesar 110 bingkai per detik (*frames per second* atau FPS), menjadikannya sangat ideal untuk pemantauan waktu nyata (*real-time*) pada perangkat komputasi tepi (*edge devices*) dengan sumber daya terbatas.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Keselamatan pekerja di sektor konstruksi dan manufaktur berat bergantung pada kepatuhan terhadap alat pelindung diri seperti helm keselamatan. Namun, pemantauan kepatuhan secara manual oleh petugas keselamatan tidak efisien, berbiaya tinggi, dan terbatas dalam cakupan spasial serta temporal. Otomatisasi pengawasan menggunakan kamera pemantau (CCTV) dan visi komputer (*computer vision*) diperlukan sebagai solusi alternatif.

Metode deteksi objek konvensional pra-pembelajaran mendalam, seperti *Histogram of Oriented Gradients* (HOG) dan *Support Vector Machine* (SVM), sangat sensitif terhadap perubahan intensitas cahaya, oklusi, dan variasi sudut pandang, sehingga memicu tingkat alarm palsu (*false alarm*) yang tinggi. Di sisi lain, penerapan deteksi objek berbasis jaringan saraf tiruan (*artificial neural network*) menghadapi tiga tantangan operasional di industri:
1. **Objek Skala Kecil:** Kamera pemantau yang dipasang tinggi membuat ukuran helm pekerja di latar belakang sangat kecil pada bidang citra (hanya beberapa piksel), menyulitkan ekstraksi fitur spasial.
2. **Kompleksitas Latar Belakang:** Lokasi kerja dipenuhi material dan peralatan dengan warna mencolok yang menyerupai helm keselamatan (kuning, merah, biru), sehingga memicu kesalahan deteksi (*false positive*).
3. **Kebutuhan Waktu Nyata:** Sistem harus memberikan peringatan instan dengan latensi minimal untuk mencegah kecelakaan sebelum terjadi.

## Ide Utama

Ide utama makalah ini adalah mengoptimalkan arsitektur YOLOv5 melalui pendekatan pembelajaran transfer (*transfer learning*) untuk mendeteksi penggunaan helm keselamatan secara cepat dan akurat. Penulis memfokuskan kontribusi pada pemetaan empiris mengenai varian model YOLOv5 yang paling optimal untuk mengatasi trade-off antara akurasi dan kecepatan inferensi pada skenario industri nyata.

Untuk meminimalkan kesalahan klasifikasi, model dilatih secara terawasi (*supervised learning*) menggunakan dataset kustom yang dirancang secara khusus untuk membedakan kelas `helmet` (kepala berhelm) dan `head` (kepala tanpa helm). Citra masukan diproses secara terpadu untuk mengekstraksi fitur spasial pada tulang punggung (*backbone*), menggabungkan fitur lintas skala pada leher jaringan (*neck*), dan memprediksi kotak pembatas (*bounding box*) beserta probabilitas kelas pada kepala prediksi (*head*). Sistem akan memicu alarm peringatan jika terdapat objek berkategori `head` terdeteksi di dalam zona berbahaya yang ditentukan.

## Cara Kerja Langkah demi Langkah

YOLOv5 bekerja secara *end-to-end* untuk memetakan piksel citra masukan langsung ke koordinat kotak pembatas dan label kelas. Proses ini dibagi menjadi empat tahapan utama:

```
            DIAGRAM ARSITEKTUR DETEKSI HELM KESELAMATAN YOLOV5
            
  Citra Input (640x640)
        │
        ▼
 ┌──────────────┐
 │   BACKBONE   │ ──► CSPDarknet53 (Ekstraksi fitur hierarkis)
 └──────┬───────┘
        │
        ├─────────────────────────┐ (Skala fitur rendah: P3 - 80x80)
        ├──────────────┐          │
        │              ▼          ▼
 ┌──────▼───────┐    ┌─────────────────┐
 │ SPPF Layer   │    │      NECK       │ ──► PANet (Fusi fitur multi-skala)
 └──────┬───────┘    │  (FPN + PANet)  │
        │            └────────┬────────┘
        ▼                     │
(Skala fitur tinggi: P5)      │
        └─────────────────────┼─────────────────────────┐
                              ▼                         ▼
                     ┌─────────────────┐       ┌─────────────────┐
                     │   YOLO HEAD     │ ──►   │   YOLO HEAD     │
                     │  (Grid 20x20)   │       │  (Grid 80x80)   │
                     └────────┬────────┘       └────────┬────────┘
                              │                         │
                              ▼                         ▼
                     [Objek Skala Besar]       [Objek Skala Kecil]
                     (Helm jarak dekat)        (Helm jarak jauh)
```

### 1. Prapemrosesan dan Augmentasi Data
Sebelum masuk ke jaringan, sistem menerapkan teknik augmentasi data Mosaic yang menggabungkan empat citra latih secara acak menjadi satu citra masukan. Hal ini memperbanyak variasi latar belakang dan secara artifisial memperkecil ukuran objek helm, memaksa model belajar mendeteksi objek skala kecil. Citra kemudian diselaraskan ke resolusi $640 \times 640$ piksel dengan pengisian dinamis (*adaptive frame padding*) untuk mencegah distorsi bentuk objek.

### 2. Ekstraksi Fitur dengan CSPDarknet53 Backbone
YOLOv5 menggunakan CSPDarknet53 sebagai *backbone*. Modul *Cross Stage Partial* (CSP) membagi peta fitur (*feature maps*) menjadi dua jalur: satu jalur melewati blok bottleneck konvolusional, sedangkan jalur lainnya langsung digabungkan (*concatenated*) di akhir blok. Aliran gradien terpisah ini memotong redundansi komputasi sebesar sekitar 20% tanpa mendegradasi fitur spasial halus. Lapisan *Spatial Pyramid Pooling Fast* (SPPF) di ujung *backbone* menangkap konteks global citra menggunakan operasi pooling multi-ukuran ($5 \times 5$, $9 \times 9$, $13 \times 13$) secara cepat.

### 3. Fusi Fitur Multi-Skala dengan PANet Neck
Bagian leher jaringan menggunakan kombinasi *Feature Pyramid Network* (FPN) dan *Path Aggregation Network* (PANet). FPN mentransfer fitur semantik tingkat tinggi ke lapisan bawah untuk memperkuat pengenalan kelas, sedangkan PANet menambahkan jalur koneksi bawah-ke-atas (*bottom-up path augmentation*) untuk mentransfer koordinat spasial presisi ke lapisan atas. Skema ini meminimalkan kegagalan deteksi pada helm kecil di latar belakang yang kompleks.

### 4. Prediksi dan Regresi Kotak Pembatas pada YOLO Head
Kepala deteksi memprediksi luaran pada tiga skala grid independen: grid $80 \times 80$ untuk objek kecil, $40 \times 40$ untuk objek sedang, dan $20 \times 20$ untuk objek besar. Pada setiap sel grid, model memprediksi koordinat kotak pembatas $(x, y, w, h)$, skor keyakinan objek, dan kelas (`helmet` vs `head`). Regresi kotak pembatas dilatih menggunakan fungsi rugi *Complete Intersection over Union* (CIoU) yang menghitung area tumpang unut (*overlap area*), jarak titik pusat dengan kotak kebenaran (*ground truth*), dan rasio aspek. Terakhir, *Non-Maximum Suppression* (NMS) mengeliminasi prediksi ganda yang tumpang tindih.

## Eksperimen dan Hasil

Evaluasi dilakukan menggunakan dataset kustom berisi 6.045 citra beresolusi tinggi di lokasi konstruksi nyata. Dataset ini juga memuat sampel negatif berupa citra keramaian manusia di kantor dan kelas untuk melatih model agar menolak alarm palsu dari rambut atau kepala polos manusia. Pengujian terhadap empat varian YOLOv5 menghasilkan data performa berikut:

- **YOLOv5s:** mencapai mAP sebesar 88,6% dengan kecepatan inferensi mencapai 110 FPS.
- **YOLOv5m:** mencapai mAP sebesar 91,2% dengan kecepatan inferensi 75 FPS.
- **YOLOv5l:** mencapai mAP sebesar 93,5% dengan kecepatan inferensi 50 FPS.
- **YOLOv5x:** mencapai mAP tertinggi sebesar 94,7% dengan kecepatan inferensi 30 FPS.

Interpretasi hasil membuktikan trade-off performa. YOLOv5x memberikan mAP tertinggi (94,7%), membuktikan keandalannya dalam mendeteksi helm kecil atau terhalang oklusi parsial, tetapi dengan laju inferensi rendah (30 FPS). Sebaliknya, YOLOv5s memberikan kecepatan inferensi 110 FPS yang melampaui batas standar kamera pengawas (30 FPS), sehingga menyisakan margin komputasi yang luas untuk diintegrasikan dengan modul pelacakan objek (*object tracking*) pada perangkat keras lokal berdaya rendah.

## Kelebihan dan Keterbatasan

**Kelebihan:**
1. **Skalabilitas:** Evaluasi empat varian YOLOv5 memberikan panduan pemilihan model sesuai kapasitas spesifikasi perangkat keras industri.
2. **Ketahanan:** Sampel negatif menekan tingkat alarm palsu dari kepala polos di luar area berbahaya.
3. **Efisiensi:** Keseimbangan optimal antara akurasi tinggi (94,7% mAP) dan kecepatan waktu nyata (110 FPS).

**Keterbatasan:**
1. **Ketergantungan RGB Tampak:** Kinerja detektor menurun tajam pada kondisi minim cahaya malam hari (*nighttime*) atau debu tebal karena hilangnya fitur tekstur dan warna helm.
2. **Kerentanan Oklusi:** Penggunaan input RGB kamera tunggal (*monocular RGB*) membuat model kesulitan melokalisasi pekerja yang terhalang tiang atau mesin. Integrasi sensor kedalaman (seperti pada kamera RGB-D) dapat memberikan informasi spasial tiga dimensi untuk pemisahan objek yang lebih konsisten.

## Kaitan dengan Bab Lain

Penelitian deteksi helm keselamatan ini termasuk dalam klaster aplikasi Industri dalam tinjauan pustaka ini, beralih dari inspeksi cacat kualitas produk ke pengawasan keselamatan operasional.

Secara taksonomis, bab ini mewujudkan pemenuhan tantangan operasional waktu nyata (*real-time constraints*) yang dibahas pada payung teoritis [135 - 2021 - Review Defect Detection (Bhatt dkk.) - Industri](./135%20-%202021%20-%20Review%20Defect%20Detection%20%28Bhatt%20dkk.%29%20-%20Industri.md). Dalam ulasan Bhatt dkk., performa waktu nyata di atas laju produksi merupakan syarat mutlak, yang dipenuhi oleh YOLOv5s (110 FPS).

Masalah deteksi objek kecil pada latar belakang kompleks menghubungkan bab ini dengan metode deteksi cacat baja pada [133 - 2023 - EFC-YOLO (Steel Strip Defects) - Industri](./133%20-%202023%20-%20EFC-YOLO%20%28Steel%20Strip%20Defects%29%20-%20Industri.md) dan inspeksi papan sirkuit pada [134 - 2024 - PCB-YOLO (PCB Defects) - Industri](./134%20-%202024%20-%20PCB-YOLO%20%28PCB%20Defects%29%20-%20Industri.md). Berbeda dengan EFC-YOLO dan PCB-YOLO yang memodifikasi arsitektur dengan mekanisme perhatian (*attention mechanism*) khusus untuk mendeteksi cacat mikro, bab ini membuktikan bahwa dengan penalaan halus dan augmentasi Mosaic yang tepat, arsitektur YOLOv5 standar sudah mampu mencapai mAP kompetitif (94,7%) tanpa meningkatkan kompleksitas model.

## Poin untuk Sitasi

- **Kunci BibTeX:** `zhou2021helmet`
- **Ringkasan untuk Sitasi:** Zhou dkk. (2021) melakukan evaluasi komparatif varian YOLOv5 (s, m, l, x) untuk deteksi pemakaian helm keselamatan pekerja pada dataset 6.045 citra konstruksi. Eksperimen menunjukkan YOLOv5x mencapai akurasi tertinggi sebesar 94,7% mAP, sedangkan YOLOv5s menawarkan kecepatan inferensi tercepat sebesar 110 FPS, yang ideal untuk pemantauan keselamatan kerja waktu nyata.
- **Catatan Verifikasi:** Nilai mAP 94,7% (YOLOv5x) dan laju inferensi 110 FPS (YOLOv5s) dilaporkan berdasarkan dataset kustom 6.045 citra dari penulis. Hasil performa dapat bervariasi jika diuji pada lokasi dengan pencahayaan atau sudut kamera berbeda, sehingga validasi silang pada dataset eksternal diperlukan sebelum penerapan skala penuh.
