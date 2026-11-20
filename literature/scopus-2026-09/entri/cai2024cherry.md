# Cherry Tomato Detection for Harvesting Using Multimodal Perception and an Improved YOLOv7-Tiny Neural Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cai2024cherry` |
| Judul asli | Cherry Tomato Detection for Harvesting Using Multimodal Perception and an Improved YOLOv7-Tiny Neural Network |
| Penulis | Cai, Yingqi; Cui, Bo; Deng, Hong; Zeng, Zhi; Wang, Qicong; Lu, Dajiang; Cui, Yukang; Tian, Yibin |
| Tahun | 2024 |
| Venue | Agronomy |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [cai2024cherry.pdf](../pdf/cai2024cherry.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy14102320

## Gambaran Umum

Penelitian ini mengatasi kesulitan mendeteksi tomat ceri untuk pemanenan robotik di lingkungan rumah kaca. Metode sebelumnya terutama bergantung pada citra warna, sehingga kurang tangguh terhadap perubahan pencahayaan yang tajam, latar yang kompleks, dan oklusi acak pada tanaman. Penulis juga mencatat bahwa model berbasis warna memerlukan perangkat keras grafis berkinerja tinggi dan kurang memanfaatkan informasi kedalaman, padahal jarak dapat mengurangi ambiguitas akibat buah yang sebagian tertutup buah tetangga. Tujuan penelitian ini adalah menghasilkan deteksi dan pelokalan buah secara real time serta akurat di fasilitas budidaya komersial.

Data dikumpulkan di sebuah rumah kaca komersial selama empat bulan (April–Juli) agar mencakup berbagai kondisi panen, menghasilkan 799 pasangan citra RGB-D dan 6.312 label hasil anotasi ulang. Dataset dibagi dengan rasio 4 banding 1 menjadi 639 citra latih dan 160 citra uji. Sensor RGB-D (Microsoft Kinect DK atau Litemaze TOF30) dipasang dalam konfigurasi eye-in-hand pada lengan robot kolaboratif Aubo i5 di atas platform kendaraan darat otomatis; komputasi memakai Nvidia Jetson TX1 dengan total biaya perangkat keras sekitar USD 28.000. Karena buah berukuran kecil, perbedaan kedalamannya sangat kecil, sehingga penulis mengubah peta kedalaman menjadi peta sudut vektor normal awan titik lalu menggabungkannya dengan kanal warna ruang Lab sebagai masukan jaringan berempat kanal.

Mekanisme deteksi memakai YOLOv7-tiny-CTD, yaitu modifikasi dari YOLOv7-tiny. Region of interest (ROI) dipisahkan lebih dulu dengan ambang batas pada kanal Lab dan kanal kedalaman (30–100 cm), setelah itu patch tanpa buah dibuang. Empat perubahan diterapkan pada jaringan: mengganti masukan citra warna dengan citra empat kanal, menghapus lapisan keluaran "Objectness" karena hanya ada satu kelas target, memperkenalkan metode "Classness" baru yang memakai persentil kedalaman (Zp) di dalam kotak prediksi, dan mengganti NMS dengan metode hibrida CWD-NMS yang menggabungkan CIOU NMS dan Weighted NMS. Peta sudut vektor normal menandai buah kecil, jauh, atau sebagian tertutup, sementara umpan balik sensor gaya yang dibatasi 10 N dipakai untuk menilai keberhasilan cengkeraman dan mencegah memar pada buah.

Pada perbandingan dengan masukan RGB-D yang sama, YOLOv7-tiny-CTD mencapai mAP 94,9%, recall 96,1%, dan akurasi 95,7%; angka ini mengungguli YOLOv7-tiny (92,8%, 91,6%, 91,8%), YOLOv5-s, Faster R-CNN, dan SSDLite. Peningkatannya berturut-turut sebesar 2,1%, 4,9%, dan 4,2% poin, dengan kecepatan sekitar 26 frame per detik di Jetson TX1. Penggunaan RGB-D meningkatkan kinerja semua model yang dibandingkan. Uji panen dalam lima percobaan, masing-masing 80 akuisisi citra dengan total 400 percobaan, menghasilkan tingkat keberhasilan rata-rata 83,5% dengan dua kali percobaan; tingkat keberhasilan dihitung sebagai jumlah panen berhasil setelah dua percobaan dibagi jumlah buah yang dicoba dipanen. Seluruh angka tersebut berasal dari Tabel 3 dan Tabel 4 naskah.

Penulis menyatakan beberapa keterbatasan. Robot memanen satu buah setiap kali dengan pergerakan lengan yang lambat, sehingga efisiensi sistem keseluruhan rendah; buah yang tertutup daun juga diabaikan. Meskipun akurasi deteksi mencapai sekitar 95%, tingkat keberhasilan panen sekitar 10% lebih rendah; penulis menilai keterbatasan ini lebih banyak berada pada sisi perangkat keras, bukan pada deteksi. End effector yang lebih rumit dianggap terlalu mahal dan kompleks untuk pemanfaatan praktis. Penulis mengusulkan pengembangan end effector baru untuk panen tunggal maupun tandan, deteksi tandan pada jaringan, penambahan sensor sentuh pada ujung jari, dan sensor multispektral portabel untuk menilai kematangan buah sebelum dipanen.
