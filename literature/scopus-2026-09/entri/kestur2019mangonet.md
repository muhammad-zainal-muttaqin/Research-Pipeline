# MangoNet: A deep semantic segmentation architecture for a method to detect and count mangoes in an open orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kestur2019mangonet` |
| Judul asli | MangoNet: A deep semantic segmentation architecture for a method to detect and count mangoes in an open orchard |
| Penulis | Kestur, Ramesh; Meduri, Avadesh; Narasipura, Omkar |
| Tahun | 2019 |
| Venue | Engineering Applications of Artificial Intelligence |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [kestur2019mangonet.pdf](../pdf/kestur2019mangonet.pdf)
- DOI resmi: https://doi.org/10.1016/j.engappai.2018.09.011

## Gambaran Umum

Kajian ini (Kestur dkk., 2019) mengusulkan MangoNet, jaringan segmentasi semantik konvolusional penuh (*fully convolutional network*) untuk menghitung buah mangga dari satu citra RGB di kebun terbuka. Jaringan menghasilkan peta piksel buah, lalu objek yang saling terhubung pada peta itu dihitung sebagai buah. Masalah yang dituju adalah penghitungan manual yang lambat, sedangkan kajian ini membatasi diri pada satu pandang dan satu pohon per citra.

Data latih berasal dari 40 citra, yang dipotong menjadi 11.096 patch berukuran 200×200 piksel. Data uji berasal dari 4 citra, yang dipotong menjadi 1.500 patch dan memuat 426 mangga. Pembanding utamanya adalah Arch4, varian lain yang juga berbasis konvolusi penuh. Arsitektur FCNnet dibuang karena performanya buruk pada citra uji. Penulis memakai ambang keyakinan piksel 0,6, bukan 0,5, yang dipilih secara empiris.

Pada evaluasi piksel (Tabel 5), MangoNet mencapai F1 rerata 0,6325, presisi 0,9140, dan recall 0,48. Arch4 mencapai F1 0,4172, presisi 0,8428, dan recall 0,2806. Presisi yang tinggi berarti piksel yang ditandai sebagai buah umumnya benar, tetapi recall hampir separuh berarti banyak buah tidak terdeteksi. Pada evaluasi penghitungan (Tabel 7), akurasi hitung MangoNet 73,6% dibanding 51% untuk Arch4, dengan F1 tingkat objek 0,844 dibanding 0,667. Penulis menyatakan bahwa metode ini *invariant* terhadap skala, pencahayaan, kontras, dan oklusi dibanding pembandingnya.

Keterbatasan kajian ini perlu dicatat. Data uji hanya 4 citra dari satu kebun, dan ambang 0,6 dipilih pada data yang sama tanpa himpunan validasi terpisah yang dilaporkan. Recall 0,48 membuat hitungan cenderung rendah pada buah yang tertutup atau kecil, dan ini tidak dianalisis lebih lanjut dalam teks. Penulis sendiri menyebut dua arah lanjutan, yaitu citra panorama 360° dan kebun dengan banyak pohon.
