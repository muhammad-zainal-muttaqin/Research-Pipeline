# Hyperparameter optimization of YOLOv4 tiny for palm oil fresh fruit bunches maturity detection using genetics algorithms

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `salim2023hyperparameter` |
| Judul asli | Hyperparameter optimization of YOLOv4 tiny for palm oil fresh fruit bunches maturity detection using genetics algorithms |
| Penulis | Salim, Edy; Suharjito |
| Tahun | 2023 |
| Venue | Smart Agricultural Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [salim2023hyperparameter.pdf](../pdf/salim2023hyperparameter.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2023.100364

## Gambaran Umum

Kajian ini membahas deteksi tingkat kematangan tandan buah segar (TBS) kelapa sawit. Harga minyak sawit bergantung pada kandungan minyak buah, dan kandungan minyak itu berkaitan dengan tingkat kematangan. Selama ini penilaian kematangan dilakukan ahli secara manual. Penilaian visual tersebut bersifat subjektif dan dapat menimbulkan kesalahan. Penulis memakai *computer vision* dengan model *YOLOv4* agar deteksi lebih objektif. Model ini termasuk *object detection* waktu-nyata yang sudah banyak dipakai untuk menilai kematangan berbagai buah. Penulis juga menilai bahwa penyetelan hiperparameter pada penelitian sebelumnya masih dilakukan secara manual. Karena itu, penelitian ini menerapkan algoritma genetika (*genetic algorithm*, GA) untuk mencari laju pembelajaran (*learning rate*) yang optimal. Tujuannya ialah memperoleh model yang lebih baik dari segi efisiensi dan akurasi.

Data penelitian berupa 4.160 citra TBS kelapa sawit. Citra dikelompokkan ke dalam enam kategori, yaitu *empty fruit*, *underripe*, *abnormal*, *ripe*, *under-ripe*, dan *over-ripe*. Pelatihan dan pengujian dilakukan menggunakan Google Colaboratory Pro+ dengan GPU NVIDIA A100-SXM4-40GB. Penelitian ini menggunakan model YOLOv4-tiny, versi YOLOv4 yang lebih kecil. Model ini memiliki lapisan lebih sedikit dan dua lapisan deteksi, sehingga pelatihannya lebih cepat. Akurasinya biasanya lebih rendah dibanding YOLOv4 penuh. Penulis juga menyebut bahwa penelitian sebelumnya dengan YOLOv4 pada kematangan kelapa sawit telah mencapai akurasi di atas 95 %.

Penelitian menyusun empat model. Dua model dasar adalah YOLOv4-tiny dan YOLOv4-tiny dengan *early stopping*. Mekanisme *early stopping* memakai parameter *patience* sebesar 5. Pelatihan dihentikan bila nilai mAP tidak membaik selama jumlah tersebut. Pada tahap optimasi, GA mencari laju pembelajaran. Populasi awal dibangkitkan secara acak dalam rentang 0,01 sampai 0,0001. Fungsi kebugaran (*fitness*) yang dipakai ialah nilai mAP (*mean Average Precision*) model. GA menjalankan seleksi, persilangan, dan mutasi untuk memperoleh gen yang lebih baik. Model dasar kemudian dilatih ulang dengan laju pembelajaran hasil GA. Keempat model, yaitu YOLOv4-tiny, YOLOv4-tiny ES, YOLOv4-tiny setelah GA, dan YOLOv4-tiny ES setelah GA, diuji menggunakan data uji. Hasil utama yang dilaporkan penulis adalah model YOLOv4 mengalami peningkatan mAP dibandingkan sebelum optimasi hiperparameter dengan GA. Metode ini juga dinilai dapat mempercepat pelatihan dan menekan biaya komputasi.
