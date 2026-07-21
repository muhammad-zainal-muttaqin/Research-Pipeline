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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract Agriculture provides an unique opportunity for the development of robotic systems; robots must be developed which can operate in harsh conditions and in highly uncertain and unknown environments. One particular challenge is performing manipulation for autonomous robotic harvesting. This paper describes recent and current work to automate the harvesting of iceberg lettuce. Unlike many other produce, iceberg is challenging to harvest as the crop is easily damaged by handling and is very hard to detect visually. A platform called Vegebot has been developed to enable the iterative development and field testing of the solution, which comprises of a vision system, custom end effector and software. To address the harvesting challenges posed by iceberg lettuce a bespoke vision and learning system has been developed which uses two integrated convolutional neural networks to achieve classification and localization. A custom end effector has been developed to allow damage free harvesting. To allow this end effector to achieve repeatable and consistent harvesting, a control method using force feedback allows detection of the ground. The system has been tested in the field, with experimental evidence gained which demonstrates the success of the vision system to localize and classify the lettuce, and the full integrated system to harvest lettuce. This study demonstrates how existing state‐of‐the art vision approaches can be applied to agricultural robotics, and mechanical systems can be developed which leverage the environmental constraints imposed in such environments. KEYWORDS

The story of agriculture is one of increasing automation. Crops are

from country to country and even company to company. While some

approach. This is implemented using two CNNs, the architecture

being shaped by the data sets available. Using this method in field

Hajjaj & Sahari, 2016) to cope. Harvesting and other crop manipulation

achieved, and the crop accurately classified. Second, the lettuces are

camera, pneumatics, a belt drive, and a soft gripper. The end effector

way that avoids damage. As the ground is uneven and its depth hard

make the cut and achieve a consistent cutting height.

outlines the overall system that was developed. Section 4 focuses on

while the lettuce head can easily be damaged by unpractised handling.

system and end effector. The field tests and experimental results are

conclusion that suggests the application of the techniques and

handling the vegetable delicately. There is a growing need for

This study investigates automating the harvesting of iceberg lettuce with three key research goals. First, how vision systems

There is prior work on vision techniques for agriculture. Many of

the late 2000s, and so use a wide variety of hand‐crafted features.

allow for the data sets available. Secondly, how mechanical

approach of rapid iterative design, prototyping, and field testing. Two

iceberg lettuce under challenging and uncertain field conditions.

F I G U R E 1 (a) The challenging localization and classification problem posed by the lettuce field. (b) The existing harvesting method [Color figure can be viewed at wileyonlinelibrary.com]

project required a separate algorithm. Grapes were classified on

demonstrate how selective plant harvesting is possible. These previous

water jet cutting. These approaches have limitations, most notably that

and there is a lack of reliability in stem cutting height and quality.

tion (Van Henten et al., 2006) and classified for maturity by estimating their weight from the perceived volume (Van Henten et al., 2002). A more recent experiment detected broccoli heads using an RGB‐D sensor had the disadvantage that the robot had to move a tent across the field to prevent interference from outdoor light. Point clouds were clustered from the depth information,

structed. A support vector machine performed the actual

detected) and classified according to their suitability for picking. For

truth position. The identified classes should include at a minimum (a)

These solutions are not appropriate for iceberg lettuce. Color

worker with a knife. The worker tilts the head of the lettuce and then

uses a high impulse maneuver to cut the stem of the lettuce. The

systems. Harvesting is a challenging task to automate and a recent review

supermarket‐quality cut. The lettuce must have a stem of the correct

performed, but little has filtered through into the commercial world. The

browning and have no damage to outer leaves. Additionally, if outer

under 10 s, which sets the benchmark for a robotic harvesting system.

lettuce stalk and retract, while the gripper actuator causes the soft gripper to grasp and release the target lettuce. The mobile platform supports the above hardware items and is moved manually around the field. The system is powered by a generator, which provides sufficient power to meet the peak

demands of the system. An air compressor is used to enable actuation of the pneumatic systems. The generator and compressor can sit on the Vegebot to allow the system to be completely mobile.

Appendix B. The web‐based user interface is shown in Figure B1b.

UR10 robot arm, two cameras, and a custom end effector, all housed on a mobile platform for field testing. A block diagram showing the integration of the system is shown in Figure 3. Vegebot contains two cameras: an overhead camera positioned approximately 2 m above the ground and another end‐effector camera mounted inside the end effector. Both are ordinary, low‐cost USB webcams and stream video to the control laptop. Together, these allow Vegebot to detect (localize and classify) lettuces, and to move the end effector into position. There are additional sensors built into the robot arm: the standard joint encoders and a force‐feedback sensor that records the force and torque being applied to the end effector. The UR10 arm provides a wide range of movements, and provides force and torque information allowing force feedback to be implemented. A commercial implementation would likely have simpler arms each with an end effector, all operating in parallel (for an example of such a system, see Scarfe et al., 2009). The control laptop controls the end effector using two digital I/O lines routed through the UR10 arm. These switch the two pneumatic actuators on and off, the blade actuator causing the blade to slice through the

3.2.1 | Control and processes The processes for training and operating Vegebot can be analyzed at three levels (see Figure 4). At the highest level, the learning cycle, data sets are gathered for the initial training of the vision system, harvesting is performed and additional data are gathered. As soon as enough new data are gathered to merit it, the system can be retrained. In this way, the accuracy and generalization abilities of the Vegebot can in principle be improved as images are obtained from new fields and under different weather conditions. The testing of these improvements is the subject of a future paper. The harvesting session outlines the structure of the work in the field. First the Vegebot is moved along the lettuce lanes (seen in Figure 2) to bring approximately 10 lettuces within the robot’s workspace and field of view. The current iteration of Vegebot is simply manually pushed into position. Next, the Vegebot is optionally calibrated, using the method described in Section 4.1.3. Calibration is always performed at the start of a session and then on an as‐needed basis as discrepancy

F I G U R E 4 Processes for training and operation of the Vegebot, showing the key processes in green. The trajectory diagram for the lowest level pick sequence is shown in Figure 14 [Color figure can be viewed at wileyonlinelibrary.com] between the lettuce position inferred by the overhead camera and that detected by the end‐effector camera increases.

inaccurate to a greater or lesser degree. At this point, the camera in the end effector takes over to fine‐tune the end‐effector position

to be directly over the center of the lettuce. The end effector then

overhead camera. A human then selects a lettuce by clicking on the user

interface. This was a manual process during the experiments for the

sake of safety. Selection could be automated with a trivial modification.

downward trajectory. The soft gripper is then activated and grasps

the lettuce. Next, the blade actuator is activated and the blade

onto the platform. Once the reachable lettuces have been picked, the

moves horizontally and cuts through the lettuce stalk. Still grasping

Vegebot can either be moved to a new position or the session finished.

surrounding lettuces. The arm then moves the end effector to a

camera. Because of the rugged nature of the environment and the

F I G U R E 6 The vision system pipeline showing the two stages of convolutional neural network. First, the lettuces are localized using one network. A second network using both the lettuces localized from the first network and presegmented lettuce images from a classification data set is used [Color figure can be viewed at wileyonlinelibrary.com] in the agriculture environment (and are shown in green boxes in

conditions. All these operations must be performed in close to real time given that Vegebot uses localization information dynamically to fine‐

tune the trajectory of its end effector. In principle, any of the latest deep‐learning based object detectors could fulfill this function. Candidates such as YOLOv3 and Faster R‐ CNN (Redmon & Farhadi, 2018; Ren, He, Girshick, & Sun, 2015) can

very small close‐together objects) was irrelevant in this use case. Fast

neighboring lettuces. The outdoor lighting conditions also vary

brightness and contrast. The lettuces need to be classified as “harvest

lettuce categories, there would be little more to do. In the present

project there were only two data sets available. The first was a

F I G U R E 7 Development of lettuce harvesting end effectors. (a) Two‐handed approach with one hand to hold the lettuce, one hand with knife, (b) rotary DC motor cutting mechanisms, (c) linear actuator knife‐powered mechanism, and (d) pneumatic cutter chosen as the best mechanism [Color figure can be viewed at wileyonlinelibrary.com]

F I G U R E 8 The final end effector developed, showing the belt drive mechanisms and dual pneumatic actuator system [Color figure can be viewed at wileyonlinelibrary.com] added manually. This data set (detailed in Table 2) was rich in

underrepresented. The second data set originated from a previous

represent the position and location of exemplars of all classes.

for detection. This latter strategy runs the risk of the network

F I G U R E 1 0 (a) The requirements for successfully lettuce harvesting determined by the physical end effector. The lettuce center must be detected within a distance such that the lettuce is fully within the footprint of the end effector when cutting. (b) The distribution of accuracy of the lettuce localization system for the two different cameras used, with images from sub‐data sets C and E, respectively [Color figure can be viewed at wileyonlinelibrary.com]

learning to detect artefacts in the synthetic images, rather than genuinely localizing the vegetables based on natural visual cues.

output their bounding boxes. Narrow bounding boxes, likely

sets. The first network, a YOLOv3 object detector would be used

of the arm, are rejected as candidates. Each of the remaining

F I G U R E 1 1 Localization performance with varying brightness and image contrast. The precision and recall are given in both cases. The images below show the contrast and brightness enhancement added applied to a typical image in the test data set [Color figure can be viewed at wileyonlinelibrary.com]

F I G U R E 1 2 Examples of the localization system working on different lettuce and with camera setups with different heights and angles and showing usage on different crops and different fields demonstrating robustness. Blue bounding boxes indicate the entire head of lettuce could be seen, green indicate where only part of the head is visible [Color figure can be viewed at wileyonlinelibrary.com]

F I G U R E 1 3 (a) Accuracy of the classification network with changes in image brightness and image contrast. (b) The confusion matrix showing the classification performance of lettuce [Color figure can be viewed at wileyonlinelibrary.com]

F I G U R E 1 4 End‐effector trajectories when undergoing the field experiments. It shows all trajectories centered on cutting (at 0 s) and an example representative trajectory. The vertical divisions correspond to the different stages of the pick sequence from Figure 4 [Color figure can be viewed at wileyonlinelibrary.com]

localization data set was collected, labeled, and assembled. Images

Network was applied to each. Finally, bounding boxes predicted by

phones and webcams. Figure 5 shows the process of obtaining

approach offers greater performance of both localization and

classification. The architecture has been chosen to achieve the

to the different field experiments in which they were obtained.

assembled data set was well balanced. Figure 6 shows some

sample images from each of the five data sets. The images cover

not. By first detecting the bounding boxes and then cropping each

are factors that can vary during lettuce harvesting. Table 2 gives a

for the classification network. This improves the likelihood of a

and image quality. Image quality refers to the subjectively

correct classification on images from the overhead camera.

passed to the second stage. Assuming 10 candidate lettuces per

of the bounding box are 10% larger than the lettuce head. Only the

lettuces whose heads are fully included in the image were labeled.

adjustments. The end‐effector camera typically has only one lettuce

in view during fine‐tuning, reducing the detection time to 0.095 s.

limiting step. The pipeline processes images from both overhead and

end‐effector cameras. The overhead camera provides candidates for

approach of the end effector to the desired lettuce.

detect lettuces at the edges as well. Classifying these partial

the reach of the Vegebot robot arm and therefore they were rejected from the detected candidates. There were also cases

Training a deep CNN object detector requires a large amount of data.

ones. Lettuce rejection algorithms were implemented to reject

such candidates. A candidate was rejected if it met either of the

scenarios the Vegebot would encounter. Since there was no existing

Background

being the longer of the two. L and W are the width and height of the

required. The problem encountered was that the system worked

iterations. The network was trained on a PC with a 4.5 GHz Intel i7‐

the field. Even small deviations in the position of the overhead

around 12 hr. Pretrained weights based on ImageNet were used. No

data augmentation was applied: This could improve localization performance and remains for future work.

A different approach was therefore attempted, where the robot could self‐calibrate the transformation from viewport pixels to arm position, using Aruco markers positioned on the top of the end effector. An occasional self‐calibration would be sufficient to reset

the transformation, for example, after moving the platform. Calibration also resets the target location of the lettuce center within the

viewport of the end‐effector camera. We assume the platform is kept

from the previous localization step. Immature and infected lettuces

which them Vegebot moves. Further details of the final calibration

should be left in the field. False‐negative localization results can be

harvesting of lettuce with minimal damage to the lettuce. To meet

the data set. Figure 6 shows sample images from each of the four

of stem. The outer leaves of the lettuce should also be removed

classes. Table 3 is an overview of the size of the data set. The 665

(12.5%) sets. A higher portion of images were allocated to the

lettuce harvesting. The UR10 arm is mounted on a mobile base which

training set deliberately due to the limitation of the images available.

harvesting procedure. To minimize the damage to the lettuce and

trained to 260 iterations. The training was on the same hardware as

two mechanisms has been used. First, a soft clamping method is used

to hold the lettuce throughout cutting and when lifting. Secondly, a cutting mechanism is required to cut the stem of the lettuce at a given height. The cutting mechanism requires force (≈20 N) to cut

The Darknet classifier has no separate validation data set; the experimenter chooses the length of training based on periodically evaluating against the test set. For the robustness evaluation below, fresh data was used.

through the stem and outer leaves, while also requiring height adjustability and also a straight linear cut.

uncertain, and unknown. To achieve this, the ground was used as a fixed

pneumatic actuation, belt drive, and rotary chopping. Figure 7 shows

the surface. Using force feedback from the joints of the UR10 robot

required a high level of coordination between the two arms. A rotary

could be assumed. The cutting height relative to the ground can be

adjusted by manually varying the height of the cutting mechanism. A

led to the mechanism having to hack at the stem. Although the linear

leading to poor cut quality. The pneumatic cutting mechanics

this application where a fast clean cut is required. Although there is

the end effector was in contact and level with the ground. This approach

fixed gripper lined with foam. Similar to other harvesting end

interfered with the cutting mechanism. This also allows the end effector

to self‐level on the ground, and provided stability and consistency. Small

and prevent it from pressing too low into the ground. This approach

different soil heights relative to the tractor track heights.

valve which has two position controls. Two digital outputs from

control. A timing belt system was used to transfer the linear motion

the UR10 end effector are used to control the valves. After the

movement. This allows the actuator to be mounted above the height

of the lettuce, such that when cutting it does not interfere. The belt

is held in a fixed place. The cutter pneumatic system is then

actuated so the blade cuts the stem of the lettuce. The arm can

easily altered by changing the height of the cutting mechanism.

then be lifted, with the knife released and then the grabber retracted to release the lettuce. Besides these two challenges, an additional one was that the weight

of the end effector was at the limit of the payload ability of the UR10. This restricted the arm to moving more slowly than would otherwise be necessary. This will be discussed in the experimental results.

1 MPa, bore 10 mm, stroke 15 cm

1.5 MPa, bore 15 mm, stroke 20 cm

weather conditions and across many (over 10) different fields. In

experiments were undertaken to test the performance of the

in 2016–2018 in lettuce fields in Cambridgeshire, UK, in varying these field trips, the system was developed and tested3.Field localization and classification system in isolation from the harvester. The entire system was also integrated to test the full functioning of the system in conjunction with its physical harvesting abilities. In this 3

These were in collaboration with a major agricultural company, G’s Growers.

section, the localization and classification is presented for both individual and system level tests, after which the harvesting system results are presented. At the beginning of each experimental session, the Vegebot was

Result

assembled at the start of a lettuce lane. Typically, a three person crew participated, one operating the control laptop, one observer, and one checking and resolving any physical issues and enabling the air compressor when required.

When integrated into the full system, the overall performance of the localization system could be tested in harvesting trials. The

recorded. The results from this overall system results include over 60

results of all lettuce that could be visible observed by the system

were recorded. The results are shown in Table 5.

the scale of the image. This threshold is illustrated by Figure 10a.

system. By skipping immature heads and avoiding unnecessary

harvesting the efficiency of the harvester can be maximized. To test

experiments (modified for brightness and contrast) were passed to

the classification network and the accuracy recorded. The results are

the detected and ground truth of the lettuce center was found. The

shown in Figure 13a. For classification, the network showed greatest

opposed to brightness. Images taken in bright sunlight were high

images in the data set to train for low brightness. Judicious data

in Figure 13b. The diagonal shows the correctly classified lettuce,

precision and recall were then found. The system showed a high

background, infected and harvest‐ready lettuce. Identifying infected

field conditions), with minimal changes in precision and recall. For the

recall dropped significantly for high changes in contrast. It is likely

lettuces. One of the reasons is that the boundary between harvest‐

Figure 12 shows some examples of the localization results. Figure

set is challenging. The classification data set was labeled under the

which for the majority of the time is the harvesting requirement. On

reject lettuces which are on the edge of the image. Localization was

When entire system tests of the Vegebot were later ran in the field, the system provide 100% accuracy when classifying lettuce.

parts of the harvesting process. The breakdown of the time series

coordinates are shown with respect to the base of robot platform, with X pointing forwards in the direction of travel, Y pointing to the left, and Z pointing up.

end effector weight on the robot arm. This led to an average cycle

previous visits to the field with well over 300 lettuce harvested. The

cutting, required only 2 s. Thus, using a lighter end effector, for

rows. Each lettuce position, and false positives or negatives were

recorded, together with the number and trajectory of all pick attempts.

the force threshold is met. This shows that the end height of arm

stalk being cut too close to the lettuce body. In total, 69 lettuces were

harvesting attempted with 31 lettuce harvested successfully. A video

detected by the vision system. Of these, attempts were made to

pick 60, the remainder being out of range of the robot arm. Thirty‐

that it was physically not possible to pick some lettuce. If the

limitations of the arm are ignored, and the denominator reflects only

black. This representative trajectory shows a single experiment

T A B L E 6 Overall system performance in the harvesting tests. Total lettuces attempted considers only lettuces within restrictions imposed by arm strength

Result

exception, if the arm could reach the lettuce, the end effector could pick it. Although this is a considerable exception, it could be simply

achieved by using a robot arm with increased torque output.

harvester for commercial operation. Existing challenges include visual

analysis, precise manipulator control, harvesting rig development, and

reduction of the overall cycle time and costs. In this study the focus

outer leaves or damage. The distribution of the lettuces which

iceberg lettuce, but many other crops. This section discusses the

supermarket perfection. Additionally, in some cases extra cuts were

approaches can be used to aid future work in this field.

required. This was often due to the leaves of the lettuce and

movement of the lettuce head within the cutting area. Additionally,

countless lab based experiments. In each iteration, new software and

The average cycle time was 31.7 s, with a variance of 32.6 s.

results compared. The development approach adopted was to

weight of the end effector. Of the trajectory sections in Figure 14, all

of the architecture systematically. Frequent field tests were used to

arm’s payload capacity. A much reduced cycle time should be

provide feedback and to identifying the improvements required. As a

achievable with a stronger arm or lighter end effector. In addition,

progress. The authors believe that this iterative approach is more

sets of lettuces were not ideally suited for an optimal vision system.

would have been combined into one integrated whole. Rather than

cases slightly too close to the lettuce head. Of the 32 picks, only two

actually resulted in inedible lettuces. Improvement can probably be

use of what was available. This enabled the robot to detect lettuces

on the overall system to continue. With future iterations and online

Again, buyer standards dictate that a packaged lettuce should not have too many superfluous leaves in the packaging. At present, a human

data‐gathering this architecture could be simplified once again into a single, fully‐integrated CNN architecture.

the lettuce onto the harvesting rig. The end effector left the picked

architecture was able to achieve the localization results that it did,

given the difficulty of the task for a human harvester. Many of the

these standards. These would have to be removed further down the

feature extraction in Kusumam et al. (2016) and radicchios using hand‐

shelves. Until the robot improves, this suggests a dual pricing

significant test data set. The average cycle time on Vegebot (31.7 s)

world commercial conditions. Vegebot operates in the same fields and

along the same lane layout as human harvesters. Neither the

versions made from lighter materials. Although the harvest success

the automated harvesting. By contrast, solutions using water knives

work is required to reduce the damage rate. Further optimization is

major changes to existing practices. The control and calibration

robustly in the field. Sensors were stripped out, not added. Complex

opposed to creating a bespoke system for this particular problem.

the ground, giving the robot a simple signal on when to cut. A design

or software module was eliminated. In the long term, this preference for

approach can make best use of the available data sets and can

has already achieved important results. The use of standard metrics as

proposed by Bac et al. (2014) kept the project on track and focused on

steady, incremental improvements. The authors feeling is that the

exploited. This has been shown to help achieve a consistent cutting

height. This use of the environment, and designing mechanical

different to many other approaches. This presents an approach to achieve robustness in challenging agricultural environments.

the harvested vegetables were perfectly edible. The most recent

possibility. While its capacity would clearly be more limited, it would

demand. Marshaling a human team and a harvesting rig can be difficult

the cut is made. In parallel, the end effector needs to be made lighter

field to fulfill them. Outside of harvesting time, it could also be used for

data gathering. The vision and learning system in combination with the

ing. This could increase crop and harvesting efficiency.

useful in other harvesting projects. The authors key recommendation

and time efficiency are key. To make the presented approach viable,

the cycle time would need to be reduce to that comparable to humans.

and using the standard metrics to stay on track.

However, using a robotic system would enable certain advantages such as a more flexible work force and nighttime operation. The techniques and approaches here have been applied to iceberg lettuce;

however, the concepts could be applied to other harvesting and robotic agriculture situations. Further work to investigate wider

approach to harvesting iceberg lettuces. The vision system, mechanics, and control strategy were described and the experimental results detailed.

avoid damage to harvested lettuces. The localization and classifica-

Growers), EPSRC Small Partnership AwardRG86264 (in collaboration with G’s Growers), and the BBSRC Small Partnership GrantRG81275. In addition, we are extremely grateful from the support and valuable time input from G’s Growers, in particular Charlie Kisby, John Currah, James Green, and Jacob Kirwan. We would also like to thank Dr. Alex Jones from the Sainsburys Laboratory and many who have contributed to the iterations of Vegebot: Luca Scimeca, Andre Rosendo, Fabio Giardina, Claudio Ravasio, and Vivian Wong.
