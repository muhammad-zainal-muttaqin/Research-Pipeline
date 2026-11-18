# A Crawling Review of Fruit Tree Image Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `oh2025crawling` |
| Judul asli | A Crawling Review of Fruit Tree Image Segmentation |
| Penulis | Oh, Il-Seok; Lee, Jin-Seon |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [oh2025crawling.pdf](../pdf/oh2025crawling.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15212239

## Gambaran Umum

Tinjauan ini mengkaji segmentasi citra pohon buah untuk mengotomatiskan tugas kebun, seperti fenotiping, pemanenan, penyemprotan, pemangkasan, estimasi hasil, dan navigasi robot. Pekerjaan manual menimbulkan kelelahan, hasil yang tidak tepat, dan biaya tenaga kerja tinggi. Segmentasi pohon sulit karena citra sangat beragam akibat jenis buah, geografi, cuaca, dan teknik budidaya; oklusi oleh penopang, tiang, daun, dan dahan; serta batas antarpohon yang kabur karena tanaman ditanam berbaris dengan cabang yang saling menjalin. Penulis membatasi kajian pada citra pandang depan (*front-view*) di kebun, bukan citra pandang atas dari UAV yang menjadi fokus tinjauan kehutanan sebelumnya.

Penulis mengumpulkan 207 makalah melalui metode baru bernama *crawling review*: sebuah antrean dimulai dari satu makalah benih, lalu makalah yang dirujuknya ditambahkan secara berulang sampai antrean kosong, dilengkapi tahap tambahan dari empat jurnal antara Januari 2020 dan Agustus 2025. Kajian berrentang 1990–2025 dan memakai taksonomi berlapis, yaitu pendekatan (berbasis aturan/*rule-based*, RB, versus pembelajaran mendalam/*deep learning*, DL), jenis citra (RGB, RGB-D, awan titik, lainnya), tugas pertanian, dan jenis buah. Dari 207 makalah, 83 memakai RB dan 124 memakai DL. Metode RB mencakup ambang batas, pengelompokan, pertumbuhan wilayah, pencocokan bentuk, dan graf; metode DL memakai CNN seperti Mask R-CNN dan YOLACT serta model *transformer* seperti DETR dan Swin.

Mekanisme segmentasi berbeda pada tiap pendekatan. Metode RB memakai fitur buatan, misalnya ambang batas kanal warna pada YCbCr atau HSI, pengelompokan *k-means*, SVM, model Bayesian, dan rekonstruksi tiga dimensi dari awan titik LiDAR atau stereo. Metode DL mempelajari fitur secara otomatis, baik segmentasi semantik maupun instansi; Mask R-CNN, U-Net, DeepLabv3+, SegNet, YOLO, dan *transformer* dipakai untuk memisahkan buah, dahan, batang, dan daun. Untuk menghitung buah, beberapa kajian menambahkan pelacakan guna menghindari penghitungan ganda: GMM dan U-Net dipasangkan dengan pelacakan lintas frame, satu kajian melacak batang karena ukurannya lebih besar dan lebih mudah diikuti daripada buah, dan kajian lain memakai pencocokan timbal balik atau *long short-term memory* (LSTM) untuk memasangkan tangkai buah pada waktu berbeda.

Angka yang dilaporkan dari kajian yang ditinjau mencakup penurunan penggunaan pestisida sebesar 23% lewat segmentasi kanopi apel berbasis ambang batas HSI, serta penyemprotan yang menyisakan 56,8%, 39,37%, dan 8,08% pestisida pada mode buka-semua, on/off, dan laju variabel. Sistem DL memakai RGB karena murah dan tersedia dari ponsel; sensor RGB-D yang lazim seperti Intel RealSense D435 berharga sekitar 200 USD, sedangkan LiDAR dan pencitraan multispektral lebih mahal dengan perbaikan akurasi yang terbatas. Lampiran mencatat 11 dataset publik, tetapi sebagian besar spesifik untuk satu tugas; satu kajian membangkitkan 4.800 citra per spesies untuk enam spesies, dan kajian lain menyintesiskan 1.000 citra delima serta 200 citra nyata.

Batasan utama yang dinyatakan penulis adalah minimnya dataset serbaguna dan model segmentasi yang dapat dipakai untuk berbagai tugas dan lingkungan, sehingga perbandingan kinerja antarmetode belum objektif. Sebagian besar percobaan memakai dataset berskala kecil dan terbatas pada satu kebun; kinerja menurun ketika diterapkan pada kebun lain dengan pencahayaan, arsitektur pohon, dan latar yang berbeda. Penulis juga mengakui *crawling review* lebih laborius, memakan waktu lama, dan kurang dapat diulang karena pemilihan makalah dilakukan manual. Enam arah penelitian masa depan diusulkan: dataset berskala besar dan serbaguna, model fondasi pertanian, penggabungan CNN dan *transformer*, estimasi kedalaman monokular, rekonstruksi 3D barisan pohon berbasis DL, serta pembelajaran *few-shot* dan *self-supervised*. Penulis menyatakan tidak ada konflik kepentingan; pendanaan berasal dari dana penelitian Universitas Nasional Jeonbuk tahun 2025.

