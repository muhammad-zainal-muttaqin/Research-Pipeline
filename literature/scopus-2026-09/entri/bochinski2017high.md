# High-Speed tracking-by-detection without using image information

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bochinski2017high` |
| Judul asli | High-Speed tracking-by-detection without using image information |
| Penulis | Bochinski, Erik; Eiselein, Volker; Sikora, Thomas |
| Tahun | 2017 |
| Venue | 2017 14th IEEE International Conference on Advanced Video and Signal Based Surveillance Avss 2017 |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [bochinski2017high.pdf](../pdf/bochinski2017high.pdf)
- DOI resmi: https://doi.org/10.1109/avss.2017.8078516

## Gambaran Umum

Bochinski dkk. (2017) mengusulkan pelacak objek IOU (*intersection over union*) untuk tracking-by-detection. Pelacak ini mengaitkan kotak deteksi pada frame berurutan jika tumpang-tindih kotaknya cukup besar, tanpa membaca isi citra. Penulis menguji metode pada dataset kendaraan UA-DETRAC dan pejalan kaki MOT16/MOT17.

Pada DETRAC, penulis melaporkan bahwa pelacak IOU mengungguli enam metode pembanding pada metrik keseluruhan PR-MOTA dan PR-MOTP, serta pada PR-MT dan PR-ML. Kecepatan yang dilaporkan lebih dari 100K fps dengan deteksi R-CNN, dibanding 0,7 sampai 390 fps untuk metode pembanding. Kecepatan itu diukur pada implementasi Python murni tanpa optimasi.

Setiap frame memiliki daftar deteksi dengan skor kepercayaan. Deteksi dengan skor di bawah σl dibuang. Track dimulai dari deteksi dengan skor minimal σh. Deteksi pada frame berikutnya dikaitkan dengan track jika IOU-nya melebihi σIOU. Track yang lebih pendek dari tmin frame dibuang. Parameter σIOU, σh, dan tmin dicari dengan grid search pada data latih, dengan rentang yang berbeda untuk tiap detektor.

Hasil pada DETRAC bergantung pada detektor. Pada EB, penulis mengakui bahwa hasilnya diuntungkan oleh kelemahan metrik, karena deteksi berskor sangat rendah memperpanjang kurva PR. Hasil pembanding di tabel adalah rerata empat detektor, sehingga tidak dapat ditiru penulis karena kebijakan server uji. Penulis juga menyatakan bahwa metode ini rentan terhadap galat deteksi dan tidak mengisi deteksi yang hilang.

Pada MOT16, pelacak ini mencapai MOTA 57,1 dengan deteksi SDP, dibanding 71,0 untuk metode terbaik. Penulis menyebut kondisi yang sulit untuk pejalan kaki: ukuran dan rasio aspek berubah, oklusi berat, dan frame rate rendah. Penulis sendiri menyatakan bahwa metode ini baik untuk objek berukuran tetap, kamera diam, dan deteksi akurat pada frame rate tinggi.
