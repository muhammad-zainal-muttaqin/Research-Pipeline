# Oil Palm Loose Fruit Detection Using YOLOv4 for an Autonomous Mobile Robot Collector

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `japar2024oil` |
| Judul asli | Oil Palm Loose Fruit Detection Using YOLOv4 for an Autonomous Mobile Robot Collector |
| Penulis | Japar, Ahmed Fareed; Ramli, Hafiz Rashidi; Norsahperi, Nor Mohd Haziq; Hasan, Wan Zuha Wan |
| Tahun | 2024 |
| Venue | IEEE Access |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [japar2024oil.pdf](../pdf/japar2024oil.pdf)
- DOI resmi: https://doi.org/10.1109/access.2024.3446890

## Gambaran Umum

Makalah ini menguji detektor objek YOLOv4 untuk menghitung brondolan (*loose fruit*, LF) kelapa sawit dari citra video yang direkam oleh robot pengumpul otomatis. Brondolan adalah buah lepas yang jatuh ke tanah di sekitar pohon, berbeda dengan tandan buah segar (TBS) yang masih menempel di pohon. Penulis menggabungkan YOLOv4 dengan *tiling*, yaitu membagi setiap citra menjadi empat ubin persegi sebelum deteksi. Pada uji kasus oklusi, YOLOv4 mencapai F1 0,82. Pada hasil akhir, varian YOLOv4-SPP-Fast mencapai F1 91,4%, dibandingkan 86,3% untuk YOLOv4.

Makalah ini menyasar penghitungan brondolan di kebun untuk robot yang bergerak di antara baris pohon. Penulis menguji YOLOv4-Tiny sebagai varian yang lebih ringan, lalu membandingkannya dengan YOLOv4 pada kondisi yang sama.
Data dikumpulkan dari video 4K dan 1080p di 100 pohon dengan kondisi pencahayaan dan latar yang beragam. Penulis memberi label 1.021 citra dengan 14.872 brondolan, lalu memperbanyak data melalui augmentasi menjadi 6.719 citra. Pada tahap *tiling*, setiap citra dipecah menjadi empat ubin, deteksi dilakukan per ubin, dan jumlah deteksi dijumlahkan dalam koordinat global citra asal. Penghitungan dilakukan per citra. Makalah tidak menjelaskan cara menghubungkan deteksi yang sama antarcitra atau antarpandang, sehingga brondolan yang tampak di dua citra berurutan berpotensi terhitung lebih dari sekali.

Hasil uji menunjukkan YOLOv4-Tiny jauh lebih lemah daripada YOLOv4, dengan mAP pada kisaran 34 sampai 36%, sedangkan YOLOv4 pada data latih mencapai sekitar 80%. Pada kasus oklusi, YOLOv4 memberi presisi 0,974 dan recall 0,74. Varian YOLOv4-Tiling mencapai F1 0,747, YOLOv4-Tiny 0,358, dan YOLOv4-Tiny-Tiling 0,623. *Tiling* menaikkan F1 pada varian Tiny, tetapi varian SPP-Fast tetap yang tertinggi. Metrik dilaporkan per citra dengan presisi, recall, dan F1, bukan mAP pada split bersama, sehingga angka antarpenelitian tidak langsung dapat dibandingkan.

Penulis menyatakan bahwa ini studi pertama yang menggabungkan YOLO dengan *tiling* untuk brondolan. Robot ARLFC dengan dua webcam Logitech Brio diuji di kebun kelapa sawit. Keterbatasan yang disebut penulis mencakup panas GPU dan daya baterai sekitar empat jam. Makalah tidak menguji deduplikasi antarpandang.
