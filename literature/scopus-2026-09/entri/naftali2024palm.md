# Palm Oil Counter: State-of-the-Art Deep Learning Models for Detection and Counting in Plantations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `naftali2024palm` |
| Judul asli | Palm Oil Counter: State-of-the-Art Deep Learning Models for Detection and Counting in Plantations |
| Penulis | Grady Naftali, Martinus; Hugo, Gregory; Suharjito |
| Tahun | 2024 |
| Venue | IEEE Access |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [naftali2024palm.pdf](../pdf/naftali2024palm.pdf)
- DOI resmi: https://doi.org/10.1109/access.2024.3419835

## Gambaran Umum

Penilaian manual tandan buah segar (TBS) kelapa sawit memerlukan biaya tinggi, memakan waktu, dan cakupannya terbatas; penilaian kematangan yang subjektif juga memicu sengketa antara pemanen dan pembeli. Penelitian ini bertujuan membandingkan sejumlah model deteksi objek, terutama varian YOLO, dan mengusulkan YOLOv8s Depthwise untuk mendeteksi sekaligus menghitung TBS yang masih menempel di pohon secara real time pada perangkat berdaya komputasi rendah.

Data dikumpulkan sendiri di perkebunan kelapa sawit di Provinsi Kalimantan Tengah, Indonesia, berupa 440 video beresolusi 320×640 piksel, 30 frame per detik, dengan durasi 8 detik sampai 1 menit 31 detik. Anotasi memakai CVAT pada lima kelas, yaitu abnormal, ripe, underripe, unripe, dan flower; video yang sama tidak dipakai bersamaan antar-split. Pra-pemrosesan mencakup ekstraksi dan pembersihan frame, anotasi, konversi format YOLOv8 ke COCO, pembagian 0,7/0,2/0,1 untuk latih/validasi/uji dengan distribusi per kelas, serta augmentasi Albumentations (flip, rotasi 90°, kecerahan/kontras, derau Gaussian, pergeseran RGB/HSV, dan crop acak) pada ukuran 640×640. Pelatihan memakai MMYOLO di Google Colaboratory dengan GPU NVIDIA V100; inferensi diuji dengan ONNX Runtime pada GPU NVIDIA T4, dengan learning rate 0,001, weight decay 0,0005, momentum 0,03, dan batch size 16.

YOLOv8s Depthwise mengganti blok konvolusi standar dengan konvolusi terpisah kedalaman (depthwise separable convolution) di seluruh arsitektur, mencakup Conv, C2f menjadi C2f DW, SPPF menjadi SPPF DW, dan head deteksi menjadi detect DW; penulis menghitung pengurangan parameter sebesar 84,589% untuk konvolusi, 50,65% untuk C2f, dan 42,25% untuk head. Deteksi memakai satu lintasan maju YOLO dengan grid, kotak pembatas, dan penekanan non-maksimum (NMS). Penghitungan dilakukan dengan mengakumulasi kotak per kelas jika IoU melebihi ambang tertentu, lalu akurasi diukur dengan MAE dan RMSE antara jumlah prediksi dan jumlah sebenarnya per kelas. Model dikonversi ke ONNX dan dikuantisasi fp16, lalu dipasang pada aplikasi web berbasis Next.js dan onnxruntime-web untuk penghitungan real time melalui kamera perangkat.

YOLOv8s Depthwise mencapai mAP50 0,75, mAP50-95 0,481, MAE 0,164, RMSE 0,4, waktu inferensi 0,027 detik, dan ukuran 21,2 MB sebelum kuantisasi atau 10,6 MB sesudah kuantisasi fp16; pelatihannya selesai dalam 2 jam 18 menit 30 detik. Angka ini dihitung dari kurva presisi-recall pada ambang IoU 0,5 dan 0,5–0,95 yang dirata-ratakan lintas lima kelas, dengan kesalahan hitung dari selisih jumlah prediksi dan ground truth per kelas; pembagian data 0,7/0,2/0,1 dan evaluasi dinyatakan penulis pada fase validasi. Pada dataset yang sama, YOLOv8s mencapai mAP50 0,759 dan mAP50-95 0,5 dengan ukuran 22,3 MB, YOLOv4 mencapai mAP50 0,787 dan mAP50-95 0,513 dengan ukuran 244,3 MB, sedangkan SSD MobileNetV2 mencapai mAP50 0,546 dengan MAE 0,321. Penyetelan hiperparameter memilih optimizer SGD, batch 16, dan learning rate 0,001; kuantisasi fp16 mengurangi ukuran model tanpa mengubah mAP secara berarti (perubahan sekitar 0,001) dan memangkas waktu inferensi, misalnya YOLOv6l dari 0,0632 menjadi 0,0378 detik.

Penulis menyatakan dataset hanya mencakup kondisi di Provinsi Kalimantan Tengah, sehingga perbedaan kondisi lingkungan, spesies sawit, dan praktik pertanian di daerah lain dapat menurunkan kemampuan generalisasi. Penerapan di lapangan juga menghadapi kendala perangkat keras, konektivitas jaringan aplikasi web, serta kebutuhan pembaruan dan pelatihan ulang model secara berkelanjutan agar mengikuti kondisi dan data baru.

