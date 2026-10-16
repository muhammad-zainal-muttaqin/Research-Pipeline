# Oil Palm Fruit Maturity Classification Algorithm Based on LAB Dual-Branch Feature Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2026oil` |
| Judul asli | Oil Palm Fruit Maturity Classification Algorithm Based on LAB Dual-Branch Feature Fusion |
| Penulis | Wu, Junli; Liu, Xuewei; Song, Junjie; Zhang, Kai; Zhao, Yan |
| Tahun | 2026 |
| Venue | Applied Sciences Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [wu2026oil.pdf](../pdf/wu2026oil.pdf)
- DOI resmi: https://doi.org/10.3390/app16147292

## Gambaran Umum
Makalah ini mengusulkan CMF-Net (*Color-Matrix Fusion Network*), jaringan klasifikasi lima tingkat kematangan buah kelapa sawit berbasis citra. Citra RGB diubah ke ruang warna CIELAB (LAB), lalu komponen luminans (L) dan kromatisitas (ab) diproses oleh dua cabang InceptionV3 yang paralel. Fitur kedua cabang digabung dengan mekanisme gerbang (*gated fusion*), diinteraksikan antarskala oleh BiFPN, dan diperkuat oleh *coordinate attention* (CA) serta *self-attention* (SA). Pelatihan memakai supervisi ordinal (CORAL) dan regresi warna tambahan.

Data utama adalah *Oil Palm Fruit Ripeness Dataset* dari Mendeley Data, yang pada Tabel 1 makalah memuat lima kelas: Immature (759), Unripe (1.420), Under-ripe (1.496), Ripe (667), dan Over-ripe (413). Tiga kumpulan data publik lain dipakai untuk uji generalisasi. Data berupa citra buah yang diklasifikasikan per citra, bukan deteksi tandan di pohon; lokasi, kultivar, dan sensor pengambilan citra tidak dijelaskan.

Pada kumpulan data utama dengan pembagian latih-validasi 8:2, CMF-Net mencapai akurasi 95,88%, presisi 96,02%, *recall* 96,66%, spesifisitas 98,91%, dan F1 96,20% (Tabel 3). Abstrak menyebut akurasi validasi 94,66% dan keunggulan 1,3 sampai 6,1 poin persentase; angka itu tidak sama dengan angka pada Tabel 3 (lihat catatan verifikasi).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Kandungan minyak buah sawit berkaitan dengan kematangannya, dan pencampuran tandan dengan tingkat kematangan berbeda sebelum sterilisasi dapat memengaruhi rendemen dan mutu minyak. Tingkat kematangan ditentukan dari ciri visual eksokarp, terutama warna dan derajat buah lepas. Penulis menyatakan bahwa tahap kematangan yang bersebelahan memiliki transisi warna bertahap dan tampilan permukaan yang mirip, sehingga terjadi kerancuan antarkelas yang berdekatan.

Penulis mencatat dua kelemahan metode terdahulu. Pada ruang RGB, informasi kecerahan dan warna bercampur sehingga perbedaan warna halus sulit ditonjolkan. Metode yang ada juga umumnya mengekstraksi fitur global dan kurang memodelkan secara bersama perubahan warna lokal dan informasi kecerahan. Kelemahan ketiga yang dikemukakan adalah bahwa klasifikasi *softmax* memperlakukan kelas kematangan sebagai label independen dan mengabaikan urutannya.

## Ide Utama
Gagasan pokoknya adalah memisahkan luminans dan kromatisitas pada ruang LAB sehingga satu cabang mempelajari struktur dan tekstur, sedangkan cabang lain mempelajari petunjuk warna kematangan. Pemisahan ini dipadukan dengan fusi adaptif berbobot gerbang, interaksi multi-skala, perhatian lokal dan global, serta kerugian yang memperhitungkan urutan kelas (supervisi ordinal) dan statistik warna (regresi rerata kanal a dan b).

## Cara Kerja Langkah demi Langkah

### 1. Data dan praproses
Semua citra diubah ukurannya menjadi 224 × 224 piksel. Kanal L, a, dan b dinormalisasi ke rentang [0, 1]; kanal L menjadi masukan cabang pertama dan kanal a dan b digabung menjadi masukan cabang kedua. Pembagian latih dan validasi 8:2 sama untuk CMF-Net dan semua model pembanding. Augmentasi hanya pada data latih: pembalikan horizontal, perturbasi kecerahan kanal L (faktor dari [0,5; 1,5], bias dari [−0,1; 0,1]), rotasi pada [−15°, 15°], dan derau Gauss dengan simpangan baku 0,03. Penghalusan label 0,02 dipakai. Jumlah total citra dan pohon asal tidak dilaporkan selain jumlah per kelas pada Tabel 1.

### 2. Adaptor masukan dan ekstraksi dua cabang
Adaptor masukan terdiri atas konvolusi 1 × 1, normalisasi *batch*, dan ReLU, yang memetakan kanal L (1 kanal) dan ab (2 kanal) menjadi tiga kanal. Dua jaringan InceptionV3 paralel mengekstraksi fitur pada tiga skala (L3, L4, L5) dengan resolusi 1/8, 1/16, dan 1/32.

### 3. Fusi bergerbang
Pada tiap skala, fitur kedua cabang diselaraskan dengan konvolusi 1 × 1, digabung secara kanal, dilewatkan pada *global average pooling*, lapisan terhubung penuh, dan sigmoid untuk menghasilkan bobot gerbang $g_s$. Fitur hasil fusi adalah $g_s \hat F^L_s + (1-g_s)\hat F^{ab}_s$.

### 4. BiFPN lintas cabang
Piramida fitur hasil fusi diproses dengan jalur *top-down* dan *bottom-up*. Tiga keluaran diselaraskan ke resolusi tertinggi, digabung, dan dipadatkan dengan konvolusi 1 × 1.

### 5. Perhatian multi-tingkat
*Coordinate attention* menghitung bobot arah tinggi dan lebar, kemudian *self-attention* dengan proyeksi Q, K, dan V melalui konvolusi 1 × 1 menangkap dependensi global, dengan sambungan residual.

### 6. Klasifikasi ordinal dan kerugian gabungan
Kepala ordinal mengeluarkan $K-1$ probabilitas sigmoid terurut, dan kategori diperoleh dari penjumlahan indikator $p_k > 0{,}5$. Kerugian total adalah $L_{ord} + \lambda L_{color}$, dengan $L_{color}$ galat kuadrat rerata kanal a dan b yang diprediksi terhadap rerata sebenarnya, dan $\lambda = 0{,}1$.

### 7. Pengaturan pelatihan
Ubuntu 20.04, PyTorch 2.0.0, CUDA 11.8, GPU NVIDIA GeForce RTX 4090; ukuran *batch* 32; 100 *epoch*; optimizer Adam dengan laju belajar awal $1\times10^{-4}$ dan penjadwal ReduceLROnPlateau (faktor 0,5; kesabaran 5 *epoch*; minimum $1\times10^{-6}$); *dropout* 0,5, 0,4, dan 0,3. *Checkpoint* dipilih berdasarkan akurasi validasi tertinggi.

## Eksperimen dan Hasil
Pembanding adalah VGG16, MobileNetV2, DenseNet121, Improved CNN, ResNet152V2, MobileViT-CBAM, Swin-T, ConvNeXt-Tiny, dan EfficientNetV2-S. Metrik meliputi akurasi, presisi, *recall*, spesifisitas, dan F1. Semua model dievaluasi pada pembagian validasi yang sama; tidak ada himpunan uji terpisah yang disebut.

Tabel berikut menyalin nilai utama dari Tabel 3 makalah (persen).

| Model | Params (M) | FLOPs (G) | Akurasi | Presisi | *Recall* | F1 |
|---|---|---|---|---|---|---|
| ResNet152V2 | 58,59 | 22,81 | 89,55 | 89,57 | 89,55 | 89,55 |
| Swin-T | 27,52 | 4,37 | 95,14 | 95,66 | 96,40 | 96,16 |
| ConvNeXt-Tiny | 27,82 | 4,45 | 95,42 | 97,11 | 96,35 | 96,11 |
| EfficientNetV2-S | 20,18 | 2,71 | 94,65 | 95,70 | 95,40 | 95,52 |
| CMF-Net | 26,74 | 5,37 | 95,88 | 96,02 | 96,66 | 96,20 |

Waktu inferensi CMF-Net adalah 0,84 ms; kolom Tabel 3 yang sama memuat akurasi latih 100,00% dan akurasi validasi 95,98% untuk CMF-Net. Pada VGG16, nilai awal-kolom yang terbaca adalah 87,54% akurasi.

Ablasi (Tabel 4): model dasar tanpa modul tambahan berakurasi 87,95% dan F1 87,01%; penambahan berturut-turut adaptor masukan (91,54%), fusi bergerbang (92,28%), BiFPN (93,66%), CA (94,19%), SA (94,58%), dan supervisi ordinal (95,88%). Selisih model lengkap terhadap model dasar adalah 7,93 poin pada akurasi dan 9,19 poin pada F1, sesuai teks makalah. Pada analisis bobot $\lambda$ (Tabel 5), nilai terbaik dicapai pada $\lambda = 0{,}1$ dengan akurasi 95,35% dan F1 95,57%, sedangkan $\lambda = 0$ memberi 93,23% dan 94,07%.

Generalisasi (Tabel 6): pada *Ripeness of Oil Palm Fruit Dataset*, CMF-Net memperoleh akurasi 98,96% dan F1 98,93%. Pada *Palm Ripeness Dataset* (kecil), akurasi 96,16% dan F1 95,63%, dengan F1 di bawah ConvNeXt-Tiny (95,82%) dan MobileViT-CBAM (95,78%) serta Swin-T (95,93%). Pada *Date Fruit Dataset* (kurma, bukan sawit), akurasi 99,63% dan F1 99,79%. Validasi silang lima lipatan menghasilkan akurasi 95,88% ± 0,32% dan F1 96,20% ± 0,35% dengan selang kepercayaan 95% [95,48; 96,28] dan [95,77; 96,63] (Tabel 7); perbedaan terhadap ConvNeXt-Tiny memiliki nilai-$p$ 0,087 sehingga tidak signifikan pada taraf 0,05. Matriks konfusi (Gambar 11) melaporkan akurasi per kelas 98,68% untuk Immature dan 98,78% untuk Decayed, dengan kesalahan terbanyak antara kelas yang bersebelahan.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: pemisahan luminans dan kromatisitas, fusi adaptif, serta supervisi ordinal mengurangi kerancuan antarkelas bersebelahan; pengujian dilakukan pada beberapa kumpulan data dan validasi silang lima lipatan.

Keterbatasan yang dinyatakan penulis: kumpulan data kematangan sawit publik masih terbatas dan belum mencakup variasi wilayah, kultivar, musim, perangkat, dan lingkungan lapangan; biaya komputasi cabang ganda lebih tinggi daripada model ringan sehingga penerapan pada perangkat tertanam memerlukan optimasi lebih lanjut. Pekerjaan mendatang meliputi perluasan ke deteksi waktu-nyata di lapangan.

Menurut pembacaan ringkasan ini, ada beberapa hal tambahan. Angka akurasi validasi pada abstrak (94,66%) berbeda dari Tabel 3 (95,88% untuk akurasi dan 95,98% untuk akurasi validasi). Akurasi latih 100,00% menunjukkan kemungkinan *overfitting* yang tidak dibahas. Evaluasi hanya memakai pembagian validasi yang juga dipakai untuk memilih *checkpoint*, tanpa himpunan uji terpisah. Pembagian dilakukan per citra; apakah citra dari tandan atau pohon yang sama dapat jatuh di kedua sisi pembagian tidak dijelaskan, sehingga kebocoran data tidak dapat dikesampingkan. Karena tugasnya klasifikasi citra tunggal, tidak ada penanganan tandan yang sama pada banyak citra.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani identitas lintas pandang. Masukannya adalah citra buah atau tandan yang diklasifikasikan satu per satu, tanpa pelacakan, pencocokan multi-pandang, atau rekonstruksi 3D, dan tidak ada pencacahan. Hasil dilaporkan sebagai metrik klasifikasi per citra (dan akurasi per kelas pada matriks konfusi), bukan sebagai hitungan per kelas terhadap acuan panen atau hitung manual; acuan label adalah anotasi kelas pada citra.

Hal yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah komponen atribut kelas. Penguraian LAB dua cabang dan supervisi ordinal dapat dipakai sebagai pengklasifikasi kematangan setelah deteksi, dan kerancuan antarkelas bersebelahan yang dilaporkan relevan bagi inventaris per kelas. Pengklasifikasi ini tidak menyelesaikan masalah penghitungan ganda lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wu2026oil`.

Wu dkk. (2026) mengusulkan CMF-Net, jaringan dua cabang pada ruang warna LAB dengan fusi bergerbang, BiFPN, CA, SA, serta supervisi ordinal dan regresi warna tambahan, untuk klasifikasi lima tingkat kematangan buah kelapa sawit. Pada *Oil Palm Fruit Ripeness Dataset* (Mendeley Data) dengan pembagian latih-validasi 8:2, model memperoleh akurasi 95,88% dan F1 96,20% (validasi silang lima lipatan: 95,88% ± 0,32% dan 96,20% ± 0,35%), melampaui sebagian pembanding tetapi tidak berbeda signifikan dari ConvNeXt-Tiny ($p$ = 0,087).

Catatan verifikasi data: Angka akurasi, presisi, *recall*, spesifisitas, dan F1 diambil dari Tabel 3 dan teks Seksi 3.3 dan 5; ablasi dari Tabel 4; bobot $\lambda$ dari Tabel 5; generalisasi dari Tabel 6; statistik lima lipatan dari Tabel 7; akurasi per kelas dari Seksi 3.9.1. Abstrak menyebut akurasi validasi 94,66% dan keunggulan 1,3 sampai 6,1 poin persentase; angka itu tidak dapat dicocokkan dengan Tabel 3. Pada Tabel 5, akurasi untuk $\lambda = 0{,}1$ (95,35%) berbeda dari akurasi model lengkap di Tabel 3 (95,88%); penyebabnya tidak dijelaskan. Ekstraksi Tabel 3 membuat kolom waktu inferensi dan beberapa kolom sulit disejajarkan (misalnya Swin-T tertulis 0,60 pada kolom waktu inferensi), sehingga nilai kecuali yang disebut di atas tidak dipakai. Jumlah total citra tidak dilaporkan; jumlah per kelas hanya tersedia dari Tabel 1 (penjumlahan 4.755 adalah hitungan ringkasan ini). Nama kelas pada Tabel 1 (Immature, Unripe, Under-ripe, Ripe, Over-ripe) tidak sama dengan nama pada teks (Immature, Partially ripe, Fully ripe, Overripe, Decayed); pemetaan tidak dijelaskan.
