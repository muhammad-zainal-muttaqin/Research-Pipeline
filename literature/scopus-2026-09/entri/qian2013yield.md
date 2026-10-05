# Yield estimation model of single tree of Fuji apples based on bilateral image identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qian2013yield` |
| Judul asli | Yield estimation model of single tree of Fuji apples based on bilateral image identification |
| Penulis | Qian, J.; others |
| Tahun | 2013 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [qian2013yield.pdf](../pdf/qian2013yield.pdf)
- DOI resmi: https://doi.org/10.3969/j.issn.1002-6819.2013.11.017

## Gambaran Umum
Makalah ini (Qian dkk., 2013, *Transactions of the Chinese Society of Agricultural Engineering*, ditulis dalam bahasa Mandarin dengan abstrak berbahasa Inggris) membangun model estimasi hasil panen per pohon apel Fuji dari citra kamera digital biasa. Setiap pohon dipotret dari dua sisi, yaitu arah tenggara dan barat laut. Buah matang dikenali dari warna, lalu jumlah dan luas piksel bercak (*patch*) buah yang teridentifikasi dipakai sebagai peubah bebas pada regresi linear terhadap bobot hasil panen per pohon.

Data terdiri atas 40 pohon Fuji di satu kebun di Kota Feicheng, Provinsi Shandong, dengan 80 citra terpilih (satu citra per sisi per pohon). Dua puluh pohon bernomor ganjil dipakai untuk membangun model dan 20 pohon bernomor genap untuk validasi. Peubah terbaik adalah jumlah bercak dari kedua sisi yang dijumlahkan, dengan koefisien determinasi $R^2$ sebesar 0,81 dan NRMSE sebesar 0,11 pada data pemodelan, serta NRMSE sebesar 0,16 pada data validasi.

Makalah ini tergolong metode yang menggabungkan dua pandangan pada satu pohon. Penggabungan dilakukan dengan menjumlahkan hitungan mentah kedua sisi tanpa pencocokan identitas buah, dan penulis mengakui adanya penghitungan ganda.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa harga apel berfluktuasi tajam dalam beberapa tahun terakhir, sehingga estimasi hasil panen penting untuk menstabilkan harga, menjamin pasokan, dan menyesuaikan rencana produksi. Studi terdahulu yang dirujuk sebagian besar memperkirakan hasil panen secara makro dan lintas tahun (model jaringan saraf kelabu, rantai Markov kelabu), atau memakai citra udara dan spektroskopi untuk estimasi per pohon.

Pendekatan berbasis citra digital biasa dinilai murah dan sederhana. Penulis mengutip sistem estimasi hasil jeruk berbasis penglihatan mesin dengan ambang tunggal yang hanya mencapai koefisien korelasi 0,79 antara jumlah jeruk terdeteksi dan hasil panen. Penulis juga menilai bahwa memotret satu arah saja menimbulkan galat besar, karena sebaran buah pada pohon tidak merata. Hal ini mendorong pengambilan citra dari dua sisi.

## Ide Utama
Gagasan utamanya adalah menggunakan citra dari dua arah berlawanan (tenggara dan barat laut) untuk mewakili seluruh buah pada pohon berbentuk dinding (*hedgerow*), kemudian menjumlahkan hitungan bercak kedua sisi sebagai fitur tunggal untuk regresi linear. Penulis membandingkan enam peubah: jumlah bercak per sisi, luas piksel bercak per sisi, dan penjumlahan kedua sisi untuk masing-masing ukuran.

Hitungan bercak bukan hitungan buah unik. Satu buah yang terpisah oleh daun dapat menjadi beberapa bercak, beberapa buah yang bertumpuk dapat menjadi satu bercak, dan buah di bagian tengah pohon dapat tercatat dari kedua sisi. Regresi linear terhadap bobot panen menyerap galat sistematis tersebut secara implisit.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Kebun berlokasi di Desa Shangzhai, Kota Feicheng, Provinsi Shandong, berukuran sekitar 30 m × 80 m (sekitar 0,24 ha) dengan 144 pohon; kultivar utama adalah Fuji dan Gala. Jarak tanam sekitar 3,5 m × 2 m dan kebun didirikan pada 2001. Sebanyak 40 pohon Fuji berbentuk dinding atau mendekati dinding dengan kondisi pertumbuhan dan pengelolaan yang seragam dijadikan objek. Pohon berumur 10 tahun menurut bagian diskusi.

Citra diambil pada 11 dan 12 Oktober 2011 antara pukul 10.00 dan 15.00, saat buah sudah dilepas dari kantong pembungkus dan berwarna baik. Kamera adalah Canon G7 (ditulis "Cannon G7" dalam makalah) dengan panjang fokus tetap. Citra berformat JPG beresolusi 800 × 600. Tiap pohon dipotret dua kali dari setiap arah (160 citra), lalu satu citra terbaik per arah dipilih sehingga terdapat 80 citra. Pemotretan diupayakan mencakup seluruh buah pohon sasaran dan mengecualikan buah pohon sekitarnya.

### 2. Pengenalan buah dan ekstraksi fitur
Karena apel berwarna merah dan kontras terhadap latar, segmentasi memakai fitur warna dengan metode apel matang berbasis ruang warna campuran dari publikasi penulis sebelumnya, disusul filter morfologi. Pemrosesan memakai Matlab V7.0. Jumlah bercak dihitung dengan fungsi `bwlabel`. Luas piksel bercak dihitung sebagai $AreaF = PerF \times 600 \times 800$, dengan $PerF$ persentase bagian bercak terhadap seluruh citra.

### 3. Data acuan hasil panen
Panen dilakukan pada 13–25 Oktober 2011. Pengelola kebun mencatat massa buah tiap pemanenan per pohon, dan hasil per pohon diperoleh dengan menjumlahkannya. Acuan hitungan adalah bobot panen per pohon, bukan hitungan buah.

### 4. Pemodelan
Empat puluh pohon diurutkan menurut hasil panen dari kecil ke besar dan diberi nomor 1–40; nomor ganjil menjadi data pemodelan dan nomor genap data validasi. Rerata hasil panen kedua kelompok adalah 57,90 kg dan 59,87 kg, dengan simpangan baku 15,10 dan 12,27. Model berupa regresi linear sederhana. Evaluasi memakai $R^2$ dan NRMSE (galat kuadrat tengah relatif), dengan $NRMSE = \sqrt{\frac{1}{N}\sum (Y'(i)-Y(i))^2} / \bar{Y}$.

## Eksperimen dan Hasil
Enam model regresi pada 20 pohon pemodelan menghasilkan nilai berikut (Tabel 1 makalah).

| Peubah | Persamaan | $R^2$ | NRMSE |
|---|---|---|---|
| Jumlah bercak, tenggara | Y = 0,4964x + 30,531 | 0,50 | 0,18 |
| Jumlah bercak, barat laut | Y = 0,4618x + 31,835 | 0,37 | 0,21 |
| Jumlah bercak, jumlah dua sisi | Y = 0,4509x + 7,5858 | 0,81 | 0,11 |
| Luas piksel bercak, tenggara | Y = 0,0055x + 30,834 | 0,41 | 0,20 |
| Luas piksel bercak, barat laut | Y = 0,0037x + 43,191 | 0,15 | 0,24 |
| Luas piksel bercak, jumlah dua sisi | Y = 0,0047x + 16,307 | 0,53 | 0,18 |

Jumlah bercak lebih baik daripada luas piksel pada semua perbandingan, dan penjumlahan dua sisi paling baik. Sisi tenggara lebih baik daripada barat laut; penulis menduga penyebabnya adalah pencahayaan searah atau menyamping dari belakang kamera pada sisi tenggara sehingga buah lebih mudah dikenali. Dugaan ini tidak diuji.

Pada validasi dengan 20 pohon genap, model jumlah bercak dua sisi menghasilkan rerata estimasi 60,07 kg dan NRMSE 0,16. Estimasi mengikuti tren hasil panen aktual tetapi dengan fluktuasi yang cukup besar. Sepuluh pohon diestimasi lebih tinggi dan sepuluh lebih rendah daripada hasil aktual. Simpangan terbesar ke atas adalah 14,02 kg (pohon nomor 4) dan ke bawah 17,79 kg (pohon nomor 30). Penulis menyebut estimasi tertinggi pada pohon nomor 40 dan terendah pada pohon nomor 2, dengan hasil panen aktual masing-masing 81,08 kg dan 35,09 kg; kalimat ini ambigu antara nilai estimasi dan nilai aktual.

Penjelasan penulis atas galat: estimasi terlalu tinggi karena satu buah terpecah menjadi beberapa bercak oleh daun atau ranting, serta penghitungan ganda buah yang tampak dari kedua sisi, terutama di bagian tengah pohon. Estimasi terlalu rendah karena buah bertumpuk menyatu menjadi satu bercak, bercak kecil akibat oklusi berat terhapus oleh operasi morfologi, dan masih ada buah tertutup meskipun dua sisi dipakai. Galat rendah-estimasi disebut lebih sering pada pohon berbuah banyak (pohon nomor 34, 36, 38, dan 40).

## Kelebihan dan Keterbatasan
Kelebihan: alat yang dipakai berupa kamera digital biasa; perbandingan enam peubah memperlihatkan kontribusi sisi kedua; terdapat pemisahan data pemodelan dan validasi; makalah menganalisis arah galat secara terbuka.

Keterbatasan yang dinyatakan penulis: pengenalan melemah pada cahaya belakang dan cahaya redup; satu buah terpisah oleh oklusi dapat dihitung sebagai beberapa buah, dan beberapa buah bertumpuk dapat dihitung sebagai satu; model hanya berlaku untuk pohon Fuji berbentuk dinding berumur 10 tahun, sedangkan bentuk pohon lain (spindel, *open center*) memerlukan model sendiri.

Menurut pembacaan ringkasan ini: (1) ukuran sampel kecil (20 pohon untuk pemodelan dan 20 untuk validasi) pada satu kebun dan satu musim; (2) pembagian ganjil-genap berdasarkan urutan hasil panen menjaga distribusi serupa tetapi bukan pemisahan acak atau lintas lokasi; (3) tidak ada pencocokan identitas buah antarsisi, sehingga penghitungan ganda hanya terkoreksi lewat koefisien regresi; (4) bercak bukan hitungan buah dan hitungan per buah tidak dibandingkan dengan hitungan manual; (5) segmentasi berbasis warna hanya cocok untuk buah merah yang kontras dengan latar.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali hanya secara statistik. Dua sisi pohon dipotret, hitungan bercak kedua sisi dijumlahkan, dan penulis mengakui bahwa buah di tengah pohon dapat terhitung dua kali. Tidak ada mekanisme pencocokan identitas, pelacakan, atau rekonstruksi 3D; koreksi dilakukan oleh intersep dan kemiringan regresi linear. Hitungan tidak dilaporkan per kelas, karena hanya buah matang berwarna merah yang dikenali.

Acuan hitungnya adalah bobot panen per pohon (kg) dari catatan pengelola kebun, bukan hitungan buah manual maupun anotasi citra. Untuk pencacahan tandan kelapa sawit multi-sisi, hal yang dapat dipindahkan adalah desain dua sisi berlawanan dengan penjumlahan hitungan dan pelaporan empiris galat penghitungan ganda serta hitungan terlalu rendah akibat oklusi. Makalah ini tidak menyediakan cara memastikan bahwa satu objek dihitung sekali, sehingga tidak menjawab masalah identitas lintas pandang itu sendiri.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `qian2013yield`.

Qian dkk. (2013) membangun model regresi linear untuk memperkirakan hasil panen per pohon apel Fuji dari citra kamera digital yang diambil dari sisi tenggara dan barat laut pada 40 pohon. Jumlah bercak buah yang dikenali dari warna dan dijumlahkan dari kedua sisi memberikan $R^2$ 0,81 dan NRMSE 0,11 pada 20 pohon pemodelan, serta NRMSE 0,16 pada 20 pohon validasi, lebih baik daripada satu sisi atau luas piksel. Penghitungan ganda dan oklusi diakui sebagai sumber galat tanpa mekanisme pencocokan antarsisi.

Catatan verifikasi data: Makalah berbahasa Mandarin (dengan abstrak berbahasa Inggris); entri ini diringkas dari teks Mandarin. Nilai $R^2$ dan NRMSE pemodelan terdapat pada Tabel 1 (seksi 2.1) dan abstrak Mandarin; NRMSE validasi 0,16 dan rerata estimasi 60,07 kg pada seksi 2.2; rerata hasil panen 57,90 dan 59,87 kg serta simpangan baku pada seksi 1.5. Abstrak bahasa Inggris memuat NRMSE 0,43 (pemodelan) dan 0,59 (validasi) yang bertentangan dengan 0,11 dan 0,16 pada teks dan abstrak Mandarin; entri ini memakai nilai teks Mandarin dan nilai Inggris tidak dapat dikonfirmasi dari tabel. Abstrak Inggris juga menyebut pohon nomor 2 sebagai simpangan terbesar 14,02, sedangkan teks utama menyebut pohon nomor 4; teks utama dipakai. Tabel dan angka terbaca baik dari ekstraksi, tetapi gambar 3 dan 4 tidak tersedia sebagai teks. Tidak dilaporkan: nilai $R^2$ pada data validasi, resolusi atau kinerja pengenalan buah (presisi dan *recall*), serta hitungan buah manual.
