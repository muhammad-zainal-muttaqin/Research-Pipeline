# 007 - YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023yolov7` |
| Judul asli | YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors |
| Penulis | Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao |
| Tahun | 2023 (pracetak arXiv Juli 2022) |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2207.02696
- **DOI (arXiv):** https://doi.org/10.48550/arXiv.2207.02696
- **Repositori kode resmi:** https://github.com/WongKinYiu/yolov7
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan YOLOv7, detektor objek satu tahap *real-time* yang dilatih dari awal hanya pada dataset MS COCO, tanpa bobot pralatih maupun data tambahan. Gagasan sentralnya adalah *trainable bag-of-freebies*: teknik yang menambah biaya pelatihan demi akurasi, tanpa menambah biaya inferensi (biaya menjalankan model jadi). Tiga komponen utamanya adalah blok agregasi fitur E-ELAN, konvolusi reparameterisasi terencana, dan penetapan label *coarse-to-fine* yang memakai kepala bantu.

Hasil utamanya: pada rentang 5 hingga 160 *frame* per detik (FPS) di GPU V100, YOLOv7 melampaui detektor *real-time* lain pada masanya dalam kombinasi kecepatan dan akurasi. Varian terbesarnya, YOLOv7-E6E, mencapai 56,8% AP (metrik akurasi utama COCO) pada 36 FPS — tertinggi di antara detektor *real-time* berkecepatan minimal 30 FPS saat terbit.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Silsilah YOLO merupakan upaya menaikkan akurasi tanpa mengorbankan kecepatan. YOLOv4 (bab 004) memperkenalkan konsep *bag-of-freebies* — teknik pelatihan yang menaikkan akurasi tanpa menambah biaya inferensi. YOLOX (bab 005) memopulerkan penetapan label dinamis: target pelatihan dihitung dari kualitas prediksi jaringan, bukan ditetapkan kaku dari kebenaran dasar (*ground truth*). YOLOv6 (bab 006) memakai reparameterisasi struktural gaya RepVGG: modul bercabang banyak saat pelatihan dilebur menjadi satu lapis konvolusi saat inferensi.

Penulis menemukan dua masalah baru. Pertama, RepConv — gabungan konvolusi 3×3, konvolusi 1×1, dan koneksi identitas (penjumlahan langsung masukan ke keluaran) — bekerja baik pada arsitektur polos, tetapi akurasinya turun saat diterapkan langsung pada arsitektur berkoneksi residual (blok yang menjumlahkan masukan ke keluarannya, seperti ResNet) atau berbasis konkatenasi (penggabungan peta fitur sepanjang dimensi kanal, seperti DenseNet); belum ada aturan kapan kombinasi itu aman. Kedua, bila detektor dilatih dengan lebih dari satu kepala keluaran melalui *deep supervision* (penambahan kepala bantu di lapisan tengah), muncul pertanyaan: kepala mana yang menetapkan target untuk kepala yang lain. Selain itu, penskalaan model lazimnya menganalisis tiap faktor secara terpisah, padahal pada model konkatenasi keduanya saling terkait.

## Ide Utama

Pisahkan tegas biaya pelatihan dari biaya inferensi. Selama pelatihan, jaringan boleh dibebani struktur tambahan — cabang konvolusi ekstra, kepala keluaran bantu, mekanisme penetapan label berlapis — asalkan semuanya dapat dilebur ke lapis lain atau dibuang saat inferensi.

Jalur datanya sendiri tidak berubah dari keluarga YOLO: citra mengalir melalui *backbone* (bagian awal jaringan yang mengekstraksi fitur) dan leher (*neck*, modul penggabung fitur multi-skala) berbasis blok E-ELAN, lalu ke kepala deteksi. Yang diubah makalah ini adalah cara blok dilatih, cara target pelatihan dibuat, dan cara model diskalakan.

## Cara Kerja Langkah demi Langkah

### Blok E-ELAN

Dasar arsitektur YOLOv7 adalah ELAN (*Efficient Layer Aggregation Network*), strategi desain dari grup penulis yang sama: jaringan dalam dapat belajar efektif bila jalur gradien terpendek dan terpanjangnya dikendalikan. Jalur gradien (*gradient path*) adalah rute sinyal gradien saat pembaruan bobot; jalur yang terlalu panjang menyulitkan konvergensi.

E-ELAN memperluas ELAN tanpa mengubah jalur gradiennya melalui tiga operasi: *expand*, *shuffle*, dan *merge cardinality* (*cardinality* = jumlah cabang paralel dalam satu blok). Setiap blok hitung diperluas memakai konvolusi grup (*group convolution* — konvolusi yang membagi kanal menjadi beberapa grup yang diproses terpisah). Peta fitur keluaran tiap blok dibagi menjadi g grup, dipertukarkan antarblok, lalu dikonkatenasi; terakhir, g grup dijumlahkan elemen demi elemen. Hanya bagian dalam blok hitung yang berubah, sedangkan lapisan transisi dipertahankan, sehingga kemampuan belajar naik tanpa merusak stabilitas gradien ELAN.

Alur data dalam satu lapisan E-ELAN:

```
masukan
   │
   ▼
┌──────────────────────────────────────┐
│ n blok hitung paralel; jalur gradien │   tiap blok: konvolusi grup,
│ ELAN dipertahankan utuh              │   kanal diperluas × pengali
└───┬────────┬────────┬────────┬───────┘
    ▼        ▼        ▼        ▼
  [FM1]    [FM2]    [FM3]    [FM4]   peta fitur tiap cabang
    │        │        │        │
    └────────┴───┬────┴────────┘
                 ▼
     shuffle: tiap peta dibagi g grup,
     grup dipertukarkan antarcabang,
     lalu dikonkatenasi
                 │
                 ▼
     merge cardinality:
     g grup dijumlahkan elemen demi elemen
                 │
                 ▼
             keluaran
```

### Penskalaan Gabungan untuk Model Berbasis Konkatenasi

*Model scaling* menghasilkan varian model berbeda ukuran dari satu desain dasar dengan mengubah kedalaman (jumlah lapis) atau lebar (jumlah kanal). Pada arsitektur biasa, tiap faktor dapat dianalisis terpisah karena memperdalam jaringan tidak mengubah lebar lapis lain. Pada model berbasis konkatenasi hal itu tidak berlaku: menaikkan kedalaman sebuah blok menambah jumlah peta fitur yang dikonkatenasi, sehingga lebar keluaran blok dan lebar masukan lapisan transisi berikutnya ikut berubah.

Solusinya, penskalaan gabungan (*compound scaling*): saat faktor kedalaman blok hitung dinaikkan, perubahan lebar keluarannya dihitung, lalu faktor lebar lapisan transisi dinaikkan dengan besar yang setara, sehingga rasio kanal optimal model dasar terjaga. Pada studi ablasi (uji yang mematikan komponen satu per satu untuk mengukur sumbangannya) dipakai kedalaman ×1,5 dan lebar transisi ×1,25. Cara ini menghasilkan varian YOLOv7-X, E6, dan D6.

### Reparameterisasi Terencana

Reparameterisasi struktural melatih modul bercabang banyak, lalu menggabungkannya menjadi satu lapis yang ekuivalen secara matematis saat inferensi. Penulis menemukan cabang koneksi identitas di dalam RepConv sumber masalahnya: ia tumpang tindih dengan koneksi residual ResNet dan mengganggu pola konkatenasi DenseNet, sehingga mengurangi keberagaman gradien antarpeta fitur dan menurunkan akurasi. Aturan yang diusulkan — reparameterisasi terencana (*planned re-parameterization*) — berbunyi sederhana: bila lapis konvolusi berada pada koneksi residual atau konkatenasi, pakai RepConvN (RepConv tanpa cabang identitas); RepConv penuh hanya untuk arsitektur polos.

Struktur RepConvN saat pelatihan dan hasil peleburannya saat inferensi:

```
saat pelatihan (dua cabang)          saat inferensi (dilebur)

        masukan                             masukan
      ┌────┴─────┐                              │
      ▼          ▼                              ▼
 ┌─────────┐ ┌─────────┐                 ┌─────────────┐
 │ conv 3x3│ │ conv 1x1│                 │ satu conv   │
 │  + BN   │ │  + BN   │                 │ 3x3 + bias  │
 └────┬────┘ └────┬────┘                 └──────┬──────┘
      └─────┬─────┘                             │
            ▼                                   ▼
      dijumlahkan                           keluaran
            │
            ▼
        keluaran

cabang identitas sengaja dibuang (RepConvN) pada lapis
yang memiliki koneksi residual atau konkatenasi
```

### Penetapan Label Coarse-to-Fine dengan Kepala Bantu

Makalah ini menamai kepala penghasil keluaran akhir sebagai *lead head* dan kepala bantu *deep supervision* sebagai *auxiliary head*; kepala bantu dibuang setelah pelatihan. Masalahnya ada pada penetapan target. Detektor modern memakai *label assigner*: mekanisme yang menghitung label lunak (*soft label*) dari gabungan prediksi jaringan dan *ground truth* — misalnya target skor keberadaan objek diset sebesar IoU (rasio luas irisan terhadap gabungan dua kotak) antara kotak prediksi dan kotak benar. Dengan dua kepala, praktik lazim saat itu adalah tiap kepala menghitung labelnya sendiri secara independen.

Strategi pertama, *lead head guided label assigner*: label lunak dihitung dari prediksi *lead head* dan *ground truth*, lalu dipakai melatih kedua kepala sekaligus. Alasannya, *lead head* lebih dalam sehingga prediksinya lebih mewakili data; kepala bantu yang dangkal mempelajari informasi yang sudah dikuasai *lead head*, sedangkan *lead head* memusatkan diri pada informasi sisa.

Strategi kedua, yang dipakai pada model final, adalah *coarse-to-fine lead head guided label assigner*. Label halus (*fine*) untuk *lead head* dibuat seperti strategi pertama; label kasar (*coarse*) untuk *auxiliary head* dibuat dengan melonggarkan syarat penetapan sampel positif, sehingga lebih banyak sel grid (sel pada peta fitur keluaran) dianggap positif dan *recall* (proporsi objek yang ditemukan) kepala bantu naik. Agar label kasar tidak merusak prior prediksi akhir, keluaran kepala bantu diberi batas atas: grid positif kasar tambahan tidak dapat menghasilkan label lunak sempurna karena skornya dibatasi menurut jarak ke pusat objek. Dengan begitu, batas optimasi label halus selalu lebih tinggi daripada label kasar.

### Bag-of-Freebies Lainnya

Tiga teknik tambahan melengkapi paket tanpa biaya inferensi. Pertama, fusi *batch normalization* (BN — normalisasi statistik tiap kanal terhadap rata-rata dan varians mini-batch): saat inferensi, parameter BN dilebur ke bobot dan bias lapis konvolusi yang bersebelahan. Kedua, pengetahuan implisit dari YOLOR: vektor yang saat pelatihan digabungkan dengan peta fitur konvolusi; saat inferensi vektor ini diprahitung dan dilebur ke bias atau bobot konvolusi di dekatnya. Ketiga, model *EMA* (*exponential moving average*): bobot inferensi diambil dari rata-rata bergerak eksponensial bobot selama pelatihan.

## Eksperimen dan Hasil

Seluruh eksperimen memakai MS COCO: *train2017* untuk pelatihan, *val2017* untuk verifikasi, dan *test-dev* (split uji resmi) untuk perbandingan akhir. AP dilaporkan menurut protokol COCO: rata-rata presisi pada ambang IoU 0,50–0,95. Tiga model dasar dirancang untuk tiga kelas perangkat: YOLOv7-tiny untuk GPU tepi (fungsi aktivasi *leaky ReLU*), YOLOv7 untuk GPU umum (aktivasi *SiLU*), dan YOLOv7-W6 untuk GPU *cloud*; varian lain diperoleh lewat penskalaan. Hasil utama pada resolusi 640:

- YOLOv7: 36,9 juta parameter, 104,7 GFLOPs (miliar operasi floating-point per citra, ukuran biaya komputasi), 161 FPS, 51,4% AP *test-dev*. Dibandingkan YOLOR-CSP (52,9 juta parameter, 120,4 GFLOPs, 106 FPS, 51,1% AP), model ini memangkas 43% parameter dan 15% komputasi sekaligus 55 FPS lebih cepat dengan AP sedikit lebih tinggi — paket *bag-of-freebies* hadir bersama arsitektur yang lebih hemat.
- YOLOv7-tiny-SiLU: 6,2 juta parameter, 286 FPS, 38,7% AP — 127 FPS lebih cepat dan 10,7 poin AP lebih tinggi daripada YOLOv5-N r6.1 (159 FPS, 28,0% AP *val*). Selisih ini menunjukkan perbaikan arsitektur paling terasa pada model kecil dengan anggaran komputasi sempit.
- YOLOv7-X: 53,1% AP pada 114 FPS; dibandingkan YOLOv5-X r6.1 (50,7% AP *val*, 83 FPS), ia 31 FPS lebih cepat dengan 22% parameter dan 8% komputasi lebih sedikit.

Pada resolusi 1280, YOLOv7-E6 mencapai 55,9% AP *val* pada 56 FPS; detektor transformer (detektor berbasis arsitektur atensi) SWIN-L Cascade Mask R-CNN mencapai 53,9% AP pada 9,2 FPS (GPU A100), sehingga YOLOv7-E6 unggul 2 poin AP sekaligus sekitar enam kali lebih cepat. YOLOv7-E6E mencapai 56,8% AP pada 36 FPS; dibandingkan YOLOR-D6 (56,5% AP *test*, 34 FPS) yang berparameter sama (151,7 juta), E6E memakai komputasi lebih rendah (843,2 lawan 935,6 GFLOPs) dengan AP 0,3 poin lebih tinggi — keuntungan datang dari desain, bukan penambahan ukuran.

Studi ablasi mengonfirmasi tiap komponen. Penskalaan gabungan memberi AP 0,5 poin lebih tinggi daripada penskalaan lebar saja, dengan parameter dan komputasi lebih kecil. Reparameterisasi terencana menghasilkan AP tertinggi pada model konkatenasi (3-stacked ELAN) maupun residual (CSPDarknet, *backbone* keluarga Darknet) dibanding RepConv biasa. Penambahan *loss* (fungsi galat yang diminimalkan saat pelatihan) bantu selalu menaikkan AP, dan strategi *coarse-to-fine* mengungguli penetapan independen maupun *lead-guided* biasa. Ketiga uji ini menunjukkan tiap klaim kontribusi berdiri sendiri.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini adalah efisiensi bukti: akurasi naik nyaris tanpa biaya inferensi karena seluruh struktur tambahan dilebur atau dibuang, cakupan variannya luas (5–160 FPS), dan pelatihan serta kode resminya terbuka untuk direproduksi dari awal tanpa data eksternal.

Keterbatasan berikut merupakan analisis penulis bab, bukan pernyataan penulis makalah. Dari sisi rekayasa, resep pelatihannya lebih kompleks daripada pendahulunya: dua kepala, dua set label, dan modul yang harus dilebur ulang lewat prosedur reparameterisasi terpisah sebelum dipakai. Dari sisi rekayasa pula, perbandingan kecepatan kelas berat dilakukan lintas GPU (V100 untuk YOLOv7, A100 untuk pembanding transformer), sehingga selisihnya tidak sepenuhnya setara. Secara konseptual, model utama tetap memakai kepala deteksi berbasis *anchor* (kotak acuan berukuran tetap yang menjadi titik tolak regresi posisi objek) dan masih memerlukan *Non-Maximum Suppression* (NMS — pembuangan kotak ganda yang tumpang tindih); varian *anchor-free* (u6) disediakan repositori, tetapi di luar hasil utama makalah.

## Kaitan dengan Bab Lain

Bab ini melanjutkan langsung resep [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md): konsep *bag-of-freebies* diperluas dari kumpulan trik pelatihan menjadi paket terstruktur yang mencakup arsitektur, reparameterisasi, dan penetapan label. Terhadap [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) dan [bab 006 (YOLOv6)](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md), YOLOv7 berperan sebagai koreksi sekaligus kelanjutan: penetapan label dinamis dan reparameterisasi struktural yang dipopulerkan kedua bab itu dianalisis ulang lalu diberi aturan pakai yang aman. Sebaliknya, [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md) menjadikan hasil bab ini garis dasar perbandingan utama pada kelas detektor *real-time*. Fondasi satu tahapnya mewarisi [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md): regresi langsung dari citra ke kotak objek dalam satu evaluasi.

## Poin untuk Sitasi

Kutip dengan kunci `wang2023yolov7`. Ringkasan yang aman dikutip: "YOLOv7 memperkenalkan *trainable bag-of-freebies* — paket teknik pelatihan yang menaikkan akurasi tanpa menambah biaya inferensi — melalui blok E-ELAN, reparameterisasi terencana, dan penetapan label *coarse-to-fine*; varian E6E-nya mencapai 56,8% AP COCO pada 36 FPS (GPU V100), akurasi tertinggi di antara detektor *real-time* minimal 30 FPS saat terbit, dan seluruh model dilatih dari awal hanya pada MS COCO."

Catatan verifikasi: tabel ablasi lengkap (Tabel 3–8 naskah) tidak terrender pada sumber HTML; angka ablasi di sini (kedalaman ×1,5, lebar ×1,25, +0,5 poin AP) berasal dari teks naskah — cocokkan ke tabel PDF sebelum sitasi formal. Klaim kecepatan kelas berat diukur lintas GPU (V100 lawan A100); kutip beserta konteksnya. Pernyataan bahwa model utama berbasis *anchor* dan memerlukan NMS diverifikasi dari repositori kode resmi, bukan dari naskah.
