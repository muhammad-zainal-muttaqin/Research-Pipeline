# In-field grape cluster size assessment for vine yield estimation using a mobile robot and a consumer level RGB-D Camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kurtser2020field` |
| Judul asli | In-field grape cluster size assessment for vine yield estimation using a mobile robot and a consumer level RGB-D Camera |
| Penulis | Kurtser, Polina; Ringdahl, Ola; Rotstein, Nati; Berenstein, Ron; Edan, Yael |
| Tahun | 2020 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [kurtser2020field.pdf](../pdf/kurtser2020field.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2020.2970654

## Gambaran Umum

Kajian ini mengukur ukuran tandan anggur (*grape cluster*) di kebun memakai robot bergerak dan kamera RGB-D konsumen. Tujuannya mendukung estimasi hasil panen (*yield estimation*) per tanaman. Penulisnya Kurtser dkk. (2020) di *IEEE Robotics and Automation Letters*. Kajian ini tidak mencacah tandan. Ia mengukur dimensi satu tandan dari awan titik (*point cloud*), yaitu kumpulan titik tiga dimensi yang dihasilkan sensor kedalaman, lalu membandingkannya dengan pengukuran manual.

Sensor yang dipakai adalah Intel RealSense D435, dipasang pada robot semprot rumah kaca pada ketinggian 625 mm dari tanah. Alurnya dimulai dari pelabelan manual atau deteksi otomatis area tandan. Area itu lalu disegmentasi berdasarkan warna memakai *Normalized Difference Index* dan pengelompokan k-means, lalu disaring menurut posisi spasialnya. Ukuran tandan diperoleh dengan mencocokkan kotak pembatas persentil, elipsoid, atau silinder ke awan titik tandan.

Data terdiri atas dua set. Set kontrol berisi 10 tanaman dalam pot, 17 tandan, enam video, tiga sudut pandang, dan variasi dengan atau tanpa latar hitam, dengan 4.072 label manual. Set kebun komersial di Israel selatan berisi 32 tandan dan 470 label. Dataset GRAPES3D dirilis secara publik.

Pada set kontrol, kotak persentil dengan ukuran diagonal memberi galat rerata absolut terkecil, yaitu 2,9 cm (Tabel II). Galat ukuran tepi kotak adalah 3,4 cm. Ketika label manual diganti deteksi otomatis, galat naik menjadi 4,6 sampai 4,9 cm. Di kebun komersial, galat tepi kotak adalah 3,6 ± 3,0 cm dan galat diagonal 4,6 ± 3,9 cm. Elipsoid dan silinder menghasilkan banyak pencilan, dengan proporsi 30 sampai 60% pada hasil yang sudah disaring. Karena itu kotak persentil lebih andal daripada dua metode lain.

Batas kajian ini ada pada tiga hal. Deteksi tandan tidak dikembangkan oleh penulis; galat deteksi otomatis sendiri dilaporkan sebagai alasan perbaikan algoritma deteksi. Standar emas berasal dari anotasi manual pada 17 tandan (kontrol) dan 32 tandan (kebun). Pengukuran elipsoid juga dibatasi oleh pengamatan dari satu sudut pandang, sehingga bagian tandan yang tertutup daun tidak terukur.
