# Neural Radiance Fields for Plot-level Cotton Crop Three-dimensional Reconstruction and Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jiang2025neural` |
| Judul asli | Neural Radiance Fields for Plot-level Cotton Crop Three-dimensional Reconstruction and Yield Estimation |
| Penulis | Jiang, Lizhi; Li, Changying; Chee, Peng W; Fu, Longsheng |
| Tahun | 2025 |
| Venue | 2025 Asabe Annual International Meeting |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [jiang2025neural.pdf](../pdf/jiang2025neural.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202500502

## Gambaran Umum
Makalah ini mengembangkan alur kerja berbasis *Neural Radiance Fields* (NeRF) untuk merekonstruksi tanaman kapas tingkat petak (*plot-level*) dalam 3D dan menghitung buah kapas (*boll*) per petak. Alurnya mencakup pengambilan citra RGB, rekonstruksi NeRF, anotasi masker 2D semiotomatis dengan *Segment Anything Model* (SAM), segmentasi buah dalam 3D dengan FruitNeRF, dan penghitungan dengan pengelompokan HDBSCAN. Naskah ini adalah makalah presentasi ASABE Annual International Meeting 2025 (Paper 2500502) yang tidak melalui telaah sejawat jurnal.

Data dikumpulkan pada 25 Oktober 2024 di Tifton, Georgia, Amerika Serikat, pada ladang berisi 160 petak dengan 32 genotipe. Dua cara akuisisi dibandingkan: robot beroda MARS dengan 10 kamera dan ponsel pintar pada penstabil genggam. Evaluasi hitungan dilakukan pada 10 petak dari data ponsel.

Hasil utama: untuk data ponsel, PSNR 16,21, SSIM 0,34, dan LPIPS 0,49 (tepatnya 16,2105; 0,3435; 0,4909 pada Tabel 2). Segmentasi 2D buah mencapai mAP50 0,845 pada data 2024 setelah *fine-tuning*. Galat persentase absolut rerata (MAPE) antara hitungan prediksi dan hitungan manual adalah 4,41% (R² = 0,94), dan MAPE terhadap berat buah sebenarnya 8,83% (R² = 0,92).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengumpulan data fenotipe kapas masih mengandalkan sampling manual di lapangan yang lambat, padat karya, dan rentan galat manusia. Buah kapas tersebar secara 3D pada tingkat petak, sehingga oklusi pada citra 2D menurunkan akurasi hitungan. Awan titik 3D mengurangi masalah oklusi, tetapi LiDAR terestrial mahal dan lambat, sedangkan kamera RGB-D memiliki resolusi terbatas untuk detail halus seperti cabang.

Rekonstruksi multipandang klasik (*Structure from Motion* dan *Multi-View Stereo*) sudah dipakai pada jagung dan kapas. NeRF telah dipakai pada tingkat petak untuk jagung dan stroberi, tetapi penulis menyatakan bentuk tanaman kapas dan sebaran buahnya lebih menantang sehingga kinerja NeRF pada skala petak kapas perlu divalidasi. Segmentasi langsung pada awan titik membutuhkan anotasi 3D yang mahal dan data langka; penulis memilih memetakan masker 2D ke ruang 3D.

## Ide Utama
Buah kapas disegmentasi pada citra 2D, lalu masker dipetakan ke medan radiansi 3D sehingga identitas buah yang tampak pada banyak citra menyatu dalam satu representasi 3D. Awan titik buah yang dihasilkan dikelompokkan dengan HDBSCAN; satu klaster dihitung satu buah. Dengan cara ini tidak perlu anotasi 3D. Anotasi 2D dipercepat dengan SAM yang diberi kotak pembatas hasil detektor YOLOv11x sebagai *prompt*.

## Cara Kerja Langkah demi Langkah

```
 Video (robot / ponsel) -> bingkai -> COLMAP -> Nerfacto (NeRF) -> FruitNeRF (+ masker 2D YOLOv11x)
                                                                      -> awan titik buah -> HDBSCAN -> hitungan
```

### 1. Akuisisi data
Ladang terdiri atas 160 petak, 32 genotipe (satu genotipe per petak), jarak baris 6 kaki, jarak kolom 25 kaki, panjang petak sekitar 18 kaki. Defoliant diaplikasikan seminggu sebelum pengambilan data, sehingga sebagian petak hampir tanpa daun dan sebagian masih berdaun. Hampir semua buah sudah membuka; sedikit buah hijau yang belum matang dikecualikan dari pengukuran hasil. Data uji diambil dari baris pertama, kedua, dan ketujuh.

Metode pertama memakai robot MARS dengan 10 kamera: lima Fuji X-A10 (1920×1080) dan lima Lumix DMC-G7 (3840×2160), semuanya 30 bingkai per detik; sekitar 40 detik per petak. Metode kedua memakai ponsel pada penstabil genggam, video 3840×2160 pada 30 bingkai per detik, memindai tampak atas dan samping pada tiga ketinggian (atas, tengah, bawah); sekitar 130 detik per petak.

### 2. Rekonstruksi NeRF
Bingkai distandarkan ke 1920×1080. Dari video multikamera diambil sekitar 90 bingkai per video, dari video ponsel 500 bingkai, dengan tumpang tindih lebih dari 90%. COLMAP mengestimasi parameter kamera dan awan titik jarang. Rekonstruksi memakai Nerfstudio versi 1.1.4 dengan model Nerfacto, 30.000 iterasi per adegan.

### 3. Anotasi masker 2D dengan SAM
Detektor YOLOv11x dilatih pada dataset deteksi buah kapas tahun 2022 (tampak atas), lalu memprediksi kotak pada data baru 2024. Kotak dipakai sebagai *prompt* SAM untuk menghasilkan masker; untuk data 2022 dipakai kotak anotasi manual. Masker diperbaiki manual di Roboflow karena masker tidak lengkap bila buah terhalang batang atau cabang. Dataset akhir (Tabel 1): data 2022 berisi 606 citra latih dan 260 validasi; data 2024 berisi 98 citra latih dan 27 validasi. Model segmentasi YOLOv11x dilatih pada data 2022, lalu di-*fine-tune* pada data 2024 (ukuran masukan 1280×1280, *batch* 8, 300 *epoch*).

### 4. FruitNeRF dan penghitungan
FruitNeRF menambah medan semantik (MLP 3 lapis, 128 neuron tersembunyi) pada medan densitas dan penampakan NeRF, dilatih dengan citra RGB dan masker biner buah. Awan titik buah diekspor dengan 3.000 sinar per *batch* dan 6.000 titik sampel per sisi kotak adegan, lalu dipotong manual ke satu petak. HDBSCAN dengan `min_cluster_size` 20 dan `min_samples` 5 (nilai empiris) mengelompokkan titik; jumlah klaster adalah hitungan buah. Pelatihan memakai satu GPU NVIDIA DGX A100 80 GB di klaster HiPerGator.

## Eksperimen dan Hasil
Kualitas rekonstruksi diukur dengan PSNR, SSIM, dan LPIPS pada 10 petak representatif; hitungan diukur dengan RMSE, MAE, dan MAPE.

Rekonstruksi NeRF (Tabel 2):

| Konfigurasi | PSNR | SSIM | LPIPS |
|---|---|---|---|
| 10 kamera | 14,5190 | 0,3766 | 0,6915 |
| 5 kamera Lumix | 17,2100 | 0,4883 | 0,5435 |
| 5 kamera Fuji | 14,6100 | 0,3186 | 0,6314 |
| Ponsel | 16,2105 | 0,3435 | 0,4909 |

Penulis menyimpulkan data ponsel dan lima Lumix lebih baik daripada lima Fuji dan sepuluh kamera campuran, dan tidak menyarankan memakai kamera berjenis berbeda karena perbedaan warna sensor merusak awan titik. Pengujian hitungan hanya memakai data ponsel karena ponsel memindai tampak atas dan dua sisi, sedangkan lima Lumix hanya tampak atas dan satu sisi; pengujian hitungan dari data Lumix dijadwalkan sebagai pekerjaan lanjutan.

Segmentasi 2D (Tabel 3):

| Data | P | R | mAP50 | mAP50-95 |
|---|---|---|---|---|
| 2022 | 0,732 | 0,661 | 0,728 | 0,428 |
| 2024 (setelah *fine-tuning*) | 0,812 | 0,778 | 0,845 | 0,548 |

Model yang hanya dilatih pada data 2022 mencapai mAP50 72,8% pada data 2024, naik menjadi 84,5% setelah *fine-tuning* (makalah menyebut peningkatan 11,7%). Penulis memperkirakan waktu anotasi per citra turun paling sedikit 50% (perkiraan kasar, bukan pengukuran formal).

Hitungan dan hasil: pada 10 petak, hitungan prediksi berkorelasi dengan hitungan manual (R² = 0,94, MAPE 4,41%); regresi antara jumlah prediksi dan berat sebenarnya memberi R² = 0,92 dengan galat 8,83% dan galat berat rerata per petak kurang dari 130 gram. Nilai RMSE dan MAE hitungan didefinisikan pada makalah, tetapi tidak dilaporkan nilainya dalam teks.

## Kelebihan dan Keterbatasan
Kelebihan: tidak memerlukan anotasi 3D; anotasi 2D dipercepat dengan SAM; pengambilan dengan ponsel berbiaya rendah; hitungan akurat pada dua jenis petak (tanpa daun dan berdaun).

Keterbatasan yang dinyatakan penulis: HDBSCAN dapat menggabungkan dua buah yang berdekatan atau terhalang sebagian menjadi satu klaster sehingga hitungan sedikit diremehkan; masker SAM tidak lengkap pada buah yang terhalang batang atau cabang sehingga perlu koreksi manual; buah dari petak sebelah kadang tersegmentasi sehingga harus disaring manual; penulis berencana menguji lebih banyak data petak untuk menilai ketangguhan.

Menurut pembacaan ringkasan ini, evaluasi hitungan hanya mencakup 10 petak dari satu hari pengambilan dan satu ladang, sehingga akurasi 4,41% belum menunjukkan generalisasi. Kebun juga telah di-*defoliasi*, dan buah belum matang dikecualikan. Pemotongan awan titik per petak dilakukan manual, sedangkan waktu komputasi NeRF per petak tidak dilaporkan. Ukuran data uji segmentasi 2D hanya 27 citra validasi untuk data 2024.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali melalui rekonstruksi 3D: citra dari banyak sudut (ratusan bingkai per petak) disatukan dalam satu medan radiansi dengan pose kamera dari COLMAP, dan masker 2D dari tiap citra dipetakan ke medan semantik 3D. Identitas buah ditentukan oleh posisi 3D (klaster HDBSCAN), bukan oleh pencocokan antarcitra. Kegagalan yang dilaporkan adalah penggabungan buah yang berdekatan dalam satu klaster.

Hitungan tidak dilaporkan per kelas; hanya satu kelas buah kapas (buah terbuka). Acuan hitungnya adalah hitungan manual per petak (10 petak) dan berat panen buah per petak yang ditimbang. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: pemetaan masker 2D ke ruang 3D agar satu tandan dari beberapa sisi menjadi satu objek, serta dua acuan (hitungan dan berat). Keterbatasan: pendekatan ini memerlukan rekonstruksi menyeluruh dengan tumpang tindih tinggi dan pose kamera yang andal, sedangkan citra sawit multi-sisi relatif jarang antarsisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `jiang2025neural`.

Jiang dkk. (2025, makalah presentasi ASABE) memadukan rekonstruksi NeRF (Nerfacto), anotasi masker 2D semiotomatis berbasis SAM dan YOLOv11x, segmentasi buah 3D dengan FruitNeRF, dan pengelompokan HDBSCAN untuk menghitung buah kapas per petak. Pada 10 petak dari data ponsel, MAPE hitungan terhadap hitungan manual 4,41% (R² = 0,94) dan MAPE terhadap berat buah 8,83% (R² = 0,92); mAP50 segmentasi 2D pada data 2024 adalah 0,845.

Catatan verifikasi data: Angka rekonstruksi ada pada Tabel 2, segmentasi 2D pada Tabel 3, ukuran dataset pada Tabel 1, dan hasil hitungan pada seksi 3.3 serta Gambar 9; angka abstrak (PSNR 16,21, SSIM 0,34, LPIPS 0,49, mAP50 0,85, MAPE 4,41% dan 8,83%) sesuai teks, dengan mAP50 0,85 pembulatan dari 0,845. Tidak ada tabel hitungan per petak; nilai hitungan dan berat tiap petak ada hanya pada Gambar 9 yang tidak terbaca dari teks, sehingga RMSE dan MAE tidak dapat diverifikasi. Seksi 3.1 menyebut ada 10 petak untuk rerata rekonstruksi dan seksi 3.3 menyebut 10 petak untuk hitungan; tidak dinyatakan apakah kedua himpunan itu sama. Tidak ada keterangan jumlah buah total. Makalah bukan artikel jurnal bertelaah sejawat.
