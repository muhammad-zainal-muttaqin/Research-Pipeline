# Simulation and modeling application in agricultural mechanization

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hudzari2012simulation` |
| Judul asli | Simulation and modeling application in agricultural mechanization |
| Penulis | Hudzari, R. M.; Ssomad, M. A. H. A.; Syazili, R.; Fauzan, M. Z. M. |
| Tahun | 2012 |
| Venue | Modelling and Simulation in Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hudzari2012simulation.pdf](../pdf/hudzari2012simulation.pdf)
- DOI resmi: https://doi.org/10.1155/2012/381239

## Gambaran Umum

Hudzari dkk. (2012) mengusulkan cara menduga hari panen tandan buah segar (TBS) kelapa sawit dari satu foto yang diambil dengan kamera digital biasa. Nilai Hue warna kulit buah dihubungkan dengan kadar minyak mesokarp, lalu kadar minyak itu dipetakan ke jumlah hari sebelum panen. Metode ini tidak memerlukan pemetikan sampel buah. Makalah ini diterbitkan di *Modelling and Simulation in Engineering* dan merupakan simulasi berbasis data dari sesi pemotretan di kebun, bukan uji deteksi atau penghitungan buah.

Penentuan waktu panen sawit bergantung pada tingkat kematangan buah. Pengukuran kadar minyak mesokarp (daging buah tempat minyak tersimpan) memerlukan pengeringan dan ekstraksi di laboratorium, sehingga tidak praktis dilakukan di kebun. Khalid dan Abbas (1992) sudah mengukur kelembapan mesokarp dengan sensor *microstrip*, tetapi sensor itu memerlukan pemetikan buah sampel dari pohon. Razali dkk. (2008) memakai model RGB untuk menduga kematangan dari citra luar ruang, tetapi hanya kanal merah yang dipakai karena kanal hijau dan biru dianggap tidak berkorelasi dengan indeks kematangan. Makalah ini menyatakan bahwa Hue, yang merangkum warna keseluruhan permukaan buah, lebih baik daripada kanal merah tunggal.

Gagasan intinya: nilai Hue rata-rata permukaan TBS pada foto berkorelasi dengan kadar minyak mesokarp, dan kadar minyak itu berkorelasi dengan jumlah hari menuju kematangan. Dengan kurva hubungan ini, satu nilai Hue dari satu foto menghasilkan estimasi hari panen. Input berupa foto, output berupa angka hari.

Foto diambil dengan Nikon Coolpix 4500 dalam mode manual, kecepatan rana 1/8 detik, dan eksposur maksimum. Pemotretan dilakukan di bawah tajuk pohon. Lebih dari 50 citra diambil dalam satu sesi. Makalah tidak menjelaskan jumlah tandan per citra atau cara memisahkan tandan yang berdekatan.

Nilai Hue ditentukan dari nilai maksimum kanal R, G, dan B. Hasilnya dibandingkan dengan sistem visi Keyence. Makalah tidak merinci ruang warna yang dipakai untuk konversi atau bagaimana piksel latar (daun, tanah) disingkirkan.

Kadar minyak mesokarp diukur dengan ekstraksi Soxhlet, lalu dihubungkan dengan Hue lewat regresi. Pada grafik yang diberikan, Hue 158 sampai 179 disebut belum matang, 185 sampai 212 kurang matang, dan 224 sampai 255 matang.

Kurva dibuat dengan interpolasi linear dari kadar minyak terhadap jumlah hari sebelum panen. Titik kematangan ditetapkan pada kadar minyak 75 persen terhadap mesokarp kering. Titik awal ditetapkan 65 hari sebelum matang. Contoh yang diberikan: Hue 170 setara kadar minyak 41 persen, dan buah memerlukan 29 hari menuju panen.

Pengujian utama adalah kesesuaian antara Hue, kadar minyak, dan waktu panen pada satu kebun. Makalah melaporkan pemantauan 65 hari sejak tahap belum matang sampai buah dianggap matang, yang ditandai buah lepas berjatuhan di tanah. Kadar minyak diuji ulang dengan ekstraksi untuk setiap titik pemantauan.

Makalah juga membandingkan siklus pematangan dengan literatur. Waktu matang dilaporkan sekitar 22 minggu setelah bunga mekar, sejalan dengan rujukan 20 sampai 22 minggu. Penulis menyatakan bahwa metode mereka lebih maju daripada sensor *microstrip* dan model RGB sebelumnya, tetapi perbandingan itu bersifat naratif. Tidak ada tabel yang membandingkan galat pada data yang sama.

Angka korelasi regresi terbaik antara Hue dan kadar minyak dilaporkan selalu bernilai 1. Nilai sempurna seperti ini jarang terjadi pada data lapangan dan tidak disertai jumlah sampel, interval kepercayaan, atau galat prediksi. Angka ini tidak dapat diverifikasi dari teks.

Kelebihan utama metode ini adalah pengambilan data tanpa pemetikan dan tanpa alat khusus selain kamera biasa. Kurva Hue ke kadar minyak juga memberi satu nilai yang mudah dibaca di kebun.

Dari sisi rekayasa, sejumlah keterbatasan perlu dicatat. Pertama, jumlah tandan, jumlah pohon, dan jumlah sesi tidak disebutkan secara lengkap, sehingga stabilitas kurva tidak dapat dinilai. Kedua, korelasi yang selalu bernilai 1 tidak masuk akal sebagai hasil lapangan dan menunjukkan kemungkinan kesalahan pelaporan atau pemodelan. Ketiga, pemotretan di bawah tajuk membuat pencahayaan bervariasi, dan makalah tidak mengukur pengaruh pencahayaan terhadap nilai Hue. Keempat, satu foto per tandan tidak menangkap sisi tandan yang tertutup pelepah. Secara konseptual, metode ini mengasumsikan warna kulit berkorelasi tetap dengan kadar minyak di seluruh kebun, dan asumsi itu tidak diuji lintas varietas atau lintas musim.
