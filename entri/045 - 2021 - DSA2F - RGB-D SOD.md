# 045 - Deep RGB-D Saliency Detection with Depth-Sensitive Attention and Automatic Multi-Modal Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2021dsa2f` |
| Judul asli | Deep RGB-D Saliency Detection with Depth-Sensitive Attention and Automatic Multi-Modal Fusion |
| Penulis | Peng Sun, Wenhu Zhang, Huanyu Wang, Songyuan Li, Xi Li |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021), oral |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2103.11832
- **Google Scholar:** https://scholar.google.com/scholar?q=Deep%20RGB-D%20Saliency%20Detection%20with%20Depth-Sensitive%20Attention%20and%20Automatic%20Multi-Modal%20Fusion
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Deep%20RGB-D%20Saliency%20Detection%20with%20Depth-Sensitive%20Attention%20and%20Automatic%20Multi-Modal%20Fusion&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DSA2F, sebuah model untuk deteksi objek salien berbasis RGB-D. Deteksi objek salien (*salient object detection*, SOD) adalah tugas melokalisasi dan mensegmentasi objek yang paling menonjol dalam sebuah adegan, dan varian RGB-D-nya memakai dua masukan sekaligus: citra RGB biasa dan peta kedalaman, yaitu citra yang setiap pikselnya menyatakan jarak permukaan ke kamera. Model ini menyerang dua masalah yang selama ini dihadapi bidang tersebut: bagaimana memanfaatkan informasi geometri kedalaman secara eksplisit, dan bagaimana merancang arsitektur fusi antara fitur RGB dan fitur kedalaman.

Jawabannya terdiri atas dua komponen. Komponen pertama adalah *depth-sensitive attention module* (DSAM), yang memecah peta kedalaman menjadi beberapa wilayah menurut mode distribusi kedalaman, lalu memakai setiap wilayah sebagai masker atensi untuk mengekstrak fitur RGB per interval kedalaman. Komponen kedua adalah modul fusi multi-modal multi-skala yang arsitekturnya tidak dirancang oleh manusia, melainkan ditemukan secara otomatis oleh *neural architecture search* (NAS) di dalam ruang pencarian yang dirancang khusus untuk tugas ini. Pada tujuh tolok ukur standar RGB-D SOD, DSA2F mengungguli 18 metode pembanding dalam metrik F-measure pada seluruh dataset.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, metode RGB-D SOD berbasis CNN terbagi dalam dua garis besar. Garis pertama adalah model satu arus (*single-stream*): citra RGB dan peta kedalaman digabung menjadi masukan empat kanal yang langsung diolah satu jaringan. Garis kedua adalah model dua arus (*multi-stream*): dua jaringan paralel mengekstrak fitur RGB dan fitur kedalaman secara terpisah, kemudian kedua arus fitur itu digabung oleh modul fusi rancangan manual. Bab-bab sebelumnya dalam klaster ini membahas contoh garis kedua, antara lain DMRA pada bab 035, BBS-Net pada bab 036, S2MA pada bab 039, dan HDFNet pada bab 040.

Penulis DSA2F mengidentifikasi dua kelemahan spesifik dari kondisi tersebut. Pertama, pada hampir semua metode, peta kedalaman hanya diperlakukan sebagai kanal masukan biasa bagi CNN. Padahal terdapat pengetahuan prior yang belum dimanfaatkan: objek salien umumnya terdistribusi pada beberapa interval kedalaman tertentu, sehingga menggeser jendela interval kedalaman secara teratur sudah dapat melokalisasi objek secara kasar. Tanpa mekanisme eksplisit untuk itu, prior geometri kedalaman tidak dipakai secara langsung, dan latar belakang yang bertekstur mirip objek tetap sulit disingkirkan.

Kedua, arsitektur fusi multi-modal dirancang lewat coba-coba manual yang memakan banyak tenaga ahli. Fitur RGB bersifat penampilan (warna, tekstur), sedangkan fitur kedalaman bersifat geometris (jarak, bentuk); heterogenitas ini membuat kombinasi operasi fusi yang tepat sukar ditebak. Modul-modul rancangan manual pada generasi sebelumnya memang berhasil, tetapi tidak ada jaminan bahwa struktur yang dipilih manusia adalah yang optimal. Ruang kemungkinan desain fusi — operasi apa, pada skala mana, dari modalitas mana — terlalu luas untuk dijelajahi dengan coba-coba.

## Ide Utama

Gagasan pertama: pecah peta kedalaman mentah menjadi T+1 wilayah berdasarkan mode-modenya pada histogram kedalaman. Setiap wilayah berisi piksel-piksel yang jaraknya ke kamera sejenis, dan wilayah itu dinormalisasi menjadi masker atensi spasial. Dengan mengalikan masker ke fitur RGB, jaringan mengekstrak fitur per lapisan kedalaman: wilayah pada interval kedalaman objek diperkuat, wilayah lain ditekan. Dengan cara ini, informasi kedalaman tidak hanya menjadi masukan, tetapi menjadi pengendali perhatian atas fitur RGB.

Gagasan kedua: berhenti merancang modul fusi secara manual. Sediakan ruang pencarian yang berisi empat jenis sel — unit komputasi kecil yang strukturnya dapat dicari — lalu biarkan algoritme pencarian arsitektur memilih operasi pada setiap sisi grafik komputasi di dalam sel. Yang dicari bukan seluruh jaringan dari nol, melainkan hanya modul fusi, sehingga biaya pencarian tetap terkendali.

## Cara Kerja Langkah demi Langkah

### Kerangka Keseluruhan

Jaringan terdiri atas tiga bagian: cabang RGB, cabang kedalaman, dan modul fusi. Cabang RGB memakai *backbone* VGG-19 — *backbone* adalah jaringan ekstraksi fitur utama, dan VGG-19 adalah CNN 19 lapis dari Visual Geometry Group yang menjadi standar pembanding pada bidang ini. Cabang kedalaman memakai DepthNet, jaringan ringan yang dipinjam dari metode ATSA, dan menghasilkan fitur kedalaman lima skala. Pada cabang RGB, satu DSAM disisipkan setelah setiap lapis *down-sampling* (penurunan resolusi spasial), sehingga diperoleh lima tingkat fitur RGB yang telah diperkuat kedalaman, dinotasikan r1 sampai r5, berdampingan dengan fitur kedalaman d1 sampai d5.

Alur data lengkap kerangka ini:

```
citra RGB --> VGG-19 --> r1..r5 ──┐
 (DSAM pada tiap tahap; DSAM       ├─> MMx3 -> C1..C3 -> MSx4 -> D1..D4
  membaca peta depth mentah)       │       MM dan MS memadukan fitur r dan d
peta depth --> DepthNet -> d1..d5 ─┘       dari berbagai skala

D1..D4 -> GA -> G -> upsampling -> SR1 -> L1 -> upsampling -> SR2 -> L2
                         (SR1 memakai d2,r2; SR2 memakai d1,r1)
L2 -> dekoder (2x upsampling + 3 konvolusi per tahap) -> peta saliensi
```

Diagram di atas menunjukkan dua arus ekstraksi fitur yang bertemu pada modul fusi hasil pencarian (sel MM, MS, GA, SR; dijelaskan pada subbagian berikut), diakhiri dekoder sederhana yang menghasilkan peta saliensi — citra keluaran yang tiap pikselnya bernilai peluang termasuk objek salien.

### Dekomposisi Kedalaman

Peta kedalaman mentah dipecah menjadi T+1 wilayah melalui tiga langkah. Pertama, nilai kedalaman dikuantisasi menjadi histogram kedalaman: sebaran frekuensi nilai jarak pada seluruh piksel. Kedua, T mode (puncak distribusi) terbesar pada histogram dipilih; setiap mode menentukan satu jendela interval kedalaman. Piksel yang nilainya jatuh pada jendela yang sama membentuk satu wilayah, sehingga diperoleh T wilayah, dan sisa histogram membentuk wilayah ke-(T+1). Ketiga, setiap wilayah dinormalisasi ke rentang [0,1] sehingga berfungsi sebagai masker atensi spasial. Pada implementasi dipakai T+1 = 3: peta kedalaman dipecah menjadi tiga wilayah, misalnya latar jauh, objek pada jarak menengah, dan latar dekat.

### Modul Depth-Sensitive Attention (DSAM)

DSAM bekerja dalam lima langkah pada setiap tahap ekstraksi fitur RGB. Pertama, setiap masker wilayah b_t disesuaikan ukurannya dengan peta fitur RGB pada tahap itu melalui *max-pooling* — operasi yang mengecilkan peta dengan mengambil nilai maksimum tiap jendela — menghasilkan masker p_t. Kedua, p_t dikalikan elemen-demi-elemen ke setiap kanal peta fitur RGB, sehingga fitur pada posisi piksel di luar wilayah kedalaman itu tertekan mendekati nol. Ketiga, hasilnya dirapikan oleh konvolusi 1×1, yaitu konvolusi berukuran satu piksel yang mengombinasikan antar-kanal tanpa mengubah resolusi spasial. Keempat, keluaran seluruh T+1 sub-cabang dijumlahkan elemen-demi-elemen menjadi fitur yang diperkuat. Kelima, koneksi residual — jalan pintas yang menjumlahkan keluaran suatu blok dengan masukannya — menambahkan fitur RGB semula kembali: r_k = F_enh_k + F_rgb_k.

Sebagai contoh numerik: pada citra masukan 256×256, tahap ketiga cabang RGB menghasilkan peta fitur 32×32. Masker wilayah 256×256 di-*max-pool* menjadi 32×32, lalu dipakai menimbang kanal-kanal fitur pada resolusi itu; dengan T+1 = 3 terdapat tiga sub-cabang yang keluarannya dijumlahkan. Hasil akhirnya adalah fitur RGB yang dikuatkan pada interval kedalaman yang berpotensi memuat objek, dengan gangguan latar berkurang.

### Ruang Pencarian Fusi Multi-Modal Multi-Skala

Penulis merangkum tiga prinsip yang konsisten muncul pada literatur RGB-D SOD: fitur berbeda modalitas pada skala yang sama selalu difusi, fitur berbeda skala difusi secara selektif, fitur tingkat rendah selalu dipadukan dengan fitur tingkat tinggi sebelum prediksi akhir, dan mekanisme atensi diperlukan saat fusi. Dari prinsip itu dirancang empat jenis sel. Sel MM (*multi-modal*) memadukan fitur RGB dan kedalaman. Sel MS (*multi-scale*) memadukan fitur lintas skala. Sel GA (*global aggregation*) mengagregasi konteks global. Sel SR (*spatial restoration*) mengembalikan detail spasial yang hilang akibat *down-sampling*.

Rangkaiannya berurutan. Tiga sel MM memadukan fitur bersebelahan dari kedua cabang: C_n = MM_n(r_{n+1}, r_{n+2}, d_{n+1}, d_{n+2}) untuk n = 1, 2, 3. Empat sel MS kemudian memadukan lintas skala: MS1(r4, C1, d4), MS2(r5, C2, d5), MS3(r3, C3, d3), dan MS4(C1, C2, C3), menghasilkan D1 sampai D4. Satu sel GA mengagregasi keempatnya menjadi G. Dua sel SR berturut-turut memadukan G yang telah di-*upsampling* (dinaikkan resolusinya) dengan fitur tingkat rendah: L1 = SR1(G, d2, r2), lalu L2 = SR2(L1, d1, r1). Dekoder akhir berisi dua *upsampling* bilinear yang masing-masing diikuti tiga lapis konvolusi.

### Struktur Sel dan Pencarian Arsitektur

Setiap sel berbentuk *directed acyclic graph* (DAG): grafik berarah tanpa siklus yang setiap simpulnya adalah peta fitur dan setiap sisinya adalah operasi. Pada tiap sisi disediakan delapan operasi kandidat: *max pooling*, *skip connection* (identitas), konvolusi 3×3, konvolusi 1×1, konvolusi terpisah (*separable*) 3×3, konvolusi terdilasi 3×3 (dilasi 2), atensi spasial 3×3, dan atensi kanal 1×1. Pencarian mengikuti DARTS, metode NAS berbasis gradien yang mengubah pilihan diskret atas operasi menjadi kombinasi berbobot *softmax* yang dapat diturunkan; setelah pencarian selesai, pada tiap sisi diambil operasi berbobot terbesar (*argmax*) sebagai operasi definitif. Sel-sel sejenis berbagi parameter arsitektur yang sama tetapi memiliki bobot jaringan berbeda. Jumlah simpul dalam sel MM, MS, GA, dan SR masing-masing adalah 8, 8, 8, dan 4.

Pelatihan berlangsung dua tahap. Tahap pencarian memakai optimasi dua tingkat (*bi-level*): bobot jaringan dioptimalkan pada setengah data latih, parameter arsitektur pada setengah sisanya sebagai data validasi; tahap ini berjalan 50 epoch selama kurang lebih 20 jam pada 4 GPU GTX 1080Ti. Tahap kedua melatih jaringan utuh dengan arsitektur fusi yang sudah tetap, selama 60 epoch pada citra 256×256 dengan *batch* 2, augmentasi pembalikan, pemotongan, dan rotasi acak, serta fungsi *loss cross-entropy* — ukuran selisih antara distribusi prediksi dan label piksel benar.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tujuh dataset standar RGB-D SOD: DUT-RGBD, NJUD, NLPR, SSD, STEREO, LFSD, dan RGBD135. Data latih mengikuti protokol ATSA: 800 sampel DUT-RGBD, 700 NLPR, dan 1485 NJUD; sisanya dipakai untuk uji generalisasi. Empat metrik dipakai: F-measure (rata-rata harmonik presisi dan *recall* pada peta saliensi), MAE (rerata selisih absolut per piksel terhadap label benar), S-measure (kemiripan struktur peta), dan E-measure (keselarasan statistik tingkat citra dan piksel).

DSA2F mencapai F-measure terbaik pada ketujuh dataset di antara 19 metode yang dibandingkan: 0,926 pada DUT-RGBD, 0,901 pada NJUD, 0,897 pada NLPR, 0,852 pada SSD, 0,898 pada STEREO, 0,882 pada LFSD, dan 0,896 pada RGBD135. Interpretasinya: terhadap ATSA — pembanding paling adil karena protokol data latihnya identik — keunggulannya 2,0 poin pada LFSD (0,882 lawan 0,862) dan 0,6 poin pada DUT-RGBD (0,926 lawan 0,920); kedua dataset itu oleh penulis disebut paling menantang karena memuat banyak adegan kompleks. Terhadap BBS-Net pada NLPR, keunggulannya 1,7 poin (0,897 lawan 0,880). MAE terbaik juga diraih pada semua dataset, misalnya 0,030 pada DUT-RGBD. Pada metrik lain DSA2F tidak selalu nomor satu — misalnya E-measure pada NLPR 0,950, sedikit di bawah PGAR 0,954 — tetapi hanya DSA2F yang konsisten terdepan dalam F-measure di seluruh dataset.

Studi ablasi pada DUT-RGBD mengukur sumbangan tiap komponen. Garis dasar dua arus tanpa DSAM dan tanpa fusi hasil pencarian mencapai F 0,830; menambah DSAM menaikkannya menjadi 0,889 (naik 5,9 poin); menambah modul fusi hasil pencarian menjadi 0,926 (naik lagi 3,7 poin). Untuk operasi penggabungan masker di dalam DSAM, perkalian elemen-demi-elemen (0,889) mengungguli penjumlahan (0,875) dan konkattenasi (0,873), sesuai peran masker sebagai atensi spasial. Jumlah wilayah optimum adalah T+1 = 3: dengan 1, 2, 4, dan 5 wilayah, F berturut-turut 0,854, 0,874, 0,844, dan 0,831. Ablasi ruang pencarian menunjukkan setiap jenis sel menyumbang kenaikan, dan operasi atensi di dalam himpunan kandidat ikut menaikkan F dari 0,919 menjadi 0,926. Satu observasi tambahan: pada sel MM hasil pencarian, jumlah operasi yang terhubung ke fitur RGB lebih banyak daripada ke fitur kedalaman, yang menurut penulis menegaskan bahwa banyak kanal fitur kedalaman memang redundan.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah bahwa fusi multi-modal tidak lagi bergantung pada intuisi perancang: arsitektur yang ditemukan otomatis mengungguli 18 metode rancangan manual pada tolok ukur yang sama, dengan biaya pencarian terkendali (sekitar 20 jam pada 4 GPU, berbanding ratusan hari GPU pada metode NAS generasi awal). DSAM memberi cara eksplisit memanfaatkan prior geometri kedalaman dan terbukti menyumbang kenaikan terbesar pada ablasi. Ruang pencariannya merangkum praktik umum literatur, sehingga tidak membatasi diri pada satu gaya fusi.

Keterbatasannya: pertama, alurnya tetap dua tahap — pencarian lalu pelatihan penuh — sehingga dari sisi rekayasa total biayanya lebih besar daripada sekali melatih model rancangan manual. Kedua, dari sisi rekayasa pula, arsitektur hasil pencarian terikat pada backbone VGG-19 dan himpunan operasi yang disediakan; mengganti backbone berarti mengulang pencarian. Ketiga, dekomposisi histogram kedalaman bergantung pada kualitas peta kedalaman; makalah menunjukkan ketangguhan terhadap kedalaman buram hanya secara kualitatif, tanpa uji kuantitatif pada kedalaman yang rusak berat. Keempat, jumlah wilayah T+1 = 3 dan ukuran sel adalah hiperparameter yang disetel empiris. Kelima, secara konseptual, arsitektur hasil NAS sukar diinterpretasikan, sehingga sulit dijadikan bahan pembelajaran desain manual.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis model dua arus yang dibahas pada bab-bab sebelumnya: [bab 035 (DMRA, 2019)](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) memperkenalkan fusi dua arus dengan perhatian terinduksi kedalaman, sementara [bab 036 (BBS-Net)](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), [bab 039 (S2MA)](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md), dan [bab 040 (HDFNet)](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md) masing-masing merancang modul fusi manualnya sendiri. Keempatnya masuk tabel pembanding makalah ini dan dikalahkan dalam F-measure pada dataset yang sama. Perbedaan mendasar bab ini terletak pada siapa yang merancang fusi: bukan lagi peneliti, melainkan algoritme pencarian. Observasi bahwa fitur kedalaman lebih sedikit dipakai daripada fitur RGB pada arsitektur hasil pencarian sejalan dengan desain dua arus asimetris yang dipakai pembanding ATSA. Sebagai kontras arah lain pada klaster yang sama, [bab 042 (VST)](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md) mengganti backbone CNN dengan transformer, sementara bab ini tetap pada CNN dan mengotomatiskan sisi fusinya.

## Poin untuk Sitasi

Kutip dengan kunci `sun2021dsa2f`. Ringkasan yang aman dikutip: "DSA2F memadukan modul atensi peka kedalaman — yang memecah peta kedalaman menjadi wilayah-wilayah menurut mode histogramnya untuk menimbang fitur RGB — dengan modul fusi multi-modal multi-skala yang arsitekturnya ditemukan otomatis melalui pencarian arsitektur saraf; kombinasi ini mengungguli 18 metode terdahulu dalam F-measure pada tujuh tolok ukur RGB-D SOD." Catatan verifikasi: seluruh angka pada bab ini dikutip dari naskah arXiv v1 (arXiv:2103.11832); klaim "upaya pertama memakai NAS untuk RGB-D SOD" adalah klaim penulis makalah; nomor halaman prosiding (1407–1417) berasal dari catatan bibliografi lokal dan sebaiknya dicocokkan dengan prosiding CVPR 2021 resmi sebelum sitasi formal.
