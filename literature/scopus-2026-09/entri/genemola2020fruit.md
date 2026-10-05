# Fruit detection, yield prediction and canopy geometric characterization using LiDAR with forced air flow

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2020fruit` |
| Judul asli | Fruit detection, yield prediction and canopy geometric characterization using LiDAR with forced air flow |
| Penulis | Gen\'e-Mola, Jordi; Gregorio, Eduard; Auat Cheein, Fernando; Guevara, Javier; Llorens, Jordi; Sanz-Cortiella, Ricardo; Escol\`a, Alexandre; Rosell-Polo, Joan R. |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2020fruit.pdf](../pdf/genemola2020fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2019.105121

## Gambaran Umum
Makalah ini menguji pendeteksian apel dan estimasi hasil panen per pohon dengan pemindai laser terestrial bergerak (*mobile terrestrial laser scanner*, MTLS) yang memakai sensor LiDAR multi-berkas Velodyne VLP-16 dan RTK-GNSS (*real-time kinematics global navigation satellite system*). Penelitian dilakukan pada kebun apel Fuji (*Malus domestica* Borkh. cv. Fuji) komersial di Agramunt, Catalonia, Spanyol, dengan 11 pohon berurutan yang berisi total 1.444 apel hasil hitung manual di lapangan. Selain deteksi dan estimasi hasil, sistem dipakai untuk mengkarakterisasi geometri kanopi (tinggi, lebar, luas penampang, dan luas daun).

Tujuan utama makalah adalah mengurangi oklusi buah pada pendekatan berbasis LiDAR melalui dua cara: aliran udara paksa dari penyemprot berbantuan udara (*air-assisted sprayer*) yang menggerakkan dedaunan, dan penginderaan multi-pandang (*multi-view sensing*), yaitu pemindaian dari dua sisi barisan pohon serta dari dua ketinggian sensor. Algoritma deteksi memakai ambang pantulan (*reflectance*), pengelompokan DBSCAN, dan *support vector machine* (SVM) untuk memisahkan klaster dan membuang deteksi palsu.

Hasil utama: sistem mendeteksi dan melokalisasi lebih dari 80% buah yang dianotasi, memprediksi hasil panen dengan *root mean square error* (RMSE) di bawah 6%, dan menemukan bahwa aliran udara paksa serta multi-pandang masing-masing menambah buah yang terlokalisasi sebesar 6,7% dan 6,5% dibandingkan konfigurasi dasar. Penggabungan data dari dua sisi barisan menaikkan F1-score dari 0,537 (0,513) dan 0,624 (0,598) pada satu sisi menjadi 0,812 (0,784) pada dua sisi. Angka dalam kurung dihitung terhadap hitungan lapangan, angka di luar kurung terhadap label pada awan titik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan hasil panen dan karakterisasi geometri tanaman memberi informasi tentang variabilitas dan vigor kebun sehingga keputusan irigasi, pemupukan, dan pemangkasan dapat dibuat lebih baik. Sensor yang paling umum untuk pemetaan hasil adalah kamera RGB, tetapi kamera itu hanya memberi informasi 2D dan kinerjanya dipengaruhi faktor di luar algoritma, yaitu oklusi buah oleh organ tanaman lain dan kondisi pencahayaan. Kamera kedalaman berbasis stereoskopi, cahaya terstruktur, atau *time-of-flight* (ToF) menurun kinerjanya di bawah sinar matahari langsung.

LiDAR tidak terpengaruh pencahayaan dan memberi lokasi 3D relatif, tetapi pemakaiannya untuk deteksi buah dan pemantauan hasil masih jarang. Penulis menyebut kemungkinan sebabnya, yaitu harga yang lebih tinggi daripada kamera RGB dan ketiadaan data warna. Studi LiDAR terdahulu untuk deteksi buah dilakukan di laboratorium dengan 7 sampai 114 buah. Oklusi pada pendeteksian berbasis LiDAR cenderung menyebabkan hasil panen terestimasi terlalu rendah, dan sangat sedikit studi yang menangani oklusi.

## Ide Utama
Hipotesis penulis adalah bahwa menggerakkan dedaunan dan memakai penginderaan multi-pandang akan mengurangi jumlah oklusi buah dan menaikkan persentase buah yang terdeteksi. Sistem dipasang pada penyemprot berbantuan udara yang ditarik traktor sehingga aliran udara turbulen dapat membuka sebagian buah yang tertutup daun.

Ide kedua adalah menggabungkan beberapa pemindaian pada tingkat awan titik sebelum deteksi. Semua pemindaian diberi georeferensi dalam koordinat dunia absolut sehingga registrasi awan titik berlangsung otomatis. Penulis menyatakan bahwa penggabungan ini mengurangi deteksi ganda (*multi-detection*): titik dari apel yang sama pada dua pemindaian (misalnya sisi timur dan sisi barat) menyatu dalam satu awan titik sehingga apel itu dideteksi satu kali.

## Cara Kerja Langkah demi Langkah

```
  [ Awan titik LiDAR + RTK-GNSS ]
              │
              ▼
  [ Penggabungan pemindaian (E+W, H1+H2, n+af) ]
              │
              ▼
  [ Pra-pemrosesan: ambang pantulan + sparse outlier removal ]
              │
              ▼
  [ Pengelompokan DBSCAN (ε = 0,03 m) ]
              │
              ▼
  [ Pemisahan buah: SVM linear memprediksi K, K-means ]
              │
              ▼
  [ Penyaringan deteksi palsu: SVM ]
```

### 1. Akuisisi data
Pemindaian dilakukan tiga minggu sebelum panen pada tahap pertumbuhan BBCH 85. Pohon berumur 8 tahun dengan sistem *tall spindle*, tinggi kanopi maksimum 3,5 sampai 4 m, lebar 1 sampai 1,5 m, dan jarak tanam 4 × 1 m. Sebanyak 11 pohon berurutan dipakai, dengan total 1.444 apel.

Sensor Velodyne VLP-16 dipasang pada bidang vertikal dengan 16 berkas laser yang tersebar pada medan pandang horizontal 30° (sudut pindai +15° sampai -15° dengan langkah 2°). Sensor mengeluarkan nilai pantulan terkalibrasi pada panjang gelombang 905 nm dengan rentang 0 sampai 100, dan laju akuisisi diatur 10 Hz. RTK-GNSS Leica GPS1200+ memberi posisi dengan galat absolut 0,01/0,02 m (horizontal/vertikal) pada laju 20 Hz. Sistem tidak memiliki IMU, sehingga ditarik traktor dengan kecepatan 0,125 m/s pada lintasan lurus untuk mengurangi getaran.

Ada empat uji, yaitu kombinasi ketinggian sensor H1 (1,8 m, kira-kira setengah tinggi pohon) dan H2 (2,5 m) dengan kondisi tanpa aliran udara (n) dan dengan aliran udara paksa (af). Penyemprot dioperasikan pada 540 rpm PTO dan menghasilkan kecepatan udara 5,5 ± 2,3 m/s pada jarak 2,4 m dari pusat kipas. Setiap uji memindai barisan dari sisi barat (W) dan sisi timur (E); gabungan kedua sisi dinotasikan (E+W).

Acuan kebenaran dibuat dengan memberi kotak pembatas 3D pada tiap apel dalam awan titik memakai CloudCompare dan dibantu citra RGB. Sebanyak 1.353 buah teridentifikasi dalam awan titik, yaitu 93,7% dari 1.444 buah hasil hitung manual (GTfield); 6,3% apel tidak tampak dalam awan titik. Dataset dan kode MATLAB dinyatakan tersedia publik.

### 2. Pra-pemrosesan dan pengelompokan
Apel memiliki pantulan inframerah yang lebih tinggi daripada latar, sehingga titik di bawah ambang pantulan dibuang, lalu derau dibuang dengan *sparse outlier removal*. Titik tersisa dikelompokkan dengan DBSCAN dengan jarak minimum ε = 0,03 m. Dua buah yang lebih dekat daripada ε masuk dalam satu klaster.

### 3. Pemisahan buah
Fitur klaster (volume, jumlah titik, nilai eigen ternormalisasi, dan pantulan) diekstraksi. SVM linear dengan faktor penalti C = 0,35 memprediksi jumlah apel K dalam klaster, dan klaster dengan K > 1 dibagi menjadi K subklaster dengan K-means.

### 4. Penyaringan deteksi palsu
Deteksi palsu berasal dari batang atau daun dengan pantulan tinggi (R > 60%) atau dari klaster yang terbagi keliru sehingga menghasilkan deteksi ganda. Sebuah SVM mengklasifikasikan tiap klaster sebagai deteksi benar atau salah. Kedua SVM memakai 8 fitur: volume $V$, jumlah titik $P_t$, nilai eigen ternormalisasi $\lambda_n$, parameter geometris $\Psi = 27 \cdot \lambda_{1n} \cdot \lambda_{2n} \cdot \lambda_{3n}$ (bernilai 1 untuk klaster bulat), histogram pantulan, pantulan rerata, simpangan baku pantulan, dan pantulan maksimum.

### 5. Karakterisasi kanopi dan evaluasi
Barisan dibagi menjadi irisan vertikal sepanjang 0,1 m (110 irisan untuk 11 pohon) untuk menghitung tinggi dan lebar rerata, kontur kanopi, dan luas penampang. Luas daun diestimasi dengan *projected tree row surface* (PTRS).

Evaluasi deteksi memakai validasi silang 11-lipat: satu pohon diuji dan sepuluh pohon lain dipakai melatih. Deteksi dianggap benar (TP) bila tumpang tindihnya dengan label lebih dari 50%; bila satu apel dideteksi $n$ kali, dihitung satu TP dan $n-1$ deteksi ganda. Metrik: *detection rate* (DR), *recall*, *precision*, *false detection rate* (FDR), *multi-detection rate* (MDR), dan F1-score, masing-masing terhadap jumlah label dan terhadap hitungan lapangan. Prediksi hasil memakai regresi linear $y = a \cdot x + b$ antara jumlah deteksi dan hitungan lapangan yang dilatih pada pohon lain, dengan galat per pohon dan RMSE.

## Eksperimen dan Hasil
Semua hasil berasal dari 11 pohon apel Fuji dalam satu kebun. Pembandingnya adalah konfigurasi dasar H1,n,(E+W) dan variasi sisi, ketinggian, serta kondisi udara. Tabel 2 makalah menunjukkan bahwa langkah pemisahan buah dan penyaringan deteksi palsu menaikkan F1-score dari 0,7449 (pra-pemrosesan) menjadi 0,7837 dan 0,8119. Volume adalah fitur yang paling berguna untuk pemisahan (0,7449 menjadi 0,7824), dan histogram pantulan adalah fitur yang paling berguna untuk penyaringan deteksi palsu.

Tabel berikut merangkum sebagian baris Tabel 3 makalah. Kolom "L" adalah hasil terhadap label awan titik dan "F" terhadap hitungan lapangan.

| Uji | DR (L) | DR (F) | Recall (L) | Presisi | F1 (L) | F1 (F) |
|---|---|---|---|---|---|---|
| H1,n,E | 0,415 | 0,389 | 0,383 | 0,898 | 0,537 | 0,513 |
| H1,n,W | 0,540 | 0,506 | 0,485 | 0,875 | 0,624 | 0,598 |
| H1,n,(E+W) | 0,823 | 0,771 | 0,758 | 0,875 | 0,812 | 0,784 |
| H1,af,(E+W) | 0,768 | 0,720 | 0,698 | 0,868 | 0,774 | 0,746 |
| H1,(n+af),(E+W) | 0,894 | 0,838 | 0,814 | 0,839 | 0,826 | 0,799 |
| H2,n,(E+W) | 0,663 | 0,621 | 0,588 | 0,841 | 0,692 | 0,666 |
| H(1+2),n,(E+W) | 0,892 | 0,836 | 0,802 | 0,860 | 0,830 | 0,802 |
| H(1+2),(n+af),(E+W) | 0,917 | 0,859 | 0,789 | 0,777 | 0,783 | 0,758 |

Pemindaian satu sisi menghasilkan DR terendah, dan tingkat deteksi turun lebih dari 28% pada sisi yang tidak dipindai. Aliran udara paksa sendirian menurunkan deteksi (H1,af,(E+W)) karena awan titik menjadi buram dan sebagian apel yang terbuka diimbangi apel lain yang tertutup. Manfaatnya muncul ketika data dengan dan tanpa aliran udara digabung, dengan DR naik dari 0,823 menjadi 0,894. Uji H2 menurun karena sensor yang berada di atas gagal mendeteksi buah di bagian bawah pohon. Penggabungan semua uji menaikkan DR tetapi menurunkan recall karena awan titik makin buram dan kelompok apel sulit dipisah; MDR pada gabungan itu 0,122.

Prediksi hasil (Tabel 4 dan 5) memberikan RMSE berikut.

| Konfigurasi | RMSE (%) |
|---|---|
| H1,n,(E+W) | 5,4 |
| H1,(n+af),(E+W) | 5,5 |
| H(1+2),n,(E+W) | 5,7 |
| H(1+2),n, hanya sisi E | 19,0 |
| H(1+2),n, hanya sisi W | 12,4 |

Pada konfigurasi H(1+2),n, penggunaan satu sisi menghasilkan R² 0,58 (timur) dan 0,54 (barat), sedangkan dua sisi menghasilkan galat antara -7,7% dan 12,0% dengan RMSE 5,7% dan R² = 0,87. Jumlah deteksi total pada pohon berurutan adalah 734 (E), 913 (W), dan 1.261 (E+W) terhadap 1.444 buah hitungan lapangan. Penggabungan kondisi udara atau ketinggian sensor menaikkan persentase buah terdeteksi, tetapi tidak memperbaiki prediksi hasil.

Karakterisasi geometri (Tabel 6) memakai H1,n sebagai acuan: tinggi rerata 3,64 m, lebar rerata 1,23 m, luas penampang 2,12 m², dan luas daun 9,77 m²/m. Pada gabungan H1,(n+af) selisihnya 2,1%, 10,7%, 22,3%, dan 10,6%; pada H(1+2),n selisihnya 1,3%, 3,8%, 16,3%, dan 8,3%.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: sensor tidak terpengaruh pencahayaan; sistem memberi lokasi 3D buah dan karakterisasi kanopi sekaligus; galat prediksi hasil sekitar 5,5% disebut sebanding dengan metode lain yang melaporkan galat 10% sampai 16%, yang sebagian memakai citra malam hari; dan tingkat deteksi disebut sebanding dengan studi berbasis citra warna (80% sampai 85% dengan fitur warna, hingga 90% F1-score dengan pembelajaran mendalam). Kelebihan lain yang dinyatakan adalah konfigurasi multi-pandang yang menaikkan deteksi tanpa terlalu menurunkan karakterisasi geometri.

Keterbatasan yang dinyatakan penulis: tidak ada IMU, sehingga kecepatan dan lintasan terbatas; pengujian hanya pada 11 pohon sehingga hubungan lebar kanopi dengan hasil perlu diuji lebih lanjut; dan penelitian lanjutan perlu menganalisis oklusi pada sistem pelatihan pohon yang lain serta varietas buah lain. Penulis juga menyatakan bahwa perbandingan dengan studi lain sulit karena dataset berbeda.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Hanya satu kebun, satu kultivar, dan satu waktu pemindaian yang diuji, sehingga generalisasi tidak teruji. Waktu pelatihan SVM dan pengujian memakai pohon dari kebun yang sama, walaupun pohon uji dipisahkan dengan validasi silang. Penggabungan pemindaian dilakukan pada awan titik dan memerlukan beberapa lintasan pada kendaraan tersendiri dengan kecepatan 0,125 m/s, yang menyiratkan biaya pengumpulan data tinggi. Pengurangan deteksi ganda dicapai dengan georeferensi RTK-GNSS pada lintasan lurus, sehingga bergantung pada akurasi posisi.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali, yaitu apel yang tertangkap oleh dua pemindaian (sisi timur dan barat, dua ketinggian sensor, dengan dan tanpa aliran udara). Mekanismenya bukan pencocokan identitas antarcitra, melainkan penggabungan awan titik berbasis georeferensi absolut RTK-GNSS sebelum deteksi, sehingga titik dari apel yang sama menyatu dalam satu klaster dan apel itu dideteksi satu kali. Deteksi ganda sisa yang timbul akibat pembagian klaster yang keliru diukur dengan MDR (misalnya 0,021 untuk H1,n,(E+W)) dan disaring dengan SVM kedua. Makalah ini juga mengukur dampak sisi tunggal terhadap hitungan: satu sisi saja memberi RMSE 19,0% (E) dan 12,4% (W), dan dua sisi memberi 5,7%.

Hitungan tidak dilaporkan per kelas; apel diperlakukan sebagai satu kelas. Acuan hitung ada dua, yaitu hitungan manual di lapangan (GTfield, 1.444 buah) dan anotasi pada awan titik (GTlabels, 1.353 buah). Untuk pencacahan tandan kelapa sawit multi-sisi, hal yang dapat dipindahkan adalah pendekatan penggabungan pada ruang geometri bersama (di sini ruang koordinat dunia) sebelum penghitungan, serta pelaporan ganda terhadap hitungan lapangan dan anotasi untuk memisahkan kehilangan akibat oklusi dari kesalahan algoritma. Pendekatan georeferensi sangat bergantung pada sensor LiDAR dan RTK-GNSS pada lintasan yang terkontrol sehingga tidak langsung berlaku untuk citra RGB dari sisi pohon yang berbeda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `genemola2020fruit`.

Gené-Mola dkk. memakai pemindai laser terestrial bergerak dengan LiDAR multi-berkas pada 11 pohon apel Fuji (1.444 buah hasil hitung manual) dan menguji aliran udara paksa serta penginderaan multi-pandang untuk mengurangi oklusi. Sistem mendeteksi dan melokalisasi lebih dari 80% buah yang dianotasi dan memprediksi hasil panen per pohon dengan RMSE di bawah 6%. Penggabungan pemindaian dari dua sisi barisan menaikkan F1-score dari 0,537 dan 0,624 (satu sisi) menjadi 0,812 terhadap label awan titik, dan penggabungan kondisi dengan dan tanpa aliran udara atau dua ketinggian sensor menambah buah yang terlokalisasi sebesar 6,7% dan 6,5%.

Catatan verifikasi data: Angka deteksi diambil dari Tabel 3 (DR, recall, presisi, FDR, MDR, F1-score), angka fitur dari Tabel 2, angka prediksi hasil dari Tabel 4 dan 5 serta seksi 3.4, dan angka geometri dari Tabel 6. Jumlah buah (1.444 lapangan; 1.353 label, yaitu 93,7%) berasal dari seksi 2.1 dan Tabel 1. Angka 6,7% dan 6,5% berasal dari seksi 4 (Diskusi) dan abstrak. Berkas teks hasil ekstraksi PDF memuat tabel dengan sel terpisah per baris, tetapi nilai tabel dapat dicocokkan dengan teks naratif. Ringkasan ini tidak memverifikasi kolom "recall" dan "FDR" tiap baris secara independen. Tidak ada informasi tentang berat atau ukuran buah dan tidak ada analisis per kelas; keduanya tidak dilaporkan.
