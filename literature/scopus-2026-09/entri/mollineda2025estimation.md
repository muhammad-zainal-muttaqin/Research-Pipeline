# Estimation of orange tree production by regression from video segments under uncontrolled conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mollineda2025estimation` |
| Judul asli | Estimation of orange tree production by regression from video segments under uncontrolled conditions |
| Penulis | Mollineda, Ram\'on A.; Sandoval, Javier; Rodr\'\iguez, Christian D.; Heredia, Jos\'e A. |
| Tahun | 2025 |
| Venue | Neural Computing and Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [mollineda2025estimation.pdf](../pdf/mollineda2025estimation.pdf)
- DOI resmi: https://doi.org/10.1007/s00521-024-10772-4

## Gambaran Umum

Makalah ini mengestimasi jumlah jeruk (*orange*) yang terlihat pada satu sisi pohon dari video barisan tanaman yang direkam kamera pada kendaraan pertanian (traktor) dalam kondisi lapangan tidak terkendali. Pendekatan yang dipakai adalah pencacahan melalui regresi (*counting by regression*), yaitu jaringan saraf dalam memetakan satu bingkai langsung ke bilangan jumlah buah tanpa mendeteksi setiap buah. Prediksi per bingkai pada urutan bingkai yang berpusat pada satu pohon (segmen video) kemudian diringkas dengan median menjadi satu estimasi per pohon.

Data berupa kumpulan data baru, *ambimetrics orange counting dataset*, yang berisi lima video barisan pohon jeruk dengan total 99 pohon. Satu video (baris 5, 22 pohon) terdampak *sunlight flare* dan dikeluarkan dari eksperimen, sehingga eksperimen memakai empat baris. Tiga model dibandingkan: EfficientNetB0, FPN-linear, dan FPN-map (*feature pyramid network* dengan EfficientNetB0 sebagai *backbone*).

Hasil utama: galat median absolut (MedAE) pada tingkat pohon turun dibandingkan satu bingkai; pada EfficientNetB0 dan FPN-map, urutan 11 bingkai menurunkan MedAE masing-masing 22% dan 25% dibandingkan satu bingkai. Nilai MedAPE terendah pada tingkat urutan adalah 0,137 (FPN-map, urutan 7 bingkai). Uji peringkat bertanda Wilcoxon menunjukkan keunggulan urutan multi-bingkai yang signifikan pada EfficientNetB0 dan FPN-map, tetapi tidak pada FPN-linear.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi produksi buah umumnya bergantung pada pengamat manusia berpengalaman yang dinilai penulis tidak akurat, memakan waktu, melelahkan, sulit diperluas skalanya, dan bergantung pada pengamat. Pencacahan berbasis deteksi bergantung pada akurasi deteksi yang peka terhadap kepadatan objek, oklusi, dan perubahan cahaya, serta memerlukan anotasi kotak atau titik untuk setiap buah.

Penulis membedakan dua skenario: menghitung buah yang terlihat pada satu pandang pohon, dan menghitung total buah pada pohon dari beberapa sisi (dua atau empat). Menurut rujukan yang dikutip makalah, pencitraan dua sisi cenderung menaksir terlalu rendah dan pencitraan empat sisi cenderung menaksir terlalu tinggi. Makalah ini mengerjakan skenario pertama dan menyatakan bahwa, sepengetahuan penulis, belum ada penelitian terdahulu yang menaksir jumlah buah dari banyak bingkai video. Penelitian terdahulu umumnya memakai satu citra per sisi pohon dalam kondisi terkendali.

## Ide Utama

Satu pohon pada video muncul pada banyak bingkai yang saling tumpang tindih tinggi. Setiap bingkai menghasilkan estimasi lemah (*weak estimate*) jumlah jeruk yang terlihat, dan penggabungan estimasi lemah itu diharapkan lebih tangguh terhadap galat deteksi pohon, tumpang tindih buah, kerapatan daun, pencahayaan, serta sudut dan jarak sensor ke buah. Penggabungan memakai median agar tahan terhadap pencilan. Karena satu pohon memiliki beberapa pengukuran, ketidakpastian estimasi dapat dihitung dengan simpangan absolut median (*median absolute deviation*, MAD).

Yang dihitung adalah jumlah jeruk yang terlihat pada satu sisi pohon, bukan total buah pada pohon. Penulis menyatakan bahwa jumlah buah terlihat dipakai sebagai contoh dari populasi buah yang tidak diketahui, dan bahwa pelatihan terhadap hasil panen aktual memerlukan anotasi hasil panen yang belum tersedia.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Video direkam dengan kamera RealSense D435 yang dipasang pada kendaraan pertanian bergerak pada kecepatan 2 sampai 5 km per jam (0,83 sampai 1,39 m per detik). Kamera berada di sisi kendaraan yang berlawanan dengan barisan agar jarak ke pohon maksimal. Lokasi ialah kebun jeruk dengan jarak antarpohon sekitar 3 m, baik dalam satu baris maupun antarbaris. Laju bingkai 30 FPS, citra RGB 24 bit berukuran 480 x 640 piksel, dan bidang pandang sekitar 2 m lebar kali 2,5 m tinggi. Semua rekaman diambil sekitar tengah hari pada hari cerah. Bingkai diekstraksi dengan paket pyrealsense2. Kultivar jeruk dan lokasi geografis kebun tidak dilaporkan dalam teks.

Jumlah pohon per baris adalah 20, 20, 19, 18, dan 22 (total 99). Baris 5 dikeluarkan karena terdampak *sunlight flare*, tetapi tetap disertakan dalam kumpulan data.

### 2. Anotasi

Satu bingkai kunci pada setiap pohon ditentukan secara manual, lalu segmen $2n+1$ bingkai berpusat pada bingkai kunci diekstraksi otomatis dengan $n=5$ (11 bingkai per pohon). Total 847 bingkai (77 pohon x 11 bingkai) dianotasi. Hanya jeruk dengan sekitar 50% permukaan atau lebih yang terlihat yang dihitung, untuk mengurangi subjektivitas. Anotasi berupa titik pada alat makesense.ai dengan waktu rata-rata sekitar 45 sampai 60 detik per bingkai; skrip Python menghitung titik menjadi label bingkai. Label urutan $c_i$ ialah rerata anotasi bingkai dalam urutan tersebut, dan seluruh bingkai dalam urutan itu diberi label $c_i$ yang sama saat pelatihan. Anotasi otomatis dengan YOLOv5 dan YOLOv7 pralatih dinilai tidak layak karena cacat sistematis (YOLOv5 menaksir berlebih dan menghitung ulang beberapa jeruk; YOLOv7 hampir tidak mendeteksi di area teduh; keduanya terganggu oleh gerombol jeruk dan jeruk di tanah).

### 3. Model regresi dan penggabungan multi-bingkai

Model $m$ memetakan citra RGB ke bilangan real. Untuk urutan $x_i$ berisi $l$ bingkai, estimasi per bingkai $\hat{c}_{ij}=m(f_{ij})$ diringkas menjadi $\hat{c}_i=S(\hat{y}_i)$ dengan $S$ berupa median. Tiga model dipakai: EfficientNetB0 dengan jaringan terhubung penuh kecil, FPN-linear (peta multiskala dilinearkan lalu digabung), dan FPN-map (peta dinaikkan skalanya ke resolusi yang sama lalu digabung sehingga distribusi spasial dipertimbangkan). Blok konvolusi terakhir *backbone* (blok 7) ikut dilatih.

### 4. Metrik

Akurasi diukur dengan MedAE dan MedAPE (galat persentase absolut median) pada tingkat bingkai dan tingkat urutan; ketidakpastian diukur dengan MAD per pohon dan MAD global.

### 5. Protokol eksperimen

Validasi silang empat lipatan mengikuti empat baris video sehingga kondisi akuisisi satu baris tidak terbagi antara data latih dan uji. Eksperimen berjumlah 960: 3 model x 4 ukuran urutan x 4 lipatan x 20 kombinasi hiperparameter acak. Ruang hiperparameter mencakup dropout {0,2; 0,3; 0,4; 0,5}, ukuran lapisan padat {8, 16, 32, 64}, laju belajar $10^{-5}$ sampai $10^{-2}$, pengoptimal {Adam, Adam dengan CosineDecay}, aktivasi keluaran {linear, sigmoid}, dan ukuran *batch* {16, 24, 32}. Studi I membandingkan regresi pada urutan 1, 3, 7, dan 11 bingkai; Studi II menghitung korelasi keluaran YOLOv5 dan YOLOv7 dengan anotasi manual.

## Eksperimen dan Hasil

Data uji ialah empat baris video (77 pohon, 847 bingkai) dengan acuan berupa anotasi manual jumlah jeruk terlihat. Tidak ada hitungan panen atau hitungan fisik pohon. Pembanding ialah EfficientNetB0 terhadap dua varian FPN, serta urutan 1 bingkai terhadap 3, 7, dan 11 bingkai.

Tabel 4 makalah (MedAE; untuk urutan ditulis tingkat bingkai/tingkat urutan; MedAPE pada tingkat urutan, kecuali kolom 1 bingkai):

| Model | 1 bingkai: MedAE | 1 bingkai: MedAPE | 3 bingkai: MedAE | 3 bingkai: MedAPE | 7 bingkai: MedAE | 7 bingkai: MedAPE | 11 bingkai: MedAE | 11 bingkai: MedAPE |
|---|---|---|---|---|---|---|---|---|
| EffNetB0 | 3,20 | 0,186 | 2,70/2,71 | 0,169 | 2,61/2,66 | 0,155 | 2,61/2,51 | 0,151 |
| FPN-linear | 2,79 | 0,147 | 2,54/2,42 | 0,149 | 2,61/2,58 | 0,152 | 2,57/2,42 | 0,163 |
| FPN-map | 3,10 | 0,217 | 2,45/2,39 | 0,147 | 2,52/2,52 | 0,137 | 2,38/2,31 | 0,151 |

Ketidakpastian (MAD, Tabel 5):

| Model | 3 bingkai | 7 bingkai | 11 bingkai |
|---|---|---|---|
| EffNetB0 | 0,21 | 0,47 | 0,54 |
| FPN-linear | 0,19 | 0,43 | 0,48 |
| FPN-map | 0,17 | 0,39 | 0,57 |

Nilai p uji Wilcoxon (Tabel 6; MedAE tingkat pohon, 1 bingkai terhadap urutan; $\alpha=0,05$):

| Model | 1 vs 3 bingkai | 1 vs 7 bingkai | 1 vs 11 bingkai |
|---|---|---|---|
| EffNetB0 | 0,014 | 0,023 | 0,005 |
| FPN-linear | 0,975 | 0,951 | 0,635 |
| FPN-map | 0,012 | 0,023 | 0,019 |

Korelasi Pearson antara keluaran detektor pralatih dan anotasi manual (Tabel 7) naik seiring panjang urutan: YOLOv5 terhadap anotasi 0,82 (1 bingkai) hingga 0,91 (11 bingkai), YOLOv7 terhadap anotasi 0,81 hingga 0,87, dan YOLOv5 terhadap YOLOv7 0,87 hingga 0,91; semua nilai p mendekati nol. Penulis memakai hasil ini sebagai bukti kelayakan anotasi manual.

Temuan lain yang dinyatakan penulis: MedAE cenderung turun dengan bertambahnya panjang urutan dan kompleksitas model; galat terbesar terjadi pada ujung distribusi jumlah jeruk yang jarang datanya; residual FPN-map pada rentang jumlah rendah dan tinggi umumnya positif, artinya menaksir terlalu rendah; dispersi (MAD) membesar seiring panjang urutan, dan model FPN memiliki ketidakpastian lebih rendah daripada EfficientNetB0 kecuali pada urutan 11 bingkai. Pada Tabel 1 penulis melaporkan hasil karya ini sebagai galat absolut 2,3 dan galat relatif 0,14. Penulis menyebut MedAPE 13,7% FPN-map pada urutan 7 bingkai sebagai laju yang menjanjikan dibandingkan sekitar 9% pada tugas regresi yang lebih terkendali di literatur.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis: pemakaian kamera pada kendaraan pertanian berbiaya rendah dan sering dipakai, pembagian data per baris video yang mencegah kebocoran kondisi akuisisi, pengujian statistik nonparametrik, perhitungan ketidakpastian, serta pelepasan kode dan kumpulan data secara publik.

Keterbatasan yang dinyatakan penulis: anotasi hanya menghitung jeruk yang terlihat sekitar 50% atau lebih sehingga jumlah pasti jeruk tidak dicari dan kemungkinan ada negatif palsu; segmen berpusat pada pohon diekstraksi manual karena deteksi pohon di luar cakupan; baris 5 dikeluarkan karena *sunlight flare*; belum ada anotasi hasil panen sehingga estimasi produksi sebenarnya belum dapat dilatih; hasil bergantung pada konfigurasi akuisisi tertentu (30 FPS, bidang pandang sekitar 2 m kali 2,5 m, kecepatan 3 sampai 5 km per jam); regresi sulit dijelaskan prediksinya; sebaran jumlah jeruk yang jarang di kedua ujung membatasi generalisasi.

Menurut pembacaan ringkasan ini: (a) data sangat kecil, yakni 77 pohon dan 4 lipatan, dengan nilai MedAE yang selisihnya antarmodel kecil dan tidak diuji signifikansinya antarmodel; (b) pada FPN-linear keunggulan multi-bingkai tidak terbukti, dan pada MedAPE FPN-linear dan EfficientNetB0 hasilnya tidak monoton terhadap panjang urutan (misalnya FPN-linear 0,147 pada 1 bingkai dan 0,163 pada 11 bingkai); (c) label bingkai ialah rerata anotasi urutan sehingga tidak merepresentasikan jumlah sebenarnya pada bingkai itu; (d) hitungan per urutan tidak mengatasi pertanyaan apakah buah yang sama dihitung dua kali pada sisi yang berbeda, karena yang ditaksir hanyalah jumlah buah terlihat pada satu sisi; (e) pencarian hiperparameter dievaluasi pada lipatan yang sama dengan pelaporan hasil, dan makalah tidak menyebut pemisahan data validasi.

## Kaitan dengan Tinjauan main6

Makalah ini tidak menangani buah yang sama terlihat lebih dari sekali dengan mekanisme identitas. Bingkai-bingkai dalam satu segmen memang memuat buah yang sama berulang kali karena tumpang tindih tinggi, tetapi makalah tidak mencocokkan atau melacak buah antarbingkai. Redundansi itu dihadapi dengan merata-ratakan (median) estimasi jumlah per bingkai, sehingga hitungan akhir ialah ringkasan statistik jumlah yang terlihat per bingkai, bukan hitungan buah unik. Hitungan tidak dilaporkan per kelas (hanya satu kelas, jeruk terlihat), dan acuan hitungnya adalah anotasi titik pada citra (rerata per urutan), bukan hasil panen maupun hitung manual di lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan agregasi median banyak bingkai untuk menekan galat dan menghitung ketidakpastian (MAD) per pohon; protokol validasi silang per baris atau per kelompok; dan peringatan bahwa hitungan jumlah terlihat per sisi tidak otomatis menjadi hitungan unik. Pendekatan ini tidak menyelesaikan identitas lintas pandang, sehingga paling cocok sebagai pembanding berbasis regresi tanpa pencocokan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `mollineda2025estimation`.

Mollineda dkk. (2025) mengestimasi jumlah jeruk yang terlihat pada satu sisi pohon dengan regresi dari urutan bingkai video barisan pohon yang direkam dari kendaraan pertanian, lalu menggabungkan prediksi per bingkai dengan median. Pada kumpulan data baru berisi empat baris video yang dipakai dalam eksperimen (77 pohon), urutan multi-bingkai menurunkan galat median absolut dibandingkan satu bingkai secara signifikan pada EfficientNetB0 dan FPN-map, tetapi tidak pada FPN-linear. Metode ini tidak mencocokkan buah antarbingkai dan tidak melaporkan hitungan per kelas.

Catatan verifikasi data: Angka MedAE dan MedAPE bersumber dari Tabel 4, MAD dari Tabel 5, nilai p dari Tabel 6, dan korelasi dari Tabel 7. Jumlah pohon per baris bersumber dari Tabel 2, sedangkan 77 pohon dan 847 bingkai dari Seksi 3.2 (77 dihitung sebagai 99 dikurangi 22 pada baris 5, sesuai 20 + 20 + 19 + 18). Penurunan MedAE 22% dan 25% (urutan 11 bingkai) tertulis di Seksi 4.2, sedangkan Kesimpulan menyebut pengurangan 25% pada urutan 7 dan 11 bingkai; tulisan tidak sepenuhnya konsisten dan kutip dengan hati-hati. Teks juga menulis "five videos" pada Seksi 3.1 dan "four" pada pendahuluan dan Seksi 4.1 (baris 5 dikeluarkan). Pada Seksi 3.1 laju kendaraan ditulis dengan satuan yang rusak ("kms", "ms") akibat ekstraksi, dan nilai $\alpha$, indeks, serta rumus terbaca sebagian rusak, tetapi nilai angka tabel terbaca utuh. Kultivar jeruk, lokasi kebun, tanggal rekaman, dan jumlah jeruk total tidak dilaporkan dalam teks. Angka galat absolut 2,3 dan relatif 0,14 pada Tabel 1 tidak dikaitkan dengan model dan panjang urutan tertentu dalam teks.
