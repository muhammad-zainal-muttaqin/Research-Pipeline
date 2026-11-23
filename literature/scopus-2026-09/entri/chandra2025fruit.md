# Fruit Detection and Counting Using Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chandra2025fruit` |
| Judul asli | Fruit Detection and Counting Using Deep Learning |
| Penulis | Chandra, G. Ramesh; Murthy, K. Sri Rama; Archana, S; Snehitha, B; Nishanth, G; Navya, M; Sai Charan, R |
| Tahun | 2025 |
| Venue | Proceedings of the IEEE International Conference Image Information Processing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [chandra2025fruit.pdf](../pdf/chandra2025fruit.pdf)
- DOI resmi: https://doi.org/10.1109/iciip68302.2025.11346118

## Gambaran Umum

Penulis menyoal penghitungan buah secara manual untuk estimasi hasil panen. Cara itu memerlukan banyak tenaga kerja dan rawan galat manusia. Penulis juga menyebut bahwa penghitungan dari citra dapat menghitung buah yang sama dua kali atau lebih pada citra berbeda. Karena itu mereka mengusulkan sistem yang mendeteksi apel, melacaknya antarbingkai video, lalu mencacahnya agar tiap buah dihitung sekali.

Data deteksi berasal dari set data Fruits-360 (Kaggle). Dari 126.305 citra, 7.571 citra disaring untuk latih dan uji, dianotasi dalam format YOLOv11, dan diaugmentasi dengan rotasi acak, pemotongan sampai 55%, dan *Gaussian blur*. Pembagiannya 6.056 citra latih (80%), 605 validasi (8%), dan 910 uji (12%). Masukan sistem berupa video siaran langsung dari *drone* yang mengitari pohon apel 360 derajat atau video tersimpan. Penulis tidak menyebut jumlah pohon, jumlah video, lokasi, maupun pemberi label.

Metodenya tiga modul. YOLO11 (detektor satu tahap) mendeteksi apel pada tiap bingkai, dengan ambang kepercayaan misalnya 70%. ByteTrack (pelacak yang juga memakai deteksi berkepercayaan rendah pada tahap asosiasi kedua, dengan *filter* Kalman dan algoritma Hungarian) memberi ID unik. Penghitung berbasis wilayah (*region*) menghitung ID yang melewati poligon yang ditentukan, sekali per ID. Model dilatih 150 epoch pada GPU RTX 4060, masukan 640×640, ukuran *batch* 4.

Pada Tabel 2, model YOLO11-fv memperoleh presisi 0,959, mAP50 0,779, dan F1 0,729, dibandingkan YOLO11m dengan presisi 0,901, mAP50 0,572, dan F1 0,378. Dalam teks, recall 0,588 dan mAP50-95 0,700. Abstrak menyebut akurasi 90%, kenaikan mAP 33% dan F1 71% terhadap YOLOv11 saja, serta perbaikan MAE; angka akurasi dan MAE tidak ditemukan di badan teks. Pelacakan dievaluasi pada 300 bingkai dengan efisiensi rerata 93,4%, ID hilang 1 sampai 2 dan pertukaran ID 0 sampai 2 per titik ukur.

Tidak ada hitungan buah yang dibandingkan dengan acuan hitung tangan atau panen, sehingga akurasi pencacahan tidak terukur langsung. Evaluasi pelacakan memakai satu urutan 300 bingkai. Set data pelatihan (Fruits-360) tidak sama dengan video *drone* yang dilacak, dan pembagian per pohon tidak disebut. Penulis sendiri mencatat hasil dapat berbeda dengan detektor lain dan sistem kurang efektif pada cuaca ekstrem serta buah yang saling menutup rapat.
