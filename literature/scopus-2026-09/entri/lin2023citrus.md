## Gambaran Umum
Makalah ini (Lin, Hu, Zheng, dan Xiong; *Agronomy* 2023, 13, 1674) mengusulkan metode pencacahan jeruk (*citrus*) pada video kebun dengan detektor YOLOv5s yang ditingkatkan dan pelacak DeepSort. Peningkatan detektor terdiri atas tiga perubahan: modul atensi CBAM ditambahkan sebelum lapisan SPPF pada tulang punggung, semua modul C3 pada tulang punggung diganti modul *Contextual Transformer* (CoT), dan fungsi kerugian diganti dari CIoU/GIoU menjadi SIoU.

Data berupa 1.940 citra jeruk berukuran 640 x 480 piksel dari kebun jeruk South China Agricultural University, Guangzhou, yang diambil pada 3 Juli 2022 dan 20 Desember 2022 pada pukul 9.00 sampai 20.00 dengan jarak kamera ke batang pohon 1 sampai 2 m dari berbagai sudut. Detektor yang ditingkatkan mencapai *average precision* (AP) 95,26% dibandingkan 91,75% pada YOLOv5s awal (selisih 3,51 poin persentase). Pada sepuluh video, rerata *Multiple Object Tracking Accuracy* (MOTA) DeepSort naik dari 88,95% menjadi 90,83%.

Hasil dilaporkan sebagai akurasi pelacakan (MOTA), bukan galat hitungan terhadap jumlah buah sebenarnya. Penulis menyatakan algoritma tidak membedakan kematangan buah dan kecepatannya menurun.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil buah pada pohon selama masa tumbuh dibutuhkan untuk pengelolaan kebun dan perencanaan penanaman serta pemasaran jeruk. Metode deteksi klasik, menurut penulis, terbatas oleh oklusi daun dan ranting, pencahayaan, dan kompleksitas serta biaya (misalnya kamera RGB-D). Pada tahap pencacahan, algoritma SORT mengalami perpindahan ID yang sering dan hanya cocok tanpa oklusi, sedangkan oklusi oleh ranting dan daun lazim terjadi pada jeruk. DeepSort menambahkan kaskade pencocokan untuk mengurangi perpindahan ID pada oklusi berulang.

Detektor YOLOv5s dasar, menurut penulis, mengalami deteksi terlewat pada objek tertutup dan deteksi keliru pada objek latar. Karena itu penulis meningkatkan detektor agar tangguh terhadap oklusi dan pencahayaan sambil menjaga sifat waktu nyata.

## Ide Utama
Gagasan utamanya adalah meningkatkan kualitas deteksi jeruk pada kondisi oklusi dan pencahayaan sulit sehingga hasil pelacakan DeepSort dan pencacahan ikut membaik. CBAM memfokuskan fitur pada buah dan mengabaikan ranting dan daun. Modul CoT menambah kemampuan pemodelan kontekstual global dengan mengagregasi konteks dari kunci (*key*) bertetangga. SIoU menambahkan sudut vektor antara kotak prediksi dan kotak target dalam fungsi kerugian untuk memperbaiki lokalisasi dan mempercepat konvergensi.

Pencacahan dilakukan dengan menjalankan pelacak pada deteksi tiap bingkai video: deteksi baru yang tidak cocok dengan lintasan yang ada mendapat ID baru, sedangkan deteksi yang cocok mempertahankan ID-nya sehingga buah yang sama pada bingkai berbeda tidak dihitung ulang.

## Cara Kerja Langkah demi Langkah
```
 [ Video kebun ] -> [ YOLOv5s + CBAM + CoT + SIoU ]
     -> [ kotak dan fitur ] -> [ DeepSort ] -> [ ID unik -> hitungan ]
```

### 1. Akuisisi dan penyusunan data
Citra diambil di kebun jeruk universitas (113° BT, 23° LU) pada dua tanggal. Jarak kamera 1 sampai 2 m dari batang pohon dan buah dipotret dari berbagai sudut. Total 1.940 citra JPG beresolusi 640 x 480 piksel, dibagi acak 8:1:1 menjadi data latih, validasi, dan uji. Anotasi memakai LabelImg; augmentasi *Mosaic* dan penskalaan adaptif diterapkan otomatis pada data latih. Jumlah pohon, kultivar, dan jumlah kotak anotasi tidak dilaporkan.

### 2. Peningkatan YOLOv5s
Model dasar adalah YOLOv5s (empat bagian: masukan, tulang punggung, leher, keluaran). Tiga peningkatan: (a) CBAM, gabungan atensi kanal dan spasial, disisipkan sebelum lapisan SPPF; (b) CoT mengganti semua modul C3 pada tulang punggung; (c) SIoU menggantikan fungsi kerugian kotak (*bounding box*) YOLOv5 yang semula CIoU, dengan komponen kerugian jarak yang memuat sudut dan kerugian bentuk.

### 3. Pelacakan DeepSort
SORT memakai filter Kalman untuk memprediksi posisi kotak dan algoritma Hungaria untuk pencocokan IoU. DeepSort menambah *Matching Cascade* dengan matriks biaya dari jarak Mahalanobis dan jarak kosinus terhadap vektor fitur (set vektor fitur 100 bingkai terakhir). Deteksi yang tidak cocok dianggap target baru dan memperoleh ID baru. Alur: detektor dilatih, bingkai video dideteksi, kotak dan fitur dimasukkan ke DeepSort, jarak dihitung, dicocokkan dengan algoritma Hungaria, lalu filter Kalman diperbarui.

### 4. Pengaturan eksperimen
Windows 10, CPU Intel i7-10875H, GPU NVIDIA GeForce RTX 2060, Python 3.7.0, PyTorch 1.12.0, CUDA 11.3. Ukuran masukan 640 x 640, laju belajar 0,01, *batch* 16, momentum 0,9, 300 putaran pelatihan. Metrik detektor: presisi, *recall*, FPS, AP; metrik pelacakan: MOTA.

## Eksperimen dan Hasil
Studi ablasi (Tabel 1) membandingkan YOLOv5s dengan tiap peningkatan tunggal, kombinasi berpasangan, dan seluruh peningkatan. Perbandingan algoritma (Tabel 2) memakai kumpulan data yang sama. Evaluasi pelacakan memakai sepuluh video (Tabel 3), dengan MOTA sebelum dan sesudah peningkatan detektor.

| Algoritma (Tabel 1 dan 2) | Presisi | *Recall* | AP | FPS |
|---|---|---|---|---|
| YOLOv5s | 87,42% | 86,04% | 91,75% | 86 |
| YOLOv5s + CBAM | 90,58% | 83,75% | 92,66% | 82 |
| YOLOv5s + SIoU | 89,07% | 87,87% | 92,99% | 90 |
| YOLOv5s + CotNet | 88,47% | 86,01% | 93,28% | 85 |
| YOLOv5s + SIoU + CotNet | 90,84% | 89,70% | 94,77% | 89 |
| YOLOv5s yang ditingkatkan (ketiganya) | 91,21% | 90,25% | 95,26% | 84 |
| YOLOv3-SPP | 90,13% | 90,52% | 87,25% | 80 |
| YOLOv3-Tiny | 86,35% | 88,84% | 80,83% | 104 |
| YOLOv4-Tiny | 85,76% | 88,29% | 90,32% | 110 |

Ukuran model yang ditingkatkan adalah 17,8 MB dibandingkan 13,7 MB pada YOLOv5s. Gabungan CBAM dengan CotNet menurunkan AP menjadi 92,50% (lebih rendah 0,16 poin daripada peningkatan tunggal terkecil). Kombinasi CBAM + SIoU memberi AP 94,11%.

Pada Tabel 3, MOTA rerata naik dari 88,95% menjadi 90,83% (selisih 0,88 poin persentase menurut teks; selisih 1,88 bila dihitung dari kedua angka tersebut, lihat catatan verifikasi). Peningkatan MOTA tidak seragam: pada video 2 (89,62% menjadi 89,25%) dan video 8 (91,31% menjadi 90,69%) MOTA justru menurun. Kecepatan keseluruhan (Tabel 4): YOLOv5s + DeepSort 78 FPS dan versi yang ditingkatkan 72 FPS.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: AP detektor naik 3,51 poin persentase, model tetap ringan dan waktu nyata, serta pelacakan lebih baik pada oklusi.

Keterbatasan yang dinyatakan penulis: kecepatan deteksi menurun setelah peningkatan; algoritma tidak membedakan kematangan buah sehingga estimasi hasil sebenarnya belum akurat; deteksi objek kecil belum dioptimalkan.

Menurut pembacaan ringkasan ini, pencacahan dinilai dengan MOTA, yang menggabungkan deteksi terlewat, deteksi keliru, dan perpindahan ID, tanpa galat hitungan terhadap jumlah buah nyata per video atau pohon; jumlah dan panjang video tidak dilaporkan. Kumpulan data berasal dari satu kebun universitas dengan satu kelas (jeruk). Pembanding detektor (Tabel 2) tidak memuat YOLOv5s tanpa peningkatan dengan variasi lain di luar famili YOLO ringan. Selisih MOTA per video berfluktuasi, dengan dua video menurun.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak pada banyak bingkai video dengan mekanisme pelacakan-berdasarkan-deteksi: deteksi YOLOv5s yang ditingkatkan dimasukkan ke DeepSort, yang memakai filter Kalman, jarak Mahalanobis, dan kemiripan fitur tampilan untuk mempertahankan ID melewati oklusi. Penyatuan identitas dilakukan hanya sepanjang urutan waktu pada satu video; penyatuan lintas sisi atau lintas pohon tidak dibahas, meski penulis menyebut buah difoto dari berbagai sudut saat pengambilan citra latih.

Hitungan tidak dilaporkan per kelas (hanya satu kelas, jeruk, tanpa kematangan). Acuan evaluasi pelacakan adalah MOTA, bukan hasil panen atau hitung manual di lapangan; jumlah acuan tidak dilaporkan pada teks. Yang dapat dipindahkan ke pencacahan tandan sawit adalah pola detektor dan DeepSort dengan penanganan oklusi oleh ranting dan daun, serta ukuran MOTA yang secara eksplisit menghitung perpindahan ID. Penulis sendiri menyatakan bahwa kematangan belum dibedakan, yang relevan dengan kebutuhan inventaris per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `lin2023citrus`.

Lin dkk. memadukan YOLOv5s yang ditingkatkan (CBAM, modul *Contextual Transformer*, dan fungsi kerugian SIoU) dengan DeepSort untuk mencacah jeruk pada video kebun. AP detektor naik dari 91,75% menjadi 95,26% pada 1.940 citra dari satu kebun, dan MOTA rerata pada sepuluh video naik dari 88,95% menjadi 90,83%; kematangan buah tidak dibedakan dan kecepatan deteksi menurun.

Catatan verifikasi data: angka detektor tertulis pada Tabel 1 (ablasi) dan Tabel 2 (perbandingan); MOTA per video pada Tabel 3; FPS keseluruhan pada Tabel 4; data pada Seksi 2.1 dan 2.2; pengaturan pada Seksi 5.1. Teks ekstraksi terbaca baik, tetapi gambar tidak terbaca. Teks menulis peningkatan MOTA sebesar 0,88 poin persentase sementara 90,83% dikurangi 88,95% adalah 1,88 poin (dihitung dalam ringkasan ini); angka manakah yang benar tidak dapat ditentukan dari teks. Keterangan di akhir makalah menyatakan CBAM sebagai "Cost Benefit Analysis Method" yang keliru terhadap isi makalah; ringkasan ini mengikuti uraian Seksi 3.2.1 (*Convolutional Block Attention Module*). Jumlah pohon, kultivar, jumlah video, dan jumlah buah acuan tidak dilaporkan.
