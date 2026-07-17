# 024 - An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dosovitskiy2021vit` |
| Judul asli | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale |
| Penulis | Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby |
| Tahun | 2021 |
| Venue | International Conference on Learning Representations (ICLR 2021) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2010.11929
- **Kode resmi dan model terlatih:** https://github.com/google-research/vision_transformer
- **Google Scholar:** https://scholar.google.com/scholar?q=An%20Image%20Is%20Worth%2016x16%20Words%3A%20Transformers%20for%20Image%20Recognition%20at%20Scale
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=An%20Image%20Is%20Worth%2016x16%20Words%3A%20Transformers%20for%20Image%20Recognition%20at%20Scale&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Vision Transformer (ViT): model klasifikasi citra yang menerapkan arsitektur Transformer — sebelumnya baku pada pemrosesan bahasa — langsung pada citra, tanpa lapis konvolusi. Citra masukan dipotong menjadi petak-petak (*patch*) berukuran tetap, setiap petak diproyeksikan menjadi satu vektor, dan rangkaian vektor itu diolah oleh *encoder* Transformer sebagaimana rangkaian kata pada tugas bahasa. Kelas citra dibaca dari satu *token* khusus bernama [CLS].

Temuan utamanya bersyarat pada skala data. Dilatih hanya pada ImageNet (1,3 juta citra), ViT berada beberapa poin di bawah ResNet seukuran. Dilatih lebih dahulu pada ratusan juta citra, ViT menyamai atau melampaui jaringan konvolusi terbaik: 88,55% akurasi top-1 pada ImageNet dan 77,63% pada paket 19 tugas VTAB, dengan biaya pelatihan awal jauh lebih kecil dari pembandingnya — bukti bahwa pada skala data cukup, bias induktif konvolusi tidak lagi diperlukan untuk pengenalan citra.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak AlexNet (2012) dan ResNet (2016, bab 147), jaringan saraf konvolusi (CNN) menjadi pilihan baku pengenalan citra. CNN memuat dua bias induktif — asumsi struktural yang tertanam dalam arsitektur: lokalitas (piksel berdekatan diolah bersama oleh jendela kecil) dan ekuivariansi translasi (tapis yang sama dipakai di semua posisi, sehingga pola yang bergeser tetap dikenali). Keduanya sesuai dengan sifat citra dan lama dipandang sebagai prasyarat kinerja visi.

Sementara itu pada pemrosesan bahasa, Transformer (Vaswani dkk., 2017) menjadi dasar model seperti BERT, dengan pola tetap: latih awal pada korpus raksasa, setel halus per tugas. Upaya memindahkan *self-attention* ke citra sebelum ViT berjalan tiga jalur: *attention* sebagai pelengkap CNN; pola *attention* khusus (lokal, jarang, per sumbu) pengganti konvolusi yang sukar dieksekusi efisien pada akselerator modern; atau Transformer pada satuan sangat kecil — Cordonnier dkk. (2020) memakai petak 2×2 yang hanya mampu menangani citra resolusi rendah, dan iGPT menurunkan resolusi serta ruang warna dengan hasil maksimal 72% pada ImageNet. Pertanyaannya: dapatkah Transformer standar bekerja langsung pada citra dan bersaing dengan CNN terbaik?

## Ide Utama

Gagasan inti ViT: sebuah citra dapat diperlakukan sebagai kalimat. Kalimat adalah urutan *token* kata; citra diubah menjadi urutan *token* petak. Judul makalah merujuk pilihan petak 16×16 piksel: citra 224×224 terbagi menjadi 14×14 = 196 petak, sehingga satu citra "bernilai 196 kata". Setiap petak diratakan menjadi vektor nilai piksel lalu dipetakan oleh satu perkalian matriks ke dimensi kerja model, setara *embedding* kata pada BERT. Sesudah itu tidak ada lagi komponen khusus visi: *encoder* Transformer standar mengolah urutan tersebut, dan satu *token* kelas tambahan menampung ringkasan untuk pengklasifikasi.

Hipotesisnya sengaja ekstrem: hilangnya bias induktif konvolusi dapat ditutup oleh data — bila contoh latih cukup banyak, model mempelajari sendiri struktur spasial yang pada CNN ditanamkan sejak awal.

## Cara Kerja Langkah demi Langkah

### Tokenisasi: dari Citra ke Urutan Vektor

Citra H×W×C (tinggi, lebar, kanal warna) dipotong menjadi petak P×P tanpa tumpang tindih. Jumlah petak N = HW/P² sekaligus menjadi panjang urutan masukan. Pada konfigurasi utama, citra 224×224×3 dan P = 16 menghasilkan N = 196 petak; setiap petak diratakan menjadi vektor 16×16×3 = 768 nilai.

Petak dipakai karena biaya *self-attention* tumbuh kuadratik terhadap panjang urutan. Pada 196 token diperlukan matriks perhatian 196×196; perhatian per piksel berarti 50.176×50.176, lebih dari 2,5 miliar pasangan — tidak terjangkau. Petak 16×16 menjaga detail sekaligus membuat urutan tetap pendek; varian lain memakai P = 14 atau P = 32 — petak lebih kecil berarti urutan lebih panjang dan lebih mahal.

### Proyeksi Linear, Token [CLS], dan Embedding Posisi

Setiap vektor petak dikalikan matriks terlatih E berukuran 768×D (D = dimensi internal; 768 pada varian Base), menghasilkan *patch embedding*. Di depan urutan ditambahkan *token* khusus [CLS]: vektor terlatih tanpa isi petak yang menjadi titik baca keluaran. Karena *self-attention* tidak membedakan posisi, ke setiap vektor dijumlahkan *embedding posisi* 1D yang juga terlatih, sehingga token ke-i membawa informasi letaknya pada kisi 14×14; varian sadar-2D tidak memberi perbaikan berarti, sehingga versi 1D dipertahankan.

### Encoder Transformer

Urutan 197 vektor berdimensi D masuk ke *encoder* Transformer: tumpukan L lapis identik, masing-masing dua blok. Blok pertama, *multi-head self-attention*: setiap token diproyeksikan menjadi tiga vektor — *query*, *key*, *value*; skor kecocokan *query* satu token terhadap seluruh *key* dinormalisasi *softmax* menjadi bobot, dan keluarannya jumlah tertimbang seluruh *value*. Mekanisme ini berjalan paralel dalam beberapa *head* (12 pada varian Base) agar jenis relasi yang berbeda tertangkap bersamaan. Blok kedua, MLP dua lapis dengan aktivasi GELU yang memperluas dimensi empat kali lalu mengembalikannya. Kedua blok diawali normalisasi lapis (*LayerNorm*, penyetaraan skala fitur per token) dan ditutup sambungan residual (keluaran blok dijumlahkan dengan masukannya), susunan yang memudahkan pelatihan jaringan dalam.

Perbedaan mendasar dari CNN: konvolusi hanya melihat tetangga lokal dan memperluas jangkauan lapis demi lapis, sedangkan *self-attention* menghubungkan setiap pasang token sejak lapis pertama — jangkauan global tanpa bantuan struktur lokal apa pun.

### Varian Model dan Arsitektur Hibrida

Makalah mendefinisikan tiga ukuran mengikuti BERT: Base dan Large diadopsi langsung (Base: 12 lapis, D = 768, 12 *head*), ditambah varian Huge yang lebih besar. Nama model menggabungkan ukuran dan petak: ViT-L/16 berarti Large dengan petak 16×16. Varian hibrida mengambil urutan masukan dari peta fitur ResNet alih-alih piksel mentah, dengan petak 1×1 pada peta fitur itu.

### Pelatihan Awal dan Penyetelan Halus

Pelatihan awal (*pre-training*) melatih ViT sebagai pengklasifikasi pada dataset besar, dengan kepala MLP satu lapis tersembunyi, pengoptimal Adam, *batch* 4096, dan *weight decay* 0,1 pada resolusi 224. Penyetelan halus (*fine-tuning*) pada dataset target yang lebih kecil mengganti kepala dengan satu lapis linear D×K (K jumlah kelas baru) berinisialisasi nol, dilatih memakai SGD bermomentum pada *batch* 512.

Penyetelan halus dilakukan pada resolusi lebih tinggi (baku 384; untuk hasil ImageNet terbaik, 512–518). Ukuran petak dipertahankan, sehingga jumlah token bertambah: pada 384 piksel dan P = 16, urutan menjadi 24×24 = 576 petak plus [CLS]. Bobot *encoder* menerima panjang baru tanpa perubahan; *embedding posisi* yang terlatih untuk 196 posisi disesuaikan dengan interpolasi 2D. Penyesuaian ini dan pemotongan petak adalah satu-satunya titik masuknya struktur 2D secara manual ke dalam ViT.

Aliran data dari citra ke prediksi kelas:

```
citra 224x224x3
   │  potong petak 16x16: 14x14 = 196 petak
   │  ratakan tiap petak: 16x16x3 = 768 nilai
   ▼
proyeksi linear E (768 -> D)     + embedding posisi terlatih
   │                              (197 vektor, dijumlahkan per token)
   ▼
┌───────┬────────┬────────┬─────┬──────────┐
│ [CLS] │ petak1 │ petak2 │ ... │ petak196 │
└───────┴────────┴────────┴─────┴──────────┘
   ▼
┌────────────────────────────────────────────────┐
│ ENCODER TRANSFORMER (L lapis identik)          │
│   LayerNorm -> multi-head self-attention -> (+)│
│   LayerNorm -> MLP dua lapis (GELU) -> (+)     │
└────────────────────────────────────────────────┘
   ▼  hanya keluaran pada posisi [CLS] yang dibaca
LayerNorm -> kepala klasifikasi -> probabilitas kelas
```

## Eksperimen dan Hasil

Evaluasi memakai tiga dataset pelatihan awal berjenjang: ImageNet (1,3 juta citra, 1.000 kelas), ImageNet-21k (14 juta, 21.000 kelas), dan JFT-300M (303 juta, 18.000 kelas, internal Google). Model dipindahkan ke tolok ukur lebih kecil: ImageNet dengan label asli dan label bersih ReaL, CIFAR-10/100, Oxford-IIIT Pets, Oxford Flowers-102, serta VTAB — paket 19 tugas dengan hanya 1.000 contoh latih per tugas untuk mengukur transfer pada data sedikit. Metriknya akurasi top-1: prediksi paling diyakini model harus tepat.

Hasil utama, dengan dua pembanding CNN terkuat — BiT (Big Transfer, ResNet besar dengan protokol transfer sama) dan Noisy Student (EfficientNet-L2 semi-terawasi, hasil ImageNet terbaik sebelumnya dengan 88,5% pada laporan lanjutannya):

- ViT-H/14 (JFT-300M): 88,55% pada ImageNet, 90,72% pada ImageNet-ReaL, 94,55% pada CIFAR-100, 77,63% pada VTAB. Angka ini melampaui Noisy Student sekaligus yang terbaik untuk model tanpa konvolusi pada tolok ukur itu.
- ViT-L/16 (JFT-300M): mengungguli BiT-L yang dilatih pada data sama pada seluruh tugas, dengan sumber daya pelatihan jauh lebih kecil.
- ViT-L/16 (ImageNet-21k, publik): baik pada sebagian besar tugas; pelatihan awalnya cukup dengan TPUv3 8 inti selama kurang lebih 30 hari — anggaran terjangkau di luar laboratorium besar.

Eksperimen kebutuhan data: dilatih hanya pada ImageNet, varian Large justru kalah dari varian Base dan keduanya di bawah ResNet (BiT) seukuran — bias induktif konvolusi lebih menentukan pada data terbatas. Pada ImageNet-21k keduanya sejajar; baru pada JFT-300M model besar mengungguli yang kecil serta melampaui CNN. Pada subset acak JFT polanya serupa: pada 9 juta citra ViT-B/32 jauh di bawah ResNet50, pada 90 juta ke atas keadaannya berbalik.

Studi penskalaan (7 ResNet, 6 ViT, 5 hibrida, data sama) menunjukkan ViT mencapai kinerja setara ResNet dengan komputasi pelatihan awal 2–4 kali lebih hemat, rata-rata pada 5 dataset. Varian hibrida sedikit lebih baik pada anggaran kecil, tetapi selisihnya hilang pada model besar. Kinerja ViT juga belum jenuh pada rentang yang diuji, tanda penskalaan lebih lanjut masih menguntungkan.

Analisis internal menunjukkan kemiripan *embedding posisi* terbentuk mengikuti jarak dan struktur baris-kolom kisi 2D; sebagian *head* memperhatikan seluruh citra sejak lapis terbawah, sisanya berjarak pandang pendek seperti konvolusi awal. Pelatihan swa-terawasi dengan prediksi petak tersembunyi memberi ViT-B/16 akurasi 79,9% pada ImageNet: naik 2 poin dari latih dari nol, tetapi 4 poin di bawah pelatihan terawasi.

## Kelebihan dan Keterbatasan

Kelebihan: (1) arsitektur sederhana dan nyaris tanpa modifikasi, sehingga implementasi Transformer NLP yang matang dapat dipakai langsung; (2) efisiensi komputasi pada skala besar, sebagaimana ditunjukkan studi penskalaan; (3) perhatian global sejak lapis pertama; (4) kemampuan transfer yang kuat pada data sedikit, terbukti pada VTAB.

Keterbatasan: (1) keunggulan mutlak bergantung pada pelatihan awal raksasa; tanpa itu model kalah dari CNN biasa; (2) dataset terkuat, JFT-300M, bersifat internal — dari sisi rekayasa, hasil terbaik makalah sulit direplikasi pihak luar, dan varian ImageNet-21k adalah jalur praktis yang tersedia; (3) biaya *attention* yang kuadratik membuat resolusi tinggi mahal — secara konseptual, ini menghambat tugas prediksi padat seperti deteksi dan segmentasi, yang oleh penulis sendiri dibiarkan sebagai pekerjaan lanjutan; (4) representasinya satu skala tanpa hierarki resolusi, padahal banyak tugas visi memerlukan fitur multi-skala — diperbaiki oleh penerusnya.

## Kaitan dengan Bab Lain

Bab-bab sebelumnya dalam klaster Fondasi RGB — dari YOLOv1 ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) hingga keluarga R-CNN — berpijak pada *backbone* konvolusi, dengan ResNet ([bab 147](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)) sebagai pembanding utama ViT melalui varian BiT-nya. DETR ([bab 022](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md)) pada tahun yang sama menunjukkan Transformer cocok untuk deteksi, tetapi masih bergantung pada fitur CNN; ViT menghapus ketergantungan itu untuk klasifikasi. Penerusnya langsung menyasar kelemahan ViT: Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)) dan Swin Transformer ([bab 025](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)) mengembalikan hierarki multi-skala dan perhatian berjendela agar Transformer layak menjadi *backbone* prediksi padat. DPT ([bab 067](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)) memakai ViT untuk estimasi kedalaman monokular, dan VST ([bab 042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)) memindahkannya ke deteksi objek menonjol RGB-D — dua jalur menuju klaster Estimasi Kedalaman dan RGB-D SOD.

## Poin untuk Sitasi

Kutip dengan kunci `dosovitskiy2021vit`. Ringkasan yang aman dikutip: "ViT menerapkan Transformer standar pada urutan petak citra 16×16 dan menunjukkan bahwa dengan pelatihan awal berskala besar, model tanpa konvolusi mengungguli CNN terbaik pada klasifikasi citra — 88,55% top-1 pada ImageNet dan 77,63% pada VTAB — dengan komputasi pelatihan awal 2–4 kali lebih hemat dari ResNet setara; pada data terbatas, CNN tetap unggul." Angka-angka tersebut berasal dari teks naskah (arXiv:2010.11929v2). Yang perlu diverifikasi ke tabel naskah sebelum sitasi formal: konfigurasi pasti varian Base/Large/Huge pada Tabel 1 (jumlah lapis, dimensi, *head*, dan parameter), angka per-benchmark setiap model pada Tabel 2, serta biaya TPUv3-core-days masing-masing model — ketiganya hanya tersedia sebagai gambar tabel pada versi HTML.
