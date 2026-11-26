# A Streamlined Deep Learning Framework for Vineyard Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `santhi2026streamlined` |
| Judul asli | A Streamlined Deep Learning Framework for Vineyard Yield Estimation |
| Penulis | Santhi, P.; Shaik, Aisha Suleiman; Meenakshi, Yemineni; Kadiyala, Komali; Pandipati, Suman; Lakshmi, V. |
| Tahun | 2026 |
| Venue | Proceedings of the 4th IEEE International Conference on Interdisciplinary Approaches in Technology and Management for Social Innovation Iatmsi 2026 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [santhi2026streamlined.pdf](../pdf/santhi2026streamlined.pdf)
- DOI resmi: https://doi.org/10.1109/iatmsi68868.2026.11465914

## Gambaran Umum

Makalah konferensi ini (IATMSI 2026) mengusulkan alur estimasi hasil anggur tanpa sensor mahal. Tahapnya adalah praproses citra, deteksi tandan, dan perkiraan jumlah buah anggur per tandan. PDF yang tersedia berupa pindaian halaman, sehingga teksnya dibaca dengan OCR.

Semua percobaan memakai WGISD, set data citra RGB kebun anggur. Citra diperbaiki dengan CLAHE dan penghilangan derau, lalu tandan dideteksi dengan Faster R-CNN (ResNet-50 dan FPN). Jumlah buah anggur per tandan diperkirakan dari potongan citra tandan dengan regresi CNN yang dilatih dengan *Huber loss*. Model ketiga, MINN, menggabungkan fitur visual dan fitur numerik tandan. YOLOv8 dipakai sebagai pembanding.

Akurasi deteksi Faster R-CNN 94,7%, YOLOv8 mencapai mAP@50 89,1%, dan MINN mencapai akurasi 95,8% dengan F1 95,5%. Matriks galat MINN memakai kelas hasil rendah, sedang, dan tinggi.

Pelacakan SORT disebut untuk mencegah hitung ganda, tetapi WGISD berupa citra lepas dan pelacakan tidak dievaluasi. MAE hitungan buah anggur didefinisikan, tetapi nilainya tidak dilaporkan. Penulis menyatakan bahwa ablasi praproses tidak dilakukan secara lengkap.
