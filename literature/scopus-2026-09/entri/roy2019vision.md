# Vision-based preharvest yield mapping for apple orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `roy2019vision` |
| Judul asli | Vision-based preharvest yield mapping for apple orchards |
| Penulis | Roy, Pravakar; Kislay, Abhijeet; Plonski, Patrick A.; Luby, James; Isler, Volkan |
| Tahun | 2019 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [roy2019vision.pdf](../pdf/roy2019vision.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2019.104897

## Gambaran Umum
Makalah ini menyajikan sistem penglihatan komputer menyeluruh untuk memetakan hasil panen kebun apel dari video yang direkam satu kamera monokular. Sistem tidak bergantung pada platform (kamera dapat dipasang pada robot darat, UAV, atau dipegang tangan) dan tidak memerlukan pencahayaan khusus. Data diambil di Horticultural Research Center, University of Minnesota (Victoria, Minnesota), pada tahun 2015 dan 2016, dengan berbagai varietas apel (merah, emas, hijau, kuning, dan campurannya) dan kondisi cuaca cerah, teduh, dan berawan.

Tiga komponen utama dikembangkan: segmentasi apel semi-terawasi berbasis warna (superpiksel SLIC pada ruang warna LAB, *Gaussian mixture model* atau GMM, dan pencocokan dengan KL divergence), penghitungan apel pada gugus apel yang saling tumpang tindih dengan GMM berbasis kriteria *minimum description length* (MDL) yang dimodifikasi, dan penggabungan hitungan antarbingkai dengan homografi berpasangan. Untuk memperoleh hitungan seluruh baris pohon, hitungan dari kedua sisi baris digabung memakai rekonstruksi 3D (Agisoft) dan prinsip inklusi-eksklusi.

Hasil utama menurut penulis: F1-measure deteksi 0,95 sampai 0,97 (enam video), akurasi penghitungan per bingkai 94,4%, akurasi penghitungan dengan pelacakan 89% sampai 98% terhadap apel yang terlihat dari satu sisi (tujuh video, model terawasi pengguna), dan akurasi estimasi hasil panen dari kedua sisi 91,98% sampai 94,81% pada tiga dataset. Penulis juga menemukan bahwa persentase apel yang terlihat dari satu sisi bervariasi antardataset (40,85% sampai 79,83%).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Tanaman khusus (*specialty crops*) seperti buah memerlukan sistem pemetaan hasil yang praktis, dan menurut penulis kekurangan sistem seperti itu menjadi salah satu hambatan utama penerapan pertanian presisi dan fenotipe pada tanaman tersebut. Sistem terdahulu bersifat khusus untuk tiap tanaman. Sistem yang disebut dalam tinjauan penulis memerlukan pencahayaan buatan malam hari (stereo dengan senter), struktur terowongan untuk menekan variasi cahaya, atau serangkaian sensor (pemindai laser, kamera multispektral, kamera termal).

Ada tiga kesulitan teknis yang dinyatakan. Pertama, warna apel, pencahayaan, bayangan, dan oklusi oleh daun serta ranting menyulitkan identifikasi piksel apel; pendekatan pembelajaran mendalam menuntut data latih besar, dan jaringan konvolusional penuh (FCN) yang penulis latih pada data Bargoti dan Underwood tidak berkinerja baik pada data mereka. Kedua, apel sering berada dalam gugus yang hampir semua anggotanya saling menutupi, sedangkan metode *circular Hough transform* (CHT) memerlukan penyetelan parameter ukuran buah untuk tiap dataset. Ketiga, hitungan dari satu bingkai atau satu sisi baris tidak mencerminkan seluruh buah, sehingga diperlukan registrasi buah antarbingkai dan antarsisi untuk menghindari penghitungan ganda.

## Ide Utama
Sistem tidak mengandalkan deteksi seluruh apel dalam satu bingkai. Asumsinya, untuk setiap apel ada "beberapa" sudut pandang tempat apel itu dapat terdeteksi; karena itu presisi per bingkai dijaga tinggi (selalu di atas 87%) dan recall dicapai dengan memakai banyak bingkai video.

Penghitungan gugus apel dirumuskan sebagai pencocokan campuran Gaussian pada piksel biner: tiap apel adalah satu komponen Gaussian dan jumlah komponen $k$ dipilih dengan kriteria baru. Penulis menyatakan AIC dan BIC cenderung memilih $k$ yang terlalu besar. Kriteria baru memberi imbalan pada komponen yang bundar, menutup area, dan berdensitas piksel tinggi, serta penalti MDL yang dimodifikasi. Hasilnya tidak memerlukan penyetelan parameter dan tidak memerlukan pelatihan.

Untuk hitungan seluruh baris, hitungan tiap sisi tidak boleh dijumlahkan begitu saja karena apel yang terlihat dari kedua sisi terhitung dua kali. Penulis menggabungkan rekonstruksi 3D kedua sisi dengan batasan semantik (permukaan tanah, batang pohon, siluet dedaunan) yang dirujuk dari karya terdahulu, lalu menghitung gabungan gugus apel dengan prinsip inklusi-eksklusi.

## Cara Kerja Langkah demi Langkah

```
  Video -> SLIC (LAB) -> GMM warna -> cocok KL -> topeng apel
  topeng -> komponen terhubung -> GMM spasial -> hitungan per kotak
  SIFT -> homografi antarbingkai -> propagasi kotak -> median hitungan
  dua sisi -> rekonstruksi 3D -> gabung -> inklusi-eksklusi
```

### 1. Akuisisi data
Semua data dikumpulkan di Horticultural Research Center, University of Minnesota, Victoria, Minnesota, selama 2015 sampai 2016. Dataset validasi terdiri atas empat bagian kebun yang dipilih sembarang dan direkam dengan kamera Samsung Galaxy S4 pada September 2016: Dataset1 (6 pohon, 270 apel, sebagian besar merah, pohon cenderung datar), Dataset2 (4 pohon, 568 apel, campuran merah dan hijau, geometri tidak datar, video satu sisi), Dataset3 (10 pohon, 274 apel, sebagian besar merah, tidak datar), dan Dataset4 (6 pohon, 414 apel, campuran merah dan hijau, tidak datar). Total tujuh video validasi. Dataset pelatihan 2015 berisi 76 pohon, direkam dengan kamera Garmin VR pada satu sisi, tanpa anotasi manual dan tanpa hitungan acuan. Frekuensi bingkai video 30 fps.

Ada dua acuan. Acuan tingkat citra diperoleh dengan menganotasi batas tiap apel pada bingkai terpilih (setiap 1 sampai 3 detik), dengan kategori terlihat jelas (lebih dari setengah luas penampang dan setengah keliling tidak tertutup) dan terlihat marginal; kotak anotasi dipropagasi ke bingkai lain dengan gerakan kamera. Acuan hasil panen berupa hitungan fisik: apel ditandai dengan stiker dan dihitung (serta diukur diameternya) setelah panen. Apel di tanah dan pada baris belakang tidak ditandai.

### 2. Segmentasi apel
Tiap bingkai dikonversi ke LAB dan disegmentasi menjadi superpiksel SLIC; tiap superpiksel diwakili rerata L, A, B. Superpiksel dimodelkan sebagai GMM dengan parameter yang diestimasi dengan *expectation maximization* (EM), menghasilkan sekitar 25 kelas warna. Pada fase inisialisasi, pengguna memilih komponen Gaussian yang menangkap apel lewat antarmuka; pada fase pemakaian, komponen bingkai saat ini dicocokkan dengan komponen tersimpan memakai KL divergence, dan superpiksel dalam batas keyakinan 90% dianggap apel. Dua model dibandingkan: model semi-terawasi (dilatih dari data 2015 dan dipakai pada data 2016 tanpa campur tangan pengguna) dan model terawasi pengguna (pengguna memilih apel pada 50 bingkai pertama video). Kecepatan segmentasi 5 sampai 6 bingkai per detik untuk citra 1920×1080 dan 15 bingkai per detik untuk 640×480 pada laptop DELL XPS dengan RAM 16 GB dan memori GPU 2 GB. Apel di bawah satu garis yang dipilih pengguna (apel tanah) diabaikan.

### 3. Penghitungan per bingkai
Analisis komponen terhubung pada topeng biner menghasilkan kotak untuk tiap gugus apel. Di tiap kotak, piksel bukan nol menjadi masukan GMM dengan komponen berkovarians diagonal (pusat apel $\mu_i$, jari-jari $2\sigma_{xi}$ dan $2\sigma_{yi}$). Inisialisasi EM memakai K-means++. Jumlah komponen dipilih dengan $\kappa = \arg\max_k R(G_k) - V(G_k)$, dengan imbalan $R_i$ yang terdiri atas empat suku (kekuatan distribusi, kebundaran lewat $1-\epsilon^2$, cakupan, dan penalti untuk Gaussian yang meliputi area besar tetapi sedikit titik) dan penalti $V = c'(3k)\log(\sum_x I_b(x) \neq 0)$ dengan $c' = 3/2$. Algoritma berjalan 2 sampai 3 fps.

### 4. Penggabungan hitungan antarbingkai
Gerakan kamera dihampiri dengan homografi berpasangan dari kecocokan fitur SIFT di atas tanah (pandangan kamera hampir tetap dan adegan hampir planar). Kotak pada bingkai sebelumnya dipropagasi dengan homografi; kotak dianggap mewakili gugus yang sama bila tumpang tindihnya lebih dari 10%. Aturan: kotak tanpa tumpang tindih membuat daftar hitungan baru; satu kotak yang tumpang tindih menambah hitungan ke daftar; dua kotak atau lebih yang tumpang tindih dengan satu kotak sebelumnya dijumlahkan dan kotaknya digabung. Pada akhir urutan, median daftar hitungan tiap kotak dijumlahkan sebagai hitungan total.

### 5. Penggabungan kedua sisi baris
Tiap sisi direkonstruksi dengan Agisoft PhotoScan, kedua rekonstruksi digabung dengan batasan semantik (dirujuk dari laporan teknis penulis, tidak dirinci dalam makalah ini). Apel yang terdeteksi diproyeksikan balik ke model 3D, gugus 3D dicari dengan komponen terhubung, lalu diproyeksikan kembali ke citra untuk dihitung dengan metode seksi 4. Hitungan sebuah gugus 3D adalah median dari tiga bingkai dengan piksel apel terbanyak. Hitungan kedua sisi digabung dengan persilangan komponen dan prinsip inklusi-eksklusi.

## Eksperimen dan Hasil
Evaluasi segmentasi memakai presisi, recall, dan F1-measure terhadap kotak anotasi manual dengan ambang IoU 0,01 untuk penghitungan. Per bingkai, presisi selalu di atas 87% tetapi recall bervariasi nyata. F1-measure (Tabel 1 makalah, IoU = 0,01) untuk enam video:

| Video | Semi-terawasi | Terawasi pengguna |
|---|---|---|
| D1 (cerah) | 0,9662 | 0,9658 |
| D1 (teduh) | 0,9585 | 0,9609 |
| D3 (cerah) | 0,9738 | 0,9711 |
| D3 (teduh) | 0,9541 | 0,9592 |
| D4 (cerah) | 0,9774 | 0,9775 |
| D2 (cerah) | 0,8931 | 0,9710 |

Pada Dataset2 (campuran merah dan hijau) model semi-terawasi tidak menggeneralisasi dengan baik: presisi serupa tetapi recall turun sekitar 20%. Penulis menyebut F1-measure terbaik yang diketahui dari literatur adalah 0,91 (Bargoti dan Underwood), tetapi menyatakan perbandingan langsung tidak mungkin karena dataset berbeda.

Evaluasi penghitungan per bingkai memakai 5.000 komponen yang dipilih acak dari tujuh video dan diberi hitungan menurut persepsi manusia. Recall turun dengan bertambahnya ukuran gugus (62,7% sampai 99%) tetapi presisi tetap di atas 87% (87,8% sampai 96%). Gugus apel tunggal mencakup 75,31% data, dengan presisi 96% dan recall 99%. Akurasi keseluruhan 94,4%; menurut kondisi cahaya akurasi 94,01% sampai 95,38%, kurang hitung 3,62% sampai 5,67%, dan lebih hitung 0,74% sampai 1,1%. Pada studi terdahulu penulis, metode GMM dibandingkan baseline mirip CHT dengan akurasi 91% terhadap 69%.

Untuk penggabungan antarbingkai, pendekatan homografi menyebabkan lebih hitung hingga 8% dibandingkan pelacakan dengan pose kamera 3D penuh. Akurasi terhadap hitungan manusia (apel yang terlihat dari satu sisi) 89% sampai 98% untuk model terawasi pengguna dan 48% sampai 98% untuk model semi-terawasi.

Terhadap hitungan panen, apel yang terlihat dari satu sisi bervariasi 40,85% sampai 79,83% antardataset. Penjumlahan hitungan satu sisi menghasilkan 101,93% sampai 150%. Hasil penggabungan kedua sisi (Tabel 2):

| Dataset | Hitungan panen | Gabungan dua sisi | Jumlah hitungan satu sisi |
|---|---|---|---|
| Dataset1 | 270 | 256 (94,81%) | 348 (128,89%) |
| Dataset3 | 274 | 252 (91,98%) | 411 (150%) |
| Dataset4 | 414 | 392 (94,68%) | 422 (101,93%) |

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: sistem tidak bergantung pada platform dan pencahayaan khusus; segmentasi dan penghitungan tidak memerlukan penyetelan parameter per dataset (berbeda dengan CHT) dan tidak memerlukan pelatihan jaringan dalam; kebutuhan masukan pengguna kecil; model terlatih dapat disimpan untuk varietas dan cahaya serupa. Penulis juga menyatakan bahwa penggabungan kedua sisi baris perlu agar hasil mendekati hasil panen sebenarnya.

Keterbatasan yang dinyatakan penulis: kasus ekstrem pada Gambar 1 (citra paling kanan) memerlukan supervisi pengguna yang banyak; metode diharapkan bekerja bila apel dapat dibedakan dari vegetasi berdasarkan warna; model semi-terawasi gagal pada varietas campuran merah dan hijau (Dataset2); homografi menyebabkan lebih hitung hingga 8%; dataset berasal dari kebun penelitian yang bukan kebun komersial dan bentuk pohon sangat bervariasi; evaluasi dilakukan pada beberapa dataset kecil.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Penggabungan kedua sisi bergantung pada rekonstruksi 3D dan registrasi yang dirinci hanya di laporan teknis lain, sehingga tahap yang menentukan akurasi akhir tidak dapat dinilai dari makalah ini. Hasil kedua sisi hanya tersedia untuk tiga dataset dengan total 22 pohon (6, 10, dan 6 pohon) dan tidak ada ulangan atau selang kepercayaan. Hitungan acuan (270, 274, 414 apel) tidak disertai pemisahan apel yang memang tidak terlihat dari kedua sisi. Hasil hitungan gabungan selalu di bawah hitungan panen (91,98% sampai 94,81%), sehingga ada kurang hitung sistematis.

## Kaitan dengan Tinjauan main6
Makalah ini secara eksplisit menangani buah yang terlihat lebih dari sekali, pada dua tingkat. Pertama, antarbingkai dalam satu sisi baris: kotak gugus apel dipropagasi dengan homografi dan hitungan per gugus direkam sebagai daftar, lalu diambil median. Kedua, antarsisi baris: rekonstruksi 3D kedua sisi digabung dan hitungan gugus yang beririsan digabung dengan prinsip inklusi-eksklusi. Makalah menunjukkan bahwa penjumlahan hitungan dua sisi tanpa penggabungan menghasilkan lebih hitung 101,93% sampai 150% dari hitungan panen, sedangkan hitungan satu sisi hanya mencakup 40,85% sampai 79,83% apel.

Hitungan tidak dilaporkan per kelas (apel dihitung sebagai satu kelas; warna merah dan hijau hanya dipakai sebagai kondisi dataset). Acuan hitung adalah hitungan fisik setelah panen dengan stiker (untuk hasil dua sisi) dan anotasi citra serta hitungan persepsi manusia (untuk segmentasi dan penghitungan per bingkai). Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan penggabungan hitungan sisi-sisi pohon pada ruang 3D bersama dengan koreksi irisan (inklusi-eksklusi), serta pelaporan terpisah antara cakupan satu sisi dan hasil gabungan. Pendekatan berbasis warna, gerakan kamera mendekati planar, dan baris pohon lurus tidak otomatis berlaku bagi pohon sawit yang dipotret dari 4 sampai 8 sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `roy2019vision`.

Roy dkk. menyajikan sistem pemetaan hasil apel dari video kamera monokular yang menggabungkan segmentasi warna semi-terawasi, penghitungan gugus apel dengan GMM yang dipilih memakai kriteria MDL modifikasi, pelacakan antarbingkai dengan homografi, dan penggabungan hitungan kedua sisi baris pohon melalui rekonstruksi 3D dan prinsip inklusi-eksklusi. Pada tiga dataset, hitungan gabungan dua sisi mencapai akurasi 91,98% sampai 94,81% terhadap hitungan panen, sedangkan penjumlahan hitungan satu sisi menghasilkan lebih hitung 101,93% sampai 150%; apel yang terlihat dari satu sisi bervariasi 40,85% sampai 79,83% antardataset.

Catatan verifikasi data: F1-measure diambil dari Tabel 1, hasil hasil panen dari Tabel 2 dan seksi 5.5, akurasi per bingkai 94,4% dan statistik gugus dari seksi 5.4.1 (Gambar 21), rentang 89% sampai 98% dan 48% sampai 98% serta 8% lebih hitung dari seksi 5.4.2. Jumlah apel dan pohon tiap dataset dari seksi 5.1. Teks abstrak menyebut "tiga baris pohon yang terdiri atas 252 pohon", sedangkan seksi 5.1 menyebut 26 pohon pada empat dataset validasi dan 76 pohon pada dataset pelatihan; ketidaksesuaian ini tidak dapat diselesaikan dari teks. Data pada Gambar 16 sampai 22 dan 24 tidak dapat dibaca dari teks ekstraksi; angka dari gambar hanya diambil yang diulang dalam teks narasi. Perincian rekonstruksi 3D dan registrasi kedua sisi dirujuk ke laporan teknis lain dan tidak tersedia dalam teks ini.
