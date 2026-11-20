# RTFVE-YOLOv9: Real-time fruit volume estimation model integrating YOLOv9 and binocular stereo vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yi2025rtfve` |
| Judul asli | RTFVE-YOLOv9: Real-time fruit volume estimation model integrating YOLOv9 and binocular stereo vision |
| Penulis | Yi, Wenlong; Xia, Shuokang; Kuzmin, Sergey; Gerasimov, Igor; Cheng, Xiangping |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [yi2025rtfve.pdf](../pdf/yi2025rtfve.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110401

## Gambaran Umum

Kajian ini mengusulkan model estimasi volume buah waktu nyata bernama RTFVE-YOLOv9. Model ini menggabungkan YOLOv9 dengan *binocular stereo vision*. Tujuannya mengatasi rendahnya otomatisasi dan kurangnya akurasi pengukuran volume buah di kebun yang kompleks. Masalah utamanya adalah struktur tajuk yang beragam dan *occlusion* berat akibat cabang dan daun. Pengukuran manual dinilai memakan waktu dan tenaga.

Data penelitian mencakup empat jenis buah ekonomi, yaitu apel, pir, pomelo, dan kiwi. Untuk validasi volume, penulis memilih 16 sampel untuk setiap jenis buah. Pengukuran pembanding memakai metode perpindahan air. Kalibrasi kamera binokular memakai papan kalibrasi dengan sisi persegi 33 mm. Sebanyak 30 set citra binokular diambil dari berbagai posisi dan sudut. Kesalahan rata-rata parameter K dan D untuk kedua kamera berada dalam 2%. Jarak baseline kedua kamera adalah 6 mm.

Model dibangun dengan dua modul baru. Modul DSGLSeq meningkatkan pengenalan buah yang terhalang. Modul MHMSI meningkatkan deteksi buah kecil. Dibandingkan dengan model dasar YOLOv9-c, *mean Average Precision* (mAP) naik 1,6% pada apel, 4% pada pir, 2,1% pada pomelo, dan 3,8% pada kiwi. Metrik yang dipakai adalah *Precision*, mAP, dan *Recall*. Untuk evaluasi volume, penulis memakai MRAE, RMSE, dan R2. Penulis juga menganalisis mekanisme model dengan *heatmap* dan *Effective Receptive Field*.
