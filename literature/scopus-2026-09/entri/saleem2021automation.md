# Automation in Agriculture by Machine and Deep Learning Techniques: A Review of Recent Developments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saleem2021automation` |
| Judul asli | Automation in Agriculture by Machine and Deep Learning Techniques: A Review of Recent Developments |
| Penulis | Saleem, Muhammad Hammad; Potgieter, Johan; Arif, Khalid Mahmood |
| Tahun | 2021 |
| Venue | Precision Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [saleem2021automation.pdf](../pdf/saleem2021automation.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-021-09806-x

## Gambaran Umum

Tinjauan ini membahas otomatisasi pertanian dengan *machine learning* dan *deep learning* yang diterapkan pada robot pertanian. Penulis menyatakan belum ada tinjauan sistematis dalam satu artikel yang mencakup performa sistem robot berbasis ML dan DL untuk operasi pertanian utama, seperti deteksi penyakit tanaman, identifikasi tanaman, pencacahan buah, pengenalan buah, identifikasi gulma, dan klasifikasi tutupan lahan. Tujuan tinjauan ini adalah memetakan kemajuan tersebut selama sekitar satu dekade terakhir dan menunjukkan celah penelitian yang perlu diisi agar otomatisasi pertanian dapat berkembang lebih jauh.

Tinjauan ini tidak menyajikan satu kumpulan data. Cakupannya adalah berbagai studi terdahulu yang menggunakan robot pertanian, seperti lengan robot, robot beroda, dan *unmanned aerial vehicle* (UAV). Komoditas yang dibahas meliputi tanaman seperti apel, anggur, jagung, dan tomat, serta sejumlah sayuran. Sumber citra pada studi-studi tersebut beragam, mulai dari citra daun pada ban berjalan hingga citra yang diambil di lapangan maupun laboratorium. Pembahasan dibagi menjadi tiga bagian utama: algoritma ML tradisional pada robot pertanian, arsitektur DL untuk operasi pertanian, serta kesimpulan dan arah penelitian lanjutan. Penulis juga menyebut metrik evaluasi yang lazim dipakai, yaitu akurasi klasifikasi, *F1-score*, *mean average precision*, dan tingkat deteksi atau kegagalan.

Hasil utama tinjauan menunjukkan bahwa arsitektur DL umumnya mengungguli algoritma ML tradisional. Pada deteksi penyakit tanaman, RCNN mencapai tingkat deteksi 82,51 persen, lebih tinggi daripada *Multi-Layer Perceptron* (64,9 persen) dan *K-nearest Neighbour* (63,76 persen). Pada pembedaan tanaman pokok dan gulma, ResNet-18 mencapai AUC 94,84 persen, sedangkan *Random Forest* (70,16 persen) dan *Support Vector Machine* (60,6 persen) lebih rendah. Pada klasifikasi tutupan lahan, FCN mencapai akurasi 83,9 persen, mengungguli SVM (67,6 persen) dan RF (65,6 persen). Untuk pengenalan dan pemanenan buah, penulis mencatat bahwa SSD pada lengan robot UR3 untuk apel mencapai akurasi deteksi lebih dari 90 persen. Studi pemanenan tomat dengan CNN disebut memperoleh akurasi 91,9 persen. Pada pemanenan kiwi, tingkat keberhasilan panen tercatat 51 persen dan dapat ditingkatkan hingga sekitar 70 persen. Untuk penghitungan kluster anggur dengan citra RGBD, VGG-19 mencapai akurasi tertinggi di antara empat model yang diuji. Penulis tidak merinci setiap angka tersebut ke dalam satu tabel terpadu, sehingga perbandingan antarstudi bergantung pada kondisi percobaan masing-masing.

Penulis menyatakan beberapa batasan. Pertama, tinjauan ini hanya memetakan performa yang dilaporkan studi-studi yang ditelaah, sehingga kondisi eksperimen dan kumpulan data antarstudi belum dibandingkan secara setara. Kedua, untuk sebagian besar tugas pengenalan dan pemanenan buah, penulis menilai akurasi masih perlu ditingkatkan, dan saran yang diajukan terbatas pada pelatihan dengan *transfer learning* serta modifikasi arsitektur DL yang sudah ada. Ketiga, beberapa studi pemanenan menunjukkan siklus kerja yang lebih lambat dibanding manusia, sehingga kecepatan operasi juga menjadi tantangan. Keempat, penulis menekankan bahwa perlu lebih banyak uji terhadap model alternatif, seperti *Faster R-CNN*, RFCN, dan YOLO, untuk tugas pemanenan tertentu. Dengan demikian, kesimpulan tinjauan ini bersifat deskriptif dan belum menjadi perbandingan kuantitatif yang seragam.
