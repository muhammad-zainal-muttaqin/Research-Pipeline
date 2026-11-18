# ByteTrack: Multi-object Tracking by Associating Every Detection Box

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022bytetrack` |
| Judul asli | ByteTrack: Multi-object Tracking by Associating Every Detection Box |
| Penulis | Zhang, Yifu; Sun, Peize; Jiang, Yi; Yu, Dongdong; Weng, Fucheng; Yuan, Zehuan; Luo, Ping; Liu, Wenyu; Wang, Xinggang |
| Tahun | 2022 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhang2022bytetrack.pdf](../pdf/zhang2022bytetrack.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-20047-2_1

## Gambaran Umum

Artikel ini mengusulkan BYTE, metode asosiasi untuk pelacakan banyak objek (*multi-object tracking*, MOT), dan ByteTrack, pelacak yang dibangun di atasnya. Masalah utamanya adalah sebagian besar metode hanya mengaitkan kotak deteksi dengan skor keyakinan di atas suatu ambang, lalu membuang kotak berskor rendah. Objek yang tertutup sebagian sering memiliki skor rendah, sehingga pembuangan itu menyebabkan objek hilang dan lintasan terputus. Penulis berpendapat bahwa kotak berskor rendah tetap perlu diperiksa karena kesamaan dengan lintasan dapat membedakan objek sebenarnya dari latar belakang.

Objek yang dilacak adalah objek pada kumpulan data visi komputer, bukan tanaman. Metode diuji pada MOT17, MOT20, HiEve, dan BDD100K dengan protokol deteksi privat. ByteTrack memakai detektor YOLOX dengan tulang punggung YOLOX-X yang diinisialisasi dari bobot COCO, lalu mengikatnya dengan BYTE. Metrik yang dilaporkan mencakup MOTA, IDF1, HOTA, ID switch, serta mMOTA dan mIDF1 untuk BDD100K. Pelatihan dilakukan pada delapan GPU Tesla V100 dengan ukuran citra 1440×800 dan augumentasi Mosaic serta Mixup.

Mekanisme BYTE terdiri dari dua tahap asosiasi. Tahap pertama mencocokkan kotak berskor tinggi dengan lintasan memakai kemiripan gerak dari Kalman Filter atau kemiripan penampilan, dengan IoU maupun jarak fitur Re-ID. Tahap kedua mencocokkan lintasan yang belum tertaut dengan kotak berskor rendah memakai kemiripan gerak yang sama. Kotak berskor rendah yang cocok dengan suatu lintasan memulihkan objek yang tertutup, sedangkan kotak tanpa lintasan yang cocok dibuang sebagai latar belakang. Ambang skor baku adalah 0,6, pencocokan ditolak bila IoU di bawah 0,2, dan lintasan yang hilang disimpan selama 30 frame.

Angka hasil menunjukkan perbaikan yang konsisten. Ketika BYTE diterapkan pada sembilan pelacak mutakhir, skor IDF1 naik antara 1 dan 10 poin; misalnya pada CenterTrack, MOTA naik dari 66,1 menjadi 67,4, IDF1 dari 64,2 menjadi 74,0, dan ID switch turun dari 528 menjadi 144 pada bagian validasi MOT17. Dibandingkan SORT, BYTE menaikkan MOTA dari 74,6 menjadi 76,6 dan IDF1 dari 76,9 menjadi 79,3 serta menurunkan ID switch dari 291 menjadi 159. ByteTrack mencatat 80,3 MOTA, 77,3 IDF1, dan 63,1 HOTA pada uji MOT17 dengan kecepatan 30 FPS pada satu GPU V100. Pada MOT20, angkanya 77,8 MOTA, 75,2 IDF1, dan 61,3 HOTA. Penulis melaporkan pula kinerja mutakhir pada HiEve dan BDD100K.

Batasan penulis tidak dinyatakan secara eksplisit dalam bagian tersendiri. Penulis mencatat sejumlah kondisi dari hasil percobaan: fitur Re-ID tidak andal untuk kotak berskor rendah karena oklusi parah atau kabur gerak, sehingga tahap kedua memakai IoU; pada oklusi berat, fitur Re-ID rentan menyebabkan peralihan identitas, sementara model gerak lebih stabil; dan pada BDD100K, pergerakan kamera besar serta anotasi berlaju frame rendah membuat petunjuk gerak gagal, sehingga Re-ID lebih baik pada tahap pertama.

