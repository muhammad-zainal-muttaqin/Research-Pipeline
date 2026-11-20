# Tomato Fruit Detection and Counting in Greenhouses Using Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `afonso2020tomato` |
| Judul asli | Tomato Fruit Detection and Counting in Greenhouses Using Deep Learning |
| Penulis | Afonso, Manya; Fonteijn, Hubert; Fiorentin, Felipe Schadeck; Lensink, Dick; Mooij, Marcel; Faber, Nanne; Polder, Gerrit; Wehrens, Ron |
| Tahun | 2020 |
| Venue | Frontiers in Plant Science |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [afonso2020tomato.pdf](../pdf/afonso2020tomato.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2020.571299

## Gambaran Umum

Penelitian ini mengatasi deteksi dan pencacahan buah tomat pada citar
rumah kaca. Pengukuran fenotipe secara manual bersifat padat karya, dan
otomatisasi deteksi buah menjadi prasyarat untuk panen otomatis. Rumah kaca
merupakan lingkungan yang sulit karena keterbatasan penempatan kamera
menghasilkan sudut pandang terbatas, sedangkan warna dan kecerahan buah
berubah antar tanaman, antar waktu, dan antar posisi kamera. Penulis
membandingkan pendekatan pembelajaran mendalam dengan metode penglihatan
komputer klasik berbasis ciri buatan.

Data berupa buah tomat di rumah kaca produksi Enza Zaden di Enkhuizen,
Belanda. Empat kamera Intel RealSense D435 dipasang pada troli yang
berjalan di atas pipa pemanas, pada ketinggian 930, 1.630, 2.300, dan
3.000 mm dari lantai dan sekitar 0,5 m dari tanaman. Citra RGB dan kedalaman
sejajar piksel berukuran 720 × 1280 diambil pada malam hari di tiga tanggal
akhir Mei sampai paruh pertama Juni 2019. Sejumlah 123 citra dianotasi
manual dengan labelme berupa poligon, termasuk beberapa segmen terpisah
untuk buah yang tertutup; hanya buah tanaman pada baris yang dipotret
(latar depan) yang diberi label. Citra dibagi acak menjadi 82 citra latih
dan 41 citra uji. Kelas matang/merah dan mentah/hijau dibentuk dalam
praproses Matlab dari peta kromatisitas: buah berlabel matang apabila nilai
kanal merah melebihi 1,4 kali kanal hijau pada sebagian besar pikselnya,
dengan faktor batas yang ditentukan secara empiris.

Mekanisme deteksi memakai MaskRCNN melalui implementasi Detectron
(Caffe2/PyTorch), dengan tulang punggung ResNet50, ResNet101, dan
ResNext101 yang telah dilatih awal pada ImageNet-1K. Pelatihan memakai SGD,
regularisasi L2 dengan weight decay 0,001, ukuran kelompok satu citra,
tanpa augmentasi data, serta 200.000 iterasi. Praproses kedalaman (+PP)
membuang buah latar belakang dengan menghitung nilai median kedalaman pada
piksel topeng setiap objek dan membandingkannya dengan ambang per kamera,
yaitu 110, 120, 120, dan 50 pada rentang 8 bit 0–255. Metrik dihitung dari
presisi = TP/(TP+FP), recall = TP/(TP+FN), dan F1 = 2·presisi·recall/
(presisi+recall), dengan suatu deteksi dihitung benar apabila IoU terhadap
instance sebenarnya mencapai ambang 0,25, 0,50, atau 0,75. Pada ambang
IoU 0,50, metode klasik menghasilkan presisi 0,45, recall 0,60, dan F1 0,58,
sedangkan ResNet50 mencatat 0,93, 0,91, dan 0,92 serta ResNext101 mencatat
0,96, 0,91, dan 0,93; ResNet101 dengan praproses kedalaman mencatat 0,94,
0,94, dan 0,94. Nilai tersebut melebihi presisi 0,88 dan recall 0,80 dari
Yamamoto dkk. (2014), AP rata-rata 0,82 dari Zhou dkk. (2017), dan akurasi
prediksi 0,91 dari Rahnemoonfar dan Sheppard (2017).

Penulis menyatakan beberapa batasan. Praproses kedalaman menaikkan presisi
tetapi menurunkan recall karena galat pada citra kedalaman RealSense
menggugurkan sebagian buah latar depan. Kamera paling atas memberi metrik
lebih rendah karena daun lebih banyak sehingga menyulitkan deteksi buah
hijau dan mengganggu ambang kedalaman. Ketidakjelasan batas warna matang
atau mentah ditambah jumlah buah mentah hampir dua kali buah matang
menyebabkan lebih banyak positif palsu pada kelas matang, sehingga penulis
menyarankan deteksi satu kelas lalu pemberian skor kematangan. Registrasi
citra antar ketinggian kamera tidak dibahas, dan penyusunan hasil deteksi
per citra menjadi inventaris tingkat petak masih menjadi pekerjaan berikutnya.
