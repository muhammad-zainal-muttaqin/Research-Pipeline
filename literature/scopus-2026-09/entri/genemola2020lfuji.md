# LFuji-air dataset: Annotated 3D LiDAR point clouds of Fuji apple trees for fruit detection scanned under different forced air flow conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2020lfuji` |
| Judul asli | LFuji-air dataset: Annotated 3D LiDAR point clouds of Fuji apple trees for fruit detection scanned under different forced air flow conditions |
| Penulis | Gen\'e-Mola, Jordi; Gregorio, Eduard; Auat Cheein, Fernando; Guevara, Javier; Llorens, Jordi; Sanz-Cortiella, Ricardo; Escol\`a, Alexandre; Rosell-Polo, Joan R. |
| Tahun | 2020 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2020lfuji.pdf](../pdf/genemola2020lfuji.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2020.105248

## Gambaran Umum

Artikel ini menyajikan himpunan data LFuji-air, yaitu awan titik LiDAR tiga dimensi dari pohon apel Fuji yang sudah diberi anotasi lokasi buah. Tujuannya adalah menyediakan data untuk melatih dan menguji algoritme deteksi buah berbasis LiDAR, sekaligus memungkinkan kajian terhadap pendekatan multi-pandang dan pemanfaatan aliran udara paksa untuk mengurangi oklusi buah. Artikel ini adalah artikel data yang terkait dengan artikel riset berjudul “Fruit detection, yield prediction and canopy geometric characterization using LiDAR with forced air flow”.

Data diperoleh dari 11 pohon apel Fuji (*Malus domestica* Borkh. cv. Fuji) yang memuat 1.444 buah di kebun komersial Agramunt, Catalonia, Spanyol. Pohon dipindai tiga minggu sebelum panen pada tahap pertumbuhan BBCH 85. Sistem pemindai darat bergerak (MTLS) terdiri atas LiDAR Velodyne Puck VLP-16 dengan akurasi ±0,03 m pada laju 10 Hz dan penerima RTK-GNSS Leica GPS1200+ pada laju 20 Hz dengan galat absolut 0,01 m horizontal dan 0,02 m vertikal. Sistem dipasang pada alat semprot berbantuan udara yang ditarik traktor dengan kecepatan 0,125 m/s; kecepatan aliran udara adalah 5,5 ± 2,3 m/s pada jarak 2,4 m dari kipas.

Setiap pohon dipindai delapan kali, yaitu kombinasi dua ketinggian sensor (1,8 m dan 2,5 m), dua kondisi aliran udara (kipas menyala dan mati), serta dua sisi barisan pohon (timur dan barat). Awan titik disimpan dalam berkas MAT berupa matriks m×4 yang memuat koordinat global X, Y, Z dan nilai reflektansi setiap titik; data mentah LiDAR tersedia dalam format PCAP dan data GNSS dalam format TXT. Transformasi koordinat dilakukan dari LiDAR ke GNSS lalu ke koordinat global. Sistem tidak memakai unit pengukur inersia, sehingga sudut orientasi diambil dari arah depan yang dihitung dari hasil RTK-GNSS dan dianggap tetap sepanjang lintasan lurus pendek. Kode MATLAB R2018a untuk menghasilkan awan titik georujuk dan untuk deteksi buah dipublikasikan di GitHub.

Acuan hitung lokasi buah dibuat manual dengan menempatkan kotak pembatas rektangular tiga dimensi di perangkat lunak CloudCompare, dibantu citra RGB tambahan. Dari 1.444 apel yang dihitung di lapangan, 1.353 dapat dianotasi; sisanya sebesar 6,3% tidak teridentifikasi pada awan titik karena tidak terlihat. Anotasi disimpan dalam format TXT: baris pertama memuat pusat buah dan delapan baris berikutnya memuat sudut kotak pembatas. Himpunan data disediakan untuk pelatihan dan pengujian algoritme, tetapi artikel ini tidak melaporkan metrik kinerja deteksi, acuan metrik, atau pembagian cawat uji; hasil tersebut ada di artikel riset terkait.

Penulis menyatakan keterbatasan pada bagian data yang tidak tampak, yaitu 6,3% buah tidak dapat diberi anotasi. Pengukuran aliran udara dilakukan pada 35 titik yang mencakup tujuh interval tinggi dan lima interval lebar, masing-masing dirata-ratakan dari sepuluh pengukuran. Artikel ini tidak menyajikan klaim peningkatan akurasi deteksi; nilainya terletak pada variasi kondisi pemindaian dan anotasi buah yang disediakan.

