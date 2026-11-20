# Visual SLAM and structure from motion in dynamic environments: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saputra2019visual` |
| Judul asli | Visual SLAM and structure from motion in dynamic environments: A survey |
| Penulis | Saputra, Muhamad Risqi U.; Markham, Andrew; Trigoni, Niki |
| Tahun | 2019 |
| Venue | ACM Computing Surveys |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [saputra2019visual.pdf](../pdf/saputra2019visual.pdf)
- DOI resmi: https://doi.org/10.1145/3177853

## Gambaran Umum

Kajian ini membahas *visual SLAM* dan *Structure from Motion* (SfM) pada lingkungan dinamis. Kedua teknik itu memperkirakan pose kamera dan struktur 3D dari sekumpulan citra. Sebagian besar metode yang ada berangkat dari asumsi bahwa lingkungan bersifat statis. Bila ada objek yang bergerak, akurasi sistem dapat menurun. Penulis menyatakan bahwa tulisan ini adalah survei pertama yang secara khusus membahas teknik visual SLAM dan SfM untuk lingkungan dinamis. Ada tiga masalah yang diidentifikasi. Masalah pertama adalah bagaimana melakukan rekonstruksi yang tangguh. Masalah kedua adalah bagaimana melakukan segmentasi dan pelacakan objek dinamis. Masalah ketiga adalah bagaimana mencapai segmentasi gerak sekaligus rekonstruksi secara bersamaan.

Survei ini ditulis oleh peneliti dari Department of Computer Science, University of Oxford, dan terbit di ACM Computing Surveys, Vol. 51, No. 2, Article 37, Februari 2018, dengan 36 halaman. Kajian ini tidak memuat data eksperimen baru. Isinya adalah pengelompokan pustaka yang sudah ada. Penulis membandingkannya dengan beberapa survei terdahulu, seperti Huang dkk. (1994), Oliensis (2000), Yousif dkk. (2015), Younes dkk. (2016), dan Garcia-Fidalgo dkk. (2015). Menurut penulis, survei-survei itu tidak membahas secara rinci masalah lingkungan dinamis. Pendahuluan juga menyinggung aplikasi seperti navigasi robot, kendaraan tanpa awak, respons darurat, dan realitas tertambah.

Penulis menyusun taksonomi pendekatan pada Bagian 2. Bagian 3 membahas *robust visual SLAM*. Pada pendekatan ini, fitur dinamis dipisahkan dari fitur statis, lalu fitur dinamis diperlakukan sebagai *outlier* dan estimasi pose hanya memakai bagian statis. Bagian 4 membahas segmentasi objek dinamis dan pelacakan 3D. Bagian 5 membahas segmentasi gerak yang dipadukan dengan rekonstruksi, termasuk *Multibody Structure from Motion* (MBSfM). Bagian 6 membahas kelebihan dan kekurangan tiap kelas pendekatan, dirangkum dalam Tabel 1, 2, dan 3. Pendekatan dibagi menjadi berbasis fitur dan berbasis *deep learning*. Penilaian disampaikan secara kualitatif dari sudut pandang praktis dan ketangguhan. Bagian 7 berisi kesimpulan dan arah penelitian lanjutan.

Penulis menyatakan beberapa batasan. Penanganan data yang hilang, berderau, dan *outlier* tetap menjadi tantangan bagi sebagian besar teknik. Teknik statistik dapat mengatasinya lewat pengambilan sampel berulang, tetapi harus mengorbankan akurasi demi biaya komputasi. Banyak teknik juga kesulitan menangani gerak yang merosot dan gerak yang saling bergantung. Teknik *subspace clustering* yang mengizinkan perpotongan antargerak masih terbatas pada data tanpa derau. Implementasi *real-time* juga masih sulit untuk segmentasi objek dinamis dan pelacakan 3D, karena algoritmanya bersifat *offline* dan biaya komputasinya tinggi. Penulis menilai masalah ini harus diselesaikan dulu sebelum teknik tersebut dapat digabungkan dengan visual SLAM standar. Pendekatan *deep learning* membuka perspektif baru karena menjadikan lokalisasi dan rekonstruksi 3D sebagai masalah pembelajaran. Namun, menurut penulis, pendekatan itu masih berada di tahap awal.
