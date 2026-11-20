# Avocado Detection System on a UAV with YOLOv8 Image Processing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yanyachi2026avocado` |
| Judul asli | Avocado Detection System on a UAV with YOLOv8 Image Processing |
| Penulis | Yanyachi, Pablo Raul; Aco, Anderson Eloy Lajo |
| Tahun | 2026 |
| Venue | IEEE Access |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | avocado |

## Tautan Akses
- PDF: [yanyachi2026avocado.pdf](../pdf/yanyachi2026avocado.pdf)
- DOI resmi: https://doi.org/10.1109/access.2026.3687453

## Gambaran Umum

Kajian ini membahas deteksi buah alpukat varietas *Hass* (*Persea americana*) menggunakan pesawat nirawak (UAV). Deteksi buah di kebun masih sulit karena bentuk buah yang tidak beraturan, kulit yang gelap, dan latar belakang yang kompleks. Kondisi ini menurunkan kinerja algoritma penglihatan komputer konvensional. Penulis mengusulkan sistem penglihatan komputer yang menggabungkan jaringan saraf YOLOv8 dengan data kedalaman untuk memperkirakan posisi tiga dimensi setiap buah. Sistem ini juga dirancang untuk klasifikasi tingkat kematangan, pencacahan buah, estimasi jarak dan tinggi, serta pemetaan dua dimensi.

Sistem diuji dalam dua tahap. Tahap pertama dilakukan di lingkungan simulasi yang meniru perkebunan buatan, dengan perangkat lunak ROS 2, Gazebo, dan PX4. Tahap kedua dilakukan di lahan budidaya nyata menggunakan UAV yang dilengkapi kamera RGB-D dan komputer onboard. Pada uji lapangan, penulis hanya menilai tahap akuisisi citra selama terbang, bukan keseluruhan pipeline deteksi. Data pada uji lapangan dicatat dalam format yang kompatibel dengan lingkungan kerja sistem, lalu dianalisis lebih lanjut dengan YOLOv8.

Metode utama adalah YOLOv8 yang memprediksi koordinat *bounding box* secara langsung dari citra, lalu mengubahnya menjadi koordinat citra asli. Penulis membandingkan beberapa varian YOLOv8. Varian YOLOv8s memberikan keseimbangan terbaik antara akurasi dan efisiensi, dengan mAP@0,5 sebesar 84,01%, mAP@0,5:0,95 sebesar 76,94%, presisi 79,66%, dan recall 85,37%. Varian lain menghasilkan mAP antara 74,39% sampai 75,31%, sehingga selisih antarvarian kecil meskipun kompleksitas modelnya berbeda jauh. Sebagai pembanding, penelitian lain melaporkan mAP YOLOv8 di atas 90% pada buah lain, misalnya klasifikasi kematangan mangga dengan 96,6%.

Penulis menyatakan bahwa hasil ini masih lebih rendah daripada nilai tertinggi yang dilaporkan dalam literatur. Warna buah yang mirip dengan daun serta oklusi yang berat pada tajuk alpukat menjadi penyebab utama. Pencahayaan yang berubah juga menyulitkan pengenalan objek. Penulis menilai modifikasi arsitektur saja belum cukup untuk mengatasi tantangan tersebut. Pada uji lapangan terdapat beberapa keterbatasan teknis, sehingga kepraktisan sistem di kebun nyata belum sepenuhnya terbukti. Penulis juga mencatat bahwa integrasi ROS2 untuk kendali real-time masih perlu dikembangkan. Penelitian lanjutan diarahkan untuk mengoptimalkan model dan memperluas penerapannya pada sistem drone yang sepenuhnya otonom.
