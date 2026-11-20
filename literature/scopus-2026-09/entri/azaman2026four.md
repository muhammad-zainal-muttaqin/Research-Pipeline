# Four-Channel CIEL*a*b*-Infrared Image Representation for CNN-Based Oil Palm Fresh Fruit Bunch Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `azaman2026four` |
| Judul asli | Four-Channel CIEL*a*b*-Infrared Image Representation for CNN-Based Oil Palm Fresh Fruit Bunch Ripeness Classification |
| Penulis | Azaman, Mohd Ikmal Hafizi; Ng, Kuan-Huei; Tan, Chin-Peng; Udos, Waldo; Khalid, Mohd Ramdhan; Nor Azhar, Nur Saiful Azmi; Mohamed, Aminulrashid; Bakri, Mohd Azwan Mohd; Lim, Kok-Sing |
| Tahun | 2026 |
| Venue | Electronics Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [azaman2026four.pdf](../pdf/azaman2026four.pdf)
- DOI resmi: https://doi.org/10.3390/electronics15173777

## Gambaran Umum

Penelitian ini mengevaluasi pengaruh representasi citra masukan terhadap klasifikasi kematangan tandan buah segar (TBS) sawit berbasis jaringan saraf konvolusional (CNN). Klasifikasi kematangan menentukan angka ekstraksi minyak, mutu minyak, kandungan asam lemak bebas, dan efisiensi pabrik. Masalah utama adalah citra RGB memiliki informasi warna yang terbatas pada buah berwarna gelap dan daerah tandan yang teduh, sehingga fitur kematangan sulit dibedakan. Empat model dengan arsitektur CNN identik dibandingkan menggunakan masukan RGB, RGB + inframerah (IR), CIEL*a*b*, dan CIEL*a*b* + IR, agar perbedaan hasil dapat dikaitkan hanya dengan representasi masukan. Representasi empat kanal yang diusulkan terdiri atas L*, a*, b*, dan satu kanal IR pada rentang 700–1100 nm.

Datanya adalah 279 pasangan citra RGB-IR yang terdiri atas 50 overripe, 65 ripe, 84 underripe, dan 80 unripe, diperoleh dari satu perkebunan. Kelas kematangan ditentukan secara visual oleh dua grader berpengalaman dari Malaysian Palm Oil Board berdasarkan warna buah, keterlepasan buah, tampilan tandan, dan warna mesokarp. Akuisisi memakai dua kamera CMOS sinkron beresolusi asli 1280 × 1024 piksel, yaitu Hikrobot MV-CU013-A0GC untuk RGB dan MV-CU013-A0GM monokrom dengan filter pita 700–1100 nm untuk IR. Kedua kamera dipasang berdampingan dengan jarak dasar sekitar 8 cm, pada jarak 3 m dari TBS, menghasilkan sudut pandang sekitar 11,4° dan panjang fokus sekitar 32 mm untuk TBS berukuran sekitar 45 × 36 cm. Pendaftaran piksel manual dilakukan untuk menyelaraskan kanal IR dengan citra RGB.

Mekanismenya adalah klasifikasi per citra TBS, bukan pelokalan atau penghitungan buah. Fusi dilakukan lebih awal pada lapis masukan dengan menggabungkan tensor warna tiga kanal dan satu kanal IR menjadi tensor 4 × 256 × 256. Model RipenessCNN memiliki tiga blok konvolusi, masing-masing berisi konvolusi 3 × 3, normalisasi batch, ReLU, dan max-pooling 2 × 2, dengan jumlah kanal 32, 64, dan 128; fitur dirangkum dengan adaptive global average pooling menjadi vektor 128, lalu masuk ke lapis fully connected 64 unit dengan dropout 0,5 dan lapis keluaran empat unit. Pelatihan memakai Adam dengan laju 0,001, hingga 100 epoch, ukuran mini-batch 64, categorical cross-entropy, serta early stopping dengan patience 15. Data dibagi secara stratifikasial 80:20 untuk latih dan uji, dengan augmentasi pembalikan horizontal, pembalikan vertikal, dan rotasi ±15°. Penilaian diulang pada 10 pembagian acak; dukungan kelas uji adalah 10, 13, 17, dan 16 untuk overripe, ripe, underripe, dan unripe.

Hasil weighted-average presisi, recall, dan F1-score berturut-turut adalah 0,79/0,76/0,76 untuk RGB, 0,82/0,80/0,80 untuk RGB + IR, 0,79/0,77/0,76 untuk CIEL*a*b*, dan 0,84/0,81/0,81 untuk CIEL*a*b* + IR sebagai model terbaik dengan simpangan baku terendah, yaitu ±0,02 pada ketiga metrik. Pada model terbaik, nilai per kelas untuk overripe, ripe, underripe, dan unripe berturut-turut adalah presisi 0,95/0,91/0,66/0,89, recall 0,95/0,78/0,83/0,72, dan F1 0,95/0,84/0,74/0,79. Matriks konfusi menunjukkan overripe yang salah diprediksi sebagai ripe turun dari 28% pada RGB dan 23% pada CIEL*a*b* menjadi akurasi 92% pada RGB + IR dan 95% pada CIEL*a*b* + IR; unripe yang salah diprediksi sebagai underripe turun dari 35,62% menjadi 28,12%, sehingga akurasi unripe naik dari 64,38% menjadi 71,88%. Uji t berpasangan dua arah pada 10 pembagian menunjukkan perbaikan presisi signifikan sebesar +0,0420 ± 0,0518 (t(9) = 2,5634; p = 0,0305). Waktu latih rata-rata CIEL*a*b* + IR adalah 35,3 ± 6,3 menit, lebih singkat 33,1% daripada RGB sebesar 52,8 ± 13,7 menit. Peta aktivasi Grad-CAM menunjukkan model lebih fokus pada wilayah buah, dengan aktivasi paling jelas pada model CIEL*a*b* + IR.

Batasan yang dinyatakan penulis mencakup ukuran data sebesar 279 pasangan citra dari satu lokasi, sehingga diperlukan data lebih besar yang mencakup kultivar, lokasi panen, dan musim berbeda. Pengujian memakai satu TBS statis dengan latar yang relatif terkendali di bawah cahaya matahari sore; kondisi lapangan nyata melibatkan banyak objek, bayangan kanopi dinamis, silau, dan oklusi buah yang parah. Sistem dua kamera berdampingan memerlukan kalibrasi manual dan pengambilan statis untuk menjaga keselarasan piksel, sehingga penerapan pada perangkat genggam atau mesin panen memerlukan sensor multispektral ringkas, pemisah berkas koaksial, atau pendaftaran citra otomatis. Kelas underripe tetap paling sulit karena sifatnya yang transisional dan heterogen serta memberi positif palsu terbanyak. Data tidak tersedia untuk umum karena menjadi milik Malaysian Palm Oil Board.
