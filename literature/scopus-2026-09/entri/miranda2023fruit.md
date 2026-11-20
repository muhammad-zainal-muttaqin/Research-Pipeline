# Fruit sizing using AI: A review of methods and challenges

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `miranda2023fruit` |
| Judul asli | Fruit sizing using AI: A review of methods and challenges |
| Penulis | Miranda, Juan C.; Gen\'e-Mola, Jordi; Zude-Sasse, Manuela; Tsoulias, Nikos; Escol\`a, Alexandre; Arn\'o, Jaume; Rosell-Polo, Joan R.; Sanz-Cortiella, Ricardo; Mart\'\inez-Casasnovas, Jos\'e A.; Gregorio, Eduard |
| Tahun | 2023 |
| Venue | Postharvest Biology and Technology |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple, citrus, mango, grape |

## Tautan Akses
- PDF: [miranda2023fruit.pdf](../pdf/miranda2023fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.postharvbio.2023.112587

## Gambaran Umum

Kajian ini (Miranda dkk., 2023) meninjau penerapan *deep learning* pada pencitraan buah: deteksi, penghitungan, segmentasi, dan pengukuran ukuran buah. Menurut abstrak, jaringan saraf konvolusi (*convolutional neural network*, CNN) dalam lima tahun terakhir menjadi metode standar untuk deteksi buah otomatis, dengan skor F1 di atas 90 % dan kecepatan proses mendekati waktu nyata. Abstrak juga menyebut galat rerata absolut (*mean absolute error*, MAE) di bawah 4 mm pada buah apel.

Bagian hasil membandingkan detektor satu tahap dan dua tahap, segmentasi semantik, dan segmentasi instans. Fusi RGB-D (citra warna dengan kanal kedalaman) menaikkan F1 sekitar 4,46 % pada apel dengan Faster R-CNN. Pada tabel perbandingan, F1 berkisar dari 0,910 (RGB) sampai 0,934 (RGB-D, NT-FFN). Penulis menyatakan bahwa F1 adalah metrik yang paling umum, dan bahwa hasil dari struktur dan kumpulan data berbeda tidak dapat dibandingkan langsung.

Kesimpulan menyebut bidang ini masih terbuka. Penghitungan dan pengukuran manual disebut mahal dalam waktu dan tenaga kerja, sedangkan penghitungan otomatis dinilai makin layak. Kemajuan berikutnya bergantung pada kumpulan data yang besar dan berkualitas tinggi.
