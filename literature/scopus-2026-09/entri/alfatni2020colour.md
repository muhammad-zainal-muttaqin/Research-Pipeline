# Colour Feature Extraction Techniques for Real Time System of Oil Palm Fresh Fruit Bunch Maturity Grading

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alfatni2020colour` |
| Judul asli | Colour Feature Extraction Techniques for Real Time System of Oil Palm Fresh Fruit Bunch Maturity Grading |
| Penulis | Alfatni, Meftah Salem M; Mohamed Shariff, Abdul Rashid; Ben Saaed, Osama M.; Albhbah, Atia Mahmod; Mustapha, Aouache |
| Tahun | 2020 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alfatni2020colour.pdf](../pdf/alfatni2020colour.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/540/1/012092

## Gambaran Umum

Studi ini (Alfatni dkk., 2020, IOP Conference Series: Earth and Environmental Science 540, 012092) membangun sistem klasifikasi tingkat kematangan tandan buah segar kelapa sawit dari citra warna. Setiap citra diberi satu dari tiga label: under ripe, ripe, atau overripe. Sistem menghitung fitur warna dengan dua cara, yaitu fitur statistik warna (rerata dan simpangan baku) dan histogram warna, lalu mengklasifikasikannya dengan jaringan saraf tiruan (ANN). Penulis melaporkan nilai AUC pada kurva ROC sampai 93 persen untuk fitur statistik dan sampai 94 persen untuk histogram warna. Studi ini tidak menghitung jumlah buah.

Data yang dipakai adalah 180 citra latih dan 270 citra uji. Citra dipotong menjadi tiga region of interest (ROI): ROI1 berukuran 300 x 300 piksel, ROI2 50 x 50 piksel, dan ROI3 100 x 100 piksel. Pemotongan dimaksudkan untuk menghindari distorsi citra di bagian acak tandan dan untuk melihat pengaruh ukuran masukan. Pengolahan citra dan percobaan dilakukan dengan MATLAB. Akuisisi dilakukan dengan kamera CCD RGB pada kondisi terkendali, dengan frame grabber NIPCI-8285.

Jawabannya bergantung pada ukuran ROI dan jenis fitur. Hasil ROC untuk fitur statistik berkisar 91,3 sampai 93,1 persen, dan untuk histogram 92,8 sampai 93,9 persen. Selisih antarukuran ROI kecil, sehingga pengaruh ukuran potongan tidak tampak besar pada data ini. Penulis memberi Tabel 1 untuk akurasi latih ANN, KNN, dan SVM. Pada tabel itu fitur statistik ROI1 dan ROI2 mencapai akurasi latih 100 persen, sedangkan histogram ROI1 98 persen dan ROI2 100 persen.

Kelas yang dipakai adalah kematangan, bukan jumlah tandan. Karena itu studi ini tidak menjawab pertanyaan penghitungan lintas pandang. Keterbatasannya terlihat dari desain: satu sumber kamera, kondisi pencahayaan terkendali, dan ukuran data yang kecil. Penulis tidak melaporkan jumlah citra per kelas atau cara pemisahan data per pohon. Karena itu angka AUC di atas tidak dapat dibandingkan langsung dengan studi lapangan yang memakai data antarpohon.
