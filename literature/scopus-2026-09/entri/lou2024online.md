# Online target detection and fast localisation of citrus fruits in irregularly disturbed state

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lou2024online` |
| Judul asli | Online target detection and fast localisation of citrus fruits in irregularly disturbed state |
| Penulis | Lou, H.; others |
| Tahun | 2024 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [lou2024online.pdf](../pdf/lou2024online.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202404120

## Gambaran Umum

Kajian ini membahas robot pemetik jeruk yang bekerja terus-menerus. Buah yang belum dipetik bergoyang tak beraturan akibat angin, gerakan robot, dan perubahan beban ranting. Buah yang bergoyang sulit dideteksi dan dilokalisasi secara daring. Cara yang lazim menurut penulis adalah menunggu buah diam sebelum pengenalan dan pemetikan berikutnya, sehingga efisiensi pemetikan turun. Penulis mengusulkan deteksi dan pelacakan buah bergoyang, lalu memprediksi posisi saat buah diam dari lintasan geraknya dalam waktu singkat.

Data deteksi berjumlah 971 citra jeruk di pohon. Sebanyak 721 citra diambil dengan telepon genggam dan kamera pada hari cerah dan berawan dari berbagai sudut, 30 citra berasal dari internet, dan 220 citra dipotong dari video. Citra dibagi 8:2 menjadi data latih dan data validasi. Kelas yang diberi label adalah "orange" (tanpa penghalang) dan "branch" (terhalang), memakai LabelImg. Data video terdiri atas 21 rekaman jeruk goyang yang dipetik acak oleh manusia untuk menirukan gangguan, diambil dari jarak sekitar 30 sampai 60 cm. Tujuh video melatih jaringan fitur pelacak, 3 video menjadi data uji, dan 11 video menjadi data evaluasi prediksi posisi. Label video dibuat dengan DarkLabel 2.4. Jumlah pohon dan jumlah buah tidak disebut.

Detektor adalah YOLOv5s yang diperbaiki dengan modul perhatian CBAM (*convolutional block attention module*, pemberi bobot pada kanal dan lokasi fitur) dan fungsi kerugian SIoU (*scalable intersection over union*, penyesuai arah antara kotak prediksi dan kotak acuan). Pelacak adalah DeepSORT, yaitu pelacak berbasis gerak dan kemiripan tampilan. Jaringan ReID (*re-identification*, pengenal ulang objek antarbingkai) di dalamnya diperbaiki. Penghitung bingkai pelacakan per buah memilih target dengan lintasan terbaik. Posisi buah diam diprediksi dari titik tengah empat titik ekstrem lintasan pada bidang gambar (atas, bawah, kiri, kanan) dan titik tengah jarak terdekat dan terjauh dari kamera stereo ZED 2i. Kamera kedalaman membatasi pelacakan pada jeruk dalam jarak petik dan paling banyak 3 target.

Detektor yang diperbaiki mencapai presisi 96,5%, recall 88,7%, dan mAP 93,3% pada data validasi, naik 3,9, 1,6, dan 1,1 poin persentase dari YOLOv5s awal, dengan 69,3 bingkai per detik. Pada tiga video uji, rerata MOTA (*multi-object tracking accuracy*) naik dari 59,4% menjadi 68,6% dan MOTP (*multi-object tracking precision*) dari 78,5% menjadi 83,9% setelah ReID diperbaiki. Pergantian identitas (IDSW) turun dari 78 menjadi 46 kali. Akurasi rerata prediksi posisi pada lima video adalah 21,3%, 53,0%, 81,9%, 83,7%, 86,1%, dan 94,9% untuk waktu prediksi 1, 2, 3, 5, 7, dan 10 detik. Pada uji ambil di laboratorium dengan jeruk pot yang digoyang sekitar 10 cm, waktu ambil rerata turun dari 18,4 detik menjadi 12,8 detik (30,4%).

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Data citra tidak punya data uji terpisah, hanya pembagian latih dan validasi 8:2, dan pembagian per pohon tidak disebut. Gangguan pada video dibuat dengan pemetikan acak oleh manusia, bukan gangguan alami di kebun. Uji ambil dilakukan dalam ruangan dengan jeruk pot. Tidak ada pencacahan buah, dan pelacakan dipakai untuk lokalisasi, sehingga metrik hitung tidak dilaporkan. Jumlah video uji pelacakan hanya 3 dan jumlah video evaluasi prediksi 5, sehingga ketidakpastian hasil tidak dapat dinilai dari teks.
