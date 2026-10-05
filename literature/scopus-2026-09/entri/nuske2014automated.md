# Automated visual yield estimation in vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nuske2014automated` |
| Judul asli | Automated visual yield estimation in vineyards |
| Penulis | Nuske, Stephen; Wilshusen, Kyle; Achar, Supreeth; Yoder, Luke; Narasimhan, Srinivasa; Singh, Sanjiv |
| Tahun | 2014 |
| Venue | Journal of Field Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [nuske2014automated.pdf](../pdf/nuske2014automated.pdf)
- DOI resmi: https://doi.org/10.1002/rob.21541

## Gambaran Umum
Makalah ini menyajikan sistem visi untuk memprakirakan hasil panen anggur (*vineyard yield estimation*) secara tidak merusak dan beresolusi spasial tinggi. Kamera menghadap ke samping dan lampu kilat dipasang pada kendaraan yang melaju di antara barisan tanaman anggur. Sistem mendeteksi buah anggur (*berry*) pada setiap citra, menghitung jumlah buah yang terlihat, lalu menghubungkan hitungan itu dengan bobot panen. Evaluasi dilakukan selama empat musim tanam pada beberapa kebun anggur anggur-vinifera untuk anggur anggur-minuman (*wine grape*) dan anggur meja (*table grape*), dengan varietas Traminette, Riesling, Chardonnay, Petite Syrah, Pinot Noir, dan Flame Seedless.

Pendeteksian berjalan dalam dua tahap: penentuan titik kunci kandidat buah (transformasi simetri radial atau detektor maksimum invarian) lalu klasifikasi kandidat memakai fitur warna dan tekstur pada *randomized KD-forest*. Untuk menghindari penghitungan ganda dari citra yang saling tumpang tindih, deteksi diproyeksikan ke dinding buah, barisan dibagi menjadi segmen sekitar 0,5 m, dan pada setiap segmen hanya citra dengan deteksi terbanyak yang dipertahankan.

Hasil utama menurut penulis: hitungan buah menjelaskan 60 sampai 75% varians hasil panen antarpohon (R2 0,6 sampai 0,73 pada Gambar 10; abstrak menyebut "hingga 75%"), dan galat prakiraan total hasil berkisar 3% sampai 11% dari total hasil panen setelah kalibrasi dari musim sebelumnya. Contoh angka: galat Chardonnay 2013 sebesar -2,47% (kalibrasi dari Chardonnay 2011) dan galat Flame Seedless 2013 sebesar 6,48% sampai 11,65% menurut sumber kalibrasi (Tabel VI dan VII).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa praktik prakiraan hasil di kebun anggur saat ini bergantung pada pengambilan sampel manual yang melelahkan, mahal, merusak, jarang secara spasial, dan memuat masukan subjektif. Sampel biasanya terlalu kecil dibanding variabilitas spasial kebun, sehingga prakiraan menjadi kasar dan tidak akurat. Prakiraan yang baik dibutuhkan untuk penjarangan buah, perencanaan panen, penyimpanan, dan penjualan.

Pendekatan visual yang ada dinilai terbatas pada satu isyarat visual (warna, bentuk, atau tekstur), pada set uji kecil (10 pohon atau satu pohon), pada gugus buah terisolasi, serta pada kondisi pengambilan citra yang terkendali dengan latar putih dan penjarangan buah buatan (*defruiting*) untuk memperlebar distribusi hasil. Pendekatan berbasis piksel buah juga peka terhadap ukuran buah, jarak, dan resolusi. Warna saja tidak memadai untuk buah hijau di antara daun hijau.

## Ide Utama
Penulis menggabungkan tiga isyarat visual (bentuk, tekstur, warna) dalam satu pengklasifikasi, lalu memodelkan hubungan antara hitungan citra dan hasil panen sebagai rangkaian fungsi linear: dari buah terdeteksi ke buah terlihat (kalibrasi deteksi), lalu dari buah terlihat ke total buah (kalibrasi keterlihatan, *visibility calibration*). Hasil panen dipandang sebagai $W_h = N_b W_b$, dan sistem hanya mengukur jumlah buah $N_b$. Menurut penulis, jumlah buah menjelaskan sekitar 90% variasi hasil, dan sisanya berasal dari bobot buah.

Ide kedua adalah mengoptimalkan ambang suara (*voting threshold*) $\tau_r$ pada klasifikasi untuk meminimalkan galat spasial, yang dikaitkan dengan R2 antara hitungan dan hasil panen. Ide ketiga adalah mendaftarkan deteksi ke posisi sepanjang baris dengan odometri visual dari kamera stereo, sehingga buah yang tampak pada beberapa citra berurutan tidak dihitung ganda.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Peralatan terbaru (2013) memakai kamera Prosilica GE4000 dengan lensa Nikkor 24 mm f/2.8D dan dua lampu kilat Einstein 640 di kedua sisi kamera, dipasang menghadap ke samping pada kendaraan utilitas kebun. Kamera stereo PointGrey BumbleBee2 menghadap ke bawah sekitar 45 derajat ke arah belakang untuk odometri visual. Kamera dipasang sekitar 0,9 sampai 1,5 m dari zona buah, citra diambil 5 Hz pada kecepatan 5,4 km/jam, dan kedua kamera disinkronkan dengan pulsa eksternal. Perangkat sebelum 2013 berbeda (Canon SX200IS dengan lampu halogen pada 2010; Nikon D300s dengan lampu cincin AlienBees pada 2011 dan 2012). Pengambilan citra paling andal dilakukan pada malam hari.

Dataset (Tabel I) mencakup antara lain: Traminette dan Riesling, Fredonia NY, September 2010 (98 dan 128 pohon, cahaya siang dengan lampu); Chardonnay, Modesto CA, Juni 2011 (636 pohon) dan Juni 2013 (24 pohon); Petite Syrah (30 pohon) dan Pinot Noir (32 pohon), Galt CA, Juni 2013; Flame Seedless, Delano CA, 2011, 2012, dan 2013 (masing-masing 88 pohon). Bobot panen dikumpulkan untuk setiap dataset sebagai acuan.

### 2. Deteksi titik kunci
Dua algoritma dipakai. Transformasi simetri radial (Loy dan Zelinsky) mencari titik puncak simetri melingkar pada rentang jari-jari. Detektor maksimum invarian (usulan baru) mencari puncak intensitas pantulan spekular di pusat buah yang disinari lampu kilat, lalu memvalidasinya dengan pertumbuhan wilayah berlapis (ambang 85% per cincin, tiga tingkat intensitas, dengan syarat sentroid dan bentuk tidak memanjang). Detektor ini bekerja untuk diameter buah dari sekitar 10 sampai lebih dari 100 piksel tanpa parameter ukuran.

### 3. Klasifikasi kandidat
Pada tiap kandidat diambil patch citra dan dihitung vektor warna enam dimensi (RGB dan L*a*b) serta salah satu dari tiga deskriptor tekstur: filter Gabor (empat skala, enam orientasi, 24 dimensi), SIFT (128 dimensi direduksi PCA menjadi 32), atau FREAK (200 dimensi direduksi PCA menjadi 32). Klasifikasi memakai *randomized KD-forest* dengan rasio suara $T_r > \tau_r$. Deteksi yang berdekatan dikelompokkan, dan kelompok yang lebih kecil dari ambang luas dibuang. Pelatihan memakai set kecil citra yang berisi pusat buah yang ditandai manual (10 citra pada Gambar 2).

### 4. Penggabungan pada urutan citra
Deteksi dari tiap citra diproyeksikan ke dinding buah memakai posisi kendaraan dari odometri visual (Kitt dkk.). Baris dibagi menjadi segmen sekitar 0,5 m. Pada segmen yang dicakup lebih dari satu citra, hanya deteksi dari citra dengan deteksi terbanyak yang dipertahankan, dengan alasan oklusi paling kecil dan menghindari registrasi halus pada buah yang bergerak karena angin. Hitungan per segmen kemudian dijumlahkan per baris, pohon, atau kelompok pohon.

### 5. Kalibrasi ke hasil panen
Kalibrasi deteksi memakai $\kappa_d = TP/(TP+FN)$ dan jumlah positif palsu per panjang baris: $\hat N_b^v = (N_b^d - FP)/\kappa_d$. Kalibrasi keterlihatan memakai $\hat N_b = \hat N_b^v/\kappa_\omega$ dan memerlukan data hasil panen musim sebelumnya atau sampel dalam musim. Ambang $\tau_r$ dioptimalkan dengan meminimalkan galat spasial yang diturunkan dari variansi laju positif benar dan positif palsu (Persamaan 16).

## Eksperimen dan Hasil
Evaluasi dilakukan pada keseluruhan dataset di atas dengan bobot panen sebagai acuan. Detektor titik kunci dievaluasi dengan *recall* (Tabel II); beberapa nilai: Riesling 2010 0,66 (simetri radial) dan 0,12 (maksimum invarian); Chardonnay 2011 0,68 dan 0,91; Petite Syrah 2013 0,87 dan 0,96. Waktu proses per citra pada CPU Intel i5-2500K (Tabel III) berkisar 0,92 detik (maksimum invarian dengan FREAK, tercepat) sampai 7,4 detik (simetri radial dengan Gabor, terlambat).

Studi laboratorium pada 56 gugus Thompson Seedless dengan penandaan manual (Tabel IV) dan pada kebun Traminette (Tabel V):

| Ukuran citra | R2 ke bobot gugus (lab) | Galat kuadrat rerata (lab) | R2 ke hasil panen (kebun) |
|---|---|---|---|
| Jumlah buah total (batas atas) | 0,95 | 9,3% | tidak dilaporkan |
| Jumlah buah terlihat 2D | 0,88 | 15,4% | 0,75 |
| Model elipsoid 3D | 0,85 pada tabel (teks menyebut 0,88) | 17% | 0,61 |
| Model *convex hull* 3D | 0,92 | 13,7% | 0,41 |

Pada kebun, korelasi hitungan buah terhadap bobot panen berkisar R2 0,6 sampai 0,73 menurut dataset (Gambar 10), sehingga 60 sampai 75% varians tertangkap. Pemilihan fitur: Gabor terbaik pada cahaya alami, FREAK pada lampu kilat biasa, SIFT pada lampu kilat terpolarisasi silang, dan SIFT paling baik digeneralisasi antar dataset tanpa fitur warna. Optimasi $\tau_r$ menaikkan akurasi spasial lebih dari 20%, dengan $\tau_r$ optimal 40 sampai 50% untuk Gabor dan FREAK serta 80% untuk SIFT.

Galat prakiraan total hasil (Tabel VI dan VII):

| Dataset target | Sumber kalibrasi | Galat prakiraan |
|---|---|---|
| Flame Seedless 2013 | Flame Seedless 2011 | 6,48% |
| Flame Seedless 2013 | Flame Seedless 2012 | 11,65% |
| Flame Seedless 2013 | Flame Seedless 2011 dan 2012 | 9,07% |
| Chardonnay 2013 | Chardonnay 2011 | -2,47% |

Kalibrasi lintas kebun untuk Chardonnay 2013: dari Traminette dan Petite Syrah galat sekitar 4% dan 5%, sedangkan dari Riesling dan Pinot Noir 17% dan 29%. Penulis menyimpulkan bahwa kalibrasi harus spesifik lokasi.

## Kelebihan dan Keterbatasan
Kelebihan: evaluasi dilakukan dari kendaraan bergerak pada ratusan pohon dan empat musim, dengan acuan bobot panen sebenarnya; sistem memperhitungkan oklusi, kesalahan deteksi, dan penghitungan ganda; kalibrasi dari musim sebelumnya pada kebun yang sama terbukti mendekati akurat.

Keterbatasan yang dinyatakan penulis: buah yang tidak terlihat oleh kamera (oklusi daun, pohon, dan antargugus) tidak diestimasi dan menjadi varians tak termodelkan; model volumetrik gugus (elipsoid, *convex hull*) tidak dapat dipakai di kebun karena gugus belum dapat dipisahkan satu dari lainnya; kalibrasi bersifat spesifik lokasi dan perlu data panen atau sampel; di kebun anggur meja berpembelahan (*split*) ada risiko menghitung buah dari kordon sisi lain; kinerja detektor titik kunci dan deskriptor bergantung kondisi cahaya sehingga perlu pemilihan per dataset; implementasi belum dioptimalkan untuk kecepatan (Gabor tidak efisien).

Menurut pembacaan ringkasan ini, penghitungan ganda ditangani dengan heuristik pemilihan satu citra per segmen 0,5 m, bukan dengan pencocokan identitas buah. Makalah tidak melaporkan metrik penghitungan buah per citra (misalnya galat hitungan terhadap hitungan manual per pohon) selain R2 dan galat total. Prakiraan total hasil untuk Chardonnay hanya diuji pada satu pasangan tahun (2011 ke 2013), dengan 24 pohon pada 2013. Ada ketidakkonsistenan kecil pada teks: R2 elipsoid 0,85 pada Tabel IV dan 0,88 pada teks, serta jumlah pohon Riesling dan Traminette 98 dan 128 pada Tabel I dibandingkan 224 pohon pada teks.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali secara eksplisit, yaitu pada gambar-gambar berurutan yang saling tumpang tindih dari kamera yang bergerak sepanjang baris. Mekanismenya adalah registrasi geometris: deteksi diproyeksikan ke koordinat dinding buah memakai odometri visual stereo, dan pada tiap segmen sekitar 0,5 m hanya citra dengan deteksi terbanyak yang dipertahankan, sedangkan deteksi dari citra lain pada segmen yang sama dibuang. Ini adalah pendekatan penghapusan duplikat berbasis posisi (kode C1), bukan pelacakan identitas buah per buah dan bukan pencocokan multi-pandang. Satu sisi baris dipotret; makalah tidak menggabungkan kedua sisi pohon, dan menyebut risiko menghitung buah dari sisi kordon lain sebagai tantangan.

Hitungan dilaporkan untuk buah secara keseluruhan, bukan per kelas (tidak ada kelas kematangan). Acuan adalah bobot panen per pohon atau per dataset, bukan hitungan buah manual di lapangan; hanya kalibrasi deteksi memakai anotasi citra manual (10 citra). Hal yang dapat dipindahkan ke pencacahan tandan sawit multisisi adalah skema kalibrasi bertahap (deteksi ke buah terlihat ke total) dengan koreksi $\kappa_d$ dan positif palsu, penggunaan segmen posisi untuk memilih satu pengamatan, dan tuntutan kalibrasi spesifik lokasi. Heuristik "citra dengan deteksi terbanyak" tidak membedakan identitas antar sisi pohon dan tidak langsung berlaku untuk tandan yang terlihat dari sisi berbeda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `nuske2014automated`.

Nuske dkk. (2014, *Journal of Field Robotics* 31(5):837-860) mengembangkan sistem prakiraan hasil anggur dari citra yang diambil dari kendaraan bergerak. Buah dideteksi dengan titik kunci dan klasifikasi warna dan tekstur, deteksi diproyeksikan ke posisi sepanjang baris memakai odometri visual dengan satu citra dipilih per segmen sekitar 0,5 m untuk mencegah penghitungan ganda, dan hitungan dikalibrasi ke hasil panen. Pada beberapa kebun dan empat musim, hitungan menjelaskan 60 sampai 75% varians hasil antarpohon, dan galat prakiraan total berkisar 3% sampai 11% setelah kalibrasi dari musim sebelumnya.

Catatan verifikasi data: R2 0,6 sampai 0,73 dan pernyataan 60 sampai 75% ada pada Bagian 5.5 (Gambar 10). Galat 3% sampai 11% ada pada abstrak dan Bagian 6; angka 6,48%, 11,65%, dan 9,07% pada Tabel VI; -2,47% pada Tabel VII; R2 laboratorium pada Tabel IV dan kebun pada Tabel V; waktu pada Tabel III; *recall* titik kunci pada Tabel II; jumlah pohon pada Tabel I. Nilai R2 per dataset pada Gambar 10, kurva pada Gambar 9, 11, 12, dan perbandingan numerik antar deskriptor tidak terbaca dari teks ekstraksi sehingga tidak dilaporkan. Teks ekstraksi memuat Tabel I-VII dengan sel terpisah sehingga pembacaan kolom adalah pembacaan ringkasan ini. Teks tidak menyebut galat hitungan terhadap hitungan manual per pohon, dan angka PCA, ambang, serta ukuran sampel pelatihan mengikuti yang tertulis di teks.
