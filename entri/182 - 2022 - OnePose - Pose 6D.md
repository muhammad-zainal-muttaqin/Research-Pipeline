# 182 - OnePose: One-Shot Object Pose Estimation without CAD Models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2022onepose` |
| Judul asli | OnePose: One-Shot Object Pose Estimation without CAD Models |
| Penulis | Jiaming Sun, Zihao Wang, Siyu Zhang, Xingyi He, Hongcheng Zhao, Guofeng Zhang, Xiaowei Zhou |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2205.12257
- **Repositori kode resmi:** https://github.com/zju3dv/OnePose
- **Google Scholar:** https://scholar.google.com/scholar?q=OnePose%3A%20One-Shot%20Object%20Pose%20Estimation%20without%20CAD%20Models

## Gambaran Umum

OnePose mengestimasi pose 6D (posisi tiga sumbu translasi dan tiga sudut rotasi objek relatif terhadap kamera) dari objek arbitrer tanpa memerlukan model CAD (*computer-aided design*, model geometri 3D presisi buatan manual atau pemindaian khusus) dan tanpa melatih ulang jaringan untuk setiap objek atau kategori baru. Metode ini hanya membutuhkan sebuah video RGB pendek yang merekam objek dari berbagai sudut sebagai referensi. Dari video itu, sebuah model titik 3D jarang (*sparse point cloud*) direkonstruksi memakai teknik *structure-from-motion* (SfM, rekonstruksi struktur 3D dan posisi kamera dari sekumpulan citra bertumpang tindih), lalu sebuah jaringan pencocokan fitur berbasis atensi menghubungkan titik 2D pada citra kueri dengan titik 3D pada model tersebut untuk menghitung pose. Penulis mengumpulkan dan merilis dataset OnePose berisi 450 sekuens video dari 150 objek sehari-hari, serta menunjukkan bahwa metode ini dapat melacak pose objek baru secara langsung (*real-time*) tanpa pelatihan tambahan, dengan kinerja yang dievaluasi juga pada dataset LINEMOD.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode estimasi pose 6D berbasis pembelajaran mendalam yang populer sebelum OnePose, misalnya GDR-Net (bab 180) dan ZebraPose (bab 181), memakai skema *instance-level*: satu jaringan dilatih khusus untuk satu objek tertentu, dan pelatihan itu membutuhkan model CAD objek tersebut sebagai sumber data sintetis serta acuan geometri saat menghitung *loss* (fungsi kerugian yang dioptimalkan selama pelatihan). Skema ini memiliki dua konsekuensi praktis. Pertama, model CAD presisi tidak selalu tersedia untuk objek dunia nyata di luar laboratorium — memindai geometri suatu benda dengan pemindai 3D khusus memakan waktu dan biaya. Kedua, begitu ada objek baru, seluruh jaringan harus dilatih ulang dari awal atau minimal disetel halus (*fine-tuned*) dengan data baru, sehingga metode ini tidak dapat langsung dipakai pada objek yang belum pernah dilihat sistem.

Pendekatan alternatif *category-level* mencoba mengatasi keterbatasan itu dengan melatih satu jaringan untuk seluruh kategori objek (misalnya semua jenis cangkir), sehingga dapat menggeneralisasi ke instansi baru dalam kategori yang sama tanpa CAD per objek. Namun pendekatan ini tetap terbatas pada kategori yang pernah dilihat saat pelatihan dan tidak dapat menangani objek dari kategori sepenuhnya baru. Kedua jalur ini menyisakan celah yang sama: tidak ada cara praktis untuk mengestimasi pose objek arbitrer yang baru pertama kali ditemui sistem, tanpa CAD dan tanpa pelatihan ulang.

## Ide Utama

Gagasan inti OnePose adalah memindahkan masalah estimasi pose 6D dari kerangka "klasifikasi/regresi per objek" ke kerangka *visual localization* (pelokalan visual, teknik menentukan posisi dan orientasi kamera relatif terhadap suatu adegan yang telah direkonstruksi sebelumnya). Dalam pelokalan visual, sebuah adegan direkonstruksi sekali menjadi model titik 3D melalui SfM, kemudian pose kamera baru dihitung dengan mencocokkan fitur citra kueri terhadap titik-titik model itu. OnePose menerapkan logika yang sama pada satu objek, bukan satu adegan luas: video referensi objek direkonstruksi menjadi model titik 3D miliknya sendiri, dan pose objek pada citra kueri dihitung dengan mencocokkan fitur 2D citra kueri terhadap titik 3D model objek tersebut.

Konsekuensi penting dari pergeseran kerangka ini adalah jaringan pencocokan fitur tidak perlu tahu objek spesifik apa yang sedang dilihat. Ia hanya perlu pandai mencocokkan fitur visual secara umum, sebuah kemampuan yang dapat dipelajari sekali dari banyak objek pelatihan dan berlaku digeneralisasi ke objek uji yang sama sekali baru. Karena itu, menambahkan objek baru ke sistem cukup dengan merekam video referensinya dan menjalankan SfM — tanpa menyentuh bobot jaringan sama sekali. Inilah yang penulis sebut sebagai kemampuan *one-shot* (satu kali tayang, tanpa pelatihan ulang untuk kasus baru).

## Cara Kerja Langkah demi Langkah

### Tahap Pemetaan: Rekonstruksi Model Titik Objek

Pengguna merekam video pendek objek dari berbagai sudut pandang, biasanya dengan bantuan penanda visual (*marker*) di sekitar objek agar batas objek dan skala nyatanya dapat ditentukan. Dari bingkai-bingkai video ini, titik-titik minat 2D diekstraksi dengan detektor SuperPoint (jaringan yang mendeteksi dan mendeskripsikan titik sudut/tekstur khas pada citra), lalu dicocokkan antarbingkai dengan SuperGlue (jaringan pencocokan fitur berbasis atensi grafis). Korespondensi antarbingkai ini dimasukkan ke pipeline SfM (memakai perangkat COLMAP) yang menghasilkan posisi 3D setiap titik minat sekaligus posisi kamera setiap bingkai, membentuk model titik jarang objek beserta korespondensi 2D-3D-nya: setiap titik 3D tertaut ke sejumlah deskriptor 2D dari berbagai sudut pandang tempat titik itu teramati.

### Agregasi Deskriptor 2D-3D

Satu titik 3D pada permukaan objek dapat teramati dari puluhan bingkai video dengan sudut pandang berbeda, sehingga memiliki puluhan deskriptor 2D yang berlainan akibat perubahan sudut pandang, pencahayaan, dan oklusi (objek terhalang sebagian). Alih-alih menyimpan seluruh deskriptor itu apa adanya, OnePose melatih sebuah jaringan atensi grafis (*Graph Attention Network*, GAT — jaringan saraf yang memperbarui representasi tiap simpul dalam suatu graf dengan menimbang kontribusi simpul tetangganya) untuk meringkas kumpulan deskriptor 2D milik satu titik 3D menjadi satu deskriptor 3D teragregasi yang stabil terhadap sudut pandang. Komponen ini, bersama jaringan pencocokan tahap berikutnya, disebut penulis sebagai GATs-SPG (*Graph Attention Networks with SuperPoint and SuperGlue*).

### Tahap Kueri: Pencocokan 2D-3D dan Penyelesaian Pose

Saat sistem menerima citra kueri baru berisi objek yang sama, titik minat 2D pada citra itu kembali diekstraksi dengan SuperPoint. Jaringan atensi grafis kedua kemudian mencocokkan setiap titik 2D kueri langsung terhadap deskriptor 3D teragregasi pada model objek — proses ini analog dengan pencocokan fitur pada SuperGlue, tetapi salah satu sisi korespondensinya berupa titik 3D dari model, bukan titik 2D dari bingkai lain. Keluaran tahap ini adalah sekumpulan pasangan korespondensi 2D-3D beserta skor kepercayaannya.

Diagram berikut meringkas alur dari video referensi hingga pose objek pada citra kueri:

```
video referensi objek         citra kueri (objek baru dilihat)
   │ SuperPoint+SuperGlue           │ SuperPoint
   ▼                                ▼
korespondensi antar-bingkai     titik minat 2D
   │ SfM (COLMAP)                   │
   ▼                                │
model titik 3D jarang               │
   │ + deskriptor 2D per titik      │
   ▼                                │
agregasi GAT -> deskriptor 3D       │
   └──────────► pencocokan GAT ◄────┘
                     │  korespondensi 2D-3D
                     ▼
              PnP + RANSAC
                     │
                     ▼
              pose 6D objek
```

Dari korespondensi 2D-3D tersebut, pose 6D dihitung dengan algoritme PnP (*Perspective-n-Point*, metode menghitung posisi dan orientasi kamera dari sekumpulan titik 3D yang diketahui beserta proyeksi 2D-nya) yang dikombinasikan dengan RANSAC (*Random Sample Consensus*, teknik penyaring korespondensi keliru dengan mencoba subset acak berulang kali dan mempertahankan solusi yang didukung mayoritas titik). Kombinasi ini menghasilkan pose yang tahan terhadap sebagian korespondensi yang salah cocok. Untuk penggunaan berkelanjutan pada video, misalnya aplikasi realitas tertambah (*augmented reality*), OnePose menambahkan pelacak pose berbasis fitur yang memanfaatkan pose bingkai sebelumnya sebagai inisialisasi, sehingga deteksi ulang penuh tidak perlu dilakukan pada setiap bingkai dan pose dapat dihitung pada laju yang mendekati waktu nyata.

## Eksperimen dan Hasil

Penulis mengevaluasi OnePose pada dua kelompok data. Pertama, dataset OnePose yang mereka kumpulkan sendiri, terdiri atas 450 sekuens video dari 150 objek sehari-hari; setiap objek direkam dengan video referensi (untuk membangun model titik) dan video pengujian terpisah (untuk mengukur akurasi pose). Kedua, dataset LINEMOD, tolok ukur standar pose 6D objek tunggal yang sebelumnya dipakai metode *instance-level* seperti GDR-Net dan ZebraPose. Pada LINEMOD, OnePose dibandingkan terhadap metode *instance-level* yang dilatih khusus per objek dengan CAD, serta terhadap metode *category-level* yang tidak memakai CAD objek uji tetapi tetap memerlukan pelatihan pada kategori terkait.

Metrik utama yang dipakai adalah ADD(-S) (*Average Distance of model points*, jarak rata-rata titik model objek setelah ditransformasikan dengan pose prediksi dibanding pose sebenarnya; varian -S dipakai untuk objek simetris), dengan ambang batas akurasi umum 10% dari diameter objek (ADD-0,1d). Penulis melaporkan bahwa OnePose mencapai akurasi yang kompetitif dengan metode *instance-level* berbasis CAD pada LINEMOD, sekalipun OnePose sama sekali tidak memakai CAD objek uji dan hanya mengandalkan video referensi singkat. Pada dataset OnePose sendiri, sistem menunjukkan kemampuan mengestimasi pose objek baru secara langsung tanpa pelatihan tambahan apa pun untuk objek tersebut. Angka ADD(-S) persis yang dilaporkan pada tabel utama makalah tidak berhasil dipastikan ulang secara independen dalam penelusuran untuk bab ini dan perlu diverifikasi langsung dari naskah sebelum dikutip formal.

Penulis juga melaporkan bahwa kinerja OnePose menurun pada objek bertekstur rendah (permukaan polos tanpa banyak corak yang membuat SuperPoint sulit menemukan titik minat yang khas), objek dengan pola berulang (yang membuat pencocokan fitur ambigu), dan objek tipis (yang sulit direkonstruksi stabil dengan SfM). Kelemahan pada objek bertekstur rendah inilah yang kemudian menjadi motivasi utama pengembangan penerus metode ini, OnePose++, yang mengganti pencocokan berbasis titik minat dengan pendekatan bebas titik minat (*keypoint-free*).

## Kelebihan dan Keterbatasan

Kelebihan utama OnePose adalah pemisahan total antara kebutuhan data objek (video RGB biasa, tanpa CAD dan tanpa pemindai khusus) dan kemampuan generalisasi ke objek baru tanpa pelatihan ulang. Ini membuat sistem dapat diperluas ke objek yang benar-benar baru hanya dengan menambah data pemetaan, bukan menambah pelatihan jaringan. Kelebihan lain adalah penggunaan kembali komponen pencocokan fitur yang telah terbukti (SuperPoint, SuperGlue) yang diperkuat lapisan atensi grafis khusus, sehingga metode tidak perlu merancang mekanisme pencocokan dari nol.

Dari sisi rekayasa, keterbatasan yang paling signifikan adalah ketergantungan pada kualitas rekonstruksi SfM: bila video referensi kurang bervariasi sudut pandangnya, pencahayaan tidak konsisten, atau objek memiliki permukaan reflektif, model titik yang dihasilkan bisa jarang atau bergeser, yang langsung menurunkan akurasi pose pada tahap kueri. Secara konseptual, seluruh pipeline bergantung pada keberadaan titik minat yang khas dan dapat diulang pengamatannya; objek bertekstur rendah — kasus yang menurut penulis sendiri menjadi kelemahan metode ini — melemahkan asumsi dasar tersebut. Proses pemetaan juga membutuhkan langkah persiapan tambahan (perekaman video, kalibrasi skala dengan penanda) yang tidak dibutuhkan metode *instance-level* begitu jaringannya sudah dilatih untuk objek yang bersangkutan.

## Kaitan dengan Bab Lain

OnePose berada pada klaster Pose 6D bersama GDR-Net (bab 180) dan ZebraPose (bab 181), tetapi menempuh jalur berbeda dari keduanya. GDR-Net dan ZebraPose adalah metode *instance-level* klasik: keduanya membutuhkan model CAD objek dan melatih jaringan khusus untuk tiap objek, dengan ZebraPose menambah skema pengodean korespondensi hierarkis di atas kerangka dasar GDR-Net. OnePose menghilangkan kedua kebutuhan itu sekaligus dengan memindahkan masalah ke kerangka pelokalan visual berbasis SfM. Ketiga bab ini baik dibaca berurutan untuk memahami spektrum trade-off pada estimasi pose 6D: dari metode yang paling akurat tetapi paling terikat objek (ZebraPose, GDR-Net) hingga metode yang paling fleksibel terhadap objek baru tetapi bergantung pada kualitas data referensi (OnePose). Keterbatasan OnePose pada objek bertekstur rendah yang dibahas pada bab ini menjadi titik awal pengembangan OnePose++, penerus langsungnya yang tidak dibahas sebagai bab tersendiri dalam tinjauan ini tetapi relevan disebut sebagai konteks perkembangan lanjutan.

## Poin untuk Sitasi

Kutip dengan kunci `sun2022onepose`. Ringkasan yang aman dikutip: "OnePose mengestimasi pose 6D objek arbitrer tanpa model CAD dan tanpa pelatihan ulang per objek, dengan membangun model titik 3D jarang dari video referensi via *structure-from-motion* lalu mencocokkan fitur 2D-3D memakai jaringan atensi grafis (CVPR 2022)." Fakta yang telah dikonfirmasi dari sumber: skema pipeline (SuperPoint/SuperGlue untuk pemetaan, COLMAP untuk SfM, GATs-SPG untuk pencocokan, PnP+RANSAC untuk penyelesaian pose), ukuran dataset OnePose (450 sekuens, 150 objek), evaluasi tambahan pada LINEMOD, serta keterbatasan pada objek bertekstur rendah/berpola berulang/tipis yang disebutkan penulis. Belum terverifikasi dan perlu dicek ulang ke tabel naskah asli sebelum dikutip formal: angka ADD(-S) persis pada LINEMOD dan pada dataset OnePose, serta angka kecepatan (FPS) pelacakan real-time.
