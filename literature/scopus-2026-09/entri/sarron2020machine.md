# Is machine learning efficient for mango yield estimation when used under heterogeneous field conditions?

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sarron2020machine` |
| Judul asli | Is machine learning efficient for mango yield estimation when used under heterogeneous field conditions? |
| Penulis | Sarron, J.; San\'e, C.A.B.; Borianne, P.; Mal\'ezieux, E.; Nordey, T.; Normand, F.; Diatta, P.; Niang, Y.; Faye, E. |
| Tahun | 2020 |
| Venue | Acta Horticulturae |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [sarron2020machine.pdf](../pdf/sarron2020machine.pdf)
- DOI resmi: https://doi.org/10.17660/actahortic.2020.1279.30

## Gambaran Umum

Penulis menyebut bahwa kajian pencacahan buah dengan pembelajaran mesin umumnya dilakukan pada kebun seragam, sehingga ketahanannya pada kondisi lapangan yang beragam belum diuji. Tujuannya adalah mengembangkan metode deteksi buah mangga matang dari citra RGB dan mengujinya pada kondisi homogen dan heterogen di Senegal untuk menaksir jumlah buah per pohon.

Citra diambil dengan kamera Sony Nex-7 (4000x6000 piksel) pada dua sisi berlawanan setiap pohon, pada langit cerah pukul 10.00 sampai 15.00. Set 1 berisi 50 citra dari 25 pohon 'Kent' di satu kebun komersial. Set 2 berisi 128 citra dari 64 pohon (22 'Kent', 22 'Keitt', 20 'Bouchodiékhal') di 30 kebun, dengan jarak kamera 5, 7, 10, atau 15 m. Delapan citra Set 1 dan 24 citra Set 2 dipakai melatih. Piksel buah dan bukan buah dipilih manual. Tiga pakar mangga melabeli semua buah matang pada citra validasi dengan kotak pembatas.

Metode memakai klasifikasi *k-nearest neighbours* (KNN), yaitu penentuan kelas piksel dari kelas k piksel latih terdekat dalam ruang fitur. Fiturnya adalah kanal R, G, B, kanal Cr dari ruang warna YCbCr, indeks VARI, dan varians tekstur dengan tapis 3x3. Hasil biner dibersihkan, lalu gumpalan piksel disaring menurut ukuran dan indeks bentuk (*shape.index* di bawah 2,5, rasio keliling terhadap luas di atas 0,05, RCC di bawah 0,60). Ambang diatur manual. Hitungan pohon adalah jumlah deteksi dari kedua citra pohon, lalu dikalibrasi dengan regresi linear per kultivar, dengan intersep dipaksa nol.

Pada Set 1 presisi 0,85, *recall* 0,64, dan F1 0,73. Pada Set 2 presisi 0,70, *recall* 0,36, dan F1 0,48. Teks membahas nilai 0,43 pada bagian diskusi, yang tidak konsisten dengan 0,48. F1 per kultivar 0,53 (Kent), 0,47 (Keitt), dan 0,28 (Bouchodiékhal). Regresi hitungan otomatis terhadap hitungan lapangan memberi R2 0,92, 0,93, dan 0,90. Pada 52 pohon validasi, RMSE 187 buah dan RMSE relatif 14%.

Keterbatasan yang dapat diperiksa: hitungan dari dua sisi dijumlahkan tanpa pencocokan buah yang sama antarcitra. Buah dalam tajuk tidak terlihat sehingga dikoreksi hanya lewat kemiringan regresi per kultivar. Ambang bentuk diatur manual. Buah bergerombol dihitung sebagai satu. Teks menyebut 104 citra validasi pada Set 2 dan 104 pohon berhitungan lapangan, padahal Set 2 hanya 64 pohon, sehingga jumlah ini tidak konsisten. Hitungan acuan lapangan berkisar 7 sampai 650 buah per pohon.
