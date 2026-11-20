# AI on the bog: Monitoring and evaluating cranberry crop risk

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `akiva2021ai` |
| Judul asli | AI on the bog: Monitoring and evaluating cranberry crop risk |
| Penulis | Akiva, Peri; Planche, Benjamin; Roy, Aditi; Dana, Kristin; Oudemans, Peter; Mars, Michael |
| Tahun | 2021 |
| Venue | Proceedings 2021 IEEE Winter Conference on Applications of Computer Vision Wacv 2021 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | other berries |

## Tautan Akses
- PDF: [akiva2021ai.pdf](../pdf/akiva2021ai.pdf)
- DOI resmi: https://doi.org/10.1109/wacv48630.2021.00254

## Gambaran Umum

Kajian ini membahas pemantauan risiko kerusakan akibat panas pada tanaman *cranberry* (kranberi). Penulis berangkat dari kenyataan bahwa sengatan matahari (*sunburn*) dapat menyebabkan kehilangan hasil hingga 30% dari seluruh panen pada satu lahan dalam tahun-tahun tertentu. Kerusakan ini terjadi karena buah yang terpapar langsung sinar matahari dapat mengalami suhu dalam hingga 25 °C di atas suhu kanopi. Petani umumnya mengandalkan penghitungan manual atau data tahun sebelumnya untuk memperkirakan hasil, sedangkan pengelolaan irigasi bergantung pada laporan cuaca yang jarang terbit, kurang memadai, dan sering tidak akurat. Tujuan penelitian ini adalah membangun sistem pemantauan kesehatan kranberi yang berjalan secara *end-to-end* dan mampu memberikan penilaian suhu lebih dari sekadar data historis, sehingga petani dapat mengambil tindakan pencegahan, seperti pengairan, sebelum kerusakan terjadi.

Data yang digunakan berasal dari dua sumber. Pertama, citra video dari lahan yang direkam menggunakan *drone* yang mengarah ke bawah, untuk menghitung buah kranberi yang terpapar matahari dan membentuk peta kepadatan lahan. Kedua, citra langit yang diambil dari kamera berlensa *fish-eye* di darat, yang merekam tutupan awan pada beberapa titik waktu untuk memperkirakan iradiansi matahari. Penulis juga menggunakan data kelembapan dan kecepatan angin. Pengumpulan data dilakukan pada beberapa titik waktu agar sistem dapat dievaluasi terhadap kondisi lapangan yang beragam. Penulis menegaskan bahwa kerangka kerjanya dirancang untuk diterapkan pada jenis tanaman lain melalui *transfer learning*, meskipun hasil yang dilaporkan hanya berasal dari kranberi.

Metode terdiri atas tiga cabang. Cabang pertama melakukan segmentasi dan penghitungan buah yang terpapar matahari menggunakan model *deep learning*, dengan pendekatan yang terinspirasi dari Triple-S Network dan jaringan berbasis titik. Cabang kedua memprediksi tutupan awan dan iradiansi matahari dengan model *weakly supervised* yang mempelajari segmentasi dan estimasi gerak awan secara bersamaan dari urutan citra langit, dengan horizon prediksi 5 hingga 20 menit. Cabang ketiga memperkirakan suhu dalam buah berdasarkan iradiansi yang diprediksi dan kondisi cuaca. Hasil kuantitatif yang dilaporkan meliputi kesalahan *mean absolute percentage error* (MAPE) suhu dalam buah sebesar 0,02%, kesalahan prediksi iradiansi matahari sebesar 8,41% hingga 20,36% MAPE pada horizon 5 hingga 20 menit, nilai *mean intersection over union* (mIoU) untuk segmentasi sebesar 62,54%, dan *mean absolute error* (MAE) penghitungan buah terpapar sebesar 13,46. Angka-angka tersebut menunjukkan bahwa prediksi suhu relatif stabil, sedangkan kesalahan prediksi awan membesar seiring bertambahnya horizon waktu.

Penulis menyimpulkan bahwa sistem ini mampu memberikan umpan balik yang informatif kepada petani. Keluaran berupa peta kepadatan buah terpapar dan prediksi suhu dalam buah memungkinkan petani memusatkan tindakan pada wilayah lahan yang berisiko tinggi dalam waktu dekat. Penulis juga menyebut bahwa pendekatan menghubungkan pengamatan langit dengan kondisi buah di lapangan merupakan langkah pertama yang, sepengetahuan penulis, belum pernah dilakukan sebelumnya untuk pemantauan kesehatan buah. Dengan demikian, sistem ini diposisikan sebagai dasar bagi pertanian presisi yang lebih luas, tidak hanya untuk kranberi.
