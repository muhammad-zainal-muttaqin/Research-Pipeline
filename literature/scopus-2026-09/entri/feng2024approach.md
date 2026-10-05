# Approach of Dynamic Tracking and Counting for Obscured Citrus in Smart Orchard Based on Machine Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `feng2024approach` |
| Judul asli | Approach of Dynamic Tracking and Counting for Obscured Citrus in Smart Orchard Based on Machine Vision |
| Penulis | Feng, Yuliang; Ma, Wei; Tan, Yu; Yan, Hao; Qian, Jianping; Tian, Zhiwei; Gao, Ang |
| Tahun | 2024 |
| Venue | Applied Sciences Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [feng2024approach.pdf](../pdf/feng2024approach.pdf)
- DOI resmi: https://doi.org/10.3390/app14031136

## Gambaran Umum
Makalah ini mengusulkan metode pendeteksian, pelacakan, dan pencacahan dinamis buah jeruk (*citrus*) yang tertutup daun dan ranting pada video kebun. Metode terdiri atas detektor YOLOv7-tiny, pelacak berbasis DeepSORT (filter Kalman dan algoritme Hungarian), penyaring masa hidup dua tahap (*two stages life filter*, TTSLF) untuk lintasan baru, dan strategi pencacahan garis (*drawing lines counting strategy*). Data berasal dari kebun jeruk di Sichuan (varietas Kasumi) yang dilengkapi citra dari tiga lokasi lain di Tiongkok.

Dataset akhir berjumlah 15.000 citra setelah augmentasi dan penambahan data publik MOT16. Detektor mencapai presisi 96,81%, *recall* 96,39%, dan *average detection precision* (ADP) 97,23%. Akurasi deteksi video (VDA) pada kondisi normal adalah 95,12%. Penambahan TTSLF menaikkan *multiple object tracking accuracy* (MOTA) dari 45,36% menjadi 67,14% dan *multiple object tracking precision* (MOTP) dari 56,77% menjadi 74,65%, serta menurunkan laju pergantian identitas (*ID switch rate*, IDSR) dari 25,97% menjadi 15,63%.

Pada 10 video jeruk, akurasi pencacahan rata-rata (*average counting precision*, ACP) terhadap hitung manual adalah 81,02%, dengan $R^2$ 0,9982 dan RMSE 32,300 pada regresi linear antara hitungan algoritme dan hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Informasi hasil panen jeruk merupakan indikator penting bagi manajemen kebun. Pada kebun berpola tanam rapat dengan pemangkasan intensif dan pembungkusan buah (*bagging*), jumlah buah masih diperkirakan dengan pencuplikan dan hitung manual yang memakan waktu dan tenaga. Penulis menyatakan bahwa penelitian pencacahan otomatis sebelumnya terutama berfokus pada model statis, yaitu pencacahan pada citra tunggal, yang menurut mereka tidak sesuai dengan lingkungan produksi nyata.

Pohon jeruk di wilayah Sichuan dan Chongqing selalu hijau, bercabang banyak, dan berdaun lebat, sehingga buah sering tertutup ranting dan daun saat video diambil. Penutupan itu menyebabkan lintasan buah hilang atau identitas (ID) buah yang sama berpindah, yang berakibat penghitungan ganda atau buah terlewat. Penulis menilai DeepSORT, yang memadukan gerak dan tampilan, relevan untuk kondisi ini, tetapi masih memerlukan penanganan lintasan baru yang tidak stabil.

## Ide Utama
Gagasan utamanya adalah menekan kesalahan identitas akibat penutupan dengan dua cara. Pertama, lintasan baru tidak langsung diterima, tetapi harus lolos penyaring masa hidup dua tahap dengan deteksi tiga bingkai berturut-turut. Lintasan yang lolos masuk ke tahap pencocokan, sedangkan yang gagal dihapus. Kedua, pencocokan prediksi Kalman dengan deteksi memakai jarak Euclid dan tumpang tindih (*intersection over union*, IoU), lalu hitungan akhir diperoleh dengan strategi garis hitung yang menggabungkan ID setiap buah.

Identitas buah antarbingkai dalam satu video dijaga oleh pelacak. Makalah tidak membahas penyatuan identitas antarvideo atau antarsisi pohon.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Lokasi utama adalah kebun di Kabupaten Pujiang, Kota Chengdu, Provinsi Sichuan, dengan jeruk Kasumi. Kamera Sony IMX596 menghasilkan 2.000 citra. Data tambahan berupa 200 citra dari Jiangxi, 300 dari Guangxi, dan 500 dari Guangdong sehingga total 3.000 citra dari kebun dan varietas berbeda. Video jeruk direkam pada 30 bingkai per detik. Jumlah video total tidak dilaporkan; pengujian pencacahan memakai 10 video berisi 300 sampai 548 bingkai.

### 2. Praproses dan pembagian data
Karena pengambilan data umumnya pada cuaca redup dan variasi varietas terbatas, 3.000 citra diaugmentasi dengan peningkatan saturasi 5 kali, penambahan dan pengurangan kecerahan 70 piksel, dan pembalikan vertikal. Dataset diperluas dengan dataset publik MOT16 menjadi 15.000 citra, lalu dibagi latih, validasi, dan uji dengan rasio 7:2:1.

### 3. Deteksi dengan YOLOv7-tiny
YOLOv7-tiny dipilih karena lapisan dan kanalnya lebih sedikit daripada YOLOv7 dan YOLOX, sehingga cepat dan cocok untuk perangkat dengan sumber daya terbatas. Citra masukan diubah ke 416 x 416. Hiperparameter terbaik menurut pencarian grid: laju belajar awal 0,001, peluruhan bobot 0,0005, momentum 0,9, dan jumlah iterasi 50.000. Pelatihan memakai laptop dengan CPU Intel Core i9-13900HX, RAM 16 GB, dan GPU NVIDIA RTX 4060 Laptop.

### 4. Prediksi gerak dengan filter Kalman
Karena posisi buah antarbingkai berubah sangat kecil pada 30 bingkai per detik, gerak dianggap beraturan dan sistem dianggap linear. Filter Kalman memprediksi posisi lintasan buah pada bingkai berikutnya beserta matriks kovariansnya, lalu memperbarui estimasi dengan observasi bingkai saat ini.

### 5. Pencocokan dengan algoritme Hungarian
Algoritme Hungarian menyelesaikan penugasan optimum antara hasil prediksi dan hasil deteksi. Kemiripan diukur dengan jarak Euclid, lalu pencocokan bertingkat (*cascade*) dan pencocokan IoU diterapkan. Lintasan yang gagal dicocokkan diinisialisasi sebagai lintasan baru.

### 6. Penyaring masa hidup dua tahap
Lintasan baru harus terdeteksi pada tiga bingkai berturut-turut sebelum memasuki pencocokan. Bila gagal, lintasan dihapus. Tujuannya mengurangi buah yang hilang dan kesalahan pencocokan berulang akibat lintasan baru yang palsu.

### 7. Strategi pencacahan garis
Hitungan diperoleh dengan menggabungkan ID setiap buah dengan garis hitung pada bingkai video (Gambar 4 makalah). Detail geometri garis, seperti posisi dan arah, tidak diuraikan pada teks yang tersedia.

## Eksperimen dan Hasil
Detektor dibandingkan dengan YOLOv5, YOLOv5-tiny, dan YOLOX pada dataset jeruk (Tabel 1). Untuk pelacakan, algoritme sebelum dan sesudah penambahan TTSLF dibandingkan pada 10 video (Tabel 3). Acuan pencacahan adalah hitung manual: peneliti memutar video bingkai demi bingkai, mencatat jumlah buah pada bingkai pertama, lalu mencatat buah baru pada bingkai berikutnya, dan hasil beberapa peneliti dirata-ratakan.

| Metode | Presisi | *Recall* | ADP |
|---|---|---|---|
| YOLOv5 | 96,62% | 95,22% | 94,17% |
| YOLOv5-tiny | 95,19% | 94,00% | 94,04% |
| YOLOX | 94,84% | 93,24% | 89,02% |
| YOLOv7-tiny | 96,81% | 96,39% | 97,23% |

| Metrik pelacakan (kondisi normal) | Sebelum | Sesudah |
|---|---|---|
| VDA | 95,12% | 95,12% |
| IDSR | 25,97% | 15,63% |
| MOTA | 45,36% | 67,14% |
| MOTP | 56,77% | 74,65% |

Selisih MOTA 21,78 poin persentase dan MOTP 17,88 poin persentase dinyatakan dalam teks. Untuk buah tertutup, Tabel 3 menyebut algoritme lama turun 5% (MOTA) dan 7% (MOTP), sedangkan algoritme baru "tidak terpengaruh"; nilai absolutnya tidak dilaporkan. Waktu deteksi satu citra adalah 0,011 detik.

Pada pencacahan, regresi hitungan algoritme terhadap hitungan manual berbentuk $y = 1{,}0742x + 0{,}8083$ dengan $R^2$ 0,9982 dan RMSE 32,300. ACP rata-rata adalah 81,02% (sekitar 80% per video). Penulis menyatakan bahwa akurasi tidak berubah nyata menurut jumlah jeruk per video. Uji khi-kuadrat menghasilkan nilai-p 0,0133 pada tingkat signifikansi 0,01, sehingga hipotesis nol tidak ditolak dan penulis menyimpulkan tidak ada perbedaan nyata antara hitungan algoritme dan hitungan manual. Hitungan per video tidak tersedia dalam teks (hanya pada Gambar 5).

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: detektor ringan dan cepat sehingga mudah dipasang pada perangkat tertanam, penyaring dua tahap menurunkan IDSR dan menaikkan MOTA serta MOTP, dan hitungan algoritme berkorelasi kuat dengan hitung manual. Pengujian memakai data dari beberapa lokasi dan varietas.

Keterbatasan yang dinyatakan penulis: data tidak tersedia untuk umum karena alasan privasi (hanya atas permintaan). Penulis juga mengakui bahwa pohon jeruk berdaun lebat menyebabkan ID melompat, yang menjadi sebab utama galat pelacakan, dan blur gerak kamera dapat menggagalkan pencocokan.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, ACP 81,02% berarti rata-rata galat relatif sekitar 19% terhadap hitung manual, padahal $R^2$ tinggi; kemiringan 1,0742 menunjukkan hitungan algoritme cenderung lebih tinggi daripada hitungan manual. Kedua, hitung manual berasal dari video yang sama sehingga buah yang tidak terlihat pada video tidak terhitung dalam acuan. Ketiga, MOTA 67,14% masih rendah. Keempat, kesimpulan uji khi-kuadrat dibaca dari nilai-p 0,0133 yang lebih besar dari 0,01, tetapi hanya dengan 10 video dan tanpa rincian uji. Kelima, pelacakan hanya dalam satu video; tidak ada penyatuan antar-video atau antar-sisi pohon, dan tidak ada hitungan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dalam satu video dengan mekanisme pelacakan berbasis deteksi (*tracking-by-detection*): prediksi gerak Kalman, pencocokan Hungarian berdasarkan jarak dan IoU, penyaring masa hidup untuk lintasan baru, dan penghitungan ID unik melalui garis hitung. Buah hanya dihitung sebagai satu kelas jeruk; hitungan per kelas tidak dilaporkan. Acuan hitungnya adalah hitung manual pada video (bukan panen dan bukan anotasi citra tunggal).

Untuk pencacahan tandan sawit multi-sisi, gagasan penyaring lintasan baru (konfirmasi pada beberapa bingkai berturut-turut sebelum ID diterima) dapat dipindahkan sebagai cara menekan ID palsu. Namun, mekanisme ini bergantung pada kontinuitas gerak antarbingkai pada 30 bingkai per detik; pada pengambilan foto dari sisi pohon yang berbeda, asumsi gerak seragam tidak berlaku, sehingga pencocokan lintas sisi memerlukan mekanisme lain.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `feng2024approach`.

Feng dkk. (2024) mengusulkan metode pencacahan jeruk dinamis pada video kebun yang menggabungkan YOLOv7-tiny, DeepSORT dengan filter Kalman dan algoritme Hungarian, penyaring masa hidup dua tahap untuk lintasan baru, dan strategi pencacahan garis. Penyaring itu menaikkan MOTA dari 45,36% menjadi 67,14% dan menurunkan IDSR dari 25,97% menjadi 15,63%. Akurasi pencacahan rata-rata terhadap hitung manual pada 10 video adalah 81,02%.

Catatan verifikasi data: Angka detektor ada pada Tabel 1 (teks hasil, Seksi 3.3.1) dan angka pelacakan pada Tabel 3 (Seksi 3.3.2). ACP 81,02%, $R^2$ 0,9982, RMSE 32,300, dan persamaan regresi ada pada Seksi 3.3.3; nilai-p 0,0133 pada akhir Seksi 3.3.3. Tabel 1 pada teks bertajuk "bagged grape dataset" padahal membahas jeruk, yang tampaknya salah ketik penulis. Kesimpulan menulis MOTP 74,15%, sedangkan Abstrak dan Tabel 3 menulis 74,65%; ringkasan ini memakai 74,65%. Teks juga menyebut ADP 97,23% dan VDA 95,12% sebagai "akurasi deteksi". Hitungan per video hanya ada pada Gambar 5 yang tidak terbaca dari teks. Jumlah video total, resolusi video, detail garis hitung, dan hasil per kondisi (Tabel 2) tidak dilaporkan secara kuantitatif.
