# Assessing automatic data processing algorithms for RGB-D cameras to predict fruit size and weight in apples

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `miranda2023assessing` |
| Judul asli | Assessing automatic data processing algorithms for RGB-D cameras to predict fruit size and weight in apples |
| Penulis | Miranda, Juan C.; Arn\'o, Jaume; Gen\'e-Mola, Jordi; Lordan, Jaume; As\'\in, Luis; Gregorio, Eduard |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [miranda2023assessing.pdf](../pdf/miranda2023assessing.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108302

## Gambaran Umum

Miranda dkk. (2023) menguji apakah kamera RGB-D dapat dipakai di kebun apel untuk mengukur ukuran dan berat buah. Kamera yang dipakai adalah Azure Kinect, yang memberi citra warna dan citra kedalaman (*depth*) secara bersamaan. Dari setiap buah diukur dua sumbu: D1 (sumbu terpanjang) dan D2 (sumbu terpendek). Kedua ukuran itu lalu dimasukkan ke model alometrik untuk memprediksi berat buah.

Pertanyaan utamanya adalah seberapa akurat ukuran dan berat yang diestimasi dari kamera di lapangan. Pengujian dilakukan pada 27 September 2021 di kebun apel, pada enam waktu rekam antara pukul 11.40 dan 19.24 (UTC+2), untuk melihat pengaruh cahaya. Sebagai acuan dipakai dua bola berdiameter 60 mm dan 120 mm serta dua apel dengan D1 dan D2 yang diukur langsung. Model alometrik dilatih pada 568 data dan diuji pada 489 data laboratorium.

Hasil model prediksi berat cukup baik. Nilai R² berada pada rentang 0,942 sampai 0,993, dan RMSE pada data uji sekitar 9 sampai 16 g. Abstrak melaporkan MAPE 5,1 sampai 5,7 persen, dengan RMSE 11,09 g dan 13,02 g tergantung pada bentuk yang dipakai untuk menyesuaikan bentuk buah (lingkaran, elips, atau kotak pembatas). Pada apel yang tidak tertutup, kombinasi *circle fitting* dan model linear dengan D1 dan D2 memberi MAPE 5,1 persen. Pada apel yang tertutup daun, galat naik menjadi 18,3 persen dengan model linear satu prediktor. Penulis tidak menemukan pola galat yang jelas terhadap iluminasi dari sekitar 15.000 lx pagi hari sampai sekitar 500 lx sore hari.

Batas studi ini perlu dibaca bersama hasilnya. Penulis sendiri menyatakan bahwa galat sizing dan galat model berinteraksi dengan cara yang tidak mudah dikuantifikasi. Model alometrik juga diperingatkan untuk diuji ulang pada kultivar, tahap perkembangan, atau kondisi kanopi lain, karena model dibangun dari data laboratorium pada satu kondisi. Pada model (3) ditemukan VIF 28,46, yang menunjukkan korelasi tinggi antara D1 dan D2. Galat pada apel tertutup, yang untuk sumbu D2 melebihi 10 persen pada sebagian metode, juga menunjukkan bahwa deteksi dan segmentasi buah belum teruji. Penulis memberi label manual pada buah, sehingga deteksi dibuat seolah-olah sempurna.
