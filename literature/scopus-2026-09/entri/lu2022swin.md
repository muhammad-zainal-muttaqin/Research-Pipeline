# Swin-Transformer-YOLOv5 for Real-Time Wine Grape Bunch Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lu2022swin` |
| Judul asli | Swin-Transformer-YOLOv5 for Real-Time Wine Grape Bunch Detection |
| Penulis | Lu, Shenglian; Liu, Xiaoyu; He, Zixuan; Zhang, Xin; Liu, Wenbo; Karkee, Manoj |
| Tahun | 2022 |
| Venue | Remote Sensing |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [lu2022swin.pdf](../pdf/lu2022swin.pdf)
- DOI resmi: https://doi.org/10.3390/rs14225853

## Gambaran Umum

Pengelolaan kanopi kebun anggur untuk produksi anggur berkualitas memerlukan jumlah tandan yang terpantau sepanjang musim tanam. Penghitungan tandan secara manual membutuhkan banyak tenaga dan rentan kesalahan. Penulis mengusulkan model deteksi *Swin-T-YOLOv5* yang bekerja secara waktu nyata pada citra lapangan. Tujuannya membantu petani memangkas dan menjarangkan rumpun secara tepat waktu.

Data dikumpulkan dari dua varietas anggur, yaitu Chardonnay dan Merlot, pada periode 4 Juli hingga 30 September 2019. Kamera diarahkan tegak lurus ke kanopi dengan resolusi citra 5312 × 2988 piksel. Total terkumpul 459 citra mentah, terdiri atas 234 citra Chardonnay dan 225 citra Merlot. Kondisi pengambilan mencakup cuaca cerah dan berawan, dua tahap kematangan buah, serta tiga waktu cahaya, yaitu pagi, siang, dan sore. Seluruh citra diambil dari sisi kanopi yang sama. Citra tersebut dibagi menjadi data latih dan data uji.

Model menggabungkan *YOLOv5* dengan *backbone Swin Transformer*. Pada validasi, model mencapai presisi 98 persen, recall 95 persen, mAP 97 persen, dan F1-score 0,96. Pada cuaca berawan, mAP mencapai 97 persen dan F1-score 0,89. Pada cuaca cerah, mAP mencapai 95 persen dan F1-score 0,86. Untuk buah belum matang, mAP mencapai 90 persen dan F1-score 0,82. Untuk buah matang, mAP mencapai 96 persen dan F1-score 0,87. Nilai mAP model ini sekitar 44 persen lebih tinggi daripada Faster R-CNN, 18 persen lebih tinggi daripada YOLOv3, 14 persen lebih tinggi daripada YOLOv4, dan 4 persen lebih tinggi daripada YOLOv5. Pada penghitungan terhadap data lapangan, Swin-T-YOLOv5 mencapai R2 0,91 dan RMSE 2,4 buah pada Chardonnay. Pada Merlot, R2 mencapai 0,70 dan RMSE 3,3 untuk buah matang. Untuk buah belum matang, R2 turun menjadi 0,08 dan RMSE naik menjadi 9,0.

Penulis menyatakan bahwa performa pada Merlot kurang baik ketika mendeteksi buah belum matang. Penulis juga menyebut model ini diharapkan dapat dijalankan pada perangkat portabel seperti ponsel pintar. Langkah tersebut masih berupa rencana. Rencana berikutnya mencakup pengembangan antarmuka aplikasi seluler dan program *back-end*, serta penambahan kumpulan data citra kanopi anggur di repositori GitHub.
