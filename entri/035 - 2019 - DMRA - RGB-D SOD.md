# 035 - Depth-Induced Multi-Scale Recurrent Attention Network for Saliency Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `piao2019dmra` |
| Judul asli | Depth-Induced Multi-Scale Recurrent Attention Network for Saliency Detection |
| Penulis | Yongri Piao, Wei Ji, Jingjing Li, Miao Zhang, Huchuan Lu (Dalian University of Technology) |
| Tahun | 2019 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2019), hlm. 7254–7263 |
| Tema | RGB-D SOD |

## Tautan Akses
- **PDF resmi (CVF Open Access):** https://openaccess.thecvf.com/content_ICCV_2019/html/Piao_Depth-Induced_Multi-Scale_Recurrent_Attention_Network_for_Saliency_Detection_ICCV_2019_paper.html
- **Kode dan dataset (GitHub resmi):** https://github.com/DUT-IIAU-OIP-Lab/DMRA_RGBD-SOD
- **Google Scholar:** https://scholar.google.com/scholar?q=Depth-Induced%20Multi-Scale%20Recurrent%20Attention%20Network%20for%20Saliency%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Depth-Induced%20Multi-Scale%20Recurrent%20Attention%20Network%20for%20Saliency%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DMRANet (*Depth-induced Multi-scale Recurrent Attention Network*), jaringan untuk deteksi objek menonjol (*salient object detection*, SOD) dari pasangan citra RGB dan peta kedalaman. SOD menghasilkan *peta saliency*, peta keabuan yang nilainya menyatakan tingkat kemenonjolan tiap piksel; peta kedalaman adalah citra yang tiap pikselnya menyatakan jarak permukaan ke kamera. Masalah yang dipecahkan adalah kegagalan metode SOD pada skenario kompleks — objek transparan, objek ganda, latar serupa objek, pencahayaan rendah — serta cara fusi RGB-D sebelumnya yang menggabungkan kedua modalitas tanpa membedakan kontribusi tiap tingkat dan tiap skala fitur.

Jaringan ini tersusun atas tiga komponen: *depth refinement block* (DRB) yang memadukan fitur RGB dan kedalaman pada lima tingkat secara residual, modul pembobotan multi-skala terinduksi kedalaman (DMSW) yang menimbang enam fitur berskala berbeda berdasarkan isyarat kedalaman, dan modul atensi berulang (RAM) yang menyempurnakan peta saliency dalam tiga langkah berbasis memori. Pada tujuh dataset, model ini menempati peringkat pertama untuk seluruh metrik yang diuji terhadap 16 metode pembanding. Makalah ini juga merilis dataset RGB-D baru berisi 1.200 pasangan citra dengan skenario yang lebih kompleks.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum era CNN, metode SOD bergantung pada fitur rancangan manual seperti kontras warna dan prior latar, yang daya generalisasinya terbatas. Metode SOD berbasis CNN pada citra RGB kemudian jauh lebih akurat, tetapi tetap keliru ketika objek dan sekelilingnya serupa secara warna dan tekstur — misalnya objek transparan atau ruangan redup. Informasi kedalaman memuat struktur spasial dan tata letak tiga dimensi yang tidak bergantung pada penampakan, sehingga pasangan RGB-D menjadi jalur untuk menangani kasus-kasus tersebut.

Namun fusi RGB-D pada 2019 menyimpan tiga kelemahan spesifik. Pertama, sebagian besar metode menggabungkan fitur RGB dan kedalaman hanya dengan penggabungan kanal (*concatenation*) atau penjumlahan pada satu tingkat saja, padahal sifat fitur berbeda antar-tingkat: fitur dalam memuat semantik diskriminatif, fitur dangkal memuat detail tepi lokal, dan keduanya saling melengkapi. Kedua, objek dalam satu adegan tersebar pada jarak dan ukuran yang berbeda; kaitan antara kedalaman dan skala objek belum pernah dimanfaatkan untuk menentukan fitur skala mana yang seharusnya dominan. Ketiga, fitur hasil fusi langsung dipakai untuk prediksi dalam satu lintasan tanpa penyempurnaan bertahap. Selain itu, dataset RGB-D SOD yang tersedia saat itu relatif kecil dan adegannya sederhana. Celah-celah inilah yang dijawab makalah ini.

## Ide Utama

Gagasan intinya tiga kalimat. Pertama, fitur kedalaman di setiap tingkat jaringan tidak dijumlahkan mentah ke fitur RGB, melainkan diubah dulu menjadi *residu* (selisih pelengkap hasil transformasi kecil), sehingga fitur RGB tetap menjadi poros dan kedalaman menambahkan isyarat yang hilang. Kedua, karena objek pada kedalaman berbeda cenderung tampak pada skala berbeda, vektor yang disarikan dari peta kedalaman dipakai sebagai bobot yang menentukan sumbangan tiap fitur multi-skala — inilah makna terinduksi kedalaman (*depth-induced*). Ketiga, peta saliency tidak dihasilkan sekali jalan, melainkan diperbaiki berulang oleh modul atensi yang membawa memori dari langkah sebelumnya.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dua Aliran

Jaringan mengikuti pola dua aliran: satu aliran untuk citra RGB, satu aliran untuk peta kedalaman. Keduanya memakai struktur sama, yaitu lima blok konvolusi VGG-19 — jaringan konvolusi 19 lapis yang bobotnya dipr latih pada ImageNet — dengan lapis *pooling* terakhir dan lapis terhubung penuh dibuang agar sesuai untuk prediksi peta. Satu-satunya perbedaan: keluaran blok terakhir aliran kedalaman diolah menjadi vektor kedalaman untuk modul DMSW. Citra masukan diseragamkan ke 256×256 piksel. Alur data selengkapnya:

```
citra RGB ──► aliran VGG-19 (5 blok) ──► f1..f5 RGB
peta depth ─► aliran VGG-19 (5 blok) ──► f1..f5 depth
                                             │
        ┌─────────────► DRB x5 ◄─────────────┘
        │  f_i = W_i( reshape( f_i^RGB + phi(f_i^depth) ) )
        ▼
   F_fuse = f1+..+f5   (resolusi 1/4 masukan, 64 kanal)
        │
        ▼                                   conv5_4 depth
   DMSW: 6 cabang paralel              pooling + conv + softmax
   (1x1 | 3x3 | pool+3x3 | D=3 | D=5 | D=7)  = V_depth (1x1x6)
        │                                          │
        ▼  F = jumlah V_depth[m] . F_m ◄───────────┘
   RAM: 3 langkah   atensi(h_{t-1}, F) ──► ConvLSTM ──► h_t
        │
        ▼  atensi spasial ──► conv 1x1 ──► upsampling x4
   peta saliency akhir
```

Diagram menunjukkan empat tahap berurutan: DRB memadukan fitur kedua aliran per tingkat menjadi `F_fuse`; DMSW memecahnya menjadi enam fitur multi-skala yang ditimbang vektor kedalaman `V_depth`; RAM menyempurnakan hasilnya dalam tiga langkah; peta akhir diperoleh setelah atensi spasial dan *upsampling* empat kali.

### Depth Refinement Block (DRB)

DRB bekerja pada tiap tingkat i = 1..5. Fitur kedalaman tingkat itu dilewatkan ke dua lapis konvolusi dengan aktivasi PReLU (fungsi aktivasi seperti ReLU, tetapi lereng sisi negatifnya ikut dipelajari), menghasilkan residu kedalaman. Residu ini ditambahkan ke fitur RGB melalui sambungan residual (penjumlahan keluaran suatu blok dengan masukannya, yang memudahkan aliran gradien saat pelatihan), sehingga fitur RGB dilengkapi isyarat kedalaman tanpa ditimpa. Hasil fusi tiap tingkat lalu diseragamkan resolusinya — diperbesar dengan interpolasi bilinear atau diperkecil dengan *max-pooling* — dirapikan skalanya oleh satu unit residual, dan disesuaikan kanalnya dengan konvolusi 1×1. Kelima fitur tingkat dijumlahkan per elemen menjadi `F_fuse`.

### Depth-Induced Multi-Scale Weighting (DMSW)

DMSW menjawab pertanyaan: fitur skala mana yang paling relevan untuk adegan ini? Dari `F_fuse`, enam cabang paralel menghasilkan enam fitur beresolusi sama dengan cakupan konteks berbeda: konvolusi 1×1, konvolusi 3×3, *max-pooling* diikuti konvolusi 3×3, dan konvolusi 3×3 terdilatasi berdilasi 3, 5, dan 7. Konvolusi terdilatasi (*atrous convolution*) merenggangkan titik sampel kernel sehingga *receptive field* (wilayah citra yang memengaruhi satu piksel keluaran) membesar tanpa menambah parameter atau menurunkan resolusi. Secara bersamaan, keluaran blok terakhir aliran kedalaman dipadatkan oleh *global average pooling* (perata-rataan seluruh peta menjadi satu angka per kanal), sebuah konvolusi, dan fungsi *softmax* (normalisasi menjadi bobot non-negatif berjumlah satu) menjadi vektor kedalaman `V_depth` berukuran 1×1×6. Fitur akhir adalah jumlah tertimbang `F = Σ V_depth[m] × F_m`: kedalaman menentukan bobot, sehingga misalnya cabang berdilasi besar yang menangkap objek besar mendapat porsi lebih ketika isyarat kedalaman menunjukkan objek dekat yang memenuhi bingkai.

### Recurrent Attention Module (RAM)

RAM terinspirasi *Internal Generative Mechanism* (IGM), teori persepsi yang menyatakan kemenonjolan pada penglihatan manusia bukan pemindahan langsung dari masukan mata, melainkan hasil serangkaian inferensi yang memanfaatkan memori. RAM menggabungkan mekanisme atensi dengan ConvLSTM — varian LSTM (*long short-term memory*, jaringan berulang dengan sel memori dan gerbang masukan, lupa, dan keluaran) yang mengganti perkalian matriks dengan konvolusi sehingga struktur spasial peta fitur terjaga.

Pada tiap langkah t, memori sebelumnya `h_{t-1}` dan fitur `F` masing-masing dikonvolusi, dijumlahkan, dipadatkan dengan *global average pooling*, dan dinormalisasi *softmax* menjadi peta atensi kanal — bobot per kanal yang menandai kanal mana yang informatif. Fitur `F` dikalikan bobot ini, lalu hasilnya masuk ConvLSTM yang memperbarui memori menjadi `h_t`. Proses berulang N = 3 langkah; keluarannya `F_c = h_3` dengan demikian membawa memori langkah-langkah sebelumnya. Sesudahnya, atensi spasial (peta bobot per piksel dari konvolusi 1×1 dan fungsi sigmoid) menekankan lokasi penting, lalu konvolusi 1×1 dan *upsampling* empat kali menghasilkan peta saliency seukuran masukan.

### Pelatihan

Jaringan dilatih *end-to-end* (seluruh komponen dioptimalkan bersama terhadap satu fungsi galat) dengan PyTorch pada satu GPU GTX 1080, memakai *softmax cross-entropy loss* terhadap kebenaran (*ground truth*), ukuran *batch* 2, momentum 0,9, dan konvergen setelah 50 epoch. Data latih adalah 800 citra dari dataset usulan ditambah 1.485 citra NJUD dan 700 citra NLPR, diperkaya augmentasi pembalikan, pemotongan, dan rotasi.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tujuh dataset: enam dataset publik — NJUD (1.985 citra), NLPR (1.000 citra, Kinect), STEREO (797 citra), LFSD (100 citra, Lytro), RGBD135 (135 citra, Kinect), SSD (80 citra) — serta dataset usulan berisi 1.200 pasangan citra RGB–kedalaman (800 dalam ruang, 400 luar ruang, kamera Lytro) yang memuat objek ganda, objek transparan, latar serupa objek, dan pencahayaan rendah. Metriknya lima: kurva *precision–recall*; F-measure (rata-rata harmonik berbobot antara *precision* dan *recall*); MAE (rata-rata selisih absolut dengan kebenaran); S-measure (kemiripan struktur kawasan); dan E-measure (keselarasan statistik tingkat citra dan kecocokan piksel lokal). Untuk MAE makin kecil makin baik; untuk tiga lainnya makin besar makin baik. Pembandingnya 16 metode: 5 RGB-D berbasis CNN (antara lain PCA, jaringan fusi progresif CVPR 2018, pembanding terkuat), 5 RGB-D tradisional, dan 6 RGB berbasis CNN.

DMRANet menempati peringkat pertama pada ketujuh dataset untuk seluruh metrik. Pada NLPR, F-measure 0,855 dan MAE 0,031, dibandingkan PCA 0,794 dan 0,044 — kesalahan peta turun sekitar 30% relatif. Pada NJUD, F-measure 0,872 dan MAE 0,051 versus 0,844 dan 0,059 milik PCA. Pada dataset usulan yang paling sulit, jarak melebar: F-measure 0,883 versus 0,760 dan MAE 0,048 versus 0,100, artinya kesalahan rata-rata terpangkas lebih dari separuh — konsisten dengan tujuan desain untuk adegan kompleks. Terhadap metode RGB murni terbaik (PiCANet), selisihnya lebih besar: pada NJUD PiCANet mencapai F-measure 0,806, sekitar 6,6 poin di bawah DMRANet, yang menunjukkan kontribusi nyata modalitas kedalaman.

Analisis ablasi (uji kontribusi tiap komponen dengan melepasnya satu per satu) menunjukkan kenaikan bertingkat. Pada dataset usulan, F-measure naik dari 0,828 (garis dasar fusi biasa) menjadi 0,839 dengan DRB, 0,861 dengan DMSW, dan 0,883 dengan RAM penuh; MAE turun dari 0,070 menjadi 0,048. Menghilangkan panduan kedalaman pada DMSW (bobot diganti konvolusi 1×1 biasa) menurunkan F-measure ke 0,855 — bukti bahwa vektor kedalaman, bukan sekadar tambahan parameter, yang membawa perbaikan. Mengganti RAM dengan blok atensi kanal–spasial biasa hanya mencapai 0,869; keunggulan RAM berasal dari penyempurnaan berulang bermemori, bukan dari atensi semata. Pada NLPR, lonjakan terbesar justru datang dari RAM: 0,801 menjadi 0,855.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah fusi yang berprinsip pada dua arah: komplementaritas multi-tingkat ditangani DRB, dan seleksi skala ditangani DMSW dengan bobot yang diturunkan dari data kedalaman itu sendiri. RAM memberi keuntungan terbesar pada dataset tersulit. Model dilatih *end-to-end* tanpa pasca-pemrosesan, dan kode, model terlatih, serta dataset dirilis terbuka sehingga mudah direproduksi.

Keterbatasannya, pertama, jalur panduan DMSW bergantung pada mutu peta kedalaman; kedalaman berderau dari sensor murah akan merambat ke bobot skala. Kedua, dari sisi rekayasa, dua aliran VGG-19 ditambah enam cabang multi-skala dan tiga langkah ConvLSTM membuat komputasi jauh lebih berat daripada SOD satu aliran; makalah tidak melaporkan kecepatan inferensi maupun jumlah parameter, sehingga biaya penerapannya tidak dapat dinilai dari naskah. Ketiga, secara konseptual, RAM menjalankan tiga langkah berulang tanpa analisis sensitivitas terhadap jumlah langkah; belum jelas apakah tiga adalah titik optimal. Keempat, *backbone* VGG-19 membatasi mutu representasi dibandingkan jaringan yang lebih baru.

## Kaitan dengan Bab Lain

Bab ini adalah entri pertama klaster RGB-D SOD dalam tinjauan dan menetapkan dua gagasan yang diwarisi bab-bab berikutnya: fusi multi-tingkat RGB–kedalaman dan pemanfaatan kedalaman sebagai pemandu, bukan sekadar masukan tambahan. Fusi yang lebih hemat melalui interaksi dua arah antar-aliran dikembangkan pada [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), sedangkan pertanyaan kapan kedalaman benar-benar membantu dijawab eksplisit oleh [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md). Pembelajaran gabungan lintas-tugas untuk fusi RGB-D dibahas pada [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md). Dari sisi pondasi, pemakaian *backbone* CNN terpralatih mengikuti tradisi yang sama dengan bab [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), meskipun tugasnya berbeda: SOD menghasilkan peta per piksel, bukan kotak objek.

## Poin untuk Sitasi

Kunci BibTeX: `piao2019dmra`.

Ringkasan aman dikutip: DMRANet (Piao dkk., ICCV 2019) adalah jaringan SOD RGB-D dua aliran berbasis VGG-19 dengan tiga komponen — fusi residual multi-tingkat (DRB), pembobotan fitur multi-skala yang dipandu vektor kedalaman (DMSW), dan penyempurnaan saliency berulang tiga langkah berbasis ConvLSTM dan atensi (RAM). Model ini menempati peringkat pertama pada tujuh dataset RGB-D terhadap 16 metode pembanding, dan makalahnya memperkenalkan dataset RGB-D baru berisi 1.200 pasangan citra dengan pembagian 800 latih dan 400 uji.

Catatan verifikasi sebelum sitasi formal: (1) seluruh angka pada bab ini dibaca langsung dari Tabel 1–3 naskah PDF CVF, tetapi disarankan mencocokkan ulang bila dikutip satu per satu; (2) nama resmi dataset pada repositori penulis adalah *DUTLF-Depth*, sedangkan literatur selanjutnya banyak menyebutnya *DUT-RGBD* — pastikan nama yang dipakai konsisten dengan naskah yang dirujuk; (3) kecepatan inferensi dan jumlah parameter tidak dilaporkan dalam naskah; (4) makalah ini tidak memiliki versi arXiv, sehingga rujukan kanonik adalah prosiding ICCV 2019.
