# Fast detection and location of longan fruits using UAV images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2021fast` |
| Judul asli | Fast detection and location of longan fruits using UAV images |
| Penulis | Li, Denghui; Sun, Xiaoxuan; Elkhouchlaa, Hamza; Jia, Yuhang; Yao, Zhongwei; Lin, Peiyi; Li, Jun; Lu, Huazhong |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [li2021fast.pdf](../pdf/li2021fast.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106465

## Gambaran Umum

Kajian ini bertujuan memungkinkan pemetikan buah longan oleh pesawat tanpa awak (UAV). Robot pemetik di darat sulit beradaptasi dengan medan kebun di pegunungan dan tidak dapat menjangkau buah pada pohon longan yang tinggi. Masalah utamanya adalah mendeteksi dan melokalisasi buah longan secara cepat dan akurat dari citra yang diambil UAV. Citra UAV juga mudah kabur karena getaran dan aliran udara, sehingga perlu disaring sebelum diproses.

Data dikumpulkan dengan kamera Intel RealSense D455 yang dipasang pada UAV DJI Jingwei M600PRO. Kamera ini menghasilkan citra warna berukuran 1280 × 720 piksel dan memiliki kanal kedalaman. Dua varietas longan, Shixia dan Chuliang, dipotret dari jarak 0,5–0,8 m (jarak dekat) dan 0,8–1,2 m (jarak jauh). Pengambilan dilakukan dalam kondisi cerah, berlawanan cahaya, dan berawan, tanpa bayangan buatan. Setelah pemotongan acak untuk memperbanyak sampel, jumlah citra menjadi 1050. Citra kabur dibuang dengan operator Laplacian of Gaussian dan ambang varians abu-abu. Citra yang lolos kemudian dinormalisasi ke ukuran 1280 × 1280 piksel.

Metode yang diusulkan memakai jaringan YOLOv4 dengan *backbone* MobileNet yang ringan. Informasi warna dan kedalaman digabung dalam skema RGB-D, lalu titik petik ditentukan dari hasil deteksi pada cabang utama. Menurut pernyataan penulis, dibanding FPN, YOLOv3, dan YOLOv4, model ini mengurangi komputasi, jumlah parameter, dan waktu deteksi. Dibanding MobileNet-SSD dan YOLOv4-tiny, akurasi deteksinya meningkat. Kinerja model dan platform pemetikan juga diuji lewat percobaan pemetikan di kebun longan.

Penulis menyebut kelebihan kombinasi UAV, kamera RGB-D, dan CNN untuk meningkatkan kecepatan dan akurasi deteksi serta lokalisasi buah longan. Batasan kajian ini belum dapat dirangkum dari bagian yang terbaca.
