# Grape cluster detection using uav photogrammetric point clouds as a low‐cost tool for yield forecasting in vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `torressanchez2021grape` |
| Judul asli | Grape cluster detection using uav photogrammetric point clouds as a low‐cost tool for yield forecasting in vineyards |
| Penulis | Torres-S\'anchez, Jorge; Mesas-Carrascosa, Francisco Javier; Santesteban, Luis-Gonzaga; Jim\'enez-Brenes, Francisco Manuel; Oneka, Oihane; Villa-Llop, Ana; Loidi, Maite; L\'opez-Granados, Francisca |
| Tahun | 2021 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape, nut crops |

## Tautan Akses
- PDF: [torressanchez2021grape.pdf](../pdf/torressanchez2021grape.pdf)
- DOI resmi: https://doi.org/10.3390/s21093083

## Gambaran Umum
Makalah ini mengembangkan alur kerja tanpa pengawasan (*unsupervised*) dan otomatis untuk mendeteksi tandan anggur pada varietas anggur merah menggunakan awan titik fotogrametri dari citra kendaraan udara nirawak (*unmanned aerial vehicle*, UAV) dan penyaringan warna. Data diambil di dua kebun anggur komersial di Traibuenas (Navarra, Spanyol utara) pada tahun 2019 dan 2020: varietas Graciano (1,37 ha) dan Garnacha tinta (0,91 ha). Pengaruh oklusi daun diuji dengan tiga perlakuan pembuangan daun: satu sisi baris, dua sisi baris, dan kontrol tanpa perlakuan.

Titik awan yang diklasifikasikan sebagai anggur diubah menjadi luas proyeksi pada bidang vertikal sejajar baris tanaman, lalu diregresikan terhadap bobot panen. Pada perlakuan pembuangan daun dua sisi, nilai $R^2$ antara luas proyeksi dan bobot panen adalah 0,81 (Gr-19), 0,56 (Gr-20), 0,63 (Ga-20), 0,77 (gabungan Gr-19 dan Ga-20), dan 0,52 (seluruh data). Pada kontrol, $R^2$ tertinggi 0,82 diperoleh pada Gr-19, sedangkan pada kebun dan gabungan lain nilainya rendah dan sebagian tidak signifikan. Perlakuan satu sisi menghasilkan $R^2$ rendah (0,01 sampai 0,31).

Makalah ini tidak menghitung jumlah buah atau tandan satuan; keluarannya adalah penaksir bobot panen berbasis luas proyeksi. Penulis menyatakan bahwa ini adalah penggunaan awan titik fotogrametri UAV pertama untuk deteksi tandan anggur.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Prakiraan hasil panen diperlukan untuk perencanaan panen, logistik pembelian anggur, dan produksi anggur olahan. Metode tradisional menimbang dan menghitung tandan pada sampel kecil tanaman lalu mengekstrapolasi ke seluruh kebun. Penulis menilai metode itu merusak, memakan waktu, dan kurang representatif secara sampling.

Pendekatan citra darat (kamera, sensor Kinect RGB-D, kendaraan yang melintasi kebun, pengambilan malam hari) dinilai terbatas oleh lereng, tanah yang dibajak atau basah, dan tanaman penutup tanah, serta oleh kemungkinan pemadatan tanah. UAV menawarkan resolusi spasial dan temporal tinggi serta tidak memadatkan tanah. Menurut makalah, awan titik fotogrametri UAV belum pernah dipakai untuk deteksi tandan anggur, padahal setiap titik memuat informasi warna RGB.

## Ide Utama
Titik awan fotogrametri yang dibangun dari citra nadir dan oblik berwarna dapat disaring secara geometris (rentang ketinggian tumbuh tandan) dan secara warna (anggur matang berwarna kebiruan) tanpa data latih. Titik yang tersisa diubah menjadi luas proyeksi, yang menjadi penaksir bobot panen per segmen baris. Karena titik berkoordinat, metode ini dapat menghasilkan peta hasil panen bila dikombinasikan dengan pembagian baris atau deteksi tanaman individu.

## Cara Kerja Langkah demi Langkah

### 1. Lokasi, perlakuan, dan akuisisi data
Kedua kebun berjarak tanam 3 × 1 m dengan baris berorientasi utara-selatan, tanaman dilatih sebagai *vertical-shoot positioned Cordon de Royat*. Graciano berumur 21 tahun pada awal penelitian dan Garnacha tinta satu tahun lebih muda. Pembuangan daun dilakukan pada 40 cm basal semua tunas. Di setiap zona sampel, enam tanaman diberi perlakuan dua sisi, enam tanaman kontrol, dan enam tanaman perlakuan satu sisi (sisi timur). Setiap set enam tanaman dipanen manual (25 September 2019 dan 21 September 2020 untuk Graciano; 14 September 2020 untuk Garnacha), dan bobot panen menjadi data validasi. Terdapat 18 lokasi sampel di Graciano (2019 dan 2020) dan 16 lokasi di Garnacha (2020). Data disingkat Gr-19, Gr-20, dan Ga-20.

Citra udara diambil pada 17 September 2019 (Graciano) dan 8 September 2020 (kedua kebun). Pada 2019 dipakai kamera Sony ILCE-6000 (24 MP, lensa 20 mm) pada quadcopter MD4-1000, terbang 10 m pada 2 m/s dengan interval 1 detik dan tumpang tindih samping 60%. Pada 2020 dipakai DJI Mavic 2 Pro dengan kamera Hasselblad L1D-20c (20 MP), terbang 15 m pada 1,5 m/s dengan interval 2 detik dan tumpang tindih samping 75%. Dua tipe jalur terbang dipakai: sejajar baris dengan kamera menghadap ke bawah, dan tegak lurus baris dengan sudut kamera 45°. Resolusi spasial citra nadir adalah 0,20 cm (2019) dan 0,38 cm (2020). Jumlah citra tidak dilaporkan.

### 2. Pembangunan awan titik
Citra nadir dan oblik diproses bersama di Agisoft Metashape Professional 1.7.0 dengan enam titik kendali tanah per kebun yang diukur dengan GPS RTK (akurasi 0,02 m planimetri dan 0,03 m altimetri). Kepadatan rerata awan titik Ga-20 adalah 30.902 titik/m², Gr-20 35.093 titik/m², dan area sampel Gr-19 yang terekonstruksi 320.411 titik/m².

### 3. Algoritma deteksi tandan
Algoritma ditulis di R 3.5.3 dengan paket `sf` dan `lidR`, dan berjalan otomatis dengan enam langkah:

1. Penipisan (*decimation*) awan titik ke kepadatan awan terendah (Ga-20, 30.902 titik/m²) dengan fungsi `homogenize`.
2. Pembuatan model elevasi digital dengan *cloth simulation filter* (ambang 0,5 m, resolusi kain 1 m, voksel 0,1 m).
3. Pembuangan titik di luar zona tandan, yaitu titik dengan tinggi di bawah 0,5 m dan di atas 1 m dari tanah.
4. Penyaringan warna: titik dengan $B/G > 1$ dan $B/R > 1$ diklasifikasikan sebagai anggur.
5. Penghapusan derau dengan *isolated voxels filter* (voksel sisi 0,1 m; titik dengan kurang dari 10 tetangga pada 27 voksel dianggap derau).
6. Perhitungan luas proyeksi titik anggur pada bidang vertikal sejajar baris, dengan penyangga (*buffer*) 1 cm per titik yang digabung agar tumpang tindih tidak dihitung ganda.

### 4. Analisis data
Regresi linear antara bobot panen dan jumlah titik atau luas proyeksi dilakukan di R untuk setiap kebun, perlakuan, dan kombinasi kebun guna menilai keterpindahan antarvarietas dan konfigurasi terbang.

## Eksperimen dan Hasil
Validasi memakai bobot panen per set enam tanaman. Empat area sampel di bagian timur Gr-20 dikeluarkan karena tumpang tindih citra buruk, dan sebagian area Gr-19 tidak terekonstruksi dengan benar akibat lereng ringan serta ketinggian terbang yang tidak konstan. Hal ini menjadi alasan penggantian platform dan konfigurasi terbang pada 2020.

Tabel 1 makalah melaporkan $R^2$ untuk jumlah titik terdeteksi dan luas proyeksi (ns: tidak signifikan; * p < 0,05; ** p < 0,01; *** p < 0,001):

| Perlakuan | Data | Area sampel | $R^2$ titik terdeteksi | $R^2$ luas proyeksi |
|---|---|---|---|---|
| Satu sisi | Gr-19 | 8 | 0,09 ns | 0,11 ns |
| Satu sisi | Gr-20 | 14 | 0,02 ns | 0,31 * |
| Satu sisi | Ga-20 | 16 | 0,05 ns | 0,11 ns |
| Satu sisi | Gr-19 + Ga-20 | 24 | 0,05 ns | 0,01 ns |
| Satu sisi | Semua | 38 | 0,00 ns | 0,06 ns |
| Dua sisi | Gr-19 | 7 | 0,57 ns | 0,81 *** |
| Dua sisi | Gr-20 | 14 | 0,55 ** | 0,56 ** |
| Dua sisi | Ga-20 | 16 | 0,48 ** | 0,63 *** |
| Dua sisi | Gr-19 + Ga-20 | 23 | 0,59 *** | 0,77 *** |
| Dua sisi | Semua | 37 | 0,35 *** | 0,52 *** |
| Kontrol | Gr-19 | 8 | 0,66 * | 0,82 ** |
| Kontrol | Gr-20 | 14 | 0,01 ns | 0,00 ns |
| Kontrol | Ga-20 | 16 | 0,18 ns | 0,17 ns |
| Kontrol | Gr-19 + Ga-20 | 24 | 0,11 ns | 0,22 * |
| Kontrol | Semua | 38 | 0,05 ns | 0,13 * |

Luas proyeksi lebih baik daripada jumlah titik sebagai penaksir bobot panen. Pada perlakuan dua sisi, gabungan Gr-19 dan Ga-20 (dua varietas, dua sensor, dua konfigurasi terbang) mencapai $R^2$ 0,77, yang menurut penulis menunjukkan keterpindahan metode. Gr-20 memiliki garis regresi sejajar tetapi berada di bawah garis lain; penulis menduga penyebabnya jeda 13 hari antara terbang dan panen, dibandingkan 8 hari (Gr-19) dan 6 hari (Ga-20). Pada perlakuan satu sisi, tandan di sisi barat tertutup daun sehingga hubungan linear hilang. Pada kontrol, hanya Gr-19 yang menonjol ($R^2$ 0,82); penulis mengaitkannya dengan resolusi citra 0,2 cm, sebagai dugaan.

Sebagai pembanding, penulis menyebut $R^2$ 0,59 pada awan titik Kinect di lapangan dengan pembuangan daun, $R^2$ 0,93 pada metode foto lapangan yang memerlukan pelatihan deteksi, dan $R^2$ 0,82 antara hasil prediksi dan taksiran pada citra UAV tunggal. Angka-angka itu dikutip dari makalah lain dan tidak dibandingkan pada data yang sama.

Waktu kerja yang dilaporkan: kurang dari 2 jam untuk terbang, sekitar 16 jam untuk pembangunan awan titik, dan hampir 1 jam untuk analisis; intervensi pengguna sekitar 20 menit untuk penentuan titik kendali tanah. UAV 2020 berharga sekitar 1.500 USD.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: memakai UAV dan sensor murah serta perangkat lunak R gratis; memproses seluruh kebun sehingga tidak terbatas pada titik sampel; titik berkoordinat sehingga dapat dipetakan; tidak memerlukan data latih; dan tidak memerlukan kendaraan darat yang melintasi baris.

Keterbatasan yang dinyatakan penulis: metode hanya bekerja cukup baik pada tanaman dengan pembuangan daun dua sisi, praktik yang tidak selalu layak karena risiko terbakar matahari atau pematangan berlebih; ketinggian terbang rendah menuntut lebih banyak penerbangan untuk kebun besar; anggur putih tidak dapat dideteksi karena pantulan anggur dan daun serupa pada kamera RGB; dan jeda terbang-panen mungkin memengaruhi hubungan luas dan bobot.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup 14 sampai 38 area sampel per konfigurasi dengan acuan bobot panen agregat per enam tanaman, sehingga ketepatan pencacahan tandan atau buah satuan tidak dapat dinilai. Ambang warna $B/G > 1$ dan $B/R > 1$ ditetapkan untuk anggur matang berwarna kebiruan dan tidak diuji pada tahap pematangan lain. Lama pemrosesan awan titik (sekitar 16 jam) juga merupakan beban praktis yang tidak dibahas sebagai keterbatasan.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menghitung buah satuan dan tidak memiliki mekanisme identitas buah yang sama. Pandangan ganda (citra nadir dan oblik) dipakai hanya untuk membangun awan titik 3D; setelah itu, titik berwarna biru dikumpulkan menjadi satu luas proyeksi per segmen baris. Buah yang terlihat pada beberapa citra otomatis menyatu dalam awan titik yang sama karena fotogrametri menempatkan titik pada koordinat dunia tunggal, tetapi tidak ada langkah penggabungan instans tandan atau penetapan identitas per buah. Hitungan per kelas tidak dilaporkan; acuan berupa bobot panen per kelompok enam tanaman, bukan jumlah tandan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan bahwa rekonstruksi 3D dari banyak pandang menempatkan pengamatan berulang pada koordinat dunia yang sama, serta penyaringan ketinggian dan warna sebagai langkah praklasifikasi. Keterbatasannya adalah penaksiran massa melalui luas proyeksi tidak memberikan hitungan per kelas dan bergantung pada oklusi daun yang rendah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `torressanchez2021grape`.

Torres-Sánchez dkk. (2021) mengembangkan alur kerja otomatis tanpa data latih untuk mendeteksi tandan anggur merah dari awan titik fotogrametri UAV dengan penyaringan ketinggian, warna ($B/G > 1$ dan $B/R > 1$), dan penghapusan derau, lalu meregresikan luas proyeksi titik anggur terhadap bobot panen. Pada pembuangan daun dua sisi, $R^2$ mencapai 0,81 pada Gr-19 dan 0,77 pada gabungan Gr-19 dan Ga-20; pada kontrol, $R^2$ 0,82 hanya dicapai pada satu kumpulan data (Gr-19).

Catatan verifikasi data: Seluruh nilai $R^2$ dan jumlah area sampel berasal dari Tabel 1 (halaman 9) dan teks Bagian 3.2. Kepadatan titik berasal dari Bagian 3.1; parameter algoritma dari Bagian 2.3; konfigurasi terbang dari Bagian 2.2. Jumlah citra, jumlah total tandan, dan galat dalam satuan bobot tidak dilaporkan di teks. Teks ekstraksi baik, tetapi tabel ditulis berurutan per sel sehingga susunan baris-kolom disimpulkan dari urutan; susunan itu konsisten dengan angka yang disebut di teks (misalnya 0,81 dan 0,77 untuk dua sisi, 0,82 untuk kontrol Gr-19).
