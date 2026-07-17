# 026 - A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `terven2023yolo` |
| Judul asli | A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS |
| Penulis | Juan Terven, Diana-Margarita Cordova-Esparza, Julio-Alejandro Romero-Gonzalez |
| Tahun | 2023 |
| Venue | Machine Learning and Knowledge Extraction (MDPI), Vol. 5, No. 4, hlm. 1680–1716 |
| Tema | Survei YOLO |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2304.00501
- **DOI (versi jurnal):** https://doi.org/10.3390/make5040083
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Comprehensive%20Review%20of%20YOLO%20Architectures%20in%20Computer%20Vision%3A%20From%20YOLOv1%20to%20YOLOv8%20and%20YOLO-NAS
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Comprehensive%20Review%20of%20YOLO%20Architectures%20in%20Computer%20Vision%3A%20From%20YOLOv1%20to%20YOLOv8%20and%20YOLO-NAS&sort=relevance

## Gambaran Umum

Makalah ini adalah survei atas seluruh silsilah detektor objek YOLO, mulai dari YOLOv1 (2016) hingga YOLOv8, YOLO-NAS, dan varian YOLO berbasis *transformer*. Alih-alih mengusulkan detektor baru, Terven dkk. melakukan tiga hal: menetapkan bahasa pengukuran yang seragam (metrik AP, IoU, dan pasca-pemrosesan NMS), membedah setiap versi menjadi komponen *backbone*–*neck*–*head* beserta teknik pelatihannya, dan menyusun kronologi perubahan sehingga kontribusi tiap generasi dapat dibandingkan.

Hasilnya adalah sintesis setebal 36 halaman (21 gambar, 4 tabel) yang memperlihatkan pergeseran desain keluarga YOLO: dari detektor berbasis *anchor* menuju *anchor-free*, dari penetapan label statis menuju dinamis, dan dari pelatihan konvensional menuju pelatihan sadar kuantisasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Antara 2016 dan 2023, keluarga YOLO bertambah menjadi lebih dari sepuluh varian utama: YOLOv1–v8, YOLO9000, Scaled-YOLOv4, YOLOR, YOLOX, PP-YOLO, YOLOv6, YOLOv7, dan YOLO-NAS. Sebagian terbit di konferensi, sebagian hanya di arXiv, dan sebagian — YOLOv5 serta YOLOv8 — tidak memiliki makalah formal, hanya repositori kode dan dokumentasi.

Keadaan ini menimbulkan tiga kesulitan. Pertama, informasi tersebar; tidak ada satu naskah yang menjelaskan perbedaan satu versi dari pendahulunya. Kedua, tolok ukurnya berganti: YOLOv1 dan v2 dievaluasi pada PASCAL VOC, sedangkan YOLOv3 dan setelahnya pada Microsoft COCO, sehingga angka antar-generasi tidak dapat dibandingkan mentah. Ketiga, survei-survei yang sudah ada hanya mencakup hingga YOLOv3 atau YOLOv4. Makalah ini mengisi celah tersebut dengan satu kerangka baca yang seragam dari v1 sampai v8. Versi yang lahir setelah survei ini — YOLOv9 dan YOLOv10 — dibahas pada bab 008 dan 009.

## Ide Utama

Gagasan inti survei ini adalah memperlakukan silsilah YOLO sebagai satu sistem yang berevolusi, bukan daftar makalah yang berdiri sendiri. Tiap versi dibedah dengan dua alat: bahasa pengukuran yang sama (AP, IoU, dan NMS didefinisikan lebih dulu agar angka antar-versi sejajar pijakannya), dan anatomi *backbone*–*neck*–*head*, sehingga tiap generasi terbaca sebagai penggantian atau penambahan modul pada kerangka yang tetap. Dengan keduanya, evolusi YOLO terurai menjadi gerakan sepanjang tiga poros: cara prediksi dibuat, cara jaringan disusun, dan cara pelatihan dilakukan.

## Cara Kerja Langkah demi Langkah

### Bahasa Pengukuran: AP, IoU, dan NMS

Bagian teknis survei dibuka dengan metrik, karena semua perbandingan selanjutnya bergantung padanya. *Precision* (presisi) adalah proporsi prediksi positif yang benar; *recall* adalah proporsi objek yang benar-benar ada yang berhasil ditemukan. Karena keduanya saling menekan melalui ambang *confidence* (skor keyakinan deteksi), kinerja diringkas oleh kurva presisi–recall; luas di bawah kurva inilah *Average Precision* (AP). Untuk banyak kelas, AP dihitung per kelas lalu dirata-rata, sehingga disebut pula *mean Average Precision* (mAP). Sebuah prediksi dinyatakan benar hanya bila IoU (*Intersection over Union* — rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran) melampaui ambang tertentu.

Perbedaan dua tolok ukur dijelaskan secara eksplisit. PASCAL VOC (20 kelas) menghitung AP dari interpolasi 11 titik kurva presisi–recall pada satu ambang IoU. Microsoft COCO (80 kelas) memakai 101 titik *recall* dan merata-ratakan AP pada sepuluh ambang IoU, dari 0,5 hingga 0,95 dengan langkah 0,05; metrik yang hanya memakai IoU 0,5 disebut AP50. Konsekuensinya, AP COCO secara sistematis lebih rendah daripada AP VOC untuk model yang setara, sehingga angka YOLOv1/v2 tidak dapat dijejerkan langsung dengan angka YOLOv3 ke atas.

Terakhir dirinci *Non-Maximum Suppression* (NMS), pasca-pemrosesan pada semua versi YOLO: kotak prediksi diurutkan menurut skor *confidence*, yang tertinggi diambil, dan semua kotak lain dengan IoU di atas ambang terhadapnya dibuang, berulang sampai habis. NMS mengubah ratusan kandidat menjadi segelintir deteksi akhir.

### Kerangka Backbone–Neck–Head

Mulai dari pembahasan YOLOv4, survei mengadopsi anatomi tiga bagian yang menjadi cara standar mendeskripsikan detektor. *Backbone* adalah jaringan konvolusi pengekstrak fitur dari citra masukan, biasanya dilatih terlebih dahulu untuk klasifikasi ImageNet. *Neck* adalah komponen perantara yang menggabungkan fitur lintas skala, misalnya FPN (*Feature Pyramid Network* — piramida fitur yang meneruskan informasi dari peta fitur dalam ke peta fitur dangkal) atau PAN. *Head* adalah komponen akhir yang mengeluarkan prediksi: koordinat *bounding box* (kotak pembatas objek), skor keberadaan objek, dan kelas.

Alur ketiga komponen tersebut digambarkan sebagai berikut:

```
citra masukan (mis. 640x640 piksel)
   │
   ▼
┌────────────┐   keluaran: peta fitur multi-skala
│  BACKBONE  │   (mis. 80x80, 40x40, 20x20)
└─────┬──────┘
      ▼
┌────────────┐   penggabungan fitur lintas skala
│    NECK    │   (FPN / PAN / SPP)
└─────┬──────┘
      ▼
┌────────────┐   prediksi per sel:
│    HEAD    │   kotak, skor objek, kelas
└─────┬──────┘   (ber-anchor / anchor-free)
      ▼
  ┌───────┐      buang kotak yang tumpang tindih
  │  NMS  │      (IoU di atas ambang dibuang)
  └───┬───┘
      ▼
 deteksi akhir: kotak + kelas + skor
```

Dengan kerangka ini, perbedaan antar-versi dapat dinyatakan secara ringkas: YOLOv3 mengganti *backbone* menjadi Darknet-53 dan memperkenalkan prediksi tiga skala; YOLOv4 memasang *neck* PANet dan blok SPP; YOLOX memisahkan *head* klasifikasi dari *head* regresi.

### Kronologi Perubahan per Versi

Survei menelusuri tiap versi secara berurutan. Dua istilah perlu dijelaskan lebih dulu. *Anchor box* adalah kotak acuan berbentuk tetap yang ditempatkan pada setiap sel keluaran; model memprediksi koreksi terhadap kotak acuan itu, bukan kotak dari nol. *Bag-of-freebies* adalah teknik yang menaikkan akurasi dengan hanya menambah biaya pelatihan (misalnya augmentasi data), sedangkan *bag-of-specials* menambah sedikit biaya inferensi demi perolehan akurasi yang besar.

| Versi | Tahun | Perubahan kunci menurut survei |
|---|---|---|
| YOLOv1 | 2016 | deteksi satu tahap berbasis grid 7×7; regresi langsung |
| YOLOv2 / YOLO9000 | 2017 | *anchor box* hasil klasterisasi, Darknet-19, pelatihan multi-skala; >9.000 kelas |
| YOLOv3 | 2018 | Darknet-53 dengan sambungan residual; prediksi tiga skala |
| YOLOv4 | 2020 | seleksi *bag-of-freebies* dan *bag-of-specials*; CSPDarknet53 + SPP + PANet |
| YOLOv5 | 2020 | rekayasa PyTorch oleh Ultralytics; AutoAnchor; lima skala model |
| Scaled-YOLOv4 | 2021 | penskalaan naik/turun untuk GPU awan dan perangkat tepi |
| YOLOR | 2021 | satu representasi bersama untuk banyak tugas (pengetahuan implisit) |
| YOLOX | 2021 | *anchor-free*, kepala terpisah, penetapan label simOTA |
| YOLOv6 | 2022 | *backbone* RepVGG (EfficientRep); distilasi dan kuantisasi untuk industri |
| YOLOv7 | 2022 | blok E-ELAN; re-parameterisasi terencana; *trainable bag-of-freebies* |
| PP-YOLOE | 2022 | jalur industri PaddlePaddle: *anchor-free*, TAL, kepala ET |
| YOLOv8 | 2023 | Ultralytics; kepala *anchor-free* terpisah; tanpa makalah formal |
| YOLO-NAS | 2023 | arsitektur hasil pencarian NAS (AutoNAC); blok sadar kuantisasi |

### Tiga Poros Perubahan Lintas Versi

Survei menyaring tiga garis perubahan besar. Poros pertama: pelepasan *anchor*. YOLOv2 memperkenalkan *anchor box* (lima bentuk dari klasterisasi *k-means* atas kotak data latih) dan semua versi hingga YOLOv5 mengikutinya. YOLOX (2021) membalik arah: prediksi dibuat langsung per lokasi tanpa kotak acuan (*anchor-free*), menyederhanakan pelatihan dan dekode keluaran; arah ini diikuti PP-YOLOE dan YOLOv8.

Poros kedua adalah penetapan label (*label assignment*), yaitu aturan yang menentukan prediksi mana yang dianggap positif untuk tiap objek saat pelatihan. Versi awal memakai aturan statis (sel yang memuat pusat objek). YOLOX memakai simOTA, yang memilih kandidat terbaik per objek melalui penyederhanaan masalah transportasi optimal. YOLOv6 dan PP-YOLOE memakai TAL (*Task Alignment Learning*), yang menyelaraskan skor klasifikasi dengan ketepatan lokalisasi. YOLOv7 menambahkan skema *coarse-to-fine* berpemandu *head* utama untuk melatih *head* bantu.

Poros ketiga adalah efisiensi pasca-pelatihan. Re-parameterisasi melatih jaringan dengan struktur bercabang lalu menggabungkannya menjadi satu konvolusi saat inferensi, sehingga akurasi naik tanpa biaya tambahan; YOLOv7 memadukannya dengan blok E-ELAN (*Extended ELAN*), yang memperbanyak ragam fitur melalui percabangan grup tanpa mengubah jalur gradien. Kuantisasi memampatkan bobot ke bilangan bulat 8 bit (INT8) agar inferensi lebih cepat. YOLO-NAS menjadi titik ekstrem poros ini: arsitekturnya tidak dirancang manual, melainkan ditemukan oleh pencarian arsitektur saraf (*Neural Architecture Search*, NAS) bernama AutoNAC yang menelusuri ruang sekitar 10^14 kandidat selama kurang lebih 3.800 jam GPU dengan sasaran latensi pada GPU NVIDIA T4.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak menjalankan eksperimen baru; buktinya berupa kompilasi angka dari naskah asli tiap versi. Lintasan yang dikutip: 63,4% AP (YOLOv1) dan 78,6% (YOLOv2) pada VOC 2007; kemudian pada COCO: 36,2% AP dengan AP50 60,6% (YOLOv3-spp, 20 FPS), 43,5% (YOLOv4, lebih dari 50 FPS pada V100), 50,7% (YOLOv5x, citra 640 piksel), 50,1% (YOLOX), 57,2% (model terbesar YOLOv6), dan 56,8% (YOLOv7-E6E) — angka tertinggi di antara detektor *real-time* berkecepatan minimal 30 FPS saat survei ditulis. Interpretasinya: dalam empat tahun pada tolok ukur yang sama, AP naik sekitar 20 poin sementara kecepatan tetap di atas 30 FPS, sehingga perbaikan berasal dari desain arsitektur dan pelatihan, bukan dari memperlambat model.

Survei juga menyalin rantai ablasi YOLOX terhadap garis dasar YOLOv3: pelepasan *anchor* menambah 0,9 poin AP, penambahan sampel positif 2,1 poin, kepala terpisah 1,1 poin, simOTA 2,3 poin, dan augmentasi kuat 2,4 poin, dengan total sekitar 8,8 poin menuju 50,1% AP; artinya, sebagian besar keuntungan datang dari teknik pelatihan, bukan pembesaran model.

Untuk YOLO-NAS, hasil yang ditonjolkan adalah ketangguhan kuantisasi: konversi ke INT8 hanya menurunkan 0,51, 0,65, dan 0,45 poin mAP untuk varian S, M, dan L, dibandingkan penurunan 1–2 poin yang lazim pada model lain. Artinya, desain sadar kuantisasi mempertahankan hampir seluruh akurasi model pada mesin inferensi cepat — isu yang diabaikan versi-versi sebelumnya.

## Kelebihan dan Keterbatasan

Kelebihan survei ini: cakupannya paling mutakhir pada masanya (hingga YOLOv8, YOLO-NAS, dan YOLO berbasis *transformer* — jaringan berbasis mekanisme atensi); pembahasan arsitektur tiap versi rinci; dan bahasa metriknya seragam sehingga pembaca baru dapat mengikuti angka antar-generasi.

Keterbatasannya ada empat. Pertama, angka lintas versi dikompilasi dari makalah dengan perangkat keras, ukuran masukan, dan pengaturan uji berbeda (misalnya YOLOv5x pada 640 piksel dibanding YOLOv7-E6E pada 1280 piksel), sehingga perbandingannya bersifat indikatif, bukan uji berpasangan yang adil. Kedua, dari sisi rekayasa, survei ini cepat tertinggal: YOLOv9 dan YOLOv10 terbit pada 2024, setahun setelahnya. Ketiga, pembahasan YOLOv5 dan YOLOv8 bertumpu pada dokumentasi repositori yang tidak melalui peninjauan sejawat. Keempat, secara konseptual, survei ini mendeskripsikan perubahan tetapi tidak mengulang eksperimennya, sehingga rantai sebab-akibat seperti ablasi YOLOX tetap merupakan klaim dari makalah asal.

## Kaitan dengan Bab Lain

Bab ini menaungi klaster Fondasi RGB: tiap versi pada kronologi di atas diuraikan pada [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), bab 002 (YOLOv2), bab 003 (YOLOv3), [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md), [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md), bab 006 (YOLOv6), dan [bab 007 (YOLOv7)](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md). Survei ini berhenti di YOLOv8 dan YOLO-NAS; garis evolusi sesudahnya dilanjutkan [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md). Di dalam klaster Survei YOLO sendiri, bab ini berdampingan dengan [bab 028 (Review Perkembangan YOLO, Jiang dkk.)](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md) yang cakupannya lebih awal.

## Poin untuk Sitasi

Kutip dengan kunci `terven2023yolo`. Ringkasan yang aman dikutip: "Terven dkk. (2023) menyurvei evolusi keluarga YOLO dari YOLOv1 hingga YOLOv8, YOLO-NAS, dan varian berbasis transformer; survei ini menstandarkan pembahasan metrik (AP, IoU, NMS), membedah tiap versi menjadi backbone–neck–head, dan merangkum pergeseran desain menuju detektor anchor-free dengan penetapan label dinamis."

Catatan verifikasi sebelum sitasi formal: (1) angka AP per versi pada bab ini dinisbatkan ke survei dan makalah asal masing-masing; cocokkan dengan Tabel 4 naskah asli. (2) Angka YOLOv8x (53,9%) bersumber dari dokumentasi Ultralytics, bukan dari survei; YOLOv8 tidak memiliki makalah formal. (3) Angka penurunan mAP akibat kuantisasi YOLO-NAS (0,51/0,65/0,45 poin) dan biaya pencarian AutoNAC (10^14 kandidat, ±3.800 jam GPU) dikutip dari blog resmi Deci AI; verifikasi ke naskah survei. (4) Daftar penulis pada berkas ini mengikuti versi jurnal (tiga nama); metadata arXiv versi terakhir hanya mencantumkan dua nama.
