# Drone and deep learning-based instrumentation for palm fruit detection and yield measurement: A Southeast Asian roadmap

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gunawan2026drone` |
| Judul asli | Drone and deep learning-based instrumentation for palm fruit detection and yield measurement: A Southeast Asian roadmap |
| Penulis | Gunawan, Teddy Surya; Kartiwi, Mira; Jamali, Annisa |
| Tahun | 2026 |
| Venue | IEEE Instrumentation and Measurement Magazine |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [gunawan2026drone.pdf](../pdf/gunawan2026drone.pdf)
- DOI resmi: https://doi.org/10.1109/mim.2026.11224873

## Gambaran Umum

Artikel majalah ini adalah tinjauan naratif tentang drone dan pembelajaran mendalam untuk deteksi tandan dan taksiran hasil sawit di Malaysia, Indonesia, dan Thailand. Artikel ini tidak melaporkan basis data, kueri, rentang tahun, atau kriteria pemilihan kajian, sehingga cakupannya tidak dapat diulang. Isinya menelusuri peralihan dari inspeksi manual dan citra satelit ke citra drone resolusi tinggi dengan CNN, detektor YOLO, dan data hiperspektral, lalu menyusun agenda untuk sistem ukur yang murah dan dapat diperluas.

Perbandingan detektor diambil dari satu kajian penulis sendiri (Gunawan dkk. 2023, ICSIMA): lima varian YOLOv8 dilatih pada set data tandan enam kelas berisi 7.171 citra dan 14.559 objek, dengan perangkat keras yang sama. mAP50 semua varian 0,995. mAP50-95 tertinggi pada YOLOv8m (0,927 dengan 25,9 juta parameter), sedangkan YOLOv8l dan YOLOv8x sama-sama 0,921. Waktu inferensi YOLOv8m 11,27 ms per citra. Penulis menyatakan bahwa hasil antarkajian sawit lain tidak dibandingkan langsung karena definisi target, set data, protokol anotasi, ambang IoU, dan perangkat kerasnya berbeda.

Bagian yang paling khas adalah model ukur taksiran hasil dari satu misi drone: hasil dihitung dari jumlah tandan terdeteksi, sebaran kelas kematangan, massa tandan rata-rata per kelas, faktor koreksi kesehatan tajuk, dan koefisien luas petak. Anggaran ketidakpastian yang disusun menurut GUM bersifat indikatif, bukan hasil ukur. Galat hitung detektor diberi 3 sampai 6% dan dinilai terhadap hitungan petak contoh. Galat kelas kematangan diberi 4 sampai 7%, dan sebaran massa tandan 5 sampai 8%. Ketidakpastian gabungan diperkirakan 8 sampai 13%, atau ±16 sampai 26% pada tingkat kepercayaan 95%. Angka itu jauh lebih lebar daripada presisi ±3 sampai 5% yang biasa dikutip dari matriks kebingungan saja. Bagian lain membahas muatan sensor drone, studi kasus per negara, tantangan teknis, ekonomi, dan kebijakan, serta peta jalan regional.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Tidak ada metode pencarian. Hitung ganda tandan yang terlihat di beberapa citra, pelacakan, dan penautan antarpandang tidak dibahas, padahal jumlah tandan terdeteksi menjadi masukan utama model ukurnya. Rentang ketidakpastian dalam anggaran tidak berasal dari pengukuran pada data tertentu.
