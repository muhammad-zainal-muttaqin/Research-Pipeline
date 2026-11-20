# A lightweight citrus detection and counting method based on deep learning model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2025lightweight` |
| Judul asli | A lightweight citrus detection and counting method based on deep learning model |
| Penulis | Chen, Jiqing; Zhang, Mingchang; Lu, Bin; Chen, Quan; Jiang, Zhiwu; Li, Peilin; Gai, Jingyao |
| Tahun | 2025 |
| Venue | Engineering Applications of Artificial Intelligence |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [chen2025lightweight.pdf](../pdf/chen2025lightweight.pdf)
- DOI resmi: https://doi.org/10.1016/j.engappai.2025.112268

## Gambaran Umum

Kajian Chen dkk. (2025) mengusulkan FEW-YOLOv8n, varian ringan dari detektor *YOLOv8n* (detektor objek satu tahap yang menandai objek dengan kotak persegi), untuk mendeteksi dan menghitung buah jeruk pada citra kebun. Penghitungan dilakukan dari satu pandang kamera, sehingga setiap citra menghasilkan satu jumlah buah.

Data yang dipakai berasal dari kamera Daheng dengan resolusi 4160 × 3120 piksel, dengan jarak pengambilan 0,5 sampai 3 m. Kumpulan awal berisi 2.126 citra, dibagi dengan rasio 8:1:1 menjadi 1.700 citra latih, 213 citra validasi, dan 213 citra uji. Setelah augmentasi, jumlah citra valid mencapai 7.400. Anotasi dibuat dengan LabelImg dalam format VOC. Buah yang tertutup lebih dari sekitar 80% tidak diberi label, dan buah latar yang jauh juga tidak diberi label karena robot hanya bekerja pada bidang di depannya. Aturan ini membatasi jumlah buah yang dihitung sebagai kebenaran dasar pada citra yang tertutup berat.

Modifikasi terhadap YOLOv8n terdiri dari tiga bagian: *FasterNet Block* pada blok C2f di *backbone*, atensi *EMA* (*exponential moving average*), dan fungsi kerugian *Wise-IoU* untuk kotak pembatas. Pada tabel ablasi, YOLOv8n menghasilkan presisi 88,6% dan mAP 89,8% dengan ukuran 3,01 MB dan 8,1 GFLOPs. Penambahan FasterNet menaikkan mAP menjadi 91,7% dan menurunkan ukuran menjadi 2,69 MB dan 7,2 GFLOPs. Penambahan EMA menaikkan presisi menjadi 92,1%, tetapi mAP turun menjadi 90,5%. Konfigurasi akhir dengan Wise-IoU menghasilkan presisi 92,4% dan mAP 91,7%, dengan 7,3 GFLOPs. Pada uji penghitungan, 40 citra uji dipilih acak dari skena yang kompleks. YOLOv8n menghasilkan MSE 5,38, MAE 1,77, RMSE 2,32, dan R² 0,91. FEW-YOLOv8n menghasilkan MSE 1,64, MAE 0,92, RMSE 1,28, dan R² 0,98. Dari nilai tabel tersebut, penurunan MSE sebesar 69,5%, MAE sebesar 48,0%, dan RMSE sebesar 44,8%, sedangkan Bagian 4 menulis MAE 44,8% dan RMSE 48%, sehingga angka di bagian itu tertukar.

Ada dua hal yang perlu dicatat. Pertama, abstrak menyebut akurasi 92,7%, sedangkan bagian kontribusi dan kesimpulan menyebut 92,4%.
