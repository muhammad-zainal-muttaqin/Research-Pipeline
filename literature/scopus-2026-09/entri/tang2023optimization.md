# Optimization strategies of fruit detection to overcome the challenge of unstructured background in field orchard environment: a review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2023optimization` |
| Judul asli | Optimization strategies of fruit detection to overcome the challenge of unstructured background in field orchard environment: a review |
| Penulis | Tang, Yunchao; Qiu, Jiajun; Zhang, Yunqi; Wu, Dongxiao; Cao, Yuhong; Zhao, Kexin; Zhu, Lixue |
| Tahun | 2023 |
| Venue | Precision Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [tang2023optimization.pdf](../pdf/tang2023optimization.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-023-10009-9

## Gambaran Umum

Tinjauan ini membahas strategi optimasi untuk deteksi buah di kebun terbuka dengan latar belakang tidak terstruktur. Penulis menyebut tiga faktor latar yang menurunkan akurasi: kondisi cahaya, buah yang tertutup (oklusi), dan perbedaan tingkat kematangan. Penulis menyatakan bahwa tinjauan terdahulu hanya meringkas faktor ini secara singkat, dan menyebut makalah ini tinjauan pertama tentang strategi optimasi deteksi buah. Tujuannya membantu peneliti merancang strategi sendiri dan mencari sistem deteksi yang lebih murah dan lebih tahan terhadap gangguan.

Cakupan tinjauan: teks tidak menyebut jumlah kajian yang ditinjau, periode terbitan, basis data, kata kunci, kriteria inklusi, maupun diagram alir seleksi. Penulis hanya menyatakan telah menelaah berbagai kajian deteksi buah dan estimasi hasil "dalam beberapa tahun terakhir". Tanaman yang dibahas beragam: apel, jeruk, stroberi, mangga, kiwi, leci, anggur, ceri, tomat, paprika, dan lainnya. Kelapa sawit tidak dibahas.

Struktur tinjauan membagi strategi menjadi dua. Pertama, optimasi sebelum pengambilan citra: mengendalikan lingkungan (penanaman terstandar, pelindung cahaya, pengambilan malam hari dengan lampu), memilih sensor (kamera RGB-D, LiDAR, kamera termal, kamera multispektral), dan mengatur pose kamera. Pada bagian pose kamera, penulis membahas pengambilan citra dari beberapa sudut dengan kamera bergerak, rekonstruksi 3D dengan *structure from motion* (SfM, pemulihan struktur 3D dari urutan citra) yang dipadukan dengan segmentasi instans, pelacakan buah antarbingkai untuk mencegah hitung ganda, dan pesawat nirawak (UAV). Kedua, optimasi sesudah pengambilan citra: augmentasi dan sintesis data (termasuk ruang warna dan GAN), serta perbaikan jaringan, baik pada tulang punggung (*backbone*) maupun bagian non-*backbone* (kotak elips, penekanan fitur, IoU yang dimodifikasi).

Hasil ditampilkan sebagai dua tabel perbandingan nilai sebelum dan sesudah optimasi dari kajian terdahulu, tanpa sintesis angka lintas kajian. Contohnya YOLOv3-Litchi: mAP 0,6234 menjadi 0,7746 (leci); YOLO-Grape: F1 0,8315 menjadi 0,9047 dan mAP 0,8412 menjadi 0,9108 (anggur); dan YOLOv3-dense: F1 0,793 menjadi 0,817 (apel). Penulis menyimpulkan bahwa hasil uji membaik setelah metode perbaikan dipakai. Untuk pencacahan, teks menyatakan bahwa Chen dkk. (2019) memperoleh akurasi hitung stroberi 84,1% dari citra UAV, dan Gongal dkk. (2016) menyebut sekitar 60% apel terlihat dari satu sisi tajuk. Kedua angka dikutip dari kajian lain, bukan hasil tinjauan ini.

Keterbatasan yang dapat diperiksa dari teks: tidak ada metode pencarian dan seleksi, sehingga cakupan tidak dapat diulang. Perbandingan sebelum dan sesudah memakai data, metrik, dan ambang berbeda antarkajian, dan teks tidak menormalkannya. Tidak ada penilaian mutu bukti. Fokus tinjauan adalah deteksi, dan pencacahan lintas pandang hanya disinggung pada dua tempat (SfM dan pelacakan; UAV dan pelacakan di bagian prospek), tanpa membandingkan mekanisme asosiasi.
