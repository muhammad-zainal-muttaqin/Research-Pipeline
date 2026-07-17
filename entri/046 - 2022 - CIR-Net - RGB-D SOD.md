# 046 - CIR-Net: Cross-Modality Interaction and Refinement for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cong2022cirnet` |
| Judul asli | CIR-Net: Cross-modality Interaction and Refinement for RGB-D Salient Object Detection |
| Penulis | Runmin Cong, Qinwei Lin, Chen Zhang, Chongyi Li, Xiaochun Cao, Qingming Huang, Yao Zhao |
| Tahun | 2022 |
| Venue | IEEE Transactions on Image Processing, vol. 31, hal. 6800–6815 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2210.02843
- **DOI (versi penerbit):** https://doi.org/10.1109/TIP.2022.3216198
- **Halaman proyek (kode dan hasil):** https://rmcong.github.io/proj_CIRNet.html
- **Google Scholar:** https://scholar.google.com/scholar?q=CIR-Net%3A%20Cross-Modality%20Interaction%20and%20Refinement%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=CIR-Net%3A%20Cross-Modality%20Interaction%20and%20Refinement%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan CIR-Net, jaringan saraf konvolusi untuk *salient object detection* (SOD — tugas menandai setiap piksel yang termasuk objek paling menonjol dalam sebuah adegan) pada pasangan citra RGB dan peta kedalaman. Gagasan utamanya adalah melakukan interaksi lintas-modal pada dua tahap sekaligus: pada *encoder* (bagian jaringan yang memampatkan citra menjadi fitur multi-tingkat) melalui unit PAI, dan pada *decoder* (bagian yang memulihkan fitur menjadi peta keluaran) melalui unit IGF. Di antara keduanya disisipkan *middleware* penyempurnaan yang membersihkan fitur dari sudut pandang modalitas tunggal (unit smAR) dan lintas-modal (unit cmWR).

Hasilnya, CIR-Net mengungguli 15 metode berbasis CNN pembanding pada enam tolok ukur RGB-D SOD. Sebagai contoh, pada NJUD-test model ini mencapai F-measure 0,9277 dan S-measure 0,9250 dengan *backbone* ResNet-50, tanpa pra-pemrosesan maupun pasca-pemrosesan tambahan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek menonjol pada citra RGB saja sering gagal ketika kontras warna antara objek dan latar rendah atau ketika latar penuh tekstur pengganggu. Peta kedalaman (citra yang setiap pikselnya menyatakan jarak ke kamera) menambahkan informasi bentuk dan konsistensi spasial yang tidak tersedia dari warna, sehingga metode RGB-D berpotensi menekan latar lebih bersih. Persoalannya, RGB dan kedalaman adalah dua modalitas dengan sifat berbeda; cara menggabungkannya menentukan mutu hasil.

Sebelum makalah ini, struktur yang lazim terbagi tiga. Struktur satu alur menggabungkan RGB dan kedalaman sejak masukan (menjadi citra empat kanal), tetapi mengabaikan perbedaan sifat kedua modalitas. Struktur dua alur memproses RGB dan kedalaman pada cabang terpisah, lalu berinteraksi hanya pada tahap *encoder* atau hanya pada tahap *decoder* — tidak keduanya; DMRA (bab 035) dan S2MA (bab 039) termasuk garis ini. Struktur tiga alur seperti D3Net (bab 037) menambahkan cabang RGB-D ketiga, tetapi cabang itu dipelajari dari nol sehingga mahal parameter. CIR-Net mengisi celah yang tersisa: interaksi pada *encoder* dan *decoder* sekaligus, dengan cabang RGB-D yang dibangun dari fusi fitur tingkat tinggi kedua modalitas.

## Ide Utama

CIR-Net memakai arsitektur tiga alur: alur RGB, alur kedalaman, dan alur RGB-D. Alur RGB-D dibentuk dengan menggabungkan fitur tingkat tinggi dari dua alur pertama secara bertingkat dan terpandu atensi (unit PAI). Fitur puncak ketiga alur kemudian disempurnakan dua kali sebelum masuk *decoder*: pertama ditegaskan dari dalam modalitasnya sendiri (unit smAR), lalu diboboti oleh konteks global lintas-modalitas (unit cmWR). Pada *decoder*, fitur alur RGB dan kedalaman dialirkan ke alur RGB-D setiap tingkat melalui pintu pembobot adaptif (unit IGF), sehingga alur RGB-D menjadi arus utama yang menghasilkan peta saliensi akhir. Yang berubah dibanding pendahulunya adalah tempat dan cara interaksi serta penyempurnaan fitur dilakukan, bukan bentuk masukan maupun keluaran.

## Cara Kerja Langkah demi Langkah

### Arsitektur Tiga Alur

*Backbone* (jaringan ekstraktor fitur yang telah terlatih pada ImageNet; makalah memakai ResNet-50 atau VGG-16) mengekstrak lima tingkat fitur dari citra RGB (f_r^1 sampai f_r^5) dan dari peta kedalaman (f_d^1 sampai f_d^5). Fitur RGB-D (f_rgbd^i) hanya dibangun untuk tingkat 3 sampai 5 oleh unit PAI. Fitur tingkat-5 ketiga modalitas masuk *middleware* penyempurnaan, lalu *decoder* lima tingkat menghasilkan peta saliensi. Alur data lengkapnya:

```
                 ┌───────── ENCODER (5 tingkat fitur) ─────────┐
 citra RGB  ──►  │ alur RGB   : fr1   fr2   fr3   fr4   fr5     │
                 │                          │     │     │       │
 peta depth ──►  │ alur depth : fd1   fd2   fd3   fd4   fd5     │
                 │                          ▼     ▼     ▼       │
                 │   PAI: fusi tingkat 3-5, dipandu atensi      │
                 │   spasial tingkat sebelumnya                 │
                 │   ──► frgbd3, frgbd4, frgbd5                 │
                 └──────────────────────┬───────────────────────┘
                                        ▼
        MIDDLEWARE PENYEMPURNAAN (hanya fitur tingkat-5)
        smAR: atensi 3D = SA(f) ⊗ CA(f) per modalitas
        cmWR: korelasi non-lokal M1 (RGB × depth) dan
              M2 (RGB-D × RGB-D) ──► bobot pemurni global
                                        ▼
                 ┌───────── DECODER (tingkat 5 ──► 1) ─────────┐
                 │ IGF_i = P_i · H_i + (1 - P_i) · f_IGF(i+1)   │
                 │ H_i : gabungan fitur dekoder RGB + depth     │
                 │ P_i : peta kepentingan terpelajari (sigmoid) │
                 └──────────────────────┬───────────────────────┘
                                        ▼
                        peta saliensi akhir (alur RGB-D)
```

### Unit PAI pada Encoder

Unit *Progressive Attention-guided Integration* (PAI) membentuk fitur RGB-D dalam dua langkah. Pertama, fitur RGB dan kedalaman setingkat digabungkan per kanal lalu dilewatkan ke konvolusi, *batch normalization* (normalisasi statistik per kelompok data), dan ReLU: f̃_rgbd^i = conv([f_r^i, f_d^i]) untuk i = 3, 4, 5. Fusi dimulai dari tingkat 3 karena fitur kedalaman dangkal cenderung memuat derau latar, sedangkan fitur dalam lebih bersih tetapi miskin detail.

Kedua, peta atensi spasial dari tingkat sebelumnya memandu fusi tingkat berikutnya. Atensi spasial adalah peta seukuran fitur yang menilai kepentingan setiap posisi; posisi penting diberi bobot besar. Fitur f̃_rgbd^3 menghasilkan peta A^3 yang disesuaikan ukurannya, lalu fitur tingkat 4 diperbarui sebagai f_rgbd^4 = f̃_rgbd^4 ⊙ A^3 + f̃_rgbd^4, dan pola yang sama berlaku untuk tingkat 5. Perkalian elemen-demi-elemen (⊙) menonjolkan wilayah yang disepakati penting pada tingkat sebelumnya, sedangkan penjumlahan residual menjaga fitur asli tetap tersedia bila atensi keliru.

### Unit smAR: Penyempurnaan Modalitas Tunggal

Fitur hasil *encoder* memuat redundansi kanal dan derau latar. Unit *self-modality attention refinement* (smAR) menggabungkan dua jenis atensi yang biasanya dipakai terpisah: atensi kanal (bobot penting per kanal fitur) dan atensi spasial (bobot penting per posisi). Keduanya dihitung secara paralel dari fitur tingkat-5 setiap modalitas, lalu dikalikan secara matriks menjadi satu tensor atensi tiga dimensi A_3D = SA(f) ⊗ CA(f). Fitur disempurnakan dengan f_smAR = conv(A_3D ⊙ f + f): satu tensor menegaskan dimensi spasial dan kanal sekaligus, lebih hemat hitungan dibanding pemakaian serial kedua atensi.

### Unit cmWR: Penyempurnaan Lintas-Modal

Unit *cross-modality weighting refinement* (cmWR) menangkap ketergantungan jarak jauh antar-modalitas dengan pola *non-local*: setiap posisi piksel dibandingkan dengan semua posisi lain melalui perkalian matriks, mirip mekanisme *self-attention*. Fitur hasil smAR dipetakan ke ruang bersama oleh konvolusi *bottleneck* (yang memangkas jumlah kanal menjadi separuh), menghasilkan F_θ dan F_ξ. Korelasi piksel-demi-piksel RGB terhadap kedalaman membentuk matriks M1 = softmax(F_θᵀ ⊗ F_ξ) berukuran HW × HW, sedangkan korelasi diri fitur RGB-D membentuk M2 = softmax(F_φᵀ ⊗ F_ψ). Gabungan softmax(M1 ⊙ M2) menjadi bobot global yang memurnikan fitur ketiga modalitas, ditambah koneksi residual. M1 menangkap respons bersama RGB–kedalaman; M2 menangkap struktur internal RGB-D, sehingga objek dengan banyak bagian tersambung lebih utuh.

### Unit IGF pada Decoder

Pada *decoder*, fitur alur RGB dan kedalaman setiap tingkat dialirkan ke alur RGB-D melalui struktur agregasi konvergen. Unit *importance gated fusion* (IGF) pertama menggabungkan fitur *decoder* RGB dan kedalaman setingkat (setelah masing-masing difusi dengan fitur *encoder* lewat *skip-connection*, yaitu jalur pintas yang menyalin fitur *encoder* ke *decoder* pada resolusi yang sama) menjadi fitur H^i. Kemudian IGF mempelajari peta kepentingan P^i = sigmoid(CA(conv([H^i, f_IGF^{i+1}↑]))) — sebuah tensor bernilai 0 sampai 1 hasil atensi kanal. Keluarannya adalah f_IGF^i = conv(P^i ⊙ H^i + (1 − P^i) ⊙ f_IGF^{i+1}↑), dihitung dari tingkat 5 turun ke tingkat 1. Bila fitur kedalaman pada suatu wilayah tidak andal, jaringan dapat menurunkan P^i di sana dan mengandalkan aliran dari tingkat sebelumnya; inilah sumber ketahanan CIR-Net terhadap peta kedalaman berkualitas rendah.

### Fungsi Loss dan Pelatihan

Ketiga alur masing-masing mengeluarkan peta saliensi (S_r, S_d, S_rgbd), dan ketiganya diawasi dengan *binary cross-entropy* (BCE — fungsi galat yang mengukur selisih distribusi antara piksel prediksi dan label biner *ground truth*): Loss = BCE(S_r, G) + BCE(S_d, G) + BCE(S_rgbd, G). Saat pengujian hanya keluaran alur RGB-D yang dipakai. Data latih terdiri atas 1.485 sampel NJUD, 700 sampel NLPR, dan 800 sampel DUT (total 2.985 pasang citra), dengan augmentasi pembalikan, rotasi, dan skala masukan 128, 256, dan 352. Jaringan dioptimalkan dengan Adam (laju pembelajaran awal 1×10⁻⁴, dibagi 5 setiap 40 *epoch*), ukuran *batch* 16, pada dua GPU RTX 2080 Ti selama sekitar 4 jam. Saat inferensi citra diubah ke 352 × 352; waktu proses 0,07 detik per citra (sekitar 14 FPS), tanpa pra-pemrosesan HHA (pengkodean kedalaman menjadi tiga kanal: disparitas horizontal, tinggi, dan sudut normal) maupun pasca-pemrosesan CRF (*conditional random field*, penghalusan tepi berbasis model grafik probabilistik).

## Eksperimen dan Hasil

Evaluasi dilakukan pada enam tolok ukur: STEREO797 (797 citra stereo), NLPR (1.000 citra Kinect), NJUD (1.985 citra, kedalaman estimasi stereo), DUT (1.200 citra kamera Lytro), LFSD (100 citra *light field*), dan SIP (929 citra beresolusi tinggi). Metriknya tiga: F-measure (rata-rata harmonik berbobot presisi dan *recall*, dengan β² = 0,3 yang menekankan presisi), S-measure (kemiripan struktur peta prediksi terhadap *ground truth*, gabungan kemiripan wilayah dan objek berbobot 0,5), dan MAE (rata-rata selisih absolut per piksel; semakin kecil semakin baik). Pembandingnya 15 metode CNN terdahulu.

Dengan *backbone* ResNet-50, CIR-Net mencapai F-measure / S-measure / MAE sebesar 0,9277 / 0,9250 / 0,0350 pada NJUD-test, 0,9241 / 0,9334 / 0,0227 pada NLPR-test, 0,9376 / 0,9324 / 0,0288 pada DUT-test, 0,9139 / 0,9166 / 0,0377 pada STEREO797, 0,8828 / 0,8753 / 0,0677 pada LFSD, dan 0,8959 / 0,8884 / 0,0523 pada SIP. Model ini terbaik pada seluruh metrik kecuali MAE pada SIP. Dibandingkan metode peringkat dua, perbaikan MAE mencapai 3,0% pada NLPR, 15,3% pada DUT, dan 10,7% pada STEREO797 — artinya galat piksel rata-rata turun hingga seperenam pada DUT tanpa bantuan pasca-pemrosesan apa pun.

Uji pada subset sulit memperkuat klaim desain. Pada subset peta kedalaman tak andal, MAE CIR-Net 0,0449 melawan 0,0561 milik DANet sebagai pembanding terbaik, atau 20,0% lebih baik — konsisten dengan fungsi pintu pembobot IGF. Pada subset kontras rendah, MAE lebih baik 25,9% dibanding SSF; pada subset objek kecil (luas objek kurang dari 10% citra), MAE lebih baik 18,7%. Pada subset multi-objek, F-measure dan S-measure unggul 1,6% berkat konteks global cmWR.

Studi ablasi pada NJUD-test menunjukkan kontribusi tiap modul secara berurutan: model dasar 0,8880; menambah PAI menjadi 0,8952; menambah IGF menjadi 0,9135; menambah cmWR menjadi 0,9175; dan model penuh dengan smAR 0,9277 (F-measure). Lompatan terbesar (+0,0183) datang dari IGF: interaksi pada *decoder* — tahap yang diabaikan banyak pendahulu — justru penyumbang perbaikan utama. Ablasi arsitektur menambah dua temuan: struktur tiga alur mengungguli varian dua alur sebesar 0,0209 F-measure pada LFSD dengan biaya kecepatan 14 FPS melawan 18 FPS; dan keluaran alur RGB-D mengungguli alur RGB tunggal dari 0,8324 menjadi 0,8828 pada LFSD (+6,0%).

## Kelebihan dan Keterbatasan

Kelebihan utama CIR-Net adalah interaksi lintas-modal pada *encoder* dan *decoder* sekaligus, ditambah penyempurnaan dua arah yang terbukti menyumbang pada ablasi. Pintu pembobot IGF memberi ketahanan terhadap peta kedalaman berkualitas rendah tanpa modul estimasi kualitas khusus. Middleware penyempurnaannya bersifat *pluggable* — dapat disisipkan ke jaringan tiga alur lain. Seluruh hasil dicapai tanpa HHA maupun CRF, sehingga alur kerja lebih sederhana dibanding metode yang bergantung pada pasca-pemrosesan.

Keterbatasan yang diakui penulis makalah ada tiga. Pertama, model gagal pada objek kecil ganda yang jauh dari lensa karena peta kedalaman tidak lagi informatif. Kedua, konflik kontras — objek yang kontras pada kedalaman berbeda dari objek yang kontras pada RGB — menimbulkan ambiguitas yang tidak terselesaikan. Ketiga, kinerja bergantung pada volume data latih: membuang data latih NLPR menurunkan F-measure pada LFSD sebesar 4,4%. Dari sisi rekayasa, struktur tiga alur menambah parameter dan menekan kecepatan ke 14 FPS, sehingga belum memenuhi tuntutan *real-time* ketat; dan *backbone* CNN yang dipakai memiliki jangkauan konteks lebih sempit dibanding *backbone* Transformer yang muncul pada periode yang sama (bab 042).

## Kaitan dengan Bab Lain

CIR-Net mewarisi garis metode dua alur yang dibahas pada bab-bab sebelumnya: [DMRA](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) (bab 035) yang memopulerkan fusi terpandu atensi, [S2MA](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md) (bab 039) dengan seleksi modalitas, dan [BBS-Net](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md) (bab 036) — ketiganya menjadi baris pembanding langsung dalam tabel hasil makalah ini. Dari sisi struktur, CIR-Net memperbaiki desain tiga alur [D3Net](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md) (bab 037) dengan membangun alur RGB-D dari fusi fitur, bukan melatihnya dari nol. [JL-DCF](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md) (bab 038) dan [UC-Net](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md) (bab 041) turut menjadi pembanding. Ke arah berikutnya, keterbatasan konteks lokal CNN yang dipakai CIR-Net dijawab oleh generasi berbasis Transformer seperti [VST](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md) (bab 042).

## Poin untuk Sitasi

Kutip dengan kunci `cong2022cirnet`. Ringkasan yang aman dikutip: "CIR-Net melakukan interaksi lintas-modal pada tahap encoder (unit PAI) dan decoder (unit IGF) sekaligus, disertai middleware penyempurnaan fitur modalitas tunggal (smAR) dan lintas-modal (cmWR); model ini mengungguli 15 metode CNN pada enam tolok ukur RGB-D SOD, misalnya F-measure 0,9277 pada NJUD-test dengan backbone ResNet-50, tanpa pra- maupun pasca-pemrosesan." Seluruh angka pada bab ini diambil dari naskah arXiv 2210.02843v1; sebelum sitasi formal, cocokkan angka tabel dengan versi terbit IEEE TIP (DOI 10.1109/TIP.2022.3216198) karena versi penerbit dapat berbeda tipis dari pracetak.
