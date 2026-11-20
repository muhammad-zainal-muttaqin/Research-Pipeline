# Eggplant Detection and Counting Across the Entire Greenhouse Using Deep Learning and Motion Parallax

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ishizuka2024eggplant` |
| Judul asli | Eggplant Detection and Counting Across the Entire Greenhouse Using Deep Learning and Motion Parallax |
| Penulis | Ishizuka, Tatsuya; Sasaki, Yusuke; Hamada, Takeo; Shimazaki-Kishi, Yuki; Koshizuka, Noboru |
| Tahun | 2024 |
| Venue | 10th IEEE International Smart Cities Conference Smart Cities Revolution for Mankind Isc2 2024 Proceedings |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [ishizuka2024eggplant.pdf](../pdf/ishizuka2024eggplant.pdf)
- DOI resmi: https://doi.org/10.1109/isc260477.2024.11004199

## Gambaran Umum

Studi ini mengatasi penghitungan buah di seluruh rumah kaca, bukan hanya pada bagian yang terekam. Metode sebelumnya menghitung setiap buah yang terlihat dalam citra sehingga buah pada barisan (ridge) latar belakang ikut terhitung dan jumlah total menjadi berlebih. Penulis menghitung jumlah terong per barisan lalu menjumlahkannya untuk seluruh rumah kaca. Kamera RGB dipasang pada troli yang berjalan dengan kecepatan tetap di lorong antarbarisan. Pemisah buah barisan depan dan belakang memakai prinsip paralaks gerak, yakni benda yang lebih dekat bergerak lebih cepat dalam citra daripada benda yang lebih jauh.

Data berasal dari rumah kaca nyata di Prefektur Kanagawa, Jepang, pada 16 dan 23 Maret 2023, keduanya siang hari dan pada barisan yang sama. Kamera iPhone 13 merekam video 1080p pada 30 FPS, dipasang dengan penstabil pada troli yang bergerak sekitar 0,4 m/s. Dari dua perekaman itu diambil secara acak potongan 10 detik, lalu 596 frame diberi anotasi dengan perangkat lunak FastLabel. Satu kumpulan data dipakai untuk menyetel hyperparameter dan kumpulan lainnya untuk menghitung metrik. Jumlah buah sebenarnya pada barisan dihitung manual dari lorong dengan memisahkan daun dan memakai penghitung mekanis. Perekaman seluruh barisan memakan waktu 36 detik.

Alur pemrosesan terdiri dari deteksi dengan YOLOv5, pelacakan dengan SORT, dan penyaringan berdasarkan paralaks gerak. Model YOLOv5 dilatih dari 180 citra terong yang berasal dari internet dan rumah kaca nyata, lalu ditambah augmentasi kecerahan menjadi 360 citra. Pengujian deteksi pada 10 citra uji menghasilkan mAP@50 sebesar 0,75. Penulis memilih SORT karena buah terong sulit dibedakan hanya dari penampilan, sehingga pendekatan berbasis penampilan pada DeepSORT kurang sesuai; pada data ini SORT juga mengungguli ByteTrack. Kecepatan rata-rata setiap buah dihitung dari perpindahan titik pusat kotak antara frame saat buah terdeteksi, lalu buah dengan kecepatan di bawah ambang dianggap berasal dari barisan belakang dan dibuang. Ambang ditetapkan 21 piksel perpindahan rata-rata per frame setelah disetel pada sebagian data kebenaran. Seluruh pemrosesan dijalankan di Google Colaboratory dengan GPU NVIDIA Tesla T4.

Hasil dinyatakan dengan metrik pelacakan IDP, IDR, dan IDF1, serta perbandingan jumlah buah terhadap anotasi dan hitungan manual. Metode penulis mencatat IDP 0,683, IDR 0,741, dan IDF1 0,711, dibandingkan SORT 0,462, 0,756, 0,574 serta ByteTrack 0,410, 0,553, 0,471. Pada potongan 10 detik, anotasi berisi 88 buah; metode penulis memprediksi 85 buah dengan galat −0,034, sedangkan SORT memprediksi 153 dengan galat 0,739 dan ByteTrack 138 dengan galat 0,568. Untuk barisan penuh, hitungan manual menemukan 346 buah, sementara 88 buah yang terlihat dalam 10 detik dikalikan 3,6 menjadi perkiraan 317 buah yang terlihat dalam video penuh, atau sekitar 8% lebih rendah dari jumlah sebenarnya.

Penulis menyatakan dua keterbatasan. Data evaluasi berasal dari hanya dua hari dengan sekitar 600 citra, sehingga ketahanan terhadap perubahan pencahayaan, misalnya cuaca berawan, belum diuji memadai. Selain itu, jumlah buah yang terlihat dalam video sekitar 8% lebih rendah daripada jumlah sebenarnya karena tertutup daun dan karena kamera tetap memiliki titik buta. Penulis menyatakan bahwa penggunaan metode ini untuk memperkirakan jumlah sebenarnya memerlukan faktor koreksi tetap yang harus ditentukan melalui percobaan lanjutan.
