# GeoSphere-DETR: RGB-D citrus fruit detection in cluttered orchards via geometry-gated fusion and geometry-aware confidence recalibration

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026geosphere` |
| Judul asli | GeoSphere-DETR: RGB-D citrus fruit detection in cluttered orchards via geometry-gated fusion and geometry-aware confidence recalibration |
| Penulis | Liu, Shiyu; Ampatzidis, Yiannis; Choi, Daeun; Lee, Won Suk |
| Tahun | 2026 |
| Venue | Artificial Intelligence in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [liu2026geosphere.pdf](../pdf/liu2026geosphere.pdf)
- DOI resmi: https://doi.org/10.1016/j.aiia.2026.08.010

## Gambaran Umum

Kajian ini (Liu, Ampatzidis, Choi, dan Lee, *Artificial Intelligence in Agriculture*, 2026) mengusulkan GeoSphere-DETR, detektor buah jeruk berbasis RT-DETR yang menerima citra RGB dan peta kedalaman (*depth*) dari kamera stereo ZED X. Tujuannya mengurangi deteksi palsu di kebun yang penuh daun dan pantulan cahaya. Kebun yang dipakai adalah kebun jeruk Hamlin (*Citrus sinensis*). Data terdiri atas 2.200 citra dengan 102.719 instans dari dua lapangan. Lapangan A dipakai untuk latih dan validasi, sedangkan lapangan B dipakai untuk uji dengan pohon dan hari yang berbeda, sehingga uji tidak tumpang tindih dengan data latih.

Metode ini menambahkan dua modul berbasis geometri. Modul pertama, *geometry-gated fusion*, memakai fitur geometri dari depth (kekasaran permukaan dan kecembungan berbasis Laplacian) untuk menimbang fitur RGB dan depth di tingkat neck. Modul kedua, *geometry-aware confidence recalibration*, menyesuaikan skor kepercayaan query berdasarkan konsistensi bentuk. Anotasi awal dibuat dengan Grounding DINO, lalu dikoreksi oleh satu anotator ahli. Sekitar 20% proposal ditolak, dan waktu anotasi turun dari 3 sampai 5 menit menjadi 1 sampai 3 menit per citra.

Pada data uji, GeoSphere-DETR mencapai mAP50 0,863 dengan 3,286 false positive per citra (FPPI). RT-DETR berbasis RGB mencapai 0,786 dengan 7,240 FPPI, dan YOLOv11m 0,715 dengan 8,735 FPPI. Penulis melaporkan kenaikan mAP50 sebesar 9,8% dan penurunan FPPI sebesar 54,6% dibanding RT-DETR. Kecepatan turun dari 34,1 FPS menjadi 32,7 FPS pada GPU NVIDIA L40S. Ambang kepercayaan 0,603 dipilih pada data validasi dan dipakai sama untuk semua metode. Angka FPPI pada satu ambang ini tidak menunjukkan kurva presisi-recall penuh.

Keterbatasan kajian ini meliputi beberapa hal. Cakupan depth stereo yang valid hanya 52,8% ± 2,6% di lapangan uji dan 67,4% ± 5,2% di lapangan latih, sehingga sebagian citra tidak punya informasi geometri yang berarti. Data hanya berasal dari satu jenis buah, satu kamera, dan dua lapangan.
