# 106 - RGB and Depth Image Fusion for Object Detection Using Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `farahnakian2021fusion` |
| Judul asli | RGB and Depth Image Fusion for Object Detection Using Deep Learning |
| Penulis | Fahimeh Farahnakian, Jukka Heikkonen |
| Tahun | 2021 |
| Venue | Bab buku dalam *Deep Learning Applications, Volume 3* (Advances in Intelligent Systems and Computing, vol. 1395), Springer, hlm. 73–93 |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **Google Scholar:** https://scholar.google.com/scholar?q=RGB%20and%20Depth%20Image%20Fusion%20for%20Object%20Detection%20Using%20Deep%20Learning
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=RGB%20and%20Depth%20Image%20Fusion%20for%20Object%20Detection%20Using%20Deep%20Learning&sort=relevance
- **SpringerLink (bab, berbayar):** https://link.springer.com/chapter/10.1007/978-981-16-3357-7_3

## Gambaran Umum

Bab ini ditulis oleh Fahimeh Farahnakian dan Jukka Heikkonen dan terbit sebagai bagian dari buku *Deep Learning Applications, Volume 3* (Springer, 2021), sebuah kumpulan versi perluasan dari makalah terpilih pada *19th IEEE International Conference on Machine Learning and Applications* (ICMLA 2020). Bab ini adalah versi perluasan dari makalah konferensi kedua penulis yang sama, "A Comparative Study of Deep Learning-based RGB-depth Fusion Methods for Object Detection" (ICMLA 2020), dan berkaitan erat dengan makalah pendamping mereka "RGB-depth Fusion Framework for Object Detection in Autonomous Vehicles" (ICSPCS 2020).

Persoalan yang diangkat adalah bagaimana menggabungkan citra RGB dengan informasi kedalaman (*depth*) untuk memperbaiki deteksi objek berbasis *deep learning*, dan pada tahap arsitektur mana penggabungan itu paling baik dilakukan. Titik pembeda penting dari banyak studi fusi RGB-D lain adalah sumber kedalamannya: alih-alih memakai sensor kedalaman khusus (mis. kamera RGB-D atau LiDAR), kedalaman diperoleh dengan mengestimasinya langsung dari citra RGB tunggal memakai jaringan estimasi kedalaman monokuler tanpa pengawasan (*unsupervised monocular depth estimation*), sehingga metode ini dapat dipakai pada kamera RGB biasa. Pengujian dilakukan pada dataset KITTI, tolok ukur standar untuk persepsi kendaraan otonom. Temuan utamanya: menggabungkan RGB dengan peta kedalaman yang diestimasikan memakai metode MonoDepth memberi akurasi deteksi lebih tinggi daripada detektor yang hanya memakai RGB atau hanya memakai kedalaman.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Detektor objek berbasis CNN yang hanya memakai citra RGB memiliki keterbatasan struktural: kamera RGB merekam intensitas warna piksel, tetapi tidak merekam jarak fisik objek ke kamera. Akibatnya, pada kondisi kompleks — objek yang saling menutupi (*occlusion*), kontras rendah, atau tekstur latar yang mirip dengan objek — detektor RGB murni kehilangan salah satu isyarat pembeda paling kuat yang tersedia bagi manusia maupun sensor 3D: struktur geometris ruang.

Cara konvensional mengatasi hal ini adalah menambahkan sensor kedalaman fisik, seperti kamera RGB-D (mis. Kinect, dipakai pada dataset SUN RGB-D dan NYU Depth) atau LiDAR (dipakai luas pada kendaraan otonom). Kedua sensor ini menambah biaya perangkat keras, konsumsi daya, dan kompleksitas kalibrasi antar-sensor. Untuk kendaraan otonom dan robotika berbiaya rendah, kebutuhan sensor tambahan ini menjadi hambatan praktis. Di sisi lain, penelitian *deep learning* tentang estimasi kedalaman monokuler tanpa pengawasan — melatih jaringan memprediksi peta kedalaman dari satu citra RGB tanpa label kedalaman asli, dengan memanfaatkan konsistensi foto-metrik antar-pasangan citra stereo saat pelatihan — telah matang menjelang 2020, sehingga peta kedalaman dapat diperoleh murni dari perangkat lunak. Pertanyaan yang belum terjawab tuntas saat itu adalah apakah kedalaman hasil estimasi (yang mengandung galat, berbeda dari kedalaman sensor yang presisi) tetap berguna bagi detektor objek, dan pada tahap mana penggabungannya paling efektif.

## Ide Utama

Gagasan inti bab ini adalah memakai kedalaman yang **diestimasi**, bukan diukur langsung oleh sensor, sebagai kanal tambahan bagi detektor objek berbasis CNN, lalu membandingkan secara sistematis dua skema penggabungan (*fusion*) kanal tersebut dengan kanal RGB. Skema pertama, *early fusion* (fusi awal), menggabungkan citra RGB dan peta kedalaman sebelum atau pada lapisan-lapisan awal jaringan, sehingga kedua modalitas diproses bersama oleh satu jalur konvolusi sejak tahap ekstraksi fitur paling dasar. Skema kedua, *late fusion* (fusi akhir), memproses RGB dan kedalaman pada dua cabang jaringan yang terpisah, masing-masing mengekstrak fiturnya sendiri, dan baru menggabungkan keduanya menjelang tahap keputusan (fitur tingkat tinggi atau skor deteksi).

Konsekuensi teknis dari pilihan ini berbeda. Fusi awal murah secara komputasi (satu jalur jaringan) tetapi memaksa jaringan mempelajari relasi RGB-kedalaman sejak fitur tingkat rendah, padahal kedua modalitas memiliki statistik yang berbeda (RGB tiga kanal warna, kedalaman satu kanal jarak). Fusi akhir memberi setiap modalitas jalur pemrosesan yang sesuai karakteristiknya sendiri, dengan biaya dua kali lipat parameter cabang konvolusi. Karena kedalaman berasal dari estimasi (bukan sensor), bab ini juga mengevaluasi dampak metode estimasi kedalaman itu sendiri terhadap hasil akhir deteksi.

## Cara Kerja Langkah demi Langkah

### Estimasi Kedalaman dari Citra RGB Tunggal

Kedalaman diperoleh dengan jaringan estimasi kedalaman monokuler tanpa pengawasan. Jaringan semacam ini dilatih memakai pasangan citra stereo (kiri-kanan) tanpa label kedalaman asli: selama pelatihan, jaringan memprediksi peta disparitas (pergeseran piksel antar-pasangan stereo, yang berbanding terbalik dengan jarak objek) dari citra kiri, lalu peta itu dipakai merekonstruksi citra kanan; selisih antara citra kanan hasil rekonstruksi dan citra kanan asli menjadi sinyal pelatihan. Setelah pelatihan selesai, saat inferensi jaringan hanya membutuhkan satu citra RGB untuk menghasilkan peta kedalaman — tanpa sensor tambahan. MonoDepth adalah salah satu metode kelompok ini yang dievaluasi pada bab ini dan yang, menurut hasil yang dilaporkan, memberi kombinasi terbaik ketika digabungkan dengan RGB untuk deteksi.

### Dua Jalur Penggabungan Modalitas

Diagram berikut membandingkan struktur kedua skema penggabungan pada tingkat blok jaringan:

```
Fusi awal (early fusion)
RGB    ---+
          +--> gabung kanal --> CNN tunggal --> kepala deteksi
Depth  ---+

Fusi akhir (late fusion)
RGB    ---> CNN cabang RGB   ---+
                                 +--> gabung fitur --> kepala deteksi
Depth  ---> CNN cabang depth ---+
```

Pada fusi awal, citra RGB dan peta kedalaman digabungkan sebagai kanal masukan tambahan (analog menambah kanal keempat pada citra RGB tiga kanal) sebelum masuk ke satu tulang punggung (*backbone*) konvolusi tunggal; seluruh lapisan sesudahnya memproses representasi gabungan itu. Pada fusi akhir, RGB dan kedalaman melewati dua tulang punggung konvolusi terpisah yang masing-masing menghasilkan peta fitur sendiri; kedua peta fitur baru digabungkan — misalnya dengan penjumlahan atau penggabungan kanal — pada tahap mendekati kepala deteksi (bagian jaringan yang memprediksi kotak pembatas dan kelas objek). Kepala deteksi pada kedua skema bertugas sama: dari representasi gabungan, memprediksi lokasi kotak pembatas dan kelas objek untuk tiap kandidat wilayah citra.

### Prosedur Pengujian

Kedua skema fusi dilatih dan diuji pada dataset yang sama agar perbandingan adil: masukan RGB dan peta kedalaman hasil estimasi identik untuk kedua skema, hanya titik penggabungannya yang berbeda. Sebagai pembanding tambahan, bab ini turut melatih detektor yang hanya memakai RGB dan detektor yang hanya memakai peta kedalaman, sehingga kontribusi setiap modalitas dan setiap skema fusi dapat diisolasi dan dibandingkan satu sama lain.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dataset KITTI, tolok ukur citra jalan raya yang direkam dari kendaraan bergerak dan menjadi rujukan standar untuk deteksi objek serta estimasi kedalaman pada domain kendaraan otonom; kelas objek yang relevan pada domain ini mencakup mobil, pejalan kaki, dan pesepeda. Perbandingan dilakukan antara detektor RGB saja, detektor kedalaman saja, dan detektor gabungan RGB-kedalaman dengan skema fusi awal maupun fusi akhir, serta antar-metode estimasi kedalaman yang berbeda sebagai sumber kanal kedalamannya.

Hasil yang dapat dipastikan dari sumber yang tersedia adalah bahwa detektor gabungan RGB-kedalaman — dengan kedalaman diestimasi memakai MonoDepth — memberi akurasi deteksi lebih tinggi daripada detektor RGB saja maupun detektor kedalaman saja pada dataset KITTI. Temuan ini menunjukkan bahwa peta kedalaman hasil estimasi, meskipun mengandung galat dibanding kedalaman sensor, tetap menyumbang informasi geometris yang saling melengkapi informasi tekstur-warna dari RGB: RGB unggul membedakan objek berdasarkan warna dan tekstur permukaan, sedangkan kedalaman menegaskan batas objek berdasarkan jarak fisiknya terhadap latar dan objek lain, sehingga kombinasi keduanya menutup kelemahan yang dimiliki masing-masing modalitas sendirian. Angka mAP (*mean Average Precision*, metrik standar akurasi deteksi objek) yang persis, serta skema fusi mana — awal atau akhir — yang unggul secara konsisten di seluruh kelas objek KITTI, tidak berhasil dipastikan dari abstrak dan cuplikan yang terjangkau untuk bab ini; angka itu perlu diambil langsung dari tabel pada naskah asli sebelum dikutip formal.

## Kelebihan dan Keterbatasan

Kelebihan utama pendekatan ini adalah tidak bergantung pada sensor kedalaman fisik: kedalaman diperoleh murni dari perangkat lunak estimasi yang berjalan di atas kamera RGB biasa, sehingga metode ini berpotensi diterapkan pada sistem tanpa kamera RGB-D atau LiDAR. Perbandingan sistematis antara fusi awal dan fusi akhir, ditambah pengujian beberapa metode estimasi kedalaman sebagai sumber kanal, memberi bukti empiris langsung tentang di mana penggabungan modalitas sebaiknya dilakukan pada arsitektur deteksi berbasis CNN — pertanyaan yang lebih sering dijawab secara ad hoc pada studi fusi lain.

Dari sisi rekayasa, keterbatasan yang tampak adalah ketergantungan akurasi keseluruhan pada kualitas peta kedalaman hasil estimasi: metode estimasi kedalaman monokuler cenderung kurang andal pada permukaan tanpa tekstur, area transparan atau reflektif, dan objek yang bergerak relatif terhadap kamera (asumsi konsistensi stereo yang mendasari pelatihannya tidak berlaku sempurna pada objek bergerak), sehingga galat pada peta kedalaman berpotensi ikut menurunkan akurasi deteksi pada skenario tersebut. Secara konseptual, evaluasi yang berpusat pada satu domain (jalan raya, KITTI) juga membatasi kepastian bahwa kesimpulan tentang skema fusi terbaik berlaku sama pada domain visual lain, misalnya ruangan dalam gedung atau lingkungan maritim yang menjadi fokus penelitian lain oleh penulis yang sama. Biaya komputasi tambahan dari menjalankan jaringan estimasi kedalaman sebelum deteksi juga merupakan pertimbangan praktis yang tidak selalu dibahas eksplisit dalam ringkasan yang tersedia.

## Kaitan dengan Bab Lain

Bab ini berbagi motif dasar dengan seluruh klaster Pedestrian RGB-T: pertanyaan tentang di mana dan bagaimana dua modalitas citra sebaiknya digabungkan pada jaringan deteksi. Bab [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md) dan bab [103 - 2021 - GAFF - Pedestrian RGB-T](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md) menjawab pertanyaan serupa untuk pasangan RGB-termal, dengan pembobotan modalitas yang bergantung kondisi (siang/malam) alih-alih pembobotan tetap; bab [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md) juga membandingkan titik penggabungan fitur di dalam jaringan. Perbedaan bab ini terhadap keluarga RGB-T tersebut terletak pada modalitas keduanya: kedalaman (geometri jarak) menggantikan termal (radiasi panas), dan kedalaman itu sendiri diestimasi dari RGB, bukan direkam sensor terpisah — sehingga bab ini menjadi rujukan pembanding penting saat menilai apakah kesimpulan tentang fusi awal versus fusi akhir bersifat umum lintas jenis modalitas atau spesifik pada pasangan RGB-termal.

## Poin untuk Sitasi

Kutip dengan kunci `farahnakian2021fusion`. Ringkasan yang aman dikutip: "Farahnakian dan Heikkonen (2021) membandingkan skema fusi awal dan fusi akhir untuk menggabungkan RGB dengan peta kedalaman hasil estimasi monokuler tanpa pengawasan pada deteksi objek berbasis CNN, dan menunjukkan pada dataset KITTI bahwa kombinasi RGB dengan kedalaman hasil estimasi MonoDepth mengungguli detektor RGB saja maupun detektor kedalaman saja." Bab ini adalah versi perluasan dari makalah konferensi ICMLA 2020 oleh penulis yang sama. Butir yang wajib diverifikasi ke naskah asli (pages 73–93) sebelum sitasi formal: angka mAP yang persis untuk tiap konfigurasi, skema fusi (awal/akhir) mana yang unggul secara konsisten, arsitektur detektor dasar (*backbone*) yang dipakai, jumlah dan nama keempat metode estimasi kedalaman yang dibandingkan selain MonoDepth, serta rincian pembagian data latih/uji pada KITTI.
