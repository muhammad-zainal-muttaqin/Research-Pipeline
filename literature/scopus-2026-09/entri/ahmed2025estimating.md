# Estimating optimal crop-load for individual branches in apple tree canopies using YOLOv8

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmed2025estimating` |
| Judul asli | Estimating optimal crop-load for individual branches in apple tree canopies using YOLOv8 |
| Penulis | Ahmed, Dawood; Sapkota, Ranjan; Churuvija, Martin; Karkee, Manoj |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [ahmed2025estimating.pdf](../pdf/ahmed2025estimating.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109697

## Gambaran Umum

Kajian ini membahas estimasi beban panen (*crop-load*) pada cabang apel dari citra RGB-D. Penulis tidak menghitung buah secara langsung dari citra. Mereka mengukur diameter cabang, menghitung luas penampang cabang (*limb cross-sectional area*, LCSA), lalu mengubah LCSA menjadi jumlah buah yang diinginkan per cabang memakai aturan manajemen kebun. Pengukuran diameter dan segmentasi dilakukan dengan YOLOv8-seg pada batang dan cabang di kebun yang kompleks.

Segmentasi batang memakai YOLOv8x-seg dengan precision 92,7%, recall 95,5%, F1 94,1%, AP0.5 96,9%, dan AP0.5:0.95 65,7%. Untuk cabang, penulis memilih YOLOv8m-seg karena skor rata-rata tertingginya 77,3. Model ini memberi recall 72,4%, F1 74,3%, dan AP0.5 76,2%. YOLOv8x-seg memberi precision cabang 77,1% tetapi AP0.5:0.95 hanya 30,5%, sehingga tidak dipilih untuk cabang.

Diameter cabang dihitung dari hasil segmentasi dan data kedalaman. Luas penampang dihitung sebagai π × d² / 4. Jumlah buah yang diinginkan per cabang memakai aturan *Desired Crop Load = 6 × LCSA*, yaitu sekitar enam buah per sentimeter persegi LCSA. Pada pengukuran diameter, RMSE 2,06 mm dengan relRMSE 10,82%. Akurasi diameter dengan toleransi 5 mm adalah 97,67% pada 43 sampel cabang.

Untuk jumlah buah, penulis melaporkan RMSE 3,93 buah per cabang dengan relRMSE 22,25%. Angka ini adalah galat dari hasil yang diturunkan dari LCSA, bukan galat hitung buah dari citra. Galat total karena itu menggabungkan galat segmentasi, galat kedalaman, dan galat aturan manajemen. Teks tidak memisahkan ketiganya.

Kajian ini memiliki beberapa batas. Jumlah sampel evaluasi crop-load hanya 43 cabang. Penulis sendiri menyatakan bahwa akurasi diameter bergantung pada kualitas segmentasi dan sensor kedalaman. Data tersedia atas permintaan, bukan diunggah ke repositori publik, sehingga angka tidak dapat diverifikasi ulang dari data mentah. Bagi tinjauan ini, kajian menunjukkan bahwa depth dapat dipakai untuk mengukur geometri cabang yang menjadi dasar estimasi beban panen pada satu pengamatan, tetapi belum menunjukkan penghitungan buah langsung dari citra.
