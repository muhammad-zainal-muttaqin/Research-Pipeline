# 126 - An Automated Fruit Harvesting Robot by Using Deep Learning

## Metadata Ringkas
| Parameter | Nilai |
|---|---|
| Kunci BibTeX | `onishi2019harvest` |
| Judul Asli | An Automated Fruit Harvesting Robot by Using Deep Learning |
| Penulis | Yuki Onishi, Takeshi Yoshida, Hiroki Kurita, Takanori Fukao, Hiromu Arihara, Ayako Iwai |
| Tahun | 2019 |
| Venue | ROBOMECH Journal |
| Tema Klaster | Pertanian |

## Tautan Akses
- **Google Scholar:** https://scholar.google.com/scholar?q=An%20Automated%20Fruit%20Harvesting%20Robot%20by%20Using%20Deep%20Learning
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=An%20Automated%20Fruit%20Harvesting%20Robot%20by%20Using%20Deep%20Learning&sort=relevance
- **DOI Portal:** https://doi.org/10.1186/s40648-019-0141-2

## Gambaran Umum
Makalah ini menyajikan pengembangan sistem robot pemanen buah otomatis yang dirancang untuk melokalisasi dan memetik buah apel di perkebunan secara mandiri. Sistem ini menggabungkan visi komputer berbasis pembelajaran mendalam (*deep learning*) untuk deteksi objek dalam koordinat dua dimensi dengan sensor kamera stereo (*stereo camera*) guna mengestimasi posisi spasial tiga dimensi target buah. Lengan robot industri dengan enam derajat kebebasan (*degrees of freedom*) digerakkan ke posisi buah dan memanipulasi cakar penangkap buah (*end effector*) melalui penyelesaian persamaan kinematika balik (*inverse kinematics*) secara analitis.

Hasil pengujian menunjukkan bahwa sistem deteksi mampu mengidentifikasi lebih dari 90,0% buah apel pada citra dengan waktu pemrosesan citra dan kalkulasi rute gerakan sekitar 2,0 detik. Proses pemetikan fisik buah apel pada model pohon tiruan membutuhkan waktu rata-rata sekitar 14,0 detik per buah, sehingga total waktu siklus pemanenan lengkap untuk satu buah apel adalah 16,0 detik. Pengambilan buah dilakukan dari arah bawah pohon untuk meminimalkan oklusi dedaunan, sedangkan pemisahan buah dilakukan dengan memutar tangkai buah (*peduncle*) sebanyak empat kali putaran tanpa menimbulkan kerusakan mekanis pada buah maupun cabang pohon.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sektor pertanian buah-buahan menghadapi tantangan berupa penyusutan jumlah tenaga kerja produktif di pedesaan serta peningkatan biaya operasional pemanenan buah secara manual. Otomasi melalui robot pemanen buah menjadi solusi potensial untuk menekan biaya operasional dan menjaga keberlanjutan produksi buah skala besar. Namun, pengembangan robot pemanen buah yang mandiri menghadapi dua kendala teknis utama, yaitu akurasi dan kecepatan deteksi objek dalam kondisi lingkungan kebun yang dinamis, serta mekanisme manipulasi fisik yang aman agar tidak merusak buah atau struktur pohon saat pemetikan.

Sebelumnya, metode visi komputer pertanian mengandalkan fitur manual berbasis warna (*color*), bentuk (*shape*), atau tekstur (*texture*). Pendekatan warna RGB murni rentan gagal akibat fluktuasi pencahayaan alami di kebun, seperti bayangan dedaunan atau paparan sinar matahari langsung. Sensor alternatif seperti kamera termal sensitif terhadap pemanasan latar belakang oleh matahari, sedangkan kamera hiperspektral terhambat oleh oklusi dedaunan. Selain masalah persepsi sensor, manipulasi mekanis lengan robot sering kali lambat dan berisiko merusak dahan jika tidak dipandu oleh lokalisasi koordinat tiga dimensi yang presisi. Integrasi bentuk pohon berbentuk V (*joint V-shaped tree*) juga sangat penting untuk menyederhanakan ruang gerak mekanis robot dibandingkan bentuk pohon tradisional yang lebat dan acak.

## Ide Utama
Gagasan inti dari penelitian ini adalah mengintegrasikan detektor objek berbasis jaringan saraf konvolusi (*Convolutional Neural Network*) satu tahap (*single-stage detector*) untuk mendeteksi koordinat dua dimensi buah dengan rekonstruksi kedalaman berbasis paralaks dari kamera stereo. Dengan memposisikan kamera stereo menghadap ke atas di bawah pohon, oklusi akibat dedaunan dapat dikurangi karena sebagian besar apel menggantung ke bawah. 

Setelah koordinat buah dalam ruang tiga dimensi ditentukan berdasarkan koordinat piksel tengah dari kotak pembatas (*bounding box*) detektor, sudut-sudut sendi lengan robot dihitung menggunakan solusi persamaan kinematika balik analitis. Lengan robot kemudian digerakkan ke titik pendekatan tepat 10,0 cm di bawah buah, naik secara vertikal untuk mencengkeram buah, lalu memutar sumbu cakar penangkap sebanyak empat kali putaran demi memotong tangkai buah (*peduncle*) dengan aman tanpa merusak buah maupun ranting pohon.

## Cara Kerja Langkah demi Langkah

### Sistem Sensor dan Pemrosesan Citra 2D
Sistem memulai pemrosesan dengan menangkap citra dari kamera stereo ZED. Deteksi koordinat buah dua dimensi dilakukan menggunakan arsitektur *Single Shot MultiBox Detector* (SSD). Jaringan saraf ini menggunakan tulang punggung (*backbone*) berupa jaringan VGG (*VGG net*) untuk melakukan ekstraksi fitur spasial secara hierarkis. SSD menerapkan filter konvolusi kecil pada peta fitur (*feature maps*) dari berbagai skala guna memprediksi kelas objek dan koordinat kotak pembatas secara simultan tanpa memerlukan modul usulan wilayah (*region proposal*) yang terpisah seperti pada Faster R-CNN. 

Penggunaan peta fitur multi-skala ini penting untuk mendeteksi apel dengan ukuran bervariasi akibat perbedaan jarak dari kamera. SSD mencapai kecepatan pemrosesan 59,0 FPS dengan mAP 74,3% pada pengujian VOC2007 (menggunakan GPU NVIDIA Titan X), mengungguli Faster R-CNN (7,0 FPS, mAP 73,2%) dan YOLOv1 (45,0 FPS, mAP 63,4%). Keunggulan kecepatan dan akurasi SSD ini menjadikannya pilihan utama untuk pemrosesan waktu nyata (*real-time*) di lapangan.

### Pengukuran Kedalaman 3D dan Lokalisasi
Setelah kotak pembatas apel terdeteksi pada citra dua dimensi oleh SSD, sistem mengekstrak koordinat piksel tengah dari kotak pembatas tersebut. Untuk menentukan posisi buah dalam ruang koordinat tiga dimensi relatif terhadap basis lengan robot, sistem memanfaatkan informasi kedalaman dari kamera stereo ZED. 

Kamera stereo ZED memanfaatkan citra dari lensa kiri dan kanan yang terpisah sejauh jarak basis (*baseline*). Perbedaan posisi horizontal objek pada kedua citra disebut paralaks (*parallax*). Secara matematis, jarak kedalaman $Z$ dihitung melalui rumus:

$$Z = \frac{f \cdot B}{d}$$

Di mana $f$ adalah panjang fokus lensa (*focal length*), $B$ adalah jarak basis (*baseline*) antar-lensa, dan $d$ adalah nilai paralaks (*disparity*) piksel objek. Melalui metode triangulasi matematis ini, sistem melakukan rekonstruksi spasial untuk menghasilkan data awan titik (*point cloud*) dalam koordinat tiga dimensi $(X, Y, Z)$ untuk setiap piksel. Koordinat tiga dimensi dari piksel pusat kotak pembatas buah kemudian digunakan sebagai titik target spasial bagi gerakan lengan robot.

### Pemodelan Kinematika Balik Lengan Robot
Koordinat target tiga dimensi buah $(p_x, p_y, p_z)$ dan orientasi cakar $(R)$ dikonversi menjadi sudut sendi manipulator UR3 (Universal Robots) dengan enam derajat kebebasan. Hubungan geometris antar-tautan sendi didefinisikan melalui konvensi parameter Denavit-Hartenberg (DH) yang memetakan matriks transformasi homogen dari basis robot ke cakar. Hubungan ini dirumuskan dalam persamaan kinematika balik analitis untuk memperoleh sudut sendi $\theta_1$ hingga $\theta_6$. Sebagai contoh, sudut sendi dasar ($\theta_1$) dihitung berdasarkan koordinat target dan parameter panjang melalui fungsi trigonometri:

$$A_1 = \arctan \left( \frac{p_y - d_6 R_{23}}{p_x - d_6 R_{13}}\right)$$
$$B_1 = \arccos \left( \frac{d_4}{\sqrt{(p_x - d_6 R_{13})^2 + (p_y - d_6 R_{23})^2}}\right)$$
$$\theta_1 = A_1 \pm B_1 + \frac{\pi }{2}$$

Melalui serangkaian persamaan trigonometri analitis tertutup ini, sistem dapat menghitung seluruh sudut sendi robot secara instan tanpa perlu melakukan komputasi iteratif numerik yang lambat, sehingga menghemat waktu siklus komputasi dan menghindari masalah ketidakkonvergenan lokal pada algoritma kontrol robot.

### Alur Pengeksekusian Pemetikan Fisik
Urutan gerakan robot selama proses pemanenan buah mengikuti diagram alir berikut:

```
[Mulai Siklus]
      │
      ▼
[Tangkap Citra Stereo dari Bawah]
      │
      ▼
[Deteksi SSD 2D & Ambil Piksel Tengah Bounding Box]
      │
      ▼
[Hitung Koordinat 3D via Point Cloud Kamera Stereo ZED]
      │
      ▼
[Selesaikan Kinematika Balik (IK) untuk Target Spasial]
      │
      ▼
[Gerakkan UR3 ke Titik Pendekatan (10 cm di Bawah Buah)]
      │
      ▼
[Gerakkan UR3 Naik secara Vertikal Mengarah ke Buah]
      │
      ▼
[Aktifkan Cakar Penangkap (Diameter 5 cm) untuk Mencengkeram]
      │
      ▼
[Putar Sumbu Pergelangan UR3 sebanyak 4 Kali Putaran]
      │
      ▼
[Putuskan Tangkai (Peduncle) & Simpan Buah]
      │
      ▼
[Selesai Siklus]
```

Seluruh perangkat keras dipasang di atas lift meja (*table lift*). Jika target di luar jangkauan lengan robot UR3, lift meja akan bergerak vertikal menyesuaikan posisi. Kamera stereo ZED diletakkan 0,5 meter di bawah basis lengan robot UR3 menghadap ke atas untuk meminimalkan oklusi dedaunan. Cakar penangkap buah berdiameter 5,0 cm dirancang khusus dengan bahan pelapis karet lunak untuk mencegah timbulnya memar mekanis pada buah apel saat dicengkeram. Proses rotasi cakar sebanyak empat kali putaran dipilih karena merupakan batas optimal untuk memutuskan tangkai apel varietas Fuji dari rantingnya tanpa menarik dahan secara berlebihan.

## Eksperimen dan Hasil
Dataset pemelajaran untuk model SSD dikumpulkan langsung di kebun milik Miyagi Prefectural Agriculture and Horticulture Research Center pada pohon apel varietas "Fuji" dengan pola tanam berbentuk V bersendi (*joint V-shaped tree*). Namun, karena pengujian perangkat keras robot secara keseluruhan tidak dapat dilakukan pada musim panen apel yang terbatas, evaluasi kinerja pemetikan robotik dilakukan menggunakan model pohon apel buatan yang meniru karakteristik spasial pohon asli di laboratorium.

Dalam evaluasi performa detektor SSD terhadap 30 citra uji yang memuat total 169 buah apel nyata di kebun, model berhasil mendeteksi buah dengan tingkat keberhasilan (*success rate*) melebihi 90,0% menggunakan ambang batas keyakinan (*confidence threshold*) $\ge 60,0\%$. Kegagalan deteksi sebagian besar terjadi pada apel yang terletak di tepi citra karena terpotong oleh batas gambar, serta apel yang jaraknya terlalu jauh dari kamera sehingga resolusinya terlalu kecil. Kegagalan deteksi jarak jauh ini tidak memengaruhi kinerja panen karena apel-apel tersebut berada di luar radius jangkauan lengan robot UR3.

Dari aspek efisiensi waktu pemrosesan, total waktu siklus pemanenan rata-rata adalah 16,0 detik per buah. Pemrosesan komputasi yang meliputi akuisisi citra stereo, deteksi objek berbasis SSD, lokalisasi spasial tiga dimensi, serta kalkulasi kinematika balik analitis hanya membutuhkan waktu sekitar 2,0 detik. Sebaliknya, proses manipulasi mekanis lengan robot untuk bergerak mendekat, naik vertikal, mencengkeram, dan memutar tangkai buah sebanyak empat kali putaran memakan waktu sekitar 14,0 detik. Eksperimen ini mengonfirmasi bahwa kendala utama kecepatan sistem terletak pada gerakan fisik manipulator robot, bukan pada komputasi visi komputer.

## Kelebihan dan Keterbatasan
Dari sisi rekayasa sistem, pemilihan sudut pandang kamera dari bawah ke atas sangat efektif meminimalkan oklusi karena buah apel secara alami menggantung di bawah daun. Integrasi detektor SSD, kamera stereo ZED, lengan robot UR3, dan lift meja memberikan solusi kompak untuk memanen buah pada berbagai ketinggian pohon berbentuk V bersendi.

Secara konseptual, sistem ini masih memiliki keterbatasan yang signifikan. Proses pemetikan fisik selama 14,0 detik per buah tergolong lambat untuk implementasi komersial skala besar, terutama karena kebutuhan gerakan rotasi cakar sebanyak empat kali untuk memotong tangkai buah. Selain itu, eksperimen pemetikan fisik hanya diuji pada model pohon buatan di lingkungan laboratorium yang terkendali, sehingga keandalan mekanis cakar penangkap dalam menghadapi buah dengan ketebalan tangkai yang bervariasi atau dahan nyata yang elastis belum sepenuhnya teruji. Terakhir, sistem kontrol robot belum dilengkapi dengan algoritma penghindaran rintangan dinamis (*dynamic obstacle avoidance*) untuk mencegah tabrakan lengan robot dengan cabang kayu yang tebal jika posisi buah terhalang secara rumit.

## Kaitan dengan Bab Lain
Sistem robot pemanen buah otomatis ini mewarisi kebutuhan penting akan deteksi objek di sektor pertanian yang dibahas dalam bab-bab sebelumnya. Metode deteksi apel dua dimensi menggunakan model detektor yang ditingkatkan dibahas secara mendalam pada [Apple Detection (Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md), sementara deteksi bunga apel untuk penjarangan buah menggunakan model kompresi dibahas pada [Apple Flower Detection (Pruned YOLOv4)](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md). Berbeda dengan penelitian-penelitian tersebut yang berfokus pada optimasi arsitektur pendeteksi dua dimensi, Onishi dkk. melangkah lebih jauh ke arah tindakan fisik dengan mengintegrasikan detektor SSD dengan kontrol robot manipulator secara fisik.

In hal penginderaan spasial tiga dimensi, penelitian ini sebanding dengan [Apple Detection RGB+Depth (Faster R-CNN)](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) yang menggunakan Faster R-CNN pada data RGB-D, serta [Fruit Detection & 3D Location (Gene-Mola dkk.)](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md) yang menggunakan kombinasi sensor kedalaman terdedikasi (seperti Microsoft Kinect) dan metode *Structure-from-Motion* (SfM). Onishi dkk. memilih menggunakan kamera stereo ZED untuk menghasilkan data awan titik secara mandiri melalui informasi paralaks tanpa memancarkan cahaya inframerah aktif yang rentan terganggu oleh cahaya matahari luar ruangan.

Penerapan detektor SSD dalam membimbing lengan robot pertanian juga memiliki kesamaan dengan [Iceberg Lettuce Harvesting Robot](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md) yang menggunakan SSD untuk melokalisasi titik pemotongan pada selada. Selain itu, visualisasi spasial buah untuk kebutuhan estimasi hasil panen secara lebih komprehensif dibahas pada [Fruit Detection & 3D Visualisation (Kang & Chen)](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md).

## Poin untuk Sitasi
Kunci BibTeX: `onishi2019harvest`

Ringkasan kutipan tinjauan pustaka:
> Onishi dkk. (2019) mengembangkan sistem robot pemanen apel otomatis yang mengintegrasikan detektor SSD untuk lokalisasi dua dimensi dan kamera stereo ZED untuk estimasi koordinat tiga dimensi. Sistem ini mengontrol lengan robot UR3 enam derajat kebebasan melalui solusi kinematika balik analitis, mencapai akurasi deteksi buah di atas 90,0% dan waktu siklus panen rata-rata 16,0 detik per buah dengan memutar tangkai buah sebanyak empat kali putaran dari arah bawah pohon.

Catatan verifikasi data:
> Eksperimen pemetikan fisik lengan robotik dalam penelitian ini dievaluasi menggunakan model pohon apel buatan (*apple tree model*) di laboratorium, bukan pada pohon apel nyata di kebun, karena kendala musim panen apel yang singkat. Komparasi kinerja SSD, Faster R-CNN, dan YOLOv1 yang dikutip di bagian metodologi merujuk pada hasil pengujian standar dataset VOC2007, bukan pada dataset apel kebun.
