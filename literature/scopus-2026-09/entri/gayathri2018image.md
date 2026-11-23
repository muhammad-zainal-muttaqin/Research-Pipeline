# Image Processing System for Automatic Segmentation and Yield Prediction of Fruits using Open CV

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gayathri2018image` |
| Judul asli | Image Processing System for Automatic Segmentation and Yield Prediction of Fruits using Open CV |
| Penulis | Gayathri Devi, T.; Neelamegam, P.; Sudha, S. |
| Tahun | 2018 |
| Venue | International Conference on Current Trends in Computer Electrical Electronics and Communication Ctceec 2017 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, citrus, mango, cherry, pomegranate |

## Tautan Akses
- PDF: [gayathri2018image.pdf](../pdf/gayathri2018image.pdf)
- DOI resmi: https://doi.org/10.1109/ctceec.2017.8455137

## Gambaran Umum

Penulis mengusulkan sistem pengolahan citra untuk segmentasi dan pencacahan buah otomatis sebagai dasar prediksi hasil panen. Latar masalahnya adalah pencacahan buah secara manual yang memakan tenaga. Sistem dibuat dengan OpenCV dan Python.

Data berupa citra beberapa jenis buah: jeruk atau tangerine, delima, apel, lemon, mangga, dan ceri. Jumlah buah per citra kecil, antara 2 dan 18 buah menurut tabel. Sumber citra, sensor, jumlah citra total, pemberi label, dan pembagian latih dan uji tidak disebut. Acuan adalah hitungan manual.

Metodenya berurutan. Latar belakang disingkirkan dengan *graph cut* (pemisahan latar dan objek memakai area yang ditentukan pengguna). Citra diubah dari RGB ke ruang warna HSV, lalu buah diambil dengan ambang warna (*color thresholding*). Derau dikurangi dengan tapis Gaussian. Tepi dideteksi dengan Canny, wilayah terhubung diberi label (*connected component labeling*), dan lingkaran dicocokkan pada tepi kuat. Jumlah lingkaran yang cocok dianggap jumlah buah. Penulis juga mengukur akurasi persentase dan MAPE (*mean absolute percentage error*).

Hasilnya dilaporkan per citra pada dua tabel. Akurasi pada tabel dengan analisis bentuk dan warna antara 92% (lemon 1) dan 100% (lemon 2, delima, apel 2, mangga, ceri), dan 83,33% sampai 94,44% untuk tiga citra jeruk. Tabel pembanding dengan kontur memberi akurasi lebih rendah, antara 30,33% dan 100%. Teks menyebut pendekatan warna dan bentuk lebih akurat daripada fitur kontur. Abstrak menyatakan segmentasi lebih dari 98% akurat, tetapi dasar angka itu tidak dijelaskan.

Keterbatasan yang dapat diperiksa: hanya sekitar sembilan citra dengan buah sedikit, tanpa pembagian per pohon atau data uji terpisah. Hitungan algoritma pada tabel tidak pernah melebihi hitungan manual. Rumus akurasi tidak memperhitungkan kesalahan ganda atau buah yang tidak cocok posisinya. Satu pandang per citra, sehingga tidak ada penanganan hitung ganda antarpandang.
