# 089 - PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shi2019pointrcnn` |
| Judul asli | PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud |
| Penulis | Shaoshuai Shi, Xiaogang Wang, Hongsheng Li |
| Tahun | 2019 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2019), hlm. 770–779 |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1812.04244
- **Google Scholar:** https://scholar.google.com/scholar?q=PointRCNN%3A%203D%20Object%20Proposal%20Generation%20and%20Detection%20from%20Point%20Cloud
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PointRCNN%3A%203D%20Object%20Proposal%20Generation%20and%20Detection%20from%20Point%20Cloud&sort=relevance

## Gambaran Umum

PointRCNN adalah detektor objek 3D dua tahap yang bekerja langsung pada *point cloud* (kumpulan titik koordinat 3D dari sensor LiDAR, tanpa struktur grid), tanpa mengubahnya lebih dahulu menjadi *voxel* (sel volume 3D diskret) atau proyeksi tampak-atas. Tahap pertama mensegmentasi setiap titik menjadi latar depan (bagian objek) atau latar belakang, lalu setiap titik latar depan langsung mengusulkan satu kotak 3D — proposal *bottom-up* yang bergerak dari titik individual ke kotak, bukan dari kumpulan *anchor* (kotak acuan berukuran tetap) yang disebar merata di ruang 3D. Tahap kedua mengambil titik di dalam setiap proposal, memindahkannya ke koordinat kanonik (kerangka acuan lokal berpusat dan berorientasi pada proposal itu sendiri), lalu menyempurnakan posisi, ukuran, dan orientasi kotak.

Pada benchmark KITTI 3D (data deteksi objek kendaraan otonom berisi *scan* LiDAR dan citra kamera berpasangan), PointRCNN memakai *modality* LiDAR saja dan mencapai *average precision* (AP, metrik presisi rata-rata pada berbagai ambang *recall*) sebesar 85,94% (mudah), 75,76% (sedang), dan 68,32% (sulit) untuk kelas mobil pada set uji, melampaui metode berbasis *voxel* seperti SECOND maupun metode fusi citra-LiDAR seperti F-PointNet dan AVOD-FPN. Makalah ini menjadi rujukan awal bahwa proposal berbasis titik murni dapat mengungguli pendekatan berbasis *voxel* atau multimodal pada deteksi mobil.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum PointRCNN, dua jalur utama mendominasi deteksi objek 3D dari LiDAR. Jalur pertama mengubah *point cloud* menjadi representasi grid: VoxelNet (bab 087) membagi ruang 3D menjadi *voxel* lalu menerapkan konvolusi 3D, sementara metode berbasis proyeksi tampak-atas (*bird's-eye view*, BEV) memampatkan ketinggian menjadi kanal fitur pada peta 2D. Diskretisasi ini menyederhanakan komputasi tetapi membuang detail geometri halus — dua titik berjarak berbeda di dalam satu *voxel* menjadi tidak terbedakan. Jalur kedua, seperti F-PointNet dan MV3D (bab 091), menghasilkan proposal 3D dengan bantuan citra RGB: deteksi 2D pada kamera membatasi wilayah pencarian di ruang 3D (disebut *frustum*, volume piramida yang memanjang dari kamera). Pendekatan ini bergantung pada kualitas deteksi 2D dan kalibrasi kamera-LiDAR yang presisi, sehingga gagal bila citra tidak tersedia atau kalibrasi meleset.

Alternatif yang belum banyak dieksplorasi saat itu adalah menghasilkan proposal 3D langsung dari titik mentah, tanpa voxelisasi maupun bantuan citra. Kesulitannya dua hal. Pertama, *point cloud* dari LiDAR bersifat jarang dan tidak seragam kerapatannya — titik yang jauh dari sensor lebih renggang daripada yang dekat — sehingga jaringan harus tahan terhadap kepadatan yang bervariasi. Kedua, ruang pencarian proposal 3D jauh lebih besar daripada ruang 2D: setiap kotak memerlukan tujuh parameter (pusat x, y, z; panjang, lebar, tinggi; sudut hadap/*yaw*), sehingga menyebar *anchor* padat ke seluruh ruang 3D menjadi mahal secara komputasi dan boros memori.

## Ide Utama

Gagasan inti PointRCNN adalah membalik urutan kerja: alih-alih menebak lokasi objek lebih dahulu lalu memeriksa titik di sekitarnya (cara kerja berbasis *anchor*), jaringan terlebih dahulu memutuskan titik mana yang merupakan bagian dari objek, kemudian membiarkan setiap titik tersebut mengusulkan kotaknya sendiri. Karena setiap titik latar depan sudah berada tepat pada permukaan objek, proposal yang dihasilkan secara alami memiliki lokasi awal yang akurat — berbeda dengan *anchor* yang disebar merata tanpa mengetahui isi *scene*.

Gagasan kedua, setelah proposal terbentuk, adalah menyempurnakan kotak bukan di koordinat dunia asli, melainkan di koordinat kanonik: setiap proposal memindahkan titik-titik lokalnya sehingga pusat proposal menjadi titik asal dan salah satu sumbunya sejajar dengan arah hadap proposal. Dengan kerangka acuan seragam ini, jaringan penyempurnaan tahap kedua tidak perlu mempelajari variasi posisi absolut di seluruh *scene* — cukup koreksi kecil relatif terhadap proposal, tugas yang jauh lebih sederhana.

## Cara Kerja Langkah demi Langkah

### Praproses dan Backbone PointNet++

Setiap adegan (*scene*) LiDAR disubsampel menjadi 16.384 titik sebagai masukan; adegan dengan titik lebih sedikit diisi ulang dengan pengulangan titik acak. Setiap titik direpresentasikan oleh koordinat (x, y, z) dan intensitas pantulan laser, lalu diproses oleh *backbone* PointNet++ dengan skema *multi-scale grouping* (MSG): jaringan bekerja langsung pada titik tanpa voxelisasi, mengelompokkan titik bertetangga pada beberapa radius berbeda secara bertingkat sehingga fitur yang dipelajari mencakup konteks lokal pada berbagai skala jarak. Keluarannya adalah satu vektor fitur per titik masukan.

### Tahap 1: Segmentasi Titik dan Proposal Bottom-Up

Dari fitur per titik itu, dua kepala (*head*) jaringan bekerja paralel. Kepala segmentasi mengklasifikasikan setiap titik sebagai latar depan (bagian objek target) atau latar belakang. Karena jumlah titik latar depan pada satu adegan jalan raya jauh lebih sedikit daripada titik latar belakang (jalan, gedung, vegetasi), pelatihan kepala ini memakai *focal loss* — fungsi kerugian yang menurunkan bobot kontribusi contoh yang mudah diklasifikasikan agar pembelajaran tidak didominasi titik latar belakang.

Kepala kedua, regresi kotak, berjalan pada setiap titik latar depan dan menghasilkan satu proposal 3D per titik. Regresi ini memakai skema *bin-based*: rentang nilai koordinat pusat pada sumbu X dan Z, serta sudut orientasi, dibagi menjadi sejumlah *bin* (kotak nilai diskret). Jaringan memilih *bin* yang benar lewat klasifikasi *cross-entropy*, kemudian meregresi residu halus di dalam *bin* tersebut dengan *smooth L1 loss* (fungsi kerugian regresi yang tidak terlalu sensitif terhadap galat besar). Sumbu Y (ketinggian), yang rentangnya jauh lebih sempit karena objek jalan raya berada pada bidang tanah relatif datar, diregresi langsung dengan *smooth L1* tanpa pembagian *bin*. Skema ini terbukti pada uji ablasi makalah konvergen lebih cepat dan mencapai *recall* (proporsi objek yang berhasil diusulkan) lebih tinggi dibandingkan regresi langsung, regresi berbasis kosinus sudut, maupun regresi berbasis sudut kotak.

Kualitas proposal yang dihasilkan diukur lewat *recall*: dengan hanya 50 proposal per adegan, PointRCNN mencapai 96,01% *recall* pada ambang IoU (*Intersection over Union*, rasio irisan terhadap gabungan luas antara kotak prediksi dan kebenaran) 0,5 untuk kelas mobil tingkat kesulitan sedang — jauh melampaui 91% yang dicapai AVOD dengan jumlah proposal yang sebanding. Angka ini menunjukkan bahwa proposal berbasis titik menghasilkan kandidat kotak yang jauh lebih sedikit terbuang dibandingkan pendekatan berbasis *anchor*.

### Tahap 2: Transformasi Kanonik dan Penyempurnaan

Untuk setiap proposal, titik di dalam dan di sekitarnya (dengan margin konteks tambahan) dikumpulkan, lalu koordinatnya ditransformasikan ke sistem kanonik: asal (0,0,0) dipindah ke pusat proposal dan sumbu diputar sejajar arah hadap proposal. Pada koordinat baru ini, jaringan tahap kedua menggabungkan tiga sumber informasi — koordinat lokal titik dalam kerangka kanonik, intensitas laser dan skor segmentasi dari tahap pertama, serta fitur semantik global dari *backbone* — untuk meregresi koreksi akhir posisi, ukuran, dan orientasi kotak, sekaligus memprediksi skor keyakinan (*confidence*) bahwa kotak tersebut berisi objek. Margin konteks di sekitar proposal (disebut η) diuji pada beberapa nilai; nilai optimal ditemukan pada η = 1,0 meter, sedangkan margin lebih besar mulai menyertakan titik dari objek tetangga yang mengganggu penyempurnaan.

Alur dua tahap ini dapat diringkas sebagai berikut:

```
point cloud mentah (16.384 titik: x,y,z,intensitas)
                |
                v
   backbone PointNet++ (multi-scale grouping)
                |
        +-------+-------+
        |               |
        v               v
 segmentasi titik   regresi kotak
 (latar depan/     bin-based per
  latar belakang)   titik latar depan
        |               |
        +-------+-------+
                v
     proposal 3D bottom-up
     (klasifikasi bin + residu)
                |
                v
  transformasi ke koordinat kanonik
  per proposal (pusat & orientasi)
                |
                v
   tahap 2: gabung fitur lokal
   kanonik + fitur global tahap 1
                |
                v
   kotak 3D akhir (x,y,z,l,w,h,yaw)
        + skor confidence
```

### Fungsi Loss

Pelatihan menggabungkan empat komponen: *focal loss* untuk segmentasi titik, *cross-entropy* untuk klasifikasi *bin* pada regresi kotak tahap pertama, *smooth L1* untuk residu dalam *bin* dan sumbu Y, serta kerugian serupa pada tahap kedua untuk penyempurnaan kotak dan klasifikasi *confidence* akhir. Tahap kedua hanya menerima proposal yang sudah dihasilkan tahap pertama sebagai masukan, sehingga kualitasnya bergantung pada kualitas tahap pertama.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada KITTI 3D Object Detection Benchmark, data deteksi objek untuk skenario mengemudi yang memakai sensor LiDAR Velodyne dan kamera stereo terkalibrasi. Metrik utamanya AP 3D pada tiga tingkat kesulitan (mudah, sedang, sulit — dibedakan dari ukuran objek pada citra, tingkat oklusi, dan pemotongan tepi citra), dengan tingkat sedang umumnya dipakai sebagai acuan peringkat utama.

| Metode | Modalitas | Mobil (mudah) | Mobil (sedang) | Mobil (sulit) |
|---|---|---|---|---|
| PointRCNN | LiDAR saja | 85,94% | 75,76% | 68,32% |
| SECOND | LiDAR saja | 83,13% | 73,66% | 66,20% |
| AVOD-FPN | RGB + LiDAR | 81,94% | 71,88% | 66,38% |
| F-PointNet | RGB + LiDAR | 81,20% | 70,39% | 62,19% |

Pada tingkat kesulitan sedang, PointRCNN unggul sekitar 2,1 poin AP dari SECOND (metode berbasis *voxel* terkuat pada tabel ini) dan sekitar 3,9–5,4 poin dari dua metode yang justru memakai tambahan citra RGB. Interpretasinya: informasi tekstur dari kamera tidak lantas menjamin proposal 3D yang lebih baik jika geometri titik sudah diproses dengan cukup teliti — proposal berbasis titik murni pada PointRCNN menghasilkan lokalisasi yang lebih presisi tanpa bantuan citra sama sekali.

Uji ablasi menunjukkan kontribusi setiap komponen. Menghilangkan transformasi kanonik pada tahap kedua menjatuhkan AP tingkat sedang secara drastis dari 77,67% menjadi 13,68% — bukti bahwa kerangka acuan lokal, bukan sekadar penyempurnaan lanjutan, adalah komponen yang menentukan keberhasilan tahap kedua. Menyertakan fitur semantik global dari tahap pertama sebagai masukan tambahan tahap kedua menyumbang kenaikan sekitar 2,71 poin AP pada tingkat sedang, menunjukkan bahwa konteks yang dipelajari pada tahap awal tetap berguna meski titik sudah dipindah ke koordinat kanonik.

## Kelebihan dan Keterbatasan

Kelebihan utama PointRCNN adalah presisi proposal: karena proposal berasal langsung dari titik latar depan, bukan dari *anchor* yang disebar tanpa mengetahui isi *scene*, kualitas kandidat kotak pada tahap awal sudah tinggi (96,01% *recall* dengan hanya 50 proposal). Pendekatan ini juga tidak bergantung pada citra RGB maupun kalibrasi kamera-LiDAR, sehingga tetap berfungsi pada sensor LiDAR-saja. Skema *bin-based regression* memberi jaringan target yang lebih mudah dipelajari dibandingkan regresi langsung nilai kontinu, terbukti dari uji ablasi pada makalah.

Dari sisi rekayasa, arsitektur dua tahap dengan *backbone* PointNet++ per titik cenderung lebih mahal secara komputasi dibandingkan metode satu tahap berbasis *voxel* atau *pillar* seperti VoxelNet atau PointPillars (bab 088), karena pemrosesan titik individual pada PointNet++ tidak semudah dipetakan ke operasi konvolusi grid yang teroptimasi perangkat keras. Sumber yang diperiksa untuk bab ini tidak melaporkan angka kecepatan inferensi (FPS), sehingga perbandingan kecepatan tidak dapat dinyatakan kuantitatif di sini. Secara konseptual, karena metode ini murni mengandalkan geometri titik LiDAR, ia tidak memanfaatkan informasi tekstur atau warna pada citra kamera — keterbatasan yang menjadi motivasi metode fusi LiDAR-kamera pada bab-bab lain di klaster ini.

## Kaitan dengan Bab Lain

PointRCNN berada pada posisi kontras dengan dua jalur deteksi 3D lain dalam klaster ini. Terhadap bab 087 (VoxelNet), yang mendiskretisasi *point cloud* menjadi *voxel* sebelum konvolusi 3D, PointRCNN menunjukkan bahwa proposal langsung dari titik menghindari kehilangan detail akibat diskretisasi. Terhadap bab 088 (PointPillars), yang memilih representasi kolom (*pillar*) demi kecepatan, PointRCNN mewakili ujung spektrum yang mengutamakan presisi proposal di atas kecepatan. Tabel eksperimen di atas juga langsung melibatkan F-PointNet, metode fusi berbasis *frustum* yang dibahas pada [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md), serta pendekatan multimodal berbasis BEV pada [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md). Skema segmentasi titik dan regresi *bin-based* di sini menjadi rujukan desain bagi metode fusi LiDAR-kamera yang lebih baru, seperti [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md), yang mewarisi ide "menandai titik lalu memprosesnya per titik" namun menambahkan informasi semantik dari citra sebelum segmentasi.

## Poin untuk Sitasi

Kutip dengan kunci `shi2019pointrcnn`. Ringkasan yang aman dikutip: "PointRCNN menghasilkan proposal 3D bottom-up langsung dari titik point cloud lewat segmentasi latar depan dan regresi bin-based, lalu menyempurnakannya dalam koordinat kanonik pada tahap kedua, mencapai 75,76% AP 3D (tingkat sedang) untuk kelas mobil pada KITTI test set menggunakan LiDAR saja." Angka AP (85,94/75,76/68,32 untuk PointRCNN; 83,13/73,66/66,20 untuk SECOND; 81,94/71,88/66,38 untuk AVOD-FPN; 81,20/70,39/62,19 untuk F-PointNet), angka *recall* proposal (96,01% versus 91% AVOD dengan 50 proposal), dan hasil ablasi (77,67% versus 13,68% tanpa transformasi kanonik; +2,71 poin dari fitur tahap 1) diperoleh dari penelusuran isi naskah lewat perangkat pengambil web, bukan dari pembacaan langsung berkas PDF/HTML asli — **wajib diverifikasi ulang terhadap tabel dan teks naskah CVPR 2019 sebelum dikutip dalam karya formal**. Angka FPS/kecepatan inferensi tidak ditemukan pada sumber yang diperiksa dan tidak dicantumkan dalam narasi di atas.
