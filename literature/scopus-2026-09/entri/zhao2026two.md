# A two-stage fine-tuning strategy for 3D object segmentation from multi-view images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2026two` |
| Judul asli | A two-stage fine-tuning strategy for 3D object segmentation from multi-view images |
| Penulis | Zhao, Jiangsan; Geipel, Jakob; Kusnierek, Krzysztof; Cui, Xuean |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [zhao2026two.pdf](../pdf/zhao2026two.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102443

## Gambaran Umum
Makalah ini mengusulkan InvNeRF-Seg (*Input-substitution NeRF for Segmentation*), strategi *fine-tuning* dua tahap untuk segmentasi objek 3D pada adegan yang direkonstruksi dengan *Neural Radiance Fields* (NeRF) dari citra multi-pandang. Tahap pertama melatih NeRF standar pada citra RGB. Tahap kedua melanjutkan pelatihan model yang sama dengan masker segmentasi 2D yang diformat sebagai masukan menyerupai RGB, tanpa mengubah arsitektur maupun fungsi *loss*. Awan titik 3D hasil segmentasi kemudian dikelompokkan untuk menghitung objek.

Data berupa dataset sintetis FruitNeRF (pohon apel dan persik) dan satu tanaman kedelai nyata yang direkam penulis dengan iPhone 12 Pro (149 citra setelah bingkai buram dibuang). Pada kebenaran dasar 283 apel dan 152 persik, InvNeRF-Seg menghitung 282 apel dan 155 persik, sedangkan FruitNeRF (BCE) menghitung 294 dan 160, SA3D berbasis bobot 351 dan 328, dan SA3D berbasis kepadatan 1.573 dan 1.249 (Tabel 1). Pengujian pada tanaman nyata hanya mencakup satu polong dan dua polong dari satu tanaman, dinilai secara kualitatif untuk awan titik 3D.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Segmentasi objek 3D di dalam adegan NeRF masih terbatas. Metode klasik seperti PointNet dan PointNet++ memerlukan anotasi awan titik 3D yang mahal. SA3D memproyeksikan masker 2D ke adegan tanpa pelatihan ulang sehingga menghasilkan awan titik berderau karena medan kepadatan tidak dioptimalkan. FruitNeRF menambahkan cabang segmentasi dan melatihnya bersama RGB, yang menurut penulis memaksa model menyeimbangkan dua tujuan berbeda dan kurang optimal, terutama untuk objek kecil karena kontribusi *loss* segmentasi lebih kecil daripada *loss* RGB.

Penulis mencatat bahwa melatih NeRF langsung pada masker biner dari awal gagal total dan menghasilkan keluaran hitam tanpa struktur kedalaman (Gambar 1), karena masker biner tidak memiliki gradien fotometrik yang mulus.

## Ide Utama
NeRF yang telah mempelajari geometri dari citra RGB dapat diubah medan kepadatannya agar terfokus pada objek latar depan dengan melanjutkan pelatihan pada masker biner yang diformat sebagai citra RGB ([1,1,1] untuk objek, [0,0,0] untuk latar). Strategi ini disebut penulis sebagai "geometri dahulu, semantik kemudian". Kontribusinya adalah resep pelatihan yang tidak mengubah arsitektur, bukan modul atau *loss* baru.

Dua pos pemeriksaan (*checkpoint*) disimpan terpisah: model tahap 1 untuk rendering fotometrik dan model tahap 2 khusus untuk segmentasi dan ekstraksi awan titik.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Data sintetis berasal dari dataset FruitNeRF publik (apel dan persik) yang sudah memuat masker segmentasi, intrinsik kamera, dan pose. Data nyata berupa video satu tanaman kedelai dewasa dengan polong terlihat, direkam dengan iPhone 12 Pro dalam cahaya matahari terang sambil menggerakkan kamera mengitari tanaman. Bingkai diekstraksi dengan FFmpeg pada 5 bingkai per detik, pose diestimasi dengan COLMAP, dan 149 citra bersih dipertahankan. Masker polong dibuat dengan AnyLabeling dan MobileSAM, lalu diverifikasi manual. Dua tugas didefinisikan: segmentasi 3D biner satu polong dan segmentasi multi-instans dua polong.

### 2. Tahap 1: NeRF pada RGB
Model Nerfacto dari Nerfstudio dengan konfigurasi bawaan (`hidden_dim` 64, `hidden_dim_color` 64, `appearance_embed_dim` 32), dilatih 4.000 *epoch*. Laju belajar 1 × 10⁻² untuk jaringan medan dan proposal serta 1 × 10⁻⁴ untuk pengoptimal kamera. Untuk kedelai, kapasitas dinaikkan (dimensi tersembunyi 128) dan bidang jauh (*far plane*) diturunkan menjadi 2; untuk apel dan persik dipakai nilai bawaan 1000.

### 3. Tahap 2: *fine-tuning* dengan masker
Seluruh jaringan dilatih 6.000 *epoch* tambahan dengan laju belajar diturunkan 100 kali, memakai MSE terhadap masker biner. FruitNeRF dilatih total 6.000 *epoch* dengan konfigurasi lain yang sama agar anggaran pelatihan setara.

### 4. Pengelompokan dan penghitungan
Semua metode memakai alur yang sama: DBSCAN (`eps` = 0,0065, `min_samples` = 3), lalu pemecahan rekursif klaster besar dengan KMeans berdasarkan statistik ukuran dan volume. Dua varian SA3D dibandingkan: berbasis bobot (ambang τ = 0,1) dan berbasis kepadatan mentah (σ ≥ 70).

### 5. Metrik
PSNR untuk mutu citra RGB, IoU untuk masker hasil render, dan akurasi hitungan buah untuk mutu awan titik 3D. Uji-t dua sisi dengan SciPy 1.15.2 untuk signifikansi.

## Eksperimen dan Hasil
Kualitas citra RGB (PSNR) antara InvNeRF-Seg dan FruitNeRF tidak berbeda signifikan. IoU masker InvNeRF-Seg lebih tinggi secara signifikan (p < 0,001) untuk apel dan persik. Pada tanaman kedelai, IoU lebih tinggi dengan p < 0,01 dan PSNR tidak berbeda signifikan; nilai numerik IoU dan PSNR hanya disajikan pada gambar, bukan di teks.

Tabel 1: hitungan buah pada kebenaran dasar 283 apel dan 152 persik.

| Metode | Apel (GT = 283) | Persik (GT = 152) |
|---|---|---|
| InvNeRF-Seg | 282 | 155 |
| FruitNeRF (BCE) | 294 | 160 |
| FruitNeRF (MSE) | 289 | 156 |
| SA3D (kepadatan) | 1.573 | 1.249 |
| SA3D (bobot) | 351 | 328 |

Tabel 2: ablasi strategi *fine-tuning*.

| Strategi | Apel | Persik |
|---|---|---|
| Keduanya (InvNeRF-Seg) | 282 | 155 |
| Hanya kepadatan | 281 | 157 |
| Hanya warna | 294 | 154 |

Pelatihan dari awal pada masker gagal (IoU sekitar nol). *Fine-tuning* hanya kepadatan lambat (sekitar 3.000 *epoch* sebelum IoU membaik), sedangkan hanya warna cepat konvergen tetapi menghasilkan awan titik lebih berderau. Mengganti BCE menjadi MSE pada FruitNeRF memberi IoU akhir sebanding, sehingga penulis menyimpulkan keunggulan berasal dari strategi dua tahap, bukan fungsi *loss*. Pada kedelai, *fine-tuning* satu polong gagal dengan bidang jauh 1000 dan berhasil dengan nilai 2. Segmentasi dua polong sedikit lebih buruk daripada kasus biner, dengan beberapa titik salah klasifikasi di dekat batas instans. Analisis kepadatan medan menunjukkan kepadatan di wilayah objek meningkat dan di latar menurun.

## Kelebihan dan Keterbatasan
Kelebihan: arsitektur dan *loss* NeRF tidak berubah; tidak memerlukan anotasi 3D; awan titik cukup terpisah sehingga pengelompokan non-terlatih (DBSCAN) memberi hitungan yang dekat dengan kebenaran dasar; perbandingan memakai anggaran pelatihan dan alur pengelompokan yang sama.

Keterbatasan yang dinyatakan penulis: metode bergantung pada citra RGB multi-pandang yang akurat dan masker 2D berkualitas tinggi serta konsisten antar-pandang; ekstensi multi-instans dengan masker berintensitas menunjukkan ambiguitas batas karena sifat regresi MSE; validasi terutama pada data pertanian; metrik 3D padat (jarak Chamfer, IoU 3D) tidak dapat dihitung karena tidak ada kebenaran dasar per titik; validasi nyata berskala kecil (satu tanaman, satu sampai dua polong) dan dinilai kualitatif; ambang mutu masukan tempat metode gagal tidak ditentukan.

Menurut pembacaan ringkasan ini, hitungan hanya diuji pada satu adegan apel dan satu adegan persik sintetis, sehingga selisih hitungan (misalnya 282 terhadap 283) tidak disertai pengulangan atau sebaran, dan klaim kinerja unggul tidak dapat dinilai ketahanannya. Menurut pembacaan ringkasan ini, bidang jauh perlu disetel pada objek kecil sehingga metode tidak sepenuhnya bebas penyetelan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani identitas buah lintas pandang secara implisit melalui rekonstruksi 3D: citra multi-pandang dengan pose kamera diketahui dipadukan dalam satu medan kepadatan, sehingga buah yang sama pada beberapa citra menjadi satu klaster pada awan titik 3D yang dihitung dengan DBSCAN. Identitas ditetapkan di ruang 3D, bukan melalui pencocokan antar-citra atau pelacakan.

Hitungan tidak dilaporkan per kelas (hanya total apel dan total persik pada dua adegan sintetis, ditambah satu dan dua polong kedelai). Acuan hitungnya adalah jumlah objek sintetis pada dataset FruitNeRF (anotasi berupa jumlah buah). Untuk kedelai tidak ada acuan hitung penuh. Bagi pencacahan tandan sawit multi-sisi, yang dapat dipindahkan adalah gagasan menghitung klaster pada awan titik 3D yang menyatukan banyak pandang, serta pelajaran bahwa medan kepadatan yang bersih menentukan keberhasilan penghitungan. Syaratnya adalah pose kamera yang akurat dan masker yang konsisten antar-pandang. Makalah tidak menguji pohon nyata berskala kebun atau buah dengan oklusi tinggi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhao2026two`.

Zhao dkk. mengusulkan InvNeRF-Seg, strategi dua tahap yang melatih NeRF pada citra RGB lalu menyetelnya dengan masker 2D sebagai masukan menyerupai RGB tanpa mengubah arsitektur atau *loss*, sehingga awan titik 3D yang disegmentasi lebih bersih. Pada kebenaran dasar 283 apel dan 152 persik sintetis, metode ini menghitung 282 dan 155 buah, dibandingkan 294 dan 160 untuk FruitNeRF (BCE) serta 351 dan 328 untuk SA3D berbasis bobot, dengan validasi nyata yang kecil dan kualitatif pada polong kedelai.

Catatan verifikasi data: Hitungan buah ada pada Tabel 1, ablasi pada Tabel 2, dan jumlah 149 citra kedelai serta parameter pelatihan pada Bagian 4.1 dan 4.2. Nilai numerik IoU, PSNR, dan nilai p hanya tampil pada Gambar 3 dan Gambar 7 serta di teks (p < 0,001 dan p < 0,01); angka IoU tidak dapat diverifikasi dari teks. Jumlah citra dataset sintetis FruitNeRF tidak dilaporkan pada makalah ini. Tabel pada ekstraksi teks terbaca utuh.
