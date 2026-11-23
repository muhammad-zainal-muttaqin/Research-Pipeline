# UAV-Based Optimization for Fruit Counting in Greenhouses

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vasconcelos2024uav` |
| Judul asli | UAV-Based Optimization for Fruit Counting in Greenhouses |
| Penulis | Vasconcelos, Jo\~ao V\'\itor R.; Hudson, Thayron M.; dos Santos, Andr\'e G.; Saska, Martin; Brand\~ao, Alexandre S. |
| Tahun | 2024 |
| Venue | 2024 International Conference on Unmanned Aircraft Systems Icuas 2024 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, sweet pepper, eggplant |

## Tautan Akses
- PDF: [vasconcelos2024uav.pdf](../pdf/vasconcelos2024uav.pdf)
- DOI resmi: https://doi.org/10.1109/icuas60882.2024.10556844

## Gambaran Umum

Penulis membahas pencacahan buah di rumah kaca dengan *Unmanned Aerial Vehicle* (UAV, pesawat nirawak). Kasusnya adalah kompetisi UAV pada konferensi ICUAS 2024. Tujuannya mencacah satu jenis buah pada bedeng yang sudah ditentukan, mulai dan kembali ke titik awal dalam waktu sesingkat mungkin. Penilaian memakai akurasi hitungan dan waktu tempuh.

Data berasal dari simulasi di Gazebo dengan ROS Noetic. Rumah kaca simulasi berukuran 20x27x8 m, berisi sembilan rak dengan tiga bedeng per rak (27 bedeng), dan tiap bedeng memuat sampai tiga tanaman. UAV adalah *quadrotor* Kopterworx Eagle dengan kamera RGB-D simulasi menghadap depan. Pemberi label dan pembagian latih/uji tidak disebut, karena metodenya tidak melatih model.

Metode terdiri atas dua bagian. Pertama, rute kunjungan dirumuskan sebagai *Traveling Salesman Problem* (TSP, mencari urutan kunjungan terpendek) dan diselesaikan dengan *Simulated Annealing* (pencarian acak yang kadang menerima solusi lebih buruk untuk keluar dari minimum lokal). Tiap bedeng dicitrakan dari depan dan belakang, sehingga n bedeng memerlukan 2n pengamatan. Kedua, pengolahan citra digital: ambang jarak 3 m dari *depth*, deteksi persegi putih tempat tanaman, penyaringan warna dalam ruang HSV, pembelahan wilayah yang terlalu besar, lalu pencocokan buah pada citra depan dan belakang untuk mencegah hitung ganda.

Pada rute tanpa pengambilan citra, selisih waktu perkiraan dan waktu nyata berkisar 0,65% sampai 14,39% dalam sepuluh simulasi (Tabel I). Pengolahan citra diuji pada 60 bedeng berisi paprika dalam sepuluh lingkungan dan mencapai akurasi di atas 86,67%. Evaluasi seluruh metode memakai 25 skenario untuk paprika, terong, dan tomat (75 simulasi), dengan 8 pencilan. Selisih persentase hitungan disajikan sebagai *box plot*; nilai rata-ratanya tidak disebut.

Keterbatasannya: seluruh evaluasi berupa simulasi, tanpa data lapangan. Ambang warna ditetapkan dari citra uji sendiri. Acuan hitung benar tidak dijelaskan rinci. Tidak ada pembanding metode lain. Penulis mengaitkan kesalahan dengan ketelitian UAV saat memotret.
