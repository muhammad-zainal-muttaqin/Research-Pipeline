# 181 - ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `su2022zebrapose` |
| Judul asli | ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation |
| Penulis | Yongzhi Su, Mahdi Saleh, Torben Fetzer, Jason Rambach, Nassir Navab, Benjamin Busam, Didier Stricker, Federico Tombari |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2203.09418
- **Google Scholar:** https://scholar.google.com/scholar?q=ZebraPose%3A%20Coarse%20to%20Fine%20Surface%20Encoding%20for%206DoF%20Object%20Pose%20Estimation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ZebraPose%3A%20Coarse%20to%20Fine%20Surface%20Encoding%20for%206DoF%20Object%20Pose%20Estimation&sort=relevance

## Gambaran Umum

ZebraPose memecahkan estimasi pose 6D (posisi tiga sumbu translasi dan tiga sumbu rotasi objek relatif terhadap kamera) dari citra RGB tunggal dengan cara membangun korespondensi 2D-3D yang jauh lebih padat dan lebih teliti daripada metode sebelumnya. Gagasan utamanya adalah memberi setiap titik pada permukaan model CAD (*computer-aided design*, model 3D objek) sebuah kode biner bertingkat yang dihasilkan dengan membagi permukaan secara hierarkis, bukan dengan meregresi koordinat 3D secara langsung atau memilih dari sejumlah kecil titik kunci (*keypoint*) tetap. Jaringan konvolusi memprediksi kode ini piksel demi piksel pada citra, kode tersebut dicocokkan dengan tabel pemetaan permukaan yang dibangun sebelumnya (*offline*), dan himpunan korespondensi 2D-3D yang terbentuk diselesaikan menjadi pose lewat solver PnP (*Perspective-n-Point*, algoritme yang menghitung pose kamera/objek dari pasangan titik 2D-3D) berbasis RANSAC.

Pendekatan ini diuji pada dua tolok ukur standar, LM-O (*Linemod-Occlusion*) dan YCB-V (*YCB-Video*), dengan metrik ADD(-S) (rata-rata jarak titik model di bawah ambang tertentu) dan AUC (*area under curve*, luas di bawah kurva akurasi-ambang). ZebraPose mencapai rata-rata perolehan (*recall*) ADD(-S) 76,9% pada LM-O dan 80,5% pada YCB-V, melampaui metode berbasis RGB sezamannya dan, pada LM-O, bahkan melampaui sejumlah metode yang memakai data kedalaman (RGB-D) tambahan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode estimasi pose 6D berbasis korespondensi bekerja dengan dua tahap konseptual: pertama, mencari padanan antara titik pada citra 2D dan titik pada model 3D objek; kedua, menghitung pose yang paling konsisten dengan padanan tersebut lewat PnP. Kualitas tahap pertama menentukan akurasi tahap kedua secara langsung, sehingga desain skema korespondensi menjadi pusat perhatian riset di bidang ini.

Metode berbasis titik kunci, seperti PVNet, membatasi korespondensi pada beberapa belas titik kunci tetap yang dipilih di muka pada model 3D; jaringan memprediksi arah vektor dari tiap piksel objek menuju titik-titik itu, lalu voting menentukan lokasinya. Skema ini murah secara komputasi, tetapi jumlah titik yang sedikit membatasi ketelitian geometris pose akhir, terutama saat sebagian objek terhalang (oklusi) sehingga voting kehilangan sebagian besar piksel pendukung. Metode lain, seperti DPOD dan GDR-Net (dibahas pada bab 180), memprediksi koordinat 3D secara padat untuk setiap piksel objek — satu nilai kontinu per piksel per sumbu koordinat. Pendekatan ini memberi korespondensi lebih padat daripada titik kunci, tetapi meregresi koordinat kontinu secara langsung merupakan tugas yang secara numerik sulit dipelajari jaringan secara stabil, dan galat regresi kecil pada permukaan yang hampir simetris dapat menghasilkan korespondensi yang salah kelompok sama sekali.

Masalah yang belum terselesaikan dengan baik adalah bagaimana merepresentasikan seluruh permukaan objek secara padat sekaligus dapat diprediksi jaringan dengan stabil, termasuk pada kondisi oklusi parsial yang umum terjadi pada tolok ukur seperti LM-O.

## Ide Utama

ZebraPose mengganti regresi koordinat 3D kontinu dengan klasifikasi kode biner diskret. Setiap titik pada permukaan model 3D diberi kode biner unik yang dihasilkan lewat pembagian hierarkis: pada iterasi pertama seluruh permukaan dibagi dua kelompok sama besar (bit pertama, 0 atau 1); pada iterasi kedua, masing-masing dari dua kelompok itu dibagi dua lagi (bit kedua); proses ini berulang hingga jumlah bit yang ditentukan, sehingga tiap titik memperoleh rangkaian bit yang menyatakan lintasan pembagian yang dilaluinya. Bit awal (kedudukan rendah) menandai pembagian kasar permukaan menjadi dua belahan besar, sedangkan bit akhir (kedudukan tinggi) menandai pembagian halus di dalam wilayah kecil. Pembagian biner berulang pada permukaan tertutup menghasilkan pola wilayah hitam-putih berselang-seling yang menjadi asal nama metode ini. Seluruh pemetaan kode-ke-titik dihitung sekali di muka dan disimpan sebagai tabel pencarian (*lookup table*).

Jaringan kemudian dilatih memprediksi rangkaian bit ini untuk setiap piksel objek pada citra, bukan koordinat kontinu. Karena kode berjenjang, jaringan dapat mempelajari bit-bit kasar (mudah, berkaitan dengan wilayah luas) lebih dulu sebelum bit-bit halus (sulit, berkaitan dengan wilayah sempit) — sebuah strategi pelatihan bertahap dari kasar ke halus (*coarse-to-fine*) yang menjadi nama bagian kedua judul makalah.

## Cara Kerja Langkah demi Langkah

### Pengodean Permukaan Secara Hierarkis

Diagram berikut menggambarkan tiga iterasi pertama pembagian biner pada satu permukaan objek yang disederhanakan menjadi satu garis:

```
iterasi 1 (bit-0):  [0000000000000000|1111111111111111]
iterasi 2 (bit-1):  [00000000|1111111|00000000|1111111]
iterasi 3 (bit-2):  [0000|1111|0000|1111|0000|1111|0000|1111]

kode 3-bit tiap wilayah, urut kiri ke kanan:
000  001  010  011  100  101  110  111
```

Setiap wilayah pada iterasi terakhir memiliki kode unik yang menjadi identitas diskret kelompok titik permukaan di dalamnya. Pada makalah ini, skema biner (basis dua) dipilih sebagai basis pengodean optimal dibandingkan basis lain yang diuji dalam ablasi, dengan panjang kode 16 bit — cukup untuk membagi permukaan objek menjadi 2^16 wilayah berbeda, jauh melampaui kepadatan titik kunci pada metode voting.

### Arsitektur Jaringan

Jaringan memakai varian DeepLabv3 (arsitektur segmentasi semantik berbasis konvolusi berlubang/*dilated convolution*) dengan *backbone* (tulang punggung ekstraksi fitur) ResNet34 dan sambungan pintas (*skip connection*) antar lapis. Sebuah pendeteksi objek (FCOS) terlebih dahulu memotong wilayah objek dari citra menjadi masukan berukuran 256×256×3 piksel. Jaringan menghasilkan peta keluaran berresolusi 128×128, terdiri atas 16 peta biner untuk 16 bit kode permukaan ditambah satu peta masker objek — sehingga tiap piksel objek memperoleh prediksi rangkaian 16 bit yang menyatakan wilayah permukaan mana yang tampak di piksel itu.

### Pelatihan Kasar-ke-Halus

Fungsi *loss* berupa *binary cross-entropy* (galat klasifikasi biner) untuk tiap bit, dijumlahkan dengan pembobotan yang berbeda antar-bit. Bobot ini bersifat adaptif: pada awal pelatihan, histogram galat tiap bit menunjukkan bit kasar lebih mudah dipelajari, sehingga bit tersebut diberi bobot lebih besar; seiring pelatihan berlanjut dan prediksi bit kasar mengonvergen, bobot bergeser ke bit yang lebih halus. Skema ini mencegah gradien pelatihan didominasi oleh bit halus yang pada awalnya masih sangat acak nilainya, sekaligus tetap mendorong jaringan mempelajari detail permukaan pada tahap lanjut pelatihan.

### Pemadanan Korespondensi dan Penyelesaian Pose

Saat inferensi, kode biner yang diprediksi tiap piksel dicocokkan dengan tabel pencarian permukaan untuk memperoleh titik 3D yang berkorespondensi. Karena prediksi dilakukan padat pada seluruh piksel objek, satu citra dapat menghasilkan ribuan pasangan korespondensi 2D-3D, jauh melampaui jumlah titik kunci pada metode voting. Himpunan korespondensi ini diselesaikan menjadi pose 6D memakai solver Progressive-X, varian PnP-RANSAC yang menyaring korespondensi keliru (*outlier*) sekaligus memanfaatkan koherensi spasial antar-korespondensi yang berdekatan pada citra.

## Eksperimen dan Hasil

Evaluasi dilakukan pada LM-O, subset dari LineMOD yang berisi delapan objek dengan oklusi berat antar-objek dalam satu adegan, dan YCB-V, tolok ukur beranggota 21 objek pada adegan meja berantakan. Model dilatih per-objek, memakai kombinasi citra sintetis hasil physically-based rendering (PBR, rendering yang mensimulasikan interaksi cahaya-material secara fisis) dan citra nyata terbatas dari data pelatihan resmi kedua tolok ukur. Metrik utama adalah ADD(-S): jarak rata-rata antara titik model yang ditransformasi memakai pose prediksi terhadap pose kebenaran (*ground truth*); untuk objek simetris dipakai varian ADD-S yang mengukur jarak ke titik terdekat, bukan titik berpasangan tetap. Sebuah prediksi dianggap benar bila ADD(-S) berada di bawah 10% diameter objek. AUC ADD(-S) mengintegralkan proporsi prediksi benar pada rentang ambang jarak, sehingga tidak bergantung pada satu ambang tunggal.

Pada LM-O, ZebraPose mencapai rata-rata perolehan ADD(-S) 76,9%, mengungguli metode berbasis RGB pembanding pada masanya seperti GDR-Net (62,2%) dan SO-Pose (62,3%) dengan selisih lebih dari 14 poin. Angka ini juga melampaui sejumlah metode berbasis RGB-D seperti FFB6D (66,2%) dan PR-GCN (65%) — pencapaian yang relevan karena metode RGB-D umumnya diuntungkan oleh informasi kedalaman langsung, sedangkan ZebraPose hanya memakai RGB. Selisih besar terhadap GDR-Net dan SO-Pose pada LM-O, dataset dengan oklusi berat, konsisten dengan klaim makalah bahwa korespondensi padat lebih tahan terhadap hilangnya sebagian permukaan objek dibanding korespondensi jarang atau regresi koordinat langsung.

Pada YCB-V, ZebraPose mencapai rata-rata perolehan ADD(-S) 80,5% dan AUC ADD(-S) 85,3%, keduanya di atas GDR-Net (60,1% dan 84,4%) dan SO-Pose (56,8% dan 83,9%). Namun pada metrik AUC ADD-S saja (tanpa penanganan khusus objek simetris), ZebraPose mencatat 90,1%, sedikit di bawah GDR-Net (91,6%). Perbedaan arah pada dua varian metrik AUC ini menunjukkan keunggulan ZebraPose lebih menonjol pada objek asimetris dan pada rata-rata perolehan berambang tetap, dibandingkan pada metrik AUC ADD-S murni yang lebih dipengaruhi objek simetris bernilai tinggi.

## Kelebihan dan Keterbatasan

Kelebihan utama ZebraPose adalah kepadatan dan ketelitian korespondensi: setiap piksel objek menyumbang satu pasangan korespondensi 2D-3D, jauh melampaui jumlah titik kunci pada metode voting, tanpa harus meregresi koordinat kontinu yang secara numerik lebih sulit dipelajari stabil. Strategi pelatihan kasar-ke-halus membuat jaringan tidak perlu langsung mempelajari detail permukaan paling halus di awal pelatihan, yang secara empiris terbukti meningkatkan akurasi dibanding pelatihan tanpa pembobotan bertingkat. Ketahanan terhadap oklusi pada LM-O menunjukkan representasi kode biner tetap berguna sekalipun sebagian permukaan objek tidak tampak, karena piksel yang tersisa tetap menyumbang korespondensi valid.

Dari sisi rekayasa, metode ini tetap memerlukan model CAD tekstur objek untuk membangun tabel pencarian kode, sehingga tidak langsung berlaku pada objek baru tanpa model 3D siap pakai. Pelatihan dan tabel kode dibuat per-objek, berbeda dengan pendekatan yang berupaya menggeneralisasi lintas objek tanpa pelatihan ulang. Secara konseptual, akurasi metode ini juga bergantung pada kualitas pendeteksi objek awal (FCOS) untuk memotong wilayah objek sebelum prediksi kode dilakukan; kegagalan deteksi akan menggagalkan seluruh proses korespondensi berikutnya.

## Kaitan dengan Bab Lain

ZebraPose berada pada garis riset korespondensi padat berbasis RGB yang sama dengan GDR-Net (bab 180): keduanya menghitung pose lewat korespondensi 2D-3D piksel-demi-piksel yang diselesaikan dengan PnP, tetapi GDR-Net meregresi koordinat 3D kontinu secara langsung sedangkan ZebraPose mengubahnya menjadi klasifikasi kode biner bertingkat, sebuah perbedaan representasi yang terbukti memberi selisih akurasi signifikan pada LM-O. Perbandingan hasil ADD(-S) antara kedua metode pada bagian Eksperimen di atas dapat dibaca berdampingan dengan bab 180 untuk melihat dampak langsung pilihan representasi korespondensi terhadap akurasi pose. Berbeda dengan OnePose (bab 182), yang menargetkan estimasi pose tanpa memerlukan model CAD objek di muka, ZebraPose tetap berada pada rezim klasik yang mengasumsikan model 3D objek tersedia sebelum pelatihan — perbandingan ini relevan untuk menilai trade-off antara akurasi (ZebraPose unggul saat model CAD tersedia) dan fleksibilitas terhadap objek baru (keunggulan OnePose).

## Poin untuk Sitasi

Kutip dengan kunci `su2022zebrapose`. Ringkasan yang aman dikutip: "ZebraPose mengodekan permukaan model 3D objek secara hierarkis menjadi kode biner bertingkat, memprediksinya padat per-piksel dengan strategi pelatihan kasar-ke-halus, lalu menyelesaikan pose 6D lewat PnP-RANSAC atas korespondensi 2D-3D yang terbentuk, mencapai rata-rata perolehan ADD(-S) 76,9% pada LM-O dan 80,5% pada YCB-V." Angka-angka berikut diperoleh dari ekstraksi otomatis terhadap naskah dan versi HTML-nya, bukan pembacaan langsung tabel PDF asli, sehingga perlu diverifikasi ulang sebelum dikutip dalam karya formal: rincian pembanding GDR-Net dan SO-Pose pada LM-O dan YCB-V, angka FFB6D (66,2%) dan PR-GCN (65%), AUC ADD-S 90,1% dan AUC ADD(-S) 85,3% pada YCB-V, panjang kode 16 bit, hasil ablasi hierarki (75,23% tanpa pelatihan bertingkat versus 76,91% dengan pelatihan bertingkat), serta rincian arsitektur (ResNet34, resolusi masukan/keluaran, pendeteksi FCOS) dan solver Progressive-X.
