# Detection of Oil Palm Tree and Loose Fruitlets for Fresh Fruit Bunch's Ready-to-Harvest Prediction via Deep Learning Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `daud2023detection` |
| Judul asli | Detection of Oil Palm Tree and Loose Fruitlets for Fresh Fruit Bunch's Ready-to-Harvest Prediction via Deep Learning Approach |
| Penulis | Daud, M.M.; others |
| Tahun | 2023 |
| Venue | Iaeng International Journal of Computer Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [daud2023detection.pdf](../pdf/daud2023detection.pdf)

## Gambaran Umum

Penelitian ini bertujuan menentukan status panen tandan buah segar secara otomatis dengan menghitung buah lepas di permukaan tanah di sekitar pohon. Latar belakangnya adalah ketergantungan industri sawit Malaysia pada tenaga kerja asing untuk memanen dan mengumpulkan tandan, sementara pekerja harus menilai kematangan secara manual. Penulis memilih buah lepas sebagai petunjuk kematangan karena warna tandan pada pohon tinggi tidak dapat dijadikan acuan yang andal: tandan yang tampak merah belum tentu matang. Pendekatan berbasis tampilan tandan juga terganggu oleh warna yang tidak konsisten antarpohon, antarwilayah, dan antarwaktu pengambilan citra, serta oleh halo daun yang menutup tandan.

Data dikumpulkan di kebun sawit petani kecil di Sg. Pelek, Selangor, Malaysia, pada sesi pagi dan sore. Pohon berukuran sekitar 5 meter dengan jarak antarpohon rata-rata 9 meter. Kamera yang dipakai adalah DJI Osmo Pocket beresolusi 1920×1080 pada 60 fps dengan penstabil tiga sumbu, dipegang tangan dengan kecepatan jalan kaki, berjarak 3–4 meter dari pohon dan pada tinggi sekitar 1,5 meter dari tanah. Anotasi dibuat manual dengan CVAT dalam format YOLO. Set data terdiri atas 2.140 citra pohon (1.498 latih, 642 uji) dan 490 citra buah lepas (343 latih, 147 uji) dengan rasio latih:uji 70:30. Pengujian deteksi memakai 1.000 citra yang diekstrak dari dua video pada 10 fps; video pertama berdurasi sekitar 9 menit 57 detik dan video kedua sekitar 2 menit 4 detik. Klasifikasi status panen diuji pada 185 klip video.

Sistem terdiri atas tiga modul, yaitu akuisisi, analitik, dan pascapengenalan. Modul analitik menjalankan deteksi pohon dengan YOLOv5, pelacakan pohon agar setiap pohon hanya dihitung sekali, pemotongan wilayah minat di sekitar batang dekat tanah, deteksi buah lepas dengan YOLOv4, penghitungan buah, dan klasifikasi status panen. Pelacakan pohon memakai penjumlahan frame berturut-turut dengan ambang t1 dan t2 untuk membedakan pohon baru, pohon yang sudah dilacak, dan derau. Jumlah akhir buah lepas ditetapkan dari frekuensi hitungan tertinggi setelah sejumlah frame pelacakan, dengan contoh n=15 frame. Dua ambang klasifikasi dipakai, yaitu ambang nol (minimal satu buah lepas) dan ambang tiga; teks hasil menyebut ambang tiga sebagai minimal empat buah lepas di sekitar batang.

Metrik deteksi adalah AP pada IoU 50% (AP@.50), sedangkan akurasi klasifikasi dihitung sebagai (TP+TN)/(TP+FP+FN+TN). Deteksi pohon dengan YOLOv5 mencapai mAP@.50 tertinggi 97,79% pada 15.000 epoch (Tabel III), sedangkan YOLOv4 mencapai 88,86%. Deteksi buah lepas dengan YOLOv4 mencapai mAP@.50 85,45% pada 10.000 epoch (Tabel IV), sedangkan YOLOv5 mencapai sekitar 72%. Konsistensi deteksi objek pada pasangan citra dilaporkan 91,13%. Akurasi klasifikasi status panen adalah 90,48% pada ambang nol dan 91,34% pada ambang tiga.

Penulis menyatakan beberapa batasan. Hasil deteksi bergantung pada model dan data latih, sehingga lingkungan baru memerlukan pelatihan ulang. Metode hanya efektif bila sedikitnya 80% buah lepas terlihat dalam cakupan kamera dan ukuran terkecil buah di citra sekurang-kurangnya 25×25 piksel pada resolusi 1920×1080. Gangguan yang disebutkan mencakup pelepah menggantung yang salah terdeteksi sebagai pohon, batang tertutup rumput atau daun, tanah gelap, buah lepas berukuran kecil, batang buram, serta warna buah yang dipengaruhi latar tanah cokelat atau rumput hijau. Penulis menganjurkan penambahan data latih untuk kondisi pencahayaan ekstrem dan susunan pohon yang beragam, serta penggunaan kamera definisi tinggi.

