# Oil Palm Fruits Dataset in Plantations for Harvest Estimation Using Digital Census and Smartphone

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `suharjito2025oil` |
| Judul asli | Oil Palm Fruits Dataset in Plantations for Harvest Estimation Using Digital Census and Smartphone |
| Penulis | Suharjito; Naftali, Martinus Grady; Hugo, Gregory; Priyadi, Muhammad Reza Azhar; Asrol, Muhammad; Utama, Ditdit Nugeraha |
| Tahun | 2025 |
| Venue | Scientific Data |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [suharjito2025oil.pdf](../pdf/suharjito2025oil.pdf)
- DOI resmi: https://doi.org/10.1038/s41597-025-05227-x

## Gambaran Umum

Artikel ini menyajikan set data citra tandan buah segar (TBS) kelapa sawit untuk estimasi panen melalui sensus digital. Penghitungan manual dianggap lambat, mahal, dan sulit diperluas, sementara set data yang tersedia untuk kondisi kebun masih terbatas. Penulis membangun set data dari tandan yang belum dipanen agar model deteksi dan penghitungan menghadapi kondisi nyata: buah saling menutupi, berada pada berbagai ketinggian, dan tampil sebagian saja. Set data ini ditujukan untuk pemantauan waktu panen, prediksi hasil, dan pengelolaan sumber daya kebun.

Data dikumpulkan pada tahun 2023 di perkebunan kelapa sawit komersial di Kalimantan Tengah, Indonesia. Perekaman memakai kamera video ponsel dengan 30 bingkai per detik, resolusi 320×640 piksel dengan orientasi potret, dan format MP4. Penulis merekam 440 video berdurasi 8 detik sampai 1 menit 31 detik dengan mengelilingi pohon bertinggi 1–3 meter. Bingkai diekstrak dan diberi anotasi dengan CVAT oleh penilai ahli, lalu diekspor ke format COCO. Anotasi terdiri atas 14.503 kotak dalam lima kelas, yaitu Unripe (7.453), Ripe (2.989), Underripe (1.803), Flower (1.554), dan Abnormal (704).

Pembagian awal memakai rasio 70% latih, 20% validasi, dan 10% uji, lalu augmentation dengan Albumentations menghasilkan 10.207 citra latih, 2.896 citra validasi, dan 1.400 citra uji. Augmentasi mencakup pemotongan acak (probabilitas 80%), pembalikan horizontal dan vertikal (50%), rotasi 90°, penyesuaian kecerahan dan kontras dengan batas 20 (50%), derau Gauss, pergeseran RGB, dan pergeseran HSV (50%, batas 20). Penyeimbangan kelas dilakukan dengan oversampling dan undersampling. Mekanisme yang diuji adalah deteksi objek dengan kotak pembatas per tandan atau bunga, yang kemudian dipakai untuk penghitungan.

Validasi teknis memakai YOLOv8n dan YOLOv8s dengan 100 epoch maksimum, masukan 640×640 RGB, laju pembelajaran 0,01, optimizer SGD bermomentum 0,9, delapan pekerja, dan seed 10; ukuran batch berturut-turut 64 dan 16. Studi ablasi pada YOLOv8s menunjukkan mAP_0.5 naik dari 71,9 menjadi 74,5 dan mAP_0.5:0,95 dari 47,1 menjadi 48,0 setelah augmentasi. YOLOv8s berhenti otomatis pada epoch ke-87 karena tidak ada perbaikan selama 50 epoch. YOLOv8n mencatat mAP_0.5 0,735, mAP_0.5:0,95 0,480, presisi 0,725, recall 0,711, F1 0,718, kecepatan 90 FPS, penggunaan GPU 9,6 GB, dan ukuran model 6 MB. YOLOv8s mencatat masing-masing 0,745, 0,480, 0,738, 0,719, 0,728, 36 FPS, 4,5 GB, dan 21 MB. Cawat penghitungan untuk angka pada validasi teknis ini tidak dinyatakan eksplisit. Prototipe sensus digital berbasis ponsel menampilkan label kelas dan nilai keyakinan secara langsung.

Penulis menyatakan dua batasan penggunaan. Set data hanya berasal dari pohon ber tinggi 1–3 meter sehingga tidak mewakili citra TBS pada pohon lebih tinggi. Karena perekaman memakai ponsel beresolusi terbatas, set data ini paling sesuai untuk aplikasi dengan masukan dari ponsel atau sistem tertanam serupa. Ketimpangan kelas juga tetap ada antara Unripe dan Abnormal, dan augmentasi dibatasi agar model tidak mengalami overfitting pada versi citra yang hanya sedikit berbeda.

