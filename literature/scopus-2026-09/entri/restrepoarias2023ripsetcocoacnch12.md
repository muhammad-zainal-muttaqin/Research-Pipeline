# RipSetCocoaCNCH12: Labeled Dataset for Ripeness Stage Detection, Semantic and Instance Segmentation of Cocoa Pods

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `restrepoarias2023ripsetcocoacnch12` |
| Judul asli | RipSetCocoaCNCH12: Labeled Dataset for Ripeness Stage Detection, Semantic and Instance Segmentation of Cocoa Pods |
| Penulis | Restrepo-Arias, Juan Felipe; Salinas-Agudelo, Mar\'\ia Isabel; Hernandez-P\'erez, Mar\'\ia Isabel; Marulanda-Tob\'on, Alejandro; Giraldo-Carvajal, Mar\'\ia Camila |
| Tahun | 2023 |
| Venue | Data |
| Kode | C4 (Atribut kelas dan pencacahan) |

## Tautan Akses
- PDF: [restrepoarias2023ripsetcocoacnch12.pdf](../pdf/restrepoarias2023ripsetcocoacnch12.pdf)
- DOI resmi: https://doi.org/10.3390/data8060112

## Gambaran Umum

Makalah ini menyajikan dataset berlabel untuk deteksi tahap kematangan, segmentasi semantik, dan segmentasi instansi buah kakao. Penentuan tahap kematangan diperlukan untuk merencanakan waktu panen dan memprediksi volume produksi. Teknik yang ada, seperti sinyal akustik, penanda biokimia, dan pencitraan laser, memerlukan perangkat mahal serta sulit diterapkan di lapang. Model pembelajaran mendalam sangat bergantung pada jumlah dan mutu data latih, sementara dataset publik untuk kakao masih terbatas. Penulis mempublikasikan RipSetCocoaCNCH12 sebagai dataset terbuka untuk mengatasi kekurangan tersebut.

Objek yang dipakai adalah kakao varietas CNCH12 dari kebun Compañía Nacional de Chocolates di Támesis, Antioquia, Kolombia, pada ketinggian rata-rata sekitar 1.100 meter. Citra dikumpulkan dari 1 Desember 2022 hingga 17 Februari 2023 pada musim panen utama. Dataset memuat lima kelas, yaitu C1 (0–2 bulan) dengan 3.278 instans, C2 (2–4 bulan) dengan 1.688 instans, C3 (4–6 bulan) dengan 1.519 instans, C4 (siap panen, lebih dari 6 bulan) dengan 1.169 instans, dan CA (buah aborsi) dengan 263 instans, sehingga totalnya 7.917 instans dalam 4.116 citra. Pengambilan memakai lima jenis ponsel, yaitu Samsung Galaxy A01, Samsung Galaxy Note 10, iPhone SE 2020, LG G5, dan Motorola G9 Plus, antara pukul 08.00 dan 16.00. Setiap buah difoto dari satu sampai empat sudut mengikuti lintasan zigzag di kebun. Citra asli berukuran 3072 × 3072 hingga 4096 × 4096 piksel diubah menjadi 3000 × 3000 piksel berformat JPEG 8-bit dengan Pillow; total ukuran dataset 27 GB.

Mekanisme pelabelan memakai CVAT dengan anotasi poligon untuk menghasilkan segmentasi semantik. Dataset disediakan dalam dua format, yaitu COCO 1.0 berupa berkas JSON yang memuat kotak pembatas dan poligon untuk deteksi, serta segmentation mask 1.1 yang memuat folder terpisah untuk segmentasi semantik dan instansi. Tiap folder citra didominasi satu kelas, meskipun satu citra dapat memuat beberapa instans dari kelas berbeda. Untuk menguji apakah pembagian kelas benar secara biologis, penulis mengukur derajat Brix atau kandungan gula internal dengan refraktometer genggam pada lebih dari 35 buah per kelas. Rerata yang diukur adalah 5,3 °Bx dari 39 sampel C1, 6,6 °Bx dari 45 sampel C2, 8,7 °Bx dari 38 sampel C3, dan 16,6 °Bx dari 40 sampel C4.

Uji ANOVA terhadap derajat Brix menghasilkan F sebesar 305,72 dan nilai p sebesar 1,12 × 10⁻⁶³, sehingga hipotesis nol yang menyatakan kesamaan rerata keempat kelas ditolak. Penulis menyimpulkan bahwa perbedaan antartahap kematangan signifikan dan pembagian empat kelas valid. Angka yang dapat dihitung ulang dari dataset adalah 4.116 citra, 7.917 instans, lima kelas, dan 27 GB. Karena makalah ini berupa data descriptor, metrik kinerja deteksi seperti presisi, recall, atau mAP tidak dinyatakan; pelatihan dan evaluasi model diserahkan kepada pengguna dataset.

Batasan yang dinyatakan penulis adalah dataset tidak memuat kelas buah kakao yang harus dibuang. Pekerjaan lanjut disarankan untuk menambahkan kelas penyakit dan buah busuk serta mengumpulkan data dari varietas kakao lain. Seluruh citra berasal dari satu varietas, satu kebun, dan satu musim panen, sehingga keragaman varietas belum terwakili. Dataset tersedia terbuka melalui Zenodo dengan DOI 10.5281/zenodo.7968315.
