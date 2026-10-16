# Estimation of fruit load in australian mango orchards using machine vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `anderson2021estimation` |
| Judul asli | Estimation of fruit load in australian mango orchards using machine vision |
| Penulis | Anderson, Nicholas Todd; Walsh, Kerry Brian; Koirala, Anand; Wang, Zhenglin; Amaral, Marcelo Henrique; Dickinson, Geoff Robert; Sinha, Priyakant; Robson, Andrew James |
| Tahun | 2021 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [anderson2021estimation.pdf](../pdf/anderson2021estimation.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy11091711

## Gambaran Umum
Makalah ini mendokumentasikan kinerja metode penglihatan mesin multipandang (*multi-view*) untuk menaksir jumlah buah mangga (*fruit load*) pada tingkat kebun, dengan acuan hitungan buah di rumah pengemasan (*packhouse*). Sistem terdiri atas kamera dan lampu LED yang dipasang pada kendaraan yang berjalan di antara baris tanaman pada malam hari, detektor MangoYOLO, dan pelacak berbasis filter Kalman yang menambahkan buah ke hitungan hanya bila buah tidak muncul kembali pada bingkai berikutnya.

Data mencakup 37 kebun mangga pada musim 2019 sampai 2020 dan 19 kebun pada musim 2020 sampai 2021 di Australia, dengan beberapa kultivar (Kensington Pride, Calypso, Honey Gold, Keitt, R2E2, dan NMBP1243), ditambah uji sistem tanam di Walkamin Research Facility. Pengulangan pada malam hari memberi selisih hitungan 0,1% (12.902 dan 13.008 buah). Galat persentase absolut (*absolute percentage error*, APE) hitungan multipandang mentah adalah 10% atau kurang pada 15 dari 20 kebun. Rerata APE pada seluruh 20 kebun adalah 11% menurut teks.

Kinerja bergantung pada arsitektur tajuk. Galat persentase rerata pada sistem pagar (*hedge*), pemimpin tunggal (*single leader*), dan konvensional masing-masing 3,4, 5,0, dan 8,2%, sedangkan pada sistem berpenyangga (*trellis*) buah terhitung berlebih dengan galat rerata 25,2%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengelola kebun mangga Australia membutuhkan taksiran dalam rentang ±10% dari hasil panen aktual untuk perencanaan sumber daya panen dan pemasaran, mengingat umur simpan buah yang pendek. Praktik yang berlaku adalah ekstrapolasi dari hitungan manual pada sampel pohon, yang padat karya sehingga jumlah pohon sampel cenderung ditekan. Penelitian terdahulu belum konsisten memenuhi galat 10% terhadap hitungan di rumah pengemasan.

Dua cara menaikkan hitungan per citra menjadi hitungan per pohon dibedakan. Pada metode dua pandang (*dual-view*), jumlah deteksi pada dua citra per pohon, satu dari tiap sisi antarbaris, dikoreksi dengan faktor buah tertutup (*occlusion factor*) dari hitungan manual pada sampel pohon. Pada metode multipandang, video direkam dari kamera yang melewati antarbaris, buah dilacak antarbingkai, dan hitungan bertambah hanya bila buah tidak muncul pada posisi prediksi selama beberapa bingkai. Penulis mengikuti rekomendasi tinjauan sebelumnya untuk melaporkan estimasi pada tingkat kebun beserta faktor yang memengaruhi kinerja (cahaya, orientasi kamera, arsitektur tajuk).

## Ide Utama
Gagasan makalah ini adalah menguji metode multipandang pada skala kebun dan lintas arsitektur tajuk, kultivar, dan musim, serta membandingkannya dengan estimasi manual (FARM dan CAL) dan koreksi buah tertutup (MV-CAL). Satu pertanyaan sentral adalah apakah pelacakan lintas bingkai membuat faktor koreksi buah tertutup tidak diperlukan. Penulis juga memeriksa dua sumber galat multipandang: buah yang tidak terlihat karena tertutup daun, dan buah yang terhitung dua kali karena terlihat dari kedua sisi tajuk.

## Cara Kerja Langkah demi Langkah

### 1. Kebun dan acuan hitungan
Sebuah kebun didefinisikan menurut area dengan praktik pengelolaan seragam, biasanya sekitar 1.000 pohon. Acuan hitungan buah diambil dari sistem data jalur pengemasan (jumlah nampan dan buah per nampan untuk buah terkirim, ditambah bobot buah afkir dibagi bobot rerata buah), atau dari bobot dan bobot rerata buah bila hanya bobot yang tersedia. Penulis mencatat bahwa data rumah pengemasan dapat menyimpang dari jumlah buah di lapangan (buah tertinggal di pohon atau tanah, pencampuran lot, kesalahan taksiran bobot rerata), dan beberapa kebun dikeluarkan karena selisihnya besar. Uji sistem tanam Walkamin memuat empat sistem pelatihan tajuk (konvensional, pagar, pemimpin tunggal, berpenyangga), tiga kultivar, dan tiga kerapatan tanam (208, 417, dan 1.250 pohon per hektare), dengan hitungan panen per pohon.

### 2. Estimasi manual
FARM adalah taksiran pengelola kebun dari hitungan manual sampel pohon sepanjang satu transek; praktik terbaiknya adalah 25 pohon oleh dua orang (sekitar 50 pohon, kira-kira 5% pohon). CAL adalah hitungan manual 18 pohon kalibrasi per kebun, dipilih secara acak terstrata menurut tiga kelas NDVI (rendah, sedang, tinggi; enam pohon tiap kelas) dari citra satelit WorldView-3, lalu dikalikan jumlah pohon kebun. Hitungan dilakukan setelah tahap pengerasan biji (sekitar enam minggu sebelum panen).

### 3. Sistem penglihatan mesin
Rangka pada kendaraan membawa dua panel LED 500 W, dua kamera RGB Basler acA2440 5 megapiksel (lensa Kowa 5 mm) menghadap kedua sisi baris, perangkat perekam, dan penerima GNSS. Kendaraan melaju 5 sampai 7 km per jam, dengan waktu pencitraan sekitar 7 menit per hektare. Jarak kamera ke tajuk umumnya 2 m dan video direkam pada 10 bingkai per detik. MangoYOLO mendeteksi buah pada tiap bingkai, filter Kalman melacak buah antarbingkai, dan buah ditambahkan ke hitungan bila tidak muncul lagi pada tujuh bingkai berikutnya. Ambang ukuran buah 12×12 piksel dipakai untuk mengurangi penghitungan ganda buah yang tampak dari sisi tajuk seberang, karena buah yang jauh tampak lebih kecil dan dikeluarkan. Pada metode dua pandang, hitungan MangoYOLO pada dua citra per pohon diregresikan terhadap hitungan manual 18 pohon untuk mendapatkan faktor oklusi tiap kebun (MV-CAL).

### 4. Latihan eksperimen
Penulis menguji (i) pengulangan dan waktu pengambilan hari, (ii) pengaruh arsitektur tajuk, (iii) pengurangan jumlah baris yang dicitrakan, (iv) pengaruh periode pembungaan yang panjang, dan (v) perbandingan empat metode estimasi pada sekitar 20 kebun per musim. Galat persentase (PE) dihitung terhadap jumlah di rumah pengemasan, dan APE memakai selisih absolut. Perbedaan antar-metode diuji dengan *Least Significant Difference* dan penyesuaian Bonferroni pada paket agricolae di R.

## Eksperimen dan Hasil
Pengulangan dan waktu hari. Dua baris kebun 30 dicitrakan dua kali pada malam yang sama dengan hitungan 12.902 dan 13.008 buah (selisih 106 buah, 0,1%). Pada kebun 28 yang dicitrakan sepanjang hari, hitungan pada pukul 08.00, 10.00, 12.00, 15.00, 16.00, 18.00, 20.00, dan 21.30 masing-masing 37, 49, 47, 54, 53, 48, 98, dan 102% dari hitungan pukul 21.00 (44.419 buah). Penulis menyimpulkan bahwa sistem terbatas untuk penggunaan malam hari, karena detektor dilatih pada citra malam beriluminasi LED dan cahaya matahari menghasilkan rentang dinamis tinggi serta paparan berlebih.

Arsitektur tajuk. Sistem berpenyangga menyebabkan hitungan berlebih karena buah terlihat dari kedua sisi tanpa pembeda ukuran. Pada kultivar NMBP1243 berkerapatan tinggi, PE adalah 32% pada sistem pagar dan 47% pada sistem berpenyangga. Kultivar Keitt, yang tajuknya relatif terbuka, memberi hasil terbaik, diikuti Calypso dan NMBP1243. Metode multipandang direkomendasikan untuk tajuk konvensional, pagar, dan pemimpin tunggal, tetapi tidak untuk tajuk berpenyangga.

Pengurangan baris. Pada lima kebun, pengambilan sampel setiap baris kedua sampai kelima tidak menghasilkan taksiran di luar ±10% dari taksiran seluruh kebun, dan pengambilan setiap baris ketiga direkomendasikan sebagai kompromi usaha dan informasi spasial. Pada kebun 23, galat melampaui ±10% mulai pengambilan setiap baris keenam atau lebih jarang.

Waktu tanam. Jumlah buah terdeteksi bertambah sesuai ukuran buah; pada kebun 28 musim 2020 sampai 2021 hitungan multipandang mencapai plateau lalu naik 29% dari total akhir, dan hitungan akhir adalah 106% dari hitungan rumah pengemasan.

Perbandingan metode 2019 sampai 2020 (Tabel 2, sembilan kebun yang memiliki hasil semua metode):

| Metode | APE rerata (%) | SD (%) | R² terhadap rumah pengemasan |
|---|---|---|---|
| FARM | 25,7 (abstrak: 26) | 11,3 | 0,929 |
| CAL | 12,6 (abstrak: 13) | 8,2 | 0,988 |
| MV-Raw | 11,1 (abstrak: 11) | 11,4 | 0,984 |
| MV-CAL | 16,9 (abstrak: 17) | 9,7 | 0,972 |

Untuk 20 kebun, APE MV-Raw adalah 11% (R² = 0,98, kemiringan 0,74, p < 0,001, Gambar 6). MV-Raw berbeda nyata dari FARM tetapi tidak dari CAL. Koreksi buah tertutup tidak memperbaiki taksiran pada 16 dari 20 kebun. Model *random forest* atas atribut kebun hanya menjelaskan 39% varians rasio hitungan multipandang terhadap hitungan rumah pengemasan (R²cv = 0,39, RMSECV = 0,09), dengan umur pohon sebagai prediktor terpenting.

Musim 2020 sampai 2021. APE rerata MV-Raw, MV-CAL, CAL, dan FARM adalah 17, 23, 22, dan 27% pada seluruh kebun. Pada enam kebun dengan hasil semua metode, tidak ada perbedaan nyata (APE rerata 23,5, 15,5, 16,8, dan 26,2% untuk MV-Raw, MV-CAL, CAL, dan FARM). Hitungan multipandang cenderung di bawah hitungan rumah pengemasan akibat pembungaan yang panjang; untuk 20 kebun pada satu pertanian, R² = 0,97 dengan kemiringan 0,62.

Penggunaan lain. Waktu berkendara sekitar 21 menit untuk kebun 3 hektare berisi 1.000 pohon, dibandingkan sekitar 3 jam untuk hitungan manual 18 pohon. Data hitungan per interval jarak tanam (umumnya 3 m) dipakai untuk membuat distribusi frekuensi hitungan per pohon dan peta panas (*heat map*) beban buah, antara lain untuk menafsirkan kerusakan akibat embun beku dan memilih area panen awal.

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: pelaporan pada tingkat kebun dengan acuan jumlah buah di rumah pengemasan pada banyak kebun dan dua musim; pengulangan malam hari yang tinggi; metode multipandang mentah tidak lebih buruk daripada hitungan manual terstrata dan lebih baik daripada taksiran pengelola kebun; waktu pencitraan jauh lebih singkat; dan keluaran spasial untuk pengelolaan.

Keterbatasan yang dinyatakan penulis: sistem hanya dapat dipakai pada malam hari dan pada tajuk terbuka; sistem berpenyangga menghasilkan hitungan berlebih; faktor koreksi buah tertutup dari pohon kalibrasi tidak mewakili seluruh kebun; periode pembungaan yang panjang memerlukan pencitraan berulang; dan data rumah pengemasan memiliki sumber galat sendiri (buah tertinggal, pencampuran lot, kesalahan bobot rerata), sehingga acuan itu perlu diperiksa. Penulis juga menyebut bahwa galat hitungan manual pada pohon merambat ke semua metode yang memakai hitungan manual.

Menurut pembacaan ringkasan ini, ada beberapa catatan tambahan. Angka SD pada abstrak (11, 8, 11, dan 9%) berbeda dari SD pada bagian hasil (4, 11, 8, dan 11%) dan dari Tabel 2 (11,3, 8,2, 11,4, dan 9,7%); ketidakkonsistenan ini tidak dijelaskan. Keunggulan MV-Raw atas CAL tidak signifikan secara statistik, dan pada musim kedua perbedaan antar-metode tidak signifikan. Penghitungan ganda lintas sisi dikendalikan dengan ambang ukuran buah (12×12 piksel), yang merupakan penyaring heuristik, bukan pencocokan identitas buah antar-sisi, dan makalah sendiri menunjukkan bahwa penyaring ini gagal pada tajuk berpenyangga.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan dua mekanisme. Di dalam satu sisi baris, pelacakan Kalman antarbingkai video (10 bingkai per detik) memastikan buah dihitung satu kali. Antara dua sisi tajuk yang dicitrakan oleh dua kamera yang berhadapan, penghitungan ganda hanya dibatasi dengan ambang ukuran buah 12×12 piksel yang membuang buah jauh. Tidak ada pencocokan buah yang sama antar-sisi. Hitungan tidak dilaporkan per kelas (satu kelas, mangga). Acuan hitungnya adalah jumlah buah di rumah pengemasan (hasil panen) pada tingkat kebun, serta hasil panen per pohon pada uji Walkamin; hitungan manual pada pohon dipakai sebagai pembanding metode.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah bukti bahwa penyaring heuristik berbasis ukuran kurang andal saat tajuk memungkinkan buah yang sama terlihat dari dua sisi (galat 25,2% pada sistem berpenyangga), penggunaan hitungan panen sebagai acuan dengan kewaspadaan terhadap galatnya, serta praktik pelaporan pengulangan dan galat per kebun. Koreksi oklusi dari sampel pohon kecil terbukti tidak mewakili kebun, yang relevan bila pencacahan sawit memakai faktor koreksi sampel.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `anderson2021estimation`.

Anderson dkk. menilai metode penglihatan mesin multipandang bermalam hari untuk menaksir jumlah buah mangga pada tingkat kebun terhadap hitungan di rumah pengemasan. Pada 20 kebun musim 2019 sampai 2020, APE hitungan mentah adalah 11%, dan 10% atau kurang pada 15 kebun. Galat persentase rerata adalah 3,4, 5,0, dan 8,2% pada tajuk pagar, pemimpin tunggal, dan konvensional, tetapi 25,2% pada tajuk berpenyangga karena buah terhitung dua kali dari kedua sisi. Koreksi buah tertutup dari pohon kalibrasi tidak memperbaiki taksiran.

Catatan verifikasi data: Angka APE rerata dan SD sembilan kebun bersumber dari Tabel 2 dan seksi 3.2.1; angka SD pada abstrak, seksi 3.2.1, dan Tabel 2 saling berbeda dan dilaporkan di atas apa adanya. Kolom per kebun pada Tabel 2 tidak terbaca sempurna pada teks ekstraksi (nilai yang kosong tidak dapat dipasangkan dengan kebunnya), sehingga angka per kebun tidak dikutip. Angka per sistem tajuk (3,4, 5,0, 8,2, dan 25,2%) bersumber dari abstrak dan kesimpulan, dan Gambar 3 tidak terbaca. Hasil kerja pengurangan baris bersumber dari Tabel 1 (tabel terbaca sebagian). Jumlah citra dan bingkai tidak dilaporkan. Presisi deteksi MangoYOLO tidak dilaporkan pada makalah ini karena dirujuk dari makalah lain.
