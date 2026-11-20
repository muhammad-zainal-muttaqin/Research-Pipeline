# Orchard Yield Estimation using Multi-angle Image Processing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ripa2022orchard` |
| Judul asli | Orchard Yield Estimation using Multi-angle Image Processing |
| Penulis | Ripa, Leon; Arif, Khalid Mahmood |
| Tahun | 2022 |
| Venue | 2022 28th International Conference on Mechatronics and Machine Vision in Practice M2vip 2022 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [ripa2022orchard.pdf](../pdf/ripa2022orchard.pdf)
- DOI resmi: https://doi.org/10.1109/m2vip55626.2022.10041098

## Gambaran Umum

Penelitian ini bertujuan menaksir hasil panen buah kiwi di kebun dengan memanfaatkan citra dari *drone*. Petani kiwi di Selandia Baru belum memiliki solusi panen mekanis, sehingga perkiraan hasil sulit dibuat secara akurat. Perkiraan yang keliru dapat menyebabkan kelebihan atau kekurangan tenaga kerja saat pemetikan. Selain itu, penyebaran virus dan penyakit membuat aktivitas manusia di bawah kanopi perlu dikurangi. Penulis mengusulkan metode yang mendeteksi, melacak, dan menghitung buah kiwi dengan jaringan saraf konvolusional. Metode ini juga diharapkan dapat menunjukkan bagian kebun yang produksinya tinggi atau rendah.

Tanaman yang diamati adalah kiwi emas di kebun Selandia Baru. Citra diambil dengan *hexa-drone* (UAV berenam baling-baling) yang terbang di bawah kanopi kebun. Citra pelatihan berasal dari kebun yang sama, sekitar satu tahun sebelum uji lapangan. Uji lapangan dilakukan pada 7 Mei 2023 dengan kecepatan terbang sekitar 1 meter per 3 sampai 5 detik. Pemrosesan berjalan pada *Nvidia Jetson Nano* dengan model YOLOv7 dan YOLOv7-Tiny, serta algoritma *DeepSORT* untuk pelacakan. Untuk menguji akurasi pencacahan, dipakai video lima detik pada 25 FPS yang dihitung manual dan menghasilkan 341 buah. Evaluasi mAP memakai 10 citra yang memuat 334 buah kiwi.

Model YOLOv7 mencapai mAP 0,898, atau akurasi umum 89,8%. YOLOv7-Tiny mencapai mAP 0,844. Pada setengah baris, hitungan real-time YOLOv7-Tiny menghasilkan 8.782 buah. Nilai aktual adalah 10.407 ± 170, sehingga akurasinya 84,3% dengan variasi 1,93%. Pada 12,5 FPS, YOLOv7-Tiny menghitung 8.220 buah, dengan akurasi 78,98% ± 2,06%. Pada satu baris penuh, hitungan 12,5 FPS sebesar 15.577 dibandingkan nilai aktual 19.123 ± 126. Akurasinya 81,45% ± 0,8%. Penulis menilai hasil ini sebagai keberhasilan untuk sebuah prototipe.

Penulis menyebutkan beberapa batasan. Angin, *drift*, dan hambatan berupa dedaunan atau sulur yang menggantung dapat mengganggu gerak drone dan deteksi. Sinar matahari langsung pada kamera menambah kesalahan. Buah yang letaknya berderet di belakang buah lain tidak terlihat dari sudut kamera depan. Rumput tinggi di lantai kebun membuat sistem tidak berfungsi. Daya baterai Jetson Nano membatasi panjang baris yang dapat dihitung, dan kecepatan terbang yang lambat diperlukan karena FPS rendah. Penulis juga menyebut bahwa model perlu lebih banyak citra buah yang terkena sinar matahari langsung. Ambang *intersection over union* yang ideal, yaitu 0,5, belum tercapai karena model paling akurat pada nilai 0,1.
