# Field Grape Berry Counting Algorithm Based on Spatial Attention Mechanism

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2022field` |
| Judul asli | Field Grape Berry Counting Algorithm Based on Spatial Attention Mechanism |
| Penulis | Tang, Yuling; Li, Yanan; Sun, Ming; Qi, Yang |
| Tahun | 2022 |
| Venue | Proceedings 2022 Chinese Automation Congress Cac 2022 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [tang2022field.pdf](../pdf/tang2022field.pdf)
- DOI resmi: https://doi.org/10.1109/cac57257.2022.10055368

## Gambaran Umum

Penulis menyebut penghitungan butir anggur masih bergantung pada pengamatan manual yang berefisiensi rendah, subjektif, dan berbiaya tenaga tinggi. Metode otomatis terdahulu menurut penulis hanya diuji pada satu konteks dengan jumlah tandan sedikit. Tujuan makalah ini adalah penghitungan butir anggur di kebun yang cepat dan berskala besar, dengan jaringan bernama SAGBCNet (*Spatial Attention Grape Berry Counting Network*).

Data berasal dari set data publik WGISD (*Embrapa Wine Grape Instance Segmentation Dataset*). Penulis memilih 225 citra RGB: 177 berukuran 3456x5184 dan 48 berukuran 864x1296. Lima varietas dipakai: Chardonnay (50 citra), Cabernet Franc (42), Cabernet Sauvignon (38), Sauvignon Blanc (47), dan Syrah (48). Sebanyak 169 citra menjadi data latih dan 56 citra data uji. Setiap butir diberi titik secara manual dengan Labelme 3.16.2, total 156.272 butir, dengan 206 sampai 1.585 butir per citra.

SAGBCNet berbasis MobileCount dan menghitung lewat peta kepadatan (*density map*), yaitu peta yang jumlah nilainya sama dengan jumlah butir. Tulang punggung (*backbone*) memakai empat blok *spatial-bottleneck* dari MobileNetV2 dengan konvolusi *dilated* (konvolusi berlubang yang memperluas bidang pandang) berlaju 1 sampai 4. Modul DANet (*Dual Attention Network*) menghitung hubungan antarposisi dan antarkanal. Fusi fitur menggabungkan empat skala dari dalam ke dangkal. Citra diubah ke 864x1296, dipotong acak 256x1024, dilatih 300 *epoch* dengan Adam.

Pada data uji, SAGBCNet mencapai MAE (galat absolut rerata) 35,59 dan MSE 47,39 per citra menurut Tabel II. Abstrak menulis MAE 35,39, berbeda dari tabel. Pembanding: CSRNet 192,89 dan 246,03; CANNet 199,73 dan 252,57; MobileCount 45,31 dan 57,32; TasselNetV2+ 41,03 dan 55,00. Ablasi: *bottleneck* biasa memberi MAE 39,55 dan MSE 51,96.

Keterbatasan yang dapat diperiksa: data uji hanya 56 citra dari satu set data, tanpa pengulangan atau interval kepercayaan. Pembagian latih-uji per varietas, bukan per tanaman, dan asal citra dari kebun yang sama tidak disebut. Butir yang dihitung dalam satu citra, tanpa penautan antarcitra. Acuan hitung adalah titik anotasi manual per citra. Persentase penurunan galat di teks (misalnya 157,3%) melebihi 100% dan tidak dapat dibaca sebagai penurunan relatif biasa.
