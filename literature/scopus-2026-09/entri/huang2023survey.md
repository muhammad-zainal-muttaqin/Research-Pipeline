# A survey of deep learning-based object detection methods in crop counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `huang2023survey` |
| Judul asli | A survey of deep learning-based object detection methods in crop counting |
| Penulis | Huang, Yuning; Qian, Yurong; Wei, Hongyang; Lu, Yiguo; Ling, Bowen; Qin, Yugang |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [huang2023survey.pdf](../pdf/huang2023survey.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108425

## Gambaran Umum

Penghitungan tanaman (*crop counting*) merupakan langkah penting dalam estimasi hasil panen, karena jumlah tanaman yang terpantau membantu menilai status pertumbuhan dan memungkinkan penyesuaian untuk meningkatkan hasil serta mutu. Penghitungan manual dinilai memakan waktu, bergantung pada pengamat, dan sangat rentan kesalahan pada produksi berskala besar, sehingga tidak memadai untuk kebutuhan analisis data dalam pertanian presisi. Kajian ini bertujuan merangkum perkembangan metode deteksi objek (*object detection*) berbasis *deep learning* untuk penghitungan tanaman, membandingkannya dengan metode penghitungan lain, serta memperkenalkan *dataset* publik dan metrik evaluasi yang lazim digunakan. Penulis menilai bahwa tinjauan sebelumnya lebih banyak berfokus pada penghitungan buah di kebun atau segmentasi semantik, sehingga belum merangkum penghitungan tanaman secara menyeluruh.

Literatur yang ditinjau mencakup periode 2019 hingga 2023. Pencarian dilakukan dengan kata kunci "crop counting", "crop detection and counting", dan "deep learning in crop counting" pada beberapa basis data dan mesin pencari akademik, antara lain Google Scholar, ScienceDirect, dan IEEE Xplore, kemudian ditambah penelusuran sitasi terhadap karya yang banyak dirujuk. Objek yang dibahas meliputi tangkai gandum (*wheat ears*), bunga jagung (*maize tassels*), buah, bunga, dan daun. Penulis membagi perkembangan penghitungan tanaman menjadi tiga tahap, yaitu penghitungan manual, penghitungan berbasis pengolahan citra tradisional, dan penghitungan berbasis *deep learning*. Kajian ini disusun dalam enam bagian, dengan fokus utama pada penerapan deteksi objek dalam penghitungan tanaman, termasuk pembahasan masalah dan solusinya.

Pada metode tradisional, Liu et al. (2019) memperkirakan jumlah tangkai gandum dengan algoritma K-means yang dimodifikasi berdasarkan fitur warna dan luas sub-area, sedangkan Du et al. (2019) menerapkan segmentasi *superpixel* SLIC sebelum memilih pengklasifikasi dengan akurasi tertinggi. Pada *deep learning*, penulis membedakan tiga kelompok: regresi berbasis *density map*, segmentasi, dan deteksi. TasselNet (Lu et al., 2017) menghitung dari blok citra lokal dan menggabungkan hasilnya menjadi peta penghitungan yang dinormalisasi. TasselNetv2 (Xiong et al., 2019) menambahkan informasi konteks melalui *global average pooling* pada lapisan pertama, sedangkan CSRNet (Li et al., 2018) dipakai pada adegan yang padat. Pada kelompok deteksi, YOLO, Faster R-CNN, dan SSD disebut sebagai algoritma yang paling banyak digunakan. Dari ulasan ini, angka yang dapat dikutip adalah rentang literatur 2019 hingga 2023, tiga kelompok metode *deep learning*, dan enam bagian kajian.

Penulis menyatakan bahwa masalah yang masih perlu diselesaikan meliputi kekurangan *dataset*, kesulitan penghitungan objek kecil, serta oklusi dalam lingkungan yang kompleks. Metode regresi, meskipun mampu mengatasi oklusi dan latar belakang kompleks sampai batas tertentu, umumnya mengabaikan informasi spasial sehingga posisi setiap objek tidak dapat ditentukan, yang membatasi cakupan dan ketepatan penerapannya. Metode berbasis pengolahan citra tradisional bergantung pada fitur yang telah ditetapkan sehingga kemampuan generalisasi dan ketahanannya terbatas, serta rentan terhadap gangguan noise dan latensi yang panjang. Penulis juga menegaskan bahwa akurasi deteksi saja belum cukup untuk penghitungan tanaman, karena kemampuan menangani oklusi dan perubahan kepadatan dinilai lebih penting.
