# Lightweight Improved YOLOv5s-CGhostnet for Detection of Strawberry Maturity Levels and Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tamrakar2024lightweight` |
| Judul asli | Lightweight Improved YOLOv5s-CGhostnet for Detection of Strawberry Maturity Levels and Counting |
| Penulis | Tamrakar, Niraj; Karki, Sijan; Kang, Myeong Yong; Deb, Nibas Chandra; Arulmozhi, Elanchezhian; Kang, Dae Yeong; Kook, Junghoo; Kim, Hyeon Tae |
| Tahun | 2024 |
| Venue | Agriengineering |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [tamrakar2024lightweight.pdf](../pdf/tamrakar2024lightweight.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering6020055

## Gambaran Umum

Kajian ini mengatasi kebutuhan algoritma deteksi dan lokalisasi stroberi yang ringan untuk robot pemanen. Model deteksi berbasis YOLO selama ini akurat, tetapi memerlukan ukuran model besar, daya komputasi tinggi, dan masih menghasilkan deteksi yang tidak diinginkan. Penulis bertujuan mengompresi YOLOv5s secara menyeluruh, mengganti fungsi loss kotak, dan menambahkan modul atensi agar model tetap akurat saat dijalankan pada perangkat dengan sumber daya terbatas.

Tanaman yang dipakai adalah stroberi kultivar Seolhyang yang ditanam di rumah kaca Laboratorium Sistem Pertanian Cerdas, Universitas Nasional Gyeongsang, Jinju, Korea Selatan, dari September 2022 hingga Maret 2023. Citra RGB dikumpulkan dengan kamera Sony Cyber-shot DSC-RX100 VII beresolusi 5472 × 3648 piksel pada November 2022–Januari 2023, pada tiga tingkat pencahayaan serta jarak 40–60 cm. Dataset mandiri terdiri atas 2.000 citra dengan 5–8 buah per citra, terdiri atas 5.000 sampel immature, 1.250 sampel transition, dan 4.200 sampel mature. Anotasi kotak pembatas dibuat dengan Label Studio 1.8.0, lalu citra dibagi menjadi himpunan latih, uji, dan validasi dengan rasio 80:10:10. Augmentasi mencakup HSV, rotasi, translasi, penskalaan, pembalikan, mix-up, dan mosaic.

Mekanisme deteksi memakai model YOLOv5s-CGhostnet. Modul CBS dan C3 pada backbone serta neck diganti dengan modul Ghost (GCBS, GhostBottleneck, GC3) yang menghasilkan peta fitur melalui konvolusi ordinary dalam jumlah kecil, lalu memperbanyaknya dengan transformasi linear murah berbasis konvolusi depth-wise. Modul CBAM ditempatkan sebelum SPPF dan di antara FPN–PAN untuk menimbang ulang peta fitur secara kanal dan spasial. Fungsi loss kotak GIoU diganti SIoU yang memperhitungkan biaya sudut, jarak, bentuk, dan IoU. Pelatihan memakai PyTorch dengan transfer learning, ukuran batch 16, weight decay 0,0005, learning rate awal 0,01, dan 100 iterasi pada Intel Core i7-10700 serta NVIDIA GeForce RTX 2060 6 GB.

Hasil dihitung dengan metrik presisi, recall, F1-score, dan mAP@0,5 pada ambang IoU lebih dari 0,5. Model mencapai mAP@0,5 sebesar 91,7%, presisi 88,1%, dan recall 87,7%, naik 0,98% mAP atas YOLOv5s. Ukuran model 9,4 MB, 6,02 × 10^6 parameter, dan 9,8 GFLOPS, masing-masing lebih rendah 49,25%, 46,18%, dan 67,35% daripada YOLOv5s; waktu inferensi 5 ms dan kecepatan 64 FPS. menurut Tabel 1, F1-score bernilai 87,9%, sedangkan narasi menyebut 90,1%. mAP per kelas berturut-turut mature, transition, dan immature adalah 97,2%, 86,8%, dan 91,2%. Ablasi menunjukkan mAP naik dari 0,824 pada model Ghostnet tanpa augmentasi menjadi 0,849 setelah augmentasi, 0,895 setelah CBAM, dan 0,917 setelah SIoU.

Batasan yang dinyatakan penulis mencakup kinerja immature yang lebih rendah karena ukuran dan tekstur buah beragam serta sulit dibedakan dari kanopi; buah pada tahap kuncup tidak dianotasi dan tidak dimasukkan ke dataset. Kelas transition memiliki mAP terendah karena ruang fitur yang luas antara immature dan mature serta jumlah sampel yang terbatas. Penulis juga menyatakan perbandingan dengan kajian lain sulit karena arsitektur dan kondisi lapang berbeda. Model belum diuji pada perangkat berdaya rendah; rencana lanjutan mencakup penerapan pada Raspberry Pi, penggunaan citra RGB-depth, arsitektur transformer, pruning, dan kuantisasi. Terdapat ketidaksesuaian angka dalam teks: simpulan menyebut ukuran model 5 MB, sementara Tabel 3 mencantumkan 9,4 MB.
