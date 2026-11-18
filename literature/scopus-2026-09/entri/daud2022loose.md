# Loose Fruitlet and Fresh Fruit Bunch Detection for Palm Oil Harvest Management

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `daud2022loose` |
| Judul asli | Loose Fruitlet and Fresh Fruit Bunch Detection for Palm Oil Harvest Management |
| Penulis | Daud, Marizuana Mat; Kadim, Zulaikha; Woon, Hon Hock |
| Tahun | 2022 |
| Venue | Proceedings of the 2022 IEEE International Conference on Internet of Things and Intelligence Systems Iotais 2022 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [daud2022loose.pdf](../pdf/daud2022loose.pdf)
- DOI resmi: https://doi.org/10.1109/iotais56727.2022.9975972

## Gambaran Umum

Penelitian ini bertujuan membangun sistem otomatis untuk pengelolaan panen kelapa sawit. Sistem ini mendeteksi dan menghitung buah lepas (loose fruitlet, LF) di tanah guna menentukan waktu pemotongan tandan buah segar (fresh fruit bunch, FFB), serta mengestimasi jumlah FFB yang terkumpul dan kepadatan LF selama kegiatan pengumpulan. Latar belakangnya adalah ketergantungan industri sawit pada tenaga kerja manual; sekitar 90% biaya panen berupa upah, dan penilaian kematangan secara tradisional didasarkan pada jumlah LF di tanah, yaitu 1-10 buah menandakan tandan siap dipotong. Informasi dari sistem ini dipakai untuk merencanakan tenaga kerja dan alat, serta meningkatkan produktivitas panen.

Data berupa 5013 citra berukuran 700 × 1000 piksel yang dikumpulkan dari lahan perkebunan kecil di dekat Sepang, Selangor, Malaysia. Sistem terdiri dari dua bagian. Pada tahap prapanen, model deteksi pohon sawit, FFB, dan grabber memakai Faster R-CNN yang dilatih awal pada MS COCO lalu dilatih ulang dengan transfer learning pada data sendiri untuk menghasilkan tiga kelas. Arsitektur Faster R-CNN mencakup lapisan konvolusi untuk ekstraksi ciri, region proposal network (RPN) untuk menghasilkan usulan wilayah, dan lapisan prediksi; hanya lapisan fully connected yang dibuka saat pelatihan ulang, dengan lapisan terakhir diubah untuk tiga kategori. Penulis menguji tiga komposisi pembagian data, yaitu (80, 10, 10), (70, 20, 10), dan (60, 20, 20) untuk latih, uji, dan validasi, serta tiga jumlah langkah latih, yaitu 15.000, 30.000, dan 50.000. Jarak antarpohon 7-9 m dan lintasan pemindaian dianggap satu arah, sehingga pelacakan pohon memakai aturan sederhana: pohon hanya dianalisis ketika berada di dalam area pelacakan.

Deteksi LF memakai analisis warna dalam ruang Lab melalui dua proses. Proses luring menentukan nilai rata-rata referensi tiap kanal warna (μLref, μaref, μbref) dari piksel di dalam kotak anotasi buah lepas pada citra referensi, serta toleransi referensi tref yang dihitung sebagai rata-rata ditambah simpangan baku citra selisih. Proses daring mengubah citra yang dipangkas di sekitar batang pohon ke ruang Lab, membentuk citra selisih δ antara nilai Lab setiap piksel dan rata-rata referensi, mengambil ambang citra itu dengan tref menjadi citra biner, lalu menerapkan operasi morfologi dilasi dan top-hat serta komponen terhubung; banyaknya wilayah terhubung menjadi jumlah LF pada citra tersebut. Jumlah LF akhir untuk satu pohon diambil dari nilai yang paling sering muncul pada frame selama pohon dilacak. Apabila jumlah itu melebihi ambang t=3, pohon ditandai siap panen (RTH); jika tidak, pohon ditandai belum siap panen (NRTH).

Pada tahap panen, sistem mendeteksi pohon, FFB, dan grabber, lalu menghitung sebuah FFB sebagai terkumpul apabila luas irisan antara kotak FFB dan kotak grabber lebih dari nol. Kepadatan LF dikelompokkan menjadi rendah untuk kurang dari 50 buah, sedang untuk 50-100 buah, dan tinggi untuk lebih dari 100 buah. Akurasi penghitungan LF didefinisikan sebagai (TP+TN)/(TP+TN+FP+FN), dan diuji pada 10 citra dengan total sekitar 200 LF menghasilkan akurasi rata-rata 92,65%. Deteksi pohon, FFB, dan grabber diukur dengan mAP pada ambang IoU 0,5. Konfigurasi terbaik, dengan 70% data latih, 20% uji, 10% validasi, dan 50.000 langkah, menghasilkan mAP 96,6% untuk FFB, 99,0% untuk grabber, dan 97,1% untuk pohon; abstrak mencantumkan angka 96,5%, 99,2%, dan 97,2%.

Penulis menyebut beberapa batasan. Deteksi positif palsu muncul dari objek latar yang warnanya mirip buah lepas, misalnya daun kering; pemangkasan citra berdasarkan kotak pohon mengurangi kesalahan ini. Buah lepas yang saling berdekatan dapat terdeteksi sebagai satu objek, sehingga buah lainnya dihitung sebagai negatif palsu, dan penulis mengusulkan penggunaan ciri bentuk untuk perbaikan. Penulis tidak menyebut interval kepercayaan, uji signifikansi, atau rincian jumlah citra pada pengujian LF selain 10 citra yang dilaporkan.

