# Detecting Ripeness of Oil Palm Fruit Using YOLO

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dahlan2026detecting` |
| Judul asli | Detecting Ripeness of Oil Palm Fruit Using YOLO |
| Penulis | Dahlan, Azlin Binti; Jasman, Wan Azra Sofea Batrisyia Binti; Ghazalli, Hajar Izzati Mohd |
| Tahun | 2026 |
| Venue | 2026 International Conference on Cognitive Systems and Computer Interaction Icosci 2026 Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [dahlan2026detecting.pdf](../pdf/dahlan2026detecting.pdf)
- DOI resmi: https://doi.org/10.1109/icosci66700.2026.11447538

## Gambaran Umum

Makalah konferensi ini (ICoSCI 2026) membandingkan YOLOv9c dan YOLO11n untuk mendeteksi tandan buah segar (TBS) kelapa sawit dan menetapkan empat kelas kematangan: mentah, kurang matang, matang, dan lewat matang. Sasarannya aplikasi ponsel untuk pemeriksaan di lapangan.

Data berupa 2.672 citra TBS yang dikumpulkan dari Mendeley, Kaggle, dan Roboflow. Sebagian berasal dari video yang dipecah menjadi bingkai setiap 0,33 detik. Tempat pengambilan citra tidak disebut. Kotak tandan dilabeli manual di Roboflow, citra diubah ke 640×640, lalu diperbanyak dengan augmentasi menjadi 6.412 citra dan dibagi sekitar 70:20:10.

Setelah 80 epoch, mAP50 validasi YOLO11n 88% dan YOLOv9c 87,1%. Presisi YOLO11n lebih tinggi 6,8 poin, sedangkan *recall* YOLOv9c lebih tinggi 0,9 poin. Perbedaan terbesar ada pada kelas kurang matang dan mentah, dengan presisi YOLO11n lebih tinggi 10,6 dan 12,3 poin.

Kajian ini hanya mendeteksi dan mengelaskan tandan per citra. Tandan tidak dicacah. Teks menyebut augmentasi dilakukan pada 2.672 citra sebelum pembagian 70:20:10, sehingga citra turunan dari satu citra asli dapat berada di data latih dan data validasi sekaligus. Hasil hanya dilaporkan pada data validasi.
