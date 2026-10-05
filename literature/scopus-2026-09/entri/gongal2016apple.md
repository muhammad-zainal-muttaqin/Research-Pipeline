# Apple crop-load estimation with over-the-row machine vision system

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gongal2016apple` |
| Judul asli | Apple crop-load estimation with over-the-row machine vision system |
| Penulis | Gongal, A.; Silwal, A.; Amatya, S.; Karkee, M.; Zhang, Q.; Lewis, K. |
| Tahun | 2016 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gongal2016apple.pdf](../pdf/gongal2016apple.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2015.10.022

## Gambaran Umum
Makalah ini mengembangkan sistem penglihatan mesin untuk estimasi beban hasil (*crop-load*) apel, yaitu jumlah apel per pohon, dengan platform di atas barisan tanaman (*over-the-row*, OTR). Platform memotret kanopi dari dua sisi berlawanan di dalam terowongan berpenutup tarpaulin dengan pencahayaan LED terkendali. Data diambil pada kebun komersial apel kultivar 'Jazz' berarsitektur *tall spindle* di Prosser, Washington, pada tahun 2013, satu sampai empat minggu sebelum panen.

Apel diidentifikasi dari citra warna berdasarkan warna dan bentuk, lalu lokasi 3D apel dari kamera *time-of-flight* (ToF) dipakai untuk mengenali apel yang terlihat dari kedua sisi sehingga tidak dihitung dua kali. Pada 20 pohon, galat persentase absolut rerata (*mean absolute percentage error*, MAPE) hitungan total adalah 18% untuk pencitraan dua sisi, dibandingkan 42% dan 41% untuk masing-masing satu sisi. Abstrak menyatakan akurasi 82% untuk dua sisi dan 58% untuk satu sisi.

Galat identifikasi apel (MAPE 21,2%) dan galat identifikasi apel duplikat (MAPE 21,1%) berada pada tingkat yang mirip. Penulis menyebut tingkat itu cukup untuk membuktikan konsep, bukan sebagai sistem final.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi beban hasil dibutuhkan untuk penjarangan buah muda, perencanaan tenaga kerja dan alat panen, pengangkutan ke rumah pengemasan, serta asuransi hasil. Model perkiraan berbasis parameter kebun memakan waktu karena parameter harus diukur per kebun. Model berbasis indeks vegetasi citra hiperspektral atau multispektral terbatas oleh variasi iklim, kultivar, dan lokasi. Penghitungan manual berbasis pengambilan sampel acak membutuhkan tenaga kerja besar dan dapat bias.

Penelitian pencitraan sebelumnya umumnya menilai akurasi berdasarkan apel yang tampak pada citra satu sisi kanopi, padahal jumlah itu dapat jauh berbeda dari jumlah apel sebenarnya pada pohon. Pengamatan lapangan penulis menunjukkan hanya sekitar 60% apel terlihat dari satu sisi kanopi, bahkan pada kebun *tall spindle* modern, karena terhalang daun, batang, dan apel lain. Studi yang dikutip makalah melaporkan akurasi 60% (stereo malam hari dengan banyak apel bergerombol) dan 40–60% (tanpa koreksi apel tak terlihat), sedangkan korelasi hitungan citra dengan hitungan manual bersifat khusus per kebun dan dapat berubah antartahun. Faktor kedua adalah pencahayaan luar ruang yang berubah, yang menyulitkan segmentasi.

## Ide Utama
Dua sisi kanopi dipotret agar jumlah apel yang tak terlihat berkurang, dan terowongan dengan lampu LED dipakai agar cahaya seragam. Risiko hitungan ganda pada apel yang tampak dari kedua sisi diatasi dengan memetakan apel dari kedua sisi ke satu sistem koordinat 3D dan menganggap dua apel sebagai satu apel yang sama bila jaraknya kurang dari ambang. Hitungan akhir per pohon adalah jumlah apel terdeteksi dari sisi A dan sisi B dikurangi jumlah apel duplikat.

```
  Citra warna + citra 3D (ToF), sisi A dan sisi B, lima tinggi kamera
        |
  Identifikasi apel 2D (warna, bentuk)
        |
  Ko-registrasi 2D-3D, lalu transformasi ke koordinat global
        |
  Jarak antarpusat apel < 0,075 m  ->  apel duplikat
        |
  Hitungan = (A + B) - duplikat
```

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Platform OTR berukuran 2,13 m (panjang) x 2,74 m (lebar) x 3,67 m (tinggi) dipasang pada *three-point hitch* traktor. Kamera warna Prosilica GigE 1290c (resolusi 1280 x 960, bidang pandang 43,6 derajat x 33,4 derajat) dan kamera 3D PMD CamCube 3.0 (200 x 200, 40 derajat x 40 derajat) dipasang bertumpuk pada mekanisme geser agar tinggi dapat diatur. Terowongan tarpaulin menghalangi sinar matahari langsung dan LED Trilliant 36 memberi cahaya seragam, termasuk untuk pengambilan malam hari.

Pohon kultivar 'Jazz' berjarak antarbaris 2,74 m dan antartanaman 1,17 m. Citra diambil dari lima tinggi kamera untuk menutupi kanopi penuh. Platform melintasi barisan untuk 20 pohon, menghasilkan 212 citra 3D dan 212 citra warna (total 424). Dari 212 citra warna, 104 diambil saat apel masih hijau dan belum matang, serta 108 saat apel matang dan berwarna merah. Dua orang menghitung apel tiap pohon secara manual dan rerata keduanya menjadi acuan. Apel duplikat (tampak dari kedua sisi) dihitung manual pada citra.

### 2. Identifikasi apel
Metode mengikuti penelitian terdahulu penulis. Citra warna menjalani pemerataan histogram pada ruang warna HSI, filter Wiener adaptif berukuran 5 x 5, lalu pengurangan kanal hijau dan biru dari kanal merah dan ambang Otsu. Objek kecil dibuang (luas kurang dari 100 piksel dan kekompakan kurang dari 190), kemudian deteksi tepi Canny dan *Circular Hough Transform* (CHT) iteratif pada jari-jari 30 sampai 65 piksel dipakai untuk mencari objek bulat. Objek hasil CHT disaring berdasarkan kemerahan. Analisis *blob* (luas di atas 90 piksel, kekompakan di atas 90) menangkap apel yang terlihat sebagian, dan klaster berbasis jarak Euklides dalam radius 65 piksel mencegah satu apel terhitung beberapa kali. Implementasi memakai MATLAB R2012a.

### 3. Ko-registrasi citra 2D dan 3D
Kamera warna dan 3D dikalibrasi dengan papan catur (25 citra pada jarak 1,5 m) memakai *toolbox* kalibrasi MATLAB. Parameter intrinsik dan ekstrinsik (rotasi dan translasi) diperoleh, lalu titik 3D diproyeksikan ke bidang citra warna dengan model *pinhole*.

### 4. Identifikasi apel duplikat dan penghitungan
Apel yang terdeteksi pada citra warna dipetakan ke koordinat 3D, lalu koordinat sisi B ditransformasikan ke sisi A dengan translasi sumbu Z (jarak antarkamera dikurangi Z) dan refleksi sumbu X. Karena platform tidak stabil di medan tidak rata, parameter transformasi disetel dengan cara coba-coba memakai lima apel yang terlihat dari kedua sisi pada setiap pohon. Parameter yang dipakai adalah translasi 0,05 m pada sumbu X dan Y serta 2,4 m atau 2,45 m pada sumbu Z, bergantung pada lokasi. Dua apel dianggap duplikat bila jarak pusatnya kurang dari 0,075 m (tiga perempat diameter rerata apel). Hitungan akhir dibandingkan dengan hitungan manual menggunakan MAPE $= \frac{1}{N}\sum |n_i - n_c|/n_i$, dengan $n_i$ hitungan algoritma dan $n_c$ hitungan manual.

## Eksperimen dan Hasil
Evaluasi mencakup identifikasi apel pada citra, identifikasi apel duplikat, dan hitungan total per pohon pada 20 pohon. Pembanding berupa hitungan satu sisi (sisi A dan sisi B) dengan acuan hitungan manual di lapangan.

| Tahap | Hasil | Sumber di makalah |
|---|---|---|
| Identifikasi apel, MAPE | 21,2% | Tabel 2 |
| Positif palsu dan negatif palsu identifikasi apel | 13,0% dan 33,2% (1.697 apel terdeteksi benar, 843 terlewat, 254 positif palsu) | Tabel 3 |
| Identifikasi apel, tanpa citra apel hijau (3 sampai 4 minggu sebelum panen) | MAPE 12%, positif palsu 13,9%, negatif palsu 25% | Bagian 3.1 |
| Identifikasi apel duplikat, MAPE | 21,1% | Tabel 4 |
| Duplikat: akurasi produsen dan akurasi konsumen | 78,0% dan 93,8% (319 benar, 90 terlewat, 21 salah) | Tabel 5 |
| Hitungan total, dua sisi, MAPE | 18,0% | Tabel 6 |
| Hitungan total, satu sisi, MAPE | 42% (sisi A) dan 41% (sisi B) | Bagian 3.3, Gambar 13 |

Penulis menyatakan galat identifikasi apel merupakan penyebab utama penghitungan di bawah jumlah sebenarnya (*undercounting*). Galat identifikasi duplikat berpengaruh lebih kecil. Positif palsu identifikasi apel dan negatif palsu identifikasi duplikat saling meniadakan sebagian efeknya. Identifikasi duplikat salah terutama pada apel berdekatan atau bergerombol yang bergeser sedikit dalam ruang 3D.

## Kelebihan dan Keterbatasan
Kelebihan: hitungan dua sisi dibandingkan langsung dengan hitungan satu sisi pada pohon yang sama, dan acuan berupa hitungan manual seluruh apel pada pohon. Terowongan dan LED mengurangi variasi pencahayaan, termasuk untuk pengambilan malam hari. Pengenalan duplikat tidak memerlukan korelasi hitungan dengan data manual per kebun.

Keterbatasan yang dinyatakan penulis: algoritma identifikasi dioptimalkan untuk apel merah sehingga apel hijau banyak terlewat. Citra diambil di kebun yang relatif datar dan platform belum mampu berjalan waktu-nyata di lahan miring. Studi dilakukan saat buah sudah berwarna dan berukuran sesuai, bukan awal musim. Ukuran apel dan pemrosesan waktu-nyata belum tersedia, dan peningkatan 3D *sensing* serta registrasi masih diperlukan. Parameter transformasi berbeda sedikit antarlokasi karena ketidakstabilan platform.

Menurut pembacaan ringkasan ini, parameter transformasi disetel dengan lima apel yang terlihat dari kedua sisi pada tiap pohon, sehingga registrasi bergantung pada penandaan manual per pohon. Menurut pembacaan ringkasan ini pula, pengujian hanya mencakup satu kultivar, satu kebun, dan 20 pohon, dan pembagian data untuk menyetel parameter registrasi terhadap data uji tidak dijelaskan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani apel yang terlihat lebih dari sekali, yaitu apel yang tampak dari kedua sisi kanopi. Mekanismenya adalah pencocokan lokasi 3D: deteksi dari kedua sisi dipetakan ke satu sistem koordinat melalui geometri tetap platform (translasi dan refleksi) yang disetel per pohon, lalu apel dengan jarak antarpusat kurang dari 0,075 m dianggap identitas yang sama dan dikurangkan dari hitungan. Ini termasuk koreksi dua sisi dengan identitas berbasis posisi 3D, bukan pelacakan video.

Hitungan tidak dilaporkan per kelas; apel dihitung sebagai satu kelas. Acuan hitung adalah hitungan manual seluruh apel pada pohon di lapangan oleh dua orang (rerata), ditambah hitungan manual apel duplikat pada citra. Untuk tandan kelapa sawit multi-sisi, gagasan yang dapat dipindahkan adalah pengurangan duplikat dengan jarak 3D pada kerangka koordinat bersama dan evaluasi galat duplikat secara terpisah dari galat deteksi. Hambatan pemindahan adalah ketergantungan pada geometri platform dua sisi yang kaku dan pada tinggi kanopi yang rendah. Kelas kematangan tidak ditangani.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gongal2016apple`.

Gongal dkk. mengembangkan platform *over-the-row* bertirai dengan pencahayaan LED untuk memotret kanopi apel 'Jazz' dari dua sisi berlawanan, lalu memakai lokasi 3D dari kamera *time-of-flight* untuk mengenali apel yang terlihat dari kedua sisi dan mencegah penghitungan ganda. Pada 20 pohon, MAPE hitungan total adalah 18% untuk pencitraan dua sisi, dibandingkan 42% dan 41% untuk satu sisi, dengan acuan hitungan manual per pohon. Galat identifikasi apel (MAPE 21,2%) menjadi sumber utama penghitungan di bawah jumlah sebenarnya.

Catatan verifikasi data: MAPE hitungan total 18,0% (Tabel 6), MAPE identifikasi apel 21,17% (Tabel 2), MAPE duplikat 21,1% (Tabel 4), matriks konfusi duplikat (Tabel 5), dan matriks identifikasi apel (Tabel 3) terbaca dari teks. Angka 42% dan 41% diambil dari teks bagian 3.3 dan label Gambar 13. Terdapat ketidakkonsistenan di makalah: abstrak menyebut akurasi identifikasi 79,8% dan galat duplikat 21,1%, sedangkan kesimpulan menyebut 78,9% dan 79%; MAPE 21,2% pada bagian 3.1 setara dengan akurasi sekitar 78,8%, sehingga angka 79,8% pada abstrak tidak dapat dicocokkan dengan teks. Akurasi 82% dan 58% adalah komplemen dari MAPE 18% dan 42% menurut penulis. Ekstraksi teks memotong beberapa angka dan simbol (rumus 1 sampai 3 dan nilai kalibrasi) sehingga tidak dikutip. Jumlah apel total pada 20 pohon tidak dilaporkan secara agregat dalam teks.
