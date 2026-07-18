# 121 - Apple Detection During Different Growth Stages in Orchards Using the Improved YOLO-V3 Model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tian2019appleyolo` |
| Judul asli | Apple Detection During Different Growth Stages in Orchards Using the Improved YOLO-V3 Model |
| Penulis | Tian, Yunong; Yang, Guodong; Wang, Zhe; Wang, Hao; Li, En; Liang, Zize |
| Tahun | 2019 |
| Venue | Computers and Electronics in Agriculture |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Apple%20Detection%20During%20Different%20Growth%20Stages%20in%20Orchards%20Using%20the%20Improved%20YOLO-V3%20Model
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Apple%20Detection%20During%20Different%20Growth%20Stages%20in%20Orchards%20Using%20the%20Improved%20YOLO-V3%20Model&sort=relevance
- **DOI (ScienceDirect):** https://doi.org/10.1016/j.compag.2019.01.012

## Gambaran Umum
Penelitian oleh Tian dkk. (2019) menyajikan model deteksi objek satu-tahap (*one-stage detector*) berbasis pembelajaran mendalam (*deep learning*) bernama YOLOv3-dense untuk mendeteksi buah apel pada tiga tahap pertumbuhan (*growth stages*) di lingkungan kebun yang kompleks. Model ini mengatasi tantangan luar ruangan seperti buah saling tumpang tindih (*overlapping*), terhalang oleh dedaunan (oklusi), fluktuasi intensitas pencahayaan matahari langsung (*direct sunlight*) maupun bayangan (*shade*), serta perubahan warna buah dari fase muda hingga matang.

Model YOLOv3-dense mengintegrasikan modul jaringan terkoneksi padat (*DenseNet*) ke dalam kerangka kerja *You Only Look Once* versi 3 (YOLOv3). Integrasi ini memperkuat propagasi dan penggunaan kembali fitur (*feature propagation and reuse*) pada lapisan fitur beresolusi rendah. Dalam pengujian menggunakan dataset citra kebun beresolusi 3000 × 4000 piksel, model ini mencapai skor F1 sebesar 0,817 dengan waktu pemrosesan rata-rata 0,304 detik per citra. Performa ini mengungguli metode pembanding seperti Faster R-CNN dan YOLOv3 standar dalam kondisi kebun yang menantang.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi buah yang akurat dan cepat di kebun terbuka sangat krusial untuk otomatisasi pertanian, seperti estimasi beban buah (*fruit load estimation*) dan pemanenan mekanis menggunakan robot. Sebelum meluasnya penerapan pembelajaran mendalam, metode visi komputer tradisional sangat bergantung pada ekstraksi fitur manual (*hand-crafted features*) seperti klasifikasi warna, analisis bentuk bulat, atau segmentasi ambang batas intensitas piksel. Namun, metode tradisional ini memiliki kelemahan inheren berupa sensitivitas yang sangat tinggi terhadap gangguan latar belakang dan perubahan lingkungan kebun alami.

Tantangan utama di lapangan meliputi:
1. Oklusi dedaunan dan cabang: Buah apel sering kali terhalang sebagian oleh daun atau ranting, sehingga visi tradisional yang mengandalkan keutuhan bentuk buah akan gagal mendeteksi objek.
2. Fluktuasi pencahayaan: Sinar matahari langsung menimbulkan efek kilau putih (*overexposure*) pada kulit apel, sedangkan awan atau dedaunan lebat menciptakan bayangan gelap (*shade*) yang mengaburkan warna asli buah.
3. Variasi warna lintas tahap pertumbuhan: Apel muda berukuran kecil dan berwarna hijau pekat, menyerupai dedaunan sekitarnya. Seiring pertumbuhan, buah membesar dan akhirnya berubah merah saat matang. Model konvensional yang hanya dilatih pada buah matang akan gagal mendeteksi buah muda.
4. Keseimbangan akurasi dan kecepatan: Detektor dua-tahap (*two-stage detector*) seperti Faster R-CNN menawarkan akurasi tinggi tetapi lambat. Sebaliknya, model satu-tahap seperti YOLOv3 standar cepat tetapi kurang akurat untuk objek kecil yang terhalang.

Oleh karena itu, diperlukan arsitektur yang mampu mempertahankan fitur halus objek kecil, tangguh terhadap variasi warna dan pencahayaan, serta memiliki kecepatan inferensi memadai untuk implementasi lapangan.

## Ide Utama
Gagasan utama penelitian ini adalah memperkuat pemeliharaan fitur pada YOLOv3 dengan menerapkan prinsip koneksi padat dari DenseNet pada lapisan ekstraksi fitur beresolusi rendah. Dalam YOLOv3 standar, informasi spasial objek kecil atau terhalang sering kali hilang pada lapisan yang lebih dalam akibat operasi penyusutan dimensi (*downsampling*) yang berulang.

Untuk mengatasinya, Tian dkk. mengganti lapisan konvolusi transisi standar pada sub-jaringan ekstraksi multi-skala YOLOv3 dengan blok padat (*dense block*). Di dalam setiap blok padat, setiap lapisan terhubung langsung dengan seluruh lapisan berikutnya dalam format maju-umpan (*feed-forward*). Lapisan ke-$l$ menerima seluruh peta fitur (*feature maps*) dari lapisan terdahulu melalui operasi penggabungan (*concatenation*). Konseptualisasi mekanis ini memastikan aliran informasi maksimal tanpa kehilangan fitur tingkat rendah. Hasilnya, fitur resolusi rendah yang kaya akan informasi tepi dan tekstur apel hijau muda dapat digunakan kembali (*feature reuse*) pada lapisan prediksi yang lebih dalam, sekaligus memperlancar aliran gradien (*backpropagation*) selama pelatihan.

## Cara Kerja Langkah demi Langkah
Model YOLOv3-dense memproses citra masukan melalui tahapan berurutan hingga menghasilkan prediksi koordinat kotak pembatas (*bounding box*).

### 6.1 Pra-pemrosesan Citra
Citra masukan beresolusi tinggi 3000 × 4000 piksel diubah ukurannya menjadi $320 \times 320$ piksel. Langkah pengecilan skala spasial ini menjaga kestabilan lapisan normalisasi bets (*batch normalization*) dan memungkinkan ukuran bets (*batch size*) yang lebih besar selama pelatihan.

### 6.2 Ekstraksi Fitur Dasar dengan Darknet-53
Citra masukan dilewatkan ke dalam *backbone* Darknet-53 yang terdiri dari 53 lapisan konvolusi dengan koneksi sisa (*residual connection*). Jaringan ini mengekstrak fitur visual secara hierarkis dan menghasilkan tiga peta fitur dengan skala spasial berbeda untuk deteksi multi-skala.

### 6.3 Densifikasi Fitur dengan Dense Block
Modifikasi inti dilakukan pada sub-jaringan prediksi fitur beresolusi rendah dengan mengganti lapisan konvolusi transisi konvensional dengan blok padat (*dense block*).
Setiap lapisan dalam blok padat menerima peta fitur dari seluruh lapisan terdahulu. Dengan laju pertumbuhan (*growth rate*) sebesar $k$, penggabungan peta fitur dilakukan secara horizontal di sepanjang dimensi saluran (*channel dimension*). Dengan demikian, informasi tepi apel hijau muda tetap terjaga dan dikombinasikan dengan representasi semantik tingkat tinggi pada lapisan dalam, sekaligus memitigasi gradien menghilang (*vanishing gradient*).

### 6.4 Fusi Fitur Multi-Skala dan Prediksi
Model menggunakan arsitektur mirip *Feature Pyramid Network* (FPN) untuk memprediksi objek pada tiga skala output yang berbeda:
1. Skala Halus (prediksi grid $80 \times 80$): Untuk melokalisasi apel muda kecil atau apel dengan oklusi berat.
2. Skala Menengah (prediksi grid $40 \times 40$): Untuk mendeteksi apel berukuran rata-rata.
3. Skala Kasar (prediksi grid $20 \times 20$): Untuk mendeteksi apel matang besar yang dekat dengan kamera.

Pada setiap sel kisi (*grid cell*), model memprediksi koordinat kotak pembatas ($x, y, w, h$), skor keyakinan (*confidence score*), dan probabilitas keberadaan kelas apel. Dimensi kotak pembatas disesuaikan menggunakan jangkar (*anchors*) yang telah diklaster sebelumnya menggunakan metode *k-means*. Akhirnya, hasil prediksi disaring menggunakan teknik penekanan non-maksimum (*Non-Maximum Suppression* / NMS) berdasarkan ambang batas *Intersection over Union* (IoU).

Alur data dan struktur integrasi *dense block* ini digambarkan secara skematis pada diagram berikut:

```
[Citra Kebun Apel]
       │
       ▼
┌──────────────┐
│  Darknet-53  │ (Ekstraksi Fitur Awal)
└──────┬───────┘
       ├─────────────────────────────────┐
       ▼ (Lapisan Dangkal)               ▼ (Lapisan Dalam)
┌──────────────┐                 ┌──────────────┐
│ Peta Fitur   │                 │ Dense Block  │ (Dense Connections
│ Skala Halus  │                 │  (Features   │  & Feature Reuse)
│ (Deteksi     │                 │ Propagation) │
│ Apel Kecil/  │                 └──────┬───────┘
│  Hijau Muda) │                        │ Up-sample & Concatenate
└──────▲───────┘                        │
       │                                ▼
       └─────────────────────────┌──────────────┐
                                 │ Peta Fitur   │ (Deteksi Apel
                                 │ Skala Kasar  │  Besar / Matang)
                                 └──────────────┘
```

## Eksperimen dan Hasil
Tian dkk. (2019) menguji model YOLOv3-dense menggunakan dataset apel yang dikumpulkan dari perkebunan buah nyata di bawah kondisi lingkungan alami.
- Dataset awal terdiri dari **480 citra asli** beresolusi **3000 × 4000 piksel** yang mencakup tiga fase pertumbuhan apel: muda (*young*), berkembang (*expanding*), dan matang (*ripe*).
- Untuk mengantisipasi *overfitting*, dilakukan augmentasi data dengan teknik rotasi, penyesuaian keseimbangan warna, kecerahan, dan penambahan efek buram (*blur*), menghasilkan **4.800 citra latih**.
- Set data uji (*test dataset*) yang digunakan terdiri dari **480 citra asli** tanpa augmentasi untuk merepresentasikan kondisi lapangan nyata.

Performa model YOLOv3-dense dievaluasi menggunakan metrik presisi (*precision*), sensitivitas (*recall*), dan skor F1, dibandingkan dengan beberapa model standar:
- **YOLOv3-dense (usulan):** skor F1 sebesar **0,817** dengan waktu inferensi rata-rata **0,304 detik** per citra.
- **YOLOv3 standar:** skor F1 sebesar **0,793** (selisih 2,4% lebih rendah dari model usulan).
- **Faster R-CNN (dengan VGG16):** skor F1 sebesar **0,801** dengan latensi komputasi yang jauh lebih tinggi.
- **YOLOv2 standar:** skor F1 sebesar **0,738**.

Eksperimen membuktikan YOLOv3-dense unggul pada kondisi cahaya berfluktuasi. Pada kilau cahaya matahari langsung (*overexposure*), koneksi padat mempertahankan batas bentuk buah. Pada oklusi dedaunan hingga 50%, model usulan menekan tingkat negatif palsu (*false negatives*). Pada tahap apel muda hijau kecil, kesalahan klasifikasi sebagai daun berkurang drastis karena detail spasial dipertahankan lewat koneksi langsung.

## Kelebihan dan Keterbatasan
Kelebihan:
1. Robustness Lintas Tahap Pertumbuhan: Andal dalam mendeteksi buah sejak fase hijau kecil hingga merah matang, mendukung pemantauan siklus hidup buah sepanjang musim.
2. Penggunaan Kembali Fitur yang Efisien: Integrasi modul DenseNet pada sub-jaringan prediksi memaksimalkan pemanfaatan fitur spasial halus tanpa menambah parameter berlebihan, efektif untuk objek terhalang (*occlusion*) dan saling menumpuk (*overlapping*).
3. Keseimbangan Akurasi-Latensi: Kecepatan inferensi 0,304 detik pada citra resolusi tinggi memadai untuk implementasi pada platform otonom atau komputasi tepi lapangan.

Keterbatasan:
1. Ketiadaan Informasi Kedalaman (Depth): Model hanya mengandalkan visual 2D (RGB murni). Ketiadaan koordinat spasial 3D absolut membatasi penerapan pada robot pemanen yang membutuhkan informasi kedalaman untuk merencanakan lintasan gerak pencengkeram fisik.
2. Batasan Inferensi Real-Time: Kecepatan sekitar 3 bingkai per detik (FPS) belum memenuhi standar real-time penuh (>15 FPS) pada perangkat berdaya rendah jika memproses video beresolusi tinggi tanpa pemotongan.
3. Oklusi Ekstrem: Jika buah terhalang dedaunan atau ranting kayu tebal melebihi 80%, fitur visual RGB murni tidak lagi memadai dan memicu kegagalan deteksi.

## Kaitan dengan Bab Lain
Penelitian YOLOv3-dense oleh Tian dkk. (2019) merupakan bagian penting dari evolusi deteksi buah berbasis visual RGB dalam klaster pertanian.
- Hubungan dengan [MangoYOLO](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md): Koirala dkk. mengembangkan MangoYOLO untuk mendeteksi mangga dan mengestimasi beban buah total (*fruit load estimation*). MangoYOLO memodifikasi YOLOv2/v3 agar lebih ringan demi kecepatan, sedangkan YOLOv3-dense memilih memodifikasi backbone dengan DenseNet untuk ketangguhan oklusi apel multi-tahap tumbuh.
- Hubungan dengan [Apple Flower Detection](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md): Wu dkk. (2020) berfokus pada deteksi bunga apel menggunakan YOLOv4 dengan pemangkasan saluran (*channel pruning*) untuk deployment perangkat tepi berdaya rendah, berlawanan dengan Tian dkk. yang menambah kompleksitas struktural demi akurasi.
- Hubungan dengan [Apple Detection RGB+Depth (Faster R-CNN)](./123%20-%202020%20-%20Apple%20Detection%20RGB%2BDepth%20%28Faster%20R-CNN%29%20-%20Pertanian.md): Fu dkk. (2020) memecahkan masalah oklusi dedaunan lebat dengan menambahkan fitur kedalaman (depth) ke Faster R-CNN (multimodal RGB-D), mengatasi keterbatasan visual 2D murni dari YOLOv3-dense.
- Hubungan dengan [Fruit Detection & 3D Location (Gene-Mola dkk.)](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md) dan [Fruit Detection & 3D Visualisation (Kang & Chen)](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md): Kedua bab ini melangkah lebih jauh dari deteksi 2D YOLOv3-dense dengan menggunakan segmentasi instan (*instance segmentation*) dan rekonstruksi 3D (fotogrametri SfM atau sensor kedalaman aktif) untuk melokalisasi posisi buah secara presisi dalam ruang tiga dimensi.
- Hubungan dengan [Automated Fruit Harvesting Robot (Onishi dkk.)](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md) dan [Iceberg Lettuce Harvesting Robot](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md): Deteksi visual 2D apel seperti yang dikembangkan oleh Tian dkk. merupakan komponen dasar sistem visi komputer yang kemudian diintegrasikan ke dalam sistem robot fisik pengeksekusi pemanenan buah otonom.

## Poin untuk Sitasi
- Kunci BibTeX: `tian2019appleyolo`
- Kutipan ringkasan:
  "Tian dkk. (2019) mengusulkan model YOLOv3-dense yang mengintegrasikan komponen DenseNet pada sub-jaringan ekstraksi fitur resolusi rendah YOLOv3 untuk mendeteksi buah apel pada tiga tahap pertumbuhan (muda, berkembang, dan matang). Model ini menunjukkan ketangguhan tinggi terhadap oklusi dedaunan dan fluktuasi pencahayaan di area perkebunan, mencapai skor F1 sebesar 0,817 dengan waktu pemrosesan rata-rata 0,304 detik per citra beresolusi tinggi."
- Catatan angka/klaim yang perlu diverifikasi:
  "Seluruh metrik performa (skor F1 0,817 dan kecepatan inferensi 0,304 detik pada citra 3000 × 4000 piksel) serta pembagian dataset (480 citra asli, diaugmentasi menjadi 4.800 citra latih, dan diuji pada 480 citra asli) telah diverifikasi secara akurat dari naskah asli publikasi Computers and Electronics in Agriculture (2019)."
