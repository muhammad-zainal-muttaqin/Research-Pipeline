# Real-Time Fruit Detection and Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `issad2025real` |
| Judul asli | Real-Time Fruit Detection and Counting |
| Penulis | Issad, Hassina Ait; Lakef, Massyl; Boucherk, Salim; Chemoun, Karima; Oubabas, Sarah; Aoudjit, Rachida |
| Tahun | 2025 |
| Venue | Icrami 2025 2025 International Conference on Recent Advances in Mathematics and Informatics |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [issad2025real.pdf](../pdf/issad2025real.pdf)
- DOI resmi: https://doi.org/10.1109/icrami64946.2025.11472714

## Gambaran Umum
Makalah konferensi ini (Ait Issad dkk., ICRAMI 2025) mengusulkan sistem deteksi dan pencacahan buah waktu nyata yang menggabungkan detektor YOLOv8 dengan pelacak multi-objek (*multi-object tracking*, MOT) ByteTrack. Sistem diterapkan pada 20 kelas buah (jenis buah, bukan tingkat kematangan) dan menghitung buah yang melintasi garis maya pada video berdasarkan arah lintasan. Tanaman yang dicakup beragam, antara lain apel, pir, pisang, jeruk, mangga, dan anggur, sehingga bukan kebun satu komoditas.

Data pelatihan adalah 746 citra JPG yang dikumpulkan dari kebun, pasar buah dan sayur, Kaggle, iStock, dan pencarian Google. Setelah augmentasi, kumpulan data mencapai 1.792 sampel yang dibagi menjadi 1.569 citra latih, 153 citra validasi, dan 70 citra uji. Pada validasi, detektor mencapai mAP@0,5 sebesar 0,942 (94,2%), *recall* 0,876, dan presisi 0,915. Pencacahan dievaluasi pada lima video dengan acuan hitung manual: total 28 buah secara manual dan 21 buah terprediksi, dengan akurasi 75,33% dan *mean absolute percentage error* (MAPE) 24,66%.

Penulis sendiri menyatakan akurasi pencacahan masih sederhana dan menempatkan penguatan MOT serta identifikasi ulang (*re-identification*) sebagai pekerjaan lanjutan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan buah secara manual dinilai lambat dan rawan galat. Penulis membedakan pencacahan berbasis regresi dan berbasis deteksi, dan merujuk bahwa yang kedua dianggap lebih efektif. Deteksi buah di lingkungan tumbuh sulit karena latar kompleks, perubahan cahaya, dan cuaca, sehingga metode berbasis warna, bentuk, atau transformasi *wavelet* dinilai belum memadai.

Penulis menyatakan bahwa studi yang menggabungkan pelacakan multi-objek dengan detektor *deep learning* untuk pencacahan buah masih sedikit dan umumnya hanya untuk satu jenis buah. Penelitian ini menjawab celah tersebut dengan mencakup 20 jenis buah dalam satu sistem.

## Ide Utama
Gagasan utamanya adalah memakai detektor YOLOv8 yang dilatih pada 20 kelas buah, lalu menautkan deteksi antarbingkai video dengan ByteTrack agar setiap buah memperoleh satu identitas pelacakan dan dihitung satu kali. Penghitungan dilakukan oleh alat *line counter* pustaka Supervision: buah yang melintasi garis acuan menaikkan penghitung masuk (*in*) atau keluar (*out*) sesuai arah geraknya.

Dua kontribusi yang dinyatakan penulis adalah (1) kumpulan data citra buah dengan variasi iluminasi dan latar kompleks yang dikumpulkan dan dianotasi, dan (2) penggabungan YOLOv8 dan ByteTrack untuk mendeteksi dan menghitung 20 jenis buah.

## Cara Kerja Langkah demi Langkah
```
 [ Pengumpulan citra ] -> [ Anotasi, praproses, augmentasi ]
        -> [ Pelatihan YOLOv8 ] -> [ Validasi dan uji ]
        -> [ ByteTrack + line counter pada video ]
```

### 1. Akuisisi data
Citra dikumpulkan dari kebun, pasar buah dan sayur, dua basis data (Kaggle dan iStock), dan mesin pencari Google; total 746 citra JPG dalam 20 kelas. Video dan citra tambahan direkam dengan ponsel POCO X4 Pro berkamera sudut lebar 108 megapiksel. Lokasi, kultivar, dan jumlah pohon tidak dilaporkan.

### 2. Anotasi, praproses, dan augmentasi
Anotasi memakai alat Annotate Roboflow dan disimpan dalam format YOLO. Citra diubah ukurannya menjadi 640 x 640 piksel dengan orientasi otomatis. Augmentasi meliputi pembalikan, rotasi, perubahan kecerahan, konversi skala abu-abu, dan pengaburan. Hasilnya 1.792 sampel yang dibagi menjadi 1.569, 153, dan 70 citra untuk latih, validasi, dan uji.

### 3. Pelatihan YOLOv8
YOLOv8 (tanpa *anchor*; tulang punggung CSPDarknet-53 yang dimodifikasi, leher PAN-FPN) dilatih di Google Colab dengan GPU NVIDIA T4. Hiperparameter pada Tabel I: 100 *epoch*, laju belajar 0,001, *patience* 50 *epoch*, ambang IoU 0,7, ukuran citra 640, ukuran *batch* 16. Varian ukuran model YOLOv8 tidak dilaporkan pada teks.

### 4. Pelacakan dan pencacahan
ByteTrack menautkan setiap buah terdeteksi pada satu bingkai dengan posisinya pada bingkai berikutnya sehingga tiap buah dihitung satu kali walau bergerak antarbingkai. Penghitung garis dari pustaka Supervision menambah hitungan buah yang melintasi garis maya sesuai arahnya.

## Eksperimen dan Hasil
Detektor dievaluasi pada set validasi dan set uji; pencacahan dievaluasi pada lima video dengan acuan hitung manual. Pembanding kuantitatif terhadap metode lain tidak disajikan; penulis hanya menyatakan hasilnya kompetitif dibanding studi terdahulu yang berfokus pada satu jenis buah, dan perbandingan dengan alur lain seperti YOLOv7 + DeepSORT dijadwalkan sebagai pekerjaan lanjutan.

| Hasil | Nilai |
|---|---|
| mAP@0,5 semua kelas (Tabel II dan III) | 0,942 |
| mAP@0,5-0,95 semua kelas | 0,872 (Tabel II) dan 0,877 (Tabel III) |
| Presisi, *recall* semua kelas (Tabel III) | 0,915; 0,876 |
| Uji 70 citra | 68 dari 70 citra diklasifikasikan dan dideteksi dengan benar |
| Pencacahan lima video (Tabel IV) | manual 28, prediksi 21, selisih 7 |
| MAPE dan akurasi pencacahan | 24,66% dan 75,33% |

Rincian per video (Tabel IV), berturut-turut hitung manual, prediksi, selisih: video 1: 10, 6, 4; video 2: 3, 1, 2; video 3: 4, 4, 0; video 4: 5, 5, 0; video 5: 6, 5, 1. Untuk kelas, AP terendah pada mAP@0,5 adalah Apricot (0,821) dan Strawberry (0,820); recall terendah adalah Apricot (0,417). Matriks konfusi (Gambar 5) menunjukkan sebagian buah salah dikelompokkan sebagai latar belakang (8% untuk Apricot hingga 21% untuk Grape) dan kebingungan kecil antara Peach dan Apple serta Kiwi dengan Pear dan Peach. Galat contoh pada Gambar 8 adalah Peach yang diklasifikasikan sebagai Apple dan buah tersembunyi di belakang buah lain yang tidak terdeteksi.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: cakupan 20 jenis buah pada latar dan pencahayaan beragam, kecepatan waktu nyata, dan detektor yang akurat pada set validasi.

Keterbatasan yang dinyatakan penulis: akurasi pencacahan masih sederhana (75,33%); buah sulit dideteksi saat tersembunyi di belakang daun, saat oklusi, atau terlalu berdekatan; buah serupa dan pencahayaan kompleks masih menantang. Pekerjaan lanjutan yang disebutkan meliputi perluasan data, evaluasi lintas domain (kebun, pasar, lapangan), penguatan MOT dan identifikasi ulang, perbandingan dengan YOLOv7 + DeepSORT dan metode regresi, serta integrasi dengan drone.

Menurut pembacaan ringkasan ini, pencacahan hanya diuji pada lima video yang berisi 28 buah dalam total, dan contoh video di teks berlatar sederhana dengan empat jenis buah, sehingga kesimpulan tentang kondisi kebun nyata terbatas. Citra latih sebagian berasal dari internet dan pasar, bukan kebun tanaman utuh, sehingga kesesuaian dengan kanopi pohon tidak terbukti. Detektor dievaluasi pada kumpulan data yang kecil (70 citra uji), dan penulis menampilkan perbedaan angka antara teks dan tabel (lihat catatan verifikasi). Penghitungan garis hanya mencegah hitungan ganda dalam satu aliran video dan tidak menyelesaikan identitas buah yang sama pada pandangan berbeda.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak pada beberapa bingkai video dalam satu aliran, dengan mekanisme pelacakan-berdasarkan-deteksi (*tracking-by-detection*) memakai ByteTrack. Identitas dipertahankan lewat asosiasi deteksi antarbingkai berurutan, dan pencacahan dilakukan dengan penghitung garis maya yang membedakan arah masuk dan keluar. Tidak ada mekanisme untuk menyatukan identitas buah yang sama pada sudut pandang atau sisi objek berbeda, dan makalah tidak membahas oklusi lintas-sisi.

Hitungan tidak dilaporkan per kelas pada tahap pencacahan; hanya total per video yang dilaporkan, meskipun detektor mengenali 20 kelas. Acuan hitung adalah hitung manual pada video (Tabel IV), bukan hasil panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pola dasar detektor ditambah pelacak, tetapi hasil makalah ini (akurasi 75,33% pada lima video sederhana) tidak memberikan bukti bahwa pola itu mengatasi identitas lintas sisi pohon; penulis sendiri menyebut perlunya strategi MOT dan identifikasi ulang yang lebih kuat.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `issad2025real`.

Ait Issad dkk. menggabungkan YOLOv8 dan ByteTrack untuk mendeteksi dan menghitung 20 jenis buah pada video, dengan penghitung garis maya yang memperhitungkan arah gerak. Detektor mencapai mAP@0,5 sebesar 94,2% pada validasi, sedangkan pencacahan pada lima video menghasilkan akurasi 75,33% (MAPE 24,66%) terhadap hitung manual; penulis menyatakan akurasi pencacahan masih sederhana.

Catatan verifikasi data: mAP, presisi, dan *recall* tertulis pada Tabel II dan III serta abstrak; hasil pencacahan pada Tabel IV; pembagian data pada Seksi II-D; hiperparameter pada Tabel I. Teks ekstraksi terbaca baik, tetapi gambar tidak terbaca. Terdapat ketidakkonsistenan pada makalah: abstrak menyebut *recall* 87,6% sedangkan teks menyebut mAP50-95 87,2% pada Tabel II dan 0,877 pada Tabel III; teks juga menyebut peningkatan validasi "0,005% dan 0,001%" tanpa rujukan angka dasar yang jelas. Akurasi 75,33% sesuai dengan 100% dikurangi MAPE 24,66% dan agak berbeda dari 21/28 (75%). Varian ukuran YOLOv8, lokasi kebun, kultivar, dan jumlah video selain lima tidak dilaporkan.
