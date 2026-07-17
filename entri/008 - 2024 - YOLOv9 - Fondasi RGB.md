# 008 - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024yolov9` |
| Judul asli | YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information |
| Penulis | Chien-Yao Wang, I-Hau Yeh, Hong-Yuan Mark Liao |
| Tahun | 2024 |
| Venue | European Conference on Computer Vision (ECCV 2024); preprint arXiv:2402.13616 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2402.13616
- **Repositori kode resmi:** https://github.com/WongKinYiu/yolov9
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv9%3A%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv9%3A%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan YOLOv9, detektor objek satu tahap keluarga YOLO yang dibangun dari dua komponen baru: *Programmable Gradient Information* (PGI) dan *Generalized Efficient Layer Aggregation Network* (GELAN). Titik tolaknya adalah pengamatan bahwa data masukan kehilangan informasi sedikit demi sedikit saat melewati lapisan-lapisan jaringan yang dalam. Akibatnya, gradien — sinyal koreksi yang dihitung dari fungsi *loss* lalu dialirkan mundur untuk memperbarui bobot — tidak lagi memuat informasi yang cukup untuk melatih jaringan dengan benar.

PGI menjawab masalah tersebut dengan menambahkan cabang reversibel bantu yang hanya aktif selama pelatihan dan dibuang saat inferensi, sehingga kualitas gradien naik tanpa menambah biaya pemakaian model. GELAN adalah blok arsitektur ringan hasil generalisasi ELAN yang dipakai sebagai tubuh jaringan. Model terbesar, YOLOv9-E, mencapai 55,6% AP pada MS COCO dengan 57,3 juta parameter: 1,7 poin AP di atas YOLOv8-X dengan parameter 16% lebih sedikit dan komputasi 27% lebih rendah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv1 (bab 001), perbaikan keluarga YOLO berpusat pada desain arsitektur dan resep pelatihan. YOLOv4 (bab 004) memopulerkan pemakaian blok CSP (*Cross Stage Partial*) untuk memperkaya jalur gradien; YOLOv7 (bab 007) memperkenalkan ELAN (*Efficient Layer Aggregation Network*), blok yang menggabungkan keluaran beberapa lapisan konvolusi agar gradien mengalir melalui jalur terpendek dan terpanjang sekaligus. Makalah ini berpendapat bahwa di balik semua perbaikan itu ada masalah yang lebih mendasar yang belum ditangani: kehilangan informasi selama proses umpan maju (*feedforward*).

Menurut prinsip *information bottleneck*, bila data X melewati transformasi berlapis f dan g, informasi bersama (*mutual information*) antara masukan dan representasinya tidak pernah bertambah: I(X,X) ≥ I(X,f(X)) ≥ I(X,g(f(X))). Semakin dalam jaringan, semakin besar peluang informasi yang relevan dengan target tergerus. Padahal bobot jaringan diperbarui dari gradien yang dihitung pada keluaran lapisan terakhir. Bila keluaran itu sudah kehilangan informasi penting, gradien menjadi tidak andal dan pelatihan konvergen ke pemetaan yang salah antara data dan target.

Tiga pendekatan yang ada untuk meredam masalah ini memiliki kelemahan masing-masing. Pertama, arsitektur reversibel (jaringan yang transformasinya dapat dibalik sehingga tidak ada informasi hilang) menaikkan biaya inferensi secara nyata: makalah ini melaporkan tambahan waktu inferensi sekitar 20% untuk koneksi balik dari lapisan dalam ke dangkal, dan lebih dari dua kali lipat bila masukan diumpan ulang ke lapisan beresolusi tinggi. Kedua, *masked modeling* (menutup sebagian masukan lalu melatih jaringan merekonstruksinya) dapat menimbulkan *loss* rekonstruksi yang bertentangan dengan *loss* tugas utama. Ketiga, *deep supervision* (menambahkan *loss* bantu pada lapisan tengah) hanya efektif pada jaringan yang sangat dalam dan dapat menimbulkan penumpukan galat serta informasi terfragmentasi.

## Ide Utama

Gagasan inti makalah ini terdiri atas dua bagian yang saling menguatkan. Pertama, PGI: alih-alih memaksa jaringan utama bersifat reversibel (yang mahal), tambahkan cabang bantu yang reversibel semata-mata untuk menghasilkan gradien yang andal selama pelatihan. Cabang ini "memprogram" informasi gradien yang diterima jaringan utama, lalu dibuang saat inferensi sehingga biaya pemakaian model tidak berubah. Kedua, GELAN: generalisasi blok ELAN agar dapat memakai sembarang blok komputasi (bukan hanya tumpukan konvolusi biasa), sehingga satu rancangan blok dapat disesuaikan dengan berbagai perangkat inferensi tanpa mengubah sifat agregasinya.

## Cara Kerja Langkah demi Langkah

### Fungsi Reversibel sebagai Dasar

Sebuah fungsi r disebut reversibel bila terdapat fungsi invers v sehingga X = v(r(X)): data dapat dipulihkan utuh, sehingga I(X,X) = I(X,r(X)) dan tidak ada informasi yang hilang. Koneksi residual pada ResNet (X lapis berikutnya = X lapis sekarang + f(X)) adalah contoh sederhana sifat ini. Penulis menunjukkan lewat visualisasi peta fitur bahwa kapasitas mempertahankan informasi berkorelasi dengan akurasi: pada bobot acak, PlainNet kehilangan hampir seluruh informasi objek pada lapis ke-100, ResNet mulai kabur pada lapis ke-100, sedangkan CSPNet dan GELAN masih mempertahankan batas objek hingga lapis ke-200. Namun arsitektur reversibel penuh mahal untuk inferensi dan justru berkinerja buruk pada jaringan dangkal, karena tugas sulit membutuhkan transformasi yang dalam.

### Cabang Reversibel Bantu (Auxiliary Reversible Branch)

PGI terdiri atas tiga komponen: *main branch*, *auxiliary reversible branch*, dan *multi-level auxiliary information*. *Main branch* adalah jaringan yang dipakai untuk inferensi. *Auxiliary reversible branch* adalah cabang tambahan yang mempertahankan informasi masukan secara eksplisit melalui struktur reversibel; pada implementasi YOLOv9, cabang ini memakai jalinan gaya CBNet/DynamicDet (disebut ICN dengan koneksi DHLC) yang meneruskan informasi antarlevel. Selama pelatihan, gradien dari cabang ini mengalir ke *main branch* dan mendorong bobotnya mengekstraksi fitur yang benar-benar relevan dengan target, bukan korelasi semu dari fitur yang sudah terdegradasi. Karena reversibilitas hanya dibutuhkan untuk menghasilkan gradien, bukan untuk inferensi, seluruh cabang ini dibuang setelah pelatihan selesai.

### Informasi Bantu Bertingkat (Multi-level Auxiliary Information)

Komponen ketiga menangani kelemahan *deep supervision* konvensional pada detektor berbasis piramida fitur. FPN (*Feature Pyramid Network*) adalah struktur yang menggabungkan fitur beberapa skala agar objek besar dan kecil terdeteksi; PAN (*Path Aggregation Network*) menambah jalur agregasi dari bawah ke atas di atasnya. Pada *deep supervision* biasa, setiap cabang prediksi dangkal diawasi terpisah, sehingga fitur dangkal diarahkan hanya untuk ukuran objek tertentu dan objek ukuran lain diperlakukan sebagai latar — informasi menjadi terfragmentasi sebelum mencapai lapisan dalam. PGI menyisipkan jaringan integrasi yang menggabungkan gradien dari seluruh *head* prediksi sebelum meneruskannya ke *main branch*. Dengan demikian setiap tingkat piramida menerima informasi tentang semua objek, dan fragmentasi itu terhindarkan. Karena gradien yang diteruskan dapat dipilih per tingkat semantik, penulis menyebut keseluruhan mekanisme ini "gradien yang dapat diprogram".

### GELAN: Generalisasi ELAN

GELAN menggabungkan dua rancangan yang sama-sama berbasis perencanaan jalur gradien: CSPNet, yang membelah peta fitur menjadi dua jalur lalu menggabungkannya kembali untuk mengurangi komputasi ganda, dan ELAN, yang menumpuk beberapa konvolusi dan menggabungkan seluruh keluaran perantaranya. ELAN asli hanya menerima lapisan konvolusi standar; GELAN menggeneralisasikannya sehingga blok komputasi apa pun (blok residual, blok CSP, dan lain-lain) dapat dipasang. Pada YOLOv9 dipilih blok CSP dengan RepConv (konvolusi yang dilatih bercabang lalu dilebur menjadi satu konvolusi saat inferensi). Struktur keseluruhan mengikuti kerangka YOLOv7: modul *downsampling* disederhanakan dan *head* prediksi diganti menjadi *anchor-free* (memprediksi posisi kotak langsung terhadap titik acuan, tanpa kotak *anchor* berukuran tetap).

Skema aliran informasi PGI saat pelatihan dan bentuk akhir saat inferensi:

```
PELATIHAN (PGI aktif penuh)
citra ──► main branch ────────────────► prediksi ──► loss utama
          (GELAN)          ▲ gradien    ▲
              ▲            │ terprogram │
              │   ┌────────┴───────────┐│
              └───┤ multi-level        ││ gradien dari
                  │ auxiliary info     │├─ head bantu tiap
                  │ (integrasi gradien)││  tingkat piramida
                  └────────▲───────────┘│
                           │            │
              auxiliary reversible branch
              (ICN/DHLC; mempertahankan
               informasi masukan secara eksplisit)

INFERENSI (kedua cabang bantu dibuang)
citra ──► main branch (GELAN) ──► prediksi
biaya inferensi identik dengan jaringan tanpa PGI
```

Diagram di atas menegaskan sifat PGI: dua cabang bawah hanya menyalurkan gradien ke *main branch* selama pelatihan, sehingga model yang dipakai pengguna akhir adalah *main branch* saja.

## Eksperimen dan Hasil

Seluruh eksperimen memakai MS COCO 2017 dengan pelatihan dari nol (*train-from-scratch*, tanpa bobot pralatih ImageNet) selama 500 *epoch* (satu *epoch* berarti satu kali putaran pelatihan atas seluruh data latih). Laju pembelajaran dinaikkan secara linear pada tiga *epoch* pertama (*warm-up*) dan augmentasi *mosaic* (menggabungkan empat citra menjadi satu citra latih) dimatikan pada 15 *epoch* terakhir. Metrik utama adalah AP (*Average Precision*) COCO: rata-rata presisi pada ambang IOU 0,50–0,95, maksimal 100%. Efisiensi diukur dari jumlah parameter (banyaknya bobot model) dan FLOPs (operasi *floating-point* per citra; makin kecil makin ringan).

Hasil utama (ukuran masukan 640):

| Model | AP val | Parameter | FLOPs |
|---|---|---|---|
| YOLOv9-S | 46,8% | 7,1 M | 26,4 G |
| YOLOv9-M | 51,4% | 20,0 M | 76,3 G |
| YOLOv9-C | 53,0% | 25,3 M | 102,1 G |
| YOLOv9-E | 55,6% | 57,3 M | 189,0 G |

Interpretasi perbandingan yang dilaporkan penulis: terhadap YOLO-MS (detektor ringan berbasis konvolusi *depth-wise*, yaitu konvolusi yang memproses tiap kanal terpisah untuk menekan biaya), YOLOv9 memakai parameter sekitar 10% lebih sedikit dan komputasi 5–15% lebih rendah, tetapi tetap unggul 0,4–0,6 poin AP — bukti bahwa konvolusi konvensional pada GELAN lebih hemat parameter daripada desain *depth-wise*. YOLOv9-C menyamai AP YOLOv7 AF (53,0%) dengan parameter 42% lebih sedikit dan komputasi 22% lebih rendah; akurasi sama pada anggaran yang jauh lebih kecil berarti efisiensi parameter naik tajam. YOLOv9-E melampaui YOLOv8-X sebesar 1,7 poin AP dengan parameter 16% lebih sedikit. Terhadap RT-DETR-X yang dilatih dengan pralatih ImageNet, YOLOv9 mencapai akurasi setara dengan hanya 66% parameter meskipun dilatih dari nol.

Studi ablasi memisahkan kontribusi tiap komponen. Penggantian blok konvolusi ELAN dengan blok CSP menurunkan parameter dan komputasi sekaligus menaikkan AP 0,7 poin, sehingga blok CSP dipilih untuk GELAN. Kedalaman ELAN dan CSP di atas dua tidak lagi mengubah akurasi secara berarti — parameter, komputasi, dan AP bergerak linear — sehingga rancangan GELAN stabil tanpa penyetelan khusus. Untuk PGI, *deep supervision* konvensional hanya membantu model yang sangat dalam dan justru menurunkan akurasi model dangkal, sedangkan PGI menaikkan akurasi pada semua ukuran model (S, M, C, E). Visualisasi peta fitur setelah satu *epoch* menunjukkan GELAN tanpa PGI menghasilkan respons menyebar pada latar, sedangkan dengan PGI fokusnya terkonsentrasi pada wilayah objek — bukti kualitatif bahwa gradien yang diprogram memperbaiki korespondensi data-target.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah efisiensi parameter dan komputasi yang terbaik pada kelasnya saat dirilis, dengan landasan analisis teoretis (information bottleneck dan fungsi reversibel) yang menjelaskan mengapa metodenya bekerja. PGI juga bebas biaya inferensi dan berlaku umum: dapat dipasang pada berbagai ukuran jaringan, termasuk model ringan yang selama ini tidak diuntungkan oleh *deep supervision*.

Keterbatasannya: (1) manfaat PGI hanya terasa saat pelatihan — ia tidak menaikkan kualitas model yang sudah dilatih tanpa PGI; (2) dari sisi rekayasa, cabang reversibel bantu menambah memori dan waktu pelatihan, dan arsitektur dua cabang lebih rumit diimplementasikan daripada detektor satu jalur; (3) secara konseptual, perolehan akurasi pada model kecil relatif tipis (0,4–0,6 poin AP terhadap YOLO-MS), sehingga nilai tambah PGI paling besar justru pada model dalam; (4) evaluasi pada makalah terbatas pada deteksi objek MS COCO, sehingga generalisasi ke tugas dan domain lain belum ditunjukkan di naskah.

## Kaitan dengan Bab Lain

Bab ini mewarisi langsung kerangka [007 - 2023 - YOLOv7](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md): arsitektur YOLOv9 dibangun di atas YOLOv7 dengan ELAN digantikan GELAN, blok RepConv, dan pengaturan *auxiliary head* yang sama, sehingga perbandingan keduanya pada AP 53,0% mengisolasi sumbangan PGI dan GELAN. Penggunaan blok CSP meneruskan garis rancangan yang diperkenalkan pada [004 - 2020 - YOLOv4](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md). Secara kronologis bab ini menjadi batu pijak sebelum [009 - 2024 - YOLOv10](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md), yang menyerang masalah berbeda — penghapusan NMS pada sisi inferensi — di atas efisiensi arsitektur yang sudah dicapai di sini.

## Poin untuk Sitasi

Kutip dengan kunci `wang2024yolov9`. Ringkasan yang aman dikutip: "YOLOv9 mengatasi kehilangan informasi pada jaringan dalam melalui Programmable Gradient Information (PGI) — cabang reversibel bantu yang memasok gradien andal selama pelatihan tanpa biaya inferensi — dan arsitektur ringan GELAN hasil generalisasi ELAN. Pada MS COCO, YOLOv9-E mencapai 55,6% AP, melampaui YOLOv8-X sebesar 1,7 poin dengan parameter 16% lebih sedikit." Seluruh angka di bab ini berasal dari naskah arXiv:2402.13616 dan tabel kinerja repositori resmi; persentase perbandingan terhadap YOLO-MS, YOLOv7 AF, YOLOv8-X, dan RT-DETR-X adalah klaim penulis pada naskah dan sebaiknya dicocokkan dengan tabel versi prosiding ECCV sebelum sitasi formal.
