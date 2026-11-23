# An Integrated Target Recognition Method Based on Improved Faster-RCNN for Apple Detection, Counting, Localization, and Quality Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yan2024integrated` |
| Judul asli | An Integrated Target Recognition Method Based on Improved Faster-RCNN for Apple Detection, Counting, Localization, and Quality Estimation |
| Penulis | Yan, Zihao; Zhang, Huishan; Li, Liping |
| Tahun | 2024 |
| Venue | 2024 IEEE 4th International Conference on Power Electronics and Computer Applications Icpeca 2024 |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [yan2024integrated.pdf](../pdf/yan2024integrated.pdf)
- DOI resmi: https://doi.org/10.1109/icpeca60615.2024.10471151

## Gambaran Umum

Penulis menangani empat masalah pada kebun apel untuk robot pemetik: sebaran buah yang rapat, lokalisasi buah yang kurang tepat, penilaian kematangan yang tidak akurat, dan tidak adanya estimasi kuantitas serta mutu dalam satu model. Mereka mengusulkan satu rangkaian metode yang mendeteksi, mencacah, melokalisasi, mengklasifikasi kematangan, dan memperkirakan berat apel dari citra tunggal.

Data berupa 200 citra apel berformat jpg berukuran 270x180 piksel yang diambil dari internet (Google), lalu diperbesar jumlahnya dengan augmentasi. Sensor dan lokasi kebun tidak disebut. Pemberi label tidak disebut. Pembagian latih dan uji tidak dinyatakan. Kelas deteksi adalah apel tidak tertutup dan apel tertutup sebagian. Kematangan dibagi empat tingkat menurut warna kulit: terlalu matang, matang, setengah matang, dan belum matang.

Detektornya adalah *Faster R-CNN* (detektor dua tahap yang mengusulkan wilayah lalu mengklasifikasinya) dengan *backbone* ResNet50, *Feature Pyramid Network* (FPN, penggabungan fitur berbagai skala), modul perhatian CBAM (pembobot kanal dan spasial), dan penyesuaian *anchor* awal. Hitungan diperoleh dari segmentasi *watershed* berbasis transformasi jarak, lalu lingkaran hasil *fitting* yang kecil dibuang (radius kurang dari dua pertiga rata-rata) dan lingkaran yang berdekatan digabung. Berat diperkirakan dari diameter dan volume dengan model linear multivariat.

Model akhir (M4) mencapai mAP 95,42% pada data apel penulis, naik dari 77,11% untuk *Faster R-CNN* dasar. MIoU lokalisasi 97,14% untuk apel tidak tertutup dan 88,93% untuk apel tertutup sebagian. Waktu deteksi 134 ms per citra, dibanding 226 ms. Pada 10 citra berisi 125 apel, galat hitungan rata-rata 3,86% dan akurasi 95,94%. Korelasi model berat linear 0,9386.

Keterbatasan: citra sedikit dan kecil, tidak ada pembagian latih/uji yang disebut, dan evaluasi hitungan hanya 10 citra. Teks menyebut mAP 94,99% maksimum pada kurva dan 95,42% pada tabel tanpa penjelasan. Klasifikasi kematangan empat tingkat dinyatakan tetapi tidak ada hasil kuantitatif per kelas. Acuan berat tidak dijelaskan.
