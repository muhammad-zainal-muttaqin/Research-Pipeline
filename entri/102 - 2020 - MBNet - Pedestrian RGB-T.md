# 102 - Improving Multispectral Pedestrian Detection by Addressing Modality Imbalance Problems

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2020mbnet` |
| Judul asli | Improving Multispectral Pedestrian Detection by Addressing Modality Imbalance Problems |
| Penulis | Kailai Zhou, Linsen Chen, Xun Cao |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020), hlm. 787–803 |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2008.03043
- **Kode sumber resmi:** https://github.com/CalayZhou/MBNet
- **Google Scholar:** https://scholar.google.com/scholar?q=Improving%20Multispectral%20Pedestrian%20Detection%20by%20Addressing%20Modality%20Imbalance%20Problems
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Improving%20Multispectral%20Pedestrian%20Detection%20by%20Addressing%20Modality%20Imbalance%20Problems&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan MBNet (*Modality Balance Network*), detektor pejalan multispektral yang menggabungkan citra warna (RGB) dan citra termal (*thermal*, inframerah panjang gelombang panjang atau *LWIR*) untuk tetap berfungsi pada kondisi pencahayaan kurang. Kontribusi utamanya adalah mengenali dan menangani secara eksplisit apa yang disebut penulis sebagai masalah ketidakseimbangan modalitas (*modality imbalance*): kualitas dan keandalan sinyal RGB serta termal tidak setara, dan tingkat ketidaksetaraan itu berubah-ubah tergantung waktu dan kondisi cahaya. Dua modul baru diusulkan untuk mengatasinya: *Differential Modality Aware Fusion* (DMAF), yang menyaring informasi pelengkap antar-modalitas pada level fitur, dan penyelarasan fitur sadar-iluminasi (*illumination-aware feature alignment*), yang menyesuaikan bobot tiap modalitas menurut kondisi cahaya sekaligus mengoreksi pergeseran spasial antara citra RGB dan termal.

Pada tolok ukur KAIST, MBNet mencapai tingkat kesalahan deteksi (*miss rate*, MR — makin kecil makin baik) 8,13% untuk kondisi siang-malam gabungan, mengungguli metode pembanding terbaik sebelumnya. Pada tolok ukur CVC-14, MBNet juga kompetitif meski dataset ini memiliki masalah misalignment RGB-termal yang jauh lebih parah. Makalah ini melanjutkan garis kerja klaster Pedestrian RGB-T dalam tinjauan ini: ia dibangun di atas persoalan misalignment yang mula-mula didokumentasikan oleh dataset KAIST (bab 100) dan atas gagasan pembobotan sadar-iluminasi yang dirintis IAF R-CNN (bab 101), tetapi menambah satu lapis penanganan baru, yaitu ketidakseimbangan keandalan antar-modalitas itu sendiri.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi pejalan berbasis RGB gagal pada malam hari atau kondisi cahaya rendah karena kontras objek terhadap latar menjadi sangat lemah. Citra termal, yang merekam pancaran panas tubuh, tetap informatif pada kegelapan karena tidak bergantung pada cahaya tampak, tetapi kehilangan detail tekstur dan warna yang berguna pada siang hari. Motivasi dasar deteksi pejalan multispektral (RGB-T, gabungan pasangan citra RGB dan termal yang diambil serentak) adalah menggabungkan keduanya sehingga kekurangan satu modalitas ditutupi modalitas lain.

Dataset KAIST (bab 100) menyediakan pasangan citra RGB-termal ini, tetapi karena kedua kamera dipasang pada posisi fisik berbeda, letak objek yang sama pada kedua citra tidak persis sejajar — persoalan yang disebut *misalignment* spasial. IAF R-CNN (bab 101) menjadi salah satu pendekatan pertama yang menyadari bahwa kondisi cahaya semestinya mengubah seberapa besar tiap modalitas dipercaya, dan menambahkan bobot bergantung iluminasi pada skor akhir tiap cabang. Meski begitu, penulis MBNet berargumen bahwa pendekatan semacam itu masih memperlakukan RGB dan termal secara simetris dalam proses pelatihan jaringan: kedua cabang dioptimalkan dengan gradien yang setara, padahal keandalan sinyal keduanya sebenarnya tidak pernah setara pada saat tertentu. Ketimpangan gradien ini disebut masalah ketidakseimbangan modalitas — salah satu modalitas cenderung mendominasi arah pembelajaran fitur gabungan, sehingga jaringan tidak benar-benar belajar memakai kedua sumber informasi secara optimal pada setiap kondisi. Masalah kedua yang dianggap belum tertangani tuntas adalah misalignment: penyelarasan berbasis kalibrasi kamera statis tidak dapat mengikuti pergeseran objek bergerak yang berjarak berbeda-beda dari kedua kamera.

## Ide Utama

MBNet menambahkan dua mekanisme pada tahap ekstraksi fitur, bukan hanya pada tahap penggabungan skor akhir. Pertama, pada tiap tahap konvolusi, jaringan menghitung selisih langsung antara peta fitur RGB dan peta fitur termal, kemudian memakai selisih ini untuk membentuk sinyal pelengkap yang disuntikkan kembali ke kedua cabang. Gagasannya: bagian yang berbeda antara dua modalitas adalah justru bagian yang saling melengkapi, sedangkan bagian yang sama sudah tersedia di kedua sisi sehingga tidak perlu ditransfer ulang. Mekanisme ini adalah modul DMAF.

Kedua, sebelum fitur kedua modalitas digabungkan untuk menghasilkan kotak deteksi akhir, sebuah subjaringan kecil menaksir tingkat iluminasi citra RGB dan mengeluarkan satu nilai bobot. Bobot ini menentukan seberapa besar kontribusi RGB dibandingkan termal pada tahap berikutnya — pada malam hari nilai ini bergeser ke termal, pada siang hari bergeser ke RGB. Bersamaan dengan itu, submodul penyelarasan memprediksi pergeseran piksel (dx, dy) tiap wilayah agar fitur termal digeser ke posisi yang sesuai dengan fitur RGB sebelum digabung, sehingga kesalahan akibat misalignment tidak terbawa ke prediksi akhir.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dasar

MBNet dibangun di atas kerangka SSD (*Single Shot Detector*, detektor satu tahap yang memprediksi kotak langsung dari peta fitur multi-skala tanpa tahap pengusulan wilayah terpisah), dengan *backbone* (jaringan penyari fitur utama) ResNet-50, yaitu jaringan konvolusi 50 lapis dengan sambungan pintas (*residual connection*) yang menjumlahkan masukan suatu blok ke keluarannya agar gradien mudah mengalir pada jaringan dalam. Citra RGB dan citra termal, masing-masing berukuran 640×512 piksel, dilewatkan melalui dua cabang ResNet-50 paralel yang tidak berbagi bobot. Pada tiap blok ResNet, modul DMAF disisipkan untuk saling menukar informasi pelengkap antar-kedua cabang sebelum masuk ke blok berikutnya.

Deteksi berjalan dalam dua tahap berurutan (kaskade): tahap *Anchor Proposal* (AP) menghasilkan kandidat kotak awal dari fitur gabungan tahap pertama, dan tahap *Illumination Aware Feature Complement* (IAFC) menyaring ulang kandidat tersebut memakai fitur yang sudah dibobot iluminasi dan diselaraskan secara spasial. Ambang *IoU* (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak, dipakai untuk menilai kecocokan kotak prediksi dengan kotak kebenaran) yang dipakai untuk menentukan kandidat positif berbeda pada tiap tahap: {0,3; 0,5} pada tahap AP dan {0,5; 0,7} pada tahap IAFC — ambang yang makin ketat pada tahap kedua membuat kotak akhir dituntut semakin presisi.

Diagram berikut merangkum aliran data dari dua citra masukan hingga kotak deteksi akhir:

```
citra RGB 640x512              citra termal 640x512
      |                              |
  [ResNet-50 cabang RGB]  <-DMAF->  [ResNet-50 cabang termal]
      |    (ditukar di tiap blok)         |
      +-------------------+--------------+
                          |
                 tahap 1: Anchor Proposal
                  (IoU positif: 0,3 / 0,5)
                          |
        RGB kecil -> jaring iluminasi -> bobot w
        fitur RGB x w   ,   fitur termal x (1-w)
        submodul penyelarasan -> geser (dx, dy)
                          |
              tahap 2: Illumination Aware
                 Feature Complement (IAFC)
                  (IoU positif: 0,5 / 0,7)
                          |
             kotak pejalan + skor akhir
```

### Modul Differential Modality Aware Fusion (DMAF)

Pada tiap titik penyisipan, DMAF menerima sepasang peta fitur — satu dari cabang RGB, satu dari cabang termal, berukuran sama. Selisih keduanya dihitung langsung (fitur RGB dikurangi fitur termal, dan sebaliknya), lalu selisih ini dirangkum per kanal memakai *global average pooling* (merata-ratakan nilai spasial tiap kanal menjadi satu angka per kanal). Hasilnya dilewatkan fungsi aktivasi tanh (menghasilkan bobot antara −1 dan 1 per kanal) untuk membentuk vektor bobot yang menandai kanal mana yang paling banyak menyimpan informasi pelengkap. Vektor bobot ini kemudian dipakai untuk menskalakan ulang fitur, dan hasilnya dijumlahkan kembali ke masing-masing cabang lewat sambungan residual — bukan menggantikan fitur asli, melainkan menambah informasi dari modalitas lawan yang sebelumnya tidak dimiliki cabang tersebut.

### Penyelarasan Fitur Sadar-Iluminasi

Subjaringan iluminasi menerima versi citra RGB yang diperkecil resolusinya sebagai masukan dan mengeluarkan satu nilai skalar yang menaksir tingkat terang citra (dilatih dengan label siang/malam sebagai bentuk pengawasan tambahan, disebut *illumination loss*). Nilai ini menjadi gerbang (*gate*) yang mengalikan fitur RGB dan (1 − nilai tersebut) mengalikan fitur termal sebelum keduanya digabung pada tahap IAFC, sehingga kontribusi tiap modalitas otomatis berubah mengikuti kondisi cahaya tanpa aturan tetap yang ditulis tangan. Terpisah dari mekanisme bobot ini, submodul penyelarasan modalitas memprediksi dua nilai pergeseran piksel (dx, dy) untuk tiap wilayah kandidat, kemudian menerapkan interpolasi bilinear (menghitung nilai piksel baru dari empat piksel tetangga terdekat) untuk menggeser fitur termal ke posisi yang selaras dengan fitur RGB pada wilayah itu. Dengan begitu, kesalahan posisi akibat kedua kamera yang tidak sejajar dikoreksi per wilayah, bukan dengan satu transformasi tetap untuk seluruh citra.

### Fungsi Rugi dan Pelatihan

Fungsi rugi total menjumlahkan tiga komponen: rugi iluminasi (mengawasi keluaran subjaringan iluminasi terhadap label siang/malam), *focal loss* untuk klasifikasi (memberi bobot lebih besar pada contoh sulit agar kelas latar yang jumlahnya jauh lebih banyak tidak mendominasi gradien), dan *smooth L1* untuk regresi koordinat kotak (kombinasi galat kuadrat dan galat mutlak yang lebih tahan terhadap nilai pencilan). Pelatihan memakai optimizer Adam dengan laju belajar 0,0001, ukuran *batch* 10, selama 7 *epoch* (putaran penuh atas data latih), dengan augmentasi distorsi warna acak dan pembalikan horizontal pada citra masukan.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dataset KAIST, tolok ukur standar deteksi pejalan multispektral yang berisi pasangan video RGB-termal siang dan malam (dibahas rinci pada bab 100), serta pada dataset CVC-14, pasangan RGB-termal yang dikenal memiliki misalignment spasial lebih parah karena kedua kamera dipasang lebih berjauhan. Metrik yang dipakai adalah *miss rate* (MR) pada subset "reasonable" (mengecualikan pejalan yang sangat kecil atau tertutup sebagian besar) dengan ambang IoU 0,5 — semakin rendah MR semakin baik.

Pada KAIST, MBNet mencatat MR 8,13% untuk kondisi gabungan siang-malam, 8,28% untuk siang, dan 7,86% untuk malam. Sebagai pembanding, metode sebelumnya IAF R-CNN (bab 101) mencatat MR 15,73%, IATDNN+IASS 14,95%, CIAN 14,12%, dan AR-CNN — metode dengan penanganan misalignment eksplisit yang sebelumnya menjadi acuan terbaik — mencatat 9,34%. Selisih sekitar 1,2 poin MR antara MBNet dan AR-CNN menunjukkan bahwa penanganan ketidakseimbangan modalitas memberi perbaikan tambahan di atas penanganan misalignment saja. Pada ambang IoU yang lebih ketat (0,75), MR keseluruhan naik jauh menjadi kisaran 60%, memperlihatkan bahwa presisi lokalisasi kotak — bukan sekadar keberadaan objek — tetap menjadi bagian tersulit dari tugas ini.

Studi ablasi (pengujian dengan menghapus atau menambah komponen satu per satu) pada KAIST menunjukkan kontribusi tiap modul: model dasar tanpa DMAF maupun penyelarasan mencatat MR keseluruhan 11,93%; penambahan DMAF saja menurunkannya ke 10,96%; penambahan modul penyelarasan spasial menurunkannya lagi ke 10,53%; dan penambahan gerbang iluminasi membawa MR ke 9,36% sebelum kombinasi penuh mencapai 8,13%. Pola ini konsisten menurun pada tiap penambahan komponen, mendukung klaim bahwa DMAF dan penyelarasan sadar-iluminasi memberi kontribusi independen, bukan saling tumpang tindih. Pada CVC-14, MBNet mencatat MR sekitar 24,7% (siang), 13,5% (malam), dan 21,1% (gabungan), sebanding atau lebih baik dari metode sezaman meski dataset ini menghadirkan misalignment yang lebih parah. Dari sisi kecepatan, makalah melaporkan waktu inferensi sekitar 0,07 detik per citra, setara kurang lebih 14 *frame* per detik — jauh di bawah kecepatan detektor satu tahap RGB murni seperti YOLO (bab 001), konsekuensi dari pemrosesan dua cabang paralel ditambah kaskade dua tahap.

## Kelebihan dan Keterbatasan

Kelebihan utama MBNet adalah penanganan ketidakseimbangan modalitas pada level fitur, bukan hanya pada skor akhir seperti pendekatan sebelumnya, dan bukti ablasi yang menunjukkan tiap modul menyumbang perbaikan terukur secara terpisah. Penyelarasan spasial per wilayah, alih-alih kalibrasi global tetap, juga membuat metode ini tetap berfungsi pada CVC-14 yang misalignment-nya lebih besar dari KAIST.

Dari sisi rekayasa, kaskade dua tahap dengan dua cabang ResNet-50 paralel menambah jumlah parameter dan biaya komputasi dibandingkan detektor satu tahap tunggal, tercermin pada kecepatan 14 FPS yang jauh dari real-time tinggi. Secara konseptual, subjaringan iluminasi hanya menghasilkan satu bobot skalar dari citra RGB berresolusi rendah, sehingga taksiran kondisi cahaya bersifat global per citra, bukan per wilayah — dua pejalan pada wilayah gelap dan terang dalam citra yang sama menerima bobot iluminasi yang sama. MBNet juga tetap bergantung pada ketersediaan kedua modalitas secara bersamaan pada saat inferensi; skenario dengan satu modalitas hilang tidak dibahas dalam kerangka ini.

## Kaitan dengan Bab Lain

MBNet mewarisi persoalan misalignment yang pertama kali dijadikan sorotan oleh dataset KAIST pada [bab 100](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md), dan melanjutkan gagasan pembobotan sadar-iluminasi yang dirintis [bab 101 (IAF R-CNN)](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md), dengan menambahkan penanganan ketidakseimbangan modalitas pada level fitur konvolusi lewat DMAF — sesuatu yang belum ditangani IAF R-CNN yang hanya membobot skor akhir. Karya-karya sesudahnya dalam klaster ini melanjutkan arah berbeda: [bab 103 (GAFF)](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md) menata ulang mekanisme fusi memakai *attention* lintas-modal, [bab 104 (Cyclic Fuse-and-Refine)](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md) mengusulkan fusi berulang antar-tahap, dan [bab 105 (CMPD)](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md) memakai ketidakpastian statistik untuk memandu bobot antar-modal — arah yang dapat dibaca sebagai kelanjutan langsung dari masalah ketidakseimbangan modalitas yang pertama kali dirumuskan eksplisit oleh MBNet. Prinsip pembagian bobot berdasarkan keandalan sinyal ini juga relevan bagi klaster RGB+Depth dalam tinjauan, terutama saat sinyal kedalaman tidak selalu andal, sebagaimana dibahas pada [bab 106 (RGB-D Fusion for Detection)](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md).

## Poin untuk Sitasi

Kutip dengan kunci `zhou2020mbnet`. Ringkasan yang aman dikutip: "MBNet menangani ketidakseimbangan modalitas pada deteksi pejalan multispektral RGB-termal lewat modul Differential Modality Aware Fusion dan penyelarasan fitur sadar-iluminasi, mencapai miss rate 8,13% pada dataset KAIST (subset reasonable, siang-malam gabungan), mengungguli AR-CNN (9,34%) dan metode sezaman lain seperti CIAN dan IAF R-CNN." Angka MR KAIST (8,13%/8,28%/7,86%; pembanding IAF R-CNN 15,73%, IATDNN+IASS 14,95%, CIAN 14,12%, AR-CNN 9,34%) dan kecepatan inferensi (~14 FPS) berasal dari naskah dan cukup dapat diandalkan. Angka studi ablasi tahap demi tahap (11,93% → 10,96% → 10,53% → 9,36% → 8,13%) dan angka CVC-14 (24,7%/13,5%/21,1%) diperoleh lewat pembacaan otomatis naskah HTML, bukan pembacaan langsung tabel oleh penulis bab ini — keduanya sebaiknya dicocokkan ulang terhadap Tabel 2/3 pada PDF asli sebelum dikutip dalam karya formal.
