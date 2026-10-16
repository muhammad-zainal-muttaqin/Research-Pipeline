# Fruit Mapping with Shape Completion for Autonomous Crop Monitoring

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `marangoz2022fruit` |
| Judul asli | Fruit Mapping with Shape Completion for Autonomous Crop Monitoring |
| Penulis | Marangoz, Salih; Zaenker, Tobias; Menon, Rohit; Bennewitz, Maren |
| Tahun | 2022 |
| Venue | IEEE International Conference on Automation Science and Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [marangoz2022fruit.pdf](../pdf/marangoz2022fruit.pdf)
- DOI resmi: https://doi.org/10.1109/case49997.2022.9926466

## Gambaran Umum
Makalah ini (arXiv:2203.15489, Universitas Bonn) menyajikan sistem pemetaan buah dan estimasi bentuknya pada tanaman paprika manis (*sweet pepper*) di rumah kaca. Segmentasi buah pada citra RGB menghasilkan masker, yang dipadukan dengan citra kedalaman untuk membentuk awan titik (*point cloud*) khusus buah. Rangkaian awan titik digabung menjadi peta berbasis *truncated signed distance field* (TSDF) dengan pustaka voxblox, permukaan peta dikelompokkan menjadi buah individual, dan setiap kelompok dicocokkan dengan satu *superellipsoid* melalui optimasi. Parameter *superellipsoid* memberi posisi dan volume buah, termasuk untuk buah yang hanya teramati sebagian.

Evaluasi kuantitatif dilakukan pada tiga skenario simulasi Gazebo (lengan robot UR5e dengan kamera RGB-D; masing-masing 20 percobaan selama tiga menit perencanaan) yang memuat 14, 28, dan 47 buah merah. Dengan syarat akurasi volume minimum 0,5, sistem mendeteksi rata-rata 7,7, 17,7, dan 27,2 buah, dibandingkan 4,7, 6,0, dan 12,4 buah pada pendekatan lama berbasis *octree*. Selain itu disajikan hasil kualitatif pada data rumah kaca komersial.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan tanaman otonom sulit karena struktur tanaman yang kompleks: daun menutupi buah sehingga, bahkan dengan banyak pandangan, buah sering hanya terliput sebagian. Estimasi bentuk dan volume buah dari informasi parsial diperlukan bagi estimasi hasil dan pemetikan otomatis. Penulis mengelompokkan karya terdahulu dalam tiga kategori: rekonstruksi lengkap (cocok untuk data acuan dan kondisi laboratorium, mahal komputasi, dan tidak lengkap bila ada oklusi), perencanaan sudut pandang tanpa penyelesaian bentuk, dan penyelesaian bentuk geometris dari satu atau sedikit pandangan tanpa perencana sudut pandang.

Karya sebelumnya dari kelompok yang sama memakai perencana sudut pandang berbasis *region of interest* dengan peta *octree*, tetapi estimasi volumenya tidak akurat karena tidak ada pemodelan bentuk untuk bagian buah yang tidak teramati.

## Ide Utama
Peta khusus buah dibuat terpisah dari peta lingkungan, sehingga hanya titik buah yang digabung dari banyak pandangan. Pada peta itu, kelompok titik permukaan dicocokkan dengan *superellipsoid* sebagai model bentuk. Karena model parametrik memiliki bentuk penuh, buah yang hanya separuh teramati tetap memperoleh perkiraan bentuk dan volume lengkap. Identitas buah antar-pandangan diselesaikan secara implisit oleh peta: titik dari berbagai pandangan masuk ke koordinat dunia yang sama dan menjadi satu kelompok.

## Cara Kerja Langkah demi Langkah
```
 Citra warna --> Masker buah --+
                               +--> Awan titik buah --> voxblox (TSDF)
 Citra kedalaman --------------+                              |
                                                              v
   Volume + posisi <-- Superellipsoid <-- Klaster Euclidean <-- Awan titik permukaan
```

### 1. Akuisisi data
Pada simulasi, lengan UR5e dengan kamera RGB-D di flensa digerakkan otomatis oleh perencana sudut pandang. Skenario 1 memakai lengan pada tiang statis (4 tanaman, 14 buah). Skenario 2 memakai lengan pada tiang yang dapat ditarik dari langit-langit (4 tanaman, 28 buah). Skenario 3 memakai lingkungan baru dengan lengan yang dapat ditarik (12 tanaman dalam dua baris dengan fase tumbuh berbeda, 47 buah merah). Pada data nyata, rekaman dari rumah kaca kapsikum memakai sensor RealSense L515 beserta konfigurasi lengan dan pose kamera; jumlah citra dan tanaman tidak dilaporkan.

### 2. Deteksi buah
Dua metode tersedia: pengambangan warna untuk piksel merah (dipakai pada simulasi yang hanya berisi paprika merah) dan jaringan saraf yang dilatih pada set data Universitas Bonn (dipakai pada data nyata). Piksel buah dicocokkan dengan awan titik kedalaman, dan pencilan dihapus dengan penghapusan pencilan statistik.

### 3. Pemetaan TSDF
voxblox dikonfigurasi dengan voksel TSDF 0,004 m dan 64 voksel per sisi. Fitur pelacakan ICP dimatikan dan posisi kamera diambil dari umpan balik lengan robot.

### 4. Klasterisasi dan pencocokan bentuk
Permukaan peta diklasterkan dengan ekstraksi klaster Euclidean (toleransi 0,01 m, ukuran minimum 100 titik, maksimum 10.000 titik). Pusat klaster diestimasi dari normal titik dengan solusi kuadrat terkecil berbentuk tertutup dan regularisasi L2 ($\lambda = 2{,}5$). *Superellipsoid* memiliki 11 parameter ($a, b, c, \varepsilon_1, \varepsilon_2$, translasi, dan tiga rotasi) yang diinisialisasi dengan $a = b = c = 0{,}05$ m dan $\varepsilon_1 = \varepsilon_2 = 0{,}5$. Fungsi biaya meminimalkan jumlah kuadrat jarak hampiran titik ke permukaan ditambah prior pusat dan prior agar $a$, $b$, $c$ berdekatan, dengan $\alpha = \gamma = 0{,}1$. Optimasi memakai Levenberg-Marquardt (Ceres) dengan batas $a, b, c$ antara 0,02 dan 0,15 m, $\varepsilon_1, \varepsilon_2$ antara 0,3 dan 0,9, dan paling banyak 100 iterasi; optimasi yang tidak konvergen dibuang.

### 5. Volume dan pencocokan dengan acuan
Volume dihitung dengan rumus fungsi beta untuk *superellipsoid*. Pada simulasi, acuan dibuat dengan mencocokkan *superellipsoid* pada awan titik dari model mesh buah. Buah terdeteksi dicocokkan dengan acuan bila jarak pusat kurang dari 20 cm dan akurasi volume ($\mathrm{acc}_V = 1 - |V_{det} - V_{gt}|/V_{gt}$) melebihi batas minimum.

## Eksperimen dan Hasil
Metrik: jumlah buah terdeteksi, jarak pusat rata-rata (cm), dan akurasi volume. Variasi: tanpa batas akurasi ("all"), akurasi minimum 0 (MA0; volume terdeteksi tidak lebih dari dua kali acuan), dan akurasi minimum 0,5 (MA50). Pendekatan lama (Old) memakai volume kotak pembatas klaster *octree*; pendekatan baru (SE) memakai volume *superellipsoid*. Nilai rata-rata pada akhir episode (Gambar 3g sampai 3i), dengan simpangan baku sebagaimana pada makalah dihilangkan di sini:

| Skenario (buah acuan) | Variasi | Buah: Old | Buah: SE | Jarak pusat Old (cm) | Jarak pusat SE (cm) | Akurasi volume Old | Akurasi volume SE |
|---|---|---|---|---|---|---|---|
| 1 (14) | all | 12,8 | 13,2 | 2,5 | 2,9 | −0,12 | 0,26 |
| 1 (14) | MA0 | 8,7 | 9,8 | 2,6 | 2,3 | 0,45 | 0,69 |
| 1 (14) | MA50 | 4,7 | 7,7 | 1,6 | 1,9 | 0,65 | 0,81 |
| 2 (28) | all | 25,5 | 26,5 | 2,2 | 1,8 | −0,05 | 0,35 |
| 2 (28) | MA0 | 16,4 | 22,4 | 2,1 | 1,4 | 0,35 | 0,67 |
| 2 (28) | MA50 | 6,0 | 17,7 | 1,8 | 1,2 | 0,66 | 0,78 |
| 3 (47) | all | 41,1 | 40,9 | 2,4 | 1,9 | −0,19 | 0,22 |
| 3 (47) | MA0 | 28,0 | 33,6 | 2,5 | 1,3 | 0,44 | 0,70 |
| 3 (47) | MA50 | 12,4 | 27,2 | 2,1 | 1,2 | 0,71 | 0,80 |

Penulis menyatakan jumlah buah tanpa batas akurasi hampir sama pada kedua pendekatan, tetapi dengan batas akurasi minimum pendekatan baru mendeteksi jauh lebih banyak buah. Jarak pusat rata-rata serupa. Akurasi volume rata-rata untuk semua buah rendah (0,22 sampai 0,35) karena klaster yang menggabungkan buah berdekatan menghasilkan bentuk berlebih dengan akurasi negatif. Setelah pencilan dibuang dengan asumsi ukuran buah maksimum, akurasi rata-rata menjadi 0,67 sampai 0,70 (dibandingkan 0,35 sampai 0,45 pada pendekatan lama), yang mencakup rata-rata lebih dari 70% buah terdeteksi pada Skenario 1 dan lebih dari 80% pada Skenario 2 dan 3. Pada pendekatan lama, jumlah buah dengan akurasi minimum menurun di akhir karena buah berdekatan tergabung menjadi satu.

Pada data rumah kaca nyata, hasil hanya kualitatif: peta lebih akurat dan bentuk buah lebih baik didekati dibandingkan peta *octree* lama (Gambar 4 dan 5); tidak ada angka.

## Kelebihan dan Keterbatasan
Kelebihan: bentuk dan volume dapat diestimasi untuk buah yang teramati sebagian, peta berbasis TSDF berjalan pada satu inti CPU, kerangka kerja berbasis ROS yang terintegrasi dengan perencana sudut pandang, dan evaluasi terhadap acuan volume pada simulasi.

Keterbatasan yang dinyatakan penulis: klasterisasi masih dapat gagal bila titik buah yang terdeteksi tidak cukup dan buah yang berdekatan tergabung sehingga volume terlalu besar; penulis juga merencanakan memakai bentuk hasil estimasi untuk memandu perencana sudut pandang pada pekerjaan mendatang.

Menurut pembacaan ringkasan ini: (1) evaluasi kuantitatif hanya pada simulasi dengan buah merah dan deteksi berbasis ambang warna, sehingga ketangguhan pada deteksi nyata tidak terukur; (2) hasil nyata hanya kualitatif tanpa acuan; (3) posisi kamera diambil dari lengan robot, yang tidak tersedia pada pemindaian lapangan yang digerakkan secara bebas; (4) buah acuan terhitung 14, 28, dan 47, tetapi jumlah terdeteksi dengan akurasi memadai (MA50) masih jauh di bawahnya pada Skenario 1 dan 3.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari banyak pandangan melalui rekonstruksi 3D: awan titik buah dari tiap pandangan digabung ke satu peta TSDF dalam koordinat dunia (dengan pose kamera dari lengan robot), sehingga buah yang sama dari pandangan berbeda berbagi lokasi yang sama dan menjadi satu klaster. Identitas buah ditetapkan melalui klasterisasi spasial, bukan pelacakan ID. Hitungan tidak dilaporkan per kelas; hanya buah merah yang dipertimbangkan. Acuan hitung adalah model simulasi (14, 28, dan 47 buah), bukan panen, hitungan lapangan, ataupun anotasi citra.

Yang dapat dipindahkan ke tandan sawit multi-sisi adalah gagasan menggabungkan pengamatan lintas pandang dalam satu kerangka koordinat bersama dan mengklasterkan menjadi objek individual, serta penyelesaian bentuk untuk objek yang tertutup sebagian. Keterbatasan pemindahan: metode ini bergantung pada pose kamera yang diketahui dan awan titik kedalaman yang rapat pada jarak dekat dengan tanaman kecil, sedangkan pohon sawit tinggi dan kedalaman lapangan lebih bising.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `marangoz2022fruit`.

Marangoz dkk. mengusulkan sistem pemetaan buah paprika manis yang menggabungkan masker buah dan data kedalaman dari banyak pandangan ke dalam peta TSDF, mengelompokkan permukaan menjadi buah individual, dan mencocokkan setiap kelompok dengan *superellipsoid* untuk mengestimasi bentuk dan volume bahkan pada buah yang teramati sebagian. Pada tiga skenario simulasi dengan akurasi volume minimum 0,5, sistem mendeteksi rata-rata 7,7, 17,7, dan 27,2 buah, dibandingkan 4,7, 6,0, dan 12,4 pada pendekatan *octree* sebelumnya.

Catatan verifikasi data: jumlah buah dan akurasi volume dari tabel Gambar 3g sampai 3i, dibaca dari ekstraksi yang terpecah per sel; urutan kolom (Fruits, Center, Vol.) dan baris (Old/SE untuk all, MA0, MA50) direkonstruksi dari label dan konsisten dengan angka 7,7 versus 4,7, 17,7 versus 6,0, dan 27,2 versus 12,4 yang disebut pada teks. Jumlah buah acuan dari keterangan Gambar 3. Parameter optimasi dari Seksi IV-A dan IV-B. Simpangan baku ada pada tabel tetapi tidak disalin di sini. Tidak dapat diverifikasi dari teks: ukuran set data jaringan saraf, jumlah tanaman dan citra pada rekaman rumah kaca nyata, serta kultivar paprika.
