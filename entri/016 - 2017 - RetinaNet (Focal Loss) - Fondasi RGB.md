# 016 - Focal Loss for Dense Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2017focal` |
| Judul asli | Focal Loss for Dense Object Detection |
| Penulis | Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, Piotr Dollár |
| Tahun | 2017 |
| Venue | IEEE International Conference on Computer Vision (ICCV 2017) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1708.02002
- **Google Scholar:** https://scholar.google.com/scholar?q=Focal%20Loss%20for%20Dense%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Focal%20Loss%20for%20Dense%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini menjawab satu pertanyaan spesifik: mengapa detektor objek satu tahap — yang menilai puluhan ribu lokasi kandidat secara padat dalam satu kali evaluasi — selalu tertinggal akurasinya dari detektor dua tahap yang lebih lambat. Penulis menemukan penyebab utamanya bukan arsitektur, melainkan ketidakseimbangan kelas ekstrem antara objek (*foreground*) dan latar (*background*) selama pelatihan: dari sekitar 100.000 lokasi kandidat per citra, hampir semuanya latar yang mudah dikenali, sehingga loss total didominasi contoh tanpa sinyal belajar.

Sebagai solusi diusulkan *focal loss*, modifikasi fungsi loss entropi silang yang menekan kontribusi contoh mudah sehingga pelatihan terfokus pada contoh sulit. Untuk mengujinya dibangun RetinaNet, detektor satu tahap berbasis ResNet dan piramida fitur, yang mencapai 39,1 AP pada tolok ukur COCO — melampaui semua detektor dua tahap saat itu — dengan kecepatan khas detektor satu tahap.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Detektor dua tahap bekerja dengan kaskade: tahap pertama mengusulkan 1.000–2.000 kandidat wilayah (*region proposal*), tahap kedua mengklasifikasikannya sebagai objek atau latar (bab 012–014). Kaskade ini sekaligus mengendalikan ketidakseimbangan kelas: proposal membuang mayoritas lokasi latar, dan contoh positif-negatif untuk melatih tahap kedua dipilih dengan rasio tetap, misalnya 1:3, sehingga *minibatch* (kumpulan contoh per langkah pelatihan) tetap seimbang.

Detektor satu tahap tidak memiliki saringan semacam itu. YOLO (bab 001, bab 002) dan SSD (bab 015) mengevaluasi kandidat pada kisi padat yang mencakup semua posisi, skala, dan rasio aspek, sekitar 100.000 lokasi per citra. Akurasinya tertinggal: SSD 10–20% lebih rendah AP-nya daripada detektor dua tahap, dan YOLO lebih jauh lagi. Teknik *hard example mining* — hanya contoh ber-loss tinggi yang dipakai melatih — kurang efektif karena pemilihannya heuristik, bukan dari dalam fungsi loss.

Akar persoalannya ada pada fungsi loss standar. Entropi silang (*cross-entropy*, CE) menghukum setiap prediksi yang keliru, tetapi contoh latar yang sudah dikenali benar pun tetap menyumbang loss kecil yang tidak nol. Dengan ±100.000 contoh latar per citra, nilai kecil ini berakumulasi dan mendominasi gradien (sinyal pembaruan bobot jaringan), sehingga sinyal contoh objek yang langka tertutup. Akibatnya model terdorong ke solusi degeneratif: memprediksi "latar" di mana-mana.

## Ide Utama

Gagasan inti makalah ini: jangan menyaring contoh, tetapi bentuk ulang fungsi loss-nya. *Focal loss* (FL) menambahkan faktor pemodulasi (1 − *p_t*)^γ pada entropi silang, dengan *p_t* adalah probabilitas yang diberikan model untuk kelas yang benar dan γ ≥ 0 adalah parameter pemfokus. Konsekuensinya bersifat mekanis: contoh yang sudah diklasifikasikan benar dengan yakin (*p_t* mendekati 1) menerima loss yang dikalikan faktor mendekati nol, sedangkan contoh yang salah atau ragu (*p_t* kecil) mempertahankan loss hampir utuh. Dengan demikian, contoh latar mudah tetap ikut dilatih, tetapi sumbangannya terhadap gradien diredam; pelatihan terpusat pada sedikit contoh sulit tanpa heuristik pemilihan apa pun.

## Cara Kerja Langkah demi Langkah

### Dari Entropi Silang ke Focal Loss

Untuk klasifikasi biner, entropi silang ditulis CE(*p_t*) = −log(*p_t*), dengan *p_t* = *p* bila label sebenarnya positif dan *p_t* = 1 − *p* bila negatif; *p* adalah keluaran probabilitas model. Loss ini besar saat prediksi salah, tetapi tidak pernah nol untuk prediksi benar: contoh latar dengan *p_t* = 0,9 masih menyumbang −log(0,9) ≈ 0,105.

Focal loss mengalikan loss tersebut dengan (1 − *p_t*)^γ:

FL(*p_t*) = −(1 − *p_t*)^γ · log(*p_t*)

Dua sifat menentukan perilakunya. Pertama, faktor (1 − *p_t*)^γ mendekati 1 untuk contoh salah klasifikasi, sehingga loss-nya tidak berubah, dan meluruh ke 0 untuk contoh mudah. Kedua, γ mengatur laju peluruhan: γ = 0 membuat FL identik dengan CE. Dengan γ = 2 — nilai yang dipakai pada seluruh eksperimen utama — contoh ber-*p_t* = 0,9 menerima loss 100 kali lebih kecil daripada pada CE, dan contoh ber-*p_t* ≈ 0,968 menerima loss 1.000 kali lebih kecil. Sebaliknya, contoh sulit (*p_t* ≤ 0,5) paling banyak ditekan 4 kali lipat.

Versi yang dipakai dalam praktik menambah bobot penyeimbang kelas α: FL(*p_t*) = −α_t(1 − *p_t*)^γ log(*p_t*), dengan α_t = α untuk kelas objek dan 1 − α untuk latar. Untuk γ = 2, α = 0,25 memberi hasil terbaik.

### Inisialisasi dengan Prior π

Pada awal pelatihan, model menghasilkan probabilitas sekitar 0,5 di semua lokasi, sehingga 100.000 contoh latar langsung menghasilkan loss besar yang mengacaukan iterasi pertama — percobaan dengan CE polos divergen (tidak konvergen). Solusinya bukan mengubah loss, melainkan inisialisasi: *bias* lapis terakhir subnet klasifikasi diisi *b* = −log((1 − π)/π) dengan π = 0,01, sehingga model memulai pelatihan dengan keyakinan rendah bahwa suatu lokasi berisi objek; ini menstabilkan pelatihan untuk CE maupun FL.

### Arsitektur RetinaNet

RetinaNet terdiri atas satu *backbone* (jaringan ekstraksi fitur) dan dua subnet tugas. Backbone-nya ResNet — jaringan konvolusi berkoneksi pintas antar-lapis yang memungkinkan pelatihan jaringan sangat dalam — dipasangi FPN (*Feature Pyramid Network*, bab 018): modul yang membangun piramida fitur multi-skala dari satu citra melalui jalur *top-down* dan koneksi lateral. Piramida yang dipakai mencakup level P3 sampai P7, masing-masing 256 kanal; level P_l beresolusi 1/2^l dari citra masukan. Pada setiap posisi piramida ditempatkan sembilan anchor, yaitu kotak acuan berukuran tetap yang digeser jaringan menjadi kotak objek.

Alur data RetinaNet dari citra masukan sampai deteksi akhir:

```
citra masukan (sisi pendek 600-800 piksel)
                │
                ▼
┌──────────────────────┐   FPN: jalur top-down + koneksi lateral
│ ResNet (C3..C5)      │──► piramida P3..P7, 256 kanal per level
└──────────────────────┘   (level P_l beresolusi 1/2^l dari citra)
                │
                ▼   tiap posisi tiap level: A = 9 anchor
                │   (3 rasio x 3 skala; sisi efektif 32-813 piksel)
   ┌────────────┴────────────┐
   ▼                         ▼
┌─────────────────────┐ ┌─────────────────────┐
│ subnet klasifikasi  │ │ subnet regresi box  │
│ 4x konv 3x3 (256)   │ │ 4x konv 3x3 (256)   │
│ konv KA + sigmoid   │ │ konv 4A (linear)    │
│ ► prob. kelas/anchor│ │ ► offset ke box     │
└─────────────────────┘ └─────────────────────┘
   │                         │
   └────────────┬────────────┘
                ▼
 ambang 0,05 ► maks. 1000 prediksi/level ► NMS 0,5
                ▼
          deteksi akhir
```

Kedua subnet adalah jaringan konvolusi kecil yang diterapkan padat pada setiap level piramida, dengan bobot yang sama lintas level. Subnet klasifikasi memprediksi probabilitas keberadaan objek untuk setiap anchor pada K kelas (K = 80 untuk COCO); keluarannya melewati fungsi sigmoid — aktivasi yang memetakan nilai ke rentang probabilitas 0–1 — sehingga tiap kelas diprediksi independen. Subnet regresi memprediksi 4 offset per anchor yang menggeser anchor menuju *bounding box* (kotak pembatas objek) kebenaran; regresor ini *class-agnostic* — satu set offset dipakai untuk semua kelas — dan parameternya terpisah dari subnet klasifikasi.

### Anchor dan Perhitungan Loss

Sembilan anchor per posisi terdiri atas 3 rasio aspek {1:2, 1:1, 2:1} dikali 3 skala {2^0, 2^(1/3), 2^(2/3)} dari luas dasar 32² sampai 512² piksel, sehingga seluruhnya mencakup objek bersisi 32–813 piksel. Totalnya sekitar 100.000 anchor per citra. Saat pelatihan, anchor diberi label dengan ambang IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak): IoU ≥ 0,5 terhadap objek berarti positif; IoU di bawah 0,4 berarti latar; selebihnya diabaikan.

Focal loss dihitung atas **semua** ±100.000 anchor per citra — berbeda dengan praktik umum yang hanya memilih ratusan contoh per minibatch. Loss total satu citra dinormalisasi dengan jumlah anchor positif, bukan total anchor, karena kontribusi anchor latar mudah sudah diredam oleh faktor pemodulasi. Loss regresi box memakai *smooth* L1 standar. Model dilatih dengan SGD (*stochastic gradient descent*) pada 8 GPU, 16 citra per minibatch, 90.000 iterasi, laju pembelajaran awal 0,01 yang dibagi sepuluh pada iterasi ke-60.000 dan ke-80.000.

### Inferensi

Inferensi adalah satu kali propagasi maju. Demi kecepatan, hanya prediksi berkeyakinan di atas 0,05 yang diolah menjadi kotak, maksimal 1.000 prediksi teratas per level; hasil semua level digabung, lalu dirampingkan dengan NMS (*Non-Maximum Suppression* — dari sekumpulan kotak yang saling menutupi, hanya kotak berskor tertinggi yang dipertahankan) dengan ambang 0,5.

## Eksperimen dan Hasil

Seluruh eksperimen dilakukan pada COCO (80 kelas); ablasi dilaporkan pada split *minival* (5.000 citra), hasil utama pada split *test-dev*. Metriknya adalah AP COCO, rata-rata presisi pada ambang IoU 0,50 sampai 0,95.

Ablasi fungsi loss (ResNet-50, skala 600 piksel) menunjukkan kontribusi tiap komponen. Dengan inisialisasi π, CE mencapai 30,2 AP. Menambah penyeimbang α terbaik (α = 0,75) hanya menaikkan 0,9 poin menjadi 31,1 AP — pembobotan kelas statis ternyata tidak cukup. Focal loss (γ = 2) menghasilkan 34,0 AP, lonjakan 2,9 poin dari jaringan yang sama, dan hasilnya stabil untuk γ antara 0,5 sampai 5. Dibandingkan dengan OHEM (*Online Hard Example Mining*, pemilihan contoh ber-loss tertinggi per minibatch) pada ResNet-101: OHEM terbaik mencapai 32,8 AP, FL mencapai 36,0 AP — selisih 3,2 poin untuk pendekatan berbasis loss. Analisis distribusi loss model konvergen menjelaskan mekanismenya: dengan γ = 2, hampir seluruh loss contoh negatif terkonsentrasi pada sebagian kecil contoh sulit. Pada ablasi kepadatan anchor: satu anchor per posisi menghasilkan 30,3 AP, sembilan anchor menaikkannya menjadi 34,0 AP, dan kepadatan lebih tinggi tidak lagi menambah hasil.

RetinaNet-101 pada skala 600 piksel menyamai akurasi Faster R-CNN berbasis FPN dengan 122 ms per citra dibandingkan 172 ms (GPU Nvidia M40) — waktu proses ±29% lebih singkat pada akurasi setara. Pada COCO test-dev, RetinaNet-101-FPN skala 800 piksel mencapai **39,1 AP** (5 FPS): mengungguli detektor satu tahap terkuat saat itu, DSSD513 (33,2; selisih 5,9), maupun dua tahap terbaik, Faster R-CNN-TDM (36,8; selisih 2,3); YOLOv2 (21,6) dan SSD513 (31,2) jauh di bawahnya. Mengganti backbone dengan ResNeXt-101-FPN menaikkan hasil menjadi **40,8 AP** — konfigurasi pertama yang menembus 40 AP pada COCO. Rincian per ukuran objek: AP objek besar 50,2, sedang 42,7, tetapi kecil hanya 21,8 — objek kecil tetap tersulit sekalipun piramida fitur dipakai.

## Kelebihan dan Keterbatasan

Kelebihan utamanya adalah kesederhanaan dan generalitas: focal loss hanya perubahan kecil pada fungsi loss, tanpa pemilihan contoh heuristik, dan ortogonal terhadap arsitektur sehingga mudah dipindahkan ke detektor lain. RetinaNet membuktikan bahwa selisih akurasi antara detektor satu tahap dan dua tahap bukan batasan mendasar, melainkan artefak cara melatih.

Keterbatasannya: (1) hiperparameter α dan γ saling berinteraksi dan harus disetel bersama; (2) RetinaNet tetap berbasis anchor dan mewarisi kerumitan penyetelannya, biarpun ablasi menunjukkan hasil jenuh setelah sembilan anchor per posisi; (3) penulis menyatakan rezim *frame rate* tinggi di luar cakupan makalah — model terbaik berjalan 5 FPS dan titik tercepatnya masih lebih lambat dari YOLOv2; (4) dari sisi rekayasa, pelatihan memerlukan 10–35 jam pada 8 GPU, biaya yang tidak kecil untuk reproduksi; (5) secara konseptual, focal loss mengendalikan dominansi contoh mudah pada klasifikasi, tetapi tidak menyentuh kesulitan lokalisasi objek kecil (AP 21,8, jauh di bawah AP objek besar 50,2).

## Kaitan dengan Bab Lain

Bab ini mewarisi tiga gagasan dari bab-bab sebelumnya: konsep anchor dari RPN pada [Faster R-CNN (bab 014)](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md), piramida fitur multi-skala dari [FPN (bab 018)](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20%28FPN%29%20-%20Fondasi%20RGB.md) yang berasal dari kelompok riset yang sama, dan formulasi deteksi padat satu tahap dari [YOLOv1 (bab 001)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), [YOLOv2 (bab 002)](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md), serta [SSD (bab 015)](./015%20-%202016%20-%20SSD%20-%20Fondasi%20RGB.md) — sekaligus menjawab mengapa ketiga pendahulu itu tertinggal akurasinya.

Pengaruhnya mengalir ke dua arah. Ke arah detektor satu tahap: focal loss menjadi komponen standar yang diadopsi banyak detektor berikutnya, antara lain [EfficientDet (bab 021)](./021%20-%202020%20-%20EfficientDet%20-%20Fondasi%20RGB.md), sedangkan ketergantungannya pada anchor menjadi motif detektor *anchor-free* seperti [FCOS (bab 019)](./019%20-%202019%20-%20FCOS%20-%20Fondasi%20RGB.md) dan [CenterNet (bab 020)](./020%20-%202019%20-%20CenterNet%20%28Objects%20as%20Points%29%20-%20Fondasi%20RGB.md). Ke arah detektor dua tahap: RetinaNet menjadi pembanding langsung [Mask R-CNN (bab 017)](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md) dan menegaskan bahwa dengan fungsi loss yang tepat, pipeline satu tahap tidak lagi harus mengalah pada kaskade proposal.

## Poin untuk Sitasi

Kutip dengan kunci `lin2017focal`. Ringkasan yang aman dikutip: "Lin dkk. mengidentifikasi ketidakseimbangan kelas foreground-background sebagai penyebab utama ketertinggalan akurasi detektor satu tahap, dan mengusulkan focal loss — entropi silang yang dimodulasi faktor (1 − *p_t*)^γ — untuk menekan kontribusi contoh mudah; detektor RetinaNet yang dilatih dengan loss ini mencapai 39,1 AP pada COCO test-dev, melampaui detektor dua tahap terbaik pada masanya." Seluruh angka pada bab ini diambil dari naskah arXiv versi 2; sebelum sitasi formal, cocokkan tabel hasil dengan versi terbit ICCV 2017 (halaman 2980–2988). Daftar penulis pada lembar telaah lama terpotong; kelimanya adalah Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, dan Piotr Dollár.
