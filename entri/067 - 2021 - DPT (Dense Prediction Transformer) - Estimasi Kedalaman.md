# 067 - Vision Transformers for Dense Prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ranftl2021dpt` |
| Judul asli | Vision Transformers for Dense Prediction |
| Penulis | René Ranftl, Alexey Bochkovskiy, Vladlen Koltun |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2021) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2103.13413
- **Kode sumber dan bobot model (resmi):** https://github.com/isl-org/DPT
- **Google Scholar:** https://scholar.google.com/scholar?q=Vision%20Transformers%20for%20Dense%20Prediction
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Vision%20Transformers%20for%20Dense%20Prediction&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DPT (*Dense Prediction Transformer*), arsitektur untuk prediksi padat, yaitu kelompok tugas yang menuntut satu keluaran untuk setiap piksel citra — estimasi kedalaman monokular menghasilkan satu nilai jarak per piksel, sedangkan segmentasi semantik menghasilkan satu label kelas per piksel. DPT mempertahankan kerangka *encoder–decoder* yang lazim, tetapi mengganti *encoder* konvolusional dengan *Vision Transformer* (ViT). Token keluaran dari beberapa lapis Transformer dirakit kembali menjadi peta fitur berbentuk citra pada empat resolusi, lalu digabung bertahap oleh *decoder* konvolusi hingga resolusi penuh. Karena Transformer mengolah representasi pada resolusi konstan dan memiliki daerah reseptif global di setiap lapis, prediksinya lebih halus sekaligus lebih koheren secara global dibanding jaringan sepenuhnya konvolusional.

Hasil utamanya terukur pada dua tugas. Pada estimasi kedalaman monokular dengan protokol *zero-shot* (model diuji pada dataset yang tidak pernah dilihat saat pelatihan), DPT memperbaiki kinerja relatif hingga 28% terhadap MiDaS, jaringan konvolusional terbaik saat itu. Pada segmentasi semantik, DPT mencatatkan mIoU 49,02% pada ADE20K — nilai tertinggi pada saat rilis — dan setelah disetel halus juga memuncaki tolok ukur NYUv2, KITTI, dan Pascal Context. Bobot DPT kemudian dirilis sebagai model MiDaS generasi berikutnya, sehingga arsitektur ini menjadi fondasi bagi banyak sistem estimasi kedalaman monokular sesudahnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak Eigen dkk. (bab 062) merumuskan estimasi kedalaman sebagai regresi dengan jaringan dalam, rancangan baku prediksi padat adalah *encoder–decoder*. Encoder biasanya berupa jaringan klasifikasi citra (*backbone*) yang dipra-latih pada ImageNet dan menurunkan resolusi citra secara bertahap; decoder menaikkan kembali resolusi fitur menjadi peta prediksi. Penurunan resolusi (*downsampling*) memang diperlukan agar daerah reseptif (*receptive field* — wilayah citra masukan yang memengaruhi satu unit fitur) membesar dan kebutuhan memori tetap terkendali, tetapi ada harganya: ketajaman spasial fitur hilang di lapis dalam, dan informasi yang hilang di encoder tidak dapat dipulihkan oleh decoder.

Berbagai perbaikan telah diusulkan tanpa mengubah fondasi konvolusinya: konvolusi terdilatasi (*dilated convolution*) yang memperbesar daerah reseptif tanpa menurunkan resolusi, *skip connection* dari lapis dangkal encoder ke decoder, serta arsitektur yang memelihara representasi multi-resolusi secara paralel. Semuanya tetap terbatas oleh sifat konvolusi itu sendiri — operator lokal yang hanya melihat lingkungan kecil, sehingga konteks seluruh citra baru tercapai setelah tumpukan lapis yang sangat dalam. Sementara itu, pada 2020 ViT membuktikan arsitektur Transformer murni mampu bersaing pada klasifikasi citra, tetapi keluarannya berupa sekumpulan token tanpa struktur dua dimensi, sehingga belum dapat dipakai langsung untuk prediksi padat. Masalah yang dipecahkan makalah ini adalah bagaimana menjadikan ViT backbone prediksi padat yang layak.

## Ide Utama

Gagasan inti DPT adalah menukar encoder konvolusional dengan ViT, lalu memanfaatkan satu sifat Transformer yang selama ini dipandang sebagai hambatan: jumlah token tidak pernah berubah di sepanjang lapis. Karena setiap token berkorespondensi satu-satu dengan petak (*patch*) citra masukan, token dari lapis mana pun dapat dilipat kembali menjadi peta fitur pada resolusi petak. Peta ini kemudian dapat dinaikkan atau diturunkan resolusinya, sehingga piramida fitur multi-skala yang biasa dihasilkan encoder konvolusional dapat ditiru — tetapi dihitung pada resolusi konstan dengan daerah reseptif global di setiap lapis. Dengan demikian, fitur tingkat rendah sekalipun sudah membawa konteks seluruh citra, dan fitur tingkat tinggi tidak kehilangan ketajaman spasial karena tidak ada *downsampling* setelah embedding awal.

## Cara Kerja Langkah demi Langkah

### Tokenisasi dan Encoder Transformer

Citra masukan dipotong menjadi petak bujur sangkar 16×16 piksel yang tidak saling tumpang tindih. Pada citra 384×384, terdapat 24×24 = 576 petak. Setiap petak (256 piksel, 768 nilai RGB) diratakan menjadi vektor dan diproyeksikan secara linier ke ruang berdimensi D = 768 (varian ViT-Base, 12 lapis Transformer) atau D = 1024 (ViT-Large, 24 lapis). Karena dimensi embedding lebih besar daripada jumlah piksel per petak, proyeksi ini pada prinsipnya dapat menyimpan informasi petak hingga ketelitian piksel. Varian ketiga, ViT-Hybrid, menghitung embedding dengan ResNet-50 (fitur pada 1/16 resolusi masukan, dua kali lebih tinggi dari fitur terdalam backbone konvolusional umum) sebelum 12 lapis Transformer; varian ini lebih hemat data.

Setiap token ditambahi *positional embedding* (vektor posisi yang dipelajari), sebab Transformer sebagai fungsi himpunan-ke-himpunan tidak mengetahui letak petak secara intrinsik. Satu token tambahan yang tidak terikat pada petak mana pun, disebut *readout token* (warisan dari pemakaian ViT untuk klasifikasi), ikut diproses. Inti setiap lapis adalah *multi-headed self-attention* (MHSA): setiap token menghitung kombinasi berbobot dari seluruh token lain berdasarkan kesamaan fitur, dengan beberapa himpunan bobot paralel. Konsekuensinya, setiap token dapat memengaruhi setiap token lain di setiap lapis — daerah reseptifnya global sejak lapis pertama, berbeda dengan konvolusi yang daerah reseptifnya tumbuh bertahap.

### Perakitan Token (Reassemble)

Keluaran ViT berupa 577 token tanpa bentuk citra. Operasi *Reassemble* mengembalikannya ke bentuk peta fitur melalui tiga tahap. Pertama, **Read** menangani readout token dengan salah satu dari tiga cara: diabaikan, dijumlahkan ke semua token, atau diproyeksikan — menggabungkan readout ke setiap token lalu melewati satu lapis linier dan aktivasi GELU (fungsi nonlinier halus berbasis distribusi Gauss). Uji ablasi menunjukkan varian proyeksi memberi hasil rata-rata terbaik, sehingga menjadi bawaan. Kedua, **Concatenate** menyusun 576 token sesuai posisi petaknya menjadi peta 24×24 dengan D kanal. Ketiga, **Resample** memproyeksikan peta ke 256 kanal dengan konvolusi 1×1, lalu mengubah resolusinya: konvolusi 3×3 ber-*stride* untuk menurunkan resolusi, atau konvolusi transposisi 3×3 untuk menaikkannya.

Perakitan dilakukan dari empat titik pada empat resolusi berbeda — lapis dangkal pada resolusi tinggi, lapis dalam pada resolusi rendah. Pada ViT-Large yang diambil adalah lapis {5, 12, 18, 24}; pada ViT-Base lapis {3, 6, 9, 12}; pada varian Hybrid diambil dua tahap pertama ResNet-50 embedding ditambah lapis {9, 12}. Untuk masukan 384×384, keempat peta berukuran 96×96 (1/4 resolusi), 48×48 (1/8), 24×24 (1/16), dan 12×12 (1/32). Alur lengkapnya:

```
citra 384 x 384
   │ potong petak 16 x 16 piksel
   ▼
576 token + 1 readout token, tiap token vektor D = 1024
   │ tambahkan positional embedding
   ▼
┌─────────────────────────────────────────────────────┐
│ ViT-Large: 24 lapis Transformer                     │
│ resolusi konstan 24 x 24 token, attention global    │
└──┬──────────────┬──────────────┬──────────────┬─────┘
lapis 5        lapis 12       lapis 18       lapis 24
   ▼              ▼              ▼              ▼
Reassemble    Reassemble    Reassemble    Reassemble
1/4: 96x96    1/8: 48x48    1/16: 24x24   1/32: 12x12
256 kanal     256 kanal     256 kanal     256 kanal
   │              │              │              ▼
   │              │              │      ┌─ blok fusi ─ upsample x2
   │              │              ▼      ▼
   │              │      ┌─ blok fusi ─ upsample x2
   │              ▼      ▼
   │      ┌─ blok fusi ─ upsample x2     (gaya RefineNet:
   ▼      ▼                              unit konvolusi residual)
peta fitur 192 x 192 (setengah resolusi masukan)
   │ head tugas (kedalaman / segmentasi)
   ▼
prediksi padat 384 x 384
```

### Decoder Konvolusi dan Head Tugas

Keempat peta digabung oleh blok fusi bergaya RefineNet — modul yang menggabungkan fitur dari dua skala berdekatan memakai unit konvolusi residual (dua lapis konvolusi dengan jalan pintas identitas). Setiap tahap fusi menaikkan resolusi dua kali lipat, dimulai dari peta terkecil, sehingga representasi akhir berukuran setengah resolusi masukan. Di atasnya dipasang *head* sesuai tugas: head kedalaman terdiri atas tiga lapis konvolusi yang bertahap mengecilkan kanal hingga satu skalar nonnegatif per piksel yang menyatakan kedalaman invers, lalu di-*upsample* bilinear ke resolusi penuh; head segmentasi menghasilkan *logit* (skor mentah sebelum normalisasi probabilitas) per kelas pada setengah resolusi, lalu di-*upsample* bilinear. Seperti jaringan sepenuhnya konvolusional, DPT menerima ukuran citra yang bervariasi selama ukurannya habis dibagi 32; *positional embedding* cukup diinterpolasi bilinear ke jumlah petak yang baru.

## Eksperimen dan Hasil

Eksperimen pertama adalah estimasi kedalaman monokular dengan protokol *zero-shot* lintas dataset dari MiDaS. Model dilatih pada MIX 6, meta-dataset gabungan sepuluh sumber data berisi sekitar 1,4 juta citra — kumpulan data pelatihan terbesar untuk tugas ini saat itu — memakai fungsi *loss* invarian terhadap skala dan pergeseran pada kedalaman invers, ditambah *gradient-matching loss* yang mencocokkan turunan spasial prediksi dengan kebenaran. Pelatihan berjalan 60 epoch pada subset terkurasi lalu 60 epoch pada data penuh, dengan 72.000 langkah per epoch dan *batch* 16 pada potongan 384×384. Hasilnya: rata-rata perbaikan relatif terhadap model MiDaS asli lebih dari 23% untuk DPT-Hybrid dan hingga 28% untuk DPT-Large. Interpretasinya langsung: dengan protokol dan data yang sama, kesalahan turun sekitar seperempat hanya karena penggantian backbone. Untuk memastikan perbaikan bukan semata akibat data yang lebih besar, jaringan konvolusional MiDaS dilatih ulang pada MIX 6 — kinerjanya memang naik, tetapi tetap kalah jelas dari kedua varian DPT. DPT juga lebih tangguh saat resolusi inferensi dinaikkan di atas resolusi latih, konsisten dengan daerah reseptif globalnya, dan latensinya sebanding dengan MiDaS meskipun DPT-Large memiliki parameter sekitar tiga kali lebih banyak.

Eksperimen kedua menyetel halus DPT-Hybrid pada dataset kecil NYUv2 (kedalaman dalam ruang) dan KITTI (kedalaman luar ruang). Karena prediksi model *zero-shot* hanya terdefinisi hingga faktor skala dan pergeseran, prediksi awal terlebih dahulu disejajarkan secara global ke data latih sebelum *loss* dihitung. Hasilnya menyamai atau memperbaiki keadaan terbaru pada semua metrik kedua dataset, menunjukkan arsitektur ini tetap berguna pada data berukuran terbatas.

Eksperimen ketiga adalah segmentasi semantik pada ADE20K (150 kelas). DPT-Hybrid mencapai mIoU 49,02% dan akurasi piksel 83,11%, melampaui pembanding konvolusional terkuat, DeepLabV3 dengan ResNeSt-200, yang mencatat 48,36% dan 82,45%. Selisih 0,66 poin mIoU pada tolok ukur seketat ADE20K merupakan margin nyata, dan mIoU 49,02% adalah nilai tertinggi yang dilaporkan saat rilis. Yang lebih informatif adalah hasil DPT-Large: 47,63% — justru di bawah DPT-Hybrid. Penulis mengaitkannya dengan ukuran ADE20K yang jauh lebih kecil daripada MIX 6; ini bukti empiris bahwa backbone Transformer besar baru unggul penuh bila data pelatihan melimpah. Penyetelan halus pada Pascal Context juga dilaporkan mencapai keadaan terbaru.

Uji ablasi pada subset terkurasi (sekitar 41.000 citra, diukur dengan deviasi absolut relatif — semakin kecil semakin baik) menegaskan tiga pilihan rancangan. Pengetukan fitur dari kombinasi lapis dangkal dan dalam lebih baik daripada hanya lapis dalam. Pada perbandingan backbone, ViT-Large (0,0778) dan ViT-Hybrid (0,0783) mengungguli ResNet-50 (0,0935) dan ResNeXt-101-WSL (0,0806); artinya backbone Transformer mengalahkan backbone konvolusional terbaik sekalipun yang terakhir dipra-latih pada korpus berskala miliaran citra, dan varian Hybrid menawarkan akurasi mendekati varian Large dengan jumlah parameter setara varian Base.

## Kelebihan dan Keterbatasan

Kelebihan DPT bersifat langsung dari desainnya: prediksi lebih halus dan lebih koheren secara global karena tidak ada *downsampling* berjenjang dan setiap lapis melihat seluruh citra; arsitekturnya memetik manfaat besar dari data besar; satu kerangka yang sama melayani regresi (kedalaman) dan klasifikasi per piksel (segmentasi) dengan hanya mengganti head; ukuran masukan fleksibel; dan degradasi kinerja pada resolusi inferensi yang lebih tinggi lebih landai dibanding jaringan konvolusional.

Keterbatasannya juga jelas. Pertama, kebutuhan data: makalah menyatakan DPT membuka potensi penuhnya pada pelatihan berskala besar, dan hasil ADE20K (DPT-Large kalah dari DPT-Hybrid) memperlihatkan konsekuensinya pada dataset kecil. Kedua, dari sisi rekayasa, biaya *self-attention* tumbuh kuadratis terhadap jumlah token, sehingga masukan beresolusi tinggi mahal; DPT-Large juga membawa parameter sekitar tiga kali lipat model MiDaS, dan kesetaraan latensinya bergantung pada paralelisme GPU. Ketiga, keluaran kedalaman *zero-shot* bersifat invarian-afine — benar hanya hingga skala dan pergeseran yang tidak diketahui — sehingga untuk kedalaman metrik diperlukan penyelarasan atau penyetelan halus tambahan. Keempat, encoder bergantung pada bobot ViT pra-latih ImageNet; tanpa pra-pelatihan klasifikasi yang baik, keunggulan arsitektur ini belum tentu terwujud.

## Kaitan dengan Bab Lain

Bab ini mewarisi dua garis sekaligus. Dari [bab 062](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md) diwarisi kerangka *encoder–decoder* multi-skala untuk kedalaman serta fungsi *loss* invarian-skala Eigen yang dipakai saat penyetelan halus. Dari [bab 068](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md) (MiDaS) diwarisi seluruh protokol pelatihan dan evaluasi *zero-shot*: meta-dataset MIX 5 diperluas menjadi MIX 6, dan metrik relatif serta prosedur penyelarasannya dipakai apa adanya — DPT dapat dibaca sebagai penggantian backbone pada resep MiDaS. Sebagai pembanding sezaman, [bab 066](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md) (AdaBins) juga memasukkan Transformer ke estimasi kedalaman, tetapi pada sisi keluaran melalui diskretisasi rentang kedalaman adaptif, sedangkan DPT mengganti sisi backbone. Ke depan, bobot DPT-Hybrid dan DPT-Large dirilis sebagai model MiDaS resmi, sehingga arsitektur ini menjadi penyedia *pseudo-depth* (peta kedalaman hasil prediksi model, pengganti sensor kedalaman) yang banyak dipakai pada bab-bab sesudahnya, termasuk untuk melengkapi data RGB-D dalam tinjauan ini.

## Poin untuk Sitasi

Kutip dengan kunci `ranftl2021dpt`. Ringkasan yang aman dikutip: "DPT (Ranftl dkk., ICCV 2021) menjadikan Vision Transformer sebagai backbone prediksi padat dengan merakit token dari beberapa lapis menjadi peta fitur multi-resolusi yang digabung decoder konvolusi; pada estimasi kedalaman monokular *zero-shot* DPT memperbaiki kinerja relatif hingga 28% terhadap MiDaS, dan pada segmentasi semantik mencapai 49,02% mIoU pada ADE20K, keadaan terbaru saat rilis." Catatan verifikasi: angka 28% dan 23% adalah rata-rata perbaikan relatif lintas dataset *zero-shot* terhadap model MiDaS asli sesuai Tabel 1 naskah; angka ADE20K (49,02%; 48,36%; 47,63%) berasal dari Tabel 4 naskah dan telah dicocokkan; angka rinci NYUv2, KITTI, dan Pascal Context (Tabel 2, 3, 5) tidak dikutip dalam bab ini dan wajib diperiksa ke naskah asli sebelum sitasi formal; nomor halaman ICCV (12179–12188) pada `references.bib` belum diverifikasi ke prosiding.
