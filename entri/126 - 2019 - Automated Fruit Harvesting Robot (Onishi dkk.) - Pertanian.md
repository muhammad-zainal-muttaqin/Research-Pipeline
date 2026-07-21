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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract Automation and labor saving in agriculture have been required recently. However, mechanization and robots for growing fruits have not been advanced. This study proposes a method of detecting fruits and automated harvesting using a robot arm. A highly fast and accurate method with a Single Shot MultiBox Detector is used herein to detect the position of fruit, and a stereo camera is used to detect the three-dimensional position. After calculating the angles of the joints at the detected position by inverse kinematics, the robot arm is moved to the target fruit’s position. The robot then harvests the fruit by twisting the hand axis. The experimental results showed that more than 90% of the fruits were detected. Moreover, the robot could harvest a fruit in 16 s. Keywords: Harvesting fruits, Robot, Manipulation, Deep learning Background The agriculture industry has many problems, including the decreasing number of farm workers and increasing cost of fruit harvesting. Saving labor and scale up in agriculture is necessary in solving these problems. In recent years, the automation of agriculture has been advancing for labor saving and large-scale agriculture. However, much of the work in the field of fruit harvesting is manually done. The development of an automated fruit harvesting robot is a viable solution to these problems. The automatic harvesting of fruits by a robot involves two big tasks: (1) fruit detection and localization on trees using computer vision with a sensor and (2) robot arm motion to the position of the detected fruit and fruit harvesting by the end effector without damaging target fruit and its tree. The fruit detection and localization on trees using computer vision have been investigated in numerous studies, and most of these have been summarized in the review of Gongal et al. [1]. Color, spectral, or thermal cameras have been widely used in these methods. When using spectral camera [2], detecting the fruit shadowed by another

fruit as an object is difficult. When a thermal camera is used [3], the fruit is detected based on the temperature difference between the fruit and the background. This method is affected by the fruit size and exposure to direct sunlight. Various different features are used in fruit detection using color camera. Bulanon et al. [4, 5] used luminance and red, green, and blue (RGB) color difference to segment an apple. Rakun et al. [6] used texture analysis to detect an apple. Linker et al. [7] integrated multiple features to improve the accuracy of fruit detection methods. Various image classification methods for fruit detection can also be performed using a color camera. Bulanon et al. [8] used K-mean clustering for apple detection. Linker et al. [7] and Cohen et al. [9] used KNN clustering for apple classification. In addition, Kurtulmus et al. [10] used an Artificial Neural Network for apple classification. Qiang et al. [11] used a Support Vector Machine classification method for apple detection. However, these methods are difficult to use in variable light conditions because the color information cannot be sufficiently acquired. For better accuracy, fruit detection should be performed using multiple features such as color, shape, texture, and reflection to overcome challenges like clustering and variable light conditions. The present study proposes “fruit detection and localization” and “fruit harvesting by a robot manipulator with a hand which is able to harvest without damaging

© The Author(s) 2019. This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creat​iveco​mmons​.org/licen​ses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

the fruit and its tree” to perform automatic fruit harvesting by a robot. We used a color camera and a Single Shot MultiBox Detector (SSD) [12] to detect the twodimensional (2D) position of the fruit. The SSD is one of the general object detection methods that use Convolution Neural Network (CNN) [13]. The SSD can comprehensively judge from color and shape. A threedimensional (3D) position must be obtained to send a command to the robot arm. A stereo camera is used to measure the 3D position of the fruit detected by the SSD. We used inverse kinematics to calculate the route of the robot arm. We moved the robot arm to the fruit position based on inverse kinematics. We used the harvesting robot hand as the end effector. The robot hand harvests a fruit by gripping and rotating it without damaging it and its tree.

Methods We describe each step in our fruit detection and harvest method in this section. Apple and tree

The fruit used in this research is the “Fuji” apple cultivated in the Miyagi Prefectural Agriculture and Horticulture Research Center. However, our method can also be applied to other apple varieties. A pear has a relatively similar shape to an apple; hence, this algorithm is also considered effective for pears. We used herein a joint V-shaped apple tree [14]. The V-shaped tree shape was suitable for mechanization and efficiency, and its fruits can be easily harvested. Figure 1 shows the tree used herein. Detection and harvest algorithm

The harvest robot was equipped with a stereo camera and a robot arm. Figure 2 presents the detection and harvest algorithm. The algorithm involves three steps:

detecting the 2D position of the apple, detecting 3D position of the apple, and calculating the inverse kinematics. These steps were divided into the detection and harvest parts. We explain each method in the sections that follow. Fruit position detection method

Position p and posture R of the hand must be moved to as specified harvest the fruit using the robot hand attached to the robot arm. In the case of a vertically articulated robot arm, the position and posture of the hand ( p, R ) are determined by the angles q of each joint. Therefore, the relationship between the joint coordinate system representing the joint angle of the robot arm and the hand coordinate system representing the position and posture of the hand must be clarified. The problem of determining the angles q of each joint from the hand position p and posture R is called an inverse kinematics problem [17]. The inverse kinematics problem aims to find a nonlinear function f −1 for the equation Eq. (1) is determined by the robot arm mechanism and configuration.

We considered that the inverse kinematic problem of the robot arm had six links. We used UR3 made by UNIVERSAL ROBOTS as the robot arm. UR3 has six degrees of freedom; thus, arbitrary position and posture can be expressed as long as they are within the operating range. Table 1 shows the Denavit–Hartenberg parameter of UR3. Table 2 presents the UR3 specification. Figure 3 displays the UR3 used herein. The Denavit–Hartenberg parameters in UR3 are described in Fig. 4. We obtain the angles q = θi (i = 1, 2, . . . , 6) of each joint when we are given the position p(px , py , pz ) and

This describes the result of the fruit position detection. The images taken at Miyagi Prefectural Agriculture and Horticulture Research Center were used for learning and testing. Shooting was performed to look at the fruit from below considering the minimized occlusion by the leaves, branches and other fruits. Figure 5 depicts the image taken by this method. We used the learning parameters shown in Table 3.

We tested whether fruits can be detected using unlearned images taken in the orchard using the learned model. We surrounded the area where the possibility of fruit was 60% or more with a red frame. We detected the presence of an apple to be tested from 30 images with 169 apples in total. Figures 6 and 7 depict the tested

images. Figures 8 and 9 show the test image result. The model can detect even if the fruits are partially occluded by other fruits and leaves. However, the fruits at the edge of the image and those far from the camera could not be detected. The edge of the image could not be detected because the fruits were cut off in the image. The fruits far from the camera could not be detected because they had become smaller in the image. However, this was not a problem herein because these fruits were out of reach of the robot arm. Table 4 presents this test result.

Figure 10 displays the harvesting robot used herein. We conducted fruit harvesting using this robot with a stereo camera installed at approximately 0.5 (m) below the base of the robot arm such that the fruit tree is looked up from directly below. If the distance to the target fruit is too long and the robot arm cannot reach the target, the table lift on which all equipment rides goes up and down, moving to the distance where the arm can reach. We use UR3 (UNIVERSAL ROBOTS) as the robot arm. Table 2 shows the robot repeatability is ± 0.1 (mm). The robot palm diameter was 5 cm; hence, even if an error occurs, it can be suppressed by the robot hand. We used ZED (STEREO LABS) as the stereo camera, with specifications shown in Table 5.

We describe the automated apple harvesting in this section. Figure 11 illustrates the experimented tree and a model of the apple tree at the Miyagi Prefectural Agriculture and Horticultural Research Center. These trees were joint V-shaped trees [14] like those in the Miyagi Prefectural Agricultural and Horticultural Research Center. Conducting the experiment during apple harvest time was difficult; hence, we experimented with a tree model. The results of the automated fruit harvesting experiments are presented herein along with the detection unit of the harvesting robot. First, we detected the 2D fruit position. Figure 12 shows the fruit detection result by the

SSD. We used a learning model that can detect more than 90% of the fruits used (fruit position detection section). We surrounded the area where the possibility of fruit was 60% or more, with a red frame. The robot was able to detect the apples the same as the real ones; hence, it seemed enough for the experiment.

Conclusions In this study, we performed automatic fruit harvesting through the method of fruit position detection and harvesting using a robot manipulator with a harvesting hand that does not damage the fruit and its tree. Using the SSD, we showed that the fruit position of 90% or more can be detected in 2 s. The proposed fruit harvesting algorithm also showed that one fruit can be harvested in approximately 16 s. The fruit harvesting algorithm proposed herein is expected to be applicable even if it is a near species of apple. Moreover, if one learns again with the target fruit, harvesting fruits, such as pears is highly possible. Abbreviations SSD: Single Shot MultiBox Detector; CNN: Convolution Neural Network. Acknowledgements This research was supported by grants from the Project of the Bio-oriented Technology Research Advancement Institution, NARO (the research project for the future agricultural production utilizing artificial intelligence). Authors’ contributions YO conducted all research and experiments. TY and TF conducted a research concept, participated in design adjustment, and drafted a paper draft assistant. All authors read and approved the final manuscript. Competing interests The authors declare that they have no competing interests.

Second, we measured the 3D fruit position. Figure 13 depicts the 3D position of the center point of the frame detected by the SSD. The 3D reconstruction of the parts other than the apples themselves was inadequate, but in this experiment it is unnecessary except for the bottom surface of the apple. Sufficient results were obtained because we were able to capture the bottom of the apple. Next, we will describe the harvesting part of the harvesting robot. To insert the robot hand from the underside for fruit harvesting, the robot was first moved 10 (cm) below the target fruit (Fig. 14). The arm then rose below the fruit (Fig. 15). The robot hand then grasped the fruit and harvesting it by twisting from the peduncle by rotating for four times (Fig. 16). The harvest time for each fruit was approximately 16 s. Detecting the fruit position and calculating the joint angle at that position took approximately 2 s. Fruit harvesting took approximately 14 s. Harvesting consumed much time because the hand rotated for several times. By reconsidering these points, speedup is possible.
