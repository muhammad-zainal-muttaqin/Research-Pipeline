# Oil palm unstripped bunch detector using modified faster regional convolutional neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `aji2022oil` |
| Judul asli | Oil palm unstripped bunch detector using modified faster regional convolutional neural network |
| Penulis | Aji, Wahyu Sapto; Bin Ghazali, Kamarul Hawari; Akbar, Son Ali |
| Tahun | 2022 |
| Venue | Iaes International Journal of Artificial Intelligence |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [aji2022oil.pdf](../pdf/aji2022oil.pdf)
- DOI resmi: https://doi.org/10.11591/ijai.v11.i1.pp189-200

## Gambaran Umum

Penelitian ini mengatasi kehilangan minyak sawit di pabrik akibat tandan buah yang masih menyisakan buah belum terlepas (unstripped bunch, USB). Di Malaysia, kerugian akibat USB diperkirakan rata-rata 0,05% dan dapat mencapai 40% apabila tandan tidak diproses dengan benar. Pemantauan USB selama ini dilakukan secara manual dan sering diabaikan karena memakan tenaga kerja. Penulis mengusulkan sistem deteksi otomatis sebagai langkah awal penghitungan USB.

Data berupa 500 citra kamera pengawas yang dipasang di atas konveyor buang pabrik minyak sawit PT Sawit Arum Madani di Blitar, Indonesia, pada Mei 2019. Citra dibagi menjadi 460 (92%) untuk latih dan 40 (8%) untuk uji, dengan dua kelas, yaitu tandan kosong (empty fruit bunch, EFB; label 255) dan USB (label 245), yang diberi anotasi memakai LabelImg. Penulis melatih detektor Faster R-CNN dua tahap dengan ekstraktor fitur VGG16, lalu membandingkan konfigurasi VGG16 original dan VGG16 termodifikasi. Perangkat lunak yang dipakai mencakup Anaconda3, Python 3.6.8, Keras 2.2.4, dan TensorFlow 1.14.0; perangkat kerasnya mencakup Intel Core i-7, RAM 8 GB, dan kartu grafis Nvidia RTX2080.

Mekanisme deteksi memakai Faster R-CNN yang terdiri atas jaringan ekstraksi fitur, region proposal network (RPN) untuk menghasilkan usulan objek, dan jaringan deteksi untuk memprediksi kelas. Modifikasi yang diusulkan mencakup tiga perubahan: pengecilan ukuran citra masukan dari 600 menjadi 300 piksel pada sisi terpendek untuk mempercepat inferensi, augmentasi Gaussian high pass filter (GHPF) untuk menajamkan fitur berfrekuensi tinggi yang membedakan USB (pola piksel membentuk lingkaran) dari EFB (pola piksel membentuk garis), dan penambahan lapisan batch normalization pada VGG16. VGG16 hasil modifikasi memiliki 136.705.400 parameter, dengan 136.696.952 parameter dapat dilatih dan 8.448 parameter tidak dapat dilatih.

Pada pengujian validasi, mAP detektor dengan VGG16 original sebesar 0,728, sedangkan detektor dengan VGG16 termodifikasi sebesar 0,782, atau naik 7,42% (selisih 0,054). Kecepatan inferensi meningkat dari 1,85 fps menjadi 3,7 fps, yaitu 100% lebih cepat. Selama pelatihan, sistem termodifikasi 58,9% lebih cepat, total loss lebih kecil 43,4% (0,103 berbanding 0,203), akurasi kelas terbaik 98% berbanding 93%, tetapi tumpang tindih kotak pembatas (bounding box) 23,91% lebih kecil. Metrik mAP dihitung sebagai rata-rata average precision (AP) per kelas menurut persamaan dalam naskah, sedangkan kecepatan dinyatakan dalam frame per detik (fps) yang diturunkan dari waktu deteksi per citra.

Batasan penulis tidak dinyatakan.
