# Detection and Counting of Lemons using Artificial Vision and Tracking Techniques for Real Time Harvest Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `serafino2020detection` |
| Judul asli | Detection and Counting of Lemons using Artificial Vision and Tracking Techniques for Real Time Harvest Estimation |
| Penulis | Serafino, Sandra E.; Cicerchia, Lucas Benjam\'\in; P\'erez, Gabriel; Adorno, Sebastian; Balmer, Agust\'\in |
| Tahun | 2020 |
| Venue | Proceedings 2020 46th Latin American Computing Conference Clei 2020 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [serafino2020detection.pdf](../pdf/serafino2020detection.pdf)
- DOI resmi: https://doi.org/10.1109/clei52000.2020.00064

## Gambaran Umum
Makalah ini (ditulis dalam bahasa Spanyol dengan abstrak berbahasa Inggris; prosiding CLEI 2020) mengembangkan algoritma pencacahan jeruk lemon secara waktu-nyata pada saat panen. Kamera RGB beresolusi rendah dan komputer berdaya olah rendah (Raspberry Pi 4 Model B) dipasang pada mesin pemanen lemon Optimus Citrus buatan Maqtec. Kamera mengamati sabuk pengangkut (*conveyor belt*) yang membawa buah hasil panen, bukan buah yang masih berada di pohon.

Metode yang dipakai berupa pengolahan citra klasik: indeks kontras warna, segmentasi rentang warna pada ruang warna CIELAB, pengurangan masker vegetasi (*Normalized Difference Index*, NDI), morfologi matematika, dan pelacakan objek berbasis algoritma Kuhn-Munkres. Pengujian memakai enam video panen yang diambil pada satu kali panen, dengan resolusi 640x480 piksel dan durasi rata-rata 25 detik per video.

Hasil utama: regresi linear antara hitungan algoritma dan hitungan visual menghasilkan persamaan y = 0,96x + 0,187 dengan koefisien korelasi (R²) 0,997. Penulis melaporkan kesesuaian hitungan di atas 95% dan galat rata-rata 4,45%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Perkiraan jumlah buah yang dipanen membantu petani mengetahui produksi, menyusun strategi dagang, dan memperkirakan pendapatan. Penghitungan visual oleh manusia, baik pada panen manual maupun dengan mesin pemanen, dinilai membosankan, subjektif, memakan waktu, dan sering menimbulkan banyak kesalahan.

Penulis menyebut pendekatan lain yang telah ada, yaitu pembelajaran mendalam serta pelacakan dengan filter Kalman dan *kernelized correlation filter* (KCF). Tujuan makalah ini berbeda: pencacahan harus berjalan waktu-nyata pada perangkat keras terbatas di atas mesin pemanen, sehingga pemilihan algoritma dibatasi oleh efisiensi sumber daya.

## Ide Utama
Gagasan utamanya ialah menghitung buah pada lokasi yang paling memudahkan, yaitu bagian awal sabuk pengangkut. Pada bagian itu buah cenderung terpisah sehingga mudah dicacah. Setiap buah dideteksi dengan segmentasi warna, kemudian dilacak antarbingkai agar satu buah dihitung satu kali selama bergerak melintasi daerah minat (*region of interest*, ROI).

Identitas buah antarbingkai dijaga oleh pelacakan berbasis penugasan optimal (algoritma Kuhn-Munkres) pada matriks biaya jarak antara deteksi saat ini dan deteksi sebelumnya. Hitungan dibentuk dari jumlah lintasan (*track*) yang valid.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Perangkat portabel dibuat dari Raspberry Pi 4 Model B dan kamera RGB Genius Widecam F100 dengan resolusi video 640x480 hingga 1024x768 piksel pada 30 fps. Video diambil dengan cahaya alami saat panen berlangsung. Lokasi pemasangan dipilih pada sabuk pengangkut karena buah panen terlihat lebih jelas di sana, tetapi sabuk berada di tempat terbuka sehingga cahaya berubah sepanjang hari dan menurut posisi mesin. Jumlah total buah dan lokasi kebun tidak dilaporkan.

### 2. Praprosesing
Penulis menetapkan ROI pada awal sabuk pengangkut. Untuk mengatasi saturasi akibat cahaya yang tidak terkendali, citra diberi operasi pembukaan morfologi berwarna (*color morphological opening*) pada ruang RGB, yang juga mengurangi derau.

### 3. Segmentasi
Dua indeks kontras warna dihitung pada ruang RGB untuk memisahkan objek kuning: R-B dan G-B (mengacu pada Xu dan Ying). Masing-masing indeks diberi ambang dan kedua masker biner diambil irisannya. Hasil prasegmentasi diperbaiki dengan segmentasi rentang warna pada CIELAB, dengan batas bawah dan atas yang diturunkan dari analisis citra yang diperoleh. Daun dihapus dengan mengurangkan masker NDI (nilai terhijau). Terakhir, morfologi biner (pembukaan dan pengisian lubang) dan penyaringan area dipakai untuk membuang deteksi yang tidak dikehendaki.

Buah yang menempel dan tersegmentasi sebagai satu objek ditangani dengan memanfaatkan area rata-rata buah: objek yang lebih besar dibagi dengan area rata-rata itu. Transformasi Hough melingkar (*circular Hough transform*), *watershed*, dan deteksi tepi dicoba tetapi tidak memberi hasil baik dan tidak dapat dijalankan waktu-nyata. Penulis juga mengamati bahwa buah pada sabuk cenderung terpisah sendiri.

### 4. Pelacakan
Masker biner dilacak dengan algoritma Kuhn-Munkres pada matriks biaya jarak terhadap deteksi sebelumnya. Parameter penerimaan dan penolakan deteksi serta masa hidup deteksi disesuaikan dengan kecepatan buah pada sabuk. Algoritma menyimpan *buffer* lintasan. Deteksi yang cocok dengan lintasan memperbarui posisi lintasan itu, deteksi tanpa pasangan menjadi lintasan baru, dan lintasan yang tidak mendapat pasangan dipertahankan selama siklus yang ditentukan lalu dibuang. Jumlah lintasan yang benar merepresentasikan jumlah buah yang terdeteksi.

## Eksperimen dan Hasil
Algoritma diuji pada enam video dari satu kali panen, masing-masing berdurasi rata-rata 25 detik. Setiap video dianalisis bingkai demi bingkai. Untuk setiap detik (30 bingkai) dicatat hitungan visual buah yang melewati sabuk sebagai acuan (*ground truth*), lalu dibandingkan dengan hitungan algoritma melalui model regresi linear.

| Ukuran | Nilai |
|---|---|
| Jumlah video uji | 6 (satu panen) |
| Durasi rata-rata video | 25 detik |
| Persamaan regresi | y = 0,96x + 0,187 |
| Koefisien korelasi (R²) | 0,997 |
| Galat rata-rata | 4,45% |
| Kesesuaian hitungan | di atas 95% |

Penulis menyatakan bahwa tidak ada pembanding metode lain dalam eksperimen. Hasil per video dan jumlah buah total tidak dilaporkan pada teks.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: algoritma ringan sehingga dapat berjalan waktu-nyata pada perangkat berdaya rendah, serta dapat diskalakan ke pencacahan objek pada adegan lain.

Keterbatasan yang dinyatakan penulis: pengujian pada adegan lain (tajuk tanaman dan tanah) menunjukkan bahwa cahaya alami, kecepatan pelacakan, serta resolusi spasial dan radiometrik memengaruhi hasil, sehingga parameter harus disesuaikan agar algoritma dapat digeneralisasi. Penulis merencanakan pengujian pada berbagai adegan dan jam, serta penambahan deteksi berbasis pembelajaran mesin.

Menurut pembacaan ringkasan ini, evaluasi terbatas pada enam video dari satu kali panen dengan satu jenis buah, sehingga generalisasi belum teruji. Kemudian, data uji tidak dipisahkan dari penyetelan parameter secara eksplisit, dan hitungan acuan berasal dari penghitungan visual pada video, bukan dari hitungan panen aktual. Pencacahan berlangsung pada sabuk pengangkut, sehingga persoalan buah yang tampak dari beberapa sudut pada pohon tidak muncul.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai berurutan, dengan mekanisme pelacakan antarbingkai berbasis penugasan Kuhn-Munkres pada matriks biaya jarak. Objek yang sama dilacak sepanjang lintasannya di ROI sehingga dihitung satu kali. Pencacahan tidak dilaporkan per kelas (hanya satu jenis buah tanpa kelas kematangan). Acuan hitungan berupa penghitungan visual manual pada video, setiap detik, bukan data panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi terbatas. Prinsip penugasan optimal antar-deteksi pada matriks biaya dan manajemen siklus hidup lintasan dapat dipakai sebagai komponen pelacakan antarbingkai. Namun, adegan sabuk pengangkut dengan gerak satu arah dan buah yang terpisah tidak menyerupai tajuk pohon sawit dengan oklusi, dan makalah tidak membahas pencocokan lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `serafino2020detection`.

Serafino dkk. (2020) mengembangkan pencacahan lemon waktu-nyata pada sabuk pengangkut mesin pemanen dengan Raspberry Pi 4 dan kamera RGB beresolusi rendah, memakai indeks warna, segmentasi CIELAB, morfologi, dan pelacakan Kuhn-Munkres. Pada enam video panen, hitungan algoritma terhadap hitungan visual memberi R² 0,997 dan galat rata-rata 4,45%.

Catatan verifikasi data: R² 0,997, persamaan y = 0,96x + 0,187, galat 4,45%, dan "di atas 95%" tertulis pada Bagian III dan IV (Gambar 10 untuk regresi). Enam video, durasi rata-rata 25 detik, dan resolusi 640x480 tertulis pada Abstrak dan Bagian III. Jumlah buah total, hasil per video, lokasi kebun, serta waktu pemrosesan tidak dilaporkan dan tidak dapat diverifikasi dari teks. Teks makalah berbahasa Spanyol; ekstraksi PDF terbaca baik, rumus indeks pada persamaan (1) dan (2) hanya terbaca sebagian (R-B dan G-B).
