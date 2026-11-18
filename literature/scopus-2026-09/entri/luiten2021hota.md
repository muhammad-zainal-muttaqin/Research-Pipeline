# HOTA: A Higher Order Metric for Evaluating Multi-object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luiten2021hota` |
| Judul asli | HOTA: A Higher Order Metric for Evaluating Multi-object Tracking |
| Penulis | Luiten, Jonathon; Osep, Aljosa; Dendorfer, Patrick; Torr, Philip; Geiger, Andreas; Leal-Taix\'e, Laura; Leibe, Bastian |
| Tahun | 2021 |
| Venue | International Journal of Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [luiten2021hota.pdf](../pdf/luiten2021hota.pdf)
- DOI resmi: https://doi.org/10.1007/s11263-020-01375-2

## Gambaran Umum

Masalah utama adalah kesulitan mengevaluasi pelacakan multi-objek (*multi-object tracking*, MOT). Metrik yang ada memberi bobot berlebih pada salah satu aspek: MOTA sangat mengutamakan deteksi, sedangkan IDF1 mengutamakan asosiasi dan bersifat non-monoton terhadap deteksi. Keduanya juga tidak menyertakan akurasi lokalisasi dalam satu skor. Penelitian ini mengajukan HOTA (*Higher Order Tracking Accuracy*), metrik yang menyeimbangkan deteksi, asosiasi, dan lokalisasi dalam satu ukuran sekaligus dapat diuraikan menjadi sub-metrik untuk menganalisis tiap jenis galat. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Data uji adalah benchmark MOTChallenge MOT17 yang memuat 37 pelacak hasil publikasi dengan tinjauan sejawat per 1 April 2020. Untuk menguji kesesuaian dengan penilaian manusia, tujuh sekuens uji dipotong menjadi 36 klip berdurasi enam detik; 175 pelacak dievaluasi pada 108 kombinasi klip dan masukan deteksi, lalu 230 peserta — terdiri atas 62 peneliti MOT dan 122 peneliti visi komputer — melakukan 2.075 perbandingan berpasangan. Metode HOTA melakukan pencocokan bijektif antara deteksi kebenaran tanah dan deteksi prediksi memakai algoritma Hungaria, dengan ambang kemiripan lokalisasi α. Untuk setiap pasangan benar (*true positive*, TP), metrik ini menghitung asosiasi tingkat tinggi sepanjang seluruh video, bukan hanya satu langkah waktu seperti IDSW pada MOTA.

Mekanisme asosiasi memakai konsep baru: *true positive association* (TPA), *false negative association* (FNA), dan *false positive association* (FPA), yang dihitung untuk setiap TP. Skor asosiasi A(c) adalah Jaccard antara TP yang memiliki ID prediksi dan ID kebenaran tanah yang sama dengan TP tersebut. HOTA pada ambang α dirumuskan sebagai akar dari hasil kali skor akurasi deteksi DetA dan akurasi asosiasi AssA, yaitu HOTA_α = √(DetA_α · AssA_α), dengan DetA_α = |TP|/(|TP| + |FN| + |FP|) dan AssA_α = rata-rata A(c) atas seluruh TP. Skor akhir diperoleh dengan mengintegrasikan HOTA_α atas 19 nilai α dari 0,05 sampai 0,95 dengan langkah 0,05, sehingga lokalisasi ikut terukur. Sub-metrik turunannya mencakup DetA, AssA, LocA, DetRe, DetPr, AssRe, dan AssPr.

Hasil pada MOT17 menunjukkan MPNTrack17 menduduki peringkat pertama dengan HOTA 46,6, MOTA 55,7, IDF1 59,1, DetA 46,2, dan AssA 47,3; diikuti eTC17 dengan HOTA 45,1 serta Tracktor++v2 dengan HOTA 45,1 meskipun pelacak terakhir ini berperingkat pertama berdasarkan MOTA 56,3. Analisis korelasi pada 37 pelacak menunjukkan MOTA berkorelasi kuat dengan DetA (R² = 0,96) tetapi lemah dengan AssA (0,46), IDF1 sebaliknya (0,97 dengan AssA dan 0,58 dengan DetA), sedangkan HOTA berada di antara keduanya (0,67 dengan DetA dan 0,94 dengan AssA). Pada 175 pelacak, pengaruh galat deteksi terhadap MOTA rata-rata 98,6 kali pengaruh galat asosiasi, dan regresi MOTA terhadap MODA menghasilkan R² 99,4%. Dalam studi pengguna, HOTA sesuai dengan penilaian manusia 61,6% berbanding 38,4% untuk MOTA dan 72,0% berbanding 28,0% untuk IDF1; di kalangan peneliti MOT, angkanya masing-masing 79,3% dan 85,9%.

Batasan yang dinyatakan penulis ada dua. Pertama, HOTA kurang sesuai untuk pelacakan daring karena asosiasi diukur atas seluruh video sehingga skor suatu TP bergantung pada asosiasi di masa depan; penulis mengajukan varian *Online HOTA* sebagai penanganannya. Kedua, HOTA tidak memperhitungkan fragmentasi hasil pelacakan secara eksplisit, sehingga ditawarkan varian *fragmentation-aware* HOTA. Selain itu, perbandingan dengan Track-mAP tidak dilakukan karena metrik itu memerlukan skor keyakinan yang tidak disediakan MOTChallenge. Penulis tidak menyatakan batasan lain.

