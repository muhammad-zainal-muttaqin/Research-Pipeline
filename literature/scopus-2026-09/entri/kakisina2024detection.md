# DETECTION AND SEQUENCE OF COLLECTING LOOSE OIL PALM FRUIT USING DEEP LEARNING TECHNIQUE

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kakisina2024detection` |
| Judul asli | DETECTION AND SEQUENCE OF COLLECTING LOOSE OIL PALM FRUIT USING DEEP LEARNING TECHNIQUE |
| Penulis | Kakisina, Sheila E.; Mokombombang, Novy N. R. A.; Indrabayu |
| Tahun | 2024 |
| Venue | Iet Conference Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kakisina2024detection.pdf](../pdf/kakisina2024detection.pdf)
- DOI resmi: https://doi.org/10.1049/icp.2025.0302

## Gambaran Umum

Makalah konferensi ini (IET Conference Proceedings 2024) memakai YOLOv7 untuk mendeteksi brondolan, yaitu buah sawit yang lepas dan jatuh ke tanah, bagi robot pemungut otomatis. PDF yang tersedia adalah versi naskah tertelaah (*reviewed manuscript*), bukan PDF penerbit.

Data berupa 839 citra GoPro Hero11 beresolusi 5568×4872 piksel yang diambil di kebun sawit di Mamuju, Sulawesi Barat, saat pemungutan brondolan. Citra diubah ke 640×640, dilabeli, diperbanyak dengan augmentasi, lalu dibagi menjadi data latih, validasi, dan uji. Dua set hiperparameter (jangkar, laju belajar, dan *weight decay*) dibandingkan.

Set A memberi mAP50 0,866 dan set B 0,823. Set A lebih baik pada akurasi deteksi dan presisi, sedangkan set B sedikit lebih baik pada ketepatan kotak. Urutan pungut ditentukan dari koordinat y kotak pada citra 640×640, yang disimpan ke berkas teks untuk robot.

Brondolan tidak dicacah. Urutan pungut tidak dievaluasi dengan robot atau dengan ukuran kinerja tersendiri.
