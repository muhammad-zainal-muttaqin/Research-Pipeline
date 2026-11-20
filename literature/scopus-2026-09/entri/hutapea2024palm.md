# Palm Fruit Ripeness Detection and Counting Using YOLOv8 Algorithm in PTPN IV Medan North Sumatera Indonesia

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hutapea2024palm` |
| Judul asli | Palm Fruit Ripeness Detection and Counting Using YOLOv8 Algorithm in PTPN IV Medan North Sumatera Indonesia |
| Penulis | Hutapea, Rael Russel; Purba, Samdo Jumar; Tandion, William Ferdinandz; Sihotang, Erna Fransisca Angela; Irwansyah, Edy |
| Tahun | 2024 |
| Venue | 2024 6th International Conference on Cybernetics and Intelligent System Icoris 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hutapea2024palm.pdf](../pdf/hutapea2024palm.pdf)
- DOI resmi: https://doi.org/10.1109/icoris63540.2024.10903790

## Gambaran Umum

Penelitian ini bertujuan membangun sistem deteksi dan penghitungan buah kelapa sawit berbasis YOLOv8 untuk mempercepat dan menyederhanakan pemilahan buah berdasarkan kematangan di PTPN IV Medan, Sumatera Utara. Penilaian kematangan manual memerlukan waktu lebih lama. Penulis mengharapkan sistem otomatis meningkatkan efisiensi pengelolaan kebun dan hasil panen. YOLOv8 dipilih karena kecepatan dan kemampuan deteksi waktu nyatanya, dengan modul C2f pada backbone yang menggabungkan fitur tingkat tinggi dan informasi kontekstual.

Data berasal dari repositori perkebunan PTPN IV dan terdiri atas 85 foto berukuran 640×640 piksel yang diambil dengan kamera iPhone 12. Citra mencakup buah matang, belum matang, busuk, dan beberapa buah dalam satu citra. Data diunggah ke Roboflow, dipilah menjadi citra baik dan buruk, lalu diberi label tiga kelas, yaitu ripe, unripe, dan rotten. Pembagian awal memakai 63 citra latih (88%), 13 citra validasi (7%), dan 9 citra uji (5%). Pra-pemrosesan memakai Auto-Orient dan pengubahan ukuran menjadi 640×640. Augmentasi hanya berupa pembalikan dan rotasi 90°, menghasilkan 185 citra setelah augmentasi dengan 163 citra pada cawat latih.

Model dilatih di Google Colab melalui API Roboflow selama 25 epoch dengan masukan 640×640 piksel. Pengujian memakai validasi silang, dan penulis menyatakan hasilnya hampir sama tetapi tidak identik. Mekanisme yang dijelaskan adalah deteksi kotak pembatas per buah beserta label kematangannya. Penulis tidak merinci cara penghitungan jumlah buah dari kotak-kotak tersebut.

Tabel II mencantumkan mAP50 dan mAP50-95 untuk dua kelas. Nilai untuk seluruh objek adalah 0,991 dan 0,662; kelas ripe mencatat 0,988 dan 0,606; kelas unripe mencatat 0,995 dan 0,717. Abstrak dan simpulan menyebut angka 0,991 sebagai akurasi 99,1% untuk ketiga kelas, sedangkan tabel mencantumkannya sebagai mAP50. Penulis tidak menyatakan secara eksplisit cawat yang dipakai untuk menghitung angka-angka itu.

Penulis menyatakan bahwa hasil untuk kelas rotten tidak ditampilkan karena data untuk kelas itu tidak cukup untuk melatih model. Studi ini memakai set data dan jumlah epoch yang lebih kecil daripada kajian sebelumnya, sehingga penulis mengusulkan pengumpulan data yang lebih banyak dan jelas per tingkat kematangan serta penambahan epoch untuk meningkatkan generalisasi.
