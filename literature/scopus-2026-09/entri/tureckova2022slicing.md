# Slicing aided large scale tomato fruit detection and counting in 360-degree video data from a greenhouse

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tureckova2022slicing` |
| Judul asli | Slicing aided large scale tomato fruit detection and counting in 360-degree video data from a greenhouse |
| Penulis | Ture\vckov\'a, Al\vzb\veta; Ture\vcek, Tom\'a\vs; Jank\ru, Peter; Va\vracha, Pavel; \vSenke\vr\'\ik, Roman; Ja\vsek, Roman; Psota, V\'aclav; \vSt\vep\'anek, Vit; Kom\'\inkov\'a Oplatkov\'a, Zuzana |
| Tahun | 2022 |
| Venue | Measurement Journal of the International Measurement Confederation |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [tureckova2022slicing.pdf](../pdf/tureckova2022slicing.pdf)
- DOI resmi: https://doi.org/10.1016/j.measurement.2022.111977

## Gambaran Umum
Makalah ini mengusulkan proses otomatis untuk mendeteksi dan menghitung buah tomat di rumah kaca tanpa intervensi manusia. Kamera 360 derajat dipasang pada troli rumah kaca, dan video yang dihasilkan diubah menjadi satu citra panorama lebar yang memuat seluruh baris tanaman. Citra tersebut dipotong menjadi tambalan (*patch*) yang saling tumpang tindih, dideteksi dengan Faster R-CNN, lalu prediksi dijahit kembali dengan inferensi berbantuan irisan (*slicing-aided inference*, pustaka SAHI). Karena setiap buah tampak hanya satu kali pada citra panorama, pelacakan antarbingkai tidak diperlukan.

Data dikumpulkan di rumah kaca hidroponik Farma Bezdínek (Dolní Lutyně, Republik Ceko) pada 2020 dan 2021 untuk tomat *cherry* (10–12 g/buah) dan *cocktail* (35–45 g/buah). Pada set uji, penjahitan dengan pengaturan terbaik menghasilkan F1 sebesar 83,09%, presisi 82,12%, dan recall 84,08%. Selisih absolut antara jumlah acuan dan jumlah deteksi hanya 2,32% dari jumlah tomat acuan, meskipun hal itu terjadi karena positif palsu dan negatif palsu saling menutupi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkiraan panen tomat rumah kaca umumnya bergantung pada pengalaman agronom, dengan galat rerata sekitar 10–20 persen yang dapat berfluktuasi nyata. Kontrak pengiriman bergantung pada prakiraan panen mingguan, sehingga selisih prakiraan dapat menimbulkan kerugian komersial dan masalah logistik. Jumlah tomat yang tepat diharapkan memperbaiki prakiraan.

Penulis menyatakan bahwa deteksi pada bingkai video atau foto yang tumpang tindih memerlukan pengindeksan atau pelacakan agar buah tidak terhitung ganda. Lorong rumah kaca sempit sedangkan sebaran vertikal buah lebar, sehingga medan pandang vertikal kamera harus lebih dari 90 derajat. Pekerjaan terdahulu pada tomat rumah kaca (Mu dkk.) hanya menghitung pada citra tunggal sehingga buah di tepi tumpang tindih terhitung dua kali, sedangkan pendekatan pelacakan DeepSORT pada tomat ceri (Chen dan Lin) hanya mencapai IDF1 51,4%.

## Ide Utama
Gagasan utamanya adalah memindahkan masalah identitas dari tahap pelacakan ke tahap pembentukan citra: dengan mengambil irisan vertikal sempit tepat di depan kamera dari tiap bingkai video 360 derajat dan menyambungkannya, dihasilkan satu citra panorama baris tanaman tempat tiap buah muncul sekali dan tidak ada batas antarbingkai. Panorama yang sangat lebar kemudian diproses melalui irisan dan penjahitan, sehingga masalah identitas yang tersisa hanya berada pada tepi tambalan dan ditangani oleh penindasan atau penggabungan kotak prediksi.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Kamera Ricoh Theta Z1 merekam video 4K UHD (3840 × 2160) dan dipasang pada troli rumah kaca (Berkvens Control Lift) dengan kecepatan maksimum 5 km/ha (sebagaimana tertulis). Pemrosesan dipisahkan dari akuisisi. Dua pandangan fisheye 180 derajat dijahit menjadi proyeksi ekuirektangular, yang mencakup hampir 180 derajat vertikal dan kedua sisi lorong.

### 2. Pembuatan citra panorama
Video diuraikan menjadi bingkai, lalu irisan vertikal kecil tepat di depan kamera dipotong dari tiap bingkai dan disambung menjadi satu citra lebar. Distorsi bagian atas dan bawah dikompensasi secara matematis. Citra panorama berukuran tinggi 2.448 piksel dan lebar hingga 100.000 piksel (ukuran berkas lebih dari 350 MB).

### 3. Anotasi dan pembagian data
Anotasi poligon dibuat dengan LabelMe oleh beberapa orang dan divalidasi silang oleh ketua kelompok anotator, lalu diekspor ke format COCO. Terdapat 50 citra panorama: 35 latih, 7 validasi, 8 uji. Rerata ukuran objek setara persegi 42 piksel, dengan seluruh objek berukuran kecil atau sedang menurut kategori COCO. Set data tersedia atas permintaan.

### 4. Pengaturan irisan
Tiga pengaturan tambalan diuji, dengan masukan model 1333 × 735 piksel:
- resolusi rendah: tambalan 2448 × 4078 piksel diperkecil sekitar 9 kali;
- resolusi sedang: tambalan 1469 × 2448 piksel diperkecil sekitar 4 kali;
- resolusi tinggi: tambalan 1333 × 735 piksel pada resolusi asli.

Setelah pengirisan, jumlah citra latih + validasi adalah 95+20 (rendah), 311+67 (sedang), dan 1.240+264 (tinggi). Tambalan tumpang tindih dengan rasio 0,2 dari ukurannya.

### 5. Detektor
Faster R-CNN dengan *backbone* ResNet-50, bobot awal COCO, satu kelas. Pelatihan 20 epoch, SGD dengan laju belajar 0,02, momentum 0,9, peluruhan bobot 0,0001, laju belajar diturunkan sepuluh kali pada epoch 16 dan 19, *batch* 2 pada Titan XP, citra diubah ke 1333 × 800, augmentasi pembalikan acak berpeluang 0,5.

### 6. Penjahitan prediksi
Dibandingkan dua ukuran kecocokan (IoU dan *intersection over smaller area*, IOS) dan tiga algoritma pascapemrosesan: penindasan non-maksimum rakus (*greedy* NMS), penggabungan non-maksimum (NMM), dan NMM rakus. Ambang kecocokan yang diuji adalah 0,3; 0,5; 0,7; dan 0,9, serta ambang keyakinan model dari 0 sampai 0,99. Pustaka SAHI dipakai.

## Eksperimen dan Hasil
Evaluasi memakai presisi, recall, F1, laju penemuan palsu, laju negatif palsu, dan AP gaya COCO pada citra panorama utuh. Pemilihan pengaturan dilakukan pada set validasi (panorama utuh), lalu diuji pada set uji.

Hasil pemilihan parameter (Gambar 2 dan 3, Bagian 4.2): ukuran kecocokan terbaik IOS dengan ambang 0,5 untuk ketiga algoritma; kedua algoritma penggabungan (NMM dan NMM rakus) mengungguli NMS; ambang keyakinan 0,4 memberi galat jumlah terkecil dan merupakan titik presisi mulai melampaui recall. Pengaturan akhir: tambalan resolusi sedang, ambang keyakinan 0,4, IOS 0,5, NMM rakus. Resolusi rendah paling buruk karena objek kecil hilang saat pengecilan (AP dan AR untuk objek kecil nyaris nol sebelum penjahitan); resolusi sedang dan tinggi serupa, resolusi tinggi sedikit lebih baik sebelum penjahitan tetapi memerlukan sekitar lima kali lebih banyak tambalan. Pemrosesan resolusi rendah sekitar 13 kali lebih cepat daripada resolusi tinggi.

| Hasil akhir pada set uji (Bagian 4.3) | Nilai |
|---|---|
| F1 | 83,09% |
| Presisi | 82,12% |
| Recall | 84,08% |
| Laju penemuan palsu | 17,89% |
| Laju negatif palsu | 15,56% |
| Selisih jumlah deteksi terhadap acuan | 2,32% dari jumlah tomat acuan |
| AP pada IoU ≥ 0,75 | 0,396 |
| AP pada IoU ≥ 0,5 | 0,811 |
| AP setelah positif palsu latar dihapus | 0,871 |

Dalam perbandingan (Bagian 5), penulis menyatakan F1 mereka hanya 0,56% lebih rendah daripada Faster R-CNN ResNet-101 pada Mu dkk. (F1 83,67%) yang mengevaluasi hitungan pada citra tunggal sebelum penjahitan, dan memperingatkan bahwa dataset tiap makalah berbeda. YOLO-tomato melaporkan F1 93,91% pada citra tomat tunggal.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tidak memerlukan pelacakan; akuisisi sederhana dan terpisah dari pemrosesan; jumlah tepat satu baris utuh dapat dihitung; kajian parameter pascapemrosesan yang rinci; uji pada citra panorama utuh yang belum pernah dilihat model.

Keterbatasan yang dinyatakan penulis: tomat hijau kecil di bagian atas tanaman sulit dideteksi dan mudah tertukar dengan daun; tomat dan tanaman dari baris belakang kadang terlihat dan terdeteksi keliru (kesalahan paling umum pada tahap koreksi anotasi); kecepatan robot yang tidak seragam menimbulkan cacat citra; buah yang tertutup daun seluruhnya tidak dianotasi sehingga tidak masuk evaluasi; kesalahan dominan adalah lokalisasi yang tidak sempurna dan kebingungan latar.

Menurut pembacaan ringkasan ini, data hanya 50 panorama dari satu rumah kaca sehingga set uji (8 panorama) kecil, dan jumlah tomat acuan absolut tidak dapat dibaca dari teks. Penyatuan identitas sepenuhnya bergantung pada geometri akuisisi satu pandang lateral; pendekatan ini tidak dirancang untuk buah yang tampak dari beberapa sisi. Hitungan tidak dilaporkan per kelas (satu kelas).

## Kaitan dengan Tinjauan main6
Makalah ini menghindari buah yang terlihat lebih dari sekali dengan mencegahnya sejak akuisisi: irisan sempit dari video yang disambung menjadi panorama sehingga tiap buah tampak sekali. Identitas yang tersisa berada pada tepi tambalan inferensi dan ditangani dengan NMS atau penggabungan kotak berbasis IOS. Hitungan berasal dari jumlah deteksi akhir pada panorama, dengan satu kelas saja. Acuan hitungnya adalah anotasi citra panorama (poligon), bukan panen atau hitung lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan mengubah masalah lintas-bingkai menjadi satu representasi bersama sebelum deteksi, serta penelaahan parameter penjahitan (ukuran IOS lebih baik daripada IoU untuk kotak terpotong di tepi tambalan). Keterbatasannya: panorama baris lurus tidak berlaku untuk pohon sawit yang dipotret dari beberapa sisi, sehingga identitas lintas sisi tetap memerlukan mekanisme lain.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `tureckova2022slicing`.

Turečková dkk. (2022) mengusulkan pendeteksian dan pencacahan tomat rumah kaca dari citra panorama baris tanaman yang disusun dari video kamera 360 derajat, memakai Faster R-CNN ResNet-50 dengan inferensi berbantuan irisan (SAHI) dan penggabungan kotak pada tepi tambalan. Pada set uji berisi 8 citra panorama, pengaturan terbaik (NMM rakus, IOS 0,5, ambang keyakinan 0,4, tambalan resolusi sedang) menghasilkan F1 83,09%, tanpa memerlukan pelacakan objek.

Catatan verifikasi data: F1, presisi, recall, laju penemuan palsu, laju negatif palsu, selisih 2,32%, dan AP (0,396; 0,811; 0,871) tertulis di Bagian 4.3; jumlah citra dan pembagian di Bagian 3.2.1; pengaturan irisan di Bagian 3.2. Isi Tabel 1, 2, 3, dan 4 tidak terekstraksi pada berkas teks (hanya keterangan tabel), sehingga AP per resolusi sebelum penjahitan, F1 validasi per resolusi, waktu inferensi, jumlah absolut tomat acuan dan deteksi, serta angka perbandingan dengan makalah lain hanya dapat diverifikasi sebagian dari narasi (misalnya F1 83,67% untuk Mu dkk. dan 93,91% untuk YOLO-tomato). Gambar 2 sampai 5 tidak terbaca dari teks. Berkas teks merupakan naskah yang diterima (*accepted manuscript*) dengan beberapa huruf awal kata hilang pada ekstraksi (misalnya "e apply"), yang tidak memengaruhi angka.
