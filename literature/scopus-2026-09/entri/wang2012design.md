# Design of crop yield estimation system for apple orchards using computer vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2012design` |
| Judul asli | Design of crop yield estimation system for apple orchards using computer vision |
| Penulis | Wang, Qi; Nuske, Stephen Thomas; Bergerman, Marcel; Singh, Sanjiv |
| Tahun | 2012 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting 2012 Asabe 2012 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wang2012design.pdf](../pdf/wang2012design.pdf)

## Gambaran Umum

Kajian ini membahas perancangan sistem estimasi hasil panen apel berbasis *computer vision* untuk kebun apel. Saat ini petani memperkirakan hasil panen dari catatan historis dan penghitungan manual. Cara ini memerlukan pengalaman manajer kebun, memakan banyak tenaga kerja, dan sering tidak akurat. Penulis menyatakan bahwa belum ada alat siap pakai untuk kebutuhan tersebut. Tujuan penelitian adalah merancang dan menguji sistem yang mendeteksi serta menghitung apel merah secara otomatis dari citra yang diambil terus-menerus di kebun. Pengujian yang dilaporkan bersifat awal.

Sistem memakai dua kamera Nikon D300s beresolusi tinggi dengan lensa sudut lebar 11 mm. Kedua kamera dipasang sebagai pasangan *stereo* dengan jarak sekitar 0,28 m dan dipicu serentak 1 Hz. Lampu ring flash digunakan agar pengambilan citra dilakukan pada malam hari. Perangkat dipasang pada kendaraan kebun otonom yang melintasi lorong pohon dengan kecepatan 0,25 m/s. Posisi kendaraan dicatat oleh sistem POS LV pada 30 Hz. Pengujian dilakukan pada blok apel di Sunrise Orchard, Rock Island, Washington, pada September 2011. Varietas yang diuji adalah Red Delicious dengan sistem tanam *tall spindle*. Blok seluas sekitar setengah acre terdiri atas 15 baris dengan sekitar 48 pohon per baris. Baris 1 sampai 10 mendapat penjarangan buah rutin seperti di kebun komersial. Baris 11 sampai 15 tidak mendapat penjarangan. Setiap baris dibagi menjadi 16 seksi, umumnya tiga pohon per seksi. Kebenaran dasar (*ground truth*) berasal dari penghitungan manual oleh pekerja kebun profesional per seksi.

Perangkat lunak pascapemrosesan mendeteksi apel merah berdasarkan warna, lalu menghitung rata-rata diameter apel dan memisahkan kelompok apel yang bersentuhan. Setiap kelompok hanya dapat dipisah menjadi dua apel. Apel yang tertutup daun atau cabang dihitung dengan cara estimasi. Koordinat global dari GPS dipakai untuk menggabungkan deteksi apel yang sama dari dua sisi baris agar tidak terjadi *overcounting*. Untuk baris 11 sampai 15, penulis memakai 10 seksi acak dari 80 seksi dan regresi linear tanpa intersep untuk memperoleh faktor kompensasi 1,7. Hasil pada baris 1 sampai 10 menunjukkan rata-rata kesalahan per baris -2,9% dengan simpangan baku 7,1%. Gabungan 10 baris itu memberi kesalahan -3,2%. Pada baris 11 sampai 15 tanpa kompensasi, rata-rata kesalahan per baris mencapai -41,3% dengan simpangan baku 3,2%. Setelah faktor kompensasi diterapkan, rata-rata kesalahan per baris turun menjadi 0,4% dengan simpangan baku 5,5%. Penulis menyimpulkan bahwa sistem berkinerja baik pada blok dengan visibilitas buah yang baik, yaitu kesalahan -3,2% untuk sekitar 480 pohon. Pada blok dengan oklusi buah yang signifikan, kesalahannya 0,4% untuk sekitar 240 pohon.

Penulis menyebut beberapa batasan. Perangkat lunak hanya dapat memisahkan kelompok dua apel, sedangkan kelompok yang lebih besar belum tertangani dengan akurat. Apel yang dekat dengan kamera tampak jauh lebih besar daripada apel lain dalam citra yang sama, sehingga diameter rata-rata dapat menimbulkan kesalahan. Penulis merencanakan perbaikan pada versi berikutnya. Faktor kompensasi hanya didasarkan pada 10 seksi, atau 12,5% dari baris 11 sampai 15. Persentase sampel minimum yang menjamin akurasi estimasi belum ditentukan dan menjadi pekerjaan selanjutnya. Penulis juga menegaskan bahwa hasil ini berasal dari pengujian pendahuluan pada satu blok kebun dan satu varietas.
