# Toward Real Scenery: A Lightweight Tomato Growth Inspection Algorithm for Leaf Disease Detection and Fruit Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kang2024real` |
| Judul asli | Toward Real Scenery: A Lightweight Tomato Growth Inspection Algorithm for Leaf Disease Detection and Fruit Counting |
| Penulis | Kang, Rui; Huang, Jiaxin; Zhou, Xuehai; Ren, Ni; Sun, Shangpeng |
| Tahun | 2024 |
| Venue | Plant Phenomics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [kang2024real.pdf](../pdf/kang2024real.pdf)
- DOI resmi: https://doi.org/10.34133/plantphenomics.0174

## Gambaran Umum

Makalah ini mengusulkan kerangka kaskade yang menggabungkan detektor dan pelacak untuk dua tugas sekaligus pada tomat rumah kaca: deteksi penyakit daun dan penghitungan buah dari aliran video. Penulis memperkenalkan YOLO-TGI, varian YOLOv8 ringan yang memakai modul Ghost dan modul perhatian CBAM, lalu membandingkannya dengan YOLOX dan NanoDet-Plus sebagai detektor, serta ByteTrack, Motpy, dan FairMOT sebagai pelacak.

Data diambil di fasilitas rumah kaca cerdas Jiangsu Academy of Agricultural Sciences pada 2023 dengan kamera iPhone 12 Pro yang dipasang pada platform bergerak otonom (resolusi asli 3.024 × 4.032 piksel). Dataset akhir berisi 5.280 citra latih, 1.320 validasi, dan 660 uji untuk tiga kelas: daun sakit, daun sehat, dan buah tomat. Video pemindaian dipakai untuk penghitungan buah.

Hasil utama: YOLO-TGI-N memiliki FLOPs terendah (2,05 G) dan bobot *checkpoint* 3,7 M dengan mAP 0,72. Untuk penghitungan buah, kombinasi YOLO-TGI-S dan ByteTrack memberi R² 0,93 dan RMSE 9,17 terhadap hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa pemantauan pertumbuhan tomat di rumah kaca terhambat oleh pola penyakit yang berubah, latar belakang kompleks, dan kondisi cahaya. Dataset penyakit daun yang ada, seperti PlantVillage dan PlantDoc, dinilai kurang mewakili kondisi nyata: PlantVillage terutama berisi citra daun tunggal dengan latar seragam, dan PlantDoc banyak diambil dari internet. Penulis juga mencatat bahwa pengaturan hiperparameter dan strategi pemasangan sering tidak diungkapkan sehingga hasil sulit direplikasi.

Untuk penghitungan buah, metode deteksi per citra dapat menghitung buah pada satu gambar tetapi tidak mengagregasi hasil pada seluruh area tanam. Pada rumah kaca, tomat ditanam berbaris sehingga pemindaian video sederhana dilakukan, namun penghitungan akurat dari video tetap sulit karena kemampuan model dasar, oklusi daun, dan keterbatasan komputasi.

## Ide Utama

Satu model ekstraksi fitur bersama dipakai untuk dua tugas, dan pelacak SORT yang ditingkatkan melacak buah antarbingkai agar tiap buah dihitung sekali. Penulis juga merancang antarmuka seragam, dengan semua detektor diekspor ke format ONNX dan parameter diatur lewat berkas konfigurasi JSON, sehingga kombinasi detektor dan pelacak dapat ditukar. Skala model tersedia dalam tiga ukuran: N (*nano*), S (*small*), dan M (*medium*).

## Cara Kerja Langkah demi Langkah

```
 Video --> detektor (YOLO-TGI / YOLOX / NanoDet) --> kotak buah per bingkai
                                                           |
                                                           v
                         pelacak (ByteTrack / Motpy / FairMOT) --> ID per buah
                                                           |
                                                           v
                    penyaringan ID dengan rentang batas virtual --> hitungan
```

### 1. Akuisisi dan anotasi data

Tanaman tomat ditanam di media cocopeat dengan sistem fertigasi. Citra diambil dengan iPhone 12 Pro pada braket di platform bergerak. Anotasi memakai Roboflow. Penyakit daun yang tercakup meliputi bercak bakteri (*bacterial spot*), virus mosaik, hawar daun (*late blight*), dan "*spider mold*" menurut teks makalah. Augmentasi (rotasi, pantulan, translasi) dilakukan dengan ImgAug, lalu citra diubah ukurannya menjadi 640 × 640 piksel dan dikonversi ke format COCO dan YOLO. Folder latih, validasi, dan uji dipisahkan untuk menghindari kebocoran data. Jumlah video, durasi, kultivar tomat, dan jumlah buah pada video uji tidak dilaporkan di teks utama; makalah merujuk pada materi tambahan.

### 2. Detektor YOLO-TGI

YOLO-TGI memodifikasi tulang punggung YOLOv8. Modul Ghost menggantikan konvolusi biasa: konvolusi primer 1×1 mengompresi kanal, lalu "operasi murah" berupa transformasi linear menghasilkan peta fitur tambahan; konvolusi *depth-wise* (DW-Conv) dipakai pada jaringan. Modul C2f dan SPPF dipertahankan. Modul CBAM (perhatian kanal dan spasial) ditambahkan untuk membantu mengenali buah yang tertutup daun, yang menurut penulis sering terlewat karena sensitivitas ambang *non-maximum suppression* (NMS).

### 3. Pelacak

Pelacak mengikuti paradigma *tracking-by-detection* dengan algoritma Hungarian, filter Kalman, dan pengelolaan lintasan. Motpy dan ByteTrack memakai IoU antara kotak deteksi dan kotak prediksi Kalman sebagai biaya. ByteTrack membagi kotak menjadi keyakinan tinggi dan rendah, dan mengasosiasikan kotak berkeyakinan rendah dengan lintasan yang belum cocok. FairMOT memakai jarak Euclidean dan penghitung inersia dengan ambang atas dan bawah.

### 4. Penghitungan dan penyaringan ID

Untuk mengurangi pergantian ID akibat oklusi dan gerak kamera, penulis menerapkan penyaringan ID berbasis rentang batas virtual (garis kuning pada gambar): buah dihitung hanya bila ID-nya memasuki area yang ditetapkan. Perincian ukuran area tidak dijelaskan.

### 5. Evaluasi dan perangkat

Detektor dilatih pada server Ubuntu dengan GPU NVIDIA A100 40 GB, PyTorch 1.12, CUDA 10.2, dengan SGD dan momentum. Kecepatan inferensi diukur pada notebook Mac dengan CPU M1, RAM 16 GB, PyTorch 1.13. Hitungan video dibandingkan dengan hitungan manual memakai R² dan RMSE.

## Eksperimen dan Hasil

### Detektor dasar pada citra uji (Tabel 1)

| Model | Resolusi | FLOPs (G) | Param (M) | Bobot (M) | mAP | Kecepatan M1-CPU (ms) |
|---|---|---|---|---|---|---|
| YOLOX-N | 416 × 416 | 4,93 | 2,24 | 9,00 | 0,50 | 32,35 |
| YOLOX-S | 416 × 416 | 6,44 | 5,03 | 20,20 | 0,68 | 38,34 |
| YOLOX-M | 640 × 640 | 26,76 | 8,94 | 35,80 | 0,85 | 99,3 |
| NanoDet-N | 640 × 640 | 18,40 | 1,16 | 5,50 | 0,78 | 166,08 |
| NanoDet-S | 320 × 320 | 8,95 | 2,43 | 10,60 | 0,81 | 72,3 |
| NanoDet-M | 640 × 640 | 35,8 | 2,44 | 10,60 | 0,83 | 245,40 |
| YOLO-TGI-N | 640 × 640 | 2,05 | 1,59 | 3,70 | 0,72 | 54,20 |
| YOLO-TGI-S | 640 × 640 | 6,08 | 5,43 | 21,90 | 0,83 | 88,20 |
| YOLO-TGI-M | 640 × 640 | 12,3 | 11,6 | 46,80 | 0,83 | 143,00 |

Teks menyebut mAP tertinggi 0,85 (YOLOX), ukuran terkecil NanoDet (1,16 M parameter), serta FLOPs terendah dan bobot 3,7 M pada YOLO-TGI. Resolusi masukan berbeda antar model sehingga perbandingan tidak sepenuhnya setara. Mayoritas kesalahan deteksi daun terjadi pada citra buram, lesi tertutup sebagian, dan infeksi batang. Penulis mengamati bahwa YOLO-TGI-S dengan CBAM terlalu sensitif dan keliru menilai daun yang seharusnya latar.

### Penghitungan buah dari video (Tabel 2, sebagian)

| Kombinasi | R² | RMSE | Kecepatan inferensi (ms) |
|---|---|---|---|
| YOLO-TGI-S + ByteTrack | 0,93 | 9,17 | 118,2 |
| YOLO-TGI-N + ByteTrack | 0,90 | 11,32 | 115,7 |
| YOLOX-M + Motpy | 0,90 | 11,23 | 303,8 |
| NanoDet-M + ByteTrack | 0,89 | 11,79 | 269,0 |
| YOLOX-N + Motpy | 0,77 | 16,91 | 49,8 |
| NanoDet-S + FairMOT | 0,34 | 28,54 | 249,6 |
| YOLOX-N + FairMOT | 0,32 | 29,13 | 61,3 |

Tabel 2 memuat seluruh 27 kombinasi; tabel di atas hanya memilih baris yang dibahas di teks. FairMOT tampil paling lemah; pada YOLO-TGI-M, FairMOT memberi R² 0,69 dan RMSE 19,48. Menurut penulis, pada skala S dan M, kombinasi YOLO-TGI dan ByteTrack hampir dua kali lebih cepat daripada YOLOX dan sekitar 2,5 kali lebih cepat daripada NanoDet. Penulis menyebut penurunan presisi YOLO-TGI dari N ke M, yang dikaitkan dengan CBAM yang memicu lebih banyak wilayah latar sebagai buah.

Kesalahan hitungan meningkat pada video dengan jumlah tomat yang lebih banyak. Kasus yang dianalisis: tomat tertutup daun pada satu bingkai tetapi terdeteksi pada bingkai lain menghasilkan hitungan membengkak, dan tomat yang semula terlihat lalu tertutup menyebabkan hitungan berkurang.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: dataset rumah kaca nyata dengan daun dan buah; model ringan; kerangka terpadu dengan ekspor ONNX dan konfigurasi JSON; serta kode dan data dibuka melalui repositori GitHub dan Roboflow.

Keterbatasan yang dinyatakan penulis: gangguan latar dan dedaunan adalah penyebab utama selisih hitungan; ketidakseimbangan jumlah sampel daun sehat berpengaruh sedikit; daun sakit yang bertekstur mirip tomat belum matang (kuning atau hitam) dapat dikira buah, terutama pada video beresolusi rendah; dan CBAM meningkatkan positif palsu pada skala besar.

Menurut pembacaan ringkasan ini: (a) jumlah video uji dan jumlah buah per video tidak dicantumkan di teks utama sehingga stabilitas R² 0,93 tidak dapat dinilai; (b) tidak ada pembanding pelacak tanpa penyaringan ID sehingga kontribusi penyaringan batas virtual tidak terukur; (c) detektor diukur pada resolusi masukan berbeda; (d) hitungan hanya total, tidak per kelas atau per tingkat kematangan; (e) pemindaian dilakukan dari satu sisi baris, tanpa pencocokan sisi berlawanan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang tampak pada banyak bingkai video dengan pelacakan multi-objek: asosiasi dan filter Kalman (Motpy, ByteTrack, FairMOT) memberi ID per buah, dan hitungan dikendalikan oleh penyaringan ID pada rentang batas virtual. Identitas hanya dipertahankan sepanjang urutan waktu satu video; tidak ada pencocokan antar-pandangan atau antar-sisi tanaman. Hitungan tidak dilaporkan per kelas buah. Acuan hitungnya adalah hitungan manual dari video.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah perbandingan sistematis beberapa pelacak pada satu detektor, serta temuan bahwa penghitungan salah membesar atau mengecil akibat oklusi dan pergantian ID. Temuan itu relevan bagi tandan yang tertutup pelepah. Penghitungan melalui batas virtual tidak dapat diterapkan langsung pada citra statis dari beberapa sisi pohon.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `kang2024real`.

Kang dkk. (2024) mengusulkan kerangka kaskade detektor dan pelacak untuk tomat rumah kaca. YOLO-TGI, varian YOLOv8 dengan modul Ghost dan CBAM, dikombinasikan dengan ByteTrack untuk menghitung buah dari video dan dibandingkan dengan YOLOX dan NanoDet serta pelacak Motpy dan FairMOT. Kombinasi YOLO-TGI-S dan ByteTrack memperoleh R² 0,93 dan RMSE 9,17 terhadap hitungan manual, sedangkan YOLO-TGI-N memiliki FLOPs 2,05 G dengan mAP deteksi daun dan buah 0,72.

Catatan verifikasi data: ukuran dataset ada pada bagian "Field data collection and preprocessing"; angka detektor pada Tabel 1; angka penghitungan pada Tabel 2 dan bagian "Fruit counting results". Pernyataan kecepatan dua kali YOLOX dan 2,5 kali NanoDet berasal dari teks dan abstrak, bukan dihitung ulang. Teks ekstraksi terbaca baik dan tabel terbaca utuh, tetapi gambar tidak tersedia. Jumlah video, durasi, jumlah buah per video, kultivar tomat, dan perincian per kelas pada mAP tidak dilaporkan di teks utama (makalah merujuk pada materi tambahan).
