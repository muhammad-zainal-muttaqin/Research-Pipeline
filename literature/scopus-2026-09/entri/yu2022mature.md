# Mature pomegranate fruit detection and location combining improved F-PointNet with 3D point cloud clustering in orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yu2022mature` |
| Judul asli | Mature pomegranate fruit detection and location combining improved F-PointNet with 3D point cloud clustering in orchard |
| Penulis | Yu, Tao; Hu, Chunhua; Xie, Yuning; Liu, Jizhan; Li, Pingping |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | pomegranate |

## Tautan Akses
- PDF: [yu2022mature.pdf](../pdf/yu2022mature.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107233

## Gambaran Umum

Deteksi dan lokalisasi buah sangat penting untuk hortikultura dan robot pemanen di kebun. Metode deteksi berbasis citra 2D masih sulit menghadapi perubahan cahaya, tertutup daun dan cabang, serta buah yang saling tumpang tindih. Kajian ini mengusulkan metode deteksi dan lokalisasi buah delima matang yang memadukan F-PointNet yang ditingkatkan dengan pengelompokan awan titik 3D. Tujuannya adalah meningkatkan akurasi deteksi dan lokalisasi buah pada kondisi kebun yang tidak terstruktur.

Data dikumpulkan di Kebun Hugang, Nanjing, Provinsi Jiangsu, Tiongkok, pada 11 Oktober 2020 saat cuaca berawan dan 12 Oktober 2020 saat cerah. Sensor yang dipakai adalah kamera Microsoft Kinect 2.0 yang merekam citra warna, citra kedalaman, dan fusi RGB-D secara bersamaan. Penulis mengambil 1000 citra dari 48 pohon delima matang dengan sudut dan jarak berbeda, yaitu 1 m, 1,2 m, dan 1,5 m. Pengambilan dilakukan antara pukul 10.00 hingga 17.00, dengan menghindari sinar matahari langsung. Untuk melatih jaringan, penulis memakai augmentasi data berupa rotasi acak dan gangguan Gaussian pada titik awan.

Metode terdiri atas tiga tahap. Pertama, Mask R-CNN dengan fusi RGB-D menghasilkan region usulan untuk deteksi dan segmentasi buah. Kedua, PointNet dipadukan dengan algoritma OPTICS berbasis manifold distance untuk memisahkan buah yang tumpang tindih dan menyegmentasi awan titik di dalam frustum, lalu kotak 3D ditempatkan pada wilayah target. Ketiga, fitting bola dipakai untuk memperoleh posisi dan ukuran setiap buah. Pada perbandingan, Mask R-CNN dengan fusi RGB-D memberikan kinerja terbaik dengan skor F1 0,845 dan skor AP 0,952. F-PointNet yang ditingkatkan juga lebih baik daripada F-PointNet klasik. Pada pengujian pengukuran radius terhadap 100 sampel yang dipilih acak, RMSE sebesar 0,235 cm, R2 sebesar 0,826, dan error posisi kurang dari 5 mm. Hasil ini menunjukkan bahwa metode mampu mendeteksi dan melokalisasi satu buah delima matang di lingkungan kebun yang tidak terstruktur.
