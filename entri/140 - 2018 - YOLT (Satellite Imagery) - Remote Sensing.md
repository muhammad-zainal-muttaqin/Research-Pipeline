# 140 - You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vanetten2018yolt` |
| Judul asli | You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery |
| Penulis | Van Etten, Adam |
| Tahun | 2018 |
| Venue | arXiv preprint arXiv:1805.09512 |
| Tema | Remote Sensing |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1805.09512
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=You%20Only%20Look%20Twice%3A%20Rapid%20Multi-Scale%20Object%20Detection%20in%20Satellite%20Imagery
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=You%20Only%20Look%20Twice%3A%20Rapid%20Multi-Scale%20Object%20Detection%20in%20Satellite%20Imagery&sort=relevance

## Gambaran Umum
Makalah ini mengusulkan pipa deteksi (*detection pipeline*) bernama *You Only Look Twice* (YOLT) yang dirancang untuk melokalisasi objek multiskala berukuran sangat kecil pada citra satelit beresolusi tinggi dengan dimensi raksasa secara cepat. Deteksi objek pada citra penginderaan jauh (*remote sensing*) satelit menghadapi tantangan unik akibat area cakupan geografis yang sangat luas dan resolusi spasial yang besar, sementara objek target seperti kendaraan, kapal, dan pesawat hanya menempati sebagian kecil piksel pada citra. Pendekatan deteksi objek konvensional yang dilatih pada citra perspektif horizontal sehari-hari umumnya gagal mendeteksi objek mikro ini karena penurunan resolusi spasial pada lapisan jaringan yang lebih dalam.

Untuk mengatasi hambatan tersebut, YOLT mengadaptasi kerangka deteksi satu tahap *You Only Look Once* versi kedua (YOLOv2) dengan memotong citra satelit raksasa menjadi ubin (*tiles*) lokal secara tumpang tindih (*overlap*). Model ini memodifikasi arsitektur konvolusi dengan memperkecil faktor penyusutan (*downsampling factor*) dari 32 kali menjadi 16 kali guna melestarikan detail spasial beresolusi tinggi pada peta fitur akhir. Setelah model memprediksi objek pada masing-masing ubin secara paralel, YOLT menggabungkan kembali koordinat deteksi lokal ke dalam koordinat piksel global citra asli dan menerapkan metode penekanan non-maksimum (*non-maximum suppression* atau NMS) secara global. Hasil eksperimen menunjukkan bahwa YOLT mampu memproses citra satelit dengan laju kecepatan lebih dari $0,5\text{ km}^2$ per detik dan menghasilkan skor F1 di atas $0,8$ pada tugas lokalisasi kendaraan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi objek pada citra satelit penginderaan jauh merupakan komponen krusial dalam berbagai aplikasi analisis geospasial, seperti pemantauan lalu lintas pelabuhan, manajemen infrastruktur perkotaan, dan pengawasan bandara. Namun, sebelum diterbitkannya makalah ini pada tahun 2018, model detektor objek berbasis jaringan saraf tiruan dalam (*deep neural networks*) seperti Faster R-CNN, SSD, dan YOLOv2 dirancang khusus untuk mendeteksi objek berskala sedang hingga besar pada citra dengan resolusi rendah (biasanya $416 \times 416$ atau $600 \times 600$ piksel) yang diambil dari sudut pandang horizontal manusia (*ground-level imagery*).

Ketika detektor standar ini diterapkan secara langsung pada citra satelit overhead, performanya menurun drastis karena tiga kendala utama. Pertama, dimensi citra satelit sangat masif. Satu citra satelit dari sensor DigitalGlobe dapat mencakup wilayah geografis seluas lebih dari $64\text{ km}^2$ dengan jumlah piksel melebihi 250 juta piksel per citra. Mengumpankan citra raksasa ini secara langsung ke dalam jaringan saraf konvolusi (*convolutional neural network* atau CNN) akan memicu galat memori (*out of memory*) pada GPU. Kedua, ukuran objek sasaran sangat kecil (*minuscule*). Objek seperti mobil atau truk sering kali hanya menempati dimensi sekitar $10 \times 10$ piksel, bahkan bisa sekecil $5 \times 5$ piksel. Operasi penyusutan spasial bertingkat pada tulang punggung (*backbone*) CNN standar (yang biasanya menyusutkan citra sebanyak 32 kali lipat) akan melenyapkan fitur spasial objek sekecil ini, menyisakan representasi yang tidak dapat diklasifikasikan pada lapisan akhir. Ketiga, variasi skala objek sangat lebar. Model harus mampu mendeteksi objek berukuran makro seperti bandara yang mencakup ribuan piksel sekaligus mendeteksi objek mikro seperti kendaraan di jalan raya, sehingga memicu kebingungan skala (*scale confusion*) yang menurunkan ketahanan model deteksi.

## Ide Utama
Gagasan inti dari YOLT adalah mengembangkan alur pemrosesan deteksi objek yang memadukan pembagian citra masukan secara spasial dengan optimalisasi resolusi internal arsitektur YOLOv2 untuk mendeteksi objek mikro secara efisien. Alih-alih melakukan penyusutan resolusi citra satelit raksasa secara paksa—yang akan membuang detail spasial berharga—YOLT menggunakan teknik jendela geser (*sliding window*) untuk memotong citra satelit menjadi ubin-ubin kecil berukuran $416 \times 416$ piksel dengan tumpang tindih marginal.

Di tingkat arsitektur model, YOLT memodifikasi jaringan konvolusi YOLOv2 dengan mengurangi laju *downsampling* dari 32x menjadi 16x. Langkah ini menghasilkan kerapatan grid prediksi yang lebih tinggi pada lapisan keluaran, dari grid $13 \times 13$ menjadi grid $26 \times 26$ untuk dimensi masukan ubin $416 \times 416$ piksel. Dengan demikian, setiap sel grid hanya mencakup wilayah spasial sebesar $16 \times 16$ piksel pada citra ubin (dibandingkan $32 \times 32$ piksel pada model standar), yang secara signifikan mempermudah lokalisasi objek mikro berukuran di bawah 10 piksel. Representasi spasial detail dipertahankan lebih lanjut dengan menambahkan koneksi *passthrough* lateral yang menggabungkan peta fitur resolusi tinggi dari lapisan awal dengan lapisan akhir yang kaya akan informasi semantik. Setelah seluruh ubin diproses oleh detektor YOLT, deteksi lokal tersebut direkonstruksi kembali ke posisi koordinat geografis global citra raksasa sebelum disaring menggunakan NMS global untuk mengeliminasi duplikasi kotak pembatas (*bounding box*).

## Cara Kerja Langkah demi Langkah
Alur kerja deteksi objek multiskala pada YOLT terdiri dari beberapa tahapan terintegrasi yang digambarkan dalam diagram berikut:

```
Citra Satelit Raksasa (mis. 16000 x 16000 piksel)
                      │
                      ▼
            [ Pembagian Ubin ] (Tiling & Overlap)
                      │
  ┌───────────────────┼───────────────────┐
  ▼                   ▼                   ▼
Ubin 1              Ubin 2              Ubin N (416 x 416 piksel)
  │                   │                   │
  ▼                   ▼                   ▼
[ Detektor YOLT (16x Downsampling, Grid 26x26, Passthrough 52x52) ]
  │                   │                   │
  ▼                   ▼                   ▼
Bbox Lokal 1        Bbox Lokal 2        Bbox Lokal N
  │                   │                   │
  └───────────────────┼───────────────────┘
                      │
                      ▼
         [ Rekonstruksi Koordinat ] (Konversi ke Piksel Global)
                      │
                      ▼
           [ Global NMS (IoU = 0,5) ]
                      │
                      ▼
             Deteksi Objek Final
```

### ### Pembagian Ubin Citra (*Tiling* dan *Overlap*)
Citra satelit resolusi tinggi yang sangat luas dibagi menjadi segmen-segmen ubin yang lebih kecil agar dapat diproses oleh GPU tanpa kendala memori. Proses jendela geser ini menggunakan ubin berukuran $416 \times 416$ piksel (atau $512 \times 512$ piksel tergantung kebutuhan pengujian). Jendela geser bergerak dengan lebar tumpang tindih (*overlap*) sebesar 15% dari ukuran ubin (sekitar 64 piksel) untuk mencegah hilangnya objek yang berada tepat di garis pemotongan ubin.

### ### Ekstraksi Fitur dengan Downsampling 16x
Setiap ubin diumpankan ke model YOLT yang dimodifikasi dari arsitektur Darknet YOLOv2. Modifikasi kunci dilakukan dengan menghilangkan satu lapisan penyusutan spasial (*max pooling*) di bagian akhir jaringan. Langkah ini mengurangi faktor penyusutan total dari 32x menjadi 16x, sehingga menghasilkan peta fitur akhir berdimensi $26 \times 26$ grid (bukan $13 \times 13$ grid). Setiap sel grid memproyeksikan wilayah $16 \times 16$ piksel pada citra asli untuk meningkatkan kapasitas lokalisasi objek mikro yang padat.

### ### Integrasi Koneksi Passthrough Multi-Skala
To mempertahankan informasi spasial objek mikro dari degradasi lapisan dalam, YOLT mengimplementasikan koneksi *passthrough* lateral. Peta fitur resolusi tinggi berukuran $52 \times 52 \times 64$ dari lapisan awal diekstraksi dan ditata ulang secara spasial menjadi dimensi $26 \times 26 \times 256$, lalu digabungkan secara saluran (*channel-wise concatenation*) dengan peta fitur lapisan akhir yang berdimensi $26 \times 26 \times 1024$. Hasil akhirnya adalah representasi terpadu berdimensi $26 \times 26 \times 1280$.

### ### Penentuan Prioritas Kotak Acuan (*Anchor Boxes*)
YOLT menggunakan lima kotak acuan (*anchor boxes*) yang disesuaikan untuk objek-objek satelit melalui algoritme pengklasteran *k-means*. Karena objek difoto dari sudut tegak lurus (*nadir*), variasi aspek rasio kotak acuan yang dihasilkan lebih simetris dan berdimensi kecil untuk menstabilkan koordinat prediksi selama pelatihan.

### ### Rekonstruksi Koordinat dan Global NMS
Kotak pembatas lokal, probabilitas kelas, dan skor kepercayaan dari setiap ubin dikonversi kembali ke koordinat piksel global citra asli. Untuk mengeliminasi deteksi ganda pada area ubin yang tumpang tindih, algoritme NMS global diterapkan dengan ambang batas Intersection over Union (IoU) sebesar 0,5 dan batas kepercayaan 0,3 hingga 0,4.

## Eksperimen dan Hasil
Evaluasi kinerja model YOLT dilakukan menggunakan citra satelit resolusi tinggi dari sensor DigitalGlobe dengan ukuran piksel spasial berkisar antara 30 cm hingga 50 cm. Dataset uji mencakup kategori objek dengan rentang skala bervariasi, seperti kendaraan (mobil dan truk), pesawat terbang, perahu/kapal, serta bangunan dan bandara utuh.

Berikut adalah hasil eksperimen kuantitatif utama dalam bentuk F1-Score yang dicapai oleh YOLT pada beberapa kategori objek sasaran:

| Kategori Objek | F1-Score | Karakteristik Ukuran Objek | Catatan Hasil Evaluasi |
|---|:---:|---|---|
| Pesawat Terbang | 0,83 | Sedang (30–100 piksel) | Deteksi stabil di area bandara yang luas. |
| Perahu / Kapal | 0,84 | Kecil-Sedang (20–80 piksel) | Tantangan pada refleksi air dan bayangan dermaga. |
| Bandara Utuh | 1,00 | Makro (>3000 piksel) | Deteksi struktur makro berhasil sempurna tanpa ubin. |
| Kendaraan | 0,82–0,85 | Mikro (8–15 piksel) | Akurasi tinggi pada jalan raya beraspal kontras. |
| Bangunan | ~0,69 | Sedang-Besar (50–200 piksel) | Kinerja kompetitif pada benchmark SpaceNet. |

Pada tugas lokalisasi kendaraan mikro, YOLT menghasilkan skor F1 berkisar antara 0,82 hingga 0,85 pada data uji native resolution. Untuk menguji batas kemampuan model terhadap resolusi rendah, penulis melakukan penurunan resolusi citra secara sistematis. Hasil menunjukkan bahwa model tetap mampu melokalisasi objek yang hanya berukuran sekitar 5 piksel dengan tingkat kepercayaan tinggi, membuktikan ketahanan model terhadap degradasi citra.

Dari aspek kecepatan inferensi, pipa pemrosesan YOLT yang digerakkan pada GPU NVIDIA Titan X mampu memproses ubin-ubin citra satelit secara paralel dengan laju pemrosesan melebihi $0,5\text{ km}^2$ per detik. Kecepatan ini jauh mengungguli detektor dua tahap tradisional seperti Faster R-CNN yang memerlukan waktu pemrosesan ubin lebih lama.

## Kelebihan dan Keterbatasan
Kelebihan utama YOLT terletak pada kemampuannya untuk mendeteksi objek dalam citra dengan ukuran piksel raksasa secara cepat tanpa membuang resolusi spasial asli citra satelit. Modifikasi faktor penyusutan menjadi 16x dan integrasi koneksi *passthrough* yang menghasilkan grid prediksi $26 \times 26$ memberikan ketahanan deteksi yang luar biasa tinggi terhadap objek mikro yang sering kali terabaikan oleh detektor standar. Selain itu, alur pemrosesan ubin yang tumpang tindih dikombinasikan dengan NMS global terbukti efektif memecahkan keterbatasan memori perangkat keras GPU saat menangani citra berukuran megapiksel tinggi.

Namun, dari sisi rekayasa dan implementasi konseptual, model ini memiliki beberapa keterbatasan. Pertama, ketergantungan pada teknik pembagian ubin (*tiling*) sliding window memicu beban komputasi tambahan (*overhead*) yang cukup signifikan pada tahap pemotongan citra di awal dan penggabungan koordinat serta NMS global di akhir. Hal ini membuat laju pemrosesan tidak sepenuhnya linier terhadap ukuran citra satelit. Kedua, YOLT memprediksi kotak pembatas horizontal (*horizontal bounding box* atau HBB) standar. Sudut pandang satelit tegak lurus (*nadir*) menyebabkan objek seperti kendaraan atau kapal dapat berorientasi ke arah mana saja dengan kerapatan tinggi. Penggunaan HBB pada objek miring yang padat sering kali memicu NMS global secara keliru menekan kotak pembatas valid di sekitarnya. Ketiga, performa deteksi pada kategori bangunan yang padat dan berhimpitan tidak sebaik detektor segmentasi khusus, karena model kesulitan menentukan batas pemisah antar-dinding gedung yang rapat.

## Kaitan dengan Bab Lain
Pipa deteksi YOLT (2018) menempati posisi historis sebagai salah satu adaptasi pionir dari keluarga model YOLO untuk domain penginderaan jauh (*remote sensing*) citra satelit. Model ini membentuk fondasi penting bagi perkembangan detektor udara berbasis drone maupun satelit pada tahun-tahun berikutnya.

Hubungan YOLT dengan bab-bab lain dalam klaster ini dapat dijelaskan sebagai berikut:
- **Kaitan dengan [Bab 138 - Robust CNN High-Res Remote Sensing](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md):** Model HRCNN (2019) mengambil arah yang berlawanan dengan YOLT. Di saat YOLT fokus pada detektor satu tahap yang cepat (YOLOv2) dengan pemrosesan ubin eksternal, HRCNN menggunakan pendekatan dua tahap yang lebih lambat namun lebih presisi, dengan memanfaatkan representasi fitur hierarkis (FPN) dan penumpukan lapisan terhubung penuh (`fc6 + fc7`) untuk meningkatkan ketahanan klasifikasi terhadap rotasi objek dalam ubin citra.
- **Kaitan dengan [Bab 137 - TPH-YOLOv5](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md):** TPH-YOLOv5 (2021) mewarisi masalah deteksi objek mikro dari YOLT tetapi menyelesaikannya melalui modifikasi arsitektur internal yang lebih canggih. TPH-YOLOv5 menambahkan head prediksi keempat (P2) pada resolusi yang sangat tinggi dan mengintegrasikan blok *Transformer Encoder* serta modul CBAM untuk menangkap konteks spasial global, sehingga mengurangi ketergantungan pada teknik pembagian ubin yang lambat untuk citra UAV yang lebih kecil dibandingkan citra satelit.
- **Kaitan dengan [Bab 139 - UAV-YOLOv8](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md):** UAV-YOLOv8 (2023) merupakan evolusi modern yang berupaya mereduksi beban komputasi tinggi dari model perhatian seperti TPH-YOLOv5. Model ini menggunakan landasan YOLOv8 *anchor-free* yang dikombinasikan dengan head deteksi objek kecil khusus, mencapai efisiensi deteksi objek mikro yang menyerupai kecepatan YOLT namun dengan akurasi klasifikasi yang jauh lebih tinggi pada platform drone.

## Poin untuk Sitasi
Kunci BibTeX untuk merujuk naskah ini adalah `vanetten2018yolt`.

Berikut adalah ringkasan yang aman dikutip dalam tinjauan pustaka:
> Van Etten mengusulkan You Only Look Twice (YOLT), sebuah pipa deteksi objek cepat untuk citra satelit beresolusi tinggi dengan area luas. YOLT mengadopsi kerangka detektor satu tahap YOLOv2 dengan memotong citra raksasa menjadi ubin-ubin kecil yang tumpang tindih dan mengurangi faktor penyusutan spasial (*downsampling*) menjadi 16x untuk menghasilkan grid prediksi $26 \times 26$. Pendekatan ini berhasil mempertahankan resolusi spasial objek kecil (seperti kendaraan dan pesawat) dan mencapai laju pemrosesan inferensi lebih dari $0,5\text{ km}^2$ per detik dengan skor F1 di atas 0,8.

Catatan untuk verifikasi lebih lanjut sebelum sitasi formal:
- Performa deteksi bandara utuh yang dilaporkan mencapai skor F1 sebesar 1,00 diuji pada dataset pengujian dengan ukuran sampel terbatas yang spesifik. Skor F1 untuk bangunan sekitar 0,69 menunjukkan bahwa model YOLT tidak dioptimalkan untuk ekstraksi jejak bangunan (*building footprint extraction*) yang kompleks.
