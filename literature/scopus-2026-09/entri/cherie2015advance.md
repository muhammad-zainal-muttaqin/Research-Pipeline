# Advance models for camera-vision based oil content prediction of intact oil palm fruits (Elaeis Guineensis Jacq) on trees with nondestructive evaluation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cherie2015advance` |
| Judul asli | Advance models for camera-vision based oil content prediction of intact oil palm fruits (Elaeis Guineensis Jacq) on trees with nondestructive evaluation |
| Penulis | Cherie, Dinah; Herodian, Sam; Mandang, Tineke; Ahmad, Usman |
| Tahun | 2015 |
| Venue | International Journal on Advanced Science Engineering and Information Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [cherie2015advance.pdf](../pdf/cherie2015advance.pdf)
- DOI resmi: https://doi.org/10.18517/ijaseit.5.4.542

## Gambaran Umum

Penelitian ini bertujuan mengembangkan cara penilaian kandungan minyak tandan buah segar (TBS) kelapa sawit yang masih menempel di pohon secara nondestruktif dan dari jarak jauh. Kematangan TBS menentukan hasil dan mutu minyak sawit mentah (CPO): tandan yang dipanen terlalu dini memberi rendemen rendah, sedangkan tandan yang terlalu matang menurunkan mutu karena minyak berubah menjadi asam lemak bebas. Praktik panen di perkebunan Indonesia sering memanen tandan belum matang karena pekerja dibayar borongan berdasarkan jumlah atau berat tandan. Penulis mengusulkan penggantian penilaian visual pekerja dengan sistem penglihatan mesin (*machine vision*) yang mampu mengamati TBS hingga jarak 15 m.

Pengambilan data dilakukan pada Mei 2013 di perkebunan PT Nirwana Alam Lestari, anak usaha PT Astra Agro Lestari, di Nanga Bulik, Pangkalan Bun, Kalimantan Tengah. Sampel berupa TBS kultivar Marihat dari pohon berusia delapan tahun; kematangan dinilai oleh panel tiga pengamat berdasarkan warna dan buah yang lepas. Citra direkam dengan kamera Canon EOS 60D beresolusi 16 megapiksel dan lensa zoom optik 30 kali dalam tiga ulangan, pada jarak 2, 7, 10, dan 15 m. Perekaman memakai tiga filter selektif spektrum, yaitu ultraviolet (280–380 nm), cahaya tampak (400–700 nm), dan inframerah (720–1100 nm), dengan lampu 600 W (6000 lux) dan 1000 W (10000 lux). Kandungan minyak mesokarp diukur di laboratorium dan berkisar 13–26% dari berat tandan.

Mekanisme prediksi memanfaatkan hubungan antara warna TBS dan kandungan minyak. Citra disegmentasi, lalu diekstrak 15 fitur warna: rata-rata R, G, B dan H, S, I; indeks R, G, B; serta enam rasio warna (R/G, R/B, G/B, G/R, B/R, B/G). Fitur itu menjadi masukan model jaringan saraf tiruan *multilayer perceptron* (MLP-ANN) yang dibangun di SPSS 20 dengan sepuluh lapis tersembunyi, fungsi aktivasi *hyperbolic tangent*, koreksi ε = 0,02, algoritma *scaled conjugate gradient*, dan *simulated annealing*. Data dibagi 70% untuk kalibrasi dan 30% untuk validasi, lalu dibuat 20 model, satu untuk setiap kombinasi spektrum, intensitas lampu, dan jarak. Penulis mendapati perubahan warna tajam saat kandungan minyak mencapai 21,6% (awal tahap pemasakan) dan 23,9% (tahap senescensi), tetapi hubungan warna dan minyak tidak dapat dinyatakan dengan regresi linier sederhana karena sampel berkandungan berbeda dapat memiliki warna yang sama.

Kinerja model dinyatakan dengan koefisien korelasi (R²) dan akar rata-rata kuadrat galat (RMSE), dihitung terhadap hasil laboratorium. Pada kalibrasi, seluruh model memperoleh R² di atas 0,99, dengan RMSE terendah 0,047 pada model Vis2 10 m dan 0,051 pada model UV 15 m. Pada validasi 30% data, hanya lima model yang dinyatakan valid, yaitu UV-15 m (R² = 0,962; RMSE = 2,385), UV-10 m (0,897; 3,707), UV-2 m (0,993; 2,868), Vis1-7 m (0,993; 3,795), dan IR1-10 m (0,401; 6,374). Model terbaik menurut penulis adalah Vis1-7 m, yaitu perekaman dengan cahaya tampak dan lampu 600 W dari jarak 7 m. Selisih RMSE dan R² antara kalibrasi dan validasi masih berada dalam batas toleransi (P < 0,05).

Penulis menyatakan jumlah sampel terbatas sehingga hanya lima dari 20 model yang dianggap valid. Kelima model menunjukkan perilaku *over-fit*: pada validasi, model UV-15 m dan UV-10 m memprediksi kandungan minyak di atas nilai aktual (*false-positive*), sedangkan IR1-10 m, Vis1-7 m, dan UV-2 m memprediksi di bawah nilai aktual (*true-negative*). Bias dan galat itu dikaitkan dengan sedikitnya sampel. Penulis juga mencatat bahwa korelasi warna dan kandungan minyak terlalu lemah untuk regresi sederhana, serta citra dari sampel berbeda dapat memiliki nilai warna identik meskipun kandungan minyak dan tahap perkembangannya berbeda.

