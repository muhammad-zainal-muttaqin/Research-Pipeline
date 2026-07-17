# 062 - Depth Map Prediction from a Single Image Using a Multi-Scale Deep Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `eigen2014depth` |
| Judul asli | Depth Map Prediction from a Single Image Using a Multi-Scale Deep Network |
| Penulis | David Eigen, Christian Puhrsch, Rob Fergus |
| Tahun | 2014 |
| Venue | Advances in Neural Information Processing Systems (NIPS 2014), hal. 2366–2374 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1406.2283
- **Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Map%20Prediction%20from%20a%20Single%20Image%20Using%20a%20Multi-Scale%20Deep%20Network
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Depth%20Map%20Prediction%20from%20a%20Single%20Image%20Using%20a%20Multi-Scale%20Deep%20Network&sort=relevance

## Gambaran Umum

Makalah ini adalah karya pertama yang memprediksi peta kedalaman (*depth map* — citra yang setiap pikselnya berisi jarak permukaan ke kamera) secara padat dari satu citra RGB tunggal menggunakan jaringan saraf konvolusi (CNN). Regresi dari piksel ke kedalaman dilakukan dua tumpukan jaringan: jaringan skala kasar membaca seluruh citra untuk menaksir struktur kedalaman global, lalu jaringan skala halus memperbaikinya pada detail lokal seperti tepi objek. Pelatihan memakai galat invarian-skala (*scale-invariant error*), fungsi galat yang menilai relasi kedalaman antarpiksel tanpa menghukum kesalahan skala global pemandangan.

Model ini menjadi yang terbaik pada masanya di dua tolok ukur, NYU Depth v2 (ruang dalam) dan KITTI (jalan raya), dengan perbaikan relatif rata-rata 35% dan 31% terhadap pesaing terdekat.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Kedalaman dapat diperoleh secara deterministik dari citra stereo: korespondensi piksel antar dua citra dicari, lalu kedalaman dihitung dari disparitas (pergeseran posisi piksel) melalui triangulasi. Kasus monokular (satu citra) tidak menawarkan jalan itu, karena satu citra 2D dapat dihasilkan oleh tak terhingga banyak susunan pemandangan 3D; masalahnya bersifat *ill-posed*. Sistem harus memakai isyarat monokular seperti perspektif garis, titik hilir, dan ukuran objek, yang sebagian hanya bermakna bila seluruh pemandangan diamati sekaligus.

Sebelum 2014, pendekatan yang ada bergantung pada fitur manual dan asumsi kuat. Make3D memprediksi kedalaman dengan regresi linier dan MRF (*Markov Random Field*, model yang memaksa prediksi piksel bertetangga saling konsisten), tetapi mengasumsikan perataan horizontal citra. Ladický dkk. menggabungkan label semantik dengan fitur kedalaman, tetapi tetap memakai fitur manual dan *superpixel* (kelompok piksel yang diperlakukan sebagai satu permukaan). Karsch dkk. mentransfer kedalaman dari dataset dengan pencocokan SIFT Flow, yang mengharuskan seluruh dataset ada saat inferensi. Sementara itu, CNN yang baru unggul pada klasifikasi citra (AlexNet, 2012) belum dipakai untuk regresi peta kedalaman padat.

Ada pula ambiguitas yang tersisa bagi model yang baik sekalipun: skala global — ruangan normal dan miniatur rumah boneka dapat menghasilkan citra hampir sama. Eksperimen *oracle* makalah ini membuktikan pengaruhnya: mengganti rata-rata log-kedalaman prediksi Make3D dengan rata-rata kebenaran menurunkan RMSE log dari 0,41 ke 0,33 (perbaikan relatif sekitar 20%). Seperlima galat metode saat itu ternyata hanya kesalahan menaksir kedalaman rata-rata pemandangan; temuan ini memotivasi fungsi galat yang tidak sensitif terhadap skala.

## Ide Utama

Gagasan intinya: pecah prediksi kedalaman menjadi dua tahap oleh dua jaringan, dan latih keduanya dengan galat yang mengukur relasi kedalaman, bukan nilai absolutnya. Jaringan skala kasar melihat seluruh citra dan mengeluarkan peta beresolusi rendah yang menangkap tata letak pemandangan. Jaringan skala halus menerima peta kasar itu dan menyuntingnya dengan detail lokal dari citra asli agar batas objek menjadi tajam. Karena skala global pemandangan memang ambigu, kualitas prediksi dinilai dan dilatih dengan galat invarian-skala: dua peta kedalaman yang hanya berbeda faktor pengali konstan dianggap sama baiknya.

## Cara Kerja Langkah demi Langkah

### Jaringan Skala Kasar

Jaringan ini terdiri atas lima lapis konvolusi yang diselingi *max-pooling* (operasi yang mengambil nilai maksimum dalam jendela kecil sehingga peta fitur menyusut), diikuti dua lapis *fully connected* (terhubung penuh, setiap unit terhubung ke semua unit lapis sebelumnya). Kelima lapis konvolusi diinisialisasi dari bobot yang telah dilatih untuk klasifikasi ImageNet. Semua lapis tersembunyi memakai aktivasi ReLU (*rectified linear unit*, f(x) = maks(0, x)), kecuali lapis keluaran yang linier karena menargetkan nilai kedalaman; *dropout* (pemadaman acak sebagian unit saat pelatihan) diterapkan pada lapis *fully connected* pertama. Lapis terhubung penuh ini membuat setiap unit keluaran melihat seluruh citra, sehingga isyarat global seperti titik hilir dapat dipakai.

Masukan untuk NYU Depth adalah potongan tengah 304×228 piksel dari citra 320×240 (citra asli 640×480 diperkecil separuh); keluarannya peta 74×55, sekitar seperempat resolusi masukan. Lapis konvolusi teratas hanya menghasilkan peta fitur 8×6. Alih-alih memperbesarnya dengan *upsampling* tetap, lapis *fully connected* terakhir mempelajari sendiri templat keluaran pada ukuran 74×55 — jaringan belajar melakukan *upsampling* berdasarkan fitur.

### Jaringan Skala Halus

Jaringan kedua hanya berisi lapis konvolusi, dengan satu tahap *pooling* pada lapis pertama. Masukannya dua: citra asli dan peta keluaran jaringan kasar. Ukuran peta kasar dirancang sama dengan keluaran lapis pertama jaringan halus setelah *pooling*, sehingga keduanya digabung melalui konkatenasi kanal. Lapis berikutnya memakai konvolusi *zero-padded* (pinggir peta diisi nol) sehingga ukuran spasial tetap 74×55. Bidang pandang (*receptive field*, wilayah citra masukan yang memengaruhi satu unit keluaran) setiap unit jaringan halus hanya 45×45 piksel: cukup untuk meluruskan tepi tanpa mengganggu struktur global.

Pelatihan dilakukan berurutan: jaringan kasar dilatih dahulu terhadap peta kebenaran, bobotnya dibekukan, lalu jaringan halus dilatih dengan peta kasar yang tetap. Pembagian kerja keduanya terlihat pada diagram berikut.

```
citra RGB (304x228 piksel)
   |
   v
+---------------------------+
| JARINGAN SKALA KASAR      |   masukan: citra penuh
| 5 konvolusi + max-pooling |   bidang pandang: seluruh citra
| 2 fully connected         |
+---------------------------+
   |  peta kedalaman kasar 74x55
   v
+---------------------------+
| JARINGAN SKALA HALUS      |   masukan: citra penuh + peta kasar
| konvolusi + 1 pooling,    |   (peta kasar dikonkatenasi ke
| lalu konvolusi zero-padded|    fitur lapis pertama)
+---------------------------+   bidang pandang: 45x45 piksel
   |  peta kedalaman halus 74x55
   v
upsampling ke resolusi citra penuh -> peta kedalaman akhir
```

Jaringan kasar membaca seluruh citra dan menghasilkan peta 74×55; jaringan halus menerima peta itu beserta fitur lokal citra asli dan menghasilkan peta berukuran sama dengan tepi lebih tajam. Keluaran akhir di-*upsampling* ke resolusi penuh untuk evaluasi.

### Galat Invarian-Skala dan Fungsi Loss

Misalkan y peta kedalaman prediksi, y* kebenarannya (*ground truth*), dan d_i = log y_i − log y*_i selisih keduanya per piksel dalam ruang logaritmik. Ruang log dipakai karena kesalahan kedalaman bersifat relatif: selisih 1 meter pada objek berjarak 2 meter lebih besar artinya daripada selisih 1 meter pada objek berjarak 20 meter. Galat invarian-skala didefinisikan D(y,y*) = (1/n) Σ (d_i + α)², dengan α = (1/n) Σ (−d_i) dipilih untuk meminimalkan galat; e pangkat α adalah faktor skala terbaik yang menyelaraskan prediksi ke kebenaran, sehingga semua kelipatan skalar dari y bergalat sama. Contoh numerik: bila prediksi tepat setengah dari kedalaman benar di semua piksel (d_i = −log 2 konstan), α = log 2 menyerap seluruh selisih dan galatnya nol; galat l2 biasa tetap menghukumnya.

Fungsi loss pelatihannya L = (1/n) Σ d_i² − (λ/n²) (Σ d_i)²: galat kuadrat biasa dikurangi suku yang memberi penghargaan bila kesalahan konsisten searah, atau secara setara membandingkan relasi kedalaman setiap pasangan piksel. Nilai λ = 0 menghasilkan l2 murni dan λ = 1 invarian-skala penuh; makalah memakai λ = 0,5, yang menjaga ketepatan skala absolut sekaligus sedikit memperbaiki kualitas visual. Lapis terakhir jaringan memprediksi log-kedalaman, dan piksel tanpa nilai kebenaran (jendela, permukaan reflektif, batas objek) dikeluarkan dari perhitungan loss dengan *masking*.

### Data dan Pelatihan

NYU Depth v2 berisi 464 rekaman ruang dalam dari kamera Microsoft Kinect dengan pembagian resmi 249 pemandangan latih dan 215 uji. Citra kedalaman dipasangkan dengan citra RGB terdekat waktunya. Data mentahnya menyediakan 120 ribu citra unik, diseimbangkan menjadi 220 ribu contoh latih; sebagai pembanding, Make3D hanya mampu dilatih pada 795 citra. Pengujian memakai 694 citra uji.

KITTI menyumbang 56 pemandangan kota, permukiman, dan jalan raya (28 latih, 28 uji); citra RGB 1224×368 diperkecil separuh. Kedalaman berasal dari pemindai LIDAR berputar yang bertitik jarang dan hanya menutupi bagian bawah citra; seluruh citra tetap dimasukkan ke jaringan kasar sebagai konteks, sedangkan jaringan halus hanya melihat potongan bawah. Setiap pemandangan menyumbang 800 citra, total 20 ribu citra unik yang digandakan menjadi 40 ribu contoh.

Augmentasi daring meliputi penskalaan s ∈ [1; 1,5] dengan kedalaman dibagi s (memperbesar citra s kali setara mendekatkan kamera s kali), rotasi ±5 derajat, pemotongan acak, pengali warna per kanal [0,8; 1,2], dan pembalikan horizontal berpeluang 0,5. Pelatihan memakai SGD (*stochastic gradient descent*) momentum 0,9, kelompok 32 citra: 2 juta contoh untuk jaringan kasar lalu 1,5 juta untuk jaringan halus pada NYU, serta 1,5 juta dan 1 juta pada KITTI.

## Eksperimen dan Hasil

Evaluasi memakai metrik baku: *rel* (rata-rata |y − y*| / y* per piksel; makin kecil makin baik), RMSE (*root mean square error*), dan akurasi ambang δ < 1,25 pangkat i (persentase piksel dengan maks(y/y*, y*/y) di bawah 1,25 pangkat i; makin besar makin baik). Pembandingnya adalah rata-rata data, Make3D yang dilatih ulang pada dataset yang sama, serta angka terbit Karsch dkk. dan Ladický dkk.

Pada NYU Depth v2, model penuh mencapai rel 0,215 dan RMSE 0,871 meter dengan δ<1,25 sebesar 61,1%, δ<1,25² 88,7%, dan δ<1,25³ 97,1%; Make3D memperoleh rel 0,349. Artinya, rata-rata piksel menyimpang 21,5% dari kedalaman benar, enam dari sepuluh piksel berada dalam faktor 1,25 dari kebenaran, dan galat relatif turun hampir 40% terhadap Make3D. Perbaikan relatif rata-rata 35% itu berlaku di semua metrik, baik yang bergantung skala maupun invarian-skala — struktur relasi kedalaman ikut membaik, bukan sekadar rata-ratanya. Pada KITTI, model mencapai rel 0,190, RMSE 7,156 meter, dan δ<1,25 sebesar 69,2%, atau perbaikan rata-rata 31% terhadap Make3D; RMSE besar karena jarak luar ruang mencapai puluhan meter, dan Make3D lebih kompetitif di sini karena asumsi perataan horizontalnya cocok dengan data berkendara.

Temuan tambahan: jaringan halus hampir tidak menaikkan skor metrik, tetapi mempertajam batas objek secara visual — pada KITTI perbaikannya lebih terbatas karena ketidakrataan pasangan kedalaman–RGB dari LIDAR berputar — dengan efek samping tepi tekstur kadang ikut masuk ke peta kedalaman. Nilai λ = 0,5 tidak menambah skor numerik dibanding λ = 0, hanya memperbaiki tampilan. Eksperimen *oracle* pada sistem sendiri menyisakan ruang perbaikan: RMSE log 0,28 turun ke 0,22, dan RMSE log terukur 0,285 menjadi 0,219 bila dinilai invarian-skala — sebagian galat tersisa masih berupa kesalahan skala global.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini: (1) mempelopori regresi kedalaman padat *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah) dengan CNN, tanpa fitur manual, *superpixel*, maupun pasca-pemrosesan; (2) pembagian global–lokal menangkap isyarat seluruh citra dan tepi tajam bersama; (3) galat invarian-skala menilai dan melatih relasi kedalaman tanpa terjebak ambiguitas skala; (4) model hanya menyimpan parameter jaringan dan dapat berjalan *real-time*; (5) mampu memanfaatkan data mentah berskala besar berkat *masking* pada loss.

Keterbatasannya: (1) supervised penuh — memerlukan peta kedalaman kebenaran dari sensor dalam jumlah besar, yang sulit dikumpulkan pada lingkungan beragam; (2) resolusi keluaran hanya seperempat masukan, dan kontribusi jaringan halus terutama bersifat visual, bukan metrik; (3) dari sisi rekayasa, lapis *fully connected* pada jaringan kasar mahal parameter dan mengikat arsitektur pada satu ukuran masukan; (4) secara konseptual, galat absolutnya masih besar dibanding generasi berikutnya pada klaster ini (bab 065–068), sehingga posisinya lebih tepat sebagai pembuka bidang dan *baseline*; (5) perbaikan halus pada KITTI dibatasi kualitas pasangan data latihnya, sebagaimana diakui penulis.

## Kaitan dengan Bab Lain

Bab ini adalah akar klaster Estimasi Kedalaman; warisannya berlanjut ke dua arah. Pertama, kebutuhan akan kedalaman kebenaran diserang oleh bab 063 ([Monodepth](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)), yang mengganti label sensor dengan konsistensi stereo kiri–kanan, dan bab 064 ([Monodepth2](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)), yang menyempurnakan pendekatan *self-supervised* (pelatihan tanpa label kedalaman) tersebut. Kedua, gagasan galat invarian-skala dilanjutkan bab 067 ([DPT](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)) dan bab 068 ([MiDaS](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)), yang melatih model pada banyak dataset dengan galat invarian skala dan pergeseran. Bagi tinjauan YOLO/RGB-D, makalah ini menyediakan konsep *pseudo-depth* — kedalaman hasil prediksi model sebagai pengganti sensor — yang relevan bagi klaster Segmentasi RGB-D seperti bab 055 ([SA-Gate](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)) yang mengasumsikan kanal kedalaman dari sensor.

## Poin untuk Sitasi

Kutip dengan kunci `eigen2014depth`. Ringkasan yang aman dikutip: "Eigen, Puhrsch, dan Fergus (NIPS 2014) adalah yang pertama memprediksi peta kedalaman padat dari satu citra RGB dengan CNN, melalui dua jaringan berskala global-kasar dan lokal-halus serta galat invarian-skala; metode ini menjadi yang terbaik pada NYU Depth v2 dan KITTI dengan perbaikan relatif rata-rata 35% dan 31% terhadap pesaing terdekat." Catatan verifikasi: angka tabel spesifik (NYU: rel 0,215; RMSE 0,871; δ<1,25 = 61,1% / 88,7% / 97,1%. KITTI: rel 0,190; RMSE 7,156; δ<1,25 = 69,2%. Make3D: rel 0,349) lazim dikutip literatur, tetapi tabel naskah tidak ikut ter-*render* pada versi HTML yang diakses — cocokkan ke PDF sebelum sitasi formal. Klaim 35%/31%, angka *oracle* (0,41 → 0,33; 0,28 → 0,22), RMSE log 0,285 dan 0,219 invarian-skala, serta seluruh detail arsitektur dan pelatihan terverifikasi dari teks arXiv:1406.2283v1.
