# A hierarchical approach to apple identification for robotic harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `silwal2016hierarchical` |
| Judul asli | A hierarchical approach to apple identification for robotic harvesting |
| Penulis | Silwal, Abhisesh; Karkee, Manoj; Zhang, Qin |
| Tahun | 2016 |
| Venue | Transactions of the Asabe |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [silwal2016hierarchical.pdf](../pdf/silwal2016hierarchical.pdf)
- DOI resmi: https://doi.org/10.13031/trans.59.11619

## Gambaran Umum

Kajian ini membahas kesulitan identifikasi apel pada sistem pemanenan robotik. Buah yang tertutup daun atau berkelompok sulit dikenali oleh sistem penglihatan mesin. Kondisi pencahayaan di kebun juga memperparah masalah tersebut. Penulis mengusulkan pendekatan hierarkis. Buah yang paling jelas terlihat dipanen lebih dahulu, lalu kanopi dicitra ulang agar buah yang tertutup menjadi lebih terlihat. Tujuan penelitian adalah mengukur akurasi identifikasi dan panen yang dapat dicapai dengan pendekatan sederhana ini di lapangan.

Data berasal dari kebun komersial di Prosser, Washington, Amerika Serikat. Tanamannya apel Jazz dengan bentuk *tall spindle*, dengan jarak baris 2,74 m dan jarak antarpohon 1,17 m. Citra diambil pada musim panen 2014 menggunakan kamera CCD Prosilica GigeE 1290C dengan lensa 6 mm dan resolusi 1280 × 960 piksel. Kamera berjarak sekitar 1 m dari batang. Apel berdiameter 6 sampai 8 cm terpetakan menjadi 35 sampai 70 piksel. Kamera dipasang pada platform *over-the-row* dengan tirai kedap cahaya dan lampu LED terdifusi, sehingga citra siang dan malam relatif seragam. Penelitian mencakup 20 pohon, 240 bagian kanopi, dan 740 citra. Rata-rata terdapat 90 apel per pohon, dengan total 1827 apel yang dihitung secara manual.

Metode memakai *circular Hough transform* (CHT) dan analisis *blob* yang dijalankan berulang pada setiap citra. CHT mengenali buah yang terlihat jelas, sedangkan analisis *blob* menemukan buah yang sebagian tertutup. Pada iterasi pertama, hanya buah hasil CHT yang dipanen tangan. Pada iterasi berikutnya, kedua metode dipakai bersama. Proses berhenti ketika algoritma tidak lagi menemukan apel. Waktu hitung rata-rata per citra pada iterasi pertama sekitar 6 s. Waktu ini turun di bawah 1 s untuk citra tanpa apel. Algoritma mendeteksi 1789 dari 1827 apel, sehingga akurasi identifikasi mencapai 98%. Negatif palsu sebesar 2%, yaitu 38 apel, dan positif palsu sebesar 7%, yaitu 130 hitungan. Sekitar 80% apel dapat dipanen dari satu sisi kanopi, dan sisanya dari sisi seberang.

Penulis menyebut bahwa negatif palsu terutama terjadi karena sebagian apel tidak terlihat dari kedua sisi kanopi. Sejumlah apel yang sepenuhnya hijau juga tidak dikenali algoritma. Positif palsu sebagian besar berupa hitungan ganda untuk satu apel. Penulis menyarankan informasi lokasi 3D untuk menghapus hitungan ganda yang berjarak lebih dekat daripada rata-rata diameter apel. Penulis juga menyatakan bahwa kecepatan komputasi belum dioptimalkan, karena implementasi memakai Matlab tanpa optimasi. Penelitian ini tidak mencakup lokalisasi dan deteksi halangan. Semua apel yang teridentifikasi dianggap dapat dipanen, dan pemanenan dilakukan secara manual untuk demonstrasi.
