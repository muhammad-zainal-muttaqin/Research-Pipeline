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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract

RGB-D salient object detection (SOD) is usually formulated as a problem of classification or regression over two modalities, i.e., RGB and depth. Hence, effective RGBD feature modeling and multi-modal feature fusion both play a vital role in RGB-D SOD. In this paper, we propose a depth-sensitive RGB feature modeling scheme using the depth-wise geometric prior of salient objects. In principle, the feature modeling scheme is carried out in a depth-sensitive attention module, which leads to the RGB feature enhancement as well as the background distraction reduction by capturing the depth geometry prior. Moreover, to perform effective multi-modal feature fusion, we further present an automatic architecture search approach for RGB-D SOD, which does well in finding out a feasible architecture from our specially designed multi-modal multi-scale search space. Extensive experiments on seven standard benchmarks demonstrate the effectiveness of the proposed approach against the state-of-the-art.

Figure 1. Left: Salient objects are often distributed within different depth intervals. Right: We decompose the raw depth map into multiple regions and extract the depth-sensitive RGB features.

and 2) how to carry out the multi-modal feature fusion effectively between RGB and depth features. In this paper, we focus on building a depth-sensitive SOD model that is capable of learning the RGB-D feature interaction architecture automatically. In the recent literature, RGB-D SOD methods usually treat the depth channel as an auxiliary input channel, which is directly fed into a convolutional neural network (CNN) for feature extraction [7, 21, 31, 43, 59]. As a result, they are incapable of well utilizing the depth prior knowledge to capture the corresponding geometric layouts of salient objects. As shown in Fig. 1, salient objects are often distributed within several particular depth intervals, and thus can be roughly detected by regularly sliding the depth interval window. Inspired by this observation, we have an intuitive idea that we can extract RGB features w.r.t. depth for effectively capturing the depth-wise geometric prior on salient objects while reducing the background distraction (e.g. cluttered objects or similar texture). With this motivation, we propose to decompose the raw depth map into multiple regions, and each region contains a set of pixels from the same depth interval. Then, we propose a depth-sensitive attention module (DSAM) to perform RGB feature extraction in different regions, thereby leading to the RGB feature enhancement with depth-wise geometric prior. Furthermore, designing an effective feature interaction architecture between RGB and depth branches is crucial

1. Introduction Recent years have witnessed a great development of RGB-D salient object detection (SOD) due to its diverse applications, e.g., image retrieval [25, 36], video segmentation [20, 55], person re-identification [62], visual tracking [27, 41]. With the multi-modal input (i.e., RGB and depth channels), RGB-D SOD aims to localize and segment the visually salient regions in a scene, and is typically cast as an image-to-mask mapping problem within an end-toend deep learning pipeline [22, 23, 45, 49]. In RGB-D SOD, depth maps, which provide useful cues such as spatial structure, 3D layout, and object boundary, are important complementary information to RGB channels. For the sake of effective learning, there are usually two key issues to solve for RGB-D SOD: 1) how to fully exploit the rich depth geometry information for saliency analysis, * Corresponding Author

for multi-modal feature fusion in RGB-D SOD. In general, the existing literature relies heavily on human expertise knowledge through enormous trial and error, e.g., flow ladder module [59] and fluid pyramid integration module [61]. Moreover, the multi-source information on RGB and depth channels is extremely heterogeneous, making the feature fusion design rather difficult and heuristic. Based on this observation, we leverage neural architecture search (NAS) [3, 13, 37] to automatically explore an effective feature fusion module. However, simply porting existing NAS ideas from image classification/segmentation to RGB-D SOD would not suffice, as the task requires nested combinations of multi-modal multi-scale features. To this end, we construct a new search space tailored for the multi-modal feature fusion across multiple scales for RGB-D SOD. As a result, the automatically-found feature fusion architecture equipped with the commonly used backbone VGG-19 [53] achieves the state-of-the-art performance. Our contributions can be summarized as follows:

complements in separate paths, and then propose to use residual connections and complementarity-aware supervisions to explicitly expose cross-modal complements in [7]. Lately, Zhang [59] proposes an asymmetric two-stream architecture, and designs a flow ladder module for the RGB stream and a depth attention module for the depth stream. Although these methods have achieved huge success, depth cues are only direct as the input of the feature extractor. In this paper, motivated by our observation, we further exploit the depth information, which contains abundant geometric prior knowledge. Then, we utilize the depth cues to explicitly eliminate the background distraction and propose an effective depth-sensitive attention module for RGBD salient object detection.

2.2. Neural Architecture Search Neural architecture search (NAS) aims at automating the network architecture design process. Early NAS works are based on either reinforcement learning [3, 66] or evolutionary algorithms [13, 50]. Despite achieving satisfactory performance, they have consumed hundreds of GPU days. Recently, one-shot methods [4, 6] have greatly solved the time-consuming problem by training a parent network from which each sub-network can inherit the weights. DARTs [37] is the pioneering work for gradient-based NAS, which uses gradients to efficiently optimize the search space. After that, NAS has been widely applied to many computer vision tasks, such as object detection [26,56], semantic segmentation [34, 35], and so on. However, in RGB-D salient object detection, the multimodal feature fusion architectures are still designed by hand. Although there are several NAS works [46, 57] for multi-modal fusion, their design purpose is especially for the visual question answering task [57] or image-audio fusion task [46]. As far as we know, our work is the first attempt to utilize the NAS algorithms to tackle the multimodal multi-scale feature fusion problem for RGB-D SOD.

• We propose a depth-sensitive attention module to explicitly eliminate the background distraction and enhance the RGB features by depth prior knowledge. • We design a new search space tailored for the heterogeneous feature fusion in RGB-D SOD and present the first attempt to introduce NAS for RGB-D SOD. • Finally, we conduct extensive experiments on seven benchmarks, which demonstrates that our method outperforms other state-of-the-art approaches.

2. Related Work 2.1. RGB-D Salient Object Detection Early RGB-D saliency detection methods [23, 30, 45, 51] design handcrafted features, such as contrast [45], shape [15], local background enclosure [23] and so on. Recently, CNN-based RGB-D approaches have achieved a qualitative leap in performance due to the powerful ability of CNNs in discriminative feature representation. The existing RGB-D approaches can be roughly divided into singlestream models [39, 45, 52, 54, 63, 64] and multi-stream models [7–11, 21, 43, 59]. The single-stream architecture adopts a straightforward way to fuse RGB images and depth cues. For example, Peng et al. [45] directly concatenate RGB-D pairs as 4-channel inputs to predict saliency maps. DANet [63] uses a single-stream network with the depthenhanced dual attention for salient object detection. For the multi-stream models, the frameworks employ two parallel networks to extract RGB and depth features respectively, and then fuse the multi-modal features with various dazzling strategies. For example, Chen et al. [9] design a multibranch network to fuse the deep and shallow cross-modal

3. Method In this section, we illustrate the proposed depth-sensitive attention and automatic multi-modal fusion (DSA2 F) framework in detail. First, we briefly introduce an overview of the proposed framework. Then, we describe the proposed depth-sensitive attention. Next, we elaborate on the taskspecific module for the automatic multi-modal multi-scale feature fusion. Finally, we illustrate the whole optimization strategy.

Figure 2. Illustration of our proposed framework. The whole network consists of an RGB branch, a depth branch, and a specially-designed module. The RGB branch is equipped with the proposed depth-sensitive attention modules (DSAMs). ri , di , Ci , Di , G, and Li represent the output features, and thin arrows represent the feature flows. Best viewed in color.

3.2. Depth-Sensitive Attention

VGG-19 [53], and the depth branch is a lightweight depth network to obtain the depth features of different scales.

We propose a depth-sensitive RGB feature modeling scheme, including the depth decomposition and the depthsensitive attention module. The raw depth map is decomposed into T + 1 regions with the following steps. First, we quantize the raw depth map into the depth histogram, and choose the T largest depth distribution modes (corresponding to the T depth interval windows) of the depth histogram. Then, using these depth interval windows, the raw depth map can be decomposed into T regions, and the remaining part of the histogram naturally forms the last region, as shown in Fig. 3(a). Finally, each region is normalized into [0,1] as a spatial attention mask for the subsequent process. After obtaining these attention masks, we describe the depth-sensitive attention module in detail. In DSAM, the obtained attention masks give rise to T + 1 sub-branches in the RGB branch, as shown in Fig. 3(b). Formally, let Frgb ∈ RCk ×Hk ×Wk be the RGB feature maps in the k-th k stage of the RGB branch, where Ck , Hk , and Wk represent the number of channels, the height, and width, respectively. Denote bt as the t-th attention mask obtained in the above depth decomposition process. We utilize the max-pooling operation to align the masks to the size of Frgb k as

We plug in a depth-sensitive attention module (DSAM) following each down-sampling layer in the RGB branch. Each DSAM utilizes a raw depth map to enhance the RGB features. Specifically, we decompose the raw depth map into multiple regions. Each region, which contains the pixel values from the same depth distribution mode, is considered as a spatial attention map to extract the corresponding RGB features. To fuse the enhanced RGB features and the depth features automatically, we propose a multi-modal multi-scale feature fusion module. In the RGB-D SOD literature [21, 31, 32, 47, 59, 60, 63], three consistent principles are noticeable: 1) The features from different modalities of the same scale are always fused, while features in different scales are selectively fused. 2) Low-level features are always combined with high-level features before the final prediction, as low-level features are rich in spatial details but lack semantic information and vice versa. 3) Attention mechanism is necessary when performing the feature fusion of different modalities. With these common practices, we design a new search space adapted to the multi-modal multi-scale fusion, which contains four different architectures i.e., the multimodal fusion (MM), multi-scale fusion (MS), global context aggregation (GA) and spatial information restoration (SR) cells.

Figure 3. (a) The depth decomposition process. ‘IW’ represents the depth interval window here. (b) The detailed depiction of the proposed depth-sensitive attention module. Best viewed in color.

use a 1 × 1 convolution layer in t-th sub-branch as a transition layer, to refine the RGB features from various depth intervals. After that, we aggregate all the depth-sensitive features from T + 1 sub-branches by an element-wise summation operation, Fkenh =

where Fkenh is the enhanced RGB features and ⊗ indicates the element-wise multiplication. Finally, we introduce a residual connection and get the final output features, rk = Fkenh + Fkrgb .

In this way, DSAM not only provides depth-wise geometric prior knowledge for RGB features, but also eliminates the intractable background distraction (e.g. cluttered objects or similar texture). Furthermore, the ablation experiments in Section 4.4 also verify the effectiveness of our DSAM.

3.3. Auto Multi-Modal Multi-Scale Feature Fusion

where m is the index of the MS cells. After that, a GA cell is introduced to seamlessly integrate the outputs of the above four MS cells for global context aggregation, which is calculated by:

We propose an automatic multi-modal multi-scale fusion module for RGB-D SOD. First, we describe the designed four types of cells, i.e., MM, MS, GA, SR cells, and they build up the entire task-specific search space. Then, we elaborate on the search space of the fusion module, in which the cells of four types cooperate in a sequential pipeline. Finally, we describe the internal structure of each cell.

Cell types. For RGB-D SOD, we design four types of cells and each cell is a searchable unit in NAS. First, we use MM cells to directly perform multi-modal feature fusion between RGB and depth branches. Second, we use MS cells for the dense multi-scale feature fusion. Third, we utilize GA cell to aggregate seamlessly the outputs of the MS cells for capturing the global context. Finally, we introduce SR cells to combine the low-level and high-level features

where σ indicates the upsampling function. In the end, a simple decoder is adopted for supervision. The decoder 4

contains two bilinear upsampling functions, each of which is followed by three convolutional layers.

where Lval and Ltrain denote validation loss and training loss (both are the cross-entropy loss), respectively. Then the fusion module is obtained by the discrete α by Eq. (10). The whole network optimization. With the obtained fusion module, the whole network is optimized on the whole training data by the standard cross-entropy loss for the saliency detection.

Cell structure. Each aforementioned cell can be formulated by a unified structure, which is a directed acyclic graph (DAG) consisting of an ordered sequence of N nodes, denoted by N = {x(1) , ..., x(N ) }. Each node x(i) is a latent representation (i.e. feature map), and each directed edge (i, j) is associated with some candidate operations o(i,j) ∈ O (e.g. conv, pooling), representing all possible transformations from x(i) to x(j) . Each intermediate node x(j) is computed based on all of its predecessors:

4. Experiments In this section, we conduct extensive experiments to verify the effectiveness of our method. Firstly, we compare our DSA2 F with other state-of-the-art methods on seven standard benchmarks. Secondly, we perform a series of ablation studies to evaluate each component of our framework.

where o(·) is an operation in the operation set O, and (i,j) is the learnable architecture parameter of the operαo ation selection for edge (i, j). Thus, each cell architecture is denoted by {α(i,j) }. The whole searchable fusion module can be represented as α = {αmm , αms , αga , αsr }. Cells of the same type share the same architecture parameters, but with different weights. After the searching phase, an optimal operation can be determined by replacing each mixed operation oe(i,j) with the most likely operation (i.e. (i,j) argmaxo∈O αo ).

Discussion. Let us retrospect the three consistent principles in the RGB-D literature, as discussed in Section 3.1. Our task-specific search space is general enough to cover the above mentioned common practices. To be specific, the design philosophy for MM and MS cells meets the requirement of multi-modal feature fusion in not only the same scale but also different scales. Then, the GA cell introduces the low-level spatial information to the high-level features. Moreover, we add the spatial and channel attention operations into the candidate operation set O to explore the collocation of attentions, and detailed analysis can be found in Section 4.4.

Evaluation metrics. To comprehensively and fairly evaluate various methods, we employ four widely used metrics, including mean F-measure (Fβ ) [1], mean absolute error (M) [5], S-measure (Sλ ) [17], E-measure (Eξ ) [18]. Specifically, the F-measure can evaluate the overall performance based on the region similarity. The M measures the average of the per-pixel absolute difference between the saliency maps and the ground truth. The S-measure that is recently proposed can evaluate the structural similarities. The Emeasure can jointly utilize image-level statistics and local pixel-level statistics for evaluating the binary saliency map.

3.4. Optimization

4.2. Implementation Details

The optimization of our framework consists of two stages. First, we search the multi-modal fusion module. Then, we optimize the whole network.

Our method is implemented with PyTorch toolbox [44]. For the depth branch, we use the DepthNet [59] which is a lightweight network compared with VGG-19. For the depth-sensitive attention module, the number of depth decomposition regions is 3. In the search process, the node numbers of the MM, MS, GA, SR cells are 8, 8, 8, 4, respectively. For the candidate operation set O, we collect the

Multi-modal fusion module search. During the search progress, we hold out half of the original training data as the validation set. We use the bi-level optimization [2, 16] to jointly optimize architecture parameter α and network weights w: 5

Quantitative comparison. Table 1 shows the quantitative comparison in terms of four evaluation metrics on seven datasets. All results in the table are quoted or tested by VGG-19 [53] backbone for a fair comparison. It can be seen that DSA2 F significantly outperforms the competing methods across all the datasets in most metrics. Especially, DSA2 F outperforms all other methods by a dramatic margin on the LFSD and DUT-RGBD dataset, which are considered as more challenging datasets due to the large number of complex scenes like similar foreground and background, low-contrast and transparent object. Moreover, DSA2 F consistently surpasses all other state-of-the-art methods in seven datasets in terms of the overall performance metric (i.e. Fβ ).

After searching, the network is trained on a GTX 1080Ti GPU, and the input images are uniformly resized to 256 × 256. The momentum, weight decay and learning rate of our network are set as 0.9, 5e-4 and 1e-10, respectively. The network converges after 60 epochs with mini-batch size 2. To reduce overfitting, we augment the training set by randomly flipping, cropping and rotating the training images.

Qualitative comparisons. To further illustrate the superior performance of our method, Fig 4 shows some visual results of the proposed method and other state-of-theart methods. From those results, we can observe that our method is able to accurately segment salient objects under various challenging scenarios, including images with low contrast foreground and background (1st and 2nd rows), cluttered distraction objects (3rd , 4th and 5th rows), blurry depth (8th and 9th rows), and fine structures (10th and 11th rows). These results further demonstrate our approach could eliminate the background distraction obviously in utilizing the depth prior knowledge. Moreover, the object

4.3. Comparison with State-of-the-art We compare our DSA2 F with 18 other state-of-the-art methods on seven widely-used benchmarks, and for a fair comparison, we recalculate the mean F-measure of other methods according to their provided saliency maps if they report the max F-measure in the paper. 6

Figure 4. Qualitative comparison of the state-of-the-art RGB-D SOD methods and our approach. Obviously, saliency maps produced by our model are clearer and more accurate than others in various challenging scenarios.

Table 2. Ablation study for DSAM on three widely-used datasets.

boundaries (6 and 7 rows) of our results are more clear and sharper than others, which preserves more details.

ments with different strategies: 1) Baseline. The network contains a VGG-19 backbone for the RGB branch and a DepthNet for the depth branch, as shown in Fig. 5 (a). 24) The network consists of the VGG-19 backbone equipped with different DSAMs and the DepthNet. As for the strategies 2-4, as shown in Fig. 5 (b), we try different fusion operations of the depth masks and the RGB features for DSAM. The strategies 2,3,4 represent ‘element-wise sum-

4.4. Ablation Analysis In this section, we perform a series of ablation studies to further investigate the relative importance and specific contribution of each component in the proposed framework. Effectiveness of depth-sensitive attention module. In order to verify the effectiveness of the proposed depthsensitive attention module, we conduct a series of experi7

Table 5. Ablation study for the designed search space. MM, MS, GA, SR are four types of cells mentioned above. AT represents the attention operations in the search space.

improvement, which demonstrates that the attention mechanism plays an important role in RGB-D SOD. Searched architecture visualization. Due to the limited space, we illustrate the searched fusion module in the supplementary material. An interesting observation is that in the MM cell, the numbers of operations connected to RGB features are more than those connected to depth features. The phenomenon demonstrates that considering the differences between RGB and depth data, numerous redundant operations or channels of depth features are unnecessary, which also verifies the asymmetric two-stream architecture for RGB and depth branches in ATSA [59] is reasonable. Effectiveness of each component in DSAF Table 3 summarizes how performance gets improved by adding each component step by step into our DSA2 F on seven standard benchmarks. The table shows that each component of our DSA2 F provides a significant performance gain.

Figure 6. Visualization results of depth decomposition. Row (a), (b), (c) represent the RGB image, ground truth, depth map. Row (d), (e), (f) show the three regions of the depth decomposition.

mation’ (+), ‘concatenation’ (c), ‘element-wise multiplication’ (*) operation, respectively. The results are shown in Table 2, and our DSAM can improve the baseline by a large margin, which demonstrates the effectiveness of DSAM. From Table 2, we observe that the ‘element-wise multiplication’ operation obtains the best overall performance as it directly serves as the spatial attention mechanism. Moreover, the ‘concatenation’ operation achieves the suboptimal accuracy, and we suspect that the depth cues play a role of ‘position encoding’ here.

5. Conclusion In this paper, we have proposed a two-stream framework named DSA2 F for RGB-D saliency detection. In the framework, we have introduced a depth-sensitive attention module (DSAM) to effectively enhance the RGB features and reduce the background distraction by utilizing the depth geometry information. Furthermore, we have designed a taskspecific search space tailored for the multi-modal multiscale feature fusion and obtained a powerful fusion architecture automatically. Extensive experiments have demonstrated the effectiveness of our framework against previous state-of-the-art methods, and the visualization results have proved that our network is capable of precisely capturing salient regions in challenging scenes. Acknowledgements This work is supported in part by Na-

Effect of the number of depth regions. The region number of depth decomposition is an important hyper-parameter in our method, thus we perform the experiments with different T + 1 values. Table 4 lists the performance as T varies, and DSAM achieves the best accuracy when T + 1 is 3. Effectiveness of the task-specific search space. In this part, we conduct the corresponding ablation studies to evaluate the effectiveness of each type of cell in our multi-modal search space. We perform the architecture search process and retrain the whole network under different search spaces. The corresponding results are shown in Table 5. Effectiveness of the attentions in our search space. To demonstrate the effectiveness of the attention operations, we perform the searching process with or without the spatial and channel attention operations. The corresponding results are shown in Table 5. With the injection of the attention operations, the performance of the model has a large

tional Key Research and Development Program of China under Grant 2020AAA0107400, National Natural Science Foundation of China under Grant U20A20222, Zhejiang Provincial Natural Science Foundation of China under Grant LR19F020004, and key scientific technological innovation research project by Ministry of Education.
