# Pemeriksaan Ulang Eksklusi Tahap Judul dari Kueri Q1 dan Q3 (AI-2)

Dibuat `tools/scopus/verifikasi_ai2_judul.py`; jangan disunting tangan. Semua keputusan dibuat model bahasa besar dan **belum diperiksa manusia**.

- Rekaman yang diperiksa ulang: 1325 (dikeluarkan putaran pertama dari judul saja; kueri Q1 atau Q3).
- Dasar bukti: {'abstrak': 1017, 'judul': 292, 'abstrak (web)': 16}.
- Tetap dikeluarkan: 1294 ({'E5': 34, 'E1': 697, 'E2': 347, 'E3': 125, 'E6': 68, 'E4': 22, 'E7': 1}).
- Diusulkan masuk: 31; bertahan terhadap penyanggah dan dimasukkan: **19** ({'C1': 6, 'C2': 4, 'C5': 1, 'T': 2, 'C3': 6}); tidak bertahan: 12.

## Dimasukkan ke korpus

| idx | key | kode | dasar | judul |
|---|---|---|---|---|
| 7 | `awal2026development` | C1 | abstrak | Development of a plant sensing robot using virtual space and evaluation of its accuracy |
| 166 | `tan2025appleyolo` | C1 | abstrak (web) | AppleYOLO: Apple yield estimation method using improved YOLOv8 based on Deep OC-SORT |
| 216 | `cho2025case` | C1 | abstrak | A case study on the integration of a snapshot hyperspectral field-portable imager solving fruit quality assessment |
| 298 | `huang2024automatic` | C1 | abstrak (web) | An automatic tracking method for fruit abscission of litchi using convolutional networks |
| 330 | `xiao20243d` | C1 | abstrak (web) | 3D reconstruction and characterization of cotton bolls in situ based on UVA technology |
| 508 | `egi2022drone` | C1 | abstrak | Drone-Computer Communication Based Tomato Generative Organ Counting Model Using YOLO V5 and Deep-Sort |
| 289 | `kutyrev2024intelligent` | C2 | abstrak | Intelligent crop yield prediction system using neural networks and databases |
| 628 | `akiva2021ai` | C2 | abstrak | AI on the bog: Monitoring and evaluating cranberry crop risk |
| 778 | `silwal2016hierarchical` | C2 | abstrak | A hierarchical approach to apple identification for robotic harvesting |
| 793 | `silwal2015hierarchical` | C2 | abstrak | A hierarchical approach of apple identification for robotic harvesting |
| 1489 | `syahputra2026comparative` | C3 | abstrak | Comparative Analysis of Oil Palm Fruit Free Fatty Acid Estimation Using a Portable VIS-NIR Spectrometer and Multispectra |
| 1767 | `phimpisan2023real` | C3 | abstrak | Real-Time oil palm ripeness classification of fresh fruit bunches using fluorescence technology |
| 1991 | `melidawati2021non` | C3 | abstrak | Non destructive evaluation quality of oil palm fresh fruit bunch (FFB) (Elaeis guineensis Jack) based on optical propert |
| 2078 | `aliteh2020fruit` | C3 | abstrak | Fruit battery method for oil palm fruit ripeness sensor and comparison with computer vision method |
| 2368 | `cherie2015optical` | C3 | abstrak | Optical characteristics of oil palm fresh fruits bunch (FFB) under three spectrum regions influence for harvest decision |
| 2486 | `hudzari2012simulation` | C3 | abstrak | Simulation and modeling application in agricultural mechanization |
| 360 | `wagner2024mass` | C5 | abstrak | Mass Estimation of Soft Fruit via Oscillatory Plant Dynamics |
| 706 | `gray2019convolutional` | T | abstrak | A convolutional neural network for detecting sea turtles in drone imagery |
| 733 | `brack2018detection` | T | abstrak | Detection errors in wildlife abundance estimates from Unmanned Aerial Systems (UAS) surveys: Synthesis, solutions, and c |

## Diusulkan masuk tetapi tidak bertahan (tetap dikeluarkan)

| idx | usul | alasan penyanggah | judul |
|---|---|---|---|
| 87 | C1 | Objek yang dihitung adalah 'pineapple buds' (tunas), dan abstrak tidak menyatakan bahwa tunas tersebut adalah buah atau buah muda; protokol menyatakan hanya bunga atau organ vegetatif tanpa buah termasuk E1. Pelacakan StrongSORT dan akurasi hitung memang dilaporkan, tetapi syarat objek berupa buah pada tanaman tidak terbukti dari abstrak. | Real-Time Pineapple Bud Counting for Yield Estimation with YOLO11 and StrongSORT |
| 224 | T | Rekaman tidak memiliki abstrak; satu-satunya dasar adalah parafrasa hasil pencarian web yang tidak menyatakan bahwa metode itu menghitung objek multipandang dengan asosiasi identitas, sehingga tidak ada bukti positif untuk kode T. Tanpa abstrak berbahasa Inggris, aturan E7 mengarah ke pengecualian dan parafrasa tidak dapat menggantikan abstrak. | BPCS: Multi-view Bus Passenger Counting System |
| 478 | C1 | Abstrak resmi (diperoleh dari web) hanya melaporkan evaluasi mAP 96,02% pada 500 citra; DeepSORT disebut sebagai mekanisme penghitung pada video drone tanpa evaluasi hitungan terhadap acuan apa pun. Menurut aturan operasional, metrik deteksi saja adalah E5, sehingga bukti positif untuk C1 atau C2 yang mensyaratkan hitungan dievaluasi tidak ada. | DURIAN DETECTION AND COUNTING SYSTEM USING DEEP LEARNING |
| 1688 | C3 | Abstrak menggambarkan sensor laser titik dengan fotodetektor koaksial yang mengukur pantulan spektral, bukan perangkat pencitraan, sehingga memenuhi kriteria E6 (bukan sensor pencitraan) dan bukan metode berbasis citra. Peninjau sendiri menyebutnya sensor laser non-citra, dan abstrak tidak menyebut deteksi, penghitungan, atau lokalisasi tandan; pembuktian hanya terhadap kandungan minyak. | Laser remote sensor for oil palm fruit ripeness assessment |
| 1998 | C3 | Sensor yang dipakai adalah spektrometer optik 180-1100 nm yang mengukur reflektansi, yaitu sensor titik tanpa citra, sehingga tidak memenuhi syarat berbasis citra dan masuk E6 (bukan sensor pencitra). Abstrak tidak menyebut citra atau pencitraan sama sekali, dan penilai sendiri mengakui batas kelayakannya tipis. | Ripeness Classification of Oil Palm Fresh Fruit Bunches Using Optical Spectrometer and Support Vecto |
| 2218 | C3 | Abstrak menggambarkan spektroskopi Raman, yaitu pengukuran spektrum titik pada sampel tandan, bukan pencitraan; protokol meminta metode berbasis citra dan E6 mengecualikan sensor yang bukan pencitraan. Tinjauan sendiri mengakui bahwa sensornya bukan pencitraan, sehingga aturan objek tandan tidak cukup untuk memasukkannya sebagai C3. | Classification of oil palm Fresh Fruit Bunches (FFB) using Raman spectroscopy |
| 2220 | C3 | Abstrak memakai LED 670 nm dan sensor optik yang membaca nilai pantulan, tanpa citra, kamera, atau pencitraan multispektral, sehingga modalitas MSI tidak didukung bukti. Sensor ini bukan pencitraan (E6), dan abstrak hanya menyatakan hasil yang diharapkan tanpa evaluasi. | Non-Destructive Oil Palm Fresh Fruit Bunch (FFB) grading technique using optical sensor |
| 2428 | C3 | Abstrak pada berkas kosong dan satu-satunya bukti adalah parafrasa web yang hanya menyebut pita panjang gelombang, tanpa menyatakan bahwa sensor menghasilkan citra. Tanpa bukti pencitraan, kriteria C3 dan pengecualian E6 (bukan sensor pencitra) tidak dapat dipisahkan, sehingga inklusi tidak dapat dipertahankan. | Ripeness detection of oil palm fresh fruit bunches using 4-band sensors |
| 2435 | C3 | Warna buah diukur dengan spektroradiometer FieldSpec 3, yaitu instrumen spektral titik yang tidak menghasilkan citra, sehingga masuk E6 (bukan sensor pencitra) dan bukan C3. Abstrak tidak menyebut citra, kamera, maupun pemetaan spasial. | Oil palm fruit classification using spectrometer |
| 2460 | C3 | Pengukuran dilakukan dengan sensor fluoresensi genggam Multiplex 3 yang memindai tandan dan menghasilkan nilai rasio, bukan citra. Aturan E6 (bukan sensor pencitraan) berlaku, dan peninjau sendiri menandai kasus ini sebagai batas dengan keyakinan rendah. | Oil palm bunch ripeness classification using fluorescence technique |
| 2480 | C3 | Sensor empat pita aktif ini merekam reflektansi spektral titik, tanpa pembentukan citra, sehingga bukan pencitraan TBS dan jatuh ke E6. Abstrak tidak menyebut citra atau kamera. | Classification of oil palm fresh fruit bunches based on their maturity using portable four-band sens |
| 2481 | C3 | Data berasal dari sensor fluoresensi genggam Multiplex 3 yang menghasilkan kandungan flavonoid dan antosianin, bukan citra. Karena tidak ada pencitraan, studi ini termasuk E6 meskipun objeknya TBS sawit. | Determination of oil palm fresh fruit bunch ripeness-Based on flavonoids and anthocyanin content |
