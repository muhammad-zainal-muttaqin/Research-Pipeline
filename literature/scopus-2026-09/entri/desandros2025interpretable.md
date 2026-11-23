# Interpretable Model for Oil Palm Fruit Ripeness Level Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `desandros2025interpretable` |
| Judul asli | Interpretable Model for Oil Palm Fruit Ripeness Level Classification |
| Penulis | Desandros, Advendio; Suparyanto, Teddy; Nugraha, Nanda Satya; Putra, Dian Pratama; Isnan, Mahmud; Pardamean, Bens |
| Tahun | 2025 |
| Venue | Proceedings 7th International Conference on Informatics Multimedia Cyber and Information System Icimcis 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [desandros2025interpretable.pdf](../pdf/desandros2025interpretable.pdf)
- DOI resmi: https://doi.org/10.1109/icimcis68501.2025.11327346

## Gambaran Umum

Penelitian ini bertujuan menemukan fitur visual yang paling berperan dalam klasifikasi tingkat kematangan tandan buah kelapa sawit. Penulis menyebut penilaian kematangan secara manual oleh pemanen bersifat subjektif dan lambat. Model *deep learning* dinilai terkendala data kecil dan sulit ditafsirkan. Studi ini disebut sebagai studi awal untuk pemodelan *deep learning* di kemudian hari.

Data berasal dari set data publik di Zenodo (rekaman 11114885) yang diambil tenaga ahli Universiti Teknologi Malaysia pada 2024. Isinya 160 buah matang, 60 terlalu matang, dan 130 mentah. Sebagian besar citra memuat satu tandan tanpa tumpang tindih dengan pencahayaan baik. Teks menyebut seluruh set data berisi 350 citra. Data dibagi 80% latih dan 20% uji. Lokasi pengambilan citra dan pemberi label tidak disebut.

Dari setiap citra diekstraksi 354 fitur buatan tangan: histogram warna 32 *bin* pada ruang warna RGB, HSV, dan YCrCb; indeks warna dan statistik; momen RGB; *Local Binary Pattern* (LBP, pola biner lokal yang membandingkan piksel pusat dengan tetangganya); *Gray Level Co-occurrence Matrix* (GLCM, matriks frekuensi pasangan intensitas piksel bertetangga); dan fitur tekstur Haralick. Karena fitur lebih banyak daripada citra, dipakai *Partial Least Squares* (PLS, proyeksi ke komponen laten yang berkorelasi dengan label). Klasifikasi memakai regresi logistik (LR) dan *Support Vector Classification* berinti RBF (RBF_SVC), dengan validasi silang lima lipatan. Kepentingan fitur dihitung dari koefisien PLS.

PLS-LR dengan 14 komponen memperoleh akurasi validasi silang 0,8393 ± 0,0253, presisi 0,8391 ± 0,0276, *recall* 0,8186 ± 0,0191, dan F1 0,8233 ± 0,0185. Pada data uji, akurasinya 0,8286 dan F1 0,8080. PLS-RBF_SVC dengan 18 komponen memperoleh akurasi validasi silang 0,8250 ± 0,0346 dan akurasi uji 0,8143. Fitur terpenting berasal dari histogram HSV dan YCrCb, indeks warna, momen warna, dan LBP.

Keterbatasan yang disebut penulis: data hanya ratusan citra berkualitas tinggi sehingga generalisasi ke citra tumpang tindih, berderau, redup, atau rusak belum teruji. Tidak ada pembagian per pohon, dan pohon asal citra tidak disebut. Tidak ada pencacahan buah. Penjelasan fitur LBP disebut penulis perlu diteliti lebih lanjut.
