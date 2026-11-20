# Real-time counting of strawberry using cost-effective embedded GPU and YOLOv4-tiny

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `immaneni2022real` |
| Judul asli | Real-time counting of strawberry using cost-effective embedded GPU and YOLOv4-tiny |
| Penulis | Immaneni, Amritha; Chang, Young Ki |
| Tahun | 2022 |
| Venue | 2022 Asabe Annual International Meeting |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [immaneni2022real.pdf](../pdf/immaneni2022real.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202200240

## Gambaran Umum

Kajian ini (Immaneni dkk., 2022) membangun sistem deteksi buah stroberi secara real-time di lapangan dengan YOLOv4-tiny yang dijalankan pada perangkat tertanam NVIDIA Jetson Nano dan kamera Raspberry Pi v2. Model mendeteksi tiga kelas per citra: bunga, stroberi mentah (unripe), dan stroberi matang (ripe). Kajian ini tidak mengukur akurasi penghitungan jumlah buah.

Hasil utama: YOLOv4-tiny pada resolusi 416×416 mencapai mAP@0,5 sebesar 91,95%, F1 87%, presisi 82%, dan recall 93%. Pada 480×480 mAP naik menjadi 93,55%, sedangkan pada 640×640 turun menjadi 88,56%. Penulis memilih 416×416 sebagai resolusi ideal karena FPS-nya lebih tinggi dengan penurunan mAP yang kecil. Kecepatan YOLOv4-tiny di Jetson Nano adalah 14,6 FPS pada kerangka Darknet, 19,86 FPS pada TensorRT (FP16), dan 0,96 FPS pada TensorFlow Lite. Untuk YOLOv4 penuh pada 416×416, kecepatan hanya 1,6 FPS, sehingga penulis menilainya kurang cocok untuk perangkat tepi.

Perbandingan antarmodel dalam kajian ini sempit. Teks menyatakan bahwa kedua model mencapai mAP di atas 90%, tetapi Tabel 2 menunjukkan YOLOv4-tiny pada 640×640 hanya 88,56%, sehingga klaim itu tidak berlaku untuk semua konfigurasi yang dilaporkan. Penulis juga menyatakan bahwa YOLOv4 lebih akurat, tetapi angka mAP YOLOv4 yang dibandingkan secara langsung tidak dirinci di bagian yang sudah dibaca. Pada uji real-time dengan layar sebagai sumber citra, FPS rata-rata video 13,9 dan tidak berubah banyak saat kamera digunakan, menurut penulis.

Kajian ini memuat analisis kesalahan kualitatif. Jumlah false positive tertinggi terjadi pada kelas stroberi mentah, yang menurut penulis disebabkan kemiripan warna dengan daun dan kasus perantara antara bunga dan buah. Penulis juga mencatat bahwa false negative lebih sering terjadi pada objek kecil. Kumpulan data, jumlah citra, dan cara anotasi tidak dibahas di bagian yang sudah dibaca, sehingga kajian ini tidak dapat dinilai dari sisi ukuran dan keragaman data.

Keterbatasan yang dinyatakan penulis mencakup objek kecil yang terlewat, dan saran perbaikan berupa data latih yang lebih besar dan lebih beragam serta kamera global-shutter. Hubungan antara mAP per citra dan galat penghitungan tidak diukur.
