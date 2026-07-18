# 128 - A Comprehensive Systematic Review of YOLO for Medical Object Detection (2018 to 2023)

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qureshi2024medyolo` |
| Judul asli | A Comprehensive Systematic Review of YOLO for Medical Object Detection (2018 to 2023) |
| Penulis | Mohammed Gamal Ragab, Said Jadid Abdulkadir, Amgad Muneer, Alawi Alqushaibi, Ebrahim Hamid Sumiea, Rizwan Qureshi, Safwan Mahmood Al-Selwi, Hitham Alhussian |
| Tahun | 2024 |
| Venue | IEEE Access |
| Tema | Medis |

## Tautan Akses
- **IEEE Xplore (Resmi):** https://doi.org/10.1109/ACCESS.2024.3386826
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Comprehensive%20Systematic%20Review%20of%20YOLO%20for%20Medical%20Object%20Detection%20%282018%20to%202023%29
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Comprehensive%20Systematic%20Review%20of%20YOLO%20for%20Medical%20Object%20Detection%20%282018%20to%202023%29&sort=relevance

## Gambaran Umum

Makalah ini menyajikan sebuah tinjauan sistematis komprehensif mengenai penerapan keluarga algoritme *You Only Look Once* (YOLO) dalam domain deteksi objek medis dari tahun 2018 hingga 2023. Ragab dkk. (2024) melakukan kurasi ketat terhadap literatur ilmiah untuk memetakan bagaimana detektor satu tahap (*one-stage detector*) ini diadaptasi guna memenuhi spesifikasi klinis. Penapisan sistematis menggunakan protokol PRISMA (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses*) menghasilkan 124 studi utama yang dianalisis secara mendalam.

Tinjauan ini mengklasifikasikan penggunaan YOLO berdasarkan modalitas citra medis (seperti radiologi, endoskopi, dan patologi), versi model yang digunakan (dari YOLOv3 hingga YOLOv8), serta organ sasaran deteksi. Hasil sintesis menunjukkan bahwa YOLO mampu memberikan keseimbangan optimal antara akurasi diagnostik dan kecepatan inferensi, yang sangat penting untuk aplikasi *real-time* (deteksi seketika). Di samping itu, makalah ini mengidentifikasi tantangan mendasar seperti kurangnya standarisasi anotasi medis, ketidakseimbangan kelas (*class imbalance*), serta kendala dalam mengenali lesi kecil.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Diagnosis medis berbantuan komputer (*computer-aided diagnosis* atau CAD) telah mengalami pergeseran paradigma sejak adopsi teknik pembelajaran mendalam (*deep learning*). Sebelum adopsi detektor satu tahap, deteksi objek medis didominasi oleh detektor dua tahap (*two-stage detectors*) seperti Faster R-CNN. Model dua tahap ini memisahkan proses deteksi menjadi fase usulan wilayah kandidat (*region proposal*) dan fase klasifikasi objek pada wilayah tersebut. Meskipun memiliki tingkat akurasi yang tinggi, model dua tahap memiliki keterbatasan komputasi berupa latensi yang tinggi. Hal ini menghambat penerapannya pada skenario klinis interaktif, seperti kolonoskopi video langsung atau panduan navigasi bedah waktu nyata (*real-time surgical guidance*).

Ketika para peneliti berupaya mengadopsi detektor satu tahap seperti YOLO untuk mengejar kecepatan inferensi, mereka menghadapi fragmentasi metodologis yang besar. Setiap studi cenderung merancang modifikasi arsitektur secara mandiri tanpa adanya konsensus mengenai metode kustomisasi mana yang paling efektif untuk modalitas citra tertentu. Karakteristik citra medis sangat berbeda dengan citra dunia nyata pada umumnya (natural images). Citra medis memiliki batas-batas lesi yang kabur, kontras yang rendah antara jaringan sehat dan sakit, serta ukuran objek patologis yang sering kali sangat kecil (mikro).

Selain itu, penyebaran literatur yang terfragmentasi menyulitkan para rekayasawan kecerdasan buatan dalam menentukan versi YOLO terbaik dan skema modifikasi *backbone* (ekstraktor fitur) atau *attention mechanism* (mekanisme atensi) yang sesuai. Oleh karena itu, diperlukan sebuah studi penelaahan sistematis yang mampu menyintesis seluruh bukti empiris untuk mengidentifikasi tren metodologi, memetakan hasil performa, dan menetapkan arah riset berikutnya.

## Ide Utama

Gagasan utama dari makalah ini adalah menyusun taksonomi komprehensif dan sintesis performa dari 124 studi YOLO medis untuk menyembuhkan fragmentasi literatur. Penulis mengklasifikasikan kontribusi ilmiah ke dalam tiga sumbu utama: modalitas citra klinis, evolusi arsitektur YOLO yang digunakan, dan bagian anatomi tubuh yang ditargetkan.

Melalui pendekatan ini, makalah menyajikan analisis mekanis mengenai bagaimana komponen utama YOLO—yaitu *backbone* (ekstraktor fitur), *neck* (jaringan penggabung fitur), dan *head* (kepala prediksi)—dimodifikasi untuk mengatasi tantangan visual citra medis. Dengan menyandingkan berbagai hasil eksperimen, penelitian ini mengidentifikasi kelebihan dan keterbatasan YOLO saat diterapkan pada berbagai kasus klinis nyata, serta merumuskan panduan untuk transisi dari eksperimen laboratorium menuju sistem pendukung keputusan klinis (*clinical decision support systems*).

## Cara Kerja Langkah demi Langkah

### Protokol Seleksi Studi PRISMA
Penulis menggunakan protokol PRISMA untuk menyaring literatur secara transparan. Proses seleksi ini digambarkan pada diagram alir berikut:

```
[Tahap 1: Identifikasi]
  Pencarian basis data PubMed dengan kueri:
  (YOLO AND ((medical application) OR (medical image)))
  dibatasi pada rentang publikasi 2018-2023.
                    │
                    ▼
[Tahap 2: Penyaringan Awal]
  Pemeriksaan judul dan abstrak naskah.
  Eksklusi: naskah non-Inggris, artikel ulasan tanpa data orisinal,
  dan studi non-medis.
                    │
                    ▼
[Tahap 3: Kelayakan Teks Lengkap]
  Evaluasi kelayakan artikel secara mendalam.
  Eksklusi: studi tanpa metrik performa kuantitatif yang jelas
  (mAP, precision, recall).
                    │
                    ▼
[Tahap 4: Inklusi Akhir]
  Diperoleh 124 studi utama yang memenuhi syarat untuk
  disintesis secara kualitatif dan kuantitatif.
```

### Taksonomi Berdasarkan Modalitas Citra Medis
Aplikasi YOLO dalam kajian ini dikelompokkan ke dalam empat modalitas klinis utama yang memiliki tantangan pemrosesan visual tersendiri:

1. **Radiologi (X-ray, CT, MRI)**: 
   - *X-ray*: Deteksi patologi paru-paru seperti pneumonia, tuberkulosis, dan COVID-19. Tantangan utamanya adalah tumpang tindih struktur tulang rusuk yang dapat mengaburkan lesi paru.
   - *CT (Computed Tomography) & MRI (Magnetic Resonance Imaging)*: Deteksi objek tiga dimensi (3D) seperti tumor otak atau kista ginjal. Karena YOLO adalah detektor dua dimensi (2D), citra 3D harus diproses per irisan (*slice-by-slice*) atau dimodifikasi menggunakan pendekatan pseudo-3D.
2. **Endoskopi**:
   - Skrining polip kolorektal secara otomatis selama kolonoskopi. Di sini, kecepatan pemrosesan frame video sangat penting (minimal 30 FPS) untuk mencegah latensi visual bagi dokter yang sedang mengoperasikan kamera endoskopi.
3. **Patologi / Mikroskopi**:
   - Lokalisasi sel kanker, penghitungan sel darah merah/putih, serta identifikasi parasit pada preparat apusan darah. Tantangannya adalah kepadatan objek yang sangat tinggi dalam satu bidang pandang citra.
4. **Mamografi**:
   - Deteksi lesi dan massa payudara. Citra mamografi memiliki tingkat kerapatan jaringan yang tinggi, sehingga mendeteksi mikroklasifikasi yang sangat kecil membutuhkan resolusi masukan yang tinggi.

### Sebaran Versi YOLO dan Kustomisasi Arsitektural
Sintesis studi menunjukkan evolusi pemakaian versi YOLO dalam kurun 2018–2023. YOLOv3 dan YOLOv5 menjadi versi yang paling dominan digunakan. YOLOv3 banyak dipakai pada studi awal karena kestabilannya dan dukungan deteksi multi-skala melalui *Feature Pyramid Network* (FPN). YOLOv5 mendominasi studi setelah tahun 2020 karena fleksibilitas kodenya dalam PyTorch dan ketersediaan berbagai ukuran model (*nano*, *small*, *medium*, *large*, *extra-large*). YOLOv7 dan YOLOv8 mulai diadopsi pada akhir rentang survei untuk meningkatkan presisi deteksi tanpa memperlambat kecepatan inferensi.

Untuk menyesuaikan YOLO dengan karakteristik citra medis, para peneliti menerapkan tiga kategori modifikasi utama:

```
                  Kategori Modifikasi YOLO Medis
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
[Modifikasi Backbone]       [Integrasi Atensi]         [Desain Skala Fitur]
- Substitusi dengan         - CBAM (spasial & kanal)   - Penambahan lapisan
  MobileNet/ShuffleNet      - SE (bobot kanal)           deteksi objek mikro
- Pengurangan parameter     - CA (koordinat spasial)   - Fusi fitur resolusi
  untuk edge device         - Memperjelas area lesi      tinggi pada neck
```

1. **Modifikasi Backbone**: Mengganti modul ekstraksi fitur bawaan YOLO (seperti CSPDarknet) dengan arsitektur yang lebih ringan seperti MobileNet atau GhostNet untuk implementasi perangkat keras medis portabel, atau dengan ResNet untuk ekstraksi fitur yang lebih mendalam.
2. **Integrasi Mekanisme Atensi**: Menyisipkan modul atensi seperti *Convolutional Block Attention Module* (CBAM), *Squeeze-and-Excitation* (SE), atau *Coordinate Attention* (CA) untuk memfokuskan bobot jaringan pada wilayah patologis yang samar dan menekan representasi derau (*noise*) jaringan sehat.
3. **Desain Skala Fitur pada Neck**: Menambahkan lapisan prediksi ekstra pada skala resolusi yang lebih tinggi (misalnya, pada ukuran fitur 160×160 untuk citra masukan 640×640) guna menangkap objek patologis berukuran mikro yang sering kali hilang akibat operasi *pooling* berulang.

## Eksperimen dan Hasil

Karena makalah ini merupakan sebuah tinjauan sistematis, hasil eksperimen yang disajikan merupakan kompilasi dan perbandingan metrik kinerja dari 124 studi primer yang ditinjau. Penulis menyintesis kinerja YOLO berdasarkan domain tugas klinis utama:

### Deteksi Kelainan Radiologi Dada (X-ray)
Studi-studi yang mengevaluasi YOLO untuk penyaringan COVID-19 dan pneumonia menggunakan dataset publik (seperti ChestX-ray8 atau dataset tantangan RSNA) melaporkan tingkat akurasi yang tinggi. Model YOLOv3 dan YOLOv5 yang dimodifikasi mencapai skor mAP (*mean Average Precision*) berkisar antara 88,2% hingga 94,5%. Sebagai contoh, dalam pendeteksian pola infiltrat pneumonia, YOLOv3 mampu berjalan dengan kecepatan lebih dari 40 FPS, mengungguli Faster R-CNN yang hanya mencatatkan kecepatan sekitar 8 FPS dengan mAP yang relatif setara.

### Skrining Polip Kolorektal (Endoskopi)
Pada deteksi polip menggunakan dataset Kvasir-SEG atau CVC-ClinicDB, model YOLOv5-tengah (*YOLOv5m*) dan YOLOv8 yang dioptimalkan mencapai mAP di atas 91,2% dengan sensitivitas (*recall*) sebesar 89,7%. Keunggulan utama YOLO dalam modalitas ini adalah kecepatannya yang melampaui 55 FPS pada GPU standar. Performa ini sangat memenuhi syarat untuk integrasi langsung ke dalam sistem video endoskopi *real-time*, membantu dokter melokalisasi polip kecil yang mungkin terlewatkan selama prosedur pemindaian manual.

### Diagnosis Lesi Payudara (Mamografi)
Untuk deteksi massa payudara pada dataset DDSM atau CBIS-DDSM, modifikasi YOLO dengan penambahan modul CBAM menunjukkan peningkatan sensitivitas dari 82,4% (pada model standar) menjadi 90,8%. Hal ini krusial karena dalam diagnosis kanker payudara, meminimalkan tingkat *false negative* (kanker yang tidak terdeteksi) jauh lebih penting daripada menekan *false positive* (alarm palsu).

Tabel berikut merangkum rentang performa umum keluarga YOLO di berbagai modalitas medis yang disintesis dalam tinjauan ini:

| Modalitas | Target Deteksi | Model YOLO Dominan | Rentang mAP (%) | Kecepatan Inferensi |
|---|---|---|---|---|
| Radiologi (X-ray) | Pneumonia, COVID-19 | YOLOv3, YOLOv5 | 88,0 – 95,0 | Tinggi (>40 FPS) |
| Radiologi (CT/MRI) | Tumor Otak, Nodul Paru | YOLOv5, YOLOv7 | 85,0 – 92,0 | Sedang (20–30 FPS) |
| Endoskopi | Polip Gastrointestinal | YOLOv5, YOLOv8 | 89,0 – 96,0 | Sangat Tinggi (>50 FPS) |
| Patologi | Sel Kanker, Mikroba | YOLOv4, YOLOv5 | 86,0 – 93,0 | Sedang (15–30 FPS) |

## Kelebihan dan Keterbatasan

### Kelebihan
Tinjauan sistematis ini memberikan landasan teoretis dan praktis yang kokoh bagi peneliti AI medis dengan beberapa keunggulan utama:
1. Menyediakan peta jalan taksonomi yang terstruktur dengan baik, membantu peneliti memilih versi YOLO dan strategi modifikasi yang paling relevan berdasarkan karakteristik unik dari modalitas citra yang dihadapi.
2. Menggunakan metodologi PRISMA secara ketat pada basis data PubMed, yang menjamin bahwa artikel yang dianalisis memiliki kredibilitas akademis yang tinggi dan meminimalkan bias seleksi.
3. Menganalisis transisi penting dari model berbasis jangkar (*anchor-based*) ke model bebas jangkar (*anchor-free*) dalam konteks pencitraan klinis.

### Keterbatasan
Meskipun menyajikan ulasan yang sangat rinci, terdapat beberapa batasan penting yang perlu dicatat:
1. *Secara konseptual*, ulasan ini bersifat mengompilasi klaim dari penulis naskah asli tanpa melakukan pengujian ulang (*benchmark* independen) secara langsung pada lingkungan komputasi yang seragam. Hal ini memicu heterogenitas data karena perbedaan ukuran resolusi citra masukan, rasio pembagian data latih/uji, serta teknik augmentasi citra yang digunakan pada masing-masing studi primer.
2. *Dari sisi rekayasa*, terdapat bias publikasi di mana studi dengan hasil negatif atau performa rendah cenderung tidak dipublikasikan, sehingga sintesis performa YOLO dalam tinjauan ini mungkin tampak terlalu optimistis dibandingkan dengan kinerja aslinya di dunia klinis nyata.
3. Rentang waktu studi dibatasi hingga akhir tahun 2023, yang menyebabkan model YOLO versi terbaru (seperti YOLOv9, YOLOv10, dan YOLOv11) belum tercakup dalam analisis ini.

## Kaitan dengan Bab Lain

Sebagai sebuah bab tinjauan sistematis, entri ini bertindak sebagai payung literatur yang menghubungkan berbagai implementasi YOLO pada klaster **Medis**. Secara khusus, bab ini memiliki hubungan silsilah langsung dengan bab-bab berikut:

- **Bab 129 ([129 - 2021 - COVID-19 CAD dari X-Ray (Al-Antari dkk.) - Medis](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md))**: Menyediakan studi kasus nyata penerapan YOLOv3 untuk deteksi patologi COVID-19 pada citra rontgen dada (*chest X-ray*), yang menjadi contoh awal dominasi YOLOv3 dalam kategori radiologi dada yang dibahas dalam tinjauan Ragab dkk.
- **Bab 130 ([130 - 2021 - Breast Lesion Detection (YOLO Fusion) - Medis](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md))** dan **Bab 131 ([131 - 2022 - Breast Tumor Detection (Modified YOLOv5) - Medis](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md))**: Menyajikan solusi konkret atas masalah deteksi lesi kecil pada citra mamografi melalui teknik fusi citra (*image fusion*) dan modifikasi *backbone* YOLOv5 dengan blok atensi, memvalidasi taksonomi strategi modifikasi yang dipetakan dalam bab survei ini.
- **Bab 132 ([132 - 2023 - YOLO untuk Deteksi Polip (Wan dkk.) - Medis](./132%20-%202023%20-%20YOLO%20untuk%20Deteksi%20Polip%20%28Wan%20dkk.%29%20-%20Medis.md))**: Menunjukkan implementasi nyata dari kategori modalitas endoskopi, di mana tuntutan pemrosesan video berbingkai tinggi secara *real-time* dipenuhi oleh kustomisasi arsitektur YOLOv5 untuk membantu deteksi polip secara instan selama prosedur medis aktif.

## Poin untuk Sitasi

Kutipan akademis untuk bab ini menggunakan kunci BibTeX berikut:
```bibtex
@article{qureshi2024medyolo,
  author    = {Ragab, Mohammed Gamal and Abdulkadir, Said Jadid and Muneer, Amgad and Alqushaibi, Alawi and Sumiea, Ebrahim Hamid and Qureshi, Rizwan and Al-Selwi, Safwan Mahmood and Alhussian, Hitham},
  title     = {A Comprehensive Systematic Review of YOLO for Medical Object Detection (2018 to 2023)},
  journal   = {IEEE Access},
  volume    = {12},
  pages     = {57815--57836},
  year      = {2024},
  doi       = {10.1109/ACCESS.2024.3386826}
}
```

Ringkasan berikut aman digunakan dalam tinjauan pustaka karya ilmiah formal:
> Ragab dkk. (2024) melakukan tinjauan sistematis terhadap 124 studi primer terkait penerapan algoritme YOLO untuk deteksi objek medis sepanjang periode 2018 hingga 2023. Tinjauan tersebut menunjukkan bahwa modifikasi arsitektur seperti integrasi mekanisme atensi (atensi CBAM atau koordinat) dan penambahan detektor skala kecil pada jaringan penggabung fitur sangat krusial dalam mengatasi keterbatasan kontras rendah dan lesi mikro pada modalitas radiologi, endoskopi, dan patologi.

Catatan verifikasi:
- Angka total 124 studi yang terpilih berasal dari hasil penyaringan PRISMA dalam artikel final yang diterbitkan pada IEEE Access (2024).
- Angka rentang mAP (85%–96%) serta perbandingan FPS antara YOLOv3/v5 (>40 FPS) dengan Faster R-CNN (8 FPS) didasarkan pada sintesis data sekunder dalam naskah asli dan perlu dikonfirmasi ulang pada studi primer yang dirujuk sebelum digunakan sebagai klaim performa mutlak.
