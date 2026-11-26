# Plant fruit counting using context aware feature and point to point pairing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shao2024plant` |
| Judul asli | Plant fruit counting using context aware feature and point to point pairing |
| Penulis | Shao, Junning; Sun, Kaiqiong; Yi, Zhao; Chen, Zhihao |
| Tahun | 2024 |
| Venue | Proceedings of SPIE the International Society for Optical Engineering |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [shao2024plant.pdf](../pdf/shao2024plant.pdf)
- DOI resmi: https://doi.org/10.1117/12.3000698

## Gambaran Umum

Kajian ini (Proc. SPIE 13086, 2024) mencacah buah per citra dengan jaringan yang memprediksi titik pusat buah. Jaringan ini turunan P2PNet, metode pencacahan kerumunan yang mencocokkan titik prediksi dengan titik acuan memakai algoritme Hungaria.

Fitur VGG dirangkum dengan *pooling* untuk memperoleh informasi konteks, lalu digabung dengan fitur asal sebelum cabang klasifikasi dan regresi titik. Struktur piramida fitur P2PNet dibuang. Pelatihan diawasi langsung dengan label titik, tanpa peta kepadatan Gaussian.

Data berupa set data publik 1.120 citra apel dari fase tumbuh sampai matang yang diambil dari berbagai sudut, dengan label titik di pusat buah. Data dibagi 896 latih, 112 validasi, dan 112 uji. Pada data uji, MAE 0,67 buah dan RMSE 0,98 per citra, lebih rendah daripada CSRNet dan CAN pada data yang sama.

Setiap citra dicacah sendiri. Buah tidak ditautkan antarcitra dan hitungan tidak dijumlahkan per pohon.
