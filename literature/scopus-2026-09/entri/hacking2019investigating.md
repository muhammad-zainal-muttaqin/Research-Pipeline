# Investigating 2-D and 3-D proximal remote sensing techniques for vineyard yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hacking2019investigating` |
| Judul asli | Investigating 2-D and 3-D proximal remote sensing techniques for vineyard yield estimation |
| Penulis | Hacking, Chris; Poona, Nitesh; Manzan, Nicola; Poblete-Echeverr\'\ia, Carlos |
| Tahun | 2019 |
| Venue | Sensors Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [hacking2019investigating.pdf](../pdf/hacking2019investigating.pdf)
- DOI resmi: https://doi.org/10.3390/s19173652

## Gambaran Umum

Penelitian ini menyelidiki estimasi hasil panen kebun anggur dengan teknik
penginderaan jauh proksimal dua dimensi (RGB) dan tiga dimensi (RGB-D)
secara berdampingan. Estimasi hasil membantu pembuat anggur merencanakan
pengelolaan kebun dan logistik panen. Metode dua langkah tradisional, yang
menghitung jumlah tandan di awal musim lalu menimbang tandan pada vèraison,
bersifat padat karya, rawan galat, dan merusak. Penulis mencatat bahwa
penginderaan proksimal belum banyak berhasil dalam vitikultur dan belum ada
kajian yang membandingkan pendekatan 2-D dan 3-D secara langsung.

Datanya adalah anggur Shiraz pada sistem teralis vertical shoot positioned
(VSP) di Welgevallen Experimental Farm, Stellenbosch, Afrika Selatan, pada
musim tanam 2016/2017. Sejumlah 31 pohon dari tiga baris dipilih dan citra
diambil antara 28 Februari dan 3 Maret 2017. Dua perlakuan kanopi diuji,
yaitu kanopi penuh (FC) tanpa manipulasi dan penghilangan daun (LR) secara
manual di zona tandan. Tiga percobaan menghasilkan sepuluh kumpulan data:
percobaan satu berupa 21 tandan di laboratorium, percobaan dua berupa 21
tandan di lapang pada kedua perlakuan kanopi, dan percobaan tiga berupa 31
pohon di lapang pada kedua perlakuan. Sensor yang dipakai adalah kamera
Nikon D3200 24,2 megapiksel untuk RGB dan Kinect V1 untuk RGB-D, berupa
jala (mesh) pada tingkat tandan dan awan titik pada tingkat pohon.
Pengukuran acuan berupa massa (gram) dan volume perpindahan air (mL).

Mekanisme RGB terdiri atas kalibrasi piksel dengan penggaris menjadi luas
dalam cm², pemilihan wilayah minat secara manual, konversi ke ruang warna
HSV, segmentasi ambang warna, lalu penghitungan piksel tandan yang
dikonversi menjadi luas. Pada tingkat pohon, luas dua sisi kanopi dirata-
kan menjadi Total Bunch Area of Vine. Mekanisme RGB-D membersihkan jala di
CloudCompare, merekonstruksinya menjadi jala rapat air dengan Screened
Poisson Surface Reconstruction di MeshLab, lalu menghitung volume; pada
tingkat pohon, awan titik dibersihkan, tandan dipisahkan menurut warna, dan
volume dihitung dengan algoritma α-shape pada paket alphashape3d dengan nilai
alpha 0,010. Model estimasi hasil dibangun dengan validasi silang lima kali
lipat yang diulang sepuluh kali, lalu regresi linier antara hasil estimasi
dan massa sebenarnya menghasilkan r² dan RMSE. Hubungan acuan massa–volume
mencapai r² 0,971 pada tingkat tandan dan 0,996 pada tingkat pohon.

Hasilnya, segmentasi RGB mencapai F1 dan akurasi berturut-turut 0,976 dan
0,971 pada percobaan satu, 0,842 dan 0,781 pada percobaan dua, serta 0,833
dan 0,932 pada percobaan tiga. Untuk estimasi hasil dengan RGB, r² dan
RMSE adalah 0,889 dan 17,978 g di laboratorium; 0,625 dan 27,738 g pada FC
serta 0,742 dan 25,066 g pada LR di percobaan dua; dan 0,779 dan 559,357 g
pada FC serta 0,877 dan 443,235 g pada LR di percobaan tiga. Dengan RGB-D,
nilai terbaik diperoleh di laboratorium dengan r² 0,950 dan RMSE 12,458 g.
Pada percobaan dua, FC awalnya menghasilkan r² 0,020 karena satu pencilan;
setelah pencilan dibuang menjadi r² 0,609 dan RMSE 26,790 g, sedangkan LR
mencapai r² 0,756. Pada percobaan tiga, RGB-D menghasilkan r² 0,487 pada FC
dan 0,594 pada LR. Secara konsisten, perlakuan LR mengungguli FC, dan pada
tingkat pohon RGB mengungguli RGB-D.

Penulis menyatakan sejumlah batasan. Sensor Kinect V1 hanya cocok untuk
kondisi laboratorium karena iluminasi matahari menimbulkan gangguan
berlebih pada citra. Rekonstruksi Screened Poisson dapat melebih-lebihkan
bentuk tandan; satu pencilan memiliki volume Kinect 856 cm³ padahal volume
sebenarnya hanya 35 cm³. Estimasi RGB-D pada tingkat pohon dibatasi oleh
proses akuisisi atau segmentasi. Penentuan ambang warna masih manual dan
diduga menurunkan kinerja di lapang, demikian pula kebutuhan penggaris pada
setiap citra. Perbandingan tingkat pohon juga tercampur oleh perbedaan
waktu akuisisi, yaitu RGB pada siang hari dan RGB-D menjelang terbenam
matahari, serta oleh pergerakan Kinect yang digenggam tangan. Penghilangan
daun penuh tidak praktis secara komersial di sebagian wilayah karena
risiko sunburn, sehingga hasil FC lebih mencerminkan kesiapan operasional.
Penulis menganjurkan metode RGB yang lebih otomatis dan penggunaan Kinect
V2 dengan pencahayaan yang sesuai.
