# Real-time detecting and counting of citrus fruits in hilly and mountainous areas using UAV imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025real` |
| Judul asli | Real-time detecting and counting of citrus fruits in hilly and mountainous areas using UAV imagery |
| Penulis | Li, Chuanhong; Fu, Xinglan; Fu, Hanwen; Song, Jie; Li, Guanglin |
| Tahun | 2025 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [li2025real.pdf](../pdf/li2025real.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202503246

## Gambaran Umum

Kajian ini membahas penghitungan buah jeruk di kebun perbukitan dan pegunungan yang masih bergantung pada tenaga manusia. Penghitungan manual lambat dan berat, padahal hitungan buah yang akurat menjadi dasar estimasi hasil panen dan pengelolaan kebun yang cerdas. Penulis menilai penelitian terdahulu kurang tepat untuk kondisi ini. Sebagian besar metode deteksi buah memakai kamera darat atau perangkat genggam, sehingga sulit menjangkau area luas dengan medan yang berat. Penulis juga menyebut bahwa model *YOLO* yang ada masih kurang dalam hal ringan, kecepatan real-time, dan ketahanan terhadap lingkungan kompleks. Tujuan penelitian ini adalah membangun metode deteksi dan penghitungan buah jeruk real-time berbasis citra *unmanned aerial vehicle* (UAV) resolusi tinggi.

Data dikumpulkan pada Desember 2024 di dua lokasi, yaitu kebun jeruk *Wogan* di Kabupaten Beibei, Chongqing, dan kebun jeruk mekanis di Wusheng, Guang'an, Sichuan. Kedua lokasi beriklim subtropis lembap dengan curah hujan tahunan rata-rata 1.128,4 mm. Penulis memakai enam rotor UAV dengan kamera CMOS 1/1,7 inci, 8 megapiksel, dan resolusi 4K. Terbang dilakukan pada ketinggian 2,9 m, kecepatan 1,0 m/s, dan sudut pandang kamera 45 derajat, dengan tumpang tindih 80 persen. Citra latih dan validasi berjumlah 3.820 gambar dari area C1 dan S1, ditambah 30 segmen video. Diameter buah rata-rata 40 hingga 70 mm, dan setiap buah menempati sekitar 70 hingga 120 piksel. Pengujian penghitungan dilakukan pada area C2 dan S2. Pengujian real-time dilakukan pada area C3 dan S3 dengan video 1.080 piksel yang dikirim langsung dari drone ke komputer.

Model yang diusulkan, GCW-YOLOv8n, memodifikasi *YOLOv8n* dengan mengganti konvolusi standar menjadi *GhostConv* dan menambahkan modul *C3Ghost* untuk mengurangi beban komputasi. Model juga menambahkan *convolutional block attention module* (CBAM) di bagian neck, memakai fungsi kerugian *wise intersection over union* (WIoU), dan melacak buah dengan *DeepSORT*. Hasilnya, presisi mencapai 98,9 persen, *recall* 94,4 persen, dan *mean average precision* 98,5 persen. Ketiganya naik 4,2, 3,4, dan 3,7 poin persentase dibanding model asli. Waktu inferensi turun 75,7 persen. Pada uji video offline, rata-rata *counting accuracy* (CA) sebesar 95,57 persen. Pada uji langsung di lapangan, rata-rata CA sebesar 94,11 persen dengan 31,69 hingga 34,87 bingkai per detik. Pada Tabel 4, CA tertinggi 98,51 persen dicapai pada video dengan 67 buah, sedangkan CA terendah 92,49 persen tercatat pada video dengan 413 buah.

Penulis menyatakan beberapa batasan. Akurasi penghitungan menurun seiring bertambahnya kepadatan buah, karena buah yang saling menutupi membuat deteksi lebih sulit. Dalam kondisi itu, model dapat melewatkan atau salah mengenali buah, dan *DeepSORT* sangat bergantung pada kualitas deteksi sehingga rentan terhadap pertukaran ID dan putusnya lintasan. Parameter terbang disesuaikan dengan jarak antarbaris sekitar 4,3 m dan jarak antarpohon sekitar 3,0 m, sehingga penerapan pada kebun dengan tata tanam lain belum diuji. Data juga hanya berasal dari dua lokasi dan satu periode pengambilan, sehingga generalisasi ke kondisi lain perlu pengujian lanjutan.
