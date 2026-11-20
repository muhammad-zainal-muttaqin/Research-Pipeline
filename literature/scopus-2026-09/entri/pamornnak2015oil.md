# Oil content determination scheme of postharvest oil palm for mobile devices

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pamornnak2015oil` |
| Judul asli | Oil content determination scheme of postharvest oil palm for mobile devices |
| Penulis | Pamornnak, Burawich; Limsiroratana, Somchai; Chongcheawchamnan, Mitchai |
| Tahun | 2015 |
| Venue | Biosystems Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [pamornnak2015oil.pdf](../pdf/pamornnak2015oil.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2015.03.010

## Gambaran Umum

Pamornnak dkk. (2015) membuat skema pengukuran kadar minyak pascapanen buah sawit yang berjalan di ponsel. Kamera menangkap buah tunggal dalam kotak berlampu terkontrol. Sistem memakai citra untuk menggolongkan buah ke dalam tiga kelas kematangan dan memperkirakan kadar minyak buah (*oil extraction rate*, OER) dari nilai *hue* dan saturasi di bagian bawah buah. Hasil uji pada 64 buah yang tidak dipakai melatih menunjukkan galat rata-rata OER 2,20 terhadap pengukuran Soxhlet.

Kadar minyak buah sawit ditentukan dengan ekstraksi Soxhlet, yaitu pengujian kimia yang merusak buah dan memakan waktu. Penulis menilai pengukuran itu tidak praktis untuk pemeriksaan di lapangan atau di pabrik. Kematangan buah sawit berkaitan dengan kadar minyak, dan perubahan warna kulit buah mengikuti perubahan kandungan klorofil, karotenoid, dan antosianin selama pematangan (Mortensen 2006 dan Tan dkk. 2010 dikutip penulis). Karena itu warna buah dipakai sebagai petunjuk tidak langsung.

Masalah yang diangkat penulis ada dua. Pertama, citra dari kamera yang berbeda menghasilkan warna yang berbeda untuk objek yang sama. Kedua, hubungan antara warna dan OER pada keseluruhan buah terlalu lebar untuk dimodelkan dengan satu fungsi. Penulis mengusulkan koreksi warna sebelum analisis, lalu mencari bagian buah yang variasi warnanya lebih sempit.

Gagasan intinya ada tiga langkah. Citra dikoreksi agar warnanya mendekati acuan sRGB. Jaringan saraf dua lapis menggolongkan buah menjadi kelas L (30–40%), M (40–50%), dan H (lebih dari 50%) berdasarkan nilai *hue* di permukaan buah. Setelah itu, fungsi polinomial memperkirakan OER dari *hue* dan saturasi di bagian bawah buah, yaitu area di bawah perhiasan (*perianth*) yang menutupi sekitar 35% buah dan terlindung dari cahaya dan hujan.

Penulis membandingkan dua algoritma koreksi. Poly-3 memetakan warna dengan polinomial, sedangkan DDC (*device dependent correction*) memakai profil perangkat yang disimpan sebagai tabel pencarian (LUT). Pada Tabel 1, DDC menurunkan jarak Euclides total dan selisih warna untuk ketiga kamera yang diuji. Pada Tabel 2, kemiringan dan intersep hasil DDC rata-rata 1 dan 0,14, sedangkan Poly-3 rata-rata 0,92 dan 13,40. Penulis memilih DDC karena lebih akurat dan cukup ringan untuk ponsel.

Jaringan saraf dua lapis memakai nilai *hue* dari permukaan buah sebagai masukan. Jumlah neuron tersembunyi diuji dari 15 sampai 40 dengan langkah 5, dan 30 neuron dipilih karena kompleksitasnya paling rendah dengan MSE terkecil. Penulis menguji 64 buah yang tidak ikut dilatih. Teks menyatakan hasil penggolongan benar seluruhnya.

Penulis mula-mula mencoba *hue* dan saturasi seluruh buah. Pada 45 buah, nilai *hue* berkisar 54–89 dan saturasi 0,32–0,81, dengan OER 30–73%. Variasi itu terlalu besar untuk satu fungsi. Rerata *hue* dan saturasi bagian atas (bagian 1–13) dan bagian bawah (bagian 14–20) dibandingkan, dan bagian bawah ternyata lebih sempit. Penulis memilih bagian bawah dan memodelkan OER per kelas dengan fungsi kubik (Persamaan 10). Tabel 4 memuat koefisien tiap kelas.

Pada 64 buah uji, galat rata-rata OER per kelas adalah 1,38 (L), 1,30 (M), dan 2,81 (H), dengan galat keseluruhan 2,20 (Tabel 5). Galat kelas H paling besar, dan kelas ini memiliki rentang OER paling lebar di atas 50%.

Algoritma dibuat dengan OpenCV dan JAMA di platform Android. Dua pemercepat dipakai: instruksi SIMD dan LUT untuk koreksi warna. Pada Tabel 6, rata-rata waktu proses total adalah 395 ms.

Data terdiri atas buah sawit varietas Negrescens Tenera. Penulis memakai 45 buah untuk membangun model dan 64 buah untuk menguji. Pengambilan citra dilakukan di dalam kotak berlampu terkontrol, bukan di kebun. Pembanding OER adalah ekstraksi Soxhlet. Hasil utama yang dilaporkan adalah galat OER 2,20 pada seluruh kelas, penggolongan tanpa kesalahan pada 64 buah uji, dan waktu proses 395 ms di ponsel.

Angka 2,20 adalah galat rata-rata dalam satuan poin persentase OER pada 64 buah. Angka ini belum tentu sebanding dengan hasil kajian lain karena ukuran sampel kecil dan tidak ada ulangan di kondisi lapangan.

Kelebihan kajian ini adalah rantai langkah yang lengkap dan dapat dijalankan di ponsel, dengan pembanding Soxhlet yang sah. Pemilihan bagian bawah buah juga beralasan karena perhiasan melindungi area itu dari lingkungan luar.

Keterbatasannya terlihat dari sisi rekayasa. Pengujian hanya dilakukan di kotak berlampu terkontrol, dan penulis sendiri menyebut koreksi warna di luar ruangan masih perlu dikembangkan. Jumlah sampel kecil (45 untuk model dan 64 untuk uji), dengan satu varietas. Teks tidak melaporkan ulangan, interval kepercayaan, atau pengujian pada kondisi pencahayaan yang berbeda. Galat kelas H (2,81) hampir dua kali galat kelas L dan M, dan penulis tidak membahas penyebabnya. Penggolongan kematangan dan perkiraan OER juga tidak diuji pada pohon atau tandan, sehingga tidak ada bukti tentang cara menghitung buah di kebun.
