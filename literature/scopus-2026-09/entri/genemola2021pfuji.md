# PFuji-Size dataset: A collection of images and photogrammetry-derived 3D point clouds with ground truth annotations for Fuji apple detection and size estimation in field conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2021pfuji` |
| Judul asli | PFuji-Size dataset: A collection of images and photogrammetry-derived 3D point clouds with ground truth annotations for Fuji apple detection and size estimation in field conditions |
| Penulis | Gen\'e-Mola, Jordi; Sanz-Cortiella, Ricardo; Rosell-Polo, Joan R.; Escol\`a, Alexandre; Gregorio, Eduard |
| Tahun | 2021 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2021pfuji.pdf](../pdf/genemola2021pfuji.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2021.107629

## Gambaran Umum

Kajian ini memperkenalkan PFuji-Size, kumpulan data citra dan awan titik 3D (*point cloud*) pohon apel Fuji yang dipindai di lapangan. Awan titik dibuat dengan *structure-from-motion* dan *multi-view stereo*, lalu setiap buah disegmentasi di ruang 3D dan diberi ukuran diameter hasil pengukuran jangka sorong. Penulis menyatakan bahwa ini adalah kumpulan data publik pertama untuk pengukuran ukuran apel di lapangan. Teks ini tidak memuat hasil metrik deteksi. Metode yang dibandingkan penulis dilaporkan di artikel terkait (Gené-Mola dkk., 2021).

Data diperoleh di kebun apel Fuji di Agramunt, Catalonia, Spanyol. Pohon dilatih dengan sistem *tall spindle* dengan tinggi tajuk sekitar 3,5 m dan lebar sekitar 1,5 m. Kamera yang dipakai adalah Canon EOS 60 DSLR (sensor 18 MP, lensa 24 mm). Foto diambil dari jarak 2,5 m dari pusat pohon, dengan tumpang-tindih antarfoto lebih dari 75% secara horizontal dan 85% secara vertikal. Citra berukuran 5184 × 3456 piksel. Ada tiga subset: Orch2018 berisi 303 apel merah pada Oktober 2018, Orch2020 berisi 312 apel hijau pada Juli 2020 (sekitar 70% ukuran akhir), dan Lab2020 berisi 25 apel yang dipindai di laboratorium dengan 180 foto per apel. Total 615 apel di lapangan dipetakan dari enam pohon, tiga pohon per subset. Diameter apel berkisar 26,9 mm sampai 94,8 mm. Tingkat tertutup daun berkisar 1,4% sampai 99%. Rata-rata diameter Orch2018 adalah 77,4 mm (simpangan baku 9,4 mm), sedangkan Orch2020 adalah 54,1 mm (simpangan baku 5,1 mm).

Metode penyegmentasian buah bersifat semi-otomatis. Mask R-CNN yang dilatih dengan data Fuji-SfM mendeteksi apel di citra, lalu piksel hasil segmentasi diproyeksikan ke awan titik memakai parameter kamera dari Agisoft Metashape v1.6.4. Hasil proyeksi kemudian dikoreksi secara manual di CloudCompare. Koreksi mencakup penggabungan deteksi ganda, pemisahan deteksi yang memuat lebih dari satu apel, segmentasi apel yang tidak terdeteksi, dan penghapusan positif palsu. Dari sisi data, awan titik untuk setiap subset dibuat dari sisi timur dan sisi barat baris pohon, lalu digabung sebelum segmentasi. Hasilnya 315 awan titik apel di lapangan dan 25 apel di laboratorium, ditambah 640 awan titik apel secara keseluruhan. Setiap berkas awan titik apel memuat koordinat x, y, z dan warna R, G, B.

Penulis menyatakan dua batasan. Pertama, proyeksi mask citra ke 3D dapat keliru, sehingga segmentasi harus diperbaiki manual dan waktu koreksinya tidak dilaporkan dalam teks. Kedua, apel tidak berbentuk bola sempurna, sehingga diameter acuan diukur sebagai diameter horizontal terbesar, bukan diameter bola yang dihitung dari geometri. Subset laboratorium hanya berisi 25 apel, sehingga jumlahnya kecil untuk menguji metode pada diameter yang lebih luas.
