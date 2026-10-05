# Automatic fruit recognition and counting from multiple images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `song2014automatic` |
| Judul asli | Automatic fruit recognition and counting from multiple images |
| Penulis | Song, Y.; Glasbey, C.A.; Horgan, G.W.; Polder, G.; Dieleman, J.A.; van der Heijden, G.W.A.M. |
| Tahun | 2014 |
| Venue | Biosystems Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [song2014automatic.pdf](../pdf/song2014automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2013.12.008

## Gambaran Umum
Makalah ini (*Biosystems Engineering* 118, 2014) menyajikan metode dua tahap untuk mengenali dan menghitung buah paprika pada citra rumah kaca yang berantakan. Tahap pertama mendeteksi buah pada satu citra dengan model *bag-of-words* (BoW) dan *support vector machine* (SVM). Tahap kedua menggabungkan estimasi dari banyak citra berurutan dengan pendekatan statistik yang mengelompokkan pengamatan berulang dan tidak lengkap dari buah yang sama.

Tanaman yang diteliti adalah paprika setinggi sekitar 3 m dari 148 galur inbrida rekombinan (151 genotipe termasuk induk dan F1), total 1.056 tanaman percobaan dalam 264 petak, pada dua percobaan tahun 2009. Tiap percobaan menghasilkan lebih dari 28.000 citra berwarna. Percobaan pertama dipakai untuk pelatihan dan yang kedua untuk validasi. Korelasi antara hitungan otomatis dan hitungan manual mencapai 74,2% pada 435 petak tanpa penyesuaian linear, sedangkan bila buah pada citra diidentifikasi secara visual dan hanya tahap kedua dipakai, korelasi mencapai 94,6% (10 petak).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Fenotipe, misalnya jumlah buah per tanaman, menjadi hambatan dalam penelitian genetika. Pengukuran manual memerlukan tenaga kerja dan bersifat subjektif. Tantangan pada citra ini: buah paprika sebagian besar hijau dengan warna dan bentuk mirip kanopi, bentuk buah melengkung dan bervariasi antar-genotipe, pencahayaan berubah, terdapat oklusi, dan satu tanaman muncul di beberapa citra sementara satu citra memuat beberapa tanaman. Penulis menyebut enam tantangan (Tabel 4): banyak tanaman dalam satu citra, tanaman membentang pada beberapa citra, bentuk buah kompleks, variasi intrakelas tinggi, variasi antarkelas rendah, dan oklusi.

## Ide Utama
Karena citra direkam setiap 5 cm, buah yang sama tampak pada beberapa citra berurutan dan bergeser secara horizontal dengan besar tetap yang bergantung pada jaraknya dari kamera, sementara posisi vertikalnya hampir tidak berubah. Sifat ini dipakai untuk memutuskan pengamatan mana yang merupakan pengamatan ulang atas buah yang sama. Dengan demikian, buah yang tidak terdeteksi pada sebagian citra karena oklusi tetap dapat dihitung, dan buah yang tampak di banyak citra tidak dihitung ganda.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Robot pencitraan SPYSEE berupa troli dengan empat kamera tersusun vertikal, komputer, lampu, dan pengodean roda didorong di antara baris tanaman sepanjang pipa pemanas (jarak 60 cm). Setiap 5 cm, lampu kilat Xenon (30 ms) dan kamera (Teli FireWire CSFS20CC2, 1024 × 1280 piksel, lensa dengan bidang pandang 75°) dipicu. Wilayah minat adalah 480 × 1280 piksel. Buah dihitung dan dipanen secara fisik per tanaman tidak lama setelah pencitraan. Untuk evaluasi deteksi, satu baris dengan 10 petak dari percobaan validasi (408 citra) diberi label manual untuk semua buah yang tampak. Pelatihan memakai 110 templat buah (104 hijau, 6 merah; ukuran 18 × 60 hingga 72 × 119) dan 80 templat latar.

### 2. Titik minat awal
Piksel ditransformasi warna menjadi G−B, G−R, dan G/(R+G+B). Klasifikator *Naive Bayes* dengan tiga kelas (latar, buah merah, buah hijau) dengan probabilitas prior 99,27%, 0,04%, dan 0,69% (Tabel 1) diterapkan pada tiap piksel, dan ambang pada probabilitas posterior (Tp) menghasilkan sekitar 10.000 titik minat per citra, dari sekitar 600.000 posisi.

### 3. Model *bag-of-words*
Jendela dukungan berukuran 40 × 90 piksel dipusatkan di tiap titik. Fitur terdiri dari deskriptor elips *Maximally Stable Colour Region* (MSCR; lima variabel bentuk dan tiga variabel warna) dan fitur tekstur filter rentang lokal (ukuran 5 × 5 dan 9 × 9). Kosakata 1.000 kata dibangun dengan K-means untuk masing-masing fitur (total 2.000 kata), dan SVM memisahkan kelas buah dari lainnya. Jarak SVM disebut ambang bobot W. Bila jendela tumpang tindih lebih dari 50% (irisan per gabungan), dipilih jendela dengan W tertinggi.

### 4. Penghitungan dari banyak citra
Untuk satu tinggi kamera, pengamatan ke-j pada citra ke-i berkoordinat (x_ij, y_ij) diasumsikan berdistribusi normal di sekitar (a_k + i·g_k, b_k) dengan varians galat σx² dan σy², dengan K buah terlihat sekurangnya sekali. Optimasi kemungkinan langsung dan MCMC dinyatakan tidak layak, sehingga dipakai metode ad hoc: σy² diperkirakan dari campuran distribusi pada selisih pasangan, σx² dari triplet, lalu untuk tiap petak dicari himpunan pengamatan yang konsisten dengan satu buah pada tingkat signifikansi 95% (uji khi-kuadrat), mulai dari ukuran himpunan terbesar dan menurun hingga singleton. Jumlah himpunan adalah estimasi K, dan K dari empat ketinggian kamera dijumlahkan.

## Eksperimen dan Hasil
Deteksi satu citra: klasifikator warna awal memberi presisi rendah (0,45) tetapi *recall* tinggi; model BoW menyingkirkan sekitar dua pertiga positif palsu dan presisi minimum 0,61. Presisi tertinggi 0,97 menghasilkan *recall* hanya 0,17 dan F1 di bawah 0,3. F1 tertinggi 0,65 pada W = 100 dan di atas 0,6 untuk W ∈ {0, 200, 300}.

Penghitungan banyak citra pada 10 petak berlabel: korelasi 94,6% antara hitungan manual (K) dan estimasi dari buah yang diidentifikasi secara visual; σx² dan σy² estimasi keduanya 52. Hitungan terlalu tinggi pada semua petak kecuali satu, yang menurut penulis kemungkinan akibat buah dari tanaman tepi dan buah yang tampak di atas satu citra dan di bawah citra di atasnya.

Tabel 2: korelasi menurut ambang bobot W pada 435 petak validasi.

| W | Jumlah data | Korelasi (%) |
|---|---|---|
| 0 | 38.600 | 63,1 |
| 100 | 28.600 | 67,8 |
| 200 | 21.400 | 72,4 |
| 300 | 16.300 | 74,2 |
| 400 | 12.900 | 74,0 |
| 500 | 10.300 | 73,0 |
| 700 | 6.600 | 70,0 |
| 1000 | 3.000 | 62,3 |

Pada W = 300, korelasi 74,2% dan galat standar prediksi 11,3 buah (rerata 21,2 buah per petak, simpangan baku 16,3), tanpa penyesuaian intersep dan skala; titik di atas dan di bawah garis 1:1 kira-kira seimbang. Kuadrat korelasi (55%) menjelaskan variabilitas K, dan genotipe menjelaskan tambahan 38%. Korelasi naik menjadi 79,4% bila hitungan dirata-rata per genotipe. Bias bergantung genotipe: semua petak dua genotipe berada di atas garis 1:1 dan satu genotipe di bawahnya. Simulasi 100 kali pada 435 petak menunjukkan bias K nol pada batas 95% dan bias 0,24 (90%), 0,19 (99%), 0,83 (75%). Waktu proses di MATLAB kurang dari 10 detik per citra 480 × 1280 dan beberapa detik untuk penghitungan banyak citra.

## Kelebihan dan Keterbatasan
Kelebihan: penanganan eksplisit atas hitungan ganda dan buah yang terlewat melalui kerangka statistik dengan pengujian signifikansi; evaluasi skala besar (435 petak, lebih dari 28.000 citra per percobaan); hasil dilaporkan tanpa penyesuaian linear; analisis kontribusi tahap penghitungan terpisah dari deteksi.

Keterbatasan yang dinyatakan penulis: pengenalan manusia masih lebih unggul daripada deteksi otomatis; presisi tahap awal rendah akibat kemiripan warna buah hijau dan daun; bias hitung bergantung genotipe karena oklusi dan bentuk buah; hitungan berlebih karena buah tanaman tepi dan buah di perbatasan citra bertumpuk; pendekatan 3D yang dicoba sebelumnya tidak diadopsi karena pembangunan peta 3D tidak mudah dan menimbulkan galat; algoritma dapat diperluas dengan fitur bentuk, ukuran, dan warna.

Menurut pembacaan ringkasan ini, evaluasi deteksi tahap pertama hanya memakai 10 petak (408 citra), dan korelasi diukur per petak sehingga akurasi per buah tidak dilaporkan. Menurut pembacaan ringkasan ini, ambang W = 300 dipilih pada data validasi yang sama dengan yang dipakai melaporkan hasil, sehingga korelasi 74,2% dapat bersifat optimistis. Pembagian latih dan validasi didasarkan pada musim tanam yang berbeda, bukan pada pemisahan tanaman.

## Kaitan dengan Tinjauan main6
Makalah ini secara langsung menangani buah yang terlihat lebih dari sekali. Mekanismenya adalah pengelompokan statistik atas deteksi berurutan pada citra yang direkam setiap 5 cm: pengamatan pada citra berbeda dinyatakan sebagai buah yang sama bila pergeseran horizontalnya konsisten dengan model gerak (a + i·g) dan posisi vertikalnya hampir sama, dengan uji khi-kuadrat pada tingkat 95%. Ini berupa asosiasi geometris 2D tanpa pelacakan dalam video dan tanpa rekonstruksi 3D, serta tidak memakai pencocokan penampilan; penulis menyebut penambahan fitur bentuk, ukuran, dan warna sebagai pengembangan.

Hitungan tidak dilaporkan per kelas (hanya total buah per petak; kelas merah dan hijau hanya dipakai pada templat). Acuan hitungnya adalah jumlah buah yang dihitung dan dipanen secara fisik per tanaman, dengan label citra manual untuk 10 petak guna menguji deteksi. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan menggabungkan pengamatan ulang dengan model geometri yang eksplisit dan uji signifikansi, serta pengamatan bahwa hitungan menjadi bias bila buah dari objek tetangga masuk bidang pandang. Namun model pergeseran tetap hanya berlaku untuk lintasan translasi sejajar, bukan pandangan mengelilingi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `song2014automatic`.

Song dkk. mengusulkan metode dua tahap untuk menghitung buah paprika di rumah kaca: deteksi pada satu citra dengan *bag-of-words* dan SVM, lalu penggabungan estimasi dari banyak citra berurutan (setiap 5 cm) dengan pengelompokan statistik atas pengamatan berulang dan tidak lengkap. Pada 435 petak validasi, korelasi hitungan otomatis dengan hitungan manual mencapai 74,2% tanpa penyesuaian linear (galat standar 11,3 buah), dan 94,6% pada 10 petak bila buah pada citra diidentifikasi secara visual.

Catatan verifikasi data: Korelasi menurut W ada pada Tabel 2, probabilitas prior pada Tabel 1, bias simulasi pada Tabel 3, dan algoritma pada Lampiran. Hasil precision-recall hanya ditampilkan pada Gambar 7, sehingga hanya nilai yang disebut di teks (presisi 0,45, 0,61, 0,97; recall 0,17; F1 0,65) yang dapat dikutip. Persentase 94,6% berasal dari 10 petak (Gambar 8). Teks ekstraksi memuat beberapa simbol matematika yang rusak (misalnya pada Persamaan 1 dan Lampiran), sehingga rumus tidak ditulis ulang secara rinci; jumlah kamera dan ukuran jendela (40 × 90) dibaca dari teks yang terekstraksi sebagian ("4090 pixels").
