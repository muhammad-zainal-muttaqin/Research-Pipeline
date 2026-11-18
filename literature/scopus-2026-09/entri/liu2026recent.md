# RECENT ADVANCES SURVEY IN COMPUTER VISION AND ARTIFICIAL INTELLIGENCE FOR FRUIT DETECTION

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026recent` |
| Judul asli | RECENT ADVANCES SURVEY IN COMPUTER VISION AND ARTIFICIAL INTELLIGENCE FOR FRUIT DETECTION |
| Penulis | Liu, Qi; Sulaiman, Puteri Suhaiza binti; Mustaffa, Mas Rina binti; Kahar, Zainal bin Abdul; Bai, Lian; Xu, Huicai |
| Tahun | 2026 |
| Venue | Inmateh Agricultural Engineering |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [liu2026recent.pdf](../pdf/liu2026recent.pdf)
- DOI resmi: https://doi.org/10.35633/inmateh-79-28

## Gambaran Umum

Tinjauan ini mengkaji deteksi buah dalam lingkungan pertanian nyata, yang menghadapi tantangan berupa perubahan pencahayaan, oklusi, tumpang tindih buah, dan keterbatasan daya komputasi perangkat. Pengesanan objek menjadi teknologi kunci untuk mengidentifikasi, menemukan, dan mengklasifikasikan buah, daun, hama, dan penyakit dari citra atau video, dengan aplikasi pada pemanenan otomatis, penilaian hasil, dan penentuan mutu. Penulis menyusun metode utama beserta evolusionya, merangkum fitur inti dan hasil penerapannya, mengungkap faktor penentu kinerja, serta menilai skalabilitas dan kelayakan penerapan sebagai acuan bagi akademisi dan rekayasa.

Data dan metode bersifat tinjauan naratif, bukan percobaan baru. Penulis mengelompokkan algoritma deteksi buah menjadi lima golongan, yaitu algoritma tradisional berbasis ciri manual, deteksi dua tahap, deteksi satu tahap, deteksi tanpa sauh (*anchor-free*), dan pembelajaran pemindahan (*transfer learning*), lalu membahas arsitektur Transformer. Skenario yang dibahas mencakup deteksi banyak objek, latar belakang kompleks, dan komputasi tepi. Strategi pencarian kepustakaan, jumlah makalah yang dimasukkan, dan satu pun dataset milik tinjauan tidak dinyatakan. Asosiasi lintas pandang dan penghitungan buah unik juga tidak dibahas.

Mekanisme deteksi dijelaskan per golongan. Metode tradisional memakai rekayasa ciri warna, bentuk, dan tekstur lewat praproses, segmentasi ambang, dan aturan klasifikasi, dengan ekstraktor seperti SIFT dan HOG serta pengklasifikasi SVM dan AdaBoost. Deteksi dua tahap memisahkan pembangkitan wilayah kandidat dan deteksi lanjutan, diwakili R-CNN, Fast R-CNN, Faster R-CNN dengan *region proposal network*, serta Mask R-CNN yang menambah cabang topeng dan mengganti ROIPooling dengan ROIAlign. Deteksi satu tahap memprediksi kelas dan posisi langsung tanpa wilayah kandidat, diwakili YOLO dan SSD. Metode tanpa sauh memakai titik pusat seperti CenterNet dan FCOS. Pembelajaran pemindahan dan Transformer memanfaatkan perhatian diri untuk memodelkan ketergantungan jarak jauh; DETR memakai pencocokan kueri tanpa sauh yang membantu deteksi objek kecil dan tertutup.

Angka hasil dikutip dari kajian dalam korpus tinjauan dan bukan hasil percobaan penulis, sehingga tinjauan ini tidak memiliki acuan hitung sendiri. Sebagai contoh, metode perbedaan warna mencapai tingkat pengenalan 85%; Faster R-CNN dengan mekanisme perhatian pada tomat muda mencapai mAP 98,46% dengan waktu deteksi 0,084 detik per citra; Mask R-CNN berbasis ResNet50-FPN pada tomat hijau mencapai skor F1 92,0% pada ambang IoU 0,5. Model RT-DETR untuk pir mencapai akurasi 93,7%, recall 91,9%, dan mAP 98%, dengan penurunan jumlah parameter, daya hitung, dan ukuran bobot masing-masing 48,47%, 56,2%, dan 48,31%. PG-DETR pada delima mencapai mAP50 93,37% dengan 6,7 juta parameter, 12,4 GFLOPs/s, dan 173,58 FPS; ML-DETR pada tomat ceri mencapai akurasi 91,36%, mAP50 0,8875, 13,9 GFLOPs, dan 81,2 FPS. Versi ringan YOLO mencapai kecepatan 30–60 FPS. Metrik yang dipakai meliputi akurasi, recall, mAP, skor F1, GFLOPs, dan FPS.

Batasan yang dinyatakan penulis meliputi kecenderungan metode tradisional menghasilkan positif dan negatif palsu serta biaya hitung tinggi; deteksi dua tahap lambat, berukuran besar, sulit diterapkan di tepi, dan kurang tanggap pada objek kecil yang rapat; deteksi satu tahap mengalami plafon pada buah kecil yang saling menutup; model Transformer memiliki jumlah parameter dan daya hitung besar sehingga sulit dipasang pada perangkat daya rendah. Kualitas dataset juga menjadi hambatan karena data tomat terfragmentasi, anotasi tidak seragam, serta data multimodal dan multitugas kurang, sehingga model terbukti baik di laboratorium tetapi sulit dipakai di lapangan. Penulis menyimpulkan bahwa tantangan utama adalah menyeimbangkan efisiensi hitung dengan kemampuan memahami skenario kompleks, dan menunjukkan penggabungan arsitektur ringan dengan mekanisme Transformer sebagai arah pengembangan.

