# Detection of Banana and Counting using One-Stage and Transformer-based Object Detection Models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `goes2026detection` |
| Judul asli | Detection of Banana and Counting using One-Stage and Transformer-based Object Detection Models |
| Penulis | Goes, Sahil; Coelho, Vollny; Arabekar, Rudresh; Sawant, Anant; Sawant, Kedar; Dharwadkar, Tanvi |
| Tahun | 2026 |
| Venue | 7th International Conference on Inventive Research in Computing Applications Icirca 2026 Proceedings |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | banana |

## Tautan Akses
- PDF: [goes2026detection.pdf](../pdf/goes2026detection.pdf)
- DOI resmi: https://doi.org/10.1109/icirca69024.2026.11570262

## Gambaran Umum

Kajian ini (ICIRCA 2026) membandingkan RF-DETR Small, YOLOv11-Fast, dan YOLOv26-Fast untuk mendeteksi dan mencacah buah pisang per citra. Objek yang dihitung adalah setiap buah dalam sisir atau tandan.

Data berupa 938 foto ponsel (iPhone 11 dan Samsung M31) dari kebun dan pasar di Goa, India. Citra diambil dari berbagai jarak, sudut, pencahayaan, dan tingkat ketertutupan. Isinya mencakup buah tunggal dan tandan pada beberapa tahap kematangan, tetapi semua buah dilabeli dalam satu kelas. Label dibuat dengan bantuan SAM lalu diperiksa manual. Data dibagi 80:10:10.

Hitungan per citra adalah jumlah kotak terdeteksi. Pada data uji, RF-DETR memberi MAE 0,17 dan hitungan tepat pada 87,23% citra. YOLOv26 memberi MAE 0,43 dan 73,40%, sedangkan YOLOv11 memberi MAE 1,52 dan 27,65%. Penulis mengaitkan galat YOLOv11 dengan buah yang berdempetan di tandan padat.

Setiap citra dicacah sendiri. Citra pasar dan citra kebun tidak dipisah dalam pelaporan hasil.
