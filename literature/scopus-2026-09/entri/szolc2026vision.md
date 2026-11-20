# Vision-Based Automatic Fruit Counting with UAV

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `szolc2026vision` |
| Judul asli | Vision-Based Automatic Fruit Counting with UAV |
| Penulis | Szolc, Hubert; Wasala, Mateusz; Mietla, Remigiusz; Iwicki, Kacper; Kryjak, Tomasz |
| Tahun | 2026 |
| Venue | Lecture Notes in Networks and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, sweet pepper, eggplant |

## Tautan Akses
- PDF: [szolc2026vision.pdf](../pdf/szolc2026vision.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-032-08359-3_23

## Gambaran Umum

Kajian ini membahas sistem pencacahan buah otomatis menggunakan *unmanned aerial vehicle* (UAV) untuk pertanian cerdas. Penulis menyoroti bahwa pemantauan hasil panen pada kebun besar sulit dilakukan secara manual, sehingga diperlukan sistem otomatis. Sistem yang diajukan memproses aliran video dari kamera RGB dan sensor kedalaman (*depth*) dengan operasi citra klasik. Sistem ini juga merencanakan dan menjalankan lintasan terbang yang meminimalkan waktu dan jarak tempuh. Solusi ini dikembangkan untuk memenuhi ketentuan UAV Competition pada konferensi ICUAS 2024.

Data berasal dari lingkungan simulasi Gazebo yang disediakan panitia kompetisi. Simulasi meniru sebuah gudang dengan 27 rak. Setiap rak berisi tanaman tomat (buah merah), paprika (buah kuning), atau terung (buah ungu). Sensor yang digunakan adalah kamera RGB dan sensor kedalaman yang dipasang pada quadcopter. Pengujian dilakukan pada 500 misi yang dibangkitkan secara acak dari total 3 × 227 kemungkinan misi. Setiap misi ditentukan oleh jenis tanaman dan urutan rak yang harus diperiksa. Seluruh 500 misi digunakan sebagai data evaluasi.

Metode utama berupa rangkaian operasi klasik. Citra diubah ke ruang warna *HSV*. Area bedengan dipisahkan dengan dilasi morfologi dan filter median, dibantu peta kedalaman. Buah disegmentasi dengan ambang yang dipilih secara empiris, lalu dihitung dengan *distance transform* dan ambang 0,7. Cara ini memisahkan buah yang saling bersentuhan. Hasil hitungan dari dua sisi bedengan digabung dengan operasi geometri dasar. Lintasan dihitung dengan algoritma Fast-TSP dan dijalankan oleh pelacak TOPP-RA. Hasil evaluasi menunjukkan skor rata-rata 87,27 dari 100. Rinciannya adalah poin pelaporan jumlah buah 49,88 dari 50, poin waktu tempuh 13,51 dari 25, dan poin jarak tempuh 23,88 dari 25. Penalti tabrakan rata-rata 0,00. Tidak ada misi dengan bedengan yang terlewat atau tabrakan. Sebanyak 2 misi (0,40 persen) mengalami kesalahan penghitungan. Pada kompetisi ICUAS 2024, skor rata-rata resmi adalah 84,83 dari 100, dengan peringkat keenam dari 23 tim. Tim ini kemudian lolos ke final.

Penulis menyebutkan beberapa batasan. Poin waktu tempuh berada jauh di bawah nilai acuan. Penulis menduga hal ini disebabkan kecepatan eksekusi yang terlalu rendah atau waktu yang hilang saat memotret buah. Penulis memilih pendekatan konservatif demi menjaga keselamatan terbang dan ketepatan hitungan. Nilai acuan waktu 100 detik dan jarak 150 meter ditetapkan sebagai konstanta sesuai panitia, sehingga skor tidak berlaku sebagai ukuran untuk setiap misi. Hasil yang dilaporkan berasal dari simulasi saja. Tahap final kompetisi memakai sensor berbeda, yaitu LiDAR tanpa kamera kedalaman, dan tahap ini berada di luar cakupan makalah. Penulis berencana menguji sistem di lingkungan nyata dengan bola berwarna sebagai pengganti buah. Rencana lainnya adalah menjalankan sistem pada platform embedded seperti SoC FPGA atau Nvidia Jetson.
