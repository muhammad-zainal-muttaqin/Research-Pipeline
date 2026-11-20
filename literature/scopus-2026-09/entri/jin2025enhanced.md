# Enhanced deep learning model for apple detection, localization, and counting in complex orchards for robotic arm-based harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jin2025enhanced` |
| Judul asli | Enhanced deep learning model for apple detection, localization, and counting in complex orchards for robotic arm-based harvesting |
| Penulis | Jin, Tantan; Han, Xiongzhe; Wang, Pingan; Zhang, Zhao; Guo, Jie; Ding, Fan |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [jin2025enhanced.pdf](../pdf/jin2025enhanced.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.100784

## Gambaran Umum

Kajian dengan kunci `jin2025enhanced` ini memperbaiki detektor YOLOv8n untuk mendeteksi apel, lalu memakai hasil deteksi itu untuk menentukan koordinat 3D setiap apel dan menghitung jumlahnya. Kamera RealSense D455 dipasang pada lengan robot. Model yang diusulkan mencapai precision 81,43%, recall 68,48%, F1 74,40%, dan mAP50 81,68%. Akurasi penghitungan keseluruhan 69,39%, naik 2,42% dibanding YOLOv8n asli.

Penghitungan buah di kebun sulit karena apel tertutup daun dan sebagian apel tertutup apel lain. Kajian ini menanggapi masalah itu dengan mengubah detektor. Dua lapisan C2f terakhir pada backbone diganti dengan modul DWR–DRB (*dilation-wise residual* dengan *dilated re-param block*), yang memperluas bidang reseptif tanpa menambah banyak parameter. Neck memakai GFPN, dan fungsi loss memakai SIoU, yang menghitung arah dan jarak kotak prediksi terhadap kotak acuan.

Setelah deteksi, sistem menentukan posisi 3D setiap apel dari kamera D455 dan menghitung jumlahnya. Galat penghitungan didefinisikan sebagai EN = |N' − N0| (Persamaan 26), dengan N' jumlah hasil prediksi dan N0 jumlah sebenarnya. Teks menyebut hasil deteksi "fed into our algorithm, which performed further analysis to accurately determine the positions and count the number of apples". Algoritma analisis itu tidak diuraikan pada bagian yang dibaca, sehingga belum jelas apakah deteksi dari beberapa posisi lengan digabung.

Uji coba luar ruangan memakai 6 pohon buatan yang berjarak 1 m dan 55 apel buatan. Robot bergerak sejajar pohon pada jarak sekitar 1 m. Citra yang ditangkap berukuran 640×480. Karena pohon dan apel buatan, hasil ini belum menunjukkan kinerja di kebun nyata.

Galat lokalisasi rata-rata adalah X 2,43 mm, Y 3,70 mm, dan Z 1,28 mm. Dibanding model asli, galat itu turun 19,27% (X), 12,67% (Y), dan 23,05% (Z). Penurunan galat pada sumbu Z penting untuk penentuan posisi petik, tetapi kajian tidak menguji dampaknya pada keberhasilan panen.

Kelebihan kajian ini adalah laporan metrik deteksi dan lokalisasi yang lengkap, dengan angka galat per sumbu. Dari sisi rancangan, uji penghitungan memakai objek buatan yang mudah dikontrol, sehingga galat hitung dapat dibandingkan secara langsung dengan jumlah sebenarnya.

Penulis sendiri menyatakan bahwa metode penghitungan "did not achieve the precision of more advanced approaches" dan dipilih karena sederhana. Secara konseptual, penghitungan dari satu tampilan tidak mengatasi apel yang sama yang terlihat dari posisi lengan berbeda, sehingga dengan rancangan ini jumlah yang dilaporkan bergantung pada apakah pengulangan itu ditangani. Keterbatasan ini belum dapat dinilai penuh tanpa membaca bagian prosedur penghitungan.
