# Apple (Malus domestica) and pear (Pyrus communis) yield prediction after tree image analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `del2023apple` |
| Judul asli | Apple (Malus domestica) and pear (Pyrus communis) yield prediction after tree image analysis |
| Penulis | Del Brio, Dolores; Tassile, Valentin; Bramardi, Sergio Jorge; Fern\'andez, Dar\'\io Eduardo; Reeb, Pablo Daniel |
| Tahun | 2023 |
| Venue | Revista De La Facultad De Ciencias Agrarias |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, pear |

## Tautan Akses
- PDF: [del2023apple.pdf](../pdf/del2023apple.pdf)
- DOI resmi: https://doi.org/10.48162/rev.39.104

## Gambaran Umum

Kajian ini bertujuan memanfaatkan analisis citra untuk meramalkan produksi apel dan pir. Latar belakangnya adalah prakiraan hasil memerlukan jumlah buah per pohon dan ukuran rata-rata buah, yang selama ini dihitung manual dan memakan banyak waktu serta tenaga. Penulis merumuskan dua tujuan: mengevaluasi model pembelajaran mendalam untuk mendeteksi dan menghitung buah apel dan pir, serta mengukur ukuran buah dari citra.

Tanaman yang digunakan adalah apel kultivar 'Red Chief' pada batang bawah MM111 dan pir kultivar 'Williams Bon Chretien' pada batang bawah bibit, di stasiun percobaan INTA, Allen, Argentina. Kedua kebun dibentuk sebagai espalier. Pengambilan data berlangsung selama empat musim pada 72 pohon apel dan 60 pohon pir per musim. Citra diambil pada siang hari antara pukul 10.00 sampai 13.00 dan pada malam hari dengan lampu kilat kamera, pada hari berawan agar terhindar dari cahaya matahari langsung. Kamera digital RGB 12 MP digunakan dari jarak sekitar 3,0 m melintang terhadap barisan, dengan tirai hitam di belakang pohon untuk menutup pohon tetangga. Kotak berukuran 15 cm × 15 cm diletakkan di samping setiap pohon sebagai acuan ukuran. Jumlah buah dihitung manual oleh satu operator pada hari yang sama untuk sisi yang terambil citranya, sisi seberang, dan total pohon; pada panen dicatat pula jumlah dan berat buah.

Metode deteksi memakai model YOLO yang dilatih terpisah per jenis buah. Apel memakai YOLOv5s6 dengan resolusi 1024 × 1024 piksel, sedangkan pir memakai YOLOv7 dengan resolusi 1280 × 1280 piksel. Pelabelan dilakukan dengan Roboflow. Kumpulan data apel berisi 505 citra dengan 36.260 anotasi buah; kumpulan data pir berisi 474 citra dengan 39.052 anotasi. Pembagiannya adalah 70% latih, 20% validasi, dan 10% uji, dengan augmentasi pada kedua kumpulan data. Kinerja dinilai dengan presisi, recall, dan F1-score; hubungan antara jumlah buah hasil deteksi dan hitungan manual diuji dengan korelasi Pearson, uji-t pasangan, dan uji normalitas Shapiro-Wilks. Pengukuran ukuran buah memakai ImageJ dengan menggaris diameter ekuator dan benda berukuran diketahui sebagai acuan, pada 106 buah laboratorium serta 89 apel dan 98 pir di lapangan.

Hasil deteksi menunjukkan presisi 0,86 untuk apel dan 0,87 untuk pir, recall 0,83 untuk keduanya, dan F1-score 0,83 untuk apel serta 0,80 untuk pir; abstrak menyebutkan nilai tertinggi untuk presisi, recall, dan F1-score berturut-turut 0,86, 0,83, dan 0,84. Korelasi antara buah berlabel dan buah dipanen mencapai 0,89 pada apel dan 0,62 pada pir. Korelasi buah dipanen terhadap hitungan manual total pohon mencapai 0,94 dan 0,82, lebih tinggi daripada terhadap hitungan pada sisi citra saja (0,91 dan 0,70). Korelasi antara hitungan manual per pohon dan jumlah buah yang terdeteksi model mencapai 0,88 pada apel dan 0,73 pada pir. Uji-t pasangan menunjukkan selisih rata-rata antara hitungan manual dan deteksi model tidak berbeda secara nyata dari nol (p = 0,0762 untuk pir dan p = 0,3642 untuk apel). Korelasi diameter hasil ukuran manual dan citra adalah 0,89 untuk buah laboratorium, 0,73 untuk apel lapangan, dan 0,80 untuk pir lapangan.

Batasan yang dinyatakan penulis mencakup nilai yang lebih rendah daripada penelitian pembanding karena citra mengambil keseluruhan pohon dengan buah yang relatif kecil, kesulitan mendeteksi semua buah dalam satu tandan, serta bertambahnya positif palsu pada cahaya siang hari. Pir lebih sulit karena tajuk lebih besar dan kompleks, buah tetap hijau saat pengambilan citra, serta tertutup daun dan cabang. Semua citra diambil dari sudut dan jarak yang sama. Penulis menyimpulkan pengukuran ukuran buah dari citra belum akurat dan bergantung pada kedekatan buah dengan benda acuan serta posisinya di pohon, dan menyarankan penambahan jumlah serta variasi kondisi citra.

