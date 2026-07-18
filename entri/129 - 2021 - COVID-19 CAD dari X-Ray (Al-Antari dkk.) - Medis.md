# 129 - Fast Deep Learning Computer-Aided Diagnosis of COVID-19 Based on Digital Chest X-Ray Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alantari2020covid` |
| Judul asli | Fast Deep Learning Computer-Aided Diagnosis of COVID-19 Based on Digital Chest X-Ray Images |
| Penulis | Mugahed A. Al-Antari, Cam-Hao Hua, Jaehun Bang, Sungyoung Lee |
| Tahun | 2021 |
| Venue | Applied Intelligence |
| Tema | Medis |

## Tautan Akses
- **DOI (Springer Link):** https://doi.org/10.1007/s10489-020-02076-6
- **Google Scholar:** https://scholar.google.com/scholar?q=Fast%20Deep%20Learning%20Computer-Aided%20Diagnosis%20of%20COVID-19%20Based%20on%20Digital%20Chest%20X-Ray%20Images
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Fast%20Deep%20Learning%20Computer-Aided%20Diagnosis%20of%20COVID-19%20Based%20on%20Digital%20Chest%20X-Ray%20Images&sort=relevance

## Gambaran Umum

Makalah ini menyajikan sebuah sistem diagnosis berbantuan komputer (*computer-aided diagnosis* atau CAD) berbasis pembelajaran mendalam (*deep learning*) yang dirancang untuk mendeteksi dan mengklasifikasikan infeksi *coronavirus disease 2019* (COVID-19) secara cepat dari citra rontgen dada digital (*digital chest X-ray* atau CXR). Masalah utama yang dipecahkan adalah kebutuhan mendesak akan alat triase klinis yang otomatis, cepat, dan akurat selama puncak pandemi COVID-19. Al-Antari dkk. (2021) mengintegrasikan detektor satu tahap (*one-stage detector*) berbasis prediktor *You Only Look Once* (YOLO) untuk melokalisasi wilayah infeksi pada paru-paru dan mengklasifikasikannya secara simultan.

Hasil eksperimen utama menunjukkan bahwa sistem CAD yang diusulkan mampu membedakan patologi COVID-19 dari delapan penyakit pernapasan umum lainnya dengan sangat efisien. Pada pengujian menggunakan dataset gabungan skala besar yang terdiri dari 50.490 citra CXR, model ini mencapai akurasi deteksi lokalisasi sebesar 96,31% dan akurasi klasifikasi multi-kelas sebesar 97,40%. Dari aspek kecepatan, sistem ini hanya membutuhkan waktu 0,0093 detik untuk memproses satu citra rontgen dada tunggal, yang setara dengan tingkat pemrosesan 108 *frames per second* (FPS). Melalui pencapaian ini, sistem yang diusulkan menawarkan solusi praktis untuk mempercepat alur diagnosis klinis tanpa mengorbankan akurasi diagnostik.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penyebaran global pandemi COVID-19 pada awal tahun 2020 menciptakan tekanan luar biasa pada sistem perawatan kesehatan di seluruh dunia. Metode diagnosis standar emas yang digunakan adalah pengujian reaksi berantai polimerase transkripsi balik (*reverse transcription-polymerase chain reaction* atau RT-PCR). Kendati memiliki spesifisitas tinggi, RT-PCR memiliki beberapa kelemahan kritis dalam skenario darurat, meliputi waktu tunggu hasil laboratorium yang berkisar antara beberapa jam hingga beberapa hari, tingkat sensitivitas yang bervariasi tergantung pada kualitas pengambilan sampel swab, serta tingginya potensi hasil negatif palsu (*false negative*) pada fase awal infeksi. Oleh karena itu, pencitraan medis dada diadopsi sebagai modalitas komplementer yang sangat penting untuk membantu triase pasien secara cepat.

Tomografi terkomputasi dada (*chest computed tomography* atau chest CT) merupakan modalitas pencitraan dengan sensitivitas sangat tinggi untuk mendeteksi lesi paru akibat COVID-19. Namun, penggunaan CT-scan secara massal terhambat oleh biaya pemeriksaan yang mahal, paparan radiasi yang signifikan terhadap pasien, keterbatasan ketersediaan mesin di wilayah terpencil, serta durasi sterilisasi ruangan mesin CT yang lama setelah digunakan oleh pasien yang terinfeksi. Sebagai alternatif, citra rontgen dada digital (CXR) menawarkan opsi yang jauh lebih praktis. Mesin rontgen dada tersedia secara luas bahkan di fasilitas kesehatan tingkat pertama, memiliki biaya operasional rendah, memancarkan dosis radiasi yang minimal, serta dapat dilakukan menggunakan perangkat rontgen portabel langsung di sisi tempat tidur pasien (*bedside imaging*).

Meskipun CXR memiliki banyak keunggulan logistik, interpretasi visual citra CXR secara manual oleh dokter atau ahli radiologi merupakan tugas yang sangat menantang. Karakteristik visual dari infeksi paru akibat COVID-19—seperti opasitas corakan kaca (*ground-glass opacity* atau GGO) dan konsolidasi ruang udara—memiliki batas-batas spasial yang sangat kabur dan kontras visual yang rendah terhadap jaringan paru sehat di sekitarnya. Selain itu, tanda-tanda radiologis ini sering kali tumpang tindih secara visual dengan manifestasi penyakit pernapasan lainnya, seperti pneumonia bakteri biasa, infiltrasi paru, atau tuberkulosis. Selama masa puncak pandemi, beban kerja radiolog yang membeludak memicu kelelahan kerja (*burnout*) yang meningkatkan risiko kesalahan interpretasi dan variabilitas subjektif antar-pengamat (*inter-observer variability*). Oleh karena itu, diperlukan sebuah sistem CAD otomatis yang tidak hanya mampu melokalisasi wilayah infeksi pada paru-paru secara akurat, tetapi juga mampu mengklasifikasikan jenis patologi tersebut secara cepat untuk mendukung keputusan klinis yang objektif.

## Ide Utama

Gagasan inti dari penelitian Al-Antari dkk. adalah menerapkan arsitektur deteksi objek satu tahap berbasis YOLO sebagai mesin prediksi tunggal terpadu untuk mendeteksi dan mengklasifikasikan lesi paru secara simultan langsung dari citra CXR digital resolusi penuh. Pendekatan ini secara mendasar berbeda dari sistem CAD konvensional yang biasanya memisahkan alur kerja menjadi beberapa modul independen, seperti segmentasi area paru-paru, ekstraksi fitur tekstur secara manual, dan klasifikasi menggunakan pengklasifikasi terpisah. Desain multi-tahap konvensional semacam itu tidak hanya meningkatkan kompleksitas komputasi tetapi juga memperlambat waktu inferensi secara signifikan karena akumulasi kesalahan dari satu tahap ke tahap berikutnya.

Dengan menggunakan prediktor YOLO, proses diagnosis diformulasikan sebagai satu masalah regresi tunggal. Citra rontgen dada masukan dilewatkan melalui jaringan saraf konvolusional (*convolutional neural network* atau CNN) mendalam yang mengekstrak fitur spasial global secara langsung. Jaringan kemudian memprediksi koordinat kotak pembatas (*bounding box*) yang melokalisasi wilayah infeksi paru dan probabilitas kelas penyakit untuk setiap wilayah tersebut secara bersamaan dalam satu lintasan maju (*single forward pass*). Untuk mengatasi tantangan data klinis riil yang tidak seimbang dan terbatas pada awal pandemi, ide utama ini didukung oleh penerapan strategi penyeimbangan data (*data balancing*) dan augmentasi data (*data augmentation*) yang agresif untuk memperkuat generalisasi model pada kelas-kelas penyakit minoritas.

## Cara Kerja Langkah demi Langkah

Sistem CAD yang diusulkan oleh Al-Antari dkk. bekerja melalui alur pemrosesan terpadu yang terbagi menjadi tiga tahapan utama: pra-pemrosesan citra digital, ekstraksi fitur spasial menggunakan 23 lapisan konvolusi berurutan, dan prediksi kotak pembatas beserta probabilitas kelas secara simultan melalui lapisan terhubung penuh.

```
[Citra CXR Digital] (Masukan Resolusi Penuh)
        │
        ▼
[Pra-Pemrosesan & Augmentasi] ───► Penyeimbangan kelas & perluasan sampel
        │
        ▼
[Ekstraksi Fitur Konvolusional] ──► 23 Lapisan Konvolusi (Filter 1x1 & 3x3)
                                ──► 5 Lapisan Max-Pooling
        │
        ▼
[Lapisan Terhubung Penuh (FC)] ──► Lapisan FC 1 (Pemetaan Linear)
                               ──► Lapisan FC 2 (Proyeksi Output)
        │
        ├──────────────────────────────┐
        ▼                              ▼
[Koordinat Kotak Pembatas]    [Probabilitas Multi-Kelas]
(Regresi x, y, w, h)          (Klasifikasi COVID-19 vs Penyakit Lain)
        │                              │
        └──────────────┬───────────────┘
                       ▼
[Penekanan Non-Maksimum (NMS)] ──► Eliminasi kotak pembatas tumpang tindih
        │
        ▼
[Prediksi Akhir Lokalisasi & Diagnosis]
```

### Pra-Pemrosesan dan Strategi Penyeimbangan Data
Citra rontgen dada digital yang dikumpulkan dari basis data mentah memiliki variasi dimensi piksel dan distribusi kelas yang sangat timpang. Sebelum dimasukkan ke dalam jaringan saraf, citra mengalami langkah-langkah berikut:
- **Penyesuaian Resolusi:** Citra CXR disesuaikan ukurannya ke resolusi spasial standar yang kompatibel dengan arsitektur masukan model tanpa membuang informasi detail klinis penting.
- **Penyeimbangan Kelas (*Data Balancing*):** Karena jumlah citra pasien COVID-19 jauh lebih sedikit dibandingkan citra penyakit pernapasan lainnya pada dataset ChestX-ray8, penulis melakukan metode penyeimbangan dengan melakukan penapisan acak pada kelas mayoritas (*undersampling*) dan menduplikasi sampel pada kelas minoritas (*oversampling*).
- **Augmentasi Data Geometris dan Intensitas:** Untuk mencegah penyesuaian berlebih (*overfitting*), citra latih diperbanyak menggunakan teknik rotasi spasial secara acak, translasi piksel pada sumbu horizontal dan vertikal, pencerminan horizontal (*horizontal flipping*), serta penyesuaian kontras lokal. Langkah ini mensimulasikan berbagai variasi posisi pasien dan kualitas paparan sinar-X saat pengambilan citra di klinik nyata.

### Ekstraksi Fitur Spasial Mendalam
Tulang punggung (*backbone*) dari prediktor YOLO yang digunakan terdiri dari **23 lapisan konvolusi berurutan** (*sequential convolutional layers*) dan **5 lapisan penyatuan maksimum** (*max-pooling layers*). Lapisan konvolusi ini dirancang secara sistematis dengan mengadopsi struktur konvolusi reduksi dimensi:
- Lapisan konvolusi dengan filter berukuran $1 \times 1$ digunakan untuk mengompresi jumlah kanal fitur (*channel reduction*), sehingga mengurangi beban komputasi secara drastis.
- Lapisan konvolusi dengan filter berukuran $3 \times 3$ ditempatkan setelahnya untuk melakukan ekstraksi fitur spasial lokal yang lebih kaya.
- Operasi penyatuan maksimum (*max-pooling*) dengan ukuran filter $2 \times 2$ diterapkan secara periodik di antara blok konvolusi untuk mereduksi dimensi spasial citra masukan setengah kali lipat, mengisolasi fitur yang paling dominan, dan memberikan sifat invarian terhadap pergeseran posisi kecil (*translation invariance*).

### Prediksi Kotak Pembatas dan Klasifikasi Simultan
Setelah citra melewati 23 lapisan konvolusi, peta fitur spasial dimensi tinggi yang dihasilkan diratakan (*flattened*) dan dialirkan ke **dua lapisan terhubung penuh** (*fully connected layers* atau FC) di ujung akhir jaringan:
- Lapisan FC pertama berfungsi untuk memetakan representasi fitur spasial secara global.
- Lapisan FC kedua memproyeksikan fitur tersebut ke dalam bentuk representasi output deteksi. Untuk setiap pembagian kisi (*grid*) berukuran $S \times S$ pada citra masukan, jaringan memprediksi parameter kotak pembatas dan skor kepercayaan (*confidence score*), serta probabilitas kelas bersyarat secara paralel.
- Setiap kotak pembatas direpresentasikan oleh lima elemen prediksi: koordinat pusat kotak ($x, y$), dimensi lebar dan tinggi kotak ($w, h$), serta nilai kepercayaan (*confidence*) bahwa kotak tersebut benar-benar melokalisasi wilayah lesi infeksi paru.
- Bersamaan dengan itu, probabilitas kelas memprediksi jenis penyakit paru dari sembilan kemungkinan kelas yang tersedia (termasuk COVID-19) untuk setiap wilayah terdeteksi.

### Penekanan Non-Maksimum (NMS)
Pada fase inferensi, model YOLO sering kali menghasilkan beberapa kotak pembatas yang tumpang tindih untuk satu wilayah infeksi yang sama. Untuk menyaring hasil deteksi tersebut, algoritme penekanan non-maksimum (*Non-Maximum Suppression* atau NMS) diterapkan. NMS bekerja dengan membandingkan nilai *Intersection over Union* (IoU) antar-kotak pembatas yang tumpang tindih. Kotak dengan skor kepercayaan tertinggi dipertahankan, sedangkan kotak lainnya yang memiliki nilai tumpang tindih melebihi ambang batas IoU yang ditentukan (misalnya IoU > 0,5) akan dieliminasi, sehingga menghasilkan representasi visual diagnosis yang bersih dan tepat bagi klinisi.

## Eksperimen dan Hasil

Evaluasi kinerja sistem CAD yang diusulkan oleh Al-Antari dkk. dilakukan dengan menggunakan dataset gabungan berskala besar yang terdiri dari total **50.490 citra CXR digital**. Basis data ini dibangun dengan menggabungkan sampel citra pasien terinfeksi COVID-19 dari repositori publik (seperti milik Cohen dkk.) dengan dataset penyakit paru-paru umum **ChestX-ray8** yang dirilis oleh *National Institutes of Health* (NIH). Penggunaan dataset gabungan ini bertujuan untuk melatih model agar mampu mendiferensiasi patologi pernapasan secara spesifik, bukan sekadar melakukan klasifikasi biner sederhana (COVID-19 vs normal).

Protokol pengujian menerapkan skema **validasi silang 5-lipat** (*five-fold cross-validation*), di mana dataset dibagi menjadi lima bagian yang sama. Secara bergiliran, empat bagian digunakan sebagai data pelatihan dan satu bagian digunakan sebagai data pengujian, kemudian seluruh hasil rata-rata dari kelima lipatan dihitung untuk menghindari bias pemilihan data. Sistem ini diuji untuk membedakan sembilan kelas patologi pernapasan yang meliputi: COVID-19, atelektasis (*atelectasis*), infiltrasi (*infiltration*), pneumotoraks (*pneumothorax*), massa (*masses*), efusi (*effusion*), pneumonia non-COVID (*pneumonia*), kardiomegali (*cardiomegaly*), dan nodul (*nodules*), serta paru-paru normal.

Hasil eksperimen kuantitatif utama dari penelitian ini adalah sebagai berikut:
- **Akurasi Deteksi Lokalisasi:** Mencapai **96,31%** dengan rata-rata nilai IoU lebih tinggi dari **90%**, membuktikan ketelitian lokalisasi kotak pembatas pada area lesi paru yang terinfeksi.
- **Akurasi Klasifikasi Multi-Kelas:** Mencapai **97,40%** dalam membedakan secara spesifik antara COVID-19, pneumonia non-COVID, penyakit paru lainnya, dan paru-paru sehat.
- **Kecepatan Inferensi:** Waktu pemrosesan rata-rata per citra tercatat sebesar **0,0093 detik**, yang setara dengan *throughput* sebesar **108 FPS**.
- **Efek Strategi Pra-Pemrosesan:** Penerapan langkah penyeimbangan data dan augmentasi data yang diusulkan terbukti meningkatkan akurasi keseluruhan sebesar **6,64%** dan skor F1 sebesar **12,17%** dibandingkan dengan model yang dilatih tanpa skema penyeimbangan data.

Dalam studi perbandingan dengan model pembanding, performa prediktor YOLO ini disandingkan dengan arsitektur CNN populer seperti VGG-16, VGG-19, ResNet-50, dan Inception-v3. Meskipun model klasifikasi murni seperti ResNet-50 mampu memberikan akurasi klasifikasi tingkat citra (*image-level classification*) yang bersaing (sekitar 95%–96%), model-model tersebut tidak memiliki kemampuan alami untuk melokalisasi posisi anatomi lesi paru secara langsung. Untuk melakukan lokalisasi, model CNN klasifikasi tersebut harus dikombinasikan dengan arsitektur segmentasi sekunder seperti U-Net, yang secara drastis meningkatkan kebutuhan memori komputasi dan menurunkan kecepatan pemrosesan di bawah batas aman untuk aplikasi klinis interaktif. Sebaliknya, prediktor YOLO satu tahap menawarkan visualisasi lokalisasi lesi instan dengan kecepatan inferensi 108 FPS yang jauh melampaui seluruh model pembanding dua tahap atau model hibrida multi-tahap.

## Kelebihan dan Keterbatasan

Secara objektif, sistem CAD yang diajukan oleh Al-Antari dkk. memiliki sejumlah keunggulan taktis dan beberapa keterbatasan yang perlu diperhatikan dalam implementasi klinis riil.

### Kelebihan:
1. **Kecepatan Inferensi Sangat Tinggi:** Latensi pemrosesan sebesar 0,0093 detik (108 FPS) membuat sistem ini sangat ideal untuk diintegrasikan ke dalam alur kerja klinik dengan beban kerja tinggi. Sistem ini memungkinkan pemeriksaan seketika saat dokter mengunggah citra CXR.
2. **Arsitektur Terpadu Satu Tahap:** Desain *end-to-end* yang menyatukan lokalisasi lesi dan klasifikasi penyakit dalam satu jaringan meminimalisasi overhead komputasi dan menyederhanakan proses penerapan (*deployment*) perangkat lunak di rumah sakit.
3. **Validasi Data Skala Besar:** Penggunaan lebih dari 50.000 citra CXR memberikan landasan statistik yang kuat, sehingga mengurangi keraguan terhadap keandalan generalisasi model jika dibandingkan dengan penelitian sejenis yang hanya menggunakan ratusan sampel citra.
4. **Efektivitas Penyeimbangan Data:** Metodologi penyeimbangan data terbukti secara empiris meningkatkan sensitivitas terhadap kelas minoritas seperti COVID-19, meminimalkan tingkat positif palsu yang dapat memicu kepanikan klinis.

### Keterbatasan:
1. **Ketergantungan pada Lapisan Terhubung Penuh (FC):** Secara konseptual, penggunaan lapisan terhubung penuh pada ujung prediksi YOLO membatasi ukuran citra masukan harus selalu tetap (*fixed input size*). Hal ini memaksa penerapan operasi pengecilan resolusi (*downsampling*) pada citra rontgen dada digital beresolusi sangat tinggi, yang berpotensi menghilangkan detail patologis berukuran mikro.
2. **Keterbatasan Sensitivitas Lesi Difus:** Secara konseptual, model deteksi objek berbasis kotak pembatas persegi (*rectangular bounding box*) seperti YOLO kurang optimal untuk melokalisasi area lesi infeksi paru yang bersifat difus (tersebar luas tanpa batas tegas) atau memiliki bentuk geometris yang sangat ireguler, yang sering kali ditemui pada kasus pneumonia bilateral parah.
3. **Derau Anotasi Dataset:** Dari sisi rekayasa klinis, meskipun dataset NIH ChestX-ray8 berukuran besar, label patologinya diekstraksi secara otomatis menggunakan pemrosesan bahasa alami (*natural language processing*) dari laporan radiologi tekstual asli, yang diketahui mengandung tingkat derau pelabelan (*label noise*) tertentu. Hal ini berpotensi memengaruhi bias keakuratan *ground-truth* saat pelatihan model deteksi.

## Kaitan dengan Bab Lain

Sebagai bagian dari klaster **Medis** dalam peta jalan tinjauan pustaka ini, bab ini memiliki keterkaitan erat dengan beberapa bab lainnya:
- **Keterkaitan dengan [Bab 128](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md) (Tinjauan Sistematis YOLO Medis):** Bab ini mengonfirmasi secara empiris tren yang dilaporkan oleh Qureshi dkk. (2024) mengenai dominasi pemakaian detektor satu tahap (keluarga YOLO) untuk mempercepat transisi dari eksperimen laboratorium menuju sistem pendukung keputusan klinis. Khususnya, skema penambahan lapisan dan penyeimbangan data pada citra radiologi rontgen dada (CXR) untuk patologi paru menjadi salah satu pilar aplikasi utama YOLO medis dalam kurun waktu 2018–2023.
- **Kesejajaran dengan [Bab 130](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md) (Deteksi Lesi Payudara dengan YOLO Fusion):** Pendekatan Al-Antari dkk. yang menyatukan deteksi lokalisasi dan klasifikasi dalam satu kerangka kerja sejalan dengan konsep fusi fitur berbasis YOLO yang diusulkan oleh Baccouche dkk. (2021). Namun, sementara Baccouche dkk. memfokuskan model fusi untuk klasifikasi biner jinak/ganas pada mamografi payudara, Al-Antari dkk. menangani klasifikasi multi-kelas 10 kategori (9 patologi pernapasan dan 1 normal) pada organ paru dengan penekanan pada optimasi kecepatan inferensi.
- **Perbandingan dengan [Bab 131](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md) (Modified YOLOv5 Payudara):** Mohiyuddin dkk. (2022) memodifikasi modul internal YOLOv5 (*BottleneckCSP*) untuk meminimalkan beban parameter komputasi pada citra mamogram. Al-Antari dkk. memilih pendekatan yang lebih sederhana dengan mengandalkan 23 lapisan konvolusi berurutan konvensional, tetapi dengan fokus kompensasi performa pada langkah pra-pemrosesan penyeimbangan data agresif untuk mengatasi ketidakseimbangan kelas.
- **Korelasi dengan [Bab 132](./132%20-%202023%20-%20YOLO%20untuk%20Deteksi%20Polip%20%28Wan%20dkk.%29%20-%20Medis.md) (Deteksi Polip Kolonoskopi):** Wan dkk. (2023) menggunakan YOLO untuk deteksi objek medis berkecepatan tinggi dalam skenario kolonoskopi video waktu nyata yang sensitif terhadap latensi. Kecepatan inferensi 108 FPS yang dicapai oleh Al-Antari dkk. pada citra statis CXR memberikan bukti komplementer bahwa performa komputasi keluarga YOLO sangat siap untuk mendukung diagnosis klinis interaktif waktu nyata di berbagai modalitas medis yang berbeda.

## Poin untuk Sitasi

- **Kunci BibTeX:** `alantari2020covid`
- **Ringkasan Sitasi:** Al-Antari dkk. (2021) mengusulkan sistem Computer-Aided Diagnosis (CAD) berbasis YOLO-predictor terintegrasi satu tahap untuk mendeteksi dan mengklasifikasikan lesi infeksi COVID-19 secara cepat dari citra rontgen dada digital (CXR). Melalui pelatihan menggunakan dataset gabungan 50.490 citra CXR (termasuk ChestX-ray8), model ini mampu membedakan COVID-19 dari 8 penyakit paru lainnya dengan akurasi deteksi 96,31%, klasifikasi 97,40%, serta kecepatan inferensi luar biasa sebesar 108 FPS (0,0093 detik per citra), menjadikannya sangat andal untuk triase klinis darurat.
- **Catatan Verifikasi Nilai:** 
  1. Nilai akurasi klasifikasi 97,40% dan akurasi deteksi 96,31% dicapai setelah pengaplikasian teknik penyeimbangan data (*data balancing*) dan augmentasi data yang berkontribusi meningkatkan akurasi keseluruhan sebesar 6,64% dan F1-score sebesar 12,17%.
  2. Throughput kecepatan sebesar 108 FPS (0,0093 detik per citra) diperoleh pada spesifikasi komputasi stasiun kerja laboratorium khusus; performa klinis nyata di lapangan dapat bervariasi tergantung pada spesifikasi unit pemroses grafis (GPU) lokal yang digunakan pada fasilitas kesehatan terkait.
