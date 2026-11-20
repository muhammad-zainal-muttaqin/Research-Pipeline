# Detection of red and bicoloured apples on tree with an RGB-D camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nguyen2016detection` |
| Judul asli | Detection of red and bicoloured apples on tree with an RGB-D camera |
| Penulis | Nguyen, Tien Thanh; Vandevoorde, Koenraad; Wouters, Niels; Kayacan, Erdal; De Baerdemaeker, Josse G.; Saeys, Wouter |
| Tahun | 2016 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [nguyen2016detection.pdf](../pdf/nguyen2016detection.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2016.01.007

## Gambaran Umum

Nguyen dkk. (2016) mengembangkan teknik sensing untuk mendeteksi dan melokalisasi apel di pohon menggunakan kamera RGB-D Kinect v1 (Xbox 360 Kinect model 1414). Algoritma menggabungkan informasi warna dan kedalaman (depth) dalam satu awan titik (point cloud) 3D. Pengujian dilakukan di kebun berpola pagar (espalier) di Santa Rosa, Chile, pada pohon apel Gala dan Fuji.

Sensor memproyeksikan pola titik inframerah dan menghitung jarak tiap piksel. Algoritma tiga tahap: (1) penyaringan awan titik berdasarkan jarak ke baris pohon terdekat dan berdasarkan warna merah (koefisien r dan g dari Bulanon dkk., 2002); (2) segmentasi Euclidean clustering dengan jarak ambang 3 mm dan ukuran klaster minimum 165 titik; (3) pascapemrosesan. Klaster yang berisi banyak apel dipisahkan dengan circular Hough transform, dan klaster satu apel yang terpecah digabungkan dengan RANSAC. Pusat dan diameter tiap apel kemudian diestimasi dengan model bola.

Dataset pertama berisi 5 pohon Gala dengan 86 apel, sebagian di antaranya dibuat sepenuhnya terlihat untuk mengukur akurasi deteksi. Dataset kedua berisi 10 pohon Fuji dengan 225 apel dalam kondisi tertutup alami. Kebenaran lapangan posisi diukur dengan sensor elektromagnetik 3D Guidance trakSTAR (akurasi statis 1,4 mm RMS). Abstrak melaporkan deteksi 100% untuk apel utuh dan 82% untuk apel sebagian tertutup, galat lokasi di bawah 10 mm pada semua sumbu, dan waktu proses di bawah 1 detik untuk 20 apel.

Penulis sendiri mencatat bahwa algoritma gagal memisahkan apel yang bergerombol rapat, sehingga jumlahnya cenderung kurang dihitung dan lokasinya bisa keliru. Estimasi orientasi apel tidak dilakukan karena data sensor dinilai tidak cukup rinci. Pengukuran hanya di satu lingkungan kebun dengan cahaya tidak langsung, karena kamera dilindungi tirai plastik hitam dari sinar matahari langsung.
