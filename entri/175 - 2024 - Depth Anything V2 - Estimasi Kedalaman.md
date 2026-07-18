# 175 - Depth Anything V2

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024depthanythingv2` |
| Judul asli | Depth Anything V2 |
| Penulis | Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, Hengshuang Zhao |
| Tahun | 2024 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2024) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2406.09414
- **Repositori kode resmi:** https://github.com/DepthAnything/Depth-Anything-V2
- **Halaman proyek:** https://depth-anything-v2.github.io/

## Gambaran Umum

Makalah ini memperkenalkan Depth Anything V2, model fondasi untuk estimasi kedalaman monokular (memperkirakan jarak setiap piksel dari kamera menggunakan satu citra RGB, tanpa sensor kedalaman). Masalah utama yang diperbaiki adalah kualitas label pelatihan: label kedalaman dari citra nyata umumnya kasar di tepi objek dan berderau di permukaan transparan atau reflektif, sehingga model yang dilatih langsung pada label tersebut ikut kabur pada detail halus. Solusinya adalah mengganti seluruh citra nyata berlabel dengan citra sintetis berlabel presisi untuk melatih model guru berkapasitas besar, lalu memakai guru itu untuk memberi label semu (*pseudo-label*) pada puluhan juta citra nyata tanpa label, yang kemudian dipakai melatih model siswa berukuran lebih kecil.

Hasilnya adalah model yang menghasilkan peta kedalaman relatif dengan tepi lebih tajam dan lebih tahan terhadap variasi domain dibandingkan Depth Anything V1, tersedia dalam empat ukuran (Small, Base, Large, Giant) dengan rentang 24,8 juta sampai 1,3 miliar parameter. Makalah ini juga mengusulkan DA-2K, tolok ukur evaluasi baru berbasis anotasi kedalaman relatif berpasangan pada citra beresolusi tinggi dan beragam skenario.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, model estimasi kedalaman monokular yang paling andal untuk generalisasi lintas domain dilatih secara *supervised* (dengan label kedalaman kebenaran/*ground truth*) pada campuran dataset citra nyata, seperti pendekatan MiDaS dan DPT (*Dense Prediction Transformer*, arsitektur Transformer untuk prediksi padat per piksel). Depth Anything V1 memperluas pendekatan ini dengan menambahkan puluhan juta citra nyata tanpa label yang diberi label semu, dan menunjukkan bahwa skala data tanpa label sangat membantu generalisasi.

Masalah yang tersisa terletak pada sumber label kedalaman nyata itu sendiri. Label kedalaman citra nyata biasanya diperoleh dari sensor jarak (LiDAR, kamera stereo, atau struktur dari gerak/*structure-from-motion*), yang menghasilkan pengukuran kasar di tepi objek tipis, gagal pada permukaan transparan atau memantul cahaya (kaca, air, logam mengkilap), dan sering memiliki lubang data pada area sulit. Karena model dilatih untuk meniru label tersebut, kesalahan itu ikut terpelajari: peta kedalaman keluaran cenderung kabur di sekitar batas objek dan tidak konsisten pada material sulit. Masalah ini penting karena estimasi kedalaman monokular dipakai sebagai pengganti sensor kedalaman fisik pada aplikasi seperti navigasi robot dan rekonstruksi 3D, sehingga ketajaman tepi langsung memengaruhi keandalan aplikasi hilir.

## Ide Utama

Gagasan inti Depth Anything V2 adalah memisahkan sumber label akurat dari sumber keragaman data. Citra sintetis yang dihasilkan mesin grafis 3D memiliki label kedalaman piksel demi piksel yang presisi sempurna, tetapi jumlah dan keragamannya terbatas sehingga model yang dilatih langsung di atasnya cenderung tidak menggeneralisasi ke citra dunia nyata. Citra nyata tanpa label tersedia dalam jumlah besar dan sangat beragam, tetapi tidak memiliki label kedalaman sama sekali.

Solusinya adalah pola guru-siswa (*teacher-student*) tiga tahap. Model guru berkapasitas besar dilatih murni pada citra sintetis berlabel presisi, sehingga mewarisi ketajaman label tanpa terpapar derau label nyata. Guru ini kemudian dipakai untuk memprediksi kedalaman pada jutaan citra nyata tanpa label, menghasilkan label semu. Model siswa yang lebih kecil dan efisien lalu dilatih pada label semu tersebut. Karena label semu berasal dari guru yang tajam, siswa mewarisi ketajaman itu sekaligus mendapat keragaman visual dari skala citra nyata yang besar — dua sifat yang sebelumnya sulit didapat bersamaan dari satu sumber data saja.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dasar

Setiap model, baik guru maupun siswa, memakai DINOv2 (model *encoder* citra yang telah dilatih awal secara *self-supervised*, yaitu tanpa label manusia, untuk menghasilkan fitur visual umum) sebagai tulang punggung (*backbone*, jaringan ekstraksi fitur utama), diikuti kepala DPT sebagai dekoder yang mengubah fitur menjadi peta kedalaman padat per piksel. Dibandingkan V1, penulis mengambil fitur dari lapisan menengah tulang punggung, bukan hanya empat lapisan terakhir, agar selaras dengan praktik umum pemakaian DPT pada literatur.

### Tahap 1 — Melatih Guru pada Data Sintetis

Guru memakai tulang punggung terbesar, ViT-Giant/DINOv2-G berkapasitas sekitar 1,3 miliar parameter. Guru dilatih pada gabungan lima dataset sintetis (BlendedMVS, Hypersim, IRS, TartanAir, VKITTI2) berjumlah total 595 ribu citra, pada resolusi masukan 518×518 piksel. Fungsi *loss* memakai kombinasi *scale-and-shift-invariant loss* (mengukur selisih kedalaman terlepas dari skala dan pergeseran absolut, karena kedalaman relatif tidak memiliki satuan tetap) dan *gradient matching loss* (menyamakan gradien spasial peta kedalaman prediksi dan kebenaran, mendorong ketajaman tepi). Karena seluruh data pelatihan tahap ini sintetis dan berlabel presisi, guru mempelajari batas objek yang tajam tanpa gangguan derau sensor.

### Tahap 2 — Pelabelan Semu pada Citra Nyata

Guru yang telah dilatih dipakai untuk memprediksi peta kedalaman pada lebih dari 62 juta citra nyata tanpa label yang dikumpulkan dari berbagai sumber publik. Prediksi ini menjadi label semu: bukan kebenaran lapangan asli, melainkan taksiran dari model guru yang dipakai sebagai target pelatihan tahap berikutnya. Skala data pada tahap ini jauh lebih besar daripada tahap sintetis, sehingga menyuntikkan keragaman skenario dunia nyata yang tidak dimiliki data sintetis.

### Tahap 3 — Melatih Siswa dengan Distilasi

Model siswa berukuran Small (24,8 juta parameter), Base (97,5 juta parameter), atau Large (335,3 juta parameter) dilatih pada label semu dari Tahap 2. Proses ini disebut distilasi karena pengetahuan model besar (guru) dipindahkan ke model kecil (siswa) lewat label yang dihasilkan guru, bukan lewat pelatihan langsung pada label kebenaran manusia. Karena label semu berjumlah puluhan juta dan berasal dari guru yang tajam, siswa memperoleh generalisasi luas sekaligus ketajaman tepi, dengan biaya komputasi inferensi jauh lebih rendah daripada guru.

Alur tiga tahap tersebut dapat diringkas sebagai berikut:

```
Tahap 1: 595rb citra sintetis (label presisi)
         -> latih guru ViT-Giant/DINOv2-G (1,3B parameter)

Tahap 2: guru terlatih -> prediksi kedalaman
         pada 62 juta+ citra nyata tanpa label
         -> dihasilkan label semu (pseudo-label)

Tahap 3: label semu -> latih siswa
         (Small 24,8M / Base 97,5M / Large 335,3M)
         -> model akhir: tajam + tahan variasi domain
```

### Varian Metrik

Selain model kedalaman relatif (hanya urutan jarak antarpiksel, tanpa satuan fisik), penulis juga merilis model kedalaman metrik (dengan satuan meter) hasil penyetelan halus (*fine-tuning*) dari varian Small dan Base pada dataset indoor dan outdoor terpisah, untuk kasus penggunaan yang membutuhkan jarak absolut.

### DA-2K: Tolok Ukur Evaluasi Baru

Penulis membangun DA-2K, tolok ukur berisi 1.000 citra beresolusi tinggi dan 2.000 anotasi kedalaman relatif berpasangan pada delapan jenis skenario (indoor, outdoor, non-foto/render, permukaan transparan-reflektif, gaya visual tidak lazim, pandangan udara, bawah air, dan objek close-up). Setiap anotasi berupa dua titik pada satu citra dengan label titik mana yang lebih dekat ke kamera. Evaluasi dilakukan sebagai akurasi peringkat berpasangan (*pairwise ranking accuracy*): model dinyatakan benar bila kedalaman prediksinya di kedua titik menghasilkan urutan yang sama dengan anotasi. Format ini berbeda dari tolok ukur kedalaman padat konvensional (seperti NYU Depth v2 atau KITTI) yang menuntut peta kedalaman piksel demi piksel; DA-2K cukup menuntut model membedakan mana yang lebih dekat pada pasangan titik yang menantang, sehingga lebih murah dianotasi sekaligus tetap menguji pemahaman geometris model pada skenario ekstrem.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tolok ukur zero-shot (model diuji pada dataset yang tidak pernah dilihat saat pelatihan) untuk kedalaman relatif, dibandingkan dengan Depth Anything V1 dan metode berbasis difusi seperti Marigold dan GeoWizard (model yang memakai proses difusi citra untuk memprediksi kedalaman). Dua sumbu pembanding utama adalah kualitas detail (ketajaman tepi objek, terutama struktur tipis) dan efisiensi komputasi.

Pada sumbu efisiensi, model Depth Anything V2 dilaporkan lebih dari sepuluh kali lebih cepat dibandingkan model berbasis difusi, dengan jumlah parameter lebih kecil dan akurasi lebih tinggi pada DA-2K. Interpretasinya: pendekatan distilasi umpan-maju satu tahap (satu kali lintasan jaringan tanpa proses iteratif difusi) memberi keunggulan kecepatan besar dibandingkan model difusi yang memerlukan banyak langkah denoising per prediksi, sambil tetap unggul pada uji ketajaman.

Pada sumbu kualitas terhadap V1, penulis melaporkan bahwa V2 menghasilkan detail lebih halus pada tepi objek dan permukaan tipis, serta prediksi lebih konsisten pada permukaan transparan dan reflektif, dievaluasi baik secara visual maupun lewat skor pada DA-2K. Angka akurasi numerik spesifik per model dan per dataset pada tolok ukur DA-2K serta tabel perbandingan lengkap dengan MiDaS tidak dikutip di sini karena perlu diverifikasi langsung pada tabel naskah asli.

Model metrik hasil penyetelan halus dari varian Small dan Base diuji pada dataset kedalaman indoor dan outdoor terpisah, menunjukkan bahwa arsitektur yang sama dapat disesuaikan untuk keluaran bersatuan fisik tanpa mengubah tulang punggung.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah pemisahan yang jelas antara sumber ketajaman label (sintetis) dan sumber keragaman domain (nyata tanpa label lewat distilasi), yang terbukti menghasilkan model lebih tajam daripada pelatihan langsung pada label kedalaman nyata. Rilis empat ukuran model memberi keleluasaan memilih titik keseimbangan antara akurasi dan biaya komputasi, dan tolok ukur DA-2K mengisi kekosongan evaluasi pada skenario yang selama ini jarang diuji (permukaan reflektif, pandangan udara, bawah air).

Dari sisi konseptual, keterbatasan utama adalah keluaran model dasar tetap berupa kedalaman relatif, bukan metrik; jarak absolut hanya tersedia lewat penyetelan halus tambahan pada dataset berlabel metrik, yang berarti akurasi metriknya bergantung pada kesesuaian domain data penyetelan tersebut dengan domain penerapan. Dari sisi rekayasa, kualitas seluruh rantai distilasi bergantung pada kualitas guru sintetis; bila lima dataset sintetis yang dipakai tidak mencakup suatu kategori objek atau tekstur permukaan, kesalahan itu berpotensi diturunkan ke label semu dan akhirnya ke model siswa. Model Giant berparameter 1,3 miliar juga tetap mahal untuk penerapan pada perangkat terbatas dibandingkan varian Small, sehingga pemilihan ukuran model tetap memerlukan pertimbangan sumber daya komputasi target.

## Kaitan dengan Bab Lain

Bab ini melanjutkan langsung [071 - 2024 - Depth Anything - Estimasi Kedalaman](./071%20-%202024%20-%20Depth%20Anything%20-%20Estimasi%20Kedalaman.md), mewarisi pola distilasi memakai citra tanpa label berskala besar dan memperbaiki sumber label guru dari data nyata kasar menjadi data sintetis presisi. Dibandingkan [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md), yang berfokus pada penyatuan kedalaman relatif dan metrik dalam satu arsitektur, Depth Anything V2 memisahkan kedua tugas tersebut: model dasar relatif dan model metrik disetel halus terpisah. Terhadap [177 - 2023 - Metric3D - Estimasi Kedalaman](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md), yang menyasar kedalaman metrik lintas kamera secara langsung, bab ini menawarkan jalur alternatif berupa fondasi relatif yang baru diberi satuan metrik pada tahap akhir. Terhadap [178 - 2024 - Marigold - Estimasi Kedalaman](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md), yang memakai model difusi, bab ini menjadi pembanding langsung pada sumbu kecepatan karena pendekatan umpan-maju satu tahap Depth Anything V2 dilaporkan jauh lebih cepat. Terhadap [179 - 2022 - NeWCRFs - Estimasi Kedalaman](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md), yang mewakili pendekatan *supervised* konvensional pada dataset kedalaman metrik tunggal, bab ini menunjukkan jalur berbeda yang mengandalkan skala data lewat distilasi alih-alih anotasi manual per dataset.

## Poin untuk Sitasi

Kutip dengan kunci `yang2024depthanythingv2`. Ringkasan yang aman dikutip: "Depth Anything V2 melatih model guru ViT-Giant/DINOv2-G pada 595 ribu citra sintetis berlabel presisi, memakainya untuk melabeli semu lebih dari 62 juta citra nyata, lalu mendistilasi hasilnya ke model siswa berukuran Small hingga Large, menghasilkan kedalaman relatif yang lebih tajam dan lebih cepat dari 10x dibandingkan model berbasis difusi seperti Marigold, dievaluasi lewat tolok ukur baru DA-2K (1.000 citra, 2.000 anotasi kedalaman relatif berpasangan)." Jumlah parameter (24,8M/97,5M/335,3M/1,3B), jumlah citra sintetis (595K), jumlah citra nyata (62M+), dan komposisi lima dataset sintetis (BlendedMVS, Hypersim, IRS, TartanAir, VKITTI2) berasal dari naskah dan repositori resmi. Angka akurasi numerik spesifik pada tabel DA-2K per model, tabel perbandingan lengkap dengan MiDaS, dan detail hasil model metrik indoor/outdoor belum terverifikasi dari tabel naskah asli dan wajib dicek ulang sebelum dikutip dalam karya formal.
