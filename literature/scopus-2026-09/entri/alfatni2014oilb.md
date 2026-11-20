# Oil palm fresh fruit bunch ripeness classification based on rule-based expert system of ROI image processing technique results

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alfatni2014oilb` |
| Judul asli | Oil palm fresh fruit bunch ripeness classification based on rule-based expert system of ROI image processing technique results |
| Penulis | Alfatni, M S M; Shariff, A R M; Abdullah, M Z; Marhaban, M H; Shafie, S B; BAmiruddin, M D; Saaed, O M B |
| Tahun | 2014 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alfatni2014oilb.pdf](../pdf/alfatni2014oilb.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/20/1/012018

## Gambaran Umum

Kajian ini (Alfatni dkk., 2014) menilai tingkat kematangan tandan buah segar (TBS) kelapa sawit dari citra warna. Setiap tandan diklasifikasikan ke dalam tiga kelas: belum matang (*under ripe*), matang (*ripe*), dan terlalu matang (*overripe*), dengan label dari pakar MPOB sebagai acuan. Tujuannya adalah memperbaiki ketepatan penilaian kematangan dengan menggabungkan sistem pakar berbasis aturan (*rule-based expert system*) dan pembelajaran mesin klasik. Kajian ini tidak menghitung jumlah tandan di kebun, sehingga tidak termasuk kajian penghitungan.

Pendekatannya bertumpu pada tiga area minat (*region of interest*, ROI) yang diambil dari setiap citra tandan. ROI1 berukuran 300 x 300 piksel, ROI2 50 x 50 piksel, dan ROI3 100 x 100 piksel. Dari tiap ROI diekstraksi dua jenis fitur: fitur warna statistik dan histogram warna. Ketiga pengklasifikasi yang dibandingkan adalah *k-nearest neighbour* (KNN), *support vector machine* (SVM), dan jaringan saraf tiruan (ANN). Aturan IF-THEN-ELSE menggabungkan keluaran ketiga ROI untuk memutuskan kelas akhir, tanpa pelatihan ulang pada tahap aturan. Aturan ini bekerja di atas hasil klasifikasi per ROI, sehingga kajian ini membandingkan sistem berbasis aturan dengan setiap ROI tunggal.

Hasil utama dilaporkan dalam tiga versi yang tidak sepenuhnya seragam. Bagian Hasil menyebut akurasi 93% untuk fitur warna statistik dengan KNN, 92% untuk statistik dengan SVM, dan 92% untuk histogram dengan SVM. Versi terbaik per ROI adalah 93% (ROI1, warna statistik, ANN), 93% (ROI1, histogram, KNN), dan 94% (ROI3, histogram, ANN). Kesimpulan dan abstrak menyebut 94% untuk KNN pada warna statistik. Kurva ROC menunjukkan nilai AUC untuk setiap lengan: pada warna statistik dengan KNN, sistem berbasis aturan mencapai AUC 92,9630% dibandingkan 92,3635% untuk ROI3 dan 90,6433% untuk ROI2. Pada SVM dengan warna statistik, sistem berbasis aturan mencapai AUC 91,5364%. Angka 93% dan 94% tidak dapat didamaikan dari teks ini, sehingga kajian ini tidak dikutip sebagai angka tunggal tanpa catatan.

Kajian ini melaporkan bahwa KNN dan SVM lebih efisien secara tingkat keberhasilan (*grading rate*) daripada ANN pada hampir semua kasus. Kesimpulan juga menyebut bahwa ROI yang lebih baik dari hasil aturan dipilih untuk tahap pemeriksaan lanjutan. Namun, tidak ada tabel yang memuat jumlah citra, pembagian data latih dan uji, atau akurasi per kelas. Ukuran sampel dan prosedur validasi silang tidak tampak dalam bagian yang dibaca, sehingga angka 93 hingga 94% belum dapat dinilai tingkat kepercayaannya. Hasil ini juga hanya berlaku untuk penilaian kematangan pada potongan citra, bukan untuk penghitungan tandan di pohon atau di antara pandangan yang berbeda.

Dari sisi tinjauan ini, kajian bermanfaat sebagai contoh bahwa klasifikasi kematangan dapat dilakukan per tandan dengan fitur warna sederhana dan ROI tetap. Kajian tidak menguji deduplikasi antarpandang, tidak memakai detektor objek, dan tidak memakai data kedalaman. Keterbatasan ini perlu disebut bila kajian dikutip sebagai bukti untuk kelas kematangan. Angka yang tertulis berbeda antarbagian juga perlu diperiksa ke naskah asli sebelum dikutip secara formal.
