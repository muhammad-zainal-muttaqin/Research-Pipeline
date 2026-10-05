# Counting bagging grape using improved YOLOv9s and adaptive Kalman filter

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lyu2025counting` |
| Judul asli | Counting bagging grape using improved YOLOv9s and adaptive Kalman filter |
| Penulis | Lyu, J.; others |
| Tahun | 2025 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [lyu2025counting.pdf](../pdf/lyu2025counting.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202412026

## Gambaran Umum

Makalah ini mengusulkan metode penghitungan anggur berkantong (*bagged grape*) dari video yang terdiri atas tiga komponen: detektor YOLOv9s yang dimodifikasi (ES-YOLOv9s), algoritma pelacakan berbasis filter Kalman adaptif (*adaptive Kalman filter tracking*, AKFT) yang dibangun di atas ByteTrack, dan penghitungan dengan garis virtual (*line-drawing counting*). Pada penghitungan garis, jumlah bertambah satu saat titik pusat kotak buah yang dilacak melewati garis hitung.

Data dikumpulkan di taman demonstrasi teknologi PaiDengTe, Distrik Bishan, Chongqing, Tiongkok, dengan ponsel OPPO Reno6pro+ dan Redmi K40 pada 22 Juli 2022 dan 1 September 2023. Terkumpul 700 citra resolusi tinggi dan 6 video (1920 × 1080 piksel, 30 bingkai/detik, sekitar 20 detik per video). Makalah ditulis dalam bahasa Mandarin dengan abstrak berbahasa Inggris.

Hasil utama: ES-YOLOv9s mencapai AP 96,9% dan *recall* 93,1% pada 70 bingkai/detik, dengan parameter berkurang 29,6% dibandingkan YOLOv9s. AKFT memperoleh HOTA 58,6%, MOTA 63,6%, dan IDF1 78,8%. Rerata akurasi hitungan terhadap hitungan manual pada enam video adalah 80,0%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penaksiran hasil panen anggur memerlukan hitungan buah yang akurat. Penulis menyatakan bahwa metode berbasis citra tunggal hanya mencakup bidang pandang terbatas dan tidak dapat meliputi seluruh pohon. Pelacakan pada video dipakai untuk mengatasinya, tetapi penulis mengidentifikasi tiga masalah pada penghitungan anggur berkantong: (1) model deteksi yang ada berfokus pada ketelitian dan mengabaikan kebutuhan waktu-nyata pada perangkat terbatas; (2) anggur yang dikantongi berukuran lebih besar dan saling menutupi atau tertutup daun sehingga sulit dideteksi; (3) guncangan perangkat pemotret dan gerakan cepat menimbulkan derau deteksi yang menurunkan ketepatan prediksi lintasan oleh filter Kalman.

## Ide Utama

Pertama, modul EFEM (*efficient feature enhancement module*) berbasis FasterNet menggantikan modul RepNCSPELAN4 pada YOLOv9s agar parameter dan komputasi berkurang, ditambah modul perhatian SEAM (*spatially enhanced attention module*) untuk memperbaiki deteksi buah tertutup. Kedua, matriks kovarians derau pengukuran pada filter Kalman dibuat bergantung pada skor keyakinan deteksi, sehingga deteksi berkeyakinan tinggi berbobot lebih besar pada tahap pembaruan. Ketiga, penghitungan memakai garis virtual pada lintasan yang telah diberi ID unik.

Persamaan 3 pada makalah menyatakan derau yang diperbarui sebagai $\tilde{N}_t = (1 - C_t) N_t$, dengan $C_t$ skor keyakinan kotak deteksi dan $N_t$ matriks kovarians derau.

## Cara Kerja Langkah demi Langkah

```
 Video --> bingkai --> ES-YOLOv9s --> AKFT (ByteTrack + KF adaptif)
                                          |
                                          v
                              ID unik per buah --> garis hitung
```

### 1. Akuisisi dan penyiapan data

Pemotretan dilakukan pada pagi, siang, dan sore, dari sudut depan, atas, bawah, dan samping, dengan peneliti berjalan menyusuri baris tanam. Citra berukuran 4.000 × 3.000 dan 4.096 × 3.072 piksel. Sebanyak 700 citra dibagi acak 7:2:1 menjadi 490 latih, 140 validasi, dan 70 uji. Augmentasi pada data latih (derau Gaussian, pembalikan, cermin, perubahan saturasi dan kecerahan) menambah data latih menjadi 2.100 citra. Citra dianotasi dengan Make Sense dalam format YOLO. Enam video dianotasi per bingkai dengan DarkLabel dan dipakai untuk menguji penghitungan. Kultivar anggur tidak dilaporkan.

### 2. Detektor ES-YOLOv9s

YOLOv9s dipilih karena PGI (*programmable gradient information*) mengatasi hambatan informasi pada jaringan dalam. EFEM memakai FasterNet dengan konvolusi parsial (PConv) yang hanya memproses sebagian kanal, diikuti dua konvolusi 1×1, normalisasi batch, ReLU, dan sambungan residual. SEAM memakai modul campuran kanal-spasial (CSMM) pada pembagian blok 6×6, 7×7, dan 8×8, konvolusi *depthwise* 3×3 dengan sambungan residual, konvolusi *pointwise* 1×1, dan jaringan terhubung penuh dua lapis; keluarannya dikalikan dengan peta fitur asli sebagai bobot perhatian. Pelatihan memakai laju belajar awal 0,01, 700 epoch, dan ukuran batch 32 pada GPU NVIDIA RTX 4060 Ti 16 GB.

### 3. Pelacakan AKFT

Dasarnya adalah ByteTrack, yang melakukan asosiasi dua tahap: deteksi berkeyakinan tinggi dicocokkan lebih dahulu dengan prediksi lintasan, lalu deteksi berkeyakinan rendah dicocokkan dengan lintasan yang belum cocok. Prediksi lintasan memakai filter Kalman. Modifikasi penulis adalah derau pengukuran adaptif sesuai Persamaan 3. Deteksi yang tidak cocok dengan lintasan mana pun diinisialisasi sebagai lintasan baru atau dihapus bila skornya di bawah ambang. Penulis tidak memakai fitur tampilan; asosiasi bertumpu pada gerak dan posisi kotak.

### 4. Penghitungan garis

Saat titik pusat kotak anggur yang dilacak menyentuh garis hitung, jumlah bertambah satu. Posisi garis dan aturan arah lintasan tidak dijelaskan lebih rinci pada teks.

## Eksperimen dan Hasil

### Deteksi (Tabel 1 dan 2)

| Model | P (%) | R (%) | AP (%) | FPS |
|---|---|---|---|---|
| YOLOv5s | 95,1 | 90,7 | 96,0 | 35 |
| YOLOv7-tiny | 95,2 | 92,7 | 95,2 | 26 |
| YOLOv8s | 89,3 | 89,5 | 94,0 | 62 |
| YOLOv9s | 98,5 | 87,4 | 96,9 | 51 |
| YOLOv10s | 93,6 | 87,2 | 93,3 | 65 |
| ES-YOLOv9s | 95,3 | 93,1 | 96,9 | 70 |

Pada ablasi (Tabel 2), YOLOv9s memiliki 9,8 M parameter dan 39,9 G FLOPs; ES-YOLOv9s memiliki 6,9 M parameter dan 29,0 G FLOPs. EFEM saja menurunkan parameter menjadi 6,6 M dan menaikkan FPS menjadi 70; SEAM saja menurunkan seluruh metrik dan FPS menjadi 46. Teks menyebut penurunan parameter 29,6%, penurunan FLOPs 10,9 G, kenaikan FPS 20, dan kenaikan *recall* 5,7 poin persentase.

### Pelacakan (Tabel 3)

| Metode | HOTA (%) | MOTA (%) | IDF1 (%) | IDSW | AFPS |
|---|---|---|---|---|---|
| Sort | 51,0 | 59,9 | 67,8 | 13 | 35 |
| DeepSort | 51,5 | 58,1 | 71,5 | 17 | 27 |
| DeepMot | 39,4 | 54,3 | 44,4 | 28 | 30 |
| UAVmot | 53,5 | 59,9 | 75,4 | 3 | 37 |
| ByteTrack | 54,3 | 61,4 | 76,3 | 3 | 35 |
| NMS-ByteTrack | 57,0 | 60,0 | 70,0 | 0 | 22 |
| AKFT | 58,6 | 63,6 | 78,8 | 6 | 35 |

Ablasi pelacakan (Tabel 4) menunjukkan bahwa filter Kalman adaptif saja meningkatkan HOTA, MOTA, dan IDF1 ByteTrack masing-masing 1,5, 1,6, dan 1,4 poin persentase serta menurunkan IDSW dari 3 menjadi 1. Kombinasi lengkap menghasilkan IDSW 6. Pada Tabel 3, IDSW AKFT (6) lebih tinggi daripada ByteTrack (3), UAVmot (3), dan NMS-ByteTrack (0); teks tidak membahas hal ini.

### Penghitungan (Tabel 5)

Hitungan manual dilakukan oleh dua peneliti secara independen dengan menonton video per bingkai, lalu dirata-ratakan.

| Metode | Video 1 | Video 2 | Video 3 | Video 4 | Video 5 | Video 6 | Rerata akurasi |
|---|---|---|---|---|---|---|---|
| Hitungan manual | 22 | 7 | 22 | 11 | 13 | 19 | tidak ada |
| Hitungan garis | 18 | 7 | 11 | 10 | 9 | 17 | 80,0% |

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: detektor lebih ringan dan cepat tanpa penurunan AP dibandingkan YOLOv9s; filter Kalman adaptif memperbaiki kotak prediksi pada kondisi tertutup (Gambar 8); dan seluruh metode berjalan dalam waktu-nyata (70 bingkai/detik untuk deteksi, AFPS 35 untuk pelacakan).

Keterbatasan yang dinyatakan penulis: penelitian hanya mencakup anggur berkantong, dengan rencana perluasan ke buah lain; aspek keringanan model, kemudahan penggunaan, dan kekokohan algoritma masih dapat ditingkatkan.

Menurut pembacaan ringkasan ini: (a) hanya enam video pendek (sekitar 20 detik) yang diuji, dengan hitungan manual 7 sampai 22 buah per video, sehingga bukti penghitungan sangat terbatas; (b) pada Video 3 hitungan garis adalah 11 terhadap 22 manual, sehingga akurasi rerata menyembunyikan penghitungan kurang yang besar; (c) cara akurasi 80,0% dihitung tidak dijelaskan di teks; (d) penghitungan garis bergantung pada lintasan tanpa fitur tampilan, sehingga buah yang kehilangan lintasan lalu muncul kembali dapat dihitung ulang atau terlewat; (e) tidak ada hitungan per kelas.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang tampak pada banyak bingkai video dengan pelacakan multi-objek: filter Kalman untuk prediksi lintasan dan asosiasi dua tahap ByteTrack, lalu penghitungan buah sekali saat lintasannya melewati garis. Identitas dipertahankan hanya dalam urutan waktu satu video yang menyusuri baris tanam; tidak ada pencocokan antar-pandangan terpisah atau antar-sisi pohon. Hitungan tidak dilaporkan per kelas. Acuannya adalah hitungan manual per video oleh dua peneliti, bukan panen.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah gagasan pembobotan derau pengukuran oleh skor keyakinan deteksi dan pola pelacakan dua tahap. Mekanisme garis hitung tidak langsung berlaku bagi citra statis dari beberapa sisi pohon karena menuntut lintasan kontinu. Hasil hitungan yang kurang (Video 3: 11 terhadap 22) menunjukkan risiko lintasan terputus akibat oklusi.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `lyu2025counting`.

Lyu dan Ran (2025) mengusulkan penghitungan anggur berkantong dari video dengan detektor YOLOv9s yang dimodifikasi (EFEM dan SEAM), pelacak ByteTrack dengan filter Kalman adaptif yang menyesuaikan derau menurut skor keyakinan deteksi, dan penghitungan garis virtual. Pelacak memperoleh HOTA 58,6%, MOTA 63,6%, dan IDF1 78,8%, dan hitungan garis mencapai rerata akurasi 80,0% terhadap hitungan manual pada enam video.

Catatan verifikasi data: makalah berbahasa Mandarin (abstrak Inggris tersedia) dan diringkas dari teks Mandarin; ekstraksi teks terbaca baik, sebagian rumus berantakan tetapi dapat dipahami dari uraian. Angka deteksi ada pada Tabel 1 dan 2, pelacakan pada Tabel 3 dan 4, hitungan pada Tabel 5, dan jumlah data pada Bagian 1.1 dan 1.2. Persentase 29,6% diambil dari teks (Tabel 2 menunjukkan 9,8 M ke 6,9 M). Cara perhitungan akurasi 80,0% tidak dapat diverifikasi dari teks. Kultivar, jumlah buah pada anotasi video, dan posisi garis hitung tidak dilaporkan.
