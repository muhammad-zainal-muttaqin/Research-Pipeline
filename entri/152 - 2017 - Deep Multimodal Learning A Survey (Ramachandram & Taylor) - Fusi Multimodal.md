# 152 - Deep Multimodal Learning: A Survey on Recent Advances and Trends

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ramachandram2017multimodalreview` |
| Judul asli | Deep Multimodal Learning: A Survey on Recent Advances and Trends |
| Penulis | Ramachandram, Dhanesh; Taylor, Graham W. |
| Tahun | 2017 |
| Venue | IEEE Signal Processing Magazine |
| Tema | Fusi Multimodal |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Multimodal%20Learning%3A%20A%20Survey%20on%20Recent%20Advances%20and%20Trends
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deep%20Multimodal%20Learning%3A%20A%20Survey%20on%20Recent%20Advances%20and%20Trends&sort=relevance

## Gambaran Umum
*Deep multimodal learning* atau pembelajaran multimodal mendalam adalah bidang pembelajaran mesin yang menggunakan model jaringan saraf tiruan mendalam untuk mengintegrasikan informasi dari berbagai modalitas data yang berbeda (seperti citra, audio, teks, atau data sensor kedalaman). Makalah survei oleh Ramachandram dan Taylor (2017) menyajikan tinjauan menyeluruh terhadap perkembangan, arsitektur, dan tantangan metodologis dalam pembelajaran representasi multimodal mendalam. Masalah utama yang dibahas adalah bagaimana menjembatani perbedaan karakteristik statistik dan struktur data antar-modalitas—yang dikenal sebagai *heterogeneity gap*—melalui pemodelan jaringan saraf tiruan mendalam.

Makalah ini memberikan kontribusi berupa taksonomi formal yang membagi arsitektur representasi menjadi tiga tipe utama: representasi bersama (*joint representation*), representasi terkoordinasi (*coordinated representation*), dan model penyandi-penyandi balik (*encoder-decoder*). Hasil utama dari survei ini menunjukkan bahwa pemilihan strategi representasi dan tingkatan fusi harus didasarkan pada tingkat korelasi antar-modalitas serta kebutuhan ketahanan model terhadap hilangnya data sensor pada saat inferensi. Survei ini menjadi landasan teoretis yang sangat penting untuk memahami perkembangan fusi multimodal, khususnya pada domain visi komputer yang menggabungkan informasi warna (RGB) dengan informasi kedalaman (*depth*) atau spasial 3D.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum era pembelajaran mendalam, fusi multimodal bergantung pada rekayasa fitur rancangan tangan (*hand-crafted features*) dan model klasifikasi dangkal (*shallow fusion*) seperti *Support Vector Machine* (SVM). Metode ini gagal menjembatani kesenjangan statistik antar-modalitas (*heterogeneity gap*), misalnya antara piksel citra kontinu dan kata teks diskret. Fusi tingkat awal pada fitur mentah tersebut tidak dapat menangkap interaksi non-linear yang kompleks.

Kekurangan lain pendekatan lama adalah ketidakmampuan menangani data yang tidak lengkap atau kegagalan sensor (*missing modality*) saat inferensi. Desain arsitektur fusi juga bersifat coba-coba (*ad hoc*) tanpa klasifikasi konseptual yang jelas tentang di mana fusi harus dilakukan (fitur mentah, representasi menengah, atau keputusan akhir). Ketiadaan panduan sistematis ini menghambat pengembangan sistem persepsi kokoh untuk aplikasi sensor heterogen, termasuk fusi RGB-D yang menyelaraskan data warna dan kedalaman.

## Ide Utama
Gagasan inti dari makalah survei ini adalah merumuskan taksonomi terpadu untuk pembelajaran representasi multimodal mendalam guna mempermudah perancangan sistem fusi yang efisien dan tangguh. Penulis mengusulkan bahwa integrasi data heterogen dapat diselesaikan secara sistematis dengan memetakan fitur modalitas ke dalam ruang laten (*latent space*) bersama yang dipelajari secara *end-to-end*. Jaringan saraf mendalam dimanfaatkan untuk mengekstraksi fitur tingkat tinggi (*high-level features*) secara hierarkis sebelum fusi dilakukan.

Ide ini diwujudkan melalui pembagian taksonomi arsitektur menjadi tiga kategori representasi: *joint representation* yang menyatukan fitur ke dalam satu ruang laten bersama; *coordinated representation* yang melatih penyandi terpisah dengan pembatas korelasi; dan *encoder-decoder* yang memetakan satu modalitas untuk merekonstruksi modalitas lainnya. Konsep tingkatan fusi (*early*, *intermediate*, dan *late fusion*) serta teknik regularisasi seperti *multimodal dropout* diperkenalkan untuk menjamin ketahanan sistem saat menghadapi modalitas yang hilang.

## Cara Kerja Langkah demi Langkah
Berikut ini adalah penjelasan rinci mengenai komponen taksonomi dan mekanisme kerja pembelajaran multimodal mendalam yang diulas dalam survei ini.

### Taksonomi Pembelajaran Representasi
Representasi menentukan bagaimana data dari berbagai modalitas dipetakan dan dikelola di dalam ruang laten jaringan:

```
  [ Joint Representation ]             [ Coordinated Representation ]

Modalitas A      Modalitas B          Modalitas A        Modalitas B
 (Citra X)        (Audio Y)            (Citra X)          (Audio Y)
     │                │                    │                  │
  [Enc A]          [Enc B]              [Enc A]            [Enc B]
     │                │                    │                  │
     ▼                ▼                    ▼                  ▼
   f_A(X)           f_B(Y)               f_A(X)             f_B(Y)
     └───────┬────────┘                    │                  │
             ▼                             │  [Koordinasi]    │
     [ Ruang Latent ]                      ├──────────────────┤
     [ Shared Latent]                      │   (DCCA/Jembatan)│
             │                             ▼                  ▼
             ▼                        Output A           Output B
         Output Z                     (Terpisah tetapi Terkorelasi)
```

*   **Representasi Bersama (Joint Representation):**
    Secara matematis, untuk modalitas masukan $x_a$ (citra) dan $x_b$ (teks), model mempelajari proyeksi $f_a(x_a)$ dan $f_b(x_b)$ menggunakan jaringan spesifik-modalitas. Hasil proyeksi digabungkan (konkatenasi atau perkalian tensor) dan diteruskan ke lapisan bersama:
    $$h = \sigma(W_a f_a(x_a) + W_b f_b(x_b) + b)$$
    di mana $W$ adalah matriks bobot dan $\sigma$ adalah fungsi aktivasi non-linear. Cara ini efisien jika seluruh modalitas tersedia lengkap pada saat pelatihan dan inferensi.
*   **Representasi Terkoordinasi (Coordinated Representation):**
    Model mempelajari ruang laten terpisah $h_a = f_a(x_a)$ dan $h_b = f_b(x_b)$, namun menerapkan fungsi kerugian (*loss function*) untuk meminimalkan jarak atau memaksimalkan korelasi antarkeduanya. Contohnya adalah *Deep Canonical Correlation Analysis* (DCCA) yang memaksimalkan korelasi linier hasil proyeksi non-linear kedua modalitas.
*   **Model Penyandi-Penyandi Balik (Encoder-Decoder):**
    Digunakan untuk penerjemahan antar-modalitas. Penyandi memetakan modalitas sumber $x_a$ menjadi representasi laten $h_a$, yang kemudian menjadi kondisi bagi penyandi balik untuk menghasilkan modalitas target $\hat{x}_b$ (misalnya dalam tugas pembuatan deskripsi citra).

### Tingkatan Fusi Multimodal
Tingkatan fusi didefinisikan berdasarkan letak penggabungan fitur di dalam hierarki jaringan saraf mendalam:

```
1. Early Fusion (Fusi Awal)
Modalitas A ──┐
              ├─► [ Fusi Fitur ] ─► [ Ekstrator Fitur ] ─► [ Prediktor ] ─► Hasil
Modalitas B ──┘

2. Late Fusion (Fusi Akhir)
Modalitas A ──► [ Model A ] ──► Prediksi A ──┐
                                             ├─► [ Fusi Keputusan ] ─► Hasil
Modalitas B ──► [ Model B ] ──► Prediksi B ──┘

3. Intermediate Fusion (Fusi Menengah / Mendalam)
Modalitas A ──► [ Blok A1 ] ──► Fitur A1 ──┐
                                           ├─► [ Fusi Menengah ] ──► [ Blok C ] ──► Hasil
Modalitas B ──► [ Blok B1 ] ──► Fitur B1 ──┘
```

*   **Fusi Awal (Early Fusion):**
    Konkatenasi fitur dilakukan langsung pada tingkat masukan atau lapisan awal jaringan. Hal ini memungkinkan model mempelajari hubungan antar-modalitas sejak awal, namun rentan terhadap pembengkakan dimensi (*curse of dimensionality*).
*   **Fusi Akhir (Late Fusion):**
    Masing-masing modalitas diproses secara terpisah hingga keputusan akhir (seperti nilai probabilitas kelas), yang kemudian digabungkan melalui voting, rata-rata, atau model klasifikasi sekunder (*meta-classifier*). Fusi ini toleran terhadap kegagalan salah satu sensor, namun tidak mampu menangkap korelasi tingkat rendah antar-fitur.
*   **Fusi Menengah/Mendalam (Intermediate/Deep Fusion):**
    Modalitas dilewatkan pada lapisan ekstraksi terpisah sebelum representasi tersembunyinya digabungkan pada tingkat menengah. Model dapat mempelajari interaksi fitur pada berbagai skala abstraksi secara bertahap.

### Arsitektur Jaringan untuk Fusi Mendalam
Beberapa model mendalam digunakan untuk mengimplementasikan taksonomi representasi tersebut:
*   **Deep Boltzmann Machines (DBM) Multimodal:**
    Model generatif tak terarah yang menggunakan *Restricted Boltzmann Machine* (RBM) terpisah di lapisan bawah untuk memodelkan distribusi data masing-masing modalitas (misalnya citra kontinu dan teks diskret) sebelum dihubungkan ke lapisan laten bersama di atas. Sifat probabilistiknya memungkinkan pengisian nilai modalitas yang hilang melalui penarikan sampel (*sampling*).
*   **Multimodal Autoencoders (MAE):**
    Jaringan tak diawasi yang memetakan masukan multimodal ke ruang laten bersama, lalu merekonstruksi kembali seluruh masukan asli. Struktur ini dapat merekonstruksi modalitas yang hilang dari informasi modalitas yang tersisa.
*   **Jaringan Hibrida CNN-RNN:**
    Menggabungkan CNN untuk fitur spasial citra dan RNN untuk data temporal/teks, diintegrasikan melalui lapisan fusi menengah atau mekanisme perhatian (*attention*).

### Strategi Pembelajaran dan Regularisasi
*   **Multimodal Dropout:**
    Teknik yang menonaktifkan seluruh jalur satu modalitas secara acak selama pelatihan untuk mencegah ketergantungan dominan pada satu modalitas dan meningkatkan ketahanan terhadap data sensor yang hilang saat pengujian.
*   **Pembelajaran Bersama (Co-learning):**
    Transfer pengetahuan dari modalitas kaya data/label ke modalitas miskin data melalui penyelarasan manifold atau regularisasi ruang laten.

## Eksperimen dan Hasil
Makalah survei ini mengulas kinerja berbagai metode fusi mendalam pada tugas-tugas penanda seperti pengenalan suara visual (*Audio-Visual Speech Recognition* / AVSR) dan klasifikasi citra-teks.

Pada tugas AVSR dengan dataset CUAVE, penggunaan model berbasis *Multimodal Deep Boltzmann Machine* (DBM) terbukti menurunkan tingkat kesalahan pengenalan kata (*Word Error Rate* / WER) secara drastis dibandingkan fusi dangkal. Saat tingkat derau (*noise*) audio ditingkatkan ke $0\text{ dB}$, model fusi mendalam mempertahankan akurasi di atas $80\%$, sedangkan model fusi awal dangkal menurun hingga di bawah $50\%$.

Pada dataset klasifikasi citra-teks seperti MIRFLICKR-25000 dan IAPR TC-12, arsitektur *Multimodal Autoencoder* (MAE) tak diawasi mampu menghasilkan representasi bersama yang unggul untuk pencarian lintas modalitas. Nilai *Mean Average Precision* (mAP) yang diperoleh MAE melampaui metode linier tradisional seperti *Canonical Correlation Analysis* (CCA) sebesar lebih dari $15\%$, menunjukkan keunggulan pemodelan hubungan non-linear mendalam dalam menjembatani kesenjangan semantik.

## Kelebihan dan Keterbatasan
Secara konseptual, kelebihan utama survei ini adalah perumusan taksonomi terstruktur yang mampu menyatukan keragaman metode fusi mendalam. Penulis juga memberikan analisis jujur mengenai aspek rekayasa praktis, termasuk penanganan kehilangan modalitas (*missing modality*) melalui pemodelan generatif dan teknik regularisasi seperti *multimodal dropout*.

Namun, secara rekayasa, survei tahun 2017 ini memiliki keterbatasan karena belum mengantisipasi dominasi arsitektur Transformer dan mekanisme perhatian mandiri (*self-attention*) skala besar yang mendominasi setelah tahun 2020. Akibatnya, pembahasan fusi didominasi oleh DBM, Autoencoder konvensional, dan kombinasi CNN-RNN. Keterbatasan lainnya adalah kurangnya ulasan sinkronisasi spasial-temporal rapat pada resolusi tinggi, yang krusial untuk fusi piksel demi piksel pada deteksi objek RGB-D modern. Analisis efisiensi komputasi (seperti FLOPs dan latensi inferensi) juga kurang dibahas secara mendalam.

## Kaitan dengan Bab Lain
Konsep representasi hierarkis dalam survei ini sangat bergantung pada arsitektur ekstraksi fitur dasar. Sebagai contoh, ekstraksi fitur spasial citra 2D sering menggunakan jaringan ResNet (bab [ResNet](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)) sebagai tulang punggung (*backbone*) sebelum fiturnya digabungkan. Pada data 3D, representasi titik spasial diproses menggunakan PointNet (bab [PointNet](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)) sebelum diselaraskan dengan fitur warna RGB. Mekanisme penimbangan fitur secara dinamis pada fusi menengah juga relevan dengan modul perhatian seperti CBAM (bab [CBAM](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)).

Taksonomi Ramachandram dan Taylor ini mendasari survei-survei fusi modern setelahnya, seperti survei deteksi dan segmentasi multimodal oleh Feng dkk. (bab [Feng dkk.](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)) serta ulasan perkembangan deteksi objek dua dekade oleh Zou dkk. (bab [Zou dkk.](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)). Konsep fusi sensor ini juga meluas ke deteksi objek menonjol RGB-D oleh Zhou dkk. (bab [Zhou dkk.](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)) dan analisis dataset RGB-D oleh Lopes dkk. (bab [Lopes dkk.](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)) yang mengeksplorasi sensor *depth* untuk informasi spasial 3D.

## Poin untuk Sitasi
- Kunci BibTeX: `ramachandram2017multimodalreview`
- Ringkasan Sitasi:
  "Ramachandram dan Taylor (2017) merumuskan taksonomi pembelajaran representasi multimodal mendalam yang membagi model menjadi representasi bersama (*joint*), terkoordinasi (*coordinated*), dan penyandi-penyandi balik (*encoder-decoder*). Survei ini menguraikan bagaimana pemodelan non-linear mendalam menjembatani kesenjangan statistik antar-modalitas (*heterogeneity gap*) melalui fusi tingkat menengah (*intermediate fusion*) dan teknik regularisasi seperti *multimodal dropout* untuk menangani modalitas yang hilang. Konsep-konsep tersebut menjadi landasan teoretis untuk pengembangan fusi sensor heterogen, termasuk integrasi RGB-D."
- Catatan verifikasi:
  Sebagai makalah survei, angka evaluasi (seperti WER pada CUAVE atau mAP pada MIRFLICKR) dikompilasi dari penelitian primer. Verifikasi ke naskah asli primer dianjurkan sebelum melakukan sitasi formal.
