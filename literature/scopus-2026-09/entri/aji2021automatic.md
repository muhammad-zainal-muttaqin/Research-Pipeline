# Automatic Oil Palm Unstripped Bunch (USB) Counting System based on Faster RCNN and Object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `aji2021automatic` |
| Judul asli | Automatic Oil Palm Unstripped Bunch (USB) Counting System based on Faster RCNN and Object Tracking |
| Penulis | Aji, Wahyu Sapto; Hawari bin Ghazali, Kamarul; Akbar, Son Ali |
| Tahun | 2021 |
| Venue | Proceedings 2nd International Conference on Computer Science and Engineering the Effects of the Digital World After Pandemic Edwap Ic2se 2021 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [aji2021automatic.pdf](../pdf/aji2021automatic.pdf)
- DOI resmi: https://doi.org/10.1109/ic2se52832.2021.9792068

## Gambaran Umum

Penelitian ini bertujuan menghitung secara otomatis tandan tak terkelupas (Unstripped Bunch, USB) di pabrik pengolahan kelapa sawit. USB adalah tandan kosong (Empty Fruit Bunch, EFB) yang masih menyisakan buah karena proses sterilisasi dan pemisahan buah tidak sempurna. Jumlah USB dipakai penulis sebagai indikator efisiensi pabrik; kehilangan akibat USB dilaporkan sekitar 0,05% per tandan di Malaysia, 2,2% dalam satu studi di Indonesia, dan dapat mencapai 40% per tandan pada penanganan yang buruk. Penghitungan USB saat ini masih manual. Penulis menyebut penutupan sebagian, tumpang tindih, dan perbedaan sudut pandang sebagai kendala bagi teknik pengolahan citra konvensional, serta penghitungan ganda sebagai masalah tersendiri pada konveyor.

Citra berasal dari kamera pengawas yang dipasang di atas konveyor buang PT Sawit Arum Madani, pabrik kelapa sawit di Blitar, Indonesia, pada Mei 2019. Dataset berisi 500 citra yang diberi anotasi dengan LabelImg untuk lima kelas, yaitu satu buah, dua buah, tiga buah, empat buah, dan tandan. Sebanyak 460 citra (92%) dipakai sebagai data latih dan 40 citra (8%) sebagai data uji. Penulis mendefinisikan sebuah tandan sebagai USB apabila kotak buah berada di dalam kotak tandan; definisi ini dipilih karena tiap pabrik memiliki batasan USB yang berbeda, mulai dari satu buah hingga lebih dari dua puluh buah yang masih menempel.

Sistem terdiri dari dua bagian. Pendeteksi memakai Faster R-CNN yang menghasilkan kelas dan kotak pembatas; kotak pembatas dipakai untuk menghitung titik pusat tandan dan menentukan apakah USB pada frame saat ini merupakan objek baru atau objek yang sama dengan frame sebelumnya. Pelacak memakai jarak Euclidean antara titik pusat objek pada frame sebelumnya dan pusat objek pada frame berikutnya. Apabila jarak melebihi ambang tertentu, objek dianggap sebagai USB baru; asumsinya adalah titik pusat objek yang sama tidak berubah jauh antarframe. Pendekatan ini dimaksudkan mengurangi penghitungan ganda.

Pendeteksi diuji pada sepuluh citra untuk setiap kelas, menghasilkan akurasi rata-rata 79,6% untuk satu buah, 70% untuk dua buah, 84,5% untuk tiga buah, 84,9% untuk empat buah, dan 95% untuk tandan, dengan rata-rata keseluruhan 82,8%. Prototipe penghitung diuji pada tiga berkas video berdurasi lima menit dengan jumlah USB dan EFB berbeda yang dihitung manual. Untuk gabungan USB dan EFB, hasil penghitungan manual terhadap prototipe berturut-turut adalah 78 terhadap 63 (80%), 90 terhadap 60 (66,7%), dan 95 terhadap 81 (85,5%), dengan rata-rata 77%. Untuk USB saja, hasilnya 75 terhadap 58 (77,3%), 81 terhadap 50 (61,7%), dan 83 terhadap 63 (75,9%), dengan rata-rata 71,5%.

Penulis tidak memuat bagian batasan tersendiri. Kendala yang dinyatakan dalam teks mencakup penutupan sebagian, tumpang tindih, perbedaan sudut pandang, dan penghitungan ganda pada konveyor. Penulis tidak merinci nilai ambang jarak Euclidean, tidak mendefinisikan secara eksplisit rumus akurasi deteksi, dan tidak melaporkan interval kepercayaan atau uji statistik untuk perbedaan antarvideo.
