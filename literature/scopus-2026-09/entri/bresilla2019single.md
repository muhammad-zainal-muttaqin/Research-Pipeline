# Single-shot convolution neural networks for real-time fruit detection within the tree

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bresilla2019single` |
| Judul asli | Single-shot convolution neural networks for real-time fruit detection within the tree |
| Penulis | Bresilla, Kushtrim; Perulli, Giulio Demetrio; Boini, Alexandra; Morandi, Brunella; Corelli Grappadelli, Luca; Manfrini, Luigi |
| Tahun | 2019 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, pear |

## Tautan Akses
- PDF: [bresilla2019single.pdf](../pdf/bresilla2019single.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2019.00611

## Gambaran Umum

Bresilla dkk. (2019) menguji apakah detektor satu tahap *single-shot detector* YOLO dapat mendeteksi dan menghitung buah apel dan pir pada citra kanopi pohon. Penulis melatih model dengan lebih dari 5.000 citra dan menguji pada citra dari kamera ponsel. Hasil utama adalah F1 tertinggi 0,81 pada model M1, dengan kecepatan 5 FPS pada Jetson TX2 dan 8 FPS pada GeForce 960M.

Data dikumpulkan dari 100 citra pohon apel dan 50 citra pohon pir, dengan sekitar 50 buah per citra. Citra diambil sebelum apel berwarna, sehingga sebagian buah masih menyatu dengan daun. Citra dipotong dan diubah ukurannya menjadi 608×608 piksel untuk model M1 dan M2, dan 1216×1216 piksel untuk M3. Model menandai setiap buah dengan *bounding box*, yaitu kotak pembatas yang mengelilingi objek, dan jumlah kotak per bingkai dipakai sebagai estimasi jumlah buah. Penulis membangun model hitung per pohon dari korelasi antara jumlah buah yang terlihat per bingkai dan jumlah buah nyata per pohon.

Ketiga model dibandingkan pada F1, IoU, dan FPS. M1 mencapai F1 0,81 dengan IoU relatif tinggi, tetapi hanya 5 FPS pada TX2 dan 8 FPS pada 960M. M2 mencapai F1 0,77 dengan IoU 0,53, dengan kecepatan 15 FPS pada TX2 dan 20 FPS pada 960M. M3 mencapai F1 0,79 dengan IoU 0,58, tetapi kecepatannya lebih rendah daripada M2. Pada bagian kesimpulan, penulis melaporkan F1 0,79 dengan 5.000 citra apel, dan F1 naik menjadi 0,9 setelah augmentasi data pada sekitar 20.000 buah. Angka 0,838 yang muncul di pendahuluan berasal dari DeepFruits (Sa dkk., 2016) dan bukan hasil kajian ini.

Keterbatasan yang dinyatakan penulis adalah model tidak dapat membedakan dua objek dengan kategori sama yang berada dalam satu sel grid. Dalam kebun dengan buah berkelompok, kondisi ini dapat menurunkan hitungan. Galat hitung tingkat pohon tidak dilaporkan sebagai metrik utama, dan kajian tidak mengevaluasi lintas pandang, sehingga buah yang terlihat di beberapa bingkai belum tentu dihitung sekali.

Kajian ini berguna sebagai bukti bahwa detektor satu tahap dapat dipakai untuk pencacahan apel dan pir dengan F1 sekitar 0,8 pada satu pandang. Batas kajian ini berada pada tiga hal: data berasal dari dua spesies dengan kamera ponsel, metrik per bingkai tidak sama dengan galat hitung per pohon, dan tidak ada mekanisme deduplikasi antarbingkai.
