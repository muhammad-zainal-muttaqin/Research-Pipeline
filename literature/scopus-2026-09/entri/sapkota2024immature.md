# Immature Green Apple Detection and Sizing in Commercial Orchards Using YOLOv8 and Shape Fitting Techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sapkota2024immature` |
| Judul asli | Immature Green Apple Detection and Sizing in Commercial Orchards Using YOLOv8 and Shape Fitting Techniques |
| Penulis | Sapkota, Ranjan; Ahmed, Dawood; Churuvija, Martin; Karkee, Manoj |
| Tahun | 2024 |
| Venue | IEEE Access |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [sapkota2024immature.pdf](../pdf/sapkota2024immature.pdf)
- DOI resmi: https://doi.org/10.1109/access.2024.3378261

## Gambaran Umum

Penelitian ini mengatasi masalah deteksi dan pengukuran ukuran apel hijau muda (fruitlet) pada tahap pertumbuhan awal di kebun komersial. Informasi jumlah dan ukuran buah pada tahap ini diperlukan untuk prediksi hasil, pengendalian hama, penipisan buah, serta perencanaan tenaga kerja dan logistik panen. Pengukuran konvensional memakai pita ukur atau alat pengukur buah memakan waktu dan tenaga, sedangkan sebagian besar kajian sebelumnya berfokus pada buah matang yang warnanya kontras dengan daun, sehingga mudah dipisahkan. Penulis menyatakan masih ada celah penelitian untuk buah yang kecil dan berwarna hijau serupa kanopi. Dua tujuan dicapai: membangun metode deteksi dan pengukuran berbasis YOLOv8 serta pencocokan bentuk tiga dimensi, dan membandingkan dua sensor RGB-D, yaitu Intel RealSense D435i dan Microsoft Azure Kinect DK.

Data dikumpulkan di kebun apel komersial di Prosser, Washington, Amerika Serikat, dengan kultivar Scifresh yang ditanam pada jarak baris 10 kaki dan jarak pohon 3 kaki. Pada 2022, sebanyak 1.079 citra kanopi diperoleh dari jarak 1–4 kaki, terdiri atas 534 citra RealSense dan 545 citra Azure, lalu diberi anotasi dengan Labelbox sehingga menghasilkan 5.921 label buah hijau muda. Pada 2023, kedua sensor dipasang bertumpuk pada lengan robot UR5e di atas kendaraan darat tak berawak Warthog, menghadap kanopi dari jarak sekitar 1 meter dengan kecepatan gerak 0,1 m/s, dari pangkal batang hingga lapisan cabang kelima. RealSense D435i memakai stereo infra merah aktif dan cahaya terstruktur dengan sensor kedalaman 1280 × 720 dan jangkauan sampai 10 m; Azure Kinect DK memakai time-of-flight dengan kamera warna 12 megapiksel dan sensor kedalaman 1 megapiksel pada mode narrow field-of-view. Evaluasi pengukuran memakai 31 apel sintetis berdiameter 24, 27, 30, dan 70 mm dalam ruangan serta 102 sampel lapangan; kebenaran dasar diukur dengan jangka sorong digital.

Mekanisme deteksi memakai lima konfigurasi YOLOv8 (n, s, m, l, x) untuk segmentasi instans, yang bersifat bebas anchor dan memakai Darknet-53 serta feature pyramid network yang dimodifikasi. Citra diubah ke ukuran 640 × 640 piksel; naskah menyebut laju pembelajaran 0,001 pada bagian perangkat keras dan 0,01 pada pengaturan optimasi SGD, dengan momentum 0,937, weight decay 0,0005, dropout 0,5, dan 1.000 iterasi dengan penghentian awal bila validasi tidak membaik selama 200 iterasi. Topeng hasil segmentasi dipakai untuk mengekstrak awan titik tiga dimensi dari citra kedalaman. Penulis mencocokkan tiga bentuk geometris: bola dengan least squares, bola dengan RANSAC yang tahan terhadap pencilan, dan elipsoid dengan algoritma Löwner–John yang disempurnakan iterative lalu didekomposisi dengan singular value decomposition untuk memperoleh sumbu panjang dan pendek. Pemilihan bentuk didasarkan pada pengamatan bahwa buah awalnya menyerupai elipsoid lalu menjadi lebih bulat seiring pertumbuhan. Kinerja deteksi diukur dengan presisi, recall, F1, AP, mAP, dan MIoU; kinerja pengukuran diukur dengan RMSE, MAE, MAPE, dan R-squared.

YOLOv8m-seg memberikan presisi 0,90, F1 0,89, AP@0,5 0,94, dan AP@0,75 0,91, sedangkan YOLOv8x-seg memiliki recall tertinggi 0,90; kurva presisi–recall menghasilkan PR-AUC 0,94 dan mAP 0,94 pada IoU 0,5. Pada 102 sampel lapangan, pencocokan elipsoid dengan Azure Kinect menghasilkan RMSE 2,35 mm, MAE 1,66 mm, MAPE 6,15, dan R-squared 0,90, sedangkan dengan RealSense menghasilkan RMSE 9,65 mm, MAE 7,80 mm, MAPE 29,48, dan R-squared 0,77. Pada uji dalam ruangan, RMSE elipsoid sebesar 5,74 mm untuk Azure dan 15,36 mm untuk RealSense, lebih baik daripada pencocokan bola least squares maupun RANSAC. Penulis menyatakan selisih antarsensor terutama berasal dari perbedaan kualitas dan kerapatan awan titik, karena model dilatih dengan proporsi citra yang sama dari kedua sensor. Buah berdiameter lebih dari 30 mm memperoleh skor keyakinan sekitar 0,92, sedangkan buah di bawah 24 mm hanya sekitar 0,75.

Penulis mencatat sejumlah keterbatasan. Oklusi oleh daun, batang, dan buah tetangga menyebabkan deteksi meleset, sementara cahaya rendah dan bayangan menghasilkan false negative. Segmentasi juga mengalami over-masking ketika dua buah dianggap satu serta under-masking ketika hanya sebagian buah yang tertutup topeng, sehingga awan titik tidak cukup untuk pencocokan bentuk. Generalisasi model terhambat oleh keragaman bentuk, ukuran, warna, dan tekstur buah serta daun. Penulis mengusulkan penambahan data dengan lebih banyak contoh oklusi dan variasi pencahayaan, pendekatan fusi beberapa sensor, serta pengambilan citra dari beberapa sudut pandang. Naskah menyatakan MAPE dengan satuan mm, padahal metrik ini didefinisikan sebagai persentase; angka tersebut dilaporkan apa adanya di sini.

