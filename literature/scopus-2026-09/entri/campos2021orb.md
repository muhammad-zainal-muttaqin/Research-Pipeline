# ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `campos2021orb` |
| Judul asli | ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM |
| Penulis | Campos, Carlos; Elvira, Richard; Rodriguez, Juan J. Gomez; M. Montiel, Jose M.; D. Tardos, Juan |
| Tahun | 2021 |
| Venue | IEEE Transactions on Robotics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [campos2021orb.pdf](../pdf/campos2021orb.pdf)
- DOI resmi: https://doi.org/10.1109/tro.2021.3075644

## Gambaran Umum

Masalah utama adalah keterbatasan sistem visual SLAM dan odometri visual dalam memanfaatkan informasi masa lalu. Kebanyakan sistem hanya memakai asosiasi data jangka pendek, sehingga membuang unsur lingkungan yang keluar dari pandangan dan menimbulkan pergeseran estimasi terus-menerus. Penelitian ini mengajukan ORB-SLAM3, pustaka SLAM sumber terbuka pertama yang melakukan SLAM visual, visual-inersia, dan multimap untuk kamera monokular, stereo, dan RGB-D dengan model lensa *pin-hole* dan *fisheye*. Dua pembaharuan utamanya adalah sistem visual-inersia terintegrasi penuh berbasis estimasi *maximum a posteriori* (MAP), termasuk saat inisialisasi unit pengukur inersia (IMU), serta sistem multimap yang memakai metode pengenalan tempat berdaya ingat (*recall*) lebih tinggi. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Data uji adalah dataset EuRoC yang memuat 11 sekuens dengan empat konfigurasi sensor (monokular, monokular-inersia, stereo, dan stereo-inersia), dataset TUM-VI yang memuat 28 sekuens dalam enam lingkungan yang direkam dengan rig stereo-inersia *fisheye* genggam, serta percobaan multisessi pada kedua dataset. Metode dibangun di atas ORB-SLAM2 dan ORB-SLAM-VI. Sistem terdiri dari utas pelacakan, pemetaan lokal, serta penutupan gelung dan penggabungan peta, dengan Atlas sebagai representasi multimap berisi kumpulan peta terputus yang dibangun pada sesi berbeda. Pengenalan tempat memakai DBoW2 yang dimodifikasi: kandidat keyframe diperiksa lebih dahulu secara geometris, lalu diverifikasi pada tiga keyframe rekan-tampak, bukan menunggu tiga keyframe berurutan. Mekanisme asosiasi data mencakup empat tingkat: jangka pendek, jangka menengah, jangka panjang, dan multimap. Inisialisasi IMU memakai estimasi MAP tiga tahap — estimasi visual saja, estimasi inersia saja, lalu estimasi visual-inersia bersama — dengan skala sebagai variabel optimasi tersendiri.

Mekanisme deteksi dan asosiasi berbasis pada fitur ORB yang dicocokkan memakai deskriptor, dengan *bundle adjustment* (BA) pada jendela keyframe lokal. Penggabungan peta memakai jendela las (*welding window*) yang terdiri dari keyframe yang cocok beserta tetangganya, dilanjutkan BA lokal dan optimasi graf pose untuk menyebarkan koreksi ke seluruh peta. Sistem tidak bergantung pada rektifikasi stereo dan memperlakukan rig stereo sebagai dua kamera monokular dengan transformasi SE(3) tetap. Model kamera diabstraksi sehingga mendukung model *pin-hole* dan *fisheye* Kannala–Brandt. Akurasi diukur dengan galat trayektori absolut akar kuadrat rata-rata (rms ATE), menyelaraskan trayektori dengan kebenaran tanah memakai transformasi Sim(3) untuk monokular dan SE(3) untuk konfigurasi lain; galat skala dihitung sebagai |1 − s| dari alignment Sim(3).

Hasil pengujian menunjukkan ORB-SLAM3 lebih akurat daripada sistem terbaik sebelumnya pada semua konfigurasi sensor. Inisialisasi IMU mencapai galat skala 5% dalam 2 detik dan menyatu ke galat 1% dalam 15 detik, jauh lebih cepat daripada ORB-SLAM-VI yang memerlukan 15 detik dan VI-DSO yang memerlukan 20–30 detik. Pada dataset EuRoC, sistem monokular-inersia 2,6 kali lebih akurat daripada VINS-Mono pada operasi satu sesi dan 3,2 kali lebih akurat pada operasi multisessi. Pada dataset TUM-VI, SLAM stereo-inersia mencapai akurasi rata-rata 9 mm pada gerakan genggam cepat di ruang kelas, sedangkan pada drone EuRoC mencapai 3,5 cm. Untuk sekuens *room* yang mewakili skenario AR/VR, konfigurasi monokular-inersia menurunkan rms ATE rata-rata mendekati 1 cm dan stereo-inersia menurunkannya ke bawah 1 cm. Waktu jalan sistem mencapai 30–40 frame per detik dan 3–6 keyframe per detik, dengan pengenalan tempat 10 ms per keyframe. Semua angka dihitung dari percobaan yang dijalankan pada CPU Intel Core i7-7700 3,6 GHz dengan 32 GB memori.

Batasan yang dinyatakan penulis: kegagalan utama terjadi pada lingkungan bertekstur rendah; metode langsung lebih tangguh dalam kondisi tersebut, tetapi hanya mendukung asosiasi jangka pendek dan menengah, sedangkan pencocokan deskriptor fitur lebih tangguh untuk asosiasi jangka panjang dan multimap tetapi kurang handal untuk pelacakan dibandingkan Lucas–Kanade. Gerakan lambat atau tanpa rotasi *roll* dan *pitch* menyulitkan inisialisasi IMU, sehingga penulis menyarankan SLAM stereo dalam kondisi tersebut. Rotasi murni selama eksplorasi tidak memungkinkan estimasi kedalaman pada konfigurasi monokular-inersia. Pada sekuens luar ruangan TUM-VI, kelangkaan fitur visual dekat menyebabkan pergeseran parameter inersia dan galat 10–70 m; titik dari langit berawan dibuang dengan membatasi jarak 20 m. Penulis tidak membandingkan waktu jalan dengan sistem lain.
