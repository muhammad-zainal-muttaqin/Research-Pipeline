# Three-dimensional photogrammetry with deep learning instance segmentation to extract berry fruit harvestability traits

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ni2021three` |
| Judul asli | Three-dimensional photogrammetry with deep learning instance segmentation to extract berry fruit harvestability traits |
| Penulis | Ni, Xueping; Li, Changying; Jiang, Huanyu; Takeda, Fumiomi |
| Tahun | 2021 |
| Venue | ISPRS Journal of Photogrammetry and Remote Sensing |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [ni2021three.pdf](../pdf/ni2021three.pdf)
- DOI resmi: https://doi.org/10.1016/j.isprsjprs.2020.11.010

## Gambaran Umum

Kajian ini menghitung jumlah buah blueberry dalam satu kluster dan menaksir kematangan serta volume tiap buah dari model tiga dimensi (3D). Model 3D dibangun dari 120 citra per kluster yang diambil dengan tiga kamera Fujifilm X-A10 pada motor putar dengan langkah 9 derajat (40 langkah). Citra itu diolah dengan fotogrametri *structure from motion* (SfM), yaitu metode yang merekonstruksi titik-titik 3D dari sejumlah foto yang diambil dari sudut berbeda. Hasilnya berupa awan titik (*point cloud*), yakni kumpulan titik 3D yang mewakili permukaan objek.

Masalah yang diangkat adalah bahwa penghitungan buah dari satu citra 2D tidak menangkap buah yang tertutup daun atau buah lain dalam kluster. Dengan rekonstruksi 3D, setiap buah dapat dipisahkan pada ruang tiga dimensi, bukan hanya pada bidang gambar. Kajian ini menguji apakah pemisahan tersebut cukup akurat untuk menghitung buah, menaksir kematangan, dan mengukur volume.

Segmentasi instans 2D dilakukan dengan Mask R-CNN, yaitu jaringan yang menghasilkan masker piksel untuk setiap objek dalam citra. Data latih terdiri dari 724 citra, dibagi menjadi 524 untuk latih, 145 untuk validasi, dan 55 untuk uji, dengan label kematangan. Masker 2D kemudian diproyeksikan ke awan titik 3D sehingga setiap berry memperoleh kumpulan titik sendiri. Dari kumpulan titik itu dihitung sifat fenotipe, termasuk volume.

Hasil utama yang dilaporkan adalah akurasi penghitungan buah per kluster sebesar 97,3% untuk seluruh kultivar. Regresi linier kematangan kluster mencapai R2 0,908 dengan RMSE 0,068. Galat volume berry dalam kluster adalah RMSE 2,92 cm3 terhadap ukuran acuan. Galat rata-rata volume per buah kurang dari 0,295 cm3 bila jumlah buah per kluster lebih dari 10.

Alur kerja terdiri dari akuisisi citra, rekonstruksi 3D, segmentasi 2D, proyeksi masker, dan ekstraksi sifat. Akuisisi memakai kamera yang berputar mengelilingi kluster sehingga setiap buah terlihat dari beberapa sudut. Rekonstruksi SfM menghasilkan awan titik yang menjadi dasar seluruh hitungan. Segmentasi 2D memberi label pada setiap buah di tiap citra, lalu label itu dipindahkan ke titik-titik 3D yang sesuai.

Kajian ini menunjukkan bahwa pipeline 3D dapat memisahkan buah dalam satu kluster sampai tingkat individual. Hitungan dilakukan per kluster dari satu rekonstruksi. Kajian tidak melaporkan pemeriksaan apakah buah yang sama dihitung ulang dari sudut berbeda, sehingga deduplikasi lintas pandang tidak dinilai secara terpisah.

Keterbatasan kajian jelas. Pengujian dilakukan di dalam ruangan dengan pencahayaan terkendali, dan hanya satu kluster diproses dalam satu waktu. Kondisi lapangan yang berubah pencahayaan, angin, dan oklusi daun belum diuji. Objek kajian adalah blueberry, bukan kelapa sawit, sehingga angka akurasinya tidak dapat langsung dipindahkan ke tandan sawit tanpa uji ulang.

Bukti itu berasal dari satu jenis tanaman pada kondisi terkendali, dan belum menunjukkan kinerja pada pohon utuh dengan banyak kluster. Pertanyaan itu menjadi bagian dari agenda untuk kajian berikutnya.
