# Development of Virescens Fresh Fruit Bunch Ripeness Prediction using LiDAR for Smart Agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bin2021development` |
| Judul asli | Development of Virescens Fresh Fruit Bunch Ripeness Prediction using LiDAR for Smart Agriculture |
| Penulis | bin Mat Seri, Abdul Dzuljalal Ikram; bin Mohd Kassim, Mohd Sallehin; binti Abdul Rahman, Siti Rahmah; Sajak, Aznida Abu Bakar |
| Tahun | 2021 |
| Venue | Tensymp 2021 2021 IEEE Region 10 Symposium |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [bin2021development.pdf](../pdf/bin2021development.pdf)
- DOI resmi: https://doi.org/10.1109/tensymp52854.2021.9550981

## Gambaran Umum

Kajian ini melaporkan prototipe pemindai berbasis sensor jarak LiDAR untuk memperkirakan tingkat kematangan tandan buah segar (TBS) kelapa sawit varietas virescens. Sensor LiDAR Lite V3 dipasang pada dua servo yang menggerakkan berkas laser secara horizontal dan vertikal, lalu setiap titik pengukuran mencatat posisi, jarak, dan nilai intensitas pantulan. Data disimpan ke berkas CSV. Penulis menyatakan bahwa tandan matang memiliki rata-rata intensitas pantulan yang lebih rendah daripada tandan mentah.

Prototipe dibangun dengan Arduino UNO sebagai pengendali, sensor LiDAR Lite V3 dengan jangkauan 40 m, dan dua servo. Dua skenario pemindaian dibandingkan. Skenario pertama memakai resolusi 60x180 dengan langkah sudut 1 derajat, dan pemindaian berhenti saat servo vertikal mencapai posisi di bawah 12 derajat. Skenario kedua memakai resolusi 60x90 dengan langkah 0,5 derajat, dan pemindaian berhenti di bawah 15 derajat. Pada skenario pertama, jumlah titik awan yang terbaca prototipe untuk tandan matang adalah 8.178 dari 8.820 titik yang dihitung dari resolusi, dengan galat 7,3%. Untuk tandan mentah, jumlahnya 8.445 dari 8.820, dengan galat 4,3%. Angka ini menunjukkan seberapa lengkap sensor menangkap titik pindai, bukan akurasi kematangan.

Pada skenario pertama, distribusi nilai intensitas terpusat pada empat nilai diskret, yaitu 84, 98, 112, dan 126. Nilai 126 paling sering muncul pada kedua kelompok, dengan 1.603 kemunculan pada tandan matang dan 3.639 pada tandan mentah. Penulis menyimpulkan bahwa tandan mentah memiliki rata-rata intensitas lebih tinggi, sehingga kematangan dapat dibedakan dari nilai rata-rata tersebut. Hasil skenario kedua hanya disajikan dalam bentuk grafik (Gambar 12) tanpa angka tabel di teks. Jumlah tandan yang diukur dan pengulangan pengukuran tidak tercantum.

Kajian ini tidak mencacah buah dan tidak mengukur akurasi deteksi per tandan. Keluarannya adalah titik awan dan nilai intensitas satu tandan dari satu arah pandang. Penulis sendiri menyebut bahwa pengujian terbatas karena perintah kendali gerakan (CMCO), bahwa data belum tersimpan langsung dari prototipe, dan bahwa analisis awan titik masih direncanakan dengan MATLAB. Verifikasi hasil dilakukan oleh MPOB Bangi, tetapi laporan itu tidak merinci metode verifikasinya.
