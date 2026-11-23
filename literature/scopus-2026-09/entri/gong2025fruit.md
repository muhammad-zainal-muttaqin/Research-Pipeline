# Fruit Detection Methods Based on Deep Learning in Agricultural Planting: A Systematic Literature Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gong2025fruit` |
| Judul asli | Fruit Detection Methods Based on Deep Learning in Agricultural Planting: A Systematic Literature Review |
| Penulis | Gong, Xinyu; Wu, Qiufeng |
| Tahun | 2025 |
| Venue | IEEE Access |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [gong2025fruit.pdf](../pdf/gong2025fruit.pdf)
- DOI resmi: https://doi.org/10.1109/access.2025.3573364

## Gambaran Umum

Gong dan Wu menyusun tinjauan pustaka sistematis tentang deteksi buah berbasis *deep learning* di lahan tanam. Masalah yang disebut penulis adalah kesenjangan antara target kebijakan otomasi pertanian dan penerapan di lapangan. Penulis membagi masalah itu menjadi empat skenario: sedikit data berlabel (*few-shot*, FS), adegan kompleks dengan oklusi dan cahaya berubah (CS), objek kecil (SO), dan deteksi waktu nyata (RS).

Pencarian memakai basis data Web of Science dan CNKI untuk periode 2018 sampai 2025. Kata kunci yang disebut adalah "deep learning", "agriculture", "object detection", "fruit", "computer vision", dan "recognition". Pencarian menghasilkan 148 publikasi. Penulis menyisihkan publikasi yang hanya membahas pencacahan buah, tidak memakai *deep learning*, atau tidak mengoptimalkan salah satu skenario. Hasil akhirnya 86 publikasi. Teks menyebut sebaran negara dan lima universitas teratas dalam Tabel 1 dan 2, tetapi isi tabel tidak terbaca pada teks.

Pengodean dilakukan per skenario. Untuk FS dibahas *meta-learning* dan augmentasi data. Untuk CS dibahas pembobotan ulang *focal loss* dan *non-maximum suppression* (NMS, penapis kotak tumpang tindih) adaptif. Untuk SO dibahas piramida fitur bertingkat dan perhatian koordinat. Untuk RS dibahas pencarian arsitektur saraf (NAS), distilasi pengetahuan, dan pemangkasan model.

Hasil dilaporkan sebagai ringkasan metode per skenario dengan angka dari kajian primer. Contohnya, kajian yang dirujuk melaporkan mAP@0,5 sebesar 96,3% pada YOLOv3 yang dimodifikasi dan 99,47% dengan 7,02 juta parameter pada model hasil distilasi. Angka tersebut berasal dari kajian lain dan tidak diperbandingkan pada satu data yang sama.

Keterbatasan yang dapat diperiksa dari teks: pencarian hanya memakai dua basis data dan tidak menyebut string pencarian lengkap, kriteria inklusi dan eksklusi tidak dinomori, dan tidak ada diagram alur penyaringan. Tinjauan ini tidak membahas asosiasi buah antar-pandang atau pencacahan lintas citra. Arah riset mendatang yang disebut adalah fusi multimodal (RGB, depth, termal, korelasi temporal), deteksi tahan derau label, dan sparsifikasi dinamis model besar.
