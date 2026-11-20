# Tomato segmentation and localization method based on RGB-D camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `malik2019tomato` |
| Judul asli | Tomato segmentation and localization method based on RGB-D camera |
| Penulis | Malik, M.H.; others |
| Tahun | 2019 |
| Venue | International Agricultural Engineering Journal |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [malik2019tomato.pdf](../pdf/malik2019tomato.pdf)

## Gambaran Umum

Kajian ini (malik2019tomato) menguji metode lokalisasi buah tomat merah di rumah kaca memakai kamera RGB-D Kinect V2. Citra warna dipakai untuk memisahkan buah dari latar, lalu data kedalaman dipakai untuk menempatkan tiap buah dalam ruang 3D. Galat yang dilaporkan adalah galat jarak kedalaman rata-rata 1,2 cm (galat relatif 1,4%) dan galat jarak tanah rata-rata 1,9 cm (galat relatif 4%), pada 29 buah dari 18 pasang citra dengan jarak kamera 0,58 sampai 1,50 m.

Di rumah kaca, penghitungan dan pengukuran buah tomat dilakukan secara manual. Kajian ini mengusulkan kamera RGB-D berbiaya rendah untuk menggantikan sebagian pekerjaan itu. Kajian ini tidak membandingkan metodenya dengan pendekatan lain, dan tidak menguji dengan kebun atau jumlah buah yang besar.

Warna merah dipakai untuk menyaring piksel buah. Setiap piksel buah kemudian dipetakan ke titik kedalaman dari sensor sehingga membentuk point cloud 3D per buah. Dari point cloud itu diperoleh jarak kedalaman dan jarak ke tanah.

Tahap pertama mengubah citra RGB ke ruang warna HSV. Ambang pada kanal H, S, dan V digabung dengan operasi morfologi untuk menghasilkan citra biner, lalu tomat merah diekstraksi dari citra itu. Tahap kedua memakai gradien dan watershed. Watershed pertama menghasilkan over-segmentation, sehingga morfologi dipakai lagi untuk memperbaiki area tiap buah. Area yang sudah diperbaiki dipetakan ke point cloud, dan outlier disaring. Pemrosesan point cloud memakan sekitar 0,2 detik per buah.

Pengukuran dilakukan pada 18 pasang citra RGB dan kedalaman yang berisi total 29 buah. Jarak kedalaman dan jarak tanah diukur dengan pita baja, dan sudut kamera juga diukur. Galat dihitung terhadap pengukuran itu. Tabel 1 memuat galat kedalaman dan Tabel 2 memuat galat jarak tanah, masing-masing untuk 29 buah. Kajian menyatakan bahwa metode mengenali dan melokalisasi tiap buah merah secara terpisah. Kajian tidak melaporkan ketepatan hitungan buah, presisi, atau recall.

Dari sisi rekayasa, sensor RGB-D murah sudah cukup untuk mengukur jarak buah di rumah kaca dalam rentang 0,58 sampai 1,50 m. Galat sekitar 1 sampai 2 cm relatif kecil untuk pengukuran tersebut. Keterbatasannya besar: sampel hanya 29 buah, satu jenis tanaman, satu lingkungan, dan satu rentang jarak. Kajian ini tidak menguji oklusi berat, pencahayaan lapangan, atau buah yang tertutup pelepah. Secara konseptual, karena tidak ada metrik hitungan, kajian ini tidak bisa dipakai sebagai bukti bahwa metode ini menghitung buah dengan benar.
