# In-field apple size and location tracking using machine vision to assist fruit thinning and harvest decision-making

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirbod2021field` |
| Judul asli | In-field apple size and location tracking using machine vision to assist fruit thinning and harvest decision-making |
| Penulis | Mirbod, Omeed; Choi, Daeun; Heinemann, Paul H; He, Long; Schupp, James R |
| Tahun | 2021 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting Asabe 2021 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [mirbod2021field.pdf](../pdf/mirbod2021field.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202100831

## Gambaran Umum

Mirbod dkk. (2021) membuat sistem stereo untuk mengukur diameter buah apel di pohon dan melacak pertumbuhannya sepanjang musim. Pengukuran manual dengan tanda pada sampel buah dan kaliper atau cincin ukur memakan banyak tenaga dan waktu. Untuk penjarangan kimia dan penentuan waktu panen, pengukuran per buah perlu dilakukan berulang di tempat yang sama. Penulis menetapkan tiga tujuan: mendaftarkan lokasi 3D setiap buah ke pohonnya, mencocokkan buah antarbulan selama musim tanam, dan membuat kurva pertumbuhan untuk tiap buah yang dilacak.

Data dikumpulkan pada 2020 di Russell E. Larson Agricultural Research Center, Pennsylvania Furnace, Amerika Serikat, pada kebun apel varietas Golden Delicious. Sensor berupa dua kamera FLIR Blackfly S (BFS-U3-88S6C-C) yang disusun sebagai pasangan stereo, dengan lampu LED untuk pencahayaan yang lebih merata. Peralatan dipasang di gerobak empat roda dan ditarik melewati satu baris kebun dengan kecepatan sekitar 0,5 m/s, menangkap citra 3 Hz. Satu baris berisi 50 pohon. Sebanyak 20 pohon dipakai untuk melatih model deteksi, dan 30 pohon sisanya untuk uji. Citra diambil pada lima periode, yaitu 13 Juni (dua percobaan), 17 Juli, 13 Agustus, 20 September, dan 7 Oktober. Jumlah citra untuk pelacakan berkisar 139 sampai 178 per periode. Diameter acuan diukur dari sampel buah tiap pohon dengan alat band-loop. Rata-rata diameter acuan naik dari 25 mm pada Juni menjadi 76 mm pada Oktober.

Metode terdiri dari tiga tahap. Faster R-CNN mendeteksi buah pada citra yang diperkecil, lalu Mask R-CNN menyegmentasi tiap buah dari potongan citra beresolusi penuh. Diameter dihitung dari kedalaman stereo. Pencocokan buah antarbulan memakai deskriptor SIFT, pencocokan Brute Force dari OpenCV, dan estimasi pose kamera dengan SolvePnP serta RANSAC. Hasil pada Tabel 2 menunjukkan 264 buah cocok pada Juni (73% dari buah terdeteksi), 174 buah pada Juli ke Agustus (55%), 304 buah pada Agustus ke September (71%), dan 329 buah pada September ke Oktober (74%). Terhadap jumlah panen, persentase cocoknya 62%, 40%, 71%, dan 76%. Pada uji tanaman, buah dengan diameter rata-rata 25 mm mencapai akurasi pencocokan 73%. Pada Juli, diameter buah terlalu besar karena kalibrasi kamera yang buruk, dan kesalahan itu diperbaiki pada data Agustus. Dari 18 buah yang dilacak empat bulan, Juli hanya memuat 9 buah.

Penulis mencatat beberapa batasan. Metode belum diuji pada buah berdiameter di bawah 25 mm. Dua percobaan Juni dilakukan pada hari yang sama, padahal pengukuran penjarangan dianjurkan dilakukan tiga dan delapan hari setelah semprot. Juni ke Juli tidak dicoba karena tekstur buah berubah dan buah turun dari dahan. Pencocokan Juli ke Agustus paling rendah karena adanya pemangkasan dan tekstur buah yang masih berubah. Pose kamera tidak dapat diestimasi untuk empat pohon pada Juli karena tertutup tajuk yang lebat. Metode juga bergantung pada urutan bingkai yang memiliki buah terlihat. Bila tidak ada buah terlihat atau pohon di baris hilang, citra satu bulan tidak dapat dicocokkan dengan bulan berikutnya. Penulis menyebut fitur yang lebih kuat dan informasi awan titik 3D sebagai arah kerja berikutnya.
