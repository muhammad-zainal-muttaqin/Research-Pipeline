# Comparative analysis of single-view and multiple-view data collection strategies for detecting partially-occluded grape bunches: Field trials

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arizasentis2025comparative` |
| Judul asli | Comparative analysis of single-view and multiple-view data collection strategies for detecting partially-occluded grape bunches: Field trials |
| Penulis | Ariza-Sent\'\is, Mar; Baja, Hilmy; V\'elez, Sergio; van Essen, Rick; Valente, Jo\~ao |
| Tahun | 2025 |
| Venue | Journal of Agriculture and Food Research |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [arizasentis2025comparative.pdf](../pdf/arizasentis2025comparative.pdf)
- DOI resmi: https://doi.org/10.1016/j.jafr.2025.101736

## Gambaran Umum
Makalah ini membandingkan dua strategi pengambilan data video untuk mendeteksi dan melacak tandan anggur yang sebagian tertutup daun: pendekatan satu pandang (*single-view*), yaitu merekam sisi kanopi dengan UAV tanpa perlakuan khusus, dan pendekatan multi-pandang (*multiple-view*) dengan tiga perspektif (depan, kiri, kanan) untuk mengurangi oklusi. Uji lapangan dilakukan di kebun anggur komersial tanpa pemangkasan daun, dengan UAV DJI Phantom 4 RTK pada ketinggian 3 m dari permukaan tanah, pada 19 sampai 20 September 2023. Algoritma *PointTrack* dilatih dan divalidasi dengan anotasi gaya pelacakan dan segmentasi multi-objek (*Multiple-Object Tracking and Segmentation*, MOTS) pada 5.958 bingkai beranotasi.

Hasil utama adalah rasio antara tandan terlacak dan tandan acuan (*ground truth*, GT) sebesar 74% untuk multi-pandang dan 23% untuk satu pandang. Fenotipe tandan (panjang dan lebar, kode OIV 202 dan 203, dalam piksel) menunjukkan $R^2$ 0,53 dan RMSE 19,13 untuk multi-pandang, dibandingkan $R^2$ 0,39 dan RMSE 28,05 untuk satu pandang. Penulis juga menyatakan bahwa pelacakan multi-pandang terganggu oleh kabur gerak (*motion blur*) akibat gerakan UAV.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan dan fenotipe tandan anggur penting untuk pemantauan mutu, kesehatan, dan estimasi hasil. Oklusi oleh daun dan cabang menyebabkan penghitungan terlalu rendah atau terlalu tinggi. Buah yang tertutup penuh tidak terlihat dari sudut mana pun, sedangkan buah yang tertutup sebagian dapat terlihat lebih baik dari sudut tertentu. Pendekatan bola (*spherical shape prior*) dan lokalisasi 3D yang dikutip penulis hanya diuji pada buah bulat, sehingga tidak cocok untuk tandan anggur.

Sebagian besar penelitian terdahulu berfokus pada pemrosesan data, sedangkan makalah ini berfokus pada tahap pengambilan data. Penelitian ini menguji secara empiris kerangka teoretis pengambilan citra multi-pandang oleh UAV yang diusulkan penulis dalam makalah sebelumnya.

## Ide Utama
Kualitas deteksi dan pelacakan dapat ditingkatkan dengan merencanakan sudut pandang saat pengambilan data, bukan hanya memperbaiki algoritma. Tandan yang tertutup pada satu sudut dapat terlihat dari sudut lain, dan tandan yang terlihat penuh pada setidaknya satu dari tiga pandangan menghasilkan topeng bentuk yang lebih akurat. Untuk fenotipe, pandangan terbaik (kabur paling sedikit, oklusi paling rendah, kontras terbaik) dipilih bila tandan terlihat penuh dari ketiga pandangan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Dua metodologi menghasilkan video MP4. Satu pandang merekam sisi kanopi tanpa perbaikan, serupa dengan penelitian sebelumnya. Multi-pandang merekam dari tiga perspektif dengan rute yang direncanakan khusus untuk tanaman berkayu. UAV yang sama (DJI Phantom 4 RTK dengan sensor terintegrasi) dipakai pada kedua metode dengan kecepatan tidak stabil antara 0,1 dan 1 m/s. Kondisi cerah dan kecepatan angin di bawah 0,5 m/s. Tidak dilaporkan: jumlah pohon atau baris dan kultivar anggur selain bahwa tandan putih berbaur dengan kanopi hijau.

### 2. Anotasi
Video dibersihkan dan 5.958 bingkai dianotasi secara manual dengan CVAT dalam format MOTS (berkas PNG dan teks dengan label tandan). Tandan yang muncul kembali setelah menghilang beberapa bingkai mempertahankan ID yang sama. Penulis menyatakan anotasi dengan lintasan terputus menghasilkan metrik pelacakan lebih rendah. Set data tersedia untuk umum (GrapeMOTS).

### 3. PointTrack
Model *Spatial Embeddings* dilatih dengan pembelajaran transfer (*transfer learning*), pengoptimal Adam dengan laju belajar $5 \times 10^{-5}$ dan laju penyetelan halus $5 \times 10^{-6}$, ukuran batch 20, dan 1.200 epoch. Potongan citra berorientasi vertikal berukuran 256 x 512 piksel untuk pelatihan awal dan 512 x 1024 piksel untuk penyetelan halus. Komponen pelacakan dilatih dengan batch 32 dan 100 epoch.

### 4. Skema uji coba
Tiga uji coba dibandingkan: Uji coba 1 melatih algoritma hanya dengan data multi-pandang, Uji coba 2 hanya dengan data satu pandang, dan Uji coba 3 dengan gabungan keduanya. Setiap uji coba dievaluasi pada 5 video: video 1 dan 2 adalah satu pandang, video 3 sampai 5 adalah multi-pandang.

### 5. Metrik
Metrik mencakup MOTSP, MODSP, MOTSA, sMOTSA, dan MODSA, dengan TP bila IoU di atas 0,5 dan galat pergantian ID (IDS) dikurangkan. Nilai dapat negatif bila positif palsu banyak. Hitungan total per video dibandingkan dengan hitungan dari anotasi, dan fenotipe dibandingkan dengan 10 tandan (ukuran sampel sesuai pedoman OIV).

## Eksperimen dan Hasil
Hasil lengkap per video tersaji pada Tabel 1 dan sebagian dikutip di sini (sMOTSA, MOTSA, MODSA):

| Uji coba | Video | Kategori | sMOTSA | MOTSA | MODSA |
|---|---|---|---|---|---|
| 2 (hanya satu pandang) | 2 | Satu pandang | -0,08 | -0,08 | -0,08 |
| 3 (gabungan) | 4 | Multi-pandang | -1,35 | 0,3 | 0,68 |
| 3 (gabungan) | 5 | Multi-pandang | 0,69 | 3,44 | 3,84 |
| 1 (hanya multi-pandang) | 3 | Multi-pandang | -16,21 | -12,92 | -11,08 |

Penulis menyatakan bahwa Uji coba 2 memberi metrik tertinggi untuk data satu pandang (sMOTSA, MOTSA, dan MODSA sama dengan -0,08) dan Uji coba 3 memberi metrik tertinggi untuk data multi-pandang (semua nilai positif pada beberapa video, MOTSA hingga 3,84 menurut abstrak). Nilai negatif muncul karena positif palsu. Abstrak menyebut rentang metrik multi-pandang dari -1,35 sampai 3,84.

Ringkasan komparatif lain:

| Ukuran | Satu pandang | Multi-pandang |
|---|---|---|
| Rasio tandan terlacak terhadap GT | 13% sampai 23% | 27% sampai 74% |
| $R^2$ fenotipe (panjang dan lebar) | 0,39 | 0,53 |
| RMSE fenotipe (piksel) | 28,05 | 19,13 |

Rasio tertinggi tercatat pada uji coba kedua menurut bagian diskusi, sedangkan kesimpulan menyebut 74% untuk multi-pandang dan 23% untuk satu pandang. Hitungan pada Gambar 4 umumnya bernilai negatif, yaitu penghitungan lebih rendah dari acuan, tetapi lebih dekat ke acuan pada multi-pandang. Pada pelacakan tiga pandangan, kabur gerak membuat kamera kehilangan jejak buah dan mengganggu kontinuitas ID, terutama pada tandan 5, 6, dan 7.

## Kelebihan dan Keterbatasan
Kelebihan: perbandingan langsung dua strategi akuisisi pada kebun komersial dengan kondisi oklusi daun, set data MOTS yang tersedia untuk umum, dan penggunaan UAV terjangkau dengan sensor terintegrasi untuk reproduksibilitas.

Keterbatasan yang dinyatakan penulis: tandan putih homogen dengan kanopi hijau dan pencahayaan sulit sehingga pelabelan menyulitkan; mengenali tandan yang sama pada sudut pandang berbeda saat anotasi video multi-pandang sulit; positif palsu akibat kemiripan warna dan variasi pencahayaan; kabur gerak pada pelacakan multi-pandang; perlunya perluasan ke lintang, varietas (termasuk anggur merah), dan buah lain.

Menurut pembacaan ringkasan ini, sebagian besar metrik pelacakan bernilai negatif sehingga kinerja absolut algoritma rendah, dan klaim keunggulan multi-pandang bertumpu pada rasio terlacak dan fenotipe yang dihitung pada hanya 5 video dan 10 tandan. Menurut pembacaan ringkasan ini pula, makalah tidak menjelaskan bagaimana tandan yang sama antar tiga pandangan digabung menjadi satu identitas dalam hitungan akhir, sehingga selisih hitungan tidak dapat dipisahkan dari efek identitas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam arti pengambilan multi-pandang untuk mengatasi oklusi, dengan pelacakan video (*PointTrack* dengan ID yang dipertahankan) pada rekaman UAV. Mekanisme penyatuan identitas antar-pandangan tidak diuraikan; hitungan dibandingkan dengan anotasi per video. Fokus makalah adalah visibilitas dan rasio terlacak, bukan koreksi duplikasi lintas pandang.

Hitungan tidak dilaporkan per kelas (satu kelas tandan anggur). Acuan hitung adalah anotasi pada video (hitungan dari anotasi), bukan panen. Yang dapat dipindahkan ke tandan kelapa sawit multi-sisi adalah bukti bahwa perencanaan sudut pandang meningkatkan rasio buah terlacak (23% menjadi 74%), pemilihan pandangan terbaik untuk pengukuran, dan catatan bahwa anotasi identitas lintas pandang sulit dilakukan. Keterbatasannya adalah rendahnya metrik pelacakan absolut dan tidak adanya mekanisme pencocokan antar-pandang yang eksplisit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `arizasentis2025comparative`.

Ariza-Sentís dkk. membandingkan pengambilan video UAV satu pandang dan tiga pandang pada kebun anggur komersial tanpa pemangkasan daun, memakai PointTrack dengan anotasi MOTS pada 5.958 bingkai. Rasio tandan terlacak terhadap acuan adalah 74% untuk multi-pandang dan 23% untuk satu pandang, dan korelasi dimensi tandan dengan acuan naik dari $R^2$ 0,39 menjadi 0,53 (RMSE 28,05 menjadi 19,13). Pelacakan multi-pandang terganggu oleh kabur gerak, dan sebagian besar metrik pelacakan bernilai negatif.

Catatan verifikasi data: rasio 74% dan 23%, $R^2$ 0,53 dan 0,39, serta RMSE 19,13 dan 28,05 terdapat pada abstrak, bagian 3.4, 4, dan 5. Nilai per video terdapat pada Tabel 1 (sebagian dikutip). Gambar 3, 4, dan 6 serta Tabel 2 berupa gambar sehingga tidak dapat dibaca dari teks. Terdapat ketidakjelasan: rasio 74% disebut sebagai nilai tertinggi pada uji coba kedua di bagian diskusi, sedangkan uji coba kedua dinyatakan hanya memakai data satu pandang di bagian 3; ringkasan ini tidak menafsirkan ketidaksesuaian tersebut. Jumlah tandan acuan, kultivar, dan jumlah baris tidak dilaporkan. Satuan fenotipe adalah piksel menurut teks.
