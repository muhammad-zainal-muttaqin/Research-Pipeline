# Fresh Fruit Bunch Detection Performance: A Comparative Evaluation of Training Strategies

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jailani2024fresh` |
| Judul asli | Fresh Fruit Bunch Detection Performance: A Comparative Evaluation of Training Strategies |
| Penulis | Jailani, Bayhaqi Mohd; Mustafa, Muhammad Farhan; Kadim, Zulaikha; Woon, Hon Hock; Chie, Lee Chia |
| Tahun | 2024 |
| Venue | Proceedings of the International Symposium on Intelligent Signal Processing and Communication Systems Ispacs |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [jailani2024fresh.pdf](../pdf/jailani2024fresh.pdf)
- DOI resmi: https://doi.org/10.1109/ispacs62486.2024.10867934

## Gambaran Umum

Penulis membandingkan empat cara melatih detektor YOLOv5s untuk buah sawit. Yang dinilai adalah waktu latih, memori GPU, dan akurasi deteksi. Masalah yang disebut: pelatihan detektor memakan daya hitung dan waktu, sedangkan penggabungan beberapa citra menjadi satu masukan belum banyak diteliti pada deteksi objek.

Data berupa 5.042 citra buah sawit di lingkungan kebun. Sebanyak 3.900 citra dipakai untuk latih, 900 untuk validasi, dan 242 untuk uji. Jenis tanaman selain sawit, lokasi kebun, sensor, jumlah buah, dan pemberi label tidak disebut. Himpunan validasi sama pada semua cara latih. Tidak ada penjelasan pembagian per pohon.

Empat cara latih memakai YOLOv5s selama 30 *epoch* (satu putaran penuh atas data latih) dengan laju belajar bawaan. Cara pertama memakai ukuran *batch* 1, cara kedua *batch* 32. Cara ketiga dan keempat menyusun setiap sembilan citra latih menjadi satu kisi 3x3 (433 citra gabungan) lalu melatih dengan *batch* 1 dan 32. Validasi memakai citra asli tanpa penggabungan. Metrik akurasi adalah skor F1, yaitu rerata harmonik presisi dan *recall*.

Waktu latih turun dari 2,936 jam menjadi 0,652 jam pada *batch* 1, dan dari 0,387 jam menjadi 0,097 jam pada *batch* 32. Skor F1 puncak turun dari 0,88 menjadi 0,57 pada *batch* 1, dan dari 0,85 menjadi 0,66 pada *batch* 32. Memori GPU hampir sama (1387 dan 1487 MiB; 6947 dan 6945 MiB). Teks dan tabel saling bertukar penempatan angka 1387 dan 1487 MiB.

Keterbatasan: mAP tidak dilaporkan dan F1 diambil dari himpunan validasi, bukan uji. Hanya satu kali jalan per cara tanpa ulangan atau selang kepercayaan. Hanya satu kelas objek (buah) dan tidak ada pencacahan. Klaim deteksi objek kecil yang lebih baik bersandar pada satu citra uji.
