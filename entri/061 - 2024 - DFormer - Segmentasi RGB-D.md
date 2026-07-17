# 061 - DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `yin2024dformer` |
| Judul asli | DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation |
| Penulis | Bowen Yin, Xuying Zhang, Zhongyu Li, Li Liu, Ming-Ming Cheng, Qibin Hou |
| Tahun | 2024 |
| Venue | International Conference on Learning Representations (ICLR) |
| Tema | Segmentasi RGB-D |

## Tautan Akses

- arXiv (PDF dan HTML): https://arxiv.org/abs/2309.09668
- Repositori kode resmi: https://github.com/VCIP-RGBD/DFormer
- Google Scholar: https://scholar.google.com/scholar?q=DFormer%3A%20Rethinking%20RGBD%20Representation%20Learning%20for%20Semantic%20Segmentation

## Gambaran Umum

DFormer adalah kerangka pra-pelatihan RGB-D untuk tugas segmentasi, diperkenalkan oleh kelompok VCIP Universitas Nankai pada ICLR 2024. Makalah ini menolak kebiasaan yang berlaku saat itu, yaitu memakai *backbone* (jaringan penyandi fitur) yang dipra-latih pada citra RGB saja lalu menambahkan modul fusi RGB-D di tahap penalaan (*finetuning*). Sebagai gantinya, interaksi antara citra RGB dan peta kedalaman dipelajari sejak pra-pelatihan pada ImageNet-1K, memakai pasangan citra-kedalaman yang peta kedalamannya dihasilkan oleh model estimasi kedalaman. Backbone yang dihasilkan, beserta blok penyusun baru bernama blok RGB-D, diturunkan ke tugas segmentasi semantik RGB-D dan deteksi objek menonjol (*salient object detection*) dengan dekoder ringan. Hasilnya, model terbesar DFormer-L mencapai 57,2% mIoU (*mean Intersection over Union*, metrik rata-rata irisan-gabungan per kelas) pada NYUDepthv2 dengan 39,0 juta parameter dan 65,7G FLOPs (*floating point operations*, ukuran biaya komputasi satu kali inferensi), lebih akurat sekaligus kurang dari separuh biaya komputasi metode terbaik sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi semantik RGB-D adalah pelabelan kelas pada setiap piksel dengan memanfaatkan dua modalitas masukan: citra RGB yang membawa warna dan tekstur, serta peta kedalaman yang membawa geometri tiga dimensi berupa jarak setiap piksel ke kamera. Sebelum DFormer, pendekatan dominan — misalnya CMX (bab [058](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)) dan TokenFusion — memakai dua backbone terpisah yang sama-sama dipra-latih pada citra RGB ImageNet, satu untuk RGB dan satu untuk kedalaman, lalu membangun modul fusi di antara keduanya saat penalaan pada data RGB-D.

Penulis DFormer menunjuk tiga masalah pada pola tersebut. Pertama, backbone dipra-latih dengan masukan satu citra, tetapi saat penalaan menerima pasangan citra-kedalaman; ketidakcocokan ini menimbulkan pergeseran distribusi representasi, dan peta kedalaman disandikan oleh bobot yang tidak pernah melihat geometri tiga dimensi. Kedua, interaksi antarmodalitas yang padat di dalam backbone saat penalaan dapat merusak distribusi representasi hasil pra-pelatihan RGB. Ketiga, dua backbone penuh berarti biaya parameter dan komputasi hampir dua kali lipat dibanding metode RGB biasa. Ketiga masalah ini dilacak ke satu sumber: kedalaman tidak pernah dilibatkan sejak pra-pelatihan.

## Ide Utama

Gagasan inti DFormer dapat dinyatakan dalam satu kalimat: pindahkan fusi RGB-D dari tahap penalaan ke tahap pra-pelatihan. Secara mekanis, backbone dirancang sejak awal menerima dua masukan — citra RGB dan peta kedalaman — dan setiap blok penyusunnya memuat mekanisme interaksi antarmodalitas. Backbone ini dipra-latih pada ImageNet-1K dengan tugas klasifikasi citra, sama seperti backbone RGB biasa, tetapi setiap citra dilengkapi peta kedalaman yang diprediksi oleh model estimasi kedalaman AdaBins, sehingga tersedia pasangan citra-kedalaman berskala besar tanpa sensor baru. Gagasan pendampingnya adalah penghematan kanal: karena kedalaman hanya memuat jarak, bukan semantik kaya, kedalaman cukup disandikan dengan sebagian kecil kanal dibanding RGB. Keluaran pra-pelatihan adalah backbone yang representasinya sudah sadar kedalaman, sehingga di hilir cukup ditambah dekoder ringan tanpa modul fusi tambahan apa pun.

## Cara Kerja Langkah demi Langkah

### Penyandian hierarkis dan *stem*

Masukan berupa citra RGB dan peta kedalaman berukuran spasial H×W masing-masing melewati *stem* (lapisan awal) sendiri yang terdiri dari dua konvolusi 3×3 dengan *stride* (langkah geser) 2, sehingga resolusi langsung turun ke seperempat. Encoder tersusun atas empat tahap yang menghasilkan fitur multi-skala pada resolusi 1/4, 1/8, 1/16, dan 1/32 dari citra asal. Setiap tahap berisi tumpukan blok RGB-D; di antara dua tahap, dua konvolusi 3×3 *stride* 2 menurunkan resolusi fitur RGB dan fitur kedalaman secara terpisah.

### Blok RGB-D: tiga cabang fitur

Setiap blok RGB-D menerima fitur RGB dan fitur kedalaman, lalu menghitung tiga cabang yang digabungkan melalui konkatenasi dan proyeksi linear untuk memperbarui kedua aliran fitur. Tiga cabang itu adalah GAA, LEA, dan Base, dijelaskan berikut.

### GAA: kesadaran global lewat *query* yang digabung

*Global awareness attention* (GAA) adalah perhatian (*attention*) yang menautkan setiap lokasi dengan seluruh adegan. Dalam mekanisme *self-attention* standar, matriks *query* (Q), *key* (K), dan *value* (V) semuanya berasal dari fitur yang sama dan biayanya tumbuh kuadratik terhadap jumlah piksel. GAA mengubah dua hal. Pertama, Q dihitung dari konkatenasi fitur RGB dan fitur kedalaman, lalu di-*pooling* adaptif ke ukuran tetap k×k (konfigurasi terbaik 7×7), sehingga jumlah *query* konstan dan kompleksitas turun. Kedua, K dan V tetap diambil dari fitur RGB saja. Jadi, Q = Linear(Pool([X_rgb, X_d])), sedangkan K = Linear(X_rgb) dan V = Linear(X_rgb). Skor perhatian Q·K kemudian diterapkan ke V dan hasilnya di-*upsampling* bilinear kembali ke ukuran spasial semula. Interpretasinya: kedalaman ikut menentukan "dari mana" perhatian diajukan, tetapi isi fitur yang dipindahkan tetap milik RGB. Uji ablasi makalah menunjukkan fusi kedalaman ke K dan V tidak menambah akurasi, hanya menambah komputasi.

### LEA: bobot kedalaman sebagai pengali fitur RGB

*Local enhancement attention* (LEA) menangkap petunjuk lokal dari kedalaman. Fitur kedalaman dilewatkan ke transformasi linear lalu konvolusi *depth-wise* (konvolusi yang bekerja per kanal secara terpisah) berkernel besar 7×7; hasilnya dipakai sebagai bobot perhatian yang mengalikan fitur RGB secara per elemen (hasil kali Hadamard): X_LEA = DConv7×7(Linear(X_d)) ⊙ Linear(X_rgb). Dasar rancangannya adalah observasi bahwa piksel berdekatan dengan nilai kedalaman serupa biasanya milik objek yang sama, sehingga bobot dari kedalaman menanamkan geometri ke fitur RGB. Cabang ketiga, Base, menerapkan pola yang sama tetapi hanya pada fitur RGB (DConv(Linear(X_rgb)) ⊙ Linear(X_rgb)) untuk menjaga informasi penampakan. Pada DFormer-S, mencabut Base menurunkan mIoU dari 53,6% ke 52,1%, mencabut GAA ke 52,3%, dan mencabut LEA ke 52,6% — ketiganya terbukti berkontribusi. Ablasi juga menunjukkan hasil kali Hadamard (53,6%) mengungguli konkatenasi (53,3%) dan penjumlahan (53,1%) sebagai cara fusi di LEA.

### Rasio kanal kedalaman

Karena kedalaman membawa informasi lebih miskin daripada RGB, lebar kanal aliran kedalaman disetel lebih kecil. Kurva ablasi menunjukkan kinerja praktis jenuh ketika rasio kanal kedalaman terhadap RGB melampaui 1/2, sementara biaya komputasi terus naik; karena itu rasio baku dipilih 1/2. Inilah salah satu sumber efisiensi DFormer dibanding dua backbone penuh. Tersedia empat varian ukuran dengan arsitektur sama: DFormer-T, -S, -B, dan -L.

### Pra-pelatihan RGB-D pada ImageNet-1K

Model estimasi kedalaman AdaBins dijalankan pada seluruh ImageNet-1K untuk menghasilkan peta kedalaman per citra. Di atas encoder dipasang kepala klasifikasi: fitur RGB tahap terakhir diratakan dan masuk klasifier dengan fungsi rugi *cross-entropy*. Pelatihan berjalan 300 *epoch* (satu epoch = satu putaran penuh data latih) dengan pengoptimal AdamW, laju pembelajaran 1e-3, *weight decay* (penalti yang menyusutkan bobot agar tidak overfitting) 5e-2, dan ukuran *batch* 1024, mengikuti resep ConvNeXt.

### Dekoder hilir yang ringan

Untuk segmentasi semantik, DFormer memakai kepala Hamburger yang ringan (dipinjam dari SegNeXt) yang mengagregasi fitur dari tiga tahap terakhir. Hal yang tidak lazim: dekoder hanya menerima fitur RGB dari encoder, tanpa fitur kedalaman dan tanpa modul fusi. Ablasi pada DFormer-B menunjukkan memakai hanya fitur RGB memberi 55,6% mIoU dengan 29,5M parameter, sementara memakai kedua modalitas memberi 55,5% dengan 30,8M parameter — fitur RGB keluaran backbone pra-latih RGB-D sudah memuat petunjuk geometri yang diperlukan.

Diagram berikut merangkum alur data DFormer dari masukan hingga prediksi.

```
  citra RGB                     peta kedalaman
      │                              │
  stem: 2x conv3x3 s2           stem: 2x conv3x3 s2
      │                              │
  ┌───▼──────────────── Tahap 1 s.d. 4 ──────────▼───┐
  │  tiap tahap: tumpukan Blok RGB-D                 │
  │   X_rgb ──┬─► GAA: Q=Pool([X_rgb,X_d]) 7x7       │
  │           │        K,V = Linear(X_rgb)           │
  │   X_d   ──┼─► LEA: DConv7x7(X_d) ⊙ Linear(X_rgb) │
  │           └─► Base: DConv(X_rgb) ⊙ Linear(X_rgb) │
  │                 │ gabung + proyeksi linear       │
  │                 ▼                                │
  │        X_rgb dan X_d diperbarui                  │
  │  antar-tahap: conv3x3 s2 (resolusi 1/4..1/32)    │
  └───────────────────────┬──────────────────────────┘
                          ▼
  Pra-latih: klasifikasi ImageNet-1K citra+kedalaman (300 epoch)
                          ▼
  Dekoder Hamburger (hanya fitur RGB tahap 2-4) ► peta segmentasi HxW
```

Diagram menegaskan dua hal yang membedakan DFormer: interaksi RGB-D terjadi di dalam blok backbone (bukan di modul fusi luar), dan jalur kedalaman berhenti di encoder — dekoder hanya membaca fitur RGB.

## Eksperimen dan Hasil

Uji utama dilakukan pada dua tugas. Pertama, segmentasi semantik RGB-D pada NYUDepthv2 (adegan dalam ruang, input 480×640) dan SUN-RGBD (input 530×730), dengan metrik mIoU. Kedua, deteksi objek menonjol RGB-D pada lima dataset (DES, NLPR, NJU2K, STERE, SIP) dengan metrik S-measure, MAE, F-measure, dan E-measure.

Hasil utama pada NYUDepthv2: DFormer-L mencapai 57,2% mIoU dengan 39,0M parameter dan 65,7G FLOPs. Pembanding terkuat saat itu, CMNext (MiT-B4), memperoleh 56,9% dengan 119,6M parameter dan 131,9G FLOPs — artinya DFormer-L lebih akurat 0,3 poin dengan sekitar sepertiga parameter dan separuh komputasi. Pada SUN-RGBD, DFormer-L memperoleh 52,5% mIoU, melampaui CMNext (51,9%) dan CMX MiT-B5 (52,4% dengan 217,6G FLOPs). Di sisi ringan, DFormer-T mencapai 51,8% mIoU pada NYUDepthv2 hanya dengan 6,0M parameter dan 11,8G FLOPs — melampaui ShapeConv (51,3%) yang memakai 86,8M parameter. Untuk deteksi objek menonjol, DFormer-T menyamai SPNet dengan biaya di bawah 10% (5,9M parameter dan 4,5G FLOPs berbanding 150,3M dan 68,1G).

Ablasi membuktikan penyebab keunggulan. Mengganti pra-pelatihan RGB-D dengan pra-pelatihan RGB biasa (kedalaman diganti citra RGB) menurunkan DFormer-B dari 55,6% ke 53,3% mIoU — selisih 2,3 poin murni dari cara pra-pelatihan. Sebaliknya, menerapkan pra-pelatihan RGB-D ala DFormer ke CMX menaikkan CMX sekitar 1,4 poin, tetapi DFormer-L tetap unggul jauh, menunjukkan blok RGB-D ikut berperan. Uji lintas modalitas pada RGB-T (MFNet) dan RGB-LiDAR (KITTI-360) juga membaik dengan pra-pelatihan RGB-D (misalnya 60,3% berbanding 59,5% mIoU pada MFNet), walau peningkatannya lebih kecil.

## Kelebihan dan Keterbatasan

Kelebihan utama DFormer adalah pergeseran paradigma yang terukur: fusi sejak pra-pelatihan menghapus ketidakcocokan distribusi representasi, memangkas kebutuhan dua backbone penuh, dan menyederhanakan dekoder menjadi hanya pembaca fitur RGB. Rasio kanal kedalaman 1/2 dan *query* GAA yang di-*pooling* tetap menjaga biaya komputasi, sehingga kurva akurasi-terhadap-biaya berada di atas seluruh pembanding pada kedua dataset segmentasi. Generalisasi ke modalitas lain (termal, LiDAR) menunjukkan kerangka ini tidak terkunci pada kedalaman.

Keterbatasannya, pertama, pra-pelatihan ulang pada ImageNet-1K citra-kedalaman adalah biaya awal yang tidak kecil (300 epoch) dan tidak dapat digantikan oleh bobot ImageNet RGB yang sudah umum beredar; dari sisi rekayasa, pengguna harus memakai bobot pra-latih khusus yang disediakan penulis. Kedua, kualitas peta kedalaman pra-latih bergantung pada estimasi AdaBins, bukan sensor nyata; secara konseptual, kesalahan sistematis estimator ikut terpelihara dalam bobot. Ketiga, peningkatan pada modalitas non-kedalaman lebih kecil daripada pada RGB-D, dan penulis sendiri menyatakan perluasan pra-pelatihan ke modalitas lain masih menjadi pekerjaan lanjutan. Keempat, metrik mIoU tertinggi dilaporkan dengan inferensi multi-skala dan pembalikan, yang menambah biaya pengujian di luar angka FLOPs tabel.

## Kaitan dengan Bab Lain

DFormer menutup satu garis perkembangan fusi RGB-D yang dibangun bab-bab sebelumnya. FuseNet (bab [051](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)) memulai fusi dua aliran dengan penjumlahan fitur; RedNet, RDFNet, dan ACNet (bab [052](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md), [053](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md), [054](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)) memperdalam fusi ke dalam arsitektur konvolusi; SA-Gate, ESANet, dan ShapeConv (bab [055](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md), [056](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md), [057](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)) memperhalus mekanisme gerbang dan operator sadar-kedalaman. Semuanya tetap berpijak pada backbone pra-latih RGB. CMX (bab [058](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)) membawa fusi ke ranah *transformer* dua cabang dan menjadi pembanding utama yang dikalahkan DFormer dengan biaya jauh lebih rendah. Kontribusi DFormer terhadap silsilah ini adalah menunjukkan bahwa lokus fusi yang paling efektif bukan di modul tambahan, melainkan di dalam bobot pra-latih itu sendiri — pelajaran yang relevan bagi rancangan fusi RGB-D pada detektor objek di klaster berikutnya.

## Poin untuk Sitasi

Kunci BibTeX: `yin2024dformer`. Ringkasan aman kutip: DFormer (ICLR 2024) adalah kerangka pra-pelatihan RGB-D yang melatih backbone pada pasangan citra-kedalaman ImageNet-1K — kedalaman dihasilkan oleh estimator AdaBins — dengan blok RGB-D berisi modul GAA dan LEA. Model ini mencapai 57,2% mIoU pada NYUDepthv2 (DFormer-L, 39,0M parameter, 65,7G FLOPs) dan 52,5% pada SUN-RGBD, dengan dekoder ringan yang hanya membaca fitur RGB. Catatan verifikasi: seluruh angka di atas dikutip dari versi arXiv v2 (Februari 2024) dan sebaiknya dicocokkan dengan naskah prosiding ICLR final sebelum sitasi formal; nilai mIoU memakai inferensi multi-skala; angka peningkatan CMX dengan pra-pelatihan RGB-D ("sekitar 1,4%") dinyatakan penulis secara naratif, bukan angka tabel tunggal.
