# Cross-Day Grape Cluster Tracking Using Branch-Based 3D Alignment in Vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yoshida2026cross` |
| Judul asli | Cross-Day Grape Cluster Tracking Using Branch-Based 3D Alignment in Vineyards |
| Penulis | Yoshida, Takeshi; Teng, Poching; Ota, Tomohiko; Murakami, Noriyuki |
| Tahun | 2026 |
| Venue | Journal of Robotics and Mechatronics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [yoshida2026cross.pdf](../pdf/yoshida2026cross.pdf)
- DOI resmi: https://doi.org/10.20965/jrm.2026.p0953

## Gambaran Umum
Makalah ini (laporan pengembangan di *Journal of Robotics and Mechatronics* 38(3), 2026) mengusulkan kerangka penyelarasan 3D berbasis cabang (*branch-based 3D alignment*) untuk melacak tandan anggur yang sama pada hari pengamatan yang berbeda. Struktur tetap tanaman, yaitu batang dan cabang utama, direkonstruksi dengan *Structure from Motion* (SfM). Sistem koordinat tiap hari disamakan melalui pencocokan fitur SIFT dan transformasi kesamaan (*similarity transformation*). Tandan yang dideteksi CenterNet kemudian dipasangkan antarhari berdasarkan kedekatan di ruang 3D bersama.

Data berasal dari kebun anggur luar ruangan di NARO Institute of Fruit Tree and Tea Science, Tsukuba, Jepang. Empat pohon anggur dipilih dan 49 tandan diamati dari 30 Mei sampai 20 Juni 2022. Citra diambil dengan satu kamera GoPro HERO11 Black (5312×2988 piksel) yang dibawa berjalan oleh operator.

Metode ini berhasil melacak 34 dari 49 tandan selama tiga minggu, yaitu tingkat keberhasilan 69,39%. Tanpa penyelarasan cabang (hanya normalisasi titik berat), keberhasilan 0,00%. Kegagalan terutama disebabkan pergeseran tandan akibat pertumbuhan dan oklusi berat sebelum pemangkasan perbungaan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa produksi buah domestik di Jepang menurun, harga grosir naik, dan tenaga kerja pertanian menua. Kebutuhan tenaga kerja budi daya anggur disebut sekitar 307 jam per 10 are, dibandingkan sekitar 12 jam untuk padi. Kondisi ini mendorong pemantauan pertumbuhan tandan secara otomatis untuk estimasi hasil, pengendalian penyakit, dan penentuan waktu panen.

Pada hari yang sama, tandan dapat dicocokkan dengan fitur tampilan seperti bentuk, ukuran, dan warna. Antarhari, tandan tumbuh, cabang bergeser, dan kondisi sudut pandang serta pencahayaan berubah, sehingga korespondensi antarhari sulit dibangun. Penulis menyatakan bahwa sedikit penelitian membangun korespondensi buah yang konsisten lintas hari.

## Ide Utama
Penulis memakai struktur pohon yang stabil (batang dan cabang utama) sebagai penanda untuk membangun kerangka koordinat 3D yang konsisten antarhari. Setelah kerangka koordinat disatukan, tandan yang berdekatan di ruang 3D dianggap tandan fisik yang sama, tanpa kontrol posisi pengambilan citra yang ketat dan tanpa sinkronisasi waktu.

Penyelarasan tidak dievaluasi dengan metrik galat registrasi tersendiri. Penulis menilainya secara tidak langsung melalui keberhasilan pelacakan tandan.

## Cara Kerja Langkah demi Langkah

```
 Hari A / Hari B (masing-masing):
 citra -> SfM -> normalisasi skala -> titik cabang (Mask R-CNN)
          \-> deteksi tandan (CenterNet) -> triangulasi 3D
 Pencocokan cabang A-B -> penyelarasan koordinat -> asosiasi lintas hari
```

### 1. Akuisisi data
Lokasi: kebun anggur NARO (NIFTS), Tsukuba. Empat pohon anggur, 49 tandan, pengamatan 30 Mei sampai 20 Juni 2022 dengan citra diambil setiap beberapa hari. Sistem pelatihan kebun adalah bentuk H pemangkasan pendek, dengan cabang utama kurang lebih lurus; citra diambil dengan berjalan di sepanjang struktur linear itu. Hanya tandan primer yang dilacak karena tandan sekunder dibuang saat penjarangan. Periode sebelum pembungkusan buah dipilih karena sesudahnya tandan tertutup. Kultivar tidak dilaporkan. Jumlah total citra tidak dilaporkan; waktu komputasi dinilai dengan sekitar 100 citra.

### 2. Rekonstruksi SfM dan normalisasi skala
Citra tiap hari diproses terpisah dengan SfM di OpenMVG. Skala absolut dipulihkan dengan penanda AR ArUco DICT_6X6_250 berukuran sisi 0,152 m. Panjang empat sisinya diestimasi lewat triangulasi multi-pandang, lalu faktor skala $s_0 = L_{true}/L_{measured}$ diterapkan. Penanda hanya dipakai untuk skala, bukan untuk penyelarasan lintas hari, karena dipasang dengan dudukan magnet dan posisinya tidak tetap. Titik yang jauh dari kamera lebih dari ambang $r_{max}$ dibuang, lalu titik berat awan titik dipindahkan ke titik asal.

### 3. Ekstraksi titik cabang
Setiap titik 3D diproyeksikan kembali ke citra dan dipertahankan hanya bila jatuh di dalam masker cabang hasil segmentasi instans Mask R-CNN. Awan titik mentah SfM rata-rata sekitar 16 juta titik; setelah penyaringan tersisa rata-rata sekitar 5.000 titik fitur jarang.

### 4. Pencocokan deskriptor dan estimasi transformasi
Untuk titik kueri hari A, kandidat dari hari B dipilih dalam radius lokal $r_{max}$. Deskriptor SIFT 128 dimensi dari seluruh pengamatan titik dikumpulkan, pasangan dengan jarak L2 terkecil dicari, dan uji rasio Lowe dengan $\tau$ umumnya 0,6 menolak kecocokan ambigu. Transformasi kesamaan (skala, rotasi, translasi) diestimasi dengan metode Umeyama bersama RANSAC.

### 5. Deteksi tandan dan asosiasi
CenterNet dipilih karena hanya memerlukan anotasi kotak pembatas. Dalam satu hari, tandan dari beberapa pandang dipasangkan dengan triangulasi, dan kombinasi dengan skor kemungkinan terakumulasi $S(x)=\sum_n L_n(\pi_n(x))$ tertinggi dipilih sebagai tandan fisik yang sama. Antarhari, tandan a dan b dipasangkan bila jarak Euklides di ruang yang telah disatukan kurang dari $\delta = 50$ mm; keputusan akhir berdasarkan jarak minimum, dan ambang hanya berfungsi sebagai penyaring.

## Eksperimen dan Hasil
Detektor CenterNet dilatih dengan dua model menurut periode (awal dan akhir), masing-masing dengan 100 citra latih dan 20 citra uji terpisah. Perangkat keras: Intel Core i9-7900X, NVIDIA TITAN RTX 24 GB, RAM 128 GB.

| Model | Precision | Recall | F1 | AP50 |
|---|---|---|---|---|
| Periode awal | 0,443 | 0,805 | 0,571 | 0,658 |
| Periode akhir | 0,846 | 0,957 | 0,898 | 0,927 |

Evaluasi pelacakan memakai 49 tandan yang berhasil dideteksi dan diverifikasi pada pengamatan awal, sehingga kinerja deteksi dipisahkan dari kinerja asosiasi.

| Metode | Keberhasilan pelacakan |
|---|---|
| Tanpa penyelarasan cabang (hanya titik berat) | 0,00% |
| Usulan (dengan penyelarasan cabang) | 69,39% (34 dari 49 tandan) |

Waktu komputasi untuk sekitar 100 citra: SfM OpenMVG 14 menit, segmentasi cabang Mask R-CNN 58 detik, deteksi CenterNet 44 detik, dan pelacakan lintas dua hari 12 menit.

Penulis menyebut tiga penyebab kegagalan: pergeseran tandan ke luar akibat pertumbuhan sehingga menempati posisi tandan lain dari tanggal sebelumnya, oklusi berat oleh perbungaan yang memanjang dan saling menutupi sebelum pemangkasan, serta tata letak cabang. Pelacakan paling berhasil bila tandan terletak berselang-seling pada sisi berlawanan cabang lateral.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: penyelarasan bertumpu pada struktur yang stabil sehingga tidak memerlukan posisi kamera yang ketat; ablasi menunjukkan penyelarasan mutlak diperlukan; tandan yang terlacak dinilai cukup mewakili sebaran spasial tandan untuk analisis tren pertumbuhan.

Keterbatasan yang dinyatakan penulis: asosiasi hanya memakai kedekatan lokal setelah penyelarasan, tanpa optimasi global; kegagalan pada tandan yang berdekatan dan oklusi; rencana pengembangan ke optimasi global tingkat pohon.

Menurut pembacaan ringkasan ini: skala evaluasi kecil (empat pohon, 49 tandan, tiga minggu, satu lokasi); galat penyelarasan tidak dilaporkan terpisah; pembanding hanya satu ablasi tanpa penyelarasan, tanpa metode pelacakan lain; hanya tandan primer yang dilacak; metode bergantung pada hasil SfM dan segmentasi cabang yang memakan waktu menit per pasangan hari; kelas atau atribut buah tidak ditangani.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tandan yang terlihat berulang, baik antarpandang dalam satu hari (triangulasi dan akumulasi kemungkinan heatmap CenterNet) maupun antarhari (penyatuan koordinat lewat cabang lalu pencocokan jarak 3D dengan ambang 50 mm). Mekanismenya adalah rekonstruksi 3D dan pencocokan multi-pandang. Hitungan per kelas tidak dilaporkan. Acuan evaluasi adalah verifikasi identitas tandan pada pengamatan awal terhadap 49 tandan, bukan hasil panen atau hitung lapangan; metode verifikasinya tidak diuraikan rinci di teks. Metrik yang dilaporkan adalah keberhasilan pelacakan, bukan galat hitungan total.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan memakai struktur tetap (batang dan pelepah) sebagai jangkar koordinat bersama antarsesi, serta pemasangan tandan dengan kedekatan 3D setelah penyelarasan. Hambatan yang disebut makalah, yaitu tandan berdekatan dan oklusi, juga relevan untuk tandan sawit yang tertutup pelepah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `yoshida2026cross`.

Yoshida dkk. mengusulkan pelacakan tandan anggur lintas hari dengan menyelaraskan rekonstruksi SfM harian melalui titik cabang (segmentasi Mask R-CNN, deskriptor SIFT, transformasi kesamaan Umeyama-RANSAC), lalu memasangkan tandan hasil deteksi CenterNet berdasarkan jarak 3D (ambang 50 mm). Pada 49 tandan di empat pohon selama tiga minggu, 34 tandan (69,39%) terlacak, sedangkan tanpa penyelarasan cabang keberhasilannya 0,00%.

Catatan verifikasi data: Angka keberhasilan pelacakan (69,39%, 34 dari 49) dan ablasi (0,00%) ada pada Tabel 2 serta Seksi 4.2 dan 4.3. Metrik deteksi ada pada Tabel 1 (seksi 4.1). Waktu komputasi ada pada Seksi 4.1. Jumlah titik (sekitar 16 juta dan 5.000) ada pada Seksi 3.2.1. Teks ekstraksi terbaca baik. Tidak dapat diverifikasi dari teks: kultivar, jumlah total citra, cara verifikasi identitas tandan sebagai acuan, dan galat penyelarasan.
