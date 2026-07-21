# 048 - CCAFNet: Crossflow and Cross-Scale Adaptive Fusion Network for Detecting Salient Objects in RGB-D Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2022ccafnet` |
| Judul asli | CCAFNet: Crossflow and Cross-Scale Adaptive Fusion Network for Detecting Salient Objects in RGB-D Images |
| Penulis | Wujie Zhou, Yun Zhu, Jingsheng Lei, Jian Wan, Lu Yu |
| Tahun | 2022 |
| Venue | IEEE Transactions on Multimedia, vol. 24, hal. 2192–2204 |
| Tema | RGB-D SOD |

## Tautan Akses
- **DOI / IEEE Xplore:** https://doi.org/10.1109/TMM.2021.3077767
- **Kode sumber resmi (PyTorch):** https://github.com/zyrant/CCAFNet
- **Google Scholar:** https://scholar.google.com/scholar?q=CCAFNet%3A%20Crossflow%20and%20Cross-Scale%20Adaptive%20Fusion%20Network%20for%20Detecting%20Salient%20Objects%20in%20RGB-D%20Images
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=CCAFNet%3A%20Crossflow%20and%20Cross-Scale%20Adaptive%20Fusion%20Network%20for%20Detecting%20Salient%20Objects%20in%20RGB-D%20Images&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan CCAFNet (*Crossflow and Cross-Scale Adaptive Fusion Network*), jaringan konvolusi untuk deteksi objek salien (*salient object detection*, SOD) pada citra RGB-D. SOD adalah tugas menghasilkan peta saliency, yaitu citra keluaran yang menandai per piksel wilayah objek yang paling menonjol dalam sebuah adegan. Citra RGB-D adalah pasangan citra warna biasa dan peta kedalaman (*depth map*), citra yang setiap pikselnya menyatakan jarak permukaan ke kamera.

Menurut para penulisnya, metode RGB-D SOD sebelumnya menggabungkan kedua modalitas pada salah satu dari tiga domain fusi (masukan, peta fitur, atau keluaran) dan kurang memanfaatkan aliran silang antara fitur tingkat tinggi yang kaya makna dan fitur tingkat rendah yang kaya detail. CCAFNet menjawabnya dengan dua modul fusi yang bekerja berbeda per tingkat — modul fusi spasial (SFM) pada tingkat rendah dan modul fusi kanal (CFM) pada tingkat tinggi — yang dihubungkan oleh fusi begerbang lintas skala. Pada tujuh *dataset* tolok ukur, CCAFNet menyamai atau melampaui tiga belas metode pembanding; pada NLPR dan SIP, CCAFNet menjadi yang terbaik pada seluruh metrik yang dilaporkan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD berbasis RGB saja rapuh ketika objek salien memiliki warna atau tekstur yang mirip latar belakangnya. Peta kedalaman memberi informasi pelengkap: batas objek umumnya tegas pada peta kedalaman, dan kedalaman tidak berubah ketika pencahayaan atau warna berubah. Karena itu penelitian RGB-D SOD berkembang, dan praktik umumnya terbagi atas tiga domain fusi: fusi awal (menggabungkan RGB dan kedalaman sebelum atau tepat setelah masukan), fusi tengah (menggabungkan peta fitur dari dua jaringan), dan fusi akhir (menggabungkan peta saliency hasil masing-masing modalitas).

Dua kekurangan dicatat makalah ini pada pendekatan tersebut. Pertama, aliran silang (*crossflow*) antara informasi tingkat tinggi dan tingkat rendah belum dimanfaatkan dengan baik: fusi umumnya dilakukan per tingkat secara terpisah, sehingga makna dari tingkat dalam tidak ikut membimbing penggabungan detail pada tingkat dangkal. Kedua, dekoder pada model-model tersebut memakai konvolusi konvensional yang memerlukan banyak perhitungan. Kedua hal ini relevan bagi karya pembanding yang telah dibahas pada bab sebelumnya, misalnya DMRA (bab 035), BBS-Net (bab 036), dan D3Net (bab 037).

## Ide Utama

Gagasan inti CCAFNet adalah memperlakukan kedua modalitas secara berbeda sesuai kekuatan masing-masing pada setiap tingkat fitur. Pada tingkat rendah (resolusi besar, detail tepi), peta kedalaman lebih dapat dipercaya untuk urusan lokasi, sehingga kedalaman dipakai menghasilkan peta atensi spasial yang memboboti fitur RGB per posisi. Pada tingkat tinggi (resolusi kecil, makna global), fitur RGB lebih kaya makna, sehingga RGB dipakai menghasilkan bobot kanal yang memboboti fitur kedalaman per kanal.

Gagasan kedua adalah fusi lintas skala yang adaptif: penggabungan dua modalitas pada setiap tingkat dikendalikan gerbang yang dipelajari, dan setiap tahap fusi di bawah tingkat terdalam menerima kembali peta hasil fusi dari tingkat yang lebih kasar. Dengan cara ini makna mengalir dari tingkat dalam ke tingkat dangkal — inilah yang dimaksud *crossflow* — sementara gerbang menentukan besar kontribusi tiap modalitas dan tiap skala secara otomatis.

## Cara Kerja Langkah demi Langkah

### Encoder Dua Aliran

CCAFNet memakai dua *backbone* (jaringan pengekstrak fitur utama) VGG-16 dengan *batch normalization* (normalisasi statistik antar-contoh dalam satu kelompok data untuk menstabilkan pelatihan), satu untuk RGB dan satu untuk kedalaman, keduanya diinisialisasi dari bobot terlatih ImageNet. Kedalaman dimasukkan sebagai citra tiga kanal. Setiap aliran menghasilkan lima tingkat fitur. Untuk masukan 224×224 piksel, ukurannya berturut-turut 224×224×64, 112×112×128, 56×56×256, 28×28×512, dan 14×14×512 (tinggi×lebar×kanal).

### Modul Fusi Spasial (SFM) pada Tingkat 1–3

SFM memanfaatkan fitur kedalaman untuk memperbaiki fitur RGB secara spasial. Fitur kedalaman tingkat-i dilewatkan konvolusi 3×3 berkeluaran satu kanal, kemudian fungsi Hsigmoid. Hsigmoid adalah aproksimasi sigmoid berbasis potongan linier, h(x) = relu6(x + 3)/6, yang murah dihitung dan mengeluarkan nilai pada rentang [0,1]. Hasilnya adalah peta atensi spasial M berukuran sama dengan peta fitur. Fitur RGB lalu diboboti: R′ = R + R ⊙ M, dengan ⊙ menyatakan perkalian per elemen. Contoh: pada tingkat 1, M berukuran 224×224 dan diterapkan ke seluruh 64 kanal fitur RGB; posisi yang oleh kedalaman dianggap wilayah objek mendapat bobot mendekati satu, posisi lain mendekati nol. Bentuk residual (penjumlahan kembali R) memastikan informasi asli tidak hilang.

### Modul Fusi Kanal (CFM) pada Tingkat 4–5

CFM bekerja sebaliknya: fitur RGB tingkat tinggi memperbaiki fitur kedalaman per kanal. Fitur RGB dirata-ratakan secara global (*global average pooling*, merata-ratakan setiap kanal menjadi satu angka), dilewatkan dua lapis linier dengan pereduksian 4 (512→128→512), lalu Hsigmoid menghasilkan vektor bobot kanal w. Fitur kedalaman diboboti: D′ = D + D ⊙ w. Pola ini menyerupai mekanisme *squeeze-and-excitation*, yaitu pembobotan ulang kanal berdasarkan statistik global citra; interpretasinya, makna dari RGB menentukan kanal kedalaman mana yang penting.

### Fusi Begerbang Lintas Skala (*Crossflow*)

Setiap tingkat kemudian menggabungkan dua fitur hasil SFM atau CFM dengan gerbang adaptif. Kedua fitur digabungkan sepanjang kanal, dilewatkan fungsi sigmoid, lalu dibelah dua menjadi gerbang G1 dan G2. Keluarannya adalah F = G1 ⊙ x + x + G2 ⊙ y + y. Hasil fusi ini disilangkan dengan peta fusi tingkat di atasnya yang telah diperbesar resolusinya: pada implementasi resmi, F dimodulasi oleh selisih absolutnya terhadap peta tersebut, F ← F + |F − up(F_atas)| ⊙ F, sehingga wilayah yang berbeda dari prediksi kasar mendapat penguatan untuk diproses lebih lanjut. Rangkaian aliran antar-tingkat inilah yang disebut *crossflow*, dan gerbang yang dipelajari inilah yang membuat fusi bersifat adaptif lintas skala.

Alur data lengkapnya dirangkum pada diagram berikut.

```
citra RGB  ─► VGG-16 BN (RGB)   ─► R1 R2 R3 R4 R5
peta depth ─► VGG-16 BN (depth) ─► D1 D2 D3 D4 D5

tingkat 1-3  SFM:  D_i ─► konv 3x3 ─► Hsigmoid ─► peta atensi M
                   R'_i = R_i + R_i * M   (RGB dibobot per lokasi)
tingkat 4-5  CFM:  R_i ─► rataan global ─► 2 linier ─► Hsigmoid ─► w
                   D'_i = D_i + D_i * w   (depth dibobot per kanal)

gerbang per tingkat: concat(x, y) ─► sigmoid ─► belah ─► G1, G2
                     F = G1*x + x + G2*y + y
crossflow          : F_i dimodulasi selisih |F_i - up(F_{i+1})|

dekoder 5 tahap (dari kasar ke halus):
  F5 (14x14) ─► F4 (28) ─► F3 (56) ─► F2 (112) ─► F1 (224)
                 │           │          │
                 keluaran samping F2..F5, masing-masing diawasi loss
                                        F1 ─► peta saliency akhir
```

### Dekoder Multi-Keluaran dan Fungsi Loss

Dekoder bekerja dari tingkat kasar ke halus: fitur diperbesar resolusinya (*upsampling* interpolasi bilinear) dan digabungkan dengan fitur tingkat di bawahnya melalui konvolusi 3×3, pola yang menyerupai *feature pyramid network* (FPN, jalur menurun yang menggabungkan peta kasar bermakna kuat dengan peta halus berdetail kuat). Selain keluaran akhir 224×224, jaringan mengeluarkan empat keluaran samping dari tingkat 2–5; masing-masing dibandingkan langsung dengan kebenaran dasar (*ground truth*) lewat fungsi loss sendiri. Teknik ini disebut *deep supervision* (pengawasan bertingkat) dan berfungsi memperlancar aliran gradien saat pelatihan. Makalah juga mengusulkan *purification loss* agar batas objek dipelajari secara lebih presisi dan detail objek tambahan diperoleh; bentuk matematis fungsi ini tidak dibahas di sini. Sebagai motivasi efisiensi, makalah mencatat dekoder konvensional memerlukan banyak perhitungan; pada kode resmi tersedia unit konvolusi terpisah *depthwise* (konvolusi 3×3 per kanal diikuti konvolusi titik 1×1) sebagai alternatif konvolusi biasa.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tujuh dataset RGB-D SOD: NJU2K (pasangan stereo), NLPR (Kinect), DES/RGBD135 (dalam ruangan), STERE (stereoskopik), LFSD (*light field*), SIP (objek orang), dan DUT. Pelatihan mengikuti protokol umum bidang ini: gabungan data latih NJU2K dan NLPR, masukan 224×224, laju pembelajaran awal 0,0001, 200 *epoch* (satu putaran penuh pelatihan atas seluruh data latih), rincian dari kode resmi. Metrik yang dipakai adalah S-measure (kemiripan struktur peta saliency dengan kebenaran dasar), E-measure adaptif (kesejajaran pada tingkat piksel dan citra), F-measure adaptif dan maksimum (rata-rata harmonik presisi-*recall*), serta MAE (galat absolut rata-rata; makin kecil makin baik). Tiga belas metode pembanding diikutsertakan, antara lain DMRA, D3Net, CMWNet, SSF, dan BBS-Net.

Cuplikan hasil (S-measure / MAE) pada empat dataset:

| Dataset | BBS-Net | CMWNet | CCAFNet |
|---|---|---|---|
| NJU2K | 0,912 / 0,040 | 0,903 / 0,046 | 0,910 / 0,037 |
| NLPR | 0,920 / 0,027 | 0,917 / 0,029 | 0,922 / 0,026 |
| SIP | 0,871 / 0,057 | 0,868 / 0,062 | 0,877 / 0,054 |
| LFSD | 0,843 / 0,081 | 0,876 / 0,067 | 0,827 / 0,087 |

Interpretasinya: pada NLPR dan SIP, CCAFNet unggul pada seluruh metrik (NLPR: S 0,922; E-measure 0,952; MAE 0,026), tanda fusi adaptifnya efektif baik pada adegan Kinect maupun objek orang. Pada NJU2K, S-measure-nya 0,910, sedikit di bawah BBS-Net (0,912), tetapi MAE-nya terbaik (0,037) — keluarannya lebih bersih secara rata-rata piksel. Pada DES, CCAFNet terbaik pada empat dari lima metrik (S 0,930; MAE 0,018). Sebaliknya, pada LFSD CCAFNet tertinggal jelas (S 0,827 berbanding 0,876 milik CMWNet), dan pada DUT serta STERE beberapa pembanding masih lebih baik. Temuan ini konsisten dengan klaim penulis bahwa hasilnya setara dengan metode terdepan, bukan selalu melampauinya.

## Kelebihan dan Keterbatasan

Kelebihan CCAFNet terletak pada fusi asimetris yang sesuai karakter tiap tingkat: detail spasial diambil dari kedalaman, makna kanal diambil dari RGB, dan gerbang adaptif menengahi variasi kontribusi antar-modalitas tanpa aturan manual. Pengawasan multi-skala dan aliran silang antar-tingkat menghasilkan MAE yang konsisten rendah pada sebagian besar dataset, tanda batas objek yang lebih presisi.

Keterbatasannya ada empat. Pertama, pada LFSD dan DUT hasilnya tertinggal dari beberapa pembanding, sehingga keunggulannya tidak seragam lintas domain. Kedua, dua aliran VGG-16 penuh menggandakan biaya *backbone*; dari sisi rekayasa, ini membebani memori dan kecepatan dibanding desain berbagi bobot, dan sumber yang tersedia tidak melaporkan jumlah parameter atau kecepatan inferensi. Ketiga, secara konseptual fusi tetap bergantung pada mutu peta kedalaman; mekanisme SFM justru memakai kedalaman sebagai pemberi atensi pada tingkat rendah, sehingga kedalaman berderau berpotensi menyesatkan pembobotan sejak awal. Keempat, konteks global terbatas karena seluruh jaringan berbasis konvolusi lokal.

## Kaitan dengan Bab Lain

CCAFNet berdiri di atas garis penelitian RGB-D SOD yang telah dibahas pada bab-bab sebelumnya. Desain dua aliran dengan fusi bertingkat sejalan dengan [DMRA (bab 035)](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) dan [BBS-Net (bab 036)](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md); implementasi resminya dinyatakan dibangun di atas kode BBS-Net dan CPD, sedangkan protokol tolok ukurnya mengikuti [D3Net (bab 037)](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md). Kontribusinya melengkapi garis tersebut dengan fusi yang sekaligus adaptif antar-modalitas dan lintas skala. Arah berikutnya dalam klaster ini adalah penggantian *backbone* konvolusi dengan transformer untuk memperoleh konteks global, misalnya pada [Visual Saliency Transformer (bab 042)](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md), yang menyerang keterbatasan konvolusi lokal yang disebut di atas.

## Poin untuk Sitasi

Kutip dengan kunci `zhou2022ccafnet`. Ringkasan yang aman dikutip: "CCAFNet melakukan fusi RGB–kedalaman secara adaptif melalui modul fusi spasial pada tingkat rendah dan modul fusi kanal pada tingkat tinggi, dihubungkan gerbang lintas skala dengan aliran silang antar-tingkat, dan mencapai hasil yang kompetitif pada tujuh tolok ukur RGB-D SOD." Catatan verifikasi sebelum sitasi formal: (1) seluruh angka hasil di atas dibaca dari tabel hasil pada repositori resmi penulis, bukan dari PDF jurnal — cocokkan dengan naskah IEEE TMM; (2) bentuk matematis *purification loss* serta klaim efisiensi dekoder belum diverifikasi ke naskah; (3) makalah terbit *early access* pada 2021 dan tercatat pada volume 24 tahun 2022 — pilih tahun sesuai gaya sitasi yang dipakai.
