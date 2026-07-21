# 131 - Breast Tumor Detection and Classification in Mammogram Images Using Modified YOLOv5 Network

## Metadata Ringkas
| Bidang | Nilai |
|---|---|
| Kunci BibTeX | `mohiyuddin2022breast` |
| Judul asli | Breast Tumor Detection and Classification in Mammogram Images Using Modified YOLOv5 Network |
| Penulis | Mohiyuddin, Aqsa; Basharat, Asma; Ghani, Usman; Peter, Vaclav; Abbas, Sidra; Naeem, Osama Bin; Rizwan, Muhammad |
| Tahun | 2022 |
| Venue | Computational and Mathematical Methods in Medicine |
| Tema | Medis |

## Tautan Akses
- Google Scholar: https://scholar.google.com/scholar?q=Breast%20Tumor%20Detection%20and%20Classification%20in%20Mammogram%20Images%20Using%20Modified%20YOLOv5%20Network
- Semantic Scholar: https://www.semanticscholar.org/search?q=Breast%20Tumor%20Detection%20and%20Classification%20in%20Mammogram%20Images%20Using%20Modified%20YOLOv5%20Network&sort=relevance
- PubMed Central (PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8752232/

## Gambaran Umum
Makalah ini mengusulkan model deteksi objek satu tahap (*one-stage object detector*) berbasis *Modified YOLOv5* untuk mendeteksi dan mengklasifikasikan tumor payudara menjadi jinak (*benign*) dan ganas (*malignant*) pada citra mamogram. Masalah utama yang diselesaikan adalah tingginya rasio positif palsu (*false positive ratio* / FPR) dan negatif palsu (*false negative ratio* / FNR) serta rendahnya nilai Koefisien Korelasi Matthews (*Matthews Correlation Coefficient* / MCC) pada metode diagnosis berbasis komputer konvensional. Penulis mengidentifikasi bahwa modul *Cross Stage Partial* (CSP) pada struktur YOLOv5 menyumbang beban parameter yang terlalu berat. Untuk mengatasinya, diusulkan modifikasi berupa penyederhanaan arsitektur *BottleneckCSP* dengan menghapus lapisan konvolusi pada cabang pintasannya (*bypass branch*).

Pengujian dilakukan menggunakan dataset publik *Curated Breast Imaging Subset of DDSM* (CBIS-DDSM). Model terbaik yang diusulkan, yaitu *Modified YOLOv5x*, dilaporkan mencapai akurasi sebesar 96,50%, rata-rata presisi rata-rata (*mean Average Precision* / mAP) sebesar 96,00%, dan nilai MCC sebesar 93,50%, melampaui performa YOLOv3 dan *Faster R-CNN*. Namun, perlu dicatat bahwa artikel ini telah resmi diretraksi pada 28 Juni 2023 oleh penerbit karena masalah integritas ilmiah dan manipulasi proses penelaahan sejawat (*peer-review*).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Kanker payudara merupakan penyebab kematian tertinggi kedua akibat kanker pada populasi wanita secara global. Penapisan (*screening*) dini menggunakan mamografi efektif menekan tingkat kematian, namun interpretasi citra mamogram secara manual sangat rentan terhadap kesalahan diagnosis. Hal ini disebabkan oleh rendahnya kontras visual antara massa tumor dengan jaringan kelenjar payudara yang padat, serta gangguan struktur anatomi lain seperti otot pektoral (*pectoral muscle*) yang memiliki intensitas piksel mirip dengan lesi tumor.

Sistem diagnosis berbantuan komputer (*computer-aided diagnosis* / CAD) konvensional berbasis detektor objek dua tahap seperti *Faster R-CNN* maupun detektor satu tahap seperti YOLOv3 masih menghasilkan tingkat diagnosis salah yang signifikan. Negatif palsu yang tinggi berisiko membiarkan tumor ganas berkembang tanpa penanganan medis, sementara positif palsu memicu kecemasan pasien dan prosedur biopsi invasif yang tidak perlu. Selain itu, akurasi global sering kali bias pada dataset dengan kelas yang tidak seimbang (*imbalanced dataset*), sehingga diperlukan metrik evaluasi yang lebih andal seperti MCC untuk mengukur akurasi prediksi pada seluruh kategori matriks kekacauan (*confusion matrix*). Masalah ini menuntut arsitektur deteksi objek yang lebih ringan, sensitif, dan mampu menekan nilai FPR serta FNR secara bersamaan.

## Ide Utama
Gagasan utama makalah ini adalah menyederhanakan mekanisme ekstraksi fitur pada tulang punggung (*backbone*) YOLOv5 untuk domain mamografi. Penulis memodifikasi modul *BottleneckCSP* asli dengan menghapus lapisan konvolusi pada salah satu cabang bypass. Struktur baru ini dinamakan *BottleneckCSP-new*, di mana fitur masukan langsung disambungkan ke operasi penggabungan (*depth-wise concatenation*) tanpa ekstraksi konvolusional tambahan di cabang tersebut. Hal ini secara signifikan memotong parameter komputasi, mempercepat inferensi, dan mencegah penyesuaian berlebih (*overfitting*). Sebelum data dimasukkan ke model, diterapkan alur pra-pemrosesan citra berbasis MATLAB untuk mengisolasi wilayah tumor dengan membuang batas putih kasar, menyaring otot pektoral serta label teks, meningkatkan kontras lokal via *Contrast Limited Adaptive Histogram Equalization* (CLAHE), dan menonjolkan massa tumor utama menggunakan operasi erosi morfologi (*morphological erosion*).

## Cara Kerja Langkah demi Langkah

### Pra-pemrosesan Citra Mamogram
Sebelum citra dimasukkan ke dalam jaringan, serangkaian langkah pra-pemrosesan diterapkan secara berurutan:
1. **Penghapusan Batas Putih:** Batas putih kasar di tepi mamogram mentah dipotong (*cropped*) karena intensitas pikselnya yang tinggi dapat memicu positif palsu.
2. **Eliminasi Otot Pektoral dan Label Teks:** Otot pektoral pada sudut atas citra yang tampak terang dideteksi berdasarkan ambang batas intensitas kolom di MATLAB dan dihapus secara otomatis bersama label teks.
3. **Peningkatan Kontras CLAHE:** CLAHE membagi citra menjadi ubin lokal berukuran $8 \times 8$ piksel dan meratakan histogram dengan membatasi kontras pada nilai default 40 untuk memperjelas batas lesi tumor yang samar.
4. **Operasi Erosi Morfologi:** Jaringan payudara sehat disaring menggunakan operasi erosi biner berbasis elemen penstruktur untuk mengikis objek minor, sehingga menyisakan area tumor utama yang menonjol.

### Modifikasi Modul BottleneckCSP (BottleneckCSP-new)
Pada YOLOv5 standar, modul *BottleneckCSP* membagi fitur masukan menjadi dua cabang. Cabang utama melewati konvolusi $1 \times 1$, blok residu (*Bottleneck*), dan konvolusi $1 \times 1$. Cabang kedua (cabang pintasan) melewati lapisan konvolusi $1 \times 1$ sebagai proyeksi linear. Kedua fitur ini kemudian digabungkan secara mendalam (*concatenation*).

Dalam rancangan *Modified YOLOv5*, penulis menghapus lapisan konvolusi pada cabang kedua tersebut. Hal ini membuat separuh fitur masukan langsung dialirkan ke operasi penggabungan tanpa transformasi konvolusional tambahan.

Perbandingan arsitektur modul disajikan dalam diagram ASCII berikut:

```
[BottleneckCSP Standar]
Input ───────────────────────────────┐
  │                                  │
[Conv 1x1]                      [Conv 1x1] (Proyeksi)
  │                                  │
[Bottleneck Block]                   │
  │                                  │
[Conv 1x1]                          │
  │                                  │
  ▼                                  ▼
[Concatenation] ◄────────────────────┘
  │
[Conv 1x1 (Akhir)]
  │
  ▼
Output
```

```
[Modified BottleneckCSP / BottleneckCSP-new]
Input ───────────────────────────────┐
  │                                  │
[Conv 1x1]                           │
  │                                  │
[Bottleneck Block]                   │
  │                                  │
[Conv 1x1]                          │
  │                                  │
  ▼                                  ▼
[Concatenation] ◄────────────────────┘ (Pintasan Langsung)
  │
[Conv 1x1 (Akhir)]
  │
  ▼
Output
```

Modifikasi ini diterapkan pada keempat modul *BottleneckCSP* di bagian tulang punggung (*backbone*) YOLOv5 untuk mereduksi parameter secara global.

### Anotasi dan Augmentasi Data
Penelitian ini menggunakan 2424 citra mamogram massa dari dataset CBIS-DDSM yang dianotasi menggunakan *Roboflow*. Berkas anotasi luaran disimpan dalam format teks `.txt` yang berisi koordinat kotak pembatas (*bounding box*) dan label kelas tumor.

Augmentasi data dilakukan melalui pemutaran horizontal, rotasi 90 dan 180 derajat, serta duplikasi kecerahan, menghasilkan total 4865 citra. Dataset dibagi menjadi 60% pelatihan (2919 citra), 30% validasi (1459 citra), dan 10% pengujian (487 citra). Karena keterbatasan memori GPU, citra beresolusi asli $3000 \times 4500$ piksel diperkecil skalanya menjadi $1000 \times 2000$ piksel.

### Proses Pelatihan dan Fungsi Kerugian
Model dilatih pada sistem Linux Ubuntu 16.04 menggunakan GPU Nvidia GeForce GTX 1080Ti (11 GB) dengan kerangka kerja *Keras* dan *TensorFlow*. Bobot awal dimuat dari pra-latih COCO. Optimasi menggunakan algoritma *Stochastic Gradient Descent* (SGD) dengan laju pembelajaran awal 0,01, momentum 0,843, peluruhan bobot (*weight decay*) 0,00036, ukuran *batch* 8, dan ambang batas IoU sebesar 0,2 selama 300 *epoch*. Fungsi kerugian total dihitung dari penjumlahan kerugian klasifikasi, kerugian objek (*objectness*), dan kerugian lokalisasi berbasis *Generalized IoU* (GIoU).

## Eksperimen dan Hasil
Performa model dievaluasi dengan membandingkan versi asli (*original*) dan versi modifikasi (*modified*) pada empat varian YOLOv5 (s, m, l, x) menggunakan data pengujian.

Rincian hasil eksperimen untuk setiap model disajikan pada tabel di bawah ini:

| Model | Versi | Sensitivitas (%) | Spesifisitas (%) | Presisi (%) | mAP (%) | Akurasi (%) | MCC (%) | FPR | FNR |
|---|---|---|---|---|---|---|---|---|---|
| **YOLOv5s** | Asli | 90,00 | 91,00 | 90,90 | 88,70 | 90,50 | 81,00 | 0,09 | 0,10 |
| | Modifikasi | 95,00 | 97,00 | 96,93 | 95,20 | 96,00 | 92,02 | 0,03 | 0,05 |
| **YOLOv5m** | Asli | 91,00 | 89,00 | 89,21 | 87,20 | 90,00 | 80,02 | 0,11 | 0,09 |
| | Modifikasi | 94,00 | 97,00 | 96,90 | 95,00 | 95,50 | 91,04 | 0,03 | 0,06 |
| **YOLOv5l** | Asli | 92,00 | 91,00 | 91,08 | 88,90 | 91,50 | 83,00 | 0,09 | 0,08 |
| | Modifikasi | 95,00 | 97,00 | 96,93 | 95,20 | 96,00 | 92,02 | 0,03 | 0,05 |
| **YOLOv5x** | Asli | 93,00 | 92,00 | 92,07 | 89,20 | 92,50 | 85,00 | 0,08 | 0,07 |
| | Modifikasi | 96,00 | 97,00 | 97,00 | 96,00 | 96,50 | 93,60 | 0,04 | 0,03 |

Hasil pengujian membuktikan bahwa seluruh varian model modifikasi melampaui kinerja versi asli pada semua metrik. *Modified YOLOv5x* mencatatkan kinerja tertinggi dengan akurasi 96,50%, mAP 96,00%, MCC 93,60%, serta tingkat kesalahan terkecil (FPR 0,04 dan FNR 0,03). Ketika dibandingkan dengan YOLOv3 dan Faster R-CNN, model *Modified YOLOv5x* secara signifikan menekan bias diagnosis. Faster R-CNN mencatat FNR 13,00% dan FPR 12,00% pada domain yang sama, sedangkan YOLOv3 menghasilkan nilai MCC di bawah 88,00%.

## Kelebihan dan Keterbatasan

### Kelebihan
Penyederhanaan arsitektur pada modul *BottleneckCSP* melalui penghapusan konvolusi cabang pintasan berhasil mengurangi parameter latih secara signifikan, sehingga menghasilkan model yang lebih ringan dan efisien secara komputasi. Integrasi pra-pemrosesan citra terarah (khususnya eliminasi otot pektoral dan batas putih) sangat efektif dalam memfokuskan wilayah tumor dan terbukti secara langsung menurunkan rasio positif palsu (FPR) dan negatif palsu (FNR). Pengujian yang membandingkan keempat varian YOLOv5 memberikan analisis komprehensif mengenai skalabilitas model pada tingkat kedalaman yang berbeda.

### Keterbatasan
Secara konseptual, penghapusan lapisan konvolusi pada cabang pintasan berisiko mengurangi kapasitas transfer informasi spasial resolusi tinggi. Hal ini dapat menghambat pendeteksian tumor yang berukuran sangat kecil atau terdistribusi dalam pola mikrokalsifikasi (*microcalcifications*). Reduksi parameter juga berisiko mengurangi generalisasi model ketika diterapkan pada citra mamogram dari mesin pemindai yang berbeda dengan dataset latih.

Dari sisi integritas akademis, keterbatasan utama makalah ini adalah status publikasinya yang telah **diretraksi** oleh penerbit pada 28 Juni 2023. Alasan retraksi meliputi manipulasi penelaahan sejawat (*peer-review*), sitasi tidak relevan, serta keraguan ilmiah atas keabsahan data eksperimen yang disajikan. Oleh karena itu, klaim kinerja numerik yang sangat tinggi (seperti mAP 96,00% dan akurasi 96,50%) harus disikapi dengan keraguan ilmiah yang tinggi dan tidak dapat dijadikan acuan klinis yang andal sebelum divalidasi melalui eksperimen replikasi independen.

## Kaitan dengan Bab Lain
Makalah ini tergolong dalam klaster **Medis** yang mengevaluasi efektivitas detektor objek satu tahap pada pencitraan medis. Makalah ini berkaitan erat dengan beberapa bab berikut:
- **Kaitan dengan [128 - 2024 - Systematic Review YOLO Medis (Qureshi dkk.) - Medis](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md):** Makalah Mohiyuddin dkk. menjadi salah satu bukti empiris yang diulas dalam tinjauan sistematis tersebut mengenai efektivitas adaptasi YOLOv5 untuk segmentasi dan deteksi lesi klinis.
- **Kaitan dengan [130 - 2021 - Breast Lesion Detection (YOLO Fusion) - Medis](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md):** Kedua penelitian berfokus pada deteksi tumor payudara pada mamogram. Sementara YOLO Fusion menggunakan fusi fitur multi-resolusi secara horizontal untuk mengatasi kontras rendah, Mohiyuddin dkk. menyederhanakan arsitektur blok residu secara vertikal untuk menekan parameter komputasi.
- **Kaitan dengan [129 - 2021 - COVID-19 CAD dari X-Ray (Al-Antari dkk.) - Medis](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md) dan [132 - 2023 - YOLO untuk Deteksi Polip (Wan dkk.) - Medis](./132%20-%202023%20-%20YOLO%20untuk%20Deteksi%20Polip%20%28Wan%20dkk.%29%20-%20Medis.md):** Semua studi ini memodifikasi arsitektur standar YOLO untuk mendeteksi patologi organ tubuh (paru-paru dan usus besar) yang memiliki kontras rendah dan bentuk yang bervariasi, menekankan pentingnya pra-pemrosesan citra medis untuk menunjang performa detektor.

## Poin untuk Sitasi
- Kunci BibTeX: `mohiyuddin2022breast`
- Kutipan Ringkas:
  > "Mohiyuddin dkk. mengusulkan arsitektur Modified YOLOv5 dengan menyederhanakan modul BottleneckCSP melalui penghapusan konvolusi cabang pintasan untuk klasifikasi tumor payudara jinak dan ganas pada dataset CBIS-DDSM. Meskipun dilaporkan menghasilkan akurasi 96,50% dan mAP 96,00%, artikel ini telah resmi diretraksi pada tahun 2023 karena masalah integritas ilmiah."
- Catatan Penting untuk Verifikasi:
  > **PERINGATAN RETRAKSI:** Makalah ini resmi diretraksi pada 28 Juni 2023 karena penyimpangan etika publikasi dan penelaahan sejawat. Seluruh klaim performa (seperti akurasi 96,50%, mAP 96,00%, dan MCC 93,60%) harus disikapi secara kritis dan tidak dapat dikutip sebagai data terverifikasi tanpa menyertakan status retraksinya.
