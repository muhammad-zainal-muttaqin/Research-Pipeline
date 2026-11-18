# DynaSLAM II: Tightly-Coupled Multi-Object Tracking and SLAM

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bescos2021dynaslam` |
| Judul asli | DynaSLAM II: Tightly-Coupled Multi-Object Tracking and SLAM |
| Penulis | Bescos, Berta; Campos, Carlos; Tardos, Juan D.; Neira, Jose |
| Tahun | 2021 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [bescos2021dynaslam.pdf](../pdf/bescos2021dynaslam.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2021.3068640

## Gambaran Umum

Masalah utama adalah asumsi kekakuan adegan (*scene rigidity*) pada algoritma visual SLAM yang membatasi pemakaiannya di lingkungan nyata berpenduduk. Pendekatan yang umum dipakai mendeteksi wilayah dinamis lalu membuangnya, sehingga hanya menghasilkan estimasi ego-gerak dari struktur statis. Aplikasi seperti kendaraan otonom, kolaborasi multi-robot, serta realitas virtual dan augmented memerlukan informasi gerak eksplisit tentang objek di sekitar. Penelitian ini mengajukan DynaSLAM II, sistem SLAM visual untuk konfigurasi stereo dan RGB-D yang mengintegrasikan pelacakan multi-objek secara terikat (*tightly-coupled*), bukan sekadar menyingkirkan fitur dinamis. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Metode dibangun di atas ORB-SLAM2. Masukannya berupa citra stereo atau RGB-D yang tersinkron dan terkalibrasi; keluarnya berupa pose kamera, pose objek dinamis pada setiap frame, serta peta spasi-waktu yang memuat objek dinamis. Data uji adalah dataset KITTI *tracking* dan KITTI *raw* yang berisi citra stereo berwarna dan *grayscale* dari sudut pandang mobil di lingkungan perkotaan dan jalan, dengan kendaraan dan pejalan kaki, serta data GPS. Untuk pelacakan multi-objek, trayektori dan kotak bounding 3D sebagai kebenaran tanah berasal dari anotasi manual pada awan titik LiDAR 3D.

Mekanisme deteksi dan asosiasi memakai segmentasi semantik *instance* per piksel dan fitur ORB yang dicocokkan lintas pasangan stereo. Fitur statis dan dinamis diasosiasikan dengan frame sebelumnya dan peta dengan asumsi kecepatan konstan; kecocokan dinamis dicari melalui reprojeksi atau, jika kecepatan belum terinisialisasi, melalui pencocokan *brute force* yang dibatasi pada *instance* dengan tumpang tindih terbesar. Asosiasi tingkat *instance*-ke-objek memakai IoU kotak bounding 2D hasil CNN, dan dua objek diberi id pelacakan sama jika sebagian besar titiknya cocok. Sistem menangani oklusi karena titik pada frame saat ini dicocokkan ke objek di peta, bukan ke objek pada frame sebelumnya. Inti mekanismenya adalah *bundle adjustment* terikat yang mengoptimasi bersama struktur statis, pose kamera, dan trayektori objek dalam jendela waktu lokal; kotak bounding 3D dioptimasi secara terpisah dalam jendela waktu tetap. Representasi berbasis objek menekan jumlah parameter dari N = 6Nc + Nc × No × 3Nop menjadi N′ = 6Nc + Nc × 6No + No × 3Nop.

Hasil pengujian pada KITTI *tracking* (Tabel I) menunjukkan galat trayektori absolut (ATE) rata-rata 1,54 m untuk DynaSLAM II, dibandingkan 2,33 m (ORB-SLAM2) dan 1,45 m (DynaSLAM), dengan galat pose relatif (RPE) translasi 0,053 m per frame dan rotasi 0,043 derajat per frame. Pada KITTI *raw* (Tabel II), ATE rata-rata 1,44 m berbanding 3,73 m (ORB-SLAM2) dan 1,30 m (DynaSLAM). Untuk pelacakan, metrik presisi pelacakan multi-objek (MOTP) 2D pada Tabel III untuk kategori Easy, Moderate, dan Hard berturut-turut adalah 64,69%, 58,75%, dan 58,36%, sedangkan MOTP 3D adalah 53,14%, 48,66%, dan 48,57%; kategori tersebut didasarkan pada tinggi kotak bounding 2D, tingkat oklusi, dan truncasi. Waktu komputasi (Tabel V) mencapai 10–12 frame per detik, dengan utas pelacakan 80,10 ± 0,78 ms pada sekuens 0003 dan 94,56 ± 1,27 ms pada sekuens 0020, di luar waktu komputasi jaringan segmentasi semantik. Angka ATE dan RPE dihitung dengan protokol benchmark KITTI, sedangkan MOTP mengikuti metrik CLEAR MOT.

Batasan yang dinyatakan penulis adalah inti berbasis fitur membatasi kemampuan menemukan kotak bounding 3D yang akurat dan melacak objek bertekstur rendah; pemanfaatan informasi visual padat secara penuh diusulkan sebagai perbaikan. Jumlah kotak bounding yang ditemukan lebih sedikit daripada metode pencocokan stereo padat, dan akurasi pelacakan pejalan kaki lebih rendah daripada mobil karena bentuknya yang tidak kaku. Penulis juga mencatat bahwa VDO-SLAM umumnya menghasilkan galat pose rotasi lebih rendah, yang dikaitkan dengan algoritma estimasi pose kamera dan tata sensor, bukan dengan kinerja pelacakan objek. Batasan lain tidak dinyatakan.

