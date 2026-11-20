# Revolutionizing palm oil ripeness classification: Utilizing YOLOv8 for ultra-precise ripeness detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `josdaan2024revolutionizing` |
| Judul asli | Revolutionizing palm oil ripeness classification: Utilizing YOLOv8 for ultra-precise ripeness detection |
| Penulis | Josdaan, Jordan; Tamsil, Vianna Calista; Harefa, Jeklin; Jingga, Kenny |
| Tahun | 2024 |
| Venue | Procedia Computer Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [josdaan2024revolutionizing.pdf](../pdf/josdaan2024revolutionizing.pdf)
- DOI resmi: https://doi.org/10.1016/j.procs.2024.10.296

## Gambaran Umum

Josdaan dkk. (2024) menguji *YOLOv8* (*You Only Look Once* versi 8), detektor objek yang juga dapat dipakai sebagai pengklasifikasi citra, untuk menentukan kelas kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyebut penentuan kematangan secara otomatis sebagai tujuan utama. Setiap citra diberi satu label kelas, dan penelitian ini tidak menghitung jumlah buah. Karena itu kajian ini termasuk kelompok pencitraan TBS dan grading, bukan pencacahan.

Data terdiri dari 3.024 citra TBS dalam enam kelas: Unripe 157 citra, Underripe 988, Rotten 86, Ripe 1.146, Overripe 423, dan Empty Set 224. Dataset tersebut diambil dari Roboflow. Setiap citra diubah ukurannya menjadi 224 × 224 piksel, nilai pikselnya dinormalisasi ke rentang 0 sampai 1 dengan *Keras ImageDataGenerator*, lalu diberi augmentasi. Pembagian data latih dan data uji, lokasi pengambilan, dan sensor kamera belum terbaca dalam bagian yang diperiksa.

Lima varian dilatih selama 20 *epoch* dengan konfigurasi *hyperparameter* yang dipilih penulis untuk setiap varian. Hasil dilaporkan sebagai *top-1 accuracy*, yaitu proporsi citra yang kelas peringkat pertamanya tepat, dan *top-5 accuracy*. Top-1 untuk YOLOv8n adalah 0,9572, YOLOv8s 0,9819, YOLOv8m 0,9885, YOLOv8l 0,9885, dan YOLOv8x 0,9884. Top-5 mencapai 1 pada n, s, l, dan x, serta 0,998 pada m. Kecepatan rata-rata dan memori GPU berbanding terbalik dengan ukuran model: n 17,97 iterasi per detik dengan 0,319 G; s 15,92 iterasi per detik dengan 0,554 sampai 0,558 G; m 14,68 iterasi per detik dengan 1,08 sampai 1,12 G; l 10,27 iterasi per detik dengan 1,81 sampai 2,11 G; x 7,12 iterasi per detik dengan 2,51 sampai 3,15 G.

Penulis memilih YOLOv8m sebagai model paling seimbang. YOLOv8m dan YOLOv8l memiliki top-1 yang sama (0,9885), tetapi YOLOv8m lebih cepat dan memakai memori GPU lebih sedikit. Penulis juga menyatakan YOLOv8 lebih akurat daripada YOLOv3, YOLOv4, YOLOv5, CNN, dan ANN dari studi 2020 sampai 2024, tetapi perbandingan itu ditulis tanpa tabel angka pembanding dalam bagian yang diperiksa.

Penulis tidak menulis bagian batasan studi tersendiri. Dari bagian yang diperiksa, dua hal belum dapat dinilai: pembagian data uji tidak dijabarkan sehingga selisih top-1 di bawah 0,01 antarvarian tidak dapat diuji ketidakpastiannya, dan hasil berasal dari satu tugas klasifikasi per citra sehingga tidak berlaku langsung untuk penghitungan buah dalam satu pohon atau satu pandang.
