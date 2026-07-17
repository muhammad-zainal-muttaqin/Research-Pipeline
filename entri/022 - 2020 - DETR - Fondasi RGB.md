# 022 - End-to-End Object Detection with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `carion2020detr` |
| Judul asli | End-to-End Object Detection with Transformers |
| Penulis | Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2005.12872
- **DOI:** https://doi.org/10.48550/arXiv.2005.12872
- **Repositori kode resmi:** https://github.com/facebookresearch/detr
- **Google Scholar:** https://scholar.google.com/scholar?q=End-to-End%20Object%20Detection%20with%20Transformers
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=End-to-End%20Object%20Detection%20with%20Transformers&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DETR (*DEtection TRansformer*), detektor objek yang merumuskan deteksi sebagai masalah prediksi himpunan langsung (*direct set prediction*): model menerima satu citra dan langsung mengeluarkan satu himpunan berukuran tetap berisi prediksi (kelas, kotak pembatas), tanpa komponen rancangan tangan seperti *anchor box* (kotak acuan berukuran dan berasio tetap yang menjadi titik tolak regresi pada detektor konvensional) maupun *Non-Maximum Suppression* (NMS, pasca-pemrosesan yang membuang kotak duplikat yang saling tumpang tindih). Dua komponen kuncinya adalah *loss* himpunan berbasis pencocokan bipartit (*bipartite matching*) yang memaksakan pemasangan satu-satu antara prediksi dan objek sebenarnya, serta arsitektur *transformer* encoder-decoder yang menalar relasi antar-objek dan konteks global citra.

Hasil utamanya: DETR dengan *backbone* ResNet-50 mencapai 42,0 AP pada COCO 2017 — setara dengan baseline Faster R-CNN yang telah dioptimalkan bertahun-tahun, dengan jumlah parameter sama dan sekitar separuh beban komputasi. DETR unggul pada objek besar tetapi tertinggal pada objek kecil. Makalah ini membuka garis detektor berbasis *transformer*, dari Deformable DETR (bab 023) hingga deteksi bebas-NMS pada YOLOv10 (bab 009).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Detektor modern sebelum 2020, baik satu tahap (YOLO, SSD, RetinaNet) maupun dua tahap (Faster R-CNN, bab 014), memprediksi objek secara tidak langsung: jaringan mengeluarkan skor dan regresi relatif terhadap kandidat awal — *anchor box*, *region proposal*, atau titik pusat pada kisi — dalam jumlah sangat besar. Karena satu objek dicakup banyak kandidat, keluaran mentah selalu mengandung duplikat, sehingga seluruh detektor ini bergantung pada NMS untuk merampingkan hasil akhir.

Ketergantungan ini menimbulkan tiga masalah. Pertama, kinerja akhir sangat dipengaruhi keputusan rancangan manual: jumlah, ukuran, dan rasio *anchor*; aturan penetapan label yang memasangkan kandidat dengan objek sebenarnya; serta ambang NMS. Kedua, NMS adalah prosedur heuristik di luar jaringan, sehingga sistem tidak dilatih *end-to-end* terhadap tujuan akhir deteksi; pada adegan padat, NMS dapat membuang deteksi yang benar. Ketiga, upaya prediksi himpunan langsung sebelumnya, umumnya berbasis jaringan berulang (RNN) yang memprediksi objek satu per satu, tidak mampu bersaing dengan baseline kuat pada tolok ukur besar seperti COCO. Masalah yang diangkat makalah ini adalah merumuskan deteksi sebagai prediksi himpunan yang benar-benar langsung — tanpa *anchor*, tanpa NMS — sambil tetap kompetitif melawan Faster R-CNN yang sudah matang.

## Ide Utama

Gagasan inti DETR adalah memperlakukan deteksi sebagai penerjemahan dari citra ke himpunan berukuran tetap. Model dilatih untuk selalu mengeluarkan tepat N = 100 prediksi — jauh lebih banyak dari jumlah objek pada citra umum (rata-rata 7 objek per citra di COCO) — dan setiap prediksi berupa satu kotak beserta kelasnya, atau kelas khusus ∅ ("bukan objek") untuk slot yang tidak terpakai.

Dua mekanisme membuat rumusan ini dapat bekerja. Pertama, fungsi *loss* pencocokan bipartit: pada setiap langkah pelatihan, algoritme Hungarian mencari pemasangan satu-satu terbaik antara 100 prediksi dan objek *ground truth* (kebenaran acuan); hanya prediksi yang terpasang dihukum atas galat kotak dan kelasnya, sedangkan sisanya dilatih memprediksi ∅. Karena setiap objek hanya boleh dipasangkan ke tepat satu prediksi, model dipaksa tidak menghasilkan duplikat — peran yang selama ini diemban NMS dipindahkan ke dalam *loss* itu sendiri. Kedua, arsitektur *transformer*: mekanisme *self-attention* membuat setiap elemen komputasi menimbang relasinya terhadap seluruh elemen lain, sehingga model dapat menalar konteks global citra dan interaksi antar-prediksi secara eksplisit.

## Cara Kerja Langkah demi Langkah

Aliran data DETR dari citra hingga himpunan prediksi:

```
citra masukan (3 x H0 x W0)
        |
        v
+-------------------+   peta fitur C = 2048 kanal,
| backbone ResNet-50|   resolusi H0/32 x W0/32
+-------------------+
        | konvolusi 1x1 mereduksi kanal: 2048 -> d = 256
        v
sekuen H*W token + positional encoding (kode posisi sinusoidal)
        |
        v
+--------------------------+   6 lapis; self-attention global
| encoder transformer (6x) |   antar seluruh token citra
+--------------------------+
        |
        v
+--------------------------+   100 object query (vektor yang
| decoder transformer (6x) | <== dipelajari); self-attention antar-
+--------------------------+     query + cross-attention ke encoder
        | 100 embedding keluaran
        v
FFN bersama (perceptron 3 lapis, diterapkan per embedding)
        |
        v
100 prediksi: (kelas, cx, cy, w, h) atau "bukan objek" (∅)

pelatihan: Hungarian matching memasangkan tiap objek ground truth
ke tepat satu prediksi; prediksi tak terpasang dilatih memprediksi ∅
```

### Backbone dan Peta Fitur

*Backbone* adalah jaringan konvolusi pengekstrak fitur di awal detektor; di sini dipakai ResNet-50 atau ResNet-101 yang dilatih awal pada ImageNet (dataset klasifikasi skala besar). Citra masukan 3×H0×W0 dipetakan menjadi peta aktivasi berkanal C = 2048 dengan resolusi 1/32 dari masukan; pada citra 800×1333 piksel, petanya berukuran sekitar 25×42. Sebuah konvolusi 1×1 kemudian mereduksi 2048 kanal menjadi d = 256 kanal, dan dimensi spasialnya diratakan menjadi sekuen berisi H×W token (masing-masing vektor 256 dimensi) — dalam contoh di atas sekitar 1.050 token.

### Encoder Transformer

*Transformer* adalah arsitektur berbasis *attention* yang diperkenalkan untuk penerjemahan mesin: pada *self-attention*, setiap token memperbarui representasinya dengan mengagregasi informasi dari seluruh token lain dengan bobot yang dihitung dari kemiripannya. Karena operasi ini invariant terhadap urutan token, *positional encoding* sinusoidal (kode posisi yang diturunkan dari fungsi sinus) ditambahkan ke setiap lapis agar model mengetahui posisi spasial tiap token. Encoder DETR terdiri atas 6 lapis, masing-masing berisi *multi-head self-attention* (attention dengan 8 kepala paralel) dan jaringan *feed-forward* (FFN). Fungsi encoder adalah memperkaya fitur setiap lokasi dengan konteks seluruh citra; ablasi makalah menunjukkan penghapusan encoder menurunkan AP sebesar 3,9 poin, terutama pada objek besar (−6,0 AP_L), yang menegaskan perannya dalam memisahkan instans melalui penalaran global.

### Decoder dan Object Query

Decoder juga terdiri atas 6 lapis. Masukannya adalah 100 *object query*: vektor 256 dimensi yang dipelajari, berperan sebagai posisi awal yang berbeda-beda agar 100 slot keluaran tidak identik. Setiap lapis decoder menjalankan *self-attention* antar-query — di sinilah prediksi-prediksi saling "melihat" sehingga duplikasi dapat ditekan — diikuti *cross-attention* (encoder-decoder attention) yang membuat setiap query menimbang token-token citra dari encoder. Seluruh 100 objek didekode secara paralel dalam satu kali lintasan, bukan satu per satu. Analisis makalah menunjukkan setiap slot query belajar menspesialisasi wilayah dan ukuran kotak tertentu, tanpa spesialisasi kelas: model tetap mampu mendeteksi 24 jerapah meskipun data latih tidak memuat lebih dari 13 jerapah per citra.

### Kepala Prediksi

Setiap embedding keluaran decoder dilewatkan ke FFN bersama yang sama: perceptron 3 lapis dengan aktivasi ReLU yang memprediksi empat angka kotak — pusat (cx, cy) serta lebar dan tinggi yang dinormalisasi terhadap ukuran citra — dan satu lapis linier dengan *softmax* yang memprediksi kelas, termasuk kelas ∅. Karena kotak diprediksi absolut (bukan selisih terhadap *anchor*), dipakai *box loss* gabungan: *loss* L1 pada koordinat ditambah *loss* GIoU (*generalized Intersection over Union*, perluasan IoU — rasio luas irisan terhadap luas gabungan dua kotak — yang invariant terhadap skala). Ablasi menunjukkan GIoU menanggung sebagian besar kinerja: melatih tanpa *loss* L1 hanya mengurangi 0,7 AP, sedangkan L1 tanpa GIoU jauh lebih buruk.

### Pencocokan Bipartit dan Hungarian Loss

Biaya pemasangan sebuah objek *ground truth* dengan sebuah prediksi menggabungkan probabilitas kelas prediksi dan *box loss* di atas. Algoritme Hungarian mencari permutasi 100 prediksi dengan total biaya terendah, sehingga setiap objek memperoleh tepat satu prediksi pasangan. *Loss* akhir (disebut *Hungarian loss*) adalah *negative log-likelihood* kelas untuk semua slot ditambah *box loss* hanya untuk slot terpasang; suku kelas pada slot ∅ diturunkan bobotnya 10 kali untuk mengimbangi banyaknya slot kosong. Fungsi *loss* ini invariant terhadap permutasi prediksi, sesuai sifat himpunan. Selama pelatihan, *loss* auxiliary juga diterapkan setelah setiap lapis decoder; evaluasi per lapis menunjukkan AP naik total +8,2 poin dari lapis decoder pertama ke terakhir, dan menjalankan NMS pada keluaran lapis-lapis akhir justru sedikit menurunkan AP — bukti bahwa mekanisme bebas-duplikat sudah bekerja di dalam jaringan.

### Pelatihan

Model dilatih dengan pengoptimal AdamW (laju pembelajaran 10⁻⁴ untuk *transformer*, 10⁻⁵ untuk *backbone*), *dropout* (regularisasi pemadaman acak sebagian unit) 0,1, dan *batch* 64. Citra diskalakan sehingga sisi terpendek 480–800 piksel (terpanjang maksimal 1.333), ditambah pemotongan acak (*random crop*) yang menambah sekitar 1 AP. Jadwal panjang 500 *epoch* (penurunan laju pembelajaran setelah epoch 400) menambah 1,5 AP dibanding jadwal 300 *epoch*; pelatihan 300 *epoch* memerlukan 3 hari pada 16 GPU V100.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada COCO 2017 (118 ribu citra latih, 5 ribu citra validasi, 80 kelas), tolok ukur standar deteksi objek. Metriknya adalah AP (*Average Precision* terintegrasi atas beberapa ambang IoU), beserta AP_S/AP_M/AP_L untuk objek kecil/sedang/besar. Pembanding utamanya adalah Faster R-CNN ber-backbone sama yang diperkuat penulis dengan GIoU, *random crop*, dan jadwal pelatihan panjang.

Hasil kunci pada COCO val2017:

- DETR (ResNet-50): 42,0 AP, 28 *frame* per detik (FPS), 41,3 juta parameter (23,5 juta di ResNet-50, 17,8 juta di *transformer*) — menyamai Faster R-CNN yang diperkuat dengan jumlah parameter sama dan separuh FLOPs.
- Rincian ukuran: DETR menang +7,8 poin AP_L tetapi kalah −5,5 poin AP_S dari Faster R-CNN; interpretasinya, *self-attention* global menguntungkan objek besar, sementara resolusi fitur tunggal 1/32 merugikan objek kecil.
- Varian beresolusi lebih tinggi (DETR-DC5, tahap terakhir *backbone* didilatasi) mencapai 43,3 AP dengan biaya komputasi total sekitar dua kali lipat; varian ResNet-101 mencapai 43,5 AP, dan gabungan keduanya 44,9 AP.
- Generalisasi ke segmentasi panoptik (tugas pelabelan tiap piksel menjadi kelas benda dan latar secara serentak): kepala masker sederhana yang dilatih 25 *epoch* di atas DETR yang dibekukan mencapai 46 PQ (*Panoptic Quality*) pada *test set* COCO, mengungguli baseline UPSNet dan Panoptic FPN, terutama pada kelas latar (*stuff*).

## Kelebihan dan Keterbatasan

Kelebihan: (1) *pipeline* deteksi paling sederhana di masanya — tanpa *anchor*, tanpa NMS, tanpa lapis khusus; kode inferensi muat dalam kurang dari 50 baris PyTorch; (2) prediksi paralel satu kali lintasan dengan kecepatan setara Faster R-CNN; (3) penalaran global *self-attention* memberi keunggulan besar pada objek besar dan pada kelas latar segmentasi panoptik, sekaligus menunjukkan desain yang mudah diperluas ke tugas lain.

Keterbatasan: (1) konvergensi pelatihan sangat lambat — hingga 500 *epoch*, dan 300 *epoch* pun memerlukan 3 hari pada 16 V100; (2) kinerja objek kecil tertinggal (−5,5 AP_S) karena peta fitur tunggal beresolusi 1/32, persoalan yang pada Faster R-CNN diselesaikan FPN (bab 018, jaringan piramida fitur yang menggabungkan peta multi-skala); (3) dari sisi rekayasa, biaya *self-attention* encoder tumbuh kuadratik terhadap jumlah token — pada varian DC5 biaya *attention* naik 16 kali dan biaya total dua kali; (4) secara konseptual, himpunan tetap 100 slot menyisakan banyak slot kosong yang harus ditekan lewat pembobotan kelas ∅, beban yang tidak ada pada detektor berbasis kandidat.

## Kaitan dengan Bab Lain

DETR adalah titik balik dari paradigma prediksi padat berbasis kandidat yang dibentuk keluarga YOLO (bab 001, [001 - YOLOv1](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) dan Faster R-CNN (bab 014, [014 - Faster R-CNN](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)): kedua garis itu memerlukan NMS, sedangkan DETR menghapusnya lewat pencocokan satu-satu. Kelemahannya pada objek kecil dan konvergensi lambat langsung diserang oleh penerusnya, Deformable DETR (bab 023, [023 - Deformable DETR](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md)), yang mengganti *attention* global dengan *attention* terdeformasi multi-skala. Gagasan prediksi satu-satu bebas-NMS juga kembali muncul pada YOLOv10 (bab 009, [009 - YOLOv10](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)), yang mengadopsi penetapan satu-satu sehingga YOLO berjalan tanpa NMS.

## Poin untuk Sitasi

Kutip dengan kunci `carion2020detr`. Ringkasan yang aman dikutip: "DETR merumuskan deteksi objek sebagai prediksi himpunan langsung dengan arsitektur *transformer* encoder-decoder dan *loss* pencocokan bipartit Hungarian, menghapus kebutuhan *anchor* dan NMS; pada COCO 2017 model ini menyamai Faster R-CNN yang dioptimalkan (42,0 AP dengan ResNet-50), unggul pada objek besar tetapi tertinggal pada objek kecil." Seluruh angka di atas berasal dari naskah dan repositori resmi; rincian Tabel 1 makalah (AP50 dan AP_M absolut) serta nilai PQ validasi per varian sebaiknya diverifikasi ulang ke tabel naskah sebelum sitasi formal.
