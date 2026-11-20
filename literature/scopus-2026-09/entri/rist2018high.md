# High-precision phenotyping of grape bunch architecture using fast 3d sensor and automation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rist2018high` |
| Judul asli | High-precision phenotyping of grape bunch architecture using fast 3d sensor and automation |
| Penulis | Rist, Florian; Herzog, Katja; Mack, Jenny; Richter, Robert; Steinhage, Volker; T\"opfer, Reinhard |
| Tahun | 2018 |
| Venue | Sensors Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [rist2018high.pdf](../pdf/rist2018high.pdf)
- DOI resmi: https://doi.org/10.3390/s18030763

## Gambaran Umum

Pemuliaan anggur memilih tanaman dengan tandan yang lebih longgar, karena tandan yang rapat meningkatkan risiko busuk tandan akibat *Botrytis cinerea*. Arsitektur tandan terdiri atas banyak sifat tunggal, seperti jumlah buah, diameter buah, volume buah, panjang tandan, dan lebar tandan. Penilaian sifat tersebut masih dilakukan secara manual oleh tenaga terlatih. Cara ini memakan waktu, bersifat subjektif, dan membatasi jumlah tanaman yang dapat dinilai. Skala OIV 204 hanya membagi kepadatan tandan ke dalam lima kelas, sehingga sifat tunggal tidak tercatat. Penelitian ini bertujuan mengembangkan alur fenotipe yang cepat dan presisi tinggi berbasis sifat tiga dimensi tandan.

Penelitian memakai anggur *Vitis vinifera* yang dipanen di kebun percobaan Geilweilerhof, Siebeldingen, Jerman, pada musim 2016 saat tahap BBCH 87 sampai 89. Sensor yang digunakan adalah pemindai 3D Artec Spider berbasis *structured light* LED biru, dengan resolusi *mesh* hingga 0,1 mm dan akurasi titik hingga 0,05 mm. Tandan dipasang pada kait bermotor yang berputar, dan pemindaian 360 derajat dilakukan hingga 7,5 bingkai per detik. Uji awal memakai 10 tandan meja yang masing-masing dipindai 10 kali dengan dua kecepatan putar. Untuk uji keterterapan, penulis memakai 39 tandan padat dan 35 tandan longgar, sehingga totalnya 74 tandan. Populasi F1 dari persilangan GF.GA-47-42 × "Villard Blanc" terdiri atas 222 tandan dari 41 genotipe. Uji lapangan memakai 48 sampel, masing-masing 12 untuk setiap varietas, yang dipindai langsung di kebun dan di laboratorium.

Perangkat lunak 3D-Bunch-Tool merupakan modifikasi algoritma Mack dan kawan-kawan. Alur kerjanya terdiri atas tiga tahap. Tahap pertama mengurangi resolusi *point cloud*. Tahap kedua melakukan segmentasi dengan *region growing*. Tahap ketiga memasang model bola dengan pendekatan *Random-Sample-Consensus* (*RANSAC*) untuk mendeteksi buah, lalu membuang model yang tumpang tindih lebih dari 25 persen. Pada uji kecepatan putar, jumlah buah rata-rata 72 pada pemindaian cepat dan 70 pada pemindaian lambat. Kedua varian tidak berbeda signifikan. Diameter buah rata-rata 17,2 mm dan 17,1 mm, sedangkan volume buah rata-rata 2,7 mL pada kedua varian. Validasi terhadap data acuan menghasilkan koefisien determinasi r² hingga 0,95 untuk jumlah buah. Volume total buah memiliki r² 0,83, dan *convex hull* memiliki r² 0,79 terhadap volume total buah. Panjang tandan memiliki koefisien korelasi 0,84 terhadap pengukuran 2D. Lebar tandan memiliki nilai r² terendah, yaitu 0,54. Pengukuran manual memerlukan sekitar 10 menit per tandan, sedangkan pemindaian dengan Artec Spider membutuhkan sekitar satu menit.

Penulis mengakui beberapa keterbatasan. Data yang tidak teratur dan tertutup dapat menyebabkan *undersegmentation* atau *oversegmentation*, sehingga jumlah buah dapat terlalu rendah. Penulis juga mencatat bahwa 3D-BT meremehkan jumlah buah, dengan selisih rata-rata sekitar 15 butir. Lebar tandan memiliki korelasi paling rendah karena 3D-BT mengukur jarak dalam tiga dimensi, sedangkan acuan 2D hanya mengukur dua dimensi. *Convex hull* selalu lebih besar daripada volume total buah karena mencakup ruang di antara buah dan struktur tangkai. Uji lapangan hanya merupakan bukti prinsip pada 48 sampel dari empat varietas, sehingga belum menjadi validasi pada skala besar.
