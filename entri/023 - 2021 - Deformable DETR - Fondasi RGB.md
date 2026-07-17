# 023 - Deformable DETR: Deformable Transformers for End-to-End Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2021deformabledetr` |
| Judul asli | Deformable DETR: Deformable Transformers for End-to-End Object Detection |
| Penulis | Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang, Jifeng Dai |
| Tahun | 2021 |
| Venue | International Conference on Learning Representations (ICLR 2021), sesi *oral* |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2010.04159
- **Repositori kode resmi:** https://github.com/fundamentalvision/Deformable-DETR
- **Google Scholar:** https://scholar.google.com/scholar?q=Deformable%20DETR%3A%20Deformable%20Transformers%20for%20End-to-End%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Deformable%20DETR%3A%20Deformable%20Transformers%20for%20End-to-End%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Deformable DETR, detektor objek *end-to-end* yang memperbaiki dua kelemahan utama DETR (bab 022): konvergensi pelatihan yang sangat lambat dan lemahnya deteksi objek kecil. Gagasan utamanya adalah mengganti *attention* global pada Transformer DETR dengan *deformable attention* multi-skala: setiap *query* tidak lagi memperhatikan seluruh posisi pada peta fitur, melainkan hanya sejumlah kecil titik *sampling* yang letaknya dipelajari di sekitar sebuah titik referensi, pada beberapa tingkat resolusi fitur sekaligus.

Hasilnya, model mencapai akurasi lebih tinggi daripada DETR dengan *epoch* pelatihan sepuluh kali lebih sedikit (50 lawan 500 epoch), dan peningkatan paling besar terjadi pada objek kecil. Dengan dua penyempurnaan tambahan — pemurnian kotak secara iteratif dan varian dua tahap — akurasinya mencapai 46,9 AP pada COCO. Mekanisme ini kemudian menjadi fondasi bagi banyak detektor Transformer setelahnya, termasuk RT-DETR.

## Latar Belakang: Masalah yang Ingin Dipecahkan

DETR (bab 022, 2020) merumuskan deteksi objek sebagai prediksi himpunan: sejumlah *object query* (vektor belajar yang masing-masing bertugas menemukan satu objek) dipasangkan satu-ke-satu dengan objek kebenaran melalui pencocokan bipartit Hungaria. Dengan cara itu, dua komponen rancangan tangan pada detektor konvensional tidak diperlukan lagi: *anchor box* (kotak acuan berukuran tetap yang menjadi titik awal regresi posisi) dan *Non-Maximum Suppression* atau NMS (pasca-pemrosesan yang membuang kotak ganda yang saling tumpang tindih). Namun, DETR memiliki dua masalah yang menghambat pemakaiannya.

Pertama, konvergensi sangat lambat: DETR memerlukan 500 epoch pelatihan, sekitar sepuluh kali lebih lama daripada detektor konvolusional seperti Faster R-CNN. Penyebabnya terletak pada *self-attention* global di *encoder*-nya. Mekanisme *attention* menghitung bobot kesesuaian antara setiap pasangan *query* dan *key* (dua proyeksi dari token fitur; bobot tinggi berarti informasi pada posisi *key* relevan bagi *query*). Pada awal pelatihan bobot-bobot ini hampir seragam di seluruh citra, sehingga diperlukan waktu lama sampai setiap query belajar memfokuskan perhatian pada wilayah sempit tempat objek berada.

Kedua, resolusi fitur terbatas. Karena biaya *attention* global tumbuh kuadratik terhadap jumlah posisi pada peta fitur, DETR hanya memakai satu peta fitur beresolusi rendah (keluaran tahap terakhir ResNet, *stride* 32, artinya satu sel fitur mewakili 32×32 piksel citra). Objek yang lebih kecil dari ukuran sel ini praktis hilang. Detektor konvolusional mengatasinya dengan *Feature Pyramid Network* (FPN), yaitu modul yang menggabungkan peta fitur beberapa resolusi agar objek kecil terdeteksi pada resolusi tinggi dan objek besar pada resolusi rendah. Menerapkan strategi serupa pada DETR tidak terjangkau: mempertinggi resolusi fitur satu skala saja (varian DETR-DC5, yang mengganti *stride* terakhir dengan konvolusi berdilasi agar peta fitur tetap besar) sudah menaikkan biaya komputasi lebih dari dua kali lipat.

## Ide Utama

Gagasan inti Deformable DETR adalah memangkas cakupan *attention* alih-alih memperhitungkan semua posisi. Setiap query memiliki satu titik referensi; dari fitur query tersebut, jaringan memprediksi letak beberapa titik *sampling* di sekitar referensi beserta bobot masing-masing titik, lalu keluaran *attention* dihitung hanya dari fitur pada titik-titik itu. Prinsip ini meniru konvolusi terdeformasi (*deformable convolution*, DCN, 2017), yang menggeser lokasi *sampling* konvolusi secara adaptif; bedanya, di sini *sampling* dilakukan di dalam kerangka *attention* berkepala banyak dan diterapkan lintas skala.

Dua konsekuensi langsung mengikuti desain ini. Pertama, kompleksitas *attention* turun dari kuadratik menjadi linear terhadap ukuran peta fitur, sebab jumlah titik per query tetap berapa pun resolusinya; ini membuat pemakaian fitur multi-skala menjadi terjangkau tanpa FPN. Kedua, konvergensi dipercepat: titik *sampling* sudah terlokalisasi di sekitar referensi sejak awal, sehingga model tidak harus belajar memfokuskan perhatian dari bobot yang seragam.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Multi-Skala

Citra masukan dilewatkan ke *backbone* ResNet-50 (jaringan konvolusi ekstraksi fitur). Diambil tiga peta fitur: C3 (stride 8), C4 (stride 16), dan C5 (stride 32). Level keempat dibentuk dengan konvolusi 3×3 stride 2 di atas C5, menghasilkan peta stride 64. Keempat level diproyeksikan ke 256 kanal dengan konvolusi 1×1, lalu diratakan menjadi barisan token (satu token per posisi spasial) dan diberi *positional encoding* sinusoidal ditambah embedding penanda level. Untuk citra 800×1333 piksel, total token keempat level sekitar 22.000 buah; pada DETR standar hanya level stride 32 yang dipakai (sekitar 1.050 token).

### Deformable Attention Multi-Skala

Modul *multi-scale deformable attention* (MSDeformAttn) adalah inti makalah. Untuk setiap query, satu lapisan linear memprediksi *offset* titik *sampling*: 8 kepala *attention* × 4 level × 4 titik × 2 koordinat. Lapisan linear kedua memprediksi bobot *attention* untuk 8 kepala × 16 titik, dinormalisasi *softmax* per kepala (fungsi yang mengubah skor menjadi bobot berjumlah satu). Lokasi *sampling* diperoleh dengan menambahkan *offset* pada titik referensi. Karena lokasi hasilnya umumnya fraksional, nilai fitur di sana dihitung dengan interpolasi bilinear, yaitu rata-rata berbobot dari empat piksel tetangga terdekat. Keluaran tiap kepala adalah jumlah berbobot dari fitur 16 titiknya; gabungan kedelapan kepala diproyeksikan kembali ke 256 kanal.

Aliran perhitungan untuk satu query:

```
query (256 kanal) + titik referensi (x, y) ternormalisasi
   │
   ├── linear -> offset: 8 kepala x 4 level x 4 titik x (dx, dy)
   └── linear -> bobot : 8 kepala x 16 titik, softmax per kepala
   │
   ▼
lokasi sampling = referensi + offset
   ├─ level stride 8  : ● ● ● ●   (4 titik per kepala)
   ├─ level stride 16 : ● ● ● ●
   ├─ level stride 32 : ● ● ● ●
   └─ level stride 64 : ● ● ● ●
   │
   ▼  interpolasi bilinear pada tiap lokasi fraksional
jumlah(bobot x fitur) 16 titik x 8 kepala -> linear -> keluaran 256 kanal
```

Setiap query dengan demikian hanya membaca 8 × 16 = 128 titik, berapa pun jumlah token peta fitur. Pada contoh citra di atas, *attention* global harus menghitung skor terhadap sekitar 22.000 posisi per query; MSDeformAttn hanya terhadap 128 titik yang dipilih sendiri.

### Encoder dan Titik Referensi

*Encoder* terdiri atas enam lapis. Tiap lapis berisi *self-attention* deformable (query dan fitur sama-sama berasal dari token peta fitur) diikuti jaringan *feed-forward* (dua lapisan linear dengan lebar dalam 1024). Titik referensi query di encoder adalah koordinat piksel token itu sendiri, dinormalisasi ke rentang [0, 1]; setiap token memusatkan *sampling*-nya di sekitar posisinya sendiri pada keempat level.

### Decoder

*Decoder* terdiri atas enam lapis dan memakai 300 *object query*. Setiap query adalah embedding 512 kanal yang dibelah dua: 256 kanal konten dan 256 kanal posisi. Titik referensi awal query diprediksi dari bagian posisi melalui satu lapisan linear beraktivasi sigmoid, sehingga berupa satu titik ternormalisasi di dalam citra. Tiap lapis decoder menjalankan tiga tahap: *self-attention* standar antar 300 query (murah karena jumlahnya tetap), *cross-attention* deformable dari query ke fitur encoder, dan jaringan *feed-forward*. Keluaran tiap lapis diteruskan ke dua *head*: lapisan linear pengklasifikasi kelas, dan perceptron tiga lapis yang meregresikan empat angka *bounding box* (kotak pembatas objek, dinyatakan sebagai pusat dan ukuran) relatif terhadap titik referensinya.

### Pemurnian Kotak Iteratif dan Varian Dua Tahap

Dua penyempurnaan opsional ditumpuk di atas struktur dasar. Pada *iterative bounding box refinement*, kotak hasil prediksi lapis decoder ke-i menjadi titik (dan ukuran) referensi bagi lapis ke-(i+1): regresi kotak berikutnya menghitung koreksi terhadap kotak sebelumnya, sehingga lokalisasi diperhalus bertahap sepanjang enam lapis. Pada varian *two-stage*, setiap posisi fitur keluaran encoder dinilai oleh satu *head* deteksi ringan; 300 proposal kotak berskor tertinggi dipakai sebagai referensi awal decoder. Varian ini menyerupai tahap *region proposal* pada Faster R-CNN, tetapi seluruhnya tetap satu jaringan yang dilatih *end-to-end*.

### Pelatihan

Pelatihan mengikuti resep DETR: pencocokan bipartit satu-ke-satu antara 300 prediksi dan objek kebenaran, *focal loss* (fungsi loss klasifikasi yang menekan kontribusi contoh mudah agar contoh sulit dominan) untuk kelas, serta kombinasi loss L1 dan *Generalized IoU* (perluasan IoU — rasio irisan terhadap gabungan dua kotak — yang tetap memberi gradien ketika kedua kotak tidak beririsan) untuk regresi kotak. Pengoptimal AdamW dengan laju belajar 2×10⁻⁴ (2×10⁻⁵ untuk backbone) dijalankan selama 50 epoch, dengan penurunan laju di epoch ke-40 dan ukuran batch total 32.

## Eksperimen dan Hasil

Evaluasi dilakukan pada COCO 2017 (118 ribu citra latih, 5 ribu citra validasi, 80 kelas), tolok ukur standar deteksi objek. Metriknya AP, rata-rata presisi lintas ambang IoU 0,50–0,95, dengan AP-S dan AP-L sebagai AP khusus objek kecil (luas < 32² piksel) dan besar (luas > 96² piksel). Semua model memakai backbone ResNet-50; kecepatan diukur pada GPU NVIDIA V100.

| Model | Epoch | AP | AP-S | AP-L | FLOPs | FPS |
|---|---|---|---|---|---|---|
| Faster R-CNN + FPN | 109 | 42,0 | 26,6 | 53,4 | 180 G | 25,6 |
| DETR | 500 | 42,0 | 20,5 | 61,1 | 86 G | 27,0 |
| DETR-DC5 | 500 | 43,3 | 22,5 | 61,1 | 187 G | 11,4 |
| Deformable DETR | 50 | 44,5 | 27,1 | 59,6 | 173 G | 15,0 |
| + refinement iteratif | 50 | 46,2 | 28,3 | 61,5 | 173 G | 15,0 |
| ++ dua tahap | 50 | 46,9 | 29,6 | 61,6 | 173 G | 14,5 |

Tiga temuan dapat dibaca dari tabel. Pertama, masalah konvergensi terkuantifikasi: DETR-DC5 yang dilatih hanya 50 epoch hanya mencapai 35,3 AP, jauh di bawah 43,3 AP pada 500 epoch; Deformable DETR mencapai 44,5 AP pada 50 epoch, melampaui DETR yang dilatih sepuluh kali lebih lama. Total waktu latihnya 325 jam-GPU berbanding sekitar 2.000 jam-GPU untuk DETR, penghematan sekitar enam kali.

Kedua, peningkatan terbesar terjadi pada objek kecil: AP-S naik dari 20,5 menjadi 27,1, dan menjadi 29,6 pada varian dua tahap. Bahwa penyebabnya adalah fitur multi-skala, bukan semata attention jarang, tampak dari varian satu skala Deformable DETR yang hanya memperoleh AP-S 20,6 — praktis sama dengan DETR. Ketiga, ada harga yang dibayar: FLOPs naik dari 86 G menjadi 173 G dan laju inferensi turun dari 27,0 menjadi 15,0 FPS, sehingga model dasar lebih lambat daripada DETR standar, walaupun tetap lebih cepat dan lebih akurat daripada DETR-DC5. AP-L sedikit di bawah DETR (59,6 lawan 61,1) karena objek besar memang sudah tertangani baik oleh fitur resolusi rendah; varian dua tahap menutup selisih ini (61,6).

## Kelebihan dan Keterbatasan

Kelebihannya: konvergensi sepuluh kali lebih cepat dari DETR; deteksi objek kecil meningkat besar berkat attention multi-skala tanpa FPN; kompleksitas attention linear terhadap resolusi; dan seluruh rancangan tetap *end-to-end* tanpa anchor maupun NMS. Kombinasi ini menjadikannya dasar bagi hampir seluruh detektor Transformer sesudahnya.

Keterbatasannya: laju 15 FPS masih jauh dari tuntutan *real-time* dan lebih lambat dari DETR standar pada backbone yang sama; operator *sampling* titik fraksional memerlukan kernel CUDA khusus, yang dari sisi rekayasa menyulitkan porting dan optimasi ke perangkat lain; jumlah titik K dan level L adalah hiperparameter rancangan yang harus dipilih manual; dan, secara konseptual, titik referensi awal query masih dipelajari bebas tanpa dikaitkan dengan konten citra, sehingga kesulitan penempatan query tidak hilang sepenuhnya — masalah inilah yang kemudian diserang oleh Conditional DETR, DN-DETR, dan DINO.

## Kaitan dengan Bab Lain

Bab ini mewarisi seluruh kerangka DETR pada [bab 022 - 2020 - DETR](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md) — prediksi himpunan, pencocokan bipartit, object query — dan hanya mengganti modul attention-nya. Garis penerusnya membentuk keluarga besar: [bab 159 - 2022 - DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md) dan [bab 158 - 2023 - DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md) memakai deformable attention yang sama sambil memperbaiki penempatan query; [bab 155 - 2024 - RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md) merekayasa ulang desain ini hingga berjalan *real-time*. Melalui jalur inilah paradigma deteksi *end-to-end* tanpa NMS akhirnya diadopsi keluarga YOLO pada [bab 009 - 2024 - YOLOv10](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `zhu2021deformabledetr`. Ringkasan yang aman dikutip: "Deformable DETR mengganti attention global DETR dengan deformable attention multi-skala — setiap query hanya memperhatikan sejumlah kecil titik sampling yang dipelajari di sekitar titik referensi pada empat level fitur — sehingga konvergensi menjadi sepuluh kali lebih cepat dan akurasi objek kecil meningkat besar; varian dua tahapnya mencapai 46,9 AP pada COCO dengan 50 epoch pelatihan." Catatan verifikasi: seluruh angka pada tabel hasil di atas diambil dari README repositori resmi (hasil reproduksi penulis); README tersebut menyatakan terdapat sedikit perbedaan angka dengan naskah arXiv akibat perpindahan platform kode, sehingga nilai AP persis pada Tabel 2 naskah asli wajib dicocokkan sebelum sitasi formal. Detail implementasi (8 kepala, 4 level, 4 titik per kepala, 300 query, 6+6 lapis, focal loss) diverifikasi dari kode sumber resmi.
