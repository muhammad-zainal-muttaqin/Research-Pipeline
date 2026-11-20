# Machine learning for automated oil palm fruit grading: The role of fuzzy C-means segmentation and textural features

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rosbi2024machine` |
| Judul asli | Machine learning for automated oil palm fruit grading: The role of fuzzy C-means segmentation and textural features |
| Penulis | Rosbi, Munirah; Omar, Zaid; Khairuddin, Uswah; Majeed, Anwar P.P.A.; Bakar, Syed A.R.S.A. |
| Tahun | 2024 |
| Venue | Smart Agricultural Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [rosbi2024machine.pdf](../pdf/rosbi2024machine.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2024.100691

## Gambaran Umum

Kajian ini bertujuan membangun sistem klasifikasi tandan buah segar (TBS) kelapa sawit dari citra luar ruang. Latar belakangnya adalah penyortiran manual yang lambat dan subjektif, serta kekurangan tenaga kerja yang membuat buah matang tidak terpanen dan produksi menurun. Penulis menilai sebagian besar penelitian dengan akurasi tinggi bergantung pada kumpulan data yang besar. Karena itu mereka mengusulkan pendekatan tradisional yang lebih sesuai untuk data terbatas, dengan penekanan pada praproses dan ekstraksi fitur.

Data terdiri atas 466 citra TBS yang diambil dengan kamera ponsel pintar memakai pengaturan otomatis bawaan. Citra diambil di tanah dan di pohon. Seorang penilai berpengalaman melabeli tingkat kematangan setiap citra. Kelas yang digunakan adalah rusak, kosong, belum matang, matang, dan terlalu matang. Sebanyak 95 citra disisihkan sebagai data uji, dan 371 citra dipakai untuk pelatihan lokalisasi YOLOv4-Tiny. Citra pelatihan itu dilipatgandakan enam kali melalui augmentasi, termasuk bayangan dan hujan sintetis, lalu diubah ukurannya menjadi 640 × 640 piksel.

Alur metode terdiri atas empat tahap. Pertama, TBS dilokalisasi dengan *bounding box* memakai YOLOv4-Tiny. Kedua, area TBS disegmentasi dengan *superpixel-based Fast Fuzzy C-means* (FFCM) untuk menghapus latar. Ketiga, fitur *colour moment* dan *opposite colour local binary pattern* (OCLBP) diekstrak. Keempat, fitur tersebut diklasifikasikan dengan *Multilayer Perceptron* (MLP). Hasil akhirnya adalah akurasi 93,68 persen dalam mengklasifikasikan tandan buah. Penulis menyatakan bahwa sistem ini mengatasi masalah pemanenan buah belum matang. Evaluasi juga memakai presisi, *recall*, spesifisitas, F1-score, *mean average precision* untuk lokalisasi, dan *intersection over union* untuk segmentasi. Tiga konfigurasi model dibandingkan dalam uji ablasi untuk melihat kontribusi segmentasi dan jenis fitur.

Penulis menyebut bahwa kondisi luar ruang, seperti pencahayaan yang berubah, bayangan, dan oklusi, dapat menurunkan kualitas segmentasi. Mereka juga menyebut kekurangan kumpulan data luar ruang yang konsisten sebagai alasan utama memilih metode semi-tradisional. Kesulitan lain yang disebut adalah kemiripan warna buah dengan latar, daun kering yang menyerupai duri buah, dan pengaruh keseimbangan putih dari cahaya alami.
