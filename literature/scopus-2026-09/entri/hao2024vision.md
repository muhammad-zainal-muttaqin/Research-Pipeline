# A Vision-Based Two-Stage Fruit Outer Diameter Detection Method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hao2024vision` |
| Judul asli | A Vision-Based Two-Stage Fruit Outer Diameter Detection Method |
| Penulis | Hao, Yifei; Yan, Shuaizheng; Wu, Zhengxing; He, Bingwei; Li, Chenghua; Yu, Junzhi |
| Tahun | 2024 |
| Venue | IEEE International Conference on Robotics and Biomimetics Robio |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [hao2024vision.pdf](../pdf/hao2024vision.pdf)
- DOI resmi: https://doi.org/10.1109/robio64047.2024.10907381

## Gambaran Umum

Penulis menyebut pemantauan diameter luar sayuran rumah kaca penting untuk mengatur pertumbuhan buah dan rencana budi daya. Metode yang ada memiliki keterbatasan. Warna tomat hijau mirip latar. Foto dari atas memuat tangkai dan daun yang mengganggu pencocokan bentuk. Kotak pembatas harus sejajar tepi foto padahal tomat tumbuh dengan arah beragam. Kajian ini mengusulkan metode dua tahap untuk segmentasi tomat dan perhitungan diameter luar maksimum.

Data berupa citra RGB tomat di rumah kaca yang diambil dengan kamera *depth* Femto Bolt genggam: 1.125 citra, 1.000 dipertahankan setelah seleksi. Sudut dan kondisi pemotretan tidak distandarkan. Citra dibagi latih, uji, dan validasi dengan rasio 8:1:1, tanpa keterangan pembagian per tanaman. Pelatihan 300 *epoch*, ukuran *batch* 2, laju belajar 0,01, masukan 640x640. Pemberi label tidak disebut. Evaluasi pengukuran memakai 215 tomat pada 80 citra. Cara pengukuran nilai acuan (*ground truth*) tidak dijelaskan.

Tahap pertama adalah YOLOv8 yang disisipi *Convolutional Block Attention Module* (CBAM, modul yang membobot kanal dan lokasi fitur penting) untuk deteksi dan segmentasi. Tahap kedua menentukan apakah masker memuat tangkai, dengan ambang rasio piksel tangkai terhadap tomat 0,015 yang ditentukan dari lebih dari 40 sampel. Tanpa tangkai, dua piksel tepi terjauh dicari. Dengan tangkai, dipakai metode sumbu pusat. Diameter dihitung dengan kedalaman pada koordinat dunia, dan kedalaman perkiraan dipilih dengan pengelompokan DPC (*density peak clustering*).

Pada deteksi, YOLOv8_CBAM mencapai presisi 90,779% dan *recall* 86,335%, dibanding YOLOv8n presisi 90,175%, *recall* 82,609%, mAP50 93,209%, dan mAP50-95 73,667%. Metode usulan juga mencapai mAP50 94,632% dan mAP50-95 74,121%. Penulis menyebut kenaikan *recall* 4%. Dari 215 tomat, 23 tidak terdeteksi (21 berdiameter kurang dari 15 mm dan tidak dilabel) dan 12 terhalang sehingga tak terukur. Laju deteksi efektif 89,3%. Pada 180 tomat sisanya, R2 0,9264, MAE 4,61 mm, SDE 3,61 mm, MAPE 10,02%. Setelah data diberi pembersihan (masker kasus kedalaman buruk), R2 0,9349, MAE 4,27 mm, SDE 2,79 mm, MAPE 8,09%. Waktu proses 34 ms per citra.

Keterbatasan dari teks: tidak ada pencacahan, tidak ada penautan tomat antarcitra, dan tiap citra diproses sendiri. Evaluasi pada 80 citra dan satu rumah kaca. Pembagian citra tidak disebut per tanaman. Hasil "bersih" dibuat dengan membuang kasus kedalaman buruk. Cara pengukuran acuan tidak disebut. Penulis menyebut kekurangan informasi kedalaman dan tomat muda sebagai penyebab galat.
