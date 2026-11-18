# AKFruitYield: Modular benchmarking and video analysis software for Azure Kinect cameras for fruit size and fruit yield estimation in apple orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `miranda2023akfruityield` |
| Judul asli | AKFruitYield: Modular benchmarking and video analysis software for Azure Kinect cameras for fruit size and fruit yield estimation in apple orchards |
| Penulis | Miranda, Juan Carlos; Arn\'o, Jaume; Gen\'e-Mola, Jordi; Fountas, Spyros; Gregorio, Eduard |
| Tahun | 2023 |
| Venue | Softwarex |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [miranda2023akfruityield.pdf](../pdf/miranda2023akfruityield.pdf)
- DOI resmi: https://doi.org/10.1016/j.softx.2023.101548

## Gambaran Umum

Perangkat lunak ini mengatasi kebutuhan perkiraan hasil panen awal untuk mengatur logistik kebun. Pengukuran buah memakai citra dua dimensi mensyaratkan target kalibrasi berukuran diketahui yang ditempatkan dekat buah, sedangkan teknik tiga dimensi seperti SfM, LiDAR, dan kamera RGB-D menghilangkan kebutuhan itu dan mengukur semua buah dalam citra sekaligus. Kamera RGB-D murah menyediakan informasi warna, kedalaman, dan inframerah, tetapi petani memerlukan aplikasi otomatis yang mengubah data lapang banyak menjadi informasi yang dapat dipakai. AKFruitYield melengkapi perangkat lunak AKFruitData sebelumnya yang hanya melakukan akuisisi dan ekstraksi data, dengan dua tujuan: membandingkan algoritme pengukuran ukuran buah dan model alometrik hasil panen, serta menyediakan analisis video untuk deteksi, pengukuran, dan prediksi hasil panen pada skala petak atau per hektar.

Data berasal dari uji lapang di kebun apel eksperimen kultivar Story Inoredcov di Mollerussa, Lleida, Spanyol. Pohon ditanam dengan jarak 3,6 × 1 m dan kanopi setinggi sekitar 3,5 m pada koordinat 41,617465 LU, 0,870730 BT, ketinggian 246,3 m. Akuisisi memakai kamera Azure Kinect (Microsoft) dalam bentuk video yang mencakup warna, kedalaman, dan data inframerah, diperoleh melalui modul AK_ACQS dari AKFruitData. Modul AK_FRAEX mengekstrak citra RGB beserta informasi kedalaman dalam berbagai format; citra berlabel disimpan dalam format PASCAL-VOC untuk pembandingan, sedangkan citra untuk pelatihan detektor disimpan dalam format COCO, dan video dikelola dalam format Matroska MKV.

Mekanisme terdiri atas dua modul. AK_SW_BENCHMARKER membandingkan algoritme pada citra berlabel yang telah dideteksi dan diberi label manual. Pengguna memilih penentu daerah menarik (ROI) berupa kotak pembatas (BBOX) atau topeng biner (MASK); untuk MASK tersedia empat penyesuaian geometri, yaitu lingkaran pembungkus (CE), lingkaran penyesuaian (CF), elips penyesuaian (EF), dan persegi panjang terputar (RR). Jarak buah ke kamera diambil dari statistik piksel ROI berupa kedalaman rata-rata (AVG), modus (MOD), atau minimum (MIN), lalu ukuran dalam piksel dikonversi menjadi milimeter memakai teori lensa tipis. Sumbu utama (A1), sumbu minor (A2), dan berat hasil model alometrik dibandingkan terhadap data sebenarnya dengan metrik RMSE, MAE, dan MAPE. AK_VIDEO_ANALYSER memproses video RGB-D dengan penyaringan berdasarkan koordinat dan rentang kedalaman, lalu menerapkan detektor Mask R-CNN atau Faster R-CNN yang dilatih pada data apel kebun sendiri, dilanjutkan pengukuran ukuran dan prediksi berat. Kedua modul memakai Python 3.8, antarmuka Tkinter, OpenCV, NumPy, scikit-learn, Pandas, dan PyTorch, berjalan pada Windows 10 atau Ubuntu 20.04 dengan Azure Kinect SDK serta lisensi MIT. Pengukuran deteksi berupa presisi, recall, atau AP tidak dinyatakan dalam artikel perangkat lunak ini.

Hasil yang dilaporkan bersifat uji pendahulu. Pengukuran ukuran buah yang tidak tertutup menghasilkan MAPE di bawah 5%, sebanding dengan teknik pencinderaan tiga dimensi mutakhir lain. Kombinasi terbaik antara algoritme pengukuran ukuran dan model alometrik memberi prediksi berat buah dengan MAPE di bawah 6%, lebih rendah daripada ambang batas galat 10% yang biasanya diterima dalam prediksi hasil panen. Modul video menampilkan jumlah buah dan hasil panen secara langsung selama analisis dan menghasilkan laporan CSV yang memuat ukuran dalam piksel dan milimeter, jarak dalam milimeter, serta berat dalam gram per buah. Penyaringan koordinat dan kedalaman mencegah buah dari barisan belakang ikut terhitung; pengujian juga memakai bola busa selain apel untuk memeriksa kemampuan penggunaan modul pada dua jenis objek. Angka kinerja deteksi tidak dinyatakan.

Batasan yang dinyatakan penulis mencakup ketergantungan modul pembandingan pada citra berlabel manual dan keterbatasan uji ukuran pada buah yang tidak tertutup. Perangkat lunak dibangun khusus untuk kamera Azure Kinect; penggunaan sensor RGB-D lain memerlukan penulisan rutinitas ekstraksi data (*wrapper*) khusus. Modul video dapat disesuaikan untuk kebun lain hanya bila detektor dan model prediksi berat tersedia atau dilatih ulang untuk kultivar, spesies, dan tahap perkembangan buah lain. Penulis mengusulkan *Multi-Object Tracking and Segmentation* (MOTS) sebagai peningkatan di masa depan dan menyatakan bahwa keluaran berupa prediksi hasil panen, bukan sekadar penghitungan buah. Rincian kinerja deteksi dan validasi lapang skala besar tidak dinyatakan.

