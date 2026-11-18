# Improved Kiwifruit Detection Using Pre-Trained VGG16 with RGB and NIR Information Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2020improved` |
| Judul asli | Improved Kiwifruit Detection Using Pre-Trained VGG16 with RGB and NIR Information Fusion |
| Penulis | Liu, Zhihao; Wu, Jingzhu; Fu, Longsheng; Majeed, Yaqoob; Feng, Yali; Li, Rui; Cui, Yongjie |
| Tahun | 2020 |
| Venue | IEEE Access |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [liu2020improved.pdf](../pdf/liu2020improved.pdf)
- DOI resmi: https://doi.org/10.1109/access.2019.2962513

## Gambaran Umum

Penelitian ini bertujuan membangun sistem deteksi buah kiwi yang lebih
akurat, cepat, dan andal sebagai dasar estimasi hasil dan panen otomatis.
Panen kiwi masih bergantung pada pemetikan manual yang padat karya. Penulis
berpendapat bahwa satu modalisitas sensor, khususnya RGB, jarang cukup untuk
mendeteksi buah dalam kondisi lapang dengan pencahayaan yang berubah,
oklusi sebagian, dan tampilan buah yang beragam. Oleh karena itu, penelitian
ini menguji penggabungan citra RGB dan inframerah dekat (NIR) dari sensor
RGB-D menggunakan jaringan saraf konvolusional.

Datanya adalah buah kiwi kultivar Hayward di Stasiun Eksperimen Kiwi
Meixian, Universitas Northwest A&F, Shaanxi, China, yang diambil pada tiga
musim panen 2016, 2017, dan 2018. Kamera Kinect v2 yang dipasang pada tripod
portabel pada ketinggian 1,0 m memotret kanopi dari bawah, baik siang maupun
malam dengan pencahayaan buatan 30–50 lux. Dataset Hayward-Kiwi RGB-NIR-D
terdiri atas 1.000 kelompok citra multidandis sejajar berukuran 512 × 424
piksel, masing-masing memuat sekitar 30–50 buah, dengan total 39.678 buah
beranotasi kotak. Pembagiannya adalah 70% latih dan 30% uji. Citra NIR
dibalik secara horizontal dan disejajarkan ke RGB, lalu dinormalisasi ke
rentang 0–255; RGB dan NIR digabung menjadi citra enam kanal.

Mekanisme deteksi memakai Faster R-CNN dengan tulang punggung VGG16 yang
dilatih awal pada ImageNet lalu disesuaikan. Empat mode diuji, yaitu
RGB-Only, NIR-Only, Image-Fusion yang mengubah lapisan masukan dari tiga
menjadi enam kanal, serta Feature-Fusion yang menggabungkan peta fitur dari
dua jaringan VGG16. Pelatihan memakai SGD dengan momentum 0,9, weight decay
0,0005, laju pembelajaran 0,001 yang diturunkan menjadi 10% setiap 10.000
iterasi, pada kerangka Caffe. Metrik yang dipakai adalah presisi, recall,
average precision (AP) dari kurva presisi–recall, detection rate (DR) atau
perbandingan jumlah buah terdeteksi terhadap jumlah buah pada setiap
kategori, serta kecepatan deteksi. Buah dibagi menjadi empat kategori:
tertutup daun atau ranting, tumpang tindih, berdekatan, dan terpisah.
Nilai AP berturut-turut adalah 88,4% untuk RGB-Only, 89,2% untuk NIR-Only,
90,5% untuk Feature-Fusion, dan 90,7% untuk Image-Fusion; peningkatan yang
dilaporkan adalah 2,1% dan 2,3% dibanding modalisitas tunggal. Kecepatan
deteksi Image-Fusion, RGB-Only, dan NIR-Only hampir sama, yaitu 0.134,
0.134, dan 0.135 detik per citra, sedangkan Feature-Fusion memakan 0,188
detik per citra. Pada 50 citra uji lapang yang memuat 2.518 buah, DR total
Image-Fusion mencapai 91,7%, mengungguli Feature-Fusion (90,8%), NIR-Only
(89,0%), dan RGB-Only (88,1%). Buah berdekatan mendominasi 60,5% sampel;
DR untuk kategori ini naik dari 88,2% pada RGB-Only menjadi 92,8% pada
Image-Fusion.

Penulis mencatat sejumlah batasan. Citra kedalaman tidak dipakai dalam
deteksi karena buah yang tidak terekspos tidak terlihat pada citra tersebut;
pendekatan ini baru direncanakan untuk pekerjaan berikutnya bersama citra
spektral lain guna deteksi dan pelokalan sekaligus. Penyejajaran menyebabkan
hilangnya informasi pada bagian tepi citra RGB karena sudut pandang sensor
kedalaman lebih luas daripada kamera RGB, dan hal ini diduga menurunkan AP
RGB-Only. Pada mode NIR-Only, buah di tepi citra sulit terdeteksi karena
anotasi dipetakan dari RGB sehingga buah di tepi dipelajari sebagai latar,
selain itu posisi kotak deteksinya kurang tepat. Mode Feature-Fusion
memerlukan dua kali parameter, waktu komputasi, dan memori GPU; penulis
mengajukan dugaan bahwa pembelajaran fitur yang ganda, misalnya bentuk buah
dan kelopak, mengurangi fitur saat penggabungan. Buah tertutup dan tumpang
tindih tetap menjadi kategori tersulit. Penulis juga menyatakan hasil antar
penelitian sulit dibandingkan karena perbedaan dataset dan resolusi citra,
meski dataset yang digunakan kini dipublikasikan.


