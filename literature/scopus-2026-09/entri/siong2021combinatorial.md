# A Combinatorial RGB and Depth Images CNN-based Model for Oil Palm Fruit Bunch Detection and Heatmap Localisation for a Visual SLAM System

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `siong2021combinatorial` |
| Judul asli | A Combinatorial RGB and Depth Images CNN-based Model for Oil Palm Fruit Bunch Detection and Heatmap Localisation for a Visual SLAM System |
| Penulis | Zheng Siong, Chua; Ibrahim, Mohd Faisal; Huddin, Aqilah Baseri; Mohd Zaman, Mohd Hairi; Hashim, Fazida Hanim |
| Tahun | 2021 |
| Venue | Jurnal Kejuruteraan |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [siong2021combinatorial.pdf](../pdf/siong2021combinatorial.pdf)
- DOI resmi: https://doi.org/10.17576/jkukm-2021-33(4)-34

## Gambaran Umum

Penelitian ini mengatasi pekerjaan panen tandan buah segar (TBS) kelapa sawit yang padat karya dan berisiko ergonomis karena tandan seberat 10–24 kg harus dipotong dan dikumpulkan. Kendaraan otonom di kebun memerlukan modul simultaneous localization and mapping (SLAM) untuk navigasi serta modul pendeteksi tandan lepas di tanah. Modul pendeteksi berfungsi memberi informasi penghindaran tabrakan dan menentukan lokasi tandan agar dapat diambil. Penulis mengusulkan sistem yang menggabungkan deteksi dan lokalisasi tandan lepas dengan visual SLAM.

Data berupa citra tandan lepas yang direkam dengan kamera kedalaman Kinect Xbox 360 secara bersamaan dalam bentuk citra RGB dan citra kedalaman (depth), masing-masing berukuran 640 × 480 piksel dan berformat JPG. Terdapat 394 citra RGB, terdiri atas 222 citra berisi tandan dan 172 citra tanpa tandan, serta 314 citra depth, terdiri atas 172 citra berisi tandan dan 142 citra tanpa tandan; semua diambil dalam kondisi cahaya terang dan gelap. Citra RGB dibagi menjadi 245 data latih, 105 data validasi, dan 44 data uji, sedangkan citra depth dibagi menjadi 189, 81, dan 44. Citra diubah ke 224 × 224 piksel agar sesuai dengan VGG16; citra depth yang awalnya satu kanal diubah menjadi tiga kanal, lalu ditambah augmentasi berupa pembesaran, rotasi, dan perubahan kecerahan. Dua model convolutional neural network (CNN) dibangun dengan meniru struktur VGG16, yaitu tiga belas lapisan konvolusi, lima lapisan pooling, satu lapisan flatten, dropout 0,3, satu dense layer berisi 512 simpul beraktivasi ReLU, dan satu dense layer berisi satu simpul beraktivasi sigmoid. Pelatihan memakai optimizer Adam, fungsi rugi binary cross-entropy, dan metrik accuracy.

Mekanisme deteksi menjalankan model RGB dan model depth secara paralel, lalu menggabungkan keluarannya dengan gerbang OR: jika salah satu model mendeteksi tandan, sistem menyatakan tandan hadir. Lokalisasi memakai heatmap berupa class activation map yang dihasilkan dari peta fitur lapisan konvolusi terakhir; piksel dengan nilai tertinggi dipilih sebagai pusat tandan. Koordinat heatmap berukuran 32 × 32 piksel dikonversi ke posisi pada citra depth, lalu diterjemahkan ke peta grid occupancy SLAM menggunakan sudut pandang horizontal kamera 57°, posisi kamera dari data odometri RTAB-Map, jarak tandan dari data depth, dan orientasi kendaraan. Pengujian gabungan dilakukan di simulator Gazebo dengan robot Turtlebot 2, paket RTAB-Map, model tiga dimensi tandan yang dibuat dengan Blender, serta empat kompartemen dengan tingkat kesulitan berbeda.

Hasil menunjukkan rugi validasi terendah sebesar 0,1029 untuk model RGB dan 0,0378 untuk model depth pada epoch ke-72. Pengujian memakai 44 citra, terdiri atas 22 citra berisi tandan dan 22 citra tanpa tandan, dengan ambang prediksi 0,5. Model RGB mencapai true positive rate (TPR) 0,773 dan false positive rate (FPR) 0,000; model depth mencapai TPR 0,864 dan FPR 0,045; model gabungan mencapai TPR 1,000 dan FPR 0,000. Model RGB gagal mendeteksi 5 dari 22 citra tandan dalam kondisi gelap total, sedangkan model depth gagal pada 3 citra karena jarak tandan tidak dapat dibedakan dari latar. TPR dihitung sebagai TP/(TP+FN) dan FPR sebagai FP/(FP+TN) dari matriks konfusi. Di simulasi, peta tiga dimensi dan peta grid dua dimensi berhasil menandai lokasi tandan sebagai rintangan dan menghitung jumlahnya.

Batasan penulis: model perlu dilatih ulang dengan tandan yang bervariasi dalam ukuran, bentuk, latar, dan kondisi cahaya agar dapat dipakai di berbagai lingkungan perkebunan; algoritma deteksi banyak tandan (multi-bunch) belum tersedia; pengujian lapangan nyata belum dilakukan karena validasi memakai simulator.
