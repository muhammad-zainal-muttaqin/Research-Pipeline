# 080 - Deep Learning for Detecting Robotic Grasps

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lenz2015grasp` |
| Judul asli | Deep Learning for Detecting Robotic Grasps |
| Penulis | Ian Lenz, Honglak Lee, Ashutosh Saxena |
| Tahun | 2015 (preprint 2013) |
| Venue | The International Journal of Robotics Research (IJRR), vol. 34, no. 4–5, hlm. 705–724 |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (preprint gratis):** https://arxiv.org/abs/1301.3592
- **DOI (versi jurnal IJRR):** https://doi.org/10.1177/0278364914549607
- **Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Learning%20for%20Detecting%20Robotic%20Grasps

## Gambaran Umum

Makalah ini mengusulkan sistem pertama yang mendeteksi posisi cengkeraman (*grasp*) robot langsung dari citra RGB-D (citra warna disertai peta kedalaman per piksel) memakai jaringan saraf dalam, tanpa fitur rancangan tangan. Setiap kandidat cengkeraman direpresentasikan sebagai kotak berorientasi (*oriented rectangle*) pada bidang citra, dan sistem memprediksi seberapa layak kotak itu dieksekusi oleh penjepit dua jari. Karena jumlah kandidat kotak pada satu citra bisa mencapai ribuan, penulis menyusun kaskade dua jaringan: jaringan pertama yang kecil menyaring kandidat secara cepat, jaringan kedua yang lebih besar mengevaluasi ulang sisa kandidat dengan lebih teliti.

Sistem diuji pada *Cornell Grasping Dataset* — kumpulan data yang diperkenalkan bersama makalah ini — dan pada dua platform robot fisik, Baxter dan PR2. Pendekatan ini mengalahkan metode berbasis fitur tangan sebelumnya pada metrik deteksi kotak, dan berhasil menjalankan cengkeraman nyata dengan tingkat keberhasilan 84% pada Baxter dan 89% pada PR2 dari 100 percobaan pada 30 objek. Bab ini menjadi rujukan akar bagi klaster Grasp Robotik dalam tinjauan ini karena meletakkan representasi kotak berorientasi dan pasangan citra-label yang dipakai ulang oleh metode-metode berikutnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, perencanaan cengkeraman robot umumnya bersifat analitik: sistem membangun model geometris tiga dimensi objek, menghitung titik kontak yang memenuhi syarat kestabilan gaya (misalnya syarat *force closure*, kondisi ketika gaya penjepit menahan objek dari segala arah gerak), lalu menurunkan pose penjepit dari model tersebut. Pendekatan ini membutuhkan model objek yang akurat dan lengkap, sesuatu yang jarang tersedia untuk objek baru yang belum pernah dilihat robot. Sensor kedalaman murah seperti Kinect, yang mulai luas dipakai pada awal 2010-an, juga menghasilkan data berderau dan berlubang (bagian permukaan yang tidak terbaca kedalamannya), sehingga model geometris yang direkonstruksi darinya sering tidak lengkap.

Alternatif berbasis pembelajaran sudah mulai muncul, tetapi bergantung pada fitur yang dirancang manual (tepi, tekstur, kontur kedalaman) yang harus disesuaikan ulang untuk setiap jenis objek. Belum ada kumpulan data cengkeraman berlabel yang cukup besar untuk melatih model pembelajaran secara luas, dan representasi cengkeraman yang dipakai sebagian karya sebelumnya (misalnya berbasis titik kontak individual) sulit diselaraskan langsung dengan koordinat citra. Kekosongan ini yang coba diisi oleh makalah Lenz, Lee, dan Saxena: representasi cengkeraman yang ringkas dan selaras citra, fitur yang dipelajari otomatis dari data RGB-D, serta kumpulan data berlabel yang dapat dipakai peneliti lain.

## Ide Utama

Gagasan inti makalah adalah memandang deteksi cengkeraman sebagai masalah klasifikasi biner pada kotak kandidat, serupa cara detektor objek menilai kelayakan sebuah *bounding box* (kotak pembatas). Setiap kandidat cengkeraman digambarkan sebagai kotak berorientasi pada citra: dua sisi sejajarnya mewakili posisi dua pelat penjepit, sedangkan sudut orientasi kotak menyatakan arah pendekatan penjepit. Jaringan saraf menerima potongan citra RGB-D di dalam kotak tersebut dan mengeluarkan skor kelayakan — bukan aturan geometris tangan, melainkan fitur yang dipelajari langsung dari piksel dan kedalaman.

Karena mengevaluasi seluruh kandidat kotak dengan satu jaringan besar terlalu lambat untuk dipakai pada robot nyata, penulis memisahkan tugas menjadi dua tahap dengan ukuran berbeda: jaringan kecil untuk menyaring cepat, jaringan besar untuk memutuskan akhir. Pemisahan ini adalah kompromi kecepatan-akurasi yang eksplisit, bukan sekadar penambahan lapisan.

## Cara Kerja Langkah demi Langkah

### Representasi Cengkeraman sebagai Kotak Berorientasi

Setiap kandidat cengkeraman dinyatakan dalam lima parameter: koordinat (x, y) sudut kiri-atas kotak, lebar, tinggi, dan sudut orientasi kotak terhadap sumbu citra. Representasi ini diadaptasi dari kerja Jiang dkk. sebelumnya. Dua sisi kotak yang sejajar dan lebih pendek mewakili posisi kedua pelat penjepit robot; jarak antar keduanya harus sesuai bukaan penjepit agar cengkeraman dapat dieksekusi secara fisik. Representasi lima parameter ini mengubah pencarian pose cengkeraman tiga dimensi menjadi pencarian kotak dua dimensi pada bidang citra, sehingga dapat diproses dengan arsitektur pengenalan citra biasa.

### Ekstraksi Fitur Multimodal

Untuk setiap kandidat kotak, citra dipotong dan diubah ukurannya menjadi tujuh kanal berukuran 24×24 piksel: tiga kanal warna dalam ruang warna YUV, satu kanal kedalaman, dan tiga kanal komponen normal permukaan (arah tegak lurus permukaan pada sumbu X, Y, Z, dihitung dari peta kedalaman). Total fitur masukan per kandidat adalah 24×24×7 = 4.032 angka. Kanal normal permukaan penting karena menangkap kemiringan lokal objek — informasi yang tidak tersedia dari kedalaman mentah saja dan relevan untuk menilai apakah permukaan cocok dijepit rata.

### Arsitektur Kaskade Dua Tahap

Diagram berikut merangkum alur dari citra ke satu kotak cengkeraman terpilih:

```
citra RGB-D, ribuan kandidat kotak berorientasi
        |
        v
+---------------------------+
| jaringan tahap 1          |  menyaring cepat,
| 2 lapis, 50 unit/lapis    |  akurasi lebih rendah
+---------------------------+
        | 100 kandidat skor tertinggi
        v
+---------------------------+
| jaringan tahap 2          |  mengevaluasi ulang,
| 2 lapis, 200 unit/lapis   |  akurasi lebih tinggi
+---------------------------+
        |
        v
   satu kotak cengkeraman terbaik
```

Jaringan tahap pertama memiliki dua lapis tersembunyi berukuran 50 unit dan dijalankan secara menyeluruh (*exhaustive search*) pada semua kandidat kotak yang dihasilkan dari citra, karena murah secara komputasi. Keluarannya adalah 100 kandidat dengan skor tertinggi. Jaringan tahap kedua memiliki dua lapis tersembunyi berukuran 200 unit — empat kali lebih besar — dan hanya dijalankan pada 100 kandidat yang lolos penyaringan tahap pertama, lalu memilih satu kotak dengan skor akhir tertinggi sebagai keluaran sistem. Kedua jaringan memakai fungsi aktivasi sigmoid pada lapis tersembunyi dan regresi logistik pada lapis keluaran untuk menghasilkan skor kelayakan biner (layak/tidak layak dieksekusi).

### Regularisasi Kelompok Multimodal

Karena masukan menggabungkan tiga modalitas berbeda (warna, kedalaman, normal permukaan) yang memiliki statistik dan tingkat keandalan berbeda, penggabungan langsung tanpa perlakuan khusus berisiko membuat jaringan menumpukan seluruh bobot pada satu modalitas yang kebetulan lebih mudah dipelajari saat pelatihan awal. Penulis mengusulkan regularisasi kelompok multimodal: penalti diterapkan per kelompok bobot yang menghubungkan satu modalitas ke satu unit tersembunyi, mendorong setiap unit tersembunyi menggunakan sebagian kecil modalitas secara efektif alih-alih mencampur semuanya secara samar. Pendekatan ini terbukti unggul dibandingkan regularisasi standar (L1 atau L2 pada seluruh bobot tanpa pengelompokan modalitas) pada pengujian yang dilaporkan.

### Pelatihan

Kedua jaringan dilatih dalam dua tahap: pra-pelatihan tanpa label memakai *sparse autoencoder* (jaringan yang belajar merekonstruksi masukannya sendiri melalui lapis tersembunyi yang dibatasi agar hanya sedikit unit aktif sekaligus, sehingga representasi yang dipelajari lebih ringkas), diikuti penyetelan halus (*fine-tuning*) terawasi memakai label layak/tidak layak dari data cengkeraman. Pra-pelatihan tanpa label ini membantu inisialisasi bobot pada data yang relatif terbatas ukurannya dibandingkan basis data pengenalan citra umum.

### Data dan Inferensi

Data dikumpulkan dalam *Cornell Grasping Dataset*: 1.035 citra RGB-D dari 280 objek yang dapat digenggam, masing-masing diberi anotasi kotak cengkeraman positif dan negatif secara manual. Pada saat inferensi di robot nyata, kaskade dua tahap memangkas waktu deteksi per citra dari sekitar 24,6 detik (bila seluruh kandidat dievaluasi langsung oleh jaringan besar) menjadi sekitar 13,5 detik, karena jaringan besar hanya perlu dijalankan pada 100 kandidat, bukan seluruh ribuan kandidat awal.

## Eksperimen dan Hasil

Evaluasi offline dilakukan pada Cornell Grasping Dataset dengan dua skema pembagian data lima-lipat (*5-fold cross-validation*): pembagian citra (*image-wise*, gambar objek yang sama bisa muncul di latih maupun uji) dan pembagian objek (*object-wise*, seluruh gambar satu objek hanya muncul di satu sisi, menguji generalisasi ke objek yang benar-benar baru). Dua metrik dipakai: metrik titik (cengkeraman dianggap benar bila titik pusat kotak prediksi cukup dekat dengan pusat kotak kebenaran, tanpa memperhatikan orientasi) dan metrik kotak (memakai IOU — rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kebenaran, minimal 25%, serta selisih orientasi maksimal 30 derajat).

Pada metrik kotak, sistem kaskade dengan regularisasi kelompok mencapai akurasi sekitar 73,9% pada pembagian citra dan 75,6% pada pembagian objek, mengungguli fitur rancangan tangan dari Jiang dkk. yang berada di kisaran 58%. Selisih kecil antara kedua skema pembagian (73,9% berbanding 75,6%) menunjukkan sistem tidak banyak kehilangan akurasi saat diuji pada objek yang belum pernah dilihat, tanda generalisasi yang wajar untuk ukuran data selatih itu. Pada eksperimen klasifikasi kelayakan (metrik titik), akurasi pengenalan meningkat dari 84,7% (fitur tangan Jiang dkk.) dan 89,6% (fitur tangan ditambah deskriptor FPFH, fitur permukaan tiga dimensi lokal) menjadi 93,7% dengan fitur yang dipelajari dan regularisasi kelompok — kenaikan yang menunjukkan fitur otomatis dari data RGB-D dapat melampaui fitur tangan yang disusun pakar untuk tugas ini.

Uji fisik pada robot menjadi pembuktian akhir. Pada Baxter, dari 100 percobaan mencakup 30 objek beragam, tingkat keberhasilan cengkeraman mencapai 84%; pada PR2, tingkat keberhasilan mencapai 89%. Kedua angka ini jauh di atas garis dasar (*baseline*) berupa kotak berukuran tetap tanpa pembelajaran, yang menurut penulis berhasil pada kisaran 30% percobaan saja — perbedaan yang menegaskan bahwa keberhasilan bergantung pada pemilihan kotak cengkeraman yang tepat, bukan sekadar mendekatkan penjepit ke objek.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini ada pada tiga hal. Pertama, representasi kotak berorientasi memindahkan masalah cengkeraman tiga dimensi menjadi masalah dua dimensi yang selaras dengan arsitektur pengenalan citra yang sudah matang. Kedua, kaskade dua tahap menawarkan kompromi kecepatan-akurasi yang terukur, dengan pengurangan waktu deteksi mendekati separuh dibanding evaluasi penuh. Ketiga, *Cornell Grasping Dataset* menyediakan tolok ukur bersama yang dipakai ulang oleh hampir seluruh metode deteksi cengkeraman berikutnya.

Dari sisi rekayasa, sistem ini tetap membatasi cengkeraman pada bidang dua dimensi dengan pendekatan dari satu arah pandang kamera, bukan cengkeraman enam derajat kebebasan penuh di ruang tiga dimensi — sudut pendekatan penjepit dari arah lain tidak dipertimbangkan. Secara konseptual, ukuran *Cornell Grasping Dataset* yang hanya 1.035 citra tergolong kecil untuk standar pembelajaran dalam saat ini, sehingga generalisasi ke objek dengan bentuk sangat berbeda dari data latih tidak terjamin. Waktu inferensi 13,5 detik per citra, meskipun lebih cepat dari 24,6 detik semula, masih jauh dari kecepatan yang dibutuhkan aplikasi robot waktu nyata. Penulis sendiri mencatat kegagalan pada permukaan mengkilap yang tidak terbaca baik oleh sensor kedalaman, dan pada objek yang warnanya menyatu dengan latar belakang.

## Kaitan dengan Bab Lain

Bab ini adalah titik awal klaster Grasp Robotik dalam tinjauan ini: representasi kotak berorientasi dan *Cornell Grasping Dataset* yang diperkenalkan di sini dipakai ulang oleh [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md), yang menggantikan kaskade dua jaringan dengan satu jaringan konvolusi penuh yang memprediksi peta kualitas cengkeraman secara langsung dan jauh lebih cepat. [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md) dan penerusnya [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md) melanjutkan arah generatif ini dengan arsitektur *encoder-decoder*. Keterbatasan skala data pada makalah ini juga menjadi motivasi langsung bagi kumpulan data yang jauh lebih besar, seperti [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md) dan [086 - 2018 - Jacquard Dataset - Grasp Robotik](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md), yang menyediakan ratusan ribu hingga miliaran anotasi cengkeraman sintetis. Fusi modalitas RGB-D yang dirintis lewat regularisasi kelompok di sini juga menjadi rujukan bagi pendekatan fusi lintas-modal lanjutan seperti [085 - 2023 - BCMFNet (Bilateral Cross-Modal Fusion) - Grasp Robotik](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md).

## Poin untuk Sitasi

Kutip dengan kunci `lenz2015grasp`. Ringkasan yang aman dikutip: "Lenz, Lee, dan Saxena mengusulkan deteksi cengkeraman robot dari citra RGB-D memakai kaskade dua jaringan saraf dengan regularisasi kelompok multimodal, memperkenalkan representasi kotak cengkeraman berorientasi dan *Cornell Grasping Dataset* (1.035 citra, 280 objek), serta mendemonstrasikan tingkat keberhasilan cengkeraman fisik 84% pada robot Baxter dan 89% pada PR2." Angka akurasi metrik kotak (73,9% pembagian citra, 75,6% pembagian objek), akurasi metrik titik (84,7% / 89,6% / 93,7%), waktu inferensi (24,6 detik menjadi 13,5 detik), dan garis dasar kotak tetap (~30%) diperoleh dari ekstraksi otomatis naskah arXiv dan sumber sekunder yang merujuk tabel aslinya; nilai-nilai ini sebaiknya dicocokkan langsung dengan tabel pada PDF makalah (arXiv 1301.3592 atau IJRR 2015) sebelum dikutip dalam karya formal.
