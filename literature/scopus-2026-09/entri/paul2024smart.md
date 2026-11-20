# Smart solutions for capsicum Harvesting: Unleashing the power of YOLO for Detection, Segmentation, growth stage Classification, Counting, and real-time mobile identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `paul2024smart` |
| Judul asli | Smart solutions for capsicum Harvesting: Unleashing the power of YOLO for Detection, Segmentation, growth stage Classification, Counting, and real-time mobile identification |
| Penulis | Paul, Ayan; Machavaram, Rajendra; Ambuj; Kumar, Dheeraj; Nagar, Harsh |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [paul2024smart.pdf](../pdf/paul2024smart.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.108832

## Gambaran Umum

Paul dkk. (2024) membangun sistem berbasis YOLOv8 untuk paprika (*sweet pepper*, atau *capsicum*) di rumah kaca. Sistem ini mendeteksi buah, mengklasifikasikan tahap pertumbuhannya, melokalisasi tangkai buah (*peduncle*), dan menghitung buah per siklus panen. Data yang dipakai terdiri atas 400 citra rumah kaca. Makalah ini diterbitkan di *Computers and Electronics in Agriculture* 219 (2024) 108832.

Deteksi paprika mencapai mAP@0,5 sebesar 0,967 dengan YOLOv8s. Klasifikasi tahap pertumbuhan mencapai mAP@0,5 sebesar 0,614. Lokalisasi tangkai mencapai mAP@0,5 sebesar 0,790 untuk kotak pembatas dan 0,771 untuk *mask* (YOLOv8s-seg). Kesalahan lokalisasi buah dengan kamera *depth* Intel RealSense D455 dilaporkan 8 mm (longitudinal), 9 mm (vertikal), dan 12 mm (lateral).

Pada penghitungan per siklus panen, penulis melaporkan lima siklus (Tabel 14). Jumlah buah sebenarnya (*ground truth*) berturut-turut 98, 103, 101, 94, dan 89. Akurasi penghitungan berturut-turut 91,8; 91,2; 94,1; 89,3; dan 87,6 persen. Akurasi tertinggi, 94,1 persen, tercapai pada penghitungan sebelum siklus ketiga. Akurasi terendah, 87,6 persen, tercapai pada siklus kelima, yang oleh penulis dikaitkan dengan ukuran paprika yang tidak seragam. Presisi per siklus berkisar 0,931 sampai 0,978 dan recall 0,809 sampai 0,891.

Aplikasi Android memakai model yang sama untuk deteksi dan lokalisasi di perangkat. Pada 500 citra, IoU rerata 0,92 dan rerata galat lokalisasi Euclidean 5 piksel. Tingkat deteksi multi-instans 98 persen, tingkat positif palsu 2 persen di bawah gangguan citra, dan keberhasilan 95 persen pada cahaya rendah. Konsumsi baterai 12 persen per jam dan beban CPU 25 persen pada beban berat.

Penulis sendiri membatasi klaim pada beberapa hal. Data hanya berasal dari rumah kaca, sehingga variasi lapangan terbuka dan cuaca belum tercakup. Ketahanan model terhadap variasi warna, bentuk, dan ukuran yang tidak tercatat dipertanyakan oleh penulis. Akurasi penghitungan dapat berubah pada kondisi lingkungan dan varietas tanaman yang berbeda. Aplikasi Android belum divalidasi di lapangan terbuka.

Angka penghitungan 87,6 sampai 94,1 persen berasal dari siklus panen yang berbeda pada satu kebun, sehingga tidak dapat dibandingkan langsung dengan akurasi deteksi per citra.
