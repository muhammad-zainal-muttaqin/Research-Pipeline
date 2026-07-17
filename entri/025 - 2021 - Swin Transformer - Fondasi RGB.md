# 025 - Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2021swin` |
| Judul asli | Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows |
| Penulis | Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, Baining Guo |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2021) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2103.14030
- **Kode sumber resmi:** https://github.com/microsoft/Swin-Transformer
- **Google Scholar:** https://scholar.google.com/scholar?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Swin Transformer, *backbone* (jaringan pengekstrak fitur) visi berbasis Transformer untuk tujuan umum. Dua kelemahan Transformer visi sebelumnya, ViT (bab 024), diperbaiki sekaligus: biaya *self-attention* (atensi-diri, mekanisme yang membobot relasi antartoken) yang kuadratik terhadap jumlah token, dan peta fitur beresolusi tunggal yang tidak cocok untuk prediksi padat seperti deteksi objek dan segmentasi semantik. Solusinya: *self-attention* hanya dihitung di dalam jendela lokal yang tidak tumpang tindih, partisi jendela digeser pada lapisan berikutnya agar informasi tetap mengalir antar-jendela, dan peta fitur disusun hierarkis dari resolusi tinggi ke rendah.

Model terbesarnya mencapai akurasi top-1 87,3% pada klasifikasi ImageNet-1K (dengan pra-pelatihan ImageNet-22K), 58,7 box AP dan 51,1 mask AP pada COCO *test-dev*, serta 53,5 mIoU pada ADE20K — ketiganya melampaui hasil terbaik sebelumnya dengan margin lebih dari dua poin.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pemodelan visi lama didominasi jaringan saraf konvolusi (CNN) seperti ResNet, yang membangun representasi secara hierarkis: resolusi peta fitur diturunkan bertahap sambil jumlah kanal dinaikkan. Struktur multi-skala ini penting karena ukuran objek dalam citra sangat bervariasi, dan kerangka hilir seperti FPN (*Feature Pyramid Network*, modul yang menggabungkan peta fitur beberapa resolusi untuk mendeteksi objek berbagai ukuran) dirancang di atasnya.

Vision Transformer (ViT, bab 024) membuktikan arsitektur Transformer mampu menyaingi CNN pada klasifikasi: citra dipotong menjadi *patch* (petak piksel) berukuran tetap, setiap petak diubah menjadi satu *token* (vektor satuan pemrosesan), dan semua token berinteraksi melalui *self-attention* global. Desain ini menyimpan dua masalah. Pertama, biaya komputasinya kuadratik terhadap jumlah token karena setiap token berelasi dengan semua token lain — tidak terjangkau pada citra beresolusi tinggi yang menghasilkan ribuan token. Kedua, resolusi token dipertahankan sama dari awal sampai akhir, sehingga hanya dihasilkan peta fitur satu skala.

Upaya lain menekan biaya attention dengan *sliding window* (jendela geser): attention setiap piksel dibatasi pada tetangganya, tetapi himpunan pembanding yang berbeda per piksel membuat akses memorinya tidak efisien. Makalah ini merancang Transformer yang sekaligus efisien, hierarkis, dan kuat daya modelnya.

## Ide Utama

Gagasan intinya terdiri atas dua bagian yang saling melengkapi. Pertama, *self-attention* dihitung hanya di dalam **jendela lokal** yang mempartisi citra tanpa tumpang tindih; karena ukuran jendela tetap, biaya per jendela konstan dan total biaya linear terhadap jumlah token. Kedua, partisi jendela **digeser** pada blok berikutnya, sehingga jendela baru melintasi batas jendela lama dan token yang tadinya terpisah kini berbagi satu jendela. Pergantian dua konfigurasi ini memulihkan konektivitas antar-jendela tanpa mengorbankan efisiensi.

Di atas keduanya, representasi dibuat hierarkis melalui *patch merging*: kelompok token bertetangga digabung menjadi satu token baru per tahap, mengikuti pola penurunan resolusi pada CNN. Keluaran tiap tahap berbeda resolusi, sehingga Swin dapat langsung menggantikan *backbone* CNN pada kerangka deteksi atau segmentasi yang ada.

## Cara Kerja Langkah demi Langkah

### Partisi Patch dan Token

Citra RGB masukan dibagi menjadi *patch* 4×4 piksel yang tidak tumpang tindih. Setiap petak direpresentasikan sebagai gabungan nilai piksel mentahnya: 4×4×3 = 48 angka. Sebuah lapisan linear (*linear embedding*) memproyeksikan vektor 48 dimensi ini menjadi vektor C dimensi, dengan C sebagai lebar kanal dasar model. Pada citra 224×224, pembagian ini menghasilkan 56×56 = 3.136 token.

### Blok Swin Transformer

Blok Swin Transformer adalah blok Transformer standar yang modul attention-nya diganti attention berjendela. Susunannya: normalisasi *LayerNorm* (LN, penormalan fitur per token), modul *multi-head self-attention* berjendela, koneksi residual (keluaran modul ditambahkan ke masukannya), LN kedua, MLP dua lapis dengan aktivasi GELU, dan koneksi residual kedua. *Multi-head* berarti attention dihitung paralel pada beberapa sub-ruang fitur (kepala) yang lalu digabung; dimensi tiap kepala 32. Blok dipasangkan: blok berpartisi reguler (W-MSA) diikuti blok berpartisi bergeser (SW-MSA).

### Attention di dalam Jendela (W-MSA)

Pada W-MSA (*window multi-head self-attention*), peta fitur h×w token dipartisi menjadi jendela-jendela berisi M×M token (M = 7 secara baku, 49 token per jendela), dan attention hanya dihitung antar-token dalam jendela yang sama. Biaya attention global adalah Ω(MSA) = 4hwC² + 2(hw)²C — suku kedua kuadratik terhadap jumlah token hw — sedangkan versi berjendela Ω(W-MSA) = 4hwC² + 2M²hwC, linear terhadap hw karena M tetap.

Contoh numerik pada tahap pertama (h = w = 56): attention global membutuhkan 3.136² ≈ 9,8 juta pasangan token per kepala, sedangkan W-MSA membutuhkan 64 jendela × 49² = 153.664 pasangan — 64 kali lebih sedikit. Selisih ini makin besar pada citra beresolusi tinggi.

### Partisi Jendela yang Digeser (SW-MSA)

Attention murni berjendela tidak memiliki koneksi antar-jendela, sehingga daya modelnya turun. SW-MSA (*shifted window*) menggeser partisi jendela sejauh ⌊M/2⌋ token ke arah kiri-atas (3 token untuk M = 7), sehingga informasi menyebar antar-jendela melalui kedalaman jaringan. Ilustrasinya pada peta 8×8 token dengan jendela 4×4 (geseran 2 token):

```
partisi reguler (W-MSA)         partisi bergeser (SW-MSA)
peta 8x8 token, jendela 4x4     digeser (2,2): 9 jendela
┌────────┬────────┐             ┌───┬──────┬───┐
│        │        │             │   │      │   │
│   A    │   B    │             ├───┼──────┼───┤
│        │        │             │   │      │   │
├────────┼────────┤    ---->    ├───┼──────┼───┤
│        │        │             │   │      │   │
│   C    │   D    │             ├───┼──────┼───┤
│        │        │             │   │      │   │
└────────┴────────┘             └───┴──────┴───┘
```

Jendela tengah pada konfigurasi bergeser mencakup seperempat wilayah jendela A, B, C, dan D; token yang tadinya terpisah kini saling ber-attention. Pergeseran menambah jumlah jendela (2×2 menjadi 3×3) dengan jendela tepi lebih kecil dari M×M. Solusi naif berupa *padding* (token kosong tambahan) menaikkan komputasi sampai 2,25 kali; makalah memakai *cyclic shift* (bagian yang keluar tepi dipindahkan ke sisi berlawanan) diikuti *attention mask* (larangan attention antar-token yang semula tidak bersebelahan), sehingga jumlah jendela yang dihitung tetap. Implementasi ini 13–18% lebih cepat daripada *padding* naif.

### Penggabungan Patch dan Empat Tahap Hierarkis

Lapisan *patch merging* ditempatkan antar-tahap: fitur setiap kelompok 2×2 token bertetangga digabungkan menjadi vektor 4C, lalu lapisan linear memproyeksikannya ke 2C. Jumlah token berkurang empat kali lipat dan resolusi turun dua kali lipat per dimensi. Pengulangan prosedur ini membentuk empat tahap beresolusi H/4×W/4, H/8×W/8, H/16×W/16, dan H/32×W/32 — sama dengan pembagian resolusi pada CNN seperti ResNet. Alurnya untuk Swin-T pada citra 224×224:

```
citra RGB 224x224
   │  patch 4x4 + linear embedding (48 -> C=96)
   ▼
Tahap 1:  56x56 token, dim 96    [2 blok Swin]
   │  patch merging: gabung 2x2 tetangga (96 -> 192)
   ▼
Tahap 2:  28x28 token, dim 192   [2 blok Swin]
   │  patch merging (192 -> 384)
   ▼
Tahap 3:  14x14 token, dim 384   [6 blok Swin]
   │  patch merging (384 -> 768)
   ▼
Tahap 4:  7x7 token, dim 768     [2 blok Swin]
   ▼
keluaran multi-skala -> klasifikasi / deteksi / segmentasi
```

### Bias Posisi Relatif

Attention tidak mengetahui posisi token. Alih-alih *absolute position embedding* (vektor posisi per token seperti pada ViT), Swin menambahkan *relative position bias* (bias posisi relatif) B pada skor kesamaan: Attention(Q,K,V) = SoftMax(QKᵀ/√d + B)V. Q, K, V adalah matriks *query*, *key*, dan *value*: proyeksi linear fitur token untuk mencari kesamaan, membandingkan, dan membawa isi yang dibobotkan. B diambil dari matriks (2M−1)×(2M−1) = 13×13 yang dipelajari, diindeks oleh jarak relatif antar-token pada kedua sumbu. Bias relatif ini memberi ketidakpekaan terhadap pergeseran posisi objek (*translation invariance*) yang berguna untuk prediksi padat.

### Varian Model

Empat varian disediakan dengan mengatur lebar kanal dasar C dan jumlah blok per tahap: Swin-T (C = 96, blok {2,2,6,2}; 29 juta parameter dan 4,5 GFLOPs, sekelas ResNet-50), Swin-S (C = 96, blok {2,2,18,2}; 50 juta parameter, sekelas ResNet-101), Swin-B (C = 128, blok {2,2,18,2}; 88 juta parameter, sekelas ViT-B), dan Swin-L (C = 192, blok {2,2,18,2}; 197 juta parameter). FLOPs (*floating-point operations*) mengukur biaya komputasi satu inferensi; G berarti giga (miliar).

## Eksperimen dan Hasil

Tiga tolok ukur dipakai: klasifikasi pada ImageNet-1K (1,28 juta citra latih, 1.000 kelas) dengan metrik akurasi top-1 (proporsi citra yang kelas teratas prediksinya benar); deteksi objek dan segmentasi instans pada COCO 2017 (118 ribu citra latih) dengan AP (*Average Precision*, ringkasan kurva presisi-recall pada berbagai ambang tumpang tindih) untuk kotak (*box AP*) dan masker piksel (*mask AP*); serta segmentasi semantik pada ADE20K (150 kategori) dengan mIoU (*mean Intersection over Union*, rata-rata rasio irisan terhadap gabungan antara peta kelas prediksi dan kebenaran). Deteksi diuji pada empat kerangka (Cascade Mask R-CNN, ATSS, RepPoints v2, Sparse R-CNN) dan segmentasi pada kerangka UperNet, dengan hanya mengganti *backbone*-nya.

Hasil utamanya sebagai berikut:

- ImageNet-1K: Swin-T mencapai 81,3% top-1, melampaui DeiT-S (79,8%), varian ViT berukuran sebanding, dengan margin +1,5 poin. Dengan pra-pelatihan ImageNet-22K (14,2 juta citra), Swin-B mencapai 86,4% pada resolusi 384², unggul 2,4 poin atas ViT-B/16 (84,0%) pada *throughput* (citra per detik) yang hampir sama (84,7 banding 85,9) dan FLOPs lebih rendah (47,0G banding 55,4G). Swin-L mencapai 87,3%.
- COCO: Swin-T unggul konsisten +3,4 sampai +4,2 box AP atas ResNet-50 pada keempat kerangka deteksi (pada Cascade Mask R-CNN: 50,5 banding 46,3). Pada ukuran model dan kecepatan sebanding, Swin-B mencapai 51,9 box AP dan 45,0 mask AP, mengungguli ResNeXt101-64x4d (48,3 dan 41,7). Sistem terbaik (Swin-L pada kerangka HTC++ dengan pengujian multi-skala) mencapai 58,7 box AP dan 51,1 mask AP pada *test-dev*, melampaui hasil terbaik sebelumnya sebesar +2,7 (Copy-paste) dan +2,6 (DetectoRS). Kenaikan beberapa poin AP tergolong besar untuk tolok ukur ini.
- ADE20K: Swin-S mencapai 49,3 mIoU, jauh di atas DeiT-S (44,0) pada biaya komputasi sebanding. Swin-L dengan pra-pelatihan ImageNet-22K mencapai 53,5 mIoU, unggul +3,2 atas SETR (50,3) — pendekatan berbasis ViT untuk segmentasi — dengan model lebih kecil (234 juta banding 308 juta parameter).

Ablasi (uji dengan mematikan satu komponen) pada Swin-T menegaskan rancangannya. Tanpa penggeseran jendela, akurasi turun ke 80,2% top-1 (−1,1), 47,7 box AP (−2,8), dan 43,3 mIoU (−2,8) — bukti bahwa koneksi antar-jendela berkontribusi nyata. Bias posisi relatif memberi tambahan +1,2 poin top-1 dibanding tanpa posisi dan +2,3 mIoU; menambahkan posisi absolut justru sedikit merugikan deteksi dan segmentasi. Partisi bergeser seakurat *sliding window* (81,3% banding 81,4% top-1), tetapi Swin-T utuh 4,1 kali lebih cepat daripada implementasi *sliding window* naif.

## Kelebihan dan Keterbatasan

Kelebihan: (1) kompleksitas linear membuat attention terjangkau pada citra beresolusi tinggi; (2) peta fitur hierarkis beresolusi standar CNN sehingga langsung kompatibel dengan FPN maupun UperNet; (3) partisi bergeser memulihkan koneksi antar-jendela dengan latensi tambahan kecil dan efisien pada perangkat keras umum; (4) satu arsitektur yang sama kuat pada klasifikasi, deteksi, dan segmentasi.

Keterbatasan: attention tetap lokal per lapisan; interaksi sangat jauh hanya terjalin tidak langsung melalui tumpukan lapisan. Dari sisi rekayasa, implementasinya lebih rumit dari CNN standar (partisi bergeser, *cyclic shift*, *attention mask* khusus), dan *throughput* yang dilaporkan masih berbasis fungsi PyTorch umum — pembanding ResNe(X)t diuntungkan kernel cuDNN yang sangat dioptimalkan, sehingga perbandingan kecepatan belum final. Angka terbaik pada ketiga tolok ukur juga bergantung pada pra-pelatihan ImageNet-22K; tanpa data tambahan itu keunggulannya lebih tipis. Ukuran jendela baku 7×7 mengikat: pada resolusi yang jauh berbeda diperlukan *padding* atau interpolasi bias posisi.

## Kaitan dengan Bab Lain

Bab ini menjawab keterbatasan ViT pada [bab 024](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md): attention global kuadratik digantikan attention berjendela linear, dan peta fitur satu skala digantikan hierarki empat tahap. Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)) turut membangun fitur multi-resolusi tetapi mempertahankan attention kuadratik. Desain ini disempurnakan penerusnya, Swin Transformer V2 ([bab 163](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)), yang menskalakan kapasitas dan resolusi model. Dari sisi CNN, ConvNeXt ([bab 162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)) memodernisasi ResNet dengan menyerap pilihan desain Transformer sebagai pembanding kuat Swin. Jejak praktisnya terlihat pada metode hilir yang memakainya sebagai *backbone*, misalnya SwinNet ([bab 043](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)) untuk deteksi objek menonjol RGB-D.

## Poin untuk Sitasi

Kutip dengan kunci `liu2021swin` (ICCV 2021, halaman 10012–10022). Ringkasan yang aman dikutip: "Swin Transformer adalah *backbone* visi hierarkis yang menghitung *self-attention* di dalam jendela lokal tidak tumpang tindih dan menggeser partisi jendela antar-lapisan, sehingga berkompleksitas linear terhadap ukuran citra sekaligus tetap menghubungkan antar-jendela. Model ini mencapai 87,3% top-1 pada ImageNet-1K, 58,7 box AP pada COCO *test-dev*, dan 53,5 mIoU pada ADE20K."

Catatan verifikasi sebelum sitasi formal: angka 87,3% top-1 dan 53,5 mIoU diperoleh dengan pra-pelatihan ImageNet-22K, dan angka COCO terbaik memakai kerangka HTC++ dengan pengujian multi-skala — sebutkan konteks ini bila mengutip. Akurasi Swin-B 224² pada ImageNet-1K tercatat 83,3% pada teks tetapi 83,5% pada tabel makalah (arXiv v2); periksa versi prosiding sebelum mengutipnya.
