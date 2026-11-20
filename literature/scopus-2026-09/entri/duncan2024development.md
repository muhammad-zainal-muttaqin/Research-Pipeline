# Development of a Cross-Platform Mobile Application for Fruit Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `duncan2024development` |
| Judul asli | Development of a Cross-Platform Mobile Application for Fruit Yield Estimation |
| Penulis | Duncan, Brandon; Bulanon, Duke M.; Bulanon, Joseph Ichiro; Nelson, Josh |
| Tahun | 2024 |
| Venue | Agriengineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [duncan2024development.pdf](../pdf/duncan2024development.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering6020105

## Gambaran Umum

Kajian ini bertujuan membangun aplikasi seluler lintas platform untuk memperkirakan hasil apel kebun Pink Lady. Petani saat ini menghitung buah secara manual dengan memilih sejumlah pohon, menghitung apel per pohon, merata-ratkannya, lalu menerapkan rata-rata itu ke seluruh kebun; proses ini memakan waktu, tenaga, dan kurang tepat. Penulis mengadaptasi aplikasi iOS pendeteksi bunga yang dikembangkan sebelumnya di NNU Robotics Vision Lab menjadi aplikasi penghitung apel untuk iOS dan Android. Tujuan tambahannya adalah memvalidasi algoritme melalui galat persentase mutlak rata-rata (MAPE) dan hubungan antara jumlah apel terdeteksi dan jumlah apel aktual.

Tanaman yang dipelajari adalah apel Pink Lady di Symm's Fruit Ranch, pada satu baris berisi 40 pohon. Citra diambil pada Oktober 2023 dengan Samsung Galaxy Tab S7 berkamera ganda 13 megapiksel, zoom bawaan, tanpa filter, dan jarak sekitar 2,5 m dari pohon. Pengambilan menghasilkan 39 citra sisi timur dan 34 citra sisi barat, sehingga total 73 citra dari 40 pohon; hanya 34 pohon memiliki citra pada kedua sisi. Jumlah apel aktual dihitung manual per cabang menggunakan kliker sekitar satu bulan sebelum panen, dan penulis menyebut angka itu sebagai indeks relatif, bukan ukuran pasti. Tidak ada pembagian himpunan latih dan uji yang dinyatakan; penyetelan hyperparameter dilakukan pada kumpulan citra yang sama, pengujian MAPE memakai 34 pohon dengan empat citra per pohon, dan uji kecepatan memakai lima citra.

Aplikasi Fruit Harvest Helper memakai React Native untuk antarmuka pada kedua platform. Back-end iOS ditulis dalam C++, sedangkan back-end Android memakai kombinasi Java dan C++, dengan algoritme deteksi C++ yang sama berbasis OpenCV. Algoritme ini melakukan segmentasi citra berdasarkan rasio warna. Citra asli disalin, dipisah menjadi kanal biru, hijau, dan merah, lalu salinan citra dan ketiga kanal diubah ke skala abu-abu. Rasio tiap kanal dihitung terhadap citra abu-abu keseluruhan dan dimasukkan ke dua persamaan klasifikasi: pixelEval1 = 0,4·redRatio − 0,2·greenRatio − 0,3·blueRatio dan pixelEval2 = 0,35·redRatio − 0,15·greenRatio − 0,3·blueRatio − 0,02. Piksel yang memenuhi kriteria ditandai putih dan sisanya hitam. Tahap pasca-olahan melakukan opening morfologis (erosi lalu dilatasi), membuang gugus di bawah ambang ukuran minimum, dan menggambar kotak pembatas hijau pada gugus apel yang tersisa. Penghitungan dilakukan dengan menghitung apel di dalam kotak pembatas pada batas pohon yang digambar manual, menjumlahkan hasil citra timur dan barat, lalu menerapkan korelasi untuk memperkirakan hasil panen.

Penulis menghitung tiga nilai MAPE dan melaporkan nilai terendah, 8,52 persen, yang diperoleh ketika citra kedua sisi pohon digabungkan. Acuan hitungnya adalah jumlah apel yang dihitung manual pada citra asli, dibandingkan dengan jumlah apel di dalam kotak pembatas pada citra olahan, untuk 34 pohon yang memiliki citra timur dan barat. Korelasi Pearson antara jumlah apel terdeteksi dan jumlah apel aktual pada 34 pohon mencapai sekitar 0,6 dan signifikan secara statistik dengan p = 0,000197. Waktu pemrosesan rata-rata pada lima citra adalah 1,16 s di Android dan 0,14 s di iOS; penulis menyatakan Android lebih lambat karena memakai JNI pada back-endnya. Aplikasi belum dirilis untuk umum dan korelasi belum diterapkan langsung pada keluaran jumlah apel di antarmuka.

Penulis menyebut sejumlah batasan. Algoritme berbasis warna menghasilkan deteksi palsu pada pita oranye, cahaya matahari, daun cokelat tua, dan mobil merah. Ambang ukuran gugus minimum menekan deteksi palsu, tetapi melewatkan apel kecil; penulis menyarankan pengambilan citra dari jarak sekitar 2,5 m dan tidak memakai aplikasi pada pohon sangat besar. Apel yang seluruhnya hijau tidak terdeteksi karena persamaan klasifikasi mengutamakan merah, sedangkan upaya menambah peka terhadap hijau justru membuat daun terdeteksi sebagai apel. Batas pohon masih harus ditentukan manual karena pohon berdekatan dan saling bertumpang tindih. Data berasal dari satu kebun dengan dua kondisi pencahayaan, sehingga penulis belum dapat menyimpulkan kinerja pada kebun lain. Penulis mengusulkan penggantian algoritme dengan pendekatan pembelajaran mesin, pengujian lapangan tanpa bantuan manusia, dan perluasan ke jenis buah lain.
