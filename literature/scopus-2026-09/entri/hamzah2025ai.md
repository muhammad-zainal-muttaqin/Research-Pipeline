# AI-Driven Delta Robot System for Automated Loose Fruitlet Collection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hamzah2025ai` |
| Judul asli | AI-Driven Delta Robot System for Automated Loose Fruitlet Collection |
| Penulis | Hamzah, Amirullah; Mustafa, Farhan; Jailani, Bayhaqi; Hasan, Hasmarina; Kadim, Zulaikha |
| Tahun | 2025 |
| Venue | 2025 11th International Conference on Robotics and Artificial Intelligence Icrai 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hamzah2025ai.pdf](../pdf/hamzah2025ai.pdf)
- DOI resmi: https://doi.org/10.1109/icrai68431.2025.11396727

## Gambaran Umum

Kajian ini membangun sistem robot *delta* untuk mengumpulkan brondolan (buah lepas) kelapa sawit secara otomatis. Penulis menyebut pengumpulan manual padat karya dan menyebabkan kehilangan hasil bila brondolan tertinggal. Sistem harus mendeteksi, menentukan posisi, dan memungut brondolan, dengan target akurasi deteksi di atas 85% dan laju lebih dari 40 buah per menit.

Data: set data brondolan sawit yang disebut "terkurasi", tetapi jumlah citra, pemberi label, dan pembagian latih-uji tidak disebut. Kamera tunggal (monokular) memotret nampan. Pengujian pengumpulan memakai 100 brondolan di tiga jenis permukaan: ubin, jalan aspal, dan rumput. Perangkat keras adalah NVIDIA Jetson AGX Orin, kamera industri, pengendali robot *delta*, dan pengendali vakum.

Metode: citra diluruskan menjadi pandangan atas dengan homografi (transformasi proyektif antarbidang), lalu YOLOv8 mendeteksi brondolan di dalam daerah lingkaran. Titik tengah kotak dipetakan ke koordinat robot dengan homografi kedua dan koreksi tambahan per zona dari tabel 9 zona. Robot melakukan gerak turun lalu angkat dengan ujung penghisap vakum. Tahap verifikasi menghitung brondolan dan menangani kegagalan.

Hasil: mAP@50 93,3% (syarat 85%), 15,2 FPS, latensi inferensi 85 ms, galat pemetaan rata-rata ±4,6 mm. Siklus ambil rata-rata 1,1 detik, setara lebih dari 54 buah per menit. Efisiensi pengumpulan rata-rata 94,5%; akurasi deteksi 95,6% (ubin), 94,5% (aspal), 93,5% (rumput), laju pengumpulan 96%, 93%, 95%.

Keterbatasan: data uji mAP tidak dijelaskan. Penulis menyatakan model mengandaikan pencahayaan stabil dan geometri nampan datar, dan kalibrasi 9 zona tetap membatasi adaptasi. Evaluasi dilakukan pada kondisi terkendali. Verifikasi pencacahan tidak dievaluasi terhadap hitung tangan secara terpisah.
