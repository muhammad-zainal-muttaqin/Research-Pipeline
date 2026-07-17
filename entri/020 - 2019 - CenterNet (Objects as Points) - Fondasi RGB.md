# 020 - Objects as Points

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2019objects` |
| Judul asli | Objects as Points |
| Penulis | Xingyi Zhou, Dequan Wang, Philipp Krähenbühl |
| Tahun | 2019 |
| Venue | arXiv preprint arXiv:1904.07850 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1904.07850
- **Google Scholar:** https://scholar.google.com/scholar?q=Objects%20as%20Points
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Objects%20as%20Points&sort=relevance
- **Repositori kode resmi:** https://github.com/xingyizhou/CenterNet

## Gambaran Umum

Makalah ini memperkenalkan CenterNet, detektor objek yang merepresentasikan setiap objek sebagai satu titik, yaitu titik pusat kotak pembatasnya (*bounding box*). Deteksi dirumuskan ulang sebagai estimasi *keypoint* (titik kunci): sebuah jaringan konvolusi penuh menghasilkan *heatmap* (peta skor per piksel) yang puncaknya menandai pusat objek pada tiap kelas, sedangkan ukuran kotak dan koreksi posisi sub-piksel diregresi langsung dari fitur pada lokasi puncak. Karena satu objek hanya diwakili satu puncak, tahap enumerasi kandidat kotak (*anchor*) dan pasca-pemrosesan *Non-Maximum Suppression* (NMS) tidak lagi diperlukan.

Kerangka yang sama, tanpa perubahan struktural, juga dipakai untuk estimasi kotak 3D monokular dan pose manusia multi-orang; cukup dengan menambah kanal keluaran pada titik pusat. Pada tolok ukur MS COCO, CenterNet mencapai 37,4% AP pada 52 FPS dengan *backbone* DLA-34 dan 45,1% AP dengan pengujian multi-skala pada 1,4 FPS — kombinasi kecepatan-akurasi terbaik di antara detektor satu tahap pada tahun publikasinya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hingga 2019, detektor objek yang paling berhasil memandang deteksi sebagai klasifikasi atas enumerasi besar kandidat kotak. Detektor dua tahap dari keluarga R-CNN (bab 012 dan 013) mengusulkan ribuan wilayah kandidat lalu mengklasifikasikannya satu per satu. Detektor satu tahap seperti YOLOv3 (bab 003), SSD (bab 015), dan RetinaNet (bab 016) menyebarkan puluhan ribu *anchor box* — kotak acuan berukuran dan berrasio tetap — pada setiap citra, lalu mengklasifikasikan dan menyesuaikan masing-masing secara langsung.

Pola enumerasi ini membawa tiga masalah. Pertama, boros: hampir semua kandidat tidak menutupi objek apa pun, sehingga muncul ketidakseimbangan contoh positif-negatif yang harus ditangani dengan teknik khusus seperti *focal loss*. Kedua, penetapan label positif-negatif bergantung pada ambang IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak) yang ditetapkan manual; pada Faster R-CNN (bab 014), sebuah anchor berlabel positif bila IoU-nya di atas 0,7 terhadap objek dan negatif bila di bawah 0,3. Ketiga, satu objek biasanya terdeteksi oleh banyak kandidat, sehingga hasil harus dirampingkan dengan NMS, operasi berbasis IoU yang tidak dapat diturunkan (*differentiable*); akibatnya detektor tidak sepenuhnya terlatih *end-to-end* (satu proses optimasi dari masukan ke keluaran).

Jalur bebas anchor melalui estimasi *keypoint* sudah ditempuh lebih dulu: CornerNet (2018) mendeteksi pasangan sudut kotak dan ExtremeNet (2019) mendeteksi empat titik ekstrem ditambah pusat. Keduanya menghapus anchor, tetapi memerlukan pengelompokan kombinatorial untuk memasangkan titik milik objek yang sama — tahap yang memperlambat inferensi dan menambah kerumitan.

## Ide Utama

Satu objek cukup diwakili satu titik: pusat kotaknya. Dengan representasi ini, deteksi menjadi masalah estimasi *keypoint* standar, persoalan yang saat itu sudah diselesaikan dengan baik pada estimasi pose manusia. Masukan berupa citra; keluaran berupa *heatmap* per kelas; setiap puncak lokal pada heatmap adalah satu deteksi. Semua properti objek yang lain — lebar dan tinggi kotak, koreksi posisi, hingga atribut 3D dan posisi sendi — diregresi dari vektor fitur tepat pada titik pusat tersebut.

Dalam tafsir yang menjembatani paradigma lama, titik pusat dapat dipandang sebagai satu *anchor* tunggal tanpa bentuk, dengan tiga perbedaan: penetapannya hanya berdasarkan lokasi, tanpa ambang IoU; hanya ada satu kandidat positif per objek; dan resolusi keluaran dinaikkan (*stride* 4, bukan 16), sehingga satu lokasi cukup untuk objek segala ukuran. Konsekuensinya, NMS tidak dibutuhkan dan pencarian puncak lokal menggantikan fungsinya.

## Cara Kerja Langkah demi Langkah

### Heatmap Pusat

Keluaran inti CenterNet adalah *heatmap* berukuran (W/R)×(H/R)×C, dengan W×H ukuran citra masukan, R = 4 adalah *output stride* (faktor pengecilan spasial), dan C jumlah kelas (C = 80 pada COCO). Nilai 1 pada suatu posisi menandakan pusat objek; nilai 0 berarti latar. Untuk pelatihan, pusat kebenaran p dipetakan ke resolusi rendah: p̃ = ⌊p/R⌋. Contoh: pada citra 512×512, heatmap berukuran 128×128; pusat objek pada piksel (200, 300) jatuh pada posisi (50, 75).

Titik kebenaran tidak ditandai sebagai satu piksel biner, melainkan disebarkan sebagai gundukan fungsi Gaussian: nilai target pada posisi sekitar p̃ berbentuk exp(−jarak²/(2σ²)), dengan simpangan baku σ yang menyesuaikan ukuran objek mengikuti aturan CornerNet — radius dipilih sehingga kotak apa pun yang pusatnya berada dalam radius itu masih memiliki IoU ≥ 0,7 terhadap kotak kebenaran. Bila dua gundukan sekelas saling tumpang tindih, diambil nilai maksimum per posisi. Piksel di sekitar pusat dengan demikian menjadi positif yang dilemahkan, bukan negatif penuh.

### Fungsi Loss Heatmap

Heatmap dilatih dengan *penalty-reduced focal loss* dari CornerNet: regresi logistik per piksel dengan pembobotan *focal* (α = 2, β = 4). Piksel dengan target 1 dihukum sebagai positif; piksel lain dihukum sebagai negatif, tetapi penaltinya diperkecil dengan faktor (1−Y)^β bila target Gaussian-nya tinggi — jaringan tidak dihukum berat karena memberi skor sedang di dalam radius toleransi pusat. Loss dinormalisasi dengan N, jumlah objek dalam citra.

### Regresi Ukuran dan Offset

Pemetaan ⌊p/R⌋ membuang sisa pembagian, sehingga pusat hasil dekode dapat meleset hingga 4 piksel pada skala citra asli. Untuk menutup galat diskritisasi ini, jaringan memprediksi *offset* lokal Ô (2 kanal, dibagi semua kelas) berisi selisih p/R − p̃, serta ukuran kotak Ŝ (2 kanal: lebar dan tinggi), keduanya pada lokasi pusat. Keduanya dilatih dengan loss L1 yang hanya aktif pada lokasi pusat; posisi lain diabaikan. Ukuran diprediksi dalam piksel mentah tanpa normalisasi skala, sehingga bobot loss-nya diperkecil: λ_size = 0,1 dan λ_off = 1. Loss total deteksi adalah L_det = L_k + 0,1·L_size + L_off.

### Backbone dan Kepala Prediksi

Karena heatmap menuntut resolusi keluaran tinggi, CenterNet memakai *backbone* (jaringan pengekstrak fitur) yang dirancang untuk estimasi keypoint, dalam empat varian. Hourglass-104 terdiri atas dua modul *hourglass* bertingkat dengan koneksi *skip*, sama seperti pada CornerNet. ResNet-18 dan ResNet-101 ditambah tiga lapis *up-convolution* (konvolusi transpos untuk menaikkan resolusi; kanal 256, 128, 64), dengan satu konvolusi *deformable* 3×3 — konvolusi yang posisi cupliknya digeser oleh offset terpelajar — sebelum setiap *upsampling*. DLA-34 (*Deep Layer Aggregation*), jaringan dengan koneksi hierarkis antar-lapis, dimodifikasi serupa untuk prediksi padat. Setiap modalitas keluaran dihasilkan kepala terpisah: konvolusi 3×3, ReLU, lalu konvolusi 1×1; total C+4 kanal per posisi.

### Inferensi Tanpa NMS

Saat inferensi, puncak diekstrak per kelas: semua posisi bernilai lebih besar atau sama dengan kedelapan tetangganya dipertahankan, lalu diambil 100 teratas. Operasi ini terimplementasi efisien sebagai *max pooling* 3×3 — posisi yang nilainya tidak berubah setelah pooling adalah puncak lokal. Setiap puncak (x̂, ŷ) dengan nilai heatmap s langsung menjadi satu deteksi: skornya s, pusatnya dikoreksi offset menjadi (x̂+δx̂, ŷ+δŷ), dan kotaknya dibangun dari ukuran yang diregresi, yaitu (x̂+δx̂−ŵ/2, ŷ+δŷ−ĥ/2, x̂+δx̂+ŵ/2, ŷ+δŷ+ĥ/2). Tidak ada perhitungan IoU antar-kandidat maupun penekanan duplikat.

Alur data lengkap dari citra ke deteksi:

```
citra 512x512
     │
     ▼
┌─────────────────────────────┐
│ backbone (DLA-34 / ResNet   │   output stride R = 4
│ + up-conv / Hourglass-104)  │
└─────────────────────────────┘
     │  peta fitur 128x128
     ▼
┌───────────┬───────────┬───────────┐
│ heatmap   │ offset    │ ukuran    │   setiap kepala:
│ C kanal   │ 2 kanal   │ 2 kanal   │   3x3 conv ->
│ (kelas)   │ (dx, dy)  │ (w, h)    │   ReLU -> 1x1 conv
└───────────┴───────────┴───────────┘
     │
     ▼
puncak lokal: max-pool 3x3 (nilai >= 8 tetangga),
ambil 100 puncak teratas
     │
     ▼
kotak = (x+dx-w/2, y+dy-h/2, x+dx+w/2, y+dy+h/2)
skor  = nilai heatmap pada puncak
```

Seluruh keluaran diperoleh dalam satu kali umpan-maju jaringan; satu-satunya tahap di luar jaringan adalah *max pooling* 3×3 untuk mengekstrak puncak.

### Perluasan ke 3D dan Pose

Untuk deteksi 3D monokular (dari satu citra kamera), tiga kepala ditambahkan: kedalaman absolut melalui transformasi sigmoid-balik d = 1/σ(d̂) − 1, karena kedalaman sukar diregresi langsung; dimensi 3D (tinggi, lebar, panjang) dalam meter; dan orientasi yang dikodekan sebagai 8 skalar dalam dua *bin* sudut mengikuti skema Mousavian et al. Untuk pose multi-orang, posisi 17 sendi manusia diregresi sebagai offset dari pusat orang (34 kanal), lalu ditempelkan ke deteksi sendi terdekat pada *heatmap* sendi terpisah yang dilatih seperti heatmap pusat. Kedua perluasan tidak mengubah kerangka deteksi pusat; yang bertambah hanya kanal keluaran.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada MS COCO (118 ribu citra latih, 5 ribu validasi, 20 ribu test-dev) dengan metrik AP COCO, yaitu rata-rata presisi pada ambang IoU 0,5 sampai 0,95; semakin tinggi semakin baik, maksimal 100%. Kecepatan diukur pada mesin yang sama untuk semua pembanding yang tersedia kodenya (GPU Titan Xp).

Hasil utama pada validasi COCO, beserta interpretasinya:

- ResNet-18: 28,1% AP pada 142 FPS — model tercepat, dengan akurasi yang masih layak untuk aplikasi waktu-nyata berdaya rendah.
- DLA-34: 37,4% AP pada 52 FPS — lebih dari dua kali lebih cepat daripada YOLOv3 (33,0% AP, 20 FPS) sekaligus 4,4 poin AP lebih akurat.
- Hourglass-104: 40,3% AP pada 14 FPS, naik menjadi 42,2% dengan uji *flip* (rata-rata keluaran citra asli dan bayangan cerminnya), dan 45,1% dengan pengujian multi-skala pada 1,4 FPS. Angka terakhir ini melampaui semua detektor satu tahap pada test-dev, termasuk CornerNet (42,1% pada 4,1 FPS) dan ExtremeNet (43,7% pada 3,1 FPS) yang memakai backbone yang sama tetapi jauh lebih lambat karena tahap pengelompokannya.
- ResNet-101: 34,8% AP pada 45 FPS, dibandingkan RetinaNet ber-backbone setara (34,4% AP, 18 FPS) — akurasi setara dengan kecepatan lebih dari dua kali lipat.

Dua analisis tambahan memperkuat klaim desainnya. Pertama, risiko tabrakan pusat — dua objek berbeda yang pusatnya jatuh pada piksel heatmap yang sama — ternyata kecil: pada data latih COCO hanya ada 614 pasang objek yang bertabrakan dari total 860.001 objek (kurang dari 0,1%), lebih rendah daripada objek yang terlewat oleh proposal wilayah (~2%) maupun oleh penempatan anchor (20% pada Faster R-CNN). Kedua, menambahkan NMS pada keluaran CenterNet hampir tidak berpengaruh: AP DLA-34 naik dari 39,2% menjadi 39,7%, dan Hourglass-104 tetap 42,2%. Hasil ini membenarkan bahwa pencarian puncak memang pengganti NMS yang memadai.

Pada tolok ukur KITTI (deteksi 3D kendaraan dari satu citra), CenterNet setara dengan Deep3DBox dan Mono3D pada metrik AP dan AOS (*average orientation similarity*), sedikit lebih baik pada AP tampak atas (*bird's-eye-view*), dengan kecepatan sekitar dua orde lebih tinggi. Pada estimasi pose manusia COCO, varian DLA-34 mencapai 58,9% AP keypoint pada 23 FPS dan Hourglass-104 mencapai 64,0% pada 6,6 FPS. Regresi offset sendi murni masih lemah pada ambang kesamaan yang ketat, tetapi penyempurnaan dengan heatmap sendi membuatnya kompetitif terhadap metode multi-tahap.

## Kelebihan dan Keterbatasan

Kelebihan: (1) *pipeline* paling sederhana di antara detektor sezamannya — satu umpan-maju tanpa anchor, tanpa ambang IoU untuk penetapan label, dan tanpa NMS; (2) sepenuhnya *end-to-end differentiable*; (3) satu kerangka berlaku untuk deteksi 2D, 3D monokular, dan pose, cukup dengan menambah kepala keluaran; (4) trade-off kecepatan-akurasi terbaik di kelasnya pada 2019.

Keterbatasan: (1) dua objek yang pusatnya berimpit hanya akan terdeteksi satu; walau analisis tabrakan pada bagian sebelumnya menunjukkan kasusnya jarang pada COCO, secara konseptual batas ini tetap ada, misalnya pada objek yang sejajar garis pandang kamera; (2) kualitas heatmap menuntut backbone resolusi tinggi, sehingga varian paling akurat bergantung pada Hourglass-104 yang berat (1,4 FPS pada pengujian multi-skala), dan ablasi penulis menunjukkan penurunan resolusi uji ke 384×384 memangkas 3 poin AP; (3) akurasi pada objek kecil (AP_S 24,1% untuk varian terbaik) masih di bawah detektor dua tahap terkuat pada masa itu; (4) dari sisi rekayasa, ketergantungan pada konvolusi deformable pada varian ResNet dan DLA menambah kerumitan implementasi pada perangkat yang tidak menyediakan operasi tersebut.

## Kaitan dengan Bab Lain

CenterNet melanjutkan garis penyederhanaan pipeline yang dimulai [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md): bila YOLOv1 menghapus tahap proposal wilayah, CenterNet menghapus anchor dan NMS sekaligus. Pembanding langsungnya adalah [bab 003 (YOLOv3)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), detektor berbasis anchor yang pada tolok ukur yang sama dikalahkan CenterNet dalam kecepatan maupun akurasi, serta [bab 016 (RetinaNet)](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md) yang *focal loss*-nya diwarisi CenterNet untuk melatih heatmap. Arah "satu titik per objek, tanpa anchor" kemudian diadopsi keluarga YOLO sendiri: [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) melepaskan anchor dan memprediksi dari satu lokasi, dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md) meniadakan NMS melalui penetapan label ganda — dua sasaran yang lebih dulu dibuktikan layak oleh CenterNet. Representasi titik pusatnya juga menjadi fondasi keluarga metode lanjutan seperti CenterTrack (pelacakan) dan CenterPoint (deteksi 3D LiDAR).

## Poin untuk Sitasi

Kutip dengan kunci `zhou2019objects`. Ringkasan yang aman dikutip: "CenterNet merepresentasikan objek sebagai titik pusat kotaknya; deteksi menjadi estimasi keypoint pada heatmap dengan output stride 4, sedangkan ukuran dan offset kotak diregresi dari fitur pusat, tanpa anchor maupun NMS. Pada MS COCO, model DLA-34 mencapai 37,4% AP pada 52 FPS dan model Hourglass-104 mencapai 45,1% AP dengan pengujian multi-skala."

Catatan verifikasi: angka 28,1%/142 FPS, 37,4%/52 FPS, dan 45,1%/1,4 FPS berasal dari abstrak naskah. Angka 42,2% (uji flip Hourglass-104) dan perbandingan 34,8% lawan 34,4% terhadap RetinaNet diambil dari teks naskah; repositori resmi mencatat 34,6% untuk varian ResNet-101, sehingga angka ini perlu dicocokkan dengan tabel naskah sebelum dikutip. Angka pose (58,9% dan 64,0% AP keypoint) diambil dari tabel hasil repositori resmi untuk set validasi; hasil KITTI dikutip secara kualitatif dari naskah.
