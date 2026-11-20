# DEPTH-AWARE DETECTION AND SEGMENTATION OF FRUITS USING FASTER R-CNN AND YOLOV5 FOR ORCHARD ROBOTICS

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hossain2026depth` |
| Judul asli | DEPTH-AWARE DETECTION AND SEGMENTATION OF FRUITS USING FASTER R-CNN AND YOLOV5 FOR ORCHARD ROBOTICS |
| Penulis | Hossain, T.; others |
| Tahun | 2026 |
| Venue | Icic Express Letters Part B Applications |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [hossain2026depth.pdf](../pdf/hossain2026depth.pdf)
- DOI resmi: https://doi.org/10.24507/icicelb.17.05.517

## Gambaran Umum

Hossain, Shi, dan Kovacs (2026) mengembangkan sistem deteksi dan segmentasi buah berbasis RGB-D untuk robotika kebun. Sistem menggabungkan *Faster R-CNN* dan *YOLOv5-Seg* secara *late fusion*, dengan informasi kedalaman dipakai untuk memandu penekanan tumpang tindih (*non-maximum suppression*) dan pengkodean kedalaman bergaya HHA. Sasaran penelitian adalah apel yang tertutup daun, berkelompok, dan berada dalam kondisi cahaya yang berubah.

Data yang dipakai terdiri atas 2.290 citra latih dan 801 citra validasi apel yang direkam dengan kamera Intel RealSense D435. Sistem juga diuji pada 1.000 citra dari MinneApple dan 3.019 citra dari Amodal. Citra masukan berukuran 896 × 896 piksel. Semua eksperimen dijalankan pada GPU NVIDIA RTX 4060 berkapasitas 8 GB, dan kecepatan sistem tercatat sekitar 18 FPS.

Hasil rata-rata pada seluruh kondisi adalah akurasi 97,3%, recall 84,0%, mAP 91,0%, dan F1-score 91,9%. Pada tabel kondisi, recall berkisar 83–84% di semua skenario, sedangkan mAP berada pada rentang 90,7–91,2%. Pada tabel perbandingan, *Improved YOLOv8s* mencapai mAP 92,5% dan lebih tinggi daripada sistem usulan. *Mask R-CNN* mencapai akurasi 98,0% tetapi recall 80,0%, dan *Faster R-CNN* memperoleh mAP 81,2%. Penulis menyimpulkan bahwa sistem usulan paling seimbang di antara keempat model, bukan paling unggul pada setiap metrik.

Penulis melaporkan dua hasil ablasi secara naratif. Menghilangkan penekanan tumpang tindih yang dipandu kedalaman menurunkan recall pada kondisi tertutup berat. Menghilangkan pengkodean HHA menurunkan mAP. Angka ablasi dan analisis runtime disebut pada kesimpulan. Kegagalan yang dibahas penulis terjadi pada apel yang hampir sama warnanya dengan daun dan sebagian tertutup, sehingga peta kedalaman menjadi halus dan tidak memberi pemisahan geometris.

Kajian menunjukkan bahwa informasi kedalaman dapat ditambahkan pada detektor berbasis citra untuk apel. Kajian tidak melaporkan hitungan buah per pohon atau per citra. Penulis sendiri menyebut skenario multi-buah dan integrasi ke platform panen robotik sebagai pekerjaan berikutnya.
