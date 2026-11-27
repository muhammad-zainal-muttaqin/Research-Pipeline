# Automated Pineapple Fruit Detection and Counting System Using Machine Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mejiashernandez2026automated` |
| Judul asli | Automated Pineapple Fruit Detection and Counting System Using Machine Learning |
| Penulis | Mej\'\ias--Hern\'andez, Diana; Leit\'on--Jim\'enez, Jason; Chavarr\'\ia--Zamora, Luis; Barboza--Artavia, Luis |
| Tahun | 2026 |
| Venue | Lecture Notes in Networks and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pineapple |

## Tautan Akses
- PDF: [mejiashernandez2026automated.pdf](../pdf/mejiashernandez2026automated.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-032-29558-3_3

## Gambaran Umum

Makalah konferensi ini (Lecture Notes in Networks and Systems, 2026) membangun sistem deteksi dan pencacahan buah nanas pada ortomosaik UAV, yaitu citra udara yang disatukan dari banyak foto. Fokusnya buah tahap awal yang kecil dan mudah terlewat.

Data latih dibuat di Roboflow dari potongan ortomosaik, diperbanyak dengan augmentasi, dan dibagi 70:15:15. Data diperluas lewat putaran pembelajaran aktif: kesalahan deteksi dianalisis, citra yang sulit dilabeli ulang, lalu model dilatih kembali. Citra diperbaiki dengan tapis super-resolusi, dan beberapa model YOLOv8 digabung.

Ortomosaik dipotong menjadi petak 1280×1280 piksel. Setelah inferensi, kotak dari setiap petak dipetakan kembali ke koordinat ortomosaik. Kotak yang terdeteksi dua kali di batas petak atau oleh beberapa model digabung dengan aturan toleransi piksel dan penggabungan skor keyakinan. Gabungan model mencapai mAP@0,5 di atas 92%. Pada ortomosaik "Lote Cerro", jumlah deteksi naik dari 36.852 menjadi 84.202 (128%) dibandingkan dengan model awal.

Jumlah deteksi tidak dibandingkan dengan hitungan lapangan, sehingga kenaikan 128% belum menunjukkan berapa yang benar dan berapa yang deteksi palsu. Penyaringan duplikat bekerja di bidang ortomosaik dan bergantung pada kualitas penyatuan citra.
