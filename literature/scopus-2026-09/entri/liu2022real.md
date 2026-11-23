# Real-time identification, localization, and grading method for navel oranges based on RGB-D camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2022real` |
| Judul asli | Real-time identification, localization, and grading method for navel oranges based on RGB-D camera |
| Penulis | Liu, D.; others |
| Tahun | 2022 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [liu2022real.pdf](../pdf/liu2022real.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.2022.14.018

## Gambaran Umum

Penelitian ini bertujuan membuat algoritma OrangePointSeg yang mengenali, menentukan posisi tiga dimensi, dan menggolongkan ukuran buah jeruk pusar (*navel orange*) secara waktu nyata untuk robot pemetik. Penulis menyebut bahwa pemetikan di Ganzhou masih dilakukan manual, bahwa set data segmentasi instans buah masih kurang, dan bahwa sistem yang ada belum menilai mutu buah. Keluaran algoritma adalah koordinat pusat dan jari-jari tiap buah dalam sistem koordinat kamera, bukan jumlah buah.

Data diambil pada 10 November 2021 pukul 15:00 sampai 17:00 di kebun jeruk di Nankang, Ganzhou, Jiangxi, dengan kamera kedalaman Azure Kinect DK (citra warna 1.920×1.080 piksel). Pohon dipilih acak dan dicitrakan dari beberapa sudut sehingga terkumpul 48 pasang RGB-D. Diameter terbesar dan terkecil diukur dengan jangka sorong, volume dengan metode perpindahan air, dan jarak buah ke sensor dengan pengukur jarak laser. Citra dipotong acak menjadi 242 citra 512×512 piksel, lalu diperbanyak dengan augmentasi menjadi 2.178 citra berisi 8.712 sampel. Sebanyak 70% menjadi data latih dan 30% data validasi. Pemberi label tidak disebut. Buah hijau tidak dilabeli.

Metode terdiri dari dua tahap. Tahap pertama adalah YOLACT-Fruit, yaitu YOLACT (segmentasi instans satu tahap) dengan tulang punggung HRNet dan HRFPN yang mempertahankan resolusi tinggi, menghasilkan masker per buah dalam dua kelas, yaitu tidak atau sedikit tertutup dan banyak tertutup. Tahap kedua memotong peta kedalaman yang telah dicocokkan dengan masker itu menjadi awan titik per buah, mengurangi jumlah titik, membuang titik pencilan, lalu mencocokkan bola dengan metode kuadrat terkecil. Hasilnya adalah pusat dan jari-jari bola, dan jari-jari menentukan golongan ukuran.

Pada data validasi, YOLACT-Fruit mencapai AP masker 31,15% dengan 44,63 bingkai/s. Teks memuat juga angka 31,35% untuk model yang sama. Pada tabel pembanding, YOLACT dasar bertulang punggung ResNet101 memperoleh AP 28,5% dan 34,41 bingkai/s. Pada pencocokan bola dengan 1.400 sampai 2.000 titik, galat akar kuadrat rata-rata jari-jari adalah 0,43 cm, galat volume 52,6 mL, galat posisi 0,49 cm, dan waktu 1,99 ms. Pada jarak sampai 1 m dengan titik minimal 800, galat jari-jari tetap di bawah 0,5 cm. Kecepatan total 29,4 bingkai/s pada adegan berisi 10 buah.

Keterbatasan yang dapat diperiksa dari teks: pembagian 70:30 dilakukan pada citra hasil augmentasi dari 242 potongan yang berasal dari 48 citra, dan teks tidak menyatakan bahwa pembagian dilakukan per citra asal atau per pohon. Jumlah buah dan jumlah pohon yang dipakai untuk uji penentuan posisi dan golongan ukuran tidak disebut. Tidak ada pencacahan buah. Buah yang tertutup berat tidak dilabeli, dan buah hijau diabaikan. Pada jarak 1,5 m jari-jari dengan titik di bawah 1.400 gagal memenuhi batas 0,5 cm.
