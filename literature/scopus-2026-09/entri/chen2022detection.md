# Detection of Oil Palm Fresh Fruit Bunches (FFBS) with Computer Vision Models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2022detection` |
| Judul asli | Detection of Oil Palm Fresh Fruit Bunches (FFBS) with Computer Vision Models |
| Penulis | Chen, Zhiyuan; Elsaid, Salma; Sim, Doreen Ying Ying; Maul, Tomas; Liao, Iman Yi |
| Tahun | 2022 |
| Venue | Proceedings 2022 International Conference on Mechanical Automation and Electrical Engineering Cmaee 2022 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [chen2022detection.pdf](../pdf/chen2022detection.pdf)
- DOI resmi: https://doi.org/10.1109/cmaee58250.2022.00023

## Gambaran Umum

Makalah ini membandingkan empat model deteksi objek untuk tandan buah segar (TBS) kelapa sawit pada citra. Empat model itu adalah SVM dengan HOG, Faster R-CNN, YOLOv4, dan YOLOv5. Citra dikumpulkan dari Google dan Kaggle, lalu diberi prapemrosesan sebelum pelatihan dan pengujian.

Pengujian mengukur mAP, presisi, recall, dan skor F1. Hasilnya, SVM dengan HOG memperoleh mAP terendah, 89%. YOLOv4 memperoleh mAP tertinggi, 98,5%, dengan kecepatan deteksi 31,8 ms. YOLOv5 memperoleh mAP 96,4% dengan kecepatan 11,4 ms.

Penulis memilih YOLOv5 sebagai pilihan terbaik karena kecepatannya dinilai cocok untuk deteksi waktu nyata. Selisih akurasi dengan YOLOv4 dinilai kecil. Uji di kebun kelapa sawit belum dilakukan, dan makalah menyebut itu sebagai pekerjaan berikutnya.

Dari sisi tinjauan ini, makalah berada pada tingkat deteksi per citra untuk satu kelas objek. Makalah tidak mencacah buah dari beberapa pandang, tidak melacak buah antarbingkai, dan tidak memakai depth atau 3D. Ia relevan sebagai pembanding deteksi TBS, bukan sebagai bukti deduplikasi lintas pandang.

Makalah juga memuat ketidakkonsistenan internal pada waktu pelatihan. Teks menyebut Faster R-CNN 23 menit 51 detik, YOLOv4 3 jam 46 menit, dan YOLOv5 14 menit 59 detik. Tabel III mencatat 23 menit 51 detik, 3 jam 46 menit, dan 15 menit 36 detik untuk YOLOv5. Angka waktu latih YOLOv5 perlu diperiksa sebelum dikutip.
