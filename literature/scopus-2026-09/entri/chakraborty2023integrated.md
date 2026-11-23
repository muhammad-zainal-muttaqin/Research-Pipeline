# An Integrated Framework for Smart Monitoring of Orange Orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chakraborty2023integrated` |
| Judul asli | An Integrated Framework for Smart Monitoring of Orange Orchard |
| Penulis | Chakraborty, Shuvam; Jana, Susovan |
| Tahun | 2023 |
| Venue | 2023 7th International Conference on Electronics Materials Engineering and Nano Technology Iementech 2023 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [chakraborty2023integrated.pdf](../pdf/chakraborty2023integrated.pdf)
- DOI resmi: https://doi.org/10.1109/iementech60402.2023.10423538

## Gambaran Umum

Penulis mengusulkan kerangka pemantauan kebun jeruk yang menggabungkan kamera, penyimpanan awan (*cloud*), *Internet of Things* (IoT), dan pembelajaran mesin. Kerangka itu mengirim jumlah jeruk dan notifikasi hasil panen kepada petani. Penulis juga membandingkan tiga metode untuk mendeteksi dan mencacah jeruk yang saling menumpuk (*overlap*).

Kerangka mengasumsikan kamera beresolusi tinggi ditempatkan di depan setiap pohon agar seluruh sisi pohon terliput, dengan pengambilan ulang tiap 5 sampai 10 menit. Kerangka ini tidak diuji. Data pembanding hanya 27 citra jeruk yang disiapkan penulis, dengan 1 sampai 6 jeruk per citra, sebagian bertumpuk dan sebagian tidak. Lokasi, kamera, pemberi label, dan pembagian latih dan uji tidak disebut. Acuan hitung per citra tercantum di Tabel I tanpa keterangan asalnya.

Metode pertama mengubah citra ke ruang warna LAB, mengelompokkan piksel dengan *K-means* (k=3), membersihkan dengan operasi morfologi, lalu mendeteksi lingkaran dengan *Hough Circle Transform*, yaitu pencarian bentuk lingkaran dari tepi citra. Metode kedua memakai ambang warna HSV, kabur Gaussian, dan transformasi Hough yang sama, dengan pembuangan lingkaran yang radiusnya menyimpang dari rata-rata. Metode ketiga memakai YOLOv3 berbobot terlatih sebelumnya dengan kelas "orange" dari COCO, masukan 416x416, dan penekanan non-maksimum (*non-maximum suppression*). Tidak ada pelatihan khusus jeruk yang disebut.

Pada 27 citra, akurasi, presisi, dan skor F1 masing-masing 0,6296, 0,6197, dan 0,6185 untuk K-means dengan kuadrat jarak terkecil. Transformasi Hough mencapai 0,7778, 0,8183, dan 0,7590. YOLOv3 mencapai 0,5555, 0,7161, dan 0,5111. Penulis menyimpulkan transformasi Hough paling baik. Pada Tabel I, YOLOv3 menghitung 1 jeruk pada Orange1 (sebenarnya 2), Orange10 (sebenarnya 5), dan Orange25 (sebenarnya 4).

Keterbatasan yang dapat diperiksa dari teks: set data kecil (27 citra) tanpa pembagian latih dan uji, dan tidak ada pembagian per pohon. Cara menghitung akurasi, presisi, dan F1 untuk hitungan per citra tidak diuraikan. Parameter Hough disebut "disetel" tanpa nilai, dan YOLOv3 tidak disesuaikan pada jeruk. Metode tidak menggabungkan beberapa citra pohon yang sama, dan kerangka IoT tidak dievaluasi.
