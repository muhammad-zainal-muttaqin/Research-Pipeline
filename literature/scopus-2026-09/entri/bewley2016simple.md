# Simple online and realtime tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bewley2016simple` |
| Judul asli | Simple online and realtime tracking |
| Penulis | Bewley, Alex; Ge, Zongyuan; Ott, Lionel; Ramos, Fabio; Upcroft, Ben |
| Tahun | 2016 |
| Venue | Proceedings International Conference on Image Processing Icip |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [bewley2016simple.pdf](../pdf/bewley2016simple.pdf)
- DOI resmi: https://doi.org/10.1109/icip.2016.7533003

## Gambaran Umum

Penelitian ini mengajukan SORT (Simple Online and Realtime Tracking), yaitu penjejak multipel objek (multiple object tracking, MOT) yang beroperasi secara daring dan waktu nyata. Permasalahan utamanya adalah asosiasi data, yakni menghubungkan deteksi antarframe. Penulis berpendapat bahwa kualitas deteksi lebih menentukan kinerja penjejak daripada kompleksitas model, sehingga mereka mengabaikan fitur penampilan di luar komponen deteksi serta tidak menangani oklusi jangka pendek maupun panjang secara eksplisit. Pendekatan ini memakai dua teknik klasik, yaitu Kalman filter untuk prediksi gerak dan algoritma Hungarian untuk asosiasi data, dengan tujuan menjadi dasar (baseline) yang sederhana sekaligus akurat untuk aplikasi seperti pelacakan pejalan kaki pada kendaraan otonom.

Data yang dipakai adalah MOT benchmark database yang memuat sebelas sekuens uji dengan gabungan kamera bergerak dan statis; ground truth untuk sekuens uji ditahan oleh server benchmark. Untuk penyesuaian parameter kovarians awal Kalman, IOUmin, dan TLost, penulis memakai pembagian latihan/validasi yang sama seperti pada literatur pembanding. Detektor yang diuji adalah Faster Region CNN (FrRCNN) dengan dua arsitektur, yaitu Zeiler–Fergus (ZF) dan VGG16 yang lebih dalam, dibandingkan dengan detektor aggregate channel filter (ACF). Seluruh model memakai parameter bawaan yang dipelajari pada tantangan PASCAL VOC; hanya deteksi orang dengan probabilitas keluaran di atas 50 persen yang diteruskan ke penjejak.

Mekanisme penjejakannya terdiri atas deteksi, propagasi keadaan, asosiasi, serta pembuatan dan penghapusan identitas lintasan. Keadaan setiap target dinyatakan sebagai vektor [u, v, s, r, u_dot, v_dot, s_dot], dengan u dan v sebagai koordinat piksel pusat, s sebagai luas, dan r sebagai rasio aspek yang dianggap tetap. Perpindahan antarframe didekati dengan model kecepatan konstan linier yang independen terhadap objek lain dan gerak kamera. Saat deteksi diasosiasikan, keadaan diperbarui melalui Kalman filter; bila tidak ada deteksi, keadaan hanya diprediksi tanpa koreksi. Matriks biaya asosiasi dihitung dari jarak intersection-over-union (IoU) antara setiap deteksi dan kotak prediksi dari lintasan yang ada, lalu diselesaikan secara optimal dengan algoritma Hungarian dan ambang batas IoU minimum. Penulis menyatakan jarak IoU secara tidak langsung menangani oklusi jangka pendek karena memberi bobot pada deteksi dengan skala serupa. Lintasan baru dibuat dari deteksi yang tumpang tindihnya di bawah IOUmin, dengan kecepatan nol dan kovarians kecepatan besar, lalu menjalani masa percobaan untuk menahan deteksi palsu. Lintasan dihapus bila tidak terdeteksi selama TLost frame; dalam semua percobaan TLost bernilai 1 karena model kecepatan konstan dipandang buruk untuk dinamika sebenarnya dan karena fokusnya pada asosiasi frame demi frame.

Hasil diukur dengan metrik MOTA, MOTP, false alarms per frame (FAF), mostly tracked (MT), mostly lost (ML), false positives (FP), false negatives (FN), ID switches (ID sw), dan fragmentasi (Frag), dengan true positive didefinisikan sebagai tumpang tindih minimal 50 persen terhadap ground truth. Percobaan penggantian detektor menunjukkan kualitas deteksi berpengaruh besar: pada penjejak yang diusulkan, MOTA naik dari 15,1 dengan detektor ACF menjadi 34,0 dengan FrRCNN(VGG16), atau perbaikan 18,9 persen seperti yang dinyatakan dalam abstrak. Pada evaluasi benchmark, SORT memperoleh MOTA 33,4 dan MOTP 72,1, dengan FAF 1,3 persen, MT 11,7 persen, ML 30,9 persen, FP 7.318, FN 32.615, ID sw 1.001, dan Frag 1.764. Angka MOTA tersebut merupakan yang tertinggi di kalangan penjejak daring dan sebanding dengan NOMT sebesar 33,7 yang lebih kompleks serta memakai frame masa depan. Komponen penjejak berjalan pada 260 Hz pada satu inti prosesor Intel i7 2,5 GHz dengan memori 16 GB, atau lebih dari 20 kali lebih cepat daripada penjejak mutakhir lainnya.

Batasan yang dinyatakan penulis mencakup pengabaian fitur penampilan, oklusi jangka pendek dan jangka panjang, serta pengenalan ulang objek. Karena TLost ditetapkan menjadi 1, objek yang muncul kembali akan diberi identitas baru. Penulis juga menyatakan model kecepatan konstan merupakan prediktor yang buruk untuk dinamika sebenarnya, sehingga penghapusan awal lintasan yang hilang dipakai untuk menjaga efisiensi. Penelitian lanjutan yang diusulkan mencakup pengenalan ulang objek untuk menangani oklusi jangka panjang dan kerangka deteksi-penjejakan yang terikat erat. Penulis tidak menyatakan batasan lain secara eksplisit.

