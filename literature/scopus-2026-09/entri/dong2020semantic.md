# Semantic mapping for orchard environments by merging two-sides reconstructions of tree rows

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dong2020semantic` |
| Judul asli | Semantic mapping for orchard environments by merging two-sides reconstructions of tree rows |
| Penulis | Dong, Wenbo; Roy, Pravakar; Isler, Volkan |
| Tahun | 2020 |
| Venue | Journal of Field Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [dong2020semantic.pdf](../pdf/dong2020semantic.pdf)
- DOI resmi: https://doi.org/10.1002/rob.21876

## Gambaran Umum

Makalah ini (Dong, Roy, dan Isler, Universitas Minnesota; versi arXiv 1809.00075v4, Januari 2020) menyajikan sistem penglihatan untuk membangun model 3D baris pohon apel dari dua sisi baris, lalu mengukur sifat semantik: diameter batang, tinggi pohon, volume kanopi, dan jumlah buah. Masalah intinya adalah rekonstruksi sisi depan dan sisi belakang baris hampir tidak tumpang tindih sehingga tidak dapat digabungkan dengan *Iterative Closest Point* (ICP) maupun *Structure from Motion* (SfM) biasa. Data berasal dari kamera RGB atau RGB-D (Intel RealSense R200) yang dibawa pada tongkat di kebun apel Universitas Minnesota.

Metode yang diusulkan menyelaraskan dua rekonstruksi memakai simetri batas oklusi proyeksi ortografis dan kesejajaran batang pohon serta bidang tanah lokal, kemudian menyempurnakannya dengan *semantic bundle adjustment*. Hasil utama untuk pencacahan: pada tiga set data RGB (Dataset-IV, V, VI), hitungan gabungan dua sisi mencapai 91,98% sampai 94,81% dari jumlah buah yang dipanen, sedangkan penjumlahan hitungan dua sisi tanpa penggabungan mencapai 101,93% sampai 150%. Pada set data RGB-D, galat rerata diameter batang sekitar 0,49 cm (dua sisi) dan galat rerata tinggi pohon 0,038 m.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pengukuran sifat fenotipe pohon buah (tinggi, volume kanopi, diameter batang) dan hasil panen secara manual memakan tenaga dan kurang akurat. Model 3D baris pohon dapat memberi ukuran itu secara otomatis, dan dapat dipakai untuk melacak buah antarcitra serta menghindari penghitungan ganda buah yang terlihat dari kedua sisi baris. Pada pohon apel yang diperlihatkan pada Gambar 1b, sebagian besar apel terlihat dari kedua sisi dan akan terhitung dua kali pada pemindaian satu sisi yang independen.

Pada kebun modern berkepadatan tinggi, pohon ditanam rapat dan dihubungkan kawat penyangga sehingga pemindaian mengelilingi tiap pohon tidak mungkin; kamera bergerak di lorong antarbaris, dan baris dapat memanjang ratusan hingga lebih dari seribu meter. Dua sisi dipotret terpisah dan hampir tidak berbagi permukaan kanopi. Galat pose kamera yang terakumulasi akibat fitur yang tidak stabil karena angin juga membuat pohon tidak sejajar antarsisi. Penulis melaporkan bahwa ORB-SLAM2 sering kehilangan jejak dan deteksi lintasan tertutup (*loop closure*) tidak andal karena kemiripan antarpohon; walaupun lintasan tertutup benar, batang dari dua sisi tetap tidak sejajar. ICP gagal bahkan dengan korespondensi manual. RTK GPS dapat menyelesaikan registrasi tetapi mahal.

## Ide Utama

Pengamatan kunci penulis adalah bahwa proyeksi ortografis batas oklusi pohon pada bidang fronto-paralel dari sisi yang berlawanan bersifat simetris. Bersama asumsi adanya bidang tanah yang sama dan batang yang kira-kira silinder, pengamatan ini memberi penyelarasan awal tanpa tumpang tindih tampilan dan tanpa GPS. Penyelarasan itu lalu disempurnakan dengan objek semantik (silinder batang dan bidang tanah lokal) yang dilihat dari kedua sisi dan dimasukkan ke dalam *bundle adjustment* sehingga pose kamera dan titik 3D dikoreksi bersamaan.

Pada tahap pencacahan, penggabungan dua sisi memungkinkan buah yang sama pada kedua sisi dikenali melalui klaster 3D yang beririsan, dan jumlahnya digabung dengan prinsip inklusi-eksklusi.

## Cara Kerja Langkah demi Langkah

```
 Video sisi depan --> rekonstruksi 3D (SfM/SLAM) --+
                                                     +--> penyelarasan awal
 Video sisi belakang -> rekonstruksi 3D ------------+     (PCA, batas oklusi, batang)
                                                              |
 deteksi batang (Mask R-CNN) -> silinder batang, bidang tanah |
                                                              v
                                          semantic bundle adjustment
                                                              |
              diameter batang, tinggi, volume kanopi, jumlah apel
```

### 1. Akuisisi data

Kamera Intel RealSense R200 dipasang pada tongkat dan menangkap data RGB atau RGB-D dari pandangan horizontal atau atas-miring; tiap sisi baris dipindai terpisah. Tiga set data RGB-D: Dataset-I (968 citra, 30 fps, 1920 x 1080, 21 pohon, banyak gulma, kecepatan kamera sekitar 1 m/s), Dataset-II (2394 citra, 60 fps, 640 x 480, 27 pohon, fokus batang), Dataset-III (2020 citra, 60 fps, 640 x 480, 30 pohon, pandangan atas-miring). Tiga set data RGB: Dataset-IV (873 citra, enam pohon, 270 apel), Dataset-V (1065 citra, sepuluh pohon, 274 apel), Dataset-VI (831 citra, enam pohon, 414 apel, campuran apel merah dan hijau). Kultivar tidak dilaporkan.

### 2. Rekonstruksi satu sisi

Transformasi relatif antarbingkai dihitung dengan RANSAC tiga titik pada kecocokan SIFT, disempurnakan dengan *bundle adjustment* berpasangan, deteksi lintasan tertutup dengan model *Bag of Words*, optimasi graf pose, dan *bundle adjustment* global. Untuk data RGB-D, galat kedalaman dari kamera inframerah stereo dimasukkan ke fungsi objektif. Untuk data RGB, peta kedalaman dibuat dari rekonstruksi padat satu sisi memakai Agisoft.

### 3. Penyelarasan awal dua sisi

Langkahnya: (a) estimasi bidang tanah dengan RANSAC dan analisis komponen utama (PCA) untuk menyamakan rotasi, skala diatur dengan median tinggi pohon; (b) translasi pada bidang XY dihitung dengan mencocokkan batas oklusi (alpha shape) dari proyeksi ortografis memakai *Coherent Point Drift* (CPD); (c) kedalaman disejajarkan dengan bidang median batang. Solusi awal ini menjadi titik awal optimasi Levenberg-Marquardt.

### 4. Pemodelan batang dan tanah lokal

Batang dideteksi dengan Mask R-CNN (ResNet-101, FPN, implementasi Matterport) yang dilatih pada 1000 citra dengan sekitar 2000 instans dari lima kebun; pembagian per kebun uji memakai 90% citra dari empat kebun lain dan 50% citra kebun uji. Titik batang dipasangkan pada silinder dengan RANSAC dan batasan 2D, dan bidang tanah lokal diestimasi dengan RANSAC yang dimodifikasi memakai arah sumbu batang. Transformasi awal sisi belakang ke sisi depan dihitung dari sedikitnya dua batang dan satu tanah lokal.

### 5. *Semantic bundle adjustment*

Silinder batang dan bidang tanah dari kedua sisi dimasukkan sebagai objek dengan pose dan bentuk tersendiri, dan titik yang berasal dari objek yang sama dikenai penalti jarak ke permukaan objek. Optimasi memakai Ceres Solver.

### 6. Ukuran morfologi dan pemetaan hasil

Diameter batang diestimasi dari kedua sisi. Pohon dipisahkan dengan algoritma *shrink-and-expand* berbasis alpha shape, volume kanopi dihitung dari alpha shape (radius 0,8 m), dan tinggi diambil dari kotak pembatas. Untuk pemetaan hasil, apel dideteksi dengan metode segmentasi penulis sebelumnya; pada RGB, titik 3D yang beririsan dengan masker apel dikelompokkan (komponen terhubung), tiap klaster 3D dihitung dari tiga bingkai dengan piksel apel terbanyak (median) memakai metode pencacahan penulis sebelumnya, dan apel di tanah dibuang. Hitungan dari klaster yang beririsan antara dua sisi digabung dengan prinsip inklusi-eksklusi.

## Eksperimen dan Hasil

Deteksi batang (Tabel 1) pada lima kebun uji: AP50 antara 93,3 dan 98,3, AP antara 50,8 dan 63,9, dan AP75 antara 55,4 dan 72,8. Rentang AP50 ini dari lima baris tabel; nilai per kebun ada di tabel makalah.

Diameter batang (Dataset-II, 14 dari 27 pohon, acuan jangka sorong, Tabel 2) dan tinggi pohon (Dataset-III, 14 dari 30 pohon, acuan tongkat ukur, Tabel 3):

| Ukuran | Galat rerata dua sisi | Galat rerata sisi depan | Galat rerata sisi belakang |
|---|---|---|---|
| Diameter batang (cm) | 0,49 | 0,54 | 0,59 |
| Tinggi pohon (m) | 0,038 | 0,059 | 0,052 |

Volume kanopi (Tabel 4, rerata enam kelompok pohon dari 18 pohon Dataset-III): alpha shape 1,227 sampai 1,912 m³; gabungan dua sisi dengan *convex hull* 1,322 sampai 2,202 m³; *convex hull* dua sisi yang dijumlahkan 2,265 sampai 3,465 m³; asumsi silinder 2,185 sampai 3,307 m³. Tidak ada acuan volume sebenarnya; penulis menyimpulkan model silinder dan penjumlahan dua sisi melebih-lebihkan volume.

Pencacahan buah (Tabel 5), dibandingkan dengan jumlah apel yang dipanen:

| Set data | Hitungan panen | Gabungan dua sisi | Penjumlahan hitungan satu sisi |
|---|---|---|---|
| Dataset-IV | 270 | 256 (94,81%) | 348 (128,89%) |
| Dataset-V | 274 | 252 (91,98%) | 411 (150%) |
| Dataset-VI | 414 | 392 (94,68%) | 422 (101,93%) |

Proporsi apel yang terlihat dari satu sisi terhadap total yang dipanen bervariasi besar antarset data; teks menyebut 54,59% sampai 79,83%, sedangkan keterangan Gambar 30 menyebut 40,85% sampai 79,83%. Waktu pemrosesan pada Dataset-I (Tabel 6): rekonstruksi satu sisi sekitar 15 menit, penyelarasan awal sekitar 3 menit, *semantic BA* sekitar 8 menit, estimasi hasil sekitar 6 menit.

## Kelebihan dan Keterbatasan

Kelebihan: pencacahan dari kedua sisi dibandingkan langsung dengan hasil panen; dua baseline (penjumlahan hitungan satu sisi, pencacahan satu sisi) ditampilkan dalam angka; metode hanya membutuhkan kamera RGB atau RGB-D tanpa GPS; dan hasil lebih konsisten antarset data daripada penjumlahan sederhana.

Keterbatasan yang dinyatakan penulis: penyelarasan awal gagal bila rekonstruksi dua sisi tidak cukup akurat atau tidak berbagi pohon (contoh: sisi depan hanya merekonstruksi empat dari sepuluh pohon dan sisi belakang enam pohon lain); detektor batang bermasalah pada pohon dorman tanpa daun dan memerlukan sedikit data tambahan dari kebun baru; hasil diameter untuk batang kecil melebih-lebihkan karena kamera jauh; segmentasi pohon dirancang untuk kebun modern dengan pohon yang masih berjarak; proses SfM satu sisi lambat (sekitar 15 menit). Pada Dataset-I hanya tiga batang dan tiga tanah lokal yang dipakai karena gulma.

Menurut pembacaan ringkasan ini: (a) hitungan gabungan selalu di bawah hasil panen (91,98% sampai 94,81%), sehingga ada kecenderungan menghitung kurang yang tidak dibahas penyebabnya; (b) hanya tiga set data pencacahan dengan total 22 pohon dan hitungan hanya agregat per set data, tanpa galat per pohon; (c) satu kultivar atau satu lokasi kebun (kultivar tidak dilaporkan), dengan pohon yang cenderung planar atau semiplanar; (d) tidak ada hitungan per kelas atau atribut buah; (e) klaim bahwa metode dapat digeneralisasi ke jeruk dan persik adalah rencana penulis dan belum didukung hasil.

## Kaitan dengan Tinjauan main6

Makalah ini menangani secara langsung buah yang terlihat dari dua sisi. Mekanismenya adalah rekonstruksi 3D dua sisi yang diselaraskan melalui landmark nonbuah (batang, tanah, batas oklusi), sehingga klaster buah dari sisi depan dan belakang berada dalam satu kerangka koordinat; irisan klaster 3D antarsisi digabung dengan prinsip inklusi-eksklusi. Ini sejenis koreksi hitungan dua sisi berbasis geometri, bukan pencocokan kemiripan penampilan buah. Hitungan tidak dilaporkan per kelas; hanya jumlah apel total. Acuan hitungnya adalah jumlah buah yang dipanen (*harvested fruit count*) per set data, bukan anotasi citra; anotasi tangan hanya dipakai untuk menaksir proporsi apel yang terlihat dari satu sisi.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: gagasan menyelaraskan rekonstruksi sisi yang tidak tumpang tindih lewat landmark yang terlihat dari semua sisi, serta bukti kuantitatif bahwa penjumlahan hitungan sisi tanpa penggabungan melebihkan hitungan (hingga 150% dari panen) sedangkan penggabungan geometri menurunkannya ke 91,98% sampai 94,81%. Pada sawit, batang pohon dan tanah di sekitar pohon dapat menjadi landmark serupa, tetapi struktur pohon sawit berbeda (satu pohon dipindai dari 4 sampai 8 sisi dengan lintasan mengelilingi pohon, bukan dua sisi baris), sehingga asumsi simetri proyeksi ortografis dua sisi tidak langsung berlaku.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `dong2020semantic`.

Dong dkk. (2020) menggabungkan rekonstruksi 3D sisi depan dan belakang baris pohon apel yang tidak saling tumpang tindih dengan penyelarasan awal berbasis simetri batas oklusi dan landmark batang serta tanah, dilanjutkan *semantic bundle adjustment*. Pada tiga set data RGB, hitungan apel gabungan dua sisi mencapai 91,98% sampai 94,81% dari jumlah yang dipanen, sedangkan penjumlahan hitungan satu sisi mencapai 101,93% sampai 150%; sistem ini juga menghasilkan galat rerata diameter batang 0,49 cm dan tinggi pohon 0,038 m pada set data RGB-D.

Catatan verifikasi data: hasil pencacahan berasal dari Tabel 5 (persentase ada di tabel; persentase dihitung terhadap hitungan panen). Galat diameter batang berasal dari Tabel 2 (rerata 0,49 cm, galat sisi depan 0,54 cm, sisi belakang 0,59 cm) dan galat tinggi dari Tabel 3 (rerata 0,038 m, sisi depan 0,059 m, sisi belakang 0,052 m). Rentang AP50 dan AP pada deteksi batang dirangkum dari Tabel 1. Volume kanopi dari Tabel 4; waktu proses dari Tabel 6. Teks Gambar 30 dan teks utama seksi 5.3 berbeda untuk batas bawah proporsi apel yang terlihat dari satu sisi (40,85% berbanding 54,59%), dan perbedaan itu dicatat apa adanya. Hitungan jumlah pohon pada Dataset-IV sampai VI diambil dari seksi 5.1. Tidak dapat diverifikasi dari teks: kultivar apel, galat per pohon pada pencacahan, dan galat metode pada selisih hitungan akibat apel yang tersembunyi dari kedua sisi. Matriks pada persamaan 10 terbaca terpotong dalam ekstraksi sehingga tidak diringkas. Teks makalah berbahasa Inggris.
