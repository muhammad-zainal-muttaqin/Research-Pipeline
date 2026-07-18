# 125 - A Field-Tested Robotic Harvesting System for Iceberg Lettuce

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `birrell2020lettuce` |
| Judul asli | A Field-Tested Robotic Harvesting System for Iceberg Lettuce |
| Penulis | Birrell, Simon; Hughes, Josie; Cai, Julia Y.; Iida, Fumiya |
| Tahun | 2020 |
| Venue | Journal of Field Robotics |
| Tema | Pertanian |

## Tautan Akses
- Google Scholar: https://scholar.google.com/scholar?q=A%20Field-Tested%20Robotic%20Harvesting%20System%20for%20Iceberg%20Lettuce
- Semantic Scholar: https://www.semanticscholar.org/search?q=A%20Field-Tested%20Robotic%20Harvesting%20System%20for%20Iceberg%20Lettuce&sort=relevance
- DOI: https://doi.org/10.1002/rob.21888
- University of Cambridge Repository: https://doi.org/10.17863/CAM.41315

## Gambaran Umum
Pemanenan selada *iceberg* (*Lactuca sativa*) merupakan aktivitas pertanian padat karya yang sangat bergantung pada tenaga kerja manusia karena karakteristik fisik tanaman yang sensitif terhadap memar dan posisi tumbuhnya yang dekat dengan tanah. Makalah ini memperkenalkan "Vegebot", sebuah sistem robot pemanen selada *iceberg* otonom yang dirancang dan diuji secara langsung di lahan pertanian nyata. Sistem ini memadukan penglihatan komputer dua tahap berbasis pembelajaran mendalam (*deep learning*) dengan sebuah manipulator robotik industri yang dilengkapi dengan *end-effector* khusus untuk mencengkeram dan memotong tanaman secara presisi tanpa merusak jaringan daun.

Secara keseluruhan, Vegebot memisahkan tugas persepsi menjadi dua jaringan syaraf tiruan konvolusional (*convolutional neural network* atau CNN) yang terintegrasi. Jaringan pertama melokalisasi selada pada citra area kerja dari kamera atas (*overhead*), sedangkan jaringan kedua mengklasifikasikan tingkat kematangan dan kesehatan selada tersebut sebelum dilakukan instruksi pemotongan fisik. Diintegrasikan dalam arsitektur modular berbasis *Robot Operating System* (ROS), pengujian lapangan di Cambridge menunjukkan tingkat keberhasilan lokalisasi visual sebesar 91,1% dan tingkat keberhasilan pelepasan fisik sebesar 51,7% dengan rata-rata waktu siklus pemanenan sebesar 31,2 detik per selada.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemanenan selada *iceberg* di sektor pertanian industri menghadapi kendala ketersediaan tenaga kerja dan kenaikan biaya operasional. Meskipun mekanisasi telah banyak diterapkan pada tanaman biji-bijian, selada *iceberg* tetap dipanen secara manual menggunakan tangan manusia. Karakteristik selada *iceberg* sangat rentan mengalami kerusakan mekanis; tekanan cengkeraman yang berlebihan akan menyebabkan daun memar dan menurunkan nilai jual komersialnya. Selain itu, batang selada harus dipotong dengan sangat presisi di dekat permukaan tanah untuk mencegah pembusukan batang namun tidak merusak bagian kepala selada yang bundar.

Pendekatan mekanisasi pemanenan non-selektif konvensional tidak cocok karena sistem pemotong traktoral memotong seluruh tanaman di satu baris tanpa memandang tingkat kematangan atau kondisi kesehatan individu tanaman. Pendekatan selektif berbasis robotika sebelumnya juga memiliki kelemahan signifikan pada aspek persepsi visual. Selada *iceberg* memiliki warna daun hijau yang identik dengan gulma dan daun pembungkus luar (*outer leaves*) di sekitarnya. Tantangan visual ini dikenal asalkan masalah *green-on-green* (hijau di atas hijau), yang membuat metode segmentasi berbasis ambang warna tradisional (*color thresholding*) tidak andal dalam mengidentifikasi batas selada secara akurat di bawah kondisi pencahayaan luar ruangan (*outdoor lighting*) yang berfluktuasi akibat sinar matahari langsung maupun bayangan awan. Masalah ini juga dipersulit oleh oklusi atau saling tertutupnya dedaunan antar-tanaman di lahan yang rapat.

## Ide Utama
Gagasan inti dari Vegebot adalah pemisahan tugas pengindraan visual dan manipulasi fisik ke dalam struktur koordinasi dua tahap (*two-stage pipeline*). Alur kerja ini dirancang untuk memastikan bahwa robot hanya memanen selada yang siap jual dan memotongnya pada posisi yang tepat tanpa menimbulkan kerusakan memar.

Untuk mengatasi hambatan variasi lingkungan luar ruangan dan kompleksitas visual *green-on-green*, persepsi visual dibagi menjadi lokalisasi global menggunakan kamera atas (*overhead camera*) untuk mendeteksi koordinat selada di lahan pertanian, diikuti oleh klasifikasi lokal menggunakan jaringan syaraf berbasis *Darknet* yang dilatih khusus untuk menganalisis kelayakan panen selada berdasarkan citra kepala selada yang telah dipotong (*cropped*), diputar (*rotated*), dan diberi bantalan (*padded*). Setelah target yang layak panen teridentifikasi, sistem memandu manipulator robotik Universal Robots UR10 yang dilengkapi dengan *end-effector* khusus. *End-effector* ini mengintegrasikan cakar pneumatik berperekat lembut (*soft pneumatic gripper*) untuk mencengkeram selada dengan tekanan yang terukur, kamera lokal untuk pemosisian akhir (*visual servoing*), serta pisau pemotong pneumatik yang dikendalikan dengan umpan balik gaya (*force feedback*) untuk mendeteksi kontak dengan tanah secara dinamis.

Berikut adalah diagram alur kerja deteksi, klasifikasi, dan manipulasi fisik pada Vegebot:

```
                                [Citra Input]
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │   Kamera Overhead (2 meter)   │
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │  Tahap 1: Jaringan Lokalisasi │ ──► Prediksi Bounding Box
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │  Pemotongan & Rotasi Citra    │
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │ Tahap 2: Jaringan Klasifikasi │ ──► Layak / Tidak Layak
                      └───────────────┬───────────────┘
                                      │ (Jika Layak Panen)
                                      ▼
                      ┌───────────────────────────────┐
                      │    Perencanaan Gerak (ROS)    │
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │  Kamera End-Effector (Lokal)  │ ──► Visual Servoing
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │  Cengkeraman Lembut & Potong  │ ──► Kontrol Force Feedback
                      └───────────────────────────────┘
```

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi Citra Bidang Kerja
Siklus pemanenan dimulai dengan akuisisi citra menggunakan kamera RGB atas (*overhead camera*) yang dipasang pada rangka robot setinggi kurang lebih 2 meter dari permukaan tanah. Kamera ini menangkap citra seluruh area kerja horizontal di bawah robot yang berisi tanaman selada dan tanah sekelilingnya secara dinamis dengan resolusi tinggi.

### 2. Jaringan Lokalisasi Selada (Tahap 1 CNN)
Citra dari kamera atas dikirimkan ke modul lokalisasi visual. Di dalam modul ini, sebuah CNN tahap pertama memproses citra untuk menemukan keberadaan setiap selada *iceberg*. Output dari jaringan lokalisasi ini adalah koordinat kotak pembatas (*bounding box*) berupa nilai piksel (x, y, lebar, tinggi) untuk setiap objek selada yang terdeteksi. Bounding box ini memisahkan setiap individu tanaman dari latar belakang gulma dan tanah.

### 3. Pemrosesan Citra Lokal (Crop, Rotate, dan Pad)
Sebelum citra potongan selada dikirim ke tahap klasifikasi, sistem melakukan pemrosesan awal (*preprocessing*) untuk meningkatkan konsistensi bentuk visual selada: citra di dalam bounding box dipotong, diputar berdasarkan estimasi orientasi pertumbuhan selada agar sejajar secara vertikal, dan diberi bantalan tepi agar memiliki rasio aspek persegi yang konsisten. Langkah ini memastikan performa pengklasifikasi pada tahap kedua tidak terganggu oleh variasi rotasi atau ukuran bounding box yang berbeda-beda.

### 4. Klasifikasi Kelayakan Panen (Tahap 2 CNN)
Citra selada hasil pemrosesan awal diumpankan ke jaringan klasifikasi berbasis kerangka kerja *Darknet* (arsitektur YOLOv3 yang disesuaikan). Jaringan ini dilatih untuk mengklasifikasikan kondisi selada menjadi tiga kelas utama: kelas matang (*harvestable*), kelas belum matang (*immature*), dan kelas rusak/sakit (*unmarketable*). Hal ini mencegah pemotongan selada yang belum matang atau sakit, sehingga menjaga kualitas hasil panen secara selektif.

### 5. Transformasi Koordinat 2D ke Ruang 3D dan Perencanaan Gerak
Jika selada layak panen, koordinat pusat bounding box dari citra 2D ditransformasikan ke koordinat ruang 3D nyata (X, Y, Z) menggunakan matriks kalibrasi intrinsik dan ekstrinsik kamera terhadap lengan robot. Koordinat target dikirim ke perencana gerakan robotik di bawah ROS untuk merencanakan jalur pergerakan bebas tabrakan bagi lengan robot Universal Robots UR10 agar bergerak membawa *end-effector* dari posisi tinggi langsung menuju ke atas koordinat pusat selada.

### 6. Pemosisian Lokal dan Pemotongan Batang
Ketika *end-effector* berada dekat dengan selada (jarak kurang dari 30 cm), kamera kedua pada bagian dalam cakar robot melakukan *visual servoing* (pengendalian gerakan robot berbasis umpan balik visual lokal) untuk mengoreksi kesalahan posisi kecil akibat goyangan mekanis atau tiupan angin. Setelah itu, manipulator menurunkan cakar pneumatik berperekat lembut (*soft pneumatic gripper*) untuk membungkus kepala selada dengan tekanan udara rendah. Bersamaan dengan cengkeraman tersebut, pisau pneumatik digerakkan ke bawah untuk memotong batang selada. Sensor umpan balik gaya (*force feedback*) digunakan untuk merasakan hambatan mekanis saat pisau menyentuh tanah, sehingga proses pemotongan dapat diselesaikan tepat di atas batas tanah tanpa merusak komponen pisau.

## Eksperimen dan Hasil
Pengujian lapangan sistem Vegebot dilakukan di lahan pertanian komersial milik koperasi pertanian G's Growers di Cambridge, Inggris. Eksperimen ini mengevaluasi performa sistem penglihatan komputer dan mekanisme pemotongan fisik dalam kondisi pertanian nyata yang berangin, berlumpur, serta di bawah fluktuasi pencahayaan matahari alami.

Dari pengujian performa penglihatan komputer (persepsi), jaringan lokalisasi dan klasifikasi gabungan berhasil melokalisasi dan mengidentifikasi selada dengan tingkat keberhasilan sebesar 91,1% di lapangan. Model visi terbukti tangguh memisahkan selada dari gulma hijau di sekitarnya. Sementara dari pengujian performa pemanenan mekanis (manipulasi), dari total 60 selada matang yang ditargetkan untuk dipanen secara fisik di lapangan terbuka, Vegebot berhasil memotong dan memindahkan 31 selada ke wadah penampung secara otonom, menghasilkan tingkat keberhasilan pelepasan tanaman (*detachment success rate*) sebesar 51,7%. Rata-rata waktu siklus (*cycle time*) pemanenan yang tercatat adalah sebesar 31,2 detik per selada, yang terdiri dari pemrosesan visual selama kurang lebih 4 detik, dan 27,2 detik untuk pergerakan lengan robot UR10 serta pemotongan batang. Tingkat kerusakan fisik pada selada yang berhasil dipanen adalah sebesar 38,3%, yang didominasi oleh robekan kecil pada daun luar akibat gesekan cakar pneumatik.

## Kelebihan dan Keterbatasan

### Kelebihan
- **Teruji di Lapangan Nyata (*Field-Tested*)**: Berbeda dengan mayoritas penelitian robotika pertanian yang diuji di laboratorium terkontrol, Vegebot diuji langsung di lahan pertanian komersial terbuka dengan kondisi tanah dan cuaca alami.
- **Sistem Penglihatan Dua Tahap yang Tangguh**: Pendekatan klasifikasi berbasis Darknet setelah tahap lokalisasi berhasil mengatasi masalah *green-on-green* dan variasi pencahayaan eksternal secara efektif.
- **Keamanan Manipulasi Produk Lembut**: Desain cakar pneumatik berperekat lembut dikombinasikan dengan umpan balik gaya pada pisau potong memberikan solusi orisinal untuk meminimalkan memar pada produk pertanian bertekstur lunak.

### Keterbatasan
- **Waktu Siklus yang Lambat**: Secara konseptual, kecepatan pemanenan sebesar 31,2 detik per selada masih sangat jauh tertinggal dari efisiensi pemanenan oleh manusia terlatih yang hanya memerlukan waktu sekitar 2 hingga 3 detik per selada.
- **Tingkat Kerusakan Produk yang Tinggi**: Secara rekayasa, tingkat kerusakan selada sebesar 38,3% masih terlalu tinggi untuk memenuhi standar kualitas kontrol supermarket yang ketat.
- **Ketergantungan pada Kerapatan Lahan**: Performa deteksi visual akan menurun secara dramatis apabila tanaman selada tumbuh terlalu rapat atau saling tumpang tindih secara ekstrem, karena kesulitan mengidentifikasi batas *bounding box* individu selada.

## Kaitan dengan Bab Lain
Vegebot merupakan representasi evolusi penting dari penelitian deteksi pertanian pasif menuju sistem manipulasi fisik yang aktif dan selektif. 

Jika dibandingkan dengan bab-bab pertanian lain:
- **Persepsi Objek**: Penelitian deteksi buah seperti [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md), [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md), dan [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md) berfokus pada optimasi model deteksi visual untuk menghitung buah atau bunga di atas pohon. Vegebot mengadopsi deteksi berbasis Darknet yang serupa tetapi mengintegrasikannya langsung dengan perencanaan gerakan lengan robotik untuk eksekusi fisik di permukaan tanah.
- **Estimasi Kedalaman 3D**: Penelitian lokalisasi buah pada [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) dan [124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md) memanfaatkan sensor RGB-D untuk pemetaan spasial 3D buah secara langsung. Sebaliknya, Vegebot mengandalkan proyeksi kamera RGB 2D ganda (atas dan lokal) yang membutuhkan kalibrasi kamera eksternal dan internal untuk mencapai koordinat 3D.
- **Otomasi Panen**: Robot pemanen buah pada [126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.) - Pertanian](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md) menunjukkan pemanenan buah apel/pear di pohon. Kompleksitas Vegebot berbeda karena bekerja pada tingkat tanah yang memiliki interaksi gaya fisik langsung dengan permukaan tanah, sehingga memerlukan sensor gaya mekanis. 
- **Peningkatan Visualisasi**: Teknologi visualisasi 3D pada [127 - 2020 - Fruit Detection & 3D Visualisation (Kang & Chen) - Pertanian](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md) berpotensi diterapkan pada modul visual servoing Vegebot untuk meningkatkan akurasi estimasi tinggi pemotongan batang selada secara 3D.

## Poin untuk Sitasi
- **Kunci BibTeX**: `birrell2020lettuce`
- **Ringkasan Sitasi**:
  Birrell dkk. (2020) mengembangkan Vegebot, sistem robotik pemanen selada *iceberg* selektif yang diuji di lapangan komersial nyata. Sistem ini menggabungkan visi komputer dua tahap berbasis CNN (lokalisasi dan klasifikasi Darknet) dengan lengan robotik UR10, cakar pneumatik lembut, dan pemotong berbasis sensor gaya (*force feedback*). Diuji di lapangan terbuka, sistem ini memperoleh akurasi lokalisasi visual sebesar 91,1%, tingkat keberhasilan pemotongan sebesar 51,7%, waktu siklus rata-rata 31,2 detik per selada, dan tingkat kerusakan produk sebesar 38,3%.
- **Catatan Angka/Klaim untuk Verifikasi**:
  Keberhasilan pelepasan fisik selada adalah 51,7% (31 dari 60 selada), waktu siklus rata-rata adalah 31,2 detik, tingkat kerusakan fisik selada adalah 38,3%, dan akurasi lokalisasi visual di lahan adalah 91,1%. Semua data ini diverifikasi langsung dari uji lapangan komersial di Cambridge, Inggris bersama G's Growers.
