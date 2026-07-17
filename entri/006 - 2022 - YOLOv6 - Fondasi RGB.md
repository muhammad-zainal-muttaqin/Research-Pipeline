# 006 - YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022yolov6` |
| Judul asli | YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications |
| Penulis | Chuyi Li, Lulu Li, Hongliang Jiang, Kaiheng Weng, Yifei Geng, Liang Li, dkk. (Meituan Inc.) |
| Tahun | 2022 |
| Venue | arXiv preprint arXiv:2209.02976 (laporan teknis) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2209.02976
- **Repositori kode resmi (Meituan):** https://github.com/meituan/YOLOv6
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications&sort=relevance

## Gambaran Umum

YOLOv6 adalah detektor objek satu tahap — model yang memprediksi lokasi dan kelas seluruh objek dalam satu kali evaluasi jaringan — yang dikembangkan tim Meituan dan dirilis sebagai laporan teknis pada September 2022. Alih-alih mengusulkan paradigma baru, makalah ini merancang ulang kerangka YOLO agar optimal pada perangkat keras produksi: kecepatan diukur pada GPU kelas menengah NVIDIA Tesla T4, arsitektur dipilih berbeda per ukuran model, dan kuantisasi (konversi bobot dan aktivasi menjadi integer 8 bit) menjadi bagian rancangan sejak awal.

Hasilnya lima model (N, T, S, M, L) dengan kombinasi akurasi-kecepatan terdepan pada COCO saat dirilis. YOLOv6-N mencapai 35,9% AP dengan *throughput* (citra per detik) 1234 FPS; YOLOv6-S mencapai 43,5% AP pada 495 FPS, melampaui YOLOv5-S, YOLOX-S, dan PP-YOLOE-S sekelasnya; versi terkuantisasinya mencapai 43,3% AP pada 869 FPS.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv4 (bab 004) merapikan kerangka detektor menjadi *backbone*, *neck*, dan *head*, lini YOLO berkembang melalui YOLOv5, YOLOX (bab 005), PP-YOLOE, dan YOLOv7. Namun industri menuntut hal lain dari tolok ukur: latensi rendah pada perangkat spesifik, kuantisasi mudah, dan beberapa ukuran model. Penulis mengidentifikasi lima celah:

1. Reparameterisasi struktural — melatih jaringan dalam bentuk bercabang lalu meleburnya menjadi konvolusi tunggal saat inferensi, dipopulerkan RepVGG — belum dimanfaatkan baik pada deteksi; arsitektur jalur tunggalnya juga tumbuh eksplosif biayanya bila diperbesar.
2. Kuantisasi model berbasis reparameterisasi mudah merusak akurasi karena konfigurasinya berbeda antara pelatihan (bercabang) dan inferensi (lebur).
3. Latensi detektor sebelumnya umumnya diukur pada GPU mahal seperti V100, bukan GPU produksi seperti Tesla T4.
4. Strategi penetapan label dan fungsi loss mutakhir perlu diverifikasi ulang untuk tiap arsitektur.
5. Perbaikan yang menambah biaya pelatihan tetapi tidak menambah biaya inferensi — misalnya distilasi pengetahuan — dapat diterima industri dan layak dieksploitasi.

## Ide Utama

Gagasan inti YOLOv6 adalah merancang ulang kerangka YOLO dengan satu kriteria: setiap komponen dipilih berdasarkan bukti ablasi, dan arsitektur boleh berbeda antar-ukuran. Model kecil memakai *backbone* jalur tunggal berbasis reparameterisasi karena paling cepat pada perangkat nyata; model besar memakai blok multi-cabang yang lebih hemat parameter. Semua teknik yang menaikkan akurasi tanpa menambah biaya inferensi — penetapan label TAL, fungsi loss yang tepat, distilasi diri, pelatihan lebih lama — dipakai, dan kuantisasi diperbaiki dari sisi pelatihan agar model INT8 tetap akurat.

## Cara Kerja Langkah demi Langkah

### Gambaran Alur Data

*Backbone* adalah jaringan ekstraksi fitur yang menurunkan citra 640×640 piksel menjadi beberapa peta fitur yang semakin kecil. *Neck* menggabungkan fitur dangkal (kaya informasi posisi) dengan fitur dalam (kaya semantik) menjadi piramida fitur multi-skala. *Head* menghasilkan prediksi kelas dan kotak objek dari fitur gabungan tersebut.

```
                ALUR DATA YOLOv6 (model N/T/S; masukan 640x640)

 citra 640 x 640
      |
      v
+------------------------------------------------------------+
| BACKBONE - EfficientRep                                    |
| pelatihan : RepBlock = tumpukan blok RepVGG bercabang      |
| inferensi : tiap blok dilebur jadi RepConv (conv 3x3+ReLU) |
+------------------------------------------------------------+
      | peta fitur multi-skala
      v
+------------------------------------------------------------+
| NECK - Rep-PAN                                             |
| topologi PAN (agregasi atas-bawah + bawah-atas),           |
| blok CSP diganti RepBlock (model besar: CSPStackRep)       |
+------------------------------------------------------------+
      | fitur gabungan tiap skala
      v
+------------------------------------------------------------+
| HEAD - Efficient Decoupled Head (anchor-free)              |
| satu conv 3x3 bersama, lalu dua cabang:                    |
|   +-- klasifikasi -> skor kelas per titik                  |
|   +-- regresi     -> jarak titik ke 4 sisi kotak           |
+------------------------------------------------------------+
```

Diagram di atas menegaskan bahwa blok bercabang hanya ada saat pelatihan, lalu dilebur menjadi konvolusi tunggal untuk inferensi. Keluaran *head* tiap skala berupa skor kelas per titik dan empat jarak ke sisi-sisi kotak objek.

### Backbone: EfficientRep dan CSPStackRep

Untuk model kecil (N/T/S), backbone EfficientRep dibangun dari RepBlock: tumpukan blok gaya RepVGG yang saat pelatihan bercabang tiga (konvolusi 3×3, konvolusi 1×1, dan koneksi identitas), masing-masing diikuti *batch normalization* (lapisan yang menormalkan aktivasi agar stabil). Setelah pelatihan, ketiga cabang yang memperkaya gradien ini dilebur menjadi satu konvolusi 3×3 setara yang disebut RepConv, diikuti aktivasi ReLU.

```
  REPARAMETERISASI STRUKTURAL SATU BLOK (gaya RepVGG)

  saat pelatihan (3 cabang)       saat inferensi (1 jalur)

        masukan                         masukan
   +------+-------+                         |
 conv3x3 conv1x1 identitas             conv 3x3 tunggal
   |      |       |                   (ketiga cabang dan
   +------+-------+                    batchnorm dilebur)
       jumlah                             |
         |                             keluaran
      keluaran
```

Peleburan ini tepat secara matematis: konvolusi 1×1 dan identitas setara dengan konvolusi 3×3 berkernel *padding*, lalu dijumlahkan, dan konvolusi 3×3 jalur tunggal sangat efisien pada GPU umum. Namun pada model besar, parameter dan biaya komputasinya tumbuh eksplosif, sehingga M dan L memakai CSPStackRep Block: tumpukan sub-blok berisi dua RepConv dengan koneksi residual (jalan pintas yang menjumlahkan masukan dan keluaran blok), dibungkus koneksi CSP (*Cross Stage Partial*: peta fitur dibagi dua, satu melewati blok dan satu dilewatkan langsung, lalu digabung kembali) untuk memangkas komputasi tanpa kehilangan keragaman gradien.

### Neck: Rep-PAN

Neck YOLOv6 mengadopsi topologi PAN (*Path Aggregation Network*) dari YOLOv4 dan YOLOv5: piramida fitur dengan jalur agregasi dua arah (dari fitur dalam ke dangkal dan sebaliknya), sehingga tiap skala memuat semantik dan detail posisi. Rep-PAN berbeda dari PAN YOLOv5 pada blok pembangunnya: blok CSP diganti RepBlock (model kecil) atau CSPStackRep Block (model besar).

### Head: Efficient Decoupled Head dan Anchor-Free

*Decoupled head* adalah head yang memisahkan cabang klasifikasi dan cabang regresi kotak; head YOLOv5 sebaliknya bersifat *coupled* (kedua tugas berbagi parameter). FCOS dan YOLOX menambahkan dua konvolusi 3×3 pada tiap cabang; YOLOv6 menyederhanakannya lewat strategi *hybrid-channel* (satu konvolusi 3×3 di tengah, lebarnya mengikuti backbone dan neck), sehingga latensi turun dengan penurunan akurasi minimal.

Head ini juga bersifat *anchor-free*: prediksi bukan offset terhadap *anchor box* (kotak acuan berukuran tetap yang dirancang sebelumnya), melainkan jarak dari sebuah titik (*anchor point*) ke empat sisi kotak objek. Dekode lebih sederhana dan pasca-pemrosesan lebih cepat karena kandidat keluaran berkurang hingga sepertiga.

### Penetapan Label: TAL

*Label assignment* adalah proses saat pelatihan untuk menentukan prediksi mana yang bertanggung jawab (contoh positif) atas setiap objek kebenaran. Versi awal YOLOv6 memakai SimOTA (strategi warisan YOLOX yang merumuskan penetapan label sebagai masalah transport optimal), tetapi SimOTA memperlambat dan tidak jarang mendestabilkan pelatihan. Sebagai gantinya dipakai TAL (*Task Alignment Learning*, dari TOOD): metrik tunggal gabungan skor klasifikasi dan kualitas kotak menjadi kriteria penetapan, sehingga ketidakselarasan kedua tugas berkurang.

### Fungsi Loss

Untuk loss klasifikasi, YOLOv6 memilih VFL (*Varifocal Loss*) setelah menguji Focal Loss, Poly Loss, dan QFL; VFL adalah turunan Focal Loss (modifikasi *cross-entropy* yang menekan kontribusi contoh mudah) yang memperlakukan contoh positif dan negatif secara asimetris sehingga sinyal belajarnya seimbang. Untuk loss regresi dipakai keluarga loss IoU. IoU (*Intersection over Union*) adalah rasio luas irisan terhadap gabungan dua kotak; GIoU tetap memberi gradien pada kotak tak beririsan, sedangkan SIoU menambahkan penalti sudut, jarak pusat, dan bentuk. YOLOv6 memakai SIoU untuk N dan T, dan GIoU untuk sisanya. DFL (*Distribution Focal Loss*) memodelkan posisi tiap sisi kotak sebagai distribusi probabilitas diskrit 17 nilai, bukan satu angka, sehingga lokalisasi batas yang kabur membaik; karena keluarannya 17 kali lebih besar, DFL hanya dipakai pada M dan L. Loss objektivitas (penalti untuk kotak berkualitas rendah, dari FCOS dan YOLOX) dicoba tetapi dibuang karena menurunkan akurasi.

### Distilasi Diri dan Durasi Pelatihan

*Knowledge distillation* melatih model murid agar meniru keluaran model guru dengan meminimalkan divergensi KL (ukuran selisih dua distribusi probabilitas). YOLOv6 memakai distilasi diri: gurunya adalah arsitektur yang sama yang sudah dilatih sebelumnya, sehingga tanpa biaya inferensi tambahan. Distilasi diterapkan pada klasifikasi dan, berkat DFL yang menghasilkan distribusi, juga pada regresi. Bobot loss distilasi meluruh mengikuti kurva kosinus: label lunak guru lebih mudah dipelajari di awal, label keras lebih bermanfaat di akhir. Durasi pelatihan juga diperpanjang dari 300 menjadi 400 epoch.

### Kuantisasi untuk Penerapan

PTQ (*post-training quantization*) mengkuantisasi model terlatih memakai himpunan kalibrasi kecil; QAT (*quantization-aware training*) menyisipkan kuantisasi tiruan selama pelatihan. Keduanya bermasalah pada model berbasis reparameterisasi karena struktur pelatihan dan inferensinya berbeda. YOLOv6 memperbaikinya dengan tiga langkah: (1) pelatihan memakai RepOptimizer, yang melakukan reparameterisasi pada gradien tiap langkah optimasi, sehingga bobot ramah PTQ; (2) analisis sensitivitas menemukan enam lapisan paling terdampak untuk dibiarkan berhitung dalam *float*; (3) bila PTQ belum cukup, QAT dibangun di atas RepOptimizer ditambah distilasi per kanal (guru berupa model FP32-nya sendiri) dan optimasi graf komputasi.

## Eksperimen dan Hasil

Model dilatih pada COCO 2017 (sekitar 118 ribu citra, 80 kelas) dan dievaluasi pada 5.000 citra validasi. Metrik utamanya AP (*Average Precision* COCO: rata-rata presisi pada ambang IoU 0,50–0,95). Pelatihan memakai SGD bermomentum dengan peluruhan kosinus, *exponential moving average* (rata-rata bergerak bobot), dan augmentasi Mosaic-Mixup, selama 300 epoch tanpa pra-pelatihan pada 8 GPU A100. Kecepatan diukur pada satu Tesla T4 dengan TensorRT presisi FP16, sebagai latensi (*batch* 1) dan *throughput* (*batch* 32).

| Model | AP | AP50 | FPS (*batch* 1) | FPS (*batch* 32) | Latensi | Parameter | FLOPs |
|---|---|---|---|---|---|---|---|
| YOLOv6-N | 35,9% | 51,2% | 802 | 1234 | 1,2 ms | 4,3 M | 11,1 G |
| YOLOv6-T | 40,3% | 56,6% | 449 | 659 | 2,2 ms | 15,0 M | 36,7 G |
| YOLOv6-S | 43,5% | 60,4% | 358 | 495 | 2,8 ms | 17,2 M | 44,2 G |
| YOLOv6-M | 49,5% | 66,8% | 179 | 233 | 5,6 ms | 34,3 M | 82,2 G |
| YOLOv6-L | 52,5% | 70,0% | 98 | 121 | 10,2 ms | 58,5 M | 144,0 G |

YOLOv6-N melampaui YOLOv5-N (28,0% AP) sebesar 7,9 poin dan YOLOv7-Tiny masukan 416 (33,3% AP) sebesar 2,6 poin, sekaligus menjadi yang tercepat. YOLOv6-S lebih akurat 3,0 poin dari YOLOX-S (40,5% AP) dan 0,4 poin dari PP-YOLOE-S (43,1% AP) dengan kecepatan lebih tinggi. YOLOv6-M melampaui YOLOv5-M (45,4% AP) sebesar 4,2 poin pada kecepatan sebanding, dan varian YOLOv6-L-ReLU (51,7% AP, 8,8 ms) melampaui YOLOX-L, PP-YOLOE-L, dan YOLOv7 pada akurasi dan kecepatan sekaligus.

Ablasi membuktikan sumbangan tiap komponen. Dari baseline YOLOv5-N (28,0% AP), penambahan head terpisah memberi 29,4%; pelepasan *anchor* memberi 30,7% sekaligus mempercepat 51% karena dimensi keluaran tiga kali lebih kecil; EfficientRep dan Rep-PAN memberi 34,3% dengan 21% lebih cepat; dan head *hybrid-channel* menutup pada 34,5% AP dengan 1242 FPS. Untuk penetapan label, TAL mencapai 35,0% AP pada YOLOv6-N, di atas SimOTA (34,5%) dan ATSS (32,5%). Distilasi diri menaikkan YOLOv6-L dari 51,0% menjadi 52,3% AP, dan perpanjangan ke 400 epoch menambah 0,4–0,6 poin pada model kecil.

Hasil kuantisasi menunjukkan mengapa penanganan khusus diperlukan: PTQ polos pada YOLOv6-S menjatuhkan AP dari 42,4% menjadi 35,0%, sedangkan dengan RepOptimizer menjadi 40,9%. Jalur QAT penuh mencapai 43,3% AP pada 869 FPS — hanya 0,1 poin di bawah model FP16 (43,4%) tetapi 60% lebih cepat (541 FPS).

## Kelebihan dan Keterbatasan

Kelebihan YOLOv6 adalah orientasi penerapannya yang konsisten: pengukuran pada GPU kelas produksi, rancangan berbeda per skala, jalur kuantisasi yang menjaga akurasi, dan pemilihan komponen melalui ablasi terdokumentasi.

Keterbatasannya: secara konseptual, kontribusinya adalah integrasi rekayasa atas teknik yang sudah ada, bukan paradigma baru. Dari sisi rekayasa, angka kecepatan terikat pada TensorRT dan Tesla T4; model terkuantisasi diuji dengan TensorRT 8 sedangkan model lain dengan TensorRT 7 — diakui penulis sendiri — sehingga perbandingan lintas makalah perlu kehati-hatian. Distilasi regresi bergantung DFL yang hanya dipakai M dan L, sehingga model kecil tidak memperoleh manfaat penuhnya; model besar justru kembali ke konvolusi biasa dengan SiLU, sehingga manfaat reparameterisasi tidak seragam antar-skala.

## Kaitan dengan Bab Lain

Formulasi deteksi satu tahap diwarisi dari [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md). Dekomposisi backbone–neck–head, pola CSP, topologi PAN, dan augmentasi Mosaic diambil dari [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md). Paradigma *anchor-free*, head terpisah, dan SimOTA diwarisi dari [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md), meskipun SimOTA kemudian digantikan TAL. YOLOv6 sezaman dengan [bab 007 (YOLOv7)](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md): keduanya memakai reparameterisasi struktural, tetapi YOLOv6 membedakan diri lewat rancangan per skala model dan penanganan kuantisasi yang eksplisit. Garis penyempurnaan ini dilanjutkan [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `li2022yolov6`. Ringkasan yang aman dikutip: "YOLOv6 (Li dkk., 2022) adalah detektor objek satu tahap berorientasi industri dari Meituan dengan backbone reparameterisasi EfficientRep, neck Rep-PAN, head anchor-free efisien, serta pelatihan berbasis TAL, Varifocal Loss, dan distilasi diri. YOLOv6-S mencapai 43,5% AP pada 495 FPS di Tesla T4; versi INT8-nya mencapai 43,3% AP pada 869 FPS."

Catatan verifikasi sebelum sitasi formal: (1) AP YOLOv6-L dilaporkan 52,3% pada abstrak tetapi 52,5% pada Tabel 1 naskah; (2) angka FPS bergantung versi TensorRT dan ukuran *batch* (model terkuantisasi diuji dengan TensorRT 8, model lain TensorRT 7); (3) makalah memuat dua rilis (v1.0, v2.0) dengan hasil kuantisasi berbeda; (4) venue berupa laporan teknis arXiv tanpa penelaahan sejawat.
