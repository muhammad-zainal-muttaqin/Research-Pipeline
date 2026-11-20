# Development and evolution of YOLO in object detection: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tian2026development` |
| Judul asli | Development and evolution of YOLO in object detection: A survey |
| Penulis | Tian, Ying; Xu, Wenbo; Yang, Bo; Yang, Xinglong; Guo, Hongliang; Wang, Gaige; Yu, Helong |
| Tahun | 2026 |
| Venue | Neurocomputing |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [tian2026development.pdf](../pdf/tian2026development.pdf)
- DOI resmi: https://doi.org/10.1016/j.neucom.2025.132436

## Gambaran Umum

Survei ini membahas perkembangan algoritme deteksi objek YOLO selama sekitar satu dekade, dari 2016 hingga 2025. Deteksi objek bertujuan mengenali objek dalam citra atau video sekaligus menentukan posisinya, biasanya dalam bentuk *bounding box* atau masker tingkat piksel. Penulis menilai YOLO penting karena mengubah deteksi objek dari dua tahap menjadi satu tahap, sehingga kecepatan dan efisiensi deteksi meningkat. Persoalan yang diangkat adalah bagaimana evolusi teknologi YOLO memengaruhi akurasi dan kecepatan, serta bagaimana metrik evaluasi dan pilihan dataset membentuk perbandingan antarmodel.

Tinjauan ini tidak memuat data lapangan, sehingga tidak ada tanaman, lokasi, atau sensor yang dicatat. Cakupannya mencakup YOLOv1 hingga YOLOv13. Dataset acuan yang dibahas adalah PASCAL VOC, MS COCO, dan ImageNet. Metrik yang dianalisis meliputi FPS, GFLOPs, presisi, recall, ROC, IoU, skor F1, kurva PR, AP, dan mAP. Sebagai contoh perbandingan, Tabel 1 memuat model YOLOv8n, SSD, DETR, dan Faster R-CNN pada dataset MS COCO. Himpunan latih berisi sekitar 118.000 citra dan himpunan validasi sekitar 5.000 citra. Semua varian dilatih selama 600 epoch dengan *batch size* 16 dan *learning rate* awal 0,01.

Metode penelitian ini berupa analisis statistik terhadap literatur. Penulis menelusuri inovasi YOLO, mulai dari mekanisme *anchor box*, prediksi multi-skala, modul atensi, desain ringan, hingga arsitektur *anchor-free*. Proporsi penggunaan YOLO pada deteksi objek, klasifikasi citra, dan segmentasi semantik juga dihitung pada beberapa dataset umum. Angka pada Tabel 1 menunjukkan YOLOv8n memiliki 3 juta parameter, mAP@0,5 sebesar 52,5%, dan 163 FPS. SSD memiliki 28 juta parameter, mAP@0,5 sebesar 48,5%, dan 25 FPS. DETR memiliki 20 juta parameter, mAP@0,5 sebesar 63,8%, dan 24 FPS. Faster R-CNN memiliki 44 juta parameter, mAP@0,5 sebesar 59,1%, dan 20 FPS. Hasil ini memperlihatkan keseimbangan antara akurasi dan kecepatan yang menjadi alasan utama popularitas YOLO.

Penulis mencatat keterbatasan YOLOv1, yaitu kinerja yang lemah pada deteksi objek kecil dan akurasi lokalisasi, serta ukuran masukan yang tetap. Penulis juga menyebut beberapa tantangan terbuka. Pada objek kecil, YOLO perlu bergerak dari fokus kecepatan menuju kombinasi kecepatan dan akurasi. Pada kondisi data terbatas, *few-shot learning* masih rentan terhadap overfitting. Pada skenario dunia terbuka dan *open-vocabulary*, model perlu mengenali kategori yang belum pernah dilatih. Kondisi oklusi berat, pencahayaan ekstrem, dan citra beresolusi rendah juga disebut sebagai tantangan yang belum tuntas.

Penulis menyimpulkan bahwa arah pengembangan YOLO berikutnya adalah menjaga keunggulan real-time sambil meningkatkan akurasi, kemampuan generalisasi, dan adaptasi terhadap skenario. Salah satu arah yang disarankan adalah menggabungkan YOLO dengan model prapelatihan visi-bahasa agar model dapat mengenali kategori yang tidak terlihat saat pelatihan.
