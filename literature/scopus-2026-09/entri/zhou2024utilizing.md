# Utilizing NeRF-Based Rays for Spatial Perception in Fruit Counting Deduplication

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2024utilizing` |
| Judul asli | Utilizing NeRF-Based Rays for Spatial Perception in Fruit Counting Deduplication |
| Penulis | Zhou, Chong; Xu, Fei; Huang, Ansheng; Wang, Chenhuizi; Zhang, Wenli |
| Tahun | 2024 |
| Venue | Proceedings 2024 International Symposium on Internet of Things and Smart Cities Isitsc 2024 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhou2024utilizing.pdf](../pdf/zhou2024utilizing.pdf)
- DOI resmi: https://doi.org/10.1109/isitsc64373.2024.00013

## Gambaran Umum
Makalah konferensi ini (*International Symposium on Internet of Things and Smart Cities*, ISITSC 2024) mengusulkan penghitungan buah jeruk pada satu pohon dengan menggabungkan deteksi 2D (YOLOv8) dan rekonstruksi 3D berbasis *Neural Radiance Fields* (NeRF). Video pohon direkonstruksi dengan instant-ngp (parameter kamera awal dari COLMAP), sudut pandang dirancang ulang pada model 3D, dan kotak pembatas jeruk dari YOLOv8 diubah menjadi sinar (*ray*) 3D. Titik 3D yang dihasilkan dikelompokkan dengan DBSCAN untuk menghapus duplikasi, dan jumlah klaster menjadi hitungan buah.

Pengujian memakai sepuluh video satu pohon jeruk simulasi dengan sebaran buah yang berbeda-beda. Metode YOLOv8+NeRF mencapai MAE 1,5 jeruk, MSE 2,5, MAPE 9,375%, dan akurasi estimasi 90,625%, dibandingkan YOLOv8+Botsort (MAE 4,4; akurasi 72,5%) dan YOLOv8+Bytetrack (MAE 3,6; akurasi 77,5%).

Perlu dicatat bahwa evaluasi dilakukan pada satu pohon simulasi dengan sepuluh konfigurasi buah, bukan pada kebun nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan jeruk secara manual tidak efisien, mahal, dan rawan galat. Metode berbasis penglihatan komputer 2D kesulitan pada buah yang terhalang daun dan sering menghitung ganda karena buah yang sama muncul pada beberapa bingkai, sebab metode itu tidak mampu membedakan hubungan spasial antarbuah. Metode 3D langsung (seperti NeRF-RPN dan NeRF-Det) memerlukan sumber daya komputasi besar dan data 3D beranotasi yang sulit dikumpulkan di pertanian. Penulis menyimpulkan bahwa penggabungan 2D dan 3D untuk menghitung buah per pohon dan menangani hitungan berulang masih perlu dikaji.

## Ide Utama
Pohon direkonstruksi dalam ruang NeRF sehingga setiap piksel pada citra yang dirender dapat dipetakan menjadi sinar 3D. Untuk setiap kotak jeruk dari detektor 2D, sinar dari kamera melalui piksel itu dipakai untuk menghitung posisi 3D buah. Karena buah yang sama diamati dari beberapa sudut, titik 3D dari pengamatan berbeda jatuh berdekatan di ruang yang sama dan digabung oleh pengelompokan berbasis kepadatan. Jumlah klaster setara dengan jumlah buah unik.

Sudut pandang juga dapat direncanakan ulang setelah rekonstruksi (sejajar mata, miring ke atas, dan dari atas) untuk meminimalkan oklusi daun, sehingga tuntutan sudut pengambilan di lapangan berkurang.

## Cara Kerja Langkah demi Langkah
```
 [Video] -> [COLMAP] -> [instant-ngp NeRF] -> [Pandang ulang] -> [YOLOv8]
                                                                    |
 [Jumlah buah] <- [DBSCAN] <- [Titik 3D = kamera + kedalaman x sinar] <-+
```

### 1. Akuisisi data
Dataset rekonstruksi 3D berasal dari satu pohon jeruk simulasi dengan sebaran buah yang diubah sebelum perekaman. Perekaman dengan kamera lensa tunggal secara memutar miring dan dari atas dengan kecepatan konstan. Sepuluh set video dengan sebaran buah berbeda dikumpulkan. Jenis kamera, kultivar, dan lokasi tidak dilaporkan.

### 2. Rekonstruksi 3D
COLMAP mengekstraksi dan mencocokkan fitur untuk mendapatkan parameter kamera awal, yang diberikan ke instant-ngp (pengodean hash multi-resolusi) untuk membangun ruang NeRF. instant-ngp memangkas area secara otomatis berdasarkan kubus satuan agar hanya pohon yang dipertahankan. Sudut pandang direncanakan ulang (tiga sudut di atas), tanpa tumpang tindih titik awal dan akhir lintasan.

### 3. Deteksi 2D
YOLOv8 dilatih pada "2D Recognition Dataset" (citra dari beragam kebun): 4.800 citra latih, 400 validasi, 150 uji. Praproses: koreksi orientasi, perubahan ukuran menjadi 1280 × 1280 piksel dengan bantalan pantulan (*reflection padding*), augmentasi saturasi (-40% sampai +40%) dan eksposur (-20% sampai +20%) yang menghasilkan tiga varian per sampel, serta pembersihan anotasi agar tidak mencakup daun. Pelatihan memakai strategi multi-skala.

### 4. Pemetaan 3D memakai sinar
Fungsi `pixel_to_ray_pinhole` pada instant-ngp memetakan piksel kotak pembatas ke arah sinar dengan model kamera lubang jarum: $\mathrm{dir} = ((x - x_0)/f_x,\ (y - y_0)/f_y,\ 1)$. Posisi 3D dihitung sebagai $\mathrm{Orange} = \mathrm{Camera} + \mathrm{Depth} \times \mathrm{Ray}$, dengan kedalaman dari instant-ngp, lalu digeser dengan langkah 0,03 (radius rata-rata jeruk dalam ruang NeRF) sepanjang sinar dari permukaan menuju inti.

### 5. Pengelompokan dengan DBSCAN
Titik 3D dikelompokkan dengan DBSCAN: $\mathrm{eps} = 0{,}03$ (radius jeruk) dan $\mathrm{minPoints} = 3$ (perkiraan jumlah pengamatan per jeruk). Titik derau dibuang dan setiap klaster dihitung sebagai satu buah.

## Eksperimen dan Hasil
Metode diuji pada dataset rekonstruksi 3D (sepuluh pohon simulasi dengan sebaran buah berbeda). Untuk pembanding 2D, video dirender dari model hasil rekonstruksi dengan lintasan lingkar 45 derajat dari atas, sebab pelacakan 2D langsung pada video asli akan menghasilkan hitungan ganda berat akibat perekaman mengelilingi pohon berulang kali. Pembanding adalah YOLOv8+Botsort dan YOLOv8+Bytetrack. Acuan adalah hitungan manual jumlah buah pada pohon. Lingkungan: AMD Ryzen 7800X3D, GPU RTX 4070Ti, Python 3.9, CUDA 11.5. Metrik: MAE, MSE, MAPE, dan akurasi estimasi $1 - \sum|y_i - \hat y_i| / \sum y_i$.

| Metode | MAE | MSE | MAPE | Akurasi |
|---|---|---|---|---|
| YOLOv8+Botsort | 4,4 | 20,4 | 27,5% | 72,5% |
| YOLOv8+Bytetrack | 3,6 | 14 | 22,5% | 77,5% |
| YOLOv8+NeRF | 1,5 | 2,5 | 9,375% | 90,625% |

Penulis menyimpulkan bahwa YOLOv8+NeRF unggul pada semua metrik karena memakai pemetaan koordinat 3D untuk menghitung tiap buah, sedangkan pelacak 2D hanya mengandalkan lintasan objek yang rawan duplikasi. Metrik detektor (mAP, presisi, recall) pada set uji 150 citra tidak dilaporkan, dan hitungan per pohon tidak dirinci.

## Kelebihan dan Keterbatasan
Keterbatasan yang dinyatakan penulis: pemodelan NeRF-RPN dan NeRF-Det dalam literatur memerlukan banyak sumber daya dan data; rencana lanjutan mencakup adaptasi ke buah lain (apel, pir, aprikot) dengan mengganti bobot YOLOv8, NeRF dinamis untuk buah yang bergerak atau tumbuh, dan efisiensi waktu nyata.

Menurut pembacaan ringkasan ini, keterbatasan lain meliputi: (1) evaluasi hanya pada satu pohon simulasi dengan sepuluh konfigurasi buah, bukan kebun nyata; (2) perbandingan tidak setara, karena metode NeRF dievaluasi pada video rekonstruksi 3D sedangkan pelacak 2D pada video render dari model yang sama dengan lintasan khusus, dan skenario pembanding ditentukan penulis; (3) tidak ada simpangan baku atau uji signifikansi, dan jumlah buah per pohon tidak dilaporkan; (4) hasil bergantung pada rekonstruksi NeRF yang baik, yang memerlukan pose kamera yang akurat dan pohon yang statis; (5) parameter DBSCAN (eps 0,03; minPoints 3) diatur pada skala ruang NeRF dan belum diuji sensitivitasnya.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme rekonstruksi 3D (NeRF) dan proyeksi sinar dari kotak deteksi 2D; titik 3D dari berbagai sudut digabung dengan pengelompokan DBSCAN berbasis jarak. Identitas tidak dijaga dengan kemiripan tampilan. Hitungan tidak dilaporkan per kelas; hanya jumlah total jeruk per pohon. Acuannya adalah hitungan manual pada pohon simulasi, bukan panen.

Untuk pencacahan tandan sawit multi-sisi, yang dapat dipindahkan adalah gagasan memetakan deteksi 2D dari banyak sudut ke ruang 3D bersama dan menggabungkan titik yang berdekatan, serta perencanaan sudut pandang ulang pada model 3D. Syaratnya adalah rekonstruksi 3D pohon yang andal (video mengelilingi pohon, parameter kamera dari COLMAP); pada pohon sawit yang tinggi dan lebat dengan citra tetap dari beberapa sisi, kelayakan ini belum ditunjukkan makalah. Per kelas dapat diperlakukan dengan pelabelan klaster oleh kelas kotak, tetapi hal itu tidak diuji di sini.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhou2024utilizing`.

Zhou dkk. menggabungkan deteksi YOLOv8 dengan rekonstruksi NeRF (instant-ngp) untuk menghitung jeruk pada satu pohon: kotak deteksi diubah menjadi sinar 3D, posisi buah dihitung dari kedalaman sepanjang sinar, dan duplikasi dihapus dengan DBSCAN. Pada sepuluh pohon jeruk simulasi, metode ini mencapai MAE 1,5 dan akurasi 90,625%, dibandingkan akurasi 72,5% (Botsort) dan 77,5% (Bytetrack) untuk pelacak 2D.

Catatan verifikasi data: Angka hasil (MAE, MSE, MAPE, akurasi) ada pada Tabel II di akhir teks (tabel terbaca dari teks ekstraksi yang berurutan dan kolomnya konsisten dengan teks seksi III-C dan abstrak). Ukuran dataset 2D (4.800/400/150) ada pada seksi III-A-1; sepuluh set video pada seksi III-A-2; parameter DBSCAN dan langkah 0,03 pada seksi II-B. Jenis kultivar, jumlah citra atau bingkai dataset 3D, serta jumlah buah acuan tidak dilaporkan. Teks ekstraksi baik, termasuk catatan pengunduhan IEEE yang tidak memengaruhi isi.
