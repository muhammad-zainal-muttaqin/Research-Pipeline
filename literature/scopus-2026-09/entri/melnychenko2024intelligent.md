# Intelligent Integrated System for Fruit Detection Using Multi-UAV Imaging and Deep Learning †

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `melnychenko2024intelligent` |
| Judul asli | Intelligent Integrated System for Fruit Detection Using Multi-UAV Imaging and Deep Learning † |
| Penulis | Melnychenko, Oleksandr; Scislo, Lukasz; Savenko, Oleg; Sachenko, Anatoliy; Radiuk, Pavlo |
| Tahun | 2024 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [melnychenko2024intelligent.pdf](../pdf/melnychenko2024intelligent.pdf)
- DOI resmi: https://doi.org/10.3390/s24061913

## Gambaran Umum

Studi ini membangun sistem terintegrasi untuk mendeteksi dan menghitung buah di kebun memakai beberapa UAV sekaligus. Penulis menyatakan bahwa drone tunggal dibatasi oleh daya baterai, kapasitas angkut, dan sudut pandang, sementara kondisi lapangan yang berubah serta buah yang tertutup daun menyulitkan deteksi. Pengambilan citra dari beberapa UAV memerlukan penyatuan aliran video yang tersinkron agar buah yang sama tidak dihitung berulang. Tujuan sistem ini adalah menyinkronkan video dari beberapa kamera UAV secara langsung, menggabungkannya menjadi citra bersama, mendeteksi buah dengan arsitektur YOLOv5-v1, dan menghitung buah unik di seluruh area misi.

Uji lapangan dilakukan di kebun apel Fuji milik usaha tani “SAM+” di desa Kuzmin, oblast Khmelnytskyi, Ukraina, seluas 50 hektare dengan pohon berbentuk spindle ramping. Barisan panjangnya 500–800 m, jarak tanam 2 m, jarak antarbarisan 4 m, tinggi pohon rata-rata 3,5 m, dan perkiraan hasil 200 apel per pohon per musim. Tiga percobaan dilakukan pada 26, 28, dan 29 September 2023 berturut-turut dalam kondisi cerah dengan matahari di zenit, berawan, dan cerah dengan bayangan kuat. Tiga UAV DJI Phantom 4 RTK terbang pada ketinggian 1,2 m, 2,2 m, dan 3,2 m dengan sudut kamera 25° ke atas, 0°, dan 20° ke bawah; pengaturan ISO 400, 800, dan 1600 mengikuti kondisi cahaya. Stasiun GNSS D-RTK 2 mencatat posisi dengan ketelitian horizontal di bawah 2,5 cm dan vertikal di bawah 5 cm. Area uji mencakup dua barisan dengan lintasan terbang sekitar 1.600 m dan sekitar 800 pohon.

Data pelatihan berupa 1.214 citra apel Fuji yang diambil dengan iPhone 13 Pro Max pada berbagai kondisi oklusi dan pencahayaan. Data dibagi menjadi 1.014 citra latih dan 200 citra uji yang terdiri atas 100 citra cerah dan 100 citra berawan; citra uji memuat 1.007 buah tampak jelas dan 1.329 buah dengan oklusi campuran. Augmentasi dengan CLAID.AI menghasilkan total 16.224 citra latih, terdiri dari 15.210 citra hasil augmentasi dan 1.014 citra asli, tanpa tumpang tindih dengan data uji. Pelabelan memakai Amazon SageMaker Data Labeling; 200 citra uji diberi label manual dan sisanya otomatis. Pelatihan memakai optimizer Adam, 30 epoch, laju pembelajaran 0,001, dan berlangsung sekitar 9 jam pada GPU NVIDIA GeForce RTX 2060 6 GB.

YOLOv5-v1 merupakan YOLOv5 yang dimodifikasi dengan menambah lapisan squeeze-and-excitation, menyederhanakan modul BottleneckCSP dengan menghilangkan satu lapisan konvolusi, mengubah penggabungan peta fitur menjadi pasangan lapisan 5–18, 8–14, dan 13–24, serta menyesuaikan ukuran awal kotak jangkar skala kecil dan menengah agar mengurangi deteksi buah di latar belakang. Modul focus mengubah masukan 3 × 640 × 640 menjadi 12 × 320 × 320 lalu 32 × 320 × 320. Ambang kepercayaan ditetapkan 0,5. Penghitungan membuang kotak objek kecil, mencocokkan koordinat antarframe, memberi ID pada objek baru, lalu memprediksi posisi berikutnya dengan filter Kalman dan penugasan Hungarian yang memakai jarak Mahalanobis serta riwayat 100 frame. Buah yang terdeteksi di luar area misi tidak dihitung, dan buah yang tertangkap beberapa kamera dihitung sekali. Sinkronisasi dinilai dengan SSIM dan PSNR; citra gabungan dengan SSIM di bawah 0,50 dan PSNR di bawah 30 dibuang.

Hasil deteksi pada 200 citra uji dengan 2.336 buah menunjukkan presisi 83,8%, recall 91,5%, F1 87,5%, dan mAP 86,8%; untuk 1.007 buah tampak jelas, mAP sebesar 89,2%, sedangkan untuk 1.329 buah dengan oklusi, 84,9%. mAP dihitung sebagai rata-rata AP untuk satu kelas apel Fuji, sedangkan presisi dan recall dihitung dari TP, FP, dan FN. Pada uji lapangan dengan perkiraan 160.000 buah, jumlah yang terdeteksi dan dihitung berturut-turut adalah 147.382, 145.223, dan 132.304 untuk kondisi cerah di zenit, berawan, dan cerah berbayang; buah yang terdeteksi tetapi tidak dihitung karena berada di luar area misi berjumlah 72.143, 69.944, dan 69.336; buah yang terlihat oleh dua atau tiga UAV tetapi dihitung sekali berjumlah 5.743, 6.611, dan 8.442. Tingkat positif palsu dan negatif palsu berturut-turut sebesar 8% dan 11,5% pada kondisi cerah, 14,7% dan 18,3% pada kondisi berawan, serta 22,2% dan 26,2% pada kondisi berbayang. Sinkronisasi video menghasilkan SSIM antara 0,45 dan 0,91 dengan rata-rata 0,87 serta PSNR antara 27,2 dan 39,1. Perbandingan model menunjukkan YOLOv5-v1 memiliki mAP 86,8%, kecepatan 0,015 detik per citra, 6,52 × 10⁶ parameter, dan ukuran 12,70 MB, dibandingkan YOLOv5-CS dengan mAP 81,7% dan Mask R-CNN dengan mAP 82,0%. Penulis menyatakan keterbatasan berupa gangguan oklusi daun, ketahanan yang belum diuji secara memadai pada hujan lebat atau kabut, serta kemampuan adaptasi ke jenis buah dan tata letak kebun lain yang masih perlu diteliti.

