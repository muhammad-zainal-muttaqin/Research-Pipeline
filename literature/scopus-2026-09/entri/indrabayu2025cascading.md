# A Cascading of YOLOv8 and Random Forest Regression in Oil Palm Fresh Fruit Bunch Mass Estimation System using Unmanned Aerial Vehicle Imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `indrabayu2025cascading` |
| Judul asli | A Cascading of YOLOv8 and Random Forest Regression in Oil Palm Fresh Fruit Bunch Mass Estimation System using Unmanned Aerial Vehicle Imagery |
| Penulis | Indrabayu, -; Nurhadi, Muhammad Ijlal; Tandungan, Sofyan; Rahmat, Muhammad Abdillah |
| Tahun | 2025 |
| Venue | International Journal on Informatics Visualization |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [indrabayu2025cascading.pdf](../pdf/indrabayu2025cascading.pdf)
- DOI resmi: https://doi.org/10.62527/joiv.9.6.3137

## Gambaran Umum

Kajian ini mengestimasi massa tandan buah segar (TBS) kelapa sawit dari citra video yang direkam dengan UAV (DJI Mavic Air). Metodenya memakai YOLOv8-Segmentation untuk memisahkan setiap tandan dari latar, mengubah hasil segmentasi menjadi mask biner, lalu mencocokkan elips pada convex hull kontur. Dari elips itu diambil sumbu mayor, sumbu minor, luas, keliling, dan eksentrisitas, yang kemudian menjadi masukan model regresi.

Massa diestimasi dengan Random Forest Regression (RFR) dan XGBoost. Sebanyak 200 tandan dipakai, 100 tertutup pelepah dan 100 tidak tertutup, dengan pembagian data 70:15:15. Massa acuan ditimbang pada timbangan bangku berkapasitas 150 kg dengan ketelitian 500 g.

Hasil utama untuk tandan tertutup pelepah adalah RMSE 3,95 dan MAE 2,87 dengan RFR pada fitur sumbu minor dan eksentrisitas, dengan YOLOv8-Small. Untuk tandan tidak tertutup, hasil terbaik adalah RMSE 3,91 dan MAE 2,91 dengan YOLOv8-Large, memakai fitur sumbu minor, keliling, dan luas. Sistem memilih model dengan cabang logika berdasarkan jumlah objek tersegmentasi dan nilai eksentrisitas (ambang 0,7).

Bagian pembahasan menyebut XGBoost mencapai RMSE sedikit lebih rendah pada satu kondisi, tetapi RFR dipilih sebagai model utama. Kajian ini tidak mengukur jumlah tandan lintas pandang, sehingga tidak membahas deduplikasi antarpandangan. Bagian metode dan hasil yang dibaca belum mencakup seluruh tabel perbandingan.
