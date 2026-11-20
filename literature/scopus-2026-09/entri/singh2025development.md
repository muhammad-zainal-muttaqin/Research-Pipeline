# Development of a smartphone application for rapid blueberry detection and yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `singh2025development` |
| Judul asli | Development of a smartphone application for rapid blueberry detection and yield estimation |
| Penulis | Singh, Puranjit; Niknejad, Nariman; Spiers, James D.; Bao, Yin; Ru, Sushan |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [singh2025development.pdf](../pdf/singh2025development.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101361

## Gambaran Umum

Pemantauan hasil panen blueberry penting untuk perencanaan panen, strategi pemasaran, dan program pemuliaan. Penghitungan hasil secara manual dengan memanen dan menimbang buah memakan banyak tenaga kerja. Estimasi visual sebelum panen juga sering tidak akurat karena buah yang banyak sulit dihitung. Penelitian ini mengembangkan dan menguji alur kerja untuk memprediksi hasil tiap tanaman dari citra smartphone. Alur kerja ini menggabungkan deteksi buah berbasis *deep learning* dengan data kunci tanaman. Tujuannya ada tiga. Pertama, menguji performa YOLOv8 untuk deteksi blueberry pada beberapa kultivar di lapangan. Kedua, menilai kelayakan prediksi hasil berbasis jumlah buah hasil deteksi, berat rata-rata buah, dan genotipe. Ketiga, membuat aplikasi smartphone yang mudah dipakai untuk pemantauan hasil dan kematangan secara *real-time*.

Citra diambil di Auburn, Alabama, pada 20 Juni 2022. Kamera yang digunakan adalah smartphone Pixel 6 Pro. Kamera berada sekitar 1 meter di atas tanah dan sekitar 2 meter dari tanaman, sehingga seluruh tanaman masuk dalam bingkai. Citra disimpan dalam format JPG berukuran 3024 × 4032 piksel. Tanaman berasal dari genotipe *southern highbush* dan *rabbiteye*, termasuk kultivar Alapaha, Premier, Powderblue, serta genotipe AU 6, AU 7, dan AU 8. Buah matang dipanen secara manual dari setiap sisi tanaman. Buah dari tiap sisi dihitung dan ditimbang terpisah untuk memperoleh berat rata-rata buah dan hasil per sisi. Citra dipangkas untuk membuang latar dan tanaman tetangga, lalu dibagi menjadi sub-citra 224 × 224 piksel. Pembagian ini menghasilkan 17.432 citra. Anotasi dibuat dengan alat Smart Polygon pada Roboflow. Buah dibagi menjadi dua kelas, yaitu matang dan belum matang, berdasarkan warna. Data dibagi 70 persen untuk latih, 15 persen untuk validasi, dan 15 persen untuk uji. Hasilnya, terdapat 12.202 citra latih dan masing-masing 2.615 citra validasi dan uji.

Model YOLOv8 dilatih dalam beberapa varian, dari yang ringan YOLOv8-n sampai YOLOv8-x. Model terbaik, YOLOv8-x, mencapai *mean average precision* (mAP50) sebesar 0,708. Jumlah buah matang yang terlihat dari dua sisi tanaman, bersama berat rata-rata buah dan genotipe, dipakai untuk melatih 42 model regresi pembelajaran mesin. Tiga strategi pemanfaatan data hitungan buah dua sisi juga diuji. Regresor *histogram-based gradient boosting* memberikan performa terbaik, dengan R² sebesar 0,80, bias 16,48 g, dan batas kesepakatan [−440,28 g; 473,24 g]. Arsitektur tanaman dan oklusi buah matang juga bervariasi secara signifikan antargenotipe. Peneliti menyimpulkan bahwa fitur arsitektur yang diperoleh dari citra dapat menjadi proksi praktis untuk genotipe pada model prediksi hasil di masa depan. Seluruh alur pengolahan citra dan pemodelan dikemas dalam aplikasi Android bernama Blueberry Yield Analyzer, yang tersedia di Google Play Store.
