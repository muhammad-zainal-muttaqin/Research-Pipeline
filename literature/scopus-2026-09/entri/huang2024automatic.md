# An automatic tracking method for fruit abscission of litchi using convolutional networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `huang2024automatic` |
| Judul asli | An automatic tracking method for fruit abscission of litchi using convolutional networks |
| Penulis | Huang, Tong; Guo, Jingfeng; Yu, Long; Chen, Houbin; Su, Zuanxian; Xue, Yueju |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [huang2024automatic.pdf](../pdf/huang2024automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109213

## Gambaran Umum

Makalah ini mengusulkan metode otomatis untuk memantau gugur buah (*fruit abscission*) leci pada cabang terpilih selama 56 hari. Metode terdiri atas tiga langkah: sistem kamera titik tetap yang memotret cabang sasaran setiap hari; algoritma pencocokan citra SE2-SuperGlue (SuperGlue dengan *backbone* CNN *steerable* ekuivarian E(2)) untuk mengekstrak wilayah minat cabang sasaran (*region of interest of the branch*, ROI-B) dari deret citra; dan detektor YOLOv8n untuk menghitung buah pada ROI-B tiap hari.

Lokasi pengambilan data adalah kebun leci di Pangkalan Pengajaran dan Penelitian Kampus Utama SCAU, Guangzhou, Tiongkok. Tiga kamera zoom Hikvision (2560 × 1440 piksel) dipasang pada ketinggian 6 m, memotret 80 cabang dari tiga varietas (Guiwei, Nuomici, Huaizhi) dari 27 April sampai 21 Juni 2022. Hasil utama: skor pencocokan SE2-SuperGlue 0,53 dengan kecepatan 177 ms per bingkai; mAP@0,5 YOLOv8n 98,7%; dan koefisien determinasi $R^2$ rerata antara hitungan prediksi dan acuan 0,98 pada deret 56 hari. Laju gugur buah relatif akhir adalah 94,7% (Guiwei), 92,8% (Huaizhi), dan 96,5% (Nuomici).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Gugur buah leci terjadi dalam beberapa puncak sebelum buah matang dan menyebabkan hasil panen rendah serta berbuah selang-seling. Praktik umum adalah menandai cabang perbungaan terpilih lalu menghitung buah secara manual setiap tujuh hari sejak minggu ketiga setelah pembungaan, yang menurut penulis menyita tenaga, tidak efisien, dan subjektif.

Penulis menyebut dua tantangan. Pertama, buah leci kecil dan berwarna hijau serupa latar, dan pengambilan citra dengan ponsel atau kamera genggam sulit mengendalikan sudut dan jarak untuk pemotretan jangka panjang. Kedua, lokasi cabang sasaran berubah akibat angin, hujan, dan pertumbuhan, sehingga bidang pandang kamera harus lebih luas daripada cabang dan ikut menangkap cabang tetangga yang buahnya mengganggu hitungan. SuperGlue disebut peka terhadap perubahan sudut cabang.

## Ide Utama

Alih-alih menghitung buah pada seluruh citra besar, penulis mengunci pandangan pada cabang sasaran dan mengekstrak ROI-B setiap hari dengan pencocokan citra, sehingga hitungan buah hanya berasal dari cabang yang sama sepanjang waktu. Identitas yang dipertahankan adalah identitas cabang, bukan identitas tiap buah. Kekokohan terhadap rotasi cabang diperoleh dengan mengganti *backbone* CNN pada SuperPoint dengan CNN *steerable* ekuivarian terhadap translasi dan rotasi.

## Cara Kerja Langkah demi Langkah

```
  Kamera titik tetap --> deret citra harian (56 hari)
  --> SE2-SuperGlue (pencocokan + RANSAC) --> ROI-B
  --> YOLOv8n --> hitungan buah per kelas --> laju gugur relatif
```

### 1. Akuisisi data

Tiga kamera zoom 23× dengan perlindungan IP66 dikendalikan oleh sistem akuisisi yang ditulis dengan Python 3.7, OpenCV, dan PyQt5, yang terhubung ke cloud Ezviz. Sistem merekam sudut dan panjang fokus pada titik prasetel (hingga 300 titik per kamera) dan menjadwalkan patroli harian. Titik prasetel dibuat pada 10 pohon Guiwei (40 titik), 5 pohon Nuomici (20 titik), dan 5 pohon Huaizhi (20 titik), menghasilkan deret citra 80 cabang selama 56 hari. Citra diambil antara pukul 08.00 dan 18.00 pada beragam cahaya, skala, dan cuaca. Jarak kamera ke cabang sekitar 1 m terdekat dan 30 m terjauh.

Set data pencocokan: 3.755 citra acak yang tidak terkait 80 cabang itu, disaring menjadi 3.380 citra dan dibagi 8:2 (2.704 latih, 676 uji). Set data deteksi: 750 citra leci hijau yang dianotasi dengan Labelimg dalam dua kelas (kelas 1: satu buah dari buah menyatu yang tumbuh; kelas 2: dua buah menyatu tumbuh), dengan rasio kelas sekitar 1:1,40. Setelah pembagian 8:2 dan augmentasi data latih, set latih berisi 2.400 citra (119.452 label) dan set uji 150 citra (7.635 label); total 2.550 citra dan 127.087 label (Tabel 1). Teks juga menyebut 37.516 label sebelum augmentasi.

### 2. SE2-SuperGlue

SuperPoint mendeteksi titik kunci dan deskriptor dengan *encoder* gaya VGG, yang diganti oleh CNN *steerable* E(2) beranggota empat lapisan konvolusi *steerable*. SuperGlue mencocokkan titik melalui GNN berbasis atensi (tujuh iterasi atensi diri dan silang) dan lapisan transportasi optimal dengan algoritma Sinkhorn dan kanal *dustbin*. Titik yang cocok dipakai RANSAC untuk menghitung matriks homografi, lalu ROI-B diperoleh dengan transformasi perspektif. Untuk mengatasi perubahan morfologi besar, citra hari ke-10, ke-28, dan ke-46 dipotong manual menjadi ROI-B acuan dan dicocokkan masing-masing dengan citra hari 1 sampai 19, 20 sampai 35, dan 36 sampai 56. Luas ROI-B sekitar 31,6% sampai 70,2% luas citra asli.

### 3. Deteksi dan penghitungan

YOLOv8n dilatih 300 epoch dengan ukuran masukan 640 × 640, optimizer Adam, laju belajar awal 0,01, *weight decay* 0,0005, dan *batch* 16. Jumlah buah kelas 1 dan kelas 2 dihitung per cabang per hari. Laju gugur relatif (Persamaan 6) adalah $(X_{i-1} - X_i)/X_{i-1} \times 100\%$ dengan $X$ jumlah buah semua cabang suatu varietas pada hari tersebut.

## Eksperimen dan Hasil

Perangkat: GPU "RTX TITAN", RAM 32 GB, Ubuntu 18.04. SE2-SuperGlue dilatih 10 epoch (sekitar 120 jam) dengan ukuran masukan 640 × 480. Skor pencocokan adalah proporsi titik cocok yang benar. Acuan hitung per hari berasal dari citra deret itu sendiri ("ground truth from the images"); makalah menyebut pembandingan pada lima cabang acak dari 80 cabang untuk 56 hari.

Pencocokan citra (Tabel 2, 676 citra uji, 1.024 fitur):

| Fitur lokal | Pencocok | Skor | Kecepatan (ms/bingkai) |
|---|---|---|---|
| ORB | KNN | 0,14 | 275 |
| SURF | KNN | 0,20 | 393 |
| SIFT | KNN | 0,28 | 480 |
| VGG + SuperPoint | SuperGlue | 0,46 | 103 |
| e2cnn + SuperPoint (usulan) | SuperGlue | 0,53 | 177 |

Deteksi buah (Tabel 3):

| Model | mAP@0,5 (%) | mAP@0,5:0,95 (%) | Ukuran (Mb) | Kecepatan (ms/bingkai) |
|---|---|---|---|---|
| YOLOv3-tiny | 86,7 | 54,5 | 17,42 | 100,64 |
| YOLOXs | 89,7 | 68,4 | 71,85 | 72,78 |
| Faster R-CNN | 91,0 | 71,8 | 165,76 | 21,58 |
| YOLOv5s | 98,3 | 80,5 | 16,81 | 114,37 |
| YOLOv8n | 98,7 | 84,0 | 6,20 | 176,25 |

Kolom kecepatan pada Tabel 3 tertulis "ms/f" sedangkan penjelasan metrik menyebut FPS; satuan sebenarnya tidak dapat dipastikan dari teks.

Statistik gugur: puncak gugur buah Guiwei pada hari ke-17 sampai 24 dan ke-38 sampai 45 setelah pembungaan; Huaizhi pada hari ke-18 sampai 25 dan ke-32 sampai 39; Nuomici pada hari ke-17 sampai 24 dan ke-45 sampai 52, serta puncak ketiga pada hari ke-59 sampai 66 sebelum panen. Laju gugur akhir 94,7% (Guiwei), 92,8% (Huaizhi), dan 96,5% (Nuomici).

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis: pemantauan otomatis jangka panjang tanpa penghitungan manual; ketahanan terhadap rotasi cabang dibandingkan SuperGlue biasa (Gambar 14, rotasi 20°, 30°, 45°); skor pencocokan lebih tinggi daripada ORB, SURF, SIFT, dan SuperGlue dengan *backbone* VGG; model detektor kecil (6,20 Mb).

Keterbatasan yang dinyatakan penulis: cabang lain kadang masuk ke ROI-B sehingga hitungan keliru (Gambar 20a); daun dikenali sebagai leci akibat bentuk serupa; buah yang bergerombol saling menutupi; daun dapat menutupi buah akibat perubahan morfologi (Gambar 20b). Karena itu rerata jumlah buah harian tidak menurun terus-menerus. Data dinyatakan bersifat rahasia.

Menurut pembacaan ringkasan ini, makalah tidak mencatat identitas buah individual: hitungan harian bisa naik akibat oklusi, dan pelacakan buah per buah tidak dilakukan. Menurut pembacaan ringkasan ini, acuan hitung per hari berasal dari penghitungan pada citra, bukan penghitungan lapangan, dan metode penyusunannya tidak dirinci. Menurut pembacaan ringkasan ini, $R^2$ 0,98 dihitung pada lima cabang acak, bukan pada seluruh 80 cabang.

## Kaitan dengan Tinjauan main6

Makalah ini tidak mencacah buah unik dengan mencocokkan identitas buah antarpandang. Yang dicocokkan adalah cabang yang sama dari hari ke hari dari titik pandang tetap, memakai fitur titik kunci, homografi, dan RANSAC, untuk membatasi hitungan pada satu cabang. Buah yang terlihat lebih dari sekali (pada hari berbeda) dihitung ulang setiap hari karena tujuannya adalah dinamika jumlah buah, bukan jumlah total buah unik. Cabang tetangga yang masuk bidang pandang diakui sebagai sumber galat.

Hitungan dilaporkan per kelas pada tahap deteksi (kelas 1 dan kelas 2 berdasarkan buah tunggal atau menyatu, bukan kematangan); hasil akhir disajikan sebagai jumlah buah per cabang dan laju gugur per varietas. Acuan hitungnya adalah penghitungan pada citra, bukan panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan membatasi wilayah hitung dengan pencocokan citra berbasis titik kunci dan homografi, serta pelaporan galat akibat masuknya objek tetangga ke wilayah hitung. Pencocokan seperti ini berlaku untuk bidang yang kira-kira datar dan bukan untuk sisi pohon dengan sudut pandang berbeda jauh.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `huang2024automatic`.

Ringkasan yang aman dikutip: Huang dkk. (2024) mengusulkan metode pemantauan gugur buah leci selama 56 hari pada 80 cabang dari tiga varietas, dengan kamera titik tetap, pencocokan citra SE2-SuperGlue untuk mengekstrak wilayah cabang sasaran (skor pencocokan 0,53; 177 ms per bingkai), dan YOLOv8n untuk menghitung buah (mAP@0,5 98,7%). Koefisien determinasi rerata antara hitungan dan acuan adalah 0,98, dan laju gugur akhir 94,7% (Guiwei), 92,8% (Huaizhi), dan 96,5% (Nuomici).

Catatan verifikasi data: Angka pencocokan ada pada Tabel 2 dan Bagian 3.3; angka deteksi pada Tabel 3 dan Bagian 3.4; pembagian data pada Tabel 1 dan Bagian 2.2; puncak gugur dan laju gugur akhir pada Bagian 3.5. Teks menyebut 37.516 label sekaligus 127.087 label dan menyatakan selisihnya akibat augmentasi tanpa merinci; keduanya dicatat sebagaimana tertulis. Teks menyebut "RTX TITAN" tanpa nomor model dan menulis "SDD" sebagai SSD pada pendahuluan. Kolom kecepatan Tabel 3 bernilai antara 21,58 dan 176,25 dengan satuan tidak jelas (tertulis ms/f). Kurva hitungan dan acuan (Gambar 16) tidak terbaca dari teks ekstraksi. Data dinyatakan rahasia, dan kode SE2-SuperGlue tersedia di repositori yang disebut pada Bagian 3.1.
