# KFuji RGB-DS database: Fuji apple multi-modal images for fruit detection with color, depth and range-corrected IR data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2019kfuji` |
| Judul asli | KFuji RGB-DS database: Fuji apple multi-modal images for fruit detection with color, depth and range-corrected IR data |
| Penulis | Gen\'e-Mola, Jordi; Vilaplana, Ver\'onica; Rosell-Polo, Joan R.; Morros, Josep-Ramon; Ruiz-Hidalgo, Javier; Gregorio, Eduard |
| Tahun | 2019 |
| Venue | Data in Brief |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2019kfuji.pdf](../pdf/genemola2019kfuji.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2019.104289

## Gambaran Umum

Artikel data ini memperkenalkan basis data KFuji RGB-DS, kumpulan citra multimodal buah apel Fuji di pohon untuk deteksi dan lokalisasi buah. Penulis menyatakan bahwa sensor RGB-D memberi informasi 3D bersama data warna, tetapi kurangnya kumpulan data yang memadai menghambat pemanfaatannya. Basis data ini ditujukan untuk pelatihan, validasi, dan pembandingan algoritma deteksi buah yang memakai sensor RGB-D.

Data dikumpulkan di kebun apel komersial Tarasso, Agramunt, Catalonia, Spanyol, tiga minggu sebelum panen (tahap BBCH 85). Sensor yang dipakai adalah dua Microsoft Kinect v2, masing-masing terdiri atas kamera RGB dan sensor kedalaman *time-of-flight* (ToF). Setiap pengambilan menghasilkan tiga modalitas: warna (RGB), kedalaman (D), dan intensitas IR yang dikoreksi jarak (S). Pengambilan dilakukan pada malam hari dengan lampu buatan, karena kinerja sensor kedalaman turun di bawah sinar matahari langsung. Total 967 citra multimodal berukuran 548 × 373 piksel dihasilkan dengan membagi setiap pengambilan menjadi sembilan citra. Sebanyak 12.839 apel dianotasi manual dengan *bounding box* persegi panjang, dan anotasinya disediakan dalam format CSV dan XML.

Metode pra-pemrosesannya terdiri atas beberapa langkah. Intensitas IR dikoreksi jarak mengikuti metode pada referensi [1]. Awan titik 3D diproyeksikan ke bidang fokus kamera, lalu citra RGB, D, dan S diregistrasi secara geometris terhadap citra RGB resolusi tinggi sehingga setiap piksel berkorespondensi antarkanal. Nilai D dan S dinormalisasi ke rentang 0 sampai 255 agar rerata dan varians antarkanal mirip, yang menurut penulis mempercepat konvergensi pelatihan jaringan saraf konvolusional. Teks ini tidak melaporkan metrik deteksi. Penulis hanya menyebut bahwa makalah pendampingnya memakai Faster R-CNN untuk mendeteksi buah pada himpunan data ini, dan hasil kuantitatifnya ada di makalah tersebut.

Penulis menyatakan satu batasan teknis yang jelas: kinerja sensor kedalaman turun di bawah sinar matahari, sehingga seluruh data diambil malam hari dengan pencahayaan buatan. Data berasal dari satu kebun komersial dan satu varietas apel, sehingga teks ini tidak menyatakan kondisi lain di luar itu. Penulis juga menyebut bahwa setiap modalitas dibuat berkorespondensi piksel demi piksel, tetapi teks tidak menguji seberapa presisi penyelarasan itu terhadap posisi buah sebenarnya.
