# A novel apple fruit detection and counting methodology based on deep learning and trunk tracking in modern orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gao2022novel` |
| Judul asli | A novel apple fruit detection and counting methodology based on deep learning and trunk tracking in modern orchard |
| Penulis | Gao, Fangfang; Fang, Wentai; Sun, Xiaoming; Wu, Zhenchao; Zhao, Guanao; Li, Guo; Li, Rui; Fu, Longsheng; Zhang, Qin |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gao2022novel.pdf](../pdf/gao2022novel.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107000

## Gambaran Umum
Makalah ini mengusulkan metode penghitungan buah apel dari video kebun dengan arsitektur dinding buah vertikal (*vertical fruiting wall*), yang melacak batang pohon alih-alih melacak buah. Detektor YOLOv4-tiny mendeteksi buah dan batang pada tiap bingkai, dan pelacak objek tunggal CSR-DCF (*channel spatial reliability-discriminative correlation filter*) melacak satu batang. Perpindahan batang antarbingkai dipakai sebagai perpindahan acuan untuk memprediksi posisi buah, dan buah yang sama pada dua bingkai berurutan dicocokkan dengan jarak Euclidean minimum. Setiap buah mendapat ID unik, dan ID terbesar pada bingkai terakhir menjadi jumlah buah pada video.

Data diambil pada kebun apel komersial kultivar 'Scifresh' dekat Prosser, Washington, AS, dengan sensor Microsoft Kinect V2 pada kendaraan kendali jarak jauh: 800 citra statis dan 20 video pada musim panen 2017 dan 2018. Hasil utama: detektor mencapai mAP 99,35% (AP buah 99,59%, AP batang 99,10%) dengan 0,022 detik per citra 1920×1080. Penghitungan pada 20 video mencapai akurasi rata-rata 91,49% dan R² 0,9875 terhadap hitungan manual, serta berjalan pada CPU sebesar 2 sampai 5 bingkai per detik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Hitungan buah yang akurat diperlukan untuk estimasi hasil panen, tetapi petani masih mengandalkan hitungan manual yang padat karya dan mahal. Metode berbasis citra tunggal mengharuskan area pemotretan diatur agar tidak tumpang tindih. Video barisan pohon lebih mudah diperoleh dari kendaraan darat, tetapi menuntut cara mengaitkan buah yang sama antarbingkai agar tidak dihitung berulang.

Metode penghitungan video terdahulu melacak semua buah terdeteksi. Penulis mengutip contoh: penghitungan mangga dengan filter Kalman yang membutuhkan rekonstruksi SfM semantik untuk mengenali buah terlacak ulang (R² 0,88), pelacakan Kalman dengan RMSE terkoreksi bias 18,0 buah per pohon, dan pelacakan multi-objek apel dengan hitungan 93% pada tingkat deteksi 54%. Penulis menilai pelacakan semua buah memerlukan banyak sumber daya dan sering salah mencocokkan atau kehilangan target, karena buah kecil dan sangat mirip satu sama lain.

## Ide Utama
Batang pohon lebih besar daripada buah dan tampak jelas pada video, sehingga cocok sebagai satu-satunya objek yang dilacak. Pada arsitektur dinding buah vertikal, pohon ditanam rapat (jarak antarpohon umumnya 0,3 sampai 1,5 m, jarak antarbaris 2,5 sampai 4,0 m), sehingga batang dapat dideteksi pada hampir setiap bingkai. Semua objek yang relatif diam terhadap batang (cabang, daun, buah) memiliki lintasan gerak yang sama pada bingkai. Perpindahan batang karenanya menjadi perpindahan acuan untuk semua buah, dan buah dicocokkan lintas bingkai tanpa pelacakan per buah.

## Cara Kerja Langkah demi Langkah
```
 Video -> YOLOv4-tiny (buah, batang) -> pilih batang u (absis terkecil)
       -> CSR-DCF melacak u -> perpindahan acuan RD
       -> posisi buah prediksi = posisi bingkai i-1 + RD
       -> cocokkan dengan jarak Euclidean minimum -> ID buah -> hitung
```

### 1. Akuisisi data
Perangkat terdiri atas Microsoft Kinect V2, penjepit kamera, dan rangka penyangga pada kendaraan kendali jarak jauh. Citra warna Kinect V2 beresolusi 1920×1080 dengan FOV 84,1×53,8 (satuan derajat tidak tertulis pada teks ekstraksi). Pohon setinggi sekitar 4,0 m dengan jarak antarpohon 1,5 m dan antarbaris 2,7 m. Sebanyak 800 citra RGB statis dan 20 video kanopi diambil pada dua musim panen (2017 dan 2018). Kendaraan dijalankan sepanjang barisan dengan kecepatan yang diusahakan hampir konstan, dan waktu pengambilan video acak sehingga jumlah pohon dan buah per video berbeda. Jumlah buah dan batang pada tiap video dihitung manual oleh tiga operator, dan rata-ratanya menjadi acuan. Galat relatif hitungan manual antaroperator pada set video adalah 2,7 buah per video. Buah di latar belakang tidak dihitung.

### 2. Penyusunan set data deteksi
Citra dibagi acak menjadi 80% pelatihan (640 citra) dan 20% pengujian (160 citra). Setiap citra dianotasi dengan kotak pembatas kelas buah dan batang dalam berkas XML; objek pada tepi citra tidak dilabeli. Augmentasi mencakup transformasi kecerahan, ekualisasi histogram adaptif, kabur gerak, dan pencerminan horizontal, sehingga 800 citra menjadi 6.400 citra; rotasi tidak dipakai karena sudut pohon hasil rotasi tidak sesuai kondisi nyata. Seluruh video dipakai untuk menguji algoritma penghitungan.

### 3. Detektor YOLOv4-tiny
YOLOv4-tiny memiliki 36 lapisan dan memakai dua peta fitur untuk deteksi. Citra dikompresi menjadi 416×416 tanpa mempertahankan rasio aspek. Pelatihan dengan Darknet pada GPU NVIDIA GTX 1080 8 GB: ukuran batch 64, SGD dengan momentum 0,9, peluruhan bobot 0,0005, laju pembelajaran awal 0,001, 50.000 iterasi, bobot awal dari COCO. Ukuran bobot hasil latih 22,4 MB.

### 4. Pelacak batang CSR-DCF
Detektor memberi posisi batang yang dipilih, yaitu batang pertama pada arah gerak video (absis terkecil), sebagai inisialisasi pelacak. Pelacak melatih templat DCF dengan fitur HoG dan Colornames untuk memprediksi posisi batang pada bingkai berikutnya. Bila *overlap* (IoU) antara kotak prediksi dan kotak batang terdeteksi turun di bawah 40%, posisi pelacak dikoreksi dengan kotak terdeteksi yang tumpang tindihnya terbesar. Ambang 20%, 30%, 40%, 50%, dan 60% dicoba, dan 40% memberi akurasi hitung tertinggi. Bila batang mencapai tepi bingkai, batang lain pada bingkai dipilih sebagai target baru.

### 5. Pencocokan dan penghitungan buah
Objek berkeyakinan lebih dari 0,5 diambil. Pada bingkai pertama, ID buah diberikan berurutan menurut arah gerak video. Pada bingkai berikutnya, perpindahan acuan RD dihitung sebagai selisih posisi batang terlacak antara bingkai saat ini dan sebelumnya, posisi buah dari bingkai sebelumnya digeser sebesar RD, dan pasangan buah dengan jarak Euclidean minimum dianggap buah yang sama sehingga ID lama dipertahankan. Buah tanpa pasangan menerima ID baru. Jumlah buah pada video adalah ID maksimum pada bingkai terakhir.

### 6. Metrik
mAP deteksi (rerata AP apel dan batang), MIDE (*mean ID calculation error*, rerata rasio buah yang IDnya berpindah terhadap buah terhitung pada tiap bingkai), RMSE antara hitungan metode dan acuan pada tiap bingkai, dan Pc (akurasi hitung per video, $1 - |P_t - N_t|/N_t$).

## Eksperimen dan Hasil
Detektor diuji pada set uji berlabel. Teks menyebut 160 citra uji pada bagian pembagian data dan 1.280 citra uji pada bagian hasil; selisihnya sesuai dengan faktor augmentasi delapan kali tetapi hal itu tidak dinyatakan secara eksplisit.

| Objek | TP | FP | FN | Presisi (%) | *Recall* (%) | AP (%) | mAP (%) |
|---|---|---|---|---|---|---|---|
| Buah | 35.720 | 3.972 | 266 | 90,26 | 99,29 | 99,59 | 99,35 |
| Batang | 1.656 | 63 | tidak terbaca pada tabel | tidak terbaca | tidak terbaca | 99,10 | |

Teks menyebut total 37.642 target, 37.376 TP, 4.036 FP, dan 266 FN, serta 1.656 dari 1.675 batang dan 35.720 dari 35.967 buah terdeteksi. Kecepatan deteksi 22 ms per citra 1920×1080 (laptop dan GPU tidak disebut untuk pengujian ini; pelatihan memakai GTX 1080).

Penghitungan pada 20 video (10 sampai 104 bingkai, 68 sampai 494 buah per video):

| Indikator | Nilai |
|---|---|
| MIDE | 0,028 |
| RMSE (per bingkai) | 5,224 |
| Pc rata-rata, 20 video | 91,49% |
| Pc minimum | di atas 80% |
| R² (hitungan metode terhadap hitungan manual) | 0,9875 |
| Kecepatan pada CPU | 2 sampai 5 fps |
| Rata-rata buah terdeteksi per bingkai | 37, dengan sekitar 0,016 FP dan 0,098 FN |
| Rata-rata buah berpindah ID per video | sekitar 0,094 |

Pada video contoh V12 (48 bingkai), 40 bingkai tidak memiliki buah yang IDnya berpindah; Tabel 2 mencantumkan Ns, Nc, dan Ng pada delapan bingkai lainnya (misalnya bingkai ke-5: Ns 8, Nc 45, Ng 53). Pergantian ID terutama disebabkan oleh penyimpangan pelacakan (bingkai 5, 12, 13) dan oleh buah bertumpuk yang tidak semuanya terdeteksi (bingkai 6, 18, 29, 34, 36). Penulis menyatakan galat hitung lebih (FP, pergantian ID) dan kurang (FN) seimbang sehingga bias rendah.

Perbandingan dengan Deep Sort memakai detektor YOLOv4-tiny yang sama pada 5 video acak: metode usulan memiliki akurasi hitung rata-rata 91,60%, sedangkan Deep Sort mengalami penghitungan berlebihan yang serius (nilai Deep Sort tidak diberikan dalam angka pada teks; hanya Gambar 10a). Kecepatan Deep Sort di bawah 2 fps.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: hanya satu objek (batang) yang dilacak sehingga hemat sumber daya dan dapat berjalan di CPU; tidak memerlukan rekonstruksi 3D; MIDE rendah; detektor ringan (22,4 MB); dan hasil lebih baik daripada pelacakan multi-objek Deep Sort pada video yang sama.

Keterbatasan yang dinyatakan penulis: hanya satu sisi barisan pohon yang diproses, sehingga buah yang terlihat dari kedua sisi dihitung ganda pada penghitungan satu barisan. Penulis merencanakan metode untuk menghilangkan buah yang terlihat dari kedua sisi dan menyebut bahwa model matematis dari studi lain sulit menghadapi perubahan hasil kebun yang mendadak, serta bahwa rekonstruksi 3D dua sisi memerlukan lebih dari 34 menit per baris.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Metode bergantung pada keberadaan batang yang terlihat jelas, yang sesuai untuk dinding buah vertikal tetapi tidak untuk kanopi pohon sawit dan pohon lain yang batangnya tertutup. Asumsi gerak seragam sebidang antara batang dan buah tidak berlaku untuk buah pada kedalaman berbeda (paralaks). Jumlah video hanya 20 dari satu kebun dan satu kultivar. Pembanding Deep Sort hanya pada 5 video tanpa angka tabulasi. Akurasi hitung (Pc) menutupi galat yang saling meniadakan antara hitungan berlebih dan kurang. Konsistensi angka pada teks tidak sempurna (160 versus 1.280 citra uji; FP 3.972 pada tabel versus 4.036 pada teks; *recall* buah 99,29% pada tabel versus 99,31% pada teks).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam rangkaian bingkai video satu sisi barisan. Mekanismenya adalah pelacakan batang sebagai jangkar gerak, penggeseran posisi buah dengan perpindahan acuan, dan pencocokan jarak Euclidean minimum untuk mempertahankan ID. Makalah ini secara eksplisit tidak menyatukan pengamatan buah yang sama dari dua sisi barisan; penulis menyatakan hal itu menyebabkan hitungan ganda dan menjadikannya pekerjaan lanjutan. Dengan demikian, identitas lintas sisi justru berstatus masalah terbuka pada makalah ini.

Hitungan tidak dilaporkan per kelas; kelas deteksi hanya buah dan batang, dan hasilnya satu angka per video. Acuan hitungnya adalah hitungan manual dari video oleh tiga operator (rata-rata), bukan hasil panen. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memakai struktur diam yang besar (batang) sebagai jangkar untuk mengaitkan objek kecil antarbingkai pada satu sisi, serta penegasan masalah buah yang terlihat dari dua sisi. Ketergantungannya pada gerak sejajar bidang dan pada batang yang terlihat menjadi batas pemindahan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gao2022novel`.

Ringkasan yang aman dikutip: Gao dkk. (2022) mengusulkan penghitungan buah apel dari video kebun dinding buah vertikal dengan mendeteksi buah dan batang memakai YOLOv4-tiny, melacak satu batang dengan CSR-DCF untuk mendapatkan perpindahan acuan antarbingkai, dan mencocokkan buah antarbingkai dengan jarak Euclidean minimum untuk memberi ID unik. Pada 20 video, metode ini memperoleh akurasi hitung rata-rata 91,49% dan R² 0,9875 terhadap hitungan manual, dengan mAP deteksi 99,35%. Penulis menyatakan metode ini hanya mencakup satu sisi barisan sehingga buah yang terlihat dari kedua sisi dihitung ganda.

Catatan verifikasi data: mAP, AP, TP, FP, FN, dan presisi buah berasal dari Tabel 1, sedangkan nilai presisi, *recall*, dan FN batang tidak terbaca pada teks ekstraksi tabel (hanya TP 1.656, FP 63, dan AP 99,10%; jumlah batang 1.675 dari teks). MIDE, RMSE, Pc rata-rata 91,49%, R² 0,9875, rentang bingkai dan buah per video, serta kecepatan 2 sampai 5 fps berasal dari teks bagian 3.2 dan abstrak. Nilai tiap video pada Gambar 9 dan Gambar 10a tidak terbaca dari teks. Akurasi 91,60% pada 5 video acak berasal dari bagian 3.3. Perbedaan angka antara tabel dan teks dicatat pada bagian keterbatasan. Akurasi hitung per video bukan galat hitung agregat.
