# 153 - RGB-D Salient Object Detection: A Survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2021rgbdsurvey` |
| Judul Asli | RGB-D Salient Object Detection: A Survey |
| Penulis | Zhou, Tao; Fan, Deng-Ping; Cheng, Ming-Ming; Shen, Jianbing; Shao, Ling |
| Tahun | 2021 |
| Venue / Jurnal | Computational Visual Media |
| Tema klaster | Fusi Multimodal |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RGB-D%20Salient%20Object%20Detection%3A%20A%20Survey
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RGB-D%20Salient%20Object%20Detection%3A%20A%20Survey&sort=relevance
- **ArXiv (PDF & Metadata):** https://arxiv.org/abs/2008.00230
- **Repositori Resmi GitHub:** https://github.com/taozh2017/RGBD-SODsurvey

## Gambaran Umum
Makalah ini adalah survei komprehensif pertama yang secara sistematis meninjau perkembangan metode Deteksi Objek Menonjol berbasis RGB-D (*RGB-D Salient Object Detection* atau RGB-D SOD). SOD bertujuan meniru sistem visual manusia dalam mengidentifikasi dan mensegmentasi objek paling menarik perhatian dalam suatu citra. Penulis memetakan lanskap riset dari metode berbasis fitur buatan tangan (*handcrafted features*) sampai arsitektur pembelajaran mendalam (*deep learning*) modern. Selain menyajikan taksonomi fusi multimodal (awal, tengah, dan akhir), survei ini mengulas dataset pembanding (*benchmark*), metrik evaluasi matematis, serta memperkenalkan domain terkait seperti deteksi objek menonjol berbasis medan cahaya (*light field* SOD).

Melalui analisis atribut terperinci pada 24 model representatif (9 tradisional dan 15 berbasis pembelajaran mendalam), survei ini memberikan evaluasi kuantitatif yang solid. Repositori kode dan evaluasi yang disediakan penulis berfungsi sebagai standar pembanding terbuka. Masalah utama yang dipecahkan adalah tidak adanya klasifikasi terstruktur dan evaluasi terstandar di tengah ledakan model RGB-D SOD, sehingga membantu peneliti mengidentifikasi strategi fusi mana yang paling efektif.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi objek menonjol (*salient object detection* / SOD) tradisional sangat mengandalkan citra RGB 2D. Namun, informasi RGB murni sering kali gagal dalam skenario menantang, seperti ketika objek memiliki penampilan visual atau warna yang sangat mirip dengan latar belakang (kamuflase rendah), atau ketika kondisi pencahayaan sangat bervariasi. Kemunculan sensor kedalaman konsumen yang terjangkau, seperti Microsoft Kinect, melahirkan modalitas citra RGB-D (RGB + *depth*) yang menyediakan informasi spasial dan struktural tambahan 3D.

Meseipun demikian, integrasi informasi kedalaman mendatangkan tantangan baru. Pertama, peta kedalaman dari sensor murah sering kali mengandung derau (*noise*), ketidakselarasan spasial (*misalignment*), dan hilangnya detail tepi. Pendekatan fusi multimodal yang ada sangat bervariasi dan belum terstruktur, baik di tingkat masukan (*early fusion*), lapisan representasi menengah (*middle fusion*), maupun prediksi akhir (*late fusion*). Di samping itu, literatur tersebar tanpa adanya standardisasi dataset pengujian dan metrik evaluasi yang konsisten. Akibatnya, peneliti sulit menentukan metode mana yang secara objektif unggul dan komponen arsitektur apa yang berkontribusi terhadap keberhasilan model fusi multimodal tersebut. Kurangnya peta jalan teoretis dan metodologis yang terpadu inilah yang diatasi oleh Zhou dkk.

## Ide Utama
Gagasan inti makalah survei ini adalah membangun taksonomi formal untuk mengklasifikasikan metode fusi multimodal pada RGB-D SOD berdasarkan **"kapan"** dan **"bagaimana"** informasi RGB dan kedalaman diintegrasikan. Penulis membagi arsitektur fusi menjadi tiga paradigma utama: fusi awal (*early fusion*), fusi tengah (*middle fusion*), dan fusi akhir (*late fusion*). 

Secara mekanis, masukan berupa citra RGB $\mathbf{I}_{RGB} \in \mathbb{R}^{H \times W \times 3}$ dan peta kedalaman $\mathbf{I}_{D} \in \mathbb{R}^{H \times W \times 1}$ diproses untuk menghasilkan peta saliens final $\mathbf{S} \in [0, 1]^{H \times W}$. Perbedaan utama ketiga paradigma ini terletak pada titik temu aliran data. Fusi awal menggabungkan $\mathbf{I}_{RGB}$ dan $\mathbf{I}_{D}$ menjadi tensor 4-saluran sebelum ekstraksi fitur dilakukan oleh satu tulang punggung (*backbone*). Fusi tengah menggunakan ekstraktor fitur paralel untuk mengekstrak fitur RGB dan kedalaman secara independen pada tingkat resolusi yang berbeda, kemudian melakukan interaksi lintas-modal di tingkat fitur sebelum didekode menjadi peta saliens. Fusi akhir menghasilkan dua peta saliens sementara secara independen dari masing-masing modalitas, lalu menggabungkannya di tahap akhir prediksi. Penulis juga memetakan domain *light field* SOD sebagai ekstensi dari informasi kedalaman dan merumuskan metrik evaluasi terstandardisasi untuk analisis performa yang adil.

## Cara Kerja Langkah demi Langkah
Metodologi survei dan klasifikasi yang diusulkan oleh Zhou dkk. disusun secara terstruktur berdasarkan taksonomi berikut:

```
       ┌─────────────────────────────────────────────────────────┐
       │             Metodologi Survei RGB-D SOD                 │
       └────────────────────────────┬────────────────────────────┘
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         ▼                                                     ▼
┌─────────────────┐                                   ┌──────────────────┐
│ Klasifikasi     │                                   │ Metrik & Dataset │
│ Arsitektur      │                                   │ Benchmarking     │
└────────┬────────┘                                   └────────┬─────────┘
         │                                                     │
         ├─► Tradisional (Handcrafted)                         ├─► NJU2K, NLPR, SIP
         │                                                     │
         └─► Deep Learning (Fusi Multimodal)                   └─► S-measure, MAE,
               │                                                   E-measure, F-measure
               ├─► Early Fusion (Input-level)
               │
               ├─► Middle Fusion (Feature-level)
               │     ├── Single-stream
               │     └── Multi-stream
               │
               └─► Late Fusion (Decision-level)
```

### Klasifikasi Model Tradisional vs. Pembelajaran Mendalam
Survei ini memisahkan metode RGB-D SOD menjadi dua era utama: metode tradisional yang mengandalkan fitur buatan tangan (*handcrafted*) dan metode berbasis pembelajaran mendalam (*deep learning*).
1. **Metode Tradisional (Sebelum 2015):** Menggunakan aturan heuristik (*heuristic rules*) dan deskriptor tingkat rendah. Kedalaman diekstrak menggunakan fitur kontras kedalaman (*depth contrast*), perbedaan histogram, penandaan batas (*boundary prior*), dan pemodelan spasial graf. Contoh modelnya termasuk LHM (2012), ACSD (2014), dan DESM (2014). Keterbatasan utamanya adalah ketidakmampuan menangkap semantik objek tingkat tinggi, sehingga sangat sensitif terhadap variasi latar belakang dan derau pada sensor.
2. **Metode Pembelajaran Mendalam (Mulai 2015):** Memanfaatkan Convolutional Neural Networks (CNN) untuk mempelajari representasi fitur secara otomatis. Model ini menggunakan tulang punggung populer seperti VGG-16, ResNet-50, atau ResNeXt-101. Metode pembelajaran mendalam mampu menangkap fitur semantik tingkat tinggi pada lapisan dalam dan fitur spasial tingkat rendah pada lapisan dangkal, kemudian menggabungkannya secara dinamis dengan fitur kedalaman.

### Taksonomi Strategi Fusi Multimodal Deep Learning
Penulis membagi strategi fusi multimodal pada model pembelajaran mendalam menjadi tiga kelompok berdasarkan letak integrasi fiturnya:

```
1. Early Fusion (Fusi Awal):
RGB ───┐
       ├─► [Concatenate] ──► [Backbone] ──► [Decoder] ──► Peta Saliens
Depth ─┘

2. Middle Fusion (Fusi Tengah):
RGB ───► [RGB Backbone] ───────┐
                               ├─► [Fusion Module] ──► [Decoder] ──► Peta Saliens
Depth ──► [Depth Backbone] ────┘

3. Late Fusion (Fusi Akhir):
RGB ───► [RGB Backbone] ──► [RGB Decoder] ───┐
                                             ├─► [Fusion Module] ──► Peta Saliens
Depth ──► [Depth Backbone] ──► [Depth Dec.] ─┘
```

- **Fusi Awal (*Early Fusion* / *Input-level Fusion*):** Penggabungan dilakukan pada tahap masukan jaringan. Citra RGB 3-saluran dan peta kedalaman 1-saluran digabungkan melalui konkatenasi menjadi tensor 4-saluran ($H \times W \times 4$). Tensor ini dimasukkan ke dalam satu tulang punggung ekstraksi fitur tunggal. Kelebihannya adalah kesederhanaan arsitektur dan pemanfaatan korelasi spasial dasar secara langsung. Kekurangannya adalah ketidakmampuan model untuk menyesuaikan perbedaan representasi intrinsik antara informasi visual RGB (warna dan tekstur) dan kedalaman (geometri spasial), yang sering kali berujung pada penurunan performa jika peta kedalaman memiliki banyak derau.
- **Fusi Tengah (*Middle Fusion* / *Feature-level Fusion*):** Integrasi dilakukan pada lapisan menengah enkoder atau dekoder. RGB dan kedalaman diekstrak secara paralel menggunakan aliran independen. Fitur-fitur ini kemudian digabungkan secara interaktif di berbagai tingkat resolusi (multi-skala). Konsep ini mendominasi penelitian karena memungkinkan model mempelajari representasi spesifik modalitas sebelum melakukan pertukaran informasi. Fusi tengah dibagi lagi menjadi dua sub-tipe:
  1. *Single-stream*: Fitur kedalaman disuntikkan ke dalam tulang punggung utama RGB untuk memandu ekstraksi fitur visual tanpa memerlukan tulang punggung penuh untuk kedalaman.
  2. *Multi-stream*: Dua tulang punggung lengkap digunakan secara paralel untuk RGB dan kedalaman, lalu fitur-fitur dari keduanya dihubungkan secara silang melalui modul interaksi lintas-modal (*cross-modal interaction*), seperti mekanisme atensi (*attention mechanism*).
- **Fusi Akhir (*Late Fusion* / *Decision-level Fusion*):** Penggabungan dilakukan pada tahap akhir prediksi. Aliran RGB dan kedalaman berjalan sepenuhnya terpisah untuk memprediksi peta saliens kasar masing-masing. Peta-peta prediksi ini kemudian digabungkan melalui operasi matematika sederhana (seperti rata-rata berbobot atau perkalian elemen) atau melalui sub-jaringan dekoder kecil untuk menghasilkan peta saliens final. Keunggulannya adalah ketahanan terhadap derau pada salah satu modalitas, karena kegagalan pada satu aliran tidak langsung merusak representasi aliran lain. Namun, fusi akhir kehilangan kesempatan untuk mengeksploitasi korelasi spasial tingkat menengah yang kaya antara tekstur dan kedalaman.

### Analisis Deteksi Objek Menonjol berbasis Medan Cahaya (Light Field SOD)
Selain citra RGB-D, survei ini juga meninjau perkembangan deteksi objek menonjol berbasis medan cahaya (*light field* SOD / LF-SOD). Citra medan cahaya merekam tidak hanya intensitas cahaya tetapi juga arah sinar cahaya di ruang 3D. Ini menghasilkan struktur data multi-pandang yang kaya (*sub-aperture images*) dan citra fokus ganda (*multi-focus images*). Informasi kedalaman dapat diturunkan secara implisit dari paralaks antar-pandang. Survei ini mengulas metodologi ekstraksi informasi fokus dan kedalaman dari medan cahaya serta mengevaluasi model-model LF-SOD (seperti LFS, LFSSD, dan DLSD) pada dataset khusus medan cahaya seperti LFSD (100 citra), HFUT-Lytro (300 citra), dan DUT-LF (1.462 citra).

### Metodologi Evaluasi Matematis
Penulis merangkum empat metrik utama yang digunakan untuk mengevaluasi kinerja model secara kuantitatif:
1. **Structure-measure ($S_\alpha$):** Menilai kemiripan struktural antara prediksi $S$ dan kebenaran dasar (*ground truth*) $G$. Diformulasikan sebagai:
   $$S_\alpha = \alpha S_o(S, G) + (1 - \alpha) S_r(S, G)$$
   di mana $S_o$ mengevaluasi kemiripan global objek, $S_r$ kemiripan wilayah lokal, dan $\alpha = 0,5$.
2. **Enhanced-alignment Measure ($E_\phi$):** Mengukur keselarasan piksel lokal sekaligus statistik global. Diformulasikan sebagai:
   $$E_\phi = \frac{1}{H \times W} \sum_{x=1}^{H} \sum_{y=1}^{W} \phi(S(x,y), G(x,y))$$
   di mana $\phi$ adalah matriks keselarasan korelasi spasial.
3. **F-measure ($F_\beta$):** Rata-rata harmonik berbobot presisi (*precision*) dan sensitivitas (*recall*):
   $$F_\beta = \frac{(1 + \beta^2) \cdot Precision \cdot Recall}{\beta^2 \cdot Precision + Recall}$$
   dengan $\beta^2 = 0,3$ untuk memprioritaskan presisi.
4. **Mean Absolute Error ($MAE$ / $M$):** Menghitung kesalahan absolut rata-rata di seluruh piksel antara $S$ kontinu dan $G$ biner:
   $$MAE = \frac{1}{H \times W} \sum_{x=1}^{H} \sum_{y=1}^{W} |S(x,y) - G(x,y)|$$

## Eksperimen dan Hasil
Eksperimen dalam survei ini merupakan kompilasi dan standardisasi evaluasi lintas-model menggunakan kode evaluasi terbuka penulis. Zhou dkk. mengevaluasi 24 model representatif (9 tradisional, 15 deep learning) pada dataset RGB-D SOD utama seperti NJU2K (1.985 citra), NLPR (700 citra), DES (135 citra), SSD (80 citra), SIP (929 citra), dan DUT-RGBD (1.200 citra).

Hasil pengujian membuktikan keunggulan mutlak model berbasis pembelajaran mendalam dibandingkan metode tradisional. Pada dataset NJU2K, metode tradisional seperti DCMC (2016) hanya menghasilkan nilai $S_\alpha$ sebesar $0,686$ dengan MAE $0,172$. Sebaliknya, model fusi tengah berbasis deep learning seperti CPFP (2019) mencapai $S_\alpha$ $0,879$ dan MAE $0,053$. Model dengan atensi lintas-modal dan pemurnian kedalaman seperti JL-DCF (2020) mencatatkan performa terbaik dengan $S_\alpha$ $0,903$ dan MAE $0,043$.

Hasil ini menegaskan bahwa fusi tengah (*middle fusion*) adalah pendekatan paling konsisten karena dapat mengekstrak fitur kaya dari tiap modalitas secara terpisah sebelum menggabungkannya secara selektif. Fusi awal (*early fusion*) terbukti gagal menangkap korelasi tingkat tinggi, sedangkan fusi akhir (*late fusion*) kehilangan hubungan spasial halus. Selain itu, model dengan modul pemurni kedalaman (seperti D3Net) menunjukkan ketahanan lebih baik pada dataset dengan kedalaman bernoda (*noisy depth*), seperti dataset SIP (citra manusia luar ruangan dengan latar belakang kompleks).

## Kelebihan dan Keterbatasan
**Kelebihan:**
Makalah ini berhasil menyajikan taksonomi fusi multimodal (awal, tengah, akhir) yang terstruktur dan kini menjadi acuan kanonik dalam literatur visi komputer. Penyediaan repositori kode evaluasi terstandarisasi sangat membantu mengatasi masalah ketidakkonsistenan pengujian lintas-model akibat perbedaan pra-pemrosesan data atau implementasi metrik. Ulasan tentang *light field* SOD juga memperluas cakrawala riset mengenai alternatif representasi kedalaman.

**Keterbatasan:**
Secara konseptual, survei ini membatasi fokus pada tugas SOD dan kurang mengaitkannya dengan tugas estimasi kedalaman monokuler (*monocular depth estimation*) atau segmentasi semantik RGB-D. Secara rekayasa, karena terbit pada 2021, tulisan ini belum mencakup model berbasis *Transformer* (seperti Vision Transformer / ViT) yang mendominasi sejak akhir 2021. Terakhir, analisis efisiensi komputasi (seperti parameter, FLOPs, dan latensi FPS) kurang mendalam dibandingkan analisis akurasi metrik, sehingga menyulitkan praktisi yang ingin mengimplementasikan model pada perangkat tertanam (*embedded devices*) atau sistem waktu-nyata.

## Kaitan dengan Bab Lain
Bab ini memiliki posisi sentral dalam klaster **Fusi Multimodal** karena mengkategorikan pendekatan fusi sensor dan visual. Bab ini mewarisi landasan pemrosesan fitur dari bab dasar seperti [147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md), yang arsitekturnya banyak digunakan sebagai tulang punggung (*backbone*) model RGB-D SOD. Selain itu, modul perhatian (*attention*) pada fusi tengah erat kaitannya dengan mekanisme atensi kanal-spasial pada [149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md).

Dalam hal metodologi survei, bab ini melengkapi [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md) dan [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md) dengan mempersempit fokus pada representasi spasial 2.5D (RGB-D). Ulasan dataset di sini dapat dibaca secara paralel dengan [154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md) yang mengulas dataset RGB-D dalam robotika. Terakhir, perkembangan historis deteksi objek secara umum dapat divalidasi pada [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md).

## Poin untuk Sitasi
- **Kunci BibTeX:** `zhou2021rgbdsurvey`
- **Ringkasan untuk Sitasi:**
  > Survei oleh Zhou dkk. (2021) menyajikan taksonomi komprehensif bagi metode deteksi objek menonjol berbasis RGB-D (RGB-D SOD), yang mengklasifikasikan strategi fusi multimodal menjadi early, middle, dan late fusion. Melalui evaluasi terstandarisasi terhadap 24 model representatif pada dataset benchmark (seperti NJU2K, NLPR, dan SIP) menggunakan metrik seperti S-measure dan MAE, studi ini menegaskan keunggulan middle fusion yang memanfaatkan atensi lintas-modal untuk menangkap interaksi spasial-geometris.
- **Catatan Verifikasi:**
  Angka performa spesifik model (seperti nilai metrik JL-DCF atau BBS-Net pada dataset NJU2K/NLPR) harus selalu dikonfirmasi dengan repositori resmi penulis (*taozh2017/RGBD-SODsurvey*) atau naskah asli model bersangkutan karena variasi kecil pada pustaka evaluasi PyTorch/MATLAB dapat menghasilkan perbedaan desimal tipis.
