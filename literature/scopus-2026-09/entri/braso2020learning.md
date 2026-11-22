# Learning a Neural Solver for Multiple Object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `braso2020learning` |
| Judul asli | Learning a Neural Solver for Multiple Object Tracking |
| Penulis | Bras\'o, Guillem; Leal-Taix\'e, Laura |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [braso2020learning.pdf](../pdf/braso2020learning.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr42600.2020.00628

## Gambaran Umum

Kajian ini mengatasi dikotomi dalam pelacakan banyak objek (*multi-object tracking*, MOT) berbasis graf. Penulis menyatakan bahwa penelitian sebelumnya terbagi antara pengoptimalan graf yang kompleks dengan biaya buatan tangan dan pembelajaran fitur pasangan dengan jaringan siam yang gagal menangkap informasi orde tinggi. Keduanya memisahkan pembelajaran biaya dari pengoptimalan akhir sehingga solver tidak dapat dilatih bersama. Penulis mengusulkan penyatuan keduanya dengan mempelajari solver secara langsung: alih-alih memprediksi biaya tepi lalu menjalankan solver graf, model memprediksi sendiri hasil akhir berupa partisi graf. Pengasosiasian data diperlakukan sebagai tugas klasifikasi tepi yang dapat dibedakan secara penuh (*fully differentiable*).

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer ke asosiasi lintas pandang. Data berasal dari benchmark MOTChallenge, yaitu 2D MOT 2015, MOT16, dan MOT17, yang memakai deteksi yang disediakan benchmark agar perbandingan adil. Encoder penampilan dilatih lebih dulu untuk identifikasi ulang pada tiga dataset eksternal, yaitu Market1501, CUHK03, dan DukeMTMC. Metrik yang dipakai mencakup MOTA dan IDF1 untuk cakupan objek serta pelestarian identitas, ditambah MT, ML, FP, FN, dan jumlah peralihan identitas (ID switches). Video diproses secara luring dalam kelompok 15 frame dengan 14 frame tumpang tindih.

Mekanisme intinya memanfaatkan formulasi *min-cost flow* klasik untuk MOT. Graf dibangun dengan simpul sebagai deteksi dan tepi menghubungkan setiap pasangan deteksi pada frame berbeda. Fitur simpul berupa penampilan dari CNN ResNet50 terlatih ImageNet dan identifikasi ulang, direduksi menjadi 256 lalu 32 dimensi; fitur tepi berupa posisi dan ukuran relatif, selisih waktu, serta jarak kosinus antarpenyematan penampilan, yang dipetakan oleh MLP. Jaringan *message passing* (MPN) menyebarkan informasi penampilan dan geometri ke seluruh graf. Penulis memperkenalkan pembaruan sadar-waktu yang mengagregasi tetangga masa lalu dan masa depan secara terpisah sebelum digabungkan, sesuai batasan konservasi aliran bahwa setiap simpul hanya boleh terhubung ke satu simpul di masa lalu dan satu di masa depan. Jumlah langkah *message passing* ditetapkan L = 12 karena kenaikan kinerja berhenti setelah dua belas langkah. Pelatihan memakai *binary cross-entropy* dengan pembobotan kelas aktif; pada inferensi, skor tepi diambang 0,5 dan pembulatan tamak atau program linear menghasilkan lintasan akhir.

Hasil ablasi menunjukkan desain tersebut terukur. Pembaruan sadar-waktu menghasilkan MOTA 64,0, IDF1 70,0, IDs 602, dan kepatuhan batasan 98,8%, dibanding pembaruan biasa yang memberi MOTA 63,0, IDF1 67,3, IDs 1.022, dan kepatuhan 82,1% (Tabel 1). Kombinasi fitur waktu, posisi, dan CNN mencapai MOTA 64,0 dan IDF1 70,0, sedangkan hanya selisih waktu memberi MOTA 58,8 dan IDF1 52,6 (Tabel 2). Pada benchmark, metode ini mencatat MOTA 51,5 dan IDF1 58,6 di 2D MOT 2015, MOTA 58,6 dan IDF1 61,7 di MOT16, serta MOTA 58,8 dan IDF1 61,7 di MOT17; peningkatan IDF1 berturut-turut 11, 6,4, dan 6,6 poin persentase dibanding metode sebelumnya (Tabel 3). Metode ini berjalan 35 fps untuk modelnya sendiri dan 6,5 fps setelah memasukkan waktu detektor, serta hingga satu orde lebih cepat daripada beberapa metode partisi graf. Seluruh angka bersumber dari tabel naskah dan bukan percobaan baru di luar kajian ini.

Batasan yang dinyatakan penulis mencakup ketergantungan pada deteksi dari benchmark dan praproses Tracktor, yang tidak dapat mengisi celah maupun memulihkan identitas melalui oklusi. Pemrosesan dilakukan secara luring per kelompok frame, dengan prediksi pada tepi yang tumpang tindih dirata-ratakan sebelum pembulatan; celah lintasan diisi oleh interpolasi bilinear sederhana. Penulis membekukan semua lapisan konvolusional karena pelatihan tambahan tidak memberi kenaikan bermakna namun menambah beban komputasi besar. Graf dipangkas hanya dengan hubungan tetangga terdekat saling timbal balik (K = 50), dan ambang batas skor tidak menjamin terpenuhinya batasan konservasi aliran sehingga prosedur pembulatan tetap diperlukan. Penggunaan dataset identifikasi ulang eksternal juga diakui sebagai praktik umum dalam MOT, bukan bagian dari benchmark itu sendiri.
