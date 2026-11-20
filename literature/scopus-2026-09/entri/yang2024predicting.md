# Predicting the growth trajectory and yield of greenhouse strawberries based on knowledge-guided computer vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024predicting` |
| Judul asli | Predicting the growth trajectory and yield of greenhouse strawberries based on knowledge-guided computer vision |
| Penulis | Yang, Qi; Liu, Licheng; Zhou, Junxiong; Rogers, Mary; Jin, Zhenong |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [yang2024predicting.pdf](../pdf/yang2024predicting.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.108911

## Gambaran Umum

Penelitian ini membahas pemantauan dan pemodelan pertumbuhan buah stroberi pada tingkat buah individual. Model pertumbuhan yang ada umumnya bekerja pada tingkat plot atau tanaman, sehingga tidak dapat menyimulasikan pertumbuhan buah satu per satu. Sementara itu, studi berbasis *computer vision* (CV) yang ada umumnya hanya menangani tugas sesaat, seperti deteksi objek atau estimasi volume buah, tanpa kemampuan penalaran untuk simulasi dinamis. Untuk mengatasi hal tersebut, penulis mengembangkan kerangka KGCV-strawberry. Kerangka ini terdiri dari dua komponen. Komponen pertama adalah detektor sifat buah, yang berperan sebagai "mata" dan membaca *bounding box* serta sifat biofisik buah dari citra mentah. Komponen kedua adalah simulator pertumbuhan buah, yang berperan sebagai "otak" dan memprediksi pertumbuhan buah dari perkiraan sifat tersebut.

Percobaan dilakukan di Plant Growth Facility, Universitas Minnesota, pada Juni hingga Oktober 2022 dan 2023. Pada 2022 digunakan 149 pot stroberi Cabrillo, dan pada 2023 digunakan 180 pot stroberi Albion. Terdapat empat perlakuan nitrogen, yaitu 0%, 50%, 100%, dan 150%. Penulis juga mengumpulkan citra dari lahan terbuka di kampus untuk memperbanyak data latih detektor. Sensor yang digunakan meliputi kamera serta stasiun cuaca berbasis *Internet-of-things* yang mengukur suhu udara, kelembapan relatif, dan radiasi gelombang pendek setiap 10 menit. Setiap tahun, 20 buah ditandai sejak fase berbunga, dengan lima buah dari tiap perlakuan nitrogen, lalu difoto setiap tiga hari. Untuk evaluasi, penulis memilih 38 urutan citra yang panjangnya lebih dari enam.

Metode utama memakai Faster-RCNN dengan *backbone* ResNet-50 untuk mendeteksi *bounding box* dan tahap fenologi buah. Jaringan CNN terpisah memperkirakan ukuran buah dan persentase kemajuan tahap fenologi. Pertumbuhan buah diasumsikan mengikuti pola kurva berbentuk-S (*S-shape*, atau fungsi logistik dan sigmoid). Jaringan simulator dilatih dengan data sintetis dari kurva tersebut, sedangkan parameter kurva untuk tiap buah diperkirakan dari urutan ukuran buah yang dihasilkan detektor. Hasil yang dilaporkan menunjukkan bahwa RMSE estimasi diameter turun 74% ketika jumlah pengamatan naik dari 1 menjadi 6. Untuk prediksi hasil panen, RMSE turun dari 3,58 g menjadi 2,01 g dan R2 naik dari 0,25 menjadi 0,73. Untuk prediksi jumlah hari derajat pertumbuhan (GDD) tersisa hingga matang, RMSE turun dari 71,87 °C·hari menjadi 39,30 °C·hari dan R2 naik dari 0,11 menjadi 0,61. Prediksi terbaik dicapai dekat masa matang. Meski demikian, akurasinya dinilai cukup dua minggu sebelum buah matang. Pada tingkat tanaman, KGCV-strawberry menangkap dinamika hasil pada tiap panen dengan lebih baik dibandingkan model proses CROPGRO-Strawberry.

Penulis menyatakan bahwa hasil di tingkat tanaman diperoleh dengan menskalakan hasil per buah menggunakan suatu rasio. Rasio itu dihitung dari jumlah buah bertanda yang dipanen dibandingkan dengan total buah yang dipanen, karena tidak semua buah di rumah kaca memiliki data urutan citra. Penskalaan ini menjadi keterbatasan dalam estimasi hasil pada tingkat tanaman. Penulis juga menekankan bahwa prediksi paling akurat dicapai dekat kematangan, sehingga akurasi pada fase awal pertumbuhan lebih rendah. Kerangka ini dirancang untuk manajemen buah individual pada pertanian stroberi cerdas, dan penulis menyediakan kode sumber serta dataset di repositori daring.
