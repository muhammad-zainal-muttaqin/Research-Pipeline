# 173 - GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jia2024geminifusion` |
| Judul asli | GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer |
| Penulis | Ding Jia, Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Chang Xu, Xinghao Chen |
| Tahun | 2024 |
| Venue | International Conference on Machine Learning (ICML 2024) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2406.01210
- **Proceedings resmi ICML (PMLR):** https://proceedings.mlr.press/v235/jia24b.html
- **Kode sumber:** https://github.com/JiaDingCN/GeminiFusion

## Gambaran Umum

GeminiFusion adalah modul fusi multimodal untuk *Vision Transformer* (ViT, arsitektur transformer yang memproses citra sebagai barisan token piksel/*patch*) yang menggabungkan fitur dari dua modalitas — misalnya RGB dan kedalaman (*depth*) — pada tingkat piksel, dengan biaya komputasi yang tumbuh linear terhadap jumlah token, bukan kuadratik seperti *cross-attention* penuh. Masalah yang disasar adalah trade-off pada metode fusi sebelumnya: mekanisme pertukaran token (*token exchange*) murah tetapi kalah akurat dibanding *cross-attention* global, sedangkan *cross-attention* global akurat tetapi mahal karena menghitung interaksi antara semua pasangan token dari kedua modalitas.

Gagasan intinya adalah membatasi interaksi *cross-attention* hanya pada pasangan token yang berada di posisi spasial sama pada kedua modalitas (fusi per-piksel), lalu memperkaya interaksi yang sempit ini dengan derau (*noise*) yang dapat dipelajari per-lapis serta sebuah pembeda hubungan (*relation discriminator*) ringan. Pada segmentasi semantik RGB-D dengan *backbone* MiT-B3 (varian *Mix Transformer* yang dipakai SegFormer), GeminiFusion mencapai 56,8% mIoU (*mean Intersection-over-Union*, metrik rata-rata rasio irisan-gabungan antara peta segmentasi prediksi dan kebenaran lapangan) pada NYUDv2, dan diklaim dapat dipasang ke berbagai *backbone* (MiT, Swin Transformer) serta berbagai tugas (segmentasi arbitrary-modal, deteksi objek 3D, translasi citra multimodal) tanpa perubahan struktural besar.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi semantik RGB-D memanfaatkan dua sumber informasi: citra warna (RGB) dan peta kedalaman yang menyimpan jarak setiap piksel ke kamera. Bab 171 (SegFormer) menunjukkan bahwa *encoder* hierarkis berbasis transformer efektif untuk segmentasi RGB tunggal, tetapi tidak dirancang untuk menggabungkan dua modalitas. Bab 172 (EMSANet) menangani penggabungan RGB-D dengan modul fusi bertujuan khusus pada arsitektur berbasis konvolusi.

Pada arsitektur berbasis transformer, dua pendekatan fusi bersaing sebelum GeminiFusion. Pendekatan pertama, TokenFusion, menukar token yang dianggap kurang informatif pada satu modalitas dengan token dari modalitas lain pada posisi yang sama. Pendekatan ini murah secara komputasi tetapi kalah akurat dibanding pendekatan kedua, yaitu *cross-attention* global, yang menghitung skor perhatian antara setiap token satu modalitas dengan setiap token modalitas lain. Untuk barisan sepanjang N token, *cross-attention* global berbiaya O(N² · c) — kuadratik terhadap jumlah token, dengan c dimensi fitur per token — sehingga tidak praktis pada peta fitur beresolusi tinggi tempat N bisa mencapai ribuan. Sebagai gambaran biaya nyata, makalah mencatat bahwa *cross-attention* penuh model pembanding (CMNeXt) memakan 17 GFLOPs pada satu contoh, sedangkan mekanisme yang diusulkan GeminiFusion hanya 0,14 GFLOPs untuk beban kerja setara — penurunan sekitar 99,2%. Kesenjangan akurasi-efisiensi ini adalah masalah yang ingin ditutup makalah: apakah fusi bisa semurah pertukaran token tetapi seakurat *cross-attention* global.

## Ide Utama

GeminiFusion mengamati bahwa pada RGB-D dan modalitas terselaraskan sejenis, fitur pada posisi piksel i di satu modalitas paling relevan dengan fitur pada posisi piksel i yang sama di modalitas lain, karena kedua peta fitur menggambarkan lokasi fisik yang sama pada adegan. Oleh karena itu, interaksi *cross-attention* dibatasi hanya pada pasangan token sejajar posisi tersebut, bukan seluruh N × N pasangan. Pembatasan ini menurunkan kompleksitas dari kuadratik menjadi linear terhadap jumlah token, O(N · c²).

Pembatasan ke satu pasangan per posisi menimbulkan dua persoalan baru yang menjadi kontribusi teknis kedua makalah. Pertama, ketika *attention* dihitung untuk satu pasangan token saja, keluaran fungsi *softmax* (fungsi yang menormalkan skor menjadi peluang berjumlah satu) selalu bernilai 1, sehingga tidak ada diferensiasi antar-kandidat. Kedua, tanpa mekanisme penyeimbang, satu modalitas cenderung "meniru" pola dirinya sendiri lewat pasangan yang mirip, bukan menyerap informasi baru dari modalitas lain — bertentangan dengan tujuan fusi. GeminiFusion mengatasi keduanya dengan menyuntikkan derau yang dapat dipelajari secara khusus per-lapis jaringan (*layer-adaptive noise*) ke dalam perhitungan *key* dan *value*, serta menambahkan modul pembeda hubungan yang menilai seberapa berbeda fitur kedua modalitas pada posisi tertentu, lalu memakai nilai itu untuk memodulasi kontribusi antar-modal.

## Cara Kerja Langkah demi Langkah

### Fusi Intra-Modal dan Inter-Modal per Piksel

Pada setiap posisi token i, GeminiFusion menghitung dua aliran secara paralel: aliran intra-modal (dalam modalitas yang sama, misalnya RGB dengan RGB) dan aliran inter-modal (RGB dengan kedalaman). Keluaran untuk modalitas 1 pada posisi i dirumuskan sebagai Y[i]¹ = Attention(Q¹, K¹, V¹) + X[i]¹, dan sebaliknya untuk modalitas 2. Yang membedakan dari *self-attention* biasa adalah isi K dan V: keduanya disusun dari gabungan fitur modalitas sendiri (untuk komponen intra-modal) dan fitur modalitas lain pada posisi sejajar (untuk komponen inter-modal), sehingga satu perhitungan *attention* sudah memuat kedua sumber informasi tanpa perlu lapis terpisah.

### Derau Adaptif per Lapis dan Pembeda Hubungan

Derau yang dapat dipelajari ditambahkan ke komponen *key* dan *value* milik jalur intra-modal, dengan nilai derau berbeda untuk setiap lapis jaringan. Derau ini memecahkan masalah *softmax* yang selalu bernilai 1 pada perhatian satu-lawan-satu, karena kini ada variasi nilai yang membuat *softmax* menghasilkan bobot bermakna. Komponen inter-modal, sebelum digabungkan, dimodulasi oleh skor hubungan φ dari modul pembeda hubungan (*relation discriminator*) — jaringan ringan berupa konvolusi 1×1 dan lapis *softmax* yang menghasilkan skor pada rentang [0, 1] sebagai ukuran kemiripan fitur kedua modalitas pada posisi tersebut. Semakin rendah kemiripan, semakin besar potensi kontribusi informasi baru dari modalitas lain, sehingga skor ini mengatur seberapa besar fitur inter-modal ikut memengaruhi keluaran.

Diagram berikut merangkum posisi kedua komponen dalam satu lapis fusi:

```
token RGB[i]  token Depth[i]        (posisi piksel i yang sama)
     │               │
     ├─ intra-modal ─┤   + derau adaptif per-lapis (atasi softmax=1,
     │   (K,V dari    │    cegah modalitas meniru dirinya sendiri)
     │   modal sendiri)│
     ├─ inter-modal ──┤   x skor relasi φ(RGB[i], Depth[i])
     │   (K,V dari     │   dari relation discriminator (conv 1x1
     │   modal lain)   │   + softmax), memodulasi kontribusi silang
     ▼                ▼
  Y_RGB[i]         Y_Depth[i]   -> hanya O(N·c^2), bukan O(N^2·c)
```

### Penyisipan pada Backbone Transformer

Modul fusi disisipkan pada setiap dari empat tahap *encoder* hierarkis bergaya SegFormer (*stride* 4, 8, 16, 32 terhadap resolusi citra masukan), dengan parameter fusi dibagi (*shared*) antar-modalitas kecuali lapis normalisasi (*Layer Normalization*) yang tetap terpisah per-modalitas. Desain ini terbukti dapat dipasang pada dua keluarga *backbone* berbeda — MiT (dipakai SegFormer, bab 171) dan Swin Transformer (varian bergeser jendela dari bab 164 PVT) — tanpa perubahan arsitektural besar, mengindikasikan modul ini bersifat plug-in (dapat disisipkan) dan tidak terikat pada satu desain *backbone* tertentu.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada segmentasi semantik RGB-D memakai dua dataset indoor standar: NYUDv2 dan SUN RGB-D, keduanya berisi pasangan citra RGB dan peta kedalaman beranotasi kelas per piksel. Dengan *backbone* MiT-B3, GeminiFusion mencapai 56,8% mIoU pada NYUDv2 dan 52,7% mIoU pada SUN RGB-D; dengan *backbone* MiT-B5 yang lebih besar, angka naik menjadi 57,7% dan 53,3%; dengan Swin-Transformer-large resolusi 384, NYUDv2 mencapai 60,2% (60,9% dengan penyetelan lanjutan dari model yang sudah dilatih pada SUN RGB-D). Dibandingkan TokenFusion pada kondisi setara, makalah melaporkan kenaikan +2,6 poin mIoU pada NYUDv2 (56,8% vs 54,2%) dan +1,3 poin pada SUN RGB-D (52,7% vs 51,4%) — bukti bahwa pembatasan interaksi ke pasangan sejajar posisi tidak mengorbankan akurasi dibanding metode pertukaran token, sekaligus jauh lebih efisien dibanding *cross-attention* penuh.

Uji ablasi (percobaan yang mengurangi komponen satu per satu untuk mengukur kontribusinya) pada NYUDv2 menunjukkan kontribusi bertahap: model unimodal murni tanpa fusi mencapai 53,3% mIoU; menambahkan *attention* silang per-piksel menaikkannya ke 55,4% (+2,1 poin); menambahkan derau adaptif per-lapis menaikkannya lagi ke 56,3% (+0,9 poin); dan menambahkan pembeda hubungan mencapai 56,8% (+0,5 poin) — setiap komponen memberi kontribusi positif meski menurun besarannya. Pengujian latensi dengan MiT-B3 menunjukkan model penuh (28 lapis fusi) berjalan pada 153 milidetik dengan 56,8% mIoU, sedangkan varian yang hanya memasang fusi pada 10 lapis terakhir berjalan 116 milidetik dengan 56,4% mIoU — masih lebih cepat sekaligus lebih akurat daripada TokenFusion (126 milidetik, 54,2% mIoU). Di luar segmentasi RGB-D, makalah juga melaporkan hasil pada deteksi objek 3D (MVX-Net dengan GeminiFusion pada KITTI: 88,49 AP kelas mudah versus 87,49 AP baseline) dan translasi citra multimodal pada dataset Taskonomy, keduanya menunjukkan perbaikan konsisten meski dengan margin lebih kecil daripada segmentasi.

## Kelebihan dan Keterbatasan

Kelebihan utama GeminiFusion adalah efisiensi: kompleksitas linear terhadap jumlah token membuatnya jauh lebih murah daripada *cross-attention* global sambil mempertahankan sebagian besar keuntungan akurasinya dibanding pertukaran token. Modul ini juga terbukti serbaguna lintas *backbone* (MiT, Swin) dan lintas tugas (segmentasi, deteksi 3D, translasi citra), yang jarang ditunjukkan oleh modul fusi bertujuan khusus.

Dari sisi konseptual, pembatasan interaksi ke pasangan token sejajar posisi mengasumsikan kedua modalitas terselaraskan secara spasial dengan baik — asumsi yang berlaku kuat untuk RGB-D hasil sensor tunggal seperti Kinect, tetapi berpotensi lemah jika kedua modalitas mengalami pergeseran kalibrasi atau resolusi berbeda. Dari sisi rekayasa, mekanisme derau per-lapis dan pembeda hubungan menambah hiperparameter serta kompleksitas pelatihan dibanding fusi sederhana seperti penjumlahan atau konkatenasi fitur, sehingga penyetelan pada dataset atau modalitas baru mungkin memerlukan usaha tambahan. Keunggulan efisiensi juga paling terasa relatif terhadap *cross-attention* penuh; dibanding metode fusi konvolusi ringan pada bab 172 (EMSANet), selisih biaya komputasi tidak dibahas secara langsung dalam sumber yang diverifikasi.

## Kaitan dengan Bab Lain

GeminiFusion beroperasi di atas fondasi *encoder* hierarkis berbasis transformer yang diletakkan SegFormer (bab 171, kunci `xie2021segformer`), memakai *backbone* MiT yang sama, dan menunjukkan portabilitas ke Swin Transformer, arsitektur transformer bergeser jendela yang menurunkan biaya *attention* dengan cara berbeda dari mekanisme *pyramid* pada PVT (bab 164). Dibanding EMSANet (bab 172), yang menyelesaikan fusi RGB-D pada arsitektur konvolusi bertujuan khusus, GeminiFusion menunjukkan jalur alternatif berbasis transformer dengan biaya komputasi yang secara eksplisit dirancang linear. Bab ini juga berhubungan dengan bab 174 (Omnivore) pada level tujuan: keduanya mengejar model tunggal yang menangani banyak modalitas, meski Omnivore memakai strategi berbagi bobot lintas modalitas pada tingkat arsitektur, sedangkan GeminiFusion memakai modul fusi eksplisit yang disisipkan ke *backbone* yang sudah ada. Prinsip pembatasan interaksi ke token sejajar posisi demi efisiensi linear relevan pula sebagai pembanding metodologis bagi mekanisme *attention* jarang (*sparse attention*) pada bab-bab transformer terdahulu seperti Co-DETR (bab 165), yang menekan biaya *attention* dengan strategi berbeda (penetapan label ganda), bukan pembatasan posisi spasial.

## Poin untuk Sitasi

Kutip dengan kunci `jia2024geminifusion`. Ringkasan yang aman dikutip: "GeminiFusion mengusulkan fusi RGB-D per-piksel pada Vision Transformer dengan kompleksitas linear terhadap jumlah token, mencapai 56,8% mIoU pada NYUDv2 dan 52,7% mIoU pada SUN RGB-D dengan backbone MiT-B3, mengungguli TokenFusion pada kedua dataset." Angka mIoU (56,8%; 57,7%; 60,2%; 60,9%; 52,7%; 53,3%; 54,8%), perbandingan FLOPs (17G vs 0,14G), hasil ablasi (53,3% → 55,4% → 56,3% → 56,8%), hasil deteksi 3D KITTI (88,49 AP), dan hasil translasi citra Taskonomy diambil dari ringkasan pihak ketiga atas makalah (bukan pembacaan langsung tabel PDF asli) dan sebaiknya diverifikasi ulang terhadap tabel resmi pada proceedings PMLR atau versi HTML arXiv sebelum dikutip dalam karya formal.
