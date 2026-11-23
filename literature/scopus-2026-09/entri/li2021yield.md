# Yield Estimation Method of Apple Tree Based on Improved Lightweight YOLOv5

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2021yield` |
| Judul asli | Yield Estimation Method of Apple Tree Based on Improved Lightweight YOLOv5 |
| Penulis | Zhijun, LI; Shenghui, YANG; Shi, Deshuai; Liu, Xingxing; Zheng, Yongjun |
| Tahun | 2021 |
| Venue | Smart Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, other berries |

## Tautan Akses
- PDF: [li2021yield.pdf](../pdf/li2021yield.pdf)
- DOI resmi: https://doi.org/10.12133/j.smartag.2021.3.2.202105-sa005

## Gambaran Umum

Kajian ini menaksir hasil panen per pohon apel dari citra. Buah dideteksi dengan YOLOv5 yang diringankan, lalu jumlah buah dan luas total kotak deteksi menjadi masukan jaringan saraf BP (*backpropagation*, jaringan saraf berlapis penuh yang dilatih dengan perambatan balik galat) yang mengeluarkan hasil panen pohon dalam kilogram. Teks yang tersedia adalah terjemahan mesin berbahasa Inggris dari *postprint* di ChinaXiv. Tabel tidak ikut diterjemahkan, sehingga hanya angka yang disebut dalam teks yang dapat diperiksa.

Citra diambil di kebun apel "Yanfu No. 3" di Qixia, Yantai, Shandong, Tiongkok, antara 3 dan 17 Oktober 2020. Wahananya drone quadrotor buatan sendiri dengan Raspberry Pi 4B dan kamera Raspberry Pi Camera V2 (bidang pandang 65°). Drone terbang pada ketinggian 1,5 m, berjarak 1,2 m dari pohon, dan membawa kain putih 4 m × 3 m sebagai latar di belakang pohon. Citra juga diambil tanpa kain putih. Pengambilan dilakukan pada hari ke-1, ke-8, dan ke-15 sesudah kantong buah dilepas, dengan cahaya dari depan, samping, dan belakang. Setiap tahap warna menyisakan 1.000 citra sesudah citra ganda dan citra tanpa buah dibuang. Uji 1 berisi 300 citra berlatar kain putih (100 per arah cahaya), dan uji 2 berisi 300 citra tanpa kain putih. Sisanya menjadi data latih. Pembagian per pohon tidak disebut. Kotak buah diberi label dengan LabelImg.

Hasil panen diperoleh dengan memetik dan menimbang semua apel setiap pohon pada 18 Oktober 2020. Dari 93 pohon, 60 dipakai melatih jaringan BP, 13 mengujinya, 10 memvalidasi model dengan kain putih, dan 10 tanpa kain putih. Rerata berat buah 250–280 g.

Konvolusi standar YOLOv5 diganti konvolusi terpisah per kanal (*depthwise separable convolution*), yaitu konvolusi yang memisahkan penapisan tiap kanal dari penggabungan antarkanal sehingga parameternya lebih sedikit. Modul perhatian PBAM (*pooling block attention module*) ditambahkan untuk memberi bobot pada kanal fitur. Jaringan BP memakai tiga lapisan berlapis penuh, dua masukan (jumlah buah dan luas kotak), dan satu keluaran (hasil panen). Jarak kamera dan parameter kamera dibuat tetap karena luas kotak bergantung padanya.

Penggantian konvolusi mempercepat deteksi 11,26–17,28%, dan gabungan kedua perubahan mempercepatnya paling banyak 15,37% (31,44 ms per citra). mAP YOLOv5 awal adalah 89,83%, 90,75%, 92,07%, dan 93,44% untuk varian s, m, l, dan x. Dengan kedua perubahan, YOLOv5x mencapai 96,27%. Pada uji berlatar kain putih, mAP tertinggi 96,79% pada data hari ke-15 dengan cahaya samping, dan reratanya 93,30% pada semua data uji. Cahaya dari belakang memberi hasil terburuk, dan buah hari ke-1 yang masih kehijauan lebih sulit dideteksi. Tanpa kain putih, mAP turun pada semua tahap warna. Angka tabelnya tidak tersedia dalam terjemahan.

Jaringan BP mencapai R² 0,7967 pada data latih dan 0,7982 pada 13 pohon uji. RMSE-nya 1,5317 kg dan 1,4021 kg, MAE 1,1259 kg dan 1,0253 kg, dan MAPE 6,34% dan 6,25%. Pada 10 pohon validasi berlatar kain putih, galat relatif taksiran hasil berkisar −6,13% sampai 3,05%. Pada 10 pohon tanpa kain putih, kisarannya −12,71% sampai 8,28%. Penulis menyebut buah dari pohon di belakang ikut terdeteksi dan dihitung sebagai buah pohon yang dipotret.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Hitungan buah dari citra tidak dibandingkan dengan hitung tangan, sehingga galat hitungnya tidak dilaporkan; yang dievaluasi hanya hasil panen dalam kilogram. Teks tidak menyebut berapa citra dipakai untuk satu pohon atau apakah buah yang terlihat di beberapa citra digabung. Validasi hasil panen hanya 10 pohon per kondisi latar, dari satu kebun, satu kultivar, dan satu musim. Pembagian citra latih dan uji tidak disebut per pohon. Teksnya terjemahan mesin, dan tabel hasil deteksi tidak tersedia.
