# 009 - YOLOv10: Real-Time End-to-End Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024yolov10` |
| Judul asli | YOLOv10: Real-Time End-to-End Object Detection |
| Penulis | Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong Han, Guiguang Ding |
| Tahun | 2024 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2024) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF dan HTML gratis):** https://arxiv.org/abs/2405.14458
- **Kode sumber resmi (THU-MIG, Tsinghua):** https://github.com/THU-MIG/yolov10
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv10%3A%20Real-Time%20End-to-End%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv10%3A%20Real-Time%20End-to-End%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan YOLOv10, detektor objek satu tahap (memprediksi kotak objek langsung tanpa tahap pengusulan wilayah) yang menghilangkan *Non-Maximum Suppression* (NMS) dari alur inferensi: citra masuk, kotak objek beserta kelasnya langsung keluar, tanpa pasca-proses. Dua gagasan menopangnya. Pertama, *consistent dual assignments*: model dilatih dengan dua kepala prediksi — satu dengan penugasan satu-ke-banyak untuk supervisi kaya, satu dengan penugasan satu-ke-satu untuk inferensi tanpa NMS — yang diselaraskan oleh metrik pencocokan yang sama. Kedua, desain arsitektur holistik yang memangkas redundansi komputasi pada hampir semua komponen YOLO.

Pada tolok ukur COCO, YOLOv10-S mencapai 46,3% AP dengan latensi 2,49 milidetik — 1,8 kali lebih cepat daripada RT-DETR-R18 pada akurasi setara, dengan parameter dan komputasi 2,8 kali lebih kecil. YOLOv10-B juga memangkas 46% latensi dan 25% parameter terhadap YOLOv9-C pada performa sama. Makalah ini membuktikan detektor konvolusi satu tahap dapat bersifat *end-to-end* seperti detektor transformer tanpa mengorbankan kecepatan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv1 (bab 001), seluruh keluarga YOLO dilatih dengan penugasan label satu-ke-banyak: setiap objek kebenaran (*ground truth*) dipasangkan dengan banyak prediksi positif. Akibatnya, pada inferensi satu objek dilaporkan banyak kotak yang saling tumpang tindih, sehingga dibutuhkan NMS — prosedur yang membuang kotak berskor lebih rendah bila tumpang tindihnya melebihi ambang *Intersection over Union* (IoU, rasio luas irisan terhadap luas gabungan dua kotak). NMS menimbulkan tiga persoalan: latensi bertambah dan bergantung pada jumlah objek; hasil sensitif terhadap hiperparameter ambangnya; dan model tidak dapat diterapkan *end-to-end* (dari masukan langsung ke keluaran akhir) karena ada tahap non-diferensial di ujung alur.

Detektor transformer seperti DETR (bab 022) dan RT-DETR (bab 155) sudah bebas NMS melalui penugasan satu-ke-satu: tiap objek hanya dipasangkan ke satu prediksi. Namun, penugasan satu-ke-satu yang diterapkan langsung pada YOLO memberi supervisi lemah — konvergensi lambat dan akurasi rendah — sedangkan detektor transformer masih kalah efisien dari YOLO pada proses umpan-maju murni. Persoalan kedua bersifat arsitektural: komponen YOLO berkembang bertahap lintas generasi tanpa pemeriksaan menyeluruh, sehingga menyimpan redundansi komputasi. YOLOv10 menangani keduanya sekaligus.

## Ide Utama

Gagasan pertama: NMS adalah solusi pasca-proses untuk masalah yang ditimbulkan pelatihan satu-ke-banyak; solusi yang lebih langsung adalah melatih model agar hanya menghasilkan satu prediksi per objek tanpa kehilangan supervisi kaya. Caranya: dua kepala prediksi berbagi tubuh jaringan yang sama — kepala satu-ke-banyak hanya hidup saat pelatihan, kepala satu-ke-satu dilatih dengan metrik pencocokan yang sama bentuknya sehingga pilihannya selaras dengan sampel terbaik kepala pertama. Saat inferensi, kepala pertama dibuang: tanpa biaya tambahan, tanpa NMS.

Gagasan kedua: periksa setiap komponen YOLO dan potong komputasi yang tidak sebanding dengan sumbangannya pada akurasi. Kepala klasifikasi yang terlalu besar diperkecil, penurunan resolusi dan penambahan kanal dipisahkan, blok pada tahap redundan diganti blok ringkas, dan kapasitas yang hilang dipulihkan dengan konvolusi berkernel besar serta perhatian-diri parsial pada posisi yang murah.

## Cara Kerja Langkah demi Langkah

### Penugasan Ganda untuk Pelatihan Tanpa NMS

Istilah kuncinya adalah *label assignment* (penugasan label): aturan yang menentukan prediksi mana yang menjadi sampel positif untuk tiap objek kebenaran selama pelatihan, sehingga fungsi loss (fungsi kerugian yang diminimalkan) tahu prediksi mana yang harus diperbaiki. YOLOv8 — basis arsitektur YOLOv10 — memakai TAL (*Task-Aligned Learning*), penugasan satu-ke-banyak yang memilih beberapa sampel positif berdasarkan keselarasan skor klasifikasi dan kualitas kotak.

YOLOv10 menambahkan kepala kedua yang strukturnya identik dan memakai fungsi loss yang sama, tetapi penugasannya satu-ke-satu: untuk tiap objek, hanya prediksi berskor pencocokan tertinggi yang menjadi sampel positif (seleksi *top-1*). Seleksi top-1 ini terbukti menyamai kualitas *Hungarian matching* — pencocokan bipartit optimal yang dipakai DETR — dengan waktu pelatihan tambahan lebih kecil. Selama pelatihan, kedua kepala dioptimalkan bersama; *backbone* (jaringan pengekstraksi fitur) dan *neck* (modul penggabung fitur lintas skala) menerima supervisi kaya dari kepala satu-ke-banyak. Selama inferensi, kepala satu-ke-banyak dibuang, sehingga latensi identik dengan model berkepala tunggal.

### Metrik Pencocokan yang Konsisten

Kedua kepala menilai kecocokan prediksi–objek dengan metrik berbentuk sama: m(α,β) = s · p^α · IoU^β, dengan p skor klasifikasi, IoU ketepatan kotak, dan s prior spasial (bernilai 1 bila titik *anchor* — titik acuan prediksi pada peta fitur — berada di dalam wilayah objek, dan 0 bila tidak). Hiperparameter α dan β mengatur timbangan tugas klasifikasi terhadap regresi kotak; kepala satu-ke-banyak memakai α = 0,5 dan β = 6 sebagaimana TAL pada YOLOv8.

Bila kedua kepala memakai α dan β berbeda, prediksi terbaik menurut kepala satu-ke-satu belum tentu termasuk sampel positif terbaik kepala satu-ke-banyak, sehingga keduanya dioptimalkan ke arah yang tidak selaras. Penulis mengukur celah supervisi ini dengan jarak 1-Wasserstein (ukuran selisih dua distribusi) antara target klasifikasi kedua cabang, dan menunjukkan celah itu minimum bila metriknya konsisten: α_o2o = r·α_o2m dan β_o2o = r·β_o2m. Dengan r = 1, kedua metrik sama persis, sehingga sampel terbaik kepala satu-ke-banyak otomatis menjadi pilihan kepala satu-ke-satu. Verifikasi empirisnya: dengan metrik konsisten, pasangan satu-ke-satu lebih sering berada dalam peringkat top-1/5/10 hasil satu-ke-banyak.

Alur pelatihan dua kepala dan inferensi satu kepala:

```
PELATIHAN (kedua head aktif, berbagi backbone dan neck)

                ┌────────────┐
                │   citra    │
                └─────┬──────┘
                      ▼
              backbone + neck
                │           │
                ▼           ▼
        head one-to-many  head one-to-one
        (TAL, banyak +)   (top-1, satu +)
                │           │
                ▼           ▼
            loss o2m  +   loss o2o  ──►  loss total

INFERENSI (head one-to-many dibuang, tanpa NMS)

  citra ─► backbone + neck ─► head one-to-one ─► kotak + kelas
```

Pada fase inferensi, keluaran kepala satu-ke-satu langsung menjadi hasil deteksi akhir tanpa pemrosesan lanjutan.

### Kepala Klasifikasi yang Ringan

Dalam YOLO, kepala klasifikasi dan kepala regresi kotak lazimnya berstruktur sama. Pengukuran penulis menemukan ketimpangan: pada YOLOv8-S, kepala klasifikasi menelan 5,95 GFLOPs dan 1,51 juta parameter — 2,5 dan 2,4 kali lipat biaya kepala regresi (2,34 GFLOPs; 0,64 juta parameter). FLOPs (*floating-point operations*) adalah jumlah operasi hitung titik mengambang, satuan baku biaya komputasi. Analisis galat menunjukkan regresi kotak lebih menentukan performa: menghilangkan seluruh galat regresi menaikkan AP jauh lebih tinggi daripada menghilangkan seluruh galat klasifikasi. Karena itu, kepala klasifikasi aman diperkecil menjadi dua konvolusi *depthwise* 3×3 (konvolusi yang mengolah tiap kanal secara terpisah, jauh lebih murah daripada konvolusi biasa) diikuti satu konvolusi 1×1.

### Penurunan Resolusi Terpisah Spasial–Kanal

Lapisan *downsampling* pada YOLO biasanya berupa konvolusi 3×3 berlangkah 2 yang sekaligus membelah dua resolusi spasial (H×W menjadi H/2×W/2) dan menggandakan kanal (C menjadi 2C), dengan biaya O(9/2·HWC²) dan parameter O(18C²). YOLOv10 memisahkan kedua operasi: konvolusi *pointwise* (konvolusi 1×1 yang mencampur antar-kanal tanpa mengubah resolusi) menaikkan kanal lebih dahulu, lalu konvolusi *depthwise* menurunkan resolusi. Biayanya turun menjadi O(2HWC² + 9/2·HWC) dengan parameter O(2C² + 18C). Urutan ini mempertahankan lebih banyak informasi: dibanding urutan terbalik, akurasi naik 0,7 poin AP pada YOLOv10-S.

### Desain Blok Berpanduan Peringkat Intrinsik

Penulis mengukur *intrinsic rank* (peringkat intrinsik: jumlah nilai singular di atas ambang pada konvolusi terakhir tiap tahap) sebagai penanda redundansi — peringkat rendah berarti fitur tahap itu banyak mengulang informasi. Pada YOLOv8, tahap-tahap dalam dan model-model besar berperingkat rendah, sehingga paling redundan. Untuk tahap seperti itu disediakan CIB (*compact inverted block*), blok ringkas berisi konvolusi *depthwise* untuk pencampuran spasial dan konvolusi *pointwise* untuk pencampuran kanal, disisipkan ke dalam struktur ELAN (struktur agregasi fitur multi-cabang dari YOLOv7, bab 007). Penggantian bersifat adaptif: tahap diurutkan dari peringkat terendah, blok diganti satu per satu, dan proses berhenti begitu akurasi turun. Pada YOLOv10-S degradasi baru muncul di tahap ketiga dalam urutan, sehingga hanya dua tahap terburuk yang memakai CIB.

### Konvolusi Kernel Besar dan Perhatian-Diri Parsial

Dua komponen menambah akurasi dengan biaya kecil. Pertama, konvolusi *depthwise* 3×3 kedua di dalam CIB pada tahap dalam diperbesar menjadi 7×7 untuk memperluas *receptive field* (wilayah citra yang memengaruhi satu unit fitur). Selama pelatihan ditambahkan cabang konvolusi 3×3 yang dilebur ke cabang utama saat inferensi (*structural reparameterization*), sehingga tidak ada biaya inferensi tambahan. Komponen ini hanya dipakai pada model kecil (N dan S), karena model besar sudah memiliki receptive field yang luas.

Kedua, PSA (*partial self-attention*). *Self-attention* adalah mekanisme yang membobot relasi setiap posisi fitur terhadap semua posisi lain; kuat untuk pemodelan global, tetapi biayanya tumbuh kuadratik terhadap jumlah posisi. PSA membelah kanal menjadi dua bagian sama besar setelah konvolusi 1×1; hanya satu bagian yang melewati satu blok *multi-head self-attention* (perhatian-diri dengan beberapa kepala paralel) dan jaringan umpan-maju (dua lapisan linier dengan aktivasi), lalu keduanya disambung dan dilebur dengan konvolusi 1×1. Dimensi kueri dan kunci dibuat separuh dimensi nilai, dan normalisasi memakai BatchNorm alih-alih LayerNorm demi kecepatan. PSA hanya dipasang setelah tahap 4 — tahap beresolusi terendah — sehingga biaya kuadratiknya tetap kecil.

## Eksperimen dan Hasil

Seluruh model dilatih dari awal pada COCO (*Common Objects in Context*, tolok ukur 80 kelas objek; AP adalah rata-rata presisi pada ambang IoU 0,50 hingga 0,95) dengan resolusi uji 640 piksel. Latensi diukur end-to-end pada GPU NVIDIA T4 dengan TensorRT FP16 (pustaka inferensi NVIDIA, presisi 16-bit). Enam varian dihasilkan: YOLOv10-N/S/M/B/L/X.

Angka utamanya: dari N ke X, AP berturut-turut 38,5 / 46,3 / 51,1 / 52,5 / 53,2 / 54,4%, latensi 1,84 / 2,49 / 4,74 / 5,74 / 7,28 / 10,70 ms, dan parameter 2,3 / 7,2 / 15,4 / 19,1 / 24,4 / 29,5 juta. Interpretasinya: YOLOv10-N berjalan lebih dari 500 kali per detik pada T4, dan kenaikan dari N ke S menambah 7,8 poin AP hanya dengan tambahan 0,65 ms.

Terhadap YOLOv8 sebagai basis, perbaikan AP pada varian N/S/M/L/X masing-masing +1,2 / +1,4 / +0,5 / +0,3 / +0,5 poin, dengan parameter berkurang 28/36/41/44/57%, komputasi 23/24/25/27/38%, dan latensi end-to-end turun 70/65/50/41/37%. Penurunan 70% pada varian N terutama berasal dari hilangnya NMS, karena pada model kecil porsi waktu pasca-proses relatif besar. Terhadap RT-DETR, YOLOv10-S dan YOLOv10-X 1,8 dan 1,3 kali lebih cepat daripada varian R18 dan R101 pada AP setara. Terhadap YOLOv9-C (bab 008), YOLOv10-B mencapai performa sama dengan latensi 46% lebih rendah dan parameter 25% lebih sedikit; terhadap Gold-YOLO-L, YOLOv10-L unggul 1,4 poin AP sekaligus 68% lebih ramping dan 32% lebih cepat.

Ablasi memisahkan sumbangan tiap komponen. Penugasan ganda konsisten memangkas latensi end-to-end YOLOv10-S sebesar 4,63 ms dibanding inferensi dengan NMS, sembari mempertahankan AP 44,3% — bukti bahwa pada model kecil sebagian besar waktu inferensi selama ini habis untuk pasca-proses. Desain efisiensi memangkas 11,8 juta parameter dan 20,8 GFLOPs serta mengurangi latensi 0,65 ms pada YOLOv10-M tanpa merusak akurasi. Desain akurasi menambah 1,8 poin AP pada varian S dan 0,7 poin pada varian M dengan biaya hanya 0,18 dan 0,17 ms; rinciannya, kernel besar menyumbang +0,4 poin AP (0,03 ms) dan PSA +1,4 poin AP (0,15 ms) pada varian S.

## Kelebihan dan Keterbatasan

Kelebihan: (1) inferensi end-to-end tanpa NMS — latensi stabil, tidak bergantung jumlah objek, dan bebas penyetelan ambang NMS; (2) tanpa biaya inferensi tambahan karena kepala satu-ke-banyak dibuang setelah pelatihan; (3) efisiensi parameter dan komputasi terbaik di kelasnya pada semua skala; (4) komponennya terpisah dan dapat diadopsi sebagian pada arsitektur lain.

Keterbatasan yang diakui penulis: pelatihan tanpa NMS masih menyisakan celah akurasi terhadap pelatihan satu-ke-banyak plus NMS pada model kecil — 1,0 poin AP pada YOLOv10-N — karena fitur model kecil kurang diskriminatif untuk pencocokan satu-ke-satu; celah ini menutup sepenuhnya pada YOLOv10-X. Manfaat konvolusi kernel besar juga menghilang pada model menengah ke atas. Dari sisi rekayasa, tiga catatan tambahan: angka latensi diukur pada satu konfigurasi perangkat keras (T4 dengan TensorRT FP16) sehingga dapat berbeda pada perangkat lain; pelatihan dua kepala menambah biaya dan kerumitan tahap pelatihan; dan tanpa NMS, praktisi kehilangan ambang pasca-proses yang biasa dipakai mengatur keseimbangan presisi–recall per aplikasi.

## Kaitan dengan Bab Lain

Bab ini menjawab masalah yang ada sejak bab 001: NMS menjadi bagian tak terpisahkan dari keluarga YOLO sejak YOLOv1, dan generasi berikutnya hingga [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) memperbaiki arsitektur tanpa menyentuh pasca-proses tersebut. Gagasan end-to-end-nya mewarisi garis [bab 022 (DETR)](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md) dan dibandingkan dengan [bab 155 (RT-DETR)](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md), detektor transformer real-time yang lebih dulu bebas NMS. Basis arsitekturnya adalah YOLOv8, pembanding utamanya YOLOv9, dan struktur ELAN yang dipakai CIB berasal dari [bab 007 (YOLOv7)](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md). Garis ini berlanjut ke [bab 010 (YOLOv11)](./010%20-%202024%20-%20YOLOv11%20%28Overview%29%20-%20Fondasi%20RGB.md) sebagai generasi berikutnya, serta ke [bab 192 (YOLO26)](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md) yang meneruskan agenda detektor real-time end-to-end yang dibakukan di sini.

## Poin untuk Sitasi

Kutip dengan kunci `wang2024yolov10`. Ringkasan yang aman dikutip: "YOLOv10 menghilangkan NMS dari inferensi YOLO melalui pelatihan penugasan ganda yang konsisten — kepala satu-ke-banyak untuk supervisi, kepala satu-ke-satu untuk inferensi — ditambah desain ulang arsitektur berbasis efisiensi dan akurasi; pada COCO, YOLOv10-S 1,8 kali lebih cepat daripada RT-DETR-R18 pada AP setara dengan 2,8 kali lebih sedikit parameter dan komputasi." Catatan verifikasi sebelum sitasi formal: seluruh angka per varian (AP, latensi, parameter, FLOPs) berasal dari Tabel 1 makalah versi *camera-ready* NeurIPS 2024 (arXiv v2) dan telah dicocokkan dengan tabel pada repositori resmi THU-MIG; angka latensi hanya berlaku untuk konfigurasi T4 dengan TensorRT FP16; rincian ablasi sebaiknya dikutip langsung dari Tabel 2 naskah asli.
