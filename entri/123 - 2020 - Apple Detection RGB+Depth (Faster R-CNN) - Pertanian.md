# 123 - Faster R-CNN-Based Apple Detection in Dense-Foliage Fruiting-Wall Trees Using RGB and Depth Features for Robotic Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fu2020apple` |
| Judul asli | Faster R-CNN-Based Apple Detection in Dense-Foliage Fruiting-Wall Trees Using RGB and Depth Features for Robotic Harvesting |
| Penulis | Fu, Longsheng; Majeed, Yaqoob; Zhang, Xin; Karkee, Manoj; Zhang, Qin |
| Tahun | 2020 |
| Venue | Biosystems Engineering |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Faster%20R-CNN-Based%20Apple%20Detection%20in%20Dense-Foliage%20Fruiting-Wall%20Trees%20Using%20RGB%20and%20Depth%20Features%20for%20Robotic%20Harvesting
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Faster%20R-CNN-Based%20Apple%20Detection%20in%20Dense-Foliage%20Fruiting-Wall%20Trees%20Using%20RGB%20and%20Depth%20Features%20for%20Robotic%20Harvesting&sort=relevance
- **DOI:** https://doi.org/10.1016/j.biosystemseng.2020.07.007

## Gambaran Umum
Makalah ini menyajikan sistem visi komputer berbasis pembelajaran mendalam untuk mendeteksi buah apel pada perkebunan sistem dinding-buah (*fruiting-wall*) berdaun lebat untuk mendukung operasi pemanenan robotik otomatis. Tantangan utama yang diselesaikan adalah oklusi dedaunan yang padat serta keberadaan buah dan pohon latar belakang pada baris kebun berikutnya yang memicu deteksi positif palsu (*false positive*). Penulis mengintegrasikan informasi spasial kedalaman (*depth*) yang diperoleh dari sensor RGB-D Kinect V2 ke dalam alur deteksi objek Faster R-CNN.

Gagasan utama metode ini adalah menerapkan penyaringan spasial berbasis kedalaman dengan ambang batas (*depth threshold*) tertentu untuk mengeliminasi informasi visual latar belakang di luar pohon target, sehingga menghasilkan citra *Foreground-RGB*. Hasil eksperimen menunjukkan bahwa penggunaan citra *Foreground-RGB* yang telah disaring meningkatkan akurasi deteksi apel secara konsisten. Kombinasi Faster R-CNN dengan arsitektur tulang punggung (*backbone*) VGG16 pada citra *Foreground-RGB* mencapai *Average Precision* (AP) tertinggi sebesar 0,893 dengan waktu pemrosesan rata-rata 0,181 detik per citra.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Modernisasi sektor perkebunan telah mendorong penerapan sistem pohon dinding-buah (*fruiting-wall*), di mana pohon apel ditanam rapat dan dipangkas secara sistematis agar tumbuh tegak dan mendatar seperti dinding. Meskipun mempermudah mekanisasi kebun, struktur kanopi dengan kerapatan daun (*foliage density*) yang tinggi tetap menimbulkan masalah oklusi yang parah bagi sistem penginderaan robotik. Buah apel sering kali tertutup sebagian atau seluruhnya oleh dedaunan, cabang, atau buah lainnya, sehingga sulit dikenali oleh kamera RGB biasa.

Selain oklusi internal, tantangan lain di lapangan adalah kompleksitas latar belakang kebun. Karena jarak antarbaris pohon relatif sempit, kamera yang menghadap ke pohon target sering menangkap buah apel dan baris pohon di seberang lorong kebun (*background rows*). Detektor objek berbasis citra RGB dua dimensi konvensional tidak memiliki kemampuan inheren untuk membedakan apakah buah apel yang terdeteksi berada di pohon target atau di pohon latar belakang. Hal ini menyebabkan kesalahan penentuan posisi target panen dan inefisiensi gerakan robot pemanen. Deteksi buah pada sistem RGB murni, seperti yang diimplementasikan pada MangoYOLO [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md) dan Improved YOLOv3 [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md), rentan terhadap kesalahan lokalisasi spasial 3D karena mengabaikan informasi kedalaman. Oleh karena itu, diperlukan integrasi data sensor multi-modal yang mampu memisahkan informasi spasial objek target dari noise latar belakang secara efisien.

## Ide Utama
Ide utama yang diusulkan dalam penelitian ini adalah menyederhanakan masalah deteksi visual di kebun apel melalui penyaringan dimensi spasial sebelum citra diproses oleh model pembelajaran mendalam. Informasi kedalaman fisik (*physical depth*) dari sensor RGB-D dimanfaatkan untuk memotong data visual pada jarak tertentu secara langsung.

Citra RGB-D menyediakan informasi koordinat warna (merah, hijau, biru) dan kedalaman spasial ($z$) secara simultan. Dengan menetapkan ambang batas kedalaman statis sebesar 1,2 meter, semua informasi visual piksel yang berada di luar jarak tersebut dieliminasi dan diubah menjadi latar belakang hitam konstan. Proses segmentasi jarak ini menghasilkan citra *Foreground-RGB* yang bersih dari objek baris pohon latar belakang. Citra hasil penyaringan ini kemudian diumpankan ke dalam detektor objek dua-tahap Faster R-CNN untuk melokalisasi buah apel target yang siap dipanen.

## Cara Kerja Langkah demi Langkah
Mekanisme sistem deteksi apel berbasis RGB-D ini dapat dibagi menjadi beberapa tahapan berurutan sebagai berikut:

### 1. Akuisisi Data Multi-Modal
Sistem penginderaan menggunakan kamera RGB-D aktif Kinect V2 yang dipasang pada platform bergerak. Kamera ini ditempatkan pada jarak nominal 0,5 meter dari permukaan kanopi pohon dinding-buah. Kinect V2 merekam citra berwarna dengan resolusi $1920 \times 1080$ piksel dan peta kedalaman menggunakan teknologi *Time-of-Flight* (ToF) dengan resolusi asli $512 \times 424$ piksel. Koordinat spasial peta kedalaman diselaraskan secara matematis (*spatially aligned*) ke koordinat citra RGB menggunakan matriks kalibrasi intrinsik dan ekstrinsik kamera. Hasil akhir dari tahap ini adalah citra RGB-D terdaftar di mana setiap piksel $(x, y)$ memiliki nilai warna $[R, G, B]^T$ dan nilai kedalaman $Z(x, y)$ dalam satuan milimeter.

### 2. Penyaringan Kedalaman Spasial (Depth Thresholding)
Setelah proses penyelarasan koordinat selesai, sistem menerapkan algoritma penyaringan kedalaman spasial. Ambang batas kedalaman ($T_d$) ditetapkan sebesar 1,2 meter (1200 mm) berdasarkan jarak maksimum jangkauan fisik lengan manipulator robot pemanen dari sensor. Untuk setiap koordinat piksel $(x, y)$, nilai kedalamannya diperiksa secara sekuensial. Jika nilai kedalaman $Z(x, y)$ lebih besar dari 1,2 meter, maka nilai warna piksel tersebut diatur menjadi nol (warna hitam). Sebaliknya, jika nilai kedalamannya kurang dari atau sama dengan 1,2 meter, nilai warna asli piksel dipertahankan. Secara matematis, transformasi ini dinyatakan sebagai berikut:

```
I_foreground(x, y) = I_original(x, y)   jika Z(x, y) <= 1200 mm
I_foreground(x, y) = [0, 0, 0]          jika Z(x, y) > 1200 mm
```

Proses pemfilteran ini secara fisik menghapus representasi visual pohon apel pada baris di belakang pohon target, dedaunan yang berada terlalu jauh, serta noise latar belakang lainnya.

```
       [Citra RGB Asli]             [Peta Kedalaman (Depth)]
              │                                │
              └───────────────┬────────────────┘
                              ▼
                 [Penyaringan Kedalaman] (z > 1,2 m)
                              │
                              ▼
                   [Citra Foreground-RGB]
                              │
                              ▼
                  [Faster R-CNN Backbone]
                 (VGG16 atau ZFNet Option)
                              │
                              ▼
                       Peta Fitur Konvolusi
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
       [Region Proposal                [RoI Pooling]
        Network (RPN)]                         │
             │                                 │
             └──────► Kandidat Wilayah ────────┘
                              │
                              ▼
                  [Lapisan Terhubung Penuh]
                  ┌───────────┴───────────┐
                  ▼                       ▼
            Klasifikasi apel       Regresi Batas Box
```

### 3. Ekstraksi Fitur Faster R-CNN
Citra *Foreground-RGB* yang telah disaring kemudian diumpankan ke dalam jaringan ekstraksi fitur utama (*backbone*). Penelitian ini mengevaluasi dua jenis arsitektur tulang punggung untuk Faster R-CNN:
*   **VGG16**: Terdiri dari 13 lapisan konvolusi dengan filter berukuran kecil ($3 \times 3$) dan lapisan *max pooling* berturut-turut untuk mengekstraksi peta fitur hierarkis yang kaya akan detail spasial dan semantik objek. Jaringan ini memiliki kapasitas representasi fitur yang sangat tinggi namun membutuhkan daya komputasi dan memori yang besar.
*   **ZFNet**: Merupakan variasi dari AlexNet dengan 5 lapisan konvolusi yang menggunakan filter berukuran $7 \times 7$ pada lapisan awal untuk mengurangi dimensi citra secara cepat. ZFNet lebih ringan dan cepat diproses, namun memiliki keterbatasan dalam mengekstraksi fitur spasial halus pada kondisi oklusi yang kompleks.

### 4. Region Proposal Network (RPN)
Peta fitur konvolusi akhir yang dihasilkan oleh tulang punggung dimasukkan ke dalam *Region Proposal Network* (RPN). RPN memindai peta fitur secara efisien menggunakan jendela geser (*sliding window*) untuk menghasilkan wilayah kandidat objek (*region proposals*). Pada setiap posisi jendela geser, RPN memproyeksikan beberapa kotak acuan (*anchor boxes*) dengan berbagai variasi skala dan rasio aspek. RPN kemudian mengeluarkan skor probabilitas keberadaan objek (*objectness score*) dan koreksi koordinat awal kotak pembatas untuk setiap kotak acuan tersebut. Wilayah dengan skor probabilitas tinggi dipilih sebagai kandidat lokasi buah apel.

### 5. RoI Pooling dan Klasifikasi Akhir
Kandidat wilayah yang diusulkan oleh RPN memiliki ukuran koordinat yang bervariasi. Lapisan *Region of Interest Pooling* (RoI Pooling) digunakan untuk memotong bagian peta fitur sesuai dengan kandidat wilayah tersebut dan mereduksinya menjadi representasi fitur berukuran tetap (misalnya $7 \times 7$ piksel). Fitur berukuran tetap ini kemudian diumpankan ke dalam lapisan terhubung penuh (*fully connected layers*). Lapisan ini memiliki dua cabang keluaran: satu cabang berupa pengklasifikasi *softmax* untuk menentukan apakah objek tersebut adalah "apel" atau "bukan apel" (latar belakang), dan cabang lainnya berupa regresor koordinat kotak pembatas (*bounding box regressor*) untuk menyempurnakan lokasi kotak pembatas target apel pada ruang piksel 2D.

## Eksperimen dan Hasil
Eksperimen dilakukan di kebun apel komersial varietas "Scifresh" (Jazz) yang dikelola dengan sistem dinding-buah. Data dikumpulkan menggunakan sistem visi komputer berbasis Kinect V2 di bawah kondisi pencahayaan alami luar ruangan. Dataset yang digunakan terdiri dari 800 set citra berkualitas tinggi.

Penelitian ini membandingkan kinerja Faster R-CNN dengan dua arsitektur tulang punggung (*backbone*), yaitu ZFNet dan VGG16, pada dua kondisi masukan: citra asli tanpa filter (*Original-RGB*) dan citra hasil filter kedalaman (*Foreground-RGB*). Evaluasi dilakukan menggunakan metrik *Average Precision* (AP) dengan batas ambang batas *Intersection over Union* (IoU) sebesar 0,5, serta waktu pemrosesan rata-rata per citra.

Hasil eksperimen utama diringkas dalam tabel GFM berikut:

| Arsitektur Tulang Punggung (*Backbone*) | Tipe Dataset Input | *Average Precision* (AP) | Waktu Pemrosesan Rata-Rata (detik) |
|---|---|---|---|
| Faster R-CNN + VGG16 | *Foreground-RGB* | **0,893** (89,3%) | 0,181 |
| Faster R-CNN + VGG16 | *Original-RGB* | 0,868 (86,8%) | 0,180 |
| Faster R-CNN + ZFNet | *Foreground-RGB* | Lebih tinggi dari Original | Lebih cepat (< 0,181) |
| Faster R-CNN + ZFNet | *Original-RGB* | Lebih rendah dari VGG16 | Lebih cepat (< 0,181) |

Analisis kuantitatif menunjukkan bahwa penerapan penyaringan kedalaman spasial (*depth-filtering*) memberikan peningkatan akurasi deteksi apel secara konsisten. Untuk model berbasis VGG16, AP meningkat sebesar 2,5% dari 0,868 pada dataset *Original-RGB* menjadi 0,893 pada dataset *Foreground-RGB*. Peningkatan ini disebabkan oleh hilangnya deteksi positif palsu dari baris pohon apel latar belakang yang berada di luar target jangkauan panen robot. 

Dari segi efisiensi komputasi, waktu pemrosesan untuk Faster R-CNN berbasis VGG16 pada citra beresolusi $1920 \times 1080$ piksel adalah 0,181 detik. Waktu pemrosesan ini dinilai memadai untuk diintegrasikan pada sistem kontrol lengan manipulator robot pemanen apel yang umumnya bergerak dengan kecepatan rendah demi keamanan mekanis pohon dan buah.

## Kelebihan dan Keterbatasan
### Kelebihan
Penerapan filter kedalaman fisik sebelum model pembelajaran mendalam memproses citra memberikan keunggulan arsitektural yang signifikan. Dengan menyaring baris pohon latar belakang pada jarak 1,2 meter secara langsung melalui perangkat keras sensor, kompleksitas data visual berkurang secara drastis sebelum masuk ke tahap komputasi konvolusi. Hal ini meminimalkan kebutuhan model untuk mempelajari fitur-fitur kompleks yang membedakan buah target dari buah latar belakang, sehingga mengurangi beban kerja pengoptimalan parameter model.

Selain itu, model Faster R-CNN dengan tulang punggung VGG16 terbukti tangguh dalam mendeteksi buah apel yang mengalami oklusi sebagian oleh dedaunan di area *foreground*. Penggunaan detektor dua-tahap memberikan akurasi penempatan kotak pembatas yang sangat presisi, yang merupakan kebutuhan krusial bagi robot pemanen untuk melakukan pendekatan cakar mekanis (*gripper*) tanpa merusak buah atau ranting pohon.

### Keterbatasan
Meskipun memberikan akurasi yang tinggi, model Faster R-CNN memiliki keterbatasan dalam hal kecepatan pemrosesan jika dibandingkan dengan detektor satu-tahap (*one-stage detector*) modern seperti keluarga YOLO. Waktu pemrosesan sebesar 0,181 detik per citra (setara dengan sekitar 5,5 FPS) membatasi penerapannya jika robot pemanen harus bergerak secara kontinu dengan kecepatan tinggi. Secara konseptual, struktur arsitektur dua-tahap yang memisahkan proses pembuatan usulan wilayah (*region proposal*) dan klasifikasi akhir inherently membutuhkan sumber daya komputasi GPU yang besar, sehingga kurang ramah untuk perangkat tepi (*edge devices*) dengan daya rendah di lapangan.

Keterbatasan fisik lainnya bersumber dari ketergantungan pada sensor kedalaman aktif Kinect V2 yang berbasis teknologi ToF. Sensor ToF bekerja dengan memancarkan sinar infra merah dekat dan mengukur waktu pantulannya. Di bawah paparan cahaya matahari langsung yang terik di perkebunan terbuka, interferensi cahaya infra merah alami dapat mendegradasi kualitas pembacaan sensor kedalaman secara signifikan. Hal ini dapat memicu timbulnya lubang informasi kedalaman (*missing depth values*) atau noise pengukuran, yang secara langsung mengganggu efisiensi pemfilteran kedalaman 1,2 meter. Selain itu, penetapan ambang batas jarak yang kaku sebesar 1,2 meter menuntut sistem navigasi robot untuk selalu menjaga jarak konstan dari kanopi pohon secara presisi; jika robot bergerak terlalu jauh dari kanopi karena kontur tanah yang tidak rata, buah target dapat tersaring keluar dari visualisasi *foreground* secara tidak sengaja.

## Kaitan dengan Bab Lain
Penelitian ini (123) memiliki kaitan erat dengan beberapa bab dalam klaster **Pertanian** yang membahas deteksi buah untuk pemanenan otomatis:
*   **Waris Silsilah Deteksi RGB**: Metode deteksi apel pada awalnya sangat bertumpu pada citra RGB dua dimensi konvensional tanpa informasi spasial kedalaman. Contohnya adalah MangoYOLO ([120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)) dan Improved YOLOv3 ([121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)) yang memodifikasi detektor satu-tahap untuk mendeteksi buah apel dan mangga secara real-time. Bab 123 mewarisi pemahaman bahwa oklusi daun dan cabang adalah hambatan terbesar deteksi objek di kebun, namun mengatasi kelemahan model RGB murni tersebut dengan memperkenalkan pemfilteran spasial berbasis kedalaman menggunakan Kinect V2.
*   **Transisi ke Pemanenan Robotik Riil**: Integrasi visi komputer dan lengan mekanis robotik di kebun apel juga dieksplorasi secara praktis dalam bab Automated Fruit Harvesting Robot ([126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.) - Pertanian](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md)) dan Iceberg Lettuce Harvesting Robot ([125 - 2020 - Iceberg Lettuce Harvesting Robot - Pertanian](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md)).
*   **Evolusi ke Lokalisasi 3D Penuh**: Pemfilteran kedalaman 2D pada bab ini (123) menjadi jembatan menuju sistem rekonstruksi dan estimasi koordinat 3D penuh yang lebih maju. Hal ini dikembangkan oleh Gene-Mola dkk. ([124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md)) dan Kang & Chen ([127 - 2020 - Fruit Detection & 3D Visualisation (Kang & Chen) - Pertanian](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md)) yang menggunakan informasi kedalaman tidak hanya untuk pemfilteran latar belakang, tetapi untuk menghitung posisi koordinat Cartesian 3D presisi buah apel dalam ruang nyata agar dapat dijangkau secara akurat oleh manipulator robotik.
*   **Efisiensi Arsitektur**: Upaya pemangkasan komputasi model deteksi apel luar ruangan diwakili oleh Apple Flower Detection ([122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)) yang melakukan pemangkasan (*pruning*) pada YOLOv4 untuk mendeteksi bunga apel secara real-time pada perangkat keras berdaya rendah, kontras dengan Faster R-CNN berbasis VGG16 (123) yang berbobot berat.

## Poin untuk Sitasi
*   **Kunci BibTeX**: `fu2020apple`
*   **Ringkasan Sitasi**: Fu dkk. (2020) mengintegrasikan sensor RGB-D Kinect V2 dengan detektor Faster R-CNN untuk pemanenan apel robotik di kebun dinding-buah. Dengan menerapkan filter kedalaman spasial pada jarak 1,2 meter, baris pohon latar belakang dieliminasi, sehingga menghasilkan dataset Foreground-RGB. Konfigurasi ini meningkatkan akurasi deteksi Average Precision (AP) sebesar 2,5% hingga mencapai nilai tertinggi 0,893 dengan backbone VGG16, dengan rata-rata waktu pemrosesan sebesar 0,181 detik per citra beresolusi 1920 × 1080 piksel.
*   **Catatan Verifikasi**: Performa deteksi kuantitatif dari tulang punggung ZFNet (AP pada dataset Original-RGB dan Foreground-RGB) tidak disajikan secara eksplisit dalam publikasi sekunder dan disarankan untuk diverifikasi langsung pada naskah jurnal asli sebelum dikutip secara formal.
