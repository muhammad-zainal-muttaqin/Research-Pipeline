# Citrus Positioning Method Based on Camera and Lidar Data Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xu2022citrus` |
| Judul asli | Citrus Positioning Method Based on Camera and Lidar Data Fusion |
| Penulis | Xu, Chengjie; Wang, Can; Kong, Bin; Yi, Bingliang; Li, Yue |
| Tahun | 2022 |
| Venue | Smart Innovation Systems and Technologies |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [xu2022citrus.pdf](../pdf/xu2022citrus.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-19-2448-4_15

## Gambaran Umum

Bab buku ini (Smart Innovation, Systems and Technologies, 2022) menentukan posisi 3D jeruk untuk robot pemetik dengan menggabungkan kamera dan LiDAR.

YOLOv3 dilatih pada 2.000 citra jeruk di lingkungan alami untuk menentukan pusat buah dalam koordinat piksel. Parameter dalam kamera dikalibrasi dengan papan kalibrasi, dengan galat reproyeksi 0,16 piksel. Kamera dan LiDAR lalu dikalibrasi bersama dengan papan yang sama. Bidang papan pada awan titik dicocokkan dan tepinya dicari dengan RANSAC. Awan titik diproyeksikan ke citra, sehingga depth di dalam kotak deteksi dapat dibaca. Koordinat X dan Y pusat buah dihitung dari depth itu dan parameter kamera.

Dari 50 pengukuran, galat posisi tidak melebihi 0,01 m. Rerata galatnya 5,82 mm pada arah X dan 5,8 mm pada arah Y. Penulis menyebut galat kalibrasi kamera dan pengukuran tangan sebagai sumber galat.

Tempat percobaan posisi tidak dijelaskan. Penulis menyatakan bahwa buah yang tertutup atau berdempetan belum ditangani dan bahwa LiDAR mahal. Buah tidak dicacah.
