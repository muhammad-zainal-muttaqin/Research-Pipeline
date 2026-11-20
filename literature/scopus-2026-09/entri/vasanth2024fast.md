# Fast region based convolutional neural network ResNet-50 model for on tree Mango fruit yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vasanth2024fast` |
| Judul asli | Fast region based convolutional neural network ResNet-50 model for on tree Mango fruit yield estimation |
| Penulis | Managali Vasanth, Neethi; PPandian, Raviraj |
| Tahun | 2024 |
| Venue | Indonesian Journal of Electrical Engineering and Computer Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [vasanth2024fast.pdf](../pdf/vasanth2024fast.pdf)
- DOI resmi: https://doi.org/10.11591/ijeecs.v33.i2.pp1084-1091

## Gambaran Umum

Penelitian ini bertujuan mengestimasi hasil panen mangga pada pohon secara otomatis sejak tahap awal. Estimasi dini membantu petani merencanakan panen dan meningkatkan mutu serta jumlah produksi, yang pada akhirnya memengaruhi pasar domestik dan ekspor. Penghitungan manual pada sampel pohon dinilai padat tenaga kerja dan kadang tidak akurat. Penulis mengusulkan model *Fast R-CNN* dengan arsitektur ResNet-50 untuk mendeteksi, mensegmentasi, dan menghitung buah mangga dari citra RGB pohon individu.

Citra diambil dengan kamera utama ponsel pintar pada siang hari dengan resolusi 1920×1080 piksel. Pohon yang dipotret berumur 15 hingga 20 tahun dengan tinggi 7 hingga 8 kaki. Pemotretan dilakukan dari jarak 2 dan 3 meter, dalam dua sesi, yaitu pukul 9.30 hingga 10.00 dan pukul 14.30 hingga 15.00. Pengumpulan data berlangsung lima bulan. Pada tiga bulan pertama data diambil setiap 7 hari, lalu frekuensinya ditingkatkan pada dua bulan berikutnya seiring kematangan buah. Setiap hari diambil 800 foto dari lima varietas, sehingga total dataset berjumlah 21.000 foto. Hanya citra buah mangga matang yang dipakai dalam studi ini. Model dilatih dengan 5.000 citra yang dibagi menjadi 80 persen data latih dan 20 persen data validasi.

Akurasi pelatihan mencapai 98% dan akurasi validasi 96%, dengan loss pelatihan 0,14 dan loss validasi 0,08. Kinerja model diukur dengan *precision*, *recall*, *F1-score*, dan akurasi deteksi pada empat kultivar, yaitu Arkaarun, Malgova, Mallika, dan Raspuri. Model mendeteksi dan mensegmentasi buah dengan akurasi 98%. Abstrak melaporkan akurasi 98,20% pada dataset yang diusulkan. Pada perbandingan dengan penelitian lain, CNN untuk buah plum mencapai 90,00%, FR-CNN untuk apel, mangga, dan jeruk mencapai 91,00%, sedangkan model usulan mencapai 98,00% untuk mangga.

Penulis menyatakan bahwa sebagian buah tetap terlewat karena oklusi, perbedaan pencahayaan, dan salah klasifikasi dengan daun. Tantangan utama terletak pada bentuk dan warna daun serta buah yang mirip, sehingga deteksi objek menjadi lebih sulit. Karena foto buah matang dipakai dalam pelatihan dan daun maupun buah sama-sama hijau, dataset menjadi lebih kompleks dan akurasi pembelajaran meningkat secara perlahan.
