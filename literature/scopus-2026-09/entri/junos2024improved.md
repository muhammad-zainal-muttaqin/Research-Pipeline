# Improved hybrid feature extractor in lightweight convolutional neural network for postharvesting technology: automated oil palm fruit grading

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `junos2024improved` |
| Judul asli | Improved hybrid feature extractor in lightweight convolutional neural network for postharvesting technology: automated oil palm fruit grading |
| Penulis | Junos, Mohamad Haniff; Mohd Khairuddin, Anis Salwa; Abu Talip, Mohamad Sofian; Kairi, Muhammad Izhar; Siran, Yosri Mohd |
| Tahun | 2024 |
| Venue | Neural Computing and Applications |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [junos2024improved.pdf](../pdf/junos2024improved.pdf)
- DOI resmi: https://doi.org/10.1007/s00521-024-10300-4

## Gambaran Umum

Penelitian ini membangun detektor objek ringan untuk menilai mutu tandan buah segar (TBS) kelapa sawit ke dalam empat kelas kematangan: matang (*ripe*), kurang matang (*underripe*), terlalu matang (*overripe*), dan belum matang (*unripe*). Sasarannya perangkat tertanam berdaya rendah, yaitu NVIDIA Jetson Nano. Penulis menyebut penilaian mutu manual di pabrik bersifat subjektif karena kemiripan visual antarkelas, intensitas cahaya, dan warna tandan yang berubah menurut sudut pandang.

Citra diambil dengan kamera kubah Hikvision 2 MP di kebun Sime Darby Plantation, Selangor, Malaysia, selama musim panen, pukul 09.00 sampai 17.00, dalam cuaca berawan dan cerah. Posisi tandan (di pohon, di tanah, atau di tempat pengumpulan) tidak disebut. Label kelas digambar dengan LabelImg berdasarkan pengetahuan penilai ahli. Himpunan data berisi 1.281 citra dengan resolusi 272 × 194 sampai 11.339 × 3.780 piksel. Rentang resolusi ini lebih besar daripada keluaran kamera 2 MP; asal citra beresolusi tinggi tidak dijelaskan (belum diperiksa). Data dibagi 70% latih dan 30% validasi. Tidak ada data uji terpisah, sehingga semua angka di bawah dihitung pada data validasi.

Model dasarnya YOLOv3 tiny, yaitu detektor satu tahap yang memprediksi kotak dan kelas sekaligus. Ada empat perubahan. Pertama, tulang punggung diganti ekstraktor ciri hibrida dari DenseNet161 (lapisan yang menggunakan ulang semua peta ciri sebelumnya) dan modul MBConv (konvolusi *depthwise* dengan *bottleneck* terbalik untuk mengurangi parameter). Kedua, leher jaringan memakai empat skala deteksi dengan *feature pyramid network*. Ketiga, ditambahkan *spatial pyramid pooling* (SPP) untuk memperluas medan reseptif. Keempat, regresi kotak memakai *complete IoU* (CIoU). Ukuran masukan 416 × 416 piksel.

Pada data validasi, model usulan mencapai mAP@0,5 94,37%, mAP@0,75 90,70%, mAP@0,5:0,95 75,26%, presisi 0,86, recall 0,93, dan F1 0,89. Pembandingnya YOLOv4 (93,73%), YOLOv3 (92,81%), YOLOv4 tiny (87,95%), dan YOLOv3 tiny (83,71%). AP per kelas model usulan adalah 96,65% (matang), 94,12% (kurang matang), 92,31% (terlalu matang), dan 94,39% (belum matang). Tabel ablasi menulis 94,73% untuk model akhir dan 85,52% untuk YOLOv3 tiny, berbeda dengan tabel perbandingan. Ukuran model 65,6 MB, 16,4 juta parameter, dan 28,353 BFLOPs. Kecepatannya 28,5 FPS pada GeForce GTX 1650 dan 4,8 FPS pada Jetson Nano, lebih lambat daripada YOLOv3 tiny dan YOLOv4 tiny (sekitar 16 FPS pada Jetson Nano). Pada set data VisDrone, mAP@0,5 model usulan 36,15%, dibanding 10,16% untuk YOLOv3 tiny.

Penulis menyatakan keterbatasan pada kompleksitas model. Tulang punggung DenseNet menyumbang sekitar 87% FLOPs, dan 291 lapisan membuat deteksi lambat. Dari teks dapat diperiksa bahwa tidak ada pembagian data menurut tandan atau pohon, tidak ada data uji terpisah, dan tandan tidak dicacah. Setiap citra dinilai sendiri-sendiri.
