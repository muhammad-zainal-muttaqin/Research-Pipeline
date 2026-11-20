# Tomato yield estimation based on object detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2018tomato` |
| Judul asli | Tomato yield estimation based on object detection |
| Penulis | Liu, Jun |
| Tahun | 2018 |
| Venue | Journal of Advanced Computational Intelligence and Intelligent Informatics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [liu2018tomato.pdf](../pdf/liu2018tomato.pdf)
- DOI resmi: https://doi.org/10.20965/jaciii.2018.p1120

## Gambaran Umum

Kajian ini (Liu, 2018, *Vol. 22 No. 7*, halaman 1122–1125) menghitung jumlah buah tomat per pohon dari citra. Penulis memakai detektor *R-CNN* (*Region-based Convolutional Neural Network*, jaringan saraf konvolusi yang mengusulkan wilayah kandidat lalu mengklasifikasikannya) untuk mendeteksi tomat pada setiap citra. Jumlah deteksi kemudian diubah menjadi estimasi hasil panen memakai regresi linear.

Data yang dipakai berjumlah 20.000 citra dari 5.000 pohon tomat. Setiap pohon difoto dari empat arah. Data dibagi tiga bagian dengan rasio 3:1:1 untuk latih, validasi, dan uji. Pelatihan dijalankan pada GPU GTX-1060 dengan memori 8 GB.

Tahap estimasi bekerja pada tingkat pohon. Jumlah tomat yang terdeteksi dari keempat arah dijumlahkan, lalu regresi linear dengan basis polinom B_j(x) = x^(j-1) memetakan jumlah itu ke hasil aktual. Koefisien dihitung dengan solusi kuadrat terkecil λ = (MᵀM)⁻¹Mᵀy. Tabel 1 memuat 20 sampel pohon yang berisi jumlah tomat terdeteksi dan jumlah aktual per pohon.

Hasil yang dilaporkan hanya galat regresi. Penulis menulis bahwa "the error value has reached a minimum of 100.23, which is very high accuracy for the yield estimation". Angka ini bukan presisi, recall, atau mAP deteksi. Galat itu juga tidak disertai pembanding dengan metode lain, sehingga angka 100,23 tidak dapat ditafsirkan sebagai akurasi deteksi.

Keterbatasan yang disebut penulis mencakup citra yang tidak panoramik, distribusi jumlah tomat yang tidak seimbang, galat yang tinggi pada citra terbatas, dan kebutuhan untuk membedakan tomat milik pohon sendiri dari tomat pohon lain. Keterbatasan terakhir ini langsung berkaitan dengan masalah identitas lintas pandang: tanpa pemisahan pohon, hitungan dari satu pohon dapat tercampur dengan pohon di sebelahnya.

Teks kajian tidak menjelaskan bagaimana tomat yang sama yang terlihat dari dua arah dikenali dan dihitung sekali.
