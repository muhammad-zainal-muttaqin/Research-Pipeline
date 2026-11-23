# Measuring Fruit Diameter for Fruit Tree Management Purposes Using an RGB-D Camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fukuda2024measuring` |
| Judul asli | Measuring Fruit Diameter for Fruit Tree Management Purposes Using an RGB-D Camera |
| Penulis | Fukuda, Teppei; Ishii, Masaki; Ito, Hidekatsu; Dohsaka, Kohji |
| Tahun | 2024 |
| Venue | 2024 Joint 13th International Conference on Soft Computing and Intelligent Systems and 25th International Symposium on Advanced Intelligent Systems Scis and Isis 2024 |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [fukuda2024measuring.pdf](../pdf/fukuda2024measuring.pdf)
- DOI resmi: https://doi.org/10.1109/scisisis61014.2024.10760234

## Gambaran Umum

Penulis menyebut jumlah petani di Jepang menurun karena penuaan dan sulitnya budi daya buah bermutu tinggi. Salah satu tugas pengelolaan pohon buah adalah survei pembesaran buah, yaitu mengukur diameter maksimum tiap buah dengan jangka sorong untuk mendapat ukuran rata-rata. Pekerjaan ini manual dan memakan waktu. Kajian ini mengembangkan cara mendeteksi buah apel dan menghitung diameternya dengan kamera RGB-D.

Tanaman yang diteliti adalah apel. Detektor apel muda dilatih dengan 6.257 citra yang diambil dengan GoPro dan AQUOS sense5G SH-M17 dari Mei sampai September 2021 sampai 2024 di Stasiun Percobaan Pohon Buah Prefektur Akita. Citra dibagi 5.005 (80%) untuk latih dan 1.252 (20%) untuk verifikasi. Pengukuran diameter memakai kamera RealSense D405 (RGB 1280x720, *depth* 640x360). Kamera dipegang pada jarak 10 sampai 30 cm dari buah, dua kali dari sudut berbeda, kira-kira 20 detik pada 30 fps. Pemberi label citra latih tidak disebut. Jumlah buah yang diukur adalah 13.

Metode memakai dua detektor, yaitu RTMDet-l-Swin-B berbobot COCO untuk apel matang dan YOLOv10s yang disetel-halus untuk apel muda. Keluaran keduanya digabung dengan *non maximum suppression* (NMS, penghapusan kotak tumpang tindih). Diameter dihitung dengan model kamera lubang jarum, dengan anggapan buah berbentuk bola. Jari-jari didapat dari kedalaman di pusat buah dan lebar kotak pada citra warna. Koreksi ditambahkan karena kedalaman terukur di permukaan dan karena proyeksi perspektif. Cara kedua, pencocokan elips pada bidang xz, dinilai berat dan kurang akurat.

Pada set verifikasi, YOLOv10s mencapai presisi 0,806, *recall* 0,873, dan mAP50 0,905. Galat rata-rata diameter adalah 0,70 mm terhadap jangka sorong pada 13 buah. Galat per buah berkisar dari -1,29 mm sampai +2,21 mm. Penulis menyimpulkan metode ini belum cocok untuk pengukuran akurat tetapi dapat dipakai membandingkan ukuran relatif.

Keterbatasan dari teks: tidak ada pencacahan buah dan tidak ada penautan buah antarframe. Dua video dari sudut berbeda hanya dipakai untuk mengambil diameter maksimum satu buah. Sampel 13 buah kecil. Set uji untuk detektor adalah set verifikasi, bukan uji terpisah, dan pembagian per pohon tidak disebut. Metrik untuk RTMDet tidak dilaporkan. Penulis menyebut oklusi daun, kemiringan buah, galat *depth*, dan sudut pandang kamera sebagai sumber galat.
