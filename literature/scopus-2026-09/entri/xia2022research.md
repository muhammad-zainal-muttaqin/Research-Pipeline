# Research on Fruit Counting of Xanthoceras Sorbifolium Bunge Based on Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xia2022research` |
| Judul asli | Research on Fruit Counting of Xanthoceras Sorbifolium Bunge Based on Deep Learning |
| Penulis | Xia, Geng; Dan, Jiang; Jinyu, Hao; Jiming, Hu; Xiaoyong, Sun |
| Tahun | 2022 |
| Venue | 2022 7th International Conference on Image Vision and Computing Icivc 2022 |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [xia2022research.pdf](../pdf/xia2022research.pdf)
- DOI resmi: https://doi.org/10.1109/icivc55077.2022.9886298

## Gambaran Umum

Penelitian ini bertujuan menghitung buah *Xanthoceras sorbifolium* Bunge secara otomatis dengan pembelajaran mendalam. Tanaman ini merupakan tanaman kayu penghasil minyak yang penting di Tiongkok. Perkiraan hasil panen selama ini bergantung pada penghitungan manual. Cara ini menimbulkan data yang terlewat, penghitungan ganda, dan beban kerja yang berat. Warna buah yang mirip dengan daun juga menyulitkan deteksi di lapangan. Penulis menyatakan belum ada penelitian pencacahan otomatis untuk tanaman ini, baik di dalam maupun di luar negeri.

Data dikumpulkan di pangkalan percobaan di Linzi, Zibo, Provinsi Shandong, pada 27 Mei sampai 18 Juni 2020. Sensornya adalah kamera 1080p pada drone DJI Mavic Mini yang merekam video dalam 19 kali penerbangan. Sebanyak 117 pohon direkam dalam tiga baris, masing-masing 39 pohon. Jarak antarpohon 3 meter dan jarak antarbaris 2 meter. Penerbangan memakai mode terbang samping, terbang vertikal, dan terbang mengelilingi tanaman. Dataset A berisi 154 buah untuk uji hitung. Dataset B dan C dibuat dengan dua kali peningkatan kontras memakai OpenCV, dan pembagian data latih, validasi, dan uji memakai rasio 7:2:1. Sebanyak 76 citra dari ponsel dipakai sebagai uji tambahan.

Penulis membandingkan SSD, YOLOv2, YOLOv2-tiny, YOLOv3, YOLOv3-tiny, YOLOv4, YOLOv5s, dan YOLOv5x. Metrik deteksi yang dipakai adalah *Intersection over Union* (IOU), presisi, *recall*, dan *average precision*. Nilai IOU tertinggi 98,84 persen dicapai YOLOv3, sedangkan SSD hanya 69,55 persen. Untuk penghitungan, YOLOv3-tiny paling akurat dengan 98,05 persen, yaitu 151 dari 154 buah. YOLOv3 menyusul dengan 97,40 persen, sedangkan YOLOv2 hanya 81,17 persen. Peningkatan kontras terbukti menaikkan akurasi hitung. Pelatihan dengan campuran dataset buah yang mirip warna dan bentuk juga membantu. Hasil terbaik diperoleh masing-masing dengan terbang samping dan terbang vertikal. Pada citra ponsel, model YOLOv3-tiny mencapai akurasi hitung 83 persen di bawah pengaruh cahaya, alat, dan lingkungan yang berbeda.

Penulis menyatakan bahwa pengenalan dan penghitungan buah yang hampir tertutup belum diteliti dan akan dikaji pada penelitian mendatang. Penulis juga menyatakan bahwa peningkatan kontras hanya efektif bila dilakukan secukupnya, karena kontras yang terlalu besar menurunkan akurasi deteksi. Angka 83 persen pada citra ponsel tercatat lebih rendah daripada 98,05 persen pada citra UAV. Penulis menilai metode ini mengurangi kesalahan dan beban kerja dibanding penghitungan manual, tetapi belum mengukur perbedaannya secara langsung.
