# Estimating strawberry size using improved YOLOv8s-seg and semi-truncated cone models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026estimating` |
| Judul asli | Estimating strawberry size using improved YOLOv8s-seg and semi-truncated cone models |
| Penulis | Liu, X.; others |
| Tahun | 2026 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [liu2026estimating.pdf](../pdf/liu2026estimating.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202508046

## Gambaran Umum

Kajian ini (Liu dkk., 2026, Transactions of the CSAE, bahasa Mandarin dengan abstrak Inggris) mengukur ukuran tiga dimensi buah stroberi di kebun bedengan. Ukuran yang diukur adalah diameter panjang (longitudinal), diameter atas (top), dan diameter bawah (bottom). Input berasal dari satu kamera RGB-D Intel RealSense D435i dengan resolusi 640 × 480 piksel, dari satu sudut pandang miring. Kajian tidak menggabungkan beberapa pengamatan dari beberapa sudut.

Data yang dipakai terdiri atas 1.109 citra, dibagi menjadi 889 untuk latih, 110 untuk validasi, dan 110 untuk uji. Model segmentasi yang dipakai adalah YOLOv8s-seg yang diperbaiki dengan modul C2f_Faster_EMA pada backbone. Hasil segmentasi dilaporkan dengan mAP@0,5 sebesar 96,9% dan akurasi segmentasi buah matang sebesar 98,3%. Kecepatan inferensi segmentasi sebesar 159,3 bingkai per detik.

Dari mask hasil segmentasi, kajian membentuk awan titik 3D dari data kedalaman. Awan titik itu difilter dengan penghapusan pencilan statistik dan downsampling voxel grid, sehingga tersisa kira-kira 100 sampai 150 titik. Sumbu utama buah dan pusat massanya dicari dengan RANSAC-PCA. Ukuran akhir diperoleh dengan mencocokkan model kerucut terpotong setengah (semi-truncated cone) yang didefinisikan oleh tinggi, diameter atas, dan diameter bawah, menggunakan optimasi L-BFGS-B.

Model kerucut dipilih karena bentuk stroberi menyerupai kerucut dengan dasar kelopak yang terpotong. Penulis menyatakan bahwa diameter bawah sering tidak terlihat dari sudut pandang kamera, sehingga model elips simetris tidak dapat memperkirakannya dengan tepat. Dalam perbandingan dengan model elips, kajian ini mencatat bahwa model elips hanya memberi satu diameter puncak dan tidak memiliki parameter diameter bawah.

Hasil ukuran dilaporkan dalam tiga bentuk. Pertama, pada beberapa sudut pandang, rerata galat relatif adalah 1,2% (panjang), 0,7% (atas), dan 1,7% (bawah). Kedua, pada tinggi pengambilan gambar 30 sampai 70 cm, galat relatif adalah 1,8%, 1,2%, dan 4,8%. Ketiga, pada uji 22 spesimen standar, rerata galat (bias) adalah -0,13 mm (panjang), 0,03 mm (atas), dan -0,03 mm (bawah). Standar deviasi galat untuk ketiga dimensi berturut-turut adalah 1,64 mm, 1,84 mm, dan 1,47 mm.

Dibandingkan dengan TSDF tunggal-citra yang disesuaikan oleh penulis, galat mutlak diameter atas dan diameter bawah turun masing-masing sekitar 50% dan 70%, menurut abstrak. Pada tabel perbandingan, nilai rerata galat TSDF untuk panjang, atas, dan bawah adalah -0,34 mm, 0,08 mm, dan 0,14 mm, sedangkan model kerucut terpotong menghasilkan -0,17 mm untuk panjang dan -0,04 mm untuk bawah. Tabel tidak melaporkan nilai diameter atas untuk model kerucut. Semua perbandingan dilakukan pada satu sudut dan satu tinggi, dengan 10 kali ulangan, sehingga tidak mencakup variasi kondisi kebun yang lebih luas.

Waktu pemrosesan ujung ke ujung (end-to-end) dilaporkan 3,3 detik per bingkai. Angka 159,3 bingkai per detik hanya berlaku untuk tahap segmentasi, sehingga keduanya tidak dapat dibandingkan langsung.

Keterbatasan yang tercantum dalam naskah dan yang terlihat dari desain uji meliputi: (a) hanya satu sudut miring yang dipakai untuk pengambilan data; (b) jumlah spesimen untuk uji ukuran hanya 22 buah standar, bukan panen lapangan; (c) pembandingan TSDF adalah versi yang dimodifikasi penulis, bukan implementasi standar; (d) hasil pada stroberi di bedengan tidak diuji pada tanaman atau sensor lain.
