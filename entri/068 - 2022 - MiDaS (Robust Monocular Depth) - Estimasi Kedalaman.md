# 068 - Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ranftl2022midas` |
| Judul asli | Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer |
| Penulis | René Ranftl, Katrin Lasinger, David Hafner, Konrad Schindler, Vladlen Koltun |
| Tahun | 2022 (praterbit arXiv 2019; diterima 2020) |
| Venue | IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), vol. 44, no. 3, hlm. 1623–1637 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1907.01341
- **Google Scholar:** https://scholar.google.com/scholar?q=Towards%20Robust%20Monocular%20Depth%20Estimation%3A%20Mixing%20Datasets%20for%20Zero-Shot%20Cross-Dataset%20Transfer
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Towards%20Robust%20Monocular%20Depth%20Estimation%3A%20Mixing%20Datasets%20for%20Zero-Shot%20Cross-Dataset%20Transfer&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan MiDaS, model estimasi kedalaman monokular (*monocular depth estimation* — memprediksi jarak setiap piksel ke kamera dari satu citra RGB tunggal) yang dirancang agar tetap akurat pada citra dari domain yang tidak pernah dilihat saat pelatihan. Gagasan intinya adalah melatih satu jaringan pada gabungan banyak *dataset* kedalaman yang saling berbeda jenis anotasi dan satuan skalanya. Penggabungan ini biasanya gagal karena setiap *dataset* mengukur kedalaman dengan cara dan satuan berbeda; makalah ini mengatasinya dengan *scale-and-shift-invariant loss*, yaitu fungsi galat yang mengabaikan perbedaan skala dan pergeseran absolut sehingga jaringan hanya dituntut memprediksi struktur kedalaman relatif yang benar.

Hasil utamanya adalah generalisasi *zero-shot* (kemampuan bekerja pada *dataset* yang sama sekali tidak muncul dalam pelatihan) yang jauh melampaui model sebelumnya. Model dilatih pada lima sumber data heterogen dan diuji pada enam *dataset* uji yang seluruhnya disisihkan dari pelatihan. Karena keluarannya kokoh lintas domain dan bobotnya dirilis terbuka, MiDaS menjadi penyedia *pseudo-depth* (peta kedalaman hasil prediksi yang dipakai sebagai pengganti sensor kedalaman) yang banyak dipakai pada pekerjaan lanjutan, termasuk penyusunan masukan RGB-D tanpa sensor fisik.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular bersifat *ill-posed*: satu citra dua dimensi dapat berasal dari tak terhingga banyak susunan tiga dimensi, sehingga model harus belajar penanda kedalaman statistik (ukuran objek relatif, oklusi, tekstur, perspektif) dari data. Kualitas model karena itu bergantung pada keragaman data pelatihannya. Model yang dilatih hanya pada satu *dataset* — misalnya NYU Depth v2 untuk ruang dalam atau KITTI untuk jalan raya — bekerja baik pada domain itu tetapi merosot tajam pada citra di luar domainnya, sebagaimana ditunjukkan pada bab 062 (Eigen dkk.) dan bab 065 (BTS).

Solusi yang jelas adalah memperbanyak dan memperagam data pelatihan. Kendalanya bersifat teknis: setiap *dataset* kedalaman mencatat kebenaran acuannya dengan cara berbeda. Sensor LiDAR menghasilkan kedalaman metrik (dalam meter) tetapi jarang; kamera stereo menghasilkan disparitas (*disparity* — pergeseran piksel antar-pandangan yang berbanding terbalik dengan kedalaman) tetapi hanya relatif dan sering tak terkalibrasi; anotasi manusia hanya memberi urutan relatif (objek A lebih dekat daripada B). Menggabungkan sumber-sumber ini secara naif berarti memaksa jaringan mencocokkan angka yang satuannya tidak sebanding — satu *dataset* mungkin menyatakan kedalaman dalam meter, yang lain dalam disparitas piksel dengan faktor skala dan pergeseran yang tidak diketahui. Galat yang dihitung langsung dari selisih angka menjadi tidak bermakna.

## Ide Utama

Pemecahannya berangkat dari satu pengamatan: untuk banyak penerapan, yang dibutuhkan bukan kedalaman metrik absolut, melainkan struktur kedalaman relatif yang benar (mana lebih dekat, seberapa kali lebih dekat). Bila target pelatihan cukup berupa kedalaman relatif, maka perbedaan skala dan pergeseran antar-*dataset* dapat dinetralkan sebelum galat dihitung.

MiDaS memprediksi kedalaman dalam ruang disparitas (kebalikan kedalaman, d = 1/kedalaman), lalu menyelaraskan prediksi ke setiap kebenaran acuan dengan dua parameter per citra: sebuah faktor skala dan sebuah pergeseran. Kedua parameter itu tidak dipelajari jaringan, melainkan dihitung tertutup (*closed-form*, rumus langsung tanpa iterasi) melalui pencocokan kuadrat terkecil terhadap kebenaran acuan pada setiap citra. Setelah prediksi diselaraskan, galat sisanya barulah dihitung. Dengan cara ini jaringan bebas memakai skala internalnya sendiri; ia hanya dihukum bila susunan kedalaman relatifnya salah. Formulasi inilah yang memungkinkan lima *dataset* dengan satuan berlainan dilatih bersama dalam satu fungsi galat yang konsisten.

## Cara Kerja Langkah demi Langkah

Alur menyeluruh dari beragam sumber data ke satu jaringan bersama dapat digambarkan sebagai berikut:

```
  Sumber data heterogen              Jaringan &            Penyelarasan per-citra
  (skala/anotasi berbeda)            keluaran              lalu galat
  ┌─────────────────────┐
  │ stereo film 3D      │──┐
  │ (disparitas)        │  │        ┌──────────┐         prediksi disparitas d*
  ├─────────────────────┤  │        │ encoder  │              │
  │ ReDWeb, WSVD        │  ├──citra─▶│ ResNeXt  │──▶ d* ──▶  cari skala s & geser t
  │ (disparitas web)    │  │        │ + dekoder│           (kuadrat terkecil ke GT)
  ├─────────────────────┤  │        └──────────┘              │
  │ MegaDepth, DIML     │──┘                            galat = | s·d* + t − d_GT |
  │ (SfM / RGB-D)       │                               (varian trimmed: buang
  └─────────────────────┘                                20% residual terbesar)
```

Diagram di atas menunjukkan tiga tahap: sumber data dengan anotasi berbeda masuk ke satu jaringan yang sama, jaringan mengeluarkan prediksi disparitas, dan prediksi itu diselaraskan ke kebenaran acuan masing-masing citra sebelum galatnya dihitung.

### Ruang Disparitas dan Penyelarasan Skala–Pergeseran

Jaringan memprediksi disparitas, bukan kedalaman langsung. Alasannya, disparitas berbanding lurus dengan kebalikan kedalaman, sehingga objek jauh (kedalaman besar) memetakan ke nilai kecil mendekati nol — rentang ini lebih mudah dipelajari dan lebih stabil secara numerik daripada kedalaman yang bisa membesar tak terbatas. Untuk setiap citra, misalkan prediksi d* dan kebenaran acuan d. Sistem mencari skala s dan pergeseran t yang meminimalkan jumlah kuadrat (s·d* + t − d)² atas seluruh piksel valid. Karena hanya ada dua peubah, penyelesaiannya berupa rumus aljabar linear langsung. Nilai s dan t inilah yang menyerap perbedaan satuan: sebuah *dataset* dalam meter dan sebuah *dataset* dalam disparitas piksel akan menerima s dan t yang berbeda, tetapi galat sisanya diukur dalam kerangka yang sama.

### Scale-and-Shift-Invariant Loss dan Varian Robust

Fungsi galat utama adalah rata-rata selisih absolut antara prediksi terselaraskan dan kebenaran acuan. Karena penyelarasan menghapus skala dan pergeseran, galat ini disebut *scale-and-shift-invariant*. Masalah tersisa adalah data yang bising: disparitas dari film atau web mengandung anotasi keliru pada tepi objek dan daerah oklusi. Untuk itu makalah memakai varian *trimmed* (dipangkas), yaitu galat yang membuang sekitar 20% piksel dengan residual terbesar sebelum merata-ratakan. Piksel bermasalah, yang biasanya menghasilkan residual ekstrem, dengan demikian tidak mendominasi gradien. Perbandingan pada makalah menunjukkan varian *trimmed* menghasilkan galat validasi terendah di seluruh *dataset* dibandingkan galat tak-dipangkas.

### Penajam Tepi Multiskala

Galat absolut saja cenderung menghasilkan peta kedalaman yang kabur pada batas objek. Karena itu ditambahkan suku pencocokan gradien multiskala (*multi-scale gradient matching*): selisih gradien spasial antara prediksi dan kebenaran acuan dihitung pada beberapa resolusi. Suku ini mendorong prediksi tajam tepat di batas benda dan mulus di dalam permukaan, sehingga peta kedalaman mempertahankan struktur objek.

### Pencampuran Multi-Dataset via Optimasi Multi-Objektif

Lima *dataset* pelatihan berbeda ukuran dan kesulitannya, sehingga satu rasio pencampuran tetap tidak akan optimal untuk semuanya. Makalah memperlakukan galat pada tiap *dataset* sebagai tujuan terpisah dan menyeimbangkannya dengan pendekatan optimasi multi-objektif (mencari titik kompromi Pareto — keadaan saat memperbaiki satu *dataset* mesti mengorbankan yang lain). Dengan ini bobot antar-*dataset* ditetapkan secara berprinsip, bukan disetel manual.

### Sumber Data dan Encoder

Lima sumber pelatihan adalah ReDWeb, DIML, MegaDepth, WSVD, dan koleksi film tiga dimensi (*3D Movies*). Sumber terakhir merupakan kontribusi data baru makalah ini: pasangan stereo dari film layar lebar diolah menjadi disparitas melalui aliran optik, menyediakan citra beragam dalam jumlah besar tanpa biaya anotasi. Tulang punggung (*backbone*) jaringan adalah ResNeXt-101 yang dipralatih secara lemah-terawasi pada data gambar berlabel-tagar dalam jumlah sangat besar; makalah menegaskan bahwa pemilihan pralatih encoder ini berdampak nyata pada generalisasi akhir.

## Eksperimen dan Hasil

Protokol evaluasi adalah *zero-shot cross-dataset transfer*: model dilatih pada sumber-sumber di atas, lalu diuji pada enam *dataset* yang seluruhnya disisihkan dari pelatihan — DIW, ETH3D, Sintel, KITTI, NYU Depth v2, dan TUM-RGBD. Karena tak satu pun *dataset* uji ikut dilatih, kinerjanya mengukur generalisasi murni, bukan hafalan domain.

Metrik disesuaikan dengan jenis kebenaran acuan tiap *dataset*. Untuk DIW yang hanya beranotasi urutan relatif dipakai WHDR (*Weighted Human Disagreement Rate* — persentase pasangan titik yang urutan kedalamannya diprediksi terbalik; makin kecil makin baik). Untuk *dataset* berkebenaran padat dipakai galat relatif seperti AbsRel (*Absolute Relative error*) dan δ>1,25 (persentase piksel dengan galat di bawah ambang), dihitung setelah prediksi diselaraskan skala dan pergeserannya. Makalah melaporkan bahwa MiDaS mengungguli metode pembanding secara konsisten di seluruh enam *dataset* uji dan menetapkan hasil terbaik saat itu untuk estimasi kedalaman relatif lintas domain. Ablasi memperkuat dua klaim: penambahan jumlah *dataset* pelatihan menurunkan galat *zero-shot*, dan galat *scale-and-shift-invariant* varian *trimmed* mengungguli alternatifnya. Angka spesifik per *dataset* pada tabel makalah tidak dikutip di sini dan perlu diperiksa ke naskah asli sebelum sitasi formal.

## Kelebihan dan Keterbatasan

Kelebihan utamanya adalah generalisasi lintas domain yang kokoh dari satu model tunggal, dicapai lewat mekanisme yang secara prinsip memungkinkan penggabungan *dataset* dengan anotasi tak sebanding. Rilis bobot terbuka membuat model langsung dapat dipakai, dan keluaran disparitas relatifnya cukup untuk banyak tugas hilir.

Keterbatasan pokoknya melekat pada rumusan: karena galat pelatihan invarian terhadap skala dan pergeseran, keluaran MiDaS adalah kedalaman relatif, bukan metrik. Untuk memperoleh jarak dalam meter diperlukan kalibrasi tambahan dari sumber luar (dua parameter skala–pergeseran harus ditaksir per adegan). Dari sisi rekayasa, ketergantungan pada disparitas dari film dan web membuat kualitas pada daerah oklusi dan objek transparan bergantung pada kualitas aliran optik yang menghasilkannya. Secara konseptual, kualitas akhir juga terikat pada kapasitas *backbone*; makalah menunjukkan encoder yang lebih kuat memberi hasil lebih baik, yang kelak dieksploitasi oleh varian berbasis *transformer* pada bab 067 (DPT).

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis estimasi kedalaman monokular yang dibuka pada [bab 062 (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md), yang memperkenalkan prediksi kedalaman dari citra tunggal beserta galat invarian-skala versi awal. MiDaS memperluas gagasan invariansi itu menjadi invariansi skala sekaligus pergeseran dan memakainya untuk menggabungkan banyak *dataset*. Berbeda dengan [bab 064 (Monodepth2)](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) yang mengejar kedalaman lewat swa-pengawasan pada satu domain video, MiDaS mengejar keragaman lewat pencampuran data berlabel yang heterogen. Tulang punggung *transformer* yang menggantikan encoder konvolusi dikembangkan pada [bab 067 (DPT)](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md), yang memakai kerangka pelatihan MiDaS ini dan menjadi tulang punggung MiDaS versi berikutnya. Bagi tema tinjauan yang lebih luas, kemampuan MiDaS menghasilkan *pseudo-depth* murah dari citra RGB biasa menjadikannya jembatan menuju masukan RGB-D tanpa sensor fisik.

## Poin untuk Sitasi

Kutip dengan kunci `ranftl2022midas`. Ringkasan yang aman dikutip: "MiDaS melatih estimasi kedalaman monokular pada gabungan lima *dataset* heterogen memakai *scale-and-shift-invariant loss* di ruang disparitas, mencapai generalisasi *zero-shot* lintas domain terbaik pada masanya dan menjadi penyedia *pseudo-depth* yang banyak dipakai." Fakta terverifikasi dari sumber primer: lima sumber pelatihan (ReDWeb, DIML, MegaDepth, WSVD, film 3D), enam *dataset* uji *zero-shot* (DIW, ETH3D, Sintel, KITTI, NYU Depth v2, TUM-RGBD), *backbone* ResNeXt-101 pralatih lemah-terawasi, galat *scale-and-shift-invariant* varian *trimmed*, suku gradien multiskala, dan penyeimbangan multi-objektif antar-*dataset*. Yang belum terverifikasi dan perlu diperiksa ke naskah asli sebelum sitasi formal: angka kuantitatif per *dataset* (WHDR, AbsRel, δ) dan margin numerik terhadap tiap metode pembanding, karena tabel hasil tidak berhasil diambil dari sumber selama penyusunan bab ini.
