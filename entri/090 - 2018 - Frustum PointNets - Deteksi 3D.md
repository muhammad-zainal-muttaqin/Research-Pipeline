# 090 - Frustum PointNets for 3D Object Detection from RGB-D Data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qi2018frustum` |
| Judul asli | Frustum PointNets for 3D Object Detection from RGB-D Data |
| Penulis | Charles R. Qi, Wei Liu, Chenxia Wu, Hao Su, Leonidas J. Guibas |
| Tahun | 2018 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2018) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1711.08488
- **Halaman proyek (kode & data):** http://stanford.edu/~rqi/frustum-pointnets/
- **Kode sumber resmi:** https://github.com/charlesq34/frustum-pointnets
- **Google Scholar:** https://scholar.google.com/scholar?q=Frustum%20PointNets%20for%203D%20Object%20Detection%20from%20RGB-D%20Data

## Gambaran Umum

Makalah ini memperkenalkan Frustum PointNets, metode deteksi objek tiga dimensi (3D) yang memadukan citra RGB dengan data kedalaman (*depth*) berbentuk *point cloud* (kumpulan titik koordinat 3D hasil pengukuran sensor jarak, misalnya LiDAR atau kamera *depth*). Alih-alih mencari objek di seluruh ruang 3D yang mahal secara komputasi, metode ini memakai detektor 2D matang pada citra RGB untuk mempersempit pencarian menjadi sebuah *frustum* (volume berbentuk piramida terpotong) yang diproyeksikan dari kotak deteksi 2D ke ruang 3D. Di dalam *frustum* itu, jaringan PointNet — arsitektur yang memproses *point cloud* langsung tanpa mengubahnya menjadi grid atau voxel — mensegmentasi titik milik objek dan meregresi kotak 3D berorientasi (memiliki sudut hadap/*yaw*, bukan sekadar sejajar sumbu).

Pada tolok ukur KITTI (deteksi objek luar ruang untuk kendaraan otonom), Frustum PointNets mencapai *average precision* (AP) 3D sebesar 81,20% untuk kategori mobil pada subset "mudah", mengungguli metode dua-tahap berbasis proyeksi sebelumnya dengan margin besar. Pada SUN RGB-D (tolok ukur dalam ruang), metode ini mencapai mAP (*mean average precision*, rata-rata presisi di seluruh kelas) sebesar 54,0% pada ambang *intersection over union* (IoU, rasio irisan terhadap gabungan dua kotak) 0,25, sekaligus berjalan jauh lebih cepat daripada pendekatan berbasis pencarian penuh di ruang 3D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, deteksi objek 3D umumnya diselesaikan dengan dua kelompok pendekatan. Kelompok pertama mendiskretisasi seluruh *point cloud* menjadi volume grid 3D (voxel) atau proyeksi tampak-atas (*bird's-eye view*), lalu menjalankan konvolusi pada representasi tersebut, seperti pada MV3D (bab 091), yang memproyeksikan LiDAR ke beberapa tampilan dan menggabungkannya dengan citra RGB. Pendekatan ini mahal karena sebagian besar ruang 3D kosong — hanya sebagian kecil voxel yang berisi titik objek — sehingga banyak komputasi terbuang pada ruang tanpa isi. Kelompok kedua menjalankan jaringan langsung pada seluruh *point cloud* tanpa panduan citra, sehingga pencarian objek tetap mencakup ruang yang sangat luas.

Masalah mendasar lainnya adalah *point cloud* dari sensor jarak bersifat jarang (*sparse*): pada jarak jauh atau untuk objek kecil, jumlah titik yang jatuh pada permukaan objek bisa sangat sedikit. Metode yang mencari objek langsung di ruang 3D penuh tanpa panduan sulit membedakan sedikit titik itu dari latar belakang. Di sisi lain, pada saat itu detektor 2D pada citra RGB (misalnya Faster R-CNN, bab 014) telah matang dan akurat, memanfaatkan tekstur serta kepadatan informasi citra yang jauh lebih tinggi daripada *point cloud*. Pertanyaan yang mendasari makalah ini adalah bagaimana memanfaatkan kematangan detektor 2D tersebut untuk mempersempit pencarian 3D, alih-alih mengulangi seluruh proses pencarian di ruang tiga dimensi.

## Ide Utama

Gagasan inti Frustum PointNets adalah kaskade dua tahap: deteksi 2D lebih dulu menentukan *di mana* mencari, kemudian jaringan 3D menentukan secara presisi *bentuk dan posisi* objek di dalam wilayah yang telah dipersempit itu. Sebuah kotak deteksi 2D pada citra RGB, jika diproyeksikan kembali ke ruang 3D memakai parameter kalibrasi kamera (hubungan geometris antara koordinat citra dan koordinat dunia nyata), tidak menghasilkan satu titik atau satu kotak, melainkan sebuah *frustum*: piramida terpotong yang memanjang dari kamera ke kedalaman tak terhingga, dibatasi oleh empat sisi kotak 2D tersebut. Semua titik *point cloud* yang jatuh di dalam *frustum* itu adalah kandidat kuat milik objek yang terdeteksi, karena proyeksinya ke citra 2D berada di dalam kotak deteksi.

Dengan mempersempit ruang pencarian dari seluruh adegan menjadi satu *frustum* per deteksi 2D, jaringan PointNet berikutnya hanya perlu menyelesaikan dua tugas yang lebih sederhana: memisahkan titik objek dari titik latar di dalam *frustum* (segmentasi instans), lalu meregresi parameter kotak 3D dari titik-titik yang tersisa. Karena wilayah pencarian sudah kecil, kedua tugas ini dapat dikerjakan cepat dan akurat, sekalipun jumlah titik pada objek tersebut sedikit.

## Cara Kerja Langkah demi Langkah

### Tahap 1: Proposal Frustum dari Detektor 2D

Sebuah detektor 2D berbasis *Feature Pyramid Network* (FPN, jaringan yang menggabungkan peta fitur dari berbagai skala resolusi) dilatih awal pada ImageNet dan COCO, kemudian disetel halus (*fine-tuned*) pada data deteksi 2D KITTI. Detektor ini menghasilkan kotak 2D beserta label kelasnya pada citra RGB. Setiap kotak 2D diangkat menjadi *frustum* 3D memakai parameter kalibrasi kamera, dan seluruh titik *point cloud* yang terproyeksi ke dalam kotak tersebut diekstrak sebagai masukan tahap berikutnya. Karena orientasi *frustum* bergantung pada posisi kotak di citra, setiap *frustum* dirotasi terlebih dahulu ke sistem koordinat pandangan-tengah (*center view*): sumbu pandang diputar sehingga sumbu-z sejajar dengan sumbu tengah *frustum*, mengurangi variasi sudut pandang yang harus dipelajari jaringan berikutnya.

### Tahap 2: Segmentasi Instans 3D dengan PointNet

Titik-titik di dalam *frustum* umumnya masih bercampur antara objek dan latar (tanah, dinding, atau objek lain pada garis pandang yang sama). Sebuah PointNet — jaringan yang memproses tiap titik secara independen lalu menggabungkan fitur global lewat *max pooling* (pengambilan nilai maksimum antar-titik) — melakukan klasifikasi biner per titik: objek atau bukan. Informasi kelas dari detektor 2D disertakan sebagai vektor *one-hot* (representasi biner bernilai 1 pada posisi kelas yang benar, 0 di posisi lain) yang digabungkan dengan fitur titik, sehingga jaringan segmentasi mengetahui jenis objek yang dicari sebelum memisahkannya dari latar.

### Tahap 3: Estimasi Pusat dengan T-Net

Titik yang telah disegmentasi sebagai objek biasanya tidak berpusat tepat pada pusat geometris objek sesungguhnya, karena sensor hanya menangkap permukaan yang terlihat — bagian objek yang terhalang tidak memiliki titik sama sekali. T-Net, sebuah PointNet regresi berukuran ringan, mengestimasi pergeseran dari pusat massa titik yang teramati menuju pusat objek sesungguhnya, lalu koordinat titik digeser sehingga pusat objek menjadi titik asal (origin) sistem koordinat lokal. Langkah ini disebut estimasi *amodal* karena kotak akhir mencakup bagian objek yang tidak teramati langsung oleh sensor.

### Tahap 4: Estimasi Kotak 3D Berorientasi

PointNet ketiga menerima titik yang sudah dipusatkan dan meregresi parameter kotak: pusat (residu kecil terhadap hasil T-Net), ukuran (tinggi, lebar, panjang), dan sudut hadap (*heading angle*). Ukuran dan sudut diprediksi dengan skema hibrida klasifikasi-lalu-regresi: beberapa templat ukuran dan beberapa bin sudut dipilih lewat klasifikasi, kemudian residu halus terhadap pilihan itu diregresi terpisah — lebih stabil daripada meregresi nilai kontinu secara langsung karena jaringan cukup memilih kategori terdekat lalu menghaluskannya.

Pelatihan memakai fungsi *loss* gabungan: *loss* segmentasi titik, *loss* regresi pusat dari T-Net, *loss* klasifikasi-regresi ukuran, *loss* klasifikasi-regresi sudut, ditambah *corner loss* — suku tambahan yang meminimalkan jarak antara delapan sudut kotak prediksi dan delapan sudut kotak kebenaran (*ground truth*), sehingga kesalahan pusat, ukuran, dan sudut sama-sama tercermin pada posisi sudut kotak akhir.

Alur data dari citra hingga kotak 3D dapat diringkas sebagai berikut:

```
citra RGB --[detektor 2D FPN]--> kotak 2D + kelas
                                     |
                        (proyeksi via kalibrasi kamera)
                                     v
point cloud --------------------> frustum 3D (dirotasi ke center view)
                                     |
                         PointNet segmentasi instans
                        (titik objek vs titik latar)
                                     v
                    titik objek --> T-Net (estimasi pusat)
                                     v
                    titik terpusatkan --> PointNet estimasi box
                                     v
                    kotak 3D: pusat, ukuran (h,w,l), sudut hadap
```

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dua tolok ukur dengan karakteristik sensor berbeda. KITTI adalah tolok ukur luar ruang untuk kendaraan otonom, dengan *point cloud* dari LiDAR berputar dan citra dari kamera stereo/mono; metriknya AP 3D pada tiga tingkat kesulitan (mudah, sedang, sulit) berdasarkan tingkat oklusi dan ukuran objek. SUN RGB-D adalah tolok ukur dalam ruang dengan kedalaman dari kamera RGB-D jarak dekat; metriknya mAP pada ambang IoU 0,25.

Pada KITTI *test set*, AP 3D untuk kategori mobil mencapai 81,20% (mudah), 70,39% (sedang), dan 62,19% (sulit); untuk pejalan kaki 51,21%/44,89%/40,23%; untuk pesepeda 71,96%/56,77%/50,39%. Menurut makalah, hasil ini mengungguli metode pembanding sebelumnya (termasuk MV3D) pada seluruh kategori dan subset, dengan selisih AP mobil sekitar delapan poin persentase di atas metode terbaik sebelumnya. Pola angka ini logis: mobil berbentuk kaku dan berukuran relatif besar sehingga titik permukaannya lebih padat, sedangkan pejalan kaki bertubuh tipis dan tidak kaku sehingga AP-nya jauh lebih rendah pada seluruh metode, termasuk Frustum PointNets.

Pada SUN RGB-D, mAP keseluruhan mencapai 54,0%, sekitar 6-9 poin persentase di atas metode pembanding. Kecepatan inferensi berkisar 5 *frame* per detik untuk keseluruhan pipa (deteksi 2D ditambah tiga tahap PointNet), dengan bagian 3D saja berjalan sekitar 88 milidetik pada varian dasar (v1) dan 167 milidetik pada varian lebih besar (v2). Dibandingkan metode pencarian penuh di ruang 3D pada SUN RGB-D saat itu, makalah melaporkan percepatan sampai orde 10 hingga 1.000 kali — bukti bahwa mempersempit pencarian lewat *frustum* memberi keuntungan kecepatan jauh lebih besar daripada peningkatan akurasi itu sendiri.

## Kelebihan dan Keterbatasan

Kelebihan utama metode ini adalah efisiensi: dengan menyerahkan pencarian kasar kepada detektor 2D matang, jaringan 3D hanya memproses titik dalam wilayah sempit, sehingga akurasi tinggi dan kecepatan *near real-time* tercapai sekaligus. Estimasi kotak bersifat *amodal* sehingga kotak akhir tetap masuk akal meski sebagian objek terhalang atau titiknya sangat jarang.

Penulis sendiri mengakui beberapa keterbatasan. Segmentasi PointNet dapat menghasilkan hasil bercampur bila lebih dari satu instans objek berada dalam *frustum* yang sama, karena arsitektur mengasumsikan satu objek dominan per *frustum*. Ketergantungan pada detektor 2D bersifat mutlak: bila detektor 2D gagal mendeteksi suatu objek, tidak ada *frustum* yang diusulkan sehingga objek itu tidak akan pernah terdeteksi di 3D, betapapun jelas titik *point cloud*-nya. Titik yang sangat jarang (kurang dari lima titik) juga menyulitkan segmentasi maupun regresi kotak. Dari sisi rekayasa, arsitektur dua tahap ini bukan sistem *end-to-end* penuh: kesalahan detektor 2D merambat langsung ke tahap 3D tanpa mekanisme koreksi balik. Kualitas anotasi turut memengaruhi hasil: akurasi segmentasi kebenaran (*ground truth*) otomatis pada SUN RGB-D hanya 82,7% dibandingkan sekitar 90% pada KITTI, akibat oklusi berat dan penataan objek yang lebih rapat pada adegan dalam ruang.

## Kaitan dengan Bab Lain

Frustum PointNets berada pada silsilah yang sama dengan MV3D (bab 091), yang menjadi salah satu *baseline* pembandingnya: keduanya memadukan RGB dan LiDAR, tetapi MV3D memproyeksikan *point cloud* ke beberapa tampilan grid, sedangkan Frustum PointNets memakai *frustum* sebagai penyaring wilayah dan PointNet sebagai pemroses titik langsung. Ketergantungan pada detektor 2D matang menautkannya ke garis keluarga deteksi 2D pada [014 - 2017 - Faster R-CNN - Fondasi RGB](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md), rujukan arsitektur detektor tahap pertama pada makalah ini.

Di dalam klaster Deteksi 3D, bab ini berdampingan dengan pendekatan yang memproses *point cloud* langsung tanpa proyeksi kaskade, seperti [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md), serta pendekatan berbasis voxelisasi seperti [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md). Gagasan mempersempit pencarian 3D memakai isyarat RGB diwarisi dan diperluas oleh metode fusi yang lebih erat, seperti [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md), yang mewarnai titik LiDAR dengan skor semantik dari segmentasi citra, dan [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md), yang menggabungkan fitur kamera dan LiDAR pada tingkat fitur, bukan tingkat kaskade keputusan.

## Poin untuk Sitasi

Kutip dengan kunci `qi2018frustum`. Ringkasan yang aman dikutip: "Frustum PointNets memproyeksikan kotak deteksi 2D pada citra RGB menjadi *frustum* 3D, lalu memakai rangkaian PointNet untuk mensegmentasi dan meregresi kotak 3D berorientasi di dalamnya, mencapai AP 3D 81,20% (mobil, subset mudah) pada KITTI dan mAP 54,0% pada SUN RGB-D." Angka AP KITTI (81,20/70,39/62,19 untuk mobil; nilai pejalan kaki dan pesepeda) serta mAP SUN RGB-D 54,0% diperoleh dari pembacaan naskah ar5iv dan sebaiknya dicocokkan sekali lagi dengan tabel PDF resmi CVPR sebelum dikutip dalam karya formal. Angka kecepatan (5 FPS pipa penuh; 88 ms dan 167 ms untuk varian v1/v2) juga berasal dari sumber sekunder yang merujuk naskah dan disarankan diverifikasi ke Tabel eksperimen asli, karena kedua angka tersebut tidak sepenuhnya konsisten secara aritmetik satu sama lain.
