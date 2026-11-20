# Green Citrus Detection and Counting in Orchards Based on YOLOv5-CS and AI Edge System

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lyu2022green` |
| Judul asli | Green Citrus Detection and Counting in Orchards Based on YOLOv5-CS and AI Edge System |
| Penulis | Lyu, Shilei; Li, Ruiyao; Zhao, Yawen; Li, Zhen; Fan, Renjie; Liu, Siying |
| Tahun | 2022 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [lyu2022green.pdf](../pdf/lyu2022green.pdf)
- DOI resmi: https://doi.org/10.3390/s22020576

## Gambaran Umum

Kajian ini membangun sistem penghitungan jeruk (*citrus*) hijau dari video yang direkam di kebun, lalu menjalankannya di perangkat tepi (*edge computing*). Detektornya YOLOv5-CS, yaitu YOLOv5 yang dimodifikasi dengan blok CBAM (*Convolutional Block Attention Module*) sebagai pengganti konvolusi biasa setelah modul Focus, ditambah kepala deteksi tambahan untuk objek kecil. Hasil deteksi dilacak antarbingkai dengan DeepSORT, dan buah dihitung ketika titik tengah kotak prediksinya melintasi garis virtual yang ditetapkan di video.

Masalah yang diangkat adalah penghitungan buah secara manual yang lambat dan tidak konsisten di kebun. Kamera yang bergerak melewati pohon juga memunculkan buah yang sama di banyak bingkai, sehingga penghitungan per bingkai saja akan melebihkan jumlah. Garis virtual memberi aturan hitung sederhana: buah dihitung sekali saat melintasi garis, dengan syarat pelacakan mempertahankan identitas buah di antara bingkai. Keberhasilan aturan ini bergantung pada kualitas pelacakan, dan teks tidak merinci kasus buah yang hilang lalu muncul kembali.

Dari sisi kecepatan, teks melaporkan waktu inferensi pada server sebesar 0,018 s per gambar untuk YOLOv5s dan 0,017 s untuk YOLOv5-CS. Deteksi dan penghitungan video pada platform tepi Nvidia Jetson Xavier NX (21 TOPS) dengan kamera HD mencapai 28 FPS.

Abstrak melaporkan mAP@.5 YOLOv5-CS untuk jeruk hijau sebesar 98,23% dan recall 97,66%. Waktu inferensi pada Jetson Xavier NX sebesar 0,037 s per gambar. Abstrak tidak menyebut galat penghitungan per video, sehingga akurasi penghitungan di tingkat video tidak dapat dinilai dari ringkasan ini.

Mekanisme CBAM dinyatakan bertujuan memfokuskan model pada buah dan mengurangi gangguan dari daun di sekitarnya. Fungsi rugi memakai CIoU (*Complete Intersection over Union*), dan laju belajar dijadwalkan dengan pemanasan lalu peluruhan kosinus (*cosine annealing*). Dari sisi rekayasa, kajian ini menunjukkan kelayakan pipeline deteksi dan penghitungan pada perangkat tepi dengan satu kamera.
