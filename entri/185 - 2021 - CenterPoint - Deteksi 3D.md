# 185 - Center-Based 3D Object Detection and Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yin2021centerpoint` |
| Judul asli | Center-Based 3D Object Detection and Tracking |
| Penulis | Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2006.11275
- **Kode resmi (GitHub):** https://github.com/tianweiy/CenterPoint
- **Google Scholar:** https://scholar.google.com/scholar?q=Center-Based%203D%20Object%20Detection%20and%20Tracking

## Gambaran Umum

Makalah ini memperkenalkan CenterPoint, kerangka deteksi dan pelacakan objek 3D dari data *point cloud* (kumpulan titik koordinat 3D hasil pemindaian LiDAR) yang merepresentasikan setiap objek sebagai satu titik pusat pada peta *bird's-eye view* (BEV, proyeksi tampak-atas dari *point cloud*) alih-alih sebagai kotak beorientasi dengan *anchor* (kotak acuan berukuran dan berorientasi tetap yang ditempatkan berulang di seluruh peta fitur). Deteksi berlangsung dua tahap: tahap pertama menemukan pusat objek lewat deteksi titik kunci (*keypoint detection*) dan meregresi atribut lain (ukuran, orientasi, kecepatan) dari pusat itu; tahap kedua menyempurnakan atribut tersebut memakai fitur titik tambahan yang diambil dari permukaan kotak prediksi. Representasi berbasis pusat ini juga menyederhanakan pelacakan multi-objek: karena jaringan sudah meregresi kecepatan, pusat objek pada bingkai berikutnya dapat diprediksi dan dicocokkan ke deteksi bingkai sebelumnya dengan pencocokan titik terdekat sederhana, tanpa model asosiasi terpisah.

Pada saat rilis, CenterPoint mencapai 65,5 NDS (*nuScenes Detection Score*, metrik gabungan nuScenes) dan 58,0 mAP pada uji deteksi nuScenes, disertai 63,8 AMOTA (*Average Multi-Object Tracking Accuracy*) pada uji pelacakan nuScenes, serta menempati peringkat pertama di antara metode berbasis LiDAR pada papan peringkat Waymo Open Dataset. Makalah ini menjadi rujukan penting bagi klaster Deteksi 3D karena menunjukkan bahwa formulasi berbasis pusat yang sebelumnya berhasil pada deteksi 2D (CenterNet) dapat diperluas ke ruang 3D tanpa kompleksitas *anchor* beorientasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum CenterPoint, detektor 3D dominan seperti VoxelNet, SECOND, dan PointPillars mengikuti paradigma deteksi 2D berbasis *anchor*: peta fitur BEV dibagi menjadi sel, dan pada setiap sel ditempatkan beberapa *anchor* 3D dengan ukuran dan orientasi tertentu (misalnya 0° dan 90°) sebagai kandidat awal. Jaringan kemudian mengklasifikasikan setiap *anchor* dan meregresi selisihnya terhadap kotak kebenaran. Pendekatan ini memiliki tiga kelemahan spesifik untuk domain 3D. Pertama, objek di dunia nyata berputar bebas pada sumbu vertikal (*yaw*), sehingga *anchor* dengan orientasi tetap sering memiliki tumpang-tindih (IoU, *Intersection over Union*) rendah dengan objek yang berorientasi miring, memperlambat konvergensi pelatihan. Kedua, jumlah *anchor* yang dibutuhkan tumbuh dengan jumlah kelas dan orientasi yang dicakup, membebani komputasi dan memori. Ketiga, langkah pasca-pemrosesan standar untuk *anchor* — *non-maximum suppression* (NMS) berbasis rotated-IoU — mahal secara komputasi karena menghitung tumpang-tindih antar-kotak yang berputar, bukan sekadar kotak sumbu-selaras.

Masalah tambahan muncul pada pelacakan (*tracking*) objek 3D lintas-bingkai. Sistem sebelumnya umumnya memakai jaringan asosiasi terpisah atau filter Kalman untuk mencocokkan deteksi antar-bingkai berdasarkan tumpang-tindih kotak 3D, yang rentan gagal ketika objek bergerak cepat sehingga kotak pada bingkai berurutan tidak lagi bertampalan. Bab 145 (nuScenes) menjelaskan bahwa dataset ini menyediakan anotasi kecepatan objek dan lintasan multi-bingkai, kondisi yang belum dimanfaatkan langsung oleh detektor berbasis *anchor* generasi sebelumnya untuk menyederhanakan pelacakan.

## Ide Utama

Gagasan inti CenterPoint adalah mengganti representasi objek dari kotak beorientasi menjadi satu titik: pusat geometris objek pada BEV. Alih-alih mengklasifikasikan dan meregresi ratusan *anchor* per sel, jaringan memprediksi peta panas (*heatmap*) berukuran sama dengan peta fitur BEV, di mana nilai tinggi menandai kemungkinan besar terdapat pusat objek pada lokasi itu. Dari titik puncak *heatmap* tersebut, jaringan meregresi langsung seluruh atribut kotak 3D yang tersisa: offset posisi sub-piksel, tinggi di atas tanah, dimensi (panjang, lebar, tinggi), orientasi (dinyatakan sebagai sepasang nilai sinus-kosinus), dan kecepatan (vx, vy).

Karena representasi ini tidak membandingkan objek dengan bentuk acuan berorientasi tetap, masalah IoU rendah pada objek berputar hilang: jaringan hanya perlu menemukan lokasi satu titik, bukan mencocokkan bentuk. Konsekuensi lanjutannya adalah pelacakan menjadi masalah pencocokan titik: pusat objek pada bingkai t diproyeksikan mundur memakai kecepatan yang diregresi, lalu dicocokkan ke deteksi pada bingkai t−1 melalui pencarian titik terdekat (*greedy closest-point matching*) — algoritme rakus yang memasangkan setiap deteksi ke tetangga terdekatnya secara berurutan tanpa optimasi global.

## Cara Kerja Langkah demi Langkah

### Tahap Pertama: Deteksi Berbasis Pusat

*Point cloud* mentah pertama-tama diproses oleh salah satu dari dua jenis *backbone* (jaringan pengekstrak fitur) yang dapat dipertukarkan: VoxelNet (memakai konvolusi 3D jarang/*sparse* pada grid voksel) atau PointPillars (mengelompokkan titik ke kolom vertikal/*pillar* lalu memprosesnya dengan konvolusi 2D). Keduanya menghasilkan peta fitur BEV dengan resolusi lebih rendah dari *point cloud* asli. Peta fitur ini diteruskan ke kepala deteksi (*detection head*) yang terdiri atas beberapa cabang konvolusi paralel: satu cabang menghasilkan *heatmap* per kelas objek, cabang lain meregresi offset, tinggi, dimensi, orientasi, dan kecepatan pada setiap lokasi.

*Heatmap* dilatih dengan target berbentuk fungsi Gaussian 2D yang berpusat pada lokasi pusat objek sebenarnya, pola yang sama seperti pada CenterNet (detektor 2D berbasis pusat yang menjadi dasar formulasi ini). Puncak Gaussian bernilai 1 tepat di pusat objek dan meluruh secara halus ke arah tepi, sehingga kesalahan lokalisasi kecil di sekitar pusat tetap diberi sinyal gradien, bukan diperlakukan sebagai kesalahan biner. Fungsi *loss* untuk *heatmap* adalah varian *focal loss* (memberi bobot lebih besar pada contoh sulit) yang disesuaikan untuk target Gaussian ini.

### Ekstraksi Deteksi dan Circle NMS

Setelah *heatmap* dihasilkan, lokasi puncak lokal (nilai lebih tinggi dari kedelapan tetangganya) diambil sebagai kandidat pusat objek. Karena representasi berbasis titik tidak memerlukan penghitungan tumpang-tindih kotak berorientasi, makalah mengusulkan *circle NMS*: kandidat dianggap duplikat dan dibuang jika jarak Euklides antar-pusatnya di bawah ambang tertentu, jauh lebih murah secara komputasi dibandingkan NMS berbasis rotated-IoU yang dipakai detektor *anchor*-based.

### Tahap Kedua: Penyempurnaan Fitur Titik

Kotak 3D hasil tahap pertama sering kurang presisi karena hanya dihitung dari satu titik pusat pada peta fitur beresolusi rendah, tanpa memandang tepi objek. Tahap kedua memperbaikinya: dari setiap kotak prediksi, empat titik tengah sisi kotak dan satu titik pusatnya diproyeksikan kembali ke peta fitur BEV, dan fitur pada kelima lokasi tersebut diambil lewat interpolasi bilinear (pembobotan nilai empat piksel tetangga). Kelima vektor fitur ini digabungkan dan dimasukkan ke jaringan saraf sederhana (MLP, *multi-layer perceptron*) yang memprediksi skor keyakinan (*confidence score*) kotak serta koreksi kecil pada posisi, dimensi, dan orientasinya.

Diagram berikut merangkum alur dua tahap ini:

```
point cloud LiDAR
        |
   backbone (VoxelNet / PointPillars)
        |
   peta fitur BEV
        |
   ┌────────────────────────────┐
   │ TAHAP 1: heatmap pusat      │
   │ + regresi (ukuran, yaw,     │
   │   tinggi, kecepatan)        │
   └────────────────────────────┘
        |
   circle NMS -> kandidat kotak 3D
        |
   ┌────────────────────────────┐
   │ TAHAP 2: ambil fitur pada   │
   │ 5 titik (4 sisi + pusat)    │
   │ -> MLP -> skor + koreksi    │
   └────────────────────────────┘
        |
   kotak 3D akhir (per bingkai)
        |
   pencocokan titik terdekat
   antar-bingkai (tracking)
```

### Pelacakan Berbasis Kecepatan

Untuk pelacakan multi-objek, pusat setiap deteksi pada bingkai saat ini digeser mundur sejauh kecepatan teregresi dikalikan selisih waktu antar-bingkai, menghasilkan perkiraan posisi objek yang sama pada bingkai sebelumnya. Perkiraan ini dicocokkan ke pusat deteksi aktual bingkai sebelumnya lewat pencocokan rakus jarak-terdekat: setiap pasangan dengan jarak terkecil dipasangkan lebih dulu, berurutan sampai seluruh deteksi terpasangkan atau melewati ambang jarak maksimum. Pendekatan ini tidak memerlukan jaringan asosiasi terlatih terpisah maupun filter Kalman.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur (*benchmark*) deteksi dan pelacakan 3D untuk kendaraan otonom: nuScenes (bab 145) dan Waymo Open Dataset. nuScenes memberi skor gabungan bernama NDS yang merata-ratakan mAP dengan lima metrik kesalahan (posisi, ukuran, orientasi, kecepatan, atribut), sedangkan Waymo memakai mAPH (mAP berbobot ketepatan *heading*/orientasi).

Pada uji deteksi nuScenes, CenterPoint dengan model tunggal mencapai 65,5 NDS dan 58,0 mAP pada kecepatan proses 11 *frame* per detik (FPS). Pada uji pelacakan nuScenes, metode ini mencapai 63,8 AMOTA, metrik yang menggabungkan akurasi identifikasi objek sepanjang waktu dengan penalti untuk pertukaran identitas (*ID switch*) dan objek yang hilang dari pelacakan. Pada Waymo Open Dataset, konfigurasi bingkai tunggal mencapai 71,9 mAPH memakai *backbone* VoxelNet pada 13 FPS, sedangkan konfigurasi dua-bingkai (menggabungkan fitur dua *point cloud* berurutan) mencapai 73,0 mAPH untuk kelas kendaraan, 71,5 mAPH untuk pejalan kaki, dan 71,3 mAPH untuk pesepeda pada 11 FPS. Penulis melaporkan bahwa hasil ini menempatkan CenterPoint di peringkat pertama di antara seluruh metode berbasis LiDAR pada papan peringkat Waymo saat publikasi.

Interpretasinya: perbandingan langsung dengan detektor *anchor*-based generasi sebelumnya (PointPillars, SECOND) pada makalah asli menunjukkan CenterPoint unggul terutama pada kelas objek dengan variasi ukuran dan orientasi besar (misalnya kendaraan besar dan pejalan kaki), konsisten dengan klaim bahwa penghapusan *anchor* mengurangi kesalahan akibat ketidaksesuaian orientasi. Angka pasti perbandingan margin terhadap setiap baseline pada makalah tidak dikutip di sini dan perlu diverifikasi langsung ke tabel naskah.

## Kelebihan dan Keterbatasan

Kelebihan utama CenterPoint adalah kesederhanaan representasi: satu titik per objek menghilangkan kebutuhan menyetel jumlah, ukuran, dan orientasi *anchor*, sekaligus mempercepat pasca-pemrosesan lewat *circle NMS*. Kerangka ini juga bersifat agnostik terhadap *backbone* — dapat dipasangkan dengan VoxelNet maupun PointPillars — sehingga mudah diintegrasikan ke sistem yang sudah ada. Penyatuan deteksi dan pelacakan dalam satu alur, tanpa model asosiasi terpisah, mengurangi kompleksitas sistem produksi.

Dari sisi rekayasa, tahap penyempurnaan kedua menambah biaya komputasi dan latensi dibandingkan detektor satu tahap murni, meski makalah melaporkan kecepatan tetap kompetitif (11-13 FPS). Secara konseptual, pencocokan titik terdekat untuk pelacakan bergantung pada akurasi regresi kecepatan; kesalahan kecepatan yang besar berpotensi menyebabkan kesalahan asosiasi pada objek yang bergerak cepat atau berdekatan, meskipun makalah tidak melaporkan kegagalan sistematik semacam ini. Metode ini juga sepenuhnya bergantung pada data LiDAR sebagai masukan utama; penerapannya pada data RGB-D atau *pseudo-LiDAR* (titik 3D hasil estimasi kedalaman dari kamera) memerlukan penyesuaian kualitas *point cloud* yang lebih jarang dan lebih berisik dibandingkan LiDAR asli.

## Kaitan dengan Bab Lain

CenterPoint mewarisi prinsip deteksi berbasis titik kunci dari CenterNet pada domain 2D, dan menerapkannya pada *point cloud* yang diproses lewat *backbone* voksel/pilar sejenis yang dipakai VoxelNet, SECOND, dan PointPillars. Bab 186 ([PV-RCNN](./186%20-%202020%20-%20PV-RCNN%20-%20Deteksi%203D.md)) juga memakai penyempurnaan dua tahap berbasis fitur titik, tetapi tahap pertamanya tetap berbasis *anchor* atau *region proposal*, berbeda dengan tahap pertama CenterPoint yang sepenuhnya bebas-*anchor*; kedua bab ini baik dibaca berdampingan untuk membandingkan dua strategi penyempurnaan dua tahap. Bab 187 ([BEVFormer](./187%20-%202022%20-%20BEVFormer%20-%20Deteksi%203D.md)) dan bab 188 ([DETR3D](./188%20-%202022%20-%20DETR3D%20-%20Deteksi%203D.md)) melanjutkan arah bebas-*anchor* dengan mengganti sumber data utama dari LiDAR menjadi kamera multi-sudut-pandang, memakai representasi kueri (*query*) berbasis Transformer alih-alih *heatmap* konvolusi. Bab 145 ([nuScenes](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)) mendefinisikan dataset dan metrik NDS/AMOTA yang menjadi tolok ukur utama evaluasi CenterPoint pada bagian eksperimen di atas.

## Poin untuk Sitasi

Kutip dengan kunci `yin2021centerpoint`. Ringkasan yang aman dikutip: "CenterPoint mendeteksi objek 3D dari *point cloud* LiDAR sebagai titik pusat pada BEV lewat deteksi *heatmap* dua-tahap, lalu menyederhanakan pelacakan multi-objek dengan pencocokan titik terdekat berbasis kecepatan teregresi, mencapai 65,5 NDS dan 63,8 AMOTA pada nuScenes serta peringkat pertama berbasis LiDAR pada Waymo Open Dataset." Angka 65,5 NDS, 58,0 mAP, 63,8 AMOTA, 71,9 mAPH (bingkai tunggal), dan 73,0/71,5/71,3 mAPH (dua-bingkai per kelas) berasal dari abstrak dan repositori resmi; rincian tabel ablasi, margin perbandingan per-baseline, dan konfigurasi hiperparameter lengkap (ambang *circle NMS*, jumlah lapis MLP tahap kedua) perlu diverifikasi ke naskah CVPR 2021 sebelum dikutip dalam karya formal.
