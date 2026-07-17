# 082 - Antipodal Robotic Grasping Using Generative Residual Convolutional Neural Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kumra2020grconvnet` |
| Judul asli | Antipodal Robotic Grasping using Generative Residual Convolutional Neural Network |
| Penulis | Sulabh Kumra, Shirin Joshi, Ferat Sahin |
| Tahun | 2020 |
| Venue | IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2020), hlm. 9626–9633 |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1909.04810
- **Google Scholar:** https://scholar.google.com/scholar?q=Antipodal%20Robotic%20Grasping%20Using%20Generative%20Residual%20Convolutional%20Neural%20Network
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Antipodal%20Robotic%20Grasping%20Using%20Generative%20Residual%20Convolutional%20Neural%20Network&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan GR-ConvNet (*Generative Residual Convolutional Neural Network*), sebuah jaringan saraf konvolusi yang memprediksi cengkeraman robotik langsung dari citra suatu adegan. Tugas yang dipecahkan adalah *robotic grasping*: menentukan di mana dan bagaimana sebuah lengan robot berpenjepit dua jari harus menutup untuk mengangkat objek yang belum pernah dilihat sebelumnya. GR-ConvNet menerima citra masukan *n*-kanal — bisa berupa RGB, kedalaman (*depth*), atau gabungan RGB-D (warna empat kanal digabung dengan satu kanal kedalaman) — dan menghasilkan tiga peta prediksi seukuran citra masukan yang, pada setiap piksel, menyatakan mutu, orientasi, dan lebar cengkeraman yang berpusat di piksel itu.

Rumusan ini bersifat generatif dan per-piksel: alih-alih menilai sejumlah kotak kandidat satu per satu, jaringan menghasilkan seluruh peta cengkeraman untuk citra penuh dalam satu evaluasi berkecepatan sekitar 20 milidetik. Pada dua tolok ukur standar, model ini mencapai akurasi 97,7% pada dataset Cornell dan 94,6% pada dataset Jacquard, serta tingkat keberhasilan cengkeraman 95,4% pada objek rumah tangga dan 93% pada objek adversarial ketika diuji pada lengan robot fisik 7 derajat kebebasan. GR-ConvNet menjadi salah satu baseline kuat untuk cengkeraman berbasis RGB-D di klaster ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Mendeteksi cengkeraman berbeda dari mendeteksi objek. Deteksi objek cukup menandai kotak pembatas dan kelas; cengkeraman menuntut geometri yang dapat dieksekusi lengan robot: posisi titik cengkeram, sudut rotasi penjepit, dan bukaan jari. Representasi baku yang dipakai bidang ini adalah *grasp rectangle* (kotak cengkeraman), yaitu kotak berorientasi yang dua sisinya mewakili pelat penjepit dan sudutnya mewakili orientasi tangan. Istilah *antipodal* merujuk pada cengkeraman dua jari yang menekan objek dari dua sisi berlawanan sepanjang satu garis lurus — model kontak paling sederhana yang tetap stabil secara fisik.

Pendekatan awal memperlakukan pencarian cengkeraman sebagai klasifikasi banyak kandidat: sistem seperti yang dibahas pada bab 080 mengevaluasi ribuan kotak cengkeraman calon dan memilih yang terbaik, sehingga lambat dan tidak sesuai untuk kendali waktu nyata. GG-CNN pada bab 081 mengubah paradigma menjadi generatif — memprediksi satu cengkeraman per piksel secara langsung — dan sangat ringan, tetapi jaringannya dangkal sehingga akurasinya terbatas dan sulit menangani objek yang bervariasi. GR-ConvNet mengambil kerangka generatif per-piksel dari GG-CNN, lalu memperdalam jaringan dengan blok residual agar akurasi naik tanpa mengorbankan kecepatan waktu nyata, sekaligus memanfaatkan fusi warna dan kedalaman.

## Ide Utama

Gagasan inti GR-ConvNet adalah memisahkan prediksi cengkeraman menjadi tiga besaran per-piksel yang mudah dipelajari jaringan, lalu merakit kembali cengkeraman terbaik dari peta-peta itu. Untuk setiap piksel citra, jaringan memprediksi: (1) *grasp quality* Q, skor antara 0 dan 1 yang menyatakan seberapa mungkin cengkeraman berpusat di piksel itu berhasil; (2) sudut orientasi Θ; dan (3) lebar bukaan penjepit W dalam piksel. Piksel dengan Q tertinggi menunjuk pusat cengkeraman terbaik, dan nilai Θ serta W pada piksel itu melengkapi geometrinya.

Kesulitan teknisnya terletak pada sudut. Orientasi penjepit bersifat *antipodal*, sehingga sudut Θ dan Θ+180° menghasilkan cengkeraman fisik yang sama; sudut juga melingkar, sehingga −90° dan +90° berdampingan. Regresi langsung terhadap nilai Θ akan membingungkan jaringan di titik lipatan ini. GR-ConvNet menghindarinya dengan tidak memprediksi Θ secara langsung, melainkan dua komponen cos(2Θ) dan sin(2Θ). Penggandaan sudut membuat Θ dan Θ+180° dipetakan ke nilai yang sama, dan pasangan (cos, sin) bersifat kontinu tanpa lompatan, sehingga menghasilkan target regresi yang mulus.

## Cara Kerja Langkah demi Langkah

### Masukan dan Representasi Cengkeraman

Jaringan menerima citra 224×224 piksel dengan *n* kanal. Pada mode RGB-D, kanal warna dan kanal kedalaman digabung menjadi masukan tunggal sehingga jaringan dapat memanfaatkan tekstur (dari warna) dan geometri (dari kedalaman) sekaligus. Keluarannya adalah empat peta beresolusi 224×224: satu peta Q, dua peta sudut (cos 2Θ dan sin 2Θ), dan satu peta lebar W. Sudut hasil rekonstruksi berada pada rentang [−π/2, π/2]. Karena keempat peta seukuran citra masukan, setiap piksel merupakan kandidat pusat cengkeraman, dan satu evaluasi jaringan menghasilkan seluruh medan kandidat sekaligus — inilah arti "generatif" pada konteks ini.

### Arsitektur Generatif Residual

Struktur jaringan mengikuti pola *encoder–decoder*. Bagian awal berisi tiga lapis konvolusi yang secara bertahap menurunkan resolusi spasial dari 224×224 menjadi 56×56 sambil menambah jumlah kanal fitur; tahap ini memadatkan citra menjadi representasi fitur yang ringkas. Bagian tengah berisi lima blok residual. Blok residual adalah susunan konvolusi yang keluarannya dijumlahkan kembali dengan masukannya melalui koneksi pintas (*skip connection*); penjumlahan ini membuat gradien mengalir lebih mudah saat pelatihan sehingga jaringan dapat diperdalam tanpa gejala gradien menghilang. Bagian akhir berisi lapis konvolusi transpos (*transpose convolution*), yaitu operasi yang menaikkan kembali resolusi dari 56×56 ke 224×224 agar keluaran sepadan dengan citra masukan piksel demi piksel. Seluruh jaringan hanya memuat 1.900.900 parameter yang dapat dilatih — tergolong kecil untuk jaringan konvolusi dalam — dan justru keringkasan inilah yang memungkinkan inferensi ~20 milidetik.

Alur data ringkas dari citra ke peta cengkeraman:

```
citra RGB-D 224x224xN
        │
   ┌────▼─────┐  3 konvolusi
   │ encoder  │  224 -> 112 -> 56 (resolusi turun)
   └────┬─────┘
   ┌────▼─────┐  5 blok residual
   │ residual │  fitur diperdalam, resolusi 56x56 tetap
   └────┬─────┘
   ┌────▼─────┐  konvolusi transpos
   │ decoder  │  56 -> 112 -> 224 (resolusi naik)
   └────┬─────┘
        │
   4 peta 224x224:  Q │ cos2Θ │ sin2Θ │ W
        │
   pilih piksel Q maksimum -> (posisi, Θ, W) cengkeraman
```

Diagram di atas menunjukkan bahwa resolusi diturunkan agar fitur dapat dipadatkan lalu dinaikkan kembali agar prediksi tetap per-piksel; blok residual bekerja pada resolusi rendah tempat komputasi paling murah.

### Pelatihan

Pelatihan memakai *smooth L1 loss* (juga disebut *Huber loss*): fungsi galat yang berperilaku kuadratik untuk selisih kecil dan linear untuk selisih besar, sehingga tidak terlalu sensitif terhadap pencilan dan mencegah gradien meledak. Optimasi memakai Adam dengan laju belajar 10⁻³ dan ukuran *batch* 8. Dataset Cornell yang berukuran kecil diperbesar lewat augmentasi (rotasi dan pergeseran acak) menjadi sekitar 51.000 contoh agar cukup untuk melatih jaringan; dataset Jacquard yang sudah besar (sekitar 54.000 citra dengan 1,1 juta anotasi cengkeraman) dipakai apa adanya.

### Evaluasi dan Eksekusi pada Robot

Sebuah cengkeraman prediksi dinyatakan benar bila memenuhi dua syarat sekaligus terhadap cengkeraman kebenaran: (1) IoU (*Intersection over Union* — rasio luas irisan terhadap luas gabungan dua kotak) lebih dari 25%, dan (2) selisih sudut kurang dari 30°. Pada robot fisik, peta Q dipakai untuk memilih piksel terbaik, nilai Θ dan W pada piksel itu diubah ke koordinat dunia lewat kalibrasi kamera, lalu lengan digerakkan untuk mengeksekusi cengkeraman.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua dataset baku. Pada Cornell, pengujian memakai dua skema validasi silang: *image-wise* (IW), yang membagi data per citra sehingga objek yang sama bisa muncul di latih dan uji, dan *object-wise* (OW), yang memisahkan per objek sehingga model diuji pada objek yang benar-benar baru — OW menguji generalisasi lebih ketat. Varian RGB-D mencapai 97,7% (IW) dan 96,6% (OW) dengan inferensi 20 milidetik. Sebagai pembanding, GG-CNN (bab 081) dilaporkan pada kisaran 73% (IW) dan 69% (OW) pada 19 milidetik: GR-ConvNet menaikkan akurasi secara besar dengan kecepatan hampir setara. Model FCGN berbasis ResNet-101 mencapai akurasi setara GR-ConvNet tetapi dengan inferensi 117 milidetik, sekitar enam kali lebih lambat; interpretasinya, GR-ConvNet menandingi akurasi jaringan yang jauh lebih berat sambil mempertahankan kelayakan waktu nyata.

Ablasi modalitas masukan pada Cornell memperjelas kontribusi tiap kanal: kedalaman saja mencapai 93,2% (IW), RGB saja 96,6% (IW), dan RGB-D 97,7% (IW). Urutan ini menunjukkan warna lebih informatif daripada kedalaman untuk tugas ini, tetapi menggabungkan keduanya tetap memberi kenaikan — bukti bahwa fusi RGB-D menyumbang informasi yang tidak dimiliki masing-masing kanal sendirian. Pada Jacquard yang lebih besar dan beragam, model mencapai 94,6%.

Pengujian fisik memakai lengan robot 7 derajat kebebasan (Baxter) dengan penjepit paralel dan kamera Intel RealSense D435. Pada objek rumah tangga, keberhasilan 95,4% (334 dari 350 percobaan); pada objek adversarial berbentuk sulit, 93% (93 dari 100); pada adegan berjejal (*cluttered*), sekitar 93,5%. Angka-angka ini menunjukkan akurasi tinggi pada dataset diikuti keberhasilan yang tetap tinggi saat dipindahkan ke perangkat keras nyata, termasuk pada objek di luar data latih.

## Kelebihan dan Keterbatasan

Kelebihan utama: akurasi setara metode terbaik pada masanya dengan biaya komputasi kecil (1,9 juta parameter, ~20 milidetik), rumusan generatif per-piksel yang mendukung deteksi banyak cengkeraman sekaligus untuk adegan multi-objek, fleksibilitas masukan *n*-kanal, dan validasi langsung pada robot fisik. Penanganan sudut lewat cos(2Θ)/sin(2Θ) menyelesaikan masalah periodisitas orientasi dengan rapi.

Keterbatasan: cengkeraman yang dihasilkan bersifat planar — kotak berorientasi pada bidang citra, bukan cengkeraman 6 derajat kebebasan penuh yang bebas memilih arah pendekatan di ruang tiga dimensi (bandingkan dengan bab 084). Dari sisi rekayasa, kualitas prediksi bergantung pada kualitas kanal kedalaman; sensor RGB-D konsumen menghasilkan lubang dan derau pada permukaan mengilap atau tepi objek, yang dapat menurunkan akurasi. Secara konseptual, dataset Cornell sangat kecil sehingga akurasi IW yang tinggi sebagian mencerminkan kemiripan latih–uji; skema OW dan pengujian Jacquard memitigasi hal ini, tetapi objek berhimpitan pada adegan berjejal tetap menjadi kasus tersulit.

## Kaitan dengan Bab Lain

Bab ini adalah kelanjutan langsung dari dua pendahulunya pada klaster Grasp Robotik. Dari [080 - Deep Learning Robotic Grasps (Lenz dkk.)](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md) diwarisi representasi *grasp rectangle* dan tolok ukur Cornell, tetapi paradigma klasifikasi kandidat yang lambat ditinggalkan. Dari [081 - GG-CNN](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md) diwarisi rumusan generatif per-piksel; GR-ConvNet memperdalamnya dengan blok residual untuk menaikkan akurasi. Penyempurnaan lanjutan dibahas pada [083 - GR-ConvNet v2](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md), sementara pendekatan cengkeraman 6 derajat kebahasan berskala besar muncul pada [084 - GraspNet-1Billion](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md). Dataset Jacquard yang dipakai untuk evaluasi kedua diuraikan pada [086 - Jacquard Dataset](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md). Kontribusi bab ini bagi tinjauan adalah menegaskan manfaat fusi RGB-D untuk manipulasi robotik dengan biaya komputasi rendah.

## Poin untuk Sitasi

Kutip dengan kunci `kumra2020grconvnet`. Ringkasan yang aman dikutip: "GR-ConvNet memprediksi cengkeraman antipodal per-piksel (mutu, sudut, lebar) dari citra RGB-D memakai arsitektur generatif residual, mencapai akurasi 97,7% pada Cornell dan 94,6% pada Jacquard dengan inferensi ~20 milidetik, serta keberhasilan 95,4% pada objek rumah tangga dengan lengan robot 7 derajat kebebasan." Angka akurasi (97,7% / 94,6%), kecepatan (~20 ms), jumlah parameter (1.900.900), dan keberhasilan robot (95,4% / 93%) berasal dari abstrak dan naskah versi HTML arXiv. Rincian yang sebaiknya diverifikasi ulang ke tabel naskah sebelum sitasi formal: angka ablasi per modalitas (D 93,2% / RGB 96,6% / RGB-D 97,7%), angka baseline pembanding (GG-CNN 73% / 69%; FCGN 117 ms), keberhasilan pada adegan berjejal (±93,5%), dan identitas persis perangkat keras (lengan Baxter, kamera RealSense D435) yang dikutip dari ekstraksi HTML, bukan dari PDF resmi.
