# Mots: Multi-object tracking and segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `voigtlaender2019mots` |
| Judul asli | Mots: Multi-object tracking and segmentation |
| Penulis | Voigtlaender, Paul; Krause, Michael; Osep, Aljosa; Luiten, Jonathon; Sekar, Berin Balachandar Gnana; Geiger, Andreas; Leibe, Bastian |
| Tahun | 2019 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [voigtlaender2019mots.pdf](../pdf/voigtlaender2019mots.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2019.00813

## Gambaran Umum

Makalah ini memperluas pelacakan multi-objek menjadi pelacakan dan segmentasi multi-objek (*multi-object tracking and segmentation*, MOTS). Penulis menilai kinerja pelacakan pada tingkat kotak pembatas mulai jenuh, sehingga peningkatan berikutnya memerlukan informasi tingkat piksel. Kotak pembatas dianggap terlalu kasar ketika dua objek saling berpapasan atau sebagian tertutup, karena kotak itu dapat memuat lebih banyak piksel objek lain daripada objeknya sendiri. Topeng segmentasi memiliki kebenaran dasar yang terdefinisi dengan jelas dan secara konstruksi tidak saling tumpang tindih, sehingga pencocokan dengan kebenaran dasar tidak memerlukan prosedur heuristik seperti pada kotak yang bertumpang tindih. Penulis menyatakan belum ada dataset untuk tugas ini, dan keberhasilan MOTS memerlukan penggabungan petunjuk temporal dan petunjuk topeng.

Dataset dibuat dengan prosedur anotasi semi-otomatis pada dua kumpulan data pelacakan yang sudah ada, menghasilkan 65.213 topeng piksel untuk 977 objek berbeda (mobil dan pejalan kaki) dalam 10.870 bingkai video. Prosedurnya memakai jaringan penyempurna berbasis DeepLabv3+ yang dilatih awal pada COCO dan Mapillary untuk mengubah kotak pembatas menjadi topeng, lalu koreksi poligon manual. Untuk setiap trek, dua topeng dianotasi manual dan dipakai untuk menyempurnakan jaringan tersebut, setelah itu proses pembangkitan dan koreksi diulang sampai akurasi tingkat piksel tercapai. KITTI MOTS memakai 21 sekuens latih KITTI yang dibagi menjadi 12 sekuens latih dan 9 sekuens validasi, dengan 5.027 dan 2.981 bingkai, 99 dan 68 trek pejalan kaki, serta 431 dan 151 trek mobil. MOTSChallenge mencakup 4 dari 7 sekuens latih MOTChallenge 2017 dengan 2.862 bingkai dan 228 trek pejalan kaki.

Metode dasar yang diusulkan, TrackR-CNN, dibangun di atas Mask R-CNN dengan backbone ResNet-101. Dua lapisan konvolusi 3D *depthwise separable* berkernel 3×3×3 dan 1024 peta fitur disisipkan antara backbone dan *region proposal network* untuk memasukkan konteks waktu; alternatif yang diuji adalah lapisan convolutional LSTM. *Association head* berupa lapisan terhubung penuh menghasilkan vektor asosiasi berdimensi 128 untuk setiap proposal, dilatih dengan *batch hard triplet loss* dengan margin 0,2 agar vektor dari instans yang sama berdekatan dan vektor dari instans berbeda menjauh. Pelacakan memakai algoritma Hungarian yang mencocokkan deteksi dengan jarak Euclidean antarvektor asosiasi, membatasi pencocokan pada deteksi terakhir dari trek dalam jendela waktu tertentu, serta memprioritaskan piksel dari deteksi berkeyakinan lebih tinggi saat topeng bertumpang tindih. Penulis juga menguji asosiasi berdasarkan *mask propagation* dengan aliran optik PWC-Net, IoU kotak, dan jarak pusat kotak. Pelatihan memakai Adam, laju 5×10⁻⁷, 40 epoch, dan mini-batch delapan bingkai berturut-turut; kecepatan pengujian sekitar dua bingkai per detik.

Penulis mengusulkan metrik MOTSA, MOTSP, dan sMOTSA sebagai turunan CLEAR MOT yang memakai IoU topeng; korespondensi ditetapkan bila IoU melebihi 0,5, dan sMOTSA menjumlahkan IoU sehingga mengukur kualitas segmentasi, deteksi, dan pelacakan sekaligus. Pada validasi KITTI MOTS (Tabel 2), TrackR-CNN memperoleh sMOTSA 76,2 untuk mobil dan 46,8 untuk pejalan kaki, MOTSA 87,8 dan 65,1, serta MOTSP 87,2 dan 75,7. Baseline Mask R-CNN dengan *mask propagation* mencatat 75,1/45,0 dan 86,6/63,5, sedangkan model yang dilatih hanya pada kotak pembatas lalu diberi topeng pasca pemrosesan mencatat 75,0/41,2 dan 87,0/57,9. Dengan kotak kebenaran dasar yang ketat sekalipun, hasilnya 82,5/50,0 untuk sMOTSA dan 95,3/71,1 untuk MOTSA. Ablasi (Tabel 3 dan 4) menunjukkan dua lapisan 3D convolution dan *association head* memberi perbaikan, sementara convolutional LSTM tidak memberi perolehan bermakna dan asosiasi berdasarkan pusat kotak paling lemah. Pada MOTSChallenge (Tabel 5, skema *leaving-one-out*), TrackR-CNN mencatat sMOTSA 52,7, MOTSA 66,9, dan MOTSP 80,2.

Batasan yang dinyatakan penulis mencakup kecepatan pengujian yang masih sekitar dua bingkai per detik dan sifat *near-online* akibat pandangan ke depan dua bingkai pada konvolusi 3D. MOTSChallenge hanya memiliki empat sekuens sehingga evaluasi memakai skema *leaving-one-out*, dan metode pembanding memakai deteksi publik SDP, sedangkan TrackR-CNN menghasilkan deteksinya sendiri, sehingga perbandingannya tidak sepenuhnya setara. Penulis juga mencatat bahwa pembangkitan topeng tetap sulit meski hipotesis lintasan sudah sempurna, terutama untuk pejalan kaki dan kotak amodal yang memuat wilayah tanpa objek; CAMOT dibatasi oleh ketersediaan kedalaman stereo; serta sedikitnya pelacak berbasis topeng dengan kode sumber yang tersedia. Prosedur anotasi masih memerlukan koreksi manual dalam jumlah besar, dan penerapan pada himpunan uji KITTI masih dalam proses saat makalah ditulis.

