# Computationally Efficient Transfer Learning Pipeline for Oil Palm Fresh Fruit Bunch Defect Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2025computationally` |
| Judul asli | Computationally Efficient Transfer Learning Pipeline for Oil Palm Fresh Fruit Bunch Defect Detection |
| Penulis | Luo, Yang; P. P. Abdul Majeed, Anwar; Omar, Zaid; Aslam, Saad; Chen, Yi |
| Tahun | 2025 |
| Venue | Technologies |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [luo2025computationally.pdf](../pdf/luo2025computationally.pdf)
- DOI resmi: https://doi.org/10.3390/technologies13060234

## Gambaran Umum

Penelitian ini bertujuan mengklasifikasikan tandan buah segar (TBS) kelapa sawit menjadi cacat dan tidak cacat tanpa melatih ulang jaringan dalam secara menyeluruh. Pemeriksaan manual dianggap memakan tenaga dan rentan terhadap inkonsistensi subjektif. Penulis memilih *feature-based transfer learning* karena pelatihan dari awal mahal secara komputasi, sementara data cacat yang berlabel terbatas. Kajian sebelumnya lebih banyak menguji klasifikasi kematangan dengan penyetelan halus (*fine-tuning*) dan deteksi objek; pengujian sistematis terhadap penggolongan cacat dengan ekstraktor fitur tetap belum banyak dilakukan.

Data berupa 466 citra TBS dari perkebunan di Johor, Negeri Sembilan, dan Perak, Malaysia. Penilai berpengalaman awalnya memberi label kematangan lima tahap, lalu penulis menyatukannya menjadi dua kelas, yaitu cacat (265 citra) dan tidak cacat (201 citra), dengan perhatian pada penanda seperti soket kosong. Citra diambil pada pencahayaan dan sudut beragam, baik di pohon maupun di tanah setelah panen, tanpa augmentasi data. Pembagian memakai *hold-out* 60:20:20: 279 citra latih (159 cacat, 120 tidak cacat), 93 citra validasi (53, 40), dan 94 citra uji (53, 41).

Mekanisme ekstraksi memakai empat CNN terlatih sebagai ekstraktor fitur tetap tanpa mengubah bobot: EfficientNet-B0 menghasilkan 1280 fitur, EfficientNet-B4 1792 fitur, ResNet152 2048 fitur, dan VGG16 512 fitur, semuanya diambil dari keluaran *global average pooling* sebelum kepala klasifikasi. Fitur tersebut masuk ke regresi logistik. Penulis menguji penalti L1, L2, ElasticNet, atau tanpa penalti; solver lbfgs, liblinear, atau saga; serta nilai C 0,001 sampai 1000. Pencarian dengan kerangka Optuna dan validasi silang lima lipat pada data latih menentukan konfigurasi terbaik, yang lalu dilatih ulang pada gabungan data latih dan validasi sebelum dinilai pada cawat uji. Metrik dihitung dari matriks konfusi: akurasi (TP+TN)/(TP+TN+FP+FN), presisi TP/(TP+FP), recall TP/(TP+FN), dan F1 sebagai rata-rata harmonis keduanya.

Tanpa penyetelan, EfficientNet-B4-LR mencatat akurasi uji 95,74% dengan F1 96,15% untuk kelas cacat dan 95,24% untuk kelas tidak cacat. EfficientNet-B0-LR dan VGG16-LR masing-masing mencatat 91,49%, sedangkan ResNet152-LR 88,30%. Setelah penyetelan, EfficientNet-B4-LR mencapai 96,81% dengan F1 97,14% dan 96,39%; VGG16-LR 94,68%; ResNet152-LR 93,62%; EfficientNet-B0-LR 92,55%. Konfigurasi terbaik memakai penalti L2 untuk seluruh pipeline, dengan solver liblinear dan C sekitar 30,4 untuk B0 serta 33,7 untuk VGG16, dan solver saga dengan C sekitar 13,5 untuk B4 serta 0,07 untuk ResNet152. Pada cawat uji, pipeline EfficientNet-B4-LR mengklasifikasikan 51 dari 53 citra cacat dan 40 dari 41 citra tidak cacat dengan benar.

Penulis menyebut biaya komputasi lebih rendah daripada *fine-tuning* karena yang dilatih hanya regresi logistik berdimensi 512–2048; angka percepatan 100–1000 kali dan penghematan memori 50–80% dikutip dari literatur, bukan diukur dalam percobaan ini. Batasan yang dinyatakan adalah *hold-out* memberi satu sudut pandang saja sehingga perlu validasi silang atau data lebih banyak, kondisi tandan borderline dan cacat sebagian masih sulit dibedakan, dan generalisasi perlu diuji pada lokasi perkebunan serta musim berbeda. Penulis juga mencatat bahwa *global average pooling* dapat melemahkan petunjuk cacat yang bersifat lokal.

