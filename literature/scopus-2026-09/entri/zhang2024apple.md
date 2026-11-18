# An Apple Detection and Localization Method for Automated Harvesting under Adverse Light Conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2024apple` |
| Judul asli | An Apple Detection and Localization Method for Automated Harvesting under Adverse Light Conditions |
| Penulis | Zhang, Guoyu; Tian, Ye; Yin, Wenhan; Zheng, Change |
| Tahun | 2024 |
| Venue | Agriculture Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [zhang2024apple.pdf](../pdf/zhang2024apple.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture14030485

## Gambaran Umum

Penelitian ini mengatasi penurunan kinerja deteksi dan pelokalan apel pada robot pemanen akibat kondisi pencahayaan yang buruk, seperti hari berawan, senja, cahaya berlebih, kontras rendah, dan kecerahan rendah. Penulis meninjau metode peningkatan citra cahaya rendah yang ada, seperti Retinex-Net, Zero-DCE, MBLLEN, KinD, TSN-CA, dan RDGAN, serta menyatakan bahwa metode tersebut memiliki keterbatasan pada pelestarian warna, peredaman derau, pelestarian detail, atau kompleksitas dan waktu komputasi. Tujuan penelitian ini adalah membangun metode deteksi dan pelokalan apel yang akurat dan tangguh pada kondisi cahaya buruk dengan cara menggabungkan peningkatan citra ringan, mekanisme perhatian, perbaikan fungsi rugi, dan pengukuran jarak dengan kamera binokular.

Data dikumpulkan dari kebun apel seluas sekitar 30 hektare di Distrik Changping, Beijing, yang memuat dua kultivar, yaitu Fuji dan Golden Crown. Pengambilan citra dilakukan pada September–Oktober 2022 menggunakan kamera digital dalam berbagai kondisi cuaca, waktu (pagi, siang, sore, dan senja), sudut cahaya (cahaya langsung, samping, dan belakang), serta jarak pengambilan, menghasilkan 2.043 citra. Himpunan uji terdiri atas 200 citra cahaya normal dan 200 citra cahaya buruk, sedangkan 1.643 citra sisanya dipakai untuk latih lalu diperluas menjadi 9.858 citra melalui peningkatan dan penurunan kecerahan, pencerminan horizontal dan vertikal, serta rotasi berbagai sudut. Pelatihan memakai PyTorch 1.6.0 dan GPU GeForce GTX 1080ti, sedangkan akuisisi memakai kamera binokular resolusi 1920 × 1080 pada komputer dengan prosesor i5-8300, memori 8 GB, dan GPU GTX1050Ti.

Model yang diusulkan, LE-YOLO, terdiri atas tiga modul. Modul peningkatan citra memakai stacked attention residual network (SARN), yang menyisipkan modul perhatian kanal SE ke dalam blok residual dan jalur pintasnya serta menggabungkan kembali fitur dangkal dengan fitur tingkat tinggi melalui koneksi global agar informasi warna tetap terjaga. Modul deteksi memakai YOLOv5s yang diberi mekanisme perhatian SE sehingga bobot tiap kanal fitur ditentukan secara otomatis; fungsi rugi CIoU diganti dengan EIoU yang memisahkan rugi tumpang tindih, rugi jarak pusat, dan rugi selisih lebar–tinggi untuk mengatasi kelemahan komponen rasio aspek pada CIoU. Pelatihan memakai SGD dengan ukuran batch 4, momentum 0,937, weight decay 0,0005, 100 epoch, serta augmentasi Hue 0,015, saturasi 0,7, dan nilai 0,4. Modul pelokalan memakai kamera binokular: citra terlebih dahulu difilter median, stereo matching mencocokkan titik panen yang sama pada citra kiri dan kanan, lalu parallax diubah menjadi koordinat tiga dimensi dengan segitiga pengukur; titik panen yang dipakai adalah pusat kotak deteksi. Kalibrasi memakai papan checkerboard berukuran 24 mm dengan 8 × 6 titik sudut dan menghasilkan baseline kamera 119,344 mm.

Pada uji ablasi, YOLOv5s dasar menghasilkan presisi 0,852, recall 0,802, dan mAP 0,853; penambahan SARN menaikkan mAP menjadi 0,885, penambahan SE menjadi 0,867, dan penggantian rugi menjadi EIoU menghasilkan 0,863. Gabungan ketiganya mencapai presisi 0,897, recall 0,851, dan mAP 0,903, atau naik masing-masing 4,4%, 4,9%, dan 5,0%. Pada perbandingan dengan YOLOv5s, RDGAN+YOLOv5s, dan Zero-DCE+YOLOv5s, model yang diusulkan mencapai mAP 0,972 pada cahaya normal, 0,782 pada cahaya berlebih, dan 0,960 pada cahaya buruk, dengan waktu inferensi 102 ms lebih singkat daripada RDGAN (256 ms) dan Zero-DCE (198 ms). Pada pelokalan, galat jarsak rata-rata turun dari 0,57 cm menjadi 0,32 cm pada cahaya normal dan dari 2,38 cm menjadi 0,65 cm pada cahaya buruk, yang sesuai dengan perbaikan 44% dan 73% yang diklaim penulis.

Penulis menyatakan beberapa keterbatasan. Modul peningkatan citra dapat sedikit menurunkan kecepatan inferensi, terbukti dari waktu 102 ms berbanding 83 ms pada YOLOv5s dasar. Akurasi deteksi pada apel yang tertutup berat belum divalidasi secara memadai. Penelitian lanjutan diarahkan pada penambahan citra dengan latar kompleks, pengujian pada berbagai skenario lingkungan, serta penerapan metode pada kultivar apel dan buah lain. Penulis juga menyatakan data tidak tersedia publik dan hanya dapat diminta kepada penulis.

