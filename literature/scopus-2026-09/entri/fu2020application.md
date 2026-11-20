# Application of consumer RGB-D cameras for fruit detection and localization in field: A critical review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fu2020application` |
| Judul asli | Application of consumer RGB-D cameras for fruit detection and localization in field: A critical review |
| Penulis | Fu, Longsheng; Gao, Fangfang; Wu, Jingzhu; Li, Rui; Karkee, Manoj; Zhang, Qin |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [fu2020application.pdf](../pdf/fu2020application.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2020.105687

## Gambaran Umum

Kajian ini adalah tinjauan tentang penggunaan sensor RGB-D untuk mendeteksi dan melokalisasi buah di kebun. Sensor RGB-D menghasilkan dua jenis citra sekaligus: citra warna (RGB) dan citra kedalaman (*depth*), yaitu jarak setiap piksel dari kamera. Penulis membandingkan hasil deteksi yang memakai citra RGB, citra kedalaman, citra inframerah, dan fusi dari beberapa sumber tersebut. Temuan utama: citra kedalaman saja memberi hasil yang lebih rendah daripada citra RGB pada beberapa studi, sedangkan fusi RGB dan depth menaikkan hasil. Pada satu studi yang dikutip, *average precision* (AP) naik dari 61,3% (depth saja) menjadi 90,7% (fusi).

Sensor RGB-D yang dibahas bekerja dengan prinsip berbeda. *Structured light* (SL) memproyeksikan pola cahaya ke adegan lalu menghitung jarak dari pergeseran pola. *Time of flight* (ToF) mengukur waktu tempuh pantulan cahaya. *Active infrared stereo* (AIRS) membandingkan dua pasang citra inframerah untuk menghitung disparitas. Bagian 2 kajian ini mendaftar kamera konsumen yang dipakai di lapangan, antara lain Kinect, Xtion PRO Live, dan RealSense. Kamera jenis ini murah, tetapi galatnya bergantung pada cahaya matahari dan jarak, sehingga kualitas depth di kebun terbuka tidak selalu stabil.

Pada hasil deteksi, kajian ini mencatat nilai yang dilaporkan oleh studi yang berbeda. Gené-Mola dkk. (2019) memakai citra depth dari Kinect v2 untuk mendeteksi apel dengan Faster RCNN berbasis VGG16, dan AP-nya hanya 61,3%. Tu dkk. (2018) melaporkan tingkat deteksi 76,3% dengan citra depth, dan Tu dkk. (2020) melaporkan F1 84,1% dengan citra depth. Untuk citra RGB, empat nilai yang dikutip berkisar dari 80,8% sampai 91,6%. Untuk perbandingan langsung, Sa dkk. (2016) pada paprika mendapat F1 0,816 dengan RGB dan 0,797 dengan inframerah. Liu dkk. (2020) melaporkan AP 89,2% dengan citra inframerah pada kiwi. Angka-angka ini berasal dari dataset, kondisi kebun, dan arsitektur yang berbeda, sehingga tidak dapat dirata-ratakan.

Batas kajian ini perlu dicatat. Kajian ini juga tidak membahas pencacahan lintas pandang, yaitu menghitung setiap buah sekali dari banyak foto. Dari sisi relevansi untuk sensus, temuan pentingnya adalah bahwa depth menolong deteksi ketika digabung dengan RGB, bukan ketika dipakai sendirian. Klaim bahwa depth menaikkan deteksi pada data sawit belum dapat ditarik dari kajian ini.
