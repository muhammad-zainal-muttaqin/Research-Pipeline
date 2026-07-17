# 087 - VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2018voxelnet` |
| Judul asli | VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection |
| Penulis | Yin Zhou, Oncel Tuzel |
| Tahun | 2018 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2018) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1711.06396
- **Versi resmi CVPR (IEEE/CVF Open Access):** https://openaccess.thecvf.com/content_cvpr_2018/html/Zhou_VoxelNet_End-to-End_Learning_CVPR_2018_paper.html
- **Google Scholar:** https://scholar.google.com/scholar?q=VoxelNet%3A%20End-to-End%20Learning%20for%20Point%20Cloud%20Based%203D%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=VoxelNet%3A%20End-to-End%20Learning%20for%20Point%20Cloud%20Based%203D%20Object%20Detection&sort=relevance

## Gambaran Umum

VoxelNet adalah jaringan deteksi objek 3D pertama yang dilatih *end-to-end* (dari data mentah ke keluaran akhir tanpa tahap terpisah) langsung dari *point cloud* (kumpulan titik koordinat 3D hasil pemindaian sensor jarak, di sini LiDAR) mentah, tanpa fitur buatan tangan. Makalah ini membagi *point cloud* menjadi *voxel* (sel volumetrik 3D, analog piksel berdimensi tiga), mempelajari fitur tiap *voxel* dengan lapisan *Voxel Feature Encoding* (VFE) yang terinspirasi PointNet, lalu memproses tensor *voxel* dengan konvolusi 3D dan *Region Proposal Network* (RPN, jaringan pengusul wilayah yang sebelumnya dipakai Faster R-CNN) untuk menghasilkan kotak pembatas 3D berorientasi.

Pada set validasi KITTI, tolok ukur standar deteksi objek untuk kendaraan otonom, VoxelNet mencapai *Average Precision* (AP) 3D untuk kelas mobil sebesar 81,97% (mudah), 65,46% (sedang), dan 62,85% (sulit), mengungguli metode berbasis fitur buatan tangan pada masanya, terutama untuk pejalan kaki dan pesepeda yang bentuknya lebih kecil dan tidak kaku. Makalah ini meletakkan paradigma "voxelisasi lalu pelajari fitur" yang dirujuk langsung oleh metode deteksi 3D berbasis *point cloud* sesudahnya, termasuk PointPillars yang menyederhanakan konvolusi 3D-nya demi kecepatan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum VoxelNet, sensor LiDAR (*Light Detection and Ranging*, sensor laser yang mengukur jarak dengan memantulkan cahaya) menghasilkan *point cloud* tidak beraturan: jumlah titik per satuan volume bervariasi tajam menurut jarak ke sensor, dan titik-titiknya tidak tersusun dalam kisi tetap seperti piksel pada citra. Jaringan konvolusi (CNN) dirancang untuk data berkisi seragam, sehingga tidak dapat diterapkan langsung pada data ini.

Dua pendekatan mengatasi ketidaksesuaian ini. Pertama, metode berbasis proyeksi dan fitur buatan tangan: *point cloud* diproyeksikan ke tampilan tampak-atas (*bird's-eye view*/BEV) atau tampak-depan, lalu setiap sel proyeksi diberi statistik rancangan manual seperti kepadatan titik, tinggi rata-rata, dan intensitas maksimum, sebelum diproses CNN 2D biasa. MV3D (bab 091) menggabungkan fitur BEV, tampak-depan, dan citra RGB dengan cara ini, tetapi representasi yang dirancang manual tidak ikut dioptimalkan bersama tujuan akhir deteksi, sehingga sebagian informasi bentuk 3D yang relevan untuk lokalisasi presisi hilang sebelum sampai ke jaringan.

Kedua, PointNet (2017) menunjukkan fitur dapat dipelajari langsung dari titik mentah memakai jaringan terhubung penuh per titik dikombinasikan dengan fungsi simetris (*max pooling*, pengambilan nilai maksimum) agar hasilnya tidak bergantung pada urutan titik, tetapi dirancang untuk klasifikasi dan segmentasi pada himpunan titik berskala kecil, bukan untuk deteksi pada adegan luar ruang berskala besar dengan puluhan ribu titik. Masalah yang tersisa adalah mempelajari fitur diskriminatif langsung dari *point cloud* mentah, tanpa rekayasa fitur manual, sekaligus tetap efisien untuk adegan sebesar itu.

## Ide Utama

VoxelNet menggabungkan dua gagasan. Pertama, *point cloud* yang tidak beraturan dipartisi menjadi *voxel* berukuran tetap: ruang 3D kontinu didiskretkan menjadi kisi sel, sehingga titik-titik yang jatuh dalam satu sel dapat dikelompokkan dan diproses bersama sebagai himpunan titik lokal berskala kecil. Kedua, di dalam setiap *voxel* yang tidak kosong, sebuah jaringan kecil bergaya PointNet (VFE) mempelajari satu vektor fitur yang meringkas bentuk lokal titik-titik di dalamnya, mengubah himpunan titik tidak beraturan menjadi tensor 4 dimensi terstruktur — mirip citra tetapi dengan sumbu kedalaman tambahan — yang dapat diproses konvolusi 3D biasa.

Setelah representasi terstruktur ini terbentuk, VoxelNet menerapkan komponen yang sudah dikenal dari detektor 2D: konvolusi 3D untuk mengumpulkan konteks antar-*voxel* tetangga, kemudian RPN untuk menghasilkan kotak pembatas 3D akhir berisi posisi, dimensi, dan sudut orientasi (*yaw*) objek. Seluruh proses, dari titik mentah sampai kotak 3D, dilatih sebagai satu jaringan tunggal.

## Cara Kerja Langkah demi Langkah

### Partisi Voxel dan Pengambilan Sampel Titik

Untuk deteksi mobil, ruang 3D di sekitar kendaraan dipartisi menjadi *voxel* berukuran 0,2 m × 0,2 m pada bidang horizontal dan 0,4 m pada sumbu tegak, menghasilkan kisi berdimensi 10 × 400 × 352 (kedalaman × tinggi × lebar). Karena kepadatan titik LiDAR menurun tajam terhadap jarak, jumlah titik per *voxel* berkisar dari nol hingga ribuan. Untuk membatasi beban komputasi dan memori, jumlah titik per *voxel* dibatasi maksimum T (T = 35 untuk mobil, T = 45 untuk pejalan kaki dan pesepeda); bila suatu *voxel* memiliki titik lebih banyak dari T, sejumlah T titik diambil secara acak, sekaligus mengurangi bias jaringan terhadap *voxel* yang kebetulan berisi lebih banyak titik.

### Voxel Feature Encoding (VFE)

Setiap titik dalam *voxel* direpresentasikan dengan 7 angka: koordinat (x, y, z), intensitas pantulan r, dan selisih posisi titik terhadap titik rata-rata seluruh titik dalam *voxel* tersebut (Δx, Δy, Δz). Lapisan VFE-1 mengubah 7 angka ini menjadi 32 angka melalui jaringan terhubung penuh, diikuti normalisasi *batch* (penyeragaman statistik aktivasi antar-titik agar pelatihan stabil) dan ReLU (fungsi aktivasi yang mempertahankan nilai positif dan menolkan nilai negatif). Dari fitur 32 angka setiap titik dilakukan *max pooling* di seluruh titik dalam *voxel* untuk memperoleh satu fitur teragregasi lokal yang mewakili seluruh isi *voxel*; fitur ini digabungkan kembali ke fitur setiap titik sehingga setiap titik memperoleh konteks dari tetangganya. Susunan yang sama diulang pada VFE-2, memetakan 32 menjadi 128 angka, lalu satu kali *max pooling* terakhir menghasilkan satu vektor 128 dimensi per *voxel*, terlepas dari berapa banyak titik yang semula ada di dalamnya.

Hasil dari seluruh proses ini adalah tensor jarang (*sparse*, sebagian besar selnya kosong karena banyak *voxel* tidak memiliki titik) berukuran 128 × 10 × 400 × 352 (kanal × kedalaman × tinggi × lebar) untuk kasus mobil.

Alur data dari titik mentah sampai kotak 3D dapat diringkas sebagai berikut:

```
point cloud mentah (tak beraturan, ratusan ribu titik)
        |
        v   partisi ke voxel 0,2 x 0,2 x 0,4 m (kisi 352x400x10)
voxel berisi 0..T titik -> VFE-1(7,32) -> VFE-2(32,128) -> max-pool
        |          (tiap voxel diringkas jadi satu vektor 128 dim)
        v
tensor voxel jarang: 128 x 10 x 400 x 352 (kanal x D x H x W)
        |
        v   tiga lapis konvolusi 3D (mereduksi sumbu kedalaman 10 -> 2)
peta fitur mirip 2D: 128 x 400 x 352
        |
        v   RPN: tiga blok konvolusi + upsampling + penggabungan
peta skor objek  +  peta regresi parameter kotak
        |
        v   Non-Maximum Suppression pada bidang tampak-atas (BEV)
kotak 3D akhir per objek: (x, y, z, l, w, h, yaw)
```

### Lapisan Konvolusi Tengah dan Reduksi ke Peta 2D

Tiga lapis konvolusi 3D memproses tensor *voxel* untuk memperluas jangkauan reseptif (wilayah masukan yang memengaruhi satu keluaran) dan mengumpulkan konteks antar-*voxel*, sambil bertahap mereduksi sumbu kedalaman dari 10 menjadi 2. Tensor 64 × 2 × 400 × 352 yang tersisa ditumpuk (kedua irisan kedalaman digabung sepanjang sumbu kanal) menjadi peta fitur 128 × 400 × 352 yang berperilaku seperti fitur 2D bagi RPN, tetapi seluruh nilainya dipelajari, bukan dihitung dengan rumus statistik tetap seperti BEV buatan tangan.

### Region Proposal Network dan Anchor 3D

RPN tersusun atas tiga blok konvolusi dengan penurunan resolusi (*stride* 2) bertahap, diikuti *upsampling* (pembesaran kembali resolusi peta fitur) dan penggabungan (*concatenation*) ketiga skala menjadi satu peta fitur beresolusi tinggi, lalu memprediksi peta skor keberadaan objek dan peta regresi parameter kotak 3D. Setiap posisi diberi dua *anchor* (kotak acuan berukuran tetap, dirotasi 0° dan 90°); untuk mobil, ukurannya panjang 3,9 m, lebar 1,6 m, tinggi 1,56 m dengan pusat ketinggian −1,0 m, sedangkan pejalan kaki dan pesepeda memakai *anchor* lebih kecil. Setiap *anchor* diberi label positif/negatif berdasarkan IOU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan) terhadap kotak kebenaran pada bidang BEV, mengikuti konvensi RPN pada Faster R-CNN (bab 014), diperluas ke ruang 3D.

### Fungsi Loss dan Pelatihan

Fungsi *loss* terdiri atas *loss* klasifikasi berupa *binary cross-entropy* (galat entropi silang biner) untuk membedakan *anchor* positif dan negatif, serta *loss* regresi berupa *Smooth L1* untuk tujuh parameter kotak (selisih posisi Δx, Δy, Δz; selisih dimensi Δl, Δw, Δh; selisih sudut Δθ), dinormalisasi terhadap diagonal *anchor*. Untuk mobil, kedua komponen diberi bobot α = 1,5 pada suku positif dan β = 1,0 pada suku negatif, menyeimbangkan pengaruh *anchor* berisi objek yang jauh lebih sedikit daripada *anchor* kosong.

### Inferensi

Saat inferensi, satu kali evaluasi jaringan pada GPU Titan X memerlukan total 225 milidetik (setara sekitar 4,4 FPS): 5 milidetik voxelisasi, 20 milidetik lapisan VFE, 170 milidetik konvolusi tengah 3D (komponen paling mahal), dan 30 milidetik RPN. Kotak-kotak yang tumpang tindih dirampingkan dengan *Non-Maximum Suppression*, mempertahankan hanya kotak berskor tertinggi pada tiap kelompok kotak yang saling menutupi.

## Eksperimen dan Hasil

Evaluasi dilakukan pada set validasi KITTI, tolok ukur deteksi objek untuk skenario berkendara, dengan tiga kelas: mobil, pejalan kaki, dan pesepeda. Metrik yang dipakai adalah AP 3D (dari volume irisan kotak 3D) dan AP BEV (dari irisan kotak pada proyeksi tampak-atas), masing-masing dilaporkan pada tiga tingkat kesulitan yang ditetapkan KITTI berdasarkan ukuran objek, oklusi, dan pemotongan tepi citra: mudah, sedang, dan sulit.

Hasil AP 3D VoxelNet: mobil 81,97%/65,46%/62,85%, pejalan kaki 57,86%/53,42%/48,87%, pesepeda 67,17%/47,65%/45,11% (mudah/sedang/sulit). Hasil AP BEV: mobil 89,60%/84,81%/78,57%, pejalan kaki 65,95%/61,05%/56,98%, pesepeda 74,41%/52,18%/50,49%. Dibandingkan HC-baseline, metode BEV berbasis fitur buatan tangan, VoxelNet unggul pada AP BEV mobil tingkat sedang (84,81% berbanding 78,42%, selisih 6,4 poin) dan lebih lebar pada pejalan kaki tingkat sedang (61,05% berbanding 53,79%, selisih 7,3 poin) — selisih terbesar justru pada kelas kecil dan tidak kaku, tempat statistik buatan tangan paling sulit merepresentasikan bentuk secara akurat.

Dari sisi kecepatan, 225 milidetik per citra (4,4 FPS) jauh di bawah kebutuhan *real-time* kendaraan otonom dan kecepatan detektor 2D seperti YOLO (45 FPS, bab 001); sebagian besar waktu habis pada konvolusi 3D di lapisan tengah, motivasi langsung metode deteksi 3D berikutnya mengganti konvolusi 3D dengan operasi lebih murah.

## Kelebihan dan Keterbatasan

Kelebihan utama VoxelNet adalah menghapus kebutuhan rekayasa fitur manual: seluruh proses, dari titik mentah sampai kotak 3D, dipelajari dan dioptimalkan sebagai satu jaringan, sehingga representasi *voxel* lebih sesuai dengan tujuan deteksi dibandingkan statistik buatan tangan. Keunggulan ini paling terasa pada kelas kecil dan tidak kaku seperti pejalan kaki dan pesepeda, sebagaimana ditunjukkan selisih AP terhadap HC-baseline pada bagian sebelumnya.

Dari sisi rekayasa, konvolusi 3D pada tensor *voxel* yang sebagian besar kosong memakan porsi waktu terbesar (170 dari 225 milidetik), sehingga VoxelNet tidak mencapai kecepatan *real-time* yang dibutuhkan aplikasi kendaraan otonom. Secara konseptual, pembagian ruang menjadi *voxel* tetap juga membatasi presisi posisi titik di dalam satu sel, karena semua titik dalam *voxel* yang sama diringkas menjadi satu vektor sehingga variasi posisi di bawah resolusi *voxel* tidak lagi dibedakan; pembatasan jumlah titik per *voxel* menjadi maksimum T dengan sampel acak juga berarti sebagian titik pada *voxel* padat dibuang, berpotensi menghilangkan detail bentuk dekat sensor. VoxelNet hanya memanfaatkan data LiDAR tanpa citra RGB, berbeda dari MV3D yang memfusikan kedua sumber.

## Kaitan dengan Bab Lain

RPN yang dipakai VoxelNet mewarisi langsung konsep *Region Proposal Network* dari Faster R-CNN (bab 014), diperluas dari kotak 2D ke kotak 3D berorientasi. VoxelNet juga berlawanan posisi dengan pendekatan fitur buatan tangan MV3D (bab 091), yang memproyeksikan *point cloud* ke BEV dan tampak-depan lalu menggabungkannya dengan citra RGB memakai statistik rancangan manual. Biaya konvolusi 3D yang tinggi pada VoxelNet menjadi motivasi langsung PointPillars (bab 088), yang mengganti *voxel* 3D dengan kolom vertikal (*pillar*) agar data dapat diproses konvolusi 2D dan berjalan lebih cepat tanpa mengubah gagasan inti "pelajari fitur dari titik mentah". Paradigma ini juga berkaitan dengan Pseudo-LiDAR (bab 095), yang mengubah peta kedalaman kamera menjadi *point cloud* semu agar dapat diproses jaringan bergaya VoxelNet.

## Poin untuk Sitasi

Kutip dengan kunci `zhou2018voxelnet`. Ringkasan aman dikutip: "VoxelNet mempelajari fitur *voxel* langsung dari *point cloud* LiDAR mentah melalui lapisan *Voxel Feature Encoding*, lalu memproses tensor *voxel* dengan konvolusi 3D dan *Region Proposal Network* untuk deteksi 3D *end-to-end*, mencapai AP BEV mobil 84,81% pada tingkat sedang di KITTI, mengungguli metode berbasis fitur buatan tangan pada masanya." Angka AP 3D/BEV, konfigurasi *voxel* (0,2 m × 0,2 m × 0,4 m, T = 35/45), dan waktu inferensi 225 milidetik telah diverifikasi terhadap naskah arXiv/ar5iv. Ambang IOU untuk penetapan label *anchor* positif/negatif tidak berhasil diverifikasi langsung dari sumber yang diakses dan sebaiknya dicek ulang ke naskah asli sebelum dikutip dalam karya formal.
