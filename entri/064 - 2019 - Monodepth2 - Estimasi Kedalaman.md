# 064 - Digging into Self-Supervised Monocular Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `godard2019monodepth2` |
| Judul asli | Digging into Self-Supervised Monocular Depth Estimation |
| Penulis | Clément Godard, Oisin Mac Aodha, Michael Firman, Gabriel J. Brostow |
| Tahun | 2019 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2019) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1806.01260
- **Repositori kode resmi (Niantic Labs):** https://github.com/nianticlabs/monodepth2
- **Google Scholar:** https://scholar.google.com/scholar?q=Digging%20into%20Self-Supervised%20Monocular%20Depth%20Estimation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Digging%20into%20Self-Supervised%20Monocular%20Depth%20Estimation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Monodepth2, model yang memprediksi peta kedalaman (jarak setiap piksel ke kamera) dari satu citra RGB tunggal, dilatih secara *self-supervised* (swa-awas) tanpa data kedalaman kebenaran: sinyal pelatihannya adalah pasangan stereo atau rangkaian video monokular. Alih-alih memperbesar arsitektur, tiga perbaikan sederhana pada fungsi loss dan skema pelatihan cukup untuk melampaui seluruh metode swa-awas sebelumnya: loss reproyeksi minimum per piksel untuk menangani oklusi, *auto-masking* untuk membuang piksel stasioner yang melanggar asumsi gerak kamera, dan *multi-scale* resolusi penuh untuk menghilangkan artefak visual.

Pada tolok ukur KITTI (pembagian Eigen), model monokular penuh mencapai galat AbsRel 0,115 dengan 87,7% piksel di bawah ambang δ<1,25, dan varian gabungan mono-plus-stereo mencapai 0,106. Berkat kesederhanaan dan ketersediaan kodenya, Monodepth2 menjadi garis dasar (*baseline*) paling banyak dipakai dalam penelitian kedalaman monokular setelah 2019.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra adalah masalah *ill-posed*: satu citra yang sama dapat dihasilkan oleh tak terhingga susunan geometri tiga dimensi. Pendekatan terawasi (*supervised*), yang dimulai oleh Eigen dkk. (bab 062), mengatasi ambiguitas ini dengan belajar dari pasangan citra dan kedalaman kebenaran, tetapi data tersebut sulit diperoleh dalam skala besar — sensor LiDAR mahal dan hanya memberi titik-titik renggang.

Jalur alternatif adalah pelatihan swa-awas berbasis rekonstruksi citra: kedalaman diprediksi, lalu citra sumber (berangka stereo atau *frame* video tetangga) digeser (*warping*) ke posisi kamera citra target; selisih warna antara hasil warping dan citra target menjadi sinyal pelatihan. Garg dkk. (2016) dan Monodepth (bab 063) memakai pasangan stereo, sedangkan Zhou dkk. (2017) memakai video monokular dengan jaringan pose tambahan. Kualitas kedua jalur tertahan oleh tiga masalah: (1) oklusi — piksel yang terlihat di target tetapi tertutup di sumber menghasilkan galat besar yang menghukum prediksi kedalaman yang sebenarnya sudah benar; (2) objek bergerak searah dan secepat kamera, atau kamera yang berhenti, melanggar asumsi "kamera bergerak, dunia statis" dan menimbulkan lubang kedalaman tak hingga saat pengujian; (3) skema multi-skala lazim menghitung loss pada citra resolusi rendah sehingga menimbulkan artefak *texture-copy* (pola tekstur citra yang keliru menempel pada peta kedalaman).

## Ide Utama

Gagasan inti Monodepth2 adalah memperbaiki cara galat rekonstruksi dihitung, bukan memperbesar model. Masukannya satu citra target I(t) dan satu atau lebih citra sumber; keluarannya kedalaman per piksel D(t). Tiga perubahan diperkenalkan.

Pertama, galat fotometrik tidak lagi **dirata-ratakan** antar-sumber, melainkan diambil **nilai minimumnya** per piksel: piksel yang teroklusi di satu sumber cukup dicocokkan ke sumber tempat ia memang terlihat, sehingga batas oklusi menjadi tajam. Kedua, piksel yang tidak berubah penampilannya antar-*frame* — tanda kamera diam, objek bergerak seiring kamera, atau daerah tanpa tekstur — otomatis dibuang: loss dihitung hanya bila warping benar-benar memperbaiki rekonstruksi. Ketiga, peta disparitas (pergeseran piksel antar-pandangan, kebalikan kedalaman) dari tiap skala dekoder di-*upsampling* ke resolusi penuh sebelum loss dihitung, sehingga semua skala bekerja pada sasaran yang sama dan artefak resolusi rendah hilang.

## Cara Kerja Langkah demi Langkah

### Kerangka Swa-Awas sebagai Sintesis Pandangan Baru

Pelatihan dirumuskan sebagai sintesis pandangan baru (*novel view synthesis*): merekonstruksi citra target I(t) dari citra sumber I(t'). Diperlukan tiga hal: kedalaman D(t) yang diprediksi jaringan kedalaman, pose relatif antar-kamera T(t→t') (rotasi dan translasi 6 derajat kebebasan), dan parameter internal kamera K (titik utama dan panjang fokus). Setiap piksel target diproyeksikan ke citra sumber memakai ketiganya; warna pada koordinat hasil proyeksi diambil dengan *bilinear sampling* (interpolasi antar empat piksel tetangga yang dapat diturunkan, sehingga gradien tetap mengalir). Untuk pelatihan monokular, sumbernya dua *frame* tetangga dan pose diprediksi jaringan terpisah; untuk stereo, sumbernya citra pasangan kamera kanan dengan pose diketahui dari kalibrasi; untuk gabungan (MS), keduanya dipakai sekaligus.

Galat fotometrik (*photometric reprojection error*) per piksel adalah gabungan dua ukuran kemiripan: pe = (α/2)·(1 − SSIM) + (1 − α)·‖Ia − Ib‖₁, dengan α = 0,85. SSIM (*Structural Similarity Index*) mengukur kemiripan struktur lokal dan lebih tahan terhadap perubahan pencahayaan daripada selisih piksel mentah; ‖·‖₁ adalah selisih absolut L1. Selain itu dipakai loss kehalusan (*edge-aware smoothness*) Ls yang menghukum perbedaan kedalaman antar-piksel tetangga kecuali di tepi citra — bobotnya mengecil secara eksponensial mengikuti gradien warna — sehingga kedalaman boleh melompat tepat di batas objek. Kedalaman dalam Ls dinormalkan terhadap rata-ratanya agar jaringan tidak mengecilkan seluruh prediksi demi memperkecil loss.

### Arsitektur Kedalaman dan Pose

Jaringan kedalaman adalah U-Net: arsitektur enkoder-dekoder konvolusional dengan *skip connection* (sambungan pintas yang menyalin fitur enkoder ke dekoder pada resolusi yang sama). Enkodernya ResNet18 — jaringan residual 18 lapis dengan 11 juta parameter — yang diinisialisasi dari bobot *pretraining* ImageNet. Dekoder mengikuti desain Monodepth (bab 063): aktivasi *sigmoid* pada keluaran, yang dikonversi menjadi kedalaman melalui D = 1/(a·σ + b) dengan a dan b dipilih agar kedalaman terbatas pada rentang 0,1 sampai 100 satuan; *reflection padding* (bantalan yang memantulkan piksel tepi) menekan artefak di batas citra. Jaringan pose adalah ResNet18 lain yang dimodifikasi untuk menerima dua citra bertumpuk (6 kanal) dan mengeluarkan satu pose relatif 6 derajat kebebasan.

### Loss Reproyeksi Minimum per Piksel

Perata-rataan galat ke seluruh sumber gagal pada piksel tepi citra yang keluar bidang pandang akibat gerak kamera dan pada piksel yang teroklusi di salah satu sumber. Monodepth2 mengganti rata-rata dengan operator minimum per piksel. Contoh numerik: bila sebuah piksel bergalat 0,40 terhadap I(t-1) tetapi hanya 0,05 terhadap I(t+1) karena tertutup objek lain di *frame* sebelumnya, rata-rata memberi 0,225 dan mendorong jaringan "memperbaiki" kedalaman yang sudah benar; minimum memberi 0,05 dan membiarkan kedalaman itu apa adanya. Hasilnya: artefak tepi citra berkurang dan batas oklusi lebih tajam.

### Auto-Masking Piksel Stasioner

Masker biner μ ∈ {0,1} dihitung otomatis pada *forward pass*, tanpa jaringan tambahan. Aturannya: μ = 1 hanya bila galat reproyeksi hasil warping lebih kecil daripada galat terhadap citra sumber asli yang tidak di-*warp*. Piksel yang penampilannya identik antar-*frame* — kamera berhenti, atau objek bergerak dengan kecepatan relatif sama terhadap kamera — memiliki galat tanpa-*warp* yang sudah rendah, sehingga μ = 0 dan piksel itu tidak menyumbang loss. Bila kamera benar-benar diam, seluruh piksel satu *frame* dapat terbuang sekaligus. Loss akhirnya L = μ·Lp + λ·Ls dengan λ = 0,001, dirata-ratakan atas piksel, skala, dan *batch*.

### Multi-Skala Resolusi Penuh

Dekoder mengeluarkan disparitas pada beberapa skala agar pelatihan tidak terjebak minimum lokal. Alih-alih menghitung loss fotometrik pada citra yang ikut diperkecil ke resolusi tiap skala, Monodepth2 meng-*upsampling* peta disparitas resolusi rendah ke resolusi masukan penuh terlebih dahulu, baru kemudian menghitung galatnya. Satu nilai disparitas resolusi rendah dengan demikian meng-*warp* satu petak piksel resolusi penuh — setara pencocokan petak (*patch matching*) klasik — dan semua skala mengejar sasaran yang sama: merekonstruksi citra target seakurat mungkin.

Alur pelatihan monokular secara keseluruhan:

```
 I(t-1) ─┐
         ├─> [jaringan pose: ResNet18, 6 kanal] ─> pose relatif T(t->t')
 I(t+1) ─┘                                            |
                                                      v
 I(t) ──> [jaringan kedalaman: U-Net + ResNet18] ─> D(t) ─> [proyeksi +
            11 juta parameter, keluaran multi-skala        sampling
                                                            bilinear]
                                                                |
            galat fotometrik per piksel per sumber <------------+
            pe = 0,425 x (1 - SSIM) + 0,15 x |Ia - Ib|
                            |
         ┌──────────────────┼───────────────────┐
         v                  v                   v
  Lp = min antar-sumber  mu = 1 hanya jika   tiap skala di-upsampling
  (anti-oklusi)          pe warp < pe tanpa  ke resolusi penuh sebelum
                         warp (piksel diam   pe dihitung
                         dibuang)
         └──────── L = mu x Lp + 0,001 x Ls ─────────┘
```

Jaringan pose hanya diperlukan saat pelatihan; saat pengujian cukup satu citra tunggal dilewatkan ke jaringan kedalaman. Model dilatih 20 *epoch* dengan pengoptimal Adam, *batch* 12 citra 640×192, laju pembelajaran 10⁻⁴ selama 15 *epoch* pertama lalu 10⁻⁵; waktu latih 8 jam (stereo), 12 jam (mono), dan 15 jam (gabungan) pada satu GPU Titan Xp.

## Eksperimen dan Hasil

Evaluasi utama memakai dataset KITTI dengan pembagian Eigen (pembelah data dari bab 062). Setelah penyaringan *frame* statis ala Zhou dkk., tersedia 39.810 triplet monokular untuk pelatihan dan 4.424 untuk validasi. Kedalaman dibatasi maksimum 80 meter sesuai praktik standar. Metrik yang dilaporkan: AbsRel (galat relatif absolut, rata-rata |prediksi − benar|/benar; makin kecil makin baik), RMSE (akar kuadrat galat rata-rata, sensitif pada galat besar), dan akurasi ambang δ<1,25 (persentase piksel dengan rasio prediksi/kebenaran di bawah 1,25; makin besar makin baik). Karena pelatihan monokular hanya menghasilkan kedalaman relatif, prediksi model mono diskalakan dengan median kedalaman kebenaran per citra uji (*median scaling*).

Hasil utama pada KITTI (resolusi 640×192): model monokular (M) mencapai AbsRel 0,115 dan δ<1,25 sebesar 87,7%; model stereo (S) 0,109 dan 86,4%; model gabungan (MS) 0,106 dan 87,4%. Ketiganya melampaui seluruh metode swa-awas sebelumnya, termasuk yang memodelkan gerak objek secara eksplisit dengan *optical flow* (Ranjan dkk., EPC++). RMSE model M sebesar 4,863 menunjukkan galat besar tersisa terkonsentrasi pada objek jauh; resolusi 1024×320 menurunkannya menjadi 4,701 dengan δ<1,25 87,9% — sebagian galat berasal dari resolusi, bukan metode.

Studi ablasi (mematikan komponen satu per satu, pelatihan mono) mengukuhkan sumbangan tiap bagian. Model dasar tanpa satu pun kontribusi bernilai AbsRel 0,140; menambahkan reproyeksi minimum saja menurunkannya ke 0,122, *auto-masking* saja ke 0,124, dan multi-skala resolusi penuh ke 0,124; gabungan ketiganya mencapai 0,115. Sebaliknya, membuang *auto-masking* dari model penuh menaikkan galat ke 0,120, dan menggantinya dengan masker prediktif Zhou dkk. justru menghasilkan 0,123 — lebih buruk daripada tanpa masker sama sekali. Pada pembagian Eigen penuh yang masih memuat *frame* kamera-diam, model dasar anjlok ke 0,146 sedangkan Monodepth2 tetap 0,116: *auto-masking* menghapus kebutuhan praproses *optical flow* untuk membuang *frame* statis. Tanpa *pretraining* ImageNet pun Monodepth2 (0,132) tetap jauh di atas model dasar (0,150). Pada dataset Make3D — evaluasi lintas domain tanpa pelatihan ulang — model ini mengalahkan semua metode yang tidak memakai supervisi kedalaman, bukti generalisasi di luar data latih.

## Kelebihan dan Keterbatasan

Kelebihannya adalah perbandingan biaya-manfaat: tiga kontribusi tidak menambah komponen terlatih baru dan murah dihitung, dengan sumbangan masing-masing terbukti pada ablasi. Model dapat dilatih dari video monokular biasa, stereo, atau keduanya, dan arsitekturnya (ResNet18) jauh lebih ringan daripada enkoder ResNet50/DispNet metode sebelumnya. Ketersediaan kode resmi membuatnya mudah direproduksi.

Keterbatasan tetap ada. Pertama, kedalaman monokular murni hanya terdefinisi sampai faktor skala yang tidak diketahui, sehingga evaluasinya masih bergantung pada *median scaling* terhadap data kebenaran. Kedua, penulis makalah sendiri menunjukkan kegagalan pada permukaan yang melanggar asumsi Lambertian — reflektif, transparan, atau jenuh warnanya — serta pada batas objek yang ambigu atau bentuk yang rumit. Ketiga, dari sisi rekayasa, *auto-masking* hanya menangani objek yang bergerak seiring kamera; objek yang bergerak bebas tetap merusak asumsi kekakuan dan tidak diselesaikan di sini. Keempat, secara konseptual, seluruh kerangka bergantung pada kemiripan penampilan antar-*frame*, sehingga perubahan pencahayaan besar atau adegan malam berada di luar jangkauannya tanpa modifikasi.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis swa-awas sebagai lawan kutub jalur terawasi yang dimulai [062 - Depth dari Citra Tunggal (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md) — pembagian data Eigen yang dipakai di sini dinamai dari makalah tersebut — dan secara langsung menyempurnakan [063 - Monodepth (Left-Right Consistency)](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md): loss fotometrik SSIM+L1, kehalusan sadar-tepi, dan desain dekoder diwarisi, sedangkan konsistensi kiri-kanan digantikan oleh reproyeksi minimum yang lebih umum. Ke depan, Monodepth2 menjadi titik tolak hampir seluruh penelitian kedalaman monokular swa-awas; [069 - PackNet](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md) mempertahankan kerangka pelatihannya sambil mengganti arsitektur agar lebih akurat pada resolusi tinggi. Bagi tinjauan RGB-D, bab ini relevan sebagai penyedia *pseudo-depth* murah: kedalaman prediksinya dapat melengkapi kanal RGB tanpa sensor kedalaman fisik.

## Poin untuk Sitasi

Kutip dengan kunci `godard2019monodepth2`. Ringkasan yang aman dikutip: "Monodepth2 (Godard dkk., ICCV 2019) menunjukkan bahwa tiga perbaikan pada loss pelatihan swa-awas — reproyeksi minimum per piksel, *auto-masking* piksel stasioner, dan multi-skala resolusi penuh — cukup untuk melampaui seluruh metode swa-awas sebelumnya pada KITTI (AbsRel 0,115, monokular murni tanpa label kedalaman)." Angka hasil pada bab ini diverifikasi dari naskah (tabel ablasi) dan repositori resmi. Catatan verifikasi: angka pembanding spesifik pada Tabel 1 naskah (Zhou dkk., Monodepth, EPC++) tidak dikutip di sini; cocokkan ke tabel naskah asli sebelum mengutipnya. Versi awal pracetak (v1) memakai enkoder bersama untuk pose dan kedalaman serta belum memuat *auto-masking*; kutipan sebaiknya merujuk versi ICCV (v3/v4).
