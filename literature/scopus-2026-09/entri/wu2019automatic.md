# Automatic recognition of juicy peaches on trees based on 3D contour features and colour data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2019automatic` |
| Judul asli | Automatic recognition of juicy peaches on trees based on 3D contour features and colour data |
| Penulis | Wu, Gang; Zhu, Qibing; Huang, Min; Guo, Ya; Qin, Jianwei |
| Tahun | 2019 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | peach/nectarine |

## Tautan Akses
- PDF: [wu2019automatic.pdf](../pdf/wu2019automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2019.10.002

## Gambaran Umum

Kajian ini membahas kebutuhan robot pemanen buah untuk mendeteksi buah secara cepat dan akurat di kebun. Deteksi buah yang tepat menentukan keberhasilan pemetikan. Selain itu, hitungan buah dapat dipakai untuk memperkirakan hasil panen kebun. Pencitraan dua dimensi hanya menangkap warna dan bentuk pada bidang gambar. Pendekatan ini tidak dapat menggambarkan ukuran nyata buah maupun posisinya terhadap objek lain di lingkungan kerja. Karena itu, penulis mengusulkan metode deteksi buah persik yang menggabungkan data warna dan fitur kontur 3D.

Data dikumpulkan dari buah persik pada pohon di kondisi lapangan yang sesungguhnya. Sensor yang dipakai adalah kamera *RGB-D* yang menghasilkan citra warna dan data kedalaman dalam bentuk *point cloud*. Penulis memilih tujuh *point cloud* dengan total 41 buah. Pengujian dilakukan dalam tiga situasi dengan tingkat oklusi yang berbeda. Waktu pemrosesan diukur pada komputer dengan prosesor Intel Core i5 3230M 2,6 GHz dan memori 8 GB.

Metode bekerja dalam beberapa tahap. Pertama, latar belakang dibuang dan *point cloud* dibagi menjadi beberapa klaster berdasarkan posisi dengan algoritma *conditional Euclidean clustering*. Kedua, fitur kontur 3D dipakai untuk mengekstraksi buah dari klaster. Klaster yang berisi beberapa buah berdekatan diproses dengan segmentasi bola *random sample consensus* (RANSAC). Segmentasi lingkaran *progressive sample consensus* (PROSAC) dipakai untuk meningkatkan akurasi. Evaluasi memakai *precision* dan *recall*. Nilai *recall* disamakan dengan akurasi pengenalan buah dalam kajian ini. Hasil total akurasi pengenalan mencapai 88,68%. Waktu rata-rata pengenalan satu buah adalah 292,4 ms. Pada tiga situasi, *recall* tercatat 97,83%, 89,74%, dan 74,29%. Nilai ini lebih tinggi daripada metode yang hanya memakai segmentasi bola secara langsung. Penulis juga menyebut bahwa *precision* metode ini melampaui 97,83% pada semua situasi. Penulis menyimpulkan bahwa waktu pemrosesan ini memenuhi kebutuhan deteksi buah untuk robot yang menargetkan buah matang.

Penulis menyatakan beberapa batasan. Oklusi berat menyulitkan segmentasi model berbasis bentuk. Buah yang belum matang sering memiliki warna mirip dengan latar, sehingga tersaring saat buah matang diambil. Pantulan cahaya juga membuat sebagian buah sulit dideteksi dan menurunkan akurasi keseluruhan. Akurasi lebih rendah ketika banyak buah belum matang berada di pohon, sehingga metode dinilai lebih andal untuk buah merah matang. Metode ini cocok untuk buah berbentuk mendekati bola seperti persik, apel, dan jeruk. Bentuk buah yang kompleks masih perlu penanganan lanjutan. Penulis juga menegaskan bahwa pengaruh variasi cahaya perlu diteliti pada studi selanjutnya. Perbaikan tahap pra-pemrosesan *point cloud* juga direncanakan untuk pekerjaan berikutnya.
