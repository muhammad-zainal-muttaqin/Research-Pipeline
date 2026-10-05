# Fruit Detection and Yield Mass Estimation from a UAV Based RGB Dense Cloud for an Apple Orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hobart2025fruit` |
| Judul asli | Fruit Detection and Yield Mass Estimation from a UAV Based RGB Dense Cloud for an Apple Orchard |
| Penulis | Hobart, Marius; Pflanz, Michael; Tsoulias, Nikos; Weltzien, Cornelia; Kopetzky, Mia; Schirrmann, Michael |
| Tahun | 2025 |
| Venue | Drones |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [hobart2025fruit.pdf](../pdf/hobart2025fruit.pdf)
- DOI resmi: https://doi.org/10.3390/drones9010060

## Gambaran Umum
Makalah ini mengembangkan prosedur otomatis untuk mendeteksi apel matang dan memperkirakan massa hasil panen langsung dari awan titik padat (*dense point cloud*) RGB yang dibangun secara fotogrametri dari citra pesawat nirawak (*unmanned aerial vehicle*, UAV). Penelitian dilakukan di kebun apel di Marquardt, Brandenburg, Jerman, pada varietas 'Gala' dan 'Jonaprince'. Kamera RGB kelas konsumen dipasang pada oktokopter dan diterbangkan pada dua ketinggian rendah, yaitu 7,5 m dan 10 m, dengan sudut pandang miring terhadap dinding tajuk.

Apel diidentifikasi dari titik berwarna merah dalam awan titik, dikelompokkan dengan DBSCAN, lalu setiap kelompok dicocokkan dengan bola tiga dimensi untuk memperoleh posisi dan volume. Massa per blok dihitung dari volume bola dikalikan kerapatan rerata varietas. Koefisien determinasi ($R^2$) model jumlah apel per blok berkisar 0,40 sampai 0,53, sedangkan $R^2$ model massa hasil panen adalah 0,56 (ketinggian 7,5 m) dan 0,76 (ketinggian 10 m) menurut abstrak dan Bagian 3.3. Penulis menyimpulkan bahwa ketinggian 10 m lebih baik daripada 7,5 m.

Makalah ini tidak melakukan pencacahan per kelas dan tidak membahas identitas buah lintas pandang secara eksplisit; penyatuan observasi terjadi implisit melalui rekonstruksi 3D dari citra yang saling tumpang tindih.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Informasi posisi dan volume buah sebelum panen membantu perkiraan hasil, pengelolaan budi daya yang spesifik lokasi, dan keputusan penyimpanan pascapanen. Citra satelit dinilai kurang rinci untuk tingkat pohon, sedangkan penilaian manual terlalu padat karya. Estimasi ukuran buah dari citra 2D memerlukan target kalibrasi atau data jarak tambahan, sedangkan sensor 3D berbasis darat (LiDAR, RGB-D, stereo multi-pandang) akurat tetapi memakan waktu, tenaga, dan biaya.

UAV dipandang fleksibel, murah, dan dapat diulang, tetapi deteksi buah pada tajuk sulit karena buah tertutup buah lain atau daun. Penulis menyatakan bahwa estimasi massa hasil panen langsung dari awan titik RGB fotogrametri jarang dilakukan. Tiga hipotesis diuji: (1) posisi dan ukuran apel matang dapat diturunkan otomatis dari awan titik RGB UAV; (2) volume apel yang ditemukan dapat dipakai memperkirakan massa panen; (3) ketinggian terbang memengaruhi mutu estimasi massa.

## Ide Utama
Gagasan utamanya adalah memperlakukan awan titik fotogrametri berwarna sebagai sumber langsung parameter buah, tanpa pelatihan jaringan saraf. Rute terbang diarahkan sejajar baris pohon pada ketinggian rendah dengan kamera miring, sehingga dinding tajuk baris tetangga tampak tanpa halangan dan rasio sinyal terhadap derau meningkat. Buah dikenali dari warna merah (ruang HSV) dan bentuk bola, lalu volumenya dikonversi menjadi massa melalui kerapatan rerata varietas.

## Cara Kerja Langkah demi Langkah

### 1. Lokasi dan akuisisi data
Pengukuran dilakukan pada 4 September 2018 dan 7 September 2020 di kebun seluas 0,5 ha berisi 1.334 pohon. Empat baris dipilih tiap kampanye (baris 7–10 pada 2018; baris 2–5 pada 2020), masing-masing 112 pohon, dengan luas gabungan 1.200 m². Varietas 'Gala' (n = 240) dan 'Jonaprince' (n = 180) ditanam bersama pohon penyerbuk 'Red Sentinel' (n = 16) dan 'Red Idared' (n = 12). Jarak baris 5 m, jarak pohon 0,75 m, tinggi dinding tajuk sekitar 3,0 m, lebar sekitar 1 m. Baris dibagi menjadi 14 blok berisi delapan pohon.

Kamera Sony α-6000 (lensa 16 mm, ISO 400) dipasang pada oktokopter dengan gimbal dua sumbu. Satu kampanye terdiri atas satu terbang kontur dan dua terbang rinci sepanjang baris. Kecepatan 0,4 m/s (7,5 m) dan 0,5 m/s (10 m), sudut vertikal 53° dan 46°, serta jarak sampel pada dinding tajuk 1,9 mm dan 2,4 mm. Jumlah citra (diambil/disejajarkan, Tabel 1): 2018 pada 7,5 m 407/406 dan pada 10 m 342/342; 2020 pada 7,5 m 1.802/1.802 dan pada 10 m 1.222/1.200. Pelat penanda dengan koordinat GNSS-RTK dipakai untuk georeferensi.

### 2. Pembuatan awan titik
Citra ARW dikonversi ke TIFF 16-bit, lalu awan titik dibangun dengan Metashape Professional 1.8.4. Awan titik jarang disaring bertahap berdasarkan galat reproyeksi, ketidakpastian rekonstruksi, dan akurasi proyeksi (Tabel A1), dengan optimasi penyejajaran setelah tiap langkah. Awan titik padat dihitung dengan akurasi tinggi dan penyaringan kedalaman ringan.

### 3. Identifikasi apel dan estimasi volume
- Titik tanah dan pohon dipisahkan dengan *cloth simulation filter* di CloudCompare, lalu awan dipotong menjadi blok delapan pohon dengan paket `lidR` di R.
- Warna RGB diubah ke HSV; hanya titik dengan hue 0,00–0,04 atau 0,96–1,00 yang dipertahankan, dan titik putih (kecerahan lebih dari 0,75 atau saturasi kurang dari 0,25) dibuang.
- Titik merah dikelompokkan dengan DBSCAN. Parameter terpilih: jarak klaster (epsilon) 0,015 m dan jumlah titik minimum 6 (Tabel 2). Klaster yang lebih besar dari dua kali diameter apel rerata dipecah dengan k-means (Hartigan dan Wong).
- Bola 3D dicocokkan pada tiap klaster dengan `pyransac3d` (algoritma PGP2X). Bola dengan jari-jari di luar 1,8–5,8 cm dibuang; pada tumpang tindih lebih dari 10%, bola yang menyimpang dari r = 4,25 cm dihapus.
- Titik dalam bola yang terverifikasi dihapus dari awan blok dan proses diulang empat kali untuk menemukan apel yang terlewat.

### 4. Konversi volume ke massa
Kerapatan rerata dihitung dari lebih dari 100 sampel apel matang per varietas: 1459,73 kg/m³ untuk 'Gala' dan 1465,39 kg/m³ untuk 'Jonaprince'. Faktor ini dikalikan dengan volume bola.

## Eksperimen dan Hasil
Acuan berupa hitung manual jumlah apel per blok dan massa hasil panen per blok. Model dioptimalkan pada satu blok uji per tahun terhadap selisih jumlah apel. Awan titik 7,5 m tahun 2020 tidak menghasilkan keluaran karena beberapa awan titik tumpang tindih menyebabkan pergeseran titik. Baris terakhir yang diterbangkan pada tiap tahun memiliki $R^2$ sangat rendah (baris 10 tahun 2018: 0,00 pada 7,5 m dan 0,03 pada 10 m; baris 5 tahun 2020: 0,06 pada 10 m) karena sisi luar tajuk tertangkap pada lebih sedikit citra, sehingga baris itu dikeluarkan dari analisis lanjutan.

| Keluaran | Ketinggian | Data | $R^2$ |
|---|---|---|---|
| Jumlah apel per blok | 7,5 m | 2018 | sekitar 0,41 |
| Jumlah apel per blok | 10 m | 'Gala' | 0,40 |
| Jumlah apel per blok | 10 m | 'Jonaprince' | 0,53 |
| Massa hasil panen per blok | 7,5 m | gabungan | sekitar 0,56 |
| Massa hasil panen per blok | 10 m | gabungan | sekitar 0,76 (abstrak, Bagian 3.3) |

Model cenderung menaksir rendah jumlah apel karena daun menutupi sebagian buah. Awan titik 7,5 m menemukan lebih banyak apel tetapi dengan sebaran posisi lebih lebar dan taksiran massa sekitar 20 kg (minimum) sampai 40 kg (maksimum) lebih tinggi dibandingkan awan titik 10 m. Acuan massa per blok berkisar 35–125 kg pada 2018 dan 63–168 kg pada 2020; taksiran 2020 masih terlalu tinggi dan dua blok melampaui 255 kg. Dalam pembahasan, penulis membandingkan hasilnya dengan studi lain: $R^2$ jumlah buah 0,8–0,85 dan massa 0,57–0,71 pada citra darat (Zhou dkk.), serta recall 74–90% pada awan titik 3D berbasis darat (Zine-El-Abidine dkk.); keduanya lebih baik untuk jumlah buah.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: perangkat keras murah, prosedur sepenuhnya otomatis, keluaran berupa posisi, jumlah, volume, dan massa apel per blok yang dapat dipetakan, serta tidak memerlukan data latih berlabel.

Keterbatasan yang dinyatakan penulis: kualitas hasil bergantung pada mutu awan titik, yang dipengaruhi pengaturan terbang; jumlah apel ditaksir rendah akibat oklusi daun; baris terakhir yang diterbangkan memiliki cakupan data lebih rendah; satu set data (7,5 m, 2020) gagal; pengaruh cahaya sekitar tidak diteliti; $R^2$ jumlah apel (0,4–0,5) jauh lebih rendah daripada pendekatan berbasis citra darat. Penulis mengusulkan jaringan saraf pada awan titik 3D dan penyelesaian bentuk buah sebagai pekerjaan lanjutan.

Menurut pembacaan ringkasan ini, evaluasi hanya berupa regresi pada tingkat blok sehingga galat per buah (presisi, recall, atau identitas buah) tidak dilaporkan. Pemisahan buah yang bergerombol bergantung pada ambang jarak dan warna merah yang hanya cocok untuk apel yang matang. Hanya dua musim dan satu kebun yang diuji, dan hanya tiga dari empat awan titik yang menghasilkan keluaran.

## Kaitan dengan Tinjauan main6
Makalah ini tidak mengelola identitas buah lintas pandang secara eksplisit, tetapi buah yang tampak pada banyak citra tumpang tindih (tumpang tindih maju sekitar 90% dan 96%) dilebur menjadi satu objek 3D melalui rekonstruksi *structure-from-motion*. Setiap apel dihitung satu kali sebagai bola di ruang dunia; mekanismenya adalah penyatuan geometris pada awan titik, bukan pelacakan atau pencocokan antarcitra. Penghitungan tidak dilaporkan per kelas, karena hanya apel matang berwarna merah yang dideteksi. Acuan hitungnya adalah hitung manual jumlah apel per blok dan massa panen per blok.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menyatukan pengamatan melalui ruang 3D bersama, penyaringan warna lalu klasterisasi, serta penghapusan titik buah yang telah terverifikasi agar buah tersisa dapat ditemukan pada iterasi berikutnya. Keterbatasan pemindahan: pemisahan berbasis warna merah tunggal tidak mencakup beberapa kelas kematangan, dan oklusi pelepah sawit serta ukuran tandan jauh berbeda dari apel.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hobart2025fruit`.

Hobart dkk. (2025) mengusulkan prosedur otomatis untuk mendeteksi apel matang dan memperkirakan massa panen dari awan titik padat RGB hasil fotogrametri citra UAV miring berketinggian rendah. Apel diidentifikasi melalui penyaringan hue HSV, klasterisasi DBSCAN, dan pencocokan bola 3D, lalu volumenya dikalikan kerapatan varietas. Pada kebun 0,5 ha dengan varietas 'Gala' dan 'Jonaprince', $R^2$ jumlah apel per blok adalah 0,40–0,53, sedangkan $R^2$ massa per blok mencapai 0,56 (ketinggian 7,5 m) dan 0,76 (ketinggian 10 m), dengan kecenderungan menaksir rendah jumlah apel akibat oklusi daun.

Catatan verifikasi data: angka $R^2$ jumlah apel (0,41; 0,40; 0,53) terdapat di abstrak dan Bagian 3.2 (Gambar 9); $R^2$ massa 0,56 dan 0,76 terdapat di abstrak dan Bagian 3.3 (Gambar 10). Bagian Kesimpulan menulis $R^2$ massa untuk 10 m sebesar 0,71, yang tidak konsisten dengan nilai 0,76 di bagian lain; ringkasan ini memakai 0,76 sambil mencatat ketidakkonsistenan tersebut. Jumlah citra berasal dari Tabel 1, parameter klaster dari Tabel 2, dan kerapatan apel dari Bagian 3.1. Data pada gambar tidak terbaca dari teks, sehingga jumlah apel absolut dan galat per blok tidak dapat diverifikasi. Teks ekstraksi memuat satu kesalahan cetak pada spesifikasi kamera ("24.7.5 megapixel"), yang tidak dipakai.
