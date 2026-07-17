# 063 - Unsupervised Monocular Depth Estimation with Left-Right Consistency

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `godard2017monodepth` |
| Judul asli | Unsupervised Monocular Depth Estimation with Left-Right Consistency |
| Penulis | Clément Godard, Oisin Mac Aodha, Gabriel J. Brostow |
| Tahun | 2017 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1609.03677
- **Google Scholar:** https://scholar.google.com/scholar?q=Unsupervised%20Monocular%20Depth%20Estimation%20with%20Left-Right%20Consistency
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Unsupervised%20Monocular%20Depth%20Estimation%20with%20Left-Right%20Consistency&sort=relevance
- **Kode sumber (TensorFlow):** https://github.com/mrharicot/monodepth

## Gambaran Umum

Makalah ini memperkenalkan Monodepth, jaringan saraf konvolusi yang belajar memprediksi peta kedalaman (jarak setiap piksel ke kamera) dari satu citra, tanpa kedalaman acuan (*ground truth*) saat pelatihan. Sebagai pengganti label, pelatihan memakai pasangan citra stereo terkalibrasi: jaringan memprediksi disparitas — pergeseran piksel antara pandangan kiri dan kanan — yang dinilai dari kemampuannya merekonstruksi citra pandangan seberang. Kontribusi kuncinya adalah rugi konsistensi kiri–kanan (*left-right consistency*), yang memaksa dua peta disparitas prediksi saling cocok secara geometris.

Pada tolok ukur KITTI, model mencapai galat relatif mutlak (AbsRel) 0,114 — sekitar 44% lebih rendah daripada pembanding terawasi (dilatih dengan kedalaman acuan) terbaik masanya, Eigen dkk., dengan 0,203. Saat pengujian model hanya memerlukan satu citra dan berjalan lebih dari 28 bingkai per detik. Makalah ini menjadi dasar metode kedalaman swa-awas (*self-supervised*) berikutnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular — menghitung kedalaman setiap piksel dari satu citra RGB — adalah masalah tanpa solusi unik (*ill-posed*): satu citra dapat dihasilkan oleh tak terhingga susunan geometri tiga dimensi. Pendekatan klasik mengandalkan banyak pengamatan (stereo binokular, *multi-view*), sehingga tidak berlaku untuk citra tunggal. Pendekatan pembelajaran pada 2014–2016 memformulasikannya sebagai regresi terawasi: jaringan dilatih memetakan citra ke peta kedalaman memakai pasangan citra dan kedalaman acuan, seperti dibahas pada [bab 062 (Eigen dkk., 2014)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md).

Kelemahannya adalah ketersediaan label. Kedalaman padat hanya dapat direkam sensor aktif seperti LiDAR (pemindai laser pengukur jarak), yang mahal dan berkeluaran jarang: pada KITTI, proyeksi titiknya menutup kurang dari 5% piksel, dengan galat akibat gerakan kendaraan dan oklusi (wilayah yang tertutup objek lain). Karya swa-awas awal, Garg dkk. (2016), mengganti label dengan rekonstruksi citra stereo, tetapi model pembentuk citranya tidak sepenuhnya dapat diturunkan sehingga pelatihannya suboptimal; Deep3D (Xie dkk., 2016) memerlukan distribusi atas semua kandidat disparitas sehingga tidak berskala ke resolusi besar. Masalah yang diangkat makalah ini: melatih kedalaman monokular tanpa label melalui model pembentuk citra yang sepenuhnya terdiferensialkan.

## Ide Utama

Gagasan intinya adalah mengubah prediksi kedalaman menjadi rekonstruksi citra. Jika sebuah fungsi mampu membangkitkan citra pandangan kanan dari citra pandangan kiri, fungsi itu harus memuat pengetahuan tentang geometri tiga dimensi pemandangan. Geometri tersebut diwujudkan sebagai peta disparitas: besaran pergeseran horizontal setiap piksel antara dua citra stereo yang telah direktifikasi (diluruskan sehingga titik yang sama terletak pada baris piksel yang sama di kedua citra). Pada pasangan stereo terkalibrasi, kedalaman diperoleh langsung melalui hubungan kedalaman = b·f/d, dengan b jarak antar-kamera (*baseline*) dan f panjang fokus kamera.

Dua keputusan desain membedakan makalah ini. Pertama, sintesis citra memakai *bilinear sampling* — pengambilan warna pada posisi bukan bulat sebagai interpolasi berbobot empat piksel tetangga — yang sepenuhnya dapat diturunkan, sehingga gradien rugi mengalir utuh ke jaringan. Kedua, jaringan memprediksi dua peta disparitas (kiri dan kanan) dari satu citra kiri saja, dan fungsi rugi memaksa keduanya konsisten: disparitas yang benar harus menjelaskan kedua pandangan secara serentak.

## Cara Kerja Langkah demi Langkah

### Formulasi: Kedalaman sebagai Hasil Samping Rekonstruksi

Saat pelatihan tersedia pasangan stereo terrektifikasi (I_kiri, I_kanan). Jaringan menerima hanya I_kiri dan mengeluarkan dua peta disparitas: d_kanan, yang diterapkan pada I_kiri menghasilkan rekonstruksi Ĩ_kanan, dan d_kiri, yang diterapkan pada I_kanan menghasilkan Ĩ_kiri. Penerapan dilakukan dengan pemetaan balik (*backward mapping*): warna setiap piksel rekonstruksi diambil dari citra sumber pada posisi yang digeser sejauh nilai disparitas, dan karena posisi itu bukan bilangan bulat, warnanya dihitung dengan *bilinear sampling*. Operator inilah yang membuat alur dapat dilatih *end-to-end* (gradien rugi citra mengalir langsung ke bobot), berbeda dengan Garg dkk. yang memerlukan aproksimasi deret Taylor.

### Arsitektur Encoder–Decoder

Jaringan bersifat *fully convolutional* (hanya lapis konvolusi, tanpa lapis terhubung penuh) dan terinspirasi DispNet, arsitektur regresi disparitas terawasi dari Mayer dkk. Bagian *encoder* (lapis cnv1–cnv7b) mengekstrak fitur sambil menurunkan resolusi; bagian *decoder* menaikkan kembali resolusi sambil menerima *skip connection* (penyaluran peta fitur *encoder* ke lapis *decoder* beresolusi sama) agar detail tepi terjaga. Disparitas diprediksi pada empat skala keluaran (disp4 sampai disp1; resolusi berlipat dua per skala), dua peta per skala (kiri dan kanan). Keluaran dibatasi ke rentang [0, d_max] oleh fungsi *sigmoid* (nonlinier pembatas keluaran) yang diskalakan, dengan d_max = 0,3 × lebar citra per skala. Model utama berparameter 31 juta; varian *encoder* ResNet50 (jaringan 50 lapis bersambungan residual) 48 juta.

Fungsi aktivasi memakai ELU (*exponential linear unit*) alih-alih ReLU, yang cenderung mengunci disparitas skala menengah ke satu nilai di awal pelatihan; perbesaran resolusi *decoder* memakai *upsampling nearest-neighbor* diikuti konvolusi, bukan dekonvolusi, demi menghindari artefak papan catur.

### Fungsi Rugi Tiga Komponen

Rugi dihitung pada keempat skala lalu dijumlahkan; setiap skala menggabungkan tiga suku dalam versi kiri dan kanan:

1. **Kecocokan tampilan (C_ap).** Kemiripan citra rekonstruksi dengan citra asli sebagai kombinasi SSIM — ukuran kemiripan struktur lokal yang lebih peka terhadap tekstur daripada selisih piksel mentah — dan L1 (rata-rata selisih absolut). Dipakai SSIM berblok 3×3 dengan bobot α = 0,85.
2. **Kehalusan disparitas (C_ds).** Penalti L1 pada gradien disparitas yang diboboti gradien citra: di daerah tanpa tepi, disparitas didorong rata; di dekat tepi — tempat diskontinuitas kedalaman — penalti dilonggarkan. Bobotnya α_ds = 0,1/r (r = faktor pengecilan skala) agar kehalusan setara di semua resolusi.
3. **Konsistensi kiri–kanan (C_lr).** Penalti L1 antara d_kiri dan d_kanan yang di-*warp* mengikuti d_kiri: bila d_kiri menyatakan piksel P bergeser 10 piksel ke kanan, d_kanan pada posisi tujuan harus menyatakan pergeseran balik yang sama besar.

Rugi kecocokan tampilan saja menghasilkan citra rekonstruksi yang tampak benar, tetapi peta disparitas yang buruk — artefak salinan tekstur dan galat pada diskontinuitas kedalaman — karena banyak medan disparitas yang salah secara geometris tetap merekonstruksi citra dengan baik. Suku C_lr mengatasi masalah ini tanpa memerlukan label.

Alur pelatihan dan pengujian tersebut diringkas pada diagram berikut:

```
   PELATIHAN (masukan: pasangan stereo terrektifikasi I_kiri, I_kanan)

 I_kiri
   │
   ▼
 ┌──────────┐   skip connection   ┌──────────┐
 │ ENCODER  │ ──────────────────► │ DECODER  │
 │ cnv1..7  │                     │ upcnv7.. │
 └──────────┘                     └──────────┘
                                       │
             d_kiri dan d_kanan pada 4 skala (disp4..disp1)
                                       │
        ┌──────────────────────────────┴──────────────────────┐
        ▼                                                     ▼
  warp(I_kanan, d_kiri) = Ĩ_kiri             warp(I_kiri, d_kanan) = Ĩ_kanan
        │                                                     │
  C_ap: SSIM+L1 vs I_kiri                     C_ap: SSIM+L1 vs I_kanan
        │                                                     │
  C_ds: disparitas halus, diboboti tepi       C_lr: d_kiri ≈ warp(d_kanan)
        └──────────► rugi total = jumlah atas 4 skala ◄───────┘

   PENGUJIAN (masukan: satu citra saja)

 citra ─► jaringan ─► d_kiri resolusi penuh ─► kedalaman = b · f / d_kiri
```

Diagram menegaskan dua hal: hanya citra kiri yang masuk ke jaringan, dan ketiga suku rugi dievaluasi pada keempat skala sehingga sinyal pelatihan tersedia dari resolusi kasar hingga penuh.

### Pelatihan dan Inferensi

Pelatihan berlangsung 50 *epoch* (putaran penuh atas data latih) dengan *batch* 8 citra, pengoptimal Adam (pembaruan bobot berlaju adaptif per parameter), dan laju pembelajaran awal 10⁻⁴ yang dibagi dua setiap 10 *epoch* setelah *epoch* ke-30 — total sekitar 25 jam pada satu GPU Titan X untuk 30 ribu citra. Augmentasi data meliputi pembalikan horizontal dengan penukaran posisi kedua citra, serta pergeseran acak gamma, kecerahan, dan warna. Saat pengujian, peta disparitas kiri pada resolusi penuh dikonversi menjadi kedalaman memakai *baseline* dan panjang fokus kamera data latih; disparitas kanan tidak dipakai. Inferensi berjalan kurang dari 35 milidetik per citra 512×256 (lebih dari 28 bingkai per detik). Pascapemrosesan opsional (*pp*) menjalankan jaringan pada citra asli dan bayangan cerminnya lalu menggabungkan kedua peta disparitas guna menekan artefak tepi oklusi, dengan biaya komputasi uji dua kali lipat.

## Eksperimen dan Hasil

Evaluasi utama memakai dataset KITTI (42.382 pasangan stereo dari 61 adegan; citra tipikal 1242×375 piksel) dengan dua pemisahan: Eigen (697 citra uji; 22.600 citra latih; acuan proyeksi LiDAR) dan KITTI (200 citra uji; 29.000 citra latih). Metriknya: AbsRel (rata-rata |prediksi − acuan|/acuan), RMSE (akar rata-rata kuadrat galat), δ < 1,25 (persentase piksel dengan simpangan di bawah 25% dari acuan), dan D1-all (persentase piksel bergalat disparitas besar menurut definisi KITTI).

Hasil kunci pada pemisahan Eigen (kedalaman dibatasi 80 m):

- Monodepth (latih KITTI saja): AbsRel 0,148; δ<1,25 = 0,803.
- Monodepth (pralatih Cityscapes + KITTI): AbsRel 0,124; δ<1,25 = 0,847.
- Monodepth ResNet + *pp* (CS+K): AbsRel 0,114; RMSE 4,935; δ<1,25 = 0,861.
- Pembanding terawasi: Eigen dkk. 0,203 dan 0,702; Liu dkk. 0,201 dan 0,680.
- Pembanding swa-awas Garg dkk. (batas 50 m): AbsRel 0,169; Monodepth dengan pengaturan setara mencapai 0,140.

Interpretasinya: tanpa satu pun label kedalaman, model ini mengalahkan dua metode terawasi (galat relatif 0,114 berbanding 0,203, turun ±44%) sembari menaikkan proporsi piksel akurat dari 70,2% menjadi 86,1%; terhadap Garg dkk., galat turun ±17% pada pengaturan sama. Pralatihan pada Cityscapes (22.973 pasangan stereo perkotaan) memperbaiki AbsRel dari 0,148 menjadi 0,124 — keragaman data latih terbukti sepenting arsitektur.

Ablasi pada pemisahan KITTI mengukuhkan peran tiap komponen: model pembentuk citra Deep3D pada arsitektur yang sama hanya mencapai AbsRel 0,412 dan D1-all 66,85%, sedangkan *bilinear sampling* dengan rugi lengkap menurunkannya ke 0,124 dan 30,27%; menghilangkan suku C_lr memperburuk metrik (AbsRel 0,148 → 0,152; RMSE 5,927 → 6,098 pada Eigen) dan menimbulkan artefak salinan tekstur pada tepi objek. Varian stereo, yang menerima kedua citra saat uji, mencapai AbsRel 0,068 dan D1-all 9,19% — acuan atas yang menunjukkan biaya pemakaian satu citra saja.

Pada Make3D — dataset RGB–kedalaman tanpa stereo, sehingga tidak dapat dipakai melatih — model yang hanya dilatih pada Cityscapes mencapai AbsRel 0,443: kalah dari metode terawasi Make3D terbaik (0,198), tetapi masih mengungguli dua metode terawasi lama pada sebagian metrik, tanpa pernah melihat data domain itu.

## Kelebihan dan Keterbatasan

Kelebihan: (1) pelatihan tanpa label kedalaman — bahan latihnya pasangan video stereo yang lebih mudah diperoleh daripada rekaman LiDAR; (2) model pembentuk citra sepenuhnya terdiferensialkan, tanpa aproksimasi rugi; (3) konsistensi kiri–kanan menaikkan akurasi dan membersihkan artefak tepi tanpa komponen tambahan saat inferensi; (4) inferensi cepat, lebih dari 28 bingkai per detik.

Keterbatasan yang diakui penulis: (1) artefak tetap muncul pada batas oklusi, karena piksel yang hanya terlihat di satu pandangan tidak memiliki pasangan untuk direkonstruksi; (2) pelatihan memerlukan stereo terrektifikasi dan selaras waktu, sehingga dataset citra tunggal tidak dapat dipakai; (3) permukaan memantul (spekular) dan transparan menghasilkan kedalaman tidak konsisten, karena rugi utama bertumpu pada kemiripan tampilan. Dari sisi rekayasa, dua hal layak dicatat. Pertama, skala kedalaman terikat kalibrasi kamera data latih: model yang hanya dilatih pada Cityscapes merosot ke AbsRel 0,699 saat diuji pada KITTI — generalisasi numerik lintas kamera lemah tanpa penyetelan halus. Kedua, pascapemrosesan yang menambah akurasi menggandakan biaya inferensi.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis estimasi kedalaman monokular dari [bab 062 (Eigen dkk., 2014)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md): bab 062 menunjukkan jaringan dalam dapat meregresikan kedalaman dari satu citra, tetapi menuntut label yang mahal; bab ini mempertahankan keluaran serupa sekaligus mengganti label dengan supervisi geometri stereo. Rumusan ini menjadi dasar [bab 064 (Monodepth2, 2019)](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md), penerus langsung oleh kelompok yang sama: oklusi ditangani dengan rugi *minimum reprojection*, adegan statis dengan *auto-masking*, dan supervisi diperluas ke video monokular sehingga kebutuhan stereo saat latih gugur. Bagi tinjauan YOLO/RGB-D, bab ini relevan sebagai dasar penggunaan *pseudo-depth* — kedalaman prediksi model sebagai pengganti sensor kedalaman — untuk melengkapi citra RGB.

## Poin untuk Sitasi

Kutip dengan kunci `godard2017monodepth`. Ringkasan yang aman dikutip: "Godard dkk. (CVPR 2017) melatih estimasi kedalaman monokular tanpa label kedalaman melalui rekonstruksi citra stereo dengan *bilinear sampling* yang terdiferensialkan dan rugi konsistensi kiri–kanan; pada KITTI, model ini mengungguli metode terawasi pembanding masanya (AbsRel 0,114 versus 0,203) dengan inferensi lebih dari 28 bingkai per detik." Catatan verifikasi: angka diambil dari teks dan tabel arXiv v3 (versi CVPR 2017) via render ar5iv; cocokkan ulang angka Tabel 1–3 (khususnya baris CS+K dan *pp*) dengan PDF naskah asli sebelum sitasi formal. Klaim "mengungguli metode terawasi" hanya berlaku untuk pembanding 2014–2015 (Eigen dkk.; Liu dkk.), bukan metode terawasi yang lebih baru.
