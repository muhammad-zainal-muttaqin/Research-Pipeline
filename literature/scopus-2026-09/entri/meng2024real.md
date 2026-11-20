# Real-time statistical algorithm for cherry tomatoes with different ripeness based on depth information mapping

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `meng2024real` |
| Judul asli | Real-time statistical algorithm for cherry tomatoes with different ripeness based on depth information mapping |
| Penulis | Meng, Zhichao; Du, Xiaoqiang; Xia, Jingyuan; Ma, Zenghong; Zhang, Tianxue |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [meng2024real.pdf](../pdf/meng2024real.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.108900

## Gambaran Umum

Kajian ini membahas penghitungan tomat ceri di rumah kaca dengan dua kamera Intel RealSense D435 yang dipasang untuk merekam tanaman dari dua sisi. Masalah utamanya adalah satu buah dapat terlihat di lebih dari satu frame dan di lebih dari satu kamera, sehingga penghitungan langsung per frame akan menghitung buah yang sama berkali-kali. Penulis menyelesaikannya dengan tiga lapis: penyambungan dua citra menjadi satu, deteksi buah dengan YOLO yang diperkuat modul perhatian SimAM, dan pelacakan antarframe dengan DeepSORT.

Citra dari kedua kamera berukuran 480 × 640 piksel pada 30 FPS. Kedua citra digabung dengan offset tetap 470 piksel: bagian yang sama pada dua kamera ditentukan dari posisi pemasangan dan tidak dihitung ulang per frame. Dataset latih berisi 826 citra dan dataset uji 204 citra. Untuk evaluasi lintas waktu, penulis memakai video dengan 184 tomat mentah, 30 setengah matang, dan 48 matang. Tahap pelacakan memakai DeepSORT, yang mencocokkan buah antarframe dengan dua sinyal: fitur tampilan dari jaringan ReID (MobileNeXt) dan prediksi posisi dari filter Kalman. Kombinasi ini dipakai untuk menentukan apakah sebuah deteksi adalah buah yang sudah tercatat atau buah baru.

Pada bagian eksperimen, penulis melaporkan kontribusi tiap komponen secara terpisah. Penambahan informasi depth menaikkan mAP sekitar 3 persen. Operasi morfologi (closing dan dilation) pada hasil segmentasi menambah sekitar 2,5 persen. Modul SimAM pada YOLO v7-tiny mencapai 87,3 persen. Angka-angka ini berasal dari ablasi di dataset penulis sendiri, sehingga tidak dapat dibandingkan langsung dengan dataset sawit atau dengan detektor lain tanpa protokol yang sama.

Penulis menyimpulkan bahwa hasil ablasi memberi bukti kuat bagi perbaikan yang diusulkan dan berhasil menyelesaikan tugas statistik (penghitungan) tomat ceri. Kesimpulan itu perlu dibaca bersama batasannya: kamera hanya dua unit, lingkungan rumah kaca dengan pencahayaan yang relatif terkendali, dan objek berupa tomat ceri, bukan tandan dengan kelas kematangan yang saling mirip. Kajian ini tidak mengukur akurasi penghitungan akhir per tanaman pada data yang tidak dipakai melatih detektor.
