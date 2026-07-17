# 044 - TriTransNet: RGB-D Salient Object Detection with a Triplet Transformer Embedding Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2021tritransnet` |
| Judul asli | TriTransNet: RGB-D Salient Object Detection with a Triplet Transformer Embedding Network |
| Penulis | Zhengyi Liu, Yuan Wang, Zhengzheng Tu, Yun Xiao, Bin Tang |
| Tahun | 2021 |
| Venue | Proceedings of the 29th ACM International Conference on Multimedia (ACM MM 2021), hal. 4481–4490 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2108.03990
- **DOI (versi penerbit):** https://doi.org/10.1145/3474085.3475601
- **Kode sumber:** https://github.com/liuzywen/TriTransNet
- **Google Scholar:** https://scholar.google.com/scholar?q=TriTransNet%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Triplet%20Transformer%20Embedding%20Network
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=TriTransNet%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Triplet%20Transformer%20Embedding%20Network&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan TriTransNet, jaringan untuk deteksi objek menonjol (*salient object detection*, SOD) pada citra RGB-D, yaitu pasangan citra warna dan peta kedalaman yang setiap pikselnya menyatakan jarak ke kamera. SOD adalah tugas prediksi padat tingkat piksel: jaringan menghasilkan peta keberadaan objek paling menonjol dalam satu adegan. Titik berangkatnya adalah temuan empiris bahwa pada kerangka U-Net — arsitektur enkoder-dekoder yang menurunkan resolusi citra menjadi fitur semantik lalu menaikkannya kembali — fitur tingkat tinggi memberi sumbangan terbesar terhadap kinerja, sedangkan agregasi ke fitur tingkat rendah cepat jenuh.

Kontribusi utamanya adalah modul penyisipan transformer kembar tiga (*triplet transformer embedding module*, TTEM): tiga encoder transformer standar dengan bobot yang dibagi bersama, masing-masing memperkuat satu dari tiga level fitur teratas dengan mempelajari ketergantungan jarak jauh antar-level. Modul ini disertai modul pemurnian kedalaman untuk fusi RGB-D dan decoder tiga aliran. Hasilnya, TriTransNet mencapai kinerja terbaik atau hampir terbaik pada hampir semua metrik di enam dataset tolok ukur RGB-D SOD.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2021, metode SOD berbasis CNN hampir seluruhnya memakai kerangka U-Net: konvolusi dan *pooling* berjenjang menghasilkan fitur multi-level, dari fitur tingkat rendah yang kaya detail spasial hingga fitur tingkat tinggi yang kaya makna semantik. Fitur-fitur ini saling melengkapi, tetapi penelitian Wu et al. (2019) yang dikutip makalah menunjukkan bahwa agregasi fitur dari level tinggi ke level rendah cepat jenuh: sumbangan terbesar justru datang dari fitur tingkat tinggi. Masalahnya, CNN membangun fitur level tinggi melalui tumpukan konvolusi lokal, sehingga ketergantungan jarak jauh — hubungan antara piksel yang berjauhan dalam citra — hanya tertangkap secara tidak langsung. Transformer, arsitektur berbasis perhatian-diri (*self-attention*) yang menghitung interaksi setiap pasang elemen secara eksplisit, mampu memodelkan ketergantungan semacam itu, tetapi biayanya yang kuadratik terhadap jumlah elemen membuatnya mahal pada peta fitur beresolusi besar.

Pada sisi modalitas, peta kedalaman menambahkan informasi susunan tiga dimensi yang membantu ketika warna objek dan latar mirip. Namun peta kedalaman dari sensor nyata sering berkualitas rendah dan bertindak sebagai derau; D3Net (bab 037) menanganinya dengan mekanisme gerbang yang menekan kedalaman buruk. TriTransNet menempati celah antara dua persoalan ini: memperkuat fitur multi-level dengan transformer secara efisien, sekaligus memanfaatkan kedalaman tanpa mewarisi deranya.

## Ide Utama

Gagasan inti TriTransNet dapat dinyatakan dalam dua kalimat. Pertama, terapkan transformer hanya pada tiga level fitur teratas — tempat resolusi spasial sudah kecil sehingga biaya perhatian-diri terjangkau — dan gunakan tiga encoder transformer yang **berbagi bobot yang sama**. Berbagi bobot masuk akal karena ketiga level tersebut adalah aspek berbeda dari citra masukan yang sama; satu set parameter yang identik memaksa transformer menemukan informasi bersama yang tersembunyi di seluruh level. Kedua, perlakukan kedalaman sebagai pelengkap, bukan mitra setara: fitur kedalaman disaring terlebih dahulu oleh perhatian kanal dan perhatian spasial yang dikondisikan oleh fitur warna, lalu dilampirkan ke fitur warna melalui koneksi residual. Dengan cara ini, informasi warna asli tetap terjaga dan kedalaman yang buruk tertekan sebelum sempat mencemari representasi.

## Cara Kerja Langkah demi Langkah

### Kerangka Keseluruhan

TriTransNet terdiri atas tiga bagian yang dilewati data secara berurutan: enkoder fusi multi-modal, modul pemercepat fitur, dan decoder tiga aliran. Enkoder memakai dua jaringan ResNet-50 — CNN 50 lapis dengan koneksi residual yang menjadi tulang punggung standar visi komputer — satu untuk citra warna dan satu untuk peta kedalaman. Setiap aliran menghasilkan lima level fitur (i = 1 sampai 5), dari resolusi besar hingga resolusi kecil. Skema aliran datanya:

```
citra RGB 256x256                peta kedalaman 256x256
      |                                |
      v                                v
+------------+                  +------------+
| ResNet-50  |                  | ResNet-50  |
| f1..f5     |                  | d1..d5     |
+--+---------+                  +--+---------+
   |        +----------------------+
   |        v DPM (per level i=1..5)
   v   F1..F5  fitur gabungan
        | F3,F4,F5 -> transisi conv 3x3 -> penyesuaian skala (UFM bertahap)
        v
   TTEM: 3 encoder transformer, bobot dibagi (L=12, D=768, N=1024)
        v
   konkatenasi (ZiL, Fi) per level
        v
   decoder 3 aliran, digabung F1,F2 -> S3, S4, S5 -> S_final (peta saliency)
```

Kedalaman tidak menjadi aliran bebas: fiturnya diserap ke fitur warna pada setiap level sebelum pemrosesan berikutnya.

### Modul Pemurnian Kedalaman (DPM)

Modul pemurnian kedalaman (*depth purification module*, DPM) bekerja pada setiap level i = 1 sampai 5, dengan masukan fitur warna f_i dan fitur kedalaman d_i pada level yang sama. Keduanya mula-mula digabung dengan konkatenasi diikuti konvolusi, lalu dilewatkan ke perhatian kanal (*channel attention*): mekanisme dari modul CBAM yang menghasilkan satu bobot per kanal, sehingga kanal kedalaman yang tidak informatif ditekan. Hasilnya diteruskan ke perhatian spasial (*spatial attention*), yang menghasilkan satu bobot per posisi piksel, sehingga wilayah kedalaman yang rusak juga tertekan. Fitur kedalaman yang telah dua kali disaring ini kemudian ditambahkan per elemen ke fitur warna asli melalui koneksi residual, mengikuti rumus F_i^r = d_i × SA(d_i × CA(Cat(d_i, f_i))) + f_i. Karena penambahannya residual, keluaran tetap memuat informasi warna utuh; kedalaman hanya mengoreksi, bukan menggantikan.

### Penyesuaian Skala

Encoder transformer menuntut masukan seragam, sedangkan F3, F4, F5 berbeda resolusi dan jumlah kanalnya. Dua tahap menyelaraskannya. Tahap pertama adalah lapis transisi: konvolusi 3×3 diikuti aktivasi ReLU yang menyamakan jumlah kanal ketiga level. Tahap kedua adalah modul fusi *upsampling* bertahap: fitur level yang lebih dalam dinaikkan resolusinya dua kali lipat, dikonvolusi, lalu dikonkatenasi dengan fitur level di bawahnya, dan proses ini diulang sampai semua level mencapai resolusi level 3. Jadi F5 dinaikkan dan digabung ke F4, hasilnya dinaikkan lagi dan digabung ke F3. Penaikan bertahap dipilih karena penaikan langsung dua atau empat kali lipat menimbulkan derau, sedangkan fusi per langkah menambah detail spasial pada fitur level dalam.

### Modul Penyisipan Transformer Kembar Tiga (TTEM)

Ketiga fitur yang telah seragam ukurannya diubah menjadi barisan *token*: peta fitur dipotong menjadi N = 1024 *patch*, setiap patch diratakan menjadi vektor dan diproyeksikan linier ke ruang penyisipan berdimensi D = 768, kemudian ditambah penyisipan posisi (*positional embedding*) yang dipelajari agar informasi letak tidak hilang. Setiap barisan masuk ke encoder transformer standar sebanyak L = 12 lapis; setiap lapis terdiri atas perhatian-diri multi-kepala dan perceptron multi-lapis, masing-masing didahului normalisasi lapis dan diikuti koneksi residual. Ketiga encoder ini arsitekturnya identik dan bobotnya dibagi penuh: satu set parameter yang sama memroses tiga barisan secara paralel — berbeda dengan VT-FPN yang memakai satu transformer untuk semua level — sehingga informasi semantik level tinggi dan tekstur level menengah sama-sama tergali. Untuk menjaga informasi asli, keluaran transformer setiap level dikonkatenasi kembali dengan fitur level sebelum masuk TTEM.

### Decoder Tiga Aliran dan Fungsi Loss

Decoder menggabungkan tiga keluaran modul pemercepat dengan dua fitur level rendah (F1 dan F2). Alih-alih memfusikan ketiganya lebih dahulu (decoder aliran tunggal), TriTransNet membuat tiga cabang: setiap fitur level tinggi dinaikkan resolusinya, digabung berturut-turut dengan F2 dan F1, lalu diproses konvolusi dan fungsi sigmoid menjadi peta saliency sendiri (S3, S4, S5). Peta akhir (S_final) diperoleh dengan menjumlahkan keluaran pra-sigmoid ketiga cabang sebelum sigmoid diterapkan. Pelatihan menyeluruh (*end-to-end*) memakai fungsi loss *pixel position aware*, yaitu pembobotan galat per piksel yang memberi hukuman lebih besar pada piksel di sekitar batas objek; total loss menjumlahkan galat pada S_final dan ketiga peta cabang terhadap peta kebenaran.

## Eksperimen dan Hasil

Evaluasi dilakukan pada enam dataset RGB-D SOD: NLPR (1.000 citra), NJU2K (2.003 pasangan citra stereo), STERE (1.000 pasangan), DES (135 citra dalam ruang dari Kinect), SIP (1.000 citra berisi orang), dan DUT (1.200 citra kamera Lytro). Protokol latih mengikuti karya sebelumnya: 1.485 citra NJU2K dan 700 citra NLPR (total 2.185 pasangan); untuk pengujian pada DUT, 800 pasangan DUT ditambahkan ke data latih dan 400 sisanya dipakai untuk uji. Lima metrik dipakai: kurva presisi-recall, S-measure (kemiripan struktur peta), F-measure adaptif (rata-rata harmonik presisi dan recall dengan ambang adaptif), E-measure adaptif (kesejajaran piksel sekaligus statistik global), dan MAE (rata-rata selisih absolut per piksel; semakin kecil semakin baik). Pelatihan memakai masukan 256×256 dengan augmentasi acak, pengoptimal Adam (laju belajar awal 10^-5, *batch* 3), 150 epoch, dan berjalan sekitar 15 jam pada satu GPU NVIDIA 3090.

Dibandingkan dengan 16 metode terkini — antara lain D3Net, UCNet, JL-DCF, dan DSA2F — TriTransNet mencapai nilai terbaik atau hampir terbaik pada hampir semua metrik di keenam dataset; hanya dua nilai S-measure (pada NLPR dan STERE) yang berada di urutan kedua. Interpretasinya: keunggulan tidak terbatas pada satu jenis adegan, tetapi konsisten lintas sensor (stereo, Kinect, Lytro) dan lintas jenis objek.

Uji ablasi memisahkan sumbangan tiap komponen pada empat dataset. Menghilangkan TTEM menurunkan kinerja rata-rata sebesar 0,016 S-measure, 0,021 F-measure, 0,008 E-measure, dan menaikkan MAE 0,007 — penurunan terbesar pada F-measure menunjukkan keseimbangan presisi-recall paling diuntungkan oleh ketergantungan jarak jauh. Mengganti TTEM dengan GRU (unit rekuren gerbang, pemroses barisan alternatif) tetap kalah 0,012–0,014 poin pada S-measure dan F-measure, sehingga keuntungannya berasal dari mekanisme perhatian-diri, bukan sekadar penambahan modul sekuensial. Konfigurasi kembar dua (dua level teratas) dan kembar empat (empat level teratas) sama-sama lebih buruk daripada kembar tiga dengan selisih rata-rata 0,009–0,016 poin S/F-measure: dua level kurang menangkap konteks, empat level menyeret fitur menengah yang tidak cocok dengan bobot bersama. Modul DPM juga mengungguli penjumlahan per elemen polos maupun modul penguat kedalaman milik BBS-Net.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah efisiensi desain. Dengan membatasi transformer pada tiga level teratas yang resolusinya kecil, TriTransNet memperoleh ketergantungan global tanpa membayar biaya atensi pada peta beresolusi besar; dengan membagi bobot antar-encoder, kapasitas representasi naik tanpa parameter sebanyak tiga transformer independen. Modul DPM memberi ketangguhan terhadap kedalaman berkualitas rendah, seluruh komponen mudah disisipkan ke U-Net yang sudah ada, dan kode sumbernya tersedia untuk reproduksi.

Keterbatasannya, pertama, perhatian-diri standar tetap berbiaya kuadratik terhadap N = 1024 token, dan menumpuk 12 lapis encoder di atas enkoder ResNet-50 ganda menjadikan model berat untuk dilatih. Kedua, ketangguhan terhadap kedalaman buruk bersifat mitigatif, bukan eliminatif — DPM menekan kanal dan wilayah yang tidak informatif, tetapi pada kedalaman yang salah secara sistematis koreksinya terbatas. Ketiga, dari sisi rekayasa, decoder tiga aliran dengan empat titik supervisi menambah operasi inferensi, dan naskah tidak melaporkan kecepatan inferensi sebagai hasil utama, sehingga kesesuaiannya untuk aplikasi waktu-nyata belum teruji. Keempat, secara konseptual, strategi bobot bersama mengasumsikan ketiga level cukup mirip sifatnya; hasil ablasi kembar empat mengindikasikan asumsi ini cepat patah begitu level menengah disertakan, sehingga pilihan "tiga level teratas" lebih merupakan titik kerja empiris daripada prinsip umum.

## Kaitan dengan Bab Lain

TriTransNet melanjutkan garis fusi RGB-D yang diletakkan bab-bab sebelumnya dalam klaster ini. Dari [037 - 2021 - D3Net (Rethinking RGB-D SOD)](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md), makalah ini mewarisi protokol data latih dan kerangka evaluasi tolok ukur, sekaligus kepedulian terhadap kedalaman berkualitas rendah. Dari [036 - 2020 - BBS-Net](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), modul penguat kedalamannya dibandingkan langsung dalam ablasi dan diklaim terungguli oleh DPM. Garis fusi lintas-modal yang lebih tua dapat ditelusuri pada [035 - 2019 - DMRA](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md). Pada tahun yang sama, [042 - 2021 - Visual Saliency Transformer (VST)](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md) juga memadukan transformer dengan SOD, tetapi TriTransNet memilih strategi hibrida — CNN sebagai enkoder, transformer sebagai pemercepat fitur level tinggi — alih-alih tulang punggung transformer murni.

## Poin untuk Sitasi

Kutip dengan kunci `liu2021tritransnet`. Ringkasan yang aman dikutip: "TriTransNet memperkuat tiga level fitur teratas enkoder U-Net dengan tiga encoder transformer standar yang berbagi bobot, dan memurnikan fitur kedalaman melalui perhatian kanal dan spasial sebelum difusikan secara residual ke fitur warna; model ini mencapai kinerja terbaik atau hampir terbaik pada hampir semua metrik di enam dataset RGB-D SOD." Catatan verifikasi sebelum sitasi formal: (1) angka ablasi di bab ini (mis. +0,016 S-measure, +0,021 F-measure) adalah rata-rata lintas dataset sebagaimana dilaporkan pada teks ablasi makalah, sedangkan tabel kuantitatif utama (Tabel 1) memuat angka per dataset per metrik yang belum dicantumkan di sini dan wajib dikutip langsung dari naskah asli; (2) naskah menulis GPU pelatihan sebagai "GTX 3090"; (3) klaim "yang pertama memakai tiga encoder transformer berbagi bobot" adalah klaim penulis.
