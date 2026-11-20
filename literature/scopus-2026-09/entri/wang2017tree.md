# On-tree mango fruit size estimation using RGB-D images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2017tree` |
| Judul asli | On-tree mango fruit size estimation using RGB-D images |
| Penulis | Wang, Zhenglin; Walsh, Kerry; Verma, Brijesh |
| Tahun | 2017 |
| Venue | Sensors Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | mango |

## Tautan Akses
- PDF: [wang2017tree.pdf](../pdf/wang2017tree.pdf)
- DOI resmi: https://doi.org/10.3390/s17122738

## Gambaran Umum

Penelitian ini mengukur ukuran buah mangga di pohon dari jarak antar baris
menggunakan pencitraan mesin. Pengukuran ukuran buah di lapang berguna untuk
memperkirakan kematangan, distribusi ukuran, keputusan panen, pengadaan
baki pengemas, dan pemasaran. Pencitraan mesin selama ini dipakai untuk
menghitung buah, tetapi pengukuran ukuran juga memerlukan jarak kamera ke
buah. Penulis membandingkan tiga teknologi pengukur jarak berbiaya rendah,
yaitu kamera stereo Zed, pengukur laser genggam Leica DISTO D2a berbasis
Time of Flight, dan kamera RGB-D Kinect V2. Kamera RGB-D direkomendasikan
atas dasar biaya dan kinerja, meski kinerjanya buruk di bawah sinar matahari
langsung.

Datanya adalah buah mangga pada dua tahap kematangan, yaitu sebelum dan
sesudah pengerasan batu, yang dipotret pada malam hari antara pukul 18.30
dan 21.30 dalam dua sesi di lapang. Sejumlah 25 citra kanopi berisi buah
yang terpisah secara visual diukur manual dengan jangka sorong; lima citra
dipilih secara acak untuk penyesuaian parameter dan pelatihan, sisanya untuk
validasi. Dalam percobaan terpisah, ke-136 buah pada satu pohon dipetakan
posisinya dalam tiga dimensi dan ditimbang setelah dipanen. Rerata panjang,
lebar, dan tebal buah adalah 101, 81, dan 73 mm, dengan rentang masing-masing
56–149, 47–123, dan 42–101 mm. Pengukuran berulang oleh operator yang sama
memiliki simpangan baku 1,2 mm.

Mekanisme pengolahan diawali dengan kalibrasi dan pendaftaran citra RGB serta
kedalaman Kinect menggunakan papan checkerboard 8 × 9 berukuran 34 mm dan
alat kalibrasi MATLAB. Deteksi buah memakai pengklasifikasi kaskade berbasis
Histogram of Oriented Gradients dengan ukuran kotak dan sel 6 × 6 piksel
serta ambang penggabungan 8 untuk menekan positif palsu. Potongan citra
kemudian diproses dengan konversi ke CIE L*a*b*, segmentasi Otsu pada kanal
L*, ambang warna pada kanal a* (−25 sampai 25) dan b* (−20 sampai 35), serta
operasi morfologi untuk membuang dan menutup objek kecil. Tangkai buah
dibuang dengan filter garis satu dimensi ber nilai w = 8, kira-kira 14 mm
pada jarak 2 m. Buah utuh dikenali melalui pencocokan elips berdasarkan momen
citra dengan empat kriteria, yaitu luas 1.000–8.000 piksel, rasio luas r >
0,97, eksentrisitas ε < 0,75, dan panjang kotak pembatas yang tidak melebihi
sumbu utama elips lebih dari 4 piksel. Ukuran buah dihitung dengan rumus
lensa tipis f/D = ukuran citra/ukuran nyata, dengan jarak D diambil dari
nilai kedalaman rata-rata pada kotak 2 × 2 piksel di tengah buah; buah
dengan kedalaman kurang dari 0,8 m dikeluarkan.

Hasil perbandingan sensor, dinyatakan sebagai RMSE setelah koreksi bias,
adalah 126,9 mm pada ubin keramik dan 155,6 mm pada buah untuk Zed, 2,0 dan
2,4 mm untuk Leica, serta 8,4 dan 11,0 mm untuk Kinect. Di bawah sinar
matahari langsung, Kinect gagal mengukur jarak di atas 3,5 m; pada rentang
0,6–3,5 m, RMSE-nya berturut-turut 14,6, 10,5, 9,4, dan 8,4 mm pada pukul
14.30, 16.00, 17.30, dan 19.00. Deteksi kaskade menghasilkan 353 objek
dengan presisi 81,1%, sedangkan setelah pencocokan elips tersisa 90 objek,
seluruhnya benar, sehingga presisi mencapai 100% atau 77% dari buah tak
tertutup menurut penilaian manusia. Estimasi ukuran terhadap ukuran manual
mencapai R² 0,96 dan RMSE 4,9 mm untuk panjang serta R² 0,95 dan RMSE 4,3 mm
untuk lebar; bias −0,7 mm dan 0,3 mm masih dalam ketidakpastian acuan 1,2 mm.
Dengan hubungan alometrik Mass = 0,42 × L × W², galat ukuran tersebut
menghasilkan galat massa 45 g pada buah rerata 278 g.

Penulis menyatakan sejumlah batasan. Kamera RGB-D tidak dapat dipakai pada
sinar matahari intens karena pita penguatnya sekitar 850 nm terganggu
cahaya matahari, sehingga sistem dirancang untuk pencitraan malam atau
pencahayaan menyebar. Rentang kerja Kinect hanya 0,5–4,5 m. Resolusi
kedalaman 512 × 424 dan piksel RGB 3,1 µm menyebabkan galat segmen satu
piksel setara 1,76 mm pada jarak 2 m; informasi profil kedalaman tidak
berguna untuk segmentasi karena resolusinya rendah. Metode ini hanya
mendeteksi buah terlu kanopi, rata-rata 4,5 buah per pohon, dan belum diuji
pada kultivar dengan bentuk buah berbeda. RMSE 4,9 mm belum memenuhi kriteria
rancangan 4 mm untuk mengklasifikasikan buah kecil ke ukuran baki yang tepat,
meski cukup untuk memantau kematangan dan penempatan dalam satu toleransi
ukuran baki. Penulis juga menyatakan diperlukan paling sedikit 95 buah untuk
estimasi ukuran rerata pada tingkat kepercayaan 95% dengan galat 4,9 mm.
