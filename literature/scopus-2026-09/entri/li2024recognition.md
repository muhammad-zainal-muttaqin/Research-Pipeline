# Recognition and Positioning of Strawberries Based on Improved YOLOv7 and RGB-D Sensing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2024recognition` |
| Judul asli | Recognition and Positioning of Strawberries Based on Improved YOLOv7 and RGB-D Sensing |
| Penulis | Li, Yuwen; Wang, Wei; Guo, Xiaohuan; Wang, Xiaorong; Liu, Yizhe; Wang, Daren |
| Tahun | 2024 |
| Venue | Agriculture Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [li2024recognition.pdf](../pdf/li2024recognition.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture14040624

## Gambaran Umum

Kajian ini (Li dkk., 2024, *Agriculture* 14, 624) mengusulkan sistem pengenalan stroberi untuk robot pemetik. Sistem memakai kamera RGB-D Intel RealSense D435i dan detektor YOLOv7 yang sudah dimodifikasi. Tujuannya adalah mengenali buah, menentukan titik petik dari geometri buah, dan menghitung posisi titik itu dalam koordinat robot.

Dataset dibuat di laboratorium dengan 600 citra dasar, lalu diperbanyak menjadi 3.000 citra lewat augmentasi. Pembagian data 2.100 citra latih dan 900 citra validasi (rasio 7:3). Pengujian dilakukan pada adegan tiruan rak stroberi yang ditinggikan, bukan pada kebun sungguhan.

Hasil deteksi YOLOv7 dasar: presisi 98,0%, recall 99,4%, mAP@0,5 99,6%, mAP@0,95 95,4%, dengan 37,2 juta parameter, 105,1 GFLOPs, dan 18,7 FPS. Versi yang diperbaiki memakai GhostConv, modul atensi CBAM, penghapusan satu lapisan fitur yang tidak perlu, dan penambahan lapisan fitur untuk objek kecil. Hasilnya: presisi 98,8%, recall 99,2%, mAP@0,5 99,8%, mAP@0,95 96,8%, dengan 15,0 juta parameter, 61,2 GFLOPs, dan 22,3 FPS. Penulis menyatakan presisi 99,0% dan recall 96,9% pada pengujian keseluruhan.

Pada uji laboratorium dengan 98 buah matang, terdapat 95 deteksi benar (TP), 1 deteksi salah (FP), dan 3 buah terlewat (FN). Keberhasilan penentuan posisi petik 90,8% dengan waktu rata-rata 76 ms per citra. Penulis menyebut kegagalan terjadi terutama pada oklusi berat. Waktu total per buah tercatat 7,5 detik.

Kajian ini tidak mengukur jumlah buah per tanaman atau per kebun, sehingga tidak menjawab pertanyaan penghitungan. Relevansinya bagi tinjauan terletak pada penggunaan depth untuk menentukan posisi tiga dimensi buah. Penulis sendiri menyatakan pengujian hanya dilakukan pada stroberi tiruan di laboratorium, dan uji pada adegan stroberi alami belum dilakukan.
