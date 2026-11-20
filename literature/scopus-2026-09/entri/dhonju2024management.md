# Management Information Systems for Tree Fruit–2: Design of a Mango Harvest Forecast Engine

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dhonju2024management` |
| Judul asli | Management Information Systems for Tree Fruit–2: Design of a Mango Harvest Forecast Engine |
| Penulis | Dhonju, Hari Krishna; Bhattarai, Thakur; Amaral, Marcelo H.; Matzner, Martina; Walsh, Kerry B. |
| Tahun | 2024 |
| Venue | Horticulturae |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | mango |

## Tautan Akses
- PDF: [dhonju2024management.pdf](../pdf/dhonju2024management.pdf)
- DOI resmi: https://doi.org/10.3390/horticulturae10030301

## Gambaran Umum

Makalah ini merancang "mesin prakiraan panen" mangga sebagai bagian dari Sistem Informasi Manajemen (MIS) kebun. Latar belakangnya adalah kemampuan prakiraan hasil berbasis lokasi yang sudah umum pada tanaman biji-bijian ladang, tetapi belum tersedia untuk buah pohon berdaging. Panen dan sortasi menyumbang sekitar 50% total biaya produksi buah pohon karena sebagian besar masih dipetik manual. Jendela panen mangga hanya beberapa minggu, buah bersifat klimakterik dengan daya simpan rendah, sehingga ketepatan waktu panen dan pengangkutan menentukan mutu. Iklan pengecer biasanya dipesan enam minggu lebih awal, sehingga diperlukan prakiraan waktu dan beban panen. Prakiraan yang lebih awal dan lebih tepat memungkinkan pengaturan tenaga kerja, kemasan, dan transportasi yang lebih baik.

Mesin ini memakai data suhu setiap 15 menit per blok kebun, perkiraan pembungaan mingguan, dan perkiraan bebuahan sebelum panen, baik hasil pengukuran manual maupun visi mesin. Keluarannya adalah waktu panen optimal dan beban buah per blok per minggu untuk penjadwalan panen. Data berasal dari pengujian teknologi visi mesin pada 37 kebun di sentra produksi mangga Australia. Masukan dari pemangku kepentingan dikumpulkan melalui wawancara semi-terstruktur pada 2022–2024 terhadap delapan pengelola kebun, tiga penyuluh atau peneliti, dan tiga pemasar mangga. Penulis menyatakan bahwa kebaruan makalah terletak pada uraian struktur mesin prakiraan, bukan pada pembangunan atau evaluasi perangkat lunak akhir.

Mekanisme prakiraan waktu panen menggabungkan dua jalur. Jalur pertama menghitung *Growing Degree Days* (GDD) dari tanggal puncak pembungaan dan suhu harian, dengan suhu dasar 12 °C dan suhu atas 32 °C. Kebutuhan GDD spesifik kultivar meliputi Honey Gold 1560, Calypso 1540, Keitt 1936, R2E2 1600, dan KP 1420. Jalur kedua memakai kandungan bahan kering (DMC) buah yang diukur berulang dengan spektrometer inframerah dekat portabel; laju kenaikan DMC dipakai untuk memprediksi tanggal tercapainya target kematangan. Sebagai acuan, buah Keitt dengan warna daging kartu nomor 13 memiliki DMC 17% w/w. Visi mesin menghitung malai bunga pada tahap pertumbuhan tertentu dari citra kamera yang dipasang pada kendaraan, sedangkan penghitungan buah memakai pelacakan antarframe sehingga setiap buah dihitung sekali setelah tidak muncul lagi pada frame berikutnya; hasilnya ditampilkan sebagai peta panas per 3,5 m barisan.

Mekanisme prakiraan beban panen memakai luas pembungaan, jumlah buah, ukuran buah, dan proporsi buah yang dapat dipasarkan. Hasil prakiraan dihitung dengan persamaan hasil prakiraan Yf = F × Ymax × A, misalnya pembungaan 40% pada blok dengan hasil maksimum 40 t/ha menghasilkan prakiraan 16 t/ha. Beban per peristiwa pembungaan dibagi dengan Yi = (FEi/FEmax) × FC, misalnya FE1 sebesar 30% dari total 90% dengan hitungan 120.000 buah menghasilkan 40.000 buah. Untuk ukuran, massa buah meningkat linier menjelang panen, sehingga laju pertumbuhan dari dua pengukuran dipakai untuk memproyeksikan distribusi ukuran pada hari panen; contoh kultivar Calypso memakai laju 23,2 g/minggu. Pada contoh penjadwalan enam minggu, total prakiraan per minggu adalah 36.975, 92.227, 257.999, 127.427, 258.668, dan 226.314 kg, dibandingkan hasil aktual 45.975, 126.123, 199.798, 101.752, 241.765, dan 191.459 kg. Pada contoh penempatan kotak, alokasi visi mesin mencapai 106% dan 112% dari kebutuhan yang dinilai dari catatan pengemasan. Seluruh angka berasal dari contoh dan data yang disajikan makalah ini, bukan dari percobaan yang dikendalikan.

Penulis menyatakan beberapa batasan. Prakiraan GDD dapat menyimpang karena suhu yang diukur sensor tidak selalu sama dengan suhu buah, baik antarblok maupun di dalam tajuk, dan pembungaan dalam satu malai berlangsung bertahap selama sedikitnya seminggu. Warna kulit tidak dapat dijadikan indeks kematangan yang andal untuk kultivar komersial Australia, sedangkan warna daging bersifat destruktif sehingga membatasi jumlah sampel. Masa tunggu di pohon berkisar 7–21 hari tergantung kultivar, sehingga masukan pengelola diperlukan untuk menyeimbangkan beban panen. Selisih antara prakiraan dan hasil aktual antara lain berasal dari kesalahan distribusi waktu pembungaan, hitungan buah, dan berat rata-rata, serta buah yang tidak dipetik atau dibuang. Penulis juga menyatakan tidak merinci atau mengevaluasi perangkat lunak yang dibangun, melainkan hanya memakai keluaran sistem prototipe untuk mengilustrasikan cara kerja mesin.
