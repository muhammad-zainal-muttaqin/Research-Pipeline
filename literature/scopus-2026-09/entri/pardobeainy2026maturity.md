# Maturity and size estimation with yield mapping for hydroponic strawberries using machine vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pardobeainy2026maturity` |
| Judul asli | Maturity and size estimation with yield mapping for hydroponic strawberries using machine vision |
| Penulis | Pardo-Beainy, Camilo; Parra, Carlos; Solaque, Leonardo |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [pardobeainy2026maturity.pdf](../pdf/pardobeainy2026maturity.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102416

## Gambaran Umum
Makalah ini mengusulkan kerangka penglihatan mesin dan GNSS RTK (*real-time kinematic*) untuk stroberi hidroponik di lahan terbuka. Kerangka itu mendeteksi tiap buah, mengestimasi tingkat kematangan dan dimensi fisiknya, menetapkan buah ke salah satu dari sembilan kategori ukuran-kematangan operasional dengan aturan ambang, lalu menyusun peta hasil (*yield map*) beresolusi tinggi. Citra RGB-D diproses dengan YOLOv8-seg dan modul pelacakan berbasis BoT-SORT untuk memperoleh masker instans. Dari masker itu diturunkan indeks kematangan berbasis warna dan awan titik 3D yang disaring dengan DBSCAN untuk menghitung panjang dan lebar buah.

Data dikumpulkan di kebun stroberi hidroponik komersial di Arcabuco, Boyacá, Kolombia, memakai kamera Intel RealSense D435i dan GNSS RTK Ardusimple simpleRTK2B, dengan total 1.626 citra RGB-D berukuran 1280 × 720 piksel pada 7 bingkai per detik. Modul deteksi, segmentasi, dan pelacakan berasal dari karya sebelumnya penulis yang sama dan dipakai sebagai tahap masukan; kontribusi makalah ini adalah ekstraksi fitur tingkat buah, kategorisasi, dan peta hasil yang diperkaya.

Hasil utamanya adalah median IoU hingga 0,83 untuk kotak pembatas dan 0,71 untuk masker (YOLOv8l-seg) serta galat absolut rerata 2,51 mm untuk panjang dan 1,85 mm untuk lebar terhadap jangka sorong (*Vernier caliper*) pada 43 buah. Peta hasil dengan sel 1 m² dan per baris tanam menunjukkan variasi spasial yang nyata dalam kerapatan buah, kematangan, dan komposisi ukuran-kematangan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil dan kematangan stroberi diperlukan untuk perencanaan panen dan pengendalian mutu, terutama pada sistem hidroponik dengan kerapatan tanaman tinggi, tenaga kerja terbatas, dan jendela kematangan komersial yang sempit. Pemantauan status buah masih dominan manual, subjektif, dan mahal. Penulis menyatakan bahwa integrasi segmentasi, estimasi kematangan dan ukuran, serta pemetaan buah berkoordinat geografis masih terbatas pada tanaman berstruktur rendah seperti stroberi, yang memiliki buah dengan tahap kematangan beragam, oklusi tinggi, serta variasi warna dan ukuran besar.

Sistem hidroponik dinilai memiliki kondisi khusus bagi penglihatan komputer: kerapatan buah dan tanaman tinggi, buah saling tumpang tindih, oklusi daun dan struktur penyangga, latar berulang dari baris sebelah, serta variasi pencahayaan lahan terbuka. Tinjauan terdahulu pada selada hidroponik disebut tidak mengintegrasikan data spasial.

## Ide Utama
Gagasan utamanya adalah menurunkan atribut tiap buah (persentase area merah, panjang, lebar) dari masker instans dan peta kedalaman, menetapkan buah ke kategori operasional dengan aturan transparan, lalu mengagregasi atribut itu ke sel spasial berdasarkan posisi GNSS RTK dalam koordinat UTM. Identitas lintas bingkai ditangani oleh pelacakan BoT-SORT sehingga buah yang tampak pada beberapa bingkai berurutan tidak dihitung ganda.

Persentase kematangan diinterpretasikan sebagai ukuran relatif cakupan permukaan merah yang tampak, bukan ukuran fisiologis kematangan internal. Penulis juga menegaskan bahwa akurasi RTK setingkat sentimeter tidak dimaksudkan untuk memisahkan buah yang berdekatan; pemisahan buah dilakukan di ruang citra lewat segmentasi dan pelacakan, sedangkan RTK memberi acuan geospasial tiap citra.

## Cara Kerja Langkah demi Langkah

```
 RGB-D + GNSS RTK --> hapus latar (rentang kedalaman) --> YOLOv8-seg
 --> BoT-SORT (track ID) --> potong RGB dan depth per masker
 --> HSV: % merah | awan titik 3D + DBSCAN: panjang, lebar
 --> kategori ukuran-kematangan (0..8) --> sel 1 m2 dan baris tanam
```

### 1. Akuisisi data dan lokalisasi
Lokasi berada pada lintang 5°45'46,3" LU, bujur 73°26'46,9" BB, ketinggian 2.739 m di atas permukaan laut. Kamera RealSense D435i dan penerima RTK dipasang pada monopod teleskopik dengan pandangan lateral ke baris tanaman pada ketinggian sekitar 1,2 m, jarak lateral sekitar 0,6 m, dan kemiringan sekitar 25°. Pengambilan data dilakukan pagi hari (08.00 sampai 11.00) dalam kondisi berawan sebagian. Konfigurasi basis-rover memakai tautan radio pita 902 sampai 927 MHz; uji statis pada titik tetap menunjukkan radius sebaran maksimum sekitar 5,61 cm. Kamera dan GNSS berjalan pada utas terpisah dengan stempel waktu bersama, dan koordinat diproyeksikan ke UTM. Latar dihapus dengan memasking piksel di luar interval kedalaman alur baris yang dianalisis, ditambah penyaringan morfologi.

### 2. Deteksi, segmentasi, dan pelacakan
Empat varian YOLOv8-seg dipakai (n, s, m, l). Anotasi, pembagian data latih, validasi, uji, dan rincian pelatihan dirujuk ke karya sebelumnya dan tidak diulang; jumlah citra pada tiap subset tidak dilaporkan pada makalah ini. Pelacakan memakai BoT-SORT dengan pendekatan *tracking-by-detection* yang memadukan gerak dan tampilan; tiap buah menerima track ID saat pertama terdeteksi, dan jalur dianggap berakhir bila tidak ada asosiasi selama sejumlah bingkai yang ditetapkan. Untuk tiap buah disimpan citra RGB tersegmentasi, peta kedalaman terpotong, serta metadata (masker, track ID, koordinat UTM) dalam berkas .csv.

### 3. Estimasi kematangan
Kematangan dihitung di ruang warna HSV pada area buah. Area matang ditentukan oleh dua interval rona merah (H 0 sampai 10 dan 170 sampai 180, dengan S ≥ 100 dan V ≥ 100), area mentah oleh interval hijau/kuning (H 25 sampai 85, S ≥ 40, V ≥ 40), dan piksel tak terklasifikasi dialihkan ke kelas mentah. Persentase matang adalah jumlah piksel matang dibagi jumlah piksel matang dan mentah, dikali 100. Ambang HSV bersifat tetap untuk kondisi akuisisi yang dievaluasi.

### 4. Estimasi ukuran
Piksel berkedalaman valid pada masker diproyeksikan ke koordinat metrik dengan model lubang jarum (*pinhole*) dan parameter intrinsik $f_x = f_y = 1210$, $c_x = 640$, $c_y = 360$. DBSCAN dengan $\varepsilon$ = 5 mm dan $m$ = 10 menyaring titik jauh, dan klaster non-derau terbesar dipakai. Lebar dan panjang adalah rentang sumbu X dan Y klaster itu, dikalikan faktor skala empiris hasil kalibrasi terhadap jangka sorong ($s_w$ = 1,43 untuk lebar dan $s_l$ = 1,67 untuk panjang), lalu dibulatkan ke milimeter. Pada contoh di makalah, sebelum DBSCAN ukuran 39 mm × 39 mm dan setelahnya 29 mm × 38 mm (lebar × panjang).

### 5. Kategorisasi dan peta hasil
Kematangan dibagi menjadi *Unripe* (≤ 20%), *Partially Ripe* (di atas 20% sampai 60%), dan *Ripe* (di atas 60%). Ukuran dibagi menjadi *Small* (lebar < 20 mm atau panjang < 30 mm), *Medium* (lebar 20 sampai kurang dari 30 mm dan panjang 30 sampai kurang dari 40 mm), dan *Large* (lebar ≥ 30 mm dan panjang ≥ 40 mm), sehingga terbentuk sembilan kategori (ID 0 sampai 8). Ambang tersebut adalah kriteria operasional, bukan standar komersial universal. Buah diagregasi ke sel 1 m × 1 m untuk kerapatan, rerata kematangan, dan sebaran kategori, serta per baris tanam untuk proporsi kategori; interpolasi hanya dipakai sebagai alat bantu visual.

## Eksperimen dan Hasil
Data uji deteksi dan segmentasi adalah subset uji dari karya sebelumnya. Metrik F1 (setara koefisien Dice) dan IoU dihitung per pasangan prediksi-*ground truth* lalu diringkas dengan median, rerata, dan simpangan baku; kecepatan inferensi dan memori GPU juga dilaporkan. Validasi ukuran memakai 43 stroberi yang diukur dengan jangka sorong.

| Metrik (uji) | YOLOv8n-seg | YOLOv8s-seg | YOLOv8m-seg | YOLOv8l-seg |
|---|---|---|---|---|
| F1 kotak (median) | 0,81 | 0,83 | 0,87 | 0,90 |
| IoU kotak (median) | 0,73 | 0,76 | 0,80 | 0,83 |
| F1 masker (median) | 0,73 | 0,75 | 0,78 | 0,80 |
| IoU masker (median) | 0,63 | 0,65 | 0,69 | 0,71 |
| IoU masker (rerata) | 0,61 | 0,64 | 0,66 | 0,68 |
| Kecepatan, kotak (FPS) | 34,48 | 35,45 | 22,40 | 13,70 |
| Kecepatan, masker (FPS) | 25,51 | 24,63 | 20,02 | 13,57 |

Nilai membaik secara monoton seiring ukuran model, dengan simpangan baku F1 dan IoU sekitar 0,13 sampai 0,16. Penulis mencatat YOLOv8s-seg sebagai kompromi untuk pemrosesan waktu nyata (lebih dari 30 FPS pada kotak) dan model m atau l untuk analisis luring.

| Galat dimensi vs jangka sorong (43 buah) | Panjang | Lebar |
|---|---|---|
| MAE | 2,51 mm | 1,85 mm |
| MRE | 7,03% | 6,62% |
| RMSE | 2,53 mm | 1,89 mm |

Sistem cenderung menaksir terlalu besar. Rentang acuan panjang 30,4 sampai 42,0 mm dan lebar 22,5 sampai 38,2 mm, dengan galat absolut 1,8 sampai 3,3 mm (panjang) dan 1,2 sampai 3,0 mm (lebar).

Distribusi buah per kategori pada dataset asli (Tabel 1): Partially Ripe–Large 178, Partially Ripe–Medium 196, Partially Ripe–Small 635, Ripe–Large 150, Ripe–Medium 147, Ripe–Small 379, Unripe–Large 352, Unripe–Medium 879, dan Unripe–Small 2.670. Jumlah keseluruhan dari tabel ini adalah 5.586 buah (dihitung dari penjumlahan sembilan kategori; makalah tidak menyebut total itu secara eksplisit). Peta menunjukkan zona dengan kerapatan tinggi yang didominasi buah kecil mentah, serta petak berkerapatan sedang dengan buah matang berukuran menengah atau besar sebagai kandidat panen selektif. Angka kerapatan per sel tidak tercantum dalam teks.

## Kelebihan dan Keterbatasan
Penulis menyatakan bahwa evaluasi dilakukan pada satu kebun hidroponik komersial; pemindahan ke kultivar, konfigurasi tanam, atau kondisi lingkungan lain memerlukan kalibrasi ulang ambang kematangan dan ukuran serta validasi ulang modul persepsi. Ambang HSV tetap dapat dipengaruhi perubahan pencahayaan, bayangan, pantulan, dan eksposur, dan *achene* dapat menimbulkan piksel kuning. Ukuran dapat dipengaruhi oklusi parsial, masker tidak lengkap, kuantisasi kedalaman, derau sensor, dan pandangan lateral tunggal. Penulis menyarankan pembandingan arsitektur segmentasi lebih baru dan evaluasi pada berbagai tingkat oklusi, pencahayaan, dan kerapatan tanaman.

Menurut pembacaan ringkasan ini, faktor skala empiris (1,43 dan 1,67) dikalibrasi memakai jangka sorong dan kemudian dipakai pada validasi 43 buah; teks tidak menyatakan bahwa kalibrasi dan validasi memakai buah yang terpisah, sehingga galat 2,51 mm dan 1,85 mm dapat optimistis. Menurut pembacaan ringkasan ini, ketepatan hitungan buah unik dari pelacakan tidak dilaporkan pada makalah ini (dirujuk ke karya sebelumnya), dan peta hasil tidak divalidasi terhadap hasil panen atau berat buah. Menurut pembacaan ringkasan ini, kematangan tidak divalidasi terhadap penilaian ahli atau pengukuran fisikokimia.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada beberapa bingkai berurutan dengan mekanisme pelacakan pada video atau urutan citra (YOLOv8-seg dengan BoT-SORT, identitas berupa track ID), dengan tujuan menghindari hitungan ganda. Akurasi hitungan hasil pelacakan tidak dilaporkan dalam makalah ini. Hitungan dilaporkan per kategori ukuran-kematangan (sembilan kelas) pada sel 1 m² dan per baris, sehingga merupakan inventaris per kelas. Acuan evaluasi pada makalah ini adalah anotasi citra (segmentasi) dan ukuran jangka sorong (dimensi); acuan terhadap panen atau hitung manual di lapangan tidak dilaporkan.

Untuk pencacahan tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah gagasan agregasi hitungan per kelas ke sel spasial dan baris, penggunaan kategori berbasis aturan ambang dari kematangan, serta pelacakan *tracking-by-detection* untuk identitas dalam satu urutan gerak. Pelacakan ini terbatas pada satu sisi baris dengan pandangan lateral dan tidak menyatukan identitas lintas sisi pohon. Makalah tidak membahas penyatuan hitungan dari sisi yang berbeda dan tidak menguji tanaman kelapa sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `pardobeainy2026maturity`.

Pardo-Beainy dkk. mengintegrasikan RGB-D, YOLOv8-seg dengan pelacakan BoT-SORT, estimasi kematangan berbasis HSV, estimasi dimensi dari awan titik yang disaring DBSCAN, dan GNSS RTK untuk memetakan stroberi hidroponik per sel 1 m² dan per baris dalam sembilan kategori ukuran-kematangan. Galat absolut rerata dimensi adalah 2,51 mm (panjang) dan 1,85 mm (lebar) terhadap jangka sorong pada 43 buah, dan median IoU masker terbaik adalah 0,71 (YOLOv8l-seg), pada satu kebun komersial di Kolombia.

Catatan verifikasi data: Angka segmentasi dan kecepatan berasal dari Tabel 2, galat dimensi dari Tabel 3 dan 4 serta seksi 3.2, distribusi kategori dari Tabel 1, serta jumlah citra (1.626) dan akuisisi dari seksi 2.1. Jumlah buah total 5.586 dihitung dari Tabel 1 dan tidak dinyatakan di teks. Ekstraksi PDF menyimpan tabel secara berderet sehingga kolom Tabel 2 dibaca berdasarkan urutan model; seluruh angka peta (Gambar 11 sampai 15) tidak terbaca dari teks. Rincian data latih, validasi, dan uji serta akurasi pelacakan dan hitungan buah dirujuk ke karya sebelumnya dan tidak dapat diverifikasi dari teks ini. Hasil peta hasil bersifat kualitatif.
