# DanceTrack: Multi-Object Tracking in Uniform Appearance and Diverse Motion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2022dancetrack` |
| Judul asli | DanceTrack: Multi-Object Tracking in Uniform Appearance and Diverse Motion |
| Penulis | Sun, Peize; Cao, Jinkun; Jiang, Yi; Yuan, Zehuan; Bai, Song; Kitani, Kris; Luo, Ping |
| Tahun | 2022 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [sun2022dancetrack.pdf](../pdf/sun2022dancetrack.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr52688.2022.02032

## Gambaran Umum

Artikel ini memperkenalkan DanceTrack, kumpulan data untuk pelacakan banyak orang (*multi-object tracking*, MOT) dengan penampilan seragam dan gerak yang beragam. Masalah yang diangkat adalah ketergantungan metode MOT pada pencocokan penampilan melalui identifikasi ulang (*re-ID*). Alur deteksi lalu re-ID bekerja baik pada kumpulan data lama karena objek di sana biasanya memiliki penampilan yang mudah dibedakan dan gerak yang teratur. Penulis menyatakan bahwa asumsi tersebut tidak berlaku pada adegan seperti tari kelompok, ketika semua penari memakai pakaian serupa, sehingga metode yang ada gagal. Penelitian ini menekankan bahwa pelacakan harus tetap bekerja ketika penampilan tidak cukup diskriminatif.

Kumpulan data berisi lebih dari 100.000 frame dari 100 video, sekitar sepuluh kali lipat MOT17, dengan pembagian 40 video latih, 25 video validasi, dan 35 video uji. Video sebagian besar menampilkan tari kelompok dan senam ritmik. Anotasi berupa kotak pembatas dan identitas; untuk objek yang tertutup sebagian dicatat kotak tubuh penuh, sedangkan objek yang tertutup sepenuhnya tidak dianotasi dan mempertahankan identitasnya saat muncul kembali. Metrik utama adalah HOTA, dilengkapi AssA dan IDF1 untuk kualitas asosiasi serta DetA dan MOTA untuk kualitas deteksi, ditambah FP, FN, dan ID switch.

Mekanisme analitisnya memisahkan pengaruh petunjuk penampilan, IoU, dan gerak. Penulis menjalankan percobaan oracle memakai kotak sebenarnya, lalu menguji berbagai kombinasi petunjuk pada MOT17 dan DanceTrack. Visualisasi fitur t-SNE menunjukkan fitur penampilan antarobjek mudah dibedakan pada MOT17, tetapi saling tumpang tindih pada DanceTrack. Dari analisis itu, penulis menyimpulkan tiga hal: representasi halus seperti segmentasi dan pose lebih baik daripada kotak pembatas kasar, informasi kedalaman berpengaruh positif pada asosiasi meski tugasnya dua dimensi, dan pemodelan dinamika temporal penting.

Angka hasil menunjukkan penurunan tajam kinerja asosiasi. Pada percobaan oracle dengan kotak sebenarnya, pencocokan IoU saja menghasilkan HOTA 98,1 pada MOT17 tetapi hanya 72,8 pada DanceTrack; AssA turun dari 97,3 menjadi 53,6 dan IDF1 dari 97,8 menjadi 63,5. Menambahkan penampilan justru menurunkan angka, dengan HOTA 59,7 pada DanceTrack. Pada perbandingan metode dengan deteksi privat, QDTrack mencatat HOTA 54,2 pada DanceTrack dibandingkan 53,9 pada MOT17, CenterTrack 41,8 dibandingkan 52,2, dan FairMOT 39,7 dibandingkan 59,3. Meskipun demikian, MOTA dan DetA justru lebih tinggi pada DanceTrack, misalnya CenterTrack mencatat MOTA 86,8 pada DanceTrack dibandingkan 67,8 pada MOT17, yang menunjukkan bahwa hambatan terletak pada asosiasi, bukan deteksi.

Batasan yang dinyatakan penulis ada dua. Pertama, artikel ini tidak mengusulkan algoritme yang secara jelas mengungguli metode sebelumnya dan menjadikannya pertanyaan terbuka untuk penelitian berikutnya. Kedua, karena keterbatasan waktu dan sumber daya, kumpulan data hanya menyediakan anotasi kotak pembatas pada versi ini, tanpa anotasi pose manusia atau topeng segmentasi yang diperlukan untuk kajian lebih rinci pada kasus yang ditekankan.
