# Determining Fruit Set Density and Spatial Arrangement of Fruit Trees for Fruit Picking Operations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sato2022determining` |
| Judul asli | Determining Fruit Set Density and Spatial Arrangement of Fruit Trees for Fruit Picking Operations |
| Penulis | Sato, Hibiki; Ishii, Masaki; Ito, Hidekatsu; Dohsaka, Kohji |
| Tahun | 2022 |
| Venue | 2022 Joint 12th International Conference on Soft Computing and Intelligent Systems and 23rd International Symposium on Advanced Intelligent Systems Scis and Isis 2022 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [sato2022determining.pdf](../pdf/sato2022determining.pdf)
- DOI resmi: https://doi.org/10.1109/scisisis55246.2022.10002107

## Gambaran Umum

Penulis menyebut berkurangnya jumlah petani dan menuanya tenaga kerja pertanian di Jepang. Penjarangan bunga dan buah apel dikerjakan berdasarkan pengalaman dan intuisi pekerja, sehingga sulit diukur dan sulit diwariskan. Tujuan penelitian adalah membuat sistem yang mengenali kepadatan buah dan susunan ruang buah pada pohon apel, sebagai dasar visualisasi teknik penjarangan.

Data berasal dari Stasiun Percobaan Pohon Buah Akita (Kota Yokote). Kamera aksi (GoPro) dipasang di kepala pekerja yang menjarangkan apel. Dari video diambil 1.492 citra diam (102 citra tanggal 3 Mei 2020, 815 citra 3 Juni 2020, 575 citra 4 Juni 2020). Anotasi kotak dibuat dengan *labelImg* untuk tiga kelas: *Bud* (kuncup) 600, *Flower* (bunga) 4.412, dan *YoungApple* (apel muda) 10.630. Pembagian latih dan evaluasi 8:2 (1.194 dan 298 citra). Pemberi label tidak disebut.

Metodenya memakai YOLOX, detektor satu tahap yang memprediksi kotak dan kelas dalam satu lintasan, dilatih 300 *epoch* dari bobot awal YOLOX-S atau Darknet. Kamera RGB-D Intel RealSense dipasang pada tongkat kaki satu. Kedalaman di titik pusat kotak terdeteksi dibaca, lalu jarak Euclid 3D antarbuah dihitung. Lubang pada peta kedalaman akibat bayangan diisi dengan tapis *domain transform*.

Hasilnya, AP pada IoU 50% adalah 64,4% (bobot awal YOLOX-S) dan 65,3% (bobot awal Darknet) pada data evaluasi. Penulis menampilkan buah yang akan dipanen sebagai lapisan pada citra dengan ukuran dari kedalaman. Jarak antarbuah dihitung, tetapi akurasi jarak dan kedalaman tidak dievaluasi.

Keterbatasan dari teks: citra latih dan evaluasi berasal dari video yang sama dengan pembagian acak 8:2, tanpa keterangan pembagian per pohon atau per tanggal. Tidak ada pencacahan buah dan tidak ada acuan hitung. Tidak ada angka kepadatan buah. Akurasi kedalaman belum dievaluasi, menurut penulis sebagai rencana kerja berikutnya. Jumlah pohon tidak disebut.
