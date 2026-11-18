# 3D reconstruction and segmentation of grape bunches for robotic berry thinning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yokin20263d` |
| Judul asli | 3D reconstruction and segmentation of grape bunches for robotic berry thinning |
| Penulis | Yok-In, Kabin; Buayai, Prawit; Moeurn, Dear; Mao, Xiaoyang |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [yokin20263d.pdf](../pdf/yokin20263d.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111898

## Gambaran Umum

Penelitian ini mengatasi penipisan buah anggur meja, yaitu pembuangan selektif 20–40% buah dari tandan rapat. Pekerja menentukan buah yang dibuang berdasarkan perkiraan jumlah buah dan ciri spasial 3D setempat, seperti kerapatan dan posisi relatif. Penulis menilai bahwa metode berbasis citra 2D mengalami galat hitung akibat oklusi dan tidak menyediakan informasi spasial 3D yang diperlukan untuk manipulasi. Tujuan penelitian adalah membangun alur visi yang terintegrasi dengan robot untuk merekonstruksi struktur tandan dari citra RGB banyak pandangan berpose, lalu menghasilkan posisi 3D per buah dan pose dekatan 6-DoF yang siap dipakai robot.

Tanaman yang dipakai adalah anggur meja di rumah kaca. Data utama berupa sekuens 360° sebanyak 279 citra RGB per tandan, resolusi 840 × 480, yang diambil dengan kamera Intel RealSense D405 pada lengan Fanuc CRX-5iA dalam konfigurasi *eye-in-hand* pada jarak kerja sekitar 300 mm. Pose kamera diperoleh dari rantai kinematika robot melalui ROS 2 TF2, bukan COLMAP, sehingga awan titik langsung berada dalam kerangka meter dasar robot. Rekonstruksi memakai Nerfacto dari Nerfstudio dengan 5.000 iterasi, laju belajar 0,01 untuk jaringan dan 0,001 untuk kamera, serta 4.096 sinar per batch; awan titik diekstrak melalui proyeksi balik dengan ambang opasitas 0,5. Untuk pengujian skala besar, penulis memakai 52 tandan yang direkam dengan iPhone 15 pada 3840 × 2160, 60 fps, dengan pose dari COLMAP dan skala meter dipulihkan memakai penanda kalibrasi 45,0 mm.

Mekanisme deteksi dan penghitungan memakai RANSAC untuk mencocokkan bola pada awan titik. Hipotesis bola dibentuk dari empat titik acak, diterima bila jumlah titik pendukung melebihi 400 dan jari-jari berada dalam rentang 10–20 mm, dengan toleransi jarak 1,5 mm dan maksimal 1.000 iterasi; titik pendukung dihapus setelah setiap deteksi agar bola berikutnya dapat ditemukan. Struktur batang dan tangkai diperoleh dari awan titik sisa melalui *Laplacian-based contraction* dan *minimum spanning tree*. Orientasi tiap buah dioptimalkan dengan merepresentasikan rotasi memakai format 6D Zhou dkk., lalu menyelaraskan sumbu dekatan ke arah titik kerangka terdekat memakai Adam dengan laju belajar 0,01 hingga 2.000 iterasi. Perintah gerak dijalankan lewat MoveIt 2 dengan perencana RRTConnect, berupa gerakan ke pose prategar, penyisipan lurus sejauh 80 mm, lalu penjepitan.

Hasil utama dihitung pada tiga himpunan uji yang berbeda. Pada 10 tandan dari rekonstruksi D405 berpose robot, RANSAC mencapai MAE 0,50 buah, RMSE 0,71 buah, dan galat rata-rata pusat 2,712 mm dengan ambang pencocokan 3D IoU 0,25; galat hitung absolut maksimal satu buah. Pada 52 tandan, RANSAC mencapai AP 0,914 dan AR 0,945, mengungguli SoftGroup++ yang mencatat AP 0,828 dan AR 0,884, dengan MAE penghitungan 1,1 buah dan RMSE 1,7 buah. Pada 35 percobaan manipulasi, pose prategar tercapai pada 30 percobaan (85,7%), dan 25 di antaranya berhasil mencapai target (83,3%); tingkat keberhasilan jepitan ujung ke ujung naik dari 51,4% pada arah tetap menjadi 68,6% pada arah sejajar tangkai. Waktu pemrosesan per tandan sekitar 3 menit 53 detik sebelum robot bergerak, dengan 8,5–10 detik per buah.

Batasan yang dinyatakan penulis meliputi kebutuhan memindai satu tandan pada satu waktu dengan cakupan pandangan rapat; penyampelan sudut yang terlalu jarang menurunkan kualitas rekonstruksi dan penghitungan. Rekonstruksi banyak tandan atau kanopi belum diuji karena struktur sekitar sengaja dibuang dengan penyaringan ROI bola. Kegagalan pada tahap target seluruhnya berasal dari ketidaklayakan inverse kinematics pada pose 6-DoF yang ketat, karena hanya sumbu dekatan yang dioptimalkan dan rotasi gulung penjepit dibiarkan bebas. Penugasan buah ke tangkai sensitif terhadap tangkai halus yang hilang akibat oklusi atau resolusi rendah, dengan galat penugasan bersama rata-rata 14,1% ± 9,3%. Penulis juga menyebut perlunya validasi lebih luas pada kultivar, tahap pertumbuhan, kondisi pencahayaan, kerapatan kanopi, dan operasi penipisan penuh; data yang dipakai dinyatakan bersifat rahasia.

