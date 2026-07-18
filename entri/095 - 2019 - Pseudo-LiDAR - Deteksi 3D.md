# 095 - Pseudo-LiDAR from Visual Depth Estimation: Bridging the Gap in 3D Object Detection for Autonomous Driving

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2019pseudolidar` |
| Judul asli | Pseudo-LiDAR from Visual Depth Estimation: Bridging the Gap in 3D Object Detection for Autonomous Driving |
| Penulis | Yan Wang, Wei-Lun Chao, Divyansh Garg, Bharath Hariharan, Mark Campbell, Kilian Q. Weinberger |
| Tahun | 2019 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2019) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv:** https://arxiv.org/abs/1812.07179
- **Google Scholar:** https://scholar.google.com/scholar?q=Pseudo-LiDAR%20from%20Visual%20Depth%20Estimation%3A%20Bridging%20the%20Gap%20in%203D%20Object%20Detection%20for%20Autonomous%20Driving
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Pseudo-LiDAR%20from%20Visual%20Depth%20Estimation%3A%20Bridging%20the%20Gap%20in%203D%20Object%20Detection%20for%20Autonomous%20Driving&sort=relevance

## Gambaran Umum

Makalah ini menunjukkan bahwa kesenjangan akurasi antara deteksi objek 3D berbasis kamera dan berbasis *LiDAR* (sensor laser penghasil titik-titik jarak, atau *point cloud*) bukan disebabkan oleh kualitas estimasi kedalaman (*depth*) dari kamera, melainkan oleh cara data itu direpresentasikan sebelum masuk ke detektor. Estimasi *depth* dari kamera stereo maupun monokuler sudah cukup akurat untuk banyak keperluan, tetapi hasilnya biasanya disimpan sebagai peta kedalaman (*depth map*): satu nilai jarak per piksel, disusun dalam grid dua dimensi yang sejajar dengan bidang citra. Penulis menunjukkan bahwa memberi masukan peta kedalaman ini ke jaringan konvolusi 2D, sebagaimana lazim dilakukan detektor 3D berbasis kamera, adalah representasi yang buruk untuk tugas geometri 3D.

Solusi yang diajukan disebut *pseudo-LiDAR*: peta kedalaman diubah menjadi *point cloud* tiga dimensi melalui proyeksi balik (*back-projection*) memakai parameter kalibrasi kamera, sehingga data berbentuk kumpulan titik dalam ruang 3D — persis format yang dihasilkan sensor *LiDAR* sungguhan. *Point cloud* buatan ini kemudian diproses oleh detektor 3D berbasis *LiDAR* yang sudah ada, seperti *Frustum PointNets* dan *AVOD* (dibahas pada bab 090 dan bab 092), tanpa mengubah arsitektur detektor itu sendiri. Pada tolok ukur KITTI, pengubahan representasi ini menghasilkan lonjakan akurasi deteksi 3D berbasis kamera yang jauh melampaui metode sebelumnya yang bekerja langsung pada peta kedalaman, dan pada saat publikasi menempati posisi teratas papan peringkat KITTI untuk metode berbasis citra stereo.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek 3D untuk kendaraan otonom membutuhkan kotak pembatas berorientasi dalam ruang tiga dimensi (posisi x, y, z, panjang, lebar, tinggi, dan sudut hadap), bukan sekadar kotak 2D pada citra. Sensor *LiDAR* memberikan pengukuran jarak langsung dan akurat dalam bentuk *point cloud* jarang (*sparse*), dan detektor yang bekerja di atasnya — seperti VoxelNet (bab 087) yang mendiskretkan *point cloud* menjadi voksel, atau PointNet-based *Frustum PointNets* yang memproses titik secara langsung — mencapai akurasi tinggi. Sebaliknya, metode yang hanya memakai kamera tertinggal jauh, meski kamera jauh lebih murah daripada *LiDAR* dan tersedia luas pada kendaraan produksi.

Sebelum makalah ini, kesenjangan tersebut umum diasumsikan berasal dari kualitas estimasi *depth* kamera yang dianggap kurang akurat dibandingkan pengukuran langsung *LiDAR*. Pendekatan perbaikan yang lazim adalah memperbaiki jaringan estimasi *depth* itu sendiri, sambil tetap memberi peta kedalaman sebagai masukan langsung ke detektor 2D-style yang memproses citra RGB ditambah kanal *depth* (RGB-D) melalui konvolusi 2D biasa. Masalahnya, konvolusi 2D pada peta kedalaman menerapkan filter yang sama pada piksel-piksel bertetangga di bidang citra, padahal piksel yang bertetangga secara spasial pada citra bisa saja sangat jauh berbeda jaraknya di dunia nyata — misalnya piksel tepi sebuah mobil dan piksel latar belakang di baliknya. Filter konvolusi yang mencampur informasi dari piksel-piksel dengan jarak sangat berbeda ini mengaburkan batas objek dalam ruang 3D, sesuatu yang tidak terjadi pada *point cloud* karena titik-titik di dalamnya sudah tersebar sesuai posisi 3D sebenarnya.

## Ide Utama

Gagasan inti makalah ini adalah memisahkan dua hal yang selama ini digabung: kualitas data kedalaman dan format penyimpanannya. Penulis membuktikan lewat percobaan bahwa data kedalaman yang sama, bila diubah formatnya dari peta kedalaman (grid 2D, dilihat dari sudut pandang kamera atau *front view*) menjadi *point cloud* (kumpulan titik dalam koordinat 3D), memberi hasil deteksi yang jauh lebih baik walau tidak ada informasi baru yang ditambahkan — hanya representasi yang berubah.

Mekanismenya adalah proyeksi balik geometris murni, tanpa jaringan saraf tambahan. Untuk setiap piksel (u, v) pada peta kedalaman dengan nilai kedalaman d, posisi 3D-nya dihitung dengan rumus kamera lubang jarum (*pinhole camera*): koordinat x dan y dunia nyata diperoleh dari (u, v) dikurangi titik pusat optik kamera, dikalikan d, dan dibagi panjang fokus kamera; koordinat z sama dengan d itu sendiri. Karena rumus ini memakai parameter kalibrasi kamera yang sudah diketahui, setiap peta kedalaman berukuran H×W piksel dapat diubah langsung menjadi *point cloud* berisi hingga H×W titik, tanpa pelatihan tambahan. Titik-titik hasil proyeksi ini kemudian diberi label "pseudo-LiDAR" karena secara format identik dengan keluaran sensor *LiDAR* asli, sehingga dapat langsung disalurkan ke detektor 3D yang sebelumnya dirancang khusus untuk data *LiDAR*.

## Cara Kerja Langkah demi Langkah

### Estimasi Kedalaman

Tahap pertama menghasilkan peta kedalaman dari citra kamera. Untuk kasus stereo (dua kamera dengan jarak dasar/*baseline* diketahui), makalah memakai jaringan pencocokan stereo PSMNet (*Pyramid Stereo Matching Network*), yang telah dilatih pada kumpulan data sintetis Scene Flow lalu disetel halus (*fine-tuning*) pada KITTI. PSMNet menghasilkan peta disparitas (selisih posisi piksel yang sama antara citra kiri dan kanan), yang kemudian dikonversi menjadi peta kedalaman memakai rumus disparitas-ke-jarak standar stereo: jarak berbanding terbalik dengan disparitas, dikalikan hasil kali panjang fokus dan *baseline*. Makalah juga menguji jalur monokuler, memakai jaringan estimasi *depth* dari citra tunggal yang sudah tersedia, meski akurasi kedalaman monokuler pada dasarnya lebih rendah daripada stereo karena tidak ada informasi paralaks (pergeseran posisi antar dua sudut pandang) untuk dijadikan acuan geometris.

### Proyeksi Balik menjadi Point Cloud

Setiap piksel peta kedalaman diproyeksikan ke koordinat 3D memakai kalibrasi kamera, sebagaimana dijelaskan pada bagian Ide Utama. Hasilnya adalah *point cloud* padat (satu titik untuk hampir setiap piksel bertekstur), berbeda dari *point cloud LiDAR* asli yang jarang (*sparse*) dan tersebar mengikuti pola pemindaian berkas laser berbentuk garis melingkar. Untuk menjaga kompatibilitas dengan detektor *LiDAR* yang sudah ada, makalah kadang menerapkan *sparsification* (pengurangan kepadatan titik) agar pola *pseudo-LiDAR* menyerupai pola sensor *LiDAR* target secara lebih dekat.

### Deteksi 3D dengan Backbone LiDAR yang Ada

*Point cloud pseudo-LiDAR* ini diberikan sebagai masukan ke detektor 3D berbasis *LiDAR* tanpa modifikasi arsitektur: *Frustum PointNets* (memakai deteksi 2D pada citra RGB untuk membatasi wilayah pencarian berbentuk piramida terpancung/*frustum*, lalu memproses titik di dalamnya dengan PointNet) dan *AVOD* (menggabungkan tampak-atas/*bird's-eye view* dari *point cloud* dengan citra RGB melalui dua cabang jaringan region proposal). Karena kedua detektor ini semula dirancang untuk data *LiDAR* asli, tidak ada pelatihan ulang arsitektur yang diperlukan selain menyesuaikan data latih dengan format *pseudo-LiDAR*.

Diagram berikut merangkum perbedaan alur data antara pendekatan konvolusi pada peta kedalaman (kiri) dan alur *pseudo-LiDAR* (kanan):

```
Peta kedalaman -> konvolusi 2D          Peta kedalaman -> point cloud 3D
(front-view, grid u,v)                  (proyeksi balik memakai kalibrasi)
                                                    |
   filter 2D menyamaratakan                         v
   piksel bertetangga di layar,          detektor berbasis LiDAR
   walau jaraknya jauh berbeda           (Frustum PointNets / AVOD)
   di dunia nyata                                   |
        |                                            v
        v                                  kotak 3D lebih akurat
   kotak 3D kurang akurat
```

Diagram ini menunjukkan bahwa perbedaan hasil kedua jalur bukan berasal dari data kedalaman yang berbeda kualitasnya, melainkan dari representasi geometris yang dipakai sebelum data itu diproses.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada tolok ukur KITTI untuk deteksi objek 3D pada kelas mobil, membandingkan detektor yang memakai *pseudo-LiDAR* (dari *depth* stereo maupun monokuler) dengan detektor berbasis kamera sebelumnya yang bekerja langsung pada peta kedalaman atau RGB-D. Metrik yang dipakai adalah *Average Precision* (AP) 3D pada berbagai tingkat kesulitan (mudah, sedang, sulit, mengikuti definisi ukuran dan tingkat oklusi objek pada KITTI).

Hasil kunci: penggunaan *pseudo-LiDAR* bersama *Frustum PointNets* atau *AVOD* menghasilkan peningkatan AP 3D yang besar dibandingkan metode berbasis peta kedalaman langsung pada jarak deteksi yang sama, dengan selisih yang oleh sejumlah rujukan sekunder digambarkan sebagai lompatan dari sekitar 22% menjadi sekitar 74% untuk deteksi objek dalam jarak 30 meter — angka ini perlu dikonfirmasi ke tabel asli sebelum dikutip formal karena konteks pastinya (kelas kesulitan dan ambang IoU yang dipakai) belum terverifikasi langsung dari naskah. Pada saat publikasi, kombinasi *pseudo-LiDAR* dengan detektor berbasis stereo ini menempati posisi teratas papan peringkat KITTI untuk kategori metode berbasis citra stereo, mengungguli seluruh pendekatan berbasis peta kedalaman/RGB-D yang ada sebelumnya.

Studi ablasi pada makalah membandingkan representasi (peta kedalaman versus *point cloud*) dengan data kedalaman yang identik, dan menunjukkan bahwa perubahan representasi saja — tanpa perubahan kualitas data — menyumbang sebagian besar peningkatan akurasi. Temuan ini mengonfirmasi hipotesis utama makalah: representasi, bukan sekadar kualitas estimasi *depth*, adalah faktor penentu kesenjangan akurasi kamera-versus-*LiDAR*. Detail angka AP per kelas kesulitan dan per ambang IoU pada tabel lengkap makalah belum diverifikasi langsung pada naskah primer dalam penulisan bab ini dan perlu dicek ulang sebelum dipakai sebagai kutipan angka pasti.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah kesederhanaan dan keberdampakannya: perbaikan diperoleh murni dari transformasi geometris (proyeksi balik), tanpa memerlukan arsitektur jaringan baru maupun pelatihan ulang detektor 3D dari nol. Pendekatan ini juga bersifat *plug-and-play* terhadap detektor *LiDAR* yang sudah matang, sehingga kemajuan riset pada detektor berbasis *point cloud* (seperti yang dibahas pada bab 087–093) langsung dapat dimanfaatkan untuk deteksi berbasis kamera. Wawasan bahwa representasi data, bukan hanya kualitas sensor, menentukan performa deteksi, memengaruhi banyak karya deteksi 3D kamera sesudahnya.

Dari sisi rekayasa, keterbatasan pertama adalah bahwa akurasi *pseudo-LiDAR* tetap bergantung penuh pada kualitas jaringan estimasi *depth* yang dipakai di hulu; galat estimasi *depth* — yang secara sistematis membesar untuk objek jauh pada metode stereo karena hubungan kedalaman-disparitas bersifat tak-linear (galat disparitas kecil menghasilkan galat jarak yang membesar secara kuadratik seiring jarak) — ikut merambat ke posisi titik dalam *point cloud* buatan. Konsekuensinya, keunggulan *pseudo-LiDAR* lebih menonjol pada objek dekat (dalam radius puluhan meter) dan menyempit pada objek jauh. Kedua, secara konseptual *point cloud* hasil proyeksi balik tetap berbeda dari *point cloud LiDAR* sungguhan: kepadatan titik pada *pseudo-LiDAR* mengikuti resolusi piksel citra (padat dan seragam), sedangkan *LiDAR* asli memiliki pola pemindaian bercincin yang jarang dan noise pengukuran yang berbeda karakteristiknya. Ketiga, karena metode ini bergantung pada detektor *LiDAR* yang sudah ada tanpa penyesuaian arsitektur, ia tidak secara eksplisit menangani derau spesifik yang muncul akibat proses konversi geometris, keterbatasan yang kemudian menjadi sasaran perbaikan langsung pada makalah lanjutannya, Pseudo-LiDAR++ (bab 096).

## Kaitan dengan Bab Lain

Bab ini bergantung langsung pada detektor *LiDAR* yang dibahas pada bab lain sebagai komponen hilir: *Frustum PointNets* (bab [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)) dan *AVOD* (bab [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)) dipakai tanpa modifikasi arsitektur sebagai penerima masukan *pseudo-LiDAR*. Wawasan representasi yang diajukan di sini langsung disempurnakan pada bab [096 - 2020 - Pseudo-LiDAR++ - Deteksi 3D](./096%20-%202020%20-%20Pseudo-LiDAR%2B%2B%20-%20Deteksi%203D.md), yang memperbaiki keterbatasan galat jarak-jauh lewat perbaikan jaringan *depth* dan koreksi titik dekat sensor. Secara lebih luas, bab ini menjadi jembatan konseptual antara klaster estimasi *depth* berbasis kamera dan klaster deteksi 3D berbasis *point cloud* yang dibuka oleh VoxelNet (bab 087) dan PointPillars (bab 088), karena membuktikan detektor pada klaster kedua dapat dipakai kembali untuk data yang berasal dari kamera semata.

## Poin untuk Sitasi

Kutip dengan kunci `wang2019pseudolidar`. Ringkasan yang aman dikutip: "Pseudo-LiDAR mengubah peta kedalaman dari kamera stereo/monokuler menjadi *point cloud* 3D lewat proyeksi balik geometris, sehingga detektor 3D berbasis *LiDAR* yang sudah ada (*Frustum PointNets*, *AVOD*) dapat dipakai langsung pada data kamera, menghasilkan lompatan akurasi deteksi 3D berbasis kamera pada KITTI dan menempati posisi teratas papan peringkat stereo KITTI saat publikasi (CVPR 2019)." Klaim spesifik yang belum terverifikasi langsung dari tabel naskah dan wajib dicek ulang sebelum sitasi formal: angka peningkatan AP dari sekitar 22% menjadi sekitar 74% untuk objek dalam jarak 30 meter (termasuk kelas kesulitan dan ambang IoU yang tepat), rincian AP per kelas kesulitan pada tabel utama, serta nama pasti jaringan estimasi *depth* monokuler yang dipakai pada eksperimen monokuler.
