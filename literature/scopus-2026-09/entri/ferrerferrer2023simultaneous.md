# Simultaneous fruit detection and size estimation using multitask deep neural networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ferrerferrer2023simultaneous` |
| Judul asli | Simultaneous fruit detection and size estimation using multitask deep neural networks |
| Penulis | Ferrer-Ferrer, Mar; Ruiz-Hidalgo, Javier; Gregorio, Eduard; Vilaplana, Ver\'onica; Morros, Josep-Ramon; Gen\'e-Mola, Jordi |
| Tahun | 2023 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [ferrerferrer2023simultaneous.pdf](../pdf/ferrerferrer2023simultaneous.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2023.07.010

## Gambaran Umum

Penelitian ini mengatasi pengukuran ukuran buah apel di kebun untuk memperkirakan hasil panen dan merencanakan sumber daya panen. Pengukuran konvensional memakai jangka sorong secara manual sehingga hanya sebagian buah yang terukur dan hasilnya bersifat perkiraan. Penulis juga mencatat tantangan generalisasi, yakni metode harus mampu mengukur buah pada berbagai tahap pertumbuhan. Tujuan penelitian ini adalah mendeteksi buah sekaligus mengestimasi diameternya dalam satu jaringan terlatih akhir-ke-akhir (*end-to-end*) tanpa target kalibrasi yang ditempatkan pada jarak sama dengan buah.

Data berasal dari himpunan PFuji-Size yang dianotasi ulang menjadi citra RGB-D apel Fuji. Peta kedalaman dibangun dari awan titik tiga dimensi memakai *structure from motion* (SfM) dan *multi-view stereo* (MVS) dengan perangkat lunak Metashape. Anotasi mencakup topeng segmentasi instans, diameter hasil ukuran jangka sorong, dan proyeksi dua dimensi dari topeng bola tiga dimensi. Total 15.335 apel teranotasi dengan diameter 27–95 mm, terdiri atas dua tahap pertumbuhan: BBCH85 (apel merah matang, Oktober 2018) dan BBCH77 (apel hijau sekitar 70% ukuran akhir, Juli 2020). Pembagian data memakai sisi barisan pohon: citra sisi barat untuk latih, citra sisi timur untuk validasi dan uji. Jumlah citra latih/validasi/uji berturut-turut 1.036/275/249 untuk BBCH77 dan 1.268/539/558 untuk BBCH85; jumlah anotasi 3.819/1.161/857 dan 4.760/2.288/2.450. Visibilitas buah didefinisikan sebagai V = Si/Ss × 100%, yaitu perbandingan luas topeng instans yang terlihat terhadap luas topeng bola terproyeksi.

Mekanisme deteksi memakai Mask R-CNN dua tahap dengan *backbone* ResNet-50 dan *Feature Pyramid Network* (FPN) untuk segmentasi instans. Kanal kedalaman ditambahkan pada masukan RGB menjadi empat kanal memakai fusi awal (*early fusion*), sehingga-filter konvolusi pertama berubah dari tiga menjadi empat tanpa mengubah akurasi deteksi. Cabang estimasi diameter (*Diameter Head*) ditambahkan sebagai cabang regresi: keluaran empat level FPN digabungkan dengan peta kedalaman yang diubah ukurannya ke empat resolusi, dicocokkan dengan kotak dari *Box Head* memakai RoI Align, lalu melalui tiga konvolusi 2D, satu dekonvolusi, dan satu lapisan linear untuk memprediksi diameter. Konfigurasi terbaik hasil pencarian grid adalah laju pembelajaran 2×10⁻⁴, ukuran kumpulan 2, dan 128 RoI per kumpulan; ambang IoU 0,5, NMS 0,1, dan keyakinan 0,7 untuk deteksi serta 0,99 untuk estimasi diameter.

Hasil pengujian menunjukkan F1-score deteksi 0,88 dan AP 0,73 secara keseluruhan (AP 0,69 untuk BBCH77 dan 0,75 untuk BBCH85), dengan presisi 0,89 dan recall 0,87. Estimasi diameter menghasilkan MAE 5,64 mm, RMSE 7,77 mm, MAPE 7,96%, dan R² 0,66 untuk gabungan kedua tahap; MAE per tahap 4,16 mm (BBCH77) dan 6,22 mm (BBCH85). Membatasi pengukuran pada buah dengan visibilitas di atas 65% menurunkan MAE menjadi 5,09 mm dan menaikkan R² dari 0,66 menjadi 0,77. Kecepatan pemrosesan 0,1439 detik per citra atau 6,95 citra per detik pada GPU NVIDIA GeForce GTX 1080 Ti. Metrik dihitung pada himpunan uji memakai protokol penulis dengan ambang yang dipilih pada himpunan validasi; perbandingan dengan literature lain memakai rentang MAE 3,5–12,4 mm.

Batasan yang dinyatakan penulis meliputi kebutuhan anotasi topeng dan diameter ground truth dalam jumlah besar. Buah yang terlewat umumnya tertutup daun, batang, atau buah lain serta berada di tepi citra dengan bagian terlihat sangat kecil; apel hijau lebih sulit karena warnanya mirip daun dan jumlah contoh latihnya lebih sedikit. Model cenderung melebihkan ukuran apel kecil (MBE 0,93 mm) dan mengurangkan ukuran apel besar (MBE −1,74 mm) karena tidak dilatih untuk ukuran tertentu. Peta kedalaman berasal dari SfM yang memerlukan banyak citra, sehingga penulis mengusulkan pengujian peta kedalaman dari kamera komersial pada penelitian lanjutan. Penulis juga menyatakan hasil dapat berbeda pada kondisi pencahayaan atau jarak kamera–pohon yang sangat berbeda serta mengusulkan identifikasi otomatis buah paling terlihat untuk membuang prediksi buah tersembunyi.
