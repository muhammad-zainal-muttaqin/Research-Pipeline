# Neural network with k-fold cross validation for oil palm fruit ripeness prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shiddiq2024neural` |
| Judul asli | Neural network with k-fold cross validation for oil palm fruit ripeness prediction |
| Penulis | Shiddiq, Minarni; Candra, Feri; Anand, Barri; Rabin, Mohammad Fisal |
| Tahun | 2024 |
| Venue | Telkomnika Telecommunication Computing Electronics and Control |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [shiddiq2024neural.pdf](../pdf/shiddiq2024neural.pdf)
- DOI resmi: https://doi.org/10.12928/telkomnika.v22i1.24845

## Gambaran Umum

Sortir dan penilaian mutu tandan buah segar (TBS) di pabrik masih dilakukan secara manual dan merusak buah, padahal mutu minyak sawit mentah ditentukan oleh kematangan, dengan kandungan minyak tinggi dan asam lemak bebas rendah sebagai sasaran. Penelitian ini bertujuan menguji penggunaan pencitraan hiperspektral dan jaringan saraf tiruan (ANN) dengan validasi silang k-fold untuk memprediksi kematangan TBS bagi mesin pengurut dan penilaian mutu secara daring di area penerimaan pabrik.

Sampel Tenera berasal dari perkebunan sekitar 7 km dari laboratorium dan dikelompokkan oleh pemanen berpengalaman berdasarkan warna dan jumlah buah lepas menjadi fraksi F0–F4; F0 dan F1 ditetapkan sebagai unripe, sedangkan F2, F3, dan F4 sebagai ripe karena F4 masih diterima di area sortir. Sistem pencitraan terdiri atas kamera monokrom NIR Sentech 2,2 MP berukuran sensor 2/3", spektrograf Specim ImSpector V10 untuk rentang 400–1000 nm, sepasang lampu garis halogen Dolan Jenner, konveyor, dan unit kendali; pemindaian memakai skema line scanning dengan MATLAB, di dalam kotak kedap cahaya, jarak lensa ke konveyor 83 cm, dan lampu pada sudut 45° terhadap garis vertikal. Kalibrasi sumbu panjang gelombang memakai tiga laser tampak pada 405, 532, dan 650 nm. Pengambilan dilakukan 23 kali dengan delapan tandan setiap kali, sehingga 184 TBS dipindai dalam 24 jam setelah pemanenan pada kecepatan 250 frame per detik, disertai citra referensi putih dan gelap dan disimpan dalam format .mat. Pemrosesan citra mengubah data 4D menjadi 3D, mengoreksi reflektansi dengan referensi putih dan gelap, menetapkan ROI, lalu merata-ratakan intensitas menjadi 523 titik data spektral yang memuat 544 panjang gelombang. Filter Savitzky-Golay diterapkan dengan panjang jendela 11, polinomial orde 3, dan dt 1/551; pemilihan data menghasilkan 72 titik data. Validasi silang tujuh lipat membagi data menjadi tujuh subset, dengan lipat 3 dan 4 berisi 11 titik (rasio latih 15:85) dan lima lipat lainnya berisi 10 titik (rasio latih 13:87).

Mekanisme prediksi memakai ANN feedforward dengan propagasi balik dan arsitektur 499-10-1 yang penulis nyatakan sebagai 499 masukan, 10 lapis tersembunyi, dan satu keluaran, dengan 100 epoch dan learning rate 0,1, dibangun dalam MATLAB 9,8 dengan antarmuka pengguna. Masukannya adalah spektrum intensitas reflektansi yang telah dihaluskan, dan keluarannya dua status, immature (unripe) atau mature (ripe). Penulis tidak menguji deteksi kotak atau penghitungan tandan; kondisi lain seperti buah busuk, tandan kosong, dan tangkai panjang dinyatakan memerlukan metode sortir lain seperti deteksi objek.

Akurasi diukur dengan confusion matrix yang memuat akurasi, laju kesalahan, recall, dan presisi, dengan nilai 1 untuk ripe dan 0 untuk unripe; model dianggap potensial bila akurasi di atas 75%. Filter SG mengurangi derau spektrum, dengan intensitas lebih tinggi pada 700–900 nm. Lipat 2, 5, dan 7 mencapai akurasi tertinggi 90%, sedangkan lipat 4 mencapai 63,63%, lipat 6 70%, lipat 3 72,72%, dan lipat 1 80%. Rata-rata akurasi tujuh lipat tercantum 79,17% pada Tabel 4, sedangkan abstrak dan simpulan menyebut 79,48%; nilai agregat lain adalah kesalahan klasifikasi 20,83%, recall 45,61%, dan presisi 83,87%. Prediksi lipat 7 memiliki MSE 8,9924e-23.

Penulis menyatakan beberapa batasan. Akurasi rendah pada lipat 3, 4, dan 6 dikaitkan dengan jumlah lipat yang lebih sedikit, sehingga disarankan memakai lebih banyak lipat dengan jumlah pengulangan kecil. Hasil ini sekitar 5% lebih rendah daripada percobaan hiperspektral dan ANN sebelumnya, yang mungkin disebabkan skema push broom dengan kecepatan konveyor dan frame rate yang tidak sepenuhnya cocok, sehingga citra menjadi kabur. Sisi belakang tandan tidak dihitung karena buah tidak subur pada setengah sisi tersebut. Derau citra hiperspektral berasal dari ketidaksejajaran komponen optik, pencahayaan tidak merata, dan derau sensor; penulis juga mengaitkan selisih antara target dan model dengan efek perataan serta citra bernoise. Kondisi TBS selain kematangan memerlukan metode deteksi tersendiri.
