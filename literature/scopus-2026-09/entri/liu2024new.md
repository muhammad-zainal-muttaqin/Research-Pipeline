# New Progress in Intelligent Picking: Online Detection of Apple Maturity and Fruit Diameter Based on Machine Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2024new` |
| Judul asli | New Progress in Intelligent Picking: Online Detection of Apple Maturity and Fruit Diameter Based on Machine Vision |
| Penulis | Liu, Junsheng; Zhao, Guangze; Liu, Shuangxi; Liu, Yi; Yang, Huawei; Sun, Jingwei; Yan, Yinfa; Fan, Guoqiang; Wang, Jinxing; Zhang, Hongjian |
| Tahun | 2024 |
| Venue | Agronomy |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [liu2024new.pdf](../pdf/liu2024new.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy14040721

## Gambaran Umum

Kajian ini mengusulkan dua hal untuk panen apel robotik. Pertama, detektor objek YOLOv5s yang diubah (disebut YOLOv5s-GGV) untuk mengenali apel dan tingkat kematangannya. Kedua, algoritma yang memakai data kedalaman dari kamera RealSense untuk memperkirakan diameter apel. Penulis melaporkan presisi rata-rata deteksi tingkat kematangan sebesar 98,7%, dengan akurasi 97,4% untuk apel kematangan rendah, serta kecepatan 155 FPS untuk detektor.

Masalah yang diangkat adalah dua kebutuhan lengan robot pemanen. Lengan perlu tahu apel mana yang sudah layak panen, dan perlu tahu ukuran apel untuk menentukan jarak dan posisi genggam. Detektor generik sering gagal pada apel kecil atau sebagian tertutup daun, dan pengukuran ukuran dari citra RGB saja tidak memberi jarak sebenarnya. Kajian ini menjawab keduanya dalam satu sistem.

Perubahan pada detektor berupa tiga modul: GSConv untuk konvolusi yang lebih ringan, VoVGSCSP untuk blok fitur, dan GAM (global attention mechanism) untuk memberi bobot pada area fitur yang penting. Pada algoritma diameter, penulis menghapus distorsi lensa, menyaring nilai kedalaman yang tidak valid, lalu menghitung diameter dari piksel dan kedalaman yang sudah dikoreksi. Hasilnya: deteksi diameter berhasil pada 93,3% percobaan (28 dari 30 apel, dua salah klasifikasi) dengan 56 FPS, dan rata-rata selisih diameter 0,878 mm pada 10 apel dalam tiga percobaan.

Pada uji ablasi dan perbandingan model, YOLOv5s-GGV dibandingkan dengan varian YOLOv5s dan model lain di set data apel yang dianotasi penulis. Anotasi hanya menandai apel yang siap dipanen untuk lengan robot, dan penulis menyatakan bahwa anotasi tidak memperhitungkan oklusi. Akibatnya, angka presisi tidak menggambarkan kinerja pada apel yang tertutup pelepah atau daun.

Nilai yang paling dapat dipegang adalah pengukuran diameter pada sampel kecil dan lingkungan terkendali.
