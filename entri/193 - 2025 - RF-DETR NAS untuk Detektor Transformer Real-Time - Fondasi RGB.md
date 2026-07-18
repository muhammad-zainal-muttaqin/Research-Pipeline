# 193 - RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `robinson2025rfdetr` |
| Judul asli | RF-DETR: Neural Architecture Search for Real-Time Detection Transformers |
| Penulis | Isaac Robinson, Peter Robicheaux, Matvei Popov, Deva Ramanan, Neehar Peri |
| Tahun | 2025 (diterima ICLR 2026) |
| Venue | arXiv preprint (diterima *International Conference on Learning Representations*, ICLR 2026) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2511.09554
- **Kode sumber resmi (Roboflow):** https://github.com/roboflow/rf-detr
- **Google Scholar:** https://scholar.google.com/scholar?q=RF-DETR%3A%20Neural%20Architecture%20Search%20for%20Real-Time%20Detection%20Transformers

## Gambaran Umum

Makalah ini memperkenalkan RF-DETR, sebuah keluarga detektor objek berbasis DETR (*Detection Transformer*, arsitektur deteksi yang memakai mekanisme *attention* untuk memetakan fitur citra langsung ke sekumpulan kotak objek tanpa NMS) yang dirancang lewat *neural architecture search* (NAS, pencarian otomatis konfigurasi arsitektur jaringan) berbagi bobot. Alih-alih menetapkan satu arsitektur tetap, metode ini melatih satu jaringan dasar yang dapat dikonfigurasi ulang, lalu mengevaluasi ribuan variasi ukuran dan kedalaman tanpa melatih ulang dari nol, sehingga diperoleh kurva Pareto akurasi-latensi (kumpulan konfigurasi yang masing-masing optimal pada titik kompromi kecepatan-akurasi tertentu) untuk kumpulan data target.

Model dibangun di atas *backbone* (jaringan ekstraksi fitur awal) DINOv2, sebuah *vision transformer* yang dilatih tanpa label lewat *self-supervised learning* pada citra dalam jumlah besar. Hasil utama: varian RF-DETR *nano* mencapai 48,0 AP (*Average Precision*, metrik deteksi objek standar yang merangkum presisi pada berbagai ambang IoU) pada COCO dengan latensi 2,3 ms, mengungguli D-FINE *nano* sebesar 5,3 AP pada latensi yang setara; varian 2x-large mencapai 60,1 AP pada COCO, disebut penulis sebagai detektor *real-time* pertama yang melampaui 60 AP. Pada RF100-VL, kumpulan seratus dataset domain berbeda yang dipakai untuk menguji generalisasi lintas domain, varian 2x-large mengungguli GroundingDINO *tiny* sebesar 1,2 AP sambil berjalan sekitar 20 kali lebih cepat.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak RT-DETR (bab 155) menunjukkan bahwa arsitektur DETR dapat berjalan *real-time* dan menyaingi kecepatan keluarga YOLO, sejumlah detektor DETR generasi berikut seperti D-FINE dan DEIM memperbaiki akurasi pada COCO dengan teknik regresi kotak dan strategi pencocokan label yang lebih halus. Menurut penulis makalah ini, detektor-detektor tersebut cenderung disetel secara khusus untuk COCO — lewat kombinasi arsitektur, jadwal pelatihan (*scheduler*), dan augmentasi data yang dipilih agar cocok dengan karakteristik COCO — sehingga performanya kurang stabil ketika dipindahkan ke dataset dunia nyata dengan distribusi kelas dan ukuran objek yang berbeda.

Di sisi lain, detektor *open-vocabulary* (mengenali kelas objek berdasarkan deskripsi teks tanpa dilatih ulang) seperti GroundingDINO memiliki generalisasi lintas domain yang baik karena dilatih pada data teks-citra berskala besar, tetapi ukurannya berat dan latensinya jauh dari *real-time* — makalah ini mencatat latensi GroundingDINO *tiny* sekitar 309,9 ms per citra pada perangkat uji yang sama, dibandingkan RF-DETR 2x-large yang hanya 15,6 ms. Masalah yang hendak dipecahkan adalah menyediakan satu keluarga model yang sekaligus cepat, akurat pada COCO, dan mudah disetel-halus (*fine-tuning*, melanjutkan pelatihan model yang sudah dilatih pada tugas atau data baru) ke domain baru tanpa perlu merancang ulang arsitektur secara manual untuk setiap kebutuhan latensi.

## Ide Utama

Gagasan inti RF-DETR adalah memisahkan proses pelatihan bobot dari proses pemilihan arsitektur. Satu jaringan dasar dilatih sedemikian rupa sehingga sebagian besar bobotnya dapat dipakai bersama oleh banyak konfigurasi arsitektur yang berbeda — inilah yang dimaksud NAS berbagi bobot (*weight-sharing NAS*). Pada setiap langkah pelatihan, sebuah konfigurasi acak (misalnya jumlah lapis *decoder* tertentu, resolusi citra tertentu, jumlah kueri objek tertentu) dipilih dari ruang pencarian, dan hanya bagian jaringan yang relevan dengan konfigurasi itu yang diperbarui gradiennya pada langkah tersebut.

Setelah pelatihan dasar selesai, ribuan kombinasi konfigurasi dapat dievaluasi pada data validasi tanpa pelatihan ulang, karena setiap konfigurasi hanya memakai subset bobot yang sudah terlatih bersama. Konsekuensinya, satu proses pelatihan menghasilkan bukan satu model melainkan satu spektrum model dengan trade-off akurasi-latensi berbeda, dan pengguna dapat memilih titik pada spektrum itu sesuai anggaran komputasi yang tersedia — dari varian *nano* yang sangat ringan sampai varian 2x-large yang paling akurat.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dasar

RF-DETR memperluas LW-DETR (*Lightweight DETR*, arsitektur DETR ringan pendahulu yang memakai *backbone* ViT dan *decoder* dengan *deformable cross-attention*, yaitu mekanisme atensi yang hanya menyampel sejumlah kecil titik fitur di sekitar posisi prediksi alih-alih seluruh peta fitur). Tiga perubahan utama dari LW-DETR: *backbone* CAEv2 diganti DINOv2 (ViT 12 lapis dengan bobot pra-latih yang lebih kuat), lapis normalisasi batch diganti *layer normalization* agar pelatihan stabil pada GPU kelas konsumen, dan ditambahkan kepala segmentasi ringan berbasis prototipe untuk varian yang juga melakukan segmentasi instans. Blok *attention* dalam *backbone* menyelang-nyelingkan (*interleave*) blok atensi berjendela (*windowed attention*, atensi dihitung hanya dalam jendela lokal untuk menghemat komputasi) dengan blok atensi penuh, untuk menyeimbangkan kecepatan dan kemampuan menangkap konteks global.

### Ruang Pencarian NAS

Lima dimensi arsitektur menjadi target pencarian: ukuran *patch* citra (gaya FlexiViT, memungkinkan *patch* — potongan citra berukuran tetap yang menjadi unit token masukan ViT — diinterpolasi ke ukuran berbeda tanpa melatih ulang), resolusi citra masukan pada rentang skala tertentu, jumlah lapis *decoder* (lapis yang menerjemahkan fitur menjadi prediksi kotak dan kelas), jumlah token kueri objek yang dipertahankan (token kueri berkeyakinan rendah dapat dibuang untuk mengurangi komputasi), serta jumlah blok atensi berjendela dalam *backbone*. Selama pencarian pasca-pelatihan, kombinasi nilai pada kelima dimensi ini dievaluasi untuk memetakan trade-off akurasi-latensi.

### Pelatihan Tanpa Jadwal Tetap

Penulis menyebut proses pelatihannya *scheduler-free* karena tidak memakai jadwal laju-belajar kosinus konvensional, yang menurut mereka mengasumsikan cakrawala optimasi (jumlah total langkah pelatihan) tetap dan diketahui sejak awal — asumsi yang tidak praktis ketika model yang sama akan disetel-halus pada dataset target dengan ukuran sangat bervariasi. Sebagai gantinya dipakai skema rata-rata bergerak eksponensial (*EMA*, *exponential moving average*, menyimpan versi bobot yang dihaluskan dari waktu ke waktu) tanpa fase pemanasan (*warmup*). Augmentasi data dijaga tetap sederhana — hanya pembalikan horizontal dan pemotongan (*crop*) — karena augmentasi lain seperti pembalikan vertikal dapat merusak makna semantik objek pada dataset dunia nyata. Laju belajar ditetapkan lebih rendah (1e-4) dibandingkan LW-DETR (4e-4) agar bobot pra-latih DINOv2 tidak rusak pada tahap awal.

Skema alur dari satu jaringan dasar menjadi banyak konfigurasi yang dievaluasi:

```
   pelatihan dasar (bobot dibagi bersama)
   setiap langkah: sampel 1 konfigurasi acak
       (jumlah lapis decoder, resolusi, kueri, ...)
       -> update gradien hanya pada subset bobot itu
                    |
                    v
   pasca-pelatihan: evaluasi ribuan konfigurasi
   tanpa latih ulang, hasilkan kurva Pareto
                    |
   ┌────────┬────────┬─────────┬─────────┬──────────┐
   │  nano   │ small  │ medium  │ large   │ 2x-large │
   │ 2,3 ms  │ 3,5 ms │ 4,4 ms  │  ...    │ 17,2 ms  │
   │ 48,0 AP │52,9 AP │54,7 AP  │  ...    │ 60,1 AP  │
   └────────┴────────┴─────────┴─────────┴──────────┘
```

### Protokol Pengukuran Latensi

Latensi diukur pada GPU NVIDIA T4 dengan TensorRT 10.4 dan CUDA 12.4. Penulis menambahkan jeda 200 ms antar-*forward pass* saat pengukuran untuk mencegah GPU menurunkan frekuensi kerjanya akibat *throttling* daya, yang bila diabaikan dapat membuat angka latensi tampak lebih baik dari kondisi penggunaan nyata. Karena variansi kompilasi TensorRT, angka latensi hanya dilaporkan sampai satu angka desimal.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada COCO (untuk akurasi deteksi standar) dan RF100-VL (Roboflow100-VL, kumpulan seratus dataset dari domain berbeda-beda seperti citra medis, industri, dan satelit, dipakai untuk mengukur generalisasi lintas domain), dibandingkan dengan D-FINE dan GroundingDINO pada anggaran latensi yang sepadan.

Pada COCO, RF-DETR *nano* mencapai 48,0 AP pada latensi 2,3 ms, mengungguli D-FINE *nano* (42,7 AP, 2,1 ms) sebesar 5,3 AP dengan latensi hampir setara — keunggulan akurasi yang besar untuk selisih kecepatan yang dapat diabaikan. Varian *small* mencapai 52,9 AP (3,5 ms) melawan D-FINE *small* 50,6 AP (3,5 ms). Pada varian *medium*, RF-DETR sedikit tertinggal dari D-FINE (54,7 AP berbanding 55,0 AP) tetapi dengan latensi lebih rendah (4,4 ms berbanding 5,4 ms), sehingga tetap unggul pada trade-off gabungan. Varian 2x-large mencapai 60,1 AP pada 17,2 ms — angka yang menurut penulis menjadikannya detektor *real-time* pertama yang melampaui ambang 60 AP pada COCO.

Pada RF100-VL, hasilnya lebih beragam: RF-DETR *nano* (57,6 AP) sedikit di bawah D-FINE *nano* (58,2 AP), tetapi varian *small* dan yang lebih besar unggul — RF-DETR *small* mencapai 60,7 AP berbanding D-FINE *small* 60,3 AP. Perbandingan paling mencolok ada pada varian 2x-large: 63,3 AP berbanding GroundingDINO *tiny* 62,3 AP, dengan latensi 15,6 ms berbanding 309,9 ms — RF-DETR unggul tipis dalam akurasi sekaligus sekitar 20 kali lebih cepat. Interpretasinya: keunggulan RF-DETR pada RF100-VL menegaskan bahwa NAS berbagi bobot bersama pra-pelatihan skala besar membantu transfer ke domain di luar COCO, bukan hanya menghasilkan model yang disetel ketat untuk satu dataset.

Kajian ablasi menelusuri sumber kenaikan akurasi: pelonggaran hiperparameter pelatihan saja sempat menurunkan akurasi 1,0 AP, penggantian *backbone* ke DINOv2 memulihkan 2,0 AP, dan NAS berbagi bobot menambah 0,3 AP lagi. Perbandingan *backbone* menunjukkan DINOv2 ViT-S/14 mencapai 54,3 AP, mengungguli CAEv2 (52,3 AP). Makalah juga melaporkan segmentasi instans pada COCO: RF-DETR-Seg *nano* mencapai 40,3 AP dibandingkan YOLOv8 *nano* (28,3 AP) dan YOLOv11 *nano* (30,0 AP) pada latensi sebanding, meskipun angka ini berasal dari eksperimen tambahan di luar fokus utama deteksi objek.

## Kelebihan dan Keterbatasan

Kelebihan utama RF-DETR adalah efisiensi proses perancangan: satu siklus pelatihan menghasilkan seluruh spektrum model dari *nano* sampai 2x-large, tanpa perlu melatih ulang untuk setiap titik pada kurva Pareto akurasi-latensi. Generalisasi lintas domain pada RF100-VL menunjukkan bahwa pendekatan ini tidak hanya cocok dengan karakteristik statistik COCO, sebuah kelemahan yang menurut penulis melekat pada beberapa detektor DETR real-time sebelumnya. Protokol pengukuran latensi yang eksplisit menyebut *throttling* GPU dan variansi kompilasi menambah kredibilitas angka yang dilaporkan.

Dari sisi rekayasa, makalah tidak mengkuantifikasi total biaya komputasi proses NAS itu sendiri, sehingga sulit menilai sumber daya pengembang yang dibutuhkan sebelum model siap dipakai — berbeda dari biaya inferensi yang dilaporkan rinci. Secara konseptual, keunggulan RF-DETR pada varian *medium* terhadap D-FINE tidak konsisten pada semua sumbu (AP sedikit kalah, latensi menang), menunjukkan trade-off ini bukan kemenangan mutlak di setiap ukuran model. Makalah juga mengakui keterbatasan ketersediaan *backbone* ringan: keluarga model fondasi seperti DINOv2 umumnya tidak merilis varian ViT-T atau ViT-S sekecil yang idealnya dibutuhkan untuk konfigurasi *nano*, sehingga ruang pencarian NAS pada ujung paling ringan tetap dibatasi oleh bobot pra-latih pihak ketiga yang tersedia.

## Kaitan dengan Bab Lain

RF-DETR meneruskan garis detektor DETR *real-time* yang dimulai dari [bab 155 (RT-DETR)](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md), yang pertama membuktikan arsitektur DETR dapat menyaingi kecepatan YOLO, dan berbagi akar konseptual mekanisme *deformable cross-attention* dengan [bab 165 (Co-DETR)](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md), yang memperbaiki konvergensi pelatihan DETR lewat kepala pelatihan kolaboratif. Perbedaan RF-DETR dari kedua pendahulu itu terletak pada penambahan dimensi NAS berbagi bobot sehingga satu pelatihan menghasilkan banyak konfigurasi, bukan satu arsitektur tetap.

Dalam klaster detektor 2025-2026 pada tinjauan ini, RF-DETR berdampingan dengan [bab 192 (YOLO26)](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md), yang mengejar tujuan *real-time end-to-end* tanpa NMS dari jalur arsitektur satu-tahap konvensional, dan [bab 194 (Le-DETR)](./194%20-%202026%20-%20Le-DETR%20Encoder%20Efisien%20untuk%20DETR%20Real-Time%20-%20Fondasi%20RGB.md), yang menyasar efisiensi *encoder* pada arsitektur DETR real-time dengan pendekatan berbeda dari pencarian arsitektur. Ketiga bab ini bersama-sama menggambarkan dua jalur paralel menuju detektor *real-time* pada 2025-2026: penyempurnaan arsitektur DETR (RF-DETR, Le-DETR) berhadapan dengan penyempurnaan lanjutan keluarga YOLO (YOLO26).

## Poin untuk Sitasi

Kutip dengan kunci `robinson2025rfdetr`. Ringkasan aman dikutip: "RF-DETR memakai NAS berbagi bobot di atas *backbone* DINOv2 untuk menghasilkan keluarga detektor DETR real-time dari satu siklus pelatihan, mencapai 48,0 AP (nano, 2,3 ms) dan 60,1 AP (2x-large, 17,2 ms) pada COCO, serta mengungguli GroundingDINO tiny sebesar 1,2 AP pada RF100-VL sambil berjalan sekitar 20 kali lebih cepat." Seluruh angka pada bagian Eksperimen dan Hasil diambil dari versi arXiv/HTML makalah (2511.09554), diproses lewat alat pembaca otomatis, bukan pembacaan langsung tabel PDF asli. Karena makalah ini sangat baru dan berstatus preprint menjelang ICLR 2026, seluruh angka wajib diverifikasi ulang terhadap versi final sebelum dikutip formal. Biaya komputasi total proses NAS tidak dilaporkan dalam sumber yang diakses dan tidak boleh diasumsikan.
