# 112 - Expandable YOLO: 3D Object Detection from RGB-D Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `takahashi2020expandableyolo` |
| Judul asli | Expandable YOLO: 3D Object Detection from RGB-D Images |
| Penulis | Masahiro Takahashi, Alessandro Moro, Yonghoon Ji, Kazunori Umeda |
| Tahun | 2020 |
| Venue | 21st International Conference on Research and Education in Mechatronics (REM 2020) |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2006.14837
- **Google Scholar:** https://scholar.google.com/scholar?q=Expandable%20YOLO%3A%203D%20Object%20Detection%20from%20RGB-D%20Images
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Expandable%20YOLO%3A%203D%20Object%20Detection%20from%20RGB-D%20Images&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Expandable YOLO (E-YOLO), perluasan arsitektur YOLOv3 (bab 003) yang menerima masukan RGB-D (citra warna ditambah citra kedalaman) dan mengeluarkan kotak pembatas tiga dimensi, bukan kotak dua dimensi seperti YOLO standar. Gagasan utamanya adalah menambahkan satu kanal kedalaman pada masukan jaringan dan memperluas bagian akhir jaringan dengan lapis konvolusi 3D, sehingga keluarannya berbentuk tensor 3D berisi parameter kotak ruang. Pendekatan ini berbeda dari detektor 3D berbasis titik awan (*point cloud*) seperti VoxelNet atau YOLO3D, yang memakai data LiDAR dan konvolusi 3D penuh sehingga jaringannya besar dan lambat.

Model diuji pada kumpulan data indoor buatan sendiri yang direkam dengan kamera stereo Intel RealSense D435. Hasilnya, E-YOLO mengeluarkan kotak 3D langsung dari citra RGB-D pada kecepatan 44,4 *frame* per detik (FPS), memisahkan dua orang berdekatan yang oleh YOLOv3 murni 2D justru digabung menjadi satu deteksi, serta mendeteksi orang berpakaian gelap yang terlewat oleh YOLOv3. Akurasi kotak 2D-nya sedikit menurun dibanding YOLOv3 baku karena arsitektur ini melepas struktur *Feature Pyramid Network* (FPN) demi menekan biaya komputasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sampai tahun 2020, dua pendekatan besar mendominasi deteksi objek. Pendekatan berbasis wilayah seperti R-CNN, Fast R-CNN, dan Mask R-CNN memiliki akurasi tinggi tetapi menjalankan jaringan konvolusi terpisah untuk tiap kandidat objek, sehingga biaya komputasinya besar. Pendekatan satu tahap seperti SSD (*Single Shot MultiBox Detector*) dan keluarga YOLO lebih cepat, tetapi YOLO versi awal (bab 001, bab 002) kesulitan mendeteksi objek yang berdekatan pada titik jangkar (*anchor*) yang sama — masalah yang dalam makalah ini disebut *object merging*, dua objek berdekatan yang justru dikeluarkan sebagai satu deteksi tunggal.

Selain itu, aplikasi yang membutuhkan posisi tiga dimensi — penghitungan orang, kendaraan otonom, robotika — tidak cukup dilayani deteksi 2D; sistem perlu mengetahui jarak (kedalaman) objek terhadap kamera untuk menangani situasi objek saling menutupi (*occlusion*). Detektor 3D yang ada saat itu, seperti VoxelNet dan Complex-YOLO, menyelesaikan masalah ini dengan memproses titik awan dari sensor LiDAR memakai konvolusi 3D penuh. Pendekatan ini memiliki tiga kekurangan sekaligus: jaringannya besar sehingga tidak berjalan *real-time*; masukannya hanya titik awan sehingga informasi warna tidak dimanfaatkan; dan karena deteksinya dilakukan dari sudut pandang mata burung (*bird's-eye view*), hasilnya perlu dipadukan lagi dengan citra subjektif secara terpisah. Sensor LiDAR yang dibutuhkan pun jauh lebih mahal daripada kamera stereo biasa. Makalah ini mengganti kombinasi mahal tersebut dengan kamera RGB-D biasa dan jaringan yang tetap ringan.

## Ide Utama

Gagasan intinya sederhana: alih-alih memproses titik awan dengan konvolusi 3D penuh, E-YOLO menambahkan kedalaman sebagai kanal keempat pada citra masukan — bersama tiga kanal merah, hijau, biru (RGB) — sehingga masukan jaringan tetap berupa satu citra, hanya dengan empat kanal alih-alih tiga. Karena masukan tetap berbentuk citra 2D biasa, fitur dari warna dan kedalaman dapat diekstraksi bersama-sama memakai tulang punggung (*backbone*) konvolusi 2D yang sama dipakai YOLOv3, yaitu Darknet-53, tanpa memerlukan konvolusi 3D pada seluruh jaringan.

Konvolusi 3D hanya ditambahkan pada bagian akhir jaringan, tepat sebelum keluaran, untuk mengubah fitur 2D menjadi tensor 3D yang memuat parameter kotak pembatas dalam ruang (posisi x, y, z serta ukuran lebar, tinggi, kedalaman). Dengan menunda pemakaian konvolusi 3D hanya pada bagian kecil di ujung jaringan, jumlah lapis 3D yang mahal secara komputasi ditekan seminimal mungkin, sehingga kecepatan proses tetap mendekati detektor 2D biasa.

## Cara Kerja Langkah demi Langkah

### Masukan RGB-D dan Tulang Punggung Darknet-53

Citra masukan berukuran 416×416 piksel dengan 4 kanal: R, G, B, dan D (kedalaman), dinormalisasi ke rentang 10 meter sebelum digabung sebagai kanal keempat. Citra 4-kanal ini diproses oleh Darknet-53, tulang punggung konvolusi 2D yang sama dipakai YOLOv3, terdiri atas lapis-lapis konvolusi 3×3 dan 1×1 dengan koneksi sisa (*residual*) bergaya ResNet. Darknet-53 dipilih karena pada YOLOv3 terbukti unggul dalam akurasi dan kecepatan ekstraksi fitur dibanding ResNet biasa; penulis berasumsi ekstraksi fitur dari citra kedalaman dapat dilakukan dengan cara sama seperti citra warna karena keduanya sama-sama peta piksel 2D.

Mengikuti pola FPN (*Feature Pyramid Network*, arsitektur yang menggabungkan fitur dari beberapa skala resolusi agar objek besar dan kecil sama-sama terdeteksi) yang dipakai YOLOv3, E-YOLO mengambil dua keluaran skala dari Darknet-53: lapis ke-43 berukuran 512 kanal pada resolusi 26×26, dan lapis ke-52 berukuran 1024 kanal pada resolusi 13×13. Berbeda dari YOLOv3 yang memakai tiga skala keluaran, E-YOLO hanya memakai skala menengah ini untuk menekan biaya komputasi.

### Perluasan ke Konvolusi 3D dan Bentuk Keluaran

Keluaran resolusi 13×13 diperbesar dua kali (*upsampling*) menjadi 26×26, lalu digabungkan (*concatenate*, menumpuk dua tensor pada sumbu kanal) dengan keluaran lapis ke-43, menghasilkan tensor 1144 kanal pada resolusi 26×26. Tensor ini kemudian disusun ulang bentuknya (*reshape*): 1144 kanal pada bidang 26×26 diubah menjadi tensor 44×26×26×26 — konsisten karena 44 × 26 = 1144. Perubahan bentuk inilah yang mengubah representasi dari bidang 2D menjadi kubus 3D, sehingga lapis-lapis konvolusi berikutnya (kombinasi kernel 1×1×1 dan 3×3×3) dapat memproses fitur sebagai volume tiga dimensi, bukan lagi bidang datar.

Tensor 44×26×26×26 diproses lebih lanjut oleh tumpukan lapis Conv3D hingga menghasilkan tensor keluaran akhir berukuran 10×26×26×26: grid kubus 26×26×26 sel, setiap sel memuat 10 nilai. Delapan nilai pertama menyusun kotak 3D — *confidence* (keyakinan ada objek), satu nilai pendamping yang dalam naskah disebut nilai *unreliable*, tiga koordinat pusat kotak (x, y, z), dan tiga ukuran kotak (lebar, tinggi, kedalaman). Dua nilai sisanya adalah probabilitas kelas, dibatasi menjadi dua kategori sesuai data latih: orang dan objek non-orang. YOLOv3 memakai tiga kandidat kotak per sel pada tiap skala; E-YOLO menekannya menjadi satu saja (B = 1) karena konvolusi 3D jauh lebih mahal daripada konvolusi 2D.

Diagram berikut meringkas alur data dari citra RGB-D masukan hingga tensor kotak 3D:

```
RGB-D 416x416x4
      |
      v  Darknet-53 (backbone 2D, sama dgn YOLOv3)
lapis-43: 512ch, 26x26      lapis-52: 1024ch, 13x13
      |                            |
      |                    upsampling 2x -> 26x26
      +---------- concatenate -----+
                    |
        conv 1x1 -> 1144 kanal, 26x26
                    |
   reshape 1144x26x26 -> 44 x (26x26x26)
                    |
      tumpukan Conv3D (1x1x1 dan 3x3x3)
                    |
        keluaran: 10 x 26 x 26 x 26
   (8 param kotak 3D: conf, unreliable,
    x, y, z, lebar, tinggi, kedalaman;
    2 kelas: orang / objek non-orang)
```

### Fungsi Loss dan IoU 3D untuk Seleksi Kotak

Pelatihan memakai fungsi *loss* yang diadaptasi dari YOLO3D dengan tambahan galat kuadrat untuk arah kedalaman: galat koordinat pusat (x, y, z), galat ukuran kotak (lebar, tinggi, kedalaman), galat *confidence* pada sel berisi objek, galat *confidence* pada sel tanpa objek, dan galat klasifikasi kelas. Bobot galat koordinat (λ_coord) diset 1, sedangkan bobot galat *confidence* pada sel tanpa objek (λ_noobj) diset 10, menekankan penekanan *false positive* pada sel kosong lebih besar daripada penghalusan posisi kotak.

Kotak akhir dipilih dengan *Non-Maximum Suppression* (NMS): dari kotak-kotak yang saling menutupi objek yang sama, hanya kotak berskor tertinggi yang dipertahankan, diukur lewat IOU (*Intersection over Union*, rasio irisan terhadap gabungan dua kotak). Detektor 3D berbasis titik awan seperti YOLO3D biasanya menghitung IOU dua kali, dari sudut pandang depan dan atas sensor, lalu menggabungkan keduanya — tidak efisien untuk komputasi paralel di GPU. E-YOLO sebagai gantinya mendefinisikan IOU 3D langsung sebagai rasio volume irisan terhadap volume gabungan dua kotak, sehingga NMS cukup menghitung IOU satu kali per pasangan. Ambang IOU untuk NMS berbasis volume ini adalah 0,35, lebih rendah daripada ambang 0,5 yang lazim dipakai pada NMS berbasis IOU 2D di YOLO, R-CNN, maupun SSD.

## Eksperimen dan Hasil

Model dilatih dan diuji pada kumpulan data indoor buatan sendiri, direkam dengan kamera stereo Intel RealSense D435 di sebuah ruangan di kampus Korakuen, Universitas Chuo, dengan skenario orang berjalan di dalam ruangan. Label kotak dibuat otomatis memakai Mask R-CNN (model segmentasi instans, yang memisahkan objek per piksel, bukan hanya per kotak) dan dikoreksi manual untuk hasil berskor keyakinan rendah; label kedalaman diperoleh dengan pengelompokan (*clustering*) titik awan hasil rekonstruksi RGB-D. Total data berjumlah 1.240 adegan: 1.140 data latih dan 100 data validasi — kumpulan data kecil dan terbatas pada satu lingkungan indoor tunggal.

Pelatihan memakai laju belajar 0,001 dengan pengoptimal Adam, berjalan 100 *epoch* (satu putaran penuh atas seluruh data latih) pada GPU RTX 2080. Nilai *loss* minimum yang tercapai adalah 2.337,63 pada data latih dan 7.180,24 pada data validasi; penurunan *loss* latih mencapai kurang dari 1/5.000 nilai awal, dan kurva validasi menunjukkan tren serupa tanpa tanda kuat *overfitting* (model terlalu menyesuaikan diri pada data latih hingga gagal menggeneralisasi ke data baru).

Akurasi kotak diukur dengan skor IOU. Pada data latih, IOU 2D rata-rata E-YOLO adalah 0,54 (maksimum 0,92), sementara IOU 3D rata-rata 0,39 (maksimum 0,85). Makalah menyebut YOLOv3 baku biasanya mencapai IOU 2D sekitar 0,7–0,8 per kelas berdasarkan studi terdahulu; akurasi kotak 2D E-YOLO yang lebih rendah disebabkan tidak dipakainya struktur FPN tiga-skala penuh demi menekan biaya komputasi. Ketika IOU 3D dikonversi memakai pangkat 2/3 (rasio luas berhubungan dengan rasio volume lewat pangkat itu), hasilnya 0,53, mendekati IOU 2D sebesar 0,54 — indikasi bahwa ekstraksi fitur 2D dan 3D pada model ini berlangsung dengan akurasi sebanding.

Secara kualitatif, pada satu adegan berisi dua orang berdekatan, YOLOv3 murni 2D mengeluarkan satu kotak gabungan untuk keduanya (contoh nyata *object merging* yang disebut pada latar belakang), sedangkan E-YOLO mengeluarkan dua kotak terpisah meski ukurannya sedikit lebih besar dari kebenaran lapangan (*ground truth*); E-YOLO juga mendeteksi seseorang berpakaian gelap yang terlewat YOLOv3.

Kecepatan proses diuji terpisah pada GPU GTX 1080 Ti dengan implementasi PyTorch. E-YOLO mencapai 44,4 FPS, dibandingkan YOLOv3 74 FPS (GPU sama), Complex-YOLO 50,4 FPS (Titan X), YOLO3D 40 FPS (Titan X), dan VoxelNet 4,3 FPS (Titan X). E-YOLO memang lebih lambat sekitar 30 FPS dibanding YOLOv3 murni 2D karena tambahan konvolusi 3D dan kanal kedalaman, tetapi jauh lebih cepat daripada VoxelNet yang memproses titik awan dengan konvolusi 3D penuh, dan sebanding dengan detektor 3D berbasis titik awan lain seperti YOLO3D — meski perbandingan lintas GPU (1080 Ti versus Titan X) perlu dibaca hati-hati karena perangkat kerasnya tidak identik.

## Kelebihan dan Keterbatasan

Kelebihan utama E-YOLO terletak pada efisiensinya: dengan memakai citra kedalaman sebagai kanal tambahan pada konvolusi 2D, alih-alih memproses titik awan dengan konvolusi 3D penuh, model tetap ringan namun mampu mengeluarkan kotak 3D dari satu jaringan tunggal, tanpa memadukan pipeline 2D dan kedalaman secara terpisah seperti YOLO3D atau Complex-YOLO. Definisi IOU 3D volumetrik juga menyederhanakan NMS menjadi satu kali komputasi per pasangan kotak. Kemampuan memisahkan objek berdekatan dan mendeteksi objek yang terlewat YOLOv3 murni 2D menjadi bukti konkret manfaat tambahan informasi kedalaman.

Keterbatasan yang diakui penulis mencakup tiga hal: akurasi panjang kotak pada arah kedalaman masih kurang presisi dibanding kebenaran lapangan; IOU 2D menurun dibanding YOLOv3 baku karena tidak memakai struktur FPN penuh; dan Darknet-53 sebagai tulang punggung tidak dioptimalkan untuk fitur RGB-D atau konvolusi 3D, karena aslinya dirancang murni untuk citra RGB.

Dari sisi rekayasa, kumpulan data latih dan validasi berjumlah sangat kecil (1.140 dan 100 adegan) dan seluruhnya direkam pada satu ruangan tunggal, sehingga generalisasi model ke lingkungan lain, pencahayaan berbeda, atau jenis objek di luar orang belum teruji dalam makalah ini. Secara konseptual, jumlah kelas keluaran juga dibatasi hanya dua kategori (orang dan objek non-orang), lebih sempit daripada evaluasi multi-kelas yang lazim dipakai pada tolok ukur deteksi objek arus utama, sehingga sulit dibandingkan langsung dengan detektor 2D yang diuji pada puluhan kelas seperti PASCAL VOC atau COCO.

## Kaitan dengan Bab Lain

E-YOLO membangun langsung di atas formulasi grid dan regresi kotak yang diperkenalkan pertama kali pada [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), dan secara arsitektural memakai ulang tulang punggung Darknet-53 dari [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), termasuk pola FPN dua-skala yang dipangkas dari tiga skala aslinya. Perbedaan mendasarnya terletak pada perluasan kanal masukan dan bagian akhir jaringan menjadi konvolusi 3D, mengikuti kerangka kerja fungsi *loss* dari YOLO3D.

Di dalam klaster YOLO plus RGB-D, cara E-YOLO menggabungkan kanal kedalaman sebagai masukan tambahan pada tahap awal jaringan merupakan salah satu strategi *fusion* konkret yang dibahas lebih sistematis pada [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md), yang membandingkan titik penggabungan kedalaman pada awal, tengah, atau akhir jaringan. Prinsip memanfaatkan kedalaman untuk lokalisasi 3D juga berlanjut pada makalah aplikatif lain di klaster ini yang memakai YOLO dan RGB-D untuk tugas manipulasi robot, seperti [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md).

## Poin untuk Sitasi

Kutip dengan kunci `takahashi2020expandableyolo`. Ringkasan yang aman dikutip: "Expandable YOLO memperluas YOLOv3 dengan menambahkan kanal kedalaman pada masukan dan konvolusi 3D pada bagian akhir jaringan, menghasilkan kotak pembatas 3D dari citra RGB-D pada kecepatan 44,4 FPS, lebih cepat daripada detektor 3D berbasis titik awan seperti VoxelNet." Angka IOU 2D/3D (0,54 dan 0,39), nilai *loss* minimum (2.337,63 dan 7.180,24), serta tabel kecepatan lintas metode (74/50,4/44,4/40/4,3 FPS) berasal dari naskah arXiv 2006.14837 dan sebaiknya diverifikasi ulang terhadap versi final REM 2020 sebelum dikutip dalam karya formal. Definisi pasti nilai kanal "unreliable" pada tensor keluaran tidak dijelaskan rinci dalam naskah dan perlu ditelusuri lebih lanjut bila dipakai untuk reproduksi arsitektur.
