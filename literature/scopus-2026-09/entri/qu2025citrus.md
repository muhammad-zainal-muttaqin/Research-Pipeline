# Citrus fruit diameter estimation in the field using monocular camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qu2025citrus` |
| Judul asli | Citrus fruit diameter estimation in the field using monocular camera |
| Penulis | Qu, Hongchun; Du, Haitong; Tang, Xiaoming; Zhai, Shidong |
| Tahun | 2025 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [qu2025citrus.pdf](../pdf/qu2025citrus.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2025.02.012

## Gambaran Umum

Kajian ini bertujuan mengukur diameter buah jeruk di lapangan dengan satu kamera monokular. Ukuran buah penting untuk pengelolaan bentuk pohon dan estimasi hasil panen. Pengukuran manual memang andal, tetapi memerlukan banyak tenaga. Metode mesin yang ada sering membutuhkan kalibrasi jarak atau sensor 3D, sedangkan sensor 3D mahal dan rumit dipasang. Penulis mengusulkan kerangka kerja berbiaya rendah yang memakai daun matang dan sehat sebagai objek referensi alami. Dengan cara ini, penanda manual dan kalibrasi parameter kamera tidak diperlukan.

Data dikumpulkan dari tiga lokasi di Chongqing, Tiongkok, pada 2023. Seluruhnya terdapat 1060 citra yang diambil dengan ponsel pintar, antara lain Apple 12, Vivo, OPPO, dan Redmi. Citra mencakup tiga varietas jeruk. Sebanyak 200 citra berisi jeruk navel (*Citrus sinensis* var. navel) yang belum matang. Sebanyak 300 citra berisi jeruk Chunjian (*Citrus reticulata* 'Chun Jian') yang sudah matang. Sebanyak 560 citra berisi jeruk darah (*Citrus sinensis* var. sanguinea) dan jeruk navel yang sudah matang. Untuk pelatihan deteksi, 700 citra diberi *bounding box* secara manual pada setiap buah. Untuk tahap daun referensi, 600 citra potongan dipilih dan diberi anotasi buah beserta daun di sekitarnya.

Metode terdiri atas tiga tahap. Tahap pertama menentukan posisi buah dengan deteksi objek dan memotong citra di sekitar setiap buah. Tahap kedua mencari daun referensi di dalam kotak potong dan menyaring daun yang terlalu besar atau berbentuk tidak beraturan. Tahap ketiga menghitung diameter buah dengan algoritma triangulasi berdasarkan daun referensi tersebut. Model deteksi YOLOv8 diperkaya dengan *deformable convolution* (DNCv2) dan *shuffle attention* (SA) agar tetap mengenali buah yang tertutup daun. Hasil utama adalah akurasi 93,14% dan R2 = 0,76. Variasi ukuran daun pada tiga varietas memberi galat relatif kurang dari 3,2% pada estimasi diameter. Untuk evaluasi model deteksi, penulis memakai *mean average precision* (mAP@50 dan mAP@50:95), presisi, dan recall. Untuk akurasi diameter, penulis memakai R2, MAE, MAPE, dan RMSE.

Penulis menyatakan bahwa buah sering tertutup daun, cabang, atau buah lain di lapangan. Kondisi ini dapat menyebabkan buah terlewat dalam deteksi atau menghasilkan ukuran yang keliru. Daun juga sering miring menjauhi kamera, sehingga ukuran referensinya kurang akurat. Penulis mencatat bahwa ukuran kotak potong memengaruhi jumlah daun yang tersedia, dan jumlah daun memengaruhi kesimpulan statistik tentang ukuran buah. Penulis berencana menjajaki strategi multi-frame atau multi-view pada pekerjaan selanjutnya untuk memperbaiki pengukuran di bawah oklusi berat.
