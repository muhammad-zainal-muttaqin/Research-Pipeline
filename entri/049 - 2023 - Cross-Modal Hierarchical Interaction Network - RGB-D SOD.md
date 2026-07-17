# 049 - Cross-Modal Hierarchical Interaction Network for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2023cmhi` |
| Judul asli | Cross-modal Hierarchical Interaction Network for RGB-D Salient Object Detection |
| Penulis | Hongbo Bi, Ranwan Wu, Ziqi Liu, Huihui Zhu, Cong Zhang, Tian-Zhu Xiang |
| Tahun | 2023 (daring 2022; volume 136, April 2023) |
| Venue | Pattern Recognition, vol. 136, artikel 109194 |
| Tema | RGB-D SOD |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1016/j.patcog.2022.109194
- **ScienceDirect (PII):** https://www.sciencedirect.com/science/article/pii/S0031320322006732
- **Kode resmi (dirilis penulis):** https://github.com/RanwanWu/HINet
- **Google Scholar:** https://scholar.google.com/scholar?q=Cross-Modal%20Hierarchical%20Interaction%20Network%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Cross-Modal%20Hierarchical%20Interaction%20Network%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini mengusulkan HINet, jaringan deteksi objek salien RGB-D yang memadukan modalitas warna (RGB) dan kedalaman (*depth*) melalui interaksi yang disusun berjenjang mengikuti hierarki fitur. Deteksi objek salien (*salient object detection*, SOD) adalah tugas menghasilkan peta saliensi, yaitu citra keabuan yang tiap pikselnya menyatakan seberapa menonjol piksel itu sebagai bagian objek yang paling menarik perhatian. Pada varian RGB-D, masukan berupa citra warna dan peta kedalaman, yaitu citra satu kanal yang tiap pikselnya berisi perkiraan jarak ke kamera. Alih-alih menggabungkan kedua modalitas sekali pada satu titik, HINet memasang modul pertukaran informasi lintas-modal (CIE) pada lima tahap ekstraksi fitur, lalu menggabungkan hasilnya secara bertingkat: fitur level tinggi yang kaya semantik lebih dahulu difusikan menjadi peta atensi, dan peta atensi itu kemudian memandu fusi fitur level rendah yang kaya detail tepi.

Model dilatih *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah) di atas dua *backbone* ResNet-50 dan diuji pada lima tolok ukur RGB-D standar. Pada NJU2K, HINet mencapai S-*measure* 0,915, unggul atas sembilan pembanding yang dipublikasikan sebelumnya; pada LFSD, galat MAE turun menjadi 0,076 dari 0,087 milik pembanding terbaik. Kode, bobot terlatih, dan peta hasil dirilis penulis secara terbuka.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Citra warna menyimpan tekstur dan rupa objek, tetapi lemah pada adegan dengan latar yang mirip warna objek, pencahayaan buruk, atau objek tembus cahaya. Peta kedalaman menyimpan struktur geometri yang tidak peka terhadap warna, sehingga kedua modalitas bersifat komplementer: menggabungkannya terbukti menaikkan akurasi SOD, seperti ditunjukkan DMRA (bab 035) yang membuang sebagian peta kedalaman buruk dan mengalihkan fokus ke modalitas RGB.

Persoalannya adalah *cara* menggabungkan. Pendekatan awal memakai fusi dini (menyambung RGB dan kedalaman sebagai masukan), fusi akhir (menggabungkan peta hasil dua jaringan), atau fusi satu level pada fitur tengah. Ketiganya mengabaikan fakta bahwa fitur CNN (*convolutional neural network*, jaringan saraf konvolusi) tersusun berjenjang: level rendah menyimpan tepi dan tekstur beresolusi tinggi, sedangkan level tinggi menyimpan makna objek beresolusi rendah. Menukar informasi RGB dan kedalaman hanya pada satu level berarti memaksakan satu jenis interaksi untuk dua kebutuhan berbeda — detail tepi memerlukan dukungan geometri lokal, sedangkan penentuan batas objek memerlukan kesepakatan semantik antarmodalitas. Metode seperti BBS-Net (bab 036) dan D3Net (bab 037) mulai memanfaatkan beberapa level fitur, tetapi pertukaran lintas-modal yang eksplisit di setiap level, dengan agregasi yang menghubungkan level tinggi ke level rendah, belum dirumuskan. HINet mengisi celah ini.

## Ide Utama

Gagasan inti HINet terdiri atas dua prinsip. Pertama, **pertukaran di mana-mana**: pada setiap tahap ekstraksi fitur, kedua modalitas saling menambahkan informasi melalui modul CIE, sehingga setiap level memperoleh versi fitur yang sudah memuat informasi modalitas pasangannya. Kedua, **fusi terpandu dari atas ke bawah**: fitur hasil pertukaran tidak digabung sekaligus, melainkan dikelompokkan menjadi level tinggi dan level rendah; level tinggi difusikan lebih dahulu menjadi peta atensi kasar, dan atensi ini dipakai sebagai pengali pembimbing saat level rendah difusikan. Dengan cara ini, lokasi objek yang disepakati kedua modalitas pada level semantik menentukan bagian tepi mana pada level detail yang diperkuat.

## Cara Kerja Langkah demi Langkah

### Encoder Dua Arus

Masukan berupa citra RGB 352×352×3 dan peta kedalaman 352×352×1. Keduanya diproses oleh dua ResNet-50 terpisah — ResNet-50 adalah jaringan konvolusi 50 lapis dengan sambungan residual (keluaran lapis ditambah masukannya) yang menjadi model ekstraksi fitur standar; bobot awalnya berasal dari pelatihan klasifikasi pada ImageNet (dataset klasifikasi citra berskala besar). Setiap arus menghasilkan lima tahap fitur: 88×88 dengan 64 kanal, 88×88 dengan 256 kanal, 44×44 dengan 512 kanal, 22×22 dengan 1.024 kanal, dan 11×11 dengan 2.048 kanal. Kanal adalah dimensi fitur per piksel; semakin dalam tahapnya, resolusi spasial mengecil tetapi isi tiap kanal semakin abstrak.

### Modul Pertukaran Informasi Lintas-Modal (CIE)

Modul CIE (*cross-modal information exchange*) dipasang di kelima titik pertemuan tahap. Untuk sepasang fitur RGB dan kedalaman berukuran sama, misalnya 88×88×64 pada tahap pertama, langkahnya: (1) kedua fitur dikalikan per elemen (*element-wise multiplication*) — perkalian ini hanya menyisakan respons yang kuat di kedua modalitas, sehingga berperan sebagai penyaring kesepakatan; (2) hasilnya dilewatkan ke konvolusi 3×3, *batch normalization* (normalisasi statistik per kanal untuk menstabilkan pelatihan), dan aktivasi ReLU (fungsi max(0, x)); (3) sinyal bersama ini ditambahkan secara residual kembali ke fitur RGB dan fitur kedalaman, sehingga masing-masing arus menerima informasi modalitas pasangannya tanpa kehilangan isinya sendiri; (4) di antaranya dipakai perataan *upsampling* bilinear diikuti *max-pooling* 2×2 yang mempertahankan resolusi tetapi menghaluskan derau terisolasi. Keluaran CIE berupa fitur gabungan per level (f1 sampai f5) yang diteruskan ke dekoder, sementara kedua arus melanjutkan ekstraksi dengan fitur yang sudah dipertukarkan.

### Modul Konvolusi Multi-Skala (MC)

Sebelum difusikan, setiap fitur gabungan dilewatkan ke modul MC yang merangkum konteks beberapa ukuran wilayah. Modul ini memiliki empat cabang paralel: satu cabang konvolusi 1×1 polos, dan tiga cabang dengan konvolusi melebar (*dilated convolution* — konvolusi yang titik-titik tapisnya direnggangkan sehingga menangkap wilayah lebih luas tanpa menambah parameter) dengan laju pelebaran 3, 5, dan 7, didahului konvolusi asimetris 1×k dan k×1 untuk menekan biaya. Keluaran keempat cabang disambung lalu dipadatkan menjadi 32 kanal. Hasilnya, fitur pada setiap level memuat konteks lokal sekaligus konteks berjangkauan luas.

### Fusi Hierarkis Terpandu (PGF)

Tahap inilah yang disebut makalah sebagai *progressively guided fusion* (PGF). Alurnya ditunjukkan diagram berikut:

```
  RGB 352x352x3 ──► ResNet-50 RGB    (5 tahap: 64/256/512/1024/2048 kanal)
                          │ CIE ×5  (pertukaran lintas-modal per tahap)
  Depth 352x352x1 ──► ResNet-50 Depth
                          │
        f1(88x88) f2(88x88) f3(44x44) f4(22x22) f5(11x11)
          │         │         └────┬─────┴────┐
          │         │             MC ──► MC ──► MC
          │         │                  HFF level tinggi
          │         │                  peta atensi M_hl (32 kanal, 44x44)
          │         │                       │ panduan balik:
          │         ▼                       ▼ sigmoid, pengali residual
          └───► MC ──► MC ◄──── diperkuat atensi
                       HFF level rendah ──► dekoder dekonvolusi
                                              │
   keluaran: M_hl (disupervisi)   peta saliensi akhir M_ll (disupervisi)
```

Fitur level tinggi (f3, f4, f5) difusikan oleh blok HFF (*hierarchical feature fusion*): fitur teratas dinaikkan resolusinya, disambung dengan level di bawahnya, diproses konvolusi, lalu dikalikan per elemen dengan fitur teratas tadi — perkalian ini membuat level atas berperan sebagai pengali selektif yang memilih isi level bawah. Proses berulang sampai menghasilkan peta atensi M_hl. Selanjutnya terjadi panduan balik: M_hl diaktivasi sigmoid (fungsi yang memetakan nilai ke rentang 0–1) dan dipakai memodulasi fitur level rendah (f1, f2, f3) dengan rumus x + x⊙sigmoid(atensi) — wilayah yang disepakati sebagai objek pada level semantik diperkuat pada level detail, wilayah lain dibiarkan. Fitur yang telah dipandu lalu difusikan oleh HFF level rendah dan diteruskan ke dekoder bertingkat berisi dekonvolusi (konvolusi transpos yang menaikkan resolusi) hingga menghasilkan peta saliensi akhir M_ll.

### Pelatihan

Kedua keluaran, M_hl dan M_ll, diawasi langsung terhadap *ground truth* (peta saliensi benar) dengan fungsi galat *binary cross-entropy* (BCE), dan total galat adalah jumlah keduanya — skema ini disebut supervisi dalam (*deep supervision*) karena keluaran perantara ikut dilatih. Optimisasi memakai Adam (algoritme pembaruan bobot adaptif berbasis gradien) dengan laju pembelajaran 10⁻⁴, ukuran *batch* 7, 200 epoch (satu epoch berarti satu putaran penuh atas data latih), peluruhan laju 0,1 setiap 60 epoch, dan pemotongan gradien 0,5. Data latih mengikuti protokol standar bidang ini: gabungan bagian latih NJU2K dan NLPR.

## Eksperimen dan Hasil

Evaluasi memakai lima tolok ukur: NJU2K (±1.985 pasang citra stereo), NLPR (1.000 pasang RGB–kedalaman dari Kinect), STERE (1.000 citra stereo dari internet), SSD (80 citra stereo), dan LFSD (100 citra *light field*). Empat metrik dipakai: S-*measure* (kesesuaian struktur peta prediksi dengan kebenaran; maksimal 1), F-*measure* maksimum (rata-rata harmonik presisi — proporsi piksel prediksi yang benar — dan recall — proporsi piksel benar yang terdeteksi — pada ambang terbaik), E-*measure* maksimum (kesesajajaran gabungan tingkat piksel dan tingkat citra), dan MAE (*mean absolute error*, rata-rata selisih mutlak per piksel; semakin kecil semakin baik). Pembandingnya sembilan metode: DMRA, CPFP, S2MA, DCMF, cmSalGAN, DRLF, MCMFNet, CMF, dan D3Net.

Hasil utama HINet (S/F/E/MAE): NJU2K 0,915/0,914/0,945/0,039; NLPR 0,922/0,906/0,957/0,026; SSD 0,865/0,852/0,916/0,049; STERE 0,892/0,883/0,933/0,049; LFSD 0,852/0,847/0,888/0,076. Interpretasinya: pada NJU2K, S-*measure* 0,915 melampaui pembanding terbaik cmSalGAN (0,903) dengan selisih 1,2 poin — peningkatan nyata pada metrik yang sudah jenuh di atas 0,9. Pada LFSD, MAE 0,076 berarti galat rata-rata turun 12,6% relatif terhadap 0,087 milik pembanding terbaik; LFSD dikenal sulit karena kedalamannya berasal dari kamera *light field*. Pada NLPR, selisihnya tipis (0,922 lawan 0,921), menandakan dataset itu mendekati titik jenuh. Secara keseluruhan HINet menjadi terbaik pada mayoritas baris metrik di kelima dataset.

Sebagai konteks lanjutan, tabel perbandingan pada karya-karya sesudahnya (misalnya SwinNet berbasis *transformer*, arsitektur berbasis mekanisme atensi) melaporkan S-*measure* NJU2K sekitar 0,935; posisi HINet kini berada di bawah generasi yang lebih baru.

## Kelebihan dan Keterbatasan

Kelebihan: (1) pertukaran lintas-modal terjadi di semua level, bukan satu titik, sehingga detail dan semantik sama-sama dipertukarkan; (2) mekanisme panduan balik membuat fusi level rendah selektif terhadap lokasi objek, bukan sekadar penjumlahan fitur; (3) desainnya sederhana — hanya konvolusi, perkalian, dan penjumlahan — sehingga mudah direproduksi, terbukti dari kode resmi yang lengkap; (4) unggul konsisten terhadap sembilan pembanding pada masanya.

Keterbatasan: (1) dua ResNet-50 penuh menjadikan model besar; dari sisi rekayasa, biaya parameter dan komputasinya berat untuk perangkat terbatas; (2) perkalian lintas-modal pada CIE mengandalkan kesepakatan kedua modalitas — secara konseptual, bila peta kedalaman rusak total pada suatu objek, respons bersama bisa ikut hilang dan tambahan informasi menjadi lemah; (3) panduan balik bersifat satu arah (tinggi ke rendah), sehingga kesalahan lokalisasi pada peta atensi level tinggi merambat ke fusi level rendah; (4) evaluasi terbatas pada lima dataset dengan protokol latih konvensional, tanpa pengujian lintas-dataset untuk mengukur generalisasi. Keterbatasan (1)–(3) merupakan analisis penulis bab, bukan pernyataan penulis makalah.

## Kaitan dengan Bab Lain

HINet melanjutkan garis fusi RGB-D yang dibuka DMRA (bab [035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) dengan pertanyaan berbeda: bukan lagi bagaimana menyaring kedalaman buruk, melainkan bagaimana menyusun pertukaran antarmodalitas. Dibandingkan BBS-Net (bab [036](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)) yang memadukan fitur multi-level dua arus, HINet menambahkan pertukaran eksplisit per level dan atensi terpandu. D3Net (bab [037](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)) hadir dalam tabel pembandingnya, sedangkan S2MA (bab [039](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)) mewakili jalur pembelajaran bersama dua modalitas yang menjadi alternatif desainnya. Generasi sesudahnya beralih ke *transformer*, misalnya VST (bab [042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)), dan dalam literatur pasca-2023 nama HINet rutin muncul sebagai baseline CNN kuat yang harus dilampaui.

## Poin untuk Sitasi

Kutip dengan kunci `chen2023cmhi`. Ringkasan yang aman dikutip: "HINet (Bi dkk., Pattern Recognition 2023) memadukan RGB dan kedalaman melalui modul pertukaran informasi lintas-modal pada setiap level hierarki fitur, lalu menggabungkan hasilnya secara bertingkat dengan fusi terpandu progresif, sehingga mencapai S-*measure* 0,915 pada NJU2K dan MAE 0,076 pada LFSD." Catatan verifikasi sebelum sitasi formal: (1) metadata lama dan `references.bib` menulis nama "Bi, Hangbo" dan "Wu, Ruimin", padahal Crossref, Semantic Scholar, dan repositori resmi menyebut "Hongbo Bi" dan "Ranwan Wu" — nama pada berkas bib perlu diperbaiki; (2) angka hasil di atas disalin dari tabel kuantitatif pada repositori resmi penulis dan cocok dengan tabel ulangan di dua makalah pihak ketiga, tetapi tetap perlu dicocokkan dengan naskah penerbit; (3) rincian studi ablasi, jumlah parameter, serta hasil pada dataset SIP dan DES yang dikutip karya lain tidak sempat diverifikasi dari naskah asli dalam penulisan bab ini.
