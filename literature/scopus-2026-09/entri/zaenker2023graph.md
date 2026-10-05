# Graph-Based View Motion Planning for Fruit Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zaenker2023graph` |
| Judul asli | Graph-Based View Motion Planning for Fruit Detection |
| Penulis | Zaenker, Tobias; R\"uckin, Julius; Menon, Rohit; Popovi\'c, Marija; Bennewitz, Maren |
| Tahun | 2023 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [zaenker2023graph.pdf](../pdf/zaenker2023graph.pdf)
- DOI resmi: https://doi.org/10.1109/iros55552.2023.10342532

## Gambaran Umum
Makalah ini mengusulkan perencana gerak sudut pandang berbasis graf (*graph-based view motion planning*, VMP) untuk memantau buah paprika manis (*sweet pepper*) dengan lengan robot berkamera RGB-D yang terpasang pada troli di dalam rumah kaca. Perencana membangun graf kandidat pose pandang (*view pose*) yang dapat dijangkau lengan robot, lalu mencari urutan pose dengan akumulasi perolehan informasi tertinggi. Graf dan urutan terbaik dihitung dengan cakrawala terbatas dan diperbarui pada selang waktu tetap saat informasi baru masuk.

Evaluasi dilakukan pada simulasi rumah kaca dengan dua skenario dan pada misi nyata di rumah kaca komersial. Pembandingnya adalah perencana pandang terbaik berikutnya (*next-best view*) tunggal buatan penulis sendiri, yang disebut RVP. Pada Skenario 1 (47 buah), VMP mendeteksi rata-rata 39,2±1,9 buah dan RVP 38,2±3,9 buah. Pada Skenario 2 (94 buah), VMP mendeteksi 87,4±2,9 buah dan RVP 72,2±1,9 buah, masing-masing dari lima kali percobaan.

Makalah ini bukan metode pencacahan lintas pandang. Buah dipetakan dalam satu peta 3D bersama, dan tujuan utamanya adalah cakupan buah dalam waktu misi terbatas.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan tanaman besar dan kompleks seperti paprika sulit karena buah sering tertutup daun. Pendekatan nonadaptif (acak atau pencakupan homogen) tidak memusatkan pengamatan pada wilayah informatif yang ditemukan secara daring. Pendekatan adaptif sebelumnya mengoptimalkan satu pose pandang berikutnya secara rakus (*myopic greedy*), yang menurut penulis cenderung menghasilkan lintasan suboptimal di bawah observabilitas parsial, dan tidak memasukkan perencanaan gerak lengan ke dalam optimasi pose pandang. Akibatnya, lintasan yang direncanakan tidak efisien dijalankan pada ruang kerja terbatas seperti rumah kaca.

## Ide Utama
Perencanaan dipecah menjadi dua prosedur yang dapat diparalelkan. Pertama, graf kandidat pose pandang dibangun dari posisi target yang diambil dari peta 3D. Kedua, pencarian jalur *best-first* pada graf itu memaksimalkan cakupan buah. Setiap sambungan pada graf hanya menghubungkan pose yang berdekatan dan bebas tabrakan, dengan waktu eksekusi disimpan pada sisi graf. Fungsi utilitas menggabungkan perolehan informasi dan waktu eksekusi jalur, sehingga urutan yang dipilih informatif sekaligus cepat dijalankan.

## Cara Kerja Langkah demi Langkah

### 1. Pemetaan
Awan titik dari kamera RGB-D digabungkan ke dalam peta probabilistik 3D OctoMap yang mencatat ruang tidak diketahui, terisi, bebas, dan daerah minat (*regions of interest*, ROI), yaitu gugus buah. Deteksi buah berasal dari proses terpisah yang tidak diuraikan rinci pada makalah ini.

### 2. Pengambilan sampel posisi target
Tiga jenis posisi target diambil dengan peluang yang ditentukan pengguna: batas antara ROI dan ruang tidak diketahui, batas antara ruang terisi dan tidak diketahui, serta batas antara ruang bebas dan tidak diketahui. Himpunan target diambil ulang setelah setiap awan titik baru digabungkan, dan target dipilih seragam acak.

### 3. Pengambilan sampel pose pandang
Pada karya sebelumnya, pose diambil dengan melempar sinar acak dari target. Pada ruang kerja terbatas, pose sering tidak terjangkau, sehingga pose kini diambil acak dari ruang kerja lengan yang telah ditetapkan dengan arah pandang ke target. *Ray-casting* kemudian membuang pose yang tidak melihat target, dan hanya pose yang dapat dijangkau tanpa tabrakan disimpan.

### 4. Pembangunan graf
Tiap pose menjadi simpul dengan konfigurasi sendi lengan. Sisi menghubungkan tiap simpul ke $k$ tetangga terdekat dengan selisih sudut sendi minimal dan lintasan lengan bebas tabrakan. Waktu eksekusi lintasan dihitung dengan MoveIt dan disimpan pada sisi. Pose kamera saat ini ditambahkan sebagai simpul.

### 5. Pencarian jalur
Pencarian dimulai dari simpul pose kamera dan memperluas simpul menurut antrean prioritas berdasarkan utilitas. Pada tiap simpul, sel peta yang terlihat dihitung dengan *ray-casting* dan dimasukkan ke himpunan sel unik sepanjang jalur. Utilitas didefinisikan sebagai

$$U(n_t) = \frac{C(n_t)_{unk}}{L(\psi_t)} \cdot \frac{ROI(\psi_t)+1}{t+1},$$

dengan $C(n_t)_{unk}$ jumlah sel tidak diketahui yang terlihat secara unik, $ROI(\psi_t)$ jumlah pose pada jalur yang menghadap buah terdeteksi, dan $L(\psi_t)$ waktu eksekusi jalur. Jalur terbaik diperoleh dengan menelusuri balik pendahulu bernilai utilitas tertinggi.

### 6. Eksekusi dan perencanaan ulang
Jalur dijalankan sampai jarak pandang ke depan maksimum, lalu direncanakan ulang setelah selang waktu tetap. Sebelum tiap pose, tabrakan diperiksa pada peta terbaru. Bila terjadi tabrakan, eksekusi dibatalkan, sisi dihapus dari graf, dan jalur direncanakan ulang. Pembangunan graf dan pencarian jalur berjalan paralel.

## Eksperimen dan Hasil
Simulasi berisi robot lengan di atas troli yang bergerak sepanjang baris tanaman dan dapat mengangkat lengan secara vertikal. Skenario 1 terdiri atas dua baris, 12 tanaman, dan 47 buah. Skenario 2 terdiri atas dua tingkat vertikal, dua baris, 12 tanaman tiap tingkat, dan 94 buah. Tiap baris dibagi menjadi empat segmen berjarak 1 m (8 segmen pada Skenario 1 dan 16 pada Skenario 2), dan tiap perencana diberi waktu 60 detik per segmen. Lima kali percobaan dilakukan per perencana per skenario, dan dilaporkan rerata serta simpangan baku. Buah dianggap terdeteksi benar bila posisi hasil penaksir bentuk superelipsoid (pembentukan peta buah dengan Voxblox) cocok dengan buah acuan dari model tanaman simulasi.

| Skenario | Jumlah buah | RVP (terdeteksi) | VMP (terdeteksi) |
|---|---|---|---|
| 1 | 47 | 38,2 ± 3,9 | 39,2 ± 1,9 |
| 2 | 94 | 72,2 ± 1,9 | 87,4 ± 2,9 |

Pada Skenario 1, RVP unggul pada segmen awal karena memilih pose jauh yang juga mencakup segmen sebelah, sedangkan VMP mendeteksi dengan laju stabil sehingga hasil akhir keduanya serupa. Pada Skenario 2, VMP lebih unggul pada akhir misi. Waktu antarpose dilaporkan lebih singkat pada VMP, dengan lebih sedikit pencilan waktu perencanaan; nilai numeriknya tidak tertulis pada teks dan hanya tampak pada Gambar 7.

Pada misi nyata di rumah kaca komersial, satu baris paprika dipetakan per segmen pada ketinggian platform tetap. Gambar 8 menunjukkan pose yang mengamati buah dari bawah untuk menghindari daun, dan Gambar 9 menunjukkan gugus buah di sepanjang baris. Acuan buah tidak tersedia, sehingga validasi hanya kualitatif, yaitu sebagian besar gugus buah terpantau.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: perencanaan non-rakus pada graf, pemakaian batasan gerak lengan, lintasan yang lebih pendek dan lebih lurus, serta implementasi ROS yang dibuka untuk umum. Penulis menyatakan bahwa metode sebelumnya cenderung gagal merencanakan lintasan bebas tabrakan pada ruang kerja terbatas.

Keterbatasan yang dinyatakan penulis: pemetaan yang lebih akurat diperlukan untuk memperbaiki rekonstruksi buah dan estimasi perolehan informasi di sepanjang urutan pose, yang disebut sebagai pekerjaan mendatang.

Menurut pembacaan ringkasan ini, pembanding hanya satu perencana milik kelompok penulis yang sama, jumlah percobaan hanya lima per kondisi, dan dasar uji hanya berupa simulasi dengan tanaman model. Percobaan nyata tidak memiliki acuan jumlah buah. Pada Skenario 1 selisih rerata (39,2 dan 38,2) berada di dalam simpangan baku. Perbandingan tidak mencakup pencacahan atau identitas buah.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali sebagai masalah identitas. Buah yang diamati dari banyak pose digabungkan secara implisit pada peta voksel 3D bersama (OctoMap dan Voxblox), lalu dikelompokkan dan dicocokkan dengan superelipsoid; tidak ada pencocokan identitas antarcitra yang dibahas pada makalah ini. Hitungan tidak dilaporkan per kelas; hanya jumlah buah terdeteksi. Acuan hitungnya adalah buah pada model tanaman simulasi, sedangkan pada percobaan nyata tidak ada acuan sama sekali (bukan panen maupun hitung manual).

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan perencanaan pose pandang berdasarkan perolehan informasi agar sisi yang belum teramati dan buah yang tertutup mendapat pandangan tambahan, serta gagasan pemetaan buah dalam kerangka 3D bersama sebagai dasar penyatuan identitas. Kebutuhan lengan robot dan troli di rumah kaca tidak sama dengan pengambilan citra manual di kebun sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zaenker2023graph`.

Zaenker dkk. mengusulkan perencana gerak sudut pandang berbasis graf yang memilih urutan pose kamera dengan utilitas gabungan antara sel tidak diketahui yang terlihat, pose yang menghadap buah, dan waktu eksekusi, untuk memantau paprika dengan lengan robot RGB-D di rumah kaca. Pada simulasi dengan 94 buah, VMP mendeteksi 87,4±2,9 buah dibandingkan 72,2±1,9 buah pada perencana pandang terbaik berikutnya, sedangkan pada simulasi dengan 47 buah hasilnya serupa (39,2±1,9 dan 38,2±3,9).

Catatan verifikasi data: angka deteksi diambil dari teks bagian V-B (Skenario 1 dan 2), dan konfigurasi skenario dari bagian V-A serta Gambar 5. Waktu antarpose hanya disajikan pada Gambar 7 dan tidak tersedia secara numerik pada teks. Persamaan utilitas diambil dari bagian IV-B; ekstraksi PDF memisahkan pembilang dan penyebutnya pada baris-baris terpisah, sehingga bentuk rumus di atas disusun dari urutan itu dan perlu dicek pada PDF. Jumlah citra, model detektor buah, dan jumlah kali eksekusi nyata tidak dilaporkan. Teks makalah secara umum terbaca baik.
