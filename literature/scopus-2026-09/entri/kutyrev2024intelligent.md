# Intelligent crop yield prediction system using neural networks and databases

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kutyrev2024intelligent` |
| Judul asli | Intelligent crop yield prediction system using neural networks and databases |
| Penulis | Kutyrev, Alexey; Zubina, Valeria |
| Tahun | 2024 |
| Venue | Bio Web of Conferences |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [kutyrev2024intelligent.pdf](../pdf/kutyrev2024intelligent.pdf)
- DOI resmi: https://doi.org/10.1051/bioconf/202413001007

## Gambaran Umum

Kajian ini mengusulkan sistem terintegrasi untuk meramalkan hasil panen apel. Sistem menggabungkan *convolutional neural network* (CNN) untuk menghitung buah pada citra pohon, *feedforward neural network* (FNN) untuk meramalkan hasil panen, dan basis data relasional SQLite yang dikelola dengan SQLiteStudio. Penulis menyatakan bahwa pengumpulan data jumlah buah di pohon dapat dibuat lebih sederhana dan lebih cepat dengan otomatisasi. Tujuan utama kajian adalah menyimpan hasil penghitungan dan data cuaca, tanah, serta hasil panen jangka panjang dalam satu struktur yang dapat dipakai untuk peramalan.

Data yang dipakai untuk penghitungan buah berupa citra dan video dari pemantauan di darat. Teks tidak menyebut lokasi kebun, jumlah pohon, jumlah citra, atau jenis sensor kamera. Data untuk FNN berasal dari stasiun cuaca, data tanah, data hasil panen jangka panjang, dan keluaran CNN. Data FNN dibagi menjadi 70% latih, 15% validasi, dan 15% uji. Jumlah sampel tidak dilaporkan.

Penghitungan buah memakai *YOLOv8* (*You Only Look Once* versi 8), detektor objek yang memprediksi kotak pembatas dan kelas objek dalam satu kali proses. Sebuah skrip Python memeriksa folder citra dan memproses setiap berkas JPG baru dengan YOLOv8. Jumlah buah hasil deteksi dicatat ke basis data. Skrip dijalankan berulang dengan jeda, misalnya satu jam. FNN memiliki lima lapisan tersembunyi dengan aktivasi ReLU dan satu neuron keluaran yang meramalkan hasil panen dalam ton per hektare. Model dilatih dengan *backpropagation* dan optimizer Adam. Pada data uji, FNN mencapai *mean square error* (MSE) 7,33 dan *mean absolute percentage error* (MAPE) 6,27%. Teks tidak melaporkan akurasi, presisi, atau galat penghitungan buah oleh YOLOv8. Gambar 6 hanya menunjukkan contoh hasil deteksi pada satu citra.

Penulis menyimpulkan bahwa kombinasi FNN, CNN, dan basis data efektif untuk peramalan hasil panen. Kesimpulan juga menyatakan bahwa penghitungan otomatis membuat pengumpulan data lebih cepat dan peramalan lebih akurat. Klaim akurasi penghitungan itu tidak didukung angka dalam teks. Angka yang ada hanya galat peramalan FNN, dan pembandingnya tidak disebut.
