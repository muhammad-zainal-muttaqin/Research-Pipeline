# A Study of Oil Palm Fruit Ripeness Using YOLOv8 for Smart Agriculture Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kiet2025study` |
| Judul asli | A Study of Oil Palm Fruit Ripeness Using YOLOv8 for Smart Agriculture Applications |
| Penulis | Kiet, Vo Minh; Chang, Fa-Shian; Tsung, Chen-Kun |
| Tahun | 2025 |
| Venue | Is3c 2025 International Symposium on Computer Consumer and Control |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kiet2025study.pdf](../pdf/kiet2025study.pdf)
- DOI resmi: https://doi.org/10.1109/is3c65361.2025.11131089

## Gambaran Umum

Kajian ini bertujuan mendeteksi dan mengklasifikasikan kematangan tandan buah segar (TBS) kelapa sawit dengan YOLOv8. Penulis menyebut penilaian manual bersifat subjektif, melelahkan, dan tidak konsisten pada perkebunan besar. Penulis ingin menunjukkan bahwa detektor waktu nyata layak dipakai pada kondisi lapangan, yaitu cahaya berubah, latar ramai, dan buah tertutup.

Data berasal dari set data publik Suharjito dkk. yang dikumpulkan di beberapa pabrik kelapa sawit di Kalimantan Selatan. Perekaman memakai ponsel beresolusi 1280×720 pada tumpukan TBS: 101 video (45 satu kategori, 56 multikategori). Satu bingkai per detik diambil, diubah menjadi 416×416 piksel, lalu diberi kotak pembatas dengan DarkLabel dan Roboflow. Set asli berisi 7.171 citra dan 14.559 objek berlabel. Setelah augmentasi, set terdiri atas 18.968 citra latih, 3.205 validasi, dan 2.787 uji. Pembagian per pohon atau per video tidak disebut.

Metode memakai YOLOv8s dan YOLOv8m, detektor satu tahap yang memprediksi kotak dan kelas dalam satu lintasan tanpa jangkar (*anchor-free*). Pelatihan memakai SGD, penjadwal laju belajar kosinus, presisi campuran (*mixed precision*), dan augmentasi Mosaic, MixUp, RandAugment, HSV, penghapusan acak, serta pembalikan horizontal. Metrik: presisi, *recall*, F1, dan mAP.

Hasil pada Tabel I untuk YOLOv8s: presisi 0,992, *recall* 0,997, mAP@0,5 0,995, F1 0,894. YOLOv8m: presisi 0,99, *recall* 0,99, mAP@0,5 0,89, F1 0,90. Pembanding dari Robi dkk. pada 350 citra internet: YOLOv4 mAP 0,772 dan YOLOv3 0,557. Naskah juga menyebut mAP@0,5 di atas 0,995 untuk enam kelas dan di atas 0,90 untuk kelas mentah dan matang.

Keterbatasan yang dapat diperiksa: angka mAP@0,5 YOLOv8m (0,89) dan F1 YOLOv8s (0,894) tidak konsisten dengan klaim di teks. Jumlah kelas disebut enam di satu bagian dan dua (mentah dan matang) di bagian lain. Penulis menyebut hasil sebagai "validasi" dan tidak menyatakan apakah citra uji terpisah dari citra latih sebelum augmentasi. Pembanding memakai set data dan kelas yang berbeda. Tidak ada pencacahan, pelacakan, atau penggabungan pandang. Nilai berasal dari satu set data satu wilayah.
