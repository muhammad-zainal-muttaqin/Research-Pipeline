# Multiple object tracking in deep learning approaches: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `park2021multiple` |
| Judul asli | Multiple object tracking in deep learning approaches: A survey |
| Penulis | Park, Yesul; Dang, L. Minh; Lee, Sujin; Han, Dongil; Moon, Hyeonjoon |
| Tahun | 2021 |
| Venue | Electronics Switzerland |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [park2021multiple.pdf](../pdf/park2021multiple.pdf)
- DOI resmi: https://doi.org/10.3390/electronics10192406

## Gambaran Umum

Masalah utama adalah pelacakan multi-objek (*multiple object tracking*, MOT), yaitu memberi identitas unik pada setiap objek yang terdeteksi dan mengikuti lintasannya antarframe. Dua tantangan yang menjadi fokus tinjauan ini adalah oklusi dan peralihan identitas (*ID switch*). Oklusi terjadi ketika satu objek menutupi objek lain sebagian atau seluruhnya, sehingga informasi tampilan dari beberapa frame diperlukan untuk membedakan objek yang berada pada lokasi yang sama. Peralihan identitas terjadi ketika objek yang sama memperoleh identitas berbeda karena tidak masuk dalam *tracklet* yang diprediksi, misalnya ketika pelacak mengira objek itu hilang lalu memberi identitas baru. Tinjauan ini menyusun perkembangan MOT pada dekade terakhir dengan fokus pada pendekatan pembelajaran mendalam. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Metode tinjauan mengikuti pedoman *Preferred Reporting Items for Systematic Reviews and Meta-Analyses* (PRISMA). Pencarian dilakukan pada Google Scholar, Scopus, dan situs MOT Challenge untuk rentang tahun 2017–2021 dengan kata kunci "multiple object tracking" dan "multiple object tracking deep learning". Dari 150 catatan yang teridentifikasi, 50 dibuang karena tidak memakai teknik pembelajaran mendalam, tiga dibuang karena duplikat, sehingga 97 makalah dimasukkan ke dalam tinjauan. Makalah dikelompokkan ke dalam 12 kategori: pembelajaran tampilan, penanganan oklusi, deteksi dan prediksi, minimasi biaya komputasi, variasi gerak, variasi tampilan dan peralihan identitas, penanganan oklusi jarak jauh, deteksi dan asosiasi target, afinitas, asosiasi *tracklet*, pembelajaran deteksi otomatis, serta *transformer*. Secara terpisah, metode dikelompokkan lagi menjadi enam teknik utama: IoU, CNN, LSTM, mekanisme atensi, jaringan Siamese, dan filter Kalman.

Mekanisme asosiasi pada pendekatan yang ditinjau membandingkan fitur objek hasil deteksi dengan fitur objek yang sedang dilacak. CNN dipakai secara luas untuk mengekstrak fitur tampilan; IoU mengukur tumpang tindih kotak dan dipasangkan dengan algoritma Hungaria untuk menetapkan pasangan deteksi dengan biaya minimum. Jaringan Siamese membandingkan dua tampilan untuk menilai kemiripan, LSTM memodelkan informasi temporal, dan mekanisme atensi menyorot bagian fitur yang relevan. Filter Kalman meramalkan posisi berikutnya dan sering digabung dengan algoritma Hungaria, seperti pada SORT dan DeepSORT. Pendekatan *transformer* yang mulai muncul pada 2021 memakai kueri objek dan kueri lintasan untuk asosiasi, misalnya TransCenter, RelationTrack, dan MOTR. Beberapa metode menangani oklusi lewat identifikasi ulang, graf, dan pemodelan MDP, sedangkan yang lain memakai informasi 3D dari LiDAR atau radar.

Dataset yang ditinjau adalah KITTI serta versi MOT Challenge. KITTI memuat 21 sekuens latih dan 29 sekuens uji dengan data citra stereo, awan titik Velodyne, GPS/IMU, dan kalibrasi; tugas pelacakannya berfokus pada kelas mobil dan pejalan kaki. MOT15 memiliki 11 sekuens latih dengan 5.500 frame, 500 lintasan, 39.905 kotak, dan kepadatan 7,3, serta 11 sekuens uji dengan 5.783 frame, 721 lintasan, 61.440 kotak, dan kepadatan 10,6. MOT16 memiliki tujuh sekuens latih dengan 5.316 frame dan 110.407 kotak serta tujuh sekuens uji dengan 5.919 frame dan 182.326 kotak. MOT17 memakai video yang sama dengan MOT16 tetapi penyusunan data dan kebenaran tanahnya diperbaiki; himpunan latihnya mencakup 21 sekuens dan 336.891 kotak. Akurasi pelacakan diukur dengan MOTA, yang menggabungkan galat negatif palsu, positif palsu, dan ketidaksesuaian identitas dibagi jumlah objek kebenaran tanah, serta MOTP, yang merupakan rata-rata jarak antara objek dan hipotesisnya atas jumlah pencocokan.

Hasil yang dilaporkan menunjukkan pada KITTI, RRC-IIITH mencapai MOTP 85,73 dan ML 2,77, sedangkan PC3T mencapai MOTA 88,8, MT 80, dan kecepatan 222 frame per detik. Pada MOT15, FairMOT mencapai MOTA 59, IDF1 62,2, MT 45,6, dan ML 11,5, sementara SORT mencatat kecepatan 260 Hz. Pada MOT16 dan MOT17, RelationTrack mencapai MOTA 75,6 dan MOTP 80,9; pada MOT17 model ini juga mencapai IDF1 75,8, MT 43,1, dan FN 34.214. Analisis tren 2019–2021 menunjukkan afinitas meningkat dari 6% menjadi 22% dari jumlah makalah, deteksi dan prediksi mencapai 32% pada 2020, dan *transformer* mencapai 17% pada 2021. Batasan penulis tidak dinyatakan dalam bagian tersendiri; penulis hanya menyatakan bahwa oklusi dan peralihan identitas masih menjadi tantangan terbuka, dan bahwa detektor yang menghasilkan positif atau negatif palsu dapat menurunkan kualitas lintasan secara besar melalui banyak peralihan identitas dan fragmentasi.
