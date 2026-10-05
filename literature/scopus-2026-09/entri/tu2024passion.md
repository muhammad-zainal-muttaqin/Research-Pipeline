# A passion fruit counting method based on the lightweight YOLOv5s and improved DeepSORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tu2024passion` |
| Judul asli | A passion fruit counting method based on the lightweight YOLOv5s and improved DeepSORT |
| Penulis | Tu, Shuqin; Huang, Yufei; Liang, Yun; Liu, Hongxing; Cai, Yifan; Lei, Hua |
| Tahun | 2024 |
| Venue | Precision Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | passion fruit |

## Tautan Akses
- PDF: [tu2024passion.pdf](../pdf/tu2024passion.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-024-10132-1

## Gambaran Umum
Makalah ini mengusulkan metode pencacahan buah markisa (*passion fruit*) dari video yang terdiri atas tiga komponen: detektor ringan YOLOv5s-little, DeepSORT yang diperbaiki, dan aturan penghitungan berbasis status lintasan. Dua perbaikan pada DeepSORT adalah penundaan pembuatan lintasan baru di daerah tengah dan tepi bingkai, serta putaran kedua pencocokan *intersection over union* (IoU). Penelitian memakai 12 video pendek yang direkam di kebun markisa berpergola di Heyuan dan Distrik Huadu, Guangzhou, Tiongkok.

Detektor YOLOv5s-little mencapai presisi 98,9%, recall 98,3%, mAP@0,5 sebesar 99,5%, dan ukuran model 0,9 MB. DeepSORT yang diperbaiki mencapai HOTA 79,6%, MOTA 92,58%, IDF1 95,02%, dan 11 pertukaran identitas (IDSW), dibandingkan DeepSORT asli dengan 74,94%, 90,78%, 85,86%, dan 76. Abstrak melaporkan akurasi hitung rerata statistik 95,1% dan $R^2 = 0{,}96$ terhadap hitung manual; angka akurasi pada bagian hasil adalah 93,28% (lihat catatan verifikasi).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil markisa secara manual memakan tenaga dan waktu. Model deteksi yang besar sulit dipasang pada robot dan perangkat bergerak. Selain itu, buah markisa sering tertutup daun atau buah lain, berukuran kecil, dan berwarna mirip daun pada tahap belum matang, sehingga deteksi terlewat dalam waktu lama dan buah yang sama menerima identitas baru sehingga terhitung ganda.

Cara hitung yang lazim, yaitu nilai identitas maksimum yang dihasilkan DeepSORT (*maximum ID value counting*, MAX-IDVC), cenderung melampaui hitungan manual. Metode garis hitung (*count line*) lebih akurat tetapi memerlukan langkah tambahan setelah pelacakan. Penulis menilai solusi yang ada rumit dan kurang cocok untuk markisa.

## Ide Utama
Penulis menggabungkan tiga hal: (1) detektor yang dipangkas dari YOLOv5s agar sangat kecil; (2) pembatasan lokasi pembuatan lintasan baru, karena pertukaran identitas yang salah terutama muncul di daerah tengah dan tepi bingkai, ditambah putaran IoU kedua agar deteksi di daerah terlarang tetap dapat dikaitkan dengan lintasan yang ada; (3) penghitungan yang diperbarui saat lintasan dibuat atau dihapus, sehingga tidak perlu garis hitung atau identitas maksimum.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi dan penyiapan data
Video direkam dengan ponsel Huawei Mate30 secara horizontal dari jarak 5–8 m. Terkumpul 12 video berdurasi sekitar 15 detik, format MP4, 25 bingkai/detik, resolusi 1280 × 720. Video dipilih yang padat buah (10 buah atau lebih), dipotong dengan FFmpeg, dan dianotasi dengan DarkLabel, dengan identitas unik untuk tiap buah. Diperoleh 1.287 bingkai citra yang dibagi acak 7:1:2 menjadi 900 latih, 130 validasi, dan 257 uji. Augmentasi (kecerahan, kontras, derau Gaussian, pemotongan) menggandakan 900 citra latih menjadi 1.800. Pada bagian implementasi disebut 4.000 citra beraugmentasi dipakai melatih detektor (lihat catatan verifikasi). Tiga video dipakai menguji pelacakan (berisi 28, 42, dan 19 buah) dan sembilan video lain melatih model identifikasi ulang (*re-identification*, ReID), yang berisi 198 buah markisa dengan sekitar 250 citra per buah setelah augmentasi.

### 2. Detektor YOLOv5s-little
YOLOv5s-2Level menghapus lapisan P5 dari YOLOv5s karena target kecil. YOLOv5s-little berstruktur sama, lalu memperkecil parameter, kedalaman, lebar, dan jumlah anchor, sehingga ukurannya kurang dari sepersepuluh YOLOv5s. Pelatihan tanpa bobot awal, optimizer SGD, laju belajar 0,01, *batch* 32, 200 epoch, masukan 640 × 640.

### 3. DeepSORT yang diperbaiki
- Pencocokan bertingkat (*cascade matching*) antara deteksi dan lintasan terkonfirmasi memakai informasi gerak dan tampilan dengan algoritma Hungarian.
- Putaran IoU pertama untuk deteksi, lintasan, dan lintasan tidak terkonfirmasi yang belum cocok.
- Putaran IoU kedua untuk sisa yang belum cocok (perbaikan 2).
- Penundaan pembuatan lintasan (perbaikan 1): setelah bingkai ketiga, deteksi tanpa pasangan di daerah tengah atau tepi tidak boleh membuat lintasan baru; lebar batas ditetapkan 25 piksel. Lintasan dikonfirmasi setelah tiga kemenangan berturut-turut. Ambang `max_IoU_distance` 0,7.

### 4. Aturan penghitungan
Total bertambah 1 saat sebuah lintasan dibuat, berkurang 1 bila lintasan yang tidak cocok masih berstatus sementara (*tentative*) lalu dihapus, dan tidak berubah bila *time-since-update* lintasan melebihi 30.

## Eksperimen dan Hasil
Metrik deteksi: presisi, recall, mAP, waktu, dan ukuran. Metrik pelacakan: HOTA, MOTA, IDF1, IDSW. Metrik hitung: akurasi hitung dan akurasi hitung rerata statistik. Acuan hitung adalah hitung manual pada tiga video uji.

| Detektor (Tabel 1) | P (%) | R (%) | mAP@0,5 (%) | mAP@0,5:0,95 (%) | Waktu (s) | Ukuran (MB) |
|---|---|---|---|---|---|---|
| YOLOv5s | 99,1 | 98,8 | 99,8 | 87 | 0,0127 | 14,4 |
| YOLOv5s-2Level | 98,7 | 99,6 | 99,8 | 85,6 | 0,0097 | 3,4 |
| YOLOv5s-little | 98,9 | 98,3 | 99,5 | 78,2 | 0,0079 | 0,9 |

| Pelacak (Tabel 2 dan 3, semua video) | HOTA (%) | MOTA (%) | IDF1 (%) | IDSW |
|---|---|---|---|---|
| DeepSORT asli | 74,94 | 90,78 | 85,86 | 76 |
| DeepSORT diperbaiki | 79,60 | 92,58 | 95,02 | 11 |
| FairMOT | 68,04 | 84,67 | 75,73 | 280 |
| TransTrack | 54,36 | 55,36 | 71,35 | 351 |

Ablasi (Tabel 4): hanya penundaan pembuatan lintasan menghasilkan HOTA 74,87, MOTA 86,52, IDF1 87,94, IDSW 29; hanya putaran IoU kedua menghasilkan 77,83, 92,46, 91,30, dan 33 (urutan baris dibaca dari teks ekstraksi); keduanya menghasilkan 79,60, 92,58, 95,02, dan 11. Pada video 3 yang padat (42 buah), nilai identitas maksimum DeepSORT asli mencapai 65 pada bingkai 50 dan 89 pada bingkai 100, sedangkan DeepSORT yang diperbaiki mencapai 40 dan 43. Pada video 2 (19 buah), nilai maksimum asli 26 dan yang diperbaiki 19 pada bingkai 100.

Perbandingan penghitungan: akurasi hitung rerata statistik MAX-IDVC 86,19% dan metode usulan 93,28% (bagian hasil); regresi terhadap hitungan manual menghasilkan $R^2$ 0,9419 untuk MAX-IDVC dan 0,9633 untuk metode usulan. Akurasi terendah dan tertinggi MAX-IDVC masing-masing 52,4% dan 94,7%; untuk metode usulan 76,2% dan 100%.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: model sangat kecil (0,9 MB) dan cepat; IDSW turun dari 76 menjadi 11; penghitungan sederhana dan terintegrasi dengan manajemen lintasan; kinerja pelacakan lebih baik daripada FairMOT dan TransTrack pada data ini.

Keterbatasan yang dinyatakan penulis: YOLOv5s-little mungkin kurang baik pada pencahayaan atau sudut pandang berbeda; bila daerah terbatas ditetapkan tidak tepat, pelacakan dapat melewatkan buah, sehingga daerah perlu disesuaikan menurut skena; gerakan kamera yang cepat dan pengambilan menghadap matahari merugikan; faktor seperti cahaya dan tingkat kematangan belum diteliti.

Menurut pembacaan ringkasan ini, data uji pelacakan hanya tiga video berisi total 89 buah (28, 42, 19) dari satu sumber lokasi dan satu perangkat, sehingga generalisasi terbatas. Nilai mAP@0,5 mendekati 100% menunjukkan detektor hampir jenuh pada data ini, dan pembagian bingkai acak dari video yang sama dapat membuat bingkai latih dan uji serupa. Aturan daerah terlarang diset manual untuk skena dengan gerakan kamera horizontal; belum ada uji untuk gerak kamera lain. Penghitungan tidak dibedakan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video melalui pelacakan: DeepSORT dengan cascade matching (gerak dan tampilan), dua putaran IoU, dan pembatasan pembuatan lintasan baru di tengah dan tepi bingkai. Hitungan berasal dari jumlah lintasan yang dibuat dikurangi lintasan sementara yang dihapus, bukan dari identitas maksimum. Hitungan tidak dilaporkan per kelas. Acuan hitung adalah hitung manual pada video (anotasi identitas per bingkai untuk metrik pelacakan), bukan panen.

Hal yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pelaporan metrik identitas (IDSW, IDF1, HOTA) di samping jumlah, ketergantungan hitungan pada status lintasan, dan pembatasan lokasi pembuatan identitas baru. Keterbatasan pemindahan: pembatasan lokasi dan asumsi gerak kamera berkesinambungan berlaku untuk satu lintasan video, bukan perpindahan antarsisi pohon yang terputus.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `tu2024passion`.

Tu dkk. (2024) mengusulkan pencacahan markisa dari video dengan detektor ringan YOLOv5s-little (0,9 MB) dan DeepSORT yang diperbaiki melalui penundaan pembuatan lintasan di daerah tengah dan tepi serta putaran IoU kedua, ditambah aturan hitung berbasis status lintasan. Pada tiga video uji, IDSW turun dari 76 menjadi 11, HOTA naik dari 74,94% menjadi 79,6%, dan hitungan berkorelasi tinggi dengan hitung manual ($R^2 = 0{,}96$).

Catatan verifikasi data: angka detektor berasal dari Tabel 1; angka pelacakan dari Tabel 2 dan 3; ablasi dari Tabel 4; perbandingan hitung dari Gambar 11 dan 12 serta teks Bagian "Evaluation of counting method". Terdapat ketidakkonsistenan dalam makalah: abstrak dan kesimpulan menyebut akurasi hitung rerata statistik 95,1% dan peningkatan 7,09% atas MAX-IDVC, sedangkan bagian hasil menyebut 93,28% (MAX-IDVC 86,19%, selisih 7,09 poin menurut perhitungan sederhana atas angka bagian hasil). Teks menyebut 4.000 citra beraugmentasi untuk pelatihan, sementara bagian data menyebut 1.800. Tabel 2 pada ekstraksi: nilai IDF1 video 02 pada DeepSORT diperbaiki (92,58) identik dengan MOTA total, sehingga kemungkinan terdapat salah baca ekstraksi; angka itu tidak dipakai. Baris ablasi pada Tabel 4 hanya ditandai dengan tanda centang yang kolomnya tidak terbaca dari teks, sehingga penetapan setiap baris pada komponen tertentu ditafsirkan dari teks pembahasan. Gambar 11 dan 12 tidak terbaca dari teks. Persentase "improvement" 4,66%, 1,8%, dan 9,16% adalah selisih poin persentase.
