# Estimation of apple orchard yield using night time imaging

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `linker2015estimation` |
| Judul asli | Estimation of apple orchard yield using night time imaging |
| Penulis | Linker, R.; Kelman, E.; Cohen, O. |
| Tahun | 2015 |
| Venue | Precision Agriculture 2015 Papers Presented at the 10th European Conference on Precision Agriculture Ecpa 2015 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [linker2015estimation.pdf](../pdf/linker2015estimation.pdf)
- DOI resmi: https://doi.org/10.3920/978-90-8686-814-8_66

## Gambaran Umum

Estimasi hasil di kebun masih mengandalkan pemeriksaan visual sebagian pohon oleh petani, yang memakan waktu dan rawan galat. Otomatisasi sulit karena tajuk pohon tidak teratur dan berantakan, buah memiliki ciri visual yang lemah serta warna yang mirip daun, dan pencahayaan siang hari tidak merata. Penelitian sebelumnya melaporkan hubungan linear yang kuat antara jumlah objek yang terdeteksi pada citra malam hari dan jumlah apel hasil inspeksi visual, tetapi belum menguji hubungan tersebut terhadap hasil panen aktual per pohon. Penelitian ini menerapkan dua metode deteksi pada lebih dari 250 citra dari 42 pohon dan menyelidiki kesesuaian masing-masing untuk estimasi hasil.

Data dikumpulkan pada 17 Juli 2014 di Matityahu Research Station di Israel Utara dari 42 pohon apel Golden Delicious. Sistem pencitraan terdiri atas tiga kamera Canon PowerShot G7 beresolusi 3648 × 2736 piksel yang dipasang pada tiang vertikal pada ketinggian 110, 180, dan 240 cm dari tanah. Dua tiang tambahan ditempatkan 60 cm dari tiang kamera dan membawa lampu LED pada ketinggian 130 dan 250 cm. Seluruh rakitan dipasang pada trailer yang ditarik di tengah baris pohon. Setiap pohon difoto dari dua sisi sehingga menghasilkan enam citra per pohon atau 252 citra secara keseluruhan. Pohon dipanen satu per satu pada akhir musim sebagai acuan hasil aktual, dan jumlah apel yang terlihat pada setiap citra juga dihitung secara visual.

Penelitian membandingkan dua pendekatan. Pendekatan pertama menganalisis warna dan tekstur melalui empat tahap: klasifikasi piksel, deteksi gumpalan piksel terhubung dan perluasannya ke piksel tetangga yang serupa, pemecahan kontur gumpalan menjadi busur, lalu pengelompokan busur menjadi objek dan perbandingan dengan model lingkaran. Kalibrasi memakai 12 citra, empat pada setiap ketinggian; sekitar setengah apel ditandai manual dan sisanya ditutup agar classifier dilatih pada region apel dan bukan apel. Parameter yang diubah hanya radius minimum 30 piksel, radius harapan 60 piksel, dan radius maksimum 150 piksel. Pendekatan kedua tidak memakai warna dan memanfaatkan sebaran cahaya di sekitar sorotan terang yang muncul pada apel di bawah iluminasi buatan. Karena apel berbentuk bola, piksel dengan intensitas di atas ambang membentuk lingkaran atau bagian lingkaran. Prosesnya mencakup pencarian maksimum lokal intensitas cahaya dan pengambilan sub-citra, pembentukan region piksel terhubung pada ambang intensitas yang menurun, serta analisis sifat geometri rentangan region tersebut. Parameter dari data tahun 2013 dipakai tanpa perubahan. Jumlah objek dari enam citra sebuah pohon dijumlahkan menjadi hitungan pohon; 14 pohon dipilih secara acak untuk menyusun hubungan antara hitungan pohon dan hasil panen aktual, lalu hubungan itu diterapkan pada pohon sisanya. Proses kalibrasi diulang sepuluh kali dengan subset pohon yang berbeda.

Untuk deteksi apel, hitungan visual seluruh citra adalah 18.242 buah, terdiri atas 4.218 pada citra bawah, 6.551 pada citra tengah, dan 7.473 pada citra atas. Pendekatan pertama mengestimasi 17.191 buah dengan rasio estimasi terhadap hitungan visual 0,94, sedangkan pendekatan kedua mengestimasi 18.663 buah dengan rasio 1,02; kedua pendekatan berada dalam kisaran 6% dari hitungan visual. Hasil terburuk terjadi pada citra kamera atas untuk pendekatan pertama karena pencahayaan yang buruk membuat banyak apel terlalu gelap bagi classifier warna. Pada estimasi hasil, jumlah objek dari enam citra hanya sekitar sepertiga hasil aktual pohon, sehingga diperlukan hubungan kalibrasi. Galat pada satu pohon terkadang mencapai sekitar 300 apel, tetapi estimasi hasil keseluruhan tetap berada dalam 10% dari hasil aktual 21.047 apel. Dengan pendekatan pertama, galat pada pohon validasi berkisar dari −10,49% hingga +9,37% dan galat keseluruhan dari −7,34% hingga +5,73%; model A1 memberi galat 7,59% pada pohon validasi dan 5,14% pada seluruh pohon. Dengan pendekatan kedua, galat validasi berkisar dari −4,69% hingga +12,51% dan galat keseluruhan dari −3,10% hingga +8,33%; model B1 memberi galat 9,98% dan 6,55%. Galat melebihi 10% hanya terjadi sekali pada masing-masing pendekatan. Acuan hitung adalah inspeksi visual untuk jumlah apel dalam citra dan timbangan hasil panen per pohon untuk estimasi hasil, dengan metrik rasio dan persentase galat. Kalibrasi deteksi memakai 12 citra, sedangkan kalibrasi hasil memakai 14 pohon dengan 28 pohon sisanya sebagai validasi yang diulang sepuluh kali.

Penulis menyatakan pencitraan malam hari menjanjikan untuk estimasi hasil, paling tidak pada skala baris. Keduanya memerlukan kurang dari 15 pohon untuk kalibrasi, dan penulis membayangkan sistem yang dapat mengkalibrasi sendiri dengan meminta petani menghitung buah pada 15–20 pohon. Pendekatan kedua memiliki keunggulan karena tidak memakai informasi warna sehingga tidak memerlukan classifier khusus untuk setiap kondisi akuisisi dan lebih tahan terhadap perubahan pencahayaan maupun jenis kamera; pendekatan pertama memerlukan pelabelan region apel yang teliti dan memakan waktu. Penulis juga menyatakan hasil ini perlu dikonfirmasi pada himpunan data yang lebih besar.

