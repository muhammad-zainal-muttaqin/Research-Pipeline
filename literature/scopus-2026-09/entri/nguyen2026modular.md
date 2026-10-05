# A Modular UAV-Based Framework for Apple Detection and Yield Extrapolation from 3D Point Clouds

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nguyen2026modular` |
| Judul asli | A Modular UAV-Based Framework for Apple Detection and Yield Extrapolation from 3D Point Clouds |
| Penulis | Nguyen, Kenny; Patel, Dhruv J.; Nguyen, Tony; Tran, Nathan; Riazi, Amin; Lauer, J. Wesley; Bae, Wan D.; Alkobaisi, Shayma |
| Tahun | 2026 |
| Venue | Proceedings of the ACM Symposium on Applied Computing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [nguyen2026modular.pdf](../pdf/nguyen2026modular.pdf)
- DOI resmi: https://doi.org/10.1145/3748522.3779768

## Gambaran Umum
Makalah ini mengusulkan kerangka modular untuk mendeteksi, mencacah, dan memperkirakan hasil panen apel dari awan titik 3D (*point cloud*) yang direkonstruksi dari citra *unoccupied aerial vehicle* (UAV). Kerangka itu terdiri atas penyaringan warna (HSV dan ExR–LAB), regresi untuk estimasi jumlah apel, pengelompokan spasial DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*), dan pendekatan geometris (kotak pembatas minimum, bola, elipsoid) untuk validasi serta pemodelan volume.

Data berasal dari satu kebun apel Fuji komersial di Amerika Serikat, dipotret dengan DJI Mavic 3M pada 1 September 2024. Evaluasi memakai 50 potongan awan titik (*section*) dengan acuan "kebenaran virtual", yaitu hitungan manual empat penilai pada visualisasi awan titik, total 759 apel pada area 339,49 m². Bukan hitungan panen.

Hasil utamanya: regresi pada jumlah titik merah mencapai $R^2$ sekitar 0,99 dan galat relatif (*relative error*, RE) paling rendah 0,022; pengelompokan DBSCAN dengan validasi geometris hanya mencapai $R^2$ 0,58–0,75 dan RE terbaik 0,21, tetapi memberi lokasi dan ukuran tiap buah. Penulis menggabungkan keduanya menjadi strategi hibrida. Estimasi massa panen tidak divalidasi terhadap berat panen.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil buah secara manual memerlukan banyak tenaga. Citra UAV 2D menghadapi oklusi, buah bergerombol, variasi pencahayaan, dan latar yang ramai oleh daun serta struktur kebun. Pendekatan 2D juga sering memerlukan target kalibrasi atau isyarat kedalaman. Penginderaan 3D dari darat lebih akurat secara spasial, tetapi menurut penulis memakan waktu, padat karya, dan sulit diperluas ke kebun komersial. Detektor 2D seperti YOLO dibatasi oleh data berlabel yang kebanyakan berupa citra daun dari permukaan tanah.

Penulis juga mencatat bahwa pekerjaan terdahulu yang memakai HSV, DBSCAN, dan pemisahan klaster kedua dengan K-means sangat peka terhadap hiperparameter, sehingga peningkatan kinerjanya sulit ditunjukkan secara konsisten.

## Ide Utama
Awan titik padat dari UAV memuat banyak titik untuk tiap buah. Tantangannya adalah menyaring titik non-buah dan memperkirakan jumlah serta ukuran buah meskipun sebagian buah tidak terselesaikan sepenuhnya. Penulis memadukan dua strategi yang saling melengkapi: regresi dari jumlah titik merah ke jumlah apel (akurat, tetapi hanya memberi hitungan global), dan pengelompokan dengan pendekatan objek geometris (kurang akurat, tetapi memberi lokalisasi dan morfologi tiap buah). Hitungan dari regresi dikombinasikan dengan rerata volume dan massa per apel dari pengelompokan untuk ekstrapolasi hasil panen.

## Cara Kerja Langkah demi Langkah

```
 Citra UAV -> Photogrammetry -> Awan titik 3D -> Filter warna (HSV / ExR-LAB)
                                                        |
                                  +---------------------+---------------------+
                                  v                                           v
                      Regresi (jumlah titik merah)              DBSCAN + validasi geometris
                                  |                                           |
                                  |                       volume per apel (bola / elipsoid)
                                  +---------------------+---------------------+
                                                        v
                                         Hitungan + massa tingkat bagian/lahan
```

### 1. Akuisisi data
Lokasi adalah kebun apel Fuji komersial dengan sistem penopang berbentuk V (*V-shaped trellis*). Citra diambil dengan DJI Mavic 3M pada tiga ketinggian dan sudut: dua penerbangan pada ketinggian 12 m (satu nadir, satu miring 80° dari horizontal), citra tambahan manual pada 2–3 m di atas kanopi dengan sudut miring 45°, dan citra darat dengan UAV dibawa berjalan sekitar 1 m di atas tanah menghadap kiri dan kanan secara bergantian. Resolusi tanah penerbangan 12 m adalah 0,55 cm. Penerbangan 30 m (sudut miring 75°, resolusi piksel 1,4 cm) hanya untuk ortofoto dan tidak dipakai pada rekonstruksi awan titik. Lahan studi berukuran 33,1 m × 60,98 m (2.023,32 m²). Dataset pemodelan terdiri atas 50 potongan awan titik yang meliputi 339,49 m², yaitu 16,8% dari lahan.

Ukuran apel diukur lapangan pada 47 apel dalam segmen baris sekitar 15 m, pada ketinggian sekitar 2–2,6 m: lebar rerata 6,7 cm (SD 0,9 cm) dan tinggi rerata 7,1 cm (SD 1,0 cm). Angka ini menjadi acuan batas geometris.

### 2. Pembangunan awan titik 3D
Rekonstruksi memakai Agisoft Metashape Professional (versi 2.1.2.18548) dari 80 citra JPEG. Penyejajaran memakai akurasi "Highest" dengan batas titik kunci 40.000 dan titik ikat 4.000, menghasilkan awan jarang 63.212 titik ikat. Rekonstruksi padat pada kualitas "Ultra High" dengan penyaringan kedalaman "Moderate" menghasilkan model sekitar 2,59 juta titik. Proyek dirujuk ke WGS 84 dan koordinat diproyeksikan ulang ke sistem metrik lokal sebelum operasi berbasis metrik.

### 3. Penyaringan warna
Dua metode dipakai. Penyaringan HSV mempertahankan lebih banyak kandidat kulit apel, tetapi menyertakan lebih banyak positif palsu dari daun dan cabang. Penyaringan ExR–LAB (indeks *Excess Red* lalu batasan ruang warna LAB) lebih selektif dan menghasilkan titik lebih sedikit. Parameter pada Tabel 1: HSV dengan H < 0,10 atau H > 0,96, S 0,20–0,80, V 0,50–1,00; ExR–LAB dengan ambang merah 0,20 dan a* 10–60.

### 4. Estimasi jumlah dan deteksi
Regresi memakai satu prediktor, yaitu jumlah titik merah hasil penyaringan per bagian. Model yang diuji: *decision tree* (DT), *random forest* (RF), *K-nearest neighbor* (KNN), *gradient boosting* (GB), dan jaringan saraf (NN), dengan pemisahan latih-uji 70/30 pada tingkat bagian dan *seed* 42.

Pengelompokan memakai DBSCAN dengan $\varepsilon$ = 0,028 dan MIN_SAMPLES = 136. Tiap klaster didekati dengan kotak pembatas minimum (*minimum bounding box*, MBB) dan diterima bila rasio sisi terkecil terhadap sisi terbesar paling sedikit 0,50 dan diagonal ruang $D$ berada dalam 4–20 cm. Satu klaster yang diterima dihitung sebagai satu apel. Tiga konfigurasi: M1 (HSV + DBSCAN + MBB), M2 (HSV + DBSCAN + bola), dan M3 (ExR–LAB + DBSCAN + bola).

### 5. Volume dan massa
Setiap MBB yang diterima didekati dengan bola (jari-jari 3–10 cm) atau elipsoid prolat dengan faktor pemanjangan $\alpha \in [1{,}1;\ 1{,}2]$. Volume dijumlahkan per bagian, diskalakan ke lahan dengan rasio cakupan, lalu dikalikan densitas apel 850–950 kg/m³ yang dikutip dari pustaka lain. Rasio cakupan yang dipakai adalah rasio titik merah HSV 18,23%.

## Eksperimen dan Hasil
Semua model dievaluasi terhadap 759 apel hasil hitungan manual pada 50 bagian. Perangkat lunak: Python 3.9.13, Open3D, scikit-learn, dan TensorFlow. Kode dan data dinyatakan tersedia di repositori publik.

Penyaringan warna (Tabel 2): pada lahan penuh (260.430.642 titik) HSV menyisakan 2.593.894 titik merah dan ExR–LAB 589.343. Pada bagian sampel (52.402.836 titik) HSV menyisakan 473.065 titik dan ExR–LAB 145.552.

Regresi (Tabel 3):

| Filter | Model | RE | RMSE | $R^2$ |
|---|---|---|---|---|
| HSV | DT | 0,036 | 1,133 | 0,969 |
| HSV | RF | 0,033 | 0,744 | 0,988 |
| HSV | KNN | 0,106 | 2,155 | 0,898 |
| HSV | GB | 0,036 | 1,093 | 0,974 |
| HSV | NN | 0,022 | 0,417 | 0,996 |
| ExR–LAB | DT | 0,062 | 1,186 | 0,961 |
| ExR–LAB | RF | 0,060 | 1,260 | 0,967 |
| ExR–LAB | KNN | 0,151 | 2,293 | 0,892 |
| ExR–LAB | GB | 0,053 | 1,278 | 0,966 |
| ExR–LAB | NN | 0,026 | 0,350 | 0,997 |

Pengelompokan (Tabel 5):

| Model | RE | RMSE | $R^2$ | Apel terestimasi pada 50 bagian (kebenaran 759) | Apel terestimasi pada lahan |
|---|---|---|---|---|---|
| M1 (HSV, DBSCAN, MBB) | 0,21 | 3,49 | 0,75 | 698 (RE = 0,0804) | 3.828 |
| M2 (HSV, DBSCAN, bola) | 0,23 | 4,08 | 0,66 | 657 (RE = 0,1344) | 3.603 |
| M3 (ExR–LAB, DBSCAN, bola) | 0,22 | 4,64 | 0,58 | 694 (RE = 0,0856) | 2.809 |

Dimensi MBB (Tabel 4): klaster yang diterima memiliki $D$ rerata 6,0 cm; klaster yang ditolak karena di bawah ambang memiliki $D$ rerata 3,6 cm dan yang di atas ambang 35,9 cm.

Massa (Tabel 6): pada bagian sampel, M1 dengan bola menghasilkan volume 0,0428 m³ dan massa 36,38–40,66 kg, sedangkan elipsoid 0,0573 m³ dan 48,71–54,44 kg. Gabungan regresi (NN) dan rerata volume M1 menghasilkan 38,67–43,22 kg (bola) dan 51,78–57,87 kg (elipsoid). Pada ekstrapolasi lahan, M1 dengan elipsoid menghasilkan 0,3143 m³ dan 257,73–298,59 kg; hibrida regresi dengan bola dan elipsoid menghasilkan 0,2918 m³ dan 248,03–277,21 kg, serta dengan elipsoid saja 0,3340 m³ dan 283,90–317,30 kg. Teks menyebut MBB memberi total yang membengkak (141–158 kg pada bagian sampel). Tidak ada berat panen sebagai pembanding.

## Kelebihan dan Keterbatasan
Kelebihan: kerangka modular yang kodenya terbuka; regresi sangat akurat terhadap hitungan acuan; pengelompokan memberi lokasi dan ukuran tiap buah; penyaringan MBB menolak klaster yang terlalu kecil atau terlalu besar.

Keterbatasan yang dinyatakan penulis: oklusi tetap menjadi masalah pada kanopi rapat; hitungan manual dapat meremehkan jumlah apel sebenarnya, terutama apel hijau atau tertutup sebagian; klaster besar yang menggabungkan beberapa apel ditolak sehingga tidak terhitung; pemisahan klaster kedua dengan K-means pada uji awal sedikit memperbaiki M3 tetapi menurunkan akurasi M1 dan M2; estimasi volume dan massa belum divalidasi dengan data panen sehingga hanya bersifat indikatif.

Menurut pembacaan ringkasan ini, regresi hanya memakai satu prediktor, dan model dilatih serta diuji pada satu kebun, satu tanggal, dan satu kultivar dengan 50 bagian (pemisahan 70/30 berarti sekitar 15 bagian uji, angka ini dihitung dari proporsi dan tidak dinyatakan langsung). Karena itu generalisasi tidak teruji. Acuan berupa hitungan visual pada awan titik yang sama dengan masukan model, sehingga apel yang tidak tampak di awan titik tidak terwakili. Hiperparameter disetel secara empiris pada data yang sama.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani identitas lintas pandang sebagai masalah tersendiri. Citra dari banyak sudut (nadir, miring, dan darat) digabung oleh rekonstruksi fotogrametri menjadi satu awan titik, sehingga satu buah yang terlihat dari beberapa citra secara implisit menjadi satu klaster titik 3D. Mekanismenya adalah rekonstruksi 3D diikuti pengelompokan DBSCAN dan validasi MBB. Tidak ada pencocokan atau pelacakan eksplisit antarcitra dan tidak ada penanganan identitas objek per citra.

Hitungan tidak dilaporkan per kelas; apel dihitung sebagai satu kelas. Acuan hitungnya adalah anotasi manual pada awan titik 3D (759 apel), bukan panen atau hitungan lapangan; penulis menyatakan tidak ada data berat panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: gagasan menyatukan banyak pandang di ruang 3D agar satu objek menjadi satu klaster, penyaringan klaster dengan batas ukuran dari pengukuran lapangan, serta pemisahan antara penghitung berbasis regresi dan penghitung berbasis objek. Keterbatasan: pendekatan ini bergantung pada warna merah sebagai penciri dan tidak menangani buah beragam kelas kematangan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `nguyen2026modular`.

Nguyen dkk. (2026) mengusulkan kerangka UAV modular yang membangun awan titik 3D dari citra, menyaring titik merah (HSV atau ExR–LAB), memperkirakan jumlah apel dengan regresi, dan melokalisasi tiap apel dengan DBSCAN yang divalidasi kotak pembatas minimum, bola, atau elipsoid. Pada 50 bagian kebun apel Fuji dengan acuan 759 apel hasil hitungan manual pada awan titik, regresi mencapai $R^2$ sekitar 0,99 (RE terbaik 0,022), sedangkan pengelompokan mencapai $R^2$ 0,58–0,75 (RE terbaik 0,21). Estimasi massa panen belum divalidasi terhadap berat panen.

Catatan verifikasi data: Angka regresi ada pada Tabel 3, angka pengelompokan dan estimasi apel pada Tabel 5, dimensi MBB pada Tabel 4, penyaringan warna pada Tabel 2, volume dan massa pada Tabel 6, parameter pada Tabel 1, serta rincian data pada seksi 4.1 dan 3.2. Teks ekstraksi memuat tabel dalam bentuk satu nilai per baris tetapi masih dapat dibaca. Ada ketidakselarasan internal: Tabel 2 menulis 24,70% untuk ExR–LAB, sedangkan catatan Tabel 5 dan seksi 4.5 menulis 24,60%. Teks menyebut RE klaster "sekitar 0,21" dan RE per jumlah total (mis. 0,0804) sebagai dua ukuran yang berbeda; definisi tepatnya hanya dijelaskan sebagai rerata persentase galat absolut pada bagian uji. Ukuran jumlah bagian uji tidak dinyatakan. Kebenaran lapangan berupa berat panen tidak tersedia.
