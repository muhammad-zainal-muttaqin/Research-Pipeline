# Canopy-attention-YOLOv4-based immature/mature apple fruit detection on dense-foliage tree architectures for early crop load estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lu2022canopy` |
| Judul asli | Canopy-attention-YOLOv4-based immature/mature apple fruit detection on dense-foliage tree architectures for early crop load estimation |
| Penulis | Lu, Shenglian; Chen, Wenkang; Zhang, Xin; Karkee, Manoj |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [lu2022canopy.pdf](../pdf/lu2022canopy.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.106696

## Gambaran Umum

Studi ini menghitung buah apel dari citra yang diambil dengan smartphone di kebun, lalu mengukur tinggi dan lebar buah dari citra yang sama. Penghitungan dilakukan per citra, tanpa menggabungkan pengamatan dari beberapa sudut pandang pohon. Pendekatannya memakai CA-YOLOv4, yaitu YOLOv4 yang ditambah modul perhatian CBAM, lapisan adaptif, peta fitur berskala lebih besar, jaringan terhubung padat, dan fungsi kerugian untuk regresi kotak batas. Citra diambil pada arsitektur SNAP, yaitu tajuk padat (dense-foliage V-trellis) dan tajuk vertikal (vertical-trellis), pada tahap pertumbuhan awal, tengah, dan akhir.

Hasil ablasi menunjukkan CA-YOLOv4 mengungguli YOLOv4 asli. Presisinya 3,68% lebih tinggi, recall 5,34% lebih tinggi, dan F1 4,55% lebih tinggi, sementara loss akhir 0,54 lebih rendah. Pada dua set data, "Scifresh" dan "Envy", CA-YOLOv4 juga mengungguli Faster R-CNN dan SSD. Terhadap SSD, teks mencatat selisih 5,49% sampai 11,29% pada tahap awal, tengah, dan akhir. Angka ini tidak dapat dibandingkan langsung dengan studi lain karena data dan protokolnya berbeda.

Studi ini membandingkan dua cara akuisisi pada 90 citra. Mode oblique menghasilkan 108 label, dengan 91 benar (84,25%), 11 positif palsu, dan 17 terlewat (15,75%). Mode panorama menghasilkan 104 label, dengan 85 benar (81,73%), 14 positif palsu, dan 19 terlewat (18,27%). Teks menyebut hasil oblique lebih baik, dan menduga penyebabnya adalah distorsi citra pada mode panorama. Selisih true positive hanya 2,52%, sehingga keunggulannya kecil dan berasal dari 90 citra saja.

Untuk ukuran buah, regresi dibuat dari piksel ke milimeter. Pada mode oblique, R² tinggi 0,64 dengan RMSE 11,01 mm dan R² lebar 0,65 dengan RMSE 10,79 mm. Pada mode panorama, R² tinggi 0,68 dengan RMSE 10,41 mm dan R² lebar 0,66 dengan RMSE 10,34 mm. Kemiringan regresi berada di 0,93 sampai 1,00. Dengan demikian, ukuran dari panorama sedikit lebih kecil galatnya, sedangkan deteksi oblique sedikit lebih baik. Keduanya tidak menunjukkan keunggulan tunggal.

Batas studi ini perlu dicatat. Penghitungan berbasis satu citra per sisi pohon tidak menyelesaikan identitas lintas pandang, sehingga buah yang sama dapat terhitung dari sudut berbeda. Data hanya dari satu kebun dan satu perangkat, dengan 90 citra untuk uji akuisisi.
