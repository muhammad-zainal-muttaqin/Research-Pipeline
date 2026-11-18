# Grape Maturity Detection and Visual Pre-Positioning Based on Improved YOLOv4

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qiu2022grape` |
| Judul asli | Grape Maturity Detection and Visual Pre-Positioning Based on Improved YOLOv4 |
| Penulis | Qiu, Chang; Tian, Guangzhao; Zhao, Jiawei; Liu, Qin; Xie, Shangjie; Zheng, Kui |
| Tahun | 2022 |
| Venue | Electronics Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [qiu2022grape.pdf](../pdf/qiu2022grape.pdf)
- DOI resmi: https://doi.org/10.3390/electronics11172677

## Gambaran Umum

Penelitian ini bertujuan memandu robot pemanen anggur agar mengenali dan mengklasifikasikan buah dengan tingkat kematangan berbeda secara cepat dan tepat di lingkungan kebun yang kompleks, sekaligus memperoleh informasi posisi ruang tandan anggur. Persoalan utamanya adalah rintangan daun dan ranting yang menutupi buah, tumpang tindih antartandan, serta tangkai yang tertutup sehingga sulit ditentukan langsung titik pemetikannya. Pendekatan yang ada, seperti metode tusuk untuk mengukur kekerasan, pencitraan hiperspektral near-infrared, jaringan saraf buatan, dan pengelompokan C-means, umumnya merusak buah, hanya bekerja pada buah yang sudah dipetik, atau terbatas pada kondisi pencahayaan dan tingkat kematangan tertentu. Penulis mengusulkan dua bagian: deteksi kematangan dengan YOLOv4 yang dimodifikasi, dan praposisi tandan memakai penglihatan stereo binokular.

Data dikumpulkan di kebun anggur di Kabupaten Lianjiang, Fuzhou, dengan kultivar Kyoho yang berubah warna dari hijau keungu muda, lalu ungu, dan akhirnya ungu kehitaman saat matang. Citra diambil dengan iPhone 11 beresolusi 4032×3024 piksel secara acak dari berbagai arah, sudut, jarak, kondisi cahaya, dan tingkat naungan, menghasilkan 1.000 citra asli. Kematangan dibagi menjadi empat kelas: hijau penuh (young_grape), sebagian kecil biji berubah ungu (near_young_grape), sebagian besar biji berubah ungu (near_mature_grape), dan ungu penuh (nature_grape). Sebanyak 200 citra tambahan diunduh dari internet untuk menyeimbangkan jumlah sampel antarkelas. Data diberi label dengan format PASCAL VOC memakai LabelImg 1.8.6, lalu diperbanyak dengan pembalikan cermin, penambahan derau, dan translasi menjadi 2.000 citra yang memuat 7.390 tandan, dibagi menjadi 6.651 citra latih dan 739 citra validasi dengan perbandingan 9:1. Pengujian praposisi memakai kamera binokular ZED2i dengan panjang fokus 1,8 mm, baseline 120 mm, dan resolusi 2560×720 piksel, dikalibrasi memakai SDK kamera; jarak kamera ke tandan berkisar 0–2 m.

Mekanisme deteksi memakai algoritma SM-YOLOv4, yaitu YOLOv4 yang mengganti jaringan ekstraksi fitur utama CSPDarknet53 dengan Mobilenetv3 pada tiga lapisan fitur berukuran sama, mengganti konvolusi biasa dengan konvolusi terpisah kedalaman pada jaringan penguat, dan menambahkan mekanisme perhatian kanal SENet sebelum fusi fitur; fungsi aktivasi h-swish menggantikan swish untuk mengurangi jumlah parameter dan mempercepat deteksi. Pelatihan berjalan 2.000 iterasi dengan ukuran kumpulan 8, laju pembelajaran awal 0,001, momentum 0,95, dan penurunan laju pembelajaran seperempuluh setiap 50 iterasi, pada Intel Core i5 12400F dengan GPU NVIDIA GeForce GTX 1080 Ti 11 GB. Untuk praposisi, kedua citra kiri dan kanan dideteksi, lalu kotak target dicocokkan bila kelasnya sama dan selisih luas piksel serta selisih ordinat sentroid masing-masing di bawah ambang 0,02 dan 0,01. Disparitas dihitung dari selisih koordinat horizontal sentroid, lalu kedalaman diperoleh dari Z = fx·b/(UL−UR), dengan koordinat X dan Y dihitung dari kedalaman dan parameter intrinsik. Jarak ke tandan dihitung sebagai akar kuadrat jumlah kuadrat komponen X dan Z.

Hasil deteksi menunjukkan SM-YOLOv4 mencapai mAP 93,52% pada ambang IoU 0,5 dengan kecepatan 92,38 frame per detik atau waktu deteksi rata-rata 10,82 ms. Nilai AP per kelas berturut-turut adalah 90,62%, 93,95%, 94,29%, dan 95,24%. Uji ablasi memberi mAP 89,59% untuk YOLOv4 awal, 92,63% untuk SE-YOLOv4, dan 91,94% untuk Mobilenetv3-YOLOv4. Dalam perbandingan model, SM-YOLOv4 mengungguli YOLOv5 (92,79%), YOLOv4-Tiny (82,46%), dan Faster R-CNN (93,11%) masing-masing sebesar 0,93, 11,06, dan 0,41 poin persentase. Pada uji praposisi dengan 37 tandan dari 10 lokasi, SM-YOLOv4 tidak menghasilkan deteksi palsu maupun terlewat, sedangkan YOLOv5 melewatkan tiga tandan dan Faster R-CNN menghasilkan satu deteksi palsu. Galat rata-rata praposisi SM-YOLOv4 adalah 0,027 m dengan rasio galat 3,89%, lebih rendah daripada YOLOv5 (0,067 m; 9,24%) dan Faster R-CNN (0,053 m; 7,38%); abstrak menyebut galat maksimum 32 mm dan galat rata-rata 27 mm.

Penulis mencatat beberapa batasan. Akurasi semua model turun ketika pencahayaan berupa cahaya belakang dan tandan bertumpang tindih parah, karena tekstur permukaan anggur menjadi tidak jelas dan tandan sulit dibedakan. Kelas hijau penuh memiliki AP terendah pada semua model karena warnanya paling mirip daun di sekitarnya, sehingga model dapat salah membedakan buah dari daun; penulis menyatakan hal ini tidak mengganggu pemanenan buah matang. YOLOv4-Tiny tercepat tetapi paling tidak akurat dan rawan terlewat, sedangkan Faster R-CNN akurat tetapi rawan deteksi palsu dan paling lambat. Pernyataan ketersediaan data dalam naskah menyatakan tidak berlaku, sehingga himpunan citra tidak dipublikasikan.

