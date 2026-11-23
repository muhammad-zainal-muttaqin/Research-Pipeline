# Identification using the K -Means Clustering and Gray Level Co-occurance Matrix (GLCM) At Maturity Fruit Oil Head

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sukemi2019identification` |
| Judul asli | Identification using the K -Means Clustering and Gray Level Co-occurance Matrix (GLCM) At Maturity Fruit Oil Head |
| Penulis | Sukemi; Sukrisno, Edi |
| Tahun | 2019 |
| Venue | Proceedings of 2019 4th International Conference on Informatics and Computing Icic 2019 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [sukemi2019identification.pdf](../pdf/sukemi2019identification.pdf)
- DOI resmi: https://doi.org/10.1109/icic47613.2019.8985681

## Gambaran Umum

Penulis menyatakan bahwa penilaian kematangan buah sawit secara visual bersifat subjektif dan tidak konsisten antarpenilai. Tujuan penelitian ialah mengidentifikasi kematangan *fresh fruit bunch* (FFB) dari citra digital dengan *K-means clustering* dan *Gray Level Co-occurrence Matrix* (GLCM). Buah dikelompokkan ke dalam dua kelas, yaitu matang dan tidak matang. Pendahuluan merujuk studi GLCM pada apel dan segmentasi *K-means* dengan akurasi di atas 60%.

Data berupa citra digital buah sawit. Teks tidak menyebut lokasi pengambilan gambar, jenis kamera, atau jumlah citra latih secara lengkap. Basis data acuan terdiri atas 8 citra, yaitu 4 matang dan 4 tidak matang. Data uji berjumlah 50 citra, dengan 25 citra per kelas. Teks tidak menyebut siapa pemberi label dan tidak menyebut pembagian per pohon.

Metode terdiri atas segmentasi, ekstraksi fitur, dan identifikasi. *K-means clustering* mengelompokkan piksel menurut kemiripan nilai RGB agar buah terpisah dari latar. GLCM menghitung statistik tekstur dari pasangan piksel bertetangga, yaitu *contrast*, *correlation*, *energy*, dan *homogeneity*. Identifikasi dilakukan dengan mencari jarak *Euclidean* terdekat terhadap basis data. Teks tidak menyebut model belajar mesin.

Hasil utama adalah akurasi 90% pada 50 data uji (Tabel 3.2): 45 benar dan 5 salah. Kelas matang 25 dari 25 benar (100%). Kelas tidak matang 20 dari 25 benar (80%). Teks tidak melaporkan presisi, recall, atau galat lain.

Keterbatasan yang dapat diperiksa dari teks: basis data hanya 8 citra dan data uji hanya 50 citra. Tidak ada validasi silang, tidak ada data uji dari pohon atau kebun lain, dan tidak ada perbandingan dengan metode lain. Kondisi pencahayaan hanya disebut secara umum.
