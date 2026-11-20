# Accurate counting of small and dense Chinese cherry in natural orchard via fruit-oriented perception and sharpening network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `weng2026accurate` |
| Judul asli | Accurate counting of small and dense Chinese cherry in natural orchard via fruit-oriented perception and sharpening network |
| Penulis | Weng, Shizhuang; Deng, Rui; Xu, Jian; Wu, Qi; Sun, Shenao; Chen, Yudi; Yang, Huiwen; Zhu, Nina; Chen, Jialing; Zheng, Ling; Zhu, Zede |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | cherry |

## Tautan Akses
- PDF: [weng2026accurate.pdf](../pdf/weng2026accurate.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111909

## Gambaran Umum

Penghitungan buah yang akurat diperlukan untuk memperkirakan hasil panen dan mengatur pengelolaan kebun. Ceri Tiongkok (*Prunus pseudocerasus*) tumbuh dalam jumlah buah yang kecil dan rapat, sehingga penghitungannya sulit. Latar belakang yang rumit, variasi bentuk buah, dan buah yang saling menempel menurunkan akurasi metode yang ada. Penulis mengusulkan *Fruit-Oriented Perception and Sharpening Network* (FOPSN) untuk mengatasi masalah tersebut. Jaringan ini bertujuan menghitung ceri dari satu citra kebun secara andal.

Data dikumpulkan di dua kebun di Provinsi Anhui. Pada April 2024, sebanyak 369 citra kultivar ‘Jiahong’ dan ‘Rainier’ diambil di Kebun Ceri Yueshan, Guangde. Pada Maret 2025, sebanyak 130 citra kultivar ‘Mingzhu’ diambil di Kebun Ceri Wannian, Hefei. Kamera Nikon Z30 dipasang pada tinggi 1,6 hingga 1,7 meter dengan sudut elevasi 30 hingga 45 derajat. Lensa tetap 24 mm dan pencahayaan alami dipakai. Total 499 citra beresolusi 4176 × 2344 piksel terkumpul. Data kemudian ditambah dengan pengaburan Gaussian, peningkatan kecerahan, dan efek kabut, sehingga jumlahnya menjadi 2.006 citra. Pembagian data 75 % untuk latih dan 25 % untuk uji dengan seed 42. Setiap buah diberi kotak pembatas dan titik pusat, yang dipakai untuk *bounding box* dan peta kepadatan.

FOPSN terdiri atas tiga modul. *Progressive Spatial Aggregation Encoder* (PSAE) memusatkan area buah dan menekan latar belakang. *Adaptive Similarity Module* (ASM) menyesuaikan diri dengan variasi morfologi buah. *Interleaved Channel Reconstruction Decoder* (ICRD) memisahkan buah yang saling menempel dengan menyusun ulang kanal. Pada pengujian, FOPSN mencapai MAE 2,097 dan RMSE 2,838. Nilai ini lebih rendah daripada metode deteksi terbaik, yaitu YOLOv12 dengan MAE 2,856. Dibandingkan LOCA, metode peta kepadatan terbaik kedua, FOPSN menurunkan MAE sebesar 8,9 % dan RMSE sebesar 8,8 %. Empat metode peta kepadatan lain memiliki MAE 2,301 hingga 3,082. Kecepatan FOPSN mencapai 73 fps. Studi ablasi juga menunjukkan bahwa konfigurasi lengkap memberikan hasil paling akurat. Satu konfigurasi parsial tanpa beberapa modul menghasilkan MAE 2,756.

Penulis menyatakan beberapa batasan. Citra dengan sudut tetap tidak menangkap buah yang tertutup berat. Akibatnya, model kurang menghitung pada area dengan oklusi tinggi. Penghitungan pada video alam belum dikaji. Efisiensi dan jumlah parameter model juga masih perlu dioptimalkan untuk penerapan di lapangan. Penulis merencanakan akuisisi multi-sudut untuk mengembalikan informasi buah yang tertutup, pelacakan *optical flow* untuk mengurangi penghitungan ganda pada video, serta model ringan melalui dekomposisi konvolusi dan *knowledge distillation*.
