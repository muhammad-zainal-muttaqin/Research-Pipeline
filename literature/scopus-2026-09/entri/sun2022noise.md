# Noise-tolerant RGB-D feature fusion network for outdoor fruit detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2022noise` |
| Judul asli | Noise-tolerant RGB-D feature fusion network for outdoor fruit detection |
| Penulis | Sun, Qixin; Chai, Xiujuan; Zeng, Zhikang; Zhou, Guomin; Sun, Tan |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [sun2022noise.pdf](../pdf/sun2022noise.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107034

## Gambaran Umum

Deteksi buah merupakan dasar bagi estimasi hasil panen, pemetikan otomatis, dan pengelolaan kebun lainnya. Citra RGB hanya memuat informasi dua dimensi. Akibatnya, buah yang tumbuh rapat, saling tumpang tindih, atau tertutup cabang dan daun sulit dibedakan secara akurat. Citra kedalaman dapat memberi jarak antara objek dan sensor, sehingga membantu memisahkan latar depan dan latar belakang. Namun, kualitas citra kedalaman di luar ruangan umumnya rendah, dan hal ini menyulitkan penggabungan fitur *RGB-D*. Penelitian ini mengusulkan *noise-tolerant feature fusion network* (NT-FFN), sebuah jaringan deteksi objek RGB-D ujung-ke-ujung yang dirancang untuk memanfaatkan data multimodal luar ruangan secara tepat dan meningkatkan akurasi deteksi.

Penelitian ini memakai buah jeruk sebagai objek kajian. Penulis membangun sendiri sebuah set data jeruk RGB-D untuk luar ruangan, yang digunakan untuk mengevaluasi jaringan yang diusulkan. Data ini mencakup citra warna dan citra kedalaman dari kebun. Jumlah citra, lokasi kebun yang tepat, dan pembagian data latih dan uji tidak dibahas dalam bagian ini. Model dilatih dengan ukuran *batch* 32, optimizer SGD dengan momentum 0,9, dan 100 iterasi. Citra masukan diubah ukurannya dari 1280 × 720 menjadi 1024 × 1024 setelah augmentasi data, yang meliputi perubahan warna, pemotongan acak, perubahan skala, dan pembalikan. Pada tahap inferensi, kotak kandidat disaring dengan NMS. Kotak yang tumpang tindih dengan IoU lebih besar dari 0,3 atau memiliki skor kepercayaan kurang dari 0,05 dibuang.

Jaringan ini memiliki dua ekstraktor fitur dengan struktur yang sama, masing-masing untuk warna dan kedalaman. Fitur kedua modalitas digabungkan oleh modul fusi berbasis atensi. Modul ini bertujuan menekan derau dari citra kedalaman dan memberi perhatian pada bagian fitur yang penting. Setelah itu, modul prediksi berstruktur piramida menghasilkan prediksi pada beberapa skala, sehingga objek berukuran berbeda dapat terdeteksi. Fungsi kerugian lokalisasi dan kepercayaan dibobot 2:1. Evaluasi memakai presisi, *recall*, AP50, F1-score, dan kecepatan inferensi (FPS). Hasil utama menunjukkan bahwa NT-FFN mencapai AP50 sebesar 95,4% dengan kecepatan real-time. Nilai ini melampaui metode berbasis satu modalitas, strategi fusi multimodal yang umum, dan metode deteksi multimodal mutakhir pada set data jeruk tersebut. Penulis juga menyatakan bahwa NT-FFN memberi hasil deteksi yang baik pada tugas deteksi buah lain, sehingga kemampuan generalisasinya teruji.

Penulis menyebut kualitas citra kedalaman luar ruangan yang buruk sebagai tantangan utama dalam penelitian ini. Kualitas tersebut terkait dengan sifat sensor dan konfigurasi adegan. Karena itu, penggabungan fitur RGB-D harus dirancang agar tidak memasukkan derau kedalaman yang berlebihan. Penulis menilai studi ini baru memberikan kemungkinan dan landasan bagi fusi informasi multimodal dalam deteksi buah di luar ruangan. Kajian ini juga berfokus pada deteksi, dan hasil yang dilaporkan adalah metrik deteksi pada set data jeruk yang dibangun penulis sendiri.
