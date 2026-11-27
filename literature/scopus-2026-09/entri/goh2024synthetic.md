# Synthetic Data Generation for Fresh Fruit Bunch Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `goh2024synthetic` |
| Judul asli | Synthetic Data Generation for Fresh Fruit Bunch Ripeness Classification |
| Penulis | Goh, Jin Yu; Md Yunos, Yusri; Mohamed Ali, Mohamed Sultan |
| Tahun | 2024 |
| Venue | Communications in Computer and Information Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [goh2024synthetic.pdf](../pdf/goh2024synthetic.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-99-7240-1_22

## Gambaran Umum

Kajian ini (bab prosiding Springer, 2024) menguji apakah citra sintetis dapat menggantikan citra nyata untuk melatih detektor kematangan tandan buah segar (TBS) kelapa sawit.

Citra sintetis dibuat di Unity dengan paket Unity Perception. Model 3D tandan diberi tekstur, lalu posisi, pencahayaan, dan latar diacak (*domain randomisation*). Label kotak dibuat otomatis. Pembandingnya 150 citra nyata dari kebun sawit yang dilabeli tangan. YOLOv8 dilatih terpisah pada kedua jenis data dengan pembagian 80:10:10.

Dengan jumlah citra latih yang sama, mAP50 naik dari 0,533 (citra nyata) menjadi 0,96 (citra sintetis), dan mAP50–95 dari 0,219 menjadi 0,678. Dengan 30.000 citra sintetis, mAP50 validasi mencapai 0,995.

Teks tidak menyebut apakah model dari data sintetis dan model dari data nyata dinilai pada data validasi yang sama. Nilai yang hampir sempurna pada data sintetis dapat mencerminkan kemiripan data latih dan data validasi yang dibuat dengan cara yang sama. Tandan tidak dicacah.
