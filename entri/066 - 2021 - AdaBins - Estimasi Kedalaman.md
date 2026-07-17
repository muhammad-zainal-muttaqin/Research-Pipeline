# 066 - AdaBins: Depth Estimation Using Adaptive Bins

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bhat2021adabins` |
| Judul asli | AdaBins: Depth Estimation Using Adaptive Bins |
| Penulis | Shariq Farooq Bhat, Ibraheem Alhashim, Peter Wonka |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2011.14141
- **DOI (versi penerbit):** https://doi.org/10.1109/CVPR46437.2021.00400
- **Kode sumber resmi:** https://github.com/shariqfarooq123/AdaBins
- **Google Scholar:** https://scholar.google.com/scholar?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan AdaBins, sebuah blok arsitektur untuk memprediksi peta kedalaman rapat (*dense depth map*) dari satu citra RGB, yaitu tugas menetapkan satu nilai jarak kamera untuk setiap piksel. Masalah yang diserang adalah cara jaringan memperlakukan rentang kedalaman: metode regresi langsung dan metode klasifikasi dengan pembagian rentang yang tetap sama-sama mengabaikan kenyataan bahwa distribusi nilai kedalaman sangat berbeda antar-citra. Citra furnitur dari jarak dekat memusat pada kedalaman kecil, sedangkan citra koridor menyebar sampai kedalaman maksimum.

Gagasan utamanya adalah membagi rentang kedalaman menjadi N *bin* (sub-rentang) yang lebarnya dihitung ulang secara adaptif untuk setiap citra masukan oleh sebuah modul *Transformer* kecil bernama mini-ViT. Kedalaman akhir setiap piksel bukan hasil memilih satu bin, melainkan kombinasi linear berbobot *softmax* dari pusat seluruh bin. Dengan desain ini, model mencapai akurasi terbaik pada masanya di dua tolok ukur utama: akurasi ambang δ < 1,25 sebesar 0,903 pada NYU Depth v2 dan 0,964 pada KITTI, mengungguli pembanding kuat seperti BTS dan DAV pada semua metrik yang dilaporkan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular adalah masalah *ill-posed*: satu citra dapat bersesuaian dengan banyak geometri adegan yang berbeda, sehingga jaringan harus memanfaatkan statistik dan konteks adegan, bukan hanya isyarat lokal. Sejak Eigen dkk. (bab 062) memperkenalkan regresi kedalaman dengan CNN multi-skala pada 2014, pendekatan dominan memprediksi satu nilai kontinu per piksel secara langsung. Fu dkk. (2018) lewat metode DORN menempuh jalan lain: regresi diubah menjadi klasifikasi ordinal dengan membagi rentang kedalaman menjadi sejumlah *bin* berlebar tetap, dan kedalaman piksel ditetapkan dari bin yang menang. Akurasi metriknya membaik, tetapi karena setiap piksel dipetakan ke tepat satu bin, peta kedalaman mengandung artefak diskretisasi berupa diskontinuitas tajam yang mengganggu aplikasi lanjutan seperti rekonstruksi 3D.

Dua metode terkuat menjelang 2021, yaitu BTS (bab 065) dengan *local planar guidance* dan DAV dengan atensi koplanaritas, bergantung pada asumsi bahwa permukaan adegan cenderung planar — asumsi yang tidak selalu berlaku, terutama di luar ruangan. Ada pula masalah arsitektural yang lebih umum: pada arsitektur konvolusi biasa, informasi global baru terolah setelah tensor menyusut ke resolusi spasial sangat rendah di sekitar *bottleneck* (titik tersempit jaringan). Padahal distribusi kedalaman berbeda tajam antar-citra, dan analisis global atas distribusi tersebut jauh lebih berguna bila dilakukan pada resolusi tinggi, ketika informasi spasial masih utuh.

## Ide Utama

AdaBins memperbaiki skema bin melalui tiga perubahan. Pertama, lebar bin tidak ditetapkan di muka dan tidak pula satu pembagian untuk seluruh dataset, melainkan dihitung ulang untuk setiap citra oleh modul *Transformer* yang membaca fitur seluruh adegan — jaringan sendiri yang memutuskan bagian rentang kedalaman mana yang layak mendapat resolusi halus. Kedua, kedalaman piksel bukan pusat bin pemenang, melainkan nilai harapan atas semua pusat bin dengan bobot probabilitas *softmax*; keluaran tetap kontinu sehingga artefak diskretisasi hilang. Ketiga, pemrosesan global ini ditempatkan setelah dekoder pada tensor beresolusi setengah citra, bukan di *bottleneck*. Masukan blok adalah tensor fitur hasil dekode; keluarannya adalah vektor lebar bin dan satu set peta perhatian; keduanya digabungkan menjadi peta kedalaman.

## Cara Kerja Langkah demi Langkah

### Baseline Encoder-Decoder

Komponen pertama adalah jaringan *encoder-decoder* konvensional yang diadaptasi dari arsitektur Alhashim dan Wonka: *encoder* menurunkan resolusi citra sambil mengekstrak fitur, *decoder* menaikkannya kembali secara bertahap. Enkoder memakai EfficientNet-B5, jaringan konvolusi yang skala lebar, kedalaman, dan resolusinya diseimbangkan menurut satu koefisien majemuk. Berbeda dari jaringan dasar tersebut, keluaran dekoder bukan peta kedalaman, melainkan tensor fitur terdekode berukuran h × w × Cd dengan h = H/2 dan w = W/2 (setengah resolusi citra masukan, demi menghemat memori GPU). Kedalaman akhir diperoleh dengan *upsampling* bilinear dua kali pada tahap paling akhir.

### Mini-ViT: Penentu Lebar Bin Adaptif

Blok AdaBins diawali mini-ViT, versi kecil dari *Vision Transformer* — arsitektur berbasis mekanisme atensi yang memroses sekuens vektor dan memungkinkan setiap elemen sekuens saling memperhatikan tanpa konvolusi. Fitur terdekode dilewatkan konvolusi berkernel p × p dengan *stride* p (p = 16), menghasilkan tensor h/p × w/p × E yang diratakan menjadi sekuens S = hw/p² vektor berdimensi E = 128 yang disebut *patch embedding*. Setelah ditambah enkoding posisi yang dipelajari, sekuens ini diproses *encoder Transformer* kecil (4 lapis, 4 kepala atensi, MLP 1024). Sebuah *MLP head* beraktivasi ReLU membaca embedding keluaran pertama dan menghasilkan vektor N dimensi b′, yang dinormalisasi menjadi lebar bin b_i = (b′_i + ε) / Σ_j(b′_j + ε) dengan ε = 10⁻³, sehingga jumlah seluruh lebar bin tepat satu.

Normalisasi ini menciptakan kompetisi: memperlebar satu bin harus mengorbankan bin lain. Jaringan dengan demikian didorong menempatkan bin sempit pada sub-rentang yang padat nilai kedalaman dan bin lebar pada sub-rentang yang jarang. Pada citra koridor, bin menyebar sampai kedalaman maksimum; pada citra furnitur jarak dekat, bin terkonsentrasi di sekitar 1–2 meter. Pusat setiap bin dihitung sebagai c(b_i) = dmin + (dmax − dmin)(b_i/2 + Σ_{j<i} b_j). Sebagai contoh, pada rentang D = (0, 10) meter: bila b_1 = 0,2 maka c(b_1) = 10 × 0,1 = 1,0 meter, dan bila b_2 = 0,1 maka c(b_2) = 10 × (0,05 + 0,2) = 2,5 meter.

### Range-Attention-Maps

Keluaran kedua mini-ViT adalah *Range-Attention-Maps* (R). Embedding keluaran ke-2 sampai ke-(C+1) dari Transformer dipakai sebagai kernel konvolusi 1 × 1 yang dikonvolusikan dengan fitur terdekode (setelah satu konvolusi 3 × 3), menghasilkan tensor R berukuran h × w × C. Operasi ini setara dengan atensi hasil kali titik: fitur setiap piksel berperan sebagai *key* dan embedding Transformer sebagai *query*. Dengan cara ini, informasi global yang diolah Transformer disuntikkan ke informasi lokal setiap piksel pada resolusi tinggi.

### Regresi Hibrida

Tensor R dilewatkan konvolusi 1 × 1 menjadi N kanal, lalu diaktifkan *softmax* sehingga setiap piksel memiliki distribusi probabilitas p_k atas N pusat bin. Kedalaman piksel dihitung sebagai kombinasi linear d̃ = Σ_k c(b_k) · p_k. Misalnya sebuah piksel dengan p = (0,7; 0,3) pada pusat bin 2,0 meter dan 2,5 meter memperoleh d̃ = 0,7 × 2,0 + 0,3 × 2,5 = 2,15 meter — nilai kontinu yang tidak terkunci pada pusat bin mana pun, sehingga peta kedalaman halus tanpa tingkatan diskrit.

Alur lengkap dari citra ke kedalaman:

```
citra RGB  H x W x 3
     |
     v
+------------------------------------------+
| encoder EfficientNet-B5  +  decoder      |
+------------------------------------------+
     | fitur terdekode h x w x Cd  (h = H/2, w = W/2)
     v
+------------------------------------------+
| mini-ViT (Transformer, 4 lapis)          |
+------------------------------------------+
     |
     +-> vektor lebar bin b (jumlah = 1) -> pusat bin c(b)
     +-> Range-Attention-Maps R -> conv 1x1 -> softmax p
     v
+------------------------------------------+
| regresi hibrida:  d = sum p_k * c(b_k)   |
+------------------------------------------+
     | peta kedalaman h x w x 1
     v
 upsampling bilinear x2  ->  kedalaman akhir H x W x 1
```

Diagram di atas memperlihatkan dua keluaran mini-ViT yang menyatu pada tahap regresi hibrida: lebar bin menentukan posisi pusat bin pada rentang kedalaman, sedangkan R menentukan bobot per piksel atas pusat-pusat tersebut.

### Fungsi Loss

Pelatihan memakai dua suku. Suku pertama adalah versi berskala dari *scale-invariant loss* Eigen dkk.: dengan g_i = log d̃_i − log d_i, loss dihitung dari rata-rata kuadrat g_i dikurangi λ kali kuadrat rata-ratanya (λ = 0,85, dikali faktor skala μ = 10); bentuk ini menghukum ketidakkonsistenan galat log antar-piksel sehingga tidak sensitif terhadap galat skala global. Suku kedua adalah loss densitas pusat bin berupa *Chamfer loss* dua arah antara himpunan pusat bin dan himpunan nilai kedalaman kebenaran dasar (*ground truth*): setiap pusat bin didorong mendekati nilai kedalaman yang benar-benar ada pada citra, dan sebaliknya. Loss total adalah L_total = L_pixel + 0,1 · L_bins.

### Pelatihan

Model dilatih dengan pengoptimal AdamW (*weight decay* 10⁻²), kebijakan laju pembelajaran 1-*cycle* dengan maksimum 3,5 × 10⁻⁴, selama 25 epoch dengan *batch* 16 — sekitar 20 menit per epoch pada empat GPU V100 32 GB. Model berisi ±78 juta parameter: 28 juta pada enkoder, 44 juta pada dekoder, dan 5,8 juta pada modul AdaBins. Saat pengujian, kedalaman akhir adalah rata-rata prediksi citra asli dan prediksi citra cerminnya.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tiga dataset. NYU Depth v2 memuat 654 citra uji dalam ruangan (resolusi 640 × 480, kedalaman maksimum 10 meter); model dilatih pada subset 50 ribu citra. KITTI memuat adegan luar ruangan dari kendaraan bergerak; pelatihan memakai ±26 ribu citra dan pengujian 697 citra menurut pemisahan Eigen, pada rentang 0–80 meter. SUN RGB-D (5.050 citra uji) hanya dipakai untuk uji silang tanpa penyetelan ulang. Metrik yang dipakai: akurasi ambang δ < 1,25 (persentase piksel yang rasio terburuknya terhadap kebenaran dasar di bawah 1,25; makin besar makin baik), AbsRel (rata-rata galat relatif absolut; makin kecil makin baik), RMSE (akar rata-rata kuadrat galat), serta SqRel (kuadrat galat relatif) untuk KITTI.

Hasil utama:

- **NYU Depth v2:** δ1 = 0,903; AbsRel = 0,103; RMSE = 0,364. Pembanding terkuat sebelumnya, BTS, mencapai 0,885 / 0,110 / 0,392 dan DAV 0,882 / 0,108 / 0,412. Artinya, 90,3% piksel prediksi AdaBins menyimpang kurang dari 25% dari kebenaran dasar, galat relatif turun sekitar 6% dari pesaing terbaik, dan RMSE turun sekitar 7%.
- **KITTI:** δ1 = 0,964; AbsRel = 0,058; RMSE = 2,360; SqRel = 0,190, dibandingkan BTS 0,956 / 0,059 / 2,756 / 0,245. Makalah melaporkan perbaikan RMSE sekitar 13,5% dan SqRel 22,4% terhadap keadaan seni sebelumnya; penurunan galat kuadrat yang besar menandakan galat besar pada piksel jarak jauh berhasil ditekan.
- **SUN RGB-D (uji silang):** AbsRel = 0,159 dan δ1 = 0,771, dibandingkan BTS 0,172 dan 0,740. Model yang dilatih di NYU menggeneralisasi lebih baik ke sensor dan adegan baru, meskipun galatnya tetap jauh di atas pengujian dalam-domain (0,103).

Studi ablasi pada NYU mengukur sumbangan tiap pilihan desain (δ1 / AbsRel / RMSE): regresi standar tanpa modul 0,881 / 0,111 / 0,419; bin tetap seragam 0,892 / 0,107 / 0,383; bin tetap skala log 0,896 / 0,108 / 0,379; bin terlatih tetapi tetap untuk semua citra 0,893 / 0,109 / 0,381; AdaBins penuh 0,903 / 0,103 / 0,364. Semua varian berbasis bin mengungguli regresi standar, tetapi hanya bin adaptif per citra yang memberi lompatan besar — bukti bahwa adaptasi terhadap distribusi kedalaman spesifik citra adalah sumber utama perbaikan. Penambahan loss Chamfer menurunkan AbsRel dari 0,106 menjadi 0,103. Jumlah bin ditetapkan N = 256 karena perbaikan di atas nilai itu jenuh.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah adaptivitas tanpa asumsi geometris: berbeda dari BTS dan DAV, tidak ada asumsi planaritas yang dapat dilanggar adegan nyata. Regresi hibrida menghilangkan artefak diskretisasi metode bin tetap seperti DORN, pemrosesan global dilakukan pada resolusi tinggi, dan kode beserta bobot terlatih dirilis publik.

Keterbatasannya: (1) metode ini *supervised* penuh dan membutuhkan kebenaran dasar kedalaman rapat, kontras dengan jalur *self-supervised* Monodepth2 (bab 064); (2) rentang (dmin, dmax) dan jumlah bin N harus ditetapkan manual per dataset; (3) modul global menambah 5,8 juta parameter dan komputasi atensi pada resolusi tinggi — dari sisi rekayasa, total 78 juta parameter lebih berat dari BTS (47 juta) dan DAV (25 juta); (4) secara konseptual, generalisasi lintas dataset tetap terbatas, terlihat dari kenaikan AbsRel dari 0,103 menjadi 0,159 pada uji silang SUN RGB-D.

## Kaitan dengan Bab Lain

Bab ini mewarisi dua hal dari [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md): loss *scale-invariant* dan protokol pemisahan data uji yang menjadi standar evaluasi. Posisinya merupakan jawaban langsung atas keterbatasan regresi murni yang dipakai [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md), pembanding utamanya, sekaligus penyempurnaan skema bin tetap DORN. Jalurnya berseberangan dengan [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) yang mengejar akurasi tanpa label kedalaman. Pada tahun yang sama, [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md) membawa Transformer ke prediksi rapat dengan cara berbeda — mengganti *backbone* konvolusi sepenuhnya — sehingga kedua bab ini menandai masuknya Transformer ke estimasi kedalaman.

## Poin untuk Sitasi

Kutip dengan kunci `bhat2021adabins`. Ringkasan yang aman dikutip: "AdaBins membagi rentang kedalaman menjadi bin yang lebarnya diprediksi secara adaptif per citra oleh modul Transformer, dan menghitung kedalaman piksel sebagai kombinasi linear pusat bin; metode ini melampaui keadaan seni pada NYU Depth v2 (δ1 = 0,903, AbsRel = 0,103) dan KITTI (δ1 = 0,964, AbsRel = 0,058) pada semua metrik standar." Seluruh angka di bab ini diverifikasi dari naskah CVPR 2021 versi *open access*; satu hal yang perlu diperiksa ulang sebelum sitasi formal adalah klaim "perbaikan RMSE 13,5%" pada KITTI, karena naskah tidak menyebut eksplisit pembanding acuan persentase tersebut pada kalimat klaimnya.
