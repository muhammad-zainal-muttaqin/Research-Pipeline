# 065 - From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `lee2019bts` |
| Judul asli | From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation |
| Penulis | Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, Il Hong Suh (Hanyang University) |
| Tahun | 2019 |
| Venue | arXiv preprint arXiv:1907.10326 |
| Tema | Estimasi Kedalaman |

## Tautan Akses

- **arXiv (abstrak dan PDF gratis):** https://arxiv.org/abs/1907.10326
- **Repositori kode resmi (TensorFlow dan PyTorch):** https://github.com/cleinc/bts
- **Google Scholar:** https://scholar.google.com/scholar?q=From%20Big%20to%20Small%3A%20Multi-Scale%20Local%20Planar%20Guidance%20for%20Monocular%20Depth%20Estimation

## Gambaran Umum

Makalah ini memperkenalkan BTS (*From Big to Small*), sebuah jaringan tersupervisi untuk estimasi kedalaman monokular, yaitu tugas memprediksi jarak setiap piksel ke kamera dari satu citra RGB saja. Masalah yang dipecahkan adalah hilangnya detail geometris ketika fitur beresolusi rendah di dalam dekoder dikembalikan ke resolusi penuh citra masukan. Alih-alih memakai *upsampling* biasa, BTS menempatkan lapisan *Local Planar Guidance* (LPG) pada tiga tahap dekoder; setiap lapisan memprediksi koefisien bidang datar lokal yang secara eksplisit menentukan nilai kedalaman di dalam petak-petak kecil pada resolusi penuh. Pada tolok ukur NYU Depth V2 dan KITTI, BTS mengungguli metode tersupervisi sebelumnya dengan margin yang dilaporkan penulis sebagai signifikan, misalnya AbsRel 0,059 pada KITTI (rentang 0–80 m) dibandingkan 0,072 milik pemegang rekor sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular adalah masalah *ill-posed*: tak berhingga banyak susunan adegan tiga dimensi dapat terproyeksi menjadi citra dua dimensi yang sama, sehingga kedalaman tidak dapat diturunkan dari geometri saja dan harus dipelajari dari data. Garis tersupervisi dimulai dari karya Eigen dkk. yang melatih jaringan konvolusi langsung dari piksel ke peta kedalaman (lihat [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)), sedangkan jalur swa-supervisi memakai rekonstruksi stereo (lihat [063 - 2017 - Monodepth (Left-Right Consistency)](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)).

Arsitektur yang lazim dipakai berbentuk *encoder-decoder*: *encoder* (jaringan ekstraksi fitur) menurunkan resolusi spasial citra melalui konvolusi terlangkah dan *pooling* hingga seperdelapan sampai sepertigapuluhdua ukuran asli, lalu *decoder* mengembalikan resolusi penuh untuk prediksi per piksel. Pemulihan resolusi ini adalah titik lemah. Teknik yang umum dipakai sebelum BTS adalah *skip connection* (menyambungkan fitur encoder ke decoder pada resolusi yang sama) dan *upconv* (penaikan resolusi tetangga-terdekat diikuti konvolusi), tetapi keduanya tidak memiliki mekanisme eksplisit untuk menentukan bagaimana satu sel fitur beresolusi rendah mengisi kembali wilayah resolusi tinggi di bawahnya. Akibatnya, peta kedalaman cenderung kabur pada batas objek dan permukaan miring.

## Ide Utama

Gagasan inti BTS: satu sel fitur pada resolusi H/k tidak di-*upsampling* secara buta, melainkan dipakai untuk memprediksi empat koefisien sebuah bidang datar dalam ruang tiga dimensi. Bidang ini kemudian dipakai untuk menghitung nilai kedalaman setiap piksel di dalam petak k×k pada resolusi penuh, melalui perpotongan sinar kamera dengan bidang tersebut. Asumsinya sederhana: dalam wilayah kecil k×k piksel, permukaan adegan cukup baik didekati oleh sebuah bidang datar, sehingga empat parameter cukup untuk merekonstruksi k×k nilai kedalaman. Tanpa asumsi ini, dekoder harus mempelajari k² nilai secara terpisah untuk petak yang sama; untuk k = 8, itu berarti 4 parameter berbanding 64 nilai. Karena lapisan ini dipasang pada tiga skala (k = 8, 4, 2), petak kasar memulihkan bentuk global dan petak halus memulihkan detail, lalu semuanya digabungkan menjadi peta kedalaman akhir.

## Cara Kerja Langkah demi Langkah

### Encoder dan Ekstraktor Konteks

Masukan berupa citra RGB berukuran H×W. Jaringan dasar (*backbone*) — dalam eksperimen dipilih dari ResNet-101, ResNext-101, atau DenseNet-161 yang sudah dilatih untuk klasifikasi ImageNet — mengekstraksi fitur hingga resolusi H/8. Setelahnya dipasang modul *atrous spatial pyramid pooling* (ASPP) versi rapat (DenseASPP): konvolusi berdilasi, yaitu konvolusi yang tapisnya diberi celah sehingga mencakup wilayah luas tanpa menurunkan resolusi, dengan lima laju dilatasi r ∈ {3, 6, 12, 18, 24} untuk menangkap konteks multi-skala.

### Dekoder dan Lapisan Local Planar Guidance

Dekoder menaikkan resolusi bertahap dengan faktor dua (1/8 → 1/4 → 1/2 → penuh) memakai *upconv*. Pada setiap tahap dengan resolusi 1/8, 1/4, dan 1/2, sebuah lapisan LPG mengambil peta fitur tahap itu dan langsung memproyeksikannya ke resolusi penuh H×W, sehingga berfungsi pula sebagai jalan pintas internal dekoder. Alur lengkapnya digambarkan pada diagram berikut.

```
citra RGB H x W
     |
     v
+------------------+      +---------------------------+
| backbone         |----->| DenseASPP (r=3,6,12,18,24)|
| (mis. DenseNet-161, H/8) |---------------------------+
+------------------+                  |
                                      v
        dekoder: upconv x2 bertahap (1/8 -> 1/4 -> 1/2 -> H)
            |              |              |            |
            v              v              v            v
         LPG-8          LPG-4          LPG-2      reduksi 1x1
        (petak 8x8)   (petak 4x4)   (petak 2x2)   (per piksel)
            |              |              |            |
            +------+-------+------+-------+------------+
                   v
        konkatenasi + konvolusi akhir --> peta kedalaman H x W
```

Diagram di atas menunjukkan bahwa keempat keluaran (tiga LPG dan satu reduksi 1×1) semuanya sudah beresolusi penuh H×W sebelum digabungkan.

### Mekanisme di dalam Satu Lapisan LPG

Untuk peta fitur beresolusi H/k, lapisan LPG bekerja dalam tiga langkah. Pertama, tumpukan konvolusi 1×1 mereduksi jumlah kanal berulang kali dengan faktor dua hingga tersisa tiga kanal, menghasilkan tensor H/k × H/k × 3. Kedua, tensor ini dipecah menjadi dua jalur agar memenuhi kendala geometris bidang: dua kanal pertama ditafsirkan sebagai sudut polar dan azimut (θ, φ) lalu diubah menjadi vektor normal satuan (n₁, n₂, n₃) melalui n₁ = sin θ cos φ, n₂ = sin θ sin φ, n₃ = cos θ; kanal ketiga dilewatkan fungsi *sigmoid* dan dikalikan konstanta κ (kedalaman maksimum, 10 m untuk NYU, 80 m untuk KITTI) menjadi n₄, jarak tegak lurus bidang ke pusat kamera. Ketiga, untuk setiap piksel i di dalam petak k×k pada resolusi penuh, kedalaman kandidat dihitung dengan rumus perpotongan sinar-bidang: c̃ᵢ = n₄ / (n₁uᵢ + n₂vᵢ + n₃), dengan (uᵢ, vᵢ) koordinat piksel yang dinormalisasi di dalam petak.

Sebagai contoh numerik: pada tahap 1/8 untuk citra 480×640, setiap sel fitur memandu petak 8×8 = 64 piksel di resolusi penuh hanya dengan empat koefisien bidang. Keluaran tiap lapisan LPG adalah satu peta H×W×1 berisi kedalaman kandidat.

### Kombinasi Multi-Skala dan Estimasi Akhir

Selain tiga keluaran LPG (c̃⁸ˣ⁸, c̃⁴ˣ⁴, c̃²ˣ²), dekoder menghasilkan c̃¹ˣ¹ melalui reduksi 1×1 setelah *upconv* terakhir. Keempat peta dikonkatenasi dan dilewatkan ke satu konvolusi akhir, yang perilakunya dapat ditulis sebagai d̃ = f(W₁c̃¹ˣ¹ + W₂c̃²ˣ² + W₃c̃⁴ˣ⁴ + W₄c̃⁸ˣ⁸). Karena fungsi rugi hanya didefinisikan pada estimasi akhir d̃, setiap skala tidak dipaksa menjadi prediksi kedalaman global yang berdiri sendiri; jaringan bebas membagi peran, dan penulis mengamati bahwa skala kasar mempelajari bentuk utama sedangkan skala halus mengoreksi detail dan kesalahan batas dari skala kasar.

### Fungsi Rugi dan Pelatihan

Pelatihan memakai rugi *scale-invariant* dari Eigen dkk.: D(g) = (1/T)Σgᵢ² − (λ/T²)(Σgᵢ)², dengan gᵢ = log d̃ᵢ − log dᵢ selisih logaritmik prediksi dan *ground truth*, serta T jumlah piksel berlabel valid. Bentuk ini setara dengan jumlah variansi galat dan rataan galat terbobot dalam ruang logaritmik; penulis menaikkan λ dari 0,5 menjadi 0,85 agar optimasi lebih menekan variansi galat, dan memakai rugi akhir L = 10√D(g) karena penskalaan rentang rugi teramati memperbaiki konvergensi. Jaringan dilatih 50 *epoch* dengan pengoptimal Adam, laju pembelajaran awal 10⁻⁴, ukuran *batch* 16, dan pemangkasan acak 352×704 (KITTI) atau 416×544 (NYU).

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur standar. NYU Depth V2 memuat citra dalam-ruang 480×640 dari sensor Kinect; BTS memakai 24.231 pasangan citra-kedalaman untuk latih dan 654 citra untuk uji. KITTI memuat adegan berkendara luar-ruang; pembagian Eigen memakai 23.488 citra latih dan 697 citra uji. Metrik yang dipakai: AbsRel (rata-rata galat relatif |d̃−d|/d, makin kecil makin baik), RMSE (akar rataan kuadrat galat dalam meter), dan δ < 1,25 (persentase piksel yang rasio prediksi terhadap *ground truth* berada dalam faktor 1,25, makin besar makin baik).

Pada KITTI rentang 0–80 m, varian ResNext-101 mencapai δ < 1,25 sebesar 0,956, AbsRel 0,059, dan RMSE 2,756 m. Angka ini mengungguli Fu dkk. (0,932; 0,072; 2,727 m) dan Yin dkk. (0,938; 0,072; 3,258 m): proporsi piksel akurat naik 1,8 poin persentase dan galat relatif turun sekitar 18% terhadap pembanding terbaik, meskipun RMSE-nya masih sedikit di atas RMSE Fu dkk. Pada rentang 0–50 m, RMSE BTS turun dari 2,271 m menjadi 1,925 m, perbaikan sekitar 15%. Pada NYU Depth V2, implementasi resmi dengan DenseNet-161 melaporkan δ < 1,25 sebesar 0,885, AbsRel 0,110, dan RMSE 0,392 m — artinya 88,5% piksel terprediksi dalam toleransi 25% pada rentang kedalaman dalam-ruang 0–10 m.

Studi ablasi pada NYU dengan dasar ResNet-101 menambahkan komponen satu per satu: ASPP, *upconv*, lalu LPG. Penambahan LPG memberi lompatan kinerja paling besar, sementara biayanya hanya sekitar 0,1 juta parameter tambahan. Eksperimen lintas *backbone* menunjukkan DenseNet-161 terbaik pada NYU, sedangkan ResNext-101 terbaik pada KITTI; varian ringan MobileNetV2 hanya kehilangan sekitar 3 poin persentase pada metrik δ dengan parameter kurang dari separuhnya.

## Kelebihan dan Keterbatasan

Kelebihan utama BTS adalah hubungan eksplisit antara fitur internal dan keluaran resolusi penuh: empat koefisien bidang per petak menggantikan k² nilai yang harus dipelajari *upconv* biasa, sehingga batas objek dan permukaan miring terrekonstruksi lebih tajam dengan biaya parameter yang hampir tidak bertambah. Desainnya juga modular — LPG dapat dipasang di atas beragam *backbone* — dan didukung kode resmi yang terbuka.

Keterbatasan pertama bersifat data: metode ini tersupervisi penuh sehingga membutuhkan *ground truth* kedalaman dari sensor. Penulis sendiri melaporkan artefak pada langit dan bagian atas citra KITTI, yang mereka analisis sebagai akibat label LiDAR yang sangat jarang di wilayah tersebut. Kedua, secara konseptual, asumsi bidang datar lokal tidak berlaku pada permukaan lengkung tajam; BTS menanganinya hanya secara implisit melalui skala yang lebih halus, bukan dengan model permukaan yang lebih kaya. Ketiga, dari sisi rekayasa, varian terbaik memakai *backbone* besar (47 juta parameter untuk DenseNet-161), sehingga biaya inferensi tidak ringan.

## Kaitan dengan Bab Lain

BTS meneruskan garis tersupervisi yang dibuka Eigen dkk. pada [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md), termasuk memakai rugi *scale-invariant* yang diperkenalkan di sana. Posisinya komplementer terhadap jalur swa-supervisi [063 - 2017 - Monodepth (Left-Right Consistency)](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md) dan [064 - 2019 - Monodepth2](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md): BTS mengorbankan kebebasan dari label demi akurasi metrik yang lebih tinggi. Gagasan memberi struktur geometris pada keluaran dekoder berkembang pada bab-bab berikutnya, antara lain [066 - 2021 - AdaBins](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md) yang memodelkan distribusi kedalaman secara adaptif, dan [067 - 2021 - DPT (Dense Prediction Transformer)](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md) yang mengganti dekoder konvolusi dengan *transformer*. Dalam konteks tinjauan YOLO/RGB-D, BTS adalah kandidat penghasil *pseudo-depth*: peta kedalaman prediksinya dapat menggantikan sensor kedalaman sebagai kanal masukan detektor RGB-D.

## Poin untuk Sitasi

Kunci BibTeX: `lee2019bts`.

Ringkasan yang aman dikutip: Lee dkk. (2019) mengusulkan BTS, jaringan estimasi kedalaman monokular tersupervisi dengan lapisan *Local Planar Guidance* pada tiga tahap dekoder, yang memprediksi koefisien bidang datar lokal untuk memandu pemulihan resolusi penuh. Metode ini melaporkan hasil state-of-the-art pada NYU Depth V2 dan KITTI saat dirilis, dengan penambahan parameter hanya sekitar 0,1 juta untuk lapisan LPG.

Catatan verifikasi sebelum sitasi formal: (1) angka NYU pada bab ini (δ1 0,885; AbsRel 0,110; RMSE 0,392 m) diambil dari tabel *model zoo* repositori resmi, bukan dari Tabel 1 naskah — cocokkan dengan versi arXiv terbaru (v6) sebelum dikutip; (2) nilai lengkap Tabel 3 (server evaluasi daring KITTI) dan Tabel 4 (ablasi) tidak sempat diekstrak angka per angka, sehingga hanya kesimpulan kualitatifnya yang dipakai; (3) makalah ini berstatus *preprint* arXiv; periksa versi terbit resmi saat sitasi dilakukan.
