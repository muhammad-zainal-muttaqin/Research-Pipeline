# Citrus yield estimation for individual trees integrating pruning intensity and image views

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2024citrus` |
| Judul asli | Citrus yield estimation for individual trees integrating pruning intensity and image views |
| Penulis | Zhu, Yihang; Liu, Feng; Zhao, Yiying; Gu, Qing; Zhang, Xiaobin |
| Tahun | 2024 |
| Venue | European Journal of Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhu2024citrus.pdf](../pdf/zhu2024citrus.pdf)
- DOI resmi: https://doi.org/10.1016/j.eja.2024.127349

## Gambaran Umum
Makalah ini (*European Journal of Agronomy* 161, 2024) memperkirakan hasil panen jeruk per pohon dari citra tanah dengan dua tahap: detektor buah berbasis pembelajaran mendalam menghitung buah pada citra pohon, lalu model *machine learning* memetakan hitungan itu ke jumlah buah sebenarnya per pohon. Faktor yang dikaji adalah intensitas pemangkasan (tanpa pemangkasan, 0–5%, 5–10%, dan 10–15% tunas baru) dan jumlah pandangan citra per pohon (dua, empat, dan enam).

Data berupa 1.200 citra pohon jeruk Miyagawa (*Citrus unshiu* Marc. 'Miyagawa wase') dari 100 pohon (25 pohon per tingkat pemangkasan) di kebun Institute of Citrus Fruit, Taizhou, Tiongkok. Detektor berbasis YOLOv6 mencapai F1 tertinggi 0,958 pada ambang keyakinan 0,8 dengan augmentasi. Model XGBoost memberi galat terendah: MAPE 0,171 dan SMAPE 0,153 pada data uji. Kondisi optimal menurut penulis adalah dua, empat, dan enam pandangan untuk pohon yang dipangkas >10%, 5–10%, dan ≤5%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil per pohon berbasis citra bergantung pada hubungan antara buah yang terdeteksi dan buah yang sebenarnya ada. Penulis mengutip bahwa hanya 70–85% buah tampak pada citra kanopi, dan proporsi itu dipengaruhi arsitektur kanopi, pemangkasan, dan sudut kamera. Pemangkasan mengubah proporsi buah yang tertutup, sedangkan jumlah dan posisi pengambilan citra memengaruhi visibilitas buah. Penulis menyatakan dampak praktik pengelolaan seperti pemangkasan terhadap akurasi deteksi belum banyak dikaji.

## Ide Utama
Gagasan utamanya adalah memperlakukan hitungan deteksi sebagai satu variabel masukan, bukan hasil akhir, lalu mengoreksinya dengan model *machine learning* yang juga memakai intensitas pemangkasan dan jumlah pandangan sebagai variabel. Dengan cara ini, bias hitung (kurang hitung akibat oklusi atau lebih hitung akibat tambahan pandangan) dipelajari dari data. Penulis juga menyimpulkan bahwa jumlah pandangan yang tepat bergantung pada tingkat pemangkasan, bukan semakin banyak semakin baik.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Pohon ditanam di blok kebun terpisah (jarak lebih dari 50 m) menurut perlakuan. Citra diambil dari tanah dengan jarak kamera ke kanopi sekitar 0,75 m, bidang pandang sekitar 77,38° dan ukuran citra sekitar 1216 × 2160 piksel (potret). Tiga skema pandangan: dua pandangan (rotasi 180°, tegak lurus arah baris), empat pandangan (tiap 90°), dan enam pandangan (tiap 60°). Total 1.200 citra (4 intensitas × 25 pohon × (2+4+6) citra per pohon). Hanya buah pada pohon latar depan yang diberi label. Pelabelan dan augmentasi memakai EasyDAM_V2. Pembagian data adalah 70% latih dan 30% uji; augmentasi (rotasi, pencerminan, perubahan skala, *blur* Gaussian) pada data latih menghasilkan 100.800 citra berlabel.

### 2. Deteksi buah
Tiga detektor dibandingkan: Faster R-CNN (dengan FPN dan RPN yang ditingkatkan), YOLOv5 (varian terkecil, tulang punggung CSPDarkNet, leher PAN), dan YOLOv6 (varian terkecil, EfficientRep, Rep-PAN). Pelatihan 88 *epoch*, ukuran *batch* dua, pengoptimal Adam (β1 = 0,900, β2 = 0,999, ε = 10⁻⁸). Metrik: presisi, *recall*, dan F1.

### 3. Hitungan per pohon
Hitungan deteksi pada semua pandangan satu pohon dijumlahkan menjadi hitungan pohon itu. Tidak ada mekanisme untuk mengenali buah yang sama pada pandangan berbeda; buah dihitung per citra lalu dijumlah.

### 4. Estimasi hasil dengan *machine learning*
Algoritma Boruta menguji pentingnya variabel (hitungan buah, pemangkasan, jumlah pandangan, tinggi dan lebar pohon). Empat model dilatih: *random forest* (RF), SVM (kernel RBF dan polinomial), XGBoost, dan *generalized linear model* (GLM) sebagai pembanding. Penyetelan parameter dengan *grid* dan validasi silang 10 lipatan (lima pengulangan). Variabel terikat adalah hitungan manual buah per pohon. Metrik: PE, MAPE, SMAPE, dan R². Analisis memakai R 4.2.1.

## Eksperimen dan Hasil
F1 detektor (ambang 0,8, data diaugmentasi, Tabel 3): YOLOv6 0,958, Faster R-CNN 0,947, YOLOv5 0,915. Augmentasi menaikkan F1 sebesar 16,48%, 13,74%, dan 9,99% pada Faster R-CNN, YOLOv5, dan YOLOv6. Waktu prediksi dengan data augmentasi (ms per citra): Faster R-CNN 107,85 ± 5,42, YOLOv5 70,56 ± 2,56, YOLOv6 75,96 ± 3,08.

Hitungan YOLOv6 terhadap hitungan sebenarnya: dengan dua pandangan, hitungan umumnya lebih rendah daripada jumlah sebenarnya dan galat membesar dengan jumlah buah; dengan empat pandangan dan pemangkasan 0–10%, R² > 0,94 dan SMAPE < 0,15; dengan enam pandangan SMAPE > 0,24 dan sebagian besar pohon terhitung berlebih. Perbedaan galat menurut jumlah pandangan dan menurut pemangkasan signifikan (ANOVA, p < 0,01). Pohon tanpa pemangkasan menghasilkan galat hitung besar.

Pentingnya variabel (penurunan akurasi pada GLM): hitungan buah 27,94%, pemangkasan 24,93%, jumlah pandangan 22,12%, tinggi pohon 5,39%, lebar pohon 4,93%.

Tabel 4: galat estimasi hasil dengan parameter optimal.

| Model | MAPE latih | SMAPE latih | MAPE uji | SMAPE uji |
|---|---|---|---|---|
| XGBoost | 0,007 | 0,005 | 0,171 | 0,153 |
| RF | 0,083 | 0,086 | 0,190 | 0,194 |
| SVM (RBF) | 0,152 | 0,155 | 0,218 | 0,183 |
| SVM (POLY) | 0,511 | 0,252 | 0,552 | 0,241 |
| GLM | 0,597 | 0,409 | 0,706 | 0,478 |

SVM (RBF) memiliki selisih galat latih-uji terkecil. Menurut penulis, galat paling rendah pada empat pandangan untuk semua model. Pada pohon tanpa pemangkasan, galat estimasi ketiga model melebihi 0,18 pada dua dan empat pandangan. Rekomendasi akhir: XGBoost terbaik untuk pohon tanpa pemangkasan dan ≤5% dengan enam pandangan, 5–10% dengan empat pandangan, dan 10–15% dengan dua pandangan.

## Kelebihan dan Keterbatasan
Kelebihan: desain faktorial yang memisahkan pengaruh pemangkasan dan jumlah pandangan; acuan hitungan manual per pohon; pembanding GLM; pelaporan galat latih dan uji.

Keterbatasan yang dinyatakan penulis: generalisasi terbatas karena satu kultivar dan satu lokasi; ketergantungan pada citra tanah; keterwakilan dataset; faktor lain seperti kualitas tanah dan hama tidak diperhitungkan; tata letak baris yang rapat menyulitkan pencitraan tanah dan memerlukan lensa lebar.

Menurut pembacaan ringkasan ini, pohon dipotret hanya dari sisi yang berbeda tanpa pencocokan buah antar-citra, sehingga lebih hitung pada enam pandangan diatasi secara statistik, bukan dengan identitas buah. Menurut pembacaan ringkasan ini, makalah tidak menyebut jumlah pohon pada pembagian latih dan uji untuk model estimasi hasil, sehingga kemungkinan kebocoran antar-citra satu pohon tidak dapat dinilai dari teks. Hitungan manual per pohon disebut sebagai acuan tanpa uraian prosedur rinci.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang dapat tampak pada lebih dari satu pandangan dengan cara statistik: hitungan per pandangan dijumlahkan, lalu model XGBoost, RF, atau SVM mengoreksinya menggunakan jumlah pandangan dan pemangkasan sebagai variabel. Tidak ada pencocokan identitas buah lintas pandangan. Penulis menyatakan bahwa penambahan pandangan menyebabkan hitungan berlebih (*overcounting*) pada enam pandangan, yang berarti hitungan ganda terjadi dan tidak dihilangkan secara eksplisit.

Hitungan tidak dilaporkan per kelas (satu kelas, buah jeruk). Acuan hitungnya adalah hitungan manual buah per pohon di lapangan. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pendekatan koreksi hitungan oleh regresi dengan jumlah pandangan sebagai variabel, serta temuan bahwa menambah sisi tidak selalu menurunkan galat bila tidak ada pemadanan identitas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhu2024citrus`.

Zhu dkk. memperkirakan hasil jeruk per pohon dengan menghitung buah memakai detektor YOLOv6 (F1 0,958 pada ambang 0,8) pada citra tanah dengan dua, empat, atau enam pandangan per pohon, lalu mengoreksi hitungan dengan model *machine learning*. XGBoost memberi galat uji terendah (MAPE 0,171; SMAPE 0,153), dan jumlah pandangan optimal bergantung pada intensitas pemangkasan, dengan lebih hitung pada enam pandangan.

Catatan verifikasi data: F1 dan waktu prediksi ada pada Tabel 3; galat estimasi pada Tabel 4; pentingnya variabel pada Bagian 3.2; desain data pada Bagian 2.1 sampai 2.2. Teks mencantumkan "Fast R-CNN" pada Tabel 2 sementara model lain disebut Faster R-CNN, yang tampak sebagai salah ketik. Nilai R² dan SMAPE per kombinasi pemangkasan dan pandangan hanya tampil pada Gambar 2 dan Gambar 4 dan disebut di teks secara garis besar. Jumlah pohon pada set uji, serta nilai F1 dengan ambang selain yang disebut, tidak dapat diverifikasi lebih jauh dari teks.
