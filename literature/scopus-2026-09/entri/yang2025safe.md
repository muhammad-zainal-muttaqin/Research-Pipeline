# Towards Safe and Efficient Through-the-Canopy Autonomous Fruit Counting with UAVs

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025safe` |
| Judul asli | Towards Safe and Efficient Through-the-Canopy Autonomous Fruit Counting with UAVs |
| Penulis | Yang, Teaya; Ibrahimov, Roman; Mueller, Mark W. |
| Tahun | 2025 |
| Venue | Proceedings IEEE International Conference on Robotics and Automation |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [yang2025safe.pdf](../pdf/yang2025safe.pdf)
- DOI resmi: https://doi.org/10.1109/icra55743.2025.11127839

## Gambaran Umum

Studi ini membangun sistem udara otonom untuk menghitung buah dengan aman dan efisien di dalam kanopi (through-the-canopy). Penerbangan di dalam kanopi mengurangi oklusi daun dan ranting, tetapi lingkungannya lebih kompleks dan padat daripada penerbangan di atas kanopi. Penulis menyatakan bahwa jalur penerbangan sulit disetel karena tata letak kebun, kerapatan kanopi, dan variasi tanaman. Tujuan sistem ini adalah menggabungkan simulasi berfidelitas tinggi untuk perencanaan jalur global, tumpukan otonomi berbiaya rendah untuk navigasi dan pengambilan data di tingkat kanopi, serta alur deteksi dan penghitungan buah dari citra RGB.

Data dan metode simulasi memakai kerangka pemodelan tanaman Helios 3D dengan plug-in Weber-Penn. Model mencakup jeruk, kenari, almond, dan apel, dengan parameter antara lain tinggi batang, jarak tanam, dan jari-jari buah. Batang, ranting, daun, dan buah dibangun sebagai mesh segitiga; setiap pohon dan setiap buah memperoleh ID. Visibilitas buah dihitung dengan frustum culling, lalu pancaran sinar dari kamera ke titik pusat buah diuji terhadap segitiga sekitar memakai algoritme Möller–Trumbore. Buah dinyatakan terlihat bila tidak ada persilangan, dan ID buah beserta ID pohon disimpan dalam multiset. Simulasi perbandingan memakai 10 pohon kenari dalam blok 10 m × 5 m dengan pola lawn-mower; simulasi optimasi ketinggian memakai blok 7,6 m × 7,3 m, ketinggian 1–8 m, satu kamera depan atau dua kamera samping, dan dirata-ratakan atas 10 blok yang dibangkitkan.

Sistem otonomi memakai kamera RealSense D455 untuk kedalaman dan citra stereo, pengontrol penerbangan Pixracer R15, papan komputasi Qualcomm RB5, dan kamera IDS untuk citra RGB. Estimasi keadaan memakai OpenVINS berbasis Multi-State Constraint Kalman Filter dengan data IMU 400 Hz dan citra stereo 15 Hz untuk memperkirakan posisi dan kecepatan 6 derajat kebebasan. Penghindaran rintangan memakai perencana lokal RAPPIDS yang berjalan pada citra kedalaman 15 Hz, menguji lintasan minimum-jerk terhadap batas masukan, batas kecepatan, dan tabrakan. Ruang bebas dibagi menjadi piramida persegi panjang; bila tidak ditemukan lintasan layak, kendaraan mengikuti lintasan sebelumnya. Estimasi dan perencanaan lokal bergantung pada kamera kedalaman sehingga tidak memerlukan GPS.

Alur penghitungan buah terdiri dari deteksi dengan YOLOv8, pelacakan dengan ByteTrack, rekonstruksi tiga dimensi dengan COLMAP, dan pengelompokan titik dengan pengelompokan spasial berbasis kepadatan untuk menghasilkan jumlah akhir. Buah dipakai sebagai fitur dalam structure from motion, dan ByteTrack menggantikan algoritme Hungarian pada metode sebelumnya karena lebih tahan terhadap deteksi berkepercayaan rendah. YOLOv8 disetel ulang dengan 100 citra berlabel manual dari buah sasaran yang diambil dalam kondisi cahaya baik; pemisahan data latih dan uji tidak dinyatakan. Tanpa penyetelan ulang, model mendeteksi 72,7% kemunculan buah dengan kepercayaan rata-rata 39,6%, dan hanya 52,4% yang diklasifikasikan benar sebagai jeruk. Setelah penyetelan ulang, model mendeteksi 100% buah dengan kepercayaan rata-rata 79,6% dan mengklasifikasikan semuanya sebagai jeruk. Pada contoh pohon jeruk dengan 12 buah, rekonstruksi menghasilkan 33 titik tiga dimensi yang dikelompokkan menjadi 12 klaster.

Angka simulasi menunjukkan cakupan buah 66% untuk penerbangan di dalam kanopi, 55% untuk penerbangan di atas kanopi, dan 34% untuk kendaraan darat pada keterangan gambar; teks artikel menyebut 36% untuk kendaraan darat. Pada optimasi ketinggian, kamera depan mencapai cakupan 32,3% pada ketinggian 6,5 m, sedangkan dua kamera samping mencapai 45,4% pada ketinggian 5 m. Penulis menyatakan keterbatasan berikut: lintasan lurus melewatkan buah di sisi seberang pohon, dan pada kebun yang lebih luas dengan buah lebih kecil, oklusi yang meningkat dapat menurunkan akurasi deteksi. Penulis juga menyebut pekerjaan berikutnya yang belum diterapkan, yakni memasukkan kecepatan terbang dalam perencanaan global, umpan balik waktu nyata atas mutu citra, dan penghitungan langsung di kendaraan. Akurasi penghitungan pada kebun skala penuh tidak dilaporkan.
